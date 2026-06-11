# 128 - Carrier-reflecting envelope response rubric

Status: external-answer rubric / landing discipline, 2026-06-11. This
scores expert replies to the doc-123 carrier-reflecting envelope packet.
It prevents ordinary traceability or decorated marks from being promoted
to CRE122 progress.

## 1. Purpose

Doc 123 asks whether a traceable envelope

```text
Q: ECar_L1 -> T_tr
```

retains the primitive field consumed by `kappa_C` as pre-trace object
data and excludes Epstein/DH controls after Q. Doc 126 gives the route
matrix. This rubric states when an answer changes the program.

The rule is:

```text
An answer changes the trajectory only if it decides a doc-126 row by
naming a theorem, object, obstruction, or smaller test for Q.
```

Everything else lands in doc 61 as DEMOTE or OUT_OF_SCOPE.

## 2. Required Landing Record

Every carrier-reflecting-envelope answer must be entered in doc 61
with these fields before TODO, HANDOFF, doc 60, doc 113, doc 114,
doc 116, or any envelope ledger changes.

```text
CRE response id:
source packet: doc 123
expert/community:
quoted answer location:

claim type:
  construction | no-go | missing theorem | analogy | background:

named Q:
source category:
target T_tr:
trace theorem:
strict prefix assumed:
  S_C:
  kappa_C:
  primitive field consumed:

carrier reflection claim:
  retained primitive field:
  pre-trace observable:
  object-data status:
    object data | inert mark | label | metadata | unknown:
  doc-125 route:
    REJECT_DECORATED_ENVELOPE_REFLECTION |
    HOLD_CARRIER_REFLECTION |
    ROUTE_TO_DOC122 |
    OUT_OF_SCOPE:

control after Q:
  Epstein Q(Y_C) formable? YES | NO | unknown:
  Epstein trace theorem applies? YES | NO | unknown:
  DH Q(Y_C) formable? YES | NO | unknown:
  DH trace theorem applies? YES | NO | unknown:
  exact failed field or axiom:

doc-120 route:
  TRIGGERS_118 | ESCAPES_118 | HOLD_ENVELOPE | OUT_OF_SCOPE:

doc-122 route:
  PASS_CARRIER_REFLECTING_ENVELOPE |
  HOLD_CARRIER_REFLECTION |
  REJECT_TRACEABLE_ENVELOPE_COLLAPSE |
  REJECT_TRACE_ILLEGAL |
  REJECT_BANK |
  REJECT_FREEZE |
  OUT_OF_SCOPE:

doc-126 route:
  PASS_ROW | HOLD_ROW | REJECT_ROW | OUT_OF_SCOPE:

doc-127 current row changed? YES | NO:
bank/freeze status:
downstream M_C/F_C/Tr_L dependence:
scope:
scope explicitly not covered:
banked failure repeated:
new information supplied:
minimal next test:
rubric verdict:
  ADVANCE | KILL | SHARPEN | DEMOTE | OUT_OF_SCOPE:
repo updates made:
```

If any field is unknown, write `unknown`; do not infer it.

## 3. Verdicts

### ADVANCE

Use `ADVANCE` only if the answer supplies all of:

```text
A128.1 named Q and trace theorem
  Q: ECar_L1 -> T_tr is named, and the trace/properness/duality/
  nuclearity/trace-class theorem on Q(Y_C) is named with hypotheses.

A128.2 strict prefix dependency
  The answer assumes or supplies S_C and kappa_C, and identifies the
  primitive field consumed before M_C/F_C/Tr_L.

A128.3 carrier reflection
  Q(Y_C) retains that primitive field as pre-trace object data, not as
  a label, metadata, decorative grading, coordinate, normalization, or
  post-completion tag.

A128.4 control exclusion after Q
  Epstein/DH controls cannot form the same Q(Y_C), or cannot satisfy
  the same trace theorem, for a named structural reason before signs,
  positivity, regularization, or zero comparison.

A128.5 downstream dependence
  M_C, F_C, or Tr_L uses the retained field as load-bearing object data
  if those objects are Q-determined.

A128.6 bank/freeze
  B0 bank data and the guard are preserved, and the record is
  zero-free.
```

