# 88 - Traceability proper-pushforward ledger

Status: operational ledger / LT76.3 legality boundary, 2026-06-11.
This records what must be proved before a proposed liquid/gaseous or
kernel trace `Tr_L` is a legal trace rather than a formal expression.

## 1. Purpose

Docs 81-87 split the front gates into scale retention, same-form
coupling, and carrier selectivity. All of them presuppose that the
trace itself exists.

LT76.3 is the legality gate:

```text
T_C -> pt must be traceable, dualizable, proper, nuclear, or
trace-class enough in the named category to define Tr_L.
```

This ledger records the required theorem before `Tr_L` can be used in
A1, LS4, or carrier-selectivity claims.

## 2. Required Record

Every traceability claim must fill:

```text
candidate:
date:
source theorem/object:

category:
  L1:
  objects:
  morphisms/correspondences:
  monoidal or kernel structure:

trace object:
  T_C:
  map T_C -> pt:
  kernel/correspondence category:
  proposed trace Tr_L:

traceability theorem:
  theorem name:
  source location:
  source:
  hypotheses:
    dualizable:
    compact/proper:
    nuclear/trace-class:
    finiteness:
    continuity/completeness:
    base-change/naturality:
  codomain:

enrichment status:
  metric/liquid/equivariant/density/kernel data retained:
  does the theorem apply before forgetting enrichment:
  does the theorem apply before forgetting carrier fields:
  traceable envelope Q, if any:
  primitive carrier field visible after Q:

failure modes checked:
  nonproper:
  nondualizable:
  nonnuclear:
  no trace-class kernels:
  only ordinary Shv(S^1):
  only compact complex/Tate curve Route A:

interaction with other gates:
  A1 status:
  LS4 status:
  carrier status:
  zero-free freeze:

verdict:
  REJECT_TRACE | REJECT_OVERCLAIM | HOLD_TRACE | PASS_TRACE |
  OUT_OF_SCOPE:
```

Blank answers in `traceability theorem` or its hypotheses force
`REJECT_TRACE` or `HOLD_TRACE`.

## 3. Decision Rule

### T.1 REJECT_TRACE

Reject if any of the following holds.

```text
R1. No theorem is named that makes T_C -> pt traceable, dualizable,
    proper, nuclear, or trace-class in L1.

R2. The theorem applies only after forgetting the enriched structure
    needed by A1.

R2b. The theorem applies only after a traceable envelope or completion
     that forgets the primitive carrier fields needed by carrier
     selectivity. Route to doc 118 when S3/LT76.6 is claimed.

R3. The theorem applies only to ordinary compact topological circles,
    bare Shv(S^1), or localizing-invariant shadows.

R4. The only available theorem is Route A/Tate-curve liquid Serre
    duality or HRR, while the proposed object is a real/liquid circle
    trace.

R5. The trace is written as a formal integral, determinant, residue,
    or kernel pairing with no trace-class/proper-pushforward theorem.

R6. The trace requires hand-chosen Gaussian, Haar measure, density,
    normalization, or unit data before it is defined.
```

### T.2 HOLD_TRACE

Hold if a plausible theorem or category is named but one of the
following is missing.

```text
H1. The theorem's hypotheses are not matched to T_C.
H2. It is unknown whether the enriched scale carrier survives in the
    traceable category.
H2b. It is unknown whether the primitive carrier field remains visible
     after the traceable envelope or completion.
H3. The trace exists for objects but not for the kernels or
    correspondences needed by LS4.
H4. Properness/nuclearity/finiteness is plausible but not proved.
H5. Base-change or functoriality needed for carrier controls is
    unwritten.
```

`HOLD_TRACE` is the honest status for a promising external category
that has not yet supplied the actual trace theorem.

### T.3 REJECT_OVERCLAIM

Reject status inflation if any of the following holds.

```text
O1. Traceability is claimed to prove A1 scale retention.
O2. Traceability is claimed to prove LS4 same-form coupling.
O3. Traceability is claimed to prove carrier selectivity.
O4. Traceability is claimed to admit B1 without docs 81, 86, and 87
    passing separately.
O5. Traceability is claimed as RH, BC13, P3, Count/Compare, or LS3
    evidence.
```

