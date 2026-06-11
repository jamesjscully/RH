# 08 - Default T1 finite certificate

Status: floating-point certificate; rigorous interval enclosure still pending.

## 1. Statement

For the default late edge `3.00 -> 3.24`, default raised-cosine basis
`ncenters=25, half_width=0.06`, and exact repair cell `n=23`, let

```text
S = D - C^* A^{-1} C
```

be the current Schur complement on the two-dimensional shell before the `23` cell. Let

```text
G = Q - R^* A_+^{-1} R
```

be the exact finite Riccati Schur increment from the residual cell

```text
E_23 = P_smooth([3.00, log 24]) - P_atom(23).
```

The default finite target is:

```text
For every nonzero shell direction y,
  y^*(S+G)y > 0.
```

This is stronger than the sector theorem originally targeted, which only asked for positivity on
directions with `y^* S y < 0`.

Equivalently, since `S+G` is the Schur complement after adding the exact `23` residual cell, write

```text
M_+ = M_current + E_23 = [A_+ C_+; C_+^* D_+].
```

Then the same endpoint matrix is

```text
H = D_+ - C_+^* A_+^{-1} C_+.
```

For the default edge there are no exact residual cells before `23` inside `[3.00,3.24]`, since the
only active zeta prime-power logarithms in the interval begin at `log 23`. Thus, after adding the
`23` residual cell, the post-cell margin has the direct form

```text
M_+ =
  W_inf
  - P_exact(log n < 3.00)
  - P_atom(23)
  - P_smooth([cell_hi(23), 3.24]).
```

The code check in `prime_defect_t1_error_budget.py` verifies that this direct composition agrees
with the incremental construction to `4.441e-16`.

The certification target can therefore avoid the internal Riccati decomposition and prove directly:

```text
A_+ > 0,
H > 0.
```

## 2. Numeric matrix certificate

The witness

```text
scripts/numerics/witness/prime_defect_default_t1_certificate.py
```

computes:

```text
S =
[[-2.281205995503e-01, -1.664116127698e-01],
 [-1.664116127698e-01, +7.932064774738e-01]]

G =
[[+2.639858158038e-01, +1.251508802592e-01],
 [+1.251508802592e-01, -6.124962190033e-01]]

H = S+G =
[[+3.586521625353e-02, -4.126073251055e-02],
 [-4.126073251055e-02, +1.807102584705e-01]]
```

The eigenvalues are:

```text
eig(S) = -2.545511630634e-01, +8.196370409870e-01
eig(H) = +2.493625500557e-02, +1.916392197184e-01
```

For a rigorous two-by-two proof it is enough to interval-certify Sylvester's inequalities:

```text
H_11  = +3.586521625353e-02 > 0,
det H = +4.778764451968e-03 > 0.
```

## 3. Proof skeleton

Once the matrix entries are rigorously enclosed:

```text
H_11 > 0 and det(H) > 0
  => H is positive definite by Sylvester's criterion
  => y^*Hy > 0 for every y != 0
  => y^*(S+G)y > 0 for every Schur-negative y.
```

This closes default T1 without a separate KKT minimization.

## 4. Budget identity

On the positive-atom sector, where `K_y(w_atom)>0`, the beta surplus is the same certificate in
edge-current normalization. With `M=smooth_mass`, for every Schur-negative direction:

```text
beta_y - required_beta_y
  = y^*(S+G)y / (M K_y(w_atom)).
```

The witness checks this identity on the sampled direction circle:

```text
negative=233/721
positive_atom=221
atom_helpful=12
repaired=233
min after on negative sector=+2.493682584097e-02
min beta surplus=+1.085219256922e-01
max identity error=3.411e-13
```

The atom-helpful sector `K_y(w_atom)<=0` does not need beta normalization; `H>0` already gives the
post-repair positivity.

## 5. Stability probe

The companion witness

```text
scripts/numerics/witness/prime_defect_t1_stability.py
```

checks nearby numerical construction choices. Refining the physical L2 grid used to orthonormalize
the nested basis from `6001` to `12001` gives:

