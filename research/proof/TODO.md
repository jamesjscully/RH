# Proof Todo Tracker

Purpose: keep the proof program oriented around theorem-shaped checkpoints, not around an
ever-growing list of diagnostics. Diagnostics stay here only when they change the theorem target or
define a fail-closed test.

## Risk Ladder (2026-06-09 reorganization)

Order of work = order of assumptions by (probability of killing the program) x (cheapness of the
test). Highest-risk, cheapest-to-test first. Each rung is fail-closed: a negative outcome kills or
reshapes the target, and that is the point.

### R0 - The reduction is recorded, not certified

`00-reduction-to-rh.md` now states `nested target => RH` with obligations O1-O4 (normalization
audit, pole-term vanishing, off-line detection, CC20 base-case anchor). Provenance: CC20
arXiv:2006.13771 + Weil's converse. Risk: low (classical technology), but load-bearing - until
written, the program could drift onto a target that no longer implies RH. Also fixes the program's
one-line shape: **extend CC20's archimedean Sonin positivity past support log 2, paying with exact
Euler atoms.**

### R1 - The asymptotic-mechanism risk (HIGHEST; attack first)

The current candidate lemmas (sectoral edge-cone, atom placement, single-repair-atom) are built
from one late edge at R ~ 3.24. Two facts say the mechanism as phrased cannot be the asymptotic
mechanism:

```text
- cells near the edge have width ~ e^{-R}, and the window (L,R] contains ~ e^R atoms:
  single-atom repair degenerates into statistics of many atoms = the transgression
  int F phi' again, F = psi(e^U) - e^U;
- unconditional bounds on F are exponentially insufficient: |phi F| ~ e^{U/2 - c sqrt(U)}
  diverges relative to any O(1) Schur margin, so no absolute-value, cell-by-cell estimate
  can close the storage step at large R.
```

Two prongs, both cheap relative to what they decide:

```text
R1a (pencil): the inverse analysis. Quantify the candidate sectoral lemma over all
     edges L < R as R -> infinity and derive what it implies about F. If it implies
     psi(x) - x = O(x^{1/2+eps}) it is RH-equivalent, geometry alone can never deliver
     it, and the program must identify the weaker-arithmetic + stronger-geometry split.
R1b (numeric): the scaling ladder. Extend the nested chain to R ~ 4.5-6. Track per edge:
     eigmin(A) (induction margin), Riccati square cost, repair surplus
     (eigmin(H) / beta surplus), number of atoms participating in repair, DH control.
     Fail-closed: if the surplus decays faster than the margin, or repair stops being
     single-atom, the current lemma shape dies and the target reforms at the
     aggregated/statistical level.
```

Do R1 before investing further in T1 polish.

**R1 OUTCOMES (2026-06-09, see `09-inverse-analysis.md`):**

```text
R1b executed (prime_ladder_scaling.py, R to 5.90): zeta positive on all 18 edges,
    DH dead on all 18; eigmin(A) ~ e^{-1.5 R}; chronological peak debt grows to
    ~17 vs final margins ~3e-3; repair concentration falls past R~5.
R1a executed: (i) margins exponentially small => slack-bearing estimates can
    never close the induction; certificates must be exact-identity + terminal
    sign (KYP shape). (ii) Cluster obstruction: per-cell repair lemmas are
    unconditionally false at scale (Maynard triples). (iii) Window dial: the
    unconditional arithmetic input is short-interval PNT at the 7/12 scale; the
    remainder is the zero-side oscillation - conservation of difficulty located.
NEW PROBES: one-place passivity proposed and REFUTED same day
    (prime_single_place_passivity.py); drop-one/KMS rigidity
    (prime_interference_rigidity.py): every place and every atom individually
    necessary; positivity only at beta=1/2 (fails both sides). Positivity is an
    irreducibly collective interference lattice; support filtration is the only
    admissible induction coordinate.
NEXT (new R1 front): the killing-direction / repair-matrix characterization
    (09 section 6'.4) - do partial-sum killing directions have a multiplicative
    / free-semigroup combinatorial skeleton?

R1 CLOSED (later 2026-06-09, 09 sections 6''-6''''): resonance dictionary CONFIRMED
    (killing directions are frequency combs, repair = equidistribution of {log p},
    sign-match 1.000); margin law is arithmetic (W_inf alone dies at gmax~2.3,
    smooth surrogates permanently indefinite, only exact atoms positive); O1
    discharged numerically (explicit formula to 4.4e-13); and the CLOSURE: tested
    against admissible profiles the finite phenomenology telescopes to the explicit
    formula exactly (form eigmin = spectral min over actual zeros, validated).
    PHENOMENOLOGY PHASE COMPLETE - no further finite-window experiment can add
    proof content. The program's sole remaining shape: the prime-side realization
    (09 section 6''''.3), with inputs {free semigroup on log p, KMS beta=1/2,
    Lambda>=0, digamma supply} and graveyard guards {Conrey-Li, circular trace,
    subset inductions}.
```

