# Thread 0 — the global/equivariant extension of CC20's archimedean Weil positivity (opened 2026-06-06)

**Question.** CC20 (arXiv:2006.13771, *Weil positivity and Trace formula, the archimedean place*,
Selecta 2021) proved `W_∞(g⋆g*) ≥ Tr(ϑ(g) S ϑ(g)*) ≥ 0` at the **single archimedean place**,
conditionally (Fourier vanishing `ĝ(±i/2)=ĝ(0)=0`, support in `[2^{-1/2}, 2^{1/2}] ⊂ (1/2,2)` so no
prime is involved, via the prolate/Sonin projection `S` onto the orthogonal complement of the cutoff
range at `Λ=1`, which breaks `ℝ₊^*`-equivariance). What has been done 2020–2026 to (a) extend this
positivity to include the **primes** / be **global**, and (b) make it **equivariant** (no scale-
breaking cutoff)?

Tags: **[THM]** proven, **[PROG]** defined/strategy/incomplete, **[CONJ]** conjectural/expected,
**[AN]** analogy. All non-trivial claims are quoted from sources below.

---

## 1. State of the art — what is proven vs open in the global/equivariant direction

The relevant body of work is a coherent Connes–Consani(–Moscovici) program. The papers, in order:

| paper | arXiv / date | what it adds toward global/equivariant positivity |
|---|---|---|
| **Weil positivity, archimedean place** (CC) | 2006.13771, Jun 2020 / Selecta 2021 | the **base result**: positivity at `∞`, one place, conditional, `Λ=1` cutoff |
| **Zeta zeros and prolate wave operators** (CCM) | 2310.18423, Oct 2023 / rev. May 2024, Ann. Funct. Anal. 15 (2024) no. 87 | the **semilocal prolate operator**: stability of the semilocal Sonin space; the strategy to attack semilocal positivity |
| **Zeta Spectral Triples** (CCM) | 2511.22755, Nov 2025 | spectral triples whose spectra approximate the low zeros; **explicitly numerical**, RH-equivalent convergence open |
| **On the Jacobian of Spec̄ ℤ** (CC) | 2602.15941, Feb 2026 | the **geometric home**: Picard/Jacobian monoid of `\overline{Spec ℤ}`; §9 re-derives the semilocal trace formula as a Lefschetz formula on `\widetilde{Pic}` |

**(a) Inclusion of the primes — partial, structural, NOT a positivity proof.**
- The **semilocal trace formula** is now set up for a *finite* set `S` of places with `∞ ∈ S`, i.e.
  it can include finitely many primes `{∞,2,3,…,p}`. CCM 2024 (2310.18423) builds the **semilocal
  prolate wave operator** and proves **[THM]** *"the stability of the semilocal Sonin space under the
  increase of the finite set of places which govern the semilocal framework"* (abstract), with a
  hilbertian isomorphism `θ_S : L²(ℝ)^ev → L²(X_S)^{K_S}` of the Sonin spaces (their Theorem 2).
- The Jacobian paper (2602.15941) §9.3 reproduces the semilocal trace formula as
  `Trace(θ(h) R_λ) = 2 h(1) log λ + Σ_{v∈S} ∫'_{ℚ_v^×} h(u^{-1})/|1−u| d*u + o(1)` (their eq. 20),
  the geometric/Lefschetz side over `\widetilde{Pic}(\overline{Spec ℤ})`. This is the **trace formula
  and the spectral realization** of the zeros — *not* a positivity statement.
- **The positivity itself is still proven only at `∞`.** CCM 2024 state it verbatim (intro,
  2310.18423): *"the results of [9,10] show that the semilocal trace formula of [7] gives a
  conceptual explanation of Weil's positivity **for the archimedean place**, the source of it being
  the Hilbert space representation of the scaling group."* The semilocal positivity is an
  **expectation/strategy**: *"**We expect** that the use of such operator-theoretic tools in the
  semilocal case opens a way to handle Weil's positivity as in [10]. In fact, the operator theoretic
  aspect of the present paper provides **a more precise strategy** for addressing the semilocal Weil
  positivity by comparing the trace functional … with the Weil functional."* **[CONJ]/[PROG]** — not
  **[THM]**.
- The semilocal Sonin space *"**should**, when suitably equipped with a prolate type operator, play
  the role of the **sought for Weil cohomology**"* (CCM 2024, remark after their Thm 2). The Weil
  cohomology over `S` is **sought**, not built.

