# The cohomological / dynamical candidate for RH's missing object

A precise characterization of the two programs that conjecture the "missing arithmetic object"
(`STRATEGY.md` §1, `state-of-search.md` §5.1) as a **cohomology + flow** (Deninger) and as a
**spectral realization on the adele class space** (Connes). Discipline per `STRATEGY.md` §8: every
claim below is tagged **[THM]** (proven), **[CONJ]** (conjectured / hypothesised), or **[ANALOGY]**
(formal correspondence, not even conjectured as an isomorphism). Sources are quoted; equation
numbers refer to the cited papers.

Primary sources (read in full from the originals, not summaries):
- **Deninger**, *Number theory and dynamical systems on foliated spaces*, arXiv:math/0204110 (2002) —
  the sequel to his ICM 1998 lecture *Some analogies between number theory and dynamical systems on
  foliated spaces* (Doc. Math. Extra Vol. ICM I (1998) 163–186). Cited below as **[D]**.
- **Connes**, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*,
  arXiv:math/9811068, Selecta Math. 5 (1999). Cited as **[C99]**.
- **Connes**, *An essay on the Riemann Hypothesis*, arXiv:1509.05576 (2015). Cited as **[Ce]**.
- **Connes–Consani**, *Weil positivity and Trace formula: the archimedean place*, arXiv:2006.13771
  (2020) [`research/papers/connes-consani-weil-positivity-archimedean.pdf`]. Cited as **[CC20]**.
- **Connes–Consani**, *The Weil proof and the geometry of the adeles class space*, arXiv:math/0703392.
  Cited as **[CC07]**.

---

## 0. What both programs are trying to manufacture

Over a function field `K = 𝔽_q(C)`, RH is a **theorem** (Weil 1948, Deligne 1974). The forcing
structure is: the zeros of `ζ_C` are eigenvalues of Frobenius `F*` on `ℓ`-adic `H¹(C̄,ℚ_ℓ)`; the
explicit formula **is** the Grothendieck–Lefschetz trace formula `N(q^r)=Σ_i(-1)^i Tr(F^{*r}|H^i)`;
and RH follows from **intersection positivity** (`D.D ≤ 0` for degree-0 divisors) on the surface
`X = C̄ ×_{𝔽̄_q} C̄`, via Riemann–Roch + the Hodge index theorem ([Ce] §2.3, eqs (7)–(12); [CC07]).

The number-field gap (`STRATEGY.md` §1): **`Spec ℤ` has no `C̄`, and `Spec ℤ ×_{𝔽₁} Spec ℤ` has no
construction.** Deninger and Connes each propose a *different* surrogate for the missing geometry:

- **Deninger** — a (conjectural) infinite-dimensional **cohomology with a flow**, modeled on the
  reduced leafwise cohomology of a **foliated dynamical system**. The Frobenius eigenvalue picture is
  transported literally: zeros = eigenvalues of the flow generator on `H¹`.
- **Connes** — a (partly proven) **spectral realization** on `L²` of the **adele class space**, where
  the zeros appear as an *absorption* spectrum and the explicit formula is literally a **trace
  formula**; RH ⇔ a **positivity** (Weil positivity of a quadratic form).

They are "deeply different" in Deninger's own words ([D] §1): Connes' phase space is "a
non-commutative quotient of the adèles" and "generalizes readily to automorphic `L`-functions ... but
not to motivic `L`-functions, it is exactly the opposite with our picture."

---

## 1. Deninger's conjectural objects

### 1.1 The sought object: a foliated dynamical system for `Spec ō_K`  **[ANALOGY → CONJ]**

The central wish ([D] §4, the table on p. 16, here transcribed verbatim in structure):

