# G - Prime-Toeplitz / passive-scattering substitute for the missing finite ground

Proof-program extraction: `research/work/H-proof-program.md`.

2026-06-09. Continuation of the #4 move: seek a noncommutative / spectral replacement for the
finite ground at infinity, not by adding a finite residue field to `Q`, but by proving an analytic
contractivity theorem coupling the prime boundary to the archimedean/Sonin space.

Update after `scripts/numerics/witness/prime_carleson_flow.py`: the naive "Carleson measure"
language is too positive. In the actual pole-killed Weil convention, writing `g = h * h#`, the prime
term is a translation/correlation operator

```text
g(log n) = <h, tau_{log n} h>,
```

not a point-evaluation square `|h(log n)|^2`. The live object is therefore a Toeplitz/scattering
domination statement with indefinite ordered jumps, not an ordinary positive sampling theorem.

## 1. Candidate theorem

On the Sonin / pole-killed test space, write the Weil form as

```text
W(h) = W_infty(h) - W_primes(h).
```

For positive-type `g = h * h#`, the prime part is

```text
W_primes(h) = 2 sum_{n>=2} Lambda(n) / sqrt(n) <h, tau_{log n} h>.
```

The proposed substitute for the finite ground is:

```text
Prime-Toeplitz theorem:
  T_Lambda := 2 sum_{n>=2} Lambda(n) / sqrt(n) tau_{log n}
  is dominated by the archimedean Sonin form on the pole-killed space:

      T_Lambda <= A_infty.
```

If this is proved from a C*/Toeplitz/Cuntz-Pimsner, passive-scattering, or canonical-system
construction, it gives Weil positivity and hence RH.

This does not pretend that infinity has finite characteristic. It replaces the missing finite
constant field by a contractive boundary representation of the Euler product inside the archimedean
space. A true Carleson/sampling factorization may still exist, but it would have to be a theorem
which factors the Toeplitz operator; it is not the starting form.

## 2. Why this is not the old prime-reflection dead end

`research/work/B-prime-reflection.md` closed the simple OS/reflection idea:

- each prime block is already a Gram block because `Lambda(n) >= 0`;
- the only prime "reflection" is the Euler product itself;
- this discriminates zeta from Davenport-Heilbronn, but adds no forcing.

The present target is stronger. It does not ask for positivity of the prime block alone. It asks for
the cross-place domination

```text
W_primes <= W_infty.
```

That is the exact place where the missing Hodge-index inequality should appear.

## 3. Finite-dimensional evidence

Using `scripts.numerics.witness.semilocal_2`, project compactly supported raised-cosine test
functions onto the pole-killed Sonin constraints. For each support edge `gmax`, compute:

- `Q_zeta = W_infty - P_zeta`;
- `Q_DH = W_infty - P_DH`, with DH log-derivative coefficients;
- the generalized Carleson constant `lambda_max(P_zeta, W_infty)`.

Observed pattern:

```text
support edge      zeta min eig      DH min eig        verdict
gmax ~ 1.00       +4.9e-05          +4.7e-05          both PSD
gmax ~ 1.56       +2.3e-05          +1.2e-03          both PSD
gmax ~ 1.80       +3e-05            -1e-02 to -2e-02  DH breaks
gmax ~ 1.96       +6e-05            -5e-02            DH breaks robustly
```

The onset is robust across bases:

```text
ncen=9,  hw=0.18: DH breaks near gmax=1.84
ncen=13, hw=0.14: DH breaks near gmax=1.76
ncen=17, hw=0.10: DH breaks near gmax=1.80
```

Meanwhile the zeta Carleson constant approaches the critical value from below:

```text
gmax=1.32: lambda_max ~ 0.93
gmax=1.44: lambda_max ~ 0.998
gmax=1.56: lambda_max ~ 0.9999
```

This is the expected knife-edge behavior for an RH-equivalent inequality: the margin becomes tiny, but
the zeta form stays positive in the tested finite windows, while DH eventually goes indefinite once
enough prime-power data enter.

The flow diagnostic sharpens this. In a pole-killed window with `ncenters=13`, `hw=0.14`,
`gmax=1.88`, zeta behaves as follows:

```text
start W_infty min eig: +7.26e-04
after n=2:              -8.49e-02
after n=3:              -3.27e-02
after n=4:              -1.44e-02
after n=5:              +3.56e-05
```

So the first prime does not simply fit under the archimedean margin. It overdraws it, and later
prime powers repair the margin by indefinite Toeplitz interference. The DH coefficients in the same
window send the wrong repairs:

```text
DH final min eig:       -4.06e-02
```

A second window (`ncenters=17`, `hw=0.10`, `gmax=2.10`) shows the same pattern: zeta ends at
`+2.28e-05`, while DH ends at `-5.67e-02`.

Eigenvector localization supports the "repair" reading. In the larger zeta window, the `n=5` jump
raises the minimum eigenvalue by `+8.70e-02`; its Rayleigh value on the current bad vector is
`-1.07e-01`, and the bad vector has alignment `0.817` with the negative eigenvector of that jump.
So the repairing prime is acting directly on the current obstruction direction, not merely changing
some unrelated part of the matrix. In the smaller window the repairs at `n=3,4,5` show the same
negative-Rayleigh behavior, with the final `n=5` jump closing the gap to `+3.56e-05`.

The first basis-refinement check is also positive. Keep the support edge fixed at `gmax=1.88` and
refine the raised-cosine basis:

```text
ncenters=13, hw=0.14, cmax=0.80: final min +3.56e-05
ncenters=17, hw=0.10, cmax=0.84: final min +4.76e-05
ncenters=21, hw=0.08, cmax=0.86: final min +4.19e-05
```

Projecting the `n=5` repair data back to physical/Fourier test-function shapes, adjacent
refinements have the following absolute `L2` correlations:

```text
pair                         bad vector   atom negative direction   final near-null
n13/hw0.14 -> n17/hw0.10     0.957        0.806                     0.826
n17/hw0.10 -> n21/hw0.08     0.990        0.984                     0.963
```

This is the strongest evidence so far that the `n=5` repair is seeing a stable boundary mode rather
than a discretization artifact.

However, growing the support edge shows that this is not one fixed global vector. With
`ncenters=17`, `hw=0.10`, and increasing `cmax`, the final near-null mode and dominant repair behave
like a relay:

```text
gmax pair     final-mode corr   dominant repair   repair-bad corr   repair-atom corr
1.60 -> 1.72  1.000             n3 -> n3          0.994             0.946
1.72 -> 1.88  0.840             n3 -> n3          0.998             0.912
1.88 -> 2.10  0.392             n3 -> n5          0.233             0.472
2.10 -> 2.30  0.436             n5 -> n7          0.412             0.260
2.30 -> 2.52  0.501             n7 -> n7          0.719             0.868
```

So the better model is not "one null mode transported forever." It is an ordered sequence of local
obstruction modes, with handoffs when new prime powers enter. This pushes the candidate further
toward a transfer-matrix / canonical-system picture: each Euler jump changes the active boundary
mode, and the exact coefficient pattern keeps the resulting product passive.

The DH comparison over the same growing windows is now sharper:

```text
gmax   zeta final / dominant repair       DH final / dominant repair
1.60   +2.02e-05 / n3  d=+5.99e-02        +4.16e-04 / none
1.72   +1.68e-05 / n3  d=+4.92e-02        +6.13e-04 / none
1.88   +4.76e-05 / n3  d=+3.04e-02        -3.62e-02 / none
2.10   +2.28e-05 / n5  d=+8.70e-02        -5.67e-02 / n2 d=+1.55e-02
2.30   +1.28e-04 / n7  d=+5.07e-02        -7.69e-02 / n2 d=+4.18e-02
2.52   +1.24e-04 / n7  d=+7.20e-02        -2.22e-01 / n2 d=+5.09e-02
```

DH is not merely "less positive." It lacks the zeta relay: before failure it has no dominant repair
at all, and after failure its repairs stay anchored at `n=2` while the margin remains negative. This
is a much better kill-test signature for the Prime-Toeplitz target than the earlier semilocal
`{infinity,2}` test.

The finite handoff matrices are now explicit. For each zeta stage, take the two active channel
vectors

```text
[incoming bad vector, jump-negative vector],
```

reconstruct them as physical test functions, `L2`-orthonormalize them, and project the next active
channel onto the previous one. At the two observed handoffs:

```text
gmax 1.88 -> 2.10, n3 -> n5:
  [[+0.233, +0.118],
   [-0.040, +0.623]]
  singular values: [0.634, 0.236]

gmax 2.10 -> 2.30, n5 -> n7:
  [[+0.412, -0.405],
   [-0.155, +0.719]]
  singular values: [0.899, 0.260]
```

These are not proof objects yet, but they are finite transfer matrices between the active local
obstruction channels. The projected transmission is `L2`-contractive in both handoffs.

The stronger sign test is the final Weil form restricted to each local active channel. Use a
four-vector channel when a repair exists,

```text
[incoming bad, jump-negative, outgoing bad, final near-null],
```

orthonormalized in physical `L2`; if no repair exists, use the final bad vector. Then:

```text
gmax   zeta active-channel eigs      DH active-channel eigs
1.60   n3  [+4.89e-05,+1.76e+00]     none [+2.09e+00,+2.09e+00]
1.72   n3  [+4.42e-05,+1.90e+00]     none [+4.87e-02,+4.87e-02]
1.88   n3  [+1.30e-04,+1.82e+00]     none [-1.06e-01,-1.06e-01]
2.10   n5  [+8.64e-05,+1.87e+00]     n2   [-1.73e-01,+1.94e+00]
2.30   n7  [+4.59e-04,+2.67e+00]     n2   [-2.96e-01,+1.35e+00]
2.52   n7  [+5.89e-04,+2.44e+00]     n2   [-9.96e-01,+1.69e+00]
```

This is the cleanest finite form of the new target: zeta's relay channels remain passive/positive;
DH's corresponding active channels become indefinite exactly when the relay test reaches the failing
windows.

## 4. Geometric object emerging

The right geometric abstraction is not a new space with a fake finite residue field. It is a
finite-dimensional shadow of a singular metric bundle over the support edge `L`.

```text
base:      support edge L
fiber:     active channel C_L = span(incoming bad, jump-negative)
metric:    J_L = local post-jump Weil energy on C_L
background h_L: physical L2 metric on C_L
connection: projection/transport T_{L -> L'} between adjacent active channels
singularities: prime-power jumps L = log n
```

The naive metric condition

```text
J_L - T^* J_{L'} T >= 0
```

is close but false. That is important: a pure Riemannian metric tensor on the active bundle is the
wrong abstraction. The better finite condition is

```text
J_L + lambda h_L - T^*(J_{L'} + lambda h_{L'})T >= 0,
```

where `h_L` is the ambient `L2` capacity of the fiber. Numerically, for zeta:

```text
edge          repair     raw defect eigs          min lambda
1.60 -> 1.72 n3 -> n3    [+1.25e-03,+2.76e-02]   0
1.72 -> 1.88 n3 -> n3    [-4.14e-03,+3.46e-01]   0.929
1.88 -> 2.10 n3 -> n5    [+9.37e-03,+1.11e+00]   0
2.10 -> 2.30 n5 -> n7    [-2.07e-01,+9.15e-01]   0.493
2.30 -> 2.52 n7 -> n7    [-9.71e-02,+1.19e+00]   0.270
```

So the candidate geometry is a bundle with two coupled tensors:

```text
energy metric J_L  +  ambient capacity metric lambda h_L.
```

This is closer to a passive system / Hermitian bundle with dissipation than to a bare Hodge metric.
The prime powers are singular connection defects, and the Euler coefficients are the point
interactions that keep the total connection passive.

