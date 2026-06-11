# 84 - Non-factorization theorem target

Status: theorem target / A1 escape boundary, 2026-06-11. This states
the minimal positive theorem needed to escape doc 82 factor-through
scale collapse. It is not a construction and does not admit B1.

## 1. Purpose

Doc 82 kills any claimed scale-retentive trace whose load-bearing data
factors through the bare scale-blind object `B_l`. The remaining live
path is to prove that an enriched trace package does not factor
through `B_l` before trace evaluation.

The target is deliberately narrow:

```text
prove non-factorization for the scale carrier and trace domain.
```

It does not prove same-form LS4, carrier selectivity, LS3, BC13, P3,
Count, Compare, or RH.

## 2. Minimal Data

A non-factorization theorem must name:

```text
1. a parameter l > 0, later l = log p;
2. an enriched pre-trace object O_l;
3. the bare scale-blind output B_l of doc 82;
4. a trace domain D_l;
5. a trace or invariant Tr_l: D_l -> V;
6. the structural map placing O_l in D_l;
7. every forgetful functor from D_l toward B_l used by the candidate.
```

The record must also state which carrier is being tested:

```text
metric coefficient;
liquid analytic-ring norm or radius;
equivariant datum;
density object;
explicit kernel parameter;
stronger retained structure.
```

## 3. Theorem Target

### Target 84.1

For a named enriched trace package `(O_l, D_l, Tr_l)`, prove one of the
following.

```text
NF84.A trace-detected non-isomorphic enriched objects
  O_l and O_m are not isomorphic in the trace-relevant enriched
  category for some l != m, and this non-isomorphism is detected by
  D_l, by a traceability hypothesis, or by the frozen value Tr_l(O_l).
  Doc 85 gives the trace-detection guard for this clause.

NF84.B no factor-through functor
  There is no functorial factorization
      O_l -> B_l -> D_l -> V
  that determines Tr_l(O_l).

NF84.C trace-domain dependence
  D_l itself changes with l in a way visible to the traceability
  theorem, not merely to notation or post-processing.

NF84.D trace-value dependence
  The frozen trace/invariant changes with l by theorem, before any
  post-trace normalization is applied.
```

Any one of NF84.A-NF84.D can move doc 81 from `HOLD_A1` toward
`PASS_A1`, subject to the full doc-81 deletion test.

## 4. Required Tests

A claimed non-factorization theorem must pass these tests.

```text
T84.1 Freeze
  All categories, objects, constants, maps, and trace formulas are
  fixed before any zero-side comparison.

T84.2 Forget
  List every forgetful functor to bare topology, bare sheaves,
  localizing-invariant outputs, theta/count shadows, and Poisson
  readouts.

T84.3 Deletion
  Replace l by arbitrary m > 0 at the earliest structural carrier and
  prove what changes.

T84.4 Factor-through exclusion
  Prove the trace is not determined by B_l. If this is unknown, record
  HOLD_A1, not PASS_A1.

T84.5 Late-insertion audit
  Verify that l, 1/l, 2pi/l, Haar density, Gaussian width, determinant
  term, residue, or normalization is not first added after Tr_l is
  evaluated.
```

## 5. Carrier-Specific Minimums

The non-factorization burden depends on the claimed carrier.

```text
Metric trace
  l must be a metric coefficient, length, growth condition, Sobolev
  control, or nuclearity control in the trace domain. Prove the
  traceability theorem uses that metric data before evaluation, not a
  later Haar or normalization factor.

Liquid analytic-ring trace
  l must occur in analytic-ring norms, radii, condensed/liquid module
  structure, or the kernel category. Prove that forgetting to bare
  Shv(S^1; C) loses the trace theorem, changes its hypotheses, or no
  longer determines the trace.

Equivariant trace
  l must survive in the equivariant or parametrized structure over
  R/lZ, not merely in the homotopy type S^1. Prove the trace is not
  naturally determined by the underlying bare circle.

Density trace
  The density must be an object or coefficient in D_l before trace.
  A Haar factor, residue, or measure normalization chosen after trace
  is doc-80 late insertion.

Kernel trace
  The kernel K_l must use l before trace evaluation and be trace-class
  in the enriched category. Prove the evaluated trace is not
  determined only by theta/count/Poisson/localizing shadows.
```

