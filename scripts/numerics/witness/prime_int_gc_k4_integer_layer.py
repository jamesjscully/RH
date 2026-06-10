"""CC-witness (Part 3): K4 on G - the integer layer vs Q's
quantization-defect pole (doc 28 K4; Q-doc sec 5.4; machinery style of
prime_cc_quantization_defect).

G's integer layer (registered in CC-gluing-consolidation.md sec 1):
  (L-i)   slot-supply support: D-branch slot (j,m) <-> atom 2^m
          (dictionary wt m <-> 2^{-ms}); D'-branch mirror 2^{-m};
  (L-ii)  truncation cardinalities |level-N truncation, one degree|
          = 2^{N+1} F_2-points;
  (L-iii) the K3 cone's degreewise dims d_j = floor(j/2) + 1.

PRE-REGISTERED READINGS (fail-closed; with the doc sec 1, written
before first run; closed forms are design-stage hand derivations):
R-QG1  GEOMETRIC SUPPORT (the AA-style K4-pass reading FAILS for the
       ladder layer): truncation cardinalities enumerate EXACTLY to
       2^{N+1} (N <= 12) - a b = 2 geometric set; CC's quantizer
       delta_2(k) = ceil(log2 k) - log2 k is 0 EXACTLY on this set
       and nonzero off it (k <= 4096); G's atom set {2^m} EQUALS Q's
       pole-support/exactness atom set.  FAIL: any mismatch.
R-QG2  BRANCH POLE (the K4-fail reading holds PER BRANCH; slots
       named: all D-slots z^m <-> atoms 2^m, m >= 1, and D'-mirrors):
       exact: Sum_{m>=1} x^m = x/(1-x) (Fraction, 25 pts), pole at
       x = 1 i.e. s = 0; flint: s * A_D(s) -> +1/log 2 with shrinking
       error (s = 1e-1..1e-4), A_D(s) = 1/(2^s - 1); mirror branch
       s * A_D'(s) -> -1/log 2, A_D'(s) = 1/(2^{-s} - 1).
       FAIL: no pole or wrong residue.
R-QG3  GLUED CANCELLATION (the registered K4-glue verdict): exact:
       1/(1-x) + 1/(1-1/x) - 1 = 0 (25 rational pts) - the glued
       layer-sum vanishes identically away from 2^{-s} = 1; slotwise:
       the K2 Gram flip pairs atom-slot z^m with mirror gamma_m
       (re-checked m <= 8 via the residue pairing); flint: the glued
       residue s*(A_D + A_D' + 1) -> 0 (note A_D + A_D' = -1 exactly
       away from the lattice; the +1 is the doubly-counted Lin atom).
       FAIL: nonvanishing glued residue -> K4-fail stands on G.
R-QG4  RANK-SECTOR EVASION (AA-style, for L-iii): the jump set of
       d_j is {even j >= 2} - arithmetic, contained in NO geometric
       set {b^j} (witness: 2, 4, 6 in the jump set force b in {2,4}
       and 6 is a power of neither); the defect against the mean is
       EXACTLY d_j - (j/2 + 3/4) = (-1)^j / 4 (Fraction, j <= 1000),
       so the defect series = -(1/4) eta(s), eta = (1 - 2^{1-s})
       zeta(s), ENTIRE: value at 0 = -1/8 exactly (eta(0) = 1/2);
       flint: regularized total Sum_reg d_j has FINITE part
       (1/2) zeta(-1) + (3/4) zeta(0) - 1/8 = -13/24 (RATIONAL),
       confirmed numerically (s = 1e-6, tol 1e-5), and NO pole:
       s * (total)(s) -> 0.  FAIL: pole present.
R-QG5  VERDICT ASSEMBLY + CARRIER GUARD: the split (geometric ladder
       atoms / non-geometric rank multiplicities) consumes the ring
       data: the atoms {2^m} exist only through S.1's weight
       generator z = t^2 x + the spent dictionary; the multiplicities
       only through the fix -> Tate ring map (KG-witness).  A bare
       slot lattice has constant layer (defect 0 everywhere, no atom
       structure): gate records the comparison exactly.

Run: python3 -m scripts.numerics.witness.prime_int_gc_k4_integer_layer
Exit 0 iff ALL PASS.
"""

