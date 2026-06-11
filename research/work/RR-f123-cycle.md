# RR - Faces F1 + F2 + F3 (OO's table), one shared witness cycle

Status: fresh-context worker RR, 2026-06-10. Required reading executed in
order: OO-face-enumeration.md IN FULL (I execute its recommended spend:
F1 + F2 in one cycle, F3 riding free), doc 35, NN-graph-class-test.md IN
FULL, GG-global-cancellation.md (GG4), HH-weil-restriction-fork.md (Theta
measure, moment cone), doc 16 (trichotomy). Inherited witness rerun by me
BEFORE any new work: prime_nn_graph_class_index - exit 0, ALL STRUCTURAL
GATES PASS, breakage map reproduced exactly ((11;2)@4.96 certified
negative; first-neg onsets 3.219/3.892/4.796/5.130/5.666 for
p = 5/7/11/13/17; Spearman -0.499; log in /tmp/rr_nn_rerun.log).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_rr_face_cycle

Sections 0-2 below (constructions, gates, registered predictions) were
written BEFORE the witness was first run. DISCLOSURE (NN/LL precedent):
sec 1 contains design-stage hand derivations (the chi_GG d=1 closed form,
the m1_GG upper bound, the (1,0,1) Toeplitz eigenvalues, the quantization-
floor argument). They are derivations, not fits; the witness checks them
fail-closed and a mismatch is a FAIL.

Discipline: F-a (no zeta values/continuation); zeros ONLY via
fork_lib.zeta_gammas AFTER the sha256 freeze, COMPARISON ONLY. G-INT6:
F1 spends ZERO choices (the normalization is GG4's, forced); F2's measure
is HH's banked Theta_p = 2 p^{-k/2} verbatim, no retuning; every logged
extra (F1d adjunction, LP floor levels) is demoted to record.

## 0. The three faces and the registered verdict table

F1 (E3-a, GG zero-mode re-embed). chi_GG(D) = chi(D) - (one continuum
unit per depth-1 place in D's GRAPH support); equivalently (same
inequality, bookkeeping moved across the equals sign) the dual count is
Theta^dual_GG(u) = Theta^dual(u) + n_1(D)/u, n_1(D) = #{depth-1 places
in the graph-class support}. NOTE (structural, registered): the NN
dictionary FORGETS depth-1 places (d_p = 1 => m_p = 0 => trivial comb;
"the k=1 class forgets p, exactly"); n_1 is graph-class data, not comb
data - which is exactly where GG4 says the continuum unit went missing.
For every class in NN's decision census (all depths >= 2) n_1(D) = 0:
the subtraction is PROVABLY INERT there.

```text
(R1-a) the (p;2) window-entry negatives REPAIR under chi_GG
       -> F1 SURVIVES; escalate immediately (the hunt's win).
(R1-b) d=1 repairs EXACTLY (theta = Theta^dual + 1/u, AJ4-shaped
       positive margin) AND (p;2) inert as predicted ((11;2)@4.96
       still certified -2.21e-3) -> F1 DEAD; X1 first clause met;
       second-side confirmation of the class/scale-coupled unit spec.
REGISTERED PREDICTION: (R1-b). The mechanism is aimed at the HOLE
(-1/u, depth-1 only); the (p;2) breakage is a RACE failure (OO sec 0
mode split). If chi_GG DOES move (p;2), the split is wrong - itself
reportable.
```

F2 (E3-b, Theta-weighted aggregate). Measure = HH's banked Theta:
weight 2 p^{-k/2} on ladder slot (p,k), k <= n_p(a) = floor(a/log p).
Aggregates: per-place A_p(a) = sum_k 2 p^{-k/2} m(p;k)(a) and global
A(a) = sum_{p <= e^a} A_p(a); two unit variants, both registered:
(v) verbatim LL6 unit (NN's m+); (g) GG-repaired (F1 composite: the
k=1 slot carries m+_GG(d=1) which is positive but <= 3 e^{-pi e^{2a}},
i.e. +0 at every decision scale - hand bound, gated).

