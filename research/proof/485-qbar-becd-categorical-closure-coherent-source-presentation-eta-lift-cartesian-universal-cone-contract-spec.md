# 485 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian universal-cone contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-forty-eighth cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 484 left the categorical closure branch live only if the doc-483 eta lift
forms a source-native universal cone over the actual twenty-four coherent
source-presentation component codomains:

```text
    Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    UP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    uniq_factor_CohSrcPres_through_lift_eta_BCCube_Qbar_BECD,
    med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD.
```

This document fixes the next edge. A universal cone can still be too
abstract if it does not pull back along the represented coherent
source-presentation source lifts. Finite path checks, chosen transport
isomorphisms, pointwise naturality, graph-side base change, or declared
naturality squares can make a cone look stable without making it cartesian in
the source fibration. The new required data are:

```text
    CartLift_CohSrcPres_BCCube_Qbar_BECD_multiplier_source_fiber,
    CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    Nat_med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD_cartesian.
```

The cartesian cone has the same twenty-four source component codomains and
the same twenty-four doc-484 legs, plus cartesian transported legs:

```text
    cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_*.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_universal_cone_contract`
(CATCOHSRCPRESETACARTCONEQBARBECD1-CATCOHSRCPRESETACARTCONEQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 484 through the DD.4 SCC interface (178/178 exit 0).

## 1. Purpose

After doc 484, the cheap repair is:

```text
construct the eta-lift universal cone in one fiber, then assert compatibility
with multiplier/source lifts by finite checks or chosen transport maps.
```

That still does not construct the missing object. The source-presentation
eta lift must be stable under the represented source lifts themselves. The
cone must pull back cartesianly, preserve the actual source component
codomains and legs under base change, and make both component-leg naturality
and mediating-arrow naturality source-native before points or graph objects
exist.

The live branch therefore narrows from "eta-lift universal cone" to:

```text
construct CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components over
CartLift_CohSrcPres_BCCube_Qbar_BECD_multiplier_source_fiber; prove every
represented source lift pulls back Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components
to the same cartesian cone; prove the twenty-four component legs and their
codomain equalities are cartesian-natural; prove
Nat_med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD_cartesian; prove the
cartesian universal property CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD;
prove the same cartesian cone transports on C3/C5/C15/C45/F22 paths; and
prove coefficient/signed-support preservation and source-before-points order.
```

## 2. Lemma

```text
Lemma 485.1 (the eta-lift universal cone must be cartesian).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted cartesian eta-lift universal-cone data are:

    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    CartLift_CohSrcPres_BCCube_Qbar_BECD_multiplier_source_fiber,
    CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    Nat_med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD_cartesian,
    UP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    uniq_factor_CohSrcPres_through_lift_eta_BCCube_Qbar_BECD,
    med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD,
    twenty-four Comp_CohSrcPres_BCCube_Qbar_BECD_*_source codomains,
    twenty-four leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_* legs,
    twenty-four cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_* legs.

The live dependency graph contains the cartesian universal-cone spine:

    eta equalizer lift -> eta lift universal cone,
    eta lift universal cone -> cartesian eta lift cone,
    cartesian source lifts -> cartesian eta lift cone,
    cartesian eta lift cone -> C3/C5/C15/C45/F22 cone pullbacks,
    cartesian eta lift cone -> base change preserves universal cone,
    base change preserves universal cone -> component-leg cartesian naturality,
    base change preserves universal cone -> mediating-arrow cartesian naturality,
    component-leg cartesian naturality -> cartesian component legs,
    cartesian component legs -> actual source components,
    component-leg cartesian naturality -> component-leg codomain equalities,
    mediating-arrow cartesian naturality -> cartesian universal property,
    cartesian universal property -> unique factorization,
    unique factorization -> mediating arrow,
    mediating arrow -> eta equalizer lift,
    cartesian eta lift cone -> same cartesian cone on multiplier paths,
    same cartesian cone on multiplier paths -> C3*C5=C15,
    same cartesian cone on multiplier paths -> C5*C3=C15,
    same cartesian cone on multiplier paths -> C3*C3*C5=C45,
    same cartesian cone on multiplier paths -> F22 product,
    cartesian eta lift cone -> coefficient preservation,
    cartesian eta lift cone -> signed-support preservation,
    cartesian eta lift cone -> source-before-points order,
    source-before-points order -> controls/DH/Epstein non-points.

The exact self-dual cartesian eta-lift cone rows are:

    z                         = {1:2, 2:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full cartesian eta-lift cone payloads:

    CartCone(T_C3(T_C5(z)))       = CartCone(T_C15(z)),
    CartCone(T_C5(T_C3(z)))       = CartCone(T_C15(z)),
    CartCone(T_C3(T_C3(T_C5(z)))) = CartCone(T_C45(z)),
    CartCone(T_C15(z*F22))        = CartCone(z*(C15*F22)),
    CartCone(T_C45(z*F22))        = CartCone(z*(C45*F22)).

Thus finite path checks, sampled transport, pointwise naturality,
graph-side base change, local transport tables, chosen transport
isomorphisms, up-to-isomorphism claims without coherence, lax naturality,
noncartesian pullbacks, reindexed cone labels, retuned transport,
base-changed component replacements, declared naturality squares, split
componentwise naturality, and control/DH/Epstein point-formability do not
construct the cartesian eta-lift universal cone.
```

## 3. Consequence

Doc 485 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 484: a universal cone is not enough unless the represented
source lifts pull it back cartesianly, including the component legs and the
unique mediating arrows. The live object is now a cartesian-universal-cone-
sourced eta lift of the internal finite-limit-realized coherent
source-presentation totalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCONEQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks
    twenty-four component codomains, twenty-four legs, twenty-four cartesian
    legs, the cartesian-cone dependency graph, and multiplier-path payload
    equality.

CATCOHSRCPRESETACARTCONEQBARBECD2
    Rejects finite path checks, sampled transport, and declared naturality
    squares.

CATCOHSRCPRESETACARTCONEQBARBECD3
    Rejects chosen transport isomorphisms, up-to-isomorphism claims without
    coherence, and noncartesian pullbacks.

CATCOHSRCPRESETACARTCONEQBARBECD4
    Rejects split component-leg naturality without mediating-arrow naturality.

CATCOHSRCPRESETACARTCONEQBARBECD5
    Rejects graph-side base change, pointwise naturality, and local transport
    tables.

CATCOHSRCPRESETACARTCONEQBARBECD6
    Rejects retuned transport, reindexed cone labels, and base-changed
    component replacements.

CATCOHSRCPRESETACARTCONEQBARBECD7
    Rejects missing cartesian multiplier-path naturality.

CATCOHSRCPRESETACARTCONEQBARBECD8
    Rejects missing cartesian universal-cone edges or cartesian legs.

CATCOHSRCPRESETACARTCONEQBARBECD9
    Rejects control/DH/Epstein point-formable cartesian cones.

CATCOHSRCPRESETACARTCONEQBARBECD10
    Accepts only the source-native cartesian eta-lift universal cone and
    rejects all dead variants.
```

## 5. Fail-Closed Note

The document is invalidated by any of the following:

1. a represented source lift whose pullback of the doc-484 cone is not
   `CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`;
2. a cartesian component leg that lands outside the listed actual source
   component codomains;
3. a coherent source-presentation arrow whose mediating arrow is not natural
   under base change;
4. a C3/C5/C15/C45/F22 multiplier path whose full cartesian cone payload
   differs from the direct path; or
5. a control, DH, or Epstein point object satisfying the same cartesian cone
   construction before the represented source lifts exist.
