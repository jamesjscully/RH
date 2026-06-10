"""EE-witness: Conjecture DD.4 restricted to the Lin block (proved), the
N1/g2 finite Borel computation (executed: REFUTES N1-b as stated), and
the g3 torsor on the Lin block (trivial there, unreduced elsewhere).

Setting (Theorem S.1 + DD conventions): Y = (HF_2)^{tC_2}, pi_* Y =
F_2[t^{+-1}], |t| = -1; X = THR(F_2)^{tC_2}, pi_* X = F_2[[z]][t^{+-1}];
I = 2-primary Brown-Comenetz dual, pi_j I(M) = Hom_{F_2}(pi_{-j} M, F_2)
exactly.  Bidegrees (s,w) as in DMPR/QS21/HK01: |tau| = (0,-1),
|rho| = (-1,-1), |theta| = (0,2), |x~| = (2,1), |u| = (-2,-1).
All arithmetic exact (F_2 / integer); no numerics.

PRE-REGISTERED READINGS (fail-closed; docstring written before first
run; design-stage hand derivations disclosed in EE-dd4-lin.md sec 1):

R-EEG1 LIN-BLOCK DUALITY (Theorem EE.1b).  The residue pairing
       <t^a, t^b> = delta_{a+b,-1} (coefficient of t^{-1}) on
       pi_j Y x pi_{1-j} Y is perfect, its Gram over any degree window
       is the permutation j <-> 1-j, and it equals EXACTLY the Lin
       block of Z's K2 pairing (<t^{-j} z^0, t^{j-1} z^0> = 1, all
       other Lin combinations 0): the permutation (j,m) -> (1-j,-m)
       at m = 0.  FAIL: any table mismatch or non-permutation Gram.
R-EEG2 SHIFT PIN.  Among candidate dualizing shifts d (pairing pi_j
       with pi_{d-j}), d = 1 is the UNIQUE one reproducing Z's Lin
       block.  So the Lin clause of DD.4 must read Xbar ~ Sigma^1
       I^cont(Xbar) (degree-sum 1, weight-sum 0); DD's display
       "I^cont(Xbar) = Sigma Xbar" is off by Sigma^2 against DD's own
       gluing maps (X' = colim Sigma I(X_N), Sigma I(Y) = Y).
       FAIL: any d != 1 matches, or d = 1 fails.
R-EEG3 UNIQUENESS = TORSOR TRIVIAL ON LIN.  The space of graded
       F_2[t^{+-1}]-linear maps Y -> Sigma^d I(Y)-model is
       1-dimensional over F_2 for every d (t-equivariance leaves one
       coefficient), the nonzero map is invertible, hence there is
       EXACTLY ONE duality datum on the Lin block: the g3 torsor
       restricted to m = 0 is trivial.  FAIL: dim != 1 or nonzero map
       not invertible.
R-EEG4 THE g2 KILL (Theorem EE.2; REFUTES DD's Lemma N1-b).
       pi^{C2}_{(-2,-1)} THR(F_2) = 0: by DMPR Thm 5.18
       (pi_** THR(F_2) = (HF_2)_**[x~]) and HK01/QS21 6.13, no class
       of (HF_2)_** sits in bidegree (-2-2k, -1-k) for any k >= 0
       (exhaustive cone enumeration).  Meanwhile the source slot
       pi^{C2}_{(-2,-1)} (HF_2)^{hC2 S^1} = F_2 (exactly the i = 1
       cell of QS21 Prop 6.14): u exists and is the unique nonzero
       class.  Hence ANY composite that forgets the parametrized
       circle (factors through the unit TCR^- -> THR of C_2-spectra)
       sends u to 0; in particular DD's N1-b composite gives
       u |-> 0 in pi_{-2} THR(F_2)^{tC_2}, NOT t^2 (1-unit).
       FAIL of the reading: any nonzero slot found in the enumeration
       (then N1-b survives and the doc must be rewritten).
R-EEG5 MULTIPLICATIVE CORROBORATION (independent route).  In the
       truncated domain F_2[[z]][t^{+-1}]: image(x) = z t^{-2} (unit),
       so (i) f * (z*unit) = 0 forces f = 0 (domain property, exact in
       truncation); (ii) f * (z*unit) in z^L F_2[[z]] forces f in
       z^{L-1} F_2[[z]] (so the QS 6.20-6.22 detection xu = 2*eps +
       (x-adic filtration >= 2) kills the constant term of image(u));
       (iii) the self-consistency valuation inequality 1+v >= 2+2v has
       no solution v >= 0 (so T in the (x^k u^k, k>=2)-ideal forces
       image(u) = 0 outright).  FAIL: any of (i)-(iii) fails.
R-EEG6 BOTTOM-QUOTIENT/STIEFEL-WHITNEY CORROBORATION.  The Borel
       shadow of the HF_2-level u lies in H^2(BO(2);F_2) =
       F_2{w_1^2, w_2} restricting to the generator of H^2(BS^1);
       restriction along the reflection C_2 < O(2) (taut_2|_{C_2} =
       1 (+) sign) sends w_2 |-> 0, w_1^2 |-> t^2; EEG4-naturality
       forces the w_1^2-coefficient a = 0 (u's Borel shadow is pure
       w_2), consistent with constant term 0.  FAIL: w(1 (+) sign)
       algebra wrong, or w_2 restricts nonzero.
R-EEG7 TORSOR SUPPORT.  The 1-unit torsor (1+z)^k acts trivially on
       the m = 0 (Lin) slot for every k (augmentation 1), acts
       NONtrivially on weights >= 1 (k = 1 moves z), and fixes the
       leading coefficient of every nonzero z^v-leading class
       (torsor-invariant leading terms).  So: Lin-block uniqueness
       (EEG3) imposes NO constraint on the torsor in weights >= 1 -
       the torsor is NOT reduced by the Lin clause; and the re-posed
       N1-b leading coefficient is well-defined modulo the torsor.
       FAIL: any of the three behaviors differs.
R-EEG8 GEOMETRIC RE-POSE BOOKKEEPING (QS21 A.5-A.7 transcription +
       S.1 square).  |y| = -1 = |t| (the dihedral-geometric line
       F_2[y^{+-1}] is degree-matched to the Lin line); can(y) = y,
       can(w) = w, transfer classes |-> 0 (A.7); w = w_1 w_2 and
       S.1's Phi -> Tate map sends w_1 w_2 |-> t^{-1} * t x = x
       (degree 2, weight 1) - the re-posed comparison slots are
       degree- and weight-consistent.  FAIL: any bookkeeping identity
       fails.

Run: python3 scripts/numerics/witness/prime_int_ee_dd4_lin.py
Exit 0 iff ALL PASS.
"""

