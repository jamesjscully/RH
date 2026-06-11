# MM - The liquid slot: internal R with Fourier, scoped (doc 33 sec 3 item 3, the long road)

Status: fresh-context worker MM, 2026-06-10. SCOPING ONLY - no
construction, no witnesses, no numerical claims. Required reading
executed in order: doc 33; JJ-archimedean-unit.md IN FULL (the
inventory and the named needed statement, sec 1.2/3.3/4); FF-kappa-on-
xbar.md IN FULL (Prop FF.1; FFG2 Aut(R/Z) = {+-1} rigidity; sec 1.4
sharpened target); HH-weil-restriction-fork.md IN FULL (the coupling
as joint cancellation, sec 3(vi)); K-global-poisson-survey.md IN FULL
(the condensed landscape baseline, secs 4-5); BB/GG via their
hand-off sections + grep-verified clauses (BB's kappa-rescaling
no-go and BB-r2 one-place scale-freeness; GG's one-continuum-unit-
per-place subtraction); doc 28 (the spec format being imitated);
doc 21 sec 3 (G-INT6).

Literature pass: primary-source grade where marked; every PDF cited
as archived was fetched THIS SESSION and grepped/read directly;
everything else is marked UNVERIFIED or abstract-grade honestly.
New refs archived under research/proof/refs/:

```text
scholze-clausen-analytic-geometry-lectures.pdf   (Scholze, Lectures on
    Analytic Geometry, Bonn 2019-20; the liquid theorem)
clausen-scholze-2022-condensed-complex-geometry.pdf (Clausen-Scholze,
    Condensed Mathematics and Complex Geometry; stable citable
    version - liquid Serre duality + HRR)
efimov-2024-k-theory-localizing-invariants-large-categories.pdf
    (arXiv:2405.12169; continuous localizing invariants)
efimov-2025-rigidity-localizing-motives.pdf (arXiv:2510.17010)
scholze-real-local-langlands-draft.pdf (gaseous R in use; DRAFT,
    "used for ARGOS seminar" - not a stable citation)
anschutz-lebras-2021-fourier-banach-colmez.pdf (arXiv:2111.11116;
    the p-adic Fourier-self-duality precedent)
```

## 1. THE DEMAND, CONSOLIDATED (the LS specification)

One missing object, three faces (JJ sec 3.3): (FF) a dualizing
object with a connected/rational layer; (GG) the archimedean
instance of one-continuum-unit-per-place; (BB) kappa readable =
Fourier self-duality internal. HH adds the binding constraint: the
unit must COUPLE (the Weil margin is a joint cancellation - any
add-on PD block is structurally wrong). Doc 28's PFD spec posed the
compactified object at determinant level; this spec poses its
CATEGORY-level prerequisite. Following doc 28's format:

A liquid slot is a symmetric monoidal (∞-)category L (presentable
stable, with a t-structure or count layer where stated) equipped
with the following, ALL as structure subject to the G-INT6 clause
LS6:

