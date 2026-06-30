# 592 - Qbar_BECD FIdx24 Probe Trace-Audited Executable Global Contraction Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 591 made the doc-590 global contraction executable inside the existing
finite critical-pair normalizer. That is still too weak if the evaluator is a
black box: it could return the unique global section while hiding a
post-hoc proof, an external auditor, an oracle query, or an unlogged payload
projection.

Doc 592 requires the executable global contraction to be trace-audited. The
same source-internal evaluator must emit a proof-relevant replay trace whose
events reconstruct the contraction and expose the normalizer, semantic,
invariant, payload, source-law, endpoint/degree/projection, boundary/DD.4,
exact-delta, graph/Rosati/control/handoff, base-change, Beck-Chevalley,
refinement/descent, and universal-arrow steps. The trace is part of the
existing exact-24 budget; it is not a new cell or a second proof layer.

## Required Object

The new live object is:

```text
TraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidCartCompatDiagRepLimSrcBundleRepLimFiltCofRefCalcStabRefDescStabMedGenCompStabJointSourceLawDD4ActiveRigidPrimEffK0Lift_TraceAuditedExecutableGlobalContraction_source_square
```

This object strengthens doc 591 by adding four acceptance clauses:

1. The evaluator returns an internal proof-relevant trace, not only a normal
   form.
2. The trace is deterministic, replayable, and order-canonical for the
   finite critical-pair calculus.
3. The trace logs every downstream invariant and every payload route used by
   the contraction.
4. Every forbidden surrogate is rejected by a named trace gap, not by a prose
   judgment.

## Fail-Closed Exclusions

Missing trace-audited certificates, non-trace-audited evaluators, opaque or
lossy traces, post-hoc logs, external or oracle auditors, proof-irrelevant
traces, nondeterministic traces, nonterminating trace extraction, unlogged
critical pairs, unlogged normal forms, missing semantic or invariant events,
unlogged payload/source-law/endpoint/degree/projection/boundary/DD.4/
exact-delta/graph/Rosati/control/handoff/base-change/Beck-Chevalley/
refinement-descent/universal-arrow events, non-replayable traces,
noncanonical trace order, new cells, context collapse, declaration-only
certificates, finite samples, basis rows, and unbudgeted trace layers are
diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_trace_audited_exec_global_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTRACEAUDITEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTRACEAUDITEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the trace-audited
executable global contraction, that its dependencies and edges resolve, and
that each banned surrogate is covered by a rejected repair.
