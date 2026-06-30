# 641 - Qbar_BECD FIdx24 Terminal-Basin-Profile-Tail-Product-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by combining
the terminal-basin kernel graph profile with structural tail-shape data.

The named mechanism is **terminal-basin profile-tail product selector
collapse**.

## Setup

Docs 637 and 638 kill the two single-axis selectors:

```text
graph profile alone
tail shape alone
```

Doc 640 then shows that raw graph symmetry makes
`{external_basin, oracle_basin}` one of 15 equivalent low-profile pairs.
The next natural repair is to multiply the available invariants: use the
kernel graph profile together with structural shape features:

```text
boundary kind
event kind
segment basin
suffix
tail length
```

## Obstruction

The product partition on the ten-surface terminal-basin kernel component has
six blocks:

```text
{external_basin, oracle_basin, noncanonical_basin, retuned_basin}
{branch_spawning_basin, proof_irrelevant_basin}
{basin_not_absorbing}
{basin_not_extensional}
{no_basin_certificate}
{unbounded_basin_search}
```

The desired left pair is not a product block. It sits in the four-element
block:

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

No union of graph-profile/tail-shape product blocks selects:

```text
external_basin
oracle_basin
```

and no union selects all four target endpoints:

```text
external_basin
oracle_basin
basin_not_absorbing
basin_not_extensional
```

The product-block-preserving kernel automorphism group has size:

```text
4! * 2! = 48
```

Within the four-element product block, the orbit of
`{external_basin, oracle_basin}` is all six two-element pairs. The product
invariant does not make that pair canonical.

The only exact cut inside the four-element block is again the attachment-token
selector:

```text
external / oracle
```

## Consequence

Combining current graph and tail data still does not construct the missing
separator. It refines the low-profile six-pack, but only to a four-pack that
still contains bad labels. A surviving route must add a genuinely new
proof-relevant operation whose action splits that four-pack without using
attachment-token lookup or defect-vocabulary exclusion.

In particular, the next live object cannot be just another product of the
current kernel graph profile and current doc610 tail-shape algebra. It has to
look like a new boundary map, composition law, endpoint-degree map, DD.4
boundary operation, Rosati datum, or control-death mechanism.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_profile_tail_product_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINPROFILETAILPRODUCTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINPROFILETAILPRODUCTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the graph
profile blocks, the six-block graph-profile/tail-shape product partition, the
four-element mixed block containing the left targets, failure of all product
block unions to select the target endpoints, the 48-element product-block
automorphism group, the six-pair orbit inside the four-element block, and the
continued dependence on `external/oracle` attachment-token selection.
