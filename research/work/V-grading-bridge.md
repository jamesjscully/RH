# V - The grading bridge: can the strict-square invariant algebra be graded so the Bokstedt tower appears?

Status: executed 2026-06-10 (fresh context, worker V). Inputs: doc 26
(front 3), Q-cc-ftest.md in full, N-cc-square-posing.md (M1 resolution,
F-criteria), prime_cc_strict_smash_q1.py (rerun this session: ALL PASS).
Discipline: no RH / zero-side input; G-INT6 ledger mandatory; carrier
guard (constructions must consume mu); fail-closed. New witnesses
(both ALL PASS, exit-code gated):

    python3 -m scripts.numerics.witness.prime_cc_grading_invariant_kernel
    python3 -m scripts.numerics.witness.prime_cc_grading_bar_degree

HEADLINE: the bridge is REFUTED at the strict-invariant level, by
construction of the very objects it would have needed. (1) The full
strict-square invariant algebra (column/row shape) is computed: it is
the CHARACTER into the free monoid ring Z[(Z \ 0, x)] of the
multiplicative monoid of nonzero integers -- the Euler-product carrier
-- and nothing else; all of Q's Phi_p factor through it. (2) The bar
grading Q called unformable IS formable (subset characters + an exact
face dictionary close the cochain complex), but it refuses the data:
Phi'_2 is NOT a closed cochain (exact counterexample), the genuine
1-cocycle space is ZERO (= pi_1 THH, a match), and the degree-3 slot
where Bokstedt's Z/2 must sit is EMPTY in the character span. The
mismatch is two-sided (degree 0: monoid ring vs Z; degree 3: 0 vs
Z/2): no regrading can fix both ends. Evasion requires either
invariants of a genuinely new shape or the derived replacement itself.

Task (doc 26 sec 4 item 3): Q proved the strict smash HZ ^ HZ carries
divided-power invariants (incl. a Z/2 of square data) that no CC probe
can see, and "degree 3" is not formable in their formalism. Construct,
or refute, a grading on the strict-square invariant algebra under which
the Bokstedt tower (pi_{2k-1} THH(Z) = Z/k; first discriminating datum
Z/2 at degree 3) becomes visible.

## 0. Pre-registered candidates and expected readings (FIXED BEFORE COMPUTING)

