# 01 — CC is Frobenius-free and square-free by design; the RH-grade primitive is the integer intersection form

Status: NO-GO with named mechanism, 2026-06-29. Cycle 0 deliverable, answering
00-entry-preregistration.md sections A (GROUND) and B (PROBE). Deliverable type:
no-go (DISCIPLINE sec 1b). It carries a positive CC inventory (the foundation)
and a reposed, non-circular R1 as its forward value.

Named mechanism: **Frobenius-free Riemann–Roch.** Connes–Consani reproduce the
RR / Serre-duality *formalism* over bar(Spec Z) using Pontryagin duality and the
scaling/adelic structure as a SURROGATE for the geometric Frobenius, and route
their "Jacobian" to the adele class space (a rank-1 generalized Picard group),
NOT to a self-product. The RH-grade primitive — an integer-valued intersection
form on a self-product, equivalently a Frobenius graph with purity — is exactly
the residue this design leaves out, and it is RH-equivalent.

## A. GROUND (what CC supplies — the foundation; grade: Reading + Certified)

```text
G1  RR (arXiv:2205.01391, "Riemann–Roch for bar(Spec Z)", rev. 2023-03-08):
    an INTEGER-valued Euler characteristic for Arakelov divisors on the
    compactified Spec Z, chi(D) = deg(D) + (modification by log 2), via three
    concepts that extend the function-field originals: cohomologies H^0/H^1,
    an INTEGER DIMENSION (a tolerance/ceiling quantization of the real
    h^0_Arakelov of van der Geer–Schoof), and Serre duality. Built on a
    universal arithmetic theory over the SPHERE SPECTRUM (Segal Gamma-rings).
    [Reading; the integer-dim transcription is Certified in
     prime_int_genus_audit, lead-reran this cycle, exit 0.]
G2  THE "FROBENIUS": there is NONE. The proof PARALLELS WEIL'S ADELIC PROOF of
    RR for function fields, with PONTRYAGIN DUALITY playing the structural role
    that the geometric Frobenius / coherent duality plays over F_q. The scaling
    action R_+^* (the arithmetic/scaling site flow) is the only Frobenius-like
    datum, and its purity (spectrum on the critical line) is NOT a theorem.
G3  SERRE/PONTRYAGIN DUALITY: real, at curve level, the dualizing structure of
    G1. This is the FE-layer (BB.1): RH-NEUTRAL.
G4  JACOBIAN (arXiv:2602.15941, Connes–Consani 2026): the "Jacobian of Spec Z"
    is the ADELE CLASS SPACE read as a generalization of the Picard group --
    torsion-free RANK-1 abelian groups L with rigidifying data (norms in the
    Riemann sector; morphisms to R + root-of-unity data adelically), a MONOID
    SPACE; tensor product of rank-1 groups = product of adeles; spectral
    realization of L-functions. EXPLICITLY no square, no intersection form, no
    Frobenius graph, no theta divisor in the classical sense. [Reading,
    abstract-verified.]
```

## B. PROBE — the product joint (verdict: kill, with the primitive named)

The pre-registration asked: does curve-level RR/duality supply a genuine
off-diagonal correspondence datum on a self-product? The grounding answers NO,
and now says WHY at the design level (sharper than the prior arc's promotion
no-go, research/proof/187):

```text
P1  CC route AROUND the square. Their "Jacobian" is rank-1 (a generalized Pic /
    adele class space), reached by Pontryagin duality, NOT a 2-dimensional
    C x C. The tensor product of rank-1 L's gives the product of ADELES, not a
    correspondence algebra on a surface. There is no H^2, no intersection form,
    no Frobenius graph in the package -- not as an oversight but because the
    method (duality-as-Frobenius-surrogate) never needs them.
P2  WHY it is still a theorem over Z: the FE-layer (RR, Serre duality, the
    L-function's functional equation) is RH-NEUTRAL (BB.1). A surrogate that
    reproduces only the FE-layer can exist over Z precisely because it carries
    no RH-grade content. CC's RR being Frobenius-free is the constructive proof
    of BB.1's guard from the other side.
P3  THE PRIMITIVE, named exactly: the missing RH-grade datum is an INTEGER-
    VALUED intersection form on a self-product carrying the scaling flow as a
    correspondence (= a Frobenius graph with purity = the positive Rosati).
    Its POSITIVITY is RH; its mere EXISTENCE as an integer form is the
    "discreteness" the prior arc isolated as "the entire cost" (research/proof/
    16-17: doubling is cheap, the integer intersection form is the whole gap).
```

## Carrier guard (DISCIPLINE sec 4) — PASS

```text
DH death: a Frobenius-free FE-layer surrogate is exactly what DH/Epstein CAN
  also carry (Epstein has the functional equation, no Euler product). So the
  CC FE-layer alone is carrier-blind -- which is consistent: it is FE-layer, it
  SHOULD die on the controls. The RH-grade primitive (P3) is what must die on
  DH by NON-EXISTENCE of the carrier. Epstein dies at multiplicativity / unique
  factorization (research/proof/187 death point: chain multisets {6,6} != {4,9}).
This is the correct signature: the foundation is shared with the controls; the
primitive is not. No false carrier was claimed.
```

