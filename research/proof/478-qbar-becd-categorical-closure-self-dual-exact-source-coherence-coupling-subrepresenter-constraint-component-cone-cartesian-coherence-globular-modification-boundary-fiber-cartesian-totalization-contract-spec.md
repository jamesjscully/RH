# 478 - Qbar_BECD categorical closure self-dual exact-source coherence-coupling subrepresenter constraint-component-cone cartesian-coherence globular-modification boundary-fiber cartesian totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-forty-first cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 477 left the categorical closure branch live only if the globular
modification is selected by a represented source boundary fiber inside the
same represented categorical source square and totalized cube:

```text
    Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components.
```

This document fixes the next edge. A represented boundary fiber over one
globular boundary is still not enough if the fiber is static, rebuilt after
base change, transported by chosen local tables, or checked only after points
or graph objects. The boundary fiber must itself be cartesian over the same
source multiplier lifts:

```text
    CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    cart_res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd.
```

The cartesian boundary fiber must transport the boundary restriction map and
the fiber universal arrow along the C3/C5/C15/C45/F22 source paths, while
preserving the fixed globular boundary, component/projection boundaries,
pair_alpha/pair_beta target boundary, pasting faces, coefficients, and signed
support before points and graph objects.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_cartesian_totalization_contract`
(CATSCARTCOHGBFCARTQBARBECD1-CATSCARTCOHGBFCARTQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 477 through the DD.4 SCC interface (171/171 exit 0).

## 1. Purpose

After doc 477, the cheap repair is:

```text
construct one represented fiber over GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components
and then reuse that fiber name for every multiplier path.
```

That still does not construct the missing object. The square needs the fiber
to pull back cartesianly over the represented source lifts. If the fiber is
rebuilt after base change or transported by local choices, the modification
can select the right boundary at one point while failing C3*C5=C15,
C5*C3=C15, C3*C3*C5=C45, or F22 compatibility.

The live branch narrows from "represented boundary fiber" to:

```text
construct CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components; prove
cart_res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd is cartesian-natural; prove
eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components transports cartesianly;
prove the same boundary fiber appears on the C3*C5=C15, C5*C3=C15,
C3*C3*C5=C45, and F22 paths; and prove the fixed boundary, source/target
boundaries, pasting faces, coefficients, signed support, and source-before
points order are preserved.
```

## 2. Lemma

```text
Lemma 478.1 (the represented boundary fiber must be cartesian).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted cartesian boundary-fiber data are:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle,
    BCCube_CatSq_Qbar_BECD_facets,
    Tot_BCCube_CatSq_Qbar_BECD,
    Rep_BCCube_Qbar_BECD_source_fiber,
    eta_BCCube_Qbar_BECD_source,
    CartLift_BCCube_Qbar_BECD_multiplier_source_fiber,
    Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    GlobBd_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd,
    Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components,
    cart_res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd,
    dd4_c_original_res1_Qbar_BECD,
    Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD.

