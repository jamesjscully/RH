# 396 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter constraint-component-cone cartesian-coherence gmbf-coherence globular-modification boundary-fiber cartesian-coherence gmbf cartesian-coherence globular-modification boundary-fiber cartesian coherence globular-modification boundary-fiber cartesian coherence globular-modification boundary-fiber cartesian contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-fifty-ninth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 395 left the strict-square branch live only if the doc-394 source-level
globular modification is selected by a represented boundary fiber:

```text
    Fib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    eta_Fib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components.
```

This document fixes the next edge. A represented boundary fiber over one
globular boundary is still not enough if the fiber is static, rebuilt after
base change, transported by chosen local tables, or checked only after points
or graph objects. The boundary fiber must itself be cartesian over the same
source multiplier lifts:

```text
    CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components,
    cart_res_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_to_GlobBd_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_NCoup.
```

The cartesian boundary fiber must transport the boundary-restriction map and
the fiber universal arrow along the C3/C5/C15/C45/F22 source paths while
preserving the fixed globular boundary, source/target boundaries,
boundary-restriction/fiber-arrow naturality, component/projection boundaries,
pair_alpha/pair_beta boundary, pasting faces, coefficients, and signed support
before points and graph objects.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cart_coh_gmbf_coh_gmod_bf_cart_coh_gmbf_ccgm_bf_cart_coh_gmod_bf_cart_coh_gmod_bf_cart_coh_gmod_bf_cart_contract`
(SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC1-SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 395 through the DD.4 SCC
interface, all exit 0.

## 1. Purpose

After doc 395, the cheap repair is:

```text
construct one represented fiber over
GlobBd_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components
and then reuse that fiber name for every multiplier path.
```

That still does not construct the missing object. The square needs the fiber
to pull back cartesianly over the represented source lifts. If the fiber is
rebuilt after base change or transported by local choices, the modification
can select the right boundary at one point while failing C3*C5=C15,
C5*C3=C15, C3*C3*C5=C45, or F22 compatibility.

The live branch narrows from "represented boundary fiber" to:

```text
construct CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components;
prove cart_res_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_to_GlobBd_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_NCoup
is cartesian-natural; prove
eta_Fib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components
transports cartesianly; prove the same boundary fiber appears on the
C3*C5=C15, C5*C3=C15, C3*C3*C5=C45, and F22 paths; and prove the fixed
boundary, source/target boundaries, pasting faces, coefficients, signed
support, and source-before-points order are preserved.
```

## 2. Lemma

```text
Lemma 396.1 (the represented boundary fiber for the cartesian boundary-fiber
coherence globular modification must be cartesian).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

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

Thus static one-boundary fibers, chosen base-change fibers, fibers rebuilt
after base change, noncartesian pullbacks, local transport tables, pointwise
cartesian fibers, graph-side cartesian fibers, post-product cartesian fibers,
retuned cartesian fibers, reindexed cartesian fibers, and
control/DH/Epstein point-formability do not construct the cartesian boundary
fiber.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_constraint_component_cone_cart_coh_gmbf_coh_gmod_bf_cart_coh_gmbf_ccgm_bf_cart_coh_gmod_bf_cart_coh_gmod_bf_cart_coh_gmod_bf_cart_contract`
verifies ten gates.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC1 records the cartesian boundary fiber,
H1 profile, strict rows, mixed path equalities, and connected cartesian
boundary-fiber graph.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC2 records again that graph identities do
not supply cartesian fiber transport.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC3 rejects static one-boundary fibers.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC4 rejects noncartesian pullbacks that
fail to preserve boundary data.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC5 rejects chosen local fiber transport
and fibers rebuilt after base change.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC6 rejects pointwise, graph-side, and
post-product cartesian fibers.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC7 rejects retuned or reindexed
cartesian fibers.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC8 makes every cartesian boundary-fiber
edge mandatory.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC9 records that graph-side cartesian
fibers still leave controls, DH, and Epstein formable.

SCFGBCCGBCCGBCCGBCCGBCCGBCCGBFCCGBFC10 accepts only cartesian represented
boundary fibers.

Therefore a candidate that satisfies doc 395 with a represented boundary
fiber is still incomplete unless that fiber is cartesian over the represented
source multiplier lifts.

## 4. Consequence

The live strict-square branch is now:

```text
construct CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components
and prove the boundary-restriction map, fiber universal arrow, fixed globular
boundary, source/target boundary data, pasting faces, coefficients, and signed
support all transport cartesianly over C3/C5/C15/C45/F22 before points and
graph objects exist.
```

The open construction target is no longer "make the represented cartesian
boundary-fiber coherence globular modification a represented boundary fiber."
It is "make that boundary fiber cartesian over the source multiplier lifts."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_NCoup_eta_source_components;
2. cart_res_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartFib_Mod_Coh_CartCone_to_GlobBd_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_Coh_CartFib_NCoup;
3. proof that this cartesian fiber transports the represented boundary fiber;
4. proof that the fiber universal arrow is cartesian;
5. proof that the fixed globular boundary pulls back cartesianly;
6. proof that source and target boundaries transport cartesianly;
7. proof that boundary-restriction, component/projection, pair_alpha/beta,
   and pasting-face data transport cartesianly;
8. proof that C3*C5=C15, C5*C3=C15, C3*C3*C5=C45, and F22 use the same
   cartesian boundary fiber;
9. proof of coefficient and signed-support preservation;
10. proof that the fiber is formed before points and graph objects.
```

Until this cartesian boundary fiber exists, the object remains missing.
