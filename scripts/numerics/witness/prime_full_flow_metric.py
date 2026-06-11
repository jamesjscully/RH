"""Full finite-rank metric-flow witness for the Prime-Toeplitz target.

The bottom spectral bundle is a useful microscope, but it is still extracted
from the final margin.  This script moves one level closer to the proposed
theorem by using the whole pole-killed finite window as the fiber.

For each support edge L:

    H_L = pole-killed subspace in the raised-cosine window
    J_L = final Weil margin M_L = W_infty,L - P_L, restricted to H_L
    h_L = physical L2 metric, normalized to the identity

Adjacent fibers are connected by ambient L2 projection.  We track positive
cone membership of J_L, and separately the metric-pair transgression.  The
second quantity is expected to be more discretization-sensitive at full rank;
the hard invariant is whether J_L is positive before any stabilizing shift.

Run:
    python3 -m scripts.numerics.witness.prime_full_flow_metric
"""
from __future__ import annotations

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


def config_for_gmax(target_gmax: float, ncenters: int, half_width: float) -> FlowConfig:
    cmax = target_gmax / 2.0 - half_width
    if cmax <= 0.0:
        raise ValueError(f"nonpositive cmax for gmax={target_gmax}, hw={half_width}")
    return FlowConfig(ncenters=ncenters, half_width=half_width, cmax=cmax)


def _metric_shift_for_logdet(J_left: np.ndarray, J_right: np.ndarray) -> float:
    min_left = float(np.linalg.eigvalsh(_sym(J_left))[0])
    min_right = float(np.linalg.eigvalsh(_sym(J_right))[0])
    return max(0.0, 1e-9 - min_left, 1e-9 - min_right)


def _repair_label(result: dict) -> str:
    repair = _dominant_repair(result)
    return "none" if repair is None else f"n{repair['n']}"


def full_point(config: FlowConfig, kind: str) -> dict:
    """Full pole-killed finite fiber with L2-normalized coordinates."""
    result = flow_rows(config, kind)
    gram = build_gram(config.centers, config.half_width)
    null = _proj_null(gram)
    Q = _gram_orthonormalize(null, _physical_gram(config))
    J = _sym(Q.T @ result["_final_form_full"] @ Q)
    eigs = np.linalg.eigvalsh(J)
    return {
        "kind": kind,
        "config": config,
        "result": result,
        "Q": Q,
        "metric": J,
        "metric_eigs": eigs,
        "dimension": int(Q.shape[1]),
        "repair_label": _repair_label(result),
    }


def _point_shapes(points: list[dict]) -> tuple[np.ndarray, list[np.ndarray]]:
    umax = max(point["config"].cmax + point["config"].half_width for point in points)
    u = np.linspace(-umax, umax, 8001)
    shapes = []
    for point in points:
        cfg = point["config"]
        Q = point["Q"]
        shapes.append(np.column_stack([
            _physical_shape(cfg.centers, cfg.half_width, Q[:, j], u)
            for j in range(Q.shape[1])
        ]))
    return u, shapes


def full_edges(points: list[dict]) -> list[dict]:
    u, shapes = _point_shapes(points)
    rows = []
    for i in range(len(points) - 1):
        left = points[i]
        right = points[i + 1]
        left_shapes = shapes[i]
        right_shapes = shapes[i + 1]
        T = np.array([[
            float(_TRAP(right_shapes[:, a] * left_shapes[:, b], x=u))
            for b in range(left_shapes.shape[1])
        ] for a in range(right_shapes.shape[1])])
        svals = np.linalg.svd(T, compute_uv=False)
        clipped = np.clip(svals, 0.0, 1.0)
        dL = right["result"]["gmax"] - left["result"]["gmax"]
        raw_defect = _sym(left["metric"] - T.T @ right["metric"] @ T)
        l2_capacity = _sym(np.eye(T.shape[1]) - T.T @ T)
        defect_lambda = _minimum_background_for_psd(raw_defect, l2_capacity)
        spd_lambda = _metric_shift_for_logdet(left["metric"], right["metric"])
        lam = max(defect_lambda, spd_lambda) if np.isfinite(defect_lambda) else float("inf")
        transgression = _metric_transgression(left["metric"], right["metric"], T, lam)
        rows.append({
            "kind": left["kind"],
            "left_gmax": left["result"]["gmax"],
            "right_gmax": right["result"]["gmax"],
            "dL": dL,
            "left_repair": left["repair_label"],
            "right_repair": right["repair_label"],
            "left_min": float(left["metric_eigs"][0]),
            "right_min": float(right["metric_eigs"][0]),
            "raw_defect_min": float(np.linalg.eigvalsh(raw_defect)[0]),
            "capacity_min": float(np.linalg.eigvalsh(l2_capacity)[0]),
            "defect_lambda": defect_lambda,
            "spd_lambda": spd_lambda,
            "lambda": lam,
            "sval_min": float(svals[-1]),
            "sval_max": float(svals[0]),
            "angle_density": float(np.linalg.norm(np.arccos(clipped)) / dL),
            "transgression": transgression,
        })
    return rows


