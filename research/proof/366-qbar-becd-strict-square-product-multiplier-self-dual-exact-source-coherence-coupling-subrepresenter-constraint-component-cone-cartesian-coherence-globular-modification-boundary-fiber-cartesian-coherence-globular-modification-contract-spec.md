# 366 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter constraint-component-cone cartesian-coherence globular-modification boundary-fiber cartesian-coherence globular-modification contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-twenty-ninth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 365 left the strict-square branch live only if the cartesian boundary
fiber has represented coherence cells:

```text
    Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    cell_C3_C5_C15_NCoup_boundary_fiber,
    cell_C5_C3_C15_NCoup_boundary_fiber,
    cell_C3_C3_C5_C45_NCoup_boundary_fiber,
    cell_F22_interchange_NCoup_boundary_fiber,
    cell_boundary_restriction_cartesian_naturality_NCoup,
    cell_boundary_fiber_arrow_cartesian_naturality_NCoup,
    cell_fixed_globular_boundary_pullback_NCoup.
```

This document fixes the next edge. A represented list of boundary-fiber
coherence cells is still not enough if those cells do not share one
2-dimensional source/target boundary. The cells must be faces of one
source-level globular modification:

```text
    Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    GlobBd_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components.
```

The source boundary must be the boundary-restriction and fiber-arrow
naturality data. The target boundary must bind the fixed globular boundary,
component/projection boundary, pair_alpha/pair_beta boundary, and pasting
faces. The C3/C5/C15/C45/F22 cells must be faces of the same modification,
with whiskering, vertical/horizontal composition, associativity,
interchange, coefficient preservation, and signed-support preservation built
before points and graph objects.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_contract`
(SCFG1-SCFG10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_cartesian_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_contract`,
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

After doc 365, the cheap repair is:

```text
produce the named cartesian boundary-fiber coherence cells and say they are
generated by CartFib_Mod_Coh_CartCone_NCoup_eta_source_components.
```

That still does not construct the missing object. A represented coherence
cell is usable in the square only when its source and target boundaries paste
into the same source-side 2-dimensional object. Otherwise the candidate can
name every boundary-fiber cell while assigning separate or incompatible
boundaries to boundary restriction, fiber universal arrow, fixed boundary,
component/projection data, pair_alpha/pair_beta, and pasting faces.

The live branch narrows from "represented cartesian boundary-fiber coherence
cells" to:

```text
construct Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components; prove
it is generated from Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components;
prove it has shared boundary
GlobBd_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components; prove its
source boundary is exactly boundary-restriction and fiber-arrow naturality;
prove its target boundary is exactly fixed-boundary/component/projection/
pair_alpha/pair_beta/pasting-face naturality; prove the C3*C5=C15,
C5*C3=C15, C3*C3*C5=C45, and F22 cells are faces of this same modification;
and prove all of this is source-level, carrier native, coefficient
preserving, signed-support preserving, and before points and graph objects.
```

## 2. Lemma

```text
Lemma 366.1 (boundary-fiber coherence cells must globularize).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted boundary-fiber coherence globular-modification data are:

    Rep_Qbar_BECD_source_fiber,
    eta_Qbar_BECD_source,
    Cart_Qbar_BECD_BCF_self_dual_exact_source,
    Mod_Coh_CartCone_NCoup_eta_source_components,
    GlobBd_CartCone_NCoup_eta_source_components,
    res_Mod_Coh_CartCone_to_GlobBd_NCoup,
    Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    cart_res_Mod_Coh_CartCone_to_GlobBd_NCoup,
    Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    GlobBd_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    source boundary = boundary-restriction and fiber-arrow naturality,
    target boundary = fixed-boundary/component/projection/pair/pasting naturality,
    C3*C5=C15 boundary-fiber coherence face,
    C5*C3=C15 boundary-fiber coherence face,
    C3*C3*C5=C45 boundary-fiber coherence face,
    F22 boundary-fiber interchange face,
    dd4_c_original_res1,
    CTRL_Qbar_BECD_coherent_death.

The exact self-dual boundary-fiber coherence modification rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full boundary-fiber coherence modification
payloads:

    FibCohMod(T_C3(T_C5(z)))       = FibCohMod(T_C15(z)),
    FibCohMod(T_C5(T_C3(z)))       = FibCohMod(T_C15(z)),
    FibCohMod(T_C3(T_C3(T_C5(z)))) = FibCohMod(T_C45(z)),
    FibCohMod(T_C15(z*F22))        = FibCohMod(z*(C15*F22)),
    FibCohMod(T_C45(z*F22))        = FibCohMod(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus independent fiber-coherence cell lists, boundary-mismatched pasting
diagrams, separate boundary-restriction modifications, separate fiber-arrow
modifications, separate fixed-boundary modifications, homotopy fillers after
points, lax modifications, graph-side modifications, pointwise modifications,
retuned modifications, reindexed modification labels, post-product
modifications, and control/DH/Epstein point-formability do not construct the
boundary-fiber coherence globular modification.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_contract`
verifies ten gates.

SCFG1 records the source-level boundary-fiber coherence globular modification,
its seven faces, H1 profile, strict rows, mixed path equalities, and connected
modification graph.

SCFG2 records again that graph identities do not supply a source
fiber-coherence modification.

SCFG3 rejects independent represented fiber-coherence cell lists.

SCFG4 rejects boundary-mismatched fiber pasting diagrams.

SCFG5 rejects split boundary-restriction, fiber-arrow, and fixed-boundary
modifications.

SCFG6 rejects homotopy, lax, pointwise, graph-side, and post-product fillers.

SCFG7 rejects retuned or reindexed fiber-coherence modifications.

SCFG8 makes every fiber-coherence modification edge mandatory.

SCFG9 records that graph-side fiber-coherence modifications still leave
controls, DH, and Epstein formable.

SCFG10 accepts only one source globular fiber-coherence modification.

Therefore a candidate that satisfies doc 365 with represented cartesian
boundary-fiber coherence cells is still incomplete unless those cells assemble
as one source-level globular modification with shared source and target
boundaries.

## 4. Consequence

The live strict-square branch is now:

```text
construct Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components and
GlobBd_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components; prove the
source boundary is boundary-restriction plus fiber-arrow naturality; prove the
target boundary binds fixed-boundary, component/projection, pair_alpha/beta,
and pasting-face naturality; prove C3/C5/C15/C45/F22 cells are faces of this
same modification; and prove whiskering, vertical/horizontal composition,
coefficient, signed-support, and source-before-points preservation.
```

The open construction target is no longer "make the cartesian boundary-fiber
transport represented by coherence cells." It is "make those cells one
globular source-side modification."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components;
2. GlobBd_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components;
3. proof that the modification is generated by the cartesian boundary-fiber coherence object;
4. proof that the source boundary is boundary-restriction and fiber-arrow naturality;
5. proof that the target boundary binds fixed-boundary/component/projection/pair/pasting naturality;
6. proof that C3*C5=C15, C5*C3=C15, C3*C3*C5=C45, and F22 are faces;
7. proof of whiskering compatibility with the cartesian boundary restriction and fiber arrow;
8. proof of vertical/horizontal composition, associativity, and interchange;
9. proof of coefficient and signed-support preservation;
10. proof that the modification is formed before points and graph objects.
```

Until this source-level globular modification exists, the object remains
missing.
