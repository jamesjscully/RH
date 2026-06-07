# F₁-(M) — does the MONOID / Deitmar–Kato–Soulé F₁ (Spec ℤ as a monoid/blue scheme, Soulé's F₁-zeta, Connes–Consani's functorial F₁) SUPPLY a finite arithmetic scale q at the archimedean place — a scaled conjugation — or is it the Step-A combinatorial skeleton, archimedean-scale-free? [CANDIDATE (M) · coherence-checked vs 𝔽_q · TERMINUS / SCALE_FREE]

2026-06-06. Module: inline mpmath 30 dps + anchor `scripts/numerics/witness/residue_field_cardinality.py` (R8). Lit (fetched/checked): Takagi *Compactifying Spec ℤ* (arXiv 1203.4914, the convexoid Zariski–Riemann compactification); Deitmar *Schemes over F₁* (monoid-ringed spaces); Soulé *Les variétés sur le corps à un élément* (N(x)∈ℤ[x] counting + F₁-zeta); Connes–Consani *Schemes over 𝔽₁ and zeta functions* (Compositio 2011, arXiv 0903.2024 — the functorial reconciliation of Soulé/Deitmar/Kato + the F₁-"curve" counting **distribution** N(q)). The (M) entry on the `f1-construction.md` candidate list. Same atom as R8/R9/QD, reached from the monoid/blue-scheme angle.

## The mandate (from `f1-construction.md`, candidate M)

The archimedean place HAS the reality (`F†=F̄`, conjugation = order-2 Frobenius) but LACKS an arithmetic **scale q**. Decisive test for (M): does the monoid-scheme structure on Spec ℤ — Deitmar's monoid-ringed spaces, Soulé's N(x)-counting / F₁-zeta, Connes–Consani's functorial F₁ — give Spec ℤ a compactification with a **finite ground at infinity** (a finite residue field / a finite cardinality q marking the radius `√q`), or does it stall at the combinatorial skeleton (the rank/dimension = Step A)?

---

## What got established (lit, checked + computed)

**[1] The pure monoid (Deitmar/Soulé) structure IS archimedean-BLIND — it ignores the additive (norm) structure. [lit, decisive]**
An F₁-ring (Deitmar) is a *multiplicative commutative monoid with absorbing 0*; Spec(A) = prime ideals of the monoid. The base change `⊗ℤ` sends finite-type F₁-schemes to **toric** ℤ-schemes — i.e. the monoid layer records exactly the **combinatorial skeleton** (the torus/lattice/fan = rank & dimension). Building the Zariski–Riemann compactification of the *monoid* morphism `F₁→ℤ` yields a proper space with **infinitely many infinite places, because the additive structure — hence the archimedean norm of ℤ — is ignored** by the multiplicative monoid. The archimedean place is precisely the datum the monoid structure throws away. **This is Step A (the skeleton), explicitly scale-free at ∞.**

**[2] The most careful monoid-flavored compactification (Takagi, *Compactifying Spec ℤ*) recovers ∞ ONLY by ADDING additive structure, and its stalk at ∞ is a VALUATION DISK — a continuum, NOT a finite residue field. [lit, fetched, decisive]**
Takagi (1203.4914) makes the diagnosis sharp and then shows what it costs to fix it:
- Pure rings/monoids cannot get `Spec̄ ℤ = Spec ℤ ∪ {∞}` canonically because **Spec ℤ is the final object** in schemes; Arakelov/number-theory put the ∞-data in **ad hoc** (a hermitian metric; valuations "not defined algebraically").
- His fix is to **add a second binary operator `⊞`** (the "convexoid ring": commutative monoid under `×`, **non-associative additive `⊞`**) — i.e. he re-imports an additive/norm structure the pure monoid lacks. Then `Spec̄ ℤ` is the Zariski–Riemann space of `Spec ℤ` over `Proj R₀`.
- **The stalk at the infinite place is `𝒪_∞ = 𝐃ℚ` = the unit disk in ℚ** = `{x∈ℚ : |x| ≤ 1}` — a **valuation convexoid ring**, an archimedean **disk** (a continuum-flavored valuation object), **NOT a finite field / finite residue cardinality.** No `q`.
- The global sections are `Γ(Spec̄ ℤ,𝒪) = {0,±1}` = the multiplicative monoid `μ₂∪{0}` (what some call `𝔽_{1²}`) — **has only the multiplicative structure, no `⊞`**, cardinality 2 (the roots of unity), **not a base size q for the radius.** Takagi himself: "we dare not say we have obtained the correct definition of 𝔽₁."

