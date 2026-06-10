# N - The CC square, posed: Arakelov divisors on Spec Z bar x Spec Z bar in the Connes-Consani formalism (K-doc step B)

Status: document-level pass executed 2026-06-10 (fresh context, worker N). No
numerics, no derivations beyond two small exactly-checkable computations
(flagged where they occur). Every quoted statement was read from the archived
PDFs (research/proof/refs/): connes-consani-2022-riemann-roch-specZbar.pdf
(arXiv:2205.01391v2), connes-consani-2023-riemann-roch-ring-Z.pdf
(arXiv:2306.00456v1), connes-consani-2026-jacobian-specZbar.pdf
(arXiv:2602.15941v1). Anything not checked from these three sources is marked
UNVERIFIED. Discipline: no RH / zero-side input anywhere in sections 1-6;
the 2026 paper's spectral-realization section (its sec 9) is inventoried as a
firewalled item only.

Executes step B of research/work/K-global-poisson-survey.md sec 6; answers to
doc 21's Q-SCHEME gate and tension T-b.

---

## 1. Formalism inventory (citation-grade)

### 1.1 The category

Base category: S-Mod = ΓSets_* = pointed covariant functors Γ^op -> Sets_*
from (a skeleton of) finite pointed sets to pointed sets ("Γ-sets, aka
S-modules"; 2022 sec 1 and sec 2; 2023 sec 2). The absolute base S is the
identity functor — their words (2022 sec 1): "The base S is in fact the most
elementary categorical form of the sphere spectrum in homotopy theory [6]"
([6] = Dundas-Goodwillie-McCarthy). S[±1] := S[µ_{2,+}] is the spherical
monoid algebra of the multiplicative monoid {±1}: S[±1](F) = {-1,0,1} ∧ F
(2022 sec 2; 2023 sec 1). An abelian group A embeds via the Eilenberg-MacLane
functor HA (A-valued divisors on F, pushforward by summation); H is full and
faithful (2022 sec 1, used in proof of Prop 5.2).

Two ring presentations of Z, both load-bearing:
- over S[±1]: Z = polynomials in X = 3 with coefficients {-1,0,1},
  presentation 1 + 1 = X - 1; "for p = 3 (and only for this rational prime)
  the Witt vectors with only finitely many non-zero components form a subring
  inside the ring of p-adic integers ... isomorphic to Z" (2022 sec 1,
  Remark 3.2).
- over S: Z = S[X] with X = -2, presentation 1 + 1 = X + X^2 (2023 abstract,
  footnote 3).

Tolerance: a tolerance relation R on X is reflexive + symmetric (no
transitivity); T_* = pointed category of tolerance sets; a tolerant S-module
is a pointed covariant functor Γ^op -> T_* (2022 Definition A.1; 2023 sec 2).
Tolerance enters because the Γ-space H(D) built by Dold-Kan is NOT a Kan
simplicial set: "The lack of transitivity of the homotopy relation in non-Kan
complexes is dealt with using the classical notion of tolerance relation"
(2022 sec 1). The key example: for (A,d) an abelian group with translation-
invariant metric and λ > 0, the tolerant module (A,d)_λ has relations
R_k = {((x_i),(y_i)) : Σ d(x_i,y_i) ≤ λ} (2022 Prop A.3). U(1)_λ :=
(R/Z, d)_λ with d the length-1 metric.

### 1.2 The dimension

2022 Definition A.2 (over S[±1]) / 2023 Definition 2.1 (over S), quoted
(2023 form): "A subset F ⊂ E(1_+) generates E(1_+) if the following two
conditions hold 1. For x,y ∈ F, with x ≠ y ⟹ (x,y) ∉ R 2. For every
x ∈ E(1_+) there exists α_j ∈ {0,1}, j ∈ F and y ∈ E(1_+) such that
y = Σ_F α_j j ∈ E(1_+) in the sense of (2.4), and (x,y) ∈ R. The dimension
dim_S(E,R) is defined as the minimal cardinality of a generating set F."
Over S[±1] the coefficients are α_j ∈ {-1,0,1}. So: dim = minimal number of
generators whose {0,1}- (resp. {-1,0,1}-) combinations, FORMED INSIDE the
partially-defined addition of the module, reach every element up to
tolerance R. An integer by definition.

Computed values (the whole quantitative content):
- 2022 (1.3)/Prop 3.3(i): dim_{S[±1]}(‖HZ‖_n) = ⌈log(2n+1)/log 3⌉
  (‖HZ‖_n = Z-divisors of total mass ≤ n). The optimal generating sets are
  the powers {3^i} — the polynomial variable of Z = S[±1][X], X = 3.
- 2023 Lemma 3.2(ii)/Theorem 3.3: minimal number of S-generators of
  (HZ)_{[-a,a]} is n+1 for 2^{n-1} ≤ a < 2^n; dim_S H^0(D) = ⌈deg_2 D⌉ + 1
  (deg_2 := deg/log 2, ⌈·⌉ = smallest integer > x).
