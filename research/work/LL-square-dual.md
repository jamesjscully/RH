# LL - The square dual: does the PFD/DD.4 duality regularize JJ's divergent dual twist? (doc 33 sec 3 item 2)

Status: fresh-context worker LL, 2026-06-10 (relaunch; prior attempt
died on transport, no artifacts). Required reading executed in order:
doc 33 (I am its question 2), doc 32, JJ-archimedean-unit.md IN FULL
(AJ5a: the certified divergence; the construction U),
CC-gluing-consolidation.md part 3 + GG-global-cancellation.md IN FULL
(the duality cancellation A_D + A_D' + 1 = 0, place-uniform, globally
load-bearing), Z-u2-gluing.md (G and its K2 pairing),
HH-weil-restriction-fork.md (the dual-cone statement the index
inequality must serve). Inherited witnesses rerun by me BEFORE any new
work: prime_int_jj_archimedean_unit (ALL PASS, AJ1-AJ7, exit 0),
prime_int_gc_k4_integer_layer (ALL PASS, QG1-QG5, exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_int_ll_square_dual

Sections 1-2 (registrations + the construction with its hand
derivations) were written BEFORE the witness was first run; verdict
sections after. DISCLOSURE (CC/GG/JJ precedent): sections 1-2 contain
design-stage hand derivations (the comb telescoping, the per-level
zero-mode cancellation identity, the dual-measure weight closed forms
c_p(e), the inhomogeneous functional equation, the sector-N failure
asymptotics). They are derivations, not fits; the witness checks them
fail-closed and any mismatch is a FAIL of the registration.

## 0. The question, posed exactly

JJ AJ5a (certified): in the strict square family, the RR dual of the
effective twist D = (a; m_2 = -1) is the twist m_2 = +1, whose
theta-count DIVERGES - on the fiber A = 2^k B (B odd) the dual weight
w(A) = A 2^{-v_2(A)} e^{-a'} = B e^{-a'} is CONSTANT in k: the
2-power ladder escapes the Gaussian damping entirely; the fiber sum is
Sum_{k>=0} 1, the branch series Sum_m x^m AT ITS POLE x = 1.

GG/CC (banked): the same per-branch divergence at the pole layer is
cancelled by the K2 pairing - A_D + A_D' + 1 = 0 identically (atom p^m
paired with mirror p^{-m}, the gluing atom counted once), place-
uniformly, and the cancellation is the EXISTENCE mechanism for the
global integer layer (GG3: the uncancelled assembly is non-summable).

Doc 33's shape-match conjecture: "a divergent count and a cancelled
pole are the program's two faces of one renormalization." TASK: build
the duality-renormalized dual count h^0_ren(K_sq - D) by re-summing
JJ's divergent dual series through the banked pairing, and decide
(L-a) / (L-b) / (L-c) as pre-registered on the task card.

G-INT6 standing rule: the ONLY new ingredient allowed is the banked K2
pairing; any additional choice is logged and demotes the result.
F-a: no zeta continuation anywhere; vdGS RR shape comparison only.
(In particular the "symmetric branch split" prescription Sum_{k>=1} 1
:= -1/2 - which would assign the fiber the value 1/2 - is REJECTED at
design time: it is zeta(0)-flavored regularization, F-a-adjacent, and
spends an unbanked choice. The construction below uses only classical
per-lattice Poisson + the pairing regrouping.)

## 1. THE CONSTRUCTION (hand derivations, written before any run)

### 1.1 The comb decomposition and the paired resummation

Let T be a finite set of primes, D_T(a) the strict-square effective
twist (m_p = -1, p in T) at scale a, S_T = {n >= 1 : v_p(n) even for
all p in T} its image comb (JJ sec 1.3), rho_T = prod_p rho_p,
rho_p = (1 - 1/p)/(1 - p^{-2}) = p/(p+1) [rho_2 = 2/3, rho_3 = 3/4].
JJ's count is h^0(D_T(a)) = log Theta_T(e^{-a}) with

    Theta_T(t) = 1 + 2 sum_{n in S_T} e^{-pi n^2 t^2}
               = sum_{n in Z : n = 0 or v_p(|n|) even all p} e^{-pi n^2 t^2}.

