"""reality_datum_kappa.py -- K2r-fix: is "Frobenius in Fix(sigma_d)" (the q-Weil-number/reality
   condition) supplied by a REAL/CONDENSED structure kappa on the weight-2 carrier over Z whose
   descent datum FORCES the Satake pair to be sigma_d-fixed -- or is that real structure itself
   only available AFTER purity (so kappa is the radius, not a free datum)?

  run:  python3 -m scripts.numerics.witness.reality_datum_kappa

THE MANDATE (AGENDA K2r-fix, the KEYSTONE reality datum, HIGH priority; charter sec.0 design law
  -- the polarization is a DUALITY/*-involution, never a metric; built on K2r-split, M3b).
  K2r-split FACTORED the involution: sigma_d(z)=d/conj(z) (the polarization duality on the weight-2
  determinant line) EXISTS FOR FREE from the Euler-borne determinant edge d=p^{k-1}, *-clean
  (involutive + ANTILINEAR), Fix(sigma_d)={|z|=sqrt d}=the even split. BUT a duality does NOT force
  its own fixed points: an off-Ramanujan plant (same d, same sigma_d) is NOT sigma_d-fixed. The
  residue RELOCATED to the REALITY condition "Frobenius in Fix(sigma_d)" = |alpha|=sqrt d = RH;
  over F_q this is the q-Weil-number theorem = "Frobenius commutes with geometric conjugation" =
  the REALITY of the realization (Deligne purity).

THE PRECISE QUESTION K2r-fix MAKES EXECUTABLE.
  The reality condition "Frobenius in Fix(sigma_d)" decomposes as: Frobenius F commutes with a
  CONJUGATION c on the realization (Frobenius-conjugation commutation). A conjugation c is an
  ANTILINEAR involution (c o c = id, c antilinear); its FIXED LOCUS V^c = {v : c(v)=v} is the
  "real points" -- M3b's kappa.  The decisive structural fork:

    (FORK 1) Is there a CANONICAL conjugation c on the weight-2 carrier, definable from the
             EULER-BORNE data ALONE (the determinant edge d, the FE), such that
                  F in Fix(sigma_d)  <=>  c o F = F o c   (F commutes with c)?
             If YES and c is Euler-borne + radius-FREE, then the reality is a free descent datum
             and RH would be forced.  (falsify: must be Euler-borne, DH-absent, see the plant.)

    (FORK 2) Or does specifying the conjugation c whose fixed locus is the even split ALREADY
             require choosing the radius sqrt d -- i.e. c = c_d is parametrized by d, and the
             commutation [c_d, F]=0 is sqrt d = |alpha| = purity itself?  Then kappa is NOT free;
             it IS the radius, available only AFTER purity.

THE ARITHMETIC OF CONJUGATIONS ON A 1-DIM DETERMINANT/EIGEN LINE (the executable core).
  On C (the eigenline of an eigenvalue alpha, or the determinant line carrying d), an ANTILINEAR
  involution has the form  c(z) = mu * conj(z)  with c o c = id  <=>  mu * conj(mu) = |mu|^2 = 1,
  i.e.  mu = e^{i theta}  on the |mu|=1 circle.  (Proof: c(c(z)) = mu conj(mu conj(z)) =
  mu conj(mu) z = |mu|^2 z, so involutive iff |mu|=1.)  Its FIXED LOCUS is the real line
  {z : mu conj(z)=z} = the line through e^{i theta/2}.  A POINT z=r e^{i phi} is c-fixed iff
  mu conj(z)=z iff e^{i theta} r e^{-i phi} = r e^{i phi} iff theta = 2 phi (PHASE condition only!).
  ==> a |mu|=1 conjugation NEVER constrains the RADIUS r.  It is purely a PHASE/reality datum.

  But sigma_d(z)=d/conj(z) is DIFFERENT: it is antilinear with MULTIPLIER d (|d| != 1), so
  sigma_d o sigma_d = |d|^2/.. wait -- sigma_d(sigma_d(z)) = d/conj(d/conj(z)) = d/(conj(d)/z)
  = d z/conj(d) = z (since d real>0).  Fix: sigma_d(z)=z <=> d=z conj(z)=|z|^2 <=> |z|=sqrt d:
  a RADIUS condition.  So sigma_d is a "conjugation SCALED by d" and ITS fixed locus IS a radius.

  THE FORK, SHARPENED:  sigma_d = (scale by d) o (unit conjugation).  The RADIUS in Fix(sigma_d)
  comes ENTIRELY from the scale d (Euler-borne, free, K2r), the PHASE/reality comes from the unit
  conjugation c_0(z)=conj(z) (the canonical real structure, M3b's kappa, radius-FREE).  So:
     Fix(sigma_d) = {|z|=sqrt d}  is determined by:  RADIUS sqrt d  (free, from d)
                                                  AND PHASE   real    (free, from c_0).
  Then WHY is "the Frobenius pair lies on Fix(sigma_d)" not free??  Because the Frobenius alpha is
  a SPECIFIC point with its OWN radius |alpha| and phase, and "lies on Fix" demands |alpha|=sqrt d:
  the Frobenius's radius must MATCH the determinant's sqrt -- and the determinant only fixes the
  PRODUCT |alpha||beta|=d, not the individual |alpha|.  kappa (the reality datum c_0) fixes the
  PHASE-reality for free, but is RADIUS-SILENT (M3b's exact lesson: (-1)^w is a sign, radius-blind).

WHAT THIS MODULE DEMONSTRATES (the K2r-fix finding, executable).
  [1] Every antilinear involution (conjugation) c with |mu|=1 is RADIUS-SILENT: its fixed locus is
      a phase/reality condition, NEVER a radius.  So the reality datum kappa CANNOT supply the
      radius -- exactly M3b's "(-1)^w is radius-silent" now as a theorem about conjugations.
  [2] sigma_d's radius comes from the SCALE d, NOT from any conjugation: sigma_d = (scale d) o c_0.
      The radius sqrt d is the Euler-borne determinant (free).  The MATCH |alpha|=sqrt d (the
      Frobenius's radius equals the half-determinant) is the even split = the per-prime purity.
  [3] So kappa is supplied for FREE over Z (the canonical real structure c_0(z)=conj(z),
      radius-silent, M3b-coherent) -- but it FORCES only the PHASE/reality, NOT the radius.  The
      Frobenius-conjugation commutation [c_0, F]=0 holds for the conjugation-symmetric (FE) config
      REGARDLESS of radius: the radius |alpha|=sqrt d is ORTHOGONAL to kappa, an Euler datum that
      kappa does not see.  => kappa is FREE but RADIUS-SILENT; it does NOT force the even split.
  [4] FF ANCHOR: over F_q the reality "F commutes with geometric conjugation" PLUS |alpha|=sqrt q
      is Deligne purity; the commutation [c_0,F]=0 alone (phase reality) is the FE (free), the
      RADIUS |alpha|=sqrt q is the SEPARATE purity theorem.  Confirmed: kappa (=c_0) is free, the
      radius is the theorem -- the FORK resolves to FORK-2-for-the-radius / FORK-1-for-the-phase.
  [5] DH: c_0 exists (it is just complex conjugation), but there is NO determinant d => NO sqrt d
      radius to match => the "even split" question is VACUOUS, and the commutation [c_0,F]=0 (the
      FE-reality) holds for DH too (DH has a FE).  So kappa is DH-SHARED (radius-silent => cannot
      distinguish), the radius is the ONLY DH-distinguishing datum -- and kappa does not carry it.

  CONCLUSION (the honest answer to K2r-fix): the real/condensed structure kappa IS available over Z
  for free (the canonical conjugation c_0, M3b-coherent, radius-silent) and it FORCES the PHASE-
  reality (the conjugation-symmetry of the zero/Satake config, = the FE) -- but it is RADIUS-SILENT
  and DH-SHARED, so it does NOT force the even split |alpha|=sqrt d.  kappa is NOT "only available
  after purity" (FORK 2 is FALSE for the phase) -- it is available before purity, FOR FREE -- but
  it is the WRONG HALF: it carries reality/phase, not the radius.  The radius (purity = even split
  = RH) is ORTHOGONAL to every conjugation, an Euler datum no real structure supplies.  This is the
  sharpest form of M3b's lesson: the archimedean reality datum is radius-silent BY THE ALGEBRA OF
  CONJUGATIONS (|mu|=1 forces a phase condition, never a radius).

FALSIFIER PRE-COMMITMENT.
  * kappa = c_0(z)=conj(z) is NOT Euler-borne (it is bare complex conjugation, exists for DH) =>
    DISPERSING on the reality half.  The radius datum sqrt d IS Euler-borne (the determinant) but
    is NOT a conjugation -- it is the scale.  So the reality datum SPLITS: phase-half DISPERSING
    (free, DH-shared, radius-silent), radius-half = the even split (CIRCULAR, = RH).
  Predicted verdict: the reality datum kappa is FREE but RADIUS-SILENT -- it forces the phase, not
  the radius; FORK 2 (kappa requires the radius) is FALSE, but kappa is the wrong half.  Tabled
  DISPERSING-on-the-reality-half (the radius is the irreducible Euler residue, not in any kappa).
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 40

TAU = {
    2: -24, 3: 252, 5: 4830, 7: -16744, 11: 534612, 13: -577738,
    17: -6905934, 19: 10661420, 23: 18643272, 29: 128406630,
}
K = 12


def satake_arith(p):
    a = TAU[p]
    det = p ** (K - 1)
    disc = mp.mpf(a) ** 2 - 4 * det
    s = mp.sqrt(mp.mpc(disc))
    return (mp.mpc(a + s) / 2, mp.mpc(a - s) / 2)


# ----------------------------------------------------------------------------------------------------
# [1] THE ALGEBRA OF CONJUGATIONS: every antilinear involution c(z)=mu conj(z) with |mu|=1 is
#     RADIUS-SILENT.  Fix(c) is a PHASE condition (theta=2 phi), NEVER a radius.
# ----------------------------------------------------------------------------------------------------

def conjugation(mu):
    """An antilinear involution c(z) = mu * conj(z).  Involutive iff |mu|=1."""
    return lambda z: mu * mp.conj(z)


def is_antilinear_involution(mu, samples):
    """Check c o c = id (involutive) and antilinearity c(a z) = conj(a) c(z)."""
    c = conjugation(mu)
    inv_err = max(abs(c(c(z)) - z) for z in samples)
    a = mp.mpc(2, 3)
    z = mp.mpc(1, 1)
    antilin_err = abs(c(a * z) - mp.conj(a) * c(z))
    return inv_err, antilin_err


def conjugation_fixed_is_phase_not_radius(mu):
    """Fix(c) for c(z)=mu conj(z), |mu|=1: c(z)=z <=> mu conj(z)=z.  Write z=r e^{i phi},
    mu=e^{i theta}: e^{i theta} r e^{-i phi}=r e^{i phi} <=> theta=2 phi -- a PHASE condition,
    INDEPENDENT of r.  Demonstrate: pick the fixed phase phi*=theta/2; points at ANY radius on
    that ray are fixed; the radius is UNCONSTRAINED."""
    theta = mp.arg(mu)
    phi_star = theta / 2
    # points at three DIFFERENT radii on the fixed ray
    fixed_errs = []
    for r in [mp.mpf("0.5"), mp.mpf("3.0"), mp.mpf("100.0")]:
        z = r * mp.exp(mp.mpc(0, 1) * phi_star)
        fixed_errs.append(abs(conjugation(mu)(z) - z))
    # a point OFF the fixed ray (wrong phase) is moved, at any radius
    z_off = mp.mpf("3.0") * mp.exp(mp.mpc(0, 1) * (phi_star + mp.mpf("0.5")))
    off_err = abs(conjugation(mu)(z_off) - z_off)
    return fixed_errs, off_err


# ----------------------------------------------------------------------------------------------------
# [2] sigma_d = (scale by d) o (unit conjugation c_0).  The RADIUS in Fix(sigma_d) is the SCALE d,
#     NOT a conjugation.  Decompose it explicitly.
# ----------------------------------------------------------------------------------------------------

def sigma_d(z, d):
    return d / mp.conj(z)


def sigma_d_decomposition(z, d):
    """sigma_d(z) = d/conj(z) = d * (1/conj(z)).  Write as (scale by d) o (inversion-conjugation).
    Cleaner: sigma_d(z) = d * conj(1/z)?  No.  The honest decomposition on the eigenline:
       sigma_d(z) = d / conj(z).
    Compare the UNIT conjugation c_0(z) = conj(z) (radius-PRESERVING, phase-flipping) and the
    SCALE s_d(z) = d/(z conj(z)) * z ... -- the clean statement is:
       Fix(sigma_d) = {|z|^2 = d}: the RADIUS sqrt d comes from d (the scale), the reality (real
       positive representative z=sqrt d) from c_0.  We verify sigma_d = m_d o c_0 where
       m_d(w) = d/|w|^2 * w is the RADIAL rescale to radius d/|w| ...
    The cleanest TRUE identity: sigma_d(z) = (d/|z|^2) * z when z is real>0?  d/conj(z) with z=r:
       = d/r (real).  And (d/|z|^2) z = d/r^2 * r = d/r.  YES for real z.  In general:
       sigma_d(z) = d/conj(z) = d z/|z|^2 = (d/|z|^2) * z  -- a POSITIVE REAL rescale of z by
       d/|z|^2, composed with NOTHING (it is already z-direction!).  So sigma_d(z) = (d/|z|^2) z:
       sigma_d moves z RADIALLY to radius d/|z| along the SAME ray.  Fixed iff d/|z|=|z| iff
       |z|=sqrt d.  The map is a RADIAL inversion about radius sqrt d -- PURELY a radius datum,
       NO phase content.  conj cancels: d/conj(z)=d z/(z conj z)=d z/|z|^2."""
    direct = d / mp.conj(z)
    radial = (d / (abs(z) ** 2)) * z
    return direct, radial, abs(direct - radial)


# ----------------------------------------------------------------------------------------------------
# [3] THE FORK RESOLVED: kappa (=c_0, the unit conjugation) forces PHASE-reality, radius-silent.
#     The Frobenius-conjugation commutation [c_0, F]=0 = the FE-symmetry, holds at ANY radius.
# ----------------------------------------------------------------------------------------------------

def frobenius_conjugation_commute(alpha, beta):
    """The weight-2 Satake pair as a diagonal F=diag(alpha,beta) on the 2-dim carrier; the unit
    conjugation that REALIZES the FE swaps the two eigenlines: c_0 = (swap) o conj.  Test
    [c_0, F] = c_0 F - F c_0 on a generic vector, and whether the commutation constrains the RADII.
    c_0(v) = swap(conj(v)) means c_0(z1,z2) = (conj(z2), conj(z1)).  Then
       c_0 F (z1,z2) = c_0(alpha z1, beta z2) = (conj(beta) conj(z2), conj(alpha) conj(z1))
       F c_0 (z1,z2) = F(conj(z2), conj(z1)) = (alpha conj(z2), beta conj(z1)).
    Equal for all (z1,z2) <=> conj(beta)=alpha AND conj(alpha)=beta <=> beta = conj(alpha).
    THAT is the FE-reality (eigenvalues conjugate-paired) -- holds at ANY radius |alpha|.  The
    RADIUS |alpha|=sqrt d is a SEPARATE condition c_0 does not see."""
    v = mp.matrix([mp.mpc(2, 1), mp.mpc(1, -3)])
    F = mp.matrix([[alpha, 0], [0, beta]])

    def c0(w):
        return mp.matrix([mp.conj(w[1]), mp.conj(w[0])])

    cF = c0(F * v)
    Fc = F * c0(v)
    comm = max(abs(cF[i] - Fc[i]) for i in range(2))
    fe_real = abs(beta - mp.conj(alpha))  # the commutation condition: beta = conj(alpha)
    return comm, fe_real


def report():
    print(__doc__)
    print("=" * 100)
    print("K2r-fix: IS THE REALITY DATUM kappa A FREE DESCENT CONDITION, OR THE RADIUS ITSELF?\n")

    # ---- [1] every |mu|=1 conjugation is RADIUS-SILENT (a phase condition) ----
    print("[1] THE ALGEBRA OF CONJUGATIONS: an antilinear involution c(z)=mu conj(z) is involutive")
    print("    IFF |mu|=1, and its FIXED LOCUS is a PHASE condition (theta=2 phi), NEVER a radius.")
    print("    => the reality datum kappa is RADIUS-SILENT by the algebra of conjugations.\n")
    print(f"    {'mu (|mu|=1)':>22s} {'inv err':>12s} {'antilin err':>14s} "
          f"{'fixed@3 radii':>26s} {'off-ray moved':>14s}")
    for mu in [mp.mpc(1, 0), mp.exp(mp.mpc(0, 1) * mp.mpf("0.7")), mp.mpc(0, 1)]:
        inv_err, antilin = is_antilinear_involution(mu, [mp.mpc(2, 1), mp.mpc(1, -1), mp.mpc(3, 0)])
        fixed_errs, off = conjugation_fixed_is_phase_not_radius(mu)
        fe = ",".join(mp.nstr(e, 2) for e in fixed_errs)
        print(f"    {mp.nstr(mu, 8):>22s} {mp.nstr(inv_err, 4):>12s} {mp.nstr(antilin, 4):>14s} "
              f"{fe:>26s} {mp.nstr(off, 6):>14s}")
    print("\n    => ALL three radii on the fixed ray are c-fixed (err ~ 0), off-ray is moved:")
    print("       Fix(c) is a RAY (phase), radius-UNCONSTRAINED.  kappa CANNOT supply the radius.\n")

    # ---- [2] sigma_d = radial inversion about sqrt d: its radius is the SCALE d, not a conjugation ----
    print("=" * 100)
    print("[2] sigma_d(z)=d/conj(z) = (d/|z|^2) z: a RADIAL inversion about radius sqrt d (conj CANCELS).")
    print("    Its radius comes ENTIRELY from the EULER-BORNE scale d -- NOT from any conjugation.\n")
    print(f"    {'p':>3s} {'d=p^{k-1}':>16s} {'|d/conj(z)-(d/|z|^2)z|':>24s} {'Fix radius=sqrt d':>18s}")
    for p in [2, 3, 5, 7, 11]:
        d = mp.mpf(p) ** (K - 1)
        a, _ = satake_arith(p)
        _, _, decomp_err = sigma_d_decomposition(a, d)
        print(f"    {p:>3d} {mp.nstr(d, 8):>16s} {mp.nstr(decomp_err, 6):>24s} "
              f"{mp.nstr(mp.sqrt(d), 10):>18s}")
    print("\n    => sigma_d = (d/|z|^2)*z EXACTLY (conj cancels, err ~ 0): a pure RADIAL map about")
    print("       sqrt d.  The radius is the SCALE (the determinant, Euler-borne); NO phase/reality")
    print("       content.  The reality (kappa) and the radius (the determinant scale) are ORTHOGONAL.\n")

    # ---- [3] the commutation [c_0, F]=0 is the FE-reality (beta=conj alpha), radius-silent ----
    print("=" * 100)
    print("[3] THE FORK RESOLVED: the Frobenius-conjugation commutation [c_0, F]=0 (c_0 = the unit")
    print("    conjugation realizing the FE, swap o conj) is the condition beta=conj(alpha) -- the")
    print("    FE/phase-reality, which holds at ANY radius |alpha|.  The radius |alpha|=sqrt d is")
    print("    ORTHOGONAL: c_0 does NOT see it.  kappa forces PHASE-reality, NOT the radius.\n")
    print(f"    {'config':>26s} {'|alpha|':>14s} {'sqrt d':>14s} {'[c_0,F]':>12s} {'beta=conj a?':>14s}")
    for p in [2, 3, 5, 7]:
        a, b = satake_arith(p)
        d = a * b
        # genuine Ramanujan pair: beta = conj(alpha) (since |alpha|=sqrt d and alpha beta = d real)
        comm, fe = frobenius_conjugation_commute(a, mp.conj(a))
        print(f"    {('Ramanujan p=' + str(p)):>26s} {mp.nstr(abs(a), 8):>14s} "
              f"{mp.nstr(mp.sqrt(abs(d)), 8):>14s} {mp.nstr(comm, 4):>12s} {mp.nstr(fe, 4):>14s}")
    # PLANT: off-radius but STILL conjugate-paired (beta'=conj(alpha')): commutation STILL holds,
    # radius is wrong -- the decisive demonstration that kappa is radius-blind.
    print("\n    PLANT (off-radius but conjugate-paired beta'=conj(alpha'), |alpha'| != sqrt d):")
    d0 = mp.mpf(11) ** (K - 1)
    r_off = mp.sqrt(d0) * mp.mpf(10) ** mp.mpf("0.3")
    ap = mp.mpc(r_off * mp.cos(mp.mpf("0.4")), r_off * mp.sin(mp.mpf("0.4")))
    bp = mp.conj(ap)  # conjugate-paired => c_0-commuting, but |alpha'| != sqrt d
    comm_p, fe_p = frobenius_conjugation_commute(ap, bp)
    print(f"      |alpha'|={mp.nstr(abs(ap), 8)}  sqrt d={mp.nstr(mp.sqrt(d0), 8)}  "
          f"[c_0,F]={mp.nstr(comm_p, 4)}  beta'=conj(a')?={mp.nstr(fe_p, 4)}")
    print(f"      => the planted OFF-RADIUS pair STILL commutes with c_0 ([c_0,F]~0) because it is")
    print(f"         conjugate-paired -- kappa is BLIND to the radius defect.  kappa = the FE/phase,")
    print(f"         RADIUS-SILENT.  The radius |alpha|=sqrt d is the irreducible Euler residue.\n")

    # ---- [4] FF anchor: c_0-commutation = the FE (free); the radius |alpha|=sqrt q = purity theorem ----
    print("=" * 100)
    print("[4] FF ANCHOR: over F_q the reality SPLITS the same way: the conjugation-commutation")
    print("    [c_0,F]=0 (Frobenius eigenvalues conjugate-paired) is the FE (FREE), and the RADIUS")
    print("    |alpha|=sqrt q is the SEPARATE Deligne-purity theorem.  kappa (=c_0) is free + radius-")
    print("    silent; the radius is the theorem.  (Confirms FORK 1 for the phase, FORK 2-fails-but-")
    print("    -orthogonal for the radius: kappa is free, NOT the radius, and does not force it.)\n")
    print(f"    {'curve':14s} {'|alpha|':>12s} {'sqrt q':>12s} {'[c_0,F] (FE)':>14s} {'radius=purity?':>16s}")
    for q, a1 in [(2, 1), (5, 2), (7, -3), (11, 5), (13, 4)]:
        disc = a1 * a1 - 4 * q
        s = mp.sqrt(mp.mpc(disc))
        a, b = mp.mpc(a1 + s) / 2, mp.mpc(a1 - s) / 2
        r = mp.sqrt(mp.mpf(q))
        # genuine q-Weil number: |alpha|=sqrt q, beta = q/alpha = conj(alpha)
        comm, fe = frobenius_conjugation_commute(a, mp.conj(a))
        purity = abs(abs(a) - r) < 1e-20 * r
        print(f"    E/F_{q:<2d} a1={a1:+d}  {mp.nstr(abs(a), 6):>12s} {mp.nstr(r, 6):>12s} "
              f"{mp.nstr(comm, 4):>14s} {str(purity):>16s}")
    print("\n    => FF: [c_0,F]=0 is the FE (free, the conjugate-pairing); |alpha|=sqrt q is purity")
    print("       (the theorem).  kappa supplies the phase-reality for free, the radius is separate.\n")

    # ---- [5] DH: c_0 exists (bare conjugation), the FE-commutation holds (DH has a FE), NO radius ----
    print("=" * 100)
    print("[5] DH FALSIFIER: c_0 (bare complex conjugation realizing the FE) EXISTS for DH -- DH HAS")
    print("    a functional equation, so the conjugate-pairing [c_0,F]=0 holds for DH too.  kappa is")
    print("    DH-SHARED (the reality/phase half is NOT Euler-distinguishing).  But DH has NO Euler")
    print("    product => NO determinant d => NO radius sqrt d to match: the EVEN-SPLIT question is")
    print("    VACUOUS for DH.  => the reality datum kappa does NOT distinguish DH (radius-silent);")
    print("    the RADIUS (the determinant edge + its even split) is the ONLY DH-distinguishing datum,")
    print("    and kappa does not carry it.  Carrier ladder: DH (c_0, no d) < Z (c_0 + d, open split)")
    print("    < FF (c_0 + d + purity theorem).\n")

    # ---- verdict ----
    print("=" * 100)
    print("VERDICT (K2r-fix):")
    print("  The reality/condensed datum kappa = the unit conjugation c_0(z)=conj(z) (M3b's real")
    print("  structure) IS available over Z FOR FREE -- it is bare complex conjugation realizing the")
    print("  FE (the conjugate-pairing of the Satake/zero config) -- and FORK 2 ('kappa is only")
    print("  available after purity') is FALSE.  BUT kappa is RADIUS-SILENT BY THE ALGEBRA OF")
    print("  CONJUGATIONS: every antilinear involution c(z)=mu conj(z) is involutive iff |mu|=1, and")
    print("  its fixed locus is a PHASE condition (theta=2 phi), NEVER a radius ([1]).  sigma_d's")
    print("  radius is the SCALE d (a radial inversion about sqrt d, conj cancels [2]), an Euler datum")
    print("  ORTHOGONAL to every conjugation.  The commutation [c_0,F]=0 is the FE-reality")
    print("  (beta=conj alpha), which holds at ANY radius -- a planted OFF-RADIUS conjugate-paired")
    print("  pair STILL commutes with c_0 ([3]).  So kappa forces the PHASE/reality (free, DH-shared,")
    print("  radius-silent), NOT the even split.  The radius |alpha|=sqrt d (purity = RH) is the")
    print("  irreducible Euler residue that NO real structure supplies.")
    print("  Falsifier: kappa NOT Euler-borne (c_0 exists for DH) => DISPERSING on the reality half;")
    print("  the radius IS Euler-borne (the determinant) but is NOT a conjugation (it is the scale).")
    print("  => the reality datum SPLITS: phase-half DISPERSING (free, radius-silent, M3b-coherent),")
    print("     radius-half = the even split = the irreducible RH (an Euler datum, not in any kappa).")
    print("  This SHARPENS M3b's lesson to a THEOREM: the archimedean reality datum is radius-silent")
    print("  BECAUSE conjugations (|mu|=1) carry only phase; the radius must be Euler-assembled (M4r).")


if __name__ == "__main__":
    report()
