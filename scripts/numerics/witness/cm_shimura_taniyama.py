"""cm_shimura_taniyama.py -- the CM / Shimura-Taniyama angle on the radius.

THE ANGLE (RF-cm-shimura-taniyama).  A CM abelian variety's Frobenius has |alpha| = q^{1/2}
by a THEOREM (Shimura-Taniyama), with purity FORCED by the CM TYPE -- a purely archimedean
datum (a set of archimedean embeddings / a Hodge structure).  Question: does this give the
radius WITHOUT RH, and does the archimedean analogue (an INFINITY-TYPE) force the zero-modulus
for zeta?

THE DECISIVE TEST (3 parts):
  (1) ANCHOR over F_q: for a CM elliptic curve, show |alpha|=sqrt q is FORCED by the CM type
      (Shimura-Taniyama), with NO appeal to the zero locations.  Compute alpha = pi exactly as
      an algebraic integer in K = Q(sqrt(-d)), and show |alpha|^2 = N(pi) = q FORCED by
      pi * pi-bar = q being the FACTORIZATION of q in O_K -- i.e. by the CM TYPE summing to all
      embeddings (Phi + Phi-bar = Hom(K,C)).
  (2) Does zeta's relevant carrier carry a CM/theta structure?  zeta = GL(1) -> the only CM AV
      is the trivial one / CM elliptic factors of the modular curve.  Test whether the
      weight-2 NS / Rankin-Selberg piece carries an infinity-type that would force purity.
  (3) Is the |alpha|^2 = q FORCED archimedean-only, or does it secretly use the q (a finite
      cardinality / a complex multiplication by an actual prime above p)?  -- the circularity probe.

THE SHARP CLAIM TO TEST (Shimura-Taniyama, made executable):
  For E/F_q with CM by O_K (K imag. quadratic), q = p^n, the Frobenius pi in O_K satisfies
      pi * pi-bar = q                                   (*)
  and this is the statement that the IDEAL (pi) and its conjugate (pi-bar) multiply to (q).
  |alpha|^2 = pi * pi-bar = q is then IMMEDIATE and EXACT -- the radius drops out of (*).
  The CONTENT of Shimura-Taniyama is WHICH primes above p divide (pi): the v-adic valuation
      ord_v(pi) / ord_v(q)  =  #(Phi  meeting v) / #(all embeddings meeting v)
  is read off the CM TYPE Phi (archimedean data).  The PURITY |alpha|=sqrt q is the *complex
  absolute value* statement, which is the v=infinity instance of the same valuation balance.

So the test: is (*) -- pi pi-bar = q -- FORCED by the CM type / Hodge structure, or does it
SMUGGLE the radius (assume |alpha|=sqrt q)?  We compute pi exactly for real CM curves and audit.
"""
from __future__ import annotations

import cmath
import math

import mpmath as mp
import numpy as np


# ----------------------------------------------------------------------------------------------------
# 1. ANCHOR: CM elliptic curves over F_q.  alpha = pi in O_K, pi*pi-bar = q EXACT (algebraic integers)
# ----------------------------------------------------------------------------------------------------

def cm_frobenius_exact(p, d):
    """For a prime p that SPLITS in K=Q(sqrt(-d)) (so an ordinary CM elliptic curve over F_p exists
    with CM by O_K), find the Frobenius pi = (a + b sqrt(-d))/(denom) with N(pi) = pi*pi-bar = p,
    i.e. a^2 + d b^2 = 4p (the prime is represented by the principal form), giving pi exactly.
    Return pi as a complex number AND the EXACT integer identity that forces |pi|^2 = p.

    KEY POINT: |alpha|^2 = pi*pi-bar = p is an EXACT integer factorization a^2+d b^2 = 4p (for
    d=3 mod 4 we use the ring Z[(1+sqrt-d)/2]); the radius sqrt p is read off this factorization,
    NOT off any 'zero is on the line' input.  This is Shimura-Taniyama / Deuring for CM curves."""
    # We want integers (a,b) with a^2 + d*b^2 = 4p  (norm form of the maximal order, x = (a+b sqrt-d)/2).
    # Then pi = (a + b sqrt(-d))/2, N(pi) = (a^2 + d b^2)/4 = p.  alpha = pi, |alpha|^2 = p.
    sols = []
    amax = int(2 * math.isqrt(p)) + 2
    for a in range(-amax, amax + 1):
        rem = 4 * p - a * a
        if rem < 0:
            continue
        if rem % d != 0:
            continue
        b2 = rem // d
        b = math.isqrt(b2)
        if b * b == b2 and b > 0:
            sols.append((a, b))
    out = []
    for (a, b) in sols:
        pi = complex(a, b * math.sqrt(d)) / 2.0
        pibar = pi.conjugate()
        norm_exact = (a * a + d * b * b)  # = 4p exactly
        out.append({
            "pi = (a+b sqrt(-d))/2": pi,
            "a,b": (a, b),
            "a^2 + d b^2 (=4p exact)": norm_exact,
            "4p": 4 * p,
            "exact identity a^2+d b^2 = 4p?": norm_exact == 4 * p,
            "N(pi)=pi*pi-bar (=p)": (pi * pibar).real,
            "|alpha|^2": abs(pi) ** 2,
            "p": p,
            "|alpha| = sqrt p?": abs(abs(pi) ** 2 - p) < 1e-9,
        })
    return out


