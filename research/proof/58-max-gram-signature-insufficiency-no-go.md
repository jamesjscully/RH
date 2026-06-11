# 58 - Max-Gram/signature insufficiency no-go

Status: insufficiency gate draft, 2026-06-11. This turns doc 48
T48.7 into a reusable gate. It rules out promoting Lorentzian
signature, max-Gram, or stress-flow certificates to a P3 second
evaluation or to BC13 unless new data are supplied. Doc 70 isolates
the reusable Gram diagnostic normal form behind this gate.

## 1. Statement

Let a proposed carrier supply a Gram or stress-flow package on a
candidate class family `N`:

```text
G_N        = Gram, max-Gram, index, or stress form on N,
sig(G_N)   = Lorentzian/signature/inertia certificate,
flow(G_N)  = jump-locus, stress, or deformation data derived from G_N.
```

Assume the package certifies one or more of the following.

```text
L1 Lorentzian shape
  The relevant form has signature (1, r), or has a controlled
  Lorentzian window under a shift/deformation parameter.

L2 max-Gram formula
  Pairings are supplied by a max kernel, norm-Gram formula, MIN/MAX
  dual kernel, or certified face such as <g_i, g_j> = c max(i,j).

L3 stress-flow response
  A flow of inertias, jump loci, Schur complements, discriminants, or
  signed margins is computed from the same Gram/index data.

L4 supply-grade arithmetic address
  The entries may contain prime-power degrees, von Mangoldt weights,
  ku-face margins, or a density tower, but only through the Gram
  package's own entries and deformations.
```

Then this package alone does not supply the doc-45 clause-E data:

```text
Count  = independent count-side evaluation,
H_odd  = nonzero odd determinant/cohomology/spectral slot,
Compare: I(n) = Count(n) on a common locus N,
```

and therefore cannot pass P3 independence. It also does not by itself
certify BC13: forced nonnegative index positivity over the full
Sonin/Frobenius-graph core with candidate-native unit and uniform
infinite-support exhaustion.

The conclusion is an insufficiency result, not a denial that the
package is useful. A max-Gram/signature certificate can certify shape,
carrier supply, window compatibility, low-rank stress facts, and
failure modes. It becomes decision-grade only when paired with new
P3-grade Count/H_odd/Compare data and a BC13 exhaustion theorem.

## 2. Hypotheses

The gate applies to any certificate satisfying the following
hypotheses.

```text
H1 Gram-derived observable
  The proposed decision observable is a function of G_N and its
  deformations: inertia, signature, eigenvalue loci, Schur
  complements, discriminants, stress margins, or max-Gram entries.

H2 no independent Count domain
  No count-side structure D_Count is named whose natural domain is
  different from the natural Gram/index domain D_I and not transported
  from it.

H3 no native H_odd
  No nonzero odd determinant/cohomology/spectral slot is supplied by
  the carrier before the acting correspondence, scale, stress
  parameter, or Gram deformation is chosen.

H4 no contentful Compare theorem
  No theorem is stated that equates an independently defined Count to
  I on a common locus using mathematics beyond the definitions of the
  Gram entries, inertia, determinant algebra, or stress flow.

H5 no full-cone exhaustion theorem
  Positivity or Lorentzian shape is proved only on a face, window,
  tower, finite panel, max-Gram family, ku face, or other named
  subfamily, with no theorem identifying it with the full
  Sonin/Frobenius-graph core.
```

H1-H4 are the E-side hypotheses. H5 is the D-side hypothesis. Either
side is enough for the corresponding demotion.

## 3. Local Dependencies

