"""R-INT / C6'' branch-fork decider (worker T): the filtration-0 layer of the
twisted square X(alpha) = THH(ku_p; ku_{(1,psi^alpha)}), executed at the
honest BAR level, plus the bookkeeping inputs of the counital no-go theorem
(T-doc, research/work/T-branch-fork.md) and the three-way s = 0 contrast.

Lineage: P-doc (research/work/P-c6pp-twisted.md) sec 3 fork (N), sec 5
branches (i)/(ii); Lee arXiv:2206.02411v3 (refs/) for the descent facts;
prime_twisted_adams_ku.py W1-W8 (lead-rerun ALL PASS) for the family laws.

Everything p-complete, p ODD; alpha = 1 + u p^c, c = v_p(alpha-1) >= 1
(wild).  R = Z_p[beta] = pi_* ku_p; the twisted bimodule R_phi has
m.x = m x and x.m = phi(x) m with phi(beta) = alpha beta (x of weight w
acts by alpha^w on one side).

PRE-REGISTERED READINGS (fail-closed, exit-gated):

  T1 (filtration-0 EXACT, bar level -- no Koszul shortcut): the honest
      two-sided normalized bar complex C_n = R_phi (x) Rbar^{(x)n} is,
      per weight w, a FINITE complex of f.g. free Z_p-modules (weight-w
      part of C_n has rank binom(w,n); the complex stops at n = w).
      Exact integer homology (flint SNF, cross-checked for small w by an
      independent pure-python SNF; construction validated against the
      Koszul model [R --(1-alpha)beta--> R] from the regular element
      beta_1 - beta_2 in R^e = Z_p[beta_1, beta_2]), pre-registered:
        HH_0: weight 0 = Z_p;  weight w >= 1 = Z/p^c  (UNIFORM half-ladder
              = ideal collapse; the relation module is the IDEAL
              ((1-alpha)beta), generated in weight 1);
        HH_n = 0 for ALL n >= 1, ALL weights (transversality: the
              cotangent line and all higher HH die);
        rational Betti numbers: b_0(0) = 1, all others 0 (rational
              transversality -- input (ii) of the no-go theorem T.1);
        untwisted control alpha = 1: HH_0 = Z_p, HH_1 = Z_p per weight
              (HKR: O + Omega^1), HH_{>=2} = 0;
        integrity: d o d = 0 exactly for every assembled matrix pair.
      VERDICT this gates: branch (i) is a THEOREM of the colimit/bar
      normalization at the pi_*-ring level (full HH, all degrees), and
      ONLY of that normalization.

  T2 (the weight-line contrast): the module-level mapping-torus complex
      [Z_p --(1-alpha^w)--> Z_p] per weight gives the LTE tower
      Z/p^{c+v_p(w)}; discriminator vs T1 is exactly v_p(w).  (Branch (ii)
      cardinality law; the bar complex proves the descent-side mechanism
      CANNOT be this -- see T3 -- so if the LTE tower survives to the
      abutment it must enter at filtration >= 1.)

  T3 (bookkeeping inputs of the counital no-go theorem T.1): in Lee's
      bigraded model (A_* free over ku_* on monomials in sigma^2 x_i,
      i >= 2, |sigma^2 x_i| = 2i+2; Gamma_* free over MU_* on monomials in
      sigma^2 b_i, |sigma^2 b_i| = 2i+2; MU_* = Z_p[x_1, x_2, ...]),
      the internal-degree-2 part of A (x)_{MU_*} Gamma has rank 1, basis
      {beta (x) 1}.  Hence ANY counital coaction psi on A_* satisfies
      psi(beta) = beta (x) 1, i.e. D^0(beta) = 0: the weight-diagonal
      (1 - alpha^w) CANNOT enter the filtration-0 differential of a
      counital descent E_1 at w = 1.  Also gated: the degeneration
      bookkeeping at (0,2) -- every d_r target dies by parity (cobar of
      even objects is even in internal degree) AND by the cobar vanishing
      line t >= 4s (Gammabar = ker(counit) is concentrated in internal
      degrees >= 4: sigma^2 b_i has degree 2i+2 >= 4 and the counit is
      iso on the MU_*-line; the previous draft cited "Lee Prop 4.1.1
      bound" -- the s <= 2 concentration is Lee Cor 4.1.2; both
      justifications are gated).  Combined with the rational row
      pi_2 X (x) Q = 0 -- T1's rational Betti numbers BRIDGED to sphere
      level by the skeletal/cyclic-bar rational comparison (T-doc Lemma
      T.2: the skeletal E^1 of the cyclic bar construction rationalizes
      to exactly the T1 complex (x) Q, because pi_*(ku_p (x) ku^{(x)s})
      (x) Q = Q_p[beta_0..beta_s] -- one p-complete factor, alpha = 1+p
      integral, so no Omega_{Q_p/Q} interference) -- and Lee Lem 3.1.5
      (strong convergence, twists verbatim: THH(MU) -> MU is
      2-connective), this REFUTES the counital twisted-comodule
      realization of the descent E_1 (P-doc sec 3 input (A) vessel):
      printed as DERIVED VERDICT (paper-level logic; arithmetic
      ingredients gated here; Theorem T.1 of the T-doc).

  T4 (the g_alpha coordinate profile and the TRUNCATED-ladder candidate):
      exact binomial arithmetic, alpha = 1 + u p^c:
        v_p(binom(alpha,k)/alpha) = c    for 2 <= k <= p-1,
                                  = c-1  for k = p and k = p+1,
      and for the canonical alpha = 1+p the cocycle is a POLYNOMIAL:
      binom(1+p, k) = 0 for k > p+1.  Consequences (pre-registered
      signatures, the L_0-identification itself is O2-blocked and NOT
      claimed): the relative-to-MU level-0 candidate ladder
      lambda(w) = min_{2<=k<=w+1} v_p(binom(alpha,k)/alpha) is c for
      w <= p-2 and c-1 for w >= p-1 (c = 1: weights >= p-1 DIE); the
      sphere-level numerical-lattice candidate (f(1) = 0 classes
      binom(u,k)) gives v_p(binom(alpha,k)) = c for 2 <= k <= p-1, c-1
      at k = p: truncation at w_0 = p.  NOTE the two candidates truncate
      at DIFFERENT weights (MU-relative at p-1; numerical at p): the
      three-way table below uses the NUMERICAL candidate (the one the
      unconditional skeletal s = 0 row of T6 actually probes); under it
      pi_{2(p-1)} is fork-blind and the trichotomy opens at 2p.
      THREE-WAY low-degree signature (alpha = 1+p, c = 1):
        pi_{2(p-1)} X: branch (i) Z/p, branch (ii) Z/p, truncated Z/p;
        pi_{2p}    X: branch (i) Z/p, branch (ii) Z/p^2, truncated 0.

  T5 (s = 0 three-way contrast, flint arb): ladder Dirichlet series
      D(s) = sum_w log(cells at weight w) w^{-s}:
        branch (i):   c log p zeta(s):     NO pole, D(0) = -(c/2) log p;
        branch (ii):  log p [c zeta(s) + zeta(s)/(p^s-1)]: simple pole,
                      residue -1/2, finite part zeta'(0)+(1/4-c/2) log p;
        truncated:    c log p sum_{w=1}^{w_0-1} w^{-s}: ENTIRE (finite
                      Dirichlet polynomial), D(0) = c (w_0 - 1) log p,
                      and NO zeta factor at all (no zero supply).
      Gated numerically at tiny s with arb; the pole/no-pole/entire
      trichotomy is the experimental discriminator.

  T6 (NEW, worker T -- the unconditional skeletal s = 0 row and the two
      named ambiguities).  The skeletal (cyclic-bar) filtration of
      X(alpha) needs only the GHM E_infinity psi^alpha on ku_p -- NOT
      blocker (A).  Its E^2_{0,2w} = coker(d^1) with
      d^1(xi) = (f(1) - f(alpha)) beta^w for xi a pi_{2w}(ku_p (x) ku)-
      class with rational coordinate function f (f = sum c_b t^b over
      beta_0^{w-b} beta_1^b).  Gated consequences:
        (a) LATTICE TRICHOTOMY: the image ideal {f(1) - f(alpha)} over
            (small lattice Z_p[beta_0,beta_1]) = p^c Z_p UNIFORM;
            (numerical/binomial lattice, KU_0KU-style, deg <= w) =
            staircase p^{max(c - j, 0)} Z_p on p^j <= w < p^{j+1}
            (c = 1: Z/p for w < p, DEATH at w >= p); per-weight-line
            (monomials only, no mixing) = LTE p^{c+v_p(w)} (= T2).
        (b) THEOREM T.3 (s = 0 exclusion): any lattice containing the
            monomial classes has image ideal containing (1-alpha)Z_p,
            so |E^2_{0,2w}| <= p^c < p^{c+v_p(w)} for p | w: the LTE
            bump CANNOT live at skeletal filtration 0.  Branch (ii), if
            it reaches the abutment, enters at filtration >= 1 or as an
            extension.  (Same verdict as T3 on the descent side: NO
            filtration-0 home for the local Euler supply.)
        (c) THE +-AMBIGUITY AT THE MU-LOCUS: v_p(kp) =
            v_p(alpha^{(p-1)k} - 1) = 1 + v_p(k) (W1 balance), and the
            two unit parts are EQUAL up to sign: kp + (alpha^{(p-1)k}-1)
            has v_p >= 2 + v_p(k) (cancellation) while
            kp - (alpha^{(p-1)k}-1) has v_p = 1 + v_p(k) exactly.  The
            twisted differential at Lee's tower locus (Prop 4.1.5)
            carries an unknown relative sign/unit: BOTH Z/p^{1+v} and
            Z/p^{2+v}-type outcomes are arithmetically realizable.
            NEW rigidity gates: the ambiguity is SPECIFIC to u = +-1
            (T6d: generic u, neither sign cancels) and to c = 1 (T6e:
            c >= 2 makes the eigenvalue term subleading, law forced):
            pre-registered dodge = compute pi_{2p} X(1+3p) instead.
      VERDICT this gates: pi_{2p} X(1+p) is UNDECIDABLE below two named
      ambiguities -- (L) the connective lattice ku_{2p}(ku)_p (is the
      k = p binomial/divided class present?) and (S) the sign/unit of
      the twisted differential on the mu/lambda_1-locus.  Degree 2p sits
      AT the first ambiguity, not below it; degrees 2w <= 2p-2 are below
      it (all candidate laws agree: Z/p^c).

Carrier guard: every object here consumes psi^alpha (the twisted bimodule,
the g_alpha cocycle = FGL conjugation of the orientation, the eigenvalue
alpha^w).  DH/Epstein: no ring => no bimodule, no FGL, no cocycle: dead at
the object.  (Necessary filter, not sufficient.)

Run:
    python3 -m scripts.numerics.witness.prime_twisted_fork_filtration_zero
"""
import math
import sys

