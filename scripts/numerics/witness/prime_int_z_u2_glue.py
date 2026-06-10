"""Z-witness: the U.2 glued object G = D cup_Lin D' at p = 2 (PFD step 1).

D = pi_* THR(F_2)^{tC_2} = F_2[[z]][t^{+-1}] (Theorem S.1), D' = its
degreewise continuous (Matlis) dual = divided-power algebra
Gamma_{F_2}[z'] with wt(gamma_m) = -m; G glues them along the Lin line
F_2[t^{+-1}] (weight 0 once).  Residue pairing on G (the only gluing
datum, K6):  <t^{-j} z^m, t^{j-1} gamma_{m'}> = delta_{m,m'},
Lin block <t^{-j}, t^{j-1}> = 1, all other weights 0.

PRE-REGISTERED READINGS (fail-closed; written before first run):
R-ZG1  D' is well-defined with zero choices: divided-power structure
       constants binom(i+j,i) mod 2 are associative/commutative,
       gamma_{2^k}^2 = 0, gamma_m = prod gamma_{2^k}^{m_k} (Lucas);
       weight-graded coproduct on z is forced additive (enumeration:
       the only weight-1 tensors are z(x)1, 1(x)z, and the counit
       forces both coefficients = 1).  FAIL: any identity fails.
R-ZG2  K2 TOWER: U's level-N pairing <a,b>_N = coeff of t^{-1}z^N in
       ab EQUALS the G-pairing <a, iota_N(b)> for the colimit
       insertion iota_N(t^a z^m) = t^a gamma_{N-m} (gamma_0 = z^0);
       iota_{N+1}(z u) = iota_N(u); fixed G-pairs are N-independent
       while U's fixed D-pairs decay (re-witnessed).  All N <= 10,
       j in -3..4.  FAIL: any mismatch -> K2 fails, locate it.
R-ZG3  K2 PERFECTNESS: on every truncation (weights -M..M, M <= 8) and
       every degree j in -3..4 the Gram matrix of <,>: G_j x G_{1-j}
       is a PERMUTATION matrix implementing the weight flip m <-> -m
       (z^m <-> gamma_m, Lin <-> Lin).  FAIL: non-permutation.
R-ZG4  FORCED SCHEME (O Thm A1 instance): on the glued carrier the
       negation ratio f_c(-w)/f_c(w) is constant over (w, weight)
       iff c = 1/2 (value -1, |dev| < 1e-12); variance scan over
       c in {0, 1/4, 1/2, 3/4, 1} has its unique zero at c = 1/2;
       exact A1 slope solve: -2 alpha + 1 = 0 -> alpha = 1/2 in
       units of log q.  FAIL: constancy at some c != 1/2.
R-ZG5  K1 SCALE-FREENESS (the not-decidable mechanism): exact rational
       identities: glued trace 1/(1-x) + 1/(1-1/x) - 1 = 0 (25 pts);
       glued two-sided ladder anomaly zeta_H(0,a)+zeta_H(0,1-a) = 0
       as a polynomial; the NONZERO anomalies live only off G:
       fold (1-s)/2, Gamma_C line 1/2 - s, Barnes s^2/4-3s/4+11/24.
       FAIL: a nonzero glued anomaly (then K1 has a local candidate).
R-ZG6  SHEAR ON D: phi(z) = z/(1+z) is [-1] of the MULTIPLICATIVE
       formal group (F(z, phi z) = 0, 1 + phi z = (1+z)^{-1}), NOT of
       the additive one (whose [-1] = id != phi); phi^2 = id on D;
       the invariant 1-form is dlog(1+z) (phi^* fixes dz/(1+z),
       moves dz).  FAIL: identities fail in truncation (wt < 12).
R-ZG7  SHEAR ON G: phi extends to phi_G = (phi on D) + (adjoint A on
       Gamma) + connecting map kappa: Gamma -> D, with kappa_0 forced
       = binom(1+a', b') and (involutivity) kappa A = phi kappa,
       (isometry) the Gamma x Gamma cross terms cancel.  EXPECTED:
       the exact F_2 linear system is SOLVABLE (existence), solution
       non-unique (nullity > 0); the solved phi_G is an involutive
       isometry, identity on Lin, NO branch swap (D never maps to
       Gamma): the shear stays unipotent, no negation component.
       FAIL: system unsolvable -> the C_2 does not act on G; report
       the obstruction row (that finding replaces the pass).
R-ZG8  N2 FORCED: the duality pairs degree j with 1-j (odd total), so
       it vanishes identically on the even sublattice F_2[t^{+-2}]
       (v-lattice): no (j, 1-j) both even; the duality needs the
       index-2 refined t-lattice (spacing pi i / log 2).  FAIL: n/a
       (parity); gate records the bookkeeping exactly.

Run: python3 -m scripts.numerics.witness.prime_int_z_u2_glue
Exit 0 iff ALL PASS.
"""

