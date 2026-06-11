# 71 - B1 proposal ledger

Status: construction ledger / admission template, 2026-06-11. This
turns docs 46, 54, and 60 into an operational format for the next
post-B0 object. It is not a B1 construction and does not claim that an
admissible B1 exists.

## 1. Purpose

B0 is now calibrated: it records the Tate/RR one-place shadow, the
`p^Z` comb address, and the Epstein guard, while refusing to promote a
unit, Frobenius action, odd slot, index form, full class family, or
comparison theorem.

B1 is the first object that must expose real candidate structure. It
is not "B0 with two primes." It must name the first map where:

```text
log p is retained before trace evaluation;
the banked comb and continuum are coupled on the same form;
Epstein/DH controls die at carrier/effectivity;
zero-side data has not entered.
```

This ledger is the required record before any new B1 witness is built.
For A6/LT76 liquid trace proposals, doc 92 routes the clause-level
ledger verdicts before this file can mark a B1 proposal advanced.

## 2. Required Record

Every B1 proposal must be entered in the following form.

```text
candidate name:
date:
source theorem/object:

L1 category:
  liquid/gaseous/metric analytic structure:
  internal R:
  internal T=R/Z:
  archimedean completion:

bank embedding b1:
  prime-power comb preserved:
  graph-depth data preserved:
  count layer preserved:
  known carrier guards preserved:

first log p carrier:
  metric coefficient | analytic ring | equivariant datum |
  density | explicit kernel | stronger:

LS3 status:
  derived | conjectural | absent | inserted:
  unit covariance statement:

LS4 map:
  domain:
  codomain:
  formula or theorem statement:
  same-form index/Gram/count object:

carrier guard:
  Epstein Q=x^2+5y^2 result:
    theta/count survives | fails:
    valuation/coupling undefined | computes:
    failure point:
  DH result:
    no carrier | computes | not tested:

zero-free freeze:
  formulas frozen:
  constants frozen:
  loci/classes frozen:
  first zero contact:

LT76/doc92 route if applicable:
  LT76 clauses claimed:
  local ledger verdicts:
  adjacent ledgers still unknown:
  NO76 kill status:
  claims not inferred:

optional promotion fields:
  Fr1:
  H_odd:
  I:
  N:
  Count:
  Compare:

doc-45 clauses advanced:
doc-45 clauses still open:
verdict:
  REJECT | HOLD | ADVANCE:
```

Blank answers are allowed only in optional promotion fields. Blank
answers in `L1`, `b1`, `first log p carrier`, `LS4 map`, `carrier
guard`, or `zero-free freeze` are automatic `REJECT` or `HOLD`.

## 3. Admission Tests

### Test B1.1 - Scale Retention

Reject if the only place `log p` lives is the homotopy type of
`R/(log p)Z`, a bare sheaf category, or a localizing-invariant value
of a circle. Docs 51, 63, 68, 80, 81, 82, 84, and 85 apply.

Advance only if `log p` is retained as metric, analytic-ring,
equivariant, density, kernel, or stronger structure before trace
evaluation.

### Test B1.2 - Conservative Bank Embedding

Reject if the embedding rescales, quotients, or destroys the banked
prime-power comb, graph-depth data, count layer, or known carrier
guards. B1 may enrich the bank; it may not replace the bank by a
parallel analogy.

Doc 89 governs the A6/LT76 bank-embedding ledger.

### Test B1.3 - LS3 Honesty

Reject if the unit is a chosen Gaussian, Haar density, normalization,
scale, Hermite perturbation, or repair atom. Hold if the unit is
honestly open. Advance only if the proposal either derives the unit or
does not use a unit-dependent claim at B1.

Docs 55 and 66 govern this test.

### Test B1.4 - Same-Form LS4 Coupling

Reject if the archimedean term is a side block beside the p-complete or
comb data. Hold if a category retaining scale is present but no trace
map is written.

Advance only if the proposal writes a map or theorem pairing the
banked comb and continuum on the same index/Gram/count form.

