# What the intersection theory + Riemann–Roch on the square would look like — and the most real-number-like geometry that could carry it (2026-06-06)

A reflection, grounded in the precise gap (`the-missing-object.md`) and the function-field template.
Speculative parts are flagged **[spec]**; everything else is theorem **[THM]** or a verbatim program
position **[PROG]**.

## 1. What it would concretely look like

Write `S = \overline{Spec ℤ}` (the arithmetic curve: the primes `+` the archimedean place `∞`), and
let `S²` be the missing square (`= S ×_{𝔽₁} S` / the square of the Scaling Site). The structure
would be a **2-dimensional Arakelov/tropical intersection theory**:

- **Divisors.** The **diagonal** `Δ`; the "vertical/horizontal" fibers `{p}×S`, `S×{p}`, and `{∞}×S`;
  and the **Frobenius correspondences** `Γ_λ` (graphs of the scaling flow `λ ∈ ℝ_+^*`), with
  `Γ_λ ∘ Γ_{λ'} = Γ_{λλ'}` **[THM, Connes–Consani]**.
- **Intersection numbers — real-valued.** This is the crux of "real-number-like": unlike `C×C/𝔽_q`,
  where `(D·D') ∈ ℤ·log q`, here the numbers are **arbitrary reals**. The off-diagonal/Frobenius
  intersections reproduce the **prime side** of the explicit formula, `(Γ_λ·Δ) ↝ Σ_{p^k} (log p)·(…)`
  (the closed orbits of length `log p`), and the **diagonal self-intersection** `(Δ·Δ)` is the
  **regularized divergent** quantity (the `Σ log p` / the `logΛ` term + the archimedean
  Euler-characteristic contribution at the corner `∞×∞`, the "small square" `Δ=[0,1]²`).
- **Riemann–Roch on the surface.** `χ(D) = ½ D·(D−K_{S²}) + χ(𝒪)`, with `K` the canonical and `χ(𝒪)`
  arithmetic. The **`H¹`** is the cohomology carrying the zeros; because the zeros are infinitely
  many, **`H¹` is infinite-dimensional** (the "arithmetic genus" is infinite) — matching Deninger's
  leafwise `H̄¹` and Connes' Hilbert space. `Tr(Fr_λ \mid H¹) = Σ_ρ λ^ρ`.
- **The positivity (= RH).** `(D·D) ≤ 0` on the primitive part `{D : D·(\text{ample}) = 0}`, applied
  to `D = Γ_Fr − (\ldots)Δ`, forces `\{Re ρ = ½\}` exactly as Hodge-index does over function fields.

So the object is **Arakelov geometry (real intersection numbers) on a characteristic-1 base, on the
square** — every ingredient is in place except the two that carry RH: the **`H¹`** and the **`(D·D)≤0`
positivity** on the square.

## 2. "Most real-number-like" — made precise: characteristic 1 / the tropical reals

The function-field proof lives over `𝔽_q`, `q` **finite**. The arithmetic case is the **`q → 1`
limit** (Connes–Consani) — **characteristic 1** — and the most real-number-like incarnation of "the
field with one element" is the **idempotent / tropical semifield** `ℝ_+^{max} = (ℝ ∪ \{−∞\}, max, +)`
(or `(ℝ, min, +)`). Three precise senses in which this is *the* real-number-like geometry:

1. **Intersection numbers live in `ℝ`** (Arakelov), not `ℤ·log q` — because the archimedean Green's
   functions and the orbit lengths `log p` are real. "Real-number-like" is literal: the pairing is
   `ℝ`-valued.
2. **The primes become a real continuum of data**: under the scaling flow `ℝ_+^*`, each prime is a
   **periodic orbit of length `log p`** — the discrete primes are coordinatized by real lengths, and
   the archimedean place is the **fixed point**. The discrete arithmetic is dissolved into a real
   dynamical system **[THM, the Scaling Site]**.
3. **The base is genuinely a real object**: the Scaling Site is a **tropical curve** `[0,∞)⋊ℕ^×`;
   its square is a tropical surface. Tropical geometry *has* a Riemann–Roch (Baker–Norine;
   Gross–Shokrieh; Mikhalkin–Zharkov) — so the *template* for a Riemann–Roch on a real object exists
   **[THM]**; the open part is the 2-dimensional version with the right `H¹` and Serre duality.

