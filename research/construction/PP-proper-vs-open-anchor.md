# PP — proper-pushforward purity vs open-curve impurity: anchoring "proper ⟹ pure ⟹ F†=F̄" over 𝔽_q [DECISION · computed vs 𝔽_q]

**Charter:** the reality residue `F†=F̄` (Rosati adjoint = conjugation = `|α|=√q` = the line), reframed
as PROPERNESS of the archimedean fibre, because over `𝔽_q` purity = `F†=F̄` is Deligne proper-pushforward
purity. **Built on:** the-complete-account.md §5 (the residue = `F†=F̄`), R6 (smooth proper ⟹ pure ⟹ N=0),
R7/R8 (the radius is a finite-residue-field / constant-field invariant). **Module:**
`scripts/numerics/witness/proper_vs_open_anchor.py`
(run: `python3 -m scripts.numerics.witness.proper_vs_open_anchor`). **[computed]**

This pass tests, with REAL point-counts on REAL curves over `𝔽_q`, whether `F†=F̄` is genuinely
**proper-pushforward purity** (a theorem) rather than an imposed positivity (the dead branch) — and
exactly **where** the zero-locations enter.

---

## What was computed (no zeros assumed; weights read off honest point counts)

Elliptic curves `E/𝔽_q` for `(q,a) = (5,+1),(7,+3),(11,−2),(13,+4)` (Hasse-valid), with
`Z_E(T) = (1 − aT + qT²)/((1−T)(1−qT))`; `α,ᾱ` = roots of `X²−aX+q`.

**(1) PROPER projective curve `E/𝔽_q`: `H¹` is PURE.** `#E(𝔽_{qⁿ}) = qⁿ+1−(αⁿ+ᾱⁿ)` are honest
integers; `α·ᾱ = q` exactly; **`|α| = √q` in all four cases** (weights `=1.0`). `H⁰,H¹,H²` carry
weights `0,1,2` (`|·| = 1, √q, q`). **PURE** — the Weil radius, [computed].

**(2) OPEN curve `U = E ∖ {pts}` (AFFINE, NON-proper): `H¹_c` is MIXED.** For `U = E` minus `n` rational
points, `H¹_c(U) = H¹(U)^∨(−1)` carries the `2g` weight-1 classes (`|·|=√q`) PLUS `(n−1)` weight-0
classes (`|·|=1`). Removing `n≥2` points: **`H¹_c` weights `= {0,1}` — IMPURE/MIXED**, the weight DROPS
to `0` (`|·|=1 < √q`). [computed: `q=5`, minus 2 pts → `|·|={2.236,2.236,1.0}`, weights `{0,1}`.]
**Non-properness LOSES the reality condition.**

**(3) MECHANISM: proper ⟹ perfect Poincaré pairing ⟹ (α ↔ q/α).** The cup pairing
`H¹ × H¹ → H² = ℚ(−1)` is PERFECT on a smooth PROPER curve, so the dual/Rosati-adjoint eigenvalue is
`α-dual = q/α` (the functional equation `F·F† = q·id`). On the pure part `|α|² = q`, hence
`q/α = ᾱ`, i.e. **`F†` (= `q/α`, dual adjoint) `=` `F̄` (= `ᾱ`, conjugation)** — verified in all four
cases. [computed]

**(3b) SKEPTIC CONTROL — the perfect pairing ALONE does NOT force reality.** Take `α` with `α·β = q`
(pairing satisfied) but `|α|² ≠ q`: the dual eigenvalue is still `q/α`, but `q/α ≠ ᾱ`. [computed:
for `q=5,7,13` and `|α| ∈ {1, 1.3, √q, 1.9}`, the FE `α·β=q` holds at EVERY radius, but reality
`q/α=ᾱ` holds ONLY at `|α|=√q`.] **The eigenvalue-pairing is free (properness); the collapse of the
pairing partner onto the conjugate is the radius `|α|=√q` itself.**

---

## The decisive honesty finding: properness supplies the PAIRING, Weil II supplies the RADIUS

The mechanism "proper ⟹ pure ⟹ F†=F̄" **factors into two steps of very different depth**, and the
computation pins exactly which step carries the zeros:

- **Step A (FREE, properness alone): `F·F† = q·id`, i.e. `α ↔ q/α`.** This is the perfect Poincaré
  cup pairing / functional equation. It is a FORMAL consequence of `E` being smooth and proper
  (`H²=ℚ(−1)`, duality perfect). It does NOT use Weil II. It holds at **every** radius (3b).
- **Step B (DEEP, Weil II / Deligne RH-over-𝔽_q): `|α| = √q`, i.e. `q/α = ᾱ`.** Only this collapses
  the pairing partner `q/α` onto the conjugate `ᾱ`. **This is the radius, and it is exactly RH over
  `𝔽_q`.**

So **properness ALONE does NOT force `F†=F̄`.** Properness forces the *functional-equation structure*
(eigenvalues pair `α ↔ q/α`); the *reality* `q/α = ᾱ` is the additional content `|α|=√q` = purity =
Deligne's theorem. Over `𝔽_q` that theorem is available *because* the smooth proper variety has a
geometric `H¹` whose Frobenius weights Deligne bounds by `q^{i/2}` — and the proof of THAT (Weil II)
uses the geometry of the curve over the finite field, not merely abstract properness.

> **`where_RH_enters`:** at **Step B**, the modulus equality `|α|² = q`. The perfect pairing (Step A)
> is RH-silent — it gives `α·β = q` at any radius. The zeros sit at the radius, supplied by Weil II,
> not by properness as a formal property.

This is consistent with, and SHARPENS, the R-thread: R6 found "smooth proper ⟹ N=0 ⟹ pure" but the
purity radius `√q` is "a Weil theorem about the smooth curve, never produced by any N." Here we see the
finer split: properness gives the **perfect pairing** (the duality `D`, the FE), which is real and free;
the **radius** that turns the pairing into the reality condition is Weil II, and Weil II's content over
`𝔽_q` is the existence of a finite base field whose Frobenius has the `q^{w/2}` weights (R7/R8's
constant-field invariant `|κ|=q`).

---

## Archimedean transcription: where properness FAILS at `∞`

The reframing "compactify the archimedean fibre; properness forces purity" is now testable against this
factorization, and it FAILS at the depth where it matters:

- **Step A transcribes fine.** At `∞` the functional equation `s ↔ 1−s` (the archimedean analogue of
  `α ↔ q/α`) is PRESENT — `Γ_ℝ(s)` and the completed `ξ(s)=ξ(1−s)` give the perfect-pairing / duality
  structure for free. This is the "properness gives the FE" half, and `ζ` HAS it.
- **Step B does NOT transcribe.** The collapse "pairing partner = conjugate" needs `|α|²=q`, a finite
  cardinality `q` read off a finite residue/constant field. **The archimedean fibre is NOT proper in the
  sense that matters:** its cohomology is **not finite-dimensional with a perfect Poincaré duality valued
  in a finite-weight `ℚ(−1)` whose Frobenius is `q`** — the archimedean `Γ`-factor is an INFINITE Euler
  product (`Γ_ℝ` = `∏` over an infinite gamma-spectrum; M2d row: "no finite numerator"), so the would-be
  `H¹_c` at `∞` is **infinite-dimensional** and Poincaré duality is **not perfect / not finite-rank**.
  There is no finite `q` for `|α|²=q` to equal. This is precisely R7/R8: `κ(t=0)=ℂ` (continuum), the
  radius is **UNMARKED**.

So the archimedean fibre **is non-proper exactly at Step B**: the FE/pairing (Step A) survives, but the
finite perfect-duality that would force the radius is absent (infinite-dimensional `Γ`-cohomology / no
finite constant field). **Non-properness at `∞` loses the radius for the SAME reason removing points from
a curve loses purity** (Step (2)): in both cases the perfect finite Poincaré pairing is broken — open
curve: by the boundary (weight-0 drop); `∞`: by the infinite-dimensional archimedean fibre (no finite
`q`).

---

## Verdict — GENUINE LEAD as an ANCHOR, but properness does NOT force reality by itself; Weil II (the radius) does

