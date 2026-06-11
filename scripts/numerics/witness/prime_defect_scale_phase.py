"""Scale-phase diagram for the passive shell transfer bound.

The perturbation witness showed that zeta's passive chain is coefficient-rigid:
sign flips, shuffles, and even old-history rescaling can break passivity.  This
script maps the local stability region around the exact von Mangoldt scale.

For a support extension H_L subset H_R, write the right margin with scaled
zeta atoms:

    M_R(a,b) = W_inf
             - a * sum_{log n < L}       atom_n
             - b * sum_{L <= log n < R}  atom_n.

Here a scales the old Euler history and b scales the newly entering shell
atoms.  The exact zeta point is (a,b)=(1,1).  We test the passive transfer
condition rho <= 1 along the nested path.

Run:
    python3 -m scripts.numerics.witness.prime_defect_scale_phase
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_nested_cone import _orthogonal_shell, build_ambient, point
from .prime_shell_coupling_bound import GMAXS

AMBIENT_N = 25
AMBIENT_HW = 0.06
MAX_GMAX = GMAXS[-1]
FOCUS_EDGES = (
    (1.72, 1.88),
    (1.88, 2.10),
    (2.30, 2.52),
    (2.76, 3.00),
    (3.00, 3.24),
)


def _invsqrt_spd(M: np.ndarray, tol: float = 1e-10) -> np.ndarray | None:
    if M.size == 0:
        return None
    eigs, vecs = np.linalg.eigh(_sym(M))
    scale = max(1.0, float(np.max(np.abs(eigs))))
    if eigs[0] <= tol * scale:
        return None
    return vecs @ np.diag(1.0 / np.sqrt(eigs)) @ vecs.T


def ambient_and_points():
    ambient = build_ambient(
        ncenters=AMBIENT_N,
        half_width=AMBIENT_HW,
        cmax=MAX_GMAX / 2.0 - AMBIENT_HW,
        max_gmax=MAX_GMAX,
    )
    points = {gmax: point(ambient, "zeta", gmax) for gmax in GMAXS}
    return ambient, points


def scaled_margin(ambient, left_gmax: float, right_gmax: float,
                  old_scale: float, new_scale: float) -> np.ndarray:
    margin = ambient.gram["Winf"].copy()
    for n, atom in ambient.atoms["zeta"].items():
        logn = math.log(n)
        if logn >= right_gmax:
            continue
        scale = old_scale if logn < left_gmax else new_scale
        margin = margin - scale * atom
    return _sym(margin)


def edge_rho(ambient, points: dict[float, dict], left_gmax: float, right_gmax: float,
             old_scale: float, new_scale: float) -> dict:
    M = scaled_margin(ambient, left_gmax, right_gmax, old_scale, new_scale)
    left = points[left_gmax]
    right = points[right_gmax]
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]
    block = _sym(B.T @ M @ B)
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])
    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    D_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])
    right_block = _sym(right["basis"].T @ M @ right["basis"])
    right_min = float(np.linalg.eigvalsh(right_block)[0])
    A_invsqrt = _invsqrt_spd(A)
    D_invsqrt = _invsqrt_spd(D)
    if A_invsqrt is None or D_invsqrt is None:
        return {
            "valid": False,
            "rho": float("nan"),
            "defect": float("nan"),
            "right_min": right_min,
            "A_min": float(A_eigs[0]),
            "D_min": float(D_eigs[0]),
        }
    K = A_invsqrt @ C @ D_invsqrt
    svals = np.linalg.svd(K, compute_uv=False)
    rho = float(svals[0] ** 2) if len(svals) else float("nan")
    return {
        "valid": True,
        "rho": rho,
        "defect": float(1.0 - rho),
        "right_min": right_min,
        "A_min": float(A_eigs[0]),
        "D_min": float(D_eigs[0]),
    }


def path_eval(ambient, points, old_scale: float, new_scale: float) -> dict:
    rows = [
        edge_rho(ambient, points, left, right, old_scale, new_scale)
        for left, right in FOCUS_EDGES
    ]
    valid = [row for row in rows if row["valid"]]
    max_rho = max((row["rho"] for row in valid), default=float("nan"))
    min_defect = min((row["defect"] for row in valid), default=float("nan"))
    min_right = min(row["right_min"] for row in rows)
    first_bad_idx = next(
        (i for i, row in enumerate(rows)
         if (not row["valid"]) or row.get("rho", 0.0) > 1.0 + 1e-9),
        None,
    )
    return {
        "old_scale": old_scale,
        "new_scale": new_scale,
        "rows": rows,
        "valid_edges": len(valid),
        "max_rho": max_rho,
        "min_defect": min_defect,
        "min_right": min_right,
        "passive": first_bad_idx is None and len(valid) == len(rows),
        "first_bad_edge": None if first_bad_idx is None else FOCUS_EDGES[first_bad_idx],
    }


def one_dim_sweep(ambient, points, mode: str, scales: np.ndarray) -> list[dict]:
    rows = []
    for scale in scales:
        if mode == "old":
            rows.append(path_eval(ambient, points, float(scale), 1.0))
        elif mode == "new":
            rows.append(path_eval(ambient, points, 1.0, float(scale)))
        elif mode == "global":
            rows.append(path_eval(ambient, points, float(scale), float(scale)))
        else:
            raise ValueError(f"unknown sweep mode: {mode}")
    return rows


def pass_interval(rows: list[dict], mode: str) -> tuple[float | None, float | None]:
    vals = [
        row["old_scale"] if mode in {"old", "global"} else row["new_scale"]
        for row in rows if row["passive"]
    ]
    return (min(vals), max(vals)) if vals else (None, None)


def derivative_rows(ambient, points, eps: float = 1e-3) -> list[dict]:
    out = []
    for left, right in FOCUS_EDGES:
        base = edge_rho(ambient, points, left, right, 1.0, 1.0)
        old_plus = edge_rho(ambient, points, left, right, 1.0 + eps, 1.0)
        old_minus = edge_rho(ambient, points, left, right, 1.0 - eps, 1.0)
        new_plus = edge_rho(ambient, points, left, right, 1.0, 1.0 + eps)
        new_minus = edge_rho(ambient, points, left, right, 1.0, 1.0 - eps)
        def slope(plus, minus):
            if not plus["valid"] or not minus["valid"]:
                return float("nan")
            return float((plus["rho"] - minus["rho"]) / (2.0 * eps))
        out.append({
            "left": left,
            "right": right,
            "rho": base["rho"],
            "defect": base["defect"],
            "old_slope": slope(old_plus, old_minus),
            "new_slope": slope(new_plus, new_minus),
        })
    return out


def joint_corridor(ambient, points, old_scales: np.ndarray, new_scales: np.ndarray) -> list[dict]:
    rows = []
    for old in old_scales:
        passing_new = []
        for new in new_scales:
            ev = path_eval(ambient, points, float(old), float(new))
            if ev["passive"]:
                passing_new.append(float(new))
        rows.append({
            "old_scale": float(old),
            "new_min": min(passing_new) if passing_new else None,
            "new_max": max(passing_new) if passing_new else None,
            "count": len(passing_new),
        })
    return rows


def _bad_text(row: dict) -> str:
    if row["first_bad_edge"] is None:
        return "none"
    left, right = row["first_bad_edge"]
    return f"{left:.2f}->{right:.2f}"


def _print_sweep(name: str, rows: list[dict]) -> None:
    lo, hi = pass_interval(rows, name)
    interval = "none" if lo is None else f"[{lo:.3f}, {hi:.3f}]"
    print(f"\n[1] {name} scale sweep, pass interval {interval}")
    print("      scale   passive  max rho   min defect  min right  first bad")
    wanted = {0.50, 0.75, 0.90, 1.00, 1.10, 1.25, 1.50}
    for row in rows:
        scale = row["old_scale"] if name in {"old", "global"} else row["new_scale"]
        if not any(abs(scale - w) < 1e-9 for w in wanted):
            continue
        print(f"      {scale:.2f}    "
              f"{str(row['passive']):<7} "
              f"{row['max_rho']:.3f}    "
              f"{row['min_defect']:+.3f}    "
              f"{row['min_right']:+.2e}  "
              f"{_bad_text(row)}")


def _print_derivatives(rows: list[dict]) -> None:
    print("\n[2] Local rho sensitivity at exact zeta scale")
    print("      edge        rho    defect   d rho/d old   d rho/d new")
    for row in rows:
        print(f"      {row['left']:.2f}->{row['right']:.2f}  "
              f"{row['rho']:.3f}  "
              f"{row['defect']:+.3f}    "
              f"{row['old_slope']:+.2f}       "
              f"{row['new_slope']:+.2f}")


def _print_corridor(rows: list[dict]) -> None:
    print("\n[3] Joint old/new passivity corridor")
    print("      old scale   passing new-scale interval   count")
    for row in rows:
        if row["old_scale"] not in {0.80, 0.90, 1.00, 1.10, 1.20}:
            continue
        interval = (
            "none" if row["new_min"] is None
            else f"[{row['new_min']:.2f}, {row['new_max']:.2f}]"
        )
        print(f"      {row['old_scale']:.2f}        {interval:<18} {row['count']:2d}")


def summary() -> dict:
    print("=" * 78)
    print("Scale phase diagram for passive shell transfer")
    print("=" * 78)
    ambient, points = ambient_and_points()

    scales = np.round(np.arange(0.50, 1.5001, 0.025), 3)
    old_rows = one_dim_sweep(ambient, points, "old", scales)
    new_rows = one_dim_sweep(ambient, points, "new", scales)
    global_rows = one_dim_sweep(ambient, points, "global", scales)
    _print_sweep("old", old_rows)
    _print_sweep("new", new_rows)
    _print_sweep("global", global_rows)

    derivatives = derivative_rows(ambient, points)
    _print_derivatives(derivatives)

    joint_old = np.round(np.arange(0.80, 1.2001, 0.025), 3)
    joint_new = np.round(np.arange(0.80, 1.2001, 0.025), 3)
    corridor = joint_corridor(ambient, points, joint_old, joint_new)
    _print_corridor(corridor)

    print("\nInterpretation:")
    print("  * Exact zeta sits in a narrow passivity corridor, not a broad stable region.")
    print("  * Old-history scaling is especially rigid: both damping and boosting can")
    print("    break positivity, but at different support shells.")
    print("  * The proof target should explain a calibrated balance between old Green")
    print("    history and newly entering Euler atoms.")
    return {
        "old_sweep": old_rows,
        "new_sweep": new_rows,
        "global_sweep": global_rows,
        "derivatives": derivatives,
        "corridor": corridor,
    }


if __name__ == "__main__":
    summary()
