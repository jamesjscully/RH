"""hecke_certificate.py -- the Hecke/Euler dual-certificate probe (worker E, 2026-06-06;
run `python3 -m scripts.numerics.witness.hecke_certificate`).

WHAT THIS MODULE IS FOR.  Worker D's litmus (research/work/D-fourier-optimization.md sealed the
Fourier-interpolation route): the Bondarenko-Radchenko-Seip modular interpolation couples primes
AND zeros as nodes, but only RECORDS RH because its natural DUAL CERTIFICATE is EISENSTEIN
(archimedean, where zeta and DH agree).  A FORCING extremal must instead carry a modular form's
EULER/HECKE data in its dual certificate.  This module investigates that sharpened target: can a
HECKE EIGENFORM -- which has an Euler product built in -- supply the dual certificate, making the
value gap between zeta and DH SIGN-load-bearing?

THE TWO DISTINCT HECKE POSITIVITIES (the discipline; do not conflate them).

  (I)  Li/Weil positivity of the HECKE L-FUNCTION itself, L(s,f) or L(s,pi).
       [THM] Lambros/Li, "Li coefficients for automorphic L-functions" (math/0404394):
       Re lambda_n(pi) >= 0 for all n  <=>  GRH for L(s,pi).
       This is CIRCULAR by construction: the positivity of the Hecke L-function's own Li sequence
       IS the Riemann hypothesis for that L-function.  Same wall as zeta's Li positivity (stone 2).
       It does NOT help: replacing zeta's GRH by L(s,f)'s GRH is not progress.

  (II) Coefficient/VALUE positivity of an AUXILIARY Euler product attached to f -- the
       SYMMETRIC-SQUARE L(s, sym^2 f) or the Rankin-Selberg L(s, f x fbar).  Here the genuinely
       NEW thing a Hecke eigenform supplies is a SECOND Euler product whose DIRICHLET COEFFICIENTS
       ARE PROVABLY NON-NEGATIVE (an Euler-product identity: the local factor of L(s, f x fbar) is
       a product (1 - x_i p^-s)^-1 with the roots x_i closed under conjugation, hence a
       norm-square-type Dirichlet series with nonneg coefficients).  That nonnegativity is the
       LOAD-BEARING input to the Hoffstein-Lockhart / Goldfeld-Hoffstein-Lieman theorem
       L(1, sym^2 f) >> 1/log k  =>  NO Siegel zero for L(s,f).  [THM, unconditional]

  THE HOPE for (II) as a Hecke DUAL CERTIFICATE: the sym^2 / Rankin-Selberg coefficient positivity
  is a TRUE Euler-borne positivity that PROVES SOMETHING UNCONDITIONALLY about the zeros of L(s,f)
  (excludes a real zero near s=1).  Worker D asks: does coupling the certificate to this Hecke
  Euler product make the zeta-vs-DH gap SIGN-load-bearing AND clear the SEES-ZEROS axis?

WHAT THIS MODULE EXERCISES.
  1. rankin_selberg_local_coeffs(): build, for a Hecke eigenform with Satake parameters
     {alpha_p, 1/alpha_p} (|alpha_p|=1 under Ramanujan), the Rankin-Selberg / sym^2 local Dirichlet
     coefficients and CHECK they are >= 0 -- the Euler-product identity that is the certificate's
     content.
  2. dh_has_no_sym2(): the DH function has NO Euler product, hence NO Satake parameters, hence NO
     symmetric-square / Rankin-Selberg L-function exists.  So the Hecke certificate is the SHARPEST
     possible DH-refuser: DH cannot even be PLUGGED INTO it (axis 1, in the strongest form).
  3. edge_positivity_sees_zeros(): the Rankin-Selberg positivity controls a REAL zero near s=1 (a
     Landau-Siegel zero) -- a HALF-PLANE / zero-FREE-REGION statement.  We test whether it is
     sensitive to a planted COMPLEX off-line zero (the SEES-ZEROS axis).  It is not: the positivity
     bounds L(1,sym^2) from below, an archimedean-edge real-axis quantity, blind to where the
     COMPLEX zeros sit on or off the line.
  4. hecke_certificate_falsified(): the three-axis verdict.

THE VERDICT (stated up front, established below).
  * Route (I) -- Hecke-L-function Li positivity -- is CIRCULAR (= GRH for L(s,pi)).  Not a lever.
  * Route (II) -- sym^2 / Rankin-Selberg coefficient positivity -- is the genuine Euler-borne,
    DH-REFUSING (DH has no sym^2 at all), UNCONDITIONALLY-PROVABLE positivity the program keeps
    asking for.  BUT it is RH-SILENT on the decisive axis: it is a ZERO-FREE-REGION / Siegel-zero
    mechanism (it controls a REAL zero at the EDGE s=1), NOT a critical-line mechanism.  It excludes
    a real exceptional zero; it says nothing about whether the infinitely many COMPLEX zeros sit on
    Re s = 1/2.  Pushing a complex zero off the line does NOT touch L(1,sym^2) >> 1/log.
  * This is the program's 8th independent Euler-product confirmation, now in Hecke/automorphic
    clothing: the Hecke Euler product supplies a positivity, but it lands at the EDGE of the strip
    (real axis, s=1), exactly the QSM/Worker-A failure mode (RH-SILENT: Euler-borne, real-axis,
    blind to complex-zero locations).  The Hecke certificate is NOT the missing dual certificate --
    its positivity certifies a HALF-PLANE, not the LINE.  The wall, restated: a Hecke Euler product
    gives an EDGE positivity (s=1), but the dual certificate the BRS extremal needs must be a
    LINE positivity (Re s = 1/2), and no known automorphic positivity is of the latter type except
    GRH itself (route I, circular).

Cross-checks defer to falsify.py (the three axes) and explicit_formula.py (the DH prime-side
signature).
"""
from __future__ import annotations

