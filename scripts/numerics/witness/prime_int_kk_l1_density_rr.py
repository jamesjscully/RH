"""KK-witness: Lemma L1 (density-RR) at theorem grade -- every proof-internal
estimate gated with the PROOF'S OWN explicit constants.

Companion: research/work/KK-L1-density-rr.md (theorem + complete proof).
Lineage: JJ AJ5/AJ6 (prime_int_jj_archimedean_unit.py, ALL PASS rerun
2026-06-10 by KK before this file was written).  Exit 0 iff ALL gates pass.
Fail-closed.  No RH / zeta / zero-side input anywhere; the proof inputs are
unique factorization at finitely many primes + second-order Euler-Maclaurin
+ geometric series, and every constant below is the one DERIVED in the doc,
not fitted.  (Design-stage calibration runs are disclosed in the doc sec 7;
no gate was amended after the first run of THIS file.)

Notation (doc sec 1): twist m: finitely many m_p <= -1 at places P, J=|P|,
d_p = 1 - m_p >= 2; comb S_m = {n>=1 : d_p | v_p(n)}; rho = prod_p rho_p,
rho_p = (1-1/p)/(1-p^-d_p); h0(a) = log(1 + 2 sum_{n in S} e^{-pi n^2 e^-2a});
chi(a) = h0(a) - h0(-a).  Proof constants: c = prod(1-1/p), sigma = prod(1+p),
r = prod p, L(a) = 1 + a/log 4, B_1 = 4/3, B_J = (4/3)(1+B_{J-1}),
C_T = (2 pi/9) sigma + (1.01 2^J e^-pi + c/2) B_J,
E_T(x) = c B_J L4(x)^{J-1} + 2^J L4(x)^J,  L4(x) = 1 + log x/log 4.

PRE-REGISTERED GATES (predicates fixed before first run):

KL0 CONTINUITY WITH JJ: c_T(8) for T2/T3/T23 matches JJ's recorded AJ5b
    values (-0.405205 / -0.287391 / -0.692608) to 1e-5.

KL1 EULER-MACLAURIN UNIT ESTIMATE (Lemma KK.2): psi(s) := theta(s) - 1/(2s)
    + 1/2 satisfies |psi(s)| <= pi s/6 on s in [0.01, 4] step 0.01 (proved
    for ALL s; the s > 4 range is the trivial regime |psi| <= 0.51 + theta(4)
    < pi*4/6, checked once); tail theta(s) <= 1.01 e^{-pi s^2} on [1,3].

KL2 COUNTING LEMMA (Lemma KK.4): for the five combs T2{2:2}, T3{3:2},
    T23{2:2,3:2}, T2d3{2:3}, T235{2:2,3:2,5:2}: |N_S(x) - rho x| <= E_T(x)
    for EVERY integer x in [1, 10^6] (running check during the sieve).

KL3 COMB CONSTANTS (Lemma KK.3): with Q enumerated exactly to 10^8:
    Q(x) <= L4(x)^J;  x*T(x) <= B_J L4(x)^{J-1} where T(x) =
    prod(1-p^-d)^-1 - sum_{q<=x} 1/q;  U(x) = sum_{q<=x} q <=
    (4/3) x L4(x)^{J-1};  at x in {10,10^2,...,10^8}, all five combs.

KL4 MASTER REMAINDER (Lemma KK.5): |theta_S(e^-a) - (rho/2) e^a| <=
    C_T L(a)^{J-1} at a in {2,4,6,8,10}, all five combs.

KL5 THE THEOREM (KK.L1(B)): wherever the precondition u(a) :=
    (1+2 C_T L(a)^{J-1}) e^-a / rho <= 1/2 holds -- registered points:
    T2/T3/T2d3 a in {4,6,8,10}; T23 a in {7,8,9,10}; T235 a in {11,12} --
    |chi(a) - a - log rho| <= (2/rho)(1+2 C_T L(a)^{J-1}) e^-a
                              + 2.02 e^{-pi e^{2a}};
    precondition itself verified at each point; dual bound
    h0(-a) <= 2.02 e^{-pi e^{2a}} checked directly at a in {0.5, 1}.

KL6 EFFECTIVE-CONE TRICHOTOMY (KK.L1(A) + real wall): (a) m_2=+1 (ON the
    real wall): partial sum along A=2^k is (K+1) e^{-pi e^-2a} > 100
    (K=10^4, a=1) -> h0 = +oo; (b) m_2=+2 (beyond wall): terms -> 1,
    partial sum over k<200 at a=0 exceeds 190; (c) REAL-CONE interior
    m_2 in {0.5, 0.9} (real grade, 0 < m < 1): finite, and
    |chi(10) - 10 - log rho_real| <= 1e-3 with rho_real =
    (1/2)/(1-2^{m_2-1}); rho_real(0.99) recorded (wall blow-up).

KL7 COROLLARY C1 (effectivity/integer count): for T2, T23, T2d3:
    N(D) = N_S(e^a) satisfies N >= 1 <=> a >= 0 at a in {-0.5, -0.01, 0,
    0.3, 1, 5, 10}; chi_ren := a + log rho > 0 => N >= 1 (rho <= 1 clause:
    log rho <= 0 checked); |N - rho e^a| <= E_T(e^a) at a in {5, 10};
    |log N - chi_ren| <= 2 E_T(e^a)/(rho e^a) at a = 10 (growth law).

KL8 UNIVERSALITY (Prop KK.8, the Gaussian is not load-bearing for rho):
    quartic unit f(x)=e^{-pi x^4} on T2: |c_f(8) - (log rho + log 2 I_f)|
    <= 2e-3, I_f = Gamma(5/4)/pi^{1/4}; a in {4,6} recorded.

KL9 LOG-PERIODIC COEFFICIENT (Prop KK.9, J=1): v(a) := e^a (chi(a)-a-
    log rho) for T2 at a in {7, 7+log2, 7+log4, 7+2log4}:
    full-period invariance |v(7)-v(7+log4)| <= 1e-3 and
    |v(7+log4)-v(7+2log4)| <= 1e-3; half-period swing
    |v(7)-v(7+log2)| >= 0.1 (the comb IS present, at coefficient level --
    rereading of JJ's AJ5b fine structure: JJ's own d(5)/d(5+log4) =
    5.842e-3/1.464e-3 = 3.99 ~ e^{log 4}); elementary-formula match
    |v(a) - (1+2 R_Z(e^-a))/rho| <= 5e-3 with R_Z = sum_{k in Z}
    [psi(4^k t) - psi(2 4^k t)] (cap s<200 + analytic tail -1/(3 s_next)).

Run: python3 -m scripts.numerics.witness.prime_int_kk_l1_density_rr
"""