def anchor_summary():
    """Run the anchor on several (p,d): the radius sqrt p drops out of an EXACT integer
    factorization a^2 + d b^2 = 4p, the norm of the Frobenius -- no zero-location input."""
    rows = []
    for d, p in [(3, 7), (3, 13), (3, 31), (1, 5), (1, 13), (1, 17), (2, 11), (7, 11), (7, 23)]:
        for r in cm_frobenius_exact(p, d):
            rows.append({"d": d, **r})
    return rows


# ----------------------------------------------------------------------------------------------------
# 2. THE CIRCULARITY PROBE: is pi*pi-bar = q FORCED by the CM TYPE (archimedean), or does it USE q?
# ----------------------------------------------------------------------------------------------------

def circularity_probe():
    """Shimura-Taniyama, decomposed.  The Frobenius pi in O_K satisfies:

      (A)  pi * pi-bar = q                    [the NORM identity; this gives |alpha|^2=q]
      (B)  prod_{v | p} v^{ord_v(pi)} = (pi),  with ord_v(pi)/ord_v(q) = |Phi cap H_v|/|H_v|  [ST formula]

    WHERE DOES |alpha|=sqrt q COME FROM?  Two candidate sources:

      SOURCE-A (the norm identity (A)):  pi*pi-bar = q is the statement that the principal ideal
        (pi) times its complex-conjugate (pi-bar) equals (q).  This is a FINITE/p-adic fact: (pi)
        is the product of the primes of K above p that 'point the Frobenius way' (the CM type Phi
        at the p-adic places), and (pi-bar) the complementary primes (Phi-bar), and together they
        exhaust all primes above p = (q).  pi*pi-bar = q USES that q is a RATIONAL prime power that
        FACTORS in O_K -- it uses the ACTUAL ARITHMETIC of p in K.  This is NOT archimedean-only:
        it is the v|p (FINITE-place) valuation balance.

      SOURCE-B (the archimedean CM type):  the COMPLEX absolute value |pi|^2 = pi*conj(pi) -- here
        conj is the ARCHIMEDEAN (complex) conjugation, the v=infinity place.  |alpha|=sqrt q would
        follow archimedean-only IF we knew |pi|^2_infinity = q WITHOUT the finite factorization.

    THE PROBE: is conj_infinity (complex conjugation at v=infinity) FORCED to agree with the
    Rosati/algebraic conjugation (pi -> pi-bar = the OTHER root, q/pi)?  In K imaginary quadratic
    they COINCIDE: the unique nontrivial automorphism of K IS complex conjugation, and it is
    simultaneously (i) the archimedean conjugation z->z-bar and (ii) the Galois/Rosati map
    pi -> q/pi.  THIS COINCIDENCE is exactly what makes |alpha|=sqrt q.  We test whether the
    coincidence is FORCED by the CM type or ASSUMED.
    """
    out = []
    # For K = Q(sqrt(-d)), the nontrivial automorphism sigma is complex conjugation.
    # Take pi with pi*sigma(pi) = q.  Is sigma = complex-conjugation FORCED?  YES: K has a UNIQUE
    # embedding pair {iota, iota-bar} into C, and sigma is the swap; the CM type Phi = {iota} picks
    # ONE, Phi-bar = {iota-bar} the other, Phi + Phi-bar = Hom(K,C).  The Rosati involution is
    # sigma = complex conjugation BECAUSE K is a CM field (totally imaginary quadratic over Q-real).
    for d, p in [(3, 7), (1, 13), (7, 11)]:
        for r in cm_frobenius_exact(p, d):
            a, b = r["a,b"]
            pi = r["pi = (a+b sqrt(-d))/2"]
            # algebraic conjugate (the OTHER root of min poly x^2 - a x + p):  q/pi
            alg_conj = p / pi
            cplx_conj = pi.conjugate()
            out.append({
                "d,p": (d, p), "pi": pi,
                "algebraic conj q/pi (Rosati)": alg_conj,
                "complex conj pi-bar (archimedean)": cplx_conj,
                "do they COINCIDE? (CM field fact)": abs(alg_conj - cplx_conj) < 1e-9,
                "|pi|^2 = pi * (complex conj) = q": (pi * cplx_conj).real,
                "FORCED by: K imag.quad => Rosati = cplx conj": True,
            })
    return out


