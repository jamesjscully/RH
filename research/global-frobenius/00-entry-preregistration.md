# 00 — entry pre-registration: ground CC curve-level, locate the product joint

Status: PRE-REGISTRATION, 2026-06-29. Cycle 0 of the global-frobenius arc.
This fixes what cycle 0 will GROUND and PROBE, and the acceptance conditions,
BEFORE any computation (DISCIPLINE sec 3). It is itself neither a sub-object nor
a no-go; it is the pre-registration that the cycle-0 deliverable answers.

## Purpose

Establish the foundation (R0) exactly and pose the entry probe (R1) sharply.
We do not yet build anything. We GROUND the external theorem we stand on and
LOCATE the precise point where it stops being a theorem — the self-product
joint — so the first real cycle has an exit-gated target.

## A. GROUND (to be filled by the cycle-0 deliverable)

The exact state of the Connes–Consani curve-level result, answered as Reading +
citations (grade per DISCIPLINE sec 8), with the precise statements pinned:

```text
G1  THE CATEGORY: in what category does CC's compactified Spec Z ("the curve")
    live? (scaling site / adele class space / topos of the arithmetic site).
    What plays the role of structure sheaf, of O(D), of H^0/H^1?
G2  THE "FROBENIUS"/SCALING DATA: what endomorphism or flow plays the role of
    Frobenius at curve level (the R_+^* scaling action)? What is its spectral
    data, and where does purity |eig| = N^{w/2} live or fail to live?
G3  THE DUALITY: the exact form of Pontryagin–Serre duality CC prove
    (arXiv:2306.00456) -- the pairing, the dualizing object, the degree/genus
    bookkeeping. Integer Riemann–Roch (arXiv:2205.01391): the exact RR formula.
G4  PIC / JACOBIAN: what the 2026 Jacobian paper supplies -- Pic^0, the
    Jacobian, any intersection or height pairing already present.
```

## B. PROBE (the entry question, R1) — to be answered as build-or-kill

```text
P1  Write the self-product joint precisely: what would C x C, its structure
    sheaf, and H^2 / the intersection form be, IN CC's category? Identify the
    EXACT ingredient that curve-level RR/duality does NOT supply when passed to
    the product (the prior arc's recurring missing list: square H^2 /
    intersection form, off-diagonal correspondences, Frobenius graph).
P2  Decide the cheapest sharp sub-target:
      (build)  exhibit ONE genuine off-diagonal correspondence datum on C x C
               that is NOT a pullback of curve-level data (a real square
               object), exit-gated; OR
      (kill)   prove a named no-go: the curve-level duality does NOT cross the
               product joint, with the exact obstruction and death point.
```

## C. ACCEPTANCE CONDITIONS (pre-committed)

The cycle-0 deliverable is accepted only if it is one of:

```text
- a VERIFIED SUB-OBJECT: an exit-gated witness exhibiting a genuine square /
  off-diagonal datum, passing the rigidity spec (CHARTER S1: canonical, no
  noncanonical choice) and the carrier guards (S6: dies on DH/Epstein); OR
- a NO-GO with a NAMED MECHANISM: the product joint cannot be crossed by
  curve-level data, with the exact missing ingredient named and the DH/Epstein
  death point exhibited.
```

Pre-committed guard checks on whatever is built or killed:

```text
- CARRIER (DISCIPLINE sec 4): does the construction die on DH (no Euler
  product) and Epstein (multiplicativity)? If a control instantiates it, REJECT.
- RIGIDITY (CHARTER S1): does it require a noncanonical choice? If yes, it is a
  category error -- REJECT, do not "repair" by another choice.
- DOF (DISCIPLINE sec 5): #constraints vs #choices logged.
- FREEZE (DISCIPLINE sec 6): no zero data touched; this cycle is pure structure.
- SCOPE (DISCIPLINE sec 9): any duality/RR result here is LAYER I (FE-layer,
  RH-neutral) -- logged as stage, never promoted.
```

## D. Anti-regress pre-commitment (binding)

```text
- Cycle 0 ships AT MOST 2 docs: this pre-registration + one deliverable.
- The deliverable's slug is a fixed-vocabulary descriptive name naming the real
  object (e.g. "01-cc-curve-ground" or "01-product-joint-no-go"); token-count
  <= this doc's slug. No scaffolding tokens (DISCIPLINE sec 2).
- If GROUND (A) cannot be pinned to a citable theorem, that is itself the
  cycle-0 finding (the foundation is softer than claimed) -- record it, do not
  paper over it with a constructed wrapper.
```

## Next

Run cycle 0: produce `01-*` answering A and B as a single build-or-kill
deliverable. Then convergence-check (DISCIPLINE sec 7): does the product-joint
obstruction, if any, match the prior arc's carrier wall? Convergence confirms
the venue change kept the real obstruction and shed the p-local artifact.
