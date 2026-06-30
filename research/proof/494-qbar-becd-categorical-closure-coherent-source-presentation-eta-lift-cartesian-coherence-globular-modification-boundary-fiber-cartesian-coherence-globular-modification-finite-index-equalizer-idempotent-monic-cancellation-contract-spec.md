# 494 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian-coherence globular-modification boundary-fiber cartesian-coherence globular-modification finite-index equalizer-idempotent monic-cancellation contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-fifty-seventh cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 493 left the categorical closure branch live only if the doc-492
finite-index closure is the actual source equalizer idempotent:

```text
e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_on_Eq_CohSrcPres_BCCube_Qbar_BECD,
cmp_e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_id_Tot_CohSrcPres_BCCube_Qbar_BECD.
```

This document fixes the next edge. A source equalizer idempotent is still
insufficient if it only becomes the identity after comparison with the
totalizer, only acts as identity on the finite index, hides in a kernel of a
nonmonic inclusion, acts as an automorphism mask, or is checked only
projectionwise. The equalizer inclusion is monic, so the compatibility

```text
incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD * e
  = incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD
```

must cancel inside the source category to:

```text
e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_on_Eq_CohSrcPres_BCCube_Qbar_BECD
  = id_Eq_CohSrcPres_BCCube_Qbar_BECD.
```

The new required data are:

```text
id_Eq_CohSrcPres_BCCube_Qbar_BECD,
cancel_incl_Eq_e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_finite_index_equalizer_idempotent_monic_cancellation_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 493 through the DD.4 SCC interface (187/187 exit 0).

## 1. Purpose

After doc 493, the cheap repair is:

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
construct id_Eq_CohSrcPres_BCCube_Qbar_BECD;
construct the monic-cancellation proof from incl_Eq * e = incl_Eq to e = id_Eq;
prove this cancellation is source-native and before points;
prove e fixes eta because it is id_Eq;
prove alpha/beta compatibility because it is id_Eq;
prove the finite index stays exact and unexpanded; and
prove no comparison-only or hidden-kernel identity remains.
```

## 2. Lemma

```text
Lemma 494.1 (the equalizer idempotent cancels to identity).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted monic-cancellation data are:

    SrcCat_BCCube_Qbar_BECD,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    id_Eq_CohSrcPres_BCCube_Qbar_BECD,
    incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    FinIdx_CohSrcPres_BCCube_Qbar_BECD,
    e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_on_Eq_CohSrcPres_BCCube_Qbar_BECD,
    cancel_incl_Eq_e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. The doc-491 payload remains the existing
fiber_coherence_modification_cell. No monic-cancellation cell is added to the
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

Doc 494 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 493: the equalizer idempotent cannot remain as extra
endomorphism data. It must cancel to id_Eq_CohSrcPres_BCCube_Qbar_BECD. The
live object is now an identity-cancelled finite coherent source-presentation
equalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    finite index, equalizer identity, monic cancellation, doc-491 cells/faces,
    strict rows, and multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD2
    Rejects comparison-only identities and hidden-kernel idempotents.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD3
    Rejects nonmonic cancellation.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD4
    Rejects index and projection identities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD5
    Rejects automorphism masks and quotient shadows.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD6
    Rejects expanded finite indexes and one-more-layer towers.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD7
    Rejects missing doc491 payload.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD8
    Rejects graph-side or retuned identities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD9
    Rejects control/DH/Epstein point-formable identities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDMONQBARBECD10
    Accepts only the monic-cancelled identity.
```

## 5. Fail-Closed Note

The witness accepts only source-native monic cancellation to the equalizer
identity. Any candidate whose identity appears only after comparison, only on
the finite index, only after quotienting, or only on graph/control points
fails before it can be counted as construction evidence.
