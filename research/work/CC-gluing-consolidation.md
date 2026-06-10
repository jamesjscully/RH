# CC - Gluing consolidation (PFD doc 29 fronts 2+3): odd-p instances of Z's recipe, K3 and K4 on G

Status: fresh-context worker CC, 2026-06-10. Required reading executed in
order: doc 28 (K3, K4), doc 29, Z-u2-gluing.md IN FULL, docs 24/25 (odd-p
fold F_p[y], |y| = 4; p = 2 Barnes Gamma_2 tower), Q-cc-ftest.md (the
quantization-defect pole), S-thr-p2.md IN FULL (the Tate square + maps).
Inherited witnesses rerun by me BEFORE any new work:
prime_int_z_u2_glue.py ALL PASS (ZG1-ZG8, exit 0),
prime_int_thr_p2_anomaly.py ALL PASS (exit 0).

New witnesses (all pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_int_gc_oddp_glue
    python3 -m scripts.numerics.witness.prime_int_gc_k3_barnes_rank
    python3 -m scripts.numerics.witness.prime_int_gc_k4_integer_layer

Sections 1-2 (registrations + constructions) were written BEFORE the
witnesses were first run; verdict sections after. DISCLOSURE: the
registrations below contain exact closed forms (the recentred Barnes
polynomial, the cone defect series, the -13/24 finite part) that I
derived BY HAND at design time, before writing any code. They are
design-stage derivations, not fits; the witnesses check them and any
mismatch is a FAIL of the registration.

## 1. PRE-REGISTERED READINGS (before any run)

### Part 1 - odd-p instances of Z's gluing recipe

```text
C1 (registered expected): the gluing goes through at odd p - the
   mechanism is NOT 2-specific. Precisely: (i) D'_p is FORCED (the
   graded/Matlis dual of the fixed-point tower is the divided-power
   algebra Gamma_{F_p}[y'] = F_p[gamma_{p^k}]/(gamma_{p^k}^p), zero
   choices: Lucas at p, unit coefficients on the digit presentation,
   additive coproduct forced by weight grading + counit); (ii) the
   K2-analogue tower identity holds (level-N socle pairing = the one
   G_p-pairing through the colimit insertions iota_N(y^m) =
   gamma_{N-m}; Gram = permutation, weight flip m <-> -m); (iii)
   c = 1/2 is forced on the glued ladder (negation-ratio constancy
   iff c = 1/2, A1 slope = 1/2 exactly, q = p); (iv) glued trace = 0
   and glued anomaly = 0 exactly (x = p^{-2s}; a = s/2), with the
   nonzero (1-s)/2 fold anomaly living ONLY on the unglued half.
C2 (fail): a named step fails - then the p = 2 Euler tower / Lin line
   was load-bearing for the MECHANISM and the PFD spec needs amending;
   report the step.
STRUCTURAL DELTAS, registered in advance as EXPECTED ABSENCES (these
   are not C2 failures; they are what "simpler" means at odd p):
   (d1) no Lin LINE: the Tate vanishes (QS), there is no t; the gluing
        locus is the single weight-0 slot F_p . 1 = F_p . gamma_0 (a
        point, not a Laurent line);
   (d2) duality degree shift = 0 (pairs deg 4m with -4m), vs the
        forced Sigma-shift 1 at p = 2 (Greenlees-May has nothing to
        shadow when the Tate is 0);
   (d3) hence NO N2-type forcing at odd p: the ZG8 mechanism (odd
        shift kills the v-lattice) is 2-SPECIFIC; nothing replaces it;
   (d4) no shear datum: U's Weyl shear lived on the p = 2 Tate disk;
        at odd p the C_2 is already quotiented and the Tate is 0;
   (d5) no Euler tower: F_p[y] is the WHOLE fixed-point carrier
        (DMPR Cor 5.19) - the rank-2/Barnes sector is 2-specific;
   (d6) no functorial completion: at p = 2 the Tate functor supplied
        F_2[[z]]; at odd p only the y-adic truncation tower is
        canonical (intrinsic weight filtration, res(y) = x^2, wt 2).
        The gluing consumes ONLY the tower + Matlis colimit - every
        gate is finite-level - so no completion choice is spent.
FAIL criteria per gate are in the witness docstring (OG1-OG6).
```

### Part 2 - K3 on G (p = 2): the Barnes Gamma_2 rank sector

```text
K3-pass (registered expected), in three clauses:
   (i)  SEEN: the gluing sees the Euler tower via the fix -> Tate map
        of S's square (xbar -> x = t^{-2} z, y -> tx = t^{-1} z): the
        monomial map Psi(xbar^i y^k) = t^{-(2i+k)} z^{i+k} is
        INJECTIVE with image the CONE {(j, m): m <= j <= 2m} inside
        G's D-branch (inverse i = j - m, k = 2m - j). The rank part
        of G is this cone: degreewise multiplicity floor(j/2) + 1 =
        the Barnes count [q^j] 1/((1-q)(1-q^2)) - linear growth,
        rank 2, vs the rank-1 (multiplicity-1) glued ladder lines.
   (ii) SIGNATURE: the cone's regularized signature is the Barnes
        anomaly P(s) = zeta_2(0, s | 1,2) = s^2/4 - 3s/4 + 11/24
        (re-verified in flint, same Hurwitz route as S's W4), whose
        QUADRATIC part is forced by the two exact slice recursions
        P(s) - P(s+1) = zeta_H(0, s/2) = 1/2 - s/2 and
        P(s) - P(s+2) = zeta_H(0, s) = 1/2 - s (the y- and xbar-
        slices of the cone); only the constant 11/24 needs the Barnes
        computation.
   (iii) s(s-1)-TYPE (gate infty-4): P is self-dual about 3/2, NOT
        about 1/2; the unique real shift recentring it to 1/2 is
        sigma = 1 - EXACTLY the forced Sigma-shift of G's duality
        (the pairing slot has degree sum j + j' = 1, ZG3) - and
            P(s + 1) = s(s-1)/4 - 1/24 :
        quadratic part proportional to s(s-1), self-dual under
        s -> 1-s. Honest accounting registered in advance: ONE
        integer (the recentring shift) is matched against ONE forced
        integer (the duality shift); the leading coefficient 1/4 (vs
        xi's s(s-1)/2) and the constant -1/24 (= zeta(-1)/2,
        observation only, zero G-INT6 weight) are NOT matched.
K3-fail: Psi not injective / multiplicity != Barnes count (then the
   gluing does NOT see the rank sector), or the recentring shift != 1
   (then the s(s-1) reading is a fit and is withdrawn).
```

### Part 3 - K4 on G: the integer layer vs Q's pole

```text
LAYER IDENTIFICATION (registered): G's integer layer = the character/
cardinality data of its slots, three strata:
   (L-i)   slot-supply support: D-branch slot (j, m) carries supply
           2^{-ms} (doc-19/20 dictionary, already spent) => atom set
           {2^m : m >= 1} (+ the Lin atom 1); D'-branch mirror
           {2^{-m}};
   (L-ii)  truncation cardinalities: |D-branch level-N truncation,
           one degree| = 2^{N+1} (F_2-points);
   (L-iii) the rank sector's degreewise dims d_j = floor(j/2) + 1
           (the K3 cone).
THREE registered readings (the task's two, plus my expected third -
written before any run):
   (K4-pass-AA): the glued weights are non-geometric like AA's
        {log k}. EXPECTED FALSE for strata (L-i)/(L-ii): they are
        EXACTLY the 2-adically geometric set {2^j} - indeed exactly
        Q's pole-support atoms (the exactness set of ceil(log_2)).
   (K4-fail): the layer inherits the pole. EXPECTED TRUE PER BRANCH:
        the D-branch atom series sum_{m>=1} (2^m)^{-s} = 1/(2^s - 1)
        has the simple pole at s = 0, residue +1/log 2; slots named:
        ALL D-slots z^m <-> atoms 2^m, m >= 1, and their D'-mirrors.
   (K4-glue, my registered expected overall verdict): the K2 duality
        CANCELS the pole pair exactly - the glued layer-sum is
        1/(1-x) + 1/(1-1/x) - 1 = 0 identically (x = 2^{-s}), atom
        2^m paired slotwise with mirror 2^{-m} by the Gram flip;
        glued residue 0; what survives is the lattice delta at
        2^{-s} = 1 = Z's K1 cross-place attachment point. The rank
        sector (L-iii) evades AA-STYLE: its jump set is 2Z
        (arithmetic, contained in NO {b^j}), its defect series is
        (1/4) Sum (-1)^j j^{-s} = -(1/4) eta(s), ENTIRE, with
        Sum_reg d_j existing: FP = (1/2)zeta(-1) + (3/4)zeta(0)
        - (1/8) = -13/24, rational.
   So: K4 PASSES on G in an AMENDED form - pole evasion by GLUING
   (a third mechanism beyond Q 5.4's (a) non-geometric exactness set
   and (b) abandoning zeta-regularization), with the branch-level
   inheritance reported as the mechanism that makes the cross-place /
   product-formula step NECESSARY. If the cancellation gate fails,
   K4-fail stands and the named slots are the deliverable.
```

Evaluation rules fixed in advance: all F_p algebra exact (integers /
Fractions; truncations weights <= 12, gamma <= 5 unless stated); flint
ball arithmetic for every analytic value (prec 300), tolerances stated
per gate; the doc-19/20 dictionary and the Lerch/Hurwitz pipeline reused
unchanged; no RH / zero-side input anywhere. Carrier guard on every
construction: each gate must consume the ring/equivariant structure
(DMPR's F_p[y] with res, S.1's square maps, the dictionary); the witness
for each part carries an explicit guard gate.

## 2. THE CONSTRUCTIONS (with G-INT6 ledgers inline)

### 2.1 Part 1: the odd-p glued object G_p (what replaces S's Tate disk)

At odd p the local situation is (docs 24/25, DMPR, QS): the C_2-Tate
VANISHES ((HF_p)^{tC_2} = 0, hence THR(F_p)^{tC_2} = 0) and the local
object is the genuine fixed-point carrier

    D_p := pi_* THR(F_p)^{C_2} = F_p[y],  |y| = 4,  res(y) = x^2,
    wt(y) = 2 (x-power via res), one slot per weight 2n, degree 4n.

What replaces S's Tate disk, stated carefully: NOT a completion (no
functor supplies one - d6), but the y-adic TRUNCATION TOWER of the
fixed-point carrier,

    D_p/y^{N+1}  --(x y)-->  D_p/y^{N+2},

