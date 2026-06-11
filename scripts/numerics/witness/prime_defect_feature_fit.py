"""Feature-cone fits for the passive defect kernel.

The defect factorization witness suggests that

    Delta = I - K^* K

is distributed and Euler-sensitive.  This script asks a sharper finite
question: can Delta be fitted by a small cone of simple positive feature
kernels?

Feature families:

  moments:
      I, |u|-moment Gram, u^2-moment Gram

  Euler atoms:
      positive and negative spectral parts of D-normalized prime-atom
      compressions on the shell

  combined:
      moments + Euler atom parts

The fit is nonnegative least squares in Frobenius norm.  A small residual for
moments would support a boundary/moment mechanism.  A much smaller residual
only after Euler atom features means the kernel must encode Euler-Toeplitz
interference.

Run:
    python3 -m scripts.numerics.witness.prime_defect_feature_fit
"""
from __future__ import annotations

import math

import numpy as np
from scipy.optimize import nnls

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


def _vec_sym(M: np.ndarray) -> np.ndarray:
    """Vectorize a symmetric matrix preserving Frobenius norm."""
    out = []
    for i in range(M.shape[0]):
        for j in range(i, M.shape[1]):
            val = M[i, j] * (math.sqrt(2.0) if i != j else 1.0)
            out.append(val)
    return np.array(out)


def _moment_feature(ambient, shell: np.ndarray, D_invsqrt: np.ndarray,
                    power: int) -> np.ndarray:
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


def _atom_parts(ambient, kind: str, right_gmax: float, shell: np.ndarray,
                D_invsqrt: np.ndarray) -> list[tuple[str, np.ndarray]]:
    rows = []
    for n, atom in ambient.atoms[kind].items():
        if math.log(n) >= right_gmax:
            continue
        B = _sym(D_invsqrt @ (shell.T @ atom @ shell) @ D_invsqrt)
        eigs, vecs = np.linalg.eigh(B)
        pos = np.zeros_like(B)
        neg = np.zeros_like(B)
        for eig, vec in zip(eigs, vecs.T):
            outer = np.outer(vec, vec)
            if eig > 1e-12:
                pos += eig * outer
            elif eig < -1e-12:
                neg += -eig * outer
        if np.linalg.norm(pos) > 1e-12:
            rows.append((f"n{n}+", _sym(pos)))
        if np.linalg.norm(neg) > 1e-12:
            rows.append((f"n{n}-", _sym(neg)))
    return rows


def _fit(target: np.ndarray, features: list[tuple[str, np.ndarray]]) -> dict:
    if not features:
        return {"rel": float("nan"), "abs": float("nan"), "top": []}
    b = _vec_sym(target)
    A = np.column_stack([_vec_sym(M) for _, M in features])
    coeffs, abs_resid = nnls(A, b, maxiter=10_000)
    fit_vec = A @ coeffs
    abs_err = float(np.linalg.norm(b - fit_vec))
    rel_err = abs_err / max(1e-12, float(np.linalg.norm(b)))
    top = sorted(
        [(name, float(coeff), float(coeff * np.linalg.norm(_vec_sym(M))))
         for coeff, (name, M) in zip(coeffs, features)
         if coeff > 1e-10],
        key=lambda item: item[2],
        reverse=True,
    )[:5]
    return {"rel": rel_err, "abs": abs_err, "top": top}


