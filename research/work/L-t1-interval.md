# L - T1 interval certificate (R2 rung): rigorous ball certification of the default active-23 endpoint

Status: executed 2026-06-10. Witness (new, fail-closed, exit-code gated):
`scripts/numerics/witness/prime_defect_t1_interval_certificate.py`.
Background rung R2; per TODO.md the epistemic value is asymmetric: a certified
`H <= 0` would REFUTE the local mechanism (major result); a certified `H > 0`
merely confirms the floats. Both readings were pre-registered in the witness
docstring before the run (P1 confirm / P2 refute / P3 inconclusive, plus a P0
construction-drift abort).

RESULT: P1 (confirmation branch). `A_+ > 0` and `H = S+G > 0` are CERTIFIED
by rigorous ball arithmetic for the exact statement of section 4, with
margin-to-width ratios ~1.7e3 (h11) and ~8.9e2 (det H). Per the
pre-registered asymmetry this confirms the floats and closes the T1
"interval certificate pending" item; it does not extend the mechanism.

## 1. Step-1 baseline: the five existing witnesses (all rerun 2026-06-10, exit 0)

All match the TODO.md "Current Evidence Snapshot" exactly:

```text
prime_defect_default_t1_certificate:
  H = [[+3.586521625353e-02, -4.126073251055e-02],
       [-4.126073251055e-02, +1.807102584705e-01]]
  eig(H) = +2.493625500557e-02, +1.916392197184e-01
  Sylvester: h11=+3.586521625353e-02, det=+4.778764451968e-03, spd=True
  identity stats: negative=233/721, repaired=233, max identity error=3.4e-13
prime_defect_t1_error_budget:
  old_dim=21, shell_dim=2; direct composition error=4.441e-16
  eig(A_+)=[+3.930222e-03, +3.705665e+00], cond(A_+)=9.429e+02
  uniform entry budget eta=3.867e-09 (safety 0.5)   [conservative, NOT used here]
prime_defect_t1_stability:
  L2 grid 6001 -> 12001: max|deig(H)|=1.6e-08, |ddet|=3.6e-10
prime_defect_t1_arb_components:
  atom/smooth/suffix Arb radii ~1e-47/8.1e-27/3.9e-32; ambient grid-vs-Arb
  atom discrepancy 6.2e-08; eigmin shift from Arb atom+suffix = +9.0e-07
prime_defect_t1_winf_tail (--tail-propagation):
  default-vs-T1500 entry drift up to 2.1e-06; envelope T=5000 -> 5.953e-12;
  compressed entry factor max||B_i||_1||B_j||_1 = 2.759e+02
```

## 2. Enclosure inventory before this rung (what was floats, what was balls)

Already Arb-enclosed (diagnostic level): atom overlap entries (radii
~1e-36..1e-47), smooth cell/suffix entries (~1e-27..1e-32), W_inf finite
integrals (~1.3e-24 per entry at T=5000), W_inf tail envelope (numerically
integrated, 5.953e-12 at T=5000).

Still floats / not certificate-grade:

```text
F1  the W_inf tail envelope was evaluated by SciPy quadrature (not a bound);
F2  the W_inf Arb integrand used digamma(z).real INSIDE the acb integrand --
    Re of a holomorphic function is not holomorphic, so Arb's Gauss-quadrature
    error bounds (which require holomorphy on the evaluation ellipses) do not
    apply; the existing winf_entry_arb enclosures are therefore NOT rigorous
    as stated (soundness finding S1, see section 3);
F3  compact-overlap endpoints (max/min of center/half-width arithmetic) were
    computed in doubles and the rounding was not included in the ball
    (soundness finding S2);
F4  the old atoms entering the certificate matrix were Fourier-grid floats in
    the default pipeline (Arb replacement existed only as a diagnostic);
F5  the atom-23 weight was the grid-derived ratio (differs from the exact
    2 log23/sqrt23 by 1.8e-14);
F6  every algebraic step (compression by B, the block split, A_+^{-1}, the
    Schur complement, eigenvalues/determinant) was float linear algebra;
F7  the basis B and the L2 Gram behind it are float constructions.
```

