# 130 - A2 strict first-map assault

Status: candidate shot / doc-103 route record, 2026-06-11. This is the
first row attack promised by doc 129. It is not a B1 construction, not
a witness license, and not a proof that the A2 route survives.

## 1. Purpose

Doc 117 recorded the smallest post-B0 calibration:

```text
C117(A2) =
  two B0 one-place records plus an intended two-place valuation-vector
  source and product-formula constraint.
```

Doc 129 says the next step is to attack that row directly. The useful
question is not whether one can write a two-place kernel. The useful
question is:

```text
Can a strict source S_C and first carrier-consuming map kappa_C be
named before any mixed object, codomain, determinant, kernel, or trace
package exists?
```

This document names the smallest candidate package and records the
current verdict.

## 2. Candidate Shot

Name:

```text
PFV2(A_p,A_q)
```

Intended meaning:

```text
product-formula valuation-pair source built from two B0 prime carriers
A_p and A_q.
```

Primitive fields intended before maps:

```text
alpha_p, alpha_q
  distinguished prime-power carrier atoms inherited from the B0_p and
  B0_q comb records.

v_p, v_q
  rank-one valuation/tower coordinates attached to alpha_p and
  alpha_q.

ell_p, ell_q
  log-address fields ell_p=log p and ell_q=log q retained as
  structural length data, not post-trace normalization.

d_p, d_q
  carrier-depth or graph-depth coordinates, if the HH/index lift is
  later claimed.

PF
  a product-formula constraint tying the two valuation towers before a
  kernel or trace is formed.
```

The intended strict source is:

```text
S_C = (A_p, A_q, alpha_p, alpha_q, v_p, v_q,
       ell_p, ell_q, PF)
```

inside a still-unnamed subcategory:

```text
ECar_L1^PFV2 subset L1.
```

## 3. First Map Attempt

The intended first carrier-consuming map is:

```text
kappa_PF: S_C -> Y_PF
```

where `kappa_PF` consumes the product-formula valuation vector:

```text
(v_p, v_q; ell_p, ell_q; PF)
```

before any of:

```text
M_C;
F_C;
Tr_L;
kernel;
bilinear form;
determinant;
cokernel;
completion;
trace-class closure;
regularization.
```

The positive theorem needed is:

```text
PFV2-FIRST.
There exists a category or subcategory ECar_L1^PFV2 and a map
kappa_PF such that:

1. S_C is an object whose primitive fields are object data;
2. kappa_PF is defined before every shadow-stable operation listed
   above;
3. kappa_PF consumes the product-formula valuation vector;
4. B0_p and B0_q embed conservatively;
5. Epstein/DH controls retain theta/count shadows but cannot form
   S_C or kappa_PF for a structural reason before signs, positivity,
   regularization, trace, or zero comparison.
```

## 4. Filled Doc-103 Record

```text
candidate:
  PFV2(A_p,A_q) product-formula valuation-pair source

ansatz class:
  A2 two-place valuation-vector kernel, before kernel formation

source theorem:
  PFV2-FIRST, not currently banked

ECar_L1 source:
  category/subcategory:
    ECar_L1^PFV2, not currently constructed.
  object S_C:
    intended PFV2(A_p,A_q).
  primitive fields present before maps:
    alpha_p, alpha_q, v_p, v_q, ell_p, ell_q, PF.
  proof these are object data, not labels:
    absent. This is the first missing theorem.

first carrier-consuming map:
  name kappa_C:
    kappa_PF.
  source:
    S_C.
  target:
    Y_PF, not currently constructed.
  exact primitive field consumed first:
    product-formula valuation vector (v_p, v_q; ell_p, ell_q; PF).
  why kappa_C is before M_C/F_C/Tr_L:
    by intended construction order, not yet theorem.
  proof before M_C? NO.
  proof before F_C? NO.
  proof before Tr_L? NO.
  operation type:
    strict carrier constraint, not kernel/determinant/trace operation.
  functoriality domain:
    unknown; must not include represented-norm or DH shadow data.

operation audit before kappa_C:
  tensor/product used before first map? NO by intention, not theorem.
  sum/completion/pushforward/coend used before first map? NO by
    intention, not theorem.
  kernel/correspondence/determinant/cokernel used before first map? NO.
  trace-class closure used before first map? NO.
  doc100/doc101 escape reason:
    conditional on proving ECar_L1^PFV2 and kappa_PF independently of
    the later mixed object or trace package.

B0 bank embedding before kappa_C:
  p^Z comb preserved:
    intended from B0_p and B0_q.
  q/log p address preserved:
    intended for each prime-place record.
  Count0/RR layer preserved:
    intended, not proved in ECar_L1^PFV2.
  graph-depth data preserved, if claimed:
    not claimed in this A2 shot.
  Epstein guard preserved as control test:
    YES as a required control branch, not as a passed exclusion.

control exclusion at kappa_C:
  Epstein represented-norm shadow exists? YES.
  Epstein S_C object? UNKNOWN.
  Epstein kappa_C formable? UNKNOWN.
  exact failed field or axiom:
    expected failure: no distinguished free rank-one Euler valuation
    pair with log-address fields and PF as object data. Not proved.
  DH shadow exists? YES.
  DH S_C object? UNKNOWN.
  DH kappa_C formable? UNKNOWN.
  exact failed field or axiom:
    expected failure: no primitive Euler-product carrier object. Not
    proved.

post-kappa construction:
  M_C operation:
    not written.
  F_C operation:
    not written.
  trace theorem:
    not written.
  why docs 100-102 do not apply:
    not yet established; depends on PFV2-FIRST.

downstream obligations, not yet promotion:
  trace legality still needed:
    YES.
  conservative B0 bank embedding still needed:
    YES.
  same mixed M_C still needed:
    YES.
  trace-derived F_C still needed:
    YES.
  zero-free freeze still needed:
    YES.

freeze:
  S_C frozen before zero contact:
    PARTIAL as a formal record; no zero contact made.
  kappa_C frozen before zero contact:
    NO, because kappa_PF is not constructed.
  control exclusions frozen before zero contact:
    NO, because exclusions are unknown.
  first zero contact:
    none.

verdict:
  FIRST_MAP_HOLD.
```

