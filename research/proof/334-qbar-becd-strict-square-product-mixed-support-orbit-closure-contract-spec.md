# 334 - Qbar_BECD strict-square product mixed-support orbit-closure contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-ninety-seventh cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 333 left the strict-square branch live only through:

```text
a carrier-native mixed-support internalization/subtower carrying
z*C3 = 2[3]-[6] in the same internal Qbar_BECD effectivity domain as the
2-power products.
```

This document fixes the orbit-closure edge. Since `z*C3` is a multiplier
translate of `z`, the mixed-support subtower cannot be a finite `{3,6}`
patch. It must be a represented `C3`-multiplier transport closed under the
strict-square product action. Compatibility with `F22` and `F41` already
forces support `12` and `24`; a finite patch, external odd-base label, local
product stack, finite table, declared transport, endpoint/count filter, or
control/DH/Epstein shadow is not the internal orbit closure.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_mixed_support_orbit_closure_contract`
(MOC1-MOC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_mixed_support_subtower_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_internal_effectivity_image_contract`,
`prime_int_n1b_qbar_becd_strict_square_boundary_stratum_product_contract`,
`prime_int_n1b_qbar_becd_strict_square_boundary_convolution_module_contract`,
`prime_int_n1b_qbar_becd_internal_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_effectivity_domain_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 333, the cheap repair is:

```text
add the two mixed keys 3 and 6 to the internal image,
then stop there.
```

That still treats `z*C3` as an exception. But the strict-square product has
already required a represented boundary-stratum product and module action.
Therefore multiplication by the `C3` character must act as a transport on
the internal domain. Once that transport exists, the mixed support closes
under the same product action as the 2-power tower.

The live branch therefore narrows from "mixed-support internalization" to:

```text
construct a carrier-native C3-multiplier transport whose orbit carries the
odd-base subtower 3,6,12,24,... inside the same internal Qbar_BECD
effectivity domain, equivariantly with DD.4 localization and the downstream
endpoint/boundary/pushforward/graph/Rosati/count/control outputs.
```

## 2. Lemma

```text
Lemma 334.1 (mixed support must close under the C3 multiplier orbit).

The base products include the 2-power subtower:

    z       = 2[1] - [2],
    z*F22   = 4[2] - 2[4],
    z*F41   = 2[4] - [8],
    z*(L*F22) = 4[2] + 2[4] - 2[8].

The C3 translate and its products are:

    z*C3       = 2[3] - [6],
    z*C3*L     = 2[3] + [6] - [12],
    z*C3*F22   = 4[6] - 2[12],
    z*C3*F41   = 2[12] - [24],
    z*C3*(L*F22) = 4[6] + 2[12] - 2[24].

Moreover:

    (z*C3)*F22 = z*(C3*F22).

Thus a finite `{3,6}` mixed-support patch is not closed under the product
action. The C3 orbit exposes an odd-base subtower:

    3,6,12,24
    relative depths 0,1,2,3 after C3 transport.

This relative-depth table is a diagnostic only unless the C3 transport is
represented by the carrier. External odd-base labels, prime factorizations,
prime-axis tags, local base-by-odd stacks, finite orbit samples, finite
product tables, declared transports, endpoint/count filters, boundary
kernels, and post-hoc control death do not construct the transport.

