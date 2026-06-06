# The two-variable lift — a precise research framing (2026-06-06)

Target (set by the convergence of this whole search): construct the missing object by achieving the
**two-variable lift** — `H¹(S²)` with Serre duality and an RH-signed intersection positivity on the
square `S² = \overline{Spec ℤ} ×_𝕊 \overline{Spec ℤ}` — fusing **Segal Γ-rings / 𝕊** (algebra),
**condensed / analytic geometry** (archimedean metric & duality), and **spectral / scattering theory**
(the self-adjoint generator). This file frames the problem precisely and assigns each framework a job.
Discipline retained: every candidate must pass the kill-tests (fail for Davenport–Heilbronn and
Epstein) and be certified on real ζ. Tags **[THM]** proven, **[have]** we computed it, **[bet]** the
working hypothesis.

---

## 1. The reduction that sharpens everything: the lift IS the metrized canonical

The hardest piece of the lift is the diagonal self-intersection `Δ·Δ`. Standard surface geometry:

> `Δ·Δ = c₁(N_Δ) = c₁(T_C) = −deg(Ω¹_C)`  — the diagonal's self-intersection is **minus the degree
> of the canonical** `Ω¹` of the curve. **[THM]**

Over `\overline{Spec ℤ}` the canonical **class** `K = Ω¹` and **Serre duality** are *already
constructed* (Connes–Consani 2023, over 𝕊: `K=−2{2}`, `H⁰(K−D) ≅ Hom(H¹(D),H¹(K))`) **[THM]**. The
finite-place degree of `Ω¹` for ℚ is trivial (`disc(ℚ)=1`). So:

> **`Δ·Δ` is determined entirely by the *archimedean metric* on the canonical `Ω¹` at `∞`**, and that
> metric is exactly where the divergence lives (`Δ·Δ = −\widehat{deg}(Ω¹) = ∞`, the corner `~ −log ε`,
> `K_∞(u) ~ −1/(2|u|)`). **[have]**

**This is the sharpening.** The lift is *not* "build `H¹(S²)` from scratch." The class and the duality
exist; **the missing object is a single archimedean structure: a metric / Green form `h_∞` on the
canonical `Ω¹` of `\overline{Spec ℤ}` whose induced (regularized) self-intersection is finite and
RH-signed, and whose Hodge Laplacian is the self-adjoint generator.** Everything else (Künneth ⟹
`H¹(S²) = H⁰⊗H¹ ⊕ H¹⊗H⁰`, the Lefschetz/explicit formula) follows once the product `S²` is formed and
`Ω¹` is metrized. The problem has gone from a surface to **a metric on a line bundle on a curve.**

## 2. The structure of `h_∞`: conformal, because the corner is scale-invariant

We computed the corner kernel is `−1/(2|u|)` — **scale-invariant (conformal)**. That dictates the
shape of `h_∞`:

- the archimedean place `∞` is a **conformal boundary at infinity**; the scaling group `ℝ₊^* =
  Aut(ℝ_max)` acts as its **conformal/dilation symmetry**;
- the metric `h_∞` on `Ω¹` is a **conformal metric**, and the natural Laplacian is a **conformally-
  covariant operator** (the conformal Laplacian / GJMS / Paneitz family), not the flat one;
- this is exactly the geometry of the **boundary of a hyperbolic object** — matching the
  negative-curvature lead (`curvature-spectral-lead.md`): the missing object is a (singular,
  manifolds-excluded) **hyperbolic arithmetic object**, and `∞` is its conformal boundary. **[bet]**

## 3. The spectral content: the zeros as scattering resonances

On a conformal boundary with a hyperbolic bulk, the natural self-adjoint operator is the **scattering
operator** (the boundary-to-boundary map of the bulk Laplacian; Patterson–Sullivan / Lax–Phillips /
the Selberg scattering matrix). Its **resonances** are the bulk Laplacian's spectrum. So the refined
Hilbert–Pólya, in this language:

> the nontrivial zeros are the **scattering resonances** of the conformal boundary operator built from
> `(Ω¹, h_∞)`; the **self-adjointness/positivity of the bulk** forces the resonances onto the critical
> line. **[bet]**

This is precisely Connes' "absorption spectrum" (a scattering picture) given a *conformal-geometric*
realization, and it is the Selberg theorem-template (`λ_n` real ⟹ zeros on the line) transported to
the arithmetic conformal boundary. The corner `−1/(2|u|)` is the **conformal weight of the scattering
kernel**; its `1/|1−λ|` raw form is the boundary Green's function of a scale-invariant operator.

## 4. The fusion — a precise division of labor

| framework | constructs | the precise job |
|---|---|---|
| **Segal Γ-rings / 𝕊** (Connes–Consani) | the algebraic skeleton | the `𝕊`-product `S²` and its Künneth; the `Ψ_λ` correspondences as cycles; the canonical class `K` and Serre duality (the FE) — **mostly done on the curve; the open piece is the product/Künneth = the `Ψ_λ` lift** |
| **condensed / analytic geometry** (Clausen–Scholze) | the archimedean metric | `h_∞` on `Ω¹` as a condensed-analytic (liquid) object: coherent archimedean Serre duality, and the **regularized, RH-signed `\widehat{deg}(Ω¹)`** = finite `Δ·Δ`. This is the framework built to make ℝ/ℂ-coefficient duality behave — exactly the corner's need |
| **spectral / scattering** (Connes; Patterson–Sullivan) | the operator | the conformally-covariant self-adjoint generator / scattering operator of `(Ω¹,h_∞)`; **resonances = zeros**; self-adjointness ⟹ critical line; the positivity = RH |

## 5. The precise problem statement

> **Construct a condensed-analytic conformal metric `h_∞` on the canonical `Ω¹` of `\overline{Spec ℤ}`
> over 𝕊** such that:
> 1. **(FE)** the induced Serre-duality pairing is the functional equation of `ξ`;
> 2. **(Δ·Δ)** the regularized self-intersection `\widehat{deg}(Ω¹,h_∞)` is finite, equivariant
>    (`ℝ₊^*`-covariant), and carries the Hodge sign;
> 3. **(spectrum)** the scattering operator of `(Ω¹,h_∞)` has resonances = the nontrivial zeros, with
>    self-adjointness forcing `Re ρ = ½`;
> 4. **(kill-test)** the construction *fails* for Davenport–Heilbronn and Epstein — it must use the
>    Euler product / the specific arithmetic of `\overline{Spec ℤ}`, not just the `Γ_ℝ` data.

Condition 4 is the guardrail that keeps this from being a dispersing reformulation: any `h_∞` that
exists equally for DH (same `Γ_ℝ`, off-line zeros) is wrong by construction.

## 6. The heart, and the first concrete move

The single load-bearing object is **the conformal scattering operator of `(Ω¹, h_∞)`**. The first
move — checkable, and a kill-test — is to **build the scattering/resonance map from the conformal
corner data and test whether it separates ζ from DH**: for ζ the resonances must be the zeros (on the
line); for DH (same archimedean conformal data, but Euler-product-free) the framing must *fail* to put
them on the line. If the conformal-scattering structure cannot distinguish them, the archimedean
conformal data is RH-neutral and the bet is dead — exactly the kind of false route the discipline is
for. If it *can*, we have the first equivariant object that sees the Euler product, and the program
has a spine.

Concretely next: (a) write the scattering kernel of the scale-invariant boundary operator and identify
its resonance condition; (b) feed ζ's and DH's archimedean+Euler data through it; (c) certify on real
ζ whether the resonances land on the line for ζ and off for DH. That is step 1 of actually building
the object — not characterizing the wall, building the first stone.
