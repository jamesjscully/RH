# UU - Face-hunt stress S3: the 2D WEIGHT x SCALE Castelnuovo on the ku face

Status: fresh-context worker UU, 2026-06-11. Doc 36 stress item S3 (the
actual index content of the surviving face). Required reading executed in
order: doc 36 (I am S3), PP-ku-face.md IN FULL, doc 23 secs 5-6 (corrected
Castelnuovo: bidegree correction, k-dependent diagonal; W's max-Gram
repair), W-monoid-frobenius.md sec 5 (max-Gram lemma + geometric-family
certificate), HH-weil-restriction-fork.md (Thm HH.1: Lambda = -<d,d>;
dual-cone form), QQ-native-face.md (the gap object Delta_p),
NN-graph-class-test.md (the kill template). Inherited witnesses rerun by
me BEFORE any new work: prime_pp_ku_face_index (ALL PASS KU1-KU9, exit 0,
freeze hash matches PP's 02250df1...), prime_int_gc_k3_barnes_rank
(ALL PASS KG1-KG5, exit 0 - the Barnes d2 = h^2/2 rank-2 carrier, the
program's evidence that the global object holds a genuine 2-parameter
quadratic slot).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_uu_ku_castelnuovo_2d

Sections 0-2 (dictionary, construction, hand derivations, gates,
registered predictions) were written BEFORE the witness was first run.
DISCLOSURE (PP/NN precedent): sec 1 contains design-stage hand
derivations (the d-frame Gram, the two Schur/inertia identities, the
override-posing signature theorem, the discriminant inequality and its
entry-corner/deep asymptotics, float estimates of the locus a*(q)). They
are derivations, not fits; the witness checks them fail-closed and a
mismatch is a FAIL.

Discipline: F-a - no zeta values, no zeta continuation anywhere; margins
via PP's certified coset-Poisson dual route (machinery re-certified
against PP's printed values, gate UU1). Zeros enter ONLY via
fork_lib.zeta_gammas, ONLY after the sha256 freeze, COMPARISON ONLY
(gate UU6, II protocol verbatim). Carrier guard UU7. G-INT6 ledger sec 5.

## 0. The question and the registered fork

THE FF MODEL (the thing RH-for-curves actually uses): Castelnuovo is a
2-parameter statement. On C x C one takes D = m Delta + n Gamma_{F^i};
the index inequality d(D) <= 2 d1 d2, applied along the Frobenius family
as i varies, makes 2 d1(D) d2(D) - D^2 a PSD quadratic in (m, n); RH
falls out of the DISCRIMINANT: (Delta'.Gamma')^2 <= (Delta'^2)(Gamma'^2),
i.e. |a_i| <= 2g q^{i/2}. Two ingredients carry all the content:
(i) the Hodge-index SHAPE (signature (1, rho-1)); (ii) one Gram entry -
Delta . Gamma_{F^i} = #Fix(F^i) - that is INDEPENDENTLY a spectral sum
(Lefschetz: q^i + 1 - sum alpha^i). The inequality then constrains the
spectrum because the supply data (degrees, genus) bound an entry that
zeros compute.

THE ku FACE HAS BOTH PARAMETERS NATIVELY: WEIGHT (the lcm-ladder
direction, where PP's certified 1D inequality lives - 527 margins, zero
negatives, deep law +e^{-a}/rho_q) and SCALE (the theta/window direction;
the geometric family {q^i} is W sec 5's certified Lorentzian max-Gram).
REGISTERED RISK (doc 36 / PP sec 6): the deep-margin MARGINALITY - the
1D inequality is evasion, not surplus; zero slack at infinity. The
quadratic/discriminant step needs slack SOMEWHERE.

PRE-REGISTERED VERDICT TABLE (task card, fixed before any computation):

```text
(U-a) the discriminant locus, computed and FROZEN, tracks zero positions
      when compared post-freeze (shock criterion: z >= 4 at >= 3 of the
      first 5 gammas on a decision series) -> the first index-grade
      spectral contact. THE escalation: NN-grade scrutiny, triple-check
      (3 deterministic reruns + perturbation control) before believing.
(U-b) the discriminant is congruence/entry-determined like everything
      else on this face - the 2D form is SUPPLY-GRADE only; characterize
      exactly what spectral-grade content would need (feeds the preprint
      either way).
(U-c) the 2D form fails the Hodge-index shape outright (the deep-margin
      marginality kills the quadratic step) - the registered risk
      realized; option 2's survivor is 1D-only.
```

FAIL-CLOSED: (U-b) and (U-c) are full-value; nothing below is tuned to
avoid them.

REGISTERED OVERALL PREDICTION (design-stage, both ways carried):
(U-b), with the U-c MECHANISM confirmed in its quantitative clause. The
shape question will turn out to be posing-dependent and entry-determined
in BOTH branches (sec 1.3: override posing Lorentzian for ANY positive
margin; append posing non-Lorentzian by exactly the unpaid atom
Lambda(q) - m+); the discriminant inequality will hold only in a small-q
entry corner (predicted q in {3, 4}, a <~ 3, with q = 8 the borderline
candidate) and die deep with needed Frobenius depth ~ rho_q Lambda_p^2
e^a against available window depth a / log q - exponential vs linear.
If the frozen series shock: (U-a), triple-check duty. If even the entry
corner is empty AND the override signature breaks: (U-c) outright.

## 1. The dictionary and the construction (hand derivations, before any run)

### 1.1 The two directions and the family Gram (G-INT6 inline)

Fix a ku cell q = p^j (prime power, j >= 1) at admissible scale
a >= log(q+1). Ambient lattice: the place-p tower R^{0..N} of classes
[p^0], ..., [p^N] with the certified index face M = (log p) MAX (HH.1's
exact face; W's E-correction recorded as variant, gate UU8).

WEIGHT-direction class (forced dictionary, HH.1 transposed to the global
cell): W = d_j = [p^j] - [p^{j-1}], the lcm-ladder step that carries the
cell's atom: Lambda(q) = log p = -<d_j, d_j>_M (HH.1 at w = 1; PP KU7:
on the global ladder the atom is the single deferred top cell). THE
CANDIDATE SELF-PAIRING (the task's instruction; logged choice C1):
replace -Lambda(q) by -m+(q, a) - PP's 1D inequality value standing in
Lambda's slot, sign per HH.1 (Lambda = -<d,d>: the inequality value is
spacelike; PP's census makes it > 0 admissibly).

SCALE-direction classes (forced family, FF's {Gamma_{F^i}}): the
geometric family g_i = [q^i] = e_{ji}, i = 0..i_max, W sec 5's certified
max-Gram <g_i, g_l> = (log q) max(i, l). WINDOW CAP (forced, NN/HH's
admissibility transposed): g_i is admissible iff its degree sits in the
window, i <= i_max(q, a) = floor(a / log q).

CROSS TERMS (forced once W, g_i live in the same certified face - zero
choices): c = M d_j, i.e. <d_j, [p^k]>_M = log p * 1_{k <= j-1}; hence
<W, g_i>_M = log p * delta_{i,0} for the {q^i} family.

### 1.2 The d-frame and the two posings

In the d-frame {e_0 = [1], d_1, ..., d_N} the certified face is EXPLICIT
(HH.1): <e_0, e_0> = 0 (null unit), <e_0, d_k> = log p (all k),
<d_k, d_l> = -(log p) delta_kl. Two inequivalent readings of "the margin
is the candidate self-pairing":

(A) OVERRIDE (the honest 2D posing): the form F' = the certified face
with the single diagonal entry <d_j, d_j> moved from -log p to
-m+(q, a). A one-parameter deformation of the certified face along the
cell's own diagonal slot; at m+ = log p it IS the face.

(B) APPEND (the strawman, tested to kill it cleanly): W adjoined as an
(N+2)-th vector with self-pairing -m+ alongside the unmodified face
(cross row c = M d_j).

### 1.3 Hand derivations (design-stage, fail-closed targets)

(D1) SCHUR IDENTITY, APPEND: the bordered Gram [[-m+, c^T], [c, M]] has
Schur complement s = -m+ - c^T M^{-1} c = -m+ + (d_j^T M d_j ... sign:
c = M d_j so c^T M^{-1} c = d_j^T M d_j = -log p):

    s = Lambda(q) - m+(q, a).

By Haynsworth, inertia(append) = inertia(M) + inertia(s) = (1, N) +
(1, 0) whenever m+ < Lambda(q): signature (2, N) - NOT Lorentzian. PP's
margins (max 0.557 at q = 3 entry, vs Lambda(3) = 1.0986) NEVER reach
Lambda: REGISTERED: the append posing fails the Hodge-index shape at
every census cell, by exactly the unpaid atom s = Lambda(q) - m+ > 0.

(D2) SIGNATURE THEOREM, OVERRIDE: in the d-frame F' has d-block
diag(-Lambda, ..., -m+, ..., -Lambda), negative definite for ANY
m+ > 0; Schur onto e_0: 0 - Lambda^2 sum_k 1/(d-block_kk) =
+Lambda^2 ((N-1)/Lambda + 1/m+) > 0. Inertia (1, N): LORENTZIAN for
every m+ > 0, with NO lower bound on m+ required. Consequences, both
edged: the shape HOLDS on the honest posing - but it holds for any
positive diagonal whatsoever, so the shape carries ZERO information
about the margin's size; and as a -> inf, m+ -> e^{-a}/rho_q -> 0: the
d_j eigendirection slides onto the light cone - the form never
degenerates at finite a (PP's 527 certified positives) but its
spacelike floor in the weight direction is exponentially marginal:
"evasion not surplus", now as a signature statement.

(D3) THE OVERRIDE GRAM OF THE 2D FAMILY (exact in the d-frame, for
i >= 1, q = p^j):

    A' = <W, W>'     = -m+(q, a)
    B' = <W, g_i>'   = Lambda_p - m+(q, a)      (Lambda_p := log p;
                       = Lambda_p at i = 0: the unit class keeps HH.1's
                       null-frame pairing)
    C' = <g_i, g_i>' = i log q + (Lambda_p - m+(q, a)).

Sanity: m+ = Lambda_p restores B' = 0... no: restores the certified
face values <d_j, [p^{ji}]> = 0 for ji >= j? NO - check: at m+ =
Lambda_p, B' = 0 and C' = i log q: MATCHES the face (cross term of d_j
against higher classes is 0, MAX diagonal i log q). The deformation
puts the unpaid atom Lambda_p - m+ INTO THE CROSS TERM - the Weil slot
where the fixed-point count sits is occupied, on the ku face, by
exactly the deficit between the atom and the 1D margin.

(D4) THE DISCRIMINANT INEQUALITY (the FF extraction transposed; the
decision object). Weil's discriminant condition is
(Delta'.Gamma')^2 <= |Delta'^2| |Gamma'^2| with the Gamma'-budget known
from degrees (2g q^i). ku transposition (logged dictionary C2: the
scale-diagonal budget = window degree + Castelnuovo's log 2; note the
face SATURATES tropical Castelnuovo: log(q^i + q^l) = max(i,l) log q +
log(1 + q^{-|i-l|}), per-entry slack log 2 on the diagonal, -> 0 off it
- zero slack at infinity in the family direction too):

    DISC(q, a, i):   (Lambda_p - m+)^2  <=  m+ * (i log q + log 2),
                     i <= i_max(q, a) = floor(a / log q), i >= 1.

REGISTERED census predictions (floats, design-stage; witness decides
with arb): holds at q = 3 entry (LHS 0.293 vs RHS 0.998, ratio 0.29)
and q = 4 entry (0.133 vs 0.684, ratio 0.19); FAILS at q = 9 entry
(0.984 vs 0.309, 3.2x), q = 5 entry (~3x), q = 121 entry (~120x), and
at EVERY q for a >= 4. Borderline candidate: q = 8 entry (~1.3x,
fails). Locus a*(q) (last admissible a where DISC holds, at i = i_max):
a*(3) ~ 2.45, a*(4) ~ 2.95, empty for all other census q (moderate
confidence; the census itself is the verdict input, any surprise q
reported not failed).

(D5) THE DEEP DEGENERATION AND WHERE SLACK WOULD HAVE TO LIVE. DISC at
i = i_max needs m+ >= (Lambda_p - m+)^2 / (a + log 2 - ...) ~
Lambda_p^2 / a. Deep law (PP KU5): m+ = e^{-a}/rho_q (1 + o(1)). So the
needed Frobenius depth is

    i* log q = (Lambda_p - m+)^2 / m+  - log 2  ~  rho_q Lambda_p^2 e^a,

EXPONENTIAL in the window, against the available i_max log q <= a,
LINEAR. The quadratic step's required slack grows like e^a; the ku face
supplies a. The deep-margin marginality is therefore EXACTLY the death
of the 2D step: the only slack anywhere on the face is the small-q
entry corner (max margin/atom ratio: m+(3, entry)/Lambda(3) = 0.507,
decaying both in q (~0.74/(q log p)) and in a (e^{-a})) - the same
small-place corner as NN's surviving cells (p <= 3) and W's low-weight
certificate holes (p in {2, 3}).

(D6) SPECTRAL-GRADE CHARACTERIZATION (the U-b clause, testable): every
entry of every posing is an explicit function of (Lambda_p, log q, i,
m+(q, a)) - congruence/entry-determined data (PP KU9: the margins are
z < 3 against the zeros). Weil's extraction works because ONE entry
(Delta.Gamma_{F^i} = #Fix) has an INDEPENDENT spectral evaluation
(Lefschetz trace). The ku face's corresponding entry is B' = Lambda_p -
m+: supply data. What spectral grade would need: a second, independent
evaluation of <W, g_i> as a fixed-point/trace count - i.e. the
assembled pairing whose value is sum_rho x^rho-type, the missing
timelike unit at infinity that HH sec 3 / doc 31 exit B / BB triply
name. The ku face's internal subtraction supplies CARDINALITY (it
homogenized the FE); it supplies no trace.

### 1.4 What is NOT posed here

No new pairing is constructed; no zeta input; the E-correction
(log(1 - p^{-|i-l|})-type) is a recorded variant only (UU8); the
truncated/honest face (PP sec 1.5) is out of scope (S2's item); w > 1
weights (W's per-weight certificates) recorded at one spot check, no
decision weight.

## 2. PRE-REGISTERED GATES (written before the first run)

Evaluation rules fixed in advance: flint arb prec 300 for all decision
quantities (margins via PP's dual route verbatim); exact
Fraction-coefficient arithmetic for every identity in the certified
face (entries are integer multiples of log p: checked at coefficient
level); sign decisions only when the arb ball resolves the sign;
float-grade (flagged) only in the UU6 spectra. Scales: census grid =
PP's KU4 grid (a = log(q+1) + 0.15 j, j = 0..19, plus {5, 8}); locus
grids step 0.01. i_max via arb ball of a/log q certified to exclude
integers (else a nudged by 1e-9, calibration).

```text
UU1 INHERITED MARGINS (machinery re-certification): m+(q, a) recomputed
    by this witness's copy of PP's dual route matches PP's printed
    values: m+(121, 4.96) = +6.4682e-3, m+(25, 3.26) = +3.2728e-2,
    m+(9, 4.96) = +8.9762e-3, entry floors m+(3) = 0.557, m+(9) =
    0.107, m+(121) = 6.249e-3 (rel < 2e-3 vs printed precision); all
    arb-positive. FAIL: any mismatch.
UU2 THE FACE IDENTITIES (exact, Fraction coefficients): c = M d_j
    (cross row forced); d_j^T M d_j = -log p (HH.1); d-frame Gram
    (0 | Lambda 1^T / Lambda 1 | -Lambda I) for N <= 12, j <= 4;
    2D-family entries (D3): B' = Lambda_p - m+ (i >= 1), B'_0 =
    Lambda_p, C' = i log q + (Lambda_p - m+), via two routes (d-frame
    expansion vs direct override sum), exact in the Lambda-coefficient
    + arb in the m+ part, rel < 1e-40. FAIL: any mismatch.
UU3 THE SHAPE, BOTH POSINGS (the Hodge-index gate):
    (a) OVERRIDE: inertia of F'(q, a, N) = (1, N) for q in {3, 4, 5,
        9, 25, 121} x a in {entry, entry+1, 5, 8} x N in {4, 8, 12}:
        via the exact Schur chain (d-block ND iff m+ > 0, arb; e_0
        Schur complement > 0, arb) AND a float eigenvalue cross-check
        (flagged). REGISTERED: Lorentzian everywhere, for any m+ > 0 -
        the shape carries no margin information.
    (b) APPEND: s = Lambda(q) - m+(q, a) arb-certified POSITIVE on the
        full PP census grid (24 prime powers <= 169, all admissible a):
        signature (2, N) - not Lorentzian, failure = the unpaid atom.
    STRUCTURAL GATE: all signs arb-resolved; the posing-dependence
    (trivially-true vs trivially-false, both entry-determined) is the
    shape verdict. FAIL: unresolved sign, or a (2,N) override / (1,N+1)
    append instance (either would refute D1/D2 - reportable shock).
UU4 THE DISCRIMINANT CENSUS (decision gate): DISC(q, a, i_max) signs
    arb-resolved on the full PP census grid. REGISTERED: holds ONLY in
    the small-q entry corner (q in {3, 4}, a <= ~3; q = 8 borderline,
    either way reported); 0 holds at a >= 4; deep ratio r = LHS/RHS
    matches rho_q Lambda_p^2 e^a / (i_max log q + log 2) within 5% at
    a = 8 for q in {3, 9, 121}. FAIL: unresolved sign or deep-law
    clause; the hold/fail census itself is the verdict input
    (surprises reported).
UU5 THE LOCUS + THE NEEDED-DEPTH WALL:
    (a) a*(q) computed (float scan step 0.01, arb-certified at the
        bracketing points and decision spots, i = i_max(a)) for all
        census q; gate clauses: a*(3) in (2.3, 2.6), a*(4) in
        (2.8, 3.1), empty for all q >= 9 and q in {5, 7}; q = 8
        reported either way (the registered borderline); sawtooth from
        the i_max floor handled: a* = last sign change;
    (b) needed depth i* log q = (Lambda_p - m+)^2/m+ - log 2 certified
        EXPONENTIAL: |i* log q * e^{-a} - rho_q Lambda_p^2| <
        0.05 rho_q Lambda_p^2 at a = 8, q in {3, 9, 121}; available
        depth a (linear): the wall printed as the slack-location
        statement. FAIL: any clause.
UU6 FREEZE + ZERO COMPARISON (II protocol verbatim, PP KU9 pattern):
    a-grid [0.5, 8], 512 pts (float-grade, flagged): T1 = r(3, a),
    T2 = r(9, a) (discriminant ratios at i_max, admissible part, 0
    pre-entry), T3 = sum_{q <= 32, admissible} log p(q) * (RHS - LHS)
    (assembled discriminant margin; EF-staircase-exposed, record
    only); locus values a*(3), a*(4) included in the frozen JSON.
    sha256 printed BEFORE any fork_lib import; THEN zeta_gammas(100),
    z at gamma_1..5 vs MAD background gamma in [5, 60] (PP's
    exclusions verbatim). SHOCK CRITERION (-> U-a, escalate +
    triple-check): z >= 4 at >= 3 of first 5 gammas on T1 or T2.
    REGISTERED EXPECTATION: z < 3 on T1/T2 (smooth functions of
    congruence/entry data). GATE: freeze ordering + comparison
    computed.
UU7 CARRIER GUARD (exact integers; PP KU8 + new clause): Epstein
    x^2+5y^2: 36 = 4*9 = 6*6, v(36) in {0, 2} -> no prime-power sieve
    -> no cell address AND no degree-separated geometric family {q^i}
    (no valuation -> no max-Gram address): BOTH directions of the 2D
    form unformable; DH: no carrier monoid (bookkeeping). FAIL: any
    clause.
UU8 VARIANTS (record only, no decision weight): E-corrected cross/
    diagonal (W sec 5.2) at q = 9, a = 5: entries and the DISC ratio
    shift printed; the w = 2 weight spot check at p = 3; the t-window
    diagnostic: is m+(q, a) inside W's certified halfwidth
    (log p)/4 - 2x/(1-x)^2, x = 1/p (noting w = 1 certificate holes at
    p in {2, 3})? Census fractions printed.
```

Registered overall verdict logic (before the run): IF UU3 confirms the
posing-split (D1/D2) AND UU4/UU5 confirm the entry-corner-only census
with the exponential wall AND UU6 shows no shock: (U-b) as the primary
verdict - the 2D form is supply-grade; the discriminant locus a*(q) and
every census sign are entry-determined; the U-c mechanism (deep-margin
marginality kills the quadratic step) is confirmed as the REASON the 2D
form carries no spectral content beyond the entry corner; option 2's
survivor remains 1D-plus-corner. IF UU6 shocks: (U-a), escalate with
triple-check duty before believing. IF the override shape breaks or the
corner is empty: (U-c) outright. Any refuted hand value: FAIL, report.

---- verdict sections written after the runs ----

## 3. VERDICT: (U-b) AS REGISTERED - THE 2D FORM IS SUPPLY-GRADE; THE
## U-c MECHANISM (DEEP-MARGIN MARGINALITY) IS CONFIRMED AS THE EXACT
## REASON THE QUADRATIC STEP DIES; NO ZERO CONTACT (U-a NOT TRIGGERED)

Witness ALL PASS (UU1-UU8, exit 0, deterministic across 3 runs,
diff-identical logs /tmp/uu_run{1,2,3}.log; freeze 3d3d291f45f7cd74d914
21ea147638246c1d40d4d5c9e9d7e79be54bafaed77f). No gate touched after the
first run. Hand-prediction scorecard: D1/D2/D3 exact (2.1e-90 worst);
deep ratio law dev <= 0.13% (gate 5%); a*(3) = 2.357 (window 2.3-2.6),
a*(4) = 2.930 (window 2.8-3.1); ONE design float guess wrong and
disclosed: D4 guessed q = 8 fails at entry by ~1.3x - it HOLDS there
(m+(8, entry) higher than the interpolation guess); q = 8 was registered
report-only either way, so no gate was affected.

```text
THE SHAPE (UU3, the Hodge-index question): POSING-SPLIT, exactly as
  derived - and therefore CONTENT-FREE:
  OVERRIDE (the honest posing: the certified face with <d_j, d_j>
    moved from -Lambda to -m+): Lorentzian (1, N) for ANY m+ > 0, by
    the exact Schur chain. PP's 527 certified positives make the shape
    hold everywhere admissible - but it would hold for any positive
    diagonal whatsoever: zero information about the margin's size.
  APPEND (W bordered onto the unmodified face): signature (2, N) at
    527/527 census cells, Schur complement s = Lambda(q) - m+(q, a)
    arb-certified positive everywhere: fails by exactly the UNPAID
    ATOM. The Lorentzian shape would need m+ >= Lambda(q): the 1D
    inequality would have to pay the full von Mangoldt weight; it
    pays at most 0.557 of 1.0986 (q = 3 entry), e^{-a}/rho_q deep.
THE WEIL SLOT (UU2, exact): in the override posing the cross term is
    B' = <W, g_i>' = Lambda_p - m+(q, a)  (all i >= 1):
  the slot where Weil's fixed-point count sits is occupied, on the ku
  face, by the atom-minus-margin deficit. Supply data, not a trace.
THE DISCRIMINANT CENSUS (UU4): (Lambda_p - m+)^2 <= m+ (i_max log q +
  log 2) holds at 15 of 527 cells, ALL in the small-q entry corner:
  q = 3 (a <= 2.29), q = 4 (a <= 2.81), q = 8 (entry only) - the
  prime-2/3 small towers, the SAME small-place corner as NN's
  surviving cells and W's low-weight certificate holes. Zero holds at
  a >= 4. Sawtooth structure measured: q = 3 fails in a sliver just
  below the i_max jump at 2 log 3 = 2.197 and resumes after; q = 4
  likewise below 2 log 4 - the hold/fail boundary is literally
  floor(a / log q): congruence/entry-determined.
THE LOCUS (UU5a, frozen pre-zeros): a*(3) = 2.357, a*(4) = 2.930,
  a*(8) = 2.308, EMPTY for q in {5, 7} and all q >= 9 (arb-certified
  at entry, i_max jumps, coarse grid). Nothing spectral about these
  numbers: they are Lambert-W-type functions of (Lambda_p, log q,
  rho_q) through PP's margin law.
THE DEEP DEATH (UU4/UU5b, the registered risk realized quantitatively):
  failure ratio r = rho_q Lambda_p^2 e^a / (i_max log q + log 2) to
  0.13% at a = 8 (r = 143 at q = 3, 384 at q = 9, 3071 at q = 121).
  Needed Frobenius depth i* log q = rho_q Lambda_p^2 e^a (certified
  +-5%): 1197 vs available 7.69 (q = 3, a = 8); 16854 vs 4.80
  (q = 121). EXPONENTIAL demand, LINEAR supply.
ZEROS (UU6, II protocol): freeze BEFORE fork_lib; z at gamma_1..5:
  T1 max -0.5, T2 max 1.5, T3 max 1.2. No shock; U-a NOT triggered.
  The discriminant locus is entry-determined, not zero-positioned.
RECORD (UU8): for p >= 7 the census margins sit INSIDE W's certified
  t-window (40/44, 44/44, 43/43 at p = 7, 11, 13): the margin-as-
  diagonal-shift is window-compatible at large p; the w = 1
  certificate holes at p in {2, 3, 5} are W's known low-weight holes.
```

## 4. What the test settles

(i) THE 2D FORM EXISTS AND IS WELL-POSED on the ku face - the override
posing is a genuine one-parameter deformation of the certified
Lorentzian face along the cell's own diagonal slot (at m+ = Lambda it
IS the face), Lorentzian everywhere admissible, with exact closed-form
entries. That much of doc 36's S3 stands.

(ii) BUT IT CARRIES NO INDEX-GRADE SPECTRAL CONTENT, for an exactly
characterized reason (the U-b clause): every entry of every posing is
an explicit function of (Lambda_p, log q, i, m+(q, a)) - all
congruence/entry-determined (PP KU9 + UU6: z < 3 throughout). Weil's
discriminant extracts RH because ONE Gram entry - Delta . Gamma_{F^i}
= #Fix(F^i) - has a SECOND, independent, spectral evaluation
(Lefschetz). The ku face's corresponding entry is B' = Lambda_p - m+:
it has exactly one evaluation, the supply one. SPECTRAL-GRADE WOULD
NEED: an independent trace/fixed-point evaluation of the weight-class-
against-Frobenius-family pairing - i.e. precisely the missing timelike
unit at infinity (HH sec 3's conserved defect W_inf; doc 31 exit B;
BB's archimedean Poisson unit; QQ's Delta_p in count dress). The 2D
posing does not create that object; it RELOCATES its absence into the
cross term of a quadratic form. This is the preprint-grade
characterization the task ordered either way.

(iii) THE REGISTERED RISK IS REAL AND QUANTIFIED (the U-c mechanism
inside the U-b verdict): PP's "evasion not surplus" is exactly fatal to
the quadratic step. The deep law m+ -> e^{-a}/rho_q makes the weight
diagonal degenerate onto the light cone; the discriminant inequality
then demands Frobenius depth rho_q Lambda_p^2 e^a against a window that
supplies a/log q. The 2D step does not fail by a constant - it fails by
e^a vs a. No re-posing that keeps (a) the margin as the weight budget
and (b) window admissibility of the scale family can cross that wall.

(iv) WHERE THE SLACK LIVES (item 3 of the task): only the small-q entry
corner - 15 of 527 cells, q in {3, 4, 8} (towers of 2 and 3), a < 3,
max budget ratio m+/Lambda = 0.507 at q = 3 entry, gone by a ~ 3. The
ku face's only atom-scale slack is the entry phase of the smallest
cells at the smallest places. Echo logged (not a claim): this is the
third independent appearance of the p in {2, 3} small-place corner
(NN's safe cells, W's low-weight holes, UU's discriminant corner).

## 5. G-INT6 ledger

```text
input                          choices spent
weight class W = d_j           forced (HH.1 dictionary; PP KU7: the
                               cell's atom is the deferred ladder step)
margin as self-pairing, sign   C1 (the task's instruction): m+ stands
                               in Lambda's slot per Lambda = -<d,d>
scale family {q^i}             forced (FF's {Gamma_{F^i}}; W's banked
                               certified family)
window cap i <= a / log q      forced (NN/HH admissibility transposed)
cross terms                    forced (c = M d_j, exact, zero choices)
override-vs-append             BOTH posed and decided; neither chosen
scale budget i logq + log 2    C2: window degree + Castelnuovo's 2
                               (the face saturates tropical Castelnuovo
                               at log 2 per diagonal entry)
margins m+(q, a)               PP's machinery verbatim, re-certified
                               (UU1) - no retuning
zeros                          fork_lib.zeta_gammas, post-freeze,
                               comparison only (UU6)
grids/windows                  calibration, registered before run 1
                               (two pre-run design fixes: deep-ratio
                               denominator i_max log q + log 2, and
                               q = 8 demoted to report-only - both
                               edited before the witness existed)
```

## 6. Honest limits

- The discriminant inequality (D4) is MY transposition of the Weil
  extraction (choice C2 for the scale budget); a different budget
  dictionary shifts the corner boundary but not the e^a-vs-a wall
  (UU5b is budget-independent: it compares (Lambda - m+)^2 / m+
  against ANY linear-in-a supply).
- "Supply-grade" is certified at the census level (527 cells, 24 prime
  powers to 169) plus the frozen-series comparison; it is not a proof
  that no reading of the 2D form ever touches zeros - it is the
  statement that THIS form's entries and locus are entry-determined
  and its z-scores are < 3.
- The q = 8 entry hold rests on the measured m+(8, entry); the corner
  membership {3, 4, 8} is census fact, not theorem; whether 2^4 = 16
  ever re-enters at other phases was checked only on the registered
  grids (it fails everywhere tested).
- Float-grade: UU3a eigenvalue cross-check and UU6 spectra (flagged);
  all decision signs are arb at prec 300.
- Nothing here weakens PP's 1D result: the ku face still evades the
  N-c kill. What dies is the hope that the SAME margins power a
  Weil-style 2-parameter discriminant without a new spectral entry.

## 7. Hand-off (doc 36 S3 decision)

```text
VERDICT:   (U-b), as registered - the 2D weight x scale Castelnuovo is
           well-posed on the ku face (override posing Lorentzian (1,N),
           exact closed-form entries) but SUPPLY-GRADE ONLY: every
           entry, the hold/fail census, and the locus a*(3) = 2.357,
           a*(4) = 2.930, a*(8) = 2.308 are congruence/entry-
           determined; frozen-series z < 1.5 at gamma_1..5 (no U-a).
MECHANISM: the U-c risk realized quantitatively INSIDE U-b: the deep
           margin e^{-a}/rho_q makes the discriminant step demand
           Frobenius depth rho_q Lambda_p^2 e^a against the window's
           a/log q - exponential vs linear. Slack exists only at the
           q in {3,4,8} entry corner (15/527 cells, gone by a ~ 3).
THE GAP,   B' = Lambda_p - m+ occupies Weil's fixed-point slot. The 2D
SHARPENED: form needs ONE new object: an independent trace evaluation
           of the weight-against-Frobenius pairing - the same missing
           timelike/archimedean unit named by HH/doc-31/BB/QQ. Without
           it the quadratic step is a tautology of the certified shape.
S3 STATUS: the stress item does NOT kill the face (the 1D survivor
           stands, PP unweakened) and does NOT promote it (no
           index-grade contact). Option 2's survivor is 1D-plus-entry-
           corner; the 2D rung requires the new entry, not new posing.
WITNESS:   prime_uu_ku_castelnuovo_2d.py (UU1-UU8, ALL PASS, exit 0,
           deterministic x3, no gate touched after first run; ~4 min).
           Inherited reruns: prime_pp_ku_face_index,
           prime_int_gc_k3_barnes_rank (both ALL PASS before any work).
```
