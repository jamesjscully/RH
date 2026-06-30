# 628 - Qbar_BECD FIdx24 Control-Plane Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by reusing the
remaining frontier-map control-plane fields as residual morphism evidence.

The named mechanism is **control-plane residual blindness**.

## Setup

Docs 620 through 627 kill rejection bookkeeping, executable lineage,
frontier metadata, accepted edges, accepted atom/invariant payloads, and
`deltas`/`witnesses` provenance payloads. The remaining structured control
plane is:

```text
frontier descriptor;
consistency_rules.requires;
consistency_rules.context_separation.
```

The `consistency_rules.excludes_current` rejected ledger was already killed by
doc 620, so this check only tests the positive control-plane payloads.

## Obstruction

The remaining control-plane section sizes are:

```text
frontier:                       7 entries
consistency_rules.requires:     86 entries
consistency_rules.context_sep:  4 entries
```

None of these payloads contains any exact doc-614 residual class/surface/tail
label:

```text
boundary_externality
source_internality
external_or_oracle
not_source_internal
```

Nor does any payload contain the broad residual tokens:

```text
external
oracle
not
tail
```

The only visible overlaps are generic source-square control-plane terms:

```text
frontier:
  source:      1
  internal:    1
  boundary:    2
  class:       1
  obstruction: 2

consistency_rules.requires:
  source:      75
  internal:    39
  boundary:    75
  class:       36
  obstruction: 15

consistency_rules.context_separation:
  source:       1
  internal:     0
  boundary:     0
  class:        0
  obstruction:  0
```

Thus the control plane names the current source-square bookkeeping and
dependency discipline. It supplies no residual-specific endpoint or class-pure
support for:

```text
entry_boundary:obstruction:external_or_oracle
escape_boundary:..._not_source_internal
```

## Consequence

The surviving route cannot use the frontier descriptor or positive consistency
rules as the missing morphism. It must add new proof-relevant morphism evidence
outside doc610 primitive algebra, source-event payload algebra, doc605 route
graph, frontier-map consistency/rejection bookkeeping, executable
stage-lineage diagnostics, doc610 audit dependency wiring, doc608 typed
rule-family dispatch, non-current frontier metadata, the global accepted edge
graph, accepted atom/invariant payload records, frontier `deltas`/`witnesses`
provenance payloads, and the remaining frontier control plane; or prove that
every such addition is synthetic duplication, name lookup, stem retuning, class
collapse, or a doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_control_plane_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONTROLPLANEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONTROLPLANEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the section sizes, absence of exact residual labels and broad residual tokens,
absence of exact residual surface strings, the generic-token control-plane
profile, and separation from the doc-620 rejected/excluded ledger.
