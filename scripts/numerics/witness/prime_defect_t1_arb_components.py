"""Arb prototypes for certified T1 matrix components.

This script starts with the easiest rigorous components: compact physical
Toeplitz atom entries and selected smooth-cell entries.  For the even
raised-cosine basis,

    T_U(i,j) = int phi_i(v) phi_j(v-U) dv

has compact support and can be split into finitely many analytic overlap
integrals.  Arb's ``acb.integral`` then gives an enclosure without any Fourier
grid or tail estimate.

This is not yet the full T1 certificate.  It is a component check showing that
the exact atom blocks can be certified independently of the current
trapezoidal Fourier implementation.

Run:
    python3 -m scripts.numerics.witness.prime_defect_t1_arb_components
"""
from __future__ import annotations

import math

import numpy as np
from flint import acb, arb, ctx

from .prime_carleson_flow import _sym, _toeplitz_atom
from .prime_defect_active_atom_shift import REPAIR_N, _compressed_atom_block, active_state
from .prime_defect_active_debt_current import LATE_EDGE, context_for_basis
from .prime_defect_measure_surrogate import smooth_prime_operator
from .prime_defect_residual_control import edge_basis, smooth_cell_operator
from .prime_defect_riccati_storage import _blocks, exact_old_operator


def _overlap_integral(si: float, sj: float, hw: float, U: float) -> acb:
    lo = max(si - hw, U + sj - hw)
    hi = min(si + hw, U + sj + hw)
    if hi <= lo:
        return acb(0)
    si_b = arb(si)
    sj_b = arb(sj)
    hw_b = arb(hw)
    U_b = arb(U)
    scale = arb.pi() / (2 * hw_b)

    def integrand(x, analytic):
        a = scale * (x - si_b)
        b = scale * (x - U_b - sj_b)
        return (a.cos() ** 2) * (b.cos() ** 2)

    return acb.integral(
        integrand,
        arb(lo),
        arb(hi),
        rel_tol=arb("1e-40"),
        abs_tol=arb("1e-40"),
    )


def arb_atom_entry(ci: float, cj: float, hw: float, U: float) -> acb:
    out = acb(0)
    for si in (ci, -ci):
        for sj in (cj, -cj):
            out += _overlap_integral(si, sj, hw, U)
    return out


def arb_atom_matrix(centers: np.ndarray, hw: float, U: float) -> np.ndarray:
    n = len(centers)
    out = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i, n):
            val = float(arb_atom_entry(float(centers[i]), float(centers[j]), hw, U).real.mid())
            out[i, j] = out[j, i] = val
    return out


def _signed_pair_smooth(si: float, sj: float, hw: float,
                        lo: float, hi: float) -> acb:
    d = si - sj
    start = d - 2.0 * hw
    stop = d + 2.0 * hw
    a = max(lo, start)
    b = min(hi, stop)
    if b <= a:
        return acb(0)

    si_b = arb(si)
    sj_b = arb(sj)
    hw_b = arb(hw)
    scale = arb.pi() / (2 * hw_b)

    def inner_for_u(U, side: str):
        if side == "left":
            vlo = si_b - hw_b
            vhi = U + sj_b + hw_b
        else:
            vlo = U + sj_b - hw_b
            vhi = si_b + hw_b

        def inner(v, analytic):
            aa = scale * (v - si_b)
            bb = scale * (v - U - sj_b)
            return (aa.cos() ** 2) * (bb.cos() ** 2)

        return acb.integral(
            inner,
            vlo,
            vhi,
            rel_tol=arb("1e-30"),
            abs_tol=arb("1e-30"),
        )

    def outer(side: str):
        def integrand(U, analytic):
            return 2 * (U / 2).exp() * inner_for_u(U, side)

        return integrand

    out = acb(0)
    if a < min(d, b):
        out += acb.integral(
            outer("left"),
            arb(a),
            arb(min(d, b)),
            rel_tol=arb("1e-25"),
            abs_tol=arb("1e-25"),
        )
    if max(a, d) < b:
        out += acb.integral(
            outer("right"),
            arb(max(a, d)),
            arb(b),
            rel_tol=arb("1e-25"),
            abs_tol=arb("1e-25"),
        )
    return out