## DOF ledger (G-INT6) — this cycle makes 0 constructions, 0 choices

A pure GROUND + kill; no sub-object built, so no calibration risk. The reposed
R1 (below) is stated as a constraint count to be met by a future build, not met
here.

## Freeze (DISCIPLINE sec 6) — honored

No zero-side data touched. Entirely structural/literature. The scaling flow's
purity (= zero locations) is named as the missing datum, never imported.

## Scope (DISCIPLINE sec 9)

CC's RR/duality/Jacobian are LAYER I (FE-layer), logged as stage, NOT promoted.
The kill bounds the ROUTE "build-on-CC dissolves the construction," not RH:
even a full impossibility here would not touch RH (existence => RH, not iff).

## Convergence check (DISCIPLINE sec 7) — FIRES cleanly

```text
The product-joint break in CC's curve-level venue = the missing integer
intersection form / Frobenius purity = the CARRIER WALL. This is the SAME wall
found ANALYTICALLY (research/proof/132-136: the radius is irreducibly global;
positivity is RH-equivalent) and HOMOTOPICALLY (138-340: no machine supplies
the square H^2 / Frobenius graph / Rosati). THREE venues, ONE wall.

Two signals:
  (+) The wall is venue-INDEPENDENT -- strong evidence it is real, not an
      artifact of any one formalism. Good for the eventual impossibility
      direction; sobering for the construction direction.
  (+) The venue change SHED the p-local artifact: the Z/2 Weyl-shear obstruction
      (c=(1+z)^{-1}) does NOT appear in CC's global framework -- confirming the
      CHARTER's diagnosis that it was an artifact of the p-local venue, not the
      real obstruction. The reframe kept the wall and dropped the artifact.
```

## The honest cycle-0 finding

Building ON CC is the RIGHT foundation (it is the only tested global+archimedean
object with a real curve-level RR/duality theorem) but is NOT, by itself, a way
to construct the Frobenius/square: CC's method deliberately routes around BOTH
(Pontryagin duality as Frobenius-surrogate; adele class space as rank-1 Jacobian
in place of C x C). The global venue inherits the FE-layer for free and still
faces the identical RH-grade wall. Necessary, not sufficient -- recorded fail-
closed.

## Reposed R1 (the forward value — a NON-circular, concrete target)

The prior arc tried to PROMOTE CC objects to the square and was killed
(research/proof/187). Cycle 0 repose instead, with a real handle:

```text
R1 (post-cycle-0): CC already have an INTEGER-DIMENSION theory at curve level
   (the tolerance/ceiling quantization of h^0, G1). The non-circular question is:

   does CC's integer-dimension theory admit a KUNNETH / self-product extension
   yielding an INTEGER-valued intersection form on a self-product?

   - This is worker N's M5 (Kunneth for dim_S) + M2 (2-dim adelic theory), but
     now anchored to a SPECIFIC existing integer-dimension construction, not a
     wish.
   - It is NON-CIRCULAR: the EXISTENCE of an integer intersection form is the
     "discreteness" cost (not its positivity, which would be RH). CC supply
     integer dimensions; the question is whether they multiply.
   - It is CHECKABLE: study the ceiling/tolerance quantization in 2205.01391 and
     test whether it is monoidal / admits a Kunneth map. A definite mathematical
     question, not a naming exercise.
   - FAIL-CLOSED: if CC's integer dimension provably does NOT admit a product
     extension (e.g. ceiling is not additive under tensor -- the quantization
     defect D_b(s) pole, research/proof/Q-worker / doc 376), that is a named
     no-go that kills the "extend CC's integer-dim" route and forces the
     condensed/liquid integer-dimension route (CHARTER route 3).
```

## Witness

```text
Certified (reused, lead-reran this cycle, exit 0):
  python3 -m scripts.numerics.witness.prime_int_genus_audit   [ALL PASS]
  -- certifies the CC curve-level integer RR / genus transcription (G1) and the
     O_K control (zeta_K tracking), i.e. that the FOUNDATION reproduces.
Reading (this doc): G2/G4 and the P1-P3 mechanism are literature-grounded
  (arXiv:2205.01391, 2602.15941, abstract-verified); no new numeric claim is
  made, so no new witness is owed. The R1 probe (Kunneth on CC integer-dim) is
  the first OWED witness of the next cycle.
```

## Next

Cycle 1: execute the reposed R1 — read CC's integer-dimension construction
(2205.01391 sec on integer dim / cohomology) and test Kunneth/monoidality of the
ceiling quantization. Deliverable: a sub-object (an integer intersection form on
a self-product) OR a named no-go (the quantization does not multiply). Then
convergence-check against the prior arc's quantization-defect pole (doc 376 /
Q-worker), which already suggests the kill -- so pre-register both outcomes.
