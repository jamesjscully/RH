# 469 - Qbar_BECD categorical closure self-dual exact-source coherence-coupling subrepresenter finite-limit totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-thirty-second cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 468 left the categorical closure branch live only if the source-coupling
representer is an actual subrepresenter/fiber of the represented categorical
source fiber:

```text
SubRep_NCoup_BCCube_Qbar_BECD_source_fiber,
incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber,
Img_NCoup_BCCube_Qbar_BECD_coupled_self_dual_exact_sources.
```

This document fixes the next edge. A source subrepresenter is still not the
missing object if it is certified only by a pointwise exact-image predicate,
a characteristic map into a subobject classifier, a sequential intersection
of filters, a local row table, or a late pullback after graph objects exist.
The subrepresenter must be produced internally by one finite-limit/equalizer
fork in the represented source fiber:

```text
LimCut_NCoup_BCCube_Qbar_BECD_source_fiber,
Fork_BCCube_endpoint_dd4_rosati_control_NCoup,
eq_NCoup_constraints_to_SubRep_BCCube_Qbar_BECD_source_fiber.
```

That fork must impose endpoint integrality, degree maps, the original DD.4
boundary, boundary pushforward, graph composition, Rosati/count, and control
death simultaneously, before points and graph objects exist.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_finite_limit_totalization_contract`
(CATSFLQBARBECD1-CATSFLQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 468 through the DD.4 SCC
interface (162/162 exit 0).

## 1. Purpose

After doc 468, the cheap repair is:

```text
name a subrepresenter whose points are exactly the coupled sources,
prove the pointwise image has the desired finite rows,
then use graph/Rosati/DD.4 filters to remove controls after the fact.
```

That still does not construct the missing object. The square must make the
source fiber cut out the subrepresenter internally. The cut must be a single
finite-limit/equalizer fork, not an intersection of separately checked
predicates. The fork must carry the endpoint, degree, DD.4, pushforward,
graph, Rosati/count, and control-death constraints together. If any one of
those constraints is added later, controls can be formed before the square
kills them.

The live branch therefore narrows from:

```text
subrepresented-coupled-formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
represented-coupled-formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
coupled-formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
exact-natural-BCF-generated-DD.4-certificate-carrying
cancellation-module-generated-DD.4-certificate-carrying
monoidwide-DD.4-certificate-carrying monoidwide-square-layer-coherent
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization.
```

to:

```text
finite-limit-subrepresented-coupled-formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
subrepresented-coupled-formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
represented-coupled-formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
coupled-formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
formation-coherent-formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
exact-natural-BCF-generated-DD.4-certificate-carrying
cancellation-module-generated-DD.4-certificate-carrying
monoidwide-DD.4-certificate-carrying monoidwide-square-layer-coherent
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization.
```

## 2. Lemma

```text
Lemma 469.1 (the categorical source subrepresenter must be an internal
finite-limit cut).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted finite-limit subrepresenter data are:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle,
    BCCube_CatSq_Qbar_BECD_facets,
    Tot_BCCube_CatSq_Qbar_BECD,
    Act_BCCube_Qbar_BECD_multiplier_functor,
    Rep_BCCube_Qbar_BECD_source_fiber,
    eta_BCCube_Qbar_BECD_source,
    SubRep_NCoup_BCCube_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber,
    Img_NCoup_BCCube_Qbar_BECD_coupled_self_dual_exact_sources,
    LimCut_NCoup_BCCube_Qbar_BECD_source_fiber,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup,
    eq_NCoup_constraints_to_SubRep_BCCube_Qbar_BECD_source_fiber,
    NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    ZFib_BCCube_Qbar_BECD_signed_zero,
    CanMod_BCCube_Qbar_BECD_z_boundary_convolution,
    BCF_BCCube_Qbar_BECD_boundary_convolution_module,
    Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary,
    dd4_c_original_res1_Qbar_BECD,
    NR_BCCube_Qbar_BECD_ordered_p1_p2,
    DegMaps_BCCube_Qbar_BECD_multiplier_endpoint,
    p1_star_Qbar_BECD_endpoint_boundary,
    p2_star_Qbar_BECD_endpoint_boundary,
    PF_Qbar_BECD_p1p2_DD4_endpoint,
    G_Qbar_BECD_pushforward_prop,
    R_Qbar_BECD_pushforward_positive,
    CD_Qbar_BECD_pushforward,
    Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD.

