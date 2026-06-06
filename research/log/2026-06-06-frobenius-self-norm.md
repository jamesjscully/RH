# The Frobenius self-norm `⟨F,F⟩=deg(F)` splits into an RH-silent number and a circular form, separated by ONE polarization relation (2026-06-06)

**Item (AGENDA NEXT #1).** What gives `⟨F,F⟩=deg(F)` — the Frobenius self-norm, the one Rosati-Gram
entry with no unconditional `ℤ`-meaning (off_diagonal.py) — an unconditional `ℤ`-meaning (a Frobenius
self-intersection/degree independent of the zeros)? Named handles: (a) Arakelov self-intersection /
BGS positive-Green-form; (b) the `q→1`/condensed limit of the `𝔽_q` degree `2q`, entering as a FORM's
diagonal (DONE #2 caveat).

**Module.** `scripts/numerics/witness/frobenius_self_norm.py` (+ two `falsify.py` registry rows).
Certified: exact integer adjunction numbers; the divergence test under a planted off-line zero.

## Finding [THM + computed + honest-negative]

`⟨F,F⟩=deg(F)` does **not** have a single `ℤ`-meaning. It **splits into two inequivalent objects** that
coincide over `𝔽_q` *only because RH holds there*:

| reading | definition | value over `𝔽_q` | sees an off-line zero? | falsifier |
|---|---|---|---|---|
| **ALGEBRAIC** (Rosati / Arakelov) | `⟨F,F⟩ = Tr(F·F^†)`, `F^† := q·F^{-1}` | `2gq` | **NO** (RH-blind) | **RH-SILENT** |
| **HILBERT** (spectral / CC20) | `⟨F,F⟩ = Tr(F·F^*)`, `F^* =` conj-transpose | `Σ_i|α_i|²` | **YES** | **CIRCULAR** |

**The load-bearing computation [computed].** `g=2, q=7`, `2gq=28`. On the circle (`|α|=√q`, RH) both
readings give `28.0`. Plant **one** off-line pair `(r=2, q/r=3.5)` respecting the FE (radii multiply to
`q`): the **algebraic stays `28.0`** (it uses only the polarization degree `q` via `F^†=qF^{-1}`,
blind to where `α` sits); the **Hilbert jumps to `30.25`** (it is `Σ|α|²`, which sees the zero). They
**agree iff `|α_i|²=q` for all `i` = RH = positivity of the Rosati involution** (`F^†=F^*`).

**Adjunction control [THM, exact integers].** The geometric self-intersection of the Frobenius graph on
`C×C` is `Γ_F·Γ_F = (2p_a−2) − K_S·Γ_F = (2g−2) − (2g−2)(q+1) = q(2−2g)`, verified exactly for
`g∈{1,2,3}, q∈{5,7,9}`. The Rosati self-pairing `Tr(F·qF^{-1}) = q·Tr(Id_{2g}) = 2gq`, verified for a
random Frobenius-like `F` with `det F = q^g`. Both are computed from `(g,q)` **alone** — RH-independent.

## Why this answers the agenda question

The unconditional value `2gq` exists over `𝔽_q` **only because the algebra `End(Jac)` supplies the
relation `F^† = q·F^{-1}`** — i.e. `F·F^† = q·Id` as an **operator identity** in an algebra, where the
`q` is the **degree of the polarization** (geometric data, not zero data). The Rosati involution's
**positivity** (`F^†=F^*`) is then exactly RH.

So **"what gives `⟨F,F⟩` an unconditional `ℤ`-meaning"** = **"construct an algebra `End(S²/ℤ)` carrying
a POSITIVE Rosati involution `F^† = (deg)·F^{-1}`"** — the *same* missing correspondence algebra
(off_diagonal.py), now **pinned to a single operator relation** `F·F^† = (deg)·Id`. This is a genuine
sharpening: the wall moves from "the self-norm is missing" to "the **polarization relation**
`F^† = (deg)·F^{-1}` is missing."

### Handle (a) — the Arakelov route — classified

- **Faltings–Hriljac** `⟨D,D⟩_Ar = −ĥ_NT(D,D)` (Faltings 1984 / Hriljac 1985): an **unconditional
  `ℤ`-valued self-intersection** (a theorem, negative-definite on the primitive part). **But** it is the
  Néron–Tate height of a *point* on `J(X_K)` of a **fixed** curve — **no `ζ`-zeros enter** (the "wrong
  divisor", `arakelov-arithmetic-surface.md` §2.4). It is the **ALGEBRAIC / RH-SILENT** type: it has the
  unconditional value, blind to the zeros. This is precisely the same RH-silent flavor as `deg·χ`
  (DONE #2).
- **CC20 archimedean diagonal** `Δ·Δ_arch = W_∞(g*g^*)` (Connes–Consani 2006.13771): **does** carry the
  zeros (= the explicit-formula sum), but its positivity is the **open BGS Cor. 6.3.2 / Weil-positivity**
  condition (a positive Green form, which BGS prove can *fail*). The **CIRCULAR / forcing-shaped** type.

### Handle (b) — `q→1` of `2gq`

A bare number `2g·|F₁|` (RH-silent, DONE #2) unless it enters as the self-intersection **FORM's**
diagonal — and the form's positivity is again `Rosati = adjoint = RH` (CIRCULAR). The caveat from DONE #2
holds: a scalar limit is RH-silent.

## Falsifier verdict (two readings, both registered)

- **ALGEBRAIC/Arakelov reading:** Euler-borne NO (pure topology×base-size, `h_NT` of a fixed curve) ·
  sees-zeros NO (RH-blind: `28.0→28.0`) · independent YES (a theorem). → **RH-SILENT.**
- **HILBERT/CC20 forcing reading:** Euler-borne YES · sees-zeros YES (`28.0→30.25`) · independent NO
  (algebraic=Hilbert IS RH). → **CIRCULAR.**

The two are separated by **exactly** the polarization relation `F^† = q·F^{-1}`. **14th Euler-product
confirmation.** Honest negative: neither named handle (a Arakelov, b `q→1`) crosses the wall — both
supply the unconditional *value* but only in the **RH-silent (wrong-divisor) channel**; the forcing
channel (CC20 archimedean diagonal) remains the open BGS §6.3 positivity.

## What this surfaces for the next pass

The wall is now a **single operator relation**, not a missing object: build a `ℤ`-algebra `A` (the
would-be `End(S²/ℤ)`) with an element `F` (the explicit-formula prime-sum operator) and an involution
`†` such that `F·F^† = c·Id` **unconditionally** (the polarization), with `†` **positive**
(`F^†=F^*` = the Hilbert adjoint) being RH. Two concrete questions this poses:
(1) the **Bost–Connes / QSM algebra** already has `ℤ`, a `ζ`-partition function, and an involution — does
its `F·F^†` close to a scalar (a `KMS`/modular relation `σ_t`), and is the resulting `c` the polarization?
(2) does the **CC20 Sonin/Toeplitz** compression furnish `F^† = (deg)·F^{-1}` as the scaling-flow
adjoint — i.e. is `S θ S = (deg)·Id` on Sonin's space the missing operator identity?

---

### References
- Faltings, *Calculus on arithmetic surfaces*, Ann. Math. 119 (1984) — `⟨·,·⟩_Ar = −ĥ_NT`.
- Hriljac, *Heights and Arakelov's intersection theory*, Amer. J. Math. 107 (1985).
- Bost–Gillet–Soulé, *Heights of projective varieties and positive Green forms*, J. AMS 7 (1994), §6.3.
- Connes–Consani, *Weil positivity and the trace formula, the archimedean place*, arXiv:2006.13771.
- `research/literature/arakelov-arithmetic-surface.md` (the "wrong divisor" §2.4);
  `scripts/numerics/witness/off_diagonal.py` (DONE #1, the self-norm localization).
