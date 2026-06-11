# 03 - Schur stress kernels and boundary reduction

Status: variational lemma proved. The admissible class is defined in the exact form needed for the
storage lemma.

## 1. Setup

Use the Sonin filtration and forms from `01-sonin-schur-scaffold.md`. Fix `0 < L < R`, and write the
`L2`-orthogonal splitting

```text
H_R = H_L direct_sum S_{L,R}.
```

Assume the compressed margin

```text
M_R = A_infty - P_R
```

has block form

```text
M_R =
  [ A  C  ]
  [ C* D  ],
```

with `A > 0` on `H_L` and `D > 0` on `S_{L,R}`. Define the transfer operator

```text
K = A^{-1/2} C D^{-1/2}.
```

The Schur target is

```text
rho = ||K||^2 <= 1.
```

## 2. Critical singular pairs

A critical transfer pair is a triple `(x,y,s)` with

```text
x in H_L,       y in S_{L,R},       s >= 0,
A(x,x) = 1,    D(y,y) = 1,         C(x,y) = s,
```

and generalized singular equations

```text
C y = s A x,
C* x = s D y.
```

Equivalently, `A^{1/2}x` and `D^{1/2}y` are a singular-vector pair for `K` with singular value `s`.
For the top pair,

```text
rho = s^2.
```

## 3. Lemma 3 - first variation of the transfer norm

Let `M(eps)` be a differentiable deformation of the block matrix, with block derivative

```text
dot M =
  [ dot A  dot C  ]
  [ dot C* dot D  ].
```

Assume the top singular value of `K` is simple at `eps=0`, and let `(x,y,s)` be the top critical
pair. Then

```text
dot rho
  = 2s Re dot C(x,y)
    - rho dot A(x,x)
    - rho dot D(y,y).
```

**Proof.**

Let

```text
p = A^{1/2}x,
q = D^{1/2}y,
K = A^{-1/2} C D^{-1/2}.
```

Then `||p||=||q||=1`, `Kq=sp`, and `K*p=sq`. For a simple singular value,

```text
dot s = Re <p, dot K q>.
```

Differentiating `A^{-1/2} C D^{-1/2}` directly is messy, but it is enough to differentiate the
constrained Rayleigh quotient

```text
s = C(x,y)
```

under the constraints `A(x,x)=D(y,y)=1`. The Lagrange equations for the critical point are precisely

```text
C y = s A x,
C* x = s D y.
```

The variations of `x` and `y` cancel by these equations, leaving

```text
dot s
  = Re dot C(x,y)
    - (s/2) dot A(x,x)
    - (s/2) dot D(y,y).
```

Since `rho=s^2`, `dot rho=2s dot s`, which gives the formula. qed

## 4. Euler-atom current

For one weighted Toeplitz atom

```text
P_U = w B_U,
w = 2 Lambda(n)n^{-1/2},   U = log n,
```

the margin deformation for increasing its scale is

```text
dot M = -P_U.
```

Lemma 3 gives

```text
d rho / d scale(P_U)
  = rho P_U(x,x) + rho P_U(y,y) - 2s Re P_U(x,y).
```

This is the analytic version of `scripts/numerics/witness/prime_defect_variational_current.py`.

## 5. Stress kernels

For a critical pair `(x,y,s)`, define the stress kernel

```text
k_{x,y,s}(U)
  = rho B_U(x,x) + rho B_U(y,y) - 2s Re B_U(x,y),
rho = s^2.
```

Then the Euler-atom current is

```text
d rho / d scale(P_U) = w k_{x,y,s}(U).
```

In Fourier variables, with

```text
X(t)=hat x(t),   Y(t)=hat y(t),
```

the kernel is the cosine transform of the Lorentz density

```text
H_{x,y,s}(t)
  = rho |X(t)|^2 + rho |Y(t)|^2 - 2s Re(X(t) conjugate(Y(t))).
```

In the real even model this becomes

```text
H(t)
  = ((rho+s)/2)(X-Y)^2 + ((rho-s)/2)(X+Y)^2.
```

For `s < 1`, the second coefficient is negative. This is why the finite stress kernels oscillate and
why a positive point-sampling/Carleson proof is the wrong abstraction.

## 6. Boundary reduction

To prove passivity, it is enough to prevent a first crossing through `rho=1`. At such a crossing,
`s=1` and `rho=1`, so the Lorentz stress collapses to the positive-density boundary kernel

```text
k_{x,y,1}(U)
  = B_U(x-y, x-y).
```

This does not make `k(U)` pointwise nonnegative; a positive Fourier density can still have an
oscillatory cosine transform. But it removes the negative Lorentz square. The first storage theorem
should therefore be stated for boundary-critical kernels, not for arbitrary finite stresses with
`s<1`.

## 7. Admissible classes

We will use three nested names.

### Critical Stress Kernels

`K_crit(L,R;M_R)` is the set of kernels `k_{x,y,s}` produced by top critical singular pairs of the
actual margin `M_R`, with `A,D > 0`.

This class is exact but depends on the margin. That dependence is not circular: it is the standard
way to extract a separating stress from a hypothetical Schur failure, and it uses no zero-side
positivity.

### Boundary Stress Kernels

`K_bdry(L,R;M_R)` is the subset of `K_crit` with `s=1`. These are the kernels relevant to first
crossing:

```text
k(U) = B_U(f,f),   f=x-y in H_R.
```

The vectors are not arbitrary. They must arise from the boundary equations

```text
C y = A x,
C* x = D y,
A(x,x)=D(y,y)=1.
```

### Envelope Kernels

`K_env(L,R)` is the larger class obtained by dropping the boundary equations and keeping only

```text
f=x-y,   x in H_L,   y in S_{L,R}.
```

This envelope is useful for estimates and compactness, but it is probably too large for the final
arithmetic inequality. Proving a sharp residual inequality for all of `K_env` would be much stronger
than the current target and may be false.

## 8. Next step

The storage lemma should be formulated at the boundary:

```text
for every k in K_bdry(L,R;M_R),
the exact Euler residual supplies a nonnegative inward Schur derivative,
after allowing a causal storage term for temporary prefix deficits.
```

That is the smallest nontrivial theorem target that matches both the Schur geometry and the finite
control evidence.
