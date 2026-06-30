# 463 - Qbar_BECD categorical closure DD.4 certificate exact-source self-duality totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-twenty-sixth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 462 left the strict-square branch live only if BCF generation of the DD.4
certificate is an exact natural boundary-delta source inside the represented
categorical source square:

```text
Ex_BCCube_Qbar_BECD_CanMod_BCF_dQ,
Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary,
Ker_BCCube_Qbar_BECD_BCF_delta_image_z,
Coim_BCCube_Qbar_BECD_CanMod_BCF_delta.
```

This document fixes the self-duality/properness edge in that categorical
source. The exact BCF source cannot merely carry a self-duality label
downstream. It must itself generate the rank-one boundary-defect duality map
and its pinned twist:

```text
Dual_BCCube_Qbar_BECD_rank1_boundary_defect,
Tw_BCCube_Qbar_BECD_OC_BCF_pinned.
```

The duality map must run from the dual boundary defect line to the primal
boundary defect line, have boundary equal to the original DD.4 representative
`c`, make the normal ratio a self-dual boundary, pair the p1/p2 endpoint
lines, and be Rosati-compatible before the graph/count/control layers are
read off.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_dd4_certificate_exact_source_self_duality_totalization_contract`
(CATBDSQBARBECD1-CATBDSQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 462 through the DD.4 SCC
interface (156/156 exit 0).

## 1. Purpose

After doc 462, the cheap repair is:

```text
construct the exact natural BCF delta,
then attach self-dual properness as a generic label,
or import a hyperbolic/Rosati/projection package after exactness.
```

That still does not construct the missing object. The DD.4 certificate is a
boundary/properness/self-duality certificate. If the exact BCF source is
one-sided, the self-duality has again been inserted from outside the square.
The exact source must produce the rank-one boundary-defect map whose boundary
is the original DD.4 representative, and it must pin the Laurent twist through
the carrier boundary data.

The live branch therefore narrows from:

```text
exact-natural-BCF-generated-DD.4-certificate-carrying
cancellation-module-generated-DD.4-certificate-carrying
monoidwide-DD.4-certificate-carrying monoidwide-square-layer-coherent
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization
```

to:

```text
self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
exact-natural-BCF-generated-DD.4-certificate-carrying
cancellation-module-generated-DD.4-certificate-carrying
monoidwide-DD.4-certificate-carrying monoidwide-square-layer-coherent
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization.
```

## 2. Lemma

```text
Lemma 463.1 (the exact categorical BCF source must generate self-dual
properness).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted self-dual exact source data are:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle,
    BCCube_CatSq_Qbar_BECD_facets,
    Tot_BCCube_CatSq_Qbar_BECD,
    D_Qbar_BECD_eff,
    Act_BCCube_Qbar_BECD_multiplier_functor,
    Rep_BCCube_Qbar_BECD_source_fiber,
    eta_BCCube_Qbar_BECD_source,
    ZFib_BCCube_Qbar_BECD_signed_zero,
    CanMod_BCCube_Qbar_BECD_z_boundary_convolution,
    BCF_BCCube_Qbar_BECD_boundary_convolution_module,
    Ex_BCCube_Qbar_BECD_CanMod_BCF_dQ,
    Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary,
    Ker_BCCube_Qbar_BECD_BCF_delta_image_z,
    Coim_BCCube_Qbar_BECD_CanMod_BCF_delta,
    Dual_BCCube_Qbar_BECD_rank1_boundary_defect,
    Tw_BCCube_Qbar_BECD_OC_BCF_pinned,
    BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality,
    dd4_c_original_res1_Qbar_BECD,
    Loc_BCCube_Qbar_BECD_single_dQ,
    NR_BCCube_Qbar_BECD_ordered_p1_p2.

The Laurent-window diagnostics remain:

    support ranks      4,6,10,18,
    hyperbolic ranks   8,12,20,36,
    defect ranks       1,1,1,1,
    unit twists        3,5,9,17,
    nonzero maps       7,31,511,131071.

