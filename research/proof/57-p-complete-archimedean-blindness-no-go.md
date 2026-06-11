# 57 - p-Complete Archimedean Blindness No-Go

Status: reusable gate for doc 48 T48.6. Doc 68 isolates the
archimedean escape normal form behind this gate.

## 1. Statement

Let C be a proposed RH carrier built purely from p-complete TP, TR,
TC, Witt vectors, prismatic/Nygaard-complete coefficients, or functors
canonically obtained from them. Assume no extra archimedean structure
has been supplied inside the construction.

Purely p-complete means:

```text
P1 p-complete coefficients
  The coefficients and mapping objects are p-complete or p-adic.

P2 cyclotomic/Witt native operations
  The available structure maps are Frobenius, Verschiebung,
  restriction, cyclotomic trace maps, TR/TC/TP comparison maps,
  Witt ghost/component maps, Nygaard/prismatic filtrations, and
  functorial maps built from these.

P3 no internal archimedean input
  The construction contains no internal R object, no T = R/Z object,
  no liquid/gaseous archimedean analytic ring, no structural
  embedding iota into C used as an archimedean realization, and no
  trace pairing that couples the p-complete comb to an archimedean
  continuum on the same form.

P4 transport comparison
  Any proposed Count/Index equality is obtained by TR_0 = W,
  Witt fixed-point descriptions, cyclotomic trace/fixed-point
  transport, TC^- -> TP comparison, determinant algebra on the same
  functorial trace data, or regularization of that same p-complete
  object.
```

Then C cannot satisfy doc 45 A2 or A4. If its second-evaluation claim
uses P4, it also cannot satisfy doc 45 E1 or E3.

Equivalently, a p-complete TP/TR/Witt tower is an address or supply
shadow until an independent archimedean escape is added. It is not the
liquid archimedean slot and is not a decision-grade second evaluation.

## 2. Local Inputs

Doc 45 A requires a liquid address with internal R and T = R/Z, and
the archimedean completion missing from the finite-adelic Anderson
layer. Its A4 trace must couple comb and continuum on the same
index/Gram form; a separate positive archimedean block is explicitly
the wrong shape.

Doc 45 E requires:

```text
E1
  Count and spectral/index evaluations have different natural
  extension domains. Natural isomorphism, Poisson transport,
  coker=det algebra, or regularization of one series is one
  evaluation.

E3
  Odd-slot eigenvalues are supplied by the carrier/slot structure
  independently of the acting map.
```

Doc 52 already classifies TP/TR/Witt transport as one evaluation
unless external independent structure is added: TR_0(A;p) = W(A),
Witt fixed-point descriptions, and cyclotomic trace transports move
functorial trace data, but do not supply an independent Count domain.

MM LS2-LS4 sharpen the missing archimedean object:

```text
LS2
  The category L must contain internal R and T = R/Z, including the
  missing archimedean corner A_f x R.

LS3
  Fourier self-duality and the Gaussian unit must be structural.

LS4
  The trace tr_L must turn the lattice sequence
  0 -> (log p)Z -> R -> T_p -> 0 into a comb-continuum exchange, with
  the archimedean coordinate paired against the banked lattice image
  on the same Lorentzian/Gram form.
```

The p-complete notes supply the blindness diagnostic: p-complete
cyclotomic pairings at p see only p-adic data; Hesselholt's finite
field determinant extracts an Euler factor only after an embedding
iota: W(F_q) -> C and a regularized determinant on the iota-image.
For the Spec Z/square analogue, the recorded blockers are
p-completeness, semilinearity of Frobenius, and absence of an iota.

## 3. Proof

### Step 1: Pure p-completion cannot supply A2

A2 asks for internal R and T = R/Z with the archimedean completion
present in the candidate category. Under P1-P3, all native
coefficients and operations remain p-complete or p-adic. Such data can
remember p-adic completions, Frobenius lifts, Witt coordinates, and
Nygaard/prismatic filtrations, but it does not contain the real
additive line, the metrized circle R/Z, or the completion A_f x R.

Adding the notation "R" after the fact does not change this. To
satisfy A2 the real object must be internal and structural, as in LS2:
T must carry its topological 2pi rigidity inside L, and the
archimedean corner must be part of the same address object. A
p-complete tower has no such corner by P3.

Therefore a purely p-complete TP/TR/Witt construction fails A2.

### Step 2: Pure p-completion cannot supply A4

A4 and LS4 require a trace coupling, not a parallel trace value. The
trace must pair the banked comb against an internal archimedean
continuum on the same index/Gram form. The lattice exact sequence

```text
0 -> (log p)Z -> R -> T_p -> 0
```

must be visible to the trace, and the global product-formula assembly
must make the archimedean constant an output of the same coupled
measurement.

Under P1-P3, the available trace data are p-complete cyclotomic,
Witt, TR/TC/TP, or prismatic data. These can produce p-adic trace
shadows and finite-place bookkeeping, but they have no internal R, no
metrized T_p, and no same-form comb-continuum pairing. A later
complex-valued determinant, a chosen regularization, or a separate
archimedean block is not LS4; it is an external readout or a side
summand.

Therefore a purely p-complete TP/TR/Witt construction fails A4.

### Step 3: Witt/TR transport fails E1

Assume the proposed second evaluation is obtained by P4. Then Count
and I are not native evaluations with different extension domains.
They are related by a natural identification or functorial transport:
TR_0(A;p) = W(A), Witt fixed-point data, cyclotomic trace comparison,
TC^- -> TP, or determinant algebra on the same p-complete trace
object.

This is exactly the E1 failure mode from doc 52. Deforming the
p-complete source data moves both sides together, and the equality
has no independent Count domain beyond the transported trace data.
Thus the comparison is one evaluation in two presentations.