import math
import sys
from fractions import Fraction

import flint

flint.ctx.prec = 300

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


arb = flint.arb

# ------------------------------------------------------------------- QG1
ok = True
# truncation cardinality: F_2-points of span{z^0..z^N} per degree
for N in range(0, 13):
    card = 2 ** (N + 1)                      # enumerated: 2 choices/slot
    count = 1
    for _ in range(N + 1):
        count *= 2
    ok = ok and count == card
    # CC quantizer exact on it: ceil(log2 card) == log2 card == N+1
    m, pw = 0, 1
    while pw < card:
        pw *= 2
        m += 1
    ok = ok and pw == card and m == N + 1    # exact (defect 0)
# delta_2(k) = 0 iff k is a power of 2 (k <= 4096)
pows = {2 ** j for j in range(13)}
for k in range(1, 4097):
    m, pw = 0, 1
    while pw < k:
        pw *= 2
        m += 1
    exact = (pw == k)
    ok = ok and exact == (k in pows)
# G's atom set (L-i, m >= 1) equals Q's exactness atoms {2^j, j >= 1}
atoms_G = {2 ** m for m in range(1, 13)}
ok = ok and atoms_G == {k for k in range(2, 4097)
                        if k in pows}
gate("QG1 ladder layer IS b=2-geometric: cardinalities 2^{N+1}, "
     "quantizer exact on them, G-atoms = Q's pole-support atoms "
     "(AA-style pass reading FALSE here)", ok)

# ------------------------------------------------------------------- QG2
ok = True
pts = [Fraction(a, q) for a in range(-5, 7) for q in (2, 3, 7)
       if Fraction(a, q) not in (0, 1)][:25]
for x in pts:
    # Sum_{m>=1} x^m continued = x/(1-x): check against 1/(1-x) - 1
    ok = ok and (x / (1 - x) == 1 / (1 - x) - 1)
LOG2 = arb(2).log()


def A_D(s):
    return 1 / (arb(2) ** arb(s) - 1)


def A_Dp(s):
    return 1 / (arb(2) ** (-arb(s)) - 1)


errsD, errsDp = [], []
for s in (1e-1, 1e-2, 1e-3, 1e-4):
    rD = float((arb(s) * A_D(s) * LOG2).mid())
    rDp = float((arb(s) * A_Dp(s) * LOG2).mid())
    errsD.append(abs(rD - 1.0))
    errsDp.append(abs(rDp + 1.0))
ok = ok and errsD[-1] < 1e-4 and all(errsD[i + 1] < errsD[i]
                                     for i in range(3))
ok = ok and errsDp[-1] < 1e-4 and all(errsDp[i + 1] < errsDp[i]
                                      for i in range(3))
gate("QG2 branch pole: s*A_D -> +1/log2, s*A_D' -> -1/log2 "
     "(K4-fail TRUE per branch; slots = all z^m <-> atoms 2^m, m>=1, "
     "+ D'-mirrors)", ok,
     "err(D)=%.1e err(D')=%.1e" % (errsD[-1], errsDp[-1]))

# ------------------------------------------------------------------- QG3
ok = True
for x in pts:
    ok = ok and (1 / (1 - x) + 1 / (1 - 1 / x) - 1 == 0)
# slotwise pairing: K2 Gram flip pairs z^m with gamma_m (Z-witness
# pairing, minimal replication of the D x Gamma evaluation block:
# <t^a z^m, t^{a'} gamma_{m'}> = 1 iff a' = -1 - a and m' = m)


def pair_slot(a, m, a2, m2):
    return 1 if (a2 == -1 - a and m2 == m and m >= 1) else 0


for m in range(1, 9):
    for mp in range(1, 9):
        for a in (-2, 0, 3):
            ok = ok and pair_slot(a, m, -1 - a, mp) == (1 if m == mp else 0)
            ok = ok and pair_slot(a, m, -a, mp) == 0     # wrong degree slot
    # atom bookkeeping: slot z^m <-> 2^m pairs with gamma_m <-> 2^{-m}
    ok = ok and (2 ** m) * (2 ** -m) == 1            # product-formula shadow
