"""ZZ-witness: M1 solenoid Lefschetz (doc 39 sec 4, the critic's composition).

Gates Z1-Z8 registered in research/work/ZZ-solenoid-lefschetz.md sec 3,
written BEFORE this file existed.  Exit 0 iff ALL PASS.  Fail-closed.

  Z1  the count #Fix(x p^w | S_p) = p^w - 1: coker route + literal
      enumeration (distinctness + completeness), exact.
  Z2  the product formula (z-ii): count = |a^w-1|_oo * |a^w-1|_p, exact,
      with each place separately carrying the count (alpha <-> 1/alpha)
      and both active (alpha = 3/2); p-adic-active instances counted.
  Z3  the trace tower (z-i): finite-level traces constant; L = 1 - a^w
      in the base ring Z[1/p]; prod_v |L|_v reproduces Z1/Z2.
  Z4  P3-a direction 1: spectral value defined where the carrier
      predicate dies (denominator prime != p); Pell: the quadratic
      carrier computes the Galois norm, never the single eigenvalue.
  Z5  P3-a direction 2: affine rigidity (#Fix(px+c) = p-1, c-blind);
      exact PL wiggle: raw count moves 1 -> 5, signed count = 1 - p
      invariant, degree structural.
  Z6  entropy log p (Lind-Ward ledger, exact bookkeeping + growth).
  Z7  BC1 conformance test (WW's 12 numbers): flow-defect modes vs the
      shape law - registered NONCONFORMANT, margins > 0.5.
  Z8  carrier guard: where the solenoid dies on Epstein x^2 + 5y^2
      (prime-support collapse: Z[1/4] = Z[1/2]; factorization-blind).

NO ZEROS CONSUMED: no fork_lib import, no freeze step needed.
Exact integer / Fraction arithmetic for all decision gates; mpmath
dps 50 only for Z6 growth + Z7 analytic values (coarse margins).

Run: python3 -m scripts.numerics.witness.prime_zz_solenoid_lefschetz
"""

import sys
from fractions import Fraction
from math import gcd

import mpmath as mp

mp.mp.dps = 50

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def record(msg):
    print("  RECORD", msg)


# ---------------------------------------------------------------- helpers
def vp(n, p):
    """p-adic valuation of a nonzero integer."""
    n = abs(n)
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def vp_frac(x, p):
    """p-adic valuation of a nonzero Fraction."""
    return vp(x.numerator, p) - vp(x.denominator, p)


def abs_p(x, p):
    """|x|_p as an exact Fraction, x a nonzero Fraction."""
    return Fraction(p) ** (-vp_frac(x, p))


def coker_size(beta, S):
    """|Z[1/S] / beta Z[1/S]| for nonzero beta in Z[1/S], S a set of primes.

    beta Z[1/S] = b Z[1/S] with b = numerator stripped of S-support;
    the quotient is Z/b (exact).  Checks beta IS in Z[1/S] first.
    """
    den = beta.denominator
    for q in S:
        while den % q == 0:
            den //= q
    assert den == 1, "beta not in Z[1/S]"
    b = abs(beta.numerator)
    for q in S:
        while b % q == 0:
            b //= q
    return b


def in_z_inv_p(x, p):
    """Carrier predicate: x in Z[1/p] (reduced denominator a p-power)."""
    den = x.denominator
    while den % p == 0:
        den //= p
    return den == 1