from flint import fmpz_mat, arb

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


def vp(n, p):
    if n == 0:
        return None  # infinity
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


# ------------------------------------------------------------------ T1
print("T1: twisted bar complex of Z_p[beta], exact homology per weight")


def weight_basis(w, n):
    """Basis of weight-w part of C_n = R (x) Rbar^{(x)n}:
    tuples (a_0, a_1..a_n), a_0 >= 0, a_i >= 1, sum = w."""
    if n == 0:
        return [(w,)]
    out = []
    # a_1..a_n >= 1 with s = sum <= w; a_0 = w - s
    def comps(total, parts):
        if parts == 1:
            if total >= 1:
                yield (total,)
            return
        for first in range(1, total - parts + 2):
            for rest in comps(total - first, parts - 1):
                yield (first,) + rest
    for s in range(n, w + 1):
        for tail in comps(s, n):
            out.append((w - s,) + tail)
    return out


def bar_matrix(w, n, alpha):
    """Matrix of d_n: C_n -> C_{n-1} (weight w), integer entries.
    d(m (x) r_1..r_n) = m r_1 (x) ...  + sum (-1)^i m (x) ..r_i r_{i+1}..
                        + (-1)^n alpha^{a_n} r_n m (x) r_1..r_{n-1}."""
    dom = weight_basis(w, n)
    cod = weight_basis(w, n - 1)
    idx = {b: i for i, b in enumerate(cod)}
    M = [[0] * len(dom) for _ in range(len(cod))]
    for j, b in enumerate(dom):
        a0, rest = b[0], list(b[1:])
        # face 0: multiply m * r_1
        t = tuple([a0 + rest[0]] + rest[1:])
        M[idx[t]][j] += 1
        # inner faces
        for i in range(1, n):
            t = tuple([a0] + rest[: i - 1] + [rest[i - 1] + rest[i]]
                      + rest[i + 1:])
            M[idx[t]][j] += (-1) ** i
        # last face: twisted action of r_n
        t = tuple([a0 + rest[-1]] + rest[:-1])
        M[idx[t]][j] += (-1) ** n * alpha ** rest[-1]
    return fmpz_mat(M)


