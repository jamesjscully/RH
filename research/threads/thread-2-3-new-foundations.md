# Threads 2 + 3 — new-foundations cohomology (condensed/analytic vs prismatic/q-de Rham) (2026-06-06)

Can the post-2018 "new foundations" — **condensed/analytic geometry** (Clausen–Scholze, thread 2)
or **prismatic / q-de Rham / Habiro** (Bhatt–Scholze, Bhatt–Lurie, Scholze, thread 3) — supply the
two missing pieces of `the-lift-program.md`:
(a) the **`H¹` on the square `\overline{Spec ℤ}²`** with a Serre duality `H¹×H¹→H²` and an RH-signed
self-intersection `Δ·Δ`; and/or (b) the **archimedean coherent duality / positive Green form `h_∞`**
on the canonical `Ω¹`?

Discipline per `STRATEGY.md` §8: **[THM]** proven (source named), **[PROG]** program/defined-but-
incomplete, **[CONJ]** conjectural, **[AN]** analogy. Quotes in `"…"` are verbatim. No fabrication —
where a source is silent I say so.

**Sources read directly for this note:**
- Clausen–Scholze, *Condensed Mathematics and Complex Geometry* (2024/25; arXiv **2605.11731**) and
  *Lectures on Analytic Geometry* / *Analytic Stacks* (2022–2024). Cited **[CS]**.
- **[Strasbourg]** = *Notes — Arakelov Geometry and Condensed Mathematics*, workshop Strasbourg
  19–23 May 2025 (le Bras et al.; full pdftotext read). The load-bearing source for thread 2: talks
  by **Wagner** (GAGA/duality, §7), **Dauser** (Betti stacks, §8; gaseous base stack & stack of
  norms, §10), **F. Charles** (A-schemes / formal-analytic surfaces / θ-invariants, §11–12).
- Bhatt–Scholze, *Prisms and Prismatic Cohomology* (Annals 2022, arXiv **1905.08229**). Cited **[BS]**.
- Bhatt–Lurie, *Absolute prismatic cohomology* (arXiv **2201.06120**); the Cartier–Witt stack. **[BL]**.
- Scholze, *The Habiro Ring of a Number Field* course (Bonn WS2024/25, full text read); Garoufalidis–
  Scholze–Wheeler–Zagier *Habiro ring of a number field*; Wagner *q-Hodge complexes over the Habiro
  ring* (arXiv **2510.04782**) and *q-Witt vectors and q-Hodge complexes* (arXiv **2410.23078**).
  Cited **[Hab]**.

---

## THREAD 2 — Condensed / analytic geometry (Clausen–Scholze)

### 2.1 What it actually has — the right archimedean coherent-duality machine [THM]

[CS] gives a *uniform* six-functor formalism for quasi-coherent sheaves on **analytic stacks** that
works identically over ℝ/ℂ and over the p-adics, and in it the coherent-duality theorems hold:

> **[THM, Strasbourg §7.20–7.22 (Wagner)]** For `f: X→Y` proper smooth of schemes, `f` is `!`-able
> with `f^! O_Y = ω_{X/Y}[d]`, and `R Hom_Y(f_* F, O_Y) = R Hom_X(F, ω_{X/Y}[d])`; over `Y=Spec(k)`,
> `H^i(X,F)^∨ ≅ Ext^{d-i}(F, ω_{X/Y})` — **Serre duality, in the analytic-stack 6-functor formalism.**

Crucially it **includes the archimedean place**, which the earlier *solid* theory could not:

