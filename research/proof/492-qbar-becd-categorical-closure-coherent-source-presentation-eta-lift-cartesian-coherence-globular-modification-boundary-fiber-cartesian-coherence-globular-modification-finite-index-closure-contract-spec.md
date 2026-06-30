# 492 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian-coherence globular-modification boundary-fiber cartesian-coherence globular-modification finite-index closure contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-fifty-fifth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 491 left the categorical closure branch live only if the represented
cartesian boundary-fiber coherence cells are faces of one source-level
globular modification with shared source and target boundary:

```text
    Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    GlobBd_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components.
```

This document fixes the anti-recursion edge. A candidate does not get to
continue by constructing the boundary fiber, cartesian transport, coherence
cells, or another globular modification for the doc-491 modification. The
doc-491 modification must be absorbed by the already finite coherent
source-presentation index, and the closure operator applied to it must return
the same source totalizer.

The new required data are:

```text
FinIdx_CohSrcPres_BCCube_Qbar_BECD,
incl_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_FinIdx_CohSrcPres_BCCube_Qbar_BECD,
idem_close_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD.
```

The finite index must remain the same twenty-four cells from the coherent
source-presentation totalizer: seven source facets and seventeen coherence
cells. The doc-491 globular modification is the existing
fiber_coherence_modification_cell inside that index, not a twenty-fifth cell.
Idempotent closure must send it back to Tot_CohSrcPres_BCCube_Qbar_BECD with
no open next-boundary-fiber, next-cartesian-transport, next-globular-
modification, or next-coherence obligation.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_coherent_source_presentation_eta_lift_cartesian_coherence_globular_modification_boundary_fiber_cartesian_coherence_globular_modification_finite_index_closure_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 491 through the DD.4 SCC interface (185/185 exit 0).

## 1. Purpose

After doc 491, the cheap repair is:

```text
construct the represented boundary fiber of the new fiber-coherence globular
modification, then repeat the cartesian/coherence/globular pattern.
```

That is exactly the layer-creation failure mode doc 444 and doc 481 were meant
to stop. The live candidate must instead prove that the doc-491 modification
is already one cell of the finite source-presentation totalizer.

The live branch narrows from "cartesian boundary-fiber coherence cells
globularize" to:

```text
construct FinIdx_CohSrcPres_BCCube_Qbar_BECD;
construct the inclusion of the doc-491 modification into that index;
prove the index has exactly seven facets plus seventeen coherence cells;
prove the doc-491 modification is the existing fiber_coherence_modification_cell;
prove the index does not expand;
prove idempotent closure returns Tot_CohSrcPres_BCCube_Qbar_BECD; and
prove no next boundary-fiber/cartesian/coherence/globular obligation remains.
```

## 2. Lemma

```text
Lemma 492.1 (doc-491 closure must be finite-index idempotent).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted finite-index closure data are:

    Cat_CohSrcPres_BCCube_Qbar_BECD,
    Tot_CohSrcPres_BCCube_Qbar_BECD,
    FinIdx_CohSrcPres_BCCube_Qbar_BECD,
    lift_eta_BCCube_to_Eq_CohSrcPres_BCCube_Qbar_BECD,
    Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    GlobBd_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD_components,
    incl_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_to_FinIdx_CohSrcPres_BCCube_Qbar_BECD,
    idem_close_Mod_Coh_CartFib_Mod_Coh_CartCone_lift_eta_CohSrcPres_BCCube_Qbar_BECD.

The finite source-presentation index has exactly:

    seven facets =
        endpoint_integrality, degree_maps, dd4_boundary, boundary_pushforward,
        graph_composition, rosati_count, control_death;

    seventeen coherence cells =
        source_square_cell, beck_chevalley_cube_cell, cartesian_lift_cell,
        component_cone_cell, component_projection_pair_cell,
        globular_modification_cell, boundary_fiber_cell,
        cartesian_boundary_fiber_cell, boundary_fiber_coherence_cell,
        fiber_coherence_modification_cell, source_boundary_cell,
        target_boundary_cell, multiplier_path_cell,
        coefficient_preservation_cell, signed_support_preservation_cell,
        source_before_points_cell, closed_finite_coherence_cell.

The doc-491 globular modification must map to
fiber_coherence_modification_cell. The closed_finite_coherence_cell then
forces idempotent closure back to the same totalizer.

The exact self-dual finite-index closure rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed checks are equality of full finite-index closure payloads:

    FinIdx(T_C3(T_C5(z)))       = FinIdx(T_C15(z)),
    FinIdx(T_C5(T_C3(z)))       = FinIdx(T_C15(z)),
    FinIdx(T_C3(T_C3(T_C5(z)))) = FinIdx(T_C45(z)),
    FinIdx(T_C15(z*F22))        = FinIdx(z*(C15*F22)),
    FinIdx(T_C45(z*F22))        = FinIdx(z*(C45*F22)).

Thus post-doc491 boundary fibers, cartesian transports, coherence cells,
globular modifications, expanded finite indexes, declared totalizers, chosen
sections, pro/local/graph-side closures, retuned indexes, and
control/DH/Epstein point-formability do not construct the finite-index
closure.
```

## 3. Consequence

Doc 492 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 491: one cannot continue the ladder by adding the next
boundary-fiber/coherence layer. The live object is now an idempotently closed
finite-index coherent source-presentation totalizer whose existing
fiber_coherence_modification_cell contains the doc-491 globular modification.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    twenty-four-cell finite index, the ten doc-491 cells/faces, strict rows,
    and multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD2
    Rejects graph closure as finite-index absorption.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD3
    Rejects one-more-layer continuation after doc491.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD4
    Rejects expanded finite indexes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD5
    Rejects declared totalizers and chosen sections.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD6
    Rejects missing doc491 cells, faces, or boundary.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD7
    Rejects pro, local, and graph-side closures.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD8
    Rejects retuned non-idempotent closure.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD9
    Rejects control/DH/Epstein point-formable finite-index closures.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINQBARBECD10
    Accepts only exact idempotent finite-index closure.
```

## 5. Fail-Closed Note

The witness accepts only source-native finite-index closure. Any candidate
that creates a new post-doc491 boundary fiber, expands the finite index, uses
a declared totalizer, or forms controls/DH/Epstein as points fails before it
can be counted as construction evidence.
