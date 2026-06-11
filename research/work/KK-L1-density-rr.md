# KK - Lemma L1 (density-RR) proved at theorem grade (doc 33 dispatch item 1)

Status: fresh-context worker KK, 2026-06-10. Required reading executed in
order: doc 33 (probe-cycle synthesis), doc 32 (charter),
JJ-archimedean-unit.md IN FULL. Inherited witness rerun by me before any
new work: prime_int_jj_archimedean_unit (ALL PASS, exit 0; AJ5b values
reproduced independently to 3e-7).

Witness (NEW, fail-closed, exit-gated, every PROOF-INTERNAL estimate gated
with the proof's own derived constants, not just the conclusion):

    python3 -m scripts.numerics.witness.prime_int_kk_l1_density_rr
    (gates KL0-KL9; ALL PASS, exit 0)

DISCLOSURE: design-stage calibration runs (inline, no files) were used to
check the derived constants had slack before gate registration; every gated
constant below is DERIVED in the proof, none is fitted. After the first run
of the witness file, exactly one amendment was made: the KL9 helper R_Z had
a computational infinite loop (theta called at s ~ 1e-13); the fix is a
truncation at s >= 1e-4 whose omitted terms are bounded by Lemma KK.2
(< 2e-4, inside the registered 5e-3 tolerance). No gate predicate was
changed at any point. Witness then ALL PASS.

HEADLINE: L1 is now a THEOREM with explicit constants, proved with NO
prime-counting input of any kind - not PNT, not Chebyshev, not Mertens,
not even Poisson/theta-FE. Total arithmetic input: unique factorization
at the finitely many twisted places. Total analytic input: second-order
Euler-Maclaurin and geometric series. The PNT-dependence verdict is
NEGATIVE (sec 5), and the place where PNT-strength input WOULD become
necessary is located exactly (infinite twist support).

## 1. Setting and precise statement

### 1.1 Objects (JJ sec 1.3, restated exactly)

M = (Z_{>=1}, x), the free effective monoid on the primes. A (square,
v_p-coupled) twist class is D = (a; m) with a in R and m = (m_p) in
Z^{(P)} (finitely many nonzero entries, support P, J := |P|). Its weight
on M:

    w_D(A) = e^{-a} A prod_p p^{-m_p v_p(A)} ,   A in M,

and the theta-regularized count and its renormalized in-family RR pairing:

    h^0(a; m) = log( 1 + 2 sum_{A in M} e^{-pi w_D(A)^2} )  in [0, +oo],
    chi_tw(a; m) = h^0(a; m) - h^0(-a; m)     (same m, reflected a).

(The TRUE in-family dual (-a; -m) diverges for m != 0 - part (A) below
makes that a theorem; chi_tw is the renormalized pairing JJ measured in
AJ5b.)

For m <= 0 write d_p := 1 - m_p >= 2 (d_p = 1 at untwisted places),

    S_m := { n >= 1 : d_p | v_p(n) for all p in P }   (the image comb),
    rho_p := (1 - 1/p) / (1 - p^{-d_p}) <= 1,    rho(m) := prod_p rho_p,

and the proof constants (all explicit, all gated):

    r = prod_{p in P} p,  c = prod (1 - 1/p),  sigma = prod (1 + p),
    L(a) = 1 + a/log 4,   L4(x) = 1 + (log x)/log 4,
    B_1 = 4/3,  B_J = (4/3)(1 + B_{J-1}),
    C_T = (2 pi / 9) sigma + ( 1.01 * 2^J e^{-pi} + c/2 ) B_J,
    E_T(x) = c B_J L4(x)^{J-1} + 2^J L4(x)^J.

### 1.2 THEOREM KK.L1 (density-RR with explicit constants)

(A) EFFECTIVE CONE = FINITENESS LOCUS (divergence locus is its
    complement). h^0(a; m) < oo for some a (equivalently: for all a)
    if and only if m_p <= 0 for all p. For any m with some m_p >= 1,
    the theta sum diverges and h^0(a; m) = +oo for EVERY a. Hence the
    finiteness locus of the divisor lattice is exactly the cone
    Eff_Z = {m <= 0}, and the duality D -> -D maps Eff_Z \ {m = 0}
    into the divergence locus: genuinely square divisors have no
    internal RR dual (JJ AJ5a, now for the whole cone). The unique
    duality-stable slice is {m = 0}, the curve shadow (AJ4, exact RR).

(B) DENSITY-RR. Let m <= 0, J = |P| >= 1. For all a >= 0:

      | theta_{S_m}(e^{-a}) - (rho/2) e^{a} | <= C_T L(a)^{J-1},

    and whenever u(a) := (1 + 2 C_T L(a)^{J-1}) e^{-a} / rho <= 1/2:

      | chi_tw(a; m) - a - log rho(m) |
          <= (2/rho)(1 + 2 C_T L(a)^{J-1}) e^{-a}  +  2.02 e^{-pi e^{2a}}.

    In particular chi_tw(a; m) - a -> log rho(m) = sum_p log rho_p with
    defect O(a^{J-1} e^{-a}); for J = 1 the defect is O(e^{-a}) - JJ's
    measured rate, now proved. The constant is additive over places by
    construction (log rho = sum log rho_p): GG's "one continuum unit per
    place" is a theorem on the strict square's count layer.

(C) COUNTING LEMMA (the integer-grade form, used by Corollary C1).
    For every real x >= 1:   | N_{S_m}(x) - rho x | <= E_T(x),
    where N_S(x) = #{ n in S_m : n <= x }.

PROPOSITION KK.L1-R (real wall; "boundary" in the honest sense). Extend
m to real values. Then h^0(a; m) < oo iff m_p < 1 for all p; the
divergence locus is the closed set {max_p m_p >= 1}, whose boundary wall
{max_p m_p = 1} carries the blow-up of the RR constant:
rho_p(m) = (1-1/p)/(1 - p^{-(1-m_p)}) -> +oo as m_p -> 1-. The
density-RR asymptotic chi_tw - a -> log rho(m) holds throughout the open
cone (same proof; constants depend on delta = min_p(1 - m_p)). The
integer classes m_p <= -1 of Eff_Z have duals with -m_p >= 1: ON or
beyond the wall. So "divergence locus = effective-cone boundary" means
precisely: the first integer class outside Eff_Z in any positive
direction (m_p = +1) sits exactly ON the real divergence wall, and the
in-family duals of the depth-one effective twists land exactly there.
[Witnessed: KL6 - m=0.5, 0.9 finite with the predicted real density to
5.5e-5; m=+1 on-wall divergence; m=+2 beyond-wall divergence;
rho(0.99) = 72.4 recorded.]

PROPOSITION KK.U (universality; the Gaussian is NOT load-bearing for L1).
Let f: [0,oo) -> [0,oo) be C^2 with f(0) = 1, f'(0) = 0, f and f'
integrable and -> 0, K_f := int_0^oo |f''| < oo, and f(x) <= C_f e^{-k x}
eventually. Then with h^0_f built from f instead of the Gaussian,
chi_f(a; m) - a -> log rho(m) + log( 2 I_f ),  I_f = int_0^oo f.
The place structure (rho, its product over places, the cone, the wall)
is independent of the unit; the Gaussian's only role in L1 is the
normalization 2 I_f = 1 (and, via vdGS, exact RR on the m = 0 slice).
[Witnessed: KL8, quartic unit e^{-pi x^4}, constant log(2 Gamma(5/4)/
pi^{1/4}) hit to 1.2e-4.]

PROPOSITION KK.P (the defect's fine structure, J = 1; elementary). For
m supported at one prime p with d = d_p:
e^a (chi_tw(a) - a - log rho) = (1 + 2 Pi(a)) / rho + O(e^{-a}), where
Pi(a + log p^d) = Pi(a) is log p^d - periodic (an explicit absolutely
convergent sum, eq. (9) below). The defect is NOT monotone-decaying in
structure: it is e^{-a} times a log-periodic comb. This REREADS JJ's
recorded AJ5b fine structure: JJ's own numbers satisfy
d_T2(5)/d_T2(5+log4) = 5.842e-3/1.464e-3 = 3.99 ~ e^{log 4} - the comb
JJ registered (then recorded as refuted) IS present, at coefficient
level; JJ's grid masked it because e^{-a} dominates raw d_T(a).
[Witnessed: KL9 - period-log4 invariance of e^a d(a) to 1.3e-4, half-
period swing 0.254, and the elementary formula predicts the measured
coefficient to 2e-4.]

## 2. Proof of Theorem KK.L1

Throughout, theta(s) := sum_{n>=1} e^{-pi n^2 s^2} (s > 0).

### Lemma KK.1 (twist bijection; first multiplicativity consumption)

For m <= 0 the map phi_m(A) = A prod_{p in P} p^{k_p v_p(A)}
(k_p = -m_p = d_p - 1) is a bijection M -> S_m, and
w_D(A) = e^{-a} phi_m(A). Hence the weight multiset of D is exactly
{ e^{-a} n : n in S_m }, each with multiplicity one, and

    h^0(a; m) = log( 1 + 2 theta_{S_m}(e^{-a}) ),
    theta_S(t) := sum_{n in S} e^{-pi n^2 t^2}.                     (1)

Proof. v_p(phi_m(A)) = d_p v_p(A) for p in P and = v_p(A) otherwise, so
phi_m lands in S_m and A is recovered from its image valuation-wise
(injectivity); given n in S_m, the A with v_p(A) = v_p(n)/d_p (p in P),
v_q(A) = v_q(n) (q not in P) maps to n (surjectivity). This uses that
v_p exist and determine the element - i.e. M free on the primes. QED.

Unique-factorization consumption #2: every n in S_m factors UNIQUELY as
n = q u with q in Q := { prod_{p in P} p^{d_p j_p} : j_p >= 0 } and
gcd(u, r) = 1. Therefore (absolute convergence permitting; established
in KK.5)

    theta_S(t) = sum_{q in Q} g(q t),
    g(s) := sum_{gcd(u, r) = 1} e^{-pi u^2 s^2}
          = sum_{d | r} mu(d) theta(d s)                            (2)

by inclusion-exclusion over the 2^J squarefree divisors of r
(consumption #3: CRT/coprime splitting - this is where the Euler-product
structure of the density enters).

### Lemma KK.2 (the unit estimate; Euler-Maclaurin, NO Poisson)

For ALL s > 0:

    psi(s) := theta(s) - 1/(2s) + 1/2   satisfies  |psi(s)| <= pi s / 6, (3)
    and for s >= 1:  theta(s) <= 1.01 e^{-pi s^2}.                   (4)

Proof. f(x) := e^{-pi s^2 x^2} has f'(0) = 0, f, f' -> 0 at infinity.
Second-order Euler-Maclaurin on [0, N], N -> oo:
sum_{n>=1} f(n) = int_0^oo f - f(0)/2 + Rem,
|Rem| <= (1/12) int_0^oo |f''|. Here int_0^oo f = 1/(2s), f(0) = 1, and
|f''(x)| <= (2 pi s^2 + 4 pi^2 s^4 x^2) e^{-pi s^2 x^2}, with
int_0^oo e^{-pi s^2 x^2} dx = 1/(2s) and
int_0^oo x^2 e^{-pi s^2 x^2} dx = 1/(4 pi s^3) (one integration by parts
from the first - still no Poisson). So int |f''| <= pi s + pi s = 2 pi s
and |Rem| <= pi s/6, giving (3). For (4): theta(s) = e^{-pi s^2}
sum_{n>=1} e^{-pi (n^2-1) s^2} <= e^{-pi s^2} (1 + sum_{j>=1}
e^{-3 pi j}) <= 1.01 e^{-pi s^2} using n^2 - 1 >= 3(n-1) and s >= 1. QED
[Gated KL1: measured worst |psi|/(pi s/6) = 0.239, worst tail ratio
1.00008 - the proof constants hold with 4x slack.]

We also use the elementary inequality

    e^{-pi v^2} <= e^{-pi} / v   for v >= 1                          (5)

(equivalent to log v <= pi(v^2 - 1), true since log v <= v - 1).

### Lemma KK.3 (comb constants; geometric series only)

For x >= 1, with Q as above (note p^{d_p} >= 4 for every p in P):

    Q(x) := #{q in Q : q <= x} <= L4(x)^J,                           (6a)
    T(x) := sum_{q in Q, q > x} 1/q <= B_J L4(x)^{J-1} / x,          (6b)
    U(x) := sum_{q in Q, q <= x} q <= (4/3) x L4(x)^{J-1}.           (6c)

Proof. (6a): j_p <= log x / (d_p log p) <= log x / log 4 for each
factor. (6b) by induction on J. J = 1: the q > x form a geometric
sequence with ratio p^{-d_p} <= 1/4 starting below 1/x, so
T(x) <= (1/x) * 1/(1 - 1/4) = (4/3)/x =: B_1/x. Step: split q = u v,
u in Q_1 (powers of p_1^{d_1}), v in Q' (the other J-1 places):
T(x) = sum_v (1/v) sum_{u > x/v} 1/u. For v <= x the inner sum is
<= (4/3) v/x (J = 1 case); for v > x it is <= 4/3 total. So
T(x) <= (4/3) [ Q'(x)/x + T'(x) ] <= (4/3)(1 + B_{J-1}) L4(x)^{J-1}/x
= B_J L4(x)^{J-1}/x by (6a) for Q' and induction. (6c): J = 1 is a
geometric sum with ratio >= 4, dominated by its largest term <= x:
U <= x/(1 - 1/4) = (4/3)x. Step: U(x) = sum_{v <= x} v U_1(x/v)
<= sum_v v (4/3)(x/v) = (4/3) x Q'(x) <= (4/3) x L4(x)^{J-1}. QED
[Gated KL3, exact enumeration of Q to 1e8, all five witness combs.]

### Lemma KK.4 (counting lemma = Theorem part (C))

For x >= 1: |N_S(x) - rho x| <= E_T(x) = c B_J L4(x)^{J-1}
+ 2^J L4(x)^J.

Proof. Phi_r(y) := #{u <= y : gcd(u, r) = 1} = sum_{d | r} mu(d)
floor(y/d) = c y - sum_d mu(d) {y/d}, so |Phi_r(y) - c y| < 2^J. Then
N_S(x) = sum_{q in Q, q <= x} Phi_r(x/q) gives
N_S(x) - rho x = -c x T(x) + sum_{q <= x} eta(x/q) with |eta| < 2^J,
since rho = c sum_{q in Q} 1/q (the product formula for the density:
sum_Q 1/q = prod_p (1 - p^{-d_p})^{-1}, hence rho = prod rho_p -
multiplicativity consumption #3 again, now quantitative). Apply (6b) and
(6a). QED
[Gated KL2 at EVERY integer x <= 1e6, five combs; worst ratio to the
bound: 0.16.]

NOTE the constant: the bound is polylog(x), NOT a power of x, and needs
no zero-free region, no prime counting - S_m is cut by congruence
conditions on valuations at FINITELY many primes; its counting function
is exact floor arithmetic. This is the precise reason L1 is elementary.

### Lemma KK.5 (master remainder = first display of part (B))

For 0 < t <= 1 (t = e^{-a}, a >= 0):

    | theta_S(t) - rho/(2t) | <= C_T L(a)^{J-1}.                     (7)

Proof. By (2) and (3), for each q (using sum_{d|r} mu(d) = 0, J >= 1 -
the constant -1/2 of (3) cancels EXACTLY across the inclusion-exclusion,
which is why no boundary constant survives at twisted level):

    g(q t) - c/(2 q t) = sum_{d | r} mu(d) psi(d q t),               (8)
    |g(q t) - c/(2 q t)| <= (pi/6) q t sum_{d | r} d = (pi/6) sigma q t.

Since rho/(2t) = sum_{q in Q} c/(2qt) (geometric/product formula,
absolutely convergent), split the q-sum at 1/t:

(i) q <= 1/t: by (8), sum <= (pi/6) sigma t U(1/t)
    <= (pi/6)(4/3) sigma L(a)^{J-1} = (2 pi/9) sigma L(a)^{J-1}  [(6c)].
(ii) q > 1/t: here bound the two halves separately. |g(qt)| <=
    sum_{d|r} theta(d q t) <= 2^J * 1.01 e^{-pi (qt)^2}  [(4), theta
    decreasing] <= 2^J * 1.01 * e^{-pi} / (q t)  [(5)]. And the removed
    main terms sum to (c/2t) T(1/t) <= (c/2) B_J L(a)^{J-1}  [(6b)].
    Total for (ii): (1.01 * 2^J e^{-pi} + c/2) B_J L(a)^{J-1}.

Add (i) + (ii): exactly C_T L(a)^{J-1}. Absolute convergence of all
rearrangements is implied by the same bounds. QED
[Gated KL4 at a in {2,...,10}, five combs; worst ratio 0.107 - the
derived C_T holds with ~10x slack.]

### Lemma KK.6 (assembly: the chi_tw bound of part (B))

Let R := theta_S(t) - rho/(2t), so 1 + 2 theta_S(t) =
rho e^a (1 + u'), u' = (1 + 2R) e^{-a}/rho, |u'| <= u(a) <= 1/2 by
hypothesis and (7). Then |log(1 + u')| <= 2|u'| (valid for |u'| <= 1/2),
so |h^0(a) - a - log rho| <= (2/rho)(1 + 2 C_T L(a)^{J-1}) e^{-a}.
Dual side: theta_S(e^{a}) <= theta(e^{a}) <= 1.01 e^{-pi e^{2a}} by (4)
(a >= 0), and log(1 + x) <= x gives 0 <= h^0(-a) <= 2.02 e^{-pi e^{2a}}.
Subtract. QED
[Gated KL5 at the registered points where u(a) <= 1/2 (T2/T3/T2d3:
a >= 4; T23: a >= 7; T235: a >= 11) plus the direct dual-bound check;
worst ratio 0.051. The conclusion reproduces JJ's AJ5b values exactly
(KL0, 3e-7).]

### Lemma KK.7 (part (A): the cone trichotomy)

If m_p <= 0 for all p: theta_S(t) <= theta(t) < oo (S_m subset of
Z_{>=1}, Lemma KK.1), so h^0 < oo for every a. If some m_p >= 1: along
A = p^j, w_D(A) = e^{-a} p^{j(1 - m_p)} <= e^{-a} for all j >= 0, so the
theta sum has infinitely many terms >= e^{-pi e^{-2a}} > 0 and diverges
for every a. For the real version (Prop KK.L1-R): if max m_p < 1, then
w_D(A) >= e^{-a} A^{delta} with delta = 1 - max(m_p, 0) > 0 (since
prod_{p in P} p^{m_p v_p(A)} <= (prod p^{v_p(A)})^{max m_p} <=
A^{max m_p} when max m_p >= 0), so the sum converges; if max m_p >= 1
the p-power line diverges as before (terms -> 1 when m_p > 1, constant
e^{-pi e^{-2a}} when m_p = 1). The real-cone density-RR is the same
proof with Q(m) = { prod p^{(1-m_p) j_p} } (a real geometric comb,
ratios p^{1-m_p} >= 2^{delta} > 1); Lemma KK.3's 4/3 becomes
1/(1 - 2^{-2 delta})-type constants, nothing else changes. QED
[Gated KL6.]

### Proof of Proposition KK.U (universality)

Identical skeleton: Euler-Maclaurin gives sum_{n>=1} f(ns) = I_f / s
- 1/2 + psi_f(s), |psi_f(s)| <= (K_f / 12) s (f'(0) = 0); the -1/2
again cancels in (8); the tail bounds use the eventual exponential decay
of f. The density rho and every comb constant of Lemma KK.3 are
untouched (they live on Q, not on the unit). The limit constant becomes
log(2 I_f rho): with the Gaussian, I_f = 1/2 (no Poisson needed for
THIS; Poisson/vdGS is needed only for the EXACT m = 0 RR of AJ4). QED

### Proof of Proposition KK.P (log-periodic coefficient, J = 1)

For P = {p}, depth d, write D = p^d, so Q = {D^k} and the coprime sieve
at the single prime gives g(s) = theta(s) - theta(p s); by (8),
R(t) = sum_{k>=0} [ psi(D^k t) - psi(p D^k t) ]. Define

    Pi(t) := sum_{k in Z} [ psi(D^k t) - psi(p D^k t) ],             (9)

absolutely convergent: small-s terms are O(s) by (3); large-s terms are
psi(s) - psi(ps) = theta(s) - theta(ps) - (1 - 1/p)/(2s), i.e.
O(1/s) + doubly-exponentially-small by (4). Pi(D t) = Pi(t) by
construction, and R(t) - Pi(t) = -sum_{k < 0} [...] = O(t) by (3)
(geometric in k). By Lemma KK.6's expansion, e^a (chi_tw - a - log rho)
= (1 + 2 R(e^{-a}))/rho + O(e^{-a}) = (1 + 2 Pi)/rho + O(e^{-a}),
log p^d - periodic in a up to O(e^{-a}). QED
[Gated KL9: e^a d(a) = 0.6228 / 0.8769 / 0.6229 / 0.6229 at
a = 7, 7+log2, 7+log4, 7+2log4 - period log 4 to 1.3e-4, half-period
swing 0.254; the truncated (9) + analytic tail predicts 0.6229, 0.8771.]

This completes Theorem KK.L1 and the propositions. Every numbered
estimate (3)-(7), the counting lemma, the assembly bound, the trichotomy,
universality, and the fine structure are SEPARATELY witnessed.

## 3. Corollary C1: what L1 gives the index program

COROLLARY C1 (the h^0 > 0 half of the index input, unconditional on the
strict square, for the twisted monoid family). Let D = (a; m), m in
Eff_Z (m <= 0), and let N(D) := #{A in M : w_D(A) <= 1} = N_{S_m}(e^a)
(Lemma KK.1) - the integer effectivity count (AJ6's unit ball,
transported by the twist; on the m = 0 slice it IS AJ6's N(D)). Then:

(1) N(D) is a finite integer for every a (and = 0 makes sense): the
    count layer exists on the whole effective cone.
(2) EXACT threshold: N(D) >= 1 <=> a >= 0 (1 in S_m always: the
    structure sheaf survives every twist).
(3) Since rho(m) <= 1 (i.e. log rho <= 0, with equality iff m = 0):

      chi_ren(D) := a + log rho(m) > 0  ==>  N(D) >= 1,

    EXACTLY (not asymptotically): chi_ren > 0 forces a > -log rho >= 0.
    The renormalized Euler characteristic - whose existence and value
    is Theorem KK.L1(B) - certifies effectivity with NO error term.
(4) GROWTH LAW: |N(D) - rho e^a| <= E_T(e^a) (Theorem part (C)), so
    for a with E_T(e^a) <= rho e^a / 2:
    | log N(D) - chi_ren(D) | <= 2 E_T(e^a) / (rho e^a) -> 0.
    h^0_int := log N is a GROWING integer observable whose growth rate
    is exactly the renormalized degree - II's structural requirement
    (an integer observable with growing response; signature has
    bounded response) is met by the effectivity count, with the growth
    certified elementarily. [Gated KL7: thresholds exact on the grid,
    growth law to 7e-5 at a = 10.]

WHAT THIS MEANS FOR THE INDEX INEQUALITY (doc 33 sec 2): in
h^0(D) + h^0(K_sq - D) >= chi_sq(D), the input "chi > 0 => h^0 > 0,
i.e. chi > 0 regions are certified effective" is now UNCONDITIONAL on
the strict square for the whole twisted monoid family - with chi_ren
(constant log rho = the per-place continuum units) playing the role of
chi. No zeta, no zeros, no RH-adjacent input anywhere in its proof. The
remaining open half is exactly the one doc 33 names: the dual/K_sq slot
(the divergence proved in part (A) is the obstruction, and the PFD/DD.4
renormalization question is untouched by this memo).

WHAT THIS DOES NOT GIVE (fail-closed): nothing here touches Frobenius-
graph classes (probe 1's defect question), the symmetry/positivity layer
(doc 21 sec 4), or any zero-side statement; chi_ren > 0 certifies
effectivity of TWISTED MONOID classes only.

## 4. Where multiplicativity is consumed (carrier guard)

Three load-bearing consumptions, each named at its lemma:

    #1 (Lemma KK.1) v_p exists: the twist class is DEFINABLE only on a
       monoid with valuations - free on primes.
    #2 (Lemma KK.1) phi_m bijective: unique factorization transports
       the weight multiset to the comb S_m.
    #3 (Lemma KK.4/KK.5) n = q u coprime splitting + inclusion-
       exclusion over d | r: the Euler-product structure of the DENSITY
       rho = prod rho_p. This is where "constants additive over places"
       (JJ's AJ5b, 4e-4) comes from: it is unique factorization made
       quantitative.

EPSTEIN: AJ7 certified the represented-norm monoid of x^2 + 5y^2 has no
valuations (36 = 4*9 = 6*6, distinct irreducible chains). Hence
consumption #1 already fails: the twist family does not EXIST for
Epstein - L1 is not false there, it is NOT A PROPOSITION, exactly the
charter's required death profile (death at the effective cone with the
untwisted count alive: the m = 0 slice - which is all Epstein has - is
the carrier-blind PD layer). DH: no carrier monoid at all.

The Gaussian is NOT load-bearing (Prop KK.U): rho and the cone survive
any admissible unit; the import pins only the normalization 2 I_f = 1.
So L1's structural content is 100% multiplicativity, 0% Gaussian.

## 5. PNT-dependence verdict (the probe-2 cross-examination)

VERDICT: L1 NEEDS NOTHING FROM PRIME COUNTING. The complete input list:

    unique factorization at the J twisted primes      (algebra)
    inclusion-exclusion over 2^J divisors of r        (finite algebra)
    geometric series (Lemma KK.3)                     (calculus)
    Euler-Maclaurin order 2 (Lemma KK.2)              (calculus)
    log v <= pi(v^2 - 1)                              (calculus)

No PNT, no Chebyshev, no Mertens, no Poisson/theta-FE, no zeta values.
(Mertens-grade citations are therefore NOT needed - stronger than the
task's allowance.)

WHERE PNT-STRENGTH INPUT WOULD ENTER (the located boundary of the
elementary regime): every constant degrades explicitly in the twist
support: sigma(r) = prod(1 + p), 2^J, B_J ~ 4(4/3)^{J-1}, and the error
(1 + a/log4)^{J-1}. For any FIXED finite-support twist these are
constants and the defect -> 0. A divisor class with INFINITE twist
support (e.g. a canonical-type class twisting all places, or any limit
along the cone with J -> oo coupled to a) breaks every one of these
bounds at once, and controlling prod_{p <= y}(1 - 1/p)-type densities
uniformly is exactly Mertens; controlling the comb error uniformly in J
is PNT-grade. That is precisely the density tower probe 2 (II) showed
the integers DO see (li vs x/log x): II's object is the GLOBAL prime
density; L1's combs never count primes - they count integers under
congruence conditions at finitely many places. The two results are
consistent and complementary: density at finite support = elementary
(this memo); density at infinite support = the analytic layer, which is
where any zero-sensitive content must (and per II, does) live. L1
therefore sits strictly below the RH-equivalence floor of doc 13 - as a
lemma must, to be unconditionally provable.

## 6. Witness results (lead-rerun: ALL PASS, exit 0)

    KL0 continuity with JJ AJ5b: c(8) reproduced to 3e-7 (3 twists)
    KL1 |psi(s)| <= pi s/6 (worst ratio 0.239); tail const 1.00008
    KL2 counting lemma at EVERY x <= 1e6, 5 combs (worst ratio 0.16)
    KL3 Q/T/U comb constants, exact enumeration to 1e8 (5 combs)
    KL4 master remainder <= C_T L^{J-1} (worst ratio 0.107)
    KL5 THEOREM bound (worst ratio 0.051) + dual doubly-exp bound
    KL6 trichotomy: wall divergence (m=+1, +2); real interior density
        to 5.5e-5; rho(0.99) = 72.4 recorded
    KL7 corollary: exact thresholds; growth law to 7e-5 at a = 10
    KL8 universality: quartic-unit constant log(2 Gamma(5/4)/pi^{1/4})
        hit to 1.2e-4
    KL9 log-periodic coefficient: period log4 to 1.3e-4, swing 0.254,
        elementary prediction matches to 2e-4

Five combs span the lattice directions: T2, T3 (depth 1, one place),
T2d3 (depth 2, one place: m_2 = -2, rho = 4/7), T23 (two places),
T235 (three places).

## 7. G-INT6 ledger

```text
input                          choices spent
unique factorization           0 (the carrier itself; consumption
                               mapped in sec 4)
Euler-Maclaurin order 2        0 (classical calculus, constants derived
                               in Lemma KK.2 and gated)
Gaussian unit                  inherited F-a flag from JJ/vdGS; proved
                               NOT load-bearing for L1 (Prop KK.U) -
                               the flag now marks ONLY the
                               normalization 2 I_f = 1
witness comb family            calibration choice (5 combs spanning
                               depth/width); all gates are proof
                               constants, no fits
KL8/KL9 tolerances             slack choices on asymptotic statements
                               (2e-3, 5e-3, 1e-3), disclosed; the
                               gated quantities are derived, the
                               tolerances only absorb finite-a error
design calibration runs        disclosed (sec 0); no gate amended
                               after first run (one COMPUTATIONAL fix:
                               R_Z truncation, disclosed)
```

## 8. Honest limits

- The defect rate proved is O(a^{J-1} e^{-a}); for J = 1 this is JJ's
  measured O(e^{-a}) exactly. For J >= 2 the witness ratios suggest the
  true remainder is still O(1)-coefficient log-periodic (KL4 ratios do
  not grow over the tested window); proving the J >= 2 coefficient
  bounded (multi-periodic Pi) was not needed and is not claimed.
- The theorem bound applies where u(a) <= 1/2; below that a it says
  nothing (finite-a regime is covered by KL4's remainder bound only).
- Prop KK.L1-R (real cone) is proved with delta-dependent constants
  sketched in Lemma KK.7; only its J = 1 instances are witnessed.
- Effectivity language for twisted classes is the transported unit-ball
  notion (sec 3); the identification with AJ6's coordinatewise
  divisor inequality is verified exactly only on the m = 0 slice
  (AJ6); extending the coordinatewise reading to twisted classes is
  bookkeeping but was not formalized here.
- Nothing here produces H^1, K_sq, or any duality: part (A) PROVES the
  divergence that makes K_sq the open problem (doc 33 item 2).
- No zero-side statement of any kind is made or implied.

## 9. Hand-off

```text
L1 STATUS: THEOREM (KK.L1 A/B/C + KK.L1-R + KK.U + KK.P), complete
           proof in sec 2, every estimate explicit and gated.
PNT:       NOT needed - nothing above calculus + unique factorization
           at finitely many places; the elementary/analytic boundary
           is located at infinite twist support (sec 5), matching II.
INDEX:     Corollary C1: chi_ren > 0 => effective, EXACT, on the whole
           twisted monoid family; h^0_int = log N grows at rate
           chi_ren (the growing integer observable II demanded, growth
           certified). The h^0 > 0 half of the index input is
           unconditional on the strict square.
DUALITY:   the divergence locus is now a theorem and sits exactly on
           the real wall {max m_p = 1}; the dual-side renormalization
           (doc 33 item 2, PFD/DD.4) is the open half.
GUARD:     multiplicativity consumed at 3 named points; Epstein loses
           the twist family at consumption #1 (L1 not posable);
           Gaussian proved not load-bearing (rho is unit-independent).
NEW READ:  JJ's "defect decays, comb refuted" is corrected: the comb is
           log-periodic at COEFFICIENT level (period log p^d), proved
           and witnessed; JJ's own recorded ratios confirm it (3.99~4).
WITNESS:   prime_int_kk_l1_density_rr.py, KL0-KL9 ALL PASS exit 0.
```