```text
default: eigmin(H)=+2.493626e-02, det(H)=+4.778764e-03
l2-fine: eigmin(H)=+2.493625e-02, det(H)=+4.778765e-03
drift:   max|deig(H)|=1.6e-08, |ddet(H)|=3.6e-10
```

This is only a stability probe. It is useful because it says the observed margin is not an artifact
of the default L2 grid, but it does not replace rigorous error bounds.

## 6. Perturbation Budget

The post-cell Schur witness

```text
scripts/numerics/witness/prime_defect_t1_error_budget.py
```

gives a conservative sufficient entrywise budget for rigorous enclosures of the post-cell block:

```text
direct composition error = 4.441e-16
eig(A_+) min:      +3.930222e-03
cond(A_+):         9.429e+02
eig(H) min:        +2.493626e-02
uniform eta:       3.867e-09 keeps ||delta H|| below 0.5 eigmin(H)
```

The tightness comes mostly from the old-block inverse. This budget is sufficient, not necessary;
direct interval Schur computation may be less wasteful.

## 7. Arb Atom And Smooth Components

The witness

```text
scripts/numerics/witness/prime_defect_t1_arb_components.py
```

computes compact physical overlap integrals for the `23` Toeplitz atom and selected smooth-cell
entries using Arb. For sampled atom entries, the Arb radii are around `1e-47` or smaller. On the
full ambient atom:

```text
ambient max |Fourier-grid atom - Arb atom| = 6.198e-08
ambient max exact-zero grid noise          = 2.934e-08
compressed atom operator-norm difference   = 1.676e-06
```

Replacing the Fourier-grid `23` atom by the Arb-overlap atom shifts the final endpoint by:

```text
eig(H) default atom     = +2.493625500557e-02, +1.916392197184e-01
eig(H) Arb-overlap atom = +2.493716727061e-02, +1.916374140765e-01
eig(H) shift            = +9.123e-07, -1.806e-06
```

So exact atom certification is feasible and does not threaten the margin. It also removes a
Fourier-grid noise source that is too large to ignore under the conservative raw-entry budget.

For selected high-edge smooth-cell entries in the same repair cell:

```text
max |Fourier-grid smooth - Arb smooth| = 2.771e-09
max Arb smooth radius                  = 8.101e-27
```

For selected entries in the post-cell smooth suffix `[cell_hi(23),3.24]`:

```text
max |Fourier-grid suffix - Arb suffix| = 1.591e-09
max Arb suffix radius                  = 3.899e-32
```

So the smooth residual cells and the actual post-cell smooth suffix both have a compact-overlap
certification route.

Replacing the full post-cell `atom(23)` block and the full smooth suffix block by Arb
compact-overlap matrices, while leaving `W_inf` and the old atoms on the current grid, gives:

```text
suffix compressed operator-norm difference = 1.035e-07
post block operator-norm difference        = 2.287e-06
eig(H) grid direct                         = +2.493625500557e-02, +1.916392197184e-01
eig(H) Arb atom+suffix                     = +2.493715947033e-02, +1.916374111264e-01
eig(H) shift                               = +9.045e-07, -1.809e-06
```

## 8. W_inf Cutoff And Tail

The witness

```text
scripts/numerics/witness/prime_defect_t1_winf_tail.py
```

uses the closed transform identity

```text
phihat_c(t) =
  2 cos(ct) pi^2 sin(hw t) / (t (pi^2 - hw^2 t^2))
```

with removable singularities. Therefore `phihat_c(t)=O(t^-3)`, and the `W_inf` tail has an
absolute `t^-6 log(t)` envelope.

Selected ambient entries show that the default `T=250` trapezoid is not entrywise certificate
accurate:

```text
entry (24,24): default - T1500 = -1.697e-06
entry (23,24): default - T1500 = -3.728e-07
entry (22,24): default - T1500 = -5.139e-07
entry (0,0):   default - T1500 = -2.051e-06
```

For these selected entries, the `T=1500` finite interval integral is already Arb-backed:

```text
max selected Arb radius at T=1500 <= 1.8e-24
Arb finite integral agrees with SciPy finite quadrature to roundoff.
```

The current conservative per-entry tail envelope is:

```text
T=1000 -> 1.558e-08
T=1500 -> 2.150e-09
T=2000 -> 5.269e-10
T=5000 -> 5.953e-12
```

The intended rigorous tail lemma is:

```text
For z = 1/4 + i t/2 and t > 0,
|Re psi(z)| <= log|z| + 1/(2|z|) + 1/(3t) <= log(t+1)+1.
```

Sketch: use the standard representation

```text
psi(z) = log z - 1/(2z)
         - 2 int_0^infty u / ((u^2+z^2)(e^{2 pi u}-1)) du
```

valid for `|arg z|<pi`. With `z=x+iy`, `x=1/4`, `y=t/2`,

```text
|u^2+z^2|^2 = (u^2+x^2-y^2)^2 + 4x^2y^2 >= 4x^2y^2,
```

so `|u^2+z^2| >= 2xy = t/4`. Also

```text
int_0^infty u/(e^{2 pi u}-1) du = 1/24.
```

Therefore the integral term has absolute value at most `1/(3t)`.

Together with

```text
|phihat_c(t)| <= 2 pi^2 / (t (hw^2 t^2 - pi^2)),  t > pi/hw,
```

this gives the absolute tail envelope used by the witness.

Replacing the whole ambient `W_inf` block by vector-valued finite quadrature and recomputing the
post-cell endpoint gives:

```text
T=250:  eigmin(H)=+2.487792096097e-02
T=500:  eigmin(H)=+2.513043634729e-02
T=1000: eigmin(H)=+2.513431252345e-02
T=1500: eigmin(H)=+2.513451932352e-02
```

The longer-cutoff `W_inf` improves the endpoint by about `+1.983e-04` in `eigmin(H)`. This is not
yet a rigorous enclosure, but it says the default `T=250` truncation is not hiding a failure.

The absolute tail bound must be propagated through the compressed basis. With the current `B`
matrix:

```text
max_i,j ||B_i||_1 ||B_j||_1 = 2.759e+02
||B||_2^2 ambient_dim        = 3.687e+02

T=1500 compressed entry tail <= 5.930e-07
T=5000 compressed entry tail <= 1.642e-09
```

Thus `T=1500` is too loose for the conservative raw post-block entry budget, but `T=5000` is in
range. The full-matrix Arb finite integral at `T=5000` gives:

```text
max |W_arb_finite - W_default| = 2.051e-06
per-entry ambient tail envelope = 5.953e-12
eig(H) = +2.513438064964e-02, +1.918095703870e-01
delta eig(H) from default = +1.981e-04, +1.704e-04
```

Combining the `T=5000` Arb finite `W_inf` matrix with the Arb `atom(23)` and Arb smooth suffix
matrices gives the current best partial-certificate endpoint:

```text
component mode = Arb W_inf finite + Arb atom(23) + Arb smooth suffix
eig(H) = +2.513528421043e-02, +1.918077628772e-01
delta eig(H) from default = +1.990e-04, +1.685e-04
```

Replacing the old exact atoms below `3.00` by compact-overlap Arb atom matrices as well gives the
current all-arithmetic Arb midpoint endpoint:

```text
component mode = Arb W_inf finite + Arb old atoms + Arb atom(23) + Arb smooth suffix
eig(H) = +2.511097945288e-02, +1.918391507057e-01
delta eig(H) from default = +1.747e-04, +1.999e-04
```

## 9. Remaining certification gap

The current numbers are not yet a proof. The next task is to bound all floating-point and quadrature
construction errors entering the direct post-cell Schur endpoint. The least brittle endpoint should
certify only:

```text
A_+ > 0,
H_11 > 0 and det(H) > 0,
or equivalently H > 0 by interval Schur computation.
```

The remaining hard pieces are:

```text
- write the W_inf tail lemma as a formal interval/rational bound with the chosen T;
- propagate Arb radii and finite-tail enclosures through the direct Schur computation;
- enclose the nested L2 basis/projection map or use a rationalized fixed basis with verified Gram
  error.
```

The KKT and edge-cone work remains relevant for T2/T3: it explains why `H>0` is plausible and gives
a fallback sector certificate if whole-shell positivity stops holding in a broader finite tower.