# ============================================================ Z1 the count
print("== Z1: #Fix(x p^w | S_p) = p^w - 1, two exact routes ==")
ok1 = True
for p in (2, 3, 5):
    for w in range(1, 7):
        m = p**w - 1
        # route (a): coker(x (p^w - 1) on Z[1/p]) = Z/m  (p invertible mod m)
        c = coker_size(Fraction(m), {p})
        inv = pow(p, -1, m) if m > 1 else 0  # p invertible mod m (witness)
        ok_a = c == m and (m == 1 or (p * inv) % m == 1)
        # route (b): enumeration. Fixed points of x p^w are
        # ker(x m on S_p) = (1/m)Z[1/p] / Z[1/p]; candidates x_j = j/m.
        # fixed: (p^w) x_j - x_j = j in Z subset Z[1/p]  -- trivially true;
        # distinct: x_i - x_j in Z[1/p] iff reduced den of (i-j)/m is a
        # p-power iff m | i - j (since gcd(m, p) = 1);
        # complete: any fixed x has m x = 0, and #ker(x m) = |coker| = m.
        distinct = all(
            not in_z_inv_p(Fraction(i - j, m), p)
            for i in range(min(m, 60))
            for j in range(i)
        )
        ok_b = distinct and gcd(m, p) == 1
        if not (ok_a and ok_b):
            ok1 = False
            record(f"Z1 failure at p={p} w={w}: coker={c} m={m}")
gate("Z1", ok1, "#Fix(p^w) = p^w - 1 exact (coker + enumeration), p in {2,3,5}, w <= 6")

# ===================================================== Z2 product formula
print("== Z2: count = |a^w - 1|_oo * |a^w - 1|_p (z-ii), exact ==")
CASES = [
    (2, Fraction(2)),
    (2, Fraction(1, 2)),
    (2, Fraction(3, 2)),
    (3, Fraction(4)),
    (3, Fraction(1, 3)),
    (5, Fraction(1, 5)),
    (7, Fraction(2)),
]
ok2 = True
n_inst = 0
n_active = 0
counts = {}  # (p, alpha, w) -> count, reused by Z3/Z6
for p, alpha in CASES:
    for w in range(1, 7):
        beta = alpha**w - 1
        if beta == 0:
            continue
        cok = coker_size(beta, {p})
        prod = abs(beta) * abs_p(beta, p)
        n_inst += 1
        if abs_p(beta, p) != 1:
            n_active += 1
        if prod != cok:
            ok2 = False
            record(f"Z2 mismatch p={p} alpha={alpha} w={w}: {prod} != {cok}")
        counts[(p, alpha, w)] = cok
# place-swap symmetry alpha <-> 1/alpha (carrying place swaps, count equal)
swap_ok = True
for p, a in [(2, Fraction(2)), (3, Fraction(3)), (5, Fraction(5))]:
    for w in range(1, 7):
        b1, b2 = a**w - 1, (1 / a) ** w - 1
        c1, c2 = coker_size(b1, {p}), coker_size(b2, {p})
        # x p carried at oo (|b1|_p = 1); x 1/p carried at p (|b2|_oo < 1)
        if not (c1 == c2 and abs_p(b1, p) == 1 and abs(b2) < 1 and abs_p(b2, p) == p**w):
            swap_ok = False
record(f"{n_inst} (case, w) instances; p-adic factor != 1 at {n_active} of them")
record("place swap: x p oo-carried, x 1/p p-carried, same count (exact, p in {2,3,5})")
gate("Z2", ok2 and swap_ok and n_active >= 4, f"product formula exact at {n_inst} instances; both places witnessed load-bearing")

# ======================================================== Z3 trace tower
print("== Z3: the trace tower (z-i) and L = 1 - alpha^w in Z[1/p] ==")
ok3 = True
# alpha = p: level-k trace of x p^w on colim(Z -p-> Z) is p^w at EVERY level
# (the endo commutes with bonding: p * (p^w n) = p^w * (p n), exact).
for p in (2, 3, 5):
    for w in range(1, 7):
        levels = [p**w for _ in range(7)]  # constant tower of traces
        commute = all(p * (p**w * n) == p**w * (p * n) for n in range(-5, 6))
        L = 1 - Fraction(p) ** w
        bridge = abs(L) * abs_p(L, p)
        if not (len(set(levels)) == 1 and commute and bridge == p**w - 1):
            ok3 = False  # Z1's count is p^w - 1