def homology_profile(w, alpha, p):
    """Per weight w return list over n = 0..w of (betti_n, [p-vals of
    elementary divisors of H_n]); also gate d o d = 0."""
    mats = {n: bar_matrix(w, n, alpha) for n in range(1, w + 1)}
    dims = {n: len(weight_basis(w, n)) for n in range(0, w + 1)}
    # integrity: d_{n} o d_{n+1} = 0
    for n in range(1, w):
        prod = mats[n] * mats[n + 1]
        if not prod.is_zero():
            return None
    out = []
    for n in range(0, w + 1):
        rk_in = mats[n + 1].rank() if n + 1 <= w else 0
        rk_out = mats[n].rank() if n >= 1 else 0
        betti = dims[n] - rk_out - rk_in
        tors = []
        if n + 1 <= w:
            S = mats[n + 1].snf()
            r = min(S.nrows(), S.ncols())
            for i in range(r):
                e = int(S[i, i])
                if e not in (0, 1, -1) and e != 0:
                    val = vp(abs(e), p)
                    if val and val > 0:
                        tors.append(val)
        out.append((betti, sorted(tors)))
    return out


ok_h0 = ok_hn = ok_rat = ok_dd = True
W1MAX = 9
for (p, c, u) in ((3, 1, 1), (3, 2, 1), (5, 1, 1), (5, 1, 2), (7, 1, 1)):
    alpha = 1 + u * p ** c
    for w in range(1, W1MAX + 1):
        prof = homology_profile(w, alpha, p)
        if prof is None:
            ok_dd = False
            continue
        b0, t0 = prof[0]
        # HH_0 weight w>=1: pure torsion Z/p^c  (betti 0, one divisor p^c)
        if not (b0 == 0 and t0 == [c]):
            ok_h0 = False
            print(f"    H0 mismatch p={p} c={c} u={u} w={w}: {prof[0]}")
        for n in range(1, w + 1):
            bn, tn = prof[n]
            if not (bn == 0 and tn == []):
                ok_hn = False
                print(f"    Hn mismatch p={p} c={c} u={u} w={w} n={n}: "
                      f"{prof[n]}")
        if any(b for (b, _) in prof):
            ok_rat = False
