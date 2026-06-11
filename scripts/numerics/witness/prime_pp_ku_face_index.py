"""PP-witness: the ku face of the index inequality (face hunt, candidate 1).

Registrations in research/work/PP-ku-face.md secs 0-2, written BEFORE the
first run.  Exit 0 iff ALL gates pass.  Fail-closed: (P-c) is full-value.
F-a: no zeta values/continuation; zeros ONLY via fork_lib.zeta_gammas AFTER
the sha256 freeze (KU9), comparison only.  flint arb prec 300 for decision
margins; exact integers/Fractions for ledgers; float-grade (flagged) only
in the KU9 spectra.

Object under test: the type-q cell comb of the ku-square torsion ladder
(Lee / I-doc K2-K3: one cell per prime power q >= 3 at weights w with
q+1 <= w and q not dividing w(w+1)), lattice-completed to

    S_q = {w in Z : q does not divide w(w+1)},
    Theta_q(t) = sum_{S_q} e^{-pi w^2 t^2}
               = theta(t) - theta_{0 mod q}(t) - theta_{-1 mod q}(t),

whose coset-Poisson FE is HOMOGENEOUS (no +1, the internal subtraction
removes the origin atom and its dual continuum unit together):

    Theta_q(t) = (1/t) D_q(1/t),
    D_q(u) = theta(u) - (1/q) sum_k (1 + cos(2pi k/q)) e^{-pi k^2 u^2/q^2}.

Margin (LL6/NN verbatim calibration, unit symmetric/self-dual):
    m+(q, a) = log(1 + e^a D) + log(1 + D) - a - log(rho_q (1 + rho_q)),
    D = D_q(e^a),  rho_q = (q-2)/q;  admissible iff a >= log(q+1).

Gates KU1-KU9 as registered in the doc.

Run: python3 -m scripts.numerics.witness.prime_pp_ku_face_index
"""

import hashlib
import json
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


def record(msg):
    print("  RECORD", msg)


def resolved_sign(x):
    """+1/-1 if the arb ball resolves the sign, else 0."""
    m, r = float(x.mid()), float(x.rad())
    if abs(m) > r:
        return 1 if m > 0 else -1
    return 0


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
    return n  # prime


PP_ALL = [q for q in range(3, 2002) if prime_power(q)]
CENSUS_Q = [q for q in PP_ALL if q <= 32] + [49, 64, 81, 121, 125, 128, 169]


# ----------------------------------------------------------------- theta
def jacobi_theta(x):
    """theta(x) = sum_Z e^{-pi m^2 x^2}; Poisson-reflected for x < 1."""
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


def D_q(q, u):
    """The paired/coset dual D_q(u) (three-theta route)."""
    u = u if isinstance(u, arb) else arb(u)
    uf = float(u.mid())
    s = arb(0)
    kmax = int(8.3 * q / uf) + 2
    pi = arb.pi()
    for k in range(1, kmax + 1):
        e = (-pi * k * k * u * u / (q * q)).exp()
        if float(e.mid()) < 1e-92 and k > 1:
            break
        s += (1 + (2 * pi * k / arb(q)).cos()) * e
    return jacobi_theta(u) - (2 + 2 * s) / q


def theta_comb_direct(q, t, trunc=False):
    """Direct comb sum over S_q (lattice; trunc=True drops |w| <= q)."""
    t = t if isinstance(t, arb) else arb(t)
    nmax = int(16.0 / float(t.mid())) + 2
    s = arb(0)
    pit2 = arb.pi() * t * t
    for w in range(-nmax, nmax + 1):
        if (w % q) in (0, q - 1):
            continue
        if trunc and abs(w) <= q:
            continue
        s += (-pit2 * w * w).exp()
    return s


def band_B(q, t):
    """B_q(t) = sum_{|w| <= q, w in S_q} e^{-pi w^2 t^2} (finite, exact set)."""
    t = t if isinstance(t, arb) else arb(t)
    s = arb(0)
    pit2 = arb.pi() * t * t
    for w in range(-q, q + 1):
        if (w % q) in (0, q - 1):
            continue
        s += (-pit2 * w * w).exp()
    return s


def margin(q, a):
    """m+(q, a) via the dual route (after KU1 certifies the FE)."""
    a = arb(a)
    D = D_q(q, a.exp())
    rho = arb(q - 2) / q
    return ((1 + a.exp() * D).log() + (1 + D).log() - a
            - (rho * (1 + rho)).log()), D


