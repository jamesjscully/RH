# 594 - Qbar_BECD FIdx24 Probe Obstruction-Localizing Verifier Trace Executable Global Contraction Contract Spec

## Status

Construction-spec refinement anchor. Layer I only; this is not an RH result.

## Pinch

Doc 593 requires a finite source-internal verifier separated from the trace
producer. That is still too weak if verification failure is only a Boolean
reject. A Boolean reject keeps the negative thread alive, but it does not say
which source facet, trace subterm, payload route, invariant, or budget charge
failed.

Doc 594 requires obstruction localization. The verifier-separated
trace-audited executable global contraction must return either an accepted
verified trace or a proof-relevant source-internal obstruction location. A
rejection must identify a canonical minimal failing subtrace/facet among the
same finite checks used by doc 593: schema, event coverage, canonical order,
replay, semantic reflection, invariant events, payload routes, source laws,
and exact-24 budget charge. This turns failure into a reusable no-go datum
rather than another search branch.

## Required Object

The new live object is:

```text
ObstructionLocalizingVerifierSeparatedTraceAuditedExecGloballyContractibleParametricContractibleLoopCompletePathIndependentPresInvariantSrcLawCompleteNFReflectPasteStabCycAmbMateCohDescEffBeckChevExactEvalNatRepSemModelSemConsInvReflectExecCritPairDiamondCohMonExactDagCompatFuncNormConfCompStabCenterElimRealCenterRealIntContrGlobUniqueEndTrivAutRigidCartCompatDiagRepLimSrcBundleRepLimFiltCofRefCalcStabRefDescStabMedGenCompStabJointSourceLawDD4ActiveRigidPrimEffK0Lift_ObstructionLocalizingVerifierTraceExecutableGlobalContraction_source_square
```

This object strengthens doc 593 by adding four acceptance clauses:

1. Verification returns a proof-relevant sum: accepted certificate or localized
   obstruction.
2. Every rejection localizes to a canonical minimal failing subtrace/facet.
3. The localized obstruction projects to source-internal invariant, route, and
   budget data.
4. The localizer is deterministic, terminating, extensional, and does not add
   a new cell or verifier layer.

## Fail-Closed Exclusions

Missing obstruction-localizing certificates, Boolean-only verifiers,
accept-only checkers, rejection without witnesses, noncanonical or nonminimal
locations, wrong blame assignment, external/oracle/producer-coupled
localization, missing subtrace witnesses, missing facet projection, missing
invariant or payload-route blame, missing budget blame, replay-unstable
obstructions, semantic-reflection blame gaps, incompatible obstruction
families, nondeterministic or nonterminating localizers, proof-irrelevant or
nonextensional localizers, unsound localization, incomplete failure coverage,
new cells, context collapse, declarations, finite samples, basis rows, and
unbudgeted localizer layers are diagnostics only.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_loc_verifier_trace_exec_global_contract
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMLOCVERIFTRACEEXECGLOBCONTR10 ALL PASS
```

The witness verifies that the frontier map accepts the obstruction-localizing
verifier trace executable global contraction, that its dependencies and edges
resolve, and that each banned localizer surrogate is covered by a rejected
repair.