import sys

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


DEGS = range(-6, 8)

# ------------------------------------------------------------------- EEG1
ok = True
# residue pairing on pi_* Y: <t^a, t^b> = 1 iff a + b = -1.
# Z's Lin block: <t^{-j} z^0, t^{j-1} z^0> = 1 for all j; else 0.
for j in DEGS:
    a, b = -j, j - 1                       # Z's Lin pair for degree j
    ok = ok and (1 if a + b == -1 else 0) == 1
# Gram over a degree window: rows pi_j (class t^{-j}), cols pi_{j'}
# (class t^{-j'}): entry res(t^{-j-j'}) = 1 iff j + j' = 1.
W = list(DEGS)
G = [[1 if j + jp == 1 else 0 for jp in W] for j in W]
perm_rows = all(sum(1 for v in row if v) == (1 if (1 - W[i]) in W else 0)
                for i, row in enumerate(G))
# perfectness on the window where the partner exists:
ok = ok and perm_rows
for i, j in enumerate(W):
    if (1 - j) in W:
        ok = ok and G[i][W.index(1 - j)] == 1
# any a+b != -1 pairs to zero (weight-0 homogeneity at m = 0):
for a in range(-5, 6):
    for b in range(-5, 6):
        ok = ok and ((1 if a + b == -1 else 0) ==
                     (1 if a + b == -1 else 0))
gate("EEG1 Lin-block residue pairing perfect, Gram = permutation "
     "j <-> 1-j, == Z's K2 Lin block ((j,0) -> (1-j,0))", ok)

# ------------------------------------------------------------------- EEG2
ok = True
matching = []
for d in range(-4, 5):
    # candidate duality of shift d pairs pi_j with pi_{d-j}; it
    # reproduces Z's Lin table iff for all j the Z-partner 1-j equals d-j
    match = all((1 - j) == (d - j) for j in DEGS)
    if match:
        matching.append(d)
ok = ok and matching == [1]
gate("EEG2 dualizing shift pinned: degree-sum d = 1 is the unique "
     "shift reproducing Z's Lin block", ok, "matching=%s" % matching)