# ----------------------------------------------------------------------------------------------------
# 3. THE ARCHIMEDEAN ANALOGUE: an INFINITY-TYPE for zeta?  Build a toy off-line CM-less Frobenius
# ----------------------------------------------------------------------------------------------------

def archimedean_infinity_type_test():
    """The CM TYPE Phi is a set of archimedean embeddings -- the INFINITY-TYPE / Hodge structure.
    For an abelian variety it FORCES purity via:  Phi + Phi-bar = all embeddings  =>  the Hodge
    structure is pure of weight 1  =>  |alpha|^2 = q.

    THE ARCHIMEDEAN ANALOGUE FOR ZETA: zeta is GL(1).  The 'motive' is Q(0); its Hodge structure
    is the TRIVIAL pure Hodge structure of weight 0, type (0,0).  There is NO CM abelian variety,
    NO Frobenius pi, NO field K with a swap.  The would-be 'infinity-type' is the Gamma_R factor
    (Hodge type at infinity), which is DH-SHARED.

    THE DECISIVE NEGATIVE TEST: a CM-TYPE forces purity ONLY through the relation pi*pi-bar = q,
    i.e. ONLY when there IS a pi (a Frobenius / Hecke eigenvalue) with a Rosati adjoint pi-bar = q/pi
    AND the archimedean conjugation = the Rosati adjoint.  The 'infinity-type' (the set Phi) tells
    you WHICH primes pi is divisible by (the v|p balance), but the |alpha|^2=q itself is pi*pi-bar=q
    = the NORM = the finite/global degree.  We show: an off-line 'pi' CANNOT be CM (no field with the
    right archimedean conjugation), so CM EXCLUDES off-line -- but only by ASSUMING pi lies in an
    imaginary quadratic field where Rosati = complex conjugation, which is itself |alpha|=sqrt q.

    Build a toy: take an off-line 'alpha' (|alpha| != sqrt q) and ask: can it be the Frobenius of a
    CM abelian variety?  ans: NO -- because a CM Frobenius pi satisfies pi * sigma(pi) = q with sigma
    the CM-field involution, and IF sigma = complex conjugation then |pi|^2 = q FORCED.  But the
    'IF sigma = complex conjugation' is the POSITIVITY of the Rosati form = RH for the AV.  We
    EXHIBIT the gap by building a fake 'CM datum' whose involution is NOT complex conjugation."""
    q = 9.0  # = 3^2
    s = math.sqrt(q)
    out = []
    # (a) genuine CM: pi in Z[i] with pi*pi-bar = q.  q=9: pi = 3 (= -3?), or pi = (a+bi), a^2+b^2=9.
    for (a, b) in [(3, 0), (0, 3)]:
        pi = complex(a, b)
        out.append({
            "case": f"genuine CM pi={a}+{b}i in Z[i]",
            "pi*pi-bar": (pi * pi.conjugate()).real,
            "|pi|": abs(pi),
            "on line |pi|=sqrt q?": abs(abs(pi) - s) < 1e-9,
            "Rosati(pi)=q/pi == cplx conj pi-bar?": abs(q / pi - pi.conjugate()) < 1e-9,
        })
    # (b) FAKE 'CM': pick an off-line pi and an algebraic involution sigma(pi)=q/pi.  Is sigma the
    # complex conjugation?  Only if |pi|^2=q.  Off-line => sigma != cplx conj => NOT a CM field embedding.
    for r in [1.5, 2.0]:
        pi = s * r * cmath.exp(0.5j)  # off the circle, |pi| = s*r != s
        rosati = q / pi               # the algebraic adjoint (q/pi)
        cconj = pi.conjugate()
        out.append({
            "case": f"fake off-line pi, |pi|=sqrt q * {r}",
            "pi*pi-bar (=|pi|^2, NOT q)": (pi * cconj).real,
            "|pi|": abs(pi),
            "on line |pi|=sqrt q?": abs(abs(pi) - s) < 1e-9,
            "Rosati q/pi == cplx conj? (CM <=> this)": abs(rosati - cconj) < 1e-9,
            "diagnosis": "Rosati != complex conj  <=>  off-line  <=>  NOT a CM-field embedding",
        })
    return {"q": q, "sqrt q": s, "cases": out}


