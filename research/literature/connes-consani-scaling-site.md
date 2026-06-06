# The Connes–Consani Arithmetic Site / Scaling Site

*A precise characterization of the candidate for RH's missing object (the arithmetic analogue
of `C × C`), with the §8 discipline: theorem vs. program vs. analogy is flagged throughout.*

**Primary sources (read for this note).**
- Connes–Consani, *The Arithmetic Site*, C. R. Acad. Sci. Paris 352 (2014) 971–975 = arXiv:1405.4527 (the CRAS note; full text read).
- Connes–Consani, *Geometry of the Arithmetic Site*, arXiv:1502.05580 (the long paper; full text read).
- Connes–Consani, *The Scaling Site*, arXiv:1507.05818 (CRAS note; abstract read verbatim).
- Connes–Consani, *Geometry of the Scaling Site*, arXiv:1603.03191 (abstract read).
- Connes–Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771 (full text read; local PDF).
- Connes–Consani, *The Riemann–Roch strategy, Complex lift of the Scaling Site*, arXiv:1805.10501 (full text read).
- Connes, *An essay on the Riemann Hypothesis*, arXiv:1509.05576 (abstract read verbatim).

A quote in `"..."` is verbatim from the source; everything else is paraphrase. Equation/theorem
numbers cite the source paper.

---

## 0. One-paragraph summary

Connes–Consani build, by genuine theorems, a *characteristic-one / `F₁`* geometric object — the
**Arithmetic Site** `(\hat{N}^×, \overline{N})` and its extension of scalars the **Scaling Site** `S`
— whose **points over the tropical/max-plus semifield `R_+^max` recover exactly the part of the adèle
class space `Q^× \ A_Q / \hat{Z}^×` that carries the zeros of `ζ`** (theorem), and on which the
scaling flow `R_+^*` plays the role of Frobenius. On this object the **complete Riemann zeta
`ζ_Q(s)=π^{-s/2}Γ(s/2)ζ(s)` is the Hasse–Weil / Lefschetz counting zeta** of the Frobenius action
(theorem, as a `q→1` limit), and on the **periodic orbits `C_p` (one per prime, of length `log p`) a
Riemann–Roch theorem holds** with real-valued dimensions (theorem). The intended payoff is to
transpose **Weil's `C × C` proof of RH over function fields** (Mattuck–Tate–Grothendieck form): the
candidate for `C × C` is the **square of the Scaling Site `S²` (or its complex lift `Γ²`)**, on which
RH would follow from the *existence half* of a Riemann–Roch theorem applied to the divisor
`D(f) = ∫ f(λ)Ψ_λ d^*λ` built from Frobenius correspondences. **That Riemann–Roch theorem on the
square does not exist** — it is the explicit, stated open problem. The archimedean paper (2006.13771)
isolates *where* the positivity is hard at the single place `∞` and proves a conditional trace
inequality there. So: the **object is built and is a theorem; the forcing structure (intersection
positivity on the square) is a program, blocked at one precise step (`H¹` / Riemann–Roch on `S²`).**

This is the same endpoint the project's own map (`state-of-search.md` §5.1) reaches: the missing
arithmetic object. This note says exactly what is and is not there.

---

## 1. What the object IS

### 1.1 The Arithmetic Site (the topos and its structure semiring) — *theorem*

- **Topos.** `\hat{N}^×` is the topos of *sets with an action of the multiplicative monoid `N^× = (Z_{>0}, ×)`*,
  i.e. presheaves/`N^×`-sets on the one-object small category with morphism monoid `N^×`. Equivalently
  "the topos which is the dual of the multiplicative semigroup of positive integers" (Arithmetic Site
  abstract, verbatim).