The right Chern-Simons-like object is a log-determinant transgression of this metric pair, not an
ordinary Chern-Simons 3-form. For a handoff connection `T: C_L -> C_{L'}` and

```text
G_L(lambda) = J_L + lambda h_L,
```

define

```text
Tau_L(lambda)
  =
  log det G_L(lambda)
  -
  log det(T^* G_{L'}(lambda) T).
```

Equivalently,

```text
Tau_L(lambda)
  =
  [log det G_L(lambda) - log det G_{L'}(lambda)]
  -
  2 log |det T|.
```

The first bracket is the metric-volume anomaly; the second term is connection-volume loss. This is a
navigation functional, not a proof by itself: determinant positivity is weaker than Loewner
positivity, so it must be read together with the defect

```text
G_L(lambda) - T^*G_{L'}(lambda)T >= 0.
```

At the fitted `lambda` values for zeta:

```text
edge          repair     lambda   Tau(lambda)   metric anomaly   connection loss
1.60 -> 1.72 n3 -> n3    0        +0.074        -0.060           +0.135
1.72 -> 1.88 n3 -> n3    0.929    +0.220        -0.012           +0.232
1.88 -> 2.10 n3 -> n5    0        +3.644        -0.152           +3.797
2.10 -> 2.30 n5 -> n7    0.493    +2.577        -0.332           +2.909
2.30 -> 2.52 n7 -> n7    0.270    +1.525        +0.235           +1.290
```

The big positive transgression at the actual handoffs is mostly connection-volume loss, exactly what
a dissipative singular connection should show. On DH's own active channels the anomaly already
degenerates in the later window because the metric is no longer positive definite, so `log det` stops
being a real positive-metric invariant. That is a useful failure mode, not an inconvenience.

Stress testing gives a more qualified picture. Extending the support sweep with the same
`ncenters=17`, `hw=0.10` discretization:

```text
edge          repair      lambda   Tau(lambda)
1.60 -> 1.72 n3 -> n3     0        +0.074
1.72 -> 1.88 n3 -> n3     0.929    +0.220
1.88 -> 2.10 n3 -> n5     0        +3.644
2.10 -> 2.30 n5 -> n7     0.493    +2.577
2.30 -> 2.52 n7 -> n7     0.270    +1.525
2.52 -> 2.76 n7 -> n7     4.71     +1.006
2.76 -> 3.00 n7 -> n13    0.145    +2.796
3.00 -> 3.24 n13 -> n19   0        +3.520
```

The good news is that `Tau` stays positive and new prime handoffs (`n7 -> n13`, `n13 -> n19`) look
like genuine dissipative events. The warning is the `lambda=4.71` spike on the non-handoff
`n7 -> n7` segment. That means the metric-pair idea has not yet stabilized globally; either the
active-channel choice is too narrow there, or the ambient capacity metric is missing a term.

Basis refinement also separates robust behavior from artifacts:

```text
edge 1.88 -> 2.10:
  n=13, hw=0.14: n3 -> n5, lambda 0.0368, Tau +3.816
  n=17, hw=0.10: n3 -> n5, lambda 0,      Tau +3.644
  n=21, hw=0.08: n5 -> n5, lambda 0.0705, Tau +0.853
  n=25, hw=0.06: n5 -> n5, lambda 0.0833, Tau +0.419

edge 2.10 -> 2.30:
  n=13, hw=0.14: n5 -> n5, lambda 0.630, Tau +0.131
  n=17, hw=0.10: n5 -> n7, lambda 0.493, Tau +2.577
  n=21, hw=0.08: n5 -> n7, lambda 0.432, Tau +2.486
  n=25, hw=0.06: n5 -> n7, lambda 0.115, Tau +2.378
```

Interpretation: the `n5 -> n7` handoff is stable under refinement; the earlier `n3 -> n5` handoff is
less stable because finer bases already make `n5` active on both sides. So the target should not be
formulated around a literal `n3 -> n5 -> n7` sequence. The more invariant object is:

```text
active fiber changes when the dominant repairing prime changes under refinement;
true handoffs are the stable changes of active prime label.
```

The current robust test case is therefore `n5 -> n7`, with later `n7 -> n13` and `n13 -> n19` as the
next candidates.

Trying to remove the late `lambda` spike by widening the local fiber does **not** work:

```text
rank 2: [incoming bad, jump-negative]
rank 3: rank 2 + outgoing bad
rank 4: rank 3 + final near-null

edge 2.52 -> 2.76, n7 -> n7:
  rank 2: lambda 4.71, Tau +1.006
  rank 3: lambda 5.54, Tau +6.924
  rank 4: lambda 5.11, Tau +3.703
```

So the spike is not just a missing vector in the fiber. The better reading is geometric: `n7 -> n7`
is not a singular handoff, it is a same-label drift segment of the active subbundle. The raw
connection is nearly an isometry there, so `I - T^*T` is small; a modest negative energy drift then
requires a large scalar `lambda` if we force it into the singular-jump inequality. This means the
bundle model must split:

```text
continuous part: metric drift / second fundamental form of C_L over L
singular part:   prime-power handoff connections when the active label changes
```

The Chern-Simons/Bott-Chern-like transgression should therefore be used in two modes:

```text
same-label segments:  curvature / metric-variation density
label-changing jumps: dissipative singular transgression
```

This is good news for abstraction discipline: the spike is telling us not to treat every finite
support increment as the same kind of geometric event.

With this split, the stress witness reads:

```text
same-label drift edges, densities per dL:
edge          repair    lambda   Tau/dL   metric/dL   connection/dL
1.60 -> 1.72 n3 -> n3   0        +0.618   -0.504      +1.122
1.72 -> 1.88 n3 -> n3   0.929    +1.375   -0.074      +1.449
2.30 -> 2.52 n7 -> n7   0.270    +6.932   +1.069      +5.863
2.52 -> 2.76 n7 -> n7   4.71     +4.193   +0.291      +3.902

label-changing jumps:
edge          repair     lambda   Tau      metric      connection
1.88 -> 2.10 n3 -> n5    0        +3.644   -0.152      +3.797
2.10 -> 2.30 n5 -> n7    0.493    +2.577   -0.332      +2.909
2.76 -> 3.00 n7 -> n13   0.145    +2.796   -0.914      +3.711
3.00 -> 3.24 n13 -> n19  0        +3.520   -0.044      +3.564
```

The label-changing jumps are the finite Bott-Chern/CS-like defects. The same-label rows are
curvature density of the active subbundle. The large `lambda` at `2.52 -> 2.76` is now correctly
classified as a drift issue: connection-volume density is high while the active label does not
change. That points to a missing continuous curvature term, not a failed prime jump.

The same-label drift geometry confirms this. For adjacent active fibers, compute the principal
angles in ambient physical `L2`. A crude second-fundamental-form proxy is

```text
||theta|| / dL       or       ||sin(theta)|| / dL.
```

The stress witness gives:

```text
edge          label   singular values   ||theta||/dL   ||sin theta||/dL   conn/dL   conn/sin^2
1.60 -> 1.72 n3      [0.999,0.936]     3.024          2.960              1.122     0.128
1.72 -> 1.88 n3      [0.999,0.892]     2.953          2.848              1.449     0.179
2.30 -> 2.52 n7      [0.924,0.568]     4.743          4.125              5.863     0.345
2.52 -> 2.76 n7      [0.995,0.629]     3.732          3.264              3.902     0.366
```

So the same-label active subbundle is not flat. The late `n7` plateau has large principal-angle
density and large connection-volume density. In geometric terms, the active channel is bending
inside the ambient Sonin space; the transgression spike is measuring this continuous curvature, not
an Euler point interaction. The ratio `connection/dL / ||sin(theta)||^2` is more stable within a
label plateau than across labels: roughly `0.13-0.18` for `n3`, and `0.35-0.37` for `n7`. That
suggests a label-dependent curvature coefficient rather than arbitrary numerical drift.

The next invariantization is now in `scripts/numerics/witness/prime_global_bundle.py`. Instead of
using the dominant repair label to define the fiber, define the active bundle intrinsically:

```text
M_L = W_infty,L - P_L                         final pole-killed margin
E_L = span of the two lowest eigenvectors of M_L
J_L = M_L restricted to E_L
h_L = physical L2 metric on E_L
T_{L -> L'} = ambient L2 projection E_L -> E_{L'}
```

The repair label is then only a landmark, not part of the definition. This matters because the
earlier `n3 -> n5 -> n7` story is basis-sensitive at the first handoff; the bottom spectral subspace
is the invariant finite object.

The intrinsic fiber test keeps the zeta metric inside the positive cone through the longer sweep:

```text
gmax   zeta repair   final min    zeta J eig range
1.60   n3            +2.02e-05    [+4.89e-05,+9.70e-02]
1.72   n3            +1.68e-05    [+4.39e-05,+1.05e-04]
1.88   n3            +4.76e-05    [+1.30e-04,+2.97e-04]
2.10   n5            +2.28e-05    [+8.62e-05,+2.21e-04]
2.30   n7            +1.28e-04    [+4.59e-04,+5.47e-04]
2.52   n7            +1.24e-04    [+5.53e-04,+1.17e-03]
2.76   n7            +1.25e-04    [+5.93e-04,+8.69e-04]
3.00   n13           +1.87e-04    [+9.00e-04,+1.28e-03]
3.24   n19           +2.40e-04    [+1.18e-03,+2.72e-03]
```

DH exits the positive cone exactly where the earlier relay test says it should:

```text
gmax   DH repair     final min    DH J eig range
1.60   none          +4.16e-04    [+1.88e+00,+2.41e+00]
1.72   none          +6.13e-04    [+2.04e-02,+2.28e+00]
1.88   none          -3.62e-02    [-1.07e-01,+2.18e+00]
2.10   n2            -5.67e-02    [-1.73e-01,+6.65e-01]
2.30   n2            -7.69e-02    [-2.89e-01,+1.33e-01]
2.52   n2            -2.22e-01    [-1.02e+00,-6.75e-02]
2.76   n2            -3.68e-01    [-1.60e+00,-4.44e-01]
3.00   n2            -3.49e-01    [-1.61e+00,-1.49e+00]
3.24   n2            -3.27e-01    [-1.60e+00,-1.59e+00]
```

So the clean global discriminator is not the size of the log-det action alone. It is:

```text
zeta: E_L carries a positive Hermitian metric J_L throughout the tested path;
DH:   the intrinsic bottom metric becomes indefinite and then negative definite.
```

The intrinsic connection still sees the prime relay as landmarks:

```text
zeta edge      landmarks     svals          lambda(def,spd)   Tau      connection
1.60 -> 1.72  n3 -> n3      [1.000,0.976]  (0,0)             +6.984   +0.049
1.72 -> 1.88  n3 -> n3      [1.000,0.645]  (1.35,0)          +0.876   +0.877
1.88 -> 2.10  n3 -> n5      [0.974,0.561]  (0,0)             +1.911   +1.208
2.10 -> 2.30  n5 -> n7      [0.936,0.477]  (0.00183,0)       +1.288   +1.613
2.30 -> 2.52  n7 -> n7      [0.824,0.348]  (0.000238,0)      +1.788   +2.501
2.52 -> 2.76  n7 -> n7      [0.397,0.226]  (0,0)             +5.056   +4.826
2.76 -> 3.00  n7 -> n13     [0.533,0.332]  (0,0)             +2.658   +3.465
3.00 -> 3.24  n13 -> n19    [0.131,0.035]  (0,0)             +9.757   +10.777
```

