# 55 - One-place and inserted-unit no-go

Status: broad no-go proof draft, 2026-06-11. This turns T48.3 into a
reusable gate. It rules out two common promotions:

```text
1. treating signs of a chosen continuum unit as object data;
2. treating one-place charge bookkeeping as global threading.
```

It does not rule out an LS3-derived unit or a unit-covariant theorem.

## 1. Statement

Let a proposed candidate use a continuum unit `U` to evaluate local
slot/payment constants for prime-power classes. Assume:

```text
H1 inserted or movable unit
  U is chosen externally, chosen placewise, selected from an
  admissible family, or determined only up to an unfixed normalization
  torsor.

H2 slot-functional obstruction
  The claimed obstruction is a sign, phase, Mellin value, Fourier
  value, repair margin, or local payment constant computed as a
  functional of U.

H3 no unit-covariant carrier theorem
  The claim does not prove an invariant statement over all admissible
  units or derive U as the candidate's unique internal fixed unit.
```

Then the obstruction is slot data, not an object condition. It cannot
establish doc 45 clauses C1-C3 or C5 for the missing structure.

Moreover, if a proposed construction evaluates each `Lambda(p)` or
`Lambda(p^k)` class independently and has no structural cross-place
assembly map, product-formula constraint, or KMS-beta=1/2 global
coupling, then it cannot establish doc 45 C3 global threading. It can
at most supply one-place calibration or local bookkeeping.

## 2. Proof: Inserted Or Movable Unit

The proof is a covariance argument, with doc 43 as the decisive model.

Doc 43 compares the banked Gaussian unit with an admissible self-dual
Hermite unit:

```text
f_C(x) = e^{-pi x^2}(1 + eps H4(sqrt(2pi)x))/(1+12eps),
eps = 1/100,
fhat_C = f_C.
```

The banked Gaussian decision cell was:

```text
m+_gauss((11;2), 4.96) = -2.214249e-3.
```

Under the admissible self-dual Hermite unit, the same banked deep cell
flips:

```text
m+((11;2), 4.96) = +2.0913e-4.
```

The candidate class did not change. Only the admissible unit did. Thus
the sign of that deep cell is not an invariant object condition. It is
a coordinate in the unit slot.

Abstractly, any obstruction satisfying H1-H3 has the same defect. If
the obstruction changes under admissible unit replacement while the
carrier data is unchanged, the obstruction belongs to the chosen unit's
slot coordinates. A theorem depending on that sign proves a property
of the chosen presentation, not a property of the missing object.

Consequently:

```text
- Gaussian deep-cell negativity is demoted.
- Hermite positivity is also not promoted.
- A strict repair atom or chosen Gaussian cannot certify the object.
- The candidate's own unit must be derived before C- or D-claims are
  tested in its covariant coordinates.
```

## 3. Proof: One-Place Bookkeeping

Doc 45 C3 requires global threading:

```text
the object must transfer or thread local deficits globally, rather
than merely record a local obstruction at each place.
```

A one-place construction has natural domain:

```text
{one prime p, one local p^Z comb, one local trace/count slot}.
```

Such a domain contains no structural map that can move surplus from
one place to another. It also contains no product-formula constraint
and no KMS-beta=1/2 assembly. Therefore it cannot prove that local
`k=1` deficits are globally payable. The most it can show is the local
ledger at a chosen place.

This is not a numerical limitation. It is a domain limitation. Global
threading is a statement about an object whose natural domain contains
multiple places and the relation among them. If that relation is not in
the construction, the theorem cannot conclude C3.

## 4. What Survives

The no-go does not erase all C-clause evidence. It sharpens it.

The surviving object-level pattern is:

```text
C1 local k=1 deficit
  The Lambda(p)-class deficit remains the local obstruction.

C2 candidate-native unit
  The unit must be derived internally, not inserted.

C3 global threading
  Per-place infeasibility must become global feasibility only through
  product-formula/KMS-beta=1/2 assembly.

C5 depth wall
  The exponential Frobenius-depth demand versus linear window supply is
  unit-free in covariant units, with law constant 1.
```

Doc 43 supplies the key separation: the named deep breaking phase is
unit-parametric, while the depth wall survives the self-dual unit swap.
Doc 66 isolates this as the unit-covariance and threading lemma.

## 5. Candidate Gate

Before promoting any unit or one-place result, ask:

```text
G55.1 Unit source
  Is U derived as the candidate's internal Fourier fixed unit, with
  normalization pinned by internal R/T rigidity?
  If no, reject C-promotion.

G55.2 Unit covariance
  Is the claimed sign or obstruction invariant under admissible
  self-dual unit replacement, or stated covariantly after deriving U?
  If no, demote to slot data.

G55.3 Threading domain
  Does the construction contain at least two places plus a structural
  product-formula or KMS-beta=1/2 assembly map?
  If no, reject global-threading promotion.

G55.4 Depth wall
  Is the claimed wall expressed in unit-free covariant coordinates?
  If no, rerun after deriving the candidate's own unit.
```

Passing G55 does not prove C. It only prevents a candidate from being
rejected for the inserted-unit or one-place failure mode.

## 6. Escape Profile

A candidate escapes this no-go only by providing one of the following.

```text
E1 LS3-derived unit
  The unit is the fixed point of an internal Fourier self-duality, with
  normalization torsor pinned to {+-1} by internal T=R/Z rigidity.

E2 unit-covariant theorem
  The obstruction is not a sign of a chosen unit, but a theorem stated
  invariantly across the admissible unit family or after U is derived.

E3 global assembly
  The construction contains a cross-place object whose maps implement
  product-formula/KMS-beta=1/2 threading, so local infeasibility and
  global feasibility are both native statements.
```

If none of E1-E3 is present, the result remains calibration or slot
bookkeeping.

## 7. Program Consequence

T48.3 is now a reusable gate:

```text
Do not re-promote Gaussian deep-cell failures, strict repair atoms,
one-place Poisson normalizations, or local payment constants as object
conditions.
```

The live theorem is narrower and harder: derive the candidate's own
unit, state the k=1 charge and depth wall covariantly, and prove that
global assembly threads the local deficit rather than padding it.
