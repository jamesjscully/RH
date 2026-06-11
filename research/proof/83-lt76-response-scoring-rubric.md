# 83 - LT76 response scoring rubric

Status: external-answer rubric / landing discipline, 2026-06-11. This
turns docs 61, 76, 77, 78, 81, and 82 into a scoring rule for expert
answers to the liquid trace theorem target.

## 1. Purpose

Doc 77 asks external experts for an answer on the LT76 trace target.
Doc 61 records answers. This document prevents ambiguous replies from
being promoted into trajectory changes.

The rule is:

```text
An external answer changes the program only if it identifies a theorem,
object, obstruction, or test whose consequence is falsifiable against
LT76.1-LT76.7, NO76.1-NO76.5, or G60.
```

Everything else is background, even if mathematically useful.

## 2. Required Landing Record

Every LT76 answer must be entered in doc 61 with these additional
fields before TODO, HANDOFF, doc 60, doc 76, doc 92, doc 105, doc 106,
doc 112, doc 114, or any LT76 routing/audit/clause ledger is updated.

```text
LT76 response id:
source packet:
expert/community:
quoted answer location:

claim type:
  construction | no-go | missing theorem | analogy | background:

direct doc-77 questions answered:
  Q1 scale retention:
  Q2 traceability:
  Q3 same-form coupling:
  Q4 carrier selectivity:
  Q4b trace-operation overreach:
  Q5 obstruction class:

affected LT76 clauses:
  LT76.1 | LT76.2 | LT76.3 | LT76.4 | LT76.5 | LT76.6 | LT76.7:

affected NO76 clauses:
  NO76.1 | NO76.2 | NO76.3 | NO76.4 | NO76.5:

affected G60 gates:

exact theorem/object named:
hypotheses:
scope:
scope explicitly not covered:
factor-through status:
  factors through bare B_l | proves non-factor-through | unknown:
scale verdict:
  REJECT_A1 | HOLD_A1 | PASS_A1 | OUT_OF_SCOPE:
carrier verdict:
  carrier-selective | carrier-blind | untested | out-of-scope:
doc-105 route:
  PASS_TO_DOC76 | HOLD_LT76_STRICT | REJECT_CARRIER_OVERREACH |
  REJECT_TRACE_ILLEGAL | REJECT_SIDE_BLOCK | REJECT_FREEZE |
  OUT_OF_SCOPE:
doc-112 route:
  REJECT_SHADOW_PACKAGE_FIRST | REJECT_LATE_CARRIER_REINTRODUCTION |
  REJECT_POST_TRACE_DECORATION | REJECT_FREE_WEIGHT |
  REJECT_FREEZE | OUT_OF_SCOPE:
doc-114 route:
  local PASS rows | local HOLD rows | local REJECT rows |
  OUT_OF_SCOPE:
same-form verdict:
  same-form | side-block | untested | out-of-scope:
zero-free status:
  frozen | zero-imported | untested | out-of-scope:

banked failure repeated:
new information supplied:
minimal next test:
rubric verdict:
  ADVANCE | KILL | SHARPEN | DEMOTE | OUT_OF_SCOPE:
repo updates made:
```

If any required field is unknown, write `unknown`; do not infer it.

## 3. Verdicts

### ADVANCE

Use `ADVANCE` only if the answer supplies named structure satisfying a
specific positive LT76 clause without triggering a known rejection.

Minimum requirements:

```text
A1. For LT76.1/G60.2, the answer earns PASS_A1 under doc 81 and does
    not factor through the doc-82 bare scale-blind output.

A2. For LT76.3, the answer names a traceability/proper-pushforward or
    trace-class theorem with hypotheses matching the proposed object.

A3. For LT76.5, the answer gives a same-form comb-continuum coupling,
    not a side archimedean block.

A4. For LT76.6, the answer names the first carrier/depth field needed
    by the trace and the first Epstein/DH formability failure point, and
    does not trigger doc 105 trace-operation overreach.

A5. For LT76.7, the answer is zero-free up to the frozen record.
```

`ADVANCE` may be local to one clause. It does not admit B1 unless the
doc-71 required gates are all satisfied. A decision-grade LT76
advance should eventually name `L1`, `R_L`, `T_C`, `b1`, `Tr_L`, the
same-form codomain, the traceability theorem, the structural location
of `log p`, and the Epstein/DH formability failure point.

### KILL

Use `KILL` only if the answer states a no-go theorem or obstruction
whose hypotheses cover the target class being considered.

Acceptable kills:

```text
K1. NO76.1-factor-through: the proposed trace factors through B_l and
    is rejected by doc 82.

K2. NO76.1-broad within stated hypotheses: every trace in the named
    target class forgets log p before trace.

K3. NO76.2: the named real/liquid/gaseous object lacks the required
    traceability, dualizability, nuclearity, or proper pushforward.

K4. NO76.3: every available archimedean contribution in the named
    class is a side block.

K5. NO76.4: every trace broad enough for the proposed kernel also
    computes for Epstein/DH controls, including doc-105 broad
    measure/kernel/operator/trace-class packages before carrier
    checking.

K6. NO76.5: the trace requires externally chosen Gaussian, Haar,
    density, normalization, or unit data before it is defined.
```

A kill must list its hypotheses. If the scope is unclear, classify as
`SHARPEN`, not `KILL`.

### SHARPEN

Use `SHARPEN` when the answer identifies a concrete theorem, minimal
object, or finite test whose resolution would decide a clause.