| number theory | dynamical system |
|---|---|
| `spec ō_K ∪ {𝔭 \| ∞}` | 3-dim dynamical system `(X, φ^t)` with a one-codim foliation `ℱ` satisfying Conj. 3.1 |
| finite place `𝔭` | closed orbit `γ = γ_𝔭` **not** contained in a leaf (transversal to `ℱ`) with length `l(γ_𝔭) = log N𝔭` and `ε_{γ_𝔭}(k)=1` for all `k≥1` |
| infinite place `𝔭` | **fixed point** `x_𝔭` with `κ_{x_𝔭}=κ_𝔭` and `ε_{x_𝔭}=1` |

> "In order to understand number theory more deeply in geometric terms it would be very desirable to
> find a system `(X, φ^t, ℱ)` which actually realizes this correspondence." ([D] p. 16)

**Status: [CONJ]/[ANALOGY].** No such `(X, φ^t, ℱ)` is known to exist for `Spec ℤ`. [D] §4 only
*matches the shape* of two distribution identities; §5 then argues the realizing space cannot even be
a manifold (it must be a **laminated space** / generalized solenoid, see §1.5 below).

### 1.2 The cohomology `H̄^•_ℱ(X)` and the flow generator `Θ`  **[THM as foliation theory; CONJ as arithmetic]**

For a `d`-dim foliation `ℱ` on a manifold `X`, the **reduced leafwise cohomology** is
`H̄^n_ℱ(X) = Ker d^n_ℱ / closure(Im d^{n-1}_ℱ)` (closure in the Fréchet topology) ([D] §2). Key facts,
all **[THM]** for actual Riemannian foliations:

- Even for dense leaves, `H̄¹_ℱ(X)` **can be infinite-dimensional** — exactly the desired feature
  (`state-of-search.md`: the missing object is asymptotic / not finitely accessible).
- A leafwise **Hodge theory** holds (Álvarez López–Kordyukov [AK1], [D] eq. (2)): for compact `X`,
  oriented Riemannian `ℱ`, bundle-like `g`, the harmonic projection `Ker Δ_ℱ ≅ H̄^n_ℱ(X)` is a
  topological isomorphism. This gives Poincaré duality, a scalar product, Künneth, and (in the Kähler
  case) a Hodge `(p,q)`-decomposition `H̄^n_ℱ(X)⊗ℂ = ⊕_{p+q=n} H^{pq}` ([D] eqs (3)–(8)).
- An `ℱ`-compatible flow `φ^t` induces `φ^{t*}` on each `H̄^n_ℱ(X)`, a strongly continuous group; its
  **infinitesimal generator** is `Θ: H̄^n_ℱ(X) → H̄^n_ℱ(X)`, `Θh = lim_{t→0} (1/t)(φ^{t*}h − h)`. `Θ`
  is an `ℝ`-linear **derivation**: `Θ(h₁∪h₂) = Θh₁∪h₂ + h₁∪Θh₂` ([D] eq. (1)).
- **[THM 3.4 of D]** (general Riemannian `ℱ`): `Θ` exists as a closed densely-defined operator; its
  spectrum lies in a vertical strip `−ω ≤ Re s ≤ ω`; **if `φ^{t*}` is orthogonal then `T = −iΘ` is
  self-adjoint** and `φ^{t*} = exp tΘ = exp itT`.

### 1.3 Zeros as eigenvalues of `Θ` on `H¹`; the functional-equation symmetry `Re ρ = ½`  **[THM in the model, CONJ for ζ]**

This is the literal Hilbert–Pólya realization, made a **theorem for the toy foliated model**:

> **[THM, Cor. 3.5 of D].** Let `X` be a compact 3-manifold foliated by surfaces with a dense leaf,
> `φ^t` a non-degenerate `ℱ`-compatible flow, transversal to `ℱ`, **conformal** on `Tℱ` with factor
> `e^{αt}`. Then `Θ` has **pure point spectrum** `Sp¹(Θ)` on `H̄¹_ℱ(X)`, **discrete in `ℝ`**, and the
> distribution identity (eq. (13))
>
> > `1 − Σ_{ρ∈Sp¹(Θ)} e^{tρ} + e^{tα} = χ_{Co}(ℱ,μ) δ₀ + Σ_γ l(γ) Σ_{k∈ℤ\0} ε_γ(k) δ_{kl(γ)}`
>
> holds, and — the forcing statement — **"All `ρ ∈ Sp¹(Θ) have Re ρ = α/2."**