```text
LS1 (the bank embeds): a symmetric monoidal functor b from the
    program's banked carriers into L - the integral tower THH(Z)
    with its Anderson fiber sequence I_Q -> I_{Q/Z} (JJ AJ1: rational
    layer Q rank 1, CRT-place-split torsion comb), the mod-p towers
    (Xbar = F_2[[z]][t^{+-1}], THH(F_p)), and the strict count layer
    (M = (Z_{>=1}, x), AA's character lattice with w([A]) = |A|).
    b must be conservative on the banked homotopy/count data: no
    banked identity may be destroyed or rescaled.
LS2 (internal R, rigid): objects R and T = R/Z in L (not just their
    torsion shadows), such that
    (i)  Aut_L(T) = {+-1}  - the 2pi-rigidity is carried INSIDE L
         (FF FFG2: this is a topological datum with no torsion
         shadow; in L it must be a theorem about the object T);
    (ii) the arithmetic fracture square of LS1's rational layer
         acquires its missing corner: the banked corner is
         (prod_p Z_p) (x) Q = A_f (JJ AJ3); L must contain the
         completion A = A_f x R with R supplied by (the underlying
         additive group of) the object R - the infinite place
         becomes structurally PRESENT, killing Prop FF.1's premise
         by design (FF sec 4 names this exact escape clause).
LS3 (Fourier self-duality with Gaussian fixed unit): an internal
    duality F: Mod_R(L) -> Mod_R(L) (kernel = a character pairing
    R x R -> T) with
    (i)   F o F = (-1)^* (Fourier inversion internal to L);
    (ii)  the normalization torsor of F is PINNED by LS2(i): the
          only residual freedom is {+-1} (against FF FFG3's
          2^{(N+1)/2}-torsors and JJ AJ2's phi(n)-torsor - the
          discriminating clause);
    (iii) the fixed unit of F on the Schwartz-type object is the
          Gaussian: F(g) = g with g unique up to the {+-1} of (ii)
          - so e^{-pi x^2} (and with it kappa = pi) comes OUT as
          the fixed-point datum, never inserted (vdGS's "we chose
          e^{-pi x^2}" becomes a theorem of L; JJ sec 3.3's
          "forced iff Fourier self-duality is internal").
LS4 (the trace coupling - the measurement): a trace functional
    tr_L on dualizable objects of L such that for each place p the
    lattice exact sequence 0 -> (log p)Z -> R -> T_p -> 0 (T_p the
    circle of circumference log p) induces the comb <-> continuum
    exchange: tr_L of the banked comb b(comb_p) against R equals
    the continuum side with ONE unit per place subtracted (GG's
    zero-mode subtraction as the trace's regularization), and the
    GLOBAL assembly over all places + the product formula makes
    BB's gate observable c_oo = -(1/2) log kappa a function of L's
    data with value -(1/2) log pi (kappa = pi OUT, not compared).
    COUPLING CLAUSE (HH 3(vi), mandatory): in the certified
    Lorentzian coordinates the supplied archimedean coordinate must
    pair against the spacelike lattice image (joint cancellation),
    i.e. tr_L restricted to the banked face reproduces Theorem
    HH.1's Gram - the unit is a measurement on the SAME form, not
    a positive block added beside it.
LS5 (RR/count compatibility): L's internal duality + trace recover
    the count layer: on product divisors the vdGS theta-count
    h^0(D) (JJ AJ4 curve shadow, exact) and on genuinely square
    (v_p-coupled) twists a FINITE renormalized dual where the
    strict family certifiably diverges (JJ AJ5a) - i.e. LS4's
    per-place subtraction is exactly the renormalization that
    makes K_sq posable (doc 33 sec 2's index inequality).
LS6 (G-INT6 / kill-tests, doc 28 K5-K6 transposed):
    (i)  ZERO free gluing choices: the only inputs are the product
         formula, the banked residue pairings, and the cited
         rigidity theorem Aut_top(R/Z) = {+-1}; any inserted scale,
         scheme, or Gaussian demotes L to calibration;
    (ii) Epstein/carrier guard AT THE LIQUID LEVEL (sec 4.3 below):
         for a lattice without multiplicativity the LS4 coupling
         must be UNDEFINABLE (no carrier), with the PD/theta layer
         alive - death at effectivity, matching JJ AJ7's profile;
         DH: no carrier group, dies at LS1;
    (iii) F-a guard: no clause may consume zeta's analytic
         continuation or any zero-side input; the EF appears only
         as comparison (doc 14).
```

