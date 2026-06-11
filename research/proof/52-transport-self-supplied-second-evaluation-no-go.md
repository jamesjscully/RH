# 52 - Transport and self-supplied second-evaluation no-go

Status: broad no-go proof draft, 2026-06-11. This turns doc 48
T48.5 into a theorem-shaped gate for doc 45 clause E. It classifies
transport comparisons and self-supplied spectra as controls, models,
or embryos, never decision-grade second evaluations.

## 1. Statement

Let a proposed RH carrier supply the following data on a candidate
agreement locus `N`:

```text
I      = spectral/index evaluation,
Count  = count-side evaluation,
H_odd  = odd determinant/cohomology/spectral slot,
Compare: I(n) = Count(n) for n in N.
```

Assume that at least one of the following holds.

```text
T1 transport
  The two evaluations are related by a chain of natural isomorphisms,
  Poisson transport, Pontryagin duality, inverse-limit/colimit
  bookkeeping, coker=det algebra, TP/TR/Witt transport, or two
  presentations of the same determinant, trace, theta, or series.

T2 same natural domain
  The natural domain on which I is defined is the same as the natural
  domain on which Count is defined, or one domain is obtained from the
  other functorially without adding independent structure.

T3 regularization of one object
  One side is analytic continuation, zeta regularization, Euler-
  Maclaurin transport, determinant regularization, or another
  regularization of the same series/object defining the other side.

S1 empty odd slot
  H_odd is zero, absent, or an analogous point/finite-field odd
  determinant slot with no nontrivial spectral parameter.

S2 acting-degree supply
  The odd-slot eigenvalue is the degree, scalar, Adams parameter,
  chosen scale, multiplication factor, or regularization variable of
  the acting correspondence itself.

S3 self-eigenvalue supply
  The action both defines the spectral parameter and queries it. The
  carrier has not supplied the parameter independently of the action.

F1 formal agreement
  Compare consumes only definitions, naturality, determinant algebra,
  product formulas on defining data, or functorial transport.
```

Then the proposed comparison cannot satisfy doc 45 E1-E4 at decision
grade. More precisely:

```text
T1, T2, or T3 fail E1 P3 independence.
S1 fails E2 nonempty odd slot.
S2 or S3 fail E3 unforced eigenvalues.
F1 fails E4 contentful theorem.
```

Thus a comparison produced by transport or by a self-supplied spectrum
is one evaluation, an empty-spectrum embryo, or a forced-spectrum
control. It is not the second evaluation required by docs 45-46.

## 2. Local Dependencies

This draft depends on the following local sources.

```text
doc 45 E1-E4
  E1 demands different natural extension domains. Natural isomorphism,
  Poisson transport, coker=det algebra, or regularization of one
  series is one evaluation.

  E2 demands a nonzero odd determinant/spectral slot.

  E3 demands odd-slot eigenvalues supplied by the carrier/slot
  structure independently of the acting map. The action queries them;
  it does not define them.

  E4 demands an agreement theorem with content beyond the definitions.

doc 46 Count/Compare
  Count must not be Poisson transport, determinant algebra of the same
  series, or a regularization of I. Compare must be a theorem equating
  I and Count on a common locus, with both evaluations defined beyond
  that locus and with nontrivial unforced odd spectral data.

doc 46 Gate 8 and falsifiers F3-F7
  Solenoid self-supply, finite-field empty/forced spectrum, and
  transport between Count and I are immediate P3 failures.

YY P3 audit
  P3 is operationally: different structures with larger natural
  extension domains, a contentful agreement theorem, and a nontrivial
  unforced spectrum. Quillen over finite fields passes the first two
  conditions but remains embryo grade because the spectrum is empty or
  forced.

ZZ solenoid audit
  The solenoid fixed-count/trace formulas agree, but the agreement is
  Pontryagin/inverse-limit transport on the affine locus and the H^1
  eigenvalue is the acting degree.

doc 48 T48.5
  Names the transport/self-supplied spectrum theorem target and its
  escape route.

doc 65
  Isolates the P3 independence normal form: extension-domain asymmetry,
  contentful agreement, and nonzero unforced odd spectrum. Doc 52 is an
  application of that lemma to transport and self-supplied spectra.
```

## 3. One Evaluation Versus P3 Independence

The distinction used here is structural, not cosmetic.

One-evaluation transport has the following normal form.

```text
data D
  |
  | formal operation: natural iso, Poisson, duality, coker=det,
  | regularization, Witt/TR comparison, product formula, or change of
  | presentation
  v
same data read as I and Count
```

In this case the apparent equality

```text
I = Count
```

is an equality inside one structure. Deforming the structure moves
both sides together, or destroys both sides together, or leaves one
side merely as a formal expression whose agreement with the count is
no longer a theorem on a larger common locus.

P3-grade independence has a different normal form.