The mechanism of `Re ρ = α/2`: conformality makes `e^{−(α/2)t}φ^{t*}` **orthogonal** on `H̄¹`, so
`T = −i(Θ − α/2)` is self-adjoint ([D] eq. (16) and proof of 3.5); `−(Θ − α/2)² = Δ¹|_{ker Δ¹_ℱ}`,
so `Θ − α/2` is `i·(self-adjoint)` ⇒ `Re Θ = α/2`. **This is exactly the function-field forcing
structure** (self-adjointness / Frobenius unitarity) realized in a leafwise-Hodge setting.

For this to be the *Riemann zeros* one needs `α = 1` (so the critical line is `Re ρ = ½`) — but
**[THM, D Remark after Cor 3.5]: the manifold setting forces `α = 0`** (the flow must be isometric).
Hence `Re ρ = 0`, **not** `½`. Matching the arithmetic *requires `α = 1`*, i.e. `φ^t` conformal with
`g(T_xφ^t v, T_xφ^t w) = e^{t} g(v,w)` ([D] eq. (22)) — **impossible on a manifold**; this is the
explicit obstruction that drives Deninger to laminated spaces (§1.5).

### 1.4 The regularized-determinant / `det_∞` reconstruction of completed `ζ`  **[CONJ]**

The completed zeta is **conjecturally** the alternating regularized determinant of `(s−Θ)/2π` (or
`(s·Id − Θ)`) over the graded cohomology. In the function-field/arithmetic-scheme heuristic Deninger
has long written (ICM 1998):

> `ζ̂_K(s) "=" ∏_{i=0}^{2} det_∞( (s − Θ) / 2π | H̄^i_ℱ )^{(-1)^{i+1}}`,

an infinite-dimensional **zeta-regularized determinant** `det_∞` of the flow generator. In [D] this
appears in distributional form: the Lefschetz trace identity (eqs (13)/(19)) is the **logarithmic
derivative** of such a determinant identity. The eigenvalue side `Σ_ρ e^{tρ}` on `H¹` (eq. (15),
`Tr(φ^{t*}|H̄¹_ℱ) = Σ_{ρ∈Sp¹(Θ)} e^{tρ}`) reproduces, place-by-place, the explicit-formula zero sum
(§3 below). **Status [CONJ]:** the `det_∞` formula is the organizing wish; it is a theorem only for
the toy foliated model, where the "ζ" is the model's own dynamical zeta, not Riemann's.

### 1.5 What kind of space — and why not a manifold  **[CONJ]**

[D] §5: the realizing `X` must be a **laminated space** (Sullivan generalized solenoid; locally
`ℝ^a ×` totally-disconnected, e.g. `𝕊¹_p = ℝ ×_ℤ ℤ_p = lim(ℝ/ℤ ←ᵖ ℝ/ℤ ←ᵖ …)`). Reasons:

1. Fixed points are **mandatory** (the archimedean place ↔ a fixed point), but Theorem 3.3 / Cor. 3.5
   (the only proven Lefschetz cases, Álvarez López–Kordyukov [AK2]) require the flow **transversal**,
   i.e. **fixed-point-free**. With fixed points, `Δ_ℱ` is "not transversally elliptic for the
   `ℝ`-action ... methods of transverse index theory do not apply directly" ([D] p. 11). The conjecture
   "is not known (except for dim X = 1) if `φ` has fixed points" ([D] Conj. 3.1, remark).
2. The arithmetic needs `α = 1` (conformal weight `e^t`), impossible on manifolds (§1.3); laminated
   spaces *can* carry such metrics ([D] §5.6, Remark 5.7.4: `|det(T_xφ^{kl(γ)}|T_xℱ)| = e^{kl(γ)}`).
