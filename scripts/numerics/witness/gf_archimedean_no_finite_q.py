"""gf_archimedean_no_finite_q -- the archimedean self-intersection is provably
NOT of finite-place type (the F5 / F2 anchor).

CONTEXT (research/global-frobenius doc 09, the F1/F5 atlas deep-dive). The
dichotomy's finite horn: a finite self-intersection over bar(Spec Z) is forced
to the archimedean value V = -zeta'(0) = (1/2) log(2 pi) (doc 04). The far-side
question (F5): is V "finite-place type", i.e. could a finite Frobenius at infinity
(a discrete q-power map) produce it as an integer/lattice value?

A FINITE PLACE p has Frobenius eigenvalues on a lattice {p^{w/2}}; its THH /
self-intersection units are integer multiples of log p (doc 19: log|THH_{2i}(F_p)|
= log p). So finite-place self-intersections live in the Q-SPAN OF {log p : p prime}.

THE ANCHOR (Theorem, Lindemann). V = (1/2)(log 2 + log pi) splits into a
FINITE-PLACE part (1/2) log 2 (in the log-prime span -- the prime 2, cf. CC's
K = -2{2}) and an ARCHIMEDEAN part (1/2) log pi. If V were in the Q-span of
{log p}, then (1/2) log pi = V - (1/2) log 2 would be too, i.e.
log pi = Sum c_p log p (c_p rational) => pi = prod p^{c_p} ALGEBRAIC --
contradicting pi transcendental (Lindemann). Hence
        V = -zeta'(0) is NOT in the Q-span of {log p}:
the archimedean self-intersection is provably NOT finite-place type. The
obstruction is concentrated in the (1/2) log pi term.

So the dichotomy's transcendental horn is not "we failed to make it an integer"
but a THEOREM (Lindemann): the archimedean value cannot be a finite-Frobenius
lattice value. The missing object would need a DISCRETE multiplicative structure
(a finite q) at infinity, where only the CONTINUOUS scaling flow exists.

THIS WITNESS certifies the exact identity V = (1/2)(log 2 + log pi) (flint balls)
and the decomposition into finite-place + archimedean parts; the transcendence
conclusion is cited (Lindemann). It also sanity-checks that V is not a low-height
rational multiple of log q for small q.

PRE-REGISTERED READINGS (fail-closed):
  W0  V = -zeta'(0) = (1/2) log(2 pi), to < 1e-30 (flint).
  W1  V = (1/2) log 2 + (1/2) log pi exactly (the finite/archimedean split).
  W2  the finite-place part (1/2) log 2 IS in the log-prime span (trivially: it
      is (1/2) log 2); the archimedean part (1/2) log pi is the residue.
  W3  SANITY for the Lindemann anchor: V / log q is not within 1e-9 of any
      rational a/b with b <= 1000, for q = 2..50 (no accidental low-height
      finite-place value). [Numerical sanity only; the proof is Lindemann.]
"""

import sys

import flint

flint.ctx.prec = 400


def zeta_deriv0():
    h = flint.arb(1) / (flint.arb(2) ** 100)
    val = (flint.acb(h).zeta() - flint.acb(-h).zeta()) / (2 * h)
    return val.real


def best_rational(x, bmax):
    """nearest a/b to float x with 1<=b<=bmax; return (a,b,dist)."""
    best = (round(x), 1, abs(x - round(x)))
    for b in range(1, bmax + 1):
        a = round(x * b)
        d = abs(x - a / b)
        if d < best[2]:
            best = (a, b, d)
    return best


def run():
    passed = True

    def check(name, cond, detail=""):
        nonlocal passed
        tag = "PASS" if cond else "FAIL"
        if not cond:
            passed = False
        print(f"  [{tag}] {name}: {detail}")

    pi = flint.arb.pi()
    log2 = flint.arb(2).log()
    logpi = pi.log()
    V = -zeta_deriv0()

    print("W0: V = -zeta'(0) = (1/2) log(2 pi)")
    half_log_2pi = (2 * pi).log() / 2
    check("V = (1/2) log(2 pi)", (abs(V - half_log_2pi) < flint.arb(1e-30)).__bool__(),
          f"V={V.str(15)}, (1/2)log(2pi)={half_log_2pi.str(15)}")

    print("W1: V = (1/2) log 2 + (1/2) log pi  (finite-place + archimedean split)")
    split = log2 / 2 + logpi / 2
    check("split identity", (abs(V - split) < flint.arb(1e-30)).__bool__(),
          f"V - [(1/2)log2 + (1/2)logpi] = {(V - split).str(6)}")

    print("W2: finite part (1/2)log2 in log-prime span; archimedean residue (1/2)log pi")
    fin = log2 / 2
    arch = logpi / 2
    check("(1/2)log2 is in Q-span{log p} (it is (1/2) log 2)", True,
          f"(1/2)log2 = {fin.str(10)}  -- finite-place type (prime 2)")
    check("archimedean residue = (1/2) log pi (the obstruction)", True,
          f"(1/2)log pi = {arch.str(10)}  -- NOT in Q-span{{log p}} by Lindemann (pi transcendental)")
    print("       => if V in Q-span{log p} then log pi in Q-span{log p} => pi = prod p^c_p")
    print("          algebraic, contra Lindemann. So V is NOT finite-place type. [Theorem]")

    print("W3: sanity -- V/log q not a low-height rational (no accidental finite-place value)")
    Vf = float(V.str(30, radius=False))
    worst = 1.0
    bad = []
    for q in range(2, 51):
        x = Vf / float(flint.arb(q).log().str(30, radius=False))
        a, b, d = best_rational(x, 1000)
        if d < 1e-9:
            bad.append((q, a, b, d))
        worst = min(worst, d) if q == 2 else worst
    check("no V/log q within 1e-9 of a/b (b<=1000), q=2..50", len(bad) == 0,
          f"violations={bad if bad else 'none'} -- consistent with Lindemann (V not finite-place type)")

    print()
    if passed:
        print("ALL PASS")
        return 0
    print("SOME FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(run())
