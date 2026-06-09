# 09 - Inverse analysis: what the candidate lemmas imply, and what survives

Status: R1a of the risk ladder. Three findings, one reformulation, one front target -
PROPOSED AND REFUTED THE SAME DAY (section 6'), which is the fail-closed method working.
Numerical companions: `scripts/numerics/witness/prime_ladder_scaling.py` (R1b),
`scripts/numerics/witness/prime_single_place_passivity.py` (refutation),
`scripts/numerics/witness/prime_interference_rigidity.py` (what replaced it).

## 1. The R1b ladder data (R pushed from 3.24 to 5.90)

Full ladder, ambient `n=46/hw=0.06`, T=300, atoms to `n=365`, 18 edges:

```text
- zeta positive on every nested window and every Schur extension through R=5.90;
- DH indefinite from the first prime-rich edge onward, on all 18 edges (control holds);
- eigmin(A) (the induction margin on the old window) decays ~ e^{-1.5 R} on 3<=R<=4.5,
  then plateaus ~ 9e-5 for R>=4.76 - CAUTION: the plateau scale is within ~2x of the
  estimated Fourier-truncation eigenvalue noise (T=300), so the plateau is not yet a fact;
- rho = ||A^{-1/2} C D^{-1/2}||^2 climbs 0.979 -> 0.999 and never crosses 1;
- chronological peak debt (smooth base vs exact cells) grows from ~0.2 at R~3.2 to ~17 at
  the 4.26->4.50 edge, while the final Schur margin is ~3e-3: the storage path is a
  cancellation of up to FOUR orders of magnitude between O(1)-to-O(10) quantities;
- repair concentration (top positive Schur jump / total positive jumps) is ~1.00 for
  R <= 4.26 and falls irregularly after (0.57 at R=5.26): single-atom repair is ending
  exactly where cells start to crowd.
```

## 2. Finding 1 - margins are exponentially small: no slack-bearing estimate can close

The induction margin `eigmin(A)` decays like `e^{-cR}`, `c ~ 1.5`, while the chronological
debt/repair terms it must referee are `O(1)`-to-`O(10)` and *growing*. Therefore:

```text
Any proof step of the form  |residual| <= (estimate with polynomial-in-R slack)
loses by an exponential factor. The certificate cannot be assembled from
magnitude estimates at ANY transport range. Every large term must cancel
EXACTLY (an identity), and only the exactly-cancelled remainder may be signed.
```

This is not a defect of the program; it is the precise local form of "Weil positivity is
knife-edge sharp." It has two constructive consequences:

```text
(a) the finite Riccati identity (05) is the right KIND of object: exact algebra
    first, positivity only at the end;
(b) the storage matrices Pi_j cannot be found by bounding - they must come from a
    structural realization (section 5).
```

## 3. Finding 2 - the cluster obstruction: per-cell repair is dead at large R

Candidate arithmetic lemma (06 section 4): for the active debt stress `k`, the repair cell
containing atom `n` satisfies

```text
int_cell 2 e^{U/2} k(U) dU - 2 Lambda(n) n^{-1/2} k(log n) >= (debt + square + leakage) >= 0.
```

**Proposition (cluster obstruction).** Quantified over all edges `R -> infinity`, every
cell-local form of this lemma is false, unconditionally, unless the admissible kernel
class conspires to be nonpositive at the middle atoms of all sufficiently large clean
prime triples.

Proof sketch. By Maynard's theorem there are infinitely many triples of primes
`p1 < p2 < p3` with `p3 - p1 <= H` (`H` an absolute constant; Polymath8b gives
`H <= 398`). The number of such triples up to `x` is `>> x/(log x)^{O(1)}`, while prime
powers `p^k, k >= 2` up to `x` number `O(sqrt(x))` and each can meet at most `O(H^2)`
triples; hence infinitely many triples are *clean*: no prime power lies in `(p1, p3)`.
For a clean triple, the chronological cell of the middle prime `p2` has log-width
`<= (log p3 - log p1)/2 <= H/(2 p1)`, so

```text
smooth cell mass  ~ 2 e^{U/2} * width  <=  H / sqrt(p1)  * (1+o(1)),
atom weight        =  2 log(p2) / sqrt(p2),
atom / smooth     >=  (2/H) log p2  ->  infinity.
```

As the width shrinks, `avg_cell(k) -> k(log p2)`, so the cell current is

```text
~ (smooth mass - atom weight) * k(log p2) ~ - (2 log p2 / sqrt(p2)) k(log p2) < 0
```

whenever `k(log p2) > 0` - violating the lemma by an unboundedly large factor. qed (sketch)

Consequences:

```text
- "every cell pays for itself" is unconditionally false at scale; debt MUST be
  transported across neighborhoods of growing atom count (prime clusters are local
  debt spikes; long gaps are local surpluses; only their aggregate is balanced);
- the T1 active-23 geometry (lone atom, wide cell, placement thresholds) is
  structurally a small-R artifact - the numerics in section 1 watch it die
  (top share falling, peak debt growing);
- this redirects T2/T3: the refinement-stable statement cannot be cell-local.
```

## 4. Finding 3 - the window dial: where the arithmetic becomes unconditional

Let the storage certificate transport debt across windows of log-width `w` at edge `R`
(integer scale `h = w e^R`). The arithmetic input needed is control of
`psi(x+h) - psi(x) - h` at `x = e^R`:

```text
w >~ e^{-5R/12}    (h >~ x^{7/12+eps}):  asymptotic PNT in short intervals holds
                    UNCONDITIONALLY (Huxley; zero-density based - genuinely
                    Euler-borne, and false for DH, whose off-line zeros force
                    x^beta fluctuations);
w ~  e^{-R/2}      (h ~ sqrt(x)):        RH-strength territory;
w <  e^{-R/2}      cell scale:           beyond even RH.
```

So the right split of roles is:

```text
arithmetic (unconditional): short-interval prime-power asymptotics at the 7/12
    scale, i.e. the window-aggregated residual is o(1) RELATIVE to the local
    smooth current;
geometry (open core): the Sonin/Schur structure must absorb geometrically
    structured debt over windows of ~ e^{7R/12} integers using the archimedean
    margin.
```

But Finding 1 immediately disciplines this: the absorbed quantities are exponentially
larger than the final margin, so the absorption cannot be proved by estimating the
window remainder either - `o(1)` relative error is still astronomically bigger than
`e^{-1.5R}` relative margin. Pushed to its limit, the "arithmetic vs geometry" split
reproduces "zeros vs archimedean": the window remainder IS the zero-side oscillation.
Conservation of difficulty, made precise.

## 5. Where this leaves the program: passivity must be structural (KYP), not estimated

The one escape consistent with Findings 1-3: prove `rho <= 1` *structurally* - exhibit
the nested system as (a compression of) a passive system, so contractivity is exact and
needs no slack at all. This is the Kalman-Yakubovich-Popov view of T3: a transfer
function is contractive iff the Riccati LMI has a PSD storage solution `Pi`; the
numerics' `Pi_j = (-S_j)_+` is the *shadow* of such a certificate; the theorem is a
*closed-form realization* whose energy-balance identity is the explicit formula itself.

Where the Euler product enters (the only non-DH input): multiplicativity makes the prime
side a sum over places of geometric series in commuting shifts,

```text
P = sum_p P_p,    P_p = 2 sum_k (log p) p^{-k/2} B_{k log p},
```

and each local factor is a Herglotz / positive-real object in its convergence region -
single-place systems are passive *there*. DH's signed coefficients are not positive-real:
the litmus test lives at exactly the right place. The divergence of every local factor at
the boundary (s=1/2) must be absorbed by the archimedean supply - the CC20 corner tension
in system-theoretic clothes. The realization (= the interconnection of passive local
systems against the W_inf port, energy-balanced by the explicit formula) is the missing
object in this language; but unlike "H^1 of the square" it has a FINITE, testable shadow
at every R.

## 6. The new front target: one-place passivity

The smallest theorem-shaped rung consistent with all of the above:

```text
One-place passivity lemma (target).
For a single prime p:   W_inf - P_p >= 0   on pole-killed H_R, for ALL R.
```

Why this is the right next lemma:

```text
- it is NOT RH and not dispersing-equivalent: it extends CC20's archimedean
  positivity past support log 2 with one place's exact Euler data;
- it isolates the corner/Mertens budget question (can the archimedean form pay
  for ONE geometric series of shifts?) without prime-prime interference;
- it is plausibly provable: one Herglotz factor against the digamma form, with
  the Sonin constraints; no zero-side input anywhere near it;
- it is fail-closed NOW: prime_single_place_passivity.py measures it on the
  ladder; a negative entry kills it immediately, a stable margin floor makes it
  the program's first new unconditional theorem target;
- if it holds with room while the all-prime margin is knife-edge, the RH content
  is localized in the INTERFERENCE between places - sharpening where the missing
  structure must live.
```

Escalation path: one place -> two places ({2,3}: does the interconnection stay passive
with the SAME archimedean budget?) -> finitely many places with uniform constants ->
the Mertens divergence as the final wall, faced with structural (not estimated) tools.

## 6'. REFUTATION (same day): one-place passivity is false; positivity is collective

`prime_single_place_passivity.py` (quick ladder to R=4.96):

```text
W_inf - P_2 is already INDEFINITE at gmax=1.60 (eigmin = -0.14), and every tested
proper subset of places fails increasingly badly:
   p=2: -0.14 -> -1.51,  p=3: +0.29 -> -1.60,  {2,3}: -1.36,  {2,3,5}: -1.62 at 4.96,
while the FULL Euler margin stays positive (+2.9e-4 at 4.96).
```

(No contradiction with C-semilocal-2 / CC20, which tested support below ~ 2 log 2; the
refuted statement is the ALL-R one-place lemma of section 6.)

`prime_interference_rigidity.py` then sharpened the collapse into the strongest
structural facts the program now owns, at gmax=4.96 (full margin +2.946e-4):

```text
drop-one place:  EVERY place p <= 113 is individually necessary - removing any
                 single place's atoms sends eigmin to between -0.25 and -0.86
                 (a collapse ~1000x the margin). Only p=127,139 are droppable,
                 and those entered within ~0.1 of the edge where Lemma 1.3 says
                 their forms are still ~0 - an internal consistency check.
drop-one atom:   every individual prime-power atom is necessary: drop n=81 ->
                 -0.10; n=32 -> -0.11; n=2 -> -0.88; n=3 -> -1.01.
KMS exponent:    reweighting atoms to 2 Lambda(n)/n^beta, positivity holds ONLY
                 at beta=0.50: beta=0.49 -> -5.0e-2, beta=0.51 -> -9.3e-4.
                 It fails on BOTH sides: lighter atoms also break the form.
```

Readings (these replace the section-6 target):

```text
1. The prime side is NOT a load to be dominated - it is a load-bearing
   counterterm at the exact critical normalization n^{-1/2}. "Domination of the
   Toeplitz operator by the archimedean form" is the wrong mental model; the
   correct object is a destructive-interference lattice in which W_inf and every
   Euler atom jointly cancel to an exponentially small positive residue.
2. No place-by-place, atom-by-atom, or any-subset induction over the Euler
   measure can work. The induction can only be over SUPPORT (the Sonin
   filtration) - which the proof track already chose; this is now forced.
3. The structural inputs the realization must encode are now visible:
   (a) Q-linear independence of {log p} (unique factorization = the shifts
       generate a free abelian semigroup - the interference pattern lives on it);
   (b) the critical KMS weight p^{-k/2} (beta=1/2 is the Bost-Connes critical
       temperature; the rigidity sweep says the form knows this).
4. Revised front target (replaces one-place passivity): characterize the
   killing directions. For the minimal eigenvector of W_inf - P_subset, measure
   how each excluded atom acts on it (the repair matrix). The conjecture worth
   testing: killing directions of partial sums are multiplicative resonances,
   and the atom that repairs a resonance is determined by the free-semigroup
   structure. If true, the cancellation has a combinatorial skeleton that a
   realization can be built on; if false, the interference is genuinely
   spectral and the realization must come from the explicit formula itself.
```

## 6''. CONFIRMATION (same day): the resonance dictionary and the scalar-density skeleton

`prime_killing_resonance.py` tested 6'.4 at gmax=4.96. All three subsets pass perfectly:

```text
S={2}:      t0 = 9.0650  vs 2pi/log2 = 9.0647;  sign-match rate 1.000
S={2,3}:    t0 = 17.615  - simultaneous resonance: t0 log2/2pi = 1.943,
            t0 log3/2pi = 3.080 (both within 0.08 of integers);
S={2,3,5,7}: t0 = 22.960 - matches signs at ALL places incl. k_y(2)<0
            (t0 log2/2pi = 2.533: half-period at 2, integer at 3,5,7).
sign-match rate 1.000 in all three cases (significant atoms);
identity y^T M_full y = y^T M_S y - sum(excluded) holds to roundoff.
```

So: killing directions of partial margins are single-frequency multiplicative resonance
combs; the repair pattern at place p is `cos(t0 log p + phase)` - the equidistribution
of `{log p}` on the resonance circle. Hand-check for S={2}: primes 11, 23 (frac(log_2 p)
= .46, .52) are the deepest repairers; 19, 53 (.25, .73) are the near-zero atoms -
exactly as the dictionary predicts, through p=113.

**The scalar-density skeleton.** Transcribing the form to Fourier variables, with

```text
D_R(t) = -log pi + Re psi(1/4 + it/2) - 2 sum_{log n < R} Lambda(n) n^{-1/2} cos(t log n),
```

the program target is exactly:

```text
M_R >= 0  <=>  int |hat h(t)|^2 D_R(t) dt >= 0
              for every even real h, supp in [-R/2, R/2], hat h(0) = hat h(i/2) = 0.
```

The admissible |hat h|^2 are Fejer-type profiles of exponential type R (with two kills).
As R -> infinity, D_R converges weakly to the ZERO-COUNTING measure on the critical line
(each on-line zero a positive point mass; an off-line zero a signed dipole). The
explicit formula says: {Lambda(n) n^{-1/2}} + archimedean term ARE the Fourier
coefficients of that measure. So the target is a Bochner/Herglotz statement - the Euler
data is a positive-definite functional - and the finite-R witnesses have been measuring
its Fejer-smoothed shadows all along. The exponentially small margins are the smoothed
measure's minima between zeros.

This does not make the theorem easier (Bochner-positivity of the explicit-formula data
IS Weil positivity). What it changes is the WORKING COORDINATE: every Schur/storage/
debt quantity in 03-08 has a scalar transcription against D_R, where the objects are
classical (Fejer kernels, Poisson dipoles, equidistribution of log p) and where the
detection lemma of doc 00 and the margin asymptotics become computable side by side.
Next witness: min over t of the Fejer-smoothed D_R vs R - WHERE does the global minimum
sit (predicted: near the lowest zero gamma_1 = 14.13...), and is its decay the e^{-1.5R}
of the ladder?

## 6'''. The margin law is arithmetic, and the two-ringing decomposition

`prime_margin_law.py` (and O1: the convention reproduces the two-sided explicit formula
against 2000 actual zeros to residual 4.4e-13, `semilocal_2.verify_explicit_formula`):

```text
   gmax    W_inf alone   W - Smooth[0,R]   W - Smooth[log2,R]   exact Euler
   2.10    +5.5e-02      +8.2e-02          -2.1e-01             +2.6e-02
   2.30    -7.3e-02      -3.9e-02          -3.1e-01             +2.3e-02
   3.00    -3.4e-01      -2.8e-01          -3.5e-01             +4.5e-03
   4.96    -9.1e-01      -7.4e-01          -4.4e-01             +2.9e-04
   exact decay rate: e^{-1.45 R};  all surrogates: permanently indefinite.
```

Three facts, each load-bearing:

```text
1. W_inf ALONE goes indefinite at gmax ~ 2.3. CC20's archimedean positivity does
   not extend past its window; from 2.3 onward the primes RESCUE the archimedean
   form. "Dominate the prime term by W_inf" is wrong in both directions - the
   object is the joint cancellation. (This also bounds O4: the base-case anchor
   is genuinely small-support; the induction needs primes immediately after.)
2. Smooth surrogates are PERMANENTLY indefinite (saturating ~ -0.4..-0.9). The
   e^{-1.5R} positive residue is carried by the exact atomic measure. The margin
   law is arithmetic, not pole bookkeeping - refuting the natural guess that the
   margin size is RH-neutral.
3. Two-ringing decomposition. Truncating either measure at R puts the SAME
   pole-ringing  e^{R/2} cos(Rt - theta(t)) / |1/2 - it|  into the density
   (Perron residue of the pole at s=1); it cancels in the difference, and

       D_R^exact - D_R^smooth = zero-ringing
         = 2 Re sum_gamma e^{iR(gamma - t)} / (i(gamma - t)) + O(1)-terms.

   The surrogate forms are indefinite because Fejer profiles catch the pole-ring
   lobes (depth -0.4 after smoothing); the exact form is positive because the
   zero-phase ringing fills every lobe. The storage/debt mechanism of 04-07 IS
   this lobe-filling, transcribed to t-space; the chronological cells are the
   R-derivative of the ringing interplay.
```

The theorem-shaped residue of 6''': prove the lobe-filling without knowing the gamma's -
i.e. derive, from the prime side alone, that the truncated exact density's negative
excursions against admissible profiles never exceed the archimedean+killed-pole budget.
That is the original target, but now with explicit phases: every quantity in the fight
(pole lobe location Rt - theta(t), lobe depth, filling term) has a closed form except
the zero phases, which are exactly what the Euler product must supply via the
equidistribution structure of 6''.

## 6''''. Closure: the finite phenomenology is the explicit formula, exactly

Pushing 6''' through against admissible profiles, every term telescopes:

```text
- the pole ringing, tested against a pole-killed profile with truncation R >=
  the support of g, contributes EXACTLY ZERO:
      int_0^R 2 e^{u/2} g(u) du = ghat(i/2) + ghat(-i/2) = 0;
- the zero-ringing Dirichlet kernels sin(R(gamma-t))/(gamma-t), tested against a
  type-R profile, reproduce EXACTLY the spectral side (bandlimited reproducing
  identity): no side-lobe loss, no remainder.
```

So `(1/2pi) int |hat h|^2 D_R = 2 sum_{gamma>0} hat h(gamma)^2` exactly - the finite
forms contain no information beyond the explicit formula. Validation with no free
parameters (3000 actual zeros, `/tmp` probe, to be promoted on demand):

```text
gmax   form eigmin     spectral min     ratio
2.30   +2.3328e-02     +2.3352e-02      1.0010
3.24   +2.4397e-03     +2.4799e-03      1.0165
4.26   +4.1418e-04     +4.4464e-04      1.0737
4.96   +2.9464e-04     +3.2208e-04      1.0934   (drift = T=250 truncation)
```

Consequences, stated bluntly:

```text
1. The witness margins ARE the extremal zero-avoidance quantity:
       margin(R) = min over admissible type-R pole-killed profiles of
                   2 sum_gamma |hat h(gamma)|^2.
   The e^{-1.5R} law is the zero set's geometry (a Beurling-type extremal
   problem), not an arithmetic mechanism waiting to be found.
2. No further finite-window phenomenology can contribute proof content. Every
   "mechanism" read off a finite window (repair atoms, resonances, lobe
   filling, storage paths) is a re-reading of zero positions through the
   explicit formula. The phenomenology phase of the program is COMPLETE.
3. The only viable proof shape remaining is the one identified in section 5:
   construct, from the prime side alone, a positive structure (passive
   realization / positive-definite functional, Bochner from coefficients)
   whose energy identity is the explicit formula. Available structural inputs,
   each now tested: the free abelian semigroup on {log p} (unique
   factorization; resonance dictionary 6''), the critical KMS weight beta=1/2
   (rigidity 6'), Lambda(n) >= 0, and the archimedean digamma supply with its
   small-support CC20 anchor (bounded at gmax ~ 2.3, 6''').
   Graveyard discipline for this construction: de Branges chains fell to
   Conrey-Li; the Connes trace framing is circular (AGENDA); one-place and
   subset inductions were refuted today (6'). The realization must be global
   in the places from the start.
```

## 7. What dies, what survives (bookkeeping)

```text
DIES:    per-cell repair lemmas (Finding 2); slack-bearing storage estimates
         (Finding 1); T1-geometry as a generalization template (it remains a
         correct finite fact and a refutation gate); one-place passivity and
         every subset-of-places induction (section 6').
SURVIVES: the Sonin filtration + Schur frame (01, 03, 05 unchanged) - now the
         ONLY admissible induction coordinate; the exact-identity discipline;
         the fail-closed harness; T1 certification as refutation-grade backstop.
NEW:     the realization/KYP framing is the stated proof shape for T3, with the
         free-semigroup + critical-KMS structure (6'.3) as its required inputs;
         the killing-direction / repair-matrix characterization (6'.4) is the
         front diagnostic.
```
