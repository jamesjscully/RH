"""Lorentzian factorization of the variational stress density.

For a critical transfer mode, let X(t) be the Fourier amplitude of the old
generalized singular vector and Y(t) the shell amplitude.  Since rho=s^2,

    H(t) = rho X(t)^2 + rho Y(t)^2 - 2s X(t)Y(t)
         = ((rho+s)/2) (X-Y)^2 + ((rho-s)/2) (X+Y)^2.

The first coefficient is positive and the second is negative for 0<s<1.  Thus
the Euler current is a difference of two positive-type shift kernels: a
finite Pontryagin/Lorentz stress, not a Hilbert-positive sampling measure.

Run:
    python3 -m scripts.numerics.witness.prime_defect_lorentz_stress
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import coefficient_table
from .prime_defect_atom_sensitivity import _prime_power_label
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points
from .prime_defect_variational_current import critical_mode
from .semilocal_2 import _grids, _phihat


def amplitudes(ambient, mode: dict) -> dict:
    grid = _grids()
    ts, dt = grid["ts"], grid["dt"]
    ph = np.array([_phihat(ts, center, ambient.half_width) for center in ambient.centers])
    old_dim = mode["old_dim"]
    old_coeffs = mode["B"][:, :old_dim] @ mode["x"]
    shell_coeffs = mode["B"][:, old_dim:] @ mode["y"]
    X = old_coeffs @ ph
    Y = shell_coeffs @ ph
    s = mode["s"]
    rho = mode["rho"]
    pos_coeff = 0.5 * (rho + s)
    neg_coeff = 0.5 * (rho - s)
    pos_density = pos_coeff * (X - Y) ** 2
    neg_density = neg_coeff * (X + Y) ** 2
    total_density = pos_density + neg_density
    return {
        "ts": ts,
        "dt": dt,
        "X": X,
        "Y": Y,
        "pos_density": pos_density,
        "neg_density": neg_density,
        "total_density": total_density,
        "pos_coeff": pos_coeff,
        "neg_coeff": neg_coeff,
    }


def kernel_from_density(parts: dict, key: str, U: float) -> float:
    ts = parts["ts"]
    weights = parts[key] * parts["dt"] / (2.0 * np.pi)
    return float(np.cos(U * ts) @ weights)


def weighted_component_samples(ambient, mode: dict, parts: dict) -> list[dict]:
    max_n = max(ambient.atoms["zeta"])
    coeffs = coefficient_table("zeta", max_n)
    rows = []
    for n in sorted(ambient.atoms["zeta"]):
        U = math.log(n)
        if U >= mode["right"]:
            continue
        weight = 2.0 * coeffs[n - 1] / math.sqrt(n)
        pos = weight * kernel_from_density(parts, "pos_density", U)
        neg = weight * kernel_from_density(parts, "neg_density", U)
        rows.append({
            "n": n,
            "label": _prime_power_label(n),
            "logn": U,
            "region": "old" if U < mode["left"] else "new",
            "pos": pos,
            "neg": neg,
            "total": pos + neg,
            "weight": weight,
        })
    return rows


def edge_report(ambient, points, left: float, right: float) -> dict:
    mode = critical_mode(ambient, points, left, right)
    parts = amplitudes(ambient, mode)
    rows = weighted_component_samples(ambient, mode, parts)
    quad_weight = parts["dt"] / (2.0 * np.pi)
    return {
        "mode": mode,
        "parts": parts,
        "rows": rows,
        "pos_mass": float(np.sum(parts["pos_density"]) * quad_weight),
        "neg_mass": float(np.sum(parts["neg_density"]) * quad_weight),
        "total_mass": float(np.sum(parts["total_density"]) * quad_weight),
        "reconstruction_error": float(np.max(np.abs(
            parts["total_density"]
            - (
                mode["rho"] * parts["X"] ** 2
                + mode["rho"] * parts["Y"] ** 2
                - 2.0 * mode["s"] * parts["X"] * parts["Y"]
            )
        ))),
    }


def _sum(rows: list[dict], key: str, region: str | None = None) -> float:
    return float(sum(row[key] for row in rows if region is None or row["region"] == region))


def _print_edge(report: dict, topn: int = 5) -> None:
    mode = report["mode"]
    parts = report["parts"]
    rows = report["rows"]
    print(f"\n[edge {mode['left']:.2f}->{mode['right']:.2f}] "
          f"s={mode['s']:.6f}, rho={mode['rho']:.6f}, defect={mode['defect']:+.6f}")
    print(f"      coeffs: positive {parts['pos_coeff']:+.6f}, "
          f"negative {parts['neg_coeff']:+.6f}, "
          f"density check {report['reconstruction_error']:.2e}")
    print(f"      kernel mass at U=0: pos {report['pos_mass']:+.3f}, "
          f"neg {report['neg_mass']:+.3f}, total {report['total_mass']:+.3f}")
    print(f"      Euler weighted sums: old pos {_sum(rows, 'pos', 'old'):+.3f}, "
          f"old neg {_sum(rows, 'neg', 'old'):+.3f}, "
          f"old total {_sum(rows, 'total', 'old'):+.3f}; "
          f"new total {_sum(rows, 'total', 'new'):+.3f}")
    print("      largest signed atom components:")
    for row in sorted(rows, key=lambda item: abs(item["total"]), reverse=True)[:topn]:
        print(f"        {row['label']:<4} {row['region']:<3} "
              f"pos={row['pos']:+.3f} "
              f"neg={row['neg']:+.3f} "
              f"total={row['total']:+.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Lorentzian factorization of the variational stress")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    print("\nInterpretation:")
    print("  * The critical stress is a rank-two Lorentz form: positive kernel")
    print("    from X-Y and negative kernel from X+Y.")
    print("  * In these windows the negative square component is small; most")
    print("    pointwise sign changes come from the cosine transform of the")
    print("    dominant positive spectral density, which need not be pointwise")
    print("    positive away from U=0.")
    print("  * This still points toward a de Branges/canonical-system proof object:")
    print("    positive type in frequency is not the same as positive sampling at")
    print("    the prime-power shifts.")
    return reports


if __name__ == "__main__":
    summary()
