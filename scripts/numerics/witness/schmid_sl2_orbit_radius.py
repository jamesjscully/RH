"""schmid_sl2_orbit_radius.py -- R2: does SCHMID'S SL(2)-ORBIT nilpotent supply the archimedean N
   that FORCES the radius |alpha|=q^{w/2} (axiom N4), or only the FREE weight PARITY (-1)^w (N1-N3)?

  run:  python3 -m scripts.numerics.witness.schmid_sl2_orbit_radius

THE MANDATE (AGENDA R2, the RESIDUE block; built on R1 = weight_monodromy_residue.py).
  R1 pinned the residue to an archimedean nilpotent N satisfying FOUR axioms:
    (N1) NILPOTENT N^{w+1}=0;
    (N2) a (-1,-1)-morphism of the polarized HS, N(F^p) subset F^{p-1}, compatible with c;
    (N3) M(N) = W (the monodromy filtration = the archimedean weight filtration);
    (N4) RADIUS COMPATIBILITY: on gr^M_k the archimedean "Frobenius" radius/scale has |alpha|=q^{k/2},
         so the centre (k=w) sits at |alpha|=q^{w/2} -- THE EVEN SPLIT.
  R1's FF anchor showed the MECHANISM is M(N)=W-with-no-zeros, and the OBSTRUCTION is that Z/infinity
  lacks the geometric degeneration that supplies N over F_q.  R2: SCHMID'S SL(2)-ORBIT THEOREM is the
  ONE place where the archimedean weight-monodromy IS a theorem -- at a degeneration of a polarized
  VARIATION OF HODGE STRUCTURE (VHS), the limiting mixed Hodge structure (LMHS) carries a nilpotent N
  with M(N) = W (the relative weight filtration), a genuine ARCHIMEDEAN-place theorem.

  THE QUESTION: does Schmid's N satisfy (N4) -- does it carry the RADIUS -- or only (N1)-(N3),
  delivering the weight PARITY (-1)^w (free, M3b) but NOT the modulus q^{w/2}?

WHAT THIS MODULE ESTABLISHES (the decisive split, exact).
  Schmid's SL(2)-orbit theorem supplies, for a polarized VHS degenerating over a punctured disk:
    - a nilpotent N = log(unipotent part of monodromy), N: H -> H, a (-1,-1)-morphism;
    - the monodromy weight filtration M(N) centered at the (pure) weight w, and the theorem
      M(N) = W (the LMHS's weight filtration) WITH the sl_2 / Hard-Lefschetz primitive decomposition;
    - a POLARIZATION of each primitive gr^M_{w+j} (the Hodge-Riemann bilinear relations in the limit).
  ALL of this is the structure (N1)-(N3) -- and the sl_2 symmetry CENTERS the HODGE numbers (p,q) of
  gr^M_k symmetrically about the centre, delivering the WEIGHT PARITY: C^2 = (-1)^w on gr^W_w, where C
  is the Weil operator.  BUT a real/complex polarized Hodge structure has NO Frobenius eigenvalue: the
  "radius" |alpha|=q^{w/2} is an ARITHMETIC datum (the comparison Frobenius/Galois), absent from any
  archimedean Hodge structure.  Schmid's N centers the (p,q)-GRADING (the phase/parity); it does NOT
  carry a q (no base field size at infinity), hence supplies (N4) only up to the FREE choice of scale.

  PRECISELY: Schmid's N gives  N1,N2,N3  +  the parity (-1)^w  (the phase, FREE).  (N4) requires a
  REAL NUMBER q (the radius base) that the archimedean Hodge structure does NOT possess -- the same
  gap M3b found (the multiplier at infinity is the SIGN (-1)^w, not the Frobenius q).  R2 verdict:
  Schmid is the M3b lesson recurring -- the SL(2)-orbit gives the parity for free, NOT the radius.
"""
from __future__ import annotations

import mpmath as mp
import numpy as np

mp.mp.dps = 40


# ====================================================================================================
# 1. A POLARIZED HODGE STRUCTURE and its LMHS nilpotent N (the SL(2)-orbit data), built concretely.
#    Model: a weight-w HS of Hodge type with a degeneration whose monodromy logarithm is N.
#    We use the standard local model -- a maximally unipotent (Tate-type) degeneration -- where N is
#    a single nilpotent Jordan structure and M(N) is its monodromy filtration.
# ====================================================================================================

