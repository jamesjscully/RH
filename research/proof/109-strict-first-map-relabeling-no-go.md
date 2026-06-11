# 109 - Strict first-map relabeling no-go

Status: bounded no-go / doc-103 hardening, 2026-06-11. This rejects
the cheapest false way to fill the doc-103 first-map record: attach
Euler-carrier labels to shadow data and call the resulting labeled
object a strict carrier source.

## 1. Purpose

Doc 103 requires a first primitive carrier-consuming map:

```text
S_C -> Y_C
```

before `M_C`, `F_C`, or `Tr_L` exists. A future proposal might try to
satisfy this by taking a shadow object, adding labels such as
`alpha`, `v`, `depth`, or `ell`, and then applying an operation that is
still functorial after the labels are forgotten.

This document proves that such a labeled-shadow first map does not
escape docs 100-108. It is not a rejection of genuinely strict
`ECar_L1` source categories.

## 2. Relabeling Hypotheses

Let a proposed S3 first-map record name:

```text
S_C -> Y_C
```

Say it is a relabeling first map if all of the following hold.

```text
H109.1 shadow base
  There is a shadow object S_sh in a category of represented-norm
  monoids, commutative monoids, positive multisets, coefficient
  shadows, measures, kernels, determinant/coker data, or theta/count
  data.

H109.2 labeled source
  S_C is obtained from S_sh by adding labels, chosen coordinates,
  windows, weights, valuation names, depth names, distinguished atoms,
  normalizations, or regularization choices.

H109.3 forgetful operation
  The proposed first map kappa_C: S_C -> Y_C is preserved, reflected,
  or detected after forgetting the labels to S_sh, or the operation
  defining Y_C exists on the shadow category before the labels are
  checked.

H109.4 no primitive consumption
  The proof that kappa_C exists does not require alpha, v, depth, ell,
  mu_C, Euler factorization, or graph-depth data as primitive object
  data. Those fields are read as parameters, decorations, coordinates,
  or post hoc restrictions.

H109.5 same later package
  The later construction of M_C, F_C, or Tr_L uses the same shadow
  operation, or the same externally supplied form, after kappa_C.

H109.6 control formability
  Epstein or DH controls can form the same decorated source and the
  same typed map after carrying the same decoration scheme. One valid
  control branch is enough, but the record must state which branch is
  being used.

H109.7 late failure only
  Any control failure occurs only after signs, positivity,
  regularization, zero comparison, or post-selection.
```

These hypotheses intentionally describe a failure mode, not every
possible strict source. A proposal escapes this no-go by showing the
source category itself makes Epstein/DH controls non-objects before
the first map can be written.

## 3. Lemma

### Lemma 109.1

Any first-map record satisfying H109.1-H109.5 fails the doc-103
`FIRST_MAP_PASS` criterion and routes to the earlier shadow/free-weight
gates.

Verdict:

```text
REJECT_RELABELING
  if S_C is a decorated shadow and kappa_C consumes no primitive
  carrier field.

REJECT_DECORATED_SHADOW_STABLE
  if kappa_C or Y_C is still available for represented-norm, measure,
  coefficient, determinant, or trace-class shadows.

REJECT_FREE_WEIGHT
  if the carrier-sensitive part is supplied by chosen weights, windows,
  bilinear forms, stress parameters, determinant presentations, or
  codomains.

REJECT_CONTROL_FORMABLE
  if the selected Epstein or DH control can form the same decorated
  S_C and kappa_C.

ROUTE_TO_DOC103
  if a genuinely primitive first carrier-consuming map is named.
```

### Proof

Doc 103 requires the first map to consume primitive Euler-carrier fields
before any mixed object, codomain, or traceable object exists.

Under H109.1-H109.3, the proposed first map is a map of labeled shadow
data whose existence is detected after forgetting the labels, or whose
target is created by an operation already available for the shadow
category. Under H109.4, the labels are not primitive object data needed
for the existence of the map. They are parameters or decorations.

