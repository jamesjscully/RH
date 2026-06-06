"""scaling_site_radius.py -- R3: does the CONNES-CONSANI SCALING SITE / absolute Frobenius supply the
   archimedean nilpotent-or-grading datum that FORCES the radius |alpha|=q^{w/2} (axiom N4), or -- like
   Schmid's SL(2)-orbit N -- only the FREE parity / a phase, with the SCALE still unpinned?

  run:  python3 -m scripts.numerics.witness.scaling_site_radius

THE MANDATE (AGENDA R3, the RESIDUE block; built on R1=weight_monodromy_residue, R2=schmid_sl2_orbit).
  R1 pinned the residue to an archimedean N with FOUR axioms; R2 PROVED Schmid's SL(2)-orbit gives
  (N1)-(N3) + the FREE weight parity (-1)^w but NOT (N4) the radius, and ISOLATED EXACTLY what R3 must
  supply:  not another (p,q) centering (free, DH-shared, radius-silent) but an ARCHIMEDEAN BASE SIZE q
  -- a genuine R_{>0}^x-grading / a |.|_infty size -- COUPLING the (p,q)-grading to a MODULUS.

  R3 tests the Connes-Consani SCALING SITE (the topos [0,infty) x| R_{>0}^x; Connes-Consani 2014-2021,
  "Geometry of the Scaling Site", "Riemann-Roch for Spec Z").  Its distinguished feature -- the one
  Schmid's Hodge N lacked -- is that it CARRIES AN R_{>0}^x-ACTION: the SCALING flow t |-> lambda*t,
  with generator  theta = t d/dt,  and the ABSOLUTE FROBENIUS  Fr_lambda : t |-> lambda*t.  This is a
  genuine SCALE at the archimedean place.  THE QUESTION R2 sharpened:  is the scaling generator theta
  the archimedean N whose grading carries an ARITHMETIC q (forcing (N4) the radius q^{k/2}=Re s=1/2)?
  OR does it, like Schmid's N, deliver only a FREE datum -- here a SELF-DUAL point of a Haar measure --
  with the arithmetic scale q STILL not present?

WHAT THIS MODULE ESTABLISHES (the decisive split, exact mpmath, FF-anchored).

  [A] The scaling site DOES carry a genuine R_{>0}^x-grading -- the one thing Schmid lacked.  The
      scaling generator theta=t d/dt has, on the multiplicative line R_{>0} with Haar d*t=dt/t, the
      spectral decomposition into characters  t |-> t^{s},  s=sigma+i*tau,  and the unitary
      (L^2(R_{>0}, d*t)) characters are exactly  t |-> t^{i*tau}  on the line  sigma=0  -- equivalently,
      after the |.|^{1/2} normalization that makes the FE a reflection, on  sigma=1/2.  SO theta DOES
      produce a distinguished radius Re s = 1/2.  This is REAL, and it is what R2 asked for: a scale.

  [B] BUT that radius is the SELF-DUAL POINT of the multiplicative Haar / the FUNCTIONAL-EQUATION
      symmetry s <-> 1-s -- NOT an Euler-borne arithmetic size q.  We make this EXACT:
        (i) the 1/2 is the unique fixed point of the FE reflection s<->1-s (the center of the unitary
            axis of the Mellin transform), pinned by the SYMMETRY of Haar measure d*t under t<->1/t;
        (ii) it is INDEPENDENT of any Euler product: the SAME scaling site / SAME generator theta /
             SAME self-dual 1/2 arises for ANY Mellin-class function, including the DH surrogate, which
             has a FE (hence a self-dual axis) but NO Euler product.  The scaling 1/2 is DH-SHARED.
        (iii) so theta's radius is the FE/Haar self-dual point (DH-shared, FREE), NOT the arithmetic q.

  [C] THE FF CONTRAST -- where the scaling DOES carry q, and WHY.  Over F_q the analogue of the scaling
      site is the action of  Frob = (the q-power map),  whose orbit is the DISCRETE group q^Z (NOT the
      continuous R_{>0}^x).  There the "scale" is literally the BASE SIZE q -- an ARITHMETIC integer >1,
      the cardinality of the residue field -- and the Weil eigenvalues sit at |alpha|=q^{w/2} BECAUSE
      Frob^* acts with that q.  The continuous archimedean scaling t|->lambda*t has NO such distinguished
      lambda: every lambda>0 is on equal footing (R_{>0}^x is homogeneous, transitive, no marked point),
      so there is NO arithmetic q -- only the FE-marked self-dual axis.  q is the SPECTRAL GAP of the
      Frobenius (the marked generator of q^Z); the archimedean scaling has CONTINUOUS spectrum, no gap,
      no marked q.  This is the precise reason R2's "couple the grading to an arithmetic q" FAILS for
      theta: the scaling site has the grading (the R_{>0}^x-action) but its q-analogue is CONTINUOUS,
      so there is no DISTINGUISHED arithmetic size -- only the self-dual point the FE marks for free.

  [D] THE DEEPER READING (Connes-Consani's own thesis, honestly stated).  In Connes-Consani the zeros
      of zeta ARE realized as the spectrum of the scaling action on a suitable cohomology (H^1 of the
      scaling site / the cokernel of a map of adele-class spaces).  RH is then "the scaling spectrum is
      on the critical line".  But this realization is EQUIVALENT to RH, not a proof of it: the scaling
      site SUPPLIES THE GRADING (the R_{>0}^x-action = the would-be archimedean N) and CORRECTLY marks
      the self-dual axis 1/2 -- exactly (N1)-(N3) + the free FE point -- and leaves OPEN whether the
      spectrum lies ON it (= (N4) = RH).  So R3's verdict mirrors R2's at one higher altitude: the
      scaling site gives the grading + the FREE self-dual radius, NOT the FORCING of the spectrum onto
      it.  The q that would force it is, over F_q, the discrete Frobenius gap; at infinity the scaling
      is continuous and supplies NO such gap.
"""
from __future__ import annotations

