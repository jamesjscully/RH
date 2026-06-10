# FF - The kappa-gate on the realized object Xbar (doc 30 front 2) + the s(s-1) bookkeeping (front 4)

Status: fresh-context worker FF, 2026-06-10. Required reading executed
in order: doc 30, BB-global-assembly.md IN FULL, DD-spectrum-
realization.md, CC-gluing-consolidation.md (parts 2-3), doc 21 sec 2
(Q-SCHEME) + doc 22. Inherited witnesses rerun by me before any new
work: prime_int_bb_global_assembly.py ALL PASS (exit 0),
prime_int_gc_k3_barnes_rank.py ALL PASS (exit 0).

Witness (NEW, pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_int_ff_kappa_xbar
    (FFG1-FFG8; ALL PASS, exit 0)

DISCIPLINE RECORD: registrations were written in the witness docstring
before the first run; the FFG3 odd/even pattern and the FFG6-FFG8
closed forms are DISCLOSED design-stage derivations/explorations (CC
precedent), checked fail-closed by the witness. One run-1 failure: a
flint TYPE error in an FFG8 anchor (acb-vs-float coercion), fixed; no
gate predicate or registered reading was amended at any point.

SINGLE ASSUMPTION (G-INT6, Part 1): Conjecture DD.4 (continuous BC
self-duality I^cont(Xbar) ~ Sigma Xbar). Everything in Part 1 is
conditional on it and so flagged; the verdict is what DD.4 would and
would not BUY. F-a guard: kappa = pi is used as COMPARISON ONLY (it
appears only in sec 4's target discussion, never in a derivation).

## 1. PART 1 VERDICT: F1-FAIL - I^cont IS NOT THE POISSON EXCHANGE

Doc 30 continuation 2 asked: is DD.4's I^cont the archimedean Poisson
exchange BB's no-go named? ANSWER (conditional on DD.4, structural):
NO. The Matlis/BC exchange is the TORSION SHADOW of the Pontryagin/
Poisson exchange, and the shadow forgets exactly the datum that
carries the scale. Doc 30's "triple duty" of DD.4 drops to DOUBLE
duty: it restores negation and cancels the pole, but it cannot carry
kappa.

### 1.1 The Matlis/Poisson dictionary, made precise (FFG1)

The classical archimedean exchange at the finite place p is Pontryagin
duality of the pair (lattice, torus): 0 -> L -> R -> R/L -> 0 with
L = (log p)Z dualizes to 0 -> L-perp -> R -> T -> 0 with L-perp =
(2pi/log p)Z; Poisson summation is the comb <-> comb identity this
self-duality of R induces, and the 2pi is the period datum of the
pairing e^{ixt} on the CONNECTED group R.

The algebraic exchange is the same diagram with the connected groups
deleted. Witnessed exactly (FFG1): on the 2-primary pair
(Z/2^N quotient tower, x2-colimit in Q_2/Z_2),

    p_N^* o s_N = s_{N+1} o (x 2)      (s_N: a -> ab/2^N, perfect),

which is verbatim DD's DDG1 conjugation (dual of the quotient tower =
the multiplication tower), and the colimit Z[1/2]/Z is PURE TORSION:
the connected part R/Q of the torus is never produced. Dictionary:

    F_2[[z]] tower  <->  Z_2 = lim Z/2^N        (profinite "lattice")
    divided powers  <->  Q_2/Z_2 = colim Z/2^N  (TORSION of the torus)
    residue pairing <->  a b / 2^N in Q/Z       (DDG1 = its shadow)
    -- no slot --   <->  R, R/Z connected       (carries e^{ixt}, 2pi)

So the task's candidate reading ("comb <-> continuum = torsion <->
divisible of Matlis duality") is adjudicated: ALMOST - Matlis/BC is
the torsion <-> torsion-of-the-torus exchange. The divisible
CONNECTED part, the actual continuum, is not exchanged but DELETED.

### 1.2 Where the scale lives, and why the shadow cannot see it (FFG2, FFG4)

- The classical exchange is scale-rigid because the torus is rigid:
  continuous Aut(R/Z) = {+-1} (theorem, cited). Its torsion shadow is
  floppy: |Aut(Z/2^N)| = 2^{N-1}, growing (witnessed); on the F_2 side
  the level-N self-duality normalizations (Frobenius forms
  <a,b> = L(ab), L(z^N) = 1) are EXACTLY a 2^N-torsor (witnessed,
  all perfect). The 2pi-rigidity is a TOPOLOGICAL datum of the
  connected dualizing torus, with no torsion shadow.
- The continuum is BC-annihilated (FFG4, exact): the image of x2^K on
  Z/2^N is 0 for K >= N, so Hom(2-divisible, Z/2^N) = 0: Z[1/2], Q, R
  - a fortiori the degenerate sector's continuum density - have NO
  nonzero map into the dualizing object's homotopy. I^cont can dualize
  the combs (FFG1 = DD.2); it maps the continuum to ZERO. The exchange
  is structurally one-sided: it cannot couple the comb to the
  degenerate sector because its dualizing object is totally
  disconnected.

### 1.3 The gate (FFG5) and Proposition FF.1

Registered F1 readings: F1-pass = kappa determined (record + Q-SCHEME
bookkeep BEFORE comparing to pi); F1-fail = still equivariant, name
the residual freedom. MEASURED: F1-FAIL, as registered.

- Transported through BB's Abel-regularized traces under the analytic
  coordinate rescale t -> ct (the torsor's analytic shadow; c in
  {1, e, pi}, p in {2, 3, 5}): comb atom weight / spacing = 1
  invariant (worst dev 7.95e-08) while the absolute weight scales by
  c. The exchange determines the RATIO only - the normalization the
  task asked for does NOT emerge.
- PROPOSITION FF.1 (conditional extension of Prop BB.1 to spectrum
  level): in every candidate home DD.4 names (filtered Mod_Y, pro-ind/
  Tate objects, solid F_2-modules), all mapping data are built from
  finite F_2-modules by limits/colimits; kappa enters the construction
  of the category nowhere, so the rescaling R_lambda fixes the
  enriched input set {banked inputs} u {I^cont equivalence data}
  pointwise while the gate observable -(1/2) log kappa moves
  (witnessed: -(1/2) log lambda != 0). No function of the enriched
  inputs determines kappa. F1-FAIL, structural.
- RESIDUAL FREEDOM, NAMED: the 1-unit normalization torsor of the
  duality - and it survives even the shear constraint. NEW exact
  finding (FFG3): the Weyl-shear(phi(z) = z/(1+z))-isometric Frobenius
  forms number 0 at even truncation level and exactly 2^{(N+1)/2} at
  odd level (N <= 12) - NEVER unique. The parity matches the forced
  odd Sigma-shift (the duality lives at odd pairing-degree-sum);
  imposing phi-equivariance halves the torsor's exponent but never
  pins it. This is DD's g3 = Z's kappa nullity, seen a third way; the
  analytic shadow of the same freedom is the coordinate scale c.

### 1.4 What this buys the program (the sharpened missing ingredient)

The missing ingredient refines: not just "an archimedean Poisson
exchange," but A DUALIZING OBJECT WITH A NONTRIVIAL CONNECTED/RATIONAL
LAYER. In spectra that is exactly the Anderson shape I_Z =
fib(I_Q -> I_{Q/Z}): the I_Q slot is the continuum slot, and it is
precisely what dies F_2-linearly (Hom(F_2-module, Q) = 0) - which is
WHY the mod-2 world is BC-only and kappa-blind. Candidate carriers,
in program terms: a real-cyclotomic ANDERSON (not BC) duality over a
base that still sees Z or R (TR/TC-level over Z_2 rather than Tate
mod 2; or a condensed home where R itself is an object). Note the
literature DD archived (Heard-Stojanoska, Greenlees-Meier) is Anderson
self-duality - the I_Q slot is already the theorem-shaped part of the
precedent. Fail-closed deliverable: DD.4 should be pursued for the
scheme and the pole (its two remaining duties), NOT for K1.

## 2. PART 2 VERDICT: BOTH CONSTANTS ADJUDICATED - THEY DISSOLVE INTO SCHEME SLOTS

Q-SCHEME quadruples (doc 21 sec 2), both sides:

```text
cone side:  ladder  = fix->Tate cone of the Euler tower (banked, KG1)
            weights = TWO banked gradings: degree (xbar, y) = (2, 1)
                      vs supply-weight (1, 1)  [doc 25's flagged
                      convention boundary - this is the whole story]
            scale   = none (zeta_2(0,.) is invariant under joint
                      rescale of offset and parameters)
            scheme  = recentring shift to the critical center
EF side:    ladder  = the pole pair {0, 1} of zeta (xi's s(s-1) roots)
            weights = n^{-s} supply (weight units)
            scale/scheme = xi's prefactor 1/2 is a NORMALIZATION
                      (chosen so xi(0) = 1/2): -d/ds log(c s(s-1)) is
                      c-independent (FFG7, exact) - the EF sees the
                      ROOT PAIR and nothing else of the prefactor.
```

### 2.1 The 1/4-vs-1/2 (FFG6, FFG7): a unit artifact, located exactly

Exact closed form (witnessed, flint + exact B_2 route):

    zeta_2(0, w | a, b) = (w-a)(w-b)/(2ab) + (a^2-3ab+b^2)/(12ab).

The leading coefficient is 1/(2ab) - PURE SCHEME (which grading
couples to s): degree (2,1) gives 1/4 (CC's banked reading); supply-
weight (1,1) gives 1/2 (= xi's number); folded variants (2,2), (4,2)
give 1/8, 1/16. Adjudications, all exact:

- The registered hypothesis "the 1/4 is the degree-vs-weight factor 2
  SQUARED" is REFUTED: the conversion changes ONLY xbar's parameter
  (y has degree 1 = weight 1, the cone's grading is mixed), so the
  factor is ab = 2, not 4.
- The convention boundary IS the folded/unfolded boundary: the
  (2,1)-scheme slices to zeta_H(0, s/2) (spacing-2, Gamma_R ladder),
  the (1,1)-scheme to zeta_H(0, s) (spacing-1, Gamma_C ladder) -
  exact polynomial identities. This is the SAME boundary as BB's
  kappa = pi (folded) = 2pi (unfolded) and doc 20 C3's EF-invisible
  2-powers.
- The comparison target "xi's 1/2" is EF-INVISIBLE (constant
  prefactor; the EF sees only the roots). So the 1/4-vs-1/2 gate AS
  POSED compares two convention-dependent numbers: it DISSOLVES
  (doc 22 A4 pattern: reading-relative). The scheme-INVARIANT content
  of K3's match is the ROOT PAIR {0,1} after forced recentring -
  achieved in both schemes: (2,1) + shift 1 (= duality degree-sum,
  CC's banked match) -> s(s-1)/4 - 1/24; (1,1) + shift 1/2 ->
  s(s-1)/2 + 1/24. READING (flagged, not banked): the weight-scheme
  shift 1/2 = the forced KMS c = 1/2 - a second forced-shift match
  candidate; banking it requires adjudicating the s-coupling
  convention (doc 25's flag), which this gate shows is the one real
  open item behind "1/4 vs 1/2".

### 2.2 The -1/24 (FFG8): the zeta(-1) vacuum, in center-value form

Exact identity (witnessed): the value at the Barnes self-dual center
w_0 = (a+b)/2 is

    zeta_2(0, (a+b)/2 | a, b) = -(a^2+b^2)/(24ab)
                              = zeta(-1) . (a/b + b/a)/2,

i.e. THE ZETA(-1) VACUUM OF THE RANK-2 TOWER weighted by the unit
asymmetry of its two generators; in the tower's own units (1,1) it is
EXACTLY zeta(-1) = -1/12. The carrier is the exact constituent
zeta_H(-1, w) = -B_2(w)/2 - one of the two rank-1 ladders that make
the rank-2 anomaly (FFG6's (1,1) decomposition). The prompt's
hypothesis is CONFIRMED in this precise form. The -1/24 itself is the
off-center remainder K(a,b) = (3 - a^2 - b^2)/(24ab): -1/24 in the
degree scheme, +1/24 in the weight scheme (the sign flips with the
convention; K(2,1) + K(1,1) = 0, recorded as observation, zero
weight). Like the prefactor, K is EF-invisible; its invariant content
is the center-value identity above.

VERDICT: both constants are ADJUDICATED, neither is "matched to xi" -
they are scheme-slot data with exact closed forms, and the EF cannot
see either slot. What the rank sector contributes invariantly: the
pole-pair roots {0,1} under a forced recentring, plus a zeta(-1)
center-value vacuum. The 1/4-vs-1/2 "discrepancy" should be struck
from the open list and replaced by the one real question it encodes:
WHICH grading couples to s (doc 25's convention flag) - equivalently
folded vs unfolded, the same boundary BB's kappa target lives on.

## 3. G-INT6 LEDGER

```text
input                         choices spent
Conjecture DD.4               the SINGLE ASSUMPTION (Part 1 wholly
                              conditional; logged; nothing else rides)
FFG1/FFG2/FFG3/FFG4 data      0 (exact finite computations; Aut(R/Z)
                              = +-1 cited as theorem, not computed)
FFG5 test functions/rescales  Gaussians + c in {1, e, pi}: exhibition
                              device (BB GB1 machinery reused)
Part 2 closed forms           0 new (hand derivations disclosed,
                              witness-checked; CC's banked cone reused)
scheme table (2,1)/(1,1)/...  enumerates the BANKED-FLAG readings; no
                              winner is declared without adjudicating
                              doc 25's convention (flagged open)
kappa = pi                    COMPARISON ONLY (sec 1.4 target talk)
```

Prop FF.1's no-go spends zero numeric choices (equivariance argument,
as BB.1); it survives if FFG5's numerics are discarded.

## 4. HONEST LIMITS

- Part 1 is conditional on DD.4 in a specific sense: it assumes DD.4
  holds IN ONE OF ITS NAMED HOMES (filtered Mod_Y / pro-ind / solid
  F_2). If a future home is genuinely enriched in topological/condensed
  R-modules (so that the degenerate sector itself is an object), Prop
  FF.1's premise fails - by design: that enrichment IS the named
  missing ingredient.
- FFG3's parity/count law is verified for N <= 12 and stated as
  measured; no proof for all N is claimed. Its tower-transition
  behavior (how the odd-level sub-torsors map under x z^2) was
  explored, did not stabilize under the two natural transitions, and
  is left open - consistent with DD's "equivariance exists only on
  the glued object", but unresolved.
- Aut(R/Z) = {+-1} (topological) is cited, not witnessed - the one
  theorem-grade citation Part 1's rigidity contrast leans on.
- Part 2 adjudicates the CONSTANTS; it does not upgrade K3's match.
  The cross-LAYER identification (anomaly polynomial in an exponent
  vs xi's polynomial prefactor) remains open and is now the honest
  formulation of gate infty-4's remaining content; the weight-scheme
  shift-1/2 = KMS-c match is a flagged reading, not banked.
- No RH / zero-side input anywhere; the EF appears only as the
  comparison frame of sec 2 (root pair), per doc 14 fork discipline.

## 5. HAND-OFF (for the lead)

```text
PART 1: F1-FAIL (registered, structural): DD.4's I^cont is NOT BB's
        Poisson exchange - Matlis/BC = TORSION SHADOW of Pontryagin
        (dictionary witnessed, FFG1); the continuum is BC-annihilated
        (FFG4); the scale-rigidity is topological (torus Aut = +-1)
        with no torsion shadow (FFG2); the shear never pins the
        normalization torsor (FFG3, new: 0 / 2^{(N+1)/2} by parity).
        DD.4's triple duty drops to DOUBLE (scheme + pole; not kappa).
        SHARPENED TARGET: a dualizing object with a connected/rational
        layer - Anderson I_Z's I_Q slot over a base seeing Z or R
        (TR/TC-level, or condensed) - is the kappa carrier shape.
PART 2: both constants adjudicated as scheme slots, EF-invisible:
        leading coeff = 1/(2ab) (degree 1/4 <-> weight 1/2, factor 2
        NOT 2^2; = the folded/unfolded boundary); constant = zeta(-1)
        vacuum at the self-dual center (exactly zeta(-1) in own
        units), remainder K = (3-a^2-b^2)/(24ab) = -+1/24 by scheme.
        Invariant residue of K3: root pair {0,1} + forced recentring
        + zeta(-1) center value. Strike "1/4 vs 1/2" from the open
        list; the real open item is doc 25's s-coupling convention.
NEXT:   (i) pose the Anderson/I_Q-slot demand precisely (which base
        category retains a rational layer AND the real-cyclotomic
        structure); (ii) adjudicate the s-coupling convention (it
        would bank the second forced-shift match 1/2 = KMS-c and
        decide folded-vs-unfolded once for K3 and K1 together).
WITNESS: prime_int_ff_kappa_xbar.py (FFG1-FFG8, ALL PASS, exit 0).
```
