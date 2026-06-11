"""Euler-measure decomposition of the variational stress kernel.

The stress-kernel witness rewrites atom sensitivities as

    2 Lambda(n) n^{-1/2} k(log n).

This script compares the actual discrete Euler measure

    dmu_E = sum_{n>=2} 2 Lambda(n) n^{-1/2} delta_{log n}

against its prime-number-theorem main density

    dmu_0(U) = 2 exp(U/2) dU.

The point is diagnostic.  If the discrete stress current is mostly explained
by the smooth main density, the proof target may be a canonical-system
density estimate.  If the residual dominates, the arithmetic sampling remains
load-bearing.

Run:
    python3 -m scripts.numerics.witness.prime_defect_euler_measure
"""
from __future__ import annotations

import math

import numpy as np

from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points
from .prime_defect_stress_kernel import edge_report, kernel_values


LOG2 = math.log(2.0)


def _trapz(values: np.ndarray, grid: np.ndarray) -> float:
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trap(values, x=grid))


def is_prime_power_label(label: str) -> bool:
    return "^" in label


def cumulative_trapezoid(values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    out = np.zeros_like(values)
    if len(values) <= 1:
        return out
    increments = 0.5 * (values[1:] + values[:-1]) * np.diff(grid)
    out[1:] = np.cumsum(increments)
    return out


def build_integrator(report: dict, lo: float, hi: float, ngrid: int = 8001) -> dict:
    Us = np.linspace(lo, hi, ngrid)
    vals = kernel_values(report["density"], Us)
    weight = 2.0 * np.exp(0.5 * Us)
    signed = weight * vals
    absolute = weight * np.abs(vals)
    return {
        "Us": Us,
        "signed_cum": cumulative_trapezoid(signed, Us),
        "abs_cum": cumulative_trapezoid(absolute, Us),
    }


def _interp_cum(integrator: dict, key: str, U: float) -> float:
    Us = integrator["Us"]
    Uc = min(max(float(U), float(Us[0])), float(Us[-1]))
    return float(np.interp(Uc, Us, integrator[key]))


def continuous_integral(integrator: dict, lo: float, hi: float) -> dict:
    if hi <= lo:
        return {"signed": 0.0, "absolute": 0.0}
    signed = _interp_cum(integrator, "signed_cum", hi) - _interp_cum(integrator, "signed_cum", lo)
    absolute = _interp_cum(integrator, "abs_cum", hi) - _interp_cum(integrator, "abs_cum", lo)
    return {"signed": signed, "absolute": absolute}


def discrete_sums(report: dict, region: str | None = None) -> dict:
    rows = [
        row for row in report["samples"]
        if region is None or row["region"] == region
    ]
    prime_rows = [row for row in rows if not is_prime_power_label(row["label"])]
    power_rows = [row for row in rows if is_prime_power_label(row["label"])]
    signed = sum(row["weighted"] for row in rows)
    absolute = sum(abs(row["weighted"]) for row in rows)
    prime_sum = sum(row["weighted"] for row in prime_rows)
    power_sum = sum(row["weighted"] for row in power_rows)
    return {
        "signed": float(signed),
        "absolute": float(absolute),
        "prime": float(prime_sum),
        "prime_power": float(power_sum),
        "count": len(rows),
    }


def edge_measure_report(ambient, points, left: float, right: float) -> dict:
    report = edge_report(ambient, points, left, right)
    integrator = build_integrator(report, LOG2, right)
    old_lo = LOG2
    old_hi = left
    new_lo = max(LOG2, left)
    new_hi = right
    old_disc = discrete_sums(report, "old")
    new_disc = discrete_sums(report, "new")
    all_disc = discrete_sums(report)
    old_main = continuous_integral(integrator, old_lo, old_hi)
    new_main = continuous_integral(integrator, new_lo, new_hi)
    all_main = continuous_integral(integrator, LOG2, right)
    return {
        "edge_report": report,
        "integrator": integrator,
        "left": left,
        "right": right,
        "old_disc": old_disc,
        "new_disc": new_disc,
        "all_disc": all_disc,
        "old_main": old_main,
        "new_main": new_main,
        "all_main": all_main,
        "old_residual": old_disc["signed"] - old_main["signed"],
        "new_residual": new_disc["signed"] - new_main["signed"],
        "all_residual": all_disc["signed"] - all_main["signed"],
    }


def late_cumulative_table(report: dict) -> list[dict]:
    edge = report["edge_report"]
    integrator = report["integrator"]
    rows = [row for row in edge["samples"] if row["region"] == "old"]
    out = []
    cumulative_disc = 0.0
    last = LOG2
    cumulative_main = 0.0
    for row in rows:
        U = row["logn"]
        if U > last:
            cumulative_main += continuous_integral(integrator, last, U)["signed"]
        cumulative_disc += row["weighted"]
        out.append({
            "label": row["label"],
            "U": U,
            "discrete_step": row["weighted"],
            "discrete_cum": cumulative_disc,
            "main_cum": cumulative_main,
            "residual": cumulative_disc - cumulative_main,
        })
        last = U
    return out


def _ratio(num: float, den: float) -> float:
    if den == 0.0:
        return float("nan")
    return num / den


def _print_edge(report: dict) -> None:
    left, right = report["left"], report["right"]
    old_d = report["old_disc"]
    old_m = report["old_main"]
    new_d = report["new_disc"]
    new_m = report["new_main"]
    all_d = report["all_disc"]
    all_m = report["all_main"]
    print(f"\n[edge {left:.2f}->{right:.2f}]")
    print("      region   discrete   smooth main   residual   |disc|    |main|    prime    powers")
    print(f"      old      {old_d['signed']:+.4f}    "
          f"{old_m['signed']:+.4f}     "
          f"{report['old_residual']:+.4f}   "
          f"{old_d['absolute']:+.4f}  "
          f"{old_m['absolute']:+.4f}  "
          f"{old_d['prime']:+.4f}  "
          f"{old_d['prime_power']:+.4f}")
    print(f"      new      {new_d['signed']:+.4f}    "
          f"{new_m['signed']:+.4f}     "
          f"{report['new_residual']:+.4f}   "
          f"{new_d['absolute']:+.4f}  "
          f"{new_m['absolute']:+.4f}  "
          f"{new_d['prime']:+.4f}  "
          f"{new_d['prime_power']:+.4f}")
    print(f"      all      {all_d['signed']:+.4f}    "
          f"{all_m['signed']:+.4f}     "
          f"{report['all_residual']:+.4f}   "
          f"{all_d['absolute']:+.4f}  "
          f"{all_m['absolute']:+.4f}  "
          f"{all_d['prime']:+.4f}  "
          f"{all_d['prime_power']:+.4f}")
    print("      residual/main ratios: "
          f"old {_ratio(report['old_residual'], old_m['signed']):+.3f}, "
          f"new {_ratio(report['new_residual'], new_m['signed']):+.3f}, "
          f"all {_ratio(report['all_residual'], all_m['signed']):+.3f}")


def _print_late_cumulative(report: dict) -> None:
    print("\n[late cumulative: discrete Euler measure vs smooth main, 3.00->3.24]")
    print("      atom   U      step      discrete   smooth main   residual")
    for row in late_cumulative_table(report):
        print(f"      {row['label']:<4} "
              f"{row['U']:.3f}  "
              f"{row['discrete_step']:+.4f}  "
              f"{row['discrete_cum']:+.4f}   "
              f"{row['main_cum']:+.4f}     "
              f"{row['residual']:+.4f}")


def summary() -> dict:
    print("=" * 78)
    print("Euler-measure decomposition of the variational stress kernel")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_measure_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    late = reports[(3.00, 3.24)]
    _print_late_cumulative(late)

    print("\nInterpretation:")
    print("  * The smooth PNT density explains only part of the Euler stress sum.")
    print("    On several edges the residual is comparable to or larger than the")
    print("    main term, so arithmetic discreteness remains load-bearing.")
    print("  * Prime powers are not negligible in the old-history current; they")
    print("    often supply a sizeable correction to the prime-only contribution.")
    print("  * The proof target is therefore not just a continuous density bound.")
    print("    It needs an explicit-formula/Euler-product identity for the discrete")
    print("    measure sampled by the critical stress kernel.")
    return reports


if __name__ == "__main__":
    summary()
