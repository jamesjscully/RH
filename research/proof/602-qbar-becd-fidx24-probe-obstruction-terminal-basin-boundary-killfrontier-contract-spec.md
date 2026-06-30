# 602 - Qbar_BECD FIdx24 Probe Obstruction Terminal Basin Boundary Killfrontier Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 601 gives the terminal obstruction basin a finite source-internal boundary.
That is still too weak if a boundary facet is only a label. A claimed boundary
can remain unfalsifiable unless each facet lands on a named negative mechanism
that would kill the construction if the facet fails.

Doc 602 requires every terminal-basin boundary facet to be anchored to a current
kill-frontier item. The anchor must preserve the boundary, preserve the
reflected fixed point, avoid a second terminal state, and remain finite,
source-internal, deterministic, extensional, proof-relevant, graph-wired,
dependency-closed, replay-stable, and budgeted.

## Required Object

The new live object is:

```text
ObstructionTerminalBasinBoundaryKillfrontierObstructionTerminalBasinBoundaryObstructionTerminalBasinObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionTerminalBasinBoundaryKillfrontierReflectedFixedpointTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 601 by adding five acceptance clauses:

1. The doc 601 terminal-basin boundary is the anchor base.
2. Every entry boundary facet has a deterministic kill-frontier anchor.
3. Every rejected escape boundary facet has a deterministic kill-frontier
   anchor.
4. Each anchor is a listed current negative kill-frontier item.
5. Anchoring is boundary-preserving, fixed-point-stable, dependency-closed,
   graph-wired, replay-stable, source-internal, and inside the exact-24 budget.

## Fail-Closed Exclusions

Missing kill-frontier anchor certificates, unanchored entry or escape
boundaries, missing kill-frontier items, unlisted/noncurrent/nonnegative/
infinite/non-source-internal anchors, nondeterministic or nonextensional
anchors, dependency-open or graph-unwired anchors, replay-unstable anchors,
anchors that relabel the boundary, change the fixed point, allow a second
terminal state, or are proof-irrelevant, external, oracle-backed,
branch-spawning, unbounded, retuned, new-cell, context-collapse, declaration,
finite-sample, basis-row, or unbudgeted systems are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that every doc 601 boundary surface is anchored to a
current negative kill-frontier item, and rejects arbitrary labels or detached
anchors as disguised repairs.
