# The polarization relation `F·F^†=c·Id` SPLITS at the archimedean place: the RELATION is the (free) functional equation, the POSITIVITY `†=*` is the whole problem (2026-06-06)

**Item (AGENDA NEXT #1).** DONE #0 (`frobenius_self_norm.py`) pinned the wall to a single operator
relation: build a `ℤ`-algebra `A` (would-be `End(S²/ℤ)`) with the explicit-formula prime-sum element
`F` and an involution `†` s.t. `F·F^† = c·Id` **unconditionally** (the polarization, `c=deg`), with `†`
**positive** (`F^†=F^*`, the Hilbert adjoint) being RH. Two named on-ramps: **(1)** Bost–Connes/QSM
modular `σ_t`; **(2)** CC20 Sonin/Toeplitz compression `SθS=(deg)·Id`. Task: do either supply the
relation, and is its `c` the polarization with positivity = RH?

**Module.** `scripts/numerics/witness/polarization_relation.py` (+ 2 `falsify.py` rows). Certified
(mpmath dps 30 / flint acb prec 200): the symbol closure `m(s)m(1-s)`, the DH kill-test of the relation,
and the resonance-location positivity test under a planted off-line zero.

## Finding [THM + computed + honest-negative]

**The polarization relation `F·F^†=c·Id` does NOT cross the wall — but it cleanly SPLITS the operator
identity into a free half and the whole problem.** Built on the archimedean model where on-ramp (2)
actually lives: `H = L²(ℝ₊*, du/u) ≅ L²(Re s=½)`, with `θ` = multiplicative inversion `f(u)↦f(1/u)`
(= the FE `s↦1−s`, `θ²=Id`), the scaling flow `U_λ`, and `F` = the Weil/explicit-formula operator =
multiplication by a symbol `m(s)`.

| half of `F·F^†=c·Id` | what it is | unconditional? | sees zeros? | falsifier |
|---|---|---|---|---|
| **RELATION** `F·F^†=c·Id` | `F^†:=θFθ` ⟹ `F·F^†` = mult by `m(s)m(1−s)`; `=c` ⟺ **unitary FE** `\|m\|=√c` on the line | **YES** (it IS the FE) | **NO** | **DISPERSING** |
| **POSITIVITY** `θFθ=F^*` | `m(1−s)=conj m(s)` ⟺ resonances on `Re s=¼` | — | **YES** | **CIRCULAR** |

**Load-bearing computation [computed].** Take the scattering symbol `M(s)=Λ(2s−1)/Λ(2s)`
(`scattering.py`; its poles are the zeros at `ρ/2`).
- **RELATION:** `M(s)M(1−s)=1` (the polarization closure) holds to `~1e-31` for **both** the RH-true
  symbol **and** a planted off-line-zero plant (`ρ₀=0.8+10i` + FE quadruple). It follows ONLY from the
  functional equation `Λ(s)=Λ(1−s)`. **Davenport–Heilbronn kill-test:** DH has a functional equation
  too, so `m_DH(s)m_DH(1−s)=1` holds (verified to `1e-9` at `t=3,10,85.699`, incl. near the *known
  off-line DH zero* `β=0.8085`). **⟹ the RELATION holds verbatim for the RH-FALSE function: RH-SILENT
  / DISPERSING.**
- **POSITIVITY:** the resonance (pole of `M` at `ρ/2`) sits on `Re s=¼` ⟺ `ρ` on the line. The off-line
  plant moves a resonance to `Re s = Re(ρ₀)/2 = 0.4 ≠ ¼` — breaking the positivity exactly when RH
  fails. **⟹ sees-zeros YES, but `θFθ=F^*` = Weil/CC20 positivity over `ℤ` = RH: CIRCULAR.**

## Why this answers the agenda question

**The two on-ramps SHARPEN, not cross, the wall — and they answer the agenda's literal question NO with
a precise reason.** The polarization relation `F·F^†=(deg)·Id` at the archimedean place **is the
functional equation `m(s)m(1−s)=c`**, a *free unitarity*, NOT a missing structure. So `F^†=(deg)F^{-1}`
already exists over `ℤ`/at `∞` — it is the FE reflection conjugation `θFθ`. What is missing is **not the
relation but an INDEPENDENT proof of the POSITIVITY `†=*`** (`m(1−s)=conj m(s)`, resonances on the
line), which is exactly the open Weil/CC20 positivity.

This **localizes the gap WITHIN the operator identity**: over `𝔽_q`, the algebra `End(Jac)` supplies
**both** the relation (`F^†=qF^{-1}`, the polarization) **and** its positivity (`F^†=F^*`, the Rosati
positivity) — both theorems. Over `ℤ`/`∞`, the **relation half is free** (the FE), but the **positivity
half is the whole problem**. The wall is therefore not "construct the algebra with the polarization
relation" — that relation is the FE — it is "prove the positivity `†=*` independently," i.e. the same
Weil positivity, now seen to be the *unique residual* content of the operator identity.

### On-ramp (1) — Bost–Connes `σ_t` — classified
The BC modular automorphism `σ_t = Ad(Z^{it})`, `Z=ζ` (the partition function), is INNER and unitary.
The polarization `F·F^†=c·Id` from `σ_t` is the **KMS/modular unitarity** — holds for ANY KMS state,
RH-independent (and `qsm_free_energy.py` already showed BC free-energy positivity is real-axis-only,
**RH-SILENT**). Its positivity (`†=*`, the state being a trace / the Hilbert adjoint = the FE
reflection) is again RH. **Same split as on-ramp (2).**

### On-ramp (2) — CC20 Sonin/scaling — classified
`SθS=(deg)·Id` is the statement that on the Sonin compression the symbol product `m(s)m(1−s)` is a
scalar — i.e. **the unitary functional equation**. Confirmed above: a scalar unconditionally (the FE),
RH-silent (holds for DH). The Sonin compression does not change this: the scaling-flow adjoint `θFθ`
is the FE reflection, free; the compression's *positivity* (CC20's actual content) is the open Weil
positivity at `∞`.

