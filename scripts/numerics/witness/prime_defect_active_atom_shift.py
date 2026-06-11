"""Location and weight sensitivity of the active repair atom.

The active-debt current diagnostic isolates the late repair cell

    3.00 -> 3.24, repair atom n=23.

This script keeps the smooth cell and active Schur-debt state fixed, but
replaces the atom in that cell by a shifted or rescaled Toeplitz atom.  The
goal is to measure how much of the repair is geometric slack and how much
depends on the exact placement/weight of log(23).

Run:
    python3 -m scripts.numerics.witness.prime_defect_active_atom_shift
    python3 -m scripts.numerics.witness.prime_defect_active_atom_shift --refinements
"""
from __future__ import annotations

import argparse
import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_active_debt_current import (
    LATE_EDGE,
    _cell_bounds_for_atoms,
    _quadratic,
    context_for_basis,
)
from .prime_defect_residual_control import edge_basis, smooth_cell_operator
from .prime_defect_riccati_storage import (
    _blocks,
    _min_pair,
    extension_base_margin,
    interval_residual_cells,
    riccati_cell,
)
from .semilocal_2 import _grids, _phihat


REPAIR_N = 23
REFINEMENTS = (
    (17, 0.10),
    (21, 0.08),
    (25, 0.06),
    (29, 0.05),
    (33, 0.045),
)


def _compressed_fourier_basis(ambient, B: np.ndarray) -> tuple[np.ndarray, np.ndarray, float]:
    grid = _grids()
    ts, dt = grid["ts"], grid["dt"]
    ph = np.array([_phihat(ts, c, ambient.half_width) for c in ambient.centers])
    return ts, B.T @ ph, dt


def _compressed_atom_block(state: dict, U: float, weight: float) -> np.ndarray:
    ts = state["fourier_ts"]
    compressed_ph = state["compressed_ph"]
    dt = state["fourier_dt"]
    weighted = compressed_ph * np.cos(U * ts)
    return _sym(weight * (weighted @ compressed_ph.T) * dt / (2.0 * np.pi))


def active_state(ncenters: int = 25, half_width: float = 0.06,
                 left: float = LATE_EDGE[0], right: float = LATE_EDGE[1],
                 repair_n: int = REPAIR_N,
                 physical_ngrid: int = 6001) -> dict:
    ambient, points = context_for_basis(
        ncenters,
        half_width,
        left,
        right,
        physical_ngrid=physical_ngrid,
    )
    B = edge_basis(ambient, points, left, right)
    old_dim = points[left]["basis"].shape[1]
    base = extension_base_margin(ambient, left, right, "zeta")
    current = _sym(B.T @ base @ B)

    cells = interval_residual_cells(ambient, left, right, "zeta")
    bounds = _cell_bounds_for_atoms(ambient, left, right)
    for n, cell_full in sorted(cells.items()):
        if n == repair_n:
            break
        current = _sym(current + B.T @ cell_full @ B)

    A, C, D = _blocks(current, old_dim)
    schur = _sym(D - C.T @ np.linalg.solve(A, C))
    debt, y = _min_pair(schur)
    x = np.linalg.solve(A, C @ y)
    f = np.concatenate([x, -y])

    lo, hi = bounds[repair_n]
    smooth_full = smooth_cell_operator(ambient, lo, hi)
    smooth_block = _sym(B.T @ smooth_full @ B)
    smooth_q = _quadratic(smooth_block, f)
    fourier_ts, compressed_ph, fourier_dt = _compressed_fourier_basis(ambient, B)
    state = {
        "ambient": ambient,
        "points": points,
        "B": B,
        "old_dim": old_dim,
        "current": current,
        "f": f,
        "left": left,
        "right": right,
        "repair_n": repair_n,
        "cell": (lo, hi),
        "smooth_block": smooth_block,
        "smooth_q": smooth_q,
        "base_debt": debt,
        "ncenters": ncenters,
        "half_width": half_width,
        "fourier_ts": fourier_ts,
        "compressed_ph": compressed_ph,
        "fourier_dt": fourier_dt,
    }
    logn = math.log(repair_n)
    k_logn = _quadratic(_compressed_atom_block(state, logn, 1.0), f)
    atom_q = _quadratic(_sym(B.T @ ambient.atoms["zeta"][repair_n] @ B), f)
    atom_weight = atom_q / k_logn
    state.update({
        "logn": logn,
        "atom_rel": (logn - lo) / (hi - lo),
        "atom_weight": atom_weight,
    })
    return state