3. The `k ≤ −1` (analytic-continuation) coefficients in the explicit formula are `N𝔭^k = e^{kl(γ)}`,
   matched only by the laminated working-hypothesis trace formula ([D] eq. (29) vs the manifold
   eq. (13), where they are merely `±1`).

**Even the laminated trace formula is a [CONJ] ("Working hypotheses" 5.6):** the existence of a
`𝒟'(ℝ*)`-valued trace of `φ^{t*}` on `H̄^•_{ℱℒ}(X)` realizing eq. (26) is assumed, proven only in
the special fixed-point-free sub-case (Thm 5.9). The full object with the archimedean fixed point and
`α=1` **does not exist as a constructed space.**

### 1.6 A genuine [THM] byproduct: the discriminant ↔ Connes-Euler-characteristic match

[D] §4 (eqs (20)–(21)): the leading explicit-formula term `−log|d_{K/ℚ}| δ₀` matches `χ_{Co}(ℱ,μ)δ₀`,
and **[THM, Fact 4.2]** `χ_{Co}(ℱ,μ) = −β₁(ℱ,μ) ≤ 0`, paralleling `−log|d_{K/ℚ}| ≤ 0`; moreover the
holomorphic Connes Euler characteristic equals the **Arakelov Euler characteristic**
`χ_{Ar}(O_{spec ō_K}) = −log√|d_{K/ℚ}|` ([D] eq. (21), via Connes' foliation Riemann–Roch). This is a
real structural match — but for the **archimedean / discriminant** term, which `state-of-search.md` §3
classifies as **RH-neutral** (shared with Davenport–Heilbronn). It is decoration, not the forcing
content.

---

## 2. Connes' spectral realization on the adele class space

### 2.1 The space and the action  **[construction: THM; that it "is" the right space: heuristic]**

> **[Def 3.1 of Ce].** The **adele class space** of a global field `K` is the quotient
> `X_K = 𝔸_K / K^×` of the adeles by **multiplicative** action of `K^×`.

The **idele class group** `C_K = GL₁(𝔸_K)/K^× = 𝔸_K^*/K^*` acts on `X_K`. The module
`Mod: C_K → ℝ_+^*` has compact-cocompact range; its kernel `C_{K,1}` is compact. **[THM]** (BC-system
origin, [C99]): the action of `K^×` (e.g. `ℚ^×`) on `𝔸_K`, preserving additive Haar measure, is
**ergodic**, giving a **type II_∞** von Neumann algebra on which the dual `C_K`-action **scales the
trace** — the precise analogue of the geodesic flow scaling the trace on the horocycle-foliation
type-II_∞ factor (Connes' motivation, [Ce] §3.3).

### 2.2 Zeros as an **absorption** spectrum  **[THM, with a caveat]**

Because `Mod` has cocompact range, Haar measure on the dual of `C_K` is **diffuse** — "a point is of
measure 0 ... no way one can see the absorption spectrum without introducing some smoothness," done
via a **Sobolev space** `L²_δ(C_K)`, `‖ξ‖² = ∫|ξ(x)|²ρ(x)d*x`, `ρ(x)=(1+log²|x|)^{δ/2}`, `δ>1`
([Ce] eq. (19); [C99]). On the codimension-2 subspace `𝒮(𝔸_K)₀ ⊂ 𝒮(𝔸_K)` (conditions `f(0)=0`,
`∫f dx=0`), with `‖f‖² = ∫_{C_K}|Σ_{q∈K^*}f(qx)|² ρ(x)|x| d*x` ([Ce] eq. (20)):

> The map `𝔈: L²_δ(X_K)₀ → L²_δ(C_K)` intertwines the idele-class representation `ϑ_a` with the
> regular representation; **"its spectrum in each sector gives the zeros of `L`-functions with
> Grössencharakter"** ([Ce] p. 12).

> **[THM, C99, Selecta 1999].** "We obtain a spectral interpretation of the critical zeros of the
> Riemann zeta function as an **absorption spectrum**, while eventual noncritical zeros appear as
> resonances." (abstract)

**Crucial caveat (the artificial weight):** because of the weight `ρ(x)` "needed to see this
absorption spectrum," the construction **only sees the zeros on the critical line, and `δ` artificially
cuts the multiplicities of the zeros" ([Ce] p. 13).** So the spectral realization, as a
Hilbert-space statement, does **not by itself prove RH**: off-line zeros would appear as resonances,
not as missing absorption lines, but the framework is **engineered around the critical line** rather
than forcing zeros onto it. This is the key honest limitation.

### 2.3 The trace formula = the Weil explicit formula  **[THM semilocally; CONJ globally]**

Retreating from "prove RH" to "interpret the explicit formula as a trace," one replaces the Hilbert
setup by a softer nuclear-space one. The **geometric side** is ([Ce] eq. (22)):

> `Tr_{distr}( ∫ h(w) ϑ(w) d*w ) = Σ_v ∫'_{K_v^*} h(w^{-1})/|1−w| d*w`.

The per-place term arises from the scaling operator `T = ϑ_{w^{-1}}`: `Tξ(x)=ξ(wx)=∫k(x,y)ξ(y)dy`
with kernel `k(x,y)=δ(wx−y)`, so
`Tr_{distr}(T) = ∫k(x,x)dx = ∫δ(wx−x)dx = 1/|w−1|` ([Ce] §3.3). Summing over places reproduces the
**Weil explicit formula** (Weil's adelic form, [Ce] eq. (4)):

> `ĥ(0) + ĥ(1) − Σ_{χ}Σ_{ρ∈Z_χ̃} ĥ(χ̃,ρ) = Σ_v ∫'_{K_v^*} h(w^{-1})/|1−w| d*w`.

- **[THM]: the local/semilocal trace formula.** [C99] proves the trace formula at one place / a finite
  set of places; [CC20] / [C99]'s semilocal framework provides "a canonical Hilbert space theoretic
  set-up where the local distributions `W_v` and their sum appear in their precise form" ([CC20] p. 2).
  The geometric-side = explicit-formula identity is a **theorem** as a (semi)local computation.
- **[CONJ]: the global trace formula.** [C99] reduces RH to **the validity of the (global) trace
  formula**; that global identity, with the correct handling of the principal values and the global
  spectral side, is **not proven**. "When working at the level of adeles one treats all places on the
  same footing and thus there is an overall minus sign in front of the spectral contribution. Thus the
  Riemann spectrum appears naturally as an absorption spectrum ... it is difficult to show that it is
  'real'." ([Ce] p. 13).

### 2.4 RH ⇔ Weil positivity of a quadratic form  **[THM as an equivalence; the positivity is CONJ = RH]**

> **[THM, Weil].** RH ⇔ `s(f,f) ≤ 0` for all real compactly-supported `f` on `ℝ_+^*` with
> `∫f(u)d*u = ∫f(u)du = 0`, where `s(f,g) = N(f ⋆ g̃)`, `g̃(u)=u^{-1}g(u^{-1})`, and `N` is the
> explicit-formula functional ([Ce] eqs (17)–(18); [CC20] eqs (1)–(2): `RH ⟺ Σ_v 𝒲_v(g∗ḡ^♯) ≤ 0`).

The forcing wish: realize `s(f,f)` (equivalently `Σ_v 𝒲_v`) as `‖·‖²`-positivity of an operator. [CC20]
achieves this **at the single archimedean place** ([CC20] Thm 1/Thm 3): the **Sonin/Sonine trace**
`Tr(ϑ(f)𝐒)` of the scaling action compressed onto Sonin's space (the orthogonal complement `𝐒` of
the range of phase-space cutoff projections at `Λ=1`) is **positive by construction**, and
`Tr(ϑ(f)𝐒) = W_∞(f) + ∫f(ρ)ε(ρ)d*ρ` differs from `−W_ℝ` by a **compact** operator (an
"infinitesimal in the sense of quantized calculus"). Hence the archimedean Weil inequality
`W_∞(g∗g^*) ≥ Tr(ϑ(f)𝐒ϑ(f)*) ≥ 0` is given an **operator-theoretic conceptual reason** ([CC20] eq.
(4)). This is **[THM] only at `∞` (and the simplest semilocal cases `{∞,2,...,p}`)** ([CC20] abstract:
"All the ingredients ... make sense in the general semilocal case, where Weil positivity implies RH").

**The global positivity — Weil positivity over *all* places simultaneously — is not proven, and is
equivalent to RH** (`STRATEGY.md` §1: "number fields: only known *equivalent* → dispersing";
`state-of-search.md` §2: "RH ⟺ it, but only known equivalent").

### 2.5 The geometric incarnation: `Â × Â` (the `C̄ × C̄` analogue)  **[ANALOGY; key pieces CONJ/missing]**

[Ce] §4 / [CC07] / Connes–Consani's **Scaling Site** `Â` is the proposed surrogate for `C̄`:

- The **arithmetic site** `𝒜 = (ℕ^×^, ℤ_max)` over `𝔹`; the **scaling site**
  `Â = ([0,∞)⋊ℕ^×, 𝒪)` over `ℝ_+^max`, "the algebraic geometric space obtained from the arithmetic
  site by extension of scalars from `𝔹` to `ℝ_+^max`" ([Ce] §4.3.2). It "inherits a natural structure
  of tropical curve."
- Periodic orbits of the scaling flow = the primes: for each `p`, a circle of length `log p` becomes
  the analogue `C_p = ℝ_+^*/p^ℤ` of an elliptic curve `ℂ^*/q^ℤ`; divisor degrees can be **any real
  number** ([Ce] §4.3.2). **[THM 4.3 of Ce]:** a tropical Riemann–Roch holds on `C_p`:
  `Dim_ℝ(H⁰(D)) − Dim_ℝ(H⁰(−D)) = deg(D)`.
- **[ANALOGY, Table 1 of Ce]:** `C̄ ×_{𝔽̄_q} C̄ ↔ Â × Â`; the Frobenius correspondence
  `D = Σ a_k Ψ^k ↔ D = ∫Ψ(λ)f(λ)d*λ`. The wish: `½ D.D = s(f,f)` (the Weil functional), so that the
  Riemann–Roch inequality `Dim_ℝ(H⁰(D)) + Dim_ℝ(H⁰(−D)) ≥ ½ D.D` would yield the key positivity (17)
  by the §2.3 Weil strategy.

> **[Ce], boxed remark §4.3.2 — the explicit gap, quoted verbatim]:** "At this point, what is missing
> is an **intersection theory and a Riemann–Roch theorem on the square of the arithmetic site.** ...
> So far the Riemann–Roch formula in tropical geometry is limited to curves and there is **no Serre
> duality or good cohomological version of `H^j` for `j≠0`**."

And ([Ce] §5): the arithmetic/scaling sites "are only the **semiclassical shadows** of a still
mysterious structure underlying the compactification of `Spec ℤ` that should give a cohomological
interpretation of the explicit formulas" — for which Connes proposes (only as a **[CONJ] research
direction**) Segal's `Γ`-rings / the sphere spectrum / **topological cyclic homology** as the
"absolute algebra"/Weil-cohomology candidate.

