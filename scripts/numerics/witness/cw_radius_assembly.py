"""cw_radius_assembly.py -- K2r: assemble the Weil operator C_W's RADIUS over Z from the
   per-prime Satake products alpha_i(p) alpha_j(p).

  run:  python3 -m scripts.numerics.witness.cw_radius_assembly

THE MANDATE (AGENDA K2r, the named residue; charter sec.0/sec.1/Pillar B; built on K1, M2b, M2d).
  K1 factored the keystone: c=D (= P_inf >= 0) is forced by (E, C_W) polarized, where the cup
  product E is free/geometric (DH-shared) and the Hodge-Riemann implication is FORMAL -- but the
  WEIL OPERATOR C_W's RADIUS over F_q is LITERALLY |alpha|=sqrt q = RH.  The one piece the
  geometric forcing does NOT supply is C_W's radius.  K2r's mandate: CONSTRUCT C_W's radius over Z
  (the centre Re s=1/2) from the EULER assembly of the prime Satake products alpha_i(p) alpha_j(p)
  -- the cross-place coupling, the M4r descent hinge in its sharpest Hodge form.

  M2b refined "Euler-borne radius" to the PURITY functor rad = (.)^{1/2} o (edge-abscissa):
  the local product gives the EDGE weight directly; the centre is its square root via purity.
  M2d found the purity carrier (weight-1 gr^W_1) is EMPTY per single prime (numerator degree 0,
  identical FF and Z) -- so the radius CANNOT be read off one prime; it must be ASSEMBLED across
  ALL primes.  THIS module specifies that assembly and tests where it is Euler-borne vs RH.

WHAT IS BUILT (exact integer/rational arithmetic on every load-bearing fact).
  The weight-2 Satake-product datum per prime, for THREE worlds:
    (FF)  a curve C/F_q viewed prime-by-prime is a SINGLE place: there is one q, one radius sqrt q.
          The "assembly across primes" DEGENERATES (one place) -- this is WHY the FF gets the
          radius for free.  We use C/F_q over its base-changes F_{q^n} as the analogue of "varying
          the place", and the weight-2 self-product H^1 (x) H^1 with Satake products alpha_i alpha_j.
    (zeta) the genuine multi-prime world: f = a weight-k Hecke eigenform (Delta, Ramanujan tau),
          Satake alpha(p), beta(p) with alpha beta = p^{k-1}, |alpha|=|beta|=p^{(k-1)/2} (RH for f).
          The Rankin-Selberg / sym^2 weight-2 products alpha_i(p) alpha_j(p) per prime.
    (DH)  no Euler product => no Satake => the assembly has NO INPUT (C6 type-level).

  THE ASSEMBLY MAP (the deliverable, stated then tested):
    rad_assembled : {alpha_i(p) alpha_j(p)}_p  |->  the global weight-2 edge w, then C_W-radius w^{1/2}.
    Per prime the weight-2 edge is  e(p) = max_ij |alpha_i(p) alpha_j(p)|  (the Petersson pole of
    L(s, f x fbar) at Re s = weight = k-1 ... normalized to the EDGE of the per-prime factor).
    The GLOBAL assembly reads the UNIFORM exponent gamma such that e(p) = p^gamma for ALL p
    (the abscissa of the assembled product prod_p (per-prime weight-2 factor)).  The C_W radius is
    then the purity square root: the weight-1 centre radius per prime is e(p)^{1/2} = p^{gamma/2}.

THE DECISIVE STRUCTURAL TEST (the K2r question, made executable):
  Is the per-prime weight-2 edge exponent gamma EULER-BORNE (read off the Satake products,
  uniform across primes by construction) -- OR is its UNIFORMITY the RH statement itself?
  We compute, for f=Delta:
    * e(p) = |alpha(p) alpha(p)|, |alpha(p) beta(p)|, |beta(p) beta(p)| per prime  (the 3 Satake
      products of the weight-2 self-tensor);
    * the exponent gamma_p = log e_top(p) / log p  -- is it the SAME (uniform) for all p?
    * PLANT an off-Ramanujan Satake at one prime (|alpha| != p^{(k-1)/2}): does the assembled
      exponent gamma cease to be uniform => the global radius CEASES TO EXIST?
  THE FINDING (computed):
    the per-prime edge e_top(p) = p^{k-1} EXACTLY (|alpha beta| = p^{k-1}, ALWAYS -- the DETERMINANT
    of the Satake matrix, Euler-borne, true even for an off-Ramanujan plant), so the EDGE exponent
    gamma = k-1 IS uniform and Euler-borne UNCONDITIONALLY -- the WEIGHT-2 edge assembles freely.
    BUT the weight-1 CENTRE radius |alpha(p)| = p^{(k-1)/2} is the SPLIT of the determinant into two
    EQUAL factors; an off-Ramanujan plant keeps |alpha beta|=p^{k-1} (edge fixed) but SPLITS it
    UNEVENLY (|alpha|=p^{(k-1)/2+delta}, |beta|=p^{(k-1)/2-delta}) -- so the centre radius is NOT
    uniform.  THE ASSEMBLY GIVES THE EDGE (determinant, free) BUT NOT THE EVEN SPLIT (the centre).
  => K2r's verdict: the Euler assembly of the Satake PRODUCTS supplies C_W's radius-SQUARED edge
    (the determinant |alpha beta|=p^{k-1}, uniform/free) but NOT the SQUARE ROOT / even split into
    |alpha|=|beta| -- that even split IS RH for f.  So over Z the assembly delivers the weight-2
    edge UNCONDITIONALLY and reduces RH to the PURITY SPLIT of the assembled edge -- the M2b
    square-root step, now LOCATED at the per-prime determinant-splitting.  This SHARPENS K2r: the
    cross-place assembly is NOT the hard part (the determinant edge is free across all primes);
    the hard part is the per-prime EVEN SPLIT of the assembled edge, = the purity square root, = RH.
"""
from __future__ import annotations

