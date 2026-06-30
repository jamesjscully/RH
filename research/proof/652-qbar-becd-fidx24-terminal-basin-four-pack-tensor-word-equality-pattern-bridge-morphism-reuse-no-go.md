# 652 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Tensor-Word-Equality-Pattern-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by applying
finite tensor-word functors to the current four-pack representation and then
using equality-pattern, diagonal/off-diagonal, symmetric-relation, or
finite-word orbit data to select

```text
external_basin
oracle_basin
```

The named mechanism is **terminal-basin four-pack tensor-word equality-pattern
collapse**.

## Setup

Doc 651 kills exterior/pair character projectors. The next functorial repair
is broader: use tensor words in the current four-pack action and look for a
pattern-level selector. This includes ordered pairs, repeated words,
diagonals, off-diagonals, symmetric relation predicates, and finite
tensor-word orbit data.

The current non-attachment structure gives full `S4` symmetry on

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

before tensor-word functors are applied.

## Obstruction

For word lengths 1 through 4, the `S4` orbits are exactly equality patterns.
The orbit counts are the Bell numbers:

```text
length 1: 1
length 2: 2
length 3: 5
length 4: 15
```

The ordered target word

```text
external_basin -> oracle_basin
```

has the equality pattern "two distinct entries." Its orbit is therefore the
whole ordered-distinct-pair orbit of size 12. Even including both orientations,

```text
external_basin -> oracle_basin
oracle_basin -> external_basin
```

saturates to all ordered distinct pairs.

More generally, every checked tensor word of length at most 4 saturates
exactly to its equality-pattern support. Tensoring the current four-pack
therefore remembers only which positions are equal, not which positions are
`external_basin` and `oracle_basin`.

## Consequence

The surviving route cannot repair the four-pack collapse by applying finite
tensor-word functors to the current action and then selecting by equality
patterns or finite orbit relations. Those constructions are still downstream
of the same `S4` symmetry.

This operation cannot be merely:

```text
ordered-pair tensor word
finite tensor power of the current four-pack
diagonal/off-diagonal tensor relation
equality-pattern predicate
symmetric relation on current tensor words
finite word-orbit selector
```

A future route must add carrier-native structure that names or constructs the
external/oracle distinction before tensor-word functors are applied.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_tensor_word_equality_pattern_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKTENSORWORDEQPATTERNBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKTENSORWORDEQPATTERNBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
four-pack, full `S4` symmetry before tensor-word functors, Bell-number orbit
counts for lengths 1 through 4, equality between word orbits and
equality-pattern supports, saturation of the ordered external/oracle word to
all ordered distinct pairs, saturation of both target orientations to the same
orbit, and final collapse of tensor-word equality-pattern reuse.
