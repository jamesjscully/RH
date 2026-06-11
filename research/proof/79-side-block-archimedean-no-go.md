# 79 - Side-block archimedean no-go

Status: proof lemma / A4 hardening, 2026-06-11. This isolates the
reusable failure mode where a proposal adds an archimedean term beside
the banked comb instead of coupling comb and continuum on one
index/Gram/count form.

## 1. Purpose

Docs 45, 54, 57, 68, and 76 all reject side archimedean blocks. This
document states the normal form so future A6/B1 proposals can be
classified without rerunning examples.

The target clause is doc 45 A4:

```text
The trace must couple comb and continuum on the same index/Gram form.
A separate positive archimedean block is the wrong shape.
```

## 2. Side-Block Normal Form

A proposed trace or kernel is a side-block trace if it has the form:

```text
T(C) = T_bank(C) + T_arch(R/T)
```

or more generally:

```text
T(C) = F(T_bank(C), T_arch(R/T))
```

where:

```text
1. T_bank depends on the finite-place comb, valuation tower, or banked
   count data;

2. T_arch depends on the archimedean real/circle object, density,
   Gaussian, determinant, or regularized continuum term;

3. there is no single domain object or trace-class correspondence on
   which b(comb_C) and R/T are paired before evaluation;

4. changing the carrier while holding the archimedean side fixed does
   not make the trace/coupling unformable at the mixed object level.
```

The most common examples are:

```text
banked comb value + positive archimedean correction;
p-complete trace + later complex determinant;
finite-place count + separately normalized Gaussian integral;
theta/Poisson term + continuum density term;
regularized determinant whose archimedean normalization is appended
after the carrier trace is computed.
```

Operational test:

```text
If deleting T_arch leaves the bank object intact, and deleting T_bank
leaves a meaningful archimedean correction, the proposal is decomposed
side-block data unless a separate mixed trace object is named.
```

## 3. Lemma

### Lemma 79.1

If a proposed B1/A6 trace has side-block normal form, then it does not
satisfy doc 45 A4, doc 54 Q3, G60.5, or LT76.5.

### Proof

Doc 45 A4 requires a trace coupling, not two separately evaluated
terms. The banked comb and the continuum must meet inside one
index/Gram/count object before trace evaluation.

In side-block normal form, the bank side and archimedean side are
computed on separate domains:

```text
C -> T_bank(C),
R/T -> T_arch(R/T).
```

The final operation `+` or `F` combines values after the two pieces
already exist. It therefore does not define the mixed object required
by A4. It is a readout, correction, or normalization, not an LS4
comb-continuum trace.

Doc 54 Q3 asks for the actual map or trace expression coupling
`b1(comb_p)` and the continuum `R` object on the same form. A
side-block expression has no such map. Thus Q3 fails.

G60.5 and LT76.5 are the operational versions of the same condition:
the trace must pair the banked comb and continuum on one same-form
object. Since the side-block expression pairs only after evaluation,
it fails both.

Therefore side-block traces fail A4/LS4. QED.

## 4. Promotion Overclaims

The A4 failure is independent of later D/E failures, but side blocks
often try to supply those clauses too. Apply these additional gates.

```text
Positivity claim
  If the side block supplies positivity, it cannot certify doc 45 D
  without doc-67-grade native nonnegative value, candidate-native unit,
  full-cone exhaustion, and support-filtration uniformity.

Count or Compare claim
  If the side block supplies Count or Compare, it fails doc 45 E1/E4
  unless it has a natural extension domain independent of the bank
  object and a contentful comparison theorem.

Eigenvalue claim
  If the side block supplies eigenvalues, it fails doc 45 E3 when
  those eigenvalues are determined by the acting map, scale,
  regularization variable, or correction term.
```

## 5. Carrier-Guard Consequence

A side-block trace also cannot pass the B1 carrier-selectivity test
unless the mixed domain is separately supplied.

For the Epstein replacement `Q=x^2+5y^2`, the theta/count side may
remain meaningful. If the archimedean side is independent and the
bank side is a generic theta/count/Poisson shadow, the expression still
computes. That is doc 53/doc 74 carrier blindness.

If the bank side uses valuation/depth data and dies for Epstein, the
proposal may pass the B2/B3 death point, but it still fails A4 unless
the archimedean continuum is coupled to that valuation/depth domain
before evaluation.

Thus:

```text
carrier death alone is not same-form coupling;
same-form coupling requires one mixed trace domain.
```

## 6. Caveats

This lemma does not forbid decompositions after a same-form theorem is
proved. A valid trace could be computed by a formula that later
decomposes, provided the construction first supplies:

```text
1. a mixed trace-class object or correspondence;
2. a same-form index/Gram/count codomain;
3. a theorem deriving the decomposition from that mixed object.
```

The lemma rejects only cases where the side-block expression is the
definition of the candidate.

It also does not reject ordinary archimedean calibration. It rejects
promotion of calibration to B1/A6 without a mixed trace domain.

It does not prove NO76.1, NO76.2, NO76.4, or NO76.5 broadly. A
p-complete-origin hybrid can escape this side-block no-go only by
satisfying NF68.1-NF68.3.

## 7. Relationship To Existing Gates

```text
doc 45
  A4 states the same-form trace-coupling requirement.

doc 54
  Q3 rejects archimedean blocks added beside the bank.

doc 57
  Pure p-complete constructions fail A4 when the archimedean term is a
  separate determinant, regularization, or correction.

doc 68
  NF68.3 states that same-form LS4 coupling is required.

doc 67 and doc 65
  Govern D-side positivity/exhaustion and E-side Count/Compare
  overclaims by side-block data.

doc 76
  LT76.5 asks for the same-form codomain; NO76.3 is the side-block
  no-go target.
```

The resulting rule is:

```text
No B1/A6 trace may be admitted if the archimedean contribution is only
an external summand, correction, determinant readout, or normalization
beside the banked comb.
```

## 8. Expert Packet Consequence

When using doc 77, classify an answer as:

```text
KILL/NO76.3
  if it proves that all available archimedean contributions are side
  blocks under the required functoriality.

DEMOTE
  if it merely supplies a side-block formula.

SHARPEN
  if it identifies the missing mixed trace-class object whose
  existence would decide whether the side-block can be promoted.
```
