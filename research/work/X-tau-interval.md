# X - tau interval certification: rigorous per-edge balls for the doc-13 tracking criterion

Status: executed 2026-06-10, COMPLETE. RESULT: X1 (confirmation branch) --
ALL FOURTEEN edges of the doc-13 computed ladder CERTIFY `A > 0`, `M_c > 0`,
`BULK > 0` and `S_N > 0` by rigorous Arb ball arithmetic (T=5000, prec=120
bits), hence `tau < 1` holds CERTIFICATE-GRADE on every computed edge (exact
pencil equivalence, no rank hypothesis). The DH negative control certifies
the expected violation (`x^T S_N x < 0` rigorously) on its one living edge.
Per the pre-registered asymmetry this confirms the doc-13 floats and makes
the finite side of the tracking equivalence (RH <=> uniform tau < 1,
research/proof/13-tracking-equivalence.md sections 3-4') rigorous AS FAR AS
COMPUTED; it proves nothing asymptotic, and doc 13's wall (no estimate-based
route to uniform tau < 1) stands untouched.

Witness: `scripts/numerics/witness/prime_edge_tau_interval.py` -- INHERITED
from a cut-off predecessor session (script complete-looking but never run to
completion; this doc never written). This session audited it, fixed five
defects (section 3), ran it to completion, and recorded the results. The
fresh-context discipline was: do not believe any output until the statement
discipline and enclosure chain were re-derived against the certified T1/T2
component library (`prime_defect_t1_interval_certificate.py`,
records `research/work/L-t1-interval.md`, `research/work/R-t2-interval-sweep.md`).

## 1. What is certified, exactly

For each edge `L -> R` of the doc-13 ladder (`cmax=2.42, ncenters=38,
hw=0.06`, gmaxs `1.60 .. 4.96`), with the FIXED float matrices `B = [Ql |
shell]` (nested pole-killed edge basis of `prime_ladder_scaling`) and `U2`
(top-2 left singular basis of the stacked cell couplings) taken as EXACT
dyadic rationals (statement data, same discipline as T1/T2), and the exact
ambient operators enclosed in Arb balls (W_inf with holomorphic-symmetrized
digamma on [0,T] plus the rigorous closed-form tail lemma; exact Toeplitz
atoms with exact von Mangoldt weights `2 Lambda(n)/sqrt(n)`; smooth cells of
density `2 e^{U/2}` on the float-midpoint cell bounds taken as exact
endpoints; `ENDPOINT_SLOP = 1e-13` on every overlap entry):

```text
A    = old-old block of B^T (W_inf - sum_{log n < L} w_n T(log n)) B
C_N, D_N = old-shell / shell-shell blocks at R;  S_N = D_N - C_N^T A^{-1} C_N
BULK = S_0 + sum E_D + B_m M_c^{-1} B_m^T          (doc-13 BULK_2)
tau  = 1 - lambda_min( pencil(S_N, BULK) )
```

Certified per edge: `A > 0`, `M_c > 0`, `BULK > 0`, `S_N > 0` (each by
interval Cholesky, the A-step congruence-preconditioned, section 3), plus a
two-sided `[tau]` enclosure (certified shift bisection for the lower spectral
bound, ball Rayleigh quotient at the float eigenvector for the upper bound).
Given `BULK > 0`, `tau < 1 <=> S_N > 0` EXACTLY -- no rank hypothesis -- so
the certified object is doc 13 section 4''s exact-hypothesis criterion. The
frozen-A statement (`E_A = 0` exactly, so A at L IS the old-old block at R)
is the support lemma, gated: G3 checks `L - 2*(max old center + hw) >= 1e-3`
against the same center-selection predicate `nested_basis` uses, which makes
every window atom/smooth overlap on old x old EMPTY analytically (re-derived
this session: for `U >= L`, `U + s_j - s_i >= 2 hw + 1e-3 > 2 hw` for all
four sign pairs); the compressed `E_A` balls must additionally contain 0.

