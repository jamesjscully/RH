# 598 - Qbar_BECD FIdx24 Probe Obstruction Normalform-Reflecting Confluent Action Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 597 requires the bounded obstruction-action system to be terminating and
confluent. That still leaves one precise escape: the unique action normal form
could be a proof-side join certificate that does not update the same
executable/global contraction state.

Doc 598 requires normal-form reflection for obstruction actions. The unique
confluent action normal form must be reflected into the executable state, the
global contraction state, the terminal certificate, the invariant state, and
the payload trace. This prevents the action layer from proving confluence while
erasing the resulting normal form before the construction actually contracts.

## Required Object

The new live object is:

```text
ObstructionNormalformReflectingObstructionConfluentObstructionActionableObstructionClassifyingObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidPrimEffK0Lift_ObstructionNormalformReflectingConfluentActionTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 597 by adding five acceptance clauses:

1. The doc 597 unique action normal form is the reflected normal form.
2. Reflection updates the executable and global contraction states.
3. Reflection updates the terminal certificate, invariant state, and payload
   trace.
4. Accepted, repair, no-go, budget, context, sample, and trace actions are all
   reflected through the same normal form.
5. Reflection is source-internal, idempotent, deterministic, proof-relevant,
   extensional, replay-stable, budgeted, and graph-wired.

## Fail-Closed Exclusions

Missing reflection certificates, proof-erased normal forms, unreflected normal
forms, executable/global/terminal reflection failure, unreflected accepted,
repair, no-go, budget, context, sample, trace, invariant, or payload actions,
wrong or stale reflected state, nonidempotent, nondeterministic,
nonreplayable, nonextensional, proof-irrelevant, external, oracle, or
non-source-internal reflection, nonterminal action normal forms, unreflected
join traces or critical pairs, branch spawning, unbounded or retuned
reflection, new cells, context collapse, declarations, finite samples, basis
rows, and unbudgeted reflection systems are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_nf_reflect_confluent_action_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the obstruction
normal-form-reflecting confluent action certificate, that all dependencies and
graph edges resolve, that the doc 597 normal form reflects into executable
state and trace payload, and that each banned non-reflecting surrogate is
covered by a rejected repair.
