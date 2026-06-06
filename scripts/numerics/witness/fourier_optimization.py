"""fourier_optimization.py -- the Fourier-optimization / sign-uncertainty reading of the
explicit-formula positivity, and the falsifier verdict on the extremal-function candidate
(worker D, 2026-06-06; run `python3 -m scripts.numerics.witness.fourier_optimization`).

WHAT THIS MODULE IS FOR.  Worker D investigates whether the modern Fourier-optimization /
sign-uncertainty / exact-interpolation machinery (Beurling-Selberg majorants in the explicit
formula; Cohn-Elkies LP and the Bourgain-Clozel-Kahane sign uncertainty; Radchenko-Viazovska
Fourier interpolation and Viazovska's modular magic functions) is the right tool to FORCE the
explicit-formula positivity, or whether it hits the program's standing wall.

THE PRECISE REDUCTION (the explicit formula AS a sign-uncertainty problem).
The Guinand-Weil explicit formula, written as a pairing on an even test function g = phi*phi^*
(so ghat = |phihat|^2 >= 0 is a Fejer/Fourier square):

    Sum_rho ghat(gamma_rho)  =  W_inf(g)  -  Sum_{n>=2} (Lambda(n)/sqrt(n)) g(log n)     (EF)
    └─ ZEROS (spectral) ─┘      └ archimedean ┘   └────────── PRIMES ──────────┘

  * The LHS is >= 0 *iff* all gamma_rho are real, i.e. iff RH  (each |phihat(gamma)|^2 >= 0).
  * W_inf(g) = (1/2pi) integral ghat(t) Re[psi(1/4 + it/2)] dt - (log pi) ghat(0)-term is the
    ARCHIMEDEAN term: ghat integrated against the Plancherel/digamma density Re psi(1/4+it/2).
  * The prime side samples g on the LOG-PRIME-POWER LATTICE {log p^k} with weights Lambda(n)/sqrt(n).

  Weil positivity (necessary for RH) is then the SIGN-UNCERTAINTY INEQUALITY:

    for every even g with ghat >= 0 (a +1-type Fourier-square constraint),
        W_inf(g)  >=  Sum_{n>=2} (Lambda(n)/sqrt(n)) g(log n).                            (WP)

  This is a Cohn-Elkies-type linear program: maximize the prime side / archimedean side ratio
  over the cone {ghat >= 0}.  The archimedean density Re psi(1/4+it/2) is the analogue of the
  Cohn-Elkies "forbidden region" -- the place the test function must avoid paying mass.  It is a
  +1 sign-uncertainty (ghat >= 0, a Fourier SQUARE), NOT the -1 (Cohn-Elkies packing) sign.

HOW THIS MODULE EXERCISES THE REDUCTION.
  1. weil_pairing(g): evaluate the three pieces of (EF) on a concrete even test g for zeta and DH,
     showing the prime side is the Euler-borne discriminator and W_inf is shared (RH-neutral).
  2. beurling_selberg_ratio(): the Beurling-Selberg / Gaussian-subordination extremal problem that
     the Carneiro-Chandee-Littmann-Milinovich line ACTUALLY solves -- bounding S(t)/prime gaps
     UNDER RH.  We compute the Fourier-optimization ratio and show it produces a one-sided
     (majorant/minorant) BOUND, not a forcing identity.
  3. extremal_candidate_falsified(): run the "Euler-borne modular extremal function" candidate
     through falsify.py's THREE axes (Euler-borne / sees-zeros / independent).

THE VERDICT (stated up front, established below).  The Fourier-optimization machinery is a
MAJORANT machine: it proves inequalities of the form "given RH, sum over zeros <= (extremal
constant)".  It is CONDITIONAL ON RH -- it consumes RH (real zeros => ghat(gamma) real-sampled)
to produce bounds; it never produces the positivity (WP) from below.  The Radchenko-Viazovska /
Bondarenko-Radchenko-Seip interpolation with zeta zeros as nodes is the deepest connection, but
the interpolation basis EXISTS UNCONDITIONALLY (nodes = zeros wherever they are) and only its
NON-REDUNDANCY is equivalent to RH+simplicity -- so it RECORDS RH, it does not force it.  On the
falsifier: the extremal-function candidate is EULER-BORNE (the prime weights Lambda(n) carry the
product; DH's signed weights break the majorant) but it does NOT SEE THE ZEROS in a forcing way
(the extremal inequality is over the cone {ghat>=0}, which is RH-agnostic), and it is NOT
INDEPENDENT (its sharp form IS the Weil positivity).  Verdict: RH-SILENT-to-CIRCULAR -- same wall
as stones 1-2.  Detail and the modular-magic-function assessment in
research/work/D-fourier-optimization.md.
"""
from __future__ import annotations

