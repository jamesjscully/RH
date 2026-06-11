# 74 - S3 generic-kernel carrier blindness

Status: proof lemma / S3 no-go, 2026-06-11. This hardens doc 73 by
ruling out the broad class of explicit kernels that factor only through
theta/count/Poisson or generic discrete-measure data. Such kernels may
be useful calibration objects, but they are not carrier-selective B1
couplings.

## 1. Purpose

Doc 73 leaves `K_B1` blank. Before trying to write it by trial and
error, this document removes the obvious false start:

```text
take a discrete measure or theta series;
apply a Poisson/heat/Gaussian kernel;
declare the result a comb-continuum coupling.
```

That construction is too broad. It computes for prime-power combs, but
it also computes for Epstein represented norms and other non-Euler
product shadows. Therefore it fails doc 45 B2/B3 before any numerical
or sign test.

## 2. Kernel Factorization Hypothesis

Let `K` be a proposed S3 kernel. Say that `K` is generic if it factors
through one of the following data types:

```text
finite or countable positive discrete measure on R;
multiset of positive numbers or represented norms;
theta series;
Poisson summation data;
LCA/lattice Haar-density data;
Dirichlet coefficient multiset before Euler-product structure.
```

Equivalently, `K` has the form:

```text
carrier C
  -> shadow S(C)
  -> kernel value K(S(C)),
```

where `S(C)` forgets the distinguished atom, valuation/tower
coordinate, graph depth, and unique prime-power factorization.
Equivalently, `K` does not require the frozen doc-73 carrier fields:

```text
distinguished atom alpha;
candidate-native valuation v;
unique tower/depth coordinate;
address map ell(k) = k log alpha;
```

before evaluation.

Examples include:

```text
K(mu, phi) = <mu, phi>;
heat or Gaussian smoothing of a discrete measure;
Poisson/Fourier transform of a lattice comb;
theta-kernel evaluation of represented norms;
regularized determinant or coker-det re-reading of the same shadow.
```

## 3. Lemma

### Lemma 74.1

If an S3 kernel `K` is generic in the sense above, and if the same
shadow functor `S` is defined for both the prime-power carrier and the
Epstein represented-norm replacement `Q=x^2+5y^2`, then `K` cannot pass
the S3 carrier-selectivity gate.

### Proof

The S3 gate requires the following death profile:

```text
theta/count shadow survives;
Euler-product carrier/coupling is undefined;
failure point is carrier/effectivity before signs.
```

For the prime-power carrier, the shadow `S(C_p)` is defined by
hypothesis. For the Epstein replacement, doc 64 proves that the
theta/count shadow survives:

```text
Q=x^2+5y^2 represents 1,4,6,9,36;
2,3 are absent;
4,6,9 are represented-norm irreducibles;
36 = 4*9 = 6*6.
```

Thus represented-norm theta/count data exists, even though the free
prime-power valuation/tower address does not.

Since `K` factors through only the shadow `S`, and `S` is defined for
the Epstein replacement, `K(S(R_Q))` is also defined. Therefore the
kernel does not die at carrier/effectivity. It computes on the control
input. That is exactly doc 45 B2/B3 failure and the doc 53
carrier-blindness mechanism.

Hence a generic S3 kernel is not a B1 LS4 coupling. QED.

## 4. Corollary: What `K_B1` Must Use

Any surviving `K_B1` must require at least one structure that the
Epstein represented-norm monoid cannot supply:

```text
distinguished atom alpha;
candidate-native valuation v;
unique tower/depth coordinate k;
graph-depth class;
Euler-product factorization domain;
same-form coupling whose domain is built from those fields.
```

It is not enough for `K_B1` to use:

```text
the set of represented values;
their logarithms;
a generic discrete measure;
theta coefficients;
Poisson duality;
Gaussian smoothing;
density or Haar normalization.
```

Those are shadows that Epstein can still provide.

## 5. Caveats

This document does not rule out S3. It rules out only the generic
kernel class.

```text
allowed calibration
  Generic kernels may still reproduce B0 Poisson comb behavior.

allowed negative control
  Generic kernels may be useful to demonstrate carrier blindness.

not allowed promotion
  A generic kernel cannot be called LS4 or B1 merely because it couples
  a comb-like measure to a continuum test function.

possible escape
  A kernel whose domain genuinely requires valuation/depth data and is
  unformable for Epstein remains open.
```

Passing this no-go also does not prove RH, P3 independence, BC13, or
unit threading. It only narrows the S3 construction attempt.

## 6. Relationship To Existing Gates

```text
doc 49
  Supplies the B0 Poisson comb calibration and the first executable
  Epstein guard.

doc 53
  Gives the broad carrier-blind Poisson/Epstein no-go.

doc 64
  Supplies the proof-level Epstein represented-norm obstruction.

doc 73
  Pre-registers S3 and names `K_B1` as the required blank.

doc 60 G60.1
  Requires carrier selectivity before another witness cycle.
```

The resulting S3 rule is:

```text
Do not write an S3 witness for a kernel that factors only through
theta/count/Poisson/discrete-measure data. Either write a `K_B1` whose
domain requires valuation/depth carrier data, or reject S3 as
carrier-blind.
```

## 7. Next Work

The remaining construction question is now precise:

```text
Can one write a same-form comb-continuum kernel whose domain includes
(A, v, depth, ell, mu_C) in a load-bearing way, so that replacing
prime powers by R_Q leaves theta/count alive but makes the coupling
unformable?
```

If yes, freeze it under doc 73 before writing a witness. If no, record
S3 as `REJECT: carrier-blind`.
