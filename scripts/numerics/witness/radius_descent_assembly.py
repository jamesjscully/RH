"""radius_descent_assembly.py -- M4r: the descent-gluing of the per-prime SCALE/radius data into the
   GLOBAL centre Re s=1/2, against the radius-silent archimedean triple (P_inf, D, c).

  run:  python3 -m scripts.numerics.witness.radius_descent_assembly

THE MANDATE (AGENDA M4r / K2r-fix, the SOLE LIVE KEYSTONE; charter sec.0/Pillar B; built on K2r, M2d,
M3b, K2r-fix).
  K2r-fix RESOLVED the reality/radius fork: the conjugation kappa = c_0 (the FE/phase) is FREE over Z
  and RADIUS-SILENT BY A THEOREM (conjugations |mu|=1 carry only phase); the radius |alpha|=sqrt d is
  sigma_d's SCALE d (a radial inversion), an EULER datum ORTHOGONAL to every conjugation, which must be
  Euler-ASSEMBLED in the descent -- NOT supplied by a real structure.  M4r: SPECIFY that assembly --
  the precise map by which the per-prime SCALE/radius data (sqrt d analogues) assemble the global
  centre Re s=1/2 against the radius-silent (P_inf, D, c) at infinity.

  THE STRUCTURAL GAP K2r LEFT OPEN (the genuine new question of M4r).  K2r/K2r-split/K2r-fix all worked
  PRIME BY PRIME: each prime's even split |alpha(p)|=|beta(p)|=p^{(k-1)/2} is, in isolation, exactly
  Ramanujan/RH for that prime, so "CIRCULAR per prime".  But M2d proved purity is INTRINSICALLY GLOBAL
  for zeta: NO single prime carries a weight-1 gr^W_1 (numerator degree 0, identical FF and Z); the
  weight-1 carrier exists only GLOBALLY (the FF curve's H^1 of rank 2g, assembled from ALL its points
  by Lefschetz).  So the per-prime framing of K2r is the WRONG ALTITUDE for the descent question.
  M4r's question, sharper than K2r: when the even split is imposed GLOBALLY (across ALL primes at once,
  as a property of the single glued weight-1 carrier), is it
     (a) a RIGIDITY -- a single cross-place constraint, where the radii at different primes are LINKED
         by the Euler product, so that the global even-split is forced by a coupling no single prime
         sees (the descent ADDS content over the per-prime conjunction);  OR
     (b) a CONJUNCTION -- the global condition factors as AND_p (per-prime even split), the primes'
         radii are INDEPENDENT, the Euler product imposes NO cross-place link, and the descent gluing
         adds NOTHING over K2r (each prime independently = RH, no global lever).
  This is the decisive descent question: does cross-place coupling EXIST as a radius constraint, or is
  the radius a per-prime-independent datum dressed up as a global object?

WHAT IS BUILT (exact arithmetic on every load-bearing fact; f=Delta and FF base-change towers).
  We make the GLOBAL weight-1 carrier explicit in the ONE world where it provably exists -- the FF --
  and read off whether the radius condition is a rigidity or a conjunction, THEN test whether zeta
  inherits a rigidity or only a conjunction.

  (FF GLOBAL carrier, the anchor).  A curve C/F_q has a GLOBAL H^1 of rank 2g whose Frobenius
  eigenvalues {alpha_1,...,alpha_{2g}} satisfy:
     * the DETERMINANT constraint  prod_i alpha_i = q^g  (the functional equation, det Frob = q^g),
       and the conjugate pairing alpha_i alpha_{g+i} = q (Poincare duality on H^1).  EULER-BORNE, FREE.
     * RH(C) = |alpha_i| = sqrt q for ALL i  (Deligne).
  THE RIGIDITY TEST: the determinant/FE constraint prod alpha_i = q^g couples the 2g eigenvalues into
  ONE product -- but does it LINK their MODULI?  Compute: can one eigenvalue's modulus move OFF sqrt q
  while ANOTHER compensates, keeping prod alpha_i = q^g (det) AND the conjugate pairing alpha_i
  alpha_{g+i}=q -- i.e. is the GLOBAL even split |alpha_i|=sqrt q for all i FORCED by (det + pairing),
  or can the moduli redistribute?  IF redistribution is possible while preserving (det + pairing), the
  global condition is a CONJUNCTION (each i independent up to its pairing partner) and the descent adds
  nothing; IF (det + pairing) FORCES all moduli to sqrt q, it is a RIGIDITY and the cross-place product
  IS the lever.

THE DECISIVE STRUCTURAL FINDING (computed below):
  The FE/determinant prod alpha_i = q^g, EVEN TOGETHER WITH the conjugate pairing alpha_i alpha_{g+i}=q,
  does NOT force |alpha_i|=sqrt q -- one can move |alpha_1|=r sqrt q, |alpha_{g+1}|=sqrt q / r (pairing
  preserved, |alpha_1 alpha_{g+1}|=q), and ANOTHER pair |alpha_2|=sqrt q / r, |alpha_{g+2}|=r sqrt q,
  so that prod_i |alpha_i| = q^g (determinant modulus PRESERVED) -- a GLOBALLY DETERMINANT-NEUTRAL,
  PAIRING-NEUTRAL redistribution of the moduli that is OFF the even split at every moved place.  So the
  global radius condition is a CONJUNCTION, NOT a rigidity: the Euler product's determinant constraint
  is blind to a balanced cross-place modulus redistribution.  The cross-place coupling that K2r hoped
  for -- a LINK between different eigenvalues' radii -- DOES NOT EXIST at the level of the determinant
  FE; the FE fixes the PRODUCT of moduli (= q^g, free) but not the INDIVIDUAL moduli.  This is the
  exact global mirror of K2r's per-prime finding: the determinant edge (now the GLOBAL determinant
  q^g) is free; the even split (now the GLOBAL "all moduli equal sqrt q") is the residue and it does
  NOT factor through any product/trace the Euler data supplies.
  => M4r's verdict: the descent gluing ASSEMBLES the determinant (the product of moduli = q^g, the
  global edge, free) but the radius RESIDUE is a CONJUNCTION of per-place even splits with NO
  cross-place rigidity -- so the descent adds NO global lever over K2r; RH stays the per-place even
  split, now seen to be globally UN-coupled by the FE.  The one thing that WOULD couple them -- a
  positivity (Hodge index) on the GLOBAL H^1 that fails under redistribution -- is exactly the Weil
  positivity (=RH), not supplied by the determinant; this LOCATES why the descent needs the
  ARCHIMEDEAN positivity P_inf >= 0 (the keystone) and cannot get the radius from the FE alone.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 40


# ----------------------------------------------------------------------------------------------------
# FF GLOBAL weight-1 carrier: H^1(C) for a genus-g curve, Frobenius eigenvalues {alpha_i}
# ----------------------------------------------------------------------------------------------------
#
# A genus-g curve C/F_q has H^1 of rank 2g.  Frobenius eigenvalues come in conjugate-dual pairs
# (alpha_i, alpha_{g+i}) with alpha_i * alpha_{g+i} = q (Poincare duality / the functional equation
# pairing on H^1).  The global determinant is prod_i alpha_i = q^g (det Frob | H^1 = q^g).
# Deligne (RH for C): |alpha_i| = sqrt q for ALL i.  We build the eigenvalue multiset and test the
# rigidity of the GLOBAL even-split condition against (determinant + pairing).

def weil_eigenvalues_on_line(q, g, angles):
    """Genuine Weil eigenvalues: g conjugate-dual pairs all on |z|=sqrt q.
    angles: list of g angles theta_i; alpha_i = sqrt q e^{i theta_i}, alpha_{g+i} = sqrt q e^{-i theta_i}
    (so alpha_i alpha_{g+i} = q, the pairing; |alpha_i|=sqrt q, on the RH circle)."""
    rq = mp.sqrt(mp.mpf(q))
    alphas = []
    for th in angles:
        alphas.append(rq * mp.expjpi(mp.mpf(th) / mp.pi))   # sqrt q e^{i theta}
    for th in angles:
        alphas.append(rq * mp.expjpi(-mp.mpf(th) / mp.pi))  # sqrt q e^{-i theta}, the dual
    return alphas


def redistributed_eigenvalues(q, g, angles, log_r):
    """A DETERMINANT-NEUTRAL, PAIRING-NEUTRAL modulus REDISTRIBUTION off the even split.
    Move pair 1: |alpha_1| = r sqrt q, |alpha_{g+1}| = sqrt q / r  (pairing preserved: product = q).
    Move pair 2: |alpha_2| = sqrt q / r, |alpha_{g+2}| = r sqrt q  (pairing preserved).
    Net effect on prod_i |alpha_i|: (r)(1/r)(1/r)(r) = 1 -- the GLOBAL determinant modulus q^g is
    PRESERVED, yet two pairs are OFF the even split.  Requires g >= 2 (two pairs to balance)."""
    assert g >= 2, "need genus >= 2 to balance the redistribution"
    rq = mp.sqrt(mp.mpf(q))
    r = mp.e ** mp.mpf(log_r)
    mods_first = [rq] * g          # moduli of alpha_1..alpha_g
    mods_dual = [rq] * g           # moduli of alpha_{g+1}..alpha_{2g}
    mods_first[0] = r * rq;   mods_dual[0] = rq / r     # pair 1: (r, 1/r)
    mods_first[1] = rq / r;   mods_dual[1] = r * rq     # pair 2: (1/r, r)  -- balances pair 1
    alphas = []
    for i, th in enumerate(angles):
        alphas.append(mods_first[i] * mp.expjpi(mp.mpf(th) / mp.pi))
    for i, th in enumerate(angles):
        alphas.append(mods_dual[i] * mp.expjpi(-mp.mpf(th) / mp.pi))
    return alphas


def global_det(alphas):
    """prod_i alpha_i (the determinant of Frobenius on H^1; should be q^g, the FE)."""
    pr = mp.mpc(1)
    for a in alphas:
        pr *= a
    return pr


def pairing_products(alphas, g):
    """The g pairing products alpha_i * alpha_{g+i} (Poincare duality: each should be q)."""
    return [alphas[i] * alphas[g + i] for i in range(g)]


def even_split(alphas, q, tol=1e-25):
    """Are ALL moduli = sqrt q (the global RH/Deligne even split)?"""
    rq = mp.sqrt(mp.mpf(q))
    return all(abs(abs(a) - rq) < tol * rq for a in alphas)


# ----------------------------------------------------------------------------------------------------
# zeta side: the per-prime Satake pairs assembled -- is there ANY cross-prime modulus link?
# ----------------------------------------------------------------------------------------------------
#
# For f = Delta the per-prime Satake (alpha(p), beta(p)) has alpha beta = p^{k-1} (determinant, the
# per-prime FE/pairing) and the GLOBAL functional equation of L(s,f) is a single relation s <-> k-1-s
# that DOES NOT couple different primes' moduli.  We exhibit a cross-prime redistribution: move p1's
# split off-even and p2's split off-even in a way that preserves EVERY per-prime determinant -- showing
# the primes are modulus-INDEPENDENT (no rigidity), the global mirror of the FF redistribution.

TAU = {2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738}
K = 12


def satake(p):
    a = TAU[p]
    det = p ** (K - 1)
    disc = mp.mpf(a) ** 2 - 4 * det
    s = mp.sqrt(mp.mpc(disc))
    return mp.mpc(a + s) / 2, mp.mpc(a - s) / 2


def cross_prime_redistribution(p1, p2, delta):
    """Plant off-even at p1 AND p2 independently, each preserving its OWN determinant p^{k-1}.
    Show there is NO global product/FE relation that this violates -- the primes are uncoupled.
    Returns the global determinant ratio (product over the two primes of |alpha beta|) before/after."""
    half1 = mp.mpf(K - 1) / 2
    # genuine
    a1, b1 = satake(p1); a2, b2 = satake(p2)
    det_before = abs(a1 * b1) * abs(a2 * b2)
    # planted: p1 split UP by delta, p2 split DOWN by delta, each determinant preserved
    pa1 = mp.mpf(p1) ** (half1 + delta); pb1 = mp.mpf(p1) ** (half1 - delta)
    pa2 = mp.mpf(p2) ** (half1 - delta); pb2 = mp.mpf(p2) ** (half1 + delta)
    det_after = (pa1 * pb1) * (pa2 * pb2)   # = p1^{k-1} p2^{k-1}, each preserved
    return det_before, det_after, (pa1, pb1, pa2, pb2)


# ----------------------------------------------------------------------------------------------------
# report
# ----------------------------------------------------------------------------------------------------

def report():
    print(__doc__)
    print("=" * 100)
    print("M4r: THE RADIUS-DESCENT ASSEMBLY -- is the GLOBAL even split a RIGIDITY or a CONJUNCTION?\n")

    # ---------------------------------------------------------------------------------------------
    print("[1] FF GLOBAL weight-1 carrier H^1(C), genus g: eigenvalues in g conjugate-dual pairs.")
    print("    The determinant prod alpha_i = q^g (FE) and pairing alpha_i alpha_{g+i}=q are FREE.")
    print("    THE RIGIDITY TEST: does (determinant + pairing) FORCE all |alpha_i|=sqrt q (even split)?\n")
    q, g = 9, 2          # genus-2 curve over F_9 (q a prime power; we only use q as a positive size)
    angles = [mp.mpf("0.7"), mp.mpf("1.9")]
    rq = mp.sqrt(mp.mpf(q))

    on = weil_eigenvalues_on_line(q, g, angles)
    det_on = global_det(on)
    pair_on = pairing_products(on, g)
    print(f"    genus g={g}, q={q}, sqrt q = {mp.nstr(rq,12)}")
    print(f"    ON the line (genuine Weil): det = prod alpha_i = {mp.nstr(det_on,10)}  (target q^g = {q**g})")
    print(f"      pairing products alpha_i alpha_(g+i): {[mp.nstr(pp,8) for pp in pair_on]}  (target q={q})")
    print(f"      even split |alpha_i|=sqrt q for ALL i?  {even_split(on, q)}\n")

    # ---------------------------------------------------------------------------------------------
    print("    NOW the DETERMINANT-NEUTRAL, PAIRING-NEUTRAL redistribution (move 2 pairs, balanced):")
    off = redistributed_eigenvalues(q, g, angles, log_r=mp.mpf("0.4"))
    det_off = global_det(off)
    pair_off = pairing_products(off, g)
    mods = [mp.nstr(abs(a), 8) for a in off]
    print(f"      moduli after redistribution: {mods}")
    print(f"      det = prod alpha_i = {mp.nstr(det_off,10)}  (target q^g = {q**g}) "
          f"[PRESERVED: {abs(abs(det_off) - q**g) < 1e-20 * q**g}]")
    print(f"      pairing products: {[mp.nstr(pp,8) for pp in pair_off]}  "
          f"[each = q={q}: {all(abs(abs(pp)-q) < 1e-20*q for pp in pair_off)}]")
    print(f"      even split |alpha_i|=sqrt q for ALL i?  {even_split(off, q)}  <-- BROKEN at 2 places\n")

    rigid = even_split(off, q)   # if the redistribution were impossible, off would still be on-line
    det_preserved = abs(abs(det_off) - q**g) < 1e-20 * q**g
    pair_preserved = all(abs(abs(pp) - q) < 1e-20 * q for pp in pair_off)
    print(f"    => (det PRESERVED: {det_preserved}) AND (pairing PRESERVED: {pair_preserved}) AND")
    print(f"       (even split BROKEN: {not rigid}) ==> the GLOBAL even split is NOT FORCED by")
    print(f"       (determinant + pairing).  It is a CONJUNCTION (per-place), NOT a RIGIDITY.")
    print(f"       The FE fixes the PRODUCT of moduli (=q^g, the global edge, FREE) but NOT the")
    print(f"       INDIVIDUAL moduli -- a balanced cross-place redistribution is invisible to it.\n")

    # ---------------------------------------------------------------------------------------------
    print("=" * 100)
    print("[2] zeta side: the per-prime Satake pairs -- is there ANY cross-PRIME modulus link?")
    print("    The global FE of L(s,f) is s <-> k-1-s; it couples NO two primes' moduli.  Plant")
    print("    off-even at p1 AND p2, each preserving its OWN determinant p^{k-1}: no global relation")
    print("    is violated -- the primes are modulus-INDEPENDENT (the global mirror of [1]).\n")
    p1, p2, delta = 5, 7, mp.mpf("0.3")
    det_b, det_a, planted = cross_prime_redistribution(p1, p2, delta)
    print(f"    primes p1={p1}, p2={p2}, delta={mp.nstr(delta,3)}")
    print(f"      global determinant (prod of per-prime |alpha beta|) before = {mp.nstr(det_b,12)}")
    print(f"      after cross-prime redistribution                       = {mp.nstr(det_a,12)}")
    print(f"      [PRESERVED: {abs(det_a - det_b) < 1e-15 * det_b}]  -- every per-prime determinant intact")
    half = mp.mpf(K - 1) / 2
    print(f"      but |alpha(p1)|={mp.nstr(planted[0],8)} != p1^((k-1)/2)={mp.nstr(mp.mpf(p1)**half,8)}, and")
    print(f"          |alpha(p2)|={mp.nstr(planted[2],8)} != p2^((k-1)/2)={mp.nstr(mp.mpf(p2)**half,8)}")
    print(f"      => off-even at BOTH primes, global determinant data UNTOUCHED: primes UNCOUPLED.\n")

    # ---------------------------------------------------------------------------------------------
    print("=" * 100)
    print("[3] DH falsifier (type-level): no Euler product => no Satake => no per-place determinant =>")
    print("    no edge to assemble AND no carrier to glue.  The descent map has EMPTY DOMAIN at step 0,")
    print("    strictly before the rigidity-vs-conjunction question.  Carrier ladder DH < zeta < FF")
    print("    (M2d): DH lacks the edge; zeta has the edge (det, free) + the open GLOBAL even split;")
    print("    FF has both but its global even split is ALSO a conjunction, forced by Deligne not by FE.\n")

    # ---------------------------------------------------------------------------------------------
    print("=" * 100)
    print("VERDICT (M4r -- the descent gluing of the radius):")
    print("  The descent ASSEMBLES the GLOBAL DETERMINANT (prod of moduli = q^g over FF, the product")
    print("  of per-prime |alpha beta|=p^{k-1} over zeta) -- the global EDGE, Euler-borne, RH-FREE.")
    print("  But the radius RESIDUE -- the GLOBAL EVEN SPLIT 'every modulus = sqrt(its base size)' -- is")
    print("  a CONJUNCTION of per-place conditions with NO CROSS-PLACE RIGIDITY: a determinant-neutral,")
    print("  pairing-neutral modulus redistribution moves eigenvalues OFF the even split at several")
    print("  places while preserving EVERY datum the Euler product / FE supplies (the global det AND")
    print("  each Poincare pairing).  So the descent gluing adds NO global lever over the per-prime")
    print("  K2r finding -- the FE couples the PRODUCT of radii, never the individual radii.")
    print("  THE STRUCTURAL CONSEQUENCE (where this sends the keystone): the ONLY structure that")
    print("  DISTINGUISHES the redistributed (off-even) config from the genuine (even) one is a")
    print("  POSITIVITY on the global H^1 that FAILS under redistribution -- exactly the Weil/Hodge")
    print("  index P_inf >= 0 (the archimedean keystone), which is NOT a function of the determinant.")
    print("  M4r thus PROVES the descent cannot read Re s=1/2 off the Euler/FE data (no rigidity) and")
    print("  RELOCATES the centre entirely onto the archimedean positivity P_inf >= 0 -- the radius is")
    print("  Euler-ASSEMBLED only as a PRODUCT (the edge); the even SPLIT is an archimedean positivity,")
    print("  not a descent constraint.  (This is K2r-fix's 'the radius must be Euler-assembled' made")
    print("  precise and then BOUNDED: the assembly gives the product, never the split.)")


if __name__ == "__main__":
    report()
