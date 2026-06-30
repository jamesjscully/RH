# 593 - Qbar_BECD FIdx24 Probe Verifier-Separated Trace Executable Global Contraction Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 592 requires the executable global contraction to emit a source-internal
proof-relevant replay trace. That is still too weak if the same evaluator can
also be the only judge of its own trace. A self-accepted trace could hide a
producer-coupled checker, a shared oracle, a post-hoc acceptance rule, or a
checker that only verifies the trace schema without replaying the source
calculus.

Doc 593 requires verifier separation. The trace-audited executable global
contraction must come with a finite source-internal verifier that is separate
from the trace producer. The verifier checks the trace schema, event coverage,
canonical order, replay, semantic reflection, invariant events, payload-route
events, and exact-24 budget charge. It must be sound, complete for admissible
traces, deterministic, terminating, proof-relevant, and extensional in the
trace data.

## Required Object

The new live object is:

```text
VerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidCartCompatDiagRepLimSrcBundleRepLimFiltCofRefCalcStabRefDescStabMedGenCompStabJointSourceLawDD4ActiveRigidPrimEffK0Lift_VerifierSeparatedTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 592 by adding four acceptance clauses:

1. Trace production and trace verification factor through distinct internal
   maps with no shared external oracle.
2. The verifier replays the trace rather than merely checking that a log is
   well shaped.
3. The verifier rejects every forbidden trace failure by a named local check.
4. The verifier itself is finite, terminating, budgeted, and source-internal.

## Fail-Closed Exclusions

Missing verifier-separated certificates, no verifier, producer-coupled
verifiers, external checkers, oracle checkers, shared-oracle checkers,
schema-only checks, unchecked event coverage, unchecked canonical order,
unchecked replay, unchecked semantic reflection, unchecked invariants,
unchecked payload routes, unchecked budget charge, unsound verifiers,
incomplete admissible-trace verification, invalid-trace acceptance,
nondeterministic or nonterminating verifiers, proof-irrelevant verifiers,
nonextensional verification, new cells, context collapse, declaration-only
certificates, finite samples, basis rows, and unbudgeted verifier layers are
diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_verifier_sep_trace_exec_global_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the verifier-separated
trace executable global contraction, that its dependencies and edges resolve,
and that each banned verifier surrogate is covered by a rejected repair.
