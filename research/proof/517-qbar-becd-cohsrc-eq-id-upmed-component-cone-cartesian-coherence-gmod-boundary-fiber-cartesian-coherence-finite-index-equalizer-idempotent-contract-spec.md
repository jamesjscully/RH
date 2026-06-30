# 517 - Qbar_BECD categorical closure coherent source-presentation equalizer-identity mediator component-cone cartesian-coherence globular-modification boundary-fiber cartesian-coherence finite-index equalizer-idempotent contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-eightieth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 516 left the equalizer-identity mediator branch live only if the
doc-515 cartesian boundary-fiber coherence is absorbed by the existing finite
index and closes idempotently to the same totalizer:

```text
FinIdx_NCoup_med_UP_Eq_id_source_components,
incl_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_FinIdx,
idem_close_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id.
```

This document fixes the next edge. A finite-index idempotent closure is still
insufficient if it lives only on the cell index, in a Karoubi completion, as
an external retract, as a facet projection, or as a graph-side idempotent.
The closure must be the actual source equalizer idempotent on
`Eq_NCoup_med_UP_Eq_id_source_components`, compatible with the alpha/beta
fork, the monic inclusion, the universal mediator, and the doc-515 coherence,
and it must compare to the identity on the same totalizer.

The new required data are:

```text
e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_on_Eq_source_components,
cmp_e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_id_Tot_NCoup_med_UP_Eq_id_source_components.
```

The idempotent must satisfy:

```text
alpha_NCoup_med_UP_Eq_id_source_constraints * e
  = beta_NCoup_med_UP_Eq_id_source_constraints * e,
incl_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components * e
  = incl_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components,
e * med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD
  = med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD,
e * Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components
  = Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
cmp_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components(e)
  = id_Tot_NCoup_med_UP_Eq_id_source_components.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 516 through the DD.4 SCC interface (210/210 exit 0).

## 1. Purpose

After doc 516, the cheap repair is:

```text
declare an idempotent on the finite cell index and say the absorbed doc-515
coherence is closed.
```

That still does not construct the missing object. The index is only an
accounting object unless the idempotent is an endomorphism of the internal
finite-limit/equalizer object. The equalizer idempotent must be seen before
points and graph objects, must preserve the doc-515 coherence payload, must
fix the equalizer-identity universal mediator, and must return the same
totalizer through the comparison.

The live branch narrows from "finite-index idempotent closure" to:

```text
construct e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_on_Eq_source_components;
prove e is an idempotent endomorphism of Eq_NCoup_med_UP_Eq_id_source_components;
prove e is compatible with alpha and beta;
prove e is invisible after the monic inclusion into Tot_NCoup_med_UP_Eq_id_source_components;
prove e fixes med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD;
prove e fixes Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components;
prove e compares to id_Tot_NCoup_med_UP_Eq_id_source_components; and
prove the finite index stays exact with no next coherence obligation.
```

## 2. Lemma

```text
Lemma 517.1 (finite-index closure must be a source equalizer idempotent).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted equalizer-idempotent closure data are:

    SrcCat_NCoup_med_UP_Eq_id_Qbar_BECD,
    Prod_NCoup_med_UP_Eq_id_source_components_facets_cells,
    alpha_NCoup_med_UP_Eq_id_source_constraints,
    beta_NCoup_med_UP_Eq_id_source_constraints,
    Eq_NCoup_med_UP_Eq_id_source_components,
    incl_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components,
    cmp_Eq_NCoup_med_UP_Eq_id_to_Tot_NCoup_med_UP_Eq_id_source_components,
    med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD,
    FinIdx_NCoup_med_UP_Eq_id_source_components,
    Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    the ten doc-515 boundary-fiber coherence cells,
    e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_on_Eq_source_components,
    cmp_e_Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_to_id_Tot_NCoup_med_UP_Eq_id_source_components.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. The doc-515 coherence remains the existing
boundary_fiber_coherence_cell and is not promoted to a new index cell.

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

Doc 517 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 516: finite-index closure is not enough unless the idempotent
is the actual source equalizer idempotent compatible with alpha/beta, the
monic inclusion, the universal mediator, and the doc-515 coherence. The live
object is now an equalizer-idempotent-closed finite-index
equalizer-identity mediator totalizer.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    finite index, source equalizer idempotent, doc-515 cells, strict rows,
    and multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD2
    Rejects index-level idempotents and set-level closure.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD3
    Rejects Karoubi completions and external retracts.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD4
    Rejects alpha/beta or monic-inclusion incompatibility.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD5
    Rejects idempotents that do not fix the mediator and doc-515 coherence.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD6
    Rejects expanded indexes and facet projections.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD7
    Rejects missing doc515 payload.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD8
    Rejects retuned graph-side idempotents.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD9
    Rejects control/DH/Epstein point-formable idempotents.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDQBARBECD10
    Accepts only the source equalizer idempotent.
```

## 5. Fail-Closed Note

The witness accepts only source-native equalizer idempotent closure. Any
candidate whose idempotent lives only on the finite index, requires a Karoubi
completion or external retract, fails to fix the mediator or doc-515
coherence, or is formable on controls/DH/Epstein fails before it can be
counted as construction evidence.
