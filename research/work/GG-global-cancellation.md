# GG - Global cancellation: does the duality pole-cancellation survive the all-places assembly? (doc 30 ranked front 3)

Status: fresh-context worker GG, 2026-06-10. Required reading executed in
order: doc 30, CC-gluing-consolidation.md IN FULL (part 3: K4 duality
cancellation A_D + A_D' + 1 = 0, residue 0 to 1e-86; part 1: the odd-p
gluings), BB-global-assembly.md (D_glob, per-place combs, product-formula
identification), Q-cc-ftest.md (the quantization-defect pole, sec 5.3-5.4).
Inherited witnesses rerun by me BEFORE any new work:
prime_int_gc_k4_integer_layer.py ALL PASS (QG1-QG5, exit 0),
prime_int_bb_global_assembly.py ALL PASS (GB1-GB5, exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_int_gg_global_cancellation

Sections 1-2 (registrations + the global layer's definition) were written
BEFORE the witness was first run; verdict sections after. DISCLOSURE
(CC-style): the registrations contain exact closed forms derived BY HAND
at design time (the place-uniform cancellation identity, the
prime-power disjointness argument, the zero-mode decomposition of the
survivor sum). They are design-stage derivations, not fits; the witness
checks them and any mismatch is a FAIL of the registration.

## 1. PRE-REGISTERED READINGS (before any run)

### 1.1 Per-place uniformity (task question 1)

```text
GG1 (registered expected): UNIFORM CANCELLATION. The K4 mechanism is an
    identity in the variable x and hence place-blind: with x = p^{-s},
    A_D,p(s) = Sum_{m>=1} x^m = 1/(p^s - 1) has the simple pole at
    s = 0 with residue +1/log p; the mirror A_D',p(s) = 1/(p^{-s} - 1)
    has residue -1/log p; and

        A_D,p + A_D',p + 1 = 0   identically   (the +1 = the gluing
        atom, counted once),

    because 1/(u-1) + 1/(1/u - 1) = -1 for every u != 0, 1 - the SAME
    exact rational identity CC witnessed at p = 2, with log p replacing
    log 2. Slotwise the K2 Gram flip m <-> -m pairs atom p^m with
    mirror p^{-m} (product-formula shadow p^m . p^{-m} = 1), exactly
    CC part 1's forced pairing <y^m, gamma_m'> = delta_{m,m'} at odd p.
    CONVENTION FLAG, registered: CC's intrinsic odd-p carrier F_p[y]
    has weight lattice 2Z (wt y = 2, res(y) = x^2), so the intrinsic
    atom set is {p^{2m}} with residues +-1/(2 log p) and x = p^{-2s};
    BB's assembly uses the full ladder {p^m}, residues +-1/log p. The
    witness checks BOTH normalizations; the cancellation is
    normalization-independent (it is an identity in x). Witnessed at
    p = 3, 5 (p = 2 as control).
    FAIL: wrong residue, nonvanishing glued residue, or pairing flip
    broken at odd p.
```

### 1.2 The global sum (task question 2): the registered G1/G2 dichotomy
### and my expected SPLIT verdict (written before any run)

```text
THE GLOBAL INTEGER LAYER, registered: in D_glob the place-p branch
slots carry atoms {p^m} (D) and {p^{-m}} (D'), plus the gluing atom;
the global integer-layer Dirichlet series is the place-sum of glued
(cancelled) layer series, and the per-place SURVIVORS are the lattice
deltas at p^{-s} = 1 (CC QG3), i.e. the combs
comb_p = (2pi/log p) Sum_n delta(t - 2pi n/log p) (BB GB5).

(G1, task-registered): the global series is entire except the survivor
    combs; candidate theorem "PFD integer layer = EF prime side, all
    regularization poles cancelled by duality".
(G2, task-registered): cross-place interference reintroduces a pole;
    candidate failure mechanism: the SAME integer n = prod p^{v_p}
    appears in multiple place-branches and the identification re-sums
    it.

MY EXPECTED VERDICT (hand derivation, registered before the run): the
dichotomy SPLITS by layer - G1 at the pole layer, G2 AMENDED at the
survivor layer, with the G2 candidate MECHANISM refuted:

GG2 (no double-count - expected REFUTATION of the registered G2
    mechanism): branch atom sets are pairwise DISJOINT across places -
    p^a = q^b forces p = q (unique factorization; a prime power has
    one prime divisor). A composite n = prod p^{v_p} (>= 2 distinct
    primes) is a slot of NO branch; the product-formula identification
    iota couples the class [A] to the TUPLE of distinct slots
    ((p, v_p))_p through the weight identity log A = sum v_p log p -
    a coupling of weights, not an identification of slots. Nothing is
    re-summed. FAIL: any integer found in two place-branches.

GG3 (the cancellation is LOAD-BEARING globally - expected): the glued
    place-sum is identically 0 (each place exactly 0 away from its
    lattice) - entire, pole-free: G1's pole-layer clause. But the
    UNCANCELLED assembly does not even exist: the residue ledger
    sum_p (+1/log p) is non-summable (sum_{p<=X} 1/log p >=
    pi(X)/log X -> oo), and the per-branch global series
    sum_p 1/(p^{s}-1) diverges for ALL s with Re s <= 1 (at s = 1/2:
    terms ~ p^{-1/2}). At ONE place the pole was a finite defect a
    scheme could regularize (Q's reading); at ALL places the
    un-cancelled poles are non-summable - duality cancellation is
    what makes the global integer layer EXIST off the lattices.
    FAIL: cancelled place-sum != 0, or a divergence check fails.

GG4 (the survivor layer - the expected G2-AMENDED obstruction,
    computed exactly): the survivor combs do NOT sum to a
    distribution. Decompose comb_p by Poisson (the K2/Abel exchange,
    BB GB5): comb_p(phi) = sum_{m in Z} phihat(m log p). The m = 0
    ZERO MODE contributes phihat(0) = integral of phi PER PLACE
    (comb density = 1 exactly: weight = spacing), so
    sum_{p<=X} comb_p(phi) = pi(X) phihat(0) + (m != 0 part):
    DIVERGES linearly in pi(X). Poisson-dually the zero mode is the
    n = 0 atom at t = 0 - and s = 0 is the UNIQUE common point of
    all the survivor lattices (2pi i/log p)Z (p^a = q^b again): the
    cross-place attachment points STACK, with weights 2pi/log p,
    non-summable. The m != 0 modes are place-summable (for Gaussian
    phi) and their total

        sum_p sum_{m != 0} phihat(m log p)

    is supported exactly on {+-log(p^m)} = +-log(prime powers): the
    sigma = 0 shell of the EF's prime side (BB sec 4), unit weights.
    So: the EXACT obstruction is the zero mode, one continuum unit
    per place; subtracting it, the renormalized global survivor
    EXISTS and IS the prime-side comb shape. What the assembly needs:
    a per-place comb <-> continuum coupling supplying the
    subtraction - the INTEGER-LAYER FACE OF THE PROPERNESS DEMAND,
    and it is the SAME missing ingredient as BB's B3 (the archimedean
    Poisson exchange), now needed not merely to READ the scale kappa
    but for the global trace to EXIST as a distribution.
    FAIL: lattices share a nonzero point; zero-mode ratio
    S_X/pi(X) not -> phihat(0); renormalized partial sums not
    Cauchy / Poisson per-place identity broken.
```

### 1.3 The comparison (task question 3; F-a discipline: EF comparison only)

```text
GG5 (registered): the determinant-layer (c = 1/2-forced) reading of
    the SAME survivors carries the KMS-1/2 weights:
    -d/ds log[2 sinh(s log p/2)] = -(log p)/2 - log p sum_k p^{-ks};
    the atom part assembles over places to -zeta'/zeta(s) (doc 19
    L2-L3, the supply ladders) - witnessed at s = 2 (sieve-tail tol)
    and s = 3 (tight). The DC face -(log p)/2 per place sums to
    -theta(X)/2 -> -oo: the SAME zero-mode obstruction, determinant-
    layer dress (filtration layer: pi(X) phihat(0); determinant
    layer: theta(X)/2). COMPARISON ONLY, F-a-flagged: the EF fixes
    the target shape; the verdict does not consume it.
    FAIL: assembled atom sum misses -zeta'/zeta beyond tail bound;
    theta-divergence check fails.
```

### 1.4 Carrier guard (task question 4)

```text
GG6 (registered): EPSTEIN DEATH POINT (AA E3/E4, executed at the
    integer layer): the place-branch construction consumes the map
    n -> (v_p(n))_p, i.e. UNIQUE FACTORIZATION of the label monoid.
    Epstein carrier Q(x,y) = x^2 + 5y^2 (Z^2, norm only, no mu): the
    represented-norm monoid is NOT factorial - 36 = 4 . 9 = 6 . 6
    with 4, 9, 6 all represented and all IRREDUCIBLE among
    represented norms (2, 3 are not represented): no well-defined
    v_q, hence no place-branches, no per-place pole pair, nothing to
    cancel, no survivors, NO GLOBAL OBJECT. DH: no carrier group at
    all, dies before the norm (bookkeeping, AA's profile).
    FAIL: 2 or 3 represented, or the double factorization fails to
    materialize, or any death-cascade flag inconsistent.
```

Evaluation rules fixed in advance: exact integer / Fraction arithmetic
for every algebraic identity (cancellation, disjointness, recomposition,
Epstein factorizations); flint ball arithmetic (prec 300) for every
analytic value (residue limits, theta/comb sums, zeta values); zeta'(s)
by arb central difference h = 10^-30 at prec 300 (disclosed); explicit
sieve to 10^6; tolerances stated per gate in the witness docstring.
Gaussian test functions are an EXHIBITION device (classical Poisson),
as in BB GB5. No RH / zero-side input anywhere; the EF appears only in
GG5, comparison-only, flagged.

## 2. THE GLOBAL INTEGER LAYER, DEFINED PRECISELY

Per place p, from CC part 3 (p = 2 constructed; p = 3, 5 via CC part
1's gluings + the spent doc-19/20 dictionary):

    branch layer series  A_D,p(s)  = sum_{m>=1} p^{-ms} = 1/(p^s - 1),
    mirror               A_D',p(s) = 1/(p^{-s} - 1),
    gluing atom          +1        (the weight-0 slot, once),
    glued layer          L_p(s)    = A_D,p + A_D',p + 1,
    survivor             the lattice delta at p^{-s} = 1, i.e.
                         comb_p = (2pi/log p) sum_n delta(t - 2pi n/log p)
                         on the vertical line (BB GB5's object).

GLOBAL integer layer (the assembly's atom data, iota spent as in BB):

    L_glob(s)   = sum_p L_p(s)            (the cancelled-branch series),
    T_surv(phi) = sum_p comb_p(phi)       (the survivor sum, tested
                                           distributionally).

The candidate-theorem statement under test (G1 form): L_glob is
identically 0 = entire (all regularization poles cancelled by duality,
place-uniformly), no slot is double-counted by iota, and what remains -
T_surv - is the EF's prime-side comb shape. The registered amendment
(sec 1.2): T_surv itself needs its zero mode subtracted, one continuum
unit per place, before it exists.

## 3. VERDICT: GG1 PASS - THE CANCELLATION IS PLACE-UNIFORM

(Written after the runs; verdicts as registered. WITNESS-ENGINEERING
RECORD, disclosed: GG1-GG3, GG5, GG6 PASS on the FIRST run, predicates
untouched; GG4 FAILED its support clause on the first run at 2.4e-16
vs the registered 1e-30 - the registered clause compared MISMATCHED
place sets (the full integer shell q <= 1e6 contains the m = 1 atoms
of places in (1e4, 1e6], absent from the comb side; my design estimate
of that tail was wrong by 20 orders). The clause was replaced by TWO:
an exact same-place-set comparison (tol 1e-60) and a full-shell
comparison bounded by the explicitly computed place-tail - coverage
strengthened, tolerance corrected to the measured tail scale, no
verdict changed; rerun ALL PASS, exit 0. All numbers below are the
MEASURED values, corrected from the drafted expectations per BB's
discipline precedent.) At p = 3 and p = 5 (p = 2 control): the exact
rational identity 1/(1-x) + 1/(1-1/x) - 1 = 0 holds at 25 Fraction
points (place-blind, as derived); branch residues s A_D,p log p -> +1
and s A_D',p log p -> -1 with monotonically shrinking error (5.5e-5 at
p = 3, 8.0e-5 at p = 5, s = 1e-4); glued residue s L_p(s) -> 0 with
|L_p| < 6e-87 at generic s (matching CC's 1.2e-86 at p = 2); the
intrinsic odd-p
normalization (atoms p^{2m}, x = p^{-2s}) gives residues +-1/(2 log p)
and the SAME exact cancellation; the K2 flip pairs p^m with p^{-m}
(product = 1 exactly, m <= 8). PER-PLACE UNIFORMITY: CONFIRMED AS
REGISTERED. The mechanism never consumed anything 2-specific - it
consumes the two-branch structure + the gluing atom, which CC part 1
forced at every p.

## 4. VERDICT: THE SPLIT, AS REGISTERED - G1 AT THE POLE LAYER,
## G2 AMENDED AT THE SURVIVOR LAYER; THE OBSTRUCTION COMPUTED EXACTLY

### 4.1 GG2 PASS: the registered G2 double-count mechanism is REFUTED

Integer-exact: all prime powers p^m <= 10^6 enumerated over all places;
every atom belongs to EXACTLY ONE (p, m) (multiplicity 1, no
exceptions). Every composite A <= 20000 with >= 2 distinct prime
factors is a slot of NO branch; iota's recomposition prod p^{v_p} = A
is integer-exact with log A = sum v_p log p to 1.8e-15, and the coupled
slots ((p, v_p))_p are pairwise distinct as slots. NOTHING IS
RE-SUMMED. The product-formula identification couples WEIGHTS across
places; it never identifies slots.

### 4.2 GG3 PASS: the duality cancellation is LOAD-BEARING globally

Cancelled: L_p(s) = 0 exactly at every rational test point, every
place, so L_glob = 0 identically - entire, pole-free: G1's pole-layer
clause HOLDS. Uncancelled: the residue ledger sum_{p<=X} 1/log p grows
6235.3 (X = 10^6) vs 159.6 (X = 10^4) - non-summable (>= pi(X)/log X
witnessed); the per-branch series at s = 1/2, sum_{p<=X} 1/(sqrt p - 1),
grows 181.4 (10^6) vs 33.7 (10^4) - divergent on the critical line.
NEW QUANTITATIVE POINT (registered, now witnessed): at one place the
pole was a finite scheme-regularizable defect; at all places the
un-cancelled poles are NON-SUMMABLE. Duality cancellation is not
hygiene - it is the existence mechanism for the global integer layer.

### 4.3 GG4 PASS: the exact obstruction - the ZERO MODE, one continuum
### unit per place

- Shared attachment point: p^a != q^b for all p < q in {2,3,5,7,11},
  1 <= a, b <= 60 (integer-exact): the survivor lattices
  (2pi/log p)Z intersect pairwise ONLY at s = 0 - every place's comb
  stacks an atom (weight 2pi/log p, non-summable by GG3's ledger) on
  the single cross-place attachment point.
- Per-place Poisson: comb_p(phi) = sum_m phihat(m log p) to < 1e-60
  (Gaussian phi, both sides computed independently in arb, p <= 10^4).
- Zero-mode divergence: S_X = sum_{p<=X} comb_p(phi) has
  S_X/(pi(X) phihat(0)) = 1.2019, 1.0300, 1.0041 at X = 10^2, 10^3,
  10^4 (-> 1 monotonically): T_surv diverges linearly in pi(X),
  coefficient = phihat(0) = the continuum unit, EXACTLY as derived.
- Renormalized convergence: R_X = S_X - pi(X) phihat(0) moves by
  |R_{10^4} - R_{10^3}| = 5.1e-9 while S moves by ~2660 (= 1061 new
  places x the continuum unit); R converges to
  sum_p sum_{m!=0} phihat(m log p) = 12.65064055... (Gaussian width 1),
  supported exactly on +-log(prime powers) (GG2's set, independently
  enumerated as integers: same-place-set match 7.3e-85; full-shell
  match 2.4e-16 = exactly the disclosed place-tail): the sigma = 0
  shell of the EF prime side.

OBSTRUCTION, stated exactly: T_surv - pi(.) x (continuum unit)
converges; T_surv does not. The assembly needs ONE CONTINUUM UNIT PER
PLACE subtracted - a comb <-> continuum coupling. This is the
integer-layer face of the properness demand, and it is the SAME missing
object as BB's archimedean Poisson exchange, with the demand UPGRADED:
BB proved the exchange is needed to read the scale kappa; GG shows it
is needed for the global survivor trace to EXIST distributionally. The
only continuum in D_glob is the degenerate sector - the subtraction is
precisely a degenerate-sector coupling, per place.

## 5. THE COMPARISON (GG5 PASS; F-a: EF as comparison only)

The determinant-layer (c = 1/2) reading of the same survivors assembles
to the supply ladders: sum_{p^k <= 10^6} log p . p^{-ks} equals
-zeta'/zeta(2) to 1.0e-6 (tail tol 2e-5) and -zeta'/zeta(3) to
4.0e-13 (tol 1e-11) - doc 19 L2-L3 re-witnessed from the assembled
object. The determinant-layer DC face -(log p)/2 sums to -theta(X)/2:
-499242 at X = 10^6 vs -49843 at 10^5 (ratio 10.0, unbounded) - the
same zero-mode obstruction in determinant dress. WHAT IS GENUINELY NEW
(the F-a-disciplined statement): in Q's framework the s = 0 pole could
only be evaded by scheme choice (non-geometric exactness set) or by
abandoning zeta-regularization; the program now possesses, at the pole
layer, the candidate theorem

    PFD INTEGER-LAYER THEOREM (candidate): in D_glob every
    regularization pole of the integer layer (the pair +-1/log p at
    s = 0, one per place, non-summable if uncancelled) is killed
    STRUCTURALLY by the K2 duality, place-uniformly, with no
    cross-place double-counting; the cancelled layer is identically
    zero (entire), and what remains is exactly the survivor comb
    family {comb_p} - the EF prime side's sigma = 0 shell, whose
    c = 1/2 determinant reading is the Lambda(n) n^{-1/2} supply -
    MODULO one renormalization: the place-sum of survivors exists
    only after subtracting one continuum unit per place (the zero
    mode at the shared attachment point s = 0).

Pole-free, duality-symmetric, integer-sourced - and the residual
demand is not a scheme choice but a single structural coupling (the
archimedean exchange), already independently named by BB.

## 6. GG6 PASS: carrier guard - the Epstein death point verified

Represented norms of x^2 + 5y^2 (exact enumeration): 2 and 3 NOT
represented; 4, 6, 9, 36 represented; 4, 6, 9 all IRREDUCIBLE in the
represented monoid; 36 = 4 . 9 = 6 . 6 - two distinct irreducible
factorizations, so no additive valuation v exists (v_6(36) = 2 via one
route, 0 via the other): NO v_p data => no place-branches => no
per-place pole pair => nothing to cancel => no survivors => NO GLOBAL
OBJECT. The death is at the FIRST consumption (the label monoid's
unique factorization), exactly where AA's E3/E4 located it. DH: no
carrier group, dies earlier (bookkeeping). The duality-cancellation
mechanism is Euler-product-load-bearing, as the program demands.

## 7. G-INT6 LEDGER

```text
input                       choices spent
cancellation identity       0 (identity in x; CC's forced pairing)
odd-p normalization         0 spent; the 2Z-vs-Z weight convention is
                            FLAGGED (CC d-list: spacing refinement not
                            forced at odd p); both witnessed, verdict
                            independent of the choice
atom disjointness           0 (unique factorization, exact)
zero-mode decomposition     0 (Poisson on (log p)Z, classical; Gaussian
                            = exhibition device, BB precedent)
-zeta'/zeta comparison      EF target: COMPARISON ONLY, F-a-flagged
                            (GG5); verdict independent of it
Epstein death               0 (exact integer enumeration)
```

Verdicts 4.1-4.3 rest on exact identities + classical Fourier analysis;
no fits, no tuned constants. The one registered dichotomy (G1/G2) was
amended by a hand-derived split DISCLOSED at registration time and
confirmed by the witness. Witness-engineering record (full text in
sec 3): five of six gates PASS on first run untouched; GG4's support
clause FAILED first run on a mismatched-place-set tolerance and was
replaced by a strictly stronger two-clause form (exact same-place-set
match + explicitly bounded place-tail); no verdict changed; rerun
ALL PASS, exit 0.

## 8. HONEST LIMITS

- Odd-p place-branches ride on CC part 1's pi_*-level gluings (DMPR
  Cor 5.19) and the spent doc-19/20 dictionary; no spectrum-level
  global object exists (C5''' untouched). BB's odd-p transfer
  assumption is now PARTIALLY discharged (the cancellation clause is
  witnessed at p = 3, 5 from CC's carriers; the full ladder vs 2Z
  weight-lattice convention at odd p remains the flagged convention).
- The renormalized-survivor convergence is exhibited for Gaussian test
  functions; the natural class is the EF's (phihat decay beating
  e^{|xi|} at the sigma = 0 shell; the determinant-layer KMS-1/2
  weights relax this to the classical EF class). Classical Fourier
  analysis, not a new theorem.
- The zero-mode subtraction is STATED as what the assembly needs; no
  candidate coupling is constructed here (that is BB's step-3 demand;
  candidate carriers: degenerate sector, K3 Barnes sector, C5''').
- "Integer layer" = slot/atom data (CC's L-i..L-iii exhaustiveness at
  pi_* level); a spectrum-level object could carry more.
- The s = 0 stacking and the m = 0 density divergence are two faces of
  one zero mode (Poisson-dual); the witness gates the density face
  quantitatively and the stacking face via the exact lattice-
  intersection + non-summability ledger.
- No RH / zero-side input anywhere.

## 9. HAND-OFF

```text
Q1 (uniformity): PASS - cancellation place-uniform (p = 3, 5 witnessed,
    exact; residues +-1/log p, glued residue < 1e-80); mechanism
    consumes only two-branch + gluing atom, which CC forced at all p.
Q2 (global): SPLIT, both registered readings located: G1 HOLDS at the
    pole layer (L_glob = 0 identically; no double-count - the G2
    mechanism REFUTED exactly; uncancelled assembly non-summable:
    cancellation is the EXISTENCE mechanism). G2 AMENDED at the
    survivor layer: obstruction = the ZERO MODE (n = 0 atom stacking
    at the unique shared lattice point s = 0 / m = 0 unit density per
    comb), divergence pi(X) phihat(0) exactly; renormalized survivor
    converges to the sigma = 0-shell prime side.
Q3 (comparison): candidate theorem stated (sec 5): pole-free,
    duality-symmetric, integer-sourced global trace = the prime-side
    comb measure, modulo one continuum subtraction per place = the
    integer-layer face of the properness demand = BB's archimedean
    exchange, UPGRADED from scale-reading to existence.
NEXT: the zero-mode coupling and BB's kappa-coupling are now ONE
    demand at two layers (existence + normalization) - the archimedean
    exchange should be posed as a RENORMALIZATION datum (one continuum
    unit per place, scale kappa), not only as a scale-reader; the K3
    Barnes/rank sector (whose -13/24 is finite, CC QG4) is the only
    banked sector with a continuum-flavored regularized total.
```

## 10. Witness (exit-gated, lead can rerun)

    python3 -m scripts.numerics.witness.prime_int_gg_global_cancellation

Inherited, rerun before work: prime_int_gc_k4_integer_layer (ALL PASS),
prime_int_bb_global_assembly (ALL PASS).