Thus the live map cannot be a full hyperbolic endpoint plane, scalar
pairing, diagonal coevaluation, inserted dual/primal matching, or degree-zero
twist normalization. It must be the rank-one boundary-defect map produced by
the exact BCF source.

The exact self-dual finite rows are:

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
the signed categorical row, the coimage preserves signed coefficients and
support, and the duality payload has:

    defect rank one,
    dual line -> primal line,
    perfect p1/p2 endpoint pairing,
    bidual fixed,
    boundary class dd4_c_original_res1_Qbar_BECD,
    res_1=1.

The mixed multiplier duality checks are equality of the full duality payload:

    Dual(T_C3(T_C5(z)))       = Dual(T_C15(z)),
    Dual(T_C5(T_C3(z)))       = Dual(T_C15(z)),
    Dual(T_C3(T_C3(T_C5(z)))) = Dual(T_C45(z)),
    Dual(T_C15(z*F22))        = Dual(z*(C15*F22)),
    Dual(T_C45(z*F22))        = Dual(z*(C45*F22)).

Every row uses the same represented categorical source square, same totalized
cube, same signed zero fiber, same cancellation module, same
boundary-convolution functor, same exact sequence, same boundary delta, same
kernel, same coimage, same rank-one boundary-defect duality, same pinned
twist, same DD.4 boundary certificate, and same original DD.4 class.
Endpoint and pushforward defects remain zero.

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus one-sided exact deltas, generic self-duality labels, hyperbolic endpoint
planes, full-support dualities, inserted dual/primal matching, scalar
pairings, diagonal coevaluations, formal Rosati adjoints, degree-zero twist
normalizations, declared normal ratios, weighted-zero/support dual kernels,
late Rosati filters, degree/count equalities, retuned dualities, and
control/DH/Epstein shadows do not construct this exact source.

The accepted datum is exactly:

    carrier-native,
    represented categorical source square,
    totalized source cube,
    represented source fiber,
    actual universal arrow,
    actual signed zero fiber,
    represented multiplier-action functor,
    actual cancellation module,
    actual boundary-convolution module functor,
    actual exact boundary delta,
    exact sequence generated by BCF,
    kernel equals cancellation-module image,
    coimage preserves signed coefficients,
    rank-one boundary-defect duality actual,
    duality generated by the exact delta,
    Laurent twist pinned,
    boundary of duality is the original DD.4 class,
    original DD.4 class nonzero before certificate,
    normal ratio is a self-dual boundary,
    connecting map sends c to zero,
    p1/p2 dual endpoint pairing,
    Rosati-compatible duality,
    DD.4 boundary certificate generated,
    one localization on dQ,
    C3/C5/C15/C45/F22 duality naturality,
    monoidwide certificate transport,
    endpoint/pushforward/graph generated,
    control death generated,
    finite anchors generated,
    controls, DH, and Epstein not point-formable,
    required self-dual exact-source edges present,
    no one-sided exact delta,
    no generic self-duality label,
    no hyperbolic endpoint plane,
    no degree-zero twist normalization,
    no scalar pairing or diagonal coevaluation,
    no full-support duality,
    no inserted dual/primal matching,
    no formal Rosati adjoint,
    no declared normal ratio,
    no weighted-zero/support dual kernel,
    no late Rosati filter,
    no degree/count equality only,
    no retuned duality.
