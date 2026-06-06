# Geometry of the square — the corner, the self-adjoint operator, the H¹, and fusion (2026-06-06)

A hard push on the **geometry side** of the missing object (`the-missing-object.md`,
`what-would-it-look-like.md`): what *constructing* the H¹-on-the-square + compactifying the
archimedean corner would take, and the most promising **current** (2015–2026) attempt, named with
its precise blocker. Discipline per `STRATEGY.md` §8: **[THM]** = proven (with source/theorem
number), **[PROG]** = program / defined-but-incomplete, **[CONJ]** = conjectural, **[AN]** = analogy.
Quotes in `"…"` are verbatim from the cited source.

**Sources read directly for this note (2018–2026, beyond the earlier literature notes):**
- Connes–Consani, *Riemann–Roch for `\overline{Spec ℤ}`*, arXiv **2205.01391** v2 (2023), publ. 2023
  (full pdftotext read). Cited **[RR-Z]**.
- Connes–Consani, *On the Jacobian of `\overline{Spec ℤ}`*, arXiv **2602.15941** v1 (17 Feb 2026)
  (full pdftotext read). Cited **[Jac]**.
- Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv **2006.13771**
  (local PDF, re-read for the corner divergence and self-adjointness status). Cited **[CC20]**.
- Deninger, *Dynamical systems for arithmetic schemes*, arXiv **1807.06400** v4 (2024), publ.
  Indag. Math. 2024 (full pdftotext read). Cited **[D18]**.
- Morishita, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's
  adelic spaces*, arXiv **2508.15971** v5 (Jan 2026) (intro read). Cited **[Mor]**.
- Bost, *Theta invariants of euclidean lattices and infinite-dimensional hermitian vector bundles
  over arithmetic curves*, arXiv 1512.08946 / Progress in Math. 334 (2020). Cited **[Bost]**.
- Clausen–Scholze, *Lectures on Analytic Geometry* (2022); *Condensed Mathematics and Complex
  Geometry* (Serre duality, coherent duality). Cited **[CS]**.

This note **supplements** the four earlier files; it does not restate their general gap. Its job is
the four sharp questions. **Headline finding:** the geometry side advanced *substantially* on the
**arithmetic curve** between 2018 and 2026 (Deninger's periodic orbits **constructed** [THM];
Connes–Consani's **Riemann–Roch, Serre duality, and Jacobian for `\overline{Spec ℤ}` itself proven**
[THM]) — but **every one of these advances is on the 1-dimensional curve, not the square**, and the
**H¹ on the square, the corner compactification, and the intersection positivity remain exactly as
open as before.** The wall did not move; the approach to it is now paved.

---

## 1. The corner / `Δ·Δ` regularization — precise analytic form and current status

### 1.1 Where the divergence lives, exactly (the "small square" `Δ=[0,1]²`)

The archimedean corner `∞×∞` is, in the operator picture of [CC20], the **first quadrant of the
`(x,y)`-plane** split by the diagonal-trace geometry into the **small square `Δ=[0,1]²`** and the
**big (infinite) square `Σ=(1,∞)²`**; the kernel weight `P(1/y)−P(x)` is `+1` on `Δ`, `−1` on `Σ`
([CC20] §1, Fig. 1). The scaling operator `f(x)↦f(λx)` has Schwartz kernel `k(x,y)=δ(λx−y)`, whose
**diagonal integral `∫k(x,x)dx` is literally the intersection with the diagonal** ([CC20] p.4,
verbatim: the trace "`corresponds geometrically to the intersection with the diagonal`"). So `Δ·Δ`
is the diagonal-trace over the corner, and its divergence is the corner divergence.

### 1.2 The precise analytic form of the divergence — **[THM]** (verbatim from [CC20])

