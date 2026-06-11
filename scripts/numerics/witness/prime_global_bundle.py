"""Intrinsic global-bundle witness for the Prime-Toeplitz target.

The earlier transgression tests used a local active channel

    [incoming bad vector, jump-negative vector].

That is useful, but it depends on identifying a dominant repairing prime.
This script removes that choice.  For each support edge L it defines the
fiber intrinsically as the bottom spectral subspace of the final pole-killed
Weil margin

    M_L = W_infty,L - P_L.

The resulting finite bundle is then transported through ambient physical L2
projection.  We track:

  * the metric tensor J_L = M_L restricted to the bottom fiber;
  * principal angles of adjacent fibers;
  * the Loewner defect J_L - T^* J_R T;
  * the fitted metric-pair transgression
        log det(J_L + lambda h_L) - log det(T^*(J_R + lambda h_R)T).

Run:
    python3 -m scripts.numerics.witness.prime_global_bundle
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .prime_carleson_flow import (
    FlowConfig,
    _dominant_repair,
    _gram_orthonormalize,
    _metric_transgression,
    _minimum_background_for_psd,
    _physical_gram,
    _physical_shape,
    _sym,
    flow_rows,
)
from .semilocal_2 import _proj_null, build_gram

_TRAP = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


@dataclass
class BundlePoint:
    kind: str
    config: FlowConfig
    result: dict
    rank: int
    margin_eigs: np.ndarray
    spectral_gap: float
    coeffs_l2: np.ndarray
    metric: np.ndarray
    metric_eigs: np.ndarray
    repair_n: int | None
    repair_delta: float

    @property
    def gmax(self) -> float:
        return float(self.result["gmax"])

    @property
    def final_min(self) -> float:
        return float(self.result["final_min"])


def _bottom_bundle_point(config: FlowConfig, kind: str, rank: int) -> BundlePoint:
    """Build the intrinsic bottom-subspace fiber at one support edge."""
    result = flow_rows(config, kind)
    gram = build_gram(config.centers, config.half_width)
    null = _proj_null(gram)
    margin_reduced = _sym(null.T @ result["_final_form_full"] @ null)
    eigs, vecs = np.linalg.eigh(margin_reduced)

    rank = min(rank, vecs.shape[1])
    bottom_full = null @ vecs[:, :rank]
    coeffs_l2 = _gram_orthonormalize(bottom_full, _physical_gram(config))
    metric = _sym(coeffs_l2.T @ result["_final_form_full"] @ coeffs_l2)
    metric_eigs = np.linalg.eigvalsh(metric) if metric.size else np.array([float("nan")])
    repair = _dominant_repair(result)
    spectral_gap = (
        float(eigs[rank] - eigs[rank - 1])
        if rank < len(eigs) else float("nan")
    )
    return BundlePoint(
        kind=kind,
        config=config,
        result=result,
        rank=rank,
        margin_eigs=eigs,
        spectral_gap=spectral_gap,
        coeffs_l2=coeffs_l2,
        metric=metric,
        metric_eigs=metric_eigs,
        repair_n=repair["n"] if repair is not None else None,
        repair_delta=repair["delta_min"] if repair is not None else 0.0,
    )


def bundle_points(configs: list[FlowConfig], kind: str, rank: int = 2) -> list[BundlePoint]:
    return [_bottom_bundle_point(config, kind, rank) for config in configs]


def _point_shapes(points: list[BundlePoint]) -> tuple[np.ndarray, list[np.ndarray]]:
    umax = max(point.config.cmax + point.config.half_width for point in points)
    u = np.linspace(-umax, umax, 7001)
    shapes = []
    for point in points:
        cfg = point.config
        if point.coeffs_l2.shape[1] == 0:
            shapes.append(np.zeros((len(u), 0)))
            continue
        shapes.append(np.column_stack([
            _physical_shape(cfg.centers, cfg.half_width, point.coeffs_l2[:, j], u)
            for j in range(point.coeffs_l2.shape[1])
        ]))
    return u, shapes


def _metric_shift_for_logdet(J_left: np.ndarray, J_right: np.ndarray) -> float:
    """Smallest scalar shift making both endpoint metrics strictly positive."""
    min_left = float(np.linalg.eigvalsh(_sym(J_left))[0])
    min_right = float(np.linalg.eigvalsh(_sym(J_right))[0])
    return max(0.0, 1e-9 - min_left, 1e-9 - min_right)


def bundle_edges(points: list[BundlePoint]) -> list[dict]:
    """Adjacent-edge connection and transgression diagnostics."""
    u, shapes = _point_shapes(points)
    rows = []
    for i in range(len(points) - 1):
        left = points[i]
        right = points[i + 1]
        left_shapes = shapes[i]
        right_shapes = shapes[i + 1]
        if left_shapes.shape[1] == 0 or right_shapes.shape[1] == 0:
            continue

        T = np.array([[
            float(_TRAP(right_shapes[:, a] * left_shapes[:, b], x=u))
            for b in range(left_shapes.shape[1])
        ] for a in range(right_shapes.shape[1])])
        svals = np.linalg.svd(T, compute_uv=False)
        clipped = np.clip(svals, 0.0, 1.0)
        angles = np.arccos(clipped)
        dL = right.gmax - left.gmax

        raw_defect = _sym(left.metric - T.T @ right.metric @ T)
        l2_capacity = _sym(np.eye(T.shape[1]) - T.T @ T)
        defect_lambda = _minimum_background_for_psd(raw_defect, l2_capacity)
        spd_lambda = _metric_shift_for_logdet(left.metric, right.metric)
        lam = max(defect_lambda, spd_lambda) if np.isfinite(defect_lambda) else float("inf")
        transgression = _metric_transgression(left.metric, right.metric, T, lam)
        raw_transgression = _metric_transgression(left.metric, right.metric, T, spd_lambda)

        if T.shape[0] == T.shape[1]:
            sign, logabsdet = np.linalg.slogdet(T)
            det_sign = int(sign)
            logabsdet = float(logabsdet)
        else:
            det_sign = 0
            logabsdet = float("nan")

        rows.append({
            "kind": left.kind,
            "left_gmax": left.gmax,
            "right_gmax": right.gmax,
            "dL": dL,
            "left_repair_n": left.repair_n,
            "right_repair_n": right.repair_n,
            "left_final_min": left.final_min,
            "right_final_min": right.final_min,
            "left_metric_min": float(left.metric_eigs[0]),
            "right_metric_min": float(right.metric_eigs[0]),
            "left_gap": left.spectral_gap,
            "right_gap": right.spectral_gap,
            "svals": svals,
            "angle_frobenius_density": float(np.linalg.norm(angles) / dL),
            "sin_frobenius_density": float(np.sqrt(np.sum(1.0 - clipped ** 2)) / dL),
            "raw_defect_eigs": np.linalg.eigvalsh(raw_defect),
            "l2_capacity_eigs": np.linalg.eigvalsh(l2_capacity),
            "defect_lambda": defect_lambda,
            "spd_lambda": spd_lambda,
            "lambda": lam,
            "raw_transgression": raw_transgression,
            "fitted_transgression": transgression,
            "det_sign": det_sign,
            "logabsdet": logabsdet,
        })
    return rows


def _repair_label(n: int | None) -> str:
    return "none" if n is None else f"n{n}"


def _print_points(points: list[BundlePoint]) -> None:
    print(f"\n[{points[0].kind}] intrinsic bottom fibers")
    print("    fiber = bottom 2D spectral subspace of final pole-killed margin")
    print("      gmax   repair landmark   final min    J eig range          spectral gap")
    for point in points:
        print(f"      {point.gmax:.2f}   "
              f"{_repair_label(point.repair_n):<7}          "
              f"{point.final_min:+.2e}   "
              f"[{point.metric_eigs[0]:+.2e},{point.metric_eigs[-1]:+.2e}]   "
              f"{point.spectral_gap:+.2e}")


def _print_edges(rows: list[dict], label: str) -> None:
    print(f"\n[{label}] intrinsic bundle connection")
    print("      edge        repairs      svals          angle/dL  raw min    lambdas(def,spd)  Tau      conn")
    for row in rows:
        svals = ",".join(f"{s:.3f}" for s in row["svals"])
        tr = row["fitted_transgression"]
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{_repair_label(row['left_repair_n'])}->{_repair_label(row['right_repair_n']):<5}  "
              f"[{svals}]   "
              f"{row['angle_frobenius_density']:.3f}    "
              f"{row['raw_defect_eigs'][0]:+.2e}   "
              f"({row['defect_lambda']:.3g},{row['spd_lambda']:.3g})   "
              f"{tr['tau']:+.3f}   "
              f"{tr['connection_volume']:+.3f}")


def cumulative_summary(rows: list[dict]) -> dict:
    finite = [row for row in rows if np.isfinite(row["fitted_transgression"]["tau"])]
    if not finite:
        return {
            "tau": float("nan"),
            "metric_delta": float("nan"),
            "connection_volume": float("nan"),
            "max_lambda": float("nan"),
            "orientation_product": 0,
            "max_angle_density": float("nan"),
        }
    orientation = 1
    for row in finite:
        orientation *= row["det_sign"] if row["det_sign"] != 0 else 0
    return {
        "tau": float(sum(row["fitted_transgression"]["tau"] for row in finite)),
        "metric_delta": float(sum(row["fitted_transgression"]["metric_delta"] for row in finite)),
        "connection_volume": float(sum(row["fitted_transgression"]["connection_volume"] for row in finite)),
        "max_lambda": float(max(row["lambda"] for row in finite)),
        "orientation_product": orientation,
        "max_angle_density": float(max(row["angle_frobenius_density"] for row in finite)),
    }


def _print_cumulative(zeta_edges: list[dict], dh_edges: list[dict]) -> None:
    print("\n[cumulative path action]")
    print("      kind   sum Tau   metric part   connection part   max lambda   max angle/dL   orient")
    for label, rows in (("zeta", zeta_edges), ("DH", dh_edges)):
        total = cumulative_summary(rows)
        print(f"      {label:<5}  "
              f"{total['tau']:+.3f}    "
              f"{total['metric_delta']:+.3f}       "
              f"{total['connection_volume']:+.3f}          "
              f"{total['max_lambda']:.3g}       "
              f"{total['max_angle_density']:.3f}        "
              f"{total['orientation_product']:+d}")
    print("    reading: on an interval there is no ordinary Chern class to integrate;")
    print("    the finite invariant is a relative transgression measure along the path.")


def summary() -> dict:
    print("=" * 78)
    print("Intrinsic Prime-Toeplitz global-bundle witness")
    print("=" * 78)

    configs = [
        FlowConfig(ncenters=17, half_width=0.10, cmax=cmax)
        for cmax in (0.70, 0.76, 0.84, 0.95, 1.05, 1.16, 1.28, 1.40, 1.52)
    ]
    zeta_points = bundle_points(configs, "zeta", rank=2)
    dh_points = bundle_points(configs, "DH", rank=2)
    _print_points(zeta_points)
    _print_points(dh_points)

    zeta_edges = bundle_edges(zeta_points)
    dh_edges = bundle_edges(dh_points)
    _print_edges(zeta_edges, "zeta")
    _print_edges(dh_edges, "DH")
    _print_cumulative(zeta_edges, dh_edges)

    print("\nInterpretation:")
    print("  * This bottom-subspace bundle is intrinsic to the final margin M_L.")
    print("  * Zeta keeps the fiber metric positive while the path accumulates positive")
    print("    relative transgression; the landmarks still line up with the prime relay.")
    print("  * DH needs a large positive background once the bottom metric goes negative,")
    print("    so its log-det action is a stabilized diagnostic, not a positive metric.")
    print("  * The cohomological target is therefore singular/relative: continuous")
    print("    curvature density between support edges plus Euler point defects at jumps.")

    return {
        "zeta_points": zeta_points,
        "DH_points": dh_points,
        "zeta_edges": zeta_edges,
        "DH_edges": dh_edges,
        "zeta_cumulative": cumulative_summary(zeta_edges),
        "DH_cumulative": cumulative_summary(dh_edges),
    }


if __name__ == "__main__":
    summary()
