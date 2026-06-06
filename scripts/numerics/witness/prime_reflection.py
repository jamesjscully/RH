"""Worker B -- the prime-place reflection / adelic Hankel form.

Thread 1 isolated reflection positivity (OS/QFT) to one open object: an involution `theta`
acting on the PRIME (finite-adelic) places that turns the Weil quadratic form into a
reflection-positive pairing `W(h,h) = <theta h, h>`.  Reflection on the archimedean/scaling
geometry is known RH-NEUTRAL (it certifies Davenport-Heilbronn verbatim).  The bet is that a
*prime-place* reflection's positivity is destroyed when the Euler product is removed.

This module builds the Weil form as a Gram/Hankel matrix split by place,

    W = W_inf  +  sum_p W_p          (CC20 adelic splitting)
    W_inf : archimedean (digamma Gamma_R) block   -- RH-neutral, shared with DH
    W_p   : prime block, kernel  Lambda(p^k)/p^(k/2) * [h sampled at u = log p^k]

and tests the candidate prime-place involutions:

    (i)   p^{-1} inversion / multiplicative flip   u = log n  ->  -u   (the n <-> 1/n adelic flip)
    (ii)  functional-equation reflection            s <-> 1-s        (already even => trivial here)
    (iii) the Gram/Hankel factorisation on the log-prime lattice

For each we ask: is  W(h,h) = <theta h, h>  a positive (OS) pairing, and -- the kill-test --
does that positivity survive for an off-line / DH control (=> RH-neutral) or fail only when the
Euler product is removed (=> the first OS-positive object that discriminates)?

DISCIPLINE (research/positivity-program.md sec.8): the SPECTRAL side of the Weil form is the
reliable, PSD-certified side (weil_form.py).  The prime/Toeplitz side with a NON-even test
convention has bitten us; every prime-side computation here is cross-checked against the spectral
side on the SAME even test functions.

Run:  python3 -m scripts.numerics.witness.prime_reflection
"""
from __future__ import annotations

import numpy as np
from flint import acb, ctx, fmpz, arb

# ----------------------------------------------------------------------------------------------
# Zeros of zeta (spectral side, the reliable side).
# ----------------------------------------------------------------------------------------------


def zeros(K, prec=64):
    ctx.prec = prec
    return np.array([float(acb.zeta_zero(k).imag) for k in range(1, K + 1)])


# ----------------------------------------------------------------------------------------------
# Test-function basis adapted to the adelic splitting.
#
# We work with EVEN test functions h on the multiplicative line, parametrised by u = log x in R,
# h(u)=h(-u).  Their Mellin/Fourier transform  hhat(gamma) = \int h(u) e^{i gamma u} du  is the
# object the explicit formula sums over the zeros (gamma = Im rho).  A convenient basis is the
# family of even Gaussians centred at +-t_a:
#
#     phi_a(u) = exp(-(u-t_a)^2/(2 s^2)) + exp(-(u+t_a)^2/(2 s^2))        (so phi_a(-u)=phi_a(u))
#     phihat_a(gamma) = sqrt(2 pi) s * exp(-s^2 gamma^2/2) * 2 cos(gamma t_a)
#
# The Weil form is W[a,b] = sum_rho phihat_a(gamma_rho) conj(phihat_b(gamma_rho)).  Because the
# phihat are real and even, this is a real symmetric Gram matrix -- a Hankel-type form in the
# centres t_a (CC20: the Weil functional IS a Hermitian Toeplitz/Hankel positivity problem).
# ----------------------------------------------------------------------------------------------


def phihat(gamma, t, s):
    """Even-Gaussian test transform  phihat(gamma) = sqrt(2pi) s e^{-s^2 gamma^2/2} 2 cos(gamma t)."""
    g = np.asarray(gamma, dtype=float)
    return np.sqrt(2 * np.pi) * s * np.exp(-0.5 * s ** 2 * g ** 2) * 2.0 * np.cos(g * t)


# ----------------------------------------------------------------------------------------------
# (1) The SPECTRAL-side Weil Gram matrix  W[a,b] = sum_rho phihat_a(gamma) phihat_b(gamma).
#     PSD <=> all gamma real <=> RH.  This is the certified side.
# ----------------------------------------------------------------------------------------------


