# CHARTER — the global/archimedean Frobenius

Status: ARC CHARTER, 2026-06-29. Greenfield. This is the standing reference
for the new direction; it fixes the target, the layers, the foundation to
build ON, the risk-ladder, the success spec, and the entry point — BEFORE any
cycle runs. It supersedes the End(S^2/Z) construction arc (old
research/proof/137) by *reframing* its target, *keeping* its proven discipline,
and *discarding* its two failure modes (the monolithic target and the
coherence-tower regress). Read DISCIPLINE.md next.

## 1. Honest framing (read first)

The target is the F_1 / Connes–Deninger object: a Frobenius over the
compactified Spec Z. This is famous and decades-open. The arc is LONG and most
likely does not finish. The charter's job is to make it FAIL-CLOSED so the arc
banks value either way, and to state the scope honestly:

```text
WIN-WIN, stated correctly:
  build it          -> RH (the positive branch).
  prove it is unbuildable in any carrier-blind category
                    -> THIS ROUTE is dead; reorient (the bounded-negative branch).

NOT an iff:
  existence(object) => RH, but  ¬existence  does NOT => ¬RH.
  RH may be true via a route that never builds this object. A construction
  impossibility bounds the ROUTE, never RH.

NO "unknowable" branch:
  RH is Pi_1 (Robin/Lagarias finite-checkable form). A Pi_1 sentence
  independent of a sound theory is TRUE. So "true but unprovable" is
  structurally foreclosed. Do not chase logical independence.
```

## 2. The target, reframed (the primitive, not the monolith)

The prior arc carried the whole square + its involution as one monolithic
target and tried to *manufacture* it. That failed ~400 times. We invert: target
the single hard PRIMITIVE; the square, the duality, and the positivity are
DERIVED theorems about it.

```text
THE PRIMITIVE (the hard thing):
  A GLOBAL FROBENIUS F -- an endomorphism of a global cohomology of the
  compactified Spec Z, with PURITY |eigenvalues(F)| = N^{w/2}. Over F_q this
  is the geometric Frobenius (RH-analogue is a theorem, Weil). Over Z it is
  ABSENT, in particular at the archimedean place. Its three jobs are the three
  walls the prior program hit, now UNIFIED:
    - radius/finiteness  : |eig F| = N^{w/2} pins purity (no finite constant
                           field over Z; the archimedean place has no q).
    - properness         : F invertible, F^dag = (deg) F^{-1} (the two-sided /
                           Laurent / Weil-pairing structure).
    - carrier            : the Euler product IS det(1 - F t)^{-1}; F is the
                           multiplicative carrier.
  ONE missing thing wearing three faces: there is no Frobenius on bar(Spec Z).

LAYER I -- THE STAGE (FE-layer, RH-NEUTRAL):
  the self-product correspondence End on the square C x C and its duality
  structure. Necessary, not sufficient. Stage results are never promoted
  (BB.1 guard, DISCIPLINE.md).

LAYER II -- THE PLAY (RH-GRADE):
  the POSITIVE Rosati involution F^dag = (deg) F^{-1} on End -- the Weil /
  Hodge-index positivity on the square. Its positivity <=> RH. Gated behind
  Layer I + the primitive.
```

## 3. The foundation — build ON this (it is a theorem)

The prior arc's own evidence pointed here: the only tested object that is
NATIVELY GLOBAL + ARCHIMEDEAN and already carries a real curve-level duality
theorem is the Connes–Consani scaling site / adele class space.

```text
DONE (external theorems): Connes–Consani proved, for the compactified Spec Z
  ("the curve"): integer Riemann–Roch + Pontryagin–Serre duality
  (arXiv:2205.01391, 2306.00456), plus the Pic / Jacobian infrastructure
  (2026 Jacobian paper). This is CURVE-LEVEL and a THEOREM. Build ON it; do
  not restart it.

THE GAP (where it breaks, = our R1): CC departs from the function-field
  analogy at the SELF-PRODUCT / SQUARE JOINT (old docs 21/22). The curve-level
  theorem does not yet give the C x C correspondence algebra, the square H^2 /
  intersection form, the Frobenius graph, or the positive Rosati. The square
  joint is the whole problem.

WRONG VENUE (do not return to it): p-local homotopy (TCR(F_2), DMP, one prime)
  sees only the SHADOW of a global object; the prior arc's Z/2 Weyl-shear
  obstruction (c = (1+z)^{-1}, [c] != 0 in H^1(<phi>; 1+zF_2[[z]])) is a
  p-LOCAL ARTIFACT of viewing a global object p-locally. Keep TCR(F_2)/DMP only
  as a PROBE of the fingerprint, never as the construction site.
```

