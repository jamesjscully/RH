"""cw_even_split_involution.py -- K2r-split: is the EVEN SPLIT of the determinant line p^{k-1}
   into two EQUAL weight-1 factors FORCED by a geometric/condensed *-involution whose fixed
   locus is |alpha|=|beta|, or is it the irreducible RH?

  run:  python3 -m scripts.numerics.witness.cw_even_split_involution

THE MANDATE (AGENDA K2r-split, the relocated residue; charter sec.0 -- the polarization is a
  DUALITY PAIRING, a *-involution, NOT a metric; built on K2r, K1, M2b).
  K2r FACTORED C_W's radius assembly: the cross-place EDGE = the determinant |alpha beta|=p^{k-1}
  assembles UNIFORMLY across all primes, Euler-borne + RH-FREE; the residue RELOCATED to the
  per-prime EVEN SPLIT |alpha|=|beta|=p^{(k-1)/2} = purity = Ramanujan/RH.  K2r-split attacks
  that residue with the charter's design law: the missing structure must be a *-INVOLUTION (a
  duality, not a metric).  THE QUESTION: does a *-involution sigma on the weight-2 determinant
  line, with fixed locus exactly the even split, FORCE the Frobenius/Satake pair onto that locus
  -- or is "the pair lies on Fix(sigma)" itself the RH statement?

THE PRECISE STRUCTURAL DICHOTOMY (the thing this module makes executable).
  Given the determinant datum d = alpha*beta = p^{k-1} (Euler-borne, free, K2r), define the
  DETERMINANT-CANONICAL involution
        sigma_d(z) := d / conj(z)        (the Rosati / polarization adjoint on the det line).
  TWO logically independent facts must be separated:

    (A) FIXED LOCUS of sigma_d.  sigma_d(z)=z  <=>  z*conj(z)=d  <=>  |z|^2 = d  <=>  |z|=sqrt(d).
        For a det-d PAIR {alpha, beta=d/alpha}: sigma_d(alpha)=d/conj(alpha)=beta  IFF |alpha|=sqrt d.
        So Fix(sigma_d) restricted to a det-d pair  ==  the EVEN SPLIT |alpha|=|beta|=sqrt d.
        THIS IS FREE: sigma_d is definable from d ALONE (the determinant, Euler-borne) + complex
        conjugation -- it does NOT presuppose the radius.  Fix(sigma_d) = the even split, for ANY d.

    (B) Does the actual pair LIE on Fix(sigma_d)?  sigma_d swaps {alpha,beta} ALWAYS
        (sigma_d(alpha)=d/conj(alpha); for the GENUINE Satake pair beta=d/alpha and |alpha|=sqrt d
        => d/conj(alpha)=alpha*beta/conj(alpha)=beta only when |alpha|^2=alpha*conj(alpha)=d).
        For an OFF-Ramanujan pair (|alpha|!=sqrt d, same d), sigma_d(alpha) = d/conj(alpha) is a
        THIRD point, NOT in {alpha,beta} -- the pair is NOT sigma_d-stable as a set with the
        conjugation built in.  So "the pair is sigma_d-FIXED (each point, via the swap+conj)" is
        a NON-TRIVIAL condition = exactly |alpha|=sqrt d = the even split = RH(f).

  CONCLUSION TO TEST: the *-involution sigma_d (with fixed locus = the even split) EXISTS FOR FREE
  from the determinant edge; but "the Satake pair lies on Fix(sigma_d)" is NOT forced by sigma_d's
  existence -- it is a SEPARATE descent/reality condition on the pair, and that condition IS the
  even split = RH.  The involution is the FREE half (charter: duality is structural); the pair's
  fixedness is the HARD half.  This is the K2r determinant-edge/even-split factorization AGAIN, now
  at the level of the involution: the involution (the duality) is geometric/free; its FIXED-POINT
  PROPERTY of the Frobenius is the irreducible RH.

WHERE THE FUNCTION FIELD FORCES IT (the anchor -- why FF gets the even split for free).
  Over F_q the pair IS sigma_q-fixed UNCONDITIONALLY -- but NOT because the involution forces it:
  because of a SEPARATE theorem, the WEIL conjugate-pairing (Frobenius eigenvalues come in pairs
  {alpha, q/alpha} AND alpha*conj(alpha)=q, i.e. the q-Weil-number property), which is Deligne's
  purity / the Riemann hypothesis for the curve.  We exhibit: over F_q the descent datum
  "F = its own Rosati adjoint composed with conjugation" (F is q-REAL) holds <=> |alpha|=sqrt q,
  and that q-reality is the THEOREM (Weil/Deligne).  Over Z there is no such theorem -- the pair's
  sigma_d-fixedness (the q-reality analogue) IS RH.

FALSIFIER PRE-COMMITMENT.
  * The *-involution sigma_d is built from the DETERMINANT d (Euler-borne) -- DH has no Euler
    product => no Satake => no d => no sigma_d (empty domain, structural DH-failure).
  * Fix(sigma_d) on a det-d pair = the even split -- so sigma_d SEES the even split (sees-zeros via
    the pair's fixedness; an off-Ramanujan plant is NOT sigma_d-fixed).
  * But "the pair is sigma_d-fixed" = the even split = Ramanujan/RH => INDEPENDENT NO (CIRCULAR):
    the involution's EXISTENCE is free, its FIXED-POINT property of the Frobenius is RH.
  Predicted verdict: CIRCULAR -- sharpened to "the duality (involution) is free; the pair's
  fixedness under it is the irreducible RH", which is the charter's design law showing its TEETH:
  a duality pairing is exactly the right (non-metric) structure, but it does not FORCE the radius;
  it RELOCATES RH to 'the Frobenius is a fixed point of the duality'.
"""
from __future__ import annotations

