"""R-INT / C6'' (PRIMARY per doc 23): the minimal Adams-twisted THH instance.

OBJECT. p odd, everything p-complete. For alpha in Z_p^x, psi^alpha is an
E_infinity automorphism of ku_p^ (Goerss-Hopkins-Miller on KU_p^ +
tau_{>=0} lax symmetric monoidal; I-doc sec 6). The graph pairing

    X(alpha) := <Gamma_id, Gamma_psi^alpha> = THH(ku_p^; (ku_p^)_{(1,psi^alpha)})
              = ku (x)_{ku (x)_S ku} ku_{psi^alpha}
              = derived fixed locus of psi^alpha on "Spec ku" over S.

Family transport (automorphism trick): <Gamma_f, Gamma_g> = X(g f^{-1});
the p-complete Adams family is the GROUP Z_p^x and the whole Gram is the
one-variable function X.  Wild direction: alpha = 1 + p.

WHAT THIS SCRIPT WITNESSES (pre-registered, fail-closed; every reading is
an exact-integer or interval-gated statement; no spectral-sequence
differential is fabricated -- the two unresolved-combinatorics branches of
the P-doc are kept separate wherever they differ):

  W1 (LTE tower law): for alpha = 1 + u p^c (p odd, u unit),
        v_p(alpha^w - 1) = c + v_p(w)   for ALL w >= 1.
      In particular alpha = 1+p: v_p(alpha^w - 1) = 1 + v_p(w).
      Exact integer check on a grid of p, c, w.

  W2 (toy Koszul shadow, the FULL derived pi_*-level answer): for
      R = Z_p[beta], phi(beta) = alpha beta, the twisted Hochschild complex
      over Z_p is the Koszul 2-term complex [R --(1-alpha)beta--> R]
      (R = R^e/(beta_1 - beta_2), regular element), so
        HH_0 = R/((1-alpha)beta):  weight 0: Z_p;  weight w>=1:
               Z/p^{v_p(alpha-1)}   (IDEAL collapse: the multiplicative
               relations contain (alpha-1)beta * beta^{w-1});
        HH_1 = ker = 0  (transverse: the cotangent line dies).
      Witnessed: the weight-w component of the ideal ((alpha^j-1)beta^j)_j
      has valuation min_j v_p(alpha^j-1) = v_p(alpha-1) EXACTLY, vs the
      single-relation (weight-graded) cokernel Z/p^{v_p(alpha^w-1)}; the
      two ladders differ exactly by v_p(w).  This is the branch
      discriminator: branch (i) "ideal collapse" = uniform Z/p^c ladder
      (the THH(F_p) half-ladder with multiplicity c); branch (ii)
      "weight-diagonal" = the LTE ladder Z/p^{c+v_p(w)}.

  W3 (the obstruction is exact FGL arithmetic): psi^alpha is NOT
      MU-linear; psi^alpha o (orientation) classifies F_{alpha beta}
      (x + y + alpha beta x y), strictly isomorphic to F_beta via
        g_alpha(x) = ((1+beta x)^alpha - 1)/(alpha beta).
      Witnessed (exact truncated integer series, beta = 1):
      G(F(x,y)) = G(x) + G(y) + G(x)G(y) for G = (1+x)^alpha - 1, and the
      coefficient valuations: the b_{k-1}-coordinate of the cocycle is
      binom(alpha, k)/alpha * beta^{k-1} with (alpha = 1+p)
        v_p(binom(1+p, k)) = 1 for 2 <= k <= p-1,  = 0 for k = p, p+1:
      every cocycle coordinate carries beta^{>=1} (twist invisible mod
      (p,beta): Lee Prop 4.1.1 layer F_p[mu] (x) Lambda(lambda_1,
      lambda_2) is UNCHANGED in both branches), the b_1..b_{p-2}
      coordinates are additionally p-divisible, and the FIRST UNIT
      coordinate is the t_1 = b_{p-1} coordinate times beta^{p-1} --
      the twist interacts at unit level exactly on the lambda_1/t_1
      locus, the class whose Bockstein tower carries Lee's untwisted
      Z/p^{1+v_p(k)} towers (Prop 4.1.5).

  W4 (family ratio law / p-adic log-distance): for the wild one-parameter
      family alpha_i = (1+p)^{k_i},
        v_p(alpha_i^w - alpha_j^w) = 1 + v_p(k_i - k_j) + v_p(w).
      The off-diagonal Gram per weight is the P-ADIC log-distance
      1 + v_p(k_i - k_j) (+ v_p(w) in branch (ii)) -- the p-adic face of
      doc 23's log|k-l| matrix.  Exact grid check; plus the ultrametric
      inequality v_p(k-m) >= min(v_p(k-l), v_p(l-m)) (the family Gram is
      hierarchical/Parisi-type, not Euclidean-log-type).

  W5 (tame/wild dichotomy, sharpened): tame alpha = Teichmuller lift
      (alpha^{p-1} = 1): v_p(alpha^w - 1) = 0 for ord(alpha) ∤ w and
      alpha^w = 1 exactly for ord | w: the fixed locus is the SUBLATTICE
      Z_p[beta^ord] -- periodic EXCESS lines (finite-order automorphism has
      positive-dimensional fixed locus), NOT "trivial".  Wild alpha:
      finite valuation at every w >= 1: no excess above weight 0, fully
      count-grade.  Witnessed with an exact Teichmuller lift mod p^N.

  W6 (regularized characteristic function, branch fork): the ladder
      Dirichlet series D_alpha(s) = sum_w log|X(alpha)_{2w}-cells| w^{-s}:
        branch (i):  D = c log p * zeta(s)         (no pole at s = 0;
                     value at 0:  -(c/2) log p);
        branch (ii): D = log p [ c zeta(s) + zeta(s)/(p^s - 1) ]
                   = c log p zeta(s) + zeta(s) * (-zeta_p'/zeta_p)(s):
                     the LOCAL Euler supply at p appears as a FACTOR;
                     simple pole at s = 0 with residue -1/2 (Abel
                     constant), finite part  zeta'(0) + (1/4 - c/2) log p.
      Witnessed: the Dirichlet identity at s = 3 against partial sums with
      a proven tail bound, and the s -> 0 pole/finite-part expansion by
      flint interval arithmetic against the closed form.

  W7 (Lefschetz/point-count reading): per weight w the branch-(ii) cell
      count is |Z_p/(alpha^w - 1)| = (p-part of alpha^w - 1) = the local
      Lefschetz denominator det(1 - d(psi^alpha) | weight-w line); the
      total through weight W is the p-adic Pochhammer
      v_p( prod_{w<=W} (alpha^w - 1) ) = sum_{w<=W} (c + v_p(w)).  Exact.
      The "bidegree (1,alpha)" expectation of doc 23 is REFUTED as a
      homological bidegree (the family is a group; all graphs are
      (1,1)-classes); alpha enters as the NORMAL/weight eigenvalue
      1 - alpha^w, i.e. through det(1 - dpsi), exactly as in a Lefschetz
      fixed-point count.

  W8 (doc-23 consumer matrices): per weight w, the wild-family matrix
        C_w[i,j] = 1 + v_p(k_i - k_j)            (i != j; branch (i);
                   add the constant v_p(w) for branch (ii)),
        C_w[i,i] = v_p(|T_{2w}|) = v_p( lcm(1..w+1)/(w(w+1)) )
      (true diagonal = p-part of the I-doc lcm ladder = untwisted
      THH(ku_p) torsion).  Gated: the diagonal formula against direct
      lcm arithmetic; signature of small sections printed as EXPLORATORY
      (not gated, no reading claimed).

Run:
    python3 -m scripts.numerics.witness.prime_twisted_adams_ku
"""
import math
import sys