- **Structure (semi)ring.** The structure sheaf is the **tropical semiring**
  `\overline{N} := (N ∪ {∞}, inf, +)` with `N = Z_{≥0}` (1405.4527, p.1, verbatim:
  `"the tropical semiring N̄ ∶= (N ∪ ∞, inf, +)"`), on which `N^×` acts by multiplication
  (`Frob_n : x ↦ nx`). In the long paper the equivalent additive normalization `Z_max = (Z ∪ {−∞}, max, +)`
  is used. So the arithmetic site is the **semiringed topos `(\hat{N}^×, Z_max)`** — a `char 1` / `F₁` object.
- **Points of the bare topos.** (1502.05580, Thm 2.1) the points of `\hat{N}^×` are *rank-one ordered
  groups* `H ⊂ Q` (equivalently `\hat{Z}^×`-orbits of finite adèles); the stalk of the structure sheaf
  at such a point is the semifield `H_max = (H ∪ {−∞}, max, +)` (Thm 3.2). The points over the Boolean
  semifield `B = ({0,1}, max, +)` recover `Q^×_{>0}` acting — the "rational" sub-skeleton.

### 1.2 Points over `R_+^max` = the adèle class space — *theorem (the key identification)*

> **Theorem** (1405.4527, Thm 2.6; 1502.05580, Thm 1.1, verbatim abstract):
> *"the set of points of the arithmetic site over the maximal compact subring of the tropical
> semifield is the non-commutative space quotient of the adele class space of `Q` by the action of
> the maximal compact subgroup of the idele class group"* — i.e. the points of `(\hat{N}^×, Z_max)`
> over `R_+^max` form `Q^× \ A_Q / \hat{Z}^×`.

The action of `R_+^*` (`= Aut(R_+^max)`, the automorphisms of the tropical semifield, written
`Fr_λ`, `λ ∈ R_+^*`) on these points **is the scaling/Frobenius flow** on the adèle class space —
the same flow whose spectral realization (Connes 1999) gives the zeros of `ζ`. This is the load-bearing
bridge: the abstract `F₁` topos *has, as its `R_+^max`-points, precisely Connes's adèle class space*,
and the topos automorphisms *are* the Frobenius.

### 1.3 The complete zeta as a counting/Lefschetz zeta — *theorem (as a `q→1` limit)*

Using the Connes trace formula `Tr_{distr}(∫ h(u) ϑ_u d^*u) = Σ_v ∫_{Q_v^*} h(u^{-1})/|1−u| d^*u`
(1405.4527 eq. (1)) on `\hat{Z}^×`-invariant test functions `h(u)=g(|u|)`, one extracts a **counting
distribution `N(u)`, `u ∈ [1,∞)`** for the Frobenius action on the `R_+^max`-points.

> **Theorem** (1405.4527, Thm 2.7; 1502.05580, Thm 4.2): the zeta function defined by
> `∂_s ζ_N(s)/ζ_N(s) = − ∫_1^∞ N(u) u^{-s} d^*u`
> **is the complete Riemann zeta `ζ_Q(s) = π^{-s/2} Γ(s/2) ζ(s)`**. This equation was shown in
> Connes–Consani *Schemes over `F₁`* (2010) to be the `q → 1` limit of the **Hasse–Weil** point-count
> formula over `F_q`.

So `ζ_Q` is realized as the Hasse–Weil/Lefschetz zeta of the Frobenius flow on this `F₁` object —
the structural analogue of `Z(C/F_q, T)` being the Lefschetz zeta of Frobenius on a curve. The
periodic orbits responsible for prime `p` are the points where the adèle component `a_p = 0`
(1502.05580, §4.1): geometrically the inverse image of `C_p` is *the mapping torus of multiplication
by Frobenius at `p`* (Scaling Site abstract).

### 1.4 The Scaling Site `S` (extension of scalars `B → R_+^max`) — *theorem*

