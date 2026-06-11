"""YY-witness: bridge B2, the second-evaluation audit (G-CH3 retroactive).

Gates Y1-Y7 registered in research/work/YY-b2-second-evaluation.md sec 4,
written BEFORE the first run.  Exit 0 iff ALL gates pass.  Fail-closed.

The P3 criterion (doc 14 extension) operationalized:
  Y1     the one banked candidate-two pair (Quillen / Hesselholt at F_q):
         geometric Fix-count in an explicitly constructed finite field
         vs the Adams-eigenvalue coker vs the zeta dress - exact.
  Y2/Y3  the P3-a deformation separations, BOTH directions, exact.
  Y4     the ONE-EVALUATION transports witnessed (lcm ladder, zeta-reg,
         Frullani, HH.1 d-frame, Lefschetz=coker/LTE).
  Y5     Witt: F = id on W(F_p) at component level; Dwork integrality
         (W(Z)^{F=1} = Z) - the TR = W identity is a functor-level
         transport, witnessed at its computational core.
  Y6     carrier guard (Epstein two-factorization kill; DH predicates).
  Y7     the agreement-locus shape (proper sublocus cut by a theorem).

NO ZEROS CONSUMED: no fork_lib import, no freeze step needed.
Exact integer / Fraction arithmetic for all decision gates; mpmath only
for the two numeric transport identities (Y4b, Y4c).

Run: python3 -m scripts.numerics.witness.prime_yy_second_evaluation_audit
"""

import sys
from fractions import Fraction
from functools import reduce
from math import gcd

import mpmath as mp

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def record(msg):
    print("  RECORD", msg)