import mpmath as mp

from .falsify import classify, li_coeff, offline_sensitivity
from .explicit_formula import log_deriv_coeffs, dh_coeffs, von_mangoldt, is_prime_power


# ---- the archimedean (Plancherel/digamma) density --------------------------------------------

def archimedean_density(t):
    """Re psi(1/4 + i t/2) - log(pi) : the archimedean spectral density against which ghat is
    integrated in W_inf.  This is the Plancherel measure of the explicit formula's ∞-place; it
    is SHARED by zeta and DH (same Gamma_R), hence RH-NEUTRAL -- the 'forbidden region' that no
    choice of test function removes."""
    return mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * t / 2)) - mp.log(mp.pi)


# ---- the three pieces of the explicit-formula pairing on a Gaussian test ---------------------

def _gaussian_pair(sigma):
    """Even test g(u) = exp(-u^2/(2 sigma^2)) with ghat(t) = sigma sqrt(2pi) exp(-sigma^2 t^2/2)
    >= 0 (a +1 Fourier-square / Fejer-type function, the cone of Weil positivity)."""
    g = lambda u: mp.e ** (-(u ** 2) / (2 * sigma ** 2))
    ghat = lambda t: sigma * mp.sqrt(2 * mp.pi) * mp.e ** (-(sigma ** 2) * t ** 2 / 2)
    return g, ghat


def weil_pairing(sigma=0.5, Nprime=2000, Tcut=60.0):
    """Evaluate the explicit-formula pairing (EF) on a Gaussian test, for zeta and for the
    DH analogue (signed prime weights).  The archimedean SIDE of the Weil functional is the full

        W_arch(g) = [pole terms g(i/2)+g(-i/2)]  +  (1/2pi) integral ghat(t) density(t) dt,

    and the Weil positivity is the margin  M = W_arch(g) - P_prime(g) = Sum_rho ghat(gamma_rho)
    >= 0 (the spectral side), positive for every even g with ghat >= 0 IFF RH.  The pole terms
    (from the simple poles of zeta at s=0,1) are the dominant POSITIVE part of W_arch; including
    them is what makes the margin genuinely positive for zeta (the point of Weil positivity).
    Returns W_arch, the prime side P, and the margin for zeta and the DH analogue."""
    g, ghat = _gaussian_pair(sigma)

    # archimedean side: pole terms (s=0,1 -> g(+-i/2)) + the digamma/Plancherel integral.
    # g is the even Gaussian; its analytic continuation g(i/2) = exp(+1/(8 sigma^2)).
    pole = 2 * mp.e ** (mp.mpf(1) / (8 * sigma ** 2))   # g(i/2) + g(-i/2)
    arch_int = (1 / (2 * mp.pi)) * mp.quad(lambda t: ghat(t) * archimedean_density(t), [-Tcut, 0, Tcut])
    W_arch = pole + arch_int

    # prime side, zeta: Sum Lambda(n)/sqrt(n) g(log n)
    P_zeta = mp.mpf(0)
    for n in range(2, Nprime + 1):
        if is_prime_power(n):
            P_zeta += von_mangoldt(n) / mp.sqrt(n) * g(mp.log(n))

    # prime side, DH: same lattice but signed log-derivative coefficients c_DH(n)
    cdh = log_deriv_coeffs(dh_coeffs(Nprime), Nprime)
    P_dh = mp.mpf(0)
    for n in range(2, Nprime + 1):
        cn = float(cdh[n - 1])
        if abs(cn) > 1e-14:
            P_dh += mp.mpf(cn) / mp.sqrt(n) * g(mp.log(n))

    return {
        "sigma": sigma,
        "W_inf": W_arch,
        "P_zeta": P_zeta,
        "P_dh": P_dh,
        "margin_zeta": W_arch - P_zeta,
        "margin_dh": W_arch - P_dh,
    }


