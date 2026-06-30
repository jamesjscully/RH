# 489 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian-coherence globular-modification boundary-fiber cartesian contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-fifty-second cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 488 left the categorical closure branch live only if the doc-487
source-level globular modification is selected by an actual source
boundary-restriction map and represented boundary fiber over its fixed
globular boundary:

```text
    res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd,
    Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    eta_Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components.
```

This document fixes the next edge. A represented boundary fiber over one
globular boundary is still insufficient if it is static, rebuilt after base
change, transported by chosen local tables, or checked only after points or
graph objects. The boundary fiber must itself be cartesian over the
represented source multiplier lifts:

```text
    CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    cart_res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd.
```

The cartesian boundary fiber must transport the boundary restriction map and
the fiber universal arrow along the C3/C5/C15/C45/F22 source paths while
preserving the fixed globular boundary, source and target boundaries, all
thirty-two pasting faces, coefficients, and signed support before points and
graph objects exist.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 488 through the DD.4 SCC interface (182/182 exit 0).

## 1. Purpose

After doc 488, the cheap repair is:

```text
construct one represented fiber over
GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components and then
reuse that fiber name for every multiplier path.
```

That still does not construct the missing object. The source must make the
boundary fiber pull back cartesianly over the represented source lifts. If
the fiber is rebuilt after base change, transported by local choices, or
identified by graph labels, it can select the right boundary at one point
while failing C3*C5=C15, C5*C3=C15, C3*C3*C5=C45, or F22 compatibility.

The live branch therefore narrows from "represented boundary fiber" to:

```text
construct CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components;
construct cart_res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd;
prove the boundary restriction is cartesian-natural;
prove eta_Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components
transports cartesianly; prove the fixed globular boundary, source boundary,
target boundary, and all pasting faces pull back; prove the same cartesian
fiber appears on the C3*C5=C15, C5*C3=C15, C3*C3*C5=C45, and F22 paths; and
prove coefficient, signed-support, and source-before-points preservation.
```

## 2. Lemma

```text
Lemma 489.1 (the represented boundary fiber must be cartesian).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted cartesian boundary-fiber data are:

    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    CartLift_CohSrcPres_BCCube_Qbar_BECD_multiplier_source_fiber,
    CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd,
    Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    eta_Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    cart_res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd,
    med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD,
    CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    twenty-four Comp_CohSrcPres_BCCube_Qbar_BECD_*_source codomains,
    twenty-four cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_* legs,
    thirty-two represented coherence cells,
    thirty-two represented pasting faces.

The live dependency graph contains the cartesian boundary-fiber spine:

    eta equalizer lift -> cartesian source lift,
    cartesian source lift -> cartesian eta lift cone,
    cartesian eta lift cone -> cartesian cone coherence,
    cartesian cone coherence -> globular modification,
    globular modification -> boundary restriction,
    boundary restriction -> represented boundary fiber,
    represented boundary fiber -> boundary fiber arrow,
    boundary fiber arrow -> selected globular modification,
    represented boundary fiber -> cartesian boundary fiber,
    boundary restriction -> cartesian boundary restriction,
    cartesian boundary restriction -> cartesian boundary fiber,
    cartesian boundary fiber -> boundary-fiber-arrow cartesianity,
    cartesian boundary fiber -> fixed globular boundary pullback,
    cartesian boundary fiber -> source-boundary cartesianity,
    cartesian boundary fiber -> target-boundary cartesianity,
    cartesian boundary fiber -> pasting-faces cartesianity,
    cartesian boundary fiber -> C3*C5=C15 fiber pullback,
    cartesian boundary fiber -> C5*C3=C15 fiber pullback,
    cartesian boundary fiber -> C3*C3*C5=C45 fiber pullback,
    cartesian boundary fiber -> F22 fiber pullback,
    all fiber pullbacks -> same cartesian fiber on all paths,
    same cartesian fiber on all paths -> C3*C5=C15,
    same cartesian fiber on all paths -> C5*C3=C15,
    same cartesian fiber on all paths -> C3*C3*C5=C45,
    same cartesian fiber on all paths -> F22 product,
    cartesian boundary fiber -> coefficient preservation,
    cartesian boundary fiber -> signed-support preservation,
    cartesian boundary fiber -> source-before-points order,
    source-before-points order -> controls/DH/Epstein non-points.

The exact self-dual cartesian boundary-fiber rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full cartesian boundary-fiber payloads:

    CartFib(T_C3(T_C5(z)))       = CartFib(T_C15(z)),
    CartFib(T_C5(T_C3(z)))       = CartFib(T_C15(z)),
    CartFib(T_C3(T_C3(T_C5(z)))) = CartFib(T_C45(z)),
    CartFib(T_C15(z*F22))        = CartFib(z*(C15*F22)),
    CartFib(T_C45(z*F22))        = CartFib(z*(C45*F22)).

Thus graph identities, static one-boundary fibers, reused fiber names without
pullback, chosen base-change fibers, fibers rebuilt after base change,
noncartesian pullbacks, local transport tables, pointwise cartesian fibers,
graph-side cartesian fibers, post-product cartesian fibers, retuned
cartesian fibers, reindexed cartesian fibers, and control/DH/Epstein
point-formability do not construct the cartesian boundary fiber.
```

## 3. Consequence

Doc 489 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 488: one represented boundary fiber is not enough unless that
fiber is cartesian over the represented source multiplier lifts. The live
object is now a cartesian-represented-boundary-fiber globular-modification-
coherent cartesian-universal-cone-sourced eta lift of the internal
finite-limit-realized coherent source-presentation totalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    cartesian boundary fiber, the connected cartesian boundary-fiber graph,
    strict rows, and multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD2
    Rejects graph identities as cartesian fiber transport.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD3
    Rejects static one-boundary fibers and reused fiber names without
    pullback.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD4
    Rejects noncartesian pullbacks that fail to preserve boundary data.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD5
    Rejects chosen local fiber transport and fibers rebuilt after base change.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD6
    Rejects pointwise, graph-side, and post-product cartesian fibers.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD7
    Rejects retuned or reindexed cartesian fibers.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD8
    Rejects missing cartesian boundary-fiber edges or pasting faces.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD9
    Rejects control/DH/Epstein point-formable cartesian fibers.

CATCOHSRCPRESETACARTCOHGMGBFCARTQBARBECD10
    Accepts only cartesian represented boundary fibers and rejects all dead
    variants.
```

## 5. Fail-Closed Note

The document is invalidated by any of the following:

1. `Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`
   accepted without
   `CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`;
2. a boundary restriction that is not transported by
   `cart_res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd`;
3. a fixed globular boundary, source boundary, target boundary, or pasting
   face not preserved by the cartesian pullback;
4. a C3/C5/C15/C45/F22 path whose full cartesian boundary-fiber payload
   differs from the direct path; or
5. a control, DH, or Epstein point object satisfying the same cartesian
   boundary-fiber construction before the source fiber exists.