The geometric (prime/archimedean) side of the explicit formula at `∞` is the **elusive distribution
`W_ℝ`**, which "`coincides, outside 1, with a locally rational, positive function that tends to +∞ as
the variable tends to 1`" ([CC20] Appendix B eq. (150)). The corner's analytic shadow is the
**trace-remainder** `δ(ρ)` (the `Δ`-vs-`Σ` discrepancy, [CC20] eq. (8)), given **explicitly** for
`ρ ≥ 1` ([CC20] eq. (10)):

> `δ(ρ) = 2ρ^{1/2} ( Si(2π(1+ρ))/(2π(1+ρ)) + Si(2π(ρ−1))/(2π(ρ−1)) )`,  with `δ(ρ^{-1})=δ(ρ)`,

`Si` the sine integral. **The decisive feature is a jump in the first derivative `δ'(ρ)` at `ρ=1`:
from `−1` as `ρ→1⁻` to `+1` as `ρ→1⁺`** ([CC20] eq. (50), Fig. 2). This derivative jump **is the
diagonal self-intersection singularity**: imposing the vanishing conditions `\hat f(±i/2)=0` (the
"`H¹` conditions", §2.3 below) replaces `δ` by `Qδ` with `Q=−(ρ∂_ρ)²+¼`, and **the jump generates
`−2δ'_1` (twice the derivative of the Dirac mass at `ρ=1`)** ([CC20] §2–3). On the Fourier side the
divergence is `θ'(t)→+∞ as t→±∞` (`θ` = Riemann–Siegel angular function); `\hatδ(t)+2θ'(t) ≥ 0` and
`\hatδ` "`compensates almost exactly the part of the graph of θ'(t) where this function is
negative`" ([CC20] p.3, Figs. 5–6).

So the **precise analytic form** of the corner divergence is: a **principal-value singularity of
`W_ℝ` at `ρ=1` (`~+∞`), equivalently a `−2δ'_1` distributional term born from the `δ'`-jump**, equiv.
the `θ'(t)→+∞` tail. This is the analytic incarnation of `Δ·Δ = ∞` and the `logΛ` cutoff divergence
of `scaling-site` §2.3 (`1805.10501 §3.4`).

### 1.3 The current regularization — and **does it give the right sign?**

**[CC20] regularizes the corner by "moving `Δ` into `Σ`"** ([CC20] §4): the negative small-square
contribution is absorbed into the *infinite positivity reservoir* of the big square `Σ`, via the
**prolate-spheroidal / pair-of-projections** decomposition of the infinite dihedral representation
at cutoff `Λ=1`. The operator-level outcome (Theorem 3.6) is `D∘Q = −2·Id + K` with `K`
Hilbert–Schmidt; reducing `K` (for `I=[½,2]`) to a **Hermitian Toeplitz matrix** (the `q→1⁺`
discretization `q^ℤ` of `R⁺_*`) and lowering its top eigenvalue below 1 **by a single orthogonality
condition** (§6) yields:

> **[THM, CC20 Thm 1 / Cor 2]** `W_∞(g⋆g^*) ≥ Tr(ϑ(g) S ϑ(g)^*) ≥ 0` for smooth positive-definite
> `g` with support in `(½,2)` and `\hat g(±i/2)=0` — the corner positivity holds **after finitely
> many linear conditions, at the single place `∞`, and the sign is correct** (`≥ 0`).

So **yes, the current regularization yields the right sign — but only at one place, after imposing
the `H¹` conditions by hand, and only for support `(½,2)` (no primes).** This is the strongest
positive result on the corner, and it is **real but local**. The Toeplitz top-eigenvalue argument is
the load-bearing mechanism; it is also the thread that links to the operator question (§2).

**Honest status of "right sign":** the right sign is obtained *because* the small-square negativity is
finite-rank-correctable against an infinite positive reservoir. This is **not** a Hodge-index/intersection
argument and does **not** see the prime side; the part that would carry RH (the Euler-product term in
`N(u)`) is exactly the part the corner regularization does not reach. Per the project's own diagnosis
(`the-missing-object.md` §5), the corner/`θ'`/Sonin apparatus is built from the **functional-equation
`Γ_ℝ` data shared with Davenport–Heilbronn ⇒ RH-neutral**. So: the corner regularization is a genuine
theorem with the right sign, but on the **RH-neutral** facet of the object.

### 1.4 Bost's theta invariants — the other corner-regularization technology, and why it is not (yet) the square's