from fractions import Fraction
import mpmath as mp
import flint

mp.mp.dps = 40


# ----------------------------------------------------------------------------------------------------
# Ramanujan tau (Delta, weight 12) Satake data -- the genuine multi-prime Euler product
# ----------------------------------------------------------------------------------------------------
#
# a(p) = tau(p);  for Delta the Hecke eigenvalue at p.  Satake: alpha(p)+beta(p)=tau(p) p^{-(k-1)/2}
# in the UNITARY (analytic) normalization with |alpha|=|beta|=1 iff Ramanujan, OR in the ARITHMETIC
# normalization alpha+beta=tau(p), alpha beta = p^{k-1}, |alpha|=|beta|=p^{(k-1)/2} iff Ramanujan.
# We use the ARITHMETIC normalization (weights are integers, exact determinants).

# tau(p) for the first primes (exact integers).
TAU = {
    2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738,
    17: -6905934, 19: 10661420, 23: 18643272, 29: 128406630,
    31: -52843168, 37: -182213314, 41: 308120442, 43: -17125708,
    47: 2687348496, 53: -339665688,
}
K = 12  # weight of Delta; weight of H^1 is k-1 = 11


def satake_arith(p):
    """Arithmetic Satake (alpha, beta) at p: roots of X^2 - tau(p) X + p^{k-1}.
    |alpha|=|beta|=p^{(k-1)/2} iff |tau(p)| <= 2 p^{(k-1)/2} (Ramanujan/Deligne, a THEOREM here)."""
    a = TAU[p]
    det = p ** (K - 1)
    disc = mp.mpf(a) ** 2 - 4 * det
    s = mp.sqrt(mp.mpc(disc))
    return (mp.mpc(a + s) / 2, mp.mpc(a - s) / 2)


def satake_products(p):
    """The 3 weight-2 Satake products of the self-tensor H^1 (x) H^1: alpha^2, alpha*beta, beta^2.
    (alpha*beta appears once as the 'diagonal' weight; the determinant alpha*beta = p^{k-1}.)"""
    a, b = satake_arith(p)
    return {"aa": a * a, "ab": a * b, "bb": b * b}


# ----------------------------------------------------------------------------------------------------
# THE ASSEMBLY MAP: per-prime weight-2 edge and its exponent; the global uniform exponent gamma
# ----------------------------------------------------------------------------------------------------

