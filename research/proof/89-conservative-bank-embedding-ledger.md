# 89 - Conservative bank embedding ledger

Status: operational ledger / LT76.4 bank-preservation boundary,
2026-06-11. This records what must be preserved when a B1/A6 proposal
claims to extend the B0 calibration bank.

## 1. Purpose

B0 is a calibration floor, not a candidate. A future object may enrich
the bank, but it may not replace the bank by a parallel analogy.

The conservative embedding target is:

```text
b1 must carry the B0 p^Z comb/address, count layer, and known carrier
guards into the proposed trace package without rescaling, quotienting,
or discarding the data that made B0 honest.
```

This ledger decides LT76.4.

## 2. Required Record

Every bank-embedding claim must fill:

```text
candidate:
date:
source theorem/object:

B0 source fields:
  q-expansion grading:
  p^Z comb:
  log p address spacing:
  Poisson dual address:
  Count0 layer:
  RR/Serre trace calibration:
  Epstein guard:
  absent promotion fields:

embedding b1:
  domain:
  codomain:
  formula/theorem:
  injective/conservative sense:
  functoriality/naturality:

preservation checks:
  p^Z comb preserved:
  log p address preserved:
  Count0/RR layer preserved:
  q-grading/valuation tower preserved:
  Epstein guard preserved:
  no promotion fields silently added:

allowed enrichment:
  metric/liquid/equivariant/kernel structure added:
  traceability theorem:
  same-form target:
  carrier-selective field:

replacement audit:
  rescaling:
  quotienting:
  forgetting to theta/count/Poisson shadow:
  replacing p^Z by generic discrete measure:
  replacing B0 by Route A analogy:

interaction with other gates:
  A1 status:
  TRACE status:
  LS4 status:
  CARRIER status:

verdict:
  REJECT_BANK | REJECT_OVERCLAIM | HOLD_BANK | PASS_BANK |
  OUT_OF_SCOPE:
```

Blank answers in `embedding b1` or `preservation checks` force
`REJECT_BANK` or `HOLD_BANK`.

## 3. Decision Rule

### E.1 REJECT_BANK

Reject if any of the following holds.

```text
R1. The proposal replaces the p^Z comb by a generic lattice, generic
    discrete measure, theta series, represented-norm multiset, or
    coefficient multiset.

R2. The log p address is rescaled, quotient-forgotten, or appended
    only after trace evaluation.

R3. The Count0/RR layer is discarded rather than embedded.

R4. The known Epstein guard is not preserved: theta/count survives,
    but valuation/q-tower address is unformable.

R5. The proposal silently adds U, Fr, H_odd, I, N, Count, or Compare
    to the bank without satisfying the corresponding gates.

R6. The claimed bank is only another calibration identity, not an
    embedding of B0 into the new trace package.
```

### E.2 HOLD_BANK

Hold if the embedding is plausible but one of the following is missing.

```text
H1. The map b1 is not written.
H2. Preservation of q-grading or p^Z comb is asserted but not proved.
H3. It is unknown whether Count0/RR survives in the enriched category.
H4. The Epstein guard has not been rerun at the formability level.
H5. The embedding preserves shadows, but it is not clear whether the
    valuation/depth carrier survives.
```

### E.3 REJECT_OVERCLAIM

Reject status inflation if any of the following holds.

```text
O1. PASS_BANK is claimed as A1 scale retention.
O2. PASS_BANK is claimed as traceability, LS4, carrier selectivity,
    LS3, BC13, P3, Count/Compare, or RH.
O3. The B0 calibration pass is promoted to B1 without docs 81, 86,
    87, and 88 passing separately.
```

Bank preservation is infrastructure, not the missing object.

### E.4 PASS_BANK

Pass only if all of the following are supplied.

```text
P1. A map b1 from the B0 bank into the proposed trace package is named.
P2. The p^Z comb and q/log p address survive as structure, not only as
    notation or a later normalization.
P3. The Count0/RR calibration layer is preserved or explicitly
    embedded as calibration-only data.
P4. The known Epstein guard is preserved at the same formability
    point: theta/count alive, valuation/q-tower unformable.
P5. No absent B0 promotion field is silently added.
P6. Any enrichment is additional structure on the bank, not a
    replacement of the bank.
```

`PASS_BANK` advances LT76.4 only. It is not A1, traceability, LS4,
carrier selectivity, LS3, BC13, P3, Count/Compare, or RH.

### E.5 OUT_OF_SCOPE

Mark OUT_OF_SCOPE if the answer discusses scale retention,
traceability, LS4, carrier controls, positivity, zeros, or RH without
deciding whether B0 embeds conservatively.

## 4. Diagnostic Tests

```text
B89.1 Map test
  Write b1. If no map is written, hold or reject.

B89.2 Comb-address test
  Verify the p^Z comb and log p address survive before trace.

B89.3 Count-layer test
  Verify Count0/RR calibration is preserved as calibration-only data.

B89.4 Guard-preservation test
  Reapply doc 64: Q=x^2+5y^2 keeps theta/count but kills the
  valuation/q-tower address.

B89.5 Shadow-replacement test
  If the embedding factors only through theta/count/Poisson or a
  generic measure, reject as bank replacement.

B89.6 Promotion audit
  Confirm U, Fr, H_odd, I, N, Count, and Compare are absent unless
  their full gates are separately satisfied.
```

## 5. Relation To Other Gates

```text
PASS_BANK, A1 FAIL
  The B0 bank embeds, but the trace still does not retain scale.

PASS_BANK, TRACE FAIL
  The bank embeds into a category with no legal Tr_L.

PASS_BANK, LS4 FAIL
  The bank embeds, but it is not coupled to the continuum on one mixed
  object.

PASS_BANK, CARRIER FAIL
  The bank embeds, but the proposed later coupling still computes on
  controls.
```

Bank preservation is required so B1 is really post-B0. It does not
replace the other admission gates.

## 6. Expert Question

Ask:

```text
What is the exact map b1 from the B0 Tate/RR q-expansion bank into the
proposed trace package, and which theorem shows it preserves the p^Z
comb, log p address, Count0/RR calibration, and Epstein guard?
```

Useful answers must identify:

```text
b1 map:
source B0 fields:
target category:
preservation theorem:
Epstein guard preservation:
promotion-field audit:
```

## 7. Relation To Existing Docs

```text
doc 49
  Defines B0 and the executable calibration witness.

doc 71
  Requires conservative bank embedding in every B1 proposal.

doc 76
  LT76.4 names conservative bank embedding.

doc 78
  Records Route A/B0 as partial calibration only.

doc 86
  Requires a separate mixed trace object for LS4.

doc 87
  Requires separate carrier selectivity beyond bank preservation.

doc 88
  Requires a separate traceability theorem before Tr_L is legal.
```

The operational rule is:

```text
Do not mark LT76.4 advanced until this ledger has a PASS_BANK entry
for the candidate.
```
