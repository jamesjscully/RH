# 346 - Qbar_BECD strict-square product multiplier monoidwide DD.4 boundary-certificate contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-ninth cycle of the doc-137 construction arc. This is not a no-go
theorem, not an RH proof, and not added to the no-go bank.

Doc 345 left the strict-square branch live only through monoidwide
square-layer coherence for the carrier-native multiplier-action functor:

```text
    MWC_Qbar_BECD_multiplier_monoid_square_layers

across C3, C5, C15, C45, F22, and the DD.4/endpoint/pushforward/graph/
Rosati/count/control-death layer chain.
```

This document fixes the next edge. Coherence with the DD.4 boundary label is
not the same as the carrier boundary/properness/self-duality certificate that
kills the original DD.4 class. The monoidwide square-layer coherence must
transport one actual boundary certificate:

```text
    BKill_Qbar_BECD_dQ_boundary_properness_self_duality

for the original class

    c = (1+z)^-1,
    res_1(c)=1,
    [c] != 0 before the boundary certificate.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_monoidwide_dd4_boundary_certificate_contract`
(MDC1-MDC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_monoidwide_square_layer_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_square_layer_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_cartesian_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_dd4_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_transport_composition_contract`,
`prime_int_n1b_qbar_becd_boundary_fiber_localization_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`,
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 345, the cheap repair is:

```text
build monoidwide coherence for the multiplier action,
keep a DD.4 boundary id on every row,
and call that the DD.4 killing.
```

That still does not construct the missing object. The original DD.4 class is
not a label; it is the nonzero class detected by `res_1(c)=1` in
`H^1(<phi>;1+zF_2[[z]])=Z/2`. The strict square needs a carrier-native
boundary/properness/self-duality map that preserves that original class as
the thing being killed, then maps it to zero through one `dQ` localization
sequence. The same certificate must be transported by the monoidwide
multiplier action.

The live branch therefore narrows from "monoidwide square-layer coherence" to:

```text
construct monoidwide square-layer coherence that transports the actual
carrier DD.4 boundary-killing certificate.
```

## 2. Lemma

```text
Lemma 346.1 (monoidwide coherence must carry the DD.4 killing certificate).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted boundary certificate is:

    BKill_Qbar_BECD_dQ_boundary_properness_self_duality,

carried through one localization sequence and one normal ratio:

    Loc_Qbar_BECD_single_dQ,
    NR_Qbar_BECD_ordered_p1_p2.

The monoidwide multiplier checks remain:

    T_C3(T_C5(z))              = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))        = T_C45(z)             = {45:2, 90:-1},
    T_C15(z*F22)               = T_C3(T_C5(z))*F22
                                = z*(C15*F22)        = {30:4, 60:-2},
    T_C45(z*F22)               = T_C3(T_C3(T_C5(z)))*F22
                                = z*(C45*F22)        = {90:4, 180:-2}.

All endpoint, boundary, and p1/p2 pushforward defects remain zero. The finite
count and Rosati diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus monoidwide coherence labels, DD.4 boundary ids, formal nullhomotopies,
coinduced acyclic replacements, deletion, quotient, separate orbit
certificates, local prime certificates, declared connecting maps, declared
localizations, declared self-dual properness, late endpoint/pushforward/graph
filters, numeric equalities, local boundary tables, external 2-cells, retuned
boundary certificates, and control/DH/Epstein shadows do not construct this
certificate.

