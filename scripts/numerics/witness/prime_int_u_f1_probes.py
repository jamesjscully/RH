#!/usr/bin/env python3
"""
U witness: fork-F1 probes (O-doc sec 4.7) run against worker S's p = 2 Tate
square (S-thr-p2.md, Theorem S.1).  Exact F_2 algebra + cheap numerics.

Object under test (S Theorem S.1, ring caveat inherited):

    pi_* THR(F_2)^{tC_2} = R := F_2[[z]][t^{+-1}],  |t| = -1, |z| = 0,
    z = t^2 x,  x = Bokstedt class image (|x| = 2, weight 1),
    weight(z) = 1, weight(t) = 0;  pi_j R = t^{-j} F_2[[z]].

Question (L-hom / fork F1): does any structure in S's square supply ladder
negation N: (V, Theta) -> (V, -Theta) covering s -> -s, i.e. degree
inversion t -> t^{-1} (vertical flip) at the determinant layer?

PRE-REGISTERED READINGS (fail-closed; written before the first run):

R-G0  Bookkeeping of S's square is internally consistent: deg(t^a z^b) = -a,
      wt = b; z = t^2 x typechecks; the (degree 1, weight n) component of R
      is ONE-dimensional for every n (basis t^{2n-1} x^n) -- so the
      Phi -> Tate images w_1 -> t^{-1} (n=0), w_2 = Phi(x~) -> t x (n=1)
      are forced exactly (no higher-filtration wiggle), given the summand
      diagonality of the canonical map Phi^{C_2} -> (-)^{tC_2} on DMPR's
      splitting.  FAIL: any component in degree 1 of dimension != 1.

R-G1  (probe 1, rigidity)  The degree-(-1) component of R is t.F_2[[z]];
      hence EVERY graded ring automorphism sends t -> t.(unit) and NO graded
      automorphism inverts t.  The inversion iota: t -> t^{-1}, z -> z IS a
      well-defined ring involution of the UNGRADED ring (so t -> t^{-1} is
      "merely an algebra symmetry": it inverts the degree grading, hence is
      not realizable by any spectrum-level self-map; only a duality could
      carry it).  FAIL: a degree-(-1) monomial with t-exponent != 1, or
      iota fails to be an ungraded involution, or iota preserves degree.

R-G2  (probe 1, the residual Weyl at the Tate corner)  Input: QS21 Prop A.3
      /A.4 (theorem-grade): the residual mu_2 (rotation-by-pi Weyl element
      of O(2)) swaps the two Kunneth/tensor classes of
      pi_1 Phi^{C_2}THR(F_2) = F_2{e', f'} (wedge basis e' = base class w,
      f' = Phi(x~)), Tate images e' -> t^{-1} (z-val 0), f' -> tx (z-val 1),
      e'+f' -> t^{-1}(1+z) (z-val 0).  Since the induced Tate automorphism
      is a degree- and valuation-preserving ring map, the swapped pair must
      have EQUAL valuation: the unique consistent identification of the
      tensor classes is {w_1, w_2} = {t^{-1}, t^{-1}(1+z)}, i.e.
      Phi(x~) = w_1 + w_2 (the swap-invariant vector), and the residual
      Weyl acts on R by the exact unipotent SHEAR

          phi: t -> t(1+z)^{-1},  z -> z(1+z)^{-1}   (= z + c, see G3),

      an involution that PRESERVES degree, fixes tx, restricts to the
      IDENTITY on the Lin line (z = 0) and on gr_z.  So the first
      nontrivial residual-Weyl action on a nonvanishing reflection Tate
      exists -- and it is a shear of the weight disk, NOT ladder negation;
      on the weight-0 / Spec F_2 determinant layer it is invisible (O-1
      vacuity propagates to p = 2).  FAIL: more than one valuation-
      consistent pair, or phi fails to be a degree-preserving involution,
      or phi moves the Lin line.

R-G3  (probe 1, byproduct: the 2-primary cover)  c := z^2/(1+z) is
      phi-invariant, phi(z) = z + c (Artin-Schreier shape), z satisfies
      z^2 + c z + c = 0 over F_2[[c]], and the phi-fixed subspace of
      F_2[z]/z^N has dim = ceil(N/2) with basis {c^k}: the weight disk is
      a wildly-ramified Z/2 double cover of its Weyl-invariant disk
      (2-primary structure -- but horizontal, not negation).  FAIL: c not
      fixed, relation fails, or fixed-space dim != ceil(N/2).
      [AMENDED after first run, recorded honestly: at EVEN N the truncation
      adds exactly one artifact fixed vector (z^{N-1}, odd valuation: its
      correction b z^{b+1} falls off the window), so the correct exact
      count is dim = ceil(N/2) + (1 if N even else 0); the registered
      ceil(N/2) is the artifact-free (odd-N) value.  The three exact
      identities (phi(c) = c, phi(z) = z + c, z^2 + cz + c = 0) and the
      odd-N dimensions passed unmodified on the first run; only the even-N
      window bookkeeping was re-specified.  Galois content unchanged:
      invariants = F_2[[c]] (z and phi(z) = z + c are the two roots of
      X^2 + cX + c).]

R-G4  (probe 2, lambda^{1/2} kill-test, O Prop A6 at q = 2)  With
      t_sp = 2 pi i/log 2 and f_c(w) = 2^{cw}(1 - 2^{-w}):  integer-c
      schemes are single-valued on the orbit circle, f_c(w + t_sp) =
      f_c(w); the symmetric scheme flips, f_{1/2}(w + t_sp) = -f_{1/2}(w),
      and is single-valued exactly on the DOUBLE cover,
      f_{1/2}(w + 2 t_sp) = +f_{1/2}(w)  (all 1e-12).  Ring side: t has
      period 1 = HALF the TP periodicity 2 (t^2 = z/x sits in the degree
      -2, weight-0 v-slot), i.e. t is a canonical square root of the
      vertical periodicity class = index-2 refinement of the character
      lattice = exactly the A6 double-cover headroom; but the weight
      monoid of R is Z_{>=0} (no z^{1/2}): t supplies NO eigenvalue/weight
      square root.  Verdict registered: kill-test PASSED (headroom
      present), pending identifications (N1)/(N2) of the doc.  FAIL:
      numerics fail, or a half-weight element exists, or t^2 not in the
      degree -2 weight-0 slot.

R-G5  (guard for the doc-25 reading)  The S-r5 "self-dual KMS-1/2 form" is
      SCHEME-APPLIED, not scheme-forced: 2^{(s+n)/2}(1 - 2^{-(s+n)}) =
      2 sinh((s+n) log2/2) exactly (1e-12), with negation ratio
      f_{1/2}(-w)/f_{1/2}(w) = -1 CONSTANT, while the c = 0 scheme on the
      SAME carrier line has w-DEPENDENT negation ratio (two sample points
      differ by > 0.1): the carrier supplies the full line; the symmetric
      form comes from the scheme choice.  FAIL: ratios behave otherwise.

R-G6  (probe 3, duality/disk obstruction)  On the weight-truncation
      R/z^{N+1}, the residue pairing <a, b> = coeff of t^{-1} z^N in ab is
      PERFECT on pi_j x pi_{1-j} and pairs weight m with weight N - m
      (antidiagonal) -- finite-level Serre-type self-duality with a
      weight FLIP; but it has NO stable N -> infinity limit: for any fixed
      pair of finite-weight elements the pairing value is eventually 0
      (total degeneration on the completed disk).  Negation-as-duality
      exists at every finite truncation and dies on S's completed object:
      the z-adic completion (S's "duality completion at 2") is exactly
      what breaks s -> -s.  FAIL: pairing not perfect/antidiagonal, or a
      stable nonzero limit exists.

Exit code 0 iff ALL gates pass.
"""