> **Definition/Theorem** (Scaling Site abstract, verbatim): *"the semi-ringed topos obtained by
> extension of scalars from the arithmetic site … by replacing the smallest Boolean semifield by the
> tropical semifield of real numbers with the max-plus operations. The obtained site is the
> semi-direct product of the Euclidean half-line by the action of the monoid of positive integers by
> multiplication"* — i.e. the topos `[0,∞) ⋊ N^×`, structure sheaf `O =` **piecewise-affine convex
> functions with integer slopes** (the `char 1` structure sheaf). *"Its points … coincide with the
> quotient of the adele class space of `Q` by the action of the maximal compact subgroup of the idele
> class group"* and *"The structure sheaf … endows it with a natural structure of tropical curve over
> the arithmetic topos."*

So `S` is a **tropical curve** (`char 1`) whose `R_+^max`-points are again `Q^× \ A_Q / \hat{Z}^×`,
now with a genuine 1-dimensional geometry (the half-line direction is the "scale"). It is the smooth
geometric refinement of the arithmetic site, and the natural arena for divisors and Riemann–Roch.

### 1.5 The square `S²` as the candidate for `C × C`

The whole program is: **`C × C` (Weil's surface) ⟷ `S²`, the square of the Scaling Site** (or its
complex lift `Γ²`, §3.4). The diagonal `Δ ⊂ S²`, the graph of Frobenius, and divisors built from
Frobenius correspondences are to live on `S²` exactly as in Weil's proof. *This square is the
"missing object" the project's strategy names.* — Status: the square exists as a topos; its
**intersection theory and Riemann–Roch do not** (see §4).

---

## 2. The structures built on it

### 2.1 Frobenius correspondences `Ψ_λ` / `Fr_λ` and their composition — *theorem*

- For each `λ ∈ R_+^*` there is a **Frobenius correspondence `Ψ_λ`**, a sub-object of the square
  `\hat{N}^× × \hat{N}^×` (resp. `S²`), of *degree `λ`*. For rational `λ = n/m` it is `μ ∘ Fr_{n,m}`
  (`μ =` product/diagonal map); the construction extends to all real `λ > 0` (1405.4527, §3.2; the
  structure sheaf of the square involves **Newton polygons**).
- **Composition law** (1405.4527, Thm 4.3; 1502.05580, Thm 7.7, verbatim):
  for `λλ' ∉ Q`, `Ψ_λ ∘ Ψ_{λ'} = Ψ_{λλ'}`; same for `λ,λ'` rational; and when `λ,λ'` irrational with
  `λλ' ∈ Q`, `Ψ_λ ∘ Ψ_{λ'} = Ψ_{λλ'} ∘ Id = Id ∘ Ψ_{λλ'}` with `Id` the *tangential deformation of the
  identity*. (The subtlety in the `λλ'∈Q` case is the analogue of the self-intersection/diagonal
  subtlety; flagged by the authors as `"subtle"`.)

This `R_+^*`-semigroup of correspondences is the `char 1` analogue of the **powers of Frobenius**
`Fr^n` on `C × C`. It is canonical in `char 1` — and (see §4) *fails to lift canonically* to `char 0`.

### 2.2 Riemann–Roch on the periodic orbits `C_p` — *theorem*

> **Theorem** (Geometry of the Scaling Site, arXiv:1603.03191, abstract, verbatim): *"The restriction
> of this structure to the periodic orbits of the scaling flow gives, for each prime `p`, an analogue
> of an elliptic curve whose Jacobian is a cyclic group of order `p−1`. The Riemann–Roch formula holds
> and involves real valued dimensions and real degrees for divisors."*

Concretely (1805.10501 §3.1 calls it a `"type-II Riemann–Roch formula for the periodic orbits"`):
on `C_p` one has divisors with **real degree**, `dim H^0` is real-valued (defined via global sections),
`H^1` is *defined by turning Serre duality into a definition*, and a Riemann–Roch identity of the form
`dim H^0(D) − dim H^0(K−D) = deg(D) + (1 − g)` holds with real indices. A theory of **theta functions**
on `C_p` is developed (1805.10501 §1, abstract). **This is a genuine theorem** and is the strongest
piece of positive evidence for the strategy: it shows `char 1` geometry can support a real-valued
Riemann–Roch with the right shape.