## Falsifier verdict (two halves, both registered)

- **RELATION `F·F^†=c·Id`:** Euler-borne NO (the FE / unitarity holds for DH) · sees-zeros NO ·
  → **DISPERSING.**
- **POSITIVITY `θFθ=F^*`:** Euler-borne YES · sees-zeros YES (resonance off `Re s=¼`) · independent NO
  (= Weil positivity over `ℤ`) → **CIRCULAR.**

**15th Euler-product confirmation. Honest negative:** neither on-ramp crosses the wall; both reveal the
polarization relation to be the (free) functional equation. **First to localize the gap WITHIN the
operator identity:** the relation half is free, the positivity half is the entire problem. This is a
genuine sharpening — it removes "construct the polarization relation" from the to-do list (it is the
FE) and pins the residual to the single positivity `†=*`.

## What this surfaces for the next pass

The wall is now: **prove `θFθ=F^*` (equivalently `m(1−s)=conj m(s)`, resonances on the line)
independently of RH, at the archimedean place.** This is the CC20 Sonin-space positivity. Two concrete
questions:
1. CC20 prove the Sonin/scaling-compression positivity **up to a finite-rank defect** (the low-lying
   zeros) — is that defect the same "off-diagonal `Tr F` / prime sum" residual (off_diagonal.py), i.e.
   does the archimedean positivity `θFθ=F^*` reduce, modulo the unconditional part, to the **cross-place
   coupling `W_∞ ≥ Σ_p W_p`**? (This would *unify* this pass with the standing wall.)
2. The relation being the FE means the eigenvalue/Frobenius operator `F` and its inversion-adjoint are
   *simultaneously* multiplication operators (commuting) on the Mellin line. Positivity `θFθ=F^*` is
   then a **reality** condition on a multiplication symbol — does the **sym²/Rankin–Selberg norm-square**
   (A4 of `F-sym2-os-bridge`) supply that reality as a *square-modulus* `m=|h|²·(phase)`, making
   `θFθ=F^*` automatic? This reconnects directly to the OS/A4 thread.

---

### References
- Connes–Consani, *Weil positivity and the trace formula, the archimedean place*, arXiv:2006.13771
  (Selecta Math. 2021) — the Sonin-space compression of the scaling action.
- Connes–Moscovici, *The UV prolate spectrum matches the zeros of zeta*, PNAS 2022; arXiv:2112.05500.
- Bost–Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry
  breaking in number theory*, Selecta Math. 1995 — the `σ_t = Ad(ζ^{it})` modular flow.
- `scripts/numerics/witness/scattering.py` (the scattering symbol `M(s)=Λ(2s−1)/Λ(2s)`, `|S|=1`
  RH-neutral); `frobenius_self_norm.py` (the `𝔽_q` split this confirms at `∞`); `qsm_free_energy.py`
  (BC positivity RH-silent).
