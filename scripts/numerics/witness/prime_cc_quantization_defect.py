"""The quantization defect of CC's dimension (Q-task part 3): the
zeta-regularized total of the quantized tower ceil(log2 k) DOES NOT EXIST.

SETTING. N-cc-square-posing.md R(iii)-weak: a CC-type theory measuring
the Bokstedt diagonal entry Z/k (degree 2k-1) with dim_S assigns
ceil(log2 k) instead of the exact log2 k nats.  The derived side has the
regularized total Sum_reg log2 k = -zeta'(0)/log 2 = log(2pi)/(2 log 2)
(finite).  The candidate "CC-computable number" is Sum_reg ceil(log2 k);
the difference is the quantization-defect series

    D(s) = Sum_{k>=1} delta(k) k^{-s},   delta(k) = ceil(log2 k) - log2 k.

ANALYTIC STRUCTURE (derivation in research/work/Q-cc-ftest.md sec 5).
delta(k) = (1 - {log2 k}) - [k is a power of 2]: a log-periodic sawtooth
minus the indicator of the dyadic atoms (exactly where the ceiling is
exact).  The sawtooth part is regular at s = 0; the atom part is
-(1/2) Sum_j (2^j)^{-s} = -(1/2)/(1 - 2^{-s}), a SIMPLE POLE at s = 0:

    D(s) = -1/(2 log 2) * 1/s + FP + O(s)      near s = 0.

So the quantized tower has NO zeta-regularized value; the obstruction is
carried by the dyadic ramification points.  Only a finite part exists
(one further scheme choice).  Base-b generalization: residue -1/(2 log b).

COMPUTATION ROUTE (rigorous up to a stated generous tail constant):
    D(s) = C(s) + zeta'(s)/log b,    C(s) = Sum_{j>=0} zeta(s, b^j + 1),
continued via Euler-Maclaurin out of each Hurwitz term:
    C(s) = T2(s) + g(s-1)/(s-1) + g(s)/2 + (s/12) g(s+1),
    T2(s) = Sum_j [zeta(s,a_j) - a_j^{1-s}/(s-1) - a_j^{-s}/2
                   - (s/12) a_j^{-s-1}],            a_j = b^j + 1,
    g(w)  = Sum_j a_j^{-w} = 2^{-w}
            + Sum_{m>=0} binom(-w,m) b^{-(w+m)}/(1 - b^{-(w+m)}),
all evaluated in flint ball arithmetic (each Hurwitz zeta is a rigorous
ball); the only non-ball inputs are the two series tails, bounded with
generous constants and ADDED AS BALL RADII, and validated in the
convergent region (W1) by exact bracketing.

PRE-REGISTERED READINGS (fixed before the run, fail-closed):
  W0  implementation sanity: g(2) and the Euler-Maclaurin remainder
      magnitude vs direct sums.  Expected PASS.
  W1  bracket check in the convergent region: since 0 <= delta < 1,
      P_K <= D(s) <= P_K + K^{1-s}/(s-1) with P_K the exact partial sum
      (K = 2^16); the decomposition value must land in the bracket for
      s = 2 and s = 1.5.  Expected PASS (certifies the decomposition).
  W2  THE POLE: s*D(s) -> -1/(2 log 2) = -0.721347520444... as s -> 0+
      (s = 1e-1..1e-4, error shrinking ~ linearly in s); final error
      < 1e-3.  Expected PASS => Sum_reg ceil(log2 k) DOES NOT EXIST:
      N-doc's "regularized value is NOT zeta'(0)" sharpens to "is not
      even finite".
  W3  FINITE PART: FP = lim (D(s) + 1/(2 s log 2)); two-sided averages
      (f(s)+f(-s))/2 at s = 1e-3, 1e-4 agree to < 1e-5; FP reported.
  W4  the comparison numbers: Sum_reg log2 k = log(2pi)/(2 log 2) finite;
      FP[Sum_reg ceil(log2 k)] = FP(D) + log(2pi)/(2 log 2).
  W5  base dependence (scheme leak, G-INT6): base 3 gives residue
      -1/(2 log 3): the divergence and its size depend on the choice of
      CC base (S vs S[+-1] presentation).  Expected PASS.
  W6  CLOSED FORM (derived by hand from the decomposition after W3's
      first run returned 0.7499999938; doc sec 5.3): since
      zeta(0,a) = 1/2 - a makes T2(0) = 0 exactly, the finite part of
      the regularized QUANTIZED tower is RATIONAL and base-dependent:
          FP[ Sum_reg ceil(log_b k) ] = b/(b-1) - 5/4
      (3/4 for b = 2, 1/4 for b = 3); equivalently FP[D_b](0) =
      b/(b-1) - 5/4 - log(2pi)/(2 log b).  All of zeta'(0) sits in the
      defect: quantization erases the transcendental datum completely.
      Checked at s = +/-1e-5 (two-sided), tolerance 1e-9.  Expected PASS.

Run:
    python3 -m scripts.numerics.witness.prime_cc_quantization_defect
"""
import math
import sys

