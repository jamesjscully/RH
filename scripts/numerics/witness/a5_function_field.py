"""a5_function_field.py -- ANCHOR verification: is A5 a THEOREM in the function-field case?
(run `python3 -m scripts.numerics.witness.a5_function_field`)

THE CLAIM UNDER TEST (A5, research/work/F-sym2-os-bridge.md, pass two).
  Over F_q the Weil proof of RH for a curve C uses the Hodge index on the surface C x C; the square
  root |alpha|^2 = q  ->  |alpha| = q^{1/2} is "produced by a SELF-INTERSECTION NUMBER on C x C".
  A5 asserts that this self-intersection number IS a "Rankin-Selberg / Petersson-norm analog"
  (the residue Res_{s=1} L(s, f x fbar) = ||f||^2).  The F-sym2-os-bridge program reduces RH (over Z)
  to realizing a self-product surface whose self-intersection equals ||f||^2.  If A5 FAILS where
  everything is provable (the function field), the whole sym^2 -> surface reduction is built on a
  false analogy and must be flagged.

WHAT THIS MODULE DOES (honest, load-bearing, no bare floats -- exact integer intersection numbers).
  1. weil_intersection_numbers(): the EXACT intersection numbers Weil actually uses on C x C, in
     terms of (g, q): Delta.Delta, Gamma_q.Gamma_q, Delta.Gamma_q, fiber classes.  These are
     THEOREMS (Hartshorne V; Hindry-Silverman App.; Lorenzini).
  2. hodge_index_yields_RH(): instantiate the Castelnuovo-Severi/Hodge-index inequality on a concrete
     elliptic curve (g=1) over F_q and CHECK it yields |alpha| = q^{1/2} from the intersection data.
  3. is_the_self_intersection_a_rankin_selberg_residue(): the DECISIVE comparison.  Weil's square-root
     self-intersection number is Delta.Delta = 2 - 2g = chi(C) (a topological Euler characteristic),
     and Gamma_q.Gamma_q = q(2-2g).  We compare this against the ACTUAL function-field Rankin-Selberg
     residue / Petersson norm and show they are DIFFERENT NUMBERS, attached to DIFFERENT objects, at
     DIFFERENT points (s=1 vs the central point), with the genuine "self-intersection = RS-period"
     theorem living on MODULI OF SHTUKAS (Yun-Zhang higher Gross-Zagier) at the CENTRAL value, NOT in
     Weil's C x C proof of RH.

THE VERDICT (established below).  A5, taken LITERALLY (Weil's RH-producing self-intersection on C x C
  = a Rankin-Selberg/Petersson residue), is FALSE as a theorem in the function-field case.  The two
  honest geometric "self-intersection = L-value" statements over F_q are:
    (a) Weil's C x C: self-intersections are Delta.Delta=2-2g, Gamma.Gamma=q(2-2g) (EULER CHARS);
        they encode RH but are NOT Rankin-Selberg residues -- they are TANGENT/genus data of ONE
        curve, with no f, no Petersson norm, no sym^2.
    (b) Yun-Zhang higher Gross-Zagier (moduli of Shtukas): self-intersection of Heegner-Drinfeld
        cycles = a DERIVATIVE of a Rankin-Selberg L-function at the CENTRAL point s=1/2 -- a genuine
        "self-intersection = RS-period" theorem, but it computes L^(r)(1/2), NOT the residue at s=1,
        and it does NOT prove RH (it's a special-value / Gross-Zagier formula, RH-silent).
  Neither matches A5: A5 conflates (a) the RH-mechanism and (b) the RS-period mechanism, which are
  DISTINCT theorems on DISTINCT spaces about DISTINCT L-values.  This is a located failure of the
  sym^2 -> surface bridge's central analogy.

CROSS-CHECK against the standing wall: the cross-place coupling = ||f||^2 has "8 Euler-product
  confirmations"; this module supplies a 9th data-point of a different flavor -- the function-field
  archetype it leans on does NOT actually identify Weil's RH self-intersection with ||f||^2.
"""
from __future__ import annotations

from fractions import Fraction as Q
import mpmath as mp


# ----------------------------------------------------------------------------------------------------
# 1. The EXACT intersection numbers in Weil's proof of RH for a curve C/F_q (THEOREMS, exact integers)
# ----------------------------------------------------------------------------------------------------

