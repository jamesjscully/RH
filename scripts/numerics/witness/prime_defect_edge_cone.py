"""Finite edge-layer cone diagnostics for the active debt profile.

The current proof target reduces the late repair cell to a one-sided
convolution near the support edge:

    K(w) = int_0^w q(r) q(w-r) dr,
    q(r) = z(a-r),  w = 2a-U.

This script measures the geometric hypotheses suggested by
``research/proof/07-active-debt-geometric-lemma.md``:

  * sign coherence of q on the repair depth interval;
  * edge-layer mass and convolution centroid;
  * the normalized repair ratio beta = Avg_cell(K) / K(w_atom);
  * stability under small multiplicative perturbations of the active edge
    coefficients.

Run:
    python3 -m scripts.numerics.witness.prime_defect_edge_cone
    python3 -m scripts.numerics.witness.prime_defect_edge_cone --refinements
"""
from __future__ import annotations

import argparse
import math

import numpy as np

from .prime_carleson_flow import _raised_cosine_even
from .prime_defect_active_atom_shift import (
    REFINEMENTS,
    active_state,
    shifted_row,
)


PERTURB_AMPS = (0.01, 0.05, 0.10, 0.20)


def _trap(y: np.ndarray, x: np.ndarray) -> float:
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trap(y, x=x))


def _edge_indices(state: dict, wmax: float) -> np.ndarray:
    ambient = state["ambient"]
    edge = float(ambient.centers.max() + ambient.half_width)
    return np.flatnonzero(ambient.centers + ambient.half_width >= edge - wmax - 1e-12)


def _profile_from_coeffs(state: dict, coeffs: np.ndarray,
                         ngrid: int = 4097) -> dict:
    ambient = state["ambient"]
    lo, hi = state["cell"]
    edge = float(ambient.centers.max() + ambient.half_width)
    w_min = max(0.0, 2.0 * edge - hi)
    w_max = max(0.0, 2.0 * edge - lo)
    w_atom = max(0.0, 2.0 * edge - state["logn"])
    r = np.linspace(0.0, w_max, ngrid)
    q = coeffs @ _raised_cosine_even(ambient.centers, ambient.half_width, edge - r)
    dr = float(r[1] - r[0]) if len(r) > 1 else 0.0

    conv = np.convolve(q, q) * dr
    conv_w = np.linspace(0.0, 2.0 * w_max, len(conv))
    w_grid = np.linspace(w_min, w_max, ngrid)
    K = np.interp(w_grid, conv_w, conv)
    K_atom = float(np.interp(w_atom, conv_w, conv))
    weight = 2.0 * np.exp(0.5 * (2.0 * edge - w_grid))
    weight_mass = _trap(weight, w_grid)
    weighted_K = weight * K
    total_current = _trap(weighted_K, w_grid)
    beta = total_current / (weight_mass * K_atom) if abs(weight_mass * K_atom) > 1e-14 else float("nan")
    centroid_w = _trap(w_grid * weighted_K, w_grid) / total_current if abs(total_current) > 1e-14 else float("nan")
    width_rel_centroid = (
        (centroid_w - w_min) / (w_max - w_min)
        if w_max > w_min and np.isfinite(centroid_w) else float("nan")
    )
    atom_width_rel = (w_atom - w_min) / (w_max - w_min) if w_max > w_min else float("nan")
    beyond = w_grid >= w_atom
    below = w_grid <= w_atom
    mass_beyond = (
        _trap(weighted_K[beyond], w_grid[beyond]) / total_current
        if abs(total_current) > 1e-14 and np.count_nonzero(beyond) > 1 else float("nan")
    )
    mass_below = (
        _trap(weighted_K[below], w_grid[below]) / total_current
        if abs(total_current) > 1e-14 and np.count_nonzero(below) > 1 else float("nan")
    )

    q_l2 = _trap(q * q, r)
    q_beyond = r >= w_atom
    q_l2_beyond = (
        _trap((q * q)[q_beyond], r[q_beyond]) / q_l2
        if q_l2 > 1e-14 and np.count_nonzero(q_beyond) > 1 else float("nan")
    )
    active = np.abs(q) > 1e-8 * max(1.0, float(np.max(np.abs(q))))
    signs = np.sign(q[active])
    sign_changes = int(np.count_nonzero(signs[1:] * signs[:-1] < 0.0)) if signs.size else 0
    return {
        "edge": edge,
        "w_min": w_min,
        "w_max": w_max,
        "w_atom": w_atom,
        "r": r,
        "q": q,
        "w_grid": w_grid,
        "K": K,
        "K_atom": K_atom,
        "weight_mass": weight_mass,
        "total_current": total_current,
        "beta": beta,
        "centroid_w": centroid_w,
        "centroid_width_rel": width_rel_centroid,
        "centroid_u_rel": 1.0 - width_rel_centroid if np.isfinite(width_rel_centroid) else float("nan"),
        "atom_width_rel": atom_width_rel,
        "atom_u_rel": 1.0 - atom_width_rel if np.isfinite(atom_width_rel) else float("nan"),
        "K_mass_beyond_atom": mass_beyond,
        "K_mass_below_atom": mass_below,
        "q_l2_beyond_atom": q_l2_beyond,
        "q_min": float(np.min(q)),
        "q_max": float(np.max(q)),
        "q_sign_changes": sign_changes,
    }