def support_points(kind: str, ncenters: int = 17, half_width: float = 0.10) -> list[dict]:
    gmaxs = (1.60, 1.72, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24)
    return [
        full_point(config_for_gmax(gmax, ncenters, half_width), kind)
        for gmax in gmaxs
    ]


def refinement_cone(kind: str) -> list[dict]:
    rows = []
    for gmax in (1.88, 2.10, 2.30, 2.76, 3.00):
        for ncenters, half_width in ((13, 0.14), (17, 0.10), (21, 0.08), (25, 0.06)):
            point = full_point(config_for_gmax(gmax, ncenters, half_width), kind)
            rows.append({
                "kind": kind,
                "gmax": gmax,
                "basis": f"n{ncenters}/hw{half_width:.2f}",
                "dimension": point["dimension"],
                "repair": point["repair_label"],
                "min_eig": float(point["metric_eigs"][0]),
                "max_eig": float(point["metric_eigs"][-1]),
                "condition_scale": float(point["metric_eigs"][-1] / point["metric_eigs"][0])
                if point["metric_eigs"][0] > 0 else float("nan"),
            })
    return rows


def _print_points(points: list[dict]) -> None:
    print(f"\n[{points[0]['kind']}] full pole-killed finite fibers")
    print("      gmax   dim  repair   J eig range              condition")
    for point in points:
        min_eig = float(point["metric_eigs"][0])
        max_eig = float(point["metric_eigs"][-1])
        cond = max_eig / min_eig if min_eig > 0 else float("nan")
        cond_text = "indef" if not np.isfinite(cond) else f"{cond:.2e}"
        print(f"      {point['result']['gmax']:.2f}   "
              f"{point['dimension']:2d}   "
              f"{point['repair_label']:<5}   "
              f"[{min_eig:+.2e},{max_eig:+.2e}]   "
              f"{cond_text}")


def _print_edges(rows: list[dict], label: str) -> None:
    print(f"\n[{label}] full-fiber L2 connection and metric-pair defect")
    print("      edge        repairs      svals[min,max]  raw min    lambdas(def,spd)  Tau       conn")
    for row in rows:
        tr = row["transgression"]
        tau = tr["tau"]
        conn = tr["connection_volume"]
        tau_text = "nan" if not np.isfinite(tau) else f"{tau:+.3f}"
        conn_text = "nan" if not np.isfinite(conn) else f"{conn:+.3f}"
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['left_repair']}->{row['right_repair']:<5}  "
              f"[{row['sval_min']:.2e},{row['sval_max']:.3f}]  "
              f"{row['raw_defect_min']:+.2e}   "
              f"({row['defect_lambda']:.3g},{row['spd_lambda']:.3g})   "
              f"{tau_text:>8}  "
              f"{conn_text:>8}")
    print("      reading: full-rank determinant volume is very sensitive to small")
    print("      singular values; positive-cone membership is the durable diagnostic.")


def _print_refinement(rows: list[dict], label: str) -> None:
    print(f"\n[{label}] full-fiber positive cone under basis refinement")
    print("      gmax   basis       dim  repair   J eig range")
    for row in rows:
        print(f"      {row['gmax']:.2f}   "
              f"{row['basis']:<10}  "
              f"{row['dimension']:2d}   "
              f"{row['repair']:<5}   "
              f"[{row['min_eig']:+.2e},{row['max_eig']:+.2e}]")
    print("      reading: this is the finite version of the actual positivity claim,")
    print("      without selecting an obstruction subspace.")


def summary() -> dict:
    print("=" * 78)
    print("Full finite-rank Prime-Toeplitz metric-flow witness")
    print("=" * 78)

    zeta_points = support_points("zeta")
    dh_points = support_points("DH")
    _print_points(zeta_points)
    _print_points(dh_points)

    zeta_edges = full_edges(zeta_points)
    dh_edges = full_edges(dh_points)
    _print_edges(zeta_edges, "zeta")
    _print_edges(dh_edges, "DH")

    zeta_refinement = refinement_cone("zeta")
    dh_refinement = refinement_cone("DH")
    _print_refinement(zeta_refinement, "zeta")
    _print_refinement(dh_refinement, "DH")

    print("\nInterpretation:")
    print("  * The full finite pole-killed margin keeps zeta in the positive cone over")
    print("    the tested support/refinement grid.")
    print("  * DH leaves the positive cone robustly at the same onset seen by the")
    print("    local and spectral-bundle witnesses.")
    print("  * Full-rank transgression is dominated by projection-volume artifacts;")
    print("    the proof target should be Loewner/positive-cone preservation, with")
    print("    transgression used only after choosing a controlled finite channel.")

    return {
        "zeta_points": zeta_points,
        "DH_points": dh_points,
        "zeta_edges": zeta_edges,
        "DH_edges": dh_edges,
        "zeta_refinement": zeta_refinement,
        "DH_refinement": dh_refinement,
    }


if __name__ == "__main__":
    summary()
