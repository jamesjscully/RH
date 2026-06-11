# 113 - S3 strict-route admission matrix

Status: operational matrix / current S3 router, 2026-06-11. This
collects the post-doc-112 S3 route into one decision table. It is not a
new theorem and does not authorize a witness.

## 1. Purpose

The S3 route now has several adjacent gates:

```text
doc 103
  first primitive carrier-consuming map;

doc 109
  no relabeled-shadow first map;

doc 111
  no strict prefix that is forgotten before M_C/F_C/Tr_L;

doc 112
  no late carrier reintroduction after a shadow trace package exists;

doc 118
  no carrier-forgetting traceable envelope after a strict prefix;

doc 120
  operation audit for deciding whether a traceable envelope triggers
  doc 118;

doc 121
  current no-pass ledger for the traceable-envelope audit;

doc 122
  positive carrier-reflecting envelope theorem target;

doc 125
  no inert labels, metadata, or post-completion tags as envelope
  reflection;

doc 126
  envelope admission matrix collecting docs 118/120/121/122/125;

doc 127
  current no-pass ledger for the envelope matrix;

doc 98 and doc 94
  strict trace domain and trace-derived same-form codomain.
```

This matrix records the order in which a future S3 proposal should be
classified.

## 2. Admission Order

```text
Step 0: existing broad no-goes
  Apply docs 74, 93, 97, 100, 101, 102, and 108.

Step 1: first-map record
  Fill doc 103. If no S_C and kappa_C are named, verdict
  FIRST_MAP_HOLD or REJECT_NO_PRIMITIVE_FIELD.

Step 2: relabeling guard
  Apply doc 109. If S_C is only decorated shadow data, reject before
  doc 98.

Step 3: downstream dependence guard
  Apply doc 111. If kappa_C consumes a primitive field but M_C/F_C/Tr_L
  forgets it, reject before doc 98.

Step 4: late-reintroduction guard
  Apply doc 112. If carrier data enters only after a shadow package is
  formed, reject before doc 98.

Step 5: traceable-envelope guard
  Apply doc 118 if Tr_L becomes legal only after an envelope or
  completion Q. Use doc 120 to classify Q. If Q forgets the primitive
  carrier field consumed by kappa_C, reject before doc 98. Use doc 121
  for the current no-pass state. Use doc 122 for a claimed
  carrier-reflecting envelope pass, and doc 125 for decorated envelope
  false positives. Use doc 126 as the compact envelope router and doc
  127 for the current no-pass status.

Step 6: strict-domain target
  Apply doc 98. Check trace legality, bank embedding, same-form mixed
  object, carrier exclusion, and freeze.

Step 7: trace-derived codomain target
  Apply doc 94. Check that F_C and the carrier-reading form are
  theorem-derived, not externally supplied.
```

No later step can repair failure at an earlier step.

## 3. Verdict Matrix

```text
No source object S_C:
  doc 103 -> FIRST_MAP_HOLD or REJECT_NO_PRIMITIVE_FIELD.

S_C is a decorated shadow:
  doc 109 -> REJECT_RELABELING or REJECT_DECORATED_SHADOW_STABLE.

kappa_C exists but controls form the same decorated map:
  doc 109 -> REJECT_CONTROL_FORMABLE.

kappa_C exists but its primitive field is forgotten before M_C/F_C/Tr_L:
  doc 111 -> REJECT_DOWNSTREAM_FORGETFUL or REJECT_ORPHAN_FIRST_MAP.

M_C/F_C/Tr_L exists first in a shadow category, then carrier data is
added:
  doc 112 -> REJECT_SHADOW_PACKAGE_FIRST,
  REJECT_LATE_CARRIER_REINTRODUCTION, or
  REJECT_POST_TRACE_DECORATION.

The downstream package is formable for Epstein/DH:
  docs 87, 108, 111, 112, or 118 -> REJECT_CARRIER_OVERREACH /
  REJECT_CARRIER_BLIND.

The trace becomes legal only through a carrier-forgetting envelope:
  docs 118 and 120 -> REJECT_TRACEABLE_ENVELOPE_COLLAPSE or
  REJECT_TRACE_ILLEGAL.

The strict package loses the B0 comb/address/count/guard:
  doc 89 -> REJECT_BANK.

The bank and continuum do not enter one mixed object:
  doc 86 -> REJECT_LS4 or REJECT_SIDE_BLOCK.

The trace theorem is missing:
  doc 88 or doc 98 -> REJECT_TRACE_ILLEGAL.

The carrier-reading codomain/form is externally supplied:
  doc 93 or doc 94 -> REJECT_FREE_WEIGHT.

The object or exclusion is selected after zero-side contact:
  doc 91 -> REJECT_FREEZE.

All strict-route fields are supplied:
  doc 103 FIRST_MAP_PASS;
  docs 109/111/112/118 do not apply;
  doc 98 PASS_STRICT_EULER;
  doc 94 PASS_TRACE_DERIVED.
```

Even the final line is not B1 admission. It only advances the S3 local
construction route to the rest of the B1 ledgers.

## 4. Minimal Positive Record

A proposal that wants local S3 advancement must supply all of:

```text
source:
  S_C:
  primitive fields as object data:

first map:
  kappa_C:
  primitive field consumed first:
  proof before M_C/F_C/Tr_L:

control exclusion:
  Epstein source object? YES/NO:
  Epstein kappa_C? YES/NO:
  DH source object? YES/NO:
  DH kappa_C? YES/NO:
  selected control branch:

downstream dependence:
  where consumed field appears in M_C:
  where consumed field appears in F_C:
  where consumed field appears in Tr_L or trace theorem:

no late repair:
  first traceable package:
  carrier field present before package? YES/NO:
  if no, route to doc 112:

strict trace domain:
  trace theorem:
  bank embedding:
  same-form mixed object:
  trace-derived codomain:
  zero-free freeze:
```

Blank `downstream dependence` or `no late repair` fields force HOLD or
rejection before witness work.

## 5. Current Status

Current local status is:

```text
No A1-A6 S3 ansatz has FIRST_MAP_PASS.
No ansatz has passed docs 109, 111, 112, and 118.
No ansatz has PASS_STRICT_EULER or PASS_TRACE_DERIVED.
No S3 witness is licensed.
```

## 6. Relation To Existing Docs

```text
doc 99
  Gives the local S3 status audit. Doc 113 is the compact route matrix
  for applying that status.

doc 103 and doc 104
  Supply and fill the first-map record.

doc 109, doc 111, doc 112
  Supply the new strict-route hardening guards.

doc 118
  Rejects strict prefixes whose trace legality requires a
  carrier-forgetting traceable envelope.

doc 120
  Supplies the fillable envelope audit for applying doc 118.

doc 121
  Records that no current S3 row has a carrier-reflecting envelope pass.

doc 122
  States the positive theorem target for a carrier-reflecting envelope
  pass.

doc 125
  Rejects decorated-envelope attempts to satisfy doc 122.

doc 126
  Collects the envelope branch into one admission matrix.

doc 127
  Records that no current envelope row passes.

doc 94 and doc 98
  Supply the positive theorem targets after the strict-route guards.

doc 110
  Supplies the narrow external packet for the first-map prerequisite.
```

## 7. Use Rule

Before building any S3 witness, fill this matrix. If any row routes to
a rejection, stop and record the rejection. If all rows pass or hold,
record the missing fields as HOLD. Do not turn a HOLD row into a
numerical experiment.