- 2022 Prop 4.1: dim_{S[±1]} U(1)_λ = ⌈(-log λ - log 2)/log 3⌉ for λ < 1/2,
  0 for λ ≥ 1/2. 2023 Prop 4.2: dim_S U(1)_λ = m for 2^{-m-1} ≤ λ < 2^{-m}.
  The over-S generating sets are {(-2)^{-j}} — again the ring presentation.
  The proofs are covering/packing arguments (2λ·3^k ≥ 1, resp. 2λ·2^k ≥ 1).

READING (mine, but forced by the proofs): dim_{S[±1]} and dim_S are METRIC
ENTROPIES — log-cardinality (base 3 resp. 2) of a minimal additive covering
at tolerance scale λ, rounded up to an integer. dim H^0 = additive-basis
count of lattice points in the adelic box; dim H^1 = covering number of the
circle at scale λ. One CC dimension unit = log 3 (over S[±1]) or log 2
(over S) nats. This is the single most consequential fact for the program:
the dimension is a QUANTIZED LOG-COUNT with resolution one base-unit, not a
cardinality.

### 1.3 The cohomologies of an Arakelov divisor

D = Σ a_j{p_j} + a{∞} (a_j ∈ Z, a ∈ R) determines the compact adelic box
O(D) = Π_ν O(D)_ν ⊂ A_Q with O(D)_∞ = [-e^a, e^a] handled functorially as
‖HR‖_{e^a} (2022 sec 2). The master object is the morphism of S[±1]-modules

    ψ : HQ × HO(D) -> HA_Q,   ψ(q,a) = q + a    (2022 (1.2)/(2.3)),

Q embedded diagonally in A_Q. The Dold-Kan correspondence of their [4]
(Segal's Gamma rings and universal arithmetic, QJM 2021) — which handles
SHORT complexes (two terms) — produces the Γ-space H(D) := Γ(α|_E)
(2022 Prop B.2), and the tolerant homotopies give (2022 Prop 2.2):

- H^0(D) = π_1^T(H(D)) = ker ψ ≅ ‖H^0(Spec Z, O(D)_f)‖_{e^a}; for
  D = a{∞} this is ‖HZ‖_n, n = ⌊e^a⌋.
- H^1(D) = π_0^T(H(D)) = coker ψ as a TOLERANT module: the pair (HA_Q, R),
  R_k = {(x,y) : x - y ∈ Image ψ(k_+)} (2022 (2.5)); computed by
  2022 Prop A.5 to be π*((R/L, d)_λ), λ = e^{deg D}, L the section lattice
  (A.4) — i.e. H^1 is NOT a quotient (which would be divisible, dimension-
  less) but the un-quotiented module carrying the relation. The tolerance IS
  the finiteness mechanism for H^1.
- Both depend only on the linear-equivalence class (Prop 2.2(iii)), which is
  what reduces everything to D = a{∞} via the Q^×-action on A_Q.

There is no H^2 and no π_n^T for n ≥ 2 anywhere in the two RR papers: the
input is a two-term complex; the machinery as published defines exactly
π_0^T and π_1^T of Γ(α|_E).

### 1.4 The two theorems

2022 Theorem 1.1 (= 4.3), over S[±1]:
    dim_{S[±1]} H^0(D) - dim_{S[±1]} H^1(D) = ⌈deg' D + log' 2⌉' - 1_L,
deg' = deg/log 3, ⌈·⌉' the odd ceiling, 1_L the indicator of the exceptional
open set L (2022 (3.4)) of finite Lebesgue measure |L| = 1.14099...

2023 Theorem 1.1 (= 5.1), over S:
    dim_S H^0(D) - dim_S H^1(D) = ⌈deg_2 D⌉' + 1,
⌈·⌉' the right-continuous odd ceiling. Their listed improvements (2023
sec 1): exceptional set eliminated; "Formula (1.1) displays a perfect
analogy with the Riemann-Roch formula holding for curves of GENUS 0";
deg_2(K) = -2 is integral.

2022 Theorem 1.2 (= 5.3), Serre duality, ONLY over S[±1]:
    H^0(K - D) ≅ Hom_{ΓT_*}(H^1(D), U(1)_{1/4}),   K = -2{2},
    deg K = -2 log 2,
"where U(1)_{1/4} coincides with H^1(K), playing the role of the dualizing
module in Pontryagin duality." The mechanism is 2022 Prop 5.2: for any
metric abelian group (A,d), Hom_{ΓT_*}((A,d)_λ, U(1)_µ) = the characters
χ ∈ Â with Σ|x_i| ≤ λ ⟹ Σ|χ(x_i)| ≤ µ — i.e. NORM-CONTROLLED Pontryagin
duality; specializing A = R/Z, µ = 1/4 returns ‖HZ‖_{1/(4λ)} (proof of
Thm 5.3). Internal Hom backbone: 2022 Lemma 5.1,
Hom_S(‖HR‖_λ, ‖HR‖_µ) ≅ ‖HR‖_{µ/λ}.

Three structural facts about the duality:
(a) The dualizing scale 1/4 is pinned by RR-symmetry, their words (2022
    sec 5): dim U(1)_λ = 1 "also holds for ... 1/6 ≤ λ < 1/2: the specific
    choice λ = 1/4 is dictated by the invariance of the Riemann-Roch
    formula (4.3) when one switches H^0 and H^1 and replaces D by K - D".
    A QUARTER-shift pinned by self-duality of the formula. (Observation
    only: this rhymes with the program's recurring quarter/half-shift
    normalizations, doc 20 / J-doc / K-doc step C. Not a derivation.)
