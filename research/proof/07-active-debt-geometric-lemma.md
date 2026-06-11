# 07 - Active-debt geometric lemma

Status: current lemma target after the boundary-profile diagnostic in
`scripts/numerics/witness/prime_defect_active_debt_current.py`.

## 1. Exact edge-convolution reduction

Let `z` be the physical representative of an active Schur-debt stress. On a support edge
`[-a,a]`, the boundary stress has the autocorrelation form

```text
k(U) = int z(v) z(v-U) dv.
```

For high shifts `U` near `2a`, set

```text
w = 2a - U,
q(r) = z(a-r).
```

Then the support restriction is exact:

```text
v in [U-a, a].
```

With `v=a-r` and the evenness of `z`,

```text
k(2a-w) = int_0^w q(r) q(w-r) dr.
```

So the geometric object is not an arbitrary positive kernel. It is a one-sided convolution of the
edge profile with itself.

This gives the right coordinate for the repair cell. If the cell is `[lo,hi]` in `U`, then in edge
width coordinates it is

```text
w in [2a-hi, 2a-lo].
```

The atom at `log n` sits at

```text
w_n = 2a - log n.
```

The normalized repair inequality becomes

```text
Avg_cell(K) / K(w_n)
  >= weight_n / smooth_mass(cell)
     + (debt + Riccati square + Schur leakage)
       / (smooth_mass(cell) K(w_n)),

K(w) = int_0^w q(r)q(w-r)dr.
```

This is the finite geometric endpoint condition we should try to prove or certify first.

## 2. Boundary-asymptotic caution

The profile diagnostic shows that the terminal edge behavior is real but is not the repair
mechanism by itself.

For the default `n25/h0.06` late edge, the active profile has

```text
fit window          alpha in |z(a-r)| ~= C r^alpha
half support        1.989
one support         1.953
repair atom width   1.872
repair left width   1.687
```

Thus the true terminal-edge asymptotic is close to quadratic. If `q(r) ~= C r^alpha`, then

```text
K(w) ~= C^2 B(alpha+1, alpha+1) w^(2alpha+1).
```

The one-support fit therefore predicts an autocorrelation power near `4.9`, not the observed
effective power near `2.5` on the `23` repair cell. The pure edge-asymptotic model would predict
`Avg/K(log23)` around `13`, while the observed value is `3.122`.

The earlier `p=2.5` toy model is still useful, but only as a finite-cell effective law. It is not a
theorem from terminal edge vanishing.

Across the tested refinements:

```text
basis       alpha1  alphaAtom alphaLeft pEffAtom pEffHi  model p=2.5
n17/h0.100 +1.954   +1.949    +1.671    +1.236   +2.405   3.009
n21/h0.080 +1.954   +1.920    +1.705    +1.889   +2.659   3.009
n25/h0.060 +1.953   +1.872    +1.687    +2.523   +2.758   3.009
n29/h0.050 +1.954   +1.841    +1.594    +1.916   +2.218   3.009
n33/h0.045 +1.953   +1.833    +1.598    +2.077   +2.402   3.009
```

The stable fact is quadratic terminal vanishing. The load-bearing repair fact is finite edge-layer
mass and centroid displacement.

## 3. Correct finite target

The proof should now aim at a finite edge-layer convolution inequality.

For the active debt direction, define

```text
K(w) = q*q(w),
W_cell = [2a-hi, 2a-lo],
w_n = 2a-log n.
```

The geometric estimate should lower-bound the smooth weighted average

```text
int_{W_cell} 2 exp((2a-w)/2) K(w) dw
```

relative to `K(w_n)`. For the `23` cell, the atom is located at a smaller width than the smooth
cell centroid, so the smooth average sees more of the larger-width part of `K`.

The sufficient condition should be phrased as a one-sided mass or centroid estimate, for example:

```text
int_{W_cell} 2 exp((2a-w)/2) K(w) dw
  >= beta K(w_n) int_{W_cell} 2 exp((2a-w)/2) dw,
```

with `beta` large enough to pay the atom weight, old debt, Riccati square, and Schur leakage.

For the default repair cell:

