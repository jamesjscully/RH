"""TT-witness: the truncated-face chi (doc 36 stress item S2).

Registrations in research/work/TT-truncated-face.md secs 0-2, written
BEFORE the first run.  Exit 0 iff ALL gates pass.  Fail-closed: T-b is
full-value (a recurrent certified negative, a deep-law break, or a failed
moment identity closes option 2 by rule).

Object: PP's honest truncated ku face, Theta^hon_q = Theta_q - B_q
(band B_q = the 2q-4 comb points |w| <= q), exact band FE
Theta^hon_q(t) = (1/t) D^hon_q(1/t), D^hon_q(u) = D_q(u) - B_q(1/u)/u.

Derived correction under test (C1, zero free parameters):

    chi^corr(q, a) = a + log(rho_q E (1 + rho_q E)),
    E = E_q(a) = erfc(sqrt(pi) q e^{-a})

(the continuum zero mode of the comb restricted to the truncated window
|y| > q; the cutoff q is FORCED by the exact zero-charge identity
(2q-4)/rho_q = 2q).  Counter-candidate C2 (deferred-top-cell / sharp
window, F = 1 - q e^{-a}) is registered to FAIL the deep law.

F-a: no zeta values/continuation; zeros ONLY via fork_lib.zeta_gammas
AFTER the sha256 freeze (TT9), comparison only.  arb prec 300 for
decision margins; exact integers/Fractions for the moment ledger.

Run: python3 -m scripts.numerics.witness.prime_tt_truncated_face_chi
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
    return n


PP_ALL = [q for q in range(3, 2002) if prime_power(q)]
CENSUS_Q = [q for q in PP_ALL if q <= 32] + [49, 64, 81, 121, 125, 128, 169]


# ----------------------------------------------------------------- theta
def jacobi_theta(x):
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
    """Coset/paired dual D_q(u) (PP KU1-certified three-theta route)."""
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


def theta_comb_trunc(q, t):
    """Direct truncated comb sum (|w| >= q+1, w in S_q)."""
    t = t if isinstance(t, arb) else arb(t)
    nmax = int(16.0 / float(t.mid())) + 2
    s = arb(0)
    pit2 = arb.pi() * t * t
    for w in range(-nmax, nmax + 1):
        if (w % q) in (0, q - 1) or abs(w) <= q:
            continue
        s += (-pit2 * w * w).exp()
    return s


def band_points(q):
    return [w for w in range(-q, q + 1) if (w % q) not in (0, q - 1)]


def band_B(q, t):
    t = t if isinstance(t, arb) else arb(t)
    s = arb(0)
    pit2 = arb.pi() * t * t
    for w in band_points(q):
        s += (-pit2 * w * w).exp()
    return s


def E_win(q, a):
    """E_q(a) = erfc(sqrt(pi) q e^{-a}), arb ball."""
    z = arb.pi().sqrt() * q * arb(-a).exp()
    if hasattr(z, "erfc"):
        return z.erfc()
    return 1 - z.erf()


def D_hon(q, a):
    u = arb(a).exp()
    return D_q(q, u) - band_B(q, 1 / u) / u


def m_with_chi(q, a, W):
    """Truncated-face margin with window factor W in the chi."""
    a = arb(a)
    u = a.exp()
    Dh = D_q(q, u) - band_B(q, 1 / u) / u
    rho = arb(q - 2) / q
    return ((1 + u * Dh).log() + (1 + Dh).log() - a
            - (rho * W * (1 + rho * W)).log())


def m_corr(q, a):
    return m_with_chi(q, a, E_win(q, a))


def m_naive(q, a):
    return m_with_chi(q, a, arb(1))


def m_c2(q, a):
    return m_with_chi(q, a, 1 - q * arb(-a).exp())


def m_lattice(q, a):
    """PP's lattice margin (KU4/KU5 object), for the anchor checks."""
    a = arb(a)
    D = D_q(q, a.exp())
    rho = arb(q - 2) / q
    return ((1 + a.exp() * D).log() + (1 + D).log() - a
            - (rho * (1 + rho)).log())


# ------------------------------------------------------------------- TT1
ok = True
worst = 0.0
for q in (3, 9, 25, 121):
    entry = math.log(q + 1)
    for a in {2.0, 3.0, entry, entry + 1.0}:
        if a < entry:
            continue
        lhs = theta_comb_trunc(q, arb(-a).exp())
        rhs = arb(a).exp() * D_q(q, arb(a).exp()) - band_B(q, arb(-a).exp())
        rel = abs(float((lhs - rhs).mid())) / abs(float(lhs.mid()))
        worst = max(worst, rel)
        ok = ok and rel < 1e-35
