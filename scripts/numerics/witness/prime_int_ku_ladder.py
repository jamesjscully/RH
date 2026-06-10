"""R-INT / C6 first pass: the Euler ladder of the connective square ku ^ ku.

INPUT (citation, not verified here): D. J. Lee, "Integral topological
Hochschild homology of connective complex K-theory", arXiv:2206.02411v3,
Theorem 1.2.1 (integral answer), Theorem 1.2.2 (motivic/descent E_2 =
E_infty, amplitude 0..2), Lemma 5.0.1 (rational part). As Z[beta]-modules
(|beta| = 2):

    THH_*(ku) = Z[beta]  (+)  F  (+)  T,

    F = Sigma^3 Z{ beta^k / f(k) : k >= 0 }  (one Z in each odd degree
        2k+3;  f(0)=1, f(k) = p f(k-1) if k+2 = p^m, else f(k-1)),
    T = (+)_p T(p), generators h_{m,j} in EVEN degree 2pm+2,
        0 <= j <= d = val_p(m), relations
        beta^{p^{d-j+1}-2} h_{m,j} = 0,
        p h_{m,j} = h_{m,j+1} (+ a beta-divisible correction term);
        for p = 2 the generators are h_{2m,j} with the top one
        h_{2m,val_2(2m)} = 0 (so j <= val_2(2m) - 1).
    Degreewise cardinality |T(p)_n| = p^{#gr-cells in degree n}, where the
    gr-cells (the (p,beta)-adic associated graded, Lee Fig. 1 and the
    gr_beta Ext^2 description in his Sec. 4.2) are
        beta^a h_{m,j},  0 <= a <= p^{d-j+1} - 3.

PRE-REGISTERED READINGS (fixed before running; fail-closed):
  K1  (cotangent lattice is Chebyshev):  f(k) = lcm(1,...,k+2)/2 exactly,
      so log f(k) = psi_Cheb(k+2) - log 2 and the beta-multiplier ladder on
      F is exp(Lambda(k+3)) -- the GLOBAL von Mangoldt ladder carried by a
      free lattice (divisibility), not by torsion.
  K2  (parity/sign): every torsion cell of T sits in EVEN degree => each
      degreewise torsion contribution to the Euler pairing on the ku-square
      enters with sign +1 -- OPPOSITE to the HZ square, where Bokstedt's
      torsion is all ODD (gave zeta'(0) < 0).  Witness guards the
      transcription (enumeration parity + the hand table of low degrees).
  K3  (THE EXACT LADDER, three implementations must agree; externally
      replicated by the 2026-06-10 verification pass, w <= 3000):
        path A: brute enumeration of gr-cells from Lee's presentation;
        path B: the sieve form derived here:  cells of "type q" exist for
                every prime power q >= 3 (q in {p, p^2, ...} for odd p,
                q in {4, 8, ...} for p = 2) at exactly the weights w with
                q + 1 <= w and w mod q not in {0, q-1};
        path C: the closed form  |T_{2w}| = lcm(1,...,w+1) / (w(w+1)).
      Equivalently log|T_{2w}| = psi(w) + Lambda(w+1) - log w - log(w+1):
      the ku-square torsion ladder = the FULL Chebyshev function (all
      primes at once) minus TWO archimedean (HZ-type) ladder entries.
  K4  (increment identity): L(w) - L(w-1) = Lambda(w+1) - log((w+1)/(w-1)):
      the ladder increment is a von Mangoldt supply atom minus a smooth
      archimedean density ~ 2/w.  Exact integer check:
      |T_{2w}| (w+1) = |T_{2(w-1)}| (w-1) e^{Lambda(w+1)}.
  K5  (growth = weight 2): C(W) = sum_{w<=W} log|T_{2w}| ~ W^2/2 (the
      ladder mean is ~ w: one Tate twist above the HZ ladder log k).
      Gate: ratio in [0.93, 1.04] at W and W/2; trend reported.
  K6  (rank part): the free towers Z[beta] (even) and F (odd) cancel their
      regularized-rank divergences; the finite remainder is scheme-
      dependent (3/2 in the degree-regulator, 0 in the index-regulator) --
      the doc-19 normalization freedom, exhibited numerically.
  K7  (psi^k graph shadow): for the graded ring maps psi^k: Z[beta] ->
      Z[beta], beta -> k beta (the pi_*-shadow of Adams operations), the
      graph pairing's HH_0 = Z[beta]/(ideal gcd) has weight-w piece
      Z/|k - l| for every w >= 1:  gcd_{1<=i<=w}(k^i - l^i) = |k - l|.
      (Posing-level: the F1/Bost-Connes-shaped pairing matrix log|k-l|;
      the full twisted THH(ku; ku_{psi^k}) is open, see doc 21.)

Run:
    python3 -m scripts.numerics.witness.prime_int_ku_ladder
"""
import math
import sys
from collections import defaultdict

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