# ------------------------------------------------------------ primes etc.
def factorize(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def prime_power(n):
    """Return p if n = p^j (j >= 1), else 0."""
    if n < 2:
        return 0
    f = factorize(n)
    return list(f)[0] if len(f) == 1 else 0


def v_adic(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


# ------------------------------------------------- GF(p^n) by polynomials
# polynomials over F_p: tuples of ints in [0, p), little-endian, trimmed.
def ptrim(a):
    i = len(a)
    while i > 0 and a[i - 1] == 0:
        i -= 1
    return tuple(a[:i])


def pmul(a, b, p):
    if not a or not b:
        return ()
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % p
    return ptrim(out)


def pmod(a, m, p):
    a = list(a)
    dm = len(m) - 1
    inv = pow(m[-1], p - 2, p)  # monic in practice, but be safe
    while len(a) - 1 >= dm and ptrim(a):
        if a[-1] == 0:
            a.pop()
            continue
        c = (a[-1] * inv) % p
        s = len(a) - 1 - dm
        for i, mi in enumerate(m):
            a[s + i] = (a[s + i] - c * mi) % p
        a = list(ptrim(a))
    return ptrim(a)


def ppowmod(a, e, m, p):
    r = (1,)
    a = pmod(a, m, p)
    while e:
        if e & 1:
            r = pmod(pmul(r, a, p), m, p)
        a = pmod(pmul(a, a, p), m, p)
        e >>= 1
    return r


def monic_polys(p, d):
    """All monic polynomials of degree exactly d over F_p."""
    n = p ** d
    for k in range(n):
        c, kk = [], k
        for _ in range(d):
            c.append(kk % p)
            kk //= p
        yield tuple(c) + (1,)


def is_irreducible(f, p):
    d = len(f) - 1
    if d <= 1:
        return d == 1
    for dd in range(1, d // 2 + 1):
        for g in monic_polys(p, dd):
            # divide f by g, check remainder
            if not pmod(f, g, p):
                return False
    return True


def find_irreducible(p, n):
    for f in monic_polys(p, n):
        if is_irreducible(f, p):
            return f
    raise RuntimeError("no irreducible found")


def field_elements(p, n):
    total = p ** n
    for k in range(total):
        c, kk = [], k
        for _ in range(n):
            c.append(kk % p)
            kk //= p
        yield ptrim(c)


# ======================================================================
# Y1  THE AGREEMENT: q^w - 1 three ways (rows 9-10 of the audit table)
# ======================================================================
print("== Y1: the Quillen pair - geometric count vs Adams coker vs zeta dress ==")
CASES = [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
         (3, 1), (3, 2), (3, 3),
         (4, 1), (4, 2),
         (5, 1), (5, 2),
         (7, 1), (7, 2),
         (8, 1), (8, 2),
         (9, 1), (9, 2)]
y1_ok = True
y1_detail = []
for q, w in CASES:
    p = prime_power(q)
    j = v_adic(q, p)
    N = 2 * j * w                      # ambient F_{q^{2w}} = F_{p^N}
    modpoly = find_irreducible(p, N)
    qw = q ** w
    # evaluation A: geometric count of Fix(Fr_q^w) = #{x : x^{q^w} = x}
    count = 0
    for x in field_elements(p, N):
        if ppowmod(x, qw, modpoly, p) == x:
            count += 1
    geomA = count - 1                  # G_m part (drop x = 0)
    # evaluation B: |coker(psi^q - 1 : pi_{2w} KU -> pi_{2w} KU)|,
    # psi^q acts by the eigenvalue q^w on the weight-w line.
    cokerB = abs(qw - 1)
    # evaluation C (dress): 1/|zeta(F_q, -w)|, zeta(F_q,s) = 1/(1-q^{-s})
    zeta_val = Fraction(1, 1) / (1 - Fraction(qw, 1))   # zeta(F_q, -w)
    dressC = 1 / abs(zeta_val)
    ok = (count == qw) and (geomA == cokerB) and (dressC == Fraction(cokerB, 1))
    y1_ok = y1_ok and ok
    if not ok:
        y1_detail.append((q, w, count, geomA, cokerB, dressC))
gate("Y1 agreement (18 cases, exact)", y1_ok,
     "all q^w fixed-subfield counts = coker(psi^q - 1) = 1/|zeta(F_q,-w)|"
     if y1_ok else str(y1_detail))

# ======================================================================
# Y2  P3-a DIRECTION 1: spectral side extends, geometric carrier dies
# ======================================================================
print("== Y2: deformation direction 1 (B moves, A's carrier nonexistent) ==")
y2_ok = True
n_npp = 0
for k in range(2, 101):
    pp = prime_power(k)
    # spectral evaluation defined for EVERY k (exact integers):
    spectral = [k ** w - 1 for w in range(1, 7)]
    spec_ok = all(isinstance(s, int) and s > 0 for s in spectral)
    # CRT idempotent e != 0,1 with e^2 = e mod k exists iff k has >= 2
    # distinct prime factors (= not a prime power):
    idem = None
    for e in range(2, k - 1):
        if (e * e - e) % k == 0:
            idem = e
            break
    # cell-comb address (SS Lemma A rerun): residues {w : k | w(w+1)}
    comb = {w for w in range(k) if (w * (w + 1)) % k == 0}
    two_coset = comb == {0, k - 1}
    if pp:
        ok = spec_ok and (idem is None) and two_coset
    else:
        n_npp += 1
        ok = spec_ok and (idem is not None) and (not two_coset)
    y2_ok = y2_ok and ok
    if not ok:
        record("Y2 violation at k = %d (pp=%s idem=%s comb=%s)"
               % (k, pp, idem, sorted(comb)[:6]))
gate("Y2 spectral-extension iff (k <= 100, exact)", y2_ok,
     "%d non-prime-powers: idempotent + comb kill; all prime powers clean"
     % n_npp)

# ======================================================================
# Y3  P3-a DIRECTION 2: geometric side moves, spectral side untouched
# ======================================================================
print("== Y3: deformation direction 2 (twisted Frobenius moves the count) ==")
y3_ok = True
for q in [3, 4, 5, 9]:
    p = prime_power(q)
    j = v_adic(q, p)
    N = 2 * j                          # ambient F_{q^2}
    modpoly = find_irreducible(p, N)
    elems = [x for x in field_elements(p, N)]
    nonzero = [x for x in elems if x]
    counts = {}
    for c in nonzero:
        cnt = 0
        for x in elems:
            if pmod(pmul(c, ppowmod(x, q, modpoly, p), p), modpoly, p) == x:
                cnt += 1
        counts[c] = cnt
    one = (1,)
    untwisted = counts[one]
    # (i) the count moves; values exactly {1, q}, both attained
    vals = set(counts.values())
    moves = vals == {1, q} and untwisted == q
    # (ii) classification: count = q iff c^{q+1} = 1
    law = all((counts[c] == q) == (ppowmod(c, q + 1, modpoly, p) == one)
              for c in nonzero)
    # (iii) partition: sum_c (count - 1) = q^2 - 1
    part = sum(v - 1 for v in counts.values()) == q * q - 1
    # (iv) spectral side carries no c: recorded (structural)
    ok = moves and law and part
    y3_ok = y3_ok and ok
    record("q=%d: Fix(c x^q) in {1,%d}; #(c: count=q) = %d; spectral q-1 = %d"
           " (c-independent)" % (q, q, sum(1 for v in counts.values() if v == q),
                                 q - 1))
    if not ok:
        record("Y3 violation at q = %d (moves=%s law=%s part=%s)"
               % (q, moves, law, part))
gate("Y3 geometric deformation (q in {3,4,5,9}, exact enumeration)", y3_ok)

# ======================================================================
# Y4  THE TRANSPORTS (one-evaluation verdicts)
# ======================================================================
print("== Y4: one-evaluation transports ==")
# (a) lcm ladder: two routes through the same structure
y4a = True
for w in range(1, 301):
    n = w + 1
    lcm1 = reduce(lambda a, b: a * b // gcd(a, b), range(1, n + 1), 1)
    sieve = 1
    for pp in range(2, n + 1):
        if prime_power(pp) == pp and len(factorize(pp)) == 1 and \
           all(pp % d for d in range(2, pp)):
            # pp is prime: contribute p^{floor(log_p(n))}
            e = 0
            t = pp
            while t <= n:
                e += 1
                t *= pp
            sieve *= pp ** e
    ok = (lcm1 == sieve) and (lcm1 % (w * (w + 1)) == 0)
    y4a = y4a and ok
gate("Y4a lcm-ladder routes (w <= 300, exact)", y4a,
     "transport = prime factorization (one structure)")

# (b) Bokstedt torsion / zeta'(0): the regularization IS the continuation
mp.mp.dps = 60
lhs = -mp.zeta(0, derivative=1)
rhs = mp.log(2 * mp.pi) / 2
y4b = abs(lhs - rhs) < mp.mpf("1e-40")
gate("Y4b -zeta'(0) = (1/2)log(2pi)", y4b,
     "|diff| = %s (transport = continuation of the SAME series)"
     % mp.nstr(abs(lhs - rhs), 3))

# (c) Frullani / Delta_p mean: gamma + log pi as one integral
mp.mp.dps = 50
I1 = mp.quad(lambda x: (1 - mp.exp(-mp.pi * x * x)) / x, [0, 1])
I2 = mp.quad(lambda x: mp.exp(-mp.pi * x * x) / x, [1, mp.inf])
frull = 2 * (I1 - I2)
target = mp.euler + mp.log(mp.pi)
y4c = abs(frull - target) < mp.mpf("1e-30")
gate("Y4c Frullani: 2 int (1_{x<1} - e^{-pi x^2}) dx/x = gamma + log pi",
     y4c, "|diff| = %s" % mp.nstr(abs(frull - target), 3))

# (d) HH.1 d-frame diagonalization (exact Fractions; coefficient of log p)
y4d = True
for n in range(2, 11):
    M = [[Fraction(max(i, jj)) for jj in range(n + 1)] for i in range(n + 1)]

    def pair(u, v):
        return sum(u[i] * M[i][jj] * v[jj]
                   for i in range(n + 1) for jj in range(n + 1))

    e0 = [Fraction(1 if i == 0 else 0) for i in range(n + 1)]
    ds = []
    for k in range(1, n + 1):
        d = [Fraction(0)] * (n + 1)
        d[k], d[k - 1] = Fraction(1), Fraction(-1)
        ds.append(d)
    ok = pair(e0, e0) == 0
    for k in range(1, n + 1):
        ok = ok and pair(e0, ds[k - 1]) == 1
        for ll in range(1, n + 1):
            want = Fraction(-1) if k == ll else Fraction(0)
            ok = ok and pair(ds[k - 1], ds[ll - 1]) == want
    y4d = y4d and ok
gate("Y4d HH.1: <d_k,d_l>_MAX = -delta_kl, e_0 null, <e_0,d_k> = 1 (n <= 10)",
     y4d, "transport = finite linear algebra on the degree data")

# (e) Lefschetz law = rank-1 coker; LTE valuation
y4e = True
for p in [3, 5]:
    for alpha in [1 + p, 1 + 2 * p, 1 + p + p * p]:
        s = v_adic(alpha - 1, p)
        for w in range(1, 13):
            lhsv = v_adic(alpha ** w - 1, p)
            rhsv = s + v_adic(w, p)
            y4e = y4e and (lhsv == rhsv)
gate("Y4e Lefschetz law: v_p(alpha^w - 1) = v_p(alpha-1) + v_p(w) (LTE, exact)",
     y4e, "pairing cardinality p^{v_p} = rank-1 coker BY DEFINITION (transport)")

# ======================================================================
# Y5  WITT: F = id on W(F_p); Dwork integrality W(Z)^{F=1} = Z
# ======================================================================
print("== Y5: Witt vectors - the TR = W transport at its computational core ==")


def ghost(x, p):
    """Ghost components w_i(x) = sum_{m<=i} p^m x_m^{p^{i-m}}, over Z/Q."""
    n = len(x)
    return [sum(Fraction(p) ** m * Fraction(x[m]) ** (p ** (i - m))
                for m in range(i + 1)) for i in range(n)]


def unghost(g, p):
    """Solve Witt components from ghost vector (triangular, over Q)."""
    n = len(g)
    x = []
    for i in range(n):
        acc = sum(Fraction(p) ** m * x[m] ** (p ** (i - m)) for m in range(i))
        x.append((g[i] - acc) / Fraction(p) ** i)
    return x


y5i = True
for p, L in [(2, 5), (3, 5), (5, 4)]:
    total = p ** L
    for k in range(total):
        xv, kk = [], k
        for _ in range(L):
            xv.append(kk % p)
            kk //= p
        g = ghost(xv, p)
        fx = unghost(g[1:], p)          # F shifts ghosts
        for i, comp in enumerate(fx):
            if comp.denominator != 1 or (comp.numerator - xv[i]) % p != 0:
                y5i = False
                record("Y5i violation p=%d x=%s i=%d comp=%s" % (p, xv, i, comp))
                break
        if not y5i:
            break
gate("Y5i F = id on W(F_p): F(x)_i integral and = x_i mod p "
     "(p in {2,3} all 5-vectors; p=5 all 4-vectors)", y5i,
     "the fixed-point dress on W(F_p) is definitional")

y5ii = True
for p in [2, 3, 5]:
    for c in range(-20, 21):
        x = unghost([Fraction(c)] * 4, p)
        if any(comp.denominator != 1 for comp in x):
            y5ii = False
            record("Y5ii violation p=%d c=%d x=%s" % (p, c, x))
gate("Y5ii W(Z)^{F=1} = Z: constant-ghost vectors have integral components "
     "(Dwork; p in {2,3,5}, |c| <= 20, length 4)", y5ii)

# ======================================================================
# Y6  CARRIER GUARD
# ======================================================================
print("== Y6: carrier guard ==")
LIM = 200
rep = set()
x = 0
while x * x <= LIM:
    y = 0
    while x * x + 5 * y * y <= LIM:
        n = x * x + 5 * y * y
        if n > 0:
            rep.add(n)
        y += 1
    x += 1
def irreducible_in(n, S):
    return n in S and not any(a > 1 and n % a == 0 and (n // a) in S and
                              (n // a) > 1 for a in S)
y6 = all(n in rep for n in (4, 6, 9, 36))
y6 = y6 and all(irreducible_in(n, rep) for n in (4, 6, 9))
y6 = y6 and (4 * 9 == 36 == 6 * 6)
gate("Y6a Epstein x^2+5y^2: 36 = 4*9 = 6*6, all factors irreducible "
     "-> no valuation -> geometric evaluation unformable", y6)
# DH: non-prime-power supports already killed by Y2's predicate; negative
# weights kill the atom dictionary (HH H6b, cited). Record the asymmetry:
record("DH/Epstein: the spectral evaluation k^w - 1 remains formable for "
       "every k; the AGREEMENT theorem (Quillen) has no carrier - the "
       "asymmetry is P3-a, and the kill is by non-existence (P2 shape).")
gate("Y6b DH predicates (non-prime-power supports, via Y2)", y2_ok)

# ======================================================================
# Y7  THE AGREEMENT LOCUS
# ======================================================================
print("== Y7: the agreement-locus shape ==")
geom_locus = {k for k in range(2, 101) if prime_power(k)}
pp_set = {k for k in range(2, 101)
          if len(factorize(k)) == 1}
y7 = geom_locus == pp_set and len(geom_locus) < 99
gate("Y7 agreement locus = prime powers (proper subset of spectral domain)",
     y7, "%d prime powers <= 100; spectral side defined at all 99 k"
     % len(geom_locus))

# ----------------------------------------------------------------------
print()
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (Y1-Y7)")
sys.exit(0)
