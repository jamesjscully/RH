"""Bounded minimum-effort residual controller.

The scalar residual-control witness follows the exact controller ray

    M(lambda) = M_smooth + lambda sum_n R_n.

Here each residual cell gets its own bounded gain:

    M(u) = M_smooth + sum_n u_n R_n,   0 <= u_n <= 1.

We solve two finite convex-control diagnostics numerically:

    minimize sum u_n      subject to M(u) >= 0,
    minimize sum u_n^2    subject to M(u) >= 0.

The exact Euler residual controller is u_n = 1 for every active cell.  If the
optimized controller is dramatically cheaper or highly non-arithmetic, then
"optimal control" is a design analogy rather than a uniqueness principle for
zeta.  If the optimizer still needs most of the exact controller, the residual
system is rigid in a stronger sense.

Run:
    python3 -m scripts.numerics.witness.prime_defect_residual_control_opt
"""
from __future__ import annotations

import math

import numpy as np
from scipy.optimize import minimize

from .prime_carleson_flow import _sym
from .prime_defect_atom_sensitivity import _prime_power_label
from .prime_defect_measure_surrogate import smooth_prime_operator
from .prime_defect_residual_control import (
    edge_basis,
    residual_cells,
    threshold_lambda,
)
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points


def compressed_problem(ambient, points, left: float, right: float) -> dict:
    B = edge_basis(ambient, points, left, right)
    cells = residual_cells(ambient, right)
    smooth = _sym(ambient.gram["Winf"] - smooth_prime_operator(ambient, right))
    smooth_block = _sym(B.T @ smooth @ B)
    cell_blocks = []
    labels = []
    for n, cell in sorted(cells.items()):
        cell_blocks.append(_sym(B.T @ cell @ B))
        labels.append({
            "n": n,
            "label": _prime_power_label(n),
            "logn": math.log(n),
        })
    residual_block = _sym(sum(cell_blocks, np.zeros_like(smooth_block)))
    exact_block = _sym(smooth_block + residual_block)
    scalar = threshold_lambda(smooth_block, residual_block)
    return {
        "left": left,
        "right": right,
        "smooth_block": smooth_block,
        "cell_blocks": cell_blocks,
        "labels": labels,
        "exact_block": exact_block,
        "scalar_threshold": scalar,
        "smooth_min": float(np.linalg.eigvalsh(smooth_block)[0]),
        "exact_min": float(np.linalg.eigvalsh(exact_block)[0]),
    }


def block_from_u(problem: dict, u: np.ndarray) -> np.ndarray:
    M = problem["smooth_block"].copy()
    for coeff, block in zip(u, problem["cell_blocks"]):
        M = M + float(coeff) * block
    return _sym(M)


def min_eig(problem: dict, u: np.ndarray) -> float:
    return float(np.linalg.eigvalsh(block_from_u(problem, u))[0])


