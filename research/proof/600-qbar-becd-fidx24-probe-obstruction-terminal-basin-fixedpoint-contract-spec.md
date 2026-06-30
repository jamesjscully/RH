# 600 - Qbar_BECD FIdx24 Probe Obstruction Terminal Basin Fixedpoint Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 599 makes the reflected obstruction normal form a replay fixed point. That
is still too weak if this is only one terminal state selected by one entry
trace. A different verifier, localizer, classifier, action, repair, no-go,
budget, context, sample, invariant, or payload entry could still escape to a
different fixed point.

Doc 600 requires a terminal basin. Every admissible obstruction entry trace in
the finite doc 599 surface must be enumerated and absorbed by the same
source-internal replay fixed point. This blocks the construction from hiding a
second terminal state behind another obstruction entry route.

## Required Object

The new live object is:

```text
ObstructionTerminalBasinObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionTerminalBasinReflectedFixedpointTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 599 by adding five acceptance clauses:

1. The doc 599 replay fixed point is the unique terminal state.
2. Every admissible obstruction entry trace is enumerated.
3. Every entry trace is absorbed by the same fixed point.
4. Pipeline, invariant, payload, repair, no-go, budget, context, sample, and
   trace entries all lie in that basin.
5. The basin is source-internal, finite, absorbing, canonical,
   proof-relevant, extensional, graph-wired, and budgeted.

## Fail-Closed Exclusions

Missing basin certificates, incomplete entry-trace coverage, unlisted entry
traces, escaping entry traces, entry traces that change the fixed point,
nonterminating, nondeterministic, non-replay-stable, or non-source-internal
entry routing, missing verifier, trace-audit, localizer, classifier, action,
confluence, reflection, fixed-point, invariant, payload, repair, no-go, budget,
context, sample, or trace entries, noncanonical basins, overlapping
incompatible basins, multiple fixed points, nonabsorbing or nonextensional
basins, proof-irrelevant, external, oracle, branch-spawning, unbounded, or
retuned basins, new cells, context collapse, declarations, finite samples,
basis rows, and unbudgeted basin systems are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_fixedpoint_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the obstruction terminal
basin certificate, that all finite obstruction entry traces route to the same
terminal fixed point, and that each banned non-basin surrogate is covered by a
rejected repair.
