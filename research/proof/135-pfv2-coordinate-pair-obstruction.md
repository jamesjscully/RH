# 135 - PFV2 coordinate-pair obstruction

Status: bounded candidate-driven no-go / Q134.1 internal result,
2026-06-11. This attacks PFV2-FIRST after doc 130. It does not kill
all A2/S3 routes. It kills the cheap coordinate-pair realization of
PFV2 and leaves only a genuinely structural product-formula source
category live.

## 1. Purpose

Doc 130 named:

```text
PFV2-FIRST
```

as the missing theorem for the A2 two-place valuation-vector route.
This document applies docs 109 and 108 to the first obvious internal
attempt:

```text
take B0_p x B0_q;
attach labels alpha_p, alpha_q, v_p, v_q, ell_p, ell_q;
impose a product-formula relation PF;
call the resulting relation the first carrier-consuming map.
```

That attempt is not strict. It is a labeled coordinate-pair shadow.

## 2. Covered Class

Call an A2 proposal `PFV2_coord` if it satisfies all of:

```text
C135.1 product of B0 records
  The source is built from B0_p x B0_q, or from two one-place comb/
  count/RR records, before a new source category is defined.

C135.2 coordinate labels
  alpha_p, alpha_q, v_p, v_q, ell_p, ell_q, and PF are labels,
  coordinates, equations, weights, or normalization choices attached
  to that product.

C135.3 relation-first map
  The proposed kappa_PF is the operation of imposing, reading, or
  evaluating the product-formula relation on those coordinates.

C135.4 no source-category exclusion
  The proof that the source and relation exist does not first define a
  category whose objects require free rank-one Euler valuation towers
  and reject represented-norm controls as non-objects.

C135.5 shadow-stable operation
  If the labels are erased or replaced by arbitrary marked
  irreducibles/lengths in a commutative-monoid, represented-norm,
  measure, or count shadow, the same typed relation/evaluation remains
  meaningful.

C135.6 late control failure
  Epstein/DH controls fail only because the chosen labels no longer
  have the intended arithmetic interpretation, or because a later sign,
  trace, regularization, positivity, or comparison test rejects them.
```

This covered class includes:

```text
two-place kernels with chosen valuation-vector coordinates;
bilinear forms or windows on (ell_p, ell_q);
product-formula constraints imposed on labeled B0_p x B0_q data;
determinant/cokernel packages using the two labels as parameters;
trace packages where the two-place field is added after a broad
product or kernel input is already available.
```

## 3. Lemma

### Lemma 135.1

Every `PFV2_coord` proposal fails doc-103 `FIRST_MAP_PASS`.

Verdict:

```text
REJECT_RELABELING
  if kappa_PF is only a relation on labeled B0_p x B0_q shadow data.

REJECT_DECORATED_SHADOW_STABLE
  if the relation/evaluation remains typed after forgetting the Euler
  labels or replacing them by marked shadow data.

REJECT_CONTROL_FORMABLE
  if Epstein/DH controls can carry the same decoration scheme and form
  the same relation before a later test rejects them.
```

### Proof

Doc 103 requires a first map whose definition consumes primitive
Euler-carrier fields before any mixed object, kernel, codomain,
determinant, trace, or shadow-stable operation exists.

Under C135.1-C135.3, the proposed source and map are made from the
product of already banked one-place records plus labels and a relation.
The product construction is already available before a new strict
Euler-carrier category is supplied. Under C135.4, no source-category
axiom makes represented-norm or DH controls non-objects before the map.

By C135.5, the typed operation survives in the shadow category after
erasing or replacing the Euler labels. Therefore doc 109 applies:
the map is a labeled-shadow first map, not primitive carrier
consumption.

For the Epstein branch, doc 64 supplies the control profile. The
represented-norm shadow for

```text
Q(x,y) = x^2 + 5y^2
```

has theta/count data but no free prime-power valuation tower:

```text
36 = 4*9 = 6*6.
```

If `PFV2_coord` accepts arbitrary marked irreducibles, lengths,
coordinate labels, or represented-norm atoms, then the Epstein control
can carry the same decoration scheme and form the same typed relation.
Its failure is only the intended Euler interpretation of those labels,
which is exactly what C135.4 failed to make object-defining. If the
control is rejected later by sign, trace, regularization, positivity,
or comparison, C135.6 makes the failure too late for carrier
selectivity.

Thus the coordinate-pair construction fails `FIRST_MAP_PASS`. QED.

## 4. Consequence For PFV2-FIRST

PFV2-FIRST is narrowed.

The following no longer count as live A2 construction work:

```text
B0_p x B0_q with valuation labels;
chosen two-place valuation vectors;
externally imposed product-formula equations;
bilinear/window/kernel formulas on (log p, log q);
determinant or trace packages using those coordinates after a product
source already exists.
```

The only live A2 escape is:

```text
PFV2-STRUCTURAL.
There exists a category or subcategory ECar_L1^PFV2 whose objects
require a two-place product-formula valuation source as primitive
object data, and whose first map kappa_PF is undefined for
represented-norm/DH controls before labels, kernels, traces, signs,
or comparisons are considered.
```

This is stronger than doc 130's initial wording. It requires the
product-formula valuation pair to be source-defining, not merely
recorded on a product of one-place data.

## 5. Updated Landing For Q134.1

Current Q134.1 status:

```text
PFV2-FIRST:
  SHARPEN.
```

The sharpened target is:

```text
PFV2-STRUCTURAL.
```

Answer landing:

```text
PASS:
  Name ECar_L1^PFV2 and kappa_PF with source-defining product-formula
  valuation data. Prove Epstein/DH are non-objects or cannot form
  kappa_PF before any shadow-stable operation.

KILL:
  Prove every PFV2-STRUCTURAL attempt collapses to PFV2_coord,
  broad product/kernel operation, control-formable source, downstream
  forgetfulness, or bank replacement.

SHARPEN:
  Name the exact axiom, product-formula theorem, or category of
  objects that decides whether PFV2-STRUCTURAL exists.
```

## 6. What This Does Not Kill

This no-go does not kill a proposal that supplies all of:

```text
1. a source category whose objects require a two-place
   product-formula valuation field;
2. a first map whose existence depends on that field;
3. a proof that Epstein/DH controls are not objects or cannot form the
   map before any relation-on-labels construction;
4. conservative B0 bank embedding;
5. downstream dependence through M_C/F_C/Tr_L;
6. zero-free freeze.
```

Such a proposal returns to doc 103 and doc 130 as a candidate
`FIRST_MAP_PASS` attempt.

## 7. Witness Rule

No witness is licensed.

The coordinate-pair failure is formal: it is a doc-109 relabeling
failure, not a boundary phenomenon that needs numerical testing.

A witness could become meaningful only after PFV2-STRUCTURAL names a
concrete source category and map, so that formability under Epstein/DH
is a deterministic structural test rather than a label audit.

## 8. Board Update

```text
A2/S3:
  PFV2_coord rejected.
  PFV2-FIRST sharpened to PFV2-STRUCTURAL.
  A2 remains HOLD_STRICT_ROUTE.
  No A2 witness licensed.
```

## 9. Relation To Existing Docs

```text
doc 64
  Supplies the Epstein represented-norm control and tower-address
  failure.

doc 109
  Supplies the relabeling/decorated-shadow no-go used here.

doc 130
  Named PFV2-FIRST. Doc 135 sharpens it to PFV2-STRUCTURAL.

doc 134
  Follow-up board. Q134.1 should now dispatch PFV2-STRUCTURAL, not the
  weaker coordinate-pair target.
```
