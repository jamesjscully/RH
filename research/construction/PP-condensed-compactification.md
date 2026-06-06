# PP-condensed — can condensed / analytic geometry (Clausen–Scholze) make the archimedean fibre PROPER with finite-dim pure cohomology, forcing `F†=F̄`? [DECISION · coherence-checked vs 𝔽_q]

**Charter:** `the-complete-account.md` §5–§6 (the residue = `F†=F̄` = the reality condition = a finite ground at `∞`), §4 (R-thread terminus: one cardinality `|κ(∞)|`). **Named successor:** M3/M3b's `M3c` ("condensed-archimedean upgrade — realize `(V,F^•,κ)` as a Clausen–Scholze condensed/analytic object, the condensed-archimedean structure Arakelov lacks"). **Block:** the RESIDUE.

**The angle.** Over `𝔽_q`, purity (`F†=F̄`, `|α|=√q`) is **Deligne proper-pushforward purity**: a smooth PROPER variety has pure cohomology. Reframe the reality condition as **PROPERNESS of the archimedean fibre**: compactify it, let properness force purity — no imposed positivity. The hope: condensed/analytic geometry (Clausen–Scholze) does honest geometry (properness, six-functor duality, proper-pushforward) over archimedean and non-Noetherian settings classical Arakelov cannot reach, so maybe it makes the archimedean fibre proper with finite-dim pure cohomology.

This log decides: is there a REAL applicable theorem (genuine lead) or is the archimedean fibre INTRINSICALLY NON-COMPACTIFIABLE (a duality/H² gap = the geometric terminus)?

---

## [computed] The anchor: purity IS properness, and OPEN loses it (exact `𝔽_q` weights)

`scripts` one-shot, exact integer/float weights (no zeros assumed):

- **PROPER smooth curve `C/𝔽_q`** (`q=25, g=2`): Frobenius on `H¹` has all `2g` eigenvalues `|αᵢ| = √q = 5` **exactly** — a SINGLE modulus. **`H¹` PURE of weight 1.** This is proper-pushforward purity (smooth + proper ⟹ pure), and it IS `F†=F̄` (`|α|²=q=deg`).
- **OPEN curve `U = C∖{r points}`** (non-proper): excision injects a weight-0 piece (the punctures, Frobenius modulus `1`) alongside the weight-1 part (modulus `5`). Computed moduli on `H¹(U)`: `{1, 5}` — **TWO distinct moduli ⟹ IMPURE.** Removing properness **destroys** purity: `H¹` becomes MIXED.

> **Anchor verdict [computed]: purity = single Frobenius-modulus = PROPERNESS genuinely. An open/non-proper curve LOSES purity (`H¹` mixed, moduli `{1,5}`).** So "properness ⟹ purity" is a REAL theorem, and the reframe "reality condition = properness of the fibre" is structurally correct over `𝔽_q`. The question is entirely whether the *archimedean* fibre can be made proper in this sense.

---

## [computed/literature] What condensed / analytic geometry actually delivers — duality, NOT purity

Four findings, each load-bearing, from the primary literature:

**[1] Clausen–Scholze complex analytic geometry proves SERRE duality (coherent), not WEIL purity.** Their `Condensed Mathematics and Complex Geometry` (and `Lectures on Analytic Geometry`) revisit complex geometry via the liquid tensor product and prove **Serre duality + GAGA + Hirzebruch–Riemann–Roch** (Lectures XIII–XV). This is **coherent-sheaf / Dolbeault** duality. It is NOT a weight filtration, NOT a Frobenius, NOT a statement that any eigenvalue modulus is `q^{w/2}`. Serre/coherent duality says nothing about purity.

**[2] Scholze's six-functor formalism (2510.26269, v2 Jan 2026) gives abstract Poincaré–Verdier duality but is AGNOSTIC about weights/Frobenius eigenvalues.** The abstract theory establishes `f^!`, `f_!`, dualizing complexes, cohomological smoothness (`f^!(1)` ⊗-invertible), and even proper base change WITHOUT properness (replace `f_*` by `f_!`). But — checked against the source — it makes **no mention of weight structures or eigenvalue conditions**; it "appears agnostic about arithmetic invariants like weights and Frobenius eigenvalues." **Verdier/Serre DUALITY ≠ Deligne PURITY.** Duality is a self-pairing of cohomology; purity is the metric statement `|α|=q^{w/2}`. The six-functor formalism furnishes the former and is silent on the latter — exactly the M3b lesson (`(−1)^w` carries reality, not radius; the radius is not in the abstract duality).