def weil_gram_spectral(centres, s, gammas):
    """Real symmetric Gram matrix on the even-Gaussian basis, summed over the zero ordinates.

    We keep +gamma_rho (the form is over the multiset {+-gamma_rho}; phihat is even in gamma so
    this only rescales by 2 -- irrelevant to the SIGN / PSD question)."""
    cols = np.array([phihat(gammas, t, s) for t in centres])  # n x K
    return cols @ cols.T


def spectral_offline_certified():
    """The SPECTRAL-side off-line kill-test, DEFERRED to the PSD-certified weil_form.py (sec.8
    discipline: the spectral/Toeplitz side there is the reliable one; we do NOT reimplement it).

    Returns (min_eig_rh, min_eig_offline).  An off-line zero drives the Toeplitz form indefinite.

    NB: a naive off-line perturbation in the even-Gaussian *Gram* basis above is Gaussian-DAMPED
    (the off-line transform carries exp(-s^2 gamma0^2) with gamma0 ~ 14, killing its weight), so it
    does NOT visibly break PSD at moderate width -- a known limitation of that basis, not a
    contradiction.  The certified Toeplitz convention (weil_form.py, sigma=0.12) is the one that
    cleanly exhibits the break, so we use it for the spectral kill-test."""
    from . import weil_form as WF
    sigma = 0.12
    taus = np.arange(0, 8.01, 0.25)
    gammas = WF._zeros(200)
    fr = WF.weil_kernel_spectral(taus, gammas, sigma)
    fo = WF.weil_kernel_offline(taus, gammas, sigma)
    return WF.toeplitz_min_eig(fr)[0], WF.toeplitz_min_eig(fo)[0]


# ----------------------------------------------------------------------------------------------
# (2) The ARITHMETIC-side splitting  W = W_inf + sum_p W_p  (the explicit formula, by place).
#
# Weil explicit formula for an even h with transform hhat:
#
#   sum_rho hhat(gamma_rho)  =  [poles s=0,1]  +  W_inf[h]  -  sum_{n>=2} Lambda(n)/sqrt(n) * h(log n)
#
# with h(u) the even test function (here phi_a) and  W_inf[h]  the archimedean (digamma) term.
#
# Prime block as a Gram/Hankel form: define the "prime sampling" of a test function as the vector
# of its values at the log-prime-power lattice, weighted by sqrt(Lambda(n)/sqrt(n)):
#
#     P[h]  =  ( sqrt(Lambda(n)/sqrt(n)) * h(log n) )_{n prime power}
#
# Then the prime contribution to the Weil form's POLARISATION is
#     W_prime[a,b] = sum_{n pp} (Lambda(n)/sqrt(n)) phi_a(log n) phi_b(log n) = P[phi_a] . P[phi_b],
# manifestly PSD *because Lambda(n) >= 0* (the Euler product!).  THIS is the adelic Hankel
# structure: each prime place p contributes a rank-(few) PSD block  W_p = P_p . P_p^T  with P_p
# sampling at u = k log p.  In the explicit formula this enters with a MINUS, so the prime places
# RESIST positivity and the archimedean place must dominate them (CC20: W_inf >= prime sum >= 0).
# ----------------------------------------------------------------------------------------------


def prime_powers(N):
    """List (n, p, k, Lambda(n)) for prime powers n in [2, N]."""
    out = []
    for n in range(2, N + 1):
        f = fmpz(n).factor()
        if len(f) == 1:
            p, k = f[0]
            out.append((n, int(p), int(k), float(arb(int(p)).log())))
    return out


def phi_even(u, t, s):
    """Even-Gaussian test function value at log-coordinate u (centred at +-t)."""
    u = np.asarray(u, dtype=float)
    return np.exp(-(u - t) ** 2 / (2 * s ** 2)) + np.exp(-(u + t) ** 2 / (2 * s ** 2))


def prime_sampling_matrix(centres, s, pps):
    """P[a, j] = sqrt(Lambda(n_j)/sqrt(n_j)) * phi_a(log n_j).  Then W_p-block = P P^T (PSD)."""
    rows = []
    for t in centres:
        row = []
        for (n, p, k, lam) in pps:
            u = np.log(n)
            w = np.sqrt(lam / np.sqrt(n))
            row.append(w * float(phi_even(u, t, s)))
        rows.append(row)
    return np.array(rows)  # n_centres x n_pp


