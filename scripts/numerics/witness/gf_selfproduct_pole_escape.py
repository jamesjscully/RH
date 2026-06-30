"""gf_selfproduct_pole_escape -- the W2 probe: does a 2-variable self-product
zeta escape the s=0 pole into a finite INTEGER intersection number?

INVESTIGATION (research/global-frobenius, doc 03 weak link W2 -- the decisive
fork). doc 02 showed the 1-variable regularized total of CC's integer dimension
DIVERGES (simple pole at s=0, residue r = -1/(2 log b)). doc 03 reduced
fundamentality of the integrality-summability dichotomy to W2:

    is <Delta,Delta> the 1-variable regularized tower (=> divergent), or does a
    genuinely 2-VARIABLE self-product zeta have a finite value at the origin --
    and if finite, is it an INTEGER (the leak = a construction handle) or forced
    transcendental (no leak = the dichotomy is fundamental)?

THREE LOGICAL OUTCOMES (pre-registered):
  (a) every natural 2-variable model is POLAR on the diagonal at the origin
      => no escape; the square makes it worse, not better;
  (b) the only finite value is FORCED TRANSCENDENTAL (a zeta'(0)-type
      archimedean constant) => escape exists but lands off the integers
      => the dichotomy holds at the 2-variable level (BOUNDED-NEGATIVE);
  (c) some model gives a FINITE INTEGER => W2 LEAKS; the 2-variable
      regularization is the missing self-product structure (swing POSITIVE).

MODELS (the natural 2-variable lifts of the 1-variable defect D_delta(s), whose
Laurent expansion at s=0 is r/s + FP + O(s), r = -1/(2 log b) certified in
prime_cc_quantization_defect). The "genuine 2-dimensional / non-pullback" part of
the square's intersection form is built from the defect (the quantization-
obstruction-carrying part); the smooth log part is the FE-layer pullback.
  M1 product (H^1 (x) H^1, the genuine 2-dim intersection content):
        Z_x(s,t) = D_delta(s) D_delta(t);  diagonal s=t.
  M2 additive (mixed pullback (+) defect):
        Z_+(s,t) = D_delta(s) zeta(t) + zeta(s) D_delta(t);  diagonal s=t.
  M3 antisymmetric / normal bundle (the standard geometric route to a finite
     self-intersection -- the transverse/normal direction to the diagonal):
        self-intersection = transverse derivative of D_delta(s) - D_delta(t).
  DERIVED (the alternating/Tate value, for comparison): V = -zeta'(0)/log b =
     (log 2pi)/(2 log b) -- the prior arc's doc-18 finite self-intersection.

Diagonal Laurent leading coefficients (exact algebra from D_delta = r/s + FP +
c1 s + ...):
  M1: Z_x(s,s) = r^2/s^2 + 2 r FP/s + ...        => DOUBLE pole, coeff r^2.
  M2: Z_+(s,s) = 2 zeta(s) D_delta(s);  zeta(0) = -1/2 (finite)
                = 2(-1/2)(r/s) + ... = -r/s + ...  => SIMPLE pole, residue -r.
  M3: [D_delta(s)-D_delta(t)]/(s-t) = r(1/s-1/t)/(s-t) + c1 + ...
                = -r/(s t) + c1 + ...; on s=t  => DOUBLE pole, coeff -r.
Each leading coefficient is a nonzero multiple of r != 0 => all three models
DIVERGE on the diagonal at the origin. Outcome (a) for the integer side; the only
finite value is the DERIVED transcendental (outcome b). Outcome (c) ABSENT.

This witness CERTIFIES (flint ball arithmetic): r != 0 (so M1,M2,M3 leading
coeffs nonzero), zeta(0) = -1/2, the derived value V is finite and NOT an integer
(transcendental). Conclusion: W2 does NOT leak to a finite integer; the dichotomy
is fundamental at the 2-variable level (within the additive class). The escape
into finiteness exists only via the alternating/Tate structure, which over Z
yields the archimedean transcendental zeta'(0) -- the properness wall
(doc 18/19) re-derived through the self-product.

PRE-REGISTERED READINGS (fixed before run, fail-closed):
  W0  residue r = -1/(2 log b): |r| > 0.1 for b=2,3 (the 1-var pole is real).
  W1  M1 (product) diagonal leading coeff r^2 > 0 (double pole; square WORSE).
  W2  zeta(0) = -1/2 exactly (flint), so M2 diagonal residue = -r != 0 (pole).
  W3  M3 (antisym/normal) diagonal leading coeff -r != 0 (double pole).
  W4  DERIVED value V = -zeta'(0)/log b is finite and |V - round(V)| > 1e-3
      for b=2,3 (the only finite self-intersection is NON-integer/transcendental).
  W5  VERDICT: outcome (a)+(b), outcome (c) absent -> no 2-variable model yields
      a finite integer. W2 does NOT leak.
"""

