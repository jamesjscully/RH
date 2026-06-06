# PA — the LOCAL ARCHIMEDEAN Rankin–Selberg positivity: is M3's `P_∞` the local-arch RS positivity, and is it a NEW radius input or the same edge wall? [DECISION · coherence-checked vs 𝔽_q / DH]

2026-06-06. Module probes: `/tmp/pa_archimedean_rs.py`, `/tmp/pa_rs_recouple.py`, `/tmp/pa_edge_vs_local.py` (computed; numpy/mpmath, residuals to machine precision). Falsifier: three axes run, `scripts/numerics/witness/falsify.py`.

## The mandate
Over 𝔽_q one proof of purity (Weil II) routes through positivity of Rankin–Selberg L-functions. The audit (Worker E, `positivity-program.md` §L) found the **GLOBAL** RS/sym² positivity is **EDGE** (`Re s=1`), Euler-borne + independent, but **RH-silent on the line**. This pass attacks the **LOCAL ARCHIMEDEAN** version specifically: is the positivity of the **local archimedean factor** (`Γ_ℝ`, the `(p,q)` Hodge–Riemann form `P_∞` from M3) a SEPARATE input that supplies the **radius** (`|α|=√q` = `Re s=½`), distinct from the global edge positivity? Is M3's `P_∞` positivity exactly the local archimedean RS positivity, and is it genuinely new or the same wall?

## What was BUILT (concretely)
The **local archimedean RS pairing** as the Hodge–Riemann form of `Hom(V,V) = V ⊗ V^∨` at `∞`, on the weight-1 anchor `V = H^1(C)`:
- `[BUILT]` `P_∞(x,y) = S(C_W x, κ y)` on `H^{1,0}`, with `C_W = i^{p−q}`, `κ` the real structure, `S` the symplectic cup product. On the `g=1,2,3` anchor it is **positive-definite** (`min eig +2.32, +4.29, +7.98`), reproducing Riemann's second bilinear relation. This IS the local archimedean RS / `Γ_ℝ` Hodge L-factor positivity. **[= M3's `P_∞`, confirmed identical.]**
- `[BUILT]` The **decisive radius test** (the M4r modulus redistribution): genuine even-split moduli `{3,3,3,3}` (`|α|=√q=3`, `q=9`) vs determinant-neutral, pairing-neutral redistribution `{4.475, 2.011, 2.011, 4.475}` (`∏|α|=81` preserved, FE pairings `{9,9}` preserved). **`P_∞` is IDENTICAL for both** — its only inputs are `C_W` (a function of the `(p,q)` grading, never the moduli) and `κ` (the real structure). **`P_∞` is radius-rescale invariant**: under a uniform modulus rescale `α ↦ λα`, `min eig P_∞` is unchanged at `λ = 1, 2, 0.5`.

## The 𝔽_q anchor — the EXACT re-coupling (where phase and modulus join, and why `∞` can't)
`[BUILT]` Elliptic curves `E/𝔽_q` (`q=5,9`, traces `a=1,2,3,4`): the Frobenius eigenvalues `α,β` are roots of `x²−ax+q`. Purity `|α|=|β|=√q` splits cleanly into TWO facts:
1. **`αβ = q`** — the **FE / Poincaré pairing** (the EDGE, the *product* of moduli). **FREE** (FE-borne, the abscissa, the `‖f‖²` pole). Confirmed `αβ=q` for all.
2. **`|α|=|β|`** ⟺ `disc = a²−4q < 0` ⟺ `α,β` a **conjugate pair** — the **PHASE/reflection** ("roots are conjugate"). Over 𝔽_q this is supplied by **Deligne's positivity** (the Hodge index on the surface `C×C`), the RADIUS input. Confirmed `disc<0` for all (the Weil bound).

The coupling that turns (phase + edge) into the **radius** `|α|=√q` is the **Rosati relation `F F^† = q·Id`** — the constant field `q` (the SCALE) multiplied against the conjugation `F^†` (the PHASE). `P_∞` supplies the **phase factor** `C_W`/`κ` (= "roots are conjugate") but the **scale factor `q`** is exactly the **missing constant field at `∞`** (R8/R9 type obstruction: `Spec ℤ` has no finite constant field). At `∞` there is **no Frobenius `F`, no eigenvalues, no `disc` to force negative, no `q`** — so the map `q·Id = F F^†` that re-couples phase to modulus has **NO archimedean realization**.

## Is local-arch RS = the global edge wall? — DISTINCT objects, SAME fatal split
| object | place | carries | controls | DH | provable | radius? |
|---|---|---|---|---|---|---|
| **GLOBAL edge RS** (Worker E) | `s=1` | Euler/Satake | edge `Re s=1` (Siegel) | refuses | YES (indep) | NO (blind to line) |
| **LOCAL arch RS = M3 `P_∞`** | `∞` | `(p,q)`/phase `C_W` | the **phase** (roots conjugate) | **shared** | YES (anchor) | **NO (modulus-blind)** |
| **the RADIUS** `|α|=√q=Re ½` | — | needs **both halves coupled via `q·Id=F F^†`** | `Re s=½` | distinguishes | = Weil pos = RH | — |

