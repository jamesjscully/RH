# 46 - Construction blueprint for a liquid/index carrier

Status: construction-facing blueprint, 2026-06-11. This is the
`construction` branch of doc 45 section 8. It does not claim that the
missing structure exists. It gives the most concrete candidate shape
currently licensed by docs 41-45 and MM, plus the first subobject that
can be built or falsified without importing zero-side data.

## 1. Scope

Doc 45 states the final target as

```text
M = (L, b, R/T, U, Fr, H_odd, I, N, Count, Compare).
```

This document refines that tuple into a construction plan. A completed
object would have to satisfy all doc 45 clauses A-E. This document only
specifies:

```text
1. proposed native objects for each component;
2. dependencies, split into theorem-grade, scoped, and unwritten;
3. the first buildable subobject;
4. exact gates before promotion;
5. immediate falsifiers.
```

The controlling negative facts are:

```text
doc 42: no banked carrier survives BC-E3'/BC13 at decision grade;
doc 43: Gaussian deep-cell phase is unit-slot data, not object data;
doc 44: the strict-square / hand-inserted-unit g2 proxy is killed;
MM: the liquid slot is scoped, not constructed, and the real LS3/LS4
    spine is unwritten.
```

## 2. Candidate Native Objects

The candidate should be approached as a liquid/gaseous enhancement of
the ku/index carrier, not as a new finite-window numerical probe.

### L - liquid/gaseous analytic trace category

Proposed native object:

```text
L = a symmetric monoidal presentable stable category of modules over a
    liquid/gaseous analytic R-object, with dualizable objects, internal
    R, internal T = R/Z, and trace-class/proper-pushforward formalism.
```

The minimal intended source is MM's LS1-LS6. In-print support is only
partial: MM reports theorem-grade liquid R foundations and liquid
Serre duality/HRR for complex manifolds, but no printed archimedean
liquid Fourier/Poisson theory and no THH/K computation with liquid
coefficients. Therefore the construction cannot start by asserting
full `L`; it must first build a trace-calibrated subcategory and test
the carrier guard there.

Native failure to avoid:

```text
bare Shv(R/(log p)Z; C)
```

This is scale-blind by the Efimov-style localizing-invariant result
recorded in MM and classified in docs 41-42. The circumference `log p`
must live in metric, analytic-ring, equivariant, or kernel data.

### b - conservative bank embedding

Proposed native object:

```text
b: Bank -> L
```

where `Bank` contains at least:

```text
1. the ku prime-power supply face;
2. the THH/TP/TR and strict count layers named in doc 45;
3. the Frobenius-graph/index faces;
4. the product-formula / comb data used by MM LS4.
```

Required behavior:

```text
b must preserve prime-power addresses, graph depths, banked count
identities, and the known carrier guards. It may enrich them, but it
may not rescale, quotient, or destroy them.
```

Evidence: doc 42 identifies the ku face as the best supply carrier and
the liquid/metrized layer as the best address; doc 45 says the final
object must merge these without promoting either alone.

### R/T - internal real line and circles

Proposed native objects:

```text
R_L       = internal real additive object in L;
T_L       = R_L / Z;
T_p       = R_L / (log p)Z, with log p retained as metric or analytic
            structure, not as bare homotopy type;
A_L       = A_f x R_L, completing the banked finite-adelic corner.
```

MM LS2 is the local source: `R` and `T=R/Z` must be internal, with the
archimedean completion present. The rigidity target is
`Aut_L(T) = {+-1}` so that normalization torsors are not free
calibration choices.

### U - candidate-native continuum unit

Proposed native object:

```text
U = the fixed/dualizing unit of an internal Fourier transform on the
    Schwartz or trace-class object of R_L.
```

For the final object, `U` must be derived inside `L`. It cannot be a
hand-inserted Gaussian repair. MM LS3 proposes the strongest form:
Fourier inversion internal to `L`, with the Gaussian fixed unit unique
up to the internal `{+-1}` rigidity.

Construction caution from doc 43:

```text
slot constants and cell signs are U-covariant. A deep Gaussian
negative cell is not object data, since the self-dual Hermite unit
already flips the banked `(11;2)@4.96` cell.
```

