"""SS-witness: the ku-face inequality PROVED (doc 36 stress item S1).

Gates SS1-SS8 registered in research/work/SS-ku-inequality-proof.md sec 9,
written BEFORE the first run.  Exit 0 iff ALL gates pass.  Fail-closed.

Every gate certifies a PROOF-INTERNAL constant or estimate of the memo
(KK standard): Lemma C calculus constants, Lemma D master identity and
two-sided H bound, Theorem SS.2's F-algebra and floors on PP's full
527-point census, Corollary SS.2c entry floors, Theorem SS.3 deep-law
error bound, Lemma A carrier iff (exact integers), Theorem SS.1 FE two
routes, Theorem SS.4 evasion ceiling.

NO ZEROS CONSUMED: no fork_lib import, no freeze step needed (F-a holds
vacuously).  flint arb prec 600 (the deep SS2 grid points need ~1e-90
resolution); series truncated at term < 1e-185 with monotone tails;
inequality gates pass only if the arb ball RESOLVES them
(lower bound of the difference > 0).

Run: python3 -m scripts.numerics.witness.prime_ss_ku_inequality_proof
"""

import math
import sys

import flint

flint.ctx.prec = 600
arb = flint.arb

TRUNC = 1e-185
failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def record(msg):
    print("  RECORD", msg)


def cert_pos(x):
    """True iff the arb ball certifies x > 0."""
    return float(x.mid()) - float(x.rad()) > 0.0


def cert_small(x, tol):
    return abs(float(x.mid())) + float(x.rad()) < tol


def A(x):
    return x if isinstance(x, arb) else arb(x)


# ---------------------------------------------------------------- primes
def prime_power(n):
    if n < 2:
        return 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return p if m == 1 else 0
        p += 1
    return n


PP_ALL = [q for q in range(3, 360) if prime_power(q)]
CENSUS_Q = [q for q in PP_ALL if q <= 32] + [49, 64, 81, 121, 125, 128, 169]

# ------------------------------------------------------- series helpers
PI = arb.pi()


def T_sum(x):
    """T(x) = sum_{m>=1} e^{-pi m^2 x^2}."""
    x = A(x)
    s = arb(0)
    m = 1
    while True:
        term = (-PI * m * m * x * x).exp()
        s += term
        if float(term.mid()) < TRUNC:
            break
        m += 1
        if m > 10 ** 6:
            raise RuntimeError("T did not truncate")
    return s


def G_fn(x):
    """G(x) = 4 x T(x) = 2x(theta(x) - 1)."""
    x = A(x)
    return 4 * x * T_sum(x)


def K2_sum(x):
    """sum_{k>=1} k^2 e^{-pi k^2 x^2}."""
    x = A(x)
    s = arb(0)
    k = 1
    while True:
        term = k * k * (-PI * k * k * x * x).exp()
        s += term
        if float(term.mid()) < TRUNC:
            break
        k += 1
    return s


def S2_sum(q, x):
    """sum_{k>=1} sin^2(pi k/q) e^{-pi k^2 x^2}."""
    x = A(x)
    s = arb(0)
    k = 1
    while True:
        e = (-PI * k * k * x * x).exp()
        s += (PI * k / q).sin() ** 2 * e
        if float(e.mid()) < TRUNC:
            break
        k += 1
    return s


def jacobi_theta(x):
    """theta(x) = 1 + 2 T(x) (only ever called at x >= 1 here)."""
    x = A(x)
    if float(x.mid()) < 1.0:
        return (1 / x) * jacobi_theta(1 / x)
    return 1 + 2 * T_sum(x)


def D_q(q, u):
    """The coset dual D_q(u) (three-theta route, PP verbatim)."""
    u = A(u)
    uf = float(u.mid())
    s = arb(0)
    kmax = int(18.0 * q / uf) + 2
    for k in range(1, kmax + 1):
        e = (-PI * k * k * u * u / (q * q)).exp()
        if float(e.mid()) < TRUNC and k > 1:
            break
        s += (1 + (2 * PI * k / arb(q)).cos()) * e
    return jacobi_theta(u) - (2 + 2 * s) / q