## 4. The success spec (acceptance criteria — when do we know we have it?)

The one durable residue of the prior arc's 400 categorical layers is a RIGIDITY
blueprint. We adopt it verbatim as the acceptance test. The constructed object
must be:

```text
S1  RIGID + CONTRACTIBLE: terminal, endomorphism-trivial, automorphism-rigid,
    internally contractible (no moduli). COROLLARY (binding on method): it
    exists EXACTLY or not at all. You cannot approximate, perturb, insert,
    project, quotient, or select your way in -- any construction that requires
    a noncanonical choice is a category error (this is what killed ~400 prior
    docs). Build it canonically or report the obstruction.
S2  SELF-DUAL: dagger-pivotal, dual-traced, adjoint-paired (the duality that
    carries the Rosati).
S3  EXACT K0 / GROTHENDIECK: an exact additive intersection / H^2 structure
    (the square's intersection form).
S4  HECKE-ACTIVE: carries an integer multiplier (Hecke/Adams) action -- the
    multiplicativity made structural.
S5  CARRIER-NATIVE: DIES on the controls (S6). The Euler product is STRUCTURE,
    not a property bolted on.
S6  CARRIER GUARDS (the death tests): dies on DH (Dirichlet/Hadamard: no Euler
    product) and on Epstein (at multiplicativity / effectivity / address) --
    exhibit the EXACT death point. If a control can also instantiate it, it is
    carrier-blind and is the WRONG object.
```

## 5. The named wall (inherited, load-bearing)

```text
THE CARRIER WALL IS PRIMARY. Of the three faces, multiplicativity (the Euler
product) is the hard one; radius and properness are DOWNSTREAM of having a
genuine multiplicative Frobenius. The missing ingredient, named: MULTIPLICATIVITY
AS NATIVE STRUCTURE, not as a property. Every cycle's first guard question is
"does this make the Euler product structural, or does a control already have it?"
```

## 6. The risk-ladder (order = kills-the-arc x cheapness)

```text
R0  FOUNDATION (done, external): CC curve-level RR + Pontryagin–Serre duality.
    First job is to GROUND it exactly (cycle 0) -- what is proven, in what
    category, with what Frobenius/duality data.

R1  THE ENTRY -- THE SQUARE JOINT: extend curve-level RR / duality to the
    C x C self-product correspondence. The cheapest sharp step that is also the
    real gap. Deliverable: the product correspondence datum (a verified
    sub-object) OR a no-go with a named mechanism (the duality cannot cross the
    product joint, with the exact obstruction).

R2  THE GLOBAL FROBENIUS GRAPH on the square (the primitive): F with purity,
    as a correspondence. Gated behind R1.

R3  LAYER II -- the POSITIVE Rosati / Hodge-index positivity (RH-grade). Gated
    behind R1 + R2. The deepest rung; the play.

Do R0 -> R1 before R2 before R3. Each rung is fail-closed: a negative reshapes
the target and is banked as a named no-go, not hidden.
```

## 7. Entry point + first cycle (pre-registered in 00)

```text
ENTRY = R0 -> R1. First cycle (pre-registered, 00-entry-preregistration.md):
  GROUND   : the exact state of CC curve-level RR + PS duality -- the category,
             the "Frobenius"/scaling data, the duality pairing, the Pic/Jac
             infrastructure; and the precise statement of what BREAKS at the
             self-product joint (square H^2, intersection form, off-diagonal
             correspondences, Frobenius graph).
  PROBE    : construct/identify the product correspondence datum, exit-gated,
             OR prove a named no-go (the duality does not cross the joint).
  VERIFY   : carrier guards (DH/Epstein death); DOF ledger; freeze; the
             rigidity spec (S1-S6); that the datum is genuine duality, not gauge.
  SYNTHESIZE: one deliverable doc (a built sub-object or a named no-go) + the
             updated arc board.
```

This charter is the arc's standing reference. Cycle docs are numbered 00, 01,
… under the DISCIPLINE.md rules.
