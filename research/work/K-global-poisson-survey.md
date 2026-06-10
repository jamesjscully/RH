# K - The global Poisson landscape: candidate vessels for "Poisson summation as a theorem about ring spectra" (C5''' survey)

Status: survey-and-gate pass executed 2026-06-10 (fresh context). No derivations,
no new numerics; every claim below is sourced to a fetched primary document
(archived under research/proof/refs/) or marked UNVERIFIED. Reading frame
pre-registered before the search: each candidate is scored against doc 19
section 1's properness decomposition

```text
PF (finiteness/integrality)  PD (duality)  PR (Riemann-Roch)  PS (sections)
```

plus a CIRCULARITY AUDIT (no RH / zero-side input) and the CARRIER CHECK
(must die on DH/Epstein by NON-EXISTENCE of the carrier, per the program's
guard).

## 0. Structural finding first: the PD layer is carrier-blind

Before the candidate list, one fact that reorganizes it. Classical Poisson
summation holds for EVERY lattice in every dimension; the theta functional
equation that powers van der Geer-Schoof's Riemann-Roch is available verbatim
for the Epstein zeta of an arbitrary quadratic form - which has off-line
zeros (doc 17 section 4). Therefore:

```text
Any vessel that delivers ONLY the duality/functional-equation layer (PD)
is structurally carrier-blind: Epstein passes it. The discriminating
content of the missing properness theorem must sit in how PD is COUPLED
to the ring carrier through the count layers (PF + PS: sections as
ring-theoretic objects with integer cardinalities) - exactly doc 17's
Epstein boundary, reappearing at the properness level.
```

Consequence for ranking: candidates are valued by how much of PF/PS they
carry, not by the strength of their PD. This immediately demotes the
Braverman-Kazhdan/Ngo front (pure PD, see section 3) and promotes the two
vessels where the carrier is built in (Connes-Consani's S-module cohomology,
section 1; THH-side/condensed re-runs, section 4).

## 1. Candidate 1: Connes-Consani absolute Riemann-Roch - the direct hit

### 1.1 What is PROVEN (citation-grade)

(a) arXiv:2205.01391 "Riemann-Roch for Spec Z bar" (published version
ScienceDirect S0007449723000672; PDF archived:
connes-consani-2022-riemann-roch-specZbar.pdf). Theorem 1.1, quoted:

> Let D be an Arakelov divisor on Spec Z bar. Then
> dim_{S[+-1]} H^0(D) - dim_{S[+-1]} H^1(D) = ceil'( deg' D + log' 2 ) - 1_L.

(deg' = deg/log 3, base-3 logarithms; ceil' = odd ceiling; 1_L = indicator
of an explicit exceptional set of finite Lebesgue measure.) The three
ingredients are all CONSTRUCTED, not postulated: H^0(D) and H^1(D) are
S[+-1]-modules (Segal Gamma-spaces; H^1 = cokernel of the adelic map
psi: Q x O(D) -> A_Q as a tolerant S-module), and the dimension is the
MINIMAL NUMBER OF LINEAR GENERATORS with coefficients in {-1,0,1} - an
integer by definition. E.g. (their (1.3)) dim_{S[+-1]}(||HZ||_n) =
ceil(log(2n+1)/log 3).

Theorem 1.2 (Serre duality), quoted:

> Let D be an Arakelov divisor on Spec Z bar and K = -2{2}, with
> deg K = -2 log 2. Then there is an isomorphism of S[+-1]-modules
> H^0(K - D) ~ Hom_{Gamma T_*}(H^1(D), U(1)_{1/4}),
> where U(1)_{1/4} coincides with H^1(K), playing the role of the
> dualizing module in Pontryagin duality.

Their gloss: "the analogue of Grothendieck's version of Serre's duality";
the duality "derives from Pontryagin's duality holding for tolerant
S[+-1]-modules (Proposition 5.2)". Note the canonical divisor is
K = -2{2}: supported at the PRIME 2, degree -2 log 2.

(b) arXiv:2306.00456 "Riemann-Roch for the ring Z" (archived:
connes-consani-2023-riemann-roch-ring-Z.pdf). Working over the absolute
base S itself (their categorical sphere spectrum) instead of S[+-1].
Theorem 1.1, quoted:

> dim_S H^0(D) - dim_S H^1(D) = ceil'( deg_2 D ) + 1.

(base-2 logarithms now; ceil' a right-continuous odd ceiling.) Their listed
improvements: the exceptional set 1_L is eliminated; "Formula (1.1) displays
a perfect analogy with the Riemann-Roch formula holding for curves of
GENUS 0"; deg_2(K) = -2 is integral. Mechanism: Z = S[X] with
1 + 1 = X + X^2, X = -2 (over S[+-1] it was base 3: Z = the finite-support
F_3 Witt vectors). Sections: 1 intro, 2 base S, 3 dim H^0, 4 dim H^1,
5 RR formula - NO Serre-duality section in the 2023 paper; duality is
proven only in the 2022 S[+-1] version. UNVERIFIED whether a duality over
S (rather than S[+-1]) exists in print as of 2026-06.

(c) arXiv:2602.15941 "On the Jacobian of Spec Z bar" (Feb 2026; archived:
connes-consani-2026-jacobian-specZbar.pdf). Construction paper, not a
theorem-of-properness paper: interprets the adele class space of Q (the
space whose spectral realization carries the zeta zeros in Connes 1999) as
the monoidal extension of Pic(Spec Z bar); elements = torsion-free rank-1
abelian groups with rigidifying data (norm in the "Riemann sector" =
metrized line bundles; morphism to R + root-of-unity parametrization in
general); adele product = tensor product of these. No Riemann-Roch on a
square, no positivity statement, no h^1 of a surface. It is the Picard/
Jacobian INFRASTRUCTURE step. [CORRECTED 2026-06-10, worker N from the
2026 PDF: CC explicitly mark "a decisive departure from the classical
function field analogy" AT EXACTLY THIS JOINT - instead of Frobenius
acting on the Jacobian (the FF square step), they rely on the idele
class group acting by translations. They are NOT walking the FF path
toward the square; they fork to the trace-formula/spectral side at the
point where the program needs the intersection form. The original
"between steps 2 and 3" reading was wrong about their stated intent.]

### 1.2 Scoring

- STATUS: theorem (RR + Serre duality at curve level, integer-valued);
  program (everything square-level and zero-level).
- DELIVERY: the FULL properness package PF + PD + PR + PS - but for the
  CURVE Spec Z bar only. PF: dimensions are integers by construction (count
  of generators - note: log-scale of a section count, not the section count
  itself; this is the honest PS caveat). PD: proven (2022, over S[+-1]).
  PR: exact formula. PS: H^0(D) is an actual S-module of actual global
  sections (Z-valued divisors of bounded adelic norm). On the FF side, the
  zeros enter through RR on the SURFACE C x C applied to Frobenius-graph
  divisors; the curve-level package is the necessary substrate, zero-free
  by itself. CC's theorem is the exact existence proof that the program's
  missing object EXISTS AT CURVE LEVEL over the sphere-flavored base.
- CIRCULARITY AUDIT: CLEAN. The proof is combinatorial-adelic: dimension
  counts (sections 3-4 of each paper) + Pontryagin duality for tolerant
  S[+-1]-modules. Theta functions appear ONLY in the introduction, as the
  vdGS predecessor being improved upon ("the log-theta number as a
  dimension remains virtual... it outputs real numbers rather than
  integers"). No zeta zeros, no RH, no positivity input anywhere. The
  Poisson-summation content is carried by the same classical fact Weil's
  adelic FF proof uses: Q is discrete cocompact self-dual in A_Q.
- CARRIER CHECK: the construction consumes the ring Z (as S[X]) and its
  adele ring. DH: no ring, no adeles, no O(D) - carrier nonexistent, dies
  correctly. Epstein: at curve level the formalism is rank-1 (divisors);
  a rank-2 extension (Epstein = theta of a rank-2 lattice) is not in the
  papers, but the norm-on-abelian-group formalism would plausibly admit
  one - i.e. curve-level CC is carrier-blind in the same benign way
  classical RR for number fields is. The discriminating layer has to be
  the square (where DH/Epstein have no diagonal because they have no
  multiplication). UNVERIFIED: whether CC's formalism obstructs rank-2
  extensions.
- TRACTABILITY RANK: 1 (see section 6).

### 1.3 A sharp tension - the two genus probes disagree

CC over S: chi(D) = deg_2 D + 1, "perfect analogy with... curves of
GENUS 0" (their words) - the RR-constant probe says g(Spec Z bar / S) = 0,
i.e. P^1-like. Doc 18's diagonal probe on the derived square:
<Delta,Delta>_tors = zeta'(0) < 0, read as 2 - 2g, says g = 1 + (1/4)log 2pi
= 1.459 - hyperbolic. On an honest curve the two probes AGREE (chi(O) =
1 - g and Delta^2 = 2 - 2g are the same g). So either (i) the two
constructions see different compactifications/bases (CC's combinatorial S
vs the homotopy-theoretic sphere; CC's K = -2{2} is supported at p = 2,
while THH's cotangent tower is spread over all k), or (ii) "Spec Z over S"
is genuinely not curve-like and the curve dictionary breaks between chi(O)
and Delta^2. Either resolution is structural information the program needs
BEFORE attempting the square. This is a new, precisely posable question:
compute the CC-Euler characteristic of the DIAGONAL datum in their
formalism and compare with Bokstedt's tower. (First step in section 6.)

## 2. Candidate 2: van der Geer-Schoof descendants (Borisov; Bost; He)

- van der Geer-Schoof (math/9802121, Selecta Math 2000; archived:
  vandergeer-schoof-1998-effectivity-arakelov.pdf): h^0(D) :=
  theta-regularized log-count of sections, h^1(D) := h^0(kappa - D) BY
  DEFINITION, exact RR h^0 - h^1 = deg D - (1/2)log|d_K|; entire proof =
  Poisson summation (the program's witness P1, doc 19, already exhibits
  the identity). STATUS: theorem. DEFICITS: h^0 is a real number (PF
  fails); h^1 is defined by duality, so PD is a tautology, not a theorem.
- Borisov, "Convolution structures and arithmetic cohomology"
  (math/9807151, Compositio Math; archived:
  borisov-1998-convolution-arithmetic-cohomology.pdf): the real upgrade.
  H^0 AND H^1 are defined INDEPENDENTLY as ghost-spaces (convolution-of-
  measures structures; H^1 by a Cech-like procedure), and Serre duality is
  then PROVEN as Pontryagin duality of convolution structures; RR and
  duality proven separately. STATUS: theorem. DELIVERY: honest PD + PR;
  PF still fails (ghost-space dimensions reproduce the vdGS real numbers);
  PS partial (the convolution structure remembers the section sets).
- Bost, "Theta invariants of Euclidean lattices..." (Progress in Math 334):
  the systematic infinite-dimensional extension of the theta counts
  (cited as [1] in CC 2022). Not fetched; UNVERIFIED details.
- Wei He, "Numerical cohomology for arithmetic surfaces and applications"
  (arXiv:2512.01811, Dec 2025): numerical cohomology + an "absolute
  arithmetic Riemann-Roch" for ARITHMETIC SURFACES - but these are
  relative curves fibered over Spec Z, NOT the arithmetic square
  Spec Z x_S Spec Z. Useful as a template for surface-level bookkeeping;
  does not touch the program's square. UNVERIFIED beyond abstract.

Scoring: CIRCULARITY clean across the family (only Poisson summation in).
CARRIER: fails the guard STRUCTURALLY - theta/Poisson works for every
lattice; Epstein passes; this family can never discriminate (section 0).
Integrality status: non-integer everywhere in this family; the integrality
problem is exactly what CC solved. DELIVERY: PD + PR without PF.
TRACTABILITY RANK: 4 as a vessel; but rank-1 as the CONTROL MODEL - any
duality the program constructs at the square level should be required to
reproduce Borisov's independent-H^1 discipline (no defining h^1 by
duality) and the vdGS numbers in the curve shadow.

## 3. Candidate 3: Braverman-Kazhdan / Ngo Poisson summation conjecture

PRECISE SHAPE (per Getz-Liu arXiv:1707.06091, archived:
getz-liu-2017-refined-poisson-bk-spaces.pdf; and Getz-Hsu-Leslie, to appear
in JEMS (volume/pages unconfirmed), abstract quoted from arXiv:2103.10261): "Braverman and
Kazhdan proposed a conjecture, later refined by Ngo and broadened to the
framework of spherical varieties by Sakellaridis, that asserts that affine
spherical varieties admit Schwartz spaces, Fourier transforms, and Poisson
summation formulae." The intended payoff (Getz-Liu): "quite general
Langlands L-functions have meromorphic continuations and functional
equations as predicted by Langlands' functoriality conjecture."

STATUS: conjecture, with proven instances: Tate's thesis (GL_1, the
prototype); Godement-Jacquet (standard representation); Braverman-Kazhdan's
partial doubling case; Getz-Liu, 'A summation formula for triples of
quadratic spaces', Adv. Math. 347 (2019) 150-191 (arXiv:1711.08087);
Getz-Liu, 'A refined Poisson summation formula for certain
Braverman-Kazhdan spaces', Sci. China Math. 64 (2021) 1127-1156
(arXiv:1707.06091, the archived PDF) [citations split by the 2026-06-10
verification pass; both are proven instances]; Getz-Hsu-Leslie (to
appear, JEMS; arXiv:2103.10261): explicit Fourier transform on those
spaces + nonarchimedean unitarity (in the earlier works the transform was
only proven to EXIST). Ngo's reformulation routes through Hankel
transforms on reductive monoids. Whole-conjecture resolution: not close;
decades-scale program (the Duke TRT on the Poisson Summation Conjecture is
an active multi-year effort).

DELIVERY: PD ONLY - and this is the load-bearing point for the program.
The conjecture generalizes exactly the theta-functional-equation ingredient
(Tate's thesis) to all (X, rho). It produces: meromorphic continuation +
functional equation. It does NOT produce: integer finiteness (Schwartz
spaces are C-valued; PF no), section counts (PS no), or a Riemann-Roch
tying counts to a pairing (PR no), and it asserts nothing about zero
locations (DH-type counterexamples satisfy functional equations; FE is not
RH). In doc 19 section 1's decomposition: resolution of the FULL conjecture
would hand the program a vastly general PD layer and nothing else - the
carrier-blind layer (section 0).

CIRCULARITY: clean (no RH input anywhere in the framework).
CARRIER: partially correct shape - the framework is intrinsically
automorphic, so DH literally has no (G, X, rho) carrier; Epstein appears
only as Eisenstein-type data, not as the L-function of an irreducible
automorphic representation. But since the delivery is PD-only, the carrier
correctness is moot for the program's purposes.
TRACTABILITY RANK: 5 (monitor only). The right use: its PROVEN instances
(Tate, Godement-Jacquet) are the analytic shadows that any S-level
properness theorem must reproduce; the conjecture itself is not the vessel.

## 4. Candidate 4: condensed/solid mathematics and spectrum-level arithmetic duality

Three distinct items, often conflated; separated here.

(a) Solid/analytic 6-functor formalisms (Clausen-Scholze; Mann; Camargo's
notes arXiv:2603.03012 "Notes on Solid Geometry" and the 2023-24 Analytic
Stacks lecture course). What is real: a 6-functor formalism of solid
quasi-coherent sheaves on schemes locally of finite type over Z, with f_!
and a "universal proof of Grothendieck-Serre duality" extending to rigid
spaces and complex manifolds (Scholze, Analytic Geometry lectures,
math.uni-bonn.de/people/scholze/Analytic.pdf; Camargo notes). The analytic
stacks framework explicitly treats archimedean and non-archimedean
geometry on one footing - the precondition for a compactified Spec Z with
honest coherent duality at the infinite place. What is NOT in print
(UNVERIFIED, lecture-course folklore at best): a theorem "Spec Z bar is
proper as an analytic stack with coherent Serre duality whose RR recovers
vdGS/CC counts". Scholze's "What does Spec Z look like?" talk is
explicitly speculative. STATUS: foundations = theorem-grade but partially
unwritten; the arithmetic compactification statement = program.
DELIVERY if it lands: PD + PF at the coherent level (nuclearity/
trace-class conditions are the analytic substitute for properness-
finiteness) - precisely the two layers the derived square lacks (doc 18:
"nothing truncates the tower"). PR/PS would still need the count
interpretation. CIRCULARITY: clean. CARRIER: preserved (no ring => no
analytic ring => no solid THH). TRACTABILITY RANK: 2 - the program's
docs 18-19 Euler pairing can be RE-POSED here today (section 6, step B),
even though the foundations are partially unwritten.

(b) Spectrum-level arithmetic duality - the only EXISTING "arithmetic
duality over the sphere" theorems found. Blumberg-Mandell, "K-theoretic
Tate-Poitou duality and the fiber of the cyclotomic trace" (arXiv:
1508.00014, Invent. Math. 2020; archived: blumberg-mandell-2015-
ktheoretic-tate-poitou.pdf): a SPECTRAL lift of the classical Poitou-Tate
9-term sequence - K(1)-locally, an Anderson self-duality for the algebraic
K-theory of number rings with p inverted; application: the homotopy type
of the fiber of the cyclotomic trace K(S) -> TC(S) at odd primes in terms
of K(Z). Extensions: prime 2 (arXiv:2501.03460, 2025); higher-dimensional
arithmetic schemes, PROPER case (arXiv:2504.14153, 2025). STATUS: theorem.
DELIVERY: PD + PF over the sphere, but on the ETALE/GALOIS side: the
duality pairs K-theory/etale cohomology with compact supports - global
arithmetic properness IS already a theorem at the etale level over S.
What it lacks for the program: it is not coherent - no Arakelov divisors,
no section counts, no RR; its zeta contact is special VALUES (Quillen-
Lichtenbaum world), never zeros. CIRCULARITY: clean. CARRIER: perfect
(input = ring spectra; DH/Epstein have none). TRACTABILITY RANK: 3 - not
the vessel, but the proof-of-concept that "global duality over S" is a
theorem-shaped thing, and a cheap diagnostic target (section 6, step C).

(c) Clausen, "A K-theoretic approach to Artin maps" (arXiv:1703.07842) +
MIT thesis "Arithmetic duality in algebraic K-theory" (2013): functorial
Artin map from K(LCA_F) (locally compact F-vector spaces) recovering Artin
reciprocity; Clausen's own framing: the argument "takes the same form as
Tate's observation that the theory of Haar measures formally implies the
product formula". The product formula is the degree-zero shadow of
"Spec Z bar is a complete curve" - i.e. this IS properness-over-S at
degree level, K-theoretically. STATUS: theorem. DELIVERY: the deg-0 slice
of PD/PR. Useful as the base case any S-level RR must contain.

Re-running docs 18-19 condensed (the assigned sub-question): the precise
open question is whether THH of the relevant ANALYTIC ring (Z with its
archimedean structure, or the analytic-stack compactification of
HZ ^ HZ) has finite-rank/nuclear homotopy per class - i.e. whether
nuclearity truncates the Bokstedt tower the way properness truncates
coherent cohomology. No literature found that computes THH in the solid/
analytic category for arithmetic rings (UNVERIFIED that it exists at all
as of 2026-06); this is a genuinely open, well-posed formulation - an
exact statement of the obstruction, which is the deliverable here.

## 5. Candidate 5: direct hits - negative results (recorded faithfully)

- "Poisson summation for ring spectra": NO HIT. No paper found stating or
  conjecturing a Poisson-summation theorem internal to ring spectra.
- "Spectral theta functions" / "theta correspondence sphere spectrum":
  NO HIT in the intended sense (hits are classical theta/modular-form
  literature, e.g. Comm. Math. Phys. 2025 on Fourier eigenmeasures on
  spheres - unrelated).
- "Arithmetic duality over the sphere": resolves to exactly the
  Tate-Poitou family of section 4(b) - etale-side only.
- Adjacent (already in the program's file): Hesselholt TP for smooth
  proper F_q-schemes (doc 18 refs); Weil-etale/THH special-value bridge
  (arXiv:2011.11549, Duke 2024). Both are value-level, proper-hypothesis
  results; neither states an S-level Poisson theorem.

Conclusion of the direct sweep: the phrase the program needs does not
exist in the literature. The nearest existing theorems are (i) CC's
curve-level integer RR + duality over S[+-1]/S and (ii) spectral
Tate-Poitou duality. The square-level coherent statement is unclaimed
territory.

## 6. Ranked recommendation

```text
RANK 1  CC absolute RR, pushed to the square.    [theorem substrate exists]
RANK 2  Condensed/solid re-run of the Euler pairing (nuclearity as
        properness).                              [posable now; foundations partly unwritten]
RANK 3  Spectral Tate-Poitou as PD diagnostic.    [theorems exist; etale side]
RANK 4  Borisov as control model (independent-H^1 discipline).
RANK 5  BK/Ngo: monitor only (PD-only, carrier-moot, decades-scale).
```

RECOMMENDED NEXT ATTEMPT (Rank 1), first concrete steps, in order:

A. RECONCILE THE GENUS PROBES (cheap, decisive, computable). CC's
   chi(D) = deg_2 D + 1 is genus-0; doc 18's <Delta,Delta> = zeta'(0)
   is genus-1.46. Compute the curve dictionary's consistency: in CC's
   formalism, what is the self-pairing of the diagonal datum? The curve
   dictionary says deg K = 2g - 2: CC's deg_2 K = -2 gives g = 0, while
   THH's diagonal gives 2 - 2g = zeta'(0), i.e. g = 1.459 (and the
   canonical degree comparison is -2 log 2 = -1.386 nats vs
   +0.919 nats [SIGN CORRECTED by the 2026-06-10 verification pass:
   THH-side deg K = 2g - 2 = -zeta'(0) = +0.919, since doc 18 has
   Delta^2 = 2 - 2g = -deg Omega^1] - they disagree in SIGN as well as
   magnitude (CC on the g < 1 side, THH on the g > 1 side); the tension
   is STRONGER than first stated. A witness-level audit of both dictionaries (which
   invariant each construction actually computes, in common units) is a
   one-afternoon computation and either aligns the two sphere-bases or
   proves they are different objects.
B. POSE THE CC SQUARE. Write the precise object: Arakelov divisors on
   Spec Z bar x_S Spec Z bar in the tolerant-S-module formalism; demand
   (i) integer dim_S of H^0, H^1, H^2, (ii) Pontryagin-Serre duality
   H^i <-> H^{2-i}, (iii) the restriction of the Euler form to diagonal
   classes reproducing doc 18's torsion tower degree-by-degree. The
   2026 Jacobian paper builds Pic/Jacobian infrastructure consistent
   with this direction (interpretation, not their stated aim); the
   program's THH computation is the complementary half (they have the
   integer dimensions, the program has the sign-bearing diagonal).
   Fail-closed criterion, pre-registered: if the CC-square Euler form
   exists but its diagonal does NOT reproduce the Bokstedt tower signs,
   the two sphere-bases are different objects and the program must pick
   one carrier and re-audit.
C. CHEAP PD DIAGNOSTIC (Rank 3 fallback, parallelizable): check whether
   Blumberg-Mandell's Anderson-duality normalization (the twist/shift in
   I_{Z_p} Anderson dual) matches doc 20's self-dual KMS-1/2 / quarter-
   shift pattern under the regularized-determinant dictionary. A match
   would tie the etale-side properness theorem to the program's ladder
   normalization; a mismatch localizes what "coherent vs etale" costs.

## 7. Archived sources (research/proof/refs/)

- connes-consani-2022-riemann-roch-specZbar.pdf  (arXiv:2205.01391)
- connes-consani-2023-riemann-roch-ring-Z.pdf    (arXiv:2306.00456)
- connes-consani-2026-jacobian-specZbar.pdf      (arXiv:2602.15941)
- borisov-1998-convolution-arithmetic-cohomology.pdf (arXiv:math/9807151)
- vandergeer-schoof-1998-effectivity-arakelov.pdf (arXiv:math/9802121)
- blumberg-mandell-2015-ktheoretic-tate-poitou.pdf (arXiv:1508.00014)
- getz-liu-2017-refined-poisson-bk-spaces.pdf    (arXiv:1707.06091)

Not archived (abstract-level only, marked where used): arXiv:2103.10261
(Getz-Hsu-Leslie, JEMS 2025), arXiv:2501.03460, arXiv:2504.14153,
arXiv:1703.07842, arXiv:2512.01811, arXiv:2603.03012, Scholze
Analytic.pdf lectures, CC Weil-positivity arc (arXiv:2006.13771,
arXiv:2310.18423 - relevant to the zero-side fork, not to properness;
their positivity results are unconditional but subspace-restricted, and
were NOT used here).