The high `Tau` at `1.60 -> 1.72` is mostly metric-volume collapse inside the bottom two-plane; it is
not a prime jump. The actual label-changing edges are again dominated by connection-volume loss.
This reinforces the split:

```text
continuous geometry: changing low spectral subspace E_L and metric-volume drift;
singular geometry:   Euler point interactions where the repair landmark changes.
```

The cumulative intrinsic path action over `gmax=1.60..3.24` is:

```text
kind   sum Tau   metric part   connection part   max lambda   orientation product
zeta   +30.319   +5.002        +25.316           1.35         +1
DH     +143.305  +121.145      +22.160           2.72         -1
```

The DH total is not good news for DH. Most of it is the artificial positive shift needed to make an
indefinite/negative metric admit a log determinant. The orientation flip is another finite warning
that the bottom bundle is no longer carrying the same positive Hermitian structure.

Stress testing in `scripts/numerics/witness/prime_global_bundle_stress.py` gives the next correction.
The stable invariant is positive-cone membership, not the absolute magnitude of `Tau`.

Across bottom spectral ranks `1..4` with the same `ncenters=17`, `hw=0.10` support sweep:

```text
kind   rank   min J eig over path   first bad L   sum Tau   max lambda
zeta   1      +4.42e-05             none          +15.162   0.000161
zeta   2      +4.39e-05             none          +30.319   1.35
zeta   3      +4.39e-05             none          +39.212   1.91
zeta   4      +4.39e-05             none          +55.198   2.77
DH     1      -1.60e+00             1.88          +132.709  1.60
DH     2      -1.61e+00             1.88          +143.305  2.72
DH     3      -1.61e+00             1.88          +158.910  3.38
DH     4      -1.61e+00             1.88          +96.628   3.43
```

So the rank choice is not what separates zeta from DH. Zeta remains positive on the tested bottom
spectral flags; DH leaves the positive cone at `gmax=1.88` for every tested rank.

Basis refinement gives a more sober message. At fixed support edge, the first overlap singular value
between adjacent refinements is often near `1`, but the second direction can rotate badly when the
spectral gap is tiny:

```text
zeta same-edge rank-2 overlap examples:
gmax 1.88:  [1.000,0.883], [1.000,0.735], [1.000,0.796]
gmax 2.10:  [1.000,0.296], [1.000,0.706], [0.991,0.055]
gmax 2.76:  [0.650,0.054], [0.654,0.260], [0.806,0.300]
gmax 3.00:  [0.905,0.138], [0.959,0.406], [0.838,0.077]
```

The edge transgressions also change size under refinement:

```text
zeta edge 1.88 -> 2.10: Tau +0.382, +1.911, +4.244, +2.951
zeta edge 2.10 -> 2.30: Tau +8.491, +1.288, +3.262, +2.576
zeta edge 2.52 -> 2.76: Tau +1.234, +5.056, +5.327, +5.998
zeta edge 2.76 -> 3.00: Tau +7.392, +2.658, +6.690, +3.366
```

This does not kill the geometric picture, but it changes what should be claimed. A finite bottom
two-plane is an obstruction microscope, not a canonical proof object. The proof target must be the
full metric-pair flow on the Sonin/pole-killed space:

```text
continuous archimedean drift + Euler Toeplitz point interactions preserve the positive cone
```

The spectral bundle `E_L` is then a way to visualize the lowest-energy obstruction and the local
failure mode for DH. It should not appear as a load-bearing definition in a noncircular proof,
because `E_L` is extracted from `M_L`, whose positivity is exactly the issue.

The full finite-rank test in `scripts/numerics/witness/prime_full_flow_metric.py` confirms this
priority. Use the entire pole-killed finite window as the fiber:

```text
H_L = full pole-killed raised-cosine window
J_L = M_L restricted to H_L and L2-orthonormalized
```

With `ncenters=17`, `hw=0.10`, the full zeta fibers remain positive:

```text
gmax   dim   repair   zeta full J eig range
1.60   15    n3       [+4.89e-05,+3.10e+00]
1.72   15    n3       [+4.39e-05,+3.04e+00]
1.88   15    n3       [+1.30e-04,+2.99e+00]
2.10   15    n5       [+8.59e-05,+3.25e+00]
2.30   15    n7       [+4.59e-04,+2.92e+00]
2.52   15    n7       [+5.39e-04,+3.01e+00]
2.76   15    n7       [+5.89e-04,+3.20e+00]
3.00   15    n13      [+8.99e-04,+3.56e+00]
3.24   15    n19      [+1.17e-03,+3.49e+00]
```

DH leaves the full positive cone at the same place as the local/spectral witnesses:

```text
gmax   dim   repair   DH full J eig range
1.60   15    none     [+1.37e-01,+2.75e+00]
1.72   15    none     [+1.16e-02,+2.68e+00]
1.88   15    none     [-1.12e-01,+2.80e+00]
2.10   15    n2       [-1.74e-01,+2.85e+00]
2.30   15    n2       [-3.04e-01,+3.23e+00]
2.52   15    n2       [-1.05e+00,+3.38e+00]
2.76   15    n2       [-1.60e+00,+3.15e+00]
3.00   15    n2       [-1.61e+00,+3.34e+00]
3.24   15    n2       [-1.60e+00,+3.30e+00]
```

Basis refinement preserves this separation without selecting any obstruction subspace:

```text
zeta, full finite window:
gmax 1.88: min eig +7.28e-05, +1.30e-04, +1.45e-04, +2.13e-04
gmax 2.10: min eig +1.41e-04, +8.59e-05, +1.16e-04, +2.26e-04
gmax 2.30: min eig +1.06e-04, +4.59e-04, +2.30e-04, +1.13e-03
gmax 2.76: min eig +6.60e-04, +5.89e-04, +4.67e-04, +1.33e-03
gmax 3.00: min eig +2.48e-04, +8.99e-04, +1.08e-03, +2.02e-03

DH, full finite window:
gmax 1.88: min eig -1.02e-01, -1.12e-01, -1.20e-01, -1.30e-01
gmax 2.10: min eig -1.72e-01, -1.74e-01, -1.76e-01, -1.78e-01
gmax 2.30: min eig -2.63e-01, -3.04e-01, -3.15e-01, -3.23e-01
gmax 2.76: min eig -1.59e+00, -1.60e+00, -1.60e+00, -1.60e+00
gmax 3.00: min eig -1.61e+00, -1.61e+00, -1.61e+00, -1.60e+00
```

This is now the cleanest finite formulation of the target: no active channel, no bottom eigenbundle,
no handpicked repair vector. Just the full pole-killed finite margin.

The full-rank connection/transgression data, however, is not the right invariant. Adjacent full
windows have very small projection singular values:

```text
zeta full-fiber min singular values:
1.60 -> 1.72: 8.89e-02
1.72 -> 1.88: 4.10e-02
1.88 -> 2.10: 1.78e-03
2.10 -> 2.30: 1.91e-03
2.30 -> 2.52: 1.04e-03
2.52 -> 2.76: 9.01e-04
2.76 -> 3.00: 5.06e-04
3.00 -> 3.24: 2.15e-04
```

Consequently the full determinant transgression is dominated by projection-volume artifacts and
requires huge fitted backgrounds. That is not the Chern-Simons object we want. The determinant
functional is meaningful after choosing a controlled low-dimensional channel; the full theorem
should be Loewner/positive-cone preservation.

The best finite formulation so far is the nested-cone witness
`scripts/numerics/witness/prime_nested_cone.py`. Instead of rebuilding the basis at each support
edge, fix one ambient raised-cosine window and define

```text
H_L = span of ambient bumps with c + hw <= L/2, then impose the pole-killing constraints.
```

Then `H_L` is literally a subspace of `H_{L'}` for `L < L'`. This turns support growth into a
positive extension problem rather than a comparison between unrelated finite models.

In one ambient window (`ncenters=25`, `hw=0.06`, `gmax=3.24`), zeta stays positive on the nested
full cones:

```text
L      dim   active n                         zeta J eig range
1.60   10    2,3,4                            [+3.25e-02,+2.47e+00]
1.72   11    2,3,4,5                          [+3.21e-02,+2.48e+00]
1.88   12    2,3,4,5                          [+2.97e-02,+2.49e+00]
2.10   14    2,3,4,5,7,8                      [+2.13e-02,+2.62e+00]
2.30   15    2,3,4,5,7,8,9                    [+1.49e-02,+2.76e+00]
2.52   17    2,3,4,5,7,8,9,11                 [+5.66e-03,+2.92e+00]
2.76   19    2,3,4,5,7,8,9,11,13              [+4.20e-03,+3.55e+00]
3.00   21    2,3,4,5,7,8,9,11,13,16,17,19     [+3.93e-03,+3.71e+00]
3.24   23    2,3,4,5,7,8,9,11,13,16,17,19,23,25 [+2.02e-03,+3.76e+00]
```

DH exits the same nested cone at the expected support:

```text
L      dim   active n                         DH J eig range
1.60   10    2,3,4                            [+1.75e-01,+2.11e+00]
1.72   11    2,3,4                            [+4.19e-02,+2.36e+00]
1.88   12    2,3,4,6                          [-6.99e-02,+2.56e+00]
2.10   14    2,3,4,6,7,8                      [-1.52e-01,+3.05e+00]
2.30   15    2,3,4,6,7,8,9                    [-2.14e-01,+3.05e+00]
2.52   17    2,3,4,6,7,8,9,11,12              [-9.20e-01,+3.32e+00]
2.76   19    2,3,4,6,7,8,9,11,12,13,14        [-1.57e+00,+3.80e+00]
3.00   21    2,3,4,6,7,8,9,11,12,13,14,16,17,18,19 [-1.59e+00,+3.85e+00]
3.24   23    2,3,4,6,7,8,9,11,12,13,14,16,17,18,19,21,23,24 [-1.59e+00,+4.25e+00]
```

The decisive new data are the Schur complements for the shell extension

```text
H_{L'} = H_L  +  shell.
```

For zeta:

```text
edge          dim       new active n   right min   shell min   Schur min
1.60 -> 1.72 10 -> 11   5              +3.21e-02   +9.12e-01   +3.32e-01
1.72 -> 1.88 11 -> 12   none           +2.97e-02   +1.57e+00   +2.70e-01
1.88 -> 2.10 12 -> 14   7,8            +2.13e-02   +3.44e-01   +7.82e-02
2.10 -> 2.30 14 -> 15   9              +1.49e-02   +1.21e+00   +1.52e-01
2.30 -> 2.52 15 -> 17   11             +5.66e-03   +8.33e-01   +4.81e-02
2.52 -> 2.76 17 -> 19   13             +4.20e-03   +6.79e-01   +2.92e-02
2.76 -> 3.00 19 -> 21   16,17,19       +3.93e-03   +4.02e-01   +6.34e-02
3.00 -> 3.24 21 -> 23   23,25          +2.02e-03   +8.18e-01   +2.74e-02
```

For DH, the first bad extension is already visible before the old block has failed:

```text
edge          dim       new active n   right min   shell min   Schur min
1.60 -> 1.72 10 -> 11   none           +4.19e-02   +1.23e+00   +1.78e-01
1.72 -> 1.88 11 -> 12   6              -6.99e-02   +1.34e+00   -1.78e+00
```

The old-subspace carry from newly active atoms is numerically tiny (`~1e-6`), as it should be:
old test functions have smaller support, so new atoms do not act on them. Positivity growth is
therefore controlled by the shell Schur complement.

This is now the best target:

```text
Nested Prime-Toeplitz extension theorem:
  For every support extension H_L ⊂ H_{L'}, the zeta Euler/Sonin shell
  has positive Schur complement in the full pole-killed Weil margin.
```

