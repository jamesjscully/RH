# 06 - Current proof outline and formalization boundary

Status: working outline. This note summarizes what is now a clean proof program versus what remains
the actual research theorem.

## 1. Current theorem shape

The target is still the nested Prime-Toeplitz extension theorem:

```text
H_L subset H_R,
M_R = W_infty - P_Euler(R),
M_R =
  [ A  C  ]
  [ C* D  ],
C* A^{-1} C <= D.
```

The proof should be by exclusion of first Schur-boundary crossing.

## 2. Proof skeleton

### Step A - Sonin filtration

Define the pole-killed support spaces

```text
H_L = { h : supp(h) subset [-L/2,L/2], hat h(0)=hat h(i/2)=0 }
```

inside the logarithmic Fourier form domain. Then `H_L subset H_R`, and Toeplitz atoms with
`U >= L` vanish on `H_L x H_L`. Hence the old block is stable:

```text
M_R|_{H_L} = M_L.
```

This is `01-sonin-schur-scaffold.md`.

### Step B - Schur boundary stress

If the Schur inequality fails, there is a first boundary contact with

```text
rho = ||A^{-1/2} C D^{-1/2}||^2 = 1.
```

At that contact, a critical pair `(x,y)` satisfies

```text
C y = A x,
C* x = D y,
A(x,x)=D(y,y)=1.
```

The first variation reduces to the boundary stress kernel

```text
k(U) = B_U(x-y,x-y).
```

This is `03-schur-stress-kernels.md`.

### Step C - Arithmetic transgression

For

```text
phi(U)=2e^{-U/2}k(U),
F(U)=psi(e^U)-e^U,
```

the exact Euler-minus-smooth residual is

```text
J(k)
  = phi(B)F(B) - phi(a)F(a) - int_a^B F(U)phi'(U)dU.
```

This is an unconditional Stieltjes integration-by-parts identity, not a zero-side positivity input.
It is `02-euler-chebyshev-transgression.md`.

### Step D - Riccati storage

Chronologically decompose the exact residual cells on the incoming interval `[L,R]`:

```text
M_base = W_infty - P_exact(<L) - P_smooth([L,R]),
M_R = M_base + sum_j E_j.
```

For each finite Schur update,

```text
S_{j+1} = S_j + Q_j - R_j* A_{j+1}^{-1} R_j.
```

The storage theorem must prove that the exact Euler cells admit a matrix storage certificate for
these increments. This is the live theorem, not yet proved.

## 3. What the new Riccati diagnostic says

`scripts/numerics/witness/prime_defect_riccati_storage.py` uses the nested coordinate above:
old history exact, smooth only on `[L,R]`, exact residual cells added in log order.

Observed summary:

```text
edge        base Schur       final Schur      scalar-isotropic suffix
1.72->1.88 +2.253e-01       +2.253e-01       feasible
1.88->2.10 +1.817e-01       +7.823e-02       fails
2.30->2.52 +1.082e-02       +4.806e-02       fails
2.76->3.00 +2.086e-01       +6.344e-02       fails
3.00->3.24 -2.546e-01       +2.737e-02       fails
```

The identity error is roundoff-level. The negative Riccati square is usually small but not zero.
Therefore a proof that controls only the signed residual `Q_j` is incomplete.

The scalar-isotropic suffix test is too crude. It fails even where the final exact Schur complement
is positive, because the harmful and repairing directions rotate. The required storage has to be
matrix/state-dependent.

The late edge `3.00->3.24` is especially important: smooth incoming density starts outside the Schur
cone, and exact Euler residual cells repair it. This confirms that the theorem cannot be phrased as
"smooth is positive and discreteness is a small perturbation."

Additional endpoint-condition tests rule out two tempting stronger statements:

```text
- strict telescoping PSD increments: every future suffix of G_j is PSD;
- total repair dominates the initial smooth-base debt in Loewner order.
```

Both fail on computed edges. The more plausible endpoint condition is debt release:

```text
Pi_j = (-S_j)_+,
S_j + Pi_j >= 0,
Pi_N = 0,
Pi_{j+1} <= Pi_j.
```

Across the full tested support chain, this negative-part debt is zero on all earlier edges and, on
`3.00->3.24`, starts at `2.546e-01` and decreases to zero with no Loewner or trace increase. This is
still not a theorem: `Pi_j=(-S_j)_+` is a diagnostic description, not yet a constructive arithmetic
storage functional.

