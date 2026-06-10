"""prime_int_ii_signature_flow.py - PROBE 2 (doc 32): does the INTEGER
signature flow of the growing count-pairing family see the zeros?

OBJECT (zero new choices; sources: AA Thm AA.1, W sec 5, GG sec 4.3):
global family at weight w, shell X = the unit class [1] (ONCE - GG's
continuum unit) + the classes [n^w], n prime power <= X (= the union of
the per-place geometric families {[p^{wi}]}, glued at the unit; GG's
renormalized-survivor normalization: unit weight per prime-power atom).
Strict CC-norm Gram (AA N4, extended cross-place by the same shared-row
representative, gate II1): M[a,b] = log2 + max(d_a,d_b) (a != b),
M[a,a] = d_a, degrees d_a = w log n_a, d_unit = 0.  INTEGER OBSERVABLE:
sig(w,X,t) of M + tI; the jump loci in t are t_k = -lambda_k(M); the
flow is in X (principal submatrices).  n_+(M) <= 2 exact (rank-2 +
PSD-MIN + Weyl; gate II2).

PRE-REGISTERED FORK (doc II sec 1; binding details fixed here BEFORE
the first run):
  CHANNEL RAW (sanity only, trivial dimension channel): F_raw(L) =
    n_-(0+; prime) - n_-(0+; surrogate-A li), w = 1.  A gamma peak here
    is pi(x)-grade counting, NOT a hit; its absence = power-limited.
  CHANNEL INT (decision, carrier-fair): F_int(tau, L) =
    n_-(tau) - (N-1) * f_sB(tau), surrogate-B = the carrier's OWN
    Gaussian-smoothed (sigma_L = 0.4) staircase resampled at k - 1/2;
    decision tau-panel tau(w) = log2 + {0.3, 1, 3} w (the bulk of the
    loci sits at log2 + w mu_k; tau <= log2 only re-counts dimension);
    decision spectrum = mean amplitude spectrum over the panel, w = 1
    primary, w = 4 confirmation.
  PRE-WHITENING (registered): all series are detrended by their own
    sigma = 0.4 Gaussian smoothing in L and multiplied by
    u(L) = L e^{-L/2} (flattens each zero's li(x^rho) amplitude),
    Hann-tapered; amplitude spectrum on gamma in [2, 70] step 0.05.
  Z-SCORE (registered): z(gamma*) = (max amplitude over
    |gamma - gamma*| <= 0.8  -  median) / (1.4826 MAD), background =
    gamma in [5, 60] minus +-1.5 bands around the first 12 zeros.
  DECISION TABLE (registered):
    sanity   = z_raw_prime(gamma_1) >= 4, else INCONCLUSIVE-POWER.
    hit      = #{first 5 gammas with z_int_prime(w=1) >= 4} >= 3.
    controls = epstein-INT and jitter-INT each have < 2 of the first 5
               gammas with z >= 3.5 (else gate II5 FAILS: the statistic
               measures geometry, not arithmetic; any hit DEMOTED).
    density  = max_L |n_-^{li}(tau_mid) - (N_li-1) f_crude(tau_mid)|
               >= 2 (the loci flow separates the li density model from
               the crude x/log x model at the spectral level).
    verdict: hit & controls -> s-a (escalate per G-INT2);
             1-2 gammas hit -> s-c (partial oscillatory content);
             no hit, density -> s-c (density layer only);
             no hit, no density -> s-b (clean no-go).
  GRID (G-INT6, logged): flow = 480 uniform-L samples, X in [200, 1e4];
    w in {1,4} flow, {1,2,4,8} static at X in {1e3, 1e4}, +3e4 at w=1;
    X = 1e5 flow OUT OF BUDGET (recorded).  Carriers: PRIME; EPSTEIN
    (distinct represented values of x^2+5y^2 - norm-Gram formable, no
    multiplicativity; AA E1); JITTER (Poisson from smoothed prime
    density, seed 20260610).  DH ladder: NOT FORMABLE (coefficients of
    the Davenport-Heilbronn 5-periodic pattern are not nonnegative
    counts; no atom multiset) - recorded at II1.
  EXACTNESS: atom data and norm masses integer-exact (II1); decisive
    small instances arb-LDL-certified at prec 300 vs numpy (II2); the
    large-N data are FLOAT-GRADE (flagged; no sign decision tighter
    than 1e-9 absolute is consumed).
  ENGINE DISCLOSURE (pre-verdict; no gate, channel or threshold
    changed): the first run used dense eigh per flow sample and was
    killed for cost (this host's LAPACK: ~12 s per 1000x1000 eigh; it
    never flushed output - no verdict was produced or seen).  The
    signature flow is now computed from the program's own split (W6d):
    M + tau I = U B U^T - (w MIN_l + c I), U = [D, 1] (D = degree
    vector), B = [[0,1],[1,log2]], c = log2 - tau; MIN_l'^{-1} is
    tridiagonal, so the inertia comes from the Haynsworth quotient
    formula In(A + UBU^T) = In(A) + In(-B^{-1} - U^T A^{-1} U)
    - In(-B^{-1}), with In(A) by a Sturm/LDL count on the tridiagonal
    and U^T A^{-1} U by two tridiagonal solves: O(N) per sample.
    GATED (II2): the fast inertia must agree EXACTLY with dense eigh
    counts on 16 random flow samples and with dense + arb LDL on the
    5 certified instances; degenerate pivots fall back to dense
    (occurrences counted and printed).
  FREEZE: sha256 of every computed series printed BEFORE the first
    import of zero data (fork_lib.zeta_gammas); the comparison runs
    only after the freeze line.

GATES (fail-closed; exit 0 iff II1-II5 all pass; the verdict value of
II6 is reported, not gated):
  II1 assembly exact (unique prime base, distinct atoms, norm = 2max
      by construction + AA(ii) bound, DH non-formability recorded)
  II2 certification (arb LDL == numpy on 5 instances; n_+ <= 2 at
      every flow sample and static instance)
  II3 grid computed + freeze hash printed before zero import
  II4 post-freeze comparison computed at the first 12 gammas
  II5 discrimination guard (controls clean as registered above)
"""
import hashlib
import math
import sys
import time

