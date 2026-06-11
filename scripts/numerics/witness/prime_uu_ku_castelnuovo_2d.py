"""UU-witness: the 2D WEIGHT x SCALE Castelnuovo posing on the ku face
(doc 36 stress item S3).

Registrations in research/work/UU-ku-castelnuovo.md secs 0-2, written
BEFORE the first run.  Exit 0 iff ALL gates pass.  Fail-closed: (U-b) and
(U-c) are full-value.  F-a: no zeta values/continuation; zeros ONLY via
fork_lib.zeta_gammas AFTER the sha256 freeze (UU6), comparison only.
flint arb prec 300 for decision quantities; Fractions for face identities
(entries are integer multiples of log p, checked at coefficient level);
float-grade (flagged) only in UU6 spectra and locus pre-scans.

Construction (doc secs 1.1-1.3): cell q = p^j, scale a >= log(q+1).
WEIGHT class W = d_j = [p^j] - [p^{j-1}] with candidate self-pairing
-m+(q, a) (PP's 1D margin standing in Lambda's slot, HH.1 sign).
SCALE family g_i = [q^i], i <= i_max = floor(a / log q) (window cap),
certified max-Gram <g_i, g_l> = (log q) max(i, l).
OVERRIDE posing F': certified d-frame face with <d_j, d_j> -> -m+.
APPEND posing: W bordered onto the unmodified face.
2D family entries (exact in the d-frame, i >= 1):
    A' = -m+,  B' = log p - m+,  C' = i log q + (log p - m+).
DISCRIMINANT inequality (the FF/Weil extraction transposed):
    (log p - m+)^2 <= m+ * (i_max log q + log 2).

Margin machinery copied verbatim from prime_pp_ku_face_index.py (PP,
ALL PASS), re-certified against PP's printed values in UU1.

Run: python3 -m scripts.numerics.witness.prime_uu_ku_castelnuovo_2d
"""

import hashlib
import json
import math
import sys
from fractions import Fraction

import flint
import numpy as np

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


# ------------------------------------------------------- primes (PP verbatim)
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


def j_of(q):
    p, j, m = prime_power(q), 0, q
    while m > 1:
        m //= p
        j += 1
    return j


# ----------------------------------------------- theta/margin (PP verbatim)
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


def margin(q, a):
    a = arb(a)
    D = D_q(q, a.exp())
    rho = arb(q - 2) / q
    return ((1 + a.exp() * D).log() + (1 + D).log() - a
            - (rho * (1 + rho)).log())


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


# ------------------------------------------------------------ 2D form pieces
LOG2 = arb(2).log()


def imax_arb(q, a):
    """floor(a / log q), arb-certified to exclude integer ties."""
    aa = arb(a)
    for _ in range(3):
        t = aa / arb(q).log()
        fl = math.floor(float(t.mid()))
        if resolved_sign(t - fl) > 0 and resolved_sign(arb(fl + 1) - t) > 0:
            return fl
        aa = aa + arb(1e-9)          # registered calibration nudge
    raise RuntimeError("imax tie unresolved at q=%d a=%s" % (q, a))


def disc_pair(q, a, m_arb):
    """(LHS, RHS, i_max) of the registered discriminant inequality."""
    Lp = arb(prime_power(q)).log()
    i = imax_arb(q, a)
    lhs = (Lp - m_arb) ** 2
    rhs = m_arb * (i * arb(q).log() + LOG2)
    return lhs, rhs, i


def disc_float(q, a, mf):
    Lp = math.log(prime_power(q))
    i = math.floor(a / math.log(q))
    lhs = (Lp - mf) ** 2
    rhs = mf * (i * math.log(q) + math.log(2.0))
    return lhs, rhs, i


# ---------------------------------------------------------------------- UU1
PRINTED = [  # (q, a, PP printed value)
    (121, 4.96, 6.4682e-3), (25, 3.26, 3.2728e-2), (9, 4.96, 8.9762e-3),
    (3, math.log(4), 0.557), (9, math.log(10), 0.107),
    (25, math.log(26), 3.270e-2), (121, math.log(122), 6.249e-3),
    (169, math.log(170), 4.448e-3),
]
ok = True
worst = 0.0
for q, a, ref in PRINTED:
    m = margin(q, a)
    rel = abs(float(m.mid()) - ref) / ref
    worst = max(worst, rel)
    ok = ok and rel < 2e-3 and resolved_sign(m) > 0
