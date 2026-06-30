# 450 - Qbar_BECD categorical closure multiplier DD.4 naturality totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-thirteenth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 449 left the strict-square branch live only if the same internal
Qbar_BECD effectivity stratum constructs a represented multiplier-action
functor with identity, transport composition, and product naturality. This
document fixes the next edge. DD.4 boundary localization cannot be attached
after that action, and the DD.4 class cannot be killed by separate splitters
on separate multiplier orbits. The same carrier boundary extension must make
the boundary square commute for C3, C9, and F22.

The DD.4-naturality totalization datum fixed by this cycle is:

```text
categorical source square: CatSq_Qbar_BECD_closes_doc443_boundary_cycle
facet cube: BCCube_CatSq_Qbar_BECD_facets
cube totalization: Tot_BCCube_CatSq_Qbar_BECD
internal effectivity domain: D_Qbar_BECD_eff
multiplier-action totalization: ActTot_BCCube_Qbar_BECD_multiplier_internal_stratum
multiplier-action functor: Act_BCCube_Qbar_BECD_multiplier_functor
DD.4 naturality totalization: DD4NatTot_BCCube_Qbar_BECD_multiplier_internal_stratum
DD.4 boundary localization: B_Qbar_BECD_DD4_multiplier_natural
carrier boundary extension: CarrierBdExt_Qbar_BECD_DD4_multiplier
transported splitter: Split_DD4_Qbar_BECD_transported_same_boundary
DD.4 naturality square: Sq_DD4Nat_Qbar_BECD_multiplier
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_multiplier_dd4_naturality_totalization_contract`
(CATDD4NATQBARBECD1-CATDD4NATQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 449 through the DD.4 SCC
interface, all exit 0.

## 1. Purpose

After doc 449, the cheap repair is:

```text
construct the multiplier-action functor,
then kill the DD.4 class separately on each visible transport orbit.
```

That is still a boundary-after-transport patch. A categorical source square
must make DD.4 boundary localization natural for the multiplier action. The
boundary rows for `z`, `T_C3(z)`, `T_C3(T_C3(z))=T_C9(z)`, `z*F22`,
`T_C3(z*F22)`, and `T_C9(z*F22)` must be typed by one DD.4 boundary map,
one carrier boundary extension, and one internal domain.

## 2. Lemma

```text
Lemma 450.1 (DD.4 boundary localization must be natural for the multiplier action).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The multiplier-action rows include:

    T_C3(T_C3(z)) = T_C9(z) = 2[9] - [18],
    T_C3(z*F22) = T_C3(z)*F22 = z*(C3*F22) = 4[6] - 2[12],
    T_C9(z*F22) = z*(C9*F22) = 4[18] - 2[36].

The DD.4 boundary rows for

    z,
    T_C3(z),
    T_C3(T_C3(z)),
    T_C9(z),
    z*F22,
    T_C3(z*F22),
    T_C3(z)*F22,
    z*(C3*F22),
    T_C9(z*F22),
    z*(C9*F22)

must all be typed by the same boundary localization
`B_Qbar_BECD_DD4_multiplier_natural`, the same internal domain
`D_Qbar_BECD_eff`, and the same DD.4 class.

Separate orbit splitters kill local copies but do not make
`T_C3(T_C3(-))=T_C9(-)` commute with boundary localization.
Boundary-after-transport filters reverse the construction direction.
Support boundaries and weighted-zero boundaries lose the obstruction
detected by `res_1`. Endpoint/count filters, boundary kernels, local
boundary stacks, finite boundary tables, declared DD.4 naturality, and
control shadows do not construct the boundary square.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_multiplier_dd4_naturality_totalization_contract`
verifies ten gates.

CATDD4NATQBARBECD1 records the represented categorical source square, the
doc-443 boundary fiber, source cube, multiplier-action totalization, DD.4
naturality totalization, carrier boundary extension, transported splitter,
ten transported boundary rows, H1 profile, endpoint balance, graph
composition, and Rosati sign.

CATDD4NATQBARBECD2 rejects recognition and equivalence wrappers as DD.4
naturality construction.

CATDD4NATQBARBECD3 rejects finite orbit closures and lone transports before
DD.4 naturality is even available.

CATDD4NATQBARBECD4 rejects endpoint and degree filters that type DD.4 only
after the source product action.

CATDD4NATQBARBECD5 rejects separate orbit splitters, free splitters,
boundary-after-transport filters, support boundaries, weighted-zero
boundaries, finite boundary tables, and declared DD.4 naturality.

CATDD4NATQBARBECD6 requires graph and Rosati faces to be typed by the same
DD.4-natural source product action.

CATDD4NATQBARBECD7 rejects control or Epstein shadows at the DD.4 boundary
formation stage.

CATDD4NATQBARBECD8 makes every DD.4-naturality totalization face mandatory.

CATDD4NATQBARBECD9 records that facet products after points leave controls,
DH, and Epstein formable.

CATDD4NATQBARBECD10 accepts only one internal multiplier-action source
totalization with natural DD.4 boundary localization.

Therefore the doc-449 multiplier-action totalization is still incomplete
unless DD.4 boundary localization is natural for the same represented
multiplier-action functor.

## 4. Consequence

The live strict-square branch is now:

```text
construct ActTot_BCCube_Qbar_BECD_multiplier_internal_stratum;
construct DD4NatTot_BCCube_Qbar_BECD_multiplier_internal_stratum;
construct B_Qbar_BECD_DD4_multiplier_natural;
construct CarrierBdExt_Qbar_BECD_DD4_multiplier;
prove the DD.4 class is killed by that same carrier boundary extension;
prove T_C3, T_C9, transport composition, and F22 product naturality commute
with DD.4 boundary localization;
prove the transported splitter comes from the same boundary;
prove controls and Epstein are undefined at DD.4 boundary formation.
```

The open construction target is no longer merely "construct the represented
multiplier-action totalization." It is "construct the represented
DD.4-natural multiplier-action totalization of the source cube."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. the totalized source cube;
3. represented multiplier-action functor;
4. DD.4 boundary localization natural for that functor;
5. carrier boundary extension killing the DD.4 class;
6. transported splitter from the same boundary;
7. boundary naturality for C3 and C9 transport composition;
8. boundary naturality for F22 product action;
9. same-domain typing for all transport boundary rows;
10. controls and Epstein undefined at DD.4 boundary formation;
11. idempotent closure of the boundary/cartesian/coherence/globular cycle.
```

Until this DD.4-natural multiplier-action source totalization exists, the
object remains missing.
