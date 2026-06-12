# 136 - LCT broad trace obstruction

Status: bounded candidate-driven no-go / Q134.2 internal result,
2026-06-11. This attacks LCT-FIRST after doc 131. It does not kill all
liquid trace routes. It kills the broad trace-class circle realization
and leaves only strict carrier-consuming trace packages live.

## 1. Purpose

Doc 131 split A6/LT76 into:

```text
LTC_broad(T_p)
  ordinary broad liquid/analytic/trace-class circle package;

LCT_strict(C)
  strict carrier-consuming trace package.
```

This document records the internal no-go for the broad side. It is an
application of docs 105, 108, 118, and 120, not a new global theorem.

## 2. Covered Class

Call an A6/LT76 proposal `LTC_broad` if it satisfies all of:

```text
B136.1 broad trace theorem
  The trace/properness/nuclearity/trace-class theorem is stated for
  positive measures, coefficient shadows, represented-norm monoids,
  ordinary kernels, Hilbert/Banach trace-class operators, sheaves,
  modules, determinants, cokernels, or localizing invariants before
  primitive Euler-carrier fields are required.

B136.2 broad mixed object
  The object coupling b1(comb_C) to R_L/T_C is formed by tensor, sum,
  completion, pushforward, coend, kernel, correspondence, determinant,
  cokernel, trace-class closure, or localizing-invariant operations in
  that broad input class.

B136.3 no strict first map
  No map before M_C or Tr_L requires alpha, v, depth, ell, mu_C, or
  Euler-product factorization as primitive object data.

B136.4 control substitution
  Epstein represented-norm shadows or DH coefficient/measure shadows
  can be substituted into the same trace input type.

B136.5 late failure only
  Controls fail only after signs, positivity, regularization, trace
  evaluation, comparison, post-selection, or zero-side contact.
```

This class includes:

```text
ordinary trace-class kernels on T_p;
measure/correspondence traces natural for positive measures;
Hilbert/Banach trace packages depending only on metric circle data;
determinant/cokernel traces formed from shadow input;
liquid or condensed sheaf/module completions that do not retain
primitive carrier fields before trace.
```

## 3. Lemma

### Lemma 136.1

Every `LTC_broad` proposal fails LT76.6 carrier selectivity and cannot
advance A6/B1.

Verdict:

```text
REJECT_CARRIER_OVERREACH
  if the broad package accepts Epstein/DH controls in the same trace
  input type.

REJECT_A1
  if the package sees only the bare scale-blind circle or inserts log p
  after trace.

REJECT_TRACEABLE_ENVELOPE_COLLAPSE
  if trace legality is obtained only after a carrier-forgetting
  completion or envelope.
```

### Proof

Under B136.1-B136.2, the trace input and mixed object are created by
broad operations before primitive carrier checking. Under B136.3, there
is no earlier source or map requiring Euler-carrier fields as object
data. Under B136.4, the same trace input type accepts an Epstein
represented-norm shadow or a DH coefficient/measure shadow.

Therefore the same construction forms:

```text
control shadow -> M_control -> Tr_L(M_control)
```

before any carrier/effectivity death occurs. This is exactly doc 105:
LT76.6 fails by carrier overreach. Doc 108 supplies the shared proof
skeleton, and doc 64 supplies the concrete Epstein control profile:
theta/count survives, but free prime-power valuation/tower address
fails.

If the broad package also factors through bare circle/localizing data,
docs 81, 82, and 85 classify it as scale collapse. If trace legality is
obtained only through an envelope that forgets the strict carrier
field, docs 118 and 120 classify it as traceable-envelope collapse.

Thus `LTC_broad` is not a live B1 candidate. QED.

## 4. Consequence For LCT-FIRST

LCT-FIRST is narrowed.

The following no longer count as live A6 construction work:

```text
ordinary trace-class kernels on metric T_p;
generic measure/operator/correspondence traces;
localizing or sheaf/module completions that see only broad shadows;
determinant/cokernel trace packages formed before carrier checking;
trace packages where carrier fields are labels added after closure.
```

The live target is:

```text
LCT-STRICT.
There exists L1 with internal R_L and T_C, and a strict trace domain
ECarTr_L1 with source S_C and first map kappa_L, such that primitive
carrier fields (A, alpha, v, depth, ell, mu_C) are required before
M_C, F_C, or Tr_L exists.
```

Trace legality for LCT-STRICT must be one of:

```text
intrinsic:
  Tr_L is legal directly on the strict carrier object; or

carrier-reflecting envelope:
  any Q: ECarTr_L1 -> T_tr used to obtain traceability retains the
  primitive carrier field as pre-trace object data and excludes
  Epstein/DH after Q.
```

Carrier-forgetting envelopes are already routed to docs 118 and 120.

## 5. Updated Landing For Q134.2

Current Q134.2 status:

```text
LCT-FIRST:
  SHARPEN.
```

The sharpened target is:

```text
LCT-STRICT.
```

Answer landing:

```text
PASS:
  Name L1, ECarTr_L1, S_C, kappa_L, M_C, F_C, and Tr_L. Prove trace
  legality is intrinsic or carrier-reflecting, and prove Epstein/DH
  fail before broad trace closure.

KILL:
  Prove every LCT-STRICT attempt either lacks trace legality, requires
  carrier-forgetting envelope passage, overreaches to controls, loses
  bank embedding, or cannot form one same-form M_C.

SHARPEN:
  Name the exact traceability, properness, nuclearity, carrier
  reflection, or strict-domain theorem that decides LCT-STRICT.
```

## 6. What This Does Not Kill

This no-go does not cover a proposal that supplies:

```text
1. a strict carrier-consuming source before trace closure;
2. a trace theorem intrinsic to that source, or a carrier-reflecting
   envelope;
3. conservative B0 bank embedding;
4. one same-form M_C receiving bank and continuum before evaluation;
5. a trace-derived F_C;
6. Epstein/DH exclusion before trace, signs, or zero comparison;
7. zero-free freeze.
```

Such a proposal returns to docs 76, 92, 114, 118, 120, 122, and 126 as
a strict A6 candidate.

## 7. Witness Rule

No witness is licensed.

The broad trace failure is formal. A witness becomes meaningful only
after LCT-STRICT names a concrete strict trace domain and the question
is whether scale deletion or control substitution changes formability
before trace.

## 8. Board Update

```text
A6/LT76:
  LTC_broad rejected under B136.1-B136.5.
  LCT-FIRST sharpened to LCT-STRICT.
  A6 remains HOLD_LT76_STRICT.
  No A6 witness licensed.
```

## 9. Relation To Existing Docs

```text
doc 105
  Supplies the LT76 trace-operation overreach audit instantiated here.

doc 118 and doc 120
  Supply the carrier-forgetting envelope rejection.

doc 131
  Split broad and strict A6 attempts. Doc 136 rejects the broad side.

doc 134
  Follow-up board. Q134.2 should now dispatch LCT-STRICT, not a broad
  trace-class liquid circle question.
```

## 10. Post-doc-144 Escape Clause

Doc 144 makes the immediate live escape:

```text
LCT-STRICT-SRC0(alpha).
```

Do not write another broad trace no-go unless a named strict-domain
class fails by theorem. The next LCT work should decide whether
S_alpha and kappa_L can exist before trace closure, then ask
LCT-STRICT-REFLECT only if source formability survives.