Examples:

```text
S1. Names the exact traceability theorem needed for T_C -> pt.
S2. Names the smallest enriched T_p where scale retention can be
    tested.
S3. Names the factor-through functor whose existence/nonexistence
    decides doc 82.
S4. Names the carrier-depth field needed to make Epstein unformable.
S5. Names the external unit choice that must be internalized or
    rejected.
```

`SHARPEN` should create a next action, not merely a reading suggestion.

### DEMOTE

Use `DEMOTE` when the answer repeats a banked failure mode.

Demote answers that provide only:

```text
D1. ordinary Shv(S^1), bare localizing invariants, or homotopy-circle
    traces;
D2. Route A/Tate/RR/Poisson calibration without B1 scale retention;
D3. post-trace factors l, 1/l, 2pi/l, residues, determinants, or
    normalizations;
D4. side archimedean blocks;
D5. theta/count/Poisson shadows that also compute for Epstein;
D6. Gaussian/Haar/unit choices inserted by hand;
D7. zero-side facts used before freeze;
D8. generic measure/kernel/operator/trace-class packages that accept
    represented-norm or DH controls before primitive carrier checking.
```

`DEMOTE` entries stay in doc 61 but do not update TODO, HANDOFF, or
doc 60.

### OUT_OF_SCOPE

Use `OUT_OF_SCOPE` when the answer is relevant mathematics but does
not address the packet's target.

Examples:

```text
O1. General background on liquid geometry without T_C traceability.
O2. RH or zero-distribution comments.
O3. Positivity, Count, or Compare remarks that do not touch LT76.
O4. Literature pointers with no theorem/object/obstruction identified.
```

Do not record an out-of-scope answer as `DEMOTE`; `DEMOTE` is for
repeated banked failure modes. `OUT_OF_SCOPE` records relevant
mathematics that simply does not decide the packet.

## 4. Propagation Rules

After entering the doc-61 record:

```text
ADVANCE:
  Update the exact affected docs only. If PASS_A1 is earned, update
  doc 81 and then doc 60 G60.2. If traceability or same-form coupling
  advances, update doc 76, doc 60, and the doc-114 matrix row. Do not
  mark B1 admitted unless doc 71 is fully satisfied.

KILL:
  Update doc 76 for the killed NO76 clause and doc 60 for the affected
  gate. If the kill is factor-through only, cite doc 82 and preserve
  doc 78's broad-open caveat. If the kill is trace-operation overreach
  or late carrier reintroduction, route through docs 105/106/112/114.

SHARPEN:
  Add the minimal next theorem/test to TODO and HANDOFF. Do not change
  gate status.

DEMOTE:
  Record in doc 61 only.

OUT_OF_SCOPE:
  Record in doc 61 only if the source is likely to be consulted again.
```

Never propagate from memory or from an informal paraphrase. The quoted
answer location must be recorded first.

## 5. Fast Scoring Checklist

For any LT76 answer, ask in order:

```text
1. Does it decide a named LT76 or NO76 clause?
2. Does it name the theorem/object/obstruction and its hypotheses?
3. Does it name the package L1, R_L, T_C, b1, Tr_L if it claims a
   construction?
4. Are internal R/T objects and Tr_L legal under docs 90 and 88?
5. Does it pass doc 81 for scale retention, or fail by docs 80/82?
6. Does it avoid Route A/B0 calibration being promoted to B1?
7. Does it preserve the B0 bank under doc 89?
8. Does it distinguish same-form coupling from side-block data under
   doc 86?
9. Does it test carrier selectivity against Epstein/DH and avoid docs
   105/108/112 overreach?
10. Is it zero-free until the frozen record?
11. What exact repo document changes, if any, follow?
```

If no exact document change follows, the verdict is `DEMOTE`,
`SHARPEN`, or `OUT_OF_SCOPE`, not `ADVANCE` or `KILL`.

## 6. Relation To Existing Docs

```text
doc 61
  Receives the normalized external answer record.

doc 76
  Supplies LT76.1-LT76.7 and NO76.1-NO76.5.

doc 77
  Supplies the sendable expert packet.

doc 78
  Preserves the overclaim boundary: broad real/liquid trace questions
  remain open unless explicitly killed.

doc 81
  Scores A1 scale retention as REJECT_A1, HOLD_A1, PASS_A1, or
  OUT_OF_SCOPE.

doc 82
  Scores factor-through scale collapse.

doc 84
  States the minimal positive theorem target for non-factorization.

doc 85
  Rejects object-level enrichment unless the trace/domain/value detects
  it before evaluation.

doc 86
  Scores LT76.5 same-form coupling claims.

doc 87
  Scores LT76.6 carrier-selectivity claims.

doc 88
  Scores LT76.3 traceability/proper-pushforward claims.

doc 89
  Scores LT76.4 conservative bank-embedding claims.

doc 90
  Scores LT76.2 internal archimedean object claims.

doc 91
  Scores LT76.7 zero-free freeze claims.

doc 92
  Routes LT76 clauses and prevents cross-gate inference.

doc 105
  Gives the conditional trace-operation overreach audit for LT76.6.

doc 106
  Records the current no-pass LT76 state after applying doc 105.

doc 112
  Rejects late carrier reintroduction after a shadow trace package.

doc 114
  Supplies the current strict-trace admission matrix and no-witness
  status for LT76/A6.
```

This rubric is the landing protocol for external answers. It does not
itself change any mathematical gate.