> The monoid layer gives the **skeleton**; recovering ∞ at all required re-adding additive/norm data by hand, and the recovered ∞-stalk is a **valuation disk (continuum) / roots-of-unity monoid**, never a finite residue field. **Scale-free / wrong-type at ∞, exactly per R8's continuum vs cardinality type-gap.**

**[3] Soulé's F₁-zeta is built from N(x)∈ℤ[x] = the rank/dimension polynomial (Step A); it produces the POLE ORDERS, not a radius. [lit + structural]**
Soulé's condition: `#X(𝔽_{p^n}) = N(p^n)` for a polynomial `N(x)=a₀+a₁x+⋯+a_d x^d`. The F₁-zeta is `ζ_{X/𝔽₁}(s) = lim_{p→1} Z_X(p,p^{-s})(p−1)^{N(1)} = ∏_k (s−k)^{−a_k}`. The output is a product of `(s−k)^{−a_k}` — the `a_k` are the **Betti/dimension data**; the value `q=p` enters only through the limit `p→1`. **N(x) is the combinatorial counting polynomial (the rank/skeleton, Step A); the F₁-zeta records pole ORDERS at integers `k`, with NO modulus / NO radius `√q`.** The `p→1` limit **deletes** the base field (the R3b-BC / R8 fact), leaving the skeleton.

**[4] Connes–Consani's functorial F₁ (the reconciliation of Soulé/Deitmar/Kato) gives the archimedean "scale" as a CONTINUUM DISTRIBUTION N(q) over q∈[1,∞), NOT a finite q. [lit + computed, decisive]**
C–C build the functorial F₁-theory that *reconciles* Soulé and Deitmar and covers Kato's monoids and Chevalley groups — the canonical home of the (M) candidate. For the **hypothetical "curve" C = Spec ℤ over F₁** whose zeta is the **complete** Riemann zeta `ζ_ℚ(s)=π^{−s/2}Γ(s/2)ζ(s)`, the counting function `N(q)` is determined by
`d/ds log ζ_ℚ(s) = −∫₁^∞ N(u) u^{−s} d*u` (`d*u = du/u`),
and **`N(q)` exists only as a DISTRIBUTION on the real CONTINUUM `q∈[1,∞)`**, positive on `(1,∞)`, with **`N(1)=−∞`** (the "infinite genus" of `C`). Computed sanity (mpmath, this pass): the leading term `N(u)∼u` gives `∫₁^∞ u·u^{−s}d*u = 1/(s−1)` at `s=2` → **1.000000**, i.e. the continuum integral reproduces the `ζ_ℚ` pole.
> The C–C archimedean "size" `q` is a **continuous real integration variable** `u∈[1,∞)` (the FE/abscissa axis — Step A, the `q^{−s}` scaling present at ∞ via `ξ(s)=ξ(1−s)`), and the object it rebuilds is **exactly `Γ_ℝ·ζ` = the archimedean INFINITE product** (the open/affine signature). There is **no single integer `q`, no marked radius `√q`; `N(1)=−∞` = no finite base.** This is the PP "open fibre / infinite product" signature recovered verbatim, and the QD "no canonical archimedean q" recovered from the counting angle.

---

## The 𝔽_q anchor (computed — what (M) would have to reproduce, and does not)