### 2.3 Intersection theory of divisors / the `(Γ_Fr · Δ)` analogue — *program (formula written, theory missing)*

The intended dictionary (1805.10501 §3.1):

- RH is encoded (Meyer; eq. (12) of 1805.10501) as the **non-positivity of a quadratic form**:
  `RH ⟺ s(f,f) ≤ 0 for all real `f` on `R_+^*` with ∫ f d^*u = ∫ f du = 0`, where
  `s(f,g) := N(f ⋆ \tilde g)`, `⋆ =` convolution, and `N(h) := Σ Λ(n)h(n) + ∫_1^∞ (u²h(u)−h(1))/(u²−1) d^*u + c·h(1)`,
  `c = ½(log π + γ)` — i.e. `N` is the **Weil explicit-formula functional**.
- The form is to be realized as a **self-intersection on `S²`** (eq. (14), verbatim shape):
  `s(f,f) = D • D`, with `D := ∫ f(λ) Ψ_λ d^*λ` (a divisor = real combination of Frobenius
  correspondences), and the **intersection number** `D • D' := ⟨ D ⋆ \tilde D', Δ ⟩`, computed by
  bilinearity from the composition law (§2.1) and the counting distribution `N(u)`, `⟨·,Δ⟩` being the
  intersection with the diagonal. This is the verbatim transcription of Weil's `(Γ_{Fr^n} · Δ)`
  intersection numbers, with `N(u)` playing the role of the point-count.

So the *formula* for `(Γ_Fr · Δ)` is written down and is computable; what is missing is the
**Riemann–Roch theorem on the square** that turns a sign of `D • D` into the **effectivity of a
divisor** (the existence half) — see §4.

### 2.4 The Lefschetz/Weil trace formula as a trace — *theorem (the trace), program (as intersection)*

The Connes trace formula (§1.3) **is** the realized Lefschetz/Weil trace: the local terms
`Σ_v ∫_{Q_v^*} h(u^{-1})/|1−u| d^*u` are exactly the Riemann–Weil explicit-formula local distributions
`W_v`, and the periodic orbits `C_p` (length `log p`) supply the prime-`p` contributions. The
identification of `Σ_v W_v` with a *geometric trace on the adèle class space* is a theorem (Connes
1999; Connes–Consani). What is *not* yet a theorem is its re-expression as an **intersection number on
`S²`** with the divergent archimedean self-intersection of `Δ` correctly renormalized (1805.10501 §3.4,
step 2).

---

## 3. How Weil positivity is reduced to the archimedean place

The paper **arXiv:2006.13771** (local PDF) handles the *single archimedean place* `v = ∞` — the place
where the explicit formula has its principal-value singularity at `u = 1` and where the geometric
intersection picture is hardest. Its contribution is to connect the **operator-theoretic** (semilocal
trace formula) and **geometric** (Scaling Site square) approaches at `∞`.

### 3.1 Setup
- Weil/RH form used: `RH ⟺ Σ_v W_v(g ⋆ g^♯) ≤ 0` for `g ∈ C_c^∞(R_+^*)` vanishing on a finite set
  `F ⊃ {0,1}` (eq. (2)); for support in `(1/2,2)` only the place `∞` is involved (eq. (149)).
- `W_∞ := −W_R`, an "elusive" distribution; on test functions it is `W_∞(f) = −½ Tr(\hat f u^* đu)`
  (eq. (7)), with `u = u_∞` the unitary from Fourier⊕inversion, `đu` its quantized differential.
- **Geometric meaning** (the load-bearing picture, Figure 1): the trace `Tr(\hat f u^* đu)` splits
  over the first quadrant into the **small square `Δ = [0,1]²`** and the **big (infinite) square
  `Σ = (1,∞)²`**. The kernel weight `P(1/y) − P(x)` is `+1` on `Δ`, `−1` on `Σ`. The archimedean Weil
  distribution comes out as `τ(ρ) = (ρ^{1/2}/2)(1/(1+ρ) + 1/|1−ρ|)` (eq. (39)).