(b) K = -2{2} is supported at the prime 2 only as a representative: on
    Spec Z bar, Pic ≅ R via deg (class number 1, units ±1), so the
    canonical CLASS is just the degree -2 log 2 = -log 4 — the 4 is
    1/(dualizing scale). The support at {2} is bookkeeping, not arithmetic
    of the prime 2.
(c) Over S (2023) there is NO duality section. The clean genus-0 RR and the
    Pontryagin-Serre duality are currently proven over DIFFERENT bases.
    UNVERIFIED whether a duality over S exists anywhere in print
    (consistent with K-doc sec 1.1(b)).

### 1.5 What plays the role of tensor product (the inventory the square needs)

Four distinct product-like structures exist in the corpus; none is the
external product of two curves:

(P1) Levelwise product of S-modules: (F_1 × F_2)(F) = F_1(F) × F_2(F)
     (2022 sec 2). Used for HQ × HO(D). This is the categorical PRODUCT,
     not a tensor.
(P2) Smash-type multiplication maps: m : HR(X) ∧ HR(Y) -> HR(X ∧ Y) (2022
     Lemma 5.1 proof); S[±1] = {-1,0,1} ∧ F as monoid algebra; the
     "(S[±1] ∧ -)-algebra" structure (2022 sec 2, citing [6] 2.1.5). So the
     Day-convolution / Lydakis smash ∧ of Γ-sets is available in their
     world and they use its structure maps — but no external smash of two
     GEOMETRIES is ever formed.
(P3) Tensor product ON the curve (Picard-monoid product): 2026 Prop 2.9,
     H_{D_1+D_2} = H_1 · H_2 ≅ H_1 ⊗_Z H_2 (rank-1 subgroups of Q);
     2026 sec 3.2: (L_1,‖·‖_1)·(L_2,‖·‖_2) = (L_1 ⊗_Z L_2, ‖·‖_1·‖·‖_2);
     2026 Thm 1.4/8.15: adele product = tensor of framed/rooted divisors.
     This is rank-1 ⊗ rank-1 = rank-1: the INTERNAL product (line bundles
     on one curve), not a square. Note its diagonal mechanism, 2026
     Remark 8.13: the tensor of roots uses the inverse of the ring
     multiplication µ_n : Z/n ⊗ Z/n -> Z/n as a coproduct ∆_n on Q/Z —
     "ill-defined in the category of abelian groups (where
     Q/Z ⊗_Z Q/Z = 0)", rigorous as Ind-rings. The ring structure of Z is
     again the carrier.
(P4) Tolerant-module products: NOT DEFINED. ΓT_* is enriched in S-modules
     (2022 Lemma A.1) but no monoidal/smash structure on ΓT_* (no rule for
     the tolerance relation on a smash of two tolerant modules) appears in
     any of the three papers. UNVERIFIED whether it exists elsewhere.

### 1.6 The 2026 Jacobian paper: what it adds and what it deliberately is not

Adds: extended (infinite-genus) divisors D = Σ n_p[p], n_p ∈ Z ∪ {∞}
(2026 Def 2.3) ↔ rank-1 subgroups of Q (Prop 2.4); Pic(Spec Z) ≅ Q^×\A_f/Ẑ^×
(Prop 2.11); arithmetic Pic of Spec Z bar = pairs (L, ‖·‖) with semi-norm,
≅ X_Q = Q^×\A/Ẑ^× the "Riemann sector" (Thm 1.1/3.4); Jac = Pic/R^×_+;
Abel-Jacobi Θ with image = idempotents (Thm 2.16); sheaf O(D) of
O_{Spec Z bar}-modules per arithmetic divisor (Thm 1.2/Prop 5.1 — the
structure sheaf's archimedean sections carry the unit-ball condition
Σ‖φ(x)‖ ≤ 1, recovering the 2022 H^0 datum).

Deliberately is not the square. Their own words (2026 sec 1, on sec 9):
"This marks a decisive departure from the classical function field analogy.
There, the spectral theory arises from the action of the Frobenius
endomorphism on the Jacobian. Here, we rely on the action of the idèle class
group acting by translations as the Galois group of a covering." And the
opening frame (2026 sec 1): "the classical Jacobian of Spec Z—its ideal
class group—is trivial, suggesting a curve of genus zero. On the other hand,
the spectral realization of the zeros ... strongly suggest that Spec Z
should be regarded as a curve of infinite genus."

CORRECTION TO THE K-DOC GENEALOGY: K-doc sec 1.1(c) read the 2026 paper as
"CC are walking the function-field proof's path (curve RR -> Pic -> Jacobian
-> correspondences), currently between steps 2 and 3." The quoted passage
shows the opposite at the decisive joint: at exactly the step where the FF
proof moves to Frobenius correspondences ON THE SQUARE, CC explicitly swap
in idele-class translations on Pic-tilde (the Connes-1999 spectral path, a
zero-side construction — firewalled here per discipline). There is no C × C,
no intersection pairing, no H^2 anywhere in the 2026 paper. CC are NOT
building toward the square; the square is unclaimed by them too.

