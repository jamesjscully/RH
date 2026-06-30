# 596 - Qbar_BECD FIdx24 Probe Obstruction-Actionable Classifier Trace Executable Global Contraction Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 595 requires every localized verifier obstruction to be classified by a
finite source-internal taxonomy. That is still too weak if the classification
is inert: a label can record the obstruction while leaving the search with an
unbounded choice of next moves.

Doc 596 requires actionability. Each obstruction class must map to exactly one
bounded source-internal action: accept the verified trace, emit named no-go
evidence, apply a bounded repair against an existing requirement, open the
recorded dependency gap, or reject budget/context/external/sample failures as
such. The action trace must be replayable and must decrease a finite frontier
measure, so classification cannot become a new branching layer.

## Required Object

The new live object is:

```text
ObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidCartCompatDiagRepLimSrcBundleRepLimFiltCofRefCalcStabRefDescStabMedGenCompStabJointSourceLawDD4ActiveRigidPrimEffK0Lift_ObstructionActionableClassifierTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 595 by adding four acceptance clauses:

1. Every finite obstruction class maps to exactly one bounded action.
2. The action plan is deterministic, terminating, replay-stable,
   proof-relevant, and extensional over the classification.
3. Repair actions target existing requirements, no-go actions target named
   no-go evidence, and every action links to named kill-frontier data.
4. The action trace decreases a finite frontier measure and cannot spawn
   unbounded branches or action loops.

## Fail-Closed Exclusions

Missing action plans, inert class-only labels, unclassified or ambiguous
actions, wrong actions, external/oracle actions, non-source-internal, partial,
nondeterministic, nonterminating, proof-irrelevant, or nonextensional action
plans, action loops, branch spawning, nonmonotone refinement, unbounded search,
repairs outside existing requirements, unnamed no-go actions, missing
kill-frontier/budget/context/sample links, missing action traces, retuned
actions, new cells, context collapse, declarations, finite samples, basis
rows, and unbudgeted action layers are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_action_classifier_trace_exec_global_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the actionable obstruction
classifier, that dependencies and graph edges resolve, that every obstruction
class has a unique bounded action, and that each banned inert/action-loop
surrogate is covered by a rejected repair.