> **[THM, Strasbourg §4.3]** "`The solid theory is not able to include archimedean objects: for
> example, we have R_{L◻}=0.`" The fix is the **gaseous** (a variant of liquid) analytic ring `R_gas`,
> for which `O(D)^† ⊗_{C_gas} O(D)^† ≃ O(D×D)^†` ([§4.26]) — i.e. the gaseous tensor product gives
> the **correct product of complex-analytic function rings**. This is exactly "descent that remembers
> norms" working over ℂ.

So thread 2's framework-level promise from `the-lift-program.md` §4 is **real and now demonstrated**:
condensed/analytic geometry is a genuine *archimedean coherent-duality machine* with a correct
`(−)×(−)` product. This is the strongest single update for thread 2.

### 2.2 The closest thing to a compactified `\overline{Spec ℤ}` including `∞`: the **stack of norms `N`** [THM/PROG]

The most directly relevant object is **the stack of norms `N`** and the **gaseous base stack `N/ℝ_{>0}`**
(Strasbourg §10, Dauser):

> **[THM, Strasbourg §10.16]** `N` surjects onto the **extended Berkovich spectrum** `M(ℤ)_ext`, which
> is `M(ℤ)` (the Berkovich spectrum of `ℤ`) "`obtained from M(ℤ) by adding the segment (1,∞], which
> corresponds to the powers |·|^α_∞ with α∈(1,∞) and a point corresponding to α=∞.`" The archimedean
> branch is the interval of `|·|^α_∞`, `α∈(0,1]` (`α>1` is the "dotted" part where the triangle
> inequality fails), **capped by a "`mysterious limit point`" at `α=∞`.**

This `M(ℤ)_ext` is, structurally, **a compactification of `Spec ℤ` that includes the archimedean place
as an actual point of an analytic stack** — the very object the program's "corner `∞`" wants to be a
point of. The archimedean fiber is built from `R_gas`:

> **[THM, §10.16 proof]** the locus `N(p)∈(1,∞)` is `AnSpec(R_gas)×(0,1)`; the non-archimedean
> ("trivial-on-archimedean") norm sits at `1/p ∈ AnSpec(R_gas)×(0,1)`; and there is "`an analytic ring
> together with a norm N such that N(p)=∞ for all p (quite mysterious)`" mapping to **the `α=∞` limit
> point** — i.e. the program's corner `∞×∞` corner-point has a candidate home, but the ring carrying it
> is explicitly flagged "mysterious / unclear" (the preimage of the limit point is "`quite unclear`").

**Verdict (2.2):** condensed/analytic geometry supplies, *for the first time*, a **single analytic
stack `N/ℝ_{>0}` over `M(ℤ)_ext`** in which the finite places, the archimedean place, and a literal
limit point at `∞` all coexist, with a working coherent 6-functor/duality formalism — the right *home*
for `\overline{Spec ℤ}` including `∞`. **The archimedean limit point itself is `[PROG]` (its ring is
"mysterious"), not yet pinned.**

### 2.3 Does it reach the SQUARE and `Δ·Δ`? — the **A-scheme / θ-invariant** facet [THM curve, PROG/CONJ square]

The part of [Strasbourg] aimed exactly at the program's `Δ·Δ`/positivity is **F. Charles' A-schemes**
(§11) — pairs `(X,K)`, `X/ℤ` finite type, `K⊂X(ℂ)` compact conjugation-invariant — and their
**θ-invariants** (the Bost/van-der-Geer–Schoof technology, §1.4 of `geometry-of-the-square.md`, now
restated inside the analytic-stack language):

> **[THM/def, Strasbourg §11.29–11.31]** `h⁰_θ(E)=log Σ_{v∈E} e^{−π‖v‖²}`, `h¹_θ(E)=h⁰_θ(E^∨)`,
> non-negative reals, with **Poisson/Serre duality** `h⁰_θ(E)−h¹_θ(E)=deg E`. Explicitly flagged
> **[§11.30]**: "`These numbers should be thought of as a dimension verifying the Serre duality, even
> though we have not defined any H⁰_θ or H¹_θ.`"

So **the H¹ is still virtual** here too — same integrality/real-valued-dimension wall as Bost
(`geometry-of-the-square.md` §1.4); condensed math has *not* yet produced an integer-dimensional
`H¹` (that is still only [RR-Z]'s char-1/𝕊 construction, on the curve). And on the **surface**, the
relevant object is named but **open**:

> **[PROG/CONJ — the two "Final questions", Strasbourg §12]** The closing open questions are precisely
> the program's targets. (1) **Archimedean Hodge degeneration**: for `X` complex, when does `X^an`
> have a model over `N/ℝ_{>0} ×_{M(ℤ)_ext/ℝ_{>0}} Z` (the archimedean branch), and "`is there a
> relation between this condition and X having a Kähler structure?`" — explicitly proposed as **"`an
> archimedean analog of Deligne–Illusie`"** (Hodge–de Rham degeneration over the archimedean point).
> (2) **Formal-analytic arithmetic surface**: for `V` an arithmetic surface and `p:Spec ℤ ↪ V` an
> integral point, how is the formal-analytic completion `(V^∧_p, K)` (`K` a compact Riemann surface)
> "`related to a closed neighbourhood of p in V×N/ℝ_{>0}`?"

These are *the surface and the archimedean Kähler/Hodge structure of the program* — posed as **open
questions inside the framework**, not theorems. The mod-Stein / ampleness dictionary does give a
genuine positivity on the curve side:

> **[THM, Strasbourg §11.20, §11.43]** a Hermitian line bundle `L` is **ample ⟺ `V(L)` is mod-Stein
> ⟺ `V(L)` is mod-affine** — an *analytic-stack characterization of arithmetic ampleness/positivity*.

### 2.4 Does thread 2 offer POSITIVITY, or only the cohomology skeleton?

**Mostly skeleton, with one genuine but RH-neutral positivity.** The 6-functor/Serre-duality
machinery (§2.1) and the norms stack (§2.2) are *duality/cohomology skeleton*. The *one real
positivity* is §2.3's **ample ⟺ mod-Stein/mod-affine** [THM] and the θ-invariant non-negativity
`h⁰_θ, h¹_θ ≥ 0` [THM]. But this is **the same θ/Arakelov positivity already audited** in
`geometry-of-the-square.md` §1.4 / §4.2: it is the *curve* arithmetic-ampleness positivity, it is
**real-valued (no integer `H¹`)**, and it does **not** see the Euler product. It therefore **fails the
kill-test in the wrong direction** — it is RH-neutral functional-equation/geometry-of-numbers data, not
an Euler-product-borne positivity that separates ζ from Davenport–Heilbronn. **No positive Green form
`h_∞` on the canonical with finite RH-signed `Δ·Δ` is constructed or even conjectured in [CS]/[Strasbourg]**
beyond the open Question §12.

### 2.5 Thread-2 gap and next step

- **Gap (square/`H¹`):** condensed math supplies the *coherent-duality skeleton* (§2.1) and the
  *right base `N/ℝ_{>0}` over `M(ℤ)_ext`* (§2.2), but the **`H¹`(square) over this base, with Serre
  duality `H¹×H¹→H²` on the surface, is not constructed** — it is exactly the open §12 question (2),
  and the θ-side `H¹_θ` "`has not been defined`" (§2.3). Same wall as the curve→square lift, now in
  analytic-stack clothes.
- **Gap (`h_∞`/positivity):** the archimedean `α=∞` limit point's ring is "mysterious" (§2.2); the
  archimedean Hodge/Kähler structure is the open §12 question (1) ("archimedean Deligne–Illusie"); no
  Euler-product-borne positivity appears. Even the available positivity (ample ⟺ mod-affine) is the
  RH-neutral θ-facet.
- **Most concrete next step (thread 2):** instantiate the program's object in [Strasbourg] §12's
  language and run the kill-test. Concretely: (i) take the arithmetic surface to be the *self-product*
  `\overline{Spec ℤ}²` (not a relative curve over ℤ), form `V×N/ℝ_{>0}`, and ask whether the diagonal
  `Δ:Spec ℤ ↪ \overline{Spec ℤ}²` extends to a section over `N/ℝ_{>0}` whose self-intersection at the
  `α=∞` limit point is the program's `−2δ'_1` corner term — i.e. **make §12 question (2)'s
  `(V^∧_p,K)`-neighbourhood the home of `Δ·Δ`**; (ii) check whether a *gaseous/liquid coherent duality*
  on that neighbourhood yields a **finite** regularized self-intersection and **with which sign**;
  (iii) kill-test it against DH/Epstein (same `Γ_ℝ` archimedean data). This is the first move that
  would convert "right framework" into "tested candidate," and it is now *formulable* because §10 (the
  norms stack) and §12 (the surface question) exist.

