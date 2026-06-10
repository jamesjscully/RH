# 24 - C5''-infty first checkpoint: the archimedean fold lives on FIXED POINTS, and c = 1/2 is the unique reflection-equivariant scheme

Status: 2026-06-10. Synthesis of worker M (research/work/M-thr-fold-test.md,
spot-verified: DMPR Cor 5.19 quoted verbatim from the archived PDF;
parity lemma re-derived by the lead; witness prime_int_thr_fold.py ALL
PASS). The THR candidate survives its first kill-test, sharpened, with
one precisely-posed hypothesis left standing.

## 1. The functor dichotomy (r1, carrier corrected)

As pre-registered, the test asked whether the C_2-TATE construction
folds the ladder. Answer: NO - and the failure is structural, not
fatal. At odd p the C_2-Tate of THR(F_p) is CONTRACTIBLE (Quigley-Shah:
(HF_p)^{tC_2} = 0), while the genuine C_2-FIXED POINTS carry exactly
the pre-registered fold:

    pi_* THR(F_p)^{C_2} = F_p[y],  |y| = 4,  res(y) = x^2
    (DMPR JEMS 2021, Cor 5.19)

- weights {n >= 0} -> {2n >= 0}: half-line, start 0, SPACING DOUBLED.
The dichotomy is functorial and matches docs 19/20 exactly:

```text
rotation subgroups  -> TATE construction   -> full ladder
                       (duality completion)   (local factors, anom dim 0)
reflection subgroups-> FIXED POINTS         -> folded half-ladder
                       (Tate VANISHES)        (Gamma-factor, anom dim (1-s)/2)
```

The Tate-vanishing at reflections is the structural form of the
program's repeated finding that "duality completion does not happen at
the archimedean place." And the C_2-involution acts on pi_{2k}THH(F_p)
by (-1)^k (DMPR, verified in-source): Serre's classical F_infinity
even/odd eigenvalue selection for archimedean local factors
materializes as genuine equivariance.

## 2. The ladder and the scheme (r2, r3)

r2: the folded ladder's regularized characteristic function is
2^{(1-s)/2} sqrt(2pi)/Gamma(s/2) with anomalous dimension (1-s)/2 - the
archimedean shape, ON the fixed-point carrier (witnessed); the
parametrized Tate TPR(F_p) keeps the full two-sided ladder
(Z_p[w^{+-1}], |w| = 4), anomalous dimension 0. The 1/(2pi) scale
remains underived (standing debt).

r3 - THE PARITY LEMMA (elementary, witnessed, lead-verified): in the
vacuum-term scheme family f_c(w) = q^{cw}(1 - q^{-w}),

    f_c(-w) = -q^{(1-2c)w} f_c(w),

so c = 1/2 - the symmetric/KMS-1/2 scheme - is the UNIQUE scheme
equivariant under the reflection w -> -w. This is the first
derivation-shaped account of the program's missing fourth realization
input: the real structure does not merely permit the symmetric scheme,
it FORCES it - conditional on:

    H-r3 (the open C5'' theorem, now precisely posed): the C_2 of THR
    acts on the analytic determinant layer of the Tate/periodic
    construction, i.e. the regularized-determinant functor can be made
    C_2-equivariant. No such theorem exists in the literature.

No conflict with Hesselholt: his Theorem A is non-equivariant (and
selects c = 0 there); the real refinement would compute the self-dual
completion. Doc 20's correction C1 stands; H-r3 is the named bridge
that would discharge it.

## 3. Gap ledger (honest)

- p = 2: the fixed points do NOT fold cleanly (Euler-class families
  F_2[xbar, y]); THR(F_2)^{tC_2} is not in the literature (precise
  missing computation stated in the M-doc). The prime 2 is exactly
  where CC's base puts its distinguished point (K = -2{2}) - the
  recurring 2-adic/real entanglement; flagged, not resolved.
- The fold is established at FINITE places (the local shadow of the
  archimedean mechanism); the compactified archimedean object itself
  still does not exist - that remains C5'''s burden.
- Carrier relocation (Tate -> fixed points) was identified post-hoc
  relative to the registration; recorded as such (the registered r1
  strictly FAILED; the fold claim rides on the fixed-point carrier).

## 4. Status after the checkpoint

Gate C5''-infty refines to: (infty-1') fixed-point fold - THEOREM-GRADE
at odd p finite places (DMPR); p = 2 and the archimedean object open;
(infty-2) the 1/(2pi) scale - open; (infty-3') H-r3 - the single named
hypothesis from which KMS-1/2 follows by the parity lemma; (infty-4)
rank factors - untouched. The scheme-selection question (doc 21's
Q-SCHEME, tension T-a) now has a candidate ANSWER PATH rather than a
candidate answer: real equivariance of the determinant layer.