They are **different objects** — one Euler-borne edge, one DH-shared archimedean — but share the fatal property: the local arch RS L-factor `L_∞(s, V⊗V^∨)` is **FE-symmetric about `Re s=½`**, so the locus it would mark is the **FE-fixed DH-shared locus** (R10 (b)); pinning the spectrum *to* it is Weil positivity = RH. The global edge controls the modulus at `s=1`; the local arch controls the phase at `∞`; **NEITHER pins `Re s=½`**, because that needs the phase and the scale `q` coupled, and the scale is the irreducibly-absent constant field.

## Anchor check (no zeros assumed)
**FAIL to recover `√q` independently.** `P_∞ > 0` holds for **every** weight-1 polarized HS regardless of any Frobenius modulus (radius-rescale invariant, computed). The radius `√q` is **not a function of `P_∞`**. Over 𝔽_q the `√q` comes from Deligne's positivity on the **surface** coupled to the constant field `q`, **not** from the local archimedean factor — which is the **same `Γ_ℝ` for every `q` and for DH**. `P_∞` anchors the **phase**, never the radius.

## Falsifier verdict (three axes, as a RADIUS candidate)
- **EULER-BORNE — NO.** `Γ_ℝ(s)=π^{-s/2}Γ(s/2)` is **literally identical** for ζ and Davenport–Heilbronn (both share the archimedean factor). `P_∞`, built from it, is **DH-shared** and cannot distinguish ζ from DH.
- **SEES-ZEROS — NO (for the radius).** `P_∞` sees the `(p,q)` **type/phase** but is **modulus-blind** (radius-rescale invariant). As a radius candidate it does not see the zero modulus.
- **INDEPENDENT — NO.** Radius-pinning = Weil positivity = RH.
- → `classify(False, False, False)` = **DISPERSING**.

This is **weaker than CIRCULAR**: the local archimedean RS positivity is not even a restatement of RH — it is the DH-shared `Γ`-factor, RH-NEUTRAL for the radius. (Distinguish from M3's own honest framing: `P_∞` is the *reality/phase half* of the build, correctly Euler-silent **by design**; the error this pass rules out is treating its positivity as the *radius* input. It is not.)

## Verdict
`[DECISION · DEAD_END]` — **M3's `P_∞` positivity IS the local archimedean Rankin–Selberg positivity** (the `Γ_ℝ` Hodge–Riemann form of `V⊗V^∨` at `∞`), built and confirmed positive-definite on the `g=1,2,3` anchor. It is a **DISTINCT object** from Worker E's global edge RS positivity (local/DH-shared vs global/Euler-borne) but is **NOT a new radius input**: it is **radius-rescale invariant** (modulus-blind, computed exact) and **DH-shared** (the same `Γ_ℝ` as Davenport–Heilbronn). The 𝔽_q anchor pinpoints why: purity = **phase** (roots conjugate, supplied by `C_W`/`κ`) **×** **scale `q`** (the modulus, supplied by the constant field), re-coupled over 𝔽_q by **`F F^† = q·Id`** (Deligne's surface positivity). `P_∞` supplies the **phase factor**; the **scale factor `q`** is exactly the **missing constant field at `∞`** (R8/R9). The local archimedean factor has **no Frobenius, no eigenvalue modulus, no `q`** — so the phase↔modulus re-coupling has **no archimedean realization**. **Not overclaimed:** this confirms the local arch RS positivity is the **phase half** of the keystone (correctly Euler-silent), and rules out the hope that it independently supplies the **radius**. It re-confirms the **count-vs-radius split** (M4r/R10) at the local archimedean RS level: the archimedean RS factor carries the **phase/type** (the analogue of "roots conjugate"), never the **modulus/radius** (which needs the absent constant field `q`).

## Why this is a DEAD_END, not a lead, stated exactly
A radius lever must (a) supply the modulus, (b) anchor `√q` on 𝔽_q without the zeros, (c) fail for DH. The local arch RS positivity does **none**: (a) it is modulus-blind (radius-rescale invariant, the M4r redistribution is invisible to it); (b) `√q` is not a function of it (anchored by Deligne's surface positivity + `q`, not by `Γ_ℝ`); (c) it is DH-shared. It is the **phase factor of a product whose scale factor is the irreducibly-absent constant field** — the same R8 type obstruction (cardinality/`q`), now localized at the RS-archimedean factor.

## Next concrete step (the one decidable question)
Does the re-coupling map `F F^† = q·Id` — the operator identity that joins `P_∞`'s phase to the modulus `√q` over 𝔽_q — admit ANY archimedean realization built from `C_W` + the duality `D` ALONE (no `q`, no Frobenius)? Equivalently: is there a Frobenius-free operator `Θ` at `∞` with `C_W Θ = Θ^* C_W` and `Θ Θ^† = ρ·Id` for a *derivable* scalar `ρ` (the would-be radius²)? **Decidable test:** on the anchor, attempt to solve `Θ Θ^† = ρ·Id` with `Θ` constructed only from `(V, F^•, D, κ)`; the prediction (R8/M4r) is that `ρ` is a **free scalar** (any `ρ>0` admits a solution) — confirming the radius is unconstrained without `q`. If instead some coherence forces a *unique* `ρ`, that `ρ` is the missing radius lever (highly unlikely; this would contradict M4r's redistribution theorem).