gate("UU1 inherited-margin re-certification", ok,
     "PP dual-route margins reproduced at 8 printed cells, worst rel "
     "%.1e (tol 2e-3); all arb-positive" % worst)

# ---------------------------------------------------------------------- UU2
# exact face identities, Fraction coefficients of log p
ok = True
N = 12
M = [[Fraction(max(i, j)) for j in range(N + 1)] for i in range(N + 1)]
for j in range(1, 5):
    d = [Fraction(0)] * (N + 1)
    d[j], d[j - 1] = Fraction(1), Fraction(-1)
    c = [sum(M[i][k] * d[k] for k in range(N + 1)) for i in range(N + 1)]
    ok = ok and c == [Fraction(1) if i <= j - 1 else Fraction(0)
                      for i in range(N + 1)]                  # c = M d_j
    ok = ok and sum(d[i] * c[i] for i in range(N + 1)) == -1  # d^T M d
# d-frame Gram: basis e_0, d_1..d_N
B = [[Fraction(0)] * (N + 1) for _ in range(N + 1)]
B[0][0] = Fraction(1)
for k in range(1, N + 1):
    B[k][k], B[k][k - 1] = Fraction(1), Fraction(-1)
for k in range(N + 1):
    for l in range(N + 1):
        v = sum(B[k][i] * M[i][jj] * B[l][jj]
                for i in range(N + 1) for jj in range(N + 1))
        if k == 0 and l == 0:
            ok = ok and v == 0
        elif k == 0 or l == 0:
            ok = ok and v == 1
        else:
            ok = ok and v == (-1 if k == l else 0)
gate("UU2a face identities (exact Fractions)", ok,
     "c = M d_j forced; d^T M d = -log p (HH.1); d-frame Gram "
     "(0 | L 1^T / L 1 | -L I) verified to N = 12, j <= 4")


def Fd_prime(q, m_arb, N):
    """Override d-frame Gram F' as arb matrix (basis e_0, d_1..d_N)."""
    Lp = arb(prime_power(q)).log()
    j = j_of(q)
    F = [[arb(0)] * (N + 1) for _ in range(N + 1)]
    for k in range(1, N + 1):
        F[0][k] = F[k][0] = Lp
        F[k][k] = -m_arb if k == j else -Lp
    return F


ok = True
worst = 0.0
for q, a in ((3, 2.0), (9, 5.0), (121, 5.0)):
    m = margin(q, a)
    j = j_of(q)
    Lp = arb(prime_power(q)).log()
    im = imax_arb(q, a)
    for i in (1, im):
        Nn = j * im + 2
        F = Fd_prime(q, m, Nn)
        W = [arb(0)] * (Nn + 1)
        W[j] = arb(1)                                   # W = d_j
        g = [arb(1)] + [arb(1) if 1 <= k <= j * i else arb(0)
                        for k in range(1, Nn + 1)]      # g_i = e_{ji}
        def quad(u, v):
            return sum(u[k] * F[k][l] * v[l]
                       for k in range(Nn + 1) for l in range(Nn + 1))
        A2, B2, C2 = quad(W, W), quad(W, g), quad(g, g)
        A1 = -m
        B1 = Lp - m
        C1 = i * arb(q).log() + (Lp - m)
        for x, y in ((A1, A2), (B1, B2), (C1, C2)):
            rel = abs(float((x - y).mid())) / max(abs(float(x.mid())), 1e-30)
            worst = max(worst, rel)
            ok = ok and rel < 1e-40
gate("UU2b 2D-family entries, two routes", ok,
     "A' = -m+, B' = log p - m+, C' = i log q + (log p - m+): d-frame "
     "expansion vs closed form, worst rel %.1e (tol 1e-40)" % worst)