Existence/consistency of (L, b, R, F, tr_L) is the mathematics.
LS1-LS2 are category-construction demands; LS3 is the structural
Gaussian; LS4 is the program-facing measurement; LS5 ties it to the
index attack (doc 33's terminus); LS6 is what keeps it honest.

## 2. THE LITERATURE MAP (primary-source grade; per clause)

### 2(a) Liquid/gaseous R-vector spaces - what is in print

- LIQUID FOUNDATIONS: IN PRINT, theorem-grade. Scholze, "Lectures
  on Analytic Geometry" (archived; grepped in full). Theorem 6.5
  (quoted exactly): for 0 < p <= 1, the p-liquid condensed R-vector
  spaces Liq_p(R) form an abelian subcategory, generated by compact
  projectives M_{<p}(S), with left adjoint liquidification and a
  unique symmetric monoidal tensor ⊗_p^liq; Theorem 6.6 is the hard
  kernel statement (the Lean-verified "liquid tensor experiment"
  theorem). So LS2's R exists as an analytic ring with a
  well-behaved Mod_R(L). VERIFIED ABSENCE: the full text of
  Analytic.pdf contains ZERO occurrences of Fourier, Poisson,
  theta, or Gaussian (grep over the extracted text, this session).
  The liquid theory in print has NO Fourier theory.
- GASEOUS R (the variant actually used now): video + draft grade
  only. The Analytic Stacks course (Clausen-Scholze 2023-24; course
  page lists only topics: light condensed abelian groups, analytic
  rings, analytic stacks, examples; NO written notes released as of
  2026-06). In-use citation: Scholze, "Geometrization of the real
  local Langlands correspondence" (archived DRAFT, "used for ARGOS
  seminar"): gaseous R- and C-algebras are defined and used in
  anger (Ch. III: gaseous distribution algebras on real groups;
  Ch. V.2: bounded subsets/Nil^dagger for gaseous R-algebras,
  "direct adaptations from the solid to the gaseous case").
  Camargo, "Notes on Solid Geometry" (arXiv:2603.03012, abstract/
  intro grade): confirms liquid R is constructed in [CS20] and
  treats the solid alternative. STATUS: the gaseous foundations the
  route would build on are USED but UNWRITTEN as stable citations -
  a real dependency risk, unchanged from K-doc 4(a).
- THE NEAREST INTERNAL-DUALITY THEOREMS WITH LIQUID COEFFICIENTS:
  Clausen-Scholze, "Condensed Mathematics and Complex Geometry"
  (archived; stable citable version). Theorem 13.6 (Serre duality
  for d-smooth maps of generalized complex analytic spaces, liquid
  coefficients), Theorem 13.10 (GAGA), Lectures XIV-XV
  (Hirzebruch-Riemann-Roch, chi(X,V) = integral of ch(V)Td(T_X) in
  HODGE cohomology). Load-bearing for the spec: internal duality +
  RR over liquid R IS theorem-shaped and in print - but for proper
  COMPLEX MANIFOLDS, not for Spec Z-bar. Note for LS3/LS6: their
  HRR is deliberately normalized in Hodge cohomology (c_1 = dlog),
  so no 2pi-type constant appears anywhere - the in-print liquid
  duality is CONSTANT-FREE; nothing in it derives kappa. The
  archimedean-proper-Spec-Z-bar statement remains NOWHERE in print
  (K-doc sec 4a verdict re-confirmed by this session's direct
  sweep; Scholze's compactification talk still the only trace,
  explicitly speculative).
- LIQUID/CONDENSED POISSON SUMMATION, "analytic stacks Tate's
  thesis": NO HIT (searched: condensed + Poisson summation,
  analytic stacks + Tate's thesis, liquid Fourier, 6-functor +
  adeles + Poisson). The phrase the program needs still does not
  exist in the literature - K-doc sec 5's negative finding stands
  as of 2026-06, now checked against the 2024-26 wave.

### 2(b) Clausen's "Fourier transform via condensed/solid"

DOES NOT EXIST in print. Clausen's IHES page (fetched this session)
lists no such paper or course; targeted searches return nothing.
What exists instead, and is genuinely toward LS3/LS4:

