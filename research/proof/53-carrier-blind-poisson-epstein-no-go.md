# 53 - Carrier-blind Poisson/Epstein no-go

Status: second broad no-go proof draft, 2026-06-11. This turns
T48.2 from doc 48 and the B0 Epstein guard from doc 49 into a
theorem-shaped carrier test. It is a negative result about
theta/Poisson/LCA/lattice/multiset formalisms whose input category is
too broad; it is not a no-go for a genuine Euler-product carrier. Doc
74 applies this mechanism to the S3 explicit-kernel slot.

## 1. Statement

Let `F` be a proposed trace/coupling formalism whose domain is built
from one of the following carrier-blind input types:

```text
locally compact abelian groups with Haar density;
lattices in locally compact abelian groups;
cocompact lattice diagrams and their Pontryagin-dual diagrams;
theta kernels and Poisson summation data;
positive represented-norm multisets with their theta series;
Dirichlet-series coefficient multisets before Euler-product structure;
regularized determinant or coker-det presentations of the same data.
```

Assume that `F` produces a comb/continuum trace comparison, or an
LS4-like trace coupling, functorially from only this input. Assume
also that the same construction is defined for:

```text
the prime-power valuation tower p^Z or its Lambda(p^k) comb; and
an Epstein represented-norm replacement; or
a Davenport-Heilbronn-type non-Euler-product replacement.
```

Then `F` is not the load-bearing Euler-product carrier required by
doc 45. More precisely, it fails doc 45 clauses B2 and B3 before any
sign, positivity, or zero-side test is reached.

Equivalently:

```text
If the same trace/coupling computes for Epstein or DH controls, then
the construction has already overreached. It is PD/theta/count-grade,
not Euler-product-carrier-grade.
```

## 2. Hypotheses

The theorem uses the following hypotheses.

```text
H1 carrier-blind domain
  The construction is defined on LCA groups, lattices, lattice
  diagrams, Haar densities, theta/Poisson data, represented-norm
  multisets, or coefficient multisets before imposing valuation or
  unique factorization structure.

H2 functorial trace/coupling
  The trace, theta transform, Poisson comparison, regularized
  determinant, or comb/continuum coupling is natural for maps in the
  carrier-blind domain.

H3 common control inputs
  The domain contains both the prime-power input used by the candidate
  and at least one Epstein or DH replacement with the same input type.

H4 no separate Euler-product subdomain
  The construction has not named a smaller structural domain on which
  prime-power classes, valuation towers, graph depths, or Euler-product
  factorization are native and on which Epstein/DH replacements are
  unformable.

H5 no hidden promotion data
  The construction does not add a candidate-native unit, nonempty
  unforced odd slot, full index form, or comparison theorem that
  changes the domain before the Epstein/DH test is run.
```

Removing H4 is the intended escape route. Removing H1 by adding
metric/liquid analytic-ring/equivariant/kernel data may escape this
theorem only if that added data also creates the structural death
specified in section 8.

## 3. Local Dependencies

This draft depends on the following local record.

```text
doc 45 A4
  The trace must couple comb and continuum on the same index/Gram
  form. A separate positive archimedean block is the wrong shape.

doc 45 B2
  DH and Epstein must fail by non-existence or undefinability of the
  carrier or coupling, while theta/PD shadows may remain alive.

doc 45 B3
  A construction that computes verbatim for Epstein or DH has not
  found the load-bearing Euler-product carrier.

doc 46 Gate 3
  At the first LS4-like coupling, replace the multiplicative
  prime-power carrier by an Epstein-shaped lattice. The required
  profile is: theta/PD/count layer survives; liquid coupling through
  b(comb_p) is undefinable; failure occurs at carrier/effectivity, not
  at a later sign estimate.

doc 46 F1
  If the p^Z/q-expansion grading can be replaced by an arbitrary
  lattice grading and the coupling still computes, the verdict is
  carrier-blind and the Epstein guard has failed.

doc 49 B0.4
  For Q=x^2+5y^2, the theta/count layer represents 1,4,6,9,36 while
  2 and 3 are absent. The represented-norm monoid has irreducibles
  4,6,9 but 36=4*9=6*6. Thus the count/Poisson shadow survives, while
  a free rank-one valuation or q-tower address is not formable.

doc 64
  Supplies the proof-level Epstein carrier-guard lemma behind this
  finite check: the theta/count layer is alive, but represented-norm
  factorization does not provide a free prime-power valuation/tower
  address.

doc 17 sec 4
  Epstein zeta functions give nonnegative count structures with
  functional equations and tempered behavior, but have off-line zeros.
  Counts, self-duality, and temperedness do not force the critical
  line; the Euler product remains the discriminating ingredient.

doc 41 OC4
  A candidate that can be run verbatim on Epstein/DH has not found the
  Euler-product carrier.
```