# ---- the Beurling-Selberg / Gaussian-subordination extremal ratio (the CCM machine) ----------

def beurling_selberg_ratio(sigmas=(0.15, 0.2, 0.3, 0.4, 0.5)):
    """The Fourier-optimization RATIO that the Carneiro-Chandee-Littmann-Milinovich line
    optimizes.  Over the cone of admissible test functions {ghat >= 0}, the conditional-on-RH
    bound is governed by

        R(g) = (prime side) / (archimedean side) = P[g] / W_inf[g],

    and the extremal problem is sup_g R(g).  R < 1 for ALL admissible g is exactly the Weil
    positivity margin (WP).  We tabulate R over a Gaussian-subordination family (the standard
    extremal family of Carneiro-Littmann-Vaaler) to exhibit the extremal ratio numerically and
    show it is a one-sided BOUND, sup over a cone -- never an identity that forces RH.  (We use
    narrow widths sigma <= 0.5: the bare Gaussian with a finite prime sum and a truncated digamma
    integral is a faithful Weil test only when the pole term dominates; the genuine Beurling-
    Selberg extremals have compactly supported ghat and keep the margin positive across all
    scales.  The point demonstrated is the EXISTENCE of a positive extremal ratio R<1 over the
    cone {ghat>=0} -- the structure, not the sharp constant.)"""
    rows = []
    best = mp.mpf(0)
    for s in sigmas:
        r = weil_pairing(sigma=s)
        ratio = r["P_zeta"] / r["W_inf"] if r["W_inf"] != 0 else mp.inf
        rows.append((s, r["W_inf"], r["P_zeta"], ratio, r["margin_zeta"] > 0))
        best = max(best, ratio)
    return rows, best


# ---- the falsifier verdict on the extremal-function candidate ---------------------------------

