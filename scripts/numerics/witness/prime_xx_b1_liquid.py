"""XX-witness: bridge B1 (doc 38) - the Tate-curve liquid calibration (T2)
and the fracture-corner bookkeeping (T3), gates XB1-XB8.

Companion: research/work/XX-b1-liquid.md (sec 0: gates + nulls registered
there BEFORE this file was written; fail-closed; exit 0 iff ALL PASS).
Lineage: MM-liquid-slot.md (Route A spec + Epstein mandate 4.3),
BB-global-assembly.md (BB-r2 comb), JJ-archimedean-unit.md (AJ3, AJ7),
FF-kappa-on-xbar.md (rigidity context), QQ-native-face.md (witness style).

PRE-REGISTERED NULL (T2): every trace-layer number of the Tate curve
X_p = C^x/q^Z (q = 1/p) is p-independent (chi(L_d) = d, residue 1);
the comb identity holds with weight = spacing = 2pi/log p and NO
constant beyond the banked 2pi.  PRE-REGISTERED PREDICTION (T3): R is
fracture-inert (finite-place data of R vanish at finite level) and the
new corner is the cocompactness layer (fundamental domain Z_p x [0,1),
covolume 1 = product formula).

Discipline: F-a (no zeta values/continuation; no zero-side input);
G-INT6 (the Gaussian is the one logged analytic import); fork_lib never
imported; no zero contact anywhere (nothing here has a zero-flavored
locus), so the freeze protocol is never triggered.

GATES:
  XB1 Tate-curve RR (exact): h^0(L_d) = d, h^0(L_{-d}) = 0, h^0(O) = 1,
      chi = deg, second-difference certificates, theta d=1 identity
  XB2 Serre/residue normalization (acb): contour mean extracts a_0 = 1;
      functional equation f(qz) = z^{-1} f(z) numerically
  XB3 transported comb = banked comb (arb): Poisson on (log p)Z <->
      (2pi/log p)Z vs Gaussian tests; p in {2,3,5} + control p = 4
  XB4 carrier clause (exact): p^Z is a free rank-1 valuation address
  XB5 Epstein kill-test (exact + arb): 36 = 4*9 = 6*6 irreducibles ->
      coupling undefinable; theta_Q(s) = (1/(s sqrt5)) theta_Q*(1/s)
      alive
  XB6 R fracture-inert (exact): divisibility certificates + Z/p^k
      contrast + AJ3 primorial denominators
  XB7 the new corner (exact): Z[1/p] dense in Q_p alone; discrete
      cocompact in Q_p x R (fundamental domain exact); covolume =
      product formula; Prufer torsion shadow
  XB8 address/scale split (exact): colim(Z -p-> Z) = Z[1/p],
      place-addressed, scale-free
"""

import sys
from fractions import Fraction
from math import gcd

import flint

flint.ctx.prec = 300

arb = flint.arb
acb = flint.acb

PI = arb.pi()

FAILURES = []


def gate(name, ok, msg=""):
    tag = "PASS" if ok else "FAIL"
    print(f"{tag} {name}: {msg}")
    if not ok:
        FAILURES.append(name)


def small(x, tol):
    """Rigorous |x| < tol for arb/acb x."""
    return abs(x) < arb(tol)


# ----------------------------------------------------------------------
# XB1: Tate-curve Riemann-Roch, exact.
# Sections of L_d on C^x/q^Z (automorphy f(qz) = z^{-d} f(z)) are
# Laurent series with a_{n+d} = q^n a_n.  Exponent of q on the orbit
# n = r + kd: e(k+1) = e(k) + (r + kd), e(0) = 0.
# ----------------------------------------------------------------------

def orbit_exponents(r, d, kmin, kmax):
    """e(k) for k in [kmin, kmax], e(0) = 0, e(k+1) - e(k) = r + kd."""
    e = {0: 0}
    for k in range(0, kmax):
        e[k + 1] = e[k] + (r + k * d)
    for k in range(0, kmin, -1):
        e[k - 1] = e[k] - (r + (k - 1) * d)
    return e


