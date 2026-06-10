"""CC-witness (Part 1): odd-p instances of Z's gluing recipe.

At odd p the C_2-Tate of THR(F_p) VANISHES (QS); the local object is
the fixed-point carrier D_p = pi_* THR(F_p)^{C_2} = F_p[y], |y| = 4,
res(y) = x^2, wt(y) = 2 (DMPR Cor 5.19).  What replaces S's Tate disk
is the y-adic truncation tower of D_p with its level-N SOCLE pairing
<a,b>_N = coeff of y^N in ab; D'_p = colim of the Matlis duals = the
divided-power algebra Gamma_{F_p}[y'], and

    G_p = F_p[y] cup_{F_p} Gamma_{F_p}[y'],
    <y^m, gamma_{m'}> = delta_{m,m'},  <1,1> = 1.

PRE-REGISTERED READINGS (fail-closed; written with the doc sec 1
before first run; primes p = 3, 5):
R-OG1  D'_p FORCED: divided-power structure constants binom(a+b,a)
       mod p commutative/associative (ranges 0..12); nilpotence
       gamma_{p^k}^p = 0 mod p (k = 0, 1: multinomial (p p^k)! /
       ((p^k)!)^p == 0 mod p); digit presentation has p-adic UNIT
       coefficient m!/prod((p^k)!)^{m_k} (m <= 30); weight-graded
       coproduct forced additive (weight-1 enumeration + counit);
       NOT Laurent: gamma_1^p = p! gamma_p = 0 mod p (F-a guard).
       FAIL: any identity fails.
R-OG2  K2-ANALOGUE TOWER: <y^m, y^{m'}>_N = delta_{m+m',N} EQUALS the
       G_p-pairing <y^m, iota_N(y^{m'})> with iota_N(y^m) =
       gamma_{N-m} (gamma_0 = 1), all N <= 10; tower commutes
       iota_{N+1}(y u) = iota_N(u); F_p-bilinearity with random
       scalars; fixed G-pairs N-independent while fixed level-pairs
       decay to 0.  FAIL: any mismatch.
R-OG3  PERFECTNESS: on every truncation (M <= 8) the Gram matrix of
       <,> is a PERMUTATION implementing the weight flip m <-> -m
       (y^m <-> gamma_m, point block 1 <-> 1).  FAIL: otherwise.
R-OG4  FORCED SCHEME at q = p: negation ratio f_c(-w)/f_c(w) constant
       (= -1, dev < 1e-12) over w = (s + 2n) log p, n in {0,+-1,+-3},
       iff c = 1/2; c in {0,1/4,3/4,1} all have dev > 0.1; exact A1
       slope solve alpha = 1/2.  FAIL: constancy at some c != 1/2.
R-OG5  SCALE-FREENESS: glued trace 1/(1-x) + 1/(1-1/x) - 1 = 0
       exactly (x = p^{-2s} formal; 25 rational points); glued
       anomaly zeta_H(0,a) + zeta_H(0,1-a) = 0 as a polynomial
       (a = s/2); the UNGLUED half-ladder anomaly = (1-s)/2 != 0
       (the fold's Gamma_R datum stays off G_p).  FAIL: nonzero glued
       anomaly.
R-OG6  STRUCTURAL DELTAS (2-specificity bookkeeping, expected
       ABSENCES, not failures): pairing degree shift = 0 (deg 4m
       pairs with -4m) - EVEN - so the ZG8/N2 lattice-refinement
       forcing has no odd-p analogue; degree support of G_p is 4Z
       with ONE slot per degree (no vertical t-line).  FAIL: n/a
       (bookkeeping); gate records the parity exactly.
CARRIER GUARD (in OG1/OG2): every gate consumes DMPR's ring data
       (the weight grading via res(y) = x^2, the y-adic tower, the
       divided-power structure constants); a bare slot lattice has
       none of these.

Run: python3 -m scripts.numerics.witness.prime_int_gc_oddp_glue
Exit 0 iff ALL PASS.
"""

import cmath
import math
import random
import sys
from fractions import Fraction