- **The obstruction is exactly the small square `Δ`** (paper's §2): the discrepancy between the Weil
  distribution and the "Sonin trace" is the **trace-remainder** `δ(ρ) = Tr((ϑ_m(ρ^{-1}) − P ϑ_m(ρ^{-1}) P) ½ (u^* đu)^g)`
  (Def. 2.1), an *explicit positive function* (eq. (49): `δ(ρ) = 2ρ^{1/2}(Si(2π(1+ρ))/(2π(1+ρ)) + Si(2π(ρ−1))/(2π(ρ−1)))`),
  with a **jump in its first derivative at `ρ = 1`** (eq. (50)). The jump is the analytic shadow of the
  diagonal self-intersection singularity.

### 3.2 The Sonin-space / prolate-spheroidal reduction
- `S` = orthogonal projection of `L²(R)_{ev}` onto **Sonin's space** = functions vanishing with their
  Fourier transform on `[−1,1]` (cutoff parameter `Λ = 1`). `ϑ(f) =` compressed scaling action.
  `Tr(ϑ(f) S)` is positive-definite by construction.
- **Theorem 1** (eq. (4), verbatim): for `g ∈ C_c^∞([2^{-1/2}, 2^{1/2}])` with `\hat g(i/2)=\hat g(0)=0`,
  `W_∞(g ⋆ g^*) ≥ Tr(ϑ(g) S ϑ(g)^*)`.
  This is the inequality the task names. **Theorem 3** (eq. (13)) makes it sharp:
  `Tr(ϑ(f) S) = W_∞(f) + ∫ f(ρ) ε(ρ) d^*ρ`, with `ε(ρ) = Σ_n λ(n)/√(1−λ(n)²) ⟨ξ_n | ϑ(ρ^{-1}) ξ_n⟩`
  expressed in **prolate-spheroidal** eigenfunctions (the `ξ_n` from the pair of projections `P_Λ, \hat P_Λ`).
- **Mechanism** ("moving `Δ` into `Σ`"): one uses the infinite positivity reservoir of the big square
  `Σ` to absorb the negative small-square contribution `Δ`, via the prolate decomposition of the
  infinite dihedral representation. The leftover `D ∘ Q` operator is `−2 Id + K` with `K` Hilbert–Schmidt
  (Theorem 3.6), so **positivity holds after imposing finitely many linear conditions** on test functions
  — proven by reducing `K` (for `I=[½,2]`) to a **Hermitian Toeplitz matrix** (`q → 1^+` discretization
  of `R_+^*` by `q^Z`) and lowering its top eigenvalue below 1 by one orthogonality condition (§6).

### 3.3 What this achieves and its scope
- **Theorem (archimedean Weil positivity, conditional):** `W_∞(g ⋆ g^*) ≥ 0` for smooth positive-definite
  `g` supported in `(1/2,2)` with `\hat g(±i/2)=0` (and the slightly stronger eq. (5) with a `−c|\hat g(0)|²`
  defect). Corollary 2 (eq. (6)) writes the Sonin trace as the zeros' contribution `Σ_s \hat g(s)\overline{\hat g(\bar s)}`
  plus an RH-irrelevant `c|\hat g(0)|²`. **This is a real theorem at the single place `∞`.**
- The abstract states the intent verbatim: *"All the ingredients and tools used above make sense in
  the general semi-local case, where Weil positivity implies RH."* The single-place result is offered
  as the simplest instance of a *semilocal* program over `{∞, 2, 3, …, p}`.
- The vanishing condition `\hat g(±i/2)=0` is interpreted (p.3) as the function-field
  *"key contribution of `H¹` in Lefschetz's trace formula"* — explicitly flagging that the hard
  cohomological object `H¹` is being *imposed by hand* here, not constructed.

---

## 4. EXACTLY what is missing / conjectural

The construction is, in the authors' own words, *blocked at one precise step*. Distinguishing theorem
from program:

**Theorems (done).**
1. The semiringed topos `(\hat{N}^×, Z_max)` and the Scaling Site `S` exist; their `R_+^max`-points are
   `Q^× \ A_Q / \hat{Z}^×` (Thm 2.6 / 1.1).
2. `ζ_Q` is the Hasse–Weil/Lefschetz counting zeta of the Frobenius flow, as a `q→1` limit (Thm 2.7 / 4.2).
3. Frobenius correspondences `Ψ_λ` exist with composition `Ψ_λ ∘ Ψ_{λ'} = Ψ_{λλ'}` (Thm 4.3 / 7.7).
4. Riemann–Roch (real-valued, "type II") **on the periodic orbits `C_p`**, with theta functions (1603.03191).
5. Conditional **archimedean** Weil positivity `W_∞(g⋆g^*) ≥ 0` on `(1/2,2)` (2006.13771, Thm 1/3, Cor 2).

**The gap (program / open).**

1. **No Riemann–Roch on the square `S²`.** This is the explicitly stated open problem (1805.10501 §1,
   verbatim): *"in the process to formulate a Riemann-Roch theorem on the square of the Scaling Site
   one faces a substantial difficulty. The problem, which is still open at this time, has to do with an
   appropriate definition of the sheaf cohomology … `H¹` (the definition of `H⁰` is straightforward and
   that of `H²` can be given by turning Serre duality into a definition)."* `H⁰` and `H²` are in hand;
   **`H¹` — the middle cohomology that carries the zeros, the analogue of Weil's `H¹(C)` — has no
   definition.** A `char 1` homological algebra (Ext-functors, resolution of the diagonal, a tropical
   Čech analogue) is *begun* (ref. [27]) but does not yet yield `H¹`.

2. **The existence/effectivity half is exactly what's missing.** The strategy (1805.10501 §3.1,
   verbatim): *"The key missing step is provided by the implementation of a Riemann-Roch formula whose
   topological side is `½ D•D` and to conclude from it that one can make the divisor
   `D := ∫ f(λ)Ψ_λ d^*λ` (or its opposite `−D`) effective."* In Weil's proof the **existence part of
   Riemann–Roch** (`deg` large `⟹ H⁰ ≠ 0 ⟹` effective) converts the assumed wrong-sign self-intersection
   `s(f,f) > 0` into a contradiction. On `S²` there is no Riemann–Roch to invoke, so the implication
   `s(f,f) > 0 ⟹` (effective divisor) `⟹` contradiction **cannot be run**. RH `⟺ s(f,f) ≤ 0` is the
   Meyer/Weil-explicit-formula equivalence — i.e. the criterion they reduce to is itself the
   *only-known-equivalent* Weil positivity (the dispersing endpoint of `state-of-search.md` §4); the
   `S²` Riemann–Roch is precisely the *forcing structure* that would break the equivalence, and it is
   absent.

