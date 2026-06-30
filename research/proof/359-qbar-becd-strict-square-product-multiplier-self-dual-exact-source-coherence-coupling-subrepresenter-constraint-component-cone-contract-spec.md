# 359 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter constraint-component-cone contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-twenty-second cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 358 left the strict-square branch live only if the seven projection
codomains are actual source component objects:

```text
    Comp_NCoup_endpoint_integrality_source,
    Comp_NCoup_degree_maps_source,
    Comp_NCoup_dd4_boundary_source,
    Comp_NCoup_boundary_pushforward_source,
    Comp_NCoup_graph_composition_source,
    Comp_NCoup_rosati_count_source,
    Comp_NCoup_control_death_source.
```

This document fixes the next edge. Seven source component objects and seven
source-native legs are still not enough if the legs are independently chosen,
pulled back from product projections after the fact, or assembled only after
points or graph objects exist. The square itself must generate one
source-native component cone from the represented universal arrow:

```text
    eta_Qbar_BECD_source,
    eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    Cone_NCoup_eta_source_components,
```

with legs:

```text
    leg_NCoup_endpoint_integrality_source,
    leg_NCoup_degree_maps_source,
    leg_NCoup_dd4_boundary_source,
    leg_NCoup_boundary_pushforward_source,
    leg_NCoup_graph_composition_source,
    leg_NCoup_rosati_count_source,
    leg_NCoup_control_death_source.
```

The product pairing must be the unique mediating arrow from this cone:

```text
    pi_NCoup_endpoint_integrality o pair_alpha_NCoup_source_constraints
        = leg_NCoup_endpoint_integrality_source,
    pi_NCoup_degree_maps o pair_alpha_NCoup_source_constraints
        = leg_NCoup_degree_maps_source,
    pi_NCoup_dd4_boundary o pair_alpha_NCoup_source_constraints
        = leg_NCoup_dd4_boundary_source,
    pi_NCoup_boundary_pushforward o pair_alpha_NCoup_source_constraints
        = leg_NCoup_boundary_pushforward_source,
    pi_NCoup_graph_composition o pair_alpha_NCoup_source_constraints
        = leg_NCoup_graph_composition_source,
    pi_NCoup_rosati_count o pair_alpha_NCoup_source_constraints
        = leg_NCoup_rosati_count_source,
    pi_NCoup_control_death o pair_alpha_NCoup_source_constraints
        = leg_NCoup_control_death_source.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_contract`