Therefore the build target is not "force the Gaussian signs"; it is
"derive the candidate's own unit, then state the index and slot data in
that unit's covariant coordinates."

### Fr - class-and-scale Frobenius correspondence

Proposed native object:

```text
Fr_{p,k,a}: a class-and-scale correspondence indexed by prime-power
            classes and graph/window data, acting on b(Bank) inside L.
```

It should come from the Euler-product/valuation address, such as the
`p^Z` grading or the ku prime-power comb, not from a bare endomorphism
degree. Its role is to query `H_odd`, `I`, and `Count`; it must not
definitionally supply the odd-slot eigenvalues.

Evidence: doc 41 BC-E3' and doc 45 E3 rule out solenoid-style
self-supply. Doc 42 says finite-field Quillen has the right pattern
but forced/empty spectrum, while the solenoid has nonempty H^1 with
self-supplied degree.

### H_odd - unforced odd slot

Proposed native object:

```text
H_odd = the odd part of a determinant/cohomology/spectral object
        attached to the liquid/index carrier itself, equipped with a
        Fr action but not defined by Fr.
```

The most conservative construction-facing placeholder is:

```text
H_odd(candidate) =
  odd determinant line or odd cohomology of the proper liquid/gaseous
  object whose trace also defines I and Count.
```

This is deliberately not identified with `H^1(T_p)` or `TP_odd(F_q)`.
Those are classified failures: self-supplied in the solenoid case and
empty in the finite-field point case. The first construction pass must
therefore expose where `H_odd` lives before any eigenvalue comparison
is attempted.

### I - forced-nonnegative index/Gram form

Proposed native object:

```text
I(n) = an index, dimension, count, or Gram norm attached natively to
       the liquid carrier and evaluated on a class family N.
```

Required sign source:

```text
nonnegative because it is a dimension/count/Gram norm/index-level
integer, not because an analytic estimate happens to be positive.
```

The expected local shape is a liquid lift of the HH Frobenius-graph
index face coupled to MM LS4's trace. Doc 44 requires this lift to
use the candidate's own unit and the full graph cone; the strict
square extension is already killed.

### N - full graph-cone class family

Proposed native object:

```text
N = the liquid class/scale family generated by prime-power atoms,
    graph-depth steps, mixed towers, k=1 boundary directions, and
    real/conic directions of the doc-00 Sonin/Frobenius-graph core.
```

`N` cannot be a strict family, a finite scan, a Gaussian cell list, or
a hand-picked positive face. Doc 44 identifies this as the live BC13
test: g1 positivity plus g2/g3 exhaustion and uniformity.

### Count - independent count-side evaluation

Proposed native object:

```text
Count(n) = a count-side trace/euler-characteristic evaluation with a
           natural domain larger than the agreement locus.
```

Candidate sources:

```text
1. MM LS5: theta-count / RR compatibility for product divisors, with
   a finite renormalized dual where the strict square diverges.
2. Quillen/Weil pattern as a model for two evaluations, but not as the
   object itself because finite-field odd spectrum is empty/forced.
3. Liquid Serre/HRR complex-shadow computations as calibration only.
```

`Count` must not be Poisson transport, determinant algebra of the same
series, or a regularization of `I`. Doc 41 G3 and doc 45 E1 demand P3
independence.

### Compare - contentful agreement theorem

Proposed native object:

```text
Compare: a theorem equating I(n) and Count(n) on a common locus in N,
         with both evaluations defined beyond that locus and with
         nontrivial unforced odd spectral data constrained.
```

The theorem must consume mathematics not already present in the
definitions of `I` and `Count`. Natural-isomorphism transport is a
failure mode, not a comparison theorem.

## 3. Dependency Ledger

```text
component      status              local source
------------- ------------------- ------------------------------------------
liquid R       partial/in print     MM sec 2(a), LS2
gaseous R      draft-grade          MM sec 2(a), sec 4.2
internal R/T   spec-level           MM LS2; doc 45 A2
Fourier U      unwritten on R       MM LS3, R1; doc 45 A3/C4
trace LS4      unwritten globally   MM LS4, R3; doc 45 A4
bank embedding partly banked        docs 42,45; MM LS1
ku supply      banked shadow        doc 42 positive residue
index face     banked shadow        docs 42,44 positive residue
H_odd          missing              docs 41,42,45 BC-E3'
Count          pattern only         docs 41,42,45 E1-E4
Compare        missing              docs 41,45
```