import math
import sys
from math import exp, fsum, log, pi

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


LOG4 = log(4.0)

COMBS = {
    "T2": {2: 2},
    "T3": {3: 2},
    "T23": {2: 2, 3: 2},
    "T2d3": {2: 3},
    "T235": {2: 2, 3: 2, 5: 2},
}


def rho_of(comb):
    r = 1.0
    for p, d in comb.items():
        r *= (1 - 1 / p) / (1 - p ** (-d))
    return r


def BJ(J):
    B = 4.0 / 3.0
    for _ in range(J - 1):
        B = (4.0 / 3.0) * (1 + B)
    return B


def CT(comb):
    J = len(comb)
    c = 1.0
    sigma = 1.0
    for p in comb:
        c *= 1 - 1 / p
        sigma *= 1 + p
    return (2 * pi / 9) * sigma + (2 ** J * 1.01 * exp(-pi) + c / 2) * BJ(J)


def ET(x, comb):
    J = len(comb)
    c = 1.0
    for p in comb:
        c *= 1 - 1 / p
    L = 1 + log(x) / LOG4 if x >= 1 else 1.0
    return c * BJ(J) * L ** (J - 1) + 2 ** J * L ** J


def in_comb(n, comb):
    for p, d in comb.items():
        v = 0
        while n % p == 0:
            n //= p
            v += 1
        if v % d:
            return False
    return True


def theta(s):
    terms = []
    m = 1
    while pi * m * m * s * s < 745:
        terms.append(exp(-pi * m * m * s * s))
        m += 1
    return fsum(terms)