[Bost] gives the most developed **non-compact arithmetic intersection** technology: an Arakelov theory
of **infinite-dimensional Hermitian vector bundles over the arithmetic curve `Spec O_K`** with the
central invariant `h⁰_θ(\overline E) := log Σ_{v∈E} e^{−π‖v‖²}` (a theta/`log`-theta number replacing
`dim H⁰`). **[THM]** for the **curve**: a full Riemann–Roch-type formalism with `h⁰_θ, h¹_θ`, an
arithmetic-Hilbert/Poisson duality, and slopes — explicitly handling **non-compact fibers**
(infinite-rank lattices) by `θ`-regularization, the exact thing the corner needs. **But [Bost]'s
objects are bundles over the 1-dimensional `Spec O_K`; he does not construct the square or a diagonal
self-intersection.** [RR-Z]'s introduction (verbatim) places Bost's `log`-theta program precisely:
"`This view of the log-theta number as a dimension remains virtual for the obvious reason that it
outputs real numbers rather than integers. An interpretation of these numbers as Murray–von Neumann
dimensions could greatly improve their status as dimensions, but this step has not been achieved so
far.`" So Bost's `θ`-regularization is the most powerful non-compact-fiber tool, it has the right
shape, and it is **stuck at the same place: real-valued (non-integer) dimensions on the curve, no
square.** (Connes–Consani's 2023 `[RR-Z]` is in part an answer to exactly this — see §3.1.)

**Corner bottom line.** The divergence is **pinned analytically** (`δ'`-jump at `ρ=1` `⟹ −2δ'_1`,
`W_ℝ~+∞` at `1`). Two regularizations exist: (a) [CC20] prolate/Toeplitz "move `Δ` into `Σ`",
**right sign, one place, conditional, RH-neutral facet**; (b) [Bost] `θ`-regularization, **right
shape, curve only, real-valued dimensions**. Neither gives a **divergence-free `Δ·Δ` on the square
with a sign that is RH** — that remains open.

---

## 2. The prolate/Sonin operator as the Hilbert–Pólya candidate — is it self-adjoint?

### 2.1 The sharp answer: **the relevant scaling Hamiltonian is NOT made self-adjoint, and "corner-compact ⟺ self-adjoint" is FALSE as stated in their setup**

This is the single most important clarification of this note, and it is **explicit in [CC20]**.

- The "Hilbert–Pólya operator" would be the **scaling Hamiltonian** `Du = x∂_x` (generator of `ϑ`),
  whose one-parameter group "`giving the spectral realization of the zeros of the Riemann zeta
  function`" ([CC20] p.3). **[CC20] states verbatim that restricting it is obstructed:** the cutoff
  of Berry–Keating "`lack[s] invariance under the scaling action ϑ … This issue makes problematic
  restricting the Hamiltonian.`" ([CC20] lines 73–75). There is "`a single 'quantum cell' arising
  from the absorption spectrum that was not accounted for`" by the naive cutoff.
- **Their resolution does NOT self-adjointify the Hamiltonian.** Instead they use the **orthogonal
  projection `S` onto Sonin's space** (functions vanishing with their Fourier transform on `[−1,1]`).
  Crucially ([CC20] verbatim): "`the scaling action ϑ does not restrict to this subspace`." So `ϑ` is
  **not** self-adjoint/unitary on Sonin's space — they sidestep self-adjointness entirely. Positivity
  comes from `Tr(ϑ(g) S ϑ(g)^*)` being "`the trace of a positive operator`" — **`S` is a positive
  projection, not the spectrum of a self-adjoint Hilbert–Pólya operator.**
- The only self-adjoint operators that *do* appear are auxiliary: `Q=−(ρ∂_ρ)²+¼` (self-adjoint on
  `L²(R⁺_*,d^*ρ)`, [CC20] Lemma 5.1), `D=Du²+Du` with `D^*=D` ([CC20] eq. after (92)), and the
  **Hermitian Toeplitz matrix `K`/`T`** whose spectrum is computed in §6 ([CC20] Thm 6.8: spectrum
  `⊂ {λ_max} ∪ [−2, λ₂]`, `λ₂ ≤ 0.7722`). These are **tools for the positivity estimate, not a
  Hilbert space whose self-adjoint generator has spectrum = the zeros.**

### 2.2 Spectrum vs zeros, and the role of the cutoff

The **prolate-spheroidal wave functions** `ξ_n` (eigenfunctions of the `PS_{2n,0}(2π,x)` operator,
[CC20] §4–5, eq. (84)) are the eigenfunctions of the *pair of projections* `(P_Λ,\hat P_Λ)` at the
time–frequency cutoff `Λ=1`; they diagonalize the Sonin compression, not the zeta dynamics. The
**Slepian/prolate cutoff `Λ=1` is exactly the "corner compactification" on the operator side** — it
is the imposition of the finite time–frequency window whose complement (Sonin's space) carries the
manifest positivity. So the dictionary is:

| geometry | operator side |
|---|---|
| compactify the corner `∞×∞` | impose the `Λ=1` prolate/Slepian cutoff (project onto Sonin's space `S`) |
| `Δ·Δ` divergence | `δ'`-jump at `ρ=1` ⟹ `−2δ'_1` |
| would-be RH positivity | `Tr(ϑ(g) S ϑ(g)^*) ≥ 0` **[THM at `∞`, conditional]** |
| Hilbert–Pólya self-adjointness | **absent — replaced by a positive projection, not a self-adjoint generator** |

So **"corner compact ⟺ operator self-adjoint" is, in their setup, neither a theorem nor a heuristic
they endorse — it is replaced by "corner compact (= Sonin projection) ⟹ positive (compressed) trace",
which is weaker** (a positive operator, not a self-adjoint one with real spectrum = zeros). The
Connes 1999 spectral realization gives the zeros only as an **absorption spectrum** on a weighted
Sobolev space `L²_δ`, and (per `deninger-spectral-cohomology.md` §2.2, Connes' own caveat) the weight
`δ` "`artificially cuts the multiplicities`" and is **engineered around the critical line**, not a
self-adjoint operator forcing zeros onto it. **Net [THM/PROG]: there is no constructed self-adjoint
Hilbert–Pólya operator here; the positivity route deliberately avoids self-adjointness.** This is the
honest state of the Hilbert–Pólya question on the geometry side as of [CC20].

### 2.3 The `H¹` conditions are imposed by hand

The vanishing conditions `\hat g(±i/2)=0` (eq. (11)) that make the corner positivity work are
interpreted by the authors ([CC20] p.3) as the function-field "`key contribution of H¹ in Lefschetz's
trace formula`." **This is the H¹-on-the-square being imposed as a boundary condition, not
constructed** — the cleanest single statement of why the archimedean positivity, though a real
theorem, does not yet carry reverse force: the `H¹` ingredient is an input, not an output.

---

## 3. The H¹ on the square — the most promising route, and the precise blocker

### 3.1 Decisive 2023–2026 progress — but on the CURVE, not the square: `[RR-Z]` and `[Jac]`

The biggest geometry-side development since the earlier notes were written is that **Connes–Consani
proved a genuine Riemann–Roch theorem, with H⁰, H¹, integer dimensions, and Serre duality, for the
Arakelov compactification `\overline{Spec ℤ}` itself** [RR-Z] (2023). This is **[THM]** and is *new*
relative to `connes-consani-scaling-site.md` (which records H¹ on the *square* as open and only the
`C_p`-Riemann–Roch as done). Precisely:

- **[THM, RR-Z Thm 1.1]** For an Arakelov divisor `D` on `\overline{Spec ℤ}`,
  `dim_{S[±1]} H⁰(D) − dim_{S[±1]} H¹(D) = ⌈ deg′D + log′2 ⌉′ − 𝟙_L`,
  with `deg′ = deg/log 3` (base-3 degree — `ℤ` reappears "`as a ring of polynomials Σ a_j 3^j with
  coefficients in {0,±1}`"), `⌈·⌉′` the odd ceiling, `𝟙_L` a finite-measure exceptional correction.
- **[THM, RR-Z Thm 1.2 (Serre duality)]** with canonical divisor `K=−2{2}`, `deg K=−2log2`:
  `H⁰(K−D) ≅ Hom_{ΓT_*}(H¹(D), H¹(K))`, `H¹(K)=U(1)_{1/4}` the dualizing module — the analogue of
  Grothendieck's form of Serre duality, derived from **Pontryagin duality of "tolerant `S[±1]`-modules"**.
- The cohomologies `H⁰(D), H¹(D)` are **genuine `S[±1]`-modules with integer dimensions**, defined
  via the **Γ-space `H(D)`** (Dold–Kan from a short complex of `S[±1]`-modules) over the **sphere
  spectrum `S`** / Segal Γ-rings ("`au dessous de Spec ℤ`"). This **solves the integrality problem
  that blocked Bost/van der Geer–Schoof** (§1.4): the dimensions are integers, not real-`log`-theta
  numbers. The proof "`parallels Weil's adelic proof of Riemann–Roch for function fields including
  the use of Pontryagin duality`."

So on the **curve**, the full template (H⁰, H¹, integer dims, Serre duality, Riemann–Roch) now
**exists as a theorem.** [Jac] (Feb 2026) extends this to the **arithmetic Picard and Jacobian
monoids** of `\overline{Spec ℤ}`: `Pic(\overline{Spec ℤ}) ≅ X_Q = Q^*\A/\hat Z^*` (the Riemann sector
of the adèle class space) as a moduli space of metrized rank-1 groups `(L,‖·‖)` [Jac Thm 1.1], an
**Abel–Jacobi map** `Θ` whose image is exactly the **idempotents** of the Jacobian monoid [Jac Thm
2.16] (the curve has **infinite genus**, so `Θ` does not surject onto an abelian variety but onto an
idempotent semilattice), and a **universal cover** `\widetilde{Spec ℤ}` whose fiber over `C_p` is the
**mapping torus of Frobenius** `T_p = (K^{(p)}×R)/((u,t)∼(pu,t+log p))` realizing the Artin/Frobenius
linking of `p` with all other primes [Jac Thm 1.3, §7.2]. **All [THM].**

### 3.2 The blocker is unchanged and now sharply isolated: **H¹ on the SQUARE**

**None of [RR-Z], [Jac], [Bost], [D18] constructs an H¹ on the square `S²` / `\overline{Spec ℤ}²`.**
The 2023 Serre duality is the duality of the **curve** (Pontryagin duality of `S[±1]`-modules in one
variable); it is **not** a Serre duality `H¹×H¹→H²` on a surface. The Jacobian [Jac] is the Jacobian
of the **curve** (a 1-dimensional invariant), not the square. So the precise current state of the
square's H¹ is:

> **[PROG/CONJ — the blocker, unchanged]** The H¹ on the square `S²` — the `2g`-dimensional (here
> infinite-dimensional) cohomology carrying the zeros as Frobenius/flow eigenvalues, with a Serre
> duality `H¹×H¹→H²` *on the surface* and an intersection pairing whose positivity is RH — **has no
> construction.** `H⁰`(square) is straightforward and `H²`(square) can be *defined* by turning Serre
> duality into a definition; **`H¹`(square) is the open middle term** (`1805.10501 §1`, verbatim:
> "`still open at this time … an appropriate definition of the sheaf cohomology … H¹`").

What 2023–2026 changed: the **template now demonstrably works in characteristic 1 in one variable**
(integer-dimensional H⁰/H¹, Serre duality, Riemann–Roch on the curve — [RR-Z]). This is **strong
positive evidence** that the `S`/Γ-ring/sphere-spectrum machinery can carry the missing structure,
and it converts the square's H¹ from "no idea how" to "lift the proven curve construction to two
variables." But the **lift is exactly the unproven step** — the same obstruction
`connes-consani-scaling-site.md` §4 names (the complex/two-variable lift loses the canonical
char-1 Frobenius `Ψ_λ`; `1805.10501 §7`, "`the most problematic`" step 3).

### 3.3 Deninger (2018) — periodic orbits **constructed** [THM], H¹ and corner **not** [PROG]

[D18] is the most concrete 2018+ "dynamical systems for arithmetic schemes." Honest status:

- **[THM, D18]** Using **sheafified rational Witt vectors** `W_rat`, Deninger **constructs**, for every
  integral normal scheme `X₀` flat of finite type over `Spec ℤ`, an infinite-dimensional `R`-dynamical
  system `X₀ = X̌₀(C) ×_{Q>0} R>0` whose **closed points `x₀` correspond to compact packets `Γ_{x₀}`
  of periodic orbits of length `log N x₀`** (primes `↔` orbits of length `log p`). This is a **genuine
  construction** — the long-missing realization of `[Den00] 3.1/4.9` — built from **Frobenius elements
  in Galois groups** (intrinsically, via `W_rat`, after Kucharczyk–Scholze). He proves `X₀` is
  **connected** and `H⁰_F(X₀)=R` (one-dimensional) [D18 Thm 10.2].
- **[NOT constructed in D18 — the open part]:**
  1. **No archimedean fixed point.** Verbatim: "`There are no fixed points of the flow.`" The
     compactification `\overline{X₀}` (whose fixed points would be the archimedean place
     `X₀(C)/F∞`) is only **predicted**: "`It should extend to an R>0-immersion … into \overline{X₀}`";
     and even then "`it is unclear why \overline{X₀} would not contain many more fixed points`" — the
     system is **too big**, and Deninger asks (open) whether a **smaller sub-system `Y₀` of the right
     dimension `2d+1`** (a Riemann-surface lamination for `d=1`) exists. **The corner is exactly the
     open part of his construction.**
  2. **Only `H⁰_F` is computed** [Thm 10.2]; the **`H¹_F` carrying the zeros, its self-adjoint
     generator `Θ` (`Re ρ=½ ⟺` orthogonality of the rescaled flow), and the Lefschetz trace formula
     with the archimedean fixed point are NOT constructed** — they remain the [CONJ] program of
     `deninger-spectral-cohomology.md` §1. The `α=1` conformal-weight problem (manifolds excluded) is
     untouched by [D18]; the spaces are "`an approximation to the … true space X₀[C]`."
- **[Mor] (2026)** relates Deninger's `W_rat` spaces (for abelian number fields) to Connes–Consani's
  adelic spaces — a **bridge theorem** answering Deninger's own §7 question, confirming the two
  programs are facets of one object. But [Mor] relates the **function spaces / coverings**, not an
  `H¹` or a positivity; it is convergence evidence, not the missing cohomology.

### 3.4 Condensed / analytic geometry (Clausen–Scholze) — the tool exists, **not yet aimed at the corner**

[CS] (2022) gives **analysis-free proofs of finiteness of coherent cohomology, Serre duality, GAGA,
and HRR**, in a framework "`unifying complex-analytic and p-adic/Berkovich/adic geometry`" — i.e. a
**uniform archimedean+nonarchimedean coherent-duality machine**, which is precisely what an `H¹` on
the square with Serre duality at the archimedean corner would want. **But there is, as of mid-2026, no
published work applying condensed/analytic geometry to: the archimedean corner of `Spec ℤ`, an `H¹`
on `\overline{Spec ℤ}²`, or RH.** The connection is **[AN], speculative**: condensed math is the most
plausible *formal home* for "`descent that remembers norms`" (the metric enrichment `STRATEGY.md` §3),
and its archimedean Serre duality is the right *kind* of theorem — but no one has built the square in
it. (Older "Archimedean cohomology" à la Consani–Marcolli predates and does not give the square.)

### 3.5 Which route is closest, and the precise blocker

**Closest to an actual `H¹` with Serre duality: Connes–Consani's `S`/Γ-ring construction [RR-Z],
because it is the only one that has produced a *proven, integer-dimensional* `H⁰`/`H¹` with Serre
duality and Riemann–Roch — in characteristic 1, over the sphere spectrum — on `\overline{Spec ℤ}`.**
The precise blocker, named:

> **THE BLOCKER:** the `[RR-Z]` cohomology is **one-variable** (Pontryagin/Serre duality of `S[±1]`-
> modules on the *curve*). Promoting it to the **square** requires a **two-variable / surface sheaf
> cohomology over the sphere spectrum** with (i) a defined `H¹(S²)`, (ii) Serre duality `H¹×H¹→H²` on
> the surface, and (iii) a **divergence-free self-intersection `Δ·Δ`** absorbing the `−2δ'_1` corner
> term (§1.2) into the right (RH-signed) Euler characteristic. Step (iii) is obstructed because the
> canonical char-1 Frobenius correspondences `Ψ_λ` **do not lift** to the two-variable/complex setting
> (`1805.10501 §7`), and step (i)+(ii) require a **char-1 homological algebra on a surface** that does
> not exist (the begun Ext/resolution-of-the-diagonal theory yields `H⁰,H²` but not `H¹`).

