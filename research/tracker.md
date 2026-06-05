# Strategy Tracker (Source of Truth)

This is the living tracker for the witness-constraint route to RH. It supersedes the
original framing in [`research-program.md`](../research-program.md) wherever they
disagree. The program spec holds the rationale and mathematics; this file holds the
**corrected architecture, the work breakdown, status, and the discipline that keeps
the search honest.**

Last major revision integrates the strategic review of 2026-06-05 (see
[Corrections Applied](#corrections-applied)).

---

## 0. One-paragraph diagnosis (read this first)

The original architecture **mislocated the difficulty of RH**. It named *reverse
visibility* (Theorem B) the "central bottleneck" and treated *forward convergence
along the coupled path* (Theorem C) as a coupling/bookkeeping problem. The truth is
the exact opposite:

- **Reverse visibility is the classical, trivial, already-solved direction.** For a
  hypothetical zero `ρ = β + iT` and any fixed `τ ∈ (1/2, β)`, the multiplier
  `φ_τ(ρ) = 0` makes *every* witness `f = φ_τ D_N` vanish at `ρ`, so the evaluation
  functional `k_ρ` annihilates `V_N(τ)` at **every** level `N`, giving
  `dist(u, V_N(τ)) ≥ |u(ρ)| / ‖k_ρ^{(τ)}‖ > 0` uniformly in `N`. No resolution
  condition, no height uniformity, no projected packets required.
- **Forward convergence is literally RH.** By Ge (2019) / Wei–Wu (2022),
  `dist_{H²(Ω_τ)}(u, closure V(τ)) = 0 ⟺ ζ is zero-free in Ω_τ`. So "unconditional
  forward → 0 as `τ ↓ 1/2`" **is** "ζ zero-free in `Re s > 1/2`" = RH. In the disk
  avatar this is Báez-Duarte's `d_N → 0 ⟺ RH`, and **no unconditional upper bound on
  `d_N` tending to 0 is known** — such a bound *is* a proof of RH.

Consequence: the witness/Hilbert-geometry machinery is **RH-neutral reformulation**.
The only place non-circular information can enter is **arithmetic (the Euler
product)**, which the original plan demoted to a secondary track. The program must be
re-architected around that fact.

---

## 1. Corrected architecture

| Layer | Original role | Corrected role |
|---|---|---|
| **Theorem A — Finite Compression** | finite Gram linear algebra | KEEP. Necessary bookkeeping. RH-neutral but real; gives the coordinates everything else lives in. |
| **Reverse Visibility** (was "Theorem B, the central bottleneck") | central bottleneck / proof ingredient | DEMOTE to **Barrier Oracle**: a cheap *soundness filter*, not a proof step. Classical, `N`-uniform, easy. Its job is backpressure. |
| **Forward / Arithmetic Theorem** (was hidden inside "Theorem C, coupled path") | bookkeeping / coupling | PROMOTE to **the bottleneck**. This is RH. It must be powered by the **Euler product** (Möbius coefficients), or it is provably blind (see §3). 95% of real effort lives here. |
| **Arithmetic locking** (was secondary track A.7) | secondary | PROMOTE to **primary**. The only non-RH-neutral content. Optimal forward coefficients are `−μ(n)` (Báez-Duarte); the achievable rate is governed by prime/zero sums. |
| **Explicit formula / positivity** (was secondary backend §10.3) | secondary backend | PROMOTE to **primary backpressure oracle**. The Weil explicit formula is the exact identity that couples *zeros* (what you constrain) and *primes* (what you must inject); finite truncations give cheap necessary inequalities. |
| **Coupled path** (was "Theorem C") | separate theorem to engineer | RECOGNIZE as RH itself, not a coupling lemma. Do not budget it as bookkeeping. |

The reframed contradiction is honest: there is no "signal-to-slack gap" to win,
because the reverse modulus is a lower bound on the *same quantity* the forward side
must drive to zero. The work is not to make two independent estimates cross; it is to
**prove the forward (arithmetic) convergence unconditionally**, using the Euler
product, with the Barrier Oracle and explicit-formula checks preventing circular or
false detours.

---

## 2. The Refutation Harness (the principled "backpressure")

Replaces ad-hoc reverse-visibility lower bounds. Every candidate forward lemma passes
through these checks **before** we invest in proving it. All four are *evaluations*,
not proofs — orders of magnitude cheaper than building Theorem B.

The waste we are guarding against has two signatures, and one mechanical test catches
both: **a statement is on the critical path to RH ⟺ it fails for Davenport–Heilbronn.**
Holds-for-DH ⟺ RH-neutral (or false).

**Check 1 — Barrier battery (catches falsity + blindness).** Evaluate the lemma's
conclusion on a graded lattice of test objects. A "pass" on an object that violates
the conclusion refutes (or exposes the hidden hypothesis of) the lemma.

| Test object | Func. eq. | Anal. cont. | Euler prod. | RH status | A pass here means… |
|---|:--:|:--:|:--:|:--:|---|
| **Davenport–Heilbronn** | ✓ | ✓ | ✗ | **false** (zeros, Re>1) | lemma is **blind to the Euler product** → off critical path |
| Dirichlet `L(s,χ)` | ✓ | ✓ | ✓ | true (GRH) | uses Euler product, maybe not ζ-specific structure |
| **planted-zero "fake ζ"** | partial | ✓ | broken | false by construction | does forward machinery **correctly fail to converge**? |
| truncated Euler product `∏_{p≤P}` | ✗ | ✓ | finite | — | isolates the arithmetic depth the lemma needs |
| degree-2 Selberg-class member | ✓ | ✓ | ✓ | open | tests reliance on degree-1 specialness |

**Check 2 — RH-content tag (catches circularity).** Does the statement, if true,
constrain `Θ = sup{Re ρ : ζ(ρ)=0}`? If not, it is RH-neutral reformulation and cannot
be on the critical path. (Mechanically: it holds for DH.)

**Check 3 — In-coordinate necessary conditions (catches wrong constructions).**
Derived *from* the forward problem, checkable on the same Gram data:
- **Möbius locking:** do the extremal coefficients asymptotically approach `−μ(n)`?
  If not, the construction is provably suboptimal.
- **Burnol consistency:** forward distance cannot decay faster than
  `d_N² ≳ (Σ_ρ m(ρ)²/|ρ|² + o(1)) / log N` (unconditional lower bound).
- **Conditioning sanity:** `κ(G_{N,τ})` must not blow up faster than the claimed
  forward gain.

**Check 4 — Finite explicit-formula consistency.** Does the claimed inequality respect
a truncated Weil-functional positivity check? The explicit formula is an *exact
identity*, so this is non-circular by construction, and DH-discriminating (DH's prime
side is not `Λ(n)`).

Operationally this harness is what the automation `reviewer` agent should run on each
proposed lemma. See [open work item H1](#workstream-h-refutation-harness).

---

## 3. Why the Euler product must be load-bearing (the DH wall)

The entire original proof spine — Hardy module, half-plane `H²`, evaluation/jet
kernels, Gram matrices, transports — uses functional-equation and analytic structure
**only**. The Euler product enters nowhere in it. Davenport–Heilbronn has a ζ-type
functional equation, full analytic continuation, and Hardy-space structure, but **no
Euler product** and **provably infinitely many off-line zeros, including `Re s > 1`**
(Davenport–Heilbronn 1936; Bombieri–Ghosh 2011; Bian–Hejhal 2007). Therefore any
argument whose spine does not use the Euler product would "prove" RH for DH — which is
false. **The current spine, as written, cannot work.** Every lemma on the critical
path must fail Check 1 for DH; if it passes, it is not on the path.

---

## 4. Workstreams & milestones

Status keys: `todo` · `active` · `blocked` · `done` · `dropped`.
Each milestone is written to be **falsifiable**.

### Workstream N — Numerics infrastructure  *(done; foundation)*
- [x] **N1** `done` — Backend chosen: **python-flint (FLINT 3 / Arb)**, certified ball
      arithmetic. Capability map in `scripts/numerics/FLINT_CAPABILITIES.md`.
- [x] **N2** `done` — Test-object battery (`scripts/numerics/witness/objects.py`):
      ζ, Davenport–Heilbronn (Hurwitz-ζ combo; functional equation verified to ~1e-57),
      planted-zero fake-ζ, truncated Euler product. Canonical DH off-line zero
      `ρ≈0.808517+85.699348i` located.
- [x] **N3** `done` — Hardy-module engine (`witness/hardy.py`): sampled Gram/target/
      distance, closed-form `‖u‖²`, barrier bound. Validated.
- [~] **N4** `partial` — Certified upgrades **demonstrated**: `hardy.certify_gram_entry`
      gives rigorous `G[n,m]` enclosures over `|t|≤T` via `acb.integral` (e.g.
      `G[1,1]=0.63936858186645976 ± 9e-18` over [−30,30]); `κ` certified via
      `acb_mat.eig`. **Remaining:** certify the Gram tail `Err_{N,τ}=∫_{|t|>T}` (needs
      an explicit `|ζ(τ+it)|` bound — `acb_dirichlet_zeta_bound`, via C API). The
      float-vs-certified gap (~0.022 for `G[1,1]`, T=30) *is* `Err`, made concrete.

### Workstream H — Refutation Harness  *(do first; it pays for itself immediately)*
- [x] **H1** `done` — Test-object battery implemented (see N2).
- [x] **H2** `done` — Four checks encoded in `witness/harness.py`; runs end to end.
      (Remaining: wire to the automation `reviewer` agent — automation polish.)
- [x] **H3** `done` — DH-blindness demonstrated numerically: at fixed `τ=0.7`, ζ's
      forward distance marches toward 0 (zero-free in Ω_τ) while DH's flattens at a
      floor (off-line zero β=0.8085); the barrier construction emits *identical* output
      for DH's real zero and a hypothetical ζ zero. The spine cannot tell them apart.

### Workstream A — Finite Compression (Theorem A; necessary bookkeeping)
- [x] **A1** `done` — Convention fixed: `⟨f,g⟩=(1/2π)∫f(τ+it)conj g dt`; closed-form
      `‖u‖²=(1/4)((τ−1)²/τ³+1/τ)`, verified `u∈H²(Ω_τ)` (and `ζ∉H²`; `(s−1)/s²` buys
      membership). In `witness/hardy.py`.
- [~] **A2** `partial` — Structural Gram formula derived & implemented:
      `G[n,m]=(nm)^{−τ}J(log(m/n))`, `J(x)=(1/2π)∫|φ_τ(τ+it)|²e^{itx}dt`; target
      `b[n]=n^{−τ}B(log n)`. Computed via sampling. **Certified entries + tail error
      `Err_{N,τ}` remain (N4).**
- [x] **A3** `done` — `κ(G_{N,τ})` scanned: flat/decreasing as `τ↓1/2`, grows ~`N²`.
      Certified `κ(G_4,0.7)=43.67` via `acb_mat.eig`. (See log 2026-06-05; risk re-scoped.)

### Workstream F — Forward / Arithmetic Theorem (THE bottleneck = RH)
Scoping note: [`forward-theorem.md`](forward-theorem.md).
- [x] **F1** `done` — Stated as the Ge / Wei–Wu bounded-norm Möbius-approximant problem
      `φ_τ M_N`, `M_N=Σ_{n≤N}μ(n)n^{−s}`, down to `τ=1/2`.
- [x] **F2** `done` — Euler product enters in two confirmed places: (i) coefficients
      lock onto `μ(n)` (Check 3), (ii) `‖φ_τ M_N‖` bounded ⇔ Littlewood's `M_N→1/ζ`
      ⇔ zero-free. Both fail for DH.
- [x] **F3** `done` — Stall point characterized: unconditional & modest above the
      1-line (power-test PASS); no unconditional rate below. Next target stated:
      move an unconditional frontier to some fixed `τ₀∈(1/2,1)`.
- [~] **F4** `partial` — `forward_bound.py` charts `‖φ_τ M_N‖²=μᵀGμ`.
      **Proved (unconditional, τ>1):** `‖φ_τ M_N‖² ≤ ζ(τ)²‖φ_τ‖²` uniformly in `N`
      ⇒ (Wei–Wu) reproves `ζ` zero-free in `Re s>1` in bounded-norm form (fails for DH).
      Numerics: bounded/convergent for `τ>1`; oscillates with growing amplitude as
      `τ↓½` for `τ<1`; crude bound diverges at `τ→1`. **Open (the real crux):** bound
      the off-diagonal Mertens sum for a fixed `τ₀<1` using `μ`-cancellation. See
      [`forward-theorem.md`](forward-theorem.md) §F4.

### Workstream P — Power Test (go/no-go before aiming at RH)
- [x] **P1** `done` — Target chosen: Littlewood `M_N→1/ζ` above the 1-line / the
      classical zero-free half-plane `Re s>1`.
- [x] **P2** `done` — PASS (`witness/power_test.py`): `M_N→1/ζ` unconditionally for
      `Re s>1` (Euler-product-driven, mu-cancellation rate); erratic inside the strip;
      `dist(u,V_N(1.1))→0` cleanly vs slow at `τ=0.7`. The machinery reproves the known
      zero-free half-plane unconditionally; the gap to RH is the extension below `τ=1`.

### Workstream B — Barrier Oracle (formerly reverse visibility; now a guardrail)
- [x] **B1** `done` — Exact `N`-uniform bound implemented (`hardy.barrier_bound`):
      `dist(u,V_N(τ)) ≥ |u(ρ)|/‖k_ρ^{(τ)}‖ = |u(ρ)|√(2(β−τ))`, with verified constant
      `‖k_ρ^{(τ)}‖² = 1/(2(β−τ))` (T-independent), `|u(ρ)| ∼ 1/T`. Trivial and
      `N`-uniform — the point.
- [ ] **B2** `dropped` — ~~Projected reverse packets / resolution function `R_τ(N)` /
      two-scale `δ_T, ν_{N,τ}` machinery~~. The evaluation obstruction is exact and
      `N`-uniform, so the resolution concern is a non-issue for the multiplier
      construction (see §6). Keep only if a *quantitative* role for the oracle emerges.

### Workstream E — Explicit-Formula Conservation Law (primary oracle)
- [x] **E1** `done` — `witness/explicit_formula.py`: prime side `−Z′/Z=Σc(n)n^{−s}`
      via the exact divisor recurrence; for ζ, `c(n)=Λ(n)` (verified). The
      Euler-product positivity signature (nonneg + prime-power support).
- [x] **E2** `done` — Discriminates ζ from DH: DH's prime side has negative coeffs
      (`c(3)=−0.31, c(9)=−2.29`) and support off prime powers (`c(6)=+1.94`). Check 4
      passes (FAILS for DH).
- [ ] **E3** `todo` — Deeper: assemble the full finite Weil functional (zero sum +
      archimedean term via `acb.digamma`) and exhibit a test function where it is `≥0`
      for ζ but `<0` for DH (using DH's off-line zeros). Promotes Check 4 from
      prime-side-signature to genuine positivity.

### Workstream L — Lean formalization (follows the math, does not lead it)
- [x] **L1** `done` — Contradiction theorem de-tautologized: `RH/Witness/`
      `DistanceSequence.lean` proves `forward_reverse_incompatible` (a ℚ-sequence can't
      both →0 and sit above a positive floor) from order facts; `ContradictionMechanism`
      and `QuantitativeInvariants` now carry real predicates, exercised by `ToyModels`
      (`floored_cannot_converge`). No assumed conclusion.
- [x] **L2** `done` — `:= True` stubs removed (A/B/C); B is a real `barrier_oracle`
      lemma, A/C are documented targets (no fake theorem). CI guard
      `scripts/automation/check-stubs.sh` (wired into `check.sh`) flags `:= True`,
      `by trivial` in the spine, and `sorry`/`axiom`. Also fixed lakefile
      `@[default_target]` so the documented `lake build` is no longer a no-op.
- [x] **L3** `done` — Mathlib added (v4.30.0). `RH/Experiments/ToyGram.lean` proves the
      **rank-1 finite-compression identity** (the genuine `N=1` Theorem A) in a real
      inner-product space: `IsLeast (range fun a => ‖u−a•v‖²) (‖u‖²−⟪u,v⟫²/⟪v,v⟫)` —
      i.e. the min over the line equals the one-term Gram expression. Fully proved
      (`toy_finite_compression`, `norm_sub_smul_sq`). Build now needs `lake exe cache
      get`. Next: generalize to `N×N` (`Matrix`/`G⁻¹`).

---

## 5. Risk register (corrected)

| Risk | Status of original mitigation | Corrected stance |
|---|---|---|
| **Circularity / RH-neutrality** (NEW, top risk) | not tracked | The dominant failure mode is proving true-but-RH-equivalent statements. Check 2 / DH test is the mechanical detector. |
| **DH-blindness / no Euler product** (NEW) | not tracked | Spine as written is DH-blind. Every critical-path lemma must fail for DH (Check 1). |
| **Mislabeled bottleneck** | "Theorem B is the central bottleneck" | False. Reverse is trivial; the forward/arithmetic theorem is the bottleneck. |
| Reverse signal outside forward coordinates | "Theorem B requires same-coordinate visibility" | Non-issue for the multiplier construction: the zero sits in every `V_N(τ)` exactly. |
| Height leakage / `T → ∞` | "track height dependence" | Irrelevant to the *existence* contradiction (single fixed zero at fixed `T`). Only matters for an effective zero-free *region* (a different target). |
| Conditioning blow-up | "make it part of Theorem A" | Keep — it is a real Check-3 input. |
| Noncommuting limits | "couple `N, τ, T` explicitly" | Keep, but note `T` is fixed for the existence argument. |
| Wrong topology | "state norm/topology" | Keep — correct and important. |

---

## 6. Settled technical facts (do not re-litigate)

- **Reverse is `N`-uniform and exact.** `φ_τ(ρ)=0 ⟹ f(ρ)=0` for all `f ∈ V_N(τ)`, all
  `N`. So `dist(u,V_N(τ)) ≥ |u(ρ)|/‖k_ρ^{(τ)}‖`. The `§7` "two scales of reverse
  visibility" / `R_τ(N)` resolution apparatus addresses a difficulty this construction
  does not have (it is real only in the BD *dilation* setup, where witnesses do not
  carry the zero as a common multiplier — a conflation of avatars).
- **Forward = RH.** `dist(u, closure V(τ)) = 0 ⟺ ζ` zero-free in `Ω_τ` (Ge 2019;
  Wei–Wu 2022). `d_N → 0 ⟺ RH` (Báez-Duarte 2003). No unconditional rate known.
- **Deformation frontier = `Θ`.** Pushing provable density to `τ = 1/2` is proving
  `Θ = 1/2` = RH; the deformation gets stuck at `Θ`. Even one fixed `τ₀ ∈ (1/2,1)` with
  an unconditional density proof would beat all known unconditional zero-free regions.
- **Arithmetic enters through coefficients.** Optimal forward coefficients `→ −μ(n)`
  (Báez-Duarte); the Hilbert geometry is RH-neutral.
- **Formula corrections.** `h_k(z) = (1/k)·(1/(1−z))·log((1+z+⋯+z^{k−1})/k)` — the
  leading `1/k` was missing. The half-plane disk criterion (GKNS Thm 4.8) is
  **one-directional** (`1 ∈ closure ⟹ zero-free`); the iff is the `τ=1/2` Ge form.

---

## 7. Literature anchors

- **Báez-Duarte (2003)**, *Rend. Mat. Acc. Lincei* — discrete/strong NB criterion;
  `RH ⟺ d_N → 0`. Optimal coefficients `~ −μ(n) n^{−ε}`.
- **Burnol (2002)**, *Adv. Math.* 170 — unconditional lower bound
  `d_N² ≥ (Σ_ρ m(ρ)²/|ρ|² + o(1))/log N`.
- **Báez-Duarte–Balazard–Landreau–Saias (2000)**, *Adv. Math.* 149 — conjecture
  `d_N² ∼ (2+γ−log 4π)/log N` (implies RH + simple zeros).
- **Balazard–de Roton (2008/2010)**, arXiv:0812.1689 — best conditional upper bound
  `d_N² ≪ (log log N)^{5/2+o(1)} (log N)^{−1/2}`.
- **Ge (2019)**, Acta Math. Sinica / Sci. China Math. — operator criterion
  `RH ⟺ Ran(M_φ)` dense, `φ = ((s−1)/s²)ζ`.
- **Wei–Wu (2022)**, *Expo. Math.* — closure-of-range characterization; zero-free in
  `Re s > τ ⟺` closed range; Dirichlet-polynomial (bounded-norm) form, Thm 1.5.
- **Ghosh–Kremnizer–Noor–Santos (2024)**, *Adv. Math.* 455 (+ Noor 2019) — disk `H²`
  criterion via `h_k`; iff at the disk, one-way in the half-plane.
- **Davenport–Heilbronn (1936)**; **Bombieri–Ghosh (2011)**, *Russian Math. Surveys*
  66(2); **Bian–Hejhal (2007)**, *Math. Comp.* 76 — DH function: func. eq., no Euler
  product, off-line zeros incl. `Re s > 1`. The barrier object.
- **Weil explicit formula / Weil positivity** — the conservation law coupling zeros
  and primes; finite positivity = backpressure oracle (Workstream E).

---

## Corrections Applied

Log of changes made to the rest of the repo to match this tracker (2026-06-05):

- `research-program.md` — rewritten to invert the architecture (forward/arithmetic is
  the bottleneck; reverse is a barrier oracle); added barrier methodology, explicit-
  formula oracle, power test; promoted arithmetic locking; fixed `h_k` and the
  one-directional half-plane criterion; corrected the `§13.1` misdiagnosis.
- `research/theorem-stubs.md` — re-labeled reverse as the Barrier Oracle; added the
  Forward/Arithmetic theorem and the Power Test; corrected `§13.1`.
- `research/agenda.md` — re-phased around the corrected architecture (Harness + Power
  Test early; forward/Euler-product injection central; reverse demoted).
- `research/failure-modes.md` — added Circularity/RH-neutrality and DH-blindness;
  corrected the reverse-coordinate and height-leakage entries.
- `research/questions.md` — added the live questions (Euler-product injection point,
  power-test target, DH discrimination); corrected the reverse-visibility section.
- `research/bibliography.md` — fixed attributions (Ge for the operator criterion);
  added Burnol, Balazard–de Roton, GKNS 2024, Davenport–Heilbronn, explicit formula.
- `README.md` — updated the Immediate Goal to the corrected plan; pointer to this file.
