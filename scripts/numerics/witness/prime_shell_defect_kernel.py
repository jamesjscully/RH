"""Defect-kernel witness for the passive shell-coupling target.

For a nested support extension, set

    K = A^{-1/2} C D^{-1/2}.

The passive shell-coupling theorem is ||K|| <= 1, equivalently

    Delta := I - K^* K >= 0.

In canonical-system / de Branges language, Delta is the finite kernel defect
that should be produced by a positive Hamiltonian increment.  This script
prints the full defect spectrum on each shell, not just the largest coupling
ratio.

Run:
    python3 -m scripts.numerics.witness.prime_shell_defect_kernel
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _physical_shape, _sym
from .prime_nested_cone import _orthogonal_shell, margin_at
from .prime_shell_coupling_bound import GMAXS, REFINEMENTS, ambient_for, cached_point

_TRAP = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


def _invsqrt_spd(M: np.ndarray, tol: float = 1e-10) -> np.ndarray | None:
    if M.size == 0:
        return None
    eigs, vecs = np.linalg.eigh(_sym(M))
    scale = max(1.0, float(np.max(np.abs(eigs))))
    if eigs[0] <= tol * scale:
        return None
    return vecs @ np.diag(1.0 / np.sqrt(eigs)) @ vecs.T


def defect_row(kind: str, ncenters: int, half_width: float,
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
    A_eigs = np.linalg.eigvalsh(A) if A.size else np.array([float("nan")])
    D_eigs = np.linalg.eigvalsh(D) if D.size else np.array([float("nan")])
    A_invsqrt = _invsqrt_spd(A)
    D_invsqrt = _invsqrt_spd(D)
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
            "shell_dim": int(shell.shape[1]),
        }

    K = A_invsqrt @ C @ D_invsqrt
    svals = np.linalg.svd(K, compute_uv=False)
    defect = _sym(np.eye(K.shape[1]) - K.T @ K)
    defect_eigs, defect_vecs = np.linalg.eigh(defect)
    worst_shell = shell @ (D_invsqrt @ defect_vecs[:, 0])
    stats = _shape_stats(ambient, worst_shell)
    top_atoms = _top_atom_rays(ambient, kind, right_gmax, worst_shell)
    return {
        "kind": kind,
        "basis": f"n{ncenters}/hw{half_width:.2f}",
        "left_gmax": left_gmax,
        "right_gmax": right_gmax,
        "new_ns": new_ns,
        "valid": True,
        "A_min": float(A_eigs[0]),
        "D_min": float(D_eigs[0]),
        "D_max": float(D_eigs[-1]),
        "shell_dim": int(shell.shape[1]),
        "svals": svals,
        "rho": float(svals[0] ** 2) if len(svals) else float("nan"),
        "defect_eigs": defect_eigs,
        "defect_min": float(defect_eigs[0]),
        "defect_trace": float(np.trace(defect)),
        "defect_det": float(np.prod(defect_eigs)),
        "worst_centroid": stats["centroid"],
        "worst_peak": stats["peak"],
        "top_atoms": top_atoms,
    }


def _shape_stats(ambient, coeffs: np.ndarray) -> dict:
    umax = ambient.centers.max() + ambient.half_width
    u = np.linspace(-umax, umax, 7001)
    shape = _physical_shape(ambient.centers, ambient.half_width, coeffs, u)
    energy = float(_TRAP(shape * shape, x=u))
    if energy <= 0.0:
        return {"centroid": float("nan"), "peak": 0.0}
    return {
        "centroid": float(_TRAP(np.abs(u) * shape * shape, x=u) / energy),
        "peak": float(np.max(np.abs(shape))),
    }


def _top_atom_rays(ambient, kind: str, right_gmax: float, coeffs: np.ndarray,
                   limit: int = 3) -> list[tuple[int, float]]:
    rows = []
    for n, atom in ambient.atoms[kind].items():
        if math.log(n) >= right_gmax:
            continue
        rows.append((n, float(coeffs.T @ atom @ coeffs)))
    rows.sort(key=lambda item: abs(item[1]), reverse=True)
    return rows[:limit]


def all_rows(kind: str) -> list[dict]:
    rows = []
    for ncenters, half_width in REFINEMENTS:
        for left, right in zip(GMAXS, GMAXS[1:]):
            rows.append(defect_row(kind, ncenters, half_width, left, right))
    return rows


def _new_n_text(row: dict) -> str:
    return ",".join(str(n) for n in row["new_ns"]) or "none"


def _spectrum_text(values: np.ndarray, limit: int = 4) -> str:
    if values.size == 0:
        return "[]"
    shown = ",".join(f"{v:.3f}" for v in values[:limit])
    return f"[{shown}{',...' if len(values) > limit else ''}]"


def _atom_text(row: dict) -> str:
    if not row.get("valid"):
        return "n/a"
    return ",".join(f"n{n}:{val:+.1e}" for n, val in row["top_atoms"])


def _print_path(rows: list[dict], label: str) -> None:
    print(f"\n[1] Defect spectra for {label}")
    print("      edge        basis       new n       shell  rho    defect eigs       trace   worst |u|  top atoms")
    for row in rows:
        if not row.get("valid"):
            print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
                  f"{row['basis']:<10}  "
                  f"{_new_n_text(row):<10} "
                  f"{row['shell_dim']:2d}     invalid A/D "
                  f"Amin={row['A_min']:+.2e} Dmin={row['D_min']:+.2e}")
            continue
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['basis']:<10}  "
              f"{_new_n_text(row):<10} "
              f"{row['shell_dim']:2d}     "
              f"{row['rho']:.3f}  "
              f"{_spectrum_text(row['defect_eigs'])}  "
              f"{row['defect_trace']:+.3f}   "
              f"{row['worst_centroid']:.3f}    "
              f"{_atom_text(row)}")


def _print_summary(rows: list[dict]) -> None:
    print("\n[2] Positive-kernel summary")
    print("      kind   basis       min defect   edge          trace at edge   rho")
    for kind in ("zeta", "DH"):
        for ncenters, half_width in REFINEMENTS:
            basis = f"n{ncenters}/hw{half_width:.2f}"
            group = [row for row in rows if row["kind"] == kind and row["basis"] == basis and row.get("valid")]
            if not group:
                continue
            worst = min(group, key=lambda row: row["defect_min"])
            print(f"      {kind:<5}  "
                  f"{basis:<10}  "
                  f"{worst['defect_min']:+.3f}      "
                  f"{worst['left_gmax']:.2f}->{worst['right_gmax']:.2f}  "
                  f"{worst['defect_trace']:+.3f}        "
                  f"{worst['rho']:.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Defect kernel for passive shell-coupling")
    print("=" * 78)

    zeta_rows = all_rows("zeta")
    dh_rows = all_rows("DH")
    _print_path(zeta_rows, "zeta")
    _print_path(dh_rows, "DH")
    _print_summary(zeta_rows + dh_rows)

    print("\nInterpretation:")
    print("  * Delta = I - K*K is the finite positive kernel increment we want.")
    print("  * Zeta's Delta remains PSD but develops small eigenvalues near late")
    print("    support extensions; DH's Delta becomes negative at the failing shell.")
    print("  * A proof should construct Delta directly as a positive kernel/Hamiltonian")
    print("    increment along the Sonin support chain.")

    return {
        "zeta_rows": zeta_rows,
        "DH_rows": dh_rows,
    }


if __name__ == "__main__":
    summary()
