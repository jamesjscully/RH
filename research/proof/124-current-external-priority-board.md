# 124 - Current external priority board

Status: operational priority board / no external answer, 2026-06-11.
This ranks the doc-115 queue after docs 119 and 123. It is not a new
packet and records no expert reply.

## 1. Purpose

Docs 119 and 123 are both sendable, but they are not equally
primitive. The carrier-reflecting envelope question presupposes a
named strict prefix and a named envelope Q. The current board has
neither.

This document records the dependency order so external work stays
falsifiable.

## 2. Priority Order

```text
P124.1 send first, if contacting one expert now
  Q115.2 S3 strict first map using doc 119.

P124.2 send only after a plausible Q is named
  Q115.5 carrier-reflecting envelope using doc 123.

P124.3 send after S_C/kappa_C or Q movement
  Q115.3 S3 trace-derived codomain using doc 95/doc 96.

P124.4 send when the recipient is specifically LT76/liquid trace
  Q115.1 LT76 strict trace package using doc 96/doc 77.

P124.5 send to proof reviewers, not constructors
  Q115.4 broad no-go reviewer.
```

## 3. Dependency Board

```text
doc 119 strict first-map dispatch
  prerequisites:
    none beyond the current S3 route.
  useful answer:
    names or kills S_C/kappa_C.
  current priority:
    FIRST.

doc 123 carrier-reflecting envelope packet
  prerequisites:
    named S_C/kappa_C and a named Q: ECar_L1 -> T_tr.
  useful answer:
    proves Q is carrier-reflecting, proves Q is carrier-forgetting, or
    names the exact reflection invariant.
  current priority:
    CONDITIONAL.

doc 95/doc 96 S3 trace-derived codomain packet
  prerequisites:
    at least a plausible strict first map and no docs 109/111/112/118
    rejection.
  useful answer:
    derives or kills M_C/F_C/trace-derived form.
  current priority:
    SECOND AFTER STRICT PREFIX MOVEMENT.

doc 77/doc 96 LT76 strict trace packet
  prerequisites:
    recipient can speak to liquid/gaseous trace packages directly.
  useful answer:
    moves LT76.1-LT76.7 or NO76.1-NO76.5.
  current priority:
    PARALLEL SPECIALIST.

doc 108/109/111/112/118 no-go reviewer bundle
  prerequisites:
    reviewer agrees to check proof skeletons rather than propose a
    construction.
  useful answer:
    sharpens or refutes a broad no-go.
  current priority:
    PARALLEL REVIEW.
```

## 4. Current Recommendation

If exactly one external message is sent now, send doc 119:

```text
reason:
  The current board has no FIRST_MAP_PASS. Without S_C and kappa_C,
  envelope reflection, trace-derived codomain, and B1 routing are all
  downstream.

expected landing:
  doc 61 -> doc 103 -> docs 109/111/112/118 -> doc 113.
```

Do not send doc 123 as the first contact unless the recipient already
has a concrete Q in mind. Without Q, the answer is likely to become an
ordinary traceability survey and should land as DEMOTE or OUT_OF_SCOPE.

## 5. Relation To Existing Docs

```text
doc 61
  Landing ledger for any answer.

doc 115
  Full current external decision queue.

doc 119
  Current strict-first-map dispatch.

doc 123
  Carrier-reflecting envelope packet.

doc 128
  Response-scoring rubric for doc 123.

doc 116
  Current B1 admission board; no witness is licensed.
```

## 6. Use Rule

Before sending an external message, choose one queue item from doc 115
and check it against this priority board. If the prerequisite is not
met, send the earlier prerequisite packet instead or record why the
recipient is an exception.
