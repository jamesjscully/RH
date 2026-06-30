# 468 - Qbar_BECD categorical closure self-dual exact-source coherence-coupling subrepresenter totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-thirty-first cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 467 left the categorical closure branch live only if the non-split
source-coherence coupling primitive is represented by an actual source-side
object and universal arrow:

```text
Rep_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source.
```

This document fixes the next edge. A represented coupling object is still not
enough if it is only an abstract equivalent, an isomorphic copy, a Morita
source, a univalence transport, or a completed/replaced object outside the
original source fiber. The missing object must be an actual subrepresenter or
fiber of the represented categorical Qbar_BECD source fiber:

```text
SubRep_NCoup_BCCube_Qbar_BECD_source_fiber,
incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber.
```

The inclusion must be monic. The coupling universal arrow must factor
through it. Its image must be exactly the coupled self-dual exact sources.
Controls, DH, and Epstein must be non-points of this subrepresenter before
graph objects exist.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_totalization_contract`
(CATSSRBQBARBECD1-CATSSRBQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 467 through the DD.4 SCC
interface (161/161 exit 0).

## 1. Purpose

After doc 467, the cheap repair is:

```text
construct any equivalent representer for the source-coupling functor,
transport the universal arrow along an equivalence or univalence path,
then call the transported object the missing source object.
```

That still does not construct the missing object. The square has to act in
the source fiber that doc 456 made represented. If the coupling representer
is external, equivalent only, Morita equivalent, idempotent-split,
localized, saturated, sheafified, stackified, quotient-defined,
closure-defined, base-changed, retuned, or merely classified by a graph
object, then the source fiber has not produced the endpoint-integral DD.4
boundary object.

The live branch therefore narrows from:

```text
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
Lemma 468.1 (the categorical coupling representer must be a source
subrepresenter).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted source-coupling subrepresenter data are:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle,
    BCCube_CatSq_Qbar_BECD_facets,
    Tot_BCCube_CatSq_Qbar_BECD,
    Act_BCCube_Qbar_BECD_multiplier_functor,
    Rep_BCCube_Qbar_BECD_source_fiber,
    eta_BCCube_Qbar_BECD_source,
    Rep_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    eta_NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    SubRep_NCoup_BCCube_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber,
    Img_NCoup_BCCube_Qbar_BECD_coupled_self_dual_exact_sources,
    NCoup_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Coh_BCCube_Qbar_BECD_BCF_self_dual_exact_source_formation,
    Tok_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Fib_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    ZFib_BCCube_Qbar_BECD_signed_zero,
    CanMod_BCCube_Qbar_BECD_z_boundary_convolution,
    BCF_BCCube_Qbar_BECD_boundary_convolution_module,
    Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary,
    Ker_BCCube_Qbar_BECD_BCF_delta_image_z,
    Coim_BCCube_Qbar_BECD_CanMod_BCF_delta,
    Dual_BCCube_Qbar_BECD_rank1_boundary_defect,
    B_Qbar_BECD_DD4_multiplier_natural,
    NR_BCCube_Qbar_BECD_ordered_p1_p2,
    DegMaps_BCCube_Qbar_BECD_multiplier_endpoint,
    p1_star_Qbar_BECD_endpoint_boundary,
    p2_star_Qbar_BECD_endpoint_boundary,
    PF_Qbar_BECD_p1p2_DD4_endpoint,
    GRCTot_BCCube_Qbar_BECD_pushforward_internal_stratum,
    G_Qbar_BECD_pushforward_prop,
    R_Qbar_BECD_pushforward_positive,
    CD_Qbar_BECD_pushforward,
    Nat_ControlDeath_T_multiplier_BCCube_Qbar_BECD.

The subrepresenter dependency graph contains the live edges:

    represented source square -> Rep_BCCube_Qbar_BECD_source_fiber,
    source cube totalization -> Rep_BCCube_Qbar_BECD_source_fiber,
    Rep_BCCube_Qbar_BECD_source_fiber -> eta_BCCube_Qbar_BECD_source,
    Rep_BCCube_Qbar_BECD_source_fiber -> SubRep_NCoup,
    SubRep_NCoup -> incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber -> Rep_BCCube source fiber,
    SubRep_NCoup -> Rep_NCoup,
    Rep_NCoup -> eta_NCoup,
    eta_NCoup -> NCoup,
    NCoup -> self-dual exact source fiber,
    self-dual exact source fiber -> signed zero fiber,
    signed zero fiber -> cancellation module,
    multiplier action functor -> cancellation module,
    cancellation module -> boundary-convolution module functor,
    boundary-convolution module functor -> exact boundary delta,
    eta_BCCube_Qbar_BECD_source -> eta_NCoup factors,
    eta_NCoup factors -> incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber -> Img_NCoup,
    Img_NCoup -> exact boundary delta,
    exact delta -> kernel -> coimage,
    coimage -> rank-one duality,
    duality -> original DD.4 boundary,
    original DD.4 -> normal ratio,
    normal ratio -> endpoint pairing,
    endpoint pairing -> p1/p2 pushforward,
    pushforward -> graph composition,
    graph composition -> Rosati and count/degree,
    Rosati and count/degree -> control death,
    SubRep_NCoup -> source-before-graph nonpoints.

