# 363 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter constraint-component-cone cartesian-coherence globular-modification boundary-fiber contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-twenty-sixth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 362 left the strict-square branch live only if the represented
cartesian-cone coherence cells assemble as one source-level globular
modification:

```text
    Mod_Coh_CartCone_NCoup_eta_source_components,
    GlobBd_CartCone_NCoup_eta_source_components.
```

This document fixes the next edge. A source-level globular modification is
still not enough if it is a chosen section over a boundary, a contractible
choice wrapper without a represented fiber, or an external boundary-fiber
table. The modification must be selected by an actual source boundary map and
represented boundary fiber:

```text
    res_Mod_Coh_CartCone_to_GlobBd_NCoup,
    Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components.
```

The fiber must be over the fixed boundary
`GlobBd_CartCone_NCoup_eta_source_components`; its universal arrow must select
`Mod_Coh_CartCone_NCoup_eta_source_components`; and any contractibility claim
is admissible only after that represented fiber exists.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_contract`
(SCGB1-SCGB10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
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

After doc 362, the cheap repair is:

```text
give a globular modification and then choose it as the boundary filler.
```

That still does not construct the missing object. The square must supply the
boundary restriction map from modifications to their globular boundary and
the represented source fiber over the fixed boundary. Otherwise the filler is
only an external section or a contractible choice label, which doc 303 already
forbids as a replacement for represented geometry.

The live branch narrows from "one source-level globular modification" to:

```text
construct res_Mod_Coh_CartCone_to_GlobBd_NCoup; construct the represented
fiber Fib_Mod_Coh_CartCone_NCoup_eta_source_components over
GlobBd_CartCone_NCoup_eta_source_components; prove
eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components selects
Mod_Coh_CartCone_NCoup_eta_source_components; prove the fiber preserves the
source and target boundaries, pasting faces, whiskering, vertical/horizontal
composition, coefficients, signed support, and source-before-points order.
```

## 2. Lemma

```text
Lemma 363.1 (the globular modification must be a represented boundary fiber).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted boundary-fiber data are:

    Rep_Qbar_BECD_source_fiber,
    eta_Qbar_BECD_source,
    eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    CartCone_NCoup_eta_source_components,
    Coh_CartCone_NCoup_eta_source_components,
    Mod_Coh_CartCone_NCoup_eta_source_components,
    GlobBd_CartCone_NCoup_eta_source_components,
    res_Mod_Coh_CartCone_to_GlobBd_NCoup,
    Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    boundary preservation,
    unique source filler after the represented fiber,
    contractibility only after the represented fiber,
    dd4_c_original_res1,
    CTRL_Qbar_BECD_coherent_death.

The boundary-fiber graph contains the live edges:

    eta_Qbar_BECD_source -> cartesian source coherence,
    eta_Qbar_BECD_source -> eta_NCoup,
    eta_NCoup -> CartCone_NCoup_eta_source_components,
    CartCone_NCoup_eta_source_components -> Coh_CartCone_NCoup_eta_source_components,
    Coh_CartCone_NCoup_eta_source_components -> Mod_Coh_CartCone_NCoup_eta_source_components,
    Mod_Coh_CartCone_NCoup_eta_source_components -> GlobBd_CartCone_NCoup_eta_source_components,
    Mod_Coh_CartCone_NCoup_eta_source_components -> res_Mod_Coh_CartCone_to_GlobBd_NCoup,
    res_Mod_Coh_CartCone_to_GlobBd_NCoup -> GlobBd_CartCone_NCoup_eta_source_components,
    res_Mod_Coh_CartCone_to_GlobBd_NCoup -> Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    GlobBd_CartCone_NCoup_eta_source_components -> Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    Fib_Mod_Coh_CartCone_NCoup_eta_source_components -> eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components -> selected globular modification,
    selected globular modification -> Mod_Coh_CartCone_NCoup_eta_source_components,
    Fib_Mod_Coh_CartCone_NCoup_eta_source_components -> unique source filler,
    unique source filler -> contractible after represented fiber,
    Fib_Mod_Coh_CartCone_NCoup_eta_source_components -> boundary preservation,
    boundary preservation -> GlobBd_CartCone_NCoup_eta_source_components,
    boundary preservation -> component/projection naturality boundaries,
    boundary preservation -> pair_alpha/pair_beta target boundary,
    boundary preservation -> C3/C5/C15/C45/F22 pasting faces,
    boundary preservation -> coefficient preservation,
    boundary preservation -> signed-support preservation,
    boundary preservation -> source before points and graph objects,
    source before points and graph objects -> controls/DH/Epstein not points.

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

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus chosen boundary sections, contractible-choice wrappers without a
represented fiber, fibers over the wrong boundary, external boundary fibers,
quotient boundary fibers, local boundary-fiber tables, pointwise boundary
fibers, graph-side boundary fibers, post-product boundary fibers, retuned
boundary restrictions, reindexed boundary fibers, and control/DH/Epstein
point-formability do not construct the represented boundary fiber.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_contract`
verifies ten gates.

SCGB1 records the represented boundary fiber, H1 profile, strict rows, mixed
path equalities, and connected boundary-fiber graph.

SCGB2 records again that graph identities do not supply the boundary fiber.

SCGB3 rejects chosen boundary sections and contractible-choice wrappers
without a representer.

SCGB4 rejects fibers over the wrong globular boundary.

SCGB5 rejects external, quotient, or local boundary fibers.

SCGB6 rejects pointwise, graph-side, and post-product boundary fibers.

SCGB7 rejects retuned or reindexed boundary fibers.

SCGB8 makes every boundary-fiber edge mandatory.

SCGB9 records that graph-side boundary fibers still leave controls, DH, and
Epstein formable.

SCGB10 accepts only represented source boundary fibers.

Therefore a candidate that satisfies doc 362 with one source-level globular
modification is still incomplete unless that modification is selected by a
represented source fiber over the named globular boundary.

## 4. Consequence

The live strict-square branch is now:

```text
construct Fib_Mod_Coh_CartCone_NCoup_eta_source_components over
GlobBd_CartCone_NCoup_eta_source_components and prove its universal arrow
selects Mod_Coh_CartCone_NCoup_eta_source_components while preserving every
component/projection/pairing boundary, every C3/C5/C15/C45/F22 pasting face,
coefficients, signed support, and source-before-points order.
```

The open construction target is no longer "choose the globular modification."
It is "make the modification the represented boundary fiber over the fixed
globular boundary."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. res_Mod_Coh_CartCone_to_GlobBd_NCoup;
2. Fib_Mod_Coh_CartCone_NCoup_eta_source_components;
3. eta_Fib_Mod_Coh_CartCone_NCoup_eta_source_components;
4. proof that the fiber is over GlobBd_CartCone_NCoup_eta_source_components;
5. proof that the fiber arrow selects Mod_Coh_CartCone_NCoup_eta_source_components;
6. proof of unique source filler after the represented fiber exists;
7. proof that any contractibility is downstream of representation;
8. proof that all source/target boundary data and pasting faces are preserved;
9. proof that coefficients and signed support are preserved on every path;
10. proof that the fiber is formed before points and graph objects.
```

Until the globular modification is represented as this boundary fiber, the
object remains missing.
