# 51 - Scale-blind localizing-trace no-go

Status: first broad no-go proof draft, 2026-06-11. This turns
T48.1 into a theorem-shaped gate. It is a negative result about bare
sheaf categories and continuous localizing-invariant traces; it is not
a no-go for metrized/liquid analytic-ring traces, equivariant traces,
or traces of explicit kernels.

## 1. Statement

Let `C` be a dualizable coefficient category and let `F` be an
accessible or finitary continuous localizing invariant in the sense
cited in MM/XX from Efimov. For `l > 0`, put

```text
T_l = R / lZ.
```

Assume that a proposed place address and trace for the prime `p`
uses only the bare sheaf category

```text
Shv(T_logp; C) = Shv(R/(log p)Z; C)
```

and the data obtained from applying `F^cont` to this category, to the
lattice diagram

```text
(log p)Z -> R -> R/(log p)Z,
```

and to functorial maps or natural traces between these resulting
localizing-invariant values.

Then the resulting data is independent of `log p`. More precisely,

```text
F^cont(Shv(T_logp; C)) ~= F^cont(C)^{S^1}
```

naturally through the homotopy type of the circle, and the full
lattice-diagram image is equivalent to the `p`-independent homotopy
diagram

```text
Z -> * -> BZ.
```

Consequently no candidate whose liquid address is represented only by
bare sheaf categories `Shv(R/(log p)Z; C)` and their continuous
localizing-invariant traces can satisfy doc 45 clause A1
scale-retention or A4 trace-coupling. In the normal form of docs 41
and 45, such a candidate cannot provide the required liquid address.

## 2. Hypotheses

The theorem uses all of the following hypotheses.

```text
H1 localizing trace
  The trace factors through continuous localizing motives or through
  an accessible/finitary continuous localizing invariant F of
  Cat^perf.

H2 constant bare sheaves
  The category at the place is Shv(T_logp; C) with fixed dualizable
  coefficient category C. The only p-dependence in the space is the
  quotient circle R/(log p)Z.

H3 no retained metric/enrichment
  The circumference log p is not retained as metrized coefficient
  data, analytic-ring data, density data, equivariant group data, or
  an explicit kernel/correspondence.

H4 natural localizing-invariant operations only
  The allowed downstream operations are functions, maps, or traces
  naturally built from the localizing-invariant outputs on the bare
  sheaf categories and their lattice diagram.
```

If any of H1-H4 is removed, the result is no longer this theorem. The
escape routes in section 7 are exactly the useful ways to remove them.

## 3. Cited Dependencies

This draft depends on the following local citations.

```text
MM sec 2(c)
  Records Efimov, "K-theory and localizing invariants of large
  categories", arXiv:2405.12169, at theorem level:

  - Theorem 0.2:
      for X locally compact Hausdorff and C dualizable,
      F^cont(Shv(X; C)) = Gamma_c(X, F^cont(C))
      for finitary localizing invariants F.

  - Proposition 4.18:
      U^cont_loc(Shv(R; C)) = Omega U^cont_loc(C).

  - Theorem 6.1:
      for X a finite CW complex and C dualizable,
      F^cont(Shv(X; C)) = F^cont(C)^X.

research/work/XX-b1-liquid.md sec 1.2
  States Corollary XX.1: no sheaf-theoretic/localizing-invariant
  trace on Shv(R/(log p)Z) distinguishes p. It gives the two-layer
  proof: scaling homeomorphism plus Efimov naturality for the lattice
  diagram.

doc 45 clauses A1 and A4
  A1 requires log p to live in metrized/liquid/analytic-ring/
  equivariant/kernel data, not in bare Shv(R/(log p)Z; C).
  A4 requires comb and continuum to be coupled on the same
  index/Gram form.

doc 48 T48.1
  Names this theorem target and its program consequence: the cheap
  liquid-circle route is permanently closed.

doc 62
  Audits the archived Efimov PDF against the local transcription.
  It confirms the core circle statement as directly citable and marks
  the full lattice-diagram statement as a derived naturality lemma
  that should be proved separately in any polished version.

doc 63
  Supplies that derived naturality lemma: the bare diagrams
  lZ -> R -> R/lZ are isomorphic by scaling, so any functorial
  localizing-invariant observable of the bare diagram is independent
  of l.
```