def psi(s):
    return theta(s) - 1 / (2 * s) + 0.5


def theta_S(t, comb):
    terms = []
    n = 1
    while pi * n * n * t * t < 745:
        if in_comb(n, comb):
            terms.append(exp(-pi * n * n * t * t))
        n += 1
    return fsum(terms)


def h0(a, comb):
    return log(1 + 2 * theta_S(exp(-a), comb))


def chi(a, comb):
    return h0(a, comb) - h0(-a, comb)


# ------------------------------------------------------------------ KL0
ok = True
detail = []
for name, jj in (("T2", -0.405205), ("T3", -0.287391), ("T23", -0.692608)):
    c8 = chi(8.0, COMBS[name]) - 8.0
    ok = ok and abs(c8 - jj) < 1e-5
    detail.append("%s %.6f" % (name, c8))
gate("KL0 continuity-with-JJ-AJ5b", ok, "; ".join(detail))

# ------------------------------------------------------------------ KL1
ok = True
worst = 0.0
for i in range(1, 401):
    s = i * 0.01
    r = abs(psi(s)) / (pi * s / 6)
    worst = max(worst, r)
    ok = ok and r <= 1.0
# trivial regime s > 4: |psi| <= 1/2 + 1/(2s) + theta(s) <= 0.51 + theta(4)
ok = ok and (0.5 + 1 / 8 + theta(4.0)) < pi * 4 / 6
wt = 0.0
for i in range(100, 301):
    s = i * 0.01
    rt = theta(s) / exp(-pi * s * s)
    wt = max(wt, rt)
    ok = ok and rt <= 1.01
gate("KL1 euler-maclaurin-unit", ok,
     "worst |psi|/(pi s/6)=%.3f; worst tail ratio=%.5f (<=1.01)"
     % (worst, wt))

# ------------------------------------------------------------------ KL2
ok = True
detail = []
for name, comb in COMBS.items():
    rho = rho_of(comb)
    N = 0
    wr = 0.0
    for n in range(1, 10 ** 6 + 1):
        if in_comb(n, comb):
            N += 1
        ratio = abs(N - rho * n) / ET(n, comb)
        if ratio > wr:
            wr = ratio
        if ratio > 1.0:
            ok = False
    detail.append("%s wr=%.3f" % (name, wr))
gate("KL2 counting-lemma-every-x<=1e6", ok, "; ".join(detail))

# ------------------------------------------------------------------ KL3
ok = True
detail = []
XMAX = 10 ** 8
for name, comb in COMBS.items():
    J = len(comb)
    # enumerate Q = {prod p^{d_p j_p}} <= XMAX exactly
    Q = [1]
    for p, d in comb.items():
        base = p ** d
        Q = [q * base ** j for q in Q
             for j in range(int(log(XMAX / q) / log(base)) + 1)
             if q * base ** j <= XMAX]
    Q.sort()
    sum_all = 1.0
    for p, d in comb.items():
        sum_all *= 1 / (1 - p ** (-d))
    for x in (10.0, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8):
        L4 = 1 + log(x) / LOG4
        Qx = sum(1 for q in Q if q <= x)
        Tx = sum_all - fsum(1 / q for q in Q if q <= x)
        Ux = sum(q for q in Q if q <= x)
        ok = ok and Qx <= L4 ** J
        ok = ok and x * Tx <= BJ(J) * L4 ** (J - 1) + 1e-9
        ok = ok and Ux <= (4 / 3) * x * L4 ** (J - 1)
    detail.append(name)
gate("KL3 comb-constants-QTU", ok, "Q(x),xT(x),U(x) bounds, x<=1e8: "
     + " ".join(detail))

# ------------------------------------------------------------------ KL4
ok = True
detail = []
for name, comb in COMBS.items():
    J = len(comb)
    rho = rho_of(comb)
    ct = CT(comb)
    wr = 0.0
    for a in (2.0, 4.0, 6.0, 8.0, 10.0):
        R = theta_S(exp(-a), comb) - (rho / 2) * exp(a)
        ratio = abs(R) / (ct * (1 + a / LOG4) ** (J - 1))
        wr = max(wr, ratio)
        ok = ok and ratio <= 1.0
    detail.append("%s wr=%.3f" % (name, wr))
