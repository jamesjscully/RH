# 335 - Qbar_BECD strict-square product multiplier-transport composition contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-ninety-eighth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 334 left the strict-square branch live only through:

```text
a carrier-native C3-multiplier transport whose orbit carries the odd-base
subtower 3,6,12,24,... inside the same internal Qbar_BECD effectivity domain.
```

This document fixes the categorical composition edge. A represented
`C3`-transport cannot be a lone arrow. It must be part of a multiplier-action
functor with identity, composition, and naturality for the product action. In
particular, `T_C3 o T_C3` must agree with `T_C9`, and transport must commute
with `F22`. Single-arrow transports, finite orbit closures, external
multiplier monoids, odd-base labels, prime-axis tags, local stacks, finite
tables, declared action functors, endpoint/count filters, boundary kernels,
and control/DH/Epstein shadows do not construct that categorical square.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_transport_composition_contract`
(MTC1-MTC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_mixed_support_orbit_closure_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_mixed_support_subtower_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_internal_effectivity_image_contract`,
`prime_int_n1b_qbar_becd_strict_square_boundary_stratum_product_contract`,
`prime_int_n1b_qbar_becd_strict_square_boundary_convolution_module_contract`,
`prime_int_n1b_qbar_becd_internal_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 334, the cheap repair is:

```text
construct one C3-orbit closure and call it the mixed-support subtower.
```

That still avoids the categorical square. If the internal image carries
strict-square multiplication, multiplier transports must compose. The
transport of `z` by `C3`, followed by transport by `C3` again, is the same
as transport by `C9`. Product naturality also requires transport to commute
with multipliers like `F22`.

The live branch therefore narrows from "C3 orbit closure" to:

```text
construct a carrier-native multiplier-action functor on the internal
Qbar_BECD effectivity domain, with identity, composition, product naturality,
DD.4 naturality, and downstream endpoint/boundary/pushforward/graph/Rosati/
count/control outputs.
```

## 2. Lemma

```text
Lemma 335.1 (mixed-support transport must compose).

The multiplier characters satisfy:

    C3*C3 = C9.

On z = 2[1]-[2],

    T_C3(z)        = z*C3        = 2[3] - [6],
    T_C3(T_C3(z))  = z*C3*C3     = 2[9] - [18],
    T_C9(z)        = z*C9        = 2[9] - [18].

Thus:

    T_C3(T_C3(z)) = T_C9(z).

Product naturality with F22 gives:

    T_C3(z*F22) = T_C3(z)*F22 = z*(C3*F22) = 4[6] - 2[12],
    T_C9(z*F22) = z*(C9*F22) = 4[18] - 2[36].

The transport support now includes:

    1,2,3,6,9,12,18,36.

Therefore a single C3 arrow, finite C3 orbit closure, external multiplier
monoid, local orbit stack, finite table, or declared action functor is not
the represented multiplier-action functor. Endpoint, graph/count, boundary,
and control filters are downstream and cannot define the transport law.

Thus the accepted datum is exactly:

    carrier-native,
    actual multiplier-action functor,
    actual identity transport,
    actual transport composition,
    product action natural,
    orbits closed under composition,
    same domain types transport orbits,
    coefficients retained,
    signed support retained,
    relative depth native to the domain,
    DD.4 boundary localization natural,
    domain has no endpoint/count prerequisite,
    endpoint integrality generated,
    boundary localization generated,
    pushforward compatibility generated,
    graph/Rosati/count data generated,
    control death generated,
    controls undefined at transport formation,
    DH undefined at transport formation,
    Epstein undefined at transport formation,
    no single transport arrow,
    no finite orbit closure,
    no external multiplier monoid,
    no external odd-base label,
    no external prime factorization,
    no prime-axis tags,
    no local product stack,
    no finite transport table,
    no declared action functor,
    no endpoint-degree fiber,
    no graph/count fiber,
    no boundary-kernel definition,
    no weighted-zero locus,
    no support-key tower,
    no post-hoc gate intersection,
    not formable on controls, DH, or Epstein.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_TRANSPORT_COMPOSITION__T_C3_SQUARED_EQUALS_T_C9__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_transport_composition_contract`
verifies ten gates.

MTC1 records `C3*C3 = C9`, checks `T_C3(T_C3(z)) = T_C9(z)`, and checks
product naturality against `F22`.

MTC2 rejects a lone C3 transport arrow.

MTC3 rejects finite C3-orbit closures because `C9` and `C9*F22` are forced.

MTC4 rejects external multiplier monoids, odd-base labels, prime
factorization, and prime-axis tags.

MTC5 rejects local orbit stacks because they split the transport domain.

MTC6 rejects declared action functors and finite transport tables without
represented edges.

MTC7 rejects endpoint, graph/count, and boundary filters as too late.

MTC8 rejects weighted-zero and support-key loci.

MTC9 keeps transport composition tied to downstream square data.

MTC10 records the live predicate. Only the carrier-native multiplier-action
functor passes.

## 4. Impact on R1

```text
R1 after docs 138-335:
  NEWLY FIXED THIS CYCLE:
    - the mixed-support transport must be a categorical multiplier-action
      functor, not a single C3 transport or finite orbit closure. It must
      satisfy identity, composition, and product naturality, including
      T_C3^2 = T_C9.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the represented boundary-stratum product;
    - construct the product-to-internal-effectivity image map to the single
      internal Qbar_BECD effectivity domain;
    - construct the carrier-native multiplier-action functor on that domain;
    - prove identity, composition, product naturality, DD.4 naturality,
      coefficient/sign retention, relative valuation depth, and orbit closure;
    - prove endpoint integrality, boundary localization, pushforward
      compatibility, graph/Rosati/count data, and formation-level control
      death are generated there;
    - prove DH, Epstein, and controls are undefined at transport formation.

  DISCIPLINE:
    - single transports, finite orbit closures, external multiplier monoids,
      odd-base labels, local stacks, finite tables, declared functors,
      endpoint/count filters, boundary kernels, weighted-zero/support loci,
      and post-hoc control filters are diagnostics only.

  STILL OPEN:
    - construct the carrier-native multiplier-action functor, or kill the
      strict-square branch with a named mechanism at this point.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-MTC.1  Exhibit the multiplier-action functor on the internal Qbar_BECD
              effectivity domain.
ACCEPT-MTC.2  Prove identity and transport composition, including
              T_C3 o T_C3 = T_C9.
ACCEPT-MTC.3  Prove product naturality for strict-square character
              convolution.
ACCEPT-MTC.4  Prove DD.4 boundary localization is natural for the transport.
ACCEPT-MTC.5  Retain coefficients, signed support, and relative depth in one
              internal domain.
ACCEPT-MTC.6  Generate endpoint, boundary, pushforward, graph/Rosati/count,
              and control death from the transport domain.
ACCEPT-MTC.7  Prove DH, Epstein, and controls are undefined at transport
              formation.

KILL-MTC.1    Reject lone transport arrows.
KILL-MTC.2    Reject finite orbit closures.
KILL-MTC.3    Reject external multiplier monoids, odd-base labels,
              factorization, and prime-axis tags.
KILL-MTC.4    Reject local product stacks.
KILL-MTC.5    Reject finite transport tables.
KILL-MTC.6    Reject declared action functors without represented edges.
KILL-MTC.7    Reject endpoint/count filters and boundary kernels.
KILL-MTC.8    Reject weighted-zero and support-key loci.
KILL-MTC.9    Reject post-hoc gate intersections.
KILL-MTC.10   Reject control/DH/Epstein-formable shadows.
```
