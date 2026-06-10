# Z - The U.2 glued object at p = 2 (PFD step 1): construction of G = D cup_Lin D', kill tests K2 and K1

Status: fresh-context worker Z, 2026-06-10. PFD spec doc 28, step 1.
Required reading executed in order: doc 28 (K1-K6, F-a/b/c), docs 24/25
(as amended), S-thr-p2.md IN FULL, U-f1-probes.md IN FULL, O-doc Thm A1
+ Prop A6 sections. Both inherited witnesses rerun by me before any new
work: prime_int_thr_p2_anomaly.py ALL PASS, prime_int_u_f1_probes.py
ALL PASS (exit 0 both).

Witness (NEW): scripts/numerics/witness/prime_int_z_u2_glue.py
(gates ZG1-ZG8, pre-registered fail-closed readings in the docstring,
exit-code gated, exact F_2/rational arithmetic except the one numeric
scheme gate at 1e-12).

Sections 1-2 (registrations + construction) were written BEFORE the
witness was first run; the verdict sections below them after.

## 1. PRE-REGISTERED READINGS (before running)

```text
Z-r1 (construction): G is constructible with K6-legal data only. The
     divided-power dual D' is FORCED (not chosen): the continuous dual
     of F_2[[z]] is the Matlis dual / colimit of U's truncation tower,
     and its weight-graded algebra structure is the divided-power
     algebra Gamma_{F_2}[z'] with zero free choices given S's weight
     grading. FAIL: any step needs a datum beyond the residue pairing
     (+ product-formula shadow); log it and stop.
Z-r2 (K2): PASS expected, in the precise form: U's level-N residue
     pairings are the restrictions of ONE evaluation pairing on G along
     the canonical tower maps (c_N, iota_N), compatibly at every level,
     perfect on every truncation, weight flip m <-> N-m becoming the
     STABLE flip m <-> -m (the runaway center N/2 = the gluing locus).
     FAIL: any non-permutation Gram matrix, tower square that does not
     commute, or N-dependence of a fixed-pair value.
Z-r3 (forced scheme, conditional on Z-r2): with negation now a
     STRUCTURE MAP of G (the duality covers (j, m) -> (1-j, -m)), O's
     Thm A1 applies and forces c = 1/2 on the glued ladder; witnessed
     as: negation ratio constant in (w, weight) iff c = 1/2; A1 slope
     solve gives exactly 1/2. CAVEAT registered in advance: the unit
     u = -1 is F_2-invisible; the dictionary step (G's duality =
     ladder negation N on (V, Theta)) is spent from docs 19/20/U, not
     re-derived. F-c is answered only modulo that identification.
Z-r4 (K1): expected NOT DECIDABLE AT ONE PLACE, with mechanism: the
     glued object is exactly SCALE-FREE (anomalous dimension of every
     glued two-sided ladder = 0, exact rational identity; regularized
     glued trace = 0 away from 2^{-s} = 1), so no scale - in
     particular no 1/(2 pi) - can emerge at p = 2 alone; nonzero
     anomalous dimensions live only in the unglued degenerate sector
     ((1-s)/2 fold, Barnes quadratic). A clean not-decidable is
     full-value per doc 28 step 1. FAIL of the reading: some glued
     anomaly is nonzero (then a scale candidate exists and must be
     confronted with K6).
Z-r5 (shear): U's Weyl shear phi extends to G K6-legally (by
     pairing-adjointness), remains UNIPOTENT, acquires NO negation /
     branch-swap component, is an isometry of the residue pairing, is
     the identity on the Lin line. The extension requires a connecting
     map kappa: Gamma -> D through the Lin line whose existence is a
     nontrivial exact linear problem: EXPECTED solvable; if not, the
     exact obstruction (order, slot) is the deliverable. Registered
     sub-finding to test: phi is [-1] of the MULTIPLICATIVE formal
     group on the weight disk (1 + phi(z) = (1+z)^{-1} exactly), and
     the phi-invariant 1-form is dlog(1+z) = du/u; over C, [-1]* on
     du/u has constant unit -1 = A1's forced unit. FAIL: identities
     fail in truncation.
Z-r6 (N1/N2): N2 becomes FORCED on G (the duality pairs degree j with
     1-j, an ODD shift, hence vanishes identically on the even
     sublattice F_2[t^{+-2}] = the v-lattice: the duality exists only
     on the index-2 refined t-lattice, spacing pi i/log 2). N1 (t vs
     Hesselholt's v as two shadows of one rho-graded class) does NOT
     become available: it is spectrum-level, G is a pi_*-level object.
```

