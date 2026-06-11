"""Stress tests for the intrinsic Prime-Toeplitz bundle.

``prime_global_bundle.py`` replaces repair-label channels by the intrinsic
bottom spectral subspace of the final margin.  This script tests whether that
object is stable enough to be a useful geometric target:

  * Does zeta keep the bottom metric positive under rank changes?
  * Does DH leave the positive cone robustly under rank changes?
  * Do bottom fibers at the same support edge stabilize under basis refinement?
  * Are intrinsic edge transgressions stable across refinements?

Run:
    python3 -m scripts.numerics.witness.prime_global_bundle_stress
"""
from __future__ import annotations

import numpy as np

from .prime_carleson_flow import FlowConfig, _physical_shape
from .prime_global_bundle import (
    BundlePoint,
    _bottom_bundle_point,
    bundle_edges,
    cumulative_summary,
)

_TRAP = np.trapezoid if hasattr(np, "trapezoid") else np.trapz

REFINEMENTS = (
    (13, 0.14),
    (17, 0.10),
    (21, 0.08),
    (25, 0.06),
)
LONG_GMAXS = (1.60, 1.72, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24)
COHERENCE_GMAXS = (1.88, 2.10, 2.30, 2.76, 3.00)
EDGE_GMAXS = ((1.88, 2.10), (2.10, 2.30), (2.52, 2.76), (2.76, 3.00))

_POINT_CACHE: dict[tuple[str, float, int, float, int], BundlePoint] = {}


def config_for_gmax(target_gmax: float, ncenters: int, half_width: float) -> FlowConfig:
    cmax = target_gmax / 2.0 - half_width
    if cmax <= 0.0:
        raise ValueError(f"nonpositive cmax for gmax={target_gmax}, hw={half_width}")
    return FlowConfig(ncenters=ncenters, half_width=half_width, cmax=cmax)


def cached_point(kind: str, target_gmax: float, ncenters: int, half_width: float,
                 rank: int = 2) -> BundlePoint:
    key = (kind, target_gmax, ncenters, half_width, rank)
    if key not in _POINT_CACHE:
        cfg = config_for_gmax(target_gmax, ncenters, half_width)
        _POINT_CACHE[key] = _bottom_bundle_point(cfg, kind, rank)
    return _POINT_CACHE[key]


def _repair_label(point: BundlePoint) -> str:
    return "none" if point.repair_n is None else f"n{point.repair_n}"


def _shapes(point: BundlePoint, u: np.ndarray) -> np.ndarray:
    cfg = point.config
    return np.column_stack([
        _physical_shape(cfg.centers, cfg.half_width, point.coeffs_l2[:, j], u)
        for j in range(point.coeffs_l2.shape[1])
    ])


def _overlap_svals(left: BundlePoint, right: BundlePoint) -> np.ndarray:
    umax = max(
        left.config.cmax + left.config.half_width,
        right.config.cmax + right.config.half_width,
    )
    u = np.linspace(-umax, umax, 7001)
    left_shapes = _shapes(left, u)
    right_shapes = _shapes(right, u)
    overlap = np.array([[
        float(_TRAP(right_shapes[:, a] * left_shapes[:, b], x=u))
        for b in range(left_shapes.shape[1])
    ] for a in range(right_shapes.shape[1])])
    return np.linalg.svd(overlap, compute_uv=False)


def rank_sensitivity() -> list[dict]:
    rows = []
    for kind in ("zeta", "DH"):
        for rank in (1, 2, 3, 4):
            points = [
                cached_point(kind, gmax, 17, 0.10, rank=rank)
                for gmax in LONG_GMAXS
            ]
            edges = bundle_edges(points)
            total = cumulative_summary(edges)
            metric_mins = [float(point.metric_eigs[0]) for point in points]
            first_bad = next(
                (point.gmax for point in points if float(point.metric_eigs[0]) < -1e-9),
                None,
            )
            rows.append({
                "kind": kind,
                "rank": rank,
                "min_metric": min(metric_mins),
                "first_bad_gmax": first_bad,
                "sum_tau": total["tau"],
                "metric_part": total["metric_delta"],
                "connection_part": total["connection_volume"],
                "max_lambda": total["max_lambda"],
                "orientation": total["orientation_product"],
            })
    return rows


def same_edge_basis_coherence(kind: str = "zeta", rank: int = 2) -> list[dict]:
    rows = []
    for gmax in COHERENCE_GMAXS:
        points = [
            cached_point(kind, gmax, ncenters, half_width, rank=rank)
            for ncenters, half_width in REFINEMENTS
        ]
        for left, right in zip(points, points[1:]):
            svals = _overlap_svals(left, right)
            rows.append({
                "kind": kind,
                "rank": rank,
                "gmax": gmax,
                "left_basis": f"n{left.config.ncenters}/hw{left.config.half_width:.2f}",
                "right_basis": f"n{right.config.ncenters}/hw{right.config.half_width:.2f}",
                "left_metric_min": float(left.metric_eigs[0]),
                "right_metric_min": float(right.metric_eigs[0]),
                "left_repair": _repair_label(left),
                "right_repair": _repair_label(right),
                "svals": svals,
            })
    return rows


