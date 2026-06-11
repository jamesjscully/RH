"""Atom-level coefficient sensitivity for passive shell transfer.

The scale-threshold witnesses show that old Euler history is tightly
calibrated.  This script asks which weighted Euler atoms are responsible for
the local passive-transfer wall by differentiating the transfer quantity

    rho = ||A^{-1/2} C D^{-1/2}||^2

with respect to the scale of each already-weighted zeta atom.

The derivative is finite-difference, but it perturbs the full atom matrix, so
it measures sensitivity to the exact von Mangoldt-scaled Toeplitz contribution
rather than to an unweighted support indicator.

Run:
    python3 -m scripts.numerics.witness.prime_defect_atom_sensitivity
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_scale_phase import FOCUS_EDGES, _invsqrt_spd, ambient_and_points
from .prime_nested_cone import _orthogonal_shell


EPS = 1e-5


def _prime_power_label(n: int) -> str:
    for p in range(2, int(math.sqrt(n)) + 1):
        if n % p:
            continue
        k = 0
        m = n
        while m % p == 0:
            m //= p
            k += 1
        if m == 1:
            return f"{p}^{k}" if k > 1 else str(p)
    return str(n)


def scaled_atom_margin(ambient, right_gmax: float,
                       scales: dict[int, float] | None = None) -> np.ndarray:
    scales = scales or {}
    margin = ambient.gram["Winf"].copy()
    for n, atom in ambient.atoms["zeta"].items():
        if math.log(n) < right_gmax:
            margin = margin - scales.get(n, 1.0) * atom
    return _sym(margin)


def edge_transfer(ambient, points: dict[float, dict], left_gmax: float,
                  right_gmax: float, scales: dict[int, float] | None = None) -> dict:
    M = scaled_atom_margin(ambient, right_gmax, scales)
    left = points[left_gmax]
    right = points[right_gmax]
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]
    block = _sym(B.T @ M @ B)
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])
    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    D_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])
    A_invsqrt = _invsqrt_spd(A)
    D_invsqrt = _invsqrt_spd(D)
    if A_invsqrt is None or D_invsqrt is None:
        return {
            "valid": False,
            "rho": float("nan"),
            "defect": float("nan"),
            "A_min": float(A_eigs[0]),
            "D_min": float(D_eigs[0]),
            "top_sval": float("nan"),
        }
    K = A_invsqrt @ C @ D_invsqrt
    svals = np.linalg.svd(K, compute_uv=False)
    top = float(svals[0]) if len(svals) else float("nan")
    rho = top ** 2
    return {
        "valid": True,
        "rho": float(rho),
        "defect": float(1.0 - rho),
        "A_min": float(A_eigs[0]),
        "D_min": float(D_eigs[0]),
        "top_sval": top,
    }


def atom_derivatives(ambient, points: dict[float, dict], left_gmax: float,
                     right_gmax: float, eps: float = EPS) -> dict:
    base = edge_transfer(ambient, points, left_gmax, right_gmax)
    rows = []
    for n in sorted(ambient.atoms["zeta"]):
        logn = math.log(n)
        if logn >= right_gmax:
            continue
        plus = edge_transfer(ambient, points, left_gmax, right_gmax, {n: 1.0 + eps})
        minus = edge_transfer(ambient, points, left_gmax, right_gmax, {n: 1.0 - eps})
        if plus["valid"] and minus["valid"]:
            slope = (plus["rho"] - minus["rho"]) / (2.0 * eps)
        else:
            slope = float("nan")
        rows.append({
            "n": n,
            "label": _prime_power_label(n),
            "logn": logn,
            "region": "old" if logn < left_gmax else "new",
            "slope": float(slope),
            "abs_slope": float(abs(slope)) if math.isfinite(slope) else float("nan"),
        })
    old_sum = sum(row["slope"] for row in rows if row["region"] == "old")
    new_sum = sum(row["slope"] for row in rows if row["region"] == "new")
    pos_mass = sum(row["slope"] for row in rows if row["slope"] > 0.0)
    neg_mass = sum(row["slope"] for row in rows if row["slope"] < 0.0)
    return {
        "left": left_gmax,
        "right": right_gmax,
        "base": base,
        "rows": rows,
        "old_sum": float(old_sum),
        "new_sum": float(new_sum),
        "pos_mass": float(pos_mass),
        "neg_mass": float(neg_mass),
    }


def _fmt_row(row: dict) -> str:
    return (f"{row['label']:<4} "
            f"n={row['n']:<2d} "
            f"log={row['logn']:.3f} "
            f"{row['region']:<3} "
            f"d rho/d scale={row['slope']:+.4f}")


def _print_edge(report: dict, topn: int = 6) -> None:
    base = report["base"]
    print(f"\n[edge {report['left']:.2f}->{report['right']:.2f}] "
          f"rho={base['rho']:.6f}, defect={base['defect']:+.6f}, "
          f"Amin={base['A_min']:+.2e}, Dmin={base['D_min']:+.2e}")
    print(f"      derivative sums: old {report['old_sum']:+.4f}, "
          f"new {report['new_sum']:+.4f}, "
          f"positive {report['pos_mass']:+.4f}, negative {report['neg_mass']:+.4f}")
    strongest = sorted(report["rows"], key=lambda row: row["abs_slope"], reverse=True)[:topn]
    print("      strongest atoms:")
    for row in strongest:
        print(f"        {_fmt_row(row)}")
    improving = sorted(
        [row for row in report["rows"] if row["slope"] < 0.0],
        key=lambda row: row["slope"],
    )[:min(3, topn)]
    if improving:
        print("      strongest local repairs when increased:")
        for row in improving:
            print(f"        {_fmt_row(row)}")


def summary() -> dict:
    print("=" * 78)
    print("Atom-level sensitivity of passive shell transfer")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = atom_derivatives(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    late = reports[(3.00, 3.24)]
    old_rows = [row for row in late["rows"] if row["region"] == "old"]
    top_old = sorted(old_rows, key=lambda row: row["abs_slope"], reverse=True)[:5]
    total_abs = sum(row["abs_slope"] for row in old_rows)
    top_abs = sum(row["abs_slope"] for row in top_old)
    frac = top_abs / total_abs if total_abs else float("nan")
    print("\nInterpretation:")
    print("  * The derivative sums reproduce the old/new scale sensitivities, but")
    print("    the atom list shows whether those sums are localized or cumulative.")
    print("  * On the late blocker edge, the largest old sensitivities are spread")
    print("    across several prime-power atoms rather than a single new atom.")
    print(f"  * Top five old atoms carry {frac:.3f} of old absolute sensitivity on "
          "3.00->3.24 in this finite model.")
    return reports


if __name__ == "__main__":
    summary()