def fit_row(kind: str, ncenters: int, half_width: float,
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
    if A_invsqrt is None or D_invsqrt is None:
        return {
            "kind": kind,
            "basis": f"n{ncenters}/hw{half_width:.2f}",
            "left_gmax": left_gmax,
            "right_gmax": right_gmax,
            "new_ns": new_ns,
            "valid": False,
            "shell_dim": int(shell.shape[1]),
            "A_min": float(np.linalg.eigvalsh(A)[0]) if A.size else float("nan"),
            "D_min": float(np.linalg.eigvalsh(D)[0]) if D.size else float("nan"),
        }
    K = A_invsqrt @ C @ D_invsqrt
    delta = _sym(np.eye(K.shape[1]) - K.T @ K)
    moment_features = [
        ("I", np.eye(delta.shape[0])),
        ("|u|", _moment_feature(ambient, shell, D_invsqrt, 1)),
        ("u2", _moment_feature(ambient, shell, D_invsqrt, 2)),
    ]
    atom_features = _atom_parts(ambient, kind, right_gmax, shell, D_invsqrt)
    combined = moment_features + atom_features
    return {
        "kind": kind,
        "basis": f"n{ncenters}/hw{half_width:.2f}",
        "left_gmax": left_gmax,
        "right_gmax": right_gmax,
        "new_ns": new_ns,
        "valid": True,
        "shell_dim": int(shell.shape[1]),
        "delta_min": float(np.linalg.eigvalsh(delta)[0]),
        "delta_trace": float(np.trace(delta)),
        "rho": float(1.0 - np.linalg.eigvalsh(delta)[0]),
        "moment_fit": _fit(delta, moment_features),
        "atom_fit": _fit(delta, atom_features),
        "combined_fit": _fit(delta, combined),
        "n_atom_features": len(atom_features),
    }


def all_rows(kind: str) -> list[dict]:
    return [
        fit_row(kind, ncenters, half_width, left, right)
        for ncenters, half_width in REFINEMENTS
        for left, right in FOCUS_EDGES
    ]


def _new_n_text(row: dict) -> str:
    return ",".join(str(n) for n in row["new_ns"]) or "none"


def _top_text(fit: dict) -> str:
    if not fit["top"]:
        return "none"
    return ",".join(f"{name}:{coef:.2g}" for name, coef, _ in fit["top"][:3])


def _print_rows(rows: list[dict], label: str) -> None:
    print(f"\n[1] Feature-cone fits for {label}")
    print("      edge        basis       new n       dim dmin    moment  atom    combined   top combined")
    for row in rows:
        if not row.get("valid"):
            print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
                  f"{row['basis']:<10}  "
                  f"{_new_n_text(row):<10} "
                  f"{row['shell_dim']:2d} invalid A/D "
                  f"Amin={row['A_min']:+.2e} Dmin={row['D_min']:+.2e}")
            continue
        print(f"      {row['left_gmax']:.2f}->{row['right_gmax']:.2f}  "
              f"{row['basis']:<10}  "
              f"{_new_n_text(row):<10} "
              f"{row['shell_dim']:2d}  "
              f"{row['delta_min']:+.3f}  "
              f"{row['moment_fit']['rel']:.3f}   "
              f"{row['atom_fit']['rel']:.3f}   "
              f"{row['combined_fit']['rel']:.3f}     "
              f"{_top_text(row['combined_fit'])}")


def _print_summary(rows: list[dict]) -> None:
    print("\n[2] Fit residual summary")
    print("      kind   rows  avg moment  avg atom  avg combined  max combined")
    for kind in ("zeta", "DH"):
        group = [row for row in rows if row["kind"] == kind and row.get("valid")]
        if not group:
            continue
        print(f"      {kind:<5}  "
              f"{len(group):2d}    "
              f"{np.mean([row['moment_fit']['rel'] for row in group]):.3f}      "
              f"{np.mean([row['atom_fit']['rel'] for row in group]):.3f}    "
              f"{np.mean([row['combined_fit']['rel'] for row in group]):.3f}        "
              f"{max(row['combined_fit']['rel'] for row in group):.3f}")


def summary() -> dict:
    print("=" * 78)
    print("Feature-cone fits for the passive defect kernel")
    print("=" * 78)
    zeta_rows = all_rows("zeta")
    dh_rows = all_rows("DH")
    _print_rows(zeta_rows, "zeta")
    _print_rows(dh_rows, "DH")
    _print_summary(zeta_rows + dh_rows)

    print("\nInterpretation:")
    print("  * Moment kernels alone sometimes fit the one-dimensional shells trivially,")
    print("    but they do not give a stable explanation on higher-dimensional shells.")
    print("  * Euler atom features sharply reduce the residual on most zeta shells,")
    print("    supporting the distributed Euler-Toeplitz kernel reading.")
    print("  * The finite fits are diagnostic only: a proof needs an intrinsic positive")
    print("    kernel construction, not an NNLS decomposition per shell.")
    return {
        "zeta_rows": zeta_rows,
        "DH_rows": dh_rows,
    }


if __name__ == "__main__":
    summary()
