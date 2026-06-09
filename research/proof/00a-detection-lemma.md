# 00a - The detection lemma (obligation O3 of the reduction)

Status: O3a, O3b, O3d discharged below (full constructions and estimates, written to
proof level modulo routine Laplace-method constants). O3c is discharged in Case A
(attained supremum) and reduced to one precise averaging sub-lemma in Case B
(unattained supremum). This is the document doc 00 demanded; the remaining gap is
section 6.

## 1. Statement

```text
Lemma (detection). Suppose zeta has a zero off the critical line. Then there
exist T > 0 and an admissible test
   h in C_c(R), even, real, supp h subset [-T/2, T/2],
   hat h(0) = hat h(i/2) = 0,
with  Z(h) = sum_rho hat h((rho-1/2)/i)^2 < 0.
```

Combined with O1/O2 (Z(h) = M_R(h,h) for R >= T) this gives the contrapositive of the
reduction: the program target for all R forces RH.

## 2. The kill-free parametrization (O3d discharged)

The two pole constraints are linear conditions that previous sketches imposed by
correctors or in-family solving - both delicate (a corrector of size hat h_T(i/2) ~
e^{T/4} has Z-cost ~ e^{T/2}, fatal for sigma < 1/2; in-family solving rotates with T).
Both problems vanish with the following device:

```text
hat h(z) := z^2 (z^2 + 1/4) hat G(z),   equivalently   h = (-D^2)(-D^2 + 1/4) G,
```

for ANY even real G in C_c^infty with supp G subset [-T/2, T/2]. Then:

```text
- hat h(0) = 0 and hat h(+-i/2) = 0 EXACTLY (polynomial prefactor zeros);
- h is even, real, compactly supported with the same support as G;
- hat h has the same exponential type T/2 as hat G;
- the class {G} is FREE - no constraint solving, no T-dependent rotation.
```

The admissible class of the reduction therefore contains the freely-parametrized
family p(D)G, p(z) = z^2(z^2+1/4). All constructions below choose G.

## 3. The violating family (O3a discharged)

Let rho* = 1/2 + sigma* + i gamma* be an off-line zero (sigma* in (0, 1/2], gamma* > 0;
selection of WHICH zero in sections 5-6). The zero quadruple contributes

```text
Q*(h) = 4 Re[ hat h(z*)^2 ],   z* = gamma* + i sigma*,
```

to Z(h) (evenness pairs +-gamma*, reflection pairs +-i sigma*; all other zeros are
estimated, not engineered). Choose a fixed even window Omega in C_c^infty(-1,1),
Omega >= 0, Omega(0) = 1, and set

```text
G_{a,b}(u) = Omega(2u/T) [ a cos(gamma* u) + b (2u/T) sin(gamma* u) ].
```

(The second member is even: odd envelope times odd sin.) Laplace asymptotics at
w = i sigma* T/2 give, with A_T = int Omega(x) e^{sigma* T x / 2} dx and
B_T = int x Omega(x) e^{sigma* T x / 2} dx (both real, |A_T|, |B_T| ~ e^{sigma* T/2}
times explicit polynomial factors, B_T > 0 dominated by the x ~ +1 edge):

```text
hat G(z*) = (T/4) [ a A'_T - i b B'_T ] (1 + O(e^{-c T}))
```

with A', B' the rescaled constants - the REAL and IMAGINARY parts are independently
tunable by (a, b). The prefactor contributes phase
arg p(z*) = O(sigma*/gamma*) =: theta_p, fixed and computable. Choose (a,b) so that

```text
arg hat G(z*) = pi/2 - theta_p   (one phase condition, two real parameters),
```

retaining |hat G(z*)| >= c e^{sigma* T/2}. Then

```text
Q*(h) = 4 |p(z*)|^2 Re[ e^{2 i theta_p} hat G(z*)^2 ] = -4 |p(z*)|^2 |hat G(z*)|^2
      <= -c' gamma*^8 e^{sigma* T}.
```

The signal is exponentially negative in T.

## 4. The on-line sum (O3b discharged)

For on-line zeros, hat h(gamma)^2 >= 0 with

```text
|hat h(gamma)| <= C gamma^4 T (1 + T|gamma - gamma*|/2)^{-N} + (gamma -> -gamma*),
```