```text
observed beta = 3.122,
required beta = 2.924.
```

The theorem should not require pointwise monotonicity of `k(U)`, since the coarse `n17/h0.10` basis
already violates strict monotonicity while still satisfying the normalized budget.

## 4. Promising sufficient hypotheses

The next finite tests should look for hypotheses on `q` that imply the weighted average bound:

```text
1. sign coherence of q on the repair depth interval;
2. enough edge-layer mass beyond w_n, not concentrated at the terminal edge;
3. a convolution centroid bound for K on W_cell;
4. a low-dimensional coefficient cone for the last few physical basis functions;
5. stability of the bound under coefficient perturbations and atom-location shifts.
```

These are geometric conditions on the active debt state. The arithmetic input is separate: the exact
Euler cell must place the atom and weight at `log n` so the residual current is positive after the
Riccati square and leakage are paid.

## 5. Edge-cone diagnostic

`scripts/numerics/witness/prime_defect_edge_cone.py` computes `K(w)=q*q(w)` directly and checks the
finite weighted-average inequality.

For the default `n25/h0.06` basis:

```text
width cell=[0.062815,0.240000]
w_atom=0.104506
beta observed=3.122
required beta=2.924
K centroid rel(U)=0.295
K mass left-of-atom(U)=0.956
q L2 beyond atom-width=0.835
q sign changes=0
```

Across refinements:

```text
basis       beta/req    centU  massLeft qL2Beyond sign  minBeta10 fail10
n17/h0.100 2.701/2.633 0.354  0.959   0.419    1    2.669   0/120
n21/h0.080 2.514/2.464 0.332  0.953   0.595    0    2.325   40/120
n25/h0.060 3.122/2.924 0.295  0.956   0.835    0    2.746   24/120
n29/h0.050 2.618/2.070 0.333  0.945   0.627    0    2.277   0/120
n33/h0.045 2.739/2.495 0.322  0.952   0.642    0    2.480   2/120
```

The stable statistic is the weighted convolution displacement: about `94.5%` to `95.9%` of the
weighted `K` mass lies to the left of the atom in `U`, equivalently at larger edge widths. Sign
coherence alone is not a theorem: the coarse `n17` case has one small sign change and still passes.

The perturbation column is also a warning. Sign-preserving `10%` multiplicative perturbations of the
active edge coefficients can break the normalized budget in several bases. Thus the useful cone
cannot be just "positive edge coefficients" or "q has one sign"; it must encode the active Schur
state, probably through a low-dimensional coefficient-ratio cone or a variational extremality
condition.

The beta sensitivity gives the first non-tautological cone direction. In the default basis:

```text
gap from edge   d log(beta) / d multiplier
0.252500        +0.001
0.188333        +0.253
0.124167        +0.660
0.060000        -0.914
```

Across refinements, the terminal-layer coefficient has negative beta derivative in all but the
coarse `n17` case:

```text
basis       terminal gradient   max interior gradient
n17/h0.100  +0.07               +0.07
n21/h0.080  -0.49               +0.46
n25/h0.060  -0.91               +0.66
n29/h0.050  -0.88               +0.56
n33/h0.045  -0.76               +0.42
```

So the edge-cone condition should include terminal anti-concentration: adding mass at the terminal
edge increases `K(w_atom)` more than the smooth cell average, while adding mass in the interior
edge layer improves the repair ratio.

## 6. Shell-sector restriction

`scripts/numerics/witness/prime_defect_shell_landscape.py` samples shell directions `y`, forms

```text
x = A^{-1}Cy,
f = [x,-y],
```

and compares the directional Schur debt with the exact Riccati repair from the `23` cell.

The normalized beta coordinate is only meaningful when `K(w_atom)>0`. If `K(w_atom)<=0`, the
atom term is already helpful because subtracting the atom increases the residual current on that
direction.

For the default `n25/h0.06` basis:

```text
Schur eigs before repair: -2.545512e-01, +8.196370e-01
negative directions:       233/721
positive-atom beta sector: 221
atom-helpful sector:       12
directionally repaired:    233
failed:                    0
min beta in negative sector:    1.048
min beta surplus in sector:    +0.109
min after on negative sector:  +2.494e-02
```