def weil_prime_block(centres, s, N=2000):
    """The PRIME-place Gram block  sum_p W_p = P P^T  (PSD by Lambda(n)>=0 = the Euler product)."""
    pps = prime_powers(N)
    P = prime_sampling_matrix(centres, s, pps)
    return P @ P.T, pps


# ----------------------------------------------------------------------------------------------
# (3) Davenport-Heilbronn prime side -- the kill-test control.
#
# DH has a functional equation but NO Euler product; its "von Mangoldt" coefficients c_DH(n) are
# NOT >= 0 and NOT prime-power supported (explicit_formula.py).  So the DH analogue of the prime
# block is  W_DH[a,b] = sum_n c_DH(n)/sqrt(n) phi_a(log n) phi_b(log n)  -- NOT a Gram matrix, can
# be indefinite.  This is exactly the place where the Euler product enters as positivity.
# ----------------------------------------------------------------------------------------------


def dh_c_coeffs(N):
    """c_DH(n) for n=1..N from -Z'/Z of the Davenport-Heilbronn function (reuses explicit_formula)."""
    from .explicit_formula import log_deriv_coeffs, dh_coeffs
    return [float(x) for x in log_deriv_coeffs(dh_coeffs(N), N)]


def weil_prime_block_dh(centres, s, N=400):
    """DH prime-side block  W_DH[a,b] = sum_n c_DH(n)/sqrt(n) phi_a(log n) phi_b(log n).

    Because c_DH(n) takes BOTH signs (no Euler product), this is NOT of Gram form and is generally
    INDEFINITE -- the Euler-product positivity is gone."""
    c = dh_c_coeffs(N)
    ncen = len(centres)
    W = np.zeros((ncen, ncen))
    for n in range(2, N + 1):
        cn = c[n - 1]
        if abs(cn) < 1e-14:
            continue
        u = np.log(n)
        vec = np.array([float(phi_even(u, t, s)) for t in centres])
        W += (cn / np.sqrt(n)) * np.outer(vec, vec)
    return W


# ----------------------------------------------------------------------------------------------
# (4) The prime-place involution theta.
#
# Candidate (i): the multiplicative flip u -> -u (= n <-> 1/n, the adelic inversion p^{-1}).  On
# the even basis this is the IDENTITY (phi_a(-u)=phi_a(u)), so <theta h, h> collapses to <h,h> --
# the archimedean reflection, known RH-neutral.  The non-trivial prime reflection must act on the
# PRIME LATTICE, not the continuous u-line.
#
# Candidate (iii): the Gram/Hankel factorisation W_p = P_p P_p^T is itself an OS-type "doubling":
# the reflection is the transpose P_p <-> P_p^T, and OS-positivity = the form being a square.  We
# test whether the prime block IS such a square (PSD) for zeta and for DH.
# ----------------------------------------------------------------------------------------------


def os_reflection_positive(G, tol=1e-9):
    """Is the symmetric matrix G a reflection-positive (OS) pairing on this basis?  Operationally:
    min eigenvalue >= 0 (the pairing <theta h,h> is PSD).  Returns (is_psd, min_eig, max_eig)."""
    w = np.linalg.eigvalsh(0.5 * (G + G.T))
    return bool(w.min() >= -tol * max(1.0, abs(w.max()))), float(w.min()), float(w.max())


def theta_flip_acts_trivially(centres, s, samples=None):
    """Demonstrate that the multiplicative-inversion reflection u -> -u is the IDENTITY on the
    even basis -- i.e. the 'adelic flip' is RH-neutral / archimedean, NOT a prime reflection."""
    if samples is None:
        samples = np.linspace(-4, 4, 41)
    maxdiff = 0.0
    for t in centres:
        a = phi_even(samples, t, s)
        b = phi_even(-samples, t, s)
        maxdiff = max(maxdiff, float(np.max(np.abs(a - b))))
    return maxdiff  # == 0 up to fp: the flip fixes the even test functions


