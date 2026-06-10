# JJ - The archimedean unit, re-chartered at index grade: scoping + first construction (doc 32, THE ROAD / exit B)

Status: fresh-context worker JJ, 2026-06-10. Required reading executed in
order: doc 32 (charter), doc 31 (exit B triple spec), BB-global-assembly.md
IN FULL, GG-global-cancellation.md IN FULL, FF-kappa-on-xbar.md IN FULL,
N-cc-square-posing.md + K-global-poisson-survey.md, AA-cc-thh-probe.md
(the norm-filtered strict layer consumed by step 1(iii)); refs:
vandergeer-schoof-1998-effectivity-arakelov.pdf (h^0/effectivity formulas
read from the PDF text), connes-consani 2022/2023 PDFs (via N's
citation-grade inventory + spot checks), dgi2006.txt (Matlis-lift
formalism, secs 6-7). Inherited witnesses rerun by me before any new run:
prime_int_ff_kappa_xbar (ALL PASS, exit 0), prime_int_bb_global_assembly
(ALL PASS, exit 0), prime_cc_thh_norm_filtration (ALL PASS, exit 0).

Witness (NEW, pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_int_jj_archimedean_unit
    (gates AJ1-AJ7; readings registered in sec 1 and the docstring
    BEFORE the first run)

THE TRIPLE SPECIFICATION (doc 31 exit B, restated as the gate frame):
the archimedean unit must (BB) couple comb to continuum so kappa is
readable (comparison target kappa = pi, F-a-flagged); (GG) supply
exactly ONE continuum unit per place so the global trace exists; (FF)
carry a rational/connected Anderson-type layer (the I_Q slot) - what
torsion provably lacks (Prop FF.1). TERMINUS (doc 32): h^0 must be a
COUNT at the infinite place so effectivity fires (chi > 0 => positive
representative) and Castelnuovo runs on the monoid family. Epstein
death-point demanded in advance: at effectivity (no multiplicative
monoid => no effective cone).

DISCLOSURE (CC/GG precedent): sections 1-2 contain design-stage hand
derivations (the Anderson homotopy SES bookkeeping; the twisted-comb
density rho = prod_p rho_p with rho_2 = 2/3, rho_3 = 3/4; the
unit-ball/effectivity equivalence). They are derivations, not fits; the
witness checks them fail-closed and any mismatch is a FAIL.

## 1. PRE-REGISTERED READINGS (written before the witness ran)

### 1.1 Candidate (i): Anderson dual I_Z = fib(I_Q -> I_{Q/Z})

Recall (standard; dgi2006 sec 6 is the Matlis-side formalism): for a
spectrum X, pi_{-n} I_Q(X) = Hom_Z(pi_n X, Q), pi_{-n} I_{Q/Z}(X) =
Hom_Z(pi_n X, Q/Z), and the fiber sequence gives the natural SES

    0 -> Ext^1_Z(pi_{n-1} X, Z) -> pi_{-n} I_Z(X) -> Hom_Z(pi_n X, Z) -> 0.

So the I_Q -> I_{Q/Z} fiber sequence IS a rational-layer-plus-
torsion-shadow decomposition, computable degree-by-degree on banked
homotopy. Registered readings:

```text
AJ1 (the integral tower carries the rational layer): on
    pi_* THH(Z) (Bokstedt: pi_0 = Z, pi_{2k-1} = Z/k, k >= 1, even
    positive degrees 0):
      I_Q layer  = Q, concentrated in degree 0, rank EXACTLY 1
                   (one global rational unit - the FF slot, present);
      I_{Q/Z}    = Q/Z in degree 0 (+) Z/k in degree -(2k-1)
                   (the Pontryagin/BC torsion shadow);
      I_Z        = Z in degree 0 (+) Z/k in degree -2k
                   (torsion shifted by one, rational layer intact).
    LES of the fiber sequence exact at every banked degree (orders
    match: |Ext(Z/k,Z)| = |Hom(Z/k,Q/Z)| = k; degree 0:
    0 -> Z -> Q -> Q/Z -> 0).  FAIL: any rank/order/exactness
    mismatch, k <= 2000 exact.
AJ2 (FF's no-go reproved at Anderson grade, on the banked carriers):
    for the mod-2 tower Xbar (pi_* = F_2[[z]][t^{+-1}], bounded
    exponent 2) and THH(F_p) (= F_p[sigma]): Hom(A, Q) = 0 for every
    homotopy group (bounded exponent kills into torsion-free), so the
    I_Q layer is IDENTICALLY ZERO: Anderson-dualizing the banked
    THR/Xbar towers inserts NO rational layer - I_Z(Xbar) = the
    Matlis/BC shadow again, nothing more.  Prop FF.1's exact reason,
    now at the dualizing-object level.  AND the normalization-torsor
    clause: Aut(Z/n) has order phi(n) -> unbounded (the level-n
    automorphisms of the I_{Q/Z} layer; Aut(Q/Z) = Zhat^x), against
    Aut_top(R/Z) = {+-1} (cited theorem, FF's FFG2): even WITH its
    rational layer, plain-spectra Anderson duality leaves the
    kappa/normalization torsor unpinned - the 2pi-rigidity is carried
    only by the CONNECTED torus, which spectra do not contain.
    FAIL: any nonzero Hom(tower group, Q), or phi(n) bounded.
AJ3 (the local-global gap of the rational layer, named exactly): the
    TORSION shadow place-splits (CRT: Z/k = (+)_p Z/p^{v_p(k)},
    exact, k <= 2000) - one torsion comb per place, as GG's survivor
    layer demands.  The RATIONAL layer does NOT: it is ONE global Q
    (rank 1), not one unit per place.  The fracture-square corner
    that would localize it is (prod_p Z_p) (x) Q = A_f (the finite
    adeles: bounded denominators = almost-everywhere integral) -
    witnessed at finite level: the minimal denominator of the
    family ((1/p))_{p in S} in the corner is prod_{p in S} p,
    growing without bound = the restricted-product condition.  So in
    plain spectra the Anderson unit's per-place rational layer lives
    on the FINITE adeles only; the archimedean completion (the R
    slot, A = A_f x R) has NO fracture slot - the infinite place is
    structurally absent.  FAIL: CRT mismatch / denominator bounded.
```

EXPECTED VERDICT (i), registered: PARTIAL PASS - candidate (i)
satisfies the FF spec provably ON THE INTEGRAL TOWER (the I_Q slot
exists, rank 1, computable), reproves FF's no-go on the banked mod-p
carriers (full-value fail-closed), satisfies GG at FINITE places only
(via the A_f corner), and FAILS BB outright (torsor unpinned, no 2pi).
The missing enrichment is exactly "R as an object" = candidate (ii).

### 1.2 Candidate (ii): condensed/liquid (gated by what exists in print)

No computation possible; the gate is citation-grade. What would be
needed (stated precisely, the fail-closed deliverable): a liquid/
gaseous R-linear enrichment of the Xbar/THR towers in which (a) R and
R/Z are objects with Aut_top(R/Z) = {+-1} (the 2pi-rigidity FF located
as topological), (b) Spec Z-bar is PROPER (f_! = f_* to the base) with
a dualizing object whose archimedean stalk is the Fourier-self-dual
line (the Gaussian slot), (c) the resulting RR recovers the vdGS/CC
counts.  In print as of 2026-06: liquid R-vector theory exists
(Clausen-Scholze lectures; foundations partially unwritten per K-doc
4a); SOLID duality at the K(1)-local/etale level is theorem-grade
(Blumberg-Mandell Tate-Poitou, K-doc 4b); the archimedean coherent
properness statement for Spec Z-bar exists NOWHERE in print (K-doc
sec 5 direct sweep: no hit; Scholze's compactification talk
"explicitly speculative").  VERDICT, registered: construction-research
(multi-year), NOT this year's theorem; it is the terminus home for
(i)'s missing R-slot, not a buildable object now.

### 1.3 Candidate (iii): vdGS theta-h^0 lifted to the strict square

vdGS (read from the PDF): h^0(D) = log sum_{f in I} e^{-pi ||f||_D^2};
effectivity e(D) = exp(-pi ||1||_D^2) if O_F in I, else 0 (e(D) is
literally the f = 1 term); RR h^0(D) - h^0(kappa - D) = deg D -
(1/2) log|Delta| is Hecke's theta FE = Poisson; "we had a choice for
our effectivity function. We chose e^{-pi x^2}" (their words - the
Gaussian is IMPORTED, pinned only by Fourier self-duality on R).
N-doc M1-M6 say what blocks the CC-integer version of this on the
square (no pi_2^T, no tolerant smash, no Kunneth, base mismatch).

