# 04 - Storage/Riccati target for Euler residuals

Status: target formulation. The Riccati sign convention is fixed; the storage inequality is the next
unproved theorem.

## 1. Fixed-edge deformation

Keep one nested pair `H_L subset H_R` fixed. Compare a smooth Euler surrogate with the exact Euler
measure:

```text
dmu_0(U) = 2e^{U/2} dU,
dmu_E(U) = sum_{log n < R} 2 Lambda(n)n^{-1/2} delta_log n.
```

Let

```text
delta mu = dmu_E - dmu_0.
```

This comparison is a coordinate for the residual, not a proposed proof path by itself. The finite
witnesses show that the smooth surrogate can fail later shell tests. Therefore we may use
`dmu_0` to expose the Chebyshev transgression, but we may not assume `M_0` is a positive baseline.

For a stress kernel `k`, the exact-minus-smooth current is

```text
J(k) = int k(U) d(delta mu)(U).
```

With

```text
phi(U) = 2e^{-U/2}k(U),
F(U) = psi(e^U)-e^U,
```

`02-euler-chebyshev-transgression.md` gives

```text
J(k)
  = phi(B)F(B) - phi(a)F(a) - int_a^B F(U)phi'(U)dU
```

on any finite interval `[a,B]`, with the endpoint convention stated there.

## 2. Boundary Riccati sign

Let

```text
M(theta) = M_0 - theta delta P,
```

where `delta P` is the Toeplitz form associated with `delta mu`. Thus increasing `theta` moves from
the smooth surrogate toward the exact Euler form.

This paragraph fixes the local boundary sign. It becomes a global proof only inside a path whose
starting point is already known to be inside the Schur cone.

Suppose a first Schur-boundary contact occurs at `theta0`, with boundary pair `(x,y)` satisfying

```text
C y = A x,
C* x = D y,
A(x,x)=D(y,y)=1.
```

Let

```text
k(U)=B_U(x-y,x-y).
```

The Schur complement is

```text
S = D - C* A^{-1} C.
```

For the null direction `y`, differentiating `S` gives

```text
d <Sy,y>
  = dD(y,y) - 2 Re dC(x,y) + dA(x,x).
```

Since `dM = -delta P`,

```text
d <Sy,y> / dtheta
  = - int k(U) d(delta mu)(U)
  = -J(k).
```

Therefore:

```text
positive J(k)  = outward/harmful for the Schur boundary,
negative J(k)  = inward/repairing.
```

This is the sign convention the storage theorem must use.

## 3. Why a pointwise monotone inequality is too strong

A naive sufficient condition would be

```text
J(k) <= 0
```

for every boundary-admissible `k`. That would make the exact Euler deformation inward at every
boundary contact.

The finite control experiments show this is probably too strong in chronological form. Prefixes can
be harmful before later prime-power cells repair them. The right object is therefore a storage
certificate, not a pointwise monotone residual bound.

## 4. Chronological residual cells

Choose a chronological partition of `(a,B]` into cells `I_j` carrying one or a small cluster of
prime-power logarithms. Define

```text
delta P_j = P_E,j - P_0,j,
r_j(k) = <delta P_j, k> = int_{I_j} k(U)d(delta mu)(U).
```

Positive `r_j(k)` is harmful for the boundary Schur derivative; negative `r_j(k)` is repairing.

The scalar storage inequality should have the form

```text
-r_j(k_j) + V_j - V_{j-1} >= 0,
V_j >= 0,
V_0 = V_N = 0.
```

Here `k_j` is the boundary stress seen at the `j`th stage. Harmful cells increase stored deficit;
repairing cells release it. Summing over `j` gives terminal inwardness without requiring every prefix
to be inward.

## 5. Riccati form

The real certificate should not choose arbitrary scalar controls. It should be a state-space storage
functional on the shell boundary state. The expected form is

```text
V_j(y) = <Pi_j y, y>_{D_j},
Pi_j >= 0,
Pi_N = 0,
```

with a backward Riccati inequality

```text
Q_j + Pi_j - Phi_j* Pi_{j+1} Phi_j >= 0.
```

Here:

```text
Q_j       encodes the signed residual cell -delta P_j at the Schur boundary;
Phi_j     transports boundary shell states through the Sonin/Euler update;
Pi_j      stores temporary prefix deficits.
```

This is intentionally not yet a theorem. The next proof task is to define `Phi_j` from the
Schur-complement geometry rather than fitting it from numerics.

## 6. Noncircular theorem target

The storage theorem we want is:

```text
For every nested pair H_L subset H_R and every first-crossing boundary stress
k in K_bdry(L,R;M), the exact Euler residual cells admit a Riccati storage
certificate with V_0=V_N=0.
```

Inputs allowed:

```text
- Sonin support geometry;
- pole-killing constraints;
- exact Euler product measure, including prime powers;
- Chebyshev transgression identity;
- unconditional bounds/identities for psi(x)-x.
```

Inputs not allowed:

```text
- zero-side Weil positivity;
- RH-equivalent positivity of F;
- arbitrary optimal controls detached from dmu_E;
- replacing dmu_E by dmu_0 after the Schur boundary is reached.
```

## 7. Immediate attack point

The smallest useful lemma is not global RH. It is a finite-dimensional Riccati identity:

```text
Given a fixed nested finite model and chronological exact residual cells,
construct Phi_j and Q_j directly from Schur block updates so that the scalar
current identity above is the rank-one boundary case of the matrix inequality.
```

Once that identity is explicit, the numerical storage depths from
`scripts/numerics/witness/prime_defect_residual_causal_flow.py` can be reinterpreted as candidate
Riccati solutions rather than generic optimal controls.