TELESCOPING (exact, forced - each n hits exactly one multi-index): for
n != 0, 1_{v_p even all p}(n) = sum_{kvec in N^T} prod_p
(1_{p^{2k_p} Z} - 1_{p^{2k_p+1} Z})(n); expanding the product,

    Theta_T(t) = 1 + sum_{kvec} sum_{dvec in {0,1}^T} (-1)^{|dvec|}
                 (theta(N t) - 1),     N = N(kvec,dvec) = prod_p p^{2k_p + d_p},

with theta(x) = sum_{m in Z} e^{-pi m^2 x^2} the Jacobi theta; the -1's
cancel within each kvec-block (sum_d (-1)^{|d|} = 0). Per-lattice
Poisson theta(x) = (1/x) theta(1/x) (classical; the banked exhibition
device of GG GB5/AJ4) gives the EXACT functional equation

    (FE)   Theta_T(t) - 1 = (1/t) Theta_T^dual(1/t),

    Theta_T^dual(u) := sum_{kvec} [ sum_{dvec} (-1)^{|dvec|}
                       N^{-1} theta(u/N) ]      (the PAIRED resummation:
                       the kvec-block of 2^{|T|} terms is the summation unit).

### 1.2 The pairing is the renormalization (the GG mechanism, square face)

Inside each kvec-block, each term N^{-1} theta(u/N) carries the
continuum ZERO MODE N^{-1} * (N/u) = 1/u (theta(x) ~ 1/x as x -> 0):
ONE CONTINUUM UNIT PER LATTICE LEVEL - GG4's zero mode, square dress.
The block's zero modes cancel EXACTLY: sum_d (-1)^{|d|} (1/u) = 0.
What survives per block is doubly-exponentially small (for T = {2}:
block_k = (1/u)[theta(4^k/u) - theta(2.4^k/u)] > 0, <= (C/u)
e^{-pi 16^k/u^2}), so the paired sum converges ABSOLUTELY. UNPAIRED,
the sum does not exist: sum_k 4^{-k} theta(u 4^{-k}) gains one
continuum unit 1/u per level - linear divergence, the square-level
face of GG3 ("the uncancelled assembly does not exist; duality
cancellation is the existence mechanism").

Identification with the banked pairing (the one new ingredient, spent
here): the level pairing (lattice p^{2k}Z with its half-refinement
p^{2k+1}Z, weights N^{-1}) is the K2 branch-mirror pairing read on
lattices - the refinement tower in the dual variable is the mirror
branch (supply p^{-2k}, GG's intrinsic-convention atoms p^{-2m}), each
level paired so its continuum unit is killed by its partner's, the
same slotwise mechanism CC part 3 / GG1 witnessed as
A_D + A_D' + 1 = 0. The +1 reappears below as the unit atom.

### 1.3 The dual measure (what the divergent dual twist re-sums TO)

Regrouping Theta_T^dual by dual point xi (dyadic-rational support,
xi = m/N): the weight at xi is c_T(xi) = prod_p c_p(v_p(xi)) with the
exact closed forms (geometric series, Fraction-exact):

    c_p(e) = rho_p                        for e >= 0   (D-branch + atom),
    c_p(-j) = (-1)^j rho_p p^{-j}         for j >= 1   (mirror branch).

So the dual of JJ's divergent twist is NOT a unit-weight count: it is
a SIGNED MEASURE whose D-branch weight is the density unit rho_p (the
L1 constant) and whose mirror branch carries the signed mirror supply
(-1)^j p^{-j} - the divergent in-family dual (unit weights flattened
along the fiber) is renormalized by transposing the v_p-twist from the
archimedean WEIGHT (where it defeated the Gaussian) into the counting
MEASURE (where it becomes the convergent mirror-branch tower). The
point-grouped series is NOT absolutely convergent (each refinement
depth contributes ~ rho_T/u in absolute value): the measure reading
exists only through the pairing - grouping is load-bearing, exactly
GG3.

### 1.4 The renormalized dual count and the exact RR identity

    h^0_ren(K_sq - D_T(a)) := log Theta_T^dual(e^{a}).

(FE) is then an EXACT, INHOMOGENEOUS Riemann-Roch:

    (RR-exact)  h^0(D) - h^0_ren(K_sq - D) = deg D + eps(D),
                eps(D) = log(1 + e^{-deg D} / Theta_T^dual(e^{deg D})) > 0,

with deg D = a (JJ's convention). The "+1" inhomogeneity is the UNIT
CLASS [1] (n = 0; HH: null/lightlike), counted once - the same
once-counted atom as the +1 in A_D + A_D' + 1 = 0. Limits (hand):
Theta_T^dual(u) -> rho_T as u -> infty - L1's genus constant is the
renormalized dual count's floor; eps(a) -> 0 at rate e^{-a}; JJ's
measured O(e^{-a}) defect d_T(a) acquires the exact closed form
d_T(a) = log[(1 + e^a Theta^dual(e^a))/Theta_T(e^a)] - a - log rho_T,
whose fine structure is the Jacobi tail sum
Theta^dual(u) - rho_T = 2 sum_k 4^{-k} sum_{n>=1} [e^{-pi(n u 4^{-k})^2}
- (1/2) e^{-pi(n u 4^{-k}/2)^2}] (T={2} form): log-p^2-periodic
modulation times e^{-a} decay. Registered sign: Theta^dual(e^a) < rho_T
for a in {5, 8} (approach from BELOW; derived by inverting JJ's banked
d_T values: e.g. at a = 8, T2: delta = rho d_T - e^{-a} ~ -1.6e-4).

### 1.5 The index inequality, posed (the program's target statement)

All terms now defined and computable:

    h^0(D) + h^0_ren(K_sq - D) >= chi_sq(D).

Given (RR-exact), with the RR-canonical chi_sq(D) := deg D + eps(D)
the inequality is EQUIVALENT to h^0_ren(K_sq - D) >= 0: the entire
content of the index inequality is the NONNEGATIVITY of the
renormalized dual count. Conventions tested (both registered):
  chi_0 = deg D:             margin_0 = eps + 2 h^0_ren;
  chi_2 = deg D + 2 log rho: margin_2 = margin_0 - 2 log rho.
Hand asymptotics, registered: on the deep effective sector
margin_2(a) = (e^{-a} + 2 delta_T(a))/rho_T + O(e^{-2a}), where
delta_T(a) = Theta^dual(e^a) - rho_T = rho_T d_T(a) - e^{-a} (JJ's
banked d_T inverted).  Computing from JJ's recorded table: the sign is
INDEFINITE in the fine structure - registered sign table:
T2(5) ~ +1.6e-3, T2(8) ~ +1.7e-5, T3(5) ~ -7.8e-4 (NEGATIVE),
T3(8) ~ +1.4e-4, T23(5) ~ +1.1e-2.  So the bare renormalized dual does
NOT satisfy a clean effective-sector positivity: the margin is
O(e^{-a}) and oscillates with the log-periodic fine structure - which
STRENGTHENS the localization below (the content is the unit atom, not
an asymptotic estimate); margin_0 -> 2 log rho < 0 (fails); sector N
(Schur-negative, a < 0): h^0_ren(a) ~ a + log 2 - pi e^{-2a} -> -infty
DOUBLY EXPONENTIALLY (the dual count lacks its own unit atom; a true
count saturates at 0), so margin_2(-1) ~ -pi e^2 + ... ~ -19.7: FAILS.

THE FAILURE IS ONE ATOM: the dual side of (FE) has no "+1". The
Fourier dual of the unit atom delta_0 is Lebesgue - the CONTINUUM
UNIT. A self-dual count (unit atom on both sides) requires the
continuum unit internal to the formalism: GG's per-place subtraction,
BB's archimedean exchange, JJ's liquid slot - the SAME object. One
LOGGED, DEMOTED insertion is tested to exhibit this: h^0_ren+ :=
log(1 + Theta^dual(e^a)) (give the dual its unit atom by hand). With
it, registered: h^0_ren+ >= 0 everywhere and the index inequality
holds on the FULL grid with chi+ = deg + log rho + log(1+rho)
(marginal as a -> +infty). The insertion is precisely the liquid-slot
placeholder; per G-INT6 it demotes that clause to a diagnosis, not a
result.

## 2. PRE-REGISTERED GATES (written before the first run)

Evaluation rules fixed in advance: exact integer/Fraction arithmetic
for every algebraic identity (telescoping coverage, zero-mode
cancellation, dual-measure weights, Epstein clauses); flint arb prec
300 for every analytic value; theta sums truncated at term < 1e-90
with monotone-tail justification; both sides of every FE gate computed
by INDEPENDENT routes (direct comb sum vs paired lattice resummation).
No RH / zero-side input; no zeta values or continuation anywhere.

```text
LL1 PAIRING = EXISTENCE (T = {2}; u in {e^-1, 1, e, e^3}):
    (a) zero-mode cancellation per level EXACT: 4^{-k} * 4^k = 1 and
        4^{-k} * (1/2) * (2 * 4^k) = 1 (Fraction): the two continuum
        units per block are equal and cancel in the (-1)^{|d|} sum;
    (b) paired convergence: block_k > 0, partial sums Cauchy
        (|S_K - S_{K-1}| < 1e-60 by K <= 14 at these u);
    (c) UNPAIRED DIVERGENCE: partial sums of sum_k 4^{-k} theta(u 4^{-k})
        grow by u * (increment) in (1 - 1e-6, 1 + 1e-6) per level for
        k in [25, 30]: one continuum unit per level, linear divergence.
    FAIL: any clause.
LL2 EXACT FE (RR identity), independent routes, tol 1e-50:
    Theta_T(e^{-a}) - 1 - e^{a} Theta_T^dual(e^{a}) = 0 for
    T in {T2, T3, T23}, a in {-1, -0.5, 0.5, 1, 2, 5} (and a = 8 for
    T2). Direct side: comb sum (JJ's machinery). Dual side: paired
    lattice tower. FAIL: any mismatch.
LL3 DUAL MEASURE (exact Fractions):
    (a) c_p(e) = rho_p (0 <= e <= 8), c_p(-j) = (-1)^j rho_p p^{-j}
        (1 <= j <= 10), from the lattice-membership geometric series;
    (b) multiplicativity c_{23}(xi) = c_2(v_2) c_3(v_3) on a grid;
    (c) NON-ABSOLUTE: sum_{depth <= J} |c| e^{-pi xi^2} grows linearly
        in J (per-depth increment in (0.5, 0.9) for J in [5, 20], u=1,
        T2): the point-grouped reading exists only through the pairing.
    FAIL: any exact identity off / growth absent.
    [WITNESS-ENGINEERING RECORD, disclosed (GG sec 3 precedent): on
    the first run (a)+(b) PASSED and (c)'s WINDOW failed at 0.333 -
    the registered window (0.5, 0.9) was hand-derived with
    |c| = rho 2^{1-j}, inconsistent with the EXACT weight rho 2^{-j}
    that clause (a) of this same gate verifies; the derived increment
    is rho_2/2 = 1/3 exactly (weight x point density x Gaussian mass).
    The clause was replaced by the strictly stronger derived-value
    form |inc - 1/3| < 0.02 plus a no-decay clause; the divergence
    verdict (linear growth, non-absolute) is unchanged; no other gate
    touched; rerun ALL PASS.]
LL4 RR CHI-SHAPE + THE DUAL FLOOR (arb; T in {T2, T3, T23}):
    (a) wiring: |(h^0 - h^0_ren) - a - eps(a)| < 1e-50, eps from its
        closed form, a in {0.5, 2, 5};
    (b) eps(a) in (0, 2 e^{-a}/rho_T) at a in {2, 5, 8};
    (c) floor: |Theta^dual(e^a) - rho_T| < 2 e^{-a} at a in {5, 8};
    (d) SIGN (new structural fact): Theta^dual(e^a) < rho_T at
        a in {5, 8} (approach from below).
    RECORD (not gated): d_T(a) reproduced against JJ's banked table;
    the log-periodic fine structure D(a) = (rho - Theta^dual(e^a)) e^a
    on a grid a in [5, 8].
LL5 INDEX INEQUALITY (the target; pre-registered both ways):
    (a) margin_2 SIGN TABLE as derived from JJ's banked d_T (sec 1.5):
        margin_2 > 0 at (T2,5), (T2,8), (T3,8), (T23,5) and
        margin_2 < 0 at (T3,5), with |margin_2| < 0.02 everywhere on
        that list: the effective-sector margin is fine-structure-sized
        and SIGN-INDEFINITE (no clean positivity for the bare dual);
    (b) margin_0(8) < -0.5 (chi_0 normalization fails: -> 2 log rho);
    (c) SECTOR N FAILS (Schur-negative): for T2,
        h^0_ren at a = -1 is < -15 (doubly-exponential collapse;
        predicted ~ -21.5) and margin_2(-1) < -5 (predicted ~ -19.7);
    (d) equivalence wiring: margin with chi = deg + eps equals
        2 h^0_ren exactly (algebra check at 3 points, 1e-50): the
        inequality's content IS h^0_ren >= 0.
    FAIL: any clause (a FAIL of (a) would itself be reportable: it
    would mean the race goes the other way; the gate is registered on
    the derived prediction).
LL6 THE LOGGED INSERTION (demoted diagnosis): h^0_ren+ :=
    log(1 + Theta^dual(e^a)): h^0_ren+ >= 0 and margin+ := h^0 +
    h^0_ren+ - a - log(rho_T (1 + rho_T)) >= 0 on the FULL grid:
    T2 at a in {-2, -1, -0.5, 0.5, 1, 2, 5, 8}; T3 at {-1, 0.5, 5, 8};
    T23 at {-1, 0.5, 5}.  Registered hand values: T2: m+(0.5) ~ 0.21,
    m+(8) ~ +7e-4 (tight), m+(-1) ~ 0.90; T3: m+(5) ~ 2.0e-3,
    m+(8) ~ +1e-4 (tight); T23: m+(5) ~ 1.2e-2.  In contrast to
    LL5(a), the repaired margin is REGISTERED UNIFORMLY >= 0 (the unit
    atom restores positivity, marginal as a -> infinity).
    FAIL: any negative.
LL7 CARRIER GUARD - EPSTEIN UNFORMABILITY (exact integers): the
    construction consumes (i) v_p to define the comb, (ii) the
    refinement tower p^{2k}Z to define the pairing levels. For
    Q(x,y) = x^2 + 5y^2: 2, 3 not represented; 4, 6, 9 represented
    and irreducible; 36 = 4*9 = 6*6; the would-be comb "v_6(36) even"
    is ILL-DEFINED (v = 2 via the chain 1|6|36, v = 0 via 1|4|36,
    parity differs): no valuation => no comb => no branch ladder =>
    no mirror => NOTHING TO PAIR: the K2 renormalization is
    UNFORMABLE (no branches - GG's death certificate, verified at the
    pairing step itself). DH: no carrier group, dies before the comb
    (bookkeeping, printed). FAIL: any clause.
```

Registered overall verdict (written before the run): (L-a), AMENDED -
the paired re-summation CONVERGES and the RR identity is EXACT in
inhomogeneous form (chi-shape deg D + eps with eps explicit and
vanishing); K_sq exists as a duality-renormalized count; the index
inequality is POSABLE with everything defined, holds on the effective
sector, and FAILS in the Schur-negative sector by exactly one atom
(the dual unit), whose duality-preimage is the continuum unit - the
liquid slot. If LL2 fails: (L-b) with the defect = the FE mismatch,
measured. If LL1(b) fails: (L-c) with the resisting levels named.

## 3. VERDICT: (L-a) AMENDED, AS REGISTERED - THE PAIRING REGULARIZES
## THE DIVERGENCE; THE RESIDUAL IS ONE ATOM

Witness ALL PASS (LL1-LL7, exit 0). Witness-engineering record: one
clause (LL3c's growth window) corrected on disclosed grounds (see the
gate block above; GG sec 3 precedent); every other gate passed the
first run untouched; no verdict changed.

### 3.1 The shape-match is REAL (doc 33's conjecture confirmed in mechanism)

```text
GG/CC (pole layer, banked)            LL (divergent count, witnessed)
----------------------------------    ----------------------------------
branch series A_D = sum x^m, pole     dual-twist fiber = sum_{k>=0} 1 =
at x = 1, residue +1/log p            the branch series AT its pole
                                      (JJ AJ5a, restated exactly)
mirror A_D' + gluing atom:            per level k: lattice + half-
A_D + A_D' + 1 = 0 identically        refinement, continuum zero modes
(zero modes pair and cancel)          1/u EQUAL and cancelling exactly
                                      in the (-1)^{|d|} block sum (LL1a)
uncancelled assembly non-summable     unpaired sum gains 1/u per level
(GG3: cancellation = existence)       (LL1c); point-grouped reading
                                      non-absolutely convergent (LL3c):
                                      the PAIRED grouping is the value's
                                      existence mechanism
survivor after cancellation =         survivor after pairing = the dual
the comb (sigma = 0 shell)            measure: D-branch density rho_p,
                                      mirror branch signed supply
                                      (-1)^j rho_p p^{-j} (LL3a, exact)
the +1 = the gluing atom,             the +1 = the unit class [1] in the
counted once                          inhomogeneous FE (HH: null class)
GG4 zero mode = phihat(0) per         zero mode = 1/u per refinement
place, the named obstruction          level, cancelled BY the pairing -
                                      and the one place it CANNOT be
                                      supplied is the dual unit atom
                                      (sec 3.3)
```

A divergent count and a cancelled pole are indeed two faces of ONE
renormalization: the same pairing, the same per-level zero-mode
cancellation, the same "uncancelled object does not exist" clause.

### 3.2 What was measured (the exact results)

- EXACT RR (LL2): Theta_T(e^{-a}) - 1 = e^a Theta_T^dual(e^a) to
  7.3e-81 worst rel, three twists, independent routes - the FE is an
  identity, so h^0(D) - h^0_ren(K_sq - D) = deg D + eps(D) with
  eps(D) = log(1 + e^{-deg D}/Theta^dual) explicit, positive, O(e^{-a}).
- THE DUAL MEASURE (LL3, exact Fractions): c_p(e) = rho_p (e >= 0),
  c_p(-j) = (-1)^j rho_p p^{-j}, multiplicative over places. The
  renormalization TRANSPOSES the v_p-twist from the archimedean weight
  (where it flattened the Gaussian: JJ's divergence) into the counting
  measure (the signed mirror-supply tower).
- THE FLOOR IS THE GENUS (LL4): Theta^dual(e^a) -> rho_T from BELOW;
  L1's density constant is the renormalized dual count's deep limit.
  JJ's banked d_T table is reproduced to all printed digits THROUGH
  THE DUAL ROUTE (record block), and JJ's registered-then-unseen
  log-periodic fine structure is RESOLVED: D(a) = (rho - dual) e^a
  cycles EXACTLY with period log 4: (0.4203, 0.5286, 0.5797, 0.4714),
  mean ~ 1/2, amplitude ~ 0.08 - it was invisible in d_T only because
  e^{-a}(1 - D(a)) compresses it below JJ's 3e-4 resolution.
- INDEX INEQUALITY (LL5): with chi = deg + eps (RR-canonical) the
  inequality is IDENTICALLY equivalent to h^0_ren >= 0 (LL5d, exact).
  Bare margins: effective sector O(e^{-a}) and SIGN-INDEFINITE
  (T2: +1.6e-3/+1.6e-5 at a = 5/8; T3: -7.8e-4 at 5, +1.4e-4 at 8;
  T23: +1.1e-2 at 5); chi_0 normalization fails to 2 log rho (-0.811);
  Schur-negative sector FAILS doubly-exponentially (margin_2(-1) =
  -19.71, h^0_ren(-1) = -21.52 vs a true count's floor 0).
- THE REPAIR IS ONE ATOM (LL6, DEMOTED diagnosis): giving the dual its
  unit atom (h^0_ren+ = log(1 + Theta^dual), ONE logged insertion)
  makes the margin uniformly nonnegative on the full grid, all twists,
  marginal as a -> infinity (m+(8) = 2e-4): nonnegativity of the dual
  count is exactly what the atom buys.

### 3.3 Why the residual is the liquid slot (the localization)

The FE is INHOMOGENEOUS: the primal side carries "+1" (the unit class
[1], n = 0), the dual side does not. Under Fourier duality the unit
atom delta_0 maps to LEBESGUE - the continuum unit. So a SELF-DUAL
count (unit atom on both sides, vdGS-style homogeneous FE, h^0 >= 0 on
both sides) requires the continuum unit to be INTERNAL to the
formalism: GG's per-place subtraction, BB's archimedean exchange, JJ's
internal-R-with-Fourier - the same missing object, now pinned to a
single atom of the square dual. The pairing renormalizes EVERY
divergent slot of JJ's dual twist (all the v_p-coupled fibers, no slot
resists - L-c is refuted); what it cannot manufacture is the dual's
OWN unit, because that unit's duality-preimage is the continuum.

## 4. THEOREM-CANDIDATE LL.1 + THE TARGET STATEMENT, POSED

THEOREM-CANDIDATE LL.1 (classical; proof = telescoping + per-lattice
Poisson + the doubly-exponential block bound; no zeta input). Let T be
a finite set of primes, D_T(a) the strict-square effective twist
(m_p = -1, p in T), rho_T = prod_p p/(p+1). Then:
 (i)  the K2-paired resummation Theta_T^dual(u) (kvec-blocks as units)
      converges absolutely; each block's continuum zero modes cancel
      exactly; the unpaired and point-grouped readings do not converge
      absolutely (pairing = existence);
 (ii) the dual object is the signed measure c_T(xi) =
      prod_p c_p(v_p(xi)), c_p(e >= 0) = rho_p,
      c_p(-j) = (-1)^j rho_p p^{-j};
 (iii) EXACT inhomogeneous RR: Theta_T(t) = 1 + (1/t) Theta_T^dual(1/t),
      i.e. h^0(D) - h^0_ren(K_sq - D) = deg D + eps(D), eps explicit,
      0 < eps = O(e^{-deg D});
 (iv) Theta_T^dual(u) -> rho_T from below as u -> infinity, with
      log-p^2-periodic fine structure of explicit Jacobi-tail form
      (this subsumes and sharpens JJ's L1).

THE INDEX INEQUALITY (the program's target, posable for the first
time with every term defined):

    h^0(D) + h^0_ren(K_sq - D) >= chi_sq(D),   chi_sq(D) = deg D + eps(D),

which by LL.1(iii) is EQUIVALENT to h^0_ren(K_sq - D) >= 0. STATUS:
posable: YES; true for the bare duality-renormalized count: NO -
sign-indefinite at fine-structure order on the effective sector,
doubly-exponentially false on the Schur-negative sector; true with the
dual unit atom inserted (one logged choice, demoted): YES, uniformly,
marginally at deep effectivity. The target statement is therefore
REDUCED: the index inequality on the strict square family holds iff
the renormalized dual count is nonnegative, and the obstruction to
nonnegativity is one canonical atom whose construction is the liquid
slot. The analytic divergence is no longer the gap; the gap is now a
single structural object.

## 5. G-INT6 LEDGER

```text
input                          choices spent
comb telescoping               0 (forced; each n hits one multi-index)
per-lattice Poisson            0 new (classical Jacobi; the banked
                               exhibition device: GG GB5, JJ AJ4)
kvec-block grouping            THE banked K2 pairing, spent here (the
                               only new ingredient, as charged: branch
                               level paired with its mirror-supply
                               refinement; zero modes cancel as
                               A_D + A_D' + 1 = 0)
zeta-style branch split -1/2   REJECTED at design time (F-a-adjacent,
                               unbanked); not used anywhere
Gaussian e^{-pi x^2}           inherited import (vdGS via JJ),
                               F-a-flagged; never used to derive kappa
chi normalizations             both REPORTED (chi_0, chi_2); the
                               RR-canonical chi = deg + eps is forced
                               by LL.1(iii), not chosen
unit-atom insertion h^0_ren+   ONE logged choice, DEMOTED (LL6 is a
                               diagnosis exhibiting what the atom
                               buys, not a result)
LL3c growth window             corrected post-first-run on disclosed
                               derivation grounds (strictly stronger
                               clause; record in sec 2)
```

No zeta values, no zeta continuation, no RH/zero-side input anywhere;
the EF appears nowhere in the witness.

## 6. HONEST LIMITS

- Everything lives on JJ's STRICT square family (m_p = -1 twists,
  scale a); degrees/H^1/a square Euler form are still absent (V's
  verdict, N-doc M1-M6 untouched). "K_sq" here means: the dual COUNT
  the RR identity needs, constructed; not a canonical divisor class
  on a compactified square.
- LL.1 is stated as theorem-candidate: witnessed exactly; the written
  proof (elementary) is not in this doc.
- The unit-atom localization (sec 3.3) is exact within this family;
  whether the SAME atom suffices for Frobenius-graph classes (HH's
  cone) is untested - that is the dual-cone statement's burden.
- h^0_ren is a SIGNED log-count (the mirror weights alternate); no
  positivity property is claimed for the bare object - indeed its
  failure of positivity is the measured content of LL5.
- The repaired inequality (LL6) is marginal as a -> infinity: any
  future positivity argument has NO slack in the deep-effective limit
  (consistent with HH's joint-cancellation reading: the unit must
  couple, not pad).
- The log-periodic fine structure is exhibited at T2 (period log 4);
  per-place periods log p^2 at other twists are implied by the same
  formula but only T2's cycle is printed.

## 7. HAND-OFF (for the lead)

```text
VERDICT:  (L-a) AMENDED. The PFD/DD.4 duality DOES regularize JJ's
          divergent dual twist, by exactly the GG mechanism (per-level
          zero-mode cancellation; pairing = existence). K_sq exists as
          a duality-renormalized count: the signed dual measure
          c_p(e>=0) = rho_p, c_p(-j) = (-1)^j rho_p p^{-j}, with the
          EXACT inhomogeneous RR Theta_T = 1 + (1/t) Theta_T^dual(1/t).
RR:       h^0(D) - h^0_ren(K_sq - D) = deg D + eps(D), eps explicit,
          positive, O(e^{-deg}); the genus constant log rho_T is the
          dual count's floor (L1 subsumed + sharpened: the log-4
          periodic comb JJ registered and could not see is real,
          amplitude ~ 0.08 in D(a), witnessed).
INDEX:    POSABLE, finally - and equivalent to h^0_ren >= 0. Bare:
          FALSE (sign-indefinite fine structure on the effective
          sector; doubly-exponential failure on the Schur-negative
          sector). With the dual unit atom (one demoted insertion):
          TRUE uniformly, marginal at infinity.
THE GAP:  one atom. The dual side of the FE has no unit class; the
          unit atom's Fourier dual is the continuum unit. GG's
          per-place subtraction, BB's exchange, JJ's liquid slot, and
          the square dual's missing atom are ONE object, now with its
          sharpest description: "the element that makes the square
          dual's FE homogeneous".
WITNESS:  prime_int_ll_square_dual.py (LL1-LL7, ALL PASS, exit 0;
          one disclosed clause correction, LL3c window -> derived
          value 1/3, no verdict changed). Inherited reruns:
          prime_int_jj_archimedean_unit, prime_int_gc_k4_integer_layer
          (both ALL PASS before any new work).
```

## Postscript (2026-06-11, worker NN): the strict-family success was small-place

NN's face test (N-c, certificate-grade): p in {2, 3} are the safe
cells; (5; 2) breaks; the Lambda(p) classes fail always - the
FE-stripped dual carries an exact continuum hole -1/u that no atom
cancels. The index inequality as posed here does not extend to the
graph classes; the unit must be class- and scale-coupled (doc 35).