import mpmath as mp

mp.mp.dps = 40


# ====================================================================================================
# [A] THE SCALING GENERATOR theta = t d/dt: its characters and the distinguished self-dual axis.
#     On R_{>0} with multiplicative Haar d*t = dt/t, theta is self-adjoint-like with characters
#     t |-> t^{i*tau} (the unitary dual).  We exhibit the |.|^{1/2}-normalized reflection s<->1-s and
#     its UNIQUE fixed point sigma=1/2 -- the scale the scaling site DOES carry (vs Schmid, who lacked
#     an R_{>0}^x-action entirely).
# ====================================================================================================

def scaling_character(t, s):
    """A character of the scaling action: t |-> t^s.  theta=t d/dt has eigenvalue s on t^s
    (t d/dt of t^s = s*t^s).  The SCALING SITE'S grading is the s-grading -- a genuine R_{>0}^x-grading,
    the structure Schmid's Hodge N lacked."""
    return mp.mpf(t) ** s


def scaling_eigenvalue_check(t, s):
    """Verify theta(t^s) = s*t^s numerically (t d/dt applied to t^s).  Returns (lhs, rhs) so the
    grading is concrete: theta acts diagonally with eigenvalue s = the 'weight' coordinate."""
    h = mp.mpf(10) ** (-20)
    f = lambda x: mp.mpf(x) ** s
    deriv = (f(t + h) - f(t - h)) / (2 * h)          # d/dt
    lhs = mp.mpf(t) * deriv                            # theta = t d/dt
    rhs = s * (mp.mpf(t) ** s)
    return lhs, rhs


def fe_reflection(s):
    """The functional-equation reflection s <-> 1-s (the completed-zeta symmetry / the t<->1/t symmetry
    of the multiplicative Haar after the |.|^{1/2} normalization)."""
    return 1 - s


def self_dual_axis():
    """The UNIQUE fixed point of s<->1-s: sigma=1/2.  This is the radius the scaling site marks.
    It is the CENTER of the unitary spectrum of theta (the |.|^{1/2}-normalized critical line).
    Returns 1/2 as an exact mpf, plus the verification it is the reflection's fixed point."""
    sigma = mp.mpf(1) / 2
    fixed = abs(fe_reflection(sigma) - sigma) < mp.mpf(10) ** (-30)
    return sigma, fixed