canonical because the weight grading is intrinsic (res-visible), with
its level-N SOCLE pairing <a, b>_N = (coeff of y^N in ab) - the unique
minimal graded slot of the truncation, the odd-p analogue of U's
t^{-1} z^N residue slot (which at p = 2 was supplied by Greenlees-May;
here the socle is canonical by gradedness alone). Then:

- [L1-p, forced] D'_p := colim of the Matlis duals of the tower
  = the graded dual of F_p[y], with z-contraction action;
- [L2-p, forced given the weight grading] as an algebra D'_p is the
  divided-power algebra Gamma_{F_p}[y']:
      gamma_a gamma_b = binom(a+b, a) gamma_{a+b}  (mod p)
      = F_p[gamma_{p^k} : k >= 0]/(gamma_{p^k}^p),
  by Lucas at p; the digit presentation gamma_m =
  unit . prod_k gamma_{p^k}^{m_k} has p-adic UNIT coefficient
  m!/prod_k ((p^k)!)^{m_k} (Legendre: v_p of numerator and denominator
  both equal (m - S_p(m))/(p-1)); the weight-graded coproduct on y is
  forced additive (only weight-1 tensors are y(x)1, 1(x)y; counit
  forces both coefficients 1). NOT Laurent: gamma_1^p = p! gamma_p = 0
  - the F-a guard persists at odd p.
- [L4-p, forced] gluing locus: the weight-0 slot F_p . 1 = F_p .
  gamma_0 (the augmentation) - a POINT (d1).
- [L5-p, forced by the tower] the residue pairing
  <y^m, gamma_{m'}> = delta_{m,m'}, <1, 1> = 1, all other weights 0
  (weight-0-homogeneity forced by tower compatibility: level N pairs
  m + m' = N).

    G_p := F_p[y] cup_{F_p} Gamma_{F_p}[y'] :
    one slot per weight in 2Z (weight 0 once), degree support 4Z,
    ONE slot per degree - no vertical line, no t (d1, d5).

[L6-p] product formula NOT SPENT (reserved for the global assembly),
exactly as in Z.

### 2.2 Part 2: where the rank sector sits relative to G

S's square map fix -> Tate: xbar |-> x = t^{-2} z, y |-> tx = t^{-1} z
(S-doc sec 4). On monomials this is

    Psi(xbar^i y^k) = t^{-(2i + k)} z^{i + k},   slot (j, m) =
    (2i + k, i + k);  i = j - m >= 0, k = 2m - j >= 0,

so Psi is injective with image the cone {m <= j <= 2m} in G's
D-branch: the Euler tower is NOT outside the glued object - the
gluing sees it through S's own square map, as a rank-2 sub-cone of
the disk branch. The K3 question becomes exact: is the cone's
regularized signature the s(s-1)-type rank pair after G's own
(forced) duality recentring? Registered answer in sec 1.

### 2.3 Part 3: the integer layer, located

The three strata (L-i)-(L-iii) of sec 1 are the complete character/
cardinality data of G's slots: each slot is one F_2-line (cardinality
2), so the only integer content is (a) WHERE the slots sit (supply
atoms - stratum L-i), (b) how many slots a truncation has (cardinality
2^{N+1} per degree - stratum L-ii), and (c) the multiplicity profile
of the structured sub-objects (the K3 cone - stratum L-iii). Q's test
(prime_cc_quantization_defect machinery, sec 5.4 of the Q-doc) is run
on each stratum; the witness reuses Q's pole/FP numerics style (flint,
prec 300) with the exact rational identities gated first.

## 3. PART 1 VERDICT: C1 - the mechanism is NOT 2-specific [OG1-OG6 ALL PASS]

Witness ALL PASS (p = 3, 5; exit 0). All four C1 clauses landed as
registered:

- D'_p FORCED (OG1): divided powers at p with zero choices; the digit
  presentation has p-adic unit coefficients (Legendre digit-count
  identity); the coproduct is forced additive; gamma_1^p = 0 keeps the
  F-a guard (the compactified dual is never a Laurent/function-field
  ring at ANY p - no meromorphic continuation can be imported).
- K2-analogue PASS (OG2, OG3): the level-N socle pairings are the one
  G_p-pairing through the colimit insertions, compatibly at every level,
  F_p-bilinearly; Gram = permutation implementing m <-> -m; fixed
  G_p-pairs N-independent while level-pairs decay - compactification
  restores negation at odd p exactly as at 2.
- c = 1/2 FORCED (OG4): negation-ratio constancy (= -1, dev < 5e-16)
  only at c = 1/2, at q = 3 and q = 5; A1 slope exact 1/2.
- Scale-freeness (OG5): glued trace = 0 and glued anomaly = 0 exactly;
  the fold's (1-s)/2 lives only on the unglued half - K1's
  "scale carriers are the unglued sectors" repeats at odd p.

The registered deltas (d1)-(d6) all materialized and none broke a named
step. CONSOLIDATED READING: the gluing mechanism (Matlis-forced dual,
tower identity, duality-restored negation, A1-forced c = 1/2) is
place-uniform; what IS 2-specific is exactly the list Z found special:
the Lin LINE (a point at odd p), the Sigma-shift (0 at odd p, so the
N2/t-lattice forcing has no odd-p analogue - the spacing pi i/log p
refinement is NOT forced at odd p by this route), the shear, and the
Euler tower. The p = 2 Euler tower / Lin line were load-bearing for
those FINDINGS, not for the gluing - the PFD spec needs no amendment;
its local-data clause is instantiated now at p = 2, 3, 5.

## 4. PART 2 VERDICT: K3 PASS in the located form [KG1-KG5 ALL PASS]

- SEEN (KG1, KG2): the gluing sees the Barnes Gamma_2 sector through
  S's own square map fix -> Tate: Psi(xbar^i y^k) = t^{-(2i+k)} z^{i+k}
  is injective with image the cone {m <= j <= 2m} INSIDE G's D-branch;
  degreewise multiplicity floor(j/2)+1 = the Barnes count. The rank
  part of G is this cone (multiplicity grows linearly in degree = rank
  2), against the multiplicity-1 glued ladder lines (rank 1, affine
  anomaly, KG5).
- SIGNATURE (KG3): P(s) = zeta_2(0,s|1,2) = s^2/4 - 3s/4 + 11/24
  re-verified in flint; NEW exact structure: the quadratic part is
  FORCED by the two slice recursions P(s) - P(s+1) = zeta_H(0, s/2)
  (y-slice) and P(s) - P(s+2) = zeta_H(0, s) (xbar-slice) - the
  rank-2 anomaly is literally the two rank-1 ladders of the cone's
  edges integrated up; only 11/24 needs the Barnes computation.
- s(s-1) (KG4, the gate infty-4 content): P is self-dual about 3/2,
  not 1/2; the unique recentring shift is sigma = 1 = EXACTLY the
  forced Sigma-shift of G's duality (pairing degree sum j + j' = 1,
  Greenlees-May), and
      zeta_2(0, s+1 | 1,2) = s(s-1)/4 - 1/24,
  self-dual under s -> 1-s. So: G's own duality shift recenters the
  Barnes anomaly into an exact s(s-1) form. Gate infty-4 gets its
  candidate identification WITNESSED: the rank pair is the
  Euler-tower cone, and the duality that the gluing restores is what
  places its quadratic at s(s-1).
