# 138 - DD.4 weights>=1: the Weyl-shear extension is obstructed (R1 no-go)

Status: no-go + named computed obstruction, 2026-06-17. First cycle of the
doc-137 arc (R1 = DD.4 on weights >= 1, exit A), building on Thm EE.1 (the
Lin-block clause, doc 31). It decides the singleton-vs-torsor question that
GROUND GC posed for the R1 entry: does the EE.1 weight-0 duality datum extend
to a genuinely O(2)-equivariant (Weyl-shear-fixed) datum on weights >= 1?
It does NOT. The obstruction is a nonzero, gauge-free, exact-F_2-computed
cohomology class. STAGE / Layer I (BB.1) -- RH-neutral either way.

Witnesses (lead-reran this cycle, all exit 0):
`prime_int_pb_shear_h1_obstruction` (PBG1-PBG6 ALL PASS) -- builds and
  enumerates H^1(<phi>; U_1) = Z/2 and pins the DDG7b defect (1+z)^{-1} as its
  nonzero class via the torsor-invariant res_1 homomorphism;
`prime_int_ee_dd4_lin` (EEG1-EEG8 ALL PASS) -- the banked Lin-block singleton
  and the torsor-support fact (EEG7) the obstruction lives in;
`prime_int_dd_bc_dual` (DDG1-DDG7 ALL PASS) -- the tower, its continuous BC
  dual, and the DDG7 Weyl shear / defect this cycle reads;
`dd4_weight1_datum` (PROBE PA, PG1-PG6 ALL PASS) -- independent corroboration
  by a coboundary/Herbrand solver: dim_{F_2} H^1 = 1 (= Z/2) and the class is a
  nontrivial torsor (not a coboundary), agreeing with PB.
(prime_int_ee_dd4_lin, prime_int_dd_bc_dual are the pre-existing EE/DD
substrate witnesses, reran exit 0; the new files banked this cycle are
prime_int_pb_shear_h1_obstruction and dd4_weight1_datum.)

## 1. Purpose

