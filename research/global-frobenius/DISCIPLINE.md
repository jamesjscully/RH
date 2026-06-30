# DISCIPLINE — the procedural envelope

Status: standing, 2026-06-29. The operating rules for this arc. Designed from
the post-mortem of the prior program: KEEP what produced its one real result,
STRUCTURALLY PREVENT its two failure modes. Binding on every cycle.

## 0. The two-regime lesson (why these rules exist)

The prior arc had two regimes:

```text
REGIME 1 (genuine, ~docs 138-340): each doc took a NAMED machine from the
  modern toolkit (DMP support, Hecke/Iwahori, geometric Satake, Hitchin
  systems, prismatic/syntomic, Fargues–Fontaine, CC Jacobian, II_1 trace,
  Tannakian compactness, ...) and proved it cannot supply the object, with a
  SPECIFIC mechanism. This produced the real result: a stable three-wall
  fingerprint, and a convergence with the analytic frontier. KEEP this.

REGIME 2 (regress, ~docs 360-540): tried to PIN the object by a universal
  property, then slid into a coherence-cell-per-doc tower -- ~150 docs in a
  day, each a "construction-spec refinement anchor" (not a no-go, not a
  witness), the name growing one token per doc, the finite index frozen at 24
  cells while naming choices grew unbounded. A degrees-of-freedom violation.
  STRUCTURALLY PREVENT this.
```

## 1. THE DELIVERABLE RULE (binding)

Every document is EXACTLY ONE of:

```text
(a) VERIFIED SUB-OBJECT -- an exit-gated, deterministic, lead-reran witness
    that BUILDS a named piece of the target; or
(b) NO-GO with a NAMED MECHANISM -- a kill of a SPECIFIC named construction
    (a real mathematical object/machine) for a SPECIFIC reason.
```

There is no third category. BANNED document types (the regime-2 bloat):
construction-spec / refinement anchor / contract spec / coherence cell /
status board / router / admission matrix / dispatch packet / rubric /
expert packet. A schema with no witness is not a document.

## 2. ANTI-REGRESS (mechanically enforced)

```text
NAME MONOTONICITY (hard): a new doc's slug token-count MUST NOT exceed its
  predecessor's. A needed new qualifier is a STOP signal -> run a witness or
  prove the impossibility. Slugs use a FIXED vocabulary of descriptive nouns
  naming REAL mathematical objects ("hitchin-system", "geometric-satake",
  "product-joint"), NEVER process-scaffolding tokens ("mediator", "coherence",
  "contract", "basin", "fixedpoint", "terminal", "probe"). Guard regex bans
  the old uppercase chain AND lowercase qualifier-accretion.

ONE-PRIMITIVE TARGET: the unit of work targets the GLOBAL FROBENIUS (the hard
  primitive). Never carry the monolith (square + Rosati) as the unit. The
  square, the duality, the positivity are DERIVED theorems.

NO MANUFACTURING A FORCED OBJECT BY CHOICE: the success spec is rigid +
  contractible (CHARTER S1). Any construction that requires a NONCANONICAL
  choice (insert a unit / project to a copy / quotient to a line / select an
  idempotent / adjoin a generator) is a category error and is auto-rejected.
  This single rule retro-kills ~400 prior docs; apply it BEFORE running.

CYCLE != DOC: a cycle ships a THEOREM-GRADE deliverable, at most a handful of
  docs. If doc-count outruns theorem-count, STOP -- that is the regress
  signature. Volume is not progress.
```

## 3. WITNESS PROTOCOL (kept — this worked)

```text
- Certified, not floating: every numeric claim is a python-flint ball
  enclosure; every structural claim is exact linear algebra.
- Exit-gated, deterministic, lead-reran by the lead at landing (rerun the
  witness yourself before committing).
- Pre-registration BEFORE computation; refuted registrations are recorded in
  place, never relocated or quietly edited.
- Witnesses live in scripts/numerics/witness/ and run via
    python3 -m scripts.numerics.witness.<name>
  exit 0 = the recorded claim reproduces.
```

## 4. CARRIER GUARDS (kept — now the PRIMARY guard)

```text
The carrier wall is primary (CHARTER sec 5). Every construction must DIE on:
  - DH (Dirichlet/Hadamard control): no Euler product. If DH can also
    instantiate it, it is carrier-blind -> REJECT.
  - Epstein: at multiplicativity / effectivity / address -- exhibit the EXACT
    death point.
First guard question every cycle: "does this make the Euler product STRUCTURAL,
or does a control already have it?"
```

## 5. DOF LEDGER (G-INT6, kept)

```text
Every constructed sub-object must match MORE constraints than it makes free
choices, or it is CALIBRATION, not construction. (This is the exact test the
regime-2 coherence tower failed: 24 fixed constraints, unbounded naming.)
Log #constraints vs #choices in every build doc.
```

## 6. FREEZE (kept)

```text
No zero-side data builds any sub-object. Zero loci are computed and HASHED
before any zeta/zero data is imported; comparison only. (Prevents the
object from secretly reading the answer it is supposed to derive.)
```

## 7. CONVERGENCE CHECK (the real-win practice, promoted to standing)

```text
The prior program's genuine discovery came from TWO independent attacks
(top-down analytic + bottom-up constructive) landing on the SAME named wall.
Convergence is the signal that a wall is REAL; fraying is the signal the target
or the venue is wrong. Every few cycles, run an explicit convergence check:
are independent routes hitting the same named obstruction? Record it.
```

## 8. CLAIMS GRADING (kept)

```text
Every claim is graded: Theorem / Certified / Census / Reading.
  Theorem   = unconditional proof.
  Certified = exit-gated witness (python-flint ball / exact linear algebra).
  Census    = exhaustive finite check over a stated range.
  Reading   = heuristic / informal -- explicitly not load-bearing.
```

## 9. SCOPE HONESTY (binding)

```text
- existence(object) => RH. ¬existence does NOT => ¬RH. Negative results bound
  the ROUTE, never RH (CHARTER sec 1).
- No "unknowable" branch: RH is Pi_1; independence of a sound theory => true.
- STAGE-vs-PLAY (BB.1): Layer-I results are FE-layer, RH-NEUTRAL; never
  promoted to RH progress.
- Honest grade on relocations: a "no analytic/constructive route supplies X"
  result is a relocation/characterization at witness rigor, NOT an
  unconditional impossibility theorem, unless proven as one.
```

## 10. The operating loop

```text
GROUND -> PRE-REGISTER -> PROBE (build or kill) -> VERIFY (guards 4,5,6 +
rigidity spec S1-S6) -> SYNTHESIZE (one deliverable) -> CONVERGENCE CHECK
(periodic). Commit atomically; the lead reruns every witness at landing.
```