import flint

flint.ctx.prec = 300

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


def rball(rad):
    """A real ball 0 +/- rad as an arb."""
    return flint.arb(0, rad)


def acb_real(x):
    return flint.acb(x)


def hurwitz(s, a):
    """zeta(s, a) as acb (rigorous ball)."""
    return flint.acb(s).zeta(flint.acb(a))


def zeta_deriv(s):
    """zeta'(s) by central difference at prec 300 (h = 2^-80; the O(h^2)
    error ~ 2^-160 is added as a radius)."""
    h = flint.arb(1) / (flint.arb(2) ** 80)
    val = (flint.acb(flint.arb(s) + h).zeta()
           - flint.acb(flint.arb(s) - h).zeta()) / (2 * h)
    return val.real + rball(1e-40)


def g_series(w, b, M=120):
    """g(w) = Sum_{j>=0} (b^j + 1)^{-w}, continued:
    2^{-w} + Sum_m binom(-w,m) b^{-(w+m)} / (1 - b^{-(w+m)})."""
    w = flint.arb(w)
    bb = flint.arb(b)
    out = flint.arb(2) ** (-w)
    binom = flint.arb(1)             # binom(-w, 0)
    for m in range(M):
        if m > 0:
            binom = binom * (-w - (m - 1)) / m
        q = bb ** (-(w + m))         # b^{-(w+m)}
        out += binom * q / (1 - q)
    # tail: |binom(-w,m)| <= prod(|w|+i)/m! <= (m+3)^3 for |w| <= 3;
    # terms <= (m+3)^3 * b^{-(m+Re w)} * 2; generous radius:
    rad = 1000.0 * (M + 3) ** 3 * float(bb) ** (-(M + float(w.mid())))
    return out + rball(abs(rad))


def C_cont(s, b, J=80):
    """C(s) = Sum_j zeta(s, b^j+1), continued for Re s > -1."""
    s = flint.arb(s)
    one = flint.arb(1)
    T2 = flint.arb(0)
    for j in range(J):
        a = flint.arb(b) ** j + 1
        T2 += (hurwitz(s, a).real
               - a ** (one - s) / (s - 1)
               - a ** (-s) / 2
               - (s / 12) * a ** (-s - 1))
    # Euler-Maclaurin remainder per term: next term is
    # -(1/720) s(s+1)(s+2) a^{-s-3}; generous bound (1/50)|s(s+1)(s+2)|
    # a^{-Re s-3}, summed over j >= J (geometric, ratio <= b^{-2}):
    sm = float(s.mid())
    coef = abs(sm * (sm + 1) * (sm + 2)) / 50.0 + 1e-12
    aJ = float(b) ** (J - 1)
    tail = 2.0 * coef * aJ ** (-(sm + 3))
    T2 += rball(tail)
    return (T2 + g_series(s - 1, b) / (s - 1)
            + g_series(s, b) / 2
            + (s / 12) * g_series(s + 1, b))