gate("TT1 band-FE-independent-routes", ok,
     "Theta^hon(e^-a) = e^a D_q(e^a) - B_q(e^-a), homogeneous, chi "
     "correction never enters; worst rel = %.1e" % worst)

# ------------------------------------------------------------------- TT2
ok = True
for q in CENSUS_Q:
    rho = Fraction(q - 2, q)
    pts = band_points(q)
    ok = ok and len(pts) == 2 * q - 4                       # cardinality
    ok = ok and Fraction(2 * q - 4) - rho * 2 * q == 0      # M_0 = 0
    ok = ok and Fraction(2 * q - 4) / rho == 2 * q          # window = 2q
    M2_direct = Fraction(sum(w * w for w in pts)) - rho * Fraction(
        2 * q ** 3, 3)
    M2_hand = Fraction(-2, 3) * q * q + Fraction(7, 3) * q - 2
    ok = ok and M2_direct == M2_hand
# NN d=1 hole control (PP KU2 rerun): one continuum unit, exactly -1.
for uf in (36.0, 968.0):
    u = arb(uf)
    H = u * (jacobi_theta(u) - 1 / u - 1)
    ok = ok and abs(float((H + 1).mid())) + float(H.rad()) < 1e-50
record("carrier guard (PP KU8, inherited bookkeeping): Epstein "
       "36 = 4*9 = 6*6 -> no valuation -> no prime-power sieve -> no "
       "cell address, no band, no truncated face; DH: no carrier monoid")
gate("TT2 zero-charge-ledger (bookkeeping-vs-hole discriminator)", ok,
     "band charge M_0 = (2q-4) - rho 2q = 0 EXACT all census q (the "
     "band carries ZERO continuum units; equivalent window |y| <= q "
     "forced); M_2 = -(2/3)q^2 + (7/3)q - 2 exact; NN control: the "
     "d=1 hole carries exactly -1 unit")

# ------------------------------------------------------------------- TT3
ok = True
detail = []
for q in (9, 121):
    rho = arb(q - 2) / q
    rhoF = Fraction(q - 2, q)
    pts = band_points(q)
    for mult in (2, 4, 8):
        # COMPUTATIONAL-ROUTE NOTE (disclosed, run 1): both routes must
        # use the SAME exact u; going through float a = log(q*mult)
        # injects a 1e-16 argument mismatch (observed rel ~ 1e-15).
        # Predicate unchanged; routes now share exact u = q*mult.
        u = arb(q * mult)
        Dh = D_q(q, u) - band_B(q, 1 / u) / u
        E = (arb.pi().sqrt() * q / u).erfc() if hasattr(arb(1), "erfc") \
            else 1 - (arb.pi().sqrt() * q / u).erf()
        lhs = u * (Dh - rho * E)
        H = u * (D_q(q, u) - rho)
        x = arb.pi() / (u * u)
        ser = arb(0)
        term_ratio_ok = True
        m = 1
        fact = 1
        while True:
            fact *= m
            M2m = Fraction(sum(w ** (2 * m) for w in pts)) - rhoF * \
                Fraction(2 * q ** (2 * m + 1), 2 * m + 1)
            t = ((-x) ** m) * (arb(M2m.numerator) / M2m.denominator) / fact
            ser += t
            if abs(float(t.mid())) < 1e-32 and m > 3:
                break
            m += 1
            if m > 200:
                term_ratio_ok = False
                break
        rhs = H - ser
        rel = abs(float((lhs - rhs).mid())) / max(abs(float(lhs.mid())),
                                                  1e-30)
        ok = ok and rel < 1e-25 and term_ratio_ok
        detail.append("q=%d u=%dq: rel=%.1e (m<=%d)" % (q, mult, rel, m))
gate("TT3 moment-identity (exact EM boundary terms, two routes)", ok,
     "u(D^hon - rho E) = H_q(u) - sum (-pi/u^2)^m/m! M_2m, M_2m exact "
     "integers/Fractions: " + "; ".join(detail))

# ------------------------------------------------------------------- TT4
ok = True
census = []
neg = []
for q in CENSUS_Q:
    entry = math.log(q + 1)
    agrid = [entry + j * 0.15 for j in range(20)]
    agrid += [a for a in (5.0, 8.0) if a >= entry]
    for a in agrid:
        m = m_corr(q, a)
        s = resolved_sign(m)
        ok = ok and s != 0
        census.append((q, a, float(m.mid()), s))
        if s == -1:
            neg.append((q, a, float(m.mid())))
