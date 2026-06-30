# 488 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian-coherence globular-modification boundary-fiber contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-fifty-first cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 487 left the categorical closure branch live only if the doc-486
represented cartesian eta-lift coherence cells are faces of one source-level
globular modification with shared source and target boundary:

```text
    Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components.
```

This document fixes the next edge. A source-level globular modification is
still insufficient if it is only chosen as a boundary filler, wrapped in a
contractible-choice argument, supplied by an external/local/quotient fiber, or
recognized by graph-side labels. The modification must be selected by an
actual source boundary-restriction map and represented boundary fiber over
its fixed globular boundary:

```text
    res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd,
    Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    eta_Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components.
```

The fiber must be over
`GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`; its
universal arrow must select
`Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`; and any
unique-filler or contractibility claim is admissible only after the
represented boundary fiber exists.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_contract`
(CATCOHSRCPRESETACARTCOHGMGBFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 487 through the DD.4 SCC interface (181/181 exit 0).

## 1. Purpose

After doc 487, the cheap repair is:

```text
give the source-level globular modification, then choose it as the boundary
filler over its named globular boundary.
```

That still does not construct the missing object. The source must supply the
boundary restriction map from modifications to their globular boundary and a
represented fiber over the fixed boundary. Otherwise the candidate has a
formal filler but no source-native object selecting it.

The live branch therefore narrows from "one source-level globular
modification" to:

```text
construct res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd;
construct Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components
over GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components;
construct eta_Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components;
prove the fiber arrow selects
Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components;
prove unique source filler and contractibility only after the represented
fiber; prove preservation of source boundary, target boundary, all pasting
faces, multiplier paths, coefficients, signed support, and source-before-
points order.
```

## 2. Lemma

```text
Lemma 488.1 (the cartesian eta-lift globular modification needs its
represented boundary fiber).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted boundary-fiber data are:

    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd,
    Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    eta_Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD,
    CartUP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    twenty-four Comp_CohSrcPres_BCCube_Qbar_BECD_*_source codomains,
    twenty-four cart_leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_* legs,
    thirty-two represented coherence cells,
    thirty-two represented pasting faces,
    boundary preservation,
    unique source filler after the represented fiber,
    contractibility only after the represented fiber.

The live dependency graph contains the boundary-fiber spine:

    eta equalizer lift -> cartesian eta lift cone,
    cartesian eta lift cone -> cartesian cone coherence,
    cartesian cone coherence -> globular modification,
    globular modification -> globular boundary,
    globular modification -> boundary restriction,
    boundary restriction -> globular boundary,
    globular boundary -> represented boundary fiber,
    boundary restriction -> represented boundary fiber,
    represented boundary fiber -> boundary fiber arrow,
    boundary fiber arrow -> selected globular modification,
    selected globular modification -> globular modification,
    represented boundary fiber -> unique source filler,
    unique source filler -> contractible after represented fiber,
    represented boundary fiber -> boundary preservation,
    boundary preservation -> source boundary,
    boundary preservation -> target boundary,
    boundary preservation -> all pasting faces,
    boundary preservation -> coefficient preservation,
    boundary preservation -> signed-support preservation,
    represented boundary fiber -> same fiber on multiplier paths,
    same fiber on multiplier paths -> C3*C5=C15,
    same fiber on multiplier paths -> C5*C3=C15,
    same fiber on multiplier paths -> C3*C3*C5=C45,
    same fiber on multiplier paths -> F22 product,
    represented boundary fiber -> source-before-points order,
    source-before-points order -> controls/DH/Epstein non-points.

The exact self-dual boundary-fiber rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full represented boundary-fiber payloads:

    Fib(T_C3(T_C5(z)))       = Fib(T_C15(z)),
    Fib(T_C5(T_C3(z)))       = Fib(T_C15(z)),
    Fib(T_C3(T_C3(T_C5(z)))) = Fib(T_C45(z)),
    Fib(T_C15(z*F22))        = Fib(z*(C15*F22)),
    Fib(T_C45(z*F22))        = Fib(z*(C45*F22)).

Thus graph identities, label-only selections, chosen boundary sections,
contractible-choice wrappers without a representer, fibers over the wrong
globular boundary, external/quotient/local boundary fibers, pointwise or
graph-side boundary fibers, post-product boundary fibers, retuned boundary
restrictions, reindexed boundary fibers, missing fiber arrows, missing unique
fillers, contractibility before representation, and control/DH/Epstein
point-formability do not construct the represented boundary fiber.
```

## 3. Consequence

Doc 488 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 487: a source-level globular modification is not enough unless
it is selected by a represented boundary fiber over its fixed globular
boundary. The live object is now a represented-boundary-fiber
globular-modification-coherent cartesian-universal-cone-sourced eta lift of
the internal finite-limit-realized coherent source-presentation totalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    represented boundary fiber, the connected boundary-fiber graph, strict
    rows, and multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD2
    Rejects graph identities or label-only selections as boundary fibers.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD3
    Rejects chosen boundary sections and contractible-choice wrappers.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD4
    Rejects fibers over the wrong globular boundary.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD5
    Rejects external, quotient, and local boundary fibers.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD6
    Rejects pointwise, graph-side, and post-product boundary fibers.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD7
    Rejects retuned or reindexed boundary fibers.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD8
    Rejects missing selection arrows, missing fillers, premature
    contractibility, missing pasting faces, and missing boundary-fiber edges.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD9
    Rejects control/DH/Epstein point-formable boundary fibers.

CATCOHSRCPRESETACARTCOHGMGBFQBARBECD10
    Accepts only represented source boundary fibers and rejects all dead
    variants.
```

## 5. Fail-Closed Note

The document is invalidated by any of the following:

1. `Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`
   accepted without
   `res_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_to_GlobBd`;
2. a boundary fiber not represented by
   `Fib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`;
3. a fiber not lying over
   `GlobBd_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components`;
4. a fiber arrow that does not select the doc-487 globular modification; or
5. a control, DH, or Epstein point object satisfying the same represented
   boundary-fiber construction before the source fiber exists.
