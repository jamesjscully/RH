# 159 - PFV2 carrier torsor formability collapse

Status: bounded no-go from the PFV2-TOR-CARRIER target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only
carrier-torsor proposals whose native band/groupoid is functorial for
broad local-shadow data and therefore formable by controls.

## 1. Purpose

Doc 158 writes the smallest native torsor source record:

```text
PFV2-NATIVE-TOR(p,q).
```

The decisive new field is:

```text
G_car
```

a carrier-native band, extension group, or automorphism/coherence
groupoid. Without such a field, the torsor class is decorative. With a
broadly functorial such field, the class is control-formable.

This document applies the control-formability kill condition to the
broad functorial class.

## 2. Covered Class

Call a proposal `PFV2_CAR_TOR_broad` if it satisfies all of:

```text
D159.1 native slot
  The proposal names a pre-assembly band, extension group, action
  groupoid, automorphism groupoid, cocycle category, or coherence
  groupoid G_car, with a class tau_car.

D159.2 broad functoriality
  The same construction of G_car and tau_car is functorial for any
  object with comparable local pieces, p,q marking, descent diagrams,
  theta/count shadows, or ordinary assembled object D plus labels.

D159.3 no Euler-only operation
  The definition of G_car uses only categorical gluing, local
  compatibility, automorphism/coherence data, ordinary cohomology, or
  torsors of choices. It does not use a named Euler-carrier operation
  unavailable to Epstein/DH controls.

D159.4 inherited first map
  kappa_car is a natural map of the broad construction, or factors
  through the assembled object plus the broad torsor label.

D159.5 shadow preservation
  Epstein represented-norm data or DH coefficient/measure shadows can
  carry the same G_car, tau_car, and kappa_car while retaining their
  theta/count shadows.
```

This class includes:

```text
torsors of compatible local trivializations;
extension groupoids of generic descent diagrams;
cocycle categories attached to p,q-marked all-places objects;
automorphism groupoids of local-shadow diagrams;
coherence torsors for diagrams controls can also instantiate;
ordinary cohomology bands functorial in D or in local pieces.
```

## 3. Lemma

### Lemma 159.1

`PFV2_CAR_TOR_broad` does not satisfy PFV2-TOR-CARRIER.

Verdict:

```text
REJECT_BROAD_CARRIER_TOR
  if G_car and tau_car are functorial for broad local-shadow objects.

REJECT_CONTROL_FORMABLE_TOR
  if Epstein/DH controls can form the same G_car, tau_car, and
  kappa_car while preserving theta/count shadows.

REJECT_INHERITED_KAPPA_CAR
  if kappa_car is just the natural map of the broad torsor construction
  or factors through D plus a label.

HOLD_EULER_NATIVE_BAND
  if a later proposal names an Euler-carrier operation defining G_car
  that controls cannot instantiate.
```

### Proof

PFV2-TOR-CARRIER requires more than a pre-assembly slot for torsor
data. It requires a named carrier-native band or groupoid whose
formation is unavailable to controls.

Under D159.1-D159.2, the same `G_car` and `tau_car` are defined for a
broad class of local-shadow objects. Thus the torsor is native only in
the weak sense that it is placed before assembly; it is not native to
the Euler carrier.

Under D159.3, no operation distinguishes the PFV2 carrier from
Epstein/DH shadows. The construction may be useful category theory,
but it does not create the source selectivity demanded by docs 130,
135, and 158.

Under D159.4, the proposed first map is inherited from the broad
construction or from `D` plus a label. That is not a carrier-consuming
first map.

Under D159.5, the controls can form the same data while retaining their
theta/count shadows. This directly violates the control
non-formability gate of doc 158.

Therefore broad functorial carrier-torsor packages do not satisfy
PFV2-TOR-CARRIER. QED.

## 4. What The Broad Class Still Supplies

Allowed:

```text
language for naming bands, groupoids, torsors, and cocycles;
comparison tests for proposed Euler-native bands;
negative calibration objects for external questions;
post-pass compatibility diagnostics if a stricter source is later
constructed.
```

Not allowed:

```text
claiming FIRST_MAP_PASS;
claiming PFV2-TOR-CARRIER;
claiming control exclusion;
using functoriality in local pieces as evidence of Euler-carrier
nativity;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 torsor route is:

```text
PFV2-TOR-EULER-BAND.
```

The target:

```text
There is a named Euler-carrier band, extension group, action groupoid,
automorphism/coherence groupoid, or cocycle category G_E such that:

1. G_E is defined from TorDesc_{p,q} before all-places assembly;
2. defining G_E uses an Euler-carrier operation not available to
   Epstein/DH controls while their theta/count shadows remain intact;
3. tau_E is a G_E-torsor, extension, cocycle, or coherence class;
4. kappa_E changes when tau_E changes while D, p,q marking, and
   complement bookkeeping are held fixed;
5. B0_p and B0_q embed conservatively before tau_E is consumed;
6. tau_E remains load-bearing downstream in M_C/F_C/Tr_L.
```

This is narrower than PFV2-TOR-CARRIER. It does not ask for any
carrier-native band; it asks for an Euler-carrier band whose defining
operation fails for controls before trace, sign, regularization,
positivity, or zero comparison.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `G_E, tau_E` proposal if
one proves:

```text
KILL-EULER-BAND.1 no Euler operation
  G_E is definable using only broad categorical gluing, ordinary
  cohomology, automorphism/coherence data, local pieces, or D plus
  labels.

KILL-EULER-BAND.2 control transport
  the defining operation for G_E transports to Epstein/DH shadows while
  preserving theta/count shadows.

KILL-EULER-BAND.3 inherited first map
  kappa_E factors through D plus an inert torsor label or through a
  broad functorial torsor construction.

KILL-EULER-BAND.4 bank replacement
  G_E or tau_E requires replacing B0_p/B0_q by the full global source.

KILL-EULER-BAND.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_E or sees it only as an inert
  label.
```

Do not apply these to all PFV2 source attempts without a theorem
covering their proposed Euler-carrier operation.

## 7. Board Update

```text
PFV2_CAR_TOR_broad:
  REJECT_BROAD_CARRIER_TOR;
  REJECT_CONTROL_FORMABLE_TOR.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-TOR-EULER-BAND or another source whose
  carrier-native operation is unavailable to controls.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 158
  Supplies PFV2-NATIVE-TOR(p,q) and the PFV2-TOR-CARRIER target.

doc 157
  Rejects decorative torsors.

doc 156
  Supplies the torsor/extension/cocycle residual shot.

doc 153
  Supplies the residual descent source slot.

doc 135
  Rejects coordinate-pair source labels.

doc 130
  Supplies the A2 kill routes.

doc 103
  Still HOLD: no FIRST_MAP_PASS.
```