---

## 4. The fusion question, sharply: does compactifying the corner FORCE positivity?

**The function-field mechanism to transport:** `C×C` **projective** (compact) `⟹` Hodge index theorem
on the surface `⟹` `(D·D)≤0` on the primitive part `⟹` Weil positivity `⟹` RH. The fusion hope is
that **compactifying the archimedean corner `∞×∞`** plays the role of "projective", and **forces** the
positivity (self-adjointness). Sharp current status:

### 4.1 Is there a concrete result where corner-compactification forces positivity? — **No (and the one partial instance is RH-neutral).**

- The **one concrete instance** where a corner-cutoff *does* produce positivity is [CC20] §1.3: the
  **Slepian/prolate `Λ=1` cutoff (= corner compactification on the operator side) `⟹`
  `Tr(ϑ(g)Sϑ(g)^*)≥0`** [THM, §1.3, §2.1 above]. This is a **real "compact ⟹ positive" implication** —
  but (a) it is **one place `∞`**, (b) **conditional** (finitely many `\hat g(±i/2)=0` conditions), and
  (c) on the **RH-neutral functional-equation facet** (`Γ_ℝ`/`θ'`, shared with Davenport–Heilbronn).
  It does **not** touch the prime/Euler-product side where the RH content lives. So **the only concrete
  "corner-compact ⟹ positive" theorem we have is on the part of the object that is RH-neutral.**
