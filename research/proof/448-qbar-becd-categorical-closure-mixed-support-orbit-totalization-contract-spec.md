# 448 - Qbar_BECD categorical closure mixed-support orbit-totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-eleventh cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 447 left the strict-square branch live only if the same internal
Qbar_BECD effectivity stratum retains the mixed support `z*C3 = 2[3]-[6]`
together with the 2-power subtower inside the categorical source
totalization. This document fixes the next edge. That mixed support cannot be
a finite `{3,6}` patch. Because `z*C3` is a multiplier translate of `z`, the
same source totalization must construct a represented `C3`-multiplier orbit
closure, equivariantly with the product action and the source cube.

The orbit-totalization datum fixed by this cycle is:

```text
categorical source square: CatSq_Qbar_BECD_closes_doc443_boundary_cycle
facet cube: BCCube_CatSq_Qbar_BECD_facets
cube totalization: Tot_BCCube_CatSq_Qbar_BECD
internal effectivity domain: D_Qbar_BECD_eff
effective totalization: EffTot_BCCube_Qbar_BECD_internal_stratum
mixed-support totalization: MixTot_BCCube_Qbar_BECD_internal_stratum
mixed-orbit totalization: OrbTot_BCCube_Qbar_BECD_C3_internal_stratum
C3 multiplier transport: T_C3_BCCube_Qbar_BECD_internal_stratum
mixed support: MixSupp_BCCube_Qbar_BECD_3_6
2-power subtower: Pow2Subtower_BCCube_Qbar_BECD_1_2_4_8
odd-base subtower: OddBaseSubtower_BCCube_Qbar_BECD_3_6_12_24
algebraization over Z: Alg_BCCube_Qbar_BECD_over_Z
domain-typed cube: Typed_BCCube_Qbar_BECD_by_D_eff
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_mixed_support_orbit_totalization_contract`
(CATORBTOTQBARBECD1-CATORBTOTQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 447 through the DD.4 SCC
interface, all exit 0.

## 1. Purpose

After doc 447, the cheap repair is:

```text
retain z*C3 = 2[3]-[6] as a finite mixed-support exception,
keep the visible 2-power subtower separate,
and let endpoint/count filters, boundary kernels, or later control death
handle the remaining products.
```

That still does not construct the missing object. The mixed row is not an
isolated row. The strict-square product action already sees the multipliers
`F22` and `F41`, and those multipliers force the `C3` translate to generate
support `12` and `24`. Therefore the categorical totalization must close the
mixed support under the represented `C3` multiplier orbit before endpoint,
boundary, graph, Rosati, or control facts are invoked.

## 2. Lemma

```text
Lemma 448.1 (mixed-support totalization must close the C3 orbit).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The base products include:

    z          = 2[1] - [2],
    z*F22      = 4[2] - 2[4],
    z*F41      = 2[4] - [8],
    z*(L*F22)  = 4[2] + 2[4] - 2[8].

The C3 translate and its products are:

    z*C3          = 2[3] - [6],
    z*C3*L        = 2[3] + [6] - [12],
    z*C3*F22      = 4[6] - 2[12],
    z*C3*F41      = 2[12] - [24],
    z*C3*(L*F22)  = 4[6] + 2[12] - 2[24].

Moreover:

    (z*C3)*F22 = z*(C3*F22).

Thus a finite `{3,6}` mixed-support patch is not closed under the product
action. The same internal Qbar_BECD stratum must carry the base 2-power
subtower and the odd-base subtower:

    3,6,12,24
    relative depths 0,1,2,3 after C3 transport.

The relative-depth table is a diagnostic only unless the `C3` transport is
represented by the carrier and typed by the same source totalization.
External odd-base labels, prime factorizations, local base-by-odd stacks,
finite orbit samples, finite product tables, declared transports,
endpoint/count filters, boundary kernels, and post-orbit control death do
not construct the missing object.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_mixed_support_orbit_totalization_contract`
verifies ten gates.

CATORBTOTQBARBECD1 records the represented categorical source square, the
doc-443 boundary fiber, the facet cube, cube totalization, internal
effectivity domain, mixed-support totalization, represented C3 transport,
odd-base orbit support `3,6,12,24`, relative depths, H1 profile, endpoint
balance, graph composition, and Rosati sign.

CATORBTOTQBARBECD2 rejects recognition and equivalence wrappers as
orbit-totalization construction.

CATORBTOTQBARBECD3 rejects finite `{3,6}` patches and truncated orbits,
because `F22` and `F41` force `12` and `24`.

CATORBTOTQBARBECD4 rejects endpoint and degree filters that type only the
visible 2-power side or split the C3 orbit from the source domain.

CATORBTOTQBARBECD5 requires DD.4 exactness to be equivariant for the
internal C3 orbit, not a free splitter, boundary kernel, valuation register,
external prime-axis tag, or odd-base label.

CATORBTOTQBARBECD6 requires graph and Rosati faces to be typed by the same
source product action that closes the C3 orbit.

CATORBTOTQBARBECD7 rejects post-orbit control death: controls and Epstein
must be undefined at the internal orbit totalization itself.

CATORBTOTQBARBECD8 makes every orbit-totalization face mandatory.

CATORBTOTQBARBECD9 records that facet products after points leave controls,
DH, and Epstein formable.

CATORBTOTQBARBECD10 accepts only one internal C3-orbit source totalization.

Therefore the doc-447 mixed-support totalization is still incomplete unless
the same internal Qbar_BECD stratum constructs a represented C3-multiplier
orbit closure.

## 4. Consequence

The live strict-square branch is now:

```text
construct MixTot_BCCube_Qbar_BECD_internal_stratum;
construct OrbTot_BCCube_Qbar_BECD_C3_internal_stratum;
construct T_C3_BCCube_Qbar_BECD_internal_stratum;
prove z*C3 = 2[3]-[6] is retained rather than projected to zero;
prove z*C3*F22 = 4[6]-2[12] and z*C3*F41 = 2[12]-[24] are retained;
prove the odd-base subtower 3,6,12,24 and the 2-power subtower live in the
same internal Qbar_BECD effectivity stratum;
prove the C3 orbit is closed under the source product action;
prove controls and Epstein are undefined at that orbit totalization.
```

The open construction target is no longer merely "construct the
mixed-support internal totalization." It is "construct the represented C3
multiplier-orbit totalization of the source cube."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. the totalized source cube;
3. internal-effectivity-domain typing of that totalization;
4. algebraization over Z;
5. native prime-power valuation tower;
6. mixed support 3,6 in the same internal domain;
7. represented C3 multiplier transport;
8. odd-base subtower 3,6,12,24 with relative depths 0,1,2,3;
9. product-action closure of the C3 orbit, including F22 and F41 faces;
10. controls and Epstein undefined at the orbit totalization;
11. idempotent closure of the boundary/cartesian/coherence/globular cycle.
```

Until this C3-orbit source totalization exists, the object remains missing.