THE SQUARE-LEVEL CANDIDATE, DEFINABLE NOW at the strict level (AA's
banked layer): let M = (Z_{>=1}, x) be the effective monoid (free on
the primes = unique factorization), Lambda = Z[Z\0] the character
lattice with AA's archimedean filtration w([A]) = |A|.  A strict
square divisor on the diagonal monoid family is D = (a; (m_p)_p),
finitely many m_p != 0, acting on weights through BOTH faces (the MAX
face twisted by MIN-face data - the square pairing of AA N7):

    w_D([A]) = |A| e^{-a} prod_p p^{-m_p v_p(A)},

and the theta-regularized square count is

    h^0_sq(D) = log( 1 + 2 sum_{A in M} e^{-pi w_D([A])^2} ).

Registered readings (the hand derivations disclosed above):

```text
AJ4 (curve shadow + RR, the untwisted slice): for PRODUCT divisors
    (m_p acting only through N(I) = prod p^{-m_p}, i.e. w = |A| N(I)
    e^{-a}: the class [A] <-> the section f = A N(I) of O(D)),
    h^0_sq(D) = vdGS h^0 of Spec Z-bar for F = Q EXACTLY, and RR
    holds exactly: h^0(D) - h^0(-D) = deg D = a + log(1/N(I))
    (kappa = 0 for Q, |Delta| = 1; flint prec 300, tail-bounded,
    tol 1e-50; grid of (a, I) incl. I = (1/12)Z).  This is classical
    Poisson (Hecke FE), exhibited - NOT a new theorem; no zeta input.
    FAIL: mismatch beyond tail bound.
AJ5 (the genuinely square direction: v_p-coupled twists): take
    m_2 = -1 (effective-cone interior): w(A) = A 2^{+v_2(A)} e^{-a},
    image comb S = {n : v_2(n) even}, density rho_2 = 2/3 (hand:
    (1 - 1/2) sum_{v even} 2^{-v}).  Registered:
    (a) THE DUAL DIVERGES: the RR partner within the family is the
        twist m_2 = +1, and h^0 of THAT diverges (w(2^k) = 1 for all
        k: certified exact lower bound, partial sums unbounded).  So
        the strict square family has NO RR dual for any genuinely
        square (v_p-coupled) divisor: the duality demands the
        per-place renormalization - GG's continuum subtraction,
        reappearing as the EFFECTIVE CONE'S boundary.
    (b) THE DENSITY IS THE RR CONSTANT: chi_tw(a) := h^0(a, m) -
        h^0(-a, m) satisfies chi_tw(a) - a bounded, within +-0.35 of
        log rho at a in {5, 8}, NOT exactly affine (spread of the
        defect > 1e-9: no exact FE), for the three twists
        (m_2 = -1: rho = 2/3), (m_3 = -1: rho = 3/4), (both:
        rho = 1/2 - per-place densities MULTIPLY: GG's one continuum
        unit per place, count-layer face, witnessed as the
        factorization of the asymptotic RR constant).  Fine structure
        of the defect (expected log-periodic comb in a - the twisted
        lattice's own survivor comb) RECORDED, not gated.
    FAIL: (a) bounded, or (b) window/spread clause fails.
AJ6 (the terminus: effectivity fires at integer grade): the integer
    count N(D) := #{A in M : w_D([A]) <= 1} (the unit ball of the
    effective monoid; CC's pre-quantization cardinality, N-doc
    F-WEAK bypass) satisfies, for product divisors with rational
    e^a (exact Fraction arithmetic):
      N(D) >= 1  <=>  deg D >= 0  <=>  D has an effective
      representative, and the ball elements are EXACTLY the f with
      (f) + D >= 0 coordinatewise (v_p(f) + x_p >= 0 all p,
      |f| <= e^a).
    So chi(D) = deg D > 0 => positive representative: EFFECTIVITY
    FIRES, with h^0 a count and e(D) = the [1]-term.  FAIL: any
    divisor in the grid violates either equivalence.
AJ7 (EPSTEIN DEATH CERTIFICATE, at effectivity as the charter
    demands): Q(x,y) = x^2 + 5y^2 (norm form of Z[sqrt-5], class
    number 2).
      ALIVE (PD layer, necessarily): the theta count
        h^0_Eps(a) = log sum_{v in Z^2} e^{-pi Q(v) e^{-2a}} exists,
        finite (two truncations agree; Poisson FE available
        classically) - the count layer alone is carrier-blind,
        exactly as K-doc sec 0 demands of every PD-flavored layer.
      DEAD (the effective cone): the represented-norm monoid is not
        free: 2, 3 not represented; 4, 6, 9 represented and
        irreducible; 36 = 4*9 = 6*6 two distinct irreducible
        factorizations => no valuations, no place-grading of the
        cone; AND the Castelnuovo step dies: the two maximal chains
        1 | 6 | 36 and 1 | 4 | 36 have step-degree multisets
        {log 6, log 6} != {log 4, log 9} (same total = log 36: the
        product-formula shadow survives; the STEPS do not) => no
        canonical point/place subtraction => the h^0-induction of
        Castelnuovo has no monoid carrier.  Death is at EFFECTIVITY
        with the count alive - the charter's required profile.  DH:
        no carrier group at all, dies before the count (bookkeeping).
    FAIL: any membership/irreducibility/chain clause fails, or the
    Epstein count fails to converge.
```

