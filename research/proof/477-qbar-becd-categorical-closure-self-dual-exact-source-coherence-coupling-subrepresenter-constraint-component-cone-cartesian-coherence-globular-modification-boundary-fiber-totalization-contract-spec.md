# 477 - Qbar_BECD categorical closure self-dual exact-source coherence-coupling subrepresenter constraint-component-cone cartesian-coherence globular-modification boundary-fiber totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-fortieth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 476 left the categorical closure branch live only if the represented
cartesian component-cone coherence cells assemble as one source-level globular
modification inside the same represented categorical source square and
totalized cube:

```text
    Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components.
```

This document fixes the next edge. A source-level globular modification is
still not enough if it is a chosen section over a boundary, a contractible
choice wrapper without a represented fiber, or an external boundary-fiber
table. The modification must be selected by an actual source boundary map and
represented boundary fiber:

```text
    res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd,
    Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components.
```

The fiber must be over the fixed boundary
`GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components`; its universal
arrow must select
`Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components`; and any
contractibility claim is admissible only after that represented fiber exists.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_totalization_contract`
(CATSCARTCOHGBFQBARBECD1-CATSCARTCOHGBFQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 476 through the DD.4 SCC interface (170/170 exit 0).

## 1. Purpose

After doc 476, the cheap repair is:

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
construct res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd; construct
the represented fiber
Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components over
GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components; prove
eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components selects
Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components; prove the
fiber preserves the source and target boundaries, pasting faces, whiskering,
vertical/horizontal composition, coefficients, signed support, and
source-before-points order.
```

## 2. Lemma

```text
Lemma 477.1 (the globular modification must be a represented boundary fiber).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted boundary-fiber data are:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle,
    BCCube_CatSq_Qbar_BECD_facets,
    Tot_BCCube_CatSq_Qbar_BECD,
    Rep_BCCube_Qbar_BECD_source_fiber,
    eta_BCCube_Qbar_BECD_source,
    eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    CartLift_BCCube_Qbar_BECD_multiplier_source_fiber,
    Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd,
    Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    boundary preservation,
    unique source filler after the represented fiber,
    contractibility only after the represented fiber,
    the seven doc-473 component legs,
    the seven doc-472 component objects,
    the seven doc-471 projections,
    dd4_c_original_res1_Qbar_BECD,
    Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD.

The boundary-fiber graph contains the live edges:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle -> Rep_BCCube_Qbar_BECD_source_fiber,
    Tot_BCCube_CatSq_Qbar_BECD -> Rep_BCCube_Qbar_BECD_source_fiber,
    Rep_BCCube_Qbar_BECD_source_fiber -> eta_BCCube_Qbar_BECD_source,
    eta_BCCube_Qbar_BECD_source -> cartesian source coherence,
    eta_BCCube_Qbar_BECD_source -> eta_NCoup,
    eta_NCoup -> CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd,
    res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd -> GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd -> Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> selected globular modification,
    selected globular modification -> Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> unique source filler,
    unique source filler -> contractible after represented fiber,
    Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components -> boundary preservation,
    boundary preservation -> GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
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

`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_totalization_contract`
verifies ten gates.

CATSCARTCOHGBFQBARBECD1 records the represented boundary fiber, H1 profile, strict rows, mixed
path equalities, and connected boundary-fiber graph.

CATSCARTCOHGBFQBARBECD2 records again that graph identities do not supply the boundary fiber.

CATSCARTCOHGBFQBARBECD3 rejects chosen boundary sections and contractible-choice wrappers
without a representer.

CATSCARTCOHGBFQBARBECD4 rejects fibers over the wrong globular boundary.

CATSCARTCOHGBFQBARBECD5 rejects external, quotient, or local boundary fibers.

CATSCARTCOHGBFQBARBECD6 rejects pointwise, graph-side, and post-product boundary fibers.

CATSCARTCOHGBFQBARBECD7 rejects retuned or reindexed boundary fibers.

CATSCARTCOHGBFQBARBECD8 makes every boundary-fiber edge mandatory.

CATSCARTCOHGBFQBARBECD9 records that graph-side boundary fibers still leave controls, DH, and
Epstein formable.

CATSCARTCOHGBFQBARBECD10 accepts only represented source boundary fibers.

Therefore a candidate that satisfies doc 476 with one source-level globular
modification is still incomplete unless that modification is selected by a
represented source fiber over the named globular boundary.

## 4. Consequence

The live categorical closure branch is now:

```text
construct Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components over
GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components and prove its universal arrow
selects Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components while preserving every
component/projection/pairing boundary, every C3/C5/C15/C45/F22 pasting face,
coefficients, signed support, and source-before-points order.
```

The open construction target is no longer "choose the globular modification."
It is "make the modification the represented boundary fiber over the fixed
globular boundary."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd;
2. Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components;
3. eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components;
4. proof that the fiber is over GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components;
5. proof that the fiber arrow selects Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components;
6. proof of unique source filler after the represented fiber exists;
7. proof that any contractibility is downstream of representation;
8. proof that all source/target boundary data and pasting faces are preserved;
9. proof that coefficients and signed support are preserved on every path;
10. proof that the fiber is formed before points and graph objects.
```

Until the globular modification is represented as this boundary fiber, the
object remains missing.
