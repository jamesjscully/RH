"""rs_pole_radius_probe.py -- PROBE PB / Fork B: does the RANKIN-SELBERG L(s, f x fbar) pole at the
   EDGE fix the EVEN SPLIT (the radius = purity), or does the pole's EXISTENCE already PRESUPPOSE
   Ramanujan (circular)?  Apply the doc-21-sec-4 / BB.1 kill-test (does it do MORE than the FE?) and
   the doc-132 case-C Davenport-Heilbronn (FE-blind) kill-test EXPLICITLY.

  run:  python3 -m scripts.numerics.witness.rs_pole_radius_probe

THE MANDATE (PROBE PB, the global-supplier fork; built on doc 132 Lemma 132.1, sec 6 surviving escape).
  doc 132 killed every BANKED PER-PRIME radius supplier (cases S/C/E) and carved out ONE unrefuted
  escape: a GLOBAL completed-product invariant (Rankin-Selberg / Eisenstein at the pole) whose
  load-bearing input is NOT the per-prime Satake modulus.  This module tests the FIRST named global
  candidate -- the RS pole of L(s, f x fbar) at the edge Re s = k -- against the two standing kill-tests.

  THE PRECISE CLAIM UNDER TEST (doc 132 sec 6, sec 7; GROUND-GB Q3):
    "Rankin-Selberg at the edge presupposes Ramanujan (the even split), it does not fix it zero-free."
  We make this EXACT and runnable in three structural facts, each with a DH control.

WHAT THIS MODULE ESTABLISHES (exact / mpmath; the EDGE = pole vs the SPLIT = convergence dichotomy).

  [A] THE RS POLE LOCATION IS THE EDGE = THE DETERMINANT, RH-INDEPENDENT.
      L(s, f x fbar) = zeta(s-(k-1)) * (Euler factors built from the Satake PRODUCTS a_i(p) a_j(p)).
      Its rightmost pole sits at  s = k  (equivalently the normalized edge), and that pole comes from
      the zeta(s-(k-1)) factor -- i.e. from the DETERMINANT |a(p) b(p)| = p^{k-1} (the diagonal Satake
      product a*b that, summed, IS the harmonic series shifted).  The pole LOCATION is therefore the
      EDGE EXPONENT k-1 = the determinant, which doc 132 / cw_radius_assembly proved is Euler-borne and
      RH-INDEPENDENT (survives the off-Ramanujan plant).  We verify: the pole abscissa is unchanged by
      an off-Ramanujan (uneven-split) plant that PRESERVES the determinant.

  [B] THE BOUND THAT WOULD FORCE THE EVEN SPLIT IS ABSOLUTE CONVERGENCE TO THE RIGHT OF THE EDGE,
      WHICH *IS* RAMANUJAN -- SO RS-AT-THE-EDGE PRESUPPOSES THE SPLIT, IT DOES NOT DELIVER IT.
      The local RS factor at p contributes |a_i(p) a_j(p)| p^{-Re s}.  The product converges absolutely
      for Re s > (edge) IFF max_i |a_i(p)| <= p^{(k-1)/2} for all p -- i.e. IFF the EVEN SPLIT holds.
      The off-Ramanujan plant (|a'| = p^{(k-1)/2+delta}) pushes the TRUE abscissa of absolute
      convergence to k-1 + delta > k-1 -- the determinant pole stays at k-1 but the largest Satake
      product |a'|^2 = p^{k-1+2delta} blows the convergence.  So "the pole is simple at the edge AND
      the series converges to its right" is LOGICALLY EQUIVALENT to the even split.  Knowing the pole is
      AT k-1 (the determinant edge) does NOT know the convergence (the split); the RS analytic
      continuation past the edge is the Ramanujan/purity bound, ASSUMED, not produced.

  [C] THE DH KILL-TEST (doc 132 case C, FE-blind).  Davenport-Heilbronn has a FUNCTIONAL EQUATION but
      NO Euler product.  The RS construction L(s, f x fbar) needs the LOCAL Satake products a_i(p)a_j(p)
      to even be DEFINED -- DH has none, so the RS pole/edge object has EMPTY DOMAIN for DH (same first-
      step death as cw_radius_assembly sec 5).  Meanwhile the only piece of the completed RS object that
      DH does share -- its archimedean Gamma-factor / the FE symmetry -- is the EDGE-symmetry, not the
      split: the FE places the pole at the edge symmetric point and is RH-SILENT (holds for DH's own FE).
      So the RS object splits exactly like every other banked supplier: the EDGE/pole/FE piece is
      DH-shared (RH-silent), the SPLIT/convergence piece needs Ramanujan = RH-for-f and is NOT supplied.

  VERDICT (PROBE PB, RS arm): NO_GO at the radius.  The RS pole supplies the EDGE (determinant /
  abscissa / FE symmetry), exactly like weight-2 Poincare-Serre in doc 132; the EVEN SPLIT (the radius =
  purity) is the absolute-convergence-past-the-edge bound, which IS Ramanujan, PRESUPPOSED not delivered.
  The pole's mere EXISTENCE at the edge is determinant-borne and RH-independent (off-Ramanujan plant
  keeps it); its being a SIMPLE pole with the series convergent to the right is the split = RH.  RS is
  FE-blind at the radius (the doc-21-sec-4 standing kill-test fires): it does not do MORE than reproduce
  the edge-symmetry.  The non-FE-blind datum that WOULD force the split is the per-prime Satake modulus
  bound -- exactly the per-prime purity carrier that doc 132 M2d shows is EMPTY/trivial over Z.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 40

# Ramanujan tau (Delta, weight 12); arithmetic Satake: roots of X^2 - tau(p) X + p^{k-1}.
TAU = {2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738,
       17: -6905934, 19: 10661420, 23: 18643272, 29: 128406630, 31: -52843168}
K = 12  # weight; H^1 weight = k-1 = 11; RS edge at s=k i.e. edge exponent k-1


def satake(p):
    """Arithmetic Satake (alpha,beta): roots of X^2 - tau(p)X + p^{k-1}."""
    a = TAU[p]
    det = p ** (K - 1)
    s = mp.sqrt(mp.mpc(mp.mpf(a) ** 2 - 4 * det))
    return (mp.mpc(a + s) / 2, mp.mpc(a - s) / 2)


def planted_satake(p, delta):
    """Off-Ramanujan plant: SAME determinant a*b=p^{k-1} (edge preserved), uneven moduli
    |a|=p^{(k-1)/2+delta}, |b|=p^{(k-1)/2-delta} (split broken)."""
    half = mp.mpf(K - 1) / 2
    return mp.mpc(mp.mpf(p) ** (half + delta), 0), mp.mpc(mp.mpf(p) ** (half - delta), 0)


# ====================================================================================================
# [A] THE RS POLE LOCATION = THE DETERMINANT EDGE, RH-INDEPENDENT.
#     The pole of L(s, f x fbar) at s=k comes from the diagonal Satake product a(p)b(p)=p^{k-1}
#     (the zeta(s-(k-1)) factor).  Its abscissa is the EDGE EXPONENT = k-1, fixed by the determinant.
# ====================================================================================================

def rs_pole_abscissa_from_determinant(satake_fn, primes):
    """The RS pole sits at the abscissa where sum_p (a(p)b(p)) p^{-s} = sum_p p^{k-1} p^{-s} diverges,
    i.e. at Re s = k.  We read the pole EDGE EXPONENT as the exponent of the DIAGONAL product |a b|:
    edge_exp(p) = log|a(p)b(p)|/log p.  Uniform = k-1 => pole at the determinant edge, RH-free."""
    exps = []
    for p in primes:
        a, b = satake_fn(p)
        exps.append(mp.log(abs(a * b)) / mp.log(p))
    return exps  # all == k-1 = 11 if determinant-borne


# ====================================================================================================
# [B] THE EVEN SPLIT = ABSOLUTE CONVERGENCE TO THE RIGHT OF THE EDGE = RAMANUJAN (PRESUPPOSED).
#     The LARGEST local factor is |a_i(p)|^2 p^{-Re s} (the aa product, not the ab determinant product).
#     True abscissa of absolute convergence = max_p exponent of the LARGEST Satake product.  Even split
#     => that equals the determinant edge k-1; off-split => it exceeds it (k-1+2 delta).
# ====================================================================================================

def true_abs_convergence_abscissa(satake_fn, primes):
    """The abscissa of ABSOLUTE convergence of the full RS Euler product = max over primes of the
    exponent of the LARGEST Satake product |a_i a_j| = (max_i|a_i|)^2.  For the even split this is the
    determinant edge k-1; an off-split plant pushes it ABOVE the edge.  Returns (abscissa_exp, even)."""
    top = []
    for p in primes:
        a, b = satake_fn(p)
        m = max(abs(a), abs(b))
        top.append(mp.log(m * m) / mp.log(p))   # exponent of the top product |a|^2
    abscissa = max(top)
    half_edge = mp.mpf(K - 1)
    even = abs(abscissa - half_edge) < mp.mpf(10) ** (-12)
    return abscissa, even


# ====================================================================================================
# [C] DH KILL-TEST: the RS local Satake products are UNDEFINED for DH (no Euler product).  The only
#     shared piece is the FE/edge symmetry, which is RH-silent.
# ====================================================================================================

def rs_domain_for_dh():
    """DH has NO Euler product => NO local Satake parameters a_i(p) => the RS object L(s, f x fbar)
    cannot be FORMED for DH (the local products are undefined).  The pole/edge construction has EMPTY
    DOMAIN for DH at the first step.  The only completed-RS piece DH shares is the archimedean
    Gamma-factor / FE symmetry s<->edge-s, which is the EDGE symmetry (RH-silent, holds for DH's own
    FE).  Returns the structural verdict."""
    return {
        "DH has Euler product": False,
        "RS local Satake products a_i(p)a_j(p) defined for DH": False,
        "=> RS pole/edge object domain for DH": "EMPTY (undefined at the first step)",
        "only completed-RS piece DH shares": "archimedean Gamma-factor / FE edge-symmetry (RH-silent)",
        "the split (absolute convergence) for DH": "not even formulable (no local moduli)",
    }


# ====================================================================================================
# report
# ====================================================================================================

def report():
    print(__doc__)
    print("=" * 100)
    primes = [p for p in TAU]

    # ---- [A] pole location = determinant edge, RH-independent (off-Ramanujan plant keeps it) --------
    print("[A] RS POLE LOCATION = the DETERMINANT EDGE (exponent k-1), RH-INDEPENDENT.\n")
    exps_true = rs_pole_abscissa_from_determinant(satake, primes)
    pole_uniform = all(abs(e - (K - 1)) < mp.mpf(10) ** (-12) for e in exps_true)
    print(f"    Ramanujan-true Delta:  diagonal-product exponent log|a b|/log p for p={primes[:6]}...:")
    print(f"       {[mp.nstr(e, 8) for e in exps_true[:6]]}")
    print(f"       all == k-1 = {K-1} (pole at the determinant edge): {pole_uniform}")

    plant = lambda p: planted_satake(p, mp.mpf('0.3')) if p == 11 else satake(p)
    exps_plant = rs_pole_abscissa_from_determinant(plant, primes)
    pole_uniform_plant = all(abs(e - (K - 1)) < mp.mpf(10) ** (-12) for e in exps_plant)
    print(f"\n    OFF-RAMANUJAN PLANT at p=11 (delta=0.3, determinant preserved):")
    print(f"       diagonal-product exponent at p=11: {mp.nstr(exps_plant[primes.index(11)], 8)} (still k-1)")
    print(f"       pole still at the edge k-1 for all primes: {pole_uniform_plant}")
    print("    => the RS POLE'S EXISTENCE/LOCATION is the DETERMINANT edge -- Euler-borne, RH-INDEPENDENT")
    print("       (the off-Ramanujan plant breaks the split but the pole stays put).\n")

    # ---- [B] the even split = absolute convergence past the edge = Ramanujan (presupposed) ----------
    print("=" * 100)
    print("[B] THE EVEN SPLIT = ABSOLUTE CONVERGENCE TO THE RIGHT OF THE EDGE = RAMANUJAN (PRESUPPOSED).\n")
    absc_true, even_true = true_abs_convergence_abscissa(satake, primes)
    print(f"    Ramanujan-true Delta: abscissa of ABSOLUTE convergence (top product exponent) "
          f"= {mp.nstr(absc_true, 10)}")
    print(f"       equals the determinant edge k-1={K-1} (even split holds): {even_true}")
    absc_plant, even_plant = true_abs_convergence_abscissa(plant, primes)
    print(f"\n    OFF-RAMANUJAN PLANT at p=11 (delta=0.3): abscissa of absolute convergence "
          f"= {mp.nstr(absc_plant, 10)}")
    print(f"       expected k-1+2*delta = {mp.nstr(mp.mpf(K-1) + 2*mp.mpf('0.3'), 10)} "
          f"(> edge): even split holds: {even_plant}")
    print("    => the pole stays at the EDGE k-1 (det), but the SERIES no longer converges to its right:")
    print("       the true absolute-convergence abscissa MOVED to k-1+2delta.  'Simple pole at the edge")
    print("       AND convergent to its right' <=> the EVEN SPLIT <=> RAMANUJAN.  RS-at-the-edge needs")
    print("       this bound as INPUT (the analytic continuation past the edge IS purity) -- CIRCULAR.\n")

    # ---- [C] DH kill-test --------------------------------------------------------------------------
    print("=" * 100)
    print("[C] DH KILL-TEST (doc 132 case C, FE-blind): RS local products UNDEFINED for DH.\n")
    for k, v in rs_domain_for_dh().items():
        print(f"    {k}: {v}")
    print("\n    => the RS object's discriminating (split) datum is the per-prime Satake MODULUS bound,")
    print("       which DH lacks entirely (no Euler product) and which doc 132 M2d shows is")
    print("       EMPTY/trivial over Z (numerator degree 1).  The DH-shared piece is the FE/edge")
    print("       symmetry = RH-silent.  RS does NOT do MORE than the FE at the radius.\n")

    # ---- verdict -----------------------------------------------------------------------------------
    print("=" * 100)
    print("VERDICT (PROBE PB, Rankin-Selberg arm): NO_GO at the radius.")
    print("  pole_location_is_determinant_edge = True  (RH-independent; off-Ramanujan plant keeps it)")
    print("  split_is_absolute_convergence_past_edge = True  (= Ramanujan, PRESUPPOSED not delivered)")
    print("  rs_does_more_than_FE_at_radius = False  (DH-shared piece is the FE/edge symmetry, RH-silent;")
    print("                                           the split datum is the per-prime modulus DH lacks)")
    print("  => the RS pole supplies the EDGE (determinant/abscissa/FE), exactly like weight-2")
    print("     Poincare-Serre in doc 132; the EVEN SPLIT (radius=purity) is the convergence-past-the-")
    print("     edge bound = Ramanujan = RH-for-f, PRESUPPOSED.  The pole's EXISTENCE presupposes")
    print("     Ramanujan (simple pole + convergence to the right); RS-at-the-edge is CIRCULAR at the")
    print("     radius.  Collapses to FE-blind, the doc-21-sec-4 standing kill-test fires.")

    # machine-readable verdict line for the harness/ledger
    assert pole_uniform and pole_uniform_plant, "pole must stay at determinant edge under plant"
    assert even_true and not even_plant, "split must hold for Ramanujan, break under plant"
    print("\nVERDICT_TAG = RS_POLE_EDGE_NOT_SPLIT__FE_BLIND_AT_RADIUS__NO_GO")


if __name__ == "__main__":
    report()
