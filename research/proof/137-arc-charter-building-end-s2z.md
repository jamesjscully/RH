# 137 - Arc charter: building End(S^2/Z)

Status: ARC CHARTER, 2026-06-17. Opens the construction arc that doc 136
named as the program's sole remaining target. This is a charter, not a
cycle: it fixes what must be built, the banked state to build ON, the
risk-ladder, the guards, and the entry point -- BEFORE any construction
cycle runs. Analogous to the doc-32 / doc-38 charters of earlier arcs.

## 1. Honest framing (read first)

The target is the F_1 / Connes-Deninger object. This is a famous,
decades-open problem; the arc is a LONG one and most likely does not
finish. The charter's job is to make it FAIL-CLOSED and regress-proof so
that the arc produces banked value either way:

```text
- Every cycle ships a VERIFIED sub-object (an exit-gated homotopy / index /
  duality computation that builds a named piece) OR a no-go with a named
  mechanism. Nothing else is progress (doc 129).
- The arc must NOT become a construction-naming regress (doc 129 / STRATEGY
  sec 6). If a target name starts growing by qualifier accretion, or a
  "shot" produces no witness and no impossibility, STOP (Cor 129.2).
- BB.1 STAGE-vs-PLAY GUARD: building the symmetry/supply object does NOT
  prove RH (it is FE-layer, RH-neutral). The RH-grade target is the
  POSITIVITY (sec 2 layer II), gated behind the stage. Do not claim RH
  progress from stage results (doc 31 sec 2, doc 21 sec 4).
```

## 2. The target, precisely (two layers)

```text
OBJECT: End(S^2/Z) -- the self-product correspondence algebra on the
  compactified arithmetic line, with a positive Rosati involution
  F^dag = (deg) F^{-1}, whose self-norm <F,F> = deg(F) is the sum over
  zeros (doc 136; frobenius_self_norm). It exists over F_q (F = Frobenius)
  and is absent over Z; building it over Z is the whole problem.

LAYER I -- THE STAGE (the free / DH-shared / symmetry half).
  The compactified object Xbar and its self-duality: the correspondence
  algebra End(Xbar) with the FE/edge/modulus structure. This is the
  supply/symmetry layer of completed zeta. Mostly built (sec 3). Finishing
  it yields "the stage, not the play" (doc 31 sec 2) -- necessary, not
  sufficient.

LAYER II -- THE PLAY (the RH half).
  The POSITIVE Rosati involution on End(Xbar): F^dag = (deg) F^{-1} with
  F^dag = F* (positive-definite), equivalently the Hodge-index / Weil
  positivity on the square. Its positivity <=> RH (doc 136 invariant
  136.1; off_diagonal: PSD on zeros, indefinite off-line). doc 136 proved
  NO analytic route supplies this; it must come from the constructed
  arithmetic correspondence. This is the RH-grade target.
```

## 3. Banked construction state (what is already built -- build ON this)

The program's PFD/Xbar line (docs 28-31, workers Y..GG) already built much
of Layer I. Do not restart it; continue it.

```text
DONE  Thm S.1 (doc 25): THR(F_2)^{tC_2} closed form, pi_* = F_2[[z]][t^+-1]
      -- the 2-primary foundation Xbar's homotopy rests on.
DONE  Xbar EXISTS (doc 30, DD): Xbar = fib(X x X' -> Y), pi_* Xbar = G
      EXACTLY, conditional on S.1 (done) and DD.4 (partial). The
      compactified local object is realized as a spectrum.
DONE  DD.4 Lin clause (doc 31, Thm EE.1): on the Lin block the duality
      datum is the UNIQUE nonzero map (singleton, torsor-free), inducing
      Z's K2 pairing; display Xbar ~ Sigma I^cont(Xbar).
DONE  KMS-1/2 forced at p = 2,3,5 (docs 29,30); pole cancellation global
      and load-bearing; the renormalized survivor = the EF prime-side shell.
OPEN  (A) DD.4 on weights >= 1 (doc 31 exit A): the branch-exchange clause +
      genuine O(2) structure + N1-b' + the weight-torsor. Homotopy-theoretic,
      sharply posed, one clause already a theorem.
OPEN  (B) the archimedean unit (doc 31 exit B): triply specified -- couple
      comb to continuum (read kappa), one continuum unit per place (global
      existence), a rational/Anderson layer (what torsion lacks). A
      construction project; homes TR/TC (I_Q slot), condensed/liquid, or a
      structural Witt iota.
OPEN  the six missing CC-square ingredients (worker N): M1 strict-collapse,
      M2 2-dim adelic theory, M3 pi_2/Dold-Kan length-2, M4 monoidal
      tolerant modules, M5 Kunneth for dim_S, M6 a single base with both RR
      and duality. (M1 partially resolved; the grading is the bridge, doc 26.)
OPEN  LAYER II entirely -- the positive Rosati involution / the Hodge-index
      positivity (gated behind A, B).
```

## 4. The risk-ladder (order of work = kills-the-arc x cheapness)