# ----------------------------------------------------------------------------------------------------
# 4. WHERE RH ENTERS: the audit
# ----------------------------------------------------------------------------------------------------

def where_rh_enters():
    return {
        "anchor F_q": (
            "|alpha|^2 = q is FORCED, and it is forced by pi*pi-bar = q = the EXACT integer norm "
            "identity a^2+d b^2 = 4p.  This uses NO zero-location: it is the factorization of the "
            "rational prime power q in O_K.  PASS -- the radius drops out of the norm, an algebraic "
            "integer identity.  BUT (see below) the *purity* |alpha|=sqrt q at the ARCHIMEDEAN place "
            "is the v=infinity instance, and it holds because in an imaginary-quadratic CM field the "
            "Rosati involution pi->q/pi COINCIDES with complex conjugation pi->pi-bar -- a structural "
            "fact of CM FIELDS, FREE (not RH)."),
        "what forces it (the real content)": (
            "Two facts, BOTH free of RH for the AV: (i) pi is an algebraic integer with pi*pi-bar=q "
            "(the characteristic poly of Frobenius has constant term q = the degree); (ii) K is a CM "
            "field so the Rosati/Galois involution IS complex conjugation.  Together: |alpha|^2 = "
            "pi*(cplx conj pi) = pi*(Rosati pi) = q.  The Shimura-Taniyama CONTENT (which primes | pi) "
            "is the FINER datum (the count of where pi sits among primes above p); the |alpha|=sqrt q "
            "is the v=infinity coarse shadow."),
        "where RH would enter for a GENERAL AV (not CM)": (
            "For a NON-CM abelian variety the Rosati involution is NOT complex conjugation on a single "
            "eigenvalue; |alpha|=sqrt q then requires the Rosati POSITIVITY (Weil), which is the "
            "general Riemann hypothesis for the AV.  CM is SPECIAL: the endomorphism field is big enough "
            "(an imaginary quadratic / CM field) that the involution is FORCED = complex conjugation by "
            "the FIELD STRUCTURE, so positivity is automatic.  THE CM SHORTCUT IS: a big enough "
            "(archimedean-typed) endomorphism algebra makes Rosati = complex-conjugation, hence "
            "positive, hence |alpha|=sqrt q -- WITHOUT a separate positivity input."),
        "the archimedean analogue for zeta": (
            "ZETA IS GL(1): the motive is Q(0), Hodge type (0,0), weight 0.  There is NO Frobenius pi, "
            "NO endomorphism field K, NO Rosati involution to coincide with complex conjugation.  The "
            "'infinity-type' for zeta is the Gamma_R factor = the (0,0)-Hodge type at infinity, which "
            "is DH-SHARED (Davenport-Heilbronn has the same Gamma factor).  THERE IS NO CM AV WHOSE "
            "ARCHIMEDEAN INFINITY-TYPE COULD FORCE PURITY, because there is no pi for it to act on."),
        "the weight-2 NS / Rankin-Selberg piece": (
            "The weight-2 self-product NS lattice (M4A) has eigenvalues alpha_i alpha_j; a CM structure "
            "there would need a CM abelian variety with those Frobenius eigenvalues, i.e. it would need "
            "the modular form f (giving alpha_i) to be CM.  But a GENERIC cusp form / the curve giving "
            "zeta's Rankin-Selberg piece is NOT CM (CM forms are a measure-zero special family).  For a "
            "CM modular form |alpha_i|=sqrt p IS forced (Hecke character of an imag.quad field, a "
            "theorem) -- but that is the CM SUBfamily, NOT zeta and NOT the generic Rankin-Selberg piece. "
            "zeta's zeros are NOT the L-function of a CM object."),
        "VERDICT on circularity": (
            "The CM angle FORCES the radius GENUINELY for CM objects (Shimura-Taniyama is a real theorem, "
            "no RH) -- but the forcing mechanism is 'the endomorphism field is a CM field, so Rosati = "
            "complex conjugation, so positivity is automatic'.  This is a SPECIAL feature of having a "
            "large archimedean-typed endomorphism algebra.  ZETA HAS NO SUCH ALGEBRA (GL(1), no CM AV); "
            "the generic Rankin-Selberg / weight-2 piece is non-CM.  So the CM shortcut DOES force the "
            "radius without RH, but ONLY for objects zeta is not.  For zeta the analogue is EMPTY: there "
            "is no infinity-type acting on a Frobenius, because there is no Frobenius eigenvalue carried "
            "by a CM endomorphism field.  NOT circular (the CM forcing is real), but INAPPLICABLE to "
            "zeta -- the very feature that makes CM work (a CM endomorphism field) is exactly what zeta "
            "lacks."),
    }


