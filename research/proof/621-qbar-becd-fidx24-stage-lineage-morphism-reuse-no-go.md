# 621 - Qbar_BECD FIdx24 Stage-Lineage Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by treating
refinement-stage persistence of the residual labels as positive morphism
evidence.

The named mechanism is **negative-stage lineage collapse**.

## Setup

Doc 620 kills the frontier-map consistency/rejection ledger as positive
morphism evidence. The remaining nearby temptation is longitudinal: maybe the
labels `not_source_internal`, `external`, and `oracle` become reusable because
they persist across executable refinement stages.

This is a different hypothesis from source-event payload reuse or route-graph
reuse: it asks whether the historical refinement chain itself supplies the
missing morphism.

## Obstruction

Across the relevant executable stages,

```text
574, 576, 594-606, 608, 610
```

the label `not_source_internal` appears exactly once per stage, but only as a
`BANNED_FLAGS` entry. Likewise `external` appears as a banned flag in docs
576, 594-606, 608, and 610, and `oracle` appears as a banned flag in docs
594-606, 608, and 610.

The exact singleton class labels and exact tail do not appear in those banned
lineages:

```text
boundary_externality
source_internality
external_or_oracle
```

More importantly, the accepted stage data contains none of the residual labels.
They do not occur in:

```text
required dependencies;
frontier-map added_atoms;
frontier-map witness ids;
current accepted atoms/invariants.
```

All 48 visible lineage flags are current rejected repairs, and each is rejected
by the same document whose executable witness lists it as banned. Thus the
longitudinal persistence is negative diagnostic persistence, not constructive
reuse.

## Consequence

The surviving route cannot use historical persistence through the existing
refinement stages as the missing morphism. It must add new proof-relevant
morphism evidence outside doc610 primitive algebra, source-event payload
algebra, doc605 route graph, frontier-map consistency/rejection bookkeeping,
and executable stage-lineage diagnostics; or prove that every such addition is
synthetic duplication, name lookup, stem retuning, class collapse, or a doc-602
anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_stage_lineage_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSTAGELINEAGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSTAGELINEAGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the exact stage profiles for `not_source_internal`, `external`, and `oracle`,
the absence of residual labels from accepted dependencies/atoms/witness ids,
and the fact that all visible lineage flags are rejected by their own stages.