- There is **no result** in which compactifying the corner forces the **global** Weil positivity / the
  self-adjointness of a Hilbert–Pólya operator / a Hodge-index `(D·D)≤0` on the square. The transport
  is **[AN], not [THM]**: the Hodge index theorem is a **compact-Kähler** fact and the **arithmetic
  Hodge index theorem is proven [THM] only on the relative-curve surface `X→Spec ℤ`** (Faltings–
  Hriljac–Moriwaki–Yuan–Zhang, `arakelov-arithmetic-surface.md` §2) — right sign, **wrong surface**,
  blind to `ζ`. On the missing self-product it is unproven.

### 4.2 Is there a precise reason it CANNOT? — a real obstruction, not a no-go.

The transport faces **three sharp obstructions** (these are the precise "reasons", and they are
**obstructions, not impossibility theorems**):

1. **BGS §6.3 — positive Green forms can genuinely fail [THM].** A positive Green form for a cycle
   need not exist (Cor. 6.3.2; explicit counterexamples). So the corner positivity is **not formal**:
   compactifying cannot *automatically* force it, because the analogous positivity is **false in
   general**. The geometry must force a positivity that is **not a soft consequence of compactness** —
   this is the precise reason "supply the object ≠ supply RH" (`what-would-it-look-like.md` §3).