This rung closes F1-F6 and disposes of F7 by reformulating the statement
(section 4). F2 and F3 are findings about the existing diagnostics, recorded
here so they are not later mistaken for certificate components.

## 3. Soundness findings in the existing Arb diagnostics (fail-closed report)

S1 (Re-inside-integrand): `prime_defect_t1_winf_tail.winf_entry_arb` integrates
`phi_i phi_j Re psi(1/4+it/2)` by returning `z.digamma().real` from the acb
integrand. For rigorous error bounds `acb_calc_integrate` requires the
integrand to be holomorphic on the complex evaluation regions; `Re` breaks
holomorphy, so those enclosures are not certificate-grade (the midpoints are
fine as diagnostics). Fix used in the new witness: integrate the holomorphic
symmetrization `(psi(1/4+it/2) + psi(1/4-it/2))/2`, which equals
`Re psi(1/4+it/2)` on the real path; its poles (t = +-i(2m+1/2)) are far from
the integration rectangle. The imaginary part of the result is asserted to
contain 0.

S2 (endpoint rounding): the overlap integrals use float `max/min` endpoint
arithmetic; the <=4e-15 endpoint error, times an integrand bounded by ~1.3,
is not in the returned ball. Fix: a conservative ENDPOINT_SLOP = 1e-13 is
added to the radius of every overlap-based entry (atoms, g(0), smooth).
[Corrected 2026-06-10: the margin over the worst case is a factor ~10-20,
not 4 orders -- 8 endpoints x ~1e-15 x integrand ~1.3 plus the
U = math.log(n) rounding INSIDE the integrand (sensitivity ~8.3, effect
~2e-15) gives ~1e-14 worst case vs the 1e-13 slop.] Still amply
sufficient: the slop contributes 1e-13 of the 2.2e-9 compressed radius,
5 orders below what the certificate margin can afford.

Neither finding changes any recorded midpoint at the reported precision; both
matter only for the word "rigorous".

## 4. The exact statement certified

For the default late edge and the FIXED basis matrix `B` (25x23 doubles
produced by `active_state()`; old block = first 21 columns, shell = last 2),
whose entries are taken as exact dyadic rationals, let

```text
M_+ = W_inf - sum_{n in {2,3,4,5,7,8,9,11,13,16,17,19}} (2 Lambda(n)/sqrt(n)) T(log n)
            - (2 log23/sqrt23) T(log 23)
            - P_smooth([b23, r]),
```

where `T(U)` is the exact Toeplitz atom (compact physical overlap), `P_smooth`
the smooth-prime operator with density `2 e^{U/2}`, `b23` the double
`3.1771850203986753` (= 0.5(log23+log25) rounded), `r` the double `3.24`, and

```text
W_inf(i,j) = -g_ij(0) log pi + (1/pi) int_0^inf phihat_i(t) phihat_j(t)
             Re psi(1/4 + i t/2) dt.
```

Claim certified: with `Mc = B^T M_+ B`, `A_+ = Mc[:21,:21]`,
`H = Mc[21:,21:] - C^T A_+^{-1} C`:

```text
A_+ > 0   and   h11 > 0, det H > 0   (hence H > 0 by Sylvester).
```

Why B needs no enclosure: the claim `A_+ > 0 and H > 0` is equivalent to
`x^T M_+ x > 0` for all nonzero `x` in span(B), and the T1 shell statement
"every shell direction y has y^T(S+G)y > 0" IS the Schur statement for this
fixed 21/2 split. The basis is part of the statement, not of the error
budget. What remains interpretive (not rigor): that B approximately satisfies
the pole-kill constraints and approximate L2-orthonormality - i.e. that this
exact statement is a faithful compression of the continuum target. That
caveat already applied to the float pipeline (doc 08 section 9 listed
"enclose the nested L2 basis or use a rationalized fixed basis"; this is the
rationalized-fixed-basis route).

Rigorous W_inf tail lemma (replaces the SciPy envelope; full derivation in
the witness docstring, re-derived by hand this session):

