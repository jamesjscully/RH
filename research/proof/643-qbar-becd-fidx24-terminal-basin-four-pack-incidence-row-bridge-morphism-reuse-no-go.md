# 643 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Incidence-Row-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by using the
current terminal-basin kernel incidence rows as the missing composition-like
operation on the four-pack

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

The named mechanism is **terminal-basin four-pack incidence-row collapse**.

## Setup

Doc 642 leaves the four-pack problem after doc-610 signature-token reuse is
removed. The next operation-shaped repair is to read the directed kernel
incidence rows and columns as a proxy for composition:

```text
surface -> right-side terminal-basin nodes
right-side terminal-basin nodes -> surface
```

If this current graph already encoded the missing composition map, the target
pair should have a different row or column from `noncanonical_basin` and
`retuned_basin`.

## Obstruction

All four surfaces have the same outgoing neighbors:

```text
basin_not_absorbing
basin_not_extensional
no_basin_certificate
unbounded_basin_search
```

and the same incoming neighbors:

```text
basin_not_absorbing
basin_not_extensional
no_basin_certificate
unbounded_basin_search
```

There are no internal directed edges among the four-pack:

```text
four_pack_internal_edges = 0
```

The incidence between the four-pack and the right-side four nodes is complete
and bidirectional. Therefore every outgoing-neighbor or incoming-neighbor
subset selector either selects the whole four-pack or nothing; none selects

```text
external_basin
oracle_basin
```

Every unordered pair inside the four-pack has the same incidence signature:

```text
direct edge left->right: false
direct edge right->left: false
common outgoing neighbors: 4
common incoming neighbors: 4
```

## Consequence

The current kernel graph does not hide a composition row that separates the
target pair. It treats

```text
external_basin / oracle_basin
```

and

```text
noncanonical_basin / retuned_basin
```

identically as incidence rows and columns. A surviving categorical route must
add a new operation: an actual boundary map, composition law, endpoint-degree
map, DD.4 boundary operation, graph/composition datum, Rosati datum, or
control-death mechanism. It cannot reuse the current kernel incidence table
as that operation.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_incidence_row_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKINCIDENCEROWBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKINCIDENCEROWBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
doc-642 four-pack, identical outgoing rows, identical incoming columns, zero
internal four-pack edges, complete bidirectional incidence to the right-side
nodes, absence of neighbor-subset selectors for the target pair, and identical
pairwise incidence signatures inside the four-pack.