Therefore Witt/TR/TP transport fails E1.

### Step 4: Witt/TR transport fails E3

E3 asks for odd-slot eigenvalues supplied by the carrier before the
acting correspondence is chosen. In the p-complete transport setting,
the visible eigenvalue data are Frobenius weights, Adams parameters,
the chosen p, the chosen q, cyclotomic degree, or the action of the
same Frobenius/Witt operator whose trace is being queried.

Such eigenvalues are action-supplied. At a finite-field point the TP
odd slot is empty; in Witt/TR point calculations the Frobenius fixed
data are definitional; in Adams/Frobenius variants the weight is part
of the acting structure. None of these provides a nonzero odd spectrum
whose eigenvalues are native to an independent carrier.

Therefore Witt/TR/TP transport fails E3.

### Step 5: The finite-field iota does not rescue the pure case

The finite-field TP determinant is not a counterexample to the
statement. Its complex determinant uses

```text
iota: W(F_q) -> C
```

and then takes a regularized determinant after re-reading p-adic
coefficients in C. That iota is the archimedean move. It is external
to pure p-completion in the sense relevant here, and it is precisely
what P3 excludes.

For the Spec Z/square target, the local notes record no analogous
internal iota: the coefficients are p-complete/Nygaard-prismatic, the
Frobenius remains semilinear, and there is no finite power that makes
the Frobenius linear over a finite fixed field as in the F_q case. So
the square cannot import the finite-field determinant pattern without
first constructing the missing archimedean structure.

This proves the theorem.

## 4. Failure Classification

```text
pure TP/TR/Witt tower
  Fails A2 and A4. It has p-complete address and trace shadows, but no
  internal R/T object and no LS4 comb-continuum coupling.

TR_0(A;p) = W(A)
  Fails E1. This is a natural isomorphism of functorial trace/Witt
  data, not an independent Count evaluation.

Witt fixed points
  Fails E1 and usually E3. Fixed-point descriptions repackage the
  same Frobenius-lift data; when eigenvalues appear, they are supplied
  by the Frobenius/action being tested.

finite-field TP determinant
  Useful embryo/calibration, not a pure p-complete escape. The
  determinant uses iota: W(F_q) -> C, and at a point TP_odd is empty.

Spec Z or square TP without iota
  Fails A2/A4 and E1/E3. The p-complete/prismatic coefficients have no
  complex embedding, no internal R/T, and no same-form LS4 trace.

separate archimedean correction term
  Fails A4. It may repair a numerical formula, but it is a positive
  block beside the p-complete bank, not a coupled trace on the same
  form.
```

## 5. Admissible Archimedean Escape

An escape from this no-go must add genuinely new structure. The
following are admissible in principle.

```text
X1 internal liquid address
  A category L with internal R and T = R/Z, including the
  archimedean completion A_f x R, as in LS2.

X2 structural Fourier/Gaussian unit
  A Fourier self-duality internal to L whose normalization and
  Gaussian fixed unit are structural, not chosen after the fact.

X3 coupled trace
  A trace tr_L on dualizable objects of L that implements the
  sequence 0 -> (log p)Z -> R -> T_p -> 0 as a comb-continuum
  exchange on the same index/Gram form.

X4 structural iota
  A map playing the role of iota, but constructed inside the global
  carrier and tied to X1-X3. A post hoc embedding into C, an external
  regularization, or a coefficient choice is not enough.

X5 independent second evaluation
  Count and I must have different natural extension domains, and
  Compare must use mathematics beyond TR/Witt/TP transport or
  determinant bookkeeping.

X6 unforced odd spectrum
  The odd slot must be nonzero, and its eigenvalues must be supplied
  by the carrier/slot before the acting correspondence is chosen.
```

Anything less remains a calibration object, supply shadow, or
one-evaluation transport. See doc 68 for the reusable admission normal
form.

## 6. Candidate Gate

Use this gate before promoting any p-complete TP/TR/Witt proposal.

```text
G57.1 p-complete audit
  List all coefficient rings and completion operations. If every
  coefficient and operation is p-complete/p-adic/prismatic, mark the
  candidate pure unless a separate item below is proved.

G57.2 internal R/T audit
  Name the internal R and T = R/Z objects. Prove that T carries its
  rigidity internally and that the archimedean corner A_f x R is part
  of the carrier. If absent, A2 fails.

G57.3 LS4 coupling audit
  Exhibit the trace tr_L and the same-form pairing implementing
  0 -> (log p)Z -> R -> T_p -> 0. If the archimedean term is separate
  from the p-complete bank, A4 fails.

G57.4 iota audit
  If an embedding or complex realization is used, prove it is
  structural inside the carrier. If it is a post hoc map to C or a
  regularized readout of p-complete coefficients, it is not an
  internal escape.

G57.5 transport audit
  Identify whether the comparison factors through TR_0 = W, Witt
  fixed points, cyclotomic trace, TC^- -> TP, coker=det algebra, or
  determinant regularization. If yes, E1 fails unless an independent
  Count domain is separately constructed.

G57.6 eigenvalue audit
  Name the odd slot and its eigenvalues before choosing the acting
  correspondence. If the eigenvalues are Frobenius degree, Adams
  weight, p, q, a scale, or a regularization variable, E3 fails.

G57.7 promotion rule
  Passing G57.1-G57.6 does not prove the candidate. It only clears the
  p-complete blindness gate and allows the full doc 45 A-E checklist
  to be run.
```

Gate verdict: pure p-complete TP/TR/Witt constructions are rejected at
G57.2 and G57.3; Witt/TR/TP transport comparisons are rejected at
G57.5 and G57.6.