def extremal_candidate_falsified():
    """Score the 'Euler-borne modular extremal function' candidate on falsify.py's three axes.

    The candidate: a Beurling-Selberg / Viazovska-style extremal majorant g_* for the explicit
    formula, whose +1 sign-uncertainty optimum would be the sharp Weil-positivity constant.

    AXIS 1 (Euler-borne): does the extremal inequality FAIL for DH?  YES -- the prime side uses
      the von Mangoldt weights Lambda(n)>=0 (Euler product); DH's signed weights c_DH(n) destroy
      the majorant.  (Demonstrated by weil_pairing: P_dh differs structurally from P_zeta.)
    AXIS 2 (sees-zeros): is the extremal inequality SENSITIVE to a planted off-line zero, i.e.
      does it depend on zero LOCATIONS?  We test the canonical zero-functional that the extremal
      problem controls (the Li/Weil functional) for offline sensitivity.  The subtlety: the
      Fourier-optimization BOUND is a sup over the cone {ghat>=0}, which is RH-AGNOSTIC -- the
      extremal CONSTANT does not move when a zero goes off-line; only the (already-RH) spectral
      side does.  So the optimization is sees-zeros only when it is read as the Weil positivity
      itself (CIRCULAR), not as the majorant bound (RH-SILENT).
    AXIS 3 (independent): is the sharp inequality provable without assuming RH?  NO -- its sharp
      form IS the Weil positivity (= RH via Bombieri-Lagarias/Li).

    Returns the falsify.py verdict for both readings of the candidate."""
    # AXIS 1: Euler-borne -- the prime weights discriminate zeta from DH.
    cz = log_deriv_coeffs([1] * 60, 60)
    cdh = log_deriv_coeffs(dh_coeffs(60), 60)
    zeta_nonneg_pp = all(float(cz[n - 1]) >= -1e-9 and
                         (abs(float(cz[n - 1])) < 1e-9 or is_prime_power(n)) for n in range(2, 61))
    dh_signed = any(float(cdh[n - 1]) < -1e-9 for n in range(2, 61))
    euler_borne = zeta_nonneg_pp and dh_signed

    # AXIS 2: sees-zeros -- reading (a) the BOUND (cone sup, RH-agnostic) vs (b) the positivity.
    # The Li/Weil zero-functional (what the sharp inequality controls) DOES see the zeros:
    sees_zeros_positivity, nstar = offline_sensitivity(li_coeff)
    # but the Fourier-optimization BOUND (sup over {ghat>=0}) is a fixed extremal CONSTANT that
    # does not depend on where the zeros sit -- it is RH-agnostic by construction:
    sees_zeros_bound = False

    # AXIS 3: independent -- the sharp inequality IS the Weil positivity (= RH).
    independent = False

    verdict_bound = classify(euler_borne, sees_zeros_bound, independent)        # the majorant reading
    verdict_sharp = classify(euler_borne, sees_zeros_positivity, independent)   # the sharp/positivity reading

    return {
        "euler_borne": euler_borne,
        "sees_zeros (bound reading)": sees_zeros_bound,
        "sees_zeros (sharp/positivity reading)": sees_zeros_positivity,
        "first_offline_n*": nstar,
        "independent": independent,
        "verdict (Fourier-optimization BOUND)": verdict_bound,
        "verdict (sharp = Weil positivity)": verdict_sharp,
    }


# ---- the modular-magic-function bet ----------------------------------------------------------

MODULAR_BET = """
THE FRESH BET -- a Viazovska-style modular magic function as the exact extremal (assessment).

The hope:  modular forms carry the primes (Hecke eigenvalues / Euler product) => Euler-borne;
           interpolation nodes = the zeros (Bondarenko-Radchenko-Seip) => sees-zeros;
           so a +1 modular eigenfunction with roots at the zeros could be the exact extremal
           that forces the Weil positivity.

Where it is genuinely fresh:
  * Viazovska's d=8,24 magic functions ARE Fourier eigenfunctions (+1/-1) with PRESCRIBED sign
    and PRESCRIBED double roots at the lattice radii, built as Laplace transforms of weakly
    holomorphic modular forms.  This is the only known machine that produces an EXACT extremal
    (not just a bound) for a sign-uncertainty LP -- it closes the Cohn-Elkies gap in d=8,24.
  * Bondarenko-Radchenko-Seip (arXiv:2005.02996) build, FOR THE THETA GROUP, a Fourier
    interpolation basis whose time-nodes are {log n / 2pi} (the PRIMES enter via Lambda(n)) and
    whose frequency-nodes are the ZETA ZEROS (rho-1/2)/i.  The Riemann-Weil functional W is
    *exactly* the evaluation of the explicit formula in this basis: W U_n = Lambda(n)/sqrt(n).
    So the modular machine ALREADY connects primes (nodes) and zeros (nodes) for zeta.

Where it hits the wall (the honest assessment):
  * The BRS interpolation basis EXISTS UNCONDITIONALLY -- the nodes are the zeros WHEREVER they
    sit; the construction never uses RH.  RH (+ simplicity) is equivalent only to the basis being
    NON-REDUNDANT (a frame, not over-/under-complete).  So the modular object RECORDS RH as a
    density/completeness statement; it does not PRODUCE the positivity.  Removing the off-line
    case does not break the interpolation, it breaks the non-redundancy -- i.e. RH is read off,
    not forced.
  * The d=8,24 magic functions force a packing bound because the -1 sign-uncertainty there has a
    GENUINE forbidden region with a SHARP modular obstruction (E_6 / E_4 Eisenstein series give
    the matching dual certificate).  The explicit-formula sign-uncertainty is +1 type and its
    'forbidden region' is the archimedean density Re psi(1/4+it/2), which is RH-NEUTRAL (shared
    with DH).  There is no Eisenstein-series dual certificate that distinguishes on-line from
    off-line zeros -- the modular obstruction lives at the wrong (archimedean) place.
  * Net: the modular machine supplies the EXACT interpolation/extremal STRUCTURE (genuinely
    fresh -- nodes are simultaneously primes and zeros), but the POSITIVITY it would have to
    certify is still the Weil positivity, and the modular dual certificate it produces (a la E_6)
    certifies the archimedean place, where ζ and DH agree.  It hits the SAME WALL: the place-
    crossing (archimedean ⟷ prime) the whole program is pinned to.  The bet is FRESH IN
    STRUCTURE, WALLED IN POSITIVITY -- it would force RH only if a modular form's Euler product
    (Hecke side) entered the dual certificate, which is exactly the open cross-place coupling.
"""