```text
(R2-kill-i)  a certified negative aggregate at an admissible scale/
             phase. REGISTERED PREDICTION: triggers at the PER-PLACE
             layer: A_11(4.96) < 0 in BOTH variants (k=1 contributes
             -e^{-a}/2-scale (v) or +0 (g); the k=2 slot is the
             certified -2.21e-3; no deeper slot in the window at
             p = 11, a = 4.96). Global A(a): uncertain, both ways
             carried.
(R2-kill-ii) the (p;2) directions are exposed/unavoidable in the
             admissible image cone: the sample direction
             c = (1, 0, 1) (load ONLY the breaking k=2 slot, zero on
             k=1) is PSD-Toeplitz (eigenvalues {0,1,2}: BOUNDARY =
             exposed) and nonnegative => admissible for quadratic
             tests (c_k = g-check(k log p) >= 0, HH H5a) => NO scalar
             aggregate can dominate the isolated class: aggregate
             positivity cannot certify dual-cone membership. Plus LP:
             feasible positive measures characterized (max feasible
             weight on (11;2) and on the breaking block; full-support
             floors).
(R2-kill-iii / doc 16) level-1 check: A(a) is computable comb-side
             (no EF, no zeros - by construction); freeze-then-zeros
             z < 3 expected; A is a scalar one-parameter family, NOT
             a PSD form over a test cone - it cannot BE level-1
             Bochner; its registered failure mode is being WEAKER
             than level-1 (kill ii).
(R2-survive) global A(a) >= 0 everywhere admissible AND the LP shows
             the breaking directions avoidable AND the aggregate is
             not level-1 -> characterize, escalate.
```

F3 (h^1 reinterpretation, riding free; on the frozen -m+ data).

```text
(R3-a) deficits count-shaped (log-cardinalities: values on/near
       {log m} or p-power lattices, place-additive over mixed
       classes, monotone window-entry) -> h^1 exists as a genuine
       count; NEW face RR-with-h^1; escalate.
(R3-b) not count-shaped (generic reals) -> X4 met.
REGISTERED PREDICTION: (R3-b), via the QUANTIZATION FLOOR: a genuine
count has h^1 in {0} u [log 2, oo); the certified deficits live
STRICTLY inside (0, log 2) (max 0.361 at d=1, a=0.5; decision cell
2.21e-3 = log 2 / 314), vary continuously in a, and at d=1 are
exactly place-independent (a count carrying the Lambda(p) = log p
atom cannot forget p). h^1 := max(0, -m+) is then the only definition
left = relabeling = G-INT6 kill (OO F3(iii)).
```

## 1. Constructions (hand derivations, before any run)

### 1.1 F1: the chi_GG margin

m+_GG(D, a) = log Theta_T(e^{-a}) + log(1 + Theta_T^dual(e^a)
              + n_1(D) e^{-a}) - a - log(rho_T (1 + rho_T)).

(D1) d=1 exact repair: NN P1 gives Theta^dual(u) = theta(u) - 1/u, so
Theta^dual_GG(u) = theta(u) (the self-dual Jacobi theta: the repaired
dual is CANONICAL) and, using the FE theta(e^{-a}) = e^a theta(e^a),

    m+_GG(d=1, a) = log theta(e^a) + log((1 + theta(e^a))/2)  >  0