This avoids the wrong abstraction in three ways:

1. it does not fake a finite field at infinity;
2. it does not choose a low-dimensional obstruction channel as a definition;
3. it does not rely on determinant transgression in a rank-unstable full space.

The geometry is a positive-cone extension geometry. Transgression can still navigate controlled
channels, but the load-bearing proof object is the shell Schur complement.

Stress testing the nested target in `scripts/numerics/witness/prime_nested_cone_stress.py` shows that
this Schur-complement discriminator survives ambient refinement. For ambient bases ending at the same
`gmax=3.24`:

```text
kind   basis       min point eig   first bad point   min Schur   min Schur edge   first bad Schur
zeta   n17/hw0.10  +1.17e-03      none              +5.13e-03   3.00 -> 3.24    none
zeta   n21/hw0.08  +7.17e-04      none              +5.51e-03   3.00 -> 3.24    none
zeta   n25/hw0.06  +2.02e-03      none              +2.74e-02   3.00 -> 3.24    none
DH     n17/hw0.10  -1.60e+00      2.10              -4.92e+00   1.88 -> 2.10    1.88 -> 2.10
DH     n21/hw0.08  -1.61e+00      1.88              -4.74e+00   1.72 -> 1.88    1.72 -> 1.88
DH     n25/hw0.06  -1.59e+00      1.88              -1.78e+00   1.72 -> 1.88    1.72 -> 1.88
```

The coarsest grid delays the DH Schur failure by one support step, but the refined grids agree on
`1.72 -> 1.88`. Zeta stays positive in all tested ambient refinements.

The block anatomy is also clarifying. For an extension block

```text
M_{L'} =
  [ A  C ]
  [ C* D ],
```

positivity over the new shell is equivalent to

```text
D - C* A^{-1} C >= 0.
```

The first DH failures are not caused by a negative shell diagonal. The shell energy `D` is positive,
but the coupling term `C* A^{-1}C` is too large:

```text
DH failure anatomy:
edge          basis       new n   shell min   coupling max   Schur min
1.88 -> 2.10 n17/hw0.10  7,8     +8.31e-01   +5.75e+00     -4.92e+00
1.72 -> 1.88 n21/hw0.08  6       +1.12e+00   +5.86e+00     -4.74e+00
1.72 -> 1.88 n25/hw0.06  6       +1.34e+00   +3.11e+00     -1.78e+00
```

For zeta, the same comparison stays on the positive side even when the margin is narrow:

```text
zeta selected shell anatomy:
edge          basis       new n       shell min   coupling max   Schur min
1.88 -> 2.10 n17/hw0.10  7,8         +1.38e+00   +1.33e+00     +4.67e-02
2.30 -> 2.52 n21/hw0.08  11          +7.16e-01   +1.24e+00     +1.87e-02
2.76 -> 3.00 n21/hw0.08  16,17,19    +6.57e-01   +1.48e+00     +8.28e-03
```

So the theorem should not merely assert "the new shell is positive." It must prove a passive
coupling bound:

```text
C* A^{-1} C <= D.
```

This is exactly the shape of a Schur / de Branges / canonical-system extension theorem. The new
support shell may couple strongly to the old space, but for zeta the Euler/Sonin coefficients keep
that coupling below the shell energy. DH-type coefficients exceed the bound.

The direct contraction witness is `scripts/numerics/witness/prime_shell_coupling_bound.py`. Normalize
the Schur inequality by the shell energy:

```text
rho(L,L') =
  lambda_max( D^{-1/2} C^* A^{-1} C D^{-1/2} ).
```

Then

```text
C^* A^{-1} C <= D    <=>    rho(L,L') <= 1
```

whenever `A` and `D` are positive. Across the nested ambient refinements:

```text
kind   basis       max rho   max gain   max edge      min Schur   first rho > 1
zeta   n17/hw0.10  0.990     0.995      3.00 -> 3.24 +5.13e-03  none
zeta   n21/hw0.08  0.994     0.997      3.00 -> 3.24 +5.51e-03  none
zeta   n25/hw0.06  0.976     0.988      3.00 -> 3.24 +2.74e-02  none
DH     n17/hw0.10  6.919     2.630      1.88 -> 2.10 -4.92e+00  1.88 -> 2.10
DH     n21/hw0.08  5.215     2.284      1.72 -> 1.88 -4.74e+00  1.72 -> 1.88
DH     n25/hw0.06  2.331     1.527      1.72 -> 1.88 -1.78e+00  1.72 -> 1.88
```

So the finite theorem target can now be stated without determinants, handpicked channels, or
eigenbundle language:

```text
Passive Shell-Coupling Theorem:
  For every nested pole-killed Sonin support extension H_L ⊂ H_{L'},
  the Euler/Sonin margin block

      M_{L'} = [ A  C ]
               [ C* D ]

  satisfies A > 0, D > 0, and

      || A^{-1/2} C D^{-1/2} ||^2 = rho(L,L') <= 1.
```

Equivalently, every new support shell enters as a passive positive extension of the old support
window. Numerically zeta is close to critical at late edges (`rho ~ 0.99`) but remains contractive;
DH exceeds the passive bound at the first refined failing shell.

The extremal-mode witness `scripts/numerics/witness/prime_shell_coupling_modes.py` reconstructs the
right singular vector for

```text
A^{-1/2} C D^{-1/2}
```

at the largest singular value. This gives the actual finite mode a proof would have to bound. For
zeta, the near-critical modes have `D`-energy normalized to `1` and old-response `A`-energy
`rho < 1`:

```text
zeta selected extremal transfer modes:
edge          basis       new n       rho    slack      shell |u|   old |u|
1.88 -> 2.10 n17/hw0.10  7,8         0.966  +3.38e-02  0.757       0.534
2.30 -> 2.52 n21/hw0.08  11          0.978  +2.22e-02  0.966       0.687
2.76 -> 3.00 n21/hw0.08  16,17,19    0.993  +7.31e-03  1.191       0.825
3.00 -> 3.24 n21/hw0.08  23,25       0.994  +5.83e-03  1.338       1.209
```

The shell mode moves outward with support, and the old response sits inward. That is exactly the
geometry of a support-extension transfer operator.

For DH, the refined first failure is the shell where the non-Euler composite `n=6` enters:

```text
DH extremal failures:
edge          basis       new n   rho    gain   slack
1.72 -> 1.88 n21/hw0.08  6       5.215  2.284  -4.22e+00
1.72 -> 1.88 n25/hw0.06  6       2.331  1.527  -1.33e+00
```

The coarser `n17/hw0.10` grid sees the same `n=6` shell but does not fail until the next edge. The
finer grids agree that the first real obstruction is the `n=6` coupling. This is a much more
specific DH-kill signature: DH does not merely have "wrong signs"; it introduces a composite
support interaction that over-couples the shell to the old space.

The individual shell Rayleigh contributions are mixed. Zeta's extremal shell is not controlled by a
single newly-entering prime power. Earlier atoms often dominate or cancel the new shell:

```text
examples of largest shell atom Rayleighs:
zeta 2.76 -> 3.00, n21/hw0.08:  n13:-4.34e-01, n7:+1.30e-01, n11:-1.24e-01, n2:-8.52e-02
zeta 3.00 -> 3.24, n17/hw0.10:  n17:-7.46e-01, n19:+4.71e-01, n7:+3.15e-01, n3:-2.82e-01
DH   1.72 -> 1.88, n25/hw0.06: n4:-5.47e-02, n3:-1.59e-02, n2:-1.19e-02, n6:+7.30e-03
```

So the proof cannot be atom-local. The passive bound must use the whole ordered Euler Toeplitz
operator: archimedean shell energy, old-space Green operator `A^{-1}`, and the cumulative prime-power
interference pattern. This is why the right abstraction is closer to a canonical system or de
Branges subspace chain than to a pointwise Carleson estimate.

Mode coherence under refinement is mixed but informative. From `n21/hw0.08` to `n25/hw0.06`, the
early zeta shell modes are stable (`~0.95` correlation on the first two edges), while late modes are
less stable but still identify the same near-critical transfer. The coarsest-to-middle comparison can
rotate sharply, so extremal vectors are diagnostic; the invariant remains the operator norm
`rho(L,L')`.

The positive-kernel version is `scripts/numerics/witness/prime_shell_defect_kernel.py`. Define

```text
K_{L,L'} = A^{-1/2} C D^{-1/2},
Delta_{L,L'} = I - K_{L,L'}^* K_{L,L'}.
```

Then the passive theorem is equivalent to

```text
Delta_{L,L'} >= 0
```

for every support-shell extension. This is the finite de Branges/canonical-system target: construct
`Delta` as a positive kernel increment or Hamiltonian increment along the Sonin support chain.

The defect spectra reinforce the picture:

```text
positive-kernel summary:
kind   basis       min defect   edge          trace at edge   rho
zeta   n17/hw0.10  +0.010      3.00 -> 3.24 +0.045          0.990
zeta   n21/hw0.08  +0.006      3.00 -> 3.24 +0.083          0.994
zeta   n25/hw0.06  +0.024      3.00 -> 3.24 +0.202          0.976
DH     n17/hw0.10  -5.919      1.88 -> 2.10 -5.919          6.919
DH     n21/hw0.08  -4.215      1.72 -> 1.88 -4.215          5.215
DH     n25/hw0.06  -1.331      1.72 -> 1.88 -1.331          2.331
```

Zeta's defect kernel is positive but close to singular at late support extensions. DH's defect
kernel becomes negative at the first failing shell, before the later blocks even have a valid
positive old metric. This is the cleanest finite analogy to a de Branges subspace-chain proof:
successive kernel differences must be positive.

The local defect spectra also show that the near-critical zeta increments are often one- or
two-dimensional:

```text
zeta examples:
edge          basis       new n       shell dim   rho    Delta eigenvalues
2.76 -> 3.00 n21/hw0.08  16,17,19    2           0.993  [0.007, 0.136]
3.00 -> 3.24 n21/hw0.08  23,25       2           0.994  [0.006, 0.077]
3.00 -> 3.24 n25/hw0.06  23,25       2           0.976  [0.024, 0.178]
```

So the next proof-facing object is not an abstract Chern class and not a determinant anomaly. It is
a positive kernel increment:

```text
K_{L'} - K_L  >= 0       (de Branges language)
```

where, in the finite block model, this increment is represented by `Delta_{L,L'}` after the Schur
normalization. The challenge is to identify the analytic kernel whose finite compressions reproduce
these `Delta` matrices from the Euler product and the archimedean Sonin constraints alone.

The factorization diagnostic `scripts/numerics/witness/prime_defect_factorization.py` rules out the
simplest boundary-only reading. It compares the weakest defect direction with outward support moments
and with individual prime-atom quadratic directions. Summary:

```text
feature alignment summary:
kind   valid rows   avg |u| align   avg u^2 align   avg best atom align
zeta   15           0.843           0.820           0.956
DH      4           1.000           1.000           1.000
```

The DH valid rows are mostly one-dimensional shells, so all alignments are automatically `1`; they
do not prove a boundary mechanism. For zeta, where shell dimension is often two, moment alignment
varies substantially while prime-atom feature directions remain more strongly aligned with the weak
defect direction. Examples:

```text
zeta weak defect examples:
edge          basis       new n       defect min  eff rank  |u| align  best atom features
2.76 -> 3.00 n21/hw0.08  16,17,19    +0.007      1.11      0.44       n13:-4.34e-01/al0.84, n11:-1.24e-01/al0.93
3.00 -> 3.24 n21/hw0.08  23,25       +0.006      1.15      0.92       n17:-5.30e-01/al1.00, n7:+1.17e-01/al0.96
3.00 -> 3.24 n25/hw0.06  23,25       +0.024      1.26      0.55       n19:-3.23e-01/al0.87, n17:-1.97e-01/al0.90
```

