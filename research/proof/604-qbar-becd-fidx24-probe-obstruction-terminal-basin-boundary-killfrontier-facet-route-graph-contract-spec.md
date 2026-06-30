# 604 - Qbar_BECD FIdx24 Probe Obstruction Terminal Basin Boundary Killfrontier Facet Route Graph Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 603 requires every terminal-basin boundary facet to pass through an
explicit finite taxonomy class before it reaches a current negative
kill-frontier anchor. That is still too weak if the taxonomy is only a static
lookup table. A lookup can name a class and an anchor while hiding whether the
route actually composes as source-level graph data.

Doc 604 requires an explicit finite route graph between boundary facets,
used taxonomy classes, and kill-frontier anchors. Every accepted route must be
a two-step graph

```text
boundary surface -> used facet class -> current kill-frontier anchor
```

whose composite equals the doc-602 boundary-anchor map. Direct
surface-to-anchor shortcuts, orphan classes, unused route classes, missing
entry/escape bridge compatibility, and noncomposable routes are rejected.

## Required Object

The new live object is:

```text
ObstructionTerminalBasinBoundaryKillfrontierFacetRouteGraphObstructionTerminalBasinBoundaryKillfrontierFacetTaxonomyObstructionTerminalBasinBoundaryKillfrontierObstructionTerminalBasinBoundaryObstructionTerminalBasinObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionTerminalBasinBoundaryKillfrontierFacetRouteGraphReflectedFixedpointTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 603 by adding five acceptance clauses:

1. The doc-603 facet taxonomy is the route-graph base.
2. Every doc-601 boundary facet has a surface-to-class edge.
3. Every used facet class has a class-to-anchor edge.
4. The two-step composite equals the doc-602 boundary-anchor map, with no
   direct surface-to-anchor shortcut.
5. The route graph is support-minimal, finite, source-internal,
   dependency-closed, graph-wired, replay-stable, proof-relevant, and
   budgeted.

## Fail-Closed Exclusions

Missing route graph certificates, missing surface-to-class or class-to-anchor
edges, noncomposable routes, composites that disagree with the doc-602 anchor
map, direct anchor shortcuts, orphan or unused route classes, missing
entry/escape bridge compatibility, anchor-bucket route merges, class-anchor
mismatches, nonminimal, infinite, non-source-internal, nondeterministic,
nonextensional, dependency-open, graph-unwired, replay-unstable,
proof-irrelevant, external, oracle-backed, branch-spawning, unbounded,
retuned, new-cell, context-collapse, declaration, finite-sample, basis-row, or
unbudgeted route graphs are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMROUTEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMROUTEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies 106 surface-to-class edges, 17 class-to-anchor edges,
17 used route classes inside the 18-class doc-603 taxonomy universe, and a
two-step composite equal to the doc-602 boundary-anchor map.
