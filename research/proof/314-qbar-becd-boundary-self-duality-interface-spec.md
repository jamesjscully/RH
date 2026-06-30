# 314 - Qbar_BECD boundary self-duality interface

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-seventy-seventh cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 313 left the live B proof at:

```text
carrier-fixed orientation + self-dual boundary/properness
```

for the oriented-Cartier boundary on `O+E`. This document sharpens the
self-duality/properness side. The boundary self-duality cannot be supplied by
an abstract hyperbolic endpoint plane, trace/End augmentation, positive Rosati
matrix envelope, projection forcing, or formal fiber-product saturation. Those
packages are Phase-B-shaped unless Qbar_BECD itself produces them as
carrier-native boundary data.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_self_duality_interface`
(BSD1-BSD7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_oriented_cartier_residual_sieve`,
`prime_int_n1b_hyperbolic_plane_rosati_no_go`,
`prime_int_n1b_trace_augmented_hyperbolic_no_go`,
`prime_int_n1b_end_augmented_hyperbolic_no_go`,
`prime_int_n1b_positive_rosati_end_envelope_no_go`,
`prime_int_n1b_projection_forced_positive_envelope_no_go`, and
`prime_int_n1b_fiber_product_saturated_positive_envelope_no_go`.

## 1. Purpose

The live Phase-A boundary contract is now narrow:

```text
oriented-Cartier shape on O+E
+ boundary-native self-dual properness.
```

Doc 312 supplied the local shape. Doc 313 rejected endpoint-coordinate
bookkeeping as the missing carrier proof. Docs 280-285 explain why the next
move is not to import a Rosati/End/projection envelope.

The missing datum must instead be intrinsic to the carrier boundary. It must
fix the oriented-Cartier representative, couple DD.4 killing to boundary
duality, preserve primary `p1,p2`, avoid Phase-B graph/projection imports,
preserve counts, and be non-formable on controls.

## 2. Lemma

```text
Lemma 314.1 (boundary self-duality interface).

Start from:

    O+E = carrier_object + endpoint_maps.

Shape-only oriented-Cartier boundary data gives:

    boundary-map shape,
    exact-localization shape,
    DD.4 zero-image shape,
    selected direction d1-d2.

It still represents only:

    carrier_object, endpoint_maps.

Adding boundary-native self-dual properness gives:

    carrier_object, endpoint_maps, DD.4_boundary_killing.

The following do not count as Phase-A boundary self-duality:

    hyperbolic endpoint plane:
      has a self-dual-looking endpoint plane but is not boundary-native,
      does not fix the oriented-Cartier representative, does not couple
      DD.4 to boundary duality, and remains formable on controls;

    trace-augmented or End-augmented hyperbolic envelope:
      imports a Phase-B graph/End slot before live B exists, leaves DD.4
      independent of boundary duality, and remains formable on controls;

    positive Rosati End envelope:
      is a Phase-B-shaped positivity package, not a carrier boundary source;

    projection-forced positive envelope:
      distorts counts and repeats projection-formula repair instead of
      producing boundary-native self-duality;

    fiber-product-saturated positive envelope:
      describes how Phase-B proper composition should behave only after Qbar
      supplies actual carrier cells.

Therefore the accepted Phase-A interface is exactly:

    boundary-native,
    orientation fixed,
    self-dual boundary/properness,
    p1,p2 primary,
    no Phase-B graph/projection import,
    count-preserving,
    DD.4 coupled to boundary duality,
    not formable on controls.

If that interface is constructed, live B is complete and the only remaining
Phase-A slot is formation-level control death.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_SELF_DUALITY__BOUNDARY_NATIVE_PHASE_A_INTERFACE__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_self_duality_interface` verifies seven
gates.

BSD1 checks slot accounting. `O+E` and OCB shape both represent
`carrier_object, endpoint_maps`; adding boundary self-duality represents
`DD.4_boundary_killing`.

BSD2 checks that orientation must fix a representative, not only the Z/2
cohomology class: `c` and `c^-1` remain distinct representatives for
L=6,8,10,12.

BSD3 checks that OCB shape fixes the DD.4 direction but not self-dual
properness by itself.

BSD4 rejects the hyperbolic endpoint plane, trace-augmented hyperbolic
envelope, and End-augmented hyperbolic envelope as Phase-A boundary
self-duality.

BSD5 rejects the positive Rosati End envelope, projection-forced positive
envelope, and fiber-product-saturated positive envelope as Phase-A boundary
self-duality.

BSD6 records the live interface: boundary-native self-dual properness. None
of the banked envelopes pass that interface.

BSD7 checks that live boundary self-duality completes B and leaves only
formation-level control death.

## 4. Impact on R1

```text
R1 after docs 138-314:
  NEWLY FIXED THIS CYCLE:
    - self-dual boundary/properness must be Phase-A boundary-native, not a
      Rosati/End/projection envelope imported from Phase B.

  CURRENT LIVE TARGET:
    - construct boundary-native self-dual properness for the oriented-Cartier
      boundary on O+E;
    - keep p1,p2 as primary endpoint maps;
    - prove the carrier fixes the orientation/sign;
    - prove non-formability on controls.

  DISCIPLINE:
    - hyperbolic, trace, End, Rosati, projection, and fiber-product packages
      may be diagnostics only until Qbar_BECD produces the carrier boundary.

  STILL OPEN:
    - construct the boundary-native self-dual properness interface;
    - prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BSD.1  Self-dual boundary/properness is carrier-native Phase-A data on
              the oriented-Cartier boundary.
ACCEPT-BSD.2  The carrier fixes the oriented-Cartier representative, not only
              its Z/2 class.
ACCEPT-BSD.3  DD.4 killing is coupled to boundary duality.
ACCEPT-BSD.4  p1,p2 remain represented primary endpoint maps.
ACCEPT-BSD.5  The interface does not import Phase-B graph/composition,
              projection formula, or Rosati positivity as prerequisites.
ACCEPT-BSD.6  Counts are preserved.
ACCEPT-BSD.7  The interface is not formable on controls.

KILL-BSD.1    Reject hyperbolic endpoint plane as Phase-A boundary
              self-duality.
KILL-BSD.2    Reject scalar trace or formal End augmentation as Phase-A
              boundary self-duality.
KILL-BSD.3    Reject positive Rosati matrix envelopes before carrier-native
              boundary data.
KILL-BSD.4    Reject projection forcing or local retuning that changes counts.
KILL-BSD.5    Reject formal fiber-product cells not produced by Qbar_BECD.
KILL-BSD.6    Reject any DD.4 repair independent of boundary duality.
KILL-BSD.7    Reject any package still formable on controls.
```
