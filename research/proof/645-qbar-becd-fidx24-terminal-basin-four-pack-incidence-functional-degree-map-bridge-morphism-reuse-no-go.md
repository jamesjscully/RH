# 645 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Incidence-Functional-Degree-Map-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by promoting any
weighted endpoint-degree, boundary, signed, total, or projected linear
functional of the current terminal-basin incidence table to the missing map on
the four-pack

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

The named mechanism is **terminal-basin four-pack incidence-functional
degree-map collapse**.

## Setup

Doc 643 kills direct reuse of the full four-pack incidence rows. Doc 644 kills
the favorable projection to right target nodes after deleting the high-bad
nodes. The next broader repair is to treat endpoint-degree, boundary,
control-death, or signed degree as a functional of the same incidence table:
count outgoing edges, count incoming edges, take total incidence, take signed
incidence, restrict to target/high-bad projections, or apply weights.

If the current incidence table already encoded the missing categorical map,
one of these readouts should split

```text
external_basin
oracle_basin
```

from

```text
noncanonical_basin
retuned_basin
```

without attachment-token lookup.

## Obstruction

The four-pack has identical incidence vectors over the current terminal-basin
kernel component. For every four-pack surface, the outgoing and incoming
neighbors are the same four right-side nodes:

```text
basin_not_absorbing
basin_not_extensional
no_basin_certificate
unbounded_basin_search
```

Consequently:

```text
outgoing incidence vector = constant on the four-pack
incoming incidence vector = constant on the four-pack
total incidence vector    = constant on the four-pack
signed incidence vector   = zero on the four-pack
```

The right-target projection and the high-bad projection both have singleton
row profiles, and both projections still support the whole four-pack. Applying
weights to the current incidence columns does not change the result: a linear
functional takes the same value on all four surfaces whenever the input vector
is the same.

Thus no endpoint-degree, boundary-degree, signed-degree, total-degree, or
projected weighted readout of the current incidence table selects
`external_basin/oracle_basin`.

## Consequence

The surviving route cannot recover the missing object by reinterpreting the
current terminal-basin incidence table as a degree map. A future categorical
repair must add carrier-native degree or boundary data, or a new composition
law, rather than extracting it from the existing rows and columns.

This operation cannot be merely:

```text
current outgoing incidence row
current incoming incidence column
current total incidence
current signed incidence
weighted current incidence
right-target projected incidence
high-bad projected incidence
```

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_incidence_functional_degree_map_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKINCFUNCDEGMAPBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKINCFUNCDEGMAPBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
doc-643 four-pack, equality of full outgoing/incoming/total/signed incidence
vectors, equality after right-side projection, equality after high-bad
projection, constant sample weighted functionals, and the final collapse of
current-incidence linear degree-map reuse.