Thus the proof is candidate theorem-grade after citation/transcription
audit if the local transcription of Efimov's cited results is accepted.
It is conditional in the ordinary bibliographic sense that the proof
imports those external theorems rather than re-proving them.

## 4. Proof Skeleton

### Step 1: The bare circle forgets circumference

For every `l > 0`, the map

```text
x mod lZ |-> x/l mod Z
```

is a homeomorphism

```text
R/lZ ~= R/Z ~= S^1.
```

Therefore, at the level of bare spaces with constant coefficients,
`Shv(T_l; C)` is equivalent to `Shv(S^1; C)`. In particular, any
invariant of the bare sheaf category alone cannot distinguish `l`.
This elementary part already kills any claim that the category
`Shv(R/(log p)Z; C)` itself remembers the numerical circumference
`log p`.

### Step 2: Efimov closes the functorial loophole

The elementary argument does not by itself rule out a more subtle
claim: perhaps `log p` could be recovered from the position of the
circle inside the diagram

```text
(log p)Z -> R -> R/(log p)Z
```

or from the functorial maps induced by that diagram.

Efimov's formulas, as recorded in MM and XX, rule this out for
continuous localizing invariants. Since `T_l` is a finite CW complex,
Theorem 6.1 gives

```text
F^cont(Shv(T_l; C)) ~= F^cont(C)^{T_l}
                  ~= F^cont(C)^{S^1}.
```

The right side depends on `T_l` only through the finite homotopy type
`S^1`. Likewise, Theorem 0.2 and Proposition 4.18 compute the
localizing-invariant data of the line and the lattice pieces by
proper-homotopy data. After applying these invariants, the diagram

```text
lZ -> R -> R/lZ
```

has the same localizing-invariant image as

```text
Z -> * -> BZ.
```

This diagram is independent of `l`, hence independent of `p`.

### Step 3: Natural traces cannot reintroduce log p

By H4, any proposed trace value or gate observable is a natural
function of the localizing-invariant outputs and their induced maps.
Those outputs and maps are already independent of `log p`. Therefore
no such trace can distinguish `log p` from `log q`; in particular it
cannot produce a place-dependent scale, a `2 pi / log p` spacing, a
`1 / log p` residue, or a `kappa` observable as a function of the
bare localizing-invariant sheaf data.

### Step 4: Translate to doc 45 clause failure

Doc 45 A1 requires that `log p` live inside the candidate address as
metric, liquid, analytic-ring, equivariant, or kernel data. The
object under H1-H4 has no such retained data after the trace factors
through the localizing invariant. It is scale-blind.

Doc 45 A4 requires the trace to couple the prime-power comb and the
continuum on the same index/Gram form. A trace that has forgotten
`log p` cannot couple the comb spacing/residue data to the continuum
scale on that form. Any later insertion of `log p` is extra data not
provided by the bare localizing-invariant trace.

Hence the proposed object fails the liquid-address clause before the
carrier, unit, positivity, or second-evaluation clauses are reached.

## 5. What This Kills

The no-go kills the following candidate classes.

```text
K1 bare circle address
  Any route whose p-place is only Shv(R/(log p)Z; C) with constant
  coefficients.

K2 continuous localizing traces of the bare circle
  Any K-theory, localizing motive, or analogous continuous
  localizing-invariant trace applied only to the bare sheaf category.

K3 localizing-invariant traces of the bare lattice diagram
  Any attempt to recover log p from the localizing-invariant image of
  (log p)Z -> R -> R/(log p)Z.

K4 cheap liquid-circle substitutions
  Any claim that replacing S^1 by R/(log p)Z in a topological or
  sheaf-theoretic localizing trace supplies the missing liquid
  address.

K5 post-hoc scale insertion
  Any construction that computes a scale-blind trace first and then
  appends log p, 2 pi/log p, or 1/log p as an external normalization.
  That may be a calibration, but it is not a candidate-native address.
  See doc 80 for the standalone late-insertion lemma.
```

Program consequence: T48.1 becomes a reusable gate. A future
candidate that factors through K1-K5 should be rejected at the A
clause, without running a numerical or positivity cycle.

