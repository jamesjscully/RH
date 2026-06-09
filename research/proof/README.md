# Prime-Toeplitz proof scaffold

This directory is the theorem/proof track extracted from
`research/work/H-proof-program.md`. The goal is to keep the proof attempt separate from numerical
diagnostics while preserving the conventions those diagnostics fixed.

## Objective

Prove the pole-killed Prime-Toeplitz domination theorem:

```text
P_Euler <= W_infty
```

on the Sonin support filtration. In nested form, for `H_L subset H_R`,

```text
M_R = W_infty - P_Euler(R)
```

must be a positive extension from `H_L` to `H_R`. Equivalently, in the `L2`-orthogonal splitting

```text
H_R = H_L + shell,
M_R = [ A  C  ]
      [ C* D  ],
```

the load-bearing target is the Schur inequality

```text
C* A^{-1} C <= D.
```

## Current files

0. `00-reduction-to-rh.md`
   Records the reduction `nested target => RH` with its provenance (Connes-Consani
   arXiv:2006.13771 + Weil's converse) and the four certification obligations O1-O4, including
   the CC20 base-case anchor (`A_infty >= 0` on the pole-killed Sonin space for support below
   `log 2` is CC20's theorem). Fixes the program's one-line shape: extend CC20's archimedean
   positivity past support `log 2`, paying with exact Euler atoms.

0a. `00a-detection-lemma.md`
   The O3 converse: an off-line zero forces a negative admissible test. The polynomial-
   prefactor device `h = (-D^2)(-D^2+1/4)G` makes pole-killing free; the phase-tuned
   two-member window produces the negative quadruple; on-line and attained-supremum
   interference are estimated; the unattained-supremum case is reduced to one stated
   averaging sub-lemma.

1. `01-sonin-schur-scaffold.md`
   Defines the continuum support spaces, pole-killing functionals, inclusion maps, and the Schur
   block target. It proves the first structural lemma: the Sonin spaces form a closed filtration, and
   Euler atoms with shift past the old support do not change the old block.

2. `02-euler-chebyshev-transgression.md`
   Begins the first arithmetic lemma. It proves the exact Euler/Chebyshev transgression identity
   behind the storage target:

   ```text
   sum Lambda(n) phi(log n) - int phi(U)e^U dU
     = phi(B)F(B) - phi(a)F(a) - int_a^B F(U)phi'(U)dU.
   ```

3. `03-schur-stress-kernels.md`
   Proves the Schur transfer first-variation formula, defines critical and boundary stress kernels,
   and isolates the first-crossing boundary class where the Lorentz stress becomes
   `k(U)=B_U(x-y,x-y)`.

4. `04-storage-riccati-target.md`
   Fixes the sign convention for exact-minus-smooth Euler residuals at a Schur boundary and states
   the Riccati/storage inequality that must replace naive pointwise residual monotonicity.

5. `05-finite-riccati-identity.md`
   Proves the exact finite Schur-complement update identity
   `S_+ = S + Q - R* A_+^{-1} R`, identifying the negative Riccati square the storage certificate
   must pay for.

6. `06-proof-outline-and-formalization.md`
   Collects the current proof skeleton, records what the finite Riccati diagnostic says, and marks
   which pieces are ready for eventual Lean formalization.

7. `07-active-debt-geometric-lemma.md`
   Converts the late active debt stress near the support edge into a one-sided edge-profile
   convolution and states the finite weighted-average repair inequality now being tested.

8. `08-default-t1-certificate.md`
   Records the simplified default T1 endpoint: for the exact active-23 residual cell, the finite
   matrix `H=S+G` is positive definite on the whole two-dimensional shell. This reduces the default
   sector theorem to a small Sylvester/interval certificate.

9. `09-inverse-analysis.md`
   The R1 risk-rung results: exponential margin decay kills slack-bearing estimates
   (certificates must be exact identities with terminal sign / KYP shape); the cluster
   obstruction (Maynard triples) kills per-cell repair lemmas unconditionally; the window
   dial locates the unconditional arithmetic input (short-interval PNT at 7/12) and the
   conserved difficulty; one-place passivity proposed and refuted the same day; drop-one
   and KMS-exponent rigidity show positivity is an irreducibly collective interference
   lattice pinned at beta=1/2.

Related witness:

```text
scripts/numerics/witness/prime_defect_active_debt_current.py
scripts/numerics/witness/prime_defect_active_atom_shift.py
scripts/numerics/witness/prime_defect_edge_cone.py
scripts/numerics/witness/prime_defect_shell_landscape.py
scripts/numerics/witness/prime_defect_default_t1_certificate.py
scripts/numerics/witness/prime_defect_t1_error_budget.py
scripts/numerics/witness/prime_defect_t1_stability.py
scripts/numerics/witness/prime_defect_t1_arb_components.py
scripts/numerics/witness/prime_defect_t1_winf_tail.py
scripts/numerics/witness/prime_defect_export_julia_reduced.py
scripts/numerics/julia/active23_ad.jl
scripts/numerics/witness/prime_ladder_scaling.py
scripts/numerics/witness/prime_single_place_passivity.py
scripts/numerics/witness/prime_interference_rigidity.py
```

This extracts the late active Schur-debt direction and reports the smooth-vs-atom arithmetic current
on the debt stress, including the boundary edge-profile diagnostic and the repair atom
location/weight sensitivity. The edge-cone witness computes the one-sided convolution target
directly and tests coefficient perturbations. The shell-landscape witness checks whether the
edge-cone inequality is needed on all shell directions or only on the Schur-negative sector. The
default T1 certificate witness computes `H=S+G`, checks the two-by-two Sylvester endpoint, and
verifies the beta-surplus identity. The T1 error-budget witness gives a conservative post-cell
block enclosure target, and the Arb component witness starts replacing Fourier-grid atom blocks
and smooth-cell blocks with compact rigorous overlap integrals. The W_inf tail witness tests finite
cutoffs, a tail envelope, and endpoint sensitivity for the archimedean block. The T1 stability
witness probes numerical sensitivity of the matrix endpoint before interval certification. The
Julia witness differentiates the reduced shell-direction objective through QuadGK integrals with
ForwardDiff.

## Rules of engagement

- Work in the log variable `u`.
- Use positive-type tests `g = h * h#`.
- Treat the prime term as a Toeplitz correlation `g(log n) = <h, tau_log(n)h>`.
- Kill the pole functionals before asking for positivity.
- Do not use zero-side positivity or any RH-equivalent positivity input.
- Do not replace the exact Euler measure by smooth PNT density before proving the Schur estimate.

## Immediate theorem path

1. Interval-certify the default active-23 matrix endpoint `H=S+G>0`.
2. Use the edge-layer convolution/KKT picture to decide whether `H>0` is refinement-stable or must
   be weakened to a sector certificate.
3. Extend fail-closed tests to coefficient perturbations and basis refinements; current
   DH/smooth/prime-only/powers-only checks fail as desired.
4. Define nontrivial boundary state transport `Phi_j` only when support spaces change.
5. Then attempt a continuum compactness/limit argument for boundary stress kernels.
6. Check every proposed inequality against the known finite stress kernels in
   `scripts/numerics/witness/prime_defect_stress_kernel.py`.
