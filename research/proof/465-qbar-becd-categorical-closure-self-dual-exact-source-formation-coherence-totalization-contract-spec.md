# 465 - Qbar_BECD categorical closure self-dual exact-source formation-coherence totalization contract

Status: construction-spec refinement anchor, 2026-06-23.
Three-hundred-twenty-eighth cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 464 left the categorical closure branch live only if the self-dual exact
BCF source is a represented source-level formation fiber before graph objects
exist:

```text
Tok_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
Fib_BCCube_Qbar_BECD_BCF_self_dual_exact_source.
```

This document fixes the next edge. The formation fiber cannot be assembled
row-by-row with a common token, finite equalities, or declared 2-cells. The
same universal arrow must generate source-level coherence cells for the
self-dual exact source:

```text
Coh_BCCube_Qbar_BECD_BCF_self_dual_exact_source_formation,
Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
MWC_BCCube_Qbar_BECD_BCF_self_dual_exact_source.
```

Those coherence cells must preserve the exact BCF delta, kernel, coimage,
rank-one duality, pinned twist, original DD.4 boundary class, normal ratio,
endpoint/pushforward/graph/Rosati/count chain, and source-level control death
across `C3`, `C5`, `C15`, `C45`, and `F22`.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_formation_coherence_totalization_contract`
(CATSFCQBARBECD1-CATSFCQBARBECD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle: from doc 464 through the DD.4 SCC
interface (158/158 exit 0).

## 1. Purpose

After doc 464, the cheap repair is:

```text
construct the self-dual exact-source token/fiber,
verify the C3/C5/C15/C45/F22 rows are numerically equal where expected,
then declare coherence cells or identify the rows by a finite table.
```

That still does not construct the missing object. Same row values do not say
that the represented source formation object generated the identifications. A
declared square or a post-hoc graph coherence can still let controls, DH, or
Epstein become graph-shaped shadows before the source kills them.

The live branch therefore narrows from:

```text
formation-gated-self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
self-dual-exact-BCF-source-generated-DD.4-certificate-carrying
exact-natural-BCF-generated-DD.4-certificate-carrying
cancellation-module-generated-DD.4-certificate-carrying
monoidwide-DD.4-certificate-carrying monoidwide-square-layer-coherent
square-layer-coherent cartesian-coherent represented source-fiber source-typed
graph-formation-control-death-natural graph/Rosati/count-natural
pushforward-natural endpoint-degree-natural DD.4-natural multiplier-action
source totalization
```

to:

```text
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
Lemma 465.1 (categorical self-dual exact source requires generated formation
coherence).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted formation-coherence data are:

    CatSq_Qbar_BECD_closes_doc443_boundary_cycle,
    BCCube_CatSq_Qbar_BECD_facets,
    Tot_BCCube_CatSq_Qbar_BECD,
    Rep_BCCube_Qbar_BECD_source_fiber,
    eta_BCCube_Qbar_BECD_source,
    Tok_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Fib_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    Coh_BCCube_Qbar_BECD_BCF_self_dual_exact_source_formation,
    Cart_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    MWC_BCCube_Qbar_BECD_BCF_self_dual_exact_source,
    ZFib_BCCube_Qbar_BECD_signed_zero,
    CanMod_BCCube_Qbar_BECD_z_boundary_convolution,
    BCF_BCCube_Qbar_BECD_boundary_convolution_module,
    Ex_BCCube_Qbar_BECD_CanMod_BCF_dQ,
    Delta_BCCube_Qbar_BECD_BCF_to_dQ_boundary,
    Ker_BCCube_Qbar_BECD_BCF_delta_image_z,
    Coim_BCCube_Qbar_BECD_CanMod_BCF_delta,
    Dual_BCCube_Qbar_BECD_rank1_boundary_defect,
    Tw_BCCube_Qbar_BECD_OC_BCF_pinned,
    BKill_BCCube_Qbar_BECD_dQ_boundary_properness_self_duality,
    Loc_BCCube_Qbar_BECD_single_dQ,
    NR_BCCube_Qbar_BECD_ordered_p1_p2.

The exact self-dual coherent source rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed coherence checks are equality of full source-coherence payloads:

    Coh(T_C3(T_C5(z)))        = Coh(T_C15(z)),
    Coh(T_C5(T_C3(z)))        = Coh(T_C15(z)),
    Coh(T_C3(T_C3(T_C5(z))))  = Coh(T_C45(z)),
    Coh(T_C15(z*F22))         = Coh(z*(C15*F22)),
    Coh(T_C45(z*F22))         = Coh(z*(C45*F22)).

Each coherence payload contains the same categorical source square, totalized
cube, source token, source fiber, universal arrow, exact delta, kernel,
coimage, rank-one duality, pinned twist, original DD.4 class, normal ratio,
endpoint pair, pushforward chain, Rosati/count chain, and source-level
control-death id.

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus same-token assertions, finite row equalities, degree/count/support/
weighted-zero arguments, declared 2-cells, formal commutative squares, finite
composition tables, local C3 patches, single-prime axes, prime-axis tags,
external choices of 2-cells, retuned source coherences, graph-object
coherence, graph predicates, late control filters, boundary/DD.4 after-
filters, functors of points without representers, semantic zeta labels, and
control/DH/Epstein coherent graph shadows do not construct source coherence.