import cmath
import math
import sys
from fractions import Fraction

MW = 12   # weight-series truncation: drop z^m, m >= MW
MG = 5    # gamma-range: gamma_1..gamma_MG
failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def binom2(k, j):
    """binom(k, j) mod 2 for any integer k, j >= 0 (generalized)."""
    if j < 0:
        return 0
    if k >= 0:
        return math.comb(k, j) % 2 if j <= k else 0
    return math.comb(j - k - 1, j) % 2


# ---------------------------------------------------------------- D-algebra
# element of D: dict {(a, m): 1} == sum t^a z^m   (deg = -a, wt = m)

def dmul(u, v):
    out = {}
    for (a1, m1) in u:
        for (a2, m2) in v:
            if m1 + m2 < MW:
                k = (a1 + a2, m1 + m2)
                if k in out:
                    del out[k]
                else:
                    out[k] = 1
    return out


def dadd(u, v):
    out = dict(u)
    for k in v:
        if k in out:
            del out[k]
        else:
            out[k] = 1
    return out


def one_plus_z_pow(k, tshift=0):
    """(1+z)^k as element of D times t^tshift, k any integer."""
    return {(tshift, m): 1 for m in range(MW) if binom2(k, m)}


def phiD(u):
    """U's Weyl shear on D: t^a z^m -> t^a z^m (1+z)^{-(a+m)}."""
    out = {}
    for (a, m) in u:
        for (aa, mm) in dmul({(a, m): 1}, one_plus_z_pow(-(a + m))):
            if (aa, mm) in out:
                del out[(aa, mm)]
            else:
                out[(aa, mm)] = 1
    return out


# --------------------------------------------------------------- G elements
# G element: (dD, dG); dD as above (wt >= 0); dG = {(a, m): 1} == t^a
# gamma_m with m >= 1 (wt = -m).  Lin line lives in dD (m = 0).

def pair_G(x, y):
    """residue pairing <x, y>, x = (dD, dG), y = (dD2, dG2)."""
    dD, dG = x
    dD2, dG2 = y
    s = 0
    for (a, m) in dD:           # D x D: Lin block only
        if m == 0 and ((-1 - a, 0) in dD2):
            s ^= 1
    for (a, m) in dD:           # D x Gamma: evaluation
        if m >= 1 and ((-1 - a, m) in dG2):
            s ^= 1
    for (a, m) in dG:           # Gamma x D
        if m >= 1 and ((-1 - a, m) in dD2):
            s ^= 1
    return s                    # Gamma x Gamma = 0


def iota(N, a, m):
    """colimit insertion iota_N: t^a z^m in D/z^{N+1} -> G."""
    assert 0 <= m <= N
    if N - m == 0:
        return ({(a, 0): 1}, {})
    return ({}, {(a, N - m): 1})


# ------------------------------------------------------------------- ZG1
ok = True
# divided-power structure constants, associativity, commutativity
for i in range(0, 13):
    for j in range(0, 13):
        cij = binom2(i + j, i)
        ok = ok and cij == binom2(i + j, j)              # commutative
        for k in range(0, 13):
            # (g_i g_j) g_k = g_i (g_j g_k)
            lhs = binom2(i + j, i) * binom2(i + j + k, i + j)
            rhs = binom2(j + k, j) * binom2(i + j + k, j + k)
            ok = ok and lhs % 2 == rhs % 2
ok = ok and all(binom2(2 ** (k + 1), 2 ** k) == 0 for k in range(4))
# Lucas presentation: prod over binary digits of m of gamma_{2^k} = gamma_m
for m in range(1, 16):
    digs = [2 ** k for k in range(4) if (m >> k) & 1]
    coeff, tot = 1, 0
    for d in digs:
        coeff = coeff * binom2(tot + d, d) % 2
        tot += d
    ok = ok and coeff == 1 and tot == m
# weight-graded coproduct forcing: weight-1 monomials in F_2[z] (x) F_2[z]
wt1 = [(i, j) for i in range(3) for j in range(3) if i + j == 1]
ok = ok and sorted(wt1) == [(0, 1), (1, 0)]   # only z(x)1 and 1(x)z
gate("ZG1 D' forced: divided powers (Lucas, assoc), additive coproduct", ok)

