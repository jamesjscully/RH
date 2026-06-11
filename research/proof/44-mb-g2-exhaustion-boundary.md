# 44 - M-B g2 exhaustion boundary

Status: 2026-06-11. Resolves the doc 40/41 move M-B against current
evidence. The conclusion is not a new survivor or a new numerical
probe. It is the applicability boundary: the only banked g2 probe is
the NN strict-face/Frobenius-graph test, and it is already closed
negatively. A genuine M-B remains meaningful only after a real
liquid/index candidate exists.

Witness rerun in this session:

```text
python3 -m scripts.numerics.witness.prime_nn_graph_class_index
```

Exit 0. Freeze reproduced:

```text
e942ab9eb1c0d77ecd3dc7bb7da0859b87a276af3761267c8848fb1eae6d942a
```

## 1. What g2 Means

AC defines the gaps in the implication from a second evaluation to RH:

```text
g1 positivity
  The second evaluation must be forced nonnegative.

g2 class coverage / exhaustion
  The forced-nonnegative family must span the doc-00 filtration core,
  equivalently HH's Frobenius-graph cone.

g3 uniformity
  The coverage must hold uniformly along the infinite support
  filtration.
```

BC13 is precisely `g1 + g2/g3`:

```text
index positivity + class/scale exhaustion.
```

So M-B is not "check another margin sign." It is: given a candidate
with its own unit and forced-positive index/Gram evaluation, decide
whether that positive family exhausts the full Frobenius-graph cone.

## 2. Banked Probe: NN

NN tested the only available concrete proxy:

```text
strict-square / LL unit-repaired index inequality
extended verbatim to HH's Frobenius-graph classes.
```

The test is valid as a kill of that proxy. It is not a test of a
future liquid/index candidate, because:

```text
1. The unit is hand-inserted, not derived.
2. The target is the strict square / graph dictionary, not a
   liquid-metized carrier with its own unit.
3. M-A later shows Gaussian deep-cell phase data is unit-slot data.
```

## 3. Rerun Result

The current-worktree rerun reproduces NN's verdict:

```text
(N-c) WRONG FACE.

k=1 prime-atom steps:
  fail always, m+ ~ -e^{-a}/2.

(p;2), p >= 5:
  fail recurrently; onset at window entry 2 log p; recurrence period
  log p^2; breakage map is comb-determined.

strict sub-cone:
  1 admissible negative among 109 resolved classes:
  (11;2)@4.96 = -2.214249e-3.

rung towers:
  hold on the tested tower classes, but margins do not track tau.

tau comparison:
  identification fails; Spearman(m+, 1-tau) = -0.499.

zero comparison:
  no shock; z < 3 at gamma_1..5; breakage is not zero-positioned.
```

This proves:

```text
The strict-family unit-repaired inequality does not exhaust the
Frobenius-graph cone.
```

It does not prove:

```text
No liquid/index carrier can satisfy BC13.
```

## 4. Interaction With M-A

Doc 43 changes how the NN result should be used. NN's named Gaussian
deep cell `(11;2)@4.96` is a valid certificate against the verbatim
strict-face proxy, but it is not object data:

```text
AB's self-dual Hermite unit flips `(11;2)@4.96` positive.
```

Therefore the lasting NN content is not the particular Gaussian cell.
The lasting content is:

```text
1. strict-face extension fails;
2. hand-inserted atom does not supply the continuum unit;
3. k=1 boundary failure and depth-wall behavior force the unit to be
   class- and scale-coupled;
4. any future BC13 test must use the candidate's own unit and the full
   graph cone.
```

## 5. M-B Verdict

M-B has two parts, now separated.

```text
M-B(strict proxy)
  DONE. NN kills the strict-square / hand-inserted-unit extension to
  Frobenius-graph classes. This is a banked no-go.

M-B(live candidate)
  NOT RUNNABLE YET. M-C found no banked carrier passing BC-E3'/BC13,
  and M-A removed Gaussian deep-cell phase as object data. There is no
  current liquid/index candidate with its own unit on which to test
  full class/scale exhaustion.
```

This is not a blocker to characterization. It is part of the
characterization: BC13 cannot be certified by recycling the strict face,
the ku face, max-Gram signatures, or Gaussian deep phases. Doc 67 is
the reusable exhaustion normal form extracted from this boundary; it
replaces rerunning NN-style strict-face probes as the first D-side
admission test.

## 6. Updated Characterization

After M-B, the missing structure must include:

```text
candidate-native unit
  The graph-cone test must be run with the candidate's own unit and
  covariant slot data.

forced-positive index/Gram
  Nonnegativity must come from dimension/count/Gram/index structure,
  not from a signed trace or a hand-inserted repair atom.

full graph-cone exhaustion
  The class family must include the k=1 boundary, deep graph steps,
  mixed towers, and the real/conic directions needed by doc 00; tested
  margins must not be a strict-family-only statement.

independent odd-slot evaluation
  Exhaustion alone is insufficient unless the comparison is a genuine
  P3-grade second evaluation with unforced odd-slot eigenvalues.
```

The compact current statement is:

```text
Find a liquid/metrized Euler-product carrier with a candidate-native
unit such that a forced-nonnegative Frobenius-index/Gram comparison
exhausts the full Sonin/Frobenius-graph cone and is independently
evaluated by a nonempty odd spectral slot whose eigenvalues are not
supplied by the acting correspondence.
```

No banked object satisfies this. The strict-face g2 proxy is killed;
the live M-B awaits the construction of the missing carrier.