- HONEST ACCOUNTING (registered in advance): one matched integer
  (shift = 1, forced both ways); the leading coefficient 1/4 vs xi's
  s(s-1)/2 is NOT matched (factor 2 open - possibly O Prop A6's
  double cover; flagged as reading, zero weight), the constant -1/24
  (= zeta(-1)/2) is NOT matched (observation, zero weight). The cone
  reads the DEGREE grading (doc 25's convention flag); the recentring
  uses the DEGREE shift of the duality, so the convention is at least
  used consistently on both sides of the match.

## 5. PART 3 VERDICT: K4 PASS IN AMENDED FORM - pole evaded by GLUING,
## not by non-geometricity [QG1-QG5 ALL PASS]

The registered dichotomy was incomplete, as registered in advance; the
split verdict:

- (K4-pass-AA) FALSE for the ladder layer (QG1): G's slot atoms and
  truncation cardinalities are EXACTLY {2^j} - b = 2-geometric, indeed
  identical to Q's pole-support set (the exactness atoms of
  ceil(log_2)). G's integer layer sits ON Q's pole.
- (K4-fail) TRUE PER BRANCH (QG2): each branch alone inherits the
  simple pole at s = 0 (residues +-1/log 2); slots named: all D-slots
  z^m <-> atoms 2^m (m >= 1), and their D'-mirrors gamma_m.