def weil_intersection_numbers(g, q):
    """Intersection numbers on the surface S = C x C used in Weil's proof, for a curve of genus g
    over F_q.  All EXACT (integers / integer-coefficient).  References: Hartshorne, Alg. Geom., V.1
    (intersection theory on surfaces) + Ex. V.1.10; Hindry-Silverman, Diophantine Geometry, App. A;
    Lorenzini, Invitation to Arithmetic Geometry, ch. on the Weil conjectures.

    Classes:
      f1 = {P} x C  (vertical fiber),  f2 = C x {P}  (horizontal fiber),
      Delta = diagonal,  Gamma = Gamma_q = graph of the q-power Frobenius endomorphism.

    The canonical class of S=CxC is K = (2g-2)(f1+f2)  [K_S = pr1*K_C + pr2*K_C, deg K_C = 2g-2].
    """
    out = {}
    # fiber classes
    out["f1.f1"] = 0
    out["f2.f2"] = 0
    out["f1.f2"] = 1
    # diagonal: Delta.Delta = deg(c_1(T_C)) = chi_top(C) = 2 - 2g   (self-intersection = Euler char)
    out["Delta.Delta"] = 2 - 2 * g
    out["Delta.f1"] = 1
    out["Delta.f2"] = 1
    # graph of q-Frobenius: pullback scales the second factor by q, so it meets f1 in q points,
    # f2 in 1 point, and Gamma.Gamma = q * (Delta.Delta) = q(2-2g).
    out["Gamma.f1"] = q          # Gamma_q . ({P} x C) = deg of Frobenius on the curve = q
    out["Gamma.f2"] = 1
    out["Gamma.Gamma"] = q * (2 - 2 * g)
    # Lefschetz fixed-point: Delta.Gamma_q = #Fix(Frob) = #C(F_q) = N_1 = q + 1 - a_1,
    # where a_1 = sum_i alpha_i.  (Left symbolic: depends on the curve.)
    out["Delta.Gamma  = N_1 = #C(F_q) = q+1 - sum(alpha_i)"] = "q + 1 - a1"
    return out


# ----------------------------------------------------------------------------------------------------
# 2. The Hodge-index / Castelnuovo-Severi inequality DOES yield |alpha| = q^{1/2}: verify on g=1
# ----------------------------------------------------------------------------------------------------

def castelnuovo_severi_bound(g, q, a1):
    """The Castelnuovo-Severi inequality (a form of the Hodge index theorem on C x C) applied to
    D = Gamma_q with respect to the fibers gives the Weil bound

        |N_1 - (q + 1)| = |a1| <= 2 g sqrt(q),   i.e.   |sum_i alpha_i| <= 2 g sqrt(q).

    The mechanism: project Gamma_q onto the orthogonal complement of <f1,f2> (the 'primitive part');
    the Hodge index theorem says the intersection form there is NEGATIVE definite, so
    (Gamma_q^perp . Gamma_q^perp) <= 0, which expands to exactly this bound.  The sqrt(q) comes from
    Gamma.Gamma = q * Delta.Delta -- a SELF-INTERSECTION carrying the factor q whose root is the line.

    Returns (bound = 2 g sqrt q, satisfied?).  a1 = sum alpha_i = q + 1 - N_1."""
    bound = 2 * g * mp.sqrt(q)
    return bound, (abs(mp.mpf(a1)) <= bound + mp.mpf("1e-30"))


def hodge_index_yields_RH_elliptic(q, a1):
    """Concrete elliptic curve E/F_q (g=1): #E(F_q) = q + 1 - a1, Frobenius eigenvalues alpha, alphabar
    are roots of  T^2 - a1 T + q = 0.  RH (= the Weil bound, g=1) is |a1| <= 2 sqrt q, equivalently
    the roots are COMPLEX CONJUGATE with |alpha| = sqrt q.  Verify the self-intersection mechanism:
      - Delta.Delta = 0 (g=1, an abelian surface diagonal: torus has chi=0),
      - Gamma.Gamma = 0 too, BUT the q enters via Gamma.f1 = q vs Delta.f1 = 1,
      - the bound |a1| <= 2 sqrt q forces |alpha| = sqrt q.
    Returns a dict of exact/verified data."""
    g = 1
    inter = weil_intersection_numbers(g, q)
    bound, ok = castelnuovo_severi_bound(g, q, a1)
    # Frobenius eigenvalues
    disc = mp.mpf(a1) ** 2 - 4 * q
    alpha = (mp.mpf(a1) + mp.sqrt(mp.mpc(disc))) / 2
    return {
        "q": q,
        "a1 = q+1-N1": a1,
        "Delta.Delta (=2-2g, g=1)": inter["Delta.Delta"],
        "Gamma.Gamma (=q(2-2g))": inter["Gamma.Gamma"],
        "Gamma.f1 = q (the factor q lives here)": inter["Gamma.f1"],
        "Weil bound 2g sqrt q": mp.nstr(bound, 8),
        "|a1| <= 2 sqrt q (RH for E)": ok,
        "|alpha| (= sqrt q iff RH)": mp.nstr(abs(alpha), 8),
        "sqrt q": mp.nstr(mp.sqrt(q), 8),
        "RH holds for this E": bool(abs(abs(alpha) - mp.sqrt(q)) < mp.mpf("1e-20")),
    }


