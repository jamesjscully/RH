"""Active-debt arithmetic current for the Riccati storage target.

The Riccati storage diagnostic found that the late edge 3.00->3.24 starts with
a negative Schur complement for the smooth-new base and is repaired by the
exact Euler residual cell at n=23.

This script extracts the active debt vector y in the shell Schur complement,
forms the old response x=A^{-1}Cy, and studies the stress

    f = x - y,
    k(U) = B_U(f,f).

For a residual cell E_n = P_smooth_cell(n) - P_atom(n), the linear Schur
increment on the debt direction is

    Q_n(y) = E_n(f,f)
           = int_cell 2e^{U/2} k(U)dU
             - 2 Lambda(n)n^{-1/2} k(log n).

Positive Q_n repairs the negative Schur debt before the Riccati square and
cross-complement leakage are paid.  This is the arithmetic quantity the proof
has to control.

Run:
    python3 -m scripts.numerics.witness.prime_defect_active_debt_current
"""
from __future__ import annotations

import math
import argparse

import numpy as np

from .prime_carleson_flow import _raised_cosine_even, _sym, _toeplitz_atom
from .prime_defect_riccati_storage import (
    _blocks,
    _min_pair,
    extension_base_margin,
    interval_residual_cells,
    riccati_cell,
)
from .prime_defect_residual_control import edge_basis, smooth_cell_operator
from .prime_defect_scale_phase import ambient_and_points
from .prime_nested_cone import build_ambient, margin_at, point
from .semilocal_2 import _grids, _phihat


LATE_EDGE = (3.00, 3.24)


def _cell_bounds_for_atoms(ambient, left: float, right: float) -> dict[int, tuple[float, float]]:
    active = [
        (n, math.log(n))
        for n in sorted(ambient.atoms["zeta"])
        if left <= math.log(n) < right
    ]
    logs = [logn for _, logn in active]
    bounds = {}
    for idx, (n, _) in enumerate(active):
        lo = left if idx == 0 else 0.5 * (logs[idx - 1] + logs[idx])
        hi = right if idx == len(active) - 1 else 0.5 * (logs[idx] + logs[idx + 1])
        bounds[n] = (lo, hi)
    return bounds


def _quadratic(M: np.ndarray, v: np.ndarray) -> float:
    return float(v.T @ _sym(M) @ v)


def _kernel_value(ambient, B: np.ndarray, f: np.ndarray, U: float) -> float:
    atom = _toeplitz_atom(ambient.centers, ambient.half_width, U, 1.0)
    return _quadratic(_sym(B.T @ atom @ B), f)


def _kernel_shape(ambient, B: np.ndarray, f: np.ndarray, lo: float, hi: float,
                  logn: float, samples: int = 401) -> dict:
    """Dense shape diagnostics for k(U)=B_U(f,f) on one cell."""
    grid = _grids()
    ts, dt = grid["ts"], grid["dt"]
    coeffs = B @ f
    ph = np.array([_phihat(ts, c, ambient.half_width) for c in ambient.centers])
    zhat = coeffs @ ph
    weights = (zhat * zhat) * dt / (2.0 * np.pi)
    Us = np.linspace(lo, hi, samples)
    vals = np.cos(np.outer(Us, ts)) @ weights
    dvals = np.diff(vals)
    tol = 1e-8 * max(1.0, float(np.max(np.abs(vals))))
    smooth_weight = 2.0 * np.exp(0.5 * Us)
    density = smooth_weight * vals
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    smooth_approx = float(trap(density, x=Us))
    if abs(smooth_approx) > 1e-14:
        centroid = float(trap(Us * density, x=Us) / smooth_approx)
    else:
        centroid = float("nan")
    return {
        "sample_min": float(vals.min()),
        "sample_max": float(vals.max()),
        "monotone_nonincreasing": bool(np.all(dvals <= tol)),
        "max_up_step": float(np.max(dvals)),
        "max_down_step": float(np.min(dvals)),
        "smooth_centroid": centroid,
        "smooth_centroid_rel": (centroid - lo) / (hi - lo) if np.isfinite(centroid) else float("nan"),
        "atom_rel": (logn - lo) / (hi - lo),
        "smooth_approx": smooth_approx,
        "left_half_fraction": (
            float(trap(density[Us <= 0.5 * (lo + hi)], x=Us[Us <= 0.5 * (lo + hi)]) / smooth_approx)
            if abs(smooth_approx) > 1e-14 and np.any(Us <= 0.5 * (lo + hi)) else float("nan")
        ),
    }


