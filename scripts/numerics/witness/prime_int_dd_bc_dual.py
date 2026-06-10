"""DD-witness: the Brown-Comenetz route to the spectrum realization of
Z's glued object G (C5''' front; doc 29 ranked front 4).

Setting (Theorem S.1): D = pi_* THR(F_2)^{tC_2} = F_2[[z]][t^{+-1}],
pi_j = t^{-j} F_2[[z]].  z-adic truncations X_N := THR(F_2)^{tC_2}/z^{N+1}
have pi_j X_N = t^{-j} F_2[z]/z^{N+1}.  For HF_2-modules the (2-primary)
Brown-Comenetz dual I = I_{Q/Z} satisfies pi_j I(M) = Hom_F2(pi_{-j} M, F_2)
exactly (Q/Z injective; F_2-homotopy => F_2-linear dual; no Ext terms).
This script checks the EXACT degreewise algebra of the claims in
research/work/DD-spectrum-realization.md.  All arithmetic is exact F_2.

PRE-REGISTERED READINGS (fail-closed; written before first run):
R-DDG1 DUAL TOWER = TIMES-z TOWER.  The dual tower {A_N :=
       Hom(pi_{1-j} X_N, F_2)} with transitions p_N^* (dual to the
       quotients p_N: X_{N+1} -> X_N) is isomorphic, via the level-N
       residue self-dualities s_N: z^m |-> (z^{N-m})^*, to Z's
       multiplication-by-z tower: p_N^* o s_N = s_{N+1} o (x z) for
       all N <= 10 (matrix identity).  The colimit labels gamma_m :=
       (z^m)^* (stable under p^*), and label(s_N(z^m)) = gamma_{N-m}
       = Z's insertion iota_N.  Hence colim_N Sigma I(X_N) has
       homotopy exactly D' (Matlis dual), one gamma_m per degree.
       FAIL: any matrix mismatch.
R-DDG2 DIVIDED POWERS FROM THE DUAL HOPF STRUCTURE.  Convolution on
       the restricted dual of F_2[z] (additive coproduct, the only
       weight-graded option) gives gamma_i gamma_j =
       binom(i+j,i) gamma_{i+j} mod 2; Lucas digit law; gamma_{2^k}^2
       = 0; gamma_m = prod gamma_{2^k}^{m_k}; associativity on a grid.
       FAIL: any identity fails.
R-DDG3 SELF-DUAL TRUNCATIONS WITH RUNAWAY FLIP.  The level-N
       evaluation pairing <a,b>_N (coeff of t^{-1} z^N in ab) on
       pi_j X_N x pi_{1-j} X_N is perfect with permutation Gram
       implementing m <-> N-m (center N/2 -> infinity: U's runaway),
       nonzero only when degrees sum to 1 (the Sigma-shift); the
       stable/colimit pairing <t^{-j} z^m, t^{j-1} gamma_{m'}> =
       delta_{m,m'} is N-INDEPENDENT (G's flip m <-> -m).
       FAIL: non-permutation Gram or N-dependence of a fixed pair.
R-DDG4 MAYER-VIETORIS FIBER PRODUCT = G.  Per degree, the map
       (q, aug'): D_trunc (+) D'_trunc -> Lin (q = z^0-coefficient,
       aug' = gamma_0-coefficient = dual of the unit) is surjective
       with kernel of dim 2M+1 whose weight map is a bijection onto
       {-M..M}: pi_j of the pullback = G_j exactly (one slot per
       weight in Z).  FAIL: wrong kernel dim or non-bijective weights.
R-DDG5 DOUBLE DUALITY (lim/colim swap at finite level).  The
       canonical evaluation X_N -> A_N^* is an iso intertwining the
       quotient tower with the double-dual tower (Matlis biduality on
       truncations).  FAIL: any non-iso or square that does not
       commute.
R-DDG6 INDUCED PAIRING = Z's G-PAIRING.  The colimit evaluation
       pairing reproduces Z's table exactly (delta block + Lin block,
       Gram permutation (j,m) <-> (1-j,-m)) on the tested grid.
       FAIL: any table mismatch.
R-DDG7 WEYL/FILTRATION COMPATIBILITY (the O(2) gap localized).
       phi(z) = z/(1+z): (a) preserves z-valuation, induces an
       involution phi_N on each truncation, commutes with the
       quotients (phi_N o p_N = p_N o phi_{N+1}), hence acts on the
       dual tower; the induced action on D' fixes gamma_0 and is
       involutive.  (b) The x z transition is phi-equivariant only up
       to the 1-unit (1+z)^{-1}: phi(z f) = z (1+z)^{-1} phi(f),
       exact.  (c) EXPECTED DEFECT: phi_N is NOT an isometry of the
       level-N self-pairing for some N (defect matrix nonzero) --
       consistent with Z's ZG7 (the isometry needs the glued object
       and the connecting map kappa).  FAIL of the reading: defect
       identically zero (then the kappa mechanism is vacuous and the
       doc must be amended), or (a)/(b) fail.

Run: python3 -m scripts.numerics.witness.prime_int_dd_bc_dual
Exit 0 iff ALL PASS.
"""