- Clausen, "A K-theoretic approach to Artin maps" (arXiv:1703.07842,
  abstract fetched; + MIT thesis 2013): the K-theoretic Tate
  thesis - functorial Artin map from K(LCA_F), with the product
  formula arising the way Tate derived it from Haar measure. This
  is the DEG-0 SHADOW of LS4 (K-doc 4c's reading confirmed): a
  trace-level coupling of arithmetic to locally compact topology,
  K-theoretically. No Fourier transform, no Gaussian, no kappa.
- THE p-ADIC PRECEDENT (the shape proof-of-concept): Anschutz-Le
  Bras, "A Fourier Transform for Banach-Colmez spaces"
  (arXiv:2111.11116, archived): an l-adic Fourier transform for
  relative Banach-Colmez spaces over perfectoid bases - a Fourier
  self-duality made internal to a Clausen-Scholze-style analytic
  category. Wrong place (p-adic/perfectoid, l-adic kernel), right
  SHAPE: it demonstrates the formalism can carry an internal
  Fourier duality when the geometry supplies the character object.
  The archimedean analogue (kernel e^{ixt} on gaseous R, fixed
  unit = Gaussian) is exactly LS3 and is UNWRITTEN.
```text
UNVERIFIED: any non-public or in-preparation Clausen work on a
condensed/gaseous Fourier transform. Marked honestly: rumors of
"Fourier via condensed" could not be sourced to any document,
talk page, or arXiv entry as of 2026-06-10.
```

### 2(c) Efimov/dualizable-category trace theory - and the scale-blindness no-go

- Efimov, "K-theory and localizing invariants of large categories"
  (arXiv:2405.12169, archived; read at theorem level). Theorem 0.2:
  for X locally compact Hausdorff and C dualizable,
  F^cont(Shv(X;C)) = Gamma_c(X, F^cont(C)) for any finitary
  localizing invariant F. Proposition 4.18: U^cont_loc(Shv(R;C)) =
  Omega U^cont_loc(C). Theorem 6.1: for X a finite CW complex,
  F^cont(Shv(X;C)) = F^cont(C)^X - depends ONLY on the homotopy
  type of X.
- CONSEQUENCE FOR THE TASK'S QUESTION (does the continuous trace of
  the liquid circle produce 2pi-type constants?): for the
  SHEAF-THEORETIC circle the answer is NO, BY THEOREM. Shv(R/(log
  p)Z; C) sees only the homotopy type S^1; by Theorem 6.1 every
  continuous localizing invariant of it equals F^cont(C)^{S^1},
  independent of the circumference log p, of any metric, and a
  fortiori of any 2pi. Localizing-invariant traces are SCALE-BLIND.
  This is Prop FF.1's pattern one level up - the invariants are
  built from colimits/limits of the same scale-free data - and it
  is now citable as theorem, not analogy. The kappa carrier cannot
  be the topological circle in Shv; it must be the METRIZED object
  (the liquid/gaseous R-algebra of functions on T_p), where Efimov
  theory does not currently compute anything (see 2d).