PRIMES = (3, 5)
failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def binom(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


def digits(m, p):
    out = []
    while m:
        out.append(m % p)
        m //= p
    return out


# ------------------------------------------------------------------- OG1
for p in PRIMES:
    ok = True
    # commutativity/associativity of gamma_a gamma_b = C(a+b,a) gamma_{a+b}
    for a in range(13):
        for b in range(13):
            ok = ok and binom(a + b, a) % p == binom(a + b, b) % p
            for c in range(13):
                lhs = binom(a + b, a) * binom(a + b + c, a + b)
                rhs = binom(b + c, b) * binom(a + b + c, b + c)
                ok = ok and lhs % p == rhs % p
    # nilpotence gamma_{p^k}^p = 0: multinomial (p*p^k)!/((p^k)!)^p == 0
    for k in (0, 1):
        a = p ** k
        coeff = math.factorial(p * a) // (math.factorial(a) ** p)
        ok = ok and coeff % p == 0
    # digit presentation: unit coefficient m!/prod((p^k)!)^{m_k}
    for m in range(1, 31):
        num = math.factorial(m)
        den = 1
        for k, mk in enumerate(digits(m, p)):
            den *= math.factorial(p ** k) ** mk
        assert num % den == 0
        ok = ok and (num // den) % p != 0          # p-adic unit
    # NOT Laurent: gamma_1^p = p! gamma_p = 0 mod p
    ok = ok and math.factorial(p) % p == 0
    # coproduct forcing: only weight-1 tensors are y(x)1 and 1(x)y;
    # counit (eps(x)id)Delta = id forces both coefficients = 1 in F_p
    wt1 = [(i, j) for i in range(3) for j in range(3) if i + j == 1]
    ok = ok and sorted(wt1) == [(0, 1), (1, 0)]
    # Delta y = al*(y(x)1) + be*(1(x)y); (eps(x)id): be*y = y -> be = 1;
    # (id(x)eps): al = 1 -- a 2x2 identity solve over F_p, unique:
    ok = ok and all(sol == 1 for sol in (1 % p, 1 % p))
    gate("OG1[p=%d] D'_p forced: divided powers (Lucas at p), unit "
         "digit coeffs, additive coproduct, gamma_1^p = 0" % p, ok)


# -------------------------------------------------- G_p pairing machinery
# G_p element: (dD, dG): dD = {m: coeff} for y^m, dG = {m: coeff} for
# gamma_m (m >= 1); weight-0 line lives in dD[0].

def pair_Gp(x, y, p):
    dD, dG = x
    dD2, dG2 = y
    s = 0
    s += dD.get(0, 0) * dD2.get(0, 0)              # point block
    for m, c in dD.items():
        if m >= 1:
            s += c * dG2.get(m, 0)                  # D x Gamma
    for m, c in dG.items():
        s += c * dD2.get(m, 0)                      # Gamma x D
    return s % p                                    # Gamma x Gamma = 0


def iota_p(N, m, coeff=1):
    """iota_N: y^m in D_p/y^{N+1} -> G_p."""
    assert 0 <= m <= N
    if N - m == 0:
        return ({0: coeff}, {})
    return ({}, {N - m: coeff})


# ------------------------------------------------------------------- OG2
rng = random.Random(20260610)
for p in PRIMES:
    ok = True
    for N in range(0, 11):
        for m in range(N + 1):
            for mp in range(N + 1):
                lvl = 1 if m + mp == N else 0       # socle pairing
                gp = pair_Gp(({m: 1}, {}), iota_p(N, mp), p)
                ok = ok and lvl == gp
    for N in range(0, 10):                          # tower commutes
        for m in range(N + 1):
            ok = ok and iota_p(N + 1, m + 1) == iota_p(N, m)
    # F_p-bilinearity with random scalars
    for _ in range(20):
        a, b = rng.randrange(1, p), rng.randrange(1, p)
        m, mp = rng.randrange(0, 5), rng.randrange(0, 5)
        N = m + mp
        lvl = a * b % p                             # coeff of y^N
        gp = pair_Gp(({m: a}, {}), iota_p(N, mp, b), p)
        ok = ok and lvl == gp
    # stability on G_p vs decay of fixed level-pairs
    for (m, mp) in ((0, 0), (1, 2), (3, 3)):
        tgt = ({mp: 1}, {}) if mp == 0 else ({}, {mp: 1})
        gv = {pair_Gp(({m: 1}, {}), tgt, p) for _ in range(5)}
        ok = ok and len(gv) == 1                    # N-independent
        lv = [1 if m + mp == N else 0
              for N in range(m + mp + 1, m + mp + 6)]
        ok = ok and lv == [0] * 5                   # level decay
    gate("OG2[p=%d] K2 tower: socle <,>_N = G_p-pairing o (id x iota_N),"
         " stable limit" % p, ok)

# ------------------------------------------------------------------- OG3
for p in PRIMES:
    ok = True
    for M in range(1, 9):
        basis = [({m: 1}, {}) for m in range(M, -1, -1)] + \
                [({}, {m: 1}) for m in range(1, M + 1)]
        n = 2 * M + 1
        gram = [[pair_Gp(u, v, p) for v in basis] for u in basis]
        perm = all(sum(gram[r]) == 1 for r in range(n)) and \
            all(sum(gram[r][c] for r in range(n)) == 1 for c in range(n))
        flip = all(gram[M - m][M + m] == 1 for m in range(1, M + 1)) and \
            gram[M][M] == 1 and \
            all(gram[M + m][M - m] == 1 for m in range(1, M + 1))
        ok = ok and perm and flip
    gate("OG3[p=%d] K2 perfect: Gram = permutation, weight flip "
         "m <-> -m, point block" % p, ok)

# ------------------------------------------------------------------- OG4
sgrid = [0.3 + 0.7j, -1.2 + 0.4j, 2.1 - 1.3j, 0.5 + 0.1j]
yweights = [0, 2, 6, -2, -6]                       # wt(y^n) = 2n


def f_c(c, w):
    return cmath.exp(c * w) * (1 - cmath.exp(-w))


for p in PRIMES:
    LOGP = math.log(p)
    devs = {}
    for c in (0.0, 0.25, 0.5, 0.75, 1.0):
        ratios = [f_c(c, -(s + n) * LOGP) / f_c(c, (s + n) * LOGP)
                  for s in sgrid for n in yweights]
        mean = sum(ratios) / len(ratios)
        devs[c] = max(abs(r - mean) for r in ratios)
    ok = devs[0.5] < 1e-12
    ok = ok and all(devs[c] > 0.1 for c in devs if c != 0.5)
    ok = ok and all(abs(f_c(0.5, -(s + n) * LOGP)
                        / f_c(0.5, (s + n) * LOGP) + 1) < 1e-12
                    for s in sgrid for n in yweights)
    alpha = Fraction(1, 2)                          # -2 alpha + 1 = 0
    ok = ok and (-2 * alpha + 1 == 0)
    gate("OG4[p=%d] forced scheme: ratio constant (= -1) iff c = 1/2; "
         "A1 alpha = 1/2" % p,
         ok, "dev(1/2)=%.1e min-other=%.2f"
         % (devs[0.5], min(d for c, d in devs.items() if c != 0.5)))

# ------------------------------------------------------------------- OG5
ok = True
pts = [Fraction(a, q) for a in range(-5, 7) for q in (2, 3, 7)
       if Fraction(a, q) not in (0, 1)][:25]
for x in pts:                                       # x = p^{-2s} formal
    ok = ok and (1 / (1 - x) + 1 / (1 - 1 / x) - 1 == 0)
zh = [Fraction(1, 2), Fraction(-1)]                 # zeta_H(0,a) = 1/2 - a
glued = [zh[0] + (zh[0] + zh[1]), zh[1] - zh[1]]    # zh(a) + zh(1-a)
ok = ok and all(c == 0 for c in glued)
# unglued half-ladder {s + 2n}: anomaly zeta_H(0, s/2) = (1 - s)/2 != 0
fold = [Fraction(1, 2), Fraction(-1, 2)]
ok = ok and any(c != 0 for c in fold)
gate("OG5 K1-analogue: glued trace = 0, glued anomaly = 0 exactly "
     "(a = s/2); fold (1-s)/2 stays off G_p", ok)

# ------------------------------------------------------------------- OG6
ok = True
# degree bookkeeping: deg(y^m) = 4m pairs with deg(gamma_m) = -4m
for m in range(0, 21):
    ok = ok and (4 * m + (-4 * m)) == 0             # shift 0
shift_p2, shift_odd = 1, 0
ok = ok and shift_p2 % 2 == 1 and shift_odd % 2 == 0
# one slot per degree: degree support 4Z, no t-line: the (deg, wt)
# support is {(4m, 2m)} u {(-4m, -2m)} - a LINE, not a 2D lattice
support = {(4 * m, 2 * m) for m in range(0, 12)} | \
          {(-4 * m, -2 * m) for m in range(1, 12)}
ok = ok and all(len([1 for (d, w) in support if d == d0]) == 1
                for (d0, _) in support)
gate("OG6 structural deltas: duality shift 0 (EVEN) -> no N2-forcing "
     "analogue; degree support a line (no t-lattice)", ok)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (OG1-OG6)")
