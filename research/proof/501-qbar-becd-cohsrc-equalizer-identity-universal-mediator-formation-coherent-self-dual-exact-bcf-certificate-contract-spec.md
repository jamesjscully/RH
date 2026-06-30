# 501 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian-coherence globular-modification boundary-fiber cartesian-coherence globular-modification finite-index equalizer-identity universal-mediator formation-coherent self-dual exact-BCF-certificate contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-sixty-fourth cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 500 left the categorical closure branch live only if the multiplier-
natural universal mediator for `id_Eq_CohSrcPres_BCCube_Qbar_BECD` generates
the source-level formation token and fiber for the self-dual exact BCF source:

```text
Tok_med_UP_Eq_id_BCF_self_dual_exact_source,
Fib_med_UP_Eq_id_BCF_self_dual_exact_source.
```

This document fixes the next edge. The mediator-generated formation fiber is
still insufficient if it is assembled row-by-row with a common token, finite
row equalities, declared 2-cells, formal commutative squares, local C3
patches, prime-axis tags, graph-object coherence, or late filters. The same
universal mediator must generate source-level coherence cells for the
formation fiber.

The new required mediator-specific formation-coherence data are:

```text
Coh_med_UP_Eq_id_BCF_self_dual_exact_source_formation,
Cart_med_UP_Eq_id_BCF_self_dual_exact_source,
MWC_med_UP_Eq_id_BCF_self_dual_exact_source.
```

Those coherence cells must preserve the mediator-carried exact BCF delta,
kernel, coimage, signed coefficients/support, rank-one duality, pinned twist,
original DD.4 class, normal ratio, endpoint pairing, endpoint/pushforward/
graph chain, Rosati/count chain, and source-level control death across
`C3`, `C5`, `C15`, `C45`, and `F22`.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_formation_coherent_self_dual_exact_bcf_certificate_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 500 through the DD.4 SCC interface (194/194 exit 0).

## 1. Purpose

After doc 500, the cheap repair is:

```text
construct the mediator formation token/fiber,
verify that the C3/C5/C15/C45/F22 rows have the expected finite equalities,
then declare source coherence or import graph coherence later.
```

That does not construct the missing object. Earlier doc 465 forced
formation coherence after the categorical self-dual exact-source formation
gate. Doc 500 moved the formation gate through the equalizer-identity
universal mediator. This document requires the same mediator to generate
the source-level coherence cells, not just the formation token and fiber.

The live branch narrows from:

```text
formation-gated self-dual-exact-BCF-generated DD.4-certificate-carrying
multiplier-natural finite-limit universal-mediator-generated monic-cancelled
equalizer identity
```

to:

```text
formation-coherent formation-gated self-dual-exact-BCF-generated
DD.4-certificate-carrying multiplier-natural finite-limit
universal-mediator-generated monic-cancelled equalizer identity.
```

## 2. Lemma

