"""Finite Riccati diagnostic for exact Euler residual cells.

The proof scaffold ``research/proof/05-finite-riccati-identity.md`` gives an
exact Schur update identity.  For a fixed old/shell splitting,

    S_+ = S + Q_E[X] - R^T A_+^{-1} R,

where ``S = D - C^T A^{-1} C`` is the Schur complement.

The correct nested coordinate keeps the old Euler history exact and compares
smooth-to-discrete only on the incoming interval:

    M_base = W_inf - P_exact(<L) - P_smooth([L,R]),
    M_discrete = M_base + sum_j E_j,
    E_j = P_smooth_cell(j) - P_atom(j).

The point is to separate the signed residual part ``Q`` from the negative
Riccati square.  A storage proof has to pay for both; scalar prefix eigenvalue
depths alone can miss the square.

Run:
    python3 -m scripts.numerics.witness.prime_defect_riccati_storage
"""
from __future__ import annotations

import argparse
import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_atom_sensitivity import _prime_power_label
from .prime_defect_measure_surrogate import smooth_prime_operator
from .prime_defect_residual_control import edge_basis, smooth_cell_operator
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points


TOL = 1e-10


def _blocks(block: np.ndarray, old_dim: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])
    return A, C, D


def _pos_part(M: np.ndarray) -> np.ndarray:
    if M.size == 0:
        return M.copy()
    eigs, vecs = np.linalg.eigh(_sym(M))
    return _sym(vecs @ np.diag(np.maximum(eigs, 0.0)) @ vecs.T)


def _neg_debt(M: np.ndarray) -> np.ndarray:
    """Smallest PSD debt D with M + D >= 0."""
    if M.size == 0:
        return M.copy()
    eigs, vecs = np.linalg.eigh(_sym(M))
    return _sym(vecs @ np.diag(np.maximum(-eigs, 0.0)) @ vecs.T)


def _min_eig(M: np.ndarray) -> float:
    if M.size == 0:
        return float("nan")
    return float(np.linalg.eigvalsh(_sym(M))[0])


def _max_eig(M: np.ndarray) -> float:
    if M.size == 0:
        return float("nan")
    return float(np.linalg.eigvalsh(_sym(M))[-1])


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def _mode_atoms(ambient, mode: str) -> dict[int, np.ndarray]:
    if mode == "zeta":
        return ambient.atoms["zeta"]
    if mode == "DH":
        return ambient.atoms["DH"]
    if mode == "primes":
        return {n: atom for n, atom in ambient.atoms["zeta"].items() if _is_prime(n)}
    if mode == "powers":
        return {n: atom for n, atom in ambient.atoms["zeta"].items() if not _is_prime(n)}
    if mode == "smooth":
        return {}
    raise ValueError(f"unknown Riccati storage mode: {mode!r}")


def _label_for_n(n: int) -> str:
    return "smooth-gap" if n < 0 else _prime_power_label(n)


def _min_pair(M: np.ndarray) -> tuple[float, np.ndarray]:
    if M.size == 0:
        return float("nan"), np.zeros(0)
    eigs, vecs = np.linalg.eigh(_sym(M))
    return float(eigs[0]), vecs[:, 0]


def _schur(block: np.ndarray, old_dim: int) -> dict:
    A, C, D = _blocks(block, old_dim)
    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    if (not A.size) or A_eigs[0] <= TOL * max(1.0, float(np.max(np.abs(A_eigs)))):
        return {
            "valid": False,
            "A_min": float(A_eigs[0]),
            "schur": np.full_like(D, np.nan),
            "schur_min": float("nan"),
        }
    schur = _sym(D - C.T @ np.linalg.solve(A, C))
    return {
        "valid": True,
        "A_min": float(A_eigs[0]),
        "schur": schur,
        "schur_min": float(np.linalg.eigvalsh(schur)[0]) if schur.size else float("nan"),
    }