2. **The corner is an analytic boundary, not a closed point [THM/AN].** Over `𝔽_q`, `C×C` is genuinely
   *projective*; the arithmetic square's `∞×∞` is where the diagonal self-intersection **diverges**
   (§1.2). "Compactness" is exactly what fails there, so the function-field polarization argument has
   no literal analogue — it must be *replaced* by the `θ`/prolate regularization, which (§4.1) lands on
   the RH-neutral facet.
3. **Self-adjointness is avoided, not forced [THM, this note §2].** In the one worked case [CC20], the
   corner cutoff yields a **positive projection `S`, not a self-adjoint generator** — the scaling
   Hamiltonian provably **does not restrict** to the cutoff space. So even where "corner-compact ⟹
   positive" holds, it does **not** deliver "operator self-adjoint." The Deninger route would *force*
   `Re ρ=½` via self-adjointness (orthogonality of the `α`-rescaled flow), but needs `α=1`
   (**manifolds excluded [THM]**) and an `H¹` and an archimedean fixed point — **none constructed**
   ([D18] §3.3).

**Fusion verdict [PROG/AN].** There is **no concrete result** in which compactifying the corner
*forces* the RH positivity/self-adjointness, and there are **three precise obstructions** explaining
why it cannot be automatic — but **none is a no-go theorem**; they say the positivity is *substantive*
(BGS §6.3), the corner is *singular* (divergent `Δ·Δ`), and the worked regularization is
*self-adjointness-free and RH-neutral*. The fusion remains the **defining open problem**, now with its
failure modes pinned exactly.