EXPECTED VERDICT (iii), registered: the count-layer half of the unit
is DEFINABLE AND COMPUTABLE NOW; its RR is exact on the curve shadow,
asymptotic-with-density-constant on genuinely square twists (the
defect = the missing exchange, quantitatively); effectivity fires at
integer grade on the monoid family; Epstein dies at effectivity.

### 1.4 What is NOT claimed (registered in advance)

- AJ4's RR is classical Poisson; AJ5(b)'s density constants are
  elementary comb densities.  No new analytic theorem is claimed by
  the witness; the NEW content is structural (which spec each layer
  provably satisfies) and the exact location of every failure.
- kappa = pi is never derived: the Gaussian (and its pi) is vdGS's
  imported choice; sec 3.3 states exactly what would force it.
- No RH / zero-side input anywhere; the EF appears nowhere in the
  witness; G-INT6 ledger in sec 5.

## 2. THE CONSTRUCTION (the two-layer unit U, defined precisely)

    U := ( U_htpy , U_count )

    U_htpy  = I_Z(THH(Z))  with its fiber sequence
              I_Q(THH(Z)) -> I_{Q/Z}(THH(Z)),
              rational layer HQ (degree 0, rank 1),
              torsion shadow = the CRT-place-split comb {Z/k}.
    U_count = the theta-weighted effective monoid
              (M, w_D, h^0_sq, N(D)) on AA's strict character
              lattice, with the Gaussian unit e^{-pi x^2} imported
              from vdGS (F-a-flagged import).

