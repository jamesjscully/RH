# R - T2 interval sweep: rigorous ball certification of H = S+G > 0 over the refinement bases

Status: executed 2026-06-10, COMPLETE. RESULT: R1 (confirmation branch) --
ALL FIVE refinement bases CERTIFIED (`A_+ > 0` and `H = S+G > 0` by
pivot-complete interval Cholesky, rigorous Arb balls, T=5000, prec=120
bits, every run exit 0).  The `H > 0` endpoint is refinement-stable at
certificate grade at the tested bases, including both 3D shells; per the
pre-registered asymmetry this confirms the floats and discharges T2's
"main weakness" line (3D shells SPD numerically but without rigorous
matrix-entry bounds) AT THE TESTED BASES only.
Witness (new, fail-closed, exit-code gated):
`scripts/numerics/witness/prime_defect_t2_interval_sweep.py`.
Extends the T1 certificate (`prime_defect_t1_interval_certificate.py`,
record `research/work/L-t1-interval.md`) from the default basis n25/h0.060
to all five refinement bases of `prime_defect_active_atom_shift.REFINEMENTS`.
Same epistemic asymmetry as T1, pre-registered in the witness docstring
BEFORE any ball computation ran:

```text
R1 all five CERTIFIED  -> H>0 endpoint refinement-stable at certificate
                          grade AT THE TESTED BASES (T2 "main weakness"
                          discharged there; confirms floats only).
R2 GAP (enclosure straddles 0) -> report width budget + dominating
                          ingredient; cure is cutoff/precision, never a
                          weakened target.
R3 certified negative pivot -> REFUTATION of refinement stability of the
                          H>0 endpoint; major result; escalate.
```

## 1. Where the refinement bases come from (located, step 1)

The TODO.md snapshot table ("Refinement H=S+G evidence") is produced by
`prime_defect_default_t1_certificate.py --refinements` -> `refinement_table()`
-> `certificate(ncenters, hw)` -> `t1_matrices` -> `active_state(ncenters,
hw)` (in `prime_defect_active_atom_shift.py`, `REFINEMENTS = ((17,0.10),
(21,0.08), (25,0.06), (29,0.05), (33,0.045))`).

Basis construction per (ncenters, hw), all on `physical_ngrid = 6001`:

```text
ambient  = build_ambient(ncenters, hw, cmax = 3.24/2 - hw, max_gmax=3.24)
           (prime_nested_cone.build_ambient; centers =
            linspace(0.02, 1.62-hw, ncenters); raised-cosine bumps)
B        = edge_basis(ambient, points, 3.00, 3.24)
           = [left_basis | orthogonal shell]  (prime_defect_residual_control)
old_dim  = points[3.00]["basis"].shape[1]
```

H assembly there (float pipeline): `current = B^T (W_inf - P_exact(<3) -
P_smooth([3,3.24])) B` (no residual cells precede n=23, the smallest atom in
the window, for every basis), then the repair cell `smooth([3, b23]) -
atom(23)` with the grid-derived weight; `H = S + Q - square` via the exact
Riccati identity = Schur complement of the compressed post-cell matrix

```text
M_+ = W_inf - sum_{n<e^3} w_n T(log n) - w_23 T(log 23) - P_smooth([b23, 3.24]),
b23 = 0.5(log23+log25) = 3.1771850203986753 (double), right = 3.24.
```

Verified identical across all five bases (cell bounds, right edge, repair
atom, old-atom set, grid weight vs exact 2log23/sqrt23 within 2e-14):

```text
n17/h0.100  B 17x15  old 13  shell 2
n21/h0.080  B 21x19  old 17  shell 2
n25/h0.060  B 25x23  old 21  shell 2   (= certified T1 default; in-sweep control)
n29/h0.050  B 29x27  old 24  shell 3   (3D shell -> pivot-complete Cholesky)
n33/h0.045  B 33x31  old 28  shell 3   (3D shell -> pivot-complete Cholesky)
```

So the ONLY per-basis changes to the certified T1 statement are the ambient
raised-cosine family (centers, hw) and the fixed dyadic B with its
old/shell split.  The W_inf tail lemma is hw-generic (c = hw^2 - pi^2/T^2 >
0 at T=5000 for every swept hw; tau scales ~1/c^2, x~3.2 at hw=0.045 vs
default).

## 2. Snapshot reproduction (P0 stage 1, float level) -- PASS