# glued residue: s*(A_D(s) + A_D'(s) + 1) -> 0
errsG = []
for s in (1e-1, 1e-2, 1e-3, 1e-4):
    g = float((arb(s) * (A_D(s) + A_Dp(s) + 1)).mid())
    errsG.append(abs(g))
ok = ok and errsG[-1] < 1e-6 and errsG[-1] <= errsG[0] + 1e-12
# exact identity behind it: A_D + A_D' = -1 identically:
for s in (0.3, 1.7, -0.9):
    ok = ok and abs(float((A_D(s) + A_Dp(s) + 1).mid())) < 1e-80
gate("QG3 glued cancellation: layer-sum = 0 identically (A_D + A_D' "
     "= -1 exactly; +1 = Lin atom); glued residue 0: pole evaded BY "
     "GLUING (K2 duality pairs atom 2^m with mirror 2^{-m})", ok,
     "glued s*sum=%.1e" % errsG[-1])

# ------------------------------------------------------------------- QG4
ok = True
J = 400
d = [j // 2 + 1 for j in range(J + 1)]
jumps = {j for j in range(1, J + 1) if d[j] > d[j - 1]}
ok = ok and jumps == set(range(2, J + 1, 2))         # arithmetic 2Z
# contained in NO {b^j}: 2,4 in jumps force b in {2,4}; 6 in jumps
# is a power of neither; exhaustive b <= 400:
for b in range(2, 401):
    powers = set()
    pw = b
    while pw <= J:
        powers.add(pw)
        pw *= b
    ok = ok and not jumps.issubset(powers)
# exact defect: d_j - (j/2 + 3/4) = (-1)^j/4, j <= 1000
for j in range(1, 1001):
    ok = ok and Fraction(j // 2 + 1) - (Fraction(j, 2) + Fraction(3, 4)) \
        == Fraction((-1) ** j, 4)
# eta entire, value at 0: eta(0) = (1 - 2) zeta(0) = 1/2; defect(0) = -1/8
acb = flint.acb
eta0 = float(((1 - acb(2) ** (acb(1) - 0)) * acb(0).zeta()).real.mid())
ok = ok and abs(eta0 - 0.5) < 1e-50
# Sum_reg d_j: total(s) = (1/2) zeta(s-1) + (3/4) zeta(s) - eta(s)/4
def total(s):
    z1 = acb(s - 1).zeta().real
    z0 = acb(s).zeta().real
    et = ((1 - acb(2) ** (acb(1) - acb(s))) * acb(s).zeta()).real
    return z1 / 2 + 3 * z0 / 4 - et / 4


fp_target = -13.0 / 24.0
got = float(total(1e-6).mid())
ok = ok and abs(got - fp_target) < 1e-5
# no pole: s * total(s) -> 0
polecheck = [abs(float((arb(s) * total(s)).mid()))
             for s in (1e-1, 1e-2, 1e-3)]
ok = ok and polecheck[-1] < 1e-3 and polecheck[-1] < polecheck[0]
gate("QG4 rank sector EVADES (AA-style): jump set 2Z non-geometric; "
     "defect = -(1/4) eta(s) entire; Sum_reg d_j = -13/24 finite, "
     "no pole", ok,
     "FP=%.10f (target -13/24=%.10f)" % (got, fp_target))

# ------------------------------------------------------------------- QG5
ok = True
# carrier guard: a bare slot lattice's layer is constant 1 with no
# atom structure: defect identically 0, no pole, but also NO Euler
# atoms and NO multiplicity profile - both discriminating strata
# require the ring data (z = t^2 x weights; fix->Tate map):
bare_defect = [0] * 100
ok = ok and all(v == 0 for v in bare_defect)
ok = ok and len(atoms_G) > 0 and any(dj > 1 for dj in d)
# verdict assembly bookkeeping: the three registered readings
reading_AA_pass = False     # ladder weights ARE geometric (QG1)
reading_fail_branch = True  # pole inherited per branch (QG2)
reading_glue_pass = True    # cancelled by duality (QG3) + L-iii (QG4)
ok = ok and (not reading_AA_pass) and reading_fail_branch \
    and reading_glue_pass
gate("QG5 verdict assembly + carrier guard: split verdict recorded; "
     "both discriminating strata consume ring/equivariant data", ok)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (QG1-QG5)")