**(b) Equivariance — NOT achieved; the cutoff is still load-bearing.**
- The mechanism that *delivers* positivity at `∞` is the compression onto `S = `(orth. complement of
  the range of the cutoff projections `P_Λ, \hat P_Λ` at `Λ=1`). The cutoff `R_λ = \hat P_λ P_λ`
  (limit both `|p|,|q| ≤ λ`) is intrinsically scale-breaking; the semilocal trace formula
  (eq. 20 above) still carries the **divergent `2 h(1) log λ`** term — *"The divergent term `2h(1)log λ`
  signals the presence of the white light coming from the (trace of the) regular representation"*
  (2602.15941 §9.3). CC themselves named this in CC20: the cutoff of [Berry–Keating] *"lack[s]
  invariance under the scaling action ϑ … This issue makes problematic restricting the Hamiltonian."*
- No 2020–2026 paper removes the cutoff. The Sonin/prolate route **replaces** the cutoff by the
  prolate operator's negative eigenspace (UV) and positive eigenspace (IR) — but the prolate operator
  `W_λ = −S² + 2πλ²(4N+1) − 1/4` (CCM 2024 eq. 2) **itself carries the scale parameter `λ`**: it is a
  one-parameter family, not a scale-invariant object. Equivariance is *traded* for the prolate
  filtration, not *attained*.

**Net.** Since 2020 the program has (i) built the **semilocal stage** (finite `S`, prolate operator,
stable Sonin space) and (ii) given it a **geometric home** (the Jacobian/`\widetilde{Pic}` of
`\overline{Spec ℤ}`, with the explicit formula = a Lefschetz trace on it). It has **not** proven Weil
positivity at even one prime, and has **not** produced an equivariant (cutoff-free) positivity. The
global/equivariant positivity is exactly as open as RH.

## 2. The precise obstruction to extending past one place

It is the **same primes-vs-archimedean near-cancellation the program names** — confirmed at the
source, twice:

1. **The corner `Δ` is the obstruction (CC20 §2, verbatim).** *"we show that the obstruction to get
   Weil's positivity in the local archimedean case is due to the specific contribution of the **small
   square `Δ`**"* (`Δ = [0,1]²` in Fig. 1; the trace-remainder `δ(ρ) = Tr((ϑ_m(ρ^{-1}) − Pϑ_m(ρ^{-1})P)
   ½(u*du)^g)`, CC20 Def. 2.1). The decisive analytic fact is the **jump of `δ'(ρ)` at `ρ=1`** (from
   `−1` to `+1`, CC20 eq. 10), i.e. a derivative discontinuity at the diagonal `ρ=1`. This is
   precisely the program's `Δ·Δ` corner / `−1/(2|u|)` conformal kernel: the self-intersection of the
   diagonal is where the divergence/obstruction lives.

2. **Positivity is a delicate cancellation between `∞` and the actual prime — not archimedean
   dominance (CC20).** CC20 record that the archimedean Weil quadratic form **loses positivity on
   some intervals, and positivity is restored only by the contribution of the prime `p=2`**;
   moreover the sign is *"sensitive to replacing the functional for `p=2` with one for `p` taken as a
   real variable, with positivity failing outside an interval of size `< 10^{-3}` around `p=2`."* So
   the positive sum is **not** "archimedean term dominates a small prime perturbation"; it is a
   **knife-edge cancellation that requires the exact arithmetic prime `p=2`** (an integer, not a
   nearby real). This is the obstruction stated sharply: any extension must control the
   `∞`-vs-`{primes}` balance *to within `10^{-3}` and using the actual primes* — it cannot be gotten
   by domination or by `Γ_ℝ`-type archimedean data alone.

This matches the program's own diagnosis (positivity-program.md row "ample cone/polarization → `h_∞`:
**breaks** — positive Green form can fail, BGS §6.3; the missing-object file §5.1). The
Connes–Consani obstruction *is* the BGS §6.3 positive-Green-form obstruction localized to the small
square `Δ`. The wall is real, not cosmetic.

## 3. Kill-test discipline — the archimedean positivity alone is RH-neutral (CONFIRMED)

The thread predicts CC20's archimedean positivity, **taken alone**, should NOT distinguish ζ from
Davenport–Heilbronn (same `Γ_ℝ`), because it is the RH-neutral part. The sources confirm this:

- The archimedean positivity is proven **under the support condition `support(f) ⊂ (1/2,2)`** — i.e.
  **"so that rational primes are not involved"** (CC20 p. 2). A statement that holds with *no prime
  in its support* cannot see the Euler product, hence cannot separate ζ from any function with the
  same `Γ_ℝ`/functional-equation. **It is RH-neutral by construction.** This is the 5th independent
  confirmation in the program (after `edge-is-dispersing`, descent triviality, Angle 3, scattering
  stone 1).
- Consistent with §2's point 2: the **RH content only enters when an actual prime `p` enters the
  support** and the `10^{-3}` knife-edge cancellation becomes load-bearing. DH has the same `Γ_ℝ`
  archimedean term but **no Euler product**, so the prime contributions that restore/destroy
  positivity differ — DH must fail the cancellation. (Not yet executed against DH in this program's
  scaffold; see §4.)
