# 05 — PIVOT CHARTER: prove the dichotomy fundamental; map its far side

Status: PIVOT CHARTER, 2026-06-29. Re-orients the global-frobenius arc after
doc 04 closed the decisive weak link W2 (no leak). User-committed:
"commit to the dichotomy, with discipline, and in a way that if the program
stalls we keep building a high-resolution picture of the other side of the wall."
This charter fixes the new primary goal, the dual deliverable that makes a stall
productive, the phased plan with checkpoints, and the anti-trap discipline. Reads
on top of CHARTER.md + DISCIPLINE.md (all standing discipline kept).

## 1. The decision (committed)

```text
PRIMARY GOAL (new): prove the integrality-summability dichotomy FUNDAMENTAL --
  "no additive/localizing integer dimension theory over bar(Spec Z) yields a
   finite integer intersection form on the self-product; finiteness forces the
   transcendental -zeta'(0), integrality forces divergence" -- the CHARTER's
   bounded-negative branch.

STANDING DUAL PRODUCT (the discipline that survives a stall): the FAR-SIDE
  ATLAS (ATLAS.md) -- a high-resolution map of what lies beyond the wall. Every
  cycle advances THE THEOREM or THE ATLAS; neither is optional, both are
  first-class, no cycle is wasted.
```

## 2. Why the pivot is coherent (the unifying insight)

```text
The wall's ONLY door is the program's ORIGINAL target. The single escape from
the dichotomy -- a canonical-but-non-additive integer intersection form -- is a
canonical MULTIPLICATIVE structure (non-additive = multiplicative: a Frobenius /
norm / delta-structure). That is exactly the carrier wall's missing ingredient
("multiplicativity must be STRUCTURE, not property", CHARTER sec 5) and exactly
the global/archimedean Frobenius the arc set out to build (CHARTER sec 2).

=> Proving the wall fundamental and characterizing the missing object are the
   SAME activity, seen from opposite sides. The far-side atlas IS the object's
   fingerprint, read from its negative space. A stall on the theorem still
   sharpens the fingerprint. The pivot does not abandon construction; it
   pursues it by triangulation, with a rigorous impossibility floor.
```

## 3. The dual deliverable rule (binding)

```text
Every cycle ships EXACTLY ONE of:
  (T) a THEOREM step -- a lemma / certified witness / no-go advancing the
      bounded-negative result (e.g. W1, widening the class C, killing an
      apparent leak); OR
  (M) an ATLAS step -- a higher-resolution characterization of one of the five
      far-side faces (sec 5), with a named sharpening and, where possible, a
      witness.
Both obey DISCIPLINE.md (witness-or-named-mechanism, carrier guards, DOF,
freeze, claims grading, name monotonicity, no scaffolding tokens, cycle != doc).
A cycle that produces neither a T-step nor an M-step is a stall to REPORT, not a
doc to pad.
```

## 4. Phased plan + checkpoints (the bounded commitment)

```text
PHASE 1 (committed now, bounded): close W1 + pin the class C.
  W1: the general-staircase sawtooth-regularity lemma (Mellin; the combinatorial
      core -- geometric jump density 1/log b -- is Census-certified,
      gf_dichotomy_jump_density). LOW risk.
  C : pin the maximal additive/localizing class for which side A holds; locate
      the first escaping structure (= the additive/non-additive line = Face 4).
  HARD CHECKPOINT at end of Phase 1:
    -> trends to A (theorem reachable): proceed to Phase 2.
    -> reveals a LEAK / B (a non-additive structure breaks the dichotomy): SWING
       POSITIVE -- that structure is the construction handle; open a build cycle.
    -> trends to D (the proof needs an RH-input = collapses to RH-equivalence):
       STOP the theorem-push, bank the certified wall as-is, go FULL ATLAS.

PHASE 2 (only if Phase 1 -> A): draft + harden the fundamentality theorem;
  widen C to the broadest defensible class; write the scope statement.

STANDING (all phases): the atlas refines every cycle regardless of phase.
```

## 5. "The other side of the wall" — the five faces (what the atlas maps)

The far side is ONE missing object (a canonical multiplicative/Frobenius
structure at infinity) seen five ways. Details + current resolution live in
ATLAS.md; the faces are:

```text
F1  THE NON-ADDITIVE DOOR: the only escape = a canonical non-additive
    (= multiplicative) form. Candidates: delta-rings / Frobenius lifts, Borger
    Lambda-rings, Tambara/norm functors -- each needing an ARCHIMEDEAN instance.
F2  THE TRANSCENDENTALITY BOUNDARY: finite => the value is -zeta'(0)/log b =
    (log 2pi)/(2 log b) = the archimedean Gamma-factor datum. What period ring
    is it; what arithmetic content survives non-integrality?
F3  THE PROPERNESS BOUNDARY: the wall = no truncation of the tower over S.
    What "properness over S/Z" (Poisson-as-theorem) would truncate it?
F4  THE CLASS BOUNDARY: the exact maximal C; the first structure outside it
    (= the additive/non-additive line = the Frobenius line).
F5  THE MISSING PLACE: the dichotomy is "the arithmetic of one missing place".
    What must infinity supply to behave like a finite place p (residue q,
    q-power Frobenius, weight-1 local numerator)?
```

## 6. Anti-trap discipline (the Outcome-D guard) + scope honesty

```text
ANTI-TRAP (avoid circling to RH-equivalence): if any T-step needs a positivity
  / zero-location input that turns out to BE RH, FLAG it and REASSIGN the cycle
  to an M-step (atlas). Do not push a circular proof. Convergence-check every
  cycle: is the wall still venue-independent, or did we circle to RH-equivalence?
  (The prior program's known trap: STRATEGY "do not prove more RH-equivalences".)

SCOPE (binding, restated): existence(object) => RH, but ¬existence does NOT
  => ¬RH. The negative theorem bounds the ROUTE (the additive/canonical
  correspondence program), NEVER RH. No "unknowable" branch (RH is Pi_1). The
  theorem is RELATIVE to C; outside C it is silent (that silence is F4/F1).
  Grade everything: Theorem / Certified / Census / Reading.
```

## 7. What success looks like (so we know when we have it)

```text
- THEOREM landed (A): the bounded-negative result, with C as wide as provable
  and an honest scope note. Closes the additive correspondence route + explains
  why (the missing place). A real, publishable, RH-NEUTRAL contribution.
- DOOR found (B): a canonical non-additive structure that breaks the dichotomy
  => the missing object => swing to construction (=> RH if it closes).
- ATLAS at high resolution (C/D fallback): the sharpest-ever fingerprint of the
  missing object, each of F1-F5 pinned to a named open question with certified
  anchors. The durable product a future breakthrough builds on.
All three are bankable; only a silent stall is failure, and the dual rule
forecloses it.
```

## Next

Open Phase 1: cycle on W1 (T-step) and seed/refine the atlas (M-step). The
atlas is seeded now (ATLAS.md) from docs 01-04 + the prior arc, so the far-side
picture starts at real resolution, not blank.
