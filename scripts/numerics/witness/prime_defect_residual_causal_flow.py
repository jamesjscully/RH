"""Causal prefix flow of the exact Euler residual controller.

The bounded-control optimizer can choose all residual-cell gains with full
lookahead.  The Euler product does not: residual cells arrive in log-order.
This witness starts from the smooth PNT-density margin and adds the exact
smooth-to-discrete residual cells chronologically:

    M_k = M_smooth + R_2 + R_3 + ... + R_{n_k}.

It tracks the compressed minimum eigenvalue along the path.  Negative prefixes
measure the storage deficit a causal/Riccati proof would need to carry until
later cells repair the cone.

Run:
    python3 -m scripts.numerics.witness.prime_defect_residual_causal_flow
"""
from __future__ import annotations

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_measure_surrogate import smooth_prime_operator
from .prime_defect_residual_control import edge_basis, residual_cells
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points


def edge_flow(ambient, points, left: float, right: float) -> dict:
    B = edge_basis(ambient, points, left, right)
    smooth = _sym(ambient.gram["Winf"] - smooth_prime_operator(ambient, right))
    block = _sym(B.T @ smooth @ B)
    cells = residual_cells(ambient, right)

    rows = []
    eigs, vecs = np.linalg.eigh(block)
    current_min = float(eigs[0])
    current_vec = vecs[:, 0]
    rows.append({
        "label": "smooth",
        "n": None,
        "before_min": current_min,
        "after_min": current_min,
        "delta_min": 0.0,
        "ray_before": 0.0,
    })

    for n, cell in sorted(cells.items()):
        comp = _sym(B.T @ cell @ B)
        ray = float(current_vec.T @ comp @ current_vec)
        before = current_min
        next_block = _sym(block + comp)
        eigs, vecs = np.linalg.eigh(next_block)
        after = float(eigs[0])
        rows.append({
            "label": str(n),
            "n": n,
            "before_min": before,
            "after_min": after,
            "delta_min": after - before,
            "ray_before": ray,
        })
        block = next_block
        current_min = after
        current_vec = vecs[:, 0]

    mins = [row["after_min"] for row in rows]
    first_positive = next(
        (i for i, row in enumerate(rows) if row["after_min"] > 1e-9),
        None,
    )
    deepest_idx = int(np.argmin(mins))
    final = rows[-1]
    return {
        "left": left,
        "right": right,
        "rows": rows,
        "first_positive_index": first_positive,
        "deepest_index": deepest_idx,
        "storage_depth": max(0.0, -mins[deepest_idx]),
        "final_min": final["after_min"],
    }


def _label(row: dict) -> str:
    return row["label"]


def _print_edge(report: dict, topn: int = 6) -> None:
    rows = report["rows"]
    first_pos = report["first_positive_index"]
    first_text = "never" if first_pos is None else f"{first_pos}/{len(rows)-1} at {_label(rows[first_pos])}"
    deepest = rows[report["deepest_index"]]
    print(f"\n[edge {report['left']:.2f}->{report['right']:.2f}] "
          f"storage depth {report['storage_depth']:.3e}, "
          f"final min {report['final_min']:+.3e}, "
          f"first positive {first_text}, "
          f"deepest {_label(deepest)} {deepest['after_min']:+.3e}")

    print("      chronological prefix tail:")
    for idx, row in list(enumerate(rows))[-min(topn, len(rows)):]:
        print(f"        k={idx:2d} {row['label']:<6} "
              f"after={row['after_min']:+.3e} "
              f"delta={row['delta_min']:+.3e} "
              f"ray(before)={row['ray_before']:+.3e}")

    repairs = sorted(
        [row for row in rows[1:] if row["delta_min"] > 0.0],
        key=lambda row: row["delta_min"],
        reverse=True,
    )[:topn]
    harms = sorted(
        [row for row in rows[1:] if row["delta_min"] < 0.0],
        key=lambda row: row["delta_min"],
    )[:topn]
    print("      largest prefix repairs:")
    for row in repairs:
        print(f"        {row['label']:<6} delta={row['delta_min']:+.3e} after={row['after_min']:+.3e}")
    print("      largest prefix harms:")
    for row in harms:
        print(f"        {row['label']:<6} delta={row['delta_min']:+.3e} after={row['after_min']:+.3e}")


def summary() -> dict:
    print("=" * 78)
    print("Causal prefix flow of exact Euler residual cells")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_flow(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    print("\nInterpretation:")
    print("  * The exact residual controller often stays negative until very late")
    print("    in the chronological cell order; positivity is a terminal effect.")
    print("  * Prefix harms and repairs interlace, so a causal proof needs a")
    print("    storage function for temporary deficits, not monotone progress.")
    print("  * This is the finite Riccati/control target: identify a storage")
    print("    functional whose terminal release is the Schur-complement margin.")
    return reports


if __name__ == "__main__":
    summary()