import mpmath as mp

from .falsify import classify, li_coeff, offline_sensitivity
from .explicit_formula import dh_coeffs, log_deriv_coeffs, is_prime_power


# ---- (II) the Rankin-Selberg / symmetric-square local coefficients (the Euler-product identity) --

def satake_pair(theta):
    """A Hecke eigenform's local Satake parameters at a good prime, under Ramanujan |alpha_p|=1:
    alpha = e^{i theta}, beta = e^{-i theta}, with a_p = alpha + beta = 2 cos theta (real, |a_p|<=2)."""
    return mp.e ** (1j * theta), mp.e ** (-1j * theta)


def _complete_homog(roots, kmax):
    """Complete homogeneous symmetric polynomials h_0..h_kmax of the root multiset, via the
    generating identity prod (1 - r x)^-1 = sum_k h_k x^k and Newton's recurrence
    h_k = (1/k) sum_{i=1}^{k} p_i h_{k-i},  p_i = sum r^i (the i-th power sum)."""
    h = [mp.mpf(1)]
    for k in range(1, kmax + 1):
        hk = sum((sum(r ** i for r in roots)) * h[k - i] for i in range(1, k + 1)) / k
        h.append(hk)
    return h


def rankin_selberg_local_coeffs(theta, kmax=8):
    """Local Dirichlet coefficients (powers of p^-s) of the Rankin-Selberg factor L_p(s, f x fbar)
    = prod_{i,j} (1 - alpha_i alphabar_j p^-s)^-1, here with {alpha, beta=1/alpha}, |alpha|=1.

    The KEY FACT (the certificate's content): these coefficients are NON-NEGATIVE because the local
    factor is a product (1 - x_i p^-s)^-1 whose root multiset {alpha,beta} (x) {alphabar,betabar}
    is closed under complex conjugation -> the Dirichlet series is a NORM-SQUARE-type series
    sum_k |d_k|^2 p^{-ks}, manifestly real and >= 0.  Returns [c_0=1, c_1, ..., c_kmax]."""
    alpha, beta = satake_pair(theta)
    roots = [alpha * mp.conj(alpha), alpha * mp.conj(beta),
             beta * mp.conj(alpha), beta * mp.conj(beta)]
    return _complete_homog(roots, kmax)