Therefore the first operation has not crossed the doc-103 boundary. It
has not produced a source object or map whose definition is structurally
unavailable for represented-norm, monoid, measure, coefficient, or
theta/count controls.

If the later package uses the same shadow operation, H109.5 puts the
proposal under docs 100, 101, 107, and 108. Under H109.6, the selected
control forms the same decorated source and same typed map, so the
doc-87 carrier death has not occurred. Under H109.7, any control
failure is too late to repair carrier selectivity. If the later package reads
the labels through a supplied form, weight, window, determinant wrapper,
or codomain, it is the doc-93 free-weight case. In neither branch does
`S_C -> Y_C` satisfy `FIRST_MAP_PASS`.

Thus a relabeling first map cannot move S3 out of `HOLD`. QED.

## 4. Decision Test

For any proposed doc-103 record, ask:

```text
F109.1
  If the labels alpha/v/depth/ell/mu_C/Euler-factorization are erased,
  does the map or target operation still exist?

F109.2
  Is the alleged primitive field used to define the source category and
  map, or only to parameterize a weight, coordinate, window, or
  codomain?

F109.3
  Can the same operation be applied to represented-norm, measure,
  coefficient, determinant/coker, or theta/count shadows?

F109.4
  Does the later M_C/F_C/Tr_L construction depend on the same
  shadow-stable operation?

F109.5
  If the answer to F109.1-F109.4 is no, what exact axiom makes
  Epstein/DH controls fail before kappa_C exists?
```

If F109.1, F109.2-as-parameter, F109.3, or F109.4 is yes, route to the
matching rejection above. Only F109.5 can return the proposal to the
strict doc-103/doc-98 path.

Do not use this test to claim that labels are never primitive. A label
can be primitive if the source category proves it is object data and
kappa_C consumes it before any shadow-stable operation creates
`M_C`, `F_C`, or `Tr_L`.

## 5. Covered Patterns

The no-go covers:

```text
depth labels on a one-place comb with a chosen weight;
valuation-vector coordinates with a chosen bilinear form or window;
graph-depth names read by a generic determinant, coker, index, or Gram
package;
liquid or measure kernels whose carrier fields enter as parameters
after a broad trace input has already been formed;
regularization choices that make the target look carrier-sensitive
after the shadow object has already been accepted.
```

These are broad classes, not new examples.

## 6. Non-Coverage

This no-go does not apply when a proposal supplies:

```text
1. a source category whose objects require primitive carrier fields
   before any shadow-stable operation;
2. a first map whose definition consumes one of those fields;
3. a proof that Epstein/DH controls are not source objects or cannot
   form that map;
4. a conservative B0 bank embedding for the source;
5. zero-free freeze before first zero contact.
```

That proposal remains governed by doc 103, then docs 111/112 and doc
98. Doc 109 only prevents decorated shadow objects from being counted
as strict first carrier sources.

## 7. Relation To Existing Docs

```text
doc 93
  Rejects externally supplied weights, forms, windows, stresses,
  determinant presentations, regularizations, and codomains.

doc 100 and doc 101
  Reject mixed-object and operation formation that is shadow-stable
  before primitive carrier checking.

doc 103
  Gives the first-map record whose cheap relabeling failure is rejected
  here.

doc 104
  Records that no current S3 ansatz has FIRST_MAP_PASS.

doc 107 and doc 108
  Supply the shared carrier-overreach theorem skeleton for same typed
  shadow constructions.
```

## 8. Use Rule

Use doc 109 before promoting a doc-103 first-map record. If the record
only labels an existing shadow object, cite this no-go and route to
docs 93, 100, 101, 107, or 108 as appropriate.

Do not use doc 109 to reject a source category that is genuinely
defined by primitive Euler-carrier object data before the first map.
That is the live strict route, and it must be scored by docs 103 and
98.
