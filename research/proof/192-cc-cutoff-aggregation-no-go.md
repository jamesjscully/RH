# 192 - Cutoff aggregation does not construct the square carrier

Status: no-go + CC non-zeta aggregation repair deletion, 2026-06-20.
Fifty-fifth cycle of the doc-137 construction arc. Docs 189-191 killed the
CC-ceiling graded-tolerance tower, its finite-part repair, and hand-retuned
non-geometric exactness sets. This document tests the second evasion named
in the Q record: abandon zeta-regularization for the aggregate.

Witness, lead-reran this cycle:
`prime_int_n1b_cc_cutoff_aggregation_no_go` (CNA1-CNA10 ALL PASS) -- the
doc-189 non-zeta evasion branch, exact cutoff sums for the CC-ceiling tower,
raw cutoff divergence, mean cutoff growth, base-dependent residual constants
after leading-scale subtraction, missing square-native cutoff/cofinality
rule, missing non-EM square functor/carrier-native aggregation, missing
square H^2/intersection/correspondence/Rosati data, missing Laurent
boundary/torsor/DD.4 data, and residual R1 carrier-guard checks.

Adjacent witnesses:
`prime_int_n1b_cc_graded_tolerance_no_go` (CGT1-CGT10 ALL PASS),
`prime_int_n1b_cc_finite_part_renormalization_no_go` (CFR1-CFR10 ALL PASS),
and `prime_int_n1b_cc_non_geometric_exactness_no_go` (CNE1-CNE10 ALL PASS).

## 1. Purpose

The Q record gives two evasion branches for the CC-ceiling pole:

```text
(a) place quantizer exactness on a non-geometric set;
(b) abandon zeta-regularization for the aggregate.
```

Doc 191 killed branch (a) in its hand-retuned form. This document tests
branch (b) in its simplest form:

```text
Keep dim_b(k)=ceil(log_b k).
Do not zeta-regularize the infinite tower.
Aggregate by finite cutoffs.
Promote the cutoff aggregate, or its elementary normalization, to the square
carrier invariant.
```

This does not construct End(S^2/Z). Raw cutoff sums diverge. The mean cutoff
also grows with the cutoff scale. Subtracting the leading scale leaves
base-dependent constants. None of these operations supplies a square-native
cofinality rule, square cohomology, or a correspondence algebra.

This document is local. It does not reject a future non-zeta aggregation
constructed internally by a square carrier. It rejects ordinary finite
cutoff aggregation of the CC-ceiling tower as construction-grade
End(S^2/Z).

## 2. Lemma

```text
Lemma 192.1 (Finite cutoff aggregation is not the square carrier).

Let

  dim_b(k) = ceil(log_b k).

For N=b^m, the finite cutoff sum is

  S_b(b^m) = Sum_{1 <= k <= b^m} ceil(log_b k)
           = [1 - (m+1)b^m + m b^(m+1)] / (b-1).

For the two CC bases at m=6:

  S_2(64)  = 321,
  S_3(729) = 4010.

These cutoff sums diverge as m increases. Their means also grow:

  S_2(2^4)/2^4 = 3.062500,
  S_2(2^6)/2^6 = 5.015625,
  S_2(2^8)/2^8 = 7.003906;

  S_3(3^4)/3^4 = 3.506173,
  S_3(3^6)/3^6 = 5.500686,
  S_3(3^8)/3^8 = 7.500076.

If the leading cutoff scale b^m m is subtracted and the result is divided
by b^m, the residual tends to

  -1/(b-1),

so it is base-dependent: approximately -1 for b=2 and -1/2 for b=3.

Thus cutoff aggregation supplies no finite square invariant without an
extra normalization/cofinality rule. No such rule is constructed by the
CC-ceiling tower. It also supplies no non-EM square functor, no square H^2,
no intersection form, no correspondence algebra, no Frobenius graph, no
positive Rosati, no Laurent boundary map, and no torsor splitter.

Therefore finite cutoff aggregation of the CC-ceiling tower is not
construction-grade End(S^2/Z). A surviving non-zeta route must construct
the aggregation carrier-natively and independently construct the square
cohomology, correspondences, Laurent boundary, and Rosati data.
```