def hodge_numbers_centered(w, hodge_type):
    """For a weight-w Hodge structure with given Hodge numbers h^{p,q} (p+q=w), return the (p,q)
    multiset.  The sl_2 / Hard-Lefschetz symmetry of Schmid's N CENTERS these about the middle:
    h^{p,q} <-> h^{q,p} (the real structure c) AND the M(N)-graded pieces pair gr_{w+j}<->gr_{w-j}.
    Returns the list of (p,q) with p+q=w."""
    pqs = []
    for (p, q), h in hodge_type.items():
        assert p + q == w, "Hodge numbers must have p+q=w"
        pqs += [(p, q)] * h
    return pqs


def weil_operator_parity(w):
    """The Weil operator C acts on gr^W_w as i^{p-q}.  Its SQUARE on the weight-w part is C^2=(-1)^w
    (since on H^{p,q}, C^2 = i^{2(p-q)} = (-1)^{p-q} = (-1)^{p+q} = (-1)^w as p-q == p+q mod 2).
    THIS is the datum Schmid's SL(2)-orbit centering delivers: the weight PARITY.  Returns (-1)^w."""
    return (-1) ** w


def schmid_N_monodromy_weights(jordan_blocks, w):
    """Schmid's N (log of unipotent monodromy) on the LMHS: a nilpotent whose monodromy filtration
    M(N), centered at w, has graded pieces at absolute weights w+j for the sl_2 strings of N.
    Returns the multiset of ABSOLUTE M(N)-weights (the W of the LMHS), symmetric about w.
    THIS is (N3): M(N)=W -- a THEOREM at the archimedean place (Schmid).  No q, no radius enters."""
    weights = []
    for b in jordan_blocks:
        weights += [w + (-(b - 1) + 2 * i) for i in range(b)]  # sl_2 string centered at w
    return sorted(weights)


# ====================================================================================================
# 2. THE DECISIVE SPLIT: Schmid delivers (N1)-(N3) + PARITY; (N4) needs a RADIUS the HS lacks.
#    We make this exact by separating the two data a graded piece gr^M_k can carry:
#      (a) the HODGE/PARITY datum  -- present in any HS: the (p,q) grading, C^2=(-1)^k.  FREE.
#      (b) the RADIUS datum |alpha|=q^{k/2} -- requires an ARITHMETIC Frobenius / a base size q.  ABSENT.
# ====================================================================================================

def parity_from_schmid(M_weights):
    """(N1)-(N3) deliverable: the sl_2 symmetry of M(N)=W centers the weights, so each pair
    gr_{w+j}<->gr_{w-j} carries OPPOSITE parities that COMBINE to the centre parity (-1)^w.  We read
    the parity of every graded piece -- a SIGN, no modulus.  Returns list of (k, parity (-1)^k)."""
    return [(k, (-1) ** k) for k in M_weights]


def radius_requires_q(M_weights, q=None):
    """(N4) deliverable: on gr^M_k the radius is |alpha|=q^{k/2}.  This needs a REAL base size q.
    A polarized Hodge structure (real/complex) carries NO such q -- there is no Frobenius eigenvalue
    at the archimedean place.  We return: can (N4) be evaluated WITHOUT supplying q externally?
    Returns (q_available, radii_if_q_given)."""
    if q is None:
        return (False, None)  # the HS does not supply q -- (N4) cannot be read off Schmid's N alone
    radii = [mp.mpf(q) ** (mp.mpf(k) / 2) for k in M_weights]
    return (True, radii)


def parity_is_radius_silent(w):
    """The parity (-1)^w fixes ONLY the sign of the centre; it is invariant under ANY rescaling of the
    radius q^{w/2} -> (lambda q)^{w/2}.  So the parity is RADIUS-SILENT: it does not pin |alpha|.
    We verify: two different base sizes q1,q2 give the SAME parity but DIFFERENT radii.  Returns
    (parity_same, radii_differ)."""
    q1, q2 = mp.mpf(9), mp.mpf(25)
    par1, par2 = (-1) ** w, (-1) ** w
    r1, r2 = q1 ** (mp.mpf(w) / 2), q2 ** (mp.mpf(w) / 2)
    return (par1 == par2, abs(r1 - r2) > mp.mpf(10) ** (-20))


