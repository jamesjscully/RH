# 87 - Carrier selectivity decision ledger

Status: operational ledger / B2-B3 positive boundary, 2026-06-11. This
turns docs 53, 64, 74, and 76 into a decision record for claims that a
trace or coupling is selective for the Euler-product carrier.

## 1. Purpose

Docs 81-86 separate scale retention and same-form coupling. A proposed
trace can still fail B1 if it computes equally for non-Euler-product
controls.

The carrier-selectivity target is:

```text
theta/count shadows may survive on controls, but the Euler-product
carrier or coupling must become unformable at a named first map.
```

This ledger records that death profile for LT76.6/G60.1.

## 2. Required Record

Every carrier-selectivity claim must fill:

```text
candidate:
date:
source theorem/object:

A1 status:
  doc-81/doc-84/doc-85 verdict:

LS4 status:
  doc-86 verdict:
  mixed trace object M_C:

Euler carrier fields:
  carrier C:
  A:
  distinguished atom alpha:
  valuation v:
  depth:
  address ell(k):
  measure/class mu_C:
  graph-depth or carrier-depth field:
  Euler-product factorization domain:

first carrier map:
  domain:
  codomain:
  formula or theorem:
  required carrier fields:

Epstein control:
  Q=x^2+5y^2 theta/count shadow:
  represented values used:
  first unformable field:
  first unformable map:
  failure reason:

DH control:
  control input class:
  analytic/coefficient shadow status:
  first unformable field:
  first unformable map:
  failure reason:

generic-shadow audit:
  theta/count/Poisson dependence:
  discrete-measure dependence:
  determinant/coker/shadow dependence:

zero-free freeze:
  carrier fields frozen before zero contact:

verdict:
  REJECT_CARRIER_BLIND | REJECT_OVERCLAIM | HOLD_CARRIER |
  PASS_CARRIER | OUT_OF_SCOPE:
```

Blank answers in `Euler carrier fields`, `first carrier map`, or
`Epstein control` force `REJECT_CARRIER_BLIND` or `HOLD_CARRIER`.

## 3. Decision Rule

### B.1 REJECT_CARRIER_BLIND

Reject if any of the following holds.

```text
R1. The same coupling computes for the Epstein represented-norm
    control using theta/count/Poisson data.

R2. The same coupling computes for a DH-type non-Euler-product control.

R3. The candidate only uses a multiset of positive numbers, logarithms,
    a discrete measure, theta coefficients, Poisson duality, Haar
    density, determinant, or coker shadow.

R4. The first claimed death point occurs after signs, zeros,
    positivity, or numerical comparison.

R5. The proposal names valuation/depth language, but the actual trace
    is determined by a shadow that Epstein/DH can still supply.
```

R1-R3 are docs 53 and 74. R4 enforces the doc-45 B2 timing. R5 is the
shadow-promotion failure.

### B.2 HOLD_CARRIER

Hold if a plausible carrier-selective domain is named but one of the
following is missing.

```text
H1. The first map requiring valuation/depth fields is not written.
H2. Epstein is tested only by analogy, not by the doc-64 represented
    norm obstruction.
H3. DH is untested.
H4. The mixed LS4 object is not known to require the carrier fields.
H5. The zero-free freeze record is missing.
```

`HOLD_CARRIER` means the direction may still be alive, but no witness
cycle should start.

### B.3 REJECT_OVERCLAIM

Reject status inflation if any of the following holds.

```text
O1. The record claims B1 admission from carrier selectivity alone.
O2. The record claims LS3, BC13, P3, Count/Compare, RH, or full
    Euler-product success from LT76.6 alone.
O3. A1 scale retention is used as a substitute for carrier death.
O4. LS4 same-form coupling is used as a substitute for carrier death.
```

Carrier death is one required gate, not the whole candidate.

### B.4 PASS_CARRIER

Pass only if all of the following are supplied.

```text
P1. The coupling domain requires at least one Euler-product carrier
    field: distinguished atom, valuation, tower/depth coordinate,
    graph depth, address map, or factorization domain.

P2. The first map using that field is written.

P3. For Q=x^2+5y^2, theta/count data remain meaningful, but that first
    map is unformable because represented-norm data has no free
    prime-power valuation/tower address.

P4. A DH-type control is either unformable at the same carrier level or
    explicitly outside the domain for the same structural reason.

P5. The failure occurs before signs, zeros, positivity, or RH-line
    comparisons.

P6. The same carrier field is load-bearing for the LS4 mixed object,
    not a decorative side condition.
```

`PASS_CARRIER` advances G60.1/LT76.6 only. It is not A1, LS4, LS3,
BC13, P3, Count/Compare, or RH.

### B.5 OUT_OF_SCOPE

Mark OUT_OF_SCOPE if the answer concerns only scale retention,
same-form coupling, positivity, zero-side data, or RH without deciding
carrier/effectivity death on controls.

## 4. Control Tests

Use these tests before any new witness.

```text
C87.1 Field test
  Name the carrier field without which the trace/coupling cannot be
  formed.

C87.2 First-map test
  Identify the first map that consumes that field.

C87.3 Epstein shadow test
  Verify Q=x^2+5y^2 still has theta/count data: 1,4,6,9,36 represented;
  2,3 absent; 36=4*9=6*6.

C87.4 Epstein death test
  Prove the first map is unformable for the represented-norm data
  because there is no distinguished atom, unique valuation, or tower
  coordinate.

C87.5 Generic-shadow test
  If the same formula can be evaluated from theta/count/Poisson data,
  reject as carrier-blind.

C87.6 Timing test
  If failure is detected only by bad signs, off-line zeros, or failed
  positivity, reject as too late for B2/B3.
```

## 5. Relation To A1 And LS4

The three front gates are distinct.

```text
A1 PASS, LS4 PASS, CARRIER FAIL
  The trace retains scale and is mixed, but the same mixed trace
  computes on non-Euler-product controls.

A1 PASS, CARRIER PASS, LS4 FAIL
  The carrier dies correctly, but the archimedean continuum is still a
  side block.

LS4 PASS, CARRIER HOLD
  A mixed trace exists, but no first carrier/effectivity death point is
  written.
```

Do not use carrier death as a substitute for same-form coupling, and
do not use same-form coupling as a substitute for carrier death.

## 6. Expert Question

For an external expert, ask:

```text
Which exact field in the trace domain requires a prime-power
Euler-product carrier, and at which first map does the Epstein
replacement Q=x^2+5y^2 become unformable while theta/count data remain
meaningful?
```

Useful answers must identify:

```text
carrier field:
first carrier-consuming map:
Epstein represented-norm shadow:
Epstein failure reason:
DH failure reason or out-of-domain theorem:
why the formula is not a theta/count/Poisson shadow:
```

## 7. Relation To Existing Docs

```text
doc 53
  Gives the broad carrier-blind Poisson/Epstein no-go.

doc 64
  Proves the concrete Epstein represented-norm obstruction.

doc 74
  Rejects generic S3 kernels that factor through theta/count/Poisson
  or discrete-measure shadows.

doc 76
  LT76.6 names the carrier-selective domain target.

doc 86
  Same-form LS4 coupling is separate. Carrier death alone does not
  prove LS4.

doc 60
  G60.1 requires carrier selectivity before B1 admission.
```

The operational rule is:

```text
Do not mark LT76.6 or G60.1 advanced until this ledger has a
PASS_CARRIER entry for the candidate.
```