### R-TRACK - The tracking theorem (THE front target as of 2026-06-09, end of session)

Final exact form of the program (proof/12 section 5, validated to 2e-5):

```text
Along the support filtration, the arithmetic transgression vector v (Chebyshev
transgressions of the edge-convolution profiles) must track the geometrically
determined point -b/alpha within radius sqrt(bulk/alpha):

    alpha (v + b/alpha)(v + b/alpha)^*  <=  S_0 + sum E_D + b b^*/alpha.
```

Sub-targets, in order: (1) compute the trajectory of -b/alpha and v along the
ladder (witness: prime_edge_compliance.py extended) - does v visibly track?
DH control: its v must not track. (2) Express -b/alpha analytically (it is
archimedean/old-history data; the resonance dictionary of 09 section 6'' should
give its leading form). (3) The tracking theorem itself: equidistribution of
prime-power atoms against edge-convolution profiles at the rate alpha grows -
this is where the arithmetic (zero-density / short-interval inputs identified in
09 Finding 3) must finally enter. All prior kills constrain the proof shape:
statistical not cell-wise; all places jointly; beta = 1/2 only; exact identities
plus terminal sign only.

### R-KYP - The realization rung (the post-R1 front)

Target: a prime-side positive structure whose energy identity is the explicit formula.
Concrete first sub-tasks:

```text
1. Transcribe the chronological storage chain (T0/05 identities) into the
   spectral coordinate and determine what functional of the truncated data the
   numerically-working debt Pi_j = (-S_j)_+ corresponds to; look for a closed
   form. (KYP: contractivity <=> existence of Pi; the realization supplies Pi.)
2. Formalize the free-semigroup + KMS_{1/2} frame: the prime side as the
   canonical state on the multiplicative shift semigroup at critical weight;
   ask what positivity the frame gives UNCONDITIONALLY and where it stops.
3. O3/O4 of doc 00 in parallel (paper work, certifies the reduction).
```

SECOND RESULT (2026-06-09, fail-closed, doc 10 section 6): S2 split executed.
The shift(correlation)/corner(autoconvolution) channels are BOTH indefinite
against W_inf alone; only their sum is positive, and edge atoms are pure
corner. No channel decomposition isolates a passive subsystem (guard G6).
The realization must be place-global AND channel-global; its natural home is
the dilated full-line even model (translations unitary, corner = boundary).

FIRST RESULT (2026-06-09, fail-closed): the naive anti-causal closed form
`Pi_j = (-Q_{F_j}[X_j])_+` with `F_j = sum_{k>j} E_k` through the FROZEN response
map X_j FAILS on every tested edge (KYP violation ~ the raw debt itself;
monotonicity also broken). The exact telescoping
`S_N - S_j = sum_{k>=j} (Q_{E_k}[X_k] - R_k^T A_{k+1}^{-1} R_k)` is not
perturbative in the X-drift or the Riccati squares at any tested scale.
Conclusion: the storage is genuinely path-dependent — the realization must be
state-space (track the evolving response map), not a formula in the future
residual. This rules out the last "cheap" version of R-KYP.

### R2 - The certification rung (refutation-grade)