---

## 5. Bottom line — the state of the geometry side (2026)

1. **Corner regularization.** The divergence is **pinned**: `δ'`-jump at `ρ=1` `⟹ −2δ'_1`,
   `W_ℝ~+∞` at `1`, `θ'(t)→+∞`. Two regularizations: [CC20] prolate/Toeplitz "move `Δ` into `Σ`"
   (**right sign, one place, conditional, RH-neutral facet** — [THM]) and [Bost] `θ`-regularization
   (**right shape, curve only, real-valued dimensions** — [THM]). **No divergence-free, RH-signed
   `Δ·Δ` on the square.**
2. **Self-adjoint operator.** **There is no constructed self-adjoint Hilbert–Pólya operator.** [CC20]
   deliberately **avoids** self-adjointness (the scaling Hamiltonian provably does not restrict to the
   cutoff/Sonin space); positivity comes from a **positive projection**, not a self-adjoint generator.
   "Corner-compact ⟺ self-adjoint" is **false as stated** in their setup; the true implemented
   statement is the weaker "corner-cutoff `⟹` positive compressed trace" [THM, conditional, at `∞`].
3. **Closest H¹ route.** **Connes–Consani's `S`/Γ-ring construction**: in 2023 they **proved**
   Riemann–Roch + Serre duality + integer-dimensional `H⁰/H¹` for the **curve** `\overline{Spec ℤ}`
   [RR-Z], and in 2026 the **Picard/Jacobian/Abel–Jacobi** structure [Jac]. This is the only program
   that has produced a **proven `H¹` with Serre duality** (solving Bost's integrality obstruction) —
   but **on the curve, not the square.** Deninger [D18] **constructs the periodic orbits = primes**
   [THM] but **not** `H¹`, the self-adjoint generator, or the archimedean fixed point. Condensed/
   analytic geometry [CS] supplies the right *kind* of archimedean Serre-duality machine but is **not
   yet aimed at the corner/square** [AN].
4. **The single sharpest blocker (geometry side).** **There is no two-variable (surface) sheaf
   cohomology over the sphere spectrum giving a defined `H¹(S²)` with Serre duality `H¹×H¹→H²` on the
   square and a divergence-free, RH-signed self-intersection `Δ·Δ`** absorbing the `−2δ'_1` corner
   term. The one-variable case is now a theorem [RR-Z]; the **lift to the square is blocked because the
   canonical char-1 Frobenius correspondences `Ψ_λ` do not lift to two variables** (`1805.10501 §7`,
   "the most problematic" step) **and char-1 homological algebra yields `H⁰,H²` but not `H¹` on a
   surface.** Equivalently, on the operator side: **the corner cutoff yields a positive projection, not
   a self-adjoint operator forcing the zeros onto the line.** That gap — `H¹` on the square ⟺
   self-adjointness — is exactly the reverse force, and it is still open.

**Net change since the earlier notes:** the geometry side moved **from "H¹/Serre duality undefined
even on the curve" to "H¹/Serre duality/Riemann–Roch proven on the curve" [RR-Z 2023]**, and from "no
construction of primes-as-orbits" to "primes-as-orbits constructed" [D18 2018]. The **square** —
its `H¹`, its corner, its positivity — **did not move.** The wall is the same wall; it is now reached
by a paved road, and its single load-bearing brick is named: **`H¹` on the square (⟺ self-adjointness),
blocked at the two-variable lift of the char-1 Frobenius and the divergence-free diagonal.**