Construction must therefore proceed by subobjects, not by declaring the
full package.

## 4. First Buildable Subobject

The first buildable subobject should be:

```text
B0 = (L0, b0, R0/T0, tr0, comb_p, Count0)
```

where:

```text
L0
  The theorem-grade complex-shadow liquid category from MM Route A,
  using the Tate curve X_p = C^x / p^Z as a compact complex manifold
  proxy for the real circle T_p.

b0
  The p^Z/q-expansion grading embedding of the banked p-tower data
  into the sections/count side. This must preserve the monoid address.

R0/T0
  The visible circle/address data carried by X_p and its p^Z grading.
  This is not yet the final internal real T_p of LS2.

tr0
  The liquid Serre-duality / HRR trace available for complex manifolds.

comb_p
  The banked one-place comb shadow from MM Route A.

Count0
  The RR/euler-characteristic count of line bundles or graded sections
  on X_p.
```

Purpose:

```text
1. calibrate the liquid trace against the banked one-place comb;
2. verify that the p^Z grading is the only source of carrier address;
3. register the expected null: one-place data should be scale-free and
   should not produce kappa or the final unit;
4. prepare the Epstein kill-test before any two-place/global lift.
```

This subobject intentionally omits:

```text
U, Fr, H_odd, I, N, Compare.
```

That omission is not a defect of the blueprint. It is the point of the
first construction step: if B0 already smuggles in a unit, a spectrum,
or a comparison theorem, it is calibration rather than construction.

## 5. Next Subobject After B0

If B0 behaves as expected, the next target is:

```text
B1 = (L1, b1, R1/T1, U1?, tr1, Fr1?, I1?, Count1?)
```

with two circles or places assembled by the product formula:

```text
T_p and T_q inside a gaseous/liquid R category,
comb_p tensor comb_q embedded by b1,
trace assembled against the product-formula constraint,
Epstein replacement tested immediately.
```

The question for B1 is not RH and not zero comparison. The question is
whether LS4's coupling is definable only for the multiplicative
Euler-product carrier while the theta/PD count remains alive for an
Epstein lattice. MM section 3 says this is the first place `kappa` can
appear and also the first serious carrier guard.

## 6. Exact Gates

### Gate 0 - no zero import

No construction step may use zeta zeros, zero-side signs, or analytic
continuation as input. The explicit formula may only appear as a later
comparison frame, as in MM LS6 and doc 41's fork protocol.

### Gate 1 - scale retention

The object must identify where `log p` lives. A bare topological circle
or a localizing invariant of `Shv(S^1)` fails immediately. Passing
requires metric, analytic-ring, equivariant, or kernel-level data.

### Gate 2 - conservative bank embedding

`b` must preserve banked prime-power, tower, count, and graph-index
identities. If enrichment changes the known ku supply theorem, the
HH graph indexing, or the count layer by rescaling, it is not the same
candidate.

### Gate 3 - Epstein/DH carrier guard

At the first LS4-like coupling, replace the multiplicative
prime-power carrier by an Epstein-shaped lattice. The required profile
is:

```text
theta/PD/count layer survives;
liquid coupling through b(comb_p) is undefinable;
failure occurs at carrier/effectivity, not at a later sign estimate.
```

If the same coupling computes for Epstein or DH, the route fails by
doc 41 OC4 and doc 45 B2/B3.

### Gate 4 - unit derivation

`U` must be the candidate's native unit. It cannot be the Gaussian, a
Hermite perturbation, or a strict repair atom inserted from outside.
Once `U` is derived, all slot constants and cell tests must be rerun in
`U`-covariant coordinates.

### Gate 5 - odd-slot supplier audit

Before using any eigenvalue, identify:

```text
where H_odd lives;
why H_odd is nonzero;
who supplies its eigenvalues;
why Fr only queries those eigenvalues.
```

Empty slot, solenoid-style degree supply, finite-field forced Adams
eigenvalues, or zero-side import all fail BC-E3'.