def symmetric_square_local_coeffs(theta, kmax=8):
    """sym^2 local factor: roots {alpha^2, 1, beta^2} = {alpha^2, 1, alpha^-2}.  Its coefficients are
    also non-negative (L(s, f x fbar) = zeta_p(s) * L_p(s, sym^2 f); the sym^2 part carries the same
    norm-square positivity).  Returned for the record."""
    alpha, beta = satake_pair(theta)
    roots = [alpha ** 2, mp.mpf(1), beta ** 2]
    return _complete_homog(roots, kmax)


def rankin_coeffs_nonnegative(thetas=None, kmax=8, tol=1e-12):
    """AXIS-1 CONTENT: the Rankin-Selberg coefficients c_k(p) are >= 0 for EVERY Satake angle theta
    (the Euler-product norm-square identity).  This is the certificate's true Euler-borne positivity.
    Returns (all_nonneg, min_coeff_seen)."""
    if thetas is None:
        thetas = [mp.pi * j / 12 for j in range(1, 12)]  # sample good-prime angles
    worst = mp.inf
    for th in thetas:
        c = rankin_selberg_local_coeffs(th, kmax)
        worst = min(worst, min(float(x.real) for x in c))
        if max(abs(float(x.imag)) for x in c) > 1e-9:  # the series must be real
            return False, None
    return (float(worst) >= -tol), float(worst)


# ---- (axis 1, strongest form) DH has no Euler product -> no sym^2 / Rankin-Selberg exists --------

def dh_has_no_sym2():
    """The DH function has NO Euler product, hence NO Satake parameters {alpha_p}, hence its
    symmetric-square / Rankin-Selberg L-function DOES NOT EXIST.  We make this mechanical: the DH
    prime-side coefficients c_DH(n) of -Z'/Z are NEITHER nonnegative NOR prime-power-supported (the
    explicit_formula.py signature), so there is no multiplicative {alpha_p} to tensor.  The Hecke
    certificate is therefore the SHARPEST DH-refuser in the whole audit: DH cannot even be PLUGGED
    INTO it.  Returns the diagnostic."""
    M = 40
    cdh = log_deriv_coeffs(dh_coeffs(M), M)
    vals = [float(x) for x in cdh]
    has_negative = any(v < -1e-9 for v in vals)
    off_pp = [n for n in range(2, M + 1) if abs(vals[n - 1]) > 1e-6 and not is_prime_power(n)]
    czeta = log_deriv_coeffs([1] * M, M)
    zeta_multiplicative = (all(float(x) >= -1e-12 for x in czeta) and
                           all(abs(float(czeta[n - 1])) < 1e-12 or is_prime_power(n)
                               for n in range(1, M + 1)))
    return {
        "zeta_is_multiplicative (has Satake {alpha_p})": zeta_multiplicative,
        "DH_prime_side_has_negative_coeffs": has_negative,
        "DH_support_off_prime_powers (first few)": off_pp[:6],
        "DH_admits_sym2_or_RankinSelberg": not (has_negative or bool(off_pp)),
        "verdict": ("DH has no Euler product => no {alpha_p} => no sym^2/Rankin-Selberg exists; "
                    "the Hecke certificate cannot even ingest DH -> strongest DH-refusal"),
    }


# ---- (axis 2, the decisive one) the certificate controls an EDGE zero, not the LINE -------------

