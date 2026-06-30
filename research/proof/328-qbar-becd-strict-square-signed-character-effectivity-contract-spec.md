# 328 - Qbar_BECD strict-square signed-character effectivity contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-ninety-first cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 327 left the strict-square branch live only through:

```text
a full character-to-internal-strata functor retaining multi-axis classes,
coefficients, signed zero-fiber data, and convolution.
```

This document fixes the next bottleneck. The functor must include a
carrier-native effectivity orientation on the signed strict-square character
algebra. Positivity cannot be obtained by taking positive parts, absolute
values, sign/support quotients, signed-zero deletion, diagonal-total
positivity, external factorization, endpoint/count filters, or
control-formable positive profiles.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_signed_character_effectivity_contract`
(SCE1-SCE10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_character_stratum_functor_contract`,
`prime_int_n1b_qbar_becd_strict_square_effectivity_extraction_contract`,
`prime_int_n1b_qbar_becd_effectivity_first_generator_orientation_contract`,
`prime_int_n1b_qbar_becd_internal_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_represented_carrier_gate_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 327, the cheap repair is:

```text
take the signed character algebra,
erase the negative/cancellation part,
declare the remaining positive profile to be the effectivity stratum.
```

That loses exactly the square data the branch was kept for. The zero fiber

```text
chi(zero) = 2[1] - [2]
```

is not noise. It is square-only cancellation data, and the target functor
must send it into boundary/cancellation structure before an internal
effectivity stratum is produced. The square must construct positivity; it may
not import a positivity convention from outside the carrier.

The live branch therefore narrows from "build a character-to-strata functor"
to:

```text
build a carrier-native effectivity orientation / positive cone on the signed
strict-square character algebra, compatible with addition and convolution,
and feeding Qbar_BECD internal strata, boundary localization, endpoint
integrality, graph/Rosati/count data, and formation-level control death.
```

## 2. Lemma

```text
Lemma 328.1 (signed effectivity cannot be sign erasure).

The strict-square signed character algebra contains:

    chi(L)      = [1] + [2],
    chi(C3)     = [3],
    chi(F22)    = 2[2],
    chi(F41)    = [4],
    chi(zero)   = 2[1] - [2],
    chi(L*F22)  = 2[2] + 2[4].

It also has cancellation and signed convolution:

    (2[1] - [2]) + [2] = 2[1],
    (2[1] - [2]) * 2[2] = 4[2] - 2[4].

Positive-part truncation is not additive:

    pos((2[1] - [2]) + [2]) != pos(2[1] - [2]) + pos([2]).

Absolute value turns cancellation into an ordinary positive profile:

    abs(2[1] - [2]) = 2[1] + [2].

Support/sign quotients identify:

    support(2[2]) = support([2]),
    support(2[1] - [2]) = support([1] + [2]).

Deleting the signed zero fiber deletes square-only object data because

    mu(zero) = 0, but chi(zero) = 2[1] - [2].

Diagonal-total positivity also collapses the strict-square split:

    mu(L) = mu(C3) = 3,
    Phi'_2(L) = 1,
    Phi'_2(C3) = 0.

Factoring [4] as the 2^2 axis imports external prime factorization. Endpoint,
count, DH, Epstein, and control filters can mimic the positive profiles

    2[1], 2[1]+[2], support([1]+[2]), 2[2].

