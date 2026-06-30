# 456 - Qbar_BECD categorical closure represented source-fiber totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-nineteenth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 455 left the strict-square branch live only if the graph-formation gate is
source-typed by a carrier-generated source token and source fiber before graph
objects exist. This document fixes representability of that source fiber. A
source-typed specification is still insufficient if it is only a functor of
points, predicate subfibration, declared representer, formal universal
property, or local table of source labels. The source fiber must be
represented by an actual carrier-side object and universal arrow with
cartesian multiplier lifts.

The represented source-fiber datum fixed by this cycle is:

```text
categorical source square: CatSq_Qbar_BECD_closes_doc443_boundary_cycle
facet cube: BCCube_CatSq_Qbar_BECD_facets
cube totalization: Tot_BCCube_CatSq_Qbar_BECD
internal effectivity domain: D_Qbar_BECD_eff
multiplier-action functor: Act_BCCube_Qbar_BECD_multiplier_functor
DD.4 boundary localization: B_Qbar_BECD_DD4_multiplier_natural
endpoint degree maps: DegMaps_BCCube_Qbar_BECD_multiplier_endpoint
pushforward square: PF_Qbar_BECD_p1p2_DD4_endpoint
graph/Rosati/count totalization: GRCTot_BCCube_Qbar_BECD_pushforward_internal_stratum
source token: SrcTok_BCCube_Qbar_BECD_source_typed_graph_formation
source formation fiber: Fib_BCCube_Qbar_BECD_source_typed_graph_formation
representing object: Rep_BCCube_Qbar_BECD_source_fiber
universal arrow: eta_BCCube_Qbar_BECD_source
cartesian lifts: CartLift_BCCube_Qbar_BECD_multiplier_source_fiber
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_represented_source_fiber_totalization_contract`
(CATRSFQBARBECD1-CATRSFQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 455 through the DD.4 SCC
interface (149/149 exit 0).

## 1. Purpose

After doc 455, the cheap repair is:

```text
declare a source-typed functor of admissible categorical points,
then invoke Yoneda or a formal universal property and call it represented.
```

That is still not a carrier. A functor of points is useful after a
representing object exists; it does not provide the object. Likewise,
predicate subfibrations and discrete source labels still classify available
points, and local lift tables choose row-by-row transports rather than
producing cartesian multiplier lifts through one representer.

## 2. Lemma

```text
Lemma 456.1 (source typing must be represented).

The transported represented-source rows are:

    z                    -> cart 1,  graph 2,  count 4,
    T_C3(z)              -> cart 3,  graph 6,  count 36,
    T_C3(T_C3(z))        -> cart 9,  graph 18, count 324,
    T_C9(z)              -> cart 9,  graph 18, count 324,
    z*F22                -> cart 4,  graph 8,  count 64,
    T_C3(z*F22)          -> cart 12, graph 24, count 576,
    T_C3(z)*F22          -> cart 12, graph 24, count 576,
    z*(C3*F22)           -> cart 12, graph 24, count 576,
    T_C9(z*F22)          -> cart 36, graph 72, count 5184,
    z*(C9*F22)           -> cart 36, graph 72, count 5184.

Every row has the same categorical source square, source cube totalization,
internal effectivity domain, multiplier-action functor, DD.4 boundary
localization, endpoint maps, pushforward square, graph/Rosati/count
totalization, source token, source formation fiber, representing object,
universal arrow, and cartesian-lift family.

The following are substitutes only:

    specification functors,
    functors of points without a representer,
    Yoneda reversal,
    predicate subfibrations,
    discrete fibration labels,
    declared representers,
    formal universal properties,
    graph-object classifiers,
    local representers and finite representer tables,
    externally chosen or retuned cartesian lifts,
    semantic zeta labels,
    control, DH, or Epstein points.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_represented_source_fiber_totalization_contract`
verifies ten gates.

CATRSFQBARBECD1 records that specification functors still see controls unless
a representer excludes them at formation.

CATRSFQBARBECD2 records one representing object and universal arrow carrying
the cartesian multiplier lifts. The finite checks include C3 composed with C3
giving the C9 lift, and the C3/F22 transports commuting through C3F22 and
C9F22 at graph and count-degree level.

CATRSFQBARBECD3 rejects specification functors, functors of points, and
Yoneda reversal.

CATRSFQBARBECD4 rejects predicate subfibrations and discrete source-label
fibrations.

CATRSFQBARBECD5 rejects declared representers and formal universal
properties.

CATRSFQBARBECD6 rejects local representer tables, externally chosen cartesian
lifts, and retuned lifts.

CATRSFQBARBECD7 rejects control, DH, and Epstein points.

CATRSFQBARBECD8 makes every upstream represented source mandatory.

CATRSFQBARBECD9 rejects representer names without universal-arrow edges.

CATRSFQBARBECD10 accepts only one represented source fiber with an actual
universal arrow.

Therefore the doc-455 source-typed graph-formation-control-death-natural
graph/Rosati/count-natural pushforward-natural endpoint-degree-natural DD.4
multiplier-action totalization is still incomplete unless the source fiber is
represented by an actual carrier-side object and universal arrow with
cartesian multiplier lifts.

## 4. Consequence

The live strict-square branch is now:

```text
construct Rep_BCCube_Qbar_BECD_source_fiber;
construct eta_BCCube_Qbar_BECD_source;
prove the source token and source formation fiber are generated by that
universal arrow;
prove represented structural maps from the categorical source square,
source cube, internal effectivity domain, multiplier action, DD.4 boundary,
endpoint maps, pushforward square, graph/Rosati/count totalization, and
graph-formation control death into the representer;
prove cartesian multiplier lifts for C3, C9, F22, C3F22, and C9F22;
prove cartesian lift composition and coefficient preservation;
prove controls, DH, and Epstein are not points of the representer.
```

The open construction target is no longer merely "construct the source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization." It is "construct the represented source-fiber
source-typed graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. the totalized source cube;
3. represented multiplier-action functor;
4. DD.4 boundary localization natural for that functor;
5. endpoint-degree totalization generated by the same internal domain;
6. p1_* and p2_* pushforward squares generated by that domain;
7. graph composition generated by the pushforward square;
8. graph, Rosati, and count/degree transport naturality;
9. graph-formation control death generated by the graph/Rosati/count layer;
10. source token generated before graph objects exist;
11. represented source formation fiber;
12. actual representing object and universal arrow;
13. cartesian multiplier lifts through the same representer;
14. controls, DH, and Epstein not points of the representer;
15. finite-field count, graph-degree, and count-degree anchors as consequences;
16. coefficients and signed support preserved.
```

Until this represented source-fiber source-typed graph-formation-control-
death-natural graph/Rosati/count-natural pushforward-natural endpoint-degree-
natural DD.4-natural multiplier-action source totalization exists, the object
remains missing.