strictly for every a (theta > 1), AJ4-shaped. At a >= 2 the value is
positive but below any resolvable scale: 0 < m+_GG(d=1, a)
<= 3 (theta(e^a) - 1)/2 <= 3 e^{-pi e^{2a}} (hand bound from
log(1+x) <= x; gated). Certification points a in {0.5, 1, 2}
(resolvable at prec 300; the a = 5 sign is the theorem theta > 1 -
NN's G3d lesson baked in at design time, disclosed).

(D2) Inertness: n_1 = 0 for every all-depths >= 2 class => m+_GG = m+
identically (not approximately): the census rerun is an identity check
plus the arb re-certification of the decision cell.

(D3) Adjunction (record only, FLAGGED): the augmented graph class
[p^2] + [q] (q a depth-1 place in window) has the SAME comb as (p;2)
but n_1 = 1; chi_GG repairs it whenever the deficit < the unit
(e^{-a}/(1+dual) ~ 4.6e-3 at a = 4.96 > 2.21e-3). This is a SUPPORT
CHOICE (the comb does not see q): repairing a breaking cell by
adjoining comb-invisible support is relabeling-adjacent and saves
nothing (the bare cell [p^2] still breaks; the inequality must hold
cone-wide). Recorded as the F1 evasion's own boundary.

### 1.2 F2: aggregates, LP, exposure

Slots (p,k), k <= n_p(a); weights w^Theta_{p,k} = 2 p^{-k/2}
(normalized where stated). Margins from the certified FE-comb route
(NN G1). k=1 margins are place-independent (computed once per a).
LP (scipy linprog, highs): variables w >= 0 on the slot family at
amax = 6 (a-grid [2.1, 6.0]); constraints sum w M(a_j) >= 0 with
M = e^a-scaled margins, slot inadmissible at a_j => coefficient 0;
sum w = 1. Outputs registered: (i) feasibility, free support;
(ii) feasibility with floor w >= eta w^Theta_norm, eta in {1e-6, 0.5};
(iii) max feasible w_(11,2); (iv) max feasible total weight on the
breaking block (variant v: all k=1 slots + (p;2) p>=5; variant g:
(p;2) p >= 5). Per-place p=11 LP is 2-variable and decided EXACTLY by
the certified margin signs.

### 1.3 F3: the three structure tests

(T1) Quantization floor: assemble the certified breaking set (d=1 at
a in {0.5,1,2,5}; (p;2) at first-neg + 0.2 for p in {5,7,11,13,17};
the decision cell). Gate: every -m+ strictly inside (0, log 2), arb;
distances to {log m : m in Z >= 1} and {k log p} recorded.
(T2) Place-additivity: m+(D1 u D2) vs m+(D1) + m+(D2) for disjoint
depth-2 pairs (5,11)@4.96, (7,11)@4.96, (11,13)@5.33; d=1
place-forgetting re-certified ((2;1) vs (5;1) identical, arb).
(T3) Sign structure at window entry: sign changes of m+ per period
from the (p;2) scans (count-shape/divisor-crossing predicts a single
onset, <= 2 changes; the banked recurrence predicts >= 2 with both
signs recurring EVERY period - sign-indefinite within the period).

## 2. Pre-registered gates (written before the first run)

Evaluation rules: flint arb prec 300 for all decision margins; sign
decisions only when the ball resolves (|mid| > rad); float-grade scans
flagged; exact Fractions / integer arithmetic for the Toeplitz minors
and carrier guard; freeze (sha256 of all series + scans + LP inputs)
printed BEFORE any fork_lib import; zeros comparison-only after.

```text
RG1 F1 d=1 exact repair: (a) two-route Theta^dual_GG = theta, rel
    < 1e-45, p in {2,3,5}, u in {e^0.5, e^2}; (b) m+_GG(d=1) > 0
    arb-certified at a in {0.5, 1, 2}; (c) closed-form identity
    m+_GG = log theta(e^a) + log((1+theta(e^a))/2) to 1e-60;
    (d) upper bound m1_GG <= 3 e^{-pi e^{2a}} < 1e-50 at a >= 2.48
    (the +0 bound used by F2-g).  FAIL: any clause.
RG2 F1 census under chi_GG (NN G4 family verbatim: depth scans, (p;2)
    cells, period scans, 14 rung towers, 36-box): n_1 = 0 for every
    class AND m+_GG - m+ = 0 (arb diff < 1e-80) AND decision cell
    (11;2)@4.96 m+_GG arb-certified < 0 with |m+_GG + 2.21e-3| <
    1e-4 AND (p;2) float breakage scans (p in {5,7,11,17}) bitwise
    identical under chi_GG.  A REPAIR here = R1-a, reportable, gate
    still passes structurally (census resolved); the verdict cell
    carries it.
RG3 F1d adjunction record: m+_GG([11^2]+[q=17], 4.96) computed, sign
    resolved (expected +), FLAGGED record, no decision weight.
RG4 F2 per-place aggregates: A_p(a) for p in {5,7,11,13}, both
    variants, at the rung scales {2.48, 4.96} and at first-neg + 0.2
    phases; decision values A_11(4.96) (v) and (g) arb-certified
    sign.  STRUCTURAL GATE: all decision signs resolved; the census
    is the verdict input.
RG5 F2 global aggregate: float scan a in [2.1, 6.0], 240 pts, both
    variants; minimum located; arb certification of the sign at
    a = 4.96 AND at the scan argmin (both variants).  GATE: resolved.
RG6 F2 LP battery (sec 1.2): solved (status OPTIMAL/INFEASIBLE per
    instance), outputs (i)-(iv) recorded; per-place p=11 LP decided
    exactly from certified signs.  GATE: computed.
RG7 F2 exposure (exact): T = Toeplitz(1,0,1) minors/eigenvalues exact
    (Fractions + eigvalsh cross-check): PSD, det = 0 (boundary),
    entries >= 0 => admissible direction isolating the breaking slot.
    FAIL: any minor negative or det != 0.
RG8 F3 T1/T2/T3 computed: every breaking-set margin arb-certified
    < 0 and -m+ in (0, log 2) certified; additivity deviations and
    sign-change counts recorded.  GATE: resolved/computed.
RG9 Carrier guard (inherited, rerun inline): Epstein x^2+5y^2: v(36)
    contradictory => no depth data => n_1(D) UNFORMABLE (chi_GG needs
    the valuation) and no tower address => Theta_p measure unformable;
    DH: no carrier monoid (bookkeeping).  FAIL: any clause.
RG10 Freeze + zeros (NN G7 verbatim): sha256 of {A_v, A_g series,
    (p;2) scans, breaking set, LP outputs} BEFORE fork_lib; z-scores
    at gamma_1..5 for e^a-scaled aggregate series, background MAD,
    comb-harmonic exclusions (p = 2, 3 jump combs).  REGISTERED
    EXPECTATION: z < 3.  Shock (>= 3 of first 5 at z >= 4) =
    escalate.  GATE: ordering enforced + computed.
```

Registered overall verdict (written before the run): R1-b + R2-kill-i
(per-place layer) + R2-kill-ii (exposure) + R3-b, jointly meeting X1
(both clauses) and X4 of OO sec 4, with the global aggregate's sign
recorded either way. Any survival instead: escalate per OO sec 4 last
paragraph.

---- verdict sections written after the runs ----

## 3. VERDICTS: R1-b, R2-kill (i)+(ii)+(iii), R3-b. X1 MET (both
## clauses), X4 MET. No survival; one structural positive banked.

Witness exit 0, runs 2-3 bit-identical (decision values, LP outputs,
freeze sha256 f036d4b6aff1087023d96a77a7388a6b8602c500d7279c8c04183daf0
9596266; logs /tmp/rr_run{1,2,3}.log). All registered predictions
confirmed; nothing moved against registration.

### 3.1 F1 - R1-b: the forced unit repairs the hole EXACTLY and is
### provably inert on the race. F1 DEAD; X1 first clause met.

```text
d=1 EXACT REPAIR (RG1): Theta^dual + 1/u = theta(u), two routes,
    rel 3.9e-90, place-independent; m+_GG(d=1) CERTIFIED > 0 at
    a in {0.5, 1, 2} (+5.9e-4, +2.5e-10, +9.7e-75), equals the
    AJ4-shaped closed form log theta(e^a) + log((1+theta(e^a))/2)
    to 1e-60.  The GG-normalized dual at d=1 IS the self-dual
    Jacobi theta: the forced normalization recovers the canonical
    statement, with zero choices.
(p;2) INERT (RG2): full NN census rerun under chi_GG (132 classes,
    109 admissible, 0 unresolved): n_1 = 0 for every class (forced:
    all census supports are depth >= 2), m+_GG - m+ = 0 EXACTLY on
    every class, 0 signs moved.  DECISION CELL (11;2)@4.96:
    m+_GG = -2.214249e-3, CERTIFIED < 0, UNCHANGED (= NN's frozen
    value).  OO's mode split (hole vs race, sec 0) is CONFIRMED from
    the second side: the mechanism aimed at the hole does not touch
    the race.
WHY THE RESTRICTION TO DEPTH-1 IS FORCED (not a choice): the
    continuum hole -1/u provably lives ONLY at d=1 (NN G3 exact;
    NN G2: at d >= 2 the dual approaches its rho_T floor with NO
    hole).  Attaching the unit to a depth-2 class would cancel a
    deficit that is not a hole - the LL6 atom-padding move again,
    with a GG label (a uniform per-place unit at (11;2) would flip
    it: gain +3.7e-3 > 2.21e-3 - but there is nothing there for it
    to be; G-INT6 forbids the retune).
ADJUNCTION BOUNDARY (RG3, flagged record): chi_GG is GRAPH-SUPPORT
    data, comb-invisible: [11^2]+[17] (same comb as (11;2), n_1 = 1)
    repairs to +1.45e-3 while the bare cell stays at -2.21e-3.  The
    unit cannot be carried by comb data; "repair by adjoining
    comb-invisible support" is an unbounded relabeling budget, not a
    face.  This is the F1 evasion's own boundary, witnessed.
```

### 3.2 F2 - all three registered kills land. F2 DEAD; X1 second
### clause met (a)+(b). One positive residue banked (sec 3.4).

```text
KILL (i) - certified negative aggregates at admissible points (RG4,
  RG5; banked Theta measure, no retuning):
  PER-PLACE (both unit variants): A_11(4.96) = -2.52e-3 (v) /
    -4.03e-4 (g), BOTH arb-certified < 0; also certified (g):
    A_5(3.419) = -2.03e-3, A_7(4.092) = -1.15e-3, A_13(5.330)
    = -2.6e-4.  The Theta-weighted ladder aggregate fails at every
    (p;2) window entry, p >= 5: the deeper-step surpluses available
    AT THAT PLACE never pay the entry deficit (at p >= 11 there ARE
    no deeper in-window steps; the k=1 slot pays +0 (g, bound 1e-50)
    or -e^{-a}/2-scale (v)).
  GLOBAL, verbatim unit: NEGATIVE on the ENTIRE grid [2.1, 6.0]
    (neg-frac 1.00; certified -1.45e-2 at 4.96, -1.21e-2 at a = 6):
    with the atom-inserted unit the aggregate face fails globally.
KILL (ii) - the breaking directions are unavoidable (RG6, RG7):
  EXACT: the sample direction c = (1, 0, 1) is PSD-Toeplitz boundary
    (minors 1, 1, det 0 exact; eigs {0,1,2}) with nonnegative
    entries: an ADMISSIBLE quadratic-test direction (HH H5a) loading
    ONLY the breaking k=2 slot with ZERO weight on k=1.  No scalar
    aggregate can dominate a class the admissible cone isolates:
    aggregate positivity cannot certify dual-cone membership.
  EXACT per-place LP (p = 11, a = 4.96): variant v INFEASIBLE
    outright (both slot margins certified < 0); variant g: any
    positive measure must charge (11;2) less than 5e-48 of its
    k=1 mass - no meaningful per-place measure exists.
  GLOBAL LP (float-grade records, HiGHS): banked Theta INFEASIBLE
    under v, FEASIBLE under g; free-support feasible both, max
    density on (11;2) (rel. Theta) 0.938, max breaking-block 0.996;
    all floor variants feasible.  The feasible cone is fat ONLY
    because cross-place subsidy is allowed - per-place it is empty
    (exact, above).
KILL (iii) - doc-16 check (RG10): z < 3 at gamma_1..5 in both frozen
  aggregate series (max |z| = 0.7): no zero content; the aggregate
  is comb-side computable by construction and is a SCALAR
  one-parameter family, not a PSD form over a test cone - it cannot
  be level-1 Bochner; it is strictly WEAKER than Weil positivity
  (kill ii is the precise sense).  No face gain available even where
  it is positive.
```

### 3.3 F3 - R3-b: the deficits are not counts. X4 MET.

```text
QUANTIZATION FLOOR (RG8, the decisive test): 15 certified deficits,
  -m+ in [1.06e-3, 0.361] - ALL strictly inside (0, log 2).  A
  genuine count has h^1 in {0} u [log 2, oo): 0 contradicts the
  certified negativity; log 2 overshoots the decision cell by x314.
  The deficits also vary CONTINUOUSLY in a (smooth e^{-a}/2 law at
  d=1; 512-pt frozen scans): no quantized observable does that.
NO PLACE STRUCTURE: d=1 deficit place-independent EXACTLY
  (m+([2]) - m+([5]) = 0 in arb): a count carrying the Lambda(p) =
  log p atom cannot forget p.  Additivity over disjoint supports
  FAILS: dev -19% ({5,11}@4.96), -238% ({7,11}@4.96), -128%
  ({11,13}@5.33) - all deviations NEGATIVE (union breaks worse than
  the sum: the deficits compound, counts would add).
NOT A CROSSING EVENT: sign changes per period = 2 with BOTH signs
  recurring EVERY period (p in {5,7,11,13,17}) - the deficit is
  permanent-periodic (log p^2 recurrence), not a one-time divisor-
  crossing jump that a genuine h^1 increment would produce.
CONSEQUENCE: the only definition left is h^1 := max(0, -m+) - the
  relabeling OO's F3(iii) pre-named as the G-INT6 kill.  X4 met.
```

### 3.4 The positive residue (banked, new)

THE GLOBAL GG-REPAIRED AGGREGATE HOLDS: A_g(a) > 0 on the whole
scanned window [2.1, 6.0] (min e^a-scaled +0.96; arb-certified
+3.03e-2 at the decision scale 4.96).  Read with the per-place
infeasibility (exact): the window-entry deficits ARE jointly payable
by the banked KMS-1/2 measure - but ONLY cross-place. No per-place
positive measure exists (the p=11 family is exactly infeasible), yet
the place-sum with HH's banked weights pays every deficit on the
scanned window. This is HH's joint-cancellation reading and doc 35's
class/scale-coupled unit spec confirmed QUANTITATIVELY at the index
face: the coupled unit must thread places together (the subsidy that
pays (11;2) at a = 4.96 comes from p = 2, 3 deep steps at the same
scale); it cannot be localized at the place, exactly as it cannot be
inserted as an atom at the class. Doc 16 keeps this honest: the
positive global aggregate carries no zero content (z < 3) and is
weaker than Weil positivity - it is a SPEC measurement, not a face.

## 4. Verdict against OO sec 4 (the exhaustion criterion)

```text
X1 (E3 closed): MET, both clauses.  F1: (p;2) window-entry negatives
    UNCHANGED under the forced GG normalization (subtraction provably
    inert at depth >= 2; decision cell certified).  F2: (a) certified
    negative aggregates at admissible rung/phases (per-place, both
    variants; global under v) AND (b) the (p;2) directions are
    exposed/admissible (exact PSD-boundary direction isolating the
    breaking slot; per-place LP exactly infeasible).
X4 (loophole closed): MET.  Deficits not count-shaped (quantization
    floor, exact place-forgetting, failed additivity, periodic
    recurrence); h^1 definable only as max(0, -m+) = relabeling.
X2, X3: not this cycle's scope (F5 transport test; F4 C6' gate;
    F6/F8 parked external).  Per OO's spend order these are the
    remaining opens of option 2.
NO SURVIVAL: no face in this cycle holds on the full decision set
    including (11;2)@4.96 without an unbanked choice.
```

## 5. Witness-engineering record (disclosed)

Run 1: ALL gates passed as registered, exit 0, no predicate touched.
Run 2 changes, display/record only: (a) the sign-display map in the
record lines was scrambled in run 1 ("+-0"[s] indexing; all GATE
decisions used resolved_sign directly and were unaffected; mids were
printed correctly); fixed to an explicit dict. (b) LP records: added
the explicit "banked Theta itself feasible?" line and a second floor
parametrization (uniform-in-density = Theta-proportional in measure
units), with the density-vs-measure parametrization disclosed inline;
both floor readings recorded, no verdict touched. (c) annotation of
the exact-+0 variant-g aggregates where only k=1 is in window.
Breaking-set selection: the doc registered "first-neg + 0.2"; the
witness evaluates BOTH those points and the first-period argmin
(gating < 0 on the argmin and the decision cell; one registered point
could in principle have left its negative phase - none did; all 15
certified). Runs 2-3 identical including the freeze hash.

## 6. G-INT6 ledger

```text
input                          choices spent
chi_GG normalization           0 (GG4 forced; n_1 from graph support;
                               depth-1 restriction forced by where the
                               hole provably is - NN G2/G3)
F2 measure                     0 (HH's banked Theta_p = 2 p^{-k/2}
                               verbatim; no retuning anywhere)
F1 d=1 cert points {0.5,1,2}   calibration (NN G3d lesson, disclosed
                               at registration; a >= 2.48 by bound)
adjunction class [11^2]+[17]   FLAGGED record, no decision weight
LP floors/parametrization      records only, both readings run
grids / scan ranges            calibration (NN G9 ranges inherited)
zeros                          fork_lib.zeta_gammas, post-freeze,
                               comparison only (z < 3 everywhere)
```

## 7. Honest limits

- Global A_g positivity is grid-scanned on [2.1, 6.0] with arb
  certification at named points only; not proved for all a (the
  e^{-a}-scale decay of both deficits and surpluses suggests but does
  not prove persistence). It is reported as a measurement (spec
  evidence), not a theorem.
- Global LP outputs are float-grade (HiGHS); the decisive per-place
  infeasibility statements are exact/arb and do not rely on them.
- The exposure kill is at the sample-direction level ((1,0,1) in the
  moment cone, exact); an explicit banked-class test function
  realizing it was not constructed (the cone statement is OO's
  registered criterion).
- m1_GG is treated as +0 in variant-g aggregates with the proven
  bound 3 e^{-pi e^{2a}} < 1e-50 (RG1d); at a in {0.5, 1, 2} it is
  computed and certified directly.
- F3's additivity/sign-structure tests are on a finite registered
  family; the quantization-floor argument is the load-bearing one
  and is certified on the full breaking set.
- Nothing here touches the canonical AJ4 statement (which F1's exact
  d=1 repair in fact RECOVERS); the failures are of the lattice
  faces, as registered.

## 8. Hand-off

```text
VERDICTS:  R1-b, R2-kill(i,ii,iii), R3-b.  X1 MET (both clauses),
           X4 MET.  Option 2 now waits only on X2 (F5 transport
           test) and X3 (F4 C6' gate; F6/F8 recorded blocked).
DECISION CELL: (11;2)@4.96 m+_GG = -2.214249e-3 certified < 0,
           UNCHANGED under the forced normalization; A_11(4.96)
           = -2.52e-3 (v) / -4.03e-4 (g), both certified.
BANKED:    (1) GG's forced unit repairs the d=1 hole EXACTLY (the
           repaired dual IS the self-dual theta); (2) the deficits
           are payable by the banked Theta measure ONLY cross-place
           (global A_g > 0 on the window, per-place exactly
           infeasible): the coupled-unit spec, quantified; (3) the
           deficits are sub-quantization continuum objects, not
           counts; (4) chi_GG is comb-invisible support data - the
           unit cannot ride on comb classes.
WITNESS:   prime_rr_face_cycle.py, exit 0, deterministic (runs 2-3
           identical, freeze f036d4b6...); inherited rerun
           prime_nn_graph_class_index exit 0 before any new work.
```
