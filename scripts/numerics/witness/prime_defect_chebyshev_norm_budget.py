"""Norm budget for the Chebyshev-error stress residual.

The Chebyshev residual witness writes the discrete-minus-smooth arithmetic
term as

    R(B) = phi(B)F(B) - int F(U) phi'(U) dU.

This script asks how sharp crude bounds are for the distributed term:

    |int F phi'| <= sup|F| * int |phi'|
    |int F phi'| <= ||F||_2 ||phi'||_2.

If these bounds are very wasteful, the proof target needs more structure than
a generic Chebyshev-error estimate plus a variation bound on the stress kernel.

Run:
    python3 -m scripts.numerics.witness.prime_defect_chebyshev_norm_budget
"""
from __future__ import annotations

import math

import numpy as np

from .prime_defect_chebyshev_residual import (
    edge_chebyshev_report,
    ibp_residual,
)
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points


def _trapz(values: np.ndarray, grid: np.ndarray) -> float:
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trap(values, x=grid))


def interval_budget(report: dict, hi: float) -> dict:
    integrator = report["cheb_integrator"]
    Us_all = integrator["Us"]
    mask = Us_all <= hi + 1e-12
    Us = Us_all[mask]
    F = integrator["F"][mask]
    phip = integrator["phip"][mask]
    integrand = -F * phip
    distributed = _trapz(integrand, Us)
    positive = _trapz(np.maximum(integrand, 0.0), Us)
    negative = _trapz(np.minimum(integrand, 0.0), Us)
    abs_pair = _trapz(np.abs(integrand), Us)
    max_F = float(np.max(np.abs(F)))
    tv_phi = _trapz(np.abs(phip), Us)
    sup_tv = max_F * tv_phi
    l2_F = math.sqrt(max(0.0, _trapz(F * F, Us)))
    l2_phip = math.sqrt(max(0.0, _trapz(phip * phip, Us)))
    l2_bound = l2_F * l2_phip
    ibp = ibp_residual(report, hi)
    return {
        "distributed": distributed,
        "positive": positive,
        "negative": negative,
        "abs_pair": abs_pair,
        "signed_over_abs": abs(distributed) / abs_pair if abs_pair else float("nan"),
        "max_F": max_F,
        "tv_phi": tv_phi,
        "sup_tv": sup_tv,
        "sup_tv_ratio": abs(distributed) / sup_tv if sup_tv else float("nan"),
        "l2_F": l2_F,
        "l2_phip": l2_phip,
        "l2_bound": l2_bound,
        "l2_ratio": abs(distributed) / l2_bound if l2_bound else float("nan"),
        "boundary": ibp["boundary"],
        "residual": ibp["total"],
    }


def edge_budget_report(ambient, points, left: float, right: float) -> dict:
    report = edge_chebyshev_report(ambient, points, left, right)
    return {
        "left": left,
        "right": right,
        "old": interval_budget(report, left),
        "all": interval_budget(report, right),
    }


def _print_row(edge: str, part: str, row: dict) -> None:
    print(f"{edge:<12} {part:<4} "
          f"{row['residual']:+.4f}  "
          f"{row['boundary']:+.4f}  "
          f"{row['distributed']:+.4f}  "
          f"{row['abs_pair']:.4f}  "
          f"{row['signed_over_abs']:.3f}  "
          f"{row['sup_tv']:.4f}  "
          f"{row['sup_tv_ratio']:.3f}  "
          f"{row['l2_bound']:.4f}  "
          f"{row['l2_ratio']:.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Norm budget for Chebyshev-error stress residual")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    print("edge         part residual  boundary  distrib   int|.|  "
          "|dist|/|.|  supTV    ratio  L2bd     ratio")
    for left, right in FOCUS_EDGES:
        report = edge_budget_report(ambient, points, left, right)
        reports[(left, right)] = report
        edge = f"{left:.2f}->{right:.2f}"
        _print_row(edge, "old", report["old"])
        _print_row(edge, "all", report["all"])

    late = reports[(3.00, 3.24)]["all"]
    print("\nLate all-history distributed term:")
    print(f"  positive part {late['positive']:+.4f}")
    print(f"  negative part {late['negative']:+.4f}")
    print(f"  signed total  {late['distributed']:+.4f}")
    print("\nInterpretation:")
    print("  * The distributed residual usually has substantial cancellation:")
    print("    |int F phi'| is often much smaller than int|F phi'|.")
    print("  * Crude sup|F|*TV(phi) bounds are far from sharp in these windows.")
    print("  * A viable proof should exploit oscillatory alignment between F and")
    print("    the admissible stress-kernel derivative, not only scalar norm bounds.")
    return reports


if __name__ == "__main__":
    summary()