```text
doc 45 D1-D4
  The second evaluation must be forced nonnegative by native
  structure, must range over the full graph-cone core, must use the
  candidate's own unit, and must persist uniformly along the infinite
  support filtration.

doc 45 E1-E4
  P3 independence requires different natural extension domains, a
  nonempty odd slot, unforced eigenvalues supplied by the carrier, and
  a contentful comparison theorem.

doc 42 rows
  Frobenius-graph / max-Gram face is STRICT-FACE: Lambda(p^k) homes
  the prime side, but graph-class extension fails recurrently and no
  forced-positive second evaluation spans the full cone.

  ku face / two-coset comb is TRANSPORT + STRICT-FACE: theorem-grade
  supply and depth wall, but every entry has one evaluation.

  2D ku Castelnuovo posing is TRANSPORT / STRICT-FACE: Hodge-index
  shape is posing-dependent and the Weil fixed-point slot is occupied
  by Lambda - m+, not an independent spectral count.

  Norm-Gram / signature flow is CARRIER-BLIND: Lorentzian signatures
  and max-Grams are certified, but integer signature response is too
  small and density-dominated.

doc II signature flow
  The global norm-Gram flow is Lorentzian in all tested samples and
  its jump loci accumulate at log 2. The raw counting channel sees
  the expected prime-count oscillations, but the decision INT channel
  carries the smooth density tower and not the zero oscillatory layer.

doc UU ku Castelnuovo
  The 2D ku form is well-posed and Lorentzian under the override
  posing, but the shape is content-free: it holds for any positive
  diagonal. The would-be Weil slot is B' = Lambda_p - m+, a supply
  entry, not an independent trace/fixed-point evaluation.

doc 56
  Strict-face positivity, ku-face positivity, max-Gram signatures,
  finite windows, rung towers, and Gaussian slot phases must not be
  promoted to BC13 without full-cone exhaustion and P3 compatibility.

doc 52
  Transport, self-supplied spectra, empty odd slots, and formal
  agreements do not pass P3. The present gate applies the same logic
  to Gram-derived signature/stress packages.
```

## 4. Proof: No P3 Second Evaluation

Let `I` be the spectral/index value supplied by the Gram package. In
this setting `I` may be a signature, an inertia jump count, an
eigenvalue-locus statistic, a Schur complement, a discriminant margin,
or a Gram entry.

### Step 1: Gram observables define one side only

Under H1, all visible quantities are functions of the same input
package:

```text
G_N
  -> entries / max kernel
  -> inertia / signature / jump loci / stress margins
  -> I
```

This is an index-side construction. It may be exact, theorem-grade,
and useful, but it is still one native source of values. The existence
of several derived readings of `G_N` does not create a count-side
evaluation.

Thus a Gram package by itself has supplied `I`, not `Count`.

### Step 2: No independent Count domain

Doc 45 E1 requires `Count` and `I` to have different natural extension
domains. H2 says that no such `D_Count` has been named. Therefore the
package fails E1.

This is precisely the failure seen in the ku and Castelnuovo rows of
doc 42/UU. The face entries can be written exactly and can carry prime
degrees, margins, or depth windows, but the same entries are not a
separate count theorem. In UU, the slot corresponding to Weil's
fixed-point count is occupied by

```text
B' = Lambda_p - m+.
```

That is a supply entry determined by the face data. It is not an
independently defined fixed-point or trace count with its own natural
domain.

### Step 3: No native odd slot

Doc 45 E2-E3 require a nonzero odd slot `H_odd` whose eigenvalues are
supplied by the carrier before the acting map queries them. H3 says
that the max-Gram/signature package has no such slot.

Eigenvalues of `G_N`, jump loci of `G_N + tI`, and stress thresholds
are not `H_odd` in the required sense. They are spectral data of the
Gram observable itself. The flow parameter `t`, a scale parameter,
an Adams/degree parameter, or a Schur-complement threshold is not an
odd-slot eigenvalue supplied independently of the action.

Thus the package fails E2 if the odd slot is absent, and fails E3 if
the claimed spectral parameter is supplied by the Gram/stress action
itself.

### Step 4: No contentful Compare theorem

Doc 45 E4 requires a theorem

```text
Compare: I(n) = Count(n)
```

whose proof uses mathematics beyond definitions, determinant algebra,
formal transport, or the construction of `I` and `Count`.

Under H4, no such theorem is present. At most, the package proves
identities inside the Gram structure: a max-kernel formula, a
signature theorem, a Schur identity, a discriminant inequality, or a
flow law. Those can be real theorems about `I`, but they do not equate
`I` with an independent `Count`.

Therefore H1-H4 imply failure of P3 independence:

