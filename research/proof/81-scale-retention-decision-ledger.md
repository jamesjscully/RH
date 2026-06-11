# 81 - Scale retention decision ledger

Status: operational ledger / A1 positive boundary, 2026-06-11. This
turns docs 51, 63, 76, and 80 into a decision record for claims that a
candidate retains `log p` before trace evaluation.

## 1. Purpose

Docs 51 and 63 kill bare scale retention. Doc 80 kills post-trace
scale insertion. The remaining live question is narrower:

```text
does the candidate name a structural datum that contains log p before
the load-bearing trace/invariant is evaluated?
```

This document is not a B1 construction. It is the required A1 record
for any future B1/A6 candidate before the candidate can claim scale
retention.

## 2. Required Record

Every scale-retention claim must fill the following fields.

```text
candidate:
date:
source theorem/object:

pre-trace object O_p:
  category:
  object/correspondence/kernel:
  first map where O_p is formed:

scale carrier:
  metric coefficient:
  analytic-ring norm:
  equivariant datum:
  density/measure:
  kernel parameter:
  stronger retained structure:

trace/invariant:
  name:
  domain:
  codomain:
  traceability theorem:
  naturality/functoriality used:

deletion test:
  operation replacing log p by arbitrary l > 0:
  object after deletion:
  trace value after deletion:
  observed/proved dependence on l:

late-insertion audit:
  first formula containing log p:
  is this before trace evaluation:
  is any 1/log p, 2pi/log p, Haar density, Gaussian width,
  residue, or normalization appended after trace:

same-form coupling:
  banked comb input:
  continuum input:
  shared index/Gram/count form:

verdict:
  REJECT_A1 | HOLD_A1 | PASS_A1 | OUT_OF_SCOPE:
```

Blank answers are allowed only in unused carrier fields. Blank
answers for `pre-trace object`, `scale carrier`, `trace/invariant`,
`deletion test`, or `late-insertion audit` force `REJECT_A1` or
`HOLD_A1`.

## 3. Decision Rule

### A1.1 REJECT_A1

Reject the scale-retention claim if any of the following holds.

```text
R1. The pre-trace object is only the bare circle R/(log p)Z, the bare
    diagram (log p)Z -> R -> R/(log p)Z, or Shv(R/(log p)Z; C) with
    constant dualizable coefficients.

R2. The trace/invariant factors through a localizing-invariant output
    already identified with the corresponding output for R/lZ.

R3. The first formula containing log p occurs after trace evaluation.

R4. The candidate needs a post-trace factor such as log p, 1/log p,
    2pi/log p, a Haar density, Gaussian width, residue, determinant
    normalization, or comparison constant to look prime-specific.

R5. The deletion test replaces log p by arbitrary l > 0 without
    changing the frozen trace/invariant.
```

R1-R2 are docs 51 and 63. R3-R5 are doc 80.

### A1.2 HOLD_A1

Hold the claim if a genuine enriched carrier is named, but one of the
following remains unwritten.

```text
H1. No traceability theorem is cited for the enriched object.
H2. The deletion test is plausible but not proved.
H3. The trace sees scale but the same-form LS4 coupling is not written.
H4. The construction may depend on external unit/density choices.
H5. Carrier selectivity against Epstein/DH has not been tested.
```

HOLD_A1 is not failure. It marks the exact theorem or construction still
needed before any witness cycle is honest.

### A1.3 PASS_A1

Pass the A1 field only if all of the following are present.

```text
P1. O_p is an enriched pre-trace object, not a relabeled bare circle.
P2. log p lives in a named structural carrier before trace evaluation.
P3. The trace/invariant is defined on that enriched object.
P4. The deletion test proves the trace/invariant changes, or the
    enriched object becomes non-isomorphic, when log p is replaced by
    arbitrary l > 0.
P5. The same pre-trace structure participates in the same-form
    comb-continuum coupling required by LS4.
P6. No zero-side information chooses O_p, the trace, or the scale.
```

PASS_A1 here only advances doc 45 A1 / G60.2 / LT76.1. It does not by
itself admit B1, and it does not advance LS3, carrier selectivity,
BC13, P3, Count, Compare, or RH.

### A1.4 OUT_OF_SCOPE

Mark an answer OUT_OF_SCOPE if it concerns only:

```text
LS4 same-form coupling;
carrier selectivity;
unit derivation;
positivity or BC13;
Count/Compare;
zero-side evidence;
RH consequences.
```

Those may be useful for other gates, but they do not decide A1 unless
they also identify the pre-trace scale carrier.

## 4. Deletion Test

The deletion test is the positive counterpart to doc 80's freeze test.
Perform it before reading any zero-side comparison.

```text
Input: a claimed scale-retentive trace Tr_p(O_p).

Step 1. Freeze all formulas, constants, categories, and maps used to
        form O_p and Tr_p.

Step 2. Replace log p by an arbitrary real l > 0 at the earliest
        structural carrier named by the candidate.

Step 3. Re-evaluate only the frozen trace/invariant.

Step 4. Decide:
        no change or only notation changes => REJECT_A1;
        enriched object changes but trace effect not proved => HOLD_A1;
        trace/domain/coupling changes by theorem => PASS_A1.
```

The test must be applied at the earliest structural carrier. Applying
it only to a later readout repeats the late-insertion failure.

## 5. Examples Of Verdicts

```text
Bare Shv(R/(log p)Z; C), constant coefficients:
  REJECT_A1 by R1-R2.

Route A Tate/RR count and Serre trace:
  REJECT_A1 as B1 scale retention, but ACCEPT as B0 calibration.

Poisson formula with 2pi/log p appended after a p-independent trace:
  REJECT_A1 by R3-R5.

Metric circle whose length is part of the trace-class domain, with a
proved traceability theorem and l-dependent trace:
  HOLD_A1 until same-form LS4 and carrier selectivity are written;
  PASS_A1 only if P1-P6 are proved.

Liquid analytic-ring quotient T_p with norms depending on log p before
kernel trace:
  HOLD_A1 until LT76.1-LT76.7 are proved or externally killed.
```

## 6. Relation To Existing Gates

```text
doc 51
  Supplies the bare sheaf/localizing-invariant rejection.

doc 63
  Supplies the bare diagram scaling rejection.

doc 71
  Requires the first log p carrier in every B1 ledger entry.

doc 76
  States the liquid trace theorem target whose LT76.1 field this
  ledger operationalizes.

doc 80
  Supplies the late-insertion freeze rejection.
```

The practical rule is:

```text
Do not mark G60.2 or LT76.1 as advanced until this ledger has a
PASS_A1 entry for the candidate. Do not promote PASS_A1 to B1
admission without the remaining doc-71 gates.
```