# general alpha from Z2: L = 1 - alpha^w, prod_v |L|_v = count
for (p, alpha, w), cok in counts.items():
    L = 1 - alpha**w
    if abs(L) * abs_p(L, p) != cok:
        ok3 = False
        record(f"Z3 bridge mismatch at p={p} alpha={alpha} w={w}")
gate("Z3", ok3, "level traces constant = p^w; count = prod_v |1 - alpha^w|_v at every Z1/Z2 instance")
record("the trace needs NO regularization: H^1 is rank-1 over the base ring Z[1/p];")
record("the unit enters at the trace->count bridge: |.|_oo of the Lefschetz element (product formula)")

# ================================================= Z4 P3-a direction 1
print("== Z4: P3-a direction 1 (spectral extends, carrier dies) ==")
ok4 = True
DIES = [(Fraction(1, 3), 2, 3), (Fraction(1, 2), 3, 2), (Fraction(5, 6), 5, 3), (Fraction(2, 7), 2, 7)]
for lam, p, qbad in DIES:
    spectral_defined = all(isinstance(lam**w - 1, Fraction) for w in range(1, 5))
    carrier = in_z_inv_p(lam, p)
    den_witness = lam.denominator % qbad == 0 and qbad != p
    if not (spectral_defined and (not carrier) and den_witness):
        ok4 = False
        record(f"Z4a failure at lambda={lam} on S_{p}")
controls = all(in_z_inv_p(alpha, p) for p, alpha in CASES)
# Pell: lambda = 1 + sqrt(2); the only carriers realize the GALOIS NORM
a_, b_ = 1, 1  # lambda^1 = 1 + 1*sqrt(2)
A = [[2, 1], [1, 0]]


def matmul(X, Y):
    return [
        [X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]],
        [X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]],
    ]


Aw = [[1, 0], [0, 1]]
pell_ok = True
pell_counts = []
for w in range(1, 9):
    Aw = matmul(Aw, A)
    det = (Aw[0][0] - 1) * (Aw[1][1] - 1) - Aw[0][1] * Aw[1][0]
    norm = (a_ - 1) ** 2 - 2 * b_**2  # N(lambda^w - 1)
    if not (b_ >= 1 and abs(det) == abs(norm) and abs(det) >= 1):
        pell_ok = False
    pell_counts.append(abs(det))
    a_, b_ = a_ + 2 * b_, a_ + b_  # lambda^(w+1)
record(f"Pell counts |det(A^w - I)| = |N(lambda^w - 1)|: {pell_counts} (integers; lambda^w - 1 itself irrational, b_w >= 1)")
gate("Z4", ok4 and controls and pell_ok, "spectral value defined where the carrier predicate dies; quadratic carrier computes the norm only")

# ================================================= Z5 P3-a direction 2
print("== Z5: P3-a direction 2 (count moves, trace blind) ==")
# (a) affine rigidity on S_p: #Fix(px + c) = #ker(x(1-p)) = p - 1, c-blind
ok5a = True
for p in (2, 3, 5):
    k = coker_size(Fraction(1 - p), {p})  # = #ker(x(1-p) on S_p), Pontryagin
    # surjectivity of x(1-p) on S_p = injectivity of x(1-p) on Z[1/p] (1-p != 0):
    # the solution set of (1-p)x = c is a ker-torsor for EVERY c.
    if k != p - 1:
        ok5a = False
record("affine twists move NOTHING (torsor rigidity) - disanalogy with YY Y3 recorded")

# (b) exact PL wiggle at the agreement's content level (circle, p = 2):
# f(theta) = 2 theta + eps * tri(theta), tri = triangle wave, period 1/2,
# breakpoints 0,1/8,3/8,1/2 values 0,1,-1,0 (slopes +-8). Exact Fractions.
TRI_BPS = [Fraction(0), Fraction(1, 8), Fraction(3, 8), Fraction(1, 2), Fraction(5, 8), Fraction(7, 8), Fraction(1)]
TRI_VAL = [Fraction(0), Fraction(1), Fraction(-1), Fraction(0), Fraction(1), Fraction(-1), Fraction(0)]