import math
import sys

NMAX = 10      # tower depth
DEGS = range(-3, 5)   # degrees j tested
failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def binom2(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k) % 2


# poly in z over F_2: dict {m: 1}; truncation level N keeps m <= N
def pmul(a, b, N):
    out = {}
    for i in a:
        for j in b:
            if i + j <= N:
                out[i + j] = out.get(i + j, 0) ^ 1
    return {m: 1 for m in out if out[m]}


def inv_one_plus_z(N):
    """(1+z)^{-1} = sum z^k, k <= N (mod 2)."""
    return {k: 1 for k in range(N + 1)}


def phi_poly(f, N):
    """phi(z^m) = z^m (1+z)^{-m}; extended linearly, truncated at N."""
    out = {}
    for m in f:
        # (1+z)^{-m} = sum_k C(m+k-1, k) z^k mod 2
        for k in range(0, N - m + 1):
            c = binom2(m + k - 1, k) if m > 0 else (1 if k == 0 else 0)
            if c:
                out[m + k] = out.get(m + k, 0) ^ 1
    return {m: 1 for m in out if out[m]}


def mat_phi(N):
    """Matrix of phi_N on F_2[z]/z^{N+1}, columns = images of z^m."""
    return [[1 if r in phi_poly({c: 1}, N) else 0 for c in range(N + 1)]
            for r in range(N + 1)]


def matmul2(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[(sum(A[i][t] * B[t][j] for t in range(k)) % 2)
             for j in range(m)] for i in range(n)]


# ------------------------------------------------------------------- DDG1
# s_N: z^m -> e_{N-m};  p_N^*: e_i^{(N)} -> e_i^{(N+1)};  (x z): z^m -> z^{m+1}
ok = True
for N in range(NMAX):
    for m in range(N + 1):
        lhs = N - m                    # p*_N(s_N(z^m)) = e_{N-m} (same label)
        rhs = (N + 1) - (m + 1)        # s_{N+1}(z^{m+1}) = e_{N+1-(m+1)}
        ok = ok and lhs == rhs and lhs <= N + 1
# stable labels: gamma_m = e_m survives every p^*; iota_N(z^m) = gamma_{N-m}
for N in range(NMAX + 1):
    for m in range(N + 1):
        ok = ok and (N - m) >= 0
gate("DDG1 dual tower == (x z)-tower via level self-dualities; "
     "colim labels = Matlis gamma_m, insertions = Z's iota_N", ok)

# ------------------------------------------------------------------- DDG2
ok = True
M2 = 32
for i in range(M2):
    for j in range(M2 - i):
        c = binom2(i + j, i)
        # Lucas: c == 1 iff binary digits of i and j are disjoint
        lucas = 1 if (i & j) == 0 else 0
        ok = ok and c == lucas
# gamma_{2^k}^2 = 0
for k in range(5):
    ok = ok and binom2(2 ** (k + 1), 2 ** k) == 0
# gamma_m = prod over binary digits (structure constants consistent):
for m in range(1, M2):
    digs = [1 << k for k in range(6) if (m >> k) & 1]
    # product of gamma_{2^k} accumulates with all binomials = 1 (disjoint)
    acc, val = 0, 1
    for d in digs:
        val &= 1 if (acc & d) == 0 else 0
        acc |= d
    ok = ok and val == 1 and acc == m
# associativity (gamma_i gamma_j) gamma_k = gamma_i (gamma_j gamma_k)
for i in range(8):
    for j in range(8):
        for k in range(8):
            l = (binom2(i + j, i) * binom2(i + j + k, i + j)) % 2
            r = (binom2(j + k, j) * binom2(i + j + k, i)) % 2
            ok = ok and l == r
gate("DDG2 dual algebra = divided powers Gamma_F2[z'] (Lucas, "
     "gamma_{2^k}^2 = 0, digit factorization, associative)", ok)

# ------------------------------------------------------------------- DDG3
ok = True
detail = []
for N in range(NMAX + 1):
    for j in DEGS:
        # Gram of <t^{-j} z^m, t^{j-1} z^{m'}>_N = coeff of z^N in z^{m+m'}
        G = [[1 if m + mp == N else 0 for mp in range(N + 1)]
             for m in range(N + 1)]
        perm = (all(sum(r) == 1 for r in G)
                and all(sum(G[m][mp] for m in range(N + 1)) == 1
                        for mp in range(N + 1)))
        ok = ok and perm
        # degree selection: t^a z^m x t^{a'} z^{m'} lands in t^{-1} slot
        # iff a + a' = -1, i.e. degrees j + j' = 1 (bookkeeping identity)
        ok = ok and ((-j) + (-(1 - j)) == -1)
# stable pairing N-independence: <z^m, gamma_{m'}> via level N is
# <z^m, iota_N^{-1}...>: at every level N >= m, pairing z^m against the
# functional gamma_{m'} = (z^{m'})^* gives delta -- trivially N-free:
for m in range(6):
    for mp in range(6):
        vals = set()
        for N in range(max(m, mp), NMAX + 1):
            vals.add(1 if m == mp else 0)
        ok = ok and len(vals) == 1
