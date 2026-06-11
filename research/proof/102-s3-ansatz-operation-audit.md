# 102 - S3 ansatz operation audit

Status: filled operation audit / S3 ledger update, 2026-06-11. This
applies docs 100 and 101 to the A0-A6 ansatz classes from doc 75. It
does not introduce a new ansatz and does not authorize a witness.

## 1. Purpose

Doc 75 classifies natural `K_B1` shapes. Docs 100 and 101 add a new
filter:

```text
If the operation creating M_C, F_C, or Tr_L is available for broad
shadow data before primitive Euler-carrier checking, then Epstein/DH
controls still enter and carrier overreach applies.
```

This document records the current operation-level status of the doc-75
ansatz classes.

## 2. Summary

```text
A0/A0p/A0t
  REJECT_SHADOW. Already doc 74; doc 101 also triggers immediately.

A1 depth-weighted one-place comb
  HOLD_STRICT_EULER only as a primitive-depth input. REJECT_FREE_WEIGHT
  if the weight/form/codomain is supplied externally; TRIGGERS_100 if a
  later mixed object is built by broad shadow operations.

A2 two-place valuation-vector kernel
  HOLD_STRICT_EULER only if the product-formula valuation object is
  primitive before M_C. REJECT_FREE_WEIGHT for chosen B/window; triggers
  doc 100 if the bilinear/codomain package is shadow-stable.

A3 HH graph-index lift
  HOLD_STRICT_EULER only if the graph-index face embeds as strict
  carrier object before trace. REJECT_SHADOW or TRIGGERS_100 if it is
  implemented by max-Gram, theta, determinant, or generic index shadows.

A4 determinant/coker/regularized kernel
  REJECT_FREE_WEIGHT or REJECT_CARRIER_OVERREACH unless the
  determinant/coker object is internal to ECar_L1 after carrier
  verification.

A5 depth-wall stress kernel
  REJECT_FREE_WEIGHT as diagnostic stress unless the stress response is
  trace-derived. If trace-derived through generic kernel/operator
  closure, TRIGGERS_100.

A6 liquid trace ansatz
  HOLD_STRICT_EULER only if the liquid trace theorem is stated on a
  strict ECar_L1 source category. Generic liquid/measure/kernel
  trace-class closure triggers docs 100 and 101.
```

No ansatz advances to B1.

## 3. A0/A0p/A0t

These classes are already rejected by doc 74. Doc 101 gives the
operation reason:

```text
operation creating M_C/F_C:
  measure, theta, Poisson, Fourier, represented-norm, or coefficient
  shadow operation.

doc-100 status:
  TRIGGERS_100.

earliest gate:
  REJECT_SHADOW before doc 100 is needed.
```

Epstein has the required represented-norm and theta/count shadows, so
the construction computes on the control.

## 4. A1 Depth-Weighted One-Place Comb

The primitive depth readout is not itself killed by doc 100:

```text
first carrier-consuming input:
  depth(k) = v(alpha^k) = k.

Epstein status:
  no distinguished atom alpha and no unique tower/depth coordinate.
```

But A1 still lacks the B1 mixed object and same-form codomain.

```text
If w or the codomain is chosen:
  REJECT_FREE_WEIGHT by doc 93.

If M_C is later formed by tensor, sum, completion, pushforward,
kernel, determinant, or trace-class closure on the weighted measure:
  TRIGGERS_100 by doc 101.

If the candidate supplies a trace theorem deriving w and F_C after a
strict first carrier map:
  route to doc 98 as HOLD_STRICT_EULER until SE98.1-SE98.8 are filled.
```

Current verdict:

```text
HOLD_STRICT_EULER for the primitive-depth input only; no witness.
```

## 5. A2 Two-Place Valuation-Vector Kernel

A2 has the same split.

```text
first carrier-consuming input:
  (a,b) in p^a q^b with product-formula constrained valuation data.

Epstein status:
  no unique prime-power valuation vector for represented norms.
```

Operation audit:

```text
chosen B(a,b), W, window, or regularization:
  REJECT_FREE_WEIGHT by doc 93.

bilinear/codomain package defined for lattice, monoid, coefficient,
measure, or determinant shadows:
  TRIGGERS_100 by doc 101.

product-formula valuation object native to ECar_L1 before the bilinear
or trace operation exists:
  route to doc 98.
```

Current verdict:

```text
HOLD_STRICT_EULER only for a future native product-formula object.
```

## 6. A3 HH Graph-Index Lift

A3 remains the most D-side-shaped ansatz, but the operation audit
separates two cases.

```text
strict case:
  HH Frobenius-graph/index face embeds conservatively in ECar_L1 before
  M_C, F_C, or trace exists.

shadow case:
  graph depth is read through max-Gram, theta, determinant, count, or
  generic index/coker data before primitive carrier checking.
```

Verdicts:

```text
strict case:
  HOLD_STRICT_EULER; route to doc 98 and docs 87-91.

shadow case:
  REJECT_SHADOW if it factors through theta/count/max-Gram;
  REJECT_CARRIER_OVERREACH if a trace-derived index exists but follows
  broad shadow functoriality.
```

No current file supplies the strict case.

## 7. A4 Determinant/Coker/Regularized Kernel

Doc 101 makes A4 mostly fail-closed:

```text
determinant/coker built from a shadow-level operator:
  TRIGGERS_100 and usually also doc 93 if the regularization is chosen.

determinant line internal to ECar_L1 after carrier verification:
  possible HOLD_STRICT_EULER, but only if the source operator is
  unavailable for Epstein/DH controls.
```

Current verdict:

```text
REJECT unless the determinant/coker category is named after a strict
carrier-consuming map. No such category is currently written.
```

## 8. A5 Depth-Wall Stress Kernel

Stress is especially vulnerable to free-weight and shadow-stability
failures.

```text
stress rule chosen from deformation, sign, zero agreement, numerical
convenience, or diagnostic behavior:
  REJECT_FREE_WEIGHT by doc 93.

stress response derived from a generic kernel/operator/measure category:
  TRIGGERS_100 by doc 101.

stress response derived inside ECar_L1 after primitive carrier fields
are required:
  HOLD_STRICT_EULER pending doc 98.
```

Current verdict:

```text
HOLD as diagnostic only; no B1 evidence.
```

## 9. A6 Liquid Trace Ansatz

A6 is the best conceptual shape and the easiest place to overclaim.
Doc 101 splits it sharply.

```text
generic liquid/analytic/measure/kernel trace-class closure:
  TRIGGERS_100 if represented-norm, coefficient, or measure shadows are
  legal inputs.

metric or equivariant enrichment of the bare circle:
  route first through docs 81, 82, and 85 for scale retention; then
  through doc 101 if M_C/F_C is formed by shadow-stable operations.

strict liquid ECar_L1 theorem:
  HOLD_STRICT_EULER only if the theorem's source objects require
  primitive alpha, v, depth, ell, mu_C, and Euler factorization before
  traceability or M_C exists.
```

Current verdict:

```text
HOLD_STRICT_EULER only as an external theorem target. Any broad liquid
trace theorem natural for monoid/measure shadows triggers docs 100 and
97.
```

## 10. Consequence For Doc 75

The doc-75 next-work list tightens to:

```text
1. For A1/A2/A3/A6, name the first ECar_L1 object or map that consumes
   primitive carrier fields before M_C, F_C, or Tr_L exists.

2. For A4/A5, do not continue unless determinant/coker/stress formation
   is internal to that strict domain and trace-derived.

3. For any ansatz built by standard tensor, sum, completion,
   pushforward, coend, kernel, correspondence, determinant, cokernel, or
   trace-class closure before carrier checking, record doc-100
   REJECT_CARRIER_OVERREACH rather than building a witness.
```

Thus S3 is still not globally dead, but the remaining positive target is
smaller:

```text
write the doc-103 strict first carrier-consuming map, then return to doc
98 to derive M_C/F_C.
```