(SCCN1-SCCN10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_product_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_morphism_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_finite_limit_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_representability_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_formation_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_formation_gate_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_represented_source_fiber_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_cartesian_coherence_contract`,
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 358, the cheap repair is:

```text
construct or name seven source component objects, attach seven component
legs separately, then assert that the product pairing packages them.
```

That still does not make the square itself construct endpoint integrality,
degree maps, DD.4 boundary, boundary pushforward, graph composition,
Rosati/count, and control death together. The seven legs must be one cone
generated from the represented source universal arrow. The product pairing is
acceptable only as the unique mediating arrow from that cone through the
doc-357 product.

The live branch therefore narrows from "source component objects" to:

```text
construct Cone_NCoup_eta_source_components from eta_Qbar_BECD_source and
eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source; prove its seven legs land in
the doc-358 component objects; prove pair_alpha is the unique product
mediating arrow whose projections are those legs; prove pair_beta is
compatible with the same zero/diagonal component cone; prove the same cone
transports along the C3/C5/C15/C45/F22 paths; and prove the cone is formed
before points and graph objects so controls, DH, and Epstein are non-points.
```

## 2. Lemma

```text
Lemma 359.1 (the source components must be one eta-generated cone).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted source component-cone data are:

    Rep_Qbar_BECD_source_fiber,
    eta_Qbar_BECD_source,
    eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    Cone_NCoup_eta_source_components,
    Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control,
    pair_alpha_NCoup_source_constraints,
    pair_beta_NCoup_source_constraints,
    leg_NCoup_endpoint_integrality_source
        -> Comp_NCoup_endpoint_integrality_source,
    leg_NCoup_degree_maps_source
        -> Comp_NCoup_degree_maps_source,
    leg_NCoup_dd4_boundary_source
        -> Comp_NCoup_dd4_boundary_source,
    leg_NCoup_boundary_pushforward_source
        -> Comp_NCoup_boundary_pushforward_source,
    leg_NCoup_graph_composition_source
        -> Comp_NCoup_graph_composition_source,
    leg_NCoup_rosati_count_source
        -> Comp_NCoup_rosati_count_source,
    leg_NCoup_control_death_source
        -> Comp_NCoup_control_death_source,
    dd4_c_original_res1,
    CTRL_Qbar_BECD_coherent_death.

The component-cone dependency graph contains the live edges:

    eta_Qbar_BECD_source -> eta_NCoup,
    eta_NCoup -> Cone_NCoup_eta_source_components,
    Rep_Qbar_BECD_source_fiber -> Cone_NCoup_eta_source_components,
    Cone_NCoup_eta_source_components -> each component leg,
    each component leg -> its doc-358 source component object,
    Cone_NCoup_eta_source_components -> constraint product object,
    constraint product object -> product universal property,
    Cone_NCoup_eta_source_components -> pair_alpha_NCoup_source_constraints,
    pair_alpha_NCoup_source_constraints -> constraint product object,
    product universal property -> pair_alpha unique from cone,
    pair_alpha unique from cone -> all projection-leg equalities,
    all projection-leg equalities -> their component legs,
    Cone_NCoup_eta_source_components -> pair_beta_NCoup_source_constraints,
    pair_beta_NCoup_source_constraints -> zero/diagonal source cone,
    Cone_NCoup_eta_source_components -> source before points and graph objects,
    source before points and graph objects -> controls/DH/Epstein not points,
    Cone_NCoup_eta_source_components -> same cone payload on all paths,
    same cone payload on all paths -> C3*C5=C15,
    same cone payload on all paths -> C5*C3=C15,
    same cone payload on all paths -> C3*C3*C5=C45,
    same cone payload on all paths -> F22 product.

The exact self-dual component-cone rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full eta-generated source cone payloads:

    Cone(T_C3(T_C5(z)))       = Cone(T_C15(z)),
    Cone(T_C5(T_C3(z)))       = Cone(T_C15(z)),
    Cone(T_C3(T_C3(T_C5(z)))) = Cone(T_C45(z)),
    Cone(T_C15(z*F22))        = Cone(z*(C15*F22)),
    Cone(T_C45(z*F22))        = Cone(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus independent component legs, externally chosen legs, post-hoc cone labels,
product-projection pullbacks, point-functor cones, graph-side cones,
componentwise natural transformations, local cone tables, finite-sample
cones, basis-dependent cones, retuned cone legs, quotient cones, closure
cones, split products of cones, declared cones, non-eta-generated cones, and
control/DH/Epstein point-formability do not construct the source component
cone.

The accepted datum is exactly:

    carrier-native,
    represented source fiber,
    actual source universal arrow,
    actual coupling universal arrow,
    actual source component cone,
    component cone generated by eta,
    source-native component cone,
    seven actual component legs,
    endpoint leg actual,
    degree leg actual,
    DD.4 leg actual,
    pushforward leg actual,
    graph leg actual,
    Rosati/count leg actual,
    control-death leg actual,
    legs land in the doc-358 source component objects,
    cone assembles pair_alpha,
    pair_alpha unique from the cone,
    projections equal the cone legs,
    pair_beta zero/diagonal cone compatible,
    cone before points,
    cone before graph objects,
    cone transports on all paths,
    same cone payload on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    controls not points,
    DH not points,
    Epstein not points,
    required source component-cone edges present,
    no independent component legs,
    no external chosen legs,
    no post-hoc cone label,
    no product-projection pullback,
    no point-functor cone,
    no graph-side cone,
    no componentwise natural transformations,
    no local cone table,
    no finite-sample cone,
    no basis-dependent cone,
    no retuned cone leg,
    no quotient cone,
    no closure cone,
    no split product of cones,
    no declared cone,
    no non-eta-generated cone,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER_CONSTRAINT_COMPONENT_CONE__ETA_GENERATED_SOURCE_CONE__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_contract`
verifies ten gates.

SCCN1 records the eta-generated source component cone, its seven legs, H1
profile, strict rows, cone-payload equalities, and connected cone graph.

SCCN2 records again that graph identities do not supply the eta-generated
source component cone.

SCCN3 rejects independent or externally chosen component legs.

SCCN4 rejects post-hoc, pointwise, or graph-side cones.

SCCN5 rejects local, finite-sample, basis-dependent, or retuned cones.

SCCN6 rejects quotient, closure, split, or declared cones because they are not
eta-generated source cones.

SCCN7 records that non-eta-generated cones still leave controls, DH, and
Epstein formable.

SCCN8 makes every eta-cone leg and projection equality mandatory.

SCCN9 accepts only eta-generated source component cones.

SCCN10 records the live cone as uniquely mediating `pair_alpha` through the
doc-358 component objects.

Therefore a candidate that satisfies doc 358 only by naming seven component
objects, or by giving seven independent component legs, is still incomplete.
The square must produce one eta-generated component cone, and the product
pairing must be the unique arrow induced by that cone.

## 4. Consequence

The live strict-square branch is now:

```text
construct Cone_NCoup_eta_source_components from eta_Qbar_BECD_source and
eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source; prove its seven legs are the
source-native endpoint, degree, DD.4, pushforward, graph, Rosati/count, and
control-death component legs; prove pair_alpha is exactly the unique product
arrow induced by that cone; and prove pair_beta is compatible with the same
source zero/diagonal component cone.
```

The open construction target is no longer "provide the seven component
objects." It is "show the represented source universal arrow generates one
cone whose seven legs are those component objects and whose product pairing is
the strict square's alpha map."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. Cone_NCoup_eta_source_components;
2. proof that it is generated from eta_Qbar_BECD_source through eta_NCoup;
3. the seven component legs listed above;
4. proof that those legs land in the doc-358 component objects;
5. proof that pair_alpha is the unique product-mediated arrow from this cone;
6. proof of the seven projection-leg equalities;
7. proof that pair_beta is zero/diagonal compatible with the same source cone;
8. proof that the same cone transports on all C3/C5/C15/C45/F22 paths;
9. proof that the cone is formed before points and graph objects;
10. proof that no independent/external/post-hoc/pointwise/graph-side/local/
    quotient/closure/split/declared/non-eta cone replacement is being used.
```

Until the eta-generated source component cone is constructed, the object
remains missing.
