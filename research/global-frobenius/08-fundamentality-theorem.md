# 08 — The fundamentality theorem (additive form), drafted

Status: THEOREM DRAFT, 2026-06-30. Phase-2 deliverable (doc 05). Assembles the
bounded-negative result from the cycle trail (docs 02, 04, 06, 07) + side B
(Efimov). Drafted with its residual obligations named — honest, not a clean QED.

## Statement

```text
THEOREM (Integrality–Summability Dichotomy, additive form). Let E be an
integer-valued ADDITIVE/LOCALIZING invariant (doc 07) on the truncations of the
compactified arithmetic line bar(Spec Z), and let <Delta,Delta>_E denote the
self-product diagonal self-intersection it computes (the regularized total of E
down the tower). Then EXACTLY ONE of:

  (A)  E is EFFECTIVE / scale-aware -- E tracks the entropy log_b(size) to O(1) --
       and then <Delta,Delta>_E DIVERGES: the defect series has a simple pole at
       s=0 (residue -1/(2 log b), shape-independent), and the 2-variable
       self-product makes the genuine (H^1 (x) H^1) content WORSE (double pole);

  (B)  E is SCALE-BLIND -- invariant under the scaling that separates divisors --
       and then E carries no intersection content (no divisor discrimination).

In neither case does E yield a FINITE INTEGER self-intersection. Equivalently:
over bar(Spec Z), integrality and archimedean regularization cannot coexist in one
additive invariant -- finiteness forces the transcendental -zeta'(0) = (1/2)log 2pi,
integrality forces divergence.

COROLLARY. No additive/localizing route realizes the Weil-positivity-via-
correspondence object (the integer intersection form / positive Rosati on the
self-product). A construction must be canonical NON-additive = MULTIPLICATIVE
(a Frobenius / norm / delta-structure), at the archimedean place (doc 07; F1).
```

## Proof (assembled)

```text
Side A:
  A1 (effective => log growth): an effective integer invariant is the rank of a
     finite presentation / minimal generating set, hence = log_b(size) + O(1).
     [CC's dim = ceil(log_3(2n+1)) is the exact instance, Prop 3.3.]
  A2 (integer + log-tracking => geometric jumps, density 1/log b): doc 03,
     Census-certified universal (gf_dichotomy_jump_density).
  A3 (=> simple pole at s=0, residue -1/(2 log b), SHAPE-INDEPENDENT): LEMMA W1,
     doc 06 (gf_w1_residue_offset_independence). The 1-variable regularized
     total diverges.
  A4 (the self-product does not rescue it): doc 04
     (gf_selfproduct_pole_escape) -- all natural 2-variable models are polar on
     the diagonal (M1 product double pole, M2 additive simple pole, M3 normal-
     bundle double pole); the only finite value is the transcendental
     -zeta'(0)/log b, certified non-integer. No 2-variable regularization yields
     a finite integer.
Side B:
  scale-blind / summable additive invariants are the CONTINUOUS localizing
  invariants, which are scale-INVARIANT by theorem (Efimov, arXiv:2405.12169);
  a scale-invariant E cannot distinguish divisors of different degree, so it
  carries no intersection content.
Additivity is load-bearing (doc 07): it forces <Delta,Delta>_E to BE the
regularized additive tower sum, which side A diverges and side B trivializes. QED
(modulo the obligations below).
```

## Residual obligations (named, honest)

```text
O1 (MEDIUM) self-intersection = additive tower sum, GENERAL form. The
   identification <Delta,Delta>_E = regularized tower sum rests on the doc-18
   derived-square model + the additive decomposition of the diagonal. doc 04
   tested the natural 2-variable models; the fully general statement (for every
   additive E) is modeled, not proved. THE LOAD-BEARING SOFT SPOT. Grade: Reading.
O2 (LOW) side B precise form. "Continuous localizing invariants are scale-
   invariant" is cited from Efimov arXiv:2405.12169 via the prior arc's
   characterization. Nail the exact statement + applicability to this category.
   Grade: cited.
O3 (LOW, routine) the general Euler-Maclaurin write-up of W1 (doc 06): the -1/2
   routing factor is structural and certified for the ceiling; the general write-
   up is routine bookkeeping. Grade: Theorem-modulo-routine.
```

## What it claims, and what it does NOT (scope)

```text
CLAIMS: within the class C = integer-valued additive/localizing invariants
(which contains EVERY construction tested across the program -- CC dim, dim_S,
THH, K-theory ranks, Euler characteristics, Bost-Connes, Borisov, Efimov), no
finite integer self-product intersection form exists; the obstruction is the
integrality/archimedean-regularization tension, with the finite value forced to
-zeta'(0) (and that value is provably transcendental, doc 09 / Lindemann).

DOES NOT CLAIM: anything about RH. existence(object) => RH, but ¬existence does
NOT => ¬RH. The theorem bounds the additive correspondence ROUTE, is RH-NEUTRAL,
and explicitly POINTS AT its own exception (the multiplicative door, F1) as the
missing construction target. It is the CHARTER's bounded-negative branch -- a
characterization of why decades of additive F_1 attempts have not produced the
object, NOT a resolution of RH.
```

## Grade

```text
THEOREM (program rigor): proof assembled from Certified witnesses (W1, no-leak,
jump-density) + one cited literature theorem (Efimov, side B) + one named
modeling assumption (O1). The hard analytic content (side A) is Certified; the
residual obligations are O1 (Reading, the real soft spot), O2 (cited), O3
(routine). Not yet a fully formalized unconditional theorem; honestly a
bounded-negative result at the program's witness rigor with O1 as the gate to
full rigor.
```

## Where it leads

```text
The theorem closes the additive route and hands the construction its exact
target: a canonical MULTIPLICATIVE structure at infinity (F1). doc 09 walks
through that door and finds it occupied by the archimedean scaling flow, whose
self-intersection -zeta'(0) is PROVABLY transcendental (Lindemann) -- so the
door, as currently occupied, reproduces the dichotomy. The next theorem target
(doc 09): EXTEND the dichotomy from additive to multiplicative by showing any
canonical archimedean multiplicative structure has continuous spectrum. The one
remaining internal obligation is O1.
```
