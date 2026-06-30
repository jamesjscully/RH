# 497 - Qbar_BECD categorical closure coherent source-presentation eta-lift cartesian-coherence globular-modification boundary-fiber cartesian-coherence globular-modification finite-index equalizer-identity universal-mediator DD.4-certificate contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-sixtieth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 496 left the categorical closure branch live only if the doc-495
universal mediator for `id_Eq_CohSrcPres_BCCube_Qbar_BECD` is natural for the
source multiplier action:

```text
Nat_med_UP_Eq_CohSrcPres_id_multiplier_action,
Whisker_med_UP_Eq_CohSrcPres_id_multiplier_action,
Comp_Nat_med_UP_Eq_CohSrcPres_id_C3_C5_C15_C45_F22.
```

This document fixes the next edge. Multiplier-natural mediator data are still
insufficient if they preserve only coefficients and signed support, carry only
a DD.4 label, hand off a certificate after the mediator is built, copy local
certificates along each path, or forget that the original DD.4 class is
nonzero with `res_1(c)=1` before the certificate kills it. The same
source-generated universal mediator must carry the existing carrier DD.4
boundary/properness/self-duality certificate.

The new required data are:

```text
Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary,
Nat_Cert_med_UP_Eq_CohSrcPres_id_DD4_multiplier_action,
Handoff_BKill_to_med_UP_Eq_id_DD4_certificate.
```

The required original certificate data remain:

```text
dd4_c_original_res1_Qbar_BECD,
BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality,
Loc_BCCube_Qbar_BECD_single_dQ,
NR_BCCube_Qbar_BECD_ordered_p1_p2.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_cohsrc_eq_id_upmed_dd4_certificate_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
from doc 496 through the DD.4 SCC interface (190/190 exit 0).

## 1. Purpose

After doc 496, the cheap repair is:

```text
make the identity mediator multiplier-natural for the visible rows, then let
the old DD.4 certificate sit nearby as a separate label.
```

That does not construct the missing object. The DD.4 certificate was already
forced earlier in the categorical-closure stack, but doc 496 introduced a new
equalizer-identity universal mediator. The certificate must be carried by
that mediator naturality itself. Otherwise the categorical closure has again
split into two independently verified pieces: a source equalizer identity on
one side and a boundary certificate on the other.

The live branch narrows from "multiplier-natural finite-limit universal
mediator" to:

```text
construct the DD.4 certificate carried by the universal mediator;
reuse the carrier boundary/properness/self-duality certificate already forced;
preserve the original nonzero DD.4 class before killing;
preserve res_1(c)=1 before the certificate;
transport the same certificate across C3/C5/C15/C45/F22 mediator naturality;
prove the same single dQ localization kills the class; and
reject coefficient-only naturality, DD.4 labels, local path certificates,
res1-forgetting, graph/pointwise certificates, and another coherence layer.
```

## 2. Lemma

```text
Lemma 497.1 (the equalizer-identity mediator carries the DD.4 certificate).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted mediator-carried DD.4 certificate data are:

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
    dd4_c_original_res1_Qbar_BECD,
    BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality,
    Cert_med_UP_Eq_CohSrcPres_id_DD4_boundary,
    Nat_Cert_med_UP_Eq_CohSrcPres_id_DD4_multiplier_action,
    Handoff_BKill_to_med_UP_Eq_id_DD4_certificate,
    Loc_BCCube_Qbar_BECD_single_dQ,
    NR_BCCube_Qbar_BECD_ordered_p1_p2.

The finite index remains exactly the seven source facets plus seventeen
coherence cells. The DD.4 certificate handoff for the mediator is not a new
finite-index cell and does not start another coherence tower.

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

Doc 497 does not solve R1 and does not prove RH. It removes the next cheap
reading of doc 496: multiplier-natural mediator data are not enough unless
that mediator carries the original DD.4 boundary certificate and preserves
the nonzero `res_1(c)=1` class before the same certificate kills it. The live
object is now a DD.4-certificate-carrying multiplier-natural finite-limit
universal-mediator-generated equalizer identity.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD1
    Confirms H^1(<phi>;U_1)=Z/2 with res_1(c)=1 for L=6,8,10,12, checks the
    DD.4 certificate handoff, five DD.4 naturality cells, four DD.4
    composition cells, finite index, doc-491 cells/faces, strict rows, and
    multiplier-path payload equality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD2
    Rejects coefficient-only or DD.4-label-only naturality.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD3
    Rejects posthoc certificate handoffs and boundary-after-mediator patches.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD4
    Rejects local path certificates and copied certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD5
    Rejects res1-forgetting and coboundary relabels.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD6
    Rejects external, graph-side, and pointwise certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD7
    Rejects expanded finite indexes and one-more-layer towers.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD8
    Rejects missing finite-limit spine and missing doc-491 payload.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD9
    Rejects control/DH/Epstein point-formable certificates.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPDD4QBARBECD10
    Accepts only the DD.4-certificate-carrying universal mediator.
```

## 5. Fail-Closed Note

The witness accepts only one source-native handoff from the already forced
DD.4 boundary/properness/self-duality certificate to the doc-496 universal
mediator naturality. Any candidate whose mediator only preserves visible
rows, carries a label, imports a late boundary certificate, forgets res_1,
copies local certificates, or works only on graph/control points fails before
it can be counted as construction evidence.