The two layers are coupled by the SAME monoid M: the torsion shadow's
place-comb (Z/k = (+) Z/p^{v_p(k)}) and the count layer's weight
factorization (log N([A]) = sum_p v_p(A) log p, AA N7) are the two
banked readings of unique factorization.  U is the minimal object I
can build that provably satisfies ONE of the three specs (FF) and
makes the terminus (effectivity-as-count) fire on the monoid family.

## 3. VERDICT AGAINST THE TRIPLE SPEC (written after the runs)

Witness ALL PASS (AJ1-AJ7, exit 0) on the FIRST run; no gate predicate
amended at any point.  One registered EXPECTATION (not a gate) was
refuted by the recorded data and is reported in 3.2.

### 3.1 Inventory verdicts

```text
(i)  ANDERSON I_Z: PARTIAL PASS, exactly as registered.
     - FF spec SATISFIED PROVABLY on the integral tower: the I_Q
       layer of I_Z(THH(Z)) is Q, rank 1, degree 0 (AJ1, exact to
       k = 2000) - the rational/connected slot exists and the fiber
       sequence is precisely the rational-layer + torsion-shadow
       decomposition, computable degree-by-degree.
     - FF's no-go REPROVED at Anderson grade on the banked carriers:
       the mod-p towers (Xbar, THH(F_p)) have I_Q layer identically
       zero (AJ2): Anderson-dualizing the banked THR/Xbar towers
       inserts NO rational layer.  The failure is the CARRIER's
       (bounded exponent), not the duality's.  Repair = dualize a
       tower that still sees Z - which THH(Z) is.
     - GG spec: FINITE places only.  The torsion shadow place-splits
       by CRT; the rational layer does NOT - it is one global Q.
       The fracture corner that holds the per-place rational data is
       (prod_p Z_p) (x) Q = A_f (AJ3, restricted-product condition
       witnessed as unbounded minimal denominators).  The Anderson
       unit's per-place continuum data is ADELIC-FINITE; the R slot
       (A = A_f x R) has no fracture corner in plain spectra: the
       infinite place is structurally absent, not merely undetermined.
     - BB spec: FAIL.  Aut(Z/n) = phi(n) unbounded (AJ2) vs
       Aut_top(R/Z) = {+-1}: the normalization torsor survives;
       no 2pi, no kappa.  Same shape as Prop FF.1, one level up.
(ii) CONDENSED/LIQUID: construction-research, gated OUT for this
     year (sec 1.2: the needed statement named; nothing in print).
     It is where (i)'s missing R-slot must live - the terminus home.
(iii) vdGS/CC LIFTED (the count layer): WINNER for construction now.
     Definable at the strict level (sec 1.3), computed (AJ4-AJ6):
     curve shadow EXACT (defect 1.2e-88), effectivity fires at
     integer grade, square twists carry an asymptotic RR whose
     constant is the per-place comb density (3.2).
```

