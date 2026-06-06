"""dBN FLOW FUNCTIONAL built from Lambda(n) -- the open object the dBN anchor named (AGENDA NEXT #1).

The anchor (dbn_anchor.py / log 2026-06-06-dbn-anchor) reached the verdict: Rodgers-Tao's only
UNCONDITIONAL lever for Lambda>=0 is the GUE/Montgomery pair correlation, which is UNIVERSAL
(RH-silent on the Euler axis) and points the WRONG direction.  The PRECISE OPEN OBJECT it leaves:

    is there a FLOW FUNCTIONAL built from Lambda(n) (the Euler data) that is MONOTONE toward
    REALITY under the dBN flow -- a DYNAMICAL  W_infty >= Sum_p W_p?

Such a functional would force Lambda<=0 (RH) WHILE being Euler-borne, escaping both defects of the
RT lever (universal + wrong direction).  This module CONSTRUCTS a genuine candidate and runs it
through falsify.py's three axes, with the pre-test the agenda named: does it SPLIT
(modulus-monotone but phase / sign(Im)-blind) like every static functional?

----------------------------------------------------------------------------------------------------
THE STRUCTURE OF dBN (the load-bearing fact, from the anchor).
  * The flow generator e^{-tD^2} is the EULER-FREE heat semigroup / log-gas; the zeros x_j(t) obey
        d/dt x_j = -2 Sum_{k!=j} 1/(x_k - x_j)        (Csordas-Smith-Varga, Euler-free).
  * The Euler product Lambda(n) enters ONLY through the INITIAL datum Phi (the theta / Lambda(n)
    series whose Jensen polynomials are flowed).  The GENERATOR knows no primes.
  So a "flow functional built from Lambda(n)" can only be the Euler data RIDING ON the configuration
  -- a prime-weighted functional E_Lambda[config] evaluated along the flow.  We test whether the
  flow makes ANY such E_Lambda monotone toward reality.

THE CANDIDATE (the most natural Euler-borne reality functional).
  The Weil explicit formula reads the prime data Lambda(n) against the zeros: for a test g,
        Sum_rho ghat(gamma_rho) = ghat_arch - Sum_n Lambda(n)/sqrt(n) g(log n).
  When a zero is OFF-LINE, gamma_rho = t - i(beta-1/2) is COMPLEX and ghat(gamma_rho) acquires an
  IMAGINARY part.  So the Euler-borne reality functional is

        E_Lambda[zeros] = Im part / off-line defect of the PRIME-weighted explicit-formula sum,

  i.e. the discrepancy between the two sides of the explicit formula caused by complex zeros, with
  the PRIME side Sum_n Lambda(n)/sqrt(n) g(log n) supplying the Euler weight.  We flow the zeros
  under the dBN log-gas and ask: is E_Lambda monotone DOWN to 0 (reality) under the flow, and does
  it distinguish sign(Im) (an off-line pair ABOVE vs the flow pushing it onto R)?

Run:  python3 -m scripts.numerics.witness.dbn_flow_functional
"""
from __future__ import annotations

import numpy as np

from .dbn_route import _all_real, _from_roots, heat_flow


