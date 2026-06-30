# 647 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Unital-Path-Idempotent-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by passing from
the current terminal-basin incidence graph to its unital path category or
Karoubi envelope and selecting the rank-two vertex-idempotent sum

```text
e_external_basin + e_oracle_basin
```

The named mechanism is **terminal-basin four-pack unital path-idempotent
choice collapse**.

## Setup

Doc 646 kills positive-length path-power composition reuse. A categorical
escape remains: add identities. Once identities exist, every vertex has an
idempotent, and every subset of vertices has an idempotent sum. The desired
target pair is therefore present extensionally as a rank-two idempotent
support.

This is not enough. The question is whether the current structure canonically
selects that support without attachment-token lookup.

## Obstruction

The four-pack remains symmetric after all current non-attachment structure is
kept:

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

All four have the same incidence rows and columns, the same positive path-power
readouts, and the same non-attachment doc-610 signature skeleton. With the
other terminal-basin vertices fixed, all 24 permutations of the four-pack
preserve the current kernel-pair graph.

The target rank-two idempotent support

```text
{external_basin, oracle_basin}
```

has orbit equal to all six rank-two supports inside the four-pack. Thus the
desired idempotent sum is one of six indistinguishable choices:

```text
choose 2 of 4 = 6
```

The only current selector for the desired support is the already-killed
external/oracle attachment-token selector.

## Consequence

The surviving categorical route cannot be merely:

```text
unital path category of the current graph
Karoubi envelope of the current graph
rank-two vertex-idempotent sum
projection onto a chosen two-object summand
```

unless it also supplies new carrier-native structure that breaks the four-pack
symmetry. A vertex idempotent is available only because identities name every
vertex; the current category does not prove why the `external_basin/oracle_basin`
sum is the required one.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_unital_path_idempotent_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKUNITALPATHIDEMPOTENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKUNITALPATHIDEMPOTENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
four-pack, symmetry of incidence/path-power/polynomial readouts,
non-attachment signature-skeleton equality, all 24 graph-preserving
permutations of the four-pack, the six-element orbit of the target pair among
rank-two idempotent supports, and final collapse of unital path-idempotent
reuse.