def shifted_row(state: dict, rel: float | None = None,
                U: float | None = None, scale: float = 1.0) -> dict:
    lo, hi = state["cell"]
    if U is None:
        if rel is None:
            raise ValueError("rel or U required")
        U = lo + rel * (hi - lo)
    rel = (U - lo) / (hi - lo)
    atom = _compressed_atom_block(state, U, scale * state["atom_weight"])
    cell = _sym(state["smooth_block"] - atom)
    ric = riccati_cell(state["current"], cell, state["old_dim"])
    k_u = _quadratic(_compressed_atom_block(state, U, 1.0), state["f"])
    atom_q = scale * state["atom_weight"] * k_u
    residual_q = state["smooth_q"] - atom_q
    split = ric.get("debt_split", {}) if ric.get("valid", False) else {}
    leakage = split.get("leakage", float("nan"))
    reduced = split.get("reduced_after", float("nan"))
    required = (
        max(0.0, -ric["before_min"])
        + ric.get("ray_square_on_before_min", float("nan"))
        + leakage
        if ric.get("valid", False) else float("nan")
    )
    return {
        "rel": float(rel),
        "U": float(U),
        "scale": float(scale),
        "k": k_u,
        "atom_q": atom_q,
        "residual_q": residual_q,
        "required": required,
        "surplus": residual_q - required if np.isfinite(required) else float("nan"),
        "after_min": ric.get("after_min", float("nan")),
        "ray_Q": ric.get("ray_Q_on_before_min", float("nan")),
        "ray_square": ric.get("ray_square_on_before_min", float("nan")),
        "leakage": leakage,
        "reduced": reduced,
        "valid": bool(ric.get("valid", False)),
    }


def location_threshold(state: dict) -> dict:
    samples = [shifted_row(state, rel=rel) for rel in np.linspace(0.0, 1.0, 51)]
    passing = [row for row in samples if row["valid"] and row["after_min"] >= -1e-9]
    if not passing:
        return {"found": False, "rel": float("nan"), "U": float("nan"), "samples": samples}
    first = passing[0]
    idx = samples.index(first)
    if idx == 0:
        return {"found": True, "rel": 0.0, "U": state["cell"][0], "samples": samples}
    lo_rel = samples[idx - 1]["rel"]
    hi_rel = first["rel"]
    for _ in range(25):
        mid = 0.5 * (lo_rel + hi_rel)
        row = shifted_row(state, rel=mid)
        if row["valid"] and row["after_min"] >= -1e-9:
            hi_rel = mid
        else:
            lo_rel = mid
    row = shifted_row(state, rel=hi_rel)
    return {"found": True, "rel": hi_rel, "U": row["U"], "samples": samples}


def scale_threshold(state: dict) -> dict:
    logn = state["logn"]
    exact = shifted_row(state, U=logn, scale=1.0)
    if not exact["valid"] or exact["after_min"] < -1e-9:
        return {"found": False, "scale": float("nan"), "exact": exact}
    lo = 1.0
    hi = 2.0
    while hi < 16.0:
        row = shifted_row(state, U=logn, scale=hi)
        if not row["valid"] or row["after_min"] < -1e-9:
            break
        lo = hi
        hi *= 2.0
    if hi >= 16.0:
        return {"found": False, "scale": float("inf"), "exact": exact}
    for _ in range(25):
        mid = 0.5 * (lo + hi)
        row = shifted_row(state, U=logn, scale=mid)
        if row["valid"] and row["after_min"] >= -1e-9:
            lo = mid
        else:
            hi = mid
    return {"found": True, "scale": lo, "exact": exact}


