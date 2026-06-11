"""Stress tests for the Prime-Toeplitz transgression diagnostic.

This keeps the main flow witness readable and focuses on the question that
matters after introducing the metric-pair transgression:

    Does the fitted background lambda and log-det anomaly Tau stabilize
    under longer support sweeps and basis refinement?

Run:
    python3 -m scripts.numerics.witness.prime_transgression_stress
"""
from __future__ import annotations

from .prime_carleson_flow import (
    FlowConfig,
    _dominant_repair,
    _gram_orthonormalize,
    _metric_transgression,
    _minimum_background_for_psd,
    _physical_gram,
    _physical_shape,
    flow_rows,
    j_metric_fit,
)

import numpy as np

_TRAP = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


def _repair_label(result: dict) -> str:
    repair = _dominant_repair(result)
    if repair is None:
        return "none"
    return f"n{repair['n']}"


def longer_support_results() -> list[dict]:
    configs = [FlowConfig(ncenters=17, half_width=0.10, cmax=cmax)
               for cmax in (0.70, 0.76, 0.84, 0.95, 1.05, 1.16, 1.28, 1.40, 1.52)]
    return [flow_rows(cfg, "zeta") for cfg in configs]


def longer_support_sweep(results: list[dict]) -> list[dict]:
    return j_metric_fit(results)


def basis_refinement_stability() -> list[dict]:
    edges = [(1.88, 2.10), (2.10, 2.30)]
    refinements = [(13, 0.14), (17, 0.10), (21, 0.08), (25, 0.06)]
    rows = []
    for left_gmax, right_gmax in edges:
        for ncenters, half_width in refinements:
            configs = [
                FlowConfig(ncenters=ncenters, half_width=half_width,
                           cmax=left_gmax / 2.0 - half_width),
                FlowConfig(ncenters=ncenters, half_width=half_width,
                           cmax=right_gmax / 2.0 - half_width),
            ]
            results = [flow_rows(cfg, "zeta") for cfg in configs]
            fit = j_metric_fit(results)[0]
            transgression = fit["fitted_transgression"]
            rows.append({
                "edge": (left_gmax, right_gmax),
                "ncenters": ncenters,
                "half_width": half_width,
                "left_repair": _repair_label(results[0]),
                "right_repair": _repair_label(results[1]),
                "left_final": results[0]["final_min"],
                "right_final": results[1]["final_min"],
                "lambda": fit["min_l2_background"],
                "tau": transgression["tau"],
                "raw_min": float(fit["raw_defect_eigs"][0]),
            })
    return rows


def fiber_rank_spike_test(results: list[dict]) -> list[dict]:
    """Check whether widening the active fiber removes the late lambda spike."""
    umax = max(result["config"].cmax + result["config"].half_width for result in results)
    u = np.linspace(-umax, umax, 6001)
    rows = []

    for rank_mode in (2, 3, 4):
        fibers = []
        for result in results:
            repair = _dominant_repair(result)
            cfg = result["config"]
            cols = [repair["_before_full"], repair["_atom_bad_full"]]
            if rank_mode >= 3:
                cols.append(repair["_after_full"])
            if rank_mode >= 4:
                cols.append(result["_final_full"])
            B = np.column_stack(cols)
            Q = _gram_orthonormalize(B, _physical_gram(cfg))
            shapes = np.column_stack([
                _physical_shape(cfg.centers, cfg.half_width, Q[:, j], u)
                for j in range(Q.shape[1])
            ])
            metric = 0.5 * (Q.T @ repair["_after_form_full"] @ Q
                            + (Q.T @ repair["_after_form_full"] @ Q).T)
            fibers.append((result, repair, shapes, metric))

        for i in range(len(fibers) - 1):
            left, right = fibers[i], fibers[i + 1]
            if left[0]["gmax"] < 2.30:
                continue
            T = np.array([[
                float(_TRAP(right[2][:, a] * left[2][:, b], x=u))
                for b in range(left[2].shape[1])
            ] for a in range(right[2].shape[1])])
            defect = left[3] - T.T @ right[3] @ T
            capacity = np.eye(T.shape[1]) - T.T @ T
            lam = _minimum_background_for_psd(defect, capacity)
            tau = _metric_transgression(left[3], right[3], T, lam)["tau"]
            rows.append({
                "rank_mode": rank_mode,
                "left_gmax": left[0]["gmax"],
                "right_gmax": right[0]["gmax"],
                "left_repair": left[1]["n"],
                "right_repair": right[1]["n"],
                "dimension": T.shape[1],
                "raw_min": float(np.linalg.eigvalsh(0.5 * (defect + defect.T))[0]),
                "lambda": lam,
                "tau": tau,
            })
    return rows


