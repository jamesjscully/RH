# 459 - Qbar_BECD categorical closure monoidwide square-layer coherence totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-twenty-second cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 458 left the strict-square branch live only if the same square-layer
coherence commutes with DD.4 boundary, endpoint degree, p1/p2 pushforward,
graph composition, Rosati, count/degree, and control death on the visible
`C3/C9/F22` patch. This document fixes the next edge. A local `C3`-adic
coherence table is still too small. The same square-layer coherence must be
monoidwide for the carrier-native multiplier-action functor. In particular,
it must survive an independent multiplier direction:

```text
C3*C5 = C5*C3 = C15,
C3*C3*C5 = C45,

and product naturality with F22.
```

The monoidwide square-layer coherence datum fixed by this cycle is:

```text
categorical source square: CatSq_Qbar_BECD_closes_doc443_boundary_cycle
facet cube: BCCube_CatSq_Qbar_BECD_facets
cube totalization: Tot_BCCube_CatSq_Qbar_BECD
internal effectivity domain: D_Qbar_BECD_eff
multiplier-action functor: Act_BCCube_Qbar_BECD_multiplier_functor
DD.4 boundary localization: B_Qbar_BECD_DD4_multiplier_natural
endpoint degree maps: DegMaps_BCCube_Qbar_BECD_multiplier_endpoint
p1 pushforward: p1_star_Qbar_BECD_endpoint_boundary
p2 pushforward: p2_star_Qbar_BECD_endpoint_boundary
pushforward square: PF_Qbar_BECD_p1p2_DD4_endpoint
graph/Rosati/count totalization: GRCTot_BCCube_Qbar_BECD_pushforward_internal_stratum
proper graph layer: G_Qbar_BECD_pushforward_prop
Rosati layer: R_Qbar_BECD_pushforward_positive
count/degree layer: CD_Qbar_BECD_pushforward
graph-formation gate: K_Qbar_BECD_graph_formation_death
control-death naturality: Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD
source token: SrcTok_BCCube_Qbar_BECD_source_typed_graph_formation
source formation fiber: Fib_BCCube_Qbar_BECD_source_typed_graph_formation
representing object: Rep_BCCube_Qbar_BECD_source_fiber
universal arrow: eta_BCCube_Qbar_BECD_source
cartesian lifts: CartLift_BCCube_Qbar_BECD_multiplier_source_fiber
cartesian coherence cells: Coh_BCCube_Qbar_BECD_cartesian_lifts
square-layer coherence: SLC_BCCube_Qbar_BECD_boundary_pushforward_graph
monoidwide square-layer coherence: MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_monoidwide_square_layer_coherence_totalization_contract`
(CATMWCSLCQBARBECD1-CATMWCSLCQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 458 through the DD.4 SCC
interface (152/152 exit 0).

## 1. Purpose

After doc 458, the cheap repair is:

```text
build a coherent C3/C9/F22 square-layer patch and call it the multiplier
action.
```

That still does not construct the carrier multiplier action. It can pass the
visible `T_C3(T_C3(z))=T_C9(z)` and `F22` tests while leaving another prime
direction, such as `C5`, supplied by a separate finite table or external
prime-factor label. The square itself must construct the monoid action, so
independent multiplier paths must use the same coherence id and the same
square-layer chain.

The live branch narrows from:

```text
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization
```

to:

```text
monoidwide-square-layer-coherent square-layer-coherent cartesian-coherent
represented source-fiber source-typed graph-formation-control-death-natural
graph/Rosati/count-natural pushforward-natural endpoint-degree-natural
DD.4-natural multiplier-action source totalization.
```

## 2. Lemma

```text
Lemma 459.1 (square-layer coherence must be monoidwide).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The represented monoidwide rows carry one coherence id

    MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers

over the same square-layer chain:

    B_Qbar_BECD_DD4_multiplier_natural,
    DegMaps_BCCube_Qbar_BECD_multiplier_endpoint,
    p1_star_Qbar_BECD_endpoint_boundary,
    p2_star_Qbar_BECD_endpoint_boundary,
    G_Qbar_BECD_pushforward_prop,
    R_Qbar_BECD_pushforward_positive,
    CD_Qbar_BECD_pushforward,
    Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD.

The new independent multiplier checks are:

    T_C3(T_C5(z))              = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))        = T_C9(T_C5(z))
                                = T_C45(z)            = {45:2, 90:-1},
    T_C15(z*F22)               = T_C3(T_C5(z))*F22
                                = z*(C15*F22)        = {30:4, 60:-2},
    T_C45(z*F22)               = T_C3(T_C3(T_C5(z)))*F22
                                = z*(C45*F22)        = {90:4, 180:-2}.

All endpoint, DD.4 boundary, and p1/p2 pushforward defects remain zero. The
finite count and Rosati diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus local C3 patches, finite generator tables, external prime-axis labels,
declared monoid actions, formal pentagon/hexagon diagrams, late boundary/
pushforward/graph filters, degree/count/support equality, weighted-zero
tests, local layer tables, external 2-cells, retuned multiplier coherences,
and control/DH/Epstein monoid-coherent shadows do not construct this layer.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_monoidwide_square_layer_coherence_totalization_contract`
verifies ten gates.

CATMWCSLCQBARBECD1 records one monoidwide square-layer coherence id across
`C3`, `C5`, `C15`, `C45`, and `F22`.

CATMWCSLCQBARBECD2 records again that graph identities do not supply
monoidwide coherence.

CATMWCSLCQBARBECD3 rejects a local `C3/C9` square-layer patch.

CATMWCSLCQBARBECD4 rejects prime-axis labels and factorization tables as
external data.

CATMWCSLCQBARBECD5 rejects declared monoid actions and formal coherence
diagrams as labels.

CATMWCSLCQBARBECD6 proves the independent multiplier paths and `F22`
naturality are mandatory.

CATMWCSLCQBARBECD7 rejects boundary, pushforward, and graph filters after
monoid action.

CATMWCSLCQBARBECD8 rejects numeric equalities and local layer tables as
diagnostics.

CATMWCSLCQBARBECD9 rejects control, DH, and Epstein monoid-coherent shadows.

CATMWCSLCQBARBECD10 records the live predicate. Only carrier-native
monoidwide square-layer coherence passes.

Therefore the doc-458 square-layer-coherent cartesian-coherent
represented-source-fiber source-typed graph-formation-control-death-natural
graph/Rosati/count-natural pushforward-natural endpoint-degree-natural
DD.4-natural multiplier-action source totalization is still incomplete unless
the same coherence is monoidwide for the carrier-native multiplier action.

## 4. Consequence

The live strict-square branch is now:

```text
construct MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers;
prove C3*C5 = C5*C3 = C15 through the same coherence id;
prove C3*C3*C5 = C45 through the same coherence id;
prove C15 and C45 product naturality with F22;
prove independent multiplier paths use the same square-layer chain;
prove square layers commute monoidwide with DD.4 boundary localization;
prove square layers commute monoidwide with endpoint degree maps;
prove square layers commute monoidwide with p1 and p2 pushforward squares;
prove square layers commute monoidwide with graph, Rosati, and count/degree;
prove square layers commute monoidwide with graph-formation control death;
prove coefficient and signed-support preservation;
prove controls, DH, and Epstein are not coherent points.
```

The open construction target is no longer merely "construct the
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization." It is "construct the monoidwide-square-layer-coherent
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. the totalized source cube;
3. represented multiplier-action functor;
4. identity transport and composition law for that functor;
5. DD.4 boundary localization natural for that functor;
6. endpoint-degree totalization generated by the same internal domain;
7. p1 and p2 pushforward squares generated by that domain;
8. graph composition generated by the pushforward square;
9. graph, Rosati, and count/degree transport naturality;
10. graph-formation control death generated by the graph/Rosati/count layer;
11. source token generated before graph objects exist;
12. represented source formation fiber;
13. actual representing object and universal arrow;
14. cartesian multiplier lifts through the same representer;
15. represented coherence cells generated by the universal arrow;
16. C3*C3=C9 and C3*F22=F22*C3=C3F22 coherence;
17. square-layer coherence for those cells across DD.4 boundary, endpoint
    degree, p1/p2 pushforward, graph, Rosati, count, and control death;
18. monoidwide square-layer coherence across C3, C5, C15, C45, and F22;
19. controls, DH, and Epstein not coherent points;
20. finite-field count, graph-degree, and count-degree anchors as consequences;
21. coefficients and signed support preserved.
```

Until this monoidwide-square-layer-coherent square-layer-coherent
cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization exists, the object remains missing.
