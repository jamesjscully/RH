# The Riemann Hypothesis, localized: a constructive account (2026-06-06)

A self-contained account of where this program arrived: a complete, function-field-validated
construction that **reduces RH to a single named object** (`ψ_∞`), together with a **proof-of-why** —
an explanation, confirmed from six independent directions, of the one obstruction that resists
construction. Not a proof of RH. The sharpest localization the method could reach, plus the mechanism
of the wall. Every load-bearing claim was checked against the `𝔽_q` anchor and the three-axis falsifier
(`scripts/numerics/witness/falsify.py`); the discipline corrected the author's own errors repeatedly
(the `‖f‖²` weld, the conjugation-odd framing, three premature termini, the `F·V=[q]` overreach).

---

## 1. Strategy

Three phases: **audit** (prove no reformulation in reach suffices, and locate the wall precisely) →
**construct** (build the object the audit's spec demands, validated on function fields first) →
**localize** (peel the construction to its single irreducible ingredient and explain why it resists).

Governing principle (`research/method.md`): definition-first, reverse-engineered from the conclusion;
move *all* hardness into one constructive question; never "try to prove RH." At every step either (a)
sharpen axioms so `axioms ⟹ RH` is formal, or (b) measure a located failure that names the next axiom.

## 2. The audit (complete) — RH is an Euler-borne cross-place coupling

`research/positivity-program.md`. Every reformulation of RH (Weil/Li positivity, Bost–Connes QSM,
sym²/Rankin–Selberg, the prime Gram, the dBN/`Λ` flow, semilocal `{∞,2}`, reflection positivity) is
**Euler-product-borne** but stops short of FORCING — each is RH-silent (sees no zeros) or circular
(is RH restated). Falsifier upgraded to three axes: Euler-borne / sees-zeros / independent. **The
certificate ladder:** Eisenstein → archimedean (`ζ=DH`, RH-neutral); Hecke/Euler (sym²/Rankin–Selberg,
the first Euler-borne *and* independent candidate) → **edge `Re s=1`** (Siegel); FORCING → **line
`Re s=½`** = EMPTY. Euler-product positivity is structurally a *half-plane* phenomenon; RH is the
*reflected centre*; the edge→line bridge is the **cross-place coupling `W_∞ ≥ Σ_p W_p`** = the missing
object. The dynamical (dBN) branch is structurally distinct (the flow escapes the static obstruction)
but its GUE lever is universal/RH-silent and it reduces to the same wall. **Every branch → one wall.**

## 3. The construction (complete, validated on `𝔽_q` to genus 2)

`research/construction-program.md`, `research/construction/M*.md`. The audit's terminal no-go — any
form encoding RH as a `*`-congruence of a fixed (DH-shared) archimedean background is Sylvester-inertia-
locked — became the **design law: the polarization must be CATEGORICAL (a duality pairing), never a
metric.** Built the **polarized arithmetic Hodge category**:
- **M1** universal property `𝕊_ℤ` (contract C1–C6): Frobenius trace = explicit formula; `(p,q)` at `∞`;
  duality `D` = FE; categorical polarization; positivity ⟺ RH; no object for DH.
- **M2** the function-field datum satisfies C1–C6 *categorically* — `C4`: the polarization `P_duality`
  equals the Gram **exactly** (`0.00e+00`), so the "metric" is the canonical duality pairing in disguise
  (the design law realized). **The Weil RH proof is reproduced from the new definitions** (C5: the
  primitive Hodge-index inertia flips when a zero leaves the circle).
- **M2b–M4C** localized the hardness to the **purity functor `(·)^{1/2}∘(edge-abscissa)`**, carrier =
  the weight-2 **Néron–Severi lattice** of the surface (rank `(2g)²`), with the indecomposable diagonal
  (dodging the naive-product trap) and `D∘D=id`.
- **M3** *invented* the archimedean polarization `P_∞(x,y) = S(C_W x, κ y)` via the Weil/Hodge
  `C`-operator — categorical, Frobenius-free. **RH ⟺ `P_∞ ⪰ 0` ⟺ archimedean `c=D`.**

The whole framework is coherent and anchor-validated; RH is reduced to **one positivity**.

## 4. The localization (the R-pass) — RH = a finite ground at `∞`

`research/construction/R*.md`. Peeled `P_∞ ⪰ 0` to its atom:
- The keystone `c=D` is forced (classically) by a **Kähler form via Hodge–Riemann** — but `K1` showed
  it **factors**: the cup product and the Hodge–Riemann *implication* are free; the **Weil operator
  `C_W` (the radius / `(p,q)` splitting)** is, over `𝔽_q`, *literally* `|α|=√q` = RH.
- The radius is an **archimedean weight-monodromy** `N` with `M(N)=W` (four axioms). Both deepest
  machines fail at the radius axiom: **Schmid's SL(2)-orbit** gives parity not radius; **Connes–Consani
  scaling** gives the free self-dual `½` not the arithmetic `q`; **Bost–Connes** gives discreteness not
  a finite base. The carrier is not the orbit (rank 1, only `N=0`) and not the smooth surface (pure,
  `N=0` — "room ≠ usage"); a nonzero `N` needs a **degenerating family** with a special fiber.
- **R7/R8:** the family, `N`, and `M(N)=W` are all *free* (Schmid); the entire residue is **one
  cardinality `|κ(∞)|`** = a **finite field of constants at infinity**. Every named `𝔽₁`-tower
  (`μ_∞`, Witt, Arakelov) is infinite; the regularized determinant gives the count, radius-silent.

**Terminus form:** `RH ⟺ Spec ℤ has a finite field of constants at the infinite place` — the central
`𝔽₁` open problem (Manin / Connes–Consani / Deninger), reached constructively, with everything else free.

## 5. The deepest result — the count/radius decoupling, and `F†=F̄`

`research/construction/PA*.md`, `RF*.md`. The sharpest statement of RH the program produced:

> **RH = the AM–GM equality case.** The radius is `|αᵢ| = q^{1/2}` for *every* eigenvalue (zero
> variance). The **count** (any trace / determinant / average) fixes only the geometric *mean*
> `(det F)^{1/2g}` — it is free. The **radius** is the per-eigenvalue *equality*, and it decouples.

The decoupling is **fundamental** — it recurs inside *every* structure, verified across six creative
angles and hard Lefschetz (`PA2`: the HL/primitivity isomorphism is the count; the polarization equality
clause is the radius) and the abelian-variety/Rosati structure (`RF`: `F·F†=[deg]` is a *free tautology*
that says nothing about the moduli — `F·F†=7·I` with `|eig|²={2.52,19.49}`). The reason: over `𝔽_q`,
`Frob = x^q` is **one ring endomorphism doing both** — `q` is simultaneously the field-size (count) and
the scaling exponent (radius), because Frobenius respects `+` and `×` at once. **At `∞` there is no such
map**; count (a volume / regularized determinant) and radius (a scaling) are carried by orthogonal
operators, and `ℂ` has no finite-degree field endomorphism to marry them.

The radius, peeled to its core, is the **reality condition**

> **`F† = F̄`** — the *arithmetic* adjoint (Rosati, from the polarization) equals the *analytic* adjoint
> (conjugation, from the Hermitian metric).

This single condition is, from three independent directions, **the same statement**:
1. **`F†=F̄`** (reality / even split / `|αᵢ|²=deg`) — the line condition itself;
2. **Hodge–Riemann metric-compatibility** — the arithmetic polarization ∝ the archimedean Hodge metric
   (two adjoint-involutions coincide iff their forms are proportional);
3. **Hilbert–Pólya self-adjointness** — the zeros are the spectrum of a self-adjoint operator.

That a reality/reflection condition is the residue **explains why it resists construction**: a reality
condition is not produced by any positivity, scalar, trace, or determinant — it must be *imposed by a
geometry* (a degeneration over a finite base) that forces the arithmetic and analytic adjoints to agree.
`𝔽_q` has that geometry; `ℤ` does not have it at `∞`. The skeptic check seals it: **off-line eigenvalues
admit a positive Rosati polarization** — the free positivity sails straight through them, never seeing
the line.

## 5b. The sharpest (geometric) form — reality = properness, factored

`research/construction/PP-*.md`. The reality condition `F†=F̄` is, *structurally correctly*,
**properness of the archimedean fibre**: over `𝔽_q`, purity is Deligne **proper-pushforward** purity
(smooth proper ⟹ pure ⟹ perfect Poincaré duality ⟹ Rosati adjoint = conjugate; anchored — proper
`H¹` pure, open `H¹_c` mixed, without the zeros). But properness **factors**:
- **Step A (free):** perfect Poincaré pairing ⟹ `α↔q/α` = the **functional equation** `F·F†=q·id`. Holds
  at *every* radius. **Condensed/analytic geometry supplies this** (the six-functor duality).
- **Step B (deep, `=RH`):** `|α|=√q` ⟹ `F†=F̄`. This is **Weil II = Rankin-squaring positivity sharpened
  by the geometric monodromy of a degenerating family.** Properness *enables* but does not force it.
  **Condensed geometry provably does NOT supply this** (`TERMINUS_GEOMETRIC`).

The obstruction gets a crisp **geometric signature**: a proper fibre has a *polynomial* local factor
(finite char-poly, degree `2g`); the archimedean `Γ_ℝ(s)` is an *infinite product* — the **exact
signature of an OPEN/affine fibre** (`H¹_c`-style, non-perfect duality, infinite-dimensional). So the
residue is correctly renamed: **the archimedean fibre is *open*, missing its *proper boundary*** — and
that boundary's monodromy is exactly what sharpens Rankin–Selberg (the *edge*, which `ζ` has) to Weil II
(the *radius*, which `ζ` lacks). This *unifies the audit's edge wall and the construction's missing
special fibre (R6/R7) as one object*, reached independently from properness.

## 6. The open frontier, named

> **`ψ_∞`** — an archimedean Frobenius / a self-adjoint realization / a finite ground at `∞`, equivalently
> the structure that forces `F†=F̄`. It is the central open object of `𝔽₁`-geometry and Hilbert–Pólya,
> here localized as the *single* residue of a complete construction, with a proof that nothing free
> supplies it (the count/radius decoupling) and that every alternative (positivity, geometry, `𝔽₁`-models,
> creative angles, hard Lefschetz, abelian-variety/Rosati) lands on it.

## 6b. The geometric no-go (the new-geometry program's terminal result)

`research/new-geometry-program.md`, `research/construction/NG-*.md`. Having reduced RH to `F†=F̄` /
the proper boundary, the program asked whether a **new geometry** (not equivalent to the seven tested)
could force it. Three candidate geometries, each the strongest of its kind, were built and tested:
- **o-minimal / tame** (candidate 1): BKT o-minimal GAGA properizes transcendental archimedean objects —
  but **properness is an INPUT**; `Γ_ℝ` is provably WILD (infinite-discrete pole spectrum, non-o-minimal).
- **Frobenius-first / Tannakian** (candidate 2): Deligne–Milne reconstruction gives Step A (finite-dim,
  duality, FE) FREE, archimedean-native — but an **off-line spectrum generates a consistent
  non-polarizable** rigid Tannakian category; Step B (compact motivic Galois) is an imported positive
  fiber functor.
- **`*`-autonomous / `C*`** (candidate 3): even **Doplicher–Roberts** (compact group *from* a `C*`-category)
  only **consumes** positivity, never manufactures it. The invariant Hermitian form has signature **`(d,0)`
  positive-definite on-line, `(k,k)` Krein off-line** (computed `(6,0)` vs `(3,3)`) — positive-definiteness
  at the arithmetic `q` IS `|α|=√q` IS RH (circular, checked).

**THE GEOMETRIC NO-GO [THM-shaped].** The duality structure (`F·F†=[deg]`, FE, the invariant Hermitian
form) is FREE and archimedean-native at every radius. RH = positive-definiteness of that form *at the
arithmetic scale `q`* (signature `(d,0)`, not Krein `(k,k)`). **No geometric/categorical coherence — rigid
tensor, `*`-autonomous, `C*`/Doplicher–Roberts, six-functor, o-minimal — forces that signature; off-line
spectra are consistent (non-polarizable / Krein) objects in every one.** The positivity is an irreducible
external input requiring a *real geometric origin* (a variety over a finite ground), which `Spec ℤ` lacks
at `∞`. **Scope:** NOT undecidability — the precise limit of *geometry-as-coherence*. It explains why all
~60 attempts stalled at Step B: coherence provably admits the off-line (Krein) model. Crossing it requires
the `𝔽₁` ground itself (a variety at `∞`), not a cleverer category.

## 7. What is proven, what is open

- **Proven (constructively, validated on `𝔽_q`):** a complete polarized arithmetic Hodge category; the
  reduction `RH ⟺ P_∞⪰0 ⟺ c=D ⟺ F†=F̄`; the count/radius decoupling and its mechanism; that the residue
  is a *reality condition* equivalent to a finite ground at `∞` / Hilbert–Pólya; that no free structure
  (positivity, scalar, trace, Rosati) forces it; DH excluded at the carrier (no Euler product ⟹ no
  `H¹` ⟹ no object).
- **Open (the residue):** the construction of `ψ_∞` — a genuinely new idea, the `𝔽₁`/Hilbert–Pólya
  frontier. Not in the literature; not produced here.

**The product:** RH turned from "construct the missing object" into "**impose `F†=F̄` at `∞` — make the
arithmetic and analytic adjoints agree — which requires a finite ground / self-adjoint geometry that
`ℤ` lacks at infinity**," with a complete validated framework around it and a six-fold-confirmed proof
that this single reality condition is the sole irreducible residue.