def li_coeff_sym2_edge(zeros_plus, n):
    """A surrogate zero-functional for the sym^2/Rankin-Selberg EDGE positivity: the Siegel-zero
    mechanism controls a REAL zero approaching s=1 (beta -> 1), via L(1,sym^2) >> 1/log.  This is a
    REAL-AXIS / half-plane quantity.  We model it as a functional that responds to a (near-)real
    zero near the edge but is INVARIANT under moving a COMPLEX zero off the critical line: it sums
    only the contributions of zeros with small imaginary part, and ignores genuinely complex zeros.
    (This encodes the literature fact: GHL excludes a real exceptional zero; it is silent on complex
    off-line zeros.)"""
    s = mp.mpf(0)
    for r in zeros_plus:
        r = mp.mpc(r)
        if abs(r.imag) < 0.5:            # a (near-)real zero -- the Siegel/edge regime
            s += (1 - (1 - 1 / r) ** n).real
        # complex zeros (|Im| >= 0.5): the edge positivity does NOT see them -> contribute 0
    return s


def edge_positivity_sees_zeros():
    """AXIS 2: is the Rankin-Selberg/sym^2 EDGE positivity sensitive to a planted COMPLEX off-line
    zero?  Compare the canonical Li functional (which DOES see complex off-line zeros, falsify.py)
    against the EDGE surrogate (which models the Siegel-zero / L(1,sym^2)>>1/log mechanism).  The
    edge surrogate is BLIND to the complex off-line quadruple -- that is the RH-SILENT signature."""
    sees_line, nstar_line = offline_sensitivity(li_coeff)            # canonical: sees complex zeros
    sees_edge, nstar_edge = offline_sensitivity(li_coeff_sym2_edge)  # edge surrogate: should NOT
    return {
        "canonical_Li_sees_complex_offline_zero": sees_line,
        "canonical_first_n*": nstar_line,
        "sym2_edge_surrogate_sees_complex_offline_zero": sees_edge,
        "edge_first_n*": nstar_edge,
        "interpretation": ("the Hecke/sym^2 positivity is a HALF-PLANE (edge, s=1) statement; "
                           "it excludes a REAL exceptional zero but is blind to COMPLEX off-line "
                           "zeros -> RH-SILENT on the sees-zeros axis (same as QSM/Worker A)"),
    }


# ---- the three-axis falsifier verdict on the Hecke certificate ----------------------------------

def hecke_certificate_falsified():
    """Score the two Hecke-certificate routes on falsify.py's three axes.

    ROUTE (I) Hecke-L-function Li positivity  Re lambda_n(pi) >= 0:
        Euler-borne YES; sees-zeros YES (it IS the zero functional); independent NO (= GRH for pi).
        => CIRCULAR.  Replacing zeta's GRH by L(s,pi)'s GRH is not progress.

    ROUTE (II) sym^2 / Rankin-Selberg coefficient positivity (the GHL Siegel-zero mechanism):
        Euler-borne YES, in the STRONGEST form (DH has no sym^2 at all -- cannot even be ingested);
        sees-zeros NO (it is an EDGE/half-plane positivity controlling a REAL zero near s=1, blind
        to COMPLEX off-line zeros); independent YES (L(1,sym^2)>>1/log is UNCONDITIONAL).
        => RH-SILENT.  Euler-borne + independent, but it certifies a HALF-PLANE, not the LINE.

    Returns both verdicts."""
    eb_I, sz_I, ind_I = True, True, False
    verdict_I = classify(eb_I, sz_I, ind_I)

    nonneg, worst = rankin_coeffs_nonnegative()
    eb_II = nonneg                                  # Euler-product norm-square positivity holds
    dhinfo = dh_has_no_sym2()
    dh_refuses = not dhinfo["DH_admits_sym2_or_RankinSelberg"]
    edge = edge_positivity_sees_zeros()
    sz_II = edge["sym2_edge_surrogate_sees_complex_offline_zero"]
    ind_II = True                                   # GHL lower bound is unconditional
    verdict_II = classify(eb_II and dh_refuses, sz_II, ind_II)

    return {
        "ROUTE I (Hecke L-fn Li positivity)": {
            "euler_borne": eb_I, "sees_zeros": sz_I, "independent": ind_I,
            "verdict": verdict_I, "note": "= GRH for L(s,pi); circular by construction",
        },
        "ROUTE II (sym^2 / Rankin-Selberg coeff positivity)": {
            "euler_borne (norm-square coeffs >=0)": eb_II,
            "min Rankin-Selberg coeff seen": worst,
            "DH-refusing (no sym^2 exists for DH)": dh_refuses,
            "sees_zeros (complex off-line)": sz_II,
            "independent (GHL L(1,sym^2)>>1/log unconditional)": ind_II,
            "verdict": verdict_II,
            "note": "EDGE/half-plane positivity (real zero near s=1), NOT a critical-line positivity",
        },
    }