check("bar d o d = 0", ok_dd, "simplicial identities of the twisted bar "
      "differential hold exactly (every consecutive matrix pair)")
check("HH_0 ideal collapse (bar level)", ok_h0,
      f"weight w>=1: HH_0 = Z/p^c UNIFORM, exact SNF over Z, w <= {W1MAX},"
      " (p,c,u) grid incl. c=2 and u=2: the relation module is the ideal"
      " ((1-alpha)beta) generated in weight 1 -- branch (i) is a THEOREM"
      " of the bar/colimit normalization at pi_*-ring level")
check("HH_n = 0, n >= 1 (transversality, all HH degrees)", ok_hn,
      "the cotangent line and ALL higher bar homology die under the wild"
      " twist (no Koszul shortcut used)")
check("rational transversality", ok_rat,
      "all rational Betti numbers vanish in weight w >= 1 (pi_{2w} X"
      " (x) Q = 0): input (ii) of no-go theorem T.1")

# independent cross-check: pure-python SNF (no flint) on small weights
def py_snf_divisors(rows):
    """Elementary divisors of an integer matrix, naive Smith reduction."""
    M = [list(r) for r in rows]
    if not M or not M[0]:
        return []
    out = []
    r = c = 0
    nr, nc = len(M), len(M[0])
    while r < nr and c < nc:
        # find pivot of minimal |value|
        piv = None
        for i in range(r, nr):
            for j in range(c, nc):
                if M[i][j] != 0 and (piv is None
                                     or abs(M[i][j]) < abs(M[piv[0]][piv[1]])):
                    piv = (i, j)
        if piv is None:
            break
        i0, j0 = piv
        M[r], M[i0] = M[i0], M[r]
        for row in M:
            row[c], row[j0] = row[j0], row[c]
        dirty = False
        for i in range(nr):
            if i != r and M[i][c] % M[r][c] != 0:
                q = M[i][c] // M[r][c]
                for j in range(nc):
                    M[i][j] -= q * M[r][j]
                dirty = True
        for j in range(nc):
            if j != c and M[r][j] % M[r][c] != 0:
                q = M[r][j] // M[r][c]
                for i in range(nr):
                    M[i][j] -= q * M[i][c]
                dirty = True
        if dirty:
            continue
        for i in range(nr):
            if i != r and M[i][c] != 0:
                q = M[i][c] // M[r][c]
                for j in range(nc):
                    M[i][j] -= q * M[r][j]
        for j in range(nc):
            if j != c and M[r][j] != 0:
                q = M[r][j] // M[r][c]
                for i in range(nr):
                    M[i][j] -= q * M[i][c]
        out.append(abs(M[r][c]))
        r += 1
        c += 1
    return out


ok_x = True
for (p, c, u) in ((3, 1, 1), (5, 1, 1)):
    alpha = 1 + u * p ** c
    for w in range(1, 6):
        for n in range(1, w + 1):
            Mf = bar_matrix(w, n, alpha)
            rows = [[int(Mf[i, j]) for j in range(Mf.ncols())]
                    for i in range(Mf.nrows())]
            ds = [d for d in py_snf_divisors(rows) if d != 0]
            S = Mf.snf()
            fds = [abs(int(S[i, i]))
                   for i in range(min(S.nrows(), S.ncols()))
                   if int(S[i, i]) != 0]
            # module invariants: rank, total volume, p-primary type
            same = (len(ds) == len(fds)
                    and math.prod(ds) == math.prod(fds)
                    and sorted(vp(d, p) for d in ds)
                    == sorted(vp(d, p) for d in fds))
            if not same:
                ok_x = False
                print(f"    SNF mismatch p={p} w={w} n={n}: {ds} vs {fds}")
        # rank-per-level bookkeeping: weight-w part of C_n has rank C(w,n)
        if len(weight_basis(w, n)) != math.comb(w, n):
            ok_x = False
check("independent SNF + rank cross-check", ok_x,
      "pure-python Smith reduction reproduces flint SNF divisors for every"
      " bar matrix (w <= 5, p in {3,5}); weight-w rank of C_n = binom(w,n)"
      " exactly -- the T1 pipeline is validated by a second implementation")

# untwisted control
ok_ctl = True
for w in range(1, 7):
    prof = homology_profile(w, 1, 3)
    if prof is None or prof[0] != (1, []) or prof[1] != (1, []):
        ok_ctl = False
    if prof and any(prof[n] != (0, []) for n in range(2, w + 1)):
        ok_ctl = False
