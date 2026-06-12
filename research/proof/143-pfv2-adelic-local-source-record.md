# 143 - PFV2 adelic-local source record

Status: smallest honest source-record attempt / Q134.1 internal result,
2026-06-11. This is not a B1 construction, witness, external answer,
or no-go theorem. It tries to build the smallest PFV2-ADELIC-LOCAL
object record left open by doc 142 and records exactly where it still
fails to become a strict first map.

## 1. Purpose

Docs 135, 140, 141, and 142 removed the cheap PFV2 options:

```text
coordinate-pair labels;
marked products or marked commutative monoids;
bare UFD/factorization pairs;
bare all-places product-formula bookkeeping.
```

The remaining A2 question is whether a two-place adelic/local source
can make the product-formula field object-defining before any kernel,
determinant, mixed object, trace package, or relation-on-labels
construction.

This document takes the promised direct shot. It writes the smallest
record that could possibly satisfy PFV2-ADELIC-LOCAL and then runs the
existing gates.

## 2. Candidate Record

For two distinct places p and q, define a proposed record
`S_{p,q}^{loc}` with fields:

```text
T_p
  a p-valuation tower or p-comb object embedding B0_p conservatively.

T_q
  a q-valuation tower or q-comb object embedding B0_q conservatively.

ell_p, ell_q
  structural log lengths, not normalization constants appended after
  trace.

v_p, v_q
  valuation-depth fields attached to T_p and T_q.

C_{not p,q}
  a complement object representing the contribution of all places other
  than p and q.

pf
  a source relation

    ell_p v_p + ell_q v_q + c(C_{not p,q}) = 0

  where c is a structural readout of C_{not p,q}, not a frozen scalar.
```

The intended first map is:

```text
kappa_PF : S_{p,q}^{loc} -> Y_{p,q}^{PF}
```

and kappa_PF is required to consume the tuple

```text
(T_p, T_q, ell_p, ell_q, v_p, v_q, C_{not p,q}, pf)
```

before M_C, F_C, Tr_L, determinant, kernel, cokernel, correspondence,
or positivity is formed.

## 3. What The Record Achieves

The record is a real improvement over the killed variants:

```text
not PFV2_coord:
  p and q are not just labels on B0_p x B0_q.

not marked product:
  the source demands a complement field and a PF relation, not only
  marked factors.

not bare UFD pair:
  PF is not imposed as an external equation on two independent
  valuations.

not bare all-places bookkeeping:
  the two-place object is named before trace, rather than obtained only
  by selecting coordinates from an already accepted global object.
```

It also gives the smallest local calibration object for future expert
answers. An answer can now point to a theorem that supplies or forbids
`C_{not p,q}` as structural source data.

## 4. Gate Run

### Gate 143.1 - B0 embedding

Verdict:

```text
LOCAL_PASS
```

Reason: the record can include conservative embeddings of B0_p and B0_q
into T_p and T_q. This is only calibration. It does not prove B1,
because B0 embedding is already known to be too weak.

### Gate 143.2 - Product-formula source data

Verdict:

```text
HOLD_COMPLEMENT
```

Reason: the relation pf is source data only if C_{not p,q} is itself a
structural object. If C_{not p,q} is a scalar, a frozen parameter, or a
placeholder for "whatever the other places contribute", then the record
falls back to doc 142 coordinate projection or complement freezing.

### Gate 143.3 - Epstein/DH non-formability

Verdict:

```text
HOLD_NO_FREE_COMPLEMENT
```

Reason: Epstein represented-norm data and DH coefficient/measure
shadows should fail before signs, trace, positivity, or zero comparison.
But this is true only if the complement object is not freely attachable
to any two towers. A formal complement slot can be added to controls as
bookkeeping, so it does not prove carrier selectivity.

### Gate 143.4 - First-map priority

Verdict:

```text
LOCAL_SCHEMA_PASS
```

Reason: the intended kappa_PF is placed before M_C/F_C/Tr_L. This is a
schema pass, not a theorem pass. The missing theorem is existence and
legality of kappa_PF in a category where C_{not p,q} is source
structural.

