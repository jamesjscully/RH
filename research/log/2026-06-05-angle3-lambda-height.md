# Angle 3 — Is the de Bruijn–Newman constant Λ an Arakelov height / a log-energy quantity?

2026-06-05. Certified probe (`scripts/numerics/witness/lambda_height.py`), per STRATEGY §8.
Reads the exact formulas from the three PDFs (`research/papers/`, gitignored) and tests the
"harmonic-number / digamma thread" of `research/metric-arakelov-probe.md` §3.

## The exact archimedean energy expressions (quoted, not invented)

**(W) Weil explicit-formula archimedean term** — Connes–Consani arXiv:2006.13771, Appendix B:

- (150)  `W_R(f) = (log 4π + γ) f(1) + ∫₁^∞ ( f(x) + f^7(x) − 2 f(1)/x ) dx / (x − x⁻¹)`
- (151)  `W_R(f) = (log π) f(1) − (1/2πi) ∫_{Re=1/2} Re( Γ'/Γ(w/2) ) f̃(w) dw`
- (153)  spectral density  `h₊(τ) = − log π + Re ψ(¼ + iτ/2)`,  `ψ = Γ'/Γ` (digamma)
- (154)  `h₊(τ) = d/dτ [ 2 θ(τ) ]`, θ the Riemann–Siegel angle `θ(E)= −E/2 logπ + Im logΓ(¼+iE/2)`

**(B) BGS resultant height** — Bost–Gillet–Soulé, JAMS 1994, Lemma 4.3.4 (read p. ~3 of the PDF):

- `log‖R‖_Herm = ½ (∏ᵢ dᵢ) · ( (N+1) H_N − N ) + ε`,  `H_N = 1 + ½ + … + 1/N` the harmonic number,
  `|ε| ≤ ½(∏dᵢ) Σ (dᵢ/N) log(dᵢ+1)`.

**(P) Pardo–Pardo expected log-norm of affine solutions** — AAECC 2016, Corollary 5.4:

- `(1/D) · E_{S(d)} Σ_{ζ} log(1 + ‖ζ‖²) = ψ(n+1) − ψ(1) = H_n`;  expected **mean** `= ½ H_n`
  (the slack/condition-number side: `μ_norm = ‖f‖_Δ ‖Diag(dᵢ^{−½}) Df†‖` in the Bombieri–Weyl norm).

## What is certified (acb/arb ball arithmetic, `lambda_height.py`)

1. **(W), (B), (P) are values/derivatives of ONE function — the digamma `ψ = Γ'/Γ`.**
   `½H_n = ½(ψ(n+1) − ψ(1))`, `H_n = ψ(n+1)+γ` (since `ψ(1) = −γ`), `(N+1)H_N − N` is a digamma
   expression, and the Weil density is `ψ(¼+iτ/2)`. `ψ` is the log-derivative of the archimedean
   local L-factor `Γ_ℝ(s)=π^{−s/2}Γ(s/2)`. Certified to machine precision (errs `0`–`10⁻¹⁵`).

2. **The de Bruijn–Newman fixed shape carries exactly the Weil archimedean term.**
   The dBN flow is `H_t(z)=∫₀^∞ Φ(u) e^{tu²} cos(zu) du`, `H_0 = Ξ`, and `Ξ(t)` is the completed
   zeta `ξ(s)=½ s(s−1) π^{−s/2}Γ(s/2) ζ(s)` on `s=½+it`. Its archimedean (gamma-factor) energy is
   `E_Ξ(t) = d/ds log[π^{−s/2}Γ(s/2)]|_{s=½+it} = −½ logπ + ½ ψ(¼+it/2)`. **Certified identity:**

   > `2 · Re E_Ξ(t)  ==  h₊(t)`   (max |difference| ≤ 2.42e-15 over t∈{0,1,5,14.13}; an EXACT identity).

   So the **de Bruijn–Newman archimedean term and the Weil archimedean term are literally the same
   digamma object** — the gamma factor of ξ. And `h₊ = d/dτ[2θ]` (Riemann–Siegel angle), confirmed.