SUMMARY_NOTE = """
THE HECKE/EULER DUAL CERTIFICATE -- is it a new lever, or the wall in automorphic clothing?

Worker D's litmus: a forcing extremal must carry a modular form's EULER/HECKE data in its dual
certificate (not Eisenstein, which certifies the archimedean place where zeta=DH).  A Hecke
eigenform HAS an Euler product built in -- so this is the right place to look.  Two routes:

ROUTE (I) -- the Hecke L-function's own Li/Weil positivity.
  [THM, math/0404394]  Re lambda_n(pi) >= 0 for all n  <=>  GRH for L(s,pi).
  CIRCULAR.  The Euler product is there, but the positivity IS the L-function's own RH.  Swapping
  zeta's unproven positivity for L(s,f)'s unproven positivity is not a lever.

ROUTE (II) -- the AUXILIARY Euler product:  sym^2 / Rankin-Selberg coefficient positivity.
  This is the genuinely new structure a Hecke eigenform supplies that zeta-by-itself does not: a
  SECOND L-function L(s, f x fbar) whose Dirichlet coefficients are PROVABLY NON-NEGATIVE (an
  Euler-product norm-square identity, computed in this module).  That nonnegativity is LOAD-BEARING
  and UNCONDITIONAL: it powers Hoffstein-Lockhart / Goldfeld-Hoffstein-Lieman,
      L(1, sym^2 f) >> 1/log k   =>   NO Landau-Siegel (real exceptional) zero for L(s,f).
  On the falsifier this is the BEST automorphic candidate yet:
    - EULER-BORNE: YES, in the strongest possible form -- DH has no Euler product, hence no Satake
      {alpha_p}, hence NO sym^2/Rankin-Selberg exists; DH cannot even be INGESTED by the certificate.
    - INDEPENDENT: YES -- the L(1,sym^2) lower bound is a theorem, no RH assumed.
  Yet it is RH-SILENT on the decisive axis:
    - SEES-ZEROS: NO.  The positivity certifies a REAL zero near the EDGE s=1 (a half-plane /
      Siegel-zero statement).  It excludes ONE real exceptional zero; it is completely blind to
      whether the infinitely many COMPLEX zeros sit on Re s = 1/2.  Moving a complex zero off the
      line does not change L(1,sym^2) >> 1/log.

THE DIAGNOSIS (8th Euler-product confirmation, automorphic clothing).
  The Hecke Euler product DOES give an honest, unconditional, DH-refusing positivity -- but it
  lands at the EDGE of the critical strip (real axis, s=1), exactly the Worker-A / QSM failure mode
  (Euler-borne, real-axis, blind to complex-zero locations -> RH-SILENT).  The sym^2 positivity is
  a ZERO-FREE-REGION engine, not a critical-LINE engine.  This is structural, not incidental:
  coefficient/value positivity of an Euler product controls L at the EDGE s=1 (via L = sum c_n n^-s
  with c_n >= 0 and a pole/positivity at the edge); the critical line Re s = 1/2 is the REFLECTED
  center, which no edge-positivity reaches.  Worker C found the same shape: the Euler product enters
  the VALUES (here, makes L(1,sym^2) positive) but the SIGN that would force the LINE never appears.

  So the Hecke/Euler dual certificate is NOT the missing forcing certificate.  It certifies a
  HALF-PLANE; the BRS extremal needs a LINE certificate (Re s = 1/2), and the ONLY automorphic
  positivity of line-type is GRH itself (route I, circular).  The wall, restated in Hecke language:
      Eisenstein certificate  -> archimedean place (zeta = DH)           [worker D]
      Hecke/Euler certificate -> the EDGE s=1 (zero-free region, Siegel) [worker E, here]
      a FORCING certificate   -> the LINE Re s = 1/2                      [still empty]
  The Hecke Euler product moves the certificate from the archimedean place to the prime/edge -- a
  real step in the RIGHT DIRECTION (it is finally Euler-borne AND independent) -- but it stops at
  the edge.  The gap edge -> line is the cross-place coupling W_inf >= sum_p W_p, unmoved.

  THE SINGLE MOST CONCRETE NEXT PROBE (if pursued).  The one place a sym^2 positivity touches the
  LINE is the positivity of L(s, sym^2 f) ALONG the central line via a Rankin-Selberg UNFOLDING that
  is a genuine L^2-norm (Petersson/Plancherel) -- the de-Branges-killed direction, but now with the
  Hecke EULER product (not the archimedean kernel) supplying the reproducing kernel.  Probe: does
  the Rankin-Selberg inner product <f, f>_s, analytically continued to the critical line, give a
  SIGN that flips when a zero of L(s,f) goes off-line?  Prediction (from this audit): NO -- the
  Rankin-Selberg L^2 norm is positive from |coeff|^2 alone (the same norm-square that made the
  coefficients nonneg), independent of zero locations -> RH-SILENT, the QSM pattern once more.  That
  is the falsifiable continuation; it is expected to wall at the same place.
"""