def theta_comb_direct(q, t):
    """Direct comb sum over S_q = {w : w mod q not in {0, q-1}}."""
    t = A(t)
    nmax = int(16.0 / float(t.mid())) + 2
    s = arb(0)
    pit2 = PI * t * t
    for w in range(-nmax, nmax + 1):
        if (w % q) in (0, q - 1):
            continue
        s += (-pit2 * w * w).exp()
    return s


def margin_full(q, a):
    """Return (m+, D, H, F, rho, u) at (q, a)."""
    a = A(a)
    u = a.exp()
    rho = arb(q - 2) / q
    D = D_q(q, u)
    H = u * (D - rho)
    F = (1 + rho) + H * (1 + 2 * rho) + (H / u) * (1 + H)
    m = (1 + u * D).log() + (1 + D).log() - a - (rho * (1 + rho)).log()
    return m, D, H, F, rho, u


# ------------------------------------------------------------------- SS1
ok = True
ok &= cert_pos(PI.exp() - arb("23.1406"))                  # e^pi
tailC = 1 / (1 - (-3 * PI).exp())
ok &= cert_pos(arb("1.0001") - tailC)                      # tail factor
T1 = T_sum(1)
ok &= cert_pos(arb("0.0432185") - T1)                      # T(1)
G1v = G_fn(1)
ok &= cert_pos(arb("0.1729") - G1v)                        # G(1) < G1
ok &= cert_pos(arb("1.2e-21") - G_fn(4) / 2)               # G(4)/2
for xs in ("1", "2"):                                      # Lemma C(iv)
    x = arb(xs)
    ok &= cert_pos(arb("1.0004") * (-PI * x * x).exp() - K2_sum(x))
for xs in ("1", "1.3", "2", "4"):                          # Lemma C(i)
    x = arb(xs)
    ok &= cert_pos(arb("1.0001") * (-PI * x * x).exp() - T_sum(x))
G1 = arb("0.1729")                                         # the F chain
Fb = (1 + arb(1) / 3) - G1 * arb(5) / 3 - (G1 / 4) * (1 + arb("1.2e-21"))
ok &= cert_pos(Fb - arb("1.0019"))
record("e^pi = %.6f > 23.1406; T(1) = %.9f; G(1) = %.9f < 0.1729; "
       "F-chain lower bound = %.7f >= 1.0019; 1 - (3/2)G(1) = %.6f"
       % (float(PI.exp().mid()), float(T1.mid()), float(G1v.mid()),
          float(Fb.mid()), float((1 - arb(3) / 2 * G1v).mid())))
gate("SS1 proof-constants (Lemma C)", ok,
     "e^pi, tail factor, T(1), G(1), G(4)/2, k^2-tail, T-tail, F-chain "
     "all arb-certified at the proof's own values")

# ------------------------------------------------------------------- SS2
ok = True
worst_id = 0.0
for q in (9, 121):
    rho = arb(q - 2) / q
    for xs in ("0.5", "1", "1.5", "3"):                    # master identity
        x = arb(xs)
        u = q * x
        H1 = u * (D_q(q, u) - rho)                         # route 1 (dual)
        H2 = G_fn(u) / 2 - G_fn(x) + 4 * x * S2_sum(q, x)  # route 2 (Lemma D)
        d = H1 - H2
        worst_id = max(worst_id, abs(float(d.mid())) + float(d.rad()))
        ok &= cert_small(d, 1e-70)
for q in (3, 4, 5, 9, 25, 121, 169):                       # two-sided bound
    rho = arb(q - 2) / q
    for xr in (None, 1.5, 2.0, 4.0, 8.0):
        x = arb(q + 1) / q if xr is None else arb(xr)
        u = q * x
        H = u * (D_q(q, u) - rho)
        ok &= cert_pos(H + G_fn(x))                        # H >= -G(u/q)
        ok &= cert_pos(G_fn(u) / 2 - H)                    # H <= G(u)/2
grid = ["1", "1.25", "1.5", "2", "3", "5", "10"]           # G decreasing
for i in range(len(grid) - 1):
    ok &= cert_pos(G_fn(arb(grid[i])) - G_fn(arb(grid[i + 1])))