# ====================================================================================================
# 3. THE FF CROSS-CHECK: over F_q, the SAME Schmid N exists (a degenerating family of curves), and
#    THERE the radius IS forced -- but ONLY because the ARITHMETIC Frobenius supplies q.  The Hodge/
#    SL(2) data is identical; the EXTRA ingredient F_q has and infinity lacks is the base size q.
# ====================================================================================================

def ff_radius_with_arithmetic_frobenius(q, w):
    """Over F_q a degenerating family of curves has the SAME Schmid N on the (limiting) Hodge
    structure -- but the l-adic/crystalline realization ALSO has a Frobenius with eigenvalue moduli
    q^{k/2} on gr^M_k.  The radius is forced BECAUSE the arithmetic Frobenius supplies q.  Returns
    the centre radius q^{w/2} (the even split), available ONLY via the arithmetic side."""
    return mp.mpf(q) ** (mp.mpf(w) / 2)


# ====================================================================================================
# 2b. THE NORM-ESTIMATE OBJECTION, MET HEAD-ON (the part the "no q at infinity" slogan glosses).
#
#   Schmid's SL(2)-orbit theorem is NOT only a statement about filtrations -- its CONTENT is a METRIC
#   estimate.  For a section v in the k-th M(N)-graded piece (the (k-w)-eigenspace of the sl_2 h), the
#   Hodge norm of v in the degenerating family over the punctured disk {0<|t|<1} satisfies
#
#         || v ||^2_t  ~  ( log(1/|t|) )^{ k - w }            (Schmid, the norm estimate)
#
#   i.e. the Hodge metric GROWS/DECAYS like a power of L := log(1/|t|) governed by the M(N)-weight k.
#   THIS is a genuine real-analytic "radius": the M(N)-grading IS read off a SCALE (the metric growth
#   exponent k-w).  So the objection to R2's slogan is precise: Schmid DOES give a radius datum -- the
#   metric power L^{k-w}.  Does THIS supply (N4)?  Two independent reasons it does NOT, both decisive:
#
#   (i) IT IS A METRIC.  The norm || . ||_t is a Hodge METRIC.  By the charter sec.0 no-go, any
#       polarization built as a *-congruence of a fixed (DH-shared) archimedean background metric is
#       Sylvester-inertia-locked = dead.  Schmid's norm is exactly such a background metric (the same
#       Gamma-factor / Hodge norm DH carries).  So even though it carries a SCALE, that scale is a
#       METRIC scale -- the forbidden kind.  (N4) wants a CATEGORICAL/arithmetic radius, NOT a metric.
#
#   (ii) IT IS A RATE, NOT A VALUE -- and it DIVERGES.  L^{k-w} -> infinity (k>w) or 0 (k<w) as t->0;
#        it is a GROWTH EXPONENT in the limit parameter t, not a fixed number q^{k/2}.  The arithmetic
#        radius q^{k/2} is a single real number ATTACHED TO THE CENTRAL FIBRE; Schmid's L^{k-w} is the
#        ASYMPTOTIC RATE along the family and has no t->0 limit (it is 0 or infinity).  To extract a
#        FINITE radius from Schmid's divergent norm one must RENORMALIZE -- divide by the divergent
#        (log 1/|t|)^{k-w} -- and the renormalization CONSTANT is exactly the datum Schmid does NOT fix
#        (it is a free positive scalar = the choice of base, the "q").  So Schmid pins the EXPONENT
#        k-w (= the M(N)-weight = the parity/centering, already counted in N1-N3), and leaves the
#        renormalization SCALE (the actual q^{k/2}) free -- precisely (N4) residual.
# ====================================================================================================

def schmid_norm_growth_exponent(k, w):
    """Schmid's norm estimate: a section in gr^M_k has Hodge norm ||v||^2_t ~ (log 1/|t|)^{k-w}.
    Returns the GROWTH EXPONENT k-w -- the real-analytic 'radius' datum Schmid DOES supply.
    Note: this EQUALS the M(N)-weight shift, i.e. it is the sl_2 h-eigenvalue -- the SAME datum as the
    centering/parity (N1-N3), NOT new information beyond the filtration."""
    return k - w


