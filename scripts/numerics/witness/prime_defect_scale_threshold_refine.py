"""Basis-refinement stress test for coefficient-scale thresholds.

This repeats the scale-threshold diagnostic for neighboring finite Sonin
windows.  The goal is not to prove continuum stability, but to test whether
the old-history rigidity survives ordinary basis refinement.

Run:
    python3 -m scripts.numerics.witness.prime_defect_scale_threshold_refine
"""
from __future__ import annotations

import math

from .prime_defect_scale_threshold import (
    _edge_text,
    _scale_of,
    add_refined_transitions,
    scan_mode,
    summarize_mode,
)
from .prime_nested_cone import build_ambient, point
from .prime_shell_coupling_bound import GMAXS


CONFIGS = (
    (17, 0.10),
    (21, 0.08),
    (25, 0.06),
)


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


def _transition_value(transition: dict | None, lower: bool) -> float | None:
    if transition is None:
        return None
    vals = (transition["pass_scale"], transition["fail_scale"])
    return min(vals) if lower else max(vals)


def _fmt_float(value: float | None) -> str:
    if value is None:
        return "scan"
    return f"{value:.6f}"


def _fmt_grid(summary: dict) -> str:
    if summary["anchor"] is None:
        return "none"
    return f"[{summary['lo']:.3f},{summary['hi']:.3f}]"


def _fmt_refined(summary: dict) -> str:
    if summary["anchor"] is None:
        return "none"
    lo = _transition_value(summary.get("lower_transition"), lower=True)
    hi = _transition_value(summary.get("upper_transition"), lower=False)
    if lo is None:
        lo_text = f"<={summary['lo']:.3f}"
    else:
        lo_text = _fmt_float(lo)
    if hi is None:
        hi_text = f">={summary['hi']:.3f}"
    else:
        hi_text = _fmt_float(hi)
    return f"[{lo_text},{hi_text}]"


def _fmt_blockers(summary: dict) -> str:
    if summary["anchor"] is None:
        return "none"
    lower = summary.get("lower_transition")
    upper = summary.get("upper_transition")
    lower_bad = "scan" if lower is None else _edge_text(lower["bad_row"])
    upper_bad = "scan" if upper is None else _edge_text(upper["bad_row"])
    return f"{lower_bad} / {upper_bad}"


def _summary_for_mode(ambient, points, mode: str) -> dict:
    if mode in {"old", "global"}:
        rows = scan_mode(ambient, points, mode, 0.80, 1.20, 0.002)
    elif mode == "new":
        rows = scan_mode(ambient, points, mode, 0.00, 1.50, 0.005)
    else:
        raise ValueError(f"unknown mode: {mode}")
    summary = summarize_mode(rows, mode)
    add_refined_transitions(ambient, points, summary)
    if summary["anchor"] is not None:
        exact = min(rows, key=lambda row: abs(_scale_of(row, mode) - 1.0))
        summary["exact_max_rho"] = exact["max_rho"]
        summary["exact_min_defect"] = exact["min_defect"]
    return summary


def _min_defect_text(summary: dict) -> str:
    value = summary.get("exact_min_defect")
    if value is None or math.isnan(value):
        return "n/a"
    return f"{value:+.4f}"


def summary() -> list[dict]:
    print("=" * 78)
    print("Basis-refinement stress test for coefficient-scale thresholds")
    print("=" * 78)
    print("basis       mode     grid run        refined local interval     defect@1   blockers")

    rows = []
    for ncenters, half_width in CONFIGS:
        ambient, points = build_config(ncenters, half_width)
        basis = f"n{ncenters}/hw{half_width:.2f}"
        for mode in ("old", "global", "new"):
            mode_summary = _summary_for_mode(ambient, points, mode)
            rows.append({
                "basis": basis,
                "mode": mode,
                "summary": mode_summary,
            })
            print(f"{basis:<11} {mode:<8} "
                  f"{_fmt_grid(mode_summary):<15} "
                  f"{_fmt_refined(mode_summary):<26} "
                  f"{_min_defect_text(mode_summary):<9} "
                  f"{_fmt_blockers(mode_summary)}")

    print("\nInterpretation:")
    print("  * The old/global coefficient tube stays narrow across these finite")
    print("    refinements and is usually closed by the last shell.")
    print("  * The new-shell upper tolerance is wider and fails at earlier/later")
    print("    shell edges depending on basis resolution.")
    return rows


if __name__ == "__main__":
    summary()
