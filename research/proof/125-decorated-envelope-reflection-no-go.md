# 125 - Decorated envelope reflection no-go

Status: bounded no-go / doc-122 false-positive guard, 2026-06-11.
This rejects attempts to satisfy carrier reflection by carrying the
primitive field only as an inert mark, label, decoration, or
post-completion parameter.

## 1. Purpose

Doc 122 allows an envelope-mediated trace route only if

```text
Q(Y_C)
```

retains the primitive field consumed by `kappa_C` as pre-trace object
data and controls cannot form the same traceable object. A cheap
failure mode is:

```text
complete first;
attach the carrier field as a mark;
claim Q is carrier-reflecting.
```

This document rules out that move unless the mark is load-bearing for
traceability, downstream formation, or control exclusion before trace
evaluation.

## 2. No-Go Statement

### DER125 - Decorated Envelope Reflection

Let

```text
S_C --kappa_C--> Y_C
Q: ECar_L1 -> T_tr
```

be a proposed doc-122 route. Suppose the primitive field consumed by
`kappa_C` appears in `Q(Y_C)` only through one of:

```text
external label;
marked parameter;
decorative grading;
metadata on an otherwise traceable object;
chosen coordinate or normalization;
post-completion tag;
readout after the trace theorem is already available.
```

Assume further:

```text
H125.1 trace theorem independence
  The trace/properness/duality/nuclearity/trace-class theorem applies
  to the underlying unmarked object.

H125.2 downstream independence
  M_C, F_C, and Tr_L(F_C) are formable from the underlying unmarked
  object, or the mark affects only notation/codomain labels.

H125.3 control markability
  Epstein/DH controls can carry the same type of mark or parameter once
  the underlying traceable object is formed.

H125.4 no pre-trace obstruction
  No axiom of T_tr prevents controls from forming the marked object
  before trace evaluation.
```

Then the proposed carrier-reflecting envelope does not satisfy
CRE122.3 or CRE122.4. Its verdict is:

```text
REJECT_DECORATED_ENVELOPE_REFLECTION
```

and it routes to:

```text
doc 120:
  TRIGGERS_118;

doc 122:
  REJECT_TRACEABLE_ENVELOPE_COLLAPSE;

doc 118:
  carrier-forgetting envelope collapse.
```

## 3. Proof Sketch

The retained field is not object data in the required sense unless it
changes what objects, maps, traceability certificates, or pre-trace
observables exist in `T_tr`.

Under H125.1, traceability is already certified without the field.
Under H125.2, the downstream package is already formed without the
field. Under H125.3-H125.4, controls can carry the same kind of mark.
Therefore the mark does not produce carrier selectivity after Q. It is
a relabeling of a traceable shadow, not a carrier-reflecting envelope.

## 4. Escape Clause

A marked or enriched envelope can escape only if it proves at least one
of:

```text
E125.1 trace theorem dependence
  The trace theorem applies only to the marked carrier object and not
  to the unmarked shadow.

E125.2 object-existence dependence
  Q(Y_C) is not an underlying object plus metadata; the primitive field
  is required for the object to exist in T_tr.

E125.3 control obstruction
  Epstein/DH cannot carry the same mark because a named axiom fails
  before trace evaluation.

E125.4 downstream dependence
  M_C, F_C, or Tr_L uses the marked primitive field as load-bearing
  object data before evaluation.
```

If one of E125.1-E125.4 is plausible but unproved, record
`HOLD_CARRIER_REFLECTION`, not a pass.

## 5. Fillable Audit

```text
candidate:
envelope Q:
claimed retained field:

mark type:
  label | parameter | grading | metadata | coordinate |
  normalization | post-completion tag | other:

trace theorem:
  applies to unmarked object? YES/NO/UNKNOWN:
  depends on mark? YES/NO/UNKNOWN:

downstream package:
  M_C formable without mark? YES/NO/UNKNOWN:
  F_C formable without mark? YES/NO/UNKNOWN:
  Tr_L formable without mark? YES/NO/UNKNOWN:

control test:
  Epstein can carry same mark? YES/NO/UNKNOWN:
  DH can carry same mark? YES/NO/UNKNOWN:
  exact failed axiom if NO:

verdict:
  REJECT_DECORATED_ENVELOPE_REFLECTION |
  HOLD_CARRIER_REFLECTION |
  ROUTE_TO_DOC122 |
  OUT_OF_SCOPE:
```

## 6. Relation To Existing Docs

```text
doc 109
  Rejects decorated-shadow first maps before Q.

doc 118
  Rejects carrier-forgetting traceable envelopes.

doc 120
  Audits whether Q triggers doc 118.

doc 122
  States the positive carrier-reflecting envelope target.

doc 123
  External packet should use this guard when a reply offers a marked or
  enriched envelope.

doc 126
  Places this guard inside the envelope admission order.
```

## 7. Use Rule

Whenever a proposal says Q retains the carrier field "as a mark,"
"as a grading," "as metadata," or "as a parameter," fill this audit
before crediting CRE122. If the trace theorem and control exclusion do
not depend on that field before evaluation, reject the route as
decorated envelope reflection.