Evaluation rules fixed in advance: all F_2 algebra exact and truncated
(weights <= 12, degrees |a| <= 6 unless stated); truncation artifacts
handled as in U (fail-closed; any gate amendment recorded verbatim);
the doc-19/20 dictionary and the Lerch/Hurwitz pipeline are reused
unchanged (zeta_H(0,a) = 1/2 - a; Barnes zeta_2(0,s|1,2) =
s^2/4 - 3s/4 + 11/24, both already witnessed by S). No RH/zero-side
input anywhere.

## 2. THE CONSTRUCTION (with the G-INT6 ledger inline)

### 2.1 The divided-power dual D', made precise

D := pi_* THR(F_2)^{tC_2} = F_2[[z]][t^{+-1}] (Theorem S.1; |t| = -1,
|z| = 0, wt z = 1, pi_j D = t^{-j} F_2[[z]]).

D' := the degreewise CONTINUOUS dual of D: per degree j and weight
m >= 0, the functional gamma_m dual to z^m,

    D'_j = Hom_cont(pi_{1-j} D, F_2) = (+)_{m>=0} F_2 . t^{-j} gamma_m,

with wt(gamma_m) = -m (restricted/Matlis dual: direct SUM, the
continuous dual of a product). Three structures, each with its ledger
entry:

- [L1, forced] MODULE: D' = E(F_2), the injective hull / Matlis dual
  of F_2[[z]], with z acting by contraction z.gamma_m = gamma_{m-1}.
  Equivalently D' = colim( D/z^{N+1} --(x z)--> D/z^{N+2} ) with
  colimit insertions iota_N(t^a z^m) = t^a gamma_{N-m}. This is
  exactly the colimit of U's truncation tower along its transition
  maps - it is the object U's finite levels already assemble to. Zero
  choices (Matlis duality is theorem-grade commutative algebra).