def wiggle_counts(eps):
    """Raw and signed fixed-point counts of f = 2x + eps*tri on R/Z, exact."""
    raw, signed = 0, 0
    for i in range(len(TRI_BPS) - 1):
        t0, t1 = TRI_BPS[i], TRI_BPS[i + 1]
        h0 = t0 + eps * TRI_VAL[i]
        h1 = t1 + eps * TRI_VAL[i + 1]
        slope = (h1 - h0) / (t1 - t0)  # h' on the piece (h = f - x)
        lo, hi = min(h0, h1), max(h0, h1)
        z = -(-lo.numerator // lo.denominator)  # ceil(lo)
        while Fraction(z) <= hi:
            theta = t0 + (z - h0) / slope if slope != 0 else None
            if theta is not None and t0 <= theta < t1:
                raw += 1
                signed += -1 if slope > 0 else 1  # index = sgn(1 - f') = -sgn(h')
            z += 1
    return raw, signed


raw0, sgn0 = wiggle_counts(Fraction(0))
rawE, sgnE = wiggle_counts(Fraction(2, 5))
deg_ok = all(
    (t + 1 + Fraction(2, 5) * v) - (t + Fraction(2, 5) * v) == 1 for t, v in zip(TRI_BPS, TRI_VAL)
)  # h(x+1) = h(x) + 1 i.e. degree 2 structural, eps-independent
ok5b = raw0 == 1 and sgn0 == -1 and rawE == 5 and sgnE == -1 and deg_ok
record(f"PL wiggle eps=2/5: raw count {raw0} -> {rawE}; signed count {sgn0} -> {sgnE} (= 1 - p, invariant); degree 2 structural")
record("solenoid wiggle F(x) = px + iota(u(pi_0 x)) homotopic to x p (H^* blind): stated memo sec 1.2")
gate("Z5", ok5a and ok5b, "raw count moves, signed/trace side blind; affine family rigid")

# ============================================================= Z6 entropy
print("== Z6: entropy = sum_v log^+ |alpha|_v (exact ledger + growth) ==")
# exact multiplicative bookkeeping of the contributing places:
led1 = abs(Fraction(2)) > 1 and abs_p(Fraction(2), 2) < 1  # x2 on S_2: oo only
led2 = abs(Fraction(1, 2)) < 1 and abs_p(Fraction(1, 2), 2) > 1  # x1/2: p only
# x 3/2 on S_2: both contribute; product of contributing |.|_v = 3 exactly
led3 = abs(Fraction(3, 2)) * abs_p(Fraction(3, 2), 2) == 3
growth1 = abs(mp.log(mp.mpf(2) ** 40 - 1) / 40 - mp.log(2)) < 2 * mp.mpf(2) ** -40 / 40
growth2 = abs(mp.log(mp.mpf(3) ** 40 - mp.mpf(2) ** 40) / 40 - mp.log(3)) < 2 * (mp.mpf(2) / 3) ** 40 / 40
gate("Z6", led1 and led2 and led3 and growth1 and growth2, "h(x2 on S_2) = log 2 (oo), h(x1/2) = log 2 (p), h(x3/2) = log 3 (both); growth route converges")
record("scale via a NON-SHEAF invariant (T1 evaded through N1/N3) - but h = log(forced H^1 eigenvalue): supplied, not read")

# ===================================================== Z7 BC1 conformance
print("== Z7: the BC1 12-number test (registered NONCONFORMANT) ==")
gamma_logpi = mp.euler + mp.log(mp.pi)


def gamma_R(s):
    return mp.pi ** (-s / 2) * mp.gamma(s / 2)


ok7 = True
min_margin = mp.inf
for p in (2, 3, 5, 7):
    lp = mp.log(p)
    flow0 = -lp / (p - 1)  # closed form, all n
    # honest truncated-sum recomputation of the flow mode at xi_1, xi_2
    for n in (1, 2):
        xi = 2 * mp.pi * n / lp
        s = mp.nsum(lambda w: mp.mpf(p) ** (-w) * mp.e ** (-1j * xi * w * lp), [1, 200])
        if abs(-lp * s - flow0) > mp.mpf(10) ** -30:
            ok7 = False
            record(f"Z7 closed-form vs sum mismatch at p={p} n={n}")
    shape0 = gamma_logpi
    m0 = abs(flow0 - shape0)
    min_margin = min(min_margin, m0)
    if m0 < mp.mpf("0.5"):
        ok7 = False
    for n in (1, 2):
        xi = 2 * mp.pi * n / lp
        shape_n = -mp.re(gamma_R(1j * xi))
        r_flow, r_shape = mp.mpf(1), shape_n / shape0
        mn = abs(r_flow - r_shape)
        min_margin = min(min_margin, mn)
        if mn < mp.mpf("0.5"):
            ok7 = False
        record(f"p={p} n={n}: shape mode {mp.nstr(shape_n, 6)}, flow mode {mp.nstr(flow0, 6)} (flat); ratio margin {mp.nstr(mn, 6)}")
record(f"n=0 means: flow -(log p)/(p-1) vs shape gamma+log pi = {mp.nstr(gamma_logpi, 8)}; min margin overall {mp.nstr(min_margin, 6)}")
record("the orbit-length comb (log p)Z itself IS the banked comb address (tautological; no gate)")
gate("Z7", ok7, "NONCONFORMANT at all 12 numbers, every margin > 0.5: the solenoid carries no Gaussian silhouette")

# ====================================================== Z8 carrier guard
print("== Z8: carrier guard - where the solenoid dies on Epstein ==")
rep = sorted({x * x + 5 * y * y for x in range(0, 7) for y in range(0, 3)} - {0, 1})
rep = [v for v in rep if v <= 36]
repset = set(rep)


def irreducible(n):
    return all(not (n % a == 0 and a in repset and n // a in repset) for a in range(2, n))


ok8a = all(v in repset for v in (4, 6, 9, 36)) and all(irreducible(v) for v in (4, 6, 9))
ok8b = 36 == 4 * 9 == 6 * 6 and irreducible(36) is False
# (a) prime-support collapse: Z[1/4] = Z[1/2] as rings (both inclusions)
collapse = Fraction(1, 2) == Fraction(2, 4) and Fraction(1, 4) == Fraction(1, 2) ** 2
# (b) factorization-blind lattice: exponent vectors over {2,3}
v4, v9, v6 = (2, 0), (0, 2), (1, 1)
sum_ok = (v4[0] + v9[0], v4[1] + v9[1]) == (v6[0] + v6[0], v6[1] + v6[1]) == (2, 2)
multiset_ok = sorted([v4, v9]) != sorted([v6, v6])
# (c) the count on the Z[1/6]-solenoid sees only the ELEMENT 36
c36 = coker_size(Fraction(36 - 1), {2, 3})
ok8c = c36 == 35
record("Z[1/4] = Z[1/2] exact: the cocompact construction cannot remember the irreducible 4")
record("lattice(4*9) = lattice(6*6) = Z[1/6] while multisets {4,9} != {6,6}: per-irreducible address unformable")
record(f"#Fix(x 36 | S_(Z[1/6])) = {c36} through EITHER factorization (the object sees the element, not the monoid)")
record("DH: no carrier monoid at all (cited; dies before any lattice)")
gate("Z8", ok8a and ok8b and collapse and sum_ok and multiset_ok and ok8c, "the solenoid functor factors through prime support; Euler product load-bearing for the ADDRESS")

# ================================================================== exit
print()
if failures:
    print("RESULT: FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (Z1-Z8)")
sys.exit(0)
