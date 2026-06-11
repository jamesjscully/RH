"""Nested finite-cone witness for the Prime-Toeplitz target.

The moving-window witnesses rebuild the basis at each support edge.  This
script fixes one ambient raised-cosine basis and forms nested pole-killed
subspaces by selecting only bumps whose convolution support stays inside a
target edge L:

    c + hw <= L / 2.

Thus H_L is literally a subspace of H_{L'} for L < L'.  This lets us test the
positive-cone extension problem directly.  In an L2-orthonormal decomposition

    H_{L'} = H_L  +  shell,

we inspect the Schur complement of the new shell block.  Positive Schur
complements mean the larger finite form is a positive extension of the smaller
one; a negative complement locates where the cone extension fails.

Run:
    python3 -m scripts.numerics.witness.prime_nested_cone
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from .prime_carleson_flow import (
    _gram_orthonormalize,
    _physical_gram,
    _sym,
    _toeplitz_atom,
    coefficient_table,
)
from .semilocal_2 import build_gram


@dataclass(frozen=True)
class Ambient:
    centers: np.ndarray
    half_width: float
    gram: dict
    l2: np.ndarray
    atoms: dict[str, dict[int, np.ndarray]]


def build_ambient(ncenters: int = 25, half_width: float = 0.06,
                  cmax: float = 1.56, max_gmax: float = 3.24,
                  physical_ngrid: int = 6001) -> Ambient:
    centers = np.linspace(0.02, cmax, ncenters)
    gram = build_gram(centers, half_width)
    l2 = _physical_gram(type("Config", (), {
        "centers": centers,
        "half_width": half_width,
        "cmax": cmax,
    })(), ngrid=physical_ngrid)

    max_n = max(2, int(math.floor(math.exp(max_gmax) - 1e-12)))
    atoms: dict[str, dict[int, np.ndarray]] = {}
    for kind in ("zeta", "DH"):
        coeffs = coefficient_table(kind, max_n)
        kind_atoms = {}
        for n in range(2, max_n + 1):
            coeff = coeffs[n - 1]
            if abs(coeff) < 1e-12:
                continue
            logn = math.log(n)
            if logn >= max_gmax:
                continue
            weight = 2.0 * coeff / math.sqrt(n)
            kind_atoms[n] = _toeplitz_atom(centers, half_width, logn, weight)
        atoms[kind] = kind_atoms
    return Ambient(centers=centers, half_width=half_width, gram=gram, l2=l2, atoms=atoms)


def margin_at(ambient: Ambient, kind: str, gmax: float) -> np.ndarray:
    margin = ambient.gram["Winf"].copy()
    for n, atom in ambient.atoms[kind].items():
        if math.log(n) < gmax:
            margin = margin - atom
    return _sym(margin)


def selected_indices(ambient: Ambient, gmax: float) -> np.ndarray:
    return np.flatnonzero(ambient.centers + ambient.half_width <= gmax / 2.0 + 1e-12)


def nested_basis(ambient: Ambient, gmax: float) -> np.ndarray:
    idx = selected_indices(ambient, gmax)
    if len(idx) <= 2:
        return np.zeros((len(ambient.centers), 0))
    constraints = np.vstack([
        ambient.gram["v0"][idx],
        ambient.gram["vih"][idx],
    ])
    _, _, vt = np.linalg.svd(constraints)
    null_sel = vt[2:].T
    embed = np.zeros((len(ambient.centers), len(idx)))
    embed[idx, np.arange(len(idx))] = 1.0
    return _gram_orthonormalize(embed @ null_sel, ambient.l2)


def point(ambient: Ambient, kind: str, gmax: float) -> dict:
    Q = nested_basis(ambient, gmax)
    M = margin_at(ambient, kind, gmax)
    J = _sym(Q.T @ M @ Q)
    eigs = np.linalg.eigvalsh(J) if J.size else np.array([float("nan")])
    active = [n for n in ambient.atoms[kind] if math.log(n) < gmax]
    return {
        "kind": kind,
        "gmax": gmax,
        "indices": selected_indices(ambient, gmax),
        "basis": Q,
        "margin": M,
        "metric": J,
        "eigs": eigs,
        "dimension": int(Q.shape[1]),
        "active_ns": active,
    }


def _orthogonal_shell(ambient: Ambient, left_basis: np.ndarray, right_basis: np.ndarray) -> np.ndarray:
    if left_basis.shape[1] == 0:
        return right_basis
    projection_coeffs = left_basis.T @ ambient.l2 @ right_basis
    residual = right_basis - left_basis @ projection_coeffs
    return _gram_orthonormalize(residual, ambient.l2)


def extension_rows(ambient: Ambient, points: list[dict]) -> list[dict]:
    rows = []
    for left, right in zip(points, points[1:]):
        Ql = left["basis"]
        Qr = right["basis"]
        if Ql.shape[1] == 0 or Qr.shape[1] == 0:
            continue
        T = Qr.T @ ambient.l2 @ Ql
        svals = np.linalg.svd(T, compute_uv=False)
        shell = _orthogonal_shell(ambient, Ql, Qr)
        B = np.column_stack([Ql, shell]) if shell.shape[1] else Ql
        block = _sym(B.T @ right["margin"] @ B)
        old_dim = Ql.shape[1]
        old_block = _sym(block[:old_dim, :old_dim])
        old_eigs = np.linalg.eigvalsh(old_block)
        shell_block = block[old_dim:, old_dim:] if shell.shape[1] else np.zeros((0, 0))
        cross = block[:old_dim, old_dim:] if shell.shape[1] else np.zeros((old_dim, 0))
        if shell.shape[1] and old_eigs[0] > 1e-10:
            coupling = _sym(cross.T @ np.linalg.solve(old_block, cross))
            schur = _sym(shell_block - coupling)
            schur_eigs = np.linalg.eigvalsh(schur)
            coupling_eigs = np.linalg.eigvalsh(coupling)
            shell_eigs = np.linalg.eigvalsh(_sym(shell_block))
        elif shell.shape[1]:
            schur_eigs = np.array([float("nan")])
            coupling_eigs = np.array([float("nan")])
            shell_eigs = np.linalg.eigvalsh(_sym(shell_block))
        else:
            schur_eigs = np.array([float("nan")])
            coupling_eigs = np.array([float("nan")])
            shell_eigs = np.array([float("nan")])
        carry = _sym(Ql.T @ (right["margin"] - left["margin"]) @ Ql)
        carry_eigs = np.linalg.eigvalsh(carry)
        new_ns = sorted(set(right["active_ns"]) - set(left["active_ns"]))
        rows.append({
            "kind": left["kind"],
            "left_gmax": left["gmax"],
            "right_gmax": right["gmax"],
            "left_dim": left["dimension"],
            "right_dim": right["dimension"],
            "shell_dim": int(shell.shape[1]),
            "left_min": float(left["eigs"][0]),
            "right_min": float(right["eigs"][0]),
            "old_block_min": float(old_eigs[0]),
            "shell_min": float(shell_eigs[0]),
            "schur_min": float(schur_eigs[0]),
            "coupling_max": float(coupling_eigs[-1]),
            "carry_norm": float(np.linalg.norm(carry, ord=2)),
            "carry_min": float(carry_eigs[0]),
            "sval_min": float(svals[-1]),
            "sval_max": float(svals[0]),
            "new_ns": new_ns,
        })
    return rows


def _print_points(points: list[dict], label: str) -> None:
    print(f"\n[{label}] nested full-cone points in one ambient basis")
    print("      gmax   dim  active n       J eig range")
    for row in points:
        active = ",".join(str(n) for n in row["active_ns"]) or "none"
        print(f"      {row['gmax']:.2f}   "
              f"{row['dimension']:2d}   "
              f"{active:<14} "
              f"[{row['eigs'][0]:+.2e},{row['eigs'][-1]:+.2e}]")


def _print_extensions(rows: list[dict], label: str) -> None:
    print(f"\n[{label}] nested positive-cone extension")
    print("      edge        dim     new n       right min   shell min   coupling    Schur min   carry ||.||")
    for row in rows:
        new_ns = ",".join(str(n) for n in row["new_ns"]) or "none"
        schur = row["schur_min"]
        schur_text = "nan" if not np.isfinite(schur) else f"{schur:+.2e}"
        coupling = row["coupling_max"]
        coupling_text = "nan" if not np.isfinite(coupling) else f"{coupling:+.2e}"
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['left_dim']:2d}->{row['right_dim']:<2d}  "
              f"{new_ns:<10} "
              f"{row['right_min']:+.2e}   "
              f"{row['shell_min']:+.2e}   "
              f"{coupling_text:>9}   "
              f"{schur_text:>9}   "
              f"{row['carry_norm']:.1e}")
    print("      carry is the old-subspace change from newly active atoms; it should be")
    print("      numerically tiny because old test functions have smaller support.")


def summary() -> dict:
    print("=" * 78)
    print("Nested finite positive-cone witness in one ambient window")
    print("=" * 78)
    ambient = build_ambient()
    print(f"ambient: ncenters={len(ambient.centers)}, hw={ambient.half_width:.3f}, "
          f"gmax={ambient.gram['gmax']:.3f}")

    gmaxs = (1.60, 1.72, 1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24)
    zeta_points = [point(ambient, "zeta", gmax) for gmax in gmaxs]
    dh_points = [point(ambient, "DH", gmax) for gmax in gmaxs]
    _print_points(zeta_points, "zeta")
    _print_points(dh_points, "DH")

    zeta_ext = extension_rows(ambient, zeta_points)
    dh_ext = extension_rows(ambient, dh_points)
    _print_extensions(zeta_ext, "zeta")
    _print_extensions(dh_ext, "DH")

    print("\nInterpretation:")
    print("  * In one fixed ambient basis, zeta stays positive on each nested full")
    print("    pole-killed window; DH exits the cone at the same first bad edge.")
    print("  * Since old subspaces are included in new ones, positivity is an extension")
    print("    problem.  The Schur complement is the finite shell obstruction.")
    print("  * This is closer to the theorem than the moving-window determinant tests:")
    print("    prove every Euler/Sonin support extension has a positive Schur complement.")

    return {
        "zeta_points": zeta_points,
        "DH_points": dh_points,
        "zeta_extensions": zeta_ext,
        "DH_extensions": dh_ext,
    }


if __name__ == "__main__":
    summary()