def _interp_values(grid: np.ndarray, values: np.ndarray, points: np.ndarray) -> np.ndarray:
    return np.interp(points, grid, values, left=0.0, right=0.0)


def _physical_overlap_shape(ambient, B: np.ndarray, f: np.ndarray,
                            Us: tuple[float, ...], ngrid: int = 16001) -> dict:
    """Physical autocorrelation geometry for k(U)=int z(v)z(v-U)dv."""
    coeffs = B @ f
    umax = float(ambient.centers.max() + ambient.half_width)
    grid = np.linspace(-umax, umax, ngrid)
    basis = _raised_cosine_even(ambient.centers, ambient.half_width, grid)
    z = coeffs @ basis
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    total_l2 = float(trap(z * z, x=grid))
    boundary = 0.20 * umax
    boundary_mask = np.abs(grid) >= umax - boundary
    boundary_l2_frac = (
        float(trap(np.where(boundary_mask, z * z, 0.0), x=grid) / total_l2)
        if total_l2 > 1e-14 else float("nan")
    )
    rows = []
    for U in Us:
        shifted = _interp_values(grid, z, grid - U)
        integrand = z * shifted
        abs_integrand = np.abs(integrand)
        mass = float(trap(integrand, x=grid))
        abs_mass = float(trap(abs_integrand, x=grid))
        support = abs_integrand > 1e-8 * max(1.0, float(abs_integrand.max()))
        if np.any(support):
            v_min = float(grid[support][0])
            v_max = float(grid[support][-1])
        else:
            v_min = v_max = float("nan")
        if abs_mass > 1e-14:
            centroid = float(trap(grid * abs_integrand, x=grid) / abs_mass)
            width = float(math.sqrt(max(0.0, trap((grid - centroid) ** 2 * abs_integrand, x=grid) / abs_mass)))
        else:
            centroid = width = float("nan")
        rows.append({
            "U": U,
            "mass": mass,
            "abs_mass": abs_mass,
            "overlap_v_min": v_min,
            "overlap_v_max": v_max,
            "overlap_width": v_max - v_min if np.isfinite(v_min) and np.isfinite(v_max) else float("nan"),
            "abs_centroid_v": centroid,
            "abs_width_v": width,
        })
    exponents = []
    if rows:
        base = rows[0]
        for row in rows[1:]:
            if (
                base["overlap_width"] > 1e-14
                and row["overlap_width"] > 1e-14
                and abs(base["mass"]) > 1e-14
                and abs(row["mass"]) > 1e-14
                and abs(base["mass"] / row["mass"]) > 0.0
            ):
                denom = math.log(base["overlap_width"] / row["overlap_width"])
                exp = math.log(abs(base["mass"] / row["mass"])) / denom if abs(denom) > 1e-14 else float("nan")
            else:
                exp = float("nan")
            exponents.append(exp)
    return {
        "umax": umax,
        "total_l2": total_l2,
        "boundary_l2_frac": boundary_l2_frac,
        "rows": rows,
        "power_exponents_from_left": exponents,
    }