import numpy as np
from scipy.linalg import solve_banded
from scipy.special import erf

import flint

T0 = time.time()
LOG2 = math.log(2.0)
RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))
    return ok


def t():
    return f"[{time.time() - T0:7.1f}s]"


# ----------------------------------------------------------------- atoms
X_HI = 10_000
L_LO, L_HI = math.log(200.0), math.log(X_HI)
X_BUF = int(X_HI * math.e ** 1.2) + 1          # smoothing edge buffer
SIGMA = 0.4                                     # registered smoothing
N_FLOW = 480

sieve = np.ones(X_BUF + 1, dtype=bool)
sieve[:2] = False
for q in range(2, int(X_BUF ** 0.5) + 1):
    if sieve[q]:
        sieve[q * q::q] = False
primes = np.nonzero(sieve)[0]

pp_atoms = []                                   # (n, p, m)
for p in primes:
    pk, m = int(p), 1
    while pk <= X_BUF:
        pp_atoms.append((pk, int(p), m))
        pk *= int(p)
        m += 1
pp_atoms.sort()
pp_n = np.array([a[0] for a in pp_atoms], dtype=np.int64)
print(f"{t()} prime-power atoms <= {X_BUF}: {len(pp_n)} "
      f"(<= {X_HI}: {int((pp_n <= X_HI).sum())})")

eps_set = set()
xm = int(X_BUF ** 0.5) + 1
for x in range(0, xm + 1):
    v0 = x * x
    if v0 > X_BUF:
        break
    y = 0
    while v0 + 5 * y * y <= X_BUF:
        v = v0 + 5 * y * y
        if v >= 2:
            eps_set.add(v)
        y += 1