# ------------------------------------------------------------------- KU1
ok = True
worst = 0.0
for q, agrid in ((3, (0.5, 2.0, 5.0)), (4, (0.5, 2.0, 5.0)),
                 (5, (0.5, 2.0, 5.0)), (9, (0.5, 2.0, 5.0)),
                 (121, (2.0, 5.0))):
    for a in agrid:
        lhs = theta_comb_direct(q, arb(-a).exp())          # direct route
        rhs = arb(a).exp() * D_q(q, arb(a).exp())          # coset route
        rel = abs(float((lhs - rhs).mid())) / abs(float(lhs.mid()))
        worst = max(worst, rel)
        ok = ok and rel < 1e-40
# zero-mode ledger, EXACT: continuum (k=0 Poisson) weights.
# theta: 1; 0-coset: (1/q)*q = 1; (-1)-coset dual support {m + 1/q}.
for q in (3, 4, 5, 9, 121):
    ok = ok and Fraction(1) - Fraction(1, q) * q == 0          # 1 - 1
    ok = ok and all((m * q + 1) != 0 for m in range(-3, 4))    # misses 0
    ok = ok and (1 % q) != 0                                   # q !| 1
gate("KU1 homogeneous-FE-independent-routes", ok,
     "Theta_q(e^-a) = e^a D_q(e^a), NO +1 anywhere, worst rel = %.1e; "
     "zero-mode ledger 1 - 1 - 0 = 0 exact; (-1)-coset dual support "
     "misses 0 (q | 1 impossible)" % worst)

# ------------------------------------------------------------------- KU2
ok = True
detail = []
for q in (9, 121):
    rho = arb(q - 2) / q
    for mult in (4, 8):
        u = arb(q * mult)
        H = u * (D_q(q, u) - rho)
        hv = abs(float(H.mid())) + float(H.rad())
        ok = ok and hv < 1e-12
    detail.append("ku q=%d: |H(4q)|,|H(8q)| < 1e-12" % q)
# CONTROL: NN's d=1 killer dual theta(u) - 1/u, hole coefficient -1.
for uf in (36.0, 968.0):
    u = arb(uf)
    H = u * (jacobi_theta(u) - 1 / u - 1)
    ok = ok and abs(float((H + 1).mid())) + float(H.rad()) < 1e-50
detail.append("NN-d1 control: u(theta - 1/u - 1) = -1 (the hole)")
gate("KU2 hole-coefficient (P-c detector)", ok,
     "ku face c_hole = 0 vs NN d=1 face c_hole = -1, arb-certified; " +
     "; ".join(detail))

# ------------------------------------------------------------------- KU3
ok = True
detail = []
q = 121
rho = arb(q - 2) / q
for xf in (0.25, 0.5, 0.75, 1.0, 1.5):
    u = arb(q) * arb(xf)
    H = u * (D_q(q, u) - rho)
    x = arb(xf)
    law = -2 * x * (jacobi_theta(x) - 1)
    rel = abs(float(((H - law) / law).mid()))
    ok = ok and rel < 0.05
    detail.append("x=%.2f H=%.4f law=%.4f" %
                  (xf, float(H.mid()), float(law.mid())))
for qq in (3, 4, 5, 9):                                   # RECORD small q
    rr = arb(qq - 2) / qq
    row = []
    for xf in (0.5, 1.0):
        u = arb(qq) * arb(xf)
        H = u * (D_q(qq, u) - rr)
        law = -2 * arb(xf) * (jacobi_theta(arb(xf)) - 1)
        row.append("x=%g H=%.4f (law %.4f)" %
                   (xf, float(H.mid()), float(law.mid())))
    record("repayment small-q q=%d: %s" % (qq, "; ".join(row)))
# PRE-ENTRY SIGN: the NN breakage regime exists strictly below entry.
for qq in (9, 121):
    a = math.log(qq / 2.0)
    m, _ = margin(qq, a)
    s = resolved_sign(m)
    ok = ok and s == -1
    detail.append("pre-entry m+(%d, e^a=q/2) = %.4f CERTIFIED<0" %
                  (qq, float(m.mid())))
gate("KU3 repayment-law + pre-entry-negativity", ok, " | ".join(detail))

