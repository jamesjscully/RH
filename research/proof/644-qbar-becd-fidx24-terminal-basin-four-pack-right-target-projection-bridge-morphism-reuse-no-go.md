# 644 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Right-Target-Projection-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by projecting
the doc-643 four-pack incidence rows to the right target nodes

```text
basin_not_absorbing
basin_not_extensional
```

after deleting the high-bad right nodes

```text
no_basin_certificate
unbounded_basin_search
```

The named mechanism is **terminal-basin four-pack right-target projection
collapse**.

## Setup

Doc 643 shows that full incidence rows cannot split the four-pack:

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

A stronger, more favorable repair is to grant a control-death-like projection
on the right side: remove the high-bad right neighbors and keep only the
right target nodes. If current incidence already encoded the missing
composition operation, this projected incidence should distinguish
`external_basin/oracle_basin`.

## Obstruction

Before projection, every four-pack surface is bidirectionally incident to both
right target nodes:

```text
basin_not_absorbing
basin_not_extensional
```

and to both high-bad nodes:

```text
no_basin_certificate
unbounded_basin_search
```

After deleting the high-bad nodes, every four-pack surface still has the same
projected outgoing and incoming row:

```text
basin_not_absorbing
basin_not_extensional
```

Thus the right-target projection selects the whole four-pack:

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

not the target pair:

```text
external_basin
oracle_basin
```

No subprojection to one or both right target nodes, in either outgoing,
incoming, or bidirectional form, selects the target pair.

## Consequence

Current data still does not supply a control-death or composition map. Even
granting the best possible current-data deletion of high-bad right nodes, the
projected incidence remains too coarse. A surviving route must add a genuine
operation that makes `external_basin/oracle_basin` compose differently from
`noncanonical_basin/retuned_basin`.

This operation cannot be merely:

```text
current incidence row
current incidence row with high-bad nodes removed
current incidence row projected to right target nodes
```

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_right_target_projection_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKRIGHTTARGETPROJBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKRIGHTTARGETPROJBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
doc-643 four-pack, complete bidirectional incidence to both right target and
high-bad nodes, whole-four-pack support after right-target projection,
whole-four-pack support after high-bad projection, singleton projected row
profiles, and absence of any right-target subprojection selector for
`external_basin/oracle_basin`.
