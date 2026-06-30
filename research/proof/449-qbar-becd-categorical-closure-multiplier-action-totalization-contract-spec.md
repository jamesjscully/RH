# 449 - Qbar_BECD categorical closure multiplier-action totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-twelfth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 448 left the strict-square branch live only if the same internal
Qbar_BECD effectivity stratum constructs a represented C3-multiplier orbit
closure. This document fixes the next edge. The C3 transport cannot be a
lone orbit closure. It must be part of a represented multiplier-action
functor with identity, composition, and product naturality.

The multiplier-action totalization datum fixed by this cycle is:

```text
categorical source square: CatSq_Qbar_BECD_closes_doc443_boundary_cycle
facet cube: BCCube_CatSq_Qbar_BECD_facets
cube totalization: Tot_BCCube_CatSq_Qbar_BECD
internal effectivity domain: D_Qbar_BECD_eff
mixed-orbit totalization: OrbTot_BCCube_Qbar_BECD_C3_internal_stratum
multiplier-action totalization: ActTot_BCCube_Qbar_BECD_multiplier_internal_stratum
multiplier-action functor: Act_BCCube_Qbar_BECD_multiplier_functor
identity transport: T_1_BCCube_Qbar_BECD_identity
C3 transport: T_C3_BCCube_Qbar_BECD_internal_stratum
C9 transport: T_C9_BCCube_Qbar_BECD_internal_stratum
transport composition: Comp_T_C3_T_C3_eq_T_C9_BCCube_Qbar_BECD
product naturality: Nat_T_multiplier_F22_BCCube_Qbar_BECD
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_multiplier_action_totalization_contract`
(CATMULACTQBARBECD1-CATMULACTQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 448 through the DD.4 SCC
interface, all exit 0.

## 1. Purpose

After doc 448, the cheap repair is:

```text
construct the C3 orbit closure,
record the rows 3,6,12,24,
and treat further multiplier composition as an external monoid label or a
finite transport table.
```

That still avoids the categorical action. If the source totalization carries
the strict-square product action, multiplier transports must compose inside
the same represented source domain. The C3 transport followed by the C3
transport is the C9 transport, and transport must be natural for products
such as F22.

## 2. Lemma

```text
Lemma 449.1 (multiplier transport must be functorial).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

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

The represented transport support now includes:

    1,2,3,6,9,12,18,36.

Therefore a lone C3 transport, finite C3 orbit closure, external multiplier
monoid, odd-base label, local orbit stack, finite transport table, declared
action functor, endpoint/count filter, boundary kernel, or control shadow is
not the represented multiplier-action source totalization.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_multiplier_action_totalization_contract`
verifies ten gates.

CATMULACTQBARBECD1 records the represented categorical source square, the
doc-443 boundary fiber, the source cube, internal effectivity stratum,
C3-orbit totalization, multiplier-action totalization, identity transport,
C3 transport, C9 transport, transport composition, product naturality, H1
profile, endpoint balance, graph composition, and Rosati sign.

CATMULACTQBARBECD2 rejects recognition and equivalence wrappers as
multiplier-action construction.

CATMULACTQBARBECD3 rejects finite orbit closures because C3 composed with C3
forces the C9 transport and the C9-F22 product row.

CATMULACTQBARBECD4 rejects endpoint and degree filters that type transport
only after the source product action.

CATMULACTQBARBECD5 keeps DD.4 exactness internal to the source cube and
rejects free boundary splitters, local tables, external labels, and boundary
kernels as substitutes for the action law.

CATMULACTQBARBECD6 requires graph and Rosati faces to be typed by the same
source product action that makes multiplier transport natural.

CATMULACTQBARBECD7 rejects control or Epstein shadows at the transport
formation stage.

CATMULACTQBARBECD8 makes every multiplier-action totalization face
mandatory.

CATMULACTQBARBECD9 records that facet products after points leave controls,
DH, and Epstein formable.

CATMULACTQBARBECD10 accepts only one internal multiplier-action source
totalization.

Therefore the doc-448 C3-orbit totalization is still incomplete unless the
same internal Qbar_BECD stratum constructs a represented multiplier-action
functor.

## 4. Consequence

The live strict-square branch is now:

```text
construct OrbTot_BCCube_Qbar_BECD_C3_internal_stratum;
construct ActTot_BCCube_Qbar_BECD_multiplier_internal_stratum;
construct Act_BCCube_Qbar_BECD_multiplier_functor;
prove identity transport inside the source domain;
prove T_C3(T_C3(z)) = T_C9(z) = 2[9]-[18];
prove T_C3(z*F22) = T_C3(z)*F22 = z*(C3*F22);
prove T_C9(z*F22) = z*(C9*F22) = 4[18]-2[36];
prove transport orbits remain typed by the same internal Qbar_BECD stratum;
prove controls and Epstein are undefined at that action totalization.
```

The open construction target is no longer merely "construct the represented
C3 orbit." It is "construct the represented multiplier-action totalization
of the source cube."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. the totalized source cube;
3. internal-effectivity-domain typing of that totalization;
4. represented C3 orbit closure;
5. represented multiplier-action functor;
6. identity transport;
7. transport composition, including T_C3 o T_C3 = T_C9;
8. product naturality for F22;
9. same-domain typing for all transport orbits;
10. controls and Epstein undefined at the action totalization;
11. idempotent closure of the boundary/cartesian/coherence/globular cycle.
```

Until this multiplier-action source totalization exists, the object remains
missing.