## 6. What This Does Not Kill

The theorem does not rule out any of the following, because each one
violates at least one hypothesis above in a way doc 45 explicitly
allows.

```text
N1 metrized coefficients
  Coefficient systems or module categories whose values carry metric
  or growth data depending on log p.

N2 liquid/gaseous analytic-ring modules
  Categories such as modules over a liquid/gaseous function algebra on
  T_logp. MM sec 2(d) records that THH/K/localizing invariants of
  liquid analytic rings over R are not computed in print; Efimov's
  theorem for bare Shv(X; constant C) is silent here.

N3 equivariant or parametrized traces
  Genuine traces that remember the group object T_logp, a family of
  groups, or an Aut(T)= {+-1} rigidity datum, rather than only the
  homotopy type of the underlying space.

N4 explicit kernel or correspondence traces
  Nonlocalizing traces of a specified comb/continuum kernel,
  Fourier-Sato object, microlocal correspondence, or LS4-style
  banked comb against R. These are covered only if they first factor
  through the bare localizing-invariant data.

N5 non-Sp-linear liquid trace theories
  A genuinely liquid-linear or gaseous-linear localizing-motive theory
  in which the base, unit, duality, and trace are liquid objects. MM
  marks this as unwritten, not impossible.
```

These are not loopholes to ignore the theorem; they are the precise
places where a live candidate must put the missing structure.

## 7. Escape Hatch

A candidate escapes this no-go only by exhibiting a first structural
map at which `log p` remains visible before any external
normalization is inserted.

Acceptable escape profiles include:

```text
E1 metric/liquid coefficient escape
  Build the p-place as a module category over a metrized or
  liquid/gaseous analytic ring whose norms, growth conditions, or
  density data depend on log p. Then prove the trace is not equivalent
  to a trace of Shv(S^1; constant C).

E2 analytic-ring trace escape
  Define the trace on dualizable modules or perfect kernels over the
  analytic ring of T_logp, and show where the circumference enters
  the trace formula structurally.

E3 equivariant rigidity escape
  Use the group object T_logp and its rigidity, not merely its
  underlying homotopy type, and prove the localizing trace is
  genuinely equivariant or parametrized over that group datum.

E4 kernel-trace escape
  Give a specific comb/continuum kernel or correspondence whose trace
  directly couples (log p)Z and R, and prove that the construction
  does not factor through the scale-blind localizing-invariant value
  F^cont(Shv(T_logp; C)).
```

In all cases the escape must be candidate-native. If `log p` appears
only as a chosen normalization after a scale-blind trace has already
been computed, the candidate remains killed by section 5.

## 8. Candidate Gate

Use this gate before any future numerical, positivity, or
second-evaluation test.

```text
G51.1 Identify the p-place.
  Is it only Shv(R/(log p)Z; C) with constant coefficients?
  If yes, reject by Step 1.

G51.2 Identify the trace functor.
  Does it factor through continuous localizing motives or an
  accessible/finitary continuous localizing invariant of the bare
  sheaf category?
  If yes, reject by Steps 2-4 unless an enrichment is named before
  the trace is formed.

G51.3 Locate log p.
  Point to the first object, coefficient, group datum, analytic ring,
  density, or kernel where log p is present. If no such object exists,
  reject by A1.

G51.4 Check coupling.
  Show that the same structure that remembers log p also couples the
  prime-power comb and the continuum on the index/Gram form. If the
  trace is scale-blind and log p is appended later, reject by A4.

G51.5 Classify the escape.
  If the candidate claims to escape, classify it as E1, E2, E3, E4,
  or something stronger, and require a theorem that it does not
  factor through the scale-blind localizing-invariant data.
```

Passing G51 does not prove the missing structure exists. It only keeps
the candidate alive past the liquid-address no-go.

## 9. Grade

The result is candidate theorem-grade for the class H1-H4 after
citation/transcription audit, conditional on the Efimov theorems
exactly as cited and transcribed in MM/XX. It is not a theorem about
the live liquid analytic-ring or kernel-trace route; for those routes
it supplies the falsification boundary and the first gate a proposed
construction must clear.