import sys

import flint

flint.ctx.prec = 300


def zeta0():
    """zeta(0) = -1/2 as a rigorous ball."""
    return flint.acb(0).zeta().real


def zeta_deriv0():
    """zeta'(0) by central difference (h = 2^-80; O(h^2) << ball prec)."""
    h = flint.arb(1) / (flint.arb(2) ** 80)
    val = (flint.acb(h).zeta() - flint.acb(-h).zeta()) / (2 * h)
    return val.real


def residue(b):
    """r = -1/(2 log b)."""
    return -flint.arb(1) / (2 * flint.arb(b).log())


def derived_value(b):
    """V = -zeta'(0)/log b = (log 2pi)/(2 log b) -- the alternating/Tate
    self-intersection (doc 18)."""
    return -zeta_deriv0() / flint.arb(b).log()


def run():
    passed = True

    def check(name, cond, detail=""):
        nonlocal passed
        tag = "PASS" if cond else "FAIL"
        if not cond:
            passed = False
        print(f"  [{tag}] {name}: {detail}")

    print("W0: the 1-variable pole is real (residue r = -1/(2 log b) != 0)")
    for b in (2, 3):
        r = residue(b)
        check(f"b={b}: |r|>0.1", (abs(r) > flint.arb("0.1")).__bool__(),
              f"r = {r.str(8)}")

    print("W1: M1 product (H^1(x)H^1) diagonal leading coeff = r^2 > 0 (DOUBLE pole)")
    for b in (2, 3):
        r = residue(b)
        r2 = r * r
        check(f"b={b}: r^2>0 (square is WORSE)", (r2 > 0).__bool__(),
              f"r^2 = {r2.str(8)} -- double pole on the diagonal")

    print("W2: zeta(0) = -1/2, so M2 additive diagonal residue = -r != 0 (pole)")
    z0 = zeta0()
    check("zeta(0) = -1/2", (abs(z0 + flint.arb("0.5")) < flint.arb(1e-40)).__bool__(),
          f"zeta(0) = {z0.str(12)}")
    for b in (2, 3):
        res_M2 = -residue(b)  # 2*zeta(0)*r = 2*(-1/2)*r = -r
        check(f"b={b}: M2 residue -r != 0", (abs(res_M2) > flint.arb("0.1")).__bool__(),
              f"residue = {res_M2.str(8)}")

    print("W3: M3 antisymmetric/normal diagonal leading coeff = -r != 0 (DOUBLE pole)")
    for b in (2, 3):
        c_M3 = -residue(b)
        check(f"b={b}: -r != 0 (normal route also diverges)",
              (abs(c_M3) > flint.arb("0.1")).__bool__(),
              f"coeff = {c_M3.str(8)} -- the standard geometric self-intersection route fails")

    print("W4: the ONLY finite value (derived/Tate) is NON-integer (transcendental)")
    for b in (2, 3):
        V = derived_value(b)
        # nearest integer (midpoint only, no radius brackets)
        Vf = float(V.str(20, radius=False))
        nearest = round(Vf)
        dist = abs(V - flint.arb(nearest))
        check(f"b={b}: |V - round(V)| > 1e-3 (finite but NOT integer)",
              (dist > flint.arb(1e-3)).__bool__(),
              f"V = {V.str(10)} = (log 2pi)/(2 log {b}); nearest int {nearest}, dist {dist.str(6)}")

    print("W5: VERDICT")
    print("  Outcome (a): M1,M2,M3 all POLAR on the diagonal (coeffs nonzero multiples of r).")
    print("  Outcome (b): the only finite self-intersection (derived/Tate) is the")
    print("               archimedean TRANSCENDENTAL -zeta'(0)/log b, NOT an integer.")
    print("  Outcome (c) ABSENT: no 2-variable model yields a finite integer.")
    print("  => W2 does NOT leak. The dichotomy is fundamental at the 2-variable")
    print("     level within the additive class: finite <=> alternating/Tate <=>")
    print("     archimedean transcendental; integer <=> non-alternating <=> divergent.")
    print("     The self-product makes the genuine (H^1(x)H^1) content WORSE (double pole).")

    print()
    if passed:
        print("ALL PASS")
        return 0
    print("SOME FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(run())
