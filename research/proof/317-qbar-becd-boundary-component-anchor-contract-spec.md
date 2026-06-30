# 317 - Qbar_BECD boundary component anchor contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-eightieth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 316 fixed the live twist source:

```text
carrier oriented-Cartier normal-ratio pinning.
```

This document sharpens the source of the two boundary components. The normal
ratio is not live if `D1,D2` are merely an oriented boundary pair, a product
boundary shape, or decoded endpoint labels. The components must be anchored
by the primary endpoint maps:

```text
D1 = the p1 boundary component,
D2 = the p2 boundary component.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_component_anchor_contract`
(BCA1-BCA8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_twist_pinning_contract`,
`prime_int_n1b_qbar_becd_boundary_defect_duality_contract`,
`prime_int_n1b_qbar_becd_oriented_cartier_boundary_contract`,
`prime_int_n1b_cc_product_boundary_endpoint_bundle_no_go`,
`prime_int_n1b_oriented_endpoint_difference_no_go`,
`prime_int_n1b_boundary_even_lattice_no_go`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

Docs 312-316 moved the live B target from "some boundary" to:

```text
oriented-Cartier normal-ratio twist pinning on O+E.
```

There is still a label ambiguity. If the two boundary components are not
anchored to `p1,p2`, then swapping them inverts the normal ratio and changes
the representative from `c` to `c^-1`. These are the same Z/2 class, but not
the same representative. A live boundary map must hit the representative.

The next construction target is therefore:

```text
endpoint-anchored normal ratio:
  D1 is anchored to p1,
  D2 is anchored to p2,
  the endpoint order fixes the orientation,
  the ordered normal ratio produces the unique twist with boundary c.
```

## 2. Lemma

```text
Lemma 317.1 (boundary component anchor contract).

In truncations L=6,8,10,12, the DD.4 representative c and its inverse c^-1
remain distinct representatives. Therefore swapping the two boundary
components is not harmless notation.

An oriented boundary pair by itself selects a direction, but it does not
anchor that direction to the primary endpoint maps p1,p2. In the tested
normal-crossing window there are 16 primitive directions; choosing the
oriented pair still leaves the source of the labels unproved.

Product endpoints anchor labels, but product shape alone does not supply live
B: it does not rigidify the normal ratio, produce the unique twist, or make
the boundary equal to c.

Endpoint-coordinate decoders do not solve the anchoring problem. Boundary
difference has rank one. Primary p1,p2 have rank two. Total+difference has
rank two only with a half-sum/parity condition, so it is a decoder, not a
carrier source for the boundary components.

Parity selects endpoint labels but still does not anchor the boundary
components. In the tested labels, (11,9) and (11,3) decode integrally, while
(11,8), (0,1), and (10,1) remain half-integral.

The accepted component anchor is exactly:

    carrier-native,
    boundary components present,
    D1 anchored to p1,
    D2 anchored to p2,
    ordered by endpoints,
    normal ratio rigidified,
    unique twist,
    boundary is c,
    p1,p2 primary,
    endpoint rank preserved,
    not product shape only,
    not coordinate decoding,
    not formable on controls.

If this is constructed, the normal-ratio twist pinning of doc 316 becomes a
live B datum. After that, only formation-level control death remains in
Phase A.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_COMPONENT_ANCHOR__P1P2_ORDERED_NORMAL_RATIO__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_component_anchor_contract` verifies eight
gates.

BCA1 checks that swapping boundary components inverts the representative:
`c` and `c^-1` remain distinct representatives for L=6,8,10,12.

BCA2 rejects an oriented pair without endpoint anchoring. It can select a
primitive direction but does not prove that `D1,D2` are the `p1,p2`
components.

BCA3 rejects product endpoint shape as live B. Product labels can anchor
names, but not the normal-ratio rigidification or the DD.4 boundary.

BCA4 rejects endpoint-coordinate decoders. Difference alone is rank one;
total+difference is a decoder, not primary carrier endpoint structure.

BCA5 records the parity residual: parity labels separate integral from
half-integral decodings but do not anchor boundary components.

BCA6 records control survival: endpoint-anchored-looking product data is
still formable on controls.

BCA7 records the live predicate. Only endpoint-anchored normal-ratio data
passes.

BCA8 checks slot accounting. `O+E` plus OCB shape remains only
`carrier_object, endpoint_maps`; endpoint-anchored normal-ratio data gives
`DD.4_boundary_killing`; adding control death completes Phase A.

## 4. Impact on R1

```text
R1 after docs 138-317:
  NEWLY FIXED THIS CYCLE:
    - the normal-ratio source must be endpoint-anchored: D1 is the p1 boundary
      component and D2 is the p2 boundary component.

  CURRENT LIVE TARGET:
    - construct the p1,p2-anchored oriented-Cartier boundary components inside
      Qbar_BECD;
    - prove their endpoint order fixes the orientation/sign;
    - rigidify their ordered normal ratio;
    - prove the resulting unique twist has boundary c;
    - preserve primary p1,p2 and endpoint rank;
    - prove non-formability on controls.

  DISCIPLINE:
    - unanchored oriented boundary pairs, product boundary shape,
      total/difference decoders, and parity labels are diagnostics only.

  STILL OPEN:
    - construct the endpoint-anchored normal ratio;
    - then prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BCA.1  The carrier supplies two boundary components D1,D2.
ACCEPT-BCA.2  D1 is anchored to p1 and D2 is anchored to p2.
ACCEPT-BCA.3  The endpoint order fixes the orientation/sign.
ACCEPT-BCA.4  The ordered normal ratio is rigidified by the carrier.
ACCEPT-BCA.5  The resulting unique twist has boundary c.
ACCEPT-BCA.6  p1,p2 remain primary and endpoint rank is preserved.
ACCEPT-BCA.7  Controls cannot form the anchored normal-ratio package.

KILL-BCA.1    Reject oriented boundary pairs whose components are not
              anchored to p1,p2.
KILL-BCA.2    Reject product boundary-endpoint shape as live B.
KILL-BCA.3    Reject total/difference or parity endpoint decoders as
              component anchoring.
KILL-BCA.4    Reject any component swap that changes c to c^-1 without a
              carrier reason for the chosen order.
KILL-BCA.5    Reject endpoint-anchored-looking data still formable on
              controls.
```