T1 below. Its epistemic value is asymmetric: the finite model is a compression of the continuum
form, so certified `H <= 0` would refute the local mechanism, while certified `H > 0` only confirms
the numerics. Finish it, in the background, after R1 is moving.

### R3 - Generalization rungs

T2 (refinement stability), T3 (general finite storage - restate as the debt-decay inequality
`(-S_{j+1})_+ <= (-S_j)_+ - repair + square`, since bare existence of Pi_j with
`S_j+Pi_j>=0, Pi decreasing, Pi_N=0` is *equivalent* to `S_N >= 0` via `Pi_j = sum_{k>=j} (-S_k)_+`
and therefore carries no content), T4 (continuum).

## Guiding Risk

The central unproved implication is:

```text
Schur-negative sector
  => old-predictable shell direction
  => bounded terminal-edge leverage / terminal anti-concentration
  => edge-convolution beta surplus
  => exact Euler repair pays debt + Riccati square + leakage.
```

In the default finite model we found a stronger endpoint than this implication: the exact
active-23 post-repair matrix `H=S+G` is already positive definite on the whole two-dimensional
shell. The near-term strategy is therefore:

```text
1. certify the default H>0 matrix endpoint fail-closed;
2. keep the sector/KKT/beta argument as the geometric explanation and generalization path;
3. only then ask whether H>0, or a weakened sectoral version of it, persists in the finite tower.
```

## Theorem Ladder

### T0 - Finite Algebra Foundation

Status: mostly stable.

Goal:

```text
S_{M+E} = S_M + Q_E[X] - R^* A_+^{-1} R
```

with correct signs and block conventions.

Done:

```text
- finite Schur/Riccati identity is isolated in 05-finite-riccati-identity.md;
- smooth-new residual coordinate is fixed:
  M_base = W_inf - P_exact(<L) - P_smooth([L,R]);
- exact residual cells are E_j = P_smooth_cell(j) - P_atom(j).
```

Keep as guardrails:

```text
- do not treat the smooth model as a positivity baseline;
- do not drop the negative Riccati square;
- do not demand local PSD residual increments.
```

### T1 - Default Active-23 Matrix Certificate

Status: floating-point certificate found; interval certificate pending.

Finite theorem to prove/certify:

```text
For the default finite late edge 3.00->3.24 and repair cell n=23,
every unit shell direction y with y^* S y < 0 satisfies

  y^*(S+G)y > 0.
```

Current stronger endpoint:

```text
H := S+G > 0 on the whole shell.
```

Default numeric certificate:

```text
H = [[+0.0358652162535, -0.0412607325106],
     [-0.0412607325106, +0.1807102584705]]

eig(H) = +0.0249362550056, +0.1916392197184
h11    = +0.0358652162535
det(H) = +0.00477876445197
```

Therefore Sylvester's criterion proves the default sector theorem once these entries are certified
with rigorous error bounds.

Budget identity on the positive-atom part of the Schur-negative sector:

```text
beta_y - required_beta_y
  = y^* H y / (smooth_mass * K_y(w_atom)).
```

Thus beta surplus is an interpretation of `H>0`, not an independent default proof obligation.

Witness:

```text
scripts/numerics/witness/prime_defect_default_t1_certificate.py
scripts/numerics/witness/prime_defect_t1_error_budget.py
scripts/numerics/witness/prime_defect_t1_stability.py
scripts/numerics/witness/prime_defect_t1_arb_components.py
scripts/numerics/witness/prime_defect_t1_winf_tail.py
```

Next work:

```text
- interval-certify A_+>0 and the post-cell Schur complement H>0;
- use Arb compact-overlap integrals for exact Toeplitz atom blocks;
- use compact-overlap integrals for smooth residual cells;
- turn the W_inf finite-cutoff/tail diagnostic into a rigorous Arb/interval enclosure;
- record exact construction dependencies for S, Q, square, smooth_mass, and atom_weight;
- keep KKT enumeration as a cross-check and explanatory geometry, not as the primary T1 endpoint.
```

Do not broaden the target until T1 is certified or fails.

### T2 - Refinement-Stable Active-Sector Theorem