The rank-2 PACKAGING of doc 13 (`tau_2 = lambda_max[M_c^{1/2} W^T BULK^{-1}
W M_c^{1/2}]`) is also enclosed per edge, with one honest deviation recorded:
the witness's `V` is the A^{-1}-orthogonal projection coefficient
`(M_c^{-1} U2^T A^{-1} G)^T`, not `prime_edge_rank2_exact`'s Euclidean
projection `G^T U2`; the two coincide under the exact rank-2 hypothesis and
differ by `O(G_perp)` off it. Both the doc-11 rank residual `||R'||_F` and
`||G_perp||_F` are enclosed and reported per edge. The decision NEVER uses
the rank-2 form; it is diagnostic.

## 2. Pre-registered readings (in the witness docstring before any ball ran)

```text
X1 CONFIRMATION: every swept edge certifies A>0, M_c>0, BULK>0, S_N>0,
   hence tau < 1 rigorously; confirms the floats, nothing asymptotic.
X2 GAP: some enclosure straddles its threshold; report width budget +
   dominating ingredient; cure is cutoff/precision, never a weakened target.
X3 VIOLATION (major): certified tau > 1 somewhere on the zeta ladder;
   demands an independent re-derivation pass BEFORE recording; escalate.
```

Verified present in the inherited docstring (nothing had to be restored).
Outcome: X1, with one transient X2 episode that was a certification-method
artifact, not an enclosure-width wall (section 3, fix 5; section 4).

## 3. Audit of the inherited script (findings and fixes)

The enclosure chain was re-derived from scratch and found SOUND:

```text
S1 ainv_product (verified Schur products): P^T A^{-1} Q = Xp^T Q + Ep^T Xq
   + Ep^T A^{-1} Eq with float-preconditioner Xp,Xq exact dyadics and
   E* = * - A X* enclosed in balls; identity checked by hand (needs A
   symmetric -- true); third term bounded by ||Ep_i|| ||Eq_j|| / lamA_lo
   with lamA_lo a CERTIFIED lambda_min lower bound. Sound.
S2 lambda_min_lb: shifted interval Cholesky -- success on A - mu I
   certifies every symmetric member PD, in particular the true A. Sound.
S3 pencil enclosures: lower bound = certified-PD shift bisection (the
   "good" endpoint is always a certified bound regardless of the "bad"
   endpoint); upper bound = ball Rayleigh quotient at a float vector with
   ball-certified positive denominator. Sound.
S4 reball / cache: cached (mid, rad) doubles re-inflated with rad*(1+1e-9)
   + |m|*3e-16 + 1e-300 -- covers nearest-rounding of both components.
   Sound. (The /tmp cache was verified empty of predecessor artifacts
   before the first run; every cache file used was produced this session.)
S5 G3 support gate: uses the SAME selection predicate (centers + hw <=
   L/2 + 1e-12) as nested_basis, and the margin assert fails closed if the
   1e-12 tolerance ever admits a boundary center. Sound.
S6 float usage: every np.linalg call is float-stage statement data, a
   preconditioner, a midpoint diagnostic (P0), or a witness vector whose
   quadratic form is re-evaluated in balls. No float inverse is
   load-bearing. The X3 branch requires a BALL-certified negative
   Rayleigh quotient (upper(x^T S_N x) < 0).
S7 float norm guards (col_norm_upper, bm_fro_upper): double arithmetic
   with (1+1e-12) slop; worst accumulated rounding for the <= ~1.4e3-term
   positive sums is ~3e-13 < 1e-12. Adequate; noted as the only places
   where float rounding enters a radius bound.
```

Defects found and FIXED (all recorded in the witness docstring AUDIT RECORD):