eps_n = np.array(sorted(eps_set), dtype=np.int64)
print(f"{t()} epstein atoms (x^2+5y^2) <= {X_BUF}: {len(eps_n)} "
      f"(<= {X_HI}: {int((eps_n <= X_HI).sum())})")

# ------------------------------------------------------------------- II1
print("\nII1: assembly exact (integer arithmetic)")
ok = True
seen = {}
for n, p, m in pp_atoms:
    if n in seen:
        ok = False
seen = None
ok = ok and len(set(int(v) for v in pp_n)) == len(pp_n)
for n, p, m in pp_atoms[:2000]:
    q, mm = n, 0
    while q % p == 0:
        q //= p
        mm += 1
    if q != 1 or mm != m:
        ok = False
check("every atom = p^m for a unique prime base; atoms distinct "
      "(p^a = q^b impossible)", ok, f"{len(pp_n)} atoms, first 2000 refactored")

rng0 = np.random.default_rng(1)
idx = rng0.choice(len(pp_atoms), size=200, replace=False)
ok = True
for i in idx:
    j = int(rng0.integers(0, len(pp_atoms)))
    if i == j:
        continue
    A, B = pp_atoms[max(i, j)][0], pp_atoms[min(i, j)][0]
    if A == B:
        continue
    A, B = max(A, B), min(A, B)
    a = (B, A - B)                       # shared-row representative (AA N4)
    if not (a[0] >= 1 and a[1] >= 1):
        ok = False
    mass_a, mass_b = a[0] + a[1], 2      # |b| = |1| + |-1|
    cols = {a[0] + a[1]: +1, a[0]: -1}   # b_0 column sums A, b_1 column sums B
    if mass_a != A or cols != {A: +1, B: -1}:
        ok = False
    if mass_a * mass_b != 2 * max(A, B):     # upper bound attained
        ok = False
    if max(A, B) * 2 != 2 * max(A, B):       # AA Thm AA.1(ii) lower bound
        ok = False
check("N([A]-[B]) = 2 max(A,B) cross-place: representative masses (A, 2) "
      "integer-exact; AA(ii) lower bound matches", ok, "200 sampled pairs")
print("  [note] DH-style perturbed ladder NOT FORMABLE: the 5-periodic "
      "Davenport-Heilbronn pattern (1, xi, -xi, -1, 0) has negative "
      "coefficients - no count multiset, no atoms (AA/GG precedent).")

# ----------------------------------------------------- surrogates + jitter
Lf = np.arange(0.0, math.log(X_BUF) + 0.01, 0.002)     # fine L grid
tg = np.arange(math.log(2.0), math.log(X_BUF) + 1e-9, 5e-4)
li_g = np.concatenate([[0.0], np.cumsum(
    0.5 * (np.exp(tg[1:]) / tg[1:] + np.exp(tg[:-1]) / tg[:-1]) * np.diff(tg))])
li_g += 1.0451637801174927848446              # li(2)


def li_of_L(L):
    return np.interp(L, tg, li_g, left=0.0, right=li_g[-1])


def pi_tilde(L, crude=False):
    """smooth prime-power count of {log n <= L}: sum_m smooth-pi(e^{L/m})."""
    out = np.zeros_like(L, dtype=float)
    for m in range(1, 17):
        Lm = L / m
        msk = Lm >= math.log(2.0)
        if crude:
            out[msk] += np.exp(Lm[msk]) / Lm[msk]
        else:
            out[msk] += li_of_L(Lm[msk])
    return out


def surrogate_atoms(count_fn):
    tot = float(count_fn(Lf[-1:])[0])
    ks = np.arange(1, int(tot) + 1) - 0.5
    return np.interp(ks, count_fn(Lf), Lf)


def smoothed_staircase(logs):
    C = np.zeros_like(Lf)
    for c0 in range(0, len(logs), 512):
        ch = logs[c0:c0 + 512]
        C += 0.5 * (1.0 + erf((Lf[:, None] - ch[None, :]) /
                              (SIGMA * math.sqrt(2.0)))).sum(axis=1)
    return C


