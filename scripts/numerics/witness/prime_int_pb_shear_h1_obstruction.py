"""PB-witness: the NAMED no-go for extending the DD.4 self-duality datum
past the Lin block (weight 0) to weights >= 1.

PROBE PB (arc charter 137, R1 entry cycle).  GROUND GC posed the
decidable carrier: the space of weight >= 1 duality data extending the
EE.1 Lin datum is a TORSOR under the 1-unit group U_1 = 1 + z F_2[[z]]
(the disk-ring units fixing the augmentation; DDG7b/c, EE.1(iii)).  For
the datum to be genuinely O(2)-equivariant (U.2(b) proper) it must admit
a phi-FIXED representative, where phi is the Artin-Schreier Weyl shear
phi(z) = z/(1+z) (W_{O(2)}(C_2) = <lambda_pi>; witness U G2 / DDG7).
The obstruction to a phi-fixed representative is the class of the
DDG7b defect cocycle c = (1+z)^{-1} in

        H^1(<phi>; U_1),   U_1 = 1 + z F_2[[z]] (multiplicative),

with <phi> = C_2 (phi is an involution, DDG7a).  This witness COMPUTES
that group and decides whether c vanishes.

Setting (Theorem S.1 + DD conventions, all exact F_2 / integer; no
numerics).  z is the weight-1 disk coordinate (z = t^2 x, |z| = 0);
F_2[[z]] is the local Euler-factor direction; U_1 is its 1-unit group.
phi acts by phi(z^m) = z^m (1+z)^{-m} (DDG7, prime_int_dd_bc_dual).
For an involution acting on an abelian group M (written
multiplicatively): Z^1 = { c in M : c * phi(c) = 1 } (the generator
cocycle condition); B^1 = { b * phi(b)^{-1} : b in M } (coboundaries,
a subgroup since M abelian => b |-> b/phi(b) is a homomorphism);
H^1 = Z^1 / B^1.  Truncate U_1 at z^{L+1}: U_1/(1+z^{L+1}) is a finite
2-group of order 2^L, on which Z^1, B^1 are honest finite subgroups
enumerable by closure from the generators 1 + z^k (k = 1..L).

PRE-REGISTERED READINGS (fail-closed; docstring written before first
run; design-stage hand derivation disclosed: the degree-1 obstruction
b_1 = b_1 + c_1 was found by hand and REGISTERED as the expected
outcome, with the explicit clause that c_1 = 0 (vanishing) would
support PA's extension and FALSIFY this no-go):

R-PBG1 phi IS AN INVOLUTION ON U_1 (DDG7a re-checked on U_1, not just
       on the tower).  phi(phi(u)) = u for every 1-unit u in the
       truncation, and phi fixes the augmentation (phi(1) = 1) and
       preserves valuation.  FAIL: phi^2 != id, or valuation moved.

R-PBG2 THE DEFECT IS A COCYCLE.  c = (1+z)^{-1} satisfies the C_2
       cocycle condition c * phi(c) = 1 (so [c] in H^1 is defined).
       This is the DDG7b 1-unit (1+z)^{-1} read as the equivariance
       defect of the (x z) transition.  FAIL: c * phi(c) != 1.

R-PBG3 THE COBOUNDARY EQUATION FAILS AT DEGREE 1 (the named
       obstruction, leading coefficient).  Seeking b in U_1 with
       b = c * phi(b) (equivalently c = b/phi(b)): because phi fixes
       the z^1-coefficient (phi(b)_1 = b_1) and c_0 = 1, c_1 = 1, the
       degree-1 component of b = c*phi(b) reads b_1 = b_1 + 1, i.e.
       0 = 1.  No b solves it.  FAIL of the reading: some b_1 in {0,1}
       makes the degree-1 components agree (then c is a coboundary at
       leading order and the no-go is wrong).

R-PBG4 H^1(<phi>; U_1) = Z/2, STABLY (the group is computed, not
       asserted).  At every truncation L in {6,8,10,12}, |U_1| = 2^L,
       |B^1| = 2^{?}, |Z^1| = 2^{?}, and the QUOTIENT |H^1| = 2
       exactly (one nontrivial class), independent of L.  FAIL: |H^1|
       != 2 at any tested L, or L-dependent.

R-PBG5 THE DEFECT IS THE NONTRIVIAL CLASS.  c = (1+z)^{-1} is NOT in
       B^1 at every tested L (so [c] != 0 in H^1).  FAIL: c in B^1 at
       any L (then the defect is a coboundary and the datum extends -
       supports PA, refutes this no-go).

R-PBG6 THE LEADING-COEFFICIENT INVARIANT DETECTS IT (torsor-free, ties
       to EEG7).  res_1: U_1 -> F_2, u |-> (z^1-coefficient of u), is a
       group homomorphism that VANISHES on every coboundary b/phi(b)
       (so it descends to H^1) and is NONZERO on c (res_1(c) = 1).
       This is exactly EEG7's torsor-invariant leading coefficient: the
       obstruction lives in the torsor-INVARIANT slot, hence is
       well-posed and not a gauge/normalization artifact.  FAIL: res_1
       nonzero on some coboundary, or res_1(c) = 0.

VERDICT IF ALL PASS: the weight-torsor is NONTRIVIAL.  The EE.1 Lin
datum does NOT extend to a phi-fixed (genuinely O(2)-equivariant)
duality datum on weights >= 1.  Named obstruction: the nonzero class
[(1+z)^{-1}] in H^1(<phi_Weyl-shear>; 1 + z F_2[[z]]) = Z/2, detected
by the torsor-invariant leading coefficient res_1.  This is a NO-GO for
the branch-exchange/O(2) clause (U.2(b)) of DD.4 as a phi-EQUIVARIANT
involution.  (STAGE caveat, BB.1: this is LAYER I; the verdict is about
the FE/self-duality stage, RH-neutral.)

Run: python3 -m scripts.numerics.witness.prime_int_pb_shear_h1_obstruction
Exit 0 iff ALL PASS.
"""

