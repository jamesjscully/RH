# 653 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Signed-Exterior-Orientation-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by using the
signed exterior square of the current four-pack representation and treating

```text
e_external_basin wedge e_oracle_basin
```

as an orientation line or signed exterior selector.

The named mechanism is **terminal-basin four-pack signed-exterior orientation
collapse**.

## Setup

Doc 651 kills unsigned pair-space character projectors, and doc 652 kills
finite tensor-word equality-pattern reuse. A remaining representation-theoretic
escape is to use the actual signed exterior square. This is distinct from
unsigned two-subset space because permutations can act with signs.

The current non-attachment structure still gives the full `S4` action on

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

before the signed exterior square is formed.

## Obstruction

The signed `Lambda^2(Q^4)` representation decomposes into two rank-three
central summands. Its central idempotent ranks are:

```text
0, 3, 3, 6
```

The trivial character projector is zero, and the sign/orientation character
projector is also zero. There is no canonical orientation line inside this
representation.

The two rank-three summands each have uniform half diagonal on all six wedge
basis lines. The actual coordinate line

```text
e_external_basin wedge e_oracle_basin
```

has rank 1, is not `S4`-equivariant, and has a six-choice orbit.

## Consequence

The surviving route cannot recover the target pair by replacing pair-space
with signed exterior orientation. The signed exterior square still sees only
current `S4` representation structure, not a carrier-native distinction of
`external_basin/oracle_basin`.

This operation cannot be merely:

```text
signed Lambda^2 of the current four-pack
orientation line in the current four-pack
sign character projector
signed wedge coordinate e_external_basin wedge e_oracle_basin
rank-three signed wedge summand
```

A future route must add carrier-native symmetry-breaking before exterior
orientation is formed.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signed_exterior_orientation_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKSIGNEDEXTERIORORIENTATIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKSIGNEDEXTERIORORIENTATIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
four-pack, full signed `S4` wedge action, vanishing trivial and sign/orientation
projectors, exact central signed-wedge ranks `0,3,3,6`, uniform half diagonals
on the two rank-three signed wedge summands, non-equivariance and six-choice
orbit of the target wedge line, and final collapse of signed exterior
orientation reuse.