The cartesian boundary-fiber graph contains the live edges:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle -> Rep_BCCube_Qbar_BECD_source_fiber,
    Tot_BCCube_CatSq_Qbar_BECD -> Rep_BCCube_Qbar_BECD_source_fiber,
    Rep_BCCube_Qbar_BECD_source_fiber -> eta_BCCube_Qbar_BECD_source,
    eta_BCCube_Qbar_BECD_source -> CartLift_BCCube_Qbar_BECD_multiplier_source_fiber,
    CartLift_BCCube_Qbar_BECD_multiplier_source_fiber -> cartesian source coherence,
    CartLift_BCCube_Qbar_BECD_multiplier_source_fiber -> cartesian boundary fiber,
    eta_BCCube_Qbar_BECD_source -> cartesian source coherence,
    eta_BCCube_Qbar_BECD_source -> globular modification,
    cartesian source coherence -> cartesian boundary fiber,
    globular modification -> boundary restriction map,
    boundary restriction map -> represented boundary fiber,
    represented boundary fiber -> cartesian boundary fiber,
    boundary restriction map -> cartesian boundary restriction,
    cartesian boundary restriction -> cartesian boundary fiber,
    cartesian boundary fiber -> fiber universal arrow,
    fiber universal arrow -> selected globular modification,
    selected globular modification -> globular modification,
    cartesian boundary fiber -> fixed globular boundary pullback,
    fixed globular boundary pullback -> shared globular boundary,
    cartesian boundary fiber -> C3*C5=C15 fiber pullback,
    cartesian boundary fiber -> C5*C3=C15 fiber pullback,
    cartesian boundary fiber -> C3*C3*C5=C45 fiber pullback,
    cartesian boundary fiber -> F22 fiber pullback,
    all fiber pullbacks -> same cartesian fiber on all paths,
    same cartesian fiber on all paths -> C3*C5=C15,
    same cartesian fiber on all paths -> C5*C3=C15,
    same cartesian fiber on all paths -> C3*C3*C5=C45,
    same cartesian fiber on all paths -> F22 product,
    cartesian boundary fiber -> component boundary cartesian,
    cartesian boundary fiber -> projection boundary cartesian,
    cartesian boundary fiber -> pair_alpha/beta boundary cartesian,
    cartesian boundary fiber -> pasting faces cartesian,
    cartesian boundary fiber -> coefficient preservation,
    cartesian boundary fiber -> signed-support preservation,
    cartesian boundary fiber -> source before points and graph objects,
    source before points and graph objects -> controls/DH/Epstein not points.

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

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus static one-boundary fibers, chosen base-change fibers, fibers rebuilt
after base change, noncartesian pullbacks, local transport tables, pointwise
cartesian fibers, graph-side cartesian fibers, post-product cartesian fibers,
retuned cartesian fibers, reindexed cartesian fibers, and
control/DH/Epstein point-formability do not construct the cartesian boundary
fiber.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cartesian_coherence_globular_modification_boundary_fiber_cartesian_totalization_contract`
verifies ten gates.

CATSCARTCOHGBFCARTQBARBECD1 records the cartesian boundary fiber, H1 profile, strict rows, mixed
path equalities, and connected cartesian boundary-fiber graph.

CATSCARTCOHGBFCARTQBARBECD2 records again that graph identities do not supply cartesian fiber
transport.

CATSCARTCOHGBFCARTQBARBECD3 rejects static one-boundary fibers.

CATSCARTCOHGBFCARTQBARBECD4 rejects noncartesian pullbacks that fail to preserve boundary data.

CATSCARTCOHGBFCARTQBARBECD5 rejects chosen local fiber transport and fibers rebuilt after base
change.

CATSCARTCOHGBFCARTQBARBECD6 rejects pointwise, graph-side, and post-product cartesian fibers.

CATSCARTCOHGBFCARTQBARBECD7 rejects retuned or reindexed cartesian fibers.

CATSCARTCOHGBFCARTQBARBECD8 makes every cartesian boundary-fiber edge mandatory.

CATSCARTCOHGBFCARTQBARBECD9 records that graph-side cartesian fibers still leave controls, DH, and
Epstein formable.

CATSCARTCOHGBFCARTQBARBECD10 accepts only cartesian represented boundary fibers.

Therefore a candidate that satisfies doc 477 with a represented boundary
fiber is still incomplete unless that fiber is cartesian over the represented
source multiplier lifts.

## 4. Consequence

The live categorical closure branch is now:

```text
construct CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components and prove the
boundary restriction map, fiber universal arrow, fixed globular boundary,
source/target boundary data, pasting faces, coefficients, and signed support
all transport cartesianly over C3/C5/C15/C45/F22 before points and graph
objects exist.
```

The open construction target is no longer "make the modification a
represented boundary fiber." It is "make that boundary fiber cartesian over
the source multiplier lifts."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. CartFib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components;
2. cart_res_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_to_GlobBd;
3. proof that the boundary restriction is cartesian-natural;
4. proof that eta_Fib_Mod_Coh_CartCone_NCoup_BCCube_Qbar_BECD_eta_source_components transports cartesianly;
5. proof that the fixed globular boundary pulls back to itself;
6. proof that component/projection/pair_alpha/beta boundaries pull back;
7. proof that C3/C5/C15/C45/F22 pasting faces pull back;
8. proof of the same boundary fiber on all multiplier paths;
9. proof that coefficients and signed support are preserved;
10. proof that the cartesian fiber is formed before points and graph objects.
```

Until the represented boundary fiber is cartesian in this sense, the object
remains missing.
