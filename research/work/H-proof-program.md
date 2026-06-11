# H - Proof program for the Prime-Toeplitz / Euler-control target

Proof scaffold: `research/proof/README.md`.

2026-06-09. This note freezes the working target extracted from
`research/work/G-prime-carleson.md`. Its purpose is to stop the numerical exploration from drifting
and give the proof attempt a clear contract.

## 1. Broad goal

We are not trying to add a fake finite residue field at infinity to `Q`. The replacement target is an
analytic/geometric finite-ground substitute:

```text
finite-ground purity
  -> ordered prime-Toeplitz passivity in the pole-killed/Sonin boundary.
```

For positive-type Weil tests `g = h * h#`, the prime term is a Toeplitz correlation,

```text
g(log n) = <h, tau_log(n) h>,
```

not a pointwise sampling square. Therefore the candidate proof cannot be an ordinary positive
Carleson-measure theorem. It must prove contractivity/passivity of an ordered Euler-Toeplitz
operator against the archimedean/Sonin form.

The global target is:

```text
T_Lambda = 2 sum_{n>=2} Lambda(n)n^{-1/2} tau_log(n)
is dominated by the archimedean Sonin form on the pole-killed space.
```

This would give Weil positivity and hence RH.

## 2. Frozen finite theorem target

Use nested pole-killed/Sonin support windows

```text
H_L subset H_R.
```

Let

```text
M_R = W_infty - P_Euler(R),
P_Euler(R) = sum_{log n < R} 2 Lambda(n)n^{-1/2} T_log(n).
```

In an `L2`-orthonormal decomposition

```text
H_R = H_L + shell,
```

write

```text
M_R =
  [ A  C  ]
  [ C* D  ].
```

The finite theorem is:

```text
Nested Prime-Toeplitz extension theorem:
  A > 0,
  D > 0,
  C* A^{-1} C <= D.
```

Equivalently, with

```text
K = A^{-1/2} C D^{-1/2},
```

prove

```text
rho(L,R) = ||K||^2 <= 1,
Delta(L,R) = I - K* K >= 0.
```

This is the load-bearing theorem. Active channels, bottom spectral bundles, and determinant
transgressions are diagnostics only unless they can be derived from this full extension statement.

## 3. What the proof must explain

The proof must account for the following stable finite facts.

1. **Zeta versus DH.** Zeta remains positive/passive on tested nested extensions; Davenport-Heilbronn
   exits the cone.
2. **Exact coefficient scale.** Old/global rescaling is confined to a narrow tube around the exact
   von Mangoldt scale. Smooth perturbations, sign flips, shuffles, and DH coefficients fail.
3. **Cumulative old history.** The positive defect is not local to the incoming shell. Old Euler
   history is load-bearing.
4. **Signed atom current.** Atom sensitivities are mixed. Some old atoms repair, others harm. No
   atomwise monotone proof is available.
5. **Oscillatory stress kernels.** Critical stresses produce shift kernels `k(U)` with sign changes.
   Positive spectral density does not imply pointwise positivity at prime-power shifts.
6. **Exact Euler measure.** Smooth PNT density, prime-only, and prime-power-only operators fail on
   later shell tests. The exact combined prime-power measure succeeds.
7. **Chebyshev residual structure.** The discrete-minus-smooth residual is

   ```text
   phi(B)F(B) - int F(U) phi'(U)dU,
   F(U) = psi(e^U) - e^U
   ```

   up to the chosen normalization.
8. **Crude bounds are too wasteful.** `sup|F|TV(phi)` and L2 estimates lose most of the observed
   cancellation.
9. **Control is causal and global.** The exact residual cells interlace harms and repairs. Positivity
   often returns only near the terminal cells, after carrying prefix deficits.

## 4. Required separation of roles

The proof should split into geometry and arithmetic, without letting either side hide the other.

Geometry should supply:

```text
- the pole-killed/Sonin spaces H_L;
- the archimedean form W_infty;
- the shell decomposition H_R = H_L + shell;
- the admissible transfer stresses S_{L,R};
- a passive/canonical-system/storage structure for Schur complements.
```

Arithmetic should supply:

```text
- the exact Euler product measure dmu_E = sum 2 Lambda(n)n^{-1/2} delta_log(n);
- the prime-power corrections, not just primes;
- the Chebyshev-error / explicit-formula residual identity;
- the ordered causal controller that repairs smooth surrogate failure.
```

The desired bridge is:

```text
For every admissible stress kernel phi from the Sonin extension geometry,
the exact Euler measure satisfies the storage inequality needed for
terminal Schur positivity.
```

