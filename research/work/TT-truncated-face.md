# TT - Doc 36 stress item S2: the truncated-face chi. Does honest truncation reopen the hole, or does a correct finite-size chi exist?

Status: fresh-context worker TT, 2026-06-11. Required reading executed in
order: doc 36 (I am stress item S2: the lattice completion is the one
modeling move PP's survival shares with NN's kill), PP-ku-face.md IN FULL
(sec 1.5 + sec 6 honest limits: the truncated face is demoted, naive-chi
margin NEGATIVE at entry, band-shaped distinguishers measured, "a sharper
truncated-face chi is future work"), NN-graph-class-test.md (the kill:
continuum hole -1/u, permanent log p^2-periodic recurrence),
KK-L1-density-rr.md + LL-square-dual.md (the chi machinery: chi = deg +
log(density constants), the density = the k = 0 / continuum zero mode of
the comb; LL6/NN chi+ = a + log(rho(1+rho))). Inherited witness rerun by
me BEFORE any new work: prime_pp_ku_face_index (ALL PASS KU1-KU9, exit 0,
freeze 02250df1...3952 reproduced, all decision values identical).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_tt_truncated_face_chi

Sections 0-2 (derivations, gates, registered predictions) were written
BEFORE the witness was first run. DISCLOSURE (KK/PP precedent): one
design-stage calibration run (inline, no witness file, full log kept in
this doc's sec 2 disclosure block) was used to check the derived
correction had slack before gate registration; every gated quantity below
is DERIVED by hand in sec 1, none is fitted; the calibration run changed
no derivation and is quoted where it confirmed hand numbers.

Discipline: F-a inherited (no zeta values/continuation; coset Jacobi
Poisson only); zeros ONLY via fork_lib.zeta_gammas AFTER the sha256
freeze, comparison only (TT9). G-INT6: every choice logged (sec 5).
Carrier guard inherited (TT2 prints the PP KU8 bookkeeping).

## 0. The question and the registered fork

PP measured (KU6, demoted): the honest (entry-truncated, even-completed)
ku face has NAIVE-chi margin negative at entry (-2.495 at q = 9, -4.549
at q = 121), healing monotonically ~ -3/x, no recurrence, c_hole = 0
throughout - band-shaped, with all three registered distinguishers from
NN's hole. Doc 36 S2: settle whether that entry band is

```text
(T-a) CHI BOOKKEEPING: the naive chi mis-counts the truncated boundary;
      a correct finite-size chi - an exact boundary correction, DERIVED
      not fitted - makes the margin positive at entry with everything
      else unchanged (deep law preserved, homogeneous FE untouched,
      no recurrence anywhere post-entry).
(T-b) GENUINE REOPENING: the lattice completion was load-bearing; no
      derived correction exists that is simultaneously positive at
      entry and consistent (deep law / FE); or the corrected margin
      breaks RECURRENTLY post-entry (the NN kill signature). Option 2
      closes by rule.
```

FAIL-CLOSED: (T-b) is full-value and closes option 2; nothing below is
tuned to avoid it. Registered expectation (from PP's measured healing +
the derivations below): (T-a), with the correction = the continuum
zero-mode of the truncated window (candidate C1 below) and the
deferred-top-cell candidate C2 REFUTED by the deep-law consistency gate
(the discrimination is part of the test: the data must select between
two pre-registered derived candidates, and C1 must survive every
consistency check or the verdict degrades toward T-b).

## 1. Hand derivations (design-stage, before any run)

Objects (PP sec 1.5, verbatim): S_q = {w in Z : q !| w(w+1)},
rho_q = (q-2)/q; band B_q(t) = sum_{|w| <= q, w in S_q} e^{-pi w^2 t^2}
(exactly 2q - 4 points); truncated face Theta_q^hon(t) = Theta_q(t) -
B_q(t); EXACT band FE Theta_q^hon(t) = (1/t) D_q^hon(1/t),
D_q^hon(u) = D_q(u) - (1/u) B_q(1/u) (homogeneous; the band's transform
is the explicit inhomogeneity carrier). Naive margin (LL6/NN chi):
m^naive = log(1 + Theta^hon(e^-a)) + log(1 + D^hon(e^a)) - a -
log(rho(1+rho)).

### 1.1 (Z) The zero-charge identity - the bookkeeping-vs-hole discriminator

The band's continuum charge is its point count minus the comb-density
length it occupies:

    M_0(q) := (2q - 4) - rho_q * 2q = 0   EXACTLY (Fractions):
    (2q - 4) / rho_q = (2q - 4) q / (q - 2) = 2q.

The band carries ZERO continuum units; equivalently, removing it removes
exactly the continuum window |y| <= q at density rho_q. CONTRAST (NN,
PP KU2 control): the d = 1 hole carries exactly MINUS ONE continuum unit
(u(theta - 1/u - 1) = -1). A zero-charge defect is absorbable by
finite-size chi bookkeeping; a one-unit defect is not (an atom cannot
cancel a continuum). This is the identity-grade form of PP's measured
distinguishers, and it FORCES the window cutoff in C1 below: the
equivalent continuum window of the removed band is |y| <= q exactly
(not q + 1, not q - 2: those would carry nonzero charge).

### 1.2 (C1) The corrected chi: the zero-mode of the truncated window

The chi machinery (KK -> LL6/NN) is: chi = deg + log of the CONTINUUM
ZERO MODE constants of the comb - primal law rho e^a (the k = 0 Poisson
/ Euler-Maclaurin leading term), dual floor rho, unit symmetric:
chi+ = a + log(rho(1+rho)). On the truncated face the comb's zero mode
through the Gaussian window is NOT rho e^a: it is the same continuum
restricted to |y| > q (the equivalent window of sec 1.1):

    primal law:  rho * 2 int_q^oo e^{-pi y^2 e^{-2a}} dy
               = rho e^a E_q(a),   E_q(a) := erfc(sqrt(pi) q e^{-a}),
    dual law:    e^{-a} * (primal law) = rho E_q(a)   (by the same
                 reflection that gives the lattice dual floor rho).

REGISTERED CORRECTION (zero free parameters, every ingredient forced):

    chi^corr(q, a) = a + log( rho_q E_q(a) (1 + rho_q E_q(a)) ),
    m^corr(q, a)   = log(1 + Theta^hon(e^-a)) + log(1 + D^hon(e^a))
                     - chi^corr(q, a).

Lattice limit: no band -> E ≡ 1 -> chi^corr ≡ chi+ (PP's census is
untouched; the correction lives only on the truncated face). Deep limit:
E -> 1 as a -> oo, so chi^corr -> chi+ (no deep tuning possible).

### 1.3 Derived consequences (the registered predictions)

(D1') THE -3/x HEALING LAW IS THE CORRECTION. chi^naive - chi^corr =
-log E - log((1+rho E)/(1+rho)). For e^a = qx, x >> 1: E = 1 - 2/x +
O(x^-3), so the difference = 2/x + 2rho/((1+rho)x) + O(x^-2) = 3/x at
rho ~ 1. PP's measured healing shape (-3/x, monotone, algebraic) is
EXACTLY the naive chi's failure to subtract the truncated window: the
band deficit was never a hole, it was the chi's own boundary term.

(D2') THE UNIVERSAL ENTRY FLOOR IS erfc(sqrt(pi)). At entry e^a = q+1
the truncated dual D^hon(q+1) = Theta^hon(1/(q+1))/(q+1): a Gaussian
tail starting EXACTLY at s = w/(q+1) = 1, density rho per unit w. Hence
D^hon(entry) -> rho * 2 int_1^oo e^{-pi s^2} ds = rho erfc(sqrt(pi)) =
rho * 0.012224 as q -> oo. PP's flagged unexplained regularity ("D^hon
at entry nearly universal, +0.0122..0.0134 across all 24 census q") is
the zero mode of the entry window; the small-q excess is the discrete
Euler-Maclaurin boundary term (first atoms e^{-pi(1+j/u)^2} vs the
integral). The universality PP flagged is the fingerprint of C1.

(D3') DEEP LAW RECOVERED EXACTLY AT FIRST ORDER, cross term derived.
Deep (y := q e^{-a} << 1): Theta(e^-a) = rho e^a + H (Gaussian-dead),
B(e^-a) = (2q-4) - pi e^{-2a} S_2 + ..., and (2q-4) = 2q rho (sec 1.1):

    log(1 + e^a D^hon) - a - log(rho E)
      = e^{-a}/rho + 2y e^{-a}/rho - e^{-2a}/(2 rho^2) + O(y^3),
    log(1 + D^hon) - log(1 + rho E) = O(y^2 e^{-a}),

(the -2y and -2y^2 of the count cancel the -2y - 2y^2 of log E
IDENTICALLY because the band charge is zero), so

    m^corr(q, a) -> (e^{-a}/rho_q)(1 + 2 q e^{-a}) + O(y^3, e^{-2a}):

the corrected truncated face obeys THE SAME deep law +e^{-a}/rho_q as
PP's lattice face (KU5a), approached from ABOVE with derived relative
cross term +2qe^{-a}. A wrong window cutoff (q+1 instead of q, i.e.
nonzero band charge) leaves a q-SIZED residue at order e^{-a} and fails
this gate: the deep law has teeth against the cutoff choice.

(D4') ENTRY MARGIN POSITIVE, ~ +c/q. At entry: m^corr ~
log(1 + rho u E1)/(rho u E(q/u)) + ... with u = q+1, E1 = erfc(sqrt(pi));
leading terms 1/(rho u E1) - (2e^{-pi}/E1)/u + EM-fluctuation =
(81.8/rho - 7.07 + O(1))/q > 0 for all q: the unit's relative weight
against the thin entry window dominates. Hand values: m^corr(3, entry)
~ +2.56, m^corr(9, entry) ~ +1.79, m^corr(121, entry) ~ +0.47.

(D5') PRE-ENTRY IS TRIVIALLY POSITIVE (record only). Below entry
chi^corr collapses (log E ~ -pi q^2 e^{-2a}) faster than the count
(whose floor is the unit, log(1+...) >= 0): m^corr -> +oo as a -> -oo.
The corrected chi KNOWS the truncated face has no pre-entry cells: NN's
pre-entry breakage regime (PP KU3) is not mis-scored as breakage here,
and pre-entry carries no decision weight (admissibility unchanged,
a >= log(q+1)).

(D6') (C2) THE DEFERRED-TOP-CELL CANDIDATE - registered to FAIL. The
integer lemma (PP KU7) attributes the truncation at integer level by
the SHARP count N^hon(x) = N(x) - (2q-4), i.e. window factor
F_q(a) = 1 - q e^{-a} (sharp window of equivalent length 2q):

    chi^C2(q, a) = a + log( rho F (1 + rho F) ).

Deep: log F = -y + O(y^2) but the actual Gaussian-weighted band deficit
is -2y: factor-2 mismatch, leaving m^C2 ~ e^{-a}[1/rho -
q(1+2rho)/(1+rho)] < 0 for q >= 5: C2 BREAKS the deep law (predicted
e^a rho m^C2(q,8): q=9 ~ -9, q=25 ~ -33, q=121 ~ -186) and produces
certified deep negatives. REGISTERED READING: the sharp count is the
right attribution at the INTEGER layer (KU7, exact) and the wrong one
at the Gaussian-scale layer; the data must select C1 over C2 (this is
the test's internal control - a derived candidate that fails).

(D7') THE MOMENT IDENTITY (the exact Euler-Maclaurin boundary terms;
the identity-grade certification of C1's attribution). B_q is a FINITE
sum of entire Gaussians, so exactly, absolutely convergently:

    u (D^hon(u) - rho_q E_q(q/u-arg)) , evaluated at u = e^a:
    u (D^hon(u) - rho_q E) = H_q(u) - sum_{m>=1} (-pi/u^2)^m / m! * M_{2m}(q),
    M_{2m}(q) := sum_{w in band} w^{2m} - rho_q * 2 q^{2m+1}/(2m+1),

with M_0 = 0 (sec 1.1) and every M_{2m} exact (integer/Fraction). In
particular M_2(q) = -(2/3)q^2 + (7/3)q - 2 (hand, from
sum_{|w|<=q} w^2 = q(q+1)(2q+1)/3 minus the two excluded cosets'
2q^2 and 1 + (q-1)^2). The entire deviation of the corrected dual from
its floor is H (PP's certified repayment kernel) plus an explicit
integer-moment tail: the correction is an attribution by exact
identity, not a model.

## 2. PRE-REGISTERED GATES (written before the first run)

Evaluation rules fixed in advance: flint arb prec 300 for all decision
margins; theta/coset/band sums truncated at term < 1e-90 with
monotone-tail justification; erfc via arb's erf (ball arithmetic);
exact integers/Fractions for M_0, M_2, the moment ledger, band
membership; sign decisions only when the arb ball resolves the sign;
float-grade (flagged) only in TT9 spectra. Census grid = PP KU4's grid
VERBATIM (comparability, not tuning).

DISCLOSURE (design-stage calibration, KK/PP precedent): one inline run
checked slack of the derived values before these gates were frozen:
entry m^corr = +2.566 (q=3), +1.788 (q=9), +0.473 (q=121), +0.364
(q=169); deep e^a rho m^corr(8) = 1.0015 (q=3) .. 1.0167 (q=25),
1.0826 (q=121) - matching 1 + 2qe^{-8} to < 2e-3; C2 deep -9.1 / -33.4
/ -185.8 (q = 9/25/121); D^hon(entry) = 0.01219..0.01341 vs rho E =
0.01256..0.02247 (small-q EM excess as derived). No derivation or gate
was changed after this check; it confirmed the hand numbers of sec 1.3.

```text
TT1 BAND FE, INDEPENDENT ROUTES (extends PP KU6a): q in {3, 9, 25,
    121} x a in {2, 3} u {entry, entry + 1} (admissible points only):
    direct truncated comb sum Theta^hon_q(e^{-a}) vs
    e^a D_q(e^a) - B_q(e^{-a}) (coset route minus band), rel < 1e-35.
    The FE stays homogeneous and untouched by the chi correction (the
    correction never enters this gate). FAIL: any mismatch.
TT2 ZERO-CHARGE LEDGER (exact; the discriminator): for ALL census q:
    M_0(q) = (2q-4) - rho_q 2q = 0 and (2q-4)/rho_q = 2q, Fractions;
    band cardinality |B| = 2q - 4 by direct enumeration; M_2(q) =
    -(2/3)q^2 + (7/3)q - 2 by direct exact summation. CONTROL (NN's
    hole carries -1 unit, PP KU2 rerun): |u(theta(u) - 1/u - 1) + 1| <
    1e-50 at u in {36, 968}. Carrier-guard bookkeeping printed (PP KU8
    citation: no valuation -> no cell address; DH: no carrier monoid).
    FAIL: any clause.
TT3 MOMENT IDENTITY (D7', exact EM boundary terms, two routes):
    q in {9, 121}, u in {2q, 4q, 8q}: arb route u(D^hon(u) - rho E)
    vs H_q(u) - sum_{m=1}^{M} (-pi/u^2)^m/m! M_{2m} with M chosen so
    the next term < 1e-30 (exact M_{2m} by integer summation; tail
    bounded by the ratio test, printed). Agreement rel < 1e-25.
    FAIL: any mismatch.
TT4 CORRECTED ENTRY CENSUS (the T-a/T-b decision gate; PP KU4 grid
    VERBATIM on the truncated face): all 24 census q, a = log(q+1) +
    j*0.15 (j = 0..19) plus {5, 8} where admissible: every m^corr sign
    arb-RESOLVED; the census is the verdict input (registered
    prediction: ALL >= 0; any certified negative is T-b evidence,
    reported per class). FAIL only if a sign is unresolvable.
TT5 NO-RECURRENCE FINE SCAN (the strongest distinguisher vs NN's
    kill): q in {9, 121}: a from entry to entry + 2 log q, step 0.02
    (>= 2 full log-q periods; 221 + 481 points): all m^corr signs
    arb-resolved; registered ZERO negatives; if any negative: report
    the pattern (contiguous transient band = bookkeeping residue vs
    sign recurrence = T-b). RECORD: m^naive on the same scan (PP's
    healing distinguisher reproduced inline). FAIL: unresolved sign.
TT6 CONSISTENCY - DEEP LAW RECOVERED (D3'; the decisive consistency
    gate): (a) |e^a rho_q m^corr(q, 8) - 1| < 0.05 for q in {3, 4, 5,
    9, 25} (PP KU5a's gate form, same tolerance, truncated face);
    (b) SHARPENED, derived cross term: |e^a rho_q m^corr(q, 8) -
    (1 + 2 q e^{-8})| < 0.01 for q in {3, 4, 5, 9, 25, 121}.
    FAIL: any clause. (This gate kills wrong window cutoffs and any
    tuned correction: chi^corr -> chi+ deep, no slack available.)
TT7 CANDIDATE DISCRIMINATION (C2, registered to fail at Gaussian
    scale): m^C2(q, 8) certified NEGATIVE for q in {9, 25, 121} and
    |e^a rho m^C2(q,8) - (1 - q rho(1+2rho)/(1+rho) ... )|: record
    the values; gate is the certified SIGN (deep law broken by C2).
    RECORD: m^C2 at entry (positive there - the discrimination is
    deep, where the Gaussian weighting bites). FAIL: a sign
    unresolvable, or m^C2(q,8) >= 0 certified (would refute D6' and
    reopen the candidate question - reportable either way).
TT8 PRE-ENTRY + NN-MATCHED RECORDS: (a) m^corr at e^a = q/2 for q in
    {9, 121}: registered POSITIVE (D5': chi collapses; trivial regime,
    no decision weight; admissibility unchanged); (b) the NN-matched
    cell on the corrected truncated face: m^corr(121, 4.96) sign
    arb-certified (registered POSITIVE; NN's (11;2)@4.96 was certified
    -2.21e-3); (c) PP lattice anchors reproduced: m+(121, 4.96) =
    +6.4682e-3 and c_hole pair (0 vs -1) - the correction changes
    NOTHING on the lattice face (chi^corr ≡ chi+ there, E ≡ 1: no
    band). GATE: signs resolved; (c) values match PP's.
TT9 FREEZE + ZERO COMPARISON (II protocol, PP KU9 pattern): a-grid
    [entry, 8], 512 pts per series (float-grade, flagged):
    S1 = e^a m^corr(9, a), S2 = e^a m^corr(121, a). sha256 printed
    BEFORE any fork_lib import; THEN zeta_gammas(100), spectral z at
    gamma_1..5 vs background (MAD, +-1.5 bands at first 12 gammas
    excluded). REGISTERED EXPECTATION: z < 3 (the correction is
    congruence/entry-determined erfc bookkeeping, no zero content).
    Shock criterion (escalate): z >= 4 at >= 3 of first 5 gammas.
    GATE: freeze ordering + comparison computed.
```

REGISTERED DECISION RULE (fixed before the run): T-a iff TT1-TT3 pass
(identity-grade derivation certified), TT4 census all-positive with all
signs resolved, TT5 zero negatives (no recurrence), TT6 both clauses
(deep law recovered), TT8(c) anchors unchanged. T-b iff: any RECURRENT
certified negative in TT4/TT5, or TT6 fails (no derived correction
consistent with the deep law), or TT3 fails (the correction is not an
identity-grade attribution). A transient (contiguous, healing,
non-recurring) certified negative with all consistency gates passing =
partial: report as bookkeeping-residue-at-EM-order, NOT full T-a, and
say so. C2's registered failure (TT7) does not degrade T-a: it is the
internal control showing the data discriminates between derived
candidates.

---- verdict sections written after the runs ----

## 3. VERDICT: (T-a) AS REGISTERED - THE ENTRY BAND IS CHI BOOKKEEPING.
## THE CORRECT TRUNCATED-FACE CHI EXISTS, IS DERIVED (ZERO PARAMETERS),
## AND THE HONEST FACE THEN PASSES EVERYTHING THE LATTICE FACE PASSED

Witness ALL PASS (TT1-TT9, exit 0, deterministic across runs 2-3
including the freeze hash 4671bc0eda12c56d82082c0cf742a16b7e1917587
7a8efb1d92a9b1b61085216; logs /tmp/tt_run{1,2,3}.log). One disclosed
COMPUTATIONAL fix after run 1 (TT3's two routes had a 1e-16 float
argument mismatch from going through a = log(q*mult); routes now share
the exact arb u; predicate untouched - the identity then verifies to
8.2e-36..1.5e-34, i.e. the run-1 "failure" was double-precision
contamination of one route's argument, exactly as recorded inline in
the witness). Every registered prediction confirmed; no gate predicate
changed at any point.

```text
THE CORRECTION (C1, derived sec 1.2; certified identity-grade):
  chi^corr = a + log(rho_q E (1 + rho_q E)),  E = erfc(sqrt(pi) q e^-a).
  Identity pedigree: band charge M_0 = (2q-4) - 2q rho_q = 0 EXACT all
  census q (TT2, Fractions) - the cutoff q is forced, the band carries
  ZERO continuum units; full EM moment identity u(D^hon - rho E) =
  H_q(u) - sum_m (-pi/u^2)^m/m! M_2m with exact integer moments
  verified two routes to 8e-36 (TT3); M_2 = -(2/3)q^2 + (7/3)q - 2.
THE DECISION CENSUS (TT4): PP's KU4 grid VERBATIM on the honest
  truncated face, 527 margins: ALL SIGNS ARB-RESOLVED, ZERO NEGATIVES.
  Entry m^corr: +2.566 (q=3), +1.788 (q=9), +1.238 (q=25), +0.473
  (q=121), +0.364 (q=169) - positive at entry, ~ c/q, minima all at
  the deep end = the deep law.
NO RECURRENCE (TT5, the kill discriminator): fine scans (step 0.02,
  two full log-q scale periods, 221 + 481 pts, q = 9, 121): zero
  negatives, all signs certified; the naive margin's monotone healing
  reproduced on the same scan. Nothing recurs because nothing was ever
  broken: the "deficit" was the naive chi's missing boundary term
  (chi^naive - chi^corr ~ 3/x = PP's measured healing law, D1').
CONSISTENCY (TT6, decisive): the corrected truncated face obeys THE
  LATTICE DEEP LAW: e^a rho_q m^corr(q,8) = 1.0015..1.0167 (KU5a gate
  form re-passed), and matches the DERIVED cross term 1 + 2qe^-8 to
  < 1.5e-3 at all six q including 121. The FE is untouched (TT1,
  3.2e-87); the lattice anchors are unchanged (TT8: m+(121,4.96) =
  +6.4682e-3 = PP's digit-for-digit; c_hole = 0).
THE INTERNAL CONTROL (TT7): the second pre-registered derived
  candidate (C2, deferred-top-cell sharp window F = 1 - qe^-a) FAILS
  exactly as derived: deep margins certified negative (-3.9e-3,
  -1.2e-2, -6.3e-2; e^a rho m = -9.1, -33.4, -185.8 at q = 9, 25,
  121): the data discriminates between derived candidates; C1 is not
  vacuously confirmable bookkeeping.
THE FLAGGED MYSTERY RESOLVED: PP's "universal entry floor D^hon ~
  +0.0122..0.0134, unexplained" is rho_q erfc(sqrt(pi)) = rho_q *
  0.012224 + EM boundary terms (D2'): the entry window always starts
  at s = w/u = 1 exactly. The universality is C1's fingerprint.
ZEROS (TT9): z < 1 at gamma_1..5 in both corrected series (max 0.6 -
  even quieter than PP's lattice series); the correction is
  congruence/entry-determined erfc bookkeeping, no zero content.
```

## 4. What this settles (S2 closed)

The one modeling move PP's survival shared with NN's kill - the lattice
completion - is now certified NOT load-bearing. The honest, truncated,
no-completion ku face satisfies the SAME index inequality with the SAME
deep law, once chi carries its own exact boundary term; and the
distinction between "fixable by bookkeeping" and "NN's hole" is itself
an exact invariant: the truncation band has continuum charge 0 (every
removed point is paid by removed window at the comb's own density,
(2q-4)/rho_q = 2q), while NN's d=1 defect has continuum charge exactly
-1 (one unpaid unit - the thing no boundary term can supply, re-certified
inline). Bookkeeping can absorb a zero-charge defect and cannot
manufacture a unit: T-a and the N-c kill are two sides of one ledger.

Mechanically, all three of PP's measured distinguishers are now derived:
band-shaped = finite zero-charge support; -3/x healing = the naive chi's
missing window term 2/x + 2rho/((1+rho)x); no recurrence = there is no
deficit object at all post-entry, only a mis-normalized chi. The lattice
completion was a convenience (it let PP use LL6/NN's chi verbatim for
comparability), not a crutch.

Bonus structure banked: (i) the deep cross term - the corrected
truncated margin approaches +e^{-a}/rho_q FROM ABOVE with derived
relative excess 2qe^{-a} (the truncated face is never tighter than the
lattice face); (ii) the entry floor of the honest face is ~ +0.8/q...
+2.6 - far ABOVE the lattice entry floor ~ 0.74/q, because the unit
dominates the thin entry window (D4'); (iii) the exact moment ledger
M_2m gives the truncated face a complete, finite, integer-valued EM
expansion - the honest face is, if anything, MORE computable than the
completed one.

## 5. G-INT6 ledger

```text
input                          choices spent
truncated object + band FE     inherited from PP sec 1.5 verbatim (its
                               two logged choices - even completion +
                               transform-as-dual - inherited, unchanged)
window cutoff |y| <= q         FORCED by M_0 = 0 (zero-charge identity,
                               exact Fractions; cutoff q+1 or q-2 has
                               nonzero charge and fails TT6 by a q-sized
                               e^{-a} residue - teeth, not choice)
erfc window E_q(a)             0 new: the k = 0 continuum zero mode of
                               the comb on the truncated window - the
                               SAME zero-mode attribution that produced
                               chi+ = a + log(rho(1+rho)) on the lattice
                               (KK -> LL6/NN machinery, restricted)
candidate C2                   pre-registered counter-candidate from
                               PP's KU7 integer attribution; REFUTED as
                               registered (internal control)
census/scan grids              PP KU4 grid VERBATIM + fine-scan step
                               0.02 (calibration, registered before
                               run 1)
zeros                          fork_lib.zeta_gammas, post-freeze,
                               comparison only (TT9)
design-stage calibration       ONE inline run, disclosed in sec 2, no
                               derivation/gate changed after it
TT3 route fix                  computational (shared exact u), disclosed
                               in sec 3 + inline; predicate untouched
```

## 6. Honest limits

- The corrected chi is derived at zero-mode (continuum) order; the
  discrete EM boundary terms are certified as an exact identity (TT3)
  but are NOT folded into chi - they are the (positive-margin) residue
  the census measures. A chi carrying the full moment ledger would be
  tautological (margin = 0 identically); the zero-mode cut is the
  principled one (it is what chi means everywhere else in the program),
  but "where to cut the EM series" is a convention this memo makes
  explicit rather than removes.
- "All positive" is the 527-point certified census plus 702 fine-scan
  points, not an all-(q, a) theorem; the derived laws (entry ~ c/q,
  deep 1 + 2qe^{-a}) make interpolation principled but unproved.
- PP's even completion of the one-sided honest support (his sec 1.5
  logged choice) is inherited, not removed: "honest truncation" here
  means entry-truncated, still symmetrized. A genuinely one-sided
  treatment would need the half-comb Poisson and is untested.
- m^corr at entry is dominated by the symmetric unit against the thin
  entry window (1/(rho u E) ~ 82/q): entry positivity is robust but
  unit-dependent, same status as every margin in the LL6/NN chain.
- TT9 spectra float-grade (flagged); nothing decision-grade reads zeros.

## 7. Hand-off (doc 36 S2 decision)

```text
VERDICT:   (T-a), as registered, certificate-grade. The truncated-face
           entry band was a CHI BOOKKEEPING artifact. Correct chi:
           chi^corr = a + log(rho_q E(1 + rho_q E)),
           E = erfc(sqrt(pi) q e^{-a}) - derived, zero parameters,
           cutoff forced by the exact zero-charge identity
           (2q-4)/rho_q = 2q. Census 527/527 certified positive at
           entry-to-deep; fine scans (2 log-q periods) zero negatives;
           deep law +e^{-a}/rho_q RECOVERED with derived cross term
           1 + 2qe^{-a}; FE and all PP lattice anchors untouched.
S2 STATUS: the survival does NOT inherit NN's kill; the lattice
           completion is certified non-load-bearing. The bookkeeping-
           vs-hole boundary is itself an invariant: band charge 0
           (absorbable) vs hole charge -1 (not) - the same ledger that
           killed NN explains why truncation is harmless.
DERIVED:   PP's two flagged open items closed: the truncated-face chi
           (this memo) and the universal entry floor D^hon ~ 0.0122 =
           rho erfc(sqrt(pi)) (the entry window starts at s = 1).
CONTROL:   counter-candidate C2 (sharp window from the integer lemma)
           refuted exactly as pre-registered (deep margins certified
           negative, -9.1..-185.8 in deep-law units): the test could
           fail and the data chose.
NOT ZEROS: corrected-series z < 1 at gamma_1..5 (freeze protocol held).
WITNESS:   prime_tt_truncated_face_chi.py (TT1-TT9, ALL PASS, exit 0,
           deterministic; one disclosed computational route fix, no
           predicate changed). Inherited rerun: prime_pp_ku_face_index
           (ALL PASS, freeze hash reproduced) before any new work.
ESCALATE:  S2 clear for the doc-36 stress round; remaining S-items are
           S1 (all-(q,a) theorem) and S3 (2D Castelnuovo posing); the
           moment ledger M_2m (exact, finite) may be directly useful
           for S1's interpolation argument on the truncated face.
```