- Efimov, "Rigidity of the category of localizing motives"
  (arXiv:2510.17010, archived). Theorem 0.1: Mot^loc is rigid
  symmetric monoidal; corepresentability of TR, TC on connective
  rings; refined HC^-/HP. This is the trace FORMALISM the route
  would want (traces of dualizable objects in a rigid category =
  the right home for LS4's tr_L) - but it is Sp-linear; no R, no
  liquid base change in print. Efimov, "Localizing invariants of
  inverse limits" (arXiv:2502.04123, abstract grade): K-theory of
  Nuc(Spf R) = classical continuous K-theory, resolving a
  Clausen-Scholze conjecture - the nuclear/trace-class machinery is
  maturing fast on the FORMAL/non-archimedean side.

### 2(d) THH/K-theory with liquid coefficients

NO HIT - nothing in print computes THH or K of a liquid/gaseous
analytic ring over R, or with liquid coefficient categories.
Nearest existing, for calibration of distance:

```text
- Cordova Fedeli, PhD thesis (Copenhagen 2023): THH of adic rings
  in the CONDENSED/SOLID setting (non-archimedean only).
- Efimov 2502.04123 (above): K/localizing invariants of nuclear
  modules on formal schemes (non-archimedean only).
- Blumberg-Mandell Tate-Poitou (K-doc 4b, archived earlier):
  K(1)-local Anderson self-duality - etale side, special values.
- Zhang, "A remark on Continuous K-theory and Fourier-Sato
  transform" (arXiv:2506.02329, PAMS to appear; abstract grade):
  Fourier-SATO (microlocal, conic - no metric, no Gaussian) used
  to recompute Efimov-type invariants. Closest phrase-match to
  "Fourier + continuous K-theory" in print; not LS3's Fourier.
- UNVERIFIED: any computation of THH(Liq_p(R)) or
  THH(R_gas / S_gas); no preprint, talk abstract, or thesis found.
```

The blunt summary per clause: LS2 exists (liquid theorem-grade,
gaseous draft-grade); LS3 exists only as a p-adic cousin; LS4's
formalism half exists (rigidity/trace theory over Sp) but its
R-linear instance does not; LS5's curve-level model exists OUTSIDE
the liquid world (CC over S[+-1], vdGS classically) and its liquid
counterpart exists only for complex manifolds; nothing computes
(d). Every "exists" above is load-bearing-cited; every gap is the
program's to build.

## 3. THE MINIMAL FIRST OBJECT (cheapest computation that tests the route)

THE LIQUID CIRCLE TRACE. Object: T_p = R/(log p)Z. Classical
shadow: BB-r2's banked one-place Poisson identity (comb atom weight
= spacing = 2pi/log p, Abel-regularized). The test: compute the
internal trace of T_p in a liquid/gaseous category and measure it
against the banked comb b(comb_p).

Two routes, by cost:

```text
ROUTE A (complex shadow, ALL INPUTS IN PRINT): replace T_p by the
  Tate curve X_p = C^x / p^Z (a compact complex manifold; |.| maps
  it onto T_p). In D(Liq(C)) (Complex.pdf): compute RGamma(X_p, O)
  and the Serre-duality trace H^1(X_p, Omega^1) -> C (Theorem
  13.6), and HRR chi(X_p, L_d) = d (Lectures XIV-XV). Couple to
  the bank through the q-expansion: the p^Z-grading of sections IS
  the banked p-tower (the monoid address of JJ/AA). MEASUREMENT:
  does the liquid trace, transported through the q-grading,
  reproduce the banked comb with any normalization BEYOND
  weight/spacing = 1? PRE-REGISTERED expected reading (from BB-r2,
  stated in advance as the honest null): NO - a one-place
  observable is scale-free; Route A is a CONSISTENCY/calibration
  computation, valuable because every input is theorem-grade.
ROUTE B (the real test - two places + product formula): assemble
  TWO circles T_p, T_q in one gaseous category with the banked
  product formula as the only gluing (LS6(i)), and compute the
  ASSEMBLED trace against b(comb_p (x) comb_q). This is the first
  place kappa CAN appear (BB: extraction requires comparing comb
  mass against a continuum density across places). Inputs needed:
    (i)   gaseous R and O(T_p) as algebra objects - EXISTS at
          draft grade (RealLL Ch. III machinery: overconvergent
          functions/distributions on compact real groups);
    (ii)  proper pushforward + finiteness for T_p -> pt with
          gaseous coefficients - UNWRITTEN for the real circle
          (the complex-manifold analogue is Theorem 12.18/13.6);
    (iii) a self-duality of the pair ((log p)Z, R) internal to the
          category - LS3, UNWRITTEN (the p-adic cousin is
          Anschutz-Le Bras);
    (iv)  the banked comb + product formula - EXISTS (witnessed).
  So Route B is blocked by exactly (ii)+(iii) = the spec's LS3/LS4
  - which is the correct shape for a first object: it isolates the
  two unwritten clauses and nothing else.
KILL-TEST AT THE FIRST OBJECT (mandatory before any banking): run
  Route A/B with the multiplicative lattice p^Z replaced by an
  Epstein-shaped lattice (rank-2 norm form, JJ AJ7's Q(x,y) =
  x^2 + 5y^2). The trace and theta/PD layer MUST survive (Poisson
  is lattice-blind - K-doc sec 0); the q-expansion/monoid grading
  used for the coupling MUST have no carrier (36 = 4*9 = 6*6: no
  valuations, no tower address). PASS = the coupling is
  undefinable for Epstein while the count is alive (death at
  effectivity, JJ AJ7's exact profile). If the constructed
  coupling computes for Epstein anyway, the route is PD-grade
  vacuous (doc 21 sec 4) and dies.
```

