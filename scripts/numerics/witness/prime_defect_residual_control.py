"""Optimal-control style diagnostic for the Euler residual correction.

Start from the smooth PNT-density margin

    M_smooth = Winf - int_{log 2}^R 2 exp(U/2) T_U dU.

Partition [log 2, R] into cells around active prime-power logarithms and write
the exact smooth-to-discrete correction as

    M_discrete = M_smooth + sum_n (P_smooth_cell(n) - P_atom(n)).

This is a finite open-loop controller made of residual cells.  The script asks:

  * how much of the exact residual controller is needed to restore the
    positive cone along each shell edge?
  * which residual cells repair or harm the smooth bad direction?

Run:
    python3 -m scripts.numerics.witness.prime_defect_residual_control
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_atom_sensitivity import _prime_power_label
from .prime_defect_measure_surrogate import smooth_prime_operator
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points
from .prime_nested_cone import _orthogonal_shell


LOG2 = math.log(2.0)


def active_logs(ambient, right_gmax: float) -> list[tuple[int, float]]:
    return [
        (n, math.log(n))
        for n in sorted(ambient.atoms["zeta"])
        if math.log(n) < right_gmax
    ]


def cell_bounds(active: list[tuple[int, float]], right_gmax: float) -> dict[int, tuple[float, float]]:
    bounds = {}
    logs = [logn for _, logn in active]
    for i, (n, logn) in enumerate(active):
        lo = LOG2 if i == 0 else 0.5 * (logs[i - 1] + logn)
        hi = right_gmax if i == len(active) - 1 else 0.5 * (logn + logs[i + 1])
        bounds[n] = (lo, hi)
    return bounds


def smooth_cell_operator(ambient, lo: float, hi: float) -> np.ndarray:
    if hi <= lo:
        return np.zeros_like(ambient.gram["Winf"])
    return _sym(smooth_prime_operator(ambient, hi) - smooth_prime_operator(ambient, lo))


def residual_cells(ambient, right_gmax: float) -> dict[int, np.ndarray]:
    active = active_logs(ambient, right_gmax)
    bounds = cell_bounds(active, right_gmax)
    cells = {}
    for n, _ in active:
        lo, hi = bounds[n]
        cells[n] = _sym(smooth_cell_operator(ambient, lo, hi) - ambient.atoms["zeta"][n])
    return cells


def edge_basis(ambient, points, left: float, right: float) -> np.ndarray:
    left_basis = points[left]["basis"]
    shell = _orthogonal_shell(ambient, left_basis, points[right]["basis"])
    return np.column_stack([left_basis, shell])


def compressed_min(B: np.ndarray, M: np.ndarray) -> tuple[float, np.ndarray]:
    block = _sym(B.T @ M @ B)
    eigs, vecs = np.linalg.eigh(block)
    return float(eigs[0]), vecs[:, 0]


def threshold_lambda(smooth_block: np.ndarray, residual_block: np.ndarray,
                     tol: float = 1e-9) -> dict:
    grid = np.linspace(0.0, 1.0, 501)
    mins = []
    for lam in grid:
        eigs = np.linalg.eigvalsh(_sym(smooth_block + float(lam) * residual_block))
        mins.append(float(eigs[0]))
    first = next((i for i, val in enumerate(mins) if val > tol), None)
    if first is None:
        return {"found": False, "lambda": float("nan"), "grid_min": mins[-1]}
    if first == 0:
        return {"found": True, "lambda": 0.0, "grid_min": mins[0]}
    lo = float(grid[first - 1])
    hi = float(grid[first])
    for _ in range(40):
        mid = 0.5 * (lo + hi)
        val = float(np.linalg.eigvalsh(_sym(smooth_block + mid * residual_block))[0])
        if val > tol:
            hi = mid
        else:
            lo = mid
    val = float(np.linalg.eigvalsh(_sym(smooth_block + hi * residual_block))[0])
    return {"found": True, "lambda": hi, "grid_min": val}


def cell_rayleighs(ambient, B: np.ndarray, smooth_bad_vec: np.ndarray,
                   cells: dict[int, np.ndarray]) -> list[dict]:
    rows = []
    for n, cell in sorted(cells.items()):
        comp = _sym(B.T @ cell @ B)
        ray = float(smooth_bad_vec.T @ comp @ smooth_bad_vec)
        rows.append({
            "n": n,
            "label": _prime_power_label(n),
            "logn": math.log(n),
            "rayleigh": ray,
        })
    return rows


def edge_report(ambient, points, left: float, right: float) -> dict:
    B = edge_basis(ambient, points, left, right)
    cells = residual_cells(ambient, right)
    smooth = _sym(ambient.gram["Winf"] - smooth_prime_operator(ambient, right))
    residual = sum(cells.values(), np.zeros_like(smooth))
    discrete = _sym(smooth + residual)
    smooth_block = _sym(B.T @ smooth @ B)
    residual_block = _sym(B.T @ residual @ B)
    discrete_block = _sym(smooth_block + residual_block)
    smooth_eigs, smooth_vecs = np.linalg.eigh(smooth_block)
    smooth_min = float(smooth_eigs[0])
    smooth_bad = smooth_vecs[:, 0]
    discrete_min = float(np.linalg.eigvalsh(discrete_block)[0])
    threshold = threshold_lambda(smooth_block, residual_block)
    rays = cell_rayleighs(ambient, B, smooth_bad, cells)
    total_ray = sum(row["rayleigh"] for row in rays)
    return {
        "left": left,
        "right": right,
        "smooth_min": smooth_min,
        "discrete_min": discrete_min,
        "threshold": threshold,
        "rays": rays,
        "total_ray": float(total_ray),
    }


def _print_edge(report: dict, topn: int = 5) -> None:
    th = report["threshold"]
    th_text = "none" if not th["found"] else f"{th['lambda']:.4f}"
    print(f"\n[edge {report['left']:.2f}->{report['right']:.2f}] "
          f"smooth min {report['smooth_min']:+.3e}, "
          f"discrete min {report['discrete_min']:+.3e}, "
          f"lambda* {th_text}, "
          f"smooth-bad residual ray {report['total_ray']:+.3e}")
    repairs = sorted(report["rays"], key=lambda row: row["rayleigh"], reverse=True)[:topn]
    harms = sorted(report["rays"], key=lambda row: row["rayleigh"])[:topn]
    print("      strongest residual-cell repairs on smooth bad vector:")
    for row in repairs:
        print(f"        {row['label']:<4} U={row['logn']:.3f} ray={row['rayleigh']:+.3e}")
    print("      strongest residual-cell harms on smooth bad vector:")
    for row in harms:
        print(f"        {row['label']:<4} U={row['logn']:.3f} ray={row['rayleigh']:+.3e}")


def summary() -> dict:
    print("=" * 78)
    print("Optimal-control style residual-cell correction")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    print("\nInterpretation:")
    print("  * Along the exact residual-control path, passivity is restored only")
    print("    after a substantial fraction of the smooth-to-discrete correction.")
    print("  * Individual residual cells can repair or harm the smooth bad vector;")
    print("    the controller is an ordered arithmetic combination, not a local")
    print("    sign-definite feedback.")
    print("  * A true optimal-control proof should look for a storage/Riccati")
    print("    inequality for the full Euler residual system, not for isolated cells.")
    return reports


if __name__ == "__main__":
    summary()