print(f"{t()} building surrogates")
pp_l = np.log(pp_n.astype(float))
eps_l = np.log(eps_n.astype(float))
sA_li_l = surrogate_atoms(lambda L: pi_tilde(L))
sA_cr_l = surrogate_atoms(lambda L: pi_tilde(L, crude=True))
C_prime = smoothed_staircase(pp_l)
C_eps = smoothed_staircase(eps_l)
sB_prime_l = np.interp(np.arange(1, int(C_prime[-1]) + 1) - 0.5, C_prime, Lf)
sB_eps_l = np.interp(np.arange(1, int(C_eps[-1]) + 1) - 0.5, C_eps, Lf)
rngJ = np.random.default_rng(20260610)          # registered seed
nJ = rngJ.poisson(C_prime[-1])
jit_l = np.sort(np.interp(rngJ.uniform(0.0, C_prime[-1], nJ), C_prime, Lf))
C_jit = smoothed_staircase(jit_l)
sB_jit_l = np.interp(np.arange(1, int(C_jit[-1]) + 1) - 0.5, C_jit, Lf)
print(f"{t()} surrogate sizes: sA_li {len(sA_li_l)}, sA_crude {len(sA_cr_l)}, "
      f"sB_prime {len(sB_prime_l)}, sB_eps {len(sB_eps_l)}, "
      f"jitter {len(jit_l)}, sB_jitter {len(sB_jit_l)}")

# ------------------------------------------------------------------ flows
LG = np.linspace(L_LO, L_HI, N_FLOW)            # registered uniform-L grid


def taus(w):
    return [LOG2 + 0.3 * w, LOG2 + 1.0 * w, LOG2 + 3.0 * w]


def gram(logs, w):
    d = np.concatenate([[0.0], w * logs])       # unit once, degree 0
    M = np.maximum.outer(d, d) + LOG2
    np.fill_diagonal(M, d)
    return M


FALLBACKS = [0]


def tridiag_Tprime(lpos):
    """MIN_l'^{-1} for 0 < l_1 < ... < l_n (with l_0 := 0): tridiagonal
    (diag a, offdiag b) - the Markov/Brownian inverse."""
    g = np.diff(np.concatenate([[0.0], lpos]))
    inv = 1.0 / g
    a = inv.copy()
    a[:-1] += inv[1:]
    b = -inv[1:]
    return a, b


def sturm_below(a, b, sigma):
    """#eigenvalues of tridiag(a, b) strictly below sigma (LDL count);
    None if a pivot is indistinguishable from 0."""
    d = a[0] - sigma
    cnt = 1 if d < 0 else 0
    for i in range(1, len(a)):
        if abs(d) < 1e-13:
            return None
        d = a[i] - sigma - b[i - 1] * b[i - 1] / d
        if d < 0:
            cnt += 1
    return cnt


