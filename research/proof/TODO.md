# Proof Todo Tracker

Purpose: keep the proof program oriented around theorem-shaped checkpoints, not around an
ever-growing list of diagnostics. Diagnostics stay here only when they change the theorem target or
define a fail-closed test.

## Risk Ladder (2026-06-09 reorganization)

Order of work = order of assumptions by (probability of killing the program) x (cheapness of the
test). Highest-risk, cheapest-to-test first. Each rung is fail-closed: a negative outcome kills or
reshapes the target, and that is the point.

### R0 - The reduction is recorded, not certified

`00-reduction-to-rh.md` now states `nested target => RH` with obligations O1-O4 (normalization
audit, pole-term vanishing, off-line detection, CC20 base-case anchor). Provenance: CC20
arXiv:2006.13771 + Weil's converse. Risk: low (classical technology), but load-bearing - until
written, the program could drift onto a target that no longer implies RH. Also fixes the program's
one-line shape: **extend CC20's archimedean Sonin positivity past support log 2, paying with exact
Euler atoms.**

### R1 - The asymptotic-mechanism risk (HIGHEST; attack first)

The current candidate lemmas (sectoral edge-cone, atom placement, single-repair-atom) are built
from one late edge at R ~ 3.24. Two facts say the mechanism as phrased cannot be the asymptotic
mechanism:

```text
- cells near the edge have width ~ e^{-R}, and the window (L,R] contains ~ e^R atoms:
  single-atom repair degenerates into statistics of many atoms = the transgression
  int F phi' again, F = psi(e^U) - e^U;
- unconditional bounds on F are exponentially insufficient: |phi F| ~ e^{U/2 - c sqrt(U)}
  diverges relative to any O(1) Schur margin, so no absolute-value, cell-by-cell estimate
  can close the storage step at large R.
```

Two prongs, both cheap relative to what they decide:

```text
R1a (pencil): the inverse analysis. Quantify the candidate sectoral lemma over all
     edges L < R as R -> infinity and derive what it implies about F. If it implies
     psi(x) - x = O(x^{1/2+eps}) it is RH-equivalent, geometry alone can never deliver
     it, and the program must identify the weaker-arithmetic + stronger-geometry split.
R1b (numeric): the scaling ladder. Extend the nested chain to R ~ 4.5-6. Track per edge:
     eigmin(A) (induction margin), Riccati square cost, repair surplus
     (eigmin(H) / beta surplus), number of atoms participating in repair, DH control.
     Fail-closed: if the surplus decays faster than the margin, or repair stops being
     single-atom, the current lemma shape dies and the target reforms at the
     aggregated/statistical level.
```

Do R1 before investing further in T1 polish.

**R1 OUTCOMES (2026-06-09, see `09-inverse-analysis.md`):**

```text
R1b executed (prime_ladder_scaling.py, R to 5.90): zeta positive on all 18 edges,
    DH dead on all 18; eigmin(A) ~ e^{-1.5 R}; chronological peak debt grows to
    ~17 vs final margins ~3e-3; repair concentration falls past R~5.
R1a executed: (i) margins exponentially small => slack-bearing estimates can
    never close the induction; certificates must be exact-identity + terminal
    sign (KYP shape). (ii) Cluster obstruction: per-cell repair lemmas are
    unconditionally false at scale (Maynard triples). (iii) Window dial: the
    unconditional arithmetic input is short-interval PNT at the 7/12 scale; the
    remainder is the zero-side oscillation - conservation of difficulty located.
NEW PROBES: one-place passivity proposed and REFUTED same day
    (prime_single_place_passivity.py); drop-one/KMS rigidity
    (prime_interference_rigidity.py): every place and every atom individually
    necessary; positivity only at beta=1/2 (fails both sides). Positivity is an
    irreducibly collective interference lattice; support filtration is the only
    admissible induction coordinate.
NEXT (new R1 front): the killing-direction / repair-matrix characterization
    (09 section 6'.4) - do partial-sum killing directions have a multiplicative
    / free-semigroup combinatorial skeleton?

R1 CLOSED (later 2026-06-09, 09 sections 6''-6''''): resonance dictionary CONFIRMED
    (killing directions are frequency combs, repair = equidistribution of {log p},
    sign-match 1.000); margin law is arithmetic (W_inf alone dies at gmax~2.3,
    smooth surrogates permanently indefinite, only exact atoms positive); O1
    discharged numerically (explicit formula to 4.4e-13); and the CLOSURE: tested
    against admissible profiles the finite phenomenology telescopes to the explicit
    formula exactly (form eigmin = spectral min over actual zeros, validated).
    PHENOMENOLOGY PHASE COMPLETE - no further finite-window experiment can add
    proof content. The program's sole remaining shape: the prime-side realization
    (09 section 6''''.3), with inputs {free semigroup on log p, KMS beta=1/2,
    Lambda>=0, digamma supply} and graveyard guards {Conrey-Li, circular trace,
    subset inductions}.
```

### R-INT - The integer search (OPENED 2026-06-09, user-directed; THE front rung)

Target (docs 14-16, sharpest wall form): an integer-valued, positivity-bearing
pairing attached to Z that touches the zeros. Search design: candidates are
triples (L, <,>, Phi) - objects attached to Z, a pairing whose values are
CARDINALITIES BY DEFINITION (positivity never proven => RH cannot enter
through the sign; all risk concentrates in the comparison identity), and a
flow Phi playing Frobenius. Method: GENERATE candidates from a grammar of
count structures; FINGERPRINT each candidate's correlation sequence against
the EF (digamma + prime atoms) with the existing fork machinery; GATE
fail-closed.

