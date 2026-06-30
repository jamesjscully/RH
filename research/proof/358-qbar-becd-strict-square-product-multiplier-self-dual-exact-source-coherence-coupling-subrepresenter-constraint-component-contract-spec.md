# 358 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter constraint-component contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-twenty-first cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 357 left the strict-square branch live only if the constraint codomain is
an actual source product with source-native projections and unique alpha/beta
pairings:

```text
    Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control,
    pair_alpha_NCoup_source_constraints,
    pair_beta_NCoup_source_constraints,
```

with projections:

```text
    pi_NCoup_endpoint_integrality,
    pi_NCoup_degree_maps,
    pi_NCoup_dd4_boundary,
    pi_NCoup_boundary_pushforward,
    pi_NCoup_graph_composition,
    pi_NCoup_rosati_count,
    pi_NCoup_control_death.
```

This document fixes the next edge. The projections cannot land in semantic
target labels, external modules, point-set codomains, graph-side target
objects, or component tables attached after the fact. Their codomains must be
actual source component objects in `Rep_Qbar_BECD_source_fiber`:

```text
    Comp_NCoup_endpoint_integrality_source,
    Comp_NCoup_degree_maps_source,
    Comp_NCoup_dd4_boundary_source,
    Comp_NCoup_boundary_pushforward_source,
    Comp_NCoup_graph_composition_source,
    Comp_NCoup_rosati_count_source,
    Comp_NCoup_control_death_source.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_contract`
