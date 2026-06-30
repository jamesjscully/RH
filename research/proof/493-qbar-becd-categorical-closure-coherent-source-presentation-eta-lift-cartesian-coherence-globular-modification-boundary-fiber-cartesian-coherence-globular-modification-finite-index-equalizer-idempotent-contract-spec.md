# 493 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian-coherence globular-modification boundary-fiber cartesian-coherence globular-modification finite-index equalizer-idempotent contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-fifty-sixth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 492 left the categorical closure branch live only if the doc-491
globular modification is absorbed by the existing finite coherent
source-presentation index and closes idempotently to the same totalizer:

```text
    FinIdx_CohSrcPres_BCCube_Qbar_BECD,
    incl_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_FinIdx_CohSrcPres_BCCube_Qbar_BECD,
    idem_close_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD.
```

This document fixes the next edge. A finite-index idempotent closure is still
insufficient if it lives only on the cell index, in a Karoubi completion, as
an external retract, as a facet projection, or as a graph-side idempotent. The
closure must be the actual source equalizer idempotent on
Eq_CohSrcPres_BCCube_Qbar_BECD, compatible with alpha/beta, the monic
inclusion, and the eta lift, and it must compare to the identity on the same
totalizer.

The new required data are:

```text
e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_on_Eq_CohSrcPres_BCCube_Qbar_BECD,
cmp_e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_id_Tot_CohSrcPres_BCCube_Qbar_BECD.
```

The idempotent must satisfy:

```text
alpha_CohSrcPres_BCCube_Qbar_BECD_constraints * e
  = beta_CohSrcPres_BCCube_Qbar_BECD_constraints * e,
incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD * e
  = incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
e * lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD
  = lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD(e)
  = id_Tot_CohSrcPres_BCCube_Qbar_BECD.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_finite_index_equalizer_idempotent_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 492 through the DD.4 SCC interface (186/186 exit 0).

## 1. Purpose

After doc 492, the cheap repair is:

```text
declare an idempotent on the finite cell index and say it closes the new
globular modification.
```

That still does not construct the missing object. The index is only an
accounting object unless the idempotent is an endomorphism of the internal
finite-limit/equalizer object sourced by eta. The equalizer idempotent must be
seen before points and graph objects, must preserve the doc-491 payload, and
must return the same totalizer through the comparison isomorphism.

The live branch narrows from "finite-index idempotent closure" to:

```text
construct e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_on_Eq_CohSrcPres_BCCube_Qbar_BECD;
prove e is an idempotent endomorphism of Eq_CohSrcPres_BCCube_Qbar_BECD;
prove e is compatible with alpha and beta;
prove e is invisible after the monic inclusion into Tot_CohSrcPres_BCCube_Qbar_BECD;
prove e fixes lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD;
prove e compares to id_Tot_CohSrcPres_BCCube_Qbar_BECD; and
prove the finite index stays exact with no next coherence obligation.
```

## 2. Lemma

```text
Lemma 493.1 (finite-index closure must be a source equalizer idempotent).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted equalizer-idempotent closure data are:

    SrcCat_BCCube_Qbar_BECD,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    incl_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    cmp_Eq_CohSrcPres_to_Tot_CohSrcPres_BCCube_Qbar_BECD,
    eta_BCCube_Qbar_BECD_source,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    cmp_lift_eta_BCCube_to_eta_CohSrcPres_BCCube_Qbar_BECD,
    FinIdx_CohSrcPres_BCCube_Qbar_BECD,
    e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_on_Eq_CohSrcPres_BCCube_Qbar_BECD,
    cmp_e_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_id_Tot_CohSrcPres_BCCube_Qbar_BECD.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. The doc-491 modification remains the existing
fiber_coherence_modification_cell and is not promoted to a new index cell.

The exact self-dual equalizer-idempotent rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full equalizer-idempotent payloads:

    EqIdem(T_C3(T_C5(z)))       = EqIdem(T_C15(z)),
    EqIdem(T_C5(T_C3(z)))       = EqIdem(T_C15(z)),
    EqIdem(T_C3(T_C3(T_C5(z)))) = EqIdem(T_C45(z)),
    EqIdem(T_C15(z*F22))        = EqIdem(z*(C15*F22)),
    EqIdem(T_C45(z*F22))        = EqIdem(z*(C45*F22)).

Thus index-level idempotents, set-level closures, Karoubi completions,
external retracts, facet projections, posthoc splits, graph-side idempotents,
retuned idempotents, expanded finite indexes, one-more-layer towers, and
control/DH/Epstein point-formability do not construct the source equalizer
idempotent.
```

## 3. Consequence

Doc 493 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 492: finite-index closure is not enough unless the idempotent
is the actual source equalizer idempotent compatible with alpha/beta, the
monic inclusion, and the eta lift. The live object is now an
equalizer-idempotent-closed finite coherent source-presentation totalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    finite index, source equalizer idempotent, doc-491 cells/faces, strict
    rows, and multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD2
    Rejects index-level idempotents and set-level closure.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD3
    Rejects Karoubi completions and external retracts.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD4
    Rejects alpha/beta or monic-inclusion incompatibility.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD5
    Rejects idempotents that do not fix the eta lift.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD6
    Rejects expanded indexes and facet projections.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD7
    Rejects missing doc491 payload.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD8
    Rejects retuned graph-side idempotents.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD9
    Rejects control/DH/Epstein point-formable idempotents.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDQBARBECD10
    Accepts only the source equalizer idempotent.
```

## 5. Fail-Closed Note

The witness accepts only source-native equalizer idempotent closure. Any
candidate whose idempotent lives only on the finite index, requires a Karoubi
completion or external retract, fails to fix eta, or is formable on
controls/DH/Epstein fails before it can be counted as construction evidence.