check("untwisted HKR control", ok_ctl,
      "alpha = 1: HH_0 = Z_p, HH_1 = Z_p (Omega^1), HH_{>=2} = 0 per"
      " weight -- the bar implementation reproduces HKR exactly")

# ------------------------------------------------------------------ T2
print("\nT2: weight-line (mapping-torus) contrast -- the LTE ladder")
ok2 = True
for p in (3, 5, 7):
    for c, u in ((1, 1), (2, 1)):
        alpha = 1 + u * p ** c
        M = p ** 40
        for w in range(1, 1001):
            lhs = vp((pow(alpha, w, M) - 1) % M, p)
            if lhs != c + (vp(w, p) or 0):
                ok2 = False
check("weight-line LTE contrast", ok2,
      "[Z_p --(1-alpha^w)--> Z_p] has H_0 = Z/p^{c+v_p(w)} (LTE tower);"
      " discriminator vs T1's uniform Z/p^c is exactly v_p(w): the two"
      " branch cardinality laws are the two normalizations of the SAME"
      " weight line")

# ------------------------------------------------------------------ T3
print("\nT3: no-go bookkeeping -- degree-2 line of A (x)_{MU*} Gamma")
# bigraded basis: ku_*-basis of A (x) Gamma = {beta^j} x {x-monomials}
#   x {b-monomials} x {MU_* monomials in x_i (Gamma's MU_*-freeness is
#   over eta_L; MU_* itself contributes via the ku_*-algebra structure:
#   x_1 -> beta, x_i -> 0, so MU_*-coefficients reduce into beta powers)}.
# Internal degree: |beta| = 2, |sigma^2 x_i| = 2i+2 (i >= 2),
# |sigma^2 b_i| = 2i+2 (i >= 1).


def count_basis(deg):
    """rank of internal-degree-`deg` part of A (x)_{MU_*} Gamma as a
    Z_p-module: beta^j * (sigma^2 x_{i})-mon * (sigma^2 b_i)-mon."""
    gens = []
    for i in range(2, deg):          # sigma^2 x_i, degree 2i+2
        if 2 * i + 2 <= deg:
            gens.append(2 * i + 2)
    for i in range(1, deg):          # sigma^2 b_i, degree 2i+2
        if 2 * i + 2 <= deg:
            gens.append(2 * i + 2)
    # count multisets of gens with total <= deg and (deg - total) even
    cnt = 0

    def rec(idx, rem):
        nonlocal cnt
        if rem % 2 == 0:
            cnt += 1  # fill with beta^{rem/2}
        for k in range(idx, len(gens)):
            if gens[k] <= rem:
                rec(k, rem - gens[k])
    rec(0, deg)
    return cnt


n2, n4, n6 = count_basis(2), count_basis(4), count_basis(6)
check("degree-2 line is {beta (x) 1}", n2 == 1,
      f"rank of (A (x) Gamma)_2 = {n2} (expected 1; Gammabar and Abar"
      " start in degree 4 and 6): ANY counital coaction has psi(beta) ="
      " beta (x) 1, so D^0(beta) = 0 -- the weight diagonal (1-alpha)"
      " CANNOT sit in the filtration-0 differential at weight 1")
check("degree-4/6 bookkeeping", (n4, n6) == (2, 4),
      f"(A (x) Gamma)_4 rank {n4} = {{beta^2, sigma^2 b_1}}, degree-6 rank"
      f" {n6} = {{beta^3, beta sigma^2 b_1, sigma^2 b_2, sigma^2 x_2}}:"
      " model matches Lee's generator degrees")

# degeneration bookkeeping: differentials leaving (s,t) = (0,2)
# two independent kill mechanisms, both required to fire for every r:
#   parity: cobar of even objects is concentrated in even internal t
#     OR s-bound: Ext concentrated in s <= 2 (Lee Cor 4.1.2)
#   vanishing line: normalized cobar has E^{s,t} = 0 for t < 4s
#     (Gammabar = ker(counit) starts in internal degree 4)
ok_deg = True
for r in range(2, 12):
    s_t, t_t = 0 + r, 2 + r - 1
    killed_parity_or_sbound = (t_t % 2 == 1) or (s_t > 2)
    killed_vline = t_t < 4 * s_t
    if not (killed_parity_or_sbound and killed_vline):
        ok_deg = False
check("degeneration bookkeeping at (0,2)", ok_deg,
      "every d_r (r >= 2) from (0,2) dies TWICE over: by parity (r even)"
      " or the s <= 2 concentration (Lee Cor 4.1.2; r odd), AND by the"
      " cobar vanishing line t >= 4s (target t = r+1 < 4r; Gammabar"
      " starts in degree 4, gated above): E_infty^{0,2} = E_2^{0,2}")
print("    DERIVED VERDICT (Theorem T.1, paper-level; arithmetic"
      " ingredients gated above and in T1):")
print("      counital comodule => D^0(beta) = 0 => E_2^{0,2} = Z_p beta;"
      " vanishing line t >= 4s")