---

## 3. The Lefschetz-trace structure: how the explicit formula is read as a fixed-point formula

The shared template. The Riemann–Weil explicit formula, in either Deninger's or Connes' form, is

> `(zeros side)  Σ_ρ h(γ_ρ)  =  (archimedean term)  +  (prime/orbit term)`,

read as a **Lefschetz / Selberg trace formula** `Σ_i(−1)^i Tr(operator | H^i) = Σ_{fixed pts/orbits}`.

**Deninger's reading ([D] §3–4):** the LHS is the alternating sum of leafwise traces
`Σ_n(−1)^n Tr(φ^{t*}|H̄^n_ℱ)`, dominated by `H¹`:
`Tr(φ^{t*}|H̄¹_ℱ) = Σ_{ρ∈Sp¹(Θ)} e^{tρ}` ([D] eq. (15)) — **the zeros are the `H¹`-eigenvalues**, with
`H⁰,H²` contributing the `1` and `e^{tα}` poles. The RHS is `χ_{Co}δ₀` (archimedean / discriminant)
`+ Σ_γ l(γ)Σ_k ε_γ(k)δ_{kl(γ)}` (closed orbits ↔ primes, `l(γ)=log N𝔭`) `+ Σ_𝔭|∞ W_𝔭` (fixed point ↔
archimedean place). This is **literally** the dynamical Lefschetz fixed-point formula (Guillemin–
Sternberg / Álvarez López–Kordyukov). The match of [D] eq. (13) with the explicit formula eq. (19) is
term-by-term ([D] §4, eqs (17)–(22)).