Doc 137 sec 8 set R1 = DD.4 on weights >= 1: extend the EE.1 Lin-block
self-duality datum (weight 0, a theorem-grade SINGLETON, torsor-free) past the
gluing locus. GROUND GA/GC reduced the OPEN content to four clauses --
branch-exchange (A), genuine O(2)/phi-equivariance (B, the open half of
C5'''), N1-b' (the geometric y-vs-t comparison, riding on HNS Thm A.2), and
the weight-torsor pinning (D). GROUND GC identified the DECIDABLE carrier: the
space of weight>=1 data extending EE.1 is a torsor under the 1-unit group
U_1 = 1 + z*F_2[[z]], and a genuinely-equivariant (Weyl-fixed) representative
exists iff the DDG7b defect c = (1+z)^{-1} is a coboundary for the shear
action -- i.e. iff [c] = 0 in H^1(<phi>; U_1). This cycle computes that group.

## 2. Covered Class

```text
- the BRANCH-EXCHANGE / genuine-O(2) / phi-equivariance clause (GROUND GA
  clauses A,B,D) of DD.4 on weights >= 1, at the cocycle level: does the
  EE.1 Lin datum admit a Weyl-shear-fixed extension to weights >= 1;
- equivalently: the weight-torsor pinning question (GROUND GC) -- is the
  weight>=1 duality datum a singleton (extends) or a nontrivial U_1-torsor
  with no phi-fixed representative (no-go).
```

It does NOT cover (sec 6): clause N1-b' -- the geometric line y vs the
Weyl-Tate line t under HNS Thm A.2's fiber formula. That comparison rides on
Harpaz-Nikolaus-Shah Thm A.2 (attributed-forthcoming, NOT archived), is the
single load-bearing missing external input, and is INDEPENDENT of this no-go.

## 3. Lemma

```text
Lemma 138.1 (the Weyl-shear extension of the DD.4 Lin datum is obstructed by
a nonzero, gauge-free H^1 class). Let U_1 = 1 + z*F_2[[z]] be the 1-unit
group of the disk ring (S.1, z = t^2 x, weight 1), and let phi be the
Artin-Schreier Weyl shear z -> z(1+z)^{-1} (the residual W_{O(2)}(C_2),
DDG7a), an involution => the coefficients are C_2. Let c = (1+z)^{-1} be the
exact DDG7b non-equivariance of the (xz)-tower transition. Then:

  (i)  [the class is defined] N(c) = c * phi(c) = 1, so c is a genuine
       1-cocycle and [c] in H^1(<phi>; U_1) is defined. (PBG2.)

  (ii) [the group] H^1(<phi>; U_1) = Z/2 EXACTLY, stably: by finite-subgroup
       closure from the generators 1 + z^k at truncations L = 6,8,10,12,
       |B^1| = 2^{L/2}, |Z^1| = 2^{L/2+1}, |H^1| = 2, L-independent. (PBG4.)

  (iii)[the class does NOT vanish] phi fixes the z^1-coefficient of every
       1-unit, so the leading-coefficient map res_1: U_1 -> F_2 is a
       homomorphism that KILLS every coboundary b/phi(b) and descends to H^1;
       res_1(c) = c_1 = 1. Hence c is NOT a coboundary; the coboundary
       equation fails at degree 1 (b_1 = b_1 + 1, i.e. 0 = 1). [c] is the
       nonzero class. (PBG3, PBG5, PBG6.)

  (iv) [gauge-free] res_1 is EXACTLY EEG7's torsor-INVARIANT leading
       coefficient ((1+z)^k preserves valuation and leading term), so the
       obstruction is well-posed, not a normalization/gauge artifact. (PBG6.)

Hence the EE.1 weight-0 Lin datum does NOT extend to a phi-fixed (genuinely
O(2)/Weyl-equivariant) weight>=1 duality datum: equivariance exists only on
the GLUED object (the DDG7c defect), never as a Weyl-isometry of the
weight>=1 datum. This is Z's kappa mechanism surviving cohomologically at
weights >= 1, now a COMPUTED falsifiable class rather than a flagged gap.
```

Verdict label:

```text
DD4_WEIGHTS_GE1__WEYL_SHEAR_EXTENSION_OBSTRUCTED__H1_DEFECT_CLASS_NONZERO.
```

## 4. Proof

(i) `prime_int_pb_shear_h1_obstruction` PBG1-PBG2 (exit 0): phi is verified an
involution on U_1 (phi^2 = id), fixing the augmentation and preserving the
z-valuation of monomials (DDG7a); c = (1+z)^{-1} satisfies c*phi(c) = 1, so it
is a genuine C_2 1-cocycle. The shear formula phi(z^m) = z^m(1+z)^{-m} and
phi^2 = id are inherited from DDG7 (`prime_int_dd_bc_dual`, rerun ALL PASS).

(ii) PBG4 (exit 0): by closing U_1 under multiplication from the generators
1 + z^k at L = 6,8,10,12 (exact F_2 arithmetic), the coboundary subgroup B^1
and cocycle subgroup Z^1 are enumerated directly; |H^1| = |Z^1|/|B^1| = 2 at
every truncation, L-independent => H^1(<phi>; U_1) = Z/2. (PA's gated
Herbrand-quotient result, dim_{F_2} H^1 = 1, is the SAME statement -- Z/2 has
dimension 1 over F_2 -- so PA and PB AGREE on the group; only a non-gated
additive diagnostic in PA was unstable and is disregarded. PB's direct
B^1/Z^1 enumeration is the banked computation.)

(iii) PBG3, PBG5, PBG6 (exit 0): the coboundary equation b = c*phi(b) reads,
in the z^1-component, b_1 = b_1 + c_1 with c_1 = 1, i.e. 0 = 1 -- no solution;
the defect c is NOT in B^1 at any tested L; res_1 (z^1-coeff) is a
homomorphism U_1 -> F_2 vanishing on all of B^1 (descends to H^1) with
res_1(c) = 1. So [c] is the nonzero class of Z/2.

(iv) PBG6: res_1 is EEG7's torsor-invariant leading coefficient (rerun
`prime_int_ee_dd4_lin` EEG7 ALL PASS): (1+z)^k preserves valuation and leading
term, so res_1 is well-defined on torsor orbits and the obstruction is
gauge-free. []

## 5. What survived adversarial verification (the honest downgrade)

```text
- PROBE PB (this no-go) survived all four adversarial lenses. The H^1 = Z/2
  verdict and the nonzero defect class are backed by GENUINE enumeration of
  B^1/Z^1 (not a relabel), and the obstruction lives in the choice-free res_1
  invariant. This is the result.

- PROBE PA reached the SAME no-go by a coboundary/norm solver, and INDEPENDENTLY
  CORROBORATES it: PA's gated Herbrand-quotient result dim_{F_2} H^1 = 1 is the
  same group as PB's |H^1| = 2 (Z/2 is 1-dimensional over F_2). A separate
  NON-gated additive diagnostic in PA gave an unstable |H^1| = 4,8,4 at small N
  (PA's own caveat) and is disregarded. PB's direct B^1/Z^1 enumeration is the
  banked computation; PA's class-nonvanishing and Herbrand dim both agree.

- PROBE PC's result_type=BUILT_SUBOBJECT (a "genuine weight-1 duality datum")
  is REFUTED, 3 of 4 lenses: (a) PCG1/PCG2 (the branch-exchange D and the
  Gram a+b=1) are tautologies on an INTEGER INDEX SET -- they PASS identically
  for any reflection a -> c-a with c odd, on any index set, and use no
  z-arithmetic; a trivial degree-graded control reproduces them, so they are
  carrier-BLIND bookkeeping, not a duality on a constructed object (doc 64,
  doc 129); (b) PCG4 "carrier death on DH" is HARDCODED literals
  (weight1_dim_full = 1, weight1_dim_DH = 0; the gate reduces to (0>0) is
  False over author-asserted constants), not a computed S.1-ring
  degeneration; (c) PC's own caveats concede it tests only the STRUCTURAL FORM
  in S.1's truncated ring, NOT a functorial assembly of I^cont into one
  involution of one object (DD.4 clause A, the open content), "NOT verified by
  any runnable witness". Per doc 129, a plausible construction with no runnable
  witness of the object is not a result. PC's PCG3 (the (1+z)^k torsor orbit,
  orbit_size 8, leading-coeff-invariant) and PCG5 (Epstein representability of
  x^2+5y^2) ARE genuine computations, consistent with the PB no-go (the torsor
  is nontrivial). NO weight>=1 SUB-OBJECT was built. The PC witness was NOT
  banked -- it was DELETED, because its "ALL PASS" gating included the
  fabricated PCG4 (hardcoded dim literals), and its genuine content is
  subsumed by PB's H^1 = Z/2 and the doc-64 Epstein guard. Recording the
  refutation here is the full-value negative (doc 129); banking the fabricated
  artifact is not.
```

## 6. Surviving Escape (the single named missing input)

```text
N1-b' / HNS Thm A.2. The no-go is for the WEYL-SHEAR-FIXED (genuinely
O(2)-equivariant, U.2(b) proper) extension route -- which GROUND GA/GC
identify as the actual open required clause. It does NOT execute clause
N1-b': the comparison of the geometric line y (QS21 A.5-A.7, can(y) = y,
|y| = |t| = -1; w = w_1 w_2 |-> x under S.1's Phi -> Tate) with the Weyl-Tate
Lin line t under HNS Thm A.2's fiber formula
  TCR(X)^{phi mu_2} = fib(X^{phiC2 h mu_2} -> X^{phiC2 t mu_2}).
Slots check (EEG8) but A.2 (Harpaz-Nikolaus-Shah, attributed-forthcoming, NOT
in the archive) made precise on THR(F_2) is the single most load-bearing
missing external input. If a genuinely different carrier surfaces from A.2,
the singleton question re-opens on that carrier; the Weyl-shear route stays
closed regardless. A bare (non-equivariant) weight>=1 datum still EXISTS
(B^1 non-empty); what is provably impossible is pinning a Weyl-invariant one
without an EXTERNAL phi-invariant normalization (the conjectured dlog(1+z)
pinning, unproven, NOT supplied by the homotopy).
```

## 7. Kill Conditions

```text
KILL-DD4.1 shear-coboundary claim
  a proposed weight>=1 extension claims a genuinely-O(2)/Weyl-fixed datum
  without exhibiting the DDG7b defect (1+z)^{-1} as a coboundary for the
  shear; it cannot, since res_1((1+z)^{-1}) = 1 and res_1 kills every
  coboundary. Witness: prime_int_pb_shear_h1_obstruction (Z/2, [c] != 0).

KILL-DD4.2 index-set bookkeeping mistaken for duality
  the datum is checked only as a reflection a <-> 1-a on a degree index set
  (D o D = id, Gram a+b=1) with no z-arithmetic; a trivial degree-graded
  control reproduces it, so it is gauge/coherence decoration, not duality on
  a constructed object (doc 64, doc 129). Witness: the PC refutation.

KILL-DD4.3 hardcoded carrier-death
  a carrier guard asserts dimension literals (e.g. weight1_dim_DH = 0) instead
  of computing the S.1-ring degeneration of the actual constructed datum under
  x -> 0; the gate is a tautology, not a measurement. Witness: PC PCG4 refuted.
```

## 8. Board

```text
doc-137 R1 (DD.4 weights >= 1, exit A), cycle 1 = doc 138:
  DD4_WEIGHTS_GE1__WEYL_SHEAR_EXTENSION_OBSTRUCTED__H1_DEFECT_CLASS_NONZERO.
  H^1(<phi_Weyl-shear>; 1 + z F_2[[z]]) = Z/2 (PBG4, enumerated L=6..12); the
  DDG7b defect (1+z)^{-1} is its nonzero class (res_1 = 1, gauge-free, PBG6).
  The EE.1 Lin singleton does NOT extend to a genuinely-O(2)-equivariant
  weight>=1 duality datum. STAGE / Layer I (BB.1) -- RH-neutral.

R1 status on the ladder: the genuine-O(2)/Weyl-shear extension clause is a
  NO-GO (named, computed). R1 is NOT closed: the N1-b' clause (HNS Thm A.2)
  is untouched and could expose a different carrier. R1 is SHARPENED, not
  finished; the no-go reshapes the target.

What got built: nothing at weight>=1 (PC's BUILT claim refuted). The positive
  content is the negative -- Z's kappa-shear obstruction is now a COMPUTED
  falsifiable Z/2 class, not a flagged gap.

Next valid work (sec 6 / next_rung): either (a) obtain/make precise HNS Thm
  A.2 on THR(F_2) and execute the geometric y-vs-t comparison (N1-b'), the one
  remaining open clause; OR (b) supply an EXTERNAL phi-invariant normalization
  (the dlog(1+z) pinning) that selects a canonical torsor element -- with a
  runnable witness. Do NOT claim a Weyl-fixed extension (KILL-DD4.1), nor an
  index-set involution as duality (KILL-DD4.2), nor a hardcoded carrier-death
  (KILL-DD4.3). R2 (the archimedean unit) is NOT unblocked: it was gated on R1
  per doc 137 sec 4, and R1's self-duality of Layer I is not finished.
```