def _required_beta(state: dict) -> float:
    exact = shifted_row(state, U=state["logn"])
    smooth_mass = 4.0 * (
        math.exp(0.5 * state["cell"][1]) - math.exp(0.5 * state["cell"][0])
    )
    return (
        state["atom_weight"] / smooth_mass
        + exact["required"] / (smooth_mass * exact["k"])
    )


def _beta_sensitivities(state: dict, coeffs: np.ndarray, profile: dict,
                        eps: float = 1e-4) -> list[dict]:
    edge_idx = _edge_indices(state, profile["w_max"])
    rows = []
    beta0 = profile["beta"]
    for idx in edge_idx:
        plus = coeffs.copy()
        minus = coeffs.copy()
        plus[idx] *= 1.0 + eps
        minus[idx] *= 1.0 - eps
        beta_plus = _profile_from_coeffs(state, plus, ngrid=2049)["beta"]
        beta_minus = _profile_from_coeffs(state, minus, ngrid=2049)["beta"]
        derivative = (beta_plus - beta_minus) / (2.0 * eps)
        ambient = state["ambient"]
        rows.append({
            "index": int(idx),
            "center": float(ambient.centers[idx]),
            "gap": float(profile["edge"] - ambient.centers[idx]),
            "coeff": float(coeffs[idx]),
            "d_beta": float(derivative),
            "d_log_beta": float(derivative / beta0) if abs(beta0) > 1e-14 else float("nan"),
        })
    return rows


def edge_cone_report(ncenters: int = 25, half_width: float = 0.06,
                     perturb_samples: int = 300,
                     seed: int = 20260609) -> dict:
    state = active_state(ncenters, half_width)
    coeffs = state["B"] @ state["f"]
    profile = _profile_from_coeffs(state, coeffs)
    required_beta = _required_beta(state)
    edge_idx = _edge_indices(state, profile["w_max"])

    rng = np.random.default_rng(seed + 1000 * ncenters + int(round(1000.0 * half_width)))
    sensitivity_rows = _beta_sensitivities(state, coeffs, profile)
    perturb_rows = []
    for amp in PERTURB_AMPS:
        betas = []
        sign_changes = []
        failures = 0
        for _ in range(perturb_samples):
            perturbed = coeffs.copy()
            multipliers = 1.0 + rng.uniform(-amp, amp, size=len(edge_idx))
            perturbed[edge_idx] *= multipliers
            prow = _profile_from_coeffs(state, perturbed, ngrid=2049)
            betas.append(prow["beta"])
            sign_changes.append(prow["q_sign_changes"])
            if not np.isfinite(prow["beta"]) or prow["beta"] < required_beta:
                failures += 1
        betas_arr = np.array(betas, dtype=float)
        perturb_rows.append({
            "amp": amp,
            "min_beta": float(np.nanmin(betas_arr)),
            "p05_beta": float(np.nanpercentile(betas_arr, 5.0)),
            "median_beta": float(np.nanmedian(betas_arr)),
            "failure_count": int(failures),
            "samples": perturb_samples,
            "max_sign_changes": int(max(sign_changes, default=0)),
        })

    coeff_rows = []
    ambient = state["ambient"]
    for idx in edge_idx:
        coeff_rows.append({
            "index": int(idx),
            "center": float(ambient.centers[idx]),
            "gap": float(profile["edge"] - ambient.centers[idx]),
            "coeff": float(coeffs[idx]),
            "rel_coeff": float(coeffs[idx] / max(1e-14, np.max(np.abs(coeffs[edge_idx])))),
        })

    return {
        "state": state,
        "profile": profile,
        "required_beta": required_beta,
        "edge_indices": edge_idx,
        "coefficients": coeff_rows,
        "sensitivities": sensitivity_rows,
        "perturbations": perturb_rows,
    }


