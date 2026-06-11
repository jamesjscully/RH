# 97 - Monoid-functorial carrier overreach no-go

Status: proof lemma / S3 carrier-overreach no-go, 2026-06-11. This
hardens doc 94 by ruling out trace-derived-looking S3 forms whose
domain is functorial for generic commutative monoid, represented-norm,
or measure shadows.

## 1. Purpose

Doc 94 leaves a positive S3 escape:

```text
a named L1 trace theorem derives the same-form codomain F_C that reads
carrier depth.
```

This document removes a broad false-positive subcase. A form may be
trace-derived inside its formalism and still fail carrier selectivity
if the formalism is defined for any represented-norm or generic
measure shadow with the same functorial input type.

The target collapse mode is:

```text
NT94.5 carrier overreach.
```

## 2. Monoid-Functorial Hypothesis

Let an S3 proposal assign to a carrier `C`:

```text
C -> M_C -> F_C -> Tr_L(F_C).
```

Say the proposal is monoid-functorial if the construction factors
through a functorial shadow category whose objects include at least
one of:

```text
commutative monoids with a length map;
represented-norm monoids;
countable positive multisets;
positive discrete measures on R;
theta/count data;
Dirichlet coefficient multisets before Euler-product structure;
determinant/coker objects built functorially from those shadows.
```

Equivalently, the construction does not require a domain in which the
following fields are primitive and load-bearing:

```text
distinguished atom alpha;
unique valuation v;
tower/depth coordinate;
Euler-product factorization domain;
prime-power graph-depth class.
```

It may still use a trace theorem and may still produce an internal
codomain `F_C`. The issue is that the theorem is available for the
control shadow as well.

Equivalently, the construction has the shape:

```text
C -> S(C) -> M_S -> F_S -> trace/kernel value,
```

where `S(C)` forgets at least one load-bearing Euler carrier field and
the trace theorem is natural for the broader shadow functor `S`.

## 3. Lemma

### Lemma 97.1

If an S3 trace-derived form is monoid-functorial in the sense above
and its input class includes the Epstein represented-norm shadow
`R_Q` for `Q=x^2+5y^2`, then it cannot pass carrier selectivity.

### Proof

Doc 87 requires the following death profile:

```text
theta/count shadows may survive;
the first carrier-consuming map must be unformable for Epstein/DH;
the failure must occur at carrier/effectivity before signs or zeros.
```

Doc 64 proves that the Epstein replacement

```text
Q(x,y) = x^2 + 5y^2
```

has a meaningful represented-norm and theta/count shadow:

```text
1, 4, 6, 9, 36 are represented;
2, 3 are absent;
4, 6, 9 are represented-norm irreducibles;
36 = 4*9 = 6*6.
```

It also proves that this shadow has no free prime-power valuation,
distinguished atom, or unique tower coordinate.

Under the monoid-functorial hypothesis, the proposed trace object
`M_C`, codomain `F_C`, and trace value are defined from a shadow input
type that includes represented-norm or measure data. Since `R_Q` is an
object of that input type, the same construction produces

```text
M_Q -> F_Q -> Tr_L(F_Q).
```

Thus the first trace/codomain map does not become unformable for
Epstein at carrier/effectivity. It computes on the control. That is
exactly doc-87 `REJECT_CARRIER_BLIND` and doc-94
`REJECT_CARRIER_OVERREACH`.

Therefore a monoid-functorial trace-derived-looking S3 form cannot
pass carrier selectivity. QED.

## 4. Consequences

This no-go applies even if:

```text
the codomain F_C is internally produced by the trace formalism;
the form is not an externally chosen weight;
the construction is natural;
the result has a determinant, index, Gram, or count interpretation.
```

Those facts can escape doc 93, but they do not escape carrier
overreach if the same formalism accepts the Epstein shadow.

This is not `REJECT_FREE_WEIGHT`. The trace-derived form may be real.
The failure is that its naturality domain is too broad, so the same
trace/codomain still computes for controls.

The only surviving S3 escape must name a trace domain where:

```text
1. the carrier fields are primitive in the domain;
2. the first map consuming them is written;
3. represented-norm controls have theta/count shadows but no object in
   that carrier-consuming domain;
4. DH controls fail for the same structural reason or are explicitly
   outside the domain.
```

## 5. Falsification Test

Before recording `PASS_TRACE_DERIVED` or `PASS_CARRIER`, ask:

```text
F97.1 Input type
  What is the input category of the trace theorem?

F97.2 Control inclusion
  Does the input category include represented-norm monoids, positive
  multisets, theta/count data, or positive measures?

F97.3 First carrier map
  Which first map requires alpha, v, depth, ell, or Euler-product
  factorization as primitive data?

F97.4 Epstein object test
  Can R_Q for Q=x^2+5y^2 be fed into that same first map?

F97.5 DH object test
  Can a DH-type coefficient or measure shadow be fed into that same
  first map?
```

If F97.2 is yes and F97.4 or F97.5 is yes, record
`REJECT_CARRIER_OVERREACH` for doc 94 and
`REJECT_CARRIER_BLIND` for doc 87.

Core quick test:

```text
Can the same trace theorem and codomain be applied to the Epstein
represented-norm monoid after replacing prime powers by values of
x^2+5y^2?

YES
  Carrier overreach.

NO
  Name the first Euler-carrier field or map that becomes unformable.
```

## 6. Relation To Existing Docs

```text
doc 64
  Supplies the Epstein represented-norm obstruction.

doc 74
  Rejects generic kernels factoring through shadows.

doc 87
  Gives the carrier-selectivity ledger.

doc 93
  Rejects free-weight valuation decoration.

doc 94
  Names carrier overreach as a negative S3 theorem target.

doc 98
  States the surviving strict Euler-carrier trace-domain target after
  this overreach no-go.

doc 107
  Extracts the shared carrier-overreach meta-lemma behind this no-go,
  doc 100, and doc 105.
```

The next positive S3 answer must therefore be stronger than:

```text
the trace derives an internal codomain.
```

It must also prove:

```text
the trace domain excludes represented-norm and DH controls at the
first carrier-consuming map while preserving their theta/count shadows
as controls.
```