An `ADVANCE` is local only. It routes to docs 98, 94, 113, 114, and
doc 71. It does not admit B1 or prove LS3, BC13, Count/Compare, H_odd,
positivity, or RH.

### KILL

Use `KILL` only if the answer proves one of:

```text
K128.1 carrier-forgetting envelope
  Q necessarily forgets the primitive field in the stated formalism.

K128.2 decorated reflection
  Q retains the field only as an inert mark, metadata, decorative
  grading, coordinate, normalization, or post-completion tag; doc 125
  applies.

K128.3 control formability after Q
  Epstein/DH controls can form the same Q(Y_C) and satisfy the same
  trace theorem.

K128.4 trace illegality
  No intrinsic or Q-mediated trace theorem exists for the stated
  carrier object.

K128.5 bank or freeze impossibility
  The bank embedding or zero-free freeze required by CRE122 is
  impossible in the stated class.
```

A kill must list hypotheses. If the scope is unclear, classify as
`SHARPEN`, not `KILL`.

### SHARPEN

Use `SHARPEN` when the answer identifies a concrete smaller decision:

```text
S128.1 the exact marked-object structure needed for Q to reflect the
  carrier;

S128.2 the reflection invariant that distinguishes prime-power carriers
  from Epstein/DH after Q;

S128.3 the traceability theorem whose hypotheses decide whether Q is
  carrier-reflecting;

S128.4 the control object or counterexample that would decide
  formability after Q;

S128.5 the downstream-dependence theorem for M_C/F_C/Tr_L after Q.
```

`SHARPEN` should create a next theorem/test. It does not change route
status.

### DEMOTE

Use `DEMOTE` for replies that repeat known failure modes:

```text
D128.1 ordinary traceability, nuclearity, or trace-class status with no
  carrier reflection;
D128.2 Morita/localizing equivalence that preserves only shadow data;
D128.3 retained carrier field only as label, metadata, decorative
  grading, coordinate, normalization, or post-completion tag;
D128.4 kernel/correspondence formula after Q with no control exclusion;
D128.5 post-trace carrier repair;
D128.6 Route A/B0 calibration;
D128.7 zero-side behavior before freeze.
```

### OUT_OF_SCOPE

Use `OUT_OF_SCOPE` for relevant mathematics that does not address Q,
carrier reflection, control formability after Q, or CRE122.

## 4. Propagation Rules

After entering the doc-61 record:

```text
ADVANCE:
  Update doc 122, doc 126, doc 127, and only the affected route matrix.
  Do not mark B1 admitted.

KILL:
  Update the exact no-go doc: doc 118 for carrier-forgetting, doc 125
  for decorated reflection, doc 88 for trace illegality, doc 89 for
  bank failure, or doc 91 for freeze failure.

SHARPEN:
  Add the named theorem/test to TODO and HANDOFF. Do not change route
  status.

DEMOTE:
  Record in doc 61 only.

OUT_OF_SCOPE:
  Record in doc 61 only if the source is likely to be consulted again.
```

Never propagate from memory or informal paraphrase. Record the answer
first.

## 5. Fast Scoring Checklist

For a doc-123 answer, ask in order:

```text
1. Is Q named?
2. Is the trace theorem on Q(Y_C) named?
3. Is S_C/kappa_C or the strict prefix assumption explicit?
4. Which primitive field was consumed before M_C/F_C/Tr_L?
5. Is that field object data in Q(Y_C), not decoration?
6. Does doc 125 trigger?
7. Can Epstein/DH form the same Q(Y_C)?
8. Can Epstein/DH satisfy the same trace theorem?
9. Does M_C/F_C/Tr_L still use the retained field?
10. Are B0 bank and zero-free freeze preserved?
11. Which exact doc-126 row changes?
```

If the answer cannot pass these questions, it is not an `ADVANCE`.

## 6. Use Rule

Use this rubric for every reply to doc 123 before updating any route
document. If the answer only says "Q is traceable," it is not enough.
The decisive field is carrier reflection after Q.