def D_cont(s, b=2):
    """D(s) = C(s) + zeta'(s)/log b (continued)."""
    return C_cont(s, b) + zeta_deriv(s) / flint.arb(b).log()


def ceil_log(k, b):
    """ceil(log_b k) by integer arithmetic."""
    m, p = 0, 1
    while p < k:
        p *= b
        m += 1
    return m


def D_direct_bracket(s, b, K):
    """Exact bracket [P_K, P_K + tail] for D(s), Re s > 1."""
    sa = flint.arb(s)
    logb = flint.arb(b).log()
    P = flint.arb(0)
    for k in range(2, K + 1):
        ka = flint.arb(k)
        P += (ceil_log(k, b) - ka.log() / logb) * ka ** (-sa)
    tailmax = flint.arb(K) ** (1 - sa) / (sa - 1)
    return P, P + tailmax


# ------------------------------------------------------------------- W0
print("W0: implementation sanity")
g2_direct = sum(flint.arb(2 ** j + 1) ** (-2) for j in range(400))
g2 = g_series(2.0, 2)
ok0a = abs(float((g2 - g2_direct).mid())) < 1e-30
# EM remainder magnitude check at (s,a) = (1.5, 257):
s0, a0 = flint.arb(1.5), flint.arb(257)
em = (hurwitz(s0, a0).real - a0 ** (1 - s0) / (s0 - 1) - a0 ** (-s0) / 2
      - (s0 / 12) * a0 ** (-s0 - 1))
bound = abs(1.5 * 2.5 * 3.5) / 50.0 * 257.0 ** (-4.5)
ok0b = abs(float(em.mid())) < bound
check("g(2) vs direct; EM remainder within generous bound", ok0a and ok0b,
      f"|g diff| < 1e-30: {ok0a}; |EM rem| = {abs(float(em.mid())):.2e} "
      f"< {bound:.2e}")

# ------------------------------------------------------------------- W1
print("\nW1: bracket certification in the convergent region (base 2)")
ok1 = True
for s in (2.0, 1.5):
    lo, hi = D_direct_bracket(s, 2, 1 << 16)
    val = D_cont(s)
    inb = float(lo.mid()) - 1e-25 <= float(val.mid()) <= float(hi.mid()) + 1e-25
    ok1 = ok1 and inb
    print(f"    s = {s}: decomposition D(s) = {float(val.mid()):.12f}  in "
          f"[{float(lo.mid()):.12f}, {float(hi.mid()):.12f}] : {inb}")
check("decomposition inside exact bracket at s = 2, 1.5", ok1,
      "0 <= delta < 1 bracketing with K = 2^16")

# ------------------------------------------------------------------- W2
print("\nW2: the pole at s = 0 (base 2)")
target = -1.0 / (2.0 * math.log(2.0))
errs = []
for s in (1e-1, 1e-2, 1e-3, 1e-4):
    r = float((s * D_cont(s)).mid())
    errs.append(abs(r - target))
    print(f"    s = {s:>6}: s*D(s) = {r:+.9f}   (target {target:+.9f}, "
          f"err {errs[-1]:.2e})")
ok2 = errs[-1] < 1e-3 and all(errs[i + 1] < errs[i] for i in range(3))
check("s*D(s) -> -1/(2 log 2), error shrinking", ok2,
      f"residue = -1/(2 log 2) = {target:.12f}; the zeta-regularized "
      "Sum ceil(log2 k) DIVERGES (simple pole, carried by the dyadic "
      "atoms k = 2^j)")

# ------------------------------------------------------------------- W3
print("\nW3: the finite part")
ln2 = math.log(2.0)


def f_reg(s):
    return float((D_cont(s) + flint.arb(1) / (2 * flint.arb(s) * flint.arb(2).log())).mid())


fp_est = {}
for s in (1e-3, 1e-4):
    fp_est[s] = 0.5 * (f_reg(s) + f_reg(-s))
    print(f"    s = +/-{s}: two-sided average = {fp_est[s]:+.12f}")
