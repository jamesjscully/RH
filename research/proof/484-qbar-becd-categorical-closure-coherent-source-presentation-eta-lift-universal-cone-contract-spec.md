# 484 - Qbar_BECD categorical closure coherent source-presentation eta-lift universal-cone contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-forty-seventh cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 483 left the categorical closure branch live only if the existing source
universal arrow factors through the doc-482 coherent source-presentation
equalizer:

```text
    eta_BCCube_Qbar_BECD_source,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD.
```

This document fixes the next edge. A sourced equalizer lift can still be only
a chosen section, an inhabited equalizer point, a product-side cone, or a
posthoc graph/Yoneda recognition statement. The lift must instead be one
source-native universal cone over the actual coherent source-presentation
component codomains:

```text
    Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    UP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    uniq_factor_CohSrcPres_through_lift_eta_BCCube_Qbar_BECD,
    med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD.
```

The cone has twenty-four source-native component codomains:

```text
    Comp_CohSrcPres_BCCube_Qbar_BECD_endpoint_integrality_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_degree_maps_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_dd4_boundary_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_boundary_pushforward_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_graph_composition_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_rosati_count_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_control_death_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_source_square_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_beck_chevalley_cube_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_cartesian_lift_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_component_cone_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_component_projection_pair_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_globular_modification_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_cartesian_boundary_fiber_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_boundary_fiber_coherence_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_fiber_coherence_modification_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_source_boundary_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_target_boundary_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_multiplier_path_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_coefficient_preservation_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_signed_support_preservation_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_source_before_points_cell_source,
    Comp_CohSrcPres_BCCube_Qbar_BECD_closed_finite_coherence_cell_source.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_universal_cone_contract`
