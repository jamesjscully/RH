# Theorem Stubs

Architecture follows [`tracker.md`](tracker.md). The headline correction: **reverse
visibility is the easy/classical direction (now the "Barrier Oracle"); the
forward/arithmetic theorem is the bottleneck and is RH.**

Status labels: `informal` · `lean-stated` · `toy-proved` · `partial` · `blocked` ·
`false` · `obsolete`. A new tag, **`shadow`**, marks a statement that holds for the
Davenport–Heilbronn function and is therefore RH-neutral (off the critical path).

## Abstract Contradiction Mechanism

Status: `toy-proved` — **real theorem now** (de-tautologized 2026-06-05)

Lean: `RH/Strategy/ContradictionMechanism.lean`, `RH/Witness/DistanceSequence.lean`

Statement: modelling the forward distances as a nonnegative `ℚ`-sequence,
`ForwardConvergence` (`TendstoZero`) and `ReverseObstruction` (`UniformPositiveFloor`)
are incompatible — `forward_reverse_incompatible` derives `False` from order facts
alone. No `incompatible` hypothesis; nothing assumes the conclusion. Exercised by
`RH/Experiments/ToyModels.lean` (`floored_cannot_converge`, a non-vacuous corollary).

## Theorem A: Finite Compression With Explicit Losses

Status: `toy-proved` (rank-1 case) / `informal` (general analytic objects)

Lean: `RH/Strategy/TheoremA_FiniteCompression.lean` (documented target, no stub);
**`RH/Experiments/ToyGram.lean` proves the `N=1` case** in a real inner-product space
(`toy_finite_compression`: the line-projection distance equals the one-term Gram
expression). Numeric general case in `scripts/numerics/witness/hardy.py`.

Statement:
\[
\operatorname{dist}(u,V_N(\tau))^2 = \|u\|^2 - b_{N,\tau}^*G_{N,\tau}^{-1}b_{N,\tau} + \operatorname{Err}_{N,\tau}
\]
with explicit Gram entries, target vector, error, and conditioning estimates.

Role: necessary bookkeeping; RH-neutral. Verify `u ∈ H²(Ω_τ)` uniformly as `τ ↓ 1/2`
(note `ζ ∉ H²` of a half-plane; `(s−1)/s²` buys membership). Tracker A1–A3.

## Barrier Oracle (was "Theorem B: Finite Reverse Visibility")

Status: `toy-proved` (abstract) / **classical / easy** — not a bottleneck.
Lean `RH/Strategy/TheoremB_ReverseVisibility.lean`: `barrier_oracle` shows a positive
`N`-uniform floor is a `ReverseObstruction` (the trivial direction). Numeric bound in
`hardy.barrier_bound`.

Statement: for a zero `ρ = β + iT` and fixed `τ ∈ (1/2, β)`,
\[
\operatorname{dist}(u,V_N(\tau)) \ge \frac{|u(\rho)|}{\|k_\rho^{(\tau)}\|} = |u(\rho)|\sqrt{2(\beta-\tau)} \sim \frac{1}{T}\sqrt{2(\beta-\tau)} > 0 \quad\text{for all }N.
\]

Correction: this is exact and `N`-uniform because `φ_τ(ρ)=0` puts the zero in every
`V_N(τ)`. The earlier "projected packets / resolution `R_τ(N)` / two-scale
`δ_T, ν_{N,τ}`" program is **dropped** for the multiplier avatar (it solves a non-issue;
see tracker §6). The oracle's job is backpressure (harness Check 1/3), not proof.

## Theorem F: Forward / Arithmetic Theorem  *(THE bottleneck = RH)*

Status: `blocked` (this is RH)

Statement: construct, **unconditionally and using the Euler product**, bounded-norm
Möbius approximants with `dist(u, V_N(τ)) → 0` along `τ ↓ 1/2`. By Ge (2019) /
Wei–Wu (2022) this equals "ζ zero-free in `Re s > 1/2`" = RH.

Current issue: no unconditional rate for `d_N → 0` is known; this *is* RH. Real work =
identify the load-bearing Euler-product mechanism (must fail for DH). Tracker F1–F3.

## Power Test (go/no-go, not RH)

Status: `todo`

Statement: the witness machinery unconditionally reproves a **known** result — the
classical zero-free region, a zero-density estimate `N(σ,T)`, or `M_N → 1/ζ` for
`Re s > 1`. If it cannot, the program has no demonstrated proving power. Tracker P1–P2.

## ~~Theorem C: Coupled Path~~

Status: `obsolete` — folded into Theorem F. The coupling is not a separate theorem; it
*is* the forward convergence statement, i.e. RH. Do not budget it as bookkeeping.