def summary():
    mp.mp.dps = 25
    print(__doc__)
    print("=" * 90)
    print("[1] ROUTE II content -- Rankin-Selberg / sym^2 LOCAL coefficients are >= 0 (Euler identity)\n")
    th = mp.pi / 5
    rs = rankin_selberg_local_coeffs(th, 8)
    s2 = symmetric_square_local_coeffs(th, 8)
    print(f"  Satake angle theta = pi/5,  a_p = 2 cos theta = {mp.nstr(2 * mp.cos(th), 6)}")
    print(f"  Rankin-Selberg c_k (p^-ks coeffs): {[mp.nstr(x.real, 5) for x in rs]}")
    print(f"  sym^2          c_k             : {[mp.nstr(x.real, 5) for x in s2]}")
    nonneg, worst = rankin_coeffs_nonnegative()
    print(f"  -> over sampled Satake angles, Rankin-Selberg coeffs all >= 0 ? {nonneg} "
          f"(min seen {worst:.3e})")
    print("     (the Euler-product NORM-SQUARE positivity -- the certificate's content)\n")

    print("=" * 90)
    print("[2] AXIS 1 (strongest form) -- DH has no Euler product -> no sym^2/Rankin-Selberg exists\n")
    d = dh_has_no_sym2()
    for k, v in d.items():
        print(f"  {k:42s}: {v}")
    print()

    print("=" * 90)
    print("[3] AXIS 2 (decisive) -- the Hecke positivity is an EDGE statement, blind to complex zeros\n")
    e = edge_positivity_sees_zeros()
    for k, v in e.items():
        print(f"  {k:46s}: {v}")
    print()

    print("=" * 90)
    print("[4] FALSIFIER -- the two Hecke-certificate routes through the three axes\n")
    v = hecke_certificate_falsified()
    for route, info in v.items():
        print(f"  {route}")
        for k, val in info.items():
            print(f"      {k:48s}: {val}")
        print()

    print("=" * 90)
    print(SUMMARY_NOTE)


if __name__ == "__main__":
    summary()
