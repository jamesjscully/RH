# Failure Modes

Ordered by severity. The top two were missing from the original list and are the
reasons programs like this waste years. See [`tracker.md`](tracker.md) §5.

## Circularity / RH-neutrality  *(top risk)*

Proving statements that are true but **equivalent to RH**, and mistaking them for
progress. The Hilbert geometry (Gram matrices, kernels, closures) is RH-neutral.

Mitigation: the **Davenport–Heilbronn test**. A statement holds for DH ⟺ it is
RH-neutral or false. Every critical-path lemma must *fail* for DH. (Harness Check 1/2.)

## DH-blindness / no Euler product

The Hardy-geometry spine uses functional-equation/analytic structure only, never the
Euler product — so it cannot distinguish ζ (RH conjectured true) from DH (RH false).

Mitigation: make the Euler product load-bearing in the forward layer; verify each
critical-path lemma fails for DH. Arithmetic locking (`a_n → −μ(n)`) is the entry point.

## Mislabeled bottleneck

Treating reverse visibility as the hard part. It is classical, exact, and `N`-uniform.

Mitigation: budget effort on the **forward/arithmetic** theorem (= RH). The reverse
oracle is a guardrail, not a proof step.

## Wrong Topology

Density in a topology that does not imply the RH-equivalent critical statement.

Mitigation: every theorem states its norm and topology.

## Conditioning Blow-Up  *(empirically re-scoped 2026-06-05)*

The original worry was `G_{N,τ}` degenerating as `τ ↓ 1/2`. Numerics say otherwise:
`κ(G_{N,τ})` is flat or slightly *decreases* as `τ ↓ 1/2`, and grows with `N`
(~`N²`-ish: N=3,5,7,9 → ~22,70,160,310 at τ=0.7). So the real conditioning cost is the
`N → ∞` limit (classical near-linear-dependence of `{n^{-s}}`), not the deformation.

Mitigation: track `κ(G_{N,τ})` vs `N` (certified via `acb_mat.eig`); the coupled-path
budget must beat the `N`-growth of `κ`, which is the actual constraint.

## ~~Height Leakage~~  *(scope-corrected)*

The raw evaluation bound `~ 1/T` is irrelevant to the **existence** contradiction,
which uses a single fixed zero at fixed height `T`. Height/`T`-uniformity matters only
for an effective zero-free *region* — a different, harder target. Do not over-engineer.

## ~~Reverse Signal Outside Forward Coordinates~~  *(non-issue here)*

In the half-plane multiplier construction the zero sits in `V_N(τ)` exactly, for every
`N`. There is no "signal outside the coordinates" to worry about. (Real only in the BD
dilation model.)

## Noncommuting Limits

`N → ∞`, `τ ↓ 1/2`, `T → ∞` may not commute.

Mitigation: state the coupling explicitly. Note `T` is fixed for the existence argument.

## Transport Loss

Transforms between avatars may destroy margins.

Mitigation: every transport carries forward, conditioning, and loss inequalities.

## Over-Abstraction / Misallocation

Lavishing structure on neutral geometry and the easy oracle.

Mitigation: theorem-first; every abstraction earns its place by a finite inequality,
and prefer unconditional intermediate results (Power Test).
