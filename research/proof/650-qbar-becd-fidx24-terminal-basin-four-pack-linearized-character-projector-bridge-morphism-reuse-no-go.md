# 650 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Linearized-Character-Projector-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by linearizing
the current four-pack symmetry and using an automorphism character,
orientation, trace, or central group-algebra projector to select

```text
external_basin
oracle_basin
```

The named mechanism is **terminal-basin four-pack linearized character-projector
collapse**.

## Setup

Doc 649 kills quotient/descent saturated-support reuse. The next categorical
repair is representation-theoretic: pass from vertex supports to the vector
space on the four-pack, then use character projectors or central idempotents
of the current automorphism action. This allows more than Boolean supports, so
it must be checked separately.

The current non-attachment structure gives the full `S4` permutation action on
the four-pack:

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

## Obstruction

In the four-point permutation representation, the `S4`-equivariant commutant
has only two parameters: one diagonal value and one off-diagonal value. Its
idempotents are forced to be:

```text
0
all-ones-line projector
standard-complement projector
identity
```

Their ranks are:

```text
0, 1, 3, 4
```

The desired coordinate projector onto

```text
external_basin
oracle_basin
```

has rank 2, but it is not `S4`-equivariant. Its orbit has the same six
rank-two choices already seen in doc 647.

The trivial character projector is the all-ones line. The sign/orientation
projector is zero in this permutation module. Thus orientation or character
language does not recover the missing rank-two selector.

## Consequence

The surviving route cannot repair the current four-pack collapse by
linearizing the same symmetry and applying character theory afterward.
Central projectors of the current action are too coarse, and the rank-two
projector is precisely the noncanonical choice.

This operation cannot be merely:

```text
linearized current four-pack action
central group-algebra idempotent
character projector
trace projector
orientation/sign projector
standard/trivial representation split
```

A future route must add new carrier-native symmetry-breaking data before
linearization or character projection is applied.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_linearized_character_projector_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKLINCHARPROJECTORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKLINCHARPROJECTORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
four-pack, full `S4` permutation representation on current non-attachment
data, exact central idempotent ranks `0,1,3,4`, non-equivariance and six-choice
orbit of the rank-two target projector, zero sign/orientation projector,
constant diagonal profiles of central projectors, and final collapse of
linearized character-projector reuse.
