# 637 - Qbar_BECD FIdx24 Terminal-Basin-Quotient-Graph-Invariant-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by using graph
degree or centrality inside the doc-635 terminal-basin kernel quotient graph
to select the four target endpoints.

The named mechanism is **terminal-basin quotient-graph invariant collapse**.

## Setup

Doc 636 kills failure-label complement filtering. The next positive-looking
repair is graph-internal: use the directed kernel-pair graph or its undirected
quotient component to separate target endpoints from failure labels.

For each surface in the ten-surface kernel component, measure:

```text
out_degree, in_degree, total_degree, undirected_degree,
eccentricity, distance_sum
```

## Obstruction

The graph has three full profiles:

```text
(4,4,8,4,2,14):  six surfaces
(8,8,16,8,2,10): two surfaces
(9,9,18,9,1,9): two surfaces
```

The two left target endpoints

```text
external_basin
oracle_basin
```

have profile `(4,4,8,4,2,14)`, but so do four bad labels:

```text
branch_spawning_basin
noncanonical_basin
proof_irrelevant_basin
retuned_basin
```

The only target-pure profile is `(8,8,16,8,2,10)`, and it selects only the
two not-side endpoints:

```text
basin_not_absorbing
basin_not_extensional
```

The highest-centrality profile is bad:

```text
(9,9,18,9,1,9):
  no_basin_certificate
  unbounded_basin_search
```

No single graph-invariant value selects all four target endpoints, and no
union of full graph profiles selects exactly the target set. The total-degree
partition is:

```text
8:  low mixed profile, with two targets and four bad labels
16: partial target profile, with only the two not-side endpoints
18: high bad profile, with no_basin_certificate and unbounded_basin_search
```

## Consequence

The terminal-basin kernel graph contains useful diagnostics, but its internal
degree/centrality data does not construct the missing morphism. A surviving
route must add positive structure not already present in the kernel graph:
something that separates `external_basin` and `oracle_basin` from the four
low-profile bad labels while also keeping the not-side endpoints.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_quotient_graph_invariant_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINQUOTGRAPHINVBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINQUOTGRAPHINVBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
58-edge terminal-basin kernel graph, the three graph profiles, the low mixed
profile containing the left target endpoints and four bad labels, the
partial-target middle profile, the high bad profile, and the absence of any
single invariant value or profile union selecting all target endpoints.
