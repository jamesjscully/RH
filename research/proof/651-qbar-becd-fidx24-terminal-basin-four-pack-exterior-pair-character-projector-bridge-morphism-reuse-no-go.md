# 651 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Exterior-Pair-Character-Projector-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by passing from
the four-pack vertex representation to pair space, exterior square, or the
six-dimensional representation on two-element subsets, and then using a
central character projector to select

```text
external_basin
oracle_basin
```

The named mechanism is **terminal-basin four-pack exterior-pair
character-projector collapse**.

## Setup

Doc 650 kills character projectors on the linearized four-pack vertex space.
There is a sharper representation-theoretic escape: the `S4` action on the
six two-element subsets has a genuine rank-two central summand. Since the
desired support has cardinality two, this rank coincidence could be mistaken
for the missing selector.

The six pair-basis elements are all two-element subsets of

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

and `S4` acts transitively on them.

## Obstruction

The central idempotents in the pair-space representation have ranks

```text
0, 1, 2, 3, 3, 4, 5, 6
```

So a canonical rank-two projector really exists. But it is not the target-pair
coordinate projector. Its diagonal profile is uniform:

```text
1/3, 1/3, 1/3, 1/3, 1/3, 1/3
```

across all six pair-basis elements.

The actual coordinate projector onto

```text
{external_basin, oracle_basin}
```

has rank 1 in pair space, is not `S4`-equivariant, and has a six-choice orbit.
Thus the rank-two central summand is representation-theoretic structure of
the orbit, not a carrier-native selection of the target pair.

## Consequence

The surviving route cannot repair the four-pack collapse by moving to
`Lambda^2`, pair space, two-subset permutation modules, or higher character
language and pointing to the canonical rank-two summand. That summand is
uniform over the whole pair orbit.

This operation cannot be merely:

```text
pair-space representation of the current four-pack
exterior-square representation of the current four-pack
two-subset orbit representation
rank-two central summand of the pair representation
Johnson/Kneser association-scheme projector
```

A future route must add carrier-native structure that distinguishes the
specific pair before pair-space or exterior-square character projectors are
taken.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_exterior_pair_character_projector_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKEXTPAIRCHARPROJECTORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKEXTPAIRCHARPROJECTORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
four-pack, transitive `S4` action on all six two-subsets, exact central
pair-projector ranks, uniform diagonal of the rank-two pair-space projector,
non-equivariance and six-choice orbit of the actual target-pair coordinate,
and final collapse of exterior/pair character-projector reuse.