print("      kills all d_r out of (0,2) and all E_infty^{s,s+2}, s >= 1;"
      " strong convergence")
print("      (Lee Lem 3.1.5, twists verbatim) => pi_2 X(alpha) = Z_p.")
print("      But pi_2 X (x) Q = 0: T1 rational row + the skeletal/cyclic-"
      "bar rational comparison")
print("      (Lemma T.2: rationalized skeletal E^1 IS the T1 complex (x)"
      " Q; one p-complete factor,")
print("      alpha integral -- no Omega_{Q_p/Q} interference)."
      "  CONTRADICTION: the twisted descent")
print("      E_1 is NEVER the cobar of a counital Gamma_*-comodule on"
      " (transported) A_*.  The")
print("      (A)-vessel as posed is dead; the twist must deform the"
      " levelwise identification itself.")

# ------------------------------------------------------------------ T4
print("\nT4: g_alpha coordinates -- exact profile + truncation candidates")


def binom_alpha(alpha_num, alpha_den, k):
    """binom(alpha, k) for alpha = alpha_num (integer), exact."""
    num = 1
    for j in range(k):
        num *= (alpha_num - j)
    return num // math.factorial(k) if num % math.factorial(k) == 0 \
        else None  # signal non-integrality (must not happen for int alpha)


ok4a = ok4b = ok4c = True
for (p, c, u) in ((3, 1, 1), (5, 1, 1), (5, 2, 1), (7, 1, 1), (7, 1, 3),
                  (11, 1, 1), (5, 3, 2)):
    alpha = 1 + u * p ** c
    for k in range(2, p + 2):
        b = binom_alpha(alpha, 1, k)
        v = vp(b, p)
        # v_p(binom(alpha,k)/alpha) = v_p(binom(alpha,k)) (alpha unit)
        if 2 <= k <= p - 1 and v != c:
            ok4a = False
            print(f"    coord mismatch p={p} c={c} u={u} k={k}: v={v}")
        if k in (p, p + 1) and v != c - 1:
            ok4b = False
            print(f"    unit-slot mismatch p={p} c={c} u={u} k={k}: v={v}")
for p in (3, 5, 7, 11):
    alpha = 1 + p
    for k in range(p + 2, p + 6):
        if binom_alpha(alpha, 1, k) != 0:
            ok4c = False
check("cocycle coordinates 2 <= k <= p-1", ok4a,
      "v_p(binom(alpha,k)/alpha) = c exactly (grid incl. c = 2,3, u != 1):"
      " the b_1..b_{p-2} coordinates carry the SAME valuation as the toy"
      " ladder -- weights 1..p-2 are fork-blind")
check("first sub-c slot at k = p, p+1", ok4b,
      "v_p = c-1 at the t_1 = b_{p-1} slot (weight p-1) and at b_p"
      " (weight p): the twist's first sub-ladder coordinate sits exactly"
      " on Lee's tower locus; for c = 1 it is a UNIT",)
check("g_{1+p} is a polynomial", ok4c,
      "binom(1+p,k) = 0 for k > p+1: the canonical wild cocycle has"
      " degree p+1 exactly (P-doc O1)")

print("    PRE-REGISTERED truncation signatures (candidates; the"
      " identification with pi_* of the")
print("    unconditional level-0 spectrum L_0(alpha) = X(alpha)"
      " (x)_{THH(MU)} MU is O2-BLOCKED, not claimed):")
for p in (5,):
    c, alpha = 1, 1 + 5
    lam = []
    best = 99
    for w in range(1, p + 3):
        # relation at weight w' = k-1 has valuation v_p(binom(alpha,k))
        b = binom_alpha(alpha, 1, w + 1)
        if b:
            best = min(best, vp(b, p))
        lam.append(best)
    print(f"      p={p}, alpha=1+p: relative-MU candidate ladder lambda(w),"
          f" w=1..{p+2}: {lam}")
    print(f"      => MU-relative candidate: uniform Z/p for w <= p-2 ="
          f" {p - 2}, DIES at w >= p-1 = {p - 1};")
    print("         numerical/skeletal candidate dies one step later,"
          " w_0 = p (this is the candidate")
    print("         the unconditional T6 row probes); three-way table"
          " (c = 1, numerical truncation):")
    print("         pi_{2(p-1)}X: (i) Z/p   (ii) Z/p     truncated Z/p"
          "   <- fork-blind")
    print("         pi_{2p}   X: (i) Z/p   (ii) Z/p^2   truncated 0"
          "     <- trichotomy opens AT 2p")