def strict_suffix_certificate(increments: list[np.ndarray], S0: np.ndarray) -> dict:
    """Check the too-strong telescoping PSD-storage condition.

    With terminal storage ``Pi_N=0`` and local conditions

        G_j + Pi_{j+1} - Pi_j >= 0,   Pi_j >= 0,

    the maximal possible storage is the future suffix sum.  Thus feasibility
    requires every suffix sum to be PSD and ``S0 + suffix_0 >= 0``.
    """
    if not increments:
        return {
            "feasible": _min_eig(S0) >= -1e-9,
            "min_suffix_eig": float("nan"),
            "first_bad_suffix": None,
            "initial_covered": _min_eig(S0) >= -1e-9,
        }
    suffix = np.zeros_like(increments[0])
    min_suffix = float("inf")
    first_bad = None
    suffix_mins = []
    for offset, inc in enumerate(reversed(increments), start=1):
        suffix = _sym(suffix + inc)
        mn = _min_eig(suffix)
        suffix_mins.append(mn)
        min_suffix = min(min_suffix, mn)
        if mn < -1e-9:
            first_bad = len(increments) - offset
    total_suffix = _sym(sum(increments, np.zeros_like(increments[0])))
    initial_covered = _min_eig(S0 + total_suffix) >= -1e-9
    return {
        "feasible": min_suffix >= -1e-9 and initial_covered,
        "min_suffix_eig": min_suffix,
        "first_bad_suffix": first_bad,
        "initial_covered": initial_covered,
        "suffix_mins": list(reversed(suffix_mins)),
    }


def path_debt_summary(schur_mats: list[np.ndarray]) -> dict:
    debts = [_neg_debt(S) for S in schur_mats]
    debt_max_eigs = [_max_eig(D) for D in debts]
    debt_traces = [float(np.trace(D)) for D in debts]
    peak_idx = int(np.argmax(debt_max_eigs)) if debt_max_eigs else 0
    loewner_increases = []
    trace_increases = []
    maxeig_increases = []
    for before, after, tr0, tr1, mx0, mx1 in zip(
        debts, debts[1:],
        debt_traces, debt_traces[1:],
        debt_max_eigs, debt_max_eigs[1:],
    ):
        loewner_increases.append(max(0.0, _max_eig(after - before)))
        trace_increases.append(max(0.0, tr1 - tr0))
        maxeig_increases.append(max(0.0, mx1 - mx0))
    return {
        "initial_debt_max": debt_max_eigs[0] if debt_max_eigs else float("nan"),
        "initial_debt_trace": debt_traces[0] if debt_traces else float("nan"),
        "peak_debt_max": debt_max_eigs[peak_idx] if debt_max_eigs else float("nan"),
        "peak_debt_trace": debt_traces[peak_idx] if debt_traces else float("nan"),
        "peak_debt_index": peak_idx,
        "final_debt_max": debt_max_eigs[-1] if debt_max_eigs else float("nan"),
        "final_debt_trace": debt_traces[-1] if debt_traces else float("nan"),
        "debt_max_eigs": debt_max_eigs,
        "debt_traces": debt_traces,
        "loewner_monotone_release": max(loewner_increases, default=0.0) <= 1e-9,
        "trace_monotone_release": max(trace_increases, default=0.0) <= 1e-9,
        "maxeig_monotone_release": max(maxeig_increases, default=0.0) <= 1e-9,
        "max_loewner_debt_increase": max(loewner_increases, default=0.0),
        "max_trace_debt_increase": max(trace_increases, default=0.0),
        "max_maxeig_debt_increase": max(maxeig_increases, default=0.0),
    }