So `Delta` is not just a rank-one boundary evaluation or outward-radius correction. It is a
distributed shell kernel with strong Euler-Toeplitz content. The de Branges/canonical-system analogy
therefore has to be interpreted as a positive reproducing-kernel increment whose Hamiltonian already
contains the Euler product interference, not as a purely geometric boundary term.

The feature-cone fit in `scripts/numerics/witness/prime_defect_feature_fit.py` makes this sharper.
Fit each finite `Delta` by nonnegative least squares using:

```text
moment cone:      I, |u|-moment Gram, u^2-moment Gram
Euler atom cone:  positive/negative spectral parts of D-normalized prime-atom compressions
combined cone:    moment cone + Euler atom cone
```

Residuals:

```text
kind   rows   avg moment residual   avg atom residual   avg combined residual   max combined
zeta   15     0.333                 0.011               0.011                   0.059
DH      4     0.750                 0.750               0.750                   1.000
```

The one-dimensional shells can be fit trivially, so the meaningful cases are the two-dimensional
shells. There the moment cone often leaves a large residual (`~0.45-0.65`), while Euler atom
features usually drive the residual near zero:

```text
zeta higher-dimensional examples:
edge          basis       moment residual   atom residual   combined residual
2.30 -> 2.52 n21/hw0.08  0.632             0.000           0.000
2.76 -> 3.00 n21/hw0.08  0.515             0.059           0.059
3.00 -> 3.24 n21/hw0.08  0.652             0.037           0.037
2.30 -> 2.52 n25/hw0.06  0.620             0.029           0.029
3.00 -> 3.24 n25/hw0.06  0.535             0.034           0.034
```

This is not a proof and the fitted coefficients can be ill-conditioned; with many atom features,
small finite matrices are easy to interpolate. But the negative result is robust: a simple moment /
boundary cone is not the right positive kernel. The positive kernel must be built from Euler
Toeplitz atom structure, or from an intrinsic analytic object that produces the same atom cone in
finite compression.

The locality test `scripts/numerics/witness/prime_defect_feature_locality.py` adds another important
correction. Split the atom dictionary into:

```text
new atoms:  log n in [L,L')
old atoms:  log n < L
all atoms:  log n < L'
```

The average residuals for zeta are:

```text
feature cone    avg residual
moments         0.333
new atoms       0.268
old atoms       0.030
all atoms       0.011
moments+new     0.206
moments+old     0.030
moments+all     0.011
```

So the positive defect kernel is not local to the newly entering support shell. Old active Euler
atoms fit almost as well as the full active history, while new atoms alone do not. Examples:

```text
zeta locality examples:
edge          basis       new n       moment   new atoms   old atoms   all atoms
2.30 -> 2.52 n21/hw0.08  11          0.632    0.453       0.000       0.000
2.76 -> 3.00 n21/hw0.08  16,17,19    0.515    0.315       0.248       0.059
3.00 -> 3.24 n21/hw0.08  23,25       0.652    0.545       0.037       0.037
3.00 -> 3.24 n25/hw0.06  23,25       0.535    0.434       0.133       0.034
```

This changes the kernel target again. It is not a local point-interaction positivity at `L=log n`.
The shell defect is a cumulative history object: when a new support shell is added, passivity is
secured by the whole already-active Euler Toeplitz flow. In canonical-system terms, the Hamiltonian
increment cannot be a rank-one jump depending only on the new atom; it must remember the previous
Euler interactions through the old-space Green operator `A^{-1}`.

The history-ablation witness `scripts/numerics/witness/prime_defect_history_ablation.py` tests the
memory length more directly. Fit `Delta` using only:

```text
new atoms, recent 1/3/5 old atoms, earliest 3 old atoms, all old atoms, all active atoms.
```

Average residuals:

```text
kind   rows   new    recent1  recent3  recent5  early3  all-old  all-active
zeta   15     0.268  0.266    0.050    0.035    0.229   0.030    0.011
DH      4     0.750  0.750    0.750    0.750    0.750   0.750    0.750
```

So there is some recency: the last three to five old atoms explain most of the finite `Delta`.
But the full old active history is still better, and the all-active dictionary improves slightly
again. Examples:

```text
zeta history ablation examples:
edge          basis       new n       new   recent3  recent5  early3  all-old  all-active
2.30 -> 2.52 n21/hw0.08  11          0.453 0.000    0.000    0.413   0.000    0.000
2.76 -> 3.00 n21/hw0.08  16,17,19    0.315 0.251    0.251    0.570   0.248    0.059
3.00 -> 3.24 n21/hw0.08  23,25       0.545 0.119    0.062    0.390   0.037    0.037
3.00 -> 3.24 n25/hw0.06  23,25       0.434 0.351    0.187    0.513   0.133    0.034
```

This points away from a finite-memory local recursion. The analytic identity should look cumulative:
the support-shell defect at `L -> L'` is governed by the old Green operator and the active Euler
Toeplitz history, with a bias toward recent atoms but no hard cutoff.

The coefficient perturbation witness `scripts/numerics/witness/prime_defect_coefficient_perturb.py`
tests whether this is just generic long-memory behavior. It is not. Keep the same nested basis and
archimedean side, but change the Euler coefficient table:

```text
variant     meaning
zeta        von Mangoldt coefficients
DH          Davenport-Heilbronn log-derivative coefficients
signflip    deterministic sign flips of zeta coefficients
shuffle     deterministic permutation of zeta coefficients among active n
damp-old    zeta, but old coefficients multiplied by 0.75 before the shell
boost-old   zeta, but old coefficients multiplied by 1.25 before the shell
```

On the `n25/hw0.06` nested ambient window:

```text
variant    valid edges   max rho   first failure
zeta       5             0.976     none
DH         1             2.331     1.72 -> 1.88, rho=2.331
signflip   0             n/a       1.72 -> 1.88 invalid
shuffle    0             n/a       1.72 -> 1.88 invalid
damp-old   3             2.904     2.30 -> 2.52, rho=2.904
boost-old  0             n/a       1.72 -> 1.88 invalid
```

The perturbation test is severe:

```text
zeta:
1.72 -> 1.88 rho 0.828
1.88 -> 2.10 rho 0.850
2.30 -> 2.52 rho 0.950
2.76 -> 3.00 rho 0.885
3.00 -> 3.24 rho 0.976

damp-old:
1.72 -> 1.88 rho 0.670
1.88 -> 2.10 rho 0.894
2.30 -> 2.52 rho 2.904   FAIL
```

So zeta's passivity is coefficient-rigid. It is not produced by any long cumulative memory; it
requires the actual Euler coefficient scale. Sign scrambling, coefficient shuffling, DH coefficients,
and even modest old-history rescaling all destroy the positive chain quickly. This makes the target
more arithmetically specific:

```text
The positive defect kernel must encode the exact von Mangoldt/Euler-product coefficient pattern,
not only support order or historical memory.
```

The scale-phase witness `scripts/numerics/witness/prime_defect_scale_phase.py` maps the stability
corridor around the exact coefficient scale. For an edge `H_L ⊂ H_{L'}` use

```text
M_R(a,b) = W_inf
         - a * sum_{log n < L}      atom_n
         - b * sum_{L <= log n < L'} atom_n.
```

The exact zeta point is `(a,b)=(1,1)`. On the `n25/hw0.06` nested ambient window:

```text
old-history scale sweep, new scale fixed at 1:
scale   passive  max rho   min defect   first bad
0.50    false    1.096     -0.096       1.88 -> 2.10
0.75    false    2.904     -1.904       2.30 -> 2.52
0.90    false    1.046     -0.046       2.30 -> 2.52
1.00    true     0.976     +0.024       none
1.10    false    invalid   invalid      1.72 -> 1.88
1.25    false    invalid   invalid      1.72 -> 1.88
```

New-shell scaling is less rigid but still bounded:

```text
new-shell scale sweep, old scale fixed at 1:
scale   passive  max rho   min defect   first bad
0.50    true     0.959     +0.041       none
0.75    true     0.963     +0.037       none
0.90    true     0.969     +0.031       none
1.00    true     0.976     +0.024       none
1.10    true     0.989     +0.011       none
1.25    false    1.114     -0.114       2.76 -> 3.00
1.50    false    1.634     -0.634       1.88 -> 2.10
```

On the coarse grid used in the sweep, the old/global scale passivity corridor is essentially pinned
at `1.000`, while the new-shell scale can vary roughly from `0.50` to `1.15`. This should not be
overread as a zero-width continuum theorem; it is finite-window evidence that the old Euler history
is much more rigidly calibrated than the incoming shell.

Local sensitivity at the exact zeta scale:

```text
edge          rho    defect   d rho/d old   d rho/d new
1.72 -> 1.88 0.828  +0.172   +0.89         +0.00
1.88 -> 2.10 0.850  +0.150   +0.71         +0.26
2.30 -> 2.52 0.950  +0.050   +0.26         +0.03
2.76 -> 3.00 0.885  +0.115   +0.08         +0.52
3.00 -> 3.24 0.976  +0.024   +0.84         +0.09
```

The most delicate late edge `3.00 -> 3.24` is highly sensitive to old-history scale and only weakly
sensitive to the newly entering atoms. Again, this says the positive kernel is a calibrated
cumulative-history object, not a local atom-bound.

The refined threshold witness `scripts/numerics/witness/prime_defect_scale_threshold.py` tightens
this. It does not assume monotonicity; it scans for passive runs and then refines the local
pass/fail transition around the run containing the exact Euler scale. On the same `n25/hw0.06`
window:

```text
direction        passive grid run     refined transition(s)        blocker
old only         [0.9820,1.0090]      0.98176756, 1.00974867       3.00 -> 3.24
global           [0.9820,1.0090]      0.98167977, 1.00973873       3.00 -> 3.24
new only         [0.0000,1.1525]      upper 1.15279513             2.76 -> 3.00
```

Here "old only" means `a` varies with `b=1`, "new only" means `b` varies with `a=1`, and
"global" means `a=b`. The lower endpoint for the new-only run is just the scan boundary `b=0`, not
a theorem about negative new coefficients. Still, the finite picture is clear: the old cumulative
Euler history is calibrated to within a few percent, while the newly entering shell has a much wider
one-sided tolerance. In particular, omitting the incoming positive shell atoms does not break the
finite passive-transfer inequality once the old history is fixed; overdriving the incoming shell
eventually breaks it at `2.76 -> 3.00`.

The local two-parameter corridor confirms the asymmetry:

```text
old scale   passing new-scale interval
0.980       none
0.985       [0.700,1.120]
0.990       [0.700,1.145]
0.995       [0.700,1.150]
1.000       [0.700,1.150]
1.005       [0.700,1.145]
1.010       none
```

So the correct rigidity statement is not "the exact point is isolated." It is: the exact Euler
history lies inside a narrow old-scale tube, and the critical wall of that tube is controlled by the
late cumulative-history edge `3.00 -> 3.24`. The positive defect kernel must explain why the old
Green/Euler history is so tightly normalized before the new shell is even decisive.

The refinement stress test `scripts/numerics/witness/prime_defect_scale_threshold_refine.py` checks
the same threshold shape across neighboring finite bases:

```text
basis       mode     grid run        refined local interval     defect@1   blockers
n17/hw0.10  old      [0.996,1.006]   [0.995468,1.006224]        +0.0104   3.00->3.24 / 3.00->3.24
n17/hw0.10  global   [0.996,1.006]   [0.995468,1.006096]        +0.0104   3.00->3.24 / 3.00->3.24
n17/hw0.10  new      [0.000,1.150]   [<=0.000,1.152432]         +0.0104   scan / 3.00->3.24
n21/hw0.08  old      [0.994,1.002]   [0.992147,1.003017]        +0.0058   3.00->3.24 / 3.00->3.24
n21/hw0.08  global   [0.994,1.002]   [0.992089,1.002991]        +0.0058   3.00->3.24 / 3.00->3.24
n21/hw0.08  new      [0.000,1.095]   [<=0.000,1.096975]         +0.0058   scan / 3.00->3.24
n25/hw0.06  old      [0.982,1.008]   [0.981768,1.009749]        +0.0237   3.00->3.24 / 3.00->3.24
n25/hw0.06  global   [0.982,1.008]   [0.981680,1.009739]        +0.0237   3.00->3.24 / 3.00->3.24
n25/hw0.06  new      [0.000,1.150]   [<=0.000,1.152795]         +0.0237   scan / 2.76->3.00
```

This is not yet a convergence statement; the finite widths move with the basis. But the qualitative
signature is stable: old/global rescaling is restricted to a narrow tube around the exact
von Mangoldt scale, and the obstruction wall is the same late cumulative-history edge. The incoming
shell tolerance is much wider and lower-open in these tests. That makes the next analytic target
more specific: prove a normalization identity for the old Euler Green history, then treat incoming
shell atoms as a controlled perturbation rather than the primary source of positivity.

The atom-level sensitivity witness `scripts/numerics/witness/prime_defect_atom_sensitivity.py` then
asks what this old-history wall is made of. For each active weighted zeta atom, perturb only that
atom's scale and differentiate `rho`. The derivative sums reproduce the old/new scale sensitivities,
but the individual atoms reveal the structure:

```text
edge          rho       old sum   new sum   positive mass   negative mass
1.72 -> 1.88 0.828089  +0.8851   +0.0000   +1.7380         -0.8529
1.88 -> 2.10 0.850159  +0.7098   +0.2636   +2.7495         -1.7761
2.30 -> 2.52 0.949535  +0.2643   +0.0252   +3.1452         -2.8557
2.76 -> 3.00 0.884847  +0.0792   +0.5211   +3.8576         -3.2572
3.00 -> 3.24 0.976289  +0.8343   +0.0913   +9.2267         -8.3011
```

The late edge is the main point. The small net old-scale slope `+0.8343` hides a much larger signed
old-history cancellation. Its strongest atoms are:

```text
3     d rho/d scale = +3.6576
5     d rho/d scale = -2.6325
2     d rho/d scale = -2.5173
11    d rho/d scale = +2.3660
7     d rho/d scale = -1.7613
2^2   d rho/d scale = +1.1515
```

So the positive defect kernel cannot be atomwise positive in the Euler variables. Some old atoms
raise the transfer norm when increased; others are local repairs. The exact von Mangoldt history
balances these opposing directions so that the net transfer remains below one.

The refinement check `scripts/numerics/witness/prime_defect_atom_sensitivity_refine.py` repeats the
late-edge atom derivative across nearby bases:

```text
basis       rho       defect    old sum   new sum   pos mass  neg mass  top old atoms
n17/hw0.10  0.989623  +0.0104   +0.945    +0.059    +5.043    -4.039    3:+2.16, 11:+1.34, 13:-1.22, 5:-1.08, 3^2:+0.89
n21/hw0.08  0.994175  +0.0058   +0.459    +0.048    +2.056    -1.550    11:+0.84, 7:+0.63, 19:+0.47, 13:-0.46, 2:-0.33
n25/hw0.06  0.976289  +0.0237   +0.834    +0.091    +9.227    -8.301    3:+3.66, 5:-2.63, 2:-2.52, 11:+2.37, 7:-1.76
```

The exact labels and magnitudes are still finite-basis dependent, but the signed-cancellation shape
is stable. This rules out an atomwise monotonic proof and strengthens the canonical-system reading:
the old Euler history should appear as a signed Green/current identity whose total Hamiltonian
increment is positive only after the full ordered history is assembled.

The variational-current witness `scripts/numerics/witness/prime_defect_variational_current.py`
removes the finite-difference layer. For one nested edge write the compressed margin as

```text
M = [ A  C ]
    [ C* D ],
rho = ||A^{-1/2} C D^{-1/2}||^2.
```

Let `s = sqrt(rho)` and let `x,y` be the critical generalized old/shell transfer vectors,
normalized by

```text
x* A x = 1,     y* D y = 1,     x* C y = s.
```

Then the first variation is

```text
d rho = 2s x* dC y - rho x* dA x - rho y* dD y.
```

For the scale of one already-weighted Euler atom, `dM = -atom`, so

```text
d rho / d scale(atom)
  = rho <A_atom x,x> + rho <D_atom y,y> - 2s <C_atom y,x>.
```

This analytic formula matches the finite-difference slopes:

```text
edge          rho       defect    finite-difference max error
1.72 -> 1.88 0.828089  +0.1719   5.03e-09
1.88 -> 2.10 0.850159  +0.1498   1.64e-08
2.30 -> 2.52 0.949535  +0.0505   2.09e-07
2.76 -> 3.00 0.884847  +0.1152   1.74e-06
3.00 -> 3.24 0.976289  +0.0237   3.28e-06
```

So the finite Euler current is explicit: each atom is contracted with a rank-two indefinite stress
tensor determined by the critical transfer mode. On the late edge:

```text
current sums over all active atoms:
old slope +0.8343, new slope +0.0913
A contribution +0.3447, D contribution -0.3648, C contribution +0.9456

strongest atoms:
atom  slope    A-part   D-part   C-part
3     +3.6576  +2.5306  -0.0762  +1.2031
5     -2.6325  -1.8575  -0.0041  -0.7708
2     -2.5173  -2.1918  -0.0634  -0.2621
11    +2.3660  +1.5568  +0.0806  +0.7286
7     -1.7613  -1.4046  +0.0719  -0.4287
2^2   +1.1515  +1.3416  -0.0212  -0.1689
```

The block terms themselves are not sign-definite because the Euler atoms are Toeplitz correlations,
not point-sampling squares. This gives the finite form of the desired transgression current:

```text
stress_{L,L'} =
  [ rho x x*       -s x y* ]
  [ -s y x*        rho y y* ],

d rho / d scale(atom_n) = <atom_n, stress_{L,L'}>.
```

The next analytic target is therefore precise. For every support extension, construct this
critical-mode stress tensor without using zero-side positivity, and prove that the exact ordered
Euler history has controlled total pairing with it. That is the variational form of the positive
Schur-complement theorem.

The stress-kernel witness `scripts/numerics/witness/prime_defect_stress_kernel.py` turns this stress
pairing into an actual function of the shift `U`. Since

```text
atom_U(i,j) = (1/2pi) int phihat_i(t) phihat_j(t) cos(Ut) dt,
```

the stress tensor defines

```text
k_{L,L'}(U)
  = (1/2pi) int H_{L,L'}(t) cos(Ut) dt,

H_{L,L'}(t)
  = phihat(t)^* S_{L,L'} phihat(t).
```

For zeta,

```text
d rho / d scale(atom_n)
  = 2 Lambda(n) n^{-1/2} k_{L,L'}(log n).
```

The numerical reconstruction is exact to roundoff:

```text
edge          old kernel range    new kernel range    sign changes  sample error
1.72 -> 1.88 [-1.485,+2.969]     [-0.000,+0.175]    10            2.22e-16
1.88 -> 2.10 [-1.880,+4.457]     [-0.000,+0.363]     5            1.11e-16
2.30 -> 2.52 [-3.340,+6.242]     [-0.000,+0.206]    12            2.50e-16
2.76 -> 3.00 [-1.846,+4.154]     [-0.000,+0.537]     7            6.66e-16
3.00 -> 3.24 [-4.156,+7.233]     [-0.000,+0.421]     8            8.88e-16
```

On the late wall, the old-history current is visibly an ordered prime-power sampling of an
oscillatory kernel:

```text
atom   U      weight   k(U)     weighted   cumulative
2      0.693  0.980   -2.568  -2.5173   -2.5173
3      1.099  1.269   +2.883  +3.6576   +1.1403
2^2    1.386  0.693   +1.661  +1.1515   +2.2918
5      1.609  1.440   -1.829  -2.6325   -0.3408
7      1.946  1.471   -1.197  -1.7613   -2.1021
2^3    2.079  0.490   +0.666  +0.3266   -1.7755
3^2    2.197  0.732   +1.440  +1.0545   -0.7210
11     2.398  1.446   +1.636  +2.3660   +1.6450
13     2.565  1.423   -0.308  -0.4375   +1.2074
2^4    2.773  0.347   -1.128  -0.3909   +0.8165
17     2.833  1.374   -0.409  -0.5615   +0.2550
19     2.944  1.351   +0.429  +0.5793   +0.8343
```

The late kernel's largest old extrema are:

```text
positive: U=1.081 k=+2.911, U=1.316 k=+1.784, U=2.357 k=+1.668
negative: U=0.539 k=-4.156, U=1.717 k=-2.547, U=2.685 k=-1.645
```

This is the cleanest finite formulation so far. The hard theorem should control

```text
sum_{log n < L'} 2 Lambda(n) n^{-1/2} k_{L,L'}(log n)
```

for every critical transfer stress `S_{L,L'}` coming from a support extension. The proof cannot
replace this by positive sampling; the kernel is oscillatory and the Euler weights are doing ordered
signed cancellation.

The Lorentz-stress witness `scripts/numerics/witness/prime_defect_lorentz_stress.py` factors the
frequency density further. If `X(t)` and `Y(t)` are the old and shell critical amplitudes, then
`rho=s^2` gives

```text
H(t)
  = rho X(t)^2 + rho Y(t)^2 - 2s X(t)Y(t)
  = ((rho+s)/2)(X-Y)^2 + ((rho-s)/2)(X+Y)^2.
```

The first coefficient is positive and the second is negative. Thus the finite stress is Lorentzian
or Pontryagin-like, not Hilbert-positive. Numerically:

```text
edge          positive coeff   negative coeff   pos mass   neg mass   total k(0)
1.72 -> 1.88 +0.869042        -0.040952        +3.116     -0.147     +2.969
1.88 -> 2.10 +0.886100        -0.035941        +4.645     -0.188     +4.457
2.30 -> 2.52 +0.961988        -0.012453        +6.324     -0.082     +6.242
2.76 -> 3.00 +0.912755        -0.027908        +4.285     -0.131     +4.154
3.00 -> 3.24 +0.982181        -0.005892        +7.276     -0.044     +7.233
```

In these finite windows the negative square component is small. The pointwise sign oscillation in
`k(U)` mostly comes from the cosine transform of the dominant positive spectral density; positive
type is not pointwise positivity. This is exactly the trap that killed the naive Carleson picture:
even a positive spectral square can sample negatively at nonzero prime-power shifts. The right
object is therefore closer to a de Branges/canonical-system or Pontryagin-space transfer kernel than
to a scalar positive measure on the support line.

The Euler-measure witness `scripts/numerics/witness/prime_defect_euler_measure.py` compares the
actual discrete prime-power measure

```text
dmu_E = sum_{n>=2} 2 Lambda(n)n^{-1/2} delta_{log n}
```

with its PNT-scale continuous main density

```text
dmu_0(U) = 2 exp(U/2) dU.
```

This is a calibration test for the stress-kernel target. If the smooth main density explained the
Euler current, we could aim for a mostly continuous canonical-system estimate. The results say no:

```text
edge          region  discrete   smooth main   residual   |disc|    |main|    primes    powers
1.72 -> 1.88 old     +0.8851    +0.3780       +0.5070   +2.5910  +1.9902  +1.3095  -0.4245
1.88 -> 2.10 old     +0.7098    +0.3502       +0.3597   +4.2620  +3.4288  +0.7343  -0.0244
2.30 -> 2.52 old     +0.2643    +0.1826       +0.0817   +5.9757  +7.4883  -2.1985  +2.4628
2.76 -> 3.00 old     +0.0792    -0.3108       +0.3901   +6.5937  +7.0121  +0.4104  -0.3312
3.00 -> 3.24 old     +0.8343    +1.0701       -0.2359   +17.4365 +15.8586 -1.3074  +2.1416
```

The arithmetic residual is comparable to the smooth main term on several edges. Also, prime powers
are not harmless lower-order noise: on `2.30 -> 2.52` and `3.00 -> 3.24`, prime powers reverse a
large part of the prime-only contribution.

For the late wall, the discrete current nearly returns to the smooth main only after a long
oscillatory path:

```text
atom   U      step      discrete   smooth main   residual
2      0.693  -2.5173  -2.5173   +0.0000       -2.5173
3      1.099  +3.6576  +1.1403   +0.8574       +0.2829
2^2    1.386  +1.1515  +2.2918   +3.0491       -0.7573
5      1.609  -2.6325  -0.3408   +3.1032       -3.4439
7      1.946  -1.7613  -2.1021   -0.4369       -1.6652
2^3    2.079  +0.3266  -1.7755   -0.6255       -1.1500
3^2    2.197  +1.0545  -0.7210   +0.1659       -0.8870
11     2.398  +2.3660  +1.6450   +2.1717       -0.5267
13     2.565  -0.4375  +1.2074   +3.1793       -1.9719
2^4    2.773  -0.3909  +0.8165   +1.1310       -0.3145
17     2.833  -0.5615  +0.2550   +0.7490       -0.4940
19     2.944  +0.5793  +0.8343   +0.8541       -0.0199
```

This moves the target again. The canonical-system object may supply the admissible stress kernels
`k_{L,L'}`, but the inequality still needs an explicit-formula/Euler-product identity for the
discrete measure `dmu_E`, including prime powers. A proof that only controls the PNT main density
would miss load-bearing arithmetic in these finite tests.

The full-operator surrogate `scripts/numerics/witness/prime_defect_measure_surrogate.py` confirms
that this is not just a first-variation artifact. Build

```text
P_discrete(R) = sum_{log n < R} 2 Lambda(n)n^{-1/2} T_{log n},
P_smooth(R)   = int_{log 2}^R 2 exp(U/2) T_U dU.
```

Then test the actual shell transfer for `Winf`, `Winf-P_smooth`, prime-only, prime-power-only, and
the full discrete zeta operator. The result is severe:

```text
edge          arch       smooth     primes     powers     discrete
1.72 -> 1.88 rho .413   invalid    invalid    rho .255   rho .828
1.88 -> 2.10 rho 1.028 invalid    invalid    rho .867   rho .850
2.30 -> 2.52 invalid    invalid    invalid    invalid    rho .950
2.76 -> 3.00 invalid    invalid    invalid    invalid    rho .885
3.00 -> 3.24 invalid    invalid    invalid    invalid    rho .976
```

Here "invalid" means an old or shell block is not positive, so the passive transfer norm is not even
defined. The exact combined discrete Euler measure is the only tested operator that stays in the
positive shell-transfer cone on the later edges. Prime-only and prime-power-only truncations both
fail; their combination repairs the margin. Thus the proof cannot safely pass through a smooth
PNT-density surrogate and then perturb. It has to keep the exact Euler product measure until the
Schur-complement positivity is established.

This makes an optimal-control framing plausible, but it has to be the right control problem. The
residual-control witness `scripts/numerics/witness/prime_defect_residual_control.py` partitions
`[log 2,R]` into cells around the active prime-power logarithms and writes the exact
smooth-to-discrete correction as

```text
M_discrete
  =
  M_smooth
  +
  sum_n (P_smooth_cell(n) - P_atom(n)).
```

Then it follows the scalar open-loop path

```text
M(lambda) = M_smooth + lambda (M_discrete - M_smooth)
```

and finds the first `lambda` where the compressed support extension becomes positive:

```text
edge          smooth min   discrete min   lambda needed
1.72 -> 1.88 -1.168e-01   +2.969e-02     0.7623
1.88 -> 2.10 -2.675e-01   +2.131e-02     0.9117
2.30 -> 2.52 -3.494e-01   +5.657e-03     0.9567
2.76 -> 3.00 -3.598e-01   +3.930e-03     0.9793
3.00 -> 3.24 -3.826e-01   +2.019e-03     0.9890
```

So the late shell is nearly bang-bang along the exact residual direction: almost the whole
smooth-to-discrete controller is needed before positivity returns. Individual residual cells can
repair or harm the smooth bad vector. On the late edge:

```text
repairs on smooth bad vector:
2      +4.685e-01
5      +1.109e-01
2^2    +4.100e-02
2^3    +2.801e-02
3^2    +1.783e-02

harms:
3      -1.648e-01
7      -1.006e-01
2^4    -2.237e-02
```

This says the control object is global and arithmetic. A plausible optimal-control proof would be a
storage/Riccati inequality for the full Euler residual system, not a local feedback law that treats
each prime-power cell as sign-definite.

The bounded-control witness `scripts/numerics/witness/prime_defect_residual_control_opt.py` tests
whether the exact Euler controller is optimal for naive actuator costs. Allow independent bounded
gains

```text
M(u) = M_smooth + sum_n u_n R_n,    0 <= u_n <= 1,
```

and numerically minimize either `sum u_n` or `sum u_n^2` subject to the compressed margin being
positive. The optimization is only a finite diagnostic, but the answer is informative:

```text
edge          cells  scalar lambda  L2 rms gain  active L2 controls
1.72 -> 1.88 4      0.7623         0.363        2:0.57, 3:0.45
1.88 -> 2.10 6      0.9117         0.397        2:0.90, 3:0.38, 7:0.03
2.30 -> 2.52 8      0.9567         0.438        2:0.93, 3:0.60, 2^2:0.47, 5:0.29, ...
2.76 -> 3.00 12     0.9793         fallback     exact controller used
3.00 -> 3.24 14     0.9890         0.431        2:0.97, 3:0.75, 2^2:0.67, 5:0.53, ...
```

For L1, SLSQP finds sparse cheap controllers on the first two edges but falls back to the exact
feasible controller on later line-search failures. For L2, several edges admit much smaller
fractional controllers than the exact `u_n=1` arithmetic pattern. Therefore the zeta residual
controller is not "optimal" for a naive magnitude cost. If optimal control is the right language,
the cost/dynamics must be arithmetic: a storage or Riccati inequality tied to the Euler product
measure, not a free actuator minimization problem.

The causal-flow witness `scripts/numerics/witness/prime_defect_residual_causal_flow.py` then restores
the time order. Starting from `M_smooth`, add the exact residual cells chronologically:

```text
M_k = M_smooth + R_2 + R_3 + ... + R_{n_k}.
```

The minimum eigenvalue is not monotone. Positivity often returns only at the end, after a deeper
temporary deficit:

```text
edge          storage depth   final min    first positive prefix      deepest prefix
1.72 -> 1.88 1.168e-01       +2.969e-02   2/4 at 3                  smooth
1.88 -> 2.10 2.675e-01       +2.131e-02   4/6 at 5                  smooth
2.30 -> 2.52 3.494e-01       +5.657e-03   7/8 at 9                  smooth
2.76 -> 3.00 5.478e-01       +3.930e-03   10/12 at 16               4
3.00 -> 3.24 5.923e-01       +2.019e-03   13/14 at 23               4
```

The late edge makes the storage issue concrete:

```text
largest prefix repairs:
2      +2.032e-01
17     +2.009e-01
5      +1.716e-01
13     +1.065e-01
19     +7.482e-02

largest prefix harms:
3      -2.346e-01
4      -1.784e-01
11     -4.255e-02
16     -1.632e-03
```

So even the exact Euler controller is not a monotone repair process. It is a causal sequence with
interlaced harms and repairs, and the margin is released only terminally. In control terms, the
finite target is a storage functional that can carry the prefix deficit and certify terminal
Schur-complement positivity.

The Chebyshev-residual witness `scripts/numerics/witness/prime_defect_chebyshev_residual.py` rewrites
that arithmetic residual in cumulative form. For

```text
phi(U) = 2 exp(-U/2) k(U),
F(U)   = sum_{log 2 <= log n <= U} Lambda(n) - (exp(U)-2),
```

the residual on `[log 2,B]` is

```text
R(B)
  =
  sum_{log n <= B} Lambda(n) phi(log n)
  -
  int_{log 2}^B phi(U) exp(U)dU
  =
  phi(B)F(B) - int_{log 2}^B F(U) phi'(U)dU.
```

Numerically, the integration-by-parts reconstruction agrees with the direct residual up to the
coarse derivative/quadrature error of this witness:

```text
edge          part  direct residual  boundary   distributed  error
1.72 -> 1.88 old   +0.5070          +0.0760    +0.4332      +2.16e-03
1.88 -> 2.10 old   +0.3597          -0.1314    +0.4885      -2.63e-03
2.30 -> 2.52 old   +0.0817          -0.0192    +0.1039      +2.93e-03
2.76 -> 3.00 old   +0.3901          -0.2714    +0.6584      -3.02e-03
3.00 -> 3.24 old   -0.2359          +0.2228    -0.4655      -6.81e-03
```

The all-history residuals show the same pattern:

```text
edge          direct residual  boundary   distributed
1.72 -> 1.88 +0.4832          -0.0000    +0.4854
1.88 -> 2.10 +0.4891          -0.0000    +0.4862
2.30 -> 2.52 +0.0466          -0.0000    +0.0496
2.76 -> 3.00 +0.5901          -0.0000    +0.5849
3.00 -> 3.24 -0.4583          +0.0000    -0.4643
```

So the residual is not mainly an endpoint Chebyshev error; it is a distributed pairing of the
cumulative error `F(U)` with the derivative of the admissible stress kernel. On the late wall,
endpoint-by-endpoint:

```text
atom   U      residual   boundary   distributed   F_end
2      0.693  -2.5173   -2.5173   +0.0000       +0.693
3      1.099  +0.2829   +1.1994   -2.3514       +0.360
2^2    1.386  -0.7573   +0.2010   -1.5616       +0.121
5      1.609  -3.4439   -0.0030   -1.6509       +0.002
7      1.946  -1.6652   -0.3428   -0.7314       +0.379
2^3    2.079  -1.1500   +0.3292   -1.5029       +0.699
3^2    2.197  -0.8870   +0.4711   -1.6932       +0.491
11     2.398  -0.5267   -1.0003   -1.7476       -1.014
13     2.565  -1.9719   -0.2368   -1.6655       +1.388
2^4    2.773  -0.3145   +0.5136   -0.6055       -0.911
17     2.833  -0.4940   -0.1698   -0.2397       +0.857
19     2.944  -0.0199   +0.3597   -0.4725       +1.828
```

This gives the next clean analytic phrasing:

```text
For every admissible critical stress kernel phi,
control phi(B)F(B) - int F phi'
with the exact Chebyshev error F attached to the Euler product.
```

That is closer to an explicit-formula/canonical-system bridge than either atomwise sampling or a
smooth-density estimate.

The norm-budget witness `scripts/numerics/witness/prime_defect_chebyshev_norm_budget.py` then asks
whether crude estimates on this Chebyshev pairing are remotely sharp. For the distributed term,
compare