- [L2, forced given S's grading] ALGEBRA: the weight-graded dual Hopf
  algebra of F_2[z]. Weight-gradedness forces the coproduct
  Delta(z) = z(x)1 + 1(x)z (the only weight-1 monomials in the tensor
  square), i.e. the additive one; the graded dual is then the
  divided-power algebra

      Gamma_{F_2}[z'] :  gamma_i gamma_j = binom(i+j, i) gamma_{i+j}
      = F_2[gamma_1, gamma_2, gamma_4, gamma_8, ...]/(gamma_{2^k}^2)

  (Lucas; gamma_m = prod gamma_{2^k}^{m_k} over binary digits m_k).
  This makes U.2's phrase "divided-power dual" precise AND shows it is
  not a choice: over F_2 the continuous dual is genuinely NOT a
  Laurent-tail ring (gamma_1^2 = 0), so no F_2((z))-type function-field
  gluing is even available - see the F-a audit, sec 6.
- [L3] The t-periodicity acts on D' invertibly (degree shift), as on D.

### 2.2 The Lin-line identification and the glued object

The Lin line is Lin = F_2[t^{+-1}]: in D the weight-0 subring; in D'
the socle F_2[t^{+-1}].gamma_0, gamma_0 = the augmentation functional
(evaluation at z = 0) - canonical on both sides [L4, forced].

    G := D cup_Lin D'  :  per degree j,
    G_j = t^{-j} F_2[[z]]  (+)  (+)_{m>=1} F_2 . t^{-j} gamma_m
          (weights >= 0)        (weights <= -1)

- weight 0 counted ONCE (gamma_0 = 1 = z^0). Weight spectrum of G_j:
all of Z, each weight one-dimensional per degree.

THE RESIDUE PAIRING (the K6-legal gluing datum; [L5, forced by U's
tower - see ZG2]): <., .>: G_j x G_{1-j} -> F_2,

    <t^{-j} z^m,  t^{j-1} gamma_{m'}> = delta_{m,m'}   (m, m' >= 1)
    <t^{-j} z^0,  t^{j-1} z^0>        = 1              (Lin block)
    all other weight combinations     = 0              (forced:
    the pairing is weight-0-homogeneous, which is itself forced by
    compatibility with U's tower, where level N pairs m + m' = N).

Degree bookkeeping: the pairing lands in the t^{-1}-slot (degree sum
1), the same Sigma-shift as U's finite levels and the Lin-line Tate
duality D_{F_2}((HF_2)^{tC_2}) ~= Sigma (HF_2)^{tC_2} (Greenlees-May),
of which the Lin block is exactly the pi_* shadow.

### 2.3 What G honestly is, and what it lacks

HAS: (i) a degree-graded, weight-graded F_2[t^{+-1}]-module with
1-dimensional (j, m)-slots for ALL (j, m) in Z x Z - the full
two-dimensional glued ladder; (ii) a commutative ring structure: the
fiber product D x_Lin D' (nodal gluing - products of strictly-positive
with strictly-negative weight vanish; D'-branch carries the
divided-power multiplication [L2]); (iii) the perfect residue pairing
of 2.2, making G_j topologically self-dual against G_{1-j}
(profinite x discrete, Pontryagin-style over F_2); (iv) t-periodicity.

LACKS, stated plainly: (a) a spectrum-level realization (G is the
pi_*-level shape of U.2's conjectured T^t; constructing T is C5'''s
burden, untouched here); (b) a single multiplication realizing the
pairing as residue-of-product (that would need a Laurent-type ring,
which the F_2 divided powers refuse - this lack is a FEATURE for F-a,
sec 6); (c) the rho-graded refinement (N1, sec 5); (d) cross-branch
products (nodal point).

[L6] The product-formula shadow: NOT SPENT in the construction. The
residue pairing alone suffices. It is reserved for the global assembly
(doc 28 step 2), exactly where K1 lands (sec 4).

## 3. K2 RUN: VERDICT PASS, as registered [ZG2, ZG3]

Witness ALL PASS (ZG1-ZG8, exit 0). The two pillars:

(i) TOWER (ZG2): U's level-N residue pairing <a, b>_N = (coeff of
t^{-1} z^N in ab) is EXACTLY the G-pairing composed with the colimit
insertion: <a, b>_N = <a, iota_N(b)>_G for iota_N(t^a z^m) =
t^a gamma_{N-m}, for all N <= 10, all degrees tested, exhaustively;
iota_{N+1} o (x z) = iota_N (the tower commutes). The divergence U
found is therefore an ARTIFACT OF READING BOTH FACTORS IN D: the
level-N pairings were always the shadows of ONE pairing on G whose
second slot lives in D'. On G, fixed pairs have N-independent values
(witnessed) where U's fixed D-pairs decay to 0 (re-witnessed,
side by side). The runaway center N/2 of the weight flip m <-> N-m is
the gluing locus: on G the flip is the STABLE m <-> -m.

(ii) PERFECTNESS (ZG3): on every truncation (M <= 8) and every degree,
the Gram matrix is a permutation implementing (j, m) <-> (1-j, -m):
weight flip m <-> -m, degree flip j <-> 1-j (the Sigma-shift), Lin
block = the pi_* shadow of Greenlees-May Lin-line Tate duality.

So: COMPACTIFICATION RESTORES NEGATION exactly where completion broke
it. Under the doc-19/20 dictionary (degree <-> vertical lattice,
weight n <-> 2^{-ns} supply - already spent, no new choices) the
duality covers s -> -s, as a DUALITY not an automorphism (O 4.6's
demand): the branch swap D <-> D' is weight inversion, the t-slot
shift is degree inversion.