Across refinements:

```text
basis       neg/samp betaSec atomHelp repaired failed minBeta minSurp minAfter
n17/h0.100 244/361 244       0      244        0    1.388   +0.113   +4.898e-03
n21/h0.080 145/361 145       0      145        0    0.998   +0.068   +4.990e-03
n25/h0.060 117/361 111       6      117        0    1.050   +0.109   +2.494e-02
n29/h0.050  27/364  25       2       27        0    1.291   +0.284   +5.518e-02
n33/h0.045  52/364  41      11       52        0    1.127   +0.142   +2.865e-02
```

For the two-dimensional shells this samples the full direction circle. For the three-dimensional
refined shells it uses the Schur eigenvectors plus deterministic unit-sphere samples, so it is a
diagnostic rather than an exhaustive certificate.

This narrows the proof target. The edge-cone inequality is not required on arbitrary shell
directions; it is required on the current Schur-negative sector. Low-beta directions outside that
sector are irrelevant to storage because they are already supported by positive Schur margin.

## 7. Autodiff/KKT clue

`scripts/numerics/witness/prime_defect_export_julia_reduced.py` exports the default late finite
model to

```text
scripts/numerics/julia/generated/active23_data.jl
```

and `scripts/numerics/julia/active23_ad.jl` differentiates the reduced shell-direction objective
with Julia `ForwardDiff` through `QuadGK` one-dimensional integrals.

This is not a certification path. It is a way to see the variational geometry. The useful output is:

```text
active theta=0.157511
S=-2.545512e-01
after=+2.664505e-02
beta=3.121992
required=2.912332
surplus=+0.209661
dSurplus=-1.051144

AD stationary theta=0.450068
S=-1.652049e-01
after=+3.095277e-02
beta=1.600676
required=1.492152
surplus=+0.108525
dSurplus=0
```

So the active Schur eigenvector is not the worst budget direction, and the worst surplus direction
found by AD is not on the Schur boundary. It is an interior stationary point of the positive-atom
part of the Schur-negative sector.

The KKT candidate enumeration is:

```text
S=0 roots:      0.665929, 2.790685
K_atom=0 roots: 2.773228, 2.841438
dSurplus roots: 0.450068

Schur-boundary positive-atom candidate:
theta=0.665929
S=+3.000378e-14
after=+5.105894e-02
beta=1.040499
required=0.914476
surplus=+0.126023

Interior stationary candidate:
theta=0.450068
S=-1.652049e-01
after=+3.095277e-02
beta=1.600676
required=1.492152
surplus=+0.108525

Atom-sector boundary candidate:
theta=2.841438
S=-4.483102e-02
after=+7.183561e-02
K_atom ~= 0
```

This is a real conceptual correction for the sectoral route. If whole-shell matrix positivity fails
in a broader target, a proof cannot check only the active eigenvector and the boundary of the
negative sector. It should prove the directional budget throughout the negative sector by the
following case split:

```text
1. K(w_atom) <= 0:
   the atom is directly helpful; prove after(theta)>0 on this sub-sector.

2. K(w_atom) > 0 and S(theta)=0:
   prove beta(theta)-required(theta)>0 at Schur-boundary candidates.

3. K(w_atom) > 0 and S(theta)<0:
   any interior minimizer satisfies

     d/dtheta [ beta(theta) - required(theta) ] = 0.

   Prove positive surplus at such stationary candidates.
```

The AD witness gives candidate stationary equations to analyze, while interval arithmetic remains
the later certification tool.

## 8. Algebraic collapse of the default T1 target

The KKT picture above is still useful, but the default finite theorem has a simpler endpoint.
For the default two-dimensional shell and the exact `23` residual cell,

```text
H := S+G
```

is already positive definite on the whole shell:

```text
H = [[+0.0358652162535, -0.0412607325106],
     [-0.0412607325106, +0.1807102584705]]

eig(H) = +0.0249362550056, +0.1916392197184
h11    = +0.0358652162535
det(H) = +0.00477876445197
```