# ---------------------------------------------------------------------- UU3
# (a) override posing: signature (1, N) via exact Schur chain + float eig
ok = True
for q in (3, 4, 5, 9, 25, 121):
    entry = math.log(q + 1)
    for a in (entry, entry + 1.0, 5.0, 8.0):
        if a < entry:
            continue
        m = margin(q, a)
        Lp = arb(prime_power(q)).log()
        j = j_of(q)
        for Nn in (4, 8, 12):
            # d-block diag: -Lp (N-1 times), -m once: ND iff m > 0
            ok = ok and resolved_sign(m) > 0
            S0 = Lp * Lp * ((Nn - 1) / Lp + 1 / m)      # e_0 Schur compl.
            ok = ok and resolved_sign(S0) > 0
            Ff = np.zeros((Nn + 1, Nn + 1))
            for k in range(1, Nn + 1):
                Ff[0][k] = Ff[k][0] = float(Lp.mid())
                Ff[k][k] = (-float(m.mid()) if k == j
                            else -float(Lp.mid()))
            ev = np.linalg.eigvalsh(Ff)
            ok = ok and int((ev > 0).sum()) == 1 and \
                int((ev < 0).sum()) == Nn
gate("UU3a override posing Lorentzian (1, N)", ok,
     "exact Schur chain (d-block ND for ANY m+ > 0; e_0 complement "
     "timelike) + float eig cross-check (flagged), q x a x N grid: the "
     "shape holds for any positive margin - it carries NO margin "
     "information")

# (b) append posing: Schur s = Lambda(q) - m+ > 0 on the full census
CENSUS = {}          # (q, a) -> margin arb
for q in CENSUS_Q:
    entry = math.log(q + 1)
    grid = [entry + 0.15 * jj for jj in range(20)]
    for aex in (5.0, 8.0):
        if aex >= entry and all(abs(aex - g) > 1e-9 for g in grid):
            grid.append(aex)
    for a in grid:
        CENSUS[(q, a)] = margin(q, a)
ok = True
npos = 0
for (q, a), m in CENSUS.items():
    s = arb(prime_power(q)).log() - m
    sg = resolved_sign(s)
    ok = ok and sg != 0
    npos += (sg > 0)
gate("UU3b append posing fails by the unpaid atom", ok and
     npos == len(CENSUS),
     "s = Lambda(q) - m+(q, a) arb-certified POSITIVE at %d/%d census "
     "cells: bordered signature (2, N), NOT Lorentzian; the shape "
     "verdict is posing-dependent and entry-determined in BOTH branches"
     % (npos, len(CENSUS)))

# ---------------------------------------------------------------------- UU4
ok = True
holds = []
fails_a4 = 0
for (q, a), m in sorted(CENSUS.items()):
    lhs, rhs, i = disc_pair(q, a, m)
    sg = resolved_sign(rhs - lhs)
    ok = ok and sg != 0
    if sg > 0:
        holds.append((q, round(a, 3)))
    elif a >= 4.0:
        fails_a4 += 1
corner = all(q in (3, 4, 8) and a < 4.0 for q, a in holds)
n_a4_holds = sum(1 for q, a in holds if a >= 4.0)
record("discriminant census holds (%d of %d): %s"
       % (len(holds), len(CENSUS), holds))
# deep ratio law
law_ok = True
for q in (3, 9, 121):
    m = CENSUS[(q, 8.0)]
    lhs, rhs, i = disc_pair(q, 8.0, m)
    r = lhs / rhs
    rho = arb(q - 2) / q
    Lp = arb(prime_power(q)).log()
    pred = rho * Lp * Lp * arb(8.0).exp() / (i * arb(q).log() + LOG2)
    dev = abs(float((r / pred - 1).mid()))
    law_ok = law_ok and dev < 0.05
    record("deep ratio q=%d a=8: r = %.4g, pred rho Lp^2 e^a/(i logq + "
           "log2) = %.4g, dev %.2g" % (q, float(r.mid()),
                                       float(pred.mid()), dev))
gate("UU4 discriminant census", ok and corner and n_a4_holds == 0 and
     law_ok,
     "all %d signs arb-resolved; holds confined to the small-q entry "
     "corner q in {3,4,8}, none at a >= 4; deep ratio law within 5%%"
     % len(CENSUS))

# ---------------------------------------------------------------------- UU5
# (a) the locus a*(q)
ok = True
astar = {}
for q in CENSUS_Q:
    entry = math.log(q + 1)
    grid = [entry + 0.001 + 0.01 * k for k in
            range(int((8.0 - entry) / 0.01))]
    sgn = []
    for a in grid:
        lhs, rhs, _ = disc_float(q, a, m_float(q, a))
        sgn.append(rhs > lhs)
    if any(sgn):
        last = max(k for k, s in enumerate(sgn) if s)
        astar[q] = grid[last]