**Connes' reading ([Ce] §3, [C99]):** the same explicit formula is `Tr_{distr}(∫h(w)ϑ(w)d*w)`, the
trace of the idele-class scaling action on `L²(X_K)`. Each place contributes a **fixed-point/isotropy
term** `∫'_{K_v^*} h(w^{-1})/|1−w| d*w`, computed exactly as a fixed-point contribution
`∫δ(wx−x)dx = 1/|w−1|` — i.e. the Lefschetz `1/|1−DF|` Jacobian factor at the fixed points of the
scaling map. Connes makes the Selberg-trace analogy explicit ([Ce] §3.1–3.2): Selberg's formula (16)
already has the zeros `ρ=½+iγ` and von-Mangoldt prime terms `−2Σ Λ(n)n^{-½}g(log n)`; the **"minus
sign"** (§3.2) is precisely why the Riemann spectrum is an **absorption** (subtracted) spectrum rather
than emission — the structural signature that the zeros live in `H¹` (odd cohomology, the `−1` in the
Lefschetz alternating sum).

**Where RH enters (both):** the trace formula by itself is **RH-neutral** — it holds whether or not
the zeros are on the line (it is an identity of distributions; cf. `STRATEGY.md`: the explicit-formula
family is *additive/dispersing*, holds for Davenport–Heilbronn). RH is the **extra positivity input**:
- Deninger: `Re ρ = α/2` requires `e^{−(α/2)t}φ^{t*}` **orthogonal** ⇒ `T=−iΘ` **self-adjoint** — a
  *positivity/unitarity* of the flow on `H¹`, true in the toy model, **unconstructed** for `ζ`.
