# 638 - Qbar_BECD FIdx24 Terminal-Basin-Low-Profile-Tail-Shape-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by using
tail-shape or suffix structure inside the low graph-profile terminal-basin
component to select `external_basin` and `oracle_basin`.

The named mechanism is **terminal-basin low-profile tail-shape selector
collapse**.

## Setup

Doc 637 shows that the terminal-basin kernel graph has a low mixed profile:

```text
(out,in,total,undirected,eccentricity,distance_sum) = (4,4,8,4,2,14)
```

This profile contains two target endpoints:

```text
external_basin
oracle_basin
```

and four bad labels:

```text
branch_spawning_basin
noncanonical_basin
proof_irrelevant_basin
retuned_basin
```

The next positive-looking repair is to use tail shape: suffix `basin`,
two-segment basin tails, or other arity/suffix structure.

## Obstruction

Suffix and segment data are too broad:

```text
suffix=basin:
  all six low-profile surfaces

segment=basin:
  all six low-profile surfaces
```

Tail arity also fails:

```text
tail_length=2:
  external_basin
  oracle_basin
  noncanonical_basin
  retuned_basin

tail_length=3:
  branch_spawning_basin
  proof_irrelevant_basin
```

No conjunction of structural tail-shape features

```text
boundary=escape
event_kind=plain_tail
segment=basin
suffix=basin
tail_length=2 or 3
```

selects exactly `external_basin` and `oracle_basin`. The only exact positive
selector is again the residual attachment-token pair:

```text
external / oracle
```

That is not internal terminal-basin structure. It is the left attachment data
from docs 633-637.

## Consequence

The low-profile bad labels cannot be separated from the left target endpoints
by suffix or tail arity. A surviving route must add positive structure beyond
the current doc610 tail shape, such as an actual boundary map or composition
law that distinguishes external/oracle basin entry from noncanonical and
retuned basin labels without just using the `external/oracle` attachment
tokens.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_tail_shape_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILETAILSHAPEBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILETAILSHAPEBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the six
low-profile surfaces, the suffix/segment-basin support, tail-length support,
absence of structural tail-shape selectors, and fallback to the
`external/oracle` attachment tokens.