for q in (3, 4):
    a_s = astar.get(q)
    okq = a_s is not None
    if okq:
        m1 = margin(q, a_s - 0.02)
        m2 = margin(q, a_s + 0.03)
        l1, r1, _ = disc_pair(q, a_s - 0.02, m1)
        l2, r2, _ = disc_pair(q, a_s + 0.03, m2)
        okq = resolved_sign(r1 - l1) > 0 and resolved_sign(l2 - r2) > 0
    ok = ok and okq
ok = ok and astar.get(3, 0) > 2.3 and astar.get(3, 9) < 2.6
ok = ok and astar.get(4, 0) > 2.8 and astar.get(4, 9) < 3.1
# empty for q >= 9 and q in {5, 7}: arb-certify fail at entry, at i_max
# jumps, and on a 0.5-step coarse grid
for q in [qq for qq in CENSUS_Q if qq >= 9 or qq in (5, 7)]:
    if q in astar:
        ok = False
        record("SURPRISE: locus nonempty at q=%d (a*=%.2f)" % (q, astar[q]))
        continue
    entry = math.log(q + 1)
    pts = [entry + 0.01]
    k = 1
    while k * math.log(q) < 8.0:
        if k * math.log(q) > entry:
            pts.append(k * math.log(q) + 0.01)
        k += 1
    a = entry + 0.25
    while a < 8.0:
        pts.append(a)
        a += 0.5
    for a in pts:
        lhs, rhs, _ = disc_pair(q, a, margin(q, a))
        ok = ok and resolved_sign(lhs - rhs) > 0
rec8 = ("a*(8) = %.3f" % astar[8]) if 8 in astar else "EMPTY"
record("locus: a*(3) = %s, a*(4) = %s; q = 8 (registered borderline): %s; "
       "all other census q: %s"
       % (astar.get(3), astar.get(4), rec8,
          "empty" if all(k in (3, 4, 8) for k in astar) else
          str({k: v for k, v in astar.items() if k not in (3, 4, 8)})))
if 8 in astar:
    m1 = margin(8, astar[8] - 0.02)
    l1, r1, _ = disc_pair(8, astar[8] - 0.02, m1)
    record("q=8 certify hold just below a*: sign(RHS-LHS) = %+d"
           % resolved_sign(r1 - l1))
gate("UU5a discriminant locus", ok,
     "a*(3), a*(4) in registered windows, arb-certified both sides; "
     "empty for q in {5, 7} and all q >= 9 (entry + i_max-jump + coarse "
     "grid, arb)")

# (b) the needed-depth wall
ok = True
for q in (3, 9, 121):
    m = CENSUS[(q, 8.0)]
    Lp = arb(prime_power(q)).log()
    rho = arb(q - 2) / q
    need = (Lp - m) ** 2 / m - LOG2          # i* log q
    dev = abs(float((need * arb(-8.0).exp() / (rho * Lp * Lp) - 1).mid()))
    ok = ok and dev < 0.05
    record("needed depth q=%d a=8: i* log q = %.1f (= %.4g e^a) vs "
           "available i_max log q = %.2f  [wall: e^a vs a]"
           % (q, float(need.mid()),
              float((need * arb(-8.0).exp()).mid()),
              imax_arb(q, 8.0) * math.log(q)))
gate("UU5b exponential-vs-linear depth wall", ok,
     "i* log q = rho_q Lambda_p^2 e^a (1 +- 5%) at a = 8, q in "
     "{3, 9, 121}: the quadratic step needs exponential Frobenius "
     "depth; the window supplies linear")

# ---------------------------------------------------------------------- UU6
print("UU6: freeze + zero comparison (II protocol; float-grade, flagged)")
AGRID = [0.5 + i * 7.5 / 511 for i in range(512)]


def ratio_series(q):
    out = []
    entry = math.log(q + 1)
    for a in AGRID:
        if a < entry:
            out.append(0.0)
            continue
        lhs, rhs, _ = disc_float(q, a, m_float(q, a))
        out.append(lhs / rhs)
    return out


