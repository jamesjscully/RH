# 357 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter constraint-product contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-twentieth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 356 left the strict-square branch live only if the doc-355 finite-limit
cut is the equalizer of actual parallel source morphisms:

```text
    alpha_NCoup_source_constraints,
    beta_NCoup_source_constraints
        : Rep_Qbar_BECD_source_fiber
          -> Con_NCoup_endpoint_dd4_rosati_control_source.
```

This document fixes the next edge. A single constraint codomain is still not
enough if it is only a bundled tuple label, an external product of sets, a
component checklist, or a graph-side product after points exist. The named
constraint product must be an actual source product with source-native
projections and unique alpha/beta pairing maps:

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

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_product_contract`
(SCPP1-SCPP10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
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

After doc 356, the cheap repair is:

```text
package endpoint, degree, DD.4, pushforward, graph, Rosati/count, and
control-death component values into a named product object,
then define alpha and beta as maps to that package.
```

That still does not construct the missing object. The product object must
exist in the represented source fiber. Its projections must be actual
source-native projections to the component constraint objects. The alpha and
beta maps must be the unique pairings through those projections. Otherwise
the "single codomain" of doc 356 is only a notational bundle.

The live branch therefore narrows from "source constraint morphisms" to:

```text
construct Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control and its
source-native projections; prove the source product universal property; prove
pair_alpha_NCoup_source_constraints and pair_beta_NCoup_source_constraints
are the unique pairings whose projected components are the endpoint, degree,
DD.4, pushforward, graph, Rosati/count, and control-death component
morphisms; prove the equalizer uses this product pair and all paths use the
same product.
```

## 2. Lemma

```text
Lemma 357.1 (the source constraint codomain must be an actual product).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted source constraint-product data are:

    Rep_Qbar_BECD_source_fiber,
    Con_NCoup_endpoint_dd4_rosati_control_source,
    Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control,
    pair_alpha_NCoup_source_constraints,
    pair_beta_NCoup_source_constraints,
    alpha_NCoup_source_constraints,
    beta_NCoup_source_constraints,
    pi_NCoup_endpoint_integrality,
    pi_NCoup_degree_maps,
    pi_NCoup_dd4_boundary,
    pi_NCoup_boundary_pushforward,
    pi_NCoup_graph_composition,
    pi_NCoup_rosati_count,
    pi_NCoup_control_death,
    eq_NCoup_constraints_to_SubRep_Qbar_BECD_source_fiber,
    LimCut_NCoup_Qbar_BECD_source_fiber,
    dd4_c_original_res1,
    CTRL_Qbar_BECD_coherent_death.

The product dependency graph contains the live edges:

    Rep_Qbar_BECD_source_fiber -> constraint product object,
    constraint product object -> constraint object,
    constraint product object -> endpoint projection,
    constraint product object -> degree projection,
    constraint product object -> DD.4 projection,
    constraint product object -> pushforward projection,
    constraint product object -> graph projection,
    constraint product object -> Rosati/count projection,
    constraint product object -> control-death projection,
    every projection -> its component object,
    constraint product object -> product universal property,
    product universal property -> projections jointly determine pairing,
    Rep_Qbar_BECD_source_fiber -> pair_alpha_NCoup_source_constraints,
    pair_alpha_NCoup_source_constraints -> alpha_NCoup_source_constraints,
    pair_alpha_NCoup_source_constraints -> constraint product object,
    pair_alpha_NCoup_source_constraints -> all alpha components,
    Rep_Qbar_BECD_source_fiber -> pair_beta_NCoup_source_constraints,
    pair_beta_NCoup_source_constraints -> beta_NCoup_source_constraints,
    pair_beta_NCoup_source_constraints -> constraint product object,
    pair_beta_NCoup_source_constraints -> all beta zero/diagonal components,
    alpha_NCoup_source_constraints and beta_NCoup_source_constraints
      -> parallel pair -> eq_NCoup_constraints_to_SubRep,
    eq_NCoup_constraints_to_SubRep -> LimCut_NCoup,
    constraint product object -> same product on all paths,
    same product on all paths -> C3*C5=C15,
    same product on all paths -> C5*C3=C15,
    same product on all paths -> C3*C3*C5=C45,
    same product on all paths -> F22 product,
    constraint product object -> source before points and graph objects,
    source before points and graph objects -> controls/DH/Epstein not points.