Two computable candidates (doc 26's ranked list), plus the obstruction
fallback. All computations bounded: dims <= 3, small entry ranges, no
enumeration stage exceeding ~10^6 instances; bulk logs to /tmp.

### Candidate 1: SIMPLICIAL/BAR DEGREE

The object: the cyclic bar construction N^cy(HZ) in GammaSets_*,
level q = HZ^{^(q+1)}, faces d_i = multiply slots (i, i+1), d_q =
cyclic (multiply slot q into slot 0), degeneracies insert the unit.
Its derived realization is THH(Z) (Bokstedt); the candidate grading is
SIMPLICIAL DEGREE on the strict object. Q's invariants live at level 1
(the square). Plan: extend Phi/divided-power invariants to levels 2-3
(per-slot functionals), machine-verify invariance, then compute the
cosimplicial differential delta(f) = Sum (-1)^i f o d_i on the
invariant cochains and locate cocycles-not-coboundaries by degree.

PRE-REGISTERED EXPECTATIONS (analytic derivations done before any run,
recorded here; the runs confirm or refute):
- V-A1: per-slot characters/divided-power functionals ARE invariant at
  level 2 under all per-slot coend moves (same mechanism as Q's lemma).
  Expected PASS.
- V-A2: faces d_i are well-defined on classes (invariant signatures
  match across moves composed with faces). Expected PASS.
- V-A3 (the discriminating one): Phi'_2 at level 1 is a 1-COCYCLE
  (delta Phi'_2 = 0 on X_2). Hand identity behind the expectation:
  C(xy,2) = x^2 C(y,2) + y C(x,2), which makes the three face terms
  cancel mod 2 on single-cell elements; expectation EXTENDS to all
  elements. Since d_0 = d_1 : X_1 -> X_0 (commutativity of Z), EVERY
  0-cochain has delta = 0, so a nonzero 1-cocycle is automatically not
  a coboundary. READING IF PASS: H^1 of the invariant cochain complex
  contains Z/2, i.e. the simplicial grading places Q's Z/2 at DEGREE 1
  -- the WRONG slot (pi_1 THH(Z) = 0; Bokstedt needs 0,0,Z/2 at
  1,2,3). That is a determinate NEGATIVE for candidate 1 as stated:
  the grading exists but grades the datum to degree 1, not 3.
  READING IF FAIL (delta != 0): candidate 1 stays alive; hunt the Z/2
  at level 3 in the cochain span.
- V-A4: search the span of natural invariant functionals at levels 2-3
  for a Z/2-valued 3-cocycle not a coboundary (within the functional
  subcomplex; scope of any claim = that subcomplex). No analytic
  expectation; exploratory, fail-closed (absence in the span is NOT
  absence in general -- recorded as bounded evidence only).

### Candidate 2: WEIGHT/FILTRATION (the invariant algebra's true shape)

Q exhibited Phi_p, Phi'_p (one Z/p per prime per side) and firewalled
the "Phi_p <-> Bokstedt Z/p at 2p-1" resonance as FIT (zero matched
constraints). Plan: compute the FULL invariant algebra of
column-functional shape F_h = Sum_j h(b_j, A_j) mod m on a bounded
window (h unknown function; every enumerated coend move = one linear
constraint on h; kernel over Z/m for m = 2,3,4,5), and compare its
shape to the Bokstedt tower's.

PRE-REGISTERED EXPECTATION (analytic derivation done first, recorded):
A-moves preserve the multiset {(b_j, A_j)} EXACTLY (column sums exact,
b untouched); B-moves force exactly ADDITIVITY in b (columns merge only
with equal patterns); basepoint forces h(*, 0-object) = 0. Hence the
expected kernel is h(b, A) = b * g(A), g : Z -> Z/m arbitrary with
g(0) = 0 -- i.e. the universal column invariant is the CHARACTER

    chi_col(a,b,S) = Sum_j b_j [A_j]  in  L := Z[Z \ 0] (free ab. gp.),

with e = total = (apply [A] |-> A) and Q's Phi_p = (apply [A] |->
C(A,p) mod p). Symmetrically chi_row. READING IF CONFIRMED: this
CORRECTS the standing picture in two directions at once:
 (i) the invariant algebra is far larger than Q's list -- it contains
     Z/m data for EVERY m (e.g. b * 1_{A=1} mod 4), so the cheap
     exponent-p obstruction to Bokstedt's Z/4 (at degree 7) VANISHES:
     one structural constraint of the firewalled resonance changes
     sign (un-FITs it in the alive direction);
 (ii) the lattice L is FREE: no grading of L alone can "be" the
     torsion tower; torsion can only arise as (co)homology of L-valued
     chains under the bar differentials -- which fuses candidate 2
     into candidate 1 and makes the divided-power comparison sharp:
     Bokstedt's Z/k = coker(gamma_1-multiplication in the divided
     power algebra Gamma_Z[x]: gamma_1 gamma_{k-1} = k gamma_k), and
     C(A,p) ARE divided-power functionals. The computable question
     becomes whether the face maps implement weight-raising with the
     binomial coefficients in the right slots.
- V-B1 (positive control): window kernel contains b*A (= total) and
  b*C(A,2) mod 2 (= Phi_2). Expected PASS.
- V-B2: window kernel mod m equals {b * g(A): g(0) = 0} up to
  window-boundary artifacts (splits leaving the window). Expected
  PASS; window-boundary handling pre-declared: verify containment
  ">=" exactly, and "<=" on the interior sub-window.
- V-B3: K_4 contains an element of additive order 4. Expected PASS
  (b * 1_{A=1} mod 4). If FAIL: the algebra is elementary abelian and
  the Bokstedt shape (Z/4 at degree 7) is UNREACHABLE by any grading
  -- immediate F-FAIL.

### Candidate 3 (fallback): the obstruction

If V-A3 lands PASS (Z/2 at simplicial degree 1) AND no degree-3
placement is found, assemble the obstruction statement: the only
natural grading mixes/misplaces the datum; state exactly what a
bridge would have to add, fail-closed.

### Dictionary fixed in advance (G-INT6)

Simplicial degree q on N^cy <-> THH degree via: homotopy of the
realization; for the linearized strict complex, chain degree = q.
"Visibility of the tower" = the pattern (H_1, H_2, H_3, ...) =
(0, 0, Z/2, ...) in the chosen homological functor of the graded
object, cardinalities exact (R(iii)-strong of N-doc) -- NOT just "some
Z/2 somewhere". Choices spent are tallied in sec 6.

## 1. The invariant algebra computed (candidate 2 first: it recalibrates everything)

Witness prime_cc_grading_invariant_kernel (ALL PASS, exit-gated):

```text
V-B1 PASS  chi_col, chi_row (defined below) EXACTLY invariant on all
           504,896 enumerated coend-move instances (the q1 plans);
           122 distinct linear constraint rows harvested.
V-B2 PASS  window kernel of the constraint system on h(b, A) over F_2
           and F_3: dim 8 = exactly the span {b * 1_{A=A0}}; interior
           excess 0.  The column-functional invariants are the
           characters and NOTHING ELSE (window-scoped upper bound).
V-B3 PASS  h = b * 1_{A=1} annihilates every constraint row over Z
           (invariant mod EVERY m) and takes values 1, 2, 3 mod 4 on
           single cells (1)x(w): a genuine ORDER-4 invariant.
V-B4 PASS  chi_col(x*y) = chi_col(x) *_conv chi_col(y) on 4000 random
           pairs (multiplicative convolution [A][A'] = [AA']);
           separations chi(L) = [1]+[2] != [3] = chi(C3),
           chi(2x2) = 2[2] != [4] = chi(4x1).
```

## 2. Theorem V.1 (the character) and what it corrects

THEOREM V.1. Define, for (a, b, S) representing a class of
(HZ ^ HZ)(1_+), with column sums A_j:

    chi_col(a,b,S) = Sum_j b_j [A_j]   in   Z[Z \ 0]
    (A = 0 buckets and zero coefficients dropped; chi_row symmetric).

(i) chi_col and chi_row descend to (HZ ^ HZ)(1_+).
(ii) Every invariant of column-functional shape Sum_j h(b_j, A_j)
mod m factors through chi_col: h(b, A) = b g(A), g arbitrary with
g(0) = 0 (window-verified upper bound; the containment direction is
exact and unconditional).
(iii) chi_col is MULTIPLICATIVE for the square's smash product
(a (x) a', b (x) b', S x S'): the universal strict column invariant is
a homomorphism into the MONOID RING Z[(Z \ 0, x)] -- by unique
factorization, Z[{+-1} x (free commutative monoid on the primes)].

Hand proof of (i): A-moves preserve the multiset {(b_j, A_j)} EXACTLY
(column sums are preserved exactly -- Q's lemma -- and b is untouched;
merged rows have equal patterns); B-moves merge only equal-pattern
columns, (b', A), (b'', A) -> (b'+b'', A), which the linear-in-b
character respects; inserted/deleted columns carry b = 0 or empty
pattern; the basepoint forms (a = 0 kills all A_j; b = 0 kills all
coefficients; S empty) force exactly the dropping of the A = 0 bucket.
Machine check: V-B1, zero violations on 504,896 instances. (iii) is a
two-line computation: product columns are pairs (j, j') with value
b_j b'_{j'} and column sum A_j A'_{j'}; machine check V-B4.

What this CORRECTS in the standing picture (Q-doc secs 2, 4):

- Q's Phi_p IS chi_col post-composed with [A] |-> C(A, p) mod p (the
  freshman dream makes b^p = b additive); e = total is [A] |-> A.
  All of Q's invariants factor through one free object.