The accepted datum is exactly:

    carrier-native,
    represented source fiber,
    actual universal arrow,
    actual multiplier-action functor,
    actual monoidwide coherence,
    actual DD.4 boundary certificate,
    original DD.4 class preserved,
    original DD.4 class nonzero before the certificate,
    connecting map sends c to zero,
    one localization on dQ,
    restricts to p1 boundary fiber,
    restricts to p2 boundary fiber,
    common sequence for the ordered normal ratio,
    normal ratio is the boundary,
    self-dual properness,
    transported certificate comes from the same boundary,
    boundary certificate is natural monoidwide,
    same certificate on all multiplier paths,
    actual C3*C5=C15,
    actual C5*C3=C15,
    actual C3*C3*C5=C45,
    actual F22 product naturality,
    endpoint degree maps,
    p1 and p2 pushforward squares,
    graph composition,
    Rosati,
    count/degree,
    control death,
    finite anchors generated,
    controls, DH, and Epstein not point-formable,
    required DD.4 boundary-certificate edges present,
    no monoidwide-label-only argument,
    no boundary-id-only argument,
    no coinduced acyclic replacement,
    no formal nullhomotopy,
    no deletion or quotient,
    no separate orbit certificates,
    no local prime certificate,
    no declared connecting map/localization/self-dual properness,
    no late boundary/pushforward/graph filters,
    no degree/count/support/weighted-zero-only argument,
    no local boundary table,
    no external choice of 2-cells,
    no retuned boundary certificate,
    no graph-object coherence.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_MONOIDWIDE_DD4_BOUNDARY_CERTIFICATE__ORIGINAL_C_KILLED_BY_DQ__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_monoidwide_dd4_boundary_certificate_contract`
verifies ten gates.

MDC1 records the original nonzero DD.4 class and one carrier boundary
certificate transported through the monoidwide multiplier rows.

MDC2 records again that graph identities do not kill the DD.4 class.

MDC3 rejects monoidwide coherence labels without the boundary certificate.

MDC4 rejects formal nullhomotopies, deletion, quotient, and coinduced
acyclic replacement because they do not preserve the original class as the
thing being killed.

MDC5 rejects separate orbit or local prime certificates.

MDC6 rejects declared connecting maps, localizations, and self-dual
properness as labels.

MDC7 rejects endpoint, pushforward, and graph filters after the certificate.

MDC8 rejects numeric equality and local boundary tables.

MDC9 proves every boundary-certificate edge is mandatory.

MDC10 records the live predicate. Only carrier-native monoidwide DD.4
boundary certificate data passes.

## 4. Impact on R1

```text
R1 after docs 138-346:
  NEWLY FIXED THIS CYCLE:
    - monoidwide square-layer coherence must transport the actual DD.4
      boundary/properness/self-duality certificate that preserves the original
      nonzero class c and maps it to zero through one dQ localization.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the represented boundary-stratum product;
    - construct the product-to-internal-effectivity image map to the single
      internal Qbar_BECD effectivity domain;
    - construct the carrier-native multiplier-action functor on that domain;
    - construct the represented source fiber and universal arrow;
    - construct monoidwide square-layer coherence for the multiplier action;
    - construct the carrier DD.4 boundary-killing certificate:
        original c preserved,
        original c nonzero before killing,
        one localization on dQ,
        restrictions to p1 and p2 boundary fibers,
        one ordered normal ratio,
        connecting map sends c to zero,
        self-dual properness;
    - prove that certificate is transported monoidwide across independent
      multiplier paths and through endpoint/pushforward/graph/Rosati/count;
    - prove coherent control death excludes controls, DH, and Epstein.

  DISCIPLINE:
    - DD.4 labels, formal nullhomotopies, deletions, quotients, local
      certificates, declared exactness/properness, late filters, and numeric
      equalities do not count.

  STILL OPEN:
    - construct the carrier-native monoidwide DD.4 boundary certificate, or
      kill the strict-square branch with a named obstruction at this
      boundary-certificate interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-MDC.1  Preserve the original DD.4 class c as nonzero before killing.
ACCEPT-MDC.2  Exhibit one carrier dQ localization sequence.
ACCEPT-MDC.3  Prove it restricts to p1 and p2 boundary fibers.
ACCEPT-MDC.4  Prove the common ordered normal ratio.
ACCEPT-MDC.5  Prove the connecting map sends c to zero.
ACCEPT-MDC.6  Prove self-dual properness.
ACCEPT-MDC.7  Prove the same certificate is transported monoidwide through
              C3/C5/C15/C45/F22 paths and square layers.
ACCEPT-MDC.8  Prove controls, DH, and Epstein are not certificate-bearing
              points.

KILL-MDC.1    Reject monoidwide-label-only or boundary-id-only arguments.
KILL-MDC.2    Reject coinduced/bar acyclic replacement.
KILL-MDC.3    Reject formal nullhomotopy.
KILL-MDC.4    Reject deletion or quotient of the original class.
KILL-MDC.5    Reject separate orbit or local prime certificates.
KILL-MDC.6    Reject declared connecting maps, localizations, and properness.
KILL-MDC.7    Reject late endpoint/pushforward/graph filters.
KILL-MDC.8    Reject numeric equality and local boundary tables.
KILL-MDC.9    Reject external choices or retuned boundary certificates.
KILL-MDC.10   Reject control/DH/Epstein certificate-shadow point-formability.
```