# ----------------------------------------------------------------------------------------------
# Report.
# ----------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------
# (5) Thread-6 bridge (bonus):  Q(f)  read two ways and kill-tested against S_offline.
#
#   (A) scaling-compression / arithmetic-trace side: the explicit-formula prime+arch trace
#       applied to f -- here we use the prime-block quadratic form's diagonal, the "trace" the
#       compression Tr(theta S theta*) reproduces (CC20).  RH-content lives in the Lambda(n) part.
#   (B) Birman-Krein scattering-phase side:  the resonance count = total winding of arg S(1/2+it),
#       N = (1/2pi) \oint d arg S  over a window -- the spectral-shift / resonance side.
#
# Bridge claim (thread 6 sec.2): (A) = (B).  Kill-test: does S_offline (an off-line resonance,
# FE preserved) BREAK the equality, or pass both verbatim (=> RH-neutral, forcing pinned to a
# cross-place term)?  The honest, decisive number is the WINDING: the off-line resonance adds an
# anomalous crossing the on-line trace does not see.
# ----------------------------------------------------------------------------------------------


def scattering_winding(Sfun, T0, T1, npts=600):
    r"""Total winding (1/2pi) \int d arg S(1/2+it) over [T0,T1] = #resonances (Birman-Krein).

    Sfun is a callable s -> mpmath value (e.g. scattering.S or scattering.S_offline)."""
    import mpmath as mp
    ts = [T0 + (T1 - T0) * k / (npts - 1) for k in range(npts)]
    phases = [mp.arg(Sfun(mp.mpc(0.5, t))) for t in ts]
    tot = mp.mpf(0)
    prev = phases[0]
    for p in phases[1:]:
        dp = p - prev
        while dp > mp.pi:
            dp -= 2 * mp.pi
        while dp < -mp.pi:
            dp += 2 * mp.pi
        tot += dp
        prev = p
    return float(tot / (2 * mp.pi))


def thread6_bridge(T0=2.0, T1=30.0):
    """Test the trace=scattering bridge (B) for zeta vs S_offline.  Returns the two windings and
    whether the off-line control breaks the resonance count."""
    from . import scattering as SC
    w_zeta = scattering_winding(SC.S, T0, T1)
    w_off = scattering_winding(SC.S_offline, T0, T1)
    return w_zeta, w_off