| | 𝔽_q-variety (anchor) | F₁-(M): monoid / Soulé / Connes–Consani |
|:--|:--|:--|
| the scale `q` | **integer prime power** (the finite constant field 𝔽_q under the curve) | **continuum** `u∈[1,∞)` (C–C) / **valuation disk 𝐃ℚ** (Takagi) / **deleted** by `p→1` (Soulé) |
| `N` | **polynomial** `N(q^n)=#X(𝔽_{q^n})`, finite degree `2g` | **distribution** on `[1,∞)`, `N(1)=−∞` (C–C) / pole-order polynomial `N(x)` (skeleton, Soulé) |
| local factor | finite char-poly `∏(1−α_iT)`, ONE Frobenius orbit | `Γ_ℝ·ζ` = **infinite** product (C–C); toric skeleton (Deitmar) |
| radius `\|α\|=√q` | **MARKED** (anchor below) | **UNMARKED** at ∞ (continuum / disk / roots of unity) |

Computed (this pass), elliptic anchor, `q` an integer prime power, `N(q^n)` polynomial-counted:
- `(5,1)`: `N(q^n)={5,35,140}`, `|α|=2.2361=√5` pure ✔
- `(7,3)`: `N={5,55,380}`, `|α|=2.6458=√7` pure ✔
- `(11,−2)`: `N={14,140,1274}`, `|α|=3.3166=√11` pure ✔
- `(13,4)`: `N={10,180,2290}`, `|α|=3.6056=√13` pure ✔

