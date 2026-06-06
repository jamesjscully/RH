# Proving the positivity `θFθ=F^*` independently — both on-ramps tested (2026-06-06)

**Item (AGENDA NEXT #1).** DONE #0 (`polarization_relation.py`) localized the entire RH gap to a
single REALITY condition on the symbol: `θFθ=F^*` ⟺ `m(1−s)=conj m(s)` ⟺ the scattering symbol
`M=Λ(2s−1)/Λ(2s)` unitary on the line / resonances on `Re s=¼` ⟺ RH. NEXT #1 names two concrete
on-ramps for proving this reality **independently** of RH. This pass makes both executable and runs
them through `falsify.py`.

Module: `scripts/numerics/witness/positivity_reality.py`. Falsifier: 2 rows in `falsify.py`.
Tags: **[THM]** / **[computed]** / **[honest-negative]**.

---

## On-ramp (a) — is the CC20 windowed positivity DEFECT the prime-sum off-diagonal?

**[THM]** CC20 (Connes–Consani 2020) prove the Sonin/scaling-compression positivity
`Tr(ϑ(g)Sϑ(g)*) ≥ 0` **only for test functions `g` supported in a window `|u| ≤ L`** (the corner
cutoff / "small square"). This windowed positivity is exactly the Weil explicit formula restricted to
the window:
`Σ_ρ ĝ(γ_ρ) = W_∞(g) − Σ_{n=p^k} Λ(n) g(log n)/√n`. Inside `|u|≤L` the prime sum is **finite**
(only `n=p^k` with `log n ≤ L`); the **uncertified DEFECT** is the out-of-window prime tail
`D(L) = Σ_{log n > L} Λ(n) g(log n)/√n`.

**[computed]** For a fixed Gaussian weight `g(u)=e^{−u²/2}` (no bare floats; mpmath dps=30,
von-Mangoldt `Λ(n)` over prime powers to `n≤2·10⁵`):

| window `L` | in-window certified prime sum | out-of-window DEFECT tail |
|---|---|---|
| 2.0 | +1.172797 | +0.168187 |
| 3.0 | +1.326049 | +0.014934 |
| 4.0 | +1.340371 | +0.000613 |
| 5.0 | +1.340973 | +0.000011 |

The defect is a genuine **von-Mangoldt prime sum** that shrinks as the window grows — it is exactly
`off_diagonal.py`'s `Tr F` (the arithmetic side of the explicit formula), i.e. the cross-place
coupling term.

**Identification.** `θFθ=F^*` (full Weil positivity, all `g`) reduces, **modulo the CC20
windowed-unconditional part**, to controlling the prime tail = `W_∞ ≥ Σ_p W_p`, the standing wall.
This is a **TRUE REDUCTION**, but it lands on the **OPEN** cross-place coupling.

**Verdict (a): CIRCULAR.** Euler-borne YES, sees-zeros YES, independent NO. The value is
**unification**: the CC20 finite-rank/windowed defect = the prime-sum off-diagonal = the standing wall
are **ONE object**. This pass and the wall are the same.

## On-ramp (b) — does the sym²/RS square-modulus `m=|h|²·phase` supply the reality?

`θFθ=F^*` is a **reality** condition on the symbol. The sym²/Rankin–Selberg structure (A4 of
`F-sym2-os-bridge`) writes a symbol as a **square-modulus times a phase**, `m = |h|²·phase`, with
`|h|²` the unconditional sym² norm-square. Does that make the reality automatic?

**[computed] — the decisive MODULUS/PHASE split** (mpmath dps=30, scattering symbol
`M=Λ(2s−1)/Λ(2s)`, FE-symmetric off-line plant `ρ₀=0.8+10i`):

- **The MODULUS is RH-SILENT.** `|M(½+it)| = 1` on the critical line for **BOTH** RH-true `M` **AND**
  the off-line plant `M_off` — verified `=1` to `<1e-10` at `t∈{6,12,20,30}`. This is forced by the
  functional equation `Λ(s)=Λ(1−s)` alone (scattering.py stone 1; holds verbatim for DH). The sym²
  norm-square `|h|²` lands here: a **modulus**, blind to zero locations.
- **The PHASE/WINDING is the line condition.** The off-line plant injects a resonance (pole of `M_off`)
  at `s=ρ₀/2`, with `Re = Re(ρ₀)/2 = 0.4 ≠ ¼` — a **phase event** (a winding of `arg M`, by the
  argument principle) that the modulus `|M|=1` cannot register.

So `m=|h|²·phase` fixes `|m|=|h|²` (the **modulus**, the EDGE positivity `Re s=1`, the `L(1,sym²)`
Siegel bound — unconditional) and leaves `arg m` (the **phase**, the LINE condition `Re s=½`,
the reality) **free**. The square-modulus controls the **wrong half**.

**Verdict (b): RH-SILENT.** Euler-borne YES (sym² needs Satake; DH-refuses), sees-zeros NO (the
modulus is FE-forced, blind to the resonance location), independent YES (`L(1,sym²)` Siegel bound).
This is the **SAME edge→line gap** as Worker E (`hecke_certificate.py`), now restated as
**MODULUS→PHASE**: the unconditional sym² positivity is the modulus/edge; the line is the phase the
square-modulus does not reach.

---

## Decisive finding

**Neither on-ramp supplies an independent proof of `θFθ=F^*`.**
- **(a) CIRCULAR** — a true reduction: the CC20 finite-rank/windowed defect IS the out-of-window
  von-Mangoldt prime tail = `off_diagonal.py`'s `Tr F` = the cross-place coupling `W_∞ ≥ Σ_p W_p`.
  So the reality reduces, modulo the unconditional windowed part, to that OPEN coupling. **Unifies this
  pass with the standing wall** (CC20 defect = prime-sum off-diagonal = one object).
- **(b) RH-SILENT** — the reality is a **PHASE** condition (arg `m` trivial); the sym² square-modulus
  supplies the **MODULUS** `|h|²` (the edge `L(1,sym²)` positivity). Decisive split: `|M|=1` on the
  line for both ζ and the off-line plant (FE-forced, RH-silent) while only the resonance location
  (phase) distinguishes them. The norm-square controls the **wrong half**.

**16th Euler-product confirmation.** First to test BOTH NEXT #1 on-ramps executably.

## What this sharpens (the next object)

The residual gap `θFθ=F^*` is now pinned to a **PHASE/reality condition** whose obstruction is
**EXACTLY the prime tail** (on-ramp a) — and the one unconditional positivity we have, the sym²
norm-square `|h|²` (on-ramp b), is provably the **MODULUS**, the wrong half. So an independent proof
must control the **PHASE `arg m`** (the winding / spectral count / argument principle) **from the prime
data** — a phase/argument-principle positivity, **not** a modulus/norm-square. This names the
pass-five target: a certificate for `arg m` (the winding), Euler-borne, that the sym² modulus
cannot give.

**Honest negatives recorded.** On-ramp (a) is a real reduction but circular (open coupling). On-ramp
(b)'s first crude sample (sampling `|M|` on `Re s=¼` near the planted pole) was misleading because
everything moves near a pole; corrected to the clean separation — `|M|=1` on the **critical line**
`Re s=½` (away from the planted pole) for both functions, isolating the modulus's RH-silence from the
phase's resonance event.
