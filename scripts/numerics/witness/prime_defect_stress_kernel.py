"""Shift-kernel profile of the variational Euler current.

The variational-current witness gives an atom pairing

    d rho / d scale(atom_U) = <atom_U, stress_{L,L'}>.

Because each Toeplitz atom is a cosine transform,

    atom_U(i,j) = (1/2pi) int phihat_i(t) phihat_j(t) cos(U t) dt,

the stress pairing is itself a shift kernel

    k_{L,L'}(U) = (1/2pi) int H_{L,L'}(t) cos(U t) dt,
    H(t) = phihat(t)^T S phihat(t).

For zeta atoms, the weighted atom sensitivity is

    2 Lambda(n) / sqrt(n) * k_{L,L'}(log n).

This is the finite version of the Euler current that the proof target has to
control.

Run:
    python3 -m scripts.numerics.witness.prime_defect_stress_kernel
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import coefficient_table
from .prime_defect_atom_sensitivity import _prime_power_label
from .prime_defect_scale_phase import FOCUS_EDGES, ambient_and_points
from .prime_defect_variational_current import atom_current_rows, critical_mode
from .semilocal_2 import _grids, _phihat


def stress_matrix(mode: dict) -> np.ndarray:
    old_dim = mode["old_dim"]
    shell_dim = mode["B"].shape[1] - old_dim
    W = np.zeros((old_dim + shell_dim, old_dim + shell_dim))
    x = mode["x"]
    y = mode["y"]
    rho = mode["rho"]
    s = mode["s"]
    W[:old_dim, :old_dim] = rho * np.outer(x, x)
    W[old_dim:, old_dim:] = rho * np.outer(y, y)
    W[:old_dim, old_dim:] = -s * np.outer(x, y)
    W[old_dim:, :old_dim] = -s * np.outer(y, x)
    return mode["B"] @ W @ mode["B"].T


def stress_density(ambient, mode: dict) -> dict:
    grid = _grids()
    ts, dt = grid["ts"], grid["dt"]
    ph = np.array([_phihat(ts, center, ambient.half_width) for center in ambient.centers])
    S = stress_matrix(mode)
    density = np.einsum("it,ij,jt->t", ph, S, ph, optimize=True)
    return {
        "ts": ts,
        "dt": dt,
        "density": density,
        "stress": S,
    }


def kernel_values(density: dict, Us: np.ndarray) -> np.ndarray:
    ts = density["ts"]
    weights = density["density"] * density["dt"] / (2.0 * np.pi)
    return np.cos(np.outer(Us, ts)) @ weights


def sample_kernel(density: dict, U: float) -> float:
    return float(kernel_values(density, np.array([U]))[0])


def sign_changes(values: np.ndarray) -> int:
    signs = np.sign(values)
    signs = signs[signs != 0]
    if len(signs) < 2:
        return 0
    return int(np.sum(signs[1:] != signs[:-1]))


def local_extrema(Us: np.ndarray, values: np.ndarray, count: int = 3) -> tuple[list[dict], list[dict]]:
    extrema = []
    for i in range(1, len(values) - 1):
        if values[i] >= values[i - 1] and values[i] >= values[i + 1]:
            extrema.append({"U": float(Us[i]), "value": float(values[i]), "kind": "max"})
        elif values[i] <= values[i - 1] and values[i] <= values[i + 1]:
            extrema.append({"U": float(Us[i]), "value": float(values[i]), "kind": "min"})
    maxima = sorted(
        [row for row in extrema if row["kind"] == "max"],
        key=lambda row: row["value"],
        reverse=True,
    )[:count]
    minima = sorted(
        [row for row in extrema if row["kind"] == "min"],
        key=lambda row: row["value"],
    )[:count]
    return maxima, minima


def weighted_samples(ambient, density: dict, mode: dict) -> list[dict]:
    max_n = max(ambient.atoms["zeta"])
    coeffs = coefficient_table("zeta", max_n)
    analytic = {row["n"]: row for row in atom_current_rows(ambient, mode)}
    rows = []
    for n in sorted(ambient.atoms["zeta"]):
        logn = math.log(n)
        if logn >= mode["right"]:
            continue
        weight = 2.0 * coeffs[n - 1] / math.sqrt(n)
        kU = sample_kernel(density, logn)
        weighted = weight * kU
        rows.append({
            "n": n,
            "label": _prime_power_label(n),
            "logn": logn,
            "region": "old" if logn < mode["left"] else "new",
            "weight": weight,
            "kernel": kU,
            "weighted": weighted,
            "analytic": analytic[n]["slope"],
            "error": weighted - analytic[n]["slope"],
        })
    return rows


def edge_report(ambient, points, left: float, right: float) -> dict:
    mode = critical_mode(ambient, points, left, right)
    density = stress_density(ambient, mode)
    Us = np.linspace(0.0, right, 801)
    vals = kernel_values(density, Us)
    samples = weighted_samples(ambient, density, mode)
    return {
        "mode": mode,
        "density": density,
        "Us": Us,
        "values": vals,
        "samples": samples,
    }


def _sum(rows: list[dict], key: str, region: str | None = None) -> float:
    return float(sum(row[key] for row in rows if region is None or row["region"] == region))


def _print_edge(report: dict, topn: int = 5) -> None:
    mode = report["mode"]
    vals = report["values"]
    Us = report["Us"]
    samples = report["samples"]
    old_vals = vals[Us < mode["left"]]
    new_vals = vals[(Us >= mode["left"]) & (Us < mode["right"])]
    max_err = max(abs(row["error"]) for row in samples)
    print(f"\n[edge {mode['left']:.2f}->{mode['right']:.2f}] "
          f"rho={mode['rho']:.6f}, defect={mode['defect']:+.6f}")
    print(f"      kernel range old [{old_vals.min():+.3f},{old_vals.max():+.3f}], "
          f"new [{new_vals.min():+.3f},{new_vals.max():+.3f}], "
          f"sign changes {sign_changes(vals)}, weighted-sample err {max_err:.2e}")
    print(f"      Euler sums: old {_sum(samples, 'weighted', 'old'):+.4f}, "
          f"new {_sum(samples, 'weighted', 'new'):+.4f}")
    print("      strongest weighted samples:")
    for row in sorted(samples, key=lambda item: abs(item["weighted"]), reverse=True)[:topn]:
        print(f"        {row['label']:<4} "
              f"U={row['logn']:.3f} {row['region']:<3} "
              f"w={row['weight']:.3f} "
              f"k(U)={row['kernel']:+.3f} "
              f"w*k={row['weighted']:+.4f}")


def _print_late_partial(report: dict) -> None:
    print("\n[late old-history cumulative current, 3.00->3.24]")
    total = 0.0
    print("      atom   U      weight   k(U)     weighted   cumulative")
    for row in report["samples"]:
        if row["region"] != "old":
            continue
        total += row["weighted"]
        print(f"      {row['label']:<4} "
              f"{row['logn']:.3f}  "
              f"{row['weight']:.3f}   "
              f"{row['kernel']:+.3f}  "
              f"{row['weighted']:+.4f}   "
              f"{total:+.4f}")


def _print_late_extrema(report: dict) -> None:
    maxima, minima = local_extrema(report["Us"], report["values"])
    print("\n[late shift-kernel extrema, 3.00->3.24]")
    print("      largest positive extrema:")
    for row in maxima:
        print(f"        U={row['U']:.3f}, k(U)={row['value']:+.3f}")
    print("      largest negative extrema:")
    for row in minima:
        print(f"        U={row['U']:.3f}, k(U)={row['value']:+.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Shift-kernel profile of the variational Euler current")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    late = reports[(3.00, 3.24)]
    _print_late_partial(late)
    _print_late_extrema(late)

    print("\nInterpretation:")
    print("  * The variational stress tensor defines a genuine shift kernel k(U);")
    print("    atom sensitivities are exactly Euler weights times k(log n).")
    print("  * The late kernel is oscillatory on the old-history interval, so the")
    print("    narrow coefficient tube comes from sampling an indefinite current")
    print("    at the prime-power logarithms with exact von Mangoldt weights.")
    print("  * This is the concrete finite target for an Euler Green identity:")
    print("    control sum 2 Lambda(n)n^{-1/2} k(log n) for every critical stress.")
    return reports


if __name__ == "__main__":
    summary()
