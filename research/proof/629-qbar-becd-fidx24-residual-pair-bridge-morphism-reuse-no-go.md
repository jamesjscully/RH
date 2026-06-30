# 629 - Qbar_BECD FIdx24 Residual-Pair-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired merely by pairing
the two remaining singleton residual surfaces and calling that pair the missing
morphism.

The named mechanism is **direct-pair selector collapse**.

## Setup

Docs 615 through 628 kill the existing primitive, payload, graph, frontier-map,
and control-plane evidence sources. A tempting next move is to bridge the two
remaining singleton residuals directly:

```text
entry_boundary:obstruction:external_or_oracle
escape_boundary:..._not_source_internal
```

This is a new hypothesis only if the bridge has independent proof-relevant
evidence. Otherwise it is just a selector for the two unsolved labels.

## Obstruction

The two residual surfaces have no shared existing support:

```text
shared doc-610 primitive signature features: none
shared exact segments: none
shared namespaces: none
shared exact payload group: none
shared action-normalized payload group: none
shared route-token support: none
```

They also cross all visible source-event typing axes:

```text
boundary kinds: entry vs escape
event kinds:    obstruction_namespace vs plain_tail
tails:          external_or_oracle vs not_source_internal
classes:        boundary_externality vs source_internality
```

The exact segments around the pair have only mixed or singleton support:

```text
external: boundary_externality=1, classifier_partition=1,
          action_semantics=1, terminal_basin_entry=1
or:       boundary_externality=1, boundary_contextual_surrogate=1,
          classifier_partition=2, action_semantics=1
oracle:   boundary_externality=1, classifier_partition=1,
          action_semantics=1, terminal_basin_entry=1
not:      terminal_basin_entry=3, finite_index_budget=1, source_internality=1
source:   source_constraint_invariant=1, trace_payload_route=1,
          source_internality=1
internal: source_internality=1
```

Thus a bridge supported only by this pair is mixed-class and exact-pair
selected. It does not become proof-relevant morphism evidence merely by naming
the pair.

## Consequence

The surviving route must add independent morphism evidence that explains why
these two residual surfaces are coupled. A direct two-surface bridge is not
enough unless it supplies new structure outside existing doc610 primitives,
source-event payload algebra, doc605 route graph, frontier-map compartments,
and direct residual-pair selection; otherwise it is synthetic duplication,
name lookup, stem retuning, class collapse, or a doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_residual_pair_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMRESIDPAIRBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMRESIDPAIRBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
absence of shared primitive features, segments, namespaces, payload groups,
action-normalized payload groups, and route-token supports, plus the mixed or
singleton exact-segment support profile.