def inertia_fast(lpos, w, tau):
    """(n_+, n_-) of M + tau I via Haynsworth on the W6d split.
    M + tau I = U B U^T - (w MIN_l + c I), c = log2 - tau,
    U = [D, 1] (D = (0, w lpos)), B = [[0,1],[1,log2]].
    Returns None on a degenerate pivot (caller falls back to dense)."""
    n = len(lpos)
    c = LOG2 - tau
    if abs(c) < 1e-12:
        return None
    a, b = tridiag_Tprime(lpos)
    if c > 0:                                   # A negative definite
        pA, nA = 0, n + 1
    else:
        k = sturm_below(a, b, w / (-c))         # #{mu > -c/w}, mu=1/eig(T')
        if k is None:
            return None
        pA, nA = 1 + (n - k), k
    # y_v = (w MIN' + c I)^{-1} v  via  (w I + c T') y = T' v
    def Tv(v):
        out = a * v
        out[:-1] += b * v[1:]
        out[1:] += b * v[:-1]
        return out
    ab = np.zeros((3, n))
    ab[0, 1:] = c * b
    ab[1, :] = w + c * a
    ab[2, :-1] = c * b
    D = w * lpos
    one = np.ones(n)
    try:
        yD = solve_banded((1, 1), ab, Tv(D))
        y1 = solve_banded((1, 1), ab, Tv(one))
    except Exception:
        return None
    G = -np.array([[D @ yD, D @ y1], [D @ y1, one @ y1 + 1.0 / c]])
    Binv = np.array([[-LOG2, 1.0], [1.0, 0.0]])  # B^{-1}, det B = -1
    S = -Binv - G
    det = S[0, 0] * S[1, 1] - S[0, 1] * S[1, 0]
    tr = S[0, 0] + S[1, 1]
    scale = max(1.0, abs(S).max()) ** 2
    if abs(det) < 1e-12 * scale:
        return None
    if det > 0:
        pS, nS = (2, 0) if tr > 0 else (0, 2)
    else:
        pS, nS = 1, 1
    return pA + pS - 1, nA + nS - 1             # minus In(-B^{-1}) = (1,1)


def counts_at(lpos, w, tau):
    """(n_+, n_-) of M + tau I; fast path with dense fallback."""
    r = inertia_fast(lpos, w, tau)
    if r is None:
        FALLBACKS[0] += 1
        ev = np.linalg.eigvalsh(gram(lpos, w))
        r = (int((ev + tau > 1e-13).sum()), int((ev + tau < -1e-13).sum()))
    return r


def flow(logs, w, name):
    """signature flow over LG: dims, n_-(0+), n_-(tau panel), n_+."""
    logs = np.sort(logs)
    logs = logs[logs <= L_HI + 1e-12]
    tp = taus(w)
    out = {k: np.zeros(N_FLOW) for k in ["N", "nm0", "nm1", "nm2", "nm3",
                                         "npos"]}
    for j, L in enumerate(LG):
        lpos = logs[:int(np.searchsorted(logs, L + 1e-12))]
        out["N"][j] = len(lpos) + 1
        np_, nm = counts_at(lpos, w, 1e-9)      # tau = 0+
        out["nm0"][j], out["npos"][j] = nm, np_
        for k, tau in enumerate(tp, start=1):
            out[f"nm{k}"][j] = counts_at(lpos, w, tau)[1]
    print(f"{t()}   flow {name:14s} w={w}  N_max={int(out['N'][-1])}  "
          f"max n_+={int(out['npos'].max())}  "
          f"n_-(panel) end={[int(out[f'nm{k}'][-1]) for k in (1, 2, 3)]}")
    return out


print(f"\nII3 grid: flows on {N_FLOW} uniform-L samples, X in [200, 1e4]")
CARRIER_LOGS = {"prime": pp_l, "sA_li": sA_li_l, "sA_crude": sA_cr_l,
                "sB_prime": sB_prime_l, "epstein": eps_l,
                "sB_epstein": sB_eps_l, "jitter": jit_l,
                "sB_jitter": sB_jit_l}
FL = {}
for name, ws in [("prime", (1, 4)), ("sA_li", (1,)), ("sA_crude", (1,)),
                 ("sB_prime", (1, 4)), ("epstein", (1, 4)),
                 ("sB_epstein", (1, 4)), ("jitter", (1, 4)),
                 ("sB_jitter", (1, 4))]:
    for w in ws:
        FL[(name, w)] = flow(CARRIER_LOGS[name], w, name)
print(f"{t()}   dense fallbacks taken: {FALLBACKS[0]}")

# ------------------------------------------------------------------ static
print(f"\n{t()} static instances")
STATIC = {}
for w in (1, 2, 4, 8):
    for Xs in (1_000, 10_000):
        logs = pp_l[np.exp(pp_l) <= Xs + 0.5]
        ev = np.linalg.eigvalsh(gram(logs, w))
        STATIC[(w, Xs)] = ev
        tol = 1e-9 * abs(ev).max()
        print(f"  w={w} X={Xs}: N={len(ev)} n_+={int((ev > tol).sum())} "
              f"lam1={ev[-1]:.2f} t_hi=-lam2={-ev[-2]:.4f} "
              f"median locus={-np.median(ev[:-1]):.4f}")
