# 336 - Qbar_BECD strict-square product multiplier DD.4 naturality contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-ninety-ninth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 335 left the strict-square branch live only through:

```text
a carrier-native multiplier-action functor on the internal Qbar_BECD
effectivity domain, with identity, composition, product naturality, DD.4
naturality, and downstream endpoint/boundary/pushforward/graph/Rosati/count/
control outputs.
```

This document fixes the DD.4 naturality edge. The DD.4 boundary localization
cannot be attached after multiplier transport, and the DD.4 class cannot be
killed by separate splitters on separate multiplier orbits. The same carrier
boundary extension must make the boundary square commute for `C3`, `C9`, and
`F22`, with the transported splitter coming from that same boundary.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_dd4_naturality_contract`
(MBN1-MBN10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_transport_composition_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_mixed_support_orbit_closure_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_mixed_support_subtower_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_internal_effectivity_image_contract`,
`prime_int_n1b_qbar_becd_strict_square_boundary_stratum_product_contract`,
`prime_int_n1b_qbar_becd_internal_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 335, the cheap repair is:

```text
construct the multiplier-action functor, then kill the DD.4 class separately
on each visible transport orbit.
```

That is still a boundary-after-transport patch. It supplies local splitters,
but not a boundary natural transformation. A categorical square must make
the boundary localization natural for the multiplier action. In particular,
the boundary rows for `z`, `T_C3(z)`, `T_C3(T_C3(z)) = T_C9(z)`, `z*F22`,
and `T_C3(z*F22)` must be typed by one DD.4 boundary map and one internal
domain, not by orbitwise splitters or declared commutative diagrams.

The live branch therefore narrows from "multiplier-action functor" to:

```text
construct a carrier-native multiplier-action functor together with a natural
DD.4 boundary localization, where the DD.4 obstruction class is killed by the
same carrier boundary extension and transported naturally across C3, C9, and
product action squares.
```

## 2. Lemma

```text
Lemma 336.1 (DD.4 localization must be natural for multiplier transport).

In the tested truncations L=6,8,10 of U_1/(1+z^{L+1}), the DD.4 class

    c = (1+z)^-1

is a cocycle, is not a coboundary, has H^1-order 2, and satisfies
res_1(c)=1 while res_1 vanishes on all coboundaries.

The multiplier transport data include:

    T_C3(T_C3(z)) = T_C9(z) = 2[9] - [18],
    T_C3(z*F22) = T_C3(z)*F22 = z*(C3*F22) = 4[6] - 2[12].

The DD.4 boundary rows for

    z,
    T_C3(z),
    T_C3(T_C3(z)),
    T_C9(z),
    z*F22,
    T_C3(z*F22),
    T_C3(z)*F22,
    z*(C3*F22)

must all be typed by the same boundary map `B_Qbar_BECD_DD4`, the same
internal domain `D_Qbar_BECD_eff`, and the same represented DD.4 class.

Separate orbit splitters kill local copies but do not make
`T_C3(T_C3(-)) = T_C9(-)` commute with boundary localization.
Boundary-after-transport filters reverse the construction direction.
Support boundaries and weighted-zero boundaries lose the obstruction
detected by `res_1`. Endpoint/count filters, boundary kernels, local
boundary stacks, finite boundary tables, declared naturality, and
control/DH/Epstein shadows do not construct the boundary square.