---

## THREAD 3 — Prismatic / q-de Rham / Habiro (Bhatt–Scholze, Bhatt–Lurie, Scholze)

### 3.1 What it is, and the structural reason it does NOT reach `∞` [THM]

Prismatic cohomology is built **from a prism `(A,I)`** — a `δ`-ring with a Cartier divisor `I`,
`p`-complete (`(p,I)`-adically) — and the prismatic site is attached to a **`p`-adic formal scheme**:

> **[THM, BS]** for a `p`-adic formal scheme, prismatic cohomology specializes to/refines the integral
> `p`-adic theories (crystalline, de Rham, étale, Hodge–Tate). **Absolute prismatic cohomology** [BL]
> recasts prismatic crystals on `Spf(ℤ_p)` as quasi-coherent sheaves on the **Cartier–Witt stack**
> `Σ = (ℤ_p)^{ΔΔ}` (a stack built from Witt vectors / `δ`-structure).

Every object here is **`p`-adic / `p`-complete by construction** (the `δ`-ring is a `p`-derivation; the
prism is `(p,I)`-complete; the Cartier–Witt stack lives over `Spf ℤ_p`). There is **no archimedean
prism and no archimedean fiber in [BS]/[BL]** — the framework has *no place `∞`* in it at all. This is
**[THM]-by-construction**, and it is the precise structural reason thread 3 is, as `positivity-program.md`
§A row 3 flags, a **"speculative bridge."** Prismatic cohomology is the deepest *unification of the
p-adic theories* and **says nothing, directly, about the archimedean place or about a square.**

