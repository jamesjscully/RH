# 578 - Qbar_BECD exact-24 admissible source-square Beck-Chevalley evaluation contract

Status: construction-spec refinement anchor, 2026-06-28.
Four-hundred-forty-first cycle of the doc-137 construction arc. This is
not a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 577 required the represented semantic model to have a source-internal
natural evaluation commuting with executable normal forms, refinements,
composition, and payload projections. The next cheap escape is vertical
naturality without base-change: the evaluation commutes projectionwise, but
pull-then-evaluate and evaluate-then-push do not agree across the existing
cartesian source square.

This document requires a named Beck-Chevalley exact-evaluation certificate:

```text
BeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidCartCompatDiagRepLimSrcBundleRepLimFiltCofRefCalcStabRefDescStabMedGenCompStabJointSourceLawDD4ActiveRigidPrimEffK0Lift_BaseChange_source_square.
```

The certificate is charged to the existing exact-24 finite-index budget. It
adds no new source square, no new base-change cell, no external model, no
quotient carrier, no functor-of-points or Yoneda reversal, no pointwise or
objectwise base-change selector, no finite sample, no basis row, no
declaration-only base-change, and no context collapse. The natural evaluation
must be exact/cartesian over the already represented source-square
compatibility diagram and satisfy Beck-Chevalley pull-push commutation and
projection formula for the boundary, DD.4, exact-delta, graph, Rosati,
control, and handoff routes.

Witness:
`prime_int_n1b_qbar_becd_fidx24_probe_beck_chevalley_evaluation_natural_represented_semantic_model_contract`
(CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM10 ALL PASS, lead-ran exit 0).
Adjacent Qbar_BECD witnesses plus the DD.4 SCC interface: 271/271 exit 0,
lead-ran.
Frontier-map check with current witness: passed at current_doc=578
(atoms=76, edges=755).

## 1. Purpose

The cheap repair after doc 577 is:

```text
the represented semantic model evaluates naturally, but base-change is not
exact/cartesian: evaluating after pullback and pushing after evaluation do not
agree on the source-square routes.
```

That repair still fails to find the missing object. Projectionwise naturality
can leave the square as a list of compatible shadows. The missing object needs
the evaluation itself to be a base-change operation of the source square:
boundary-pushforward must agree with DD.4/exact-delta, graph-composition must
agree with Rosati/control, handoff must agree with later graph realization,
and endpoint/degree projections must satisfy the same projection formula.

## 2. Lemma

```text
Lemma 578.1 (natural evaluation must satisfy Beck-Chevalley).

The admissible source-square category is accepted only if the doc-577 natural
evaluation of the represented semantic model satisfies exact/cartesian
Beck-Chevalley base-change over the existing source-square compatibility
diagram.

The Beck-Chevalley evaluation certificate must provide:

    exact/cartesian base-change over the represented source-square diagram,
    pull-then-evaluate equals evaluate-then-push,
    projection formula for endpoint integrality and degree maps,
    DD.4 boundary/base-change compatibility,
    boundary-pushforward compatibility,
    DD.4/exact-delta base-change compatibility,
    graph-composition base-change compatibility,
    Rosati/control base-change compatibility,
    handoff/graph-later base-change compatibility,
    source-before-points preservation,
    original-H1 and doc515 payload preservation,
    subrepresenter-internal base-change,
    universal-arrow selected base-change,
    exact-24 finite-index budget preservation,
    no external or quotient base-change,
    no functor-of-points or Yoneda-reversal base-change,
    no pointwise/objectwise base-change selector,
    no finite sample or basis row,
    no new finite-index cell,
    and no context collapse.

Thus natural evaluations with pull-push mismatch, projection-formula gaps,
boundary/DD.4/exact-delta/graph/Rosati/control/handoff base-change gaps, or
externally supplied base-change data do not construct the current frontier.
```

## 3. Consequence

Doc 578 does not solve R1 and does not prove RH. It removes the vertical
naturality escape. The missing object now has to be a realized center whose
eliminator computes, normalizes, is functorial, preserves the structural
payload, executes that preservation by finite diamonds, gives conservative
represented semantics to the normal forms, evaluates naturally, and makes
that evaluation satisfy exact/cartesian Beck-Chevalley base-change.

The next negative route is sharper: prove every natural evaluation of a
represented source-internal semantic model has a pull-push mismatch,
projection-formula gap, boundary/DD.4/exact-delta/graph/Rosati/control/
handoff base-change gap, external/quotient/functor-of-points/Yoneda
base-change, or requires choice, a new finite-index cell, context collapse,
declaration, finite sample, basis row, or unbudgeted base-change data.

## 4. Verification Gates

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM1
    Requires the doc-578 Beck-Chevalley evaluation layer to be embedded.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM2
    Requires evaluation to have exact cartesian Beck-Chevalley base-change.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM3
    Requires pull-push commutation and projection formula.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM4
    Requires DD.4, boundary-pushforward, and exact-delta base-change routes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM5
    Requires graph, Rosati, control, handoff, and graph-later base-change routes.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM6
    Requires base-change to be internal, universal-arrow based, budgeted, and not a disguised external repair.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM7
    Requires Beck-Chevalley dependency closure.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM8
    Requires every Beck-Chevalley graph edge.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM9
    Requires every banned base-change repair to be covered by a rejecting variant.

CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBCHEVEVALNATREPSEM10
    Requires only exact/cartesian Beck-Chevalley evaluation to pass.
```