gate("KL4 master-remainder<=C_T L^{J-1}", ok, "; ".join(detail))

# ------------------------------------------------------------------ KL5
ok = True
detail = []
POINTS = {"T2": (4, 6, 8, 10), "T3": (4, 6, 8, 10), "T2d3": (4, 6, 8, 10),
          "T23": (7, 8, 9, 10), "T235": (11, 12)}
for name, alist in POINTS.items():
    comb = COMBS[name]
    J = len(comb)
    rho = rho_of(comb)
    ct = CT(comb)
    wr = 0.0
    for a in alist:
        a = float(a)
        amp = 1 + 2 * ct * (1 + a / LOG4) ** (J - 1)
        u = amp * exp(-a) / rho
        ok = ok and u <= 0.5                       # precondition holds
        d = chi(a, comb) - a - log(rho)
        bound = (2 / rho) * amp * exp(-a) + 2.02 * exp(-pi * exp(2 * a)) \
            if a < 2 else (2 / rho) * amp * exp(-a)
        ratio = abs(d) / bound
        wr = max(wr, ratio)
        ok = ok and ratio <= 1.0
    detail.append("%s wr=%.3f" % (name, wr))
# dual bound directly
for a in (0.5, 1.0):
    dual = h0(-a, COMBS["T2"])
    ok = ok and dual <= 2.02 * exp(-pi * exp(2 * a))
gate("KL5 THEOREM-defect-bound", ok, "; ".join(detail)
     + "; dual<=2.02e^{-pi e^2a} ok")

# ------------------------------------------------------------------ KL6
ok = True
# (a) m_2 = +1: ON the wall; A = 2^k all have w = e^-a
a0 = 1.0
lower = (10 ** 4 + 1) * exp(-pi * exp(-2 * a0))
ok = ok and lower > 100.0
# (b) m_2 = +2: beyond the wall; w(2^k) = 2^-k -> terms -> 1
s_b = fsum(exp(-pi * (2.0 ** (-k)) ** 2) for k in range(200))
ok = ok and s_b >= 190.0
# (c) real-cone interior 0 < m_2 < 1: finite with real density rho(m)
def theta_real(t, alpha):
    # w(A) = 2^{alpha v} B (B odd); theta = sum_v [theta(2^av t)-theta(2^{av+1} t)]
    v = 0
    terms = []
    while pi * (2 ** (alpha * v) * t) ** 2 < 745:
        s = 2 ** (alpha * v) * t
        terms.append(theta(s) - theta(2 * s))
        v += 1
    return fsum(terms)
detail = []
for m2 in (0.5, 0.9):
    alpha = 1 - m2
    rho_r = 0.5 / (1 - 2 ** (-alpha))
    a = 10.0
    cr = log(1 + 2 * theta_real(exp(-a), alpha)) \
        - log(1 + 2 * theta_real(exp(a), alpha)) - a
    ok = ok and abs(cr - log(rho_r)) <= 1e-3
    detail.append("m=%.1f rho=%.3f dev=%.1e" % (m2, rho_r, cr - log(rho_r)))
rho_wall = 0.5 / (1 - 2 ** (-0.01))
gate("KL6 effective-cone-trichotomy", ok,
     "wall m=+1 partial>=%.0f; m=+2 sum>=%.0f; real interior: %s; "
     "rho(m=0.99)=%.1f RECORDED (wall blow-up)"
     % (lower, s_b, "; ".join(detail), rho_wall))

# ------------------------------------------------------------------ KL7
ok = True
def N_S(x, comb):
    c = 0
    n = 1
    while n <= x:
        if in_comb(n, comb):
            c += 1
        n += 1
    return c