def arb_smooth_entry(ci: float, cj: float, hw: float, lo: float, hi: float) -> acb:
    out = acb(0)
    for si in (ci, -ci):
        for sj in (cj, -cj):
            out += _signed_pair_smooth(si, sj, hw, lo, hi)
    return out


def arb_smooth_matrix(centers: np.ndarray, hw: float, lo: float, hi: float) -> np.ndarray:
    n = len(centers)
    out = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i, n):
            val = float(arb_smooth_entry(
                float(centers[i]),
                float(centers[j]),
                hw,
                lo,
                hi,
            ).real.mid())
            out[i, j] = out[j, i] = val
    return out


def _float_mid(x: arb) -> float:
    return float(x.mid())


def _float_rad(x: arb) -> float:
    return float(x.rad())


def selected_atom_checks() -> list[dict]:
    ctx.prec = 140
    ambient, _ = context_for_basis(
        ncenters=25,
        half_width=0.06,
        left=LATE_EDGE[0],
        right=LATE_EDGE[1],
    )
    U = math.log(REPAIR_N)
    grid_atom = _toeplitz_atom(ambient.centers, ambient.half_width, U, 1.0)
    # Most entries are exactly zero for U=log(23); the nonzero overlap is
    # concentrated where center_i + center_j is close to U.
    indices = [0, 4, 10, 18, 19, 20, 21, 22, 23, 24]
    rows = []
    for i in indices:
        for j in indices:
            if j < i:
                continue
            ball = arb_atom_entry(
                float(ambient.centers[i]),
                float(ambient.centers[j]),
                float(ambient.half_width),
                U,
            ).real
            ref = float(grid_atom[i, j])
            lo = float(ball.lower())
            hi = float(ball.upper())
            rows.append({
                "i": i,
                "j": j,
                "center_i": float(ambient.centers[i]),
                "center_j": float(ambient.centers[j]),
                "arb_mid": _float_mid(ball),
                "arb_rad": _float_rad(ball),
                "grid": ref,
                "grid_minus_mid": ref - _float_mid(ball),
                "grid_in_ball": bool(lo <= ref <= hi),
            })
    return rows


def selected_smooth_checks(state: dict, lo: float, hi: float, label: str) -> list[dict]:
    ctx.prec = 120
    ambient = state["ambient"]
    grid_smooth = smooth_cell_operator(ambient, lo, hi)
    indices = [21, 22, 23, 24]
    rows = []
    for i in indices:
        for j in indices:
            if j < i:
                continue
            ball = arb_smooth_entry(
                float(ambient.centers[i]),
                float(ambient.centers[j]),
                float(ambient.half_width),
                lo,
                hi,
            ).real
            ref = float(grid_smooth[i, j])
            rows.append({
                "i": i,
                "j": j,
                "label": label,
                "arb_mid": _float_mid(ball),
                "arb_rad": _float_rad(ball),
                "grid": ref,
                "grid_minus_mid": ref - _float_mid(ball),
            })
    return rows


def full_atom_comparison() -> dict:
    ctx.prec = 140
    from .prime_defect_active_atom_shift import active_state
    from .prime_defect_default_t1_certificate import t1_matrices

    state = active_state()
    ambient = state["ambient"]
    U = state["logn"]
    exact_unit_atom = arb_atom_matrix(ambient.centers, ambient.half_width, U)
    grid_unit_atom = _toeplitz_atom(ambient.centers, ambient.half_width, U, 1.0)
    ambient_diff = grid_unit_atom - exact_unit_atom
    exact_zero = np.abs(exact_unit_atom) < 1e-15
    max_zero_noise = float(np.max(np.abs(np.where(exact_zero, ambient_diff, 0.0))))

    B = state["B"]
    compressed_exact = B.T @ exact_unit_atom @ B
    from .prime_defect_active_atom_shift import _compressed_atom_block

    compressed_grid = _compressed_atom_block(state, U, 1.0)
    compressed_delta = compressed_grid - compressed_exact

    exact_weight = 2.0 * U / math.sqrt(REPAIR_N)
    cell_exact_atom = state["smooth_block"] - exact_weight * compressed_exact
    post_exact_atom = state["current"] + cell_exact_atom
    A, C, D = _blocks(post_exact_atom, state["old_dim"])
    H_exact_atom = D - C.T @ np.linalg.solve(A, C)

    default = t1_matrices()
    return {
        "exact_unit_atom": exact_unit_atom,
        "grid_unit_atom": grid_unit_atom,
        "ambient_max_abs_diff": float(np.max(np.abs(ambient_diff))),
        "ambient_max_zero_noise": max_zero_noise,
        "compressed_max_abs_diff": float(np.max(np.abs(compressed_delta))),
        "compressed_op_norm_diff": float(np.linalg.norm(compressed_delta, ord=2)),
        "state_atom_weight": state["atom_weight"],
        "exact_weight": exact_weight,
        "weight_delta": state["atom_weight"] - exact_weight,
        "H_exact_atom": H_exact_atom,
        "H_default": default["H"],
        "H_delta": H_exact_atom - default["H"],
        "eig_H_exact_atom": np.linalg.eigvalsh(H_exact_atom),
        "eig_H_default": np.linalg.eigvalsh(default["H"]),
    }