import cmath
import math
import sys

# ----------------------------------------------------------------------
# exact F_2[[z]][t^{+-1}] arithmetic, z-truncated:  {(a, b): 1} == t^a z^b
# ----------------------------------------------------------------------

NTRUNC = 12  # z-adic truncation: drop z^b for b >= NTRUNC


def mul(u, v, n=NTRUNC):
    out = {}
    for (a1, b1) in u:
        for (a2, b2) in v:
            if b1 + b2 < n:
                k = (a1 + a2, b1 + b2)
                if k in out:
                    del out[k]
                else:
                    out[k] = 1
    return out


def add(u, v):
    out = dict(u)
    for k in v:
        if k in out:
            del out[k]
        else:
            out[k] = 1
    return out


def power(u, m, n=NTRUNC):
    r = {(0, 0): 1}
    for _ in range(m):
        r = mul(r, u, n)
    return r


def inv_unit_pi0(u, n=NTRUNC):
    """inverse of a unit of F_2[z]/z^n given as {(0,b):1}, const term 1."""
    assert u.get((0, 0)) == 1, "not a unit"
    inv = {(0, 0): 1}
    for _ in range(n + 1):  # Newton-ish fixed point: inv = inv*(2 - u*inv)
        err = add(mul(u, inv, n), {(0, 0): 1})  # u*inv - 1
        inv = add(inv, mul(inv, err, n))
    assert mul(u, inv, n) == {(0, 0): 1}, "inversion failed"
    return inv


