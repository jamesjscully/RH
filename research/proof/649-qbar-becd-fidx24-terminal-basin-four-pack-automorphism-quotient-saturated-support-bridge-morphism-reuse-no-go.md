# 649 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Automorphism-Quotient-Saturated-Support-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by passing to
the orbit quotient, homotopy quotient, or descent category of the current
four-pack symmetry and recovering

```text
external_basin
oracle_basin
```

as a quotient-side equalizer, fiber, fixed locus, or saturated subobject.

The named mechanism is **terminal-basin four-pack automorphism-quotient
saturated-support collapse**.

## Setup

Doc 648 kills invariant or central idempotent reuse. The next categorical
repair is quotient-shaped: instead of selecting an invariant idempotent inside
the current category, pass to the quotient by the current four-pack symmetry
and try to define the desired pair there by a universal construction.

Any support that descends from the quotient pulls back to a saturated support
for the automorphism action. Thus the question is whether the desired pair is
saturated under the current non-attachment structure.

## Obstruction

The current non-attachment graph/signature data gives one four-pack orbit:

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

The full ten-vertex terminal-basin kernel component has seven quotient orbits:
six fixed singleton vertices plus this one four-pack orbit.

Therefore any quotient-side support pulls back to a saturated support. Its
intersection with the four-pack is either

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

The target pair is not saturated:

```text
saturation({external_basin, oracle_basin})
  = {external_basin, oracle_basin, noncanonical_basin, retuned_basin}
```

The quotient image of the target pair is the same as the quotient image of the
whole four-pack. No quotient-side equalizer, fiber, fixed locus, or subobject
can pull back to exactly `external_basin/oracle_basin`.

## Consequence

The surviving categorical route cannot repair doc 614 by quotienting the
current symmetry and then applying a universal construction on the quotient.
The quotient erases the target-pair distinction rather than making it
canonical.

This operation cannot be merely:

```text
orbit quotient of the current four-pack symmetry
homotopy quotient of the current four-pack symmetry
descent support from the current quotient
quotient-side equalizer or fiber
fixed locus after quotienting
saturated subobject pulled back from the quotient
```

A future route must add carrier-native structure that breaks the four-pack
before quotient/descent is taken, or it must prove that the quotient itself is
not the current `S4`-symmetric one.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_automorphism_quotient_saturated_support_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKAUTOQUOTSATSUPPORTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKAUTOQUOTSATSUPPORTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
four-pack, descent through a single four-pack orbit, the seven-orbit quotient
of the ten-vertex kernel component, saturation of the target pair to the whole
four-pack, equality between quotient-side saturated supports and invariant
vertex supports, equality of the target-pair and whole-four-pack quotient
images, and final collapse of automorphism-quotient/descent/equalizer support
reuse.
