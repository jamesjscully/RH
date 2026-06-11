"""Chebyshev-error integration by parts for the Euler stress residual.

The Euler-measure witness showed that the discrete prime-power measure is not
well replaced by the smooth PNT density.  This script rewrites the residual
against a stress kernel as a pairing with the cumulative Chebyshev error.

For

    phi(U) = 2 exp(-U/2) k(U),
    F(U) = sum_{log 2 <= log n <= U} Lambda(n) - (exp(U) - 2),

the residual on [log 2, B] is

    R(B) = sum_{log n <= B} Lambda(n) phi(log n)
           - int_{log 2}^B phi(U) exp(U) dU
         = phi(B) F(B) - int_{log 2}^B F(U) phi'(U) dU.

This turns the arithmetic residual into a boundary Chebyshev term plus a
distributed coupling of the cumulative error with the stress-kernel derivative.

Run:
    python3 -m scripts.numerics.witness.prime_defect_chebyshev_residual
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import coefficient_table
from .prime_defect_euler_measure import continuous_integral, discrete_sums
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points
from .prime_defect_stress_kernel import edge_report, kernel_values


LOG2 = math.log(2.0)


def _trapz(values: np.ndarray, grid: np.ndarray) -> float:
    trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trap(values, x=grid))


def kernel_and_derivative(density: dict, Us: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    ts = density["ts"]
    weights = density["density"] * density["dt"] / (2.0 * np.pi)
    phase = np.outer(Us, ts)
    k = np.cos(phase) @ weights
    kp = -np.sin(phase) @ (ts * weights)
    return k, kp


def phi_and_derivative(report: dict, Us: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    k, kp = kernel_and_derivative(report["density"], Us)
    factor = 2.0 * np.exp(-0.5 * Us)
    phi = factor * k
    phip = factor * (kp - 0.5 * k)
    return phi, phip


def chebyshev_error_grid(right: float, ngrid: int = 10001) -> dict:
    Us = np.linspace(LOG2, right, ngrid)
    max_n = max(2, int(math.floor(math.exp(right) - 1e-12)))
    coeffs = coefficient_table("zeta", max_n)
    active = np.array([coeffs[n - 1] for n in range(2, max_n + 1)])
    prefix = np.concatenate([[0.0], np.cumsum(active)])
    ns = np.arange(2, max_n + 1)
    idx = np.searchsorted(np.log(ns), Us, side="right")
    psi = prefix[idx]
    F = psi - (np.exp(Us) - 2.0)
    return {"Us": Us, "F": F}


def cumulative_trapezoid(values: np.ndarray, grid: np.ndarray) -> np.ndarray:
    out = np.zeros_like(values)
    if len(values) <= 1:
        return out
    increments = 0.5 * (values[1:] + values[:-1]) * np.diff(grid)
    out[1:] = np.cumsum(increments)
    return out


def build_cheb_integrator(edge_report: dict, right: float, ngrid: int = 3001) -> dict:
    cheb = chebyshev_error_grid(right, ngrid=ngrid)
    Us = cheb["Us"]
    F = cheb["F"]
    k = kernel_values(edge_report["density"], Us)
    phi = 2.0 * np.exp(-0.5 * Us) * k
    phip = np.gradient(phi, Us)
    distributed_integrand = -F * phip
    return {
        "Us": Us,
        "F": F,
        "phi": phi,
        "phip": phip,
        "distributed_cum": cumulative_trapezoid(distributed_integrand, Us),
    }


def _interp(integrator: dict, key: str, U: float) -> float:
    Us = integrator["Us"]
    Uc = min(max(float(U), float(Us[0])), float(Us[-1]))
    return float(np.interp(Uc, Us, integrator[key]))


def direct_residual(report: dict, hi: float) -> dict:
    edge = report["edge_report"]
    rows = [row for row in edge["samples"] if row["logn"] <= hi + 1e-12]
    disc = sum(row["weighted"] for row in rows)
    main = continuous_integral(report["integrator"], LOG2, hi)["signed"]
    return {"discrete": float(disc), "main": float(main), "residual": float(disc - main)}


def ibp_residual(report: dict, hi: float) -> dict:
    integrator = report["cheb_integrator"]
    F_hi = _interp(integrator, "F", hi)
    phi_hi = _interp(integrator, "phi", hi)
    boundary = float(phi_hi * F_hi)
    distributed = _interp(integrator, "distributed_cum", hi)
    return {
        "boundary": boundary,
        "distributed": distributed,
        "total": boundary + distributed,
        "F_end": F_hi,
        "F_max_abs": float(np.max(np.abs(integrator["F"][integrator["Us"] <= hi + 1e-12]))),
        "phi_end": phi_hi,
        "phip_l1": _trapz(
            np.abs(integrator["phip"][integrator["Us"] <= hi + 1e-12]),
            integrator["Us"][integrator["Us"] <= hi + 1e-12],
        ),
    }


def edge_chebyshev_report(ambient, points, left: float, right: float) -> dict:
    edge = edge_report(ambient, points, left, right)
    # Build the same continuous-integral table used by the Euler-measure witness.
    from .prime_defect_euler_measure import build_integrator

    wrapped = {
        "edge_report": edge,
        "integrator": build_integrator(edge, LOG2, right),
        "cheb_integrator": build_cheb_integrator(edge, right),
    }
    old_direct = direct_residual(wrapped, left)
    all_direct = direct_residual(wrapped, right)
    old_ibp = ibp_residual(wrapped, left)
    all_ibp = ibp_residual(wrapped, right)
    return {
        "left": left,
        "right": right,
        "edge_report": edge,
        "integrator": wrapped["integrator"],
        "cheb_integrator": wrapped["cheb_integrator"],
        "old_direct": old_direct,
        "all_direct": all_direct,
        "old_ibp": old_ibp,
        "all_ibp": all_ibp,
        "old_error": old_ibp["total"] - old_direct["residual"],
        "all_error": all_ibp["total"] - all_direct["residual"],
    }


def _print_part(label: str, direct: dict, ibp: dict, error: float) -> None:
    print(f"      {label:<4} "
          f"resid {direct['residual']:+.4f} = "
          f"boundary {ibp['boundary']:+.4f} + "
          f"distributed {ibp['distributed']:+.4f} "
          f"(err {error:+.2e}); "
          f"F_end {ibp['F_end']:+.3f}, "
          f"max|F| {ibp['F_max_abs']:.3f}")


def _print_edge(report: dict) -> None:
    print(f"\n[edge {report['left']:.2f}->{report['right']:.2f}]")
    _print_part("old", report["old_direct"], report["old_ibp"], report["old_error"])
    _print_part("all", report["all_direct"], report["all_ibp"], report["all_error"])


def _print_late_cumulative(report: dict) -> None:
    edge = report["edge_report"]
    print("\n[late Chebyshev residual by endpoint, 3.00->3.24]")
    print("      atom   U      residual   boundary   distributed   F_end")
    rows = [row for row in edge["samples"] if row["region"] == "old"]
    for row in rows:
        hi = row["logn"]
        direct = direct_residual(report, hi)
        ibp = ibp_residual(report, hi)
        print(f"      {row['label']:<4} "
              f"{hi:.3f}  "
              f"{direct['residual']:+.4f}   "
              f"{ibp['boundary']:+.4f}   "
              f"{ibp['distributed']:+.4f}     "
              f"{ibp['F_end']:+.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Chebyshev-error integration by parts for Euler stress residual")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_chebyshev_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    late = reports[(3.00, 3.24)]
    _print_late_cumulative(late)

    print("\nInterpretation:")
    print("  * The discrete-minus-smooth residual is exactly reproduced by")
    print("    Chebyshev integration by parts, up to quadrature error.")
    print("  * The residual is usually distributed through F(U) phi'(U), not just")
    print("    an endpoint Chebyshev boundary term.")
    print("  * The arithmetic object to control is therefore a cumulative error")
    print("    paired with the derivative of the admissible stress kernel.")
    return reports


if __name__ == "__main__":
    summary()