### 3.2 The count layer, measured (AJ4-AJ6)

- CURVE SHADOW EXACT (AJ4): on product divisors h^0_sq IS vdGS h^0
  for Q and RR holds to 1.2e-88 (classical Poisson, exhibited).
- THE SQUARE HAS NO INTERNAL RR DUAL (AJ5a): the in-family dual of
  the effective twist m_2 = -1 is m_2 = +1, whose h^0 DIVERGES
  (certified lower bound, unbounded).  Genuinely square (v_p-coupled)
  divisors have no dual divisor in the strict formalism; the duality
  demands a renormalization at the divergent fiber - GG's continuum
  subtraction, reappearing as the boundary of the effective cone.
- THE RR CONSTANT IS THE COMB DENSITY, MULTIPLICATIVE OVER PLACES
  (AJ5b): chi_tw(a) - a -> log rho with rho_2 = 2/3, rho_3 = 3/4,
  rho_23 = 1/2; measured at a = 8: -0.405205 / -0.287391 / -0.692608
  vs log rho = -0.405465 / -0.287682 / -0.693147.  The constants ADD
  across places to 4e-4 (c_23 = c_2 + c_3): GG's "one continuum unit
  per place" is realized at the count layer as one DENSITY FACTOR per
  twisted place - the genus term of the square RR is the product of
  local continuum units.
- REGISTERED EXPECTATION REFUTED (recorded honestly): the defect
  d_T(a) = chi_tw(a) - a - log rho was registered as expected
  log-periodic (a survivor-comb shadow).  MEASURED: d_T decays
  monotonically over the grid (T2: 5.8e-3 -> 2.6e-4 from a = 5 to 8,
  consistent with O(e^{-a})); any log-periodic component is below
  ~3e-4 at this resolution.  The defect behaves like a boundary term,
  not a comb - which makes the density-RR Lemma (sec 4) CLEANER than
  registered, not harder.
- EFFECTIVITY FIRES (AJ6, exact Fractions): N(D) = #(unit ball of the
  effective monoid) = floor(e^{deg D}); N(D) >= 1 <=> deg D >= 0 <=>
  an effective representative exists, and the ball elements ARE the
  effective representatives (set equality).  chi > 0 => positive
  representative: the terminus condition holds at integer grade on
  the monoid family - h^0 is a count at the infinite place.

