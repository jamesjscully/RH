# 191 - Non-geometric exactness retuning does not construct the square carrier

Status: no-go + CC exactness-set repair deletion, 2026-06-20. Fifty-fourth
cycle of the doc-137 construction arc. Docs 189-190 killed the CC-ceiling
graded-tolerance tower and its finite-part repair. This document tests the
next evasion named in the Q record: avoid the pole by replacing the
b-geometric exactness atoms with a non-geometric exactness set.

Witness, lead-reran this cycle:
`prime_int_n1b_cc_non_geometric_exactness_no_go` (CNE1-CNE10 ALL PASS) --
the doc-189 evasion branch, CC-ceiling b-geometric exactness atoms,
representative retuned non-geometric sets, finite-window selector counts,
base-pair selector overproduction, abandonment of the CC ceiling mechanism,
missing non-EM square functor/carrier-native aggregation, missing square
H^2/intersection/correspondence/Rosati data, missing Laurent boundary/torsor
DD.4 data, and residual R1 carrier-guard checks.

Adjacent witnesses:
`prime_int_n1b_cc_graded_tolerance_no_go` (CGT1-CGT10 ALL PASS) records the
underlying geometric-exactness pole mechanism, and
`prime_int_n1b_cc_finite_part_renormalization_no_go` (CFR1-CFR10 ALL PASS)
records the finite-part selector failure.

## 1. Purpose

The Q record states the exact evasion condition for the CC-ceiling pole:

```text
An evading proposal must either
  (a) place quantizer exactness on a non-geometric set, or
  (b) abandon zeta-regularization for the aggregate.
```

Doc 190 killed retaining the finite part of the original geometric tower.
This document tests branch (a) in its simplest form:

```text
Keep zeta aggregation.
Change the exactness atoms from {b^j} to a non-geometric sequence.
Use the retuned exactness sequence as the square carrier invariant.
```

This can avoid the named pole mechanism only by replacing the CC ceiling
atoms. Without a carrier-native rule that constructs the new exactness set,
the repair spends an external sequence selector.

This document is local. It does not reject a future square functor that
constructs a non-geometric exactness set internally. It rejects hand-retuning
the exactness set as construction-grade End(S^2/Z).

## 2. Lemma

```text
Lemma 191.1 (Hand-retuned non-geometric exactness is a selector).

For the CC-ceiling dimension

  dim_b(k) = ceil(log_b k),

the exactness atoms in the window 1 <= k <= b^6 are forced:

  b=2: {1,2,4,8,16,32,64},
  b=3: {1,3,9,27,81,243,729}.

Replacing these atoms by a non-geometric set is not a consequence of
dim_b(k). It is new sequence data.

Even before passing to an infinite tower, finite windows already overproduce
selectors. Among subsets of [1,64] with the same cardinality as the b=2 atom
set, there are

  binom(64,7) - 1 = 621216191

alternatives to the CC atom set. Among subsets of [1,729] with the same
cardinality as the b=3 atom set, there are

  binom(729,7) - 1 = 21091830512086619

alternatives. Choosing compatible alternatives in both CC bases multiplies
the selector burden unless the square carrier supplies a base-covariance rule.

No such rule is supplied by the retuning. It also supplies no non-EM square
functor, no square H^2, no intersection form, no correspondence algebra, no
Frobenius graph, no positive Rosati, no Laurent boundary map, and no torsor
splitter.

Thus non-geometric exactness retuning is not construction-grade End(S^2/Z).
A surviving non-geometric exactness route must construct the exactness set
carrier-natively and independently construct the square cohomology,
correspondences, Laurent boundary, and Rosati data.
```

Verdict label:

```text
N1B_CC_NON_GEOMETRIC_EXACTNESS__EXTERNAL_SEQUENCE_SELECTOR_NOT_SQUARE_AGGREGATION__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_non_geometric_exactness_no_go` verifies the finite
statement.

CNE1 records the tested branch: this is the non-geometric exactness evasion
while keeping zeta aggregation, with no new square aggregation supplied.

CNE2 records the forced CC-ceiling exactness atoms:

```text
b=2: 1,2,4,8,16,32,64;
b=3: 1,3,9,27,81,243,729.
```

CNE3 records representative retuned non-geometric exactness sets:

```text
b=2 candidate: 1,2,3,5,7,11,13;
b=3 candidate: 1,3,5,7,11,13,17.
```

They are not the CC atom sets. They include non-powers and omit powers.

CNE4 records the finite-window selector overproduction:

```text
binom(64,7) - 1  = 621216191;
binom(729,7) - 1 = 21091830512086619.
```

CNE5 records that choosing a pair of retuned exactness sets across the two
CC bases multiplies choices unless a square-native base-covariance rule is
constructed.

CNE6 records the mechanism-level cost: de-geometrizing exactness abandons
the CC ceiling/log-periodic quantizer mechanism. Avoiding the pole this way
does not construct the missing carrier; it changes the sequence data.

CNE7 records that no non-EM square functor is constructed and no diagonal
factorization barrier is broken.

CNE8-CNE9 record the carrier failure: no square H^2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent axis,
boundary map, torsor splitter, or DD.4 weight>=1 datum is constructed.

CNE10 records that the base R1 obstructions and carrier guard remain.

## 4. Impact on R1

```text
R1 after docs 138-191:
  NEWLY CLOSED THIS CYCLE:
    - hand-retuned non-geometric exactness sets as End(S^2/Z),
      carrier-native aggregation, square H^2/intersection/correspondence
      data, Frobenius graph, Laurent boundary data, torsor splitter, or
      positive Rosati (doc 191).

  STILL ADMISSIBLE:
    - a future non-EM square functor or carrier-native aggregation that
      constructs a non-geometric exactness set internally and then constructs
      square H^2, intersection, correspondences, Laurent boundary data, and
      Rosati.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. Retuning exactness atoms by hand is a measured failure,
not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CNE.1 hand-retuned exactness set as carrier
  A proposal replaces {b^j} by a non-geometric exactness set and promotes
  that set to End(S^2/Z). Kill it unless the set is carrier-constructed.

KILL-CNE.2 exactness sequence without base covariance
  A proposal chooses different exactness sets in the S and S[+-1] bases.
  Kill it unless a square-native base-covariance rule is supplied.

KILL-CNE.3 non-geometric exactness as preserved CC ceiling
  A proposal claims to preserve dim_b(k)=ceil(log_b k) while changing the
  exactness atoms. Kill it: the CC ceiling exact atoms are b-powers.

KILL-CNE.4 regularity without aggregation
  A proposal avoids the geometric pole but supplies no carrier-native
  aggregate. Regularity is not End(S^2/Z).

KILL-CNE.5 exactness set without square H2/intersection
  A proposal gives an exactness sequence but no H^2, intersection form, or
  correspondence algebra. This is not the square carrier.

KILL-CNE.6 exactness set without Rosati/Laurent boundary
  A proposal gives an exactness sequence but no Frobenius graph, positive
  Rosati, Laurent boundary map, torsor splitter, or DD.4 weight>=1 datum.
  This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 54 = doc 191:
  N1B_CC_NON_GEOMETRIC_EXACTNESS__EXTERNAL_SEQUENCE_SELECTOR_NOT_SQUARE_AGGREGATION__NO_GO.

What got built: no End object. The value is a deletion: non-geometric
exactness retuning avoids the named pole only by spending external sequence
data and still constructs no square correspondence algebra.

What remains: construct a genuinely new carrier-native aggregation or return
to the in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
