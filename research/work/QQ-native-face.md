# QQ - Face hunt, candidate 2: the native-pairing face - the index inequality posed ON the glued objects G_p

Status: fresh-context worker QQ, 2026-06-10. Required reading executed in
order: doc 35 (the N-c kill and the transport caveat), NN-graph-class-test.md
(breakage map), Z-u2-gluing.md IN FULL (G, the K2 pairing as structure),
CC-gluing-consolidation.md part 1 (native pairings at p = 3, 5),
EE-dd4-lin.md (Theorem EE.1, the Lin block singleton-dual),
LL-square-dual.md + KK-L1-density-rr.md (dual-count and effectivity
machinery). Inherited witnesses rerun by me BEFORE any new work:
prime_int_z_u2_glue (ALL PASS ZG1-ZG8, exit 0), prime_int_ee_dd4_lin
(ALL PASS EEG1-EEG8, exit 0), prime_int_ll_square_dual (ALL PASS LL1-LL7,
exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_qq_native_face_index

Sections 0-2 (the construction, the hand derivations, the gates, the
registered predictions) were written BEFORE the witness was first run.
DISCLOSURE (NN/LL precedent): sec 1 contains design-stage hand
derivations (the per-slot inversion structure, the partition identity,
the deficit positivity and its tail rates, the closed form
C* = gamma + log pi for the deficit integral, the colimit divergence,
the two-place non-summability). They are derivations, not fits; the
witness checks them fail-closed and any mismatch is a FAIL.

Discipline: F-a (no zeta values, no zeta continuation; atom series are
exact rational functions; the divided-power dual refuses Laurent - Z
sec 6's guard inherited). G-INT6: the Gaussian weighting e^{-pi w^2} is
imported as in JJ (logged, the ONLY analytic import); NO other choices -
every other ingredient below is forced (ledger in sec 6). Carrier guard:
no ring => no G_p (Z/CC; gate QQ9). ZERO CONTACT: none anywhere in this
test (every locus below is log p-periodic by construction); the freeze
protocol is therefore never triggered - registered in advance: if any
gate had emitted a zero-flavored series it would be sha256-frozen before
any fork_lib import, per II/NN; none does and fork_lib is never imported.

## 0. The question, the evasion hypothesis, and the registered verdicts

Doc 35 (N-c): NN's duals off the integer lattice were FE-TRANSPORTED -
the dual was computed by transporting the functional equation onto
classes where no pairing lives, and the FE-stripped dual carried an
exact continuum hole (-1/u). The kill covers the forced lattice
embedding, not every conceivable face (NN sec 8).

EVASION HYPOTHESIS (E1): on the glued objects G_p the pairing IS the
object (K2 proven at p = 2, 3, 5: Z ZG2/ZG3, CC OG2/OG3; the Lin block
singleton-dual: Theorem EE.1). The dual of a class is its literal
pairing-image on the divided-power branch - no transport, no
resummation of a divergent series. If the native dual count is finite
and the index inequality holds on G_p's classes including the
Lambda(p)-analogue killers, the continuum hole never appears because
nothing was stripped.

PRE-REGISTERED VERDICT TABLE (task card, fixed before any computation):

```text
(Q-a) native dual counts are FINITE (including in the colimit over the
      divided-power branch) AND the inequality holds on G_p's classes
      including the killers (weight-1 classes, window-entry phases) ->
      the face evades; the margin structure becomes the LS3/LS4
      target; escalate.
(Q-b) partial (e.g. an exact native form holds including the killers
      while a smoothed/archimedean form fails, or finiteness holds
      while a killer fails) -> boundary mapped; report the split.
(Q-c) the hole reappears natively: the divided-power colimit count
      DIVERGES, or the killers fail on the native form ->
      face-independence datum for the exhaustion criterion.
```

FAIL-CLOSED: (Q-c) is full-value; nothing below is tuned to avoid it.

REGISTERED OVERALL PREDICTION (written before any run; both ways
carried): the central hope FAILS in its strong form - the divided-power
colimit count is predicted to DIVERGE (sec 1.4: the per-branch pole of
CC QG2 is the hole's native carrier; it was never a transport artifact)
- so the registered criterion lands (Q-c). The predicted yield en route
is (Q-b)-grade: the EXACT native form of the inequality (hard window
counts) is a one-line THEOREM on G_p including the killers, and the
entire gap localizes in the Gaussian import as a canonical, per-place,
log p-periodic, window-entry-phased deficit whose period-mean is
(gamma + log pi)/log p - doc 35's coupled-unit spec materializing as a
structure rather than a missing insertion. If instead the colimit count
converges, (Q-a) is live and the verdict escalates - that would be a
reportable shock refuting the hand derivation of sec 1.4.

## 1. The construction (hand derivations, written before any run)

### 1.1 The slot lattice, the classes, and the native dual

G_p's slots (Z sec 2, CC sec 2.1): one F_p-line per weight m; at p = 2
the bigraded slots (j, m) are t-periodic in degree j (t invertible), so
counts are taken per degree-orbit - one slot per weight m in Z; at odd
p the degree is locked to the weight (4m to 2m) and there is one slot
per weight outright. D-branch: m >= 1 (z^m / y^m); Lin/gluing slot:
m = 0, counted ONCE (Z 2.2 - the unit class is IN the object, native);
divided-power branch: the dual slots gamma_m, mirror weight -m, m >= 1.

Slot atoms (the doc-19/20 dictionary as consolidated in CC part 3
stratum L-i, already spent): slot m carries atom p^m; the mirror slot
gamma_m carries atom p^{-m}. CLASSES: a class C is a finite set of
weights (a sub-object spanned by slots); the primary family is the
weight-truncations C_N = {0, 1, ..., N} (the level-N truncation of the
tower, U/Z/CC), plus singletons - in particular the WEIGHT-1 CLASS {1}
(the address of [p], the Lambda(p) atom: NN's always-breaking class)
- and sub-boxes. K2-IMAGE: at level N the pairing pairs m with N - m
(Gram = permutation, Z ZG2/CC OG2: the image of C_N is the full dual
level {gamma_0..gamma_N}); stably the flip is m <-> -m (the image of C
is C^dual = {-m : m in C} on the divided-power branch). Both EXIST
natively - no transport. EE.1: at m = 0 the duality datum is a
singleton (theorem), so the unit slot's self-pairing spends no choice.

### 1.2 The count (the one logged import) and the dual scale (forced)

Count, primal, at scale a (the Gaussian import, JJ, logged):

    Theta_C(a)  = sum_{m in C} f(x_m),   f(x) = e^{-pi x^2},
    x_m = e^{-a} p^m   (slot weight = scale times atom),
    N_w(C; a)   = #{m in C : x_m <= 1}   (hard effectivity count:
                  AJ6/KK's unit-ball notion, slotwise).

Count, dual, of the K2-image, native: the duality covers s -> -s
(weight inversion + degree inversion; Z sec 3), so the dual scale is
-a and the image slot -m has weight e^{+a} p^{-m} = 1/x_m:

    Theta^dual_C(a) = sum_{m in C} f(1/x_m),
    N_w^dual(C; a)  = #{m in C : x_m >= 1}.

FORCED, NOT CHOSEN (gate QQ2): the finite-level route gives the same
per-slot value - at level N the image of m is gamma_{N-m}; reading the
dual level through its own tower presentation (atom p^{N-m}) at the
RR-canonical dual scale a^dual = N log p - a (= deg K_N - a, the
classical g-shift; the degree of the level-N dualizing slot is N log p)
gives weight e^{-(N log p - a)} p^{N-m} = e^{a} p^{-m} = 1/x_m: the
exponent identity -(N - k)L + (N - m)L = (k - m)L, L = log p, a = kL,
is exact. The stable and level routes agree slotwise; per-slot WEIGHT
INVERSION x <-> 1/x is the invariant content of the K2 flip.

Native chi: chi(C) = |C| - the slot dimension (each slot one F_p-line;
the Euler measure of a complex of lines with no native H^1). At level
N: chi(C_N) = N + 1.

### 1.3 The inequality, natively: hand derivations

THE HARD (EXACT) FORM. For every slot, x_m <= 1 or x_m >= 1, with both
iff x_m = 1 (the tie: window entry, a = m log p exactly). Hence the
PARTITION IDENTITY (one line, theorem-grade):

    N_w(C; a) + N_w^dual(C; a) = |C| + #{m in C : x_m = 1}
                               >= chi(C),

with equality off ties and margin +1 exactly at window-entry phases.
REGISTERED PREDICTION P1: the hard form HOLDS on every class, every a,
every p - INCLUDING the killers (the weight-1 class at its window
entry a = log p gives margin +1, never a deficit). The K2 pairing
makes the index inequality a partition statement: each slot is counted
on exactly one side, because the dual weight is the literal inverse.
This is what "the pairing is the object" buys; NN's transported dual
could not see it because off the lattice there is no second slot.

THE SMOOTHED FORM (the archimedean import switched on). Per slot the
Gaussian pair mass is f(x) + f(1/x) and the hand inequality

    d(x) := 1 - f(x) - f(1/x) > 0   for ALL x in (0, oo)

is strict (at x = 1: d = 1 - 2e^{-pi} ~ 0.9136, the maximum; tails
d(e^u) = pi e^{-2|u|} (1 + o(1)) as |u| -> oo). REGISTERED PREDICTION
P2: the smoothed inequality Theta_C + Theta^dual_C >= chi(C) = |C|
FAILS for every nonempty class at every scale, with margin exactly
-Delta_C(a), Delta_C(a) = sum_{m in C} d(x_m) > 0, MAXIMAL on the
killer phases: the weight-1 class at window entry has margin
-(1 - 2e^{-pi}) ~ -0.9136. The deficit is largest exactly where the
slot crosses the window - the window-entry phase structure of NN's
breakage map, reappearing natively with no transport.

### 1.4 Native finiteness (the central hope), tested first - and the
### registered prediction that it fails

Per-level dual counts are finite by construction (|C_N| = N + 1 terms;
the colimit-of-finite-levels structure is honored slot by slot). The
COLIMIT dual count - the count of the whole divided-power branch - is

    sum_{m >= 1} f(e^{a} p^{-m}),   terms -> f(0+) = 1:

REGISTERED PREDICTION P3: DIVERGES (linearly in the truncation level)
for every a and every p; equally the hard count N_w^dual(full branch)
= #{m : p^{-m} <= e^{a}} is infinite. Certified form (gate QQ5): by
1 - e^{-y} <= y, the M-th increment block satisfies S_2M - S_M >=
M (1 - pi e^{2a} p^{-2M}). The mechanism is BANKED, not new: CC QG2 -
each branch ALONE inherits the simple pole at s = 0 (atom series
A_D'(s) = sum_m (p^{-m})^{-s}, residue -1/log p), cancelled only by
pairing against the primal branch (A_D + A_D' + 1 = 0, exact). NN's
continuum hole -1/u was therefore NOT a transport artifact: natively,
with nothing stripped, the hole is the divided-power branch's own pole
- infinitely many mirror slots sit inside every window. The native
face RELOCATES the hole from a stripped term to a per-branch pole; it
does not remove it.

### 1.5 The deficit as the gap object (the boundary map)

Single place: Delta_p(a) := sum_{m in Z} d(e^{-a} p^m) converges
(geometric tails), is EXACTLY log p-periodic in a (index shift), has
maxima at window-entry phases (a = 0 mod log p, where some x_m = 1)
and minima at half-phase. HAND DERIVATION (registered closed form):
its period-mean is C*/log p with

    C* = int_R d(e^u) du = gamma + log pi = 1.72200...,

derivation: C* = 2 int_0^oo (1_{x<1} - e^{-pi x^2}) dx/x; substituting
t = pi x^2 (dt/t = 2 dx/x) gives int_0^oo (1_{t<pi} - e^{-t}) dt/t =
gamma + log pi by the classical Frullani/gamma integral
gamma = int_0^1 (1-e^{-t}) dt/t - int_1^oo e^{-t} dt/t plus
int_1^pi dt/t. So the native smoothed gap per place is THE ARCHIMEDEAN
CONSTANT gamma + log pi per log p of scale - the EF's archimedean unit,
emerging from the Gaussian-vs-partition deficit with no EF input.
REGISTERED PREDICTION P4: Delta_p periodic to truncation accuracy,
period-mean = (gamma + log pi)/log p to 1e-6, max at entry phase.
DEMOTED READING (logged, no headline weight): with the renormalized
chi_ren(C; a) := |C| - Delta_p(a), the smoothed inequality holds for
ALL single-place classes including the killers, by termwise positivity
(Delta_C <= Delta_p, subset monotonicity), with equality in the
colimit. The counterweight is canonical (constructed from the same
pairing + import, class-independent) but presenting it as chi is a
reading, not a forced identity - it is the measured shape of the gap:
one continuum unit per place, paid at each window-entry phase, doc
35's spec with its constant now NAMED.

### 1.6 Cross-place assembly (GG normalization), registered

Two places p < q: product classes, slot (m, n), atom p^m q^n, weight
x = e^{-a} p^m q^n; the K2-image flips both (CC's place-uniform
pairing; GG's assembly). The hard partition identity is UNCHANGED
(weight inversion is weight inversion). REGISTERED PREDICTION P5: the
two-place colimit deficit sum_{(m,n) in Z^2} d(e^{-a} p^m q^n)
DIVERGES: for every m there is n*(m) with |m log p + n* log q - a| <=
(log q)/2, so each m contributes >= d(q^{1/2}) > 0 - linearly many
O(1) contributions (the log-lattice is dense at the window boundary).
This is GG3's non-summability ("the place-sum of survivors exists only
after subtracting one continuum unit per place") in count dress: the
per-place counterweight Delta_p does NOT assemble naively. REGISTERED
PREDICTION P6 (the failure boundary, both ways carried): for product
truncation boxes C = [0..N]^2 at T = {2,3} there is a SMALL N
(predicted N <= 12) and a phase a with Delta_C(a) > Delta_2(a) +
Delta_3(a): the one-unit-per-place budget is exceeded by a finite box
- named, certified. (If no failure box exists to N = 16 the
prediction is refuted and the per-place budget is reported as
sufficient on the tested range - reportable either way.)

## 2. PRE-REGISTERED GATES (written before the first run)

Evaluation rules fixed in advance: exact integer/Fraction arithmetic
for all algebra (pairing Grams, insertion compatibility, exponent
identities, tie bookkeeping, rational-function pole identities); flint
arb prec 300 for every analytic value; deficit/theta truncations
carry certified geometric tail bounds added into the ball radius; sign
decisions only when the arb ball resolves the sign. Scales a are taken
either as exact rational multiples of log p (entry phases; ties exact
by integer comparison) or as generic rationals (no tie: p^m != e^a for
a rational nonzero - transcendence of e^a at rational a != 0, Hermite;
certified numerically by balls excluding 1). No RH / zero-side input;
fork_lib never imported.

```text
QQ1 NATIVE CARRIER + PAIRING (exact, replicating Z/CC minimally):
    p in {2,3,5}, levels N <= 8: level-N Gram <m, m'> = delta_{m',N-m}
    is a permutation; colimit insertion compatibility iota_{N+1}(z m)
    = iota_N(m) on all slots; divided-power products gamma_a gamma_b
    = C(a+b,a) mod p gamma_{a+b} (Lucas spot checks, exact); stable
    flip = m <-> -m. FAIL: any mismatch. (The dual slots EXIST
    natively or there is no face.)
QQ2 DUAL SCALE FORCED (route equality, exact): the stable-route dual
    weight e^{a} p^{-m} equals the level-route weight
    e^{-(N log p - a)} p^{N-m} as an EXACT exponent identity in
    Fractions (a = k log p, all 0 <= m, k <= N <= 8, p in {2,3,5}).
    FAIL: any mismatch (then the dual scale is a choice, and the
    construction loses its forced status - reported, full stop).
QQ3 DEFICIT POSITIVITY (arb): d(e^u) > 0 sign-resolved on u in
    [-6, 6] step 0.01; tail clause at u in {6, 8, 10}:
    e^{-pi e^{2u}} / (1 - e^{-pi e^{-2u}}) < 1e-40 (so d > 0 there),
    plus the hand tail rate |d(e^u) e^{2|u|} - pi| < 0.1 at |u| = 8.
    FAIL: any unresolved sign or clause.
QQ4 HARD PARTITION IDENTITY (exact; the native-form killer test):
    p in {2,3,5}; classes C_N (N in {0,1,2,4,8,12}), the weight-1
    killer {1}, the box {1,2,3}; scales: entry phases a = k log p
    (k in {0,1,2,3}, ties exact) and generic a in {1/2, 1, 5/2, 5}:
    N_w + N_w^dual - |C| = #ties, with #ties = 1 exactly at the
    killer's window entry and 0 at generic scales. STRUCTURAL GATE:
    identity exact everywhere; any certified deficit -> killer FAILS
    natively -> (Q-c) evidence.
QQ5 NATIVE FINITENESS (the central hope; decision gate, fail-closed):
    (a) per-level finiteness: structural (finite slot sets; printed);
    (b) COLIMIT DIVERGENCE: p in {2,3,5}, a in {1/2, 2, 5}:
        S_2M - S_M >= M (1 - pi e^{2a} p^{-2M}) certified (arb) at
        M in {20, 40}, and S_60 >= 0.8 (60 - a/log p - 2) (terms -> 1
        above the window crossing);
    (c) the pole is the branch's own (CC QG2 minimal replication):
        A_D + A_D' + 1 = 0 at x = p^{-s} exact (Fractions, 5 sample
        s per p), per-branch residues +-1/log p (arb, 1e-30).
    REGISTERED: (b) certifying divergence CONFIRMS P3 -> the (Q-c)
    criterion's first disjunct lands. A FAILURE of (b) (bounded
    partial sums) would REFUTE P3 and re-open (Q-a): reportable
    shock; gate then FAILS (prediction wrong), fail-closed.
QQ6 SMOOTHED-FORM KILLER CENSUS (arb, signs resolved): margins
    Theta_C + Theta^dual_C - |C| for: killer {1} at p in {2,3,5},
    a in {1/2, log p, 1, 2, 2 log p, 5} and a 16-point phase scan
    over one full period [log p, 2 log p] at p in {2, 5}; C_N for
    N in {2,4,8} at a in {1, 2.48, 4.96}. REGISTERED: every margin
    certified NEGATIVE (= -Delta_C < 0); killer at entry =
    -(1 - 2 e^{-pi}) to 1e-30. Log-form (JJ/NN-comparable) margins
    log Theta + log Theta^dual - log|C| RECORDED (no gate weight).
    STRUCTURAL GATE: all signs arb-resolved; the census is the
    verdict input.
QQ7 THE DEFICIT OBJECT (boundary map): p in {2,3,5}:
    (a) periodicity: |Delta_p(a) - Delta_p(a + log p)| < 1e-28
        (truncation M with certified tail < 1e-30);
    (b) phase structure over one period (32-pt grid): max at the
        entry phase (within grid resolution), max - min > 0 certified;
    (c) period-mean: |mean * log p - (gamma + log pi)| < 1e-6
        (trapezoid over one period, 256 pts; the function is analytic
        and periodic - exponential trapezoid convergence; tolerance
        absorbs it); arb gamma = const_euler;
    (d) domination (the demoted chi_ren reading): Delta_C(a) <=
        Delta_p(a) for every QQ6 class/scale (termwise subset sum;
        exact given (a)'s truncation control).
QQ8 CROSS-PLACE (GG normalization test), T = {2,3} and {2,5}:
    (a) colimit non-summability: sum over |m| <= M of
        d(at nearest-lattice phase) >= (2M+1) d_q where d_q =
        certified arb lower bound min(d(e^u): |u| <= log q/2) > 0.4
        (d evaluated on a 64-pt grid + the QQ3 grid certification;
        monotonicity in |u| checked on the grid), M = 50: the
        two-place deficit grows linearly - GG3 native;
    (b) the failure boundary: product boxes [0..N]^2, N <= 16,
        scales a in {1.24, 2.48, 4.96} plus an 8-pt phase grid in
        [4.96, 4.96 + log 6) (the box window must CROSS the scale for
        the boundary population to exist): find the smallest N with
        Delta_box(a) > Delta_2(a) + Delta_3(a) certified;
        REGISTERED: exists with N <= 12 (P6); if none to N = 16,
        P6 is refuted and reported (gate then records the refutation;
        structural gate = census computed + signs resolved).
QQ9 CARRIER GUARD (exact integers; LL7/GG6 replication): Epstein
    x^2 + 5y^2: 36 = 4*9 = 6*6 with 4, 6, 9 irreducible (exact
    enumeration) => no valuation => no weight grading => no truncation
    tower => no Matlis colimit => NO G_Epstein: the native count is
    UNFORMABLE (no ring => no G_p, as charged). DH: no carrier monoid
    at all (bookkeeping, printed). FAIL: any clause.
```

Registered overall verdict logic (before the run): IF QQ5(b) certifies
divergence -> the registered (Q-c) criterion lands on its first
disjunct, FULL VALUE, regardless of how clean the rest is. The split
findings (QQ4 exact form holds incl. killers; QQ6 smoothed census all
negative; QQ7 the canonical deficit; QQ8 the cross-place wall) are then
the (Q-b)-grade boundary map REPORTED INSIDE a (Q-c) verdict: the face
does not evade NN's kill - it re-expresses it, and the re-expression is
the yield. IF QQ5(b) fails (convergence): P3 refuted, escalate to
(Q-a) analysis in a follow-up section (none of the other gates change).
IF QQ4 finds a certified native killer deficit: (Q-c) on the second
disjunct as well.

---- verdict sections written after the runs ----

## 3. VERDICT: (Q-c) ON THE REGISTERED CRITERION - the hole reappears
## natively (the divided-power colimit count diverges) - WITH the full
## (Q-b)-grade boundary map as the yield

Witness ALL PASS (QQ1-QQ9, exit 0), deterministic across 3 runs (logs
/tmp/qq_run2-4.log, diff-identical). Witness-engineering record
(disclosed): one harness API fix after the aborted first invocation
(python-flint arb has no .abs() method; replaced by builtin abs();
QQ1/QQ2 had already PASSed before the crash in QQ3's reporting line);
no gate predicate touched at any point; all decision values from the
first complete run reproduced identically in runs 2-3.

### 3.1 The central hope (E1), answered

NATIVE FINITENESS FAILS - registered prediction P3 confirmed, certified
(QQ5): per-level dual counts are finite (the colimit-of-finite-levels
structure is honored slot by slot; NOTHING IS STRIPPED - there is no
-1/u term, no FE transport, no missing unit at any finite level), and
yet the colimit count of the divided-power branch DIVERGES, linearly,
one unit per level (S_40 - S_20 = 20.000000 at p = 2, a = 2; certified
lower bounds at all p in {2,3,5}, a in {1/2, 2, 5}). The mechanism is
the branch's OWN pole (CC QG2, re-certified: A_D + A_D' + 1 = 0 exact,
per-branch residues +-1/log p): infinitely many mirror slots sit inside
every window because the mirror atoms p^{-m} accumulate at 0.

CONSEQUENCE FOR THE FACE HUNT: NN's continuum hole was NOT a transport
artifact. E1 is refuted in its strong form: computing the dual natively
(literal pairing-image, no FE, no resummation) relocates the hole from
a stripped continuum term to the divided-power branch's own pole - it
does not remove it. The hole is FACE-INDEPENDENT across both faces now
tested (transported lattice duals, native pairing duals): this is the
face-independence datum for the exhaustion criterion, full value.

### 3.2 What the native face nevertheless proves (the boundary map)

(i) THE HARD FORM IS A THEOREM (QQ4, exact, all classes/scales/places):

    N_w(C; a) + N_w^dual(C; a) = |C| + #ties >= chi(C) = |C|,

because the K2 pairing inverts slot weights exactly (x <-> 1/x; QQ2:
the stable and finite-level routes agree slotwise, the dual scale is
forced, deg K_N = N log p emerges as the classical g-shift). Every
slot is counted on exactly one side; the Lambda(p)-analogue killers
CANNOT break it - the weight-1 class at its window entry a = log p
yields margin +1 (the tie), never a deficit. On the native face the
index inequality, in counting form, is a PARTITION IDENTITY of the
duality. NN's killers had no native analogue to kill: where the
pairing is the object, the dual slot is always there to catch what
leaves the primal window.

(ii) THE ENTIRE GAP IS THE ARCHIMEDEAN IMPORT (QQ3 + QQ6): switching
on the Gaussian (the one logged import) creates a strictly positive
per-slot deficit d(x) = 1 - f(x) - f(1/x) > 0 (certified), maximal
exactly at window entry (d(1) = 1 - 2e^{-pi} = 0.91357...), with tails
pi e^{-2|u|}. The smoothed inequality vs the native chi = |C| FAILS for
every nonempty class at every scale (census all-negative, certified);
the weight-1 killer at entry has margin -(1 - 2e^{-pi}) to 1e-30,
PLACE-INDEPENDENT - precisely NN's place-independent k = 1 breakage,
reproduced natively with no transport. (Log-form record at entry:
log Theta + log Theta^dual = -2 pi exactly.) The native face thus
LOCALIZES doc 35's gap with no residue: exact duality layer - no gap
at all; archimedean layer - all of it.

(iii) THE GAP OBJECT IS CANONICAL AND ITS CONSTANT IS NAMED (QQ7): the
single-place colimit deficit Delta_p(a) = sum_m d(e^{-a} p^m) is
finite, EXACTLY log p-periodic, maximal at window-entry phases (amp
0.0047 / 0.0420 / 0.1754 at p = 2/3/5), and its period-mean satisfies

    mean(Delta_p) * log p = gamma + log pi    (certified to 1.5e-36),

the hand-derived closed form (sec 1.5, Frullani). The archimedean EF
constant gamma + log pi emerges from the Gaussian-vs-partition deficit
with NO explicit-formula input. Doc 35's terminal gap spec ("one
continuum unit per place, paid at each window-entry phase") is here
MATERIALIZED as a structure: Delta_p is class-independent, dominates
every class deficit (QQ7d, termwise positivity), so the demoted
chi_ren = |C| - Delta_p(a) reading makes the smoothed inequality hold
on ALL single-place classes including the killers, with equality in
the colimit. (Demoted because presenting chi_ren as chi is a reading;
the object itself is constructed, not inserted - unlike LL6's
hand-inserted atom, Delta_p is computed FROM the pairing + import.)

(iv) THE CROSS-PLACE WALL (QQ8): the two-place colimit deficit is
non-summable (101 of 101 m-rows contribute > 0.4 each at T = {2,3}
and {2,5}: the log-lattice is dense at the window boundary) - GG3's
"the place-sum exists only after subtracting one continuum unit per
place", in count dress. And the naive per-place budget FAILS at a
FINITE box: Delta_box > Delta_2 + Delta_3 already for the box [0..3]^2
at a = 1.24 (4.628 > 4.067, certified; prediction P6 confirmed, even
smaller than the registered N <= 12). The native counterweight exists
per place and does NOT assemble additively across places: the global
coupling must come from the unspent product formula (GG/Z's K1
attachment point), not from per-place padding.

### 3.3 Scale comparison with NN (honest, no identification claimed)

NN's killer margins were -e^{-a}/2 in log-count units on MONOID combs
(all integers); QQ's are O(1) in linear slot units on ONE place's atom
ladder (the monoid count is exponentially larger than the slot count:
h^0_slot ~ log(a/log p) vs h^0_monoid ~ a). The two faces carry the
same gap in different normalizations; no margin identification is
claimed (NN's G5 lesson), only the LOCUS identification, which is
exact: window-entry phases, log p^(period) recurrence, place-
independent weight-1 maximum.

## 4. G-INT6 ledger

```text
input                          choices spent
slot atoms p^m / p^{-m}        doc-19/20 dictionary via CC L-i (spent)
Gaussian e^{-pi w^2}           THE import (JJ, logged) - the only one
dual scale a^dual = -a         FORCED (duality covers s -> -s, Z sec 3;
                               route equality QQ2 exact)
chi = |C|                      native (slot dimension; F_p-lines)
classes (truncations/killers)  the task card's families; calibration
chi_ren = |C| - Delta_p        READING, demoted (sec 3.2(iii))
grids/scan ranges              calibration (registered before run 1;
                               two pre-run design corrections to QQ5b/
                               QQ8b disclosed in-place in sec 2's
                               history: the S_60 floor and the QQ8b
                               scale family, both fixed BEFORE the
                               witness existed)
zeros                          NONE (no zero contact; freeze protocol
                               never triggered, as registered)
```

## 5. Honest limits

- The hard-form partition identity is exact but COUNTING-WEAK: G_p's
  slot ladder is one prime's atoms; it does not see the monoid's
  exponential count (sec 3.3). The theorem is real and native, but the
  EF-grade content of the index inequality lives in the smoothed/
  global layers, exactly where the deficits are.
- "Max at entry phase" (QQ7b) is certified on a 32-pt grid (the p = 2
  amplitude is only 0.0047); the periodicity and the mean are the
  load-bearing clauses and are certified tightly.
- The chi_ren reading's "holds with equality in the colimit" is
  monotonicity of positive terms - near-tautological as a positivity
  statement; its content is the canonicity, class-independence, and
  the named constant of the counterweight, not the inequality itself.
- The QQ8b failure box depends on the tested scale family; smaller
  boxes might fail at other phases. The claim is existence (certified),
  not minimality over all scales.
- Everything is pi_*-level on G_p (Z/CC's standing limit); no
  spectrum-level statement; no H^1; no zero-side statement of any
  kind anywhere.
- e^a transcendental at rational a != 0 (Hermite) is invoked for
  exact no-tie bookkeeping at generic scales; numerically the balls
  resolve every sign regardless.

## 6. Hand-off (for the lead)

```text
VERDICT:   (Q-c) on the registered criterion - the native-pairing face
           does NOT evade: the divided-power colimit count diverges
           (certified), i.e. NN's continuum hole is the mirror
           branch's own pole (CC QG2), present with nothing stripped.
           The hole is now FACE-INDEPENDENT across both tested faces:
           exhaustion-criterion datum, full value.
BUT:       the native face splits the gap EXACTLY: (1) hard/duality
           layer: the index inequality is a one-line THEOREM (window
           partition of the K2 pairing; killers structurally cannot
           break it); (2) archimedean layer: the whole gap, as a
           canonical per-place deficit Delta_p(a), log p-periodic,
           window-entry-phased, period-mean (gamma + log pi)/log p
           (closed form certified to 1e-36) - doc 35's coupled-unit
           spec materialized as a computed structure with its
           constant named, NOT a hand insertion; (3) cross-place:
           Delta_p does not assemble (finite failure box [0..3]^2
           certified; two-place colimit non-summable = GG3): the
           coupling slot belongs to the product formula (unspent).
TARGET:    if LS3/LS4 inherits anything from this face, it is the
           OBJECT Delta_p(a) (and its named mean), not an inequality:
           the spine's coupled unit must restrict to Delta_p at each
           place and resolve the cross-place non-summability exactly
           where the product formula acts.
WITNESS:   prime_qq_native_face_index.py (QQ1-QQ9, ALL PASS, exit 0,
           ~0.4 s, deterministic x3); inherited reruns before any work:
           prime_int_z_u2_glue, prime_int_ee_dd4_lin,
           prime_int_ll_square_dual (ALL PASS, exit 0).
NO ZEROS:  no zero contact anywhere; freeze never triggered; every
           locus is log p-periodic by construction.
```
