# Constructing 𝔽₁ — the finite ground at infinity (exhaustive program, 2026-06-06)

The geometric no-go (`research/the-complete-account.md` §6b) proved RH needs a **real geometric origin —
a projective surface over a finite ground — which `Spec ℤ` lacks at `∞`**, and that no coherence structure
fakes it. This program **exhausts the attempt to construct that finite ground `𝔽₁`.** Endpoint: either a
candidate ground supplies the arithmetic scale (⟹ RH), or **every** candidate is shown scale-free with a
precise reason (the path is closed, and we know exactly why `𝔽₁` cannot carry the scale).

## The object `X` (universal property — definition first)

> `X` = the **projective arithmetic surface over a finite ground `𝔽₁`** whose function field is `ℚ`, whose
> zeta is `ζ_ℚ`, and whose **Hodge-index signature is `(d,0)`** (positive-definite). Then `(X exists) ⟹ RH`
> is a one-line Hodge-index argument (Step B = the `(d,0)` signature, *created* by projectivity-over-a-field,
> not imported). **All hardness is moved into constructing `𝔽₁`.**

## The single constructive question — the *scaled conjugation*

The archimedean place HAS the reality (complex conjugation = the order-2 Frobenius `Gal(ℂ/ℝ)=ℤ/2` = `F†=F̄`)
but LACKS an arithmetic **scale `q`** (over `𝔽_q`, `Frob=x^q` carries the size `q`; at `∞`, conjugation is
order 2, no `q`). So:

> **`𝔽₁` ⟺ a *scaled conjugation*:** an archimedean Frobenius that is BOTH the reality (`F†=F̄`, which `∞`
> has) AND carries an arithmetic scale `q` (which `∞` lacks), turning `ℤ/2`-conjugation into a
> `Ẑ`-Frobenius-with-a-size. **Decisive test for every candidate ground: does it supply the SCALE `q`?**

## Discipline (every candidate)
1. **Anchor:** over `𝔽_q` recover `Frob=x^q` (reality + scale `q`), and `|α|=√q`, WITHOUT assuming the zeros.
2. **Scale test:** does the candidate give the archimedean conjugation an arithmetic `q`, or is it scale-free
   (the universal failure — reality without scale)?
3. **Falsify:** fails for DH (no Euler product ⟹ no `𝔽₁`). `[BUILT]/[computed]/[circular]/[aspirational]`.

## The candidate grounds (to be exhausted)
- **(S) Sphere spectrum `𝕊`** — homotopy-finite (Serre: `π_n(𝕊)` finite, `n>0`); Connes–Consani's `𝔽₁`-base.
  Does the homotopical finiteness give conjugation a scale (a `K`-theoretic / homotopy `q`)?
- **(T) Tropical / Boolean / max-plus `𝔽₁`** (Connes–Consani characteristic 1; the scaling site). Does the
  `ℝ₊ˣ`-scaling supply a *discrete arithmetic* `q`, or only the continuum (R3: free self-dual ½)?
- **(Λ) Borger Λ-ring / Witt `𝔽₁`** — finite-prime-indexed (QD: archimedean-blind). Re-test for the scale.
- **(M) Monoid / Deitmar–Kato–Soulé `𝔽₁`** — `Spec ℤ` as a monoid scheme. Does the monoid structure carry a
  scale at `∞`?
- **(P) Period / Tate-twist** — `ℝ(1)=2πi·ℝ`, conjugation-with-weight, scale `2π` (a period). Quantize it?
- **(G) Global / product-formula** — the scale at `∞` borrowed from the primes via `∏_v|x|_v=1`. (Caveat: the
  audit's Euler structure gave the edge not the line — must add something.)
- **(N) New object** — if all fail, the blueprint: what minimal new structure carries reality + scale.

## Exhaustion criterion
`𝔽₁` CONSTRUCTED (a ground supplies the scale, anchored, DH-failing ⟹ RH) — or **PATH CLOSED**: every
candidate scale-free, each with its precise reason, and the residual blueprint for what would be required.
