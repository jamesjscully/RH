# 65 - P3 independence normal form

Status: proof lemma for docs 52 and 60, 2026-06-11. This isolates the
second-evaluation criterion from YY/ZZ into a reusable normal form.

## 1. Purpose

Doc 45 clause E requires:

```text
E1 different natural extension domains;
E2 nonempty odd slot;
E3 unforced odd-slot eigenvalues;
E4 contentful agreement theorem.
```

Doc 52 turns transport and self-supplied spectra into a broad no-go.
This document gives the local normal-form lemma behind that gate.

## 2. Definitions

Let a proposed candidate supply:

```text
Count : D_Count -> V;
I     : D_I     -> V;
N     subset D_Count and D_I;
Compare: Count(n) = I(n) for n in N.
```

`Count` and `I` are P3-independent only if:

```text
P3-a extension asymmetry
  D_Count and D_I are natural domains larger than N, and neither is
  obtained from the other by natural isomorphism, functorial transport,
  regularization, or change of presentation.

P3-b content
  Compare uses mathematics beyond the definitions of Count and I.

P3-c decision spectrum
  The agreement constrains a nonzero odd determinant/cohomology/
  spectral slot whose eigenvalues are supplied by the carrier/slot,
  not by the acting correspondence.
```

This is the YY criterion in proof-track form.

## 3. One-Evaluation Normal Form

A claimed two-evaluation package is one evaluation if it has the form:

```text
data D
  -> presentation A(D)
  -> presentation B(D)
  -> formal equality A(D) = B(D).
```

The formal equality may be:

```text
natural isomorphism;
Poisson/Fourier transport;
Pontryagin duality;
inverse-limit/colimit bookkeeping;
coker=det algebra;
TP/TR/Witt transport;
Euler-Maclaurin or zeta regularization;
two presentations of one determinant, trace, theta, or series.
```

In this normal form the natural extension domain is `D`. The apparent
two sides move together under deformation of `D`, or fail together, or
are only two readings of the same object. Therefore P3-a fails.

## 4. Proof Of The Transport Lemma

Assume `Count` and `I` are connected by functorial transport:

```text
Phi: D_Count ~= D_I
I(Phi(x)) = Count(x)
```

or by a regularization/presentation rule internal to one object `D`.
Then the agreement locus is not cut out by independent structures. It
is all of the transported domain, or the part where the same formal
operation is defined.

Any deformation of the source object induces both sides by the same
transport. Thus there is no deformation direction in which one
evaluation remains naturally defined while the other is absent,
unchanged, or outside its domain for structural reasons.

This contradicts P3-a. Hence transport packages are one evaluation.

## 5. Proof Of The Formal-Agreement Lemma

Assume `Compare` is a definitional equality, naturality square,
determinant rewrite, product formula on defining data, or regularizing
rule. Then the proof of `Compare` consumes no mathematics beyond the
definitions and formal operations used to define the two sides.

This contradicts P3-b. Hence formal agreement is not a contentful
second-evaluation theorem.

## 6. Proof Of The Self-Supply Lemma

Assume the odd-slot spectral parameter is:

```text
degree of the acting map;
Adams weight;
Frobenius scalar chosen in the action;
scale parameter;
regularization variable;
Gram/stress eigenvalue of the tested observable;
zero-side imported ordinate.
```

Then the acting correspondence, test deformation, or external import
supplies the parameter it is supposed to query. The carrier/slot has
not supplied an independent eigenvalue before the action is chosen.

This contradicts P3-c and doc 45 E3. Hence acting-degree and
self-supplied spectra are not decision-grade odd slots.

Doc 70 applies this self-supply lemma to max-Gram, signature, and
stress-flow packages: Gram eigenvalues, stress thresholds, and jump
loci do not become `H_odd` merely by re-reading the same observable.

## 7. Empty-Spectrum Lemma

Assume `H_odd = 0`, is absent, or has no nontrivial spectral parameter.
Then no agreement theorem can constrain an odd-slot eigenvalue. Even if
P3-a and P3-b hold, the result is an embryo rather than a decision-grade
second evaluation.

This is the finite-field Quillen/Hesselholt pattern in YY: the two
evaluations exist, and the agreement is a theorem, but the point has no
unforced odd spectrum for RH-grade content.

## 8. Decision-Grade Escape

A candidate escapes this normal-form no-go only if it supplies all of:

```text
E1 two larger domains
  D_Count and D_I are independently natural and strictly larger than
  their agreement locus N.

E2 deformation separation
  There are admissible deformations showing one side's native domain
  can vary, persist, or fail independently of the other.

E3 contentful comparison
  Compare is a theorem using mathematics not already present in the
  definitions of Count and I.

E4 nonzero odd slot
  H_odd is nonzero.

E5 unforced eigenvalues
  H_odd eigenvalues are supplied by the carrier/slot before the acting
  correspondence is chosen.
```

Only this package is P3-decision-grade.

## 9. Relation To Banked Examples

This lemma explains the existing classifications without re-running
them.

```text
Poisson/theta pairs
  One Fourier object in two coordinates; P3-a fails.

coker=det
  Linear algebra on one endomorphism; P3-a and often P3-b fail.

TR_0 = W and TP/TR/Witt transport
  Natural functor-level transport; P3-a fails.

solenoid Lefschetz
  Count/trace agreement uses Pontryagin/inverse-limit transport, and
  H^1 eigenvalue is the acting degree; P3-a and P3-c fail.

finite-field Quillen/Hesselholt
  P3-a and P3-b hold at embryo grade, but the odd slot is empty or the
  spectrum is forced; P3-c fails for the RH target.

zero import
  The external zero side supplies the spectral parameter; P3-c and the
  freeze protocol fail.
```

## 10. Program Consequence

Doc 52 can now be read as an application of this normal-form lemma:

```text
transport comparison => one evaluation;
formal agreement => no contentful Compare;
empty/forced/self-supplied spectrum => no decision-grade H_odd.
```

A future candidate should not be scored by the number of formulas it
has for one value. It should be scored by extension-domain asymmetry,
content of the agreement theorem, and unforced odd-slot spectrum.
