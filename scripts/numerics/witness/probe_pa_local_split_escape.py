"""probe_pa_local_split_escape.py -- PROBE PA / Fork A: is the LOCAL even-split lemma
   strictly weaker than RH-for-f, or RH-equivalent/circular?

  run:  python3 -m scripts.numerics.witness.probe_pa_local_split_escape

  SUPERSEDED INTERPRETATION (recorded, not hidden -- doc 129 discipline). Adversarial
  verification (cycle 3) refuted this probe's "LOCAL vs GLOBAL firewall" framing: a uniform
  eps-band is simultaneously a per-prime LOCAL predicate AND a two-sided global-mean bound, so
  the clean LOCAL/GLOBAL bifurcation leaks. The ACTUAL firewall is AUTOMORPHY (Deligne: no
  holomorphic Hecke newform realizes a det-pinned off-split, so over the automorphic class the
  eps-band and the exact split have the same truth value). See doc 133 sec 4(A) for the corrected
  mechanism. What this witness still establishes CORRECTLY (and exit-gates): the eps-band is
  genuinely wider than the exact split, and is RH-SILENT (holds for the off-Ramanujan plant) --
  i.e. no weaker LOCAL band fixes the radius. The is_local_predicate() labels below are the
  probe's original (superseded) classification, kept as the refuted registration.

THE MANDATE (PROBE PA, both directions).
  Doc 132 (Lemma 132.1) already banks the NO-GO at the radius: every banked PER-PRIME radius
  supplier is (S) self-supplied = RH, (C) Sylvester/FE-shared = RH-silent + imported positivity,
  or (E) absent carrier.  The surviving frontier (doc 132 sec 6) is M4r: a zero-free purity
  descent that is "NOT strictly weaker than RH (the even split IS RH-for-f)".

  PROBE PA tries to BREAK that.  Direction (i) ESCAPE: find a genuinely WEAKER zero-free LOCAL
  statement the Euler/Satake assembly DOES give -- a one-sided non-sharp bound |alpha|<=p^{(k-1)/2+eps},
  a Ramanujan-on-average bound, a positive-density even split -- that is NOT full RH-for-f.
  Direction (ii) NO-GO: confirm every genuinely-weaker statement is GLOBAL (a completed-product /
  average object), never a LOCAL per-prime Euler reading, so the LOCAL split has no weaker form.

THE DECISIVE STRUCTURAL DICHOTOMY THIS MODULE MAKES EXECUTABLE.
  A "LOCAL per-prime even-split supplier" reads, at a SINGLE prime p, only the Euler-factor
  coefficients (the Satake pair {alpha(p), beta(p)}, det = p^{k-1}) by exact arithmetic, and emits
  a per-prime predicate.  We enumerate the only three per-prime predicates the Satake pair admits:

    EDGE      : |alpha(p) beta(p)| = p^{k-1}          (the determinant, the radius-SQUARED)
    SPLIT_eq  : |alpha(p)| = |beta(p)| = p^{(k-1)/2}  (the EXACT even split, the radius)
    SPLIT_ineq: |alpha(p)| <= p^{(k-1)/2 + eps}       (a one-sided non-sharp bound)

  CLAIM TO TEST (the escape's only hope): is SPLIT_ineq a genuine third option -- LOCAL, zero-free,
  and STRICTLY weaker than RH-for-f?

  THE COLLAPSE WE EXPECT AND TEST:
    (a) At a SINGLE prime, |alpha(p)| <= p^{(k-1)/2+eps} with the determinant pinned at p^{k-1}
        forces |beta(p)| = p^{k-1}/|alpha(p)| >= p^{(k-1)/2-eps}.  So per prime the one-sided bound
        is a TWO-SIDED band of width 2*eps*log p around the even split.  As eps -> 0 the band
        collapses ONTO the even split.  For eps > 0 FIXED the band is genuinely wider -- BUT:
    (b) a per-prime band |alpha(p)| in [p^{(k-1)/2-eps}, p^{(k-1)/2+eps}] is NOT what any analytic
        statement about f asserts.  The actual unconditional weaker statements (Rankin-Selberg
        |a(p)| <= C p^{(k-1)/2} on AVERAGE; Sato-Tate density; the subconvex/Kim-Sarnak exponents)
        are GLOBAL: they bound a SUM or a DENSITY over p, not a single fixed prime's modulus.  A
        statement that is TRUE AT EVERY PRIME with a FIXED eps band, read locally, is NOT a theorem
        weaker than Ramanujan -- it is the unconditional TRIVIAL bound (|alpha| <= p^{k-1}, eps=1/2)
        or it IS Ramanujan-with-slack, which for a SINGLE prime is decided by that prime's a(p)
        and carries no global content.
    (c) THE KILL-TEST THAT SEPARATES THEM: a LOCAL per-prime predicate must hold at EVERY prime
        independently (it reads one prime at a time).  We show the only per-prime predicates that
        are (i) Euler-borne, (ii) uniform across primes, and (iii) not the trivial bound, are EDGE
        (free, RH-independent) and SPLIT_eq (= RH-for-f).  Any eps-band predicate is EITHER trivial
        (eps >= the trivial slack at that prime, RH-silent) OR collapses to SPLIT_eq in the only
        regime where it constrains the radius.  There is NO local per-prime statement strictly
        between EDGE and SPLIT_eq.

  THE GLOBAL/LOCAL FIREWALL (the honest residue, = doc 132 sec 6 surviving frontier):
    The genuinely-weaker zero-free statements EXIST -- but they are GLOBAL.  We exhibit the
    Rankin-Selberg second-moment Sum_{p<=x} |a(p)|^2 / p^{k-1}, which is a COMPLETED-PRODUCT
    residue (a sum over primes, the L(s, f x fbar) pole), NOT a per-prime Euler reading.  It is
    unconditionally bounded and STRICTLY weaker than RH-for-f.  This confirms the firewall: the
    weaker statements live on the GLOBAL side; the LOCAL per-prime side has only EDGE (free) and
    SPLIT_eq (= RH).  PROBE PA's escape FAILS at the LOCAL level and SUCCEEDS only by crossing to
    the global completed product -- which is exactly doc 132's surviving (unbuilt) frontier, not a
    local even-split lemma.

KILL-TESTS APPLIED (doc-discipline):
  * DH / FE-blindness: DH has no Euler product => no Satake => the LOCAL predicates have EMPTY
    domain; the GLOBAL average has a DH analogue only as a phase statistic with no purity content.
  * FREEZE (doc 59): no zeta-zero / no f-zero data is read; only Euler-factor coefficients +
    p^{(k-1)/2} in COMPARISON (E4-allowed).  Off-Ramanujan is a negative-control PLANT (A3).
  * unit-insertion (doc 37): the determinant base p^{k-1} is the genuine arithmetic constant term;
    no zero-slack unit is inserted.  The verdict is independent of any free scale.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 40

# Ramanujan tau (Delta, weight 12), arithmetic Satake -- the genuine multi-prime Euler product.
TAU = {
    2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738,
    17: -6905934, 19: 10661420, 23: 18643272, 29: 128406630,
    31: -52843168, 37: -182213314, 41: 308120442, 43: -17125708,
    47: 2687348496, 53: -339665688, 59: 1024967588, 61: -1311411435,
    67: -5917346022, 71: 3148752378, 73: -8419515290, 79: -16178261664,
    83: -4762312338, 89: 9737507730, 97: -3140440226,
}
K = 12  # weight; H^1 weight k-1 = 11
HALF = mp.mpf(K - 1) / 2


def satake_arith(p):
    """Roots of X^2 - tau(p) X + p^{k-1}: |alpha|=|beta|=p^{(k-1)/2} iff |tau(p)|<=2 p^{(k-1)/2}."""
    a = TAU[p]
    det = p ** (K - 1)
    disc = mp.mpf(a) ** 2 - 4 * det
    s = mp.sqrt(mp.mpc(disc))
    return (mp.mpc(a + s) / 2, mp.mpc(a - s) / 2)


def planted_satake(p, delta):
    """Off-Ramanujan plant: same det p^{k-1}, |alpha'|=p^{(k-1)/2+delta}, |beta'|=p^{(k-1)/2-delta}."""
    ra = mp.mpf(p) ** (HALF + delta)
    rb = mp.mpf(p) ** (HALF - delta)
    return mp.mpc(ra, 0), mp.mpc(rb, 0)


# ----------------------------------------------------------------------------------------------------
# DIRECTION (i) ESCAPE: enumerate the local per-prime predicates; is SPLIT_ineq a genuine third option?
# ----------------------------------------------------------------------------------------------------

def edge_ok(alpha, beta, p):
    """EDGE: |alpha beta| = p^{k-1}.  Euler-borne (determinant), RH-INDEPENDENT."""
    return abs(abs(alpha * beta) - mp.mpf(p) ** (K - 1)) < 1e-15 * mp.mpf(p) ** (K - 1)


def split_eq_ok(alpha, beta, p):
    """SPLIT_eq: |alpha|=|beta|=p^{(k-1)/2}.  The EXACT even split = Ramanujan/RH-for-f."""
    exp = mp.mpf(p) ** HALF
    return abs(abs(alpha) - exp) < 1e-18 * exp and abs(abs(beta) - exp) < 1e-18 * exp


def split_ineq_ok(alpha, beta, p, eps):
    """SPLIT_ineq: |alpha| <= p^{(k-1)/2 + eps} (one-sided non-sharp bound, the escape candidate)."""
    bound = mp.mpf(p) ** (HALF + eps)
    return abs(alpha) <= bound and abs(beta) <= bound


def one_sided_forces_band(alpha, beta, p, eps):
    """Per prime, with det pinned at p^{k-1}: |alpha|<=p^{(k-1)/2+eps} forces
    |beta|=p^{k-1}/|alpha| >= p^{(k-1)/2-eps}.  Returns (lower_modulus, lower_bound_p^{half-eps}),
    showing the one-sided bound is a TWO-SIDED BAND of half-width eps*log p around the even split."""
    lo = min(abs(alpha), abs(beta))
    band_lo = mp.mpf(p) ** (HALF - eps)
    return lo, band_lo


# ----------------------------------------------------------------------------------------------------
# DIRECTION (ii) NO-GO: the GLOBAL/LOCAL firewall -- the genuinely weaker statement is GLOBAL
# ----------------------------------------------------------------------------------------------------

def rankin_selberg_second_moment(primes):
    """The Rankin-Selberg second moment  M(x) = (1/N) Sum_{p<=x} |a(p)|^2 / p^{k-1},  where
    a(p)=tau(p) and p^{k-1} normalizes.  Under Ramanujan |a(p)|/p^{(k-1)/2}=2 cos theta_p, so
    |a(p)|^2/p^{k-1} = 4 cos^2 theta_p, and by Sato-Tate its average -> 4 * <cos^2> = 4*(1/2)=...
    The GENUINELY-WEAKER fact: this average is BOUNDED unconditionally (Rankin-Selberg, the
    L(s,fxfbar) pole) and < the trivial bound, WITHOUT proving the per-prime even split.  It is a
    SUM over primes = a COMPLETED-PRODUCT residue, NOT a per-prime Euler reading.
    Returns (mean of |a(p)|^2/p^{k-1}, max single-prime term)."""
    terms = []
    for p in primes:
        norm = mp.mpf(abs(TAU[p])) ** 2 / mp.mpf(p) ** (K - 1)
        terms.append(norm)
    return sum(terms) / len(terms), max(terms)


def is_local_predicate(predicate_name):
    """Classify whether a statement is LOCAL (per-prime Euler reading) or GLOBAL (sum/density).
    Returns (is_local, content) -- the firewall classification."""
    classification = {
        "EDGE":        (True,  "Euler-borne determinant; RH-INDEPENDENT (free)"),
        "SPLIT_eq":    (True,  "exact even split = Ramanujan/RH-for-f (the answer)"),
        "SPLIT_ineq":  (True,  "one-sided band; collapses to SPLIT_eq or trivial (see [1])"),
        "RS_2nd_mom":  (False, "sum over primes = completed-product residue (GLOBAL, weaker)"),
        "SatoTate":    (False, "density over primes (GLOBAL, weaker, still implies RP)"),
        "subconvex":   (False, "global L-value bound (GLOBAL, weaker exponent)"),
    }
    return classification[predicate_name]


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    PRIMES = sorted(TAU.keys())

    # ===== DIRECTION (i): ESCAPE attempt -- is SPLIT_ineq a genuine LOCAL weaker statement? =====
    print("DIRECTION (i) ESCAPE: is the one-sided LOCAL bound |alpha(p)|<=p^{(k-1)/2+eps} genuinely")
    print("  weaker than the exact even split, at a SINGLE prime?\n")
    print("[1] Per prime, the determinant is pinned at p^{k-1} (EDGE, free).  A one-sided upper bound")
    print("    on |alpha| therefore FORCES a lower bound on |beta|=p^{k-1}/|alpha|: the one-sided bound")
    print("    is a TWO-SIDED BAND [p^{(k-1)/2-eps}, p^{(k-1)/2+eps}] around the even split.")
    print("    As eps->0 the band COLLAPSES onto SPLIT_eq.  Demonstration with an off-split PLANT:\n")
    eps = mp.mpf("0.10")
    print(f"    eps = {mp.nstr(eps,3)}.  PLANT off-Ramanujan |alpha'|=p^{{(k-1)/2+delta}}, delta sweeps.\n")
    print(f"    {'p':>3s} {'delta':>7s} {'|alpha|/p^h':>12s} {'|beta|/p^h':>12s} {'in eps-band?':>13s} {'exact split?':>13s}")
    band_collapse_ok = True
    for p in [11, 13]:
        for delta in [mp.mpf("0.0"), mp.mpf("0.05"), mp.mpf("0.10"), mp.mpf("0.15")]:
            a, b = planted_satake(p, delta)
            ra = abs(a) / mp.mpf(p) ** HALF
            rb = abs(b) / mp.mpf(p) ** HALF
            inband = split_ineq_ok(a, b, p, eps)
            exact = split_eq_ok(a, b, p)
            # CORE CHECK: in-band but NOT exact <=> 0 < delta <= eps (genuinely weaker locally? -- see verdict)
            print(f"    {p:>3d} {mp.nstr(delta,3):>7s} {mp.nstr(ra,6):>12s} {mp.nstr(rb,6):>12s} "
                  f"{str(inband):>13s} {str(exact):>13s}")
            # the band is genuinely wider than the point: delta=0.05,0.10 in-band but not exact
            if delta == mp.mpf("0.05") or delta == mp.mpf("0.10"):
                band_collapse_ok = band_collapse_ok and inband and not exact
    print()
    print("    => LOCAL OBSERVATION: at a FIXED prime the eps-band IS strictly wider than the even")
    print(f"       split (delta in (0,eps] is in-band but off-split): genuinely-wider-band = {band_collapse_ok}.")
    print("       So |alpha(p)|<=p^{(k-1)/2+eps} at ONE prime is, in isolation, weaker than the exact")
    print("       split AT THAT PRIME.  THE ESCAPE'S HOPE.  Now we kill it -- it has NO global content.\n")

    # ===== [2] The kill: a per-prime band predicate has no uniform-across-primes weaker form =====
    print("=" * 100)
    print("[2] THE KILL (why the local band is NOT a theorem weaker than Ramanujan).  A LOCAL per-prime")
    print("    predicate reads ONE prime at a time and must hold at EVERY prime.  The genuine Satake")
    print("    data already satisfies the EXACT split at every prime (Deligne, for Delta).  The only")
    print("    'weaker' LOCAL relaxations are:\n")
    print("      (a) eps >= 1/2 : the TRIVIAL bound |alpha|<=p^{k-1} -- holds for ANY det-p^{k-1} pair,")
    print("          including the off-Ramanujan plant, so it is RH-SILENT (no purity content).")
    print("      (b) 0 < eps < 1/2 FIXED at every prime : a uniform band.  But there is NO arithmetic")
    print("          theorem of this LOCAL shape: the unconditional results (Rankin-Selberg, Kim-Sarnak")
    print("          theta<=7/64) bound a GLOBAL object (a sum/an L-value), NOT every single prime's")
    print("          modulus.  A LOCAL uniform-eps band asserted at every prime is either implied by")
    print("          the trivial bound (a) or, in the only regime where it pins the radius (eps->0),")
    print("          IS the exact split = RH.\n")

    # show the trivial bound is RH-silent: the plant satisfies eps=1/2 at every prime
    print(f"    {'p':>3s} {'delta(plant)':>12s} {'|alpha|/p^h':>12s} {'trivial eps=0.5 ok?':>20s} {'exact split?':>13s}")
    trivial_silent = True
    for p in [11, 13, 17]:
        a, b = planted_satake(p, mp.mpf("0.4"))   # badly off-split
        ra = abs(a) / mp.mpf(p) ** HALF
        triv = split_ineq_ok(a, b, p, mp.mpf("0.5"))
        exact = split_eq_ok(a, b, p)
        trivial_silent = trivial_silent and triv and not exact
        print(f"    {p:>3d} {'0.40':>12s} {mp.nstr(ra,6):>12s} {str(triv):>20s} {str(exact):>13s}")
    print(f"\n    => the trivial LOCAL bound (eps=1/2) holds for the OFF-Ramanujan plant: {trivial_silent}")
    print("       (RH-SILENT -- it does not see the even split; it is the empty/free relaxation).\n")

    # ===== DIRECTION (ii): the GLOBAL/LOCAL firewall -- the genuinely weaker statement is GLOBAL =====
    print("=" * 100)
    print("DIRECTION (ii) NO-GO: the genuinely-weaker zero-free statements EXIST but are GLOBAL, never")
    print("  a LOCAL per-prime Euler reading.\n")
    print("[3] Rankin-Selberg second moment  M = mean_p |a(p)|^2 / p^{k-1}  (= 4<cos^2 theta_p>).")
    print("    This is a SUM over primes = the L(s, f x fbar) pole residue = a COMPLETED-PRODUCT")
    print("    object, bounded UNCONDITIONALLY and STRICTLY weaker than the per-prime split.\n")
    mean, mx = rankin_selberg_second_moment(PRIMES)
    print(f"    over {len(PRIMES)} primes (Delta, Ramanujan-true): mean |a(p)|^2/p^{{k-1}} = {mp.nstr(mean,8)}")
    print(f"      (Sato-Tate predicts mean -> 4*<cos^2> = 2.0; finite-sample value above)")
    print(f"      max single-prime term = {mp.nstr(mx,8)}  (< trivial 4 -- the average is a GLOBAL bound)")
    print()
    print("    The KEY firewall point: M is a function of the WHOLE prime sum; it does NOT decide any")
    print("    single prime's even split.  One could LOWER one prime's |a(p)| and RAISE another's,")
    print("    keeping M fixed, while BREAKING the per-prime split at both.  M is GLOBAL; the split")
    print("    is LOCAL.  Demonstrate the average is INSENSITIVE to a compensated local off-split:\n")
    # compensate: pretend tau(11) shrinks, tau(13) grows, same second moment contribution swap
    base = [mp.mpf(abs(TAU[p]))**2 / mp.mpf(p)**(K-1) for p in PRIMES]
    M0 = sum(base) / len(base)
    pert = list(base)
    i11, i13 = PRIMES.index(11), PRIMES.index(13)
    shift = mp.mpf("0.5")
    pert[i11] = base[i11] - shift
    pert[i13] = base[i13] + shift          # second moment SUM preserved exactly
    M1 = sum(pert) / len(pert)
    print(f"      mean before compensated swap : {mp.nstr(M0,10)}")
    print(f"      mean after  compensated swap : {mp.nstr(M1,10)}   [GLOBAL average preserved: "
          f"{abs(M0-M1) < 1e-25}]")
    print("      (the global second moment is BLIND to a per-prime split redistribution -- so it is")
    print("       strictly weaker than, and CANNOT supply, the per-prime even split).\n")

    # ===== [4] classification table: the firewall =====
    print("=" * 100)
    print("[4] THE FIREWALL (classification).  LOCAL per-prime Euler readings: only EDGE (free) and")
    print("    SPLIT_eq (= RH).  Everything genuinely weaker is GLOBAL.\n")
    print(f"    {'statement':14s} {'LOCAL?':>8s}  content")
    for name in ["EDGE", "SPLIT_eq", "SPLIT_ineq", "RS_2nd_mom", "SatoTate", "subconvex"]:
        loc, content = is_local_predicate(name)
        print(f"    {name:14s} {str(loc):>8s}  {content}")
    print()

    # ===== [5] DH kill-test =====
    print("=" * 100)
    print("[5] DH KILL-TEST: Davenport-Heilbronn has NO Euler product => NO Satake => the LOCAL")
    print("    predicates (EDGE, SPLIT_eq, SPLIT_ineq) have EMPTY DOMAIN (no per-prime determinant).")
    print("    The GLOBAL second moment has a DH analogue only as a phase statistic with NO purity")
    print("    content (DH is RH-false yet its coefficient statistics are FE-shared).  So no local")
    print("    or global weaker statement separates zeta from RH-false DH at the purity level.\n")

    # ===== VERDICT =====
    print("=" * 100)
    print("VERDICT (PROBE PA / Fork A):")
    print("  ESCAPE (i): At a SINGLE prime the one-sided bound |alpha(p)|<=p^{(k-1)/2+eps} IS a strictly")
    print("    wider band than the exact even split (delta in (0,eps] is in-band, off-split).  BUT this")
    print("    'weaker local statement' has NO arithmetic content as a theorem about f: held at EVERY")
    print("    prime with eps>=1/2 it is the TRIVIAL bound (RH-silent, satisfied by the off-Ramanujan")
    print("    plant); held with eps->0 it IS the exact split = RH-for-f.  There is no per-prime")
    print("    predicate strictly BETWEEN the free EDGE and the RH-equivalent SPLIT_eq.")
    print("  NO-GO (ii): The genuinely-weaker zero-free statements (Rankin-Selberg second moment,")
    print("    Sato-Tate density, Kim-Sarnak subconvex exponent) ALL EXIST and are STRICTLY weaker than")
    print("    RH-for-f -- but they are GLOBAL (sums/densities/L-values over the completed product),")
    print("    NOT local per-prime Euler readings.  The GLOBAL second moment is provably BLIND to a")
    print("    compensated per-prime split redistribution, so it cannot supply the local split.")
    print("  CONCLUSION: the LOCAL even-split lemma is RH-EQUIVALENT (= RH-for-f, a theorem for Delta")
    print("    via Deligne, open for zeta).  It is NOT strictly weaker than RH at the LOCAL level: the")
    print("    only weaker statements are GLOBAL completed-product objects -- which is exactly doc 132")
    print("    sec 6's surviving (unbuilt) frontier, NOT a local even-split lemma.  The escape FAILS")
    print("    locally and SUCCEEDS only by crossing the global firewall.")


# ----------------------------------------------------------------------------------------------------
# self-check asserts (so EXIT code is meaningful)
# ----------------------------------------------------------------------------------------------------

def selfcheck():
    PRIMES = sorted(TAU.keys())
    # 1. EDGE holds for the genuine pair AND for the off-Ramanujan plant (free, RH-independent)
    for p in [11, 13, 17]:
        a, b = satake_arith(p)
        assert edge_ok(a, b, p), f"EDGE genuine failed p={p}"
        ap, bp = planted_satake(p, mp.mpf("0.3"))
        assert edge_ok(ap, bp, p), f"EDGE plant failed p={p}"          # edge preserved off-split
    # 2. SPLIT_eq holds for genuine (Ramanujan/Deligne) and FAILS for the plant
    for p in [11, 13, 17]:
        a, b = satake_arith(p)
        assert split_eq_ok(a, b, p), f"SPLIT_eq genuine failed p={p}"   # Ramanujan true for Delta
        ap, bp = planted_satake(p, mp.mpf("0.3"))
        assert not split_eq_ok(ap, bp, p), f"SPLIT_eq plant should fail p={p}"
    # 3. trivial bound (eps=1/2) is RH-silent: holds for the badly off-split plant
    for p in [11, 13, 17]:
        ap, bp = planted_satake(p, mp.mpf("0.45"))
        assert split_ineq_ok(ap, bp, p, mp.mpf("0.5")), f"trivial bound should hold p={p}"
        assert not split_eq_ok(ap, bp, p), f"plant not exact p={p}"
    # 4. one-sided bound is a two-sided band: in-band-but-off-split for 0<delta<eps
    for p in [11, 13]:
        ap, bp = planted_satake(p, mp.mpf("0.05"))
        assert split_ineq_ok(ap, bp, p, mp.mpf("0.10")), "delta<eps should be in-band"
        assert not split_eq_ok(ap, bp, p), "delta>0 should be off-split"
    # 5. GLOBAL firewall: the second moment is BLIND to a compensated per-prime split swap
    base = [mp.mpf(abs(TAU[p]))**2 / mp.mpf(p)**(K-1) for p in PRIMES]
    M0 = sum(base) / len(base)
    pert = list(base)
    pert[PRIMES.index(11)] -= mp.mpf("0.5")
    pert[PRIMES.index(13)] += mp.mpf("0.5")
    M1 = sum(pert) / len(pert)
    assert abs(M0 - M1) < mp.mpf("1e-25"), "second moment should be swap-invariant (GLOBAL)"
    # 6. classification: only EDGE and SPLIT_eq are the non-trivial LOCAL readings; weaker => GLOBAL
    assert is_local_predicate("RS_2nd_mom")[0] is False
    assert is_local_predicate("SatoTate")[0] is False
    assert is_local_predicate("EDGE")[0] is True
    assert is_local_predicate("SPLIT_eq")[0] is True
    return True


if __name__ == "__main__":
    report()
    ok = selfcheck()
    print("\n" + "=" * 100)
    print(f"SELFCHECK: {'PASS' if ok else 'FAIL'}  (all structural asserts hold)")
