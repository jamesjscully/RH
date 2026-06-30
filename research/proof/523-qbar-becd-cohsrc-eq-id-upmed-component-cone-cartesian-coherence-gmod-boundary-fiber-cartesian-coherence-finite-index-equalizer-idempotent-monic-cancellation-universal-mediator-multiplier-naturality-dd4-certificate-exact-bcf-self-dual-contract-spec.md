# 523 - Qbar_BECD coherent source equalizer-identity universal mediator multiplier-naturality DD.4-certificate exact-BCF self-dual-certificate contract

Status: construction-spec refinement anchor, 2026-06-24.
Three-hundred-eighty-sixth cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 522 left the categorical closure branch live only if the multiplier-
natural universal mediator for `id_Eq_NCoup_med_UP_Eq_id_source_components`
carries the exact BCF generation of the DD.4 certificate:

```text
ZFib_med_UP_Eq_NCoup_med_UP_Eq_id_id_signed_zero,
CanMod_med_UP_Eq_NCoup_med_UP_Eq_id_id_z_boundary_convolution,
BCF_med_UP_Eq_NCoup_med_UP_Eq_id_id_boundary_convolution_module,
Ex_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_dQ,
Delta_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_to_dQ_boundary,
Ker_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_delta_image_z,
Coim_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_delta.
```

This document fixes the next edge. Mediator-carried exact BCF generation is
still insufficient if the exact source is one-sided and self-dual properness
is attached later as a generic label, a hyperbolic endpoint plane, a scalar
pairing, a formal Rosati adjoint, or a declared normal ratio. The same
mediator-carried exact source must generate the rank-one boundary-defect
duality map and its pinned Laurent twist.

The new required mediator-specific self-dual exact BCF data are:

```text
Dual_med_UP_Eq_NCoup_med_UP_Eq_id_id_rank1_boundary_defect,
Tw_med_UP_Eq_NCoup_med_UP_Eq_id_id_OC_BCF_pinned.
```

The mediator still carries the exact BCF, self-dual, and original
certificate data:

```text
dd4_c_original_res1_Qbar_BECD,
BKill_NCoup_med_UP_Eq_id_Qbar_BECD_dQ_boundary_properness_self_duality,
Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_boundary,
Nat_Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_multiplier_action,
Handoff_BKill_to_med_UP_Eq_NCoup_med_UP_Eq_id_DD4_certificate,
ZFib_med_UP_Eq_NCoup_med_UP_Eq_id_id_signed_zero,
CanMod_med_UP_Eq_NCoup_med_UP_Eq_id_id_z_boundary_convolution,
BCF_med_UP_Eq_NCoup_med_UP_Eq_id_id_boundary_convolution_module,
Ex_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_dQ,
Delta_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_to_dQ_boundary,
Ker_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_delta_image_z,
Coim_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_delta,
Dual_med_UP_Eq_NCoup_med_UP_Eq_id_id_rank1_boundary_defect,
Tw_med_UP_Eq_NCoup_med_UP_Eq_id_id_OC_BCF_pinned,
Loc_NCoup_med_UP_Eq_id_Qbar_BECD_single_dQ,
NR_NCoup_med_UP_Eq_id_Qbar_BECD_ordered_p1_p2.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_exbcf_selfdual_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 522 through the DD.4 SCC interface (216/216 exit 0).

## 1. Purpose

After doc 522, the cheap repair is:

```text
carry the exact BCF delta, kernel, and coimage through the universal
mediator, then attach self-dual properness as a downstream label.
```

That does not construct the missing object. The DD.4 certificate is a
boundary/properness/self-duality certificate. Earlier doc 463 already forced
the exact BCF source to generate rank-one boundary-defect duality and a
pinned Laurent twist. Doc 522 moved the exact BCF obligation through the
equalizer-identity universal mediator; this document requires the same
mediator handoff to carry that self-dual generation, not just the exact
one-sided delta.

The live branch narrows from:

```text
exact-BCF-generated DD.4-certificate-carrying multiplier-natural finite-limit
universal-mediator-generated monic-cancelled equalizer identity
```

to:

```text
self-dual-exact-BCF-generated DD.4-certificate-carrying multiplier-natural
finite-limit universal-mediator-generated monic-cancelled equalizer identity.
```

## 2. Lemma

```text
Lemma 523.1 (the equalizer-identity mediator carries self-dual exact BCF
generation).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted mediator-carried self-dual exact BCF certificate data are:

    SrcCat_NCoup_med_UP_Eq_id_Qbar_BECD,
    Prod_NCoup_med_UP_Eq_id_source_components_facets_cells,
    alpha_NCoup_med_UP_Eq_id_source_constraints,
    beta_NCoup_med_UP_Eq_id_source_constraints,
    Eq_NCoup_med_UP_Eq_id_source_components,
    id_Eq_NCoup_med_UP_Eq_id_source_components,
    UP_Eq_NCoup_med_UP_Eq_id_source_components_finite_limit,
    med_UP_Eq_NCoup_med_UP_Eq_id_id_to_id_Eq_NCoup_med_UP_Eq_id_source_components,
    Nat_med_UP_Eq_NCoup_med_UP_Eq_id_id_multiplier_action,
    Comp_Nat_med_UP_Eq_NCoup_med_UP_Eq_id_id_C3_C5_C15_C45_F22,
    dd4_c_original_res1_Qbar_BECD,
    BKill_NCoup_med_UP_Eq_id_Qbar_BECD_dQ_boundary_properness_self_duality,
    Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_boundary,
    Nat_Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_multiplier_action,
    Handoff_BKill_to_med_UP_Eq_NCoup_med_UP_Eq_id_DD4_certificate,
    ZFib_med_UP_Eq_NCoup_med_UP_Eq_id_id_signed_zero,
    CanMod_med_UP_Eq_NCoup_med_UP_Eq_id_id_z_boundary_convolution,
    BCF_med_UP_Eq_NCoup_med_UP_Eq_id_id_boundary_convolution_module,
    Ex_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_dQ,
    Delta_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_to_dQ_boundary,
    Ker_med_UP_Eq_NCoup_med_UP_Eq_id_id_BCF_delta_image_z,
    Coim_med_UP_Eq_NCoup_med_UP_Eq_id_id_CanMod_BCF_delta,
    Dual_med_UP_Eq_NCoup_med_UP_Eq_id_id_rank1_boundary_defect,
    Tw_med_UP_Eq_NCoup_med_UP_Eq_id_id_OC_BCF_pinned,
    Loc_NCoup_med_UP_Eq_id_Qbar_BECD_single_dQ,
    NR_NCoup_med_UP_Eq_id_Qbar_BECD_ordered_p1_p2.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. The mediator self-dual exact BCF handoff is not a new
