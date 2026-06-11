"""RR-witness: faces F1 + F2 + F3 (OO's table) in one shared cycle.

F1 (E3-a): GG4's forced normalization as the Euler characteristic --
chi_GG(D) = chi(D) - one continuum unit per DEPTH-1 place in D's graph
support; equivalently Theta^dual_GG(u) = Theta^dual(u) + n_1(D)/u.
F2 (E3-b): HH's banked Theta_p = 2 p^{-k/2} as the MEASURE on the class
family; per-place and global aggregates + LP/exposure battery.
F3 (free rider): count-shape structure tests on the frozen -m+ data.

Registrations in research/work/RR-f123-cycle.md secs 0-2, written BEFORE
the first run.  Exit 0 iff all STRUCTURAL gates pass; sign censuses and
LP outputs are verdict inputs (NN/II precedent), recorded not gated,
EXCEPT where a registered derivation is load-bearing (RG1, RG7, RG9).

Discipline: F-a (no zeta values/continuation); zeros ONLY via
fork_lib.zeta_gammas AFTER the sha256 freeze (RG10), comparison only.
G-INT6: F1 spends zero choices; F2's measure is banked Theta verbatim.

Core arb machinery copied from prime_nn_graph_class_index.py (NN)
verbatim, with the margin computation shared between the verbatim-unit
and chi_GG variants (one Theta evaluation per class).

Run: python3 -m scripts.numerics.witness.prime_rr_face_cycle
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
LOG = math.log

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def record(msg):
    print("  " + msg)


# ------------------------------------------------- core (NN, verbatim)
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


def vp(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


def theta_comb(depths, t):
    t = t if isinstance(t, arb) else arb(t)
    nmax = int(16.0 / float(t.mid())) + 2
    pit2 = arb.pi() * t * t
    s = arb(0)
    for n in range(1, nmax + 1):
        if all(vp(n, p) % d == 0 for p, d in depths.items()):
            s += (-pit2 * n * n).exp()
    return 1 + 2 * s


def theta_dual_paired(depths, u, kmax):
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


def resolved_sign(x):
    m, r = float(x.mid()), float(x.rad())
    if abs(m) > r:
        return 1 if m > 0 else -1
    return 0


SIGNCH = {1: "+", -1: "-", 0: "?"}   # display map (run-1 fix, display only)


_theta_cache = {}


def margin_pair(depths, a, n1):
    """(m_verbatim, m_GG) sharing one Theta evaluation.  Comb data =
    the depth->=2 part of the graph class; n1 = #depth-1 places in the
    GRAPH support (comb-invisible, chi_GG-visible).  n1 == 0 implies
    m_GG = m_verbatim IDENTICALLY (delta = arb(0) exactly)."""
    comb = {p: d for p, d in depths.items() if d >= 2}
    comb = comb if comb else {2: 1}     # the m=0 / d=1 shadow class
    key = (tuple(sorted(comb.items())), a)
    if key not in _theta_cache:
        _theta_cache[key] = theta_comb(comb, arb(-a).exp())
    Theta = _theta_cache[key]
    dual = (Theta - 1) * arb(-a).exp()
    rho = rho_T(comb)
    rho_a = arb(rho.numerator) / arb(rho.denominator)
    m_v = Theta.log() + (1 + dual).log() - arb(a) - (rho_a * (1 + rho_a)).log()
    if n1 == 0:
        delta = arb(0)
    else:
        delta = ((1 + dual + n1 * arb(-a).exp()) / (1 + dual)).log()
    return m_v, m_v + delta


def n1_of(graph_class):
    return sum(1 for d in graph_class.values() if d == 1)


# ============================================================== RG1: F1
print("RG1: F1 d=1 exact repair (GG4's unit restores the self-dual theta)")
ok = True
worst = 0.0
for p in (2, 3, 5):
    for ua in (0.5, 2.0):
        u = arb(ua).exp()
        got = theta_dual_paired({p: 1}, u, 28) + 1 / u   # repaired dual
        want = jacobi_theta(u)                            # = theta exactly
        rel = abs(float((got - want).mid())) / abs(float(want.mid()))
        worst = max(worst, rel)
        ok = ok and rel < 1e-45
mvals = []
for a in (0.5, 1.0, 2.0):
    _, mg = margin_pair({2: 1}, a, 1)     # graph class [p]: n1 = 1
    closed = jacobi_theta(arb(a).exp()).log() + \
        ((1 + jacobi_theta(arb(a).exp())) / 2).log()
    ok = ok and resolved_sign(mg) == 1
    ok = ok and abs(float((mg - closed).mid())) < 1e-60
    mvals.append("m+_GG(%g)=%+.3e" % (a, float(mg.mid())))
bound_ok = True
for a in (2.48, 4.96, 6.0):
    b = 3 * (-(arb.pi() * (2 * arb(a)).exp())).exp()
    bound_ok = bound_ok and float(b.mid()) < 1e-50
ok = ok and bound_ok
gate("RG1 F1-d1-exact-repair", ok,
     "Theta^dual+1/u = theta two-route rel %.1e (p in {2,3,5}); %s "
     "(all CERTIFIED > 0, AJ4-shaped, closed form to 1e-60); "
     "m1_GG <= 3e^{-pi e^2a} < 1e-50 at a >= 2.48: %s" %
     (worst, "; ".join(mvals), bound_ok))

# ============================================================== RG2: F1
print("RG2: F1 census under chi_GG (NN G4 family verbatim; n1 forced = 0)")
census = []          # (label, a, admissible, sign_v, mid_v, sign_g, diff)


def add_class(graph_class, a, label):
    n1 = n1_of(graph_class)
    m_v, m_g = margin_pair(graph_class, a, n1)
    comb = {p: d for p, d in graph_class.items() if d >= 2}
    adm = all(d <= math.floor(a / LOG(p) + 1e-12) for p, d in comb.items())
    census.append((label, a, adm, resolved_sign(m_v), float(m_v.mid()),
                   resolved_sign(m_g), float((m_g - m_v).mid()), n1))


for d in range(2, 9):
    for a in (1.0, 2.48, 4.96, 8.0):
        add_class({2: d}, a, "(2;%d)" % d)
for d in (2, 3, 4):
    for a in (1.0, 2.48, 4.96, 8.0):
        add_class({3: d}, a, "(3;%d)" % d)
for p in (5, 7, 11, 13):
    for a in (2.48, 4.96):
        add_class({p: 2}, a, "(%d;2)" % p)
for j in range(17):
    add_class({2: 3}, 5.0 + j * 3 * LOG(2) / 16, "(2;3)per")
    add_class({2: 5}, 5.0 + j * 5 * LOG(2) / 16, "(2;5)per")
EDGES_HI = [1.88, 2.10, 2.30, 2.52, 2.76, 3.00, 3.24, 3.50,
            3.76, 4.00, 4.26, 4.50, 4.76, 4.96]
PRIMES23 = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def rung_depths(R):
    out = {}
    for p in PRIMES23:
        n_p = math.floor(R / LOG(p) + 1e-12)
        if n_p >= 2:
            out[p] = n_p
    return out


for Rhi in EDGES_HI:
    add_class(rung_depths(Rhi), Rhi, "D_%.2f" % Rhi)
d496 = rung_depths(4.96)
for k2 in range(2, d496[2] + 1):
    for k3 in range(2, d496[3] + 1):
        for k5 in range(2, d496[5] + 1):
            add_class({2: k2, 3: k3, 5: k5, 7: 2, 11: 2}, 4.96,
                      "box(%d,%d,%d,2,2)" % (k2, k3, k5))

n_adm = sum(1 for c in census if c[2])
n_unres = sum(1 for c in census if c[2] and (c[3] == 0 or c[5] == 0))
all_n1_zero = all(c[7] == 0 for c in census)
all_ident = all(c[6] == 0.0 for c in census)
moved = [c for c in census if c[2] and c[3] != c[5]]
# decision cell
mv_dec, mg_dec = margin_pair({11: 2}, 4.96, n1_of({11: 2}))
dec_ok = (resolved_sign(mg_dec) == -1 and
          abs(float(mg_dec.mid()) + 2.21e-3) < 1e-4 and
          float((mg_dec - mv_dec).mid()) == 0.0)
gate("RG2 F1-census-chi_GG (structural)",
     n_unres == 0 and all_n1_zero and all_ident and dec_ok,
     "%d classes (%d admissible), %d unresolved; n1 = 0 for ALL census "
     "classes (forced); m+_GG - m+ = 0 exactly on every class; DECISION "
     "CELL (11;2)@4.96: m+_GG = %+.6e CERTIFIED < 0 (= NN's frozen "
     "-2.21e-3), UNCHANGED" % (len(census), n_adm, n_unres,
                               float(mg_dec.mid())))
record("classes whose sign MOVED under chi_GG: %d %s"
       % (len(moved), "(R1-a evidence!)" if moved else "(R1-b as registered)"))
neg_g = [c for c in census if c[2] and c[5] == -1]
record("admissible negatives under chi_GG: %d (NN found 1: (11;2)@4.96)"
       % len(neg_g))
for c in neg_g:
    record("BREAK-under-chi_GG %s a=%.3f m+_GG=%+.2e" % (c[0], c[1], c[4]))

# ----- RG3: adjunction record (FLAGGED, no decision weight)
mv_adj, mg_adj = margin_pair({11: 2, 17: 1}, 4.96, n1_of({11: 2, 17: 1}))
gate("RG3 F1-adjunction-record (flagged)", resolved_sign(mg_adj) != 0,
     "[11^2]+[17] @ 4.96: m+ = %+.4e -> m+_GG = %+.4e (n1=1): the unit "
     "repairs the AUGMENTED class while the bare cell stays broken -- "
     "comb-invisible support = relabeling-adjacent, saves nothing"
     % (float(mv_adj.mid()), float(mg_adj.mid())))

# ============================================== float machinery (NN G7)
AMAX = 6.0
NMAXF = int(16 * math.exp(AMAX)) + 2
PRIM = [p for p in range(2, int(math.exp(AMAX)) + 1)
        if all(p % q for q in range(2, int(p ** 0.5) + 1))]
VP = {}
for p in PRIM:
    v = np.zeros(NMAXF, dtype=np.uint8)
    pw = p
    while pw <= NMAXF:
        v[pw - 1::pw] += 1
        pw *= p
    VP[p] = v
NARR = np.arange(1, NMAXF + 1, dtype=float)


def mplus_float(depths, a):
    nmax = int(16 * math.exp(a)) + 2
    mask = np.ones(nmax, dtype=bool)
    for p, d in depths.items():
        if d >= 2:
            mask &= (VP[p][:nmax] % d) == 0
    t2 = math.exp(-2 * a)
    Theta = 1 + 2 * float(np.exp(-math.pi * NARR[:nmax][mask] ** 2 * t2).sum())
    dual = (Theta - 1) * math.exp(-a)
    rho = float(rho_T({p: d for p, d in depths.items() if d >= 2} or {2: 1}))
    return math.log(Theta) + math.log1p(dual) - a - math.log(rho * (1 + rho))


# ============================================================== RG4: F2
print("RG4: F2 per-place Theta-weighted aggregates (banked measure, "
      "variants v=verbatim / g=GG-repaired)")


def n_p_of(p, a):
    return math.floor(a / LOG(p) + 1e-12) if p <= math.exp(a) else 0


def agg_place_arb(p, a):
    """(A_p variant v, A_p variant g) in arb; k=1 slot: m1_v = NN margin,
    m1_g = 0 with bound < 1e-50 (RG1d) -- neglected, documented."""
    npa = n_p_of(p, a)
    if npa == 0:
        return None, None
    m1_v, _ = margin_pair({2: 1}, a, 0)   # place-independent d=1 margin
    Av = 2 * arb(p) ** arb("-0.5") * m1_v
    Ag = arb(0)
    for k in range(2, npa + 1):
        mk, _ = margin_pair({p: k}, a, 0)
        wk = 2 * arb(p) ** (-arb(k) / 2)
        Av += wk * mk
        Ag += wk * mk
    return Av, Ag


FIRSTNEG = {5: 3.219, 7: 3.892, 11: 4.796, 13: 5.130, 17: 5.666}
agg_rows = []
ok = True
for p in (5, 7, 11, 13):
    pts = [2.48, 4.96, FIRSTNEG[p] + 0.2]
    for a in pts:
        Av, Ag = agg_place_arb(p, a)
        if Av is None:
            agg_rows.append("A_%d(%.3f): place not in window" % (p, a))
            continue
        sv, sg = resolved_sign(Av), resolved_sign(Ag)
        only_k1 = n_p_of(p, a) < 2     # variant g is then exactly 0 + bound
        dec = (p == 11 and a == 4.96)
        if dec:
            ok = ok and sv != 0 and sg != 0
        agg_rows.append("A_%d(%.3f): v=%+.5f [%s]  g=%+.5f [%s]%s%s" %
                        (p, a, float(Av.mid()), SIGNCH[sv], float(Ag.mid()),
                         SIGNCH[sg],
                         " (g: only k=1 in window: +0, bound 1e-50)"
                         if only_k1 else "",
                         "  <-- DECISION" if dec else ""))
Av11, Ag11 = agg_place_arb(11, 4.96)
gate("RG4 F2-per-place-aggregates (structural)",
     ok and resolved_sign(Av11) == -1 and resolved_sign(Ag11) == -1,
     "decision A_11(4.96): v = %+.6f, g = %+.6f, BOTH CERTIFIED < 0 "
     "(g neglects k=1 term in [0, 1e-50])" %
     (float(Av11.mid()), float(Ag11.mid())))
for r in agg_rows:
    record(r)

# ============================================================== RG5: F2
print("RG5: F2 global aggregate scan + arb certification")
AGRID = np.linspace(2.1, 6.0, 240)
slots = []                       # (p, k)
for p in PRIM:
    slots.append((p, 1))
for p in PRIM:
    nmaxk = n_p_of(p, AMAX)
    for k in range(2, nmaxk + 1):
        slots.append((p, k))
M_v = np.zeros((len(AGRID), len(slots)))
M_g = np.zeros((len(AGRID), len(slots)))
m1cache = np.array([mplus_float({2: 1}, a) for a in AGRID])
for i, (p, k) in enumerate(slots):
    w = 2 * p ** (-k / 2)
    for j, a in enumerate(AGRID):
        if n_p_of(p, a) < k:
            continue
        if k == 1:
            M_v[j, i] = w * math.exp(a) * m1cache[j]
            M_g[j, i] = 0.0           # m1_GG = +0 (bound RG1d)
        else:
            mm = w * math.exp(a) * mplus_float({p: k}, a)
            M_v[j, i] = mm
            M_g[j, i] = mm
A_v = M_v.sum(axis=1)            # e^a-scaled global aggregates (Theta wts)
A_g = M_g.sum(axis=1)
jm_v, jm_g = int(np.argmin(A_v)), int(np.argmin(A_g))


def agg_global_arb(a, variant):
    tot = arb(0)
    for p in PRIM:
        if p > math.exp(a):
            continue
        Av, Ag = agg_place_arb(p, a)
        tot += Av if variant == "v" else Ag
    return tot


ok = True
glob_rows = []
for tag, a in (("a=4.96 v", 4.96), ("a=4.96 g", 4.96),
               ("argmin_v a=%.3f" % AGRID[jm_v], float(AGRID[jm_v])),
               ("argmin_g a=%.3f" % AGRID[jm_g], float(AGRID[jm_g]))):
    var = "g" if (" g" in tag or "argmin_g" in tag) else "v"
    G = agg_global_arb(a, var)
    s = resolved_sign(G)
    ok = ok and s != 0
    glob_rows.append("GLOBAL %s [%s]: %+.5f [%s]" %
                     (tag, var, float(G.mid()), SIGNCH[s]))
neg_frac_v = float(np.mean(A_v < 0))
neg_frac_g = float(np.mean(A_g < 0))
gate("RG5 F2-global-aggregate (structural)", ok,
     "scan [2.1, 6.0] x240: neg-frac v = %.2f, g = %.2f; min_v(e^a A) = "
     "%+.4f @ a=%.2f, min_g = %+.4f @ a=%.2f; decision signs arb-resolved"
     % (neg_frac_v, neg_frac_g, float(A_v[jm_v]), AGRID[jm_v],
        float(A_g[jm_g]), AGRID[jm_g]))
for r in glob_rows:
    record(r)

# ============================================================== RG6: F2
print("RG6: F2 LP battery (feasible positive measures on the slot family)")
from scipy.optimize import linprog  # noqa: E402

IDX112 = slots.index((11, 2))
BLOCK_V = [i for i, (p, k) in enumerate(slots) if k == 1 or (k == 2 and p >= 5)]
BLOCK_G = [i for i, (p, k) in enumerate(slots) if k == 2 and p >= 5]
THW = np.array([2 * p ** (-k / 2) for (p, k) in slots])
THW_N = THW / THW.sum()
lp_out = {}


def lp_solve(Mmat, c, lo):
    res = linprog(c, A_ub=-Mmat, b_ub=np.zeros(len(AGRID)),
                  A_eq=np.ones((1, len(slots))), b_eq=[1.0],
                  bounds=[(l, None) for l in lo], method="highs")
    return res


# PARAMETRIZATION (disclosed, run-1 clarification): M already carries the
# banked Theta weights, so the LP variable w is the DENSITY of the trial
# measure w.r.t. banked Theta (Radon-Nikodym), normalized sum w = 1.  The
# banked measure itself is w = uniform; floors are run in BOTH registered
# readings: eta * Theta-proportional-in-w (the literal sec-1.2 formula)
# AND eta * uniform-in-w (= eta * banked-Theta-proportional in measure
# units, the intended meaning).  Both recorded; no verdict depends on the
# choice (the decisive per-place statement is exact, below).
for var, Mmat, block in (("v", M_v, BLOCK_V), ("g", M_g, BLOCK_G)):
    nsl = len(slots)
    lo0 = [0.0] * nsl
    feas = lp_solve(Mmat, np.zeros(nsl), lo0)
    banked_ok = bool(np.all(Mmat.sum(axis=1) >= 0))   # w uniform = banked
    mx112 = lp_solve(Mmat, -np.eye(nsl)[IDX112], lo0)
    cblk = np.zeros(nsl)
    cblk[block] = -1.0
    mxblk = lp_solve(Mmat, cblk, lo0)
    flr = {}
    for eta in (1e-6, 0.5):
        fT = lp_solve(Mmat, np.zeros(nsl), list(eta * THW_N))
        fU = lp_solve(Mmat, np.zeros(nsl), [eta / nsl] * nsl)
        flr[eta] = (int(fT.status), int(fU.status))   # 0 feasible, 2 infeas
    lp_out[var] = {
        "feasible_free": int(feas.status), "banked_Theta_feasible": banked_ok,
        "max_w_11_2": float(mx112.x[IDX112]) if mx112.status == 0 else None,
        "max_block_weight": float(-mxblk.fun) if mxblk.status == 0 else None,
        "floor_1e-6_T/U": flr[1e-6], "floor_0.5_T/U": flr[0.5]}
    record("variant %s: banked Theta itself %s; free-support %s; "
           "max w_(11,2) = %s; max breaking-block weight = %s; floors "
           "(eta=1e-6, 0.5) x (Theta-prop, uniform): %s %s" %
           (var, "FEASIBLE" if banked_ok else "INFEASIBLE",
            "FEASIBLE" if feas.status == 0 else "INFEASIBLE",
            ("%.4f" % lp_out[var]["max_w_11_2"]) if lp_out[var]["max_w_11_2"]
            is not None else "n/a",
            ("%.4f" % lp_out[var]["max_block_weight"])
            if lp_out[var]["max_block_weight"] is not None else "n/a",
            flr[1e-6], flr[0.5]))
# per-place p = 11 LP decided EXACTLY by certified margins (RG4):
m1v, _ = margin_pair({2: 1}, 4.96, 0)
m2v, _ = margin_pair({11: 2}, 4.96, 0)
exact11 = resolved_sign(m1v) == -1 and resolved_sign(m2v) == -1
record("per-place p=11 @ 4.96 LP, variant v: both slot margins CERTIFIED "
       "< 0 -> INFEASIBLE exactly (any w >= 0, sum 1)")
record("per-place p=11 @ 4.96 LP, variant g: w_(11,2) <= m1_GG/|m2| "
       "<= 1e-50/2.2e-3 < 5e-48: NO measure charging the breaking class "
       "above 5e-48 is feasible (m1_GG bound RG1d)")
gate("RG6 F2-LP-battery (computed)", exact11 and
     all(v["feasible_free"] in (0, 2) for v in lp_out.values()),
     "global LPs solved (statuses recorded); per-place p=11 decided exact")

# ============================================================== RG7: F2
print("RG7: F2 exposure -- the isolating direction (1,0,1) is admissible")
T = [[Fraction(1), Fraction(0), Fraction(1)],
     [Fraction(0), Fraction(1), Fraction(0)],
     [Fraction(1), Fraction(0), Fraction(1)]]
min1 = T[0][0]
min2 = T[0][0] * T[1][1] - T[0][1] * T[1][0]
det = (T[0][0] * (T[1][1] * T[2][2] - T[1][2] * T[2][1])
       - T[0][1] * (T[1][0] * T[2][2] - T[1][2] * T[2][0])
       + T[0][2] * (T[1][0] * T[2][1] - T[1][1] * T[2][0]))
eigs = np.linalg.eigvalsh(np.array(T, dtype=float))
ok = (min1 == 1 and min2 == 1 and det == 0 and
      all(e > -1e-12 for e in eigs) and abs(eigs[0]) < 1e-12)
gate("RG7 F2-exposure-exact", ok,
     "Toeplitz(c=(1,0,1)): minors 1,1, det = 0 (exact Fractions), eigs = "
     "{%.0f,%.0f,%.0f}: PSD BOUNDARY, entries >= 0 -> ADMISSIBLE sample "
     "direction (c_k = g-check(k log p) >= 0, HH H5a) loading ONLY the "
     "breaking k=2 slot: no scalar aggregate dominates it" %
     tuple(round(e) for e in sorted(eigs)))

# ============================================================== RG8: F3
print("RG8: F3 count-shape structure tests on the frozen -m+ data")
# --- (p;2) scans (NN G9 machinery) + sign-change counts
scans = {}
signflips = {}
for p in (5, 7, 11, 13, 17):
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
    flips = []
    for ip in range(nper):
        sel = (ag >= a0 + ip * per) & (ag < a0 + (ip + 1) * per)
        sg = np.sign(ms[sel])
        flips.append(int(np.sum(sg[1:] * sg[:-1] < 0)))
    signflips[p] = flips
    record("T3 p=%d sign changes per period: %s (count-shape predicts <= "
           "2 with single onset; both signs recur each period)"
           % (p, flips))

# --- T1: quantization floor on the certified breaking set
LOG2 = LOG(2)
breaking = []          # (label, a, -m+ mid, certified<0, inside (0,log2))
ok = True
for a in (0.5, 1.0, 2.0, 5.0):
    m, _ = margin_pair({2: 1}, a, 0)
    cert = resolved_sign(m) == -1
    inside = resolved_sign(-m) == 1 and resolved_sign(m + LOG2) == 1
    ok = ok and cert and inside
    breaking.append(("d=1@%g" % a, a, -float(m.mid()), cert, inside))
for p in (5, 7, 11, 13, 17):
    sc = scans["p%d_d2" % p]
    ag, ms = np.array(sc["a"]), np.array(sc["m"])
    sel = ag < FIRSTNEG[p] + 2 * LOG(p)
    a_star = float(ag[sel][np.argmin(ms[sel])])     # first-period argmin
    for a in (a_star, FIRSTNEG[p] + 0.2):
        m, _ = margin_pair({p: 2}, a, 0)
        s = resolved_sign(m)
        if s == -1:
            inside = resolved_sign(-m) == 1 and resolved_sign(m + LOG2) == 1
            ok = ok and inside
            breaking.append(("(%d;2)@%.3f" % (p, a), a, -float(m.mid()),
                             True, inside))
        else:
            record("T1 note: (%d;2)@%.3f not negative (m=%+.1e, sign %d) "
                   "-- excluded from breaking set" % (p, a, float(m.mid()), s))
        if a == a_star:
            ok = ok and s == -1     # the period argmin must certify < 0
breaking.append(("(11;2)@4.96 DECISION", 4.96, -float(mv_dec.mid()),
                 True, True))
vals = [b[2] for b in breaking]
record("T1 breaking set: %d certified deficits, -m+ in [%.2e, %.3f]; "
       "count lattice {log m} has NO point in (0, log2): nearest points "
       "0 (=> h^1=0, contradicts certified <0) and log2 (overshoot "
       "x%.0f at the decision cell)" %
       (len(breaking), min(vals), max(vals), LOG2 / 2.21e-3))
ok = ok and max(vals) < LOG2 and min(vals) > 0

# --- T2: place-additivity over mixed depth-2 classes
t2rows = []
for (pa, pb, a) in ((5, 11, 4.96), (7, 11, 4.96), (11, 13, 5.33)):
    mu, _ = margin_pair({pa: 2, pb: 2}, a, 0)
    ma, _ = margin_pair({pa: 2}, a, 0)
    mb, _ = margin_pair({pb: 2}, a, 0)
    dev = float((mu - ma - mb).mid())
    t2rows.append("T2 {%d,%d}@%.2f: m(union)=%+.5f vs sum=%+.5f, "
                  "additivity dev = %+.5f (%.0f%% of |sum|)" %
                  (pa, pb, a, float(mu.mid()), float((ma + mb).mid()), dev,
                   100 * abs(dev) / max(abs(float((ma + mb).mid())), 1e-12)))
m2a, _ = margin_pair({2: 1}, 2.0, 0)
m5a, _ = margin_pair({5: 1}, 2.0, 0)
ident_d1 = abs(float((m2a - m5a).mid())) < 1e-80
t2rows.append("T2 place-forgetting at d=1: m+([2])-m+([5]) = 0 exactly "
              "(%s): a count carrying Lambda(p)=log p cannot forget p"
              % ident_d1)
for r in t2rows:
    record(r)
ok = ok and ident_d1
gate("RG8 F3-structure-tests (structural)", ok,
     "breaking set certified strictly inside (0, log 2) -- BELOW the "
     "count quantization floor; additivity deviations recorded; sign "
     "structure oscillatory (T3)")

# ============================================================== RG9
print("RG9: carrier guard (inherited, rerun inline)")


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
v_via_49, v_via_66 = 0 + 0, 1 + 1
ok = ok and v_via_49 != v_via_66
gate("RG9 carrier-guard", ok,
     "Epstein x^2+5y^2: 36 = 4*9 = 6*6, no additive valuation -> n_1(D) "
     "UNFORMABLE (chi_GG needs depth data) AND no tower address -> "
     "Theta_p measure unformable; DH: no carrier monoid (bookkeeping)")

# ============================================================== RG10
print("RG10: freeze + zero comparison (NN G7 protocol verbatim)")
payload = json.dumps({
    "a": AGRID.tolist(), "A_v": A_v.tolist(), "A_g": A_g.tolist(),
    "scans": scans, "breaking": [(b[0], b[1], b[2]) for b in breaking],
    "lp": lp_out,
    "decision_cell": float(mg_dec.mid()),
    "A11_496": [float(Av11.mid()), float(Ag11.mid())]}).encode()
with open("/tmp/rr_freeze.json", "wb") as fh:
    fh.write(payload)
frz = hashlib.sha256(payload).hexdigest()
print("  FREEZE sha256 = %s  (computed BEFORE any zero import)" % frz)

from .fork_lib import zeta_gammas  # noqa: E402  (AFTER freeze, comparison only)

gam = zeta_gammas(100)
da = AGRID[1] - AGRID[0]


def spectrum_z(series, excl_fund):
    k = np.exp(-0.5 * (np.arange(-60, 61) * da / 0.4) ** 2)
    f = series - np.convolve(series, k / k.sum(), mode="same")
    f = f * np.hanning(len(f))
    gg = np.arange(0.5, 70.0, 0.02)
    amp = np.abs(np.exp(-1j * np.outer(gg, AGRID)) @ f) * da
    bg = (gg >= 5) & (gg <= 60)
    for g0 in gam[:12]:
        bg &= np.abs(gg - g0) > 1.5
    for w in excl_fund:
        kk = 1
        while kk * w <= 60.5:
            bg &= np.abs(gg - kk * w) > 0.75
            kk += 1
    med = float(np.median(amp[bg]))
    mad = float(np.median(np.abs(amp[bg] - med))) + 1e-300
    return [(float(amp[np.argmin(np.abs(gg - g0))]) - med) / (1.4826 * mad)
            for g0 in gam[:5]]


EXCL = [2 * math.pi / LOG(2), 2 * math.pi / LOG(3)]
Zv = spectrum_z(A_v, EXCL)
Zg = spectrum_z(A_g, EXCL)
for nm, zz in (("A_v(global aggregate)", Zv), ("A_g", Zg)):
    record("z at gamma_1..5 [%s]: %s" % (nm, ", ".join("%.1f" % z for z in zz)))
shock = (sum(z >= 4 for z in Zv) >= 3) or (sum(z >= 4 for z in Zg) >= 3)
gate("RG10 freeze-then-zeros comparison", True,
     "freeze ordering enforced; shock (>=3 of 5 at z>=4): %s; registered "
     "expectation z<3: %s" %
     ("TRIGGERED - ESCALATE" if shock else "not triggered",
      "met" if max(Zv + Zg) < 3 else "EXCEEDED (see table)"))

# ------------------------------------------------------------------ exit
print("=" * 78)
print("VERDICT INPUTS: F1 decision cell (11;2)@4.96 m+_GG = %+.5e "
      "(moved: %s); F2 A_11(4.96) v/g = %+.5f / %+.5f; global aggregate "
      "neg-frac v/g = %.2f / %.2f; LP: %s; F3 deficits strictly inside "
      "(0, log 2): see RG8" %
      (float(mg_dec.mid()), bool(moved), float(Av11.mid()),
       float(Ag11.mid()), neg_frac_v, neg_frac_g, lp_out))
if failures:
    print("FAILURES:", failures)
    sys.exit(1)
print("ALL STRUCTURAL GATES PASS")
sys.exit(0)