def split_continuous_and_singular(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        transgression = row["fitted_transgression"]
        dL = row["right_gmax"] - row["left_gmax"]
        same_label = row["left_n"] == row["right_n"]
        out.append({
            "kind": "continuous" if same_label else "singular",
            "left_gmax": row["left_gmax"],
            "right_gmax": row["right_gmax"],
            "left_n": row["left_n"],
            "right_n": row["right_n"],
            "lambda": row["min_l2_background"],
            "tau": transgression["tau"],
            "metric_delta": transgression["metric_delta"],
            "connection_volume": transgression["connection_volume"],
            "tau_density": transgression["tau"] / dL if same_label else None,
            "metric_density": transgression["metric_delta"] / dL if same_label else None,
            "connection_density": transgression["connection_volume"] / dL if same_label else None,
        })
    return out


def continuous_drift_geometry(results: list[dict], fit_rows: list[dict]) -> list[dict]:
    """Principal-angle / second-fundamental proxies for same-label drift edges."""
    umax = max(result["config"].cmax + result["config"].half_width for result in results)
    u = np.linspace(-umax, umax, 6001)

    fibers = []
    for result in results:
        repair = _dominant_repair(result)
        cfg = result["config"]
        B = np.column_stack([repair["_before_full"], repair["_atom_bad_full"]])
        Q = _gram_orthonormalize(B, _physical_gram(cfg))
        shapes = np.column_stack([
            _physical_shape(cfg.centers, cfg.half_width, Q[:, j], u)
            for j in range(Q.shape[1])
        ])
        fibers.append((result, repair, shapes))

    out = []
    for i, fit in enumerate(fit_rows):
        left, right = fibers[i], fibers[i + 1]
        if left[1]["n"] != right[1]["n"]:
            continue
        T = np.array([[
            float(_TRAP(right[2][:, a] * left[2][:, b], x=u))
            for b in range(left[2].shape[1])
        ] for a in range(right[2].shape[1])])
        svals = np.linalg.svd(T, compute_uv=False)
        clipped = np.clip(svals, 0.0, 1.0)
        angles = np.arccos(clipped)
        dL = right[0]["gmax"] - left[0]["gmax"]
        transgression = fit["fitted_transgression"]
        out.append({
            "left_gmax": left[0]["gmax"],
            "right_gmax": right[0]["gmax"],
            "label": left[1]["n"],
            "lambda": fit["min_l2_background"],
            "svals": svals,
            "max_angle_density": float(np.max(angles) / dL),
            "angle_frobenius_density": float(np.linalg.norm(angles) / dL),
            "sin_frobenius_density": float(np.sqrt(np.sum(1.0 - clipped ** 2)) / dL),
            "connection_density": transgression["connection_volume"] / dL,
            "metric_density": transgression["metric_delta"] / dL,
            "tau_density": transgression["tau"] / dL,
        })
        out[-1]["connection_over_sin2"] = (
            out[-1]["connection_density"] / (out[-1]["sin_frobenius_density"] ** 2)
            if out[-1]["sin_frobenius_density"] > 0 else float("nan")
        )
    return out


def summary() -> dict:
    print("=" * 78)
    print("Prime-Toeplitz transgression stress tests")
    print("=" * 78)

    print("\n[1] Longer support sweep, ncenters=17, hw=0.10")
    print("      edge        repair      lambda     Tau(lambda)   raw defect min")
    long_results = longer_support_results()
    long_rows = longer_support_sweep(long_results)
    for row in long_rows:
        tr = row["fitted_transgression"]
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"n{row['left_n']}->n{row['right_n']}   "
              f"{row['min_l2_background']:.3g}      "
              f"{tr['tau']:+.3f}        "
              f"{row['raw_defect_eigs'][0]:+.2e}")
    print("      reading: Tau stays positive; lambda is usually modest but spikes at")
    print("      2.52->2.76, so boundedness needs a longer/refined check.")

    print("\n[2] Continuous drift vs singular handoffs")
    print("      same-label edges are reported as densities per dL; label changes as jumps")
    print("      edge        mode         repair      lambda   Tau        metric      connection")
    split_rows = split_continuous_and_singular(long_rows)
    for row in split_rows:
        if row["kind"] == "continuous":
            print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
                  f"drift       n{row['left_n']}->n{row['right_n']}   "
                  f"{row['lambda']:.3g}   "
                  f"{row['tau_density']:+.3f}/dL   "
                  f"{row['metric_density']:+.3f}/dL   "
                  f"{row['connection_density']:+.3f}/dL")
        else:
            print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
                  f"jump        n{row['left_n']}->n{row['right_n']}   "
                  f"{row['lambda']:.3g}   "
                  f"{row['tau']:+.3f}     "
                  f"{row['metric_delta']:+.3f}     "
                  f"{row['connection_volume']:+.3f}")
    print("      reading: the lambda spike lies on a same-label drift edge, so it")
    print("      should be modeled by curvature/metric variation, not a point jump.")

    print("\n[3] Same-label active-subbundle drift geometry")
    print("      angles are principal angles between adjacent L2-orthonormal active fibers")
    print("      edge        label  svals              angle||/dL  sin||/dL  conn/dL  conn/sin2  lambda")
    drift_rows = continuous_drift_geometry(long_results, long_rows)
    for row in drift_rows:
        svals = ",".join(f"{s:.3f}" for s in row["svals"])
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"n{row['label']:<2d}   [{svals}]   "
              f"{row['angle_frobenius_density']:.3f}      "
              f"{row['sin_frobenius_density']:.3f}    "
              f"{row['connection_density']:.3f}   "
              f"{row['connection_over_sin2']:.3f}     "
              f"{row['lambda']:.3g}")
    print("      reading: same-label drift is not flat; high connection density marks")
    print("      continuous curvature of the active subbundle, not a prime jump.")

    print("\n[4] Fiber rank test near the late lambda spike")
    print("      rank mode: 2=[bad,atom], 3=+outgoing, 4=+final")
    print("      edge        repair      rank  lambda     Tau(lambda)   raw defect min")
    rank_rows = fiber_rank_spike_test(long_results)
    for row in rank_rows:
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"n{row['left_repair']}->n{row['right_repair']}   "
              f"{row['dimension']}     "
              f"{row['lambda']:.3g}      "
              f"{row['tau']:+.3f}        "
              f"{row['raw_min']:+.2e}")
    print("      reading: simply widening the local fiber does not remove the spike;")
    print("      the missing term is likely in the metric/capacity model, not just rank.")

    print("\n[5] Basis refinement at two handoff edges")
    print("      edge        basis       repairs       lambda     Tau(lambda)   raw defect min")
    refine_rows = basis_refinement_stability()
    for row in refine_rows:
        left, right = row["edge"]
        print(f"      {left:.2f}->{right:.2f}  "
              f"n={row['ncenters']:2d},hw={row['half_width']:.2f}  "
              f"{row['left_repair']}->{row['right_repair']:<3}   "
              f"{row['lambda']:.3g}      "
              f"{row['tau']:+.3f}        "
              f"{row['raw_min']:+.2e}")
    print("      reading: the n5->n7 handoff is stable under refinement; the n3->n5")
    print("      edge is less stable because finer bases already make n5 active on both sides.")

    return {
        "longer_support_sweep": long_rows,
        "continuous_singular_split": split_rows,
        "continuous_drift_geometry": drift_rows,
        "fiber_rank_spike_test": rank_rows,
        "basis_refinement_stability": refine_rows,
    }


if __name__ == "__main__":
    summary()