Thus the accepted datum is exactly:

    carrier-native,
    actual multiplier-action functor,
    actual DD.4 boundary localization,
    actual carrier boundary extension,
    DD.4 class killed by carrier boundary,
    boundary transport natural,
    transport-composition boundary natural,
    product boundary natural,
    same boundary map types transport orbits,
    transported splitter comes from the same boundary,
    coefficients retained,
    signed support retained,
    res_1 obstruction tracked,
    domain has no endpoint/count prerequisite,
    endpoint integrality generated,
    boundary localization generated,
    pushforward compatibility generated,
    graph/Rosati/count data generated,
    control death generated,
    controls undefined at DD.4 boundary formation,
    DH undefined at DD.4 boundary formation,
    Epstein undefined at DD.4 boundary formation,
    no separate orbit splitters,
    no free torsor splitter,
    no boundary-after-transport filter,
    no declared DD.4 naturality,
    no support boundary,
    no weighted-zero boundary,
    no endpoint-degree boundary filter,
    no graph/count boundary filter,
    no boundary-kernel definition,
    no local boundary stack,
    no finite boundary table,
    no external multiplier monoid,
    no post-hoc gate intersection,
    not formable on controls, DH, or Epstein.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_DD4_NATURALITY__SEPARATE_ORBIT_SPLITTERS_DO_NOT_COMMUTE__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_dd4_naturality_contract`
verifies ten gates.

MBN1 recomputes the DD.4 obstruction profile and records the multiplier
boundary rows for `C3`, `C9`, and `F22`.

MBN2 rejects separate orbit splitters and free torsor splitters.

MBN3 rejects boundary-after-transport filters.

MBN4 rejects support and weighted-zero boundary shadows.

MBN5 rejects endpoint/count and boundary-kernel definitions as downstream.

MBN6 rejects local boundary stacks and finite boundary tables.

MBN7 rejects declared DD.4 naturality without represented edges.

MBN8 keeps DD.4 naturality tied to downstream endpoint, pushforward,
graph/Rosati/count, and control-death data.

MBN9 records the control/DH/Epstein failure mode.

MBN10 records the live predicate. Only carrier-native multiplier DD.4
naturality passes.

## 4. Impact on R1

```text
R1 after docs 138-336:
  NEWLY FIXED THIS CYCLE:
    - DD.4 boundary localization must be natural for the multiplier-action
      functor. Separate orbit splitters, free torsor splitters, and
      boundary-after-transport patches do not construct the boundary square.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the represented boundary-stratum product;
    - construct the product-to-internal-effectivity image map to the single
      internal Qbar_BECD effectivity domain;
    - construct the carrier-native multiplier-action functor on that domain;
    - construct the natural DD.4 boundary localization for that functor;
    - prove the DD.4 class is killed by the same carrier boundary extension,
      with transported splitter, composition naturality, and product
      naturality;
    - prove endpoint integrality, boundary localization, pushforward
      compatibility, graph/Rosati/count data, and formation-level control
      death are generated there;
    - prove DH, Epstein, and controls are undefined at DD.4 boundary
      formation.

  DISCIPLINE:
    - separate orbit splitters, free splitters, support/weighted-zero
      boundaries, endpoint/count filters, boundary kernels, local stacks,
      finite tables, declared naturality, and post-hoc control filters are
      diagnostics only.

  STILL OPEN:
    - construct the carrier-native multiplier-action functor with natural
      DD.4 boundary localization, or kill the strict-square branch with a
      named mechanism at this point.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-MBN.1  Exhibit the natural DD.4 boundary localization for the
              multiplier-action functor.
ACCEPT-MBN.2  Prove the DD.4 obstruction class is killed by the same carrier
              boundary extension across transport orbits.
ACCEPT-MBN.3  Prove transport composition and product action commute with
              DD.4 boundary localization.
ACCEPT-MBN.4  Prove the transported splitter comes from the same boundary,
              not from orbitwise free splitters.
ACCEPT-MBN.5  Retain coefficients, signed support, and res_1 obstruction data
              in one internal domain.
ACCEPT-MBN.6  Generate endpoint, boundary, pushforward, graph/Rosati/count,
              and control death from the DD.4-natural transport domain.
ACCEPT-MBN.7  Prove DH, Epstein, and controls are undefined at DD.4 boundary
              formation.

KILL-MBN.1    Reject separate orbit splitters.
KILL-MBN.2    Reject free torsor splitters.
KILL-MBN.3    Reject boundary-after-transport filters.
KILL-MBN.4    Reject declared DD.4 naturality without represented edges.
KILL-MBN.5    Reject support and weighted-zero boundary shadows.
KILL-MBN.6    Reject endpoint/count boundary filters and boundary kernels.
KILL-MBN.7    Reject local boundary stacks and finite boundary tables.
KILL-MBN.8    Reject external multiplier monoids.
KILL-MBN.9    Reject post-hoc gate intersections.
KILL-MBN.10   Reject control/DH/Epstein-formable shadows.
```