(SCCO1-SCCO10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
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

After doc 357, the cheap repair is:

```text
name the product and projections, but let each projection land in a
semantic/external component slot rather than an object already constructed in
the represented source fiber.
```

That still does not construct the missing object. The square has to make the
component codomains before it can use them. Endpoint integrality, degree maps,
DD.4 boundary, boundary pushforward, graph composition, Rosati/count, and
control death must be source component objects, and the product projections
must land in exactly those objects.

The live branch therefore narrows from "source product with projections" to:

```text
construct the seven source component objects; prove each is carrier-native in
Rep_Qbar_BECD_source_fiber before points and graph objects; prove the seven
product projections land in them; prove pair_alpha and pair_beta use those
component codomains; prove the same component objects transport along the
C3/C5/C15/C45/F22 paths; and prove this source-component datum kills
control/DH/Epstein point-formability.
```

## 2. Lemma

```text
Lemma 358.1 (the product projections must land in source component objects).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted source component-object data are:

    Rep_Qbar_BECD_source_fiber,
    Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control,
    pair_alpha_NCoup_source_constraints,
    pair_beta_NCoup_source_constraints,
    pi_NCoup_endpoint_integrality
        -> Comp_NCoup_endpoint_integrality_source,
    pi_NCoup_degree_maps
        -> Comp_NCoup_degree_maps_source,
    pi_NCoup_dd4_boundary
        -> Comp_NCoup_dd4_boundary_source,
    pi_NCoup_boundary_pushforward
        -> Comp_NCoup_boundary_pushforward_source,
    pi_NCoup_graph_composition
        -> Comp_NCoup_graph_composition_source,
    pi_NCoup_rosati_count
        -> Comp_NCoup_rosati_count_source,
    pi_NCoup_control_death
        -> Comp_NCoup_control_death_source,
    dd4_c_original_res1,
    CTRL_Qbar_BECD_coherent_death.

The component dependency graph contains the live edges:

    Rep_Qbar_BECD_source_fiber -> each component object,
    Rep_Qbar_BECD_source_fiber -> constraint product object,
    each component object -> constraint product object,
    constraint product object -> each projection,
    each projection -> its source component object,
    each component object -> source before points and graph objects,
    source before points and graph objects -> controls/DH/Epstein not points,
    each component object -> same component on all paths,
    same component on all paths -> C3*C5=C15,
    same component on all paths -> C5*C3=C15,
    same component on all paths -> C3*C3*C5=C45,
    same component on all paths -> F22 product,
    constraint product object -> pair_alpha_NCoup_source_constraints,
    constraint product object -> pair_beta_NCoup_source_constraints.

The exact self-dual component rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full source component-object payloads:

    Comp(T_C3(T_C5(z)))       = Comp(T_C15(z)),
    Comp(T_C5(T_C3(z)))       = Comp(T_C15(z)),
    Comp(T_C3(T_C3(T_C5(z)))) = Comp(T_C45(z)),
    Comp(T_C15(z*F22))        = Comp(z*(C15*F22)),
    Comp(T_C45(z*F22))        = Comp(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus semantic target labels, external component objects, point-set codomains,
graph-side target objects, post-hoc component codomains, component shells with
no source object, local component tables, finite-sample components,
basis-dependent components, retuned component objects, quotient components,
closure components, declared component objects, products with non-source
codomains, and control/DH/Epstein point-formability do not construct the
source component objects.

The accepted datum is exactly:

    carrier-native,
    represented source fiber,
    seven actual source component objects,
    endpoint component source object,
    degree component source object,
    DD.4 component source object,
    pushforward component source object,
    graph component source object,
    Rosati/count component source object,
    control-death component source object,
    projections land in source components,
    product uses source components,
    alpha/beta pairings use source components,
    components before points,
    components before graph objects,
    components transport on all paths,
    same component objects on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    controls not points,
    DH not points,
    Epstein not points,
    required source component/projection edges present,
    no semantic target labels,
    no external component objects,
    no point-set codomain,
    no graph-side target object,
    no post-hoc component codomain,
    no component shell with no source object,
    no local component table,
    no finite-sample component,
    no basis-dependent component,
    no retuned component object,
    no quotient component,
    no closure component,
    no declared component object,
    no product with non-source codomains,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER_CONSTRAINT_COMPONENT__SOURCE_COMPONENT_OBJECT_CODOMAINS__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_contract`
verifies ten gates.

SCCO1 records the seven component objects, projection targets, H1 profile,
strict rows, component-payload equalities, and connected component graph.

SCCO2 records again that graph identities do not supply the source component
objects.

SCCO3 rejects semantic or external target labels.

SCCO4 rejects point-set, graph-side, or post-hoc projection codomains.

SCCO5 rejects local, finite-sample, basis-dependent, or retuned component
objects because they do not transport on all paths.

SCCO6 rejects quotient, closure, or declared component shells.

SCCO7 records that products with non-source component codomains still leave
control/DH/Epstein point-formability available.

SCCO8 makes every source component/projection edge mandatory.

SCCO9 accepts only source component-object products.

SCCO10 records the live product as using exactly the seven source component
objects.

Therefore a candidate that satisfies doc 357 only by naming a product and
projections is still incomplete. It must construct the seven projection
codomains as source objects first.

## 4. Consequence

The live strict-square branch is now:

```text
construct Comp_NCoup_endpoint_integrality_source,
Comp_NCoup_degree_maps_source, Comp_NCoup_dd4_boundary_source,
Comp_NCoup_boundary_pushforward_source,
Comp_NCoup_graph_composition_source, Comp_NCoup_rosati_count_source,
and Comp_NCoup_control_death_source inside Rep_Qbar_BECD_source_fiber;
then prove Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control is the
source product of exactly those seven objects, with the doc-357 pairings and
the doc-356 equalizer.
```

The open construction target is no longer "package the constraints." It is
"construct the seven carrier-native source component objects and show that the
strict square's product, pairings, equalizer, path coherences, DD.4 boundary,
Rosati/count data, graph composition, endpoint integrality, and control death
all use those same objects."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the seven component objects listed above inside Rep_Qbar_BECD_source_fiber;
2. proof that each exists before points and graph objects;
3. proof that each product projection lands in its listed component object;
4. proof that pair_alpha and pair_beta use exactly those component codomains;
5. proof that the same components transport on the C3/C5/C15/C45/F22 paths;
6. proof that these source components make controls, DH, and Epstein
   non-point-formable;
7. proof that no semantic/external/pointwise/graph-side/post-hoc/quotient/
   closure/declared component replacement is being used.
```

Until those seven source component objects are constructed, the object remains
missing.