For all carrier types, identify the hypothesis of the traceability
theorem that fails, changes, or becomes unavailable after forgetting
the enriched carrier to `B_l`.

## 6. Verdicts

Doc 81 remains the canonical A1 verdict ledger. The doc-84 local
verdicts are:

```text
PASS_NONFACTOR_A1
  NF84.A, NF84.B, NF84.C, or NF84.D is proved and the result passes
  doc 81 P1-P4/P6. This maps to PASS_A1 for scale retention only.

HOLD_NONFACTOR_A1
  A genuine enriched carrier is named, but traceability, deletion,
  theorem dependency, or same-form use remains unwritten. This maps to
  HOLD_A1.

REJECT_A1
  The claimed enrichment factors through B_l, is forgotten before
  trace, or uses post-trace scale insertion.

OUT_OF_SCOPE
  The answer discusses LS4, carrier selectivity, positivity, zeros, or
  RH without deciding pre-trace scale retention.
```

`PASS_NONFACTOR_A1` here is only A1/G60.2/LT76.1. It is not B1
admission.

## 7. A1 Verdicts

```text
REJECT_A1
  The claimed enrichment is forgotten before trace, or the trace value
  is determined by B_l.

HOLD_A1
  A plausible enriched carrier is named, but non-factorization or
  trace dependence has not been proved.

PASS_A1
  NF84.A, NF84.B, NF84.C, or NF84.D is proved, the deletion test
  changes the frozen trace/domain/object, and no late insertion occurs.

OUT_OF_SCOPE
  The answer concerns LS4, carrier selectivity, positivity, Count,
  Compare, or zero-side evidence without deciding non-factorization.
```

`PASS_A1` here is only A1/G60.2/LT76.1. It is not B1 admission.

## 8. Overclaim Guards

```text
G84.1 Non-factorization is not same-form coupling.
  A trace may retain scale but still fail doc 79 if the archimedean
  piece is a side block.

G84.2 Non-factorization is not carrier selectivity.
  A trace may retain scale but still compute for Epstein/DH controls.

G84.3 Non-factorization is not unit derivation.
  A trace may retain scale but still rely on external Gaussian/Haar or
  normalization data.

G84.4 Non-factorization is not broad NO76.1 failure.
  Proving one enriched package survives does not classify all others.

G84.5 Calibration is not non-factorization.
  Route A/B0 Poisson or Tate/RR identities remain calibration unless
  the trace package retains l before evaluation.
```

## 9. Minimal Expert Question

For an external expert, the falsifiable question is:

```text
In your proposed category, does the trace of T_l or its kernel package
factor through the bare object B_l of doc 82? If no, state the theorem
that prevents the factorization and identify whether it proves
NF84.A, NF84.B, NF84.C, or NF84.D.
```

Useful answers must provide:

```text
category:
enriched object O_l:
trace domain D_l:
traceability theorem:
forgetful functors:
non-factorization theorem:
deletion-test result:
late-insertion audit:
```

## 10. Relation To Existing Docs

```text
doc 81
  Provides the A1 decision ledger and deletion test.

doc 82
  Provides the factor-through rejection theorem.

doc 83
  Scores external answers that claim non-factorization.

doc 76
  Places this target inside LT76.1. LT76.3-LT76.7 remain separate.

doc 79
  Still governs whether a scale-retentive trace is same-form LS4 or a
  side block.

doc 85
  Requires object-level non-isomorphism to be detected by the
  load-bearing trace/domain/value before it can count as PASS_A1.
```

The operational rule is:

```text
Do not write a new A6/S3 witness from an enriched trace package until
doc 84 is answered at PASS_NONFACTOR_A1, this is mapped to doc-81
PASS_A1, and the remaining doc-76/doc-71 gates are separately
recorded.
```
