# 606 - Qbar_BECD FIdx24 Probe Obstruction Terminal Basin Boundary Killfrontier Facet Route Edge Priority Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 605 requires every facet-route edge to carry a local semantic witness.
That is still too weak if overlapping semantic tokens are resolved by hidden
code order, name order, or a global lookup table. In the doc-605 surface
inventory, 57 of 106 surface witnesses match more than one semantic class
under the declared token rules.

Doc 606 requires those overlaps to be resolved by a finite, explicit,
replay-stable priority audit. Every surface witness must record its winning
class, winning tokens, all lower-priority shadow classes, shadow tokens, and
the composed doc-602 anchor.

## Required Object

The new live object is:

```text
ObstructionTerminalBasinBoundaryKillfrontierFacetRouteEdgePriorityObstructionTerminalBasinBoundaryKillfrontierFacetRouteEdgeWitnessObstructionTerminalBasinBoundaryKillfrontierFacetRouteGraphObstructionTerminalBasinBoundaryKillfrontierFacetTaxonomyObstructionTerminalBasinBoundaryKillfrontierObstructionTerminalBasinBoundaryObstructionTerminalBasinObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionTerminalBasinBoundaryKillfrontierFacetRouteEdgePriorityReflectedFixedpointTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 605 by adding seven acceptance clauses:

1. The doc-605 edge-witness object is the priority-audit base.
2. The priority order is finite, explicit, and contains exactly the 18
   semantic classes used by the local edge-witness rules.
3. All 106 surface witnesses have priority decisions.
4. All 57 token-overlap cases are explicitly recorded as ambiguous priority
   decisions.
5. Each decision records the winning class, winning tokens, shadow classes,
   shadow tokens, and the composed doc-602 anchor.
6. Class-anchor support remains present inside the same priority order.
7. The priority layer is minimal, finite, source-internal, deterministic,
   extensional, proof-relevant, dependency-closed, graph-wired,
   replay-stable, and budgeted.

## Fail-Closed Exclusions

Missing priority certificates, missing or incomplete priority orders, retuned
priority orders, missing priority decisions, unprioritized token overlaps,
winner-class mismatches, missing winning tokens, unrecorded shadow tokens,
composite priority mismatches, class anchors missing from priority,
global-lookup priority, name-order priority, nonminimal, infinite,
non-source-internal, nondeterministic, nonextensional, dependency-open,
graph-unwired, replay-unstable, proof-irrelevant, external, oracle-backed,
branch-spawning, unbounded, retuned, new-cell, context-collapse,
declaration-only, finite-sample, basis-row, or unbudgeted priority audits are
diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPRIOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPRIOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies 106 priority decisions, 57 ambiguous token-overlap
decisions, the 18-class priority order, preservation of doc-602 anchor
composition, the doc-605 edge-witness base, and 29 audited graph edges.