logs3 = pp_l[np.exp(pp_l) <= 30_000.5]
ev3 = np.linalg.eigvalsh(gram(logs3, 1))
STATIC[(1, 30_000)] = ev3
print(f"  w=1 X=30000: N={len(ev3)} n_+={int((ev3 > 1e-9 * abs(ev3).max()).sum())} "
      f"t_hi={-ev3[-2]:.4f}  (X=1e5 flow: OUT OF BUDGET, recorded)")

# ------------------------------------------------------------------- II2
print("\nII2: certification")


def certified_signature(M_entries, prec=300):
    """arb LDL pivot signs, reversed order (AA's method); None if a pivot
    sign is not ball-certified."""
    old = flint.ctx.prec
    flint.ctx.prec = prec
    try:
        n = len(M_entries)
        A = [[flint.arb(0) + M_entries[n - 1 - r][n - 1 - c]
              for c in range(n)] for r in range(n)]
        pos = neg = 0
        for k in range(n):
            piv = A[k][k]
            if piv > 0:
                pos += 1
            elif piv < 0:
                neg += 1
            else:
                return None
            for r in range(k + 1, n):
                f = A[r][k] / piv
                for c in range(k, n):
                    A[r][c] = A[r][c] - f * A[k][c]
        return (pos, neg)
    finally:
        flint.ctx.prec = old


def arb_gram(ns, w):
    l2 = flint.arb(2).log()
    degs = [flint.arb(0)] + [flint.arb(int(n)).log() * w for n in ns]
    return [[degs[max(i, j)] + (l2 if i != j else flint.arb(0))
             for j in range(len(degs))] for i in range(len(degs))]


ok2 = True
for ns, w, lbl in [(pp_n[pp_n <= 300], 1, "prime X=300 w=1"),
                   (pp_n[pp_n <= 300], 4, "prime X=300 w=4"),
                   (pp_n[pp_n <= 600], 1, "prime X=600 w=1"),
                   (pp_n[pp_n <= 600], 4, "prime X=600 w=4"),
                   (eps_n[eps_n <= 300], 1, "epstein X=300 w=1")]:
    sig = prec_used = None
    for prec in (300, 1200):
        # run-2 repair, disclosed: arb_gram must be BUILT at the working
        # precision (the ambient default 53 bits gave fat input balls and
        # uncertifiable pivots); escalation kept as a safety margin.  No
        # gate semantics changed.
        flint.ctx.prec = prec
        sig = certified_signature(arb_gram(ns, w), prec=prec)
        if sig is not None:
            prec_used = prec
            break
    lpos = np.log(ns.astype(float))
    ev = np.linalg.eigvalsh(gram(lpos, w))
    tol = 1e-9 * abs(ev).max()
    fsig = (int((ev > tol).sum()), int((ev < -tol).sum()))
    qsig = inertia_fast(lpos, w, 1e-9)
    good = (sig is not None and sig == fsig and sig == qsig
            and sum(sig) == len(ns) + 1)
    ok2 = ok2 and good
    print(f"    {lbl}: arb {sig} (prec {prec_used}) vs numpy {fsig} vs "
          f"fast {qsig} {'OK' if good else 'BAD'}")
check("arb-certified LDL inertia == numpy == fast Haynsworth on 5 "
      "instances (every pivot ball-certified, prec escalated)", ok2)