Verdict label:

```text
N1B_CC_CUTOFF_AGGREGATION__CUTOFF_SELECTOR_NOT_SQUARE_CORRESPONDENCE__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_cutoff_aggregation_no_go` verifies the finite statement.

CNA1 records the tested branch: zeta-regularization is abandoned and finite
cutoff aggregation is selected, with no new square carrier supplied.

CNA2 verifies the exact power-window formula:

```text
S_2(64)  = 321;
S_3(729) = 4010.
```

CNA3 records raw divergence along presentation powers:

```text
base 2, m=4,6,8: 49, 321, 1793;
base 3, m=4,6,8: 284, 4010, 49208.
```

CNA4 records that the mean cutoff aggregate still grows with the cutoff
scale.

CNA5 records that subtracting the leading scale and dividing by the cutoff
size leaves base-dependent residual constants:

```text
b=2, m=10: -0.999023437500;
b=3, m=10: -0.499991532456.
```

CNA6 records the selector failure: no square-native cutoff or cofinality rule
is supplied.

CNA7 records that no non-EM square functor is constructed and no diagonal
factorization barrier is broken.

CNA8-CNA9 record the carrier failure: no square H^2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent axis,
boundary map, torsor splitter, or DD.4 weight>=1 datum is constructed.

CNA10 records that the base R1 obstructions and carrier guard remain.

## 4. Impact on R1

```text
R1 after docs 138-192:
  NEWLY CLOSED THIS CYCLE:
    - finite cutoff / ordinary non-zeta aggregation of the CC-ceiling tower
      as End(S^2/Z), carrier-native aggregation, square H^2/intersection/
      correspondence data, Frobenius graph, Laurent boundary data, torsor
      splitter, or positive Rosati (doc 192).

  STILL ADMISSIBLE:
    - a future non-zeta aggregation constructed internally by a non-EM square
      functor, provided it also constructs square H^2, intersection,
      correspondences, Laurent boundary data, and Rosati.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. Cutoff aggregation of the CC-ceiling tower is a measured
failure, not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CNA.1 raw cutoff aggregate as square carrier
  A proposal replaces zeta aggregation by finite cutoff sums of
  ceil(log_b k). Kill it: the raw cutoff sums diverge.

KILL-CNA.2 mean cutoff aggregate as invariant
  A proposal divides by the cutoff size and promotes the mean to the square
  invariant. Kill it: the mean still grows with the cutoff scale.

KILL-CNA.3 leading-subtracted cutoff constant
  A proposal subtracts the leading cutoff scale and keeps the residual
  constant. Kill it unless the normalization is carrier-native; the residual
  is base-dependent.

KILL-CNA.4 cutoff/cofinality without square rule
  A proposal chooses a cutoff family or cofinality rule externally. Kill it
  unless the square carrier constructs the rule.

KILL-CNA.5 cutoff aggregate without square H2/intersection
  A proposal gives a cutoff aggregate but no H^2, intersection form, or
  correspondence algebra. This is not the square carrier.

KILL-CNA.6 cutoff aggregate without Rosati/Laurent boundary
  A proposal gives a cutoff aggregate but no Frobenius graph, positive
  Rosati, Laurent boundary map, torsor splitter, or DD.4 weight>=1 datum.
  This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 55 = doc 192:
  N1B_CC_CUTOFF_AGGREGATION__CUTOFF_SELECTOR_NOT_SQUARE_CORRESPONDENCE__NO_GO.

What got built: no End object. The value is a deletion: cutoff aggregation
of the CC-ceiling tower is divergent or base-normalized bookkeeping and
constructs no square correspondence algebra.

What remains: construct a genuinely new carrier-native aggregation or return
to the in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
