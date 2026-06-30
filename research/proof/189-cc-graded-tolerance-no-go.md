# 189 - Graded tolerance does not construct the square carrier

Status: no-go + CC graded-tolerance derived-square repair deletion,
2026-06-20. Fifty-second cycle of the doc-137 construction arc. Doc 188
killed promoting strict-square divided-power/character data itself to
End(S^2/Z). This document tests the next repair: add the missing grading by
putting a Connes-Consani style integer tolerance dimension on each derived
degree of the square.

Witness, lead-reran this cycle:
`prime_int_n1b_cc_graded_tolerance_no_go` (CGT1-CGT10 ALL PASS) -- exact
graded-tolerance input flags, geometric exactness sets, pole residues,
rational finite parts, comparison with the smooth derived total, defect
finite parts, missing H^2/intersection/correspondence/Rosati data, missing
Laurent/boundary/torsor data, residual R1 obstruction checks, and
carrier-guard checks. Adjacent heavy witness:
`prime_cc_quantization_defect` (W0-W6 ALL PASS in the Q record) supplies the
ball-arithmetic continuation underlying the pole and finite-part formulas.

## 1. Purpose

Doc 188 leaves a natural repair:

```text
The strict square has real object-level data.
Maybe a derived/tolerant square functor extracts it degree by degree.
Use CC's integer dimension on each derived degree.
```

The simplest version assigns to a degree with diagonal group size k the
integer

```text
dim_b(k) = ceil(log_b k)
```

where b=2 for the S presentation and b=3 for the S[+-1] presentation. This
buys integer dimensions degree-by-degree, but it breaks the regularized
global tower. The quantization defect has a simple pole at s=0, caused by
the geometric exactness set {b^j}. The finite part is rational and
base-dependent, not the smooth derived regularized invariant.

This document is local. It does not reject every possible derived/tolerant
square functor. It rejects the CC-ceiling graded-tolerance repair:

```text
degreewise CC tolerance dimensions on the derived square = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 189.1 (CC-ceiling graded tolerance does not supply the square carrier).

Let

  dim_b(k) = ceil(log_b k)

be the proposed integer dimension assigned degreewise to a derived-square
diagonal group of size k. The smooth derived tower has regularized total

  Sum_reg log_b(k) = log(2 pi)/(2 log b).

The quantization defect is

  D_b(s) = Sum_{k>=1} (ceil(log_b k) - log_b k) k^{-s}.

The ceiling is exact on the geometric set

  {1,b,b^2,b^3,...}.

Consequently, as recorded by the Q witness,

  D_b(s) = - 1/(2 log b) * 1/s + FP_b + O(s)

near s=0. In particular, the zeta-regularized sum of ceil(log_b k) does not
exist without adding a finite-part prescription.

The finite part of the quantized tower is rational:

  FP Sum_reg ceil(log_b k) = b/(b-1) - 5/4.

For the two CC bases:

  b=2: residue = -1/(2 log 2),  finite part = 3/4;
  b=3: residue = -1/(2 log 3),  finite part = 1/4.

These finite parts are base-dependent and do not equal the smooth derived
totals

  log(2 pi)/(2 log 2),  log(2 pi)/(2 log 3).

Thus the degreewise integer tolerance layer does not produce the regularized
derived-square invariant. It also supplies no square H^2, no intersection
form, no correspondence algebra, no Frobenius graph, no positive Rosati, no
Laurent boundary map, and no torsor splitter.

Therefore CC-ceiling graded tolerance is not construction-grade
End(S^2/Z). A surviving graded/tolerant route must specify a non-polar
aggregation or an exactness set that is not b-geometric, and independently
construct square cohomology, correspondences, the Laurent boundary, and the
positive Rosati.
```

Verdict label:

```text
N1B_CC_GRADED_TOLERANCE__GEOMETRIC_EXACTNESS_POLE_NOT_SQUARE_CORRESPONDENCE__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_graded_tolerance_no_go` verifies the finite statement.