```text
F1 ctx.prec clobber (fidelity, not soundness): build_ladder's
   _digamma_grid sets ctx.prec = 80 globally; the inherited flow then ran
   the ENTIRE ball stage (workers, compression, Cholesky, bisection) at 80
   bits regardless of --prec, and mislabeled the p120 cache tag. Arb stays
   outward-rounded at any precision, so no past output would have been
   wrong, only wider. Fixed: ctx.prec restored right after the ladder build.
F2 single-proc mode ignored --prec (module-default 120 hardcoded). Fixed.
F3 DH-control verdict semantics were inverted relative to the docstring's
   own control contract: a certified DH violation is the control PASSING,
   a DH tau<1 certificate means the frame is dispersing. The inherited
   code would have printed the X3 "escalate" language and exited 0 for
   the expected control outcome. Fixed: dedicated control branch, exit 0
   pass / 3 dispersing / 1 inconclusive.
F4 no cheap validation path: --float-only added (gates G1-G5, no balls).
F5 A>0 step was interval Cholesky DIRECTLY on the cond ~1e5..1e6 old
   block. Sound but width-fragile: entry radii ~3e-9 compound by ~cond,
   and the first full sweep returned spurious X2 GAP-A on the three last
   edges (eigmin(A) ~ 3e-4..3e-5 float). Fixed by Rump-style congruence
   preconditioning (pd_certify): with Y the float triangular inverse of
   the midpoint Cholesky factor, exactly lower-triangular with nonzero
   diagonal hence an exact nonsingular dyadic, A - mu I > 0 <=> Y (A - mu
   I) Y^T > 0 (Sylvester inertia), and the preconditioned ball matrix ~ I
   admits interval Cholesky easily. Decisions remain entirely in ball
   arithmetic. This is the one mathematically substantive repair.
```

Gate verification (this session, before the ball runs): the two float
pipelines were rerun in full. `prime_edge_tracking` reproduces doc 13
exactly (zeta tau < 1 all 14 edges; DH edge 1: tau = 1.554, eigmin(S_N) =
-0.282; DH old block dead on all later edges). `prime_edge_rank2_exact`
reproduces tau_2 max 0.9539 at 4.00->4.26 and all eight late-edge values
pinned in REFERENCE_TAU2 digit-for-digit; the six early-edge reference
values reproduce through the witness's own float stage (G1 PASS at 5e-5 on
all 14). G2 (pencil-vs-rank2) measured <= 3.3e-5 as pre-registered, and is
EXACT (1e-16) on edges where the cell stack has rank <= 2, as it must be.

## 4. Results (final clean run, one code version: T=5000, prec=120, 18 procs)

Per-edge certified balls, zeta ladder (all CERTIFIED, exit 0):

```text
edge        dl+ds  float    [tau] enclosure        width    margin  lamSN_lb   lamA_lb    P0 drift
            .      tau_2    .                      .        to 1    .          .          .
1.60->1.88  10+2   0.7900   [0.789932, 0.789932]   6.4e-07  0.2101  7.77e-02   3.45e-02   9.7e-05
1.88->2.10  12+1   0.5749   [0.574759, 0.574759]   2.0e-07  0.4252  3.17e-01   3.17e-02   1.1e-04
2.10->2.30  13+2   0.8049   [0.804761, 0.804761]   1.3e-07  0.1952  6.87e-02   2.61e-02   1.2e-04
2.30->2.52  15+2   0.8025   [0.802065, 0.802066]   8.4e-07  0.1979  4.73e-02   2.31e-02   4.2e-04
2.52->2.76  17+2   0.6996   [0.698573, 0.698584]   1.1e-05  0.3014  2.56e-02   1.11e-02   1.0e-03
2.76->3.00  19+1   0.8364   [0.835844, 0.835851]   7.0e-06  0.1641  1.07e-01   6.09e-03   5.2e-04
3.00->3.24  20+2   0.8659   [0.864786, 0.864825]   3.9e-05  0.1352  2.72e-02   4.45e-03   1.1e-03
3.24->3.50  22+2   0.7249   [0.724536, 0.724560]   2.4e-05  0.2754  2.02e-02   2.46e-03   3.1e-04
3.50->3.76  24+2   0.8163   [0.813728, 0.813756]   2.8e-05  0.1862  2.13e-02   2.03e-03   2.6e-03
3.76->4.00  26+2   0.9173   [0.915612, 0.915668]   5.6e-05  0.0843  2.93e-03   1.12e-03   1.7e-03
4.00->4.26  28+2   0.9539   [0.951471, 0.952146]   6.8e-04  0.0479  2.30e-03   7.59e-04   2.1e-03
4.26->4.50  30+2   0.8094   [0.801764, 0.803332]   1.6e-03  0.1967  1.66e-03   4.40e-04   6.8e-03
4.50->4.76  32+2   0.2574   [0.213961, 0.272891]   5.9e-02  0.7271  2.03e-03   3.80e-04   1.3e-02
4.76->4.96  34+2   0.2763   [0.198934, 0.326252]   1.3e-01  0.6737  1.49e-03   3.23e-04   8.3e-03
```