def direct_component_comparison() -> dict:
    state = active_state()
    ambient = state["ambient"]
    B = state["B"]
    old_dim = state["old_dim"]
    suffix_lo = state["cell"][1]
    suffix_hi = state["right"]
    exact_weight = 2.0 * state["logn"] / math.sqrt(REPAIR_N)

    atom_exact = arb_atom_matrix(ambient.centers, ambient.half_width, state["logn"])
    suffix_exact = arb_smooth_matrix(ambient.centers, ambient.half_width, suffix_lo, suffix_hi)
    suffix_grid = smooth_prime_operator(ambient, suffix_hi) - smooth_prime_operator(ambient, suffix_lo)
    old_grid = exact_old_operator(ambient, state["left"], "zeta")

    direct_grid = _sym(
        B.T @ (ambient.gram["Winf"] - old_grid - suffix_grid) @ B
        - state["atom_weight"] * _compressed_atom_block(state, state["logn"], 1.0)
    )
    direct_exact_components = _sym(
        B.T @ (ambient.gram["Winf"] - old_grid - suffix_exact) @ B
        - exact_weight * (B.T @ atom_exact @ B)
    )

    def schur(block):
        A, C, D = _blocks(block, old_dim)
        return _sym(D - C.T @ np.linalg.solve(A, C))

    H_grid = schur(direct_grid)
    H_exact_components = schur(direct_exact_components)
    suffix_delta = suffix_grid - suffix_exact
    block_delta = direct_grid - direct_exact_components
    return {
        "suffix_ambient_max_diff": float(np.max(np.abs(suffix_delta))),
        "suffix_compressed_op_diff": float(np.linalg.norm(B.T @ suffix_delta @ B, ord=2)),
        "post_block_op_diff": float(np.linalg.norm(block_delta, ord=2)),
        "eig_H_grid_direct": np.linalg.eigvalsh(H_grid),
        "eig_H_exact_components": np.linalg.eigvalsh(H_exact_components),
        "eig_H_shift": np.linalg.eigvalsh(H_exact_components) - np.linalg.eigvalsh(H_grid),
    }