```

Verdict label:

```text
N1B_QBAR_BECD_CATEGORICAL_CLOSURE_DD4_CERTIFICATE_EXACT_SOURCE_SELF_DUALITY__RANK_ONE_DUAL_DEFECT_FROM_BCF__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_dd4_certificate_exact_source_self_duality_totalization_contract`
verifies ten gates.

CATBDSQBARBECD1 records the H1 profile, Laurent-window rank/twist
diagnostics, exact self-dual rows, and full mixed multiplier duality payload
equalities.

CATBDSQBARBECD2 records again that graph identities do not supply boundary
self-duality.

CATBDSQBARBECD3 rejects one-sided exact deltas and generic self-duality
labels.

CATBDSQBARBECD4 rejects hyperbolic endpoint planes and full-support
dualities.

CATBDSQBARBECD5 rejects scalar pairings, diagonal coevaluations, and formal
adjoints.

CATBDSQBARBECD6 rejects twist normalization and declared normal ratios.

CATBDSQBARBECD7 rejects weighted-zero/support dual kernels because they
overaccept non-square profiles.

CATBDSQBARBECD8 rejects late Rosati and count filters.

CATBDSQBARBECD9 proves every self-dual exact-source edge is mandatory,
including exact-delta -> rank-one-boundary-defect-duality, duality -> pinned
Laurent twist, duality -> original DD.4 boundary, and normal-ratio ->
connecting-map-sends-c-to-zero.

CATBDSQBARBECD10 records the live predicate. Only self-dual exact
BCF-source-generated DD.4 boundary certificate data passes; control, DH, and
Epstein point shadows do not.

## 4. Impact on R1

```text
R1 after docs 138-463:
  NEWLY FIXED THIS CYCLE:
    - the exact BCF boundary-delta source in the categorical closure square
      must itself generate the rank-one boundary-defect duality/properness
      datum, with pinned twist and boundary equal to the original DD.4
      representative.

  CURRENT LIVE TARGET ON THE CATEGORICAL-CLOSURE BRANCH:
    - construct the represented categorical source square and totalized
      Beck-Chevalley cube;
    - construct the represented multiplier-action functor and internal
      effectivity domain;
    - construct the signed zero fiber and universal arrow;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the exact BCF boundary-delta source;
    - construct inside that source the rank-one dual-boundary-to-primal-
      boundary defect map:
        duality generated by exact delta,
        Laurent twist pinned by carrier boundary data,
        boundary equal to original c,
        normal ratio self-dual,
        p1/p2 endpoint pairing,
        Rosati-compatible duality;
    - prove C3/C5/C15/C45/F22 duality naturality;
    - prove endpoint/pushforward/graph/Rosati/count/control are generated
      from that same self-dual exact source;
    - prove controls, DH, and Epstein are not points.

  DISCIPLINE:
    - self-duality is not a label after exactness. Hyperbolic planes,
      scalar pairings, formal adjoints, twist fiats, weighted-zero kernels,
      and late Rosati filters do not count.

  STILL OPEN:
    - construct the categorical self-dual exact BCF source, or kill the
      categorical closure branch with a named obstruction at this
      self-dual exact-source interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-CATBDS.1  Exhibit the exact BCF boundary-delta source inside the
                 represented categorical source square.
ACCEPT-CATBDS.2  Exhibit the rank-one boundary-defect duality map generated
                 by that exact delta.
ACCEPT-CATBDS.3  Prove the Laurent twist is pinned by carrier boundary data.
ACCEPT-CATBDS.4  Prove the boundary of the duality map is the original DD.4
                 representative c.
ACCEPT-CATBDS.5  Prove the normal ratio is a self-dual boundary and sends c
                 to zero.
ACCEPT-CATBDS.6  Prove p1/p2 dual endpoint pairing and Rosati compatibility.
ACCEPT-CATBDS.7  Prove C3/C5/C15/C45/F22 duality naturality.
ACCEPT-CATBDS.8  Prove endpoint/pushforward/graph/Rosati/count/control are
                 generated from the same source.
ACCEPT-CATBDS.9  Prove controls, DH, and Epstein are not points.

KILL-CATBDS.1    Reject one-sided exact deltas.
KILL-CATBDS.2    Reject generic self-duality labels.
KILL-CATBDS.3    Reject hyperbolic endpoint planes and full-support dualities.
KILL-CATBDS.4    Reject scalar pairings, coevaluations, and formal Rosati
                 adjoints.
KILL-CATBDS.5    Reject inserted dual/primal matching.
KILL-CATBDS.6    Reject degree-zero twist normalization and declared normal
                 ratios.
KILL-CATBDS.7    Reject weighted-zero/support dual kernels.
KILL-CATBDS.8    Reject late Rosati filters.
KILL-CATBDS.9    Reject degree/count equality only.
KILL-CATBDS.10   Reject retuned dualities and control/DH/Epstein shadows.
```