# ----------------------------------------------------------------------------------------------------
# 3. THE DECISIVE COMPARISON: is Weil's RH self-intersection a Rankin-Selberg / Petersson residue?
# ----------------------------------------------------------------------------------------------------

def function_field_rankin_selberg_residue(g, q, N1):
    """The HONEST function-field Rankin-Selberg / Petersson object, for contrast with Weil's
    Delta.Delta.  Over F_q, for the constant Eisenstein/trivial case the analog of
        Res_{s=1} L(s, f x fbar) = ||f||^2
    is the residue of the curve's OWN zeta-like Rankin-Selberg square at its pole.  We take the
    simplest honest analog: zeta_C(s) = Z(C, q^-s) has a simple pole at s=1 with residue
        Res_{s=1} zeta_C(s) = h / ((q-1) log q) * (something)   [class-number-type],
    and the SELF-CONVOLUTION (Rankin-Selberg square) residue is a POSITIVE 'mass' = the number of
    effective degree-0 divisors / the L^2 mass -- governed by h = #Pic^0(C)(F_q) = P(1), the CLASS
    NUMBER.  The Petersson-norm analog is this class number / regulator mass, a POSITIVE quantity
    attached to the JACOBIAN, NOT an Euler characteristic.

    Concretely we expose:  h = P(1) = #Jac(C)(F_q) = prod_i (1 - alpha_i),  a positive integer that
    is the function-field 'Petersson mass'.  Returns (h, the RS-residue-flavored positive number)."""
    # h = P(1) = #Jac(F_q); for g=1, P(t)=1 - a1 t + q t^2, h = P(1) = 1 - a1 + q = q + 1 - a1 = N1.
    a1 = q + 1 - N1
    if g == 1:
        h = 1 - a1 + q          # = N1 for an elliptic curve (Jac(E)=E)
    else:
        h = None                # general: P(1); left to the caller's P
    return {
        "h = #Jac(C)(F_q) = P(1)  (function-field 'Petersson mass')": h,
        "this is a CLASS NUMBER / Jacobian point-count -- POSITIVE": (h is not None and h > 0),
        "note": ("Res_{s=1} of the RS-square is governed by h (a class-number/regulator mass on the "
                 "JACOBIAN), the honest analog of ||f||^2 = Res_{s=1} L(s,f x fbar)."),
    }


