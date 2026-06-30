# 640 - Qbar_BECD FIdx24 Terminal-Basin-Low-Profile-Automorphism-Orbit-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by treating
`external_basin` and `oracle_basin` as a canonical graph-symmetry pair inside
the terminal-basin kernel graph.

The named mechanism is **terminal-basin low-profile automorphism-orbit
collapse**.

## Setup

Docs 637-639 reduce the surviving left-endpoint question to the low graph
profile:

```text
(out,in,total,undirected,eccentricity,distance_sum) = (4,4,8,4,2,14)
```

This profile contains six terminal-basin surfaces:

```text
external_basin
oracle_basin
branch_spawning_basin
noncanonical_basin
proof_irrelevant_basin
retuned_basin
```

Tail shape and valence do not produce a positive separator. The next
nonlexical repair is to use symmetry: perhaps `external_basin` and
`oracle_basin` form a canonical orbit, twin pair, or invariant two-point
subobject in the kernel graph.

## Obstruction

The directed graph induced on the six low-profile vertices has no internal
edges:

```text
low_profile_internal_edges = 0
```

Consequently its internal automorphism group is the full symmetric group:

```text
|Aut(low_profile_induced_graph)| = 6! = 720
```

The full ten-surface terminal-basin kernel graph has three automorphism
orbits:

```text
low profile:
  six surfaces

middle profile:
  basin_not_absorbing
  basin_not_extensional

high bad profile:
  no_basin_certificate
  unbounded_basin_search
```

The graph automorphism count is:

```text
6! * 2! * 2! = 2880
```

Within that full graph, the orbit of the target pair

```text
{external_basin, oracle_basin}
```

is every two-element subset of the low-profile component:

```text
15 pairs
```

The setwise stabilizer of the chosen pair has size `192`, so selecting the
pair is exactly a choice among those 15 possible low-profile pairs. The graph
does not force that choice.

The six low-profile vertices also have identical directed neighborhood
fingerprints in the full kernel graph. There is no hidden neighbor-asymmetry
that distinguishes the `external/oracle` pair.

## Consequence

Graph symmetry does not construct the missing separator. It makes the
problem worse: the current kernel graph is maximally symmetric on the
low-profile component, and the desired pair is just one of 15 equivalent
pairs until attachment-token or defect-vocabulary information is reintroduced.

A surviving route must add a real proof-relevant map or law whose action
breaks this symmetry in a carrier-native way: boundary map, composition law,
endpoint degree map, DD.4 boundary, graph/composition operation, Rosati datum,
or control-death mechanism. The current terminal-basin kernel graph supplies
none of that.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_automorphism_orbit_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILEAUTORBITBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILEAUTORBITBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the three
kernel-graph profile blocks, zero low-profile internal edges, the `6!`
low-profile automorphism count, the `2880` full kernel-graph automorphism
count, the 15-pair orbit of `{external_basin, oracle_basin}`, the 192-element
setwise stabilizer, and identical low-profile neighborhood fingerprints.
