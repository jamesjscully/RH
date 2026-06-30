# 353 - Qbar_BECD strict-square product multiplier self-dual exact-source coherence-coupling representability contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-sixteenth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 352 left the strict-square branch live only if the source-level
coherence object is one non-split coupling primitive:

```text
    NCoup_Qbar_BECD_BCF_self_dual_exact_source.
```

This document fixes the next edge. A non-split connected dependency graph is
still not the missing object. Nor is a nerve, Segal completion, category of
elements, formal universal property, or free categorical completion. The
coupling primitive must be represented by an actual source-side object and
universal arrow:

```text
    Rep_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source.
```

The points of this representer must be exactly the coupled self-dual exact
sources. Controls, DH, and Epstein must be non-points of this representer
before graph objects exist.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_representability_contract`
(SCCR1-SCCR10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
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

After doc 352, the cheap repair is:

```text
draw one connected source-coupling dependency graph,
call it non-split,
then treat its nerve, category of elements, or formal universal property as
the represented source object.
```

That still does not construct the missing object. The graph records what must
be coupled; it is not a carrier-side source object. A functor of points is
valid evidence only after the representing object exists. A formal universal
property without the object and arrow is a label. Free completions or Rezk/
codescent repairs can produce a shell while leaving controls formable.

The live branch therefore narrows from "non-split source-coherence coupling
primitive" to:

```text
construct Rep_NCoup_Qbar_BECD_BCF_self_dual_exact_source and
eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source, prove they represent the
source-coupling functor, and prove their points are exactly the coupled
self-dual exact sources with controls/DH/Epstein excluded as non-points.
```

## 2. Lemma

```text
Lemma 353.1 (the source-coupling primitive must be represented).

The original DD.4 class remains:

    c=(1+z)^-1,
    H^1(<phi>; U_1)=Z/2,
    [c] != 0,
    res_1(c)=1,

in truncations L=6,8,10,12.

The accepted source-coupling representability data are:

    Rep_Qbar_BECD_source_fiber,
    eta_Qbar_BECD_source,
    Rep_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    Tok_Qbar_BECD_BCF_self_dual_exact_source,
    Fib_Qbar_BECD_BCF_self_dual_exact_source,
    Coh_Qbar_BECD_BCF_self_dual_exact_source_formation,
    NCoup_Qbar_BECD_BCF_self_dual_exact_source,
    Cart_Qbar_BECD_BCF_self_dual_exact_source,
    MWC_Qbar_BECD_BCF_self_dual_exact_source,
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

The representability dependency graph contains the live edges:

    eta_Qbar_BECD_source -> Rep_NCoup,
    Rep_NCoup -> eta_NCoup,
    eta_NCoup -> NCoup,
    NCoup -> self-dual exact source token/fiber/coherence,
    NCoup -> exact boundary delta,
    exact delta -> exact sequence/kernel/coimage,
    coimage -> rank-one duality,
    duality -> original DD.4 boundary,
    original DD.4 -> normal ratio,
    normal ratio -> endpoint pairing,
    endpoint pairing -> p1 and p2 pushforward,
    pushforward -> graph composition,
    graph composition -> Rosati and count/degree,
    Rosati and count/degree -> control death,
    Rep_NCoup -> source-before-graph nonpoints.

The exact self-dual represented rows are:

    z                         = {1:2, 2:-1},
    T_C3(z)                   = {3:2, 6:-1},
    T_C5(z)                   = {5:2, 10:-1},
    T_C3(T_C5(z))             = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))       = T_C45(z)              = {45:2, 90:-1},
    z*F22                     = {2:4, 4:-2},
    T_C15(z*F22)              = z*(C15*F22)           = {30:4, 60:-2},
    T_C45(z*F22)              = z*(C45*F22)           = {90:4, 180:-2}.

The mixed representability checks are equality of full representability
payloads:

    Rep(T_C3(T_C5(z)))       = Rep(T_C15(z)),
    Rep(T_C5(T_C3(z)))       = Rep(T_C15(z)),
    Rep(T_C3(T_C3(T_C5(z)))) = Rep(T_C45(z)),
    Rep(T_C15(z*F22))        = Rep(z*(C15*F22)),
    Rep(T_C45(z*F22))        = Rep(z*(C45*F22)).

The graph/Rosati/count diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus connected dependency graphs, nerves, Segal completions, functor-of-
points wrappers, Yoneda reversal, Grothendieck constructions, categories of
elements, formal universal properties, limit cones, comma categories, free
operad completions, collages, proarrow equipment, codescent/descent labels,
Rezk completions, local representer tables, external or retuned
representers, products or pullbacks of representers, graph-object
classifiers, semantic zeta labels, declared representers, and
control/DH/Epstein point-formability do not construct the representer.