```text
Lemma 501.1 (the equalizer-identity mediator generates source formation
coherence).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted mediator-carried formation-coherent self-dual exact BCF
certificate data are:

    SrcCat_BCCube_Qbar_BECD,
    Prod_CohSrcPres_BCCube_Qbar_BECD_facets_cells,
    alpha_CohSrcPres_BCCube_Qbar_BECD_constraints,
    beta_CohSrcPres_BCCube_Qbar_BECD_constraints,
    Eq_CohSrcPres_BCCube_Qbar_BECD,
    id_Eq_CohSrcPres_BCCube_Qbar_BECD,
    UP_Eq_CohSrcPres_BCCube_Qbar_BECD_finite_limit,
    med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD,
    Nat_med_UP_Eq_CohSrcPres_id_multiplier_action,
    Comp_Nat_med_UP_Eq_CohSrcPres_id_C3_C5_C15_C45_F22,
    Tok_med_UP_Eq_id_BCF_self_dual_exact_source,
    Fib_med_UP_Eq_id_BCF_self_dual_exact_source,
    Coh_med_UP_Eq_id_BCF_self_dual_exact_source_formation,
    Cart_med_UP_Eq_id_BCF_self_dual_exact_source,
    MWC_med_UP_Eq_id_BCF_self_dual_exact_source,
    dd4_c_original_res1_Qbar_BECD,
    BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality,
    Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary,
    Nat_Cert_med_UP_Eq_CohSrcPres_id_DD4_multiplier_action,
    Handoff_BKill_to_med_UP_Eq_id_DD4_certificate,
    ZFib_med_UP_Eq_id_signed_zero,
    CanMod_med_UP_Eq_id_z_boundary_convolution,
    BCF_med_UP_Eq_id_boundary_convolution_module,
    Ex_med_UP_Eq_id_CanMod_BCF_dQ,
    Delta_med_UP_Eq_id_BCF_to_dQ_boundary,
    Ker_med_UP_Eq_id_BCF_delta_image_z,
    Coim_med_UP_Eq_id_CanMod_BCF_delta,
    Dual_med_UP_Eq_id_rank1_boundary_defect,
    Tw_med_UP_Eq_id_OC_BCF_pinned,
    Loc_BCCube_Qbar_BECD_single_dQ,
    NR_BCCube_Qbar_BECD_ordered_p1_p2.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. The mediator formation coherence is not a new finite-index
cell and does not start another coherence tower.

The formation-coherent mediator rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed coherence checks are equality of full source-coherence payloads:

    CohMed(T_C3(T_C5(z)))       = CohMed(T_C15(z)),
    CohMed(T_C5(T_C3(z)))       = CohMed(T_C15(z)),
    CohMed(T_C3(T_C3(T_C5(z)))) = CohMed(T_C45(z)),
    CohMed(T_C15(z*F22))        = CohMed(z*(C15*F22)),
    CohMed(T_C45(z*F22))        = CohMed(z*(C45*F22)).

Each coherence payload contains the same universal mediator, formation token,
formation fiber, source coherence, cartesian source coherence, monoidwide
source coherence, exact delta, kernel, coimage, rank-one duality, pinned
twist, original DD.4 class, normal ratio, endpoint pair, finite index,
doc-491 cells/faces, and source-level control-death id.

Thus same-token assertions, finite row equalities, degree/count/support/
weighted-zero arguments, declared 2-cells, formal commutative squares, finite
composition tables, local C3 patches, single-prime axes, prime-axis tags,
external choices of 2-cells, retuned source coherences, graph-object
coherence, graph predicates, late control filters, boundary/DD.4 after-
filters, functors of points without representers, semantic zeta labels,
expanded finite indexes, one-more-layer towers, and control/DH/Epstein
point-formability do not construct the missing object.
```

## 3. Consequence

Doc 501 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 500: a mediator-generated formation token/fiber is not enough
unless the universal mediator also generates cartesian and monoidwide
source-level coherence preserving the full exact BCF/DD.4/duality/control
payload. The live object is now a formation-coherent formation-gated
self-dual-exact-BCF-generated DD.4-certificate-carrying multiplier-natural
finite-limit universal-mediator-generated equalizer identity.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    mediator-generated formation coherence, cartesian/monoidwide source
    coherence, five source-coherence naturality cells, four source-coherence
    composition cells, finite index, doc-491 payload, strict rows, and mixed
    coherence payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD2
    Rejects same-token assertions and finite row equalities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD3
    Rejects local C3 patches, single-prime-axis patches, and prime-axis tags.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD4
    Rejects declared 2-cells, formal commutative squares, and finite
    composition tables.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD5
    Rejects degree/count/support-only and weighted-zero-only coherence.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD6
    Rejects external choices of 2-cells, retuned source coherence, and
    semantic zeta labels.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD7
    Rejects graph-object coherence, graph predicates, late control filters,
    DD.4 after-filters, and functors of points without representers.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD8
    Rejects missing preservation of rank-one duality, pinned twist, DD.4,
    normal ratio, endpoint pairing, endpoint/pushforward/graph, and Rosati/
    count data.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD9
    Rejects control/DH/Epstein coherent graph shadows.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFCOHSDXBCFQBARBECD10
    Accepts only the formation-coherent formation-gated self-dual-exact-BCF-
    generated DD.4-certificate-carrying universal mediator.
```

## 5. Fail-Closed Note

The witness accepts only one source-native mediator handoff: the
equalizer-identity universal mediator generates the formation coherence,
cartesian source coherence, and monoidwide source coherence preserving the
full exact BCF/DD.4/duality/control-death chain before graph objects exist.
A candidate whose mediator relies on finite row equality, declared 2-cells,
local patches, external choices, graph coherence, late filters, or semantic
labels fails before it can be counted as construction evidence.
