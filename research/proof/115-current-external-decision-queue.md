# 115 - Current external decision queue

Status: operational dispatch queue, 2026-06-11. This collects the
current sendable expert questions after the S3 and LT76 admission
matrices. It is not a new packet and records no external answers.

## 1. Purpose

The active front is no longer "find a promising analogy." The useful
external answers must decide a route:

```text
ADVANCE
  name a theorem/object/map satisfying a local ledger field without
  triggering a known no-go;

KILL
  prove a no-go whose hypotheses cover the proposed route;

SHARPEN
  name the smallest theorem/object/axiom whose resolution would decide
  the route.
```

Everything else lands in doc 61 as DEMOTE or OUT_OF_SCOPE.

## 2. Queue

### Q115.1 LT76 Strict Trace Package

```text
recipient:
  liquid/gaseous analytic geometry, trace-of-kernels, categorical
  trace, condensed analytic experts.

send:
  doc 96 LT76 short message first;
  doc 77 full packet if more context is requested.

decision route:
  doc 61 -> doc 83 -> doc 92 -> doc 114.

ADVANCE if:
  a package (L1, R_L, T_C, b1, Tr_L) is named and local LT76.1-LT76.7
  rows can be scored without docs 105/108/112/118/120 triggering.

KILL if:
  the answer proves NO76.1-NO76.5 for the stated class, especially
  factor-through scale collapse, no real trace package, side-block
  coupling, carrier overreach, or inserted external unit data.

SHARPEN if:
  the answer names a minimal traceability, non-factorization,
  same-form coupling, or carrier-selectivity theorem that would decide
  a row.
```

### Q115.2 S3 Strict First Map

```text
recipient:
  trace/index/kernel, arithmetic topology, noncommutative geometry, or
  categorical experts who can speak about strict source categories and
  first carrier-consuming maps.

send:
  doc 119 current strict-first-map dispatch;
  doc 110 full packet if more context is requested.

decision route:
  doc 61 -> doc 103 -> docs 109/111/112/118 -> doc 113.

ADVANCE if:
  S_C and kappa_C are named; kappa_C consumes primitive carrier fields
  before M_C/F_C/Tr_L; controls cannot form the source/map; the
  consumed field remains load-bearing downstream.

KILL if:
  every candidate first map in the formalism is a relabeled shadow,
  downstream-forgetful strict prefix, late carrier repair, or same
  typed control-formable operation.

SHARPEN if:
  the answer names the exact source-category axiom or first-map theorem
  that would decide whether such S_C and kappa_C exist.
```

### Q115.3 S3 Trace-Derived Codomain

```text
recipient:
  trace, index, kernel, categorical trace, or noncommutative geometry
  experts.

send:
  doc 96 S3 trace-derived short message;
  doc 95 full packet if more context is requested.

decision route:
  doc 61 -> doc 94/doc 98/doc 103 -> doc 113.

ADVANCE if:
  after a valid strict first map, the same trace theorem derives M_C,
  F_C, and the carrier-reading form without free weights, side blocks,
  shadow overreach, downstream erasure, or late repair.

KILL if:
  the answer proves the form/codomain is necessarily shadow-derived,
  externally supplied, side-blocked, trace-illegal, carrier-overbroad,
  downstream-forgetful, or late-reintroduced in the stated class.

SHARPEN if:
  the answer names the minimal trace-derived codomain theorem or
  obstruction.
```

### Q115.4 Broad No-Go Reviewer

```text
recipient:
  a reviewer willing to check the proof skeletons rather than propose
  a construction.

send:
  docs 108, 109, 111, 112, 113, 114, and 118 as the minimal bundle.

decision route:
  doc 61 -> affected local proof doc -> TODO/HANDOFF only if a theorem
  statement changes.

ADVANCE if:
  the reviewer supplies missing hypotheses that make a no-go theorem
  citable.

KILL if:
  the reviewer finds a counterexample to a stated no-go class.

SHARPEN if:
  the reviewer narrows a theorem to a precise ambient category or
  identifies the exact external theorem needed for citation hardening.
```

### Q115.5 Carrier-Reflecting Envelope

```text
recipient:
  experts in categorical trace, Morita/localizing invariants,
  trace-class/nuclear categories, liquid/condensed analysis, kernel
  categories, or marked/enriched envelope formalisms.

send:
  doc 124 priority board first;
  doc 123 carrier-reflecting envelope packet if the prerequisite Q is
  named;
  score replies by doc 128.

decision route:
  doc 61 -> doc 120 -> doc 121 -> doc 122 -> docs 113/114.

ADVANCE if:
  a named Q: ECar_L1 -> T_tr is traceable and carrier-reflecting:
  Q(Y_C) retains the primitive field consumed by kappa_C as pre-trace
  object data, controls cannot form the same Q(Y_C) or satisfy the
  same trace theorem, doc 125 does not trigger, and CRE122.1-CRE122.7
  are supplied.

KILL if:
  the answer proves the named envelope/completion is carrier-forgetting
  for the stated formalism, or only retains carrier data as inert marks
  under doc 125, so doc 118 triggers.

SHARPEN if:
  the answer names the exact marked-object structure, reflection
  invariant, traceability theorem, or control test that would decide
  whether Q is carrier-reflecting.
```

## 3. Non-Decision Replies

Do not update the trajectory for replies that only provide:

```text
general analogy;
ordinary circle traceability without scale retention;
Route A/B0 calibration;
post-trace normalizations;
free weights, codomains, or regularizations;
ordinary traceability without carrier reflection;
zero-side evidence;
encouragement or broad literature lists.
```

Record them in doc 61 as DEMOTE or OUT_OF_SCOPE.

## 4. Current No-Witness Rule

```text
No S3 witness:
  until doc 113 has no rejecting rows and the remaining rows are
  explicit PASS/HOLD records with named missing theorems.

No A6/LT76 witness:
  until doc 114 has local PASS rows for every claimed LT76 clause and
  no doc-105/doc-108/doc-112/doc-118/doc-120 rejection or unresolved
  doc-121 HOLD row.
```

HOLD is not a witness license.

## 5. Relation To Existing Docs

```text
doc 61
  Landing ledger for all external answers.

doc 77, doc 95, doc 96, and doc 110
  The sendable packet/message bank.

doc 119 and doc 123
  Current sendable packets for strict first maps and
  carrier-reflecting envelopes.

doc 124
  Current priority order for choosing which packet to send.

doc 128
  Scoring rubric for carrier-reflecting envelope replies.

doc 113
  Current S3 strict-route matrix.

doc 114
  Current LT76/A6 strict-trace matrix.
```

## 6. Use Rule

Before contacting an expert, choose exactly one queue row and one
packet. After an answer arrives, record it in doc 61 before updating
any proof target, gate, TODO, or HANDOFF text.