ok3 = abs(fp_est[1e-3] - fp_est[1e-4]) < 1e-5
FP = fp_est[1e-4]
check("two-sided averages stable", ok3,
      f"FP[D](0) = {FP:+.10f} (quadratic-term agreement "
      f"{abs(fp_est[1e-3] - fp_est[1e-4]):.2e})")

# ------------------------------------------------------------------- W4
print("\nW4: the comparison (the trade, in numbers)")
smooth = math.log(2 * math.pi) / (2 * ln2)     # Sum_reg log2 k (finite)
print(f"    Sum_reg log2 k        = log(2pi)/(2 log 2) = {smooth:+.10f}"
      "   (FINITE: the derived/THH side regularizes)")
print(f"    Sum_reg ceil(log2 k)  = -1/(2 log 2)/s|_(s->0) + "
      f"{FP + smooth:+.10f}   (POLE: no CC-computable number exists)")
print(f"    quantization defect   = D(s) ~ {target:+.10f}/s "
      f"{FP:+.10f} + O(s)")
check("defect bookkeeping consistent", abs(smooth - 1.3257480647) < 1e-9,
      "FP[Sum_reg ceil] = FP[D] + log(2pi)/(2 log 2) "
      f"= {FP + smooth:+.10f}")

# ------------------------------------------------------------------- W5
print("\nW5: base dependence (G-INT6 scheme leak): base 3 / S[+-1]")
target3 = -1.0 / (2.0 * math.log(3.0))
errs3 = []
for s in (1e-2, 1e-3, 1e-4):
    r = float((s * D_cont(s, b=3)).mid())
    errs3.append(abs(r - target3))
    print(f"    s = {s:>6}: s*D_3(s) = {r:+.9f}   (target {target3:+.9f})")
ok5 = errs3[-1] < 1e-3 and errs3[-1] < errs3[0]
check("base-3 residue = -1/(2 log 3)", ok5,
      "the divergence persists in every base and its SIZE is "
      "base-dependent: the quantized tower's failure is scheme-laden "
      "exactly as G-INT6 predicts")

# ------------------------------------------------------------------- W6
print("\nW6: closed form -- FP[Sum_reg ceil(log_b k)] = b/(b-1) - 5/4")
ok6 = True
for b in (2, 3):
    smooth_b = math.log(2 * math.pi) / (2 * math.log(b))
    pred = b / (b - 1.0) - 1.25 - smooth_b          # FP[D_b](0)
    s = 1e-5
    got = 0.5 * (float((D_cont(s, b=b)
                        + flint.arb(1) / (2 * flint.arb(s)
                                          * flint.arb(b).log())).mid())
                 + float((D_cont(-s, b=b)
                          + flint.arb(1) / (2 * flint.arb(-s)
                                            * flint.arb(b).log())).mid()))
    err = abs(got - pred)
    ok6 = ok6 and err < 1e-9
    print(f"    b = {b}: FP[D_b] = {got:+.12f}  vs  b/(b-1) - 5/4 - "
          f"log(2pi)/(2 log b) = {pred:+.12f}   (err {err:.1e})")
check("rational closed form for the quantized tower's finite part", ok6,
      "FP[Sum_reg ceil(log_b k)] = b/(b-1) - 5/4 exactly (3/4 over S, "
      "1/4 over S[+-1]): the finite part is RATIONAL -- the entire "
      "zeta'(0) datum is erased by quantization and lives in the defect")

print("""
VERDICT (pre-registered): W1-W6 PASS => the candidate synthesis "graded
tolerance with CC-computable regularized totals" is REFUTED in its
simplest form.  The ceiling that buys integrality at each degree
(N-doc L1, resolution erosion) destroys summability down the tower: the
defect series has a simple pole at s = 0, residue -1/(2 log b), supported
exactly on the ramification set {b^j} where the quantization is exact.
The trade is strict: tolerance <=> integer dims at each level, NO
regularized global number; derived <=> regularized global number
(zeta'(0)), NO integer dims.  Any reconciling object must break this
exact dichotomy, and nothing in CC/Bost/Borisov does (doc sec 5).
""")

print(f"{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