## 4. Proof

Let `C_blind` be the input category on which the proposed formalism is
defined. By H1, objects of `C_blind` are LCA/lattice/theta/Poisson or
represented-multiset objects before the addition of a native
Euler-product carrier. By H2, the claimed trace/coupling is a
functorial construction on `C_blind`.

By H3, there are objects

```text
P in C_blind
E in C_blind
```

where `P` is the prime-power or valuation-tower input and `E` is an
Epstein or DH replacement of the same formal input type. Since the
trace/coupling is functorial on `C_blind`, the same construction that
computes on `P` also computes on `E`. No sign estimate, positivity
test, zero-side test, or numerical window is needed for this step: the
failure is already a domain statement.

Now compare this with doc 45 B2. B2 requires DH and Epstein to fail by
non-existence or undefinability of the carrier or coupling, while
theta/PD shadows may remain alive. But under H1-H4, the carrier or
coupling is defined on `E`. Therefore the required B2 death point is
absent.

Compare also with doc 45 B3. B3 says that a construction computing
verbatim for Epstein or DH has not found the load-bearing
Euler-product carrier. Under H2-H3, the construction computes
verbatim for `E`. Therefore B3 fails.

This proves the no-go:

```text
carrier-blind common domain + functorial trace/coupling
  + Epstein/DH object in the same domain
  => B2/B3 failure before sign testing.
```

The conclusion is independent of whether the Epstein/DH control later
has bad signs, off-line zeros, or failed positivity. Those later
failures are too late. The program's carrier guard demands structural
unformability at carrier/effectivity.

## 5. Concrete Guard: Q=x^2+5y^2

Use the positive binary quadratic form

```text
Q(x,y) = x^2 + 5y^2.
```

Its theta/count layer is ordinary lattice data:

```text
theta_Q(t) = sum_(x,y in Z) exp(-pi t Q(x,y)).
```

The represented norms include:

```text
1  = Q(1,0)
4  = Q(2,0)
6  = Q(1,1)
9  = Q(3,0)
36 = Q(6,0) = Q(4,2)
```

and the norms `2` and `3` are not represented. In the represented-norm
monoid generated by this data, the elements `4`, `6`, and `9` behave
as irreducible represented norms at the first visible level, but

```text
36 = 4*9 = 6*6.
```

Thus the represented-norm multiset does not carry a free rank-one
valuation tower analogous to

```text
1, p, p^2, p^3, ...
```

and it does not provide a well-defined prime-power address or graph
depth matching Lambda(p^k) classes. The theta series and Poisson
summation still exist. The carrier address does not.

This is exactly the doc 49 B0 guard, with proof isolated in doc 64:

```text
theta/count survives;
Poisson/Pontryagin-dual shadow survives;
valuation/q-tower carrier is unformable.
```

Therefore a candidate passes the Q-guard only if its first
comb/continuum coupling uses the valuation/q-tower structure that
Q=x^2+5y^2 cannot supply. If the same formula can simply substitute
the theta series or represented-norm multiset of Q and continue, the
candidate is carrier-blind.

## 6. Davenport-Heilbronn Control

The same logic applies to a DH-type control in the local record. DH is
used as a non-Euler-product replacement: analytic and coefficient data
may be formable, and explicit numerical sign failures may appear, but
the program does not permit a candidate to survive by computing on DH
and then observing a bad sign.

