# 122 - Carrier-reflecting envelope theorem target

Status: positive theorem target / doc-120 escape specification,
2026-06-11. This records the minimal theorem that would let a
traceable envelope avoid doc 118. It is not a construction and does not
claim such an envelope exists.

## 1. Purpose

Docs 118-121 establish the current envelope boundary:

```text
If trace legality is obtained only after an envelope Q and Q forgets
the primitive carrier field, reject.
No current S3/LT76 route has a carrier-reflecting Q pass.
```

This document states the positive target needed to change that status.

## 2. Target Statement

### CRE122 - Carrier-Reflecting Traceable Envelope

A future proposal may escape doc 118 only by naming:

```text
Q: ECar_L1 -> T_tr
```

and proving all of:

```text
CRE122.1 strict source
  S_C and kappa_C are named, and kappa_C consumes a primitive carrier
  field before M_C, F_C, or Tr_L exists.

CRE122.2 traceability after Q
  Q(Y_C) lies in a category where the claimed trace/properness/
  duality/nuclearity/trace-class theorem applies.

CRE122.3 carrier reflection
  The primitive field consumed by kappa_C is retained by Q(Y_C) as
  object data visible before trace evaluation, not merely as a label,
  decoration, parameter name, or post-trace readout.

CRE122.4 control exclusion after Q
  Epstein/DH controls cannot form the same typed Q(Y_C), or cannot
  satisfy the same traceability theorem, for a structural reason that
  occurs before signs, positivity, regularization, or zero comparison.

CRE122.5 Q-determined downstream dependence
  If M_C, F_C, or Tr_L(F_C) are Q-determined, their construction still
  uses the retained primitive field as load-bearing object data.

CRE122.6 conservative bank embedding
  B0 comb, q/log address, Count0/RR layer, and the Epstein guard embed
  into the Q-mediated package without replacement by a parallel shadow.

CRE122.7 zero-free freeze
  S_C, kappa_C, Q, Q(Y_C), control exclusions, formulas, constants,
  domains, codomains, and first zero contact are frozen before any
  zero-side comparison.
```

## 3. Fillable Record

```text
candidate:
source theorem:

strict prefix:
  S_C:
  kappa_C:
  primitive field consumed:
  proof before M_C/F_C/Tr_L:

envelope:
  Q:
  source:
  target T_tr:
  trace theorem:
  theorem hypotheses:

carrier reflection:
  retained primitive field:
  how Q(Y_C) stores it as object data:
  pre-trace observable:
  why this is not a label/decoration:
  doc-125 decorated-reflection audit:

control exclusion after Q:
  Epstein Q(Y_C) formable? YES/NO:
  Epstein trace theorem applies? YES/NO:
  DH Q(Y_C) formable? YES/NO:
  DH trace theorem applies? YES/NO:
  exact failed field or axiom:

downstream dependence:
  M_C uses retained field:
  F_C uses retained field:
  Tr_L or trace theorem uses retained field:

bank/freeze:
  B0 fields preserved:
  guard preserved:
  zero-free freeze:

doc-120 status:
  ESCAPES_118 | HOLD_ENVELOPE | TRIGGERS_118 | OUT_OF_SCOPE:

verdict:
  PASS_CARRIER_REFLECTING_ENVELOPE |
  HOLD_CARRIER_REFLECTION |
  REJECT_TRACEABLE_ENVELOPE_COLLAPSE |
  REJECT_TRACE_ILLEGAL |
  REJECT_BANK |
  REJECT_FREEZE |
  OUT_OF_SCOPE:
```

## 4. Decision Rule

```text
PASS_CARRIER_REFLECTING_ENVELOPE
  CRE122.1-CRE122.7 are supplied. Route to docs 98, 94, 113, 114, and
  doc 71 as a local pass only.

HOLD_CARRIER_REFLECTION
  Q is plausible, but carrier reflection, control exclusion after Q,
  downstream dependence, bank embedding, or freeze is incomplete.

REJECT_TRACEABLE_ENVELOPE_COLLAPSE
  Q is carrier-forgetting. Route to docs 118, 120, and 121.

REJECT_TRACE_ILLEGAL
  Neither intrinsic trace legality nor Q-mediated trace legality is
  supplied. Route to doc 88.
```

No positive verdict here implies B1 admission, Count/Compare,
positivity, H_odd, LS3, BC13, or RH.

## 5. Expert Question

Ask only after a proposed Q is named:

```text
Does the traceable envelope Q retain the primitive carrier field
consumed by kappa_C as pre-trace object data, and do Epstein/DH controls
fail to form the same Q(Y_C) or satisfy the same trace theorem?
```

Useful answers:

```text
ADVANCE
  prove CRE122.1-CRE122.7 for the named Q;

KILL
  prove Q is carrier-forgetting for the stated formalism;

SHARPEN
  name the exact reflection invariant, marked object, or traceability
  theorem needed to decide whether Q is carrier-reflecting.
```

## 6. Relation To Existing Docs

```text
doc 88
  Supplies trace-legality requirements.

doc 98
  Supplies the strict Euler-carrier trace-domain target.

doc 103
  Supplies the strict first-map prerequisite.

doc 118
  Rejects carrier-forgetting traceable envelopes.

doc 120
  Supplies the operation audit for Q.

doc 121
  Records that no current route has this pass.

doc 123
  Supplies the sendable external packet for deciding this target.

doc 125
  Rejects attempts to satisfy carrier reflection by inert labels,
  metadata, decorative gradings, or post-completion tags.

doc 126
  Routes the whole envelope branch and states when this target can be
  used as a local pass.
```

## 7. Use Rule

Do not claim an envelope-mediated trace pass by naming a completion or
trace-class category. Fill this record. If the primitive field consumed
by kappa_C is not visible in Q(Y_C) before trace evaluation, route to
doc 118. If it is visible, record the exact theorem and continue to the
local route matrices.
