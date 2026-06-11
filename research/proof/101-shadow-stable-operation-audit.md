# 101 - Shadow-stable operation audit

Status: operational audit / S3 no-go router, 2026-06-11. This records
which common mixed-object operations fall under doc 100 when they are
performed before primitive Euler-carrier checking. It is not a global
impossibility theorem.

## 1. Purpose

Doc 100 proves:

```text
If M_C, F_C, and the trace are functorial in broad shadow data before
primitive carrier checking, then Epstein/DH controls still enter and
doc 97 carrier overreach applies.
```

This document turns that conditional lemma into an audit for proposed
S3 constructions. Its question is:

```text
Does the operation that creates M_C require ECar_L1 object data first,
or is it already available for monoid/measure/represented-norm shadows?
```

## 2. Trigger Rule

For each operation below, record `TRIGGERS_100` if the operation is
defined on the shadow input category before a map consumes primitive
Euler fields:

```text
alpha;
v;
depth;
ell;
mu_C;
Euler-product factorization domain;
prime-power graph-depth class.
```

Record `ESCAPES_100` only if the operation's source category already
requires those fields as object data and Epstein/DH controls cannot form
the source object or the first carrier-consuming map.

Naming a strict subcategory is not enough. The first unformable map must
be written.

Common test:

```text
A. Is the operation defined on commutative monoids, represented-norm
   data, positive multisets, coefficient multisets, or positive
   measures?

B. Does the shadow functor U preserve, reflect, or detect the
   operation?

C. Can Epstein Q=x^2+5y^2 or a DH coefficient/measure shadow be
   substituted before alpha/v/depth/ell/mu_C/Euler factorization is
   checked?

D. Do F_C and the trace theorem still exist after substitution?
```

If A-D are yes, route to doc 100 and record
`REJECT_CARRIER_OVERREACH`.

## 3. Operation Audit

```text
tensor product / monoidal product
  TRIGGERS_100 if it is the ordinary tensor/product of count, measure,
  coefficient, sheaf, module, kernel, or determinant shadows.
  ESCAPES_100 only if the tensor product is defined in ECar_L1 and its
  input objects already include primitive carrier fields.

direct sum / additive completion
  TRIGGERS_100 if M_C is formed by adding bank and continuum summands,
  or by additive closure of shadow objects. Also check doc 79/doc 86
  for side-block collapse.
  ESCAPES_100 only if the addition is internal to one carrier-typed
  mixed object and cannot be formed for represented-norm or measure
  controls.

completion / closure
  TRIGGERS_100 if the completion is metric, Banach, Hilbert, condensed,
  liquid, bornological, or measure-theoretic completion of shadow data
  before carrier consumption.
  ESCAPES_100 only if the completion functor is defined for carrier
  objects after alpha/v/depth/ell/mu_C are load-bearing.

pushforward / integration / trace to a point
  TRIGGERS_100 if the pushforward exists for positive measures,
  countable multisets, represented-norm monoids, or ordinary kernel
  traces.
  ESCAPES_100 only if the properness/trace theorem is stated on ECar_L1
  objects and fails to accept Epstein/DH shadows at the source.

coend / colimit / quotient
  TRIGGERS_100 if the coend or quotient is computed in a broad
  monoidal, additive, module, sheaf, or correspondence category whose
  inputs are shadow-stable.
  ESCAPES_100 only if the indexing category or equivalence relation
  itself requires primitive Euler fields before the coend exists.

kernel / correspondence
  TRIGGERS_100 if the kernel is a function, distribution, measure,
  integral operator, sheaf kernel, or correspondence built from length,
  count, or coefficient data.
  ESCAPES_100 only if the kernel source and target are ECar_L1 objects
  and the correspondence cannot be written for represented-norm or DH
  shadows.

determinant / cokernel / index
  TRIGGERS_100 if the determinant, cokernel, index, Gram, or count
  object is built functorially from the shadow-level mixed object.
  ESCAPES_100 only if the determinant/index theory is defined after the
  strict carrier map and is unavailable for the controls.

trace-class closure
  TRIGGERS_100 if the class of traceable objects is closed under the
  same shadow operations that build M_C and F_C.
  ESCAPES_100 only if traceability is a theorem about strict carrier
  objects and explicitly excludes represented-norm and measure shadows.
```

## 4. Composite Constructions

For a composite construction, classify by the earliest operation that
creates a mixed object, codomain, or traceable object.

```text
If the earliest such operation is shadow-stable:
  route to doc 100, then doc 97.

If the earliest such operation is carrier-consuming:
  route to doc 98 and require the full ECar_L1 record.

If bank and continuum are only combined after separate evaluation:
  route to docs 79 and 86 before doc 100.

If the form or codomain is chosen externally after M_C exists:
  route to doc 93 before doc 100.

If the construction is chosen after zero-side comparison:
  route to doc 91 before doc 100.
```

The earliest broken gate wins. Do not use a later trace-derived
codomain to repair an earlier shadow-stable mixed object.

## 5. Fillable Audit

```text
candidate:
operation creating M_C:
operation creating F_C:
trace theorem:

first mixed-object operation:
  operation:
  source category:
  primitive carrier fields required before operation? YES/NO:
  represented-norm shadow accepted? YES/NO:
  positive measure/DH shadow accepted? YES/NO:

doc-100 status:
  TRIGGERS_100 | ESCAPES_100 | OUT_OF_SCOPE:

earliest gate:
  REJECT_TRACE_ILLEGAL | REJECT_BANK | REJECT_SIDE_BLOCK |
  REJECT_FREE_WEIGHT | REJECT_CARRIER_OVERREACH |
  REJECT_FREEZE | HOLD_STRICT_EULER:

exact first carrier-consuming map, if claimed:
control exclusion proof:
```

## 6. Consequence

A future S3 proposal cannot advance by saying that M_C is produced by a
standard construction unless it also states the source category and the
first primitive carrier requirement. If the construction is already
available for monoid, measure, coefficient, represented-norm, or
determinant shadows, doc 100 applies.

The surviving positive work remains doc 98:

```text
write the first ECar_L1 map that consumes primitive Euler carrier fields
before M_C, F_C, or Tr_L exists, and prove that Epstein/DH cannot form
that object or map.
```

## 7. Relation To Existing Docs

```text
doc 79 and doc 86
  Reject side-block combinations before this audit is needed.

doc 91
  Rejects zero-side-dependent operation selection.

doc 93
  Rejects externally supplied forms and codomains.

doc 97
  Receives the carrier-overreach verdict when doc 100 triggers.

doc 98
  Gives the full strict-domain target after the first map is named.

doc 100
  Proves the conditional no-go that this audit applies.

doc 103
  Gives the first-map record for proposals claiming to escape doc 100 by
  requiring primitive carrier fields first.
```
