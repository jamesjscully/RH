# The two-variable lift obstruction, concretely (2026-06-06)

The single load-bearing blocker named in `geometry-of-the-square.md` §4: the characteristic-1
Frobenius correspondences `Ψ_λ` (= `Γ_λ`, graphs of scaling-by-`λ`) compose on the **curve** but do
not lift to a family of finite-self-intersection cycles on the **square** `S²`. Here is *exactly why*
— computed (`scripts/numerics/witness/lift_obstruction.py`) and tied to the corner we measured.

## The mechanism

**`(Γ_λ · Δ) = Tr(ϑ_λ) = 1/|1−λ|`** — the intersection of the Frobenius correspondence with the
diagonal is the **Atiyah–Bott/Lefschetz trace** of scaling-by-`λ`: a single fixed point `x=0` (the
archimedean place), contributing `1/|1 − dϑ| = 1/|1−λ|`. (Connes uses exactly this local term in the
trace formula.)

- **It diverges as `λ → 1`** — and `λ=1` is the identity, where `Γ_1 = Δ`. So the diagonal
  self-intersection is `Δ·Δ = lim_{λ→1} 1/|1−λ| = ∞` **[computed]**.
- **It is the corner.** In `u = log λ`, `1/|1−λ| ~ 1/|u|` near `u=0` (verified, ratio → 1) — the *raw
  geometric form* of the corner kernel `K_∞(u) ~ −1/(2|u|)` (`corner_defect.py`) and of CC20's `δ'`-jump
  at `ρ=1`. The Weil explicit formula's archimedean term `∫ f(λ)/|1−λ| d*λ` is a **principal value
  precisely because of this `λ=1` divergence**; the regularization *is* the corner singularity.

## Why `𝔽_q` escapes it (the contrast that isolates the cause)

Over `𝔽_q`, `Tr(Fr^n) = #Fix(Fr^n) = q^n + 1 − (α^n + ᾱ^n)` with `|α| = √q`. The Frobenius
eigenvalues **never equal 1**, so the discrete semigroup `{Fr^n}_{n≥0}` **never hits the identity**,
and every diagonal intersection — and `Δ·Δ = 2−2g` — is **finite** **[computed]**. The Lefschetz
machine works because the Frobenius is *discrete and fixed-point-nondegenerate*.

## The obstruction, stated

> Lifting `Ψ_λ` to the square requires intersecting with the diagonal; that intersection is
> `1/|1−λ|`, finite for `λ≠1` but **infinite at `λ=1` (the diagonal itself)**. Over `𝔽_q` the
> Frobenius is a **discrete semigroup that avoids the identity** (`Δ·Δ` finite); over `ℤ` the scaling
> is the **continuous group `ℝ₊^*` that contains `λ=1`** (`Δ·Δ = ∞`). The very continuity that makes
> the arithmetic geometry "real-number-like" — `Aut(ℝ_max) = ℝ₊^*`, a *real* Frobenius — is what puts
> the identity *inside* the group and makes the diagonal self-intersection diverge.

Gift and wound are the same feature (cf. `what-would-it-look-like.md` §5). This is not a technical gap
to be patched; it is structural — the continuous Frobenius *necessarily* contains the degenerate
identity.

## The two faces and where a resolution must act

- **Geometric:** `Δ·Δ = ∞` at `λ=1`; the correspondence family is singular at the diagonal.
- **Cohomological:** `H¹(S²)` would satisfy `Tr(Γ_λ | H¹) = Σ_ρ λ^ρ`; the diagonal class cannot
  decompose with a finite `H¹⊗H¹` Künneth piece (that piece *is* `Δ·Δ = ∞`) — equivalently, **no `H¹`
  on the square**. The 1-variable `H¹` (infinite-dimensional but tamed: Bost `θ`-invariants, CC2023
  Riemann–Roch, von Neumann dimensions) does *not* fix the 2-variable diagonal divergence.

A resolution must **regularize the `λ=1` divergence with the RH sign, equivariantly** — i.e. give
`Δ·Δ` a finite value of the Hodge-index sign without breaking the `ℝ₊^*`-equivariance. CC20's "move
`Δ` into `Σ`" gets the right sign at the single place `∞` but **breaks equivariance** ("the scaling
action does not restrict to Sonin's space") and does not see the primes. That — an equivariant,
RH-signed regularization of the `1/|1−λ|` diagonal divergence on the square — is the precise open
problem the whole missing object reduces to.
