# 126 - Carrier-reflecting envelope admission matrix

Status: operational matrix / envelope router, 2026-06-11. This
collects docs 118, 120, 121, 122, and 125 into one decision table for
envelope-mediated trace proposals. It is not a construction and does
not authorize a witness.

## 1. Purpose

Future S3 or LT76 proposals may try to pass from a strict carrier
prefix to a legal trace through an envelope:

```text
S_C --kappa_C--> Y_C
Q: ECar_L1 -> T_tr.
```

The question is not whether Q is a respectable completion. The question
is whether Q preserves the carrier field that made kappa_C selective.

## 2. Admission Order

```text
Step 0: strict prefix prerequisite
  Apply doc 103. If S_C and kappa_C do not have FIRST_MAP_PASS, stop.

Step 1: intrinsic trace check
  Apply docs 88 and 98. If Tr_L is legal on Y_C as a carrier object,
  route to docs 98/94/113/114 without using the envelope branch.

Step 2: Q-mediated trigger
  If trace legality is obtained only after Q, fill doc 120.

Step 3: carrier-forgetting check
  If Q(Y_C) does not retain the primitive field consumed by kappa_C as
  pre-trace object data, apply doc 118 and reject.

Step 4: decorated-reflection guard
  If Q(Y_C) retains the field only as label, mark, metadata, grading,
  coordinate, normalization, or post-completion tag, apply doc 125.

Step 5: carrier-reflecting target
  If Q is claimed carrier-reflecting, fill doc 122. Check CRE122.1-
  CRE122.7.

Step 6: current ledger
  Compare with doc 121. If no filled doc-122 pass replaces the current
  HOLD row, no witness is licensed.

Step 7: downstream routing
  If a local envelope pass exists, route to docs 98, 94, 113, 114, and
  doc 71. Do not infer B1 admission.
```

No later step repairs failure at an earlier step.

## 3. Verdict Matrix

```text
No strict first map:
  doc 103 -> FIRST_MAP_HOLD or rejection.

Trace intrinsic on strict carrier object:
  docs 88 and 98 -> route outside the envelope branch.

Trace theorem missing:
  doc 88 -> REJECT_TRACE_ILLEGAL.

Q is needed, but not named:
  doc 120 -> HOLD_ENVELOPE.

Q named, carrier field not visible after Q:
  doc 120 -> TRIGGERS_118;
  doc 118 -> REJECT_TRACEABLE_ENVELOPE_COLLAPSE.

Q retains field only as inert decoration:
  doc 125 -> REJECT_DECORATED_ENVELOPE_REFLECTION;
  docs 120/118 -> REJECT_TRACEABLE_ENVELOPE_COLLAPSE.

Q retains field, but controls can form same Q(Y_C):
  doc 122 -> REJECT_TRACEABLE_ENVELOPE_COLLAPSE or
  HOLD_CARRIER_REFLECTION depending on scope.

Q retains field, controls fail, but downstream package ignores field:
  doc 122 -> HOLD_CARRIER_REFLECTION or route to doc 111 if the field
  is forgotten before M_C/F_C/Tr_L.

Q retains field, but bank is replaced:
  doc 122 -> REJECT_BANK; route to doc 89.

Q retains field, but freeze is missing:
  doc 122 -> REJECT_FREEZE; route to doc 91.

CRE122.1-CRE122.7 supplied:
  doc 122 -> PASS_CARRIER_REFLECTING_ENVELOPE;
  route to docs 98, 94, 113, 114, and doc 71 as a local pass only.
```

## 4. Minimal Positive Record

A proposal that wants local envelope advancement must supply:

```text
strict prefix:
  S_C:
  kappa_C:
  primitive field consumed before M_C/F_C/Tr_L:

envelope:
  Q:
  target T_tr:
  trace theorem:
  why Q is needed:

carrier reflection:
  retained primitive field:
  pre-trace object data in Q(Y_C):
  why not label/decoration:
  doc-125 status:

control after Q:
  Epstein Q(Y_C) formable? YES/NO:
  Epstein trace theorem applies? YES/NO:
  DH Q(Y_C) formable? YES/NO:
  DH trace theorem applies? YES/NO:
  exact failed axiom:

downstream dependence:
  M_C uses retained field:
  F_C uses retained field:
  Tr_L uses retained field:

bank and freeze:
  B0 fields preserved:
  guard preserved:
  zero-free freeze:

verdict:
  PASS_CARRIER_REFLECTING_ENVELOPE |
  HOLD_CARRIER_REFLECTION |
  REJECT_DECORATED_ENVELOPE_REFLECTION |
  REJECT_TRACEABLE_ENVELOPE_COLLAPSE |
  REJECT_TRACE_ILLEGAL |
  REJECT_BANK |
  REJECT_FREEZE |
  OUT_OF_SCOPE:
```

## 5. Current Status

```text
No current route has FIRST_MAP_PASS.
No current route has a named carrier-reflecting Q.
No current route has PASS_CARRIER_REFLECTING_ENVELOPE.
Doc 121 remains the current no-pass ledger.
No S3, LT76, A6, or B1 witness is licensed by the envelope branch.
```

## 6. Relation To Existing Docs

```text
doc 88
  Trace legality.

doc 98
  Strict Euler-carrier trace-domain target.

doc 103
  Strict first-map prerequisite.

doc 118
  Traceable-envelope collapse no-go.

doc 120
  Envelope operation audit.

doc 121
  Current no-pass ledger.

doc 122
  Positive carrier-reflecting envelope target.

doc 123
  Sendable packet for the positive target.

doc 125
  Decorated-envelope reflection no-go.

doc 127
  Current no-pass ledger for this matrix.
```

## 7. Use Rule

Before treating any envelope-mediated trace theorem as progress, fill
this matrix. If the result is not `PASS_CARRIER_REFLECTING_ENVELOPE`,
do not compute a witness. If it is a pass, continue through doc 98,
doc 94, doc 113 or doc 114, and doc 71 before any witness.