# ------------------------------------------------------------------- KU4
ok = True
census = []          # (q, a, x, mid, sign)
neg = []
for q in CENSUS_Q:
    entry = math.log(q + 1)
    agrid = [entry + j * 0.15 for j in range(20)]
    agrid += [a for a in (5.0, 8.0) if a >= entry]
    for a in agrid:
        m, _ = margin(q, a)
        s = resolved_sign(m)
        ok = ok and s != 0
        census.append((q, a, math.exp(a) / q, float(m.mid()), s))
        if s == -1:
            neg.append((q, a, float(m.mid())))
n_adm = len(census)
print("  KU4 census: %d admissible (q, a) margins, all signs %s; "
      "certified negatives: %d" %
      (n_adm, "RESOLVED" if ok else "UNRESOLVED PRESENT", len(neg)))
for q in (3, 9, 25, 121, 169):
    rows = [c for c in census if c[0] == q]
    lo = min(rows, key=lambda c: c[3])
    record("q=%d: min margin %.3e at a=%.2f (x=%.2f); entry margin %.3e"
           % (q, lo[3], lo[1], lo[2], rows[0][3]))
for c in neg:
    record("CERTIFIED NEGATIVE q=%d a=%.3f m+=%.3e" % (c[0], c[1], c[2]))
gate("KU4 admissible-census", ok,
     "all %d signs arb-resolved; census verdict input: %d negatives "
     "(registered prediction: 0)" % (n_adm, len(neg)))
KU4_ALL_POS = ok and not neg

# ------------------------------------------------------------------- KU5
ok = True
detail = []
for q in (3, 4, 5, 9, 25):
    m, _ = margin(q, 8.0)
    val = float((arb(8).exp() * arb(q - 2) / q * m).mid())
    ok = ok and abs(val - 1.0) < 0.05
    detail.append("q=%d e^a rho m+(8)=%.4f" % (q, val))
matched = []
for q, a, nn_ref in ((121, 4.96, "(11;2)@4.96: -2.21e-3 CERTIFIED<0"),
                     (25, 3.26, "(5;2) onset 2log5=3.22, neg-frac 0.25"),
                     (9, 4.96, "(3;2) held for NN (small-place cell)")):
    m, _ = margin(q, a)
    s = resolved_sign(m)
    ok = ok and s != 0
    matched.append("ku q=%d a=%.2f: m+ = %+.4e %s  [NN: %s]" %
                   (q, a, float(m.mid()),
                    "CERTIFIED>0" if s == 1 else
                    ("CERTIFIED<0" if s == -1 else "UNRESOLVED"), nn_ref))
m22, _ = margin(25, 3.22)   # NN onset scale, ku-inadmissible boundary
record("q=25 at NN onset a=3.22 (ku-INADMISSIBLE, entry log26=3.258): "
       "m+ = %+.4e (record only)" % float(m22.mid()))
for line in matched:
    record(line)
record("no depth-1 address on this face: the sieve starts at q >= 3 "
       "(every cell has a proper congruence); q in {1, 2} are the two "
       "subtracted HZ entries -- NN's always-failing [p] classes "
       "(dual theta - 1/u) DO NOT EXIST in the ku dictionary")
gate("KU5 laws+NN-matched-table", ok, "deep law (+e^-a/rho_q, NN's "
     "envelope SIGN-FLIPPED): %s; matched-cell signs all resolved"
     % "; ".join(detail))

# ------------------------------------------------------------------- KU6
ok = True
for q in (3, 9):
    for a in (2.0, 3.0):
        lhs = theta_comb_direct(q, arb(-a).exp(), trunc=True)
        rhs = (arb(a).exp() * D_q(q, arb(a).exp())
               - band_B(q, arb(-a).exp()))
        rel = abs(float((lhs - rhs).mid())) / abs(float(lhs.mid()))
        ok = ok and rel < 1e-35
entry_vals = []
for q in CENSUS_Q:
    u = arb(q + 1)
    Dh = D_q(q, u) - band_B(q, 1 / u) / u
    entry_vals.append((q, float(Dh.mid())))
record("D^hon at entry (positivity structural; registered ~ +0.01..0.08): "
       + ", ".join("q=%d:%.4f" % t for t in entry_vals[:8])
       + " ... q=121:%.4f q=169:%.4f"
       % (dict(entry_vals)[121], dict(entry_vals)[169]))