Gates (all unconditional): G-INT1 integer gate (what does it count?);
G-INT2 comparison/fingerprint on the FULL pole-killed class (S4');
G-INT3 P2/Epstein gate (impossible for DH; must USE multiplicative closure -
verbatim-Epstein = over-proving, dies); G-INT4 trichotomy gate (not secretly
a square or Bochner form - level-2 fork, E3b machinery); G-INT5 no-scale
check (counts of GLOBAL objects only; never residue cardinalities at infinity
- the no-go configuration); G-INT6 degrees-of-freedom audit (added
2026-06-10, doc 21 sec 3: every ladder/dictionary claim ships a DOF
ledger - #independently-matched constraints must EXCEED #free modeling
choices (weight, scale, scheme, start, spacing), else it is calibration,
not derivation; prefer ring-bearing negative controls: THH(O_K) must
produce the DEDEKIND zeta_K supply, not zeta's).

Candidate grammar, ordered by tractability:

```text
C0 (calibration) - DONE, PASSES (count_fingerprint.py): the generic chain
   (counts -> Dirichlet-log recursion -> correlation profile -> fingerprint
   regression) returns k_hat = +2.0000 with residual 2.2e-16 on d(n); the
   AB and R2 cells show residuals supported ENTIRELY on prime powers with
   the predicted structures - the pipeline reports WHICH zeros a count
   structure touches. G-INT2 machinery operational.
C0' (normalization insight, from the ZN probe c(n) = n): count structures
   see zeros at the line set by their counting growth (zeta(s-1): k_hat
   blows up, no s=1/2 fingerprint). The critical line is reached precisely
   by SELF-DUAL count structures - d(n) sits at 1/2 because ab = n is
   a <-> b symmetric; the functional equation IS the count duality.
   GRAMMAR REFINEMENT: restrict the search to self-dual count structures
   (pairings with built-in symmetry) - i.e., intersection pairings on
   squares; G-INT2 refines to "fingerprint at the self-dual normalization".
C1 Orbit/fixed-point counts - SUBSUMED by doc 17 section 4 (2026-06-10):
   any self-dual tempered Euler count structure lands on Selberg-class
   fingerprints (the mapped reachable set); C1 instances would re-confirm
   the boundary, not extend it. The discriminating question is the
   SIGNATURE side (C4'), not more fingerprint rows.
C4 Hall pairing - EXECUTED (count_hall_signature.py + doc 17 sections 5-6):
   Hall numbers integer + symmetric (duality theorem, verified in-data);
   self-dual-grade forms POSITIVE DEFINITE all cells = metric, no index
   (consistent with PSH positivity). Structural why: the Euler form
   chi = log|Hom| - log|Ext| VANISHES IDENTICALLY on finite Z-modules
   (|Ext^1| = |Hom|) - the categorical form of "Spec Z is 1-dimensional"
   (third independent derivation). Index demands a 2-DIMENSIONAL category.
C4' - EXECUTED (prime_int_derived_square.py + doc 18, 2026-06-09): SIGN
   EXISTS. The derived self-intersection of the diagonal in the square
   Z (x)^L_S Z IS THH(Z) (by definition); Bokstedt's pi_{2k-1} = Z/k (all
   odd degrees) gives <Delta,Delta>_tors = -sum_reg log k = zeta'(0)
   = -(1/2) log 2pi < 0 - the first sign-bearing, torsion-sourced pairing
   on an arithmetic square in the program, and its value is the ARCHIMEDEAN
   CONSTANT of zeta, produced from integer counts rather than inserted.
   Genus reading: 2 - 2g_Z = zeta'(0) => g_Z ~ 1.459 > 1 (hyperbolic over
   S). Local control THH(F_p): +(1/2) log p. Gates: G-INT5 PASS, carrier
   fork PASS (DH/Epstein have no ring => no THH); G-INT1 degree-wise PASS /
   total FAIL - the non-integer enters ONLY through the infinite tower.
   WALL RELOCATED: not "no sign-bearing pairing" but NO PROPERNESS - the
   square is affine over S, nothing truncates the Ext tower; the zeros sit
   behind the global Euler characteristic (Riemann-Roch over S). Local
   case is already a theorem (Hesselholt arXiv:1602.01980, properness
   hypothesis included).
C2 Trace-formula integer structures - SUBSUMED by doc 17 section 4, same
   reason as C1; additionally the Hurwitz class numbers H(n) carry 1/3, 1/2
   Aut-corrections (the groupoid/q->1 leak, third appearance). Integer class
   numbers h(d) are non-multiplicative; their count structures land in the
   mapped set. Signature side only (C4').
```

R-INT STATUS after the verified fleet (2026-06-10): C0, C0', C4, C4',
C5, C5'-diagnostic, C6-first-pass executed; C1, C2 subsumed; C5''-as-TP
superseded. Docs 17-21 are the rung record (20 corrected in place;
worker records in research/work/I,J,K,L; doc 21 = synthesis). THE FRONT
GATE, before any other continuation (doc 21 sec 2):

Q-SCHEME (pre-registered): for each square (HZ^HZ, ku^ku, CC's proper
Spec Z bar) state the computed invariant as (ladder, weight dictionary,
scale, scheme) and check cross-dictionary consistency in common units.
Collapses the three open tensions: T-a KMS-1/2 scheme datum (J), T-b
genus clash, T-c HZ-odd/negative vs ku-even/positive torsion sign.
FIRST GATE EXECUTED (2026-06-10, prime_int_genus_audit.py ALL PASS +
doc 22): T-b is INVARIANT-LEVEL (no unit reconciles; CC chi =
cohomology-with-duality over their base, THH diagonal = cotangent of
the unit map over S - different objects, both correct; "unit error"
excluded). Doc 18's sign is native to the COUNT reading only (operator
reading flips at c = 2pi); genus number 1.459 DEMOTED to calibration
(doc 18 annotated). The wall is now MEASURED: the FF index needs the
two invariants identified on one square, calibration pair
(deg K_CC, deg Omega_THH) = (-2 log 2, +(1/2) log 2pi). G-INT6 control
LIVE: <Delta,Delta>_{O_K} = d zeta'(0) + (1/2)log|d_K| (LM orders,
Z[i] spot-checked) - discriminates, tracks xi_K's |d|^{s/2}; standing
test bench for any "produces zeta" claim. Remaining Q-SCHEME work:
T-c (HZ/ku sign normalization in one indexing) - fold into C6';
workers M (THR fold test) and N (CC square posing) in flight.
Discovery banked meanwhile (fleet/K, verified): Connes-Consani PROVED
integer-valued RR + Pontryagin-Serre duality for compactified Spec Z
(arXiv:2205.01391 Thm 1.1-1.2, 2306.00456 Thm 1.1; circularity-clean) -
the missing object EXISTS AT CURVE LEVEL as a theorem; their 2026
Jacobian paper builds Pic infrastructure. BK/Ngo demoted to monitor
(PD-only; PD is carrier-blind - Epstein passes Poisson). Blumberg-
Mandell spectral Tate-Poitou = only existing duality-over-S theorem
(diagnostic). Standing kill-test to keep in front (doc 21 sec 4): an
S-level duality must be shown to do more than reproduce the functional
equation - "Poisson achieved, still vacuous for RH" has no other guard.