# ------------------------------------------------------------------ T5
print("\nT5: s = 0 three-way Dirichlet contrast (flint arb)")
prec = 350
import flint
flint.ctx.prec = prec
ok5i = ok5ii = ok5t = True
for (p, c) in ((3, 1), (5, 1), (5, 2)):
    lp = arb(p).log()
    # branch (i): D(0) = c log p * zeta(0) = -(c/2) log p, regular
    z0 = arb.zeta(arb(0))
    Di0 = c * lp * z0
    if not (Di0 + c * lp / 2).abs_upper() < arb(10) ** (-60):
        ok5i = False
    # branch (ii): D(s) + 1/(2s) -> zeta'(0) + (1/4 - c/2) log p
    # evaluate at tiny s, two scales, gate the limit
    zp0 = -(arb(2) * arb.pi()).log() / 2          # zeta'(0)
    target = zp0 + (arb(1) / 4 - arb(c) / 2) * lp
    vals = []
    for k in (25, 30):
        s = arb(10) ** (-k)
        zs = arb.zeta(s)
        D = lp * (c * zs + zs / ((arb(p) ** s) - 1))
        vals.append(D + 1 / (2 * s) - target)
    # |error| should shrink ~ s
    if not (vals[0].abs_upper() < arb(10) ** (-20)
            and vals[1].abs_upper() < arb(10) ** (-25)):
        ok5ii = False
    # residue probe: s * D(s) -> -1/2
    s = arb(10) ** (-28)
    res = (s * lp * (c * arb.zeta(s) + arb.zeta(s) / ((arb(p) ** s) - 1)))
    if not (res + arb(1) / 2).abs_upper() < arb(10) ** (-20):
        ok5ii = False
    # truncated: finite Dirichlet polynomial, w_0 = p-1 (MU candidate)
    w0 = p - 1
    Dt0 = c * lp * (w0 - 1)        # value at s = 0 (entire)
    s = arb(10) ** (-25)
    Dts = c * lp * sum(arb(w) ** (-s) for w in range(1, w0))
    if not (Dts - Dt0).abs_upper() < arb(10) ** (-20):
        ok5t = False
check("branch (i): regular at 0, value -(c/2) log p", ok5i,
      "c log p zeta(0) = -(c/2) log p exactly (no pole): the uniform"
      " ladder keeps the doc-18 local-constant form")
check("branch (ii): pole -1/(2s), finite part zeta'(0)+(1/4-c/2) log p",
      ok5ii, "verified at s = 1e-25, 1e-28, 1e-30 with arb (prec 350):"
      " the LTE ladder produces the LOCAL Euler supply factor"
      " (-zeta_p'/zeta_p)(s) and the s = 0 pole, residue -1/2")
check("truncated candidate: ENTIRE, value c(w_0 - 1) log p", ok5t,
      "the finite ladder has no pole AND no zeta factor (no zero supply):"
      " a THIRD discriminable s = 0 behaviour, pre-registered for"
      " whoever computes pi_* L_0")

# ------------------------------------------------------------------ T6
print("\nT6: unconditional skeletal s = 0 row -- lattice trichotomy and"
      " the two named ambiguities")


def binom_int(a, k):
    """binom(a, k) for integer a, exact (a may exceed k)."""
    num = 1
    for j in range(k):
        num *= (a - j)
    return num // math.factorial(k)


def image_val(p, c, u, w, lattice):
    """min v_p over the d^1-image ideal {f(1) - f(alpha)} at weight w.
    lattice: 'small' = Z_p[beta_0,beta_1] (f = monomials t^b, b=1..w);
    'numerical' = binomial basis binom(t,k), k=1..w (KU_0KU-style);
    'line' = the single monomial t^w only (per-weight-line/mapping
    torus normalization).  None = zero ideal."""
    alpha = 1 + u * p ** c
    vals = []
    if lattice == "small":
        gens = [alpha ** b - 1 for b in range(1, w + 1)]
    elif lattice == "numerical":
        gens = [binom_int(alpha, k) - binom_int(1, k)
                for k in range(1, w + 1)]
    elif lattice == "line":
        gens = [alpha ** w - 1]
    for g in gens:
        v = vp(g, p)
        if v is not None:
            vals.append(v)
    return min(vals) if vals else None


ok6a = ok6b = True
for (p, c, u) in ((3, 1, 1), (5, 1, 1), (5, 2, 1), (7, 1, 1), (3, 3, 2)):
    for w in range(1, 4 * p ** min(c + 1, 3)):
        vs = image_val(p, c, u, w, "small")
        vn = image_val(p, c, u, w, "numerical")
        vl = image_val(p, c, u, w, "line")
        # (a) trichotomy laws
        j = 0
        ww = w
        while ww >= p:
            ww //= p
            j += 1                      # j = floor(log_p w)
        if vs != c:
            ok6a = False
            print(f"    small-lattice law fails p={p} c={c} w={w}: {vs}")
        if vn != max(c - j, 0):
            ok6a = False
            print(f"    numerical staircase fails p={p} c={c} u={u}"
                  f" w={w}: v={vn} expected {max(c - j, 0)}")
        if vl != c + (vp(w, p) or 0):
            ok6a = False
        # (b) s = 0 exclusion: any lattice containing the monomials has
        # image ideal >= (alpha-1): coker divides p^c; LTE demands more
        # exactly at p | w
        if w % p == 0 and not (vl > c >= vs and vn <= vs):
            ok6b = False