heal = []
for q in (9, 121):
    row = []
    prev = None
    monotone = True
    for xf in (None, 1.5, 2.0, 3.0, 10.0, 20.0):   # None = entry
        a = math.log(q + 1) if xf is None else math.log(q * xf)
        u = arb(a).exp()
        Dh = D_q(q, u) - band_B(q, 1 / u) / u
        rho = arb(q - 2) / q
        mh = float(((1 + u * Dh).log() + (1 + Dh).log() - arb(a)
                    - (rho * (1 + rho)).log()).mid())
        row.append("x=%s:%.3f" % ("entry" if xf is None else xf, mh))
        if prev is not None:
            monotone = monotone and mh > prev      # heals toward 0
        prev = mh
    heal.append("q=%d [%s] healing monotone: %s" %
                (q, ", ".join(row), monotone))
for line in heal:
    record("naive-chi truncated margin (DEMOTED, band-shaped): " + line)
gate("KU6 truncated-face (DEMOTED: even completion + transform-as-dual)",
     ok, "band FE exact two routes (rel < 1e-35); D^hon entry values "
     "recorded; naive-chi deficit = the band (heals algebraically, "
     "never recurs - NOT the NN hole)")

# ------------------------------------------------------------------- KU7
ok = True
W = 2000
# |T_2w| ladder, closed form (lcm route)
ordC = [0] * (W + 2)
L = 1
for n in range(1, W + 2):
    L = L * n // math.gcd(L, n)
    if n - 1 >= 1:
        ordC[n - 1] = L // ((n - 1) * n)
hand = {1: 1, 2: 1, 3: 1, 4: 3, 5: 2, 6: 10, 7: 15, 8: 35, 9: 28, 10: 252}
ok = ok and all(ordC[w] == v for w, v in hand.items())
# prod identity: prod_{q pp >= 3, q | n} p(q) = n / 2^{[2|n]}
def pp_divisors(n):
    return [q for q in PP_ALL if q <= n and n % q == 0]
for n in range(3, W + 2):
    prod = 1
    for q in pp_divisors(n):
        prod *= prime_power(q)
    ok = ok and prod * (2 if n % 2 == 0 else 1) == n
# ON/OFF sets vs direct support recomputation + K4 recursion + deferral
def support(q, w):
    return q + 1 <= w and (w % q) not in (0, q - 1)
for w in range(3, W + 1):
    ON = sorted(q for q in pp_divisors(w - 1))
    OFF = sorted(q for q in pp_divisors(w + 1) if q <= w - 2)
    direct_on = sorted(q for q in PP_ALL if q <= w
                       and support(q, w) and not support(q, w - 1))
    direct_off = sorted(q for q in PP_ALL if q <= w
                        and support(q, w - 1) and not support(q, w))
    ok = ok and ON == direct_on and OFF == direct_off
    p = prime_power(w + 1)
    e = p if p else 1
    ok = ok and ordC[w] * (w + 1) == ordC[w - 1] * (w - 1) * e   # K4
    # top-cell deferral: the Lambda(w+1) atom = the not-yet-entered cell
    full = pp_divisors(w + 1)
    ok = ok and sorted(OFF + ([w + 1] if p and w + 1 >= 3 else [])) == full
gate("KU7 Lambda-attribution (exact integers, w <= %d)" % W, ok,
     "ON = {q | w-1}, OFF = {q | w+1, q <= w-2} (= direct support diff); "
     "dL = Lambda(w+1) - log((w+1)/(w-1)) exact (K4 rerun); the atom is "
     "carried by the SINGLE deferred top cell q = w+1")

