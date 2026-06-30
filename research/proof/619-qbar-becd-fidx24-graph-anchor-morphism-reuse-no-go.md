# 619 - Qbar_BECD FIdx24 Graph-Anchor Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by reusing the
existing doc-605 route-graph anchor witnesses.

The named mechanism is **graph-anchor singleton support**.

## Setup

Docs 617 and 618 kill the natural payload-algebra normalizations. The next
source of proof-relevant evidence is the already banked doc-605 graph layer:

```text
surface -> class edge witness;
class -> kill-frontier anchor witness.
```

This layer is not merely a string payload algebra. It is the existing local
graph evidence that doc610 inherits.

## Obstruction

The only class-anchor witnesses with support one are exactly:

```text
boundary_externality
source_internality
```

Those are the two doc-614 singleton residual classes, and their supports are:

```text
boundary_externality -> entry_boundary:obstruction:external_or_oracle
source_internality   -> escape_boundary:..._not_source_internal
```

Their local surface-edge tokens are singleton supports too:

```text
external
not_source_internal
```

The anchor routes are:

```text
boundary_externality -> obstruction_terminal_basin_boundary_failure
source_internality   -> represented_limit_source_constraint_bundle_failure
```

The route witnesses are local and not marked as surface-name-only or
global-lookup-only. The problem is stronger: the existing graph evidence is
valid local evidence, but its reusable support is still singleton exactly at
the two residual classes that need repair.

## Consequence

The surviving route cannot be the current doc610 primitive algebra, source-event
payload algebra, or doc605 route graph. It must add new proof-relevant morphism
evidence outside those existing structures, or prove that every such addition is
synthetic duplication, name lookup, stem retuning, class collapse, or a doc-602
anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_graph_anchor_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMGRAPHANCHORMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMGRAPHANCHORMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the doc-605 surface-edge and class-anchor supports, the singleton graph-token
supports, and the fact that the only singleton class-anchor supports are exactly
the two residual singleton classes.