def riccati_cell(block: np.ndarray, cell: np.ndarray, old_dim: int) -> dict:
    A, C, _ = _blocks(block, old_dim)
    EA, EC, ED = _blocks(cell, old_dim)
    A_plus = _sym(A + EA)
    next_block = _sym(block + cell)
    before = _schur(block, old_dim)
    after = _schur(next_block, old_dim)
    A_plus_eigs = np.linalg.eigvalsh(A_plus) if A_plus.size else np.array([float("nan")])
    if (
        not before["valid"]
        or A_plus_eigs[0] <= TOL * max(1.0, float(np.max(np.abs(A_plus_eigs))))
    ):
        return {
            "valid": False,
            "before": before,
            "after": after,
            "A_plus_min": float(A_plus_eigs[0]),
            "identity_error": float("nan"),
        }

    X = np.linalg.solve(A, C)
    residual = EC - EA @ X
    qform = _sym(ED - X.T @ EC - EC.T @ X + X.T @ EA @ X)
    square = _sym(residual.T @ np.linalg.solve(A_plus, residual))
    increment = _sym(qform - square)
    actual_increment = _sym(after["schur"] - before["schur"])
    identity_error = float(np.max(np.abs(actual_increment - increment)))
    q_eigs = np.linalg.eigvalsh(qform) if qform.size else np.array([float("nan")])
    square_eigs = np.linalg.eigvalsh(square) if square.size else np.array([float("nan")])
    inc_eigs = np.linalg.eigvalsh(increment) if increment.size else np.array([float("nan")])
    before_min, before_vec = _min_pair(before["schur"])
    after_min, after_vec = _min_pair(after["schur"])
    debt_split = {}
    if before_vec.size:
        ray_increment = float(before_vec.T @ increment @ before_vec)
        ray_Q = float(before_vec.T @ qform @ before_vec)
        ray_square = float(before_vec.T @ square @ before_vec)
        eigs_before, vecs_before = np.linalg.eigh(_sym(before["schur"]))
        if eigs_before[0] < -1e-9 and len(eigs_before) > 1:
            v = vecs_before[:, [0]]
            W = vecs_before[:, 1:]
            after_local = _sym(before["schur"] + increment)
            comp = _sym(W.T @ after_local @ W)
            cross = W.T @ after_local @ v
            head = float((v.T @ after_local @ v)[0, 0])
            comp_min = _min_eig(comp)
            if comp_min > 1e-10:
                leakage = float((cross.T @ np.linalg.solve(comp, cross))[0, 0])
                reduced = head - leakage
            else:
                leakage = float("nan")
                reduced = float("nan")
            debt_split = {
                "head_after": head,
                "comp_min_after": comp_min,
                "cross_norm_after": float(np.linalg.norm(cross)),
                "leakage": leakage,
                "reduced_after": reduced,
            }
    else:
        ray_increment = ray_Q = ray_square = float("nan")
    align_min_vecs = (
        float(abs(before_vec.T @ after_vec))
        if before_vec.size and after_vec.size else float("nan")
    )
    return {
        "valid": after["valid"],
        "before": before,
        "after": after,
        "A_plus_min": float(A_plus_eigs[0]),
        "Q": qform,
        "square": square,
        "increment": increment,
        "identity_error": identity_error,
        "Q_min": float(q_eigs[0]),
        "Q_max": float(q_eigs[-1]),
        "square_max": float(square_eigs[-1]),
        "square_trace": float(np.trace(square)),
        "increment_min": float(inc_eigs[0]),
        "increment_max": float(inc_eigs[-1]),
        "ray_increment_on_before_min": ray_increment,
        "ray_Q_on_before_min": ray_Q,
        "ray_square_on_before_min": ray_square,
        "before_min": before_min,
        "after_min": after_min,
        "min_vec_alignment": align_min_vecs,
        "debt_split": debt_split,
    }


def _scalar_suffix_capacity(increment_mins: list[float]) -> dict:
    """Sufficient isotropic-storage test from the cell minimum eigenvalues.

    If ``G_j >= g_j I`` and scalar storage satisfies
    ``G_j + lambda_j I - lambda_{j-1} I >= 0`` with ``lambda_N=0``, then a
    backward capacity evolves by adding ``g_j``.  A negative suffix means this
    crude scalar certificate cannot work.  Failure here is not a theorem-level
    obstruction, because matrix storage can exploit rotating directions.
    """
    cap = 0.0
    min_cap = 0.0
    first_bad_from_right = None
    suffix_rows = []
    for offset, gmin in enumerate(reversed(increment_mins), start=1):
        cap += gmin
        min_cap = min(min_cap, cap)
        suffix_rows.append(cap)
        if cap < -1e-9 and first_bad_from_right is None:
            first_bad_from_right = offset
    return {
        "terminal_capacity": cap,
        "min_suffix_capacity": min_cap,
        "scalar_isotropic_feasible": first_bad_from_right is None,
        "first_bad_from_right": first_bad_from_right,
        "suffix_capacities_from_right": list(reversed(suffix_rows)),
    }