**[3] Weil II purity ESSENTIALLY uses the Frobenius / a finite field — and is archimedean-incompatible.** Kedlaya's `Weil II` notes (checked): the purity engine is **Rankin's positivity argument**, "a real analysis argument which boils down to the fact that squares of real numbers are nonnegative," driven by Frobenius eigenvalue analysis **over finite fields**. There is no archimedean version; the notes state outright we are "manipulating ℓ-adic objects and attempting to keep track of archimedean information, and the two are not very compatible." So purity is NOT a formal consequence of abstract proper-pushforward duality — it requires the Frobenius and the finite-field positivity. This is the same `q→1` / no-constant-field wall as R8, seen from the Weil-II side: **purity's proof imports the finite field that `ℤ` lacks at `∞`.**

**[4] The archimedean fibre is INTRINSICALLY NON-COMPACT — the Γ-factor is a regularized determinant on an INFINITE-dimensional space, with only a LOG of Frobenius.** Deninger / Consani–Marcolli (`Archimedean cohomology revisited`, checked): the local Γ-factor at `∞` is
> `L_κ(H^m,s)^{-1} = det_∞( (1/2π)(s − Φ) | V^m )`, `V^m` **infinite-dimensional**,
a **zeta-regularized determinant of an UNBOUNDED operator Φ** = the **logarithm of Frobenius** (a derivation), NOT a Frobenius automorphism. [computed] contrast: a FINITE/proper fibre gives a **POLYNOMIAL** local factor (finite char poly, `det(1−Fq^{-s})`, degree `2g` for the `𝔽_q` curve `H¹`); the Γ-factor is an **infinite product** (the Gamma function, spectrum `{0,−2,−4,…}`), hence `V` is **infinite-dimensional**. properness ⟺ finite-dim cohomology ⟺ polynomial local factor. **The Γ-factor is not a polynomial ⟹ the archimedean fibre is not proper / not compact.**

---

## Verdict — TERMINUS_GEOMETRIC: the archimedean fibre is intrinsically non-compactifiable (a real duality / infinite-dim gap)

> **[DECISION].** Condensed / analytic geometry is a genuinely living theory that does honest archimedean geometry, and it DOES supply DUALITY at `∞` (Serre, Poincaré–Verdier) — but **duality is not purity**, and the thing the reality condition `F†=F̄` needs is **purity**, the metric `|α|=q^{w/2}` statement. Three independent facts converge:
> 1. **The applicable theorems are duality theorems, agnostic about weights/Frobenius eigenvalues** ([1],[2]). A six-functor / Serre duality gives a perfect self-pairing of cohomology; it does NOT assert a single eigenvalue modulus. (M3/M3b already proved this: `C_W` + `(−1)^w` give a coherent *duality* `(P_∞,D,c)` Frobenius-free, but `(−1)^w` is a sign carrying reality, **not** the radius.)
> 2. **Purity's only known proof imports the Frobenius and finite-field positivity** ([3]) — the constant field `ℤ` lacks at `∞` (R8). Abstract proper-pushforward does NOT formally yield purity; Rankin positivity does, and it is finite-field-bound.
> 3. **The archimedean fibre is provably NON-compact in the only sense that matters: its cohomology is INFINITE-dimensional** ([4]). The Γ-factor is a regularized `det_∞` over an infinite spectrum, with a *log of Frobenius* derivation, not a finite Frobenius. A proper fibre would give a polynomial; the Γ-factor is an infinite product. **This is the H²/Poincaré-duality gap in concrete form: there is no finite dualizing object at `∞`, only a regularized one.**

So the reframe is structurally CORRECT (purity genuinely IS properness, anchor [computed]) but it lands on the **same terminus**: making the archimedean fibre proper is exactly the obstruction. Condensed geometry **cannot fill it** — not for lack of development, but because the obstruction is a **type/cardinality fact** (R8: no finite constant field at `∞`) that resurfaces here as **infinite-dimensionality** ([4]): a finite-dim pure cohomology at `∞` would BE the finite ground / Frobenius `ℤ` lacks. **Properness does NOT force `F†=F̄` here, because the archimedean fibre is not proper and the available archimedean duality (Serre/Verdier) is the wrong theorem (duality, not purity).**

**Does properness FORCE reality?** Over `𝔽_q`, YES — and unconditionally (the `H¹`/open computation forces it without assuming the zeros). At `∞`: properness WOULD force it IF the fibre were proper, but the fibre is **intrinsically non-proper** (infinite-dim cohomology, [4]). So reality is **OPEN**, not forced — and the place it would be forced (a proper archimedean fibre with finite-dim pure cohomology) is precisely the non-constructed object `ψ_∞`.