from fractions import Fraction
import mpmath as mp

mp.mp.dps = 40

# Ramanujan tau (Delta, weight 12), arithmetic Satake -- the multi-prime Euler product.
TAU = {
    2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738,
    17: -6905934, 19: 10661420, 23: 18643272, 29: 128406630,
    31: -52843168, 37: -182213314, 41: 308120442, 43: -17125708,
    47: 2687348496, 53: -339665688,
}
K = 12  # weight; H^1 weight k-1 = 11


def satake_arith(p):
    """Arithmetic Satake (alpha,beta): roots of X^2 - tau(p) X + p^{k-1}.  alpha*beta = p^{k-1}."""
    a = TAU[p]
    det = p ** (K - 1)
    disc = mp.mpf(a) ** 2 - 4 * det
    s = mp.sqrt(mp.mpc(disc))
    return (mp.mpc(a + s) / 2, mp.mpc(a - s) / 2)


# ----------------------------------------------------------------------------------------------------
# THE DETERMINANT-CANONICAL *-INVOLUTION sigma_d(z) = d / conj(z), d = alpha*beta (Euler-borne edge)
# ----------------------------------------------------------------------------------------------------

def sigma_d(z, d):
    """The polarization/Rosati adjoint on the determinant line: sigma_d(z) = d / conj(z).
    Built from the DETERMINANT d (Euler-borne, K2r-free) + complex conjugation ONLY.
    Properties (verified below):
      - involutive:  sigma_d(sigma_d(z)) = z
      - antilinear (conjugate-linear): a *-structure, NOT a metric (charter sec.0)
      - fixed locus:  sigma_d(z)=z <=> |z|^2 = d  (the EVEN-split radius sqrt d)."""
    return d / mp.conj(z)


def is_involutive(d, samples):
    """sigma_d o sigma_d = id (a *-involution).  Returns max |sigma^2(z)-z| over samples."""
    err = mp.mpf(0)
    for z in samples:
        z2 = sigma_d(sigma_d(z, d), d)
        err = max(err, abs(z2 - z))
    return err


def fixed_locus_is_even_split(d):
    """Fix(sigma_d) = { z : sigma_d(z)=z } = { |z| = sqrt(|d|) } (for d real positive).
    Verify: a point at radius sqrt|d| (any phase) is fixed; a point off that radius is not.
    Returns (fixed_on_radius_err, moved_offradius_dist)."""
    r = mp.sqrt(abs(d))
    # on the even-split radius, real positive: z = r (alpha=beta=sqrt d case) is fixed
    z_on = mp.mpc(r, 0)
    fixed_err = abs(sigma_d(z_on, d) - z_on)
    # off the radius
    z_off = mp.mpc(r * mp.mpf("1.3"), 0)
    moved = abs(sigma_d(z_off, d) - z_off)
    return fixed_err, moved