- Connes: RH ⇔ **Weil positivity** `s(f,f) ≤ 0` / `Σ_v𝒲_v(g∗ḡ^♯) ≤ 0` — the positive-definiteness of
  the trace-formula quadratic form, proven **only at `∞` and semilocally** ([CC20]), **open globally**.

In the function-field [THM] case this missing input is **intersection positivity** `D.D ≤ 0` on
`C̄×C̄` (Hodge index). Deninger's self-adjointness and Connes' Weil positivity are the **two faces of
that same positivity** transported to a number-field object that does not exist.

---

## 4. The precise gap — what each program would need

### Deninger
1. **Construct the space.** A laminated / foliated dynamical system `(X, φ^t, ℱ)` (3-dimensional,
   one-codimensional `ℱ`) whose closed orbits are the primes (`l(γ_p)=log p`) and which has **fixed
   points** for the archimedean place(s), with conformal weight **`α = 1`** (so `Re ρ = ½`). **No such
   space is known to exist**; manifolds are provably excluded (forced `α=0`, no fixed points allowed by
   the proven Lefschetz theorems).
2. **Prove the Lefschetz trace formula *with fixed points*.** [D] Conj. 3.1 / Working Hypotheses 5.6
   are open exactly in the fixed-point case ("not known except dim X = 1"); `Δ_ℱ` fails to be
   transversally elliptic there, so transverse index theory (Connes–Moscovici) does not yet apply.