Status: diagnostic only.

Goal:

```text
Extend T1's statement across raised-cosine refinements and any shell dimensions that occur in the
same late edge, either by the same H>0 endpoint or by a sector substitute if H>0 fails.
```

Known evidence:

```text
- repair atom remains 23 across tested bases;
- every sampled Schur-negative direction is directionally repaired;
- the stronger H=S+G endpoint is SPD in all tested refinements;
- positive-atom negative directions have beta surplus at least +0.068;
- K_atom<=0 directions are atom-helpful rather than beta-controlled;
- terminal coefficient is beta-dangerous, interior edge-layer coefficients usually improve beta.
```

Main weakness:

```text
3D refined shells have H SPD numerically, but not yet with rigorous matrix-entry bounds.
```

Next work after T1:

```text
- test whether H>0 is the correct refinement-stable endpoint or just a default coincidence;
- formulate a dimension-independent matrix or sector certificate;
- replace deterministic random sphere sampling with optimization/KKT enumeration in dimension >2;
- test whether the terminal anti-concentration condition has uniform constants.
```

### T3 - General Finite Storage Theorem

Status: speculative.

Goal:

```text
For every finite Sonin extension and exact chronological Euler residual cells,
construct a storage/debt-release certificate:

  S_j + Pi_j >= 0,
  Pi_{j+1} <= Pi_j,
  Pi_N = 0.
```

Known constraints:

```text
- strict telescoping PSD suffixes fail;
- total repair dominating initial debt in Loewner order fails;
- scalar-isotropic storage is too crude;
- path debt Pi_j=(-S_j)_+ survives tested zeta chain but is not constructive.
```

What must replace diagnostics:

```text
- a constructive rule for Pi_j or an equivalent sectoral repair theorem;
- a proof that each dangerous Schur-negative sector has a corresponding exact Euler repair;
- fail-closed tests against DH, smooth-only, prime-only, power-only, sign flips, and shuffles.
```

### T4 - Continuum Sonin Passage

Status: not ready.

Goal:

```text
Pass from finite raised-cosine/Sonin witnesses to the logarithmic Fourier form domain and prove the
nested Prime-Toeplitz domination theorem.
```

Do later:

```text
- density/compactness for pole-killed support spaces;
- convergence of finite Schur complements and residual cells;
- transfer of storage certificates to continuum boundary stresses.
```

Do not prioritize until T1-T3 are mathematically stable.

## Conceptual Framing

Use prediction/innovation language:

```text
Schur complement = conditional innovation energy.
S(y)<0 means the shell direction is strongly predictable from the old space.
Terminal-edge concentration is mostly innovation-like and should weaken old predictability.
Therefore Schur negativity should force terminal anti-concentration.
```

Useful external frameworks to keep in mind:

```text
- Schur complements as conditional covariance / prediction error;
- Toeplitz prediction, Schur algorithm, reflection coefficients;
- Slepian / PSWF concentration operators;
- Christoffel / leverage / boundary concentration estimates.
```

## Current Evidence Snapshot

Default active-23 data:

```text
base Schur min:        -2.545512e-01
H=S+G eigmin:          +2.493626e-02
after cell 23:         +2.494e-02 to +2.665e-02 depending on directional split
Riccati square cost:   +1.550930e-02
Schur leakage cost:    +1.484445e-03
reduced margin:        +2.516061e-02
```

Stability probe:

```text
default L2 grid 6001:  eigmin(H)=+2.493626e-02, det(H)=+4.778764e-03
fine L2 grid 12001:   eigmin(H)=+2.493625e-02, det(H)=+4.778765e-03
invariant drift:      max|deig(H)|=1.6e-08, |ddet(H)|=3.6e-10
```

Post-cell perturbation budget:

```text
direct post-cell composition error = 4.441e-16
eig(A_+) min:          +3.930222e-03
cond(A_+):             9.429e+02
uniform entry eta:     3.867e-09 keeps ||delta H|| below 0.5 eigmin(H)
```

Arb atom component:

```text
ambient max |Fourier-grid atom - Arb atom| = 6.198e-08
compressed atom operator-norm difference   = 1.676e-06
replacing the 23 atom by Arb-overlap atom shifts eigmin(H) by +9.123e-07
selected repair-cell smooth Fourier-grid discrepancy <= 2.771e-09
selected repair-cell smooth Arb radii <= 8.101e-27
selected post-cell suffix smooth Fourier-grid discrepancy <= 1.591e-09
selected post-cell suffix smooth Arb radii <= 3.899e-32
full direct Arb atom+suffix replacement:
  suffix compressed operator-norm difference = 1.035e-07
  post block operator-norm difference        = 2.287e-06
  eigmin(H) shift from atom+suffix           = +9.045e-07
```

W_inf cutoff/tail diagnostic:

```text
selected default W_inf entries differ from T=1500 finite quadrature by up to about 2.1e-06
selected T=1500 finite W_inf integrals have Arb radii <= 1.8e-24
absolute per-entry tail envelope: T=1500 -> 2.150e-09, T=2000 -> 5.269e-10
tail propagation through B:
  T=1500 compressed entry bound <= 5.930e-07
  T=5000 compressed entry bound <= 1.642e-09
full W_inf replacement endpoint:
  T=250  eigmin(H)=+2.487792096097e-02
  T=1500 eigmin(H)=+2.513451932352e-02
  T=1500 shift from default eigmin(H)=+1.983e-04
full Arb finite W_inf endpoint:
  T=5000 eigmin(H)=+2.513438064964e-02
  T=5000 tail envelope=5.953e-12 per ambient entry
partial certificate endpoint:
  T=5000 Arb W_inf finite + Arb atom(23) + Arb smooth suffix
  eigmin(H)=+2.513528421043e-02
  shift from default eigmin(H)=+1.990e-04
all-arithmetic Arb midpoint endpoint:
  T=5000 Arb W_inf finite + Arb old atoms + Arb atom(23) + Arb smooth suffix
  eigmin(H)=+2.511097945288e-02
  shift from default eigmin(H)=+1.747e-04
```

Refinement H=S+G evidence:

```text
n17/h0.100 eigmin(H)=+4.897369e-03
n21/h0.080 eigmin(H)=+4.989831e-03
n25/h0.060 eigmin(H)=+2.493626e-02
n29/h0.050 eigmin(H)=+5.153857e-02
n33/h0.045 eigmin(H)=+2.760913e-02
```

Edge-convolution mechanism:

```text
K(w) = int_0^w q(r)q(w-r)dr,
w = 2a-U.

default beta observed/required: 3.122 / 2.924
weighted K mass left of atom in U: about 0.956
terminal edge profile: nearly quadratic, but terminal asymptotics alone are not the repair.
```

Arithmetic placement:

```text
log23 relative cell position: 0.765
location threshold default:   0.722
weight threshold default:     1.138 times exact weight
```

Autodiff/KKT:

```text
active eigenvector theta=0.157511:
  surplus=+0.209661, dSurplus=-1.051144

interior stationary theta=0.450068:
  S=-0.165205, surplus=+0.108525, dSurplus=0

Schur boundary theta=0.665929:
  surplus=+0.126023
```

## Infrastructure

### Certification

Use only after a finite statement is stable.

Candidates:

```text
- Julia interval arithmetic around the reduced KKT cases;
- Arb/FLINT for certified quadrature/matrix entries;
- Lean for finite algebra after the theorem statement stops moving.
```

### Julia Autodiff

Status: useful for concept discovery, not certification.

Current setup:

```text
scripts/numerics/witness/prime_defect_export_julia_reduced.py
scripts/numerics/julia/active23_ad.jl
scripts/numerics/julia/Project.toml
```

Use interactive workflow for iteration:

```text
julia --project=scripts/numerics/julia
include("scripts/numerics/julia/active23_ad.jl")
```

### Reproducibility Rule

Every numerical claim that affects the theorem target should have:

```text
1. a script under scripts/numerics/witness/ or scripts/numerics/julia/;
2. a short interpretation in research/proof/;
3. a fail-closed note explaining what would invalidate the claim.
```