Thus the accepted datum is exactly:

    carrier-native,
    actual mixed-support internalization,
    actual multiplier transport,
    product action equivariant,
    orbit closed under character convolution,
    same domain types the base and C3-orbit products,
    odd-base subtower native to the domain,
    base prime-power subtower native to the domain,
    coefficients retained,
    signed support retained,
    relative depth native to the domain,
    DD.4 boundary localization equivariant,
    domain has no endpoint/count prerequisite,
    endpoint integrality generated,
    boundary localization generated,
    pushforward compatibility generated,
    graph/Rosati/count data generated,
    control death generated,
    controls undefined at orbit formation,
    DH undefined at orbit formation,
    Epstein undefined at orbit formation,
    no finite mixed patch,
    no truncated orbit,
    no external odd-base label,
    no external prime factorization,
    no prime-axis tags,
    no local product stack,
    no finite orbit sample,
    no finite product table,
    no declared transport,
    no endpoint-degree fiber,
    no graph/count fiber,
    no boundary-kernel definition,
    no control-death-after-orbit declaration,
    no weighted-zero locus,
    no support-key tower,
    no post-hoc gate intersection,
    not formable on controls, DH, or Epstein.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MIXED_SUPPORT_ORBIT_CLOSURE__C3_FORCES_ODD_BASE_SUBTOWER__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_mixed_support_orbit_closure_contract`
verifies ten gates.

MOC1 records the base products, the C3-orbit products, the associativity
check `(z*C3)*F22 = z*(C3*F22)`, and the odd-base support `3,6,12,24`.

MOC2 rejects finite `{3,6}` patches because `F22` and `F41` force `12` and
`24`.

MOC3 rejects odd-base labels and prime factorizations as substitutes for
transport.

MOC4 rejects local base-by-odd stacks because they split the domain.

MOC5 rejects declared transports and finite orbit tables without represented
edges.

MOC6 rejects endpoint, boundary, and control filters as downstream.

MOC7 rejects weighted-zero and support-key loci.

MOC8 makes endpoint, pushforward, graph/Rosati/count, and control death
mandatory outputs of orbit closure.

MOC9 records the control/DH/Epstein failure mode.

MOC10 records the live predicate. Only carrier-native multiplier-orbit
closure passes.

## 4. Impact on R1

```text
R1 after docs 138-334:
  NEWLY FIXED THIS CYCLE:
    - the mixed-support subtower is not a finite 3,6 patch. It must be a
      carrier-native C3-multiplier orbit closed under strict-square character
      convolution, forcing the odd-base subtower 3,6,12,24,...

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the represented boundary-stratum product;
    - construct the product-to-internal-effectivity image map to the single
      internal Qbar_BECD effectivity domain;
    - construct the carrier-native C3-multiplier transport and its orbit
      closure inside that domain;
    - prove base prime-power subtowers, odd-base subtowers, coefficients,
      signed support, relative valuation depth, and DD.4 localization are
      retained equivariantly;
    - prove endpoint integrality, boundary localization, pushforward
      compatibility, graph/Rosati/count data, and formation-level control
      death are generated there;
    - prove DH, Epstein, and controls are undefined at orbit formation.

  DISCIPLINE:
    - finite mixed patches, external odd-base labels, prime factorization,
      local stacks, finite orbit samples, finite product tables, declared
      transports, endpoint/count filters, boundary kernels, and post-hoc
      control death are diagnostics only.

  STILL OPEN:
    - construct the carrier-native multiplier-orbit closure, or kill the
      strict-square branch with a named mechanism at this point.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-MOC.1  Exhibit the C3-multiplier transport inside the internal
              Qbar_BECD effectivity domain.
ACCEPT-MOC.2  Prove the orbit is closed under strict-square character
              convolution.
ACCEPT-MOC.3  Type the base 2-power subtower and the C3 odd-base subtower
              by the same internal domain.
ACCEPT-MOC.4  Retain coefficients, signed support, relative depth, and DD.4
              localization equivariantly.
ACCEPT-MOC.5  Generate endpoint, boundary, pushforward, graph/Rosati/count,
              and control death from orbit closure.
ACCEPT-MOC.6  Prove DH, Epstein, and controls are undefined at orbit
              formation.

KILL-MOC.1    Reject finite mixed-support patches.
KILL-MOC.2    Reject truncated orbits.
KILL-MOC.3    Reject external odd-base labels, prime factorizations, and
              prime-axis tags.
KILL-MOC.4    Reject local base-by-odd product stacks.
KILL-MOC.5    Reject finite orbit samples and finite product tables.
KILL-MOC.6    Reject declared transports without represented edges.
KILL-MOC.7    Reject endpoint/count filters and boundary-kernel definitions.
KILL-MOC.8    Reject control-death-after-orbit declarations.
KILL-MOC.9    Reject weighted-zero and support-key loci.
KILL-MOC.10   Reject control/DH/Epstein-formable shadows.
```
