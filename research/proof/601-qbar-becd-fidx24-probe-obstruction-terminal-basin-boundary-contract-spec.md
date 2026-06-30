# 601 - Qbar_BECD FIdx24 Probe Obstruction Terminal Basin Boundary Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 600 makes every admissible obstruction entry trace absorb into the same
source-internal terminal fixed point. That is still too weak if the basin has
an untyped edge: a claimed absorption can hide an unseparated escape surface
where the next obstruction is neither an accepted entry nor a rejected repair.

Doc 601 requires a finite boundary separator for the terminal basin. Every
entry surface and every rejected escape variant must have a named
source-internal boundary facet, and those facets must separate without
changing the terminal fixed point or opening a second terminal state.

## Required Object

The new live object is:

```text
ObstructionTerminalBasinBoundaryObstructionTerminalBasinObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionTerminalBasinBoundaryReflectedFixedpointTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 600 by adding five acceptance clauses:

1. The doc 600 terminal basin is the boundary base.
2. Every admissible entry trace has a boundary facet.
3. Every doc 600 rejected escape variant has a boundary facet.
4. Boundary separation is absorbing and fixed-point stable.
5. The boundary is finite, source-internal, canonical, proof-relevant,
   extensional, replay-stable, graph-wired, and budgeted.

## Fail-Closed Exclusions

Missing boundary certificates, incomplete entry-boundary or escape-boundary
coverage, unlisted boundary surfaces, nonseparating boundaries, missing
pipeline, invariant, payload, repair, no-go, budget, context, sample, or trace
boundaries, boundaries that fail to absorb, change the fixed point, allow a
second terminal state, overlap incompatibly, are infinite, noncanonical,
non-replay-stable, nonterminating, nondeterministic, nonextensional,
proof-irrelevant, external, oracle, branch-spawning, unbounded, retuned, or
non-source-internal, new cells, context collapse, declarations, finite
samples, basis rows, and unbudgeted boundary systems are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the obstruction terminal
basin boundary certificate, covers all entry and escape boundary surfaces, and
rejects each non-boundary surrogate as a disguised repair.
