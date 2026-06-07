# F1-(S) — does the SPHERE SPECTRUM 𝕊 (Connes–Consani 2023 Riemann–Roch over 𝕊 / Segal Γ-rings) supply the archimedean conjugation an arithmetic SCALE q, or only the curve/duality skeleton (Step A) like every prior R-pass? [DECISION · coherence-checked vs 𝔽_q · SCALE_FREE_CLOSED]

2026-06-06. Candidate (S) of `research/f1-construction.md`. Lit (WebSearch/WebFetch, checked this pass): Connes–Consani *Riemann–Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$* (arXiv:2205.01391, 2023); *Riemann–Roch for the ring $\mathbb Z$* (arXiv:2306.00456, Bull. Sci. Math. 2023); *On the metaphysics of $\mathbb F_1$* (arXiv:2307.06748). Cross-thread: R8 (constant-field type obstruction), R10 (compactness = count not radius), QD (prismatic = finite-prime-indexed). Inline mpmath 25 dps. 49th `falsify.py` consideration, DISPERSING-by-design (terminus-characterizer, Euler-silent — but DH-killing).

## The mandate

(S) is the candidate with the **best 𝔽₁-pedigree** (Connes–Consani's own absolute base) and a **genuine homotopical finiteness** (Serre: `π_n(𝕊)` finite for `n>0`), and it is NOT one of the ruled-out coherence structures (NG-1/2/3). The single decisive test: does the homotopy-finiteness of 𝕊 give the archimedean conjugation an arithmetic SCALE `q` (a K-theoretic / homotopy invariant playing the role of `|𝔽_q|=q` = the Frobenius eigenvalue on `H²` = the Tate twist), or does 𝕊 give the **Step-A skeleton** (the curve + Serre duality, which CC2023 DID get) but NOT the archimedean radius — the same Step-A/Step-B split every prior R-pass hit?

## What CC2023 actually proved (lit, checked)

> **CC2023 Riemann–Roch over 𝕊:** `χ(D) = deg₂(D) + 1`, where the Euler characteristic of an Arakelov divisor on `\overline{\mathrm{Spec}\,\mathbb Z}` is its degree (logarithms **base 2**) plus `1`. The structural reading: `ℤ = 𝕊[X]` with `1+1 = X + X²` — `ℤ` is a **ring of polynomials in one variable over 𝕊**, and **𝕊 is a strong candidate for 𝔽₁**.

This is real and is the strongest 𝔽₁-result in the literature. The cohomologies `H⁰, H¹` (Serre duality) are built over 𝕊 via Segal Γ-rings (𝕊-modules = Kapranov–Smirnov vector spaces over 𝔽₁). **This is exactly Step A** (the curve, the duality, the functional equation / Riemann–Roch). The question is whether the **2** or the **homotopy-finiteness** is a Step-B scale.

## What got DECIDED (no zeros assumed on the radius axis; F_q anchor computed)

**[1] `χ(D) = deg₂(D) + 1` IS the genus-0 classical Riemann–Roch.** [computed]
Classical RR: `χ(O(D)) = deg(D) + 1 − g`. CC2023's `deg₂(D) + 1` is **`1 − g = 1`, i.e. `g = 0`** — `𝕊` sees `\overline{\mathrm{Spec}\,\mathbb Z}` as a **genus-0 𝔽₁-line** `𝕊[X]`. RR is the **Euler-characteristic (degree / count) statement = Step A**. It is the *same* equation for a pure and a non-pure Frobenius — it is **radius-blind**.

**[2] The base 2 is a DEGREE NORMALIZATION (a count), not an arithmetic radius q.** [computed, decisive]
The `2` is the Euler characteristic of the boundary 0-sphere (`χ(S⁰)=2`, `χ(S^{even})=2`) / the unit of the archimedean log-degree — it sets the **valuation/Haar normalization = the FE-symmetric scaling axis (Step A)**. Test: an arithmetic scale `q` lives in a **zeta numerator** `P(T)=∏(1−αᵢT)` as a Frobenius eigenvalue with modulus `√q`. The `2` is **not** in any such numerator; there is **no `H²` / Tate twist with eigenvalue `2`, no Frobenius of modulus `√2` acting on an `H¹`**. So `2 ≠ q` as a radius scale; it is the **+1/duality (count) side**, exactly the `deg`/abscissa coordinate that is free and DH-shared.

**[3] Homotopy-finiteness of 𝕊 (Serre) is a COUNT (Euler char / K-theory torsion), not a radius.** [structural]
- `π₀(𝕊) = ℤ` → **rank 1** → the **ONE variable `X`** of `𝕊[X]` = the curve/line = the duality skeleton (Step A). The "finiteness" that builds the curve is the rank-1 `π₀`.
- `π_n(𝕊)` finite (`n>0`) → **torsion** → contributes to the **Euler characteristic / `K`-theory torsion** — an **integer-valued count**, the `χ`/Lefschetz datum, NOT a continuous per-eigenvalue modulus. Baez–Dolan **homotopy cardinality** `|𝕊|` is an Euler-characteristic-type **rational / period-like** invariant (alternating sum over `π_n`) — it lives on the **COUNT axis** (the same axis R10's regularized trace and the explicit-formula Lefschetz count live on), and a count fixes only the geometric mean `(det F)^{1/2g}` (PA: the AM–GM *count*), **never the per-eigenvalue equality `|αᵢ|=√q`** (the radius / Step B). Serre-finiteness is the **wrong type** for the radius — precisely the R8 type mismatch (cardinality/count vs modulus), now at the homotopy level.

**[4] F_q ANCHOR — the 𝕊-RR does NOT recover `Frob=x^q` or `|α|=√q`.** [computed]
Applied to an actual `C/𝔽_q`, the 𝕊-Riemann–Roch yields `χ = deg + 1 − g` — the **Euler characteristic**, identical for pure and off-circle Frobenius. It does **not** reproduce the zeta numerator, the Frobenius `x^q`, or the radius. Computed `√q` for `q=4,9,25 → 2,3,5` and `genus-1 (q,a)=(5,1),(7,3),(11,−2),(13,4) → |α|=√q` exactly (`2.236,2.646,3.317,3.606`): the radius lives in `P(T)`, **radius-blind to RR**. The 𝕊-construction recovers the **curve + duality (Step A)**, never the **per-eigenvalue modulus (Step B)** — failing the decisive anchor clause.

**[5] DH falsified.** [computed/structural]
The `𝕊[X]`, `1+1=X+X²` presentation is the **multiplicative/Frobenius (Euler) datum** — the polynomial-ring structure over 𝕊. DH (functional equation, **no Euler product**) has no such presentation: no local Frobenius polynomial, no `𝕊[X]` Frobenius generator. The 𝕊-object is **unposable for DH** (inherited Euler-product kill, like every Frobenius-based candidate). DH dies — correctly.

## THE CRUX — is the homotopy-finiteness the missing scale, or the same Step A?

The 𝕊-finiteness is **real** (Serre) but it is the **wrong-axis** finiteness:
- It builds the **curve** (`π₀=ℤ` rank 1 = the one variable) and the **duality** (Serre duality / RR over 𝕊) — **Step A, which CC2023 explicitly achieved.**
- Its quantitative content (`π_n` torsion, homotopy cardinality, base-2 χ) is a **count / Euler characteristic**, the location/abscissa axis — **never a per-eigenvalue radius `√q`.**

This is the SAME split as the whole R-thread, now confirmed a fifth way:
- R3/R3b/R3b-BC: scaling site / length / `ℕˣ` → grading, edge, discreteness (free, Step A), **no constant-field size**.
- R8: residue field at `∞` = constant-field cardinality, **missing** (type obstruction).
- R10: compactness → regularized **trace = the count/explicit-formula** (free); radius is a separate Weil-positivity input = RH.
- QD: prismatic q-deformation = finite-prime-indexed Λ-ring, **archimedean-blind**, no archimedean `q`.
- **(S): 𝕊 → the curve `𝕊[X]` + Serre duality (Step A) + an Euler-characteristic/homotopy-cardinality COUNT; NO Tate twist, NO `H²` eigenvalue `q`, NO archimedean radius (Step B).**

**Honesty clause (as mandated):** CC2023 got the curve + Serre duality over 𝕊 — but their *archimedean positivity* (Weil positivity, BGS / Stone 3) is a **separate** line of work (the scaling Hamiltonian / Sonin space / prolate operator, where the archimedean positivity is proved by hand as an operator-positivity), **NOT supplied by the 𝕊-Riemann–Roch**. The scale is **exactly** that open piece: the 𝕊-base gives the duality skeleton; the radius/positivity stays an independent archimedean input (= RH). The two pieces of the program are disjoint, and only the skeleton is 𝕊-borne.

## Verdict — SCALE_FREE_CLOSED (the count axis; Step A only)

> **[DECISION · F1-(S) verdict].** The sphere spectrum 𝕊 is the strongest 𝔽₁-candidate in the literature and CC2023's Riemann–Roch over 𝕊 (`χ(D)=deg₂(D)+1`, `ℤ=𝕊[X]`, `1+1=X+X²`) genuinely realizes `\overline{\mathrm{Spec}\,\mathbb Z}` as a **genus-0 𝔽₁-curve with Serre duality** — **but that is Step A** (the curve + the functional-equation/duality skeleton). The **base-2** is a degree/Haar **normalization** (Euler char of the boundary sphere), not an arithmetic radius `q`; there is **no `H²` / Tate twist / Frobenius eigenvalue of modulus `√q`**. The genuine **homotopy-finiteness** (Serre: `π_n(𝕊)` finite) is the **wrong type**: `π₀=ℤ` (rank 1) builds the **curve**, and `π_n` torsion / homotopy cardinality is an **Euler-characteristic COUNT** (location/abscissa axis), which fixes only the geometric mean — **never the per-eigenvalue radius `|αᵢ|=√q`** (Step B = purity = RH). **Anchor FAIL:** applied to an actual `C/𝔽_q` the 𝕊-RR returns `χ=deg+1−g`, identical for pure and off-circle Frobenius — it does **not** recover `Frob=x^q` or `|α|=√q` (computed). **DH dies** (no Euler product ⟹ no `𝕊[X]` Frobenius presentation ⟹ no object). The 𝕊-base supplies the duality skeleton; the archimedean **positivity/radius** that CC2023 needs is proved *separately* (scaling Hamiltonian / Sonin), is **not** 𝕊-Riemann–Roch-borne, and **is exactly the open piece**. **SCALE_FREE_CLOSED — 𝕊 carries the reality-bearing duality (Step A) but is scale-free on the radius (Step B); the homotopy-finiteness is a COUNT, not the arithmetic `q`.** Same atom as R8/R10/QD, fifth confirmation, from the sharpest 𝔽₁-pedigree.

## Five-line decision (as required)

- **(a) Does 𝕊 build the curve/duality (Step A)?** YES — `χ(D)=deg₂(D)+1`, `ℤ=𝕊[X]`, genus-0 𝔽₁-line + Serre duality. The strongest 𝔽₁-skeleton in print.
- **(b) Does the base-2 supply an arithmetic radius q?** NO — it is the Euler char of the boundary sphere / degree-Haar normalization (the FE-symmetric axis, Step A); not a Frobenius eigenvalue, no `√2` radius, no `H²`/Tate twist.
- **(c) Does Serre homotopy-finiteness supply the scale?** NO — wrong type: `π₀=ℤ` (rank 1) = the curve; `π_n` torsion / homotopy cardinality = an **Euler-characteristic COUNT** (location axis), fixing the geometric mean only, never the per-eigenvalue modulus = radius.
- **(d) F_q anchor — recovers `Frob=x^q`, `|α|=√q`?** NO — 𝕊-RR returns `χ=deg+1−g`, radius-blind, identical for pure/non-pure (computed `√q` lives in `P(T)`, not in RR).
- **(e) Honest verdict + residual.** **SCALE_FREE_CLOSED.** 𝕊 gives the reality-bearing duality skeleton (Step A) and a genuine but **count-typed** finiteness; the radius/positivity (Step B = RH) is a **separate** archimedean input (CC2023's own Sonin/scaling-Hamiltonian positivity, *not* 𝕊-borne). **Residual:** the radius needs an **`H²`/Tate-twist Frobenius eigenvalue `q` over 𝕊** — a self-map of `𝕊[X]` with modulus `√q` on `H¹` — which 𝕊's homotopy structure does **not** carry; the count/radius decoupling (PA) recurs at the homotopy-cardinality level. **DH dies.**

## Falsifier verdict (F1-(S) — terminus-characterizer, Euler-silent by design, DH-killing)
- **EULER-BORNE — NO on this pass, by design.** Type-checks the 𝕊-Riemann–Roch + computes the `𝔽_q` anchor; not a standalone `ℤ`-positivity. DISPERSING-by-design (`euler_borne=False`). DH structural verdict SHARP: no Euler product ⟹ no `𝕊[X]` Frobenius presentation ⟹ no object.
- **SEES-ZEROS — YES.** The sought radius `√q = q^{w/2}` = even split = purity = where the zeros sit.
- **INDEPENDENT — NO.** The radius = purity = Weil II = the solved case over `𝔽_q`; over `ℤ` this is RH. The 𝕊-RR carries only the count (Euler char), not the radius.
→ **DISPERSING-by-design** (49th wall confirmation: the strongest 𝔽₁-base supplies the Step-A skeleton + a count-typed homotopy-finiteness, never the Step-B radius — the count/radius decoupling at the homotopy level).