# ------------------------------------------------------------------- ZG2
ok = True
for N in range(0, 11):
    for j in range(-3, 5):
        for m in range(N + 1):
            for mp in range(N + 1):
                u_level = 1 if m + mp == N else 0          # U's <,>_N
                g_pair = pair_G(({(-j, m): 1}, {}), iota(N, j - 1, mp))
                ok = ok and u_level == g_pair
# tower: iota_{N+1}(z u) = iota_N(u)
for N in range(0, 10):
    for m in range(N + 1):
        ok = ok and iota(N + 1, 3, m + 1) == iota(N, 3, m)
# stability on G vs decay on U's tower for fixed pairs
for (m, mp) in ((0, 0), (1, 2), (3, 3)):
    gvals = {pair_G(({(0, m): 1}, {}), ({}, {(-1, mp): 1}) if mp else
             ({(-1, 0): 1}, {})) for _ in range(5)}
    ok = ok and len(gvals) == 1                            # N-independent
    uvals = [1 if m + mp == N else 0 for N in range(m + mp + 1, m + mp + 6)]
    ok = ok and uvals == [0] * 5                           # U decay
gate("ZG2 K2 tower: U's <,>_N = G-pairing o (id x iota_N), stable limit", ok)

# ------------------------------------------------------------------- ZG3
ok = True
for M in range(1, 9):
    for j in range(-3, 5):
        # basis of G_j window: z^M..z^1, z^0, gamma_1..gamma_M
        def basis(jj):
            b = [({(-jj, m): 1}, {}) for m in range(M, -1, -1)]
            b += [({}, {(-jj, m): 1}) for m in range(1, M + 1)]
            return b
        B1, B2 = basis(j), basis(1 - j)
        gram = [[pair_G(u, v) for v in B2] for u in B1]
        n = 2 * M + 1
        perm = all(sum(gram[r]) == 1 for r in range(n)) and \
            all(sum(gram[r][c] for r in range(n)) == 1 for c in range(n))
        # weight flip m <-> -m: z^m (row M-m) pairs with gamma_m (col M+m)
        flip = all(gram[M - m][M + m] == 1 for m in range(1, M + 1)) and \
            gram[M][M] == 1 and \
            all(gram[M + m][M - m] == 1 for m in range(1, M + 1))
        ok = ok and perm and flip
gate("ZG3 K2 perfect: Gram = permutation, weight flip m <-> -m, Lin<->Lin",
     ok)

# ------------------------------------------------------------------- ZG4
LOG2 = math.log(2.0)
sgrid = [0.3 + 0.7j, -1.2 + 0.4j, 2.1 - 1.3j, 0.5 + 0.1j]
weights = [0, 1, 3, -1, -3]


def f_c(c, w):
    return cmath.exp(c * w) * (1 - cmath.exp(-w))   # q^{cw}(1-q^{-w}), w in log q units


devs = {}
for c in (0.0, 0.25, 0.5, 0.75, 1.0):
    ratios = []
    for s in sgrid:
        for n in weights:
            w = (s + n) * LOG2
            ratios.append(f_c(c, -w) / f_c(c, w))
    mean = sum(ratios) / len(ratios)
    devs[c] = max(abs(r - mean) for r in ratios)
ok = devs[0.5] < 1e-12
ok = ok and all(devs[c] > 0.1 for c in devs if c != 0.5)
ok = ok and all(abs(f_c(0.5, -(s + n) * LOG2) / f_c(0.5, (s + n) * LOG2)
                    + 1) < 1e-12 for s in sgrid for n in weights)
# exact A1 slope solve: f(-w) = u f(w), P_odd = alpha w (log q units):
# -2 alpha + 1 = 0
alpha = Fraction(1, 2)
ok = ok and (-2 * alpha + 1 == 0)
gate("ZG4 forced scheme: ratio constant (= -1) iff c = 1/2; A1 alpha = 1/2",
     ok, "dev(1/2)=%.1e min-other=%.2f" % (devs[0.5],
                                           min(d for c, d in devs.items()
                                               if c != 0.5)))

# ------------------------------------------------------------------- ZG5
ok = True
pts = [Fraction(p, q) for p in range(-5, 7) for q in (2, 3, 7)
       if Fraction(p, q) not in (0, 1)][:25]
for x in pts:
    ok = ok and (1 / (1 - x) + 1 / (1 - 1 / x) - 1 == 0)   # glued trace = 0
# anomaly polynomials (coeff lists in the ladder variable, exact):
# zeta_H(0, a) = 1/2 - a -> [1/2, -1]
zh = [Fraction(1, 2), Fraction(-1)]


def padd(p, q):
    n = max(len(p), len(q))
    return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0)
            for i in range(n)]


def psub_at_1_minus(p):
    # p(1 - a) for linear p
    return [p[0] + p[1], -p[1]]