3. **Constant coincidences.** Weil constant `log4π + γ = 3.10824…` and the Burnol/BD constant
   `2 + γ − log4π = 0.0461914…` (the one in `FLINT_CAPABILITIES.md` Check 3, the Li/Báez-Duarte
   dilation asymptotics) are **complementary**: `(log4π+γ) + (2+γ−log4π) = 2 + 2γ` (certified). Both
   are built from the *same* archimedean data `(γ, log4π)` — i.e. the value/derivative of `Γ_ℝ` at the
   central point. They are two sides of one archimedean constant, not two unrelated numbers.

## Verdict — GO on the unification, NO-GO on the literal height

**GO (the threads are the same potential theory).** The dBN fixed-shape archimedean energy, the
Weil explicit-formula archimedean term, the Pardo–Pardo condition-number/height (`½H_n`), and the
BGS resultant height (`(N+1)H_N − N`) are **all the digamma `ψ=Γ'/Γ`** — values, derivatives, or
finite differences of the *same* archimedean object (the log-energy of the local L-factor `Γ_ℝ`).
This is a genuine, certified unification of the program's threads: the slack's height (Arakelov),
the Weil positivity term, and the de Bruijn–Newman fixed shape share one archimedean potential
theory. The metric-arakelov-probe §3 "harmonic-number/digamma thread" is now an *exact identity*,
not an analogy, on the side it can be made exact (the dBN↔Weil junction: `2 E_Ξ = h₊`).

**NO-GO (Λ is not literally a height).** Λ has no known closed form. It is the *marginal time* of
a flow whose kernel is the **Gaussian heat kernel `e^{tu²}`** — not a digamma, not a height. The
digamma/height structure lives entirely in the **fixed shape Ξ = H₀** (the gamma factor), which is
shared with Weil/Arakelov; it does **not** descend to Λ as a single number. `Λ ≥ 0` (Rodgers–Tao)
comes from the *dynamics* + Montgomery pair correlation, not from an `h(X) ≥ 0` positivity, so the
hoped-for "Λ≥0 re-derives as BGS `h≥0`" does **not** hold: they are different positivities of
different objects (a dynamical inf vs. an arithmetic intersection number).

Honest distinction (as instructed):
- **Established (certified):** dBN-fixed-shape ≡ Weil archimedean ≡ digamma; the three heights are
  one `ψ`; the Weil/Burnol constants are complementary halves of `2+2γ`.
- **Structurally suggestive only:** that this shared archimedean potential theory could let an
  Arakelov positivity speak to `Λ ≤ 0`. The *archimedean place* is shared; the *finite/dynamical*
  content that actually pins Λ (heat flow, zero statistics) is not Arakelov and is the hard part.
- **Not established (dropped):** Λ as a single Arakelov height; `Λ≥0` as `h(X)≥0`.

## Honest next step

The unification is real but lives at the archimedean place — which is the *easy, known* part
(the gamma factor / `Γ_ℝ`). The RH-hard content (Euler product on the Weil side; the heat-flow +
pair-correlation on the dBN side; the positive-Green-form obstruction BGS §6.3 on the Arakelov
side) is precisely the part that is **not** captured by the shared digamma. So the digamma thread
is a true structural bridge but **not a forcing structure**: it does not separate ζ from
Davenport–Heilbronn (DH has the *same* `Γ_ℝ` archimedean factor — the digamma term is DH-blind, it
is exactly the kind of functional-equation/Γ-factor data STRATEGY §0 flags as RH-neutral). The
productive next move is **not** to push Λ-as-height further (NO-GO) but to ask whether the dBN
*flow* (the Gaussian part, where Λ actually lives) admits a height/energy reading — i.e. carry the
analysis to the **finite places / heat-kernel**, not the archimedean Γ-factor, since the archimedean
piece is now fully accounted for and is shared/RH-neutral. Net for the program: one thread closed
cleanly (the archimedean energies are one object, certified), and the RH-hard difficulty is
relocated, sharply, to the non-archimedean / dynamical side where it belongs.
