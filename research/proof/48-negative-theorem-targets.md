# 48 - Negative theorem targets

Status: 2026-06-11. Branch from doc 45 sec 8: negative theorem work.
Reads docs 41-45 and MM. This is a theorem-target list, not a proof
and not a construction.

## 1. Purpose

Doc 45 characterizes the missing structure by five required clauses:

```text
A. liquid address
B. Euler-product carrier
C. unit and threading
D. index positivity and exhaustion
E. second evaluation
```

The negative branch should prove impossibility/no-go theorems for broad
ambient classes. A useful negative theorem does not merely say that a
banked carrier failed. It says that every object in a natural class must
fail one of A-E for structural reasons, thereby sharpening where the
missing structure could still live.

The best current target shape is:

```text
Every successful candidate must escape all of the following classes:

bare localizing sheaf traces
carrier-blind theta/Poisson lattice formalisms
inserted or one-place continuum units
strict-face/index-window positivity
transport/self-supplied second evaluations
```

## 2. Priority Targets

### T48.1 Scale-Blind Localizing Trace No-Go

Clause attacked: A.

Theorem-shaped target:

```text
Let C be a dualizable coefficient category and let F be any finitary
continuous localizing invariant in the sense of Efimov. For
T_l = R/lZ, the value F(Shv(T_l; C)) is naturally equivalent to
F(C)^{S^1}. In particular it is independent of l.

Consequently no candidate whose liquid address is represented only by
bare sheaf categories Shv(R/(log p)Z; C), or by their continuous
localizing-invariant traces, can satisfy A1 or A4.
```

Assumptions to make explicit:

```text
1. The trace factors through continuous localizing motives or a
   finitary continuous localizing invariant.
2. The only p-dependence in the category is the topological circle
   R/(log p)Z, with no metrized coefficient, analytic-ring, kernel,
   equivariant, or density data retained.
```

Consequence for the program:

```text
This permanently closes the cheap liquid-circle route. The object must
live in metrized/liquid analytic-ring data or a nonlocalizing kernel
trace where log p remains visible.
```

Minimal proof route:

```text
Use Efimov's formulas cited in MM: for locally compact X and dualizable
C, F^cont(Shv(X; C)) = Gamma_c(X, F^cont(C)); for finite CW X,
F^cont(Shv(X; C)) = F^cont(C)^X. Since all T_l are homotopy S^1,
the output forgets l. Then observe that A1 needs log p and A4 needs
comb/continuum coupling on the same index form; both are absent after
the invariant factors through S^1.
```

Counterexample/escape route:

```text
Exhibit a trace that does not factor through continuous localizing
motives and whose definition uses analytic-ring, metric, character
kernel, or density data on T_l. Such an escape would not refute T48.1;
it would locate the needed extra structure.
```

### T48.2 Carrier-Blind Poisson/Epstein No-Go

Clause attacked: B, with spillover to A4 and E.

Theorem-shaped target:

```text
Let a proposed trace-coupling formalism depend only on a locally
compact abelian group, a lattice, a Haar density, and Poisson/theta
duality data. If the formalism produces its comb/continuum comparison
for every cocompact lattice or represented-norm multiset with the same
input type, then it cannot satisfy B2/B3.

In particular, any such formalism that computes for Epstein-shaped
rank-two norm data as well as for prime-power valuation towers is not
a load-bearing Euler-product carrier.
```

Assumptions to make explicit:

```text
1. The construction is functorial for lattices or LCA groups before
   imposing unique factorization / valuation monoid data.
2. Its trace, theta, or Poisson layer remains defined for Epstein/DH
   controls.
3. The candidate does not contain a separate structural domain on
   which prime-power classes exist and Epstein/DH classes do not.
```

Consequence for the program:

```text
This turns the DH/Epstein guard into a theorem-level kill test: death
must be undefinability of the carrier/coupling, not a later bad sign.
Any candidate that merely appends positivity to a lattice-theta theory
is PD-grade, not Euler-product-grade.
```

Minimal proof route:

```text
Formalize the common input category of the proposed construction. Show
that its objects include both p^Z valuation towers and Epstein norm
lattices, and that the trace/coupling maps are defined functorially on
both. Then compare with doc 45 B2/B3: the carrier guard demands
non-existence or undefinability for DH/Epstein. A construction defined
on both fails before numerical testing.
```

Counterexample/escape route:

```text
Produce the first structural map whose domain is a multiplicative
prime-power/valuation category and prove that the analogous Epstein
norm multiset has no object in that domain, while its theta/PD shadow
still exists. This is the death-at-effectivity profile required by MM.
```

### T48.3 One-Place or Inserted Unit No-Go

Clause attacked: C, especially C1-C3 and C5.

Theorem-shaped target:

```text
Let U be a continuum unit chosen externally, placewise, or up to an
unfixed normalization torsor, and let all local slot/payment constants
be functionals of U. Then signs of deep-cell slot data are not object
conditions. No theorem depending on a chosen U can establish C1-C3 for
the missing structure.

Moreover, any one-place construction whose charge/payment is computed
before global KMS-beta=1/2 assembly cannot satisfy global threading:
it can at most produce local bookkeeping or slot data.
```

Assumptions to make explicit:

```text
1. U is inserted or selected from an admissible family instead of
   derived as a candidate-native fixed unit.
2. The claimed obstruction is expressed by Mellin/Fourier slot
   constants of U, not by a unit-covariant carrier theorem.
3. The construction evaluates each Lambda(p) class independently and
   does not contain a structural cross-place transfer/assembly map.
```

Consequence for the program:

```text
This prevents re-promoting Gaussian deep-cell failures, strict repairs,
or one-place Poisson normalizations. The live C-claim is narrower:
k=1 local deficit, global cross-place payability, and the unit-free
depth wall with law constant 1.
```

Minimal proof route:

```text
Use doc 43 as the model lemma: the Gaussian cell (11;2)@4.96 is
negative, but an admissible self-dual Hermite unit flips it positive.
Abstract the argument: if an obstruction changes under admissible
unit replacement while the candidate class is unchanged, it is slot
data. Then prove that a one-place trace lacks the product-formula or
KMS-beta=1/2 assembly needed to move surplus across places.
```

Counterexample/escape route:

```text
Derive U internally from an LS3-style Fourier self-duality whose
normalization is pinned by internal T=R/Z rigidity, then prove C1-C3
in a unit-covariant form. A successful escape must explain why the
Hermite flip changes only slot diagnostics and not the theorem.
```

### T48.4 Strict-Face Positivity No-Go

Clause attacked: D.

Theorem-shaped target:

```text
Let I be a forced-nonnegative index/Gram/count form certified only on
a strict square family, a finite scanned window, a rung tower, or any
proper subcone that omits k=1 boundary directions, recurrent deep
graph steps, mixed towers, or real/conic directions of the doc-00
Sonin/Frobenius-graph core. Then I cannot satisfy D2-D4.

If the extension to the full graph cone requires a hand-inserted unit
or signed analytic correction, it also fails D1/D3.
```

Assumptions to make explicit:

```text
1. Positivity is proved for a named family strictly smaller than the
   full Frobenius-graph cone.
2. The proof does not supply a candidate-native unit or a uniform
   infinite-support filtration argument.
3. The missing directions include any of the hard boundary classes
   named in docs 43-44.
```

Consequence for the program:

```text
This promotes doc 44's banked failure into a reusable theorem target:
BC13 is not a positivity estimate on a favorable face. It is forced
nonnegativity plus full class/scale exhaustion.
```

Minimal proof route:

```text
Define the ambient graph cone and the certified subfamily. Prove the
subfamily is a proper cone/family by exhibiting one omitted direction
type, preferably k=1 prime atoms or a recurrent deep graph direction.
Then show doc 45 D2 requires the omitted direction. If the proposed
repair inserts a unit, invoke D3 and doc 43's unit-covariance demotion.
```

Counterexample/escape route:

```text
Give a theorem that the positive family spans the full graph cone and
persists along the infinite support filtration using the candidate's
own unit. Numerical panels or strict-square embeddings are not enough.
```

### T48.5 Transport and Self-Supplied Spectrum No-Go

Clause attacked: E.

Theorem-shaped target:

```text
Let a proposed comparison between count and spectral/index sides be
implemented by a chain of natural isomorphisms, Poisson transport,
Pontryagin duality, coker=det algebra, regularization of one series,
or an acting correspondence whose degree/input supplies the spectral
eigenvalues. Then the comparison is one evaluation or a forced-spectrum
evaluation. It cannot satisfy E1-E4.
```

Assumptions to make explicit:

```text
1. The two sides have the same natural extension domain, or one side
   is transported functorially into the other without extra content.
2. The odd slot is empty, or its eigenvalue is the acting map's degree,
   the chosen scale, a regularization input, or zero-side data.
3. The agreement theorem consumes only definitions or formal algebra.
```

Consequence for the program:

```text
This classifies solenoid, TP/TR transport, bare Poisson, coker=det,
and finite-field empty-slot analogues as models or controls, never as
decision-grade candidates. It also explains why Quillen over F_q is
only a pattern: it has the two-evaluation silhouette but not the
needed unforced odd spectrum.
```

Minimal proof route:

```text
For each proposed comparison, identify the natural domains of the two
evaluations and the supplier of the spectral parameter. If domains
coincide by construction or the parameter is the acting map's own
degree, the comparison fails E1/E3. If the odd slot is zero, it fails
E2. If the agreement is definitional, it fails E4.
```

Counterexample/escape route:

```text
Produce two evaluations with genuinely different extension domains and
a theorem cutting out their common agreement locus, while the odd-slot
eigenvalues are supplied by the carrier/slot structure independently
of the querying action.
```

## 3. Lower-Priority Targets

### T48.6 p-Complete Blindness No-Go

Clauses attacked: A and E.

Target:

```text
A purely p-complete TP/TR/Witt construction without an internal
archimedean iota, R/T object, or liquid trace cannot satisfy A2/A4, and
any comparison obtained by Witt/TR transport cannot satisfy E1/E3.
```

Use:

```text
This would formalize why p-complete towers are supply/address shadows
only. It is lower priority because docs 42 and MM already isolate the
failure sharply; the stronger work is proving what an admissible
archimedean escape must contain.
```

### T48.7 Max-Gram/Signature Insufficiency No-Go

Clauses attacked: D and E.

Target:

```text
Lorentzian signature, max-Gram positivity, or stress-flow data alone
cannot provide E's independent odd-slot comparison. Even when they
certify a sign shape, they remain supply-grade unless paired with a
P3-grade second evaluation.
```

Use:

```text
This prevents Gram-shape certificates from being mistaken for the
missing theorem. It is lower priority because it is an insufficiency
result, not yet a broad categorical impossibility.
```

### T48.8 Zero-Import Circularity No-Go

Clauses attacked: E and the global freeze protocol.

Target:

```text
Any construction that reads eigenvalues, signs, or class choices from
zeta zeros before constructing the carrier and comparison theorem is
circular and cannot satisfy E3/E4.
```

Use:

```text
This is logically important but not the most characterizing theorem,
because the current branch already avoids zero-side input. It should
remain a gate on future candidates.
```

## 4. Suggested Order

The negative theorem branch should proceed in this order:

```text
1. T48.1 scale-blind localizing trace no-go.
   It is closest to a citable theorem now and closes the broadest cheap
   liquid address class.

2. T48.5 transport/self-supply no-go.
   It turns BC-E3' into a reusable diagnostic theorem and covers many
   tempting analogues at once.

3. T48.2 carrier-blind Poisson/Epstein no-go.
   It formalizes the carrier guard and prevents lattice-theta
   overreach.

4. T48.4 strict-face positivity no-go.
   It is the D-side analogue of the carrier guard: forced positivity
   must exhaust the cone, not a favorable subfamily.

5. T48.3 one-place/inserted unit no-go.
   It is necessary, but likely depends on first making "admissible
   unit" and "candidate-native unit" field-native.
```

The main conclusion is negative but useful: the missing structure is
not hidden in any formalism that forgets scale, computes for all
lattices, inserts its continuum unit, proves positivity only on a
strict face, or identifies the second evaluation by transport. A real
candidate must escape all five no-go classes simultaneously.