def exact_old_operator(ambient, left_gmax: float, mode: str) -> np.ndarray:
    out = np.zeros_like(ambient.gram["Winf"])
    for n, atom in _mode_atoms(ambient, mode).items():
        if math.log(n) < left_gmax:
            out = out + atom
    return _sym(out)


def interval_residual_cells(ambient, left_gmax: float, right_gmax: float,
                            mode: str) -> dict[int, np.ndarray]:
    atoms = _mode_atoms(ambient, mode)
    active = [
        (n, math.log(n))
        for n in sorted(atoms)
        if left_gmax <= math.log(n) < right_gmax
    ]
    if not active:
        if mode == "smooth" or right_gmax <= left_gmax:
            return {}
        key = -int(round(1000.0 * right_gmax))
        return {key: _sym(smooth_prime_operator(ambient, right_gmax) -
                          smooth_prime_operator(ambient, left_gmax))}
    if mode == "smooth":
        return {}
    logs = [logn for _, logn in active]
    cells = {}
    for idx, (n, _) in enumerate(active):
        lo = left_gmax if idx == 0 else 0.5 * (logs[idx - 1] + logs[idx])
        hi = right_gmax if idx == len(active) - 1 else 0.5 * (logs[idx] + logs[idx + 1])
        cells[n] = _sym(smooth_cell_operator(ambient, lo, hi) - atoms[n])
    return cells


def extension_base_margin(ambient, left_gmax: float, right_gmax: float,
                          mode: str) -> np.ndarray:
    smooth_new = _sym(smooth_prime_operator(ambient, right_gmax) -
                      smooth_prime_operator(ambient, left_gmax))
    return _sym(ambient.gram["Winf"] - exact_old_operator(ambient, left_gmax, mode) - smooth_new)


def edge_report(ambient, points, left: float, right: float, mode: str = "zeta") -> dict:
    B = edge_basis(ambient, points, left, right)
    old_dim = points[left]["basis"].shape[1]
    base = extension_base_margin(ambient, left, right, mode)
    cells = interval_residual_cells(ambient, left, right, mode)

    block = _sym(B.T @ base @ B)
    initial_schur = _schur(block, old_dim)
    rows = []
    schur_prefix = [initial_schur["schur_min"]]
    schur_mats = [initial_schur["schur"]]
    increments = []
    total_increment = None
    for n, cell_full in sorted(cells.items()):
        cell = _sym(B.T @ cell_full @ B)
        data = riccati_cell(block, cell, old_dim)
        data.update({
            "n": n,
            "label": _label_for_n(n),
            "logn": math.log(n) if n > 0 else float("nan"),
        })
        rows.append(data)
        if data.get("valid"):
            total_increment = (
                data["increment"].copy() if total_increment is None
                else _sym(total_increment + data["increment"])
            )
            increments.append(data["increment"])
        block = _sym(block + cell)
        schur_prefix.append(data["after"]["schur_min"])
        schur_mats.append(data["after"]["schur"])

    final_schur = _schur(block, old_dim)
    exact_increment = _sym(final_schur["schur"] - initial_schur["schur"])
    total_error = (
        float(np.max(np.abs(exact_increment - total_increment)))
        if total_increment is not None and initial_schur["valid"] and final_schur["valid"]
        else float("nan")
    )
    valid_rows = [row for row in rows if row.get("valid")]
    increment_mins = [row["increment_min"] for row in valid_rows]
    suffix = _scalar_suffix_capacity(increment_mins)
    strict = strict_suffix_certificate(increments, initial_schur["schur"])
    debt = path_debt_summary(schur_mats)
    initial_debt = _neg_debt(initial_schur["schur"])
    final_surplus = _pos_part(final_schur["schur"])
    total_repair = _sym(final_schur["schur"] - initial_schur["schur"])
    endpoint = {
        "repair_minus_initial_debt_min": _min_eig(total_repair - initial_debt),
        "final_surplus_minus_initial_debt_min": _min_eig(final_surplus - initial_debt),
        "total_repair_min": _min_eig(total_repair),
        "final_surplus_min": _min_eig(final_surplus),
        "final_surplus_max": _max_eig(final_surplus),
    }
    finite_identity_error = max(
        (row["identity_error"] for row in valid_rows),
        default=float("nan"),
    )
    finite_prefix = np.array([
        value if np.isfinite(value) else np.inf
        for value in schur_prefix
    ])
    deepest_idx = int(np.argmin(finite_prefix))
    storage_depth = max(0.0, -float(finite_prefix[deepest_idx]))
    return {
        "left": left,
        "right": right,
        "mode": mode,
        "old_dim": old_dim,
        "shell_dim": B.shape[1] - old_dim,
        "rows": rows,
        "initial_schur_min": initial_schur["schur_min"],
        "final_schur_min": final_schur["schur_min"],
        "schur_prefix": schur_prefix,
        "deepest_index": deepest_idx,
        "storage_depth": storage_depth,
        "max_identity_error": finite_identity_error,
        "total_identity_error": total_error,
        "suffix": suffix,
        "strict_suffix": strict,
        "path_debt": debt,
        "endpoint": endpoint,
    }


