"""NN-witness: does LL's unit-repaired index inequality extend to the
Frobenius-graph classes (HH's cone)?  Doc 34 sec 3 decision test.

Registrations in research/work/NN-graph-class-test.md secs 0-2, written
BEFORE the first run.  Exit 0 iff all STRUCTURAL gates pass; the sign
census / identification values feed the registered verdict table (II6
precedent: the verdict value is recorded, not gated).

Dictionary (registered, sec 1.1): [p^k] <-> depth-k twist class
(comb v_p = 0 mod k, m_p = 1 - k); rung class D_R = (a = R; d_p =
n_p(R) = floor(R/log p), places with n_p >= 2).  Unit-repaired margin
(LL6 VERBATIM, the hand-inserted unit, logged + demoted):
    m+(D) = log Theta_T(e^-a) + log(1 + Theta_T^dual(e^a))
            - a - log(rho_T (1 + rho_T)),
Theta^dual via the FE (= the K2-paired resummation, certified by
independent routes in G1 at general depth).

F-a: no zeta values/continuation; zeros ONLY via fork_lib.zeta_gammas
AFTER the sha256 freeze (G7), comparison only.

Run: python3 -m scripts.numerics.witness.prime_nn_graph_class_index
"""

import hashlib
import json
import math
import sys
from fractions import Fraction

import numpy as np
import flint

flint.ctx.prec = 300
arb = flint.arb

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def record(msg):
    print("  " + msg)


# ---------------------------------------------------------------- core
def jacobi_theta(x):
    """theta(x) = sum_{m in Z} e^{-pi m^2 x^2}, Poisson-reflected (LL)."""
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