The finite-limit dependency graph contains the live edges:

    represented source square -> Rep_BCCube_Qbar_BECD_source_fiber,
    source cube totalization -> Rep_BCCube_Qbar_BECD_source_fiber,
    Rep_BCCube_Qbar_BECD_source_fiber -> LimCut_NCoup,
    eta_BCCube_Qbar_BECD_source -> LimCut_NCoup,
    LimCut_NCoup -> Fork_BCCube_endpoint_dd4_rosati_control_NCoup,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup -> endpoint integrality,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup -> degree maps,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup -> DD.4 boundary,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup -> boundary pushforward,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup -> graph composition,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup -> Rosati/count,
    Fork_BCCube_endpoint_dd4_rosati_control_NCoup -> control death,
    LimCut_NCoup -> eq_NCoup_constraints_to_SubRep,
    eq_NCoup_constraints_to_SubRep -> SubRep_NCoup,
    eq_NCoup_constraints_to_SubRep -> incl_NCoup_to_Rep_BCCube source fiber,
    eq_NCoup_constraints_to_SubRep -> Img_NCoup,
    eq_NCoup_constraints_to_SubRep -> monic equalizer arrow,
    monic equalizer arrow -> exact subrepresenter image,
    exact subrepresenter image -> coupled self-dual exact sources,
    coupled self-dual exact sources -> NCoup,
    NCoup -> signed zero fiber,
    signed zero fiber -> cancellation module,
    multiplier action functor -> cancellation module,
    cancellation module -> boundary-convolution module functor,
    boundary-convolution module functor -> exact boundary delta,
    NCoup -> exact boundary delta,
    exact boundary delta -> original DD.4 boundary,
    original DD.4 boundary -> normal ratio,
    normal ratio -> endpoint pushforward,
    endpoint pushforward -> graph composition,
    graph composition -> Rosati/count,
    Rosati/count -> control death,
    LimCut_NCoup -> universal property,
    universal property -> same cut on all paths,
    same cut on all paths -> C3*C5=C15,
    same cut on all paths -> C5*C3=C15,
    same cut on all paths -> C3*C3*C5=C45,
    same cut on all paths -> F22 product,
    LimCut_NCoup -> source before points and graph objects,
    source before points and graph objects -> controls not points,
    source before points and graph objects -> DH not points,
    source before points and graph objects -> Epstein not points.

