# 00 - Reduction: nested Prime-Toeplitz domination implies RH

Status: provenance recorded; reduction stated; proof obligations O1-O4 are classical technology
(Weil's converse, adapted to the pole-killed even model) but are NOT yet written rigorously.
This document exists because the reduction was previously asserted across G/H and the proof
scaffold without ever being stated as a lemma with obligations.

Noncircularity note: this document uses zero-side reasoning. That is legitimate here and only
here, because this document proves `program target => RH`, not the target itself. The rules of
engagement in `README.md` (no zero-side input) apply to proving the target, not to certifying
its sufficiency.

## 1. Provenance

The pole-killed/Sonin framing is not original to this project. It comes from:

```text
Connes-Consani, "Weil positivity and trace formula, the archimedean place",
arXiv:2006.13771 (CC20).
```

(cited in `research/work/B-prime-reflection.md`; analyzed in `research/literature/the-fusion.md`
and `research/literature/connes-consani-scaling-site.md`).

What CC20 prove [THM]: the archimedean Weil functional is positive on the pole-killed
("H^1-conditions" `hat g(+-i/2)=0`) Sonin space for test functions with multiplicative support
in `(1/2, 2)` - i.e. exactly the prime-free window `|u| < log 2` in our log coordinate.
No primes are included. The scaling action does not preserve the Sonin space, so CC20 obtain a
positive projection, not a self-adjoint generator; that obstruction is why their result stops at
the archimedean place.

What this project adds on top of CC20's frame: the nested support filtration `H_L subset H_R`,
the exact Euler atoms as Toeplitz correlations, and the Schur-complement extension target. The
program, stated in one line:

```text
extend CC20's archimedean Sonin positivity past support log 2,
paying for each support extension with the exact Euler atoms,
one Schur shell at a time.
```

This gives the proof track a published, unconditional base anchor (see section 5) and makes the
induction step the only open mathematics.

## 2. The reduction statement

```text
Theorem (Reduction; obligations O1-O4 below).
Suppose for every R > 0 the form

  M_R = A_infty - P_R

satisfies M_R(h,h) >= 0 for every h in the smooth core of H_R:

  h even, real, C_c^infty, supp(h) subset [-R/2, R/2],
  hat h(0) = hat h(i/2) = 0.

Then every nontrivial zero of zeta has Re(rho) = 1/2.
```

Conventions are those of `01-sonin-schur-scaffold.md`. Note the hypothesis is positivity of the
*arithmetic* side; the zeros enter only through the explicit formula.

## 3. Why the hypothesis equals the zero-side sum (O1, O2)

For real even `h`, the positive-type test is `g = h * h# = h * h`, so `hat g = (hat h)^2`.
The Weil explicit formula for such `g` reads (project normalization):

```text
sum_rho hat g((rho - 1/2)/i)
  = hat g(i/2) + hat g(-i/2)
    - sum_n Lambda(n) n^{-1/2} (g(log n) + g(-log n))
    + A_infty(h,h).
```

**O2 (pole killing, trivial).** `hat g(+-i/2) = hat h(+-i/2)^2 = 0` on the pole-killed space
(evenness gives `hat h(-i/2) = hat h(i/2)`).

**O1 (normalization audit, mechanical).** Verify that the archimedean term of the explicit
formula in this normalization is exactly the `A_infty` of `01-sonin-schur-scaffold.md`
(`-log pi <h,h> + (1/2pi) int |hat h|^2 Re psi(1/4 + it/2) dt`), and that the prime term equals
`P_R(h,h)` exactly when `supp(h) subset [-R/2,R/2]` (then `g` is supported in `[-R,R]` and atoms
with `log n >= R` vanish - Lemma 1.3). The witness scripts already pin these constants
numerically; O1 is a paper check against Weil/Bombieri.

Granting O1-O2, for admissible `h`:

```text
Z(h) := sum_rho hat h((rho-1/2)/i)^2 = M_R(h,h).
```

So the program hypothesis is: `Z(h) >= 0` for all pole-killed even real compactly supported `h`.

## 4. Detection of an off-line zero (O3 - the actual converse)

Suppose `rho_0 = beta + i gamma_0` with `sigma := beta - 1/2 > 0`. The zero quadruple
`{rho_0, conj(rho_0), 1-rho_0, 1-conj(rho_0)}` maps to the `z`-points `{z_0, -z_0, conj(z_0),
-conj(z_0)}` with `z_0 = gamma_0 - i sigma`. For real even `h` the quadruple contributes

```text
4 Re[ hat h(z_0)^2 ]
```

to `Z(h)` (evenness pairs `+-z_0`; reality pairs `z_0, conj(z_0)`).

**The phase point (where a naive bump fails).** For `h(u) = w(u) cos(gamma_0 u)` with `w >= 0`
even, `hat h(z_0) ~ (1/2) hat w(-i sigma) > 0` is positive real, so the quadruple contributes
*positively*. Detection requires rotating the phase of `hat h(z_0)` to near `i`. An even real
`h` can do this:

```text
h(u) = w(u) cos(gamma_0 u) + v(u) sin(gamma_0 u),
w even, v odd  (then h is even),
hat h(z_0) ~ (1/2) [ W + i V ],
W = int w(u) e^{sigma u} du-type term, V = the v-analogue.
```

Choosing `V` dominant makes `Re[hat h(z_0)^2] ~ -V^2/4 < 0`.

**The size race.** On support `[-T/2, T/2]`:

```text
off-line quadruple:  |hat h(z_0)|^2 ~ e^{sigma T} (exponential in T);
on-line zeros:       each term hat h(t)^2 >= 0, total polynomial in T
                     (frequency localization near +-gamma_0, zero density log gamma_0);
other off-line zeros: only those with ordinate near gamma_0 survive localization;
                     take the one with maximal local beta as the dominant term.
```

Exponential beats polynomial, so `Z(h_T) < 0` for large `T` - contradicting the hypothesis.

**The constraint design (important).** The two pole-killing constraints must be imposed *inside
the concentrated family*, not by an external corrector: an external corrector `c phi` needs
`c ~ hat h_T(i/2)`, which can be as large as `e^{T/4}`, and its own `Z`-cost `~ e^{T/2}` would
beat the main term whenever `sigma < 1/2`. Instead take a >= 3-dimensional concentrated family
(e.g. three windows `w_1, w_2, w_3` at the same scale), impose the two homogeneous conditions
`hat h(0) = hat h(i/2) = 0` within it, and check the `z_0`-amplitude functional remains
nondegenerate on the solution ray. Three dimensions, two constraints, one direction survives
with full `e^{sigma T}` growth.

**O3 obligations, itemized:**

```text
O3a. The even real two-component modulation achieves arg hat h(z_0) ~ pi/2
     with |hat h(z_0)| ~ e^{sigma T/2}. (Computation: the quadruple contributes
     (aW)^2 - (b V)^2 with W, V the symmetric/antisymmetric window amplitudes
     at -i sigma; choose b dominant.)
O3b. On-line sum bound: sum over on-line zeros of hat h(t)^2 = O(T^k) for the
     localized family (uses unconditional zero-counting N(T) only).
O3c. Off-line interference - THE SUBTLE STEP. Frequency localization suppresses
     zeros at other ordinates only POLYNOMIALLY ((T|gamma'-gamma_0|)^{-2k}),
     while a zero elsewhere with strictly larger sigma' > sigma_0 grows
     e^{(sigma'-sigma_0)T} faster - and an uncontrolled POSITIVE contribution
     can swamp the engineered negative term. The selection must therefore take
     sigma_0 within delta of sup_rho sigma_rho (the sup need not be attained;
     work with a near-maximal zero), shrink the frequency window below the
     distance to other near-maximal-sigma zeros, and absorb the remaining
     same-level terms. If the sup is approached only along a sequence of
     heights, a compactness/diagonal argument over (delta, T) is required.
     This is where the classical proofs (Weil's converse; Bombieri's lectures)
     do real work - DO NOT treat O3 as routine until this case is written.
O3d. In-family constraint satisfaction with surviving z_0-amplitude
     (>=3-dimensional concentrated family; external correctors fail for
     beta < 3/4 because their Z-cost ~ e^{T/2} beats the signal).
```

## 5. Base case anchor (O4) and what the induction needs

**O4 (base case) - AUDITED 2026-06-09 against the paper.** CC20 Theorem 1 (ar5iv text
of arXiv:2006.13771): for `g in C_c^infty(R_+^*)` with support in `[2^{-1/2}, 2^{1/2}]`
and `hat g(i/2) = 0`,

```text
W_infty(g * g^*) >= Tr(theta(g) S theta(g)^*) - c |hat g(0)|^2,   13 < c < 17,
```

so with both kills (`hat g(0) = hat g(i/2) = 0`, our `ell_0, ell_1`) the form is
`>= Tr(...) >= 0`. Audit results:

```text
- support match: their single-factor support [2^{-1/2}, 2^{1/2}] is |u| <= (log 2)/2
  in our log coordinate, i.e. exactly our H_L for L <= log 2 - the prime-free window;
  the base case of the filtration is PRECISELY their theorem (in fact with a
  quantitative lower bound, not just >= 0);
- kills match: hat g(i/2) = 0 required; hat g(0) = 0 for the clean form (otherwise
  the explicit -c|hat g(0)|^2 correction, 13 < c < 17);
- model match: even L^2 functions via their isomorphism w; their Delta^{-1/2}
  unitarization shift corresponds to our n^{-1/2} / e^{U/2} critical weights;
  O1's numeric explicit-formula verification (4.4e-13) pins the remaining
  normalization equivalence;
- NAMING DRIFT (record): CC20's "Sonin space" = even L^2 functions vanishing,
  together with their Fourier transform, on [-1,1] - the double-vanishing space
  behind their lower-bound projection S. The project's H_L (pole-killed support
  windows) are a DIFFERENT object that this repo has been calling "Sonin" loosely.
  Keep the name for H_L but do not import CC20 statements about their S verbatim;
- consistency: our margin-law witness has W_inf alone positive at gmax = 1.30
  (+0.58) through ~2.2, dying at ~2.3 - consistent with (and numerically extending)
  their theorem, which stops at convolution support log 2.
```

Remaining formality: a line-by-line transcription of their `W_infty = -W_R(Delta^{-1/2}.)`
convention onto the `A_infty` digamma form (O1's numeric check makes failure here
implausible).

**Strictness note (not part of the reduction, but recorded here).** The Schur induction uses
`A = M_L > 0` (invertibility), while the reduction only needs `>= 0`. On finite-dimensional
compressions strictness is generic and is what the witnesses observe; the continuum induction
(T4) must either carry a quantitative lower bound for `eigmin(A)` along the filtration or work
with the Schur form `D - C* A^{-1} C` on `ran(A)`. This is an honest open bookkeeping item, and
the observed decay of `eigmin(A)` with `R` (cond(A_+) ~ 1e3 already at R ~ 3.2) is one of the
scaling risks tracked in `TODO.md`.

## 6. Status summary

```text
O1  normalization audit                 discharged numerically 2026-06-09:
                                        semilocal_2.verify_explicit_formula reproduces
                                        the two-sided explicit formula against 2000
                                        actual zeros, residual 4.4e-13 (Gaussian test);
                                        paper transcription remains a formality
O2  pole-term vanishing                 done (trivial)
O3  off-line detection                  WRITTEN in 00a-detection-lemma.md:
                                        O3a/O3b/O3d discharged (the p(D)G polynomial-
                                        prefactor device dissolves the constraint
                                        problem entirely); O3c done for attained
                                        supremum; unattained case reduced to one
                                        precise averaging sub-lemma (00a section 6)
O4  base case = CC20 archimedean        AUDITED 2026-06-09 (section 5): support, kills,
                                        and model all match; base case = CC20 Thm 1
                                        verbatim with a quantitative lower bound.
                                        Naming drift recorded (their Sonin space is
                                        not our H_L). Line-by-line normalization
                                        transcription remains a formality (O1 pins it).
                                        BOUNDED: W_inf alone goes indefinite at
                                        gmax ~ 2.3 (prime_margin_law.py) - the anchor
                                        is genuinely small-support; the induction
                                        requires primes immediately past the window.
```

None of O1-O4 is believed to be research-hard. Until they are written, the program's claim
"target => RH" is provenance-backed (CC20 + Weil's converse) but not certified. This document
is the fail-closed record of exactly what remains.