CGT1 records that the corpus inputs do not already contain graded square
cohomology:

```text
CC tolerance is metric and ungraded;
CC Dold-Kan input is short-complex;
no graded tolerance construction is in the corpus.
```

CGT2 records the exactness sets:

```text
b=2: 1,2,4,8,16,32,64;
b=3: 1,3,9,27,81,243,729.
```

CGT3 records the simple pole residues:

```text
residue_b2 = -1/(2 log 2);
residue_b3 = -1/(2 log 3).
```

Thus the aggregate integer tower has no zeta-regularized value.

CGT4 records the rational base-dependent finite parts:

```text
FP_b2 = 3/4;
FP_b3 = 1/4.
```

CGT5 compares these with the smooth derived totals:

```text
log(2 pi)/(2 log 2) = 1.325748064736...
log(2 pi)/(2 log 3) = 0.836453899782...
```

CGT6 records that the defect finite parts carry the missing transcendental
regularized content:

```text
3/4 - log(2 pi)/(2 log 2);
1/4 - log(2 pi)/(2 log 3).
```

CGT7-CGT8 record the carrier failure: no square H^2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent axis,
boundary map, torsor splitter, or DD.4 weight>=1 datum is constructed.

CGT9-CGT10 record that the base R1 obstructions and carrier guard remain.

The heavier witness `prime_cc_quantization_defect`, already banked in the Q
record, independently checks the analytic continuation and finite-part
formulas with ball arithmetic. This doc uses the exact formulas as the R1
carrier gate.

## 4. Impact on R1

```text
R1 after docs 138-189:
  NEWLY CLOSED THIS CYCLE:
    - CC-ceiling graded tolerance on a derived square as End(S^2/Z), square
      H^2/intersection/correspondence data, Frobenius graph, Laurent boundary
      data, torsor splitter, or positive Rosati (doc 189).

  STILL ADMISSIBLE:
    - a future non-EM square functor or derived/tolerant construction whose
      exactness set is not b-geometric or whose aggregation is constructed by
      new carrier-native structure, provided it also constructs square H^2,
      intersection, correspondences, Laurent boundary data, and Rosati.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs the square data internally and finishes DD.4 weights>=1.
```

R1 is still open. Graded tolerance in this CC-ceiling form is a measured
failure, not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CGT.1 degreewise ceiling dimension as square carrier
  A proposal assigns dim_b(k)=ceil(log_b k) per derived degree and promotes
  it to the square carrier. Kill it: the aggregate has a simple pole at s=0.

KILL-CGT.2 finite part as construction
  A proposal keeps only FP Sum_reg ceil(log_b k). Kill it unless the
  finite-part prescription is carrier-native; the finite part is rational
  and base-dependent.

KILL-CGT.3 tolerance integer tower as derived invariant
  A proposal identifies the integer tolerance tower with the smooth derived
  regularized tower. Kill it: log(2 pi)/(2 log b) sits in the defect.

KILL-CGT.4 graded tolerance without square H2/intersection
  A proposal gives per-degree dimensions but no H^2, intersection form, or
  correspondence algebra. This is not End(S^2/Z).

KILL-CGT.5 graded tolerance without Rosati/Frobenius
  A proposal gives per-degree dimensions but no Frobenius graph or
  replacement correspondence and no positive Rosati. This is not the play.

KILL-CGT.6 graded tolerance without Laurent boundary/torsor
  A proposal gives per-degree dimensions but no Laurent axis, boundary map,
  torsor splitter, or DD.4 weight>=1 datum. This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 52 = doc 189:
  N1B_CC_GRADED_TOLERANCE__GEOMETRIC_EXACTNESS_POLE_NOT_SQUARE_CORRESPONDENCE__NO_GO.

What got built: no End object. The value is a deletion: CC-ceiling graded
tolerance buys integer dimensions degreewise but cannot aggregate to the
regularized square invariant and constructs no correspondence algebra.

What remains: construct a genuinely new non-EM square functor or return to
the in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