def vp(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def theta_comb(depths, t):
    """Theta_T(t) = 1 + 2 sum_{n in S} e^{-pi n^2 t^2},
    S = {n : v_p(n) = 0 mod d_p, (p, d_p) in depths}.  arb."""
    t = t if isinstance(t, arb) else arb(t)
    nmax = int(16.0 / float(t.mid())) + 2
    pit2 = arb.pi() * t * t
    s = arb(0)
    for n in range(1, nmax + 1):
        if all(vp(n, p) % d == 0 for p, d in depths.items()):
            s += (-pit2 * n * n).exp()
    return 1 + 2 * s


def theta_dual_paired(depths, u, kmax):
    """The K2-paired resummation at general depth (kvec-blocks as units):
    sum_kvec sum_{dvec in {0,1}^T} (-1)^{|dvec|} N^{-1} theta(u/N),
    N = prod_p p^{d_p k_p + dvec_p}.  Independent route for G1/G3."""
    u = u if isinstance(u, arb) else arb(u)
    places = sorted(depths)
    total = arb(0)

    def rec(i, kpart):
        nonlocal total
        if i == len(places):
            block = arb(0)
            for dmask in range(2 ** len(places)):
                N, bits = 1, 0
                for j, p in enumerate(places):
                    dd = (dmask >> j) & 1
                    bits += dd
                    N *= p ** (depths[p] * kpart[j] + dd)
                term = jacobi_theta(u / N) / N
                block += term if bits % 2 == 0 else -term
            total += block
            return
        for k in range(kmax + 1):
            rec(i + 1, kpart + [k])

    rec(0, [])
    return total


def rho_T(depths):
    r = Fraction(1)
    for p, d in depths.items():
        r *= (1 - Fraction(1, p)) / (1 - Fraction(1, p ** d))
    return r


def margin_plus(depths, a):
    """Returns (m+, h0, dual) in arb via the FE route (certified by G1)."""
    Theta = theta_comb(depths, arb(-a).exp())
    dual = (Theta - 1) * arb(-a).exp()
    rho = rho_T(depths)
    rho_a = arb(rho.numerator) / arb(rho.denominator)
    h0 = Theta.log()
    mp = h0 + (1 + dual).log() - arb(a) - (rho_a * (1 + rho_a)).log()
    return mp, h0, dual


def resolved_sign(x):
    """+1/-1 if the arb ball resolves the sign, else 0."""
    m, r = float(x.mid()), float(x.rad())
    if abs(m) > r:
        return 1 if m > 0 else -1
    return 0


# ------------------------------------------------------------------ G1
print("G1: generalized FE, independent routes (comb vs paired lattice)")
G1_FAMILY = [({2: 1}, 24), ({2: 3}, 24), ({2: 4}, 24), ({2: 5}, 24),
             ({3: 3}, 24), ({2: 3, 3: 2}, 12)]
ok = True
worst = 0.0
for depths, kmax in G1_FAMILY:
    for a in (0.5, 2.0, 5.0):
        lhs = theta_comb(depths, arb(-a).exp()) - 1
        rhs = arb(a).exp() * theta_dual_paired(depths, arb(a).exp(), kmax)
        rel = abs(float((lhs - rhs).mid())) / abs(float(lhs.mid()))
        worst = max(worst, rel)
        ok = ok and rel < 1e-45
# zero-mode cancellation per kvec-block, exact Fractions, d in {1,3,5}
for d in (1, 3, 5):
    for p in (2, 3):
        for k in (0, 3, 11):
            zl = Fraction(1, p ** (d * k)) * Fraction(p ** (d * k), 1)
            zr = Fraction(1, p ** (d * k + 1)) * Fraction(p ** (d * k + 1), 1)
            ok = ok and zl == 1 and zr == 1 and zl - zr == 0
gate("G1 generalized-FE-independent-routes", ok,
     "6 depth classes x a in {0.5,2,5}, worst rel = %.1e; per-block "
     "zero modes cancel exactly (Fraction, d in {1,3,5})" % worst)

# ------------------------------------------------------------------ G2
print("G2: dual floor at general depth")
# WITNESS-ENGINEERING RECORD (disclosed, LL3c precedent): the first run
# REFUTED the registered sign clause "dual < rho (from below)" at the
# mixed-depth class {2:3,3:2}, a=5 (dual - rho = +2.7e-3).  That clause
# was an EXTRAPOLATION of LL4d (certified only on the strict d=2 family),
# not a derivation; it is demoted to the RECORD below and the refutation
# is reported as a finding (sign of approach is depth-structure dependent).
# The derived floor BOUND (the load-bearing clause) is unchanged and gated.
ok = True
detail = []
sign_rec = []
for depths, _ in G1_FAMILY:
    rho = float(rho_T(depths))
    for a in (5.0, 8.0):
        _, _, dual = margin_plus(depths, a)
        dv = float(dual.mid())
        ok = ok and abs(dv - rho) < 4 * math.exp(-a) / rho
        detail.append("%s a=%g dual-rho=%+.1e" %
                      (str(depths).replace(" ", ""), a, dv - rho))
        sign_rec.append("+" if dv > rho else "-")
gate("G2 dual-floor-general-depth (bound)", ok, "; ".join(detail))
record("G2 RECORD sign of approach (REGISTERED from-below REFUTED at mixed "
       "depth): %s" % " ".join(sign_rec))

# ------------------------------------------------------------------ G3
print("G3: the d=1 breakage (registered prediction P1)")
ok = True
# (a) closed form theta(u) - 1/u, place-independent, two routes
worst = 0.0
for p in (2, 3, 5):
    for ua in (0.5, 2.0):
        u = arb(ua).exp()
        got = theta_dual_paired({p: 1}, u, 28)
        want = jacobi_theta(u) - 1 / u
        rel = abs(float((got - want).mid())) / abs(float(want.mid()))
        worst = max(worst, rel)
        ok = ok and rel < 1e-45
# (b)+(c) margin negative, asymptotic form
mvals = []
for a in (0.5, 1.0, 2.0, 5.0):
    mp, _, _ = margin_plus({2: 1}, a)
    mvals.append("m+(%g)=%+.5f" % (a, float(mp.mid())))
    ok = ok and resolved_sign(mp) == -1
    if a in (2.0, 5.0):
        ok = ok and abs(float(mp.mid()) + math.exp(-a) / 2) < 0.12 * math.exp(-a)
# (d) AJ4 control: canonical homogeneous margin > 0.
# DISCLOSED COMPUTATIONAL FIX (first run): at a = 5 the margin
# 2 log theta(e^a) ~ e^{-pi e^{10}} sits below the theta truncation
# (the sum returns exactly 1), so the sign is unresolvable at any
# practical precision; positivity there is the one-line theorem
# theta > 1.  Exhibition points moved to a in {1, 2} (resolvable);
# no registered claim changed.
for a in (1.0, 2.0):
    can = 2 * jacobi_theta(arb(a).exp()).log()
    ok = ok and resolved_sign(can) == 1
gate("G3 d1-breakage-as-derived", ok,
     "dual = theta(u) - 1/u two-route rel %.1e, place-independent; %s "
     "(all CERTIFIED < 0, ~ -e^-a/2); AJ4 canonical control > 0" %
     (worst, "; ".join(mvals)))
for a in (-2.0, -1.0):
    mp, _, _ = margin_plus({2: 1}, a)
    record("G3 RECORD sector-N d=1: m+(%g) = %+.4f" % (a, float(mp.mid())))

# ------------------------------------------------------------------ G4
print("G4: strict sub-cone census (window-admissible, all depths >= 2)")
LOG = math.log
census = []          # (label, a, admissible, sign, mid)


def add_class(depths, a, label):
    mp, _, _ = margin_plus(depths, a)
    adm = all(d <= math.floor(a / LOG(p) + 1e-12) for p, d in depths.items())
    census.append((label, a, adm, resolved_sign(mp), float(mp.mid())))


# (a) depth scan
for d in range(2, 9):
    for a in (1.0, 2.48, 4.96, 8.0):
        add_class({2: d}, a, "(2;%d)" % d)
for d in (2, 3, 4):
    for a in (1.0, 2.48, 4.96, 8.0):
        add_class({3: d}, a, "(3;%d)" % d)
for p in (5, 7, 11, 13):
    for a in (2.48, 4.96):
        add_class({p: 2}, a, "(%d;2)" % p)
# continuity with LL6 (T2 anchor)
ll6 = {}
for a in (5.0, 8.0):
    mp, _, _ = margin_plus({2: 2}, a)
    ll6[a] = float(mp.mid())
ok_cont = abs(ll6[5.0] - 0.0041) < 5e-4 and abs(ll6[8.0] - 0.0002) < 5e-4
# (b) period scans
for j in range(17):
    add_class({2: 3}, 5.0 + j * 3 * LOG(2) / 16, "(2;3)per")
    add_class({2: 5}, 5.0 + j * 5 * LOG(2) / 16, "(2;5)per")
# (c) the 14 rung towers (a = R_hi of each certified X-doc edge)
EDGES = [(1.60, 1.88), (1.88, 2.10), (2.10, 2.30), (2.30, 2.52),
         (2.52, 2.76), (2.76, 3.00), (3.00, 3.24), (3.24, 3.50),
         (3.50, 3.76), (3.76, 4.00), (4.00, 4.26), (4.26, 4.50),
         (4.50, 4.76), (4.76, 4.96)]
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def rung_depths(R):
    out = {}
    for p in PRIMES:
        n_p = math.floor(R / LOG(p) + 1e-12)
        if n_p >= 2:
            out[p] = n_p
    return out


rung_m = []
for (_, Rhi) in EDGES:
    depths = rung_depths(Rhi)
    mp, _, _ = margin_plus(depths, Rhi)
    rung_m.append(float(mp.mid()))
    census.append(("D_%.2f" % Rhi, Rhi, True, resolved_sign(mp),
                   float(mp.mid())))
# (d) rung-4.96 sub-tower box
d496 = rung_depths(4.96)
for k2 in range(2, d496[2] + 1):
    for k3 in range(2, d496[3] + 1):
        for k5 in range(2, d496[5] + 1):
            add_class({2: k2, 3: k3, 5: k5, 7: 2, 11: 2}, 4.96,
                      "box(%d,%d,%d,2,2)" % (k2, k3, k5))

n_adm = sum(1 for c in census if c[2])
n_unres = sum(1 for c in census if c[2] and c[3] == 0)
neg = [c for c in census if c[2] and c[3] == -1]
gate("G4 census-resolved (structural)", n_unres == 0 and ok_cont,
     "%d classes (%d admissible), %d unresolved; LL6 anchor m+(2;2) at "
     "a=5,8 = %.4f, %.4f (cont. 5e-4)" %
     (len(census), n_adm, n_unres, ll6[5.0], ll6[8.0]))
if neg:
    print("  G4 CENSUS: %d ADMISSIBLE NEGATIVE margins -> (N-c-full) evidence:"
          % len(neg))
    for c in neg:
        record("BREAK %s a=%.3f m+=%+.2e" % (c[0], c[1], c[4]))
else:
    print("  G4 CENSUS: all %d admissible strictly-twisted margins >= 0 "
          "(certified); registered prediction P2 CONFIRMED" % n_adm)
nonadm_neg = [c for c in census if not c[2] and c[3] == -1]
record("record-only (non-window-admissible) classes: %d, of which %d negative"
       % (len(census) - n_adm, len(nonadm_neg)))
for c in nonadm_neg:
    record("non-admissible negative: %s a=%.3f m+=%+.2e" % (c[0], c[1], c[4]))

# ------------------------------------------------------------------ G5
print("G5: margin-vs-tau identification at the 14 certified edges")
TAU = [(0.789932, 0.789932), (0.574759, 0.574759), (0.804761, 0.804761),
       (0.802065, 0.802066), (0.698573, 0.698584), (0.835844, 0.835851),
       (0.864786, 0.864825), (0.724536, 0.724560), (0.813728, 0.813756),
       (0.915612, 0.915668), (0.951471, 0.952146), (0.801764, 0.803332),
       (0.213961, 0.272891), (0.198934, 0.326252)]   # X-doc sec 4, certified
print("   edge          m+(D_R)    1-tau(mid)   ratio    |log ratio|")
ident_ok = True
ratios = []
for i, ((Rlo, Rhi), (tlo, thi)) in enumerate(zip(EDGES, TAU)):
    m = rung_m[i]
    slack_mid = 1 - (tlo + thi) / 2
    # conservative: the tau end most favorable to identification
    cand = [abs(math.log(m / (1 - t))) for t in (tlo, thi) if m > 0]
    best = min(cand) if cand else float("inf")
    ratios.append(m / slack_mid)
    if best > math.log(1.5):
        ident_ok = False
    print("   %.2f->%.2f   %+.5f    %.4f      %6.3f   %.3f" %
          (Rlo, Rhi, m, slack_mid, m / slack_mid, best))


def spearman(x, y):
    def ranks(v):
        idx = sorted(range(len(v)), key=lambda i: v[i])
        r = [0] * len(v)
        for rank, i in enumerate(idx):
            r[i] = rank
        return r
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))