### Gate 6 - forced nonnegativity

`I` must be nonnegative by native structure. If positivity is an
estimate, a signed trace, or a repaired inequality on a hand-picked
face, it does not satisfy doc 45 D1.

### Gate 7 - full graph-cone exhaustion

The class family `N` must include:

```text
k=1 boundary directions;
deep graph steps;
mixed towers;
real/conic directions;
uniform infinite-support filtration behavior.
```

Strict-square, ku-only, max-Gram-only, Gaussian-cell, and finite-window
tests fail this gate by docs 42 and 44.

### Gate 8 - P3 comparison

`Count` and `I` must have larger natural domains and agree by a
contentful theorem on the common locus. If the comparison is Poisson
transport, coker=det algebra, a natural isomorphism, or regularization
of one series, it is one evaluation.

## 7. Immediate Falsifiers

```text
F0: B0 depends on log p only through the homotopy type of a circle.
    Verdict: bare-circle failure; return to L.

F1: the p^Z/q-expansion grading can be replaced by an arbitrary lattice
    grading and the coupling still computes.
    Verdict: carrier-blind; Epstein guard failed.

F2: the first trace-coupling requires choosing a Gaussian, scale, or
    normalization not forced by internal R/T rigidity.
    Verdict: inserted unit; violates MM LS6 and doc 45 U.

F3: the odd slot is H^1 of the acting circle and the eigenvalue is the
    degree of the acting map.
    Verdict: solenoid self-supply.

F4: the odd slot is TP_odd or analogous point cohomology and vanishes,
    or eigenvalues are forced Adams parameters.
    Verdict: finite-field empty/forced spectrum.

F5: nonnegativity is certified only on the strict square, the ku face,
    max-Gram scans, or the NN strict proxy.
    Verdict: strict-face BC13 failure.

F6: the construction asks a Gaussian deep-cell sign to remain negative.
    Verdict: slot artifact; doc 43 already demotes it.

F7: Count and I are related by transport or by two presentations of the
    same determinant/series.
    Verdict: P3 independence failure.

F8: the construction consumes zeta zeros or zero-side signs before the
    carrier and slot are built.
    Verdict: circular zero import.
```

## 8. Build Order

```text
Step 1 - B0 complex-shadow calibration
  Implement the Tate-curve/liquid-RR trace against the p^Z graded comb.
  Expected outcome: scale-free one-place null, with banked grading
  preserved. This is a calibration, not the missing object.

Step 2 - B0 Epstein replacement
  Replace p^Z with an Epstein-shaped lattice at the same trace/count
  level. Required outcome: count/theta survives, but the bank coupling
  through monoid/valuation address is undefinable.

Step 3 - B1 two-place liquid/gaseous assembly
  Attempt the product-formula-coupled trace for T_p and T_q. This is
  where MM says the real LS3/LS4 dependency appears.

Step 4 - unit extraction
  If B1 exists, derive U from internal Fourier self-duality rather than
  inserting it. Then restate the k=1 charge, threading, and depth wall
  in U-covariant coordinates.

Step 5 - index lift
  Lift the HH Frobenius-graph Gram/index face into L and test whether
  forced nonnegativity covers the full N, not a strict face.

Step 6 - odd slot and comparison
  Expose H_odd, audit its eigenvalue supplier, define Count on a larger
  domain, and prove Compare with P3 independence.
```

Only steps 1-2 are construction-facing with current printed inputs.
Steps 3-6 are the actual missing mathematics.

## 9. Main Conclusion

The most precise construction-facing blueprint is:

```text
start with the liquid complex-shadow trace B0 on a Tate-curve
p^Z-graded comb, use it only to calibrate the bank embedding and
Epstein guard, then attempt a two-place gaseous/liquid LS4 coupling
whose native Fourier unit, Frobenius-index form, full graph-cone
coverage, and independent odd-slot comparison must all be built rather
than imported.
```

No construction exists in the current record. The first honest
subobject is not the final carrier; it is the calibration/kill-test
platform that prevents the later construction from degenerating into
bare-circle scale blindness, Epstein-blind Poisson transport, a
hand-inserted unit, or a strict-face index proxy.