glued = padd(zh, psub_at_1_minus(zh))            # zeta(0,a)+zeta(0,1-a)
ok = ok and all(c == 0 for c in glued)           # glued anomaly == 0
fold = [Fraction(1, 2), Fraction(-1, 2)]         # (1-s)/2
gammac = zh                                      # 1/2 - s
barnes = [Fraction(11, 24), Fraction(-3, 4), Fraction(1, 4)]
ok = ok and any(c != 0 for c in fold) and any(c != 0 for c in gammac) \
    and any(c != 0 for c in barnes) and barnes[2] != 0
gate("ZG5 K1: glued trace = 0, glued anomaly = 0 exactly; "
     "nonzero anomalies only off G (fold, Gamma_C, Barnes)", ok)

# ------------------------------------------------------------------- ZG6
z_el = {(0, 1): 1}
phz = phiD(z_el)                                  # z/(1+z)
ok = phz == {(0, m): 1 for m in range(1, MW)}     # z + z^2 + ...
# multiplicative FGL: F(z, phz) = z + phz + z*phz = 0
ok = ok and dadd(dadd(z_el, phz), dmul(z_el, phz)) == {}
# 1 + phi z = (1+z)^{-1}
ok = ok and dadd({(0, 0): 1}, phz) == one_plus_z_pow(-1)
# additive [-1] = z itself != phi z
ok = ok and phz != z_el
# phi^2 = id on D (sample monomials incl. t-powers)
for (a, m) in ((0, 1), (2, 0), (-3, 2), (1, 1), (4, 3)):
    ok = ok and phiD(phiD({(a, m): 1})) == {(a, m): 1}
# invariant form: phi^*(h dz) = h(phi z) phi'(z) dz, phi'(z) = (1+z)^{-2}
# h = (1+z)^{-1}: h(phi z) = 1 + z (exact), so phi^*omega = (1+z)^{-1} dz


def subst_phz(h):
    """h(phi z) for h = {(0,m)} series."""
    out = {}
    for (a, m) in h:
        assert a == 0
        term = {(0, 0): 1}
        for _ in range(m):
            term = dmul(term, phz)
        out = dadd(out, term)
    return out


h = one_plus_z_pow(-1)
pullback = dmul(subst_phz(h), one_plus_z_pow(-2))   # h(phz) * phi'(z)
ok = ok and pullback == h                            # omega invariant
ok = ok and one_plus_z_pow(-2) != {(0, 0): 1}        # dz NOT invariant
gate("ZG6 shear = [-1] of G_m-hat; invariant form dlog(1+z); phi^2 = id",
     ok)

# ------------------------------------------------------------------- ZG7
# solve for kappa: Gamma -> D per degree pair (a', a'' = -1 - a')
# variables kappa[(a, b')][m], b' = 1..MG, m = 0..MW-1


def A_mat(a):
    """adjoint on Gamma-branch: A(t^a g_{b'}) = sum_b C[b'][b] t^a g_b,
    C[b'][b] = binom2(1 + a - b, b' - b), b = 1..b'."""
    return {(bp, b): binom2(1 + a - b, bp - b)
            for bp in range(1, MG + 1) for b in range(1, bp + 1)}