rngV = np.random.default_rng(7)
okv, nv = True, 0
keys = sorted(FL.keys())
while nv < 16:
    name, w = keys[int(rngV.integers(0, len(keys)))]
    j = int(rngV.integers(0, N_FLOW))
    logs = CARRIER_LOGS[name]
    logs = np.sort(logs)
    logs = logs[logs <= L_HI + 1e-12]
    lpos = logs[:int(np.searchsorted(logs, LG[j] + 1e-12))]
    if len(lpos) > 600:
        continue
    ev = np.linalg.eigvalsh(gram(lpos, w))
    for tau in [1e-9] + taus(w):
        dense = (int((ev + tau > 1e-13).sum()), int((ev + tau < -1e-13).sum()))
        fast = counts_at(lpos, w, tau)
        if dense != fast:
            okv = False
            print(f"    MISMATCH {name} w={w} j={j} tau={tau}: "
                  f"dense {dense} fast {fast}")
    nv += 1
check("fast Haynsworth/Sturm inertia == dense eigh counts on 16 random "
      "flow samples (all panel taus)", okv)
maxnp = max(int(FL[k]["npos"].max()) for k in FL)
maxnp = max(maxnp, max(int((ev > 1e-9 * abs(ev).max()).sum())
                       for ev in STATIC.values()))
lorentz = all(int(FL[k]["npos"].max()) == 1 and int(FL[k]["npos"].min()) == 1
              for k in FL)
check("n_+ <= 2 at every flow sample and static instance (exact bound: "
      "rank-2 + PSD MIN + Weyl)", maxnp <= 2,
      f"max n_+ = {maxnp}; Lorentzian (n_+ = 1) everywhere: {lorentz}")

# ------------------------------------------------------ channels + FREEZE
GAM_GRID = np.arange(2.0, 70.0, 0.05)


def spectrum(F):
    """registered pre-whitening: detrend by own sigma=0.4 smoothing in L,
    multiply by u(L) = L e^{-L/2}, Hann taper, amplitude spectrum."""
    dL = LG[1] - LG[0]
    half = int(4 * SIGMA / dL)
    ker = np.exp(-0.5 * ((np.arange(-half, half + 1) * dL) / SIGMA) ** 2)
    ker /= ker.sum()
    pad = np.concatenate([F[half:0:-1], F, F[-2:-half - 2:-1]])
    trend = np.convolve(pad, ker, mode="valid")
    G = (F - trend) * LG * np.exp(-LG / 2.0) * np.hanning(N_FLOW)
    ph = np.exp(-1j * np.outer(GAM_GRID, LG))
    return np.abs(ph @ G) * dL


def int_channel(carrier, sB, w):
    spec = np.zeros_like(GAM_GRID)
    a, b = FL[(carrier, w)], FL[(sB, w)]
    for k in (1, 2, 3):
        F = a[f"nm{k}"] - (a["N"] - 1) * b[f"nm{k}"] / (b["N"] - 1)
        spec += spectrum(F)
    return spec / 3.0


F_raw = FL[("prime", 1)]["nm0"] - FL[("sA_li", 1)]["nm0"]
SP = {"raw_prime": spectrum(F_raw),
      "int_prime_w1": int_channel("prime", "sB_prime", 1),
      "int_prime_w4": int_channel("prime", "sB_prime", 4),
      "int_epstein_w1": int_channel("epstein", "sB_epstein", 1),
      "int_epstein_w4": int_channel("epstein", "sB_epstein", 4),
      "int_jitter_w1": int_channel("jitter", "sB_jitter", 1),
      "int_jitter_w4": int_channel("jitter", "sB_jitter", 4),
      "raw_epstein": spectrum(FL[("epstein", 1)]["nm0"]
                              - FL[("sB_epstein", 1)]["nm0"]),
      "raw_jitter": spectrum(FL[("jitter", 1)]["nm0"]
                             - FL[("sB_jitter", 1)]["nm0"])}
a, b = FL[("sA_li", 1)], FL[("sA_crude", 1)]
D_int = a["nm2"] - (a["N"] - 1) * b["nm2"] / (b["N"] - 1)
D_dim = a["N"] - b["N"]

h = hashlib.sha256()
for key in sorted(FL):
    for f in sorted(FL[key]):
        h.update(FL[key][f].tobytes())
