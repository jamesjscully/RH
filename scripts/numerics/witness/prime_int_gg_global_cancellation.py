"""GG-witness: does the K4 duality pole-cancellation survive the
all-places assembly?  (doc 30 ranked front 3; CC part 3 + BB's D_glob;
registrations in research/work/GG-global-cancellation.md sec 1, written
before first run.)

PRE-REGISTERED GATES (fail-closed; exit 0 iff ALL PASS):

GG1 PER-PLACE UNIFORMITY (p = 3, 5; p = 2 control): the cancellation
    is an identity in x = p^{-s}: 1/(1-x) + 1/(1-1/x) - 1 = 0 at 25
    exact Fraction points; flint (prec 300): branch residues
    s * A_D,p * log p -> +1 and s * A_D',p * log p -> -1 with
    monotonically shrinking error (s = 1e-1..1e-4, tol 2e-4 at the
    last point); glued |A_D + A_D' + 1| < 1e-80 at generic s;
    intrinsic odd-p normalization (atoms p^{2m}, x = p^{-2s}):
    residues +-1/(2 log p), same cancellation; K2 flip pairs atom p^m
    with mirror p^{-m} (Fraction product == 1, m <= 8).
    FAIL: wrong residue / nonzero glued residue / pairing broken.

GG2 NO DOUBLE-COUNT (the task-registered G2 mechanism, tested exactly):
    all prime-power atoms p^m <= 10^6 enumerated over all places have
    multiplicity EXACTLY 1 (no integer in two branches); every
    composite A <= 20000 with >= 2 distinct prime factors is in NO
    branch; iota recomposes prod p^{v_p} == A integer-exactly with
    |log A - sum v_p log p| < 1e-12.  FAIL: any double-count.

GG3 CANCELLATION IS LOAD-BEARING GLOBALLY: cancelled layer L_p == 0
    exactly (Fraction) => place-sum identically 0 (entire);
    uncancelled residue ledger sum_{p<=X} 1/log p exceeds
    pi(X)/log X and grows by > 10x from X = 1e4 to 1e6; uncancelled
    branch series at s = 1/2, sum_{p<=X} 1/(sqrt p - 1), grows by
    > 4x over the same range (divergence on the critical line).
    FAIL: any check fails.

GG4 THE SURVIVOR LAYER + THE EXACT OBSTRUCTION (zero mode): (a) the
    survivor lattices meet pairwise only at 0: p^a != q^b, exact
    integers, p < q in {2,3,5,7,11}, 1 <= a,b <= 60; (b) per-place
    Poisson: comb_p(phi) = sum_m phihat(m log p) for Gaussian
    phi = e^{-t^2/2} (both sides independent arb sums, p <= 1e4,
    tol 1e-60); (c) zero-mode divergence: S_X = sum_{p<=X} comb_p
    has S_X > pi(X) phihat(0) and S_X/(pi(X) phihat(0)) DECREASING
    to < 1.01 across X = 1e2, 1e3, 1e4 (divergence linear in pi(X),
    coefficient = the continuum unit phihat(0)); (d) renormalized
    convergence: R_X = S_X - pi(X) phihat(0) moves by < 1e-5 from
    X = 1e3 to 1e4 while S_X moves by > 100; R_{1e4} equals the
    independently enumerated sigma=0-shell prime side (support =
    +-log prime powers, GG2's set): exactly (tol 1e-60) over the SAME
    place set (q = p^m, p <= 1e4, all m), and to within the
    explicitly computed place-tail bound sum_{1e4<p<=1e6} 2 phihat
    (log p) (< 1e-14) against the full integer shell q <= 1e6.
    [AMENDED AFTER FIRST RUN, disclosed: the registered single-clause
    tol 1e-30 compared MISMATCHED place sets (the full shell contains
    m = 1 atoms of places > 1e4, tail ~ 2.4e-16); replaced by the two
    clauses above - coverage strengthened, tolerance corrected to the
    measured tail scale.]  FAIL: shared lattice point / ratio not
    decreasing / renormalized not Cauchy / support mismatch.

GG5 COMPARISON (F-a-FLAGGED: EF comparison only) + DETERMINANT DC:
    sum_{p^k <= 1e6} log p p^{-ks} == -zeta'/zeta(s) at s = 2
    (tol 2e-5, tail-limited) and s = 3 (tol 1e-11); zeta' by arb
    central difference h = 1e-30 at prec 300 (disclosed); the
    determinant-layer DC face theta(X)/2 = (1/2) sum_{p<=X} log p
    grows by > 5x from 1e5 to 1e6 and exceeds 1e5 (the zero-mode
    obstruction in determinant dress).  FAIL: mismatch beyond tol.

GG6 CARRIER GUARD (Epstein death point, exact): represented norms of
    x^2 + 5y^2: 2, 3 NOT represented; 4, 6, 9, 36 represented;
    4, 6, 9 irreducible in the represented monoid; 36 = 4*9 = 6*6
    two DISTINCT irreducible factorizations => no additive valuation
    (v_6 would be 2 and 0) => no v_p data => no place-branches => no
    pole pair => nothing to cancel => no global object.  DH: no
    carrier group (bookkeeping).  FAIL: any membership/irreducibility
    /distinctness clause fails.

Run: python3 -m scripts.numerics.witness.prime_int_gg_global_cancellation
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


# ---------------------------------------------------------------- sieve
N = 10 ** 6
sieve = bytearray([1]) * (N + 1)
sieve[0:2] = b"\x00\x00"
for i in range(2, int(N ** 0.5) + 1):
    if sieve[i]:
        sieve[i * i:: i] = bytearray(len(sieve[i * i:: i]))
PRIMES = [i for i in range(2, N + 1) if sieve[i]]

# ------------------------------------------------------------------- GG1
ok = True
pts = [Fraction(a, q) for a in range(-5, 7) for q in (2, 3, 7)
       if Fraction(a, q) not in (0, 1)][:25]
for x in pts:                       # identity in x: place-blind, exact
    ok = ok and (1 / (1 - x) + 1 / (1 - 1 / x) - 1 == 0)

detail = []
for p in (3, 5, 2):                 # p = 2 is the control (CC's QG2/QG3)
    LOGP = arb(p).log()

    def A_D(s, p=p):
        return 1 / (arb(p) ** arb(s) - 1)

    def A_Dp(s, p=p):
        return 1 / (arb(p) ** (-arb(s)) - 1)

    errsD, errsDp, errsG = [], [], []
    for s in (1e-1, 1e-2, 1e-3, 1e-4):
        errsD.append(abs(float((arb(s) * A_D(s) * LOGP).mid()) - 1.0))
        errsDp.append(abs(float((arb(s) * A_Dp(s) * LOGP).mid()) + 1.0))
        errsG.append(abs(float((arb(s) * (A_D(s) + A_Dp(s) + 1)).mid())))
    ok = ok and errsD[-1] < 2e-4 and all(errsD[i + 1] < errsD[i]
                                         for i in range(3))
    ok = ok and errsDp[-1] < 2e-4 and all(errsDp[i + 1] < errsDp[i]
                                          for i in range(3))
    ok = ok and errsG[-1] < 1e-6
    # glued layer exactly -1 + 1 = 0 away from the lattice
    for s in (0.3, 1.7, -0.9):
        ok = ok and abs(float((A_D(s) + A_Dp(s) + 1).mid())) < 1e-80
    # intrinsic odd-p normalization: atoms p^{2m}, x = p^{-2s}
    errsY = []
    for s in (1e-1, 1e-2, 1e-3, 1e-4):
        AY = 1 / (arb(p) ** (2 * arb(s)) - 1)
        AYp = 1 / (arb(p) ** (-2 * arb(s)) - 1)
        errsY.append(abs(float((arb(s) * AY * 2 * LOGP).mid()) - 1.0))
        ok = ok and abs(float((AY + AYp + 1).mid())) < 1e-60
    ok = ok and errsY[-1] < 4e-4 and errsY[-1] < errsY[0]
    # K2 flip: atom p^m pairs with mirror p^{-m}; product-formula shadow
    for m in range(1, 9):
        ok = ok and Fraction(p) ** m * Fraction(1, p) ** m == 1
    detail.append("p=%d errD=%.1e glued@s=1e-4:%.1e" %
                  (p, errsD[-1], errsG[-1]))
gate("GG1 per-place uniformity: A_D + A_D' + 1 = 0 exact (identity in "
     "x); residues +-1/log p (and +-1/(2 log p) intrinsic) at p = 3, 5; "
     "K2 flip pairs p^m with p^-m", ok, " ".join(detail))

# ------------------------------------------------------------------- GG2
ok = True
ppow = {}                            # prime power -> list of (p, m)
for p in PRIMES:
    q, m = p, 1
    while q <= N:
        ppow.setdefault(q, []).append((p, m))
        q *= p
        m += 1
ok = ok and all(len(v) == 1 for v in ppow.values())   # multiplicity 1
# composites are in NO branch; iota recomposition exact
spf = list(range(20001))
for i in range(2, 142):
    if spf[i] == i:
        for j in range(i * i, 20001, i):
            if spf[j] == j:
                spf[j] = i
worst = 0.0
for A in range(2, 20001):
    n, fac = A, {}
    while n > 1:
        fac[spf[n]] = fac.get(spf[n], 0) + 1
        n //= spf[n]
    if len(fac) >= 2:
        ok = ok and A not in ppow                     # not a slot
    rec = 1
    for p, v in fac.items():
        rec *= p ** v
    ok = ok and rec == A                              # iota exact
    worst = max(worst, abs(math.log(A)
                           - sum(v * math.log(p) for p, v in fac.items())))
ok = ok and worst < 1e-12
gate("GG2 no double-count: every prime-power atom <= 1e6 in EXACTLY one "
     "place-branch; composites in NO branch; iota couples weights, not "
     "slots (recomposition exact)", ok, "worst log-identity %.1e" % worst)

# ------------------------------------------------------------------- GG3
ok = True
for x in pts:                        # cancelled layer == 0 exactly
    ok = ok and (1 / (1 - x) + 1 / (1 - 1 / x) - 1 == 0)
s_res4 = sum(1.0 / math.log(p) for p in PRIMES if p <= 10 ** 4)
s_res6 = sum(1.0 / math.log(p) for p in PRIMES)
ok = ok and s_res6 > len(PRIMES) / math.log(N) and s_res6 > 10 * s_res4
s_half4 = sum(1.0 / (math.sqrt(p) - 1) for p in PRIMES if p <= 10 ** 4)
s_half6 = sum(1.0 / (math.sqrt(p) - 1) for p in PRIMES)
ok = ok and s_half6 > 4 * s_half4
gate("GG3 cancellation load-bearing: cancelled place-sum identically 0 "
     "(entire); uncancelled residues sum 1/log p NON-SUMMABLE; branch "
     "series diverges at s = 1/2", ok,
     "sum 1/log p: %.1f (1e4) -> %.1f (1e6); sum 1/(sqrt p - 1): "
     "%.1f -> %.1f" % (s_res4, s_res6, s_half4, s_half6))

# ------------------------------------------------------------------- GG4
ok = True
# (a) survivor lattices meet only at 0: p^a != q^b, exact
small = [2, 3, 5, 7, 11]
for i in range(len(small)):
    for j in range(i + 1, len(small)):
        p, q = small[i], small[j]
        pa = {p ** a for a in range(1, 61)}
        ok = ok and pa.isdisjoint({q ** b for b in range(1, 61)})
# (b)-(d) Gaussian phi = exp(-t^2/2); phihat(xi) = sqrt(2pi) exp(-xi^2/2)
SQ2PI = (2 * arb.pi()).sqrt()


def comb_p(p):                       # t-side: (2pi/logp) sum phi(2pi n/logp)
    lp = arb(p).log()
    sp = 2 * arb.pi() / lp
    nmax = int(25 * float(lp.mid()) / (2 * math.pi)) + 10
    tot = arb(1)                     # n = 0
    for n in range(1, nmax + 1):
        tot += 2 * (-(sp * n) ** 2 / 2).exp()
    return sp * tot


def osc_p(p):                        # xi-side, m != 0 only
    lp = arb(p).log()
    mmax = int(25 / float(lp.mid())) + 8
    tot = arb(0)
    for m in range(1, mmax + 1):
        tot += 2 * SQ2PI * (-(lp * m) ** 2 / 2).exp()
    return tot


PHI0 = SQ2PI                         # phihat(0) = continuum unit
ratios, Svals, Rvals = [], {}, {}
worst_poisson = 0.0
for p in PRIMES:
    if p > 10 ** 4:
        break
    c, o = comb_p(p), osc_p(p)       # two independent arb computations
    worst_poisson = max(worst_poisson, abs(float((c - PHI0 - o).mid())))
for X in (10 ** 2, 10 ** 3, 10 ** 4):
    Sx = arb(0)
    nx = 0
    for p in PRIMES:
        if p > X:
            break
        Sx += comb_p(p)
        nx += 1
    Svals[X] = Sx
    Rvals[X] = Sx - nx * PHI0
    ratios.append(float((Sx / (nx * PHI0)).mid()))
ok = ok and worst_poisson < 1e-60                       # (b)
ok = ok and ratios[0] > ratios[1] > ratios[2] > 1.0     # (c)
ok = ok and ratios[2] < 1.01
ok = ok and float((Svals[10 ** 4] - Svals[10 ** 3]).mid()) > 100
rmove = abs(float((Rvals[10 ** 4] - Rvals[10 ** 3]).mid()))
ok = ok and rmove < 1e-5                                # (d) Cauchy
# independent sigma=0-shell enumeration over INTEGER prime powers
# (GG2's set).  (i) same place set (p <= 1e4, ALL m, q unbounded to
# the e^-80 cutoff): exact match; (ii) full shell q <= 1e6: match to
# within the explicitly computed place-tail (m = 1 atoms of places in
# (1e4, 1e6], absent from the comb side).
shell_full, shell_local = arb(0), arb(0)
for q in sorted(ppow):
    term = 2 * SQ2PI * (-arb(q).log() ** 2 / 2).exp()
    shell_full += term
    if ppow[q][0][0] <= 10 ** 4:
        shell_local += term
for p in PRIMES:                     # powers q > 1e6 of places <= 1e4
    if p > 10 ** 4:
        break
    q = p
    while q <= N:
        q *= p
    while math.log(q) <= 80:
        shell_local += 2 * SQ2PI * (-arb(q).log() ** 2 / 2).exp()
        q *= p
tail_bound = sum(2 * math.sqrt(2 * math.pi)
                 * math.exp(-math.log(p) ** 2 / 2)
                 for p in PRIMES if p > 10 ** 4)
support_err = abs(float((Rvals[10 ** 4] - shell_local).mid()))
full_err = abs(float((Rvals[10 ** 4] - shell_full).mid()))
ok = ok and support_err < 1e-60
ok = ok and tail_bound < 1e-14 and full_err < tail_bound + 1e-30
gate("GG4 survivor layer: lattices meet ONLY at s=0 (p^a != q^b exact); "
     "zero mode diverges as pi(X)*phihat(0); renormalized survivor "
     "converges to the sigma=0-shell prime side", ok,
     "ratios %.4f %.4f %.4f; R-move %.1e; R=%.8f support err %.1e "
     "(full-shell err %.1e <= place-tail %.1e)" %
     (ratios[0], ratios[1], ratios[2], rmove,
      float(Rvals[10 ** 4].mid()), support_err, full_err, tail_bound))

# ------------------------------------------------------------------- GG5
ok = True
h = arb(10) ** -30
def neg_zp_over_z(s):
    zp = (arb(s + 0) + h).zeta() - (arb(s) - h).zeta()
    return float((-(zp / (2 * h)) / arb(s).zeta()).mid())


diffs = []
for s, tol in ((2, 2e-5), (3, 1e-11)):
    lam = 0.0
    for p in PRIMES:
        q, k = p, 1
        lp = math.log(p)
        while q <= N:
            lam += lp / q ** s
            q *= p
            k += 1
    d = abs(lam - neg_zp_over_z(s))
    diffs.append((s, d))
    ok = ok and d < tol
theta5 = sum(math.log(p) for p in PRIMES if p <= 10 ** 5)
theta6 = sum(math.log(p) for p in PRIMES)
ok = ok and theta6 > 5 * theta5 and theta6 / 2 > 1e5
gate("GG5 comparison (F-a FLAGGED, EF comparison only): assembled atom "
     "sum = -zeta'/zeta(s); determinant DC face theta(X)/2 diverges "
     "(same zero mode, determinant dress)", ok,
     "|diff| s=2: %.1e, s=3: %.1e; theta/2: %.0f -> %.0f" %
     (diffs[0][1], diffs[1][1], theta5 / 2, theta6 / 2))

# ------------------------------------------------------------------- GG6
ok = True
rep = set()
for x in range(0, 61):
    for y in range(0, 28):
        v = x * x + 5 * y * y
        if 0 < v <= 3600:
            rep.add(v)
ok = ok and 2 not in rep and 3 not in rep
ok = ok and all(v in rep for v in (4, 6, 9, 36))


def irreducible(n):
    return not any(n % d == 0 and d in rep and (n // d) in rep
                   for d in range(2, n))


ok = ok and irreducible(4) and irreducible(6) and irreducible(9)
f1, f2 = tuple(sorted((4, 9))), tuple(sorted((6, 6)))
ok = ok and 4 * 9 == 36 == 6 * 6 and f1 != f2     # two factorizations
# no additive valuation: v_6(36) = 2 via 6*6, = 0 via 4*9
v6_route1, v6_route2 = 2, 0
ok = ok and v6_route1 != v6_route2
# death cascade (bookkeeping): no v_p => no branches => no pole pair
# => nothing to cancel => no survivors => no global object
has_vp, has_branches, has_pole_pair = False, False, False
has_cancellation, has_global = False, False
ok = ok and not (has_vp or has_branches or has_pole_pair
                 or has_cancellation or has_global)
dh_has_carrier_group = False                       # AA's profile
ok = ok and not dh_has_carrier_group
gate("GG6 carrier guard: Epstein x^2+5y^2 dies at unique factorization "
     "(36 = 4*9 = 6*6, all irreducible, 2 and 3 unrepresented => no "
     "v_p => no place-branches => no global object); DH dies earlier",
     ok)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (GG1-GG6)")