def edge_refinement(kind: str = "zeta", rank: int = 2) -> list[dict]:
    rows = []
    for left_gmax, right_gmax in EDGE_GMAXS:
        for ncenters, half_width in REFINEMENTS:
            points = [
                cached_point(kind, left_gmax, ncenters, half_width, rank=rank),
                cached_point(kind, right_gmax, ncenters, half_width, rank=rank),
            ]
            edge = bundle_edges(points)[0]
            tr = edge["fitted_transgression"]
            rows.append({
                "kind": kind,
                "rank": rank,
                "left_gmax": left_gmax,
                "right_gmax": right_gmax,
                "basis": f"n{ncenters}/hw{half_width:.2f}",
                "left_repair": _repair_label(points[0]),
                "right_repair": _repair_label(points[1]),
                "left_metric_min": float(points[0].metric_eigs[0]),
                "right_metric_min": float(points[1].metric_eigs[0]),
                "svals": edge["svals"],
                "defect_lambda": edge["defect_lambda"],
                "spd_lambda": edge["spd_lambda"],
                "tau": tr["tau"],
                "metric_delta": tr["metric_delta"],
                "connection_volume": tr["connection_volume"],
                "raw_min": float(edge["raw_defect_eigs"][0]),
            })
    return rows


def _print_rank_sensitivity(rows: list[dict]) -> None:
    print("\n[1] Rank sensitivity of intrinsic bottom bundle, ncenters=17/hw=0.10")
    print("      kind   rank  min J eig   first bad L   sum Tau   metric    connection  max lambda  orient")
    for row in rows:
        first_bad = "none" if row["first_bad_gmax"] is None else f"{row['first_bad_gmax']:.2f}"
        print(f"      {row['kind']:<5}  "
              f"{row['rank']:<4d}  "
              f"{row['min_metric']:+.2e}  "
              f"{first_bad:<11}  "
              f"{row['sum_tau']:+.3f}   "
              f"{row['metric_part']:+.3f}   "
              f"{row['connection_part']:+.3f}     "
              f"{row['max_lambda']:.3g}      "
              f"{row['orientation']:+d}")
    print("      reading: zeta positivity should survive rank changes; DH should leave")
    print("      the positive cone before any log-det stabilization is trusted.")


def _print_coherence(rows: list[dict], label: str) -> None:
    print(f"\n[2] Same-edge basis coherence for {label} bottom rank-2 fibers")
    print("      gmax   basis pair              repairs       min J eigs          overlap svals")
    for row in rows:
        svals = ",".join(f"{s:.3f}" for s in row["svals"])
        print(f"      {row['gmax']:.2f}   "
              f"{row['left_basis']}->{row['right_basis']:<10}  "
              f"{row['left_repair']}->{row['right_repair']:<5}  "
              f"{row['left_metric_min']:+.2e}/{row['right_metric_min']:+.2e}   "
              f"[{svals}]")
    print("      reading: the near-null line is often stable; the second direction can")
    print("      rotate when the spectral gap is tiny, so rank-2 data must be gap-aware.")


def _print_edge_refinement(rows: list[dict], label: str) -> None:
    print(f"\n[3] Edge transgression refinement for {label} intrinsic rank-2 bundle")
    print("      edge        basis       repairs      min J eigs          lambda(def,spd)  Tau     conn")
    for row in rows:
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['basis']:<10}  "
              f"{row['left_repair']}->{row['right_repair']:<5}  "
              f"{row['left_metric_min']:+.2e}/{row['right_metric_min']:+.2e}   "
              f"({row['defect_lambda']:.3g},{row['spd_lambda']:.3g})   "
              f"{row['tau']:+.3f}  "
              f"{row['connection_volume']:+.3f}")
    print("      reading: stable sign of min J matters more than stable Tau magnitude;")
    print("      Tau changes when a refinement resolves a different low-energy direction.")


def summary() -> dict:
    print("=" * 78)
    print("Intrinsic Prime-Toeplitz global-bundle stress tests")
    print("=" * 78)

    rank_rows = rank_sensitivity()
    _print_rank_sensitivity(rank_rows)

    zeta_coherence = same_edge_basis_coherence("zeta", rank=2)
    _print_coherence(zeta_coherence, "zeta")

    dh_coherence = same_edge_basis_coherence("DH", rank=2)
    _print_coherence(dh_coherence, "DH")

    zeta_edges = edge_refinement("zeta", rank=2)
    _print_edge_refinement(zeta_edges, "zeta")

    dh_edges = edge_refinement("DH", rank=2)
    _print_edge_refinement(dh_edges, "DH")

    print("\nInterpretation:")
    print("  * The robust invariant is positive-cone membership of the intrinsic metric,")
    print("    not the absolute value of the log-det transgression.")
    print("  * The bottom two-plane is a useful obstruction microscope, but tiny spectral")
    print("    gaps make the second direction rotate under refinement.")
    print("  * A proof should be formulated for the full metric-pair flow; the spectral")
    print("    bundle is diagnostic evidence, not a noncircular construction by itself.")

    return {
        "rank_sensitivity": rank_rows,
        "zeta_coherence": zeta_coherence,
        "DH_coherence": dh_coherence,
        "zeta_edge_refinement": zeta_edges,
        "DH_edge_refinement": dh_edges,
    }


if __name__ == "__main__":
    summary()