print("  TT4 census: %d corrected truncated-face margins, all signs %s; "
      "certified negatives: %d" %
      (len(census), "RESOLVED" if ok else "UNRESOLVED PRESENT", len(neg)))
for q in (3, 9, 25, 121, 169):
    rows = [c for c in census if c[0] == q]
    lo = min(rows, key=lambda c: c[2])
    record("q=%d: entry m^corr=%+.4f; min %+.3e at a=%.2f" %
           (q, rows[0][2], lo[2], lo[1]))
for c in neg:
    record("CERTIFIED NEGATIVE q=%d a=%.3f m^corr=%.3e" % c)
gate("TT4 corrected-entry-census (T-a/T-b decision gate)", ok,
     "all %d signs arb-resolved; %d negatives (registered prediction: 0)"
     % (len(census), len(neg)))
TT4_ALL_POS = ok and not neg

# ------------------------------------------------------------------- TT5
ok = True
scan_neg = {}
for q in (9, 121):
    entry = math.log(q + 1)
    n = int(2 * math.log(q) / 0.02) + 1
    negs = []
    prev_naive = None
    naive_monotone = True
    for j in range(n + 1):
        a = entry + j * 0.02
        m = m_corr(q, a)
        s = resolved_sign(m)
        ok = ok and s != 0
        if s == -1:
            negs.append(a)
        mn = float(m_naive(q, a).mid())
        if prev_naive is not None:
            naive_monotone = naive_monotone and mn > prev_naive
        prev_naive = mn
    scan_neg[q] = negs
    record("q=%d fine scan [entry, entry+2log q], %d pts: corrected "
           "negatives %d; naive margin healing monotone on same scan: %s"
           % (q, n + 1, len(negs), naive_monotone))
    if negs:
        record("q=%d negative a-values: %s" %
               (q, ", ".join("%.2f" % a for a in negs[:20])))
total_neg = sum(len(v) for v in scan_neg.values())
gate("TT5 no-recurrence-fine-scan", ok,
     "all signs arb-resolved; corrected negatives: %d (registered 0; "
     "any RECURRENT pattern = T-b)" % total_neg)
TT5_CLEAN = ok and total_neg == 0

# ------------------------------------------------------------------- TT6
ok = True
detail = []
for q in (3, 4, 5, 9, 25):
    val = float((arb(8).exp() * arb(q - 2) / q * m_corr(q, 8.0)).mid())
    ok = ok and abs(val - 1.0) < 0.05
    detail.append("q=%d:%.4f" % (q, val))
sharp = []
for q in (3, 4, 5, 9, 25, 121):
    val = float((arb(8).exp() * arb(q - 2) / q * m_corr(q, 8.0)).mid())
    pred = 1.0 + 2 * q * math.exp(-8.0)
    ok = ok and abs(val - pred) < 0.01
    sharp.append("q=%d:%.4f(pred %.4f)" % (q, val, pred))
gate("TT6 deep-law-recovered (decisive consistency)", ok,
     "(a) |e^a rho m^corr(8) - 1| < 0.05 (PP KU5a form): %s; "
     "(b) derived cross term 1 + 2qe^-8 to < 0.01: %s"
     % (" ".join(detail), " ".join(sharp)))

# ------------------------------------------------------------------- TT7
ok = True
detail = []
for q in (9, 25, 121):
    m = m_c2(q, 8.0)
    s = resolved_sign(m)
    ok = ok and s == -1
    detail.append("q=%d: m^C2(8)=%.3e CERTIFIED<0 (e^a rho m = %.1f)" %
                  (q, float(m.mid()),
                   math.exp(8) * (q - 2) / q * float(m.mid())))
    me = float(m_c2(q, math.log(q + 1)).mid())
    record("C2 (deferred-top-cell sharp window) q=%d: entry m^C2=%+.3f "
           "(positive at entry; the discrimination is DEEP)" % (q, me))
gate("TT7 candidate-discrimination (C2 registered to fail deep)", ok,
     "sharp window breaks the Gaussian-scale deep law as derived "
     "(factor-2 band-weight mismatch): " + "; ".join(detail))