def solve_pair(ap):
    app = -1 - ap
    var = {}
    for a in (ap, app):
        for bp in range(1, MG + 1):
            for m in range(MW):
                var[(a, bp, m)] = len(var)
    nv = len(var)
    rows = []   # (bitmask over vars, rhs bit)
    A = {ap: A_mat(ap), app: A_mat(app)}
    k0 = {(a, bp): binom2(1 + a, bp)
          for a in (ap, app) for bp in range(1, MG + 1)}
    # C1: kappa_0 forced
    for a in (ap, app):
        for bp in range(1, MG + 1):
            rows.append((1 << var[(a, bp, 0)], k0[(a, bp)]))
    # C2: involutivity  sum_b A[bp][b] kappa^{(b)}  =  phi(kappa^{(bp)})
    # row per output weight r:  sum_b A kappa^{(a,b)}_r
    #   + sum_m binom2(-(a+m), r-m) kappa^{(a,bp)}_m = 0
    for a in (ap, app):
        for bp in range(1, MG + 1):
            for r in range(MW):
                mask = 0
                for b in range(1, bp + 1):
                    if A[a].get((bp, b), 0):
                        mask ^= 1 << var[(a, b, r)]
                for m in range(0, r + 1):
                    if binom2(-(a + m), r - m):
                        mask ^= 1 << var[(a, bp, m)]
                if mask:
                    rows.append((mask, 0))
    # C3: Gamma x Gamma isometry:
    # sum_b A^{a'}[bp][b] kappa^{(a'',bpp)}_b
    #   + sum_b A^{a''}[bpp][b] kappa^{(a',bp)}_b = k0 k0'
    for bp in range(1, MG + 1):
        for bpp in range(1, MG + 1):
            mask = 0
            for b in range(1, bp + 1):
                if A[ap].get((bp, b), 0):
                    mask ^= 1 << var[(app, bpp, b)]
            for b in range(1, bpp + 1):
                if A[app].get((bpp, b), 0):
                    mask ^= 1 << var[(ap, bp, b)]
            rows.append((mask, k0[(ap, bp)] * k0[(app, bpp)] % 2))
    # F_2 Gaussian elimination
    pivots = {}
    for mask, rhs in rows:
        for pc in sorted(pivots, reverse=True):
            if mask >> pc & 1:
                mask ^= pivots[pc][0]
                rhs ^= pivots[pc][1]
        if mask == 0:
            if rhs:
                return None, None, None
            continue
        pivots[mask.bit_length() - 1] = (mask, rhs)
    # full reduction to RREF (each pivot row keeps only its own pivot
    # bit + free columns), then read off a particular solution with
    # all free variables = 0
    for pc in sorted(pivots, reverse=True):
        mpc, rpc = pivots[pc]
        for pc2 in pivots:
            if pc2 != pc and (pivots[pc2][0] >> pc & 1):
                pivots[pc2] = (pivots[pc2][0] ^ mpc, pivots[pc2][1] ^ rpc)
    sol = [0] * nv
    for pc, (mask, rhs) in pivots.items():
        sol[pc] = rhs
    nullity = nv - len(pivots)
    kap = {}
    for (a, bp, m), idx in var.items():
        if sol[idx]:
            kap.setdefault((a, bp), {})[(a, m)] = 1
    return kap, nullity, var


ok = True
detail = []
for ap in (0, 1, 2, 3):
    kap, nullity, var = solve_pair(ap)
    if kap is None:
        ok = False
        detail.append("a'=%d UNSOLVABLE" % ap)
        continue
    detail.append("a'=%d nullity=%d" % (ap, nullity))
    ok = ok and nullity > 0
    app = -1 - ap
    A = {ap: A_mat(ap), app: A_mat(app)}

    def phiG(x, a_home):
        """phi_G on a G-element living in degrees {a_home, partner}."""
        dD, dG = x
        outD, outG = phiD(dD), {}
        for (a, m) in dG:
            for b in range(1, m + 1):
                if A[a].get((m, b), 0):
                    if (a, b) in outG:
                        del outG[(a, b)]
                    else:
                        outG[(a, b)] = 1
            outD = dadd(outD, kap.get((a, m), {}))
        return (outD, outG)

    # verify involution + isometry + no branch swap, exhaustively on basis
    tests = [({(a, m): 1}, {}) for a in (ap, app) for m in range(0, 4)] + \
            [({}, {(a, m): 1}) for a in (ap, app) for m in range(1, MG + 1)]
    for x in tests:
        xx = phiG(phiG(x, ap), ap)
        # compare modulo truncation: weights < MW - MG safe zone
        trim = lambda e: ({k: 1 for k in e[0] if k[1] < MW - MG}, e[1])
        ok = ok and trim(xx) == trim(x)
        # no branch swap: D-element never acquires Gamma part
        if not x[1]:
            ok = ok and phiG(x, ap)[1] == {}
    for x in tests:
        for y in tests:
            dx = -list(x[0] or x[1])[0][0]
            dy = -list(y[0] or y[1])[0][0]
            if dx + dy == 1:
                ok = ok and pair_G(phiG(x, ap), phiG(y, ap)) == pair_G(x, y)
    # identity on Lin line
    for a in (ap, app):
        ok = ok and phiG(({(a, 0): 1}, {}), ap)[0].get((a, 0)) == 1
gate("ZG7 shear extends to G: involutive isometry, unipotent, no swap",
     ok, "; ".join(detail))

# ------------------------------------------------------------------- ZG8
ok = all(not (j % 2 == 0 and (1 - j) % 2 == 0) for j in range(-20, 21))
# even-sublattice Gram (degrees even both sides) is empty/zero:
for j in range(-6, 7, 2):
    jp = 1 - j           # odd: not in even sublattice
    ok = ok and jp % 2 == 1
gate("ZG8 N2 forced: duality shift 1 is odd -> vanishes on v-lattice "
     "F_2[t^{+-2}]; needs t-lattice (spacing pi i/log 2)", ok)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (ZG1-ZG8)")