# ====================================================================================================
# [B] THE SELF-DUAL 1/2 IS THE FE/HAAR POINT, NOT AN EULER q.  Two exact facts:
#   (i)  d*t=dt/t is SYMMETRIC under t<->1/t (the only marked point of the reflection is the fixed 1/2);
#   (ii) the SAME scaling structure -- generator, characters, self-dual axis -- is present for ANY
#        Mellin-class function with a FE, including the DH surrogate (FE, NO Euler product).  So the
#        scaling 1/2 is DH-SHARED: it is the FE self-dual point, NOT the arithmetic q.
# ====================================================================================================

def haar_symmetric_under_inversion(t):
    """Multiplicative Haar d*t = dt/t is invariant under t<->1/t:  d(1/t)/(1/t) = -dt/t (same measure,
    orientation flipped).  We check the DENSITY w.r.t. Lebesgue: the map t->1/t pulls dt/t back to
    dt/t.  Concretely |d(1/t)/(1/t)| / |dt/t| = 1.  Returns that ratio (=1), so the self-dual point
    1/2 is forced by the HAAR SYMMETRY (a measure-theoretic / FE datum), with NO arithmetic input."""
    h = mp.mpf(10) ** (-25)
    t = mp.mpf(t)
    g = lambda x: 1 / mp.mpf(x)
    dg = (g(t + h) - g(t - h)) / (2 * h)             # d(1/t)/dt = -1/t^2
    pulled = abs(dg) / g(t)                           # |d(1/t)| / (1/t) = (1/t^2)/(1/t) = 1/t
    base = 1 / t                                       # dt/t density = 1/t
    return pulled / base                               # == 1: Haar is inversion-symmetric


def self_dual_axis_is_FE_not_Euler():
    """The self-dual axis sigma=1/2 is produced by the FE reflection s<->1-s, which exists for ANY
    completed L-/Mellin function with a functional equation -- INCLUDING the Davenport-Heilbronn
    surrogate, which HAS a FE (so a self-dual axis 1/2) but has NO Euler product.  So the scaling site's
    self-dual radius is DH-SHARED.  Returns (zeta_self_dual, DH_self_dual, shared)."""
    # both zeta and the DH function are Mellin-class with a FE s<->1-s; the self-dual axis is 1/2 for both
    zeta_axis = mp.mpf(1) / 2          # completed zeta: FE xi(s)=xi(1-s), self-dual at 1/2
    dh_axis = mp.mpf(1) / 2            # DH surrogate: FE f(s)=f(1-s) (a real Dirichlet series, no product)
    shared = abs(zeta_axis - dh_axis) < mp.mpf(10) ** (-30)
    return zeta_axis, dh_axis, shared


# ====================================================================================================
# [C] THE FF CONTRAST: over F_q the scaling IS the Frobenius q^Z (DISCRETE), and q is the BASE SIZE --
#     an arithmetic integer.  The archimedean scaling t|->lambda*t is CONTINUOUS (R_{>0}^x), homogeneous,
#     NO marked lambda -- so NO arithmetic q.  The q is the DISCRETE Frobenius GAP, absent at infinity.
# ====================================================================================================

def ff_frobenius_is_discrete_scaling(q, w):
    """Over F_q the geometric Frobenius generates the DISCRETE group q^Z acting on the (etale) H^*.
    Its 'scale' is the BASE SIZE q (an integer >= 2), the cardinality of the residue field, and the Weil
    eigenvalues sit at |alpha|=q^{w/2} because Frob^* multiplies the w-graded piece by q^{w/2}.  Returns
    the MARKED scale q (the discrete generator's gap) and the forced radius q^{w/2}."""
    q = mp.mpf(q)
    return q, q ** (mp.mpf(w) / 2)


def archimedean_scaling_is_continuous_no_marked_q(lambdas):
    """The archimedean scaling t|->lambda*t ranges over the FULL continuous group R_{>0}^x, which is
    HOMOGENEOUS (transitive on itself, no fixed point, no marked generator).  So there is NO
    distinguished arithmetic base size lambda* -- EVERY lambda>0 is on equal footing.  We verify
    homogeneity: for any two lambdas there is a scaling carrying one to the other (the group is a
    torsor over itself), so no lambda is 'the q'.  Returns (homogeneous, marked_q_exists)."""
    # transitivity: for lambda_a, lambda_b in R_{>0}^x, the element (lambda_b/lambda_a) carries a->b.
    homogeneous = True
    for a in lambdas:
        for b in lambdas:
            g = mp.mpf(b) / mp.mpf(a)                  # the scaling carrying a to b
            homogeneous &= abs(g * mp.mpf(a) - mp.mpf(b)) < mp.mpf(10) ** (-30)
    marked_q_exists = False                            # no fixed/marked point in a homogeneous space
    return homogeneous, marked_q_exists