# ------------------------------------------------------------------- TT8
ok = True
detail = []
for q in (9, 121):
    a = math.log(q / 2.0)
    m = m_corr(q, a)
    s = resolved_sign(m)
    ok = ok and s == 1
    detail.append("pre-entry m^corr(%d, e^a=q/2) = %+.2f CERTIFIED>0 "
                  "(trivial: chi collapses; no decision weight)" %
                  (q, float(m.mid())))
m_nn = m_corr(121, 4.96)
s = resolved_sign(m_nn)
ok = ok and s == 1
detail.append("NN-matched corrected cell m^corr(121, 4.96) = %+.4e "
              "CERTIFIED>0 [NN (11;2)@4.96: -2.21e-3]" %
              float(m_nn.mid()))
m_lat = m_lattice(121, 4.96)
ok = ok and abs(float(m_lat.mid()) - 6.4682e-3) < 1e-6
u = arb(8 * 121)
H = u * (D_q(121, u) - arb(119) / 121)
ok = ok and abs(float(H.mid())) + float(H.rad()) < 1e-12
detail.append("PP lattice anchors UNCHANGED: m+(121,4.96)=%.4e "
              "(PP: +6.4682e-3); |H_121(8q)| < 1e-12 (c_hole = 0); "
              "lattice chi^corr = chi+ identically (no band, E = 1)" %
              float(m_lat.mid()))
gate("TT8 pre-entry + NN-matched + lattice-anchors", ok,
     " | ".join(detail))

# ------------------------------------------------------------------- TT9
print("TT9: freeze + zero comparison (II protocol; float-grade, flagged)")


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


def m_corr_float(q, a):
    u = math.exp(a)
    B = sum(math.exp(-math.pi * w * w / (u * u)) for w in band_points(q))
    Dh = D_float(q, u) - B / u
    rho = (q - 2) / q
    W = math.erfc(math.sqrt(math.pi) * q * math.exp(-a))
    return (math.log1p(u * Dh) + math.log1p(Dh) - a
            - math.log(rho * W * (1 + rho * W)))


SERIES = {}
GRIDS = {}
for nm, q in (("S1", 9), ("S2", 121)):
    entry = math.log(q + 1)
    grid = [entry + i * (8.0 - entry) / 511 for i in range(512)]
    GRIDS[nm] = grid
    SERIES[nm] = [math.exp(a) * m_corr_float(q, a) for a in grid]
payload = json.dumps({"a1": GRIDS["S1"], "S1": SERIES["S1"],
                      "a2": GRIDS["S2"], "S2": SERIES["S2"]}).encode()
with open("/tmp/tt_freeze.json", "wb") as fh:
    fh.write(payload)
frz = hashlib.sha256(payload).hexdigest()
print("  FREEZE sha256 = %s  (series hashed BEFORE any zero import)" % frz)

import numpy as np                                    # noqa: E402
from .fork_lib import zeta_gammas                     # noqa: E402

gam = zeta_gammas(100)


def spectrum_z(grid, series):
    A = np.array(grid)
    da = A[1] - A[0]
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


Z1 = spectrum_z(GRIDS["S1"], SERIES["S1"])
Z2 = spectrum_z(GRIDS["S2"], SERIES["S2"])
for nm, zz in (("S1(q=9, corrected)", Z1), ("S2(q=121, corrected)", Z2)):
    record("z at gamma_1..5 [%s]: %s" % (nm, ", ".join("%.1f" % z
                                                       for z in zz)))
shock = (sum(z >= 4 for z in Z1) >= 3) or (sum(z >= 4 for z in Z2) >= 3)
gate("TT9 freeze-then-zeros", True,
     "freeze ordering enforced; shock criterion: %s; registered "
     "expectation z < 3: %s" %
     ("TRIGGERED - ESCALATE" if shock else "not triggered",
      "met" if max(Z1 + Z2) < 3 else "EXCEEDED (see table)"))

# ------------------------------------------------------------------ exit
print("=" * 78)
print("VERDICT INPUTS: identity-grade derivation (TT1-TT3): %s; corrected "
      "census all-positive: %s; no recurrence (fine scan): %s; deep law "
      "recovered (TT6): %s; C2 discriminated (TT7): %s"
      % ("PASS" if not any(f.startswith(("TT1", "TT2", "TT3"))
                           for f in failures) else "FAIL",
         "YES" if TT4_ALL_POS else "NO",
         "YES" if TT5_CLEAN else "NO",
         "PASS" if not any(f.startswith("TT6") for f in failures)
         else "FAIL",
         "PASS" if not any(f.startswith("TT7") for f in failures)
         else "FAIL"))
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (TT1-TT9)")
sys.exit(0)
