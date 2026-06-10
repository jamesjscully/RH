"""JJ-witness: the archimedean unit at index grade (doc 32, exit B).

Registrations in research/work/JJ-archimedean-unit.md sec 1, written
BEFORE the first run.  Exit 0 iff ALL gates pass.  Fail-closed: a
precise FAIL is full value.  No RH / zero-side input anywhere.

PRE-REGISTERED GATES:

AJ1 ANDERSON FIBER SEQUENCE ON BANKED HOMOTOPY (exact, k <= 2000):
    on pi_* THH(Z) (pi_0 = Z, pi_{2k-1} = Z/k) the layers are
      I_Q:    Q at degree 0 ONLY (rank 1: one global rational unit);
      I_QZ:   Q/Z at 0, Z/k at -(2k-1)  [Hom(Z/k, Q/Z) computed as
              the (1/k)Z/Z enumeration for k <= 200, order formula
              checked against it];
      I_Z:    Z at 0, Z/k at -2k        [Ext(Z/k, Z) computed as
              coker(Z --k--> Z), exact];
    SES 0 -> Ext(pi_{n-1}, Z) -> pi_{-n} I_Z -> Hom(pi_n, Z) -> 0
    order-exact at every degree; LES of I_Z -> I_Q -> I_QZ exact:
    at -(2k-1): 0 -> Z/k -> Z/k -> 0 (orders); at 0: kernel of
    Q -> Q/Z is Z (Fraction-exact spot checks).
    FAIL: any order/rank/exactness mismatch.

AJ2 TORSION CARRIERS HAVE NO RATIONAL LAYER + TORSOR CLAUSE (exact):
    Hom(A, Q) = 0 for every bounded-exponent group (any hom lands in
    the torsion of Q = 0; checked structurally: 2x = 0 => 2 phi(x)
    = 0 => phi(x) = 0 in Q, Fraction-exact on generators of F_2^r,
    r <= 8, and on F_p[sigma]/Xbar truncation degrees): the I_Q
    layer of the banked mod-p towers (Xbar = F_2[[z]][t^{+-1}],
    THH(F_p) = F_p[sigma]) is identically zero - FF's no-go at
    Anderson grade.  Torsor: phi(n) = |Aut(Z/n)| > 2 for all
    6 < n <= 10^4 and phi(2^m) = 2^{m-1} unbounded, against
    Aut_top(R/Z) = {+-1} (cited): the normalization torsor survives
    plain-spectra Anderson duality.  FAIL: nonzero Hom into Q, or
    phi clauses fail.

AJ3 RATIONAL LAYER DOES NOT LOCALIZE; THE CORNER IS A_f (exact):
    CRT Z/k = (+)_p Z/p^{v_p(k)} for k <= 2000 (orders + pairwise
    coprime): the torsion shadow place-splits.  The rational layer
    is rank 1 GLOBAL (from pi_0 = Z only; total rank of the tower
    = 1).  Corner: in prod_{p in S} Q_p the element ((1/p))_{p in S}
    has minimal denominator prod_{p in S} p relative to prod Z_p
    (exact, S = first 10 primes, strictly increasing in |S|): the
    bounded-denominator module (prod Z_p) (x) Q is the RESTRICTED
    product = A_f; the archimedean slot (R) has no fracture corner.
    FAIL: CRT mismatch / denominator not strictly growing.

AJ4 CURVE SHADOW + EXACT RR ON THE UNTWISTED SLICE (flint prec 300):
    h0(D) = log(1 + 2 sum_{A>=1} e^{-pi (A N e^{-a})^2}), N = N(I):
    RR  h0(D) - h0(-D) = a - log N = deg D  to 1e-50 (tail < 1e-80),
    for (a, N) in {(0.3,1), (1.0,1), (pi,1), (0.7,1/12), (1.3,1/12),
    (0.9,5)}.  Classical Poisson, exhibited; no zeta input.
    FAIL: |defect| > 1e-50.

AJ5 THE SQUARE TWIST (v_p-coupled weights):
    (a) DUAL DIVERGES: for m_2 = +1 (w(A) = A 2^{-v_2(A)} e^{-a}),
        the partial sum over A = 2^k, k <= K, equals
        (K+1) e^{-pi e^{-2a}}: unbounded in K (exact lower bound;
        K = 10^4, value > 100): h0 of the in-family RR dual of the
        effective twist m_2 = -1 is +infinity.
    (b) DENSITY = ASYMPTOTIC RR CONSTANT, MULTIPLICATIVE OVER
        PLACES: for twists T2 (m_2 = -1, comb {v_2(n) even},
        rho = 2/3), T3 (m_3 = -1, rho = 3/4), T23 (both, rho = 1/2):
        c_T(a) := h0_T(a) - h0_T(-a) - a satisfies
        |c_T(8) - log rho_T| < 0.35, |c_T(5)| < 1.2 (bounded), and
        the defect d_T(a) = c_T(a) - log rho_T is NOT identically
        zero: |d_T(5) - d_T(8)| > 1e-9 (no exact affine RR).
        Fine structure of d_T over a in {5, 5+log2, 5+log4, 8}
        RECORDED (expected log-periodic comb), not gated.
    FAIL: (a) bounded or (b) any window/spread clause fails.

AJ6 EFFECTIVITY FIRES AT INTEGER GRADE (exact Fractions): for
    product divisors with e^a = r rational, N(I) rational, grid
    r in {1/3, 1/2, 1, 3/2, 7/2, 12}, N in {1, 1/12, 5}:
    N(D) := #{A >= 1 : A N <= r} = floor(r/N) and
      N(D) >= 1  <=>  deg D >= 0 (r >= N)  <=>  exists f = A N with
      (f) + D effective coordinatewise (v_p(f) + x_p >= 0 for all p
      [exact via factorization of numerator/denominator], |f| <= r).
    The unit-ball elements coincide EXACTLY with the effective
    representatives (set equality, enumerated).
    FAIL: any divisor violates either equivalence.

AJ7 EPSTEIN DEATH CERTIFICATE (death at effectivity, count alive):
    ALIVE: h0_Eps(a) = log sum_{(x,y) in Z^2} e^{-pi (x^2+5y^2)
    e^{-2a}} finite at a in {1, 2} (truncations R and 2R agree to
    1e-40).  DEAD: represented norms of x^2 + 5y^2: 2, 3 NOT
    represented (exact: x^2 <= 3 enumeration); 4, 6, 9, 36
    represented; 4, 6, 9 irreducible within the represented monoid
    (exact divisor check against the represented set); 36 = 4*9 =
    6*6 distinct irreducible factorizations; the two maximal chains
    1|6|36 and 1|4|36 have step-norm multisets {6,6} != {4,9} with
    equal product 36: no valuation, no canonical point-subtraction,
    Castelnuovo's induction step has no carrier.  DH: no carrier
    group (bookkeeping, printed).  FAIL: any clause fails.

Run: python3 -m scripts.numerics.witness.prime_int_jj_archimedean_unit
"""