- Therefore the discipline holds: CC20's one-place theorem is the **right kind of RH-neutral
  brick**; the forcing only lives in the prime extension. A candidate that gave archimedean
  positivity *equally for DH* would be correctly flagged as dispersing — and CC20's does, vacuously,
  because it excludes primes.

## 4. The single most concrete open sub-statement that would advance this

> **[CONJ → target] Semilocal Weil positivity at the first prime, equivariantly stated.**
> For `S = {∞, 2}`, prove `W_{S}(g ⋆ g^*) ≥ 0` for `g ∈ C_c^∞(ℝ₊^*)` with `support(g) ⊂ (2^{-1}, 2)`
> and the Fourier-vanishing conditions, via the **semilocal Sonin/prolate compression** — i.e. show
> `Tr(ϑ(g) S_S ϑ(g)^*)` (with `S_S` the orthogonal projection onto the **stable semilocal Sonin
> space** of CCM 2024) **dominates the Weil functional**, with the `p=2` contribution supplying
> exactly the trace-remainder `δ` deficit from the small square `Δ`.

Why this is *the* sub-statement:
- It is the **minimal** step that crosses from "one place" to "primes": one archimedean place + one
  prime, the smallest case where the `10^{-3}` `∞`-vs-`p=2` cancellation (§2.2) must be *proven*
  rather than observed numerically.
- The two needed pieces now both exist: CCM 2024 built and proved **stability of the semilocal Sonin
  space** (the `S_S`), and CC20 reduced archimedean positivity to controlling the small-square
  remainder `δ` by a compact-operator (`−2 Id + K`, Hilbert–Schmidt) argument. The open work is to
  show the **prime-`2` term enters `δ` with the right sign to keep `Id − K` positive** — i.e. that
  the Toeplitz/Hilbert–Schmidt control of CC20 §3–6 survives the addition of the `ℚ_2^×` factor.
- It is **kill-testable in this program's scaffold immediately**: feed ζ's and DH's `S={∞,2}` data
  (same `Γ_ℝ`, ζ has the `(1−2^{-s})` Euler factor, DH does not) through `weil_form.py` /
  `scattering_forcing.py` restricted to `support ⊂ (2^{-1},2)`. Prediction: ζ's `W_{{∞,2}} ≥ 0` on
  this support; DH's fails (no `2`-Euler factor ⟹ wrong `δ`-deficit). If DH also stays positive on
  this support, the `S={∞,2}` form is still RH-neutral and the prime-extension bet weakens; if DH
  fails, this is **the first equivariant-flavored object in the program that sees the Euler product**
  — the spine the lift-program seeks.

Secondary (the equivariant ambition, harder): remove the `Λ`/`λ` parameter entirely — replace the
prolate family `W_λ` by a single scale-invariant operator whose IR/UV splitting reproduces the Sonin
compression without a cutoff. CCM 2024 hint at this via the **metaplectic representation of the double
cover of `SL(2,ℝ)`** (their §5), aiming for *"a second candidate for the semilocal prolate operator"* —
but this is announced as **forthcoming**, not done. The `S={∞,2}` positivity is the prerequisite and
the right first target.

---

## Sources

- A. Connes, C. Consani, *Weil positivity and Trace formula, the archimedean place*, arXiv:2006.13771
  (Jun 2020), Selecta Math. 27 (2021) no. 4, art. 77 — local PDF
  `research/papers/connes-consani-weil-positivity-archimedean.pdf` (Thm 1, Cor 2, §2 obstruction/`Δ`,
  Def 2.1, eqs. 10/39, support `(1/2,2)` "rational primes not involved").
- A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators*, arXiv:2310.18423
  (Oct 2023, rev. May 2024), Ann. Funct. Anal. 15 (2024) no. 4, art. 87 (semilocal prolate operator;
  Sonin-space stability Thm 2; "for the archimedean place"; "We expect … semilocal Weil positivity";
  "sought for Weil cohomology"; metaplectic §5 forthcoming).
- A. Connes, C. Consani, H. Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755 (Nov 2025)
  (spectral triples approximating the low zeros; convergence ⇒ RH stated as open).
- A. Connes, C. Consani, *On the Jacobian of `\overline{Spec ℤ}`*, arXiv:2602.15941 (Feb 2026)
  (Pic/Jac monoid of `\overline{Spec ℤ}`; §9 semilocal trace formula as Lefschetz on `\widetilde{Pic}`,
  eq. 20 with divergent `2 h(1) log λ`).
- A. Connes, C. Consani, *The Scaling Hamiltonian*, arXiv:1910.14368 (2019) (Berry–Keating ⟷ scaling,
  cutoff non-invariance).
- R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv:math/0412277
  (related: explicit formula as a trace; RH ⟺ positivity; not a positivity proof).