import sys
from math import comb, log2

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def make(L):
    """Truncated F_2[[z]] arithmetic mod z^{L+1}; polys are dicts {k: 1}."""
    def mul(a, b):
        out = {}
        for i in a:
            for j in b:
                if i + j <= L:
                    out[i + j] = out.get(i + j, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def add(a, b):
        out = dict(a)
        for k in b:
            out[k] = out.get(k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def inv(a):
        """Invert a 1-unit (a_0 = 1) by the char-2 Neumann series."""
        assert a.get(0, 0) == 1
        rem = add(a, {0: 1})            # a - 1 (the positive-degree part)
        term, res = {0: 1}, {0: 1}
        for _ in range(1, L + 1):
            term = mul(term, rem)
            if not term:
                break
            res = add(res, term)
        return res

    def phi(f):
        """Weyl shear phi(z^m) = z^m (1+z)^{-m}, extended linearly (DDG7)."""
        out = {}
        for m in f:
            if m == 0:
                out[0] = out.get(0, 0) ^ 1
                continue
            for k in range(0, L - m + 1):
                if comb(m + k - 1, k) % 2:        # [(1+z)^{-m}]_k mod 2
                    out[m + k] = out.get(m + k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    return mul, add, inv, phi


def to_vec(f, L):
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    return {0: 1, **{k + 1: 1 for k, x in enumerate(v) if x}}


# ------------------------------------------------------------------- PBG1
L = 16
mul, add, inv, phi = make(L)
ok = True
for k in range(1, L + 1):
    u = {0: 1, k: 1}
    ok = ok and phi(phi(u)) == u                       # involution on U_1
    ok = ok and min(phi(z := {k: 1})) == k             # valuation of z^k preserved
ok = ok and phi({0: 1}) == {0: 1}                      # fixes augmentation
gate("PBG1 phi is an involution on U_1 (phi^2 = id), fixes the "
     "augmentation, preserves z-valuation of monomials (DDG7a)", ok)

# ------------------------------------------------------------------- PBG2
ok = True
c = inv({0: 1, 1: 1})                                  # c = (1+z)^{-1}
ok = ok and mul(c, phi(c)) == {0: 1}                   # cocycle: c*phi(c)=1
gate("PBG2 the DDG7b defect c = (1+z)^{-1} is a C_2 cocycle "
     "(c * phi(c) = 1): [c] in H^1 is defined", ok)

# ------------------------------------------------------------------- PBG3
ok = True
# Seek b with b = c*phi(b); test degree-1 component over both b_1 in {0,1}.
disagree_both = True
for b1 in (0, 1):
    cand = {0: 1}
    if b1:
        cand[1] = 1
    rhs = mul(c, phi(cand))
    if cand.get(1, 0) == rhs.get(1, 0):
        disagree_both = False                          # a b_1 would solve deg 1
ok = ok and disagree_both
ok = ok and c.get(1, 0) == 1                           # the obstruction = c_1
gate("PBG3 coboundary equation b = c*phi(b) fails at degree 1 "
     "(b_1 = b_1 + c_1, c_1 = 1 => 0 = 1): named leading obstruction", ok,
     "c_1=%d" % c.get(1, 0))

# ------------------------------------------------------------------- PBG4
ok = True
orders = {}
for Lc in (6, 8, 10, 12):
    m_, a_, i_, p_ = make(Lc)

    def closure(genpolys, Lc=Lc, m_=m_):
        seen = {(0,) * Lc}
        q = [(0,) * Lc]
        while q:
            curp = from_vec(q.pop())
            for gp in genpolys:
                nv = to_vec(m_(curp, gp), Lc)
                if nv not in seen:
                    seen.add(nv)
                    q.append(nv)
        return seen

    # B^1 = image of the homomorphism b |-> b/phi(b); generated by 1+z^k.
    Bgens = [m_({0: 1, k: 1}, i_(p_({0: 1, k: 1}))) for k in range(1, Lc + 1)]
    B = closure(Bgens)
    # |Z^1| = |U_1| / |im N|, N(x) = x*phi(x) (norm); im N generated by N(1+z^k).
    Ngens = [m_({0: 1, k: 1}, p_({0: 1, k: 1})) for k in range(1, Lc + 1)]
    imN = len(closure(Ngens))
    Zord = 2 ** Lc // imN
    H1 = Zord // len(B)
    orders[Lc] = (len(B), Zord, H1)
    ok = ok and H1 == 2
gate("PBG4 H^1(<phi>; U_1) = Z/2 stably (|H^1| = 2 at L = 6,8,10,12, "
     "L-independent)", ok,
     "  ".join("L%d:|B|=2^%d|Z|=2^%d|H1|=%d"
               % (Lc, int(log2(b)), int(log2(z)), h)
               for Lc, (b, z, h) in orders.items()))

# ------------------------------------------------------------------- PBG5
ok = True
for Lc in (6, 8, 10, 12):
    m_, a_, i_, p_ = make(Lc)
    seen = {(0,) * Lc}
    q = [(0,) * Lc]
    Bgens = [m_({0: 1, k: 1}, i_(p_({0: 1, k: 1}))) for k in range(1, Lc + 1)]
    while q:
        curp = from_vec(q.pop())
        for gp in Bgens:
            nv = to_vec(m_(curp, gp), Lc)
            if nv not in seen:
                seen.add(nv)
                q.append(nv)
    cL = i_({0: 1, 1: 1})
    ok = ok and to_vec(cL, Lc) not in seen            # c NOT a coboundary
gate("PBG5 the defect c = (1+z)^{-1} is NOT in B^1 at any tested L: "
     "[c] is the NONTRIVIAL class of H^1 (no-go, not coboundary)", ok)

# ------------------------------------------------------------------- PBG6
ok = True
mul, add, inv, phi = make(L)
# res_1 vanishes on every coboundary generator (=> on all of B^1, a hom);
for k in range(1, L + 1):
    cob = mul({0: 1, k: 1}, inv(phi({0: 1, k: 1})))
    ok = ok and cob.get(1, 0) == 0
# res_1 is a homomorphism U_1 -> F_2: (uv)_1 = u_1 + v_1 (additive); spot-check:
for k in range(1, 6):
    for l in range(1, 6):
        prod = mul({0: 1, k: 1}, {0: 1, l: 1})
        ok = ok and prod.get(1, 0) == (({0: 1, k: 1}).get(1, 0) ^
                                       ({0: 1, l: 1}).get(1, 0))
ok = ok and inv({0: 1, 1: 1}).get(1, 0) == 1          # res_1(c) = 1
gate("PBG6 leading-coefficient invariant res_1 (z^1-coeff) is a "
     "homomorphism vanishing on B^1 (descends to H^1) and res_1(c) = 1: "
     "obstruction lives in EEG7's torsor-INVARIANT slot (well-posed, "
     "not gauge)", ok)

# --------------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (PBG1-PBG6)")
print("VERDICT: NO-GO. H^1(<phi_Weyl-shear>; 1+z F_2[[z]]) = Z/2; the "
      "DDG7b defect (1+z)^{-1} is its nonzero class (res_1 = 1). The EE.1 "
      "Lin datum does NOT extend to a phi-fixed (genuinely O(2)-equivariant) "
      "weight>=1 duality datum. STAGE (BB.1): Layer I, RH-neutral.")