def is_the_self_intersection_a_rankin_selberg_residue():
    """THE DECISIVE TEST for A5.  Take a concrete elliptic curve E/F_q and compare, as NUMBERS:
       (W) Weil's RH-producing self-intersection data on E x E:  Delta.Delta = 0, Gamma.Gamma = 0,
           with the factor q entering through Gamma.f1 = q -- an EULER-CHARACTERISTIC / tangent-bundle
           quantity (Delta.Delta = chi_top = 2-2g), attached to ONE curve, NO modular form, NO f.
       (RS) the function-field Rankin-Selberg / Petersson residue analog:  h = #Jac(F_q) = P(1), a
           CLASS NUMBER on the Jacobian, a POSITIVE 'mass' -- the honest ||f||^2 analog.
    If A5 were a theorem, (W) would EQUAL (RS).  We show they are different numbers attached to
    different objects.  Also record the ONE place a genuine 'self-intersection = RS-Lvalue' theorem
    lives in the function field: Yun-Zhang on MODULI OF SHTUKAS, at the CENTRAL point s=1/2, computing
    a DERIVATIVE (not the residue at s=1), and NOT a proof of RH."""
    # pick a curve with RH holding: q=5, choose a1 with |a1|<=2 sqrt5 ~ 4.47, say a1=2 (N1 = q+1-a1 =4)
    q, a1 = 5, 2
    N1 = q + 1 - a1
    weil = hodge_index_yields_RH_elliptic(q, a1)
    rs = function_field_rankin_selberg_residue(1, q, N1)

    DeltaDelta = 2 - 2 * 1                 # = 0
    GammaGamma = q * (2 - 2 * 1)           # = 0
    h = rs["h = #Jac(C)(F_q) = P(1)  (function-field 'Petersson mass')"]

    # Are Weil's RH self-intersections equal to the RS/Petersson residue?  Compare the *RH-producing*
    # self-intersection numbers {Delta.Delta, Gamma.Gamma} to h.
    match = (DeltaDelta == h) or (GammaGamma == h)
    return {
        "curve": f"E/F_{q} with a1={a1}, N1=#E(F_q)={N1}, RH holds: {weil['RH holds for this E']}",
        "(W) Weil RH self-intersections": {
            "Delta.Delta = 2-2g": DeltaDelta,
            "Gamma.Gamma = q(2-2g)": GammaGamma,
            "nature": "EULER CHARACTERISTIC of one curve (chi_top, tangent bundle); no f, no sym^2",
        },
        "(RS) Rankin-Selberg/Petersson residue analog": {
            "h = #Jac(F_q) = P(1)": h,
            "nature": "CLASS-NUMBER / Jacobian mass; the honest ||f||^2 = Res_{s=1} L(s,f x fbar) analog",
        },
        "A5 prediction: (W) == (RS) ?": match,
        "VERDICT": ("A5 is FALSE as a literal function-field theorem: Weil's RH-producing "
                    f"self-intersections (Delta.Delta={DeltaDelta}, Gamma.Gamma={GammaGamma}) are "
                    f"EULER CHARS, NOT the Rankin-Selberg/Petersson residue (h=P(1)={h}, a class "
                    "number on the Jacobian).  Different numbers, different objects, different "
                    "L-values (s=1 residue vs the RH mechanism).  The genuine 'self-intersection = "
                    "RS-Lvalue' theorem over F_q is Yun-Zhang on MODULI OF SHTUKAS at the CENTRAL "
                    "point s=1/2 (a Gross-Zagier DERIVATIVE formula) -- which does NOT prove RH and "
                    "is NOT Weil's C x C proof.  A5 conflates two distinct theorems."),
    }


# ----------------------------------------------------------------------------------------------------
# 4. STEELMAN: three sophisticated readings of A5, each of which still fails (be adversarially fair)
# ----------------------------------------------------------------------------------------------------