(CATCOHSRCPRESETACONEQBARBECD1-CATCOHSRCPRESETACONEQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 483 through the DD.4 SCC interface (177/177 exit 0).

## 1. Purpose

After doc 483, the cheap repair is:

```text
construct a source arrow into Eq_CohSrcPres_BCCube_Qbar_BECD, then treat that
arrow as the missing object because it inhabits the equalizer.
```

That still does not construct the missing object. The branch only becomes
construction-grade if the eta lift is universal for coherent
source-presentation arrows: every such arrow must factor uniquely through the
eta lift, the mediating arrow must target
lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD, and the cone legs must
land in the actual twenty-four source component codomains rather than in
semantic labels or external point objects.

The live branch therefore narrows from "sourced eta equalizer lift" to:

```text
construct Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components from
lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD; prove its twenty-four legs
leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_* land in the twenty-four
Comp_CohSrcPres_BCCube_Qbar_BECD_*_source objects; prove
UP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD; prove
uniq_factor_CohSrcPres_through_lift_eta_BCCube_Qbar_BECD and
med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD for every coherent
source-presentation arrow; prove the same universal cone transports along
the C3/C5/C15/C45/F22 multiplier paths; and prove coefficient preservation,
signed-support preservation, and source-before-points order.
```

## 2. Lemma

```text
Lemma 484.1 (the eta lift must be a universal cone over actual components).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted eta-lift universal-cone data are:

    eta_BCCube_Qbar_BECD_source,
    fact_eta_BCCube_to_Prod_CohSrcPres_BCCube_Qbar_BECD,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    UP_Cone_lift_eta_CohSrcPres_BCCube_Qbar_BECD,
    uniq_factor_CohSrcPres_through_lift_eta_BCCube_Qbar_BECD,
    med_CohSrcPres_arrow_to_lift_eta_BCCube_Qbar_BECD,
    twenty-four Comp_CohSrcPres_BCCube_Qbar_BECD_*_source codomains,
    twenty-four leg_lift_eta_CohSrcPres_BCCube_Qbar_BECD_* legs.

The live dependency graph contains the eta-lift universal-cone spine:

    source universal arrow -> eta product factorization,
    eta product factorization -> eta equalizer lift,
    eta equalizer lift -> equalizer object,
    eta equalizer lift -> eta lift universal cone,
    eta lift universal cone -> all component legs,
    all component legs -> actual source components,
    actual source components -> seven facet components,
    actual source components -> seventeen cell components,
    all component legs -> component-leg codomain equalities,
    eta lift universal cone -> universal cone property,
    universal cone property -> unique factorization,
    unique factorization -> mediating arrow,
    mediating arrow -> eta equalizer lift,
    unique factorization -> same cone on multiplier paths,
    same cone on multiplier paths -> C3*C5=C15,
    same cone on multiplier paths -> C5*C3=C15,
    same cone on multiplier paths -> C3*C3*C5=C45,
    same cone on multiplier paths -> F22 product,
    eta lift universal cone -> coefficient preservation,
    eta lift universal cone -> signed-support preservation,
    eta lift universal cone -> source-before-points order,
    source-before-points order -> controls/DH/Epstein non-points.

The exact self-dual eta-lift cone rows are:

    z                         = {1:2, 2:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full eta-lift universal-cone payloads:

    Cone(T_C3(T_C5(z)))       = Cone(T_C15(z)),
    Cone(T_C5(T_C3(z)))       = Cone(T_C15(z)),
    Cone(T_C3(T_C3(T_C5(z)))) = Cone(T_C45(z)),
    Cone(T_C15(z*F22))        = Cone(z*(C15*F22)),
    Cone(T_C45(z*F22))        = Cone(z*(C45*F22)).

Thus chosen cones, pointwise sections, inhabited equalizers, external
component codomains, semantic target labels, graph-side cones, posthoc
Yoneda recognition, retuned component codomains, retuned cone payloads,
nonunique mediating arrows, and control/DH/Epstein point-formability do not
construct the eta-lift universal cone.
```

## 3. Consequence

Doc 484 does not solve R1 and does not prove RH. It removes the last cheap
reading of doc 483: an eta lift is not enough unless it carries the universal
source-cone structure over the actual finite coherent source presentation.
The live object is now a universal-cone-sourced eta lift of the internal
finite-limit-realized coherent source-presentation totalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACONEQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks
    twenty-four component codomains and legs, verifies the cone dependency
    graph, and checks multiplier-path payload equality.

CATCOHSRCPRESETACONEQBARBECD2
    Rejects chosen cones, pointwise sections, and inhabited equalizers.

CATCOHSRCPRESETACONEQBARBECD3
    Rejects external component codomains and semantic target labels.

CATCOHSRCPRESETACONEQBARBECD4
    Rejects nonunique or missing mediating arrows and factorizations that do
    not target the eta lift.

CATCOHSRCPRESETACONEQBARBECD5
    Rejects graph-side cones and posthoc Yoneda recognition.

CATCOHSRCPRESETACONEQBARBECD6
    Rejects retuned component codomains and retuned cone payloads.

CATCOHSRCPRESETACONEQBARBECD7
    Rejects missing C3/C5/C15/C45/F22 multiplier-path naturality.

CATCOHSRCPRESETACONEQBARBECD8
    Rejects missing universal-cone edges, component codomains, or legs.

CATCOHSRCPRESETACONEQBARBECD9
    Rejects control/DH/Epstein point-formable cones.

CATCOHSRCPRESETACONEQBARBECD10
    Accepts only the source-native eta-lift universal cone and rejects all
    dead variants.
```

## 5. Fail-Closed Note

The document is invalidated by any of the following:

1. a counterexample where an inhabited equalizer or chosen section satisfies
   the gates without a universal source cone;
2. a component leg whose codomain is not one of the twenty-four listed
   `Comp_CohSrcPres_BCCube_Qbar_BECD_*_source` objects;
3. a coherent source-presentation arrow with two distinct mediating arrows
   through `lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD`;
4. a C3/C5/C15/C45/F22 multiplier path whose full cone payload differs from
   the direct path; or
5. a control, DH, or Epstein point object satisfying the same construction
   before the source cone exists.
