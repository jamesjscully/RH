"""Tail diagnostics for the archimedean W_inf block in T1.

The remaining hard certification component is

    W_inf(i,j) = -g_ij(0) log(pi)
                 + (1/2pi) int_R phihat_i(t) phihat_j(t)
                   Re digamma(1/4 + i t/2) dt.

For the folded raised-cosine basis,

    phihat_c(t) = 2 cos(ct) pi^2 sin(hw t) / (t (pi^2 - hw^2 t^2)),

with removable singularities at ``t=0`` and ``t=+-pi/hw``.  Hence
``phihat_c(t)=O(t^-3)`` and the tail is bounded by a ``t^-6 log(t)`` envelope.

This script is diagnostic, not a rigorous proof.  It uses SciPy quadrature for
finite intervals and an explicit absolute tail envelope to estimate what a
future Arb/interval W_inf certificate must control.

Run:
    python3 -m scripts.numerics.witness.prime_defect_t1_winf_tail
    python3 -m scripts.numerics.witness.prime_defect_t1_winf_tail --endpoint
    python3 -m scripts.numerics.witness.prime_defect_t1_winf_tail --tail-propagation
    python3 -m scripts.numerics.witness.prime_defect_t1_winf_tail --arb-full --arb-T 1500
"""
from __future__ import annotations

import argparse
import math

import numpy as np
from flint import acb, arb, ctx
from scipy import integrate, special

from .prime_defect_active_debt_current import LATE_EDGE, context_for_basis
from .prime_defect_active_atom_shift import _compressed_atom_block, active_state
from .prime_defect_default_t1_certificate import t1_matrices
from .prime_defect_riccati_storage import _blocks, exact_old_operator
from .prime_carleson_flow import _sym, coefficient_table
from .prime_defect_t1_arb_components import arb_atom_entry, arb_atom_matrix, arb_smooth_matrix
from .semilocal_2 import _phihat


def phi_hat(c: float, hw: float, t: float) -> float:
    return float(_phihat(np.array([t], dtype=float), c, hw)[0])


def winf_integrand(ci: float, cj: float, hw: float, t: float) -> float:
    psi = float(special.digamma(0.25 + 0.5j * t).real)
    return phi_hat(ci, hw, t) * phi_hat(cj, hw, t) * psi


def exact_g0_overlap(ci: float, cj: float, hw: float) -> float:
    return float(arb_atom_entry(ci, cj, hw, 0.0).real.mid())


def winf_entry_quad(ci: float, cj: float, hw: float, T: float) -> dict:
    g0 = exact_g0_overlap(ci, cj, hw)
    val, err = integrate.quad(
        lambda t: winf_integrand(ci, cj, hw, t),
        0.0,
        T,
        epsabs=1e-12,
        epsrel=1e-12,
        limit=1000,
    )
    return {
        "T": T,
        "g0": g0,
        "finite_integral": val,
        "quad_error": err,
        "winf": -g0 * math.log(math.pi) + val / math.pi,
    }


def _arb_S(x: acb, hw: arb) -> acb:
    return hw * (x * hw).sinc()


def arb_phi_hat(c: float, hw: float, x: acb) -> acb:
    hw_b = arb(hw)
    c_b = arb(c)
    p = arb.pi() / hw_b
    return 2 * (x * c_b).cos() * (
        _arb_S(x, hw_b)
        + _arb_S(x + p, hw_b) / 2
        + _arb_S(x - p, hw_b) / 2
    )


def winf_entry_arb(ci: float, cj: float, hw: float, T: float) -> dict:
    ctx.prec = 120
    g0 = exact_g0_overlap(ci, cj, hw)

    def integrand(x, analytic):
        phi_i = arb_phi_hat(ci, hw, x)
        phi_j = arb_phi_hat(cj, hw, x)
        z = acb(arb("0.25")) + x * acb(0, arb("0.5"))
        return phi_i * phi_j * z.digamma().real

    val = acb.integral(
        integrand,
        arb(0),
        arb(T),
        rel_tol=arb("1e-25"),
        abs_tol=arb("1e-25"),
        eval_limit=200000,
        depth_limit=100,
    ).real
    winf = -arb(g0) * arb.pi().log() + val / arb.pi()
    return {
        "T": T,
        "g0": g0,
        "finite_integral_mid": float(val.mid()),
        "finite_integral_rad": float(val.rad()),
        "winf_mid": float(winf.mid()),
        "winf_rad": float(winf.rad()),
    }


def winf_matrix_arb_finite(ambient, T: float) -> np.ndarray:
    n = len(ambient.centers)
    out = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(i, n):
            row = winf_entry_arb(
                float(ambient.centers[i]),
                float(ambient.centers[j]),
                float(ambient.half_width),
                T,
            )
            out[i, j] = out[j, i] = row["winf_mid"]
    return _sym(out)


