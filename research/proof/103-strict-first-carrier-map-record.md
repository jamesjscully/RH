# 103 - Strict first carrier-map record

Status: positive-side record template / S3 admission precheck,
2026-06-11. This is the smallest record a future strict `ECar_L1`
proposal must fill before it can escape docs 100-102. It is not a
construction and does not authorize a witness.

## 1. Purpose

Docs 100-102 reject S3 proposals whose mixed object, codomain, or trace
is created by shadow-stable operations before primitive carrier
checking. The surviving positive route must therefore start earlier:

```text
write the first carrier-consuming object or map before M_C, F_C, or
Tr_L exists.
```

This document records exactly what that first map must contain.

## 2. Minimal Shape

A strict first carrier-map proposal has the form:

```text
source object S_C in ECar_L1
  contains primitive Euler-carrier fields

first carrier-consuming map kappa_C
  S_C -> Y_C

then, only after kappa_C exists:
  b1(comb_C) -> M_C <- R_L/T_C
  M_C -> F_C -> Tr_L(F_C)
```

The first map `kappa_C` must be unavailable for Epstein/DH controls for
structural reasons, not because a later form, weight, regularization,
or positivity test rejects them.

## 3. Required Primitive Fields

The source object must state which fields are primitive object data:

```text
alpha:
  distinguished atom or base generator:

v:
  valuation or carrier-degree map:

depth:
  tower or graph-depth coordinate:

ell:
  length/log-address tied to alpha and v:

mu_C:
  carrier measure/density, if claimed:

Euler factorization:
  product/factorization domain:

graph-depth class:
  Frobenius/index/HH graph class, if claimed:
```

At least one of `alpha`, `v`, `depth`, `ell`, or the Euler
factorization domain must be consumed by `kappa_C` before any
shadow-stable operation can form `M_C`, `F_C`, or a traceable object.

## 4. Fillable Record

```text
candidate:
ansatz class:
source theorem:

ECar_L1 source:
  category/subcategory:
  object S_C:
  primitive fields present before maps:
  proof these are object data, not labels:

first carrier-consuming map:
  name kappa_C:
  source:
  target:
  exact primitive field consumed first:
  why kappa_C is before M_C/F_C/Tr_L:
  proof before M_C? YES/NO:
  proof before F_C? YES/NO:
  proof before Tr_L? YES/NO:
  operation type:
  functoriality domain:

operation audit before kappa_C:
  tensor/product used before first map? YES/NO:
  sum/completion/pushforward/coend used before first map? YES/NO:
  kernel/correspondence/determinant/cokernel used before first map? YES/NO:
  trace-class closure used before first map? YES/NO:
  doc100/doc101 escape reason:

B0 bank embedding before kappa_C:
  p^Z comb preserved:
  q/log p address preserved:
  Count0/RR layer preserved:
  graph-depth data preserved, if claimed:
  Epstein guard preserved as control test:

control exclusion at kappa_C:
  Epstein represented-norm shadow exists? YES/NO:
  Epstein S_C object? YES/NO:
  Epstein kappa_C formable? YES/NO:
  exact failed field or axiom:
  DH shadow exists? YES/NO:
  DH S_C object? YES/NO:
  DH kappa_C formable? YES/NO:
  exact failed field or axiom:

post-kappa construction:
  M_C operation:
  F_C operation:
  trace theorem:
  why docs 100-102 do not apply:

downstream obligations, not yet promotion:
  trace legality still needed:
  conservative B0 bank embedding still needed:
  same mixed M_C still needed:
  trace-derived F_C still needed:
  zero-free freeze still needed:

freeze:
  S_C frozen before zero contact:
  kappa_C frozen before zero contact:
  control exclusions frozen before zero contact:
  first zero contact:

verdict:
  FIRST_MAP_PASS | FIRST_MAP_HOLD |
  REJECT_NO_PRIMITIVE_FIELD | REJECT_SHADOW_STABLE |
  REJECT_CONTROL_FORMABLE | REJECT_FREE_WEIGHT | REJECT_BANK |
  REJECT_TRACE_ILLEGAL | REJECT_FREEZE | OUT_OF_SCOPE:
```

## 5. Decision Rule

```text
FIRST_MAP_PASS
  S_C and kappa_C are named; kappa_C consumes primitive carrier fields
  before M_C/F_C/Tr_L; B0 embeds conservatively enough to test the map;
  Epstein/DH cannot form S_C or kappa_C; freeze is recorded. Route to
  doc 98 for the remaining trace, mixed-object, and codomain fields.

FIRST_MAP_HOLD
  A plausible S_C or kappa_C is named, but at least one primitive field,
  bank embedding, control exclusion, or freeze field is incomplete.

REJECT_NO_PRIMITIVE_FIELD
  S_C is a relabeling of shadow data and no primitive carrier field is
  consumed before M_C/F_C/Tr_L. Route to doc 109 for the bounded
  relabeling/decorated-shadow no-go.

REJECT_SHADOW_STABLE
  kappa_C or the operation creating its target is defined for monoid,
  represented-norm, measure, coefficient, determinant, or trace-class
  shadows. Route to docs 100-102 and doc 109 if the claimed strict
  source is only a decorated shadow.

REJECT_CONTROL_FORMABLE
  Epstein or DH controls can form S_C and kappa_C.

REJECT_FREE_WEIGHT
  The first-map record names a strict source, but the carrier-reading
  form, codomain, weight, stress, window, determinant wrapper, or
  regularization is externally supplied.

REJECT_BANK
  The B0 comb/address/count/guard data are replaced rather than
  embedded.

REJECT_TRACE_ILLEGAL
  The proposal uses Tr_L or trace-class closure before a named trace
  theorem covers the strict domain.

REJECT_FREEZE
  S_C, kappa_C, the exclusion proof, or first zero contact is selected
  after zero-side comparison.
```

## 6. Non-Promotion Rule

Passing this record is only a precheck. It does not prove:

```text
trace legality for M_C;
same-form LS4 coupling;
trace-derived F_C;
Count/Compare;
positivity or BC13;
H_odd;
B1 admission;
RH.
```

It only lets the candidate escape the doc-100/doc-101/doc-102
shadow-stability rejection and return to doc 98.

## 7. Relation To Existing Docs

```text
doc 87
  Supplies the carrier-selectivity ledger; this record names the first
  map tested by that ledger.

doc 89
  Supplies the conservative bank-embedding ledger.

doc 91
  Supplies the zero-free freeze ledger.

doc 98
  Gives the full strict Euler-carrier trace-domain target after the
  first map is named.

docs 100-102
  Reject proposals whose first mixed/codomain/trace operations are
  shadow-stable before primitive carrier checking.

doc 104
  Applies this record to the current A1-A6 S3 ansatz classes and records
  that no class has FIRST_MAP_PASS.

doc 109
  Rejects attempts to satisfy this record by relabeling or decorating
  shadow data rather than making primitive carrier fields object data.

doc 111
  Rejects plausible first maps whose consumed primitive field is
  forgotten before M_C, F_C, or Tr_L is formed.

doc 112
  Rejects late attempts to add carrier fields after a shadow-stable
  trace package already exists.
```