```text
For T > pi/hw and c = hw^2 - pi^2/T^2:
 (i)  |phihat_c(t)| <= 2 pi^2/(t(hw^2 t^2 - pi^2)) <= 2 pi^2/(c t^3), t >= T
      (phihat_c(t) = 2 cos(ct) pi^2 sin(hw t)/(t(pi^2 - hw^2 t^2)); the
      sinc-form implementation equals this closed form, checked analytically
      and asserted numerically);
 (ii) |Re psi(1/4+it/2)| <= log t + log 2 + 1 for t >= 1, from DLMF 5.9.15
      (Binet): psi(z) = log z - 1/(2z) - 2 int_0^inf u/((u^2+z^2)(e^{2pi u}-1)) du,
      |u^2+z^2| >= Im(z^2) = t/4, int u/(e^{2pi u}-1) = 1/24, |z| <= (t+1)/2,
      |z| >= t/2;
 (iii) per-entry tail <= tau(T) = (4 pi^4/(pi c^2)) [(log T + log 2 + 1)/(5T^5)
      + 1/(25 T^5)];  tau(5000) ~ 6.4e-12, consistent with and slightly above
      the witness's numerically integrated envelope 5.953e-12.
```

Pipeline of the new witness (everything after the float `active_state`
bookkeeping is arb ball arithmetic at 120 bits):

```text
1. cross-checks (asserts): phihat forms agree; digamma envelope dominates
   sampled |Re psi|; closed-form tail brackets the numeric envelope; the old
   atom set is exactly the 12 prime powers below e^3; exact-vs-pipeline atom
   weight < 1e-12;
2. ambient balls: g(0) gram, W_inf (Arb integral on [0,T] with holomorphic
   symmetrized digamma + tau(T) added to every radius), 12 old atoms with arb
   von Mangoldt weights, atom(23) with weight 2log23/sqrt23, smooth suffix;
   ENDPOINT_SLOP=1e-13 added to every overlap entry;
3. compression B^T M_+ B in balls (symmetric-pair intersection, valid since
   the true matrix is symmetric);
4. P0 sanity gate: midpoint endpoint must reproduce the snapshot
   all-arithmetic value eigmin(H)=+2.511097945288e-02 to 5e-6, else ABORT;
5. interval Cholesky of A_+ (success certifies every symmetric matrix in the
   ball family PD, in particular the true A_+);
6. H = D - V^T V with V = L^{-1}C by interval forward substitution;
7. Sylvester decision on the h11 and det H balls; width-budget ledger printed
   in every branch.
```

## 5. Result (run of 2026-06-10, T=5000, prec=120 bits, exit 0; W_inf stage
451 s, everything else < 1 s, ~25 min wall on a loaded machine)

All fail-closed cross-checks PASS. P0 reproduction of the snapshot
all-arithmetic midpoint endpoint is exact to roundoff:

```text
P0 midpoint endpoint: eig(H_mid) = +2.511097945288e-02, +1.918391507057e-01
P0 drift from snapshot all-arithmetic eigmin: 4.295e-15  (limit 5e-6)
```

Certified enclosures:

```text
interval Cholesky: 21/21 pivots strictly positive;
  min pivot lower bound = +6.339944e-03, max pivot rad = 5.09e-06
  => A_+ > 0 CERTIFIED

H = S+G enclosure (Schur complement of the certified A_+):
  h11      = [+3.610295036051e-02 +/- 2.191e-05]
  h12      = [-4.137448376025e-02 +/- 1.391e-05]
  h22      = [+1.808471784946e-01 +/- 8.833e-06]
  det H    = [+4.817268801602e-03 +/- 5.433e-06]
  eigmin(H)= [+2.511099531499e-02 +/- 6.796e-05]

Sylvester: h11 lower bound  = +3.608104133604e-02  (margin/width = 1.65e+03)
           det H lower bound = +4.811836132233e-03  (margin/width = 8.86e+02)
  => H > 0 CERTIFIED
```

Width budget ledger (per ingredient, max |mid| / max radius):