(Values from the final clean `--edges all` run of 2026-06-10, exit 0,
`/tmp/x_tau_final.log`; the earlier per-edge runs reproduce every ball to
the printed digits.)

Headline: the TIGHTEST edge (4.00->4.26, float tau_2 = 0.9539, the doc-13
maximum) certifies `[tau] = [0.951471, 0.952146]`, width 6.8e-4,
margin-to-1 = 0.0479 -- seventy widths of slack. Every edge's
`S_N > 0` is certified outright (lambda_min lower bounds 1.5e-3 .. 3.2e-1),
which is the exact decision; the `[tau]` balls are the quantitative record.

Float-reproduction check vs doc 13: P0 midpoint-vs-float drifts are
1e-4 .. 1.3e-2, growing with edge (consistent with the known Fourier-grid
T_grid=250 truncation systematic ~1e-6/entry amplified through eigmin(A) ~
3e-4..3e-5 on late edges), all far inside the pre-registered 5e-2 budget
and orders below any decision threshold. The certified-statement midpoints
sit systematically ~2e-3 BELOW the grid floats on late edges -- same
exact-vs-grid W_inf shift seen in T1/T2.

Width anatomy: ambient radii are tail-dominated (W_inf 6.5e-12 at T=5000;
overlap entries at the 1e-13 slop); compression by the 38xdim basis costs
~500x (l1^2); the verified Schur step through A costs ~100x (NOT the
worst-case cond ~1e5 -- the residual-preconditioned product realizes the
true sensitivity); the late-edge [tau] width is dominated by the BULK
enclosure through M_c^{-1} (compliance alpha ~ 400 amplifies) and by the
pencil-bisection resolution against BULK radii ~1e-4. The widths grow
exactly as compliance blow-up predicts (doc 12 section 5), from 1e-7
(early) to 1e-1 (last edge) -- still decision-grade everywhere because the
margins are O(1).