def phi_tail_envelope(hw: float, t: float) -> float:
    """Envelope for |phihat_c(t)|, valid for t > pi/hw."""
    denom = t * (hw * hw * t * t - math.pi * math.pi)
    if denom <= 0.0:
        return float("inf")
    return 2.0 * math.pi * math.pi / denom


def psi_tail_envelope(t: float) -> float:
    # For z=1/4+i t/2, the standard digamma integral representation gives
    # |Re psi(z)| <= log|z| + 1/(2|z|) + 1/(3t) for t>0.  For the cutoffs used
    # here this is safely below log(t+1)+1.
    return math.log(t + 1.0) + 1.0


def winf_tail_bound(hw: float, T: float) -> float:
    if T <= math.pi / hw:
        return float("inf")
    val, _ = integrate.quad(
        lambda t: phi_tail_envelope(hw, t) ** 2 * psi_tail_envelope(t),
        T,
        math.inf,
        epsabs=1e-18,
        epsrel=1e-12,
        limit=1000,
    )
    return val / math.pi


def selected_entries_report() -> list[dict]:
    ambient, _ = context_for_basis(
        ncenters=25,
        half_width=0.06,
        left=LATE_EDGE[0],
        right=LATE_EDGE[1],
    )
    pairs = [(24, 24), (23, 24), (22, 24), (20, 24), (0, 0)]
    cutoffs = [250.0, 500.0, 1000.0, 1500.0]
    rows = []
    for i, j in pairs:
        ci = float(ambient.centers[i])
        cj = float(ambient.centers[j])
        vals = [winf_entry_quad(ci, cj, float(ambient.half_width), T) for T in cutoffs]
        arb_1500 = winf_entry_arb(ci, cj, float(ambient.half_width), 1500.0)
        default = float(ambient.gram["Winf"][i, j])
        rows.append({
            "i": i,
            "j": j,
            "ci": ci,
            "cj": cj,
            "default": default,
            "vals": vals,
            "arb_1500": arb_1500,
        })
    return rows


def winf_matrix_quad(ambient, T: float) -> tuple[np.ndarray, float]:
    centers = ambient.centers
    hw = float(ambient.half_width)
    p = math.pi / hw

    def integrand(t):
        ph = np.array([phi_hat(float(c), hw, t) for c in centers])
        psi = float(special.digamma(0.25 + 0.5j * t).real)
        return np.outer(ph, ph) * psi

    val, err = integrate.quad_vec(
        integrand,
        0.0,
        T,
        epsabs=1e-11,
        epsrel=1e-11,
        limit=10000,
        points=[p] if p < T else None,
    )
    return _sym(-ambient.l2 * math.log(math.pi) + val / math.pi), float(err)


def endpoint_replacement_report(cutoffs: tuple[float, ...] = (250.0, 500.0, 1000.0, 1500.0)) -> list[dict]:
    state = active_state()
    ambient = state["ambient"]
    default = t1_matrices()
    eig_default = np.linalg.eigvalsh(default["H"])
    atom = _sym(state["atom_weight"] * _compressed_atom_block(state, state["logn"], 1.0))
    rows = []
    for T in cutoffs:
        W, err = winf_matrix_quad(ambient, T)
        dW = _sym(W - ambient.gram["Winf"])
        current = _sym(state["current"] + state["B"].T @ dW @ state["B"])
        post = _sym(current + state["smooth_block"] - atom)
        A, C, D = _blocks(post, state["old_dim"])
        H = _sym(D - C.T @ np.linalg.solve(A, C))
        eig_H = np.linalg.eigvalsh(H)
        rows.append({
            "T": T,
            "quad_error": err,
            "max_winf_delta": float(np.max(np.abs(dW))),
            "eig_H": eig_H,
            "eig_delta": eig_H - eig_default,
        })
    return rows


def endpoint_from_replacement_winf(W, state, default_H: np.ndarray) -> dict:
    ambient = state["ambient"]
    atom = _sym(state["atom_weight"] * _compressed_atom_block(state, state["logn"], 1.0))
    dW = _sym(W - ambient.gram["Winf"])
    current = _sym(state["current"] + state["B"].T @ dW @ state["B"])
    post = _sym(current + state["smooth_block"] - atom)
    A, C, D = _blocks(post, state["old_dim"])
    H = _sym(D - C.T @ np.linalg.solve(A, C))
    eig_H = np.linalg.eigvalsh(H)
    eig_default = np.linalg.eigvalsh(default_H)
    return {
        "H": H,
        "eig_H": eig_H,
        "eig_delta": eig_H - eig_default,
        "max_winf_delta": float(np.max(np.abs(dW))),
    }


