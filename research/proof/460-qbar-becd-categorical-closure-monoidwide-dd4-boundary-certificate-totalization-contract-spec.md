# 460 - Qbar_BECD categorical closure monoidwide DD.4 boundary-certificate totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-twenty-third cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 459 left the strict-square branch live only through monoidwide
square-layer coherence for the carrier-native multiplier-action functor:

```text
MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers

across C3, C5, C15, C45, F22, and the DD.4/endpoint/pushforward/graph/
Rosati/count/control-death layer chain.
```

This document fixes the next edge. Coherence with the DD.4 boundary label is
not the same as the carrier boundary/properness/self-duality certificate that
kills the original DD.4 class. The monoidwide square-layer coherence must
transport one actual boundary certificate:

```text
BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality

for the original class

c = (1+z)^-1,
res_1(c)=1,
[c] != 0 before the boundary certificate.
```

The DD.4 boundary-certificate datum fixed by this cycle is:

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
monoidwide square-layer coherence: MWC_BCCube_Qbar_BECD_multiplier_monoid_square_layers
original DD.4 class: dd4_c_original_res1_Qbar_BECD
boundary certificate: BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality
localization sequence: Loc_BCCube_Qbar_BECD_single_dQ
normal ratio: NR_BCCube_Qbar_BECD_ordered_p1_p2
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_monoidwide_dd4_boundary_certificate_totalization_contract`
(CATMDCQBARBECD1-CATMDCQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 459 through the DD.4 SCC
interface (153/153 exit 0).

## 1. Purpose

After doc 459, the cheap repair is:

```text
build monoidwide coherence for the multiplier action,
keep a DD.4 boundary id on every row,
and call that the DD.4 killing.
```

That still does not construct the missing object. The original DD.4 class is
not a label; it is the nonzero class detected by `res_1(c)=1` in
`H^1(<phi>;1+zF_2[[z]])=Z/2`. The categorical source square needs a
carrier-native boundary/properness/self-duality map that preserves that
original class as the thing being killed, then maps it to zero through one
`dQ` localization sequence. The same certificate must be transported by the
monoidwide multiplier action.

The live branch narrows from:

```text
monoidwide-square-layer-coherent square-layer-coherent cartesian-coherent
represented source-fiber source-typed graph-formation-control-death-natural
graph/Rosati/count-natural pushforward-natural endpoint-degree-natural
DD.4-natural multiplier-action source totalization
```

to:

```text
monoidwide-DD.4-certificate-carrying monoidwide-square-layer-coherent
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization.
```

## 2. Lemma

```text
Lemma 460.1 (monoidwide coherence must carry the DD.4 killing certificate).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted boundary certificate is:

    BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality,

carried through one localization sequence and one normal ratio:

    Loc_BCCube_Qbar_BECD_single_dQ,
    NR_BCCube_Qbar_BECD_ordered_p1_p2.

The monoidwide multiplier checks remain:

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

Thus monoidwide coherence labels, DD.4 boundary ids, formal nullhomotopies,
coinduced acyclic replacements, deletion, quotient, separate orbit
certificates, local prime certificates, declared connecting maps, declared
localizations, declared self-dual properness, late endpoint/pushforward/graph
filters, numeric equalities, local boundary tables, external 2-cells, retuned
boundary certificates, and control/DH/Epstein shadows do not construct this
certificate.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_monoidwide_dd4_boundary_certificate_totalization_contract`
verifies ten gates.

CATMDCQBARBECD1 records the original nonzero DD.4 class and one carrier
boundary certificate transported through the monoidwide multiplier rows.

CATMDCQBARBECD2 records again that graph identities do not kill the DD.4
class.

CATMDCQBARBECD3 rejects monoidwide coherence labels without the boundary
certificate.

CATMDCQBARBECD4 rejects formal nullhomotopies, deletion, quotient, and
coinduced acyclic replacement because they do not preserve the original class
as the thing being killed.

CATMDCQBARBECD5 rejects separate orbit or local prime certificates.

CATMDCQBARBECD6 rejects declared connecting maps, localizations, and
self-dual properness as labels.

CATMDCQBARBECD7 rejects endpoint, pushforward, and graph filters after the
certificate.

CATMDCQBARBECD8 rejects numeric equality and local boundary tables.

CATMDCQBARBECD9 proves every boundary-certificate edge is mandatory.

CATMDCQBARBECD10 records the live predicate. Only carrier-native monoidwide
DD.4 boundary certificate data passes.

Therefore the doc-459 monoidwide-square-layer-coherent square-layer-coherent
cartesian-coherent represented-source-fiber source-typed graph-formation-
control-death-natural graph/Rosati/count-natural pushforward-natural
endpoint-degree-natural DD.4-natural multiplier-action source totalization is
still incomplete unless the same monoidwide square-layer coherence transports
one carrier-native DD.4 boundary/properness/self-duality certificate killing
the original class.

## 4. Consequence

The live strict-square branch is now:

```text
construct BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality;
prove the original DD.4 class is preserved before the certificate;
prove c is nonzero and res_1(c)=1 before the certificate;
prove one connecting map sends c to zero;
prove one dQ localization sequence carries the certificate;
prove the sequence restricts to p1 and p2 boundary fibers;
prove one ordered normal ratio is the boundary;
prove self-dual properness;
prove the same certificate is transported on all C3/C5/C15/C45/F22 paths;
prove endpoint, pushforward, graph, Rosati, count, and control death are fed
  by that same certificate;
prove controls, DH, and Epstein are not coherent points.
```

The open construction target is no longer merely "construct the monoidwide-
square-layer-coherent square-layer-coherent cartesian-coherent represented
source-fiber source-typed graph-formation-control-death-natural graph/Rosati/
count-natural pushforward-natural endpoint-degree-natural DD.4-natural
multiplier-action source totalization." It is "construct the monoidwide-DD.4-
certificate-carrying monoidwide-square-layer-coherent square-layer-coherent
cartesian-coherent represented source-fiber source-typed graph-formation-
control-death-natural graph/Rosati/count-natural pushforward-natural
endpoint-degree-natural DD.4-natural multiplier-action source totalization."

## 5. Acceptance Target For Any Future Candidate

A future candidate must provide:

```text
1. the represented categorical source square;
2. the totalized source cube;
3. represented multiplier-action functor;
4. identity transport and composition law for that functor;
5. the original nonzero DD.4 class c with res_1(c)=1 before killing;
6. one DD.4 boundary/properness/self-duality certificate;
7. one dQ localization sequence and ordered normal ratio;
8. a connecting map sending c to zero;
9. monoidwide transport of the same certificate across C3, C5, C15, C45, F22;
10. DD.4 boundary localization natural for the multiplier functor;
11. endpoint-degree totalization generated by the same internal domain;
12. p1 and p2 pushforward squares generated by that domain;
13. graph composition generated by the pushforward square;
14. graph, Rosati, and count/degree transport naturality;
15. graph-formation control death generated by the graph/Rosati/count layer;
16. source token generated before graph objects exist;
17. represented source formation fiber;
18. actual representing object and universal arrow;
19. cartesian multiplier lifts through the same representer;
20. represented coherence cells generated by the universal arrow;
21. square-layer and monoidwide square-layer coherence;
22. controls, DH, and Epstein not coherent points;
23. finite-field count, graph-degree, and count-degree anchors as consequences;
24. coefficients and signed support preserved.
```

Until this monoidwide-DD.4-certificate-carrying monoidwide-square-layer-
coherent square-layer-coherent cartesian-coherent represented source-fiber
source-typed graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization exists, the object remains missing.
