# 521 - Qbar_BECD categorical closure coherent source-presentation equalizer-identity mediator component-cone cartesian-coherence globular-modification boundary-fiber cartesian-coherence finite-index equalizer-idempotent monic-cancellation universal-mediator multiplier-naturality DD.4-certificate contract

Status: construction-spec refinement anchor, 2026-06-24.
Three-hundred-eighty-fourth cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 520 left the equalizer-identity mediator branch live only if the doc-519
universal mediator for `id_Eq_NCoup_med_UP_Eq_id_source_components` is
natural for the source multiplier action:

```text
Nat_med_UP_Eq_NCoup_med_UP_Eq_id_id_multiplier_action,
Whisker_med_UP_Eq_NCoup_med_UP_Eq_id_id_multiplier_action,
Comp_Nat_med_UP_Eq_NCoup_med_UP_Eq_id_id_C3_C5_C15_C45_F22.
```

This document fixes the next edge. Multiplier-natural mediator data are still
insufficient if they preserve only coefficients and signed support, carry
only a DD.4 label, hand off a certificate after the mediator is built, copy
local certificates along each path, or forget that the original DD.4 class is
nonzero with `res_1(c)=1` before the certificate kills it. The same
source-generated universal mediator must carry the existing carrier DD.4
boundary/properness/self-duality certificate.

The new required data are:

```text
Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_boundary,
Nat_Cert_med_UP_Eq_NCoup_med_UP_Eq_id_id_DD4_multiplier_action,
Handoff_BKill_to_med_UP_Eq_NCoup_med_UP_Eq_id_DD4_certificate.
```

The required original certificate data remain:

```text
dd4_c_original_res1_Qbar_BECD,
BKill_NCoup_med_UP_Eq_id_Qbar_BECD_dQ_boundary_properness_self_duality,
Loc_NCoup_med_UP_Eq_id_Qbar_BECD_single_dQ,
NR_NCoup_med_UP_Eq_id_Qbar_BECD_ordered_p1_p2.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_component_cone_cartesian_coherence_gmod_bf_cart_coh_finidx_eqidem_monic_upmed_nat_dd4_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 520 through the DD.4 SCC interface (214/214 exit 0).

## 1. Purpose

After doc 520, the cheap repair is:

```text
make the identity mediator multiplier-natural for the visible rows, then let
the old DD.4 certificate sit nearby as a separate label.
```

That does not construct the missing object. The DD.4 certificate was already
forced earlier in the categorical-closure stack, but doc 520 introduced a
new, more local equalizer-identity universal mediator. The certificate must
be carried by that mediator naturality itself. Otherwise the categorical
closure has split again into two independently verified pieces: a source
equalizer identity on one side and a boundary certificate on the other.

The live branch narrows from "multiplier-natural finite-limit universal
mediator" to:

```text
construct the DD.4 certificate carried by the universal mediator;
reuse the carrier boundary/properness/self-duality certificate already forced;
preserve the original nonzero DD.4 class before killing;
preserve res_1(c)=1 before the certificate;
transport the same certificate across C3/C5/C15/C45/F22 mediator naturality;
prove the same single dQ localization kills the class;
preserve the doc-515 finite-index payload; and
reject coefficient-only naturality, DD.4 labels, local path certificates,
res1-forgetting, graph/pointwise certificates, and another coherence layer.
```

## 2. Lemma

```text
Lemma 521.1 (the doc-520 equalizer-identity mediator carries the DD.4 certificate).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted mediator-carried DD.4 certificate data are:

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
    Loc_NCoup_med_UP_Eq_id_Qbar_BECD_single_dQ,
    NR_NCoup_med_UP_Eq_id_Qbar_BECD_ordered_p1_p2.

The finite index remains exactly the seven source facets plus seventeen
coherence cells, including boundary_fiber_coherence_cell. The DD.4
certificate handoff for the mediator is not a new finite-index cell and does
not start another coherence tower.

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

The mixed checks are equality of full mediator-carried DD.4 certificate
payloads:

    UPMedDD4(T_C3(T_C5(z)))       = UPMedDD4(T_C15(z)),
    UPMedDD4(T_C5(T_C3(z)))       = UPMedDD4(T_C15(z)),
    UPMedDD4(T_C3(T_C3(T_C5(z)))) = UPMedDD4(T_C45(z)),
    UPMedDD4(T_C15(z*F22))        = UPMedDD4(z*(C15*F22)),
    UPMedDD4(T_C45(z*F22))        = UPMedDD4(z*(C45*F22)).

Thus coefficient-only naturality, DD.4 labels, posthoc certificate handoffs,
local path certificates, res1-forgetting, coboundary relabels, copied
certificates, boundary-after-mediator patches, external certificates,
graph-side or pointwise certificates, expanded finite indexes,
one-more-layer towers, and control/DH/Epstein point-formability do not
construct the missing object.
```

## 3. Consequence

Doc 521 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 520: multiplier-natural mediator data are not enough unless
that mediator carries the original DD.4 boundary certificate and preserves
the nonzero `res_1(c)=1` class before the same certificate kills it. The live
object is now a DD.4-certificate-carrying multiplier-natural
finite-limit-universal-mediator-generated equalizer identity over the
finite-index equalizer-identity mediator presentation.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    DD.4 certificate handoff, five DD.4 naturality cells, four DD.4
    composition cells, finite index, doc-515 cells, strict rows, and
    multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD2
    Rejects coefficient-only or DD.4-label-only naturality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD3
    Rejects posthoc certificate handoffs and boundary-after-mediator patches.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD4
    Rejects local path certificates and copied certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD5
    Rejects res1-forgetting and coboundary relabels.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD6
    Rejects external, graph-side, and pointwise certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD7
    Rejects expanded finite indexes and one-more-layer towers.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD8
    Rejects missing finite-limit spine and missing doc-515 payload.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD9
    Rejects control/DH/Epstein point-formable certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCOMPCONECARTCOHGMGBFCARTCOHFINEQIDMONUPNATDD4QBARBECD10
    Accepts only the DD.4-certificate-carrying universal mediator.
```

## 5. Fail-Closed Note

The witness accepts only one source-native handoff from the already forced
DD.4 boundary/properness/self-duality certificate to the doc-520 universal
mediator naturality. Any candidate whose mediator only preserves visible
rows, carries a label, imports a late boundary certificate, forgets res_1,
copies local certificates, or works only on graph/control points fails before
it can be counted as construction evidence.
