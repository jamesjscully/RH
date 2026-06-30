# 648 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Automorphism-Invariant-Central-Idempotent-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by taking
automorphism-invariant, central, trace-invariant, or averaged idempotent data
from the current unital path/Karoubi category and using it to canonically
select

```text
external_basin
oracle_basin
```

inside the four-pack.

The named mechanism is **terminal-basin four-pack automorphism-invariant
central-idempotent collapse**.

## Setup

Doc 647 shows that the unital path category or Karoubi envelope makes the
desired rank-two vertex-idempotent sum available only extensionally. It is one
of six symmetric rank-two supports inside

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

The next categorical repair is to restore canonicity by passing to invariant
or central data: take the center, take an automorphism-invariant projector,
take a trace-invariant support, or average the target-pair projector over the
symmetry group.

## Obstruction

The current non-attachment graph/signature structure has the full `S4`
symmetry on the four-pack, with all other terminal-basin kernel-component
vertices fixed. Therefore the four-pack is one orbit.

Any canonical vertex-idempotent support built from the current category and
invariant under this action can intersect the four-pack only as

```text
empty
```

or

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

It cannot intersect the four-pack exactly in

```text
external_basin
oracle_basin
```

The executable witness enumerates all invariant vertex supports in the
ten-vertex kernel component. There are `2^6 * 2 = 128`: the six fixed
non-four-pack vertices are arbitrary, while the four-pack contribution is
either absent or the whole four-pack.

The rank-two target-pair orbit is still all six rank-two supports. Averaging
the target pair over the 24 graph-preserving permutations gives equal
incidence count 12 on each four-pack vertex, i.e. half-weight on every
four-pack vertex rather than a rank-two selector.

## Consequence

The surviving route cannot recover canonicity by saying that the selected
idempotent is central, invariant, averaged, or trace-defined inside the current
category. Those operations remove the noncanonical choice only by erasing the
target-pair distinction.

This operation cannot be merely:

```text
center of the current unital path category
automorphism-invariant vertex-idempotent support
trace-invariant support
orbit average of e_external_basin + e_oracle_basin
central projector obtained from the current four-pack symmetry
```

A future categorical repair must add new carrier-native symmetry-breaking
structure before the invariant or central operation is taken.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_automorphism_invariant_central_idempotent_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKAUTOINVCENTRALIDEMPOTENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKAUTOINVCENTRALIDEMPOTENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
four-pack, full `S4` symmetry of current non-attachment graph/signature data,
single-orbit action on the four-pack, invariant support enumeration, absence
of an invariant support intersecting the four-pack in the target pair,
equal orbit-average incidence on all four vertices, and final collapse of
automorphism-invariant/central idempotent reuse.