T1 = ratio_series(3)
T2 = ratio_series(9)
T3 = []
for a in AGRID:
    tot = 0.0
    for q in PP_ALL:
        if q > 32 or a < math.log(q + 1):
            continue
        lhs, rhs, _ = disc_float(q, a, m_float(q, a))
        tot += math.log(prime_power(q)) * (rhs - lhs)
    T3.append(tot)
payload = json.dumps({"a": AGRID, "T1": T1, "T2": T2, "T3": T3,
                      "astar3": astar.get(3), "astar4": astar.get(4),
                      "astar8": astar.get(8)}).encode()
with open("/tmp/uu_freeze.json", "wb") as fh:
    fh.write(payload)
frz = hashlib.sha256(payload).hexdigest()
print("  FREEZE sha256 = %s  (series hashed BEFORE any zero import)" % frz)

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


Z1, Z2, Z3 = spectrum_z(T1), spectrum_z(T2), spectrum_z(T3)
for nm, zz in (("T1(r at q=3)", Z1), ("T2(r at q=9)", Z2),
               ("T3(assembled disc margin, staircase-exposed, record "
                "only)", Z3)):
    record("z at gamma_1..5 [%s]: %s" % (nm, ", ".join("%.1f" % z
                                                       for z in zz)))
shock = (sum(z >= 4 for z in Z1) >= 3) or (sum(z >= 4 for z in Z2) >= 3)
gate("UU6 freeze-then-zeros", True,
     "freeze ordering enforced; U-a shock criterion on T1/T2: %s; "
     "registered expectation z < 3 on T1/T2: %s" %
     ("TRIGGERED - ESCALATE (U-a), triple-check duty" if shock
      else "not triggered",
      "met" if max(Z1 + Z2) < 3 else "EXCEEDED (see table)"))

# ---------------------------------------------------------------------- UU7
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
ok = ok and 4 * 9 == 36 and 6 * 6 == 36 and (0 + 0) != (1 + 1)
gate("UU7 carrier-guard", ok,
     "Epstein 36 = 4*9 = 6*6, v(36) in {0,2}: no prime-power sieve -> "
     "no cell address (weight direction) AND no valuation -> no "
     "degree-separated family {q^i} (scale direction): BOTH 2D "
     "directions unformable; DH: no carrier monoid at all (bookkeeping)")

# ---------------------------------------------------------------------- UU8
for p in (2, 3, 5, 7, 11, 13):
    x = 1.0 / p
    h = math.log(p) / 4 - 2 * x / (1 - x) ** 2
    if h <= 0:
        record("t-window p=%d: w=1 certificate HOLE (halfwidth %.3f)"
               % (p, h))
    else:
        cells = [(q, a) for (q, a) in CENSUS if prime_power(q) == p]
        inside = sum(1 for (q, a) in cells
                     if float(CENSUS[(q, a)].mid()) < h)
        record("t-window p=%d: halfwidth %.3f; census margins inside: "
               "%d/%d" % (p, h, inside, len(cells)))
x = 1.0 / 9
record("w=2 spot p=3: halfwidth %.3f > 0 (W: w_0(3) = 2)"
       % (2 * math.log(3) / 4 - 2 * x / (1 - x) ** 2))
record("E-correction bound at q=9: 2x/(1-x)^2 = %.4f (x = 1/9); RHS "
       "shift O(E) vs log 2 = 0.693: recorded, no decision weight"
       % (2 * x / (1 - x) ** 2))

# ----------------------------------------------------------------------exit
print("=" * 78)
print("VERDICT INPUTS: shape posing-split (UU3): override (1,N) for any "
      "m+ > 0 / append (2,N) by s = Lambda - m+ > 0; discriminant census "
      "holds: %s; locus a*(3) = %s, a*(4) = %s, q=8: %s; depth wall "
      "exponential-vs-linear: %s; U-a shock: %s"
      % (len(holds), astar.get(3), astar.get(4),
         ("%.3f" % astar[8]) if 8 in astar else "empty",
         "UU5b PASS" if "UU5b exponential-vs-linear depth wall"
         not in failures else "FAIL",
         "no" if not shock else "YES"))
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL PASS (UU1-UU8)")
sys.exit(0)