---

## 2. The square, posed

### 2.1 The object demanded

    Arakelov divisors on (Spec Z bar) ×_B (Spec Z bar),  B ∈ {S, S[±1]},
    with cohomologies H^0, H^1, H^2 as (tolerant) B-modules, integer
    dimensions dim_B, Pontryagin-Serre duality against a dualizing module,
    and an Euler/intersection form on divisor classes.

### 2.2 What is definable today in CC's formalism

(D1) The AFFINE square exists as a B-algebra: HZ ∧_B HZ, using the smash of
     Γ-sets (P2 above; the smash of S-algebras is standard in ΓSets_*, and
     CC's [5] "On Absolute Algebraic Geometry, the affine case" provides
     Spec of an S-algebra — UNVERIFIED in detail, [5] not archived). So
     "Spec(HZ ∧ HZ)" is a formable expression in their world.
(D2) The diagonal exists: the multiplication µ : HZ ∧ HZ -> HZ is a map of
     B-algebras (this is the ring structure of Z, nothing else).
(D3) Curve-level Arakelov data on each factor exists (the whole sec 1
     inventory).

### 2.3 What is missing (the precise reasons the compactified square is not yet definable)

(M1) STRICT COLLAPSE ONTO THE DIAGONAL. At the strict (1-categorical) level
     the algebraic content of the square degenerates: Z ⊗_Z Z = Z, and the
     underlying "algebraic shadow" of HZ ∧ HZ is again Z (the universal map
     HZ ∧ HZ -> H(Z ⊗ Z) = HZ; in spectra this is a π_0-isomorphism).
     [Flagged: the spectra statement is standard background, taken on
     citation from doc 18's framework; the precise π_0^T of the strict
     Γ-set smash in CC's tolerance sense is an OPEN COMPUTATION — posed as
     Q1 in sec 6.] All off-diagonal directions of the arithmetic square —
     the cotangent data, doc 18's entire torsion tower — are DERIVED
     phenomena (higher homotopy of the derived smash). CC's published
     machinery extracts exactly π_0^T and π_1^T of Γ-spaces built from
     SHORT complexes ([4]; 2022 appendix B). A formalism that retains only
     (π_0, π_1) of strict constructions is structurally blind to the only
     part of the square that differs from the curve.
(M2) NO TWO-DIMENSIONAL ADELIC THEORY. The curve theory's master object is
     ψ : HQ × HO(D) -> HA_Q with Q diagonal in A_Q. A square RR needs the
     analogue of the length-2 adelic (Cech/Parshin-type) resolution: a
     complex with three terms, whose middle cohomology is H^1 of the
     surface and whose end is H^2. Strictly, "A_Q ⊗ A_Q over Q ⊗ Q = Q"
     carries no second dimension; no candidate object is present in the
     papers. (For schemes this is Parshin-Beilinson 2-adeles on flags; the
     arithmetic square is not a scheme — doc 17/18 — so even that template
     is only an analogy.)
(M3) NO π_2^T / NO LONG-COMPLEX DOLD-KAN. Their [4] extension of Dold-Kan
     is stated for short complexes; the tolerance treatment of homotopy is
     developed for π_0, π_1 (2022 (B.10), Prop B.1). An H^2 needs π_2^T of
     a non-Kan Γ-space: the relation-not-equivalence problem compounds at
     each level, and nothing in print defines or controls it. UNVERIFIED
     whether their Gromov-norm paper [3] (Spec Z and the Gromov norm, TAC
     2020) defines higher π_n^T usable here ([3] not archived).
(M4) NO MONOIDAL STRUCTURE ON TOLERANT MODULES (P4 above): even given two
     tolerant modules (E_1,R_1), (E_2,R_2), the tolerance on E_1 ∧ E_2 is
     undefined — needed for any Kunneth-type assembly of square cohomology
     from curve cohomology.
(M5) NO KUNNETH FOR dim_B. dim_B is a quantized log-count (sec 1.2); under
     tensor of intervals the logs ADD, so the correct Kunneth shape is
     ADDITIVE (dim(E_1 ∧ E_2) ≈ dim E_1 + dim E_2, up to rounding), but no
     such theorem exists. Without it, no surface RR can be assembled or
     even consistency-checked against the curve.
(M6) BASE MISMATCH AT CURVE LEVEL. Requirement (ii) below needs duality;
     duality is proven only over S[±1] (with the exceptional set 1_L
     polluting RR); the clean genus-0 RR is only over S (no duality). The
     square program must first close this gap on the CURVE: either prove
     duality over S, or remove 1_L over S[±1]. As it stands there is no
     single base over which even the curve-level package {integer RR
     without exceptional set} + {PS duality} is complete.

### 2.4 The program's demands on the square (numbered requirements, pre-registered)

Let X = Spec Z bar, and suppose a compactified square X ×_B X with an
Arakelov divisor theory is constructed in a CC-type formalism. The program
requires:

R(i)   INTEGER DIMENSIONS: dim_B H^0(D), dim_B H^1(D), dim_B H^2(D) defined
       and integer-valued for every Arakelov divisor D on the square, by
       generator-count (no theta/measure-valued dimensions), finite for
       every D — this finiteness IS the properness theorem (doc 18 sec 5:
       "nothing truncates the tower" is exactly what R(i) must defeat).