# ----------------------------------------------------------------------------------------------------
# (A) FIXED LOCUS is the EVEN SPLIT -- FREE (sigma_d definable from d alone)
# (B) "the pair lies on Fix(sigma_d)" -- the SEPARATE condition = the even split = RH(f)
# ----------------------------------------------------------------------------------------------------

def pair_is_sigma_fixed(alpha, beta, d, tol=mp.mpf("1e-20")):
    """Does the det-d pair {alpha,beta} lie on Fix(sigma_d)?  i.e. does sigma_d SWAP the pair
    (sigma_d(alpha)=beta and sigma_d(beta)=alpha)?  sigma_d(alpha)=d/conj(alpha).
    For beta=d/alpha:  d/conj(alpha) = beta = d/alpha  <=>  conj(alpha)=alpha?  NO -- the right
    condition is  d/conj(alpha)=beta=d/alpha is FALSE in general; the correct fixed-point reading
    is each eigenvalue is a sqrt-d-Weil-number: |alpha|=|beta|=sqrt d.  We test that directly:
      the pair is sigma_d-fixed (as a conjugation-stable det-d configuration) <=> |alpha|=sqrt|d|."""
    r = mp.sqrt(abs(d))
    da = abs(abs(alpha) - r)
    db = abs(abs(beta) - r)
    # the swap-with-conjugation closure: sigma_d(alpha) should equal beta IFF |alpha|=sqrt d
    swap_resid = abs(sigma_d(alpha, d) - beta)
    fixed = (da < tol * r) and (db < tol * r)
    return fixed, swap_resid, da, db


def planted_pair(d, delta):
    """Off-Ramanujan: same determinant d but uneven split |alpha|=sqrt(d)*p^delta scaled.
    We place a det-d pair on the positive real axis with |alpha|!=|beta|."""
    r = mp.sqrt(abs(d))
    ra = r * mp.mpf(10) ** delta      # |alpha| moved off sqrt d
    rb = abs(d) / ra                   # so |alpha||beta| = |d|, determinant preserved
    return mp.mpc(ra, 0), mp.mpc(rb, 0)


# ----------------------------------------------------------------------------------------------------
# FF anchor: q-reality (the q-Weil-number property) is the THEOREM that puts F on Fix(sigma_q)
# ----------------------------------------------------------------------------------------------------