### 3.3 The construction U against the triple spec (the honest scorecard)

```text
spec                       U's status                         grade
(FF) rational layer        SATISFIED: I_Q(THH(Z)) = Q rank 1  proven on
                           (AJ1); zero on torsion carriers    banked
                           (AJ2) - the spec discriminates     homotopy
(GG) one unit per place    HALF: finite places supplied
                           twice over (CRT torsion comb,
                           AJ3; density factors rho_p, AJ5b);
                           the ARCHIMEDEAN unit itself is
                           imported, not supplied (below)
(BB) kappa readable        FAIL AS DERIVATION: kappa = pi
                           enters only through the imported
                           Gaussian (vdGS's own flagged
                           choice); the import is FORCED iff
                           Fourier self-duality on R is
                           internal to the formalism - i.e.
                           iff candidate (ii) exists.  U
                           reads kappa; it does not derive it.
```

The triple spec is therefore CONSISTENT and ORDERED: (FF) is
satisfiable today in plain spectra; (GG) reduces to its archimedean
instance; (BB) is exactly equivalent to making R-with-Fourier internal
- one missing object, three faces, as docs 30/31 predicted, now with
the finite-place halves DONE and the gap localized to a single slot
(the R corner of the fracture square / the Gaussian unit of the count).

### 3.4 Epstein death certificate (AJ7) - the charter's advance demand

DEATH AT EFFECTIVITY, count alive, verified exactly: the Epstein theta
count exists and is finite (PD layer carrier-blind, necessarily - it
has an FE); the effective CONE does not exist: 2, 3 unrepresented;
4, 6, 9 irreducible; 36 = 4*9 = 6*6 => no valuations, AND the new
Castelnuovo-specific clause: the maximal chains 1|6|36 and 1|4|36 have
distinct step multisets {6,6} != {4,9} with equal product (the product
formula survives; the STEPS do not) => no canonical point-subtraction
=> Castelnuovo's h^0-induction has no monoid carrier.  Effectivity is
not false for Epstein - it is NOT A PROPOSITION.  DH: no carrier group,
dies before the count (bookkeeping).  The construction path has the
charter's required death profile.

## 4. SCOPING VERDICT + THE FIRST LEMMA

THEOREM-REACHABLE THIS YEAR (classical tools only):

```text
L1 (DENSITY-RR LEMMA - the precise first lemma): Let tw be a place
   twist A -> A prod_p p^{-m_p v_p(A)} with m_p <= 0 (finitely many
   nonzero), S its image comb, rho = prod_p rho_p its density
   (rho_p = (1 - 1/p) sum_{v: admissible} p^{-v}).  Then
   h^0_tw(a) - h^0_tw(-a) - a -> log rho = sum_p log rho_p,
   with O(e^{-a}) defect; and for m_p > 0 at any place, h^0 = +oo.
   Status: witnessed (AJ5); proof = Abel summation / dyadic
   decomposition on the comb, no zeta FE needed.  Value: GG's
   continuum unit becomes a THEOREM on the square's strict layer
   (genus term = product of per-place continuum units), and the
   effective cone's boundary = exactly the divergence locus.
L2 (EFFECTIVITY LEMMA): AJ6's equivalences for all product divisors
   (elementary, exact); the integer-count h^0 with chi > 0 =>
   effective representative, on the monoid family.
L3 (ANDERSON BOOKKEEPING): AJ1-AJ3 as stated for the full banked
   towers (Hom/Ext computations; the A_f corner identification is
   classical algebra).
```

CONSTRUCTION-RESEARCH (not theorem-reachable this year): the
archimedean slot itself - the single missing object now has a sharp
triple description: (homotopy face) an R-corner for the arithmetic
fracture square; (count face) an internal derivation of the Gaussian
unit (Fourier self-duality as a property of the formalism, not an
import); (symmetry face) Aut_top(R/Z) = {+-1} rigidity pinning the
torsor.  All three are the same demand: candidate (ii), the
condensed/liquid enrichment.  Per doc 31's guard this whole road,
completed, yields the SYMMETRY layer - the index/positivity demand on
the square (doc 21 sec 4) is untouched by anything here.