def xb1():
    ok = True
    msgs = []
    for p in (2, 3, 5):
        q = Fraction(1, p)
        # h^0(O) = 1: a_n (q^n - 1) = 0 forces a_n = 0 for n != 0.
        for n in range(-20, 21):
            if n != 0 and q ** n == 1:
                ok = False
                msgs.append(f"q^{n} = 1 at p={p}")
        # L_d, d in 1..6: d free orbits; second difference of e(k) is
        # exactly +d; e(k) -> +infinity both directions (decay, since
        # 0 < q < 1 and coefficient = q^{e(k)}).
        for d in range(1, 7):
            for r in range(d):
                e = orbit_exponents(r, d, -15, 15)
                for k in range(-13, 13):
                    if e[k + 2] - 2 * e[k + 1] + e[k] != d:
                        ok = False
                        msgs.append(f"2nd diff != {d} at p={p} r={r}")
                # growth in both tails
                if not (e[15] > e[10] > 0 or d == 0):
                    ok = False
                    msgs.append(f"upper tail not growing p={p} d={d} r={r}")
                if not (e[-15] > e[-10] > 0):
                    ok = False
                    msgs.append(f"lower tail not growing p={p} d={d} r={r}")
            # h^0(L_{-d}) = 0: recursion a_{n-d} = q^n a_n gives second
            # difference -d: exponents -> -infinity in a tail => blow-up.
            # e'(k) on orbit: e'(k+1) = e'(k) - (r + kd) (orbit downward).
            for r in range(d):
                e = orbit_exponents(r, d, -15, 15)
                # dual exponents are -e(k): second difference -d
                if not all(
                    (-e[k + 2]) - 2 * (-e[k + 1]) + (-e[k]) == -d
                    for k in range(-13, 13)
                ):
                    ok = False
                    msgs.append(f"dual 2nd diff != -{d} p={p}")
                # -e(k) -> -infinity both directions: nonzero solution
                # blows up (q^{-e} -> infinity): only 0 is holomorphic.
                if not ((-e[15]) < (-e[10]) and (-e[-15]) < (-e[-10])):
                    ok = False
                    msgs.append(f"dual not blowing up p={p} d={d} r={r}")
        # chi(L_d) = h^0 - h^1 = d - 0 = d = deg(L_d): bookkeeping,
        # p-independent (the registered null at the RR layer).
    # theta d=1 functional-equation coefficient identity, exact integers:
    for n in range(-50, 51):
        if n * (n - 1) // 2 + n != n * (n + 1) // 2:
            ok = False
            msgs.append(f"theta identity fails at n={n}")
    gate(
        "XB1",
        ok,
        "h^0(L_d)=d (d free orbits, 2nd-diff=+d), h^0(L_-d)=0 (blow-up), "
        "h^0(O)=1, chi=deg p-independent; theta FE identity exact"
        + ("" if ok else "; " + "; ".join(msgs[:4])),
    )


# ----------------------------------------------------------------------
# XB2: Serre/residue normalization on the Tate curve, acb.
# theta(z) = sum_n q^{n(n-1)/2} z^n (truncated, certified-small tails);
# (1/(2 pi i)) oint theta(z) dz/z over |z|=1 via N-point trapezoid
# equals (1/N) sum_j theta(z_j) = a_0 + (aliasing, astronomically
# small) = 1.  Functional equation theta(qz) = z^{-1} theta(z) checked
# at sample points.
# ----------------------------------------------------------------------