```text
R0  FOUNDATION (done): S.1 computed (doc 25); Xbar realized (doc 30). The
    arc has a non-empty starting object -- not a fantasy.

R1  DD.4 weights >= 1 (exit A) -- THE ENTRY POINT (sec 8). Cheapest sharp
    next step: one clause (Lin, EE.1) is already a theorem; the branch-
    exchange / O(2) / weight-torsor clauses are homotopy-theoretic and
    exit-gateable by a pi_*-level witness. Highest priority: it finishes
    the self-duality of Layer I and is the prerequisite for End(Xbar).

R2  the archimedean unit (exit B). Harder, multi-route; gated partly on R1.
    Fail-closed sub-targets: (B1) couple comb-continuum in one object
    (read kappa); (B2) one continuum unit per place from structure, not
    inserted (zero-slack guard, LL/NN); (B3) the rational/Anderson I_Q
    layer. Each route (TR/TC, condensed, Witt iota) gets a deletion test.

R3  LAYER II -- the positive Rosati involution F^dag = (deg) F^{-1} on
    End(Xbar) (the RH-grade target). Gated behind R1+R2 (the algebra must
    exist before its involution). doc 136: no analytic route; it must come
    from the constructed correspondence. The deepest rung; the play.

Do R1 before R2 before R3. Each rung is fail-closed: a negative reshapes
the target and is banked (a no-go), not hidden.
```

## 5. Guards (standing, every cycle)

```text
- Carrier guards: the constructed object must DIE on DH (no carrier) and on
  Epstein (dies at multiplicativity/effectivity/address; use doc 64). A
  construction that Epstein/DH can also instantiate is the wrong object.
- BB.1 stage-vs-play: stage results are FE-layer; do not claim RH progress
  from them (sec 1).
- No unit insertion (zero-slack theorem, LL/NN): the archimedean unit (R2)
  must be DERIVED, never hand-set; any insertion demotes the result.
- G-INT6 DOF ledger: every constructed sub-object matches more constraints
  than free choices, or it is calibration.
- FREEZE (doc 59): no zero-side data builds any sub-object; comparison only,
  loci hashed before import.
- Witnesses: homotopy/index/duality computations, exit-gated, deterministic,
  lead-reran at landing (the prime_int_* / prime_cc_* fleet is the model).
```

## 6. Candidate construction routes (ordered)

```text
ROUTE 1 (in-house, most developed): the PFD/Xbar spectral line (docs 28-31).
  Finish A (DD.4 weights>=1), then B (the unit), then End(Xbar)'s Rosati.
  Strength: realized object, banked machinery. This is the default route.

ROUTE 2 (most-proven external): the Connes-Consani scaling site / C x C.
  CC PROVED integer RR + Pontryagin-Serre duality for compactified Spec Z
  (arXiv:2205.01391, 2306.00456) and built Pic infrastructure (2026
  Jacobian paper). Test: does the curve-level theorem EXTEND to the
  self-product correspondence End(C x C) with a positive Rosati? Strength:
  the curve-level object is a THEOREM; weakness: CC departs from the FF
  analogy at the square joint (doc 21/22) -- the self-product is the gap.

ROUTE 3 (STRATEGY sec 3 metric enrichment): condensed / liquid + Lawvere
  cost. "Metric replaces topology": the Rosati positivity as a graded /
  pro-etale-to-condensed enrichment carrying the slack. Strength: aligns
  with the located liquid address (doc 42); weakness: least concrete.

The arc may interleave routes; R1 is route-agnostic (DD.4 is in-house).
```

## 7. The anti-regress contract (the doc-129 lesson, binding for this arc)

```text
Because this arc IS a construction arc -- the exact shape that went off the
rails before -- it is bound to the strictest reading of doc 129:
  1. A cycle's deliverable is a VERIFIED sub-object (exit-gated witness) or
     a no-go with a mechanism. A schema with no witness is not a document.
  2. No qualifier-accretion: target names do not grow segment by segment. A
     needed new qualifier is a STOP signal -> run a witness or prove the
     impossibility (Cor 129.2). The guard's regress-signature check applies.
  3. Stage results are logged as stage (FE-layer), never promoted (BB.1).
```

## 8. Entry point + first cycle

```text
ENTRY = R1: DD.4 on weights >= 1 (exit A), building on EE.1.
First cycle (to be run, ultracode-scale, when authorized):
  - GROUND: the exact state of DD.4 (EE.1 Lin clause proven; what the
    branch-exchange / O(2) / N1-b' / weight-torsor clauses require at
    pi_*-level), from docs 28-31 + workers EE/FF/GG + Thm S.1.
  - PROBE: construct/compute the weight->=1 duality datum (the homotopy
    computation), exit-gated; OR prove a no-go (the duality cannot extend
    past the Lin block with a named obstruction).
  - VERIFY: carrier guards (DH/Epstein death); G-INT6; freeze; that the
    datum is genuine duality not gauge/decoration.
  - SYNTHESIZE: doc 138 = DD.4-weights>=1 result (a built sub-object or a
    no-go), and the updated arc board.

This charter is the arc's standing reference; doc 138+ are its cycles.
```