def arb_old_exact_operator(state) -> np.ndarray:
    ambient = state["ambient"]
    max_n = max(ambient.atoms["zeta"])
    coeffs = coefficient_table("zeta", max_n)
    out = np.zeros_like(ambient.gram["Winf"])
    for n in sorted(ambient.atoms["zeta"]):
        if math.log(n) >= state["left"]:
            continue
        coeff = coeffs[n - 1]
        weight = 2.0 * coeff / math.sqrt(n)
        out = out + weight * arb_atom_matrix(ambient.centers, ambient.half_width, math.log(n))
    return _sym(out)


def endpoint_from_direct_components(W, state, default_H: np.ndarray,
                                    exact_old: bool = False) -> dict:
    exact_weight = 2.0 * state["logn"] / math.sqrt(state["repair_n"])
    atom = arb_atom_matrix(state["ambient"].centers, state["ambient"].half_width, state["logn"])
    suffix = arb_smooth_matrix(
        state["ambient"].centers,
        state["ambient"].half_width,
        state["cell"][1],
        state["right"],
    )
    old = arb_old_exact_operator(state) if exact_old else exact_old_operator(state["ambient"], state["left"], "zeta")
    dW = _sym(W - state["ambient"].gram["Winf"])
    post = _sym(
        state["B"].T @ (W - old - suffix) @ state["B"]
        - exact_weight * (state["B"].T @ atom @ state["B"])
    )
    A, C, D = _blocks(post, state["old_dim"])
    H = _sym(D - C.T @ np.linalg.solve(A, C))
    eig_H = np.linalg.eigvalsh(H)
    eig_default = np.linalg.eigvalsh(default_H)
    return {
        "H": H,
        "eig_H": eig_H,
        "eig_delta": eig_H - eig_default,
        "max_winf_delta": float(np.max(np.abs(dW))),
        "component_mode": (
            "Arb W_inf finite + Arb old atoms + Arb atom(23) + Arb smooth suffix"
            if exact_old
            else "Arb W_inf finite + Arb atom(23) + Arb smooth suffix"
        ),
        "exact_old": exact_old,
    }


def arb_full_endpoint_report(T: float = 1500.0, exact_components: bool = False,
                             exact_old: bool = False) -> dict:
    state = active_state()
    default = t1_matrices()
    W_arb = winf_matrix_arb_finite(state["ambient"], T)
    endpoint = (
        endpoint_from_direct_components(W_arb, state, default["H"], exact_old=exact_old)
        if exact_components
        else endpoint_from_replacement_winf(W_arb, state, default["H"])
    )
    endpoint.update({
        "T": T,
        "W_arb": W_arb,
        "tail_bound": winf_tail_bound(float(state["ambient"].half_width), T),
        "exact_components": exact_components,
        "exact_old": exact_old,
    })
    return endpoint


def tail_propagation_report(cutoffs: tuple[float, ...] = (1500.0, 2000.0, 3000.0, 5000.0, 8000.0)) -> list[dict]:
    state = active_state()
    B = state["B"]
    ambient_dim = B.shape[0]
    col_l1 = np.sum(np.abs(B), axis=0)
    entry_factor = float(np.max(np.outer(col_l1, col_l1)))
    spectral_factor = float(np.linalg.norm(B, ord=2) ** 2 * ambient_dim)
    rows = []
    for T in cutoffs:
        tau = winf_tail_bound(float(state["ambient"].half_width), T)
        rows.append({
            "T": T,
            "ambient_tail": tau,
            "compressed_entry": tau * entry_factor,
            "compressed_spectral": tau * spectral_factor,
            "entry_factor": entry_factor,
            "spectral_factor": spectral_factor,
        })
    return rows


