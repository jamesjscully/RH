# 138 - METEQ late/factor-through obstruction

Status: bounded candidate-driven no-go / Q134.4 internal result,
2026-06-11. This attacks METEQ-A1 after doc 133. It does not kill all
metric, equivariant, liquid, density, or kernel circle enrichments. It
rejects enrichments that factor through bare circle data or insert
scale only after trace.

## 1. Purpose

Doc 133 named:

```text
METEQ-A1
```

as the surviving S2 scale-retention target. This document applies docs
80, 82, 84, and 85 to the obvious false-positive class:

```text
write T_p as an enriched metric/equivariant circle, but let the
load-bearing trace forget the enrichment or append log p after the
trace has already been computed.
```

That class does not pass A1.

## 2. Covered Class

Call an S2 proposal `METEQ_late` if it satisfies all of:

```text
M138.1 enriched notation
  The pre-trace object is written as a metric, equivariant, analytic,
  density, kernel, or liquid enrichment of R/(log p)Z.

M138.2 bare trace-visible image
  The trace theorem, trace domain, or trace value is determined by a
  bare scale-blind image B_l, bare Shv(S^1)-type data, ordinary
  localizing invariants, theta/count shadows, or Poisson readouts.

M138.3 forgotten enrichment
  The metric/equivariant/liquid/density/kernel datum is forgotten
  before trace evaluation, or is not a hypothesis of the trace theorem.

M138.4 late scale dependence
  Any remaining log p dependence enters as l, 1/l, 2pi/l, Haar
  density, Gaussian width, determinant normalization, residue, or
  comparison factor after the trace-visible value is computed.

M138.5 no same-structure LS4 use
  The enriched datum, even if object-level non-isomorphic, is not shown
  to be the same structure that later enters one mixed LS4 object with
  b1(p^Z).
```

This class includes:

```text
ordinary circle traces with 2pi/log p normalization;
localizing-invariant circle values with metric labels;
metric non-isomorphism proofs whose trace theorem ignores the metric;
density or Haar factors appended after trace;
kernel formulas whose evaluated trace factors through theta/count or
Poisson shadows.
```

## 3. Lemma

### Lemma 138.1

Every `METEQ_late` proposal fails doc-81 `PASS_A1`.

Verdict:

```text
REJECT_A1
  if the trace-visible image factors through the bare scale-blind
  object B_l or if scale appears only after trace.

HOLD_A1
  if enriched objects are genuinely non-isomorphic but trace detection
  has not been proved.

REJECT_SIDE_BLOCK
  if the enriched scale data is only a side object and not the same
  structure used for LS4 coupling.
```

### Proof

Under M138.2-M138.3, the trace value is determined by the image of the
candidate in scale-blind trace-visible data. Doc 82 applies when that
image is the bare object B_l: the frozen trace is independent of
`l`. Doc 85 applies when object-level enrichment exists but is
forgotten by the trace: non-isomorphic enriched objects do not advance
A1 unless the trace domain, trace theorem, or frozen trace value
detects the enrichment.

Under M138.4, doc 80 applies. Appending `log p`, `1/log p`,
`2pi/log p`, Haar density, Gaussian width, determinant normalization,
or residue after the trace has been evaluated is late scale insertion,
not scale retention.

Under M138.5, even a trace-detected scale datum would not yet supply
same-form LS4. If the scale datum lives in a side object rather than
the mixed comb-continuum trace object, docs 79 and 86 block promotion.

Thus `METEQ_late` cannot pass A1 and cannot license an S2 witness. QED.

## 4. Consequence For METEQ-A1

METEQ-A1 is narrowed.

The following no longer count as live S2 construction work:

```text
bare Shv(S^1) or localizing-invariant traces with metric labels;
ordinary Poisson/Haar normalization by log p;
object-level metric non-isomorphism without trace-domain detection;
density data appended after trace;
kernel traces determined only by theta/count/Poisson shadows.
```

The live target is:

```text
METEQ-DETECTED.
There exists an enriched circle trace package (O_l, D_l, Tr_l) such
that the metric/equivariant/liquid/density/kernel scale carrier is a
hypothesis of the trace domain or trace theorem, the deletion
l -> m changes the frozen trace domain or value before evaluation, and
the same structure can enter a future same-form LS4 object.
```

METEQ-DETECTED would still advance only A1/G60.2/LT76.1.

## 5. Updated Landing For Q134.4

Current Q134.4 status:

```text
METEQ-A1:
  SHARPEN.
```

The sharpened target is:

```text
METEQ-DETECTED.
```

Answer landing:

```text
PASS:
  Name O_l, D_l, Tr_l, the trace-detected enriched carrier, and the
  deletion theorem showing l -> m changes the frozen trace domain or
  value before evaluation.

KILL:
  Prove every METEQ-DETECTED attempt in a named class factors through
  B_l, forgets enrichment before trace, inserts scale late, or cannot
  feed same-form LS4.

SHARPEN:
  Name the exact enriched trace-domain theorem or factor-through
  obstruction deciding METEQ-DETECTED.
```

## 6. What This Does Not Kill

This no-go does not cover a proposal that supplies:

```text
1. an enriched object O_l whose distinguishing data are trace-visible;
2. a trace domain D_l whose hypotheses depend on l before evaluation;
3. a frozen trace value or traceability theorem changing under
   l -> m;
4. no post-trace scale insertion;
5. a path to use the same enriched structure in LS4.
```

Such a proposal returns to docs 81, 84, 85, 86, 88, 90, and 114 as an
A1 candidate.

## 7. Witness Rule

No S2 witness is licensed.

A deletion witness becomes meaningful only after METEQ-DETECTED names a
concrete `(O_l, D_l, Tr_l)`. Then the witness may freeze the trace
domain and replace `l` by `m` before evaluation. Until then, numerical
Poisson or Haar-normalization checks are calibration only.

## 8. Board Update

```text
S2:
  METEQ_late rejected or held by trace-detection status.
  METEQ-A1 sharpened to METEQ-DETECTED.
  S2 remains HOLD_A1.
  No S2 witness licensed.
```

## 9. Relation To Existing Docs

```text
doc 80
  Supplies the late scale insertion no-go.

doc 82
  Supplies the factor-through scale-collapse no-go.

doc 85
  Supplies the trace-detection requirement.

doc 133
  Named METEQ-A1. Doc 138 sharpens it to METEQ-DETECTED.

doc 134
  Follow-up board. Q134.4 should now dispatch METEQ-DETECTED, not
  generic enriched-circle notation.
```

## 10. Post-doc-146 Escape Clause

Doc 146 makes the immediate live escape:

```text
METEQ-MINTRACE.
```

Do not write another generic late-scale no-go unless a named
(O_l,D_l,Tr_l) formalism collapses by theorem. The next METEQ work
should decide whether the frozen trace domain, traceability theorem, or
trace value changes under l -> m before evaluation.
