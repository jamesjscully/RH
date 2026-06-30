# 474 - Qbar_BECD categorical closure self-dual exact-source coherence-coupling subrepresenter constraint-component-cone cartesian totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-thirty-seventh cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 473 left the categorical closure branch live only if the seven categorical
source component legs are one eta-generated component cone:

```text
    Cone_NCoup_BCCube_Qbar_BECD_eta_source_components,
```

generated from:

```text
    eta_BCCube_Qbar_BECD_source,
    eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source.
```

This document fixes the next edge. An eta-generated cone is still not enough
if its transport is only checked on selected paths, supplied by chosen
isomorphisms, or made natural only after applying points or graph objects.
The cone must be cartesian over the represented source lifts:

```text
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source.
```

The cartesian cone must carry component-leg naturality and projection-leg
naturality for both product pairings:

```text
    pair_alpha_NCoup_BCCube_Qbar_BECD_source_constraints,
    pair_beta_NCoup_BCCube_Qbar_BECD_source_constraints.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_totalization_contract`
(CATSCARTCONEQBARBECD1-CATSCARTCONEQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 473 through the DD.4 SCC interface (167/167 exit 0).

## 1. Purpose

After doc 473, the cheap repair is:

```text
give one eta-generated component cone, verify the named C3/C5/C15/C45/F22
rows, and call the cone stable.
```

That still does not construct the missing object. The square needs source
fibration stability, not finite row coincidence. The eta-generated cone must
pull back cartesianly along the represented source lifts, preserve the same
doc-473 cone and doc-472 component objects under base change, and make
`pair_alpha` and `pair_beta` natural with respect to those pullbacks.

The live branch therefore narrows from "eta-generated component cone" to:

```text
construct CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components over
Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source; prove every represented
cartesian source lift pulls back Cone_NCoup_BCCube_Qbar_BECD_eta_source_components to the same
source cone; prove all seven component legs and all seven projection-leg
equalities are natural; prove pair_alpha and pair_beta are cartesian-natural;
and prove this happens before points and graph objects.
```

## 2. Lemma

```text
Lemma 474.1 (the eta-generated categorical component cone must be cartesian).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted cartesian component-cone data are:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle,
    BCCube_CatSq_Qbar_BECD_facets,
    Tot_BCCube_CatSq_Qbar_BECD,
    Rep_BCCube_Qbar_BECD_source_fiber,
    eta_BCCube_Qbar_BECD_source,
    eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Cone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    CartLift_BCCube_Qbar_BECD_multiplier_source_fiber,
    Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Prod_NCoup_BCCube_Qbar_BECD_endpoint_degree_dd4_push_graph_rosati_control,
    pair_alpha_NCoup_BCCube_Qbar_BECD_source_constraints,
    pair_beta_NCoup_BCCube_Qbar_BECD_source_constraints,
    the seven doc-473 component legs,
    the seven doc-472 component objects,
    the seven doc-471 projections,
    dd4_c_original_res1_Qbar_BECD,
    Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD.

The cartesian component-cone dependency graph contains the live edges:

    represented source square -> Rep_BCCube_Qbar_BECD_source_fiber,
    source cube totalization -> Rep_BCCube_Qbar_BECD_source_fiber,
    Rep_BCCube_Qbar_BECD_source_fiber -> eta_BCCube_Qbar_BECD_source,
    eta_BCCube_Qbar_BECD_source -> cartesian source lifts,
    eta_BCCube_Qbar_BECD_source
        -> eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source
        -> Cone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Cone_NCoup_BCCube_Qbar_BECD_eta_source_components -> CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    cartesian source lifts -> CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> C3/C5/C15/C45/F22 cone pullbacks,
    every cone pullback -> component-leg naturality,
    component-leg naturality -> all seven component legs natural,
    component-leg naturality -> projection-leg naturality,
    projection-leg naturality -> pair_alpha cartesian natural,
    projection-leg naturality -> pair_beta cartesian natural,
    pair_alpha cartesian natural -> constraint product object,
    pair_beta cartesian natural -> zero/diagonal cartesian cone,
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> same cartesian cone on all paths,
    same cartesian cone on all paths -> C3*C5=C15,
    same cartesian cone on all paths -> C5*C3=C15,
    same cartesian cone on all paths -> C3*C3*C5=C45,
    same cartesian cone on all paths -> F22 product,
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> base change preserves doc-473 cone,
    base change preserves doc-473 cone -> base change preserves components,
    base change preserves components -> doc-472 component objects,
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> source before points and graph objects,
    source before points and graph objects -> controls/DH/Epstein not points.

The exact self-dual cartesian component-cone rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full cartesian source component-cone
payloads:

    CartCone(T_C3(T_C5(z)))       = CartCone(T_C15(z)),
    CartCone(T_C5(T_C3(z)))       = CartCone(T_C15(z)),
    CartCone(T_C3(T_C3(T_C5(z)))) = CartCone(T_C45(z)),
    CartCone(T_C15(z*F22))        = CartCone(z*(C15*F22)),
    CartCone(T_C45(z*F22))        = CartCone(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus finite path checks, sampled path transport, pointwise naturality,
graph-side base change, local transport tables, chosen transport
isomorphisms, up-to-isomorphism claims without coherence, lax naturality,
noncartesian pullbacks, reindexed cone labels, retuned transport,
base-changed component replacements, declared naturality squares, split
componentwise naturality, and control/DH/Epstein point-formability do not
construct the cartesian source component cone.

The accepted datum is exactly:

    carrier-native,
    represented categorical source square,
    totalized source cube,
    represented source fiber,
    actual source universal arrow,
    actual coupling universal arrow,
    actual doc-473 component cone,
    actual cartesian source lifts,
    actual cartesian component cone,
    actual cone pullbacks,
    actual component-leg naturality,
    actual projection-leg naturality,
    pair_alpha cartesian natural,
    pair_beta cartesian natural,
    base change preserves the doc-473 cone,
    base change preserves the doc-472 components,
    same cartesian cone on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    cone before points,
    cone before graph objects,
    controls not points,
    DH not points,
    Epstein not points,
    required cartesian component-cone edges present,
    no finite path check only,
    no sampled path transport,
    no pointwise naturality,
    no graph-side base change,
    no local transport table,
    no chosen transport isomorphisms,
    no up-to-isomorphism without coherence,
    no lax naturality only,
    no noncartesian pullback,
    no reindexed cone label,
    no retuned transport,
    no base-changed component replacement,
    no declared naturality square,
    no split naturality by component,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_CATEGORICAL_CLOSURE_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER_CONSTRAINT_COMPONENT_CONE_CARTESIAN_TOTALIZATION__SOURCE_FIBRATION_NATURALITY__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_totalization_contract`
verifies ten gates.

CATSCARTCONEQBARBECD1 records the cartesian component cone, H1 profile,
categorical rows, cartesian-cone payload equalities, and connected naturality
graph.

CATSCARTCONEQBARBECD2 records again that graph identities do not supply cartesian cone
naturality.

CATSCARTCONEQBARBECD3 rejects finite path checks and declared naturality squares.

CATSCARTCONEQBARBECD4 rejects pointwise or graph-side base change.

CATSCARTCONEQBARBECD5 rejects local, chosen, up-to-isomorphism, or lax transport.

CATSCARTCONEQBARBECD6 rejects reindexed or retuned base changes that replace the cone.

CATSCARTCONEQBARBECD7 records that split componentwise naturality still leaves controls, DH,
and Epstein formable.

CATSCARTCONEQBARBECD8 makes every cartesian component-cone edge mandatory.

CATSCARTCONEQBARBECD9 accepts only cartesian eta-component cones.

CATSCARTCONEQBARBECD10 records the live cone as natural for `pair_alpha` and `pair_beta` over
the represented cartesian source lifts.

Therefore a candidate that satisfies doc 473 only by producing one
eta-generated cone is still incomplete unless that cone is cartesian over the
represented source fibration.

## 4. Consequence

The live categorical closure branch is now:

```text
construct CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components and prove the doc-473 cone,
its seven component legs, the seven projection-leg equalities, pair_alpha,
and pair_beta are natural for the represented cartesian source lifts before
points and graph objects exist.
```

The open construction target is no longer "give one eta-generated component
cone." It is "make that cone cartesian over the source fibration so no
finite-table, chosen-transport, pointwise, or graph-side replacement can
stand in for the missing object."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components;
2. proof that it is built over Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source;
3. proof that all cartesian source lifts pull back the doc-473 cone;
4. proof of naturality for all seven component legs;
5. proof of naturality for all seven projection-leg equalities;
6. proof that pair_alpha and pair_beta are cartesian-natural;
7. proof that base change preserves the doc-472 component objects;
8. proof that the same cartesian cone transports on C3/C5/C15/C45/F22 paths;
9. proof that this is before points and graph objects;
10. proof that no finite/sample/pointwise/graph-side/chosen/lax/noncartesian/
    reindexed/retuned/split replacement is being used.
```

Until the eta-generated source component cone is made cartesian, the object
remains missing.