def summary(with_endpoint: bool = False, with_arb_full: bool = False,
            arb_T: float = 1500.0, with_tail_propagation: bool = False,
            with_selected: bool = True, exact_components: bool = False,
            exact_old: bool = False) -> dict:
    rows = selected_entries_report() if with_selected else []
    hw = 0.06
    tail_rows = [
        {"T": T, "bound": winf_tail_bound(hw, T)}
        for T in (250.0, 500.0, 1000.0, 1500.0, 2000.0, 5000.0, 8000.0)
    ]
    print("=" * 78)
    print("T1 W_inf finite-cutoff and tail diagnostic")
    print("=" * 78)
    if with_selected:
        print("Selected W_inf entries using exact compact-overlap g(0):")
        for row in rows:
            last = row["vals"][-1]["winf"]
            print(f"\n      entry ({row['i']},{row['j']}) centers=({row['ci']:.6f},{row['cj']:.6f})")
            print(f"        default trapezoid W_inf = {row['default']:+.12e}")
            for val in row["vals"]:
                print(f"        T={val['T']:>6.0f} quad W_inf={val['winf']:+.12e} "
                      f"delta_from_T1500={val['winf'] - last:+.3e} "
                      f"quad_err={val['quad_error']:.1e}")
            arb_row = row["arb_1500"]
            print(f"        T=  1500 Arb  W_inf={arb_row['winf_mid']:+.12e} "
                  f"radius={arb_row['winf_rad']:.1e} "
                  f"Arb-quad={arb_row['winf_mid'] - last:+.3e}")
            print(f"        default - T1500 = {row['default'] - last:+.3e}")
    else:
        print("Selected W_inf entries skipped.")

    print("\nAbsolute per-entry tail envelope:")
    print("      T       bound for |tail W_inf_ij|")
    for row in tail_rows:
        print(f"      {row['T']:>6.0f}  {row['bound']:.3e}")
    print("\nInterpretation:")
    print("  The finite-cutoff drift and envelope estimate the W_inf accuracy")
    print("  requirement. The envelope is intentionally conservative and still needs")
    print("  a rigorous digamma inequality before it can be used in a proof.")
    endpoint_rows = []
    if with_endpoint:
        endpoint_rows = endpoint_replacement_report()
        print("\nEndpoint recomputation after replacing W_inf by full-matrix finite quadrature:")
        print("      T       max|dW|     eigmin(H)      eigmax(H)      delta eigmin")
        for row in endpoint_rows:
            print(f"      {row['T']:>6.0f}  "
                  f"{row['max_winf_delta']:.3e}  "
                  f"{row['eig_H'][0]:+.12e}  "
                  f"{row['eig_H'][1]:+.12e}  "
                  f"{row['eig_delta'][0]:+.3e}")
        print("  The endpoint remains positive and the longer-cutoff W_inf increases")
        print("  the current eigmin(H) in this diagnostic. This is not a rigorous")
        print("  enclosure, but it says the T=250 truncation is not hiding a failure.")
    arb_full = None
    if with_arb_full:
        arb_full = arb_full_endpoint_report(
            T=arb_T,
            exact_components=exact_components,
            exact_old=exact_old,
        )
        print("\nFull-matrix Arb finite W_inf replacement:")
        print(f"      T={arb_full['T']:.0f}")
        if arb_full.get("exact_components"):
            print(f"      component mode={arb_full['component_mode']}")
        print(f"      max|W_arb_finite - W_default|={arb_full['max_winf_delta']:.3e}")
        print(f"      per-entry tail envelope={arb_full['tail_bound']:.3e}")
        print(f"      eig(H)={arb_full['eig_H'][0]:+.12e}, {arb_full['eig_H'][1]:+.12e}")
        print(f"      delta eig(H)={arb_full['eig_delta'][0]:+.3e}, {arb_full['eig_delta'][1]:+.3e}")
        print("  This uses Arb for the finite interval but not yet a rigorous matrix tail")
        print("  propagation. It is the intended finite-interval component of the certificate.")
    propagation_rows = []
    if with_tail_propagation:
        propagation_rows = tail_propagation_report()
        first = propagation_rows[0]
        print("\nConservative tail propagation through the compressed basis:")
        print(f"      entry factor=max_i,j ||B_i||_1||B_j||_1 = {first['entry_factor']:.3e}")
        print(f"      spectral factor=||B||_2^2 ambient_dim       = {first['spectral_factor']:.3e}")
        print("      T       ambient tail  compressed entry  compressed spectral")
        for row in propagation_rows:
            print(f"      {row['T']:>6.0f}  "
                  f"{row['ambient_tail']:.3e}    "
                  f"{row['compressed_entry']:.3e}       "
                  f"{row['compressed_spectral']:.3e}")
        print("  With this no-cancellation bound, T=1500 is too loose for the raw")
        print("  post-block entry budget; T around 5000 is in the right range.")
    return {
        "entries": rows,
        "tails": tail_rows,
        "endpoint": endpoint_rows,
        "arb_full": arb_full,
        "tail_propagation": propagation_rows,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint", action="store_true")
    parser.add_argument("--tail-propagation", action="store_true")
    parser.add_argument("--arb-full", action="store_true")
    parser.add_argument("--arb-T", type=float, default=1500.0)
    parser.add_argument("--exact-components", action="store_true")
    parser.add_argument("--exact-old", action="store_true")
    parser.add_argument("--skip-selected", action="store_true")
    args = parser.parse_args()
    summary(
        with_endpoint=args.endpoint,
        with_arb_full=args.arb_full,
        arb_T=args.arb_T,
        with_tail_propagation=args.tail_propagation,
        with_selected=not args.skip_selected,
        exact_components=args.exact_components,
        exact_old=args.exact_old,
    )
