# WW - The silhouette dossier: every certificate-grade shadow of the missing unit, consolidated; the inverse problem, posed

Status: fresh-context worker WW, 2026-06-11. Charter doc 38 sec 2 (first
cycle under the charter). Required reading executed in order: doc 38
(I am its sec 2), docs 34 + 37 (the six-clause spec), then the shadow
sources: QQ-native-face.md, NN-graph-class-test.md, TT-truncated-face.md,
RR-f123-cycle.md, UU-ku-castelnuovo.md, HH-weil-restriction-fork.md,
BB-global-assembly.md, LL-square-dual.md, SS-ku-inequality-proof.md;
doc 21 (Q-SCHEME format), doc 32 (the FF conjunction). Inherited
witnesses rerun by me BEFORE any new work: prime_qq_native_face_index
(ALL PASS QQ1-QQ9, exit 0), prime_ss_ku_inequality_proof (ALL PASS
SS1-SS8, exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_ww_silhouette

Sections 0-3 (the dossier rows, the hand derivation of the new-shadow
closed form, the gates, the registered predictions) were written BEFORE
the witness was first run. DISCLOSURE (TT precedent): ONE design-stage
calibration run (inline, no witness file) checked the NS1 closed form
had slack before gate registration (agreement 1e-58 at p in {2,3,5},
n in {0,1,2}; and 4c_1 reproduced QQ's measured amplitudes 0.0047 /
0.042 / 0.175); no derivation or gate was changed after it.

Discipline: F-a (no zeta values, no zeta continuation; the Gamma
function enters ONLY as the closed form of a hand-derived Mellin
integral of the Gaussian deficit - sec 2.1 - never as an EF import);
zeros NEVER consumed (no fork_lib import; no freeze needed - every
quantity below is congruence/entry/period-determined, z < 3 already
certified in the source memos). G-INT6 ledger sec 7; carrier guard
WW14. Comparison-only items (kappa = pi; HH's eigmin) are FLAGGED
in-row. All decision values flint arb prec 300; exact
integers/Fractions for every algebraic identity; sign decisions only
when the ball resolves.

## 0. The task and what "self-certifying" means here

Doc 38 sec 2: we hold certificate-grade SHADOWS of the six-times-
demanded object. This memo (1) consolidates them into ONE normalized
inventory with ONE consolidated witness recomputing every decisive
number (so the dossier does not depend on nine scattered witnesses),
(2) EXTENDS the silhouette by three pre-registered new shadows, and
(3) poses the inverse problem as a constraint-satisfaction statement
with an honest first characterization pass.

THE SIX CLAUSES (doc 34 sec 2 + doc 37 sec 2, fixed labels used
throughout):

```text
C1 (BB)  couples comb to continuum and READS THE SCALE kappa = pi
         (density layer, not FE layer - FE is kappa-blind by theorem).
C2 (GG)  supplies ONE CONTINUUM UNIT PER PLACE, paid at each
         window-entry phase (global existence; doc 35 spec).
C3 (FF)  lives in the rational/Anderson layer that torsion provably
         lacks (no shadow in this dossier computes C3; recorded).
C4 (HH)  is a SIGNED archimedean coordinate that JOINTLY CANCELS
         (cannot enter as a PD block; the cancellation is load-bearing).
C5 (LL)  makes the square dual's FE HOMOGENEOUS: the unit class whose
         Fourier dual is the continuum unit.
C6 (UU/SS/doc 37) supplies a SECOND, INDEPENDENT evaluation of the
         weight-against-Frobenius pairing (class- and scale-coupled
         trace; Lefschetz's slot).
```

FF conjunction (doc 32/34, for G-CH2 scoring): index shape,
integrality, effectivity, monoid family, growing observable.

## 1. THE DOSSIER (rows S1-S12; certificates recomputed by gates WW1-WW14)

Format per row: STATEMENT / CERTIFICATE (witness + precision) /
Q-SCHEME units (ladder data, weight dictionary, scale, scheme) /
CLAUSE.

```text
S1  MEAN IDENTITY. mean_a(Delta_p) * log p = gamma + log pi for every
    p; Delta_p(a) = sum_{m in Z} d(e^{-a} p^m), d(x) = 1 - e^{-pi x^2}
    - e^{-pi/x^2}; exactly log p-periodic, max at entry phase.
    CERT: QQ7 (1.5e-36); recomputed WW1 at p in {2,3,5,7} (< 1e-20).
    UNITS: linear slot units on G_p's atom ladder p^m; scale a = log
    window radius; scheme = K2-paired glued object; Gaussian import
    logged. CLAUSE: C2 (the per-place unit's mean mass), C4 (its
    constant is the EF archimedean constant, emerging with no EF input).
S2  THE SHAPE LAW (NEW, NS1). The FULL Fourier data of Delta_p:
    c_n(p) * log p = -Re Gamma_R(2 pi i n / log p), Gamma_R(s) =
    pi^{-s/2} Gamma(s/2), for ALL n (n = 0 case = S1). The unit's
    complete per-place silhouette is the archimedean Euler factor on
    the imaginary axis, sampled at the place's own frequencies
    2 pi n / log p. CERT: WW2 (registered < 1e-20; hand derivation
    sec 2.1, Mellin, no EF input). UNITS: as S1; frequencies in
    1/scale units. CLAUSE: C2 + C4 (the shape), C1 (the pi in
    Gamma_R's argument is S7's kappa, now appearing in every mode).
S3  ZERO-CHARGE DICHOTOMY. The d = 1 (Lambda(p)-class) dual carries
    continuum charge EXACTLY -1 (u(theta - 1/u - 1) -> -1); the
    truncation band carries charge EXACTLY 0 ((2q-4) - 2q rho_q = 0,
    Fractions); the surviving face's hole coefficient is 0 by identity
    (|u(D_q - rho_q)| <= G(u/q) -> 0). Charge is integer-quantized;
    -1 is unrepairable by bookkeeping, 0 always is.
    CERT: NN G3 (4e-90), TT2 (exact), SS.1; recomputed WW5.
    UNITS: continuum units (coefficient of 1/u in the dual);
    scheme = comb/coset Poisson on Z. CLAUSE: C5 (the missing unit is
    exactly one unit of continuum charge, no more, no less).
S4  PAYMENT SCHEDULE. Deficits the unit must pay: -e^{-a}/2 (1+o(1))
    on every Lambda(p) class (place-independent, smooth); per-slot
    entry deficit d(1) = 1 - 2e^{-pi} = 0.91357 (linear units);
    entry floor of the honest dual D^hon(entry) -> rho_q
    erfc(sqrt(pi)) = rho_q * 0.012224 [POST-RUN CORRECTION, sec 4:
    the true value is 0.0121889; TT's prose digit was a display slip];
    entry margin constant
    1 - 6T(1) = 0.740696 = lim q m+(q, entry).
    CERT: NN G3c, QQ6, TT D2', SS.2c; recomputed WW6, WW7.
    UNITS: log-count units (NN/SS margins) vs linear slot units (QQ) -
    same locus, two normalizations, NO margin identification claimed
    (NN G5 lesson); scheme = LL6/NN chi calibration. CLAUSE: C2
    (quantitative), C6 (what the second evaluation must reproduce).
S5  THREADING LAW. Per-place: NO positive measure pays the window-entry
    deficits (p = 11 family exactly infeasible: both slot margins
    certified < 0 under v; (11;2) chargeable < 5e-48 of k=1 mass under
    g). Globally: the banked KMS-1/2 measure pays everything on the
    scanned window (A_g(4.96) = +3.03e-2 > 0). The unit is NOT a
    per-place object; the subsidy crosses places.
    CERT: RR RG4-RG6 (arb/exact); recomputed WW8, WW9.
    UNITS: Theta-weighted aggregate of log-count margins; weights
    2 p^{-k/2} (KMS-1/2, banked); scheme = NN comb dictionary.
    CLAUSE: C2 + C4 jointly (coupling, not padding); kills every
    localized construction.
S6  DEPTH WALL. The 2D (Castelnuovo) step demands Frobenius depth
    (Lambda_p - m+)^2 / m+ ~ rho_q Lambda_p^2 e^a (EXPONENTIAL in the
    window) against available depth a (LINEAR). At a = 8: needed 1197
    vs available 7.69 (q = 3); 16854 vs 4.80 (q = 121). The append
    posing fails Lorentzian shape by EXACTLY the unpaid atom
    s = Lambda(q) - m+ > 0; B' = Lambda_p - m+ occupies Weil's
    fixed-point slot with only ONE evaluation.
    CERT: UU3-UU5 (0.13% on the law); recomputed WW10 (2%).
    UNITS: degree units (log p); scheme = override posing on the
    certified Lorentzian face. CLAUSE: C6 (the wall IS the demand for
    the second evaluation; no re-posing crosses e^a vs a).
S7  KAPPA = PI (COMPARISON-FLAGGED). The assembly determines no scale
    (Prop BB.1, equivariance); the FE layer is kappa-blind
    (zeta_H(0,s/2) + zeta_H(0,(1-s)/2) = 1/2 exactly); the EF shadow
    selects kappa = pi (folded) = 2pi (unfolded, Legendre duplication
    Gamma_R(s) Gamma_R(s+1) = 2 Gamma_C(s)); the 2pi is already in the
    finite-place combs (weight = spacing).
    CERT: BB GB1-GB5; recomputed WW11 (identity exact in Fractions;
    duplication < 1e-40; selection comparison-flagged).
    UNITS: doc 21 Q-SCHEME quadruple explicitly: (half-ladder
    {nu + s/2}, spacing 2, scale kappa, real/folded scheme); 2-powers
    EF-invisible. CLAUSE: C1 (its entire content).
S8  FE-HOMOGENIZER CHARGE. A_D + A_D' + 1 = 0 identically (exact
    rational functions); the +1 is the unit class counted once; the
    dual side of the square FE lacks it; its Fourier dual is the
    continuum unit; inserted by hand it repairs the strict family
    with ZERO SLACK at deep effectivity (must couple, not pad).
    The forced GG repair at d = 1 recovers the self-dual Jacobi theta
    EXACTLY (m+_GG(d=1) = log theta(e^a) + log((1+theta(e^a))/2) > 0).
    CERT: LL1-LL6, RR RG1 (3.9e-90); recomputed WW12 (exact + 1e-60).
    UNITS: continuum units at the pole layer; scheme = K2 pairing on
    the divided-power branches. CLAUSE: C5 (its entire content).
S9  JOINT-CANCELLATION GEOMETRY. In the certified Lorentzian face:
    primes are spacelike (Lambda(p^k) = -<d_k, d_k>, exact), the unit
    class is null, W_inf is SIGNED on the class (eigmin -0.907 at
    R = 4.96 while the margin stays positive: CITED from HH H4, not
    recomputed - flagged import); the (1,0,1) Toeplitz direction
    (eigenvalues {0,1,2}, exact) is admissible and isolates the
    breaking slot: no scalar aggregate can dominate.
    CERT: HH H1/H4 (exact/measured), RR RG7 (exact); recomputed WW13
    (Toeplitz exact; two-place non-summability rows certified).
    UNITS: M-geometry of (log p) MAX face; scheme = d-frame.
    CLAUSE: C4 (its entire content).
S10 SMALL-PLACE CORNER + AMPLITUDE LADDER (NS3, partly NEW). The only
    slack anywhere: q in {3,4,8}, a < 3 (UU corner); NN's safe cells
    p in {2,3}; W's low-weight holes p in {2,3}. NEW: the per-place
    oscillation amplitude of Delta_p is 4 sum_{n odd} c_n(p), c_n from
    S2 - so the amplitude ladder amp(2) = 0.0047 << amp(3) = 0.042
    << amp(5) = 0.175 is FORCED by Gamma decay on the imaginary axis
    (|Gamma_R(2 pi i/L)| collapses as L -> 0): the small places are
    quiet because their frequencies 2 pi/log p are HIGH. The corner is
    where the unit's oscillation is below the breakage scale.
    CERT: WW3 (registered: parity identity < 8|c_5|; amplitudes
    monotone in p over {2,3,5,7,11,13}); UU4 census (cited).
    UNITS: linear slot units. CLAUSE: constrains C2's local size; the
    record explains the thrice-seen corner echo.
S11 DISJOINT SPECTRA (NEW, NS2). The frequency supports
    {2 pi n / log p}_n of Delta_p and Delta_q are DISJOINT for p != q
    (p^m = q^n impossible: unique factorization, exact integers), so
    long-window correlation of the per-place fluctuations -> 0: the
    cross-place coupling CANNOT be carried by correlated fluctuations;
    only the means (S1) couple - exactly where the product formula
    acts (QQ's "coupling slot belongs to the product formula").
    CERT: WW4 (exact disjointness 1 <= m, n <= 24; covariance records).
    UNITS: frequency = 1/scale. CLAUSE: C1 + C2 (the coupling's only
    available channel), C3-adjacent (a regulator/log-lattice
    constraint on the category).
S12 CARRIER GUARD (the Euler-product clause). EVERY shadow above is
    unformable on Epstein x^2 + 5y^2 (36 = 4*9 = 6*6, 4/6/9
    irreducible: no valuation -> no slot ladder, no comb, no tower
    address, no Delta_p, no charge ledger) and on DH (no carrier
    monoid). CERT: LL7/QQ9/NN G6/UU7 (exact); recomputed WW14.
    CLAUSE: all six - the structure the inverse problem characterizes
    must consume unique factorization to even pose the shadows.
```

NOT IN THE DOSSIER (recorded): C3 (rational/Anderson layer) has no
computed shadow - it is a demand from FF's structural side with no
certificate-grade number yet; the dossier cannot constrain it. The
2-primary lambda^{1/2} of doc 38's inventory (small-place corner,
q = 8 = 2^3 entry) is carried inside S10's census citation.

## 2. THE NEW SHADOWS: hand derivations (written before any run)

### 2.1 NS1 - the shape law (S2): the silhouette IS Gamma_R on Re s = 0

Delta_p(a) = sum_m g(a - m log p), g(u) := d(e^u) (even, decay
pi e^{-2|u|}). Poisson: Delta_p(a) = c_0 + 2 sum_{n>=1} c_n
cos(2 pi n a / L), L = log p, c_n = ghat(2 pi n/L)/L,
ghat(xi) = int_R d(e^u) e^{-i xi u} du.

MELLIN EVALUATION (hand). For -2 < Re s, s != 0, define
G(s) = int_0^oo (e^{-pi x^2} - 1_{x<1}) x^{s} dx/x
     = (1/2) pi^{-s/2} Gamma(s/2) - 1/s
(split for Re s > 0, continue; near 0: G(s) = -(gamma + log pi)/2
+ O(s) from Gamma(s/2) = 2/s - gamma + O(s)). Decompose d(x) =
[1_{x<1} - e^{-pi x^2}] + [1_{x>1} - e^{-pi/x^2}]; substitute
x -> 1/x in the second piece:

    ghat(xi) = -G(-i xi) - G(i xi) = -2 Re G(i xi)
             = -Re[ pi^{-i xi/2} Gamma(i xi/2) ]      (xi != 0;
               the 1/s terms are imaginary and cancel),
    ghat(0)  = -2 G(0) = gamma + log pi               (= QQ's C*).

Hence the REGISTERED CLOSED FORM:

    c_n(p) * log p = -Re Gamma_R(i xi_n),  xi_n = 2 pi n / log p,

with Gamma_R(s) = pi^{-s/2} Gamma(s/2). S1 is the n = 0 mode. The
Gamma function here is DERIVED from the Gaussian deficit's Mellin
transform (one differentiation under the integral away from Lemma-B
grade calculus) - no EF, no zeta, no zero-side input. Consequences,
registered: (i) c_n real (Delta_p even about entry phase - QQ7b's max
locus, now structural); (ii) |c_n| collapses doubly fast in n and in
1/log p (|Gamma(iy)|^2 = pi/(y sinh(pi y))): the silhouette is
analytically COMPLETE - a finite number of modes determines it to any
precision; (iii) the amplitude ladder of S10.

### 2.2 NS2 - disjoint spectra (S11)

Delta_p's spectrum is {2 pi n/log p : n in Z}. For p != q the supports
meet only at 0: n log q = m log p with (n, m) != (0,0) would give
p^m = q^n, impossible by unique factorization (exact integer
statement; the same carrier consumption as everywhere - S12). So
cov_[0,T](Delta_p, Delta_q) -> 0: registered NUMERICAL RECORD
(|corr| at T in {50, 200}, 4096-pt grids, float-grade flagged) +
EXACT gate (p^m != q^n for all 1 <= m, n <= 24, pairs (2,3), (2,5),
(3,5), (2,7)). Registered prediction: |corr(200)| < 0.1.

### 2.3 NS3 - the amplitude/parity identity (S10)

Delta_p(0) - Delta_p(L/2) = 4 sum_{n odd} c_n. REGISTERED:
|(Delta_p(0) - Delta_p(L/2)) - 4(c_1 + c_3)| <= 8 |c_5^closed| + 1e-25
at p in {2,3,5,7,11,13} (c_5^closed from sec 2.1; the tail is
sign-alternating-or-smaller by Gamma decay, factor 2 safety), and
amp(p) := Delta_p(0) - Delta_p(L/2) STRICTLY INCREASING in p on
{2,3,5,7,11,13}. RECORD (no gate weight): amp against NN's
neg-frac table (0/0/0.25/0.30/0.35/0.36 at p = 2/3/5/7/11/13) - the
breakage boundary sits between amp(3) = 0.042 and amp(5) = 0.175.

## 3. PRE-REGISTERED GATES (written before the first run)

Evaluation rules fixed in advance: arb prec 300; lattice sums
truncated |m| <= 120 with certified geometric tail added to the ball
radius (d(x) <= pi/x^2 for x >= 1, termwise); DFT N = 128 points
(aliasing < |c_{n+128}|, astronomically below tolerance by the closed
form's own decay - the closed form is the TARGET, so the gate
tolerance 1e-20 absorbs quadrature honestly only because both routes
are computed at prec 300 with certified tails; any mismatch FAILS);
theta/comb sums truncated at term < 1e-90 (monotone tails); exact
Fractions for every algebraic clause. Banked decision values are
gated against the SOURCE-PRINTED numbers (tolerance = printed
precision); a mismatch is a FAIL of the consolidation, full stop.

```text
WW1  S1 mean identity: |c_0(p) log p - (gamma + log pi)| < 1e-20,
     p in {2,3,5,7}. FAIL: any p.
WW2  S2/NS1 shape law: |c_n(p) log p + Re Gamma_R(2 pi i n/log p)|
     < 1e-20, p in {2,3,5,7}, n in {1,2,3}. FAIL: any pair. (A PASS
     certifies the silhouette's completeness; a FAIL kills NS1.)
WW3  S10/NS3: parity identity (tolerance 8|c_5^closed| + 1e-25) and
     strict amp monotonicity over p in {2,3,5,7,11,13}; NN neg-frac
     comparison RECORDED. FAIL: identity or monotonicity.
WW4  S11/NS2: p^m != q^n exact, 1 <= m,n <= 24, four pairs; corr
     records at T in {50, 200} (float-grade, flagged);
     |corr(200)| < 0.1. FAIL: any clause.
WW5  S3 charge dichotomy: |u(theta(u) - 1/u - 1) + 1| < 1e-40 at
     u in {36, 968}; M_0(q) = 0 and (2q-4)/rho_q = 2q exact Fractions,
     q in {3, 9, 25, 121, 169}; |u(D_q(u) - rho_q)| <= G_fn(u/q) at
     (q, u) in {(9, 72), (121, 968)} (G_fn(x) = 4x T(x)). FAIL: any.
WW6  S4 payment schedule: (a) |m+(d=1, a) + e^{-a}/2| < 0.12 e^{-a},
     a in {2, 5}, and m+(d=1, 4.96) < 0; (b) d(1) = 1 - 2 e^{-pi} to
     1e-60, value 0.9135...; (c) 1 - 6 T(1) = 0.740696... (printed,
     6 digits), and q m+(q, entry): |val - 0.8175| < 2e-3 (q = 25),
     |val - 0.7561| < 2e-3 (q = 121), both > 0.740696. FAIL: any.
WW7  S4 erfc floor: D^hon_q(q+1) computed (coset dual minus band);
     |D^hon - rho_q erfc(sqrt pi)| < 3/(q+1) at q in {25, 121};
     |diff(121)| < |diff(25)| (EM excess shrinks); values recorded.
     FAIL: any clause.
WW8  S5 threading, per-place (NN/RR machinery replicated): decision
     cell |m+((11;2), 4.96) + 2.214249e-3| < 1e-8, certified < 0;
     A_11(4.96) variant v: certified < 0, |A + 2.52e-3| < 2e-5;
     variant g: certified < 0, |A + 4.03e-4| < 1e-5 (m1_GG = exact-0
     ball, bound 3 e^{-pi e^{2a}}); per-place infeasibility (v) =
     both slot signs negative, printed. FAIL: any.
WW9  S5 threading, global: A_g(4.96) = sum over the 13 admissible
     k >= 2 slots (p <= 11) + exact-0 k=1 balls: certified > 0;
     comparison |A_g - 3.03e-2| / 3.03e-2 < 0.25 (slot-set
     reconstruction tolerance, flagged). FAIL: sign unresolved or
     comparison off.
WW10 S6 depth wall: m+(q, a) via coset dual route, anchors
     |m+(3, log 4) - 0.55653| < 2e-5, |m+(121, 4.96) - 6.4682e-3|
     < 1e-6; needed(q, 8) := (Lambda_p - m+)^2/m+ - log 2 satisfies
     |needed * e^{-8} - rho_q Lambda_p^2| < 0.02 rho_q Lambda_p^2 at
     q in {3, 121}; available = floor(8/log q) log q printed; append
     Schur s = Lambda(q) - m+ > 0 at q in {3, 9, 121} x {entry, 8};
     DISC(3, entry, 1) HOLDS and DISC(9, entry, 1) FAILS (signs
     certified). FAIL: any.
WW11 S7 kappa: (1/2 - s/2) + (1/2 - (1-s)/2) = 1/2 exact Fractions,
     s in {1/3, 2/5, 7/2}; Gamma_R(s) Gamma_R(s+1) = 2 (2pi)^{-s}
     Gamma(s), rel < 1e-40, s in {0.7, 1.3, 5/2}; kappa* = pi
     selection printed COMPARISON-FLAGGED. FAIL: identity clauses.
WW12 S8 FE-homogenizer: x/(1-x) + (1/x)/(1-1/x) + 1 = 0 exact
     Fractions, x in {1/4, 1/9, 3/7}; GG repair two routes
     |direct - closed| < 1e-60 and m+_GG(d=1) > 0 at a in {1/2, 1}.
     FAIL: any.
WW13 S9 joint cancellation: Toeplitz [[1,0,1],[0,1,0],[1,0,1]]
     eigenvalues {0,1,2} exact (charpoly in Fractions), minors PSD,
     det 0; two-place non-summability: 101 rows (|m| <= 50, T={2,3},
     a = 1.24), each row's nearest-lattice deficit > 0.4 certified;
     HH eigmin -0.907 CITED (printed, import-flagged, no gate).
     FAIL: Toeplitz or row clauses.
WW14 S12 carrier guard (exact integers): Epstein x^2 + 5y^2
     represented set to 36; 4, 6, 9 irreducible in the monoid;
     36 = 4*9 = 6*6 distinct factorizations -> valuation ill-defined
     -> S1-S11 unformable (clause-by-clause bookkeeping printed);
     DH: no carrier monoid (printed). FAIL: any.
```

Registered overall verdict logic (before the run): ALL PASS -> the
dossier is self-certifying and secs 4-6 stand on it. Any banked-value
mismatch (WW5-WW10) -> consolidation FAIL: report which shadow's
certificate broke; the inverse problem still poses on the surviving
rows. A WW2 FAIL kills NS1 (the null-hypothesis analysis of sec 5
then loses its sharpest input and says so).

---- verdict sections written after the runs ----

## 4. VERDICT: ALL PASS (WW1-WW14, exit 0) - THE DOSSIER IS
## SELF-CERTIFYING, AND THE NEW SHAPE LAW COMPLETES THE SILHOUETTE

Witness ALL PASS, exit 0, ~0.5 s, deterministic (runs diff-identical;
logs /tmp/ww_run{4,5}.log). Witness-engineering record (disclosed, no
gate predicate touched at any point): (i) arb-from-Fraction ctor shims
(API); (ii) WW4 run 1 evaluated the truncated lattice sum at raw
a >> M log p, outside its truncation window - fixed by reducing a mod
log p (exact by the certified periodicity); the run-1 corr(200) = 0.74
was an artifact of the broken evaluation, the honest record is
corr(50) = -0.0049, corr(200) = +0.0004; (iii) WW5's H-vs-G(u/q) gap
at u = 8q is ~1e-89 absolute, below prec-300 absolute error of the
order-1 cancellation - local prec 600 resolves; (iv) WW13 run 1
selected the candidate lattice point minimizing d instead of |u|
(the farthest instead of nearest phase) - fixed; rows then 101/101
> 0.4 (min 0.6508), matching QQ8a.

Decisive recomputed numbers (all certified, see log):

```text
S1  c_0 log p = gamma + log pi = 1.72194555... to < 6.1e-89 (p <= 7).
S2  NS1 CONFIRMED, worst |c_n log p + Re Gamma_R(2 pi i n/log p)|
    resolves to 0 at ball precision (~1e-74..1e-90), 12 (p, n) pairs.
    THE SILHOUETTE IS COMPLETE: Delta_p's full Fourier data is the
    archimedean Euler factor Gamma_R on Re s = 0, sampled at the
    place's frequencies 2 pi n / log p.
S3  hole charge -1 (3.9e-90); band charge 0 (exact, 5 q's); surviving-
    face |H| <= G(u/q) certified (prec 600) -> c_hole = 0.
S4  -e^{-a}/2 law (2.4e-3, 5.7e-6 abs dev at a = 2, 5); d(1) =
    1 - 2e^{-pi} = 0.913572 (4.9e-91); 1 - 6T(1) = 0.740696;
    q m+(entry) = 0.8175 / 0.7561 at q = 25 / 121 (banked digits).
    CORRECTION RECORDED: erfc(sqrt pi) = 0.0121889 (arb + independent
    quadrature); TT's prose digit "0.012224" is a display slip at the
    4th digit - TT's gates and measured range (0.01219..0.01341) are
    unaffected and bracket the true constant.
S5  m+((11;2), 4.96) = -2.214249375e-3 (banked to all digits);
    A_11(4.96) = -2.520784e-3 (v) / -4.025908e-4 (g), both < 0;
    per-place LP infeasible (both slot signs negative, exact);
    A_g(4.96) = +3.027393e-2 > 0 (banked +3.03e-2) over 13 deep slots
    (slot table printed; the paying surplus sits at p = 2, 3 deep
    steps - the subsidy is cross-place, witnessed slot by slot).
S6  needed depth 1197.0 / 16854.3 vs law 1199.3 / 16856.9 (q = 3/121,
    0.2%/0.02% dev); available 7.69 / 4.80; ratios 155.7 / 3514.4;
    append Schur s > 0 everywhere tested; DISC(3, entry) HOLDS,
    DISC(9, entry) FAILS - the corner as banked.
S7  FE-blindness exact (Fractions); duplication < 1e-40; kappa = pi
    selection COMPARISON-FLAGGED.
S8  A_D + A_D' + 1 = 0 exact; GG repair two routes 1.1e-90, margins
    +5.87e-4 / +2.49e-10 > 0.
S9  Toeplitz (1,0,1) = {0,1,2} exact; 101/101 rows > 0.4 (min 0.65);
    HH eigmin -0.907 cited (import-flagged).
S10 amplitude ladder 0.0047 / 0.0420 / 0.1754 / 0.2986 / 0.4636 /
    0.5184 (p = 2..13), STRICTLY monotone, parity identity to within
    8|c_5|; QQ's measured amps reproduced FROM THE CLOSED FORM.
S11 p^m != q^n exact (4 pairs x 24 x 24); corr(200) = +0.0004
    (float-grade record).
S12 Epstein: 36 = 4*9 = 6*6, all factors irreducible; every row
    unformable; DH: no carrier monoid.
```

The headline new result: WITH NS1 THE SILHOUETTE IS ANALYTICALLY
COMPLETE. Before this cycle the program held the unit's mean
(gamma + log pi), its period, and its phase. Now it holds EVERY
Fourier mode in closed form: the missing unit's per-place shadow is
not LIKE the archimedean Euler factor - it IS Gamma_R restricted to
the imaginary axis, place-sampled. Three corollaries certified en
route: the entry-phase maximum is structural (all c_n real, function
even about entry); the amplitude ladder (and hence the small-place
corner's quietness) is forced by |Gamma_R(iy)| ~ e^{-pi y/4} decay -
small places have HIGH frequencies 2 pi/log p and exponentially small
oscillation; and QQ's three measured amplitudes are now derived
numbers.

## 5. THE INVERSE PROBLEM, POSED

PROBLEM (charter sec 2, now formal). Characterize the structures
(C, tr) - a category/object class C with a trace functional tr,
producing for each prime p a scale-flow trace t_p(a) and a global
pairing - whose output reproduces boundary conditions BC1-BC12. "The
spine" (LS1-LS6 + the C6 demand) is the conjectured solution; the
dossier is the DATA every candidate must hit.

```text
BC1  (S1/S2) per-place restriction: t_p(a) - chi-normalization is
     log p-periodic with Fourier data c_n log p =
     -Re Gamma_R(2 pi i n / log p), all n.
     EXCLUDES: any unit with a different per-place profile - in
     particular any smooth/non-oscillating insertion (constants,
     pure means), any profile whose modes do not collapse at small
     places, and any non-Gaussian self-dual unit (the modes are the
     Gaussian deficit's Mellin data; a different fixed unit changes
     every c_n).
BC2  (S3) total continuum charge is INTEGER and the missing charge is
     EXACTLY -1 per Lambda(p) class; zero-charge defects must be
     absorbed by bookkeeping (chi), never by the unit.
     EXCLUDES: any unit carrying fractional or smeared charge; any
     "regularization" that pays partial units (zeta(0)-style -1/2
     splits are charge-1/2 objects: forbidden); any design where
     truncation bands consume unit budget.
BC3  (S4) the payment schedule: deficits -e^{-a}/2 (1+o(1)) at every
     Lambda(p) class, entry-phased, place-independent at d = 1; entry
     constants 1 - 2e^{-pi}, 1 - 6T(1), rho_q erfc(sqrt pi).
     EXCLUDES: units paying at wrong scale decay (any e^{-c a} with
     c != 1 in count units), wrong phase (payment must spike AT
     window entry), or place-dependent d = 1 payments.
BC4  (S5) THREADING: per-place exactly infeasible, globally feasible
     under the KMS-1/2 weights.
     EXCLUDES: every per-place/local construction - any unit of the
     form sum_p (object at p) with nonnegative per-place margins.
     The structure must move surplus ACROSS places at fixed scale
     (the only certified payer of (11;2)@4.96 is p = 2,3 depth).
BC5  (S11) the per-place fluctuation spectra are pairwise disjoint
     (unique factorization); only the MEANS are common channel.
     EXCLUDES: coupling carried by correlated fluctuations; forces
     the cross-place coupling through the zero-mode/product-formula
     channel (log-lattice/regulator structure in C).
BC6  (S6) the SECOND EVALUATION: the structure must assign the
     weight-against-Frobenius pairing <W, g_i> a value with an
     evaluation INDEPENDENT of the supply data (Lambda_p, log q, i,
     m+), at exponential depth rho_q Lambda_p^2 e^a vs the window's a.
     EXCLUDES: every structure whose every number has one evaluation
     (the whole certified corpus to date); every re-posing/relabeling
     (UU: posing-split is content-free); any "evaluation" equal to
     the count BY CONSTRUCTION (doc 38 P4's pre-registered failure
     mode).
BC7  (S7) the structure determines the scale kappa = pi at the
     DENSITY layer; its FE layer is provably kappa-blind.
     EXCLUDES: any FE/duality-only structure (BB's vacuity guard:
     reproducing the functional equation determines nothing); the
     scale must be read by a comb-vs-continuum density comparison.
BC8  (S8) the unit is ONE class, counted once, whose Fourier dual is
     the continuum unit; inserted by hand the repair has ZERO SLACK
     deep. EXCLUDES: padded/atomic insertions (they fail BC3 at
     finite scale); any unit with slack (SS.4: surplus = positive
     hole = contradiction).
BC9  (S9) the archimedean coordinate is SIGNED and jointly cancels;
     admissible directions isolate breaking slots.
     EXCLUDES: any positive-definite archimedean block; any scalar
     aggregate certificate; the unit must couple inside the
     inequality, not dominate it.
BC10 (S10) per-place oscillation amplitude follows the Gamma_R decay
     ladder; all structural slack lives at p in {2, 3} entry.
     (Consequence of BC1; kept as an independent check because it is
     what the census sees.)
BC11 (S12) every BC above must be UNFORMABLE without unique
     factorization (Epstein/DH die at the carrier).
     EXCLUDES: any structure that would also produce these shadows
     for DH/Epstein - the Euler product must be load-bearing, not
     decorative (the F1-litmus of the strategy reframe).
BC12 (S4/S6 jointly) the deficits are sub-quantization continuum
     objects (all certified |deficits| in (0, log 2)).
     EXCLUDES: h^1/count reinterpretations (RR F3): the unit is not
     a cardinality; tr cannot be a cardinality-valued trace on the
     deficit channel.
```

CONSTRAINT-SATISFACTION FORM: find (C, tr) such that (a) tr's
per-place scale flow has BC1's exact Fourier data; (b) tr's charge
ledger is integral with the -1/0 dichotomy (BC2); (c) tr's global
assembly is BC4-threaded through BC5's mean channel reading BC7's
kappa; (d) tr is signed per BC9 with zero slack per BC8; (e) at least
one pairing in C has TWO independent evaluations per BC6; (f) the
whole package consumes unique factorization per BC11.

## 6. First characterization pass (honest grades)

THE MINIMAL STRUCTURE SATISFYING BC1-BC5, BC7-BC12: Tate's thesis at
the real place, read backwards - i.e. (R, +, e^{-pi x^2}, Mellin)
with the product formula as the cross-place identification. Checked
clause by clause: BC1 is NS1's theorem (the Gaussian's Mellin data IS
Gamma_R; that is Tate's local computation); BC2-BC3 are the Poisson
bookkeeping of full cosets vs the half-line (SS.1 vs NN's -1/2 strip);
BC4/BC5's threading-through-means is the product formula on the idele
class group; BC7 is the classical Gamma_R normalization (kappa = pi
folded); BC8 is delta_0 <-> Lebesgue; BC9 is the EF's W_inf read in
lattice coordinates (HH); BC10 follows from BC1; BC11 is satisfied
trivially (no monoid, no Tate); BC12: the EF archimedean term is a
continuum density, not a count.

VERDICT ON THE NULL HYPOTHESIS (F1-fork, stated plainly): the
minimal solution to BC1-BC5 + BC7-BC12 IS the explicit formula's own
archimedean apparatus read backwards. NS1 makes this exact rather
than impressionistic - the silhouette is EF-archimedean data TO ALL
ORDERS, so no shape measurement of Delta_p, however refined, can
distinguish the spine from the EF reading itself. The dossier's shape
rows do not over-determine the EF; they CONFIRM the unit's identity
as the EF's archimedean term (which doc 35 already said in words).

THE SMALLEST BC SUBSET FORCING NON-EF STRUCTURE: {BC6}. It is the
only clause the EF-read-backwards fails - in the EF, <W, g_i>'s value
at the prime side has exactly one evaluation (the supply one); the
zero-side "second evaluation" is the THEOREM TO BE PROVED, not a
structure in hand. Every other BC is satisfiable by classical Fourier
analysis on the adeles. Corollary for the program: the inverse
problem is NOT under-determined in an interesting way on the shape
axis; it is determined-and-classical there, and ALL the residual
content of the missing object lives in the single multiplicity demand
BC6 - with BC4 as its quantitative enforcement (the second evaluation
must move surplus cross-place at fixed scale, which is exactly what a
Lefschetz-type global trace does and a per-place formula cannot).

What this buys LS3/LS4 (the spine): the demand-side spec is now
closed-form. The spine's trace must restrict, at each place, to a
function whose Fourier modes are -Re Gamma_R(2 pi i n/log p)/log p -
no freedom remains in the unit's shape; the entire construction
problem is the EVALUATION STRUCTURE (BC6) and its threading (BC4).
Equivalently: build any category with a trace that (i) is forced to
the Gaussian fixed unit (LS3), and (ii) computes the pairing twice
(LS4/C6); the dossier proves everything else is then automatic or
already classical.

G-CH2 FULL-LEDGER SCORE of the named minimal structure (Tate-at-oo
read backwards), against the six clauses: C1 PASS (kappa = pi is its
normalization, density layer); C2 PASS per place; C3 NOT ADDRESSED
(no rational/Anderson content; the dossier has no C3 shadow to test
against - recorded gap); C4 PASS as data (it IS W_inf), but supplies
no mechanism; C5 PASS (Gaussian self-duality = homogeneous FE); C6
FAIL (one evaluation). Against the FF five: index shape PASS
(carried by the certified face, not by Tate); integrality FAIL (the
EF's archimedean term is not integer-structured); effectivity FAIL
(no h^0 >= 0 mechanism); monoid family PASS (trivially, via the
carrier); growing observable FAIL (no second evaluation to grow
against). Score 7/11: the null structure is a SHADOW-COMPLETE,
MECHANISM-EMPTY solution - exactly what "read backwards" should
score. G-CH3 (second-evaluation audit of THIS memo): NS1's c_n have
two computation routes (DFT of the lattice sum vs Gamma closed form)
but both are supply-side/analytic - NOT an independent evaluation in
the C6 sense; no escalation.

## 7. G-INT6 ledger

```text
input                          choices spent
shadow inventory               0 new (the nine banked memos; decisive
                               numbers RECOMPUTED, not trusted)
NS1 closed form                0 new (hand Mellin derivation of the
                               banked deficit d(x); Gamma enters as
                               the integral's value, not as EF import)
NS2 disjointness               0 new (unique factorization, exact)
NS3 parity/amplitude           0 new (corollary of NS1)
clause labels C1-C6            doc 34 sec 2 + doc 37 (fixed, cited)
DFT grid N = 128, M = 120      calibration (registered; tails certified
                               into ball radius)
banked-value tolerances        registered before run 1 (printed-digit
                               precision; WW9's 25% comparison flagged)
kappa = pi, HH eigmin          COMPARISON/IMPORT-FLAGGED (not derived,
                               not recomputed respectively)
zeros                          NONE (no fork_lib, no freeze; every
                               quantity congruence/entry/period-
                               determined; z < 3 certified at source)
witness fixes (4)              computational, disclosed in sec 4; no
                               predicate touched
```

## 8. Honest limits

- The dossier consolidates SINGLE-PLACE and small-window certificates;
  "global feasibility" (S5) is the scanned-window measurement of RR,
  re-witnessed at the decision scale only (a = 4.96). Nothing here
  proves the global aggregate positive for all a.
- NS1 is proved as an identity of the QQ deficit object; its
  promotion to "the unit's shape" assumes doc 35's identification of
  Delta_p as the unit's computed shadow - the dossier's standing
  premise, not a new theorem.
- NS2's covariance numbers are float-grade records (flagged); the
  certified content is the exact frequency disjointness.
- The null-hypothesis verdict (sec 6) is a characterization at the
  level of the twelve BCs as stated; a future BC outside this dossier
  (e.g. a computed C3 shadow) could change the minimal-structure
  analysis. BC6's "excludes everything in hand" is the program's own
  no-go corpus speaking, not an abstract impossibility proof.
- The erfc display correction (S4) affects TT's prose only; no TT
  gate pinned the 4th digit.
- The clause-C3 column of the inventory is EMPTY: the dossier cannot
  currently constrain the rational/Anderson layer at all. This is the
  one axis on which the inverse problem remains shapeless.

## 9. Hand-off (for the lead)

```text
DOSSIER:   12 rows S1-S12, all recomputed in ONE witness (WW1-WW14,
           ALL PASS, exit 0, 0.5 s, deterministic): mean identity;
           NS1 shape law (NEW, the headline); charge dichotomy
           -1/0; payment schedule (e^{-a}/2, 1-2e^{-pi}, 1-6T(1),
           rho erfc(sqrt pi) = rho * 0.0121889 - TT prose digit
           corrected); threading (per-place infeasible / global
           +3.03e-2); depth wall (155.7x / 3514x at a = 8); kappa =
           pi (flagged); FE-homogenizer (+1, exact); joint
           cancellation; amplitude ladder (NEW); disjoint spectra
           (NEW); carrier guard.
NEW:       NS1 - Delta_p's COMPLETE Fourier data is Gamma_R on the
           imaginary axis: c_n log p = -Re Gamma_R(2 pi i n/log p),
           certified to ball precision at 12 (p, n) pairs after a
           hand Mellin derivation; QQ's measured amplitudes now
           DERIVED. The silhouette is analytically complete.
INVERSE:   posed as BC1-BC12 with per-BC exclusions (sec 5).
NULL:      the minimal solution to all BCs EXCEPT BC6 is Tate's
           thesis at the real place read backwards - the F1-fork
           null hypothesis is CONFIRMED for the entire shape axis;
           {BC6} alone (with BC4 as its quantitative arm) forces
           non-EF structure. The spine's remaining unknown is the
           evaluation structure, not the unit's shape.
WITNESS:   prime_ww_silhouette.py (WW1-WW14, ALL PASS, exit 0,
           deterministic x2 diff-identical; 4 disclosed computational
           fixes, no predicate touched). Inherited reruns before any
           work: prime_qq_native_face_index, prime_ss_ku_inequality_
           proof (both ALL PASS, exit 0).
G-CH1:     the footnote that should be a gate: NS1 means ANY future
           candidate unit can be killed or passed by a 12-number
           Fourier test - propose "BC1 conformance" as a standing
           gate for every LS3/LS4 candidate trace.
```