detail = []
for name in ("T2", "T23", "T2d3"):
    comb = COMBS[name]
    rho = rho_of(comb)
    ok = ok and log(rho) <= 0                       # rho <= 1 clause
    for a in (-0.5, -0.01, 0.0, 0.3, 1.0, 5.0, 10.0):
        N = N_S(exp(a), comb)
        ok = ok and (N >= 1) == (a >= 0)
        if a + log(rho) > 0:
            ok = ok and N >= 1                      # chi_ren > 0 => effective
    for a in (5.0, 10.0):
        N = N_S(exp(a), comb)
        ok = ok and abs(N - rho * exp(a)) <= ET(exp(a), comb)
    a = 10.0
    N = N_S(exp(a), comb)
    growth_dev = log(N) - a - log(rho)
    ok = ok and abs(growth_dev) <= 2 * ET(exp(a), comb) / (rho * exp(a))
    detail.append("%s N(10)=%d logN-chi_ren=%+.1e" % (name, N, growth_dev))
gate("KL7 corollary-effectivity+growth", ok, "; ".join(detail))

# ------------------------------------------------------------------ KL8
ok = True
def theta_S_quartic(t, comb):
    terms = []
    n = 1
    while pi * (n * t) ** 4 < 745:
        if in_comb(n, comb):
            terms.append(exp(-pi * (n * t) ** 4))
        n += 1
    return fsum(terms)
If = math.gamma(1.25) / pi ** 0.25
target = log(rho_of(COMBS["T2"])) + log(2 * If)
recs = []
for a in (4.0, 6.0, 8.0):
    cf = log(1 + 2 * theta_S_quartic(exp(-a), COMBS["T2"])) \
        - log(1 + 2 * theta_S_quartic(exp(a), COMBS["T2"])) - a
    recs.append((a, cf - target))
ok = ok and abs(recs[-1][1]) <= 2e-3
gate("KL8 universality-quartic-unit", ok,
     "I_f=%.6f; dev(a=4,6,8) = %s (gate at a=8 <= 2e-3): rho is "
     "unit-independent, Gaussian only normalizes the constant"
     % (If, ["%+.1e" % d for _, d in recs]))

# ------------------------------------------------------------------ KL9
ok = True
rho2 = rho_of(COMBS["T2"])
l2, l4 = log(2.0), LOG4
vals = {}
for da in (0.0, l2, l4, 2 * l4):
    a = 7.0 + da
    vals[da] = exp(a) * (chi(a, COMBS["T2"]) - a - log(rho2))
ok = ok and abs(vals[0.0] - vals[l4]) <= 1e-3
ok = ok and abs(vals[l4] - vals[2 * l4]) <= 1e-3
ok = ok and abs(vals[0.0] - vals[l2]) >= 0.1
def R_Z(t):
    # k in Z with 1e-4 <= 4^k t < 200; skipped small-s terms are bounded
    # by sum (pi/6)(s + 2s) <= (pi/2) 1e-4 (4/3) ~ 2e-4 (Lemma KK.2),
    # within the 5e-3 gate tolerance; large-s tail added analytically.
    k = 0
    while 4 ** (k - 1) * t >= 1e-4:
        k -= 1
    s = 4 ** k * t
    terms = []
    while s < 200:
        terms.append(psi(s) - psi(2 * s))
        s *= 4
    return fsum(terms) - 1 / (3 * s)                # analytic -1/(4s) tail
preds = {}
for da in (0.0, l2):
    a = 7.0 + da
    preds[da] = (1 + 2 * R_Z(exp(-a))) / rho2
    ok = ok and abs(vals[da] - preds[da]) <= 5e-3
gate("KL9 log-periodic-coefficient", ok,
     "v(7,7+l2,7+l4,7+2l4) = %.4f %.4f %.4f %.4f; period-log4 invariance "
     "<=1e-3, half-period swing %.3f >= 0.1; elementary R_Z prediction "
     "%.4f %.4f (match <=5e-3)"
     % (vals[0.0], vals[l2], vals[l4], vals[2 * l4],
        abs(vals[0.0] - vals[l2]), preds[0.0], preds[l2]))
print("  KL9 reread of JJ AJ5b fine structure: JJ's recorded d_T2(5)/"
      "d_T2(5+log4) = 5.842e-3/1.464e-3 = 3.99 ~ 4 = e^{log4}: the comb JJ "
      "registered IS present, at coefficient (e^a d) level, period log 4.")

# ------------------------------------------------------------------ exit
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (KL0-KL9)")
sys.exit(0)