Older per-front records follow (kept for genealogy):

C5 FIRST PASS EXECUTED (prime_int_thh_supply.py + doc 19, 2026-06-09):
   the digamma question answered YES at the affine level - the S^1-weighted
   regularized characteristic function of the diagonal's torsion is
   D(s) = prod_reg(s+k) = sqrt(2pi)/Gamma(s+1), with -d/ds log D = psi(s+1)
   (digamma = the EF's archimedean supply shape; s=0 recovers zeta'(0)).
   Local: log|THH_{2i}(F_p)| = log p = Lambda(p^i) - von Mangoldt IS a THH
   log-cardinality; ladders sum to -zeta_p'/zeta_p and assemble to
   -zeta'/zeta (verified); the deformation kill is CATEGORICAL (closed
   points have residue fields F_p exactly - DH atoms cannot exist). So the
   ENTIRE supply side of the EF = THH count ladders; 3 of doc 10's 4
   realization inputs now have count carriers. Missing fourth = KMS 1/2 =
   a DUALITY datum. Properness decomposed (PF/PD/PR/PS, doc 19 sec 1);
   sharpest wall form: PROPERNESS = POISSON SUMMATION AS A THEOREM ABOUT
   RING SPECTRA (classical face: vdGS theta-RR, math/9802121; char-p face:
   Hesselholt's smooth+proper hypothesis; S-level: OPEN).
C5' DIAGNOSTIC EXECUTED (prime_int_tate_ladder.py + doc 20, 2026-06-10):
   BOTH doc-19 fail-closed criteria MET at ladder level. (i) KMS-1/2
   EMERGES from duality completion: the full Tate ladder gives
   prod_reg_{n in Z}(s + 2pi i n/log p) = 2 sinh((log p)s/2) =
   p^{s/2}(1 - p^{-s}) - the self-dual prefactor is GENERATED by the
   ladder's negative half (THH half-ladder alone lacks it); every
   regularization step exhibited (sinh product 1.5e-13, scaling anomaly
   7.5e-16, assembly 3e-14). (ii) The 1/4-shift: the degenerate
   archimedean ladder prod_reg(n + s/2) = sqrt(2pi)/Gamma(s/2) has
   log-derivative (1/2) psi(1/4 + it/2) ON the critical line (1.3e-6).
   Place dichotomy = orbit geometry: compact orbit (circumference log p)
   -> full ladder -> local factor with p^{s/2}; fixed point (infinity) ->
   degenerate ladder -> Gamma_R. [CORRECTED 2026-06-10, fleet/J + doc 20
   sec 6: realization inputs are 3-FOR-4 plus a scheme-dependent fourth -
   KMS-1/2 = full ladder + SYMMETRIC SCHEME, and no homotopy theorem
   selects the scheme (Hesselholt selects the prefactor-FREE one,
   Deninger 1992 Prop 2.3). Ladder claims stand; the scheme-selection
   principle is OPEN and = the archimedean question (C_2/real structure,
   gate C5''-infty in research/work/J-c5pp-tate-derivation.md sec 5).]
C5'' [SUPERSEDED 2026-06-10]: "via TP of the square" killed by the
   BMS triple; replaced by gate C5''-infty (J-doc sec 5).
   FIRST CHECKPOINT EXECUTED (2026-06-10, worker M + doc 24): the fold
   lives on FIXED POINTS, not Tate - C_2-Tate is contractible at odd p
   (Quigley-Shah) and pi_* THR(F_p)^{C_2} = F_p[y], |y|=4 (DMPR Cor
   5.19) is exactly the half-line/start-0/spacing-doubled archimedean
   ladder; functor dichotomy rotations->Tate->full ladder vs
   reflections->fixed points->folded ladder, with Tate-vanishing at the
   reflection = "no duality completion at infinity", and the
   C_2-involution (-1)^k on pi_2k THH(F_p) = Serre's F_infinity
   eigenvalue selection. PARITY LEMMA (r3): c = 1/2 is the UNIQUE
   negation-equivariant scheme.
   H-r3 SPLIT AND HALF-PROVEN (2026-06-10, worker O + doc 24 as
   amended): H-r3(an) is a THEOREM (negation-naturality forces c = 1/2
   exactly; ALL branch/window schemes have INTEGER slope - no branch
   convention can ever yield 1/2; Deninger's convention = orientation
   choice, C_2-average = symmetric scheme; KMS-1/2 = principal-value
   Euler factor; needs canonical lambda^{1/2} double cover - 2-primary,
   converges with p=2 anomaly + CC's -2{2}). GLOSS CORRECTED: the
   selector is NEGATION (local FE flip), NOT conjugation (Schwarz holds
   for every real-c scheme, selects nothing - any future
   c=1/2-from-conjugation derivation is circular). Doc 24's original
   H-r3 wording was satisfiable-but-VACUOUS (linear Weyl action
   commutes with Theta; witnessed). OPEN RESIDUE = H-r3(hom) = lemma
   L-hom (negation supply at Spec F_q) via fork F1: does the C_2
   inversion-twist on C_p reach the determinant layer? pi_*-level NO
   everywhere computable; positive must come from rho-graded
   parametrized or duality layer (C5''' territory); three ranked
   probes in O-doc sec 4.7 incl. the A6 lambda^{1/2} kill-test for
   candidate carriers. RISK: F1 negative => realization input 4 loses
   its only carrier.
   P=2 COMPUTED (2026-06-10, worker S + doc 25): Theorem S.1 (new):
   THR(F_2)^{tC_2} = prod Sigma^{2n}(HF_2)^{tC_2}, pi_* =
   F_2[[z]][t^{+-1}] (DMPR splitting => Borel formality => Tate SS
   collapse; complete Tate square, integer-exact). The anomaly
   factorizes: (odd-p fold core) x (Gamma_C degeneration - Serre's
   (-1)^n dies mod 2; Legendre duplication mirrored exactly) x (Euler
   tower = Barnes Gamma_2(s|1,2), quadratic anomalous dimension, the
   first RANK-2 archimedean object from homotopy theory - candidate
   for (infty-4)'s s(s-1) pair, unexplored). CONVERGENCE (doc 25 sec
   3): KMS-1/2 APPEARS GEOMETRICALLY at 2 (S-r5: reflection-sector
   duality completion yields 2^{(s+n)/2}(1-2^{-(s+n)}) per weight) +
   O's lambda^{1/2} double cover (2-primary) + CC's K = -2{2}: the
   scheme selector should be sought in the 2-primary sector - run
   F1's probes against the S-doc Tate square first. Refined gate:
   (infty-1') fold theorem-grade at odd p, p = 2 computed; (infty-2)
   1/(2pi) scale open; (infty-3'') L-hom/F1 with 2-primary target;
   (infty-4) candidate = Barnes Gamma_2. Then C5''' = the global
   Poisson step (the zeros). Archimedean compactified object still
   missing.
C6 (Frobenius family): the FF index needs graphs of Frobenius powers;
   HZ has no ring endomorphisms but K-theory has the Adams operations
   psi^k - the only known two-parameter correspondence family. POSING
   CONSTRAINT (doc 18 sec 6): periodic KU is OUT - Stonek proves
   THH(KU) ~ KU v Sigma KU_Q, i.e. inverting Bott rationalizes the
   diagonal's torsion (the q->1 leak again: buy the flow, lose the
   integers). Target the CONNECTIVE square ku ^ ku (psi^k act; THH(ku)
   has finite torsion, Ausoni) with the psi^k graphs as second family.
   C6 FIRST PASS EXECUTED (2026-06-10, fleet/I, verified; record
   research/work/I-c6-ku-square.md + prime_int_ku_ladder.py ALL PASS):
   |T_2w| = lcm(1..w+1)/(w(w+1)) exactly, i.e. log|T_2w| = psi(w) +
   Lambda(w+1) - log w(w+1) - the ku square's torsion carries the
   GLOBAL Chebyshev/EF supply in single cardinalities (the fracture
   square internalizes doc 19's sum over places); free-lattice
   denominators lcm(1..k+2)/2; ALL torsion even-degree (H^2/surface
   slot, pairs POSITIVELY - tension T-c, doc 21 sec 2); Adams shadow
   Z/|k-l| per weight (shadow only). Next: C6' (D_ku constant after the
   scheme fix - s=0 is pole-obstructed), C6'' (minimal twisted
   instance: Lee descent SS with psi^{1+p}), C6''' (signature protocol
   on the family matrices log|k-l|). Verification debt: AHL/Ausoni
   cross-check of T(2)/T(p) tables (partial discharge via 2511.02346).

Pre-registered readings: a candidate passing G-INT1-5 with a verified
comparison identity = the first live S3 object - escalate immediately.
All candidates failing at G-INT2 (fingerprint absent/partial) = map WHERE
the EF fingerprint can and cannot live among count structures - itself a
new constraint (the "count-conservation" question: which spectral data is
reachable by cardinality pairings at all). Failures at G-INT3/4 = standard
graveyard entries.

### R-SQ - The doubled laboratory (RESOLVED 2026-06-09 same day: two-variable conservation, proof/16)

OUTCOME: pre-registered reading (b). E1/E2/E3a/E3a'/E3b all executed; the
natural level-2 pairings trichotomize (free-blind / level-1 Bochner / the
index itself) - the square's analytic shadow contains no new sign. THE WALL,
sharpest form: not the absence of the square but the absence of an
INTEGER-VALUED intersection pairing on any available square; doubling is
cheap, discreteness is the entire cost. Positive residue: phase-free
detection with measured threshold (E3a'), the finite Goldston-Montgomery
instrument (E2), and the trichotomy as a reusable level-2 fork test.
Full record: proof/16. Original spec follows.

Premise (docs 14/15): every no-go so far is ONE-VARIABLE - functionals of single
explicit-formula data fork to single-zero functionals. The missing second factor's
analytic shadow is the PAIR system: shifted convolutions Lambda(n)Lambda(m) on the
arithmetic side, zero-pair correlations gamma - gamma' on the spectral side, with
the free (non-EF-derived) positivity |sum_gamma c(gamma) X^{i gamma}|^2 >= 0 and
the Castelnuovo/Hodge-index inequality as the index's landing spot. Nobody (repo
or literature) has run a POSITIVITY LAB at two variables.

Ordered experiments, fail-closed readings fixed in advance; status updated live:

```text
E1 (doubled closure) - DONE, PASSES (prime_pair_closure.py): A(t) closes
   zero-side vs arithmetic-side to 8e-6..2.6e-4 over t in [0,3]; doubled
   Fejer form closes to 3.0e-5; positivity manifest both ways. (One bug
   caught fail-closed: translated tests reach primes to e^{R+t}.)
E2 (P1 + level-2 image) - DONE, PASSES (prime_pair_fork.py): P1 holds
   STRUCTURALLY at level 1 (the pair functional is quadratic in Lambda; the
   level-1 orbit is linear - no transport exists; first verified P1
   instance). Level-2 conservation VERIFIED: the finite Goldston-Montgomery
   identity 16*PZ = int kB^2 + 2 int kBS + int kS^2 closes to 2.9e-5
   (explicit zero-pair double sum; internal consistency 7.1e-7). The
   conservation law moves up one level instead of breaking. CONSEQUENCE:
   the index must be hunted in INEQUALITIES between pair objects, not in
   their values.
E3a (phase-free detection) - PARTIAL PASS (prime_pair_dh_growth.py): the
   doubled form discriminates zeta from DH from coefficient data alone with
   NO phase engineering and NO interpolation (zeta cells at the stationary
   Fejer baseline, slopes +0.28/+0.32 ~ 1/T0; both DH cells accelerate,
   +0.46/+0.49) - the first structural ADVANTAGE of level 2 over level 1
   (level-1 detection needed the Yoshida device). Localization at a target
   zero NOT confirmed: the DH@30 control was as hot as DH@85.7 - consistent
   with DH's known sigma > 1 zeros at scattered heights (the control-cell
   assumption was wrong, not the mechanism).
E3a' (localization) - DONE, PASSES (prime_pair_localization.py): synthetic
   one-pair calibration. Far-frequency leak exactly 0.000; tuned-frequency
   excess tracks 2 sigma minus a fixed dilution (~0.5 at R=5): threshold
   sigma_min ~ 0.4-0.5 at this support, FALLING with support (cosh^2
   accumulates, dilution fixed). CONSEQUENCE: the doubled form detects any
   sigma > 0 at sufficient support, phase-free and interpolation-free -
   the level-2 structural advantage over the one-variable detection lemma,
   quantified. (S_offline-based redesign unnecessary; synthetic calibration
   cleaner for the instrument question.)
E3b (the Castelnuovo shape) - OPEN, sharpened by E2: since pair VALUES are
   level-2-conserved, the index must be an inequality: cross pair-block
   bounded by diagonal pair-blocks with a discrete defect. Candidate form:
   for the flow-shifted family A_s(t) = A(t+s), test whether the matrix
   C[s,s'] = int k A_s A_{s'} has, for zeta, a constrained signature /
   determinant structure that fails for the off-line objects - and run the
   level-2 fork on the INEQUALITY'S DEFECT, not on the values. READING
   unchanged: live S3 candidate vs two-variable conservation no-go -
   publishable either way.
```

Guards inherited: F1-F3 (doc 14, now at level 2: the comparison map is the
two-variable EF), G5 (over-proving), margin thinness (any index inequality
must be exact + discrete). Infrastructure: fork_lib (extend with pair-Gram),
ladder stack, 5000 cached zeros.

### R-TRACK - The tracking theorem (RESOLVED fail-closed 2026-06-09: terminal equivalence, proof/13)

Final exact form of the program (proof/12 section 5, validated to 2e-5):

```text
Along the support filtration, the arithmetic transgression vector v (Chebyshev
transgressions of the edge-convolution profiles) must track the geometrically
determined point -b/alpha within radius sqrt(bulk/alpha):

    alpha (v + b/alpha)(v + b/alpha)^*  <=  S_0 + sum E_D + b b^*/alpha.
```

OUTCOME (proof/13, witnesses prime_edge_tracking.py + prime_edge_residual_zerosum.py):

```text
(1) DONE - tracking is real: cos(v, -b/alpha) -> +0.9995, relative residual
    1.00 -> 0.033 as alpha grows 70x; tau = alpha r^* BULK^{-1} r < 1 on all
    14 edges (tau < 1 <=> edge positivity, exact). DH control DISCRIMINATING:
    on its only living edge tau = 1.554 > 1, eigmin(SN) = -0.282 - DH fails
    exactly as a tracking failure. The frame is not dispersing.
(2) DONE - fork decided: exact identity C_N^* A^{-1} u = alpha (v + b/alpha),
    so r = (2/alpha) sum_gamma hhat_{A^{-1}u}(gamma) hhat_shell(gamma) - the
    residual IS a zero cross-correlation (verified to truncation: rel err
    7.7e-4..3.7e-3 vs 5000 zeros, cos = +1.00000; closure sanity 8.8e-6).
    -b/alpha is the explicit-formula prediction of v.
(3) CLOSED fail-closed: there is no independent attack surface - any proof of
    tau < 1 must control zero cross-correlations (RH-strength input); with 09
    Finding 1 (slack can never close) and Finding 3 (Huxley ceiling), no
    estimate-based route survives. The rung's product is the TRACKING
    EQUIVALENCE (proof/13 section 3): RH <=> uniform tau < 1 along a one-mode
    scalar recursion - exact, finite-dimensional per edge, terminal.
```

Program-closure status (2026-06-09 evening):
- O3 DISCHARGED in full (00a section 6''): Yoshida's interpolation device
  (primary source read, refs/yoshida1992.pdf) transcribed with the m>=6
  envelope and phase normalization; no concentration => no Case A/B split.
  Second anchor: Li-coordinate route + Lemma B2 (proven, 00a section 6';
  Bombieri 2000 archived refs/bombieri2000.pdf).
- Certification harness DONE: scripts/numerics/witness/certify_chain.py
  (C1-C5 all PASS, exit-code gated; run after any ladder-stack change).
- Remaining for the equivalence write-up: state the tracking equivalence with
  exact hypotheses (doc 11 rank-2 correction replacing the one-mode form);
  O1/O4 line-by-line transcription formalities; the routine sub-lemmas
  itemized in 00a section 6''.

### R-KYP - The realization rung (the post-R1 front)

Target: a prime-side positive structure whose energy identity is the explicit formula.
Concrete first sub-tasks:

```text
1. Transcribe the chronological storage chain (T0/05 identities) into the
   spectral coordinate and determine what functional of the truncated data the
   numerically-working debt Pi_j = (-S_j)_+ corresponds to; look for a closed
   form. (KYP: contractivity <=> existence of Pi; the realization supplies Pi.)
2. Formalize the free-semigroup + KMS_{1/2} frame: the prime side as the
   canonical state on the multiplicative shift semigroup at critical weight;
   ask what positivity the frame gives UNCONDITIONALLY and where it stops.
3. O3/O4 of doc 00 in parallel (paper work, certifies the reduction).
```

SECOND RESULT (2026-06-09, fail-closed, doc 10 section 6): S2 split executed.
The shift(correlation)/corner(autoconvolution) channels are BOTH indefinite
against W_inf alone; only their sum is positive, and edge atoms are pure
corner. No channel decomposition isolates a passive subsystem (guard G6).
The realization must be place-global AND channel-global; its natural home is
the dilated full-line even model (translations unitary, corner = boundary).

FIRST RESULT (2026-06-09, fail-closed): the naive anti-causal closed form
`Pi_j = (-Q_{F_j}[X_j])_+` with `F_j = sum_{k>j} E_k` through the FROZEN response
map X_j FAILS on every tested edge (KYP violation ~ the raw debt itself;
monotonicity also broken). The exact telescoping
`S_N - S_j = sum_{k>=j} (Q_{E_k}[X_k] - R_k^T A_{k+1}^{-1} R_k)` is not
perturbative in the X-drift or the Riccati squares at any tested scale.
Conclusion: the storage is genuinely path-dependent — the realization must be
state-space (track the evolving response map), not a formula in the future
residual. This rules out the last "cheap" version of R-KYP.

### R2 - The certification rung (refutation-grade) - CLOSED 2026-06-10 (confirmation branch)

T1 below. Its epistemic value is asymmetric: the finite model is a compression of the continuum
form, so certified `H <= 0` would refute the local mechanism, while certified `H > 0` only confirms
the numerics. OUTCOME (fleet/L, verified by independent rerun): CERTIFIED `H > 0` by rigorous ball
arithmetic - `prime_defect_t1_interval_certificate.py` (exit-code gated; T=5000, prec=120;
interval Cholesky A_+ > 0 all 21 pivots; Sylvester h11 = [+3.610e-2 +/- 2.2e-5],
det H = [+4.817e-3 +/- 5.4e-6]; certifies down to T=1500; starved T=60 run aborts fail-closed).
Two soundness bugs in older Arb diagnostics found and FIXED (S1: digamma .real inside an acb
integrand broke holomorphy - old W_inf enclosures were not certificate-grade, replaced by
holomorphic symmetrization; S2: float endpoint rounding outside the balls - ENDPOINT_SLOP).
Record: research/work/L-t1-interval.md. Caveats: certificate is relative to the fixed dyadic
basis B taken as exact; single interval library (Arb). Per the pre-registered asymmetry this
confirms the floats and closes doc 08's pending item; it adds nothing to the asymptotic
mechanism (R1's verdict stands). Optional T2 follow-up: same pipeline over refinement bases.

### R3 - Generalization rungs

T2 (refinement stability), T3 (general finite storage - restate as the debt-decay inequality
`(-S_{j+1})_+ <= (-S_j)_+ - repair + square`, since bare existence of Pi_j with
`S_j+Pi_j>=0, Pi decreasing, Pi_N=0` is *equivalent* to `S_N >= 0` via `Pi_j = sum_{k>=j} (-S_k)_+`
and therefore carries no content), T4 (continuum).

## Guiding Risk

The central unproved implication is:

```text
Schur-negative sector
  => old-predictable shell direction
  => bounded terminal-edge leverage / terminal anti-concentration
  => edge-convolution beta surplus
  => exact Euler repair pays debt + Riccati square + leakage.
```

In the default finite model we found a stronger endpoint than this implication: the exact
active-23 post-repair matrix `H=S+G` is already positive definite on the whole two-dimensional
shell. The near-term strategy is therefore:

```text
1. certify the default H>0 matrix endpoint fail-closed;
2. keep the sector/KKT/beta argument as the geometric explanation and generalization path;
3. only then ask whether H>0, or a weakened sectoral version of it, persists in the finite tower.
```

## Theorem Ladder

### T0 - Finite Algebra Foundation

Status: mostly stable.

Goal:

```text
S_{M+E} = S_M + Q_E[X] - R^* A_+^{-1} R
```

with correct signs and block conventions.

Done:

```text
- finite Schur/Riccati identity is isolated in 05-finite-riccati-identity.md;
- smooth-new residual coordinate is fixed:
  M_base = W_inf - P_exact(<L) - P_smooth([L,R]);
- exact residual cells are E_j = P_smooth_cell(j) - P_atom(j).
```

Keep as guardrails:

```text
- do not treat the smooth model as a positivity baseline;
- do not drop the negative Riccati square;
- do not demand local PSD residual increments.
```

### T1 - Default Active-23 Matrix Certificate

Status: CERTIFIED 2026-06-10 - rigorous interval certificate done (see R2 rung above;
witness prime_defect_t1_interval_certificate.py). The remainder of this section is kept
as the historical record of the float-level evidence.

Finite theorem to prove/certify:

```text
For the default finite late edge 3.00->3.24 and repair cell n=23,
every unit shell direction y with y^* S y < 0 satisfies

  y^*(S+G)y > 0.
```

Current stronger endpoint:

```text
H := S+G > 0 on the whole shell.
```

Default numeric certificate:

```text
H = [[+0.0358652162535, -0.0412607325106],
     [-0.0412607325106, +0.1807102584705]]

eig(H) = +0.0249362550056, +0.1916392197184
h11    = +0.0358652162535
det(H) = +0.00477876445197
```

Therefore Sylvester's criterion proves the default sector theorem once these entries are certified
with rigorous error bounds.

Budget identity on the positive-atom part of the Schur-negative sector:

```text
beta_y - required_beta_y
  = y^* H y / (smooth_mass * K_y(w_atom)).
```

Thus beta surplus is an interpretation of `H>0`, not an independent default proof obligation.

Witness:

```text
scripts/numerics/witness/prime_defect_default_t1_certificate.py
scripts/numerics/witness/prime_defect_t1_error_budget.py
scripts/numerics/witness/prime_defect_t1_stability.py
scripts/numerics/witness/prime_defect_t1_arb_components.py
scripts/numerics/witness/prime_defect_t1_winf_tail.py
```

Next work:

```text
- interval-certify A_+>0 and the post-cell Schur complement H>0;
- use Arb compact-overlap integrals for exact Toeplitz atom blocks;
- use compact-overlap integrals for smooth residual cells;
- turn the W_inf finite-cutoff/tail diagnostic into a rigorous Arb/interval enclosure;
- record exact construction dependencies for S, Q, square, smooth_mass, and atom_weight;
- keep KKT enumeration as a cross-check and explanatory geometry, not as the primary T1 endpoint.
```

Do not broaden the target until T1 is certified or fails.

### T2 - Refinement-Stable Active-Sector Theorem

Status: diagnostic only.

Goal:

```text
Extend T1's statement across raised-cosine refinements and any shell dimensions that occur in the
same late edge, either by the same H>0 endpoint or by a sector substitute if H>0 fails.
```

Known evidence:

```text
- repair atom remains 23 across tested bases;
- every sampled Schur-negative direction is directionally repaired;
- the stronger H=S+G endpoint is SPD in all tested refinements;
- positive-atom negative directions have beta surplus at least +0.068;
- K_atom<=0 directions are atom-helpful rather than beta-controlled;
- terminal coefficient is beta-dangerous, interior edge-layer coefficients usually improve beta.
```

Main weakness:

```text
3D refined shells have H SPD numerically, but not yet with rigorous matrix-entry bounds.
```

Next work after T1:

```text
- test whether H>0 is the correct refinement-stable endpoint or just a default coincidence;
- formulate a dimension-independent matrix or sector certificate;
- replace deterministic random sphere sampling with optimization/KKT enumeration in dimension >2;
- test whether the terminal anti-concentration condition has uniform constants.
```

### T3 - General Finite Storage Theorem

Status: speculative.

Goal:

```text
For every finite Sonin extension and exact chronological Euler residual cells,
construct a storage/debt-release certificate:

  S_j + Pi_j >= 0,
  Pi_{j+1} <= Pi_j,
  Pi_N = 0.
```

Known constraints:

```text
- strict telescoping PSD suffixes fail;
- total repair dominating initial debt in Loewner order fails;
- scalar-isotropic storage is too crude;
- path debt Pi_j=(-S_j)_+ survives tested zeta chain but is not constructive.
```

What must replace diagnostics:

```text
- a constructive rule for Pi_j or an equivalent sectoral repair theorem;
- a proof that each dangerous Schur-negative sector has a corresponding exact Euler repair;
- fail-closed tests against DH, smooth-only, prime-only, power-only, sign flips, and shuffles.
```

### T4 - Continuum Sonin Passage

Status: not ready.

Goal:

```text
Pass from finite raised-cosine/Sonin witnesses to the logarithmic Fourier form domain and prove the
nested Prime-Toeplitz domination theorem.
```

Do later:

```text
- density/compactness for pole-killed support spaces;
- convergence of finite Schur complements and residual cells;
- transfer of storage certificates to continuum boundary stresses.
```

Do not prioritize until T1-T3 are mathematically stable.

## Conceptual Framing

Use prediction/innovation language:

```text
Schur complement = conditional innovation energy.
S(y)<0 means the shell direction is strongly predictable from the old space.
Terminal-edge concentration is mostly innovation-like and should weaken old predictability.
Therefore Schur negativity should force terminal anti-concentration.
```

Useful external frameworks to keep in mind:

```text
- Schur complements as conditional covariance / prediction error;
- Toeplitz prediction, Schur algorithm, reflection coefficients;
- Slepian / PSWF concentration operators;
- Christoffel / leverage / boundary concentration estimates.
```

## Current Evidence Snapshot

Default active-23 data:

```text
base Schur min:        -2.545512e-01
H=S+G eigmin:          +2.493626e-02
after cell 23:         +2.494e-02 to +2.665e-02 depending on directional split
Riccati square cost:   +1.550930e-02
Schur leakage cost:    +1.484445e-03
reduced margin:        +2.516061e-02
```

Stability probe:

```text
default L2 grid 6001:  eigmin(H)=+2.493626e-02, det(H)=+4.778764e-03
fine L2 grid 12001:   eigmin(H)=+2.493625e-02, det(H)=+4.778765e-03
invariant drift:      max|deig(H)|=1.6e-08, |ddet(H)|=3.6e-10
```

Post-cell perturbation budget:

```text
direct post-cell composition error = 4.441e-16
eig(A_+) min:          +3.930222e-03
cond(A_+):             9.429e+02
uniform entry eta:     3.867e-09 keeps ||delta H|| below 0.5 eigmin(H)
```

Arb atom component:

```text
ambient max |Fourier-grid atom - Arb atom| = 6.198e-08
compressed atom operator-norm difference   = 1.676e-06
replacing the 23 atom by Arb-overlap atom shifts eigmin(H) by +9.123e-07
selected repair-cell smooth Fourier-grid discrepancy <= 2.771e-09
selected repair-cell smooth Arb radii <= 8.101e-27
selected post-cell suffix smooth Fourier-grid discrepancy <= 1.591e-09
selected post-cell suffix smooth Arb radii <= 3.899e-32
full direct Arb atom+suffix replacement:
  suffix compressed operator-norm difference = 1.035e-07
  post block operator-norm difference        = 2.287e-06
  eigmin(H) shift from atom+suffix           = +9.045e-07
```

W_inf cutoff/tail diagnostic:

```text
selected default W_inf entries differ from T=1500 finite quadrature by up to about 2.1e-06
selected T=1500 finite W_inf integrals have Arb radii <= 1.8e-24
absolute per-entry tail envelope: T=1500 -> 2.150e-09, T=2000 -> 5.269e-10
tail propagation through B:
  T=1500 compressed entry bound <= 5.930e-07
  T=5000 compressed entry bound <= 1.642e-09
full W_inf replacement endpoint:
  T=250  eigmin(H)=+2.487792096097e-02
  T=1500 eigmin(H)=+2.513451932352e-02
  T=1500 shift from default eigmin(H)=+1.983e-04
full Arb finite W_inf endpoint:
  T=5000 eigmin(H)=+2.513438064964e-02
  T=5000 tail envelope=5.953e-12 per ambient entry
partial certificate endpoint:
  T=5000 Arb W_inf finite + Arb atom(23) + Arb smooth suffix
  eigmin(H)=+2.513528421043e-02
  shift from default eigmin(H)=+1.990e-04
all-arithmetic Arb midpoint endpoint:
  T=5000 Arb W_inf finite + Arb old atoms + Arb atom(23) + Arb smooth suffix
  eigmin(H)=+2.511097945288e-02
  shift from default eigmin(H)=+1.747e-04
```

Refinement H=S+G evidence:

```text
n17/h0.100 eigmin(H)=+4.897369e-03
n21/h0.080 eigmin(H)=+4.989831e-03
n25/h0.060 eigmin(H)=+2.493626e-02
n29/h0.050 eigmin(H)=+5.153857e-02
n33/h0.045 eigmin(H)=+2.760913e-02
```

Edge-convolution mechanism:

```text
K(w) = int_0^w q(r)q(w-r)dr,
w = 2a-U.

default beta observed/required: 3.122 / 2.924
weighted K mass left of atom in U: about 0.956
terminal edge profile: nearly quadratic, but terminal asymptotics alone are not the repair.
```

Arithmetic placement:

```text
log23 relative cell position: 0.765
location threshold default:   0.722
weight threshold default:     1.138 times exact weight
```

Autodiff/KKT:

```text
active eigenvector theta=0.157511:
  surplus=+0.209661, dSurplus=-1.051144

interior stationary theta=0.450068:
  S=-0.165205, surplus=+0.108525, dSurplus=0

Schur boundary theta=0.665929:
  surplus=+0.126023
```

## Infrastructure

### Certification

Use only after a finite statement is stable.

Candidates:

```text
- Julia interval arithmetic around the reduced KKT cases;
- Arb/FLINT for certified quadrature/matrix entries;
- Lean for finite algebra after the theorem statement stops moving.
```

### Julia Autodiff

Status: useful for concept discovery, not certification.

Current setup:

```text
scripts/numerics/witness/prime_defect_export_julia_reduced.py
scripts/numerics/julia/active23_ad.jl
scripts/numerics/julia/Project.toml
```

Use interactive workflow for iteration:

```text
julia --project=scripts/numerics/julia
include("scripts/numerics/julia/active23_ad.jl")
```

### Reproducibility Rule

Every numerical claim that affects the theorem target should have:

```text
1. a script under scripts/numerics/witness/ or scripts/numerics/julia/;
2. a short interpretation in research/proof/;
3. a fail-closed note explaining what would invalidate the claim.
```