### Gate 143.5 - Downstream load-bearing

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem yet shows that the consumed p,q+complement field
remains necessary inside M_C, F_C, or Tr_L. Doc 111 would reject a route
that forms S_{p,q}^{loc} and then forgets the complement before the
same-form codomain or trace.

## 5. Calibration Object

The smallest honest PFV2 calibration object is:

```text
PFV2_local_record(p,q):
  S_{p,q}^{loc}
  kappa_PF schema
  B0_p and B0_q embeddings
  explicit complement slot C_{not p,q}
  pf as a source relation
```

It may be used for:

```text
expert falsification questions;
checking whether a proposed adelic theorem supplies the complement;
testing whether controls can freely add the same complement slot;
downstream-dependence bookkeeping if a real kappa_PF is later named.
```

It may not be used for:

```text
claiming FIRST_MAP_PASS;
running an A2 witness;
declaring Epstein/DH dead;
feeding doc 98, 94, 111, 112, 118, 120, or 126 as if the source were
already admitted.
```

## 6. Decisive Missing Theorem

Q134.1 is now concretely localized to:

```text
PFV2-COMP-REFLECT.
```

The theorem target:

```text
There exists an adelic/local source category with objects
S_{p,q}^{loc} such that C_{not p,q} is structural, not freely
attachable, and kappa_PF exists only for sources whose p,q towers and
complement satisfy the product-formula relation as object data.

Moreover, Epstein represented-norm data and DH coefficient/measure
shadows cannot form S_{p,q}^{loc} or kappa_PF, while B0_p and B0_q
embed conservatively and the consumed p,q+complement field remains
load-bearing downstream.
```

This is not a new perimeter gate. It is the exact obstruction exposed
by the concrete candidate record.

## 7. Verdict

Current verdict:

```text
PFV2-ADELIC-LOCAL:
  HOLD_COMPLEMENT_REFLECTION.

PFV2_local_record:
  ACCEPT_AS_CALIBRATION_OBJECT.

A2 witness:
  still not licensed.
```

Why this is progress:

```text
The target is no longer "find some product-formula source". The target
is specifically a non-free structural complement object and a first map
that consumes it before trace while controls cannot form it.
```

## 8. Board Update

Update Q134.1 and doc 139 wording as follows:

```text
PFV2-ADELIC-LOCAL remains the active A2 target.

PFV2-COMP-REFLECT is the next deciding theorem inside that target.

The allowed calibration object is PFV2_local_record(p,q).

No witness is licensed until PFV2-COMP-REFLECT is PASS or an expert
answer supplies an equivalent theorem.
```

## 9. Relation To Existing Docs

```text
doc 103
  Still HOLD: FIRST_MAP_PASS is not obtained.

doc 111
  Still blocking: downstream load-bearing is unproved.

doc 134
  Q134.1 should ask for complement reflection/no-free-complement.

doc 139
  The sendable packet should include PFV2_local_record as the concrete
  object to accept, kill, or sharpen.

doc 142
  This document fills the "structural complement" slot left open there
  and shows why a formal complement is not enough.
```

## 10. Post-doc-147 Update

Doc 147 tests the first concrete complement candidate:

```text
PFV2-REL-DIV(p,q).
```

Result:

```text
LOCAL_COMP_PASS
  for structural complement data;

HOLD_RELATIVE_FIRST_MAP
  because the p,q+complement record may still be inherited from an
  all-places source and projected to p,q;

HOLD_SOURCE_SELECTIVITY, HOLD_BANK_REPLACEMENT, HOLD_DOWNSTREAM
  for the remaining PFV2 gates.
```

Doc 147 first sharpened the immediate theorem target to:

```text
PFV2-REL-FIRST.
```

Doc 148 then rejected the ordinary classical relative divisor
presentation and sharpened the live target again:

```text
PFV2-REL-UPROP.
```

PFV2-COMP-REFLECT remains the enclosing target, but future internal
work should attack the relative universal-property/reflection theorem
before inventing another complement class.