FAILURE-MODE WATCH (doc 32): nothing in L1-L3 consumes zero-repulsion
or any zero-side input; the effectivity delivered is on the MONOID
family (product divisors + v_p-twists), not yet on Frobenius-graph
classes - whether THAT effectivity costs zero-repulsion is exactly
probe 1's defect question, untouched here.

## 5. G-INT6 LEDGER

```text
input                          choices spent
Anderson Hom/Ext bookkeeping   0 (standard SES; dgi2006 formalism;
                               exact computations)
Aut_top(R/Z) = {+-1}           cited theorem (FF's FFG2 precedent)
banked towers                  0 new (Bokstedt, S.1/EE, doc 24/25)
Gaussian e^{-pi x^2}           IMPORTED, F-a-flagged (vdGS's own
                               flagged choice); never used to derive
                               kappa; sec 3.3 names what would force it
twist family m_p = -1          calibration choice of the cheapest
                               square direction (v_p-coupled); the
                               density formulas are hand derivations
                               DISCLOSED at registration, witnessed
AJ5b windows (+-0.35, 1.2)     tolerance choices for an asymptotic
                               statement (loose, discriminating
                               between the three rho values)
Epstein clauses                0 (exact integer enumeration)
```

No fits anywhere; AJ1-AJ4, AJ6-AJ7 are exact or 1e-50-grade; AJ5b is
the only loose-tolerance gate and its reading (density constants,
additivity across places) is confirmed at 4e-4 against hand values.

## 6. HONEST LIMITS

- AJ1-AJ3 are pi_*-level order/rank computations on banked homotopy
  with truncations (k <= 2000); the spectrum-level Anderson
  statements (e.g. I_Z(THH(Z)) as a cyclotomic object, real/THR
  variants) are NOT touched; "computable on banked homotopy" is
  exactly what was computed, no more.
- The square count h^0_sq lives on the STRICT layer (AA's character
  lattice): degrees are still missing (V's verdict stands); nothing
  here produces H^1/H^2 or a square Euler form (N-doc M1-M6 remain
  the blockers for the CC-integer version).
- L1 is stated as witnessed + classically provable; the proof is NOT
  written here.  The O(e^{-a}) rate is measured, not proved.
- The "one unit per place" delivered at the count layer (density
  factors) is per TWISTED place; the untwisted places contribute
  rho_p = 1 - consistency, not content.
- kappa = pi appears only inside the imported Gaussian; no derivation
  is claimed (the import is the named gap, not a result).
- No RH / zero-side input anywhere; the EF appears nowhere.

## 7. HAND-OFF (for the lead)

```text
INVENTORY: (i) Anderson PARTIAL PASS (FF satisfied on THH(Z), exact;
           torsion carriers fail it - FF.1 reproved at Anderson
           grade; per-place rational layer = A_f corner, R-slot
           absent); (ii) condensed/liquid = construction-research,
           statement named, nothing in print; (iii) theta-on-strict-
           square = DEFINABLE NOW, computed, winner.
CONSTRUCTION: U = (I_Z(THH(Z)), theta-monoid-count): satisfies FF
           provably; GG at finite places (twice: CRT comb + density
           factors, multiplicative to 4e-4); BB only by Gaussian
           import.  The three specs collapse to ONE missing slot:
           internal R with Fourier (= the liquid demand).
TERMINUS:  effectivity FIRES at integer grade on the monoid family
           (N(D) = floor(e^deg), ball = effective reps, exact);
           square twists have NO internal RR dual (dual diverges) -
           the renormalized RR constant is the per-place density.
EPSTEIN:   death certificate issued at effectivity (count alive,
           cone nonexistent, Castelnuovo step carrier-free), exact.
FIRST LEMMA: L1 (density-RR): chi_tw(a) - a -> sum_p log rho_p with
           the divergence locus = the effective cone boundary;
           provable classically this year; makes GG's continuum
           unit a theorem on the square's strict layer.
WITNESS:   prime_int_jj_archimedean_unit.py (AJ1-AJ7, ALL PASS,
           exit 0, first run, no gate amended; one registered
           non-gate expectation - log-periodic defect - refuted by
           the recorded data: the defect decays).
```