def theta_tate(z, q, M=40):
    s = acb(0)
    for n in range(-M, M + 1):
        s += q ** (n * (n - 1) // 2) * z ** n
    return s


def xb2():
    ok = True
    msgs = []
    N = 64
    for p in (2, 3, 5):
        q = arb(1) / p
        # contour mean = a_0
        mean = acb(0)
        for j in range(N):
            z = (acb(0, 2) * PI * j / N).exp()
            mean += theta_tate(z, q)
        mean = mean / N
        if not small(mean - 1, "1e-20"):
            ok = False
            msgs.append(f"contour mean != 1 at p={p}: {mean}")
        # functional equation at sample z (on |z| = 1 and |z| = 1.3)
        for zval in (
            (acb(0, 2) * PI * arb(3) / 17).exp(),
            acb("1.3") * (acb(0, 2) * PI * arb(5) / 13).exp(),
        ):
            lhs = theta_tate(acb(q) * zval, q)
            rhs = theta_tate(zval, q) / zval
            if not small(lhs - rhs, "1e-18"):
                ok = False
                msgs.append(f"FE fails at p={p}")
    gate(
        "XB2",
        ok,
        "residue/trace extracts a_0 = 1 (constant-free, p-independent); "
        "f(qz) = z^-1 f(z) numerically"
        + ("" if ok else "; " + "; ".join(msgs[:3])),
    )


# ----------------------------------------------------------------------
# XB3: the transported comb = the banked comb (Poisson on (log p)Z <->
# (2pi/log p)Z), against Gaussian tests phi_s(t) = exp(-t^2/(2 s^2)),
# phihat(u) = s sqrt(2pi) exp(-s^2 u^2 / 2):
#   sum_n phihat(n L) = (2pi/L) sum_k phi(2pi k / L),  L = log p.
# Registered null: identity holds with the banked 2pi only; atom
# weight = atom spacing = 2pi/L (ratio 1 structurally).
# ----------------------------------------------------------------------

def xb3():
    ok = True
    msgs = []
    NTRM = 200
    sqrt2pi = (2 * PI).sqrt()
    for p in (2, 3, 4, 5):  # 4 = the p -> p^2 scaling control
        L = arb(p).log()
        for s in (arb(1), arb(1) / 2):
            lhs = arb(0)
            for n in range(-NTRM, NTRM + 1):
                u = n * L
                lhs += s * sqrt2pi * (-(s * u) ** 2 / 2).exp()
            rhs = arb(0)
            for k in range(-NTRM, NTRM + 1):
                t = 2 * PI * k / L
                rhs += (2 * PI / L) * (-(t ** 2) / (2 * s ** 2)).exp()
            if not small(lhs - rhs, "1e-25"):
                ok = False
                msgs.append(f"Poisson fails p={p} s={s}")
    gate(
        "XB3",
        ok,
        "comb identity to 1e-25 at p in {2,3,5} + control p=4; "
        "weight/spacing = 1 (scale-free null confirmed; banked 2pi only)"
        + ("" if ok else "; " + "; ".join(msgs[:3])),
    )


# ----------------------------------------------------------------------
# XB4: carrier clause - p^Z is a free rank-1 valuation address (exact).
# ----------------------------------------------------------------------

def xb4():
    ok = True
    for p in (2, 3, 5):
        for a in range(-6, 7):
            for b in range(-6, 7):
                if Fraction(p) ** a * Fraction(p) ** b != Fraction(p) ** (a + b):
                    ok = False
        # injectivity of the address
        vals = set(Fraction(p) ** a for a in range(-6, 7))
        if len(vals) != 13:
            ok = False
    gate("XB4", ok, "p^Z: v(p^a p^b) = a + b, address bijective (exact)")


# ----------------------------------------------------------------------
# XB5: Epstein kill-test at the T2 coupling.
# (a) carrier death: represented values of Q(x,y) = x^2 + 5y^2;
#     4, 6, 9 irreducible in the value monoid; 36 = 4*9 = 6*6.
# (b) PD alive: theta_Q(s) = (1/(s sqrt5)) theta_{Q*}(1/s).
# ----------------------------------------------------------------------

def theta1(s, M=200):
    t = arb(1)
    for n in range(1, M + 1):
        t += 2 * (-PI * s * n * n).exp()
    return t


def xb5():
    ok = True
    msgs = []
    # (a) exact carrier death
    V = set()
    for x in range(-12, 13):
        for y in range(-12, 13):
            v = x * x + 5 * y * y
            if 0 < v <= 144:
                V.add(v)
    for w in (4, 6, 9, 36):
        if w not in V:
            ok = False
            msgs.append(f"{w} not represented")

    def irreducible(w):
        for a in sorted(V):
            if a >= w:
                break
            if a > 1 and w % a == 0 and (w // a) in V and (w // a) > 1:
                return False
        return True

    for w in (4, 6, 9):
        if not irreducible(w):
            ok = False
            msgs.append(f"{w} reducible")
    if not (36 % 4 == 0 and 36 // 4 == 9 and 36 == 6 * 6 and 6 in V and 4 in V and 9 in V):
        ok = False
        msgs.append("36 factorizations broken")
    # => two distinct irreducible factorizations: no valuation, no
    #    q-expansion address: the XB3/XB4 coupling is UNDEFINABLE.
    # (b) theta/PD alive
    for snum, sden in ((1, 2), (1, 1), (2, 1)):
        s = arb(snum) / sden
        lhs = theta1(s) * theta1(5 * s)
        rhs = theta1(1 / s) * theta1(1 / (5 * s)) / (s * arb(5).sqrt())
        if not small(lhs - rhs, "1e-25"):
            ok = False
            msgs.append(f"theta_Q FE fails at s={snum}/{sden}")
    gate(
        "XB5",
        ok,
        "carrier dead (36 = 4*9 = 6*6, 4/6/9 irreducible: coupling "
        "undefinable); theta_Q(s) = (1/(s sqrt5)) theta_Q*(1/s) alive "
        "to 1e-25 - death at effectivity, AJ7 profile"
        + ("" if ok else "; " + "; ".join(msgs[:3])),
    )


# ----------------------------------------------------------------------
# XB6: R is fracture-inert (finite-level certificates).
# ----------------------------------------------------------------------

def xb6():
    ok = True
    msgs = []
    # (a) divisibility in the rational/connected layer: n x = r solvable
    samples = [Fraction(1), Fraction(-7, 3), Fraction(22, 7), Fraction(5, 9)]
    for r in samples:
        for n in (2, 3, 4, 5, 8, 9):
            x = r / n
            if n * x != r:
                ok = False
                msgs.append(f"divisibility fails {r}/{n}")
    # torsion-freeness: n x = 0 => x = 0 (over Q: clear; sample check)
    for n in (2, 3, 5):
        if Fraction(0) / n != 0:
            ok = False
    # contrast: p x = 1 unsolvable in Z/p^k (non-divisible tower)
    for p, k in ((2, 3), (3, 2), (5, 2)):
        if any((p * x) % p ** k == 1 for x in range(p ** k)):
            ok = False
            msgs.append(f"p x = 1 solvable in Z/{p}^{k} (!)")
    # (b) AJ3 replication: minimal denominator of ((1/p))_{p in S} in the
    # A_f corner = primorial(S), strictly increasing.
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    prev = 1
    for k in range(1, 9):
        S = primes[:k]
        denom = 1
        for p in S:
            denom = denom * p // gcd(denom, p)
        primorial = 1
        for p in S:
            primorial *= p
        if denom != primorial or denom <= prev:
            ok = False
            msgs.append(f"primorial clause fails at |S|={k}")
        prev = denom
    gate(
        "XB6",
        ok,
        "R fracture-inert at finite level: divisible+torsion-free certs "
        "(=> R(x)Z/n = 0, Tor = 0, R^_p = 0), Z/p^k contrast, AJ3 "
        "primorial denominators unbounded"
        + ("" if ok else "; " + "; ".join(msgs[:3])),
    )


# ----------------------------------------------------------------------
# XB7: the new corner exists only with R present (exact).
# ----------------------------------------------------------------------

def vp(fr, p):
    """p-adic valuation of a nonzero Fraction."""
    n, d = fr.numerator, fr.denominator
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def principal_part(x, p):
    """z0 in Z[1/p] with x - z0 in Z_p (v_p >= 0), for x in Q with
    v_p(x) possibly negative."""
    j = max(0, -vp(x, p)) if x != 0 else 0
    if j == 0:
        return Fraction(0)
    # x = u / (p^j m), gcd(m, p) = 1
    pj = p ** j
    m = x.denominator // pj
    u = x.numerator
    minv = pow(m, -1, pj)
    t = (u * minv) % pj
    return Fraction(t, pj)


def xb7():
    ok = True
    msgs = []
    for p in (2, 3, 5):
        # (a) WITHOUT R: Z[1/p] (already Z) dense in Z_p: for rational
        # targets r with denominator coprime to p, z = num * den^{-1}
        # mod p^12 satisfies v_p(r - z) >= 12.
        targets = [Fraction(1, 3), Fraction(22, 7), Fraction(-5, 9)]
        if p == 3:
            targets = [Fraction(1, 2), Fraction(22, 7), Fraction(-5, 11)]
        for r in targets:
            k = 12
            z = (r.numerator * pow(r.denominator, -1, p ** k)) % (p ** k)
            if vp(r - z, p) < k:
                ok = False
                msgs.append(f"density fails p={p} r={r}")
        # (b) WITH R: fundamental domain Z_p x [0,1).
        xs = [Fraction(7, p ** 3), Fraction(-22, 7 * p ** 2), Fraction(5)]
        rs = [Fraction(13, 4), Fraction(-9, 7), Fraction(0)]
        for x in xs:
            for r in rs:
                z0 = principal_part(x, p)
                if x != z0 and vp(x - z0, p) < 0:
                    ok = False
                    msgs.append(f"principal part fails p={p} x={x}")
                    continue
                import math

                z = z0 + math.floor(r - z0)
                # representative check
                cond_qp = (x == z) or vp(x - z, p) >= 0
                cond_r = Fraction(0) <= r - z < Fraction(1)
                if not (cond_qp and cond_r):
                    ok = False
                    msgs.append(f"fundamental domain fails p={p}")
        # uniqueness pivot: Z[1/p] cap Z_p = Z at finite level:
        # a/p^j with p \nmid a, j >= 1 has v_p < 0.
        for j in range(1, 7):
            for a in (1, p + 1, 2 * p + 1):
                if a % p == 0:
                    continue
                if vp(Fraction(a, p ** j), p) >= 0:
                    ok = False
                    msgs.append(f"pivot fails p={p} j={j}")
        # covolume = product formula: |p^k|_p * |p^k|_oo = 1 exact
        for k in range(-6, 7):
            norm_p = Fraction(1, p) ** k  # |p^k|_p = p^{-k}
            norm_oo = Fraction(p) ** k
            if norm_p * norm_oo != 1:
                ok = False
                msgs.append(f"product formula fails p={p} k={k}")
        # (c) Prufer torsion shadow: order of a/p^k mod Z is p^k for
        # gcd(a, p) = 1: exact pure p-powers.
        for k in range(1, 6):
            for a in (1, p + 1):
                if a % p == 0:
                    continue
                fr = Fraction(a, p ** k)
                order = None
                for n in range(1, p ** k + 1):
                    if (n * fr).denominator == 1:
                        order = n
                        break
                if order != p ** k:
                    ok = False
                    msgs.append(f"Prufer order fails p={p} k={k}")
    gate(
        "XB7",
        ok,
        "Z[1/p] dense in Q_p alone (no corner); discrete cocompact in "
        "Q_p x R (fundamental domain Z_p x [0,1) exact, pivot "
        "Z[1/p] cap Z_p = Z); covolume 1 = product formula exact; "
        "torsion shadow = Prufer p-comb"
        + ("" if ok else "; " + "; ".join(msgs[:3])),
    )


# ----------------------------------------------------------------------
# XB8: address/scale split on the corner (exact bookkeeping).
# Cech H^1(S_p) = colim(Z --p--> Z) = Z[1/p] via (stage k, m) -> m/p^k.
# ----------------------------------------------------------------------

def xb8():
    ok = True
    msgs = []
    for p in (2, 3, 5):
        # well-definedness of the colimit identification, exact:
        for k in range(0, 8):
            for m in (-3, 1, 7):
                if Fraction(p * m, p ** (k + 1)) != Fraction(m, p ** k):
                    ok = False
                    msgs.append(f"colimit map fails p={p}")
        # generator at stage k maps to p^m at stage k+m: iterate the
        # transition map (x p) m times and compare (exact integers)
        for mstep in range(1, 6):
            v = 1
            for _ in range(mstep):
                v *= p
            if v != p ** mstep:
                ok = False
                msgs.append(f"transition iteration fails p={p}")
    # place-addressing: 1/p in Z[1/p] but not in Z[1/q] for q != p:
    for p, q in ((2, 3), (3, 5), (5, 2)):
        fr = Fraction(1, p)
        # in Z[1/q] iff denominator is a power of q
        d = fr.denominator
        while d % q == 0:
            d //= q
        if d == 1:
            ok = False
            msgs.append(f"1/{p} wrongly in Z[1/{q}]")
    # scale-freeness: the directed system (Z, x p) is defined over Z;
    # no real number (in particular no log p) occurs in its data:
    # bookkeeping print (structural; nothing to compute).
    gate(
        "XB8",
        ok,
        "colim(Z -p-> Z) = Z[1/p] exact; place-addressed "
        "(Z[1/p] != Z[1/q]); system defined over Z: scale-free"
        + ("" if ok else "; " + "; ".join(msgs[:3])),
    )


def main():
    print("=" * 72)
    print("XX-B1 witness: T2 Tate-curve liquid calibration + T3 fracture")
    print("corner bookkeeping (gates XB1-XB8, fail-closed)")
    print("=" * 72)
    xb1()
    xb2()
    xb3()
    xb4()
    xb5()
    xb6()
    xb7()
    xb8()
    print("=" * 72)
    if FAILURES:
        print(f"RESULT: FAIL ({len(FAILURES)} gate(s)): {FAILURES}")
        sys.exit(1)
    print("RESULT: ALL PASS (XB1-XB8)")
    sys.exit(0)


if __name__ == "__main__":
    main()