## 5. Decision

The A2 shot does not pass today. It also should not be rejected today.

Reason:

```text
The candidate names the right first missing object and map, but the
source theorem PFV2-FIRST is absent. The control exclusion is expected
but not proved. Therefore the correct status is FIRST_MAP_HOLD.
```

This is progress over doc 117 because the missing theorem is now
explicit:

```text
PFV2-FIRST decides whether A2 is a real strict first-map route or only
decorated two-place B0 shadow data.
```

## 6. What Would Advance A2

A2 advances only if a future answer supplies all of:

```text
ADV-A2.1
  A named category or subcategory ECar_L1^PFV2.

ADV-A2.2
  A theorem that S_C carries alpha_p, alpha_q, v_p, v_q, ell_p,
  ell_q, and PF as object data.

ADV-A2.3
  A map kappa_PF defined before all mixed-object, trace, determinant,
  kernel, completion, or regularization operations.

ADV-A2.4
  A proof that Epstein/DH controls cannot form S_C or kappa_PF, while
  their theta/count shadows remain meaningful.

ADV-A2.5
  A proof that the consumed product-formula valuation field remains
  load-bearing downstream in M_C, F_C, or Tr_L rather than being
  forgotten before trace legality is obtained.
```

If ADV-A2.1-ADV-A2.5 are supplied, update doc 103 to
`FIRST_MAP_PASS`, then route to docs 98, 94, 111, 112, 113, 118, 120,
and 126. Do not infer B1 admission.

## 7. What Would Kill A2

A2 should be rejected if one proves any of:

```text
KILL-A2.1 decorated shadow
  Every PFV2-style source is only B0_p x B0_q shadow data with labels
  alpha, v, ell, or PF attached externally.

KILL-A2.2 broad product operation
  Every construction of kappa_PF uses tensor/product/kernel/
  determinant/trace-class closure before primitive carrier checking.

KILL-A2.3 control formability
  Any theorem creating S_C and kappa_PF also applies to Epstein
  represented-norm or DH coefficient/measure shadows.

KILL-A2.4 downstream forgetfulness
  The product-formula valuation field can be consumed first, but every
  trace-legal M_C/F_C/Tr_L package forgets it before evaluation.

KILL-A2.5 bank replacement
  The two B0 one-place records cannot embed into ECar_L1^PFV2 without
  replacing the comb/address/count/guard data by a parallel shadow.
```

These are the only currently licensed A2 no-go targets. A narrower
failed formula should be recorded as local failure, not a new gate.

## 8. Witness Rule

No A2 numerical or symbolic witness is licensed from this record.

A witness becomes meaningful only after one of:

```text
W-A2.1 deletion/control witness
  PFV2-FIRST supplies enough structure to test whether deleting the
  primitive valuation pair or replacing it by an Epstein/DH control
  changes formability before trace.

W-A2.2 downstream-dependence witness
  A concrete M_C/F_C/Tr_L is written after kappa_PF and the question is
  whether the consumed PFV2 field remains load-bearing.

W-A2.3 calibration witness
  A failed but theorem-shaped PFV2 attempt exposes a boundary worth
  recording without promotion.
```

Free two-place kernel scans remain disallowed.

## 9. Next Action

The next useful work is one of:

```text
1. Ask the doc-110 strict-first-map question with PFV2-FIRST as the
   named formalism/theorem target.

2. Try internally to prove KILL-A2.1 or KILL-A2.3 for PFV2-style
   sources under a precise functoriality hypothesis.

3. Draft a candidate ECar_L1^PFV2 construction from a real liquid or
   analytic category and immediately run the control-formability test.
```

The preferred next action is 1 unless a concrete construction theorem
for ECar_L1^PFV2 is already available.

## 10. Relation To The Board

```text
doc 117
  Previous A2 calibration record. Doc 130 sharpens its missing theorem.

doc 129
  Candidate-driven operating ledger. This document is the first A2 row
  attack.

doc 103
  Supplies the first-map record. Doc 130 fills it with FIRST_MAP_HOLD.

doc 113
  Routes the S3 strict route. A2 remains HOLD_STRICT_ROUTE.

doc 116
  Current B1 board. No witness license changes.
```

Current board update:

```text
A2/S3:
  still HOLD_STRICT_ROUTE;
  missing theorem now named PFV2-FIRST;
  no B1 witness licensed.
```