The exact self-dual subrepresenter rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed subrepresenter checks are equality of full subrepresenter
payloads:

    SubRep(T_C3(T_C5(z)))       = SubRep(T_C15(z)),
    SubRep(T_C5(T_C3(z)))       = SubRep(T_C15(z)),
    SubRep(T_C3(T_C3(T_C5(z)))) = SubRep(T_C45(z)),
    SubRep(T_C15(z*F22))        = SubRep(z*(C15*F22)),
    SubRep(T_C45(z*F22))        = SubRep(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus external representers, equivalent representers, univalence transports,
isomorphic copies, Morita equivalent sources, Karoubi/idempotent splits,
localizations/saturations, sheafifications/stackifications, image closures,
dense subobjects, quotient predicates, base-changed subobjects, retuned
inclusions, graph-object classifiers, declared subobjects, and
control/DH/Epstein point-formability do not construct the source
subrepresenter.

The accepted datum is exactly:

    carrier-native,
    represented categorical source square,
    totalized source cube,
    actual source universal arrow,
    actual coupling representing object,
    actual coupling universal arrow,
    actual coupling subrepresenter/fiber of the source fiber,
    actual monic inclusion into Rep_BCCube_Qbar_BECD_source_fiber,
    eta_NCoup factors through that inclusion,
    image exactly the coupled self-dual exact sources,
    actual source-coherence coupling primitive,
    actual source-coherence cells,
    exact delta in the image,
    original DD.4 in the image,
    controls not points of the subrepresenter,
    DH not points of the subrepresenter,
    Epstein not points of the subrepresenter,
    source before graph objects,
    same subrepresenter on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    required subrepresenter edges present,
    no abstract external representer,
    no equivalent representer,
    no univalence transport,
    no isomorphic copy only,
    no Morita source,
    no Karoubi/idempotent split,
    no localization or saturation,
    no sheafification or stackification,
    no image closure,
    no dense subobject,
    no quotient predicate,
    no base-change subobject,
    no retuned inclusion,
    no graph-object classifier,
    no declared subobject,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_CATEGORICAL_CLOSURE_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER__ACTUAL_SOURCE_SUBOBJECT_AND_MONIC_INCLUSION__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_coherence_coupling_subrepresenter_totalization_contract`
verifies ten gates.

CATSSRBQBARBECD1 records the actual categorical source subrepresenter/fiber,
monic inclusion, exact image, H1 profile, categorical rows, and connected
subrepresenter graph.

CATSSRBQBARBECD2 records again that graph identities do not supply the
source subrepresenter.

CATSSRBQBARBECD3 rejects external or equivalent representers, univalence
transport, and isomorphic-copy-only repairs.

CATSSRBQBARBECD4 rejects Morita sources, Karoubi/idempotent splits,
localizations, saturations, sheafifications, and stackifications.

CATSSRBQBARBECD5 rejects image closures, dense subobjects, quotient
predicates, graph classifiers, and control point-formability.

CATSSRBQBARBECD6 rejects base-changed subobjects, retuned inclusions,
declared subobjects, and path-dependent subrepresenters.

CATSSRBQBARBECD7 rejects control/DH/Epstein subobject shadows.

CATSSRBQBARBECD8 proves every subrepresenter edge is mandatory.

CATSSRBQBARBECD9 proves only exact source subrepresenters pass.

CATSSRBQBARBECD10 records the live predicate. The live object is a
subrepresenter inside the represented categorical source fiber, not an
equivalent shell.

## 4. Impact on R1

```text
R1 after docs 138-468:
  NEWLY FIXED THIS CYCLE:
    - the categorical coupling representer must be an actual subrepresenter
      or fiber of Rep_BCCube_Qbar_BECD_source_fiber with a monic inclusion
      and exact coupled image. Equivalent, completed, closed, quotient, or
      graph-classified representers do not count.

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
      incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber:
        monic inclusion,
        eta_NCoup factors through the inclusion,
        image exactly the coupled self-dual exact sources,
        one subrepresenter on all C3/C5/C15/C45/F22 paths,
        controls/DH/Epstein non-points of the subrepresenter.

  DISCIPLINE:
    - no external/equivalent representer, univalence transport, isomorphic
      copy, Morita source, Karoubi split, localization, saturation,
      sheafification, stackification, image closure, dense subobject,
      quotient predicate, base-change subobject, retuned inclusion, graph
      classifier, or declaration counts.

  STILL OPEN:
    - construct the categorical source subrepresenter and monic inclusion,
      or kill the categorical-closure branch with a named obstruction at this
      subrepresenter interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-CATSSRB.1  Exhibit
                  SubRep_NCoup_BCCube_Qbar_BECD_source_fiber.
ACCEPT-CATSSRB.2  Exhibit
                  incl_NCoup_to_Rep_BCCube_Qbar_BECD_source_fiber.
ACCEPT-CATSSRB.3  Prove the inclusion is monic.
ACCEPT-CATSSRB.4  Prove eta_NCoup factors through the inclusion.
ACCEPT-CATSSRB.5  Prove the image is exactly the coupled self-dual exact
                  sources.
ACCEPT-CATSSRB.6  Prove one subrepresenter transports C3/C5/C15/C45/F22
                  paths through the represented categorical square.
ACCEPT-CATSSRB.7  Prove controls, DH, and Epstein are non-points of the
                  subrepresenter before graph objects exist.

KILL-CATSSRB.1    Reject abstract external representers.
KILL-CATSSRB.2    Reject equivalent representers, univalence transports, and
                  isomorphic copies.
KILL-CATSSRB.3    Reject Morita sources and Karoubi/idempotent splits.
KILL-CATSSRB.4    Reject localizations, saturations, sheafifications, and
                  stackifications.
KILL-CATSSRB.5    Reject image closures, dense subobjects, and quotient
                  predicates.
KILL-CATSSRB.6    Reject base-changed subobjects and retuned inclusions.
KILL-CATSSRB.7    Reject graph-object classifiers and declared subobjects.
KILL-CATSSRB.8    Reject control/DH/Epstein point-formability.
```