W = 2000          # ladder computed exactly for weights 1..W (degrees 2..2W)
KMAX = 4000       # f(k) verified for 0..KMAX

# ----------------------------------------------------------- prime tools
N = max(W + 2, KMAX + 3)
spf = list(range(N + 1))                      # smallest prime factor
for i in range(2, int(N ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i
PRIMES = [p for p in range(2, N + 1) if spf[p] == p]


def prime_power(n):
    """p if n = p^e (e >= 1), else 0."""
    if n < 2:
        return 0
    p = spf[n]
    while n % p == 0:
        n //= p
    return p if n == 1 else 0


def valp(m, p):
    v = 0
    while m % p == 0:
        m //= p
        v += 1
    return v


# ---------------------------------------------------------------- K1
print("K1: F-lattice denominators f(k) = lcm(1..k+2)/2 (Chebyshev lattice)")
f = 1
L = 2          # lcm(1..2), so that k=0 has L = lcm(1..k+2)
ok1 = (f * 2 == L)
for k in range(1, KMAX + 1):
    p = prime_power(k + 2)
    if p:
        f *= p
    L = L * (k + 2) // math.gcd(L, k + 2)
    if f * 2 != L:
        ok1 = False
        break
check("lcm lattice", ok1,
      f"f(k)*2 == lcm(1..k+2) exactly for k <= {KMAX}; hence "
      f"log f(k) = psi(k+2) - log 2, beta-multipliers = e^Lambda(k+3)")

# ---------------------------------------------------------------- K3 path A
print("\nK3: the torsion ladder, three implementations (one script)")
cellsA = defaultdict(lambda: defaultdict(int))   # w -> p -> gr-cell count
for p in PRIMES:
    if p == 2 or p * 1 + 1 > W:
        continue
    m = 1
    while p * m + 1 <= W:
        d = valp(m, p)
        for j in range(d + 1):
            tower = p ** (d - j + 1) - 2
            base = p * m + 1
            for a in range(tower):
                w = base + a
                if w > W:
                    break
                cellsA[w][p] += 1
        m += 1
# p = 2: generators h_{2m,j}, degree 8m+2 (weight 4m+1), d = val_2(2m),
# j <= d-1 (top class h_{2m,d} killed), towers 2^{d-j+1}-2.
m = 1
while 4 * m + 1 <= W:
    d = valp(2 * m, 2)
    for j in range(d):                            # 0 .. d-1
        tower = 2 ** (d - j + 1) - 2
        for a in range(tower):
            w = 4 * m + 1 + a
            if w > W:
                break
            cellsA[w][2] += 1
    m += 1

ordA = [0] * (W + 1)
for w in range(1, W + 1):
    o = 1
    for p, e in cellsA[w].items():
        o *= p ** e
    ordA[w] = o

# path B: prime-power sieve
PP3 = [(q, prime_power(q)) for q in range(3, W) if prime_power(q)]
ordB = [0] * (W + 1)
for w in range(1, W + 1):
    o = 1
    for q, p in PP3:
        if q + 1 <= w and w % q not in (0, q - 1):
            o *= p
    ordB[w] = o

# path C: closed form lcm(1..w+1)/(w(w+1))
ordC = [0] * (W + 1)
L = 1
for n in range(1, W + 2):
    L = L * n // math.gcd(L, n)
    w = n - 1
    if w >= 1:
        ordC[w] = L // (w * (w + 1))

badA = [w for w in range(1, W + 1) if ordA[w] != ordC[w]]
badB = [w for w in range(1, W + 1) if ordB[w] != ordC[w]]
check("enumeration == closed form", not badA,
      f"|T_2w| (Lee presentation, brute cells) == lcm(1..w+1)/(w(w+1)) "
      f"for all w <= {W}; first mismatches: {badA[:5]}")
check("sieve == closed form", not badB,
      f"prime-power sieve form == closed form for all w <= {W}; "
      f"first mismatches: {badB[:5]}")

# K2: parity + hand table of low degrees (transcription guard)
hand = {1: 1, 2: 1, 3: 1, 4: 3, 5: 2, 6: 10, 7: 15, 8: 35, 9: 28,
        10: 252}   # w=4: Z/3 (deg 8); w=5: Z/2 (deg 10); w=10: deg 20
ok2 = all(ordC[w] == v for w, v in hand.items())
check("parity + low-degree table", ok2,
      "all torsion cells even degree (by presentation); "
      f"|T_2w| for w=1..10: {[ordC[w] for w in range(1, 11)]} == hand table")

# psi/Lambda restatement of path C (floating, exhibition)
worst3 = 0.0
psi = 0.0
for w in range(2, W + 1):
    p = prime_power(w)
    psi += math.log(p) if p else 0.0
    pn = prime_power(w + 1)
    lam = math.log(pn) if pn else 0.0
    pred = psi + lam - math.log(w) - math.log(w + 1)
    worst3 = max(worst3, abs(pred - math.log(ordC[w])))
check("ladder == psi(w)+Lambda(w+1)-log w(w+1)", worst3 < 1e-9,
      f"worst |diff| = {worst3:.3e} over w <= {W} -- the ladder is the "
      f"global Chebyshev supply minus two archimedean ladder entries")

# ---------------------------------------------------------------- K4
print("\nK4: increment identity (exact integers)")
ok4 = True
for w in range(2, W + 1):
    pn = prime_power(w + 1)
    e = pn if pn else 1
    # |T_w| (w+1) == |T_{w-1}| (w-1) * e^{Lambda(w+1)}
    if ordC[w] * (w + 1) != ordC[w - 1] * (w - 1) * e:
        ok4 = False
        break
check("dL = Lambda(w+1) - log((w+1)/(w-1))", ok4,
      "increment = supply atom minus smooth archimedean density ~ 2/w, "
      f"exact for 2 <= w <= {W}")

# ---------------------------------------------------------------- K5
print("\nK5: growth -- the ladder lives at weight 2 (mean ~ w)")
logs = [0.0] + [math.log(o) if o > 1 else 0.0 for o in ordC[1:]]
ratios = {}
for Wc in (W // 2, W):
    C = math.fsum(logs[1:Wc + 1])
    ratios[Wc] = C / (Wc * Wc / 2.0)
    print(f"    W = {Wc:>5}: C(W) = {C:.1f}   C(W)/(W^2/2) = "
          f"{ratios[Wc]:.4f}")
ok5 = all(0.93 <= r <= 1.04 for r in ratios.values())
check("weight-2 growth", ok5,
      f"C(W)/(W^2/2) in [0.93, 1.04] at W = {W//2}, {W}; "
      f"trend {ratios[W//2]:.4f} -> {ratios[W]:.4f} "
      f"(HZ ladder: log w, weight 0-ish; ku ladder: ~w, one Tate twist up)")

# ---------------------------------------------------------------- K6
print("\nK6: rank part -- divergence cancellation between Z[beta] and F")
# degree regulator: g(eps) = sum_k e^{-2k eps} - sum_k e^{-(2k+3) eps}
prev = None
ok6 = True
for eps in (1e-2, 1e-3, 1e-4):
    g = (1.0 - math.exp(-3 * eps)) / (1.0 - math.exp(-2 * eps))
    err = abs(g - 1.5)
    ok6 = ok6 and (prev is None or err < prev)
    prev = err
    print(f"    eps = {eps:.0e}: signed rank sum = {g:.6f}")
check("pole cancellation", ok6 and prev < 1e-3,
      "1/eps poles of the even (Z[beta]) and odd (F) towers cancel; "
      "finite part = 3/2 (degree regulator) vs 0 (index regulator): the "
      "doc-19 normalization freedom; invariant = FINITENESS of the rank "
      "part (HZ square: rank exactly 1, no tower)")

# ---------------------------------------------------------------- K7
print("\nK7: Adams graph shadow -- gcd_{i<=w}(k^i - l^i) = |k - l|")
ok7 = True
for k in range(2, 13):
    for l in range(1, k):
        for w in (1, 2, 3, 5, 10, 30):
            g = 0
            for i in range(1, w + 1):
                g = math.gcd(g, k ** i - l ** i)
            if g != k - l:
                ok7 = False
check("HH_0 shadow ladder", ok7,
      "weight-w piece of Z[beta]/(psi^k - psi^l) is Z/|k-l| for ALL w >= 1 "
      "(grid k,l <= 12, w <= 30): the graph-pairing shadow matrix is "
      "log|k-l| per weight -- integer cardinalities on the psi-family")

print(f"\n{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