## 5. Noncircularity rules

The proof may not use:

```text
- zero-side Weil positivity;
- any statement equivalent to RH hidden as a positivity input;
- a fake finite residue field at infinity;
- pointwise positive prime sampling in place of Toeplitz correlations;
- determinant/log-volume positivity as a substitute for Loewner positivity;
- active low-rank channels as definitions of the theorem;
- smooth PNT-density replacement before Schur positivity is proved;
- prime-only or prime-power-only truncations as the arithmetic object;
- arbitrary optimal controls not tied to Euler-product data.
```

These are not aesthetic restrictions. Each one corresponds to a failure mode already seen in the
finite witnesses.

## 6. Admissible stress kernels

For a support extension, suppose the top singular value of

```text
K = A^{-1/2} C D^{-1/2}
```

is `s = sqrt(rho)` with generalized old/shell singular vectors `x,y` normalized by

```text
x* A x = 1,
y* D y = 1,
x* C y = s.
```

The first variation is

```text
d rho = 2s x* dC y - rho x* dA x - rho y* dD y.
```

For one weighted Toeplitz atom,

```text
d rho / d scale(atom)
  = rho <A_atom x,x> + rho <D_atom y,y> - 2s <C_atom y,x>.
```

Equivalently, define the finite stress tensor

```text
S_{L,R} =
  [ rho x x*       -s x y* ]
  [ -s y x*        rho y y* ].
```

Then each Euler atom pairs with this stress. In Fourier variables this becomes a shift kernel

```text
k_{L,R}(U)
  = (1/2pi) int H_{L,R}(t) cos(Ut) dt,
H_{L,R}(t) = phihat(t)* S_{L,R} phihat(t),
```

and zeta contributes

```text
2 Lambda(n)n^{-1/2} k_{L,R}(log n).
```

The proof program needs a noncircular continuum definition of the admissible class containing these
finite critical stresses. Ideally this class is produced by a canonical system, de Branges space, or
passive scattering realization.

## 7. Control formulation

The useful control problem is not:

```text
choose a small arbitrary correction to the smooth PNT surrogate.
```

Naive L1/L2 actuator costs choose artificial fractional controllers. The arithmetic controller is
fixed by the Euler product.

The useful problem is:

```text
Given the exact causal residual cells
  R_n = P_smooth_cell(n) - P_atom(n),
construct a storage functional V_k such that
  V_{k+1} - V_k absorbs temporary prefix deficits,
and terminal storage release implies
  M_R >= 0 or C* A^{-1} C <= D.
```

This is the Riccati/storage version of the theorem. It must allow nonmonotone prefixes:

```text
smooth -> negative prefixes -> terminal repair.
```

## 8. First proof obligation

The first proof attempt should be a lemma, not RH.

```text
Lemma 1 (finite storage inequality, target form).
For every nested extension H_L subset H_R and every admissible critical
stress kernel phi_{L,R}, the exact Euler residual satisfies

  phi(B)F(B) - int F phi'

with a bound sharp enough to imply Delta(L,R) >= 0 after adding the
archimedean/Sonin drift.
```

This lemma is still too broad, but it identifies the right variables:

```text
admissible phi from geometry,
Chebyshev error F from arithmetic,
storage/Riccati inequality linking them,
terminal Schur positivity.
```

## 9. Immediate next tasks

1. Define the continuum Sonin support spaces `H_L` cleanly, with pole-killing constraints and
   inclusion maps. Done in `research/proof/01-sonin-schur-scaffold.md`.
2. Write the exact Schur-complement theorem in functional-analytic language. Started in
   `research/proof/01-sonin-schur-scaffold.md`.
3. Derive the stress-kernel variational formula in that continuum notation. Done in
   `research/proof/03-schur-stress-kernels.md`.
4. Define the admissible stress-kernel class without referring to numerical eigenvectors if possible.
   Boundary-critical and envelope classes are separated in
   `research/proof/03-schur-stress-kernels.md`.
5. Formulate a candidate storage/Riccati inequality for the exact Euler residual cells. Done as a
   target in `research/proof/04-storage-riccati-target.md`.
6. Identify the smallest nontrivial lemma that can be attacked without assuming Weil positivity.
   Done algebraically in `research/proof/05-finite-riccati-identity.md`; diagnostic and proof
   outline are in `research/proof/06-proof-outline-and-formalization.md`. Current target: solve the
   matrix storage endpoint condition.

At this point, further numerical work should be tied to one of these tasks. Otherwise it is likely to
produce more diagnostics without moving the proof.
