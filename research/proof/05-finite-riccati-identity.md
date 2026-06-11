# 05 - Finite Schur/Riccati update identity

Status: finite algebraic lemma proved. This is the fixed-space identity that the storage certificate
has to use.

## 1. Block update

Fix a finite-dimensional nested model with splitting

```text
H_R = H_L direct_sum S.
```

Let the current margin be

```text
M =
  [ A  C  ]
  [ C* D  ],
```

with `A > 0`, and define the Schur complement

```text
S_M = D - C* A^{-1} C.
```

Let one chronological cell update the margin by

```text
E =
  [ E_A  E_C  ]
  [ E_C* E_D  ],
M_+ = M + E =
  [ A_+  C_+  ]
  [ C_+* D_+  ],
```

where `A_+ = A + E_A > 0`.

Define the response map

```text
X = A^{-1} C
```

and the Riccati residual

```text
R = E_C - E_A X.
```

## 2. Lemma 5 - exact Schur/Riccati update

With the notation above,

```text
S_{M_+}
  = S_M
    + E_D - X* E_C - E_C* X + X* E_A X
    - R* A_+^{-1} R.
```

Equivalently, if

```text
Q_E[X] = E_D - X* E_C - E_C* X + X* E_A X,
```

then

```text
S_{M_+} = S_M + Q_E[X] - R* A_+^{-1} R.
```

The last term is negative semidefinite. It is the finite Riccati square that a storage proof must
pay for.

## 3. Proof

Since `C=AX`,

```text
C_+ = C + E_C = A_+ X + R.
```

Therefore

```text
C_+* A_+^{-1} C_+
  = (A_+X+R)* A_+^{-1} (A_+X+R)
  = X* A_+ X + X*R + R*X + R* A_+^{-1} R.
```

Using `A_+=A+E_A` and `R=E_C-E_A X`, the first three terms simplify to

```text
X* A X + X* E_C + E_C* X - X* E_A X.
```

Thus

```text
S_{M_+}
  = D + E_D - C_+* A_+^{-1} C_+
  = D - X*AX
    + E_D - X*E_C - E_C*X + X*E_A X
    - R* A_+^{-1} R.
```

Since `D-X*AX = D-C*A^{-1}C = S_M`, the identity follows. qed

## 4. Boundary current as the rank-one case

Let `y in S`, and set

```text
x = Xy = A^{-1}Cy.
```

The quadratic part of the update is

```text
<Q_E[X]y,y>
  = E_D(y,y) - 2 Re E_C(x,y) + E_A(x,x).
```

At a Schur boundary, `S_M y=0` and the boundary equations give the same `x` as in
`03-schur-stress-kernels.md`. If the update is the exact-minus-smooth residual direction in the
margin,

```text
E = -delta P_j,
```

then

```text
<Q_E[X]y,y> = -r_j(k),
k(U)=B_U(x-y,x-y).
```

So the scalar storage inequality in `04-storage-riccati-target.md` is the rank-one shadow of the
matrix update, but the full matrix identity also contains

```text
- <R y, A_+^{-1} R y> <= 0.
```

Ignoring this square would overstate the storage margin.

## 5. Fixed-space storage certificate

For a fixed shell space, the natural matrix certificate is

```text
Q_{E_j}[X_j] - R_j* A_{j+1}^{-1} R_j
  + Pi_j - Pi_{j-1} >= 0,
Pi_j >= 0,
Pi_0 = Pi_N = 0.
```

This is the fixed-space version of the Riccati target. A nontrivial transport `Phi_j` is only needed
when the support space itself changes between cells or edges.

## 6. Immediate numerical check to build next

The next script should compute, for the existing finite witnesses:

```text
Q_{E_j}[X_j],
R_j* A_{j+1}^{-1} R_j,
minimum storage Pi_j needed by backward recursion.
```

This will tell us whether the observed scalar storage depths survive the full matrix Riccati square.