R(ii)  PONTRYAGIN-SERRE DUALITY: a canonical divisor class K_X2 and
       isomorphisms of tolerant B-modules
       H^i(D) ≅ Hom_{ΓT_*}(H^{2-i}(K_X2 - D), Ω), i = 0,1,2, with a
       dualizing module Ω whose scale is pinned by RR-symmetry (the
       square's analogue of U(1)_{1/4}), over ONE base B for which the
       curve-level package is also complete (M6).
R(iii) DIAGONAL = BOKSTEDT TOWER. The diagonal class Δ (defined via µ of
       (D2)) has a self-pairing under the Euler/intersection form of the
       theory, and its graded constituents reproduce Bokstedt
       (π_{2k-1} THH(Z) = Z/k, odd degrees only) DEGREE BY DEGREE. Two
       grades of this demand, in decreasing strength:
       R(iii)-strong (cardinality level): the theory's degree-(2k-1)
         diagonal object is a finite object of CARDINALITY exactly k, in
         odd degree (hence pairing with a minus sign), for every k ≥ 1.
         This is the only form that can feed doc 19's EF supply
         (Λ(p^i) = log|THH_{2i}(F_p)| etc.), which consumes exact
         cardinalities, not dimensions.
       R(iii)-weak (dim_B level): dim_B of the degree-(2k-1) diagonal
         object equals ⌈log_2 k⌉ over S (resp. ⌈log_3-type count over
         S[±1]). [Small exact computation, mine: for the discrete tolerance,
         dim_S H(Z/k) = ⌈log_2 k⌉ for k ≥ 2 — lower bound 2^{#F} ≥ k as in
         2023 (3.1), upper bound by binary-digit generators {1,2,...,
         2^{m-1}} whose subset sums cover [0, 2^m - 1] ⊇ Z/k. Checkable in
         one line; not in CC.]
       The weak form is LOSSY: ⌈log_2 k⌉ collapses all k in a dyadic
       interval; Σ(-1)·⌈log_2 k⌉ has no CC-internal regularization and its
       (externally) regularized value is NOT ζ'(0). A theory meeting only
       R(iii)-weak does not reconnect to doc 18/19 and must be recorded as
       computing a different invariant.
R(iv)  CURVE SHADOW: restriction of the square theory along either
       projection (divisors of the form D × X) reproduces the curve-level
       χ of the corresponding factor divisor exactly (the analogue of
       Borisov-discipline from K-doc sec 2: no defining the new H's by
       duality, no defining the square χ to make RR true).
R(v)   CARRIER FATALITY (G-INT-style guard): every ingredient added for the
       square must consume the multiplication of Z (the map µ), so that the
       construction is NONEXISTENT — not merely false — for DH and for a
       generic Epstein lattice (sec 5 below identifies the exact joints).

---

## 3. The Q-SCHEME verdict: what χ(D) computes

In doc 21 sec 2's (ladder data, weight dictionary, scale, scheme) language:

- LADDER DATA: the archimedean degree half-line alone. After linear
  equivalence (Prop 2.2(iii)) every divisor is D = a{∞}; the finite places
  enter only through the Q^×-action that performs this reduction and
  through the section lattice L (2022 (A.4)). There is no prime-indexed
  ladder: χ(D) is a function of the single real number deg D. CC's χ
  cannot see an individual prime (the canonical class's support at {2} is
  representative bookkeeping, sec 1.4(b)).
- WEIGHTS: uniform — every generator counts 1. No 1/|Aut|, no groupoid
  measure, no q->1 leak (contrast doc 17 sec 5's Hall-form caveat). This is
  why the output is an honest integer.
- SCALE: FIXED BY THE BASE RING. One dimension unit = log|coefficients| =
  log 2 over S ({0,1}), log 3 over S[±1] ({-1,0,1}). This is the striking
  answer to doc 18's scale note (the J-doc finding that ζ'(0) carries one
  unit choice): CC's formalism does not leave the scale free — it is set by
  the choice of absolute base. But it is set BY FIAT OF BASE, and the two
  available bases give different formulas (exceptional set appears over
  S[±1], disappears over S; genus constant shifts). The scheme question
  reappears one level up, as base-dependence: what selects S over S[±1] is
  "the formula is cleaner" (their listed improvements, 2023 sec 1) — an
  aesthetic selector, not a theorem-selector. Same disease as doc 21 T-a,
  milder strain.
- SCHEME: NONE. χ(D) is a difference of two finite integers. No infinite
  ladder is ever summed; no regularization, no conjugate-pairing convention,
  no KMS choice anywhere. The Poisson-summation content is the same
  classical fact Weil's adelic proof uses (Q discrete cocompact self-dual
  in A_Q), consumed at the level of strong approximation (2022 Prop A.5
  proof: p_f(Q) dense in A_f^Q), not as a theta identity.

VERDICT. χ(D) computes the QUANTIZED DEGREE: the image of the analytic
(vdGS/Poisson) curve-level Euler characteristic — which for Q is deg D
exactly, since log|d_Q| = 0 — under the quantization map
x ↦ ⌈x/log 2⌉' + 1 (over S). The integer-valuedness comes from replacing
the theta-count (a measure) by a generator-count (a covering number): the
ceiling IS the tolerance, materialized. Nothing about zeros, nothing about
primes individually, nothing regularized.

IS THE INTEGER MECHANISM THE SAME MECHANISM THAT ERASES THE THH TORSION?
Yes, and one can say exactly how, in two layers:
(L1) RESOLUTION EROSION: dim_B has resolution one base-unit (log 2 nats).
     The Bokstedt entry at degree 2k-1 carries log k nats EXACTLY; under
     dim_S it becomes ⌈log_2 k⌉ (computation in R(iii)-weak above) — the
     sub-unit information distinguishing Z/k within a dyadic block is
     rounded away. The regularized non-integer ζ'(0) = -(1/2)log 2π is a
     SUB-UNIT constant (0.92 nats < log 3, and not a multiple of log 2);
     no CC-dimension difference can ever equal it. The ceiling that
     promotes vdGS's reals to integers and the coarseness that forgets the
     tower's fine cardinalities are the same rounding.
(L2) TRUNCATION EROSION (the deeper layer): the tower lives in degrees
     2k-1 ≥ 1 of a DERIVED smash; CC's machinery takes π_0^T, π_1^T of
     STRICT constructions (M1/M3). The torsion is not even presented to
     the dimension functor to be rounded: it is quotiented away one
     categorical level earlier. So doc 21's reading (b) of T-b holds in a
     sharpened form — CC's coarseness forgets the torsion TWICE, once by
     truncation (structural, provable from their definitions as published:
     no slot of degree ≥ 2 exists) and once by quantization (would apply
     even to a derived extension that kept the slots but measured them
     only with dim_B).

THE GENUS QUESTION. CC's genus-0 is a theorem about a different object than
the cotangent-of-unit-map genus. Their g = 0 is the RR-CONSTANT genus of
the quantized-degree theory: χ(D) = deg_2 D + (1 - g) with g = 0, and
deg_2 K = -2 = 2g - 2 — internally consistent, entirely curve-level, about
the (π_1^T, π_0^T) of the strict adelic ψ. Doc 18's g = 1.459 is the
DIAGONAL genus of the derived square: 2 - 2g = <Δ,Δ> = ζ'(0), about
π_{≥1} of the derived smash — the exact range CC truncate. On an honest
curve the two probes agree because the surface RR + adjunction tie them;
here nobody possesses the tying theorem (that is precisely the missing
square). And CC themselves hold a THIRD genus: "Spec Z should be regarded
as a curve of infinite genus" (2026 sec 1), realized by their extended
divisors n_p = ∞. The full tally of canonical-class probes now on the
table, in nats:

    vdGS theta-RR:        deg κ = log|d_Q| = 0        ("g = 1"-like)
    CC quantized RR:      deg K = -2 log 2 = -1.386   (g = 0)
    THH diagonal (doc18): deg K = -ζ'(0)  = +0.919    (g = 1.459)
    CC Jacobian (2026):   g = ∞ (extended divisors)

Four formalisms, four canonical degrees. This confirms doc 21 sec 2's
diagnosis ("nobody has stated WHICH invariant each construction computes")
and strengthens it: the genus of "Spec Z over the sphere" is not yet a
well-posed single number; it is formalism-indexed.

THE MAP BETWEEN THE TWO BASES. It has a name: Segal's realization functor
from Γ-sets/Γ-spaces to connective spectra (CC's own [6] = Dundas-
Goodwillie-McCarthy is their citation for it; 2022 sec 1: their S "is ...
the most elementary categorical form of the sphere spectrum"). Under
realization, CC's S ↦ the sphere spectrum 𝕊, HA ↦ the EM spectrum HA.
The comparison the program needs is then precisely posable: realize the
(yet-to-be-built or even the strict) CC square and compare with
HZ ∧^L_𝕊 HZ; the discrepancy is the derived replacement (cofibrancy) —
i.e. THE DERIVED ENHANCEMENT OF CC'S FORMALISM IS, BY DEFINITION, THE THH
SIDE. The two sphere-bases are not two carriers that might disagree about
one invariant; on present evidence they are one carrier seen at two
truncation levels, and T-b is an artifact of comparing a truncated
invariant with an untruncated one. The fail-closed criterion (sec 4) is
what protects this reading from being assumed rather than tested.

---

## 4. The pre-registered fail-closed criterion (K-doc sec 6.B, refined)

SETUP REQUIRED BEFORE THE TEST CAN FIRE: a CC-square theory satisfying
R(i), R(ii), R(iv) (integer dims, duality, curve shadow) with ANY diagonal
Euler form e(Δ, Δ) — by construction or by someone else's theorem.

THE TEST: evaluate the graded diagonal against Bokstedt per requirement
R(iii), at the strong (cardinality) grade, with the dictionary FIXED IN
ADVANCE as: realization functor (sec 3) + "one CC unit = log(base) nats" +
"odd degree = minus sign". Zero free parameters remain after the base B is
named (G-INT6 ledger: choices spent = base B only; constraints = infinitely
many cardinalities |T_{2k-1}| = k plus the sign).

OUTCOMES:
(F-PASS) Diagonal reproduces the tower (cardinalities and signs). Then the
  two sphere-bases are one object; T-b dissolves as truncation artifact;
  CC's R(i) finiteness is the properness theorem the program lacks
  (doc 18 sec 5 wall), and the program's next gate is the F1 value fork
  (does the square's GLOBAL χ on non-diagonal classes see anything beyond
  the archimedean factor).
(F-WEAK) Diagonal reproduces only R(iii)-weak (dims ⌈log_2 k⌉, not
  cardinalities). Record: the CC square computes the QUANTIZED SHADOW of
  the tower. Not a refutation, but the EF supply (doc 19) cannot be fed
  from it; the program would need the pre-quantization (cardinality-level)
  objects of the CC theory, which the theory keeps (the modules themselves)
  even though dim_B forgets them — a usable partial outcome: take
  cardinalities of the CC objects, bypass dim_B.
(F-FAIL) The Euler form exists but its diagonal does NOT reproduce the
  tower even at the weak grade (wrong cardinality pattern, or wrong SIGN —
  e.g. even-degree/positive pairing like the ku square, doc 21 T-c). Then
  the two sphere-bases are genuinely different objects (truncation cannot
  explain a sign flip or a different tower), and the program must choose:
  COST OF CHOOSING CC: keep the only proven integer RR + PS duality
    (curve-level properness package, PF+PD+PR+PS); LOSE the entire torsion
    supply chain — doc 19's place-by-place EF assembly
    (Λ(p^i) = log|THH_{2i}(F_p)|), doc 18's produced archimedean constant,
    worker I's ku/lcm ladder — all of which live in derived degrees CC
    discards. The prime-supply mechanism would have to be rebuilt inside a
    formalism whose curve-level χ is provably blind to individual primes
    (sec 3, LADDER DATA). No candidate mechanism is currently visible in
    the CC corpus.
  COST OF CHOOSING THH: keep the torsion supply and the EF contact; LOSE
    the only existing integer-valued RR + duality theorems over a
    sphere-flavored base; the properness wall (doc 18 sec 5) stands with no
    known theorem-substrate, and G-INT1's TOTAL FAIL (regularized
    non-integers through the infinite tower) remains unrepaired.
  Either way, doc 21's Q-SCHEME bookkeeping must then carry a CARRIER
  column too (which sphere), not just (ladder, weights, scale, scheme).

GUARD AGAINST VACUOUS PASS: by K-doc sec 0 (PD is carrier-blind), an
F-PASS must additionally show the square theory DIES on the Epstein control
(sec 5) — a square theory that passes the diagonal test but also exists for
a non-multiplicative lattice has smuggled the tower in by hand (fitted
dictionary, G-INT6).

---

## 5. Carrier check: where CC consumes the ring Z beyond its lattice

Joint-by-joint audit of the construction (curve level, then square):

(C1) Q^× LINEAR EQUIVALENCE (2022 Prop 2.2(iii), Prop B.2): the reduction
     of every divisor to D = a{∞} — without which neither dimension
     formula applies — uses the multiplicative group of the global FIELD
     acting on adeles. A generic Epstein lattice (rank-2 quadratic form,
     not an order's norm form... precisely: not multiplicatively closed)
     has no such action: no linear equivalence, no Pic, no reduction.
(C2) STRONG APPROXIMATION (2022 Prop A.5 proof: "The subgroup
     p_f(Q) ⊂ A_f^Q is dense"): the computation H^1(D) = (R/L, d)_λ — the
     entire H^1 side of RR — is a global-field theorem. No field, no
     identification, no dim H^1 formula.
(C3) POLYNOMIAL/WITT PRESENTATION (2022 Remark 3.2; 2023 footnote 3): the
     optimal generating sets realizing the dimensions are the powers of
     the ring generator (3 over S[±1], -2 over S). The dimension VALUES
     would exist for any metrized group (covering numbers always exist),
     but the exact formulas — hence the exact RR — are theorems about
     Z = S[X]. This is where "Z is a polynomial ring over the absolute
     base" is load-bearing, not decorative.
(C4) THE ADELE RING ITSELF: O(D) ⊂ A_Q and ψ presuppose the restricted
     product over the places of Q — i.e. unique factorization of the ring
     Z organizing the local components. DH (Davenport-Heilbronn): no ring,
     no integral structure, no places, no adeles, no O(D), no ψ — the
     construction is NONEXISTENT, as required. Dies at the first joint.
(C5) THE SQUARE'S DIAGONAL (D2): µ : HZ ∧ HZ -> HZ is literally the
     multiplication of Z. Epstein lattices have no µ. The square theory,
     if built per sec 2, is nonexistent for Epstein at the diagonal-class
     level even if some compactified product of two metrized-lattice
     curves were formable.
(C6) THE PICARD TENSOR'S COPRODUCT (2026 Remark 8.13): ∆_n = µ_n^{-1} on
     Z/n — ring structure again, this time of the residue rings.

WHERE CC IS CARRIER-BLIND (the honest part): the duality ENGINE,
2022 Prop 5.2, is stated and proven for an ARBITRARY metric abelian group
(A,d) — norm-controlled Pontryagin duality holds for every lattice,
including Epstein's. Likewise the tolerant-module machinery (A,d)_λ and
the covering-number dimension exist for any metrized group. So: CC's PD
layer passes Epstein (exactly as K-doc sec 0 predicted for every PD layer);
what dies on Epstein is PF+PS+PR — H^0 as Q ∩ O(D) (needs the diagonal
field), linear equivalence (C1), the H^1 computation (C2), the exact
dimension formulas (C3), and the square's diagonal (C5). CONCLUSION: the
CC formalism passes the carrier filter in the same layered way the program
demands — theta/Pontryagin duality available to Epstein (necessarily so;
Epstein HAS a functional equation), everything that couples duality to
counts fatally ring-bound. The discriminating content sits exactly where
K-doc sec 0 located it: in the coupling of PD to the count layers through
the adelic diagonal Q ⊂ A_Q.

DH vs Epstein summary: DH dies at C4 (no carrier at all — correct,
trivially); Epstein dies at C1/C2/C3/C5 but NOT at the PD engine
(Prop 5.2) — the non-trivial, informative fatality. A CC-square theory
satisfying R(v) must preserve this profile.

---

## 6. Posed open questions (exceed careful reach here; stated precisely)

Q1 (cheap, witness-grade): compute π_0^T and π_1^T, in CC's tolerance
   sense, of the STRICT Γ-set smash HZ ∧ HZ (and of the two-term complex
   µ : HZ ∧ HZ -> HZ). Is the result Z concentrated in degree 0 (full
   strict collapse, M1 confirmed at the CC level), or does the non-Kan
   tolerance homotopy retain a shadow of the first Tor? This is the
   first-ever CC-side number the program can compare against Bokstedt's
   π_1 = Z/1 = 0 and π_3 = Z/2 (the first nonzero entry: does ANY Z/2
   shadow survive strictly?). Note π_1 THH(Z) = Z/1 = 0 means degrees ≤ 2
   cannot distinguish F-PASS from F-FAIL: the first bite is degree 3.
Q2 (paper-scale): define the smash of tolerant modules (M4) — candidate:
   R^{∧}_k generated by pairs differing by (R_1, diagonal) or (diagonal,
   R_2) smash factors — and prove/refute additive Kunneth for dim_S on
   ‖HZ‖_n ∧ ‖HZ‖_m (M5). Exactly computable in small cases.
Q3 (paper-scale): duality over S at curve level (M6) — does 2022 Prop 5.2
   survive with {0,1} coefficients, and what replaces U(1)_{1/4}? If no:
   that asymmetry (duality needs the involution ±1, i.e. the C_2 action)
   would connect to J-doc's C5''-infty demand that a C_2/real structure
   supplies the archimedean reflection — the quarter-shift dualizing
   module U(1)_{1/4} living only over S[µ_2] is suggestive. Observation,
   not a claim.
Q4 (the comparison theorem, fresh-context scale): construct the
   realization comparison |·| : (CC curve theory) -> (spectra) explicitly
   enough to state "CC χ = quantized π_{≤1}-shadow of a spectral Euler
   characteristic" as a theorem rather than a reading. This is the
   T-b-dissolving statement if true.

## 7. Honest limits

- I did not read CC's [3] (Gromov norm), [4] (QJM 2021), [5] (Advances
  2021) — cited as the homological substrate; M3's "no usable higher
  π_n^T" is asserted from the three archived papers only and could be
  weakened by [3]/[4] content. UNVERIFIED.
- The claim "strict smash collapses to the diagonal" (M1) is verified at
  the level of standard homotopy theory citations (doc 18's framework),
  not recomputed inside CC's tolerance category — that is exactly Q1.
- Whether CC's [5] affine theory has fiber products of Spec's: UNVERIFIED.
- No statement in this document touches zeros, the explicit formula's
  spectral side, or any RH-conditional input; the 2026 paper's sec 9 was
  inventoried for the genealogy correction (sec 1.6) only.

## 8. Sources

- connes-consani-2022-riemann-roch-specZbar.pdf (arXiv:2205.01391v2):
  Thm 1.1/4.3, Thm 1.2/5.3, (1.3), Prop 2.1, 2.2, 3.3, 4.1, 5.2,
  Lemma 3.1, 5.1, Remark 3.2, 4.2, Defs A.1, A.2, Props A.3-A.5, B.1, B.2,
  (3.4) exceptional set.
- connes-consani-2023-riemann-roch-ring-Z.pdf (arXiv:2306.00456v1):
  Thm 1.1/5.1, Lemma 2.1, Prop 2.2, Def 2.1, Lemmas 3.1-3.2, Thm 3.3,
  Prop 4.2; footnote 3 (Z = S[X], X = -2).
- connes-consani-2026-jacobian-specZbar.pdf (arXiv:2602.15941v1):
  Defs 2.3, 2.12-2.14, 3.1-3.3; Props 2.4, 2.9, 2.11, 5.1; Thms 1.1-1.4,
  2.15, 2.16, 3.4, 8.15(ref), 9.1; Remarks 2.8, 8.13; intro quotes
  (genus paradox; "decisive departure").
- Program documents: research/proof/17, 18, 21; research/work/K.