Thus the accepted datum is exactly:

    actual strict-square character data,
    actual signed character algebra,
    actual character convolution,
    actual carrier-native effectivity orientation,
    actual positive cone,
    multi-axis classes retained,
    coefficients retained,
    negative coefficients retained as boundary/cancellation data,
    signed zero-fiber data retained,
    additive orientation,
    convolution-compatible orientation,
    positive cone mapped to internal effectivity strata,
    cancellation mapped to boundary localization,
    internal effectivity domain produced,
    prime-power subtowers produced,
    endpoint integrality generated,
    boundary localization generated,
    graph/Rosati/count data generated,
    control death generated,
    controls undefined at the orientation,
    DH undefined at the orientation,
    Epstein undefined at the orientation,
    no positive-part truncation,
    no absolute-value map,
    no sign/support quotient,
    no negative-coefficient deletion,
    no signed-zero deletion,
    no diagonal-total positive selector,
    no external ordering or factorization,
    no endpoint/count filter,
    no declared positive cone,
    not formable on controls, DH, or Epstein.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_SIGNED_CHARACTER_EFFECTIVITY__POSITIVE_CONE_MUST_RETAIN_CANCELLATION__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_signed_character_effectivity_contract`
verifies ten gates.

SCE1 records the signed strict-square character algebra, including
cancellation and signed convolution.

SCE2 rejects positive-part truncation because it erases the negative
coefficient and is not additive on the cancellation datum.

SCE3 rejects absolute value because it turns the signed zero fiber into a
positive control-formable profile.

SCE4 rejects sign/support quotients because they lose coefficients and
identify the zero-fiber support with ordinary multi-axis support.

SCE5 rejects signed-zero deletion.

SCE6 rejects diagonal-total positivity because it collapses the `L` / `C3`
strict-square split and treats the zero fiber as harmless.

SCE7 rejects external ordering/factorization of character keys.

SCE8 rejects endpoint/count/control filters because they can mimic the
positive profiles after sign erasure.

SCE9 makes boundary cancellation and control death mandatory outputs of the
signed effectivity orientation.

SCE10 records the live predicate. Only a carrier-native signed-character
effectivity orientation passes.

## 4. Impact on R1

```text
R1 after docs 138-328:
  NEWLY FIXED THIS CYCLE:
    - strict-square character extraction now requires a carrier-native
      positive cone / effectivity orientation on the signed character algebra.
      Positivity cannot be obtained by truncating, absolutizing, quotienting,
      deleting signed zero fibers, using diagonal totals, factoring support
      keys externally, or filtering by endpoint/count/control success.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct its carrier-native effectivity orientation / positive cone;
    - prove the orientation retains multi-axis classes, coefficients,
      negative coefficients as boundary/cancellation data, signed zero fibers,
      and convolution;
    - prove it maps cancellation to DD.4 boundary localization and maps the
      positive cone to Qbar_BECD internal effectivity strata;
    - prove prime-power subtowers, endpoint integrality, graph/Rosati/count
      data, and formation-level control death are generated there;
    - prove DH, Epstein, and controls are undefined at orientation formation.

  DISCIPLINE:
    - sign-erasing maps are diagnostics only. They may expose the obstruction,
      but they do not construct the missing object.

  STILL OPEN:
    - construct the carrier-native signed-character effectivity orientation,
      or kill the strict-square branch with a named mechanism at this point.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-SCE.1  Exhibit the signed strict-square character algebra and its
              character convolution.
ACCEPT-SCE.2  Exhibit a carrier-native effectivity orientation / positive cone.
ACCEPT-SCE.3  Retain multi-axis classes, coefficients, negative coefficients
              as boundary/cancellation data, signed zero fibers, and
              convolution.
ACCEPT-SCE.4  Map cancellation to boundary localization and the positive cone
              to Qbar_BECD internal effectivity strata.
ACCEPT-SCE.5  Generate endpoint, graph/Rosati/count, and control-death data
              from the signed effectivity orientation.

KILL-SCE.1    Reject positive-part truncation.
KILL-SCE.2    Reject absolute-value maps.
KILL-SCE.3    Reject sign/support quotients.
KILL-SCE.4    Reject signed-zero deletion.
KILL-SCE.5    Reject diagonal-total positivity.
KILL-SCE.6    Reject external ordering/factorization of support keys.
KILL-SCE.7    Reject endpoint/count/control/DH/Epstein filters.
KILL-SCE.8    Reject declared positive cones.
```