`prime_defect_default_t1_certificate --refinements --samples 361` rerun
2026-06-10 reproduces the TODO.md table exactly at printed precision:

```text
n17/h0.100  2  +4.897369e-03   n29/h0.050  3  +5.153857e-02
n21/h0.080  2  +4.989831e-03   n33/h0.045  3  +2.760913e-02
n25/h0.060  2  +2.493626e-02
```

The witness re-derives these internally per basis (gate D1, tol 6e-9 =
7-significant-digit rounding) and ABORTs fail-closed on mismatch.

## 3. Components reused vs rebuilt (vs the T1 certificate / L-doc)

Reused VERBATIM by import from `prime_defect_t1_interval_certificate`:
`atom_matrix_ball`, `smooth_matrix_ball`, `winf_matrix_ball` (holomorphic
symmetrized digamma integrand, S1 fix), `winf_tail_envelope` (rigorous
closed-form tail lemma), `ENDPOINT_SLOP = 1e-13` on every overlap entry (S2
fix), `compress` (symmetric-pair intersection), `interval_cholesky`,
`forward_substitute`, `von_mangoldt_arb`, `OLD_NS_EXPECTED`, ledger
helpers.  All are dimension/center/hw-generic; no numerical code was
modified.

New in the T2 witness:
- per-basis gates D1 (float snapshot reproduction, 6e-9), D2 (statement
  drift: cell/right/repair), D3 (old-atom set), D4 (atom weight vs exact,
  1e-10), D5 (per-basis phihat/digamma/tail cross-checks at the basis hw);
- P0 midpoint drift gate, tol 2e-3 against the FLOAT snapshot eigmin
  (pre-registered: known exact-vs-grid W_inf systematic +1.75e-4 at hw=0.06,
  tail scaling <= x4.5 at hw=0.045 => expected < 1e-3; gross drift is
  orders larger, cf. the starved-T control at -0.227);
- the H-side decision is a PIVOT-COMPLETE INTERVAL CHOLESKY ON H
  (dimension-generic; replaces the 2x2 Sylvester step, as required for the
  3D shells n29/n33; for 2D shells h11/det are also printed as a T1-format
  cross-check);
- per-basis verdict CERTIFIED / GAP / REFUTED / ABORT; exit 0 only if all
  swept bases are definite (CERTIFIED/REFUTED), 1 if any GAP, 2 if any
  ABORT.

Note on the P0 reference: T1's P0 compared against an all-Arb snapshot
midpoint (5e-6).  No such reference exists for the refinement bases, so P0
here gates against the float eigmin with the wider, pre-registered 2e-3
budget; D1 separately pins the float reference to the TODO table at 6e-9.

## 4. Results (T=5000, prec=120 bits)

### n17/h0.100 (old 13, shell 2) -- CERTIFIED, exit 0, wall 245 s

```text
D1 float eigmin(H) = +4.897369044641e-03  (snapshot drift 4.464e-11)
P0 midpoint eigmin(H_mid) = +4.900407990250e-03  (drift from float 3.039e-06)
A_+ interval Cholesky: 13/13 pivots > 0, min pivot lower bound +2.377706e-03,
  max pivot rad 4.88e-07
H = [[+4.343019856907e-02 +/- 9.702e-07, -7.873742961005e-03 +/- 1.034e-06],
     [ .,                                +6.509444156362e-03 +/- 1.101e-06]]
H pivots: 1: [+4.343019856907e-02 +/- 9.702e-07] lower +4.342923e-02  m/w 4.48e+04
          2: [+5.081962114318e-03 +/- 1.508e-06] lower +5.080454e-03  m/w 3.37e+03
det H (pivot product) = [+2.207106237454e-04 +/- 7.041e-08]
ledger: g0 rad 1.0e-13, W_inf rad 9.4e-13 (tail 8.26e-13), old atoms 1.3e-12,
  ambient M_+ 2.5e-12, compressed 3.4e-10, H entries 1.1e-06
```

Note: the n17 midpoint-vs-float drift (3.0e-6) is far below the default
basis's known +1.75e-4 exact-vs-grid W_inf systematic, consistent with the
grid truncation error shrinking at larger hw (envelope ~1/c^2).

### n21/h0.080 (old 17, shell 2) -- CERTIFIED, exit 0, wall 446 s