FAIL = []


def check(name, ok, detail):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    if not ok:
        FAIL.append(name)


def vp(n, p):
    if n == 0:
        return None          # infinite
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


# ------------------------------------------------------------------ W1
print("W1: LTE tower law v_p(alpha^w - 1) = c + v_p(w), alpha = 1 + u p^c")
ok = True
for p in (3, 5, 7, 11, 13):
    M = p ** 40
    for c, u in ((1, 1), (1, 2), (2, 1), (3, 2)):
        if u % p == 0:
            continue
        alpha = 1 + u * p ** c
        aw = 1
        for w in range(1, 1501):
            aw = (aw * alpha) % M
            lhs = vp((aw - 1) % M, p)
            if lhs != c + vp(w, p):
                ok = False
                print(f"    mismatch p={p} c={c} u={u} w={w}")
                break
check("LTE law", ok,
      "v_p(alpha^w-1) = c + v_p(w) exact for p in {3,5,7,11,13}, "
      "c <= 3, w <= 1500; alpha = 1+p gives the tower Z/p^{1+v_p(w)}")

# ------------------------------------------------------------------ W2
print("\nW2: toy Koszul shadow -- ideal collapse vs weight-graded ladder")
ok_ideal = True
ok_diff = True
p = 5
c = 1
alpha = 1 + p
M = p ** 30
for w in range(1, 401):
    # weight-w component of the ideal ((alpha^j - 1) beta^j : j>=1):
    # spanned by (alpha^j - 1) Z_p, j = 1..w; valuation = min_j v_p(...)
    vmin = min(vp(pow(alpha, j, M) - 1, p) for j in range(1, w + 1))
    if vmin != c:                       # = v_p(alpha - 1)
        ok_ideal = False
    # weight-graded single relation: v_p(alpha^w - 1) = c + v_p(w)
    if (vp(pow(alpha, w, M) - 1, p) - vmin) != vp(w, p):
        ok_diff = False
