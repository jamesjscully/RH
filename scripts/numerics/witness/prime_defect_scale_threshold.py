"""Fine coefficient-scale thresholds for passive shell transfer.

The coarse scale-phase witness says that zeta's passive chain is rigid in the
old-history direction.  This script refines that statement without assuming
global monotonicity: for each one-parameter scaling direction it scans the
finite grid, finds all passive runs, and reports the run containing the exact
Euler scale.

Run:
    python3 -m scripts.numerics.witness.prime_defect_scale_threshold
"""
from __future__ import annotations

import math

import numpy as np

from .prime_defect_scale_phase import ambient_and_points, path_eval


def _scale_of(row: dict, mode: str) -> float:
    if mode in {"old", "global"}:
        return float(row["old_scale"])
    if mode == "new":
        return float(row["new_scale"])
    raise ValueError(f"unknown mode: {mode}")


def _eval_mode(ambient, points, mode: str, scale: float) -> dict:
    if mode == "old":
        return path_eval(ambient, points, old_scale=scale, new_scale=1.0)
    if mode == "new":
        return path_eval(ambient, points, old_scale=1.0, new_scale=scale)
    if mode == "global":
        return path_eval(ambient, points, old_scale=scale, new_scale=scale)
    raise ValueError(f"unknown mode: {mode}")


def scan_mode(ambient, points, mode: str, lo: float, hi: float, step: float) -> list[dict]:
    count = int(round((hi - lo) / step))
    scales = [round(lo + i * step, 10) for i in range(count + 1)]
    if not math.isclose(scales[-1], hi, abs_tol=step / 10.0):
        scales.append(round(hi, 10))
    return [_eval_mode(ambient, points, mode, float(scale)) for scale in scales]


def passive_runs(rows: list[dict], mode: str) -> list[tuple[int, int]]:
    runs = []
    start = None
    for idx, row in enumerate(rows):
        if row["passive"]:
            if start is None:
                start = idx
        elif start is not None:
            runs.append((start, idx - 1))
            start = None
    if start is not None:
        runs.append((start, len(rows) - 1))
    return runs


def anchored_run(rows: list[dict], mode: str, anchor: float = 1.0) -> tuple[int, int] | None:
    runs = passive_runs(rows, mode)
    for start, end in runs:
        lo = _scale_of(rows[start], mode)
        hi = _scale_of(rows[end], mode)
        if lo <= anchor <= hi:
            return start, end
    return None


def _edge_text(row: dict | None) -> str:
    if row is None:
        return "scan boundary"
    edge = row["first_bad_edge"]
    if edge is None:
        return "none"
    return f"{edge[0]:.2f}->{edge[1]:.2f}"


def _rho_text(row: dict | None) -> str:
    if row is None:
        return "n/a"
    rho = row["max_rho"]
    if math.isnan(rho):
        return "invalid"
    return f"{rho:.6f}"


def summarize_mode(rows: list[dict], mode: str) -> dict:
    runs = passive_runs(rows, mode)
    anchor = anchored_run(rows, mode)
    if anchor is None:
        return {
            "mode": mode,
            "runs": runs,
            "anchor": None,
            "lower_blocker": None,
            "upper_blocker": None,
        }

    start, end = anchor
    lower = rows[start - 1] if start > 0 else None
    upper = rows[end + 1] if end + 1 < len(rows) else None
    exact = min(rows, key=lambda row: abs(_scale_of(row, mode) - 1.0))
    return {
        "mode": mode,
        "runs": runs,
        "anchor": anchor,
        "lo": _scale_of(rows[start], mode),
        "hi": _scale_of(rows[end], mode),
        "width": _scale_of(rows[end], mode) - _scale_of(rows[start], mode),
        "exact_max_rho": exact["max_rho"],
        "exact_min_defect": exact["min_defect"],
        "lower_blocker": lower,
        "upper_blocker": upper,
    }


def refine_transition(ambient, points, mode: str, good_scale: float, bad_scale: float,
                      iters: int = 24) -> dict:
    """Refine one local pass/fail transition bracket.

    This is only a local threshold diagnostic.  The grid scan above is still
    what prevents us from assuming global monotonicity.
    """
    good = float(good_scale)
    bad = float(bad_scale)
    for _ in range(iters):
        mid = 0.5 * (good + bad)
        ev = _eval_mode(ambient, points, mode, mid)
        if ev["passive"]:
            good = mid
        else:
            bad = mid
    bad_row = _eval_mode(ambient, points, mode, bad)
    return {
        "pass_scale": good,
        "fail_scale": bad,
        "bad_row": bad_row,
        "width": abs(good - bad),
    }


def add_refined_transitions(ambient, points, mode_summary: dict) -> None:
    if mode_summary["anchor"] is None:
        return
    mode = mode_summary["mode"]
    lower = mode_summary["lower_blocker"]
    upper = mode_summary["upper_blocker"]
    if lower is not None:
        mode_summary["lower_transition"] = refine_transition(
            ambient,
            points,
            mode,
            good_scale=mode_summary["lo"],
            bad_scale=_scale_of(lower, mode),
        )
    if upper is not None:
        mode_summary["upper_transition"] = refine_transition(
            ambient,
            points,
            mode,
            good_scale=mode_summary["hi"],
            bad_scale=_scale_of(upper, mode),
        )