### 3.1 The forced scheme (O Thm A1 applies): c = 1/2 [ZG4]

On G, negation is a STRUCTURE MAP (the duality), not an external
demand. So scheme equivariance is forced, and O's Theorem A1 (proved,
analytic half) yields: the unique negation-natural zeta-class scheme
on the glued ladder is

    f(w) = e^a 2^{w/2} (1 - 2^{-w}) = e^a 2 sinh(w log 2 / 2),

c = 1/2 exactly, unit u = -1, per weight pair +-n. Witnessed: the
negation ratio is constant (= -1, dev 8.5e-16) across the w-grid AND
across glued weights {0, +-1, +-3} only at c = 1/2; every other c in
the scan has deviation >= 3.14; the A1 slope solve gives alpha = 1/2
exactly. THE GLUED LADDER at p = 2: the full lattice (degree, weight)
in Z x Z, vertical spacing pi i/log 2 (the t-lattice, sec 5.2),
per-weight determinant the self-dual Euler factor - S-r5's form, now
SCHEME-FORCED rather than scheme-applied: doc 25's G5 weakening is
discharged at the p = 2 instance.

Registered caveats, maintained: (a) the unit -1 is F_2-invisible; its
carrier-level shadow is exhibited structurally instead: the
Weyl-invariant 1-form on the weight disk is dlog(1+z) = du/u, and
[-1]^*(du/u) = -du/u over a char-0 base - the constant unit -1 is the
classical transformation of the Haar form under inversion (sec 5.1).
(b) The identification "G's duality = ladder negation N on (V, Theta)"
spends the doc-19/20 dictionary; what is NEW and exact is that a
perfect duality covering (j, m) -> (1-j, -m) EXISTS on the
compactified carrier. The scheme question at p = 2 closes modulo that
dictionary, i.e. F-c is answered: forced, not applied (sec 6).

## 4. K1 RUN: NOT DECIDABLE AT ONE PLACE - with the mechanism computed
## [ZG5]

As the spec's honest expected outcome anticipated, sharpened to a
theorem-shaped reason:

(i) THE GLUED OBJECT IS EXACTLY SCALE-FREE. The anomalous dimension of
every glued two-sided ladder vanishes identically: zeta_H(0, a) +
zeta_H(0, 1-a) = 0 as an exact rational polynomial (witnessed), in
both the vertical (t) and horizontal (weight) directions. The c = 1/2
form is the scale-free member of the family (S's W5 kappa-independence
is its numeric shadow). A determinant layer with zero anomalous
dimension SINGLES OUT NO SCALE - there is nothing on which a 1/(2 pi)
could attach at p = 2 alone, and any pi-valued constant in the F_2 /
Q.log2 universe of G would be an insertion (K6 violation).

(ii) THE GLUED TRACE VANISHES: 1/(1-x) + 1/(1-1/x) - 1 = 0 exactly
(x = 2^{-s}; D-trace + D'-trace - shared Lin line, inclusion-exclusion
over the gluing; 25 rational points, exact). The regularized trace of
G is identically 0 away from 2^{-s} = 1: the glued object's trace
layer is a pure lattice-delta supported on the vertical lattice - the
one-place shadow of Poisson. This is the LOCAL FACE on which the
global product formula will act (the MIN/MAX pairing of the W-doc):
the scale datum is a relation BETWEEN places.

(iii) Where the scale actually lives: the nonzero anomalous dimensions
in the p = 2 picture are exactly the UNGLUED degenerate-sector data -
the fold (1-s)/2, the Gamma_C line 1/2 - s, the Barnes quadratic
s^2/4 - 3s/4 + 11/24 (all exact, witnessed nonzero). The 1/(2 pi) /
-(1/2) log pi datum (doc 20 C2) must arise when THESE meet the
scale-free glued objects in the global assembly - doc 28 step 2's
burden, now with a precise attachment point.