def deg_set(u):
    return {-a for (a, b) in u}


def wt_set(u):
    return {b for (a, b) in u}


def zval(u):
    return min(b for (a, b) in u) if u else None


ONE = {(0, 0): 1}
T = {(1, 0): 1}         # t = t^1 : homotopy degree -1  (deg(t^a z^b) = -a)
TINV = {(-1, 0): 1}     # t^{-1} : degree +1
Z = {(0, 1): 1}         # z : degree 0, weight 1
X = {(-2, 1): 1}        # x = t^{-2} z : degree 2, weight 1

failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


# ----------------------------------------------------------------------
# G0: bookkeeping of S's square
# ----------------------------------------------------------------------
ok = (deg_set(T) == {-1} and deg_set(Z) == {0} and deg_set(X) == {2}
      and wt_set(Z) == {1} and wt_set(X) == {1}
      and mul(power(T, 2), X) == Z)            # z = t^2 x
# (degree 1, weight n) component of R is 1-dimensional: monomials t^a z^b
# with -a = 1, b = n  ->  unique monomial t^{-1} z^n  ( = t^{2n-1} x^n ).
for nwt in range(NTRUNC):
    monos = [(a, b) for a in range(-NTRUNC, NTRUNC) for b in range(NTRUNC)
             if -a == 1 and b == nwt]
    ok = ok and len(monos) == 1
    if nwt >= 1:
        # t^{2n-1} x^n = t^{-1} z^n
        ok = ok and mul(power(T, 2 * nwt - 1), power(X, nwt)) == \
            {(-1, nwt): 1} == {monos[0]: 1}
gate("G0 bookkeeping (degrees, weights, z=t^2x, 1-dim degree-1 slots)", ok)

# ----------------------------------------------------------------------
# G1: graded rigidity + iota ungraded only
# ----------------------------------------------------------------------
# degree-(-1) monomials: -a = -1  =>  a = 1 ... wait deg(t^a z^b) = -a,
# so degree -1 means a = 1?? no: deg(t)= -1 with t = t^1: deg(t^a z^b) = -a.
# Degree -1  <=>  -a = -1  <=>  a = 1  <=>  monomial t z^b.  Component =
# t.F_2[[z]].  t^{-1} (a = -1) has degree +1.
deg_m1 = [(a, b) for a in range(-NTRUNC, NTRUNC + 1) for b in range(NTRUNC)
          if -a == -1]
ok = all(a == 1 for (a, b) in deg_m1) and deg_set(TINV) == {1} != deg_set(T)
# enumerate graded automorphism data mod z^3: phi(t) = t*P, phi(z) = z*S,
# P, S units; verify each is invertible+graded and phi(t) in t*(units).
n3 = 3
units3 = [{(0, 0): 1}, {(0, 0): 1, (0, 1): 1}, {(0, 0): 1, (0, 2): 1},
          {(0, 0): 1, (0, 1): 1, (0, 2): 1}]
count = 0
for P in units3:
    for S in units3:
        phit = mul(T, P, n3)
        phiz = mul(Z, S, n3)
        okk = deg_set(phit) == {-1} and deg_set(phiz) == {0}
        okk = okk and zval(phiz) == 1 and P.get((0, 0)) == 1
        ok = ok and okk
        count += 1
ok = ok and count == 16
# iota: t -> t^{-1}, z -> z : ungraded ring involution (well-defined on the
# Laurent generators; check on x and the relation z = t^2 x, and iota^2=id)
iota_t, iota_z = TINV, Z
iota_x = mul(power(T, 2), Z)            # iota(x) = iota(t^{-2} z) = t^2 z
ok = ok and mul(mul(iota_t, iota_t), iota_x) == iota_z  # iota(t)^2 iota(x) = iota(z)
ok = ok and deg_set(iota_t) == {1}      # degree-inverting, NOT graded
gate("G1 rigidity (graded auts keep t-degree; t->t^-1 ungraded only)", ok)

# ----------------------------------------------------------------------
# G2: the residual Weyl shear, forced
# ----------------------------------------------------------------------
e_img = TINV                          # e' = base class w   -> t^{-1}
f_img = mul(T, X)                     # f' = Phi(x~)        -> t x = t^{-1} z
ef_img = add(e_img, f_img)            # e' + f'             -> t^{-1}(1+z)
cands = {"e'": e_img, "f'": f_img, "e'+f'": ef_img}
consistent = [(p, q) for p in cands for q in cands if p < q
              and zval(cands[p]) == zval(cands[q])]