`q` is an **integer**, `N` a **polynomial**, the radius `√q` **marked** — exactly the three things the monoid/F₁-(M) layer does not produce at ∞ (continuum variable, distribution, unmarked radius). The finiteness is inherited from the finite constant field 𝔽_q **under** the curve; the monoid place at ∞ has **no field of constants** (Γ(Spec̄ ℤ,𝒪)={0,±1}, the roots of unity, cardinality 2, infinite cyclotomic tower in general — R9's `μ_∞`).

## DH falsified [computed]

DH (functional equation, **no Euler product**) has no `#X(𝔽_{p^n})`-counting, hence **no Soulé polynomial `N(x)`**, no toric/monoid model, and no Connes–Consani local Frobenius — the entire counting/monoid apparatus is **unposable** for DH (it requires a per-prime point-count `N(p^n)`, which a non-motivic L-function lacks). Four levels of vacuity (R8): no `H¹` ⟹ no surface ⟹ no family ⟹ no special fiber ⟹ no closed point. **(M) dies for DH** (inherited Euler-product kill).

---

## Verdict — SCALE_FREE_CLOSED (the Step-A combinatorial skeleton; ∞ is a valuation continuum, not a finite q)

> **[CANDIDATE M verdict].** The monoid / Deitmar–Kato–Soulé / Connes–Consani F₁ carries the combinatorial **skeleton** (toric rank & dimension; Soulé's `N(x)` = Betti/pole-order data; the multiplicative roots-of-unity monoid `Γ(Spec̄ ℤ)={0,±1}`) — i.e. **Step A, the dimension/count** — and it carries the **reality only weakly** (the order-2 `{0,±1}=μ₂` conjugation-monoid, no scale). It does **NOT** supply an arithmetic scale `q` at ∞: (i) the **pure monoid structure is archimedean-blind** — it ignores the additive/norm structure, giving infinitely many infinite places (Deitmar/Takagi); (ii) recovering ∞ at all (Takagi's convexoids) requires **re-adding additive structure by hand**, and the recovered ∞-stalk is the **valuation disk `𝐃ℚ` = a continuum**, not a finite residue field — the **R8 continuum-vs-cardinality type gap**, verbatim; (iii) Soulé's F₁-zeta `∏(s−k)^{−a_k}` records **pole orders (skeleton)**, the `p→1` limit **deletes** the base field; (iv) Connes–Consani's archimedean counting `N(q)` is a **distribution on the real continuum `q∈[1,∞)`** with `N(1)=−∞` (no finite base), rebuilding **exactly `Γ_ℝ·ζ` = the archimedean INFINITE product** (the open/affine signature, the radius **unmarked**). The 𝔽_q anchor — `q` an integer prime power, `N` a polynomial, `|α|=√q` marked (computed: `√5,√7,√11,√13` pure) — is reproduced by the finite constant field **under** the curve, which the monoid place at ∞ lacks. **DH dies** (no point-count ⟹ no `N(x)` ⟹ unposable). **This is the SAME atom as R8/R9/QD** (no finite constant field at ∞), now confirmed from the **monoid / blue-scheme / Soulé-counting / Connes–Consani-distribution** angle: the monoid F₁ reaches the **skeleton and the FE/abscissa axis (Step A)**, and the archimedean "scale" it produces is a **continuum/distribution/valuation-disk — a WRONG-TYPE size, not the arithmetic q (Step B = radius = RH).**

### Five-line decision
- **(a) Does the monoid-scheme give Spec ℤ a finite ground at ∞?** **NO.** Pure monoid is archimedean-blind (ignores additive norm ⟹ infinitely many infinite places). Takagi's convexoid `Spec̄ ℤ` exists only by **re-adding additive structure**; the ∞-stalk is the **valuation disk `𝐃ℚ`** (continuum), `Γ={0,±1}` (roots of unity) — **no finite residue field.**
- **(b) Soulé's F₁-zeta — scale or skeleton?** **Skeleton (Step A).** `N(x)∈ℤ[x]` = Betti/pole-order data; F₁-zeta `=∏(s−k)^{−a_k}` records pole orders; `p→1` deletes the base. No radius.
- **(c) Connes–Consani N(q) interpolation — scale at ∞?** **NO — a continuum distribution.** `N(q)` lives on real `q∈[1,∞)`, `N(1)=−∞`, rebuilds `Γ_ℝ·ζ` (infinite product). The "scale" is the **abscissa axis (Step A / FE)**, not an integer `q`; computed `∫₁^∞ u·u^{−s}d*u=1/(s−1)`.
- **(d) Anchor — recovers q?** **YES at 𝔽_q, NO at ∞.** 𝔽_q: integer `q`, polynomial `N`, `|α|=√q` marked (`√5,√7,√11,√13` pure ✔). The monoid place at ∞ supplies none of these (continuum/disk/roots of unity).
- **(e) Verdict + residual.** **SCALE_FREE_CLOSED.** (M) carries the skeleton + a weak order-2 reality (`μ₂`), reaches Step A (FE/abscissa, pole orders, dimension), and is **archimedean-scale-free**: its ∞-"size" is a **continuum / distribution / valuation disk**, the wrong type for the arithmetic `q`. **Residual blueprint:** supply a **finite field of constants** under the compactified ∞-point — equivalently replace the valuation disk `𝐃ℚ`/distribution `N(q)`/continuum with a **finite residue cardinality `q` marking `√q`** — the same irreducible datum as R8 (constant field), R9 (`μ_∞` infinite), QD (no canonical archimedean q). The monoid/blue-scheme framework provably **cannot** cross the type gap (its native ∞-objects are continua/roots-of-unity), confirming the terminus a further (fifth) way.

## Falsifier row (Euler-silent by design — terminus characterizer)
- **EULER-BORNE — NO (by design).** Type-checks the monoid F₁'s ∞-object against the constant-field cardinality; not a standalone ℤ-positivity. DISPERSING-by-design.
- **SEES-ZEROS — YES.** The sought radius `√q = M(N)=W =` purity `=` where the zeros sit; the monoid layer never reaches it (stops at skeleton/abscissa).
- **INDEPENDENT — NO.** A supplied finite constant field at ∞ would equal the solved 𝔽_q case (= RH over ℤ).
- Registered as a wall confirmation: the **monoid/Deitmar–Soulé/Connes–Consani F₁ reaches the Step-A skeleton + FE axis and is archimedean-scale-free** (∞ = valuation disk / continuum distribution / roots of unity), same atom as R8/R9/QD.