- The invariant content is NOT "one Z/p per prime": the algebra
  carries Z/m data for EVERY m (V-B3, order 4 exhibited). The
  "per-prime pattern" that resonated with Bokstedt was an artifact of
  the probe list, not structure. The cheap exponent obstruction to
  Bokstedt's Z/4 at degree 7 vanishes -- but so does the per-prime
  match itself.
- The universal invariant is FREE (torsion-free): no grading on the
  invariant algebra ALONE can present a torsion tower. Torsion can
  only arise from a differential / imposed relations. F-WEAK's "the
  grading is the entire missing bridge" is therefore false as stated:
  the bridge needs grading + differential, and the only differential
  CC's strict world offers is the bar direction (sec 3).
- THE MONOID appears (doc 26 sec 2's second convergence): the
  universal strict invariant of CC's square is the monoid ring of the
  multiplicative monoid of nonzero integers -- the Euler-product
  carrier, surfacing uninvited at the strict-square level. (The
  structural fact is derivation-grade; its connection to the G-INT3
  monoid thread is an observation, zero weight.)

## 3. The bar degree (candidate 1): cocycle structure at levels 1-3

Witness prime_cc_grading_bar_degree (ALL PASS, exit-gated). The
complex: cyclic bar N^cy(HZ), level q = strict (q+1)-fold smash,
faces multiply adjacent slots (d_q cyclic). Subset characters
chi_T (sec 0) generalize chi_row/chi_col to every level.

```text
V-A1 PASS  chi_T invariant under per-slot coend moves at level 2:
           571,536 instances, 0 violations, all 6 subset characters.
V-A2 PASS  FACE DICTIONARY: chi of a face is a subset character of
           the source (table in sec 0 of the witness); 180,000
           instances, 0 violations.  On level 1, d_0 = d_1 (= total;
           commutativity of Z), so ALL 0-coboundaries vanish.
           => the bar complex GRADES the characters: the cochain
           complex of character functionals is well-defined.  The
           grading Q said was unformable IS formable.  The question
           becomes: where does it put the data?
V-A3 PASS  (PRE-REGISTRATION REFUTED, branch table honored.)  The
           sec-0 expectation "Phi'_2 is a 1-cocycle" is FALSE:
           nonzero-delta counts on 197,586 exhaustively enumerated
           level-2 elements: Phi'_2: 14,016; Phi_2: 95,280;
           Phi'_3: 111,370; Phi_3: 125,017.  Minimal counterexample
           (exact, certificate-grade): vecs = ((-1), (-1,-1), (-1,-1)),
           S = {(0,0,1), (0,1,0)}: delta Phi'_2 = 1.  (The single-cell
           identity C(xy,2) = x^2 C(y,2) + y C(x,2) does NOT extend to
           multi-cell elements.)  => Q'S Z/2 IS NOT A CLOSED COCHAIN:
           under the only differential available it represents no
           class in ANY degree.  Same for the mod-3 data.
V-A3 PASS  The FULL 1-cocycle space of character shape: window kernel
           over F_2 and F_3 is exactly the line g = cB, g' = -cB,
           whose functional is c(total - total) = 0 identically.
           => H^1 of the character subcomplex = 0, MATCHING
           pi_1 THH(Z) = 0.  (e = total itself: delta e = total != 0,
           also not a cocycle -- sanity.)
V-A4 PASS  (exploratory: sampled, span-scoped) H^2 estimate = 0
           (cocycle value-rank 37 = coboundary value-rank 37);
           H^3 estimate = 0 (85 = 85).  Bokstedt wants pi_2 = 0 (match)
           and Z/2 at degree 3 (EMPTY SLOT: no match).
           Simplicial identities d_i d_j = d_{j-1} d_i machine-checked.
```

## 4. Verdict on the bridge: REFUTED at the strict-invariant level (with the exact evasion condition)

Assembling the two candidates' outcomes, the strict bar-graded pattern
of the character-visible homology versus the Bokstedt tower:

```text
degree:        0              1    2    3
strict:        F[Z \ 0]       0    0    0     (monoid ring; H^1 window-
                                               proven, H^2/H^3 sampled)
Bokstedt:      Z              0    0    Z/2
```

- CANDIDATE 1 (bar degree): the grading EXISTS and closes on the
  characters (V-A2: the face dictionary) -- this part of Q's "degree 3
  is not formable" is now REPAIRED: degree is formable. But the
  discriminating Z/2 (Phi'_2) is NOT a cocycle (exact counterexample):
  it carries no degree at all; and the degree-3 slot, where Bokstedt's
  Z/2 must sit, is EMPTY in the character span. VERDICT: candidate 1
  FAILS, determinately for "grade Q's Z/2 to degree 3" (the datum is
  not a class), and at bounded-evidence level for "any Z/2 at degree 3"
  (span + sample scope).
- CANDIDATE 2 (weight/filtration): the invariant algebra is the FREE
  monoid ring (Thm V.1): no regrading of a torsion-free object
  presents a torsion tower without a differential, and the only
  available differential is candidate 1's, already computed. The
  mismatch is two-sided: at degree 0 the strict side is BIGGER
  (monoid ring vs Z -- the strict square remembers every bilinear
  factorization; THH's pi_0 = Z is its e-collapse), at degree 3 it is
  SMALLER (0 vs Z/2). A grading is a reorganization: it can neither
  collapse the degree-0 monoid ring nor create the missing degree-3
  Z/2. VERDICT: candidate 2 FAILS; and Q's firewalled resonance
  "Phi_p <-> Bokstedt Z/p at 2p-1" is now KILLED at the strict level
  (two independent mismatches: non-closedness; order-m data for every
  m, so the per-prime pattern was probe-artifact).
- THE OBSTRUCTION (candidate 3, what is actually proven): any bridge
  must either (a) enlarge the cochain shape beyond the characters --
  but the kernel computation shows column/row-shape invariants are
  EXACTLY the characters, so (a) requires invariants of a genuinely
  new shape (joint/cell-shape: unclassified, sec 7); or (b) change
  the differential -- i.e. derive the smash (cofibrant replacement
  before smashing, Q's T3 joint), WHICH IS THE THH SIDE ITSELF. At
  the strict invariant level the gap is unbridgeable: F-FAIL for the
  strict route, recorded with both witnesses' certificates.

The F-criteria bookkeeping (N-doc sec 4): the registered test still
cannot FIRE (R(i)/(ii)/(iv) unmet -- unchanged); the bypass execution
now returns F-FAIL-at-strict (was F-WEAK): the kept data is not merely
ungraded; it is ungradeable BY the only differential its world
provides, and the slot Bokstedt occupies is empty there. The live
content moves to the positive finding: the strict square's universal
invariant is the Euler-product monoid ring, and the collapse e (the
unique CC-visible map, Q's EM-factorization) is exactly the monoid
ring -> Z evaluation [A] |-> A. What CC's formalism cannot see (Q's
H1) and what the bar grading cannot place (this doc) is precisely the
monoid-ring EXCESS over its evaluation -- the factorization memory.

## 5. Carrier audit

- chi_col/chi_row for H A ^ H B exist for arbitrary abelian groups
  (carrier-blind layer, like Q-C2): the character ALONE carries no
  RH-discriminating content.
- The MONOID RING structure (Thm V.1(iii)) consumes mu twice: the
  square product is mu (x) mu on entries. Epstein lattices have no mu:
  the multiplicative structure is NONEXISTENT for Epstein. DH: no
  carrier at all.
- The cyclic bar complex consumes mu in EVERY face map: candidates 1
  and 3 are nonexistent for both controls. The negative results are
  statements about Z's own square, as required by R(v).

## 6. G-INT6 ledger

```text
claim                          choices spent           constraints matched
Thm V.1 (i),(iii) character    0 (shape = Q's, forced) exact identities on
+ monoid ring                                          504,896 + 4,000
                                                       instances + hand
                                                       proof: DERIVATION
Thm V.1 (ii) completeness      window sizes (calibr.)  kernel dim 8 = span,
(column shape)                                         interior excess 0:
                                                       window-scoped thm
bar grading exists (V-A2)      0 (cyclic bar forced)   dictionary exact on
                                                       180,000: DERIVATION
Phi_p not closed               0                       exact counterexample:
                                                       REFUTATION-grade
H^1 = 0                        window |B| <= 16        negative result,
                                                       window-scoped
H^2 = H^3 = 0                  span (subset chars) +   EXPLORATORY bounded
                               sample sizes            evidence only
Q's mod-p <-> Bokstedt 2p-1    (Q spent >= 2)          now 2 independent
resonance                                              MISMATCHES: KILLED
                                                       at strict level
monoid-ring <-> doc 26 monoid  observation             0: zero weight
thread
```

Fitting-risk note (doc 26 flagged this front highest): the one place a
fit could have been smuggled in -- choosing a grading dictionary until
the tower appears -- is exactly what the pre-registration prevented:
the dictionary (simplicial degree, cardinality-exact visibility) was
fixed in sec 0 before any run, and under it the answer is NO. The
refuted V-A3 expectation is recorded, and the observed branch was one
of the two pre-registered branches.

## 7. Honest limits

- COMPLETENESS SCOPE: invariants are classified only in column/row
  functional shape (Sum_j h(b_j, A_j)). Joint cell-shape functionals
  (Sum_{(i,j) in S} h(a_i, b_j, ...)) and non-functional invariants
  are NOT classified; whether (e, chi_col, chi_row) is complete for
  (HZ ^ HZ)(1_+) remains open (inherits Q's limit). A degree-3 class
  built from an unclassified shape is not excluded -- this is the
  (a)-branch of the evasion condition, stated in sec 4.
- H^1 = 0 is window-scoped (|B| <= 16; constraint rows from the FULL
  bounded X_2 enumeration). H^2/H^3 = 0 are sampled (20,000 elements
  at levels 3-4) and span-scoped (subset characters; the universal
  invariant at levels >= 2 was not classified).
- Degeneracies/normalization: cohomology computed on unnormalized
  cochains (standard equivalence taken on citation; degeneracy
  compatibilities not machine-checked).
- The original V-A3 expectation (cocycle) was wrong; the single-cell
  identity misled the pre-registration. Recorded honestly; the branch
  table in sec 0 covered the observed outcome.
- Over S only; the S[+-1] relative smash not redone (Q's caveat
  stands).
- No statement touches zeros or the explicit formula's spectral side.
  The Bokstedt tower values are standard background (doc 18's
  framework), used only as the comparison target.

## 8. Sources

- research/proof/26-cycle-synthesis.md (task framing, front 3).
- research/work/Q-cc-ftest.md (Phi_p/Phi'_p, EM-factorization, F-WEAK).
- research/work/N-cc-square-posing.md (M1 resolution, R(iii), F-criteria).
- scripts/numerics/witness/prime_cc_strict_smash_q1.py (machinery reused).
- Witnesses (this doc): prime_cc_grading_invariant_kernel.py,
  prime_cc_grading_bar_degree.py.
