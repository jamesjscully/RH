# 70 - Gram diagnostic normal form

Status: proof lemma / gate hardening, 2026-06-11. This isolates the
reusable content behind doc 58: max-Gram, Lorentzian signature, and
stress-flow packages can be strong diagnostics, but they are one
observable package until separate P3 and BC13 data are supplied.

## 1. Purpose

Doc 58 is the broad insufficiency gate. This document extracts the
normal form so future proposals do not re-promote Gram shape,
signature flow, stress margins, or ku/max faces as independent
`Count`, native `H_odd`, or full-cone positivity.

The issue is not whether a Gram package is useful. It often is. The
issue is role discipline:

```text
Gram package alone
  => shape / supply / diagnostic / index-side data;

Gram package + independent Count/H_odd/Compare
  => possible P3 candidate;

Gram package + full native positivity/exhaustion theorem
  => possible BC13 candidate.
```

## 2. Normal Form

Let a candidate supply a package

```text
G = (N, Gram, signature, stress flow, jump loci, margins).
```

The package is in Gram diagnostic normal form if its promoted role is
classified by the following tests.

```text
NF70.1 Source audit
  Every claimed decision observable is either a function of G or is
  supplied by a separately named structure.

NF70.2 P3 separation
  If G is used toward the final second evaluation, the proposal names
  D_Count, D_I, Count, I, H_odd, and Compare satisfying doc 65.

NF70.3 No Gram self-supply
  Gram eigenvalues, stress thresholds, jump loci, deformation
  parameters, scales, signatures, and inertia changes are not counted
  as H_odd eigenvalues unless a carrier/slot supplies them before the
  Gram action or deformation is chosen.

NF70.4 No Gram re-reading as Count
  A second formula for a Gram entry, determinant, signature, Schur
  complement, margin, or stress response is not Count unless it has a
  different natural extension domain and a contentful Compare theorem.

NF70.5 BC13 separation
  If G is used toward positivity, the proposal separately states the
  doc 67 package: native nonnegative value, candidate-native unit, full
  graph-cone exhaustion, and uniform support-filtration persistence.
```

If only NF70.1 is present, the result is supply or diagnostic data.
NF70.2-NF70.4 are needed for P3 promotion. NF70.5 is needed for BC13
promotion.

## 3. Lemma

### Lemma 70.1

Assume all claimed `Count`, `H_odd`, eigenvalue, comparison, or
positivity data are functions of one Gram/signature/stress package
`G`, its determinant algebra, its deformation parameters, or its
stress-flow definitions. Then `G` alone does not supply doc 45 E1-E4
or D1-D4.

### Proof

For E1, doc 45 requires Count and I to have different natural
extension domains. If both are functions or presentations of `G`, then
their natural source is the same package. A second formula for a Gram
entry, determinant, signature, Schur complement, or stress response is
a re-reading of `G`, not an independent Count domain. E1 fails.

For E2/E3, doc 45 requires a nonzero odd slot whose eigenvalues are
supplied by the carrier/slot before the acting map queries them. Gram
eigenvalues, stress thresholds, jump loci, deformation parameters,
scales, and signatures are spectral data of the tested observable or
of its deformation. They are supplied by the Gram action being read.
They are not an unforced odd slot. E2/E3 fail unless a separate
carrier/slot supplies `H_odd`.

For E4, a contentful Compare theorem must use mathematics beyond the
definitions of Count and I. If the comparison is determinant algebra,
a Schur identity, a signature theorem, or a stress-flow definition
inside `G`, it is a theorem about the index-side package, not a
comparison with an independently supplied Count. E4 fails.

For D1-D4, a Lorentzian or max-Gram shape does not by itself provide a
native nonnegative value on the full Sonin/Frobenius-graph core. If the
proved domain is a face, finite panel, tower, or max-Gram family, doc
67 applies: a full-cone exhaustion theorem and uniformity theorem are
still missing. If the sign depends on a chosen unit or repair, docs 55
and 66 apply independently.

Thus `G` alone remains diagnostic or supply data. QED.

## 4. Caveats

This document does not reject Gram mathematics. It preserves its
correct uses.

```text
allowed supply
  Exact max-Gram formulas, ku-face inequalities, Lorentzian windows,
  and stress flows may be theorem-grade supply constraints.

allowed diagnostics
  Jump loci, depth walls, density response, unpaid atoms, Schur
  complements, and discriminants may diagnose where a candidate pays
  or fails.

allowed compatibility checks
  A future independent Count/H_odd/Compare package must be compatible
  with the banked Gram constraints.

not enough
  None of those uses alone supplies P3 independence or BC13
  exhaustion.
```

Passing NF70 also does not prove RH. It only prevents a diagnostic
package from being misclassified.

This also does not rule out a future carrier whose native index form is
Gram-like. It rules out only promotion when the alleged second
evaluation, spectrum, or comparison is re-read from the same Gram
observable. The E-side P3 factorization failure and the D-side BC13
exhaustion failure are independent failures and should be audited
separately.

## 5. Relationship To Existing Gates

```text
doc 45
  Defines D1-D4 and E1-E4.

doc 58
  Gives the broad max-Gram/signature/stress-flow insufficiency gate.

doc 65
  Supplies the P3 independence normal form for Count/H_odd/Compare.

doc 67
  Supplies the BC13 exhaustion normal form for full-cone positivity.

doc 69
  Supplies the zero-free freeze normal form; zero-side tuning cannot
  turn a Gram diagnostic into H_odd or Compare.
```

The resulting admission rule is:

```text
No Gram/signature/stress package is P3 or BC13 by re-reading itself.
For P3, it must add independent Count/H_odd/Compare.
For BC13, it must add full native positivity/exhaustion data.
```

## 6. Live Diagnostic Target

A surviving Gram-origin proposal must state:

```text
T_G70 role declaration
  Is G being used as supply, diagnostic, P3 evidence, BC13 evidence,
  or a compatibility check?

T_G70 P3 theorem
  If P3, name the independent Count domain, native odd slot, unforced
  eigenvalue supplier, and contentful Compare theorem.

T_G70 BC13 theorem
  If BC13, name the native nonnegative value, candidate-native unit,
  full graph-cone exhaustion theorem, and uniformity theorem.

T_G70 freeze rule
  If any zero-side comparison is used, it occurs only after the
  zero-free freeze record.
```

Without these statements, additional Gram/signature/stress witnesses
should be classified as supply calibration or fail-closed diagnostics,
not as candidate evidence.