Traceability answers whether `Tr_L` can be defined. It is not a
candidate by itself.

### T.4 PASS_TRACE

Pass only if all of the following are supplied.

```text
P1. L1 and T_C are named.
P2. The map T_C -> pt is covered by a theorem giving a trace,
    proper pushforward, duality, or trace-class kernel formalism.
P3. The hypotheses of that theorem are checked for the enriched object
    before any forgetting to bare Shv(S^1).
P4. The codomain of Tr_L is named.
P5. The theorem is strong enough for the kind of object used later:
    kernels/correspondences if LS4 needs them, not just functions.
P6. The record is zero-free before optional comparison.
P7. No external Gaussian/Haar/normalization/unit choice is inserted as
    hidden trace data.
```

`PASS_TRACE` advances LT76.3 only. It is not A1 scale retention, LS4
same-form coupling, carrier selectivity, LS3, BC13, P3, Count/Compare,
or RH.

### T.5 OUT_OF_SCOPE

Mark OUT_OF_SCOPE if the answer discusses scale retention, side-block
coupling, carrier controls, positivity, zeros, or RH without deciding
whether `Tr_L` exists.

## 4. Diagnostic Tests

```text
D88.1 Theorem test
  Name the theorem that defines Tr_L. If no theorem is named, reject
  or hold.

D88.2 Hypothesis test
  Check dualizability, properness, nuclearity, trace-class,
  finiteness, and completeness exactly as the theorem requires.

D88.3 Enrichment test
  Does the theorem apply before the scale/enriched carrier is
  forgotten? If not, A1 cannot be supported by this trace.

D88.4 Kernel-strength test
  If LS4 needs kernels or correspondences, verify the theorem covers
  those, not only scalar functions or ordinary sheaves.

D88.5 Route-A demotion test
  If the theorem is only the B0 Tate/RR calibration theorem, demote to
  calibration unless the real/liquid trace object is separately
  covered.

D88.6 Control functoriality test
  If carrier selectivity will be claimed, verify the trace theorem is
  functorial enough to state the Epstein/DH control substitution.

D88.7 Adjacent-gate audit
  Record A1, LS4, and carrier status explicitly. Do not infer them from
  PASS_TRACE.

D88.8 Envelope audit
  If a trace theorem is obtained through an envelope or completion Q,
  record whether Q is carrier-reflecting or carrier-forgetting before
  using the trace in S3/LT76.6 routing.
```

## 5. Relation To Other Gates

```text
PASS_TRACE, A1 FAIL
  A trace exists, but it forgets scale or factors through B_l.

PASS_TRACE, LS4 FAIL
  A trace exists, but bank and continuum are not coupled on one mixed
  object.

PASS_TRACE, CARRIER FAIL
  A trace exists, but it computes on Epstein/DH controls.

A1/LS4/CARRIER PASS, TRACE FAIL
  The proposed formula has the right shape but no legal trace theorem.
```

Traceability is a legality condition, not a substitute for any other
gate.

## 6. Expert Question

Ask:

```text
In the proposed liquid/gaseous/analytic-ring or kernel category, what
theorem makes T_C -> pt traceable or gives a trace-class kernel
formalism for Tr_L? Which hypotheses must be checked, and do they hold
before forgetting the enriched scale carrier?
```

Useful answers must identify:

```text
category L1:
trace object T_C:
trace theorem:
hypotheses:
codomain:
kernel/correspondence strength:
whether enrichment survives to the theorem:
```

## 7. Relation To Existing Docs

```text
doc 76
  LT76.3 names trace-class/proper pushforward.

doc 83
  Scores external answers that claim traceability.

doc 81-85
  Govern scale retention; traceability alone does not pass A1.

doc 86
  Requires kernels/correspondences if same-form LS4 uses them.

doc 87
  Requires enough functoriality to state carrier controls.
```

The operational rule is:

```text
Do not use Tr_L in A1, LS4, or carrier-selectivity claims until this
ledger has a PASS_TRACE entry for the trace package.
```