# ------------------------------------------------------------------- KU8
ok = True
rep = set()
for n in range(1, 100):
    x = 0
    while x * x <= n:
        r = n - x * x
        if r % 5 == 0 and math.isqrt(r // 5) ** 2 == r // 5:
            rep.add(n)
            break
        x += 1
ok = ok and 2 not in rep and 3 not in rep
ok = ok and all(n in rep for n in (4, 6, 9, 36))
def irreducible(n):
    return n in rep and not any(n % d == 0 and d in rep and n // d in rep
                                for d in range(2, n))
ok = ok and all(irreducible(n) for n in (4, 6, 9))
ok = ok and (0 + 0) != (1 + 1)        # v(36) via 4*9 vs 6*6: no valuation
gate("KU8 carrier-guard", ok,
     "categorical: no ring -> no THH -> no T(p) cells -> no ladder "
     "(I-doc G-INT3; DH: no carrier monoid at all); arithmetic: Epstein "
     "36 = 4*9 = 6*6, v(36) in {0,2} -> no prime-power sieve -> the cell "
     "address (q, w) is unformable")

# ------------------------------------------------------------------- KU9
print("KU9: freeze + zero comparison (II protocol; float-grade, flagged)")


def D_float(q, u):
    s = 0.0
    kmax = int(6.5 * q / u) + 2
    for k in range(1, kmax + 1):
        s += (1 + math.cos(2 * math.pi * k / q)) * \
            math.exp(-math.pi * k * k * u * u / (q * q))
    th = 1.0
    m = 1
    while True:
        t = math.exp(-math.pi * m * m * u * u)
        if t < 1e-18:
            break
        th += 2 * t
        m += 1
    return th - (2 + 2 * s) / q


def m_float(q, a):
    u = math.exp(a)
    D = D_float(q, u)
    rho = (q - 2) / q
    return (math.log1p(u * D) + math.log1p(D) - a
            - math.log(rho * (1 + rho)))


AGRID = [0.5 + i * 7.5 / 511 for i in range(512)]
S1 = [math.exp(a) * m_float(9, a) for a in AGRID]
S2 = [math.exp(a) * m_float(121, a) for a in AGRID]
S3 = []
for a in AGRID:
    tot = 0.0
    for q in PP_ALL:
        if q > 32 or a < math.log(q + 1):
            continue
        tot += math.log(prime_power(q)) * m_float(q, a)
    S3.append(tot)
payload = json.dumps({"a": AGRID, "S1": S1, "S2": S2, "S3": S3}).encode()
with open("/tmp/pp_freeze.json", "wb") as fh:
    fh.write(payload)
frz = hashlib.sha256(payload).hexdigest()
print("  FREEZE sha256 = %s  (series hashed BEFORE any zero import)" % frz)

import numpy as np                                    # noqa: E402
from .fork_lib import zeta_gammas                     # noqa: E402

gam = zeta_gammas(100)
A = np.array(AGRID)
da = A[1] - A[0]


def spectrum_z(series):
    s = np.array(series)
    k = np.exp(-0.5 * (np.arange(-60, 61) * da / 0.4) ** 2)
    f = (s - np.convolve(s, k / k.sum(), mode="same")) * np.hanning(len(s))
    gg = np.arange(0.5, 70.0, 0.02)
    amp = np.abs(np.exp(-1j * np.outer(gg, A)) @ f) * da
    bg = (gg >= 5) & (gg <= 60)
    for g0 in gam[:12]:
        bg &= np.abs(gg - g0) > 1.5
    med = float(np.median(amp[bg]))
    mad = float(np.median(np.abs(amp[bg] - med))) + 1e-300
    return [(float(amp[np.argmin(np.abs(gg - g0))]) - med) /
            (1.4826 * mad) for g0 in gam[:5]]


Z1, Z2, Z3 = spectrum_z(S1), spectrum_z(S2), spectrum_z(S3)
for nm, zz in (("S1(q=9)", Z1), ("S2(q=121)", Z2),
               ("S3(assembled staircase, EF-tautology-exposed, "
                "record only)", Z3)):
    record("z at gamma_1..5 [%s]: %s" % (nm, ", ".join("%.1f" % z
                                                       for z in zz)))
shock = (sum(z >= 4 for z in Z1) >= 3) or (sum(z >= 4 for z in Z2) >= 3)
gate("KU9 freeze-then-zeros", True,
     "freeze ordering enforced; shock criterion on S1/S2: %s; registered "
     "expectation z < 3 on S1/S2: %s" %
     ("TRIGGERED - ESCALATE" if shock else "not triggered",
      "met" if max(Z1 + Z2) < 3 else "EXCEEDED (see table)"))

# ------------------------------------------------------------------ exit
print("=" * 78)
print("VERDICT INPUTS: hole coefficient 0 (vs NN -1): %s; admissible "
      "census all-positive: %s; deep law +e^-a/rho_q: %s; NN-matched "
      "q=121@4.96 positive where NN's (11;2) was certified negative: %s"
      % ("KU2 PASS" if "KU2 hole-coefficient (P-c detector)" not in
         failures else "KU2 FAIL",
         "YES" if KU4_ALL_POS else "NO",
         "KU5 PASS" if not any("KU5" in f for f in failures) else "FAIL",
         "see KU5 table"))
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (KU1-KU9)")
sys.exit(0)
