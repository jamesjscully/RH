# SS - S1 stress: PP's certified census as THEOREMS (the homogeneous FE, the all-(q,a) inequality, evasion-not-surplus)

Status: fresh-context worker SS, 2026-06-11. Doc 36 stress item S1.
Required reading executed in order: research/proof/36-face-hunt.md,
research/work/PP-ku-face.md IN FULL, research/work/KK-L1-density-rr.md
(the elementary-proof model), research/work/I-c6-ku-square.md (the
lcm-ladder provenance). Inherited witness rerun by me BEFORE any new
work: prime_pp_ku_face_index (ALL PASS KU1-KU9, exit 0; freeze sha256
02250df1...3952 reproduced exactly; 527-point census all-positive
reproduced).

New witness (fail-closed, exit-gated; every PROOF-INTERNAL constant
gated with the proof's own derived value, KK standard):

    python3 -m scripts.numerics.witness.prime_ss_ku_inequality_proof
    (gates SS1-SS8)

DISCLOSURE (KK/PP precedent): sections 0-8 (statements, complete
proofs, gate registrations) were written BEFORE the witness was first
run. Every gated constant below is DERIVED in the proofs; none is
fitted. No zeros are consumed anywhere in this memo or its witness (no
fork_lib import, hence no freeze step is required). F-a discipline: no
zeta values, no zeta continuation; the only analytic inputs are Poisson
summation for Gaussians on cosets (the program's banked exhibition
device, here PROVED from scratch by elementary calculus) and geometric
series. Total arithmetic input: gcd(w, w+1) = 1 and unique
factorization at one prime (Lemma A) - the carrier consumption is
named there.

HEADLINE: all three tasks close with COMPLETE proofs - no named gap.
(1) The homogeneous FE (PP KU1, verified to 5.0e-88) is Theorem SS.1,
an exact identity: coset Poisson + the two-coset structure of the cell
comb; the prime-power hypothesis is consumed exactly once, at the comb
identification (Lemma A), and FAILS for every non-prime-power modulus
(CRT counterexample - the carrier guard is an iff). (2) The 527-point
all-positive census (PP KU4) is Theorem SS.2: m+(q, a) > 0 for EVERY
prime power q >= 3 and EVERY admissible a >= log(q+1), with the
uniform explicit floor m+ >= (4/9) e^{-a} and entry floor >= 1/(3q).
There is no hard middle range: one monotone Gaussian-tail bound
(|H_q| <= G(e^a/q) <= G(1) < 0.173, Lemma D) covers entry to deep in
one stroke, because admissibility u = e^a >= q+1 puts the dual
argument u/q strictly past the Gaussian shoulder. PP's hand constants
are all derived: the threshold H* = -(1+rho)/(1+2rho), the entry-floor
constant 0.74 = 1 - (3/2) G(1) (Corollary SS.2c: it is a LIMIT, proved
two-sided), the deep law +e^{-a}/rho_q with explicit error (Theorem
SS.3). (3) Evasion-not-surplus is Theorem SS.4: e^a rho_q m+ -> 1
exactly, sup_{a >= A} m+ <= 1.298 e^{-A}/rho_q, no uniform floor over
the family; a SURPLUS is equivalent to a strictly positive hole
coefficient, which Theorem SS.1 forbids as an identity - the precise
structural demand is logged for the Castelnuovo risk register (sec 8).

## 0. Objects, conventions, statements

All sums over Gaussians converge absolutely; rearrangements used below
are justified by absolute convergence throughout (geometric-series
domination, Lemma C).

```text
T(x)  := sum_{m >= 1} e^{-pi m^2 x^2}          (x > 0),
theta(x) := 1 + 2 T(x) = sum_{w in Z} e^{-pi w^2 x^2},
G(x)  := 4 x T(x) = 2x (theta(x) - 1),

S_q   := { w in Z : w mod q not in {0, q-1} }   (two-coset comb),
C_q   := { w in Z : q does not divide w(w+1) }  (the ku cell comb,
                                                 Lee / I-doc K2-K3),
Theta_q(t) := sum_{w in S_q} e^{-pi w^2 t^2},

rho_q := (q-2)/q,
D_q(u) := theta(u) - (1/q) sum_{k in Z} (1 + cos(2 pi k / q))
                                        e^{-pi k^2 u^2 / q^2},
H_q(u) := u (D_q(u) - rho_q),

m+(q, a) := log(1 + e^a D) + log(1 + D) - a - log(rho_q (1 + rho_q)),
            D = D_q(e^a)          (PP's margin, LL6/NN calibration),
admissible: a >= log(q + 1)       (PP's entry rule; u := e^a >= q+1).
```

THEOREM SS.1 (the homogeneous FE; PP's KU1/KU2 as an identity).
For every integer q >= 2 and every t > 0:

    Theta_q(t) = (1/t) D_q(1/t),

with NO inhomogeneous term. Consequently, for 0 < t <= 1, with
u = 1/t >= 1:

    | t Theta_q(t) - rho_q | = |D_q(u) - rho_q| <= 2 T(u) + (4/q) T(u/q),

every correction Gaussian; in particular the hole coefficient

    c_hole(q) := lim_{u -> oo} u (D_q(u) - rho_q) = 0     (vs NN d=1:
    sum_{n>=1} e^{-pi n^2 t^2} = 1/(2t) - 1/2 + (1/t) T(1/t):
    inhomogeneity -1/2, dual continuum hole; c_hole = -1 in PP's
    normalization).

Zero-mode ledger (exact, inside the proof): primal origin atom
chi(0) = 1 - 1 - 0 = 0 (0 lies in the 0-coset; the (-1)-coset misses
0 because q | 1 is impossible); dual k = 0 modes 1 - 1/q - 1/q =
rho_q (the comb density). An ATOM subtraction dualizes to a continuum
hole (NN's -1/u); a full COSET subtraction dualizes to a density
reduction - that is the mechanism, made exact.

LEMMA A (carrier guard, an iff). C_q = S_q if and only if q is a
prime power. (Forward: consumed by every theorem below via PP's
dictionary. Backward: for q with two coprime factors > 1, CRT
produces w with q | w(w+1) but w not in {0, -1} mod q - the cell comb
is NOT a two-coset comb, the coset Poisson of Theorem SS.1 does not
apply, and no statement below is even posable. This is the exact
point where "prime power" is consumed.)

THEOREM SS.2 (the inequality, all (q, a); PP's KU4 census as a
theorem). For every prime power q >= 3 and every a >= log(q+1):

    m+(q, a) >= log( 1 + e^{-a} / (rho_q (1 + rho_q)) )
             >= (4/9) e^{-a}  >  0.

Entry floor: m+(q, log(q+1)) >= 1/(3q). Refined per-q floor (gated):

    m+(q, log(q+1)) >= log(1 + F_q / ((q+1) rho_q (1+rho_q))),
    F_q := (1+rho) - G((q+1)/q) (1+2rho)
           - (G((q+1)/q)/(q+1)) (1 + 1.2e-21).

COROLLARY SS.2c (PP's 0.74/q law derived).
q * m+(q, log(q+1)) -> 1 - (3/2) G(1) = 1 - 6 T(1) = 0.740696...
as q -> oo (two-sided sandwich in the proof; PP's hand constant
"~0.74" is this limit).

THEOREM SS.3 (the deep law with explicit error; PP's KU5/D6 as a
theorem). For every prime power q >= 3 and every a >= log(q+1):

    | e^a rho_q m+(q, a) - 1 | <= 1.72 G(e^a / q) + 0.842 e^{-a}/rho_q.

So m+(q, a) = (e^{-a}/rho_q)(1 + O(.)) with the O(.) explicit and
valid from entry on: the first term is doubly exponentially small once
e^a >> q (Gaussian in e^a/q); the second is the universal second-order
log term. (Check against PP's measured deep margins e^a rho m+(q,8) =
0.9995..0.9998: the bound gives 1 +- 8.5e-4 at q = 3 - holds with
factor ~1.7 slack, gated SS5.)

THEOREM SS.4 (evasion, not surplus; the honest negative half).
(i)  ZERO SLACK AT INFINITY: for every prime power q >= 3,
     0 < m+(q, a) <= 1.298 e^{-a}/rho_q for all admissible a; hence
     sup_{a >= A} m+(q, a) <= 1.298 e^{-A}/rho_q -> 0, and
     lim_{a -> oo} e^a rho_q m+(q, a) = 1 exactly (Theorem SS.3).
(ii) NO UNIFORM FLOOR: inf over the admissible family of m+ is 0
     (already along entry points: m+(q, log(q+1)) <= 1.298 /
     (rho_q (q+1)) -> 0).
(iii) SURPLUS IMPOSSIBILITY: if for some q and some beta > 0,
     m+(q, a) >= (1+beta) e^{-a}/rho_q for all large a, then
     liminf_{u -> oo} H_q(u) >= beta (1+rho)/(1+2rho) > 0; but
     |H_q(u)| <= G(u/q) -> 0 (Lemma D). Equivalently: a surplus IS a
     strictly positive hole coefficient, and Theorem SS.1 forbids any
     nonzero hole coefficient as an identity. The face evades the
     kill; it cannot manufacture slack. Sec 8 logs what a surplus
     would structurally require (Castelnuovo register).

PROPOSITION SS.5 (the repayment law, PP's D4/KU3, post-entry, as a
theorem). For all q >= 3 and all x > 0 the EXACT identity

    H_q(q x) = -G(x) + 4x sum_{k>=1} sin^2(pi k/q) e^{-pi k^2 x^2}
               + G(q x)/2

holds, and for x >= 1:

    -G(x) <= H_q(q x) <= -G(x) (1 - 1.0004 pi^2 / q^2) + G(q x)/2.

(The double hole -2x(theta(x)-1) = -G(x) is the law; the curvature
error is O(q^{-2}) relative, exactly PP's recorded small-q deviation;
at q = 121 the relative error bound is 6.8e-4, matching KU3's
measured < 0.4%.)

## 1. Lemma A: the comb is two cosets iff q is a prime power

Proof. Since gcd(w, w+1) = 1, any prime p divides at most one of
w, w+1. Let q = p^j. Then v_p(w(w+1)) = v_p(w) + v_p(w+1) =
max(v_p(w), v_p(w+1)), so q | w(w+1) iff q | w or q | w+1, i.e. iff
w mod q in {0, q-1}. Hence C_q = S_q.

Conversely, if q = q1 q2 with q1, q2 > 1 coprime, choose by CRT w with
w = 0 mod q1 and w = -1 mod q2. Then q1 | w and q2 | w+1, so
q | w(w+1); but w = 0 mod q would force q2 | w, contradicting
q2 | w+1 and gcd(w, w+1) = 1 (q2 > 1), and symmetrically w = -1 mod q
fails. So C_q is strictly smaller than S_q. QED

(Witnessed SS6: for every q <= 300, the residue set
{w in [0,q) : q | w(w+1)} equals {0, q-1} exactly when q is a prime
power and is strictly larger otherwise - exact integers.)

Consumption ledger: this is the ONLY place any theorem below uses
q = p^j. Theorems SS.1-SS.5 hold verbatim for the two-coset comb S_q
at ANY integer modulus q >= 3; the ku LADDER supplies the comb C_q
(I-doc K2-K3, Lee's sieve), and Lemma A is the bridge. On a carrier
without unique factorization the cell address (q, w) is unformable
(PP KU8, I-doc G-INT3) and there is no comb to complete.

## 2. Lemma B: coset Poisson, elementary

LEMMA B. For t > 0, q in Z_{>= 1}, c in Z:

    sum_{w = c mod q} e^{-pi w^2 t^2}
        = (1/(q t)) sum_{k in Z} e^{2 pi i k c / q} e^{-pi k^2/(q^2 t^2)}.

Proof. (i) Gaussian self-transform by calculus: for s > 0 let
I(b) = int_R e^{-pi s^2 y^2} cos(2 pi b y) dy. Differentiating under
the integral (dominated convergence) and integrating by parts,
I'(b) = -(2 pi b / s^2) I(b); with I(0) = 1/s (the normal integral),
I(b) = (1/s) e^{-pi b^2 / s^2}. The sine integral vanishes by parity.

(ii) Periodization: f(y) := e^{-pi t^2 (q y + c)^2}; F(y) :=
sum_{m in Z} f(y + m) converges uniformly on compacts (Gaussian
domination), is continuous and 1-periodic. Its k-th Fourier
coefficient is (Fubini, absolute convergence)

    int_R f(y) e^{-2 pi i k y} dy
      = (1/q) int_R e^{-pi t^2 v^2} e^{-2 pi i k (v - c)/q} dv
      = (e^{2 pi i k c / q}/q) (1/t) e^{-pi k^2/(q^2 t^2)}      [by (i)].

These coefficients are summable (Gaussian in k), so the Fourier series
of F converges absolutely and uniformly to a continuous function with
the same coefficients, hence to F. Evaluate at y = 0: the left side is
sum_m f(m) = sum_{w = c mod q} e^{-pi w^2 t^2}. QED

(Geometric series + second-year calculus; this is the program's banked
Jacobi/coset device, proved self-contained. q = 1, c = 0 is Jacobi's
theta(t) = (1/t) theta(1/t).)

## 3. Proof of Theorem SS.1

By definition of S_q (two excluded cosets, disjoint since q >= 2):

    Theta_q(t) = theta(t) - theta_{0 mod q}(t) - theta_{-1 mod q}(t).

Apply Lemma B to each piece (c = 0 twice with q = 1 and q; c = -1):

    Theta_q(t) = (1/t) [ sum_k e^{-pi k^2/t^2}
                 - (1/q) sum_k (1 + e^{-2 pi i k/q}) e^{-pi k^2/(q^2 t^2)} ].

Pairing k with -k cancels the imaginary parts, 1 + cos(2 pi k/q)
remains: Theta_q(t) = (1/t) D_q(1/t), an identity of absolutely
convergent sums, with no leftover term of any other homogeneity - the
FE is homogeneous because every ingredient is a FULL lattice coset
(contrast: the half-line comb {n >= 1} is not, and its Poisson carries
the boundary term -1/2, NN's stripped unit; PP sec 4).

Expansion at u -> oo: the k = 0 term of the subtracted sum is
(1/q)(1 + 1) = 2/q, and theta(u) = 1 + 2T(u), so

    D_q(u) - rho_q = 2 T(u) - (2/q) sum_{k >= 1} (1 + cos(2 pi k/q))
                                                e^{-pi k^2 u^2/q^2},   (*)

whence |D_q(u) - rho_q| <= 2T(u) + (4/q) T(u/q) (termwise
1 + cos <= 2). Every term is Gaussian in u; c_hole = 0.

Ledger: chi := 1 - 1_{0 mod q} - 1_{-1 mod q} has chi(0) = 1 - 1 - 0
(q | 0; q | 1 impossible) - the primal origin atom is removed by the
comb itself; dually the three k = 0 continuum modes contribute
(1 - 1/q - 1/q)/t = rho_q / t, the density, and nothing else survives
at u^0 or u^{-1} order: PP's D2/D3, now exact statements inside an
identity. QED

(Witnessed SS7: two independent routes, direct comb sum vs
e^a D_q(e^a), rel < 1e-40; SS2 re-certifies |H_q| at u = 8q.)

## 4. Lemma C: calculus constants (all gated, SS1)

LEMMA C. (i) For x >= 1: T(x) <= e^{-pi x^2} / (1 - e^{-3 pi})
<= 1.0001 e^{-pi x^2}.
(ii) G(x) = 4x T(x) is strictly decreasing on [1, oo), and
G(1) <= 4 e^{-pi} (1.0001) < 0.1729.
(iii) G(4)/2 < 1.2e-21.
(iv) sum_{k >= 1} k^2 e^{-pi k^2 x^2} <= 1.0004 e^{-pi x^2} for x >= 1.

Proof. (i) m^2 - 1 >= 3(m - 1) gives T(x) <= e^{-pi x^2}
sum_{j >= 0} e^{-3 pi j x^2} <= e^{-pi x^2}/(1 - e^{-3 pi}) for
x >= 1, and e^{-3 pi} < e^{-9} < 1.24e-4, so the factor is < 1.0001.
(ii) Each summand 4x e^{-pi m^2 x^2} has derivative
4(1 - 2 pi m^2 x^2) e^{-pi m^2 x^2} < 0 for x >= 1 (2 pi > 1);
termwise strict decrease. For the value: e^pi > 23.1406 (e^3 >
20.085536; e^{0.1415926} > 1.1521072 by the positive Taylor partial
sum through x^5; product > 23.14069 > 23.1406; pi > 3.1415926), so
e^{-pi} < 1/23.1406 < 0.0432141, T(1) <= (1.0001)(0.0432141) <
0.0432185, and G(1) = 4 T(1) < 0.172874 < 0.1729.
(iii) G(4) = 16 T(4) <= 16 (1.0001) e^{-16 pi} < 16.01 e^{-50.26}
< 16.01 * 1.5e-22 < 2.4e-21.
(iv) k^2 e^{-pi(k^2-1)x^2} <= k^2 e^{-3 pi (k-1)} for x >= 1, and
1 + 4 e^{-3 pi} + 9 e^{-6 pi} + ... < 1 + 4(1.24e-4) + 9(1.6e-8)(1 +
...) < 1.0004 (geometric domination from k = 3 on). QED

Throughout we write G1 := 0.1729 (the certified upper bound for G on
[1, oo)).

## 5. Lemma D: the two-sided H bound; proof of Proposition SS.5

LEMMA D (master identity and bounds). For all q >= 3, x > 0, with
u = q x:

    H_q(u) = G(u)/2 - G(x) + 4x sum_{k>=1} sin^2(pi k/q) e^{-pi k^2 x^2},

and for u >= q (x >= 1):

    -G(x) <= -G(u/q) <= H_q(u) <= G(u)/2 <= 1.2e-21.

In particular, for ADMISSIBLE (q, a) (u = e^a >= q + 1, so
x = u/q >= (q+1)/q > 1):

    |H_q(e^a)| <= Hhat := G(e^a/q) <= G((q+1)/q) <= G(1) < 0.1729.

Proof. Multiply (*) by u: u (theta(u) - 1) = 2u T(u) = G(u)/2, and
with 1 + cos(2 pi k/q) = 2 - 2 sin^2(pi k/q),

    (2u/q) sum_{k>=1} (1 + cos(2 pi k/q)) e^{-pi k^2 x^2}
        = 4x T(x) - 4x sum_{k>=1} sin^2(pi k/q) e^{-pi k^2 x^2}
        = G(x) - 4x sum_{k>=1} sin^2(.) e^{-pi k^2 x^2},

giving the identity. Lower bound: drop the two nonnegative terms.
Upper bound: sin^2 <= 1 makes the sin^2-sum <= T(x)-sum, so the last
two terms together are <= 0; what remains is G(u)/2, and G(u)/2 <=
G(q)/2 <= G(4)/2 <= 1.2e-21 for u >= q >= 4 -- for q = 3, u >= 4
directly gives G(u)/2 <= G(4)/2. Monotonicity of G (Lemma C(ii))
gives G(u/q) <= G((q+1)/q) <= G(1) on the admissible range, and
G(u)/2 <= G(u/q)/2 <= Hhat (since u > u/q >= 1), so |H| <= Hhat. QED

Proof of Proposition SS.5. The identity is Lemma D's. For x >= 1,
sin^2(pi k/q) <= (pi k/q)^2 and Lemma C(iv) give

    0 <= 4x sum_{k>=1} sin^2(pi k/q) e^{-pi k^2 x^2}
      <= (pi^2/q^2) 4x (1.0004) e^{-pi x^2}
      <= 1.0004 (pi^2/q^2) G(x)        [e^{-pi x^2} <= T(x)]. QED

(Witnessed SS2: identity to 1e-70 and both bounds arb-certified at
q in {9, 121}, x in {0.5 (identity only), 1, 1.5, 3}; the two-sided
H bound certified on a (q, u) grid; G-monotonicity sanity grid.)

## 6. Proof of Theorem SS.2 (and Corollary SS.2c)

Fix a prime power q >= 3 and a >= log(q+1); write u = e^a >= q+1 >= 4,
rho = rho_q in [1/3, 1), D = D_q(u) = rho + H/u, H = H_q(u).

WELL-DEFINEDNESS. |H| <= G1 (Lemma D), so D >= 1/3 - 0.1729/4 > 0.28:
both logarithms in m+ are defined and 1 + uD, 1 + D > 0.

THE EXACT ALGEBRA. m+(q, a) = log[(1 + uD)(1 + D) / (u rho (1+rho))],
and expanding D = rho + H/u:

    (1 + uD)(1 + D) - u rho (1 + rho)
        = (1 + rho) + H (1 + 2 rho) + (H/u)(1 + H)  =: F,

so that

    m+(q, a) = log( 1 + F / (u rho (1 + rho)) ),                    (#)

and m+ > 0 iff F > 0 (PP's threshold H* = -(1+rho)/(1+2rho) is the
zero of the dominant part of F; the (H/u)(1+H) term is the exact
finite-u correction).

THE UNIFORM BOUND F >= 1. If H >= 0 then F >= 1 + rho >= 4/3.
If H < 0, use H >= -G1 (Lemma D), u >= 4, 1 + H <= 1 + 1.2e-21:

    F >= (1 + rho) - G1 (1 + 2 rho) - (G1/4)(1 + 1.2e-21)
       = (1 - G1) + rho (1 - 2 G1) - 0.0432251
      >= 0.8271 + (1/3)(0.6542) - 0.04323          [rho >= 1/3,
                                                    1 - 2 G1 > 0]
       = 1.0019417 >= 1.0019.

(The minimum of the bound is at q = 3; the witness gates F >= 1.0019
at every census point, SS3.)

CONCLUSION. By (#) with F >= 1: m+ >= log(1 + e^{-a}/(rho(1+rho))).
Since rho(1+rho) < 2, also m+ >= log(1 + y) with y := e^{-a}/2 <= 1/8
(u >= 4), and log(1+y) >= y/(1+y) >= (8/9) y = (4/9) e^{-a} > 0.
At entry e^{-a} = 1/(q+1):
m+ >= (4/9)/(q+1) >= 1/(3q) for q >= 3 (12q >= 9q + 9). The refined
floor is (#) with the per-q bound F >= F_q (same chain, G((q+1)/q)
in place of G1, u >= q+1 in the third term). QED

Proof of Corollary SS.2c. At entry, u = q+1, x = u/q = (q+1)/q.
Lower: by (#), q m+ >= q log(1 + F_q/((q+1) rho (1+rho))) and
log(1+z) >= z - z^2/2: q m+ >= [q/(q+1)] F_q/(rho(1+rho)) - O(1/q).
Upper: log(1+z) <= z and Lemma D's upper bound H <= -G(x)(1 -
1.0004 pi^2/q^2) + G(q+1)/2 (Proposition SS.5; H < 0 here makes
(H/u)(1+H) < 0, droppable) give q m+ <= [q/(q+1)] Fup_q/(rho(1+rho)),
Fup_q := (1+rho) - G(x)(1 - 1.0004 pi^2/q^2)(1+2rho) + tiny. As
q -> oo: rho -> 1, rho(1+rho) -> 2, G((q+1)/q) -> G(1) (continuity:
0 <= G(1) - G(x) <= G(1) - G(1 + 1/q) -> 0 by monotone continuity of
the defining series), so both sandwich sides converge to
(2 - 3 G(1))/2 = 1 - (3/2) G(1) = 1 - 6 T(1) = 0.740696... QED

(PP's measured entry floors: q = 121: 6.25e-3 vs refined floor
log(1 + F_121/238.0) = 6.245e-3 - the floor is SHARP to O(q^{-2})
relative; gated SS4.)

## 7. Proof of Theorem SS.3

Keep the notation of sec 6; Hhat = G(e^a/q), |H| <= Hhat <= G1.
From the definition of F:

    | F/(1+rho) - 1 | <= Hhat (1+2rho)/(1+rho)
                         + Hhat (1 + Hhat)/(u (1+rho))
                      <= Hhat (3/2 + 1.1729/(4 * 4/3)) <= 1.72 Hhat,

using (1+2rho)/(1+rho) < 3/2 (increasing in rho, rho < 1), u >= 4,
1 + rho >= 4/3. Let z := F/(u rho (1+rho)) > 0; then
u rho z = F/(1+rho) in [1 - 1.72 Hhat, 1 + 1.72 Hhat] and
z <= (1 + 1.72 G1)/(u rho). From z - z^2/2 <= log(1+z) <= z:

    e^a rho m+ = u rho log(1+z) in
        [ F/(1+rho) - (F/(1+rho)) z/2 ,  F/(1+rho) ],

and (F/(1+rho)) z/2 <= (1 + 1.72 G1)^2 / (2 u rho) <= 0.842 e^{-a}/rho
((1 + 1.72 * 0.1729)^2 / 2 = 0.8416 < 0.842). Combine:

    | e^a rho_q m+(q, a) - 1 | <= 1.72 G(e^a/q) + 0.842 e^{-a}/rho_q. QED

(Witnessed SS5 at q in {3,4,5,9,25,121} x admissible a-grid including
entry, where the bound is loosest but still certified; the measured
tightest point is deep, q = 121 at a = 8: deviation -1.7051e-4 vs
bound 2.8721e-4.)

## 8. Proof of Theorem SS.4; the surplus register (feeds doc 36 S3)

(i) Upper bound: by (#) and log(1+z) <= z,
m+ <= F/(u rho (1+rho)) <= (1 + 1.72 Hhat)/(u rho) <= 1.298 e^{-a}/rho
(1 + 1.72 * 0.1729 = 1.29739 < 1.298). With Theorem SS.2's lower
bound, 0 < m+ <= 1.298 e^{-a}/rho_q; the sup and limit statements
follow from Theorem SS.3 since G(e^a/q) -> 0 (Gaussian) and
e^{-a} -> 0.

(ii) At entry m+ <= 1.298/(rho_q (q+1)) <= 3.894/(q+1) -> 0 along
q -> oo; combined with (i) the infimum over the admissible family is
0 and is not attained.

(iii) Suppose m+(q, a) >= (1+beta) e^{-a}/rho for all a >= A. By (#)
and log(1+z) <= z: F/(1+rho) >= (1+beta) for all u >= e^A, i.e.
H (1+2rho)/(1+rho) + (H/u)(1+H)/(1+rho) >= beta, and since the second
term is O(1/u): liminf H_q(u) >= beta (1+rho)/(1+2rho) > 0. But
|H_q(u)| <= G(u/q) -> 0 (Lemma D). Contradiction. Reading: a
persistent H-floor IS a continuum term beta'/u in D_q(u) - rho_q,
i.e. a hole coefficient c_hole = beta' > 0; Theorem SS.1 makes
c_hole = 0 an identity. QED

THE SURPLUS REGISTER (what additional structure a surplus would
require; Castelnuovo risk input for doc 36 S3). On this face, at this
calibration, slack is structurally impossible; a positivity argument
needing UNIFORM slack must obtain it from one of exactly three moves:

```text
R-i   a POSITIVE hole: an inhomogeneous FE with a positive stripped
      unit (D_q gaining +beta/u). The only inhomogeneity carrier the
      honest object owns is the entry band B_q (PP sec 1.5), and the
      band enters with the NEGATIVE (deficit) sign - the truncated
      face (doc 36 S2) can only lower margins, not add slack.
R-ii  chi recalibration: shrinking chi+ = a + log(rho(1+rho)) by
      eta > 0 manufactures e^0-level slack by fiat; it breaks the
      LL6/NN comparability that made PP's kill-evasion
      apples-to-apples. Forbidden without a new forced dictionary.
R-iii AGGREGATION: the per-cell margins are summable against the cell
      weights: sum over admissible q <= e^a - 1 of log p(q) m+(q, a)
      has each term ~ log p(q) e^{-a}/rho_q while the admissible count
      grows like e^a - the assembled margin is Theta(1) iff
      sum_{q <= x, q = p^j >= 3} log p ~ x, which is Chebyshev/
      PNT-grade (EXTERNAL to this memo; PP's S3 series is its record;
      flagged, no decision weight). The index content, if any, lives
      in the 2D weight x scale assembly - per-cell slack is zero and
      PROVED zero.
```

This is the precise sense of doc 36's registered risk "deep-margin
marginality": the ku face's per-cell inequality is true, explicit,
and asymptotically TIGHT at both ends (deep a, large q); any
Castelnuovo-type posing must consume the assembly, not the cells.

## 9. PRE-REGISTERED GATES (written before the first run)

Evaluation rules: flint arb prec 300; gate inequalities certified only
when the arb ball resolves them (lower bound of the difference > 0);
exact integers for SS6; series truncated at term < 1e-95 with monotone
tails. CENSUS_Q and a-grids verbatim PP KU4.

```text
SS1 PROOF CONSTANTS: e^pi > 23.1406; 1/(1 - e^{-3pi}) < 1.0001;
    T(1) < 0.0432185; G(1) < 0.1729; G(4)/2 < 1.2e-21;
    sum k^2 e^{-pi k^2 x^2} <= 1.0004 e^{-pi x^2} at x in {1, 2};
    tail lemma T(x) <= 1.0001 e^{-pi x^2} at x in {1, 1.3, 2, 4};
    the F chain: (1 + 1/3) - G1 (5/3) - (G1/4)(1 + 1.2e-21) >= 1.0019.
    FAIL: any clause.
SS2 LEMMA D: master identity two routes to 1e-70 (q in {9, 121},
    x in {0.5, 1, 1.5, 3}); two-sided bound -G(u/q) <= H_q(u) <=
    G(u)/2 arb-certified at q in {3,4,5,9,25,121,169} x
    u/q in {(q+1)/q, 1.5, 2, 4, 8}; G strictly decreasing on the grid
    {1, 1.25, 1.5, 2, 3, 5, 10}; Prop SS.5 bound
    |H_q(qx) + G(x)| <= 1.0004 (pi^2/q^2) G(x) + G(qx)/2 at
    q in {9, 121}, x in {1, 1.5, 3}. FAIL: any clause.
SS3 THEOREM SS.2 ON THE CENSUS: at every PP census point (24 prime
    powers, entry-to-deep grids, n = 527): the algebra (#)
    |m+ - log(1 + F/(u rho (1+rho)))| < 1e-60; F >= 1.0019;
    m+ >= log(1 + e^{-a}/(rho(1+rho))); m+ >= (4/9) e^{-a}.
    All arb-resolved. FAIL: any point.
SS4 ENTRY FLOORS: m+(q, log(q+1)) >= 1/(3q) AND the refined per-q
    floor (#, F_q) for all census q; RECORD q * m+ at entry vs the
    limit 1 - (3/2) G(1) = 0.740696. FAIL: either floor at any q.
SS5 DEEP LAW: |e^a rho m+ - 1| <= 1.72 G(e^a/q) + 0.842 e^{-a}/rho
    arb-certified at q in {3,4,5,9,25,121} x a in {entry, entry+0.5,
    entry+1, 3, 5, 8 : a >= entry}. FAIL: any point.
SS6 CARRIER (Lemma A, exact): for all q in 3..300:
    {w in [0,q) : q | w(w+1)} == {0, q-1} iff q is a prime power;
    for each non-prime-power a CRT witness w printed (first few).
    FAIL: any q.
SS7 FE TWO ROUTES (Theorem SS.1): direct comb sum vs e^a D_q(e^a),
    q in {3, 5, 9, 121}, a in {0.7, 2.0} (+ q=3, a=5), rel < 1e-40.
    FAIL: any point.
SS8 EVASION (Theorem SS.4): m+ <= 1.298 e^{-a}/rho at every census
    point, arb-resolved; RECORD e^a rho m+ at a = 8 for
    q in {3,4,5,9,25} (the zero-slack limit). FAIL: any point.
```

No zeros, no freeze (nothing zero-side is computed; F-a holds
vacuously).

---- verdict section written after the runs ----

## 10. VERDICT: ALL GATES PASS - THE THREE TASKS CLOSE WITH NO NAMED GAP

Witness ALL PASS (SS1-SS8, exit 0, FIRST RUN UNTOUCHED - no gate, no
constant, no code amended after the first run; deterministic across
3 runs, byte-identical output; < 0.1 s at arb prec 600).

```text
SS1  constants: e^pi = 23.140693 > 23.1406; T(1) = 0.043217406 <
     0.0432185; G(1) = 0.172869622 < 0.1729; F-chain lower bound
     1.0019417 >= 1.0019; 1 - (3/2)G(1) = 0.740696.  PASS
SS2  master identity two routes: worst |diff| = 3.8e-178 (gate 1e-70)
     at all 8 points; two-sided H bound resolved at all 35 grid
     points; G strictly decreasing on the grid; Prop SS.5 curvature
     bound certified (q=121, x=1: H+G = 1.1653e-4 <= 1.1658e-4 -
     the bound is sharp to 4e-4 relative, as the sin^2 expansion
     predicts).  PASS
SS3  527/527 census points: algebra (#) two routes worst |diff| =
     1.7e-179 (gate 1e-60); min actual F = 1.32375 (q=3 at entry)
     >= 1.0019 (the proved uniform bound); both floors
     (log(1 + e^-a/(rho(1+rho))) and (4/9)e^-a) arb-certified at
     every point.  PASS
SS4  1/(3q) floor and refined per-q floor certified at all 24 q.
     Refined floor vs measured at entry: q=3: 0.54721 vs 0.55653;
     q=9: 0.10519 vs 0.10709; q=121: 6.2467e-3 vs 6.2490e-3 (sharp
     to 3.7e-4 relative - the predicted O(q^-2)).  q*m+(entry) =
     1.6696 (q=3), 0.9638 (9), 0.8175 (25), 0.7561 (121), 0.7517
     (169): monotone approach to the limit 0.740696 from above.  PASS
SS5  deep law certified at all 34 (q, a) points; tightest: q=121 at
     a=8 (deviation -1.7051e-4 vs bound 2.8721e-4, slack 1.7x -
     exactly the comfortable-not-sharp factor of sec 12).  PASS
SS6  Lemma A iff: exact at all q in 3..300; first CRT witnesses
     q=6: w=2; q=10: w=4; q=12: w=3.  PASS
SS7  FE two routes: worst rel = 3.2e-178 (gate 1e-40; PP's KU1
     5.0e-88 strengthened at the higher precision).  PASS
SS8  evasion ceiling 1.298 e^-a/rho certified at 527/527;
     e^8 rho m+(q,8) = 0.99950 (q=3), 0.99966 (4), 0.99972 (5),
     0.99978 (9), 0.99982 (25): the zero-slack limit, ordered in
     rho exactly as the 0.842 e^{-a}/rho second-order term
     predicts.  PASS
```

## 11. G-INT6 ledger

```text
input                          choices spent
two-coset comb S_q             forced (= Lee's cell comb C_q by
                               Lemma A, an iff; the lattice
                               completion remains PP's logged choice,
                               inherited, not re-spent here)
coset Poisson (Lemma B)        0 new (banked device, here proved
                               self-contained by calculus; no contour,
                               no FE input)
margin/chi calibration         LL6/NN verbatim (inherited from PP;
                               comparability, not tuning)
proof constants G1 = 0.1729,   derived in Lemmas C/D and gated SS1;
1.72 / 0.842 / 1.298 / 4/9 /   none fitted
1/(3q) / 1.0019
witness grids                  calibration; census grid verbatim PP
                               KU4 (no new ranges)
zeros                          NONE consumed (no fork_lib import,
                               no freeze needed)
```

Carrier guard summary: "q is a prime power" is consumed at exactly one
point, Lemma A (comb = two cosets), and the guard is an iff with a CRT
counterexample at every composite non-prime-power modulus; on DH /
Epstein the cell address itself is unformable (PP KU8 standing). The
weight log p(q) is consumed only in the R-iii assembly remark, which
is record-only.

## 12. Honest limits

- The theorems are about PP's LATTICE-COMPLETED margin object m+ at
  the LL6/NN calibration. The lattice completion stays a logged
  dictionary choice (PP sec 6); the truncated/honest face is doc 36
  S2, untouched here except that R-i notes its band carries the
  deficit sign.
- Per-cell statements only. The 2D weight x scale posing (doc 36 S3)
  is not posed; the R-iii aggregation remark uses Chebyshev-grade
  growth of sum log p(q) as an EXTERNAL flag, record only.
- Lemma B is Poisson summation (for Gaussians on cosets) - one rung
  above KK's no-Poisson toolkit, unavoidable: the FE under test IS a
  Poisson statement. Everything else is KK-grade (geometric series,
  calculus, one differentiation under the integral).
- Corollary SS.2c's limit is proved with a two-sided sandwich whose
  rate is not optimized (O(1/q) suffices and is not sharpened).
- The deep-law constant pair (1.72, 0.842) is comfortable, not sharp
  (true second-order coefficient is 1/2 vs 0.842; measured slack
  ~1.7x).
- Nothing here touches extension problems, the true ku-square
  diagonal, spectrum-level duality, or any zero-side statement
  (I-doc sec 7 walls unmoved).

## 13. Hand-off

```text
S1 STATUS:  COMPLETE - no named gap. PP's (P-a) census survival is
            now a theorem package:
            SS.1 homogeneous FE = identity (coset Poisson, elementary,
                 c_hole = 0 exact);
            SS.2 m+(q, a) > 0 for ALL prime powers q >= 3 and ALL
                 a >= log(q+1), floor (4/9)e^{-a}, entry floor 1/(3q),
                 refined floor sharp to O(q^{-2});
            SS.2c entry constant DERIVED: 0.74 = 1 - (3/2)G(1);
            SS.3 deep law m+ = e^{-a}/rho_q (1 + O(.)), O(.) explicit
                 from entry on;
            SS.4 evasion-not-surplus: zero slack at infinity, no
                 uniform floor, surplus = positive hole coefficient =
                 contradiction with SS.1;
            SS.5 repayment law exact identity + O(q^{-2}) error.
MIDDLE      There is none: |H| <= G(e^a/q) <= G(1) < 0.1729 < 2/3 <=
RANGE:      |H*| covers entry-to-deep in one monotone bound; the
            "bridge" PP flagged as unproved is Lemma D + Lemma C(ii).
CARRIER:    prime power consumed ONCE (Lemma A, an iff, CRT-killed on
            composites); guard gated exactly (SS6, q <= 300).
S3 FEED:    the surplus register (sec 8): R-i positive hole (forbidden
            by SS.1), R-ii recalibration (forbidden by comparability),
            R-iii assembly (the only live route; Theta(1) aggregate,
            PNT-grade, where the Castelnuovo posing must live).
WITNESS:    prime_ss_ku_inequality_proof.py, SS1-SS8 ALL PASS, exit 0,
            no zeros consumed. Inherited rerun:
            prime_pp_ku_face_index ALL PASS exit 0 (freeze hash
            matches PP's record).
```