def report_for_config(ncenters: int = 25, half_width: float = 0.06) -> dict:
    state = active_state(ncenters, half_width)
    exact = shifted_row(state, U=state["logn"])
    loc = location_threshold(state)
    scale = scale_threshold(state)
    rows = [
        shifted_row(state, rel=rel)
        for rel in (0.0, 0.25, 0.50, state["atom_rel"], 0.90, 1.0)
    ]
    return {
        "state": state,
        "exact": exact,
        "location_threshold": loc,
        "scale_threshold": scale,
        "rows": rows,
    }


def _print_report(report: dict) -> None:
    state = report["state"]
    lo, hi = state["cell"]
    loc = report["location_threshold"]
    scale = report["scale_threshold"]
    print("=" * 78)
    print("Active repair atom location/weight sensitivity")
    print("=" * 78)
    print(f"basis n={state['ncenters']} hw={state['half_width']:.3f}, "
          f"cell {state['repair_n']}=[{lo:.6f},{hi:.6f}], "
          f"log n={state['logn']:.6f}, rel={state['atom_rel']:.3f}")
    print(f"base debt={state['base_debt']:+.6e}, "
          f"smooth_q={state['smooth_q']:+.6e}, "
          f"atom_weight={state['atom_weight']:.6e}")
    if loc["found"]:
        print(f"location threshold: rel={loc['rel']:.6f}, U={loc['U']:.6f}, "
              f"exact slack rel={state['atom_rel'] - loc['rel']:+.6f}")
    else:
        print("location threshold: none in the cell")
    if scale["found"]:
        print(f"scale threshold at exact log n: {scale['scale']:.6f} "
              f"(extra weight slack {(scale['scale'] - 1.0):+.3%})")
    else:
        print(f"scale threshold at exact log n: {scale['scale']}")
    print("\n      rel      U          k(U)        residual    required    surplus     after min   reduced")
    for row in report["rows"]:
        print(f"      {row['rel']:.3f}  "
              f"{row['U']:.6f}  "
              f"{row['k']:+.3e}  "
              f"{row['residual_q']:+.3e}  "
              f"{row['required']:+.3e}  "
              f"{row['surplus']:+.3e}  "
              f"{row['after_min']:+.3e}  "
              f"{row['reduced']:+.3e}")


def refinement_table() -> list[dict]:
    print("\n[repair atom shift refinement table]")
    print("      basis       loc*    atomRel  relSlack  scale*   afterExact  reducedExact")
    out = []
    for ncenters, half_width in REFINEMENTS:
        report = report_for_config(ncenters, half_width)
        state = report["state"]
        loc = report["location_threshold"]
        scale = report["scale_threshold"]
        exact = report["exact"]
        row = {
            "ncenters": ncenters,
            "half_width": half_width,
            "loc_rel": loc["rel"],
            "atom_rel": state["atom_rel"],
            "rel_slack": state["atom_rel"] - loc["rel"] if loc["found"] else float("nan"),
            "scale": scale["scale"],
            "after": exact["after_min"],
            "reduced": exact["reduced"],
        }
        out.append(row)
        print(f"      n{ncenters:<2d}/h{half_width:.3f} "
              f"{row['loc_rel']:.3f}   "
              f"{row['atom_rel']:.3f}   "
              f"{row['rel_slack']:+.3f}   "
              f"{row['scale']:.3f}   "
              f"{row['after']:+.3e}  "
              f"{row['reduced']:+.3e}")
    return out


def summary(with_refinements: bool = False) -> dict:
    report = report_for_config()
    _print_report(report)
    if with_refinements:
        report["refinements"] = refinement_table()
    print("\nInterpretation:")
    print("  * Moving the atom right helps because the active kernel is smaller there.")
    print("  * The location threshold measures how far left the atom could move before")
    print("    the first repair cell stops closing the Schur debt.")
    print("  * The scale threshold measures how much atom weight can be added at the")
    print("    exact location before the repair fails.")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--refinements", action="store_true")
    args = parser.parse_args()
    summary(with_refinements=args.refinements)