def _print_report(report: dict) -> None:
    state = report["state"]
    profile = report["profile"]
    print("=" * 78)
    print("Finite edge-layer cone diagnostic")
    print("=" * 78)
    print(f"basis n={state['ncenters']} hw={state['half_width']:.3f}, "
          f"cell {state['repair_n']}=[{state['cell'][0]:.6f},{state['cell'][1]:.6f}], "
          f"log n={state['logn']:.6f}")
    print(f"width cell=[{profile['w_min']:.6f},{profile['w_max']:.6f}], "
          f"w_atom={profile['w_atom']:.6f}, "
          f"atom rel(U)={profile['atom_u_rel']:.3f}")
    print(f"beta observed={profile['beta']:.3f}, "
          f"required={report['required_beta']:.3f}, "
          f"margin={profile['beta'] - report['required_beta']:+.3f}")
    print(f"K centroid rel(U)={profile['centroid_u_rel']:.3f}, "
          f"K mass left-of-atom(U)={profile['K_mass_beyond_atom']:.3f}, "
          f"q L2 beyond atom-width={profile['q_l2_beyond_atom']:.3f}")
    print(f"q range=[{profile['q_min']:+.3e},{profile['q_max']:+.3e}], "
          f"q sign changes={profile['q_sign_changes']}, "
          f"K(log n)={profile['K_atom']:+.3e}")
    print("\n      active edge coefficients:")
    for row in report["coefficients"]:
        print(f"        i={row['index']:<2d} "
              f"center={row['center']:.6f} "
              f"gap={row['gap']:.6f} "
              f"coeff={row['coeff']:+.6e} "
              f"rel={row['rel_coeff']:+.3f}")
    print("\n      beta sensitivity to coefficient multipliers:")
    for row in report["sensitivities"]:
        print(f"        i={row['index']:<2d} "
              f"gap={row['gap']:.6f} "
              f"dlogbeta/dmult={row['d_log_beta']:+.3f}")
    print("\n      multiplicative edge-coefficient perturbations:")
    print("        amp    min beta  p05 beta  median   fails  max sign changes")
    for row in report["perturbations"]:
        print(f"        {row['amp']:.2f}   "
              f"{row['min_beta']:.3f}    "
              f"{row['p05_beta']:.3f}    "
              f"{row['median_beta']:.3f}   "
              f"{row['failure_count']:>3d}/{row['samples']:<3d}  "
              f"{row['max_sign_changes']}")


def refinement_table() -> list[dict]:
    rows = []
    print("\n[edge-cone refinement table]")
    print("      basis       beta/req  centU  massLeft qL2Beyond sign  minBeta10 fail10")
    for ncenters, half_width in REFINEMENTS:
        report = edge_cone_report(ncenters, half_width, perturb_samples=120)
        profile = report["profile"]
        amp10 = next(row for row in report["perturbations"] if abs(row["amp"] - 0.10) < 1e-12)
        terminal_sens = report["sensitivities"][-1]["d_log_beta"] if report["sensitivities"] else float("nan")
        max_sens = max((row["d_log_beta"] for row in report["sensitivities"]), default=float("nan"))
        row = {
            "ncenters": ncenters,
            "half_width": half_width,
            "beta": profile["beta"],
            "required": report["required_beta"],
            "centroid_u": profile["centroid_u_rel"],
            "mass_left": profile["K_mass_beyond_atom"],
            "q_l2_beyond": profile["q_l2_beyond_atom"],
            "sign_changes": profile["q_sign_changes"],
            "min_beta10": amp10["min_beta"],
            "fail10": amp10["failure_count"],
            "samples10": amp10["samples"],
            "terminal_sens": terminal_sens,
            "max_sens": max_sens,
        }
        rows.append(row)
        print(f"      n{ncenters:<2d}/h{half_width:.3f} "
              f"{row['beta']:.3f}/{row['required']:.3f} "
              f"{row['centroid_u']:.3f}  "
              f"{row['mass_left']:.3f}   "
              f"{row['q_l2_beyond']:.3f}    "
              f"{row['sign_changes']:<4d} "
              f"{row['min_beta10']:.3f}   "
              f"{row['fail10']}/{row['samples10']} "
              f"termGrad={row['terminal_sens']:+.2f} "
              f"maxGrad={row['max_sens']:+.2f}")
    return rows


def summary(with_refinements: bool = False) -> dict:
    report = edge_cone_report()
    _print_report(report)
    if with_refinements:
        report["refinements"] = refinement_table()
    print("\nInterpretation:")
    print("  * The default active debt profile is sign-coherent on the repair edge layer.")
    print("  * The repair ratio is controlled by convolution mass lying to the")
    print("    left of the atom in U, equivalently at larger edge widths.")
    print("  * Small edge-coefficient perturbations test whether the proposed cone")
    print("    inequality is broad enough to become a lemma; failures mean the cone")
    print("    must include active-state structure, not only coefficient signs.")
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--refinements", action="store_true")
    args = parser.parse_args()
    summary(with_refinements=args.refinements)
