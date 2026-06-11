# 90 - Internal archimedean objects ledger

Status: operational ledger / LT76.2 internal R/T boundary,
2026-06-11. This records what must be proved before a proposal can
claim internal archimedean objects.

## 1. Purpose

LT76.2 requires:

```text
L1 contains internal R_L and T=R/Z, with the archimedean completion
present at the object or trace level.
```

This is separate from traceability, A1 scale retention, LS4 coupling,
and carrier selectivity. A p-complete or finite-place construction may
provide valuable supply data, but it does not satisfy LT76.2 unless
`R_L`, `T`, and the archimedean completion are structural objects in
the candidate category.

## 2. Required Record

Every LT76.2 claim must fill:

```text
candidate:
date:
source theorem/object:

category:
  L1:
  object class:
  morphisms:
  monoidal/analytic structure:

internal archimedean objects:
  R_L:
  T=R/Z:
  quotient theorem:
  T_C=R_L/(log alpha)Z:
  archimedean completion:
  structural iota, if used:

construction status:
  first map where R_L appears:
  first map where T appears:
  first map where archimedean completion appears:
  relation to finite-place/banked data:

p-complete audit:
  p-complete source data:
  external complex readout:
  determinant/regularization readout:
  side archimedean block:
  transport-only comparison:

interaction with other gates:
  TRACE status:
  A1 status:
  LS4 status:
  BANK status:
  CARRIER status:

verdict:
  REJECT_ARCH | REJECT_OVERCLAIM | HOLD_ARCH | PASS_ARCH |
  OUT_OF_SCOPE:
```

Blank answers for `R_L`, `T=R/Z`, or `archimedean completion` force
`REJECT_ARCH` or `HOLD_ARCH`.

## 3. Decision Rule

### A2.1 REJECT_ARCH

Reject if any of the following holds.

```text
R1. The construction is purely p-complete, TP/TR/TC/Witt, prismatic,
    Nygaard-complete, or cyclotomic, with no internal R_L or T.

R2. R or C appears only as an external readout, embedding, determinant
    target, or regularization codomain.

R3. The circle is only a bare topological S^1 or notation for
    R/(log p)Z, with no internal analytic/metric/liquid object.

R4. The archimedean term is a side block rather than part of the
    candidate object or trace domain.

R5. The claimed internal object is introduced only after the trace or
    bank computation has already been evaluated.
```

R1-R2 are docs 57 and 68. R4 overlaps doc 79 but is rejected here at
the object level.

### A2.2 HOLD_ARCH

Hold if plausible internal archimedean objects are named but one of
the following is missing.

```text
H1. The category L1 is not specified.
H2. R_L is named, but T=R/Z or T_C is not constructed internally.
H3. The archimedean completion is asserted but not located at object
    or trace level.
H4. A structural iota is needed but not constructed.
H5. It is unclear how the internal R/T relates to the banked finite
    place data.
```

### A2.3 REJECT_OVERCLAIM

Reject status inflation if any of the following holds.

```text
O1. PASS_ARCH is claimed as traceability.
O2. PASS_ARCH is claimed as A1 scale retention.
O3. PASS_ARCH is claimed as LS4 same-form coupling.
O4. PASS_ARCH is claimed as carrier selectivity.
O5. PASS_ARCH is claimed as LS3, BC13, P3, Count/Compare, B1
    admission, RH, or positivity.
```

Internal archimedean objects are infrastructure, not the whole
candidate.

### A2.4 PASS_ARCH

Pass only if all of the following are supplied.

```text
P1. L1 is named.
P2. R_L is an internal object of L1.
P3. T=R/Z or the relevant quotient T_C is constructed internally.
P4. A quotient theorem or construction supplies the circle internally;
    it is not merely identified with bare S^1.
P5. The archimedean completion is present at object or trace level,
    not only as a later readout.
P6. Any iota-like map is structural and candidate-native.
P7. The construction is not purely p-complete or side-block
    archimedean data.
P8. The record is zero-free before optional comparison.
```

`PASS_ARCH` advances LT76.2/G60.3 only. It is not traceability, A1,
LS4, bank embedding, carrier selectivity, LS3, BC13, P3,
Count/Compare, or RH.

### A2.5 OUT_OF_SCOPE

Mark OUT_OF_SCOPE if the answer concerns traceability, scale
retention, same-form coupling, carrier controls, positivity, zeros, or
RH without deciding whether `R_L` and `T` are internal.

## 4. Diagnostic Tests

```text
A90.1 Internal-object test
  Identify R_L and T=R/Z as objects of L1. If they appear only in
  notation or in a target field, reject or hold.

A90.2 Circle quotient test
  Prove T=R_L/Z or T_C internally. Do not identify it only with bare
  S^1.

A90.3 Completion test
  Locate the archimedean completion at object or trace level.

A90.4 Iota test
  If an embedding into C or another archimedean realization is used,
  prove it is structural, not post hoc readout.

A90.5 P-complete test
  If the construction starts from TP/TR/Witt/prismatic data, verify
  the NF68.1-NF68.3 escape fields before marking PASS_ARCH.

A90.6 Side-block test
  If the real/circle object appears only as a separate correction
  term, reject at LT76.2 or route to doc 79/doc 86.

A90.7 Adjacent-gate audit
  Record TRACE, A1, LS4, BANK, and CARRIER statuses separately. Do not
  infer them from PASS_ARCH.
```

## 5. Relation To Other Gates

```text
PASS_ARCH, TRACE FAIL
  Internal R/T exists, but no legal Tr_L is defined.

PASS_ARCH, A1 FAIL
  Internal R/T exists, but the trace still forgets log p.

PASS_ARCH, LS4 FAIL
  Internal R/T exists, but the archimedean continuum is not coupled to
  the banked comb on one mixed object.

PASS_ARCH, BANK FAIL
  Internal R/T exists, but B0 was replaced rather than embedded.

PASS_ARCH, CARRIER FAIL
  Internal R/T exists, but the coupling computes on controls.
```

Internal archimedean objects are necessary address infrastructure.
They do not replace the other gates.

## 6. Expert Question

Ask:

```text
In the proposed category L1, what are the internal objects R_L and
T=R/Z, where is the archimedean completion present, and is any
iota-like realization structural rather than a post-trace readout?
```

Useful answers must identify:

```text
category L1:
R_L:
T=R/Z or T_C:
archimedean completion:
structural iota, if any:
relation to finite-place data:
```

## 7. Relation To Existing Docs

```text
doc 57
  Rejects pure p-complete archimedean blindness.

doc 68
  Gives the archimedean escape normal form.

doc 76
  LT76.2 names internal archimedean objects.

doc 88
  Traceability/proper-pushforward is separate.

doc 86
  Same-form LS4 coupling is separate.
```

The operational rule is:

```text
Do not mark LT76.2 or G60.3 advanced until this ledger has a PASS_ARCH
entry for the candidate.
```
