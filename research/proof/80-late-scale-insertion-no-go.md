# 80 - Late scale insertion no-go

Status: proof lemma / A1 hardening, 2026-06-11. This isolates the
failure mode where `log p` is added only after a scale-blind trace,
localizing invariant, or kernel value has already been computed.

## 1. Purpose

Docs 51 and 63 prove that bare sheaf/localizing-invariant circle data
forget the circumference. This document records the immediate
consequence for attempted repairs:

```text
post-processing a scale-blind value by log p is not scale retention.
```

The target clause is doc 45 A1:

```text
log p must live in metrized/liquid/analytic-ring/equivariant/kernel
data before trace evaluation.
```

## 2. Late-Insertion Normal Form

A proposed address or trace is in late-insertion normal form if it has:

```text
1. a scale-blind source value X(C_p);
2. a post-processing rule G;
3. an externally supplied scale parameter l_p = log p;
4. output Y_p = G(X(C_p), l_p).
```

Here `X(C_p)` is computed before `l_p` enters. Typical examples are:

```text
F^cont(Shv(R/(log p)Z; C)) followed by multiplying by log p;
the bare diagram (log p)Z -> R -> R/(log p)Z scaled to Z -> R -> R/Z
  and then relabeled by log p;
a p-independent trace value with 2pi/log p appended as density;
a localizing-invariant output with p-dependence inserted as notation;
a generic Poisson normalization chosen after a scale-blind trace.
```

## 3. Lemma

### Lemma 80.1

If a proposed B1/A6 address has late-insertion normal form, then it
does not satisfy doc 45 A1, G60.2, LT76.1, or the B1 scale-retention
test.

### Proof

Doc 45 A1 requires `log p` to live in the candidate address before
trace evaluation. In late-insertion normal form, the candidate first
computes:

```text
X(C_p).
```

By hypothesis, this value is scale-blind: for primes `p` and `q`,

```text
X(C_p) = X(C_q)
```

or is naturally identified by the same bare/localizing diagram. The
only p-dependence appears later as an external parameter in:

```text
Y_p = G(X(C_p), log p).
```

Therefore the trace or invariant did not retain `log p`. The
post-processing rule received `log p` from outside the candidate value
already computed. This is an external normalization or coordinate
choice, not candidate-native scale structure.

Thus the proposal fails A1. Since G60.2, LT76.1, and the B1
scale-retention test are operational versions of A1, they fail too.
QED.

## 4. Operational Reject Test

For any proposed repair that introduces `log p` late, apply this test:

```text
1. freeze the candidate immediately before log p is inserted;
2. replace log p by an arbitrary l > 0 in the pre-insertion input;
3. evaluate the frozen trace/invariant/value;
4. ask whether the frozen value changes with l.
```

If the frozen value is unchanged, then the construction is
scale-blind at the point where the candidate trace is actually
computed. If the later formula still needs `log p`, `1/log p`,
`2pi/log p`, a Haar density, metric scale, Gaussian width, residue, or
comparison constant to look prime-specific, reject it as late scale
insertion.

This test does not say the post-processing identity is false. It says
the scale entered as readout/calibration data rather than as
candidate-native A1/A4 structure.

## 5. Relation To The Bare Diagram

Doc 63 proves that the bare diagrams:

```text
lZ -> R -> R/lZ
```

are isomorphic by scaling. Consequently a candidate built naturally
from the bare localizing-invariant image of this diagram has no
internal memory of `l`. A later instruction:

```text
now set l = log p
```

does not change the computed object. It only changes an external label.

This is why the escape hatches in doc 63 require metric, liquid
analytic-ring, equivariant, density, or kernel data before the trace is
applied.

## 6. What This Does Not Kill

This lemma does not apply if `log p` is part of the input object or
trace domain before evaluation, such as:

```text
metric R with fixed length scale;
liquid/gaseous analytic-ring modules whose norms depend on log p;
equivariant traces over the group object R/(log p)Z;
density data retained in the object, not appended after;
explicit kernels using log p before trace;
same underlying spaces with non-isomorphic enriched structures.
```

Those are the live LT76.1 escape routes. They still must satisfy the
other B1 gates: same-form coupling, carrier selectivity, and
zero-free freeze.

## 7. Overclaim Guard

Late insertion can still be useful for calibration. For example, B0
uses the banked Poisson normalization:

```text
sum_n phihat(n log p)
  = (2 pi / log p) sum_k phi(2 pi k / log p).
```

That identity calibrates the p^Z address spacing. It does not prove
that a trace has retained `log p` as candidate-native structure. The
B0 witness is honest precisely because it calls this calibration, not
B1.

## 8. Relationship To Existing Gates

```text
doc 51
  Proves the scale-blind localizing-trace no-go for bare sheaves and
  continuous localizing invariants.

doc 63
  Proves the scaling naturality lemma for the full bare diagram.

doc 71
  B1 scale retention requires naming the first object carrying log p
  before trace evaluation.

doc 76
  LT76.1 requires T_C to retain log p before trace evaluation.

doc 77
  Rejection rule: answers where log p appears only as notation or a
  chosen coordinate are non-answers.
```

The resulting rule is:

```text
No proposal advances A1 by appending log p to a scale-blind trace
output. The enriched datum must be named before the trace.
```
