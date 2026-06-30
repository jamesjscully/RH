# 518 - Qbar_BECD categorical closure coherent source-presentation equalizer-identity mediator component-cone cartesian-coherence globular-modification boundary-fiber cartesian-coherence finite-index equalizer-idempotent monic-cancellation contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-eighty-first cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 517 left the equalizer-identity mediator branch live only if the doc-516
finite-index closure is the actual source equalizer idempotent:

```text
e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_on_Eq_source_components,
cmp_e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_id_Tot_NCoup_med_UP_Eq_id_source_components.
```

This document fixes the next edge. A source equalizer idempotent is still
insufficient if it only becomes the identity after comparison with the
totalizer, only acts as identity on the finite index, hides in a kernel of a
nonmonic inclusion, acts as an automorphism mask, or is checked only
projectionwise. The equalizer inclusion is monic, so the compatibility

```text
incl_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components * e
  = incl_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components
```

must cancel inside the source category to:

```text
e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_on_Eq_source_components
  = id_Eq_NCoup_med_UP_Eq_id_source_components.
```

The new required data are:

```text
id_Eq_NCoup_med_UP_Eq_id_source_components,
cancel_incl_Eq_e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_id_Eq_NCoup_med_UP_Eq_id_source_components.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 517 through the DD.4 SCC interface (211/211 exit 0).

## 1. Purpose

After doc 517, the cheap repair is:

```text
keep a nontrivial idempotent on the equalizer and only require it to look like
identity after comparison with the totalizer.
```

That does not construct the missing object. Since the equalizer inclusion is
monic, equality after inclusion must cancel in the source category. The
finite-index closure therefore contributes no new endomorphism: it is the
identity of the equalizer object itself.

The live branch narrows from "source equalizer idempotent" to:

```text
construct id_Eq_NCoup_med_UP_Eq_id_source_components;
construct the monic-cancellation proof from incl_Eq * e = incl_Eq to e = id_Eq;
prove this cancellation is source-native and before points;
prove e fixes the universal mediator because it is id_Eq;
prove e fixes the doc-515 coherence because it is id_Eq;
prove alpha/beta compatibility because it is id_Eq;
prove the finite index stays exact and unexpanded; and
prove no comparison-only or hidden-kernel identity remains.
```

## 2. Lemma

```text
Lemma 518.1 (the equalizer idempotent cancels to identity).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted monic-cancellation data are:

    SrcCat_NCoup_med_UP_Eq_id_Qbar_BECD,
    Prod_NCoup_med_UP_Eq_id_source_components_facets_cells,
    alpha_NCoup_med_UP_Eq_id_source_constraints,
    beta_NCoup_med_UP_Eq_id_source_constraints,
    Eq_NCoup_med_UP_Eq_id_source_components,
    id_Eq_NCoup_med_UP_Eq_id_source_components,
    incl_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components,
    cmp_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components,
    med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD,
    Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    FinIdx_NCoup_med_UP_Eq_id_source_components,
    e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_on_Eq_source_components,
    cancel_incl_Eq_e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_id_Eq_NCoup_med_UP_Eq_id_source_components.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. The doc-515 coherence remains the existing
boundary_fiber_coherence_cell. No monic-cancellation cell is added to the
finite index.

The exact self-dual monic-cancellation rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full monic-cancellation payloads:

    MonCancel(T_C3(T_C5(z)))       = MonCancel(T_C15(z)),
    MonCancel(T_C5(T_C3(z)))       = MonCancel(T_C15(z)),
    MonCancel(T_C3(T_C3(T_C5(z)))) = MonCancel(T_C45(z)),
    MonCancel(T_C15(z*F22))        = MonCancel(z*(C15*F22)),
    MonCancel(T_C45(z*F22))        = MonCancel(z*(C45*F22)).

Thus comparison-only identities, hidden-kernel idempotents, nonmonic
cancellations, index/projection identities, automorphism masks, quotient
shadows, graph-side identities, retuned identities, expanded finite indexes,
one-more-layer towers, and control/DH/Epstein point-formability do not
construct the monic-cancelled identity.
```

## 3. Consequence

Doc 518 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 517: the equalizer idempotent cannot remain as extra
endomorphism data. It must cancel to
`id_Eq_NCoup_med_UP_Eq_id_source_components`. The live object is now an
identity-cancelled finite-index equalizer-identity mediator totalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    finite index, equalizer identity, monic cancellation, doc-515 cells,
    strict rows, and multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD2
    Rejects comparison-only identities and hidden-kernel idempotents.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD3
    Rejects nonmonic cancellation.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD4
    Rejects index and projection identities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD5
    Rejects automorphism masks and quotient shadows.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD6
    Rejects expanded finite indexes and one-more-layer towers.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD7
    Rejects missing doc515 payload.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD8
    Rejects graph-side or retuned identities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD9
    Rejects control/DH/Epstein point-formable identities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONQBARBECD10
    Accepts only the monic-cancelled identity.
```

## 5. Fail-Closed Note

The witness accepts only source-native monic cancellation to the equalizer
identity. Any candidate whose identity appears only after comparison, only on
the finite index, only after quotienting, or only on graph/control points
fails before it can be counted as construction evidence.