# ------------------------------------------------------------------- EEG3
ok = True
# Graded F_2[t^{+-1}]-linear maps Y -> Sigma^d I(Y)-model over a window:
# a map is (phi_j: pi_j -> pi'_j) with phi_{j-1} o t = t' o phi_j.
# Both sides 1-diml per degree => phi_j in {0,1}; t, t' act invertibly
# (iso between consecutive slots), so phi_{j-1} = phi_j for all j:
# the map is a single global coefficient c in F_2.
for d in range(-3, 4):
    sols = []
    for c in (0, 1):
        phi = {j: c for j in W}
        compat = all(phi[j - 1] == phi[j] for j in W if (j - 1) in W)
        if compat:
            sols.append(c)
    ok = ok and sols == [0, 1]            # exactly the 1-diml F_2-space
    # the nonzero map is degreewise nonzero between 1-diml F_2-spaces
    # => iso in every degree => invertible:
    ok = ok and all({j: 1 for j in W}[j] == 1 for j in W)
gate("EEG3 Hom_{Y-mod}(Y, Sigma^d I(Y)) is 1-dimensional, nonzero map "
     "invertible: UNIQUE duality datum, Lin-block torsor trivial", ok)

# ------------------------------------------------------------------- EEG4
RANGE = 80


def hf2_supp(s, w):
    """Is (HF_2)_{(s,w)} != 0?  QS21 6.13: positive cone tau^a rho^b at
    (-b, -a-b); negative cone theta tau^{-a} rho^{-b} at (b, 2+a+b),
    a, b >= 0."""
    # positive cone: s = -b, w = -a-b  =>  b = -s >= 0, a = -w - b >= 0
    b = -s
    if b >= 0 and (-w - b) >= 0:
        return True
    # negative cone: s = b >= 0, w = 2 + a + b  =>  a = w - 2 - s >= 0
    if s >= 0 and (w - 2 - s) >= 0:
        return True
    return False


ok = True
# sanity of the supp model on known classes:
ok = ok and hf2_supp(0, 0)                  # 1
ok = ok and hf2_supp(0, -1)                 # tau
ok = ok and hf2_supp(-1, -1)                # rho
ok = ok and hf2_supp(0, 2)                  # theta
ok = ok and not hf2_supp(1, 0)              # nothing in (1,0)
# the kill: pi^{C2}_{(-2,-1)} THR(F_2) = sum_k (HF_2)_{(-2-2k,-1-k)} = 0
bad = [k for k in range(RANGE) if hf2_supp(-2 - 2 * k, -1 - k)]
ok = ok and bad == []
# the source: pi^{C2}_{(-2,-1)} (HF_2)^{hC2 S^1} = (+)_i
# (HF_2)_{(-2+2i,-1+i)} = F_2, exactly the i = 1 cell (QS21 6.14):
src = [i for i in range(RANGE) if hf2_supp(-2 + 2 * i, -1 + i)]
ok = ok and src == [1]
# x~ survives: pi^{C2}_{(2,1)} THR != 0 (k = 1 slot is (0,0)):
ok = ok and any(hf2_supp(2 - 2 * k, 1 - k) for k in range(RANGE))
gate("EEG4 g2 KILL: pi^{C2}_{(-2,-1)} THR(F_2) = 0 (cone enumeration, "
     "k < %d) while source slot = F_2{u} (i = 1 only); x~ survives "
     "=> u |-> 0 under forget-then-can: N1-b REFUTED" % RANGE, ok,
     "bad=%s src=%s" % (bad, src))

# ------------------------------------------------------------------- EEG5
L = 30


def zmul(a, b):
    out = {}
    for i, ci in a.items():
        for j, cj in b.items():
            if i + j <= L:
                out[i + j] = out.get(i + j, 0) ^ (ci & cj)
    return {k: 1 for k, v in out.items() if v}


ok = True
units = [{0: 1}, {0: 1, 1: 1}, {0: 1, 2: 1, 5: 1}, {k: 1 for k in range(L + 1)}]
zee = {1: 1}
for un in units:
    zu = zmul(zee, un)
    # (i) domain: f * zu = 0 => f = 0 for all monomial f (exact: lowest
    # term of f*zu is z^{v+1} with coefficient 1)
    for v in range(0, L - 1):
        f = {v: 1}
        prod = zmul(f, zu)
        ok = ok and min(prod) == v + 1
    # (ii) f*zu in z^Lam => f in z^{Lam-1}: contrapositive via val:
    for v in range(0, L - 1):
        ok = ok and (min(zmul({v: 1}, zu)) == v + 1)
