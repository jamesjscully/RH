# 326 - Qbar_BECD strict-square effectivity extraction contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-eighty-ninth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Docs 323-325 fixed the current target:

```text
a non-circular represented internal Qbar_BECD effectivity-domain primitive.
```

Docs 187-188 left one strong local positive signal: the strict Gamma-set
square has real object-level divided-power and character data that does not
collapse to the diagonal. This document says exactly how that signal can
still matter. It cannot be used raw. It needs an actual non-EM extraction
functor from strict-square character data to the Qbar_BECD internal
effectivity stratum.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_effectivity_extraction_contract`
(SSE1-SSE10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_strict_square_divided_power_no_go`,
`prime_int_n1b_cc_pic_jacobian_square_no_go`,
`prime_int_n1b_qbar_becd_effectivity_first_generator_orientation_contract`,
`prime_int_n1b_qbar_becd_internal_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_effectivity_domain_contract`,
`prime_int_n1b_represented_carrier_gate_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

The strict square branch is worth preserving because it supplies real
square-only information:

```text
strict Gamma-set square object-level data distinguishes classes that the
diagonal curve shadow identifies.
```

But docs 187-188 already killed the direct promotion:

```text
strict-square invariants themselves = End(S^2/Z).
```

The remaining live question is narrower and more useful:

```text
Can strict-square object-level character data be extracted as the internal
Qbar_BECD effectivity stratum demanded by docs 323-325?
```

This document separates the branch cleanly. Raw divided-power invariants,
raw character monoids, diagonal published probes, ad-hoc grading
dictionaries, endpoint/count fibers, and declared functors fail. A surviving
strict-square route must construct the extraction functor.

## 2. Lemma

```text
Lemma 326.1 (strict-square data requires an extraction functor).

The strict Gamma-set square has real object-level noncollapse. For

    L  = ((1,1),(1,1), edges (1,1),(1,2),(2,1)),
    C3 = ((3),(1), edge (1,1)),

one has

    mu(L) = mu(C3) = 3,
    Phi'_2(L) = 1,
    Phi'_2(C3) = 0.

For

    F22 = ((2),(2), edge (1,1)),
    F41 = ((4),(1), edge (1,1)),

one has

    mu(F22) = mu(F41) = 4,
    Phi_3(F22) = 0,
    Phi_3(F41) = 1.

The zero fiber also splits:

    chi_col = 2[1] - [2].

The universal character convolution is real:

    chi(L)   = [2] + [1],
    chi(C3)  = [3],
    chi(F22) = 2[2],
    chi(F41) = [4],
    chi(L*F22) = chi(L) * chi(F22).

This is a positive signal, but it overproduces axes and remains diagnostic
until an extraction functor exists. The accepted strict-square branch must
contain represented edges:

    strict_square_data -> extraction_functor,
    extraction_functor -> internal_effectivity_domain,
    internal_effectivity_domain -> endpoint,
    internal_effectivity_domain -> boundary,
    internal_effectivity_domain -> control_death,
    endpoint -> pushforward,
    boundary -> pushforward,
    pushforward -> graph,
    graph -> Rosati,
    graph -> count_degree.

The accepted datum is exactly:

    actual strict-square object data,
    visible diagonal-fiber noncollapse,
    visible bilinear factorization memory,
    visible universal character data,
    actual extraction functor,
    non-EM extraction,
    extraction not factorizing through the diagonal,
    characters mapped to internal strata,
    internal effectivity domain produced,
    prime-power towers produced,
    valuation depth produced,
    endpoint integrality generated,
    boundary localization generated,
    graph/Rosati/count data generated,
    controls undefined at extraction,
    Epstein undefined at extraction,
    no raw divided-power promotion,
    no raw character-monoid promotion,
    no published diagonal probe,
    no ad-hoc grading dictionary,
    no external prime-axis selector,
    no endpoint/count-fiber extraction,
    no declared extraction functor,
    not formable on controls.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_EFFECTIVITY_EXTRACTION__NON_EM_FUNCTOR_OR_BRANCH_DIES__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_effectivity_extraction_contract`
verifies ten gates.

SSE1 records strict-square object-level noncollapse: diagonal fibers and
bilinear factorizations are separated.

SSE2 records the universal character convolution and its overproduction of
axes.

SSE3 rejects raw divided-power invariants as the extraction functor.

SSE4 rejects the raw character monoid as a canonical effectivity stratum.

SSE5 rejects published diagonal probes because they lose the square-only
split.

SSE6 rejects ad-hoc grading dictionaries such as reading a Z/2 invariant as
a Bokstedt degree.

SSE7 rejects endpoint/count-fiber extraction because it reverses the
first-generation direction fixed in doc 325.

SSE8 rejects declared extraction functors without represented edges.

SSE9 records the accepted branch: an actual non-EM extraction functor to
internal effectivity strata, producing prime-power towers and valuation
depth.

SSE10 records the live predicate. Only represented strict-square extraction
passes.

## 4. Impact on R1

```text
R1 after docs 138-326:
  NEWLY FIXED THIS CYCLE:
    - the strict-square positive signal remains live only through an actual
      non-EM extraction functor to Qbar_BECD internal effectivity strata.
      Raw divided-power invariants, character monoids, diagonal probes,
      ad-hoc grading dictionaries, endpoint/count fibers, and declared
      functors do not count.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct a represented non-EM extraction functor from strict Gamma-set
      square character data to the Qbar_BECD internal effectivity stratum;
    - prove it does not factor through the diagonal curve shadow;
    - prove it maps character data to internal Cartier/effectivity strata;
    - prove prime-power towers and valuation depth are produced there;
    - prove endpoint integrality, boundary localization, graph/Rosati/count
      data, and formation-level control death are generated from it.

  DISCIPLINE:
    - strict-square data is valuable only as source data for this extraction
      functor. It is not itself the missing object.

  STILL OPEN:
    - construct the represented strict-square-to-effectivity extraction
      functor, or prove this branch impossible with a named mechanism.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-SSE.1  Exhibit actual strict-square source data and the extraction
              functor.
ACCEPT-SSE.2  Prove the extraction is non-EM and does not factor through the
              diagonal.
ACCEPT-SSE.3  Map strict-square character data to Qbar_BECD internal
              effectivity strata.
ACCEPT-SSE.4  Produce prime-power towers and valuation depth in those strata.
ACCEPT-SSE.5  Generate endpoint, boundary, graph/Rosati/count, and control
              death from the extracted domain.

KILL-SSE.1    Reject raw divided-power invariants as the carrier domain.
KILL-SSE.2    Reject raw character monoids or external prime-axis selectors.
KILL-SSE.3    Reject published diagonal probes.
KILL-SSE.4    Reject ad-hoc grading dictionaries.
KILL-SSE.5    Reject endpoint/count-fiber extraction.
KILL-SSE.6    Reject declared extraction functors without represented edges.
```