def summary():
    mp.mp.dps = 25
    print(__doc__)
    print("=" * 90)
    print("[1] the explicit-formula pairing (EF) on a Gaussian test -- prime side is the discriminator\n")
    r = weil_pairing(sigma=0.5)
    print(f"  sigma = {r['sigma']}")
    print(f"  W_inf (archimedean, shared / RH-neutral) = {mp.nstr(r['W_inf'], 8)}")
    print(f"  prime side  P_zeta (Lambda(n)>=0, Euler)  = {mp.nstr(r['P_zeta'], 8)}")
    print(f"  prime side  P_dh   (c_DH(n) signed)       = {mp.nstr(r['P_dh'], 8)}")
    print(f"  Weil margin  W_inf - P_zeta               = {mp.nstr(r['margin_zeta'], 8)}  (>0: {r['margin_zeta'] > 0})")
    print(f"  Weil margin  W_inf - P_dh                 = {mp.nstr(r['margin_dh'], 8)}")
    print("  -> the prime side carries the Euler product; the archimedean side is shared with DH.\n")

    print("=" * 90)
    print("[2] the Beurling-Selberg / Gaussian-subordination extremal ratio R = P/W_inf (the CCM machine)\n")
    rows, best = beurling_selberg_ratio()
    print(f"  {'sigma':>6}  {'W_inf':>12}  {'P_zeta':>12}  {'ratio R':>10}  margin>0")
    for s, wi, pz, ratio, ok in rows:
        print(f"  {s:>6}  {mp.nstr(wi, 6):>12}  {mp.nstr(pz, 6):>12}  {mp.nstr(ratio, 6):>10}  {ok}")
    print(f"\n  sup R over this admissible family = {mp.nstr(best, 6)}  (< 1 => Weil margin positive here)")
    print("  -> this is a one-sided BOUND (sup over the cone {ghat>=0}), the conditional-on-RH")
    print("     extremal inequality -- NOT an identity that forces RH.\n")

    print("=" * 90)
    print("[3] FALSIFIER -- the extremal-function candidate through the three axes\n")
    v = extremal_candidate_falsified()
    for k, val in v.items():
        print(f"  {k:42s}: {val}")
    print("\n  Reading the candidate as the Fourier-optimization BOUND  -> RH-SILENT")
    print("  Reading it as the sharp inequality (= Weil positivity)   -> CIRCULAR")
    print("  Either way it does NOT independently force the zeros on-line: the SAME WALL.\n")

    print("=" * 90)
    print(MODULAR_BET)


if __name__ == "__main__":
    summary()
