# 349 - Qbar_BECD strict-square product multiplier boundary-certificate exact-source self-duality contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-twelfth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 348 left the strict-square branch live only if the represented
boundary-convolution functor generates an exact natural boundary-delta source:

```text
    Ex_Qbar_BECD_CanMod_BCF_dQ,
    Delta_Qbar_BECD_BCF_to_dQ_boundary,
    Ker_Qbar_BECD_BCF_delta_image_z,
    Coim_Qbar_BECD_CanMod_BCF_delta.
```

This document fixes the self-duality/properness edge. The exact BCF source
cannot merely carry a self-duality label downstream. It must itself generate
the rank-one boundary-defect duality map and its pinned twist:

```text
    Dual_Qbar_BECD_rank1_boundary_defect,
    Tw_Qbar_BECD_OC_BCF_pinned.
```

The duality map must run from the dual boundary defect line to the primal
boundary defect line, have boundary equal to the original DD.4 representative
`c`, make the normal ratio a self-dual boundary, pair the p1/p2 endpoint
lines, and be Rosati-compatible before the graph/count/control layers are
read off.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_boundary_certificate_exact_source_self_duality_contract`
(BDS1-BDS10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_boundary_certificate_exact_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_boundary_certificate_cancellation_module_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_monoidwide_dd4_boundary_certificate_contract`,
`prime_int_n1b_qbar_becd_boundary_defect_duality_contract`,
`prime_int_n1b_qbar_becd_boundary_self_duality_interface`,
`prime_int_n1b_qbar_becd_boundary_fiber_localization_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`,
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 348, the cheap repair is:

```text
construct an exact natural BCF delta,
then attach self-dual properness as a generic label,
or import a hyperbolic/Rosati/projection package after exactness.
```

That still does not construct the missing object. The DD.4 certificate is a
boundary/properness/self-duality certificate. If the exact BCF source is
one-sided, the self-duality has again been inserted from outside the square.
The exact source must produce the rank-one boundary-defect map whose boundary
is the original DD.4 representative, and it must pin the Laurent twist through
the carrier boundary data.

The live branch therefore narrows from "exact natural BCF source" to:

```text
construct a self-dual exact BCF source: the exact boundary-delta source plus
the rank-one dual-boundary-to-primal-boundary defect map, pinned twist,
original-DD.4 boundary, self-dual normal ratio, p1/p2 endpoint pairing,
Rosati-compatible duality, mixed multiplier duality, and control death.
```

## 2. Lemma

```text
Lemma 349.1 (the exact BCF source must generate self-dual properness).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted self-dual exact source data are:

    Rep_Qbar_BECD_source_fiber,
    eta_Qbar_BECD_source,
    CanMod_Qbar_BECD_z_boundary_convolution,
    BCF_Qbar_BECD_boundary_convolution_module,
    Ex_Qbar_BECD_CanMod_BCF_dQ,
    Delta_Qbar_BECD_BCF_to_dQ_boundary,
    Ker_Qbar_BECD_BCF_delta_image_z,
    Coim_Qbar_BECD_CanMod_BCF_delta,
    Dual_Qbar_BECD_rank1_boundary_defect,
    Tw_Qbar_BECD_OC_BCF_pinned,
    BKill_Qbar_BECD_dQ_boundary_properness_self_duality,
    Loc_Qbar_BECD_single_dQ,
    NR_Qbar_BECD_ordered_p1_p2.

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
the signed strict-square row, the coimage preserves signed coefficients and
support, and the duality payload has:

    defect rank one,
    dual line -> primal line,
    perfect p1/p2 endpoint pairing,
    bidual fixed,
    boundary class dd4_c_original_res1,
    res_1=1.

The mixed multiplier duality checks are equality of the full duality payload:

    Dual(T_C3(T_C5(z)))       = Dual(T_C15(z)),
    Dual(T_C5(T_C3(z)))       = Dual(T_C15(z)),
    Dual(T_C3(T_C3(T_C5(z)))) = Dual(T_C45(z)),
    Dual(T_C15(z*F22))        = Dual(z*(C15*F22)),
    Dual(T_C45(z*F22))        = Dual(z*(C45*F22)).

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
    represented source fiber,
    actual universal arrow,
    actual signed zero fiber,
    actual strict-square character convolution,
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
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_BOUNDARY_CERTIFICATE_EXACT_SOURCE_SELF_DUALITY__RANK_ONE_DUAL_DEFECT_FROM_BCF__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_boundary_certificate_exact_source_self_duality_contract`
verifies ten gates.

BDS1 records the H1 profile, Laurent-window rank/twist diagnostics, exact
self-dual rows, and full mixed multiplier duality payload equalities.

BDS2 records again that graph identities do not supply boundary self-duality.

BDS3 rejects one-sided exact deltas and generic self-duality labels.

BDS4 rejects hyperbolic endpoint planes and full-support dualities.

BDS5 rejects scalar pairings, diagonal coevaluations, and formal adjoints.

BDS6 rejects twist normalization and declared normal ratios.

BDS7 rejects weighted-zero/support dual kernels because they overaccept
non-square profiles.

BDS8 rejects late Rosati and count filters.

BDS9 proves every self-dual exact-source edge is mandatory.

BDS10 records the live predicate. Only self-dual exact BCF source data passes.

## 4. Impact on R1

```text
R1 after docs 138-349:
  NEWLY FIXED THIS CYCLE:
    - the exact BCF boundary-delta source must itself generate the rank-one
      boundary-defect duality/properness datum, with pinned twist and
      boundary equal to the original DD.4 representative.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
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
    - construct the self-dual exact BCF source, or kill the strict-square
      branch with a named obstruction at this self-dual exact-source
      interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BDS.1  Exhibit the exact BCF boundary-delta source.
ACCEPT-BDS.2  Exhibit the rank-one boundary-defect duality map generated by
              that exact delta.
ACCEPT-BDS.3  Prove the Laurent twist is pinned by carrier boundary data.
ACCEPT-BDS.4  Prove the boundary of the duality map is the original DD.4
              representative c.
ACCEPT-BDS.5  Prove the normal ratio is a self-dual boundary and sends c to
              zero.
ACCEPT-BDS.6  Prove p1/p2 dual endpoint pairing and Rosati compatibility.
ACCEPT-BDS.7  Prove C3/C5/C15/C45/F22 duality naturality.
ACCEPT-BDS.8  Prove endpoint/pushforward/graph/Rosati/count/control are
              generated from the same source.
ACCEPT-BDS.9  Prove controls, DH, and Epstein are not points.

KILL-BDS.1    Reject one-sided exact deltas.
KILL-BDS.2    Reject generic self-duality labels.
KILL-BDS.3    Reject hyperbolic endpoint planes and full-support dualities.
KILL-BDS.4    Reject scalar pairings, coevaluations, and formal Rosati
              adjoints.
KILL-BDS.5    Reject inserted dual/primal matching.
KILL-BDS.6    Reject degree-zero twist normalization and declared normal
              ratios.
KILL-BDS.7    Reject weighted-zero/support dual kernels.
KILL-BDS.8    Reject late Rosati filters.
KILL-BDS.9    Reject degree/count equality only.
KILL-BDS.10   Reject retuned dualities and control/DH/Epstein shadows.
```