The exact self-dual finite-limit rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed finite-limit checks are equality of full finite-limit cut payloads:

    LimCut(T_C3(T_C5(z)))       = LimCut(T_C15(z)),
    LimCut(T_C5(T_C3(z)))       = LimCut(T_C15(z)),
    LimCut(T_C3(T_C3(T_C5(z)))) = LimCut(T_C45(z)),
    LimCut(T_C15(z*F22))        = LimCut(z*(C15*F22)),
    LimCut(T_C45(z*F22))        = LimCut(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus pointwise image certificates, predicate subobject selections, subobject
classifiers, characteristic-map-only repairs, sequential intersections,
iterated filters, post-hoc image factorizations, external finite-limit
completions, pullbacks after graph objects, local row tables, finite-sample
cuts, basis-dependent cuts, retuned/projected constraints,
graph-invariant classifiers, declared equalizers, and control/DH/Epstein
point-formability do not construct the finite-limit source cut.

The accepted datum is exactly:

    carrier-native,
    represented categorical source square,
    totalized source cube,
    represented source fiber,
    actual categorical source universal arrow,
    actual coupling subrepresenter,
    actual finite-limit cut,
    actual joint constraint fork,
    actual equalizer arrow,
    monic equalizer arrow,
    commuting fork,
    actual universal property,
    cut before points,
    cut before graph objects,
    image is the doc-468 subrepresenter,
    constraints in one fork,
    endpoint integrality in the fork,
    degree maps in the fork,
    DD.4 boundary in the fork,
    boundary pushforward in the fork,
    graph composition in the fork,
    Rosati/count in the fork,
    control death in the fork,
    same cut on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    controls not points,
    DH not points,
    Epstein not points,
    required finite-limit edges present,
    no pointwise image certificate,
    no predicate subobject selection,
    no subobject classifier,
    no characteristic map only,
    no sequential intersection,
    no iterated filters,
    no post-hoc image factorization,
    no external finite-limit completion,
    no pullback after graph objects,
    no local row table,
    no finite-sample cut,
    no basis-dependent cut,
    no retuned/projected constraint,
    no graph-invariant classifier,
    no declared equalizer,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_CATEGORICAL_CLOSURE_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER_FINITE_LIMIT__SIMULTANEOUS_SOURCE_EQUALIZER_CUT__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_finite_limit_totalization_contract`
verifies ten gates.

CATSFLQBARBECD1 records the categorical source finite-limit/equalizer fork,
H1 profile, categorical rows, finite-limit-payload equalities, and connected
cut graph.

CATSFLQBARBECD2 records again that graph identities do not supply the
finite-limit cut.

CATSFLQBARBECD3 rejects pointwise exact-image predicates, predicate
subobject selection, subobject classifiers, and characteristic-map-only
repairs.

CATSFLQBARBECD4 rejects sequential intersections, iterated filters, and
post-hoc image factorizations.

CATSFLQBARBECD5 rejects external finite-limit completions and pullbacks
after graph objects.

CATSFLQBARBECD6 rejects local row tables, finite-sample cuts, basis-dependent
cuts, and retuned/projected constraints.

CATSFLQBARBECD7 rejects graph/Rosati/DD.4 after-filters that leave controls,
DH, and Epstein formable.

CATSFLQBARBECD8 proves every finite-limit cut edge is mandatory.

CATSFLQBARBECD9 proves only simultaneous source finite-limit cuts pass.

CATSFLQBARBECD10 records the live predicate. The live cut is internal, not a
predicate shell.

## 4. Impact on R1

```text
R1 after docs 138-469:
  NEWLY FIXED THIS CYCLE:
    - the categorical source-coupling subrepresenter must be produced by a
      carrier-native finite-limit/equalizer fork inside
      Rep_BCCube_Qbar_BECD_source_fiber. Endpoint integrality, degree maps,
      original DD.4, boundary pushforward, graph composition, Rosati/count,
      and control death must be imposed simultaneously before points and
      graph objects exist.

  CURRENT LIVE TARGET ON THE CATEGORICAL-CLOSURE BRANCH:
    - construct the represented categorical source square and totalized
      Beck-Chevalley cube;
    - construct the represented multiplier-action functor and internal
      effectivity domain;
    - construct the signed zero fiber and universal arrow;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the exact BCF boundary-delta source;
    - construct the rank-one self-dual boundary-defect map inside that source;
    - construct the represented self-dual exact-source formation fiber;
    - construct source-level formation-coherence cells generated by the same
      universal arrow;
    - construct the non-split source-coherence coupling primitive;
    - construct Rep_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source and
      eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source;
    - construct SubRep_NCoup_BCCube_Qbar_BECD_source_fiber and
      incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber;
    - construct LimCut_NCoup_BCCube_Qbar_BECD_source_fiber,
      Fork_BCCube_endpoint_dd4_rosati_control_NCoup, and
      eq_NCoup_constraints_to_SubRep_BCCube_Qbar_BECD_source_fiber:
        one finite-limit/equalizer fork,
        monic equalizer arrow,
        image exactly the doc-468 subrepresenter,
        all endpoint/DD.4/pushforward/graph/Rosati/count/control constraints
        imposed together,
        controls/DH/Epstein non-points before graph objects.

  DISCIPLINE:
    - no pointwise image certificate, predicate selection, subobject
      classifier, characteristic map, sequential intersection, iterated
      filter, post-hoc image factorization, external finite-limit completion,
      late pullback, local row table, finite sample, basis-dependent cut,
      retuned/projected constraint, graph-invariant classifier, or declared
      equalizer counts.

  STILL OPEN:
    - construct the categorical finite-limit source cut and equalizer fork,
      or kill the categorical-closure branch with a named obstruction at this
      finite-limit interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-CATSFL.1  Exhibit
                 LimCut_NCoup_BCCube_Qbar_BECD_source_fiber.
ACCEPT-CATSFL.2  Exhibit
                 Fork_BCCube_endpoint_dd4_rosati_control_NCoup.
ACCEPT-CATSFL.3  Exhibit
                 eq_NCoup_constraints_to_SubRep_BCCube_Qbar_BECD_source_fiber.
ACCEPT-CATSFL.4  Prove the equalizer arrow is monic and its image is the
                 doc-468 subrepresenter.
ACCEPT-CATSFL.5  Prove endpoint, degree, DD.4, pushforward, graph,
                 Rosati/count, and control-death constraints are imposed in
                 one fork.
ACCEPT-CATSFL.6  Prove one cut transports C3/C5/C15/C45/F22 paths through
                 the represented categorical square.
ACCEPT-CATSFL.7  Prove controls, DH, and Epstein are non-points before
                 graph objects exist.

KILL-CATSFL.1    Reject pointwise image certificates and predicate subobject
                 selections.
KILL-CATSFL.2    Reject subobject classifiers and characteristic-map-only
                 repairs.
KILL-CATSFL.3    Reject sequential intersections and iterated filters.
KILL-CATSFL.4    Reject post-hoc image factorizations.
KILL-CATSFL.5    Reject external finite-limit completions and pullbacks after
                 graph objects.
KILL-CATSFL.6    Reject local row tables, finite-sample cuts, and
                 basis-dependent cuts.
KILL-CATSFL.7    Reject retuned/projected constraints and graph-invariant
                 classifiers.
KILL-CATSFL.8    Reject declared equalizers.
KILL-CATSFL.9    Reject control/DH/Epstein point-formability.
```