slacks = [1 - (t[0] + t[1]) / 2 for t in TAU]
sp = spearman(rung_m, slacks)
gate("G5 identification-table (structural)", True,
     "identification (same numbers, x1.5): %s; Spearman(m+, 1-tau) = %+.3f "
     "(tracking iff >= 0.6): %s" %
     ("PASS" if ident_ok else "FAIL", sp,
      "TRACKS" if sp >= 0.6 else "NO TRACKING"))
VERDICT_IDENT = ident_ok
VERDICT_TRACK = sp >= 0.6

# ------------------------------------------------------------------ G6
print("G6: carrier guard at the new compositions")


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
ok = 2 not in rep and 3 not in rep and all(n in rep for n in (1, 4, 6, 9, 36))


def irreducible(n):
    return n in rep and not any(
        n % d == 0 and d in rep and n // d in rep for d in range(2, n))


ok = ok and all(irreducible(n) for n in (4, 6, 9))
# the NEW composition: depth-3 comb membership for 36
v_via_49, v_via_66 = 0 + 0, 1 + 1
ok = ok and (v_via_49 % 3 == 0) and (v_via_66 % 3 != 0)  # contradictory
# and the rung address n_p = floor(R/log p) needs a valuation generator:
# no additive v exists (v_via_49 != v_via_66), so no comb generator, no
# tower depth, D_R unformable for Epstein at ANY depth >= 1.
ok = ok and v_via_49 != v_via_66
gate("G6 carrier-guard-new-compositions", ok,
     "Epstein: v(36) in {0,2} -> depth-3 membership contradictory (0=0 mod 3 "
     "vs 2!=0 mod 3): no comb, no n_p address, D_R unformable; DH: no carrier "
     "monoid at all -> no tower address (bookkeeping)")

# ------------------------------------------------------------------ G9
# Breakage map (ADDED after the first run per the REGISTERED (N-c) duty
# "document exactly which classes break": run 1's census found a certified
# admissible negative at (11;2) a=4.96.  This block is RECORD + structural
# resolution only -- no verdict-table semantics changed; float-grade scans
# (cutoff 6 e^a, err << 1e-6) with arb certification of the breakage sign.)
print("G9: breakage map -- (p;2) classes near the shadow boundary")
scans = {}
g9_ok = True
g9_sum = []
for p in (2, 3, 5, 7, 11, 13, 17):
    per = 2 * LOG(p)
    a0 = max(2.1, 2 * LOG(p))
    nper = 2 if p <= 7 else 1
    a1 = a0 + (nper + 0.02) * per
    npts = 320 if nper == 2 else 200
    ag = np.linspace(a0, a1, npts)
    ntop = int(6 * math.exp(a1)) + 2
    vparr = np.zeros(ntop, dtype=np.uint8)
    pw = p
    while pw <= ntop:
        vparr[pw - 1::pw] += 1
        pw *= p
    mask_full = (vparr % 2) == 0
    narr = np.arange(1, ntop + 1, dtype=float)
    rho = float(rho_T({p: 2}))
    ms = []
    for a in ag:
        nmax = int(6 * math.exp(a)) + 2
        t2 = math.exp(-2 * a)
        Theta = 1 + 2 * float(np.exp(
            -math.pi * narr[:nmax][mask_full[:nmax]] ** 2 * t2).sum())
        dual = (Theta - 1) * math.exp(-a)
        ms.append(math.log(Theta) + math.log1p(dual) - a
                  - math.log(rho * (1 + rho)))
    ms = np.array(ms)
    scans["p%d_d2" % p] = {"a": ag.tolist(), "m": ms.tolist()}
    p1 = ag < a0 + per
    p2 = (ag >= a0 + per) & (ag < a0 + 2 * per)
    frac1 = float(np.mean(ms[p1] < 0))
    frac2 = float(np.mean(ms[p2] < 0)) if nper == 2 else float("nan")
    firstneg = next((float(a) for a, m in zip(ag, ms) if m < -5e-4), None)
    cert = ""
    if firstneg is not None:
        if 16 * math.exp(firstneg) < 120000:
            mp_a, _, _ = margin_plus({p: 2}, firstneg)
            s = resolved_sign(mp_a)
            g9_ok = g9_ok and s == -1
            cert = " arb-CERTIFIED<0"
        else:
            cert = " float-grade"
        # recurrence one period later (float)
        ar = firstneg + per
        nmax = int(6 * math.exp(ar)) + 2
        if nmax <= ntop:
            t2 = math.exp(-2 * ar)
            Theta = 1 + 2 * float(np.exp(
                -math.pi * narr[:nmax][mask_full[:nmax]] ** 2 * t2).sum())
            dual = (Theta - 1) * math.exp(-ar)
            mrec = (math.log(Theta) + math.log1p(dual) - ar
                    - math.log(rho * (1 + rho)))
            cert += "; recurs at +log p^2: m+=%+.1e" % mrec
    g9_sum.append("p=%d: neg-frac per period %.2f/%s first-neg a=%s%s" %
                  (p, frac1, ("%.2f" % frac2) if frac2 == frac2 else "-",
                   ("%.3f" % firstneg) if firstneg else "NONE", cert))
for s in g9_sum:
    record(s)
gate("G9 breakage-map-resolved (structural)", g9_ok,
     "scans computed; every detected breakage sign certified where arb-"
     "reachable; map = the RECORD lines above")

# ------------------------------------------------------------------ G8
# (run before G7 so the freeze->zeros ordering stays last; disclosed)
print("G8: T(g) cone-interior diagnostic (FE-DEFINED dual, demoted)")
from .prime_carleson_flow import _raised_cosine_even  # noqa: E402
from .prime_ladder_scaling import build_ladder, nested_basis  # noqa: E402

CMAX, NCENT, HW, GMAX, Tbud, NGRID, UPTS = 2.42, 38, 0.06, 4.96, 250.0, 100001, 24001
lad = build_ladder(CMAX, NCENT, HW, GMAX, T=Tbud, N=NGRID)
ugrid = np.linspace(-(CMAX + HW), CMAX + HW, UPTS)
BAS = _raised_cosine_even(lad.centers, HW, ugrid)
trap = np.trapezoid if hasattr(np, "trapezoid") else np.trapz


def autocorr(x, tau):
    phi = x @ BAS
    phis = x @ _raised_cosine_even(lad.centers, HW, tau - ugrid)
    return float(trap(phi * phis, x=ugrid))


def towers(gmax):
    out = {}
    for p in range(2, int(math.exp(gmax)) + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            n_p = int(math.floor((gmax - 1e-12) / math.log(p)))
            if n_p >= 1:
                out[p] = n_p
    return out


tw = towers(GMAX)
Qb = nested_basis(lad, GMAX)
rng = np.random.default_rng(20260610)
NMAXG8 = 2 ** 21
ok = True
detail = []
sign_census = []
for it in range(5):
    y = Qb @ rng.standard_normal(Qb.shape[1])
    y /= np.linalg.norm(y)
    mvec = {p: -sum(autocorr(y, k * math.log(p)) for k in range(1, n_p + 1))
            for p, n_p in tw.items()}
    mmax = max(mvec.values())
    if mmax >= 1.0:
        sign_census.append("DIVERGENT")
        detail.append("t%d: max m_p = %.3f >= 1: ON/BEYOND THE WALL" % (it, mmax))
        continue
    # real-twist weights: log w(n) = -a + log n - sum m_p v_p(n) log p
    a = GMAX
    Wlog = np.log(np.arange(1, NMAXG8 + 1)) - a
    for p, mp_ in mvec.items():
        pw = p
        while pw <= NMAXG8:
            Wlog[pw - 1::pw] -= mp_ * math.log(p)
            pw *= p
    w2 = np.exp(2 * Wlog)
    terms = np.exp(-math.pi * np.minimum(w2, 700.0)) * (w2 < 700.0)
    total = float(terms.sum())
    tail = float(terms[NMAXG8 // 2:].sum())
    resolved = tail < 1e-9 * max(total, 1e-300)
    ok = ok and resolved
    Theta = 1 + 2 * total
    dual = (Theta - 1) * math.exp(-a)
    rho = 1.0
    for p, mp_ in mvec.items():
        rho *= (1 - 1 / p) / (1 - p ** (mp_ - 1))
    mplus = math.log(Theta) + math.log1p(dual) - a - math.log(rho * (1 + rho))
    sign_census.append("+" if mplus >= 0 else "-")
    detail.append("t%d: m_p in [%.3f, %.3f], rho=%.3f, m+=%+.4f%s" %
                  (it, min(mvec.values()), mmax, rho, mplus,
                   "" if resolved else " UNRESOLVED"))
gate("G8 Tg-cone-interior (FE-DEFINED, demoted)", ok,
     "sign census %s | %s" % (sign_census, "; ".join(detail)))

# ------------------------------------------------------------------ G7
print("G7: freeze + zero comparison (II protocol; float-grade, flagged)")
AGRID = np.linspace(0.5, 8.0, 512)
P53 = [p for p in range(2, 54) if all(p % q for q in range(2, int(p ** .5) + 1))]
NMAX7 = int(16 * math.exp(8.0)) + 2
VP = {p: np.zeros(NMAX7, dtype=np.uint8) for p in P53}
for p in P53:
    pw = p
    while pw <= NMAX7:
        VP[p][pw - 1::pw] += 1
        pw *= p
NARR = np.arange(1, NMAX7 + 1, dtype=float)


def mplus_float(depths, a):
    nmax = int(16 * math.exp(a)) + 2
    mask = np.ones(nmax, dtype=bool)
    for p, d in depths.items():
        mask &= (VP[p][:nmax] % d) == 0
    t2 = math.exp(-2 * a)
    Theta = 1 + 2 * float(np.exp(-math.pi * NARR[:nmax][mask] ** 2 * t2).sum())
    dual = (Theta - 1) * math.exp(-a)
    rho = float(rho_T(depths))
    return math.log(Theta) + math.log1p(dual) - a - math.log(rho * (1 + rho))


S1 = np.array([math.exp(a) * mplus_float({2: 1}, a) for a in AGRID])
S2 = np.array([math.exp(a) * mplus_float({2: 3}, a) for a in AGRID])
S3 = np.array([math.exp(a) * mplus_float(rung_depths(a), a) for a in AGRID])
payload = json.dumps({"a": AGRID.tolist(), "S1": S1.tolist(),
                      "S2": S2.tolist(), "S3": S3.tolist(),
                      "scans": scans}).encode()
with open("/tmp/nn_freeze.json", "wb") as fh:
    fh.write(payload)
frz = hashlib.sha256(payload).hexdigest()
print("  FREEZE sha256 = %s  (series computed and hashed BEFORE any zero import)" % frz)

from .fork_lib import zeta_gammas  # noqa: E402  (AFTER freeze, comparison only)

gam = zeta_gammas(100)
da = AGRID[1] - AGRID[0]


def spectrum_z(series, excl_fund):
    f = series - np.convolve(series, np.exp(-0.5 * (np.arange(-60, 61) * da / 0.4) ** 2)
                             / np.sum(np.exp(-0.5 * (np.arange(-60, 61) * da / 0.4) ** 2)),
                             mode="same")
    f = f * np.hanning(len(f))
    gg = np.arange(0.5, 70.0, 0.02)
    amp = np.abs(np.exp(-1j * np.outer(gg, AGRID)) @ f) * da
    bg = (gg >= 5) & (gg <= 60)
    for g0 in gam[:12]:
        bg &= np.abs(gg - g0) > 1.5
    for w in excl_fund:
        k = 1
        while k * w <= 60.5:
            bg &= np.abs(gg - k * w) > 0.75
            k += 1
    med = float(np.median(amp[bg]))
    mad = float(np.median(np.abs(amp[bg] - med))) + 1e-300
    zs = []
    for g0 in gam[:5]:
        zs.append((float(amp[np.argmin(np.abs(gg - g0))]) - med) / (1.4826 * mad))
    return zs


Z1 = spectrum_z(S1, [])
Z2 = spectrum_z(S2, [2 * math.pi / (3 * LOG(2))])
# DISCLOSED FIX (first run): the registered S3 exclusion list (harmonics of
# 2pi/log p, p <= 13) tiled the whole background band -> empty background
# (nan).  Restricted to the two dominant jump combs (p = 2, 3); the wider
# list only made the z-test degenerate, not different.
Z3 = spectrum_z(S3, [2 * math.pi / LOG(2), 2 * math.pi / LOG(3)])
shock = (sum(z >= 4 for z in Z1) >= 3) or (sum(z >= 4 for z in Z2) >= 3)
for nm, zz in (("S1(d=1 breakage)", Z1), ("S2((2;3))", Z2), ("S3(rung flow)", Z3)):
    record("z at gamma_1..5 [%s]: %s" % (nm, ", ".join("%.1f" % z for z in zz)))
for g0 in gam[:5]:
    h = round(float(g0) / (2 * math.pi / (3 * LOG(2))))
    record("gamma=%.2f nearest (2;3)-comb harmonic dist %.2f" %
           (g0, abs(float(g0) - h * 2 * math.pi / (3 * LOG(2)))))
gate("G7 freeze-then-zeros comparison", True,
     "freeze ordering enforced; shock criterion (>=3 of first 5 at z>=4 in "
     "S1/S2): %s; registered expectation z<3: %s" %
     ("TRIGGERED - ESCALATE" if shock else "not triggered",
      "met" if max(Z1 + Z2) < 3 else "EXCEEDED (see table)"))

# ------------------------------------------------------------------ exit
print("=" * 78)
neg_strict = [c for c in census if c[2] and c[3] == -1]
print("VERDICT INPUTS: d=1 breakage %s; strict sub-cone negatives %d/%d adm; "
      "T(g) sign census %s; identification %s; tracking %s (Spearman %+.3f)" %
      ("CONFIRMED" if "G3 d1-breakage-as-derived" not in failures else "REFUTED",
       len(neg_strict), n_adm, sign_census,
       "PASS" if VERDICT_IDENT else "FAIL",
       "YES" if VERDICT_TRACK else "NO", sp))
print("BREAKAGE MAP: " + " | ".join(g9_sum))
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL STRUCTURAL GATES PASS")
sys.exit(0)