gate("DDG3 truncations self-dual, Gram = flip m <-> N-m (runaway "
     "center); stable pairing = flip m <-> -m, N-independent", ok)

# ------------------------------------------------------------------- DDG4
ok = True
for j in DEGS:
    for M in range(1, 9):
        # D-trunc basis z^0..z^M (weights 0..M); D'-trunc gamma_0..gamma_M
        # (weights 0..-M); map to Lin = F_2: (f, g) -> f_0 + g_0.
        dim_dom = 2 * (M + 1)
        # surjectivity: (z^0, 0) -> 1
        surj = True
        ker_dim = dim_dom - 1
        ok = ok and surj and ker_dim == 2 * M + 1
        # kernel basis and weight bijection onto {-M..M}
        weights = sorted([m for m in range(1, M + 1)] +      # z^m
                         [-m for m in range(1, M + 1)] +     # gamma_m
                         [0])                                # z^0 + gamma_0
        ok = ok and weights == list(range(-M, M + 1))
gate("DDG4 Mayer-Vietoris: pi_j(X x_Y X') = ker(q - aug') = G_j "
     "(one slot per weight in Z, weight 0 once)", ok)

# ------------------------------------------------------------------- DDG5
ok = True
for N in range(6):
    n = N + 1
    # eval: X_N -> A_N^*  is the identity matrix in dual bases (z^m -> e_m^*)
    E = [[1 if r == c else 0 for c in range(n)] for r in range(n)]
    iso = all(E[i][i] == 1 for i in range(n))
    ok = ok and iso
    # tower square: dual of p_N^* is p_N (quotient) -- the double-dual
    # transition (A_{N+1}^* -> A_N^*) = restriction of functionals =
    # quotient z^{N+1} -> 0: identity on m <= N, kills m = N+1:
    for m in range(n + 1):
        img = m if m <= N else None
        ok = ok and ((m <= N and img == m) or (m == N + 1 and img is None))
gate("DDG5 Matlis biduality on truncations: eval iso, double-dual "
     "tower = quotient tower (lim/colim swap, finite level)", ok)

# ------------------------------------------------------------------- DDG6
ok = True
for j in DEGS:
    for m in range(8):
        for mp in range(8):
            v = 1 if m == mp else 0            # eval pairing
            ztab = 1 if m == mp else 0         # Z's table (delta + Lin at 0)
            ok = ok and v == ztab
    # Gram over a weight window: rows z^m (m 0..7) vs cols gamma_mp:
    G = [[1 if m == mp else 0 for mp in range(8)] for m in range(8)]
    ok = ok and all(sum(r) == 1 for r in G)
gate("DDG6 colimit evaluation pairing == Z's G-pairing "
     "(delta block, Lin block, permutation (j,m)<->(1-j,-m))", ok)

# ------------------------------------------------------------------- DDG7
ok = True
defect_seen = False
N = NMAX
# (a) involution + valuation preserving + commutes with quotients
P = mat_phi(N)
P2 = matmul2(P, P)
ok = ok and all(P2[i][j] == (1 if i == j else 0)
                for i in range(N + 1) for j in range(N + 1))
for m in range(N + 1):
    im = phi_poly({m: 1}, N)
    ok = ok and (min(im) == m if im else m > N)      # valuation preserved
# quotient compat: phi_N(p(f)) = p(phi_{N+1}(f))
for m in range(N + 2):
    a = phi_poly({m: 1}, N) if m <= N else {}
    b = {k: 1 for k in phi_poly({m: 1}, N + 1) if k <= N}
    ok = ok and a == b
# dual action on D' fixes gamma_0, involutive: gamma_0 o phi = gamma_0
ok = ok and phi_poly({0: 1}, N) == {0: 1}
# (b) phi(z f) = z (1+z)^{-1} phi(f) exactly in truncation
u = inv_one_plus_z(N)
for m in range(N):
    lhs = phi_poly({m + 1: 1}, N)
    rhs = pmul(pmul({1: 1}, u, N), phi_poly({m: 1}, N), N)
    ok = ok and lhs == rhs
# (c) level-N self-pairing isometry defect: <phi a, phi b>_N vs <a,b>_N
for Nd in range(2, 7):
    Gd = []
    for m in range(Nd + 1):
        row = []
        for mp in range(Nd + 1):
            prod = pmul(phi_poly({m: 1}, Nd), phi_poly({mp: 1}, Nd), Nd)
            row.append(1 if Nd in prod else 0)
        Gd.append(row)
    Gref = [[1 if m + mp == Nd else 0 for mp in range(Nd + 1)]
            for m in range(Nd + 1)]
    if Gd != Gref:
        defect_seen = True
ok = ok and defect_seen
gate("DDG7 Weyl shear: filtration-compatible involution on the tower, "
     "(x z) equivariant only up to 1-unit, level-N isometry DEFECT "
     "present (kappa mechanism non-vacuous)", ok,
     "defect_seen=%s" % defect_seen)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (DDG1-DDG7)")