for q in (9, 121):                                         # Prop SS.5 bound
    for xs in ("1", "1.5", "3"):
        x = arb(xs)
        u = q * x
        rho = arb(q - 2) / q
        E = u * (D_q(q, u) - rho) + G_fn(x)                # = H + G(x) >= 0
        bnd = arb("1.0004") * PI * PI / (q * q) * G_fn(x) + G_fn(u) / 2
        ok &= cert_pos(E)
        ok &= cert_pos(bnd - E)
        if xs == "1":
            record("Prop SS.5 at q=%d, x=1: H+G = %.4e <= bound %.4e"
                   % (q, float(E.mid()), float(bnd.mid())))
gate("SS2 Lemma-D (master identity + two-sided H bound)", ok,
     "identity two routes worst |diff| = %.1e (< 1e-70); -G(u/q) <= H <= "
     "G(u)/2 certified on 35-point grid; G strictly decreasing; "
     "Prop SS.5 curvature bound certified" % worst_id)

# ------------------------------------------------------------------- SS3
ok = True
census = []
minF, minF_at = None, None
worst_alg = 0.0
for q in CENSUS_Q:
    entry = math.log(q + 1)
    agrid = [entry + j * 0.15 for j in range(20)]
    agrid += [a for a in (5.0, 8.0) if a >= entry]
    for af in agrid:
        a = arb(af)
        m, D, H, F, rho, u = margin_full(q, af)
        census.append((q, af, m, rho))
        z = F / (u * rho * (1 + rho))
        d = m - (1 + z).log()                              # the algebra (#)
        worst_alg = max(worst_alg, abs(float(d.mid())) + float(d.rad()))
        ok &= cert_small(d, 1e-60)
        ok &= cert_pos(F - arb("1.0019"))                  # F >= 1.0019
        if minF is None or float(F.mid()) < minF:
            minF, minF_at = float(F.mid()), (q, af)
        floor1 = (1 + (-a).exp() / (rho * (1 + rho))).log()
        ok &= cert_pos(m - floor1)                         # main floor
        ok &= cert_pos(m - arb(4) / 9 * (-a).exp())        # (4/9)e^-a
n_pts = len(census)
record("census n = %d; min F = %.5f at (q=%d, a=%.3f) >= 1.0019; "
       "algebra (#) worst |diff| = %.1e" %
       (n_pts, minF, minF_at[0], minF_at[1], worst_alg))
gate("SS3 Theorem-SS.2 on the full census", ok,
     "%d points: algebra (#) < 1e-60, F >= 1.0019, "
     "m+ >= log(1 + e^-a/(rho(1+rho))) >= (4/9)e^-a, all arb-resolved"
     % n_pts)

# ------------------------------------------------------------------- SS4
ok = True
qm_rows = []
for q in CENSUS_Q:
    entry = math.log(q + 1)
    m, D, H, F, rho, u = margin_full(q, entry)
    ok &= cert_pos(m - arb(1) / (3 * q))                   # 1/(3q) floor
    Gq = G_fn(arb(q + 1) / q)
    Fq = (1 + rho) - Gq * (1 + 2 * rho) \
        - (Gq / (q + 1)) * (1 + arb("1.2e-21"))
    floor_q = (1 + Fq / ((q + 1) * rho * (1 + rho))).log()
    ok &= cert_pos(m - floor_q)                            # refined floor
    qm_rows.append((q, q * float(m.mid()), float(m.mid()),
                    float(floor_q.mid())))
for q, qm, mv, fl in qm_rows:
    if q in (3, 9, 25, 121, 169):
        record("entry q=%d: m+ = %.4e (refined floor %.4e), q*m+ = %.4f"
               % (q, mv, fl, qm))
record("limit 1 - (3/2)G(1) = %.6f (Corollary SS.2c)"
       % float((1 - arb(3) / 2 * G1v).mid()))
gate("SS4 entry floors (1/(3q) + refined per-q)", ok,
     "both floors arb-certified at all %d census q; q*m+ recorded vs "
     "the 0.740696 limit" % len(CENSUS_Q))

