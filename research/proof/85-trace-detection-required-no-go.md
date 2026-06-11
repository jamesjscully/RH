# 85 - Trace detection required no-go

Status: proof lemma / A1 false-positive guard, 2026-06-11. This
prevents object-level enrichment from being mistaken for scale
retention when the load-bearing trace forgets that enrichment.

## 1. Purpose

Doc 84 asks for a non-factorization theorem. One tempting weak answer
is:

```text
O_l and O_m are non-isomorphic enriched objects.
```

That is not enough for A1. The candidate must prove that the
trace-domain theorem, trace value, or same pre-trace structure used by
the load-bearing trace detects the non-isomorphism before evaluation.

This document records the no-go:

```text
non-isomorphic enriched objects do not advance scale retention if the
trace forgets the enrichment.
```

Equivalently, doc 84's NF84.A must be read as trace-detected
non-isomorphism, not object-level non-isomorphism alone.

## 2. Trace-Forgotten Normal Form

A proposed scale-retention claim is in trace-forgotten normal form if
it has:

```text
1. enriched objects O_l, with O_l not isomorphic to O_m for l != m;
2. a trace domain D_l and trace/invariant Tr_l;
3. a forgetful or comparison functor U_l from the enriched data to a
   trace-visible domain E_l;
4. a trace value determined by U_l(O_l);
5. natural identifications U_l(O_l) ~= U_m(O_m) for all l,m > 0.
```

Equivalently, enrichment exists before trace, but the trace only sees
its scale-blind image.

## 3. Lemma

### Lemma 85.1

If a proposed A1/LT76.1 claim is in trace-forgotten normal form, then
it does not satisfy doc 81 `PASS_A1`. Its verdict is `REJECT_A1` if
the trace-visible image factors through doc 82's `B_l`, and otherwise
`HOLD_A1` until trace detection is proved.

### Proof

The load-bearing trace value is determined by `U_l(O_l)`. By
hypothesis, the trace-visible images are naturally identified:

```text
U_l(O_l) ~= U_m(O_m).
```

Therefore the frozen trace value cannot distinguish `l` from `m`:

```text
Tr_l(O_l) = Tr_m(O_m)
```

through the data actually seen by the trace. The object-level
non-isomorphism of `O_l` and `O_m` is not load-bearing for the
candidate trace.

By doc 81, the deletion test requires the frozen trace, trace domain,
or trace-relevant enriched object to change when `l` is replaced. A
change only in data forgotten before trace does not pass that test. If
the trace-visible image is the bare scale-blind object `B_l`, doc 82
gives `REJECT_A1`. If the image is not known to be `B_l` but trace
detection is unwritten, the honest verdict is `HOLD_A1`. QED.

## 4. Diagnostic Tests

Apply these tests to every non-factorization claim.

```text
D85.1 Object test
  Are O_l and O_m non-isomorphic in the proposed enriched category?
  If no, doc 84 cannot pass by NF84.A.

D85.2 Trace-domain test
  Does the trace theorem require the enriched datum that distinguishes
  O_l from O_m?

D85.3 Value test
  Is Tr_l(O_l) proved to change, or is the trace value otherwise
  proved not to be determined by a scale-blind image?

D85.4 Forgetful test
  List every functor used before trace. If any functor forgets the
  distinguishing datum and the trace is computed after that functor,
  the object-level non-isomorphism is not enough.

D85.5 Same-form test
  If the trace detects scale, is that same scale-detecting structure
  also the one used for comb-continuum coupling? If not, A1 may hold
  while LS4 still fails.
```

## 5. What This Kills

```text
K85.1 Decorative enrichment
  The candidate equips the circle with metric/liquid/equivariant data,
  but the trace first forgets to bare topology, bare sheaves, or a
  localizing-invariant output.

K85.2 Trace-insensitive parameters
  The parameter l appears in the object definition, but all trace
  hypotheses and trace values are invariant after forgetting it.

K85.3 Non-isomorphic side data
  A side object depends on l, while the load-bearing trace is computed
  on a separate scale-blind object.

K85.4 Value-free non-factorization
  A no-factor-through functor is asserted at object level, but no
  trace-domain or trace-value consequence is proved.
```

These classes should not trigger a witness cycle.

## 6. What Remains Live

The lemma does not kill a candidate that proves any of:

```text
L85.1 trace-domain detection
  The traceability theorem fails, changes, or has different hypotheses
  after forgetting the enriched scale carrier.

L85.2 trace-value detection
  The frozen trace value changes with l before post-processing.

L85.3 no trace-visible factorization
  There is no scale-blind trace-visible image through which Tr_l is
  determined.

L85.4 same-structure detection
  The same structure that detects l is also the structure entering the
  proposed same-form LS4 coupling.
```

These are exactly the positive burdens in doc 84.

## 7. Relation To Existing Docs

```text
doc 81
  Requires the deletion test to affect the frozen trace/domain/object.

doc 82
  Rejects the stronger case where the trace-visible image is the bare
  scale-blind object B_l.

doc 84
  States the positive theorem target. This document clarifies that
  NF84.A must be trace-relevant, not merely object-level.

doc 79
  Still governs whether trace-detected scale is same-form LS4 or side
  data.
```

The operational rule is:

```text
Do not record PASS_A1 from object-level non-isomorphism alone. Record
PASS_A1 only after the trace theorem, trace domain, or frozen trace
value detects the enrichment before evaluation.
```