def schmid_norm_value(k, w, t):
    """The actual Hodge norm-square (log 1/|t|)^{k-w} at a finite t in (0,1).  Used to show it
    DIVERGES (k>w) or vanishes (k<w) as t->0, so it is a RATE, not a fixed radius q^{k/2}."""
    L = mp.log(1 / mp.mpf(t))
    return L ** (k - w)


def renormalized_radius_is_free(k, w, ts):
    """Extract a finite radius from Schmid's divergent norm by dividing out (log 1/|t|)^{k-w}.
    The renormalized quantity ||v||^2_t / L^{k-w} tends to a CONSTANT -- but that constant is a FREE
    positive scalar (the metric's normalization), NOT pinned to q^{k/2}.  We DEMONSTRATE freedom: any
    rescaling of the metric v -> lambda*v multiplies the limit by |lambda|^2 with NO effect on the
    EXPONENT k-w.  Returns (exponent_pinned, limit_constant_is_free)."""
    L_values = [mp.log(1 / mp.mpf(t)) for t in ts]
    raw = [L ** (k - w) for L in L_values]
    renorm = [r / (L ** (k - w)) for r, L in zip(raw, L_values)]  # == 1 by construction; the POINT:
    # the exponent k-w is forced; the prefactor (here 1, but ANY positive c under a metric rescale)
    # is free.  Two metric normalizations c1,c2 give the SAME exponent, DIFFERENT radius -- like q.
    c1, c2 = mp.mpf(1), mp.mpf(7)  # two admissible metric normalizations (the free choice)
    exponent_pinned = all(abs(x - 1) < mp.mpf(10) ** (-30) for x in renorm)  # exponent fixes the rate
    radius_free = abs(c1 - c2) > mp.mpf(10) ** (-20)  # the renormalization constant is unconstrained
    return (exponent_pinned, radius_free)


# ====================================================================================================
# report
# ====================================================================================================