# ------------------------------------------------------------------- SS5
ok = True
n5 = 0
tightest = None
for q in (3, 4, 5, 9, 25, 121):
    entry = math.log(q + 1)
    avals = sorted({entry, entry + 0.5, entry + 1.0} |
                   {a for a in (3.0, 5.0, 8.0) if a >= entry})
    for af in avals:
        a = arb(af)
        m, D, H, F, rho, u = margin_full(q, af)
        t = u * rho * m - 1
        rhs = arb("1.72") * G_fn(u / q) + arb("0.842") * (-a).exp() / rho
        ok &= cert_pos(rhs - t) and cert_pos(rhs + t)      # rhs > |t|
        n5 += 1
        slack = min(float((rhs - t).mid()), float((rhs + t).mid()))
        if tightest is None or slack < tightest[0]:
            tightest = (slack, q, af, float(t.mid()), float(rhs.mid()))
record("deep law: %d points; tightest at (q=%d, a=%.3f): deviation "
       "%+.4e vs bound %.4e (slack %.2e)" %
       (n5, tightest[1], tightest[2], tightest[3], tightest[4],
        tightest[0]))
gate("SS5 Theorem-SS.3 deep-law bound", ok,
     "|e^a rho m+ - 1| <= 1.72 G(e^a/q) + 0.842 e^-a/rho arb-certified "
     "at all %d points" % n5)

# ------------------------------------------------------------------- SS6
ok = True
crt_examples = []
for q in range(3, 301):
    R = {w for w in range(q) if (w * (w + 1)) % q == 0}
    if prime_power(q):
        ok &= (R == {0, q - 1})
    else:
        ok &= (R > {0, q - 1})                             # strict superset
        if len(crt_examples) < 3:
            extra = min(R - {0, q - 1})
            crt_examples.append("q=%d: w=%d" % (q, extra))
record("Lemma A iff exact on q in 3..300; first CRT witnesses: "
       + "; ".join(crt_examples))
gate("SS6 carrier-guard (Lemma A, exact integers)", ok,
     "{w : q | w(w+1)} == {0, q-1} iff q is a prime power, all q <= 300; "
     "prime power consumed HERE and only here")

# ------------------------------------------------------------------- SS7
ok = True
worst_fe = 0.0
for q, avals in ((3, (0.7, 2.0, 5.0)), (5, (0.7, 2.0)),
                 (9, (0.7, 2.0)), (121, (0.7, 2.0))):
    for af in avals:
        a = arb(af)
        lhs = theta_comb_direct(q, (-a).exp())
        rhs = a.exp() * D_q(q, a.exp())
        rel = abs(float((lhs - rhs).mid())) / abs(float(lhs.mid()))
        worst_fe = max(worst_fe, rel)
        ok &= rel < 1e-40
gate("SS7 Theorem-SS.1 FE two routes", ok,
     "Theta_q(e^-a) = e^a D_q(e^a), worst rel = %.1e (< 1e-40), "
     "no inhomogeneous term" % worst_fe)

# ------------------------------------------------------------------- SS8
ok = True
for q, af, m, rho in census:
    ceil = arb("1.298") * arb(-af).exp() / rho
    ok &= cert_pos(ceil - m)
deep = []
for q in (3, 4, 5, 9, 25):
    m, D, H, F, rho, u = margin_full(q, 8.0)
    deep.append("q=%d: %.5f" % (q, float((u * rho * m).mid())))
record("zero-slack limit e^8 rho m+(q,8): " + ", ".join(deep))
gate("SS8 Theorem-SS.4 evasion ceiling", ok,
     "m+ <= 1.298 e^-a/rho_q arb-certified at all %d census points; "
     "e^a rho m+ -> 1 recorded" % n_pts)

# ------------------------------------------------------------------ exit
print("=" * 78)
print("THEOREM INPUTS CERTIFIED: Lemma C constants (SS1); Lemma D identity "
      "+ bounds (SS2); Theorem SS.2 algebra/floors on %d census points "
      "(SS3, SS4); Theorem SS.3 error bound (SS5); Lemma A carrier iff "
      "(SS6); Theorem SS.1 FE (SS7); Theorem SS.4 ceiling (SS8)." % n_pts)
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (SS1-SS8)")
sys.exit(0)
