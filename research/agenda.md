# Research Agenda

Re-phased around the corrected architecture ([`tracker.md`](tracker.md)). Headline:
the **forward/arithmetic theorem is the bottleneck (= RH)**; reverse visibility is a
cheap oracle; the **refutation harness** and **power test** come first.

## Current Priority

Stand up the refutation harness and run the power test before elaborating the spine.

## Phase 0: Infrastructure  *(done)*

- [x] Lean 4 Lake project; abstract witness skeleton; logs; `lake build RH` passes.
- [x] WhippleScript + Loft automation; `scripts/automation/check.sh` passes.
- [ ] Decide whether/when to add Mathlib (needed by Phase A real formalization).
- [ ] Set up a minimal numerics stack (env has Python only; no scipy/mpmath).

## Phase H: Refutation Harness  *(do first)*

- [ ] Test-object battery: `ζ`, Davenport–Heilbronn, a planted-zero "fake ζ", a
      truncated Euler product. (tracker H1)
- [ ] Encode the four checks (DH/barrier, RH-content tag, in-coordinate necessary
      conditions, finite explicit-formula consistency); wire to the `reviewer` agent.
      (tracker H2)
- [ ] Demonstrate DH-blindness: run the spine's evaluation obstruction against DH and
      show it cannot distinguish DH from ζ. First real result. (tracker H3)

## Phase P: Power Test  *(go/no-go)*

- [ ] Choose a known unconditional target (classical zero-free region / `N(σ,T)` /
      `M_N → 1/ζ` for `Re s > 1`). (tracker P1)
- [ ] Attempt the unconditional reproof in the witness language, Euler product
      load-bearing. If it fails for even the classical zero-free region, reassess.
      (tracker P2)

## Phase A: Finite Hardy-Module Package  *(necessary bookkeeping)*

- [ ] Fix the `H²(Ω_τ)` convention; verify `u ∈ H²(Ω_τ)` uniformly as `τ ↓ 1/2`.
- [ ] Closed-form Gram entries `G_{N,τ}`, target vector `b_{N,τ}`, tail error.
- [ ] Condition-number profile `κ(G_{N,τ})` as `τ ↓ 1/2` (Check-3 input).

## Phase F: Forward / Arithmetic Theorem  *(the bottleneck = RH)*

- [ ] State the forward target as the Ge / Wei–Wu bounded-norm Möbius approximant
      problem down to `τ = 1/2`.
- [ ] Locate where the Euler product must enter to make forward convergence
      unconditional (must fail for DH).
- [ ] Study the stall point of the Balazard–de Roton conditional upper bound; aim to
      move an unconditional frontier, not re-derive the equivalence.

## Phase B: Barrier Oracle  *(cheap guardrail)*

- [ ] Write the exact `N`-uniform evaluation bound with explicit constants. (tracker B1)
- [ ] ~~Projected reverse packets / resolution `R_τ(N)` / two-scale machinery~~
      (dropped for the multiplier avatar; tracker B2).

## Phase E: Explicit-Formula Conservation Law  *(primary oracle)*

- [ ] Set up the Weil explicit formula coupling zeros and primes; define the finite
      truncated positivity check (harness Check 4).
- [ ] Verify it discriminates ζ from DH at finite truncation.

## Phase L: Lean formalization  *(follows the math)*

- [x] Contradiction theorem de-tautologized (`forward_reverse_incompatible`); real
      predicates over a ℚ distance sequence; toy `floored_cannot_converge`.
- [x] `:= True` stubs removed; CI guard `check-stubs.sh` wired into `check.sh`;
      lakefile `@[default_target]` fixed (plain `lake build` now works).
- [x] Toy Theorem A formalized: `RH/Experiments/ToyGram.lean` (rank-1 finite-
      compression identity, real inner-product space; Mathlib v4.30.0 added).