check("T6a lattice trichotomy", ok6a,
      "image ideal {f(1)-f(alpha)} at weight w: small lattice -> p^c"
      " UNIFORM (ideal collapse); numerical/binomial lattice ->"
      " staircase p^{max(c-floor(log_p w),0)} (c = 1: DEATH at w >= p);"
      " single-line -> LTE p^{c+v_p(w)}: the three candidate filtration-0"
      " laws are the three lattices, exact on the full grid")
check("T6b s = 0 exclusion (Theorem T.3 arithmetic)", ok6b,
      "any lattice containing the monomial classes beta_0^{w-b}beta_1^b"
      " gives |E^2_{0,2w}| <= p^c < p^{c+v_p(w)} at p | w: the LTE bump"
      " is IMPOSSIBLE at skeletal filtration 0 (needs only GHM psi^alpha"
      " -- blocker (A) not consumed); branch (ii) must enter at"
      " filtration >= 1 or as an extension")

# (c) the +-ambiguity at the mu/lambda_1-locus.  Lee's tower coefficient
# is kp INDEPENDENT of alpha (Lem 3.2.8(d): eta_R sigma^2 x_{p-1} =
# sigma^2 x_{p-1} + p sigma^2 t_1 + beta^{p-2} sigma^2 b_1); the twisted
# differential adds the eigenvalue term (1 - alpha^{(p-1)k}) with an
# unknown relative unit theta.  Three regimes, all gated:
ok6c = ok6d = ok6e = True
for k in range(1, 40):
    # regime A: canonical alpha = 1+p (c = 1, u = 1): exact balance and
    # the + sign cancels (ev = alpha^w - 1 = -kp mod p^{2+v}): BOTH
    # outcomes realizable depending on theta -- the REAL ambiguity
    for p in (3, 5, 7, 11):
        alpha, v0 = 1 + p, 1 + (vp(k, p) or 0)
        ev = alpha ** ((p - 1) * k) - 1
        lee = k * p
        if not (vp(lee, p) == vp(ev, p) == v0
                and vp(lee + ev, p) >= v0 + 1 and vp(lee - ev, p) == v0):
            ok6c = False
    # regime B: u not +-1 mod p (alpha = 1+3p, p = 7): balance holds but
    # NEITHER sign cancels (1 -+ u both units): theta = +-1 cannot bump
    for (p, u) in ((7, 3), (11, 4)):
        alpha, v0 = 1 + u * p, 1 + (vp(k, p) or 0)
        ev = alpha ** ((p - 1) * k) - 1
        lee = k * p
        if not (vp(lee + ev, p) == v0 and vp(lee - ev, p) == v0):
            ok6d = False
    # regime C: c >= 2: NO balance (eigenvalue term subleading by c-1):
    # v = 1 + v_p(k) forced for ANY relative unit: tower law ROBUST
    for (p, c, u) in ((3, 2, 1), (5, 2, 1), (3, 3, 2)):
        alpha, v0 = 1 + u * p ** c, 1 + (vp(k, p) or 0)
        ev = alpha ** ((p - 1) * k) - 1
        lee = k * p
        if not (vp(ev, p) == c + (vp(k, p) or 0) > v0
                and vp(lee + ev, p) == v0 and vp(lee - ev, p) == v0):
            ok6e = False
check("T6c mu-locus ambiguity at alpha = 1+p", ok6c,
      "v_p(kp) = v_p(alpha^{(p-1)k}-1) = 1+v_p(k) (W1 balance) AND the"
      " unit parts agree up to sign (+ cancels to >= 2+v_p(k), - exact):"
      " the unknown relative unit theta of the twisted differential at"
      " Lee's tower locus makes BOTH Z/p^{1+v} and Z/p^{2+v} outcomes"
      " realizable -- pi_{2p} X(1+p) sits AT this ambiguity")
check("T6d generic-u rigidity (NEW)", ok6d,
      "for alpha = 1+up with u != +-1 mod p the balance holds but"
      " NEITHER sign cancels: a theta = +-1 twist CANNOT bump the tower"
      " -- the sign-ambiguity is SPECIFIC to the canonical generators"
      " u = +-1; a u-generic computation would dodge it (pre-registered"
      " dodge: compute pi_{2p} X(1+3p) instead)")
check("T6e c >= 2 rigidity (NEW)", ok6e,
      "for c >= 2 the eigenvalue term is subleading (c+v_p(k) >"
      " 1+v_p(k)): v = 1+v_p(k) forced for ANY relative unit -- the"
      " mu-locus tower law is ROBUST for alpha = 1+up^c, c >= 2: the"
      " fork's differential ambiguity lives ONLY on the bottom rung of"
      " the wild filtration")

print("\nCarrier guard: every gated object consumes psi^alpha (twisted"
      " bimodule, g_alpha FGL cocycle,")
print("eigenvalues alpha^w).  DH/Epstein: no ring, no bimodule, no"
      " cocycle -- dead at the object.")

print(f"\n{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