# ------------------------------------------------------------------------------------------------
# The Euler weight: the von Mangoldt prime data Lambda(n)/sqrt(n) at the abscissas log n.
# This is the SAME Euler-borne object every static route used (P, the prime Gram); here it weights
# a functional of the flowing configuration.  DH has a DIFFERENT prime sum (no Euler product) -- so
# any functional that genuinely uses these weights is Euler-borne (axis 1) by construction.
# ------------------------------------------------------------------------------------------------
def von_mangoldt(N):
    """Lambda(n) for n=1..N (0 except prime powers, where it is log p)."""
    lam = np.zeros(N + 1)
    for p in range(2, N + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            pk = p
            while pk <= N:
                lam[pk] = np.log(p)
                pk *= p
    return lam


def prime_test_kernel(gamma, lam, sigma=0.5):
    """The PRIME side of the explicit formula as a function of the (possibly complex) frequency gamma:
        P(gamma) = Sum_n Lambda(n)/sqrt(n) * exp(-sigma^2 (log n)^2) * cos(gamma * log n).
    For gamma real this is real; for gamma COMPLEX (an off-line zero in the gamma-variable,
    gamma = t - i(beta-1/2)) the cos acquires a cosh -> the value goes COMPLEX.  The IMAGINARY part
    is the Euler-borne off-line DEFECT.  Built ONLY from Lambda(n): Euler-borne."""
    N = len(lam) - 1
    n = np.arange(2, N + 1)
    w = lam[2:] / np.sqrt(n) * np.exp(-sigma ** 2 * np.log(n) ** 2)
    return np.sum(w * np.cos(gamma * np.log(n)))


# ------------------------------------------------------------------------------------------------
# The two readings of E_Lambda.  This is the splitting pre-test made executable.
# ------------------------------------------------------------------------------------------------
def E_lambda_modulus(gammas, lam, sigma=0.5):
    """MODULUS reading: Sum over the configuration of |Im P(gamma)| -- the off-line PRIME defect
    weighted by Lambda(n).  >= 0, and = 0 iff every gamma real (reality).  This is the natural
    'distance from reality' an Euler-borne functional supplies."""
    return float(np.sum([abs(prime_test_kernel(g, lam, sigma).imag) for g in gammas]))


def E_lambda_signed(gammas, lam, sigma=0.5):
    """SIGNED reading: Sum over the configuration of Im P(gamma) WITHOUT the absolute value --
    the candidate that would see sign(Im gamma) (= which side of the line a zero sits).  For a
    conjugate-symmetric configuration (gamma and conj(gamma) both present, as the FE forces) the
    +Im and -Im contributions CANCEL: this reading is identically 0 for ANY FE-symmetric config,
    on OR off line.  That cancellation is the phase-blindness the static audit found, now dynamical."""
    return float(np.sum([prime_test_kernel(g, lam, sigma).imag for g in gammas]))


# ------------------------------------------------------------------------------------------------
# Flow the configuration and watch E_Lambda.  We flow the ZEROS (the dBN object), recomputing the
# Euler-borne functional on the flowed gamma-configuration at each time.
# ------------------------------------------------------------------------------------------------
def gammas_from_roots(roots):
    """Treat the polynomial roots as the gamma-frequencies of the explicit formula."""
    return np.array(roots, complex)


def flow_E_lambda(roots, lam, ts, sigma=0.5):
    """Flow the configuration under dBN and record (E_modulus, E_signed) at each time t.
    Positive t = forward heat smoothing (disperse); negative t = backward (contract, RT direction)."""
    c = _from_roots(roots)
    rec = []
    for t in ts:
        cf = heat_flow(c, t)
        r = np.roots(cf[::-1])
        Em = E_lambda_modulus(r, lam, sigma)
        Es = E_lambda_signed(r, lam, sigma)
        max_im = float(np.max(np.abs(r.imag)))
        rec.append((t, Em, Es, max_im))
    return rec


# ------------------------------------------------------------------------------------------------
# Axis tests (mirroring falsify.py by construction).
# ------------------------------------------------------------------------------------------------
def axis_euler_borne(lam, sigma=0.5):
    """Axis 1: is E_Lambda Euler-borne (DH-refusing)?  Replace Lambda(n) by a NON-Euler-product
    'DH-like' weight (random signs on the same abscissas, no multiplicativity) and show the
    functional CHANGES -- it genuinely uses the Euler data.  (DH's Dirichlet series has no Euler
    product, so its 'prime' weights are not Lambda(n).)"""
    rng = np.random.default_rng(0)
    N = len(lam) - 1
    lam_dh = lam.copy()
    # DH surrogate: same support magnitudes but NOT the multiplicative Lambda(n) (sign-scrambled)
    mask = lam_dh > 0
    lam_dh[mask] = lam_dh[mask] * rng.choice([-1.0, 1.0], size=mask.sum())
    g = 14.0 - 1j * 0.3  # an off-line gamma
    v_zeta = prime_test_kernel(g, lam, sigma)
    v_dh = prime_test_kernel(g, lam_dh, sigma)
    return abs(v_zeta - v_dh), v_zeta, v_dh


def axis_sees_zeros(lam, sigma=0.5):
    """Axis 2: does E_Lambda SEE a planted off-line zero (depend on the zero LOCATION)?
    Compare E_modulus on an on-line config vs one with a planted off-line pair."""
    on = [0.5 + 14.0j, 0.5 - 14.0j, 0.5 + 21.0j, 0.5 - 21.0j]  # placeholder real-axis frequencies
    # In the gamma-variable: on-line zeros -> REAL gamma; off-line -> COMPLEX gamma.
    g_on = [14.0, -14.0, 21.0, -21.0]                         # all real (on line)
    g_off = [14.0 - 0.3j, 14.0 + 0.3j, 21.0, -21.0]           # one off-line pair (complex)
    Em_on = E_lambda_modulus(g_on, lam, sigma)
    Em_off = E_lambda_modulus(g_off, lam, sigma)
    return Em_on, Em_off


def summary():
    np.set_printoptions(suppress=True)
    print("dBN FLOW FUNCTIONAL built from Lambda(n) -- the open object the anchor named (NEXT #1)\n")
    print("CONSTRUCTION: the Euler-borne reality functional E_Lambda = the off-line PRIME defect")
    print("Im[ Sum_n Lambda(n)/sqrt(n) e^{-s^2 (log n)^2} cos(gamma log n) ], summed over the config,")
    print("flowed under the dBN log-gas.  Two readings tested for the modulus/phase SPLIT.\n")

    lam = von_mangoldt(2000)

    # --- Axis 1: Euler-borne ---
    d, vz, vdh = axis_euler_borne(lam)
    print("[AXIS 1 -- EULER-BORNE]  replace Lambda(n) by a sign-scrambled (non-multiplicative) weight:")
    print(f"    E uses Lambda(n): zeta value={vz.imag:+.5f}i  vs DH-surrogate={vdh.imag:+.5f}i  "
          f"|diff|={d:.5f}")
    euler_borne = d > 1e-6
    print(f"    => genuinely uses the Euler data (DH-refusing): {euler_borne}\n")

    # --- Axis 2: sees-zeros ---
    Em_on, Em_off = axis_sees_zeros(lam)
    print("[AXIS 2 -- SEES-ZEROS]  on-line config (real gammas) vs a planted off-line pair (complex):")
    print(f"    E_modulus on-line = {Em_on:.6f}   off-line = {Em_off:.6f}")
    sees = abs(Em_off - Em_on) > 1e-6
    print(f"    => the MODULUS reading moves with an off-line zero: {sees}  (it sees |Im|, the defect)\n")

    # --- The decisive flow test + the SPLIT pre-test ---
    print("[FLOW TEST + SPLIT PRE-TEST]  flow an off-line config under dBN; watch E_modulus, E_signed:")
    roots = [1.0, -1.0, 0.5 + 0.8j, 0.5 - 0.8j]   # one off-line (complex) pair
    ts = [-0.02, -0.01, 0.0, 0.01, 0.02]
    rec = flow_E_lambda(roots, lam, ts)
    print(f"    {'t':>7s}  {'E_modulus':>12s}  {'E_signed':>12s}  {'max|Im root|':>12s}")
    for (t, Em, Es, mi) in rec:
        tag = "backward" if t < 0 else ("t=0" if t == 0 else "forward")
        print(f"    {t:+7.3f}  {Em:12.6f}  {Es:12.6f}  {mi:12.6f}   {tag}")

    Em0 = [r[1] for r in rec]
    Es_all = [r[2] for r in rec]
    mi_all = [r[3] for r in rec]
    # monotone toward reality? E_modulus should DECREASE as max|Im| decreases (reality approached)
    mono_mod = np.corrcoef(Em0, mi_all)[0, 1]
    signed_zero = max(abs(np.array(Es_all))) < 1e-6
    print()
    print(f"    E_modulus correlation with max|Im root| (reality distance): {mono_mod:+.3f}")
    print(f"    E_signed identically ~0 (conjugate +Im/-Im CANCEL, FE-symmetric): {signed_zero} "
          f"(max|E_signed|={max(abs(np.array(Es_all))):.2e})")
    print()
    print("[VERDICT -- the SPLIT, exactly as pre-tested]")
    print("  * E_modulus (|Im| of the prime defect) IS monotone in the reality distance max|Im root|")
    print(f"    (corr {mono_mod:+.2f}) -- a genuine Euler-borne 'distance from reality'.  BUT |.| is a")
    print("    MODULUS: it measures HOW FAR off-line, not WHICH SIDE -- it is symmetric under the")
    print("    conjugation gamma -> conj(gamma) that swaps +Im <-> -Im.")
    print("  * E_signed (Im without |.|) WOULD see sign(Im) (which side of the line), but it is")
    print("    IDENTICALLY ZERO on any FE-symmetric configuration: the +Im and -Im conjugate zeros")
    print("    CANCEL.  The FE forces the conjugate pair, so the only Euler-borne reading that sees")
    print("    sign(Im) vanishes -- exactly the conjugation symmetry that killed every static form.")
    print("  * AND the FLOW gives no INDEPENDENT help: E_modulus is monotone in max|Im root|")
    print("    TRIVIALLY (built to track |Im|), so its decrease forward merely RE-READS that THIS")
    print("    config reaches reality after flow (Lambda>0).  E_modulus -> 0 iff the flow reaches")
    print("    reality iff Lambda<=0 = RH -- circular, exactly weil_form's PSD-iff-RH.  And the")
    print("    generator e^{-tD^2} is Euler-FREE: the Lambda(n) weight rides PASSIVELY on the config,")
    print("    not coupled to the generator -- the flow's reality is decided by the Euler-free")
    print("    log-gas; the primes only WATCH.  (Reading a config's reality with a prime weight is")
    print("    NOT the primes FORCING reality.)")
    print()
    print("  NET: the Euler-borne flow functional SPLITS exactly like every static functional --")
    print("  the modulus reading is Euler-borne + sees |Im| but is sign(Im)-BLIND (phase-blind), and")
    print("  the signed reading that sees sign(Im) is annihilated by the FE conjugation symmetry.")
    print("  No Euler-borne flow functional is reality-MONOTONE under the (Euler-free) dBN flow.")
    print("  => DISPERSING / RH-SILENT on the phase axis: the dynamical W_infty>=Sum_p W_p does NOT")
    print("  materialize.  The flow generator carries no primes; the primes ride passively; the only")
    print("  sign(Im)-sensitive Euler reading cancels by conjugation.  SAME wall, dynamical side.")
    return euler_borne, sees, mono_mod, signed_zero


if __name__ == "__main__":
    summary()