def _fmt(x: float, prec: int = 3) -> str:
    if not np.isfinite(x):
        return "nan"
    return f"{x:+.{prec}e}"


def _print_edge(report: dict, topn: int = 5) -> None:
    suffix = report["suffix"]
    strict = report["strict_suffix"]
    debt = report["path_debt"]
    endpoint = report["endpoint"]
    deepest = report["deepest_index"]
    print(f"\n[{report['mode']} edge {report['left']:.2f}->{report['right']:.2f}] "
          f"dims {report['old_dim']}+{report['shell_dim']}, "
          f"schur base {_fmt(report['initial_schur_min'])}, "
          f"final {_fmt(report['final_schur_min'])}, "
          f"depth {report['storage_depth']:.3e} at prefix {deepest}, "
          f"id err {report['max_identity_error']:.1e}")
    print("      scalar isotropic suffix: "
          f"feasible={suffix['scalar_isotropic_feasible']} "
          f"terminal={_fmt(suffix['terminal_capacity'])} "
          f"min_suffix={_fmt(suffix['min_suffix_capacity'])}")
    print("      strict matrix suffix: "
          f"feasible={strict['feasible']} "
          f"min_suffix={_fmt(strict['min_suffix_eig'])} "
          f"initial_covered={strict['initial_covered']}")
    print("      path debt: "
          f"initial={debt['initial_debt_max']:.3e} "
          f"peak={debt['peak_debt_max']:.3e}@{debt['peak_debt_index']} "
          f"final={debt['final_debt_max']:.3e} "
          f"mono(L/tr)={debt['loewner_monotone_release']}/"
          f"{debt['trace_monotone_release']}")
    print("      endpoint repair tests: "
          f"repair-debt min={_fmt(endpoint['repair_minus_initial_debt_min'])} "
          f"surplus-debt min={_fmt(endpoint['final_surplus_minus_initial_debt_min'])}")

    valid_rows = [row for row in report["rows"] if row.get("valid")]
    harms = sorted(valid_rows, key=lambda row: row["increment_min"])[:topn]
    squares = sorted(valid_rows, key=lambda row: row["square_trace"], reverse=True)[:topn]
    active_debt_rows = [
        row for row in valid_rows
        if row["before_min"] < -1e-9 or row["after_min"] < -1e-9
    ]
    print("      strongest Riccati harms by min eigen of Q-square:")
    for row in harms:
        print(f"        {row['label']:<4} "
              f"Gmin={_fmt(row['increment_min'])} "
              f"Qmin={_fmt(row['Q_min'])} "
              f"sq_tr={row['square_trace']:.2e} "
              f"afterS={_fmt(row['after']['schur_min'])}")
    print("      largest negative-square loads:")
    for row in squares:
        print(f"        {row['label']:<4} "
              f"sq_tr={row['square_trace']:.2e} "
              f"sq_max={row['square_max']:.2e} "
              f"Gmin={_fmt(row['increment_min'])}")
    if active_debt_rows:
        print("      active debt direction:")
        for row in active_debt_rows:
            print(f"        {row['label']:<4} "
                  f"S {row['before_min']:+.3e}->{row['after_min']:+.3e} "
                  f"rayG={row['ray_increment_on_before_min']:+.3e} "
                  f"rayQ={row['ray_Q_on_before_min']:+.3e} "
                  f"raySq={row['ray_square_on_before_min']:+.3e} "
                  f"align={row['min_vec_alignment']:.3f}")
            split = row.get("debt_split") or {}
            if split:
                print(f"             "
                      f"head={split['head_after']:+.3e} "
                      f"compMin={split['comp_min_after']:+.3e} "
                      f"cross={split['cross_norm_after']:.3e} "
                      f"leak={split['leakage']:+.3e} "
                      f"reduced={split['reduced_after']:+.3e}")