```text
Gram/signature/stress package alone
  => I-side data only
  => no independent Count, no native H_odd, no contentful Compare
  => failure of doc 45 E1-E4.
```

## 5. Proof: No BC13 By Shape Alone

BC13 is not merely the assertion that a form has Lorentzian signature
or that a favorable face has positive margins. It requires the D-side
package of doc 45:

```text
forced nonnegative value type
+ full graph-cone exhaustion
+ candidate-native unit and slot data
+ uniform infinite-support behavior.
```

### Step 1: Lorentzian shape is not forced nonnegativity

A Lorentzian signature certificate controls inertia. It does not by
itself produce a forced nonnegative second evaluation. In UU, the
override form is Lorentzian for any positive diagonal entry. That
shows the shape can be insensitive to the arithmetic size of the
margin.

Thus Lorentzian shape can support an index story, but it is not the
BC13 value type unless the candidate also identifies the native
nonnegative value and proves why it is nonnegative by structure.

### Step 2: Max-Gram faces are not full-cone exhaustion

Doc 45 D2-D4 require the full Sonin/Frobenius-graph core and uniform
support filtration behavior. H5 says the certificate is proved on a
face, window, tower, finite panel, max-Gram family, ku face, or other
subfamily without an exhaustion theorem.

Then the implication

```text
positive or Lorentzian on the max-Gram/signature family
  => positive on the full graph-cone core
```

is not available. By doc 56, that is a strict-face failure. Recurrent
graph directions, k=1 boundary atoms, mixed towers, real/conic
directions, or infinite-support behavior may be omitted or may break.

Therefore H5 implies failure of D2-D4.

### Step 3: Stress flow does not repair the unit problem

A stress flow may identify margins, jump loci, depth walls, or
degeneration toward a light cone. Those are diagnostics of the chosen
form. Unless the flow derives the candidate's own unit and covariant
slot data, it does not satisfy doc 45 D3.

In the signature-flow case, the jump-locus accumulation at log 2 is
the norm constant, not a zero position. In the ku Castelnuovo case,
the cross term is the atom-minus-margin deficit, not a trace count.
These are structural measurements of the supplied face, not a
candidate-native unit plus full-cone nonnegative index theorem.

Thus shape and stress data alone do not certify BC13.

Combining the steps:

```text
Lorentzian/max-Gram/stress certificate alone
  => no forced full-cone nonnegative index theorem
  => no candidate-native unit/exhaustion package
  => no BC13 certification.
```

## 6. What These Packages Can Still Certify

The no-go is deliberately narrow. It preserves the following uses.

```text
Lorentzian shape
  Certifies Hodge-index-style geometry, inertia windows, and low-rank
  structure of a proposed index form.

max-Gram supply
  Homes prime-power degrees, von Mangoldt weights, max-kernel faces,
  and exact entry formulas inside a useful supply carrier.

carrier guards
  Can show that some controls are formable or not formable. For
  example, DH-style negative coefficients may fail to define an atom
  multiset, while Epstein-shaped data can test carrier blindness.

density diagnostics
  Signature flow can see smooth density layers and distinguish them
  from oscillatory zero content when the protocol is frozen.

stress localization
  Can locate unpaid atoms, depth walls, entry-corner slack,
  degeneration toward the light cone, and exponential-versus-linear
  failure laws.

compatibility checks
  Can test whether a proposed future Count/H_odd/Compare package is
  compatible with known ku/index supply constraints.
```

These are supply-grade and diagnostic achievements. They are not the
missing second evaluation.

## 7. Classified Demotions

```text
Frobenius-graph / max-Gram face
  Homes Lambda(p^k) on the prime side and gives exact Gram structure,
  but remains a strict face unless a full graph-cone exhaustion theorem
  is supplied.

Norm-Gram / signature flow
  Certifies global Lorentzian behavior and density response. It does
  not provide a native odd slot or an independent count comparison,
  and its decision channel is zero-blind at the witnessed level.

ku face
  Best current supply model: prime-power comb, depth wall, and carrier
  guard. It has one evaluation unless a new independent trace/count
  entry is added.

2D ku Castelnuovo posing
  Well-posed Lorentzian override form, but shape is content-free and
  the Weil fixed-point slot is occupied by Lambda_p - m+.

finite signature panels
  Useful witnesses and sanity checks. They cannot prove uniform
  infinite-support exhaustion without a theorem.

stress margins and discriminants
  Useful to locate where a face pays or fails. They become decision
  data only when one entry is independently evaluated by Count and by
  I through a contentful Compare theorem.
```

