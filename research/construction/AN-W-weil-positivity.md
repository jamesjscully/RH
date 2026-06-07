# AN-W — Weil positivity / the explicit formula: the audit's central object (2026-06-06)

**Strategy (W).** RH ⟺ the **Weil functional** `W(f) = Σ_ρ ĥ_f(ρ) ≥ 0` for all suitable test
functions `f` (equivalently: the quadratic form attached to the Guinand–Weil explicit formula is
positive-semidefinite; equivalently Li's `λ_n ≥ 0` for all `n`). This is the analytic shadow of the
"missing object" — `weil_form.py`, the centre of the whole positivity audit
(`research/positivity-program.md`).

**Verdict: CIRCULAR — the positivity *is* RH, and there is no independent analytic source.**
Bombieri–Lagarias pins the circularity exactly. The only unconditional positivity (Bombieri's
small-support / Yoshida theorem) is an EDGE result that provably does not reach the line.

---

## 1. Confirm the equivalence (the prerequisite IS RH) [established]

`W(f) ≥ 0` for all suitable `f` ⟺ RH (Weil 1952; Bombieri). The mechanism is transparent and verified
in the repo (`weil_form.py`, `li_positivity.py`):

- **Spectral side.** `W = Σ_ρ |Σ_a c_a ĥ_a(γ_ρ)|²` is **manifestly ≥ 0 iff every `γ_ρ` is real**,
  i.e. iff RH. Computed: on the true zeros the Weil Toeplitz form has `min eig = −3.4e-16` (PSD); a
  planted off-line zero `β=0.8` gives `min eig = −1.49` (positivity breaks). *The form IS the
  RH-detector.* [computed]
- **Li avatar.** For `ρ=½+iγ`, `|1−1/ρ| = |ρ−1|/|ρ| = 1` **exactly** ⟹ each pair contributes in
  `[0,4] ≥ 0`. For an off-line zero `Re ρ<½`, `|1−1/ρ|>1` ⟹ `(1−1/ρ)^n` grows ⟹ `λ_n → −∞`.
  Computed on DH's sub-½ functional-equation mate (`Re=0.1915`, `|1−1/ρ|=1.000042>1`): first
  negative at `n=521`, reaching `−3.9e7` by `n≈4e5`. [computed]

So as a STRATEGY — "prove `W ≥ 0` directly" — the prerequisite is RH restated. **CIRCULAR unless a new
source of positivity, independent of the zeros' location, is exhibited.**

## 2. The precise content: the cross-place coupling (the wall) [established]

The explicit formula writes the SAME form on the arithmetic side as
`W(f) = W_∞(f) [archimedean Γ_ℝ/digamma] + (poles s=0,1) − Σ_p W_p(f) [primes Λ(n)]`.
RH ⟺ the archimedean term dominates the prime term, `W_∞ ≥ Σ_p W_p` — the **cross-place coupling**.
The program's entire auditor (`positivity-program.md` §B, 29 Euler-product confirmations) reduces every
route to exactly this margin. Three independent facts make it the wall:

- **The archimedean piece is RH-NEUTRAL.** `W_∞` (the `Γ_ℝ` Gram) is *identical* for ζ and
  Davenport–Heilbronn: `max|A_ζ − A_DH| = 0` exactly (`arakelov_signature.py`,
  `operator_domination.py`). The dominating positive term carries no Euler content.
- **The Euler content lives only in the dominated prime term** `Σ_p W_p` (the `Λ(n)` Gram), which is
  itself PSD and *zero-independent*: `Λ(n)` is a property of the Euler product, with no "plant a zero"
  knob (`max|P_from(−ζ'/ζ) − P_from(Λ)| = 0`, `operator_domination.py`). So `W = A − P` read as a
  difference of two fixed forms is RH-SILENT; the only zero-bearing reading is the spectral side
  `Σ_ρ ĥ(γ_ρ)`, which is PSD ⟺ RH = circular. **The pin: no single piece is BOTH Euler-borne-and-
  independent AND zero-bearing.**

## 3. Is there any non-circular analytic positivity source? [established — NO known one]

This is the decisive question, and the literature answers it sharply against the strategy:

- **Bombieri–Lagarias (1999), "Complements to Li's criterion."** Li's positivity `λ_n ≥ 0` follows
  from a general set of inequalities for an **ARBITRARY multiset of complex numbers lying on
  `Re s = ½`** — it is *not specific to ζ*. ⟹ The positivity is a CONSEQUENCE of the zeros already
  being on the line, **not an independent source that forces them there.** This is the cleanest proof
  that the strategy is circular: the positivity carries no zeta-specific arithmetic lever; supply the
  on-line zeros and you get positivity for free, generically. [established]
- **Bombieri (2000), "Remarks on Weil's quadratic functional, I."** The ONE unconditional positivity:
  `W` attains its minimum on the unit ball of `L²` with support in `[−t,t]`, and is **positive-
  definite for `t` sufficiently small** (Yoshida's theorem). This is an EDGE/small-support result —
  the same shape as Worker E's certificate ladder (Hecke/Euler certifies the edge `Re s=1`, never the
  line `Re s=½`). It provably does NOT extend to large support (that extension *is* RH). [established,
  partial scope]
- **Burnol, Yoshida, et al.** sharpen positivity on subspaces (Sonin space, Hermite–Biehler), all
  conditional or small-support. No unconditional global `W ≥ 0` is known by any analytic route. [established]

**Conclusion:** the only known global positivity *is* the assertion `W ≥ 0` = RH; the only
unconditional positivity is small-support (edge), which does not reach the line. **No non-circular
analytic positivity source for `W` is known.**

## 4. Anchor (function field) + DH

- **Anchor [established].** Over `𝔽_q(C)` the same explicit formula holds and `W ≥ 0` is **Weil's
  theorem** — but its positivity source is the **Hodge index theorem on `C×C`**, a *geometric*
  positivity holding because the surface is projective over the finite field. The analytic content of
  W over function fields is therefore NOT vacuous and NOT analytic — it is *imported from the
  geometry*. By Theorem A (`WRITEUP-geometric-obstruction.md`) that geometric source has no
  archimedean analogue over ℚ (no finite ground at `∞`), and by Theorem B′ the similitude/duality
  structure underdetermines the signature. So over ℚ the W-positivity has **no structural source** and
  must come from analysis — and §3 shows no analytic source is known. This is the exact junction where
  the geometric no-go hands off to the analytic audit.
- **DH: FAIL [established].** Davenport–Heilbronn has the ζ-type Γ_ℝ functional equation, **no Euler
  product**, and off-line zeros. Its `W_∞` is identical to ζ's (`max|A_ζ−A_DH|=0`); its Li
  coefficients go negative (computed, §1). So DH violates W-positivity *because* it has off-line zeros
  — confirming W IS the RH-detector and that the discrimination is downstream of the zero locations,
  carried only through the prime term. The litmus is consistent: W is "on the critical path" but its
  positivity is not an independent lever.

## 5. Positivity source classification

- **GENUINE_ANALYTIC?** NO global one is known. Bombieri's small-support positivity is genuine and
  analytic but EDGE-only (does not reach the line). [partial]
- **REDUCES_TO_WEIL.** The strategy IS Weil positivity; Bombieri–Lagarias shows the positivity is a
  consequence of on-line-ness, generic to any multiset on `Re=½` — i.e. it reduces to itself with no
  arithmetic lever. **positivity_source = REDUCES_TO_WEIL.**

## Verdict

> **CIRCULAR.** The prerequisite (`W(f) ≥ 0` for all suitable `f`) is RH restated (Weil; computed
> both ways in `weil_form.py`/`li_positivity.py`). Bombieri–Lagarias proves the positivity is generic
> to any on-line multiset — no zeta-specific, zero-forcing source. The only unconditional positivity
> (Bombieri small-support / Yoshida) is an edge result that provably does not reach the line. The
> precise content is the cross-place coupling `W_∞ ≥ Σ_p W_p`: the dominating archimedean term is
> RH-neutral (DH-shared), the Euler-borne prime term is zero-independent — so no single piece is both
> Euler-borne-independent and zero-bearing. **No new analytic positivity source; the strategy is the
> wall, not a road past it.**

**Prerequisite_status = CIRCULAR.** It is not contradictory (consistent: it holds iff RH) and not an
unconstructed object — it is RH itself wearing a quadratic-form coat.

## References
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, 1952.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers, I*, 2000
  (small-support positive-definiteness; Yoshida's theorem).
- E. Bombieri, J. Lagarias, *Complements to Li's criterion for the Riemann hypothesis*, J. Number
  Theory 77 (1999) — λ_n positivity for an arbitrary multiset on `Re=½` (the non-specificity = the
  circularity pin).
- X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, 1997.
- Repo: `scripts/numerics/witness/weil_form.py`, `li_positivity.py`, `operator_domination.py`,
  `arakelov_signature.py`; `research/positivity-program.md` (the full auditor, §§B,E,L).