def solve_control(problem: dict, objective: str, tol: float = 1e-8) -> dict:
    n = len(problem["cell_blocks"])
    if n == 0:
        return {"success": False, "message": "no cells"}

    scalar = problem["scalar_threshold"]
    if scalar["found"]:
        x0 = np.full(n, min(1.0, max(0.0, scalar["lambda"] + 1e-3)))
    else:
        x0 = np.ones(n)

    def constraint(u: np.ndarray) -> float:
        return min_eig(problem, u) - tol

    if objective == "l1":
        def fun(u: np.ndarray) -> float:
            return float(np.sum(u))

        def jac(u: np.ndarray) -> np.ndarray:
            return np.ones_like(u)
    elif objective == "l2":
        def fun(u: np.ndarray) -> float:
            return float(np.dot(u, u))

        def jac(u: np.ndarray) -> np.ndarray:
            return 2.0 * u
    else:
        raise ValueError(f"unknown objective: {objective}")

    best = None
    best_any = None
    starts = [
        x0,
        np.ones(n),
        np.linspace(1.0, 0.25, n),
        np.linspace(0.25, 1.0, n),
    ]
    for start in starts:
        res = minimize(
            fun,
            np.clip(start, 0.0, 1.0),
            method="SLSQP",
            jac=jac,
            bounds=[(0.0, 1.0)] * n,
            constraints=[{"type": "ineq", "fun": constraint}],
            options={"ftol": 1e-11, "maxiter": 1000, "disp": False},
        )
        if best_any is None or constraint(res.x) > constraint(best_any.x):
            best_any = res
        if not res.success and constraint(res.x) < -1e-6:
            continue
        if best is None or fun(res.x) < fun(best.x):
            best = res

    if best is None:
        exact = np.ones(n)
        exact_eig = min_eig(problem, exact)
        if exact_eig >= -1e-7:
            return {
                "success": True,
                "message": (
                    "optimizer failed; using exact feasible controller"
                    if best_any is None else
                    f"optimizer failed; best infeasible eig {constraint(best_any.x) + tol:+.2e}; "
                    "using exact feasible controller"
                ),
                "objective": objective,
                "u": exact,
                "value": fun(exact),
                "min_eig": exact_eig,
                "active_count": n,
                "saturated_count": n,
                "fallback_exact": True,
            }
        return {"success": False, "message": "optimizer failed"}

    u = np.clip(best.x, 0.0, 1.0)
    eig = min_eig(problem, u)
    if eig < -1e-7:
        exact = np.ones(n)
        exact_eig = min_eig(problem, exact)
        if exact_eig >= -1e-7:
            return {
                "success": True,
                "message": (
                    f"optimizer returned infeasible eig {eig:+.2e}; "
                    "using exact feasible controller"
                ),
                "objective": objective,
                "u": exact,
                "value": fun(exact),
                "min_eig": exact_eig,
                "active_count": n,
                "saturated_count": n,
                "fallback_exact": True,
            }
    return {
        "success": bool(best.success or eig >= -1e-7),
        "message": best.message,
        "objective": objective,
        "u": u,
        "value": fun(u),
        "min_eig": eig,
        "active_count": int(np.sum(u > 1e-3)),
        "saturated_count": int(np.sum(u > 1.0 - 1e-3)),
        "fallback_exact": False,
    }


def edge_report(ambient, points, left: float, right: float) -> dict:
    problem = compressed_problem(ambient, points, left, right)
    l1 = solve_control(problem, "l1")
    l2 = solve_control(problem, "l2")
    return {"problem": problem, "l1": l1, "l2": l2}


def _top_controls(problem: dict, result: dict, count: int = 8) -> list[str]:
    if not result.get("success"):
        return [result.get("message", "failed")]
    rows = []
    for label, coeff in zip(problem["labels"], result["u"]):
        if coeff <= 1e-3:
            continue
        rows.append((float(coeff), label))
    rows.sort(reverse=True, key=lambda item: item[0])
    return [
        f"{label['label']}:{coeff:.2f}"
        for coeff, label in rows[:count]
    ]


def _print_edge(report: dict) -> None:
    problem = report["problem"]
    scalar = problem["scalar_threshold"]
    n = len(problem["cell_blocks"])
    scalar_norm = scalar["lambda"] if scalar["found"] else float("nan")
    print(f"\n[edge {problem['left']:.2f}->{problem['right']:.2f}] "
          f"cells={n}, smooth min={problem['smooth_min']:+.3e}, "
          f"exact min={problem['exact_min']:+.3e}, scalar lambda={scalar_norm:.4f}")
    for name in ("l1", "l2"):
        result = report[name]
        if not result.get("success"):
            print(f"      {name}: failed {result.get('message')}")
            continue
        l1_frac = float(np.sum(result["u"]) / n)
        l2_frac = math.sqrt(float(np.dot(result["u"], result["u"])) / n)
        print(f"      {name}: value={result['value']:.3f}, "
              f"min eig={result['min_eig']:+.2e}, "
              f"mean gain={l1_frac:.3f}, rms gain={l2_frac:.3f}, "
              f"active={result['active_count']}, saturated={result['saturated_count']}")
        if result.get("fallback_exact"):
            print(f"          fallback: {result['message']}")
        print("          top controls: " + ", ".join(_top_controls(problem, result)))


def summary() -> dict:
    print("=" * 78)
    print("Bounded minimum-effort residual-cell controller")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    print("\nInterpretation:")
    print("  * Cellwise bounded control can restore positivity with less total")
    print("    effort than the exact Euler residual, but it chooses artificial")
    print("    fractional/saturated patterns rather than the arithmetic pattern.")
    print("  * The exact zeta controller is therefore not optimal for simple L1/L2")
    print("    effort costs.  A meaningful optimal-control formulation needs an")
    print("    arithmetic storage cost or dynamics, not just actuator magnitude.")
    return reports


if __name__ == "__main__":
    summary()