3. **The diagonal self-intersection / divergence is unrenormalized.** The self-intersection `Δ • Δ` and
   the divergent `log Λ` cutoff term (coefficient of `f(1)`) have *no good definition* (1805.10501 §3.4,
   verbatim: *"the divergent term in `logΛ` … is due to the lack of good definition of self-intersection
   of the diagonal"*). A correct intersection theory must absorb this divergence into the right Euler
   characteristic — not done. The archimedean paper's derivative-jump of `δ(ρ)` at `ρ=1` (§3.1 above) is
   the same `Δ•Δ` singularity seen analytically; the paper *controls* it at `∞` via prolate/Toeplitz
   analysis but does **not** give it a geometric (intersection-number) meaning.

4. **The complex lift `Γ` loses the canonical Frobenius.** The RR-strategy paper's actual construction
   lifts `S` to a complex object `Γ` (moduli of elliptic curves with triangular structure, related to
   the `GL₂`-system) to access complex Riemann–Roch (Hirzebruch–RR / index theorem) and tropical
   descent. But (1805.10501 §7, conclusion, verbatim): *"one meets a fundamental difficulty tied up to
   the loss of the one parameter group of automorphisms of `R_max` in moving from characteristic 1 to
   characteristic zero. The difficulty arises in the construction of the proper lift of the
   correspondences `Ψ_λ` which are canonical in characteristic 1."* The five-step program (construct
   `Γ`; develop intersection theory killing the `logΛ` divergence; prove HRR on `Γ²` with topological
   side `½ c₁(E)²`; use `s(f,f)>0` for an `H⁰` existence result; tropical-descend to effectivity) has
   **step 3 unproven** and called *"the most problematic."*