The exact self-dual constraint-product rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full source constraint-product payloads:

    Prod(T_C3(T_C5(z)))       = Prod(T_C15(z)),
    Prod(T_C5(T_C3(z)))       = Prod(T_C15(z)),
    Prod(T_C3(T_C3(T_C5(z)))) = Prod(T_C45(z)),
    Prod(T_C15(z*F22))        = Prod(z*(C15*F22)),
    Prod(T_C45(z*F22))        = Prod(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus bundled tuple labels, external products of sets, products after a
functor of points, component-checklist products, missing projections,
nonuniversal bundles, coproduct/sum substitutes, fiber products after graph
objects, projections after graph objects, local projection tables,
finite-sample products, basis-dependent projections, retuned/projected
component maps, graph-classifier products, declared products, and
control/DH/Epstein point-formability do not construct the source product.

The accepted datum is exactly:

    carrier-native,
    represented source fiber,
    actual source constraint product,
    actual source constraint object,
    actual component objects,
    actual source-native product projections,
    projections jointly determine pairings,
    actual product universal property,
    actual alpha pairing,
    actual beta pairing,
    alpha pairing unique,
    beta pairing unique,
    alpha components factor through projections,
    beta components factor through projections,
    alpha and beta parallel after product pairing,
    equalizer uses the product pair,
    same product on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    product before points,
    product before graph objects,
    controls not points,
    DH not points,
    Epstein not points,
    required product/projection edges present,
    no bundled tuple label,
    no external product of sets,
    no product after functor of points,
    no component-checklist product,
    no missing projection,
    no nonuniversal bundle,
    no coproduct/sum substitute,
    no fiber product after graph objects,
    no projection after graph objects,
    no local projection table,
    no finite-sample product,
    no basis-dependent projection,
    no retuned/projected component map,
    no graph-classifier product,
    no declared product,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER_CONSTRAINT_PRODUCT__SOURCE_PRODUCT_PROJECTIONS_AND_UNIQUE_PAIRINGS__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_product_contract`
verifies ten gates.

SCPP1 records the actual source product, projections, H1 profile, strict
rows, product-payload equalities, and connected product graph.

SCPP2 records again that graph identities do not supply the source product.

SCPP3 rejects bundled tuple labels, external products of sets,
component-checklist products, and declared products.

SCPP4 rejects nonuniversal bundles, coproduct/sum substitutes, missing
projections, and nonunique alpha/beta pairings.

SCPP5 rejects pointwise or graph-side products.

SCPP6 rejects local projection tables, finite-sample products,
basis-dependent projections, and retuned/projected component maps.

SCPP7 rejects graph-classifier products that leave controls, DH, and Epstein
formable.

SCPP8 proves every product/projection edge is mandatory.

SCPP9 proves only source products with universal pairings pass.

SCPP10 records the live predicate. The live product has projections and
unique alpha/beta pairings.

## 4. Effect on R1

This cycle fixes one more interface in the categorical square:

```text
Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control is acceptable only
as an actual source product with projections and universal pairings that
assemble alpha_NCoup_source_constraints and beta_NCoup_source_constraints.
```

The open construction target is now:

```text
construct Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control, its seven
source-native projections, and the unique pairings
pair_alpha_NCoup_source_constraints and pair_beta_NCoup_source_constraints,
or kill the strict-square branch at the source constraint-product interface.
```

No claim here proves R1 or RH. The document only prevents the next
categorical shortcut: replacing the source product by a bundle, tuple,
external product, component checklist, late product, local table, retuning, or
declared product.

## 5. Acceptance and kill conditions

ACCEPT-SCPP.1 Exhibit
`Prod_NCoup_endpoint_degree_dd4_push_graph_rosati_control`.

ACCEPT-SCPP.2 Exhibit the seven source-native projections
`pi_NCoup_endpoint_integrality`, `pi_NCoup_degree_maps`,
`pi_NCoup_dd4_boundary`, `pi_NCoup_boundary_pushforward`,
`pi_NCoup_graph_composition`, `pi_NCoup_rosati_count`, and
`pi_NCoup_control_death`.

ACCEPT-SCPP.3 Prove the source product universal property.

ACCEPT-SCPP.4 Prove the projections jointly determine unique pairings.

ACCEPT-SCPP.5 Exhibit and prove uniqueness of
`pair_alpha_NCoup_source_constraints` and
`pair_beta_NCoup_source_constraints`.

ACCEPT-SCPP.6 Prove alpha/beta components factor through the projections and
the equalizer uses this product pair.

ACCEPT-SCPP.7 Prove the same source product transports all
C3/C5/C15/C45/F22 paths.

ACCEPT-SCPP.8 Prove controls/DH/Epstein are non-points before points and
graph objects exist.

KILL-SCPP.1 Kill any bundled tuple label, external product of sets, product
after functor of points, component-checklist product, missing projection,
nonuniversal bundle, coproduct/sum substitute, late fiber product, late
projection, local projection table, finite-sample product, basis-dependent
projection, retuned/projected component map, graph-classifier product,
declared product, or point-formable control/DH/Epstein repair.