## 5. THE SHEAR AUDIT AND N1/N2 [ZG6, ZG7, ZG8]

### 5.1 The shear extends to G, stays unipotent - and is a formal-group
### inversion

NEW FINDING (exact, ZG6): U's Weyl shear phi(z) = z/(1+z) is [-1] OF
THE MULTIPLICATIVE FORMAL GROUP on the weight disk: F(z, phi z) = 0
for F(x,y) = x + y + xy, equivalently 1 + phi(z) = (1+z)^{-1} - in the
group-like coordinate u = 1 + z the shear is EXACTLY u -> u^{-1}. The
additive law's [-1] is the identity (char 2), so the Weyl action
SELECTS the multiplicative structure (uniqueness across all FGLs not
claimed). The phi-invariant 1-form is dlog(1+z) = du/u (witnessed
exact; dz itself is not invariant) - the Haar form of G_m-hat, whose
char-0 transformation under inversion is the constant unit -1 = A1's
forced unit. Reading (flagged): in the u-coordinate the shear is a
HORIZONTAL (weight-direction) inversion fixing the residue disk - the
unipotent shape U saw is the multiplicative inversion read in the
additive coordinate.

EXTENSION TO G (ZG7): phi_G = (phi on D) + (adjoint A on the
D'-branch) + a connecting map kappa: D' -> D through the Lin line,
with kappa_0 forced = binom(1+a', b') and the involutivity/isometry
constraints an exact F_2 linear system. WITNESSED: solvable at every
tested degree pair (nullity 43 each: existence YES, uniqueness NO -
ledger), and the solved phi_G is an involutive ISOMETRY of the residue
pairing, identity on the Lin line, with NO branch swap (D never
acquires a D'-component). VERDICT: the gluing does NOT give the shear
a negation component - negation is carried by the duality (branch
swap), the residual Weyl stays unipotent, and the two commute in the
isometry sense. The division of labor is clean: duality = negation,
Weyl = inversion of the formal group in the weight disk.

### 5.2 N1/N2 on G

N2 (Theta normalization): FORCED ON G (ZG8). The duality pairs degree
j with 1 - j - an ODD shift - so it vanishes identically on the even
sublattice F_2[t^{+-2}] (the v-lattice): no self-duality exists over
the TP periodicity lattice; the duality REQUIRES the index-2 refined
t-lattice. The determinant layer of G must read its character lattice
from t: spacing pi i/log 2, q^{w/2} integral. The doc-25
degree-vs-weight convention question is answered BY the object, not by
convention - Q-SCHEME bookkeeping can cite this.

N1 (t vs Hesselholt's v as two shadows of one rho-graded class): NOT
available on G and cannot be - it is a spectrum-level comparison and G
is a pi_*-level object. Owed exactly as U stated it; the natural
vehicle remains TR(F_2) with the Witt anti-involution / QS21 Prop 6.14.

## 6. FAILURE-MODE AUDIT

F-a (circularity): NOT TRIGGERED, with a structural guard found: over
F_2 the continuous dual of the disk is divided-power, NOT Laurent
(gamma_1^2 = 0): the compactification is NOT the function field
F_2((z)) and CANNOT import a meromorphic continuation - there is no
ring of functions extending D across the gluing locus (cross-branch
products vanish at the node). Analytic inputs spent: geometric series
of one rational function (elementary), Matlis duality, Hurwitz
zeta(0, a) = 1/2 - a (pipeline already spent). No zeta-side input.

F-c (applied vs forced): the point of K2. On G the negation is a
structure map; A1 then forces c = 1/2 (sec 3.1). Resolved at the
p = 2 instance modulo the dictionary caveat, stated in 3.1(b).

F-b (vacuity/carrier-blindness): not this step's burden (K5 needs the
odd-p and O_K instances; doc 28 step 2), but noted: the construction
used S's computed square at every step - no ring, no D, no D', no G.

## 7. G-INT6 LEDGER (complete)

- L1 D' as module = Matlis dual = colimit of U's tower: FORCED.
- L2 D' algebra = divided powers: FORCED given S's weight grading
  (graded coproduct on z has no other option). The multiplicative
  coproduct (whose [-1] is the shear) lives one level up, on the
  FILTERED object; recorded as structure found, not chosen.
- L3 t-periodicity: inherited, no choice.
- L4 Lin identification gamma_0 = 1: the augmentation; canonical.
- L5 pairing: weight-0 blocks and values forced by U's tower (ZG2);
  zero choices.
- L6 product formula: NOT SPENT; reserved for step 2. K6 SATISFIED:
  gluing data = residue pairing only.
- Non-unique datum, disclosed: the connecting map kappa of the shear
  extension (nullity 43 per degree pair at this truncation). The
  EXISTENCE verdict and all other gates are kappa-independent. A
  canonical kappa (e.g. minimal/invariant-form-normalized) is an open
  bookkeeping item, not load-bearing.
- Witness-engineering record (registration discipline): gate logic
  never amended; two harness bugs in the F_2 Gaussian elimination
  (back-substitution order; missing RREF reduction) caused two ZG7
  FAILs before the fix - found by direct row-satisfaction check,
  fixed in the solver only, all gate predicates untouched.

## 8. HONEST LIMITS

- G is a pi_*-level object. U.2's clauses (a), (c), (d) are now
  CONSTRUCTED/witnessed at pi_*-level; clause (b) ("the self-duality
  is INDUCED by the O(2)/real structure") is established only for the
  Lin block (Greenlees-May is genuinely equivariant); for the weight
  branches the duality is supplied by Matlis theory and shown
  CONSISTENT with the Weyl action (isometry), not derived from O(2).
  The spectrum-level T (C5''') remains the conjecture's burden; U.2
  is hereby demoted from "interface conjecture" to "realization
  conjecture for an existing pi_*-level object".
- The scheme forcing spends the doc-19/20 dictionary and O's A1; the
  unit -1 is exhibited structurally (du/u under inversion), not over
  F_2.
- ZG7's linear algebra is solved within truncation (wt < 12,
  gamma <= 5, four degree pairs); a closed-form kappa
  (e.g. binom(1+a', b') t^{a'} (1+z)^{-a'/2}-type for even a',
  hand-verified for a' = 2) is not pinned in general.
- K1's "not decidable" is an exact statement about THIS object's
  anomaly content, not a proof that no other p = 2 structure carries
  a scale.
- Everything rides on Theorem S.1 (lead-rerun, not independently
  re-derived) and U's shear derivation (derived-structural grade,
  inherited caveats).
- No RH/zero-side input anywhere; all carriers are finite-place
  shadows.

## 9. HAND-OFF (for the lead)

```text
CONSTRUCTION:  G = D cup_Lin D' built, K6-clean (ledger sec 7);
               D' = divided powers, FORCED not chosen.
K2:            PASS - U's pairings = one perfect pairing on G,
               compatibly at every level; negation restored as a
               duality; weight flip stabilizes at m <-> -m.
SCHEME:        c = 1/2 FORCED on the glued ladder (A1 applies since
               negation is now internal); doc 25 G5 "applied not
               forced" discharged at p = 2; F_2-invisible unit -1
               carried by [-1]^* du/u = -du/u.
K1:            NOT DECIDABLE AT ONE PLACE (full-value per spec):
               glued object exactly scale-free (anomaly = 0, trace =
               lattice delta); scale carriers are the unglued
               degenerate sectors; attachment point for step 2 named.
SHEAR:         extends to G as involutive isometry, unipotent, no
               negation component; NEW: shear = [-1] of G_m-hat,
               invariant form dlog(1+z), unit -1 shadow.
N2:            FORCED on G (duality dies on the v-lattice, needs t);
               spacing pi i/log 2.  N1: still owed, spectrum-level.
NEXT (step 2): odd-p instances + global assembly; the product formula
               (unspent) acts on the glued trace-deltas; the scale
               must emerge from degenerate-sector x glued-sector
               interaction across places.
```