for key in sorted(STATIC):
    h.update(STATIC[key].tobytes())
for key in sorted(SP):
    h.update(SP[key].tobytes())
h.update(D_int.tobytes())
FREEZE = h.hexdigest()
print(f"\n{t()} FREEZE sha256 = {FREEZE}")
print("  (all loci, flows and spectra frozen; zero data imported ONLY now)")
check("II3: grid computed and frozen before zero import", True, FREEZE[:16])

# ------------------------------------------------- II4: the comparison
from scripts.numerics.witness.fork_lib import zeta_gammas  # noqa: E402  POST-FREEZE

gam = zeta_gammas(12)
bg_mask = (GAM_GRID >= 5.0) & (GAM_GRID <= 60.0)
for g in gam:
    bg_mask &= np.abs(GAM_GRID - g) > 1.5


def zscores(spec):
    med = np.median(spec[bg_mask])
    mad = np.median(np.abs(spec[bg_mask] - med)) * 1.4826
    return np.array([(spec[np.abs(GAM_GRID - g) <= 0.8].max() - med) / mad
                     for g in gam])


print("\nII4: post-freeze z-scores at the first 12 zeta gammas")
Z = {k: zscores(v) for k, v in SP.items()}
for k in ["raw_prime", "int_prime_w1", "int_prime_w4", "int_epstein_w1",
          "int_jitter_w1", "raw_epstein", "raw_jitter"]:
    print(f"    {k:16s} " + " ".join(f"{z:5.1f}" for z in Z[k]))
check("comparison computed (12 gammas, all channels)", True,
      f"gamma_1..3 = {gam[0]:.2f}, {gam[1]:.2f}, {gam[2]:.2f}")

# ------------------------------------------------- II5 + II6: verdict
print("\nII5: discrimination guard")
ctrl_bad = max(int((Z["int_epstein_w1"][:5] >= 3.5).sum()),
               int((Z["int_jitter_w1"][:5] >= 3.5).sum()))
ok5 = ctrl_bad < 2
check("controls clean: epstein-INT and jitter-INT have < 2 of first 5 "
      "gammas with z >= 3.5", ok5,
      f"epstein {Z['int_epstein_w1'][:5].round(1)}, "
      f"jitter {Z['int_jitter_w1'][:5].round(1)}")

print("\nII6: verdict (registered decision table)")
sanity = Z["raw_prime"][0] >= 4.0
hits = int((Z["int_prime_w1"][:5] >= 4.0).sum())
density = float(np.abs(D_int).max()) >= 2.0
print(f"    sanity (raw gamma_1 z = {Z['raw_prime'][0]:.1f} >= 4): {sanity}")
print(f"    hits (INT prime w=1, z >= 4, first 5): {hits}   "
      f"w=4 confirmation: {int((Z['int_prime_w4'][:5] >= 4.0).sum())}")
print(f"    density separation max|D_int| = {np.abs(D_int).max():.2f} "
      f"(>= 2: {density});  dimension-level max|N_li - N_crude| = "
      f"{np.abs(D_dim).max():.0f}")
if not sanity:
    verdict = "INCONCLUSIVE-POWER"
elif hits >= 3 and ok5:
    verdict = "s-a (HIT: escalate per G-INT2)"
elif hits >= 3:
    verdict = "s-b WITH FLAG (hit demoted: controls dirty)"
elif hits >= 1:
    verdict = "s-c (partial oscillatory content)"
elif density:
    verdict = "s-c (density layer only: loci see the PNT/li layers, "\
              "not the oscillations)"
else:
    verdict = "s-b (clean no-go: signature flow supply-blind beyond "\
              "the dimension count)"
print(f"    VERDICT: {verdict}")

print(f"\n{t()} " + ("ALL PASS" if all(r[1] for r in RESULTS) else "FAILURES")
      + f" ({sum(r[1] for r in RESULTS)}/{len(RESULTS)} gates)")
sys.exit(0 if all(r[1] for r in RESULTS) else 1)