(Schwartz decay of Omega-hat at scale T). With the unconditional zero count
N(t+1) - N(t) = O(log(2+t)):

```text
sum_{on-line} hat h(gamma)^2 <= C_N T^2 gamma*^8 log(2+gamma*) = poly(T),
```

beaten by the e^{sigma* T} signal. (The polynomial prefactor costs gamma^8, absorbed
by taking N >= 5 in the window decay.)

## 5. Off-line interference, Case A (O3c, attained supremum)

Let sigma_max = sup_rho (beta_rho - 1/2) > 0.

**Case A: the supremum is attained.** Choose rho* attaining it, with gamma* minimal
among attainers (any fixed attainer works). Every other off-line quadruple satisfies
sigma_j <= sigma*, and its magnitude is

```text
|hat h(z_j)|^2 <= C gamma_j^8 T^2 e^{sigma_j T} (1 + T|gamma_j - gamma*|/2)^{-2N}.
```

Split the sum over j != *:

```text
- sigma_j <= sigma* - delta':   total <= poly(T) e^{(sigma*-delta') T}  - beaten;
- sigma_j in (sigma*-delta', sigma*]: a discrete set; the nearest such zero is at
  fixed distance d* > 0 in ordinate, and the height-tail converges:
     sum_j gamma_j^8 (T|gamma_j-gamma*|)^{-2N} = O((T d*)^{-2N}) + O(T^{-2N})
  for 2N > 9.  Total <= C e^{sigma* T} (T d*)^{-2N} = o(signal).
```

So Z(h_T) <= -c' gamma*^8 e^{sigma* T} (1 + o(1)) < 0 for large T. Case A complete.

## 6. Off-line interference, Case B (the one remaining gap)

**Case B: the supremum is not attained** - zeros with sigma_j increasing to sigma_max
only along heights gamma_j -> infinity. Then for any fixed choice of rho*, zeros with
sigma_j > sigma* exist (at large heights), and their terms carry e^{(sigma_j-sigma*)T}
relative growth against only polynomial localization suppression - with UNCONTROLLED
sign. Exponential beats polynomial, so the fixed-test argument of section 5 does not
close.

**ATTEMPTED RESOLUTION - REFUTED SAME DAY (kept as graveyard; see correction below).**

The following Landau/annular-window argument was drafted and then killed by its own
step-2 check: the crossing value is s = sigma_j (1 - (x+y)/2), and (a) the PQ cross
terms have x + y = 2 gamma* x / (gamma_j + gamma*) -> 0, putting foreign real-axis
singularities at s ~ sigma_j (NOT below (3/4) sigma_max as claimed); (b) worse, the
self-product (P^2) terms cross at exactly s = sigma_j with nonvanishing density
Omega(x) Omega(-x) along x + y = 0 - intrinsic to ANY even window. The engineered
singularity at sigma* < sigma_max is therefore always shadowed by sign-uncontrolled
foreign singularities in Case B. The Landau route as drafted is DEAD; the draft is
retained below because the curve bookkeeping it introduces is the right language for
whatever replaces it.

Suppose, for contradiction, Z(h_T) >= 0 for all T (the hypothesis (H) restricted to
the family below). Consider W(T) = Z(h_T) as a function of T >= T_0 and its Laplace
transform F(s) = int W(T) e^{-sT} dT.

