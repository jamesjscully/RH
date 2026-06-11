"""Extremal modes for the passive shell-coupling bound.

The contraction witness computes

    rho = || A^{-1/2} C D^{-1/2} ||^2.

This script reconstructs the shell vector that attains the largest singular
value.  It reports the corresponding old-space response and the prime atoms
which contribute most to the shell Rayleigh value.

This is diagnostic: it tells us what a noncircular proof of the passive
coupling bound must control.

Run:
    python3 -m scripts.numerics.witness.prime_shell_coupling_modes
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _physical_shape, _sym
from .prime_nested_cone import _orthogonal_shell, margin_at
from .prime_shell_coupling_bound import FOCUS_EDGES, REFINEMENTS, ambient_for, cached_point

_TRAP = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


def _invsqrt_spd(M: np.ndarray, tol: float = 1e-10) -> np.ndarray | None:
    if M.size == 0:
        return None
    eigs, vecs = np.linalg.eigh(_sym(M))
    scale = max(1.0, float(np.max(np.abs(eigs))))
    if eigs[0] <= tol * scale:
        return None
    return vecs @ np.diag(1.0 / np.sqrt(eigs)) @ vecs.T


def _shape_stats(ambient, coeffs: np.ndarray) -> dict:
    umax = ambient.centers.max() + ambient.half_width
    u = np.linspace(-umax, umax, 7001)
    shape = _physical_shape(ambient.centers, ambient.half_width, coeffs, u)
    energy = float(_TRAP(shape * shape, x=u))
    if energy <= 0.0:
        return {"l2": 0.0, "centroid": float("nan"), "peak": 0.0, "shape": shape, "u": u}
    centroid = float(_TRAP(np.abs(u) * shape * shape, x=u) / energy)
    peak = float(np.max(np.abs(shape)))
    return {
        "l2": math.sqrt(energy),
        "centroid": centroid,
        "peak": peak,
        "shape": shape,
        "u": u,
    }


def _grid_corr(left: dict, right: dict) -> float:
    u = left["u"]
    # The compared rows use the same support edge but not necessarily the same
    # ambient grid.  Interpolate the right shape to the left grid.
    rshape = np.interp(u, right["u"], right["shape"], left=0.0, right=0.0)
    inner = float(_TRAP(left["shape"] * rshape, x=u))
    denom = left["l2"] * math.sqrt(max(0.0, float(_TRAP(rshape * rshape, x=u))))
    return abs(inner) / denom if denom > 0 else float("nan")


def _top_atom_rays(ambient, kind: str, right_gmax: float, coeffs: np.ndarray,
                   limit: int = 4) -> list[tuple[int, float]]:
    rows = []
    for n, atom in ambient.atoms[kind].items():
        if math.log(n) >= right_gmax:
            continue
        rows.append((n, float(coeffs.T @ atom @ coeffs)))
    rows.sort(key=lambda item: abs(item[1]), reverse=True)
    return rows[:limit]


def mode_row(kind: str, ncenters: int, half_width: float,
             left_gmax: float, right_gmax: float) -> dict:
    ambient = ambient_for(ncenters, half_width)
    left = cached_point(ambient, kind, left_gmax)
    right = cached_point(ambient, kind, right_gmax)
    shell = _orthogonal_shell(ambient, left["basis"], right["basis"])
    B = np.column_stack([left["basis"], shell])
    old_dim = left["basis"].shape[1]
    M = margin_at(ambient, kind, right_gmax)
    block = _sym(B.T @ M @ B)
    A = _sym(block[:old_dim, :old_dim])
    C = block[:old_dim, old_dim:]
    D = _sym(block[old_dim:, old_dim:])

    A_invsqrt = _invsqrt_spd(A)
    D_invsqrt = _invsqrt_spd(D)
    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    D_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])
    new_ns = sorted(set(right["active_ns"]) - set(left["active_ns"]))

    if A_invsqrt is None or D_invsqrt is None:
        return {
            "kind": kind,
            "basis": f"n{ncenters}/hw{half_width:.2f}",
            "left_gmax": left_gmax,
            "right_gmax": right_gmax,
            "new_ns": new_ns,
            "valid": False,
            "A_min": float(A_eigs[0]),
            "D_min": float(D_eigs[0]),
        }

    K = A_invsqrt @ C @ D_invsqrt
    U, svals, Vt = np.linalg.svd(K, full_matrices=False)
    rho = float(svals[0] ** 2)
    shell_coords = D_invsqrt @ Vt.T[:, 0]
    old_coords = -np.linalg.solve(A, C @ shell_coords)
    shell_coeffs = shell @ shell_coords
    old_coeffs = left["basis"] @ old_coords
    combined_coeffs = old_coeffs + shell_coeffs

    shell_energy = float(shell_coords.T @ D @ shell_coords)
    old_energy = float(old_coords.T @ A @ old_coords)
    total_energy = float(combined_coeffs.T @ M @ combined_coeffs)
    winf_shell = float(shell_coeffs.T @ ambient.gram["Winf"] @ shell_coeffs)
    prime_shell = winf_shell - shell_energy
    shell_stats = _shape_stats(ambient, shell_coeffs)
    old_stats = _shape_stats(ambient, old_coeffs)
    combined_stats = _shape_stats(ambient, combined_coeffs)

    return {
        "kind": kind,
        "basis": f"n{ncenters}/hw{half_width:.2f}",
        "left_gmax": left_gmax,
        "right_gmax": right_gmax,
        "new_ns": new_ns,
        "valid": True,
        "A_min": float(A_eigs[0]),
        "D_min": float(D_eigs[0]),
        "rho": rho,
        "gain": float(svals[0]),
        "slack": float(1.0 - rho),
        "shell_energy": shell_energy,
        "old_energy": old_energy,
        "total_energy": total_energy,
        "winf_shell": winf_shell,
        "prime_shell": prime_shell,
        "top_atoms": _top_atom_rays(ambient, kind, right_gmax, shell_coeffs),
        "shell_stats": shell_stats,
        "old_stats": old_stats,
        "combined_stats": combined_stats,
    }


def all_rows(kind: str) -> list[dict]:
    rows = []
    for ncenters, half_width in REFINEMENTS:
        for left, right in FOCUS_EDGES:
            rows.append(mode_row(kind, ncenters, half_width, left, right))
    return rows


def _atom_text(row: dict) -> str:
    if not row.get("valid"):
        return "n/a"
    return ",".join(f"n{n}:{val:+.2e}" for n, val in row["top_atoms"])


def _new_n_text(row: dict) -> str:
    return ",".join(str(n) for n in row["new_ns"]) or "none"


def _print_modes(rows: list[dict], label: str) -> None:
    print(f"\n[1] Extremal coupling modes for {label}")
    print("      edge        basis       new n       rho    slack    |u|shell |u|old  shell(W-P)      top shell atom rays")
    for row in rows:
        if not row.get("valid"):
            print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
                  f"{row['basis']:<10}  "
                  f"{_new_n_text(row):<10} invalid A/D  "
                  f"Amin={row['A_min']:+.2e} Dmin={row['D_min']:+.2e}")
            continue
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['basis']:<10}  "
              f"{_new_n_text(row):<10} "
              f"{row['rho']:.3f}  "
              f"{row['slack']:+.2e}  "
              f"{row['shell_stats']['centroid']:.3f}   "
              f"{row['old_stats']['centroid']:.3f}  "
              f"{row['winf_shell']:+.2e}-{row['prime_shell']:+.2e}  "
              f"{_atom_text(row)}")
    print("      shell(W-P) reports the extremal shell vector with D-energy normalized to 1.")


def _print_coherence(rows: list[dict], label: str) -> None:
    print(f"\n[2] Extremal shell-mode coherence across refinements for {label}")
    print("      edge        pair                    rho pair       shell corr   old-response corr")
    for left, right in zip(rows, rows[1:]):
        if (
            left["left_gmax"] != right["left_gmax"]
            or left["right_gmax"] != right["right_gmax"]
            or not left.get("valid")
            or not right.get("valid")
        ):
            continue
        shell_corr = _grid_corr(left["shell_stats"], right["shell_stats"])
        old_corr = _grid_corr(left["old_stats"], right["old_stats"])
        print(f"      {left['left_gmax']:.2f}->{left['right_gmax']:.2f}  "
              f"{left['basis']}->{right['basis']:<10}  "
              f"{left['rho']:.3f}/{right['rho']:.3f}   "
              f"{shell_corr:.3f}        "
              f"{old_corr:.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Extremal modes for passive shell-coupling")
    print("=" * 78)

    zeta_rows = all_rows("zeta")
    dh_rows = all_rows("DH")
    _print_modes(zeta_rows, "zeta")
    _print_modes(dh_rows, "DH")

    # Sort by edge first for coherence comparisons.
    zeta_sorted = sorted(zeta_rows, key=lambda r: (r["left_gmax"], r["right_gmax"], r["basis"]))
    dh_sorted = sorted(dh_rows, key=lambda r: (r["left_gmax"], r["right_gmax"], r["basis"]))
    _print_coherence(zeta_sorted, "zeta")
    _print_coherence(dh_sorted, "DH")

    print("\nInterpretation:")
    print("  * Zeta's near-critical modes are genuine passive transfer modes: D-energy")
    print("    is normalized to one and the old response has A-energy rho < 1.")
    print("  * DH's failing modes have rho > 1 before A ceases to be positive; after")
    print("    that point the contraction formulation correctly becomes invalid.")
    print("  * The proof target is to bound these transfer modes uniformly, likely via")
    print("    a canonical-system/de Branges kernel rather than determinant topology.")

    return {
        "zeta_rows": zeta_rows,
        "DH_rows": dh_rows,
    }


if __name__ == "__main__":
    summary()