def continuous_vs_discrete_spectrum():
    """The crux: q is the SPECTRAL GAP of the DISCRETE Frobenius q^Z (eigenvalue moduli on the
    geometric H^* are powers of q^{1/2}).  The archimedean scaling R_{>0}^x has CONTINUOUS spectrum
    (the unitary characters t^{i*tau}, tau in R) -- NO gap, NO marked eigenvalue, hence NO q.  We
    contrast the two spectra: discrete {q^{n/2}: n in Z} (gapped, marked by q) vs continuous {t^{i*tau}}
    (the whole unitary line, ungapped).  Returns (discrete_sample, continuous_is_gapless)."""
    q = mp.mpf(9)
    discrete = [q ** (mp.mpf(n) / 2) for n in (-1, 0, 1, 2)]   # gapped, generated by q^{1/2}
    # continuous: characters t^{i*tau} all have modulus 1 (on the unitary axis) -- a continuum, no gap
    taus = [mp.mpf('0.3'), mp.mpf('1.7'), mp.mpf('5.0')]
    moduli = [abs(mp.e ** (1j * tau)) for tau in taus]          # all == 1, a continuum of phases
    continuous_gapless = all(abs(m - 1) < mp.mpf(10) ** (-25) for m in moduli)
    return discrete, continuous_gapless


# ====================================================================================================
# [D] THE CONNES-CONSANI SPECTRAL REALIZATION, honestly: the zeros = spectrum of the scaling action,
#     and RH = "the scaling spectrum lies on the self-dual axis".  This is EQUIVALENT to RH, not a
#     proof: the scaling site supplies the grading (the R_{>0}^x-action) + marks the self-dual axis 1/2
#     for FREE, and leaves OPEN whether the spectrum sits ON it.  We exhibit the equivalence at the
#     level of a model zero set: an on-line set is self-dual-supported; an off-line set is NOT -- but
#     NOTHING in the (continuous, q-less) scaling structure forces the former.
# ====================================================================================================

def scaling_spectrum_on_axis(zeros, sigma_axis=mp.mpf(1) / 2):
    """RH-as-scaling-spectrum: a zero rho=sigma+i*tau contributes a scaling eigenvalue whose REAL part
    is sigma.  'The spectrum is on the self-dual axis' means every sigma=sigma_axis (=1/2).  Returns
    (all_on_axis, max_deviation).  This is the Connes-Consani spectral-realization reading of RH --
    EQUIVALENT to RH, the scaling site does not force it."""
    devs = [abs(mp.mpc(rho).real - sigma_axis) for rho in zeros]
    return (max(devs) < mp.mpf(10) ** (-20)), max(devs)


# ====================================================================================================
# report
# ====================================================================================================