For B2/B3, the required DH outcome is:

```text
the theta/analytic shadow may remain meaningful;
the Euler-product carrier or trace coupling is undefined;
the rejection happens before zeros, signs, or tracking tests.
```

If a proposed trace/coupling takes DH coefficients, DH functional
equation data, or DH-style LCA/theta inputs and computes the same
comparison as for zeta, then the candidate fails by carrier overreach.
The later fact that DH has the wrong zeros or bad signs does not
repair B2.

## 7. Candidate Gate

Every future trace/coupling candidate must pass this gate before unit,
positivity, or odd-slot testing.

```text
Carrier-Blind Poisson/Epstein Gate

Input:
  A proposed first LS4-like comb/continuum trace coupling T.

Step 1:
  Name the structural domain Dom(T).

Step 2:
  State whether Dom(T) is merely LCA/lattice/theta/Poisson/
  represented-multiset data, or whether it contains native
  prime-power valuation objects, Euler-product factorization, and
  graph-depth classes.

Step 3:
  Replace the prime-power input by Q=x^2+5y^2 represented-norm data.

Required pass profile:
  theta/PD/count layer survives;
  T through the prime-power comb carrier is undefined;
  the first undefined map is named;
  the failure occurs before any sign or zero-side test.

Fail profile:
  T computes after replacing p^Z or Lambda(p^k) by an arbitrary
  lattice, theta series, represented-norm multiset, Epstein zeta
  input, or DH coefficient input.
```

Verdict:

```text
Pass:
  Continue to unit derivation, full-cone positivity, and odd-slot
  supplier audit.

Fail:
  Reject as carrier-blind. The construction may be a valid theta,
  Poisson, count, or PD shadow, but it is not the doc 45
  Euler-product carrier.
```

## 8. Exact Escape Profile

A successful escape from this theorem must exhibit all of the
following data.

```text
E1 native carrier domain
  A structural domain D_Euler whose objects include prime-power
  classes, valuation towers, Lambda(p^k) addresses, Euler-product
  factorization, or graph-depth data as native objects.

E2 first carrier map
  A named first map or operation

      Phi: D_Euler -> target

  used by the trace/coupling, not merely by an interpretation after
  the trace has computed.

E3 Epstein death point
  A proof that the Q=x^2+5y^2 represented-norm multiset has no object
  of D_Euler, or that Phi is undefined on it, while its theta/PD/count
  shadow remains defined.

E4 DH death point
  A proof that the DH replacement has no object of D_Euler, or that
  Phi is undefined on it, before using DH zeros, signs, or tracking
  behavior.

E5 no arbitrary lattice replacement
  A proof that p^Z/q-expansion grading cannot be replaced by an
  arbitrary lattice grading without losing the coupling.

E6 A4 compatibility
  The surviving trace must couple comb and continuum on the same
  index/Gram form. It cannot be a separate archimedean block appended
  to a carrier-blind theta identity.

E7 promotion discipline
  Unit, positivity, odd-slot spectrum, and comparison theorem data are
  introduced only after E1-E6 are satisfied, or else they are part of
  the same structural domain that already causes Epstein/DH
  undefinability.
```

This is the exact useful escape: the Epstein and DH shadows may remain
alive as theta/count/analytic objects, but the candidate's load-bearing
carrier or coupling must be unformable there.

## 9. Consequence

The no-go closes a broad class of cheap upgrades:

```text
plain Poisson summation;
Pontryagin-dual transport;
theta functional equations;
LCA Haar-density trace formulas;
lattice determinant/coker algebra;
represented-norm count formalisms;
coefficient-multiset regularizations before Euler products.
```

These structures may calibrate shadows, as B0 does, but they cannot
serve as the final carrier if they compute for Epstein or DH. The next
valid construction work is therefore narrower:

```text
name the Euler-product carrier first;
name the first trace/coupling map that uses it;
run Q=x^2+5y^2 and DH before any sign test;
proceed only if theta/count survives but the carrier map is undefined.
```
