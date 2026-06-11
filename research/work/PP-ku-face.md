# PP - Face hunt candidate 1: the ku face. Does the index inequality live on the ku square's GLOBAL torsion?

Status: fresh-context worker PP, 2026-06-10. Required reading executed in
order: doc 35 (the N-c kill + gap spec my face must evade),
NN-graph-class-test.md (the breakage mechanism: continuum hole -1/u at
depth-1 duals under the forced lattice dictionary), I-c6-ku-square.md IN
FULL (the ku square: |T_2w| = lcm(1..w+1)/(w(w+1))), doc 23 secs 5-6
(corrected Castelnuovo form; W's max-Gram repair), W-monoid-frobenius.md
sec 5, LL-square-dual.md (the dual-count construction adapted here).
Inherited witnesses rerun by me BEFORE any new work:
prime_int_ku_ladder (ALL PASS, exit 0, all printed values reproduced),
prime_int_ll_square_dual (ALL PASS LL1-LL7, exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_pp_ku_face_index

Sections 0-2 (dictionary, construction, hand derivations, gates,
registered predictions) were written BEFORE the witness was first run.
DISCLOSURE (LL/NN precedent): sec 1 contains design-stage hand
derivations (the homogeneous coset FE, the zero-mode ledger, the hole
coefficient, the repayment law, the exact margin form and its entry/deep
asymptotics, the NN-matched predicted values). They are derivations, not
fits; the witness checks them fail-closed and a mismatch is a FAIL.

Discipline: F-a - no zeta values, no zeta continuation anywhere;
per-lattice/per-coset Jacobi Poisson only (the banked exhibition
device). Zeros enter ONLY via fork_lib.zeta_gammas, ONLY after the
sha256 freeze, COMPARISON ONLY (gate KU9).

## 0. The question and the registered fork

NN killed the index inequality on the Frobenius-graph classes under the
forced lattice dictionary: the FE strips the primal unit and leaves an
exact continuum hole -1/u in the dual; an inserted ATOM cannot cancel a
CONTINUUM deficit; the Lambda(p) (depth-1) classes fail always
(-e^{-a}/2), and (p;2) classes fail recurrently at every window-entry
phase for p >= 5. Doc 35's gap spec: the counterweight must be one
continuum unit per place, paid at each window-entry phase, at the
e^{-a}/2 scale, in phase with the combs.

EVASION HYPOTHESIS (E2, this face): the ku square's torsion cells are
GLOBAL (one cell per prime power q >= 3, q <= w-1, q not dividing
w(w+1); the fracture square already internalized the sum over places),
EVEN-degree, positively paired (the H^2 slot), and the supply
cardinality CONTAINS ITS OWN SUBTRACTION:

    L(w) = log|T_2w| = psi(w) + Lambda(w+1) - log w - log(w+1),
    dL(w) = Lambda(w+1) - log((w+1)/(w-1))   (atom MINUS continuum
                                              density ~ 2/w, exact).

CENTRAL HOPE (test first): the internal subtraction -log w(w+1) is the
structural form of NN's missing per-class counterweight.

PRE-REGISTERED VERDICT TABLE (fixed before any computation):

```text
(P-a) the internal subtraction cancels the continuum hole: the per-cell
      FE is HOMOGENEOUS (no stripped unit, hole coefficient = 0 vs NN's
      -1), the admissible (post-window-entry) margin census is all
      arb-certified >= 0, and the truncated-face structure is band-
      (not hole-) shaped -> the ku face EVADES the N-c kill; escalate
      with the margin structure (entry floor, deep law).
(P-b) the hole is cancelled (KU2 passes) but some admissible class
      still breaks (certified negative in KU4, or a hole-shaped
      truncated-face failure) -> partial evasion; map the boundary
      (which q, which phases).
(P-c) the continuum hole REAPPEARS on this face (KU2 fails: a nonzero
      hole coefficient; or post-entry margins follow NN's -e^{-a}/2
      law / permanent-periodic recurrence) -> the hole is
      FACE-INDEPENDENT - a major datum for the exhaustion criterion.
```

FAIL-CLOSED: (P-c) is full-value; nothing below is tuned to avoid it.

## 1. The dictionary and the construction (hand derivations, before any run)

### 1.1 The forced dictionary (G-INT6 ledger inline)

Lee's cell structure (I-doc K2-K3, witnessed exactly, externally
replicated): T_2w has one cell of type q for every prime power q >= 3
with q + 1 <= w and q not dividing w(w+1); the cell of type q = p^j
contributes log p to L(w). FORCED ingredients (zero choices):

    cell comb of type q:   {w : w = 0 mod q and w = -1 mod q both
                            EXCLUDED}, i.e. q does not divide w(w+1)
                            (Lee's sieve, verbatim);
    entry rule:            the cell exists only for w >= q + 1
                            (Lee's q+1 <= w);
    cell weight:           log p(q) (cardinality, exact);
    scale dictionary:      count window at scale a = Gaussian
                            e^{-pi w^2 e^{-2a}} (the program's standard,
                            JJ/LL/NN verbatim); deg D = a.

CHOSEN ingredients (logged, the same moves NN's kill covered):

    lattice completion:    the type-q class is the FULL congruence comb
                            S_q = {w in Z : q does not divide w(w+1)}
                            (adds the pre-entry band |w| <= q and the
                            negative mirror). This is exactly NN's
                            forced-lattice-dictionary move (their combs
                            v_p = 0 mod d also lived on the whole
                            lattice); it is the apples-to-apples
                            transplant. The entry rule is reinstated
                            via (i) the ADMISSIBILITY rule below and
                            (ii) the truncated face (sec 1.5).
    admissibility:         a class (q; a) enters the decision census
                            only if a >= log(q+1) (the window contains
                            the cell's first honest weight) - NN's
                            window-admissibility rule transposed.
    unit treatment:        h^0 = log(1 + Theta), h^0_dual =
                            log(1 + Dual): the "+1" is the trivial
                            torsion element (|T| >= 1), present on BOTH
                            sides by the cardinality dictionary -
                            SYMMETRIC, self-dual; no one-sided
                            insertion (contrast LL6, where the dual
                            unit was the hand-inserted, demoted atom).
    chi calibration:       chi+ = a + log(rho_q (1 + rho_q)),
                            rho_q = (q-2)/q the comb density - LL6/NN
                            VERBATIM, so margins are comparable.

There is NO depth-1 degenerate address on this face: the sieve starts
at q >= 3 and every cell carries a proper congruence condition; the
classes that killed NN (the unconstrained-comb [p] classes, whose dual
is theta - 1/u) DO NOT EXIST in the ku dictionary. q in {1, 2} are
exactly the subtracted HZ entries. (Bookkeeping, printed by KU5.)

### 1.2 The dual: native-pairing status (the task's first check)

What Lee/I-doc supply natively: (i) the even-degree pairing slot - all
T-cells even, every Euler contribution +1 (I-doc K2) - a SIGN, at
cardinality level; (ii) NO analytic duality: the Poisson/Serre wall
over S is explicitly open (I-doc sec 7.6). So there is no NEW native
pairing to spend. What IS constructible with zero new pairing choices:
the banked K2/Jacobi per-lattice Poisson (GG/LL's exhibition device)
applied to the three cosets of the cell comb:

    Theta_q(t) = theta(t) - theta_{0 mod q}(t) - theta_{-1 mod q}(t),

each summand an exact lattice/coset Poisson. Unlike LL (which needed
the infinite kvec mirror tower to cancel one continuum unit per level),
the ku comb needs NO tower: it is a FINITE signed combination of three
lattice objects, and its internal subtraction performs the zero-mode
cancellation in one stroke (sec 1.3). Status: native pairing = the
banked one, coset form; the pairing itself spends no new choice; the
lattice completion (1.1) is the spent choice.

### 1.3 Hand derivations (design-stage, fail-closed targets)

(D1) THE HOMOGENEOUS FE. Coset Poisson (theta(x) = (1/x)theta(1/x);
sum_{w = c mod q} e^{-pi w^2 t^2} = (1/(qt)) sum_k e^{2pi i k c/q}
e^{-pi k^2/(q^2 t^2)}) gives EXACTLY

    Theta_q(t) = (1/t) D_q(1/t),
    D_q(u) = theta(u) - (1/q) sum_{k in Z} (1 + cos(2pi k/q))
             e^{-pi k^2 u^2 / q^2}.

NO "+1": the FE is HOMOGENEOUS. The comb's excluded residue w = 0 mod q
removes the origin atom from the primal; LL's entire gap ("the element
that makes the square dual's FE homogeneous") is supplied by the
internal subtraction. Dual floor: D_q(u) -> rho_q = (q-2)/q.

(D2) ZERO-MODE LEDGER (exact). The continuum (k = 0 Poisson) weights:
theta contributes 1; the 0-coset contributes (1/q) * q = 1; the
(-1)-coset's dual support is {m + 1/q : m in Z}, which misses 0 for
every q >= 2 (q | 1 impossible) - continuum-free. Ledger: 1 - 1 - 0 =
0, EXACT. One continuum unit per cell-class, paid internally by the
0-coset - the doc-35 spec's "one continuum unit per place", realized
inside the supply.

(D3) HOLE COEFFICIENT (the face-vs-face number). c_hole :=
lim_{u -> inf} u (D(u) - rho):

    NN d = 1 face:  D(u) = theta(u) - 1/u:  c_hole = -1  (THE hole);
    ku face:        all dual corrections Gaussian:  c_hole = 0.

(D4) REPAYMENT LAW (where the counterweight is paid). H_q(u) :=
u (D_q(u) - rho_q). For large q: H_q(qx) = -2x(theta(x) - 1) +
O(q^{-2}-curvature, e^{-pi q^2 x^2}). Hence H = -2 + 2x + O(e^{-pi/x^2})
for x << 1 (a DOUBLE hole pre-entry - the TWO excluded residues = the
two archimedean entries log w, log(w+1)), repaid through the theta
kernel at the entry scale u ~ q, and DEAD (0) beyond entry. The
counterweight is per-class (per q = p^j: per place AND scale), paid
exactly at the window-entry phase, in phase with the comb (the
cos(2pi k/q) harmonics): all three clauses of doc 35's spec.

(D5) EXACT MARGIN FORM. With D = D_q(e^a) = rho + delta,
delta = e^{-a} H_q(e^a):

    m+(q, a) = log(1 + (delta + e^{-a})/rho) + log(1 + delta/(1+rho))
             = e^{-a} [ (1 + H)/rho + H/(1+rho) ] + O(e^{-2a});

threshold H* = -(1+rho)/(1+2rho) (= -2/3 at rho ~ 1; -0.8 at q = 3).
By (D4), |H| <= 2x(theta(x)-1)|_{x=1} ~ 0.173 for all x >= 1 (post-
entry), far above H*: REGISTERED: every admissible margin positive;
the sign flip of the lattice margin sits at H = H*, i.e. e^a ~ (2/3) q
- strictly BELOW window entry e^a = q + 1. NN's breakage regime is,
on the ku face, entirely PRE-ENTRY (where the ladder has no cells).

(D6) THE TWO LAWS (registered numbers):
  entry floor:  m+(q, log(q+1)) ~ (1/q)[1 - 0.173 * 1.5] ~ +0.74/q
                (large q; exact values per q from the witness);
  deep law:     m+(q, a) -> +e^{-a}/rho_q as a -> inf:  SAME e^{-a}
                envelope as NN's killer law, OPPOSITE SIGN, density-
                weighted (NN: -e^{-a}/2 always).
  NN-matched cells: (11;2)@a=4.96 was NN's certified killer (-2.21e-3).
                ku match q = 121 @ a = 4.96 (x = 1.18, just post-entry):
                predicted m+ ~ +6.5e-3 (hand: H(1.18) = -0.0594).
                (5;2) broke for NN from onset 2 log 5 = 3.22 (neg-frac
                0.25): ku q = 25 @ 3.22+: predicted ~ +0.030.
  hand checks:  m+(3, log 4) ~ +0.557; m+(4, log 5) ~ +0.329.

(D7) Lambda-ATTRIBUTION (exact integers; the killers' new address).
Between w-1 and w the cells that switch ON are exactly {q >= 3 : q |
w-1}; OFF are exactly {q >= 3 : q | w+1, q <= w-2}. Using
prod_{q | n, q >= 3} p(q) = n / 2^{[2|n]} (exact), the increment
identity dL = Lambda(w+1) - log((w+1)/(w-1)) follows with the Lambda
atom carried by ONE cell: the top cell q = w+1, excluded from OFF
because it has not yet ENTERED (q <= w-2 fails). The von Mangoldt atom
on this face = the deferred entry of the top cell; the smooth -2/w =
the two residue switches. The Lambda killers' analogue is the
entry-phase neighborhood of each cell - covered by the census grid.

### 1.4 What the internal subtraction is (registered reading)

The two excluded residues are the two archimedean ladder entries of
|T_2w| = lcm(1..w+1)/(w(w+1)): the 0-residue (log w) carries the
continuum unit that kills theta's zero mode (D2) - GG's per-place
subtraction, realized as a residue class; the (-1)-residue (log(w+1))
is continuum-free at the origin and carries the deferred-entry Lambda
mechanism (D7). Registered claim: this IS the structural form of the
doc-35 counterweight, with the payment schedule (D4): the hole exists
pre-entry (-2/u), is repaid through the theta kernel AT entry, and the
admissible window opens already-paid. (Gated via KU1-KU3; the reading
itself is interpretation, flagged.)

### 1.5 The truncated face (the honest ku object; demoted diagnostics)

The honest cell support is one-sided and entry-truncated. Even
completion (logged choice): Theta_q^hon(t) = Theta_q(t) - B_q(t),
B_q(t) = sum_{|w| <= q, w in S_q} e^{-pi w^2 t^2} (a FINITE band,
2q - 4 points). EXACT band FE: Theta_q^hon(t) = (1/t) D_q^hon(1/t)
with D_q^hon(u) = D_q(u) - (1/u) B_q(1/u) - again homogeneous, with
the band's continuum transform as the explicit inhomogeneity carrier
(compare LL's single unit atom: the ku-truncated face's "gap object"
is a BAND, finite and explicit, not a point). D_q^hon(u) =
(1/u) Theta_q^hon(1/u) > 0 STRICTLY (positivity structural: it is a
positive count reflected) - the LL5d-content of the truncated face
holds by homogeneity; the values at entry (~ +0.078 at q = 121,
~ +0.012 at q in {3, 4, 9}, hand) are recorded. The NAIVE-chi margin
(chi = a + log(rho(1+rho))) on the truncated face is registered
NEGATIVE at entry (hand: -3.05 at q = 121): the deg-dictionary
mismatch (the band removes ~ all of the window below q), NOT a hole -
registered distinguishers vs NN's breakage: (i) heals monotonically
~ -3/x (algebraic), never recurs (NN: permanent log p^2-periodic);
(ii) scale O(1), attributable to B_q by exact identity (NN: -e^{-a}/2
from the FE-stripped unit); (iii) c_hole = 0 throughout (KU2).
DEMOTED: even completion + transform-as-dual are logged choices (NN
G8 precedent); sign census + healing ratios reported, no decision
weight against the lattice census.

## 2. PRE-REGISTERED GATES (written before the first run)

Evaluation rules fixed in advance: flint arb prec 300 for all decision
margins; theta/coset sums truncated at term < 1e-90 with monotone-tail
justification; exact integer/Fraction arithmetic for the zero-mode
ledger, the Lambda attribution, and the band membership; sign
decisions only when the arb ball resolves the sign (|mid| > rad);
float-grade (flagged) only in the KU9 spectral series. Decision-grade
values computed via the DUAL route after KU1 certifies the FE
(NN sec 1.2 precedent, reversed side).

```text
KU1 HOMOGENEOUS FE, INDEPENDENT ROUTES: q in {3, 4, 5, 9, 121} x
    a in {0.5, 2, 5} (q=121: {2, 5}): direct comb sum
    Theta_q(e^{-a}) vs e^a D_q(e^a) (three-theta coset route),
    rel < 1e-40; NO inhomogeneity (the identity as stated, no +1).
    Zero-mode ledger EXACT: continuum weights 1 - 1 - 0 = 0
    (Fractions); (-1)-coset dual support misses 0 exactly (q | 1
    impossible, exact integers). FAIL: any mismatch.
KU2 HOLE COEFFICIENT (decisive, the P-c detector): ku face:
    |H_q(u)| = |u (D_q(u) - rho_q)| < 1e-12 at u in {4q, 8q},
    q in {9, 121}. CONTROL (NN's killer reproduced inline):
    |u (theta(u) - 1/u - 1) + 1| < 1e-50 at u in {36, 968}.
    The face-vs-face pair (0 vs -1) printed. FAIL: any clause.
KU3 REPAYMENT LAW: |H_121(121 x) + 2x(theta(x) - 1)| <
    0.05 * |2x(theta(x)-1)| at x in {1/4, 1/2, 3/4, 1, 3/2}.
    RECORD: same table at q in {3, 4, 5, 9} (small-q deviation =
    curvature of the cos harmonics; the prime-2-anomaly watch).
    PRE-ENTRY SIGN: m+(q, a) at e^a = q/2 certified NEGATIVE for
    q in {9, 121} (the NN breakage regime exists on this face too -
    strictly below entry). FAIL: any clause.
KU4 ADMISSIBLE CENSUS (the decision set; arb, fail-closed):
    q in {all prime powers 3..32} u {49, 64, 81, 121, 125, 128, 169};
    grid a = log(q+1) + j*0.15, j = 0..19, plus a in {5, 8} where
    admissible. STRUCTURAL GATE: every census margin sign
    arb-RESOLVED. The census itself is the verdict input (registered
    prediction: ALL >= 0); any certified negative -> (P-b) evidence,
    reported per class. FAIL only if a sign is unresolvable.
KU5 THE LAWS + NN-MATCHED TABLE: (a) deep law:
    |e^a rho_q m+(q, 8) - 1| < 0.05 for q in {3, 4, 5, 9, 25};
    (b) NN-matched cells: m+(121, 4.96) sign arb-certified
    (registered POSITIVE, ~ +6.5e-3, vs NN's (11;2) certified
    -2.21e-3); m+(25, 3.25), m+(9, 4.96) certified signs (registered
    positive); (c) bookkeeping: no depth-1 address exists (sieve
    starts at q >= 3); q in {1, 2} are the subtracted HZ entries.
    FAIL: (a) or an unresolved sign in (b).
KU6 TRUNCATED FACE (DEMOTED, logged choices per sec 1.5):
    (a) band FE two routes: q in {3, 9}, a in {2, 3}: direct
        truncated comb vs D_q - transform, rel < 1e-35;
    (b) D_q^hon(e^{a_entry}) computed for all census q: positivity
        structural (printed; registered values ~ +0.01..0.08);
    (c) RECORD: naive-chi truncated margins at x = e^a/q in
        {1.0+, 1.5, 2, 3, 10, 20} for q in {9, 121}: registered
        all-negative-at-entry, healing monotonically (successive
        ratios < 1, no sign recurrence), -3/x-shaped.
    GATE: (a) + computations complete; (c) is record.
KU7 LAMBDA ATTRIBUTION (exact integers, 3 <= w <= 2000):
    ON(w) = {q >= 3 : q | w-1}, OFF(w) = {q >= 3 : q | w+1,
    q <= w-2} verified against direct support recomputation;
    prod identity prod_{q|n, q>=3} p(q) = n / 2^{[2|n]}; top-cell
    deferral: q = w+1 in (divisors \ OFF) iff w+1 is a prime power;
    K4 recursion |T_2w| (w+1) = |T_2(w-1)| (w-1) e^{Lambda(w+1)}
    rerun exactly. FAIL: any integer mismatch.
KU8 CARRIER GUARD: ku-cell unformability on the fakes, two
    independent kills printed: (i) categorical (I-doc G-INT3): no
    ring -> no THH -> no T(p) cells -> no ladder (DH: no carrier
    monoid at all); (ii) arithmetic: the cell address (q, w) needs
    "prime power" in a UF monoid; Epstein x^2+5y^2: 36 = 4*9 = 6*6,
    v(36) in {0, 2} by chain (LL7 rerun inline) -> no valuation, no
    sieve, no cell address. FAIL: any clause.
KU9 FREEZE + ZERO COMPARISON (II protocol verbatim, NN G7 pattern):
    a-grid [0.5, 8], 512 pts (float-grade, flagged): S1 = e^a
    m+(9, a), S2 = e^a m+(121, a), S3 = sum_{q <= 32} log p(q)
    m+(q, a) [admissible q only] (the assembled record series).
    sha256 of the JSON printed BEFORE any fork_lib import; THEN
    zeta_gammas(100), spectral z at gamma_1..5 vs background
    gamma in [5, 60] (MAD; +-1.5 bands at first 12 gammas excluded).
    REGISTERED EXPECTATION: S1, S2 z < 3 (single-q congruence
    structure, no prime sum, no gamma channel). S3 contains the
    prime-power staircase (entries at a = log(q+1)) and is
    EF-TAUTOLOGY-EXPOSED: elevated z there is expected structure,
    RECORD ONLY, no shock semantics. Shock criterion (escalate):
    z >= 4 at >= 3 of first 5 gammas in S1 or S2.
    GATE: freeze ordering + comparison computed.
```

Registered overall verdict (written before the run): IF KU1-KU5 pass
as derived: (P-a) - the ku face EVADES the N-c kill; the internal
subtraction is the structural counterweight (one continuum unit per
cell-class, paid at window entry through the theta kernel); the
admissible margin laws are entry floor ~ +0.74/q and deep +e^{-a}/rho_q
(NN's envelope, sign flipped); the breakage regime survives only
PRE-ENTRY, where the ladder has no cells. IF KU2 fails: (P-c). IF KU2
passes but KU4/KU5 produce certified admissible negatives: (P-b) with
the boundary mapped.

---- verdict sections written after the runs ----

## 3. VERDICT: (P-a) AS REGISTERED - THE ku FACE EVADES THE N-c KILL;
## THE INTERNAL SUBTRACTION IS THE COUNTERWEIGHT, AND THE KILLER LAW
## COMES BACK SIGN-FLIPPED

Witness ALL PASS (KU1-KU9, exit 0, deterministic across 3 runs, ~50 s;
freeze 02250df1201b63f55fb8f6fccc8182ef415c62d9e4275aa218ad47d4849e
3952; full logs /tmp/pp_run{1,2,3}.log). NO witness engineering: every
gate passed the first run untouched, every hand-derived value confirmed
(worst law deviation 0.2%; the NN-matched prediction +6.5e-3 measured
+6.4682e-3).

```text
THE STRUCTURAL PAIR (KU1, KU2; arb-certified):
  NN d=1 face: FE inhomogeneous (+1 stripped), dual = theta - 1/u,
               hole coefficient c_hole = -1 (control reproduced inline
               to 1e-50): the breakage mechanism.
  ku face:     FE HOMOGENEOUS (no +1 anywhere, two routes, 5.0e-88),
               c_hole = 0 (|u(D_q - rho_q)| < 1e-12 at u = 4q, 8q).
               The comb's excluded residue 0 mod q removes the origin
               atom AND its dual continuum unit in one stroke (the
               zero-mode ledger 1 - 1 - 0 = 0, exact; the (-1)-coset
               is continuum-free: q | 1 impossible).
THE PAYMENT SCHEDULE (KU3): H_q(qx) = -2x(theta(x) - 1) confirmed at
  q = 121 to < 0.4% (worst gate point); the double hole (-2, the TWO
  archimedean entries) exists ONLY pre-entry, is repaid through the
  theta kernel at the entry scale u ~ q, and is DEAD beyond entry.
  The lattice margin is certifiably NEGATIVE at e^a = q/2 (m+ =
  -0.0730 at q=9, -0.0083 at q=121) - NN's breakage regime exists on
  this face too, but sits STRICTLY BELOW window entry, where the ku
  ladder has no cells.
THE CENSUS (KU4): 527 admissible (q, a) margins, 24 prime powers
  q <= 169, entry-to-deep grids: ALL SIGNS ARB-RESOLVED, ZERO
  NEGATIVES. Entry floors: m+ = +0.557 (q=3), +0.107 (q=9), +0.0327
  (q=25), +6.25e-3 (q=121), +4.45e-3 (q=169) - the ~0.74/q law.
  Minima all at the deep end (a = 8), all = the deep law.
THE LAWS (KU5): deep margin e^a rho_q m+(q, 8) = 0.9995..0.9998
  (five q): m+ -> +e^{-a}/rho_q. NN's killer envelope (-e^{-a}/2),
  SAME SHAPE, OPPOSITE SIGN, density-weighted.
THE MATCHED CELLS (KU5): ku q=121 @ a=4.96: +6.4682e-3 CERTIFIED > 0
  where NN's (11;2) @ 4.96 was CERTIFIED -2.21e-3. ku q=25 @ 3.26:
  +3.27e-2 (NN's (5;2): recurrent breakage, neg-frac 0.25). And the
  always-failing classes have NO ADDRESS: the sieve starts at q >= 3;
  there is no depth-1/unconstrained comb on the ku face - q in {1,2}
  are exactly the two subtracted HZ entries.
ZEROS (KU9, II protocol): z < 3 at gamma_1..5 in S1/S2 (max 2.7), no
  shock; S3 (assembled prime-power staircase, EF-tautology-exposed,
  record only): max z = 1.2. The margin structure is entry/congruence-
  determined, not zero-positioned.
```

## 4. The mechanism (why the sign flips)

One identity does all the work. NN's depth-1 comb contains the unit;
Poisson strips it; the dual inherits an unpayable continuum hole -1/u;
the hand-inserted atom recovers half: m+ = -e^{-a}/2. The ku cell comb
EXCLUDES w = 0 and w = -1 (q | w(w+1) - Lee's sieve, i.e. the
denominator w(w+1) of |T_2w|): the 0-coset's k = 0 Poisson mode is
EXACTLY one continuum unit and cancels theta's zero mode inside the
comb itself; the FE comes out homogeneous; the cardinality unit
(|T| >= 1, the trivial element, present symmetrically on both sides)
is then NET SURPLUS +e^{-a}/rho instead of a stripped debt. Doc 35's
gap spec is satisfied clause by clause, internally: one continuum unit
per class (the 0-coset zero mode), per place AND scale (q = p^j), paid
at the window-entry phase (the repayment law H_q(qx) = -2x(theta(x)-1),
support u <~ q), in phase with the comb (the cos(2pi k/q) harmonics),
at the e^{-a} scale (the margin envelope). The increment identity
dL = Lambda(w+1) - log((w+1)/(w-1)) is the integer shadow of the same
schedule, now with an exact attribution (KU7): the von Mangoldt atom
is the SINGLE deferred top cell q = w+1 (excluded from the OFF-switch
set because it has not yet entered); the smooth -2/w is the pair of
residue switches. "Atom minus continuum density" is literally
"deferred entry minus the two excluded residues".

What the truncated (honest, entry-truncated) face adds (KU6, demoted):
its exact FE is also homogeneous with the FINITE band B_q (2q - 4
points) as the only inhomogeneity carrier - LL's gap was ONE atom; the
ku-truncated gap is an explicit band, and its naive-chi deficit at
entry heals monotonically (~ -3/x, measured -2.50 -> -0.14 at q=9,
-4.55 -> -0.16 at q=121, monotone, no recurrence) - band-shaped, not
hole-shaped: all three registered distinguishers vs NN's permanent
log p^2-periodic breakage hold. New observed regularity (recorded, not
gated): D^hon at entry is nearly UNIVERSAL, +0.0122..0.0134 across all
24 census q - the entry-edge dual count has a q-independent floor;
unexplained, flagged for the escalation step.

## 5. G-INT6 ledger

```text
input                          choices spent
cell comb q !| w(w+1)          forced (Lee's sieve, I-doc K2-K3,
                               externally replicated)
entry rule w >= q+1            forced (Lee); enters as admissibility
                               (NN's window rule transposed) + the
                               truncated face
cell weight log p(q)           forced (cardinality, exact)
lattice completion S_q on Z    THE spent choice - the same forced-
                               lattice-dictionary move NN's kill
                               covered (apples-to-apples transplant)
pairing/dual                   banked K2 coset Poisson, ZERO new
                               pairing choices (no kvec tower needed;
                               Lee supplies the even-degree sign slot
                               but no analytic duality - none spent)
unit treatment                 symmetric +1 both sides (the trivial
                               torsion element; cardinality dictionary;
                               NO one-sided insertion - contrast LL6)
chi calibration                a + log(rho_q(1+rho_q)), LL6/NN VERBATIM
                               (comparability, not tuning)
truncated-face dual            even completion + transform-as-dual:
                               TWO logged choices, DEMOTED (KU6 record)
zeros                          fork_lib.zeta_gammas, post-freeze,
                               comparison only (KU9)
grids/census ranges            calibration, registered before run 1
```

## 6. Honest limits

- The lattice completion is MY dictionary move (logged): the test
  certifies the NN-matched transplant of the cells, not Lee's
  truncated object as such; the truncated face is handled only at the
  demoted level (its naive-chi margin IS negative at entry - explained
  as the deg-dictionary/band mismatch, with measured non-recurrence,
  but a sharper truncated-face chi is future work).
- "All positive" is a 527-point certified census (entry-to-deep grids,
  24 prime powers to 169), not a proof for all (q, a); the laws (D5,
  D6) make the interpolation principled but unproved. No phase can
  recur post-entry by the Gaussian decay of H, but that argument is
  hand-level, not gated.
- m+ -> +e^{-a}/rho_q means the deep-effective margin is MARGINAL
  (consistent with HH/LL: no slack at infinity); the face evades the
  kill, it does not manufacture slack.
- The margin object is per-cell-type; the assembled (log p-weighted)
  margin is a positive combination of per-type margins by construction
  (S3 is its record). A genuinely 2D ku-face inequality (weight x
  scale, the H^2 Castelnuovo slot, doc 23 sec 5-6) is NOT posed here.
- Cardinality level only: extension problems, the true ku-square
  diagonal, and any spectrum-level duality remain open (I-doc sec 7);
  nothing here touches the properness/Poisson wall.
- KU9 spectra are float-grade (flagged); S3's EF-tautology exposure is
  registered, so its (low) z-scores carry no evidential weight either
  way.

## 7. Hand-off (face hunt, candidate 1 decision)

```text
VERDICT:   (P-a), as registered. The ku face EVADES the N-c kill,
           certificate-grade at the census level: hole coefficient 0
           (vs -1, control reproduced), homogeneous FE by internal
           subtraction, 527/527 admissible margins certified positive,
           killer law sign-flipped (+e^{-a}/rho_q vs -e^{-a}/2),
           NN's certified killer cell (11;2)@4.96 = -2.21e-3 maps to
           ku q=121@4.96 = +6.4682e-3 CERTIFIED POSITIVE.
INTERNAL   CONFIRMED as the structural form of doc 35's counterweight:
SUBTRACTION: the 0-coset zero mode = one continuum unit per cell-class,
           internal; payment exactly at window entry (H = -2x(theta(x)
           -1)); the Lambda atom = the deferred top cell (exact, KU7).
           The breakage regime survives only PRE-ENTRY, where the
           ladder has no cells.
PAIRING:   no NEW native pairing exists (Lee gives the even/positive
           sign slot only); the banked K2 coset Poisson suffices with
           zero new choices and NO mirror tower - the subtraction does
           in one stroke what LL's kvec tower did level-by-level.
ESCALATE:  hand the spine the margin structure: entry floor ~ 0.74/q,
           deep +e^{-a}/rho_q (marginal, no slack), threshold
           H* = -(1+rho)/(1+2rho) never crossed post-entry; open items
           for the next rung: (i) the truncated-face chi (the band),
           (ii) the universal entry floor D^hon ~ +0.0127, (iii) the
           2D (weight x scale) Castelnuovo posing on H^2 with doc 23
           sec 5-6's corrected diagonal.
NOT ZEROS: z < 3 everywhere decision-grade (max 2.7); the structure is
           congruence/entry-determined. Freeze protocol held.
WITNESS:   prime_pp_ku_face_index.py (KU1-KU9, ALL PASS, exit 0,
           deterministic x3, no gate touched after first run).
           Inherited reruns: prime_int_ku_ladder,
           prime_int_ll_square_dual (both ALL PASS before any work).
```