The rank-2-form diagnostic balls are tight wherever the coupling stack is
near rank 2 and loose where M_c is tiny relative to its radius (worst:
4.00->4.26, `[tau_2 rank-2] = [0.71, 1.71]` straddling 1 while the
DECISION ball [tau] has width 6.8e-4). This is the packaging's
ill-conditioning, not the criterion's: `||R'||_F <= 1.5e-2` there. Doc 13's
scalar narrative survives at certificate grade only in its pencil form;
recorded as a caution against quoting the rank-2 factorization as the
certified object.

DH negative control (`--dh-control`, float weights as exact statement
data): on the one edge where DH's old block is alive (1.60->1.88; doc 13's
one-mode tau = 1.554, pencil/rank-2 packaging of the same failure = 1.3458),
the machinery certifies `A > 0`, `BULK > 0`, a certified
`[tau] = [1.345619, 1.345619] > 1` (width 1.4e-7), and a ball-negative
Rayleigh quotient `x^T S_N x <= -2.822e-01 < 0` -- matching doc 13's
eigmin(S_N) = -0.282. A CERTIFIED tracking violation exactly where doc 13
says one exists: control PASS (exit 0); the frame separates zeta from DH at
certificate grade; the certification is not dispersing.
(See `/tmp/x_tau_dh.log`.)

## 5. Reused vs new inventory

Reused VERBATIM by import from `prime_defect_t1_interval_certificate`
(certified library, L/R records): `atom_entry_ball`, `smooth_entry_ball`,
`winf_entry_ball` (S1 holomorphic-symmetrization fix), `winf_tail_envelope`
(rigorous closed-form tail lemma), `ENDPOINT_SLOP` discipline (S2),
`compress` (symmetric-pair intersection), `interval_cholesky`,
`forward_substitute`, `von_mangoldt_arb`, ledger helpers; plus
`arb_phi_hat` / `winf_tail_bound` from `prime_defect_t1_winf_tail` for the
G5 cross-checks. No numerical-kernel code was modified.

New in this witness (statement level): the edge bases B / coupling bases U2
as fixed statement data with gates G1-G4; the frozen-A support gate G3; the
residual-preconditioned verified Schur products (`ainv_product`); the
congruence-preconditioned PD certification (`pd_certify`, this session);
back-substitution + SPD solve for the 2x2 M_c; pencil shift-bisection
enclosures; the per-edge X1/X2/X3 verdict machinery and the DH-control
branch; `/tmp/x_tau_cache` ambient cache with multiprocessing workers.

Runtime: ladder + float gates ~2 min; ambient cache build (g0 741 entries,
W_inf 741 Arb integrals to T=5000, 47 atom matrices, 44 smooth cells) ~2
min wall on 18 procs (W_inf ~0.5 s/entry); per-edge ball algebra seconds
(early) to ~3 min (4.76->4.96, dl=34: dominated by the dl^3 ball products
in ainv_product/pd_certify and the 60-step pencil bisections). Full sweep
from cold cache ~15 min wall; from warm cache ~10 min. Logs:
`/tmp/x_floatonly.log`, `/tmp/x_tau_edge400.log`, `/tmp/x_tau_all.log`
(pre-fix-5 run with the three GAP-A), `/tmp/x_tau_late.log`,
`/tmp/x_tau_final.log`, `/tmp/x_tau_dh.log`.

## 6. Honest limits

```text
- Certificates are relative to the FIXED float bases B and U2 taken as
  exact dyadics (compression-faithfulness caveat exactly as in T1/T2: that
  B approximately pole-kills and is approximately L2-orthonormal is
  interpretation, not rigor), and to the float cell bounds / edge
  endpoints as exact statement data.
- Computed-ladder-only: 14 edges, R <= 4.96, one basis family
  (38/hw=0.06/cmax=2.42). NO asymptotic claim of any kind; doc 13's
  conclusion that no estimate-based route reaches uniform tau < 1 is
  untouched (and is the program's own wall). The certified X1 outcome is
  epistemically the WEAK branch of the pre-registered asymmetry.
- Single interval library (Arb / python-flint); rigor is conditional on
  acb_calc and outward-rounded ball ops being correct. No independent
  interval library was run.
- The B/U2 statement data are produced at run time by the deterministic
  float pipeline on this machine and pinned only through G1 (5e-5) /
  G2 / P0; a different BLAS could produce a (slightly) different exact
  statement. The certified inequality is about the bases of THIS run.
- The [tau_2 rank-2 form] diagnostic uses the A^{-1}-orthogonal projection
  V (coincides with doc-13's V under the exact rank hypothesis); its ball
  straddles 1 on the tightest edge and must not be quoted as certified.
- The DH control certifies the violation with DH's float atom weights
  taken as the statement (they are definitional for DH, not approximations
  of an arithmetic quantity).
```

## 7. Suggested follow-ups (not started)

```text
- TODO.md: record that the finite side of the doc-13 equivalence is now
  certificate-grade on the computed ladder (max certified tau upper bound
  0.952146 at 4.00->4.26).
- Optional: tighten the late-edge [tau] balls (the BULK/M_c^{-1} stage
  dominates; a residual-preconditioned product for M_c^{-1}B_m^T analogous
  to ainv_product would cut the 4.76->4.96 width ~10x). Not needed for
  any current decision.
- Optional: one cross-validation of a W_inf entry in an independent
  interval library (Julia IntervalArithmetic), discharging the
  single-library caveat for T1/T2/X simultaneously.
```