def falsify_dh():
    return {
        "DH a CM structure?": (
            "NO.  Davenport-Heilbronn has NO Euler product, hence NO Frobenius/Satake parameters, hence "
            "NO algebraic Frobenius pi, hence NO endomorphism field, hence NO CM type.  A CM structure "
            "REQUIRES a Frobenius eigenvalue in an imaginary-quadratic/CM field; DH supplies none.  The "
            "CM angle is UNPOSABLE for DH -- same as every Euler-borne carrier."),
        "does this make the angle DH-discriminating?": (
            "The CM MECHANISM is Euler-borne (needs Satake/Frobenius), so it is DH-failing BY DESIGN -- "
            "but that does NOT help zeta, because zeta itself (GL(1)) ALSO has no CM AV.  The angle "
            "discriminates DH from a CM ELLIPTIC CURVE, not DH from zeta.  zeta is on the DH side of "
            "THIS particular discriminator (neither has a CM AV with a Frobenius pi)."),
    }


def summary():
    mp.mp.dps = 30
    print(__doc__)
    print("=" * 100)
    print("[1] ANCHOR: CM elliptic curves over F_p -- |alpha|^2 = p from EXACT norm a^2+d b^2 = 4p\n")
    for r in anchor_summary():
        print(f"    d={r['d']:2d} p={r['p']:3d}  pi={r['pi = (a+b sqrt(-d))/2']:.4f}  "
              f"a^2+d b^2={r['a^2 + d b^2 (=4p exact)']:4d} (=4p={r['4p']})  "
              f"|alpha|^2={r['|alpha|^2']:.4f}  |alpha|=sqrt p? {r['|alpha| = sqrt p?']}")
    print()
    print("=" * 100)
    print("[2] CIRCULARITY PROBE: Rosati (q/pi) == complex conj (pi-bar)?  -- the CM-field coincidence\n")
    for r in circularity_probe():
        print(f"    d,p={r['d,p']}  pi={r['pi']:.4f}  q/pi={r['algebraic conj q/pi (Rosati)']:.4f}  "
              f"pi-bar={r['complex conj pi-bar (archimedean)']:.4f}  "
              f"COINCIDE? {r['do they COINCIDE? (CM field fact)']}  "
              f"|pi|^2=q: {r['|pi|^2 = pi * (complex conj) = q']:.4f}")
    print()
    print("=" * 100)
    print("[3] ARCHIMEDEAN INFINITY-TYPE TEST: genuine CM vs fake off-line 'CM'\n")
    t = archimedean_infinity_type_test()
    print(f"    q={t['q']}, sqrt q={t['sqrt q']:.4f}")
    for c in t["cases"]:
        print(f"    {c['case']:38s}  |pi|={c['|pi|']:.4f}  on-line? {c['on line |pi|=sqrt q?']}  "
              f"Rosati==cplx-conj? {c.get('Rosati(pi)=q/pi == cplx conj pi-bar?', c.get('Rosati q/pi == cplx conj? (CM <=> this)'))}")
    print()
    print("=" * 100)
    print("[4] WHERE RH ENTERS (the audit)\n")
    for k, v in where_rh_enters().items():
        print(f"    {k}:\n        {v}\n")
    print("=" * 100)
    print("[5] DH falsify\n")
    for k, v in falsify_dh().items():
        print(f"    {k}:\n        {v}\n")


if __name__ == "__main__":
    summary()