3. **Identify the cohomology with the actual zeros.** Even granting 1–2, one needs `H̄¹_ℱ(X)` to be the
   space whose `Θ`-spectrum is `{γ_ρ}` for *Riemann's* `ζ` (not a model dynamical zeta) — the
   `det_∞((s−Θ)/2π|H^•)= ζ̂` identification. This is the entire content, and it is **[CONJ]**.
4. The forcing step (`Re ρ=½`) reduces to **self-adjointness of `T=−iΘ` on `H¹`**, i.e. orthogonality
   of the (conformally-rescaled) flow — Deninger's Hilbert–Pólya operator. **Unconstructed.**

### Connes
1. **Promote the trace formula from semilocal to global.** The geometric-side = explicit-formula
   identity is a theorem locally/semilocally ([C99], [CC20]); the **global** trace formula (all places,
   correct principal values and global spectral side) — to which [C99] reduces RH — is **unproven**.
2. **Prove global Weil positivity.** `Σ_v 𝒲_v(g∗ḡ^♯) ≤ 0` for all admissible `g` is proven **only at
   `∞`** (the Sonin-space compression, [CC20]) and in simplest semilocal cases; the full positivity
   **is equivalent to RH** and is the open endpoint. (This is the **dispersing equivalence** flagged in
   `STRATEGY.md` §1 / `state-of-search.md` §2 — an `iff`, not yet a forcing structure, unless the
   operator-theoretic Sonin positivity can be globalized.)
3. **Build the missing geometry.** An **intersection theory + Riemann–Roch (with Serre duality and
   `H^{j≠0}`) on `Â × Â`** — Connes' own boxed statement of what is missing. Currently tropical
   Riemann–Roch exists only on curves `C_p`; the surface `Â×Â`, its diagonal self-intersection
   `½D.D = s(f,f)`, and the Hodge-index positivity are **not constructed**. The deeper "Weil
   cohomology over `𝔽₁`" (`Γ`-rings / sphere spectrum / topological cyclic homology) is a **[CONJ]
   program**, not a theory.

### The shared, irreducible gap (matches `state-of-search.md` §5.1)
Both programs **reduce RH to a positivity** (self-adjointness on `H¹` / Weil positivity on the trace
form) that, over function fields, **is** the proven intersection positivity on `C̄×C̄`. Over `Spec ℤ`:

> **The object that would make the positivity provable — the arithmetic surface / its `H¹` with a
> Frobenius-like flow — does not exist as a constructed object, and the positivity itself is unproven
> (and only known to be *equivalent* to RH).**

Deninger supplies a **candidate shape** for the cohomology+flow (reduced leafwise `H̄¹_ℱ` + generator
`Θ`), proven to have the right formal properties (Hodge duality, self-adjointness ⇒ critical line) in a
**toy foliated model** but with **no arithmetic realization** and an **obstruction** (manifolds give
`α=0`, no fixed points). Connes supplies a **partial realization** of the *spectrum* (absorption
spectrum on `L²(X_K)`, semilocal trace formula = explicit formula — both **[THM]**) but the global
**positivity** and the **`Â×Â` intersection theory** that would force it are **open / unconstructed**.

This is precisely the project's diagnosis: the RH content sits in the **subleading Euler-product /
intersection-positivity** structure; the archimedean / functional-equation pieces both programs handle
(Deninger's `χ_{Co}=χ_{Ar}` discriminant match; Connes–Consani's archimedean Sonin positivity) are the
**RH-neutral** parts (`state-of-search.md` §3–4). Neither program has, to date, produced the **forcing
structure** — a positivity provable on its own terms that forces the zeros onto the line — for
`Spec ℤ`. They have produced the most precise available **specification** of what that missing object
must be.
