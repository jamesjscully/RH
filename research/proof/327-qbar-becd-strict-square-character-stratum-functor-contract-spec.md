# 327 - Qbar_BECD strict-square character-stratum functor contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-ninetieth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 326 left the strict-square branch live only through:

```text
an actual non-EM extraction functor from strict-square character data to
Qbar_BECD internal effectivity strata.
```

This document sharpens that extraction. It cannot be a scalar axis selector
on the universal character algebra. It must be a full character-to-strata
functor retaining multi-axis classes, coefficients, signed zero-fiber data,
and convolution before producing prime-power subtowers, endpoint/boundary
data, graph/Rosati/count data, and formation-level control death.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_character_stratum_functor_contract`
(SCF1-SCF10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_effectivity_extraction_contract`,
`prime_int_n1b_cc_strict_square_divided_power_no_go`,
`prime_int_n1b_qbar_becd_effectivity_first_generator_orientation_contract`,
`prime_int_n1b_qbar_becd_internal_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_effectivity_domain_contract`,
`prime_int_n1b_represented_carrier_gate_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

The cheapest attempted extraction after doc 326 is:

```text
compute chi_col,
choose one distinguished support axis,
call that axis the effectivity stratum.
```

This is too weak. The strict square signal is not just the presence of a
support integer. It is the whole character object: multiple support axes,
coefficients, signed zero-fiber classes, and convolution. A scalar selector
throws away exactly the square-only data that made the branch worth keeping.

The live strict-square branch therefore narrows from "build an extraction
functor" to:

```text
build a full character-to-internal-strata functor.
```

## 2. Lemma

```text
Lemma 327.1 (axis selection is not character-to-strata extraction).

The strict-square character data contains:

    chi(L)      = [2] + [1],
    chi(C3)     = [3],
    chi(F22)    = 2[2],
    chi(F41)    = [4],
    chi(zero)   = 2[1] - [2],
    chi(L*F22)  = 2[4] + 2[2].

The diagonal total collapses the square-only split:

    mu(L) = mu(C3) = 3,
    Phi'_2(L) = 1,
    Phi'_2(C3) = 0.

Scalar support selectors fail structurally:

    min chi(L) = 1, max chi(L) = 2;
    singleton selection is undefined on chi(L);
    coefficient selection is undefined on chi(L) and selects 2 on 2[2];
    prime-support selection is undefined on [4];
    min/max select axes from the signed zero-fiber character.

Factoring support keys, for example reading [4] as the 2^2 tower, imports
external prime factorization and is not a represented strict-square map.
Rejecting signed zero-fiber characters throws away object-level square data.
Controls can mimic the scalar profiles:

    dim2 -> [1]+[2],
    dim4 -> 2[2],
    dim8 -> [4].

Thus the accepted strict-square datum is exactly:

    actual strict-square character data,
    actual character convolution,
    actual character-stratum functor,
    functor not a scalar axis selector,
    multi-axis classes retained,
    coefficients retained,
    signed zero-fiber data retained,
    convolution mapped to stratum product,
    internal effectivity domain produced,
    prime-power subtowers produced,
    endpoint integrality generated,
    boundary localization generated,
    graph/Rosati/count data generated,
    controls undefined at the functor,
    Epstein undefined at the functor,
    no diagonal-total selector,
    no single-axis selector,
    no min/max/singleton/coefficient/prime-support selector,
    no external prime factorization,
    no zero-fiber deletion,
    no endpoint/count-fiber selector,
    no declared stratum functor,
    not formable on controls.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_CHARACTER_STRATUM_FUNCTOR__FULL_CHI_FUNCTOR_NOT_AXIS_SELECTOR__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_character_stratum_functor_contract`
verifies ten gates.

SCF1 records the strict-square character data, including multi-axis,
coefficient, signed zero-fiber, and convolution information.

SCF2 rejects diagonal-total selection because it collapses the `L` / `C3`
strict-square split.

SCF3 rejects scalar axis selectors: min, max, singleton support, coefficient,
and prime-support rules each discard required character structure.

SCF4 rejects factoring character keys as an external prime-axis selector.

SCF5 rejects deleting signed zero-fiber data.

SCF6 records control formability of scalar character-axis profiles.

SCF7 makes endpoint generation mandatory.

SCF8 rejects declared character-stratum functors without represented edges.

SCF9 records the accepted branch: full character data is retained before
strata are produced.

SCF10 records the live predicate. Only a full character-to-strata functor
passes.

## 4. Impact on R1

```text
R1 after docs 138-327:
  NEWLY FIXED THIS CYCLE:
    - strict-square extraction cannot be scalar axis selection on chi_col.
      The branch now requires a full character-to-internal-strata functor.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct a represented non-EM functor from strict-square character
      objects to Qbar_BECD internal effectivity strata;
    - prove it retains multi-axis classes, coefficients, signed zero-fiber
      data, and convolution;
    - prove it maps convolution to the stratum product;
    - prove prime-power subtowers, endpoint integrality, boundary
      localization, graph/Rosati/count data, and formation-level control
      death are generated from that functor.

  DISCIPLINE:
    - diagonal totals, scalar axis selection, support-key prime
      factorization, signed-zero deletion, endpoint/count fibers, and
      declared functors are diagnostics only.

  STILL OPEN:
    - construct the full represented strict-square character-to-strata
      functor, or kill that stricter branch with a named mechanism.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-SCF.1  Exhibit an actual character-to-strata functor.
ACCEPT-SCF.2  Retain multi-axis classes, coefficients, signed zero-fiber
              data, and convolution.
ACCEPT-SCF.3  Map convolution to the Qbar_BECD internal stratum product.
ACCEPT-SCF.4  Produce prime-power subtowers without scalar axis selection.
ACCEPT-SCF.5  Generate endpoint, boundary, graph/Rosati/count, and control
              death from the character-stratum functor.

KILL-SCF.1    Reject diagonal-total selectors.
KILL-SCF.2    Reject min/max/singleton/coefficient/prime-support selectors.
KILL-SCF.3    Reject external factorization of support keys as a prime axis.
KILL-SCF.4    Reject deletion of signed zero-fiber data.
KILL-SCF.5    Reject endpoint/count-fiber selectors.
KILL-SCF.6    Reject packages formable on controls.
```
