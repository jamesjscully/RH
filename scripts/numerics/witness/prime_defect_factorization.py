"""Factorization diagnostics for the passive defect kernel.

The previous witness established the finite positive-kernel target

    Delta = I - K^* K >= 0,   K = A^{-1/2} C D^{-1/2}.

This script asks what kind of object Delta looks like:

  * low-rank boundary increment?
  * outward-support moment?
  * Euler/prime-atom distributed kernel?

For each shell, we diagonalize Delta in the D-normalized shell coordinates.
The weakest direction is compared with:

  * the outer support moment |u|;
  * the strongest individual prime-atom quadratic directions on the shell.

The result should guide the search for a noncircular analytic kernel.

Run:
    python3 -m scripts.numerics.witness.prime_defect_factorization
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _physical_shape, _sym
from .prime_nested_cone import _orthogonal_shell, margin_at
from .prime_shell_coupling_bound import REFINEMENTS, ambient_for, cached_point

_TRAP = np.trapezoid if hasattr(np, "trapezoid") else np.trapz

FOCUS_EDGES = (
    (1.72, 1.88),
    (1.88, 2.10),
    (2.30, 2.52),
    (2.76, 3.00),
    (3.00, 3.24),
)


def _invsqrt_spd(M: np.ndarray, tol: float = 1e-10) -> np.ndarray | None:
    if M.size == 0:
        return None
    eigs, vecs = np.linalg.eigh(_sym(M))
    scale = max(1.0, float(np.max(np.abs(eigs))))
    if eigs[0] <= tol * scale:
        return None
    return vecs @ np.diag(1.0 / np.sqrt(eigs)) @ vecs.T


def _moment_matrix(ambient, shell: np.ndarray, D_invsqrt: np.ndarray,
                   power: int = 1) -> np.ndarray:
    umax = ambient.centers.max() + ambient.half_width
    u = np.linspace(-umax, umax, 8001)
    shapes = np.column_stack([
        _physical_shape(ambient.centers, ambient.half_width, shell[:, j], u)
        for j in range(shell.shape[1])
    ])
    weight = np.abs(u) ** power
    M = np.zeros((shell.shape[1], shell.shape[1]))
    for i in range(shell.shape[1]):
        for j in range(i, shell.shape[1]):
            M[i, j] = M[j, i] = float(_TRAP(weight * shapes[:, i] * shapes[:, j], x=u))
    return _sym(D_invsqrt @ M @ D_invsqrt)


def _feature_alignment(target: np.ndarray, feature_matrix: np.ndarray) -> tuple[float, float]:
    """Alignment of target with the dominant feature eigenvector by absolute eigenvalue."""
    if feature_matrix.size == 0:
        return float("nan"), float("nan")
    eigs, vecs = np.linalg.eigh(_sym(feature_matrix))
    idx = int(np.argmax(np.abs(eigs)))
    return float(abs(target @ vecs[:, idx])), float(eigs[idx])


def _atom_alignments(ambient, kind: str, right_gmax: float, shell: np.ndarray,
                     D_invsqrt: np.ndarray, target: np.ndarray,
                     limit: int = 5) -> list[dict]:
    rows = []
    for n, atom in ambient.atoms[kind].items():
        if math.log(n) >= right_gmax:
            continue
        matrix = _sym(D_invsqrt @ (shell.T @ atom @ shell) @ D_invsqrt)
        align, eig = _feature_alignment(target, matrix)
        ray = float(target.T @ matrix @ target)
        rows.append({
            "n": n,
            "align": align,
            "feature_eig": eig,
            "target_ray": ray,
        })
    rows.sort(key=lambda row: abs(row["target_ray"]), reverse=True)
    return rows[:limit]


def factor_row(kind: str, ncenters: int, half_width: float,
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
    new_ns = sorted(set(right["active_ns"]) - set(left["active_ns"]))
    A_min = float(np.linalg.eigvalsh(A)[0]) if A.size else float("nan")
    D_min = float(np.linalg.eigvalsh(D)[0]) if D.size else float("nan")

    if A_invsqrt is None or D_invsqrt is None:
        return {
            "kind": kind,
            "basis": f"n{ncenters}/hw{half_width:.2f}",
            "left_gmax": left_gmax,
            "right_gmax": right_gmax,
            "new_ns": new_ns,
            "valid": False,
            "shell_dim": int(shell.shape[1]),
            "A_min": A_min,
            "D_min": D_min,
        }

    K = A_invsqrt @ C @ D_invsqrt
    defect = _sym(np.eye(K.shape[1]) - K.T @ K)
    eigs, vecs = np.linalg.eigh(defect)
    weakest = vecs[:, 0]
    abs_moment = _moment_matrix(ambient, shell, D_invsqrt, power=1)
    sq_moment = _moment_matrix(ambient, shell, D_invsqrt, power=2)
    abs_align, abs_eig = _feature_alignment(weakest, abs_moment)
    sq_align, sq_eig = _feature_alignment(weakest, sq_moment)
    eff_rank = float((np.sum(eigs) ** 2) / np.sum(eigs ** 2)) if np.sum(eigs ** 2) > 0 else float("nan")
    atoms = _atom_alignments(ambient, kind, right_gmax, shell, D_invsqrt, weakest)
    return {
        "kind": kind,
        "basis": f"n{ncenters}/hw{half_width:.2f}",
        "left_gmax": left_gmax,
        "right_gmax": right_gmax,
        "new_ns": new_ns,
        "valid": True,
        "shell_dim": int(shell.shape[1]),
        "A_min": A_min,
        "D_min": D_min,
        "defect_eigs": eigs,
        "defect_min": float(eigs[0]),
        "defect_trace": float(np.sum(eigs)),
        "effective_rank": eff_rank,
        "rho": float(1.0 - eigs[0]),
        "abs_moment_align": abs_align,
        "abs_moment_eig": abs_eig,
        "sq_moment_align": sq_align,
        "sq_moment_eig": sq_eig,
        "atoms": atoms,
    }


def all_rows(kind: str) -> list[dict]:
    return [
        factor_row(kind, ncenters, half_width, left, right)
        for ncenters, half_width in REFINEMENTS
        for left, right in FOCUS_EDGES
    ]


def _new_n_text(row: dict) -> str:
    return ",".join(str(n) for n in row["new_ns"]) or "none"


def _atom_text(row: dict) -> str:
    if not row.get("valid"):
        return "n/a"
    return ",".join(
        f"n{a['n']}:{a['target_ray']:+.2e}/al{a['align']:.2f}"
        for a in row["atoms"][:3]
    )


def _print_rows(rows: list[dict], label: str) -> None:
    print(f"\n[1] Defect factor diagnostics for {label}")
    print("      edge        basis       new n       dim  dmin    effrank  |u|al  u2al   top atom rays/alignment")
    for row in rows:
        if not row.get("valid"):
            print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
                  f"{row['basis']:<10}  "
                  f"{_new_n_text(row):<10} "
                  f"{row['shell_dim']:2d}   invalid A/D "
                  f"Amin={row['A_min']:+.2e} Dmin={row['D_min']:+.2e}")
            continue
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['basis']:<10}  "
              f"{_new_n_text(row):<10} "
              f"{row['shell_dim']:2d}   "
              f"{row['defect_min']:+.3f}  "
              f"{row['effective_rank']:.2f}    "
              f"{row['abs_moment_align']:.2f}   "
              f"{row['sq_moment_align']:.2f}   "
              f"{_atom_text(row)}")


def _print_summary(rows: list[dict]) -> None:
    print("\n[2] Feature-alignment summary")
    print("      kind   valid rows  avg |u| align  avg u2 align  avg best atom align")
    for kind in ("zeta", "DH"):
        group = [row for row in rows if row["kind"] == kind and row.get("valid")]
        if not group:
            continue
        atom_aligns = []
        for row in group:
            if row["atoms"]:
                atom_aligns.append(max(atom["align"] for atom in row["atoms"]))
        print(f"      {kind:<5}  "
              f"{len(group):2d}          "
              f"{np.mean([row['abs_moment_align'] for row in group]):.3f}         "
              f"{np.mean([row['sq_moment_align'] for row in group]):.3f}        "
              f"{np.mean(atom_aligns):.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Factorization diagnostics for the passive defect kernel")
    print("=" * 78)

    zeta_rows = all_rows("zeta")
    dh_rows = all_rows("DH")
    _print_rows(zeta_rows, "zeta")
    _print_rows(dh_rows, "DH")
    _print_summary(zeta_rows + dh_rows)

    print("\nInterpretation:")
    print("  * Delta is not just a boundary evaluation form: moment alignments vary.")
    print("  * Prime-atom feature directions often align more strongly with the weakest")
    print("    defect mode, so the positive kernel must encode Euler Toeplitz structure.")
    print("  * The likely proof object is a distributed de Branges/canonical kernel,")
    print("    not a rank-one boundary correction.")

    return {
        "zeta_rows": zeta_rows,
        "DH_rows": dh_rows,
    }


if __name__ == "__main__":
    summary()