```text
|int F phi'|,
int |F phi'|,
sup|F| * int |phi'|,
||F||_2 ||phi'||_2.
```

The answer is that the scalar bounds are very wasteful:

```text
edge          part  residual  boundary  distrib   int|.|   |dist|/|.|  supTV    ratio  L2bd    ratio
1.72 -> 1.88 old   +0.5092   +0.0760   +0.4329   2.0322   0.213       5.9638   0.073  2.9538  0.147
1.88 -> 2.10 old   +0.3570   -0.1314   +0.4887   2.5125   0.195       9.6170   0.051  4.5906  0.106
2.30 -> 2.52 old   +0.0847   -0.0192   +0.1040   5.5099   0.019       14.8547  0.007  7.5008  0.014
2.76 -> 3.00 old   +0.3870   -0.2714   +0.6596   3.7512   0.176       15.5759  0.042  6.1279  0.108
3.00 -> 3.24 old   -0.2427   +0.2228   -0.4658   8.3305   0.056       42.4892  0.011  15.4917 0.030
```

For the late all-history edge, the distributed term is

```text
positive part +3.9998
negative part -4.4641
signed total  -0.4643
```

so it is only `5.5%` of `int |F phi'|`, `1.1%` of the `sup|F|TV(phi)` bound, and `2.8%` of the L2
bound. This means a proof based only on a scalar Chebyshev-error estimate and a variation norm for
`phi` would miss most of the cancellation. The needed arithmetic estimate is more structured:
exploit oscillatory alignment between the cumulative Chebyshev error `F` and derivatives of the
admissible stress kernels generated by the Sonin/canonical-system geometry.

The late-edge refinement check `scripts/numerics/witness/prime_defect_chebyshev_norm_refine.py`
keeps this conclusion, with an important caveat about signs:

```text
basis       part  residual  boundary  distrib   int|.|  |dist|/|.|  supTVr  L2r    pos      neg
n17/hw0.10  old   +1.0538   +0.2147   +0.8388   5.3514  0.157       0.027   0.076  +3.095  -2.256
n17/hw0.10  all   +0.8269   +0.0000   +0.8269   5.4804  0.151       0.026   0.069  +3.154  -2.327
n21/hw0.08  old   +0.8799   +0.1670   +0.7126   2.0019  0.356       0.080   0.246  +1.357  -0.645
n21/hw0.08  all   +0.7139   +0.0000   +0.7139   2.0984  0.340       0.077   0.226  +1.406  -0.692
n25/hw0.06  old   -0.2427   +0.2228   -0.4658   8.3305  0.056       0.011   0.030  +3.932  -4.398
n25/hw0.06  all   -0.4643   +0.0000   -0.4643   8.4639  0.055       0.011   0.028  +4.000  -4.464
```

The sign and magnitude of the late residual are not stable finite invariants. What is stable is that
the signed distributed term is much smaller than `int |F phi'|`, and much smaller again than
`sup|F|TV(phi)` or L2 Cauchy-Schwarz budgets. Thus the theorem should not try to prove a fixed sign
for the residual alone. It should prove that the whole archimedean-plus-Euler Schur defect remains
positive, using a structured oscillatory estimate for the admissible stress-kernel family.

Topologically, the base is still just an interval in the support edge `L`, so an ordinary Chern class
cannot be the obstruction: `H^2` of the base is zero. The useful object is relative and singular,
closer to a Bott-Chern / Chern-Simons transgression current for a metric pair:

```text
continuous 1-form:    d log det G_L  -  connection-volume density
point masses:         log det G_- - log det(T_n^* G_+ T_n) at L = log n
positivity constraint: G_- - T_n^*G_+T_n >= 0, with G_L = J_L + lambda h_L
```

That is the cohomological target: not a closed topological class on a smooth bundle, but a positive
relative transgression measure on a singular Hermitian bundle. RH-content would be the theorem that
zeta's Euler point interactions keep this metric pair in the positive cone, while DH-type coefficient
systems leave it.

## 5. Current plan of attack

1. **Nested extension theorem.** Formulate the theorem for inclusions `H_L ⊂ H_{L'}` of pole-killed
   Sonin support windows. The target invariant is positivity of the shell Schur complement.
   Equivalently, in block form, prove `C^* A^{-1} C <= D`, or `rho(L,L') <= 1`.
2. **Full cone first, channels second.** Active channels and `E_L = bottom spectral subspace of M_L`
   are diagnostic finite shadows. They should not define the proof object.
3. **Separate support-shell geometry from Euler jumps.** Old subspaces are carried almost unchanged;
   the new shell sees both archimedean geometry and newly active Euler Toeplitz atoms.
4. **Seek a canonical-system/de Branges mechanism.** The observed bound is a passive transfer
   estimate from shell energy `D` to old-space energy `A`; prove it by constructing the right
   positive defect kernel `Delta = I - K^*K` or Hamiltonian increment, not by diagonalizing finite
   matrices. The kernel must be distributed/Euler-Toeplitz and cumulative in the active Euler
   history, not merely a boundary, moment, new-atom, or finite-memory term. It must also use the
   exact von Mangoldt coefficient scale. The refined scale thresholds say this more precisely:
   old/global rescaling is confined to a narrow tube around scale `1`, usually blocked by the late
   `3.00 -> 3.24` edge, while incoming-shell rescaling has a much wider one-sided tolerance. The
   atom sensitivities show that the old-history tube is a signed cancellation between Euler atoms,
   not atomwise monotone positivity. The variational-current formula identifies the finite stress
   tensor against which the Euler history must be controlled; the stress-kernel reconstruction turns
   that pairing into an oscillatory shift kernel sampled at prime-power logarithms. The Lorentz
   factorization shows why the right setting is canonical-system/de Branges or Pontryagin-flavored:
   positive spectral density still gives sign-changing values at nonzero shifts. The Euler-measure
   decomposition shows that the smooth PNT density is insufficient; the full-operator surrogate says
   this remains true before linearization, because smooth, prime-only, and prime-power-only operators
   all fail the later shell tests while the exact combined Euler measure succeeds. The Chebyshev
   integration by parts converts the discrete-minus-smooth residual into a distributed pairing
   `-int F phi'` plus a boundary term, with `F(U)=psi(e^U)-e^U`. The norm budget shows that crude
   `sup|F|TV(phi)` or L2 controls are too wasteful; the estimate has to use the oscillatory alignment
   of `F` with admissible stress-kernel derivatives. Refinement checks suggest that residual sign is
   not itself invariant; the invariant target is positivity of the full Schur defect after the
   archimedean and exact Euler pieces are combined. An optimal-control formulation should therefore
   be a storage/Riccati inequality for the exact smooth-to-discrete Euler residual controller, which
   is nearly fully engaged on late shells, not a model where the arithmetic error is freely chosen.
   Naive L1/L2 actuator costs select artificial fractional controllers, so the storage cost must
   encode Euler-product arithmetic rather than generic control effort. The causal prefix flow shows
   why storage is necessary: exact residual cells interlace harms and repairs, and late-shell
   positivity is recovered only after carrying substantial prefix deficits.
5. **Use transgression only on controlled channels.** Full-rank determinant volume is dominated by
   projection singular values. The transgression measure is useful after selecting a stable
   obstruction channel, not as the primary invariant.
6. **Stress the positive cone.** The real finite discriminator is whether the full compressed `J_L`
   and its shell Schur complements stay positive. Zeta does in the tested windows; DH does not.
7. **Make the theorem noncircular.** The proof cannot invoke Weil positivity on the zero side. It
   must construct the positive metric pair from the Euler product / archimedean Sonin geometry.

## 6. The proof shape if this is real

Treat the support edge `L` as time.

Between prime powers, the archimedean/Sonin form changes continuously. At `L = log n`, the prime
side adds a Toeplitz/correlation jump

```text
2 Lambda(n) n^{-1/2} tau_{log n}.
```

These jumps are indefinite on the square-root test space. A noncircular proof would therefore be an
ordered energy-balance / Loewner theorem with signed point interactions:

```text
ordered archimedean drift + exact Euler jumps preserve positivity.
```

Equivalently, build a passive canonical system whose Hamiltonian is positive and whose point
interactions are the prime powers. The transfer function should be the scattering object attached to
zeta; passivity would imply the Schur kernel is positive, forcing resonances to the line. The new
numerics say this cannot be a monotone "each atom costs capacity" proof; it must use ordered
cancellation/repair among the Euler jumps.

In more geometric language: construct a fibration over the support line whose fibers are Sonin
boundary channels, equip it with a metric pair `(J,h)`, and prove that the Euler point-interaction
connection is dissipative:

```text
T_n^*(J_+ + lambda h_+)T_n <= J_- + lambda h_-.
```

The archimedean drift supplies the continuous part of the metric; the prime powers supply singular
connection jumps. RH would follow from positivity of the resulting Schur/Herglotz kernel.

## 7. Failure modes

1. **Weil positivity in disguise.**
   If the proof of `T_Lambda <= A_infty` uses the zero-side identity
   `sum_rho |hhat(gamma_rho)|^2 >= 0`,
   it is circular.

2. **Bost-Connes/QSM only.**
   KMS positivity gives the prime weights and dynamics, but ordinary KMS positivity does not give the
   cross-place domination.

3. **Archimedean-only Sonin positivity.**
   `W_infty >= 0` is DH-shared and RH-silent. The whole point is the contractive embedding of the
   prime Toeplitz operator into the archimedean norm.

4. **Arithmetic P is zero-independent.**
   This is not a logical objection to a proof, but it means finite "plant a zero" tests cannot verify
   the arithmetic side. The proof must make zeta's actual `Lambda(n)` force positivity.

5. **False rank-one Carleson model.**
   The expression `sum Lambda(n)/sqrt(n) |h(log n)|^2 <= W_infty(h)` is not the pole-killed Weil
   form. It may be a useful factorized shadow only if a new theorem constructs that factorization.

## 7. Flow computation

Formalize the support-flow:

```text
M(L) = A_infty(L) - P_zeta(L)
```

and numerically decompose the change into

```text
continuous drift: M(L+eps-) - M(L-eps+)
Toeplitz jump:    - 2 Lambda(n)/sqrt(n) tau_{log n}.
```

This is now implemented in:

```text
python3 -m scripts.numerics.witness.prime_carleson_flow
```

The transgression stress tests are separated into:

```text
python3 -m scripts.numerics.witness.prime_transgression_stress
```

The useful observable is no longer just the Schur complement of a positive atom. It is the full
ordered trajectory of the smallest eigenvalue and the relative size of each indefinite jump. The
first result is decisive for shaping the program: zeta's coefficient pattern repairs the margin
critically; DH's does not.

Next computation: refine the continuous curvature term. For same-label segments, estimate whether
the connection-volume density is controlled by a quadratic expression in the second fundamental form,
for example

```text
connection-density  ~  Tr(B_L^* B_L)
```

up to a bounded metric-variation term. For label-changing segments (`n5 -> n7`, `n7 -> n13`, ...),
keep the finite dissipative handoff transgression. If the drift density and jump transgression both
stabilize under refinement, the target becomes a singular Hermitian bundle with continuous
curvature plus Euler point defects.

## 8. Current status

This is a live analytic target, not a proof. The candidate is interesting because it gives a precise
replacement for "finite ground at infinity":

```text
finite-ground purity  ->  ordered prime-Toeplitz passivity in the Sonin boundary
```

The hard theorem remains exactly the RH-hard statement:

```text
2 sum Lambda(n)/sqrt(n) <h, tau_{log n} h> <= W_infty(h)
```

for all admissible test functions.
