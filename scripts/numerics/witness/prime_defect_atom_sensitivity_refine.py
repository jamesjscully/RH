"""Refinement check for atom-level sensitivity on the late passive wall.

The late edge 3.00 -> 3.24 closes the old/global coefficient-scale tube in
the threshold witnesses.  This script checks whether the atom-level sensitivity
there remains a signed cumulative old-history balance across neighboring
finite Sonin windows.

Run:
    python3 -m scripts.numerics.witness.prime_defect_atom_sensitivity_refine
"""
from __future__ import annotations

import math

from .prime_defect_atom_sensitivity import atom_derivatives
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


def _top_text(rows: list[dict], count: int = 5) -> str:
    top = sorted(rows, key=lambda row: row["abs_slope"], reverse=True)[:count]
    return ", ".join(f"{row['label']}:{row['slope']:+.2f}" for row in top)


def _old_concentration(rows: list[dict], count: int = 5) -> float:
    old = [row for row in rows if row["region"] == "old"]
    total = sum(row["abs_slope"] for row in old)
    if total == 0.0 or math.isnan(total):
        return float("nan")
    top = sorted(old, key=lambda row: row["abs_slope"], reverse=True)[:count]
    return sum(row["abs_slope"] for row in top) / total


def summary() -> list[dict]:
    print("=" * 78)
    print("Refinement check for late atom-level sensitivity")
    print("=" * 78)
    print("basis       rho       defect    old sum   new sum   pos mass  neg mass  top old atoms")

    reports = []
    for ncenters, half_width in CONFIGS:
        ambient, points = build_config(ncenters, half_width)
        report = atom_derivatives(ambient, points, EDGE[0], EDGE[1])
        reports.append(report)
        old_rows = [row for row in report["rows"] if row["region"] == "old"]
        basis = f"n{ncenters}/hw{half_width:.2f}"
        base = report["base"]
        print(f"{basis:<11} "
              f"{base['rho']:.6f}  "
              f"{base['defect']:+.6f}  "
              f"{report['old_sum']:+.3f}    "
              f"{report['new_sum']:+.3f}    "
              f"{report['pos_mass']:+.3f}    "
              f"{report['neg_mass']:+.3f}    "
              f"{_top_text(old_rows)}")
        print(f"{'':<11} top-five old abs sensitivity fraction: "
              f"{_old_concentration(report['rows']):.3f}")

    print("\nInterpretation:")
    print("  * The old-history derivative remains a signed cancellation across")
    print("    refinements: large positive and negative atom sensitivities nearly")
    print("    balance, leaving a small net old-scale slope.")
    print("  * The leading labels are stable enough to be arithmetic data, but their")
    print("    signs alternate; a proof needs an Euler Green identity, not an")
    print("    atomwise positivity argument.")
    return reports


if __name__ == "__main__":
    summary()