### 3.2 The one place it gestures globally: `q`-de Rham → **Habiro** [THM construction, but range is `q=1`/roots of unity, not `∞`]

The only part of thread 3 that reaches *toward* a global/over-ℤ object is `q`-de Rham cohomology and
its conjectural home, the **Habiro ring** `H = lim_{n,m} ℤ[q^{±1}]/(1−q^n)^m`. Scholze's own framing
([Hab], course intro, verbatim):

> "`there is the q-deformation of de Rham cohomology … This only lives over ℤ[[q−1]], the completion
> over the first root of unity q=1, but … the specialization near p-power roots of unity seems to
> admit … meaning over ℤ; thus, I had long wondered whether the q-deformation of de Rham cohomology
> might in fact be defined over the Habiro ring.`"

> "`My hope was always that this q-deformation of de Rham cohomology should form a bridge between the
> period rings of p-adic Hodge theory and the period rings of complex Hodge theory.`"

And the recent theorem that realizes part of this bridge:

> **[THM, Hab — Wagner 2510.04782 / 2410.23078]** whenever the `q`-de Rham complex carries a
> "`q-Hodge filtration`", the associated **`q`-Hodge complex descends canonically to the Habiro ring
> `H`**; away from finitely many primes `q`-de Rham/`q`-Hodge cohomology is canonically defined over
> `H` (via Efimov's refined `TC^-` relative to `ku`).

So thread 3's most global object, **Habiro cohomology, is built and "`valid across all primes
simultaneously`"** — it is genuinely a *cohomology over (a completion of) `ℤ` unifying the p-adic
theories with a complex/`q→`root-of-unity asymptotic side*. But:

- its parameter range is **roots of unity / `q=1` (= `ℤ[[q−1]]`)**, i.e. the **multiplicative-group /
  cyclotomic** direction, **not the archimedean place `∞` of `Spec ℤ`.** The "complex Hodge theory"
  end Scholze hopes to bridge is the **twistor-`P¹` / Fargues–Fontaine** side (his words), **not the
  Arakelov archimedean metric `h_∞`**. The course explicitly disclaims understanding the relevant
  line bundles (the `K_3(K)→Pic(H_K)` "`regulator`" — "`I do not understand the meaning of those line
  bundles`").
- it is **`q`-DE RHAM**, i.e. it deforms `H^*_{dR}`; it is **not a sheaf cohomology of `\overline{Spec ℤ}²`**
  and has **no `H¹`-on-the-square, no Serre duality on a surface, no `Δ·Δ`.**

### 3.3 Does thread 3 offer POSITIVITY? — No.

Searched (BS, BL, Hab, q-Hodge): **there is no positivity statement** — no positive Green form, no
intersection positivity, no Weil-positivity analog — anywhere in the prismatic/q-de Rham/Habiro
literature. The theory is a **cohomology/coefficient skeleton** (it unifies *which cohomology*, not a
*sign*). It carries a rich Frobenius/`δ`-structure and a Hodge–Tate/Hodge filtration, but **no inner
product whose positivity is at issue.** Confirmed silent on Serre duality over `∞` and on the
compactified `Spec ℤ` (Wagner 2510.04782 abstract: no archimedean place, no `q=1` Serre duality, no
compactification statement).

### 3.4 Thread-3 gap and next step

- **Gap:** an **archimedean / global prism does not exist** (and is not even conjectured concretely):
  the prism is `p`-complete by definition, so there is no `(A,I)` at `∞`. The Habiro/`q`-de Rham bridge
  reaches a *complex/twistor* end via roots of unity, **not the Arakelov `∞`**, and supplies **no `H¹`
  on a square and no positivity.** Thread 3 is, honestly, **a cohomology-coefficient unification of the
  finite places** that the program would need to (a) acquire an archimedean term and (b) acquire a sign
  — neither of which it has or claims.
- **Most concrete next step (thread 3):** the only checkable bridge is the **`q=1` ↔ archimedean**
  speculation. Concretely: take the canonical `Ω¹` of `\overline{Spec ℤ}` and ask whether its
  *`q`-deformation* (the `q`-Hodge complex of [Hab]) has a **specialization at `q=1` over `ℝ` that
  carries the corner metric `−1/(2|u|)`** — i.e. whether the program's conformal corner weight is the
  `q→1` limit of a `q`-Hodge filtration. This is a long shot, but it is the single concrete contact
  point: it would test whether "`q=1` completion" and "archimedean place `∞`" are the same point (the
  program's bet that `∞` is a scale-invariant `q→1`-type corner). If `q=1` is provably the *cyclotomic*
  point and not `∞` (likely), thread 3 is confirmed orthogonal to `h_∞` and can be **shelved as a
  finite-place coefficient theory**, redirecting effort to thread 2.

---

## Bottom line

**Condensed verdict (thread 2):** condensed/analytic geometry is the **right framework and is now
partly built toward the target.** It supplies (i) an archimedean coherent **Serre/duality 6-functor
formalism** [THM, §2.1], (ii) a **single analytic stack `N/ℝ_{>0}` over the extended Berkovich
spectrum `M(ℤ)_ext`** that *includes the archimedean place and a limit point at `∞`* [THM, §2.2], and
(iii) an explicit A-scheme/θ-invariant + **open "Final questions"** that *are literally the program's
surface and archimedean-Hodge problems* [PROG/CONJ, §2.3/§12]. But the **`H¹` on the square is not
constructed** (still virtual, same as Bost), the **archimedean `∞` point's ring is "mysterious,"** and
the **only positivity present is the RH-neutral θ/ampleness facet** — no `h_∞`, no Euler-product-borne
sign.

**Prismatic verdict (thread 3):** prismatic/q-de Rham is **structurally `p`-complete — it has no
archimedean place, no square, no `H¹(S²)`, and no positivity.** Its most global avatar, **Habiro
cohomology**, is a real [THM] *unification of the finite (p-adic) places* whose "complex" end is the
**twistor/`q=1`-root-of-unity** side, **not the Arakelov `∞`**. It supplies *coefficients/skeleton for
the finite places only* and **offers no `h_∞` and no sign.**

**Which is closer to `H¹(S²)`/`h_∞`: THREAD 2 (condensed), decisively.** Thread 2 already names and
partially builds the exact objects — the compactified-`Spec ℤ` base `N/ℝ_{>0}`, archimedean coherent
duality, and the surface/Hodge questions — and the gap is "construct `H¹` + the positive `h_∞` *in this
framework*." Thread 3 is **orthogonal to the archimedean place**: closer to a *coefficient theory for
the finite primes* than to the corner, and would first have to *invent an archimedean prism* (which
does not exist) before it could even be aimed at `h_∞`.

**Next step, each:**
- **Thread 2 (do this):** instantiate `\overline{Spec ℤ}²` as an analytic stack over `N/ℝ_{>0}`,
  realize the diagonal `Δ` as a section, and test whether its self-intersection at the `α=∞` limit
  point of `M(ℤ)_ext` is finite, RH-signed, and **fails for DH/Epstein** — turning [Strasbourg] §12's
  open surface question into the program's kill-tested candidate for `Δ·Δ`/`h_∞`.
- **Thread 3 (cheap to settle):** test the `q=1 ↔ ∞` identification — is the corner weight `−1/(2|u|)`
  the `q→1` limit of a `q`-Hodge filtration on `Ω¹`? Most likely `q=1` is the *cyclotomic* point, not
  `∞`; if so, shelve thread 3 as a finite-place coefficient theory and concentrate on thread 2.