```text
structure A  --->  Count
structure B  --->  I

agreement locus N = where A and B meet
theorem Compare: Count(n) = I(n) for n in N
```

The decisive features are:

```text
P3-a extension domains
  Count and I have natural domains larger than N, and the two
  extensions are not transported from each other.

P3-b content
  Compare consumes mathematics not present in the definitions of Count
  and I.

P3-c decision spectrum
  The agreement constrains at least one nonzero odd spectral parameter
  not supplied by the acting correspondence.
```

Therefore two formulas, two notations, two functorial presentations,
or two regularizations do not constitute two evaluations. They become
P3-grade only when there are two native structures with independent
extension behavior and a theorem cutting out their common agreement.

## 4. Proof

### Step 1: Transport fails E1

Assume T1 or T2. By hypothesis, Count and I are connected by
functorial transport or share the same natural domain. Hence the pair
does not exhibit the P3 extension asymmetry required by doc 45 E1.

If the equality is obtained by a natural isomorphism, then any
deformation of the source data is transported to both sides. If it is
obtained by Poisson summation, both sides are two presentations of the
same Fourier object. If it is obtained by Pontryagin duality, fixed
points and cokernels are dual readings of the same compact/discrete
pair. If it is obtained by coker=det algebra, the determinant is a
linear-algebraic dress of the cokernel. If it is obtained by
TP/TR/Witt comparison, the functor-level comparison transports the
same trace data. In every case the two sides fail to have independent
natural extension domains.

Thus T1 or T2 implies failure of E1.

### Step 2: Regularization fails E1

Assume T3. A regularized value of a series, determinant, theta sum, or
trace may be useful, but it is not an independent count evaluation of
that same object. It extends one object by analytic or formal rules;
it does not supply a second native structure with its own larger
domain.

Thus T3 also implies failure of E1.

### Step 3: Empty odd slot fails E2

Assume S1. Doc 45 E2 requires a nonzero odd determinant/spectral slot.
If the odd slot is zero or absent, then there is no odd spectral
parameter for Compare to constrain. A two-evaluation silhouette may
remain, but it is embryo grade at most.

Thus S1 implies failure of E2.

### Step 4: Acting-degree supply fails E3

Assume S2 or S3. Doc 45 E3 requires the odd-slot eigenvalues to be
supplied by the carrier/slot structure independently of the acting
map. If the eigenvalue is the degree, scalar, Adams parameter, chosen
scale, or regularization variable of the same action being tested,
then the action defines the spectral data it is supposed to query.

This gives a forced spectrum, not an unforced odd spectrum.

Thus S2 or S3 implies failure of E3.

### Step 5: Formal agreement fails E4

Assume F1. Doc 45 E4 requires Compare to consume mathematics beyond
the definitions of the two sides. Definitional equalities, naturality,
linear algebra, product formulas on defining data, and functorial
transport are not such a theorem. They are bookkeeping inside the
same structure.

Thus F1 implies failure of E4.

Combining the five steps proves the statement.

## 5. Classified Failure Modes

The following candidates are classified by the theorem.

```text
solenoid S_p
  Status: one-evaluation transport plus acting-degree self-supply.

  The fixed-count/trace comparison is

      Fix = ker
      #ker = #coker on the Pontryagin dual
      dual = H^1 for compact connected abelian groups
      coker size = product-formula value of the Lefschetz element.

  This is Pontryagin duality, inverse-limit/colimit bookkeeping, and
  product-formula algebra on the defining dual pair. H^1 is nonempty,
  but the eigenvalue of multiplication by p is p, the acting degree.
  Hence E1/E3 fail. The solenoid remains a scale/address control, not
  a decision-grade second evaluation.

Poisson and theta transport
  Status: one evaluation.

  A Poisson pair reads one Fourier object in primal and dual
  coordinates. Unless the count side and index side have separate
  native extension domains and a contentful agreement theorem, the
  equality is transport. E1 fails. If the same Poisson formalism also
  works for carrier-blind Epstein or DH data, the carrier guard fails
  earlier as well.

coker=det algebra
  Status: one evaluation.

  Rewriting a finite cokernel, Lefschetz factor, or rank-one pairing
  as a determinant does not create a point count. It is linear algebra
  on the same endomorphism. E1 fails, and E4 fails if Compare is only
  this rewrite.

TP/TR/Witt transport
  Status: one evaluation unless an external independent structure is
  added.

  Natural identifications such as TR_0(A;p) = W(A), Witt fixed-point
  descriptions, and cyclotomic trace transports move functorial trace
  data; they do not by themselves supply Count with an independent
  domain. A purely p-complete TP/TR/Witt construction also lacks the
  required archimedean iota unless additional structure is supplied.
  E1 fails for the transport comparison.

finite-field Quillen / DGM / TP point pattern
  Status: two-evaluation embryo, not decision grade.

  The Quillen finite-field pattern gives a genuine count/spectral
  agreement in the P3-a and P3-b sense: geometric fixed points and
  homotopy/K-theoretic cokernel data are different structures, and
  Quillen/DGM consumes real mathematics. But at a point the odd
  spectrum is empty, and the Adams eigenvalues q^w are forced supply
  data. E2/E3 fail for the decision-grade RH target.

regularization
  Status: one evaluation.

  Analytic continuation, zeta regularization, determinant
  regularization, Euler-Maclaurin transport, or a continued version of
  the same theta/series object is not a second native evaluation.
  E1 fails. If the agreement is merely the regularization rule, E4
  also fails.

acting-degree / self-eigenvalue constructions
  Status: forced spectrum.

  If the candidate action is multiplication by p, Frobenius with a
  prescribed Adams weight, a chosen scaling map, or any correspondence
  whose degree supplies the H_odd eigenvalue, the eigenvalue is an
  input of the test. The action is not querying an independently
  supplied odd spectrum. E3 fails.

zero-side import
  Status: circular, outside the gate.

  If the construction uses zeta zeros, zero-side signs, or RH-line
  information before building the carrier, H_odd, Count, and Compare,
  it is not a supply-side second evaluation. It fails the construction
  protocol before E can be tested.
```