def compact_mode_table(modes: tuple[str, ...]) -> dict:
    ambient, points = ambient_and_points()
    reports = {}
    print("\n[fail-closed mode table]")
    print("      mode     final all+  debt->0 all+  invalid  worst final   peak debt")
    for mode in modes:
        rows = [
            edge_report(ambient, points, left, right, mode=mode)
            for left, right in FOCUS_EDGES
        ]
        reports[mode] = rows
        finals = [row["final_schur_min"] for row in rows]
        invalid = sum(1 for value in finals if not np.isfinite(value))
        finite_finals = [value for value in finals if np.isfinite(value)]
        final_all = invalid == 0 and all(value >= -1e-9 for value in finite_finals)
        debt_all = invalid == 0 and all(
            row["path_debt"]["loewner_monotone_release"]
            and row["path_debt"]["final_debt_max"] <= 1e-9
            for row in rows
        )
        worst_final = min(finite_finals) if finite_finals else float("nan")
        peak_debt = max(
            (row["path_debt"]["peak_debt_max"] for row in rows
             if np.isfinite(row["path_debt"]["peak_debt_max"])),
            default=float("nan"),
        )
        print(f"      {mode:<8} {str(final_all):<10} {str(debt_all):<12} "
              f"{invalid:<7d} {worst_final:+.3e}  {peak_debt:.3e}")
    return reports


def summary(mode: str = "zeta", compact_modes: tuple[str, ...] = ()) -> dict:
    print("=" * 78)
    print("Finite Riccati diagnostic for exact Euler residual cells")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_report(ambient, points, left, right, mode=mode)
        reports[(left, right)] = report
        _print_edge(report)

    print("\nInterpretation:")
    print("  * The Schur update identity holds to numerical roundoff, so the")
    print("    Q - R^T A_+^{-1} R split is the right finite algebraic object.")
    print("  * The negative Riccati square is usually small but not zero; a proof")
    print("    that only controls the signed residual Q would be incomplete.")
    print("  * The crude scalar-isotropic suffix test is intentionally severe.")
    print("    The strict matrix suffix test is also severe: it demands all")
    print("    future Riccati suffixes be PSD.  Failure there means endpoint debt")
    print("    or state transport is needed, not that the exact Euler path fails.")
    if compact_modes:
        reports["_compact"] = compact_mode_table(compact_modes)
    return reports


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="zeta",
                        choices=("zeta", "DH", "primes", "powers", "smooth"))
    parser.add_argument("--compact-modes", nargs="*", default=())
    args = parser.parse_args()
    summary(mode=args.mode, compact_modes=tuple(args.compact_modes))