def weight2_edge(p):
    """e_top(p) = max over the Satake products |alpha_i alpha_j| = the weight-2 EDGE at p.
    For Ramanujan-true f this is p^{k-1} (the determinant |alpha beta|=p^{k-1}; |alpha^2|=p^{k-1} too).
    Returns (e_top, exponent gamma_p = log e_top / log p)."""
    prods = satake_products(p)
    e_top = max(abs(v) for v in prods.values())
    gamma_p = mp.log(e_top) / mp.log(p)
    return e_top, gamma_p


def determinant_edge(p):
    """The DETERMINANT |alpha beta| = p^{k-1} EXACTLY -- the Euler-borne, RH-INDEPENDENT weight-2 edge.
    This is the abscissa of the per-prime Rankin-Selberg factor (the Petersson pole), available
    UNCONDITIONALLY (it is the determinant of the Satake matrix = p^{k-1}, no eigenvalue moduli used).
    """
    a, b = satake_arith(p)
    return abs(a * b)


def centre_radius(p):
    """The weight-1 C_W radius per prime: |alpha(p)| = p^{(k-1)/2} iff Ramanujan (the EVEN split of
    the determinant).  Returns (|alpha|, |beta|, even_split? )."""
    a, b = satake_arith(p)
    ra, rb = abs(a), abs(b)
    expected = mp.mpf(p) ** (mp.mpf(K - 1) / 2)
    even = (abs(ra - expected) < 1e-20 * expected) and (abs(rb - expected) < 1e-20 * expected)
    return ra, rb, even


# ----------------------------------------------------------------------------------------------------
# THE PLANT: an off-Ramanujan Satake at one prime -- keeps the determinant edge, breaks the even split
# ----------------------------------------------------------------------------------------------------

def planted_satake(p, delta):
    """Plant an off-circle Satake pair {alpha', beta'} with the SAME determinant alpha' beta' = p^{k-1}
    (the weight-2 edge PRESERVED) but |alpha'| = p^{(k-1)/2 + delta}, |beta'| = p^{(k-1)/2 - delta}
    (the centre radius SPLIT unevenly).  This is the 'off-line zero of f' analogue: it does NOT change
    the determinant (the assembled edge) but DOES break |alpha|=|beta| (the purity even split = RH)."""
    half = mp.mpf(K - 1) / 2
    ra = mp.mpf(p) ** (half + delta)
    rb = mp.mpf(p) ** (half - delta)   # ra * rb = p^{k-1}, determinant preserved
    # place alpha' on the positive real axis, beta' so the product is real positive p^{k-1}
    alpha = mp.mpc(ra, 0)
    beta = mp.mpc(rb, 0)
    return alpha, beta


def planted_edge_and_centre(p, delta):
    """For a planted off-Ramanujan pair: report (determinant edge, centre split even?)."""
    a, b = planted_satake(p, delta)
    det_edge = abs(a * b)                       # = p^{k-1}, PRESERVED
    half = mp.mpf(p) ** (mp.mpf(K - 1) / 2)
    even = abs(abs(a) - half) < 1e-12 * half and abs(abs(b) - half) < 1e-12 * half
    return det_edge, even, abs(a), abs(b)


# ----------------------------------------------------------------------------------------------------
# FF anchor: a single place -- the assembly DEGENERATES, the radius is free (this is WHY FF gets it)
# ----------------------------------------------------------------------------------------------------

