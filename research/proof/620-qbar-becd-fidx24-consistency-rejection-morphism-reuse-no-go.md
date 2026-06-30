# 620 - Qbar_BECD FIdx24 Consistency-Rejection Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by reusing the
frontier-map consistency/rejection ledger as hidden morphism evidence.

The named mechanism is **negative-ledger morphism collapse**.

## Setup

Docs 615 through 619 kill the obvious existing morphism-evidence layers:

```text
doc610 primitive conjunctions;
source-event role-payload graphs;
action-normalized and negation-normalized payload graphs;
doc605 route-graph anchor witnesses.
```

The remaining existing structure around the frontier is the consistency layer:
accepted atoms/invariants, rejected repairs, and current exclusion rules.

## Obstruction

The current frontier has 2109 rejected repairs. Exactly 36 of those are
doc-610 rejected repairs, and the current exclusion rule for
KILLCOMPEVENTSIGACTION is exactly that 36-element doc-610 rejected set.

The accepted current nodes contain none of:

```text
boundary_externality
source_internality
external_or_oracle
not_source_internal
external
oracle
```

The exact singleton class labels and the exact `external_or_oracle` tail do not
appear as rejected-repair nodes either. The `not_source_internal` tail appears
only as 17 rejected failures, rejected by docs 574, 576, 594-606, 608, and 610.
The visible `external` and `oracle` labels appear only as broad rejected flags,
with 64 and 21 rejected occurrences respectively.

Thus the consistency/rejection layer records negative failure bookkeeping. It
does not supply a positive accepted node, morphism, or reused support that can
carry the doc-614 singleton residual classes:

```text
boundary_externality -> entry_boundary:obstruction:external_or_oracle
source_internality   -> escape_boundary:..._not_source_internal
```

## Consequence

The surviving route cannot be the current doc610 primitive algebra, source-event
payload algebra, doc605 route graph, or frontier-map consistency/rejection
ledger. It must add new proof-relevant morphism evidence outside those existing
structures, or prove that every such addition is synthetic duplication, name
lookup, stem retuning, class collapse, or a doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_consistency_rejection_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONSISTREJECTMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONSISTREJECTMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the 2109 current rejected repairs, the exact 36 doc-610 exclusion set, the lack
of accepted nodes for the singleton labels/tails, and the fact that
not_source_internal, external, and oracle occur only in rejected/excluded
bookkeeping rather than positive morphism evidence.