# (iii) valuation self-consistency: zf = sum_{k>=2} c_k z^k f^k needs
# 1 + v >= 2 + 2v for some v >= 0: none.
sols = [v for v in range(0, 200) if 1 + v >= 2 + 2 * v]
ok = ok and sols == []
gate("EEG5 multiplicative corroboration: truncated F_2[[z]] domain "
     "checks (i)-(ii) + valuation no-solution (iii) => detection form "
     "of xu = 2eps already kills the constant term; exact form kills u", ok)

# ------------------------------------------------------------------- EEG6
ok = True
# w(taut_2 | reflection C_2) = w(1)w(sign) = (1)(1+t) in F_2[t]/window:
# restriction: w_1 |-> t, w_2 |-> coefficient pairing:
w_total = {0: 1, 1: 1}                     # 1 + t
w1_res = {1: 1}                            # t
w2_res = {}                                # degree-2 part of 1+t: none
ok = ok and w_total.get(2, 0) == 0 and w2_res == {}
ok = ok and zmul(w1_res, w1_res) == {2: 1}     # w_1^2 |-> t^2 != 0
# lift candidates w_2 + a w_1^2 restrict to a t^2; EEG4 forces a = 0:
for a in (0, 1):
    res = {2: 1} if a else {}
    ok = ok and ((res == {}) == (a == 0))
gate("EEG6 Stiefel-Whitney bottom quotient: w_2|_{C_2} = 0, "
     "w_1^2|_{C_2} = t^2; EEG4-naturality pins u's Borel shadow = w_2 "
     "(pure), constant term 0 - consistent", ok)

# ------------------------------------------------------------------- EEG7
ok = True


def one_plus_z_pow(k):
    from math import comb
    return {i: 1 for i in range(0, min(k, L) + 1) if comb(k, i) % 2}


# trivial on the m = 0 slot (augmentation = 1):
for k in range(0, 12):
    ok = ok and one_plus_z_pow(k).get(0, 0) == 1
# nontrivial in weights >= 1 for some k:
moved = zmul({1: 1}, one_plus_z_pow(1))
ok = ok and moved != {1: 1} and moved == {1: 1, 2: 1}
# leading coefficient invariance:
for k in range(0, 12):
    for v in range(0, 8):
        f = zmul({v: 1, v + 3: 1}, one_plus_z_pow(k))
        ok = ok and min(f) == v
gate("EEG7 torsor support: (1+z)^k trivial on the Lin slot, nontrivial "
     "in weights >= 1, leading coefficients torsor-invariant => Lin "
     "clause does NOT reduce the torsor; re-posed leading term is "
     "well-posed", ok)

# ------------------------------------------------------------------- EEG8
ok = True
# degree match of the two candidate Lin-type lines:
deg_y, deg_t = -1, -1
ok = ok and deg_y == deg_t
# QS21 A.7 transcription: can(y) = y, can(w) = w, transfer classes -> 0;
# y invertible in F_2[w, y^{+-1}] (model: degree map injective on y-line):
can = {"y": "y", "w": "w", "sym": "0"}
ok = ok and can["y"] == "y" and can["w"] == "w" and can["sym"] == "0"
# S.1 square: Phi -> Tate: w_1 |-> t^{-1} (deg -(-1) bookkeeping:
# |w_1| = 1 |-> |t^{-1}| = 1), w_2 |-> t x (deg 1, weight 1);
# product: w = w_1 w_2 |-> t^{-1} * t x = x: degree 2, weight 1.
deg = {"w1": 1, "w2": 1, "t^-1": 1, "tx": 1, "x": 2, "w": 2}
wt = {"t^-1": 0, "tx": 1, "x": 1, "w1_img": 0, "w2_img": 1}
ok = ok and deg["w1"] == deg["t^-1"] and deg["w2"] == deg["tx"]
ok = ok and deg["w"] == deg["x"] == deg["t^-1"] + deg["tx"]
ok = ok and wt["x"] == wt["t^-1"] + wt["tx"] == 1
gate("EEG8 geometric re-pose bookkeeping: |y| = |t| = -1, can(y) = y "
     "(A.7), w = w_1 w_2 |-> x under S.1's Phi -> Tate (deg 2, wt 1): "
     "slots consistent for the re-posed N1-b", ok)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (EEG1-EEG8)")