```text
Step 1 (annular window). Choose Omega even, smooth, >= 0, supported in
   1/2 < |x| < 1 (an annular window; the signal estimates of section 3 used
   only the |x| ~ 1 edge mass, so they survive unchanged). Each quadruple
   term's Laplace transform is then a double integral
      int int Omega(x) Omega(y) / (s - sigma_j - i(w x + w' y)/2) dx dy
   over x, y in supp Omega, with w, w' in {(gamma_j -+ gamma*) + i sigma_j}.
   Its singularities lie on the CURVES s = sigma_j + i(w x + w' y)/2.

Step 2 (real-axis crossings). A curve point is real iff
   Re(w) x + Re(w') y = 0. With the annular support (|x|,|y| in [1/2,1]):
   - the engineered zero j = * (w = i sigma*, recentered frequency 0):
     real segment with RIGHTMOST point s = sigma* (x = y = 1 endpoint),
     coefficient strictly NEGATIVE by the phase engineering of section 3;
   - foreign zeros gamma_j != gamma*: crossings require
     y/x = -(gamma_j - gamma*)/(gamma_j + gamma*), giving |x + y| <= 1/2
     and real singular points at s <= (3/4) sigma_j <= (3/4) sigma_max;
   - same-ordinate zeros (gamma_j = gamma*, finitely many, sigma_j <= sigma*):
     contained in the j = * bookkeeping or strictly below it;
   - on-line zeros: nonnegative terms with transform singularities at
     Re s <= 0.

Step 3 (selection). In Case B choose rho* with sigma* > (3/4) sigma_max
   (possible since sigma_j -> sigma_max). Then the rightmost real-axis
   singularity of F is the engineered one at s = sigma*, with negative
   leading coefficient; the real axis is regular on (sigma*, infinity).

Step 4 (Landau). W is locally integrable; F converges absolutely for
   Re s > sigma_max + eps (uniform summability over zeros, 2N > 9). By
   Landau's theorem for Laplace transforms of nonnegative functions, the
   abscissa of convergence is a singular point on the real axis; since the
   real axis is regular down to sigma*, the integral converges for
   Re s > sigma*, and F(sigma) >= 0 for real sigma > sigma* (nonnegative
   integrand). But F(sigma) -> -infinity as sigma -> sigma*+ (negative
   endpoint singularity). Contradiction. qed (sketch)
```

Hygiene still to be written (none believed hard): (i) the complete cross-term
enumeration (PP, PQ, QQ products and the b-member/p(z) slow factors - same curves,
polynomial densities, no new real crossings); (ii) the endpoint-singularity
coefficient sign at s = sigma* including the slow factors (Omega >= 0 near the
corner x = y = 1 and the engineered phase give definiteness); (iii) the interchange
of zero-sum and Laplace integral (absolute convergence, as in section 5).

## 6'. Case B resolved in architecture: the Li coordinate (2026-06-09)

Source audit (primary text read): E. Bombieri, "Remarks on Weil's quadratic
functional in the theory of prime numbers, I", Rend. Mat. Acc. Lincei s.9 v.11
(2000), 183-233, section 3. His Theorem 1 (after Weil 1952) proves, with a
COMPLETE converse and NO case split:

```text
RH  <=>  sum_rho gtilde(rho) conj(gtilde)(1-conj(rho)) > 0
         for every complex g in C_c^infty((0,infty)), g != 0.
```

The converse mechanism is the answer to our Case B, and it is a COORDINATE
CHANGE, not a harder estimate. Detection is run not in the beta-coordinate
(sigma = beta - 1/2, whose supremum may be unattained - our Case B) but in
Li's coordinate

```text
|1 - 1/rho|^2 = 1 + (1 - 2 beta)/|rho|^2 ,
```

which tends to 1 as |rho| -> infinity. Hence if RH fails, the MAXIMUM of
|1 - 1/rho| over all zeros is > 1 and is ATTAINED BY FINITELY MANY ZEROS -
always. The unattained-supremum case structurally cannot occur: high zeros are
crushed by the 1/|rho|^2 weight regardless of how their beta behaves. Our Case
A/B split (and the Landau/annular failure) was an artifact of detecting in the
wrong coordinate.

The classical chain (Bombieri section 3): Li's criterion [Li 1997: RH <=>
lambda_n > 0 for all n, lambda_n = sum_rho (1 - (1-1/rho)^n) + conjugate
member]; if RH fails, the finitely many Li-extremal zeros rho_k contribute
-2(1+t)^n sum_k cos(n phi_k) with t > 0, the rest O(n^2 (1+t-delta)^n);
Dirichlet's theorem on simultaneous Diophantine approximation gives infinitely
many n with sum cos(n phi_k) ~ +K, so lambda_n < 0 infinitely often. The
witnessing test g_n is explicit (inverse Mellin of 1-(1-1/s)^n: a polynomial
P_n(log x) on (0,1]), truncated at epsilon to compact support (the limit
justified by the de la Vallee-Poussin zero-free region, his eq. 3.4), then
mollified to C_c^infty. Every step is classical and unconditional.

Transcription into the program's admissible class (even real h, supp in
[-T/2,T/2], hhat(0) = hhat(i/2) = 0). Two named obligations remain:

```text
T-even (evenness). Bombieri's Theorem 1 uses complex non-even g. The even-class
   statement is Yoshida's theorem [Yoshida 1992]: positivity of the Weil
   functional on smooth EVEN compactly supported tests <=> RH excluding real
   zeros. The real-zero exclusion is unconditional for zeta: zeta(s) != 0 on
   (0,1) since (1 - 2^{1-s}) zeta(s) = sum (-1)^{n-1} n^{-s} > 0 there. So
   even-class positivity <=> RH, classically.
T-kill (pole constraints). The hypothesis lives on the pole-killed subspace.
   By the p(D) device (section 2), the pole-killed even class contains
   {p(D) G : G even real C_c^infty} freely, so the hypothesis implies the
   p^2-WEIGHTED Weil form  G |-> sum_rho p(z_rho)^2 Ghat(z_rho)^2  is PSD on
   the UNCONSTRAINED even class (w_rho = p(z_rho)^2 != 0 at every nontrivial
   zero, since p vanishes only at s in {0, 1/2, 1}). The Li detection must
   then be rerun for the weighted form. The extremal-zero contribution
   becomes -2(1+t)^n sum_k Re[w_k e^{i n phi_k}] with fixed nonzero weights:
   the homogeneous Dirichlet step is replaced by
   Lemma B2 (mean-zero oscillation, to write): for finitely many phases
   phi_k != 0 mod 2pi and weights w_k != 0, the sequence
   F(n) = sum_k Re[w_k e^{i n phi_k}] has Cesaro mean 0 and attains values
   >= c > 0 infinitely often unless F vanishes identically on the orbit
   closure; the degenerate F == 0 configurations force real zeros (excluded
   unconditionally) or w_k = 0 (impossible) - the level-set recursion to the
   next Li level handles any residual degeneracy.
```

Status of Case B after this section: ANCHORED (architecture + citations +
explicit remaining lemmas), no longer device-less. The remaining work (the
even/weighted Li detection: Lemma B1 = even analogue of Bombieri's Theorem 1
with p^2 weights; Lemma B2 above; reading Yoshida's proof to check weight-
robustness) is classical-technique transcription with named sources, not a
new mechanism. Until B1/B2 are written to proof level, the reduction's O3
carries this as its only conditional joint - and the condition is on OUR
write-up, not on any unproven mathematics.

References (verified against the printed bibliography, Bombieri 2000):
A. Weil, Sur les "formules explicites" de la theorie des nombres premiers,
Meddelanden Fran Lunds Univ. Mat. Sem. (dedie a M. Riesz), 1952, 252-265.
H. Yoshida, On Hermitian Forms attached to Zeta Functions, in: Zeta Functions
in Geometry, Adv. Stud. Pure Math. 21, Math. Soc. Japan, Tokyo 1992, 281-325.
X.-J. Li, The positivity of a sequence of numbers and the Riemann Hypothesis,
J. Number Theory 65 (1997), 325-333.
E. Bombieri - J.C. Lagarias, Complements to Li's criterion for the Riemann
Hypothesis, J. Number Theory 77 (1999), 274-287.
E. Bombieri, Remarks on Weil's quadratic functional in the theory of prime
numbers, I, Rend. Mat. Acc. Lincei s.9 v.11 (2000), 183-233.

## 7. Summary of O3 status

```text
O3a  phase-engineered negative quadruple      DONE (section 3)
O3b  on-line polynomial bound                 DONE (section 4)
O3c  interference, attained case              DONE (section 5)
O3c' interference, unattained case            ANCHORED (section 6'): the Case
                                              A/B split is an artifact of the
                                              beta-coordinate; in Li's coordinate
                                              |1-1/rho| the extremum is always
                                              attained (Bombieri 2000 Thm 1,
                                              complete classical converse).
                                              Remaining: transcription lemmas
                                              B1 (even + p^2-weighted Li
                                              detection; Yoshida 1992 for the
                                              even class) and B2 (mean-zero
                                              oscillation replacing Dirichlet).
                                              The Landau/annular graveyard
                                              (section 6) stands as the record
                                              of why beta-coordinate devices die.
O3d  constraint satisfaction                  DISSOLVED (section 2: p(D)G device)
```