Thus the default sector theorem follows from Sylvester's criterion after the matrix entries are
interval-certified:

```text
H>0
  => y^*Hy > 0 for all y != 0
  => y^*(S+G)y > 0 for every Schur-negative direction.
```

For certification, `H` should be built directly as the post-cell Schur complement
`D_+ - C_+^* A_+^{-1} C_+`. The Riccati split explains the storage mechanism, but it is not the
least brittle way to enclose the default endpoint.

On the positive-atom part of the Schur-negative sector, the beta surplus is exactly this same
matrix statement in normalized edge-current coordinates. Let

```text
K_y = K_y(w_atom) > 0,
M = smooth_mass.
```

Then, for `y^*Sy<0`,

```text
beta_y - required_beta_y
  = y^*(S+G)y / (M K_y).
```

Indeed, `beta_y M K_y` is the smooth current, while `required_beta_y M K_y` is the atom current
plus the old Schur debt and Riccati square:

```text
beta_y M K_y                  = smooth_y,
required_beta_y M K_y         = atom_y - y^*S y + square_y,
smooth_y - atom_y - square_y  = y^*G y.
```

So the default beta/KKT diagnostic is not an independent proof obligation. It explains why `H>0`
looks geometrically plausible and identifies the sectors that a broader theorem must control if the
whole-shell positivity endpoint fails later.

The reproducible witness is:

```text
scripts/numerics/witness/prime_defect_default_t1_certificate.py
```

Its sampled identity check on the default negative sector reports:

```text
negative=233/721
positive_atom=221
atom_helpful=12
repaired=233
min after on negative sector=+2.493682584097e-02
min beta surplus=+1.085219256922e-01
max identity error=3.411e-13
```

## 9. Arithmetic placement sensitivity

`scripts/numerics/witness/prime_defect_active_atom_shift.py` keeps the active debt state and smooth
cell fixed, but shifts or rescales the repair atom in the Riccati update.

For the default `n25/h0.06` basis:

```text
cell 23=[3.000000,3.177185]
log23 relative position: 0.765
location threshold:      0.722
exact location slack:   +0.042 of the cell
weight threshold:        1.138 times exact weight
```

Across refinements:

```text
basis       loc*    atomRel  relSlack  scale*   afterExact  reducedExact
n17/h0.100 0.744   0.765   +0.021   1.144   +4.897e-03  +6.730e-03
n21/h0.080 0.750   0.765   +0.015   1.086   +4.990e-03  +5.123e-03
n25/h0.060 0.722   0.765   +0.042   1.138   +2.494e-02  +2.516e-02
n29/h0.050 0.648   0.765   +0.116   1.334   +5.154e-02  +5.180e-02
n33/h0.045 0.723   0.765   +0.041   1.161   +2.761e-02  +2.774e-02
```

So the exact atom is not infinitesimally critical, but the placement is genuinely load-bearing. A
proof cannot say "some atom in the right half of the cell" is enough. It needs the actual Euler
cell geometry: `log23` sits safely to the right of the location threshold, and the von
Mangoldt-scaled atom weight sits below the failure threshold.

## 10. Current direction

The next useful target is a fail-closed default matrix certificate:

```text
Construct rigorous enclosures for the entries of H=S+G in the active-23 finite model, then prove
H[1,1]>0 and det(H)>0.
```

The sectoral edge-cone theorem remains the likely generalization path:

```text
If a shell direction lies in the current Schur-negative sector, then either K(w_atom)<=0 and the
atom is directly helpful, or its active-state edge profile satisfies the terminal
anti-concentration / convolution displacement bound. With the exact Euler atom to the right of the
location threshold and with controlled weight, the repair cell satisfies the directional budget
inequality. Interior stationary directions of the positive-atom sector satisfy the additional
autodiff/KKT equations above and should be treated as the main finite proof case.
```

This sectoral statement is weaker than the final theorem and stronger than what default T1 now
needs. It should be tested against zeta, Davenport-Heilbronn, smooth-only, prime-only, power-only,
atom shifts, and coefficient perturbations before spending effort on a continuum or Lean
formalization.