The accepted datum is exactly:

    carrier-native,
    represented source fiber,
    actual source universal arrow,
    actual coupling representing object,
    actual coupling universal arrow,
    coupling functor represented,
    actual source-coherence coupling primitive,
    coupling generated by the representer,
    representer points exactly the coupled sources,
    actual source-coherence cells,
    exact delta coupled,
    kernel/coimage coupled,
    rank-one duality coupled,
    original DD.4 coupled,
    normal ratio coupled,
    endpoint/pushforward coupled,
    graph/Rosati/count coupled,
    control death coupled,
    source before graph objects,
    non-split dependency graph,
    same representer on all paths,
    actual C3*C5=C15 source coherence,
    actual C5*C3=C15 source coherence,
    actual C3*C3*C5=C45 source coherence,
    actual F22 product source coherence,
    finite anchors generated,
    controls not points of the representer,
    DH not points of the representer,
    Epstein not points of the representer,
    required coupling-representability edges present,
    no connected dependency graph only,
    no nerve or Segal completion,
    no functor of points without representer,
    no Yoneda reversal,
    no Grothendieck construction or category of elements only,
    no formal universal property,
    no limit cone or comma category label,
    no free operad completion,
    no collage or proarrow equipment,
    no codescent/descent label,
    no Rezk completion,
    no local representer table,
    no external choice or retuned representer,
    no product or pullback of representers,
    no graph-object classifier,
    no semantic zeta label,
    no declared representer,
    no control/DH/Epstein point-formability.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_SELF_DUAL_EXACT_SOURCE_COHERENCE_COUPLING_REPRESENTABILITY__ACTUAL_SOURCE_REP_AND_ARROW__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_self_dual_exact_source_coherence_coupling_representability_contract`
verifies ten gates.

SCCR1 records the actual source-coupling representing object and universal
arrow, H1 profile, strict-square rows, representability-payload equalities,
and connected representability graph.

SCCR2 records again that graph identities do not supply the coupling
representer.

SCCR3 rejects connected dependency graphs, nerves, and Segal completions.

SCCR4 rejects functors of points, Yoneda reversal, Grothendieck
constructions, and categories of elements without a representer.

SCCR5 rejects formal universal properties, limit cones, comma categories,
and declared representers.

SCCR6 rejects free operad, collage/proarrow, codescent, and Rezk completions.

SCCR7 rejects local representer tables, external choices, and retunings.

SCCR8 rejects products/pullbacks of representers and graph classifiers.

SCCR9 proves every coupling-representability edge is mandatory.

SCCR10 records the live predicate. Only represented source-coupling objects
pass.

## 4. Impact on R1

```text
R1 after docs 138-353:
  NEWLY FIXED THIS CYCLE:
    - the non-split source-coherence coupling primitive must be represented
      by an actual source-side object and universal arrow. A connected
      dependency graph or formal universal-property shell is not enough.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct the signed zero fiber and universal arrow;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the exact BCF boundary-delta source;
    - construct the rank-one self-dual boundary-defect map inside that source;
    - construct the represented self-dual exact-source formation fiber;
    - construct source-level formation-coherence cells generated by the same
      universal arrow;
    - construct the non-split source-coherence coupling primitive;
    - construct Rep_NCoup and eta_NCoup representing that coupling primitive:
        points exactly the coupled self-dual exact sources,
        one representer on all C3/C5/C15/C45/F22 paths,
        controls/DH/Epstein non-points of the representer.

  DISCIPLINE:
    - no dependency graph, nerve, Segal completion, functor of points, Yoneda
      reversal, Grothendieck/category-of-elements wrapper, formal universal
      property, limit cone, free completion, local representer table, product
      representer, graph classifier, semantic label, or declaration counts.

  STILL OPEN:
    - construct the represented source-coupling object and universal arrow,
      or kill the strict-square branch with a named obstruction at this
      representability interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-SCCR.1  Exhibit Rep_NCoup_Qbar_BECD_BCF_self_dual_exact_source.
ACCEPT-SCCR.2  Exhibit eta_NCoup_Qbar_BECD_BCF_self_dual_exact_source.
ACCEPT-SCCR.3  Prove eta_NCoup generates NCoup from eta_Qbar_BECD_source.
ACCEPT-SCCR.4  Prove the represented points are exactly the coupled
               self-dual exact sources.
ACCEPT-SCCR.5  Prove one representer transports C3/C5/C15/C45/F22 paths.
ACCEPT-SCCR.6  Prove exact/DD.4/duality/endpoint/graph/Rosati/count/control
               data are coupled through the representer.
ACCEPT-SCCR.7  Prove controls, DH, and Epstein are non-points of the
               representer before graph objects exist.

KILL-SCCR.1    Reject connected dependency graphs, nerves, and Segal
               completions.
KILL-SCCR.2    Reject functor-of-points and Yoneda wrappers without a
               representer.
KILL-SCCR.3    Reject Grothendieck constructions and categories of elements.
KILL-SCCR.4    Reject formal universal properties, limit cones, and comma
               category labels.
KILL-SCCR.5    Reject free completions, collages, proarrow equipment,
               codescent labels, and Rezk completions.
KILL-SCCR.6    Reject local representer tables.
KILL-SCCR.7    Reject external choices and retuned representers.
KILL-SCCR.8    Reject products or pullbacks of representers.
KILL-SCCR.9    Reject graph-object classifiers and semantic labels.
KILL-SCCR.10   Reject control/DH/Epstein point-formability.
```