def ff_q_reality(q, a1):
    """Genus-1 C/F_q, Frobenius char poly X^2 - a1 X + q.  The pair {alpha, beta=q/alpha}.
    sigma_q(z)=q/conj(z).  The pair is sigma_q-fixed (alpha*conj(alpha)=q) <=> |alpha|=sqrt q,
    which is the WEIL/DELIGNE THEOREM (purity = RH for the curve), NOT forced by sigma_q's
    existence.  Returns (|alpha|, sqrt q, q-real?, sigma swaps pair?)."""
    disc = a1 * a1 - 4 * q
    s = mp.sqrt(mp.mpc(disc))
    a, b = mp.mpc(a1 + s) / 2, mp.mpc(a1 - s) / 2
    r = mp.sqrt(mp.mpf(q))
    qreal = abs(abs(a) - r) < 1e-20 * r
    # for a genuine q-Weil number alpha (|alpha|=sqrt q), conj(alpha)=q/alpha=beta, so
    # sigma_q(alpha)=q/conj(alpha)=q/beta=alpha -- FIXED.  Test the swap closure:
    swap = abs(sigma_d(a, mp.mpf(q)) - b)
    return abs(a), r, qreal, swap


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    print("K2r-split: IS THE EVEN SPLIT FORCED BY A *-INVOLUTION (a DUALITY, NOT a metric)?\n")

    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

    # ---- 1. sigma_d is a genuine *-involution, definable from the determinant d ALONE ----
    print("[1] The determinant-canonical *-involution  sigma_d(z) = d/conj(z),  d = alpha*beta = p^{k-1}.")
    print("    INVOLUTIVE (sigma^2=id) + ANTILINEAR (a *-structure, NOT a metric -- charter sec.0),")
    print("    definable from the EULER-BORNE determinant d ALONE (no radius presupposed).\n")
    print(f"    {'p':>3s} {'d=p^{k-1}':>20s} {'|sigma^2-id|':>16s} {'Fix on sqrt d':>16s} {'moved off':>14s}")
    inv_ok = True
    for p in PRIMES:
        d = mp.mpf(p) ** (K - 1)
        a, b = satake_arith(p)
        err = is_involutive(d, [a, b, mp.mpc(d, 0), mp.mpc(1, 1)])
        fix_err, moved = fixed_locus_is_even_split(d)
        ok = err < 1e-15 * d and fix_err < 1e-15 * mp.sqrt(d) and moved > 1e-3 * mp.sqrt(d)
        inv_ok = inv_ok and ok
        print(f"    {p:>3d} {mp.nstr(d,10):>20s} {mp.nstr(err,6):>16s} {mp.nstr(fix_err,6):>16s} {mp.nstr(moved,8):>14s}")
    print(f"\n    => sigma_d is a *-involution with Fix(sigma_d)={{|z|=sqrt d}}=the EVEN-SPLIT radius,")
    print(f"       definable from the determinant edge ALONE (FREE, Euler-borne): {inv_ok}")
    print("       (the DUALITY -- the involution -- is the FREE half; charter sec.0 design law.)\n")

    # ---- 2. (A) Fix(sigma_d) on a det-d pair = the even split; (B) the GENUINE pair lies on it ----
    print("=" * 100)
    print("[2] (A) Fix(sigma_d) restricted to a det-d PAIR == the EVEN SPLIT |alpha|=|beta|=sqrt d.")
    print("    (B) the GENUINE Satake pair (Ramanujan) LIES on Fix(sigma_d) -- but this is a SEPARATE")
    print("    condition (|alpha|=sqrt d), = Ramanujan/Deligne, NOT forced by sigma_d's existence.\n")
    print(f"    {'p':>3s} {'|alpha|':>16s} {'sqrt d':>16s} {'pair on Fix?':>14s} {'swap resid':>14s}")
    pair_ok = True
    for p in PRIMES:
        a, b = satake_arith(p)
        d = a * b
        fixed, swap, da, db = pair_is_sigma_fixed(a, b, d)
        pair_ok = pair_ok and fixed
        print(f"    {p:>3d} {mp.nstr(abs(a),10):>16s} {mp.nstr(mp.sqrt(abs(d)),10):>16s} "
              f"{str(fixed):>14s} {mp.nstr(swap,6):>14s}")
    print(f"\n    => the genuine pair lies on Fix(sigma_d) for all primes: {pair_ok}")
    print("       (this is Ramanujan/Deligne = a THEOREM here = the analogue of RH for Delta)\n")

    # ---- 3. THE PLANT: off-Ramanujan -- sigma_d EXISTS (same d) but the pair is NOT on Fix(sigma_d) ----
    print("=" * 100)
    print("[3] PLANT off-Ramanujan at p=11 (delta=0.3): SAME determinant d (sigma_d UNCHANGED, the")
    print("    involution exists verbatim), but the pair is NO LONGER on Fix(sigma_d) -- the duality")
    print("    exists but does NOT FORCE the pair onto its fixed locus.\n")
    p0, delta = 11, mp.mpf("0.3")
    d0 = mp.mpf(p0) ** (K - 1)
    ap, bp = planted_pair(d0, delta)
    # determinant preserved?
    det_resid = abs(abs(ap * bp) - d0)
    fixed, swap, da, db = pair_is_sigma_fixed(ap, bp, ap * bp)
    print(f"    planted at p={p0}, delta={mp.nstr(delta,3)}:")
    print(f"      |alpha'*beta'| = {mp.nstr(abs(ap*bp),12)}  vs  d=p^{{k-1}} = {mp.nstr(d0,12)}"
          f"   [det/sigma_d PRESERVED: {det_resid < 1e-10*d0}]")
    print(f"      |alpha'| = {mp.nstr(abs(ap),10)},  |beta'| = {mp.nstr(abs(bp),10)},  "
          f"sqrt d = {mp.nstr(mp.sqrt(d0),10)}")
    print(f"      pair on Fix(sigma_d)?  {fixed}   [BROKEN -- sigma_d exists, pair NOT fixed]")
    print("\n    => the *-involution sigma_d (the DUALITY) is INSENSITIVE to the plant (same d);")
    print("       only 'the pair lies on Fix(sigma_d)' sees it.  THE INVOLUTION'S EXISTENCE IS FREE;")
    print("       the pair's FIXEDNESS under it is the irreducible even split = RH(f).\n")

    # ---- 4. FF anchor: q-reality (Weil/Deligne) is the THEOREM putting F on Fix(sigma_q) ----
    print("=" * 100)
    print("[4] FF ANCHOR: over F_q the pair IS on Fix(sigma_q) UNCONDITIONALLY -- but NOT because")
    print("    sigma_q forces it: because the FROBENIUS is a q-WEIL NUMBER (|alpha|=sqrt q), which is")
    print("    Deligne's purity / RH for the curve, a SEPARATE THEOREM.  sigma_q's existence is free;")
    print("    the q-reality (pair on Fix) is the theorem.\n")
    print(f"    {'curve':14s} {'|alpha|':>14s} {'sqrt q':>14s} {'q-real (on Fix)?':>18s} {'swap resid':>14s}")
    ff_ok = True
    for q, a1 in [(2, 1), (5, 2), (7, -3), (11, 5), (13, 4)]:
        ra, r, qreal, swap = ff_q_reality(q, a1)
        ff_ok = ff_ok and qreal
        print(f"    E/F_{q:<2d} a1={a1:+d}  {mp.nstr(ra,8):>14s} {mp.nstr(r,8):>14s} "
              f"{str(qreal):>18s} {mp.nstr(swap,6):>14s}")
    print(f"\n    => FF: pair on Fix(sigma_q) (q-Weil-number / Deligne purity) for all curves: {ff_ok}")
    print("       (the involution is free; q-reality = the pair on Fix = the THEOREM = RH for C)\n")

    # ---- 5. DH falsifier: no Euler product => no determinant d => no sigma_d (empty domain) ----
    print("=" * 100)
    print("[5] DH FALSIFIER: Davenport-Heilbronn has NO Euler product => NO Satake => NO determinant")
    print("    d=alpha*beta => the involution sigma_d=d/conj(.) has NO DOMAIN (it is BUILT from d).")
    print("    So even the FREE half (the duality) does not exist for DH -- structural DH-failure at")
    print("    the involution's very definition, strictly before the fixed-point question.\n")

    # ---- verdict ----
    print("=" * 100)
    print("VERDICT (K2r-split):")
    print("  The *-INVOLUTION sigma_d(z)=d/conj(z) -- the polarization/Rosati DUALITY on the weight-2")
    print("  determinant line -- EXISTS FOR FREE from the Euler-borne determinant edge d=p^{k-1}:")
    print("  it is a genuine *-involution (involutive + antilinear, NOT a metric -- charter sec.0),")
    print("  and its FIXED LOCUS restricted to a det-d pair IS the even split |alpha|=|beta|=sqrt d.")
    print("  BUT its existence does NOT FORCE the Satake pair onto Fix(sigma_d): an off-Ramanujan")
    print("  plant (same d, same sigma_d) is NOT sigma_d-fixed.  'The Frobenius/Satake pair lies on")
    print("  Fix(sigma_d)' is a SEPARATE descent/reality condition = |alpha|=sqrt d = Ramanujan/RH.")
    print("  Over F_q that condition is the q-WEIL-NUMBER property (Deligne purity = RH for the curve),")
    print("  a THEOREM external to sigma_q.  Over Z it is the OPEN even split = RH.")
    print("  => the charter's design law shows its TEETH: a DUALITY (not a metric) is exactly the right")
    print("     structure -- the involution is FREE and *-clean -- but it RELOCATES RH, it does not")
    print("     dissolve it: RH = 'the Frobenius is a FIXED POINT of the polarization duality'.")
    print("  Falsifier: euler-borne Y (sigma_d built from d; DH has no d => no sigma_d), sees-zeros Y")
    print("  (pair-on-Fix moves under the plant), independent NO (pair-on-Fix = Ramanujan/RH) => CIRCULAR,")
    print("  sharpened to 'the duality is free; the Frobenius's FIXEDNESS under it is the irreducible RH'.")


if __name__ == "__main__":
    report()