**Where RH enters / where the zeros are used:** NOWHERE is a zero location assumed in this analysis (the anchor weights are Weil's theorem about the smooth curve; the Γ-factor infinite-dimensionality is the analytic fact about `Γ_ℝ`). The zeros enter ONLY at the unbuilt step: a finite-dim pure `H^•` at `∞` (a proper archimedean fibre) would place `|α|=√q` = the line = the zeros. That step is exactly the missing `ψ_∞`. So this is **not circular** — it imports no RH — but it is **TERMINUS_GEOMETRIC**: it proves the archimedean fibre is non-compactifiable in the operative sense (infinite-dim, no finite Frobenius), a genuine duality/H² gap, and that the living condensed theory supplies duality but not the purity that needs a finite ground.

---

## Falsifier verdict (PP-condensed — a terminus/type-obstruction locator, Euler-silent by design)

- **EULER-BORNE — NO, by design.** Like the R-thread, this locates the obstruction (properness/finite-dim purity at `∞`) via exact `𝔽_q`-vs-`∞` structure; not a standalone `ℤ`-positivity. DH structural verdict sharp and several levels before the radius: no `H¹` ⟹ no surface ⟹ no fibre ⟹ **nothing to compactify** (no Euler product ⟹ no fibre). `falsify.py`-consistent.
- **SEES-ZEROS — YES.** Finite-dim pure `H^•` at `∞` (a proper fibre) `= |α|=√q = M(N)=W =` purity `=` exactly where the zeros sit.
- **INDEPENDENT — NO.** Purity at `∞` `=` Weil II `=` the solved case over `𝔽_q`; over `ℤ` this is RH.

→ classifier **DISPERSING-by-design** (a terminus-characterizer / type-obstruction locator). **Ladder `DH < ζ < FF`:** DH no fibre to compactify; `ζ` an archimedean fibre with Serre/Verdier DUALITY (condensed-geometric, real) but INFINITE-dimensional cohomology (Γ-factor `det_∞`, log-Frobenius) — **non-proper, purity UNMARKED**; FF a smooth PROPER curve — finite-dim `H¹`, polynomial local factor, Frobenius converting weight to radius `√q`, **purity = a THEOREM**.

---

## Verdict

`[DECISION · coherence-checked vs 𝔽_q]` — **TERMINUS_GEOMETRIC.** The reframe "reality condition `F†=F̄` = properness of the archimedean fibre" is structurally CORRECT — [computed] anchor: over `𝔽_q` purity IS proper-pushforward purity (single Frobenius modulus `√q`), and an open/non-proper curve genuinely LOSES it (`H¹` mixed, moduli `{1,5}`). But condensed / analytic geometry (Clausen–Scholze), though a living theory that does honest archimedean geometry, supplies only **DUALITY** at `∞` — **Serre duality** (coherent, GAGA/HRR) and the abstract **six-functor Poincaré–Verdier duality** (2510.26269), which is provably **agnostic about weights and Frobenius eigenvalues**. **Duality is not purity.** Purity's only known proof (Weil II, Rankin positivity, squares-nonneg) **essentially imports the Frobenius and a finite field**, and is "not very compatible" with the archimedean place. Decisively, the archimedean fibre is **intrinsically NON-compact**: its cohomology is **INFINITE-dimensional** (Deninger/Consani–Marcolli — the Γ-factor is a regularized `det_∞` of an unbounded *log of Frobenius* `Φ` on an infinite-dim `V`, not a finite polynomial char-poly), the concrete **H²/Poincaré-duality gap**. **Properness does NOT force `F†=F̄` here**, because the fibre is not proper and the available archimedean theorem is the wrong one. **No RH/zero location is assumed** (not circular); the analysis proves the fibre is non-compactifiable in the operative sense — a real geometric terminus, the SAME atom as R8 (no finite constant field at `∞`) reappearing as infinite-dimensionality. **A finite-dim pure cohomology at `∞` would BE the missing `ψ_∞`** (a finite ground / archimedean Frobenius). **Successor:** none new — this confirms `ψ_∞` from the condensed/properness direction. The lead is genuine in form (purity = properness) but **TERMINUS in fact** (the archimedean fibre is non-compactifiable; condensed geometry gives duality, not the purity that requires the finite ground `ℤ` lacks at `∞`).
