# 354 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling subrepresenter contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-seventeenth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 353 left the strict-square branch live only if the non-split
source-coherence coupling primitive is represented by an actual source-side
object and universal arrow:

```text
    Rep_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source.
```

This document fixes the next edge. A represented coupling object is still not
enough if it is only an abstract equivalent, an isomorphic copy, a Morita
source, a univalence transport, or a completed/replaced object outside the
original source fiber. The missing object must be an actual subrepresenter or
fiber of the represented Qbar_BECD source fiber:

```text
    SubRep_NCoup_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_Qbar_BECD_source_fiber.
```

The inclusion must be monic. The coupling universal arrow must factor through
it. Its image must be exactly the coupled self-dual exact sources. Controls,
DH, and Epstein must be non-points of this subrepresenter before graph
objects exist.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_contract`
(SCSR1-SCSR10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_representability_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_formation_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_formation_gate_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_represented_source_fiber_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_cartesian_coherence_contract`,
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 353, the cheap repair is:

```text
construct any equivalent representer for the source-coupling functor,
transport the universal arrow along an equivalence or univalence path,
then call the transported object the missing source object.
```

That still does not construct the missing object. The square has to act in
the source fiber that doc 342 made represented. If the coupling representer
is external, equivalent only, Morita equivalent, idempotent-split,
localized, saturated, sheafified, stackified, quotient-defined, closure-
defined, base-changed, retuned, or merely classified by a graph object, then
the source fiber has not produced the endpoint-integral DD.4 boundary object.

The live branch therefore narrows from "represented source-coupling object"
to:

```text
construct SubRep_NCoup_Qbar_BECD_source_fiber and
incl_NCoup_to_Rep_Qbar_BECD_source_fiber, prove the inclusion is monic,
prove eta_NCoup factors through it, prove its image is exactly the coupled
self-dual exact sources, and prove controls/DH/Epstein are non-points of this
subrepresenter before graph objects exist.
```

## 2. Lemma

```text
Lemma 354.1 (the coupling representer must be a source subrepresenter).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted source-coupling subrepresenter data are:

    Rep_Qbar_BECD_source_fiber,
    eta_Qbar_BECD_source,
    Rep_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    SubRep_NCoup_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_Qbar_BECD_source_fiber,
    Img_NCoup_coupled_self_dual_exact_sources,
    NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    Coh_Qbar_BECD_BCF_self_dual_exact_source_formation,
    Tok_Qbar_BECD_BCF_self_dual_exact_source,
    Fib_Qbar_BECD_BCF_self_dual_exact_source,
    Ex_Qbar_BECD_CanMod_BCF_dQ,
    Delta_Qbar_BECD_BCF_to_dQ_boundary,
    Ker_Qbar_BECD_BCF_delta_image_z,
    Coim_Qbar_BECD_CanMod_BCF_delta,
    Dual_Qbar_BECD_rank1_boundary_defect,
    BKill_Qbar_BECD_dQ_boundary_properness_self_duality,
    Loc_Qbar_BECD_single_dQ,
    NR_Qbar_BECD_ordered_p1_p2,
    PF_Qbar_BECD_p1p2,
    G_Qbar_BECD_prop,
    R_Qbar_BECD_pos,
    CD_Qbar_BECD,
    CTRL_Qbar_BECD_coherent_death.

The subrepresenter dependency graph contains the live edges:

    Rep_Qbar_BECD_source_fiber -> eta_Qbar_BECD_source,
    Rep_Qbar_BECD_source_fiber -> SubRep_NCoup,
    SubRep_NCoup -> incl_NCoup_to_Rep_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_Qbar_BECD_source_fiber -> Rep_Qbar_BECD_source_fiber,
    SubRep_NCoup -> Rep_NCoup,
    Rep_NCoup -> eta_NCoup,
    eta_NCoup -> NCoup,
    eta_Qbar_BECD_source -> eta_NCoup factors,
    eta_NCoup factors -> incl_NCoup_to_Rep_Qbar_BECD_source_fiber,
    incl_NCoup_to_Rep_Qbar_BECD_source_fiber -> Img_NCoup,
    Img_NCoup -> exact boundary delta,
    exact delta -> exact sequence/kernel/coimage,
    coimage -> rank-one duality,
    duality -> original DD.4 boundary,
    original DD.4 -> normal ratio,
    normal ratio -> endpoint pairing,
    endpoint pairing -> p1 and p2 pushforward,
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
    represented source fiber,
    actual source universal arrow,
    actual coupling representing object,
    actual coupling universal arrow,
    actual coupling subrepresenter/fiber of the source fiber,
    actual monic inclusion into Rep_Qbar_BECD_source_fiber,
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
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_SUBREPRESENTER__ACTUAL_SOURCE_SUBOBJECT_AND_MONIC_INCLUSION__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_subrepresenter_contract`
verifies ten gates.

SCSR1 records the actual source subrepresenter/fiber, monic inclusion, exact
image, H1 profile, strict-square rows, and connected subrepresenter graph.

SCSR2 records again that graph identities do not supply the source
subrepresenter.

SCSR3 rejects external or equivalent representers, univalence transport, and
isomorphic-copy-only repairs.

SCSR4 rejects Morita sources, Karoubi/idempotent splits, localizations,
saturations, sheafifications, and stackifications.

SCSR5 rejects image closures, dense subobjects, quotient predicates, graph
classifiers, and control point-formability.

SCSR6 rejects base-changed subobjects, retuned inclusions, declared
subobjects, and path-dependent subrepresenters.

SCSR7 rejects control/DH/Epstein subobject shadows.

SCSR8 proves every subrepresenter edge is mandatory.

SCSR9 proves only exact source subrepresenters pass.

SCSR10 records the live predicate. The live object is a subrepresenter inside
the represented source fiber, not an equivalent shell.

## 4. Effect on R1

This cycle fixes one more interface in the categorical square:

```text
Rep_NCoup is acceptable only as an actual source subrepresenter/fiber of
Rep_Qbar_BECD_source_fiber, with a monic inclusion and exact coupled image.
```

The open construction target is now:

```text
construct SubRep_NCoup_Qbar_BECD_source_fiber and
incl_NCoup_to_Rep_Qbar_BECD_source_fiber, or kill the strict-square branch at
the subrepresenter interface.
```

No claim here proves R1 or RH. The document only prevents the next
categorical shortcut: replacing source construction by equivalence,
completion, closure, quotienting, base change, retuning, graph classification,
or declaration.

## 5. Acceptance and kill conditions

ACCEPT-SCSR.1 Exhibit `SubRep_NCoup_Qbar_BECD_source_fiber`.

ACCEPT-SCSR.2 Exhibit `incl_NCoup_to_Rep_Qbar_BECD_source_fiber`.

ACCEPT-SCSR.3 Prove the inclusion is monic.

ACCEPT-SCSR.4 Prove
`eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source` factors through the
inclusion.

ACCEPT-SCSR.5 Prove the image is exactly the coupled self-dual exact sources.

ACCEPT-SCSR.6 Prove all C3/C5/C15/C45/F22 paths use the same subrepresenter.

ACCEPT-SCSR.7 Prove controls/DH/Epstein are non-points of the subrepresenter
before graph objects exist.

KILL-SCSR.1 Kill any external or equivalent representer, univalence transport,
isomorphic copy, Morita source, Karoubi/idempotent split, localization,
saturation, sheafification, stackification, image closure, dense subobject,
quotient predicate, base-change subobject, retuned inclusion, graph
classifier, declared subobject, or point-formable control/DH/Epstein repair.