def summary() -> dict:
    rows = selected_atom_checks()
    state = active_state()
    smooth_rows = selected_smooth_checks(state, state["cell"][0], state["cell"][1], "repair")
    suffix_rows = selected_smooth_checks(state, state["cell"][1], state["right"], "suffix")
    full = full_atom_comparison()
    direct_components = direct_component_comparison()
    print("=" * 78)
    print("Arb compact-overlap checks for T1 atom entries")
    print("=" * 78)
    print(f"atom n={REPAIR_N}, U=log(n)={math.log(REPAIR_N):.12f}")
    print("      i  j   center_i center_j   arb mid        rad        grid-mid    contains")
    for row in rows:
        print(f"      {row['i']:2d} {row['j']:2d}  "
              f"{row['center_i']:.6f} {row['center_j']:.6f}  "
              f"{row['arb_mid']:+.6e}  "
              f"{row['arb_rad']:.1e}  "
              f"{row['grid_minus_mid']:+.2e}    "
              f"{row['grid_in_ball']}")
    print("\nSelected Arb smooth-cell checks for the repair cell:")
    print("      i  j   arb mid        rad        Fourier-grid minus Arb")
    for row in smooth_rows:
        print(f"      {row['i']:2d} {row['j']:2d}  "
              f"{row['arb_mid']:+.6e}  "
              f"{row['arb_rad']:.1e}  "
              f"{row['grid_minus_mid']:+.2e}")
    print("\nSelected Arb smooth-cell checks for the post-cell suffix:")
    print("      i  j   arb mid        rad        Fourier-grid minus Arb")
    for row in suffix_rows:
        print(f"      {row['i']:2d} {row['j']:2d}  "
              f"{row['arb_mid']:+.6e}  "
              f"{row['arb_rad']:.1e}  "
              f"{row['grid_minus_mid']:+.2e}")
    max_abs_diff = max(abs(row["grid_minus_mid"]) for row in rows)
    max_rad = max(row["arb_rad"] for row in rows)
    max_smooth_diff = max(abs(row["grid_minus_mid"]) for row in smooth_rows)
    max_smooth_rad = max(row["arb_rad"] for row in smooth_rows)
    max_suffix_diff = max(abs(row["grid_minus_mid"]) for row in suffix_rows)
    max_suffix_rad = max(row["arb_rad"] for row in suffix_rows)
    eig_delta = full["eig_H_exact_atom"] - full["eig_H_default"]
    print("\nFull ambient/compressed atom comparison:")
    print(f"      ambient max |Fourier grid - Arb atom| = {full['ambient_max_abs_diff']:.3e}")
    print(f"      ambient max exact-zero grid noise     = {full['ambient_max_zero_noise']:.3e}")
    print(f"      compressed max entry diff             = {full['compressed_max_abs_diff']:.3e}")
    print(f"      compressed operator-norm diff         = {full['compressed_op_norm_diff']:.3e}")
    print(f"      state atom weight - exact weight      = {full['weight_delta']:+.3e}")
    print(f"      eig(H) default atom                   = "
          f"{full['eig_H_default'][0]:+.12e}, {full['eig_H_default'][1]:+.12e}")
    print(f"      eig(H) Arb-overlap atom               = "
          f"{full['eig_H_exact_atom'][0]:+.12e}, {full['eig_H_exact_atom'][1]:+.12e}")
    print(f"      eig(H) shift from atom replacement    = "
          f"{eig_delta[0]:+.3e}, {eig_delta[1]:+.3e}")
    print("\nDirect post-cell replacement of atom(23) and smooth suffix:")
    print(f"      suffix ambient max |Fourier grid - Arb| = "
          f"{direct_components['suffix_ambient_max_diff']:.3e}")
    print(f"      suffix compressed operator-norm diff    = "
          f"{direct_components['suffix_compressed_op_diff']:.3e}")
    print(f"      post block operator-norm diff           = "
          f"{direct_components['post_block_op_diff']:.3e}")
    print(f"      eig(H) grid direct                      = "
          f"{direct_components['eig_H_grid_direct'][0]:+.12e}, "
          f"{direct_components['eig_H_grid_direct'][1]:+.12e}")
    print(f"      eig(H) Arb atom+suffix                  = "
          f"{direct_components['eig_H_exact_components'][0]:+.12e}, "
          f"{direct_components['eig_H_exact_components'][1]:+.12e}")
    print(f"      eig(H) shift                            = "
          f"{direct_components['eig_H_shift'][0]:+.3e}, "
          f"{direct_components['eig_H_shift'][1]:+.3e}")
    print("\nInterpretation:")
    print(f"  max |Fourier-grid atom - Arb midpoint| on sampled entries = {max_abs_diff:.3e}")
    print(f"  max Arb radius on sampled entries = {max_rad:.3e}")
    print(f"  max |Fourier-grid smooth - Arb midpoint| on selected smooth entries = {max_smooth_diff:.3e}")
    print(f"  max Arb smooth radius on selected entries = {max_smooth_rad:.3e}")
    print(f"  max |Fourier-grid suffix - Arb midpoint| on selected suffix entries = {max_suffix_diff:.3e}")
    print(f"  max Arb suffix radius on selected entries = {max_suffix_rad:.3e}")
    print("  The Fourier grid values are not expected to lie inside the tiny Arb")
    print("  balls; the grid has its own truncation/discretization error. The point")
    print("  is that atom and smooth-cell entries can be certified by compact")
    print("  overlap integrals with negligible enclosure radius.")
    return {
        "rows": rows,
        "smooth_rows": smooth_rows,
        "suffix_rows": suffix_rows,
        "full": full,
        "direct_components": direct_components,
    }


if __name__ == "__main__":
    summary()
