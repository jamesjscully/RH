# 599 - Qbar_BECD FIdx24 Probe Obstruction Reflected Fixedpoint Normalform Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 598 requires the doc 597 unique bounded action normal form to reflect into
the executable/global contraction state. That is still too weak if the
reflected state fails on replay: rerunning the verifier, localizer,
classifier, action plan, confluence, or reflection step could produce a fresh
obstruction or a changed normal form.

Doc 599 requires fixed-point closure. Once the reflected normal form is written
into the executable/global contraction state, the entire obstruction pipeline
must replay as a no-op. This turns reflection from a one-time update into a
stable terminal state.

## Required Object

The new live object is:

```text
ObstructionReflectedFixedpointObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionReflectedFixedpointNormalformTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 598 by adding five acceptance clauses:

1. The doc 598 reflected normal form is the fixed-point base.
2. Rerunning verifier, trace audit, localizer, classifier, action plan,
   confluence, and reflection leaves the state unchanged.
3. Replay creates no residual obstruction and no new bounded action.
4. The normal form, terminal certificate, invariant state, and payload trace
   are stable under replay.
5. The replay fixed point is source-internal, idempotent, deterministic,
   terminating, proof-relevant, extensional, graph-wired, and budgeted.

## Fail-Closed Exclusions

Missing fixed-point certificates, post-reflection verifier or trace audit
failure, localizer/classifier/action/confluence/reflection changes, residual
obstructions, new obstructions or actions after replay, changed normal forms,
changed terminal certificates, invariant states, or payload traces, unfixed
accepted, repair, no-go, budget, context, sample, or trace states,
non-idempotent pipelines, nondeterministic, nonterminating, non-replay-stable,
proof-irrelevant, nonextensional, external, oracle, or non-source-internal
fixed points, branch-spawning or unbounded replay, retuned pipelines, new
cells, context collapse, declarations, finite samples, basis rows, and
unbudgeted fixed-point systems are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_reflected_fixedpoint_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the obstruction reflected
fixed-point certificate, that replay dependencies and graph edges resolve,
that the reflected normal form is stable under the obstruction pipeline, and
that each banned non-fixed surrogate is covered by a rejected repair.