- (K4-glue) THE VERDICT (QG3): the K2 duality pairs each atom 2^m with
  its mirror 2^{-m} (the product-formula shadow |2^m| . |2^m|^{-1} = 1
  slotwise) and the glued layer-sum is A_D + A_D' + 1 = 0 IDENTICALLY
  (residue 0 to 1e-86): the pole pair cancels. This is a THIRD evasion
  mechanism beyond Q 5.4's (a) non-geometric exactness set and (b)
  abandoning zeta-regularization: (c) DUALITY CANCELLATION. What
  survives is the lattice delta at 2^{-s} = 1 - precisely Z's K1
  cross-place attachment point: the un-cancelled pole reappears as the
  local face on which the global product formula must act.
- RANK SECTOR (QG4): evades AA-STYLE - jump set 2Z (arithmetic, in no
  {b^j}), defect series exactly -(1/4) eta(s) (entire), Sum_reg d_j =
  -13/24 finite and rational. (Observation, zero weight: -1/24 =
  (1/2)zeta(-1) appears both here and in the recentred Barnes
  constant.)

So G's integer layer DOES break the strict tolerance <-> derived
dichotomy in a recorded way (doc 28 K4's demand), but the recorded way
is new: per-branch divergence + duality cancellation, with the
non-geometric (AA-like) behavior confined to the rank sector.

## 6. G-INT6 LEDGERS

Part 1 (odd p): L1-p Matlis dual/tower colimit FORCED; L2-p divided
powers FORCED given weight grading (unit digit coefficients proved, not
assumed); L4-p gluing point = augmentation, canonical; L5-p pairing
forced by tower compatibility; L6-p product formula NOT SPENT. Socle
slot at level N: canonical by gradedness (replaces the Greenlees-May
t^{-1}-slot, which needed the Tate). Zero free choices. Deltas
(d1)-(d6) are absences, not choices.

Part 2: inputs = S's square maps (spent), the dictionary (spent), the
Barnes pipeline (spent by S's W4, re-verified); the slice recursions
are new exact identities with zero choices; the recentring match spends
nothing (both integers forced). Unmatched: 1/4 and -1/24 (declared).

Part 3: layer identification is exhaustive for a slotwise
one-dimensional object (location + count + multiplicity); Q's machinery
reused at the closed-form level (the G-layer needs no sawtooth
continuation - its atom series are exact rational functions, simpler
than Q's D_b). Base b = 2 is G's own (the carrier's F_2/weight-2
structure), not a presentation choice - the one place the Q-doc's
base-dependence caveat does NOT bite.

Witness-engineering record: one vacuous gate clause in QG3 (slotwise
pairing tautology) found on self-review after first run and replaced by
a genuine minimal replication of the Z-witness pairing block; gate
predicate strengthened, never weakened; all gates re-run PASS. One dead
variable removed from KG5 (never used in a predicate).

## 7. HONEST LIMITS

- Everything is pi_*-level, riding on DMPR Cor 5.19 (odd p, theorem-
  grade) and Theorem S.1 (p = 2, lead-rerun); no spectrum-level
  realization (C5''' untouched).
- Odd-p instances: F_p-bilinearity tested with random scalars at
  monomial level; the divided-power MULTIPLICATION's interaction with
  the pairing (residue-of-product) is not claimed - as at p = 2, no
  Laurent ring exists, and the tower identity is the content.
- The odd-p socle-slot argument ("canonical by gradedness") is mine,
  not literature-sourced; it replaces Greenlees-May, which genuinely
  has no odd-p analogue (Tate = 0). If the lead wants the odd-p
  pairing derived from an equivariant duality rather than from Matlis
  theory alone, that is open.
- K3: the s(s-1) identification matches ONE forced integer; the factor
  1/4 vs 1/2 and the constant -1/24 are open; the degree-grading
  convention (doc 25 flag) is used, consistently but unadjudicated.
- K4: "G's integer layer" is exhaustive for slot data, but a future
  spectrum-level G could carry MORE integer content (e.g. k-invariant
  data); the verdict covers the pi_*-level object only. The duality-
  cancellation mechanism (c) is exact here; whether it survives the
  global assembly (all places at once, where the deltas from different
  p must interact) is exactly doc 28 step 2's burden.
- No RH / zero-side input anywhere.

## 8. HAND-OFF

```text
PART 1 (C1): PASS - gluing mechanism place-uniform (p = 3, 5 witnessed;
        D' forced, tower identity, Gram permutation, c = 1/2 forced at
        q = p, glued object scale-free). 2-specific: Lin line,
        Sigma-shift, N2-forcing, shear, Euler tower. PFD spec stands
        unamended; local clause instantiated at p = 2, 3, 5.
PART 2 (K3): PASS, located - the rank part of G is the fix->Tate CONE
        of the Euler tower (multiplicity floor(j/2)+1); quadratic
        anomaly forced by two exact slice recursions; G's own duality
        shift (1) recenters it to s(s-1)/4 - 1/24. Gate infty-4
        candidate witnessed. Open: factor 1/4 vs 1/2; constant -1/24.
PART 3 (K4): PASS AMENDED - ladder layer is b=2-geometric (sits ON Q's
        pole), inherits the pole PER BRANCH (slots named), cancelled
        EXACTLY by the K2 duality (mechanism (c), new); rank sector
        evades AA-style (-13/24 finite). Survivor = the lattice delta
        = K1's cross-place attachment point.
NEXT:   the global assembly (doc 28 step 2) now has: place-uniform
        glued objects at p = 2, 3, 5; the scale carriers (fold,
        Gamma_C, Barnes) all UNGLUED; the per-place pole-cancellation
        leaving exactly the lattice deltas the product formula must
        bind; and the rank pair sitting at s(s-1) once the duality
        shift is spent. The 1/(2pi) gate (first gate of step 2) should
        be attacked where these meet.
```

## 9. Witnesses (all exit-gated, ALL PASS, lead can rerun)

    python3 -m scripts.numerics.witness.prime_int_gc_oddp_glue
    python3 -m scripts.numerics.witness.prime_int_gc_k3_barnes_rank
    python3 -m scripts.numerics.witness.prime_int_gc_k4_integer_layer

Inherited, rerun before work: prime_int_z_u2_glue, prime_int_thr_p2_anomaly.
