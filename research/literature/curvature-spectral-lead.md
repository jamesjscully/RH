# What the negative corner sign leads to: negative curvature and the spectral forcing structure (2026-06-06)

Following the one structurally encouraging fact from `equivariant-regularization.md`: the diagonal
self-intersection divergence carries the **negative (Hodge-index) sign**. Pursued honestly — first
deflating it, then finding what genuinely survives. Tags **[THM]/[CONJ]/[AN]**; §8 throughout.

## First, the honest deflation: the sign alone is generic, RH-neutral

The naive reading ("`Δ·Δ < 0`, the Hodge direction — encouraging for RH") is **too generous**:

- The **arithmetic Hodge index theorem is already proven** (Faltings–Hriljac **[THM]**): the Arakelov
  pairing is negative-definite on the primitive part (`= −ĥ_NT`), with **no RH input**. Negative is
  the *generic* Arakelov sign.
- Davenport–Heilbronn shares the same `Γ_ℝ` archimedean factor ⟹ the **same negative corner**. So the
  sign is **shared with DH = RH-neutral** (consistent with our three prior confirmations). It is the
  **framework, not the content**.

So `sign(Δ·Δ) < 0` on its own is *necessary scaffolding*, not a signal that distinguishes RH-true ζ
from RH-false DH.

## What genuinely survives: not the sign, but the *infinitude*

`Δ·Δ` is not merely negative — it is **negative and divergent** (`~ −log(1/ε) → −∞`, computed). That
is more than the generic sign. By Gauss–Bonnet, `Δ·Δ ~ −χ ~ (2g−2)`, so

> `Δ·Δ → −∞`  ⟺  **infinite genus**  ⟺  a **negatively curved / hyperbolic** object.

The infinite-dimensional `H¹` (infinitely many zeros) is the same statement. So the corner is telling
us the *kind* of geometry the missing object must be: **negatively curved**, not flat or positively
curved. That is a real constraint, and it points somewhere specific.

## Where negative curvature leads: the Selberg/spectral forcing structure [AN→template]

Negative curvature is exactly the regime in which a **spectral forcing structure makes "RH" a
theorem.** For a compact hyperbolic surface the **Selberg zeta** is the precise analog of ζ:

| Riemann ζ | Selberg zeta of a hyperbolic surface |
|---|---|
| primes `p`, `log p` | closed geodesics `γ`, lengths `ℓ(γ)` |
| nontrivial zeros `ρ` | Laplacian eigenvalues `λ_n` via `s = ½ ± i r_n`, `λ_n = ¼ + r_n²` |
| archimedean corner (the `1/|1−λ|` fixed point) | the identity/area term of the trace formula |
| Weil explicit formula | **Selberg trace formula** (same shape) |

**The forcing [THM, for hyperbolic surfaces]:** the Laplacian `Δ_hyp` is **self-adjoint and positive**,
so `λ_n ≥ 0` are real, so (computed) `s = ½ + i√(λ−¼)` has `Re s = ½` for every `λ ≥ ¼`. **Selberg-RH
is a theorem** — the zeros are on the line *because the generator is self-adjoint*. (The finitely many
small `λ < ¼` give the controlled exceptional zeros.) A non-self-adjoint generator (complex `λ`) puts
the zeros off the line — verified by contrast.

So the chain is:

> `Δ·Δ < 0` and divergent  ⟹  **negative curvature / hyperbolic**  ⟹  **self-adjoint positive
> Laplacian**  ⟹  spectrum real  ⟹  **zeros on the line.**

The negative corner is the **first (necessary) link of the spectral (Hilbert–Pólya) forcing
structure** — the very template STRATEGY §1 lists as "proven over function fields, the object
missing over ℤ." Reaching it from the *curvature sign* is the genuine content of the encouraging fact:
it says the missing object is of the **negatively-curved / spectral / Selberg–Deninger type**, and it
**rules out** flat or positively-curved alternatives (where no such forcing exists).

## The Janus face — the same corner is the obstruction (loop closes)

Here is the honest sting, and it unifies the whole arc. The corner that **signals** the right
structure (negative-divergent ⟹ hyperbolic ⟹ self-adjoint forcing) is the *same* corner that
**obstructs** it: the `−1/(2|u|)` conformal singularity (`corner_defect.py`) is exactly the failure of
**essential self-adjointness** of the scaling generator — it forces a self-adjoint *extension*, and
(CC20) the extension breaks equivariance or misses the spectrum. So:

> The negative-divergent corner is **both the promise and the wound**: its sign/infinitude says "this
> is a hyperbolic object whose self-adjoint Laplacian would force RH," and its divergence says "but the
> generator is not (essentially) self-adjoint here." Gift and wound are one object — now at the level
> of the *forcing structure*, not just the geometry.

This is why the spectral route (Connes, Deninger) is the right instinct *and* why it stalls at the
same place: the operator that would force RH is obstructed by the corner that tells you to look for it.

## Honest verdict — what it leads to, and what it does not

**Leads to:** a sharp identification of the forcing structure the missing object must realize — a
**self-adjoint positive Laplacian-type generator on a (singular, since manifolds are excluded —
Deninger) negatively-curved arithmetic object**, the Selberg/Hilbert–Pólya template — plus a genuine
**constraint** (the object is hyperbolic/infinite-genus, not flat/positive-curvature) and the
**unification** of corner, self-adjointness, and curvature into one Janus object.

**Does not lead to:** a new handle. The sign alone is RH-neutral; the Selberg analogy is the *template*,
not a construction over ℤ; the hyperbolic object is unconstructed (manifolds provably excluded), the
self-adjoint generator obstructed (the corner), the positivity = the missing equivariant positive
Green form (BGS §6.3-open). The encouraging fact **reinforces and sharpens the spectral frontier; it
does not cross it.**

Net: the corner's negative sign is not a crack in the wall — it is a label on the wall, reading
"hyperbolic spectral object goes here," written in the same ink (`−1/(2|u|)`) as the lock.