def joint_corridor(ambient, points,
                   old_scales: np.ndarray, new_scales: np.ndarray) -> list[dict]:
    rows = []
    for old in old_scales:
        passing = []
        blockers = []
        for new in new_scales:
            ev = path_eval(ambient, points, float(old), float(new))
            if ev["passive"]:
                passing.append(float(new))
            else:
                blockers.append(ev)
        rows.append({
            "old": float(old),
            "new_min": min(passing) if passing else None,
            "new_max": max(passing) if passing else None,
            "count": len(passing),
            "first_blocker": blockers[0] if blockers else None,
        })
    return rows


def _print_mode(summary: dict, rows: list[dict]) -> None:
    mode = summary["mode"]
    print(f"\n[1] {mode} scale, passive runs on scanned grid")
    runs = summary["runs"]
    if not runs:
        print("      none")
    else:
        for start, end in runs:
            lo = _scale_of(rows[start], mode)
            hi = _scale_of(rows[end], mode)
            mark = "  <-- contains exact scale" if summary["anchor"] == (start, end) else ""
            print(f"      [{lo:.4f}, {hi:.4f}]  width {hi - lo:.4f}{mark}")

    if summary["anchor"] is None:
        print("      exact scale is not passive on this grid")
        return

    lower = summary["lower_blocker"]
    upper = summary["upper_blocker"]
    print("      exact scale: "
          f"max rho {summary['exact_max_rho']:.6f}, "
          f"min defect {summary['exact_min_defect']:+.6f}")
    print("      lower blocker: "
          f"scale {_scale_of(lower, mode):.4f}, "
          f"rho {_rho_text(lower)}, first bad {_edge_text(lower)}"
          if lower is not None else
          "      lower blocker: scan boundary")
    print("      upper blocker: "
          f"scale {_scale_of(upper, mode):.4f}, "
          f"rho {_rho_text(upper)}, first bad {_edge_text(upper)}"
          if upper is not None else
          "      upper blocker: scan boundary")
    lower_transition = summary.get("lower_transition")
    upper_transition = summary.get("upper_transition")
    if lower_transition is not None:
        lo = min(lower_transition["pass_scale"], lower_transition["fail_scale"])
        hi = max(lower_transition["pass_scale"], lower_transition["fail_scale"])
        print("      lower transition bracket: "
              f"[{lo:.8f}, {hi:.8f}], "
              f"first bad {_edge_text(lower_transition['bad_row'])}")
    if upper_transition is not None:
        lo = min(upper_transition["pass_scale"], upper_transition["fail_scale"])
        hi = max(upper_transition["pass_scale"], upper_transition["fail_scale"])
        print("      upper transition bracket: "
              f"[{lo:.8f}, {hi:.8f}], "
              f"first bad {_edge_text(upper_transition['bad_row'])}")


def _print_joint(rows: list[dict]) -> None:
    print("\n[2] Local old/new corridor")
    print("      old scale   passing new-scale interval   count   first blocker")
    for row in rows:
        if row["count"]:
            interval = f"[{row['new_min']:.3f}, {row['new_max']:.3f}]"
            blocker = row["first_blocker"]
            bad = _edge_text(blocker)
        else:
            interval = "none"
            bad = _edge_text(row["first_blocker"])
        print(f"      {row['old']:.3f}       {interval:<18} {row['count']:3d}     {bad}")


def summary() -> dict:
    print("=" * 78)
    print("Fine coefficient-scale thresholds for passive shell transfer")
    print("=" * 78)
    ambient, points = ambient_and_points()

    specs = {
        "old": (0.80, 1.20, 0.001),
        "global": (0.80, 1.20, 0.001),
        "new": (0.00, 1.50, 0.0025),
    }
    mode_rows = {}
    mode_summaries = {}
    for mode, (lo, hi, step) in specs.items():
        rows = scan_mode(ambient, points, mode, lo, hi, step)
        mode_rows[mode] = rows
        mode_summaries[mode] = summarize_mode(rows, mode)
        add_refined_transitions(ambient, points, mode_summaries[mode])
        _print_mode(mode_summaries[mode], rows)

    old_grid = np.round(np.arange(0.970, 1.0301, 0.005), 3)
    new_grid = np.round(np.arange(0.700, 1.2501, 0.005), 3)
    corridor = joint_corridor(ambient, points, old_grid, new_grid)
    _print_joint(corridor)

    print("\nInterpretation:")
    print("  * The relevant object is the passive corridor containing the exact")
    print("    Euler scale, not a globally monotone stability interval.")
    print("  * Old-history and global rescaling close quickly; incoming-shell")
    print("    rescaling has a wider one-sided tolerance.")
    print("  * The blocker edge identifies where the cumulative Euler history stops")
    print("    balancing the shell transfer.")
    return {
        "mode_rows": mode_rows,
        "mode_summaries": mode_summaries,
        "corridor": corridor,
    }


if __name__ == "__main__":
    summary()