def _loglog_fit(r: np.ndarray, values: np.ndarray) -> dict:
    """Fit |z(a-r)| ~= C r^alpha on a selected positive-depth range."""
    abs_values = np.abs(values)
    scale = max(1.0, float(abs_values.max(initial=0.0)))
    mask = (r > 0.0) & (abs_values > 1e-10 * scale)
    if int(np.count_nonzero(mask)) < 3:
        return {
            "alpha": float("nan"),
            "intercept": float("nan"),
            "r2": float("nan"),
            "n": int(np.count_nonzero(mask)),
        }
    x = np.log(r[mask])
    y = np.log(abs_values[mask])
    alpha, intercept = np.polyfit(x, y, 1)
    pred = alpha * x + intercept
    ss_res = float(np.sum((y - pred) ** 2))
    ss_tot = float(np.sum((y - float(np.mean(y))) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-14 else float("nan")
    return {
        "alpha": float(alpha),
        "intercept": float(intercept),
        "r2": float(r2),
        "n": int(np.count_nonzero(mask)),
    }


def _weighted_power_model_ratio(lo: float, hi: float, logn: float,
                                edge: float, power: float,
                                samples: int = 4001) -> float:
    """Smooth-weighted average of (2a-U)^p divided by its atom value."""
    if not np.isfinite(power):
        return float("nan")
    Us = np.linspace(lo, hi, samples)
    widths = np.maximum(2.0 * edge - Us, 0.0)
    atom_width = max(2.0 * edge - logn, 0.0)
    if atom_width <= 0.0:
        return float("nan")
    weights = 2.0 * np.exp(0.5 * Us)
    profile = widths ** power
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    avg = float(trap(weights * profile, x=Us) / trap(weights, x=Us))
    return avg / (atom_width ** power)


def _boundary_profile(ambient, B: np.ndarray, f: np.ndarray,
                      repair_row: dict | None,
                      ngrid: int = 20001) -> dict:
    """Inspect the active debt vector z(v) near the physical support edge."""
    coeffs = B @ f
    edge = float(ambient.centers.max() + ambient.half_width)
    grid = np.linspace(-edge, edge, ngrid)
    basis = _raised_cosine_even(ambient.centers, ambient.half_width, grid)
    z = coeffs @ basis
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    total_l2 = float(trap(z * z, x=grid))

    reference_depths = [
        0.5 * ambient.half_width,
        ambient.half_width,
        2.0 * ambient.half_width,
        3.0 * ambient.half_width,
    ]
    model_cell = None
    if repair_row is not None:
        physical = repair_row["physical"]["rows"]
        reference_depths.extend(
            row["overlap_width"] for row in physical
            if np.isfinite(row["overlap_width"]) and row["overlap_width"] > 0.0
        )
        lo, hi = repair_row["cell"]
        model_cell = (lo, hi, repair_row["logn"])
    max_depth = min(edge, max(reference_depths))
    depths = sorted({
        round(float(depth), 12)
        for depth in reference_depths
        if np.isfinite(depth) and 0.0 < depth <= edge
    })

    sample_rows = []
    for depth in depths:
        val = float((coeffs @ _raised_cosine_even(
            ambient.centers,
            ambient.half_width,
            np.array([edge - depth]),
        ))[0])
        mask = np.abs(grid) >= edge - depth
        edge_l2 = (
            float(trap(np.where(mask, z * z, 0.0), x=grid) / total_l2)
            if total_l2 > 1e-14 else float("nan")
        )
        sample_rows.append({
            "depth": depth,
            "z": val,
            "abs_z": abs(val),
            "edge_l2_frac": edge_l2,
        })

    fit_grid = np.geomspace(max(1e-5, max_depth * 1e-5), max_depth, 800)
    fit_values = coeffs @ _raised_cosine_even(ambient.centers, ambient.half_width, edge - fit_grid)
    fit_windows = [
        ("half support", 0.5 * ambient.half_width),
        ("one support", ambient.half_width),
    ]
    if repair_row is not None:
        fit_windows.append(("repair atom width", max(2.0 * edge - repair_row["logn"], 0.0)))
        lo, _ = repair_row["cell"]
        fit_windows.append(("repair left width", max(2.0 * edge - lo, 0.0)))
    fit_rows = []
    for label, hi_depth in fit_windows:
        if not np.isfinite(hi_depth) or hi_depth <= 0.0:
            continue
        lo_depth = max(1e-5, 1e-3 * hi_depth)
        mask = (fit_grid >= lo_depth) & (fit_grid <= min(hi_depth, max_depth))
        fit = _loglog_fit(fit_grid[mask], fit_values[mask])
        alpha = fit["alpha"]
        fit_rows.append({
            "label": label,
            "lo_depth": lo_depth,
            "hi_depth": min(hi_depth, max_depth),
            "alpha": alpha,
            "autocorr_power": 2.0 * alpha + 1.0 if np.isfinite(alpha) else float("nan"),
            "r2": fit["r2"],
            "n": fit["n"],
        })

    dense_depths = np.linspace(max(1e-5, 1e-4 * max_depth), max_depth, 4000)
    dense_values = coeffs @ _raised_cosine_even(ambient.centers, ambient.half_width, edge - dense_depths)
    scale = max(1.0, float(np.max(np.abs(dense_values))))
    active = np.abs(dense_values) > 1e-8 * scale
    signs = np.sign(dense_values[active])
    sign_changes = int(np.count_nonzero(signs[1:] * signs[:-1] < 0.0)) if signs.size else 0

    model_rows = []
    if model_cell is not None:
        lo, hi, logn = model_cell
        observed_power = repair_row["physical"]["power_exponents_from_left"][1]
        powers = [2.5, observed_power]
        powers.extend(row["autocorr_power"] for row in fit_rows)
        seen = set()
        for power in powers:
            if not np.isfinite(power):
                continue
            key = round(float(power), 6)
            if key in seen:
                continue
            seen.add(key)
            model_rows.append({
                "power": float(power),
                "avg_over_atom": _weighted_power_model_ratio(lo, hi, logn, edge, float(power)),
            })

    coeff_rows = []
    for idx in np.argsort(ambient.centers)[-5:][::-1]:
        coeff_rows.append({
            "index": int(idx),
            "center": float(ambient.centers[idx]),
            "right_edge_gap": float(edge - ambient.centers[idx]),
            "coeff": float(coeffs[idx]),
        })

    return {
        "edge": edge,
        "max_depth": max_depth,
        "total_l2": total_l2,
        "samples": sample_rows,
        "fits": fit_rows,
        "sign_changes": sign_changes,
        "model_rows": model_rows,
        "coefficients": coeff_rows,
    }


def context_for_basis(ncenters: int, half_width: float,
                      left: float = LATE_EDGE[0],
                      right: float = LATE_EDGE[1],
                      physical_ngrid: int = 6001):
    ambient = build_ambient(
        ncenters=ncenters,
        half_width=half_width,
        cmax=right / 2.0 - half_width,
        max_gmax=right,
        physical_ngrid=physical_ngrid,
    )
    points = {
        left: point(ambient, "zeta", left),
        right: point(ambient, "zeta", right),
    }
    return ambient, points


def active_debt_report(left: float = LATE_EDGE[0], right: float = LATE_EDGE[1],
                       ambient=None, points=None) -> dict:
    if ambient is None or points is None:
        ambient, points = ambient_and_points()
    B = edge_basis(ambient, points, left, right)
    old_dim = points[left]["basis"].shape[1]
    base = extension_base_margin(ambient, left, right, "zeta")
    block = _sym(B.T @ base @ B)
    A, C, _ = _blocks(block, old_dim)
    schur = _sym(_blocks(block, old_dim)[2] - C.T @ np.linalg.solve(A, C))
    debt, y = _min_pair(schur)
    x = np.linalg.solve(A, C @ y)
    f = np.concatenate([x, -y])

    cells = interval_residual_cells(ambient, left, right, "zeta")
    bounds = _cell_bounds_for_atoms(ambient, left, right)
    rows = []
    current = block.copy()
    for n, cell_full in sorted(cells.items()):
        cell = _sym(B.T @ cell_full @ B)
        smooth_full = smooth_cell_operator(ambient, *bounds[n])
        atom_full = ambient.atoms["zeta"][n]
        smooth_block = _sym(B.T @ smooth_full @ B)
        atom_block = _sym(B.T @ atom_full @ B)
        smooth_q = _quadratic(smooth_block, f)
        atom_q = _quadratic(atom_block, f)
        residual_q = smooth_q - atom_q
        lo, hi = bounds[n]
        mid = 0.5 * (lo + hi)
        smooth_mass = 4.0 * (math.exp(0.5 * hi) - math.exp(0.5 * lo))
        k_lo = _kernel_value(ambient, B, f, lo)
        k_mid = _kernel_value(ambient, B, f, mid)
        k_atom = _kernel_value(ambient, B, f, math.log(n))
        k_hi = _kernel_value(ambient, B, f, hi)
        shape = _kernel_shape(ambient, B, f, lo, hi, math.log(n))
        physical = _physical_overlap_shape(ambient, B, f, (lo, mid, math.log(n), hi))
        atom_weight = atom_q / k_atom if abs(k_atom) > 1e-14 else float("nan")
        ric = riccati_cell(current, cell, old_dim)
        square_ray = ric["ray_square_on_before_min"]
        G_ray = ric["ray_increment_on_before_min"]
        Q_ray = ric["ray_Q_on_before_min"]
        split = ric.get("debt_split", {})
        leakage = split.get("leakage", 0.0) if split else 0.0
        debt_need = max(0.0, -ric["before_min"])
        required_residual = debt_need + square_ray + leakage
        repair_surplus = residual_q - required_residual
        avg_k = smooth_q / smooth_mass if abs(smooth_mass) > 1e-14 else float("nan")
        avg_over_atom_k = avg_k / k_atom if abs(k_atom) > 1e-14 else float("nan")
        required_avg_over_atom_k = (
            (atom_q + required_residual) / (smooth_mass * k_atom)
            if abs(smooth_mass * k_atom) > 1e-14 else float("nan")
        )
        rows.append({
            "n": n,
            "logn": math.log(n),
            "cell": bounds[n],
            "smooth_q": smooth_q,
            "atom_q": atom_q,
            "residual_q": residual_q,
            "atom_weight": atom_weight,
            "smooth_mass": smooth_mass,
            "smooth_mass_ratio": smooth_mass / atom_weight if abs(atom_weight) > 1e-14 else float("nan"),
            "k_lo": k_lo,
            "k_mid": k_mid,
            "k_atom": k_atom,
            "k_hi": k_hi,
            "shape": shape,
            "physical": physical,
            "smooth_atom_ratio": smooth_q / atom_q if abs(atom_q) > 1e-14 else float("nan"),
            "Q_ray": Q_ray,
            "square_ray": square_ray,
            "G_ray": G_ray,
            "before_min": ric["before_min"],
            "after_min": ric["after_min"],
            "debt_need": debt_need,
            "required_residual": required_residual,
            "repair_surplus": repair_surplus,
            "avg_over_atom_k": avg_over_atom_k,
            "required_avg_over_atom_k": required_avg_over_atom_k,
            "debt_split": split,
        })
        current = _sym(current + cell)

    repair_rows = [
        row for row in rows
        if row["before_min"] < -1e-9 or row["after_min"] < -1e-9
    ]
    repair_row = repair_rows[0] if repair_rows else max(rows, key=lambda item: item["residual_q"])
    boundary_profile = _boundary_profile(ambient, B, f, repair_row)

    exact_margin = margin_at(ambient, "zeta", right)
    exact_block = _sym(B.T @ exact_margin @ B)
    final_A, final_C, final_D = _blocks(exact_block, old_dim)
    final_schur = _sym(final_D - final_C.T @ np.linalg.solve(final_A, final_C))
    final_min = _min_pair(final_schur)[0]
    return {
        "left": left,
        "right": right,
        "ncenters": len(ambient.centers),
        "half_width": ambient.half_width,
        "old_dim": old_dim,
        "shell_dim": B.shape[1] - old_dim,
        "base_schur_min": debt,
        "final_schur_min": final_min,
        "rows": rows,
        "boundary_profile": boundary_profile,
    }


def _print_report(report: dict) -> None:
    print("=" * 78)
    print("Active-debt arithmetic current")
    print("=" * 78)
    print(f"edge {report['left']:.2f}->{report['right']:.2f}, "
          f"basis n={report['ncenters']} hw={report['half_width']:.3f}, "
          f"dims {report['old_dim']}+{report['shell_dim']}, "
          f"base Schur {report['base_schur_min']:+.6e}, "
          f"final Schur {report['final_schur_min']:+.6e}")
    print("\n[cell currents on f=x-y]")
    print("      n     cell interval          smooth      atom        smooth-atom   "
          "Q_ray      square     G_ray")
    for row in report["rows"]:
        lo, hi = row["cell"]
        print(f"      {row['n']:<4d} [{lo:.6f},{hi:.6f}] "
              f"{row['smooth_q']:+.6e} "
              f"{row['atom_q']:+.6e} "
              f"{row['residual_q']:+.6e} "
              f"{row['Q_ray']:+.6e} "
              f"{row['square_ray']:+.6e} "
              f"{row['G_ray']:+.6e}")
        split = row.get("debt_split") or {}
        if split:
            print("           split after this cell: "
                  f"head={split['head_after']:+.6e}, "
                  f"compMin={split['comp_min_after']:+.6e}, "
                  f"cross={split['cross_norm_after']:.6e}, "
                  f"leak={split['leakage']:+.6e}, "
                  f"reduced={split['reduced_after']:+.6e}")
        print("           kernel on initial debt stress: "
              f"k(lo)={row['k_lo']:+.6e}, "
              f"k(mid)={row['k_mid']:+.6e}, "
              f"k(log n)={row['k_atom']:+.6e}, "
              f"k(hi)={row['k_hi']:+.6e}, "
              f"weight={row['atom_weight']:.6e}, "
              f"mass/weight={row['smooth_mass_ratio']:.3f}, "
              f"smooth/atom={row['smooth_atom_ratio']:.3f}")
        if row["debt_need"] > 0.0:
            print("           repair budget: "
                  f"need={row['required_residual']:+.6e}, "
                  f"surplus={row['repair_surplus']:+.6e}, "
                  f"avg/k_atom={row['avg_over_atom_k']:.3f}, "
                  f"required avg/k_atom={row['required_avg_over_atom_k']:.3f}")
        shape = row["shape"]
        print("           shape: "
              f"monotone_down={shape['monotone_nonincreasing']} "
              f"kRange=[{shape['sample_min']:+.3e},{shape['sample_max']:+.3e}] "
              f"maxUp={shape['max_up_step']:+.3e} "
              f"centroidRel={shape['smooth_centroid_rel']:.3f} "
              f"atomRel={shape['atom_rel']:.3f} "
              f"leftHalf={shape['left_half_fraction']:.3f} "
              f"smoothApprox={shape['smooth_approx']:+.6e}")
        physical = row["physical"]
        print("           physical overlap: "
              f"umax={physical['umax']:.3f}, "
              f"boundaryL2={physical['boundary_l2_frac']:.3f}")
        for prow in physical["rows"]:
            print("             "
                  f"U={prow['U']:.6f} "
                  f"k_phys={prow['mass']:+.6e} "
                  f"overlap=[{prow['overlap_v_min']:.3f},{prow['overlap_v_max']:.3f}] "
                  f"width={prow['overlap_width']:.3f} "
                  f"centroid={prow['abs_centroid_v']:.3f} "
                  f"absWidth={prow['abs_width_v']:.3f}")
        exps = [x for x in physical["power_exponents_from_left"] if np.isfinite(x)]
        if exps:
            print("             "
                  f"overlap power exponents from left: "
                  f"{', '.join(f'{x:.2f}' for x in exps)}")

    profile = report["boundary_profile"]
    print("\n[active debt boundary profile]")
    print("      "
          f"positive edge a={profile['edge']:.6f}, "
          f"total L2={profile['total_l2']:.6e}, "
          f"edge sign changes={profile['sign_changes']}")
    print("      depth        z(a-depth)      edge L2 frac")
    for row in profile["samples"]:
        print(f"      {row['depth']:.6f}   "
              f"{row['z']:+.6e}   "
              f"{row['edge_l2_frac']:.3f}")
    print("      fits for |z(a-r)| ~= C r^alpha:")
    for row in profile["fits"]:
        print(f"        {row['label']:<17} "
              f"r=[{row['lo_depth']:.2e},{row['hi_depth']:.3f}] "
              f"alpha={row['alpha']:.3f} "
              f"p=2alpha+1={row['autocorr_power']:.3f} "
              f"r2={row['r2']:.3f} "
              f"n={row['n']}")
    print("      model avg/k(log repair atom) for k(U) proportional to (2a-U)^p:")
    for row in profile["model_rows"]:
        print(f"        p={row['power']:.3f}: avg/atom={row['avg_over_atom']:.3f}")
    print("      last physical coefficients:")
    for row in profile["coefficients"]:
        print(f"        i={row['index']:<2d} "
              f"center={row['center']:.6f} "
              f"gap={row['right_edge_gap']:.6f} "
              f"coeff={row['coeff']:+.6e}")

    print("\nInterpretation:")
    print("  * smooth-atom is the margin update from replacing the smooth incoming")
    print("    density by the exact Euler atom on this debt stress.")
    print("  * Q_ray matches smooth-atom on the active debt direction.  G_ray is")
    print("    the value after paying the Riccati square.")
    print("  * The proof target is to lower-bound smooth-atom on the active debt")
    print("    stress and show the complement leakage remains smaller than the")
    print("    repaired head margin.")


def refinement_table(configs: tuple[tuple[int, float], ...]) -> list[dict]:
    rows = []
    print("\n[active-debt refinement table]")
    print("      basis       base       final      repair n  mono  centroid atomRel  "
          "smooth/atom  avg/req surplus    reduced")
    for ncenters, half_width in configs:
        ambient, points = context_for_basis(ncenters, half_width)
        report = active_debt_report(ambient=ambient, points=points)
        repair_rows = [
            row for row in report["rows"]
            if row["before_min"] < -1e-9 or row["after_min"] < -1e-9
        ]
        row = repair_rows[0] if repair_rows else max(report["rows"], key=lambda item: item["residual_q"])
        split = row.get("debt_split") or {}
        reduced = split.get("reduced_after", float("nan"))
        fits = {item["label"]: item for item in report["boundary_profile"]["fits"]}
        exps = row["physical"]["power_exponents_from_left"]
        model25 = next(
            (
                item["avg_over_atom"]
                for item in report["boundary_profile"]["model_rows"]
                if abs(item["power"] - 2.5) < 1e-9
            ),
            float("nan"),
        )
        rows.append({
            "ncenters": ncenters,
            "half_width": half_width,
            "base": report["base_schur_min"],
            "final": report["final_schur_min"],
            "repair_n": row["n"],
            "monotone": row["shape"]["monotone_nonincreasing"],
            "centroid": row["shape"]["smooth_centroid_rel"],
            "atom_rel": row["shape"]["atom_rel"],
            "smooth_atom": row["smooth_atom_ratio"],
            "avg_over_atom": row["avg_over_atom_k"],
            "required_avg": row["required_avg_over_atom_k"],
            "surplus": row["repair_surplus"],
            "reduced": reduced,
            "alpha_one": fits["one support"]["alpha"],
            "alpha_atom": fits["repair atom width"]["alpha"],
            "alpha_left": fits["repair left width"]["alpha"],
            "p_eff_atom": exps[1] if len(exps) > 1 else float("nan"),
            "p_eff_hi": exps[2] if len(exps) > 2 else float("nan"),
            "model25": model25,
        })
        print(f"      n{ncenters:<2d}/h{half_width:.2f} "
              f"{report['base_schur_min']:+.3e} "
              f"{report['final_schur_min']:+.3e} "
              f"{row['n']:<8d} "
              f"{str(row['shape']['monotone_nonincreasing']):<5} "
              f"{row['shape']['smooth_centroid_rel']:.3f}    "
              f"{row['shape']['atom_rel']:.3f}    "
              f"{row['smooth_atom_ratio']:.3f}       "
              f"{row['avg_over_atom_k']:.3f}/{row['required_avg_over_atom_k']:.3f} "
              f"{row['repair_surplus']:+.3e} "
              f"{reduced:+.3e}")
    print("\n[boundary-profile refinement table]")
    print("      basis       alpha1  alphaAtom alphaLeft pEffAtom pEffHi  model p=2.5")
    for row in rows:
        print(f"      n{row['ncenters']:<2d}/h{row['half_width']:.3f} "
              f"{row['alpha_one']:+.3f}   "
              f"{row['alpha_atom']:+.3f}    "
              f"{row['alpha_left']:+.3f}    "
              f"{row['p_eff_atom']:+.3f}   "
              f"{row['p_eff_hi']:+.3f}   "
              f"{row['model25']:.3f}")
    return rows


def summary(with_refinements: bool = False) -> dict:
    report = active_debt_report()
    _print_report(report)
    if with_refinements:
        report["refinements"] = refinement_table((
            (17, 0.10),
            (21, 0.08),
            (25, 0.06),
            (29, 0.05),
            (33, 0.045),
        ))
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--refinements", action="store_true")
    args = parser.parse_args()
    summary(with_refinements=args.refinements)
