# 190 - Finite-part renormalization does not construct the square carrier

Status: no-go + CC finite-part repair deletion, 2026-06-20. Fifty-third
cycle of the doc-137 construction arc. Doc 189 killed the CC-ceiling
graded-tolerance derived-square repair because the quantized integer tower
has a simple pole at s=0. This document tests the next repair: subtract the
pole and keep the finite part as the proposed square invariant.

Witness, lead-reran this cycle:
`prime_int_n1b_cc_finite_part_renormalization_no_go` (CFR1-CFR10 ALL PASS)
-- pole residues, rational finite parts, smooth-derived comparison, defect
finite parts, missing carrier-native finite-part/base selector, the failed
S[+-1] quarter echo, missing non-geometric exactness/new aggregation data,
missing square H^2/intersection/correspondence/Rosati data, missing Laurent
boundary/torsor/DD.4 data, and residual R1 carrier-guard checks.

Adjacent witness:
`prime_int_n1b_cc_graded_tolerance_no_go` (CGT1-CGT10 ALL PASS) records the
underlying geometric-exactness pole mechanism.

## 1. Purpose

Doc 189 leaves a natural repair:

```text
The CC-ceiling integer tower has a pole.
Subtract the pole and keep the finite part.
Use that pole-subtracted value as the square carrier invariant.
```

This is a narrower claim than doc 189. It does not re-test the existence of
the pole. It tests whether the pole-subtracted finite part itself supplies
construction-grade End(S^2/Z).

The answer is no. Pole subtraction chooses a regularization prescription and
a base. The resulting finite parts are

```text
b=2: 3/4
b=3: 1/4
```

These are rational scheme calibrations. They are not the smooth derived
regularized totals, and they construct no square cohomology or
correspondence data.

## 2. Lemma

```text
Lemma 190.1 (Finite-part renormalization is not the square carrier).

Let

  dim_b(k) = ceil(log_b k)

be the CC-ceiling graded-tolerance dimension from doc 189. Its quantized
tower has Laurent expansion

  Sum_{k>=1} ceil(log_b k) k^{-s}
    = -1/(2 log b) * 1/s + FP_b + O(s)

after separating the smooth regularized total. The pole residue and finite
part are

  residue_b = -1/(2 log b),
  FP_b      = b/(b-1) - 5/4.

For the two CC bases:

  b=2: residue = -1/(2 log 2),  finite part = 3/4;
  b=3: residue = -1/(2 log 3),  finite part = 1/4.

These data are base-dependent. The finite parts do not equal the smooth
derived totals

  log(2 pi)/(2 log 2),  log(2 pi)/(2 log 3).

Therefore keeping FP_b after subtracting the pole is a regularization
selector unless a carrier-native rule constructs the base and finite-part
prescription.

No such rule is supplied by the CC-ceiling tower. It also supplies no square
H^2, no intersection form, no correspondence algebra, no Frobenius graph, no
positive Rosati, no Laurent boundary map, and no torsor splitter.

Thus finite-part renormalization of the CC-ceiling tower is not
construction-grade End(S^2/Z). A surviving finite-part route must construct
a carrier-native aggregation and independently construct the square
cohomology, correspondences, Laurent boundary, and Rosati data.
```

Verdict label:

```text
N1B_CC_FINITE_PART_RENORMALIZATION__BASE_DEPENDENT_SELECTOR_NOT_SQUARE_CORRESPONDENCE__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_finite_part_renormalization_no_go` verifies the finite
statement.

CFR1 records that the pole-subtraction datum is nonzero and base-specific:

```text
residue_b2 = -1/(2 log 2);
residue_b3 = -1/(2 log 3).
```

CFR2 records the rational base-dependent finite parts:

```text
FP_b2 = 3/4;
FP_b3 = 1/4.
```

CFR3 compares these with the smooth derived totals:

```text
log(2 pi)/(2 log 2) = 1.325748064736...
log(2 pi)/(2 log 3) = 0.836453899782...
```

CFR4 records that the finite-part defect still contains the regularized log
content:

```text
3/4 - log(2 pi)/(2 log 2);
1/4 - log(2 pi)/(2 log 3).
```

CFR5 records the selector failure: no square-native rule chooses the base or
the finite-part prescription.

CFR6 records that the S[+-1] finite part 1/4 is not evidence for a dualizing
module mechanism. The S value is 3/4, and no dualizing map is constructed.

CFR7 records that the doc-189 evasion condition has not been met: no
non-geometric exactness set and no new carrier-native aggregation are
constructed.

CFR8-CFR9 record the carrier failure: no square H^2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent axis,
boundary map, torsor splitter, or DD.4 weight>=1 datum is constructed.

CFR10 records that the base R1 obstructions and carrier guard remain.

## 4. Impact on R1

```text
R1 after docs 138-190:
  NEWLY CLOSED THIS CYCLE:
    - keeping the finite part / subtracting the pole of the CC-ceiling
      graded-tolerance tower as End(S^2/Z), carrier-native aggregation,
      square H^2/intersection/correspondence data, Frobenius graph, Laurent
      boundary data, torsor splitter, or positive Rosati (doc 190).

  STILL ADMISSIBLE:
    - a future carrier-native aggregation whose exactness set is not
      b-geometric, or whose non-zeta aggregation is supplied by new square
      structure rather than by a chosen finite-part prescription.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. Finite-part renormalization of the CC-ceiling tower is a
measured failure, not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CFR.1 pole-subtracted value as square carrier
  A proposal subtracts the CC-ceiling pole and promotes the finite part to
  End(S^2/Z). Kill it unless the finite-part prescription is carrier-native.

KILL-CFR.2 base-dependent finite part as invariant
  A proposal identifies FP_b with the derived square invariant. Kill it:
  FP_b is 3/4 for b=2 and 1/4 for b=3.

KILL-CFR.3 finite part as smooth derived total
  A proposal treats the finite part as the smooth regularized tower. Kill it:
  log(2 pi)/(2 log b) remains in the defect.

KILL-CFR.4 quarter-shift numerology
  A proposal reads the S[+-1] value 1/4 as a dualizing-module mechanism.
  Kill it unless it supplies the missing map; the S value is 3/4.

KILL-CFR.5 finite part without square H2/intersection
  A proposal gives a pole-subtracted number but no H^2, intersection form,
  or correspondence algebra. This is not End(S^2/Z).

KILL-CFR.6 finite part without Rosati/Laurent boundary
  A proposal gives a pole-subtracted number but no Frobenius graph, positive
  Rosati, Laurent boundary map, torsor splitter, or DD.4 weight>=1 datum.
  This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 53 = doc 190:
  N1B_CC_FINITE_PART_RENORMALIZATION__BASE_DEPENDENT_SELECTOR_NOT_SQUARE_CORRESPONDENCE__NO_GO.

What got built: no End object. The value is a deletion: finite-part
renormalization of the CC-ceiling tower chooses base-dependent regularized
numbers and constructs no square correspondence algebra.

What remains: construct a genuinely new carrier-native aggregation or return
to the in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
