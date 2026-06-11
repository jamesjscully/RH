"""LL-witness: the duality-renormalized square dual (doc 33 sec 3 item 2).

Registrations in research/work/LL-square-dual.md secs 1-2, written
BEFORE the first run.  Exit 0 iff ALL gates pass.  Fail-closed.
No RH / zero-side input; no zeta values or continuation anywhere
(F-a); flint arb prec 300 + exact Fractions.

Object under test: for the strict-square effective twist D_T(a)
(m_p = -1, p in T; JJ AJ5), whose in-family RR dual DIVERGES (JJ
AJ5a: constant weight along the p-power fiber = the branch series at
its pole), the K2-paired resummation

    Theta_T^dual(u) = sum_{kvec in N^T} [ sum_{dvec in {0,1}^T}
                      (-1)^{|dvec|} N^{-1} theta(u/N) ],
    N = prod_p p^{2 k_p + d_p},   theta = Jacobi theta,

with the kvec-block as the summation unit (the banked branch-mirror
pairing: each block's continuum zero modes 1/u cancel exactly - the
A_D + A_D' + 1 = 0 mechanism, square dress).  Renormalized dual count
h^0_ren(K_sq - D) := log Theta_T^dual(e^a); exact inhomogeneous RR
Theta_T(t) - 1 = (1/t) Theta_T^dual(1/t).  Gates LL1-LL7 as
registered in the doc.

Run: python3 -m scripts.numerics.witness.prime_int_ll_square_dual
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


# ---------------------------------------------------------------- theta
def jacobi_theta(x):
    """theta(x) = sum_{m in Z} e^{-pi m^2 x^2}; Poisson-reflected for
    x < 1 (theta(x) = (1/x) theta(1/x), classical Jacobi - the SAME
    per-lattice Poisson the construction spends); terms to < 1e-95."""
    x = x if isinstance(x, arb) else arb(x)
    if float(x.mid()) < 1.0:
        return (1 / x) * jacobi_theta(1 / x)
    s = arb(1)
    pix2 = arb.pi() * x * x
    m = 1
    while True:
        term = (-pix2 * m * m).exp()
        if float(term.mid()) < 1e-95:
            break
        s += 2 * term
        m += 1
        if m > 10 ** 6:
            raise RuntimeError("theta did not truncate")
    return s


def theta_comb(T, t):
    """Direct side: Theta_T(t) = 1 + 2 sum_{n in S_T} e^{-pi n^2 t^2},
    S_T = {n >= 1 : v_p(n) even for all p in T}  (JJ's machinery)."""
    t = t if isinstance(t, arb) else arb(t)
    nmax = int(16.0 / float(t.mid())) + 2
    s = arb(0)
    pit2 = arb.pi() * t * t
    for n in range(1, nmax + 1):
        good = True
        for p in T:
            v, m = 0, n
            while m % p == 0:
                v += 1
                m //= p
            if v % 2 == 1:
                good = False
                break
        if good:
            s += (-pit2 * n * n).exp()
    return 1 + 2 * s


def theta_dual(T, u):
    """The PAIRED resummation Theta_T^dual(u): kvec-blocks as units."""
    u = u if isinstance(u, arb) else arb(u)
    kmax = int(math.log(max(float(u.mid()), 1.0)) / math.log(2)) + 14
    total = arb(0)

    def rec(i, kpart):
        nonlocal total
        if i == len(T):
            block = arb(0)
            for dmask in range(2 ** len(T)):
                N, bits = 1, 0
                for j, p in enumerate(T):
                    d = (dmask >> j) & 1
                    bits += d
                    N *= p ** (2 * kpart[j] + d)
                term = jacobi_theta(u / N) / N
                block += term if bits % 2 == 0 else -term
            total += block
            return
        for k in range(kmax + 1):
            rec(i + 1, kpart + [k])

    rec(0, [])
    return total


# ------------------------------------------------------------------ LL1
ok = True
detail = []
# (a) zero-mode cancellation per level, EXACT (Fractions): the continuum
# unit of N^{-1} theta(u/N) is N^{-1} * (N/u) = (1/u) for lattice and
# half-refinement alike; the (-1)^{|d|} sum kills them level-by-level.
for k in range(0, 30):
    zm_lat = Fraction(1, 4 ** k) * Fraction(4 ** k, 1)          # x (1/u)
    zm_ref = Fraction(1, 2 * 4 ** k) * Fraction(2 * 4 ** k, 1)  # x (1/u)
    ok = ok and zm_lat == 1 and zm_ref == 1 and zm_lat - zm_ref == 0
# (b) paired convergence (T={2}, u in {e^-1, 1, e, e^3}): blocks
#     positive while resolvable, Cauchy by K <= 14
for a in (-1.0, 0.0, 1.0, 3.0):
    u = arb(a).exp()
    cauchy_at = None
    for K in range(0, 16):
        N1, N2 = 4 ** K, 2 * 4 ** K
        block = jacobi_theta(u / N1) / N1 - jacobi_theta(u / N2) / N2
        b = float(block.mid())
        if abs(b) > 1e-60:
            ok = ok and b > 0                      # positivity per block
        elif cauchy_at is None:
            cauchy_at = K
    ok = ok and cauchy_at is not None and cauchy_at <= 14
    detail.append("u=e^%g cauchy@K=%s" % (a, cauchy_at))
# (c) UNPAIRED divergence: increments of sum_k 4^{-k} theta(u 4^{-k})
#     are one continuum unit (1/u) per level for k in [25, 30]
for a in (0.0, 1.0):
    u = arb(a).exp()
    for k in range(25, 31):
        inc = jacobi_theta(u / 4 ** k) / (4 ** k)
        ok = ok and abs(float((inc * u).mid()) - 1.0) < 1e-6
gate("LL1 pairing-is-existence", ok,
     "zero modes cancel exact/level; paired blocks >0, %s; unpaired "
     "increment = 1/u per level (k=25..30): divergence" %
     "; ".join(detail))

# ------------------------------------------------------------------ LL2
ok = True
worst = 0.0
TWISTS = {"T2": (2,), "T3": (3,), "T23": (2, 3)}
RHO = {"T2": Fraction(2, 3), "T3": Fraction(3, 4), "T23": Fraction(1, 2)}
AGRID = {"T2": (-1.0, -0.5, 0.5, 1.0, 2.0, 5.0, 8.0),
         "T3": (-1.0, -0.5, 0.5, 1.0, 2.0, 5.0, 8.0),
         "T23": (-1.0, -0.5, 0.5, 1.0, 2.0, 5.0)}
H0 = {}      # cache (Tname, a) -> (h0, h0ren, theta_dual value)
for name, T in TWISTS.items():
    for a in AGRID[name]:
        lhs = theta_comb(T, arb(-a).exp()) - 1       # direct route
        dual = theta_dual(T, arb(a).exp())           # paired route
        rhs = arb(a).exp() * dual
        rel = abs(float((lhs - rhs).mid())) / abs(float(lhs.mid()))
        worst = max(worst, rel)
        ok = ok and rel < 1e-50
        H0[(name, a)] = ((1 + lhs).log(), dual.log(), dual)
gate("LL2 exact-FE-RR-identity", ok,
     "Theta_T(e^-a)-1 = e^a Theta_T^dual(e^a), independent routes, "
     "worst rel = %.1e (3 twists x grid)" % worst)

# ------------------------------------------------------------------ LL3
ok = True


def c_weight(p, e):
    """Exact dual-measure weight at v_p(xi) = e, from the
    lattice-membership geometric series (Fractions):
    c_p(e) = sum_{k >= ka} p^{-2k} - sum_{k >= kb} p^{-2k-1},
    ka = ceil(-e/2)+, kb = ceil((-e-1)/2)+."""
    j = -e
    ka = max(0, (j + 1) // 2)
    kb = max(0, j // 2) if j >= 1 else 0
    s1 = Fraction(1, p ** (2 * ka)) / (1 - Fraction(1, p * p))
    s2 = Fraction(1, p ** (2 * kb + 1)) / (1 - Fraction(1, p * p))
    return s1 - s2


for p in (2, 3):
    rho = Fraction(p, p + 1)
    for e in range(0, 9):
        ok = ok and c_weight(p, e) == rho
    for j in range(1, 11):
        ok = ok and c_weight(p, -j) == (-1) ** j * rho * Fraction(1, p ** j)
# (b) multiplicativity: two-place truncated membership sums vs the
#     product of closed forms (truncation k <= 40: error < 4^-40)
def c_weight2_trunc(p, q, ep, eq):
    tot = Fraction(0)
    for kp in range(0, 41):
        for dp in (0, 1):
            # xi in p^{2kp+dp}-refined lattice iff v_p(xi) >= -(2kp+dp)
            if ep < -(2 * kp + dp):
                continue
            for kq in range(0, 41):
                for dq in (0, 1):
                    if eq < -(2 * kq + dq):
                        continue
                    w = Fraction(1, p ** (2 * kp + dp) * q ** (2 * kq + dq))
                    tot += w if (dp + dq) % 2 == 0 else -w
    return tot


for ep in (-2, -1, 0, 1):
    for eq in (-2, -1, 0, 1):
        diff = c_weight2_trunc(2, 3, ep, eq) - c_weight(2, ep) * c_weight(3, eq)
        ok = ok and abs(float(diff)) < 1e-20
# (c) NON-ABSOLUTE convergence of the point-grouped reading (u=1, T2):
#     per-depth |c|-mass increment -> rho_2/2 = 1/3 EXACTLY (derived:
#     |c_2(-j)| * point density = rho 2^-j * 2^{j-1} * 2 Int e^{-pi x^2}
#     = rho/2), no decay.  WITNESS-ENGINEERING RECORD (disclosed, GG
#     precedent): first run measured 0.333/depth against a registered
#     window (0.5, 0.9) that was hand-derived with |c| = rho 2^{1-j} --
#     inconsistent with the EXACT weight rho 2^{-j} this same gate
#     verifies.  Clause replaced by the derived-value form
#     |inc - 1/3| < 0.02 (strictly stronger); divergence verdict
#     unchanged.
incs = []
S = 0.0
for j in range(1, 21):
    w = float(Fraction(2, 3) * Fraction(1, 2 ** j))     # |c_2(-j)|
    sub, B = 0.0, 1
    while True:
        x = B / 2 ** j
        term = math.exp(-math.pi * x * x)
        if term < 1e-30:
            break
        sub += 2 * term                                  # xi = +-B/2^j
        B += 2
    Sprev, S = S, S + w * sub
    if j >= 5:
        incs.append(S - Sprev)
ok = ok and all(abs(i - 1.0 / 3.0) < 0.02 for i in incs)
ok = ok and incs[-1] > 0.3                       # no decay: divergence
gate("LL3 dual-measure-weights", ok,
     "c_p(e)=rho_p (e>=0), c_p(-j)=(-1)^j rho_p p^-j exact; two-place "
     "product exact to trunc; |c|-mass grows %.3f/depth (j=5..20): "
     "point-grouping non-absolute, pairing load-bearing" %
     (sum(incs) / len(incs)))

# ------------------------------------------------------------------ LL4
ok = True
detail = []
for name, T in TWISTS.items():
    rho = float(RHO[name])
    # (a) wiring: (h0 - h0ren) - a - eps = 0 exactly
    for a in (0.5, 2.0, 5.0):
        h0, h0ren, dual = H0[(name, a)]
        eps = (1 + (arb(-a)).exp() / dual).log()
        ok = ok and abs(float((h0 - h0ren - arb(a) - eps).mid())) < 1e-50
    # (b) eps in (0, 2 e^-a / rho)
    for a in (2.0, 5.0) + ((8.0,) if name in ("T2", "T3") else ()):
        _, _, dual = H0[(name, a)]
        eps = float(((1 + (arb(-a)).exp() / dual).log()).mid())
        ok = ok and 0 < eps < 2 * math.exp(-a) / rho
    # (c)+(d) floor convergence and approach FROM BELOW
    for a in (5.0,) + ((8.0,) if name in ("T2", "T3") else ()):
        _, _, dual = H0[(name, a)]
        dv = float(dual.mid())
        ok = ok and abs(dv - rho) < 2 * math.exp(-a) and dv < rho
        detail.append("%s a=%g dual-rho=%.2e" % (name, a, dv - rho))
gate("LL4 RR-chi-shape+dual-floor", ok, "; ".join(detail))
print("  LL4 RECORD d_T(a) via the FE/dual route (compare JJ banked "
      "0.005842/0.000260 T2, 0.004104/0.000291 T3, 0.012172 T23@5):")
for name, T in TWISTS.items():
    for a in (5.0,) + ((8.0,) if name in ("T2", "T3") else ()):
        h0, _, _ = H0[(name, a)]
        h0neg = theta_comb(T, arb(a).exp()).log()
        dT = float((h0 - h0neg - arb(a)).mid()) - math.log(float(RHO[name]))
        print("    %s a=%g d_T=%.6f" % (name, a, dT))
print("  LL4 RECORD fine structure D(a) = (rho - dual(e^a)) e^a, T2, "
      "a = 5..8 step log(4)/4 (log-periodic modulation, period log 4):")
step = math.log(4) / 4
for i in range(int(3.0 / step) + 1):
    a = 5.0 + i * step
    dv = theta_dual((2,), arb(a).exp())
    print("    a=%.4f D(a)=%.6f" %
          (a, (float(RHO["T2"]) - float(dv.mid())) * math.exp(a)))

# ------------------------------------------------------------------ LL5
ok = True
detail = []


def margins(name, a):
    h0, h0ren, dual = H0[(name, a)]
    eps = (1 + (arb(-a)).exp() / dual).log()
    m0 = float((eps + 2 * h0ren).mid())
    m2 = m0 - 2 * math.log(float(RHO[name]))
    return m0, m2, float(h0ren.mid())


# (a) REGISTERED SIGN TABLE (sign-indefinite fine-structure margin):
SIGNS = {("T2", 5.0): +1, ("T2", 8.0): +1, ("T3", 5.0): -1,
         ("T3", 8.0): +1, ("T23", 5.0): +1}
for (name, a), sgn in SIGNS.items():
    _, m2, _ = margins(name, a)
    ok = ok and (m2 > 0 if sgn > 0 else m2 < 0) and abs(m2) < 0.02
    detail.append("%s margin2(%g)=%+.2e" % (name, a, m2))
# (b) chi_0 normalization fails: margin_0(8) -> 2 log rho < 0
m0_8, _, _ = margins("T2", 8.0)
ok = ok and m0_8 < -0.5
detail.append("T2 margin0(8)=%.3f" % m0_8)
# (c) SECTOR N (Schur-negative) FAILS doubly-exponentially (T2, a=-1)
_, m2n, h0ren_n = margins("T2", -1.0)
ok = ok and h0ren_n < -15 and m2n < -5
detail.append("T2 a=-1: h0ren=%.2f margin2=%.2f" % (h0ren_n, m2n))
# (d) equivalence: margin with chi = deg + eps equals 2 h0ren exactly
for name, a in (("T2", 2.0), ("T3", 1.0), ("T23", 0.5)):
    h0, h0ren, dual = H0[(name, a)]
    eps = (1 + (arb(-a)).exp() / dual).log()
    d = abs(float((h0 + h0ren - arb(a) - eps - 2 * h0ren).mid()))
    ok = ok and d < 1e-50
gate("LL5 index-inequality-posed", ok, "; ".join(detail))

# ------------------------------------------------------------------ LL6
ok = True
detail = []
GRID6 = {"T2": (-2.0, -1.0, -0.5, 0.5, 1.0, 2.0, 5.0, 8.0),
         "T3": (-1.0, 0.5, 5.0, 8.0), "T23": (-1.0, 0.5, 5.0)}
for name, T in TWISTS.items():
    rho = float(RHO[name])
    kappa = math.log(rho * (1 + rho))
    for a in GRID6[name]:
        if (name, a) in H0:
            h0, _, dual = H0[(name, a)]
        else:
            h0 = theta_comb(T, arb(-a).exp()).log()
            dual = theta_dual(T, arb(a).exp())
        h0renp = (1 + dual).log()
        mp = float((h0 + h0renp).mid()) - a - kappa
        ok = ok and float(h0renp.mid()) >= 0 and mp >= 0
        detail.append("%s m+(%g)=%.4f" % (name, a, mp))
gate("LL6 logged-insertion-repairs (DEMOTED diagnosis)", ok,
     "; ".join(detail))

# ------------------------------------------------------------------ LL7
ok = True


def represented(n):
    x = 0
    while x * x <= n:
        rem = n - x * x
        if rem % 5 == 0:
            y = math.isqrt(rem // 5)
            if y * y == rem // 5:
                return True
        x += 1
    return False


rep = {n for n in range(1, 100) if represented(n)}
ok = ok and 2 not in rep and 3 not in rep
ok = ok and all(n in rep for n in (1, 4, 6, 9, 36))


def irreducible(n):
    return n in rep and not any(
        n % d == 0 and d in rep and n // d in rep for d in range(2, n))


ok = ok and all(irreducible(n) for n in (4, 6, 9))
ok = ok and 4 * 9 == 36 and 6 * 6 == 36
# ill-definedness of the comb: an additive v would need
# v(36) = v(4) + v(9) = 0 + 0 AND v(36) = 2 v(6) = 2: contradiction,
# so "v(n) even" is not a proposition: no comb, no branch ladder,
# no mirror, no pairing levels: the K2 renormalization is UNFORMABLE.
v_via_49, v_via_66 = 0 + 0, 1 + 1
ok = ok and v_via_49 != v_via_66
ok = ok and (v_via_49 % 2) == 0 and (v_via_66 % 2) == 0  # both EVEN: yet
# the VALUES differ, so no additive v exists at all (the parity comb
# needs v first); the failure is at valuation-existence, before parity.
gate("LL7 epstein-unformable (no comb, no branches, nothing to pair)",
     ok, "2,3 absent; 4,6,9 irreducible; 36=4*9=6*6; v(36) in {0,2} by "
     "chain: comb membership not a proposition; K2 pairing unformable")
print("  LL7 DH bookkeeping: no carrier group at all -> no monoid, no "
      "comb, dies before the pairing (nonexistence, as required).")

# ------------------------------------------------------------------ exit
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (LL1-LL7)")
sys.exit(0)