```text
D1 float eigmin(H) = +4.989831303059e-03  (snapshot gate PASS, tol 6e-9)
P0 midpoint eigmin(H_mid) = +5.000873259151e-03  (drift from float 1.104e-05)
A_+ interval Cholesky: 17/17 pivots > 0, min pivot lower bound +1.408765e-03,
  max pivot rad 4.14e-06
H = [[+3.047638598271e-02 +/- 3.307e-06, -3.863623464657e-02 +/- 4.787e-06],
     [ .,                                +6.359669636723e-02 +/- 6.930e-06]]
H pivots: 1: [+3.047638598271e-02 +/- 3.307e-06] lower +3.047308e-02  m/w 9.22e+03
          2: [+1.461586711614e-02 +/- 2.438e-05] lower +1.459148e-02  m/w 5.98e+02
det H (pivot product) = [+4.454388077036e-04 +/- 7.915e-07]
ledger: W_inf rad 2.1e-12 (tail 2.02e-12), ambient M_+ 3.7e-12,
  compressed 7.9e-10, H entries 6.9e-06
```

### n25/h0.060 (old 21, shell 2; T1 default, in-sweep control) -- CERTIFIED, exit 0, wall 605 s

```text
D1 float eigmin(H) = +2.493625500557e-02  (snapshot gate PASS)
P0 midpoint eigmin(H_mid) = +2.511097945288e-02  (drift from float 1.747e-04
  = the known exact-vs-grid W_inf systematic; EXACTLY the T1 all-arb
  snapshot midpoint, all 13 printed digits)
A_+ interval Cholesky: 21/21 pivots > 0, min pivot lower bound +6.339944e-03,
  max pivot rad 5.09e-06        [identical to the T1 certificate record]
H = [[+3.610295036051e-02 +/- 2.191e-05, -4.137448376025e-02 +/- 1.391e-05],
     [ .,                                +1.808471784946e-01 +/- 8.833e-06]]
H pivots: 1: [+3.610295036051e-02 +/- 2.191e-05] lower +3.608104e-02  m/w 1.65e+03
          2: [+1.334314212861e-01 +/- 6.951e-05] lower +1.333619e-01  m/w 1.92e+03
det H (pivot product) = [+4.817267979224e-03 +/- 5.435e-06]
  [2x2 cross-check det = [+4.817268801602e-03 +/- 5.433e-06], the T1
   certificate's Sylvester det ball verbatim]
```

This is an independent re-derivation of the T1 certificate through the new
pivot-complete-H code path; h11 / det / A_+ pivot data agree
digit-for-digit with the certified T1 record, validating the T2
orchestration against a known answer.

### n29/h0.050 (old 24, SHELL 3 -- first 3D pivot-complete case) -- CERTIFIED, exit 0, wall 772 s

```text
D1 float eigmin(H) = +5.153856876351e-02  (snapshot drift 1.236e-09)
P0 midpoint eigmin(H_mid) = +5.161336637491e-02  (drift from float 7.480e-05)
A_+ interval Cholesky: 24/24 pivots > 0, min pivot lower bound +2.351212e-02,
  max pivot rad 9.34e-06
H (3x3 enclosure, radii <= 2.4e-05):
  [+1.569268377725e-01  -8.969755426120e-02  +2.054475609952e-03]
  [ .                   +1.325308310810e-01  +5.892792406218e-02]
  [ .                    .                   +8.661559292477e-01]
H pivots: 1: [+1.569268377725e-01 +/- 1.609e-05] lower +1.569108e-01  m/w 9.75e+03
          2: [+8.126075152045e-02 +/- 3.700e-05] lower +8.122375e-02  m/w 2.20e+03
          3: [+8.216760773715e-01 +/- 8.883e-05] lower +8.215873e-01  m/w 9.25e+03
det H (pivot product) = [+1.047800739884e-02 +/- 6.979e-06]
ledger: W_inf rad 1.3e-11 (tail 1.32e-11), ambient M_+ 1.5e-11,
  compressed 5.3e-09, H entries 2.4e-05
```

### n33/h0.045 (old 28, SHELL 3) -- CERTIFIED, exit 0, wall 953 s