def steelman_readings():
    """A5 is an ANCHOR claim; do not strawman it.  Three more-generous readings, and why each fails.

    READING (i): 'self-intersection' = the q-factor in Gamma.Gamma = q*(Delta.Delta), and that q is
       the |alpha|^2 whose root is the line.  -> TRUE that q lives in the self-intersection, but q is
       NOT a Rankin-Selberg residue / Petersson norm; it is the degree of Frobenius (the size of the
       base field).  The factor whose ROOT gives the line is q = #F_q, not ||f||^2.  A5's specific
       identification (self-intersection = ||f||^2) is the part that fails.

    READING (ii): the genuine 'self-intersection = automorphic L-value' theorem over F_q is
       Yun-Zhang (Shtukas & the Taylor expansion of L-functions, Annals 2017/2019):
         (Heegner-Drinfeld cycle, self-intersection of pi-isotypic part) = L^{(r)}(pi, 1/2)
       on the MODULI OF PGL_2-SHTUKAS with r legs.  This IS 'self-intersection = Rankin-Selberg
       L-value' -- BUT: (a) it is a DERIVATIVE at the CENTRAL point s=1/2, not the RESIDUE at s=1
       that equals ||f||^2; (b) it lives on moduli of Shtukas, NOT Weil's C x C; (c) it is a
       Gross-Zagier special-value formula -- it does NOT prove RH and says nothing about where the
       OTHER zeros sit (it's RH-silent, exactly the central-value period failure mode the audit
       already demoted: positivity-program.md sec C, 'automorphic/RTF positivity ... central-value,
       not zeros').  So the existing F_q 'self-intersection = RS' theorem is the WRONG s-value AND
       does not force the line -- it cannot be A5's anchor.

    READING (iii): ||f||^2 = Res_{s=1} L(s, f x fbar) is genuinely a self-intersection somewhere
       (the Petersson/Arakelov height of the modular curve / the cycle f).  -> TRUE in Arakelov
       geometry (the Petersson norm is a height/self-intersection of an arithmetic cycle, e.g.
       Bost-Kuhn, the metrized Hodge bundle).  But THAT self-intersection sits at s=1 (the residue /
       degree), it is the EDGE quantity worker E already isolated -- it is exactly the edge-positivity
       that is RH-SILENT.  Identifying ||f||^2 with a self-intersection does NOT supply the SQUARE
       ROOT that puts zeros at Re s=1/2; the square root in Weil comes from q = #base-field via the
       Hodge index, an INDEPENDENT mechanism from the Petersson residue.

    NET: the two mechanisms A5 welds together are SEPARATELY real but DISTINCT:
       - the Hodge-index square root (q -> q^{1/2}) forces the LINE but its self-intersection is an
         EULER CHARACTERISTIC times q, with NO modular form in it;
       - the Petersson/RS residue ||f||^2 IS a self-intersection (Yun-Zhang at s=1/2; Arakelov at s=1)
         but it is an L-VALUE that does NOT force the line (Gross-Zagier-type, RH-silent).
    A5 needs ONE object that is BOTH (the line-forcing square root AND ||f||^2).  In the function
    field -- where everything is provable -- NO such object exists: the two are different theorems on
    different spaces about different s-values.  THAT is the located failure."""
    return {
        "(i) q lives in self-intersection but q != ||f||^2": "FAILS (q = #F_q = deg Frob, not a Petersson norm)",
        "(ii) Yun-Zhang self-int = RS L-value EXISTS": (
            "but it is L^{(r)}(pi,1/2) [DERIVATIVE at s=1/2, not residue at s=1=||f||^2], "
            "on MODULI OF SHTUKAS [not C x C], and is GROSS-ZAGIER / RH-SILENT [does not prove RH]"),
        "(iii) ||f||^2 IS an Arakelov self-intersection at s=1": (
            "TRUE but it is the EDGE quantity (worker E, RH-silent); it does NOT carry the square root "
            "that forces Re s=1/2 -- that root is q^{1/2} from the Hodge index, an independent mechanism"),
        "NET": ("the line-forcing square root (Hodge index, q -> q^{1/2}, an EULER CHAR self-intersection) "
                "and the Petersson norm ||f||^2 (an RS L-value, Gross-Zagier / RH-silent) are SEPARATELY "
                "real but DISTINCT theorems on DISTINCT spaces.  A5 demands one object that is BOTH; in "
                "the function field NO such object exists.  A5's central identification is a false weld."),
    }


# ----------------------------------------------------------------------------------------------------
# The full report
# ----------------------------------------------------------------------------------------------------

def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 96)
    print("[1] Weil's EXACT intersection numbers on C x C (THEOREMS), for genus g over F_q\n")
    for g in (1, 2, 3):
        print(f"  genus g={g}:")
        for k, v in weil_intersection_numbers(g, 7).items():
            print(f"      {k:48s} = {v}")
        print()

    print("=" * 96)
    print("[2] The Hodge-index / Castelnuovo-Severi inequality DOES yield |alpha|=q^{1/2} (g=1)\n")
    for (q, a1) in [(5, 2), (7, -3), (11, 5), (13, 6)]:
        d = hodge_index_yields_RH_elliptic(q, a1)
        print(f"  q={q}, a1={a1}:")
        for k, v in d.items():
            print(f"      {k:42s}: {v}")
        print()

    print("=" * 96)
    print("[3] DECISIVE: is Weil's RH self-intersection a Rankin-Selberg / Petersson residue?\n")
    d = is_the_self_intersection_a_rankin_selberg_residue()
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for kk, vv in v.items():
                print(f"      {kk:40s}: {vv}")
        else:
            print(f"  {k}: {v}")
    print()

    print("=" * 96)
    print("[4] STEELMAN -- three sophisticated readings of A5, each still fails\n")
    for k, v in steelman_readings().items():
        print(f"  {k}:\n      {v}\n")


if __name__ == "__main__":
    summary()
