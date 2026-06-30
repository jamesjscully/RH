# 646 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Path-Power-Composition-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by iterating the
current terminal-basin kernel incidence relation and reading positive-length
path powers as the missing composition map on the four-pack

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

The named mechanism is **terminal-basin four-pack path-power composition
collapse**.

## Setup

Doc 645 kills endpoint-degree, boundary, signed, total, projected, and weighted
linear readouts of the current incidence table. The next stronger repair is
composition-shaped: perhaps the first incidence rows are too coarse, but
two-step, three-step, or higher positive-length paths through the current
terminal-basin kernel graph reveal a canonical split.

This tests positive-length adjacency powers of the current directed kernel
graph, not vertex idempotent lookup. If the current relation already encoded
the missing composition law, some path-power profile or positive adjacency
polynomial should distinguish

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

The four-pack has identical outgoing rows and identical incoming columns at
power one. Multiplying by the same adjacency matrix preserves this equality:
equal rows remain equal after right multiplication, and equal columns remain
equal after left multiplication.

The executable witness checks powers 1 through 7. For every checked positive
path length, all four surfaces have one row profile and one column profile.
The total path profiles are also constant:

```text
power 1: outgoing 4, incoming 4, signed 0
power 2: outgoing 34, incoming 34, signed 0
power 3: outgoing 182, incoming 182, signed 0
power 4: outgoing 1278, incoming 1278, signed 0
power 5: outgoing 7598, incoming 7598, signed 0
power 6: outgoing 49934, incoming 49934, signed 0
power 7: outgoing 308686, incoming 308686, signed 0
```

Right-target and high-bad projections of these path-power profiles are still
singleton profiles. Sample positive-length adjacency-polynomial readouts are
constant as well.

Thus iterating the current relation does not create the missing distinction.
It preserves the same four-pack collapse.

## Consequence

The surviving route cannot recover composition by repeatedly composing the
current doc-635 kernel pairs. A future categorical repair must add a new
carrier-native composition or boundary operation whose arrows are not merely
positive-length paths in the existing terminal-basin incidence graph.

This operation cannot be merely:

```text
A
A^2
A^3
positive-length polynomial in A
projected positive-length path counts
weighted positive-length path counts
```

where `A` is the current terminal-basin kernel adjacency matrix.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_path_power_composition_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKPATHPOWERCOMPOSITIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKPATHPOWERCOMPOSITIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
doc-643 four-pack, equality of power-one neighbors, equality of row and column
profiles for positive path powers 1 through 7, constant total/signed path
counts, constant right-target and high-bad projected path-power profiles,
constant sample positive adjacency-polynomial readouts, and final collapse of
current path-power composition reuse.