The accepted datum is exactly:

    carrier-native,
    represented categorical source square,
    totalized source cube,
    represented source fiber,
    actual universal arrow,
    actual self-dual exact source token,
    actual self-dual exact source fiber,
    source before graph objects,
    actual source-coherence cells,
    source coherence generated by the universal arrow,
    actual cartesian source coherence,
    actual monoidwide source coherence,
    same coherence id on all multiplier paths,
    coherence preserves exact delta,
    coherence preserves kernel,
    coherence preserves coimage,
    coherence preserves signed coefficients,
    coherence preserves rank-one duality,
    coherence preserves pinned twist,
    coherence preserves original DD.4 class,
    coherence preserves normal ratio,
    coherence preserves endpoint pairing,
    coherence preserves endpoint/pushforward/graph,
    coherence preserves Rosati/count,
    coherence preserves source-level control death,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    controls, DH, and Epstein not points,
    required self-dual source-coherence edges present,
    no same-token-without-coherence argument,
    no declared 2-cells,
    no formal commutative square,
    no finite composition table,
    no local C3 patch,
    no single-prime-axis patch,
    no prime-axis tags,
    no degree/count/support/weighted-zero-only argument,
    no external choice of 2-cells,
    no retuned source coherence,
    no graph-object coherence,
    no graph predicate gate,
    no late control filter,
    no boundary/DD.4 after-filter,
    no functor of points without representer,
    no semantic zeta label,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_CATEGORICAL_CLOSURE_SELF_DUAL_EXACT_SOURCE_FORMATION_COHERENCE__UNIVERSAL_ARROW_GENERATED_SOURCE_2CELLS__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_categorical_closure_self_dual_exact_source_formation_coherence_totalization_contract`
verifies ten gates.

CATSFCQBARBECD1 records the universal-arrow-generated self-dual exact-source
coherence, H1 profile, categorical rows, source-coherence payload equalities,
and source-before-graph nonpoint status.

CATSFCQBARBECD2 records again that graph identities do not supply source
coherence.

CATSFCQBARBECD3 rejects same tokens and finite equalities as substitutes for
coherence.

CATSFCQBARBECD4 rejects local C3 patches, single-prime axes, and prime-axis
tags.

CATSFCQBARBECD5 rejects declared 2-cells, formal squares, and finite
composition tables.

CATSFCQBARBECD6 rejects external choices, retuned coherences, and semantic
labels.

CATSFCQBARBECD7 rejects graph predicates and late boundary/DD.4/control
filters.

CATSFCQBARBECD8 proves every source-coherence edge is mandatory.

CATSFCQBARBECD9 rejects control, DH, and Epstein coherent graph shadows.

CATSFCQBARBECD10 records the live predicate. Only universal-arrow-generated
self-dual source coherence passes.

## 4. Impact on R1

```text
R1 after docs 138-465:
  NEWLY FIXED THIS CYCLE:
    - the categorical self-dual exact-source formation fiber must carry
      represented source-level coherence cells generated by the same universal
      arrow. The coherence must be cartesian and monoidwide across C3, C5,
      C15, C45, and F22, and must preserve the exact BCF/DD.4/duality/
      control-death chain before graph objects exist.

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
    - construct the represented self-dual exact-source formation fiber:
        source token generated by universal arrow,
        source fiber before graph objects,
        control/DH/Epstein non-points at source formation,
        exact BCF delta and DD.4 killing inside the source,
        endpoint/pushforward/graph/Rosati/count generated from the source;
    - construct source-level formation-coherence cells generated by the same
      universal arrow:
        C3*C5=C15,
        C5*C3=C15,
        C3*C3*C5=C45,
        F22 product naturality,
        preservation of exact delta/kernel/coimage,
        preservation of rank-one duality/pinned twist/original DD.4,
        preservation of normal ratio and endpoint pairing,
        preservation of endpoint/pushforward/graph/Rosati/count/control death.

  DISCIPLINE:
    - no same-token equality, finite table, declared 2-cell, formal square,
      local C3 patch, prime-axis tag, external choice, retuned coherence,
      graph predicate, late filter, or graph-object coherence counts.

  STILL OPEN:
    - construct the categorical represented self-dual exact-source
      formation-coherence object, or kill the categorical closure branch with
      a named obstruction at this source-coherence interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-CATSFC.1  Exhibit the represented self-dual exact-source token and
                 fiber.
ACCEPT-CATSFC.2  Exhibit source-coherence cells generated by the universal
                 arrow.
ACCEPT-CATSFC.3  Prove the source coherence exists before graph objects.
ACCEPT-CATSFC.4  Prove actual cartesian and monoidwide source coherence.
ACCEPT-CATSFC.5  Prove C3*C5=C15, C5*C3=C15, C3*C3*C5=C45, and F22 product
                 source coherence.
ACCEPT-CATSFC.6  Prove coherence preserves exact delta, kernel, coimage,
                 signed coefficients, rank-one duality, pinned twist,
                 original DD.4, normal ratio, endpoint pairing,
                 graph/Rosati/count, and source-level control death.
ACCEPT-CATSFC.7  Prove controls, DH, and Epstein are non-points through the
                 source-coherence object.

KILL-CATSFC.1    Reject same-token and finite-equality substitutes.
KILL-CATSFC.2    Reject declared 2-cells and formal commutative squares.
KILL-CATSFC.3    Reject finite composition tables.
KILL-CATSFC.4    Reject local C3 patches, single-prime axes, and prime-axis
                 tags.
KILL-CATSFC.5    Reject external choices of 2-cells.
KILL-CATSFC.6    Reject retuned source coherences.
KILL-CATSFC.7    Reject graph-object coherence and graph predicate gates.
KILL-CATSFC.8    Reject late control, boundary, and DD.4 filters.
KILL-CATSFC.9    Reject functors of points without representers and semantic
                 zeta labels.
KILL-CATSFC.10   Reject control/DH/Epstein point-formability.
```