## 8. Candidate Gate

Before promoting a max-Gram/signature/stress result, require the
following.

```text
G58.1 identify the role
  Is the result being used only as shape/supply/diagnostic data, or is
  it being promoted to P3 or BC13? If only supply, record the
  constraint and stop.

G58.2 define I
  Name the index/spectral value I. State whether it is a Gram entry,
  inertia, jump count, Schur complement, discriminant, stress margin,
  or another function of G_N.

G58.3 define Count
  Name D_Count and the Count evaluation. Prove that D_Count is not the
  same natural domain as D_I and is not transported from the Gram
  package. See docs 65 and 70.

G58.4 identify H_odd
  Name the nonzero odd determinant/cohomology/spectral slot. Prove
  that it exists before the acting map, stress parameter, scale, or
  Gram deformation is chosen. See docs 65 and 70.

G58.5 audit eigenvalue supply
  Prove that the H_odd eigenvalues are supplied by the carrier/slot
  structure independently of the action. Gram eigenvalues, jump loci,
  and deformation thresholds do not count by themselves.

G58.6 state Compare
  State the theorem equating I and Count on the common locus. Identify
  the mathematical input in its proof beyond the Gram formula,
  determinant algebra, or stress-flow definitions. See docs 65 and 70.

G58.7 prove BC13 separately
  If the result is used for BC13, name the full Sonin/Frobenius-graph
  core, prove exhaustion, prove forced nonnegativity by native value
  type, identify the candidate-native unit, and prove uniformity along
  the infinite support filtration. See doc 67.

G58.8 freeze zero-side data
  Verify that no zeta zeros, zero-side signs, or RH-line information
  are used before the carrier, unit, H_odd, Count, and Compare are
  built; see docs 59 and 69.
```

Failure of G58.3-G58.6 rejects P3 promotion. Failure of G58.7 rejects
BC13 promotion. Passing the shape checks alone is not enough.

## 9. Exact Escape Criteria

A max-Gram/signature/stress package escapes this no-go only by adding
all of the following data.

```text
E1 independent Count
  A count-side evaluation with its own natural domain, not a
  regularization, transport, or re-reading of the Gram/index package.

E2 native H_odd
  A nonzero odd determinant/cohomology/spectral slot supplied by the
  carrier before the acting map or deformation is chosen.

E3 unforced eigenvalues
  Eigenvalues in H_odd supplied by the carrier/slot structure, not by
  the acting degree, scale, stress parameter, Gram eigenvalue, or
  zero-side input.

E4 contentful Compare
  A theorem equating Count and I on a common locus, with proof content
  beyond the definitions of the Gram entries and stress flow.

E5 full BC13 package
  A forced nonnegative native value over the full Sonin/Frobenius-
  graph core, with candidate-native unit and uniform infinite-support
  exhaustion.
```

If E1-E4 are absent, the package is not a P3 second evaluation. If E5
is absent, it is not BC13. If only Lorentzian shape, max-Gram entries,
or stress-flow margins are present, the correct classification is
supply-grade diagnostic.

## 10. Program Consequence

T48.7 is now a reusable gate:

```text
Do not promote Lorentzian signature, max-Gram positivity, norm-Gram
flow, ku-face Hodge-index shape, or stress-flow margins to P3 or BC13
unless the proposal separately supplies independent Count, native
H_odd, contentful Compare, and full graph-cone exhaustion.
```

The live role of max-Gram/signature data is positive but bounded: it
constrains any future liquid/metrized carrier by preserving the known
prime-power supply, Lorentzian index shape, depth-wall diagnostics,
and carrier guards. The missing theorem is still the merger of that
index shape with an independent Count/H_odd/Compare package and a
BC13-grade full-cone positivity theorem.