## 4. FEASIBILITY VERDICT

### 4.1 Theorem-reachable segments (classical-tools-or-in-print grade, ~this year)

```text
T1 (SCALE-BLINDNESS NO-GO, provable now): formalize sec 2(c) as a
   lemma - no finitary localizing invariant of Shv(T_p; C) can
   depend on log p (Efimov Thm 6.1/0.2); hence no kappa from
   sheaf-theoretic traces; the carrier must be the metrized/
   analytic-ring object. A small, citable negative theorem that
   channels all future work to the right door (and retires the
   cheap version of the route in advance).
T2 (ROUTE A, the complex-shadow calibration): Tate-curve liquid
   RR/Serre trace vs the banked one-place comb; all inputs in
   print (Complex.pdf Thm 13.6, Lectures XIV-XV) + banked
   witnesses; expected reading scale-free (registered above).
T3 (LS2 BOOKKEEPING): the fracture-square statement - R as
   condensed object completing JJ AJ3's A_f corner at module
   level; light-condensed foundations suffice; this is exact
   algebra over in-print material (Analytic.pdf Lectures I-IV).
```

### 4.2 Research-program segments (multi-year; unwritten foundations)

```text
R1 (LS3): internal archimedean Fourier self-duality with Gaussian
   fixed unit on gaseous/liquid R - no print precedent on R (only
   the p-adic cousin); depends on gaseous foundations whose stable
   write-up does not exist (Analytic Stacks notes unreleased;
   RealLL is a draft). This is the spine.
R2 (proper Spec Z-bar as analytic stack with dualizing object
   whose archimedean stalk is the Fourier-self-dual line):
   explicitly speculative in the field's own words; nothing in
   print; strictly downstream of R1.
R3 (LS4 global): the two-place-then-all-places assembled trace
   with kappa = pi OUT; needs R1 + a liquid-linear Efimov-type
   trace theory (base-changing arXiv:2510.17010 from Sp to a
   gaseous base - no such theory exists).
```

HONEST TIMELINE SHAPE: T1-T3 are bankable within the year and are
genuinely useful (T1 closes a wrong door permanently; T2 puts the
first liquid number against a banked witness; T3 makes Prop FF.1's
escape clause concrete). The spine R1-R3 is a foundations-dependent
research program - multi-year at best, with a hard EXTERNAL
dependency (gaseous foundations write-up) the program does not
control. JJ sec 1.2's registered verdict ("construction-research,
NOT this year's theorem") is CONFIRMED by this deeper sweep, now
with the additions that (i) the in-print liquid world has internal
duality + RR but provably no Fourier/Poisson statement of any kind,
and (ii) the trace-theory shortcut is closed by theorem (T1), so
there is no cheap version: the route costs R1, exactly as specced.

### 4.3 The kill-test the route must pass FIRST (gate, pre-registered here)