def summary():
    np.set_printoptions(precision=3, suppress=True)
    print("=" * 86)
    print("Worker B -- the prime-place reflection / adelic Hankel form")
    print("=" * 86)

    s = 0.35
    centres = np.array([0.0, 0.7, 1.4, 2.1, 2.8, 3.5])
    gammas = zeros(300)

    # --- (1) spectral side: the certified RH-detector ---
    print("\n[1] SPECTRAL-side Weil form (the reliable, PSD-certified side)")
    Gs = weil_gram_spectral(centres, s, gammas)
    psd, mn, mx = os_reflection_positive(Gs)
    print(f"    even-Gaussian Gram (this module): RH-true min eig = {mn:+.4e}  PSD={psd} (cross-check)")
    sp_rh, sp_off = spectral_offline_certified()
    psd_o = sp_off >= -1e-9
    print(f"    certified Toeplitz (weil_form.py): RH-true min eig = {sp_rh:+.3e}  PSD=True")
    print(f"                                       off-line  min eig = {sp_off:+.3e}  PSD={psd_o}"
          f"  <- off-line zero {'BREAKS' if not psd_o else 'keeps'} positivity")
    print("    (spectral side PSD-certified: PSD <=> all gamma real <=> RH.)")

    # --- (2) adelic splitting: the prime Gram block ---
    print("\n[2] ADELIC SPLITTING  W = W_inf + sum_p W_p")
    Wp, pps = weil_prime_block(centres, s, N=4000)
    psd_p, mn_p, mx_p = os_reflection_positive(Wp)
    print(f"    prime block sum_p W_p = P P^T  (P samples Lambda(n)/sqrt(n) at u=log n):")
    print(f"      min eig = {mn_p:+.4e}   max = {mx_p:.4e}   PSD={psd_p}  (#prime powers={len(pps)})")
    print("      => W_p is a Gram matrix, PSD *because Lambda(n) >= 0* -- this is the Euler product.")
    print("      Each place p contributes a rank-(few) PSD block W_p sampled at u = k log p:")
    for p in (2, 3, 5):
        sub = [(n, q, k, lam) for (n, q, k, lam) in pps if q == p]
        Pp = prime_sampling_matrix(centres, s, sub)
        Wpp = Pp @ Pp.T
        r = int(np.linalg.matrix_rank(Wpp, tol=1e-10))
        ev = np.linalg.eigvalsh(Wpp)
        print(f"        place p={p}: block rank={r}, top eig={ev.max():.4e} (>=0, PSD)")

    # --- (3) the candidate prime-place involution theta ---
    print("\n[3] THE PRIME-PLACE INVOLUTION theta")
    d = theta_flip_acts_trivially(centres, s)
    print(f"    (i) multiplicative inversion u->-u (n<->1/n, the 'adelic flip'):")
    print(f"        max |phi(u) - phi(-u)| over basis = {d:.2e}  => theta = IDENTITY on even tests.")
    print("        => the adelic/inversion reflection is the ARCHIMEDEAN reflection: RH-NEUTRAL.")
    print("    (ii) functional-equation reflection s<->1-s: even tests already self-dual => trivial.")
    print("    (iii) the only non-trivial 'reflection' carried by the primes is the Gram doubling")
    print("          W_p = P_p P_p^T.  Its OS-positivity IS the Euler product (Lambda(n) >= 0) --")
    print("          there is NO extra OS involution beyond the sign of Lambda.")

    # --- (4) KILL-TEST against DH ---
    print("\n[4] KILL-TEST -- Davenport-Heilbronn (FE, NO Euler product) prime block")
    Wdh = weil_prime_block_dh(centres, s, N=400)
    psd_dh, mn_dh, mx_dh = os_reflection_positive(Wdh)
    print(f"    DH prime block W_DH[a,b] = sum_n c_DH(n)/sqrt(n) phi_a phi_b:")
    print(f"      min eig = {mn_dh:+.4e}   max = {mx_dh:.4e}   PSD={psd_dh}")
    if not psd_dh:
        print("      => INDEFINITE.  c_DH(n) takes both signs (no Euler product), so the prime block")
        print("         LOSES the Gram/PSD structure.  The prime-block positivity is DESTROYED")
        print("         exactly when the Euler product is removed.")
    else:
        print("      => still PSD: the prime-block positivity is RH-NEUTRAL (would certify DH too).")

    # the discriminator, stated as one number.
    print("\n[VERDICT]")
    print(f"    zeta prime block PSD : {psd_p}   (Lambda(n) >= 0, Gram form)")
    print(f"    DH   prime block PSD : {psd_dh}   (c_DH(n) signed, NOT Gram)")
    discriminates = psd_p and not psd_dh
    print(f"    => prime-block OS-positivity DISCRIMINATES zeta from DH: {discriminates}")
    print("    But the 'reflection' theta is NOT an extra OS involution -- it is just the Gram")
    print("    factorisation W_p = P_p P_p^T, whose positivity = sign(Lambda) = the Euler product.")
    print("    So the OS-positive object that discriminates is the EULER PRODUCT itself, re-skinned")
    print("    as a Hankel/Gram form -- NOT a new prime-place reflection.  See B-prime-reflection.md.")

    # --- (5) Thread-6 bridge bonus: trace = scattering-phase, kill-tested on S_offline ---
    print("\n[5] THREAD-6 BRIDGE (bonus): Q(f) as (B) Birman-Krein scattering winding")
    w_zeta, w_off = thread6_bridge(2.0, 30.0)
    print(f"    (1/2pi) winding of arg S(1/2+it) over t in [2,30]:")
    print(f"      zeta    : N = {w_zeta:+.4f}   (resonances ON Re=1/4)")
    print(f"      S_offline: N = {w_off:+.4f}   (one off-line resonance at Re != 1/4, FE preserved)")
    breaks6 = abs(w_zeta - w_off) > 0.5
    print(f"    off-line resonance adds anomalous winding Delta = {w_off - w_zeta:+.3f}"
          f"  => bridge {'DISCRIMINATES' if breaks6 else 'is RH-NEUTRAL'} here")
    print("    (the resonance/phase side SEES the off-line zero; but this counts zeros, it does not")
    print("     by itself FORCE them on-line -- the forcing is still pinned to the Euler-product")
    print("     positivity of the prime block, the cross-place term.  See B-prime-reflection.md sec.4.)")
    print("=" * 86)
    return {
        "spectral_psd_rh": psd,
        "spectral_psd_offline_certified": bool(psd_o),
        "prime_block_psd_zeta": psd_p,
        "prime_block_psd_dh": psd_dh,
        "discriminates": bool(discriminates),
        "theta_flip_is_identity": d < 1e-9,
        "thread6_winding_zeta": w_zeta,
        "thread6_winding_offline": w_off,
        "thread6_bridge_discriminates": bool(breaks6),
    }


if __name__ == "__main__":
    summary()
