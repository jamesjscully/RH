# 118 - Traceable envelope collapse no-go

Status: theorem target / broad no-go skeleton, 2026-06-11. This is a
post-doc-103 no-go class. It does not deny that a strict first carrier
map could exist; it rejects routes whose trace theorem becomes legal
only after forgetting the carrier field that made the first map strict.

## 1. Purpose

Docs 103, 109, 111, and 112 handle the first obvious S3 failure modes:

```text
no primitive first map;
decorated-shadow first map;
strict prefix forgotten downstream;
late carrier repair after a shadow trace package.
```

One escape remains. A candidate could name a real strict prefix

```text
S_C --kappa_C--> Y_C
```

but obtain trace legality only by passing from the strict carrier
domain to a traceable envelope:

```text
Q: ECar_L1 -> T_tr.
```

This document isolates the corresponding no-go class.

## 2. Prototype

Let `ECar_L1` be a proposed strict Euler-carrier domain. Suppose:

```text
S_C
  is an object whose primitive data include some carrier field among
  alpha, v, depth, ell, mu_C, Euler factorization, or graph-depth data.

kappa_C: S_C -> Y_C
  consumes at least one primitive carrier field before M_C, F_C, or
  Tr_L exists.

Q: ECar_L1 -> T_tr
  is the envelope or completion used to make traces legal.
```

Examples of `Q` include Morita, localizing, stable, idempotent-complete,
nuclear, trace-class, Hilbert/Banach, liquid-kernel, sheaf, module, or
kernel envelopes. The list is illustrative; the hypothesis is about
what `Q` forgets, not the name of the completion.

## 3. Theorem Skeleton

### TEC118 - Traceable Envelope Collapse

Assume:

```text
H118.1 strict prefix
  S_C and kappa_C are named, and kappa_C consumes primitive
  Euler-carrier data before M_C, F_C, or Tr_L exists.

H118.2 extrinsic trace legality
  Tr_L is not legal on the strict carrier domain itself. Traceability
  is obtained only after applying Q: ECar_L1 -> T_tr.

H118.3 carrier-insensitive trace test
  Dualizability, properness, nuclearity, trace-class status, codomain
  formation, determinant/index formation, or traceability in T_tr is
  certified from Q(Y_C) without using the primitive carrier field as
  object data.

H118.4 Q-determined downstream package
  M_C, F_C, and Tr_L(F_C) are invariant under Q-equivalence, or depend
  only on Q(Y_C) and the induced data in T_tr.

H118.5 control admissibility after Q
  After carrier rigidification is forgotten by Q, the corresponding
  Epstein represented-norm, DH coefficient, measure, kernel, or shadow
  package can form the same typed Q(Y_C) and the same traceability
  certificate.

H118.6 no carrier-reflecting observable
  T_tr contains no additional pre-trace observable, defect,
  coefficient, monodromy, noninvertible structure, or marked object
  data that records the primitive carrier field consumed by kappa_C.
```

Then the candidate has one of two verdicts:

```text
REJECT_TRACE_ILLEGAL
  if Tr_L is used before Q supplies a legal trace theorem;

REJECT_TRACEABLE_ENVELOPE_COLLAPSE
  if Tr_L is legal only after Q, but Q erases the primitive carrier
  field from the downstream traceable package.
```

In the second case, the route also triggers:

```text
S3:
  REJECT_DOWNSTREAM_FORGETFUL or REJECT_CARRIER_OVERREACH.

LT76/A6:
  LT76.6 rejection / NO76.4 carrier overreach.
```

## 4. Proof Plan

The intended proof is a factorization argument.

```text
Step 1.
  By H118.2, any legal trace calculation occurs in T_tr, not directly
  in the strict ECar_L1 carrier domain.

Step 2.
  By H118.3 and H118.4, the traceable package factors through Q(Y_C).
  Therefore two strict prefixes with the same Q(Y_C) have the same
  M_C/F_C/Tr_L data.

Step 3.
  By H118.5, an Epstein/DH/control shadow can form the same typed
  traceable package after Q forgets the carrier rigidification.

Step 4.
  By H118.6, no pre-trace observable inside T_tr reintroduces the
  consumed primitive field. Therefore carrier selectivity is not
  visible to the trace or codomain.

Step 5.
  The strict prefix was real, so this is not doc-109 relabeling and not
  the doc-108 shadow-first case. The failure happens at traceable
  envelope passage: the route is strict enough to exclude controls
  before Q, but traceable only after forgetting the data that excluded
  them.
```

## 5. Relation To Earlier No-Gos

```text
doc 108
  Handles packages formed by shadow-stable operations before primitive
  carrier checking.

doc 109
  Handles first maps that are only labels or decorations on shadow
  data.

doc 111
  Handles strict prefixes whose consumed primitive field is forgotten
  before M_C/F_C/Tr_L.

doc 112
  Handles trace packages formed first, with carrier data added later.

doc 118
  Handles the remaining envelope case: the prefix may be strict, but
  the trace becomes legal only after a carrier-forgetting completion.

doc 120
  Turns this envelope case into a fillable operation audit.
```

Thus doc 118 is not another Epstein example. Epstein/DH are controls
only after the structural hypothesis says the traceable envelope has
forgotten the strict field.

## 6. Escape Clause

To escape TEC118, a future proposal must show that the traceable
passage is carrier-reflective, not carrier-forgetting. It must provide
at least one of:

```text
intrinsic trace legality:
  Tr_L is legal on Y_C as a carrier object before applying a
  carrier-forgetting envelope.

carrier-reflecting Q:
  Q(Y_C) retains the primitive field consumed by kappa_C as object data
  that is detected before trace evaluation.

pre-trace observable:
  T_tr contains a named observable, defect, coefficient, monodromy,
  noninvertible structure, or marked object that distinguishes the
  prime-power carrier from Epstein/DH controls before Tr_L.

control exclusion after Q:
  Epstein/DH cannot form the same Q(Y_C), not merely the original
  strict S_C.
```

Any escape must also preserve:

```text
B0 bank embedding;
same-form M_C;
trace-derived F_C;
zero-free freeze;
doc-71 B1 ledger routing.
```

## 7. Routing Rule

When evaluating a strict proposal, apply doc 118 after doc 103 and
before promoting a trace theorem:

```text
doc 103 FIRST_MAP_PASS
  -> docs 109 and 111 and 112 do not reject
  -> check whether Tr_L is intrinsic or Q-mediated
  -> if Q-mediated, fill doc 120 and apply H118.1-H118.6
  -> only then route to docs 98, 94, 113, and 114.
```

If doc 118 rejects, do not repair by adding carrier labels after Q.
That routes to doc 112.