Docs 54, 68, 79, 86, and 88 govern this test.

### Test B1.5 - Carrier Selectivity

Run the Epstein guard at the level of formability, not signs. For
`Q=x^2+5y^2`, theta/count shadows may survive, but the prime-power
valuation/tower coupling must be undefined because represented-norm
data has no free rank-one valuation address.

Reject if the same LS4 coupling computes for Epstein or DH. Hold if
the death point is not tested. Advance only if the failure point is
carrier/effectivity.

Docs 53, 64, 74, and 87 govern this test.

### Test B1.6 - Zero-Free Freeze

Reject if zeta zeros, zero-side signs, zero-side eigenvalues, or
RH-line facts choose any B1 object, constant, class, unit, or coupling.
Advance only if the first zero contact is after a frozen record.

Docs 59, 69, and 91 govern this test.

## 4. Optional Promotion Audit

B1 may leave `Fr1`, `H_odd`, `I`, `N`, `Count`, and `Compare` open. If
any are claimed, they must satisfy their full gates immediately.

```text
Fr1 claimed:
  apply docs 52, 65, 69.

H_odd claimed:
  nonzero slot and unforced eigenvalues required; apply docs 52, 65,
  68, 69, and 70.

I or N claimed:
  native nonnegative value plus full graph-cone exhaustion required;
  apply docs 56, 67, and 70.

Count or Compare claimed:
  different natural domains and contentful theorem required; apply
  docs 52, 65, 68, 69, and 70.
```

If an optional promotion field fails, the proposal is not necessarily
dead as B1. It may be demoted to an A/B/LS4 construction if the failed
field is removed and the demotion is recorded.

## 5. Initial Candidate Slots

The ledger currently licenses only slots, not admitted candidates.

```text
Slot S1 liquid/gaseous analytic trace
  Source: MM LS1-LS6 and doc 46.
  Required next object: a trace-calibrated subcategory with internal
  R/T and a written LS4-like map.
  Current status: HOLD until the map is written.

Slot S2 equivariant metric circle trace
  Source: doc 54 Q1/Q3.
  Required next object: T_p retaining log p as equivariant/metric data
  before trace, not as bare Shv(S^1).
  Current status: HOLD until the trace is shown scale-retentive.

Slot S3 explicit comb-continuum kernel
  Source: doc 46 build order and doc 49 calibration.
  Required next object: a doc-103 strict first carrier-consuming map
  that precedes M_C/F_C/Tr_L and is unformable for Epstein/DH controls.
  Current status: HOLD until that first-map record is filled, then
  routed back through doc 98.

Slot S4 p-complete-origin hybrid
  Source: docs 57 and 68.
  Required next object: internal R/T, structural iota, same-form LS4,
  non-transport Count, and unforced H_odd if E-side claims are made.
  Current status: HOLD only if the archimedean escape package is
  structural; otherwise REJECT as pure p-complete.

Slot S5 A6/LT76 liquid trace route
  Source: docs 76-92.
  Required next object: a doc-92 routed LT76 package with explicit
  verdicts for each claimed LT76 clause, no cross-gate inference, and
  doc-71 B1 fields filled from local ledger passes only.
  Current status: HOLD until the relevant docs 81-91 ledgers have
  local PASS entries or a covered NO76 kill routes the proposal away.
```

No slot is currently `ADVANCE`. Doc 72 fills these slots as ledger
entries: S1-S3 and S5 are `HOLD`, and S4 is `REJECT` as pure
p-complete or `HOLD` only after a structural archimedean escape
package is supplied.

## 6. Next Work

The next construction step is not another witness. It is to fill one
ledger entry for a concrete proposal and classify it:

```text
REJECT
  A required B1 field fails.

HOLD
  Scale/carrier structure is plausible, but LS4 or carrier death is
  not written.

ADVANCE
  The proposal has retained log p, conservative bank embedding,
  same-form LS4 coupling, carrier/effectivity death for Epstein/DH,
  and a zero-free freeze record.
```

Only an `ADVANCE` entry should trigger a new B1 witness.
