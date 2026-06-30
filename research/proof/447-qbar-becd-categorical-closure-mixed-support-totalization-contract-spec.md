# 447 - Qbar_BECD categorical closure mixed-support totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-tenth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 446 left the strict-square branch live only if the doc-445 source cube
totalization is effective inside the internal Qbar_BECD effectivity stratum,
algebraizes over Z, keeps native prime-power valuation towers, types every
cube face by that stratum, and leaves controls/Epstein undefined there. This
document fixes the next edge. That internal-effective totalization is still
insufficient if it projects to the visible 2-power subtower and deletes the
mixed support `z*C3 = 2[3]-[6]`. The same internal stratum must retain mixed
support and the 2-power subtower together.

The mixed-support totalization datum fixed by this cycle is:

```text
categorical source square: CatSq_Qbar_BECD_closes_doc443_boundary_cycle
facet cube: BCCube_CatSq_Qbar_BECD_facets
cube totalization: Tot_BCCube_CatSq_Qbar_BECD
internal effectivity domain: D_Qbar_BECD_eff
effective totalization: EffTot_BCCube_Qbar_BECD_internal_stratum
mixed-support totalization: MixTot_BCCube_Qbar_BECD_internal_stratum
mixed support: MixSupp_BCCube_Qbar_BECD_3_6
2-power subtower: Pow2Subtower_BCCube_Qbar_BECD_1_2_4_8
algebraization over Z: Alg_BCCube_Qbar_BECD_over_Z
domain-typed cube: Typed_BCCube_Qbar_BECD_by_D_eff
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_mixed_support_totalization_contract`
(CATMIXTOTQBARBECD1-CATMIXTOTQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 446 through the DD.4 SCC
interface, all exit 0.

## 1. Purpose

Doc 446 stopped formal effective totalization. The remaining cheap repair is:

```text
use the native 2-power tower 1,2,4,8,16,32,64 as the whole internal stratum,
project all support to that tower,
and route z*C3 = 2[3]-[6] through external factorization, boundary-null
bookkeeping, or later control death.
```

That still does not construct the missing object. A source cube whose
endpoint, boundary, graph, Rosati, and control faces all come from the same
square cannot discard the mixed product `z*C3`. The mixed support `3,6` and
the 2-power support `1,2,4,8` must be internalized in the same Qbar_BECD
effectivity stratum. Otherwise the totalization is only a projection of the
square, not the square itself.

## 2. Lemma

```text
Lemma 447.1 (mixed-support totalization contract).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The totalization must be typed by the internal effectivity stratum

    D_Qbar_BECD_eff

and must carry:

    native prime-power tower      1,2,4,8,16,32,64,
    native valuation depths       0,1,2,3,4,5,6,
    mixed support                 3,6,
    total support                 1,2,3,4,6,8,
    algebraization over Z,
    all cube faces typed by the same internal stratum,
    controls undefined at that stratum,
    Epstein undefined at that stratum.

The required product rows include:

    z      = 2[1] - [2],
    z*F22  = 4[2] - 2[4],
    z*F41  = 2[4] - [8],
    z*C3   = 2[3] - [6].

Projection to the 2-power support keeps z, z*F22, and z*F41, but sends z*C3
to zero. Therefore a 2-power-only totalization deletes a real strict-square
product face.

Two-power projection, non-2 support deletion, external prime-axis tags,
mixed-support boundary-null declarations, local multiprime stacks, declared
mixed-support domains, and post-product control death do not construct the
missing object.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_mixed_support_totalization_contract`
verifies ten gates.

CATMIXTOTQBARBECD1 records the represented categorical source square, the
doc-443 boundary fiber, the facet cube, cube totalization, internal
effectivity domain, mixed-support totalization, algebraization, native
prime-power tower, mixed support, total support, H1 profile, finite-field
count anchors, endpoint balance, graph composition, and Rosati sign.

CATMIXTOTQBARBECD2 rejects recognition and equivalence wrappers as
mixed-support totalization construction.

CATMIXTOTQBARBECD3 rejects finite-anchor and truncationwise towers that do
not retain non-2 support.

CATMIXTOTQBARBECD4 rejects endpoint/degree totalizations that project to the
2-power tower and delete mixed support.

CATMIXTOTQBARBECD5 requires DD.4 exactness to be internal-mixed-support, not
a free splitter, valuation register, local table, external prime-axis tag, or
boundary-null declaration for the mixed support.

CATMIXTOTQBARBECD6 requires graph and Rosati faces to retain mixed
coefficients in the same domain as the 2-power subtower.

CATMIXTOTQBARBECD7 rejects post-product control death for mixed support:
controls and Epstein must be undefined at the mixed-support totalization
itself.

CATMIXTOTQBARBECD8 makes every mixed-support totalization face mandatory.

CATMIXTOTQBARBECD9 records that facet products after points leave controls,
DH, and Epstein formable.

CATMIXTOTQBARBECD10 accepts only one internal-mixed-support source
totalization.

Therefore the doc-446 internal-effective totalization is still incomplete
unless the same internal Qbar_BECD stratum retains the mixed support
`z*C3=2[3]-[6]` together with the 2-power subtower.

## 4. Consequence

The live strict-square branch is now:

```text
construct EffTot_BCCube_Qbar_BECD_internal_stratum;
construct MixTot_BCCube_Qbar_BECD_internal_stratum;
construct MixSupp_BCCube_Qbar_BECD_3_6;
construct Pow2Subtower_BCCube_Qbar_BECD_1_2_4_8;
prove z*C3 = 2[3]-[6] is retained rather than projected to zero;
prove mixed support and the 2-power subtower live in the same internal
Qbar_BECD effectivity stratum;
prove controls and Epstein are undefined at that mixed-support totalization.
```

The open construction target is no longer "make the totalization effective."
It is "construct the mixed-support internal totalization of the source cube."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. the totalized source cube;
3. internal-effectivity-domain typing of that totalization;
4. algebraization over Z;
5. native prime-power valuation tower;
6. mixed support 3,6 in the same internal domain;
7. coefficient and signed-support retention for z*C3;
8. rejection of 2-power projection as the totalization;
9. controls and Epstein undefined at the mixed-support totalization;
10. idempotent closure of the boundary/cartesian/coherence/globular cycle.
```

Until this mixed-support source totalization exists, the object remains
missing.