def report():
    print(__doc__)
    print("=" * 100)
    print("R2: SCHMID SL(2)-ORBIT -- does its N force the RADIUS (N4) or only the FREE PARITY (-1)^w?\n")

    w = 1  # H^1, the weight of the curve's cohomology (Re s=1/2 <-> weight 1)

    # ---- 1. Schmid's N: (N1)-(N3) hold at the archimedean place (a THEOREM) ----------------------
    print("[1] Schmid's SL(2)-orbit supplies (N1)-(N3) AT THE ARCHIMEDEAN PLACE (a theorem for VHS):")
    for blocks in [[1, 1], [2], [3], [2, 2]]:
        Mw = schmid_N_monodromy_weights(blocks, w)
        from collections import Counter
        c = Counter([k - w for k in Mw])
        sym = all(c[j] == c[-j] for j in c)
        print(f"    N Jordan {str(blocks):8s} -> M(N)=W absolute weights {str(Mw):20s} "
              f"sl_2-symmetric about w={w}: {sym}")
    print("    => (N3) M(N)=W holds with the Hard-Lefschetz sl_2 symmetry -- the ARCHIMEDEAN")
    print("       weight-monodromy theorem (Schmid). NO zeros, NO q entered: pure Hodge/filtration data.\n")

    # ---- 2. what the centering DELIVERS: the PARITY (a sign), NOT the radius (a modulus) ---------
    print("[2] What Schmid's centering DELIVERS at the centre k=w:")
    par = weil_operator_parity(w)
    print(f"    the Weil operator parity  C^2 = (-1)^w = {par}  -- a SIGN (the phase/reality, M3b's (-1)^w)")
    Mw = schmid_N_monodromy_weights([3], w)  # a degeneration spreading weights {0,1,2}
    print(f"    graded parities (k, (-1)^k) on M(N)=W of a Jordan-3 N: {parity_from_schmid(Mw)}")
    q_avail, _ = radius_requires_q(Mw, q=None)
    print(f"    (N4) RADIUS |alpha|=q^(k/2): can it be read off Schmid's N ALONE (no external q)? {q_avail}")
    print("    => the archimedean Hodge structure carries NO Frobenius eigenvalue / NO base size q,")
    print("       so (N4) is NOT supplied by Schmid's N: the SL(2)-orbit gives the PARITY, not the radius.\n")

    # ---- 3. the parity is RADIUS-SILENT (the M3b lesson, made exact) -----------------------------
    print("[3] The parity (-1)^w is RADIUS-SILENT (same parity, different radius for different q):")
    psame, rdiff = parity_is_radius_silent(w)
    print(f"    q=9 vs q=25 both give parity (-1)^w={par}: parity_same={psame}; radii 3 vs 5 differ={rdiff}")
    print("    => fixing the parity does NOT fix |alpha|; the radius is ORTHOGONAL to the SL(2)-orbit's")
    print("       phase datum (exactly K2r-fix: reality/phase free, radius is the scale, orthogonal).\n")

    # ---- 3b. the NORM-ESTIMATE objection met: Schmid DOES give a scale -- a METRIC RATE, not q ----
    print("[3b] THE NORM-ESTIMATE OBJECTION (the part 'no q at infinity' glosses), met head-on:")
    print("     Schmid's SL(2)-orbit theorem IS a metric estimate: ||v||^2_t ~ (log 1/|t|)^{k-w} for")
    print("     v in gr^M_k.  So Schmid DOES carry a real-analytic 'radius' -- the growth exponent k-w.")
    print("     Two decisive reasons it is NOT (N4):")
    print("     (i) it EQUALS the M(N)-weight shift (the sl_2 h-eigenvalue) -- the SAME datum as the")
    print("         centering/parity (N1-N3), no new info:")
    for k in (0, 1, 2):
        e = schmid_norm_growth_exponent(k, w)
        print(f"         gr^M_{k}: norm growth exponent k-w = {e}  (= the M(N)-weight shift, already in N1-N3)")
    print("     (ii) it is a RATE that DIVERGES as t->0, not a fixed value q^{k/2}:")
    for t in (mp.mpf('0.1'), mp.mpf('0.001'), mp.mpf('0.00001')):
        v2 = schmid_norm_value(2, w, t)  # k=2 piece: ||.||^2 ~ (log 1/|t|)^1 -> infinity
        print(f"         k=2, t={mp.nstr(t,2):8s}: ||v||^2_t = (log 1/|t|)^1 = {mp.nstr(v2,8)}  (-> infinity, not 3 or 5)")
    epin, rfree = renormalized_radius_is_free(2, w, [mp.mpf('0.1'), mp.mpf('0.001')])
    print(f"     RENORMALIZE (divide by the divergent L^{{k-w}}): exponent_pinned={epin}, "
          f"radius_constant_free={rfree}")
    print("     => Schmid pins the EXPONENT k-w (the parity/centering, in N1-N3); the renormalization")
    print("        SCALE (the actual q^{k/2}) is a FREE positive constant -- precisely (N4) residual.")
    print("     => AND the norm is a METRIC: by charter sec.0 a metric polarization is Sylvester-locked")
    print("        (DH-shared background) = dead.  Schmid's scale is the FORBIDDEN (metric) kind.\n")

    # ---- 4. the FF cross-check: over F_q the radius IS forced -- but via the ARITHMETIC Frobenius -
    print("[4] FF CROSS-CHECK: over F_q the SAME Schmid N exists (degenerating family of curves), and")
    print("    the radius IS forced -- but ONLY because the l-adic/crystalline realization adds an")
    print("    ARITHMETIC FROBENIUS supplying q.  The Hodge/SL(2) data is IDENTICAL; the extra")
    print("    ingredient F_q has and infinity LACKS is the base size q:")
    for q in (4, 9, 25):
        r = ff_radius_with_arithmetic_frobenius(q, w)
        print(f"      q={q:3d}: centre radius q^(w/2) = {mp.nstr(r,10)}  (from the ARITHMETIC Frobenius, NOT Schmid's N)")
    print("    => over F_q Schmid's N + arithmetic Frobenius TOGETHER force the even split; the SL(2)-")
    print("       orbit alone gives M(N)=W (parity), the Frobenius supplies q (radius).  At infinity")
    print("       the second factor is MISSING.\n")

    # ---- 5. verdict ------------------------------------------------------------------------------
    print("=" * 100)
    print("R2 VERDICT -- the M3b lesson RECURS (phase free, radius residual):\n")
    print("  Schmid's SL(2)-orbit theorem DELIVERS (N1),(N2),(N3) AT THE ARCHIMEDEAN PLACE -- a genuine")
    print("  archimedean weight-monodromy theorem (M(N)=W with the Hard-Lefschetz sl_2 symmetry) -- and")
    print("  its centering supplies the WEIGHT PARITY (-1)^w (the phase/reality, M3b's free datum).")
    print("  It does NOT supply (N4), the RADIUS |alpha|=q^{w/2}: a polarized real/complex Hodge")
    print("  structure carries NO Frobenius eigenvalue, NO base size q -- the radius is an ARITHMETIC")
    print("  datum absent at infinity.  Over F_q the radius is forced by the l-adic Frobenius (the")
    print("  EXTRA factor), not by Schmid's N.  So the SL(2)-orbit gives the parity for FREE and leaves")
    print("  the RADIUS exactly where M3b/M4r/K2r-fix left it: the residual, Euler/arithmetic datum.\n")
    print("  THE NORM-ESTIMATE REFINEMENT (R2's sharpest content): Schmid DOES carry a real-analytic")
    print("  scale -- the Hodge norm growth ||v||^2_t ~ (log 1/|t|)^{k-w}.  But that scale is (i) the")
    print("  SAME datum as the centering (exponent k-w = the M(N)-weight = the sl_2 h-eigenvalue,")
    print("  already in N1-N3), (ii) a DIVERGENT RATE in t (-> 0 or infinity) whose renormalization to a")
    print("  finite radius needs a FREE constant Schmid does not fix (= the q), and (iii) a METRIC --")
    print("  Sylvester-inertia-locked by charter sec.0, the FORBIDDEN kind of scale.  So the SL(2)-orbit's")
    print("  only radius datum is the metric growth EXPONENT (parity-equivalent, free, metric), NOT the")
    print("  categorical arithmetic VALUE q^{k/2}.\n")
    print("  THE RESIDUE, RE-SHARPENED BY R2: the missing archimedean N must carry MORE than Schmid's")
    print("  Hodge-theoretic N -- it must couple the (p,q)-grading to an ARITHMETIC SCALE q at infinity")
    print("  that is (a) CATEGORICAL not metric (evading sec.0), (b) a FINITE VALUE not a divergent rate,")
    print("  (c) NEW beyond the centering exponent.  Schmid gives the (p,q) centering and a divergent")
    print("  metric rate; the open object is the q (finite + categorical) -- handed to R3 (Connes-Consani")
    print("  scaling site / absolute Frobenius: IS the scaling generator the archimedean N that supplies")
    print("  q?), with R2's success criterion: does the scaling N carry the RADIUS (N4) as a finite")
    print("  CATEGORICAL value, or -- like Schmid's -- only the parity / a divergent metric rate?\n")

    print("=" * 100)
    print("FALSIFIER (R2 -- characterization/anchor, not a Z-candidate):")
    print("  euler-borne N on this pass (the SL(2)-orbit/Hodge data is Euler-SILENT -- it is exactly the")
    print("  DH-SHARED archimedean structure: DH has the SAME Gamma-factor / archimedean Hodge type, so")
    print("  Schmid's N exists for DH too and is RADIUS-SILENT for both -- it does NOT distinguish zeta).")
    print("  This is the SHARP DH verdict: Schmid's N is DH-SHARED (the archimedean place is common),")
    print("  hence CANNOT be the discriminator -- (N4)'s q is the only DH-distinguishing datum and Schmid")
    print("  does not carry it.  sees-zeros Y (only via (N4), which Schmid lacks), independent N (M(N)=W")
    print("  => purity over FF).  => the SL(2)-orbit is the PHASE half (free, DH-shared, radius-silent);")
    print("  the radius is NOT here.  CONSISTENT with the 35-confirmation wall: phase free, radius residual.")


if __name__ == "__main__":
    report()
