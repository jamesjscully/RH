"""Perturbation budget for the default T1 Schur endpoint.

The default T1 certificate can be targeted directly at the post-cell Schur
complement.  Let

    M_+ = M_current + E_23 = [A C; C' D],
    H   = D - C' A^{-1} C.

If rigorous construction gives interval enclosures for the entries of
``M_+``, this script estimates how small those enclosures must be to keep
``H`` positive definite by a conservative norm perturbation bound.

Run:
    python3 -m scripts.numerics.witness.prime_defect_t1_error_budget
"""
from __future__ import annotations

import math

import numpy as np

from .prime_carleson_flow import _sym
from .prime_defect_active_atom_shift import _compressed_atom_block, active_state
from .prime_defect_measure_surrogate import smooth_prime_operator
from .prime_defect_riccati_storage import _blocks, exact_old_operator


def post_cell_blocks() -> dict:
    state = active_state()
    old_dim = state["old_dim"]
    atom = _sym(state["atom_weight"] * _compressed_atom_block(state, state["logn"], 1.0))
    cell = _sym(state["smooth_block"] - atom)
    post = _sym(state["current"] + cell)
    suffix_smooth = _sym(
        smooth_prime_operator(state["ambient"], state["right"])
        - smooth_prime_operator(state["ambient"], state["cell"][1])
    )
    # Build the post-cell block directly:
    # W_inf - exact(<left) - smooth([cell_hi,right]) - atom(23).
    direct_compressed = _sym(
        state["B"].T
        @ (
            state["ambient"].gram["Winf"]
            - exact_old_operator(state["ambient"], state["left"], "zeta")
            - suffix_smooth
        )
        @ state["B"]
        - atom
    )
    A, C, D = _blocks(post, old_dim)
    H = _sym(D - C.T @ np.linalg.solve(A, C))
    return {
        "state": state,
        "post": post,
        "A": A,
        "C": C,
        "D": D,
        "H": H,
        "direct_post": direct_compressed,
        "direct_post_error": float(np.max(np.abs(post - direct_compressed))),
    }


def schur_error_bound(A: np.ndarray, C: np.ndarray,
                      eps_A: float, eps_C: float, eps_D: float) -> dict:
    """Bound ||delta H||_2 from block perturbation spectral-norm bounds.

    Assumes

        ||delta A||_2 <= eps_A,
        ||delta C||_2 <= eps_C,
        ||delta D||_2 <= eps_D,

    and ``A + delta A`` remains SPD.  The bound uses

        ||(A+dA)^-1|| <= ||A^-1|| / (1 - ||A^-1|| eps_A).
    """
    eig_A = np.linalg.eigvalsh(_sym(A))
    alpha = 1.0 / float(eig_A[0])
    rho = alpha * eps_A
    if rho >= 1.0:
        return {
            "valid": False,
            "bound": float("inf"),
            "rho": rho,
            "inv_A_norm": alpha,
            "inv_A_pert_norm": float("inf"),
        }
    inv_pert = alpha / (1.0 - rho)
    C_norm = float(np.linalg.norm(C, ord=2))
    inv_diff = alpha * inv_pert * eps_A
    bound = (
        eps_D
        + C_norm * C_norm * inv_diff
        + 2.0 * eps_C * inv_pert * C_norm
        + eps_C * eps_C * inv_pert
    )
    return {
        "valid": True,
        "bound": float(bound),
        "rho": float(rho),
        "A_min": float(eig_A[0]),
        "A_max": float(eig_A[-1]),
        "inv_A_norm": float(alpha),
        "inv_A_pert_norm": float(inv_pert),
        "C_norm": C_norm,
        "inv_diff_bound": float(inv_diff),
    }


def entrywise_to_spectral(old_dim: int, shell_dim: int, eta: float) -> tuple[float, float, float]:
    """Convert a uniform entrywise block error to spectral-norm block errors."""
    eps_A = old_dim * eta
    eps_C = math.sqrt(old_dim * shell_dim) * eta
    eps_D = shell_dim * eta
    return eps_A, eps_C, eps_D


def solve_uniform_entry_budget(A: np.ndarray, C: np.ndarray, H: np.ndarray,
                               safety: float = 0.5) -> dict:
    old_dim, shell_dim = C.shape
    h_min = float(np.linalg.eigvalsh(_sym(H))[0])
    target = safety * h_min
    lo = 0.0
    hi = 1e-3
    while True:
        eps_A, eps_C, eps_D = entrywise_to_spectral(old_dim, shell_dim, hi)
        row = schur_error_bound(A, C, eps_A, eps_C, eps_D)
        if (not row["valid"]) or row["bound"] >= target:
            break
        hi *= 2.0
        if hi > 1.0:
            break
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        eps_A, eps_C, eps_D = entrywise_to_spectral(old_dim, shell_dim, mid)
        row = schur_error_bound(A, C, eps_A, eps_C, eps_D)
        if row["valid"] and row["bound"] < target:
            lo = mid
        else:
            hi = mid
    eps_A, eps_C, eps_D = entrywise_to_spectral(old_dim, shell_dim, lo)
    final = schur_error_bound(A, C, eps_A, eps_C, eps_D)
    final.update({
        "entry_eta": float(lo),
        "target_delta_H": target,
        "h_min": h_min,
        "safety": safety,
        "eps_A": eps_A,
        "eps_C": eps_C,
        "eps_D": eps_D,
    })
    return final


def summary() -> dict:
    data = post_cell_blocks()
    A, C, D, H = data["A"], data["C"], data["D"], data["H"]
    eig_A = np.linalg.eigvalsh(A)
    eig_H = np.linalg.eigvalsh(H)
    budget_half = solve_uniform_entry_budget(A, C, H, safety=0.5)
    budget_ninety = solve_uniform_entry_budget(A, C, H, safety=0.9)
    print("=" * 78)
    print("Default T1 post-cell Schur perturbation budget")
    print("=" * 78)
    print(f"old_dim={A.shape[0]}, shell_dim={D.shape[0]}")
    print(f"direct post-cell composition error={data['direct_post_error']:.3e}")
    print(f"eig(A_+)=[{eig_A[0]:+.6e}, {eig_A[-1]:+.6e}], "
          f"cond(A_+)={eig_A[-1] / eig_A[0]:.3e}")
    print(f"||C_+||_2={np.linalg.norm(C, ord=2):.6e}")
    print(f"eig(H)=[{eig_H[0]:+.6e}, {eig_H[-1]:+.6e}], "
          f"det(H)={np.linalg.det(H):+.6e}")
    print("\nUniform post-block entrywise enclosure budget:")
    print("      safety   eta(entry)   epsA(spec)  epsC(spec)  epsD(spec)  bound||dH||")
    for row in (budget_half, budget_ninety):
        print(f"      {row['safety']:.1f}      "
              f"{row['entry_eta']:.3e}   "
              f"{row['eps_A']:.3e}   "
              f"{row['eps_C']:.3e}   "
              f"{row['eps_D']:.3e}   "
              f"{row['bound']:.3e}")
    print("\nInterpretation:")
    print("  If every entry of the post-cell block M_+ is enclosed within eta,")
    print("  then the displayed conservative bound keeps ||delta H|| below the")
    print("  chosen fraction of eigmin(H). This is a sufficient budget for the")
    print("  later rigorous quadrature/enclosure work, not a proof by itself.")
    return {
        "data": data,
        "budget_half": budget_half,
        "budget_ninety": budget_ninety,
    }


if __name__ == "__main__":
    summary()
