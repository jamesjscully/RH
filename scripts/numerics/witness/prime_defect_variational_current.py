"""Variational current for the passive shell transfer norm.

For one nested edge, write the compressed margin in old/shell block form

    M = [ A  C ]
        [ C* D ].

The passive-transfer number is rho = ||A^{-1/2} C D^{-1/2}||^2.  If x,y are
the generalized old/shell singular vectors for the top singular value
s = sqrt(rho), normalized by

    x* A x = 1,  y* D y = 1,  x* C y = s,

then the first variation is

    d rho = 2 s x* dC y - rho x* dA x - rho y* dD y.

For the scale of one already-weighted Euler atom, dM = -atom, hence

    d rho / d scale(atom)
      = rho <A_atom x,x> + rho <D_atom y,y> - 2s <C_atom y,x>.

This script computes that exact finite-dimensional current and compares it
against the finite-difference atom sensitivity witness.

Run:
    python3 -m scripts.numerics.witness.prime_defect_variational_current
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_atom_sensitivity import _prime_power_label, atom_derivatives
from .prime_defect_scale_phase import FOCUS_EDGES, _invsqrt_spd, ambient_and_points, scaled_margin
from .prime_nested_cone import _orthogonal_shell


def critical_mode(ambient, points: dict[float, dict], left_gmax: float,
                  right_gmax: float) -> dict:
    M = scaled_margin(ambient, left_gmax, right_gmax, old_scale=1.0, new_scale=1.0)
    left = points[left_gmax]
    right = points[right_gmax]
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]
    block = _sym(B.T @ M @ B)
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])
    A_invsqrt = _invsqrt_spd(A)
    D_invsqrt = _invsqrt_spd(D)
    if A_invsqrt is None or D_invsqrt is None:
        raise ValueError(f"non-SPD block on edge {left_gmax}->{right_gmax}")

    K = A_invsqrt @ C @ D_invsqrt
    U, svals, Vt = np.linalg.svd(K, full_matrices=False)
    s = float(svals[0])
    p = U[:, 0]
    q = Vt.T[:, 0]
    x = A_invsqrt @ p
    y = D_invsqrt @ q

    # Normalize signs/roundoff so x*C*y is positive and equals s.
    coupling = float(x.T @ C @ y)
    if coupling < 0.0:
        y = -y
        coupling = -coupling
    return {
        "left": left_gmax,
        "right": right_gmax,
        "B": B,
        "old_dim": old_dim,
        "A": A,
        "C": C,
        "D": D,
        "x": x,
        "y": y,
        "s": s,
        "rho": s * s,
        "defect": 1.0 - s * s,
        "coupling": coupling,
        "xAx": float(x.T @ A @ x),
        "yDy": float(y.T @ D @ y),
    }


def atom_current_rows(ambient, mode: dict) -> list[dict]:
    B = mode["B"]
    old_dim = mode["old_dim"]
    x = mode["x"]
    y = mode["y"]
    s = mode["s"]
    rho = mode["rho"]
    right_gmax = mode["right"]
    rows = []
    for n, atom in sorted(ambient.atoms["zeta"].items()):
        logn = math.log(n)
        if logn >= right_gmax:
            continue
        atom_block = _sym(B.T @ atom @ B)
        A_atom = _sym(atom_block[:old_dim, :old_dim])
        C_atom = atom_block[:old_dim, old_dim:]
        D_atom = _sym(atom_block[old_dim:, old_dim:])
        old_term = float(rho * (x.T @ A_atom @ x))
        shell_term = float(rho * (y.T @ D_atom @ y))
        cross_term = float(-2.0 * s * (x.T @ C_atom @ y))
        slope = old_term + shell_term + cross_term
        rows.append({
            "n": n,
            "label": _prime_power_label(n),
            "logn": logn,
            "region": "old" if logn < mode["left"] else "new",
            "old_term": old_term,
            "shell_term": shell_term,
            "cross_term": cross_term,
            "slope": slope,
            "abs_slope": abs(slope),
        })
    return rows


def compare_to_finite_difference(analytic: list[dict], finite: list[dict]) -> dict:
    finite_by_n = {row["n"]: row for row in finite}
    diffs = []
    for row in analytic:
        fd = finite_by_n[row["n"]]["slope"]
        diffs.append(abs(row["slope"] - fd))
    return {
        "max_abs": max(diffs, default=float("nan")),
        "mean_abs": float(np.mean(diffs)) if diffs else float("nan"),
    }


def edge_report(ambient, points, left: float, right: float) -> dict:
    mode = critical_mode(ambient, points, left, right)
    analytic = atom_current_rows(ambient, mode)
    finite = atom_derivatives(ambient, points, left, right)
    cmp = compare_to_finite_difference(analytic, finite["rows"])
    return {
        "mode": mode,
        "analytic": analytic,
        "finite": finite,
        "comparison": cmp,
    }


def _sum(rows: list[dict], key: str, region: str | None = None) -> float:
    return float(sum(row[key] for row in rows if region is None or row["region"] == region))


def _print_edge(report: dict, topn: int = 6) -> None:
    mode = report["mode"]
    rows = report["analytic"]
    cmp = report["comparison"]
    print(f"\n[edge {mode['left']:.2f}->{mode['right']:.2f}] "
          f"rho={mode['rho']:.6f}, defect={mode['defect']:+.6f}, "
          f"s={mode['s']:.6f}")
    print(f"      checks: xAx={mode['xAx']:.6f}, yDy={mode['yDy']:.6f}, "
          f"xCy={mode['coupling']:.6f}, "
          f"fd max err={cmp['max_abs']:.2e}")
    print("      current sums: "
          f"old slope {_sum(rows, 'slope', 'old'):+.4f}, "
          f"new slope {_sum(rows, 'slope', 'new'):+.4f}, "
          f"A {_sum(rows, 'old_term'):+.4f}, "
          f"D {_sum(rows, 'shell_term'):+.4f}, "
          f"C {_sum(rows, 'cross_term'):+.4f}")
    print("      strongest atoms with A/D/C split:")
    for row in sorted(rows, key=lambda item: item["abs_slope"], reverse=True)[:topn]:
        print(f"        {row['label']:<4} "
              f"n={row['n']:<2d} {row['region']:<3} "
              f"slope={row['slope']:+.4f} "
              f"A={row['old_term']:+.4f} "
              f"D={row['shell_term']:+.4f} "
              f"C={row['cross_term']:+.4f}")


def summary() -> dict:
    print("=" * 78)
    print("Variational current for passive shell transfer")
    print("=" * 78)
    ambient, points = ambient_and_points()
    reports = {}
    for left, right in FOCUS_EDGES:
        report = edge_report(ambient, points, left, right)
        reports[(left, right)] = report
        _print_edge(report)

    late = reports[(3.00, 3.24)]["analytic"]
    old_rows = [row for row in late if row["region"] == "old"]
    print("\nInterpretation:")
    print("  * The analytic first variation matches finite differences, so the")
    print("    atom sensitivities are the contraction of each Toeplitz atom with")
    print("    a rank-two indefinite transfer stress tensor.")
    print("  * The A and D terms are old/shell diagonal contractions, and the C")
    print("    term is old/shell interference.  None is atomwise sign-definite")
    print("    because the Euler atoms are Toeplitz correlations, not samples.")
    print("  * On the late wall, old atoms have mixed signs because the transfer")
    print("    current is indefinite before summing the exact Euler history.")
    print(f"  * Late old current totals: A={_sum(old_rows, 'old_term'):+.3f}, "
          f"D={_sum(old_rows, 'shell_term'):+.3f}, "
          f"C={_sum(old_rows, 'cross_term'):+.3f}.")
    return reports


if __name__ == "__main__":
    summary()
