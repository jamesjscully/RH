# 93 - S3 free-weight kernel no-go

Status: proof lemma / S3 no-go, 2026-06-11. This hardens docs 73-75
by ruling out the next broad false-positive class after generic
theta/Poisson kernels: kernels that read carrier depth but use
externally supplied weights, windows, bilinear forms, or stress
parameters as the load-bearing coupling.

Equivalently, this is the valuation-decoration collapse no-go: merely
mentioning `(alpha, v, depth, ell, mu_C)` is not enough if the trace
does not derive the form that reads those fields.

## 1. Purpose

Doc 74 rejects kernels that factor only through theta/count/Poisson or
generic discrete-measure shadows. Doc 75 leaves several HOLD ansatz
classes because they mention valuation/depth data:

```text
A1 depth-weighted one-place comb;
A2 two-place valuation-vector kernel;
A5 depth-wall stress kernel;
conditional A4 determinant/coker kernel with carrier-depth domain.
```

These can escape the doc-74 carrier-blindness lemma in a weak sense:
the formula may be unformable for Epstein represented norms because
Epstein has no distinguished atom or unique tower coordinate. That is
not enough for B1. B1 also requires the same-form LS4 coupling and
candidate-native source of all load-bearing forms.

This document proves the broad rejection criterion for free-weight S3
kernels.

## 2. Free-Weight Hypothesis

Let `K` be an S3 kernel defined on a carrier interface

```text
C = (A, alpha, v, depth, ell, mu_C).
```

Say that `K` is free-weight if its carrier-sensitive part has one of
the following forms.

```text
one-place depth weight:
  K(C, phi, w) = sum_k w(depth(k)) phi(ell(k));

two-place valuation-vector form:
  K(C_{p,q}, Phi, B) = sum_(a,b in W) B(a,b) Phi(a log p + b log q);

stress/deformation response:
  K(C, t) = stress(depth, t) or depth-wall response under a chosen t;

determinant/coker regularization:
  K(C) = det_reg(1 - T_C) or coker(1 - T_C),
  where the carrier-depth domain is present but the comparison form is
  chosen outside the candidate trace.
```

The load-bearing auxiliary data are:

```text
w, B, W, t, deformation family, determinant presentation,
regularization rule, truncation window, normalization, or codomain.
```

`K` is free-weight when those data are not derived by a named
candidate trace theorem and are not forced by one same-form
index/Gram/count object in `L1` before evaluation.

## 3. Lemma

### Lemma 93.1

A free-weight S3 kernel cannot advance B1, LS4, P3, or BC13. It may at
most be decorated B0 calibration, carrier-selective calibration, or
diagnostic data.

### Proof

B1 requires all of the following before a witness:

```text
1. retained log p before trace evaluation;
2. conservative embedding of the B0 bank;
3. a same-form LS4 coupling pairing the banked comb and continuum on
   one named index/Gram/count object;
4. carrier/effectivity death for Epstein/DH controls;
5. zero-free freeze of all load-bearing choices.
```

A free-weight kernel may satisfy part of (4): because it reads
`alpha`, `v`, `depth`, or `ell`, the Epstein represented-norm monoid
may be unable to form the same input. But the value of the kernel is
then determined by auxiliary data such as `w`, `B`, `W`, `t`, a
regularization rule, or a codomain that is not produced by the
candidate trace.

Therefore the coupling is not the trace of `b1(comb_C)` with the
continuum on one candidate-native form. It is a carrier-dependent
readout against an externally supplied form. That fails the LS4
same-form condition of docs 54, 79, and 86.

If the free auxiliary data are later interpreted as the second
evaluation, the P3 independence gate also fails: the two values are
defined on the same carrier-readout domain or are connected by formal
transport, not by two larger natural domains and a contentful Compare
theorem as required by docs 52 and 65.

If the free auxiliary data are interpreted as positivity or
exhaustion, BC13 fails: a chosen weight, window, stress direction, or
regularization is not native forced nonnegativity over the full
Frobenius-graph cone, and docs 56, 67, and 70 apply.

Thus a free-weight kernel cannot advance B1, LS4, P3, or BC13. QED.

## 4. Corollaries For Doc 75 Ansatz Classes

```text
A1 depth-weighted one-place comb
  HOLD only if w is produced by the candidate trace and paired with R
  on a same-form object. Otherwise REJECT as free-weight calibration.

A2 two-place valuation-vector kernel
  HOLD only if W and B are native product-formula or trace objects in
  L1. Otherwise REJECT as a free bilinear/windowed carrier readout.

A4 determinant/coker/regularized kernel
  HOLD only if the determinant object has a carrier-depth domain and
  is not a free regularization. If Count/Compare is claimed, an
  independent Count/Compare theorem is also required. Otherwise REJECT
  as a regularized re-reading.

A5 depth-wall stress kernel
  HOLD only if stress is the output of the L1 trace coupling.
  Otherwise REJECT as diagnostic stress data.
```

The only surviving S3 shape is therefore not "carrier data plus an
interesting form." It must be:

```text
carrier data + candidate-native same-form trace/codomain + frozen
zero-free supplier ledger.
```

## 5. Falsification Test

Before any S3 witness, ask:

```text
F93.1 Source test
  Is every weight, window, bilinear form, deformation parameter,
  determinant presentation, regularization rule, and codomain derived
  from the candidate trace theorem?

F93.2 Same-form test
  Do the banked comb and continuum enter one mixed object before
  evaluation, or is the carrier read against an externally supplied
  test form?

F93.3 P3 test
  If Count/Compare is claimed, are there two larger natural domains
  and a contentful Compare theorem, rather than two readings of the
  same weighted carrier sum?

F93.4 BC13 test
  If positivity is claimed, is nonnegativity forced by value type over
  the full graph cone, not by a chosen weight/window/stress direction?

F93.5 Freeze test
  Were all auxiliary data fixed by zero-free suppliers before any
  zero-side comparison?
```

Any `no` answer to F93.1, F93.2, or F93.5 blocks witness construction.
F93.3 blocks only Count/Compare promotion; F93.4 blocks only
positivity or BC13 promotion. B1 may leave those promotion fields open
under doc 60.

## 6. Relation To Existing Docs

```text
doc 73
  Preregisters S3 and requires K_B1 before any witness.

doc 74
  Rejects generic theta/count/Poisson kernels.

doc 75
  Lists the A1-A6 ansatz classes; this document resolves the
  free-weight subcase of A1, A2, A4, and A5.

doc 86
  Gives the same-form LS4 ledger.

doc 91
  Gives the zero-free freeze ledger.
```

The next S3 work is now sharper:

```text
Either derive the weights/forms/codomain from a named trace theorem in
L1, or reject the corresponding S3 ansatz as free-weight calibration.
```
