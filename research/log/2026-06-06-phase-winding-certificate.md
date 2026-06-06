# Phase/winding certificate for `arg m` — NEXT #1 on-ramp (a) made forcing (2026-06-06)

**Item (AGENDA NEXT #1).** DONE #0 (`positivity_reality.py`) pinned the residual RH gap to a **PHASE
condition**: the symbol `m = |h|²·phase` has an unconditional MODULUS (sym² / `L(1,sym²)`, the edge,
RH-SILENT) and a FREE PHASE `arg m` (the line). NEXT #1 asks for an **Euler-borne phase/winding
certificate — NOT a norm-square** — that does what the sym² modulus cannot: on-ramp (a) the
Birman–Krein winding `d/dt arg S(½+it)` already SEES off-line zeros; *can it be made to FORCE* — a
positivity on the winding density, dominated by an Euler-borne archimedean phase?

Module: `scripts/numerics/witness/phase_winding.py`. Falsifier: 1 sharpened row in `falsify.py`.
Tags: **[THM]** / **[computed]** / **[honest-negative]**.

---

## The object

The scattering-phase **winding density** on the critical line,

> `w(t) := −(1/2π) d/dt arg S(½+it)`,  `S(s) = Λ(2s−1)/Λ(2s)`.

By the argument principle (Riemann–von Mangoldt) it splits **`w = w_arch − w_zeros`**:
- `w_arch(t) = (1/π) dθ/dt` — the **archimedean** `Γ_ℝ` (Riemann–Siegel `θ`) phase density: smooth,
  positive, monotone, **Euler-FREE**, and **shared verbatim with Davenport–Heilbronn** (DH has the
  same archimedean Γ factor).
- `w_zeros(t)` — a sum of **Poisson kernels** centred at the resonance ordinates, with width = the
  resonance's distance off the line `Re s = ¼` (its off-RH-ness). On-line ⟹ delta; off-line ⟹ a
  spread Lorentzian.

This is the **PHASE** half (vs DONE #0's RH-silent **MODULUS** `|h|²`) — the *right* half.

## What was computed (mpmath dps=25; `S`, `S_offline` from `scattering.py`, plant `ρ₀=0.8+10i`)

**[A] Decomposition is real.** `w(t) − w_arch(t)` is the prime/zero content; `w_arch` carries the
smooth positive background (e.g. `t=15`: `w=0.813`, `w_arch=0.138`, residue `0.675`). `w_arch` is
identical for ζ and DH.

**[B] The global winding SEES zeros (Birman–Krein count).** Over `t∈[2,30]`:
`N_ζ = 12.960`, `N_off = 14.919`, `Δ = +1.96` — the off-line resonance adds an anomalous crossing.
(Reproduces `prime_reflection.py` thread6.)

**[C] FORCING test — DECISIVE HONEST NEGATIVE.** Hypothesis: an off-line resonance makes the winding
density DIP NEGATIVE (backward winding) on the line, so `w(t)≥0` would discriminate. **The test
refuted this.** Computed on a grid `t∈[3,8]` straddling the plant's resonance ordinate:
- ζ: `min w = +8.1e-4`, nonneg ✓.
- off-line: `min w = +4.2e-2`, nonneg ✓ **(does NOT dip negative on the line)**.

The backward winding lives **at `Re s = Re(ρ₀)/2 = 0.4`** (the resonance line), where `w` plunges to
`≈ −2500` (the pole) — **NOT on `Re s = ½`**, where the off-line resonance is only a POSITIVE
Lorentzian **tail** (`≈ +4`). Verified directly:

| `Re s` | `w` at `t=5` |
|---|---|
| 0.50 (line) | +4.01 |
| 0.45 | +5.08 |
| 0.40 (resonance) | **−2498** |
| 0.35 | −1.59 |

So **local on-line density-positivity `w(t)≥0` is RH-NEUTRAL** — it holds for the off-line plant too.

**[D] KILL-TEST — the dominator is not Euler-borne.** A "forcing" would dominate `w_zeros` by the
positive background `w_arch`. But `w_arch` is the `Γ_ℝ` phase, **shared with DH**. Confirmed: the
archimedean-only scattering `S_inf(s)=Λ_∞(2s−1)/Λ_∞(2s)` (no Euler product, no zeros) carries the
**same** monotone background (`w_Sinf ≈ w_arch` to the smooth part). So any positivity resting on the
dominating phase is RH-neutral.

## Verdict — CIRCULAR (sees-zeros via a COUNT, not a local forcing; dominator not Euler-borne)

| axis | result |
|---|---|
| Euler-borne | the SIGNED density / global winding YES, but the available POSITIVITY (the dominating background `w_arch`) NO — it is the archimedean `Γ_ℝ` phase, shared verbatim with DH [D] |
| sees-zeros | YES, but only via the **GLOBAL winding** (Birman–Krein count [B]); the **LOCAL** density-positivity `w(t)≥0` on the line is RH-NEUTRAL [C] |
| independent | NO — `w(t)≥0` (read at the resonance location, `Re=¼`) IS "resonances on the line" = RH; the prime phase is SIGNED, no Euler-borne lower bound forces it |

**⟹ CIRCULAR.** Same box as the prior "Birman–Krein phase winding" row, now **sharpened**: the PHASE
(the right half, vs the RH-silent modulus) turns out to be a **WINDING COUNT**, and **counting ≠
forcing**. The off-line-ness is detected by a negative density **at `Re=0.4`** — i.e. by reading the
resonance LOCATION off the line, which is RH stated geometrically, not an independent positivity.

## What this sharpens (the decisive structural lesson)

DONE #0 split the gap MODULUS (sym², RH-silent) vs PHASE (the line). This pass takes the PHASE and
finds it is the **winding/argument-principle count**: it does see the zeros, but only **globally**
(the resonance count), and the natural **local** positivity (`w(t)≥0` on the line) is RH-neutral —
the negative winding that signals off-line-ness happens **at the off-line resonance's `Re`-value**,
which is exactly "the resonance is off the line" = ¬RH, read off, not forced. The only thing that
could DOMINATE the signed prime phase is the **archimedean `Γ_ℝ` background**, which DH shares ⟹ not
Euler-borne. **17th Euler-product confirmation.** First to make on-ramp (a) executable as a *density*
(not just a count) and pin why the phase, like the modulus, does not cross alone:

> The MODULUS (sym²) is Euler-borne + independent but RH-silent (blind to the line).
> The PHASE (winding) sees-zeros but is a COUNT — its forcing positivity is either the global
> resonance count (= a number, not a domination) or local `w≥0` (= RH, with an archimedean,
> RH-neutral, dominator). **Neither half forces alone.**

This says the certificate cannot be "modulus alone" or "phase alone" — it must **couple** the
Euler-borne modulus (sym², which DH lacks) to the line-detecting phase **in one functional whose
positivity is the domination `w_arch ≥ w_zeros`**, i.e. the explicit-formula inequality
`W_∞ ≥ Σ_p W_p` — the standing wall. The phase half re-confirms the wall from the argument-principle
side: the wall *is* "the Euler-borne (prime) phase is dominated by the archimedean phase," and the
prime phase is **signed** (no Euler-product lower bound), exactly as DONE #0(a) found the prime tail
to be the defect.

## Honest negatives recorded

- My initial hypothesis (off-line ⟹ negative density excursion **on the line**) was **wrong**; the
  test [C] caught it cleanly (off-line plant stays `w≥0` on `Re=½`). Corrected: the backward winding
  is **at `Re=0.4`**, off the line — so on-line density-positivity is RH-neutral, a *weaker* statement
  than I expected. This makes the negative finding sharper, not weaker: the phase's line-detection is
  purely GLOBAL (the count), never local.
- The "dominating archimedean phase" route (the explicit forcing on-ramp NEXT #1 named) is the `Γ_ℝ`
  background — confirmed **not Euler-borne** (DH-shared), so it cannot be the discriminating dominator.
