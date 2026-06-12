# 145 - HHG source-1 record

Status: smallest HHG source attempt / Q134.3 internal target,
2026-06-11. This is not a B1 construction, not a positivity theorem,
not an external answer, and not a witness license.

## 1. Purpose

Docs 132 and 137 separate HH graph/index data from diagnostic shadows.
The remaining A3 question is whether HH/Frobenius graph-depth data can
be primitive source data before Gram, determinant, mixed object,
codomain, or trace construction.

This document names the smallest source-level target inside
HHG-STRUCTURAL.

## 2. Candidate Record

Name:

```text
HHG-SOURCE-1.
```

Claim to decide:

```text
There exists a liquid/metrized L1 source object

  S_HH = (HH_C, alpha, v, depth, ell, graph_class, b0_embedding)

and a first map

  kappa_HH : S_HH -> Y_HH

such that HH_C cannot be defined without prime-power graph-depth
carrier data, and kappa_HH consumes that data before Gram,
determinant, mixed object, codomain, or trace construction.
```

This is narrower than full HHG-STRUCTURAL. It asks only for a real
source and first map, plus one downstream slot where the consumed field
is supposed to remain load-bearing.

## 3. Local Pass Condition

Verdict `PASS_SOURCE` requires all of:

```text
1. a named category/object construction for HH_C;
2. alpha, v, depth, ell, and graph_class as object-defining data, not
   labels;
3. a named kappa_HH consuming graph-depth or prime-power data before
   diagnostics;
4. conservative B0 comb/address/count/guard embedding;
5. Epstein/DH failure at source or first-map formability while
   theta/count shadows remain meaningful;
6. one explicit downstream slot where the consumed field remains
   load-bearing.
```

`PASS_SOURCE` would update docs 103 and 113 for A3 only. It would still
have to route through docs 98, 94, 111, 112, 118, 120, and 126 before
any B1 claim.

## 4. Kill Condition

Verdict `KILL_SOURCE_CLASS` is licensed only for the attempted
HH_C/kappa_HH construction family if it necessarily collapses to one of:

```text
diagnostic readout;
decorated shadow labels;
control-formable source/map;
side-block HH/index data;
downstream forgetfulness.
```

Do not generalize beyond the named HH source family.

## 5. Sharpen Condition

Verdict `SHARPEN_SOURCE` applies if the attempt exposes a smaller
deciding theorem, for example:

```text
HHG-DEPTH-OBJECT
  prime-power graph-depth can be object-defining in the HH/THH source
  category, rather than only an invariant or readout.

HHG-FIRST-CONSUME
  the first HH/Frobenius map consumes graph-depth before index/Gram
  formation.

HHG-CONTROL-FORM
  the same source construction is automatically formable for
  Epstein/DH controls.
```

## 6. Current Gate Run

```text
HH_C:
  not named beyond schema.

object-defining graph_class:
  not proved.

kappa_HH:
  schema named, not constructed.

B0 embedding:
  intended, not proved.

control non-formability:
  unknown.

downstream slot:
  not named.
```

Verdict:

```text
HHG-STRUCTURAL:
  HOLD_SOURCE_1.

HHG-SOURCE-1:
  ACCEPT_AS_NEXT_INTERNAL_TARGET.

A3 witness:
  still not licensed.
```

## 7. Board Update

Update Q134.3 and doc 139 as follows:

```text
The immediate internal target is HHG-SOURCE-1.

Ask first whether HH_C/kappa_HH exists as source data, with one named
downstream load-bearing slot.

Do not run Gram/index witnesses until PASS_SOURCE survives control
formability and downstream dependence.
```

## 8. Relation To Existing Docs

```text
doc 132
  HHG-FIRST remains the full strict route; SOURCE-1 is its source-level
  first step.

doc 137
  Diagnostic HH/index packages remain demoted. SOURCE-1 is the live
  escape clause.

doc 103/113
  Updated only after PASS_SOURCE, not merely after schema naming.

doc 111
  Still blocks any route whose graph-depth field is forgotten
  downstream.
```