finite-index cell and does not start another coherence tower.

The source mediator and doc515 boundary-fiber coherence payload remain fixed:

    med_UP_Eq_CohSrcPres_id_to_id_Eq_CohSrcPres_BCCube_Qbar_BECD,
    Coh_CartFib_Mod_Coh_CartCone_NCoup_med_UP_Eq_id_eta_source_components,
    boundary_fiber_coherence_cell,
    the ten doc515 cartesian boundary-fiber coherence cells.

The Laurent-window diagnostics remain:

    support ranks      4,6,10,18,
    hyperbolic ranks   8,12,20,36,
    defect ranks       1,1,1,1,
    unit twists        3,5,9,17,
    nonzero maps       7,31,511,131071.

Thus the live map cannot be a full hyperbolic endpoint plane, scalar pairing,
diagonal coevaluation, inserted dual/primal matching, or degree-zero twist
normalization. It must be the rank-one boundary-defect map produced by the
same mediator-carried exact BCF delta.

The exact self-dual mediator-certificate rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

For each row, the exact delta is still exact-natural, the kernel relation is
the signed row, the coimage preserves signed coefficients and support, and
the mediator-carried duality payload has:

    defect rank one,
    dual line -> primal line,
    perfect p1/p2 endpoint pairing,
    bidual fixed,
    boundary class dd4_c_original_res1_Qbar_BECD,
    res_1=1,
    normal ratio self-dual boundary,
    Rosati-compatible duality.

The mixed multiplier checks are equality of full self-dual exact BCF
payloads:

    SDEBCFMed(T_C3(T_C5(z)))       = SDEBCFMed(T_C15(z)),
    SDEBCFMed(T_C5(T_C3(z)))       = SDEBCFMed(T_C15(z)),
    SDEBCFMed(T_C3(T_C3(T_C5(z)))) = SDEBCFMed(T_C45(z)),
    SDEBCFMed(T_C15(z*F22))        = SDEBCFMed(z*(C15*F22)),
    SDEBCFMed(T_C45(z*F22))        = SDEBCFMed(z*(C45*F22)).

Thus one-sided exact deltas, generic self-duality labels, hyperbolic endpoint
planes, full-support dualities, inserted dual/primal matching, scalar
pairings, diagonal coevaluations, formal Rosati adjoints, degree-zero twist
normalizations, declared normal ratios, weighted-zero/support dual kernels,
late Rosati filters, degree/count equalities, retuned dualities, graph-side
dualities, expanded finite indexes, one-more-layer towers, and
control/DH/Epstein point-formability do not construct the missing object.
```

## 3. Consequence

Doc 523 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 522: exact BCF generation at the mediator is not enough
unless the same exact source generates self-dual properness through the
rank-one boundary-defect duality and pinned Laurent twist. The live object
is now a self-dual-exact-BCF-generated DD.4-certificate-carrying multiplier-
natural finite-limit universal-mediator-generated equalizer identity.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    Laurent-window rank/twist diagnostics, mediator self-dual exact BCF
    handoff, five duality naturality cells, four duality composition cells,
    finite index, doc-515 cells, strict rows, and multiplier-path
    duality payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD2
    Rejects one-sided exact deltas and generic self-duality labels.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD3
    Rejects hyperbolic endpoint planes, full-support dualities, and inserted
    dual/primal matching.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD4
    Rejects scalar pairings, diagonal coevaluations, and formal Rosati
    adjoints.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD5
    Rejects degree-zero twist normalizations and declared normal ratios.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD6
    Rejects weighted-zero and support dual kernels.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD7
    Rejects late Rosati filters, degree/count equality only, retuned
    dualities, and graph-side dualities.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD8
    Rejects expanded finite indexes and one-more-layer towers.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD9
    Rejects control/DH/Epstein duality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPSDXBCFQBARBECD10
    Accepts only the self-dual-exact-BCF-generated DD.4-certificate-carrying
    universal mediator.
```

## 5. Fail-Closed Note

The witness accepts only one source-native mediator handoff: the exact BCF
delta carried by the equalizer-identity universal mediator also generates the
rank-one boundary-defect duality and pinned Laurent twist, with boundary the
original nonzero DD.4 class and with the ordered normal ratio a self-dual
boundary. A candidate whose mediator imports self-duality later, replaces the
rank-one defect by a hyperbolic or scalar package, normalizes the twist away,
or works only on graph/control points fails before it can be counted as
construction evidence.