The row-level debt-direction diagnostic gives the first constructive-looking mechanism. On the late
edge the `23` cell has an indefinite global Riccati increment, but on the active debt vector it gives

```text
S_min:  -2.546e-01 -> +2.494e-02
ray(G): +2.812e-01
ray(Q): +2.967e-01
ray(square): +1.551e-02
alignment of min vectors: 0.995
```

Splitting the updated Schur form into the old negative eigendirection and its orthogonal complement
gives the finite scalar condition we should try to prove:

```text
head after repair:       +2.665e-02
complement min:          +1.899e-01
cross norm:              1.679e-02
Schur leakage cost:      +1.484e-03
reduced repaired margin: +2.516e-02
```

The arithmetic current behind this repair is now isolated in
`scripts/numerics/witness/prime_defect_active_debt_current.py`. For the active debt stress
`k(U)=B_U(x-y,x-y)` on `3.00->3.24`,

```text
cell 23: [3.000000, 3.177185]
smooth integral:          +3.967778e-01
exact atom at log 23:     +1.000723e-01
smooth - atom repair:     +2.967055e-01
Riccati square cost:      +1.550930e-02
net debt-direction gain:  +2.811962e-01

k(3.000000):              +6.250304e-01
k(mid cell):              +2.028511e-01
k(log 23):                +7.653175e-02
k(3.177185):              +1.538131e-02
smooth mass / atom weight: 1.270
smooth current / atom current: 3.965
```

So the repair is not merely that the smooth cell has slightly more mass than the atom. Most of the
margin comes from the active debt kernel being strongly decreasing across the cell: the smooth
density sees the large left side of the cell, while the exact atom samples near the smaller right
side.

Basis refinement keeps the mechanism, but warns against making monotonicity itself the theorem:

```text
basis       base Schur   final Schur  repair atom  monotone  centroid  atomRel  smooth/atom  reduced
n17/h0.10   -1.722e-01   +5.132e-03   23           False     0.354     0.765    3.430        +6.730e-03
n21/h0.08   -1.703e-01   +5.514e-03   23           True      0.332     0.765    3.192        +5.123e-03
n25/h0.06   -2.546e-01   +2.737e-02   23           True      0.295     0.765    3.965        +2.516e-02
n29/h0.05   -1.175e-01   +5.313e-02   23           True      0.333     0.765    3.324        +5.180e-02
n33/h0.045  -1.857e-01   +3.038e-02   23           True      0.322     0.765    3.478        +2.774e-02
```

The robust feature is the displacement:

```text
smooth-weighted centroid of k in the cell is near 0.30-0.35 of the interval,
while log(23) sits at 0.765 of the interval.
```

The repair atom is stable (`23`), and the reduced Schur margin stays positive across these bases.

The normalized budget form is:

```text
avg_k(cell) / k(log n)
  >= weight_n / smooth_mass(cell)
     + (debt + Riccati square + Schur leakage)
       / (smooth_mass(cell) k(log n)).
```

For the repair cell `23`, the tested ratios are:

```text
basis       observed avg/k(log23)   required avg/k(log23)
n17/h0.10   2.701                   2.633
n21/h0.08   2.514                   2.464
n25/h0.06   3.122                   2.924
n29/h0.05   2.618                   2.070
n33/h0.045  2.739                   2.495
```

This is currently the cleanest finite inequality: prove a lower bound for the smooth-cell average of
the active debt kernel relative to its value at the repair atom.

The physical autocorrelation picture explains why this ratio is large. Near the late support edge,
`k(U)=int z(v)z(v-U)dv` only sees the shrinking boundary overlap interval

```text
v in [U-a, a],   a = R/2 = 1.620.
```

For the `23` cell:

```text
U              overlap width      k(U)
3.000000       0.240              +6.250e-01
mid cell       0.151              +2.028e-01
log 23         0.104              +7.653e-02
3.177185       0.063              +1.538e-02
```

The empirical decay from the left endpoint has power exponents about `2.44, 2.52, 2.76`. A toy
finite-cell model

```text
k(U) proportional to (2a-U)^p
```

with `p=2.5` predicts:

```text
avg_k(cell)/k(log23) = 3.009,
centroidRel = 0.298.
```

The observed values are `3.122` and `0.295`.

The boundary-profile diagnostic corrects the interpretation. The active physical profile itself
vanishes almost quadratically at the terminal edge:

```text
fit window          alpha in |z(a-r)| ~= C r^alpha
half support        1.989
one support         1.953
repair atom width   1.872
repair left width   1.687
```

Pure terminal-edge asymptotics would give an autocorrelation exponent near `2alpha+1 ~= 4.9`, which
is far stronger than the effective repair-cell exponent and predicts a much larger average ratio.
Therefore the geometric lemma should be a finite edge-layer convolution/centroid estimate for active
debt vectors, not merely an edge-vanishing asymptotic and not an arbitrary kernel inequality. This is
spelled out in `07-active-debt-geometric-lemma.md`.

So the correct local statement is not `G_j >= 0`. It is:

```text
the exact Euler residual is positive on the current debt subspace,
and its off-debt negative directions do not create larger new debt.
```

Fail-closed compact tests currently support this as a zeta-specific property:

```text
mode     final all+  debt->0 all+  invalid  worst final   peak debt
zeta     True       True         0       +2.737e-02  2.546e-01
DH       False      False        4       -1.779e+00  1.816e+00
primes   False      False        5       nan         nan
powers   False      False        3       +8.463e-02  3.421e-02
smooth   False      False        3       -1.384e-01  1.384e-01
```

The invalid entries mean the relevant old or updated Schur block is not SPD in that mutilated model,
so the Schur-transfer theorem is not even well-posed there.

## 4. The live research lemma

The next theorem to attack is therefore:

```text
Finite matrix debt-release lemma.
For every finite Sonin extension and the exact chronological Euler residual
cells on [L,R], there exist PSD storage-debt matrices Pi_j such that

  S_j + Pi_j >= 0,
  Pi_{j+1} <= Pi_j,
  Pi_N = 0,

with Pi_0 controlled by the smooth-new Schur defect and the exact old history.
```

This replaces the too-rigid local condition

```text
Q_j - R_j* A_{j+1}^{-1}R_j + Pi_j - Pi_{j-1} >= 0
```

which fails because harmful cell directions can be absorbed by the current positive Schur margin.
The proof still needs a constructive formula or estimate for `Pi_j`; otherwise the statement is only
a restatement of computed positivity.

A sharper finite version to test/prove is:

```text
Let N_j be the current negative Schur eigenspace and G_j=Q_j-R_j*A_{j+1}^{-1}R_j.
Then

  P_{N_j}(S_j+G_j)P_{N_j} >=
    coupling leakage through N_j^\perp

and the new negative part of S_{j+1}
is no larger than the old storage debt.
```

This is the first place where a real arithmetic estimate should enter: the exact Euler cell has to
pair correctly with the active debt stress, not with every possible shell direction.

Candidate arithmetic lemma, finite form:

```text
For every active debt stress k arising from a first negative Schur direction,
the incoming prime-power cell containing the repair atom n satisfies

  int_cell 2e^{U/2} k(U)dU
    - 2 Lambda(n)n^{-1/2} k(log n)
      >= Schur leakage + Riccati square + required debt head.
```

The geometric side must explain why these active debt kernels have the required one-sided shape
inside the repair cell. The arithmetic side supplies the exact prime-power cell location and weight.
The safer shape hypothesis is a centroid/one-sided-mass inequality, not pointwise monotonicity.

## 5. Lean readiness

Some pieces are ready for formalization soon:

```text
- finite Schur complement algebra;
- Lemma 5: S_+ = S + Q - R* A_+^{-1} R;
- finite-dimensional first-variation formula under a simple singular value;
- support/correlation old-block invariance in a simplified L2 model;
- the discrete finite residual-cell identities.
```

Pieces not yet Lean-ready:

```text
- the continuum Sonin form-domain details for W_infty;
- the Stieltjes Chebyshev identity in full analytic generality;
- the matrix storage theorem;
- any compactness/limit passage from finite raised-cosine models to the continuum;
- the final Prime-Toeplitz domination theorem.
```

Pragmatic Lean plan when we start:

1. Formalize the finite linear algebra in Lean first, independent of zeta.
2. Keep all matrices over `R` with explicit symmetry/SPD hypotheses.
3. Prove the Schur/Riccati identity and first-variation lemma as reusable algebra.
4. Treat arithmetic cells as an abstract finite list of symmetric updates.
5. Only after the storage theorem is mathematically correct, add analytic interpretations.

That gives us useful formal pressure without forcing the unsolved analytic theorem into Lean too
early.
