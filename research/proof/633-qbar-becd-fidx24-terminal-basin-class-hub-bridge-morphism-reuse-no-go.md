# 633 - Qbar_BECD FIdx24 Terminal-Basin-Class-Hub-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired merely by
promoting the `terminal_basin_entry` class to the missing bridge object.

The named mechanism is **terminal-basin class-hub selector collapse**.

## Setup

Doc 632 kills the direct `external_basin` / `oracle_basin` mediator path.
The sharper remaining repair is class-level:

```text
boundary_externality -> terminal_basin_entry -> source_internality
```

This is not random. In the doc610 segment-induced class graph,
`terminal_basin_entry` is the unique common class neighbor of
`boundary_externality` and `source_internality`.

The class-edge tokens are:

```text
boundary_externality -> terminal_basin_entry:
  external, oracle

terminal_basin_entry -> source_internality:
  not
```

## Obstruction

The class-level residue is real, but it is only adjacency evidence.

The terminal-basin class has seventeen surfaces. Its external/oracle and not
attachments are disjoint:

```text
terminal_basin_entry surfaces with external/oracle:
  external_basin, oracle_basin

terminal_basin_entry surfaces with not:
  basin_not_absorbing, basin_not_extensional, entry_trace_not_replay_stable

terminal_basin_entry surfaces with both external/oracle and not:
  none
```

Both external attachment closures are mixed-class:

```text
external/oracle support:
  terminal_basin_entry=2, action_semantics=1,
  classifier_partition=1, boundary_externality=1

not support:
  terminal_basin_entry=3, finite_index_budget=1, source_internality=1
```

The internal terminal-basin connector is not automatic either. The `basin`
segment support has:

```text
basin support:
  terminal_basin_entry=10, action_semantics=1
```

and only after filtering to the terminal-basin class does it connect the
external/oracle mediators to the two basin-not mediators. That leaves four
internal basin paths:

```text
external_basin or oracle_basin
  -> basin_not_absorbing or basin_not_extensional
```

while `entry_trace_not_replay_stable` remains a not-attachment that is not in
the basin connector.

Thus the class hub requires at least three extra choices: the mixed
external/oracle attachment, the mixed not attachment, and the internal basin
mediator selector. The unique class neighbor does not itself construct a
proof-relevant morphism.

## Consequence

This is the sharpest positive residue so far: any surviving bridge is likely
trying to make the terminal-basin class into an actual categorical middle
object. But the current doc610 source-event algebra supplies only class
adjacency, not a constructed morphism with endpoints and composition. A
surviving route must add an actual terminal-basin composition law or boundary
map that explains the four mediator choices, rather than selecting them by
token filters.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_class_hub_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINCLASSHUBBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINCLASSHUBBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
unique `terminal_basin_entry` common class neighbor, the exact class-edge
tokens, the disjoint terminal-basin attachment surfaces, the mixed
external/oracle and not supports, the basin connector profile, and the four
remaining internal mediator choices.