```text
g(0) overlap gram                   +1.324049e-01   1.00e-13
W_inf (T=5000 + tail 6.38e-12)      +8.733919e-02   6.49e-12
old atoms (12 prime powers < e^3)   +9.861777e-02   1.30e-12
atom(23), weight 2log23/sqrt23      +5.271563e-02   1.31e-13
smooth suffix                       +1.067004e-03   1.00e-13
ambient M_+                         +1.074877e-01   8.02e-12
compressed B^T M_+ B                +3.001690e+00   2.21e-09
A_+ Cholesky pivots                 min +6.339944e-03  rad 5.09e-06
H entries                           +1.808472e-01   2.19e-05
det H                               +4.817269e-03   5.43e-06
```

Reading of the ledger: the ambient radii are dominated by the W_inf tail
envelope (6.4e-12) and the deliberate ENDPOINT_SLOP (1e-13); compression
multiplies by the basis l1 factor (~2.8e2); the interval Cholesky /
substitution through the cond~9.4e2 old block costs another ~1e4. Total
amplification ambient -> H is ~3e6, leaving 3 orders of magnitude of slack
against the h11 = 3.6e-2 margin. The conservative uniform-eta budget of
prime_defect_t1_error_budget (3.9e-9 per entry) was ~160x too pessimistic
[corrected 2026-06-10: 6.42e-7 needed / 3.867e-9 budgeted at the T=1500
||dH|| ~ 0.5 eigmin point] about what direct interval Schur computation
needs, as doc 08 suspected.

Robustness and fail-closed gate runs (same script, different --T):

```text
T=1500 (tail 2.33e-09): CERTIFIED, exit 0, but tight:
  h11   = [+3.602212865740e-02 +/- 6.588e-03]  margin/width = 4.47
  det H = [+4.799883932345e-03 +/- 1.669e-03]  margin/width = 1.88
  radius propagation ambient -> H is linear (~3e6 amplification), so
  T=1500 is the practical floor; T<=500 cannot certify det H.
T=60 (tail envelope 2.59e-01, deliberately inadequate): P0 ABORT, exit 2.
  The finite-cutoff midpoint endpoint is wrong (eigmin(H_mid) = -2.27e-01)
  and the construction-drift gate catches it BEFORE any certificate
  language is printed; the ledger shows compressed radii ~7.2e+01.  This
  exercises the fail-closed paths: the script cannot be talked into a
  certificate by starving the cutoff.
```

Note on midpoints: the certified-statement H differs from the default
Fourier-grid floats at the ~2e-4 level (h11: 3.610e-2 vs 3.587e-2), exactly
the known T=250 -> exact W_inf shift (snapshot: +1.99e-4 in eigmin). The
certificate is about the exact statement, not about the grid floats.

## 6. What is and is not certified (honest limits)

Certified, conditional only on Arb/python-flint correctness (rigorous
integration per Johansson's acb_calc, outward-rounded ball ops):

```text
A_+ > 0 and H = S+G > 0 for the EXACT statement of section 4 - i.e. the
default T1 endpoint matrix inequality, with the W_inf tail, all quadrature,
and all linear algebra inside the balls.
```

Not certified / out of scope:

```text
- that the fixed dyadic B is exactly pole-killed or exactly L2-orthonormal
  (interpretive compression-faithfulness caveat, as in the float pipeline);
- anything about refinement bases (T2), other edges, or the finite tower;
- the continuum statement (T4); the reduction obligations (doc 00);
- independence from Arb: no second interval library was run against it.
```

## 7. Next steps

```text
- T2 direction: rerun the same certificate over the refinement bases
  (n17/h0.100 ... n33/h0.045); the machinery is dimension-generic (interval
  Cholesky + 2x2/3x3 Sylvester or pivot-complete Cholesky on H);
- optional hardening: replace the remaining float bookkeeping inputs (cell
  bounds, centers) by rational definitions inside the witness itself;
- optional: cross-validate one W_inf entry against an independent interval
  integrator (e.g. Julia IntervalArithmetic + TaylorModels) to discharge the
  single-library caveat.
```
