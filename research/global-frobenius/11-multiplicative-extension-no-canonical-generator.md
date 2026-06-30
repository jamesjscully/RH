# 11 — the door shuts for known structures: R₊^* has no canonical generator

Status: THEOREM step (T), 2026-06-30. The multiplicative-extension target of
doc 09: does a canonical multiplicative structure at the archimedean place escape
the dichotomy? Result: for every KNOWN canonical archimedean multiplicative
structure, NO -- and the obstruction is one structural fact. Anti-trap checked:
RH-clean. The single residual is the F_1 problem itself.

## The target

```text
doc 09 reduced the program to Q: does a canonical DISCRETE (finite-q) Frobenius
exist at infinity (a discretization of the scaling flow Theta)? doc 08 + doc 10
close the ADDITIVE class. The multiplicative extension asks whether the
NON-additive (multiplicative) door escapes. Target theorem:
  "every canonical archimedean multiplicative structure has CONTINUOUS spectrum"
  -- which (via doc 09) forces the transcendental self-intersection, extending
  the dichotomy from additive to multiplicative.
```

## The structural argument (named mechanism: no canonical generator)

```text
(1) THE ARCHIMEDEAN MULTIPLICATIVE SYMMETRY is the value group R_+^* (the scaling
    action / Connes' flow / the generator of Deninger's Theta). R_+^* ~= (R,+)
    via log: CONNECTED, divisible, torsion-free.

(2) NO CANONICAL GENERATOR. A discrete Frobenius is a distinguished generator of
    the value group (a canonical "q"). The finite place p HAS one: its value
    group is p^Z ~= Z, with canonical generator p (Frobenius) -- Z has exactly two
    generators (+-1), a canonical one up to inversion. The archimedean value group
    R_+^* ~= R has NO canonical generator: Aut(R,+) = R^* acts TRANSITIVELY on
    R \ {0}, so no element is distinguished. Choosing a "q at infinity" is a
    NON-CANONICAL choice.

(3) CANONICITY (S1) FORBIDS THE CHOICE. The success spec S1 requires the object
    canonical / no-moduli / no noncanonical choice (the prior arc's
    "manufacturing-by-choice is a category error"). A discrete archimedean
    Frobenius requires choosing a generator of R_+^* -- forbidden by S1.
    => no CANONICAL discrete archimedean Frobenius from the value group.

(4) CONTINUOUS SPECTRUM. R_+^* connected (non-compact abelian) has Pontryagin
    dual R: any structure equivariant for the scaling decomposes over the
    CONTINUOUS dual R (Connes' spectral realization: the scaling flow's spectrum
    is the critical line, continuous). So the archimedean multiplicative structure
    has continuous, not discrete (lattice), spectrum.

(5) CONTINUOUS => TRANSCENDENTAL (the dichotomy bites). A discrete lattice
    spectrum {q^{w/2}} gives self-intersection in Q.log q (finite-place type); the
    continuous archimedean spectrum gives the regularized determinant = -zeta'(0)
    = (1/2)log 2pi, which is PROVABLY not finite-place type (Lindemann; CERTIFIED
    gf_archimedean_no_finite_q, doc 09). So the multiplicative door, occupied by
    the scaling flow, reproduces the transcendental horn. QED for the value group.
```

## Covering the other known multiplicative structures

```text
- NORM / Tambara at infinity: the only archimedean norm is for C/R, Gal = Z/2
  (complex conjugation, order 2). Its eigenvalues are +-1 -- a trivial finite
  group, NOT a q-power Frobenius with growing |q^{w/2}|. No discrete purity.
- delta-rings / Borger Lambda-rings: the Lambda-structure has one Frobenius lift
  psi_p per FINITE prime p; there is NO psi at infinity (no archimedean Frobenius
  congruence in char 0). The global delta-structure is silent at infinity.
=> every KNOWN canonical multiplicative structure at infinity is either CONTINUOUS
   (the scaling flow R_+^*) or TRIVIAL-FINITE (Z/2 conjugation) -- neither is a
   discrete q-power Frobenius. The door shuts for all known structures.
```

## Net status: the door shut, and the one residual = F_1

```text
The dichotomy now extends from ADDITIVE (doc 08) to (known) MULTIPLICATIVE
(this doc): no canonical structure in either class -- additive/localizing OR known
multiplicative (scaling, norm, Lambda/delta) -- yields a finite integer
self-intersection. The bounded-negative branch is COMPLETE over the canonical
class as currently known.

THE SINGLE RESIDUAL (genuinely open): an UNKNOWN, exotic canonical structure that
supplies a discrete generator of the archimedean value group -- a canonical "q at
infinity" -- WITHOUT a noncanonical choice. That is precisely the F_1 / Connes-
Deninger problem: make infinity a finite-place-like point with a Frobenius. The
program CANNOT close this without solving F_1; it has REDUCED "is the dichotomy
fundamental?" to "does a canonical q at infinity exist?" = the F_1 problem.
```

## Anti-trap + scope + grade

```text
RH-CLEAN: the argument uses only the structure of R_+^* (connected, no canonical
generator) and S1 (canonicity) -- no zeros, no positivity. Not a circling to
RH-equivalence (Outcome-D guard passed).
SCOPE: bounds the route over the FULL known canonical class; the residual (an
exotic canonical archimedean discretization = F_1) is the POSITIVE escape, not RH.
GRADE: structural (named mechanism: R_+^* has no canonical generator) +
Certified link continuous->transcendental (Lindemann, gf_archimedean_no_finite_q).
Not witness-backed at step (2)-(3) -- those are structural facts about R_+^*
and S1, stated as such, not numerics.
```

## Convergence (eighth, and the terminus)

```text
The asymmetry "Z has a canonical generator (Frobenius p); R has none" IS the F_1
problem, now pinned as the SOLE door. Every face of the wall (additive/
multiplicative, integer/transcendental, discrete/continuous, finite-place/
archimedean, properness) reduces to: infinity's value group R_+^* has no canonical
generator. The wall is fully drawn; there is exactly one door, and the door = a
canonical q at infinity = F_1. The bounded-negative program has reached its
natural terminus: it has proved the dichotomy for the entire known canonical
class and reduced the lone exception to the F_1 problem itself, which it cannot
adjudicate from inside.
```

## Next

The program has reached the limit of what the bounded-negative branch can
establish without solving F_1. Two coherent end-states for review:
  (a) BANK IT: write the combined theorem (docs 08+10+11) -- "the dichotomy is
      fundamental over the known canonical class; the sole exception is a
      canonical q at infinity (F_1)" -- with O1's residual (iv,
      regularization-uniqueness) and the F_1 residual both named. This is the
      durable contribution: the wall, fully mapped, with one labelled door.
  (b) ATTACK THE DOOR: take on F_1 directly (does a canonical q at infinity
      exist?) -- the positive branch, a famous open problem, unbounded.
Recommend (a): bank the mapped wall; (b) is the open frontier, not a bounded cycle.
```
