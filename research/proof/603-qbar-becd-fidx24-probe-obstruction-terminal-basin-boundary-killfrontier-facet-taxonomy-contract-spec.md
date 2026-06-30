# 603 - Qbar_BECD FIdx24 Probe Obstruction Terminal Basin Boundary Killfrontier Facet Taxonomy Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 602 requires every terminal-basin boundary facet to anchor to a current
negative kill-frontier item. That is still too weak if the route from facet to
anchor can pass through a default bucket. A fallback classifier can preserve
the anchor list while hiding which local failure type the boundary facet is
actually testing.

Doc 603 requires an explicit facet taxonomy between boundary facets and
kill-frontier anchors. Every entry and rejected-escape facet must have exactly
one finite source-internal class, no default route, and a class anchor that
agrees with the doc-602 facet anchor.

## Required Object

The new live object is:

```text
ObstructionTerminalBasinBoundaryKillfrontierFacetTaxonomyObstructionTerminalBasinBoundaryKillfrontierObstructionTerminalBasinBoundaryObstructionTerminalBasinObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionTerminalBasinBoundaryKillfrontierFacetTaxonomyReflectedFixedpointTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 602 by adding five acceptance clauses:

1. The doc 602 kill-frontier anchor map is the taxonomy base.
2. Every doc 601 boundary facet is classified.
3. Facet classes are explicit and disjoint; fallback/default anchors are
   rejected.
4. The class anchor for each facet equals the doc 602 facet anchor.
5. The taxonomy is minimal, boundary-preserving, fixed-point-stable,
   dependency-closed, graph-wired, replay-stable, source-internal, and
   budgeted.

## Fail-Closed Exclusions

Missing facet taxonomy certificates, unclassified or ambiguously classified
boundary surfaces, default anchor routes, class-anchor mismatches,
unseparated anchor buckets, infinite or non-source-internal facet classes,
nondeterministic or nonextensional classes, dependency-open or graph-unwired
classes, replay-unstable or nonminimal classes, classes that relabel the
boundary, change the fixed point, allow a second terminal state, or are
proof-irrelevant, external, oracle-backed, branch-spawning, unbounded,
retuned, new-cell, context-collapse, declaration, finite-sample, basis-row, or
unbudgeted classifiers are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that all 106 doc-601 boundary facets reach their
doc-602 kill-frontier anchors through explicit finite facet classes, and
rejects fallback buckets as disguised repairs.