5. **Archimedean positivity is one place, conditional, and imports `H¹` by hand.** 2006.13771 proves
   `W_∞ ≥ 0` only for support in `(1/2,2)` (no primes), only after **finitely many linear conditions**,
   and the vanishing condition `\hat g(±i/2)=0` *stands in for* the function-field `H¹` contribution
   rather than deriving it. The semilocal case `{∞,2,…,p}` — where *"Weil positivity implies RH"* — is
   asserted to use *"the same ingredients"* but **is not carried out**; it is a stated program, not a
   theorem.

**Net.** The object (`C × C` analogue = `S²` / `Γ²`) is **built and is a theorem at the level of the
topos, its points, its zeta, its Frobenius, and Riemann–Roch on the 1-dimensional periodic orbits.**
The **forcing structure** — intersection positivity on the *square*, i.e. a Riemann–Roch theorem on
`S²` with a defined `H¹` whose existence-half forces the wrong-sign assumption into a contradiction —
**does not exist.** It is blocked at the definition of `H¹` (sheaf cohomology in `char 1`) and at a
divergence-free intersection theory for the diagonal. This is exactly the project's named frontier
(`state-of-search.md` §5.1): the missing object's *geometry exists; its positivity does not*. Until
the `S²` Riemann–Roch is proven, the Connes–Consani framework reduces RH to **the same Weil-positivity
equivalence** it set out to make provable — a beautifully structured restatement, not yet a route with
reverse force.

---

## 5. Relation to this project's strategy (cross-reference)

- This is the **`C × C` endpoint** of `state-of-search.md` (§2 row "Weil positivity / explicit
  formula"; §5 frontier 1). The geometric/metric/Jensen routes all *land here* (their BGS §6.3
  positive-Green-form obstruction is the archimedean facet of exactly this intersection positivity).
- The archimedean paper's mechanism is **RH-neutral in isolation** by the project's own diagnosis: it
  is the *archimedean / functional-equation / `Γ_ℝ`* structure (the `δ(ρ)`, `θ'(t)`, Sonin/prolate
  apparatus is built from the Riemann–Siegel angular function `θ`), which `state-of-search.md` §4
  identifies as *shared with Davenport–Heilbronn ⇒ RH-neutral*. The RH content lives in the
  **Euler-product/prime side** — i.e. precisely in the *square* `S²` intersection numbers `⟨D⋆\tilde D, Δ⟩`
  weighted by `N(u)` (which contains `Σ Λ(n)h(n)`), the part with **no Riemann–Roch**.
- **Kill-test posture (informational, not run as code here):** Meyer's `RH ⟺ s(f,f) ≤ 0` is an
  explicit-formula equivalence (would *hold* for any zeta with the same `N`-functional shape unless the
  Euler-product term `Σ Λ(n)` is made load-bearing by a real `S²` Riemann–Roch). So the criterion as it
  stands is the **dispersing** Weil positivity; the *non-dispersing* content would be entirely in the
  unbuilt `S²` intersection-positivity theorem. The framework therefore does **not** currently supply a
  forcing structure that passes the §5 gates — it supplies the *object on which such a forcing structure
  would live.*

*No claim above is asserted as proven beyond what the cited theorem numbers support; every "missing"
item is quoted from the authors' own statements of the open problem.*
