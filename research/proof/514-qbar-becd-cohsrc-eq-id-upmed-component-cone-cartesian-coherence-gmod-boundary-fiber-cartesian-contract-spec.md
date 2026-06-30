# 514 - Qbar_BECD categorical closure coherent source-presentation eta-lift equalizer-identity universal-mediator component-cone cartesian-coherence globular-modification boundary-fiber cartesian component-object product-projected parallel-morphism finite-limit subrepresented coupled formation-coherent self-dual exact-BCF-certificate contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-seventy-seventh cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 513 left the equalizer-identity mediator branch live only if the
doc-512 globular modification is selected by a represented boundary fiber:

```text
res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd,
Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
eta_Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components.
```

This document fixes the next edge. A represented boundary fiber over one
fixed globular boundary is still not enough if the fiber is static, merely
reused by name after base change, rebuilt after base change, transported by
chosen local tables, or checked only after points or graph objects. The
boundary fiber itself must be cartesian over the represented source lifts:

```text
CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
cart_res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd.
```

The cartesian boundary fiber must transport the boundary restriction map and
the fiber universal arrow along the C3/C5/C15/C45/F22 source paths while
preserving the fixed globular boundary, source and target boundaries, pasting
faces, coefficients, signed support, and source-before-points order.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOMPOBJPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOMPOBJPROJPMORFLIMSUBREPCPLFCOHSDXBCFQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 513 through the DD.4 SCC interface (207/207 exit 0).

## 1. Purpose

After doc 513, the cheap repair is:

```text
construct one represented fiber over
GlobBd_CartCone_NCoup_med_UP_Eq_id_eta_source_components
and reuse that fiber name for every source path.
```

That still does not construct the missing source object. The source must make
the represented boundary fiber pull back cartesianly over
CartLift_med_UP_Eq_id_source_fiber and
Cart_med_UP_Eq_id_BCF_self_dual_exact_source. If the fiber is rebuilt or
identified only locally after base change, it can select the right globular
modification at one boundary while failing C3*C5=C15, C5*C3=C15,
C3*C3*C5=C45, or F22 compatibility.

The live branch narrows from "represented boundary fiber" to:

```text
construct CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components;
construct cart_res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd;
prove the boundary restriction map is cartesian-natural;
prove eta_Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components
transports cartesianly;
prove the same cartesian boundary fiber appears on the C3*C5=C15,
C5*C3=C15, C3*C3*C5=C45, and F22 paths; and prove fixed-boundary,
source/target-boundary, pasting-face, coefficient, signed-support, and
source-before-points preservation.
```

## 2. Lemma

```text
Lemma 514.1 (the represented boundary fiber must be cartesian over source
lifts).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted cartesian boundary-fiber data are:

    med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD,
    Fib_med_UP_Eq_id_BCF_self_dual_exact_source,
    eta_NCoup_med_UP_Eq_id_BCF_self_dual_exact_source,
    SubRep_NCoup_med_UP_Eq_id_source_fiber,
    LimCut_NCoup_med_UP_Eq_id_source_fiber,
    CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    CartLift_med_UP_Eq_id_source_fiber,
    Cart_med_UP_Eq_id_BCF_self_dual_exact_source,
    Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    GlobBd_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd,
    Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    eta_Fib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    cart_res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd,
    the seven component legs, seven component objects, seven projections,
    dd4_c_original_res1_Qbar_BECD,
    Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. Cartesianity of the represented boundary fiber does not add
a new finite-index cell and does not start another coherence tower.

The cartesian boundary-fiber graph contains the live edges:

    represented boundary fiber -> cartesian boundary fiber,
    boundary restriction map -> cartesian boundary restriction,
    cartesian boundary restriction -> cartesian boundary fiber,
    cartesian source lifts -> cartesian boundary fiber,
    cartesian source coherence -> cartesian boundary fiber,
    cartesian boundary fiber -> cartesian fiber-arrow transport,
    cartesian fiber-arrow transport -> selected globular modification,
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
    cartesian boundary fiber -> source before points and graph objects.

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

    CartFibMed(T_C3(T_C5(z)))       = CartFibMed(T_C15(z)),
    CartFibMed(T_C5(T_C3(z)))       = CartFibMed(T_C15(z)),
    CartFibMed(T_C3(T_C3(T_C5(z)))) = CartFibMed(T_C45(z)),
    CartFibMed(T_C15(z*F22))        = CartFibMed(z*(C15*F22)),
    CartFibMed(T_C45(z*F22))        = CartFibMed(z*(C45*F22)).

Thus static one-boundary fibers, reused fiber names without pullback, chosen
base-change fibers, fibers rebuilt after base change, noncartesian pullbacks,
local transport tables, pointwise cartesian fibers, graph-side cartesian
fibers, post-product cartesian fibers, retuned or reindexed cartesian fibers,
expanded finite indexes, one-more-layer towers, and control/DH/Epstein
point-formability do not construct the cartesian boundary fiber.
```

## 3. Consequence

Doc 514 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 513: one represented boundary fiber is not enough unless that
fiber is cartesian over the represented source multiplier lifts.

The live object is now a component-cone-cartesian-coherence-globular-
modification-boundary-fiber-cartesian component-object-product-projected
parallel-morphism finite-limit subrepresented coupled formation-coherent
formation-gated self-dual-exact-BCF-generated DD.4 certificate-carrying
equalizer-identity universal mediator.

## 4. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components;
2. cart_res_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_GlobBd;
3. proof the boundary restriction is cartesian-natural;
4. proof the fiber universal arrow transports cartesianly;
5. proof the fixed globular boundary pulls back without changing boundary;
6. proof the same cartesian fiber appears on the C3/C5/C15/C45/F22 paths;
7. proof source/target boundaries and pasting faces pull back;
8. proof coefficients and signed support are preserved on every path;
9. proof no finite-index cell is added by cartesianity; and
10. proof the cartesian fiber is formed before points, graph objects,
    controls, DH, or Epstein.
```

Until the represented boundary fiber is cartesian in this sense, the object
remains missing.