So the honest answer to "what is the most real-number-like geometry that could support this" is:
**Arakelov intersection theory over a characteristic-1 (tropical/idempotent) base — the geometry of
the tropical reals `ℝ_+^{max}` with real-valued intersection numbers.** That is exactly the
Connes–Consani direction, and it is the most-developed candidate precisely because it *is* the most
real-number-like.

## 3. Why it is hard — and the precise obstructions to "real-number-like"

Three sharp obstructions say the geometry **cannot be too nice**:

- **A smooth real manifold is provably excluded [THM, Deninger].** The leafwise structure forces a
  conformal weight `α` with `Re ρ = α`; manifolds give `α = 0` (wrong), and they cannot carry the
  required archimedean fixed points. So the real-number-like space must be **singular** — a
  lamination, a non-Hausdorff/stacky object, or a topos — not a manifold.
- **The Hodge-index positivity is a compact-Kähler fact, but the square is non-compact at `∞`
  [THM/AN].** Over `𝔽_q`, `C×C` is *projective*; Hodge index needs a polarization. The arithmetic
  square's archimedean corner `∞×∞` is an analytic boundary, not a closed point, and the diagonal
  self-intersection **diverges** there (the "small square `Δ`"). The positivity is exactly where
  compactness fails.
- **The positivity can fail for purely formal reasons [THM, BGS §6.3].** Positive Green forms do not
  always exist; Connes–Consani localize the obstruction to a derivative jump at `ρ=1`. So a
  *characteristic-1 / tropical* structure must **force** a positivity that is false in general — it
  cannot be a soft consequence of the formalism. This is the precise reason "supply the object" ≠
  "supply RH".

In characteristic 1 the degeneration is *infinitely* strong (`1+1=1` collapses linear algebra), and
**`H¹` on the square has no definition** **[PROG]** — cohomology in characteristic 1 is genuinely
unsolved at degree 1 on a surface. That is where "real-number-like" runs out: the most real-number-
like base we have (`ℝ_+^{max}`) is *too* degenerate to obviously carry an `H¹` with Serre duality.

## 4. The deepest tension — and a hint from GUE [spec]

Why might the right geometry be **noncommutative/spectral** rather than tropical-commutative? The
**zeros obey GUE statistics** (Montgomery). If they were Frobenius eigenvalues on a *classical
algebraic* `H¹`, their correlations would carry algebraic rigidity; GUE says they look like
eigenvalues of a **generic self-adjoint operator**. This is a real hint that the `H¹` is
**random-matrix-like, not algebraic** — i.e. a *Hilbert space with a self-adjoint operator* (Connes'
spectral realization on the adèle class space), where:

- the geometry is **noncommutative** (the adèle class quotient is a bad quotient = an operator
  algebra), which is *also* a real-number-like geometry — the "points" are states on a `C^*`-algebra;
- the positivity is **operator positivity / self-adjointness** (`T = −iΘ` self-adjoint ⇒ `Re ρ = ½`),
  and the GUE-ness is the natural spectral statistics of a generic such operator.

So there are **two** real-number-like answers, and they may be the same object seen twice:
*commutative-tropical* (Arakelov over `ℝ_+^{max}`, the Scaling Site square — real intersection numbers)
and *noncommutative-spectral* (a spectral triple / the adèle class space — a real Hilbert space with a
self-adjoint flow). Connes–Consani's program is precisely the bridge between them; the unbuilt `H¹`
on the square is, on the spectral side, exactly the Hilbert space carrying the absorption spectrum,
and the missing positivity is its self-adjointness = the Weil positivity.

## 5. Honest assessment

The most real-number-like geometry that *could* carry this is **characteristic-1 Arakelov geometry**
— intersection theory with real-valued numbers over the tropical reals `ℝ_+^{max}`, equivalently the
noncommutative geometry of the adèle class space — and we can say precisely why it is hard: it must
be **singular** (manifolds excluded), it must **compactify the archimedean corner** (where the
diagonal diverges), and it must **force a positivity that is formally false** (BGS §6.3). The two
genuinely missing ingredients are sharply named: an **`H¹` on the square with Serre duality**, and the
**`(D·D) ≤ 0` / self-adjointness positivity** on it — the reverse force. Whether such a geometry
exists is the deepest open problem in the subject; what this program adds is the *precise shape* of
what it must be and the *precise locus* (the small square `Δ`, the corner `∞×∞`, characteristic-1
`H¹`) where every existing construction stops.
