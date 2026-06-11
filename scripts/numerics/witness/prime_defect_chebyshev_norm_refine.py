"""Refinement check for late Chebyshev norm-budget alignment.

The norm-budget witness showed that crude scalar bounds are very wasteful on
the late edge 3.00 -> 3.24.  This script repeats that budget on neighboring
finite Sonin windows to test whether the cancellation/alignment signal is
stable under basis refinement.

Run:
    python3 -m scripts.numerics.witness.prime_defect_chebyshev_norm_refine
"""
from __future__ import annotations

from .prime_defect_chebyshev_norm_budget import interval_budget
from .prime_defect_chebyshev_residual import edge_chebyshev_report
from .prime_nested_cone import build_ambient, point
from .prime_shell_coupling_bound import GMAXS


CONFIGS = (
    (17, 0.10),
    (21, 0.08),
    (25, 0.06),
)
EDGE = (3.00, 3.24)


def build_config(ncenters: int, half_width: float):
    max_gmax = GMAXS[-1]
    ambient = build_ambient(
        ncenters=ncenters,
        half_width=half_width,
        cmax=max_gmax / 2.0 - half_width,
        max_gmax=max_gmax,
    )
    points = {gmax: point(ambient, "zeta", gmax) for gmax in GMAXS}
    return ambient, points


def _print_row(basis: str, part: str, row: dict) -> None:
    print(f"{basis:<11} {part:<4} "
          f"{row['residual']:+.4f}  "
          f"{row['boundary']:+.4f}  "
          f"{row['distributed']:+.4f}  "
          f"{row['abs_pair']:.4f}  "
          f"{row['signed_over_abs']:.3f}  "
          f"{row['sup_tv_ratio']:.3f}  "
          f"{row['l2_ratio']:.3f}  "
          f"{row['positive']:+.3f}  "
          f"{row['negative']:+.3f}")


def summary() -> list[dict]:
    print("=" * 78)
    print("Refinement check for late Chebyshev norm-budget alignment")
    print("=" * 78)
    print("basis       part residual  boundary  distrib   int|.|  "
          "|dist|/|.|  supTVr  L2r    pos      neg")
    rows = []
    for ncenters, half_width in CONFIGS:
        ambient, points = build_config(ncenters, half_width)
        report = edge_chebyshev_report(ambient, points, EDGE[0], EDGE[1])
        old = interval_budget(report, EDGE[0])
        all_row = interval_budget(report, EDGE[1])
        basis = f"n{ncenters}/hw{half_width:.2f}"
        rows.append({"basis": basis, "old": old, "all": all_row})
        _print_row(basis, "old", old)
        _print_row(basis, "all", all_row)

    print("\nInterpretation:")
    print("  * Across these finite refinements, the late distributed term remains")
    print("    a small signed fraction of int|F phi'| and a still smaller fraction")
    print("    of crude supTV/L2 bounds.")
    print("  * The signs and magnitudes vary with the finite model, but the need")
    print("    for an alignment-sensitive estimate is stable.")
    return rows


if __name__ == "__main__":
    summary()