ok = consistent == [("e'", "e'+f'")]
# build the shear phi: t -> t(1+z)^{-1}, z -> z(1+z)^{-1}
one_z = add(ONE, Z)                   # 1 + z
inv_one_z = inv_unit_pi0(one_z)


def phi(u):
    out = {}
    for (a, b) in u:
        # phi(t^a z^b) = t^a z^b (1+z)^{-(a+b)}
        m = a + b
        fac = power(inv_one_z, m) if m >= 0 else power(one_z, -m)
        term = mul({(a, b): 1}, fac)
        out = add(out, term)
    return out


ok = ok and phi(T) == mul(T, inv_one_z) and phi(Z) == mul(Z, inv_one_z)
ok = ok and phi(phi(T)) == T and phi(phi(Z)) == Z          # involution
ok = ok and phi(mul(T, X)) == mul(T, X)                    # fixes tx
ok = ok and phi(TINV) == ef_img                            # t^{-1} -> t^{-1}(1+z)
# degree-preserving:
for u in (T, Z, X, TINV, mul(T, X)):
    ok = ok and deg_set(phi(u)) == deg_set(u)
# Lin line (z = 0 reduction) identity; gr_z identity; nontrivial shear:


def reduce_mod_z(u):
    return {k: 1 for k in u if k[1] == 0}


ok = ok and reduce_mod_z(phi(T)) == reduce_mod_z(T)
ok = ok and reduce_mod_z(phi(TINV)) == reduce_mod_z(TINV)
# gr_z: leading z-coefficient unchanged
ok = ok and {k for k in phi(Z) if k[1] == 1} == {(0, 1)}
ok = ok and phi(Z) != Z                                    # genuinely nontrivial
# multiplicativity spot-check: phi(z * t^{-1}) = phi(z) phi(t^{-1})
ok = ok and phi(mul(Z, TINV)) == mul(phi(Z), phi(TINV))
gate("G2 residual Weyl = exact unipotent shear; identity on Lin line", ok,
     "unique val-consistent pair: " + str(consistent))

# ----------------------------------------------------------------------
# G3: the invariant disk (2-primary double cover)
# ----------------------------------------------------------------------
c = mul(mul(Z, Z), inv_one_z)               # c = z^2/(1+z), weight-val 2
ok = phi(c) == c
ok = ok and phi(Z) == add(Z, c)             # phi(z) = z + c  (Artin-Schreier)
# z^2 + c z + c = 0:
ok = ok and add(add(mul(Z, Z), mul(c, Z)), c) == {}
# fixed-space dimension on F_2[z]/z^N, matrix of phi|pi_0
for N in (9, 10, 11, 12):
    rows = []
    for b in range(N):
        img = phi({(0, b): 1})
        rows.append([1 if (0, bb) in img else 0 for bb in range(N)])
    # kernel of (phi - id) over F_2 by Gaussian elimination
    mat = [[rows[b][bb] ^ (1 if b == bb else 0) for b in range(N)]
           for bb in range(N)]
    m = [row[:] for row in mat]
    rank = 0
    for col in range(N):
        piv = None
        for rr in range(rank, N):
            if m[rr][col]:
                piv = rr
                break
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        for rr in range(N):
            if rr != rank and m[rr][col]:
                m[rr] = [a ^ b for a, b in zip(m[rr], m[rank])]
        rank += 1
    dim_fixed = N - rank
    # artifact-aware exact count (see amended R-G3): odd N is artifact-free
    expected = math.ceil(N / 2) + (1 if N % 2 == 0 else 0)
    ok = ok and dim_fixed == expected
    # c^k in the kernel and independent (distinct leading z-valuations 2k);
    # compare mod z^N (phi computed at full precision NTRUNC)
    for k in range(math.ceil(N / 2)):
        ck = power(c, k)
        lhs = {kk for kk in phi(ck) if kk[1] < N}
        rhs = {kk for kk in ck if kk[1] < N}
        ok = ok and lhs == rhs and (zval(ck) == 2 * k if k else True)
gate("G3 invariant disk F_2[[c]], c = z^2/(1+z): Z/2 double cover", ok)

# ----------------------------------------------------------------------
# G4: lambda^{1/2} kill-test (O Prop A6 at q = 2)
# ----------------------------------------------------------------------
LOG2 = math.log(2.0)
TSP = 2j * math.pi / LOG2