```text
D1 float eigmin(H) = +2.760913442420e-02  (snapshot drift 4.424e-09)
P0 midpoint eigmin(H_mid) = +2.784990566297e-02  (drift from float 2.408e-04)
A_+ interval Cholesky: 28/28 pivots > 0, min pivot lower bound +1.126795e-02,
  max pivot rad 5.85e-05
H (3x3 enclosure, radii <= 1.3e-04):
  [+3.558531961309e-01  -1.551411375864e-01  +2.928753859464e-01]
  [ .                   +1.029604539168e-01  -1.187791047532e-01]
  [ .                    .                   +5.146293164283e-01]
H pivots: 1: [+3.558531961309e-01 +/- 6.483e-05] lower +3.557884e-01  m/w 5.49e+03
          2: [+3.532364170176e-02 +/- 2.149e-04] lower +3.510878e-02  m/w 1.63e+02
          3: [+2.713404678759e-01 +/- 3.277e-04] lower +2.710128e-01  m/w 8.27e+02
det H (pivot product) = [+3.410758038093e-03 +/- 2.552e-05]
ledger: W_inf rad 2.0e-11 (tail 2.02e-11), ambient M_+ 2.2e-11,
  compressed 1.0e-08, H entries 1.2e-04
```

The sweep-wide tightest enclosure is n33 pivot 2 (margin/width 1.63e+02) --
still two orders of magnitude of slack; the radius chain confirms the
L-doc's amplification picture (ambient ~2e-11 -> compressed ~1e-08 (basis
l1 factor) -> H ~1e-04 (old-block solve), growing with basis size/cond).

## 4b. Sweep verdict table

```text
basis        old+shell  float eigmin   mid eigmin    P0 drift   verdict    min H pivot lower  worst m/w   wall
n17/h0.100   13+2       +4.897369e-03  +4.900408e-03  3.04e-06  CERTIFIED  +5.080454e-03      3.37e+03    245s
n21/h0.080   17+2       +4.989831e-03  +5.000873e-03  1.10e-05  CERTIFIED  +1.459148e-02      5.98e+02    446s
n25/h0.060   21+2       +2.493626e-02  +2.511098e-02  1.75e-04  CERTIFIED  +3.608104e-02      1.65e+03    605s
n29/h0.050   24+3       +5.153857e-02  +5.161337e-02  7.48e-05  CERTIFIED  +8.122375e-02      2.20e+03    772s
n33/h0.045   28+3       +2.760913e-02  +2.784991e-02  2.41e-04  CERTIFIED  +3.510878e-02      1.63e+02    953s
```

All P0 midpoint drifts are well inside the pre-registered 2e-3 budget and
follow the predicted hw-scaling of the exact-vs-grid W_inf systematic
(largest at the smallest hw).  All D1 snapshot reproductions passed at
tol 6e-9 (worst 4.4e-9, at n33).  No GAP, no ABORT, no negative pivot.

Runtime: wall time is dominated by the W_inf Arb integration stage
(220-907 s, scaling with ncenters^2); every other stage < 1 s.  The five
bases were run as independent processes (n17 first end-to-end as the
cheapest pilot, then n21/n25/n29/n33 in parallel on a 20-core box); full
sweep wall clock ~25 min.  Logs: /tmp/t2_n17.log ... /tmp/t2_n33.log.

## 5. Honest limits

- Certificates are relative to each FIXED dyadic basis B taken as exact
  (same compression-faithfulness caveat as T1/L-doc section 4); they say
  nothing about bases not swept, the finite tower, or the continuum.
- Single interval library (Arb / python-flint); no independent
  cross-validation run.
- Confirmation branch only confirms the floats (pre-registered asymmetry);
  the R1 risk-ladder verdict on the asymptotic mechanism is untouched.
- The five bases share the SAME late edge and the same exact statement
  ingredients; refinement stability is certified in basis resolution
  (ncenters, hw), not across edges or window placements.
- P0 here gates against the float snapshot (2e-3), weaker than T1's
  all-Arb-reference gate (5e-6); the float reference itself is pinned to
  the TODO table by D1 at 6e-9.  No starved-T abort control was rerun for
  the new bases (the T1 T=60 control exercises the same code path, since
  the gate logic is shared).

## 6. Suggested follow-ups (not started)

- TODO.md: mark the T2 H>0-endpoint certification done at the five tested
  bases; the remaining T2 items (dimension-independent certificate, KKT in
  dim>2, uniform anti-concentration constants) are untouched.
- Optional: one Julia IntervalArithmetic cross-check of a single W_inf
  entry to discharge the single-library caveat for both T1 and T2.