## 6. Candidate Gate

Before a proposed carrier can be treated as a decision-grade
second-evaluation candidate, it must pass the following gate.

```text
G1 define domains
  Name the natural domain D_Count of Count and the natural domain D_I
  of I. Both must be strictly larger than the common agreement locus N.

G2 separate domains
  Exhibit deformation directions showing that D_Count and D_I are not
  transported versions of each other. It must be possible for one
  side's native structure to vary or remain defined while the other
  side's native structure is absent, fixed, or outside its definition.

G3 identify H_odd
  Name the nonzero odd determinant/cohomology/spectral slot.

G4 audit eigenvalue supply
  Prove that the H_odd eigenvalues are supplied by the carrier/slot
  structure before the acting correspondence is chosen. The acting
  correspondence may query these eigenvalues but may not define them.

G5 exclude transport
  Prove that Count is not Poisson transport, Pontryagin duality,
  coker=det algebra, TP/TR/Witt transport, a natural isomorphism, a
  regularization of I, or a second presentation of the same series.

G6 prove content
  State the theorem Compare and identify the mathematical input in its
  proof that is not already present in the definitions of Count and I.

G7 exclude zero import
  Verify that no zeta zeros, zero-side signs, or RH-line information
  are used before the carrier, H_odd, Count, and Compare are built.
```

Failure of any one of G1-G7 demotes the candidate to a model, control,
embryo, or one-evaluation construction.

## 7. Exact Escape Criteria

The no-go is avoided only by producing all of the following data.

```text
E1 escape
  Two evaluations Count and I with genuinely different natural
  extension domains, not connected by functorial transport or by a
  regularization of one object.

E2 escape
  A nonzero odd slot H_odd native to the carrier.

E3 escape
  Odd-slot eigenvalues supplied by the carrier/slot structure
  independently of the acting map, scale choice, Adams parameter,
  regularization variable, or zero-side data.

E4 escape
  A theorem Compare equating Count and I on a common locus N, whose
  proof uses mathematics beyond definitions, natural isomorphisms,
  formal determinant algebra, product-formula bookkeeping, or
  Poisson/TP/TR/Witt transport.

protocol escape
  The construction must not consume zeta zeros, zero-side signs, or
  an inserted unit before the carrier and slot are built.
```

Equivalently, the candidate must reproduce the Weil-shaped pattern at
decision grade: independent count and spectral structures, a theorem
cutting out their agreement, and a nonempty unforced odd spectrum. The
banked solenoid, Poisson, coker=det, TP/TR/Witt, regularization, and
acting-degree constructions do not meet this escape criterion.

## 8. Program Consequence

This theorem does not say that solenoids, Poisson formulas,
finite-field K-theory, TP/TR/Witt theory, determinant algebra, or
regularized traces are useless. They remain calibration objects and
failure controls:

```text
solenoid
  tests address, product-formula bookkeeping, and self-supply failure;

Quillen/DGM
  supplies the finite-field two-evaluation embryo and shows what the
  missing odd spectrum must add;

Poisson and regularization
  calibrate Fourier and analytic continuations while marking
  one-evaluation transport;

TP/TR/Witt
  records the p-complete trace shadow and its need for an independent
  archimedean/iota structure;

coker=det
  records determinant bookkeeping without pretending to be a count.
```

The construction-facing target after this no-go is therefore narrow:
build a carrier whose odd spectrum is native and unforced, then prove
a contentful Count/Index comparison between two genuinely independent
natural domains. Anything less is already classified by T48.5.