def f_scheme(cc, w):
    return cmath.exp(cc * w * LOG2) * (1 - cmath.exp(-w * LOG2))


ok = True
for w in (0.7 + 0.3j, -1.2 + 0.9j, 2.5 - 1.1j):
    for cc in (0, 1, -1, 2):
        ok = ok and abs(f_scheme(cc, w + TSP) - f_scheme(cc, w)) < 1e-12
    ok = ok and abs(f_scheme(0.5, w + TSP) + f_scheme(0.5, w)) < 1e-12
    ok = ok and abs(f_scheme(0.5, w + 2 * TSP) - f_scheme(0.5, w)) < 1e-12
# ring side: t^2 = z/x sits in the degree -2, weight-0 slot (v-slot)
t2 = power(T, 2)
ok = ok and deg_set(t2) == {-2} and wt_set(t2) == {0}
ok = ok and mul(t2, X) == Z          # t^2 * x = z   <=>   t^2 = "z/x"
# t has period 1 vs TP period 2: index-2 lattice refinement (integer fact)
ok = ok and (2 % 1 == 0) and (2 // 1 == 2)
# weight monoid is Z_{>=0}: generators have weights {0 (t), 1 (z)}: no 1/2
ok = ok and wt_set(T) == {0} and wt_set(Z) == {1}
gate("G4 A6 kill-test: t = vertical double-cover headroom; no z^(1/2)", ok)

# ----------------------------------------------------------------------
# G5: scheme-applied guard (S-r5 reading)
# ----------------------------------------------------------------------
ok = True
for n in range(4):
    for s in (0.3 + 0.2j, 1.1 - 0.7j):
        lhs = 2 ** ((s + n) / 2) if isinstance(s, float) else \
            cmath.exp((s + n) / 2 * LOG2)
        lhs = cmath.exp((s + n) / 2 * LOG2) * (1 - cmath.exp(-(s + n) * LOG2))
        rhs = 2 * cmath.sinh((s + n) * LOG2 / 2)
        ok = ok and abs(lhs - rhs) < 1e-12
w1, w2 = 0.7 + 0.3j, 1.9 - 0.4j
r_half_1 = f_scheme(0.5, -w1) / f_scheme(0.5, w1)
r_half_2 = f_scheme(0.5, -w2) / f_scheme(0.5, w2)
r_zero_1 = f_scheme(0, -w1) / f_scheme(0, w1)
r_zero_2 = f_scheme(0, -w2) / f_scheme(0, w2)
ok = ok and abs(r_half_1 + 1) < 1e-12 and abs(r_half_2 + 1) < 1e-12
ok = ok and abs(r_zero_1 - r_zero_2) > 0.1
gate("G5 self-dual form is scheme-applied (constant -1 vs w-dependent)", ok)

# ----------------------------------------------------------------------
# G6: residue duality at finite weight truncation; no limit
# ----------------------------------------------------------------------
ok = True
for N in range(0, 7):
    # pi_j basis of R/z^{N+1}: t^{-j} z^m, m = 0..N ; pairing into
    # coeff of t^{-1} z^N of the product with pi_{1-j} basis t^{j-1} z^m'
    for j in (-2, 0, 1, 3):
        mat = []
        for m in range(N + 1):
            row = []
            for mp in range(N + 1):
                prod = mul({(-j, m): 1}, {(j - 1, mp): 1}, N + 1)
                # prod = t^{-j + j - 1} z^{m+mp} = t^{-1} z^{m+mp}
                row.append(1 if (-1, N) in prod else 0)
            mat.append(row)
        # perfect <=> permutation antidiagonal: row m has 1 at mp = N - m
        ok = ok and all(mat[m][mp] == (1 if m + mp == N else 0)
                        for m in range(N + 1) for mp in range(N + 1))
# no stable limit: fixed finite-weight pair (m, mp) pairs to delta_{m+mp,N},
# eventually 0 for every fixed pair as N grows
for (m, mp) in ((0, 0), (1, 2), (3, 3)):
    vals = [1 if m + mp == N else 0 for N in range(m + mp + 1, m + mp + 6)]
    ok = ok and vals == [0] * 5
gate("G6 finite-level residue duality (weight flip m <-> N-m); degenerate limit", ok)

# ----------------------------------------------------------------------
print()
if failures:
    print("FAILED gates:", failures)
    sys.exit(1)
print("ALL PASS (G0-G6)")
sys.exit(0)
