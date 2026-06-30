# 07 — the class C and the additive/non-additive line (the door, located)

Status: ATLAS step (M), 2026-06-29. Phase-1 dual cycle (doc 05), M-deliverable.
Refines far-side faces F4 (class boundary) and F1 (the door). Grade: Reading
(conceptual characterization; framework cited, no new witness). Corrects an
over-hopeful reading of the squeeze in doc 03.

## What the dichotomy actually quantifies over

```text
C = INTEGER-VALUED ADDITIVE / LOCALIZING INVARIANTS. Precisely: a localizing
invariant (Blumberg-Gepner-Tabuada) E : Cat^perf -> (stable target) sends a
Verdier/exact sequence A -> B -> C to a (co)fiber sequence E(A) -> E(B) -> E(C);
"integer-valued" = the relevant homotopy/rank lands in Z. Members: K_0, ranks,
Euler characteristics, dim_S, CC's integer dimension, the TC/THH component
counts, Bost-Connes / Borisov dimensions, Efimov continuous traces.
```

Why additivity is load-bearing for the wall (not incidental):

```text
A1 (effective => log growth): effectivity = the invariant is the rank of a finite
   presentation / the size of a minimal generating set, so it grows like
   log_b(size). [The entropy; forces W1's hypothesis.]
SELF-INTERSECTION = THE ADDITIVE TOWER SUM: in a localizing invariant the
   diagonal decomposes additively over the cells of the tower, so <Delta,Delta>
   IS the additive regularized total of the invariant down the tower. ADDITIVITY
   is exactly what forces <Delta,Delta> to be that sum -- which W1 (doc 06) shows
   diverges, and doc 04 shows the 2-variable square cannot rescue.
```

So the wall is: **integer + additive + effective => the self-intersection is the
divergent log-tower sum** (side A, now W1-proved for the whole class); and
**additive + summable => scale-blind** (side B, Efimov). The class C is precisely
where both horns bite.

## The boundary of C = the additive/non-additive line = the door (F4 => F1)

```text
The FIRST structure outside C drops ADDITIVITY. The canonical non-additive
operations are exactly the MULTIPLICATIVE ones:
   - norms / Tambara functors (multiplicative transfers; the HHR norm),
   - Frobenius / delta-ring structures (phi(x) = x^p + p delta(x)),
   - lambda-operations / Adams operations.
These are non-additive BY DESIGN (a norm multiplies, it does not add over a sum),
so the wall's side-A mechanism (the additive tower sum) does not apply to them.
The boundary of C is the additive/multiplicative line, and the multiplicative
side is the F1 door.
```

## The squeeze, corrected (honest status)

```text
doc 03 hoped: rigidity S1 (canonical) + fundamentality (no additive route) =>
impossible, IF "canonical" forces "additive". THAT IMPLICATION IS FALSE, and this
cycle corrects it:

  "canonical" (forced, no moduli, no noncanonical choice) properly CONTAINS
  "additive" -- the canonical MULTIPLICATIVE structures (the norm, the Frobenius,
  the delta-structure) are equally canonical (they are forced, choice-free) yet
  NON-additive.

Therefore the squeeze does NOT close. The door is not shut by rigidity; it is
PRECISELY LOCATED: the only escape is a canonical MULTIPLICATIVE (norm / Frobenius
/ delta) integer intersection structure -- at the archimedean place. That is F1,
and it is exactly the program's original target (a global/archimedean Frobenius).
```

This is the wall and its door as dual faces, made precise:

```text
WALL  (proved, modulo EM bookkeeping + side B): no ADDITIVE/localizing integer
      dimension over bar(Spec Z) gives a finite integer self-product intersection
      form. [The bounded-negative theorem, class = C.]
DOOR  (open, = F1): a canonical MULTIPLICATIVE (Frobenius/norm/delta) integer
      structure at infinity would escape -- because the wall's side-A mechanism is
      the additive tower sum, which multiplicative structures do not feed.
```

## Consequence for the theorem's scope

```text
The fundamentality theorem is exactly bounded by C = additive/localizing. Its
honest scope line: "no ADDITIVE route works; a construction must be canonical
NON-additive = multiplicative = a Frobenius/norm/delta at the archimedean place."
This is NOT a weakness to hide -- it is the theorem POINTING AT its own exception,
which is the missing object. The theorem closes the additive correspondence
program AND hands the construction program its exact target.
```

## Atlas update (this cycle)

```text
F4 (class boundary): RESOLVED to "additive/localizing line"; the maximal C is the
   integer-valued localizing invariants; the boundary IS the door (F1).
F1 (the door): SHARPENED. The escape is not vaguely "non-additive" but precisely
   "canonical MULTIPLICATIVE (norm/Frobenius/delta), archimedean". The squeeze does
   not shut it; it isolates it. Candidates unchanged (delta-rings, Borger Lambda,
   Tambara/norm) -- each still needing the archimedean instance (F5).
```

## Scope / convergence

```text
Scope: characterization of the theorem's class, not RH. The correction (canonical
does NOT force additive) is a HONESTY repair on doc 03, banked.
Convergence: the additive/multiplicative line = the carrier wall's "multiplicativity
as structure" (CHARTER sec 5) = the F1 door = the missing Frobenius. The class
boundary, the carrier wall, and the construction target are one line, approached
from three sides. Sixth convergence; the wall and its door are now a single,
precisely located object.
```

## Next

Phase-1 checkpoint is now reachable: W1 closed (doc 06), C pinned (this doc). The
theorem is assembled within C (modulo routine EM write-up). The remaining live
question is entirely on the far side: F1 -- does a canonical multiplicative
(Frobenius/delta/norm) integer structure exist at the archimedean place? That is
the door, and the next atlas cycles map it (e.g. the archimedean delta-structure;
F5's exact deficit of infinity vs a finite place). Bring the assembled theorem +
this checkpoint for review before Phase 2 drafting.