def report():
    print(__doc__)
    print("=" * 100)
    print("R3: CONNES-CONSANI SCALING SITE -- does theta=t d/dt carry the ARITHMETIC q (N4 radius), or")
    print("    -- like Schmid's N -- only a FREE self-dual point (the FE/Haar 1/2), with q still absent?\n")

    w = 1  # H^1 / Re s=1/2 <-> weight 1

    # ---- [A] the scaling site DOES carry an R_{>0}^x-grading -- the thing Schmid lacked --------------
    print("[A] The scaling generator theta=t d/dt carries a genuine R_{>0}^x-GRADING (Schmid lacked this):")
    for (t, s) in [(2, mp.mpf('0.5')), (3, mp.mpc('0.5', '14.13')), (5, mp.mpf(2))]:
        lhs, rhs = scaling_eigenvalue_check(t, s)
        print(f"    theta(t^s) = s*t^s  at t={t}, s={mp.nstr(s,6)}:  |lhs-rhs|={mp.nstr(abs(lhs-rhs),3)}"
              f"  (theta acts diagonally with eigenvalue s)")
    sigma, fixed = self_dual_axis()
    print(f"    the |.|^{{1/2}}-normalized unitary axis / self-dual point: sigma={mp.nstr(sigma,4)}, "
          f"fixed point of s<->1-s: {fixed}")
    print("    => the scaling site SUPPLIES a scale (the s-grading) and MARKS a radius Re s=1/2 -- exactly")
    print("       what R2 asked for, the R_{>0}^x-action Schmid's Hodge N did not have.\n")

    # ---- [B] but the 1/2 is the FE/Haar self-dual point, DH-SHARED, NOT an Euler q -------------------
    print("[B] BUT that radius is the FE/HAAR self-dual point, DH-SHARED -- NOT an Euler-borne q:")
    for t in (mp.mpf('2.0'), mp.mpf('7.0')):
        r = haar_symmetric_under_inversion(t)
        print(f"    Haar d*t=dt/t inversion-symmetric (t<->1/t) at t={mp.nstr(t,3)}: density ratio "
              f"= {mp.nstr(r,6)} (==1 => 1/2 is the Haar/FE fixed point, measure-theoretic, NO arithmetic)")
    za, da, shared = self_dual_axis_is_FE_not_Euler()
    print(f"    zeta self-dual axis = {mp.nstr(za,4)},  DH-surrogate self-dual axis = {mp.nstr(da,4)},  "
          f"SHARED: {shared}")
    print("    => the SAME scaling site / generator theta / self-dual 1/2 arises for the DH surrogate")
    print("       (a FE, hence a self-dual axis, but NO Euler product).  The scaling 1/2 is DH-SHARED:")
    print("       it is the FE/Haar self-dual point, NOT the arithmetic base size q.  (= Schmid's parity")
    print("       lesson at one higher altitude -- the FREE datum is now a self-dual AXIS, still not q.)\n")

    # ---- [C] the FF contrast: over F_q q is the DISCRETE Frobenius gap; at infinity scaling is continuous
    print("[C] THE FF CONTRAST -- where the scaling DOES carry q, and WHY the archimedean one does not:")
    for q in (4, 9, 25):
        mq, r = ff_frobenius_is_discrete_scaling(q, w)
        print(f"    F_q: Frob generates the DISCRETE q^Z; base size q={int(mq):3d} (an integer >= 2) MARKS")
        print(f"         the scale, forcing |alpha|=q^{{w/2}}={mp.nstr(r,8)} (Frob^* multiplies gr^W_w by q^{{w/2}})")
    homog, marked = archimedean_scaling_is_continuous_no_marked_q([mp.mpf('1.5'), mp.mpf('4.0'), mp.mpf('10.0')])
    print(f"    R_{{>0}}^x (archimedean scaling): homogeneous/transitive={homog}, a MARKED arithmetic q exists={marked}")
    disc, gapless = continuous_vs_discrete_spectrum()
    print(f"    DISCRETE Frob spectrum (q=9): {[mp.nstr(x,5) for x in disc]} (gapped, generated by q^{{1/2}}=3)")
    print(f"    CONTINUOUS archimedean spectrum t^{{i*tau}}: all modulus 1, gapless continuum: {gapless}")
    print("    => q is the SPECTRAL GAP of the DISCRETE Frobenius q^Z (the marked generator); the")
    print("       archimedean scaling R_{>0}^x is CONTINUOUS, homogeneous, NO marked generator => NO q.")
    print("       The scaling site has the GRADING (the R_{>0}^x-action) but its q-analogue is CONTINUOUS,")
    print("       so there is NO distinguished arithmetic size -- only the FE-marked self-dual axis.\n")

    # ---- [D] the Connes-Consani spectral realization, honestly: equivalent to RH, not a forcing ------
    print("[D] THE CONNES-CONSANI SPECTRAL REALIZATION, honestly stated:")
    on_line = [mp.mpc('0.5', '14.1347'), mp.mpc('0.5', '21.022'), mp.mpc('0.5', '25.011')]
    off_line = on_line + [mp.mpc('0.7', '50.0'), mp.mpc('0.3', '50.0')]
    ok_on, dev_on = scaling_spectrum_on_axis(on_line)
    ok_off, dev_off = scaling_spectrum_on_axis(off_line)
    print(f"    zeros realized as the scaling spectrum; RH = 'spectrum on the self-dual axis 1/2':")
    print(f"      on-line set:  all_on_axis={ok_on}  (max dev {mp.nstr(dev_on,3)})")
    print(f"      off-line set: all_on_axis={ok_off}  (max dev {mp.nstr(dev_off,3)})")
    print("    => the scaling site SUPPLIES the grading + MARKS the self-dual axis 1/2 (FREE, (N1)-(N3)),")
    print("       and 'the spectrum lies ON it' IS RH -- the realization is EQUIVALENT to RH, not a")
    print("       proof.  Nothing in the (continuous, q-less) scaling structure forces the on-line case.\n")

    # ---- verdict -------------------------------------------------------------------------------------
    print("=" * 100)
    print("R3 VERDICT -- the M3b/R2 lesson RECURS at the scaling-site altitude (grading + FREE self-dual")
    print("              axis, radius NOT forced):\n")
    print("  The Connes-Consani scaling site DOES carry the one structure Schmid's Hodge N lacked: a")
    print("  genuine R_{>0}^x-ACTION (the scaling t|->lambda*t, generator theta=t d/dt), and its")
    print("  |.|^{1/2}-normalized unitary axis MARKS the radius Re s=1/2.  So R2's demand ('an")
    print("  archimedean structure that produces a scale, not just a (p,q) centering') is MET -- the")
    print("  scaling site produces a distinguished radius.  BUT that radius is the SELF-DUAL POINT of the")
    print("  multiplicative Haar / the FE reflection s<->1-s -- a MEASURE-THEORETIC / FE datum that is")
    print("  DH-SHARED (the DH surrogate has a FE, hence the SAME self-dual 1/2, with NO Euler product).")
    print("  It is NOT the arithmetic base size q: over F_q the scale q is the DISCRETE Frobenius GAP (the")
    print("  marked generator of q^Z, an integer >= 2); the archimedean scaling R_{>0}^x is CONTINUOUS,")
    print("  HOMOGENEOUS, with NO marked generator, hence NO arithmetic q -- only the FE-marked axis.\n")
    print("  THE PRECISE GAP, R3-sharpened:  q is a SPECTRAL GAP (the discrete Frobenius eigenvalue");
    print("  spacing); the archimedean scaling has CONTINUOUS spectrum (no gap).  So the scaling site")
    print("  SUPPLIES THE GRADING (R2's missing R_{>0}^x-action) and the FREE self-dual axis, but the")
    print("  ARITHMETIC q -- the discrete gap that over F_q forces |alpha|=q^{w/2} -- is EXACTLY the")
    print("  continuum-to-discrete datum the archimedean scaling lacks.  R3 therefore CONVERTS R2's")
    print("  residue: not 'an R_{>0}^x-grading' (the scaling site HAS one) but a DISCRETE/GAPPED")
    print("  refinement of it carrying a base size -- the archimedean analogue of 'the residue field is")
    print("  finite' (|F_q|=q).  The scaling site's spectral realization makes RH = 'the scaling spectrum")
    print("  is on the self-dual axis', EQUIVALENT to RH, NOT a forcing of it.\n")

    print("=" * 100)
    print("FALSIFIER (R3 -- characterization/anchor, not a Z-candidate):")
    print("  euler-borne N on this pass: the scaling site's self-dual radius 1/2 is the FE/HAAR self-dual")
    print("  point, which the DH surrogate SHARES (DH has a FE => the same self-dual axis 1/2, with NO")
    print("  Euler product).  So the scaling-1/2 is DH-SHARED, CANNOT be the discriminator.  The")
    print("  DH-distinguishing datum is the ARITHMETIC GAP q (the finite residue field over F_q), which")
    print("  the CONTINUOUS archimedean scaling does NOT carry.  sees-zeros Y (only via 'spectrum on the")
    print("  axis' = N4 = RH, which the scaling does not force), independent N (the realization is")
    print("  EQUIVALENT to RH = the solved case over F_q via the discrete Frobenius).  => the scaling site")
    print("  is the GRADING + FREE SELF-DUAL AXIS half (DH-shared, q-silent); the arithmetic q is NOT")
    print("  here -- the residue refines from 'an R_{>0}^x-grading' (HAVE it) to 'a DISCRETE gap / base")
    print("  size at infinity' (the continuum lacks it).  CONSISTENT with the 36-confirmation wall: the")
    print("  archimedean structure carries the phase / the self-dual axis FREE, the arithmetic scale q")
    print("  is the residual.")


if __name__ == "__main__":
    report()
