# 605 - Qbar_BECD FIdx24 Probe Obstruction Terminal Basin Boundary Killfrontier Facet Route Edge Witness Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 604 requires the doc-603 taxonomy to be executable as a finite two-step
route graph:

```text
boundary surface -> used facet class -> current kill-frontier anchor
```

That is still too weak if the graph edges are bare edges justified only by a
global lookup table or by surface-name matching. Such an edge graph can
compose correctly while hiding whether each edge has a local semantic reason.

Doc 605 requires every surface-to-class edge and every class-to-anchor edge to
carry a local semantic witness. A surface-edge witness must record the source
kind, local subject, matched semantic token, class rule, anchor rule, and
composed anchor. A class-anchor witness must have nonempty supporting
surface-edge witnesses and support tokens.

## Required Object

The new live object is:

```text
ObstructionTerminalBasinBoundaryKillfrontierFacetRouteEdgeWitnessObstructionTerminalBasinBoundaryKillfrontierFacetRouteGraphObstructionTerminalBasinBoundaryKillfrontierFacetTaxonomyObstructionTerminalBasinBoundaryKillfrontierObstructionTerminalBasinBoundaryObstructionTerminalBasinObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionTerminalBasinBoundaryKillfrontierFacetRouteEdgeWitnessReflectedFixedpointTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 604 by adding five acceptance clauses:

1. The doc-604 route graph is the edge-witness base.
2. All 106 surface-to-class edges have local semantic witnesses.
3. All 17 class-to-anchor edges have support witnesses and support tokens.
4. The edge-witness composites equal the doc-602 boundary-anchor map.
5. The edge-witness layer is minimal, finite, source-internal,
   dependency-closed, graph-wired, replay-stable, proof-relevant, and
   budgeted.

## Fail-Closed Exclusions

Missing edge-witness certificates, missing surface-edge witnesses, missing
class-anchor witnesses, missing edge subjects, edge-kind mismatches, missing
local tokens, class-rule mismatches, anchor-rule mismatches, composite witness
mismatches, name-only surface edges, global-lookup-only surface or class-anchor
edges, missing class-anchor support, missing support tokens, nonminimal,
infinite, non-source-internal, nondeterministic, nonextensional,
dependency-open, graph-unwired, replay-unstable, proof-irrelevant, external,
oracle-backed, branch-spawning, unbounded, retuned, new-cell,
context-collapse, declaration, finite-sample, basis-row, or unbudgeted edge
witnesses are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies 106 surface-edge witnesses, 17 class-anchor witnesses,
local semantic tokens for each surface edge, support tokens for each used
class anchor, and edge-witness composition equal to the doc-602 anchor map.