check("ideal collapse", ok_ideal,
      "weight-w ideal component has valuation v_p(alpha-1) = c exactly "
      "(w <= 400): toy HH_0 ladder is the UNIFORM Z/p^c half-ladder; "
      "HH_1 = ker((1-alpha)beta) = 0 (nonzerodivisor): transverse, "
      "no cotangent excess")
check("branch discriminator", ok_diff,
      "weight-graded cokernel minus ideal cokernel = v_p(w) exactly: "
      "branch (i) uniform vs branch (ii) LTE differ by the v_p(w) bump")

# ------------------------------------------------------------------ W3
print("\nW3: orientation conjugation g_alpha -- exact FGL arithmetic")
# truncated integer series in x, y; beta = 1; G(x) = (1+x)^alpha - 1.
N = 14          # truncation order (degree <= N)
p3 = 5
alpha3 = 1 + p3


def poly_mul(a, b):
    out = [0] * (N + 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                if bj and i + j <= N:
                    out[i + j] += ai * bj
    return out


def poly_pow(a, k):
    out = [1] + [0] * N
    base = a[:]
    while k:
        if k & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        k >>= 1
    return out


# bivariate, encoded as dict (i,j) -> coeff, total degree <= N
def biv_mul(a, b):
    out = {}
    for (i, j), av in a.items():
        for (k, l), bv in b.items():
            if i + k + j + l <= N:
                out[(i + k, j + l)] = out.get((i + k, j + l), 0) + av * bv
    return out


def biv_pow(a, k):
    out = {(0, 0): 1}
    base = dict(a)
    while k:
        if k & 1:
            out = biv_mul(out, base)
        base = biv_mul(base, base)
        k >>= 1
    return out


X = {(1, 0): 1}
Y = {(0, 1): 1}
F = {(1, 0): 1, (0, 1): 1, (1, 1): 1}            # x + y + xy  (beta = 1)
onepF = dict(F)
onepF[(0, 0)] = 1                                 # 1 + F = (1+x)(1+y)
GF = biv_pow(onepF, alpha3)
GF[(0, 0)] -= 1                                   # G(F)
onepX = {(0, 0): 1, (1, 0): 1}
onepY = {(0, 0): 1, (0, 1): 1}
GX = biv_pow(onepX, alpha3)
GX[(0, 0)] -= 1
GY = biv_pow(onepY, alpha3)
GY[(0, 0)] -= 1
rhs = dict(GX)
for k, v in GY.items():
    rhs[k] = rhs.get(k, 0) + v
for k, v in biv_mul(GX, GY).items():
    rhs[k] = rhs.get(k, 0) + v
ok3 = all(GF.get(k, 0) == rhs.get(k, 0)
          for k in set(GF) | set(rhs))
check("strict-iso identity", ok3,
      "G(F(x,y)) = G(x)+G(y)+G(x)G(y) exactly (deg <= 14, p = 5, "
      "alpha = 6): g_alpha conjugates F_beta to F_{alpha beta}; "
      "psi^alpha o orientation = orientation o (twist by g_alpha): "
      "psi^alpha is NOT MU-linear, the twist is this strict iso")

ok3b = True
for pp in (3, 5, 7, 11, 13):
    vals = []
    for k in range(2, pp + 2):
        v = vp(math.comb(1 + pp, k), pp)
        vals.append((k, v))
        expect = 1 if k <= pp - 1 else 0
        if v != expect:
            ok3b = False
    if pp == p3:
        vals_show = vals
check("cocycle coordinate valuations", ok3b,
      f"v_p(binom(1+p,k)) (p=5): {vals_show}: p-divisible for "
      "2<=k<=p-1, all coords carry beta^{>=1} (twist invisible mod "
      "(p,beta): Lee Prop 4.1.1 layer unchanged); FIRST UNIT at k = p: "
      "the t_1 = b_{p-1} coordinate, beta^{p-1} -- the twist hits the "
      "lambda_1-locus (Lee Prop 4.1.5 tower source) at unit level")

# ------------------------------------------------------------------ W4
print("\nW4: family ratio law and ultrametric structure")
ok4 = True
p = 7
M = p ** 30
base = 1 + p
for ki in range(1, 30):
    for kj in range(1, ki):
        for w in (1, 2, p, p * 3, p * p, 60):
            a = pow(base, ki * w, M)
            b = pow(base, kj * w, M)
            if vp((a - b) % M, p) != 1 + vp(ki - kj, p) + vp(w, p):
                ok4 = False
check("ratio law", ok4,
      "v_p(alpha_i^w - alpha_j^w) = 1 + v_p(k_i-k_j) + v_p(w) exact "
      "(p = 7, k <= 30): Gram entries depend only on the RATIO -- the "
      "family is a group, all self-pairings equal THH(ku_p)")
ok4b = True
for k in range(1, 40):
    for l in range(1, 40):
        for m in range(1, 40):
            if k != l and l != m and k != m:
                if vp(k - m, p) < min(vp(k - l, p), vp(l - m, p)):
                    ok4b = False
check("ultrametric", ok4b,
      "v_p(k-m) >= min(v_p(k-l), v_p(l-m)): the p-adic log-distance "
      "matrix is hierarchical (Parisi-type), unlike archimedean log|k-l|")

# ------------------------------------------------------------------ W5
print("\nW5: tame/wild dichotomy (Teichmuller vs 1+p)")
p = 5
Nprec = 25
M = p ** Nprec
t = 2
for _ in range(60):                  # Teichmuller lift of 2 mod 5^25
    t = pow(t, p, M)
ok5 = (pow(t, p - 1, M) == 1) and (t % p == 2)
pattern_ok = True
for w in range(1, 200):
    tw = pow(t, w, M)
    if w % 4 == 0:
        if tw != 1:                  # exact fixed line mod p^25
            pattern_ok = False
    else:
        if vp((tw - 1) % M, p) != 0:
            pattern_ok = False
check("tame periodic excess", ok5 and pattern_ok,
      "Teichmuller alpha (ord 4, p = 5): alpha^w = 1 exactly iff 4 | w; "
      "fixed locus = sublattice Z_p[beta^4] (periodic EXCESS lines, "
      "Lefschetz fixed locus of a finite-order automorphism); tame "
      "weights off the sublattice are unit-transverse (no torsion)")
ok5b = all(vp(pow(1 + p, w, M) - 1, p) is not None and
           vp(pow(1 + p, w, M) - 1, p) <= 1 + 3 for w in range(1, 100))
check("wild no-excess", ok5b,
      "alpha = 1+p has infinite order: v_p(alpha^w - 1) finite at every "
      "w >= 1: no excess above weight 0 -- fully count-grade (P2)")

# ------------------------------------------------------------------ W6
print("\nW6: regularized characteristic function D_alpha(s), branch fork")
try:
    import flint
    prec_old = flint.ctx.prec
    flint.ctx.prec = 300
    p = 5
    c = 1
    logp = flint.arb(p).log()
    s = flint.arb(3)
    # partial sum of branch (ii): sum (c + v_p(w)) log p w^{-3}
    W = 4000
    partial = flint.arb(0)
    for w in range(1, W + 1):
        partial += (c + vp(w, p)) * logp / flint.arb(w) ** 3
    closed = logp * (c * flint.acb(3).zeta().real
                     + flint.acb(3).zeta().real / (flint.arb(p) ** 3 - 1))
    # tail bound: terms <= (c + log_p w + 1) log p w^{-3} <= C w^{-2.5}
    # for w > W; bound crudely by integral of (c+1+log_5 w) log p w^-3
    tail = (c + 1 + math.log(W) / math.log(p) + 1) * float(logp) \
        * (1.0 / (2 * W ** 2) + 1.0)  # extremely crude upper envelope
    tail = (c + 2 + math.log(W) / math.log(p)) * float(logp) / (W ** 2)
    diff = abs(float(partial - closed))
    ok6 = diff < tail * 2
    check("Dirichlet identity at s=3", ok6,
          f"|partial - logp(c zeta + zeta/(p^s-1))| = {diff:.3e} "
          f"< tail bound {tail * 2:.3e} (W = {W}): the branch-(ii) "
          "ladder transform IS c log p zeta(s) + zeta(s)(-zeta_p'/"
          "zeta_p)(s) -- the local Euler supply appears as a factor")

    # s -> 0: f(s) = logp (c zeta(s) + zeta(s)/(p^s - 1)); pole -1/(2s),
    # finite part zeta'(0) - (1/4 + c/2) log p.
    h = flint.arb(1) / flint.arb(10) ** 30
    def f(sv):
        sv = flint.acb(sv)
        return (logp * (c * sv.zeta()
                        + sv.zeta() / ((flint.acb(p) ** sv) - 1))).real
    fp_plus = f(h) + flint.arb(1) / (2 * h)
    fp_minus = f(-h) + flint.arb(1) / (2 * (-h))
    fp = (fp_plus + fp_minus) / 2
    zprime0 = -(flint.arb(2) * flint.arb.pi()).log() / 2
    target = zprime0 + (flint.arb(1) / 4 - flint.arb(c) / 2) * logp
    err = abs(float(fp - target))
    resid = float((f(h) - f(-h)) * h)        # ~ -1/2 * ... residue probe
    ok6b = err < 1e-12
    check("s=0 expansion (branch ii)", ok6b,
          f"finite part = zeta'(0) + (1/4 - c/2) log p to {err:.1e}; "
          f"pole residue -1/2 (probe {resid:.6f}); branch (i) instead "
          f"gives NO pole and value -(c/2) log p = "
          f"{-float(logp) / 2:.6f}: the s = 0 behaviour DISCRIMINATES "
          "the branches (pole vs no pole)")
    flint.ctx.prec = prec_old
except ImportError:
    check("Dirichlet identity at s=3", False, "python-flint unavailable")

# ------------------------------------------------------------------ W7
print("\nW7: Lefschetz / p-adic Pochhammer reading")
p = 5
c = 1
alpha = 1 + p
ok7 = True
# exact unbounded-integer product for W <= 60 (no modulus, no cap)
for W in (10, 30, 60):
    prod = 1
    tot = 0
    aw = 1
    for w in range(1, W + 1):
        aw = aw * alpha
        prod *= aw - 1
        tot += c + vp(w, p)
    if vp(prod, p) != tot:
        ok7 = False
# term-wise valuations to W = 500 (each term mod p^40, vp << 40)
M = p ** 40
aw = 1
tot = 0
acc = 0
for w in range(1, 501):
    aw = (aw * alpha) % M
    acc += vp((aw - 1) % M, p)
    tot += c + vp(w, p)
if acc != tot:
    ok7 = False
check("Pochhammer valuation", ok7,
      "v_p(prod_{w<=W}(alpha^w - 1)) = sum (c + v_p(w)) exact (W <= 500): "
      "per-weight cell count = local Lefschetz factor det(1 - d psi^alpha"
      " | weight-w line); alpha is a NORMAL eigenvalue, not a bidegree -- "
      "the family is a group of (1,1)-classes (doc 23's (1,alpha) "
      "expectation refuted as bidegree, relocated to the normal data)")

# ------------------------------------------------------------------ W8
print("\nW8: doc-23 consumer -- per-weight family matrices")
p = 3
ok8 = True
for w in range(1, 200):
    L = 1
    for n in range(1, w + 2):
        L = L * n // math.gcd(L, n)
    lhs = vp(L // (w * (w + 1)), p)
    rhs = math.floor(math.log(w + 1) / math.log(p) + 1e-12) \
        - vp(w, p) - vp(w + 1, p)
    # guard against float log edge: recompute floor properly
    k = 0
    while p ** (k + 1) <= w + 1:
        k += 1
    rhs = k - vp(w, p) - vp(w + 1, p)
    if lhs != rhs:
        ok8 = False
check("true diagonal (p-part of lcm ladder)", ok8,
      "v_p(|T_2w|) = floor(log_p(w+1)) - v_p(w) - v_p(w+1) exact "
      "(w < 200): the diagonal slot of the doc-23 corrected form is the "
      "p-part of the I-doc lcm ladder (self-pairing = untwisted THH)")

try:
    import numpy as np
    print("    EXPLORATORY (ungated): signatures of "
          "[diag = v_p|T_2w|, offdiag = 1 + v_p(k_i - k_j)], p = 3")
    for w in (8, 10, 27, 40, 100):
        L = 1
        for n in range(1, w + 2):
            L = L * n // math.gcd(L, n)
        d = vp(L // (w * (w + 1)), p)
        nfam = 9
        Mx = np.zeros((nfam, nfam))
        for i in range(nfam):
            for j in range(nfam):
                Mx[i, j] = d if i == j else 1 + vp((i + 1) - (j + 1), p)
        ev = np.linalg.eigvalsh(Mx)
        npos = int((ev > 1e-9).sum())
        nneg = int((ev < -1e-9).sum())
        print(f"      w={w:>3} diag={d}: signature (+{npos}, -{nneg}) "
              f"eigs[{ev[0]:.2f}..{ev[-1]:.2f}]"
              + ("   <-- Lorentzian" if npos == 1 and nneg == nfam - 1
                 else ""))
except ImportError:
    print("    (numpy unavailable, exploratory block skipped)")

print(f"\n{'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
sys.exit(0 if not FAIL else 1)