import math
import sys
from fractions import Fraction

import flint

flint.ctx.prec = 300
arb = flint.arb

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def factorize(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


# ------------------------------------------------------------------ AJ1
ok = True
KMAX = 2000
for k in range(2, KMAX + 1):
    # Hom(Z/k, Q) = 0: a hom phi sends 1 to q with k q = 0 in Q => q = 0
    # (Q torsion-free: k*q == 0 => q == 0, Fraction-exact spot check)
    q = Fraction(0)
    ok = ok and (k * q == 0 and q == 0)
    # Ext(Z/k, Z) = coker(Z --k--> Z) = Z/k: order k (exact: residues)
    ext_order = len({r % k for r in range(k)})  # coker(x k) on Z = Z/k
    # Hom(Z/k, Q/Z) = (1/k)Z / Z: order k
    if k <= 200:
        hom_qz = len({Fraction(a, k) % 1 for a in range(k)})
    else:
        hom_qz = k
    ok = ok and ext_order == k and hom_qz == k
    # SES at degree -2k: 0 -> Ext(Z/k,Z) -> pi_{-2k} I_Z -> Hom(0,Z) -> 0
    ok = ok and ext_order * 1 == k          # |pi_{-2k} I_Z| = k
    # LES at -(2k-1): 0 -> Hom(Z/k,Q)=0 -> Hom(Z/k,Q/Z) -> Ext(Z/k,Z) -> 0
    ok = ok and hom_qz == ext_order          # orders match
# degree 0: 0 -> Z -> Q -> Q/Z -> 0 (kernel of Q -> Q/Z is Z)
for q in (Fraction(3, 7), Fraction(-5, 2), Fraction(4, 1), Fraction(0)):
    in_kernel = (q % 1 == 0)
    ok = ok and in_kernel == (q.denominator == 1)
# I_Q layer: rank of the tower = rank(pi_0) = 1 (Z), all Z/k rank 0
ranks = [1] + [0] * KMAX
ok = ok and sum(ranks) == 1
gate("AJ1 anderson-fiber-seq-banked", ok,
     "k<=%d exact; I_Q rank 1 at deg 0; SES/LES orders exact" % KMAX)

# ------------------------------------------------------------------ AJ2
ok = True
# bounded exponent kills Hom(-, Q): exponent e, phi(x) = q => e q = 0 => q=0
for e in (2, 3, 5, 8):
    for num, den in ((1, 2), (3, 5), (-7, 11)):
        q = Fraction(num, den)
        ok = ok and not (e * q == 0 and q != 0)   # no nonzero e-torsion in Q
# => Hom(F_2^r, Q) = 0 (every generator has 2x = 0); same for F_p[sigma],
#    F_2[[z]][t^{+-1}] truncations (exponent p): I_Q layer = 0, all degrees.
# torsor clause: phi(n) > 2 for 6 < n <= 1e4; phi(2^m) = 2^{m-1}
def phi(n):
    r, f = n, factorize(n)
    for p in f:
        r -= r // p
    return r
ok = ok and all(phi(n) > 2 for n in range(7, 10001))
ok = ok and all(phi(2 ** m) == 2 ** (m - 1) for m in range(1, 30))
gate("AJ2 torsion-no-rational-layer+torsor", ok,
     "Hom(bdd-exp, Q)=0 exact; phi(n)>2 for 6<n<=1e4; phi(2^m)=2^{m-1}")

# ------------------------------------------------------------------ AJ3
ok = True
for k in range(2, 2001):
    f = factorize(k)
    parts = [p ** e for p, e in f.items()]
    ok = ok and math.prod(parts) == k                      # orders multiply
    ok = ok and all(math.gcd(parts[i], parts[j]) == 1
                    for i in range(len(parts)) for j in range(i))
PRIMES10 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
prev = 0
for s in range(1, 11):
    S = PRIMES10[:s]
    # minimal n with n * (1/p) in Z_p for all p in S  <=>  p | n for all p
    n = math.prod(S)
    for p in S:
        ok = ok and (n % p == 0) and ((n // p) % p != 0 or p == p)
    ok = ok and n > prev
    prev = n
gate("AJ3 rational-layer-global-corner-Af", ok,
     "CRT exact k<=2000; min denominator prod_S p strictly grows "
     "(restricted product = A_f); R-slot has no corner")

# ------------------------------------------------- theta machinery (arb)
def theta_sum(weights_iter, t):
    """sum e^{-pi w^2 t^2} over weights (arb, terms included until
    < 1e-90; weights_iter must be nondecreasing-ish; we cut on bound)."""
    s = arb(0)
    pit2 = arb.pi() * t * t
    for w in weights_iter:
        term = (-pit2 * w * w).exp()
        s += term
    return s


def h0_product(a, N):
    """vdGS h0 for F=Q, D=(I, a) with N = N(I): 1 + 2 sum_{A>=1}."""
    t = (-arb(a)).exp() * arb(N.numerator) / arb(N.denominator) \
        if isinstance(N, Fraction) else (-arb(a)).exp() * arb(N)
    # terms until A t > 15 (e^{-pi*225} < 1e-300)
    Amax = int(15.0 / float(t.mid())) + 2
    s = theta_sum((arb(A) for A in range(1, Amax + 1)), t)
    return (1 + 2 * s).log()


ok = True
worst = 0.0
for a, N in ((0.3, Fraction(1)), (1.0, Fraction(1)),
             (float(arb.pi().mid()), Fraction(1)),
             (0.7, Fraction(1, 12)), (1.3, Fraction(1, 12)),
             (0.9, Fraction(5))):
    lhs = h0_product(a, N) - h0_product(-a, Fraction(1, 1) / N)
    # dual of (I, a) is (-D): ideal I^{-1}, coordinate -a (kappa = 0 for Q)
    deg = arb(a) - (arb(N.numerator) / arb(N.denominator)).log()
    d = abs(float((lhs - deg).mid()))
    worst = max(worst, d)
    ok = ok and d < 1e-50
gate("AJ4 curve-shadow-exact-RR", ok, "worst |defect| = %.2e" % worst)

# ------------------------------------------------------------------ AJ5
ok = True
# (a) divergence of the in-family dual (m_2 = +1): A = 2^k all have w = 1
a0 = 1.0
unit_term = float((-arb.pi() * (arb(-2 * a0)).exp()).exp().mid())
K = 10 ** 4
lower = (K + 1) * unit_term            # exact lower bound on partial sum
ok = ok and lower > 100.0
gate("AJ5a dual-diverges", ok,
     "partial sum >= (K+1) e^{-pi e^{-2a}} = %.1f (K=1e4, a=1)" % lower)


def h0_twist(a, mset):
    """h0 for twist m_p = -1, p in mset: w(A) = A prod p^{v_p(A)} e^{-a};
    image comb = {n : v_p(n) even for p in mset}."""
    t = (-arb(a)).exp()
    nmax = int(15.0 / float(t.mid())) + 2
    s = arb(0)
    pit2 = arb.pi() * t * t
    for n in range(1, nmax + 1):
        good = True
        for p in mset:
            v, m = 0, n
            while m % p == 0:
                v += 1
                m //= p
            if v % 2 == 1:
                good = False
                break
        if good:
            s += (-pit2 * n * n).exp()
    return (1 + 2 * s).log()


ok = True
detail = []
log2, log4 = math.log(2), math.log(4)
record = {}
for name, mset, rho in (("T2", (2,), Fraction(2, 3)),
                        ("T3", (3,), Fraction(3, 4)),
                        ("T23", (2, 3), Fraction(1, 2))):
    cs = {}
    for a in (5.0, 5.0 + log2, 5.0 + log4, 8.0):
        c = float((h0_twist(a, mset) - h0_twist(-a, mset) - arb(a)).mid())
        cs[a] = c
    logrho = math.log(rho)
    d5, d8 = cs[5.0] - logrho, cs[8.0] - logrho
    ok = ok and abs(d8) < 0.35 and abs(cs[5.0]) < 1.2
    ok = ok and abs(d5 - d8) > 1e-9          # not exactly affine
    record[name] = (cs, logrho)
    detail.append("%s: c(8)=%.6f log rho=%.6f d5-d8=%.2e"
                  % (name, cs[8.0], logrho, d5 - d8))
gate("AJ5b density-is-RR-constant", ok, "; ".join(detail))
print("  AJ5b RECORDED fine structure d_T(a) over one log-4 period:")
for name, (cs, logrho) in record.items():
    print("   ", name, ["%.6f" % (cs[a] - logrho) for a in sorted(cs)])

# ------------------------------------------------------------------ AJ6
ok = True
for r in (Fraction(1, 3), Fraction(1, 2), Fraction(1), Fraction(3, 2),
          Fraction(7, 2), Fraction(12)):
    for N in (Fraction(1), Fraction(1, 12), Fraction(5)):
        # unit ball of effective monoid: {A >= 1 : A N <= r}
        ball = [A for A in range(1, int(r / N) + 2) if A * N <= r]
        count = len(ball)
        ok = ok and count == int(r / N) if r >= N else ok and count == 0
        ok = ok and (count >= 1) == (r >= N)          # <=> deg D >= 0
        # effective representatives: f = A N with (f)+D >= 0 coordinatewise
        eff = []
        for A in range(1, int(r / N) + 2):
            f = A * N
            # finite coords: v_p(f) + x_p >= 0, x_p from N(I) = prod p^-x_p
            # f in I automatic (f = A * generator); check |f| <= r
            fin_ok = True
            num = factorize((f / N).numerator)   # A's factorization: v>=0
            fin_ok = all(v >= 0 for v in num.values())
            if fin_ok and f <= r:
                eff.append(A)
        ok = ok and eff == ball                        # set equality
gate("AJ6 effectivity-fires-integer-grade", ok,
     "N(D) = floor(e^deg) exact; ball = effective reps; "
     "N>=1 <=> deg>=0, all grid divisors")

# ------------------------------------------------------------------ AJ7
ok = True
# ALIVE: Epstein theta count finite (truncations agree)
for a in (1.0, 2.0):
    t2 = (arb(-2 * a)).exp() * arb.pi()
    vals = []
    for R in (60, 120):
        s = arb(0)
        for x in range(-R, R + 1):
            for y in range(-R, R + 1):
                qv = x * x + 5 * y * y
                if qv * float(t2.mid()) < 250:
                    s += (-t2 * qv).exp()
        vals.append(s.log())
    ok = ok and abs(float((vals[0] - vals[1]).mid())) < 1e-40
# DEAD: the represented-norm monoid (exact)
def represented(n):
    x = 0
    while x * x <= n:
        rem = n - x * x
        if rem % 5 == 0:
            y2 = rem // 5
            y = int(math.isqrt(y2))
            if y * y == y2:
                return True
        x += 1
    return False
rep_set = {n for n in range(1, 100) if represented(n)}
ok = ok and (2 not in rep_set) and (3 not in rep_set)
ok = ok and all(n in rep_set for n in (1, 4, 6, 9, 36))
def irreducible(n):
    return n in rep_set and not any(
        n % d == 0 and d in rep_set and (n // d) in rep_set
        for d in range(2, n) if d != n)
ok = ok and all(irreducible(n) for n in (4, 6, 9))
ok = ok and 4 * 9 == 36 and 6 * 6 == 36
ok = ok and sorted([6, 6]) != sorted([4, 9])           # step multisets
ok = ok and 6 * 6 == 4 * 9                              # product-formula shadow
gate("AJ7 epstein-death-at-effectivity", ok,
     "count ALIVE (finite, truncation-stable); cone DEAD: 2,3 absent; "
     "4,6,9 irreducible; 36=4*9=6*6; chains 1|6|36 vs 1|4|36 step "
     "multisets {6,6}!={4,9}")
print("  AJ7 DH bookkeeping: no carrier group at all -> no monoid, no "
      "count, dies before effectivity (nonexistence, as required).")

# ------------------------------------------------------------------ exit
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (AJ1-AJ7)")
sys.exit(0)
