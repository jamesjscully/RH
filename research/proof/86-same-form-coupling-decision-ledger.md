# 86 - Same-form coupling decision ledger

Status: operational ledger / LS4 positive boundary, 2026-06-11. This
turns docs 76 and 79 into a decision record for claims that a proposed
trace couples the banked comb and continuum on one form.

## 1. Purpose

Docs 81-85 now isolate the A1 scale-retention boundary. Passing A1 is
not enough. The next required A/B-front gate is LS4:

```text
the banked comb and the archimedean continuum must meet inside one
mixed trace object before evaluation.
```

Doc 79 rejects side archimedean blocks. This ledger records what a
positive same-form coupling claim must supply.

## 2. Required Record

Every LS4/LT76.5 claim must fill:

```text
candidate:
date:
source theorem/object:

A1 status:
  doc-81 verdict:
  doc-84/doc-85 non-factorization status:
  scale-detection source: domain | traceability theorem | frozen trace value:

bank input:
  b1(comb_C):
  valuation/depth fields used:
  conservative bank embedding:

continuum input:
  R_L:
  T_C or R_L/T_C:
  archimedean completion:
  scale carrier inherited from A1:

mixed trace object M_C:
  category:
  construction map from bank input:
  construction map from continuum input:
  traceability theorem:

same-form codomain:
  index form | Gram form | count form | stronger:
  formula or theorem statement:
  where both bank and continuum appear before evaluation:

side-block audit:
  bank-only value:
  archimedean-only value:
  post-evaluation operation:
  deletion test:

carrier guard:
  Epstein/DH formability status:
  theta/count shadow status:

zero-free freeze:
  formulas/maps/constants frozen before zero contact:

verdict:
  REJECT_SIDE_BLOCK | REJECT_LS4 | HOLD_LS4 | PASS_LS4 | OUT_OF_SCOPE:
```

Blank answers in `mixed trace object`, `same-form codomain`, or
`side-block audit` force `REJECT_LS4` or `HOLD_LS4`.

## 3. Decision Rule

### LS4.1 REJECT_SIDE_BLOCK / REJECT_LS4

Reject if any of the following holds.

```text
R1. The expression is T_bank(C) + T_arch(R/T), or a post-evaluation
    function F(T_bank(C), T_arch(R/T)).

R2. The bank input and continuum input are evaluated on separate
    domains before being combined.

R3. Deleting the archimedean part leaves a complete bank trace, and
    deleting the bank part leaves a complete archimedean correction.

R4. The same claimed coupling computes for Epstein/DH controls without
    becoming unformable at a carrier/effectivity point.

R5. The only common object is notation, normalization, determinant
    readout, or comparison after both sides are evaluated.

R6. The A1 scale-detecting structure is abandoned before the LS4
    coupling; the mixed trace uses only a scale-blind shadow.
```

R1-R3 are doc 79. R4 is the carrier guard from docs 53, 64, and 74.
R5 is the post-evaluation readout failure. R6 is the doc-85 detection
guard applied to LS4.

Use `REJECT_SIDE_BLOCK` for R1-R3 or R5. Use `REJECT_LS4` for other
LS4 failures.

### LS4.2 HOLD_LS4

Hold if a plausible mixed trace object is named but one of the
following is missing.

```text
H1. The traceability theorem for M_C is not stated.
H2. The same-form codomain is not named.
H3. The maps from bank input and continuum input into M_C are not both
    written.
H4. Carrier selectivity is untested.
H5. The construction has not been frozen before zero-side comparison.
```

`HOLD_LS4` is the correct status for an A1-positive trace package whose
actual mixed LS4 theorem is still unwritten.

### LS4.3 PASS_LS4

Pass only if all of the following are supplied.

```text
P1. One mixed trace object M_C exists before evaluation.
P2. b1(comb_C) and R_L/T_C both map into M_C before trace.
P3. The traceability theorem applies to M_C.
P4. The output lands in one named index/Gram/count form or stronger
    codomain.
P5. The same theorem uses the A1 scale carrier; the continuum is not a
    separate side block.
P6. Epstein/DH fail at carrier/effectivity while theta/count shadows
    may remain meaningful.
P7. The record is zero-free before optional comparison.
```

`PASS_LS4` advances G60.5/LT76.5 only. It does not prove LS3, carrier
selectivity as a full B gate, BC13, P3, Count/Compare, or RH.

### LS4.4 OUT_OF_SCOPE

Mark OUT_OF_SCOPE if the answer concerns only scale retention,
traceability, unit derivation, positivity, Count/Compare, zero-side
evidence, or RH without writing the mixed comb-continuum coupling.

## 4. Same-Form Tests

Apply these tests before any witness cycle.

```text
S86.1 Mixed-object test
  Name M_C. If no mixed object exists, reject or hold.

S86.2 Two-map test
  Name the map from b1(comb_C) to M_C and the map from R_L/T_C to M_C.

S86.3 Before-evaluation test
  Verify both inputs enter M_C before Tr_L is evaluated.

S86.4 A1-continuity test
  Verify that the A1 scale-detecting structure is still present in the
  mixed object. If it is forgotten before LS4, doc 85 blocks promotion.

S86.5 Deletion test
  Delete either input. If the remaining expression is still a complete
  trace of the same candidate, the proposal is side-block data.

S86.6 Common-codomain test
  State the index/Gram/count form receiving the coupled trace.

S86.7 Timing test
  Identify the first formula containing the archimedean contribution.
  If it appears only after bank trace evaluation, reject as a side
  block.

S86.8 Control test
  Replace p^Z by the Epstein represented-norm control. If the mixed
  trace still computes as theta/count/Poisson data, reject carrier
  selectivity or hold until the death point is named.
```

## 5. Relation To A1

A1 and LS4 are independent gates.

```text
A1 PASS, LS4 FAIL
  The trace detects scale, but the archimedean contribution is a side
  block or independent readout.

A1 HOLD, LS4 HOLD
  The object may be enriched, but neither scale detection nor mixed
  coupling is proved.

A1 PASS, LS4 PASS
  The same pre-trace structure that detects scale also participates in
  the mixed comb-continuum trace. This advances only the A/B/LS4
  front, not B1 admission by itself.
```

Do not use A1 scale retention as a substitute for the mixed trace
object required by LS4.

## 6. Expert Question

For an external expert, ask:

```text
Can you name a trace-class mixed object M_C in which b1(comb_C) and
R_L/T_C both enter before trace evaluation, with output in one
index/Gram/count form? If not, is there a theorem forcing every
available archimedean contribution to be a side block?
```

Useful answers must identify:

```text
M_C:
bank-to-M_C map:
continuum-to-M_C map:
traceability theorem:
same-form codomain:
Epstein/DH failure point:
side-block exclusion theorem:
```

## 7. Relation To Existing Docs

```text
doc 76
  LT76.5 names the same-form coupling target.

doc 79
  Rejects side-block normal forms.

doc 81-85
  Govern A1 scale retention and non-factorization. They do not by
  themselves prove LS4.

doc 60
  G60.5 requires same-form LS4 coupling before B1 admission.

doc 71
  B1 admission still also requires carrier selectivity, LS3 status,
  and zero-free freeze.
```

The operational rule is:

```text
Do not mark LT76.5 or G60.5 advanced until this ledger has a PASS_LS4
entry for the candidate.
```