The Epstein/carrier guard at the liquid level (LS6(ii), sec 3's
kill-test): WHAT DIES FOR A LATTICE WITHOUT MULTIPLICATIVITY. The
liquid/gaseous formalism is lattice-blind by design (any cocompact
lattice in R^n has a circle/torus, a theta, a Poisson identity -
the PD layer survives, and MUST survive, or the formalism is
broken). The discriminating clause is LS4's coupling THROUGH THE
BANK: the comb object b(comb_p) carries the monoid/valuation
address (unique factorization), and Epstein's represented-norm
monoid has none (JJ AJ7: 36 = 4*9 = 6*6, chains with distinct step
multisets). REQUIRED death profile: coupling undefinable (not
false), count alive, at effectivity - same joint as AJ7. This gate
must be run on the FIRST constructed instance of LS4 (Route B, or
any partial), before any banking; a coupling that computes for
Epstein is vacuous and kills the route regardless of how much of
R1-R3 has been built.

## 5. G-INT6 LEDGER (for this scoping doc)

```text
input                          choices spent
LS1-LS6 spec                   0 new demands invented: every clause
                               is sourced (LS2i=FF FFG2; LS2ii=JJ
                               AJ3; LS3iii=JJ 3.3/vdGS; LS4=BB+GG
                               +HH 3(vi); LS5=JJ AJ4-AJ5; LS6=doc
                               28 K5/K6 + doc 14)
kappa = pi                     comparison target ONLY (LS4 states
                               it as required OUTPUT; F-a-flagged)
literature claims              each pinned to an archived PDF with
                               theorem numbers, or marked
                               UNVERIFIED/abstract-grade in place
no witnesses                   scoping only; the one pre-registered
                               reading (Route A scale-free) is a
                               null expectation, not a gate
```

## 6. HONEST LIMITS

- This is a map, not a construction: no object of L is built; the
  spec's consistency is NOT established (in particular whether
  LS3(ii)'s torsor-pinning and LS4's coupling clause can coexist
  is open mathematics).
- Negative literature findings ("no hit") are bounded by search
  reach: arXiv + the principals' pages + targeted sweeps, 2026-06;
  unreleased lecture notes or in-preparation work could overturn
  2(b)/2(d) - flagged UNVERIFIED where relevant.
- The gaseous citations (RealLL, Analytic Stacks course) are
  draft/video grade; any T-segment that touches gaseous (rather
  than liquid) material inherits that instability.
- Theorem 6.1/0.2 scale-blindness (T1) is cited, not yet written
  out as the program-facing lemma; writing it is part of T1.
- Nothing here touches the index/positivity demand (doc 21 sec 4):
  a completed liquid slot supplies the SYMMETRY layer (doc 31's
  guard, restated by JJ sec 4) - the square's index inequality
  remains a separate, untouched burden.
- No RH / zero-side input anywhere; the EF appears only as the
  comparison frame of LS4's output clause.

## 7. HAND-OFF (for the lead)

```text
SPEC:     LS1-LS6 (sec 1) - the consolidated single statement of
          the liquid demand, doc-28 format, all clauses sourced.
LIT:      LS2 liquid R = in print (Analytic.pdf Thm 6.5/6.6,
          archived); gaseous = draft grade; liquid Serre duality +
          HRR in print for complex manifolds (Complex.pdf Thm
          13.6, XIV-XV) with NO Fourier/Poisson anywhere in the
          liquid corpus (verified absence); Clausen condensed
          Fourier = does not exist; p-adic precedent =
          Anschutz-Le Bras (archived); Efimov trace theory =
          scale-blind by Thm 6.1/0.2 (the kappa cannot come from
          Shv); THH/K with liquid coefficients = no hit.
FIRST:    the liquid circle trace (sec 3): Route A computable now
          (all inputs in print, expected scale-free null); Route B
          blocked by exactly LS3+LS4 - the correct isolation.
VERDICT:  T1-T3 theorem-reachable this year (incl. the
          scale-blindness no-go, a permanent door-closer); R1-R3
          the multi-year spine with an external foundations
          dependency; kill-test = Epstein at the first LS4
          instance, death-at-effectivity profile mandatory.
REFS:     6 new PDFs archived (header list).
```