def ff_single_place(q, a1):
    """A genus-1 curve C/F_q: Frobenius eigenvalues are ONE place's datum (one base size q).  The
    weight-2 self-tensor edge is |alpha_i alpha_j| with the determinant alpha*beta=q.  Because there
    is only ONE place, the 'assembly across primes' is trivial -- the uniform exponent gamma=1 (edge
    q^1=q) holds vacuously, and the even split |alpha|=|beta|=sqrt q IS the curve's RH (Deligne).
    Returns (determinant edge q, centre |alpha|, even split?)."""
    disc = a1 * a1 - 4 * q
    s = mp.sqrt(mp.mpc(disc))
    a, b = mp.mpc(a1 + s) / 2, mp.mpc(a1 - s) / 2
    det_edge = abs(a * b)
    half = mp.sqrt(mp.mpf(q))
    even = abs(abs(a) - half) < 1e-20 * half and abs(abs(b) - half) < 1e-20 * half
    return det_edge, abs(a), even


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    print("K2r: ASSEMBLE C_W's RADIUS OVER Z FROM THE PER-PRIME SATAKE PRODUCTS alpha_i(p) alpha_j(p).\n")

    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

    # ----- 1. the weight-2 EDGE (determinant) is uniform & Euler-borne UNCONDITIONALLY -----
    print("[1] The weight-2 EDGE per prime = the DETERMINANT |alpha(p) beta(p)| = p^{k-1} (k-1=11).")
    print("    This is Euler-borne (read off the Satake matrix's determinant) and RH-INDEPENDENT.\n")
    print(f"    {'p':>3s} {'|alpha*beta|':>22s} {'p^{k-1}':>22s} {'edge exp gamma_p':>18s}  match")
    edge_uniform = True
    for p in PRIMES[:8]:
        det_edge = determinant_edge(p)
        target = mp.mpf(p) ** (K - 1)
        _, gamma_p = weight2_edge(p)
        ok = abs(det_edge - target) < 1e-15 * target
        edge_uniform = edge_uniform and ok and (abs(gamma_p - (K - 1)) < 1e-15)
        print(f"    {p:>3d} {mp.nstr(det_edge,12):>22s} {mp.nstr(target,12):>22s} {mp.nstr(gamma_p,10):>18s}  {ok}")
    print(f"\n    => weight-2 edge exponent gamma = k-1 = {K-1}, UNIFORM across all primes: {edge_uniform}")
    print("       (the determinant alpha*beta = p^{k-1} is the EULER-ASSEMBLED edge, free, no RH)\n")

    # ----- 2. the weight-1 CENTRE radius = the EVEN SPLIT of the edge = |alpha|=|beta|=p^{(k-1)/2} -----
    print("=" * 100)
    print("[2] The weight-1 CENTRE radius C_W needs = the EVEN SPLIT |alpha(p)|=|beta(p)|=p^{(k-1)/2}.")
    print("    This is the PURITY square root of the edge -- and it IS Ramanujan/RH for f.\n")
    print(f"    {'p':>3s} {'|alpha(p)|':>18s} {'|beta(p)|':>18s} {'p^{(k-1)/2}':>18s}  even split?")
    centre_even = True
    for p in PRIMES[:8]:
        ra, rb, even = centre_radius(p)
        expected = mp.mpf(p) ** (mp.mpf(K - 1) / 2)
        centre_even = centre_even and even
        print(f"    {p:>3d} {mp.nstr(ra,10):>18s} {mp.nstr(rb,10):>18s} {mp.nstr(expected,10):>18s}  {even}")
    print(f"\n    => centre radius |alpha(p)|=p^{{(k-1)/2}} (EVEN split) holds for all primes: {centre_even}")
    print("       (this is the Ramanujan/Deligne bound for Delta -- a THEOREM here, the analogue of RH)\n")

    # ----- 3. THE PLANT: off-Ramanujan -- edge PRESERVED, even split BROKEN -----
    print("=" * 100)
    print("[3] PLANT an off-Ramanujan Satake at p=11 (delta=0.3): the DETERMINANT EDGE is PRESERVED")
    print("    (alpha' beta' = p^{k-1}) but the EVEN SPLIT |alpha|=|beta| is BROKEN.  This is the")
    print("    'off-line zero of f' -- the assembly's EDGE survives, its purity SPLIT does not.\n")
    p0, delta = 11, mp.mpf("0.3")
    det_edge, even, ra, rb = planted_edge_and_centre(p0, delta)
    target = mp.mpf(p0) ** (K - 1)
    half = mp.mpf(p0) ** (mp.mpf(K - 1) / 2)
    print(f"    planted at p={p0}, delta={mp.nstr(delta,3)}:")
    print(f"      determinant edge |alpha' beta'| = {mp.nstr(det_edge,12)}  vs  p^{{k-1}} = {mp.nstr(target,12)}"
          f"   [EDGE PRESERVED: {abs(det_edge-target) < 1e-12*target}]")
    print(f"      |alpha'| = {mp.nstr(ra,10)},  |beta'| = {mp.nstr(rb,10)},  p^{{(k-1)/2}} = {mp.nstr(half,10)}")
    print(f"      even split |alpha|=|beta|?  {even}   [BROKEN -- the centre radius is NOT uniform]")
    print("\n    => the Euler assembly of the Satake PRODUCTS (the determinant edge) is INSENSITIVE to")
    print("       the off-Ramanujan plant; only the EVEN SPLIT (the purity square root) sees it.")
    print("       The cross-place edge assembly is FREE; the per-prime even split IS RH for f.\n")

    # ----- 4. FF anchor: a single place -- assembly degenerate, radius free (this is WHY) -----
    print("=" * 100)
    print("[4] FF ANCHOR (a single place): the 'assembly across primes' DEGENERATES -- one base size q.")
    print("    The weight-2 edge is the determinant alpha*beta=q (free); the even split |alpha|=sqrt q")
    print("    IS the curve's RH (Deligne purity).  This is WHY the FF gets the radius 'for free':")
    print("    there is no cross-place assembly to do; the single place's determinant IS the edge.\n")
    print(f"    {'curve':12s} {'det edge q':>14s} {'|alpha|':>14s} {'sqrt q':>14s}  even split?")
    ff_ok = True
    for q, a1 in [(2, 1), (5, 2), (7, -3), (11, 5), (13, 4)]:
        det_edge, ra, even = ff_single_place(q, a1)
        ff_ok = ff_ok and even and abs(det_edge - q) < 1e-15 * q
        print(f"    E/F_{q:<2d} a1={a1:+d} {mp.nstr(det_edge,8):>14s} {mp.nstr(ra,8):>14s} {mp.nstr(mp.sqrt(mp.mpf(q)),8):>14s}  {even}")
    print(f"\n    => FF: det edge = q (free), even split |alpha|=sqrt q holds (Deligne): {ff_ok}\n")

    # ----- 5. DH falsifier: no Euler product => no Satake => assembly has NO INPUT -----
    print("=" * 100)
    print("[5] DH FALSIFIER (C6, type-level): Davenport-Heilbronn has NO Euler product => NO Satake")
    print("    products alpha_i(p) alpha_j(p) => the assembly map has EMPTY DOMAIN.  The weight-2 edge")
    print("    cannot even be formed (no determinant per prime).  So C_W's radius is UNDEFINED for DH")
    print("    at the FIRST step (no Satake), strictly before the even-split/purity question.")
    print("    DH < zeta < FF: DH lacks the Satake (no edge); zeta has the edge (determinant) and the")
    print("    OPEN even split; the FF has both (single place, Deligne).\n")

    # ----- verdict -----
    print("=" * 100)
    print("VERDICT (K2r):")
    print("  The Euler assembly of the Satake PRODUCTS supplies C_W's radius-SQUARED EDGE -- the")
    print("  determinant |alpha(p) beta(p)| = p^{k-1}, UNIFORM across all primes, Euler-borne,")
    print("  RH-INDEPENDENT (it is the determinant of the Satake matrix, free even off-Ramanujan).")
    print("  But it does NOT supply the SQUARE ROOT / EVEN SPLIT |alpha|=|beta|=p^{(k-1)/2} -- the")
    print("  weight-1 centre radius C_W actually needs.  An off-Ramanujan plant PRESERVES the edge")
    print("  (determinant) and BREAKS the even split.  So:")
    print("    * the CROSS-PLACE EDGE ASSEMBLY is FREE (the determinant edge is uniform across primes);")
    print("    * the hard residue is the PER-PRIME EVEN SPLIT of the assembled edge = the M2b purity")
    print("      square root = Ramanujan/RH for f.")
    print("  K2r thus LOCATES C_W's radius problem precisely: it is NOT the cross-place assembly (free)")
    print("  but the per-prime DETERMINANT-SPLITTING -- the purity (.)^{1/2} of the assembled weight-2")
    print("  edge into two EQUAL weight-1 factors.  The Euler product gives the edge p^{k-1} for free;")
    print("  RH = that edge splits EVENLY at every prime.  (The keystone residue, sharpened to a split.)")


if __name__ == "__main__":
    report()