> **[DECISION · PP verdict].** The mechanism "proper ⟹ pure ⟹ `F†=F̄`" is REAL and the anchor is
> CONFIRMED on real `𝔽_q` curves: (1) proper `H¹` PURE; (2) open `H¹_c` MIXED (weight-0 drop), so
> non-properness LOSES the reality condition; (3) proper ⟹ perfect Poincaré pairing ⟹ `α ↔ q/α`, and on
> the pure part `q/α = ᾱ` ⟹ `F†=F̄`. **BUT the honest factorization (3b) shows properness alone supplies
> only Step A (the perfect pairing / functional equation `α↔q/α`, RH-silent, holds at every radius); the
> reality `q/α=ᾱ` is Step B = `|α|=√q` = Weil II = RH over `𝔽_q`, NOT a formal consequence of
> properness.** Properness ⟹ perfect duality ⟹ FE is FREE; the RADIUS that collapses the FE into reality
> is the deep theorem, and the zeros enter exactly there.

**Classification of the components:**
- `[computed]` proper `H¹` pure (`|α|=√q`), open `H¹_c` mixed (weight `0` drop), `F†=F̄` on the pure
  part, and the skeptic control (FE free / reality only at `√q`) — all four, on real curves.
- `[BUILT]` the precise two-step factorization "properness ⟹ perfect pairing (Step A, free) ; Weil II
  ⟹ radius (Step B, the zeros)", and its archimedean transcription (Step A survives at `∞` via the FE;
  Step B fails via infinite-dimensional `Γ`-cohomology / no finite `q`).
- `[circular]` would be: claiming properness *by itself* forces `F†=F̄`. (3b) DISPROVES this — that is
  the dead "imposed positivity / assumed radius" branch, here explicitly excluded by computation.

**Is the archimedean fibre compactifiable in a living geometric theory (the GENUINE-LEAD condition)?**
The anchor is genuine (properness is the right *frame* — it is exactly what supplies the perfect duality
and, over `𝔽_q`, carries the radius via Weil II). But the residue is unchanged: the archimedean fibre is
**non-proper at Step B** — its cohomology is infinite-dimensional (`Γ`-factor, no finite numerator),
Poincaré duality is not perfect/finite, and there is no finite `q` for `|α|²=q`. Compactifying the
archimedean fibre into a FINITE perfect-duality object with a finite `q` IS the open problem `ψ_∞`
(R7/R8: a finite constant field at `∞`). **Properness frames the residue correctly and forces Step A;
it does NOT force Step B, and Step B is RH.**

**Why this is not a number conjured:** every weight is a point-count on a real curve; the skeptic control
explicitly separates the free (pairing) from the load-bearing (radius); the archimedean failure is
located at a concrete structural fact (infinite-dimensional `Γ`-cohomology), the same place M2d/R7/R8
independently reached.

---

## Falsifier verdict (PP — anchor / mechanism-locator, Euler-silent by design)

- **EULER-BORNE — NO on this pass.** Anchors the proper-pushforward mechanism via exact `𝔽_q`
  weight/pairing algebra; not a standalone `ℤ`-positivity.
- **SEES-ZEROS — YES (at Step B only).** The radius `|α|=√q` = purity = the even split = exactly where
  the zeros sit. Step A (the pairing) is RH-SILENT.
- **INDEPENDENT — NO.** Step B = Weil II = the solved case over `𝔽_q`; over `ℤ` it is RH.

→ **DISPERSING-by-design** (an anchor / mechanism-locator). **Ladder `DH < ζ < FF`:** DH no `H¹` (no
curve, no pairing); `ζ` HAS the perfect-pairing FE (`ξ(s)=ξ(1−s)`, Step A free) but the archimedean
fibre is non-proper (infinite-dim `Γ`-cohomology, no finite `q`) so Step B / the radius is UNMARKED;
FF a smooth proper curve with BOTH the perfect pairing (Step A) AND Weil II's finite-`q` radius (Step B,
MARKED `|α|=√q`). The decisive new content: **properness ⟹ perfect duality ⟹ FE is FREE and present at
`∞`; the radius is the separate deep step (Weil II), and it is exactly the residue.**
