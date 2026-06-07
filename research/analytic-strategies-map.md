# Mapping the analytic side: which roads to RH are foreclosed, which are open (2026-06-06)

We proved the **geometric** strategy for RH is foreclosed (`WRITEUP-geometric-obstruction.md`: Theorem A,
the char-0 contradiction; Theorem B′, a similitude underdetermines the signature). By elimination, if RH is
provable, the proof lives on the **archimedean / analytic / char-0 side**. This document maps that side the
same way: for each analytic strategy, state its **prerequisite** and classify it as **CONTRADICTORY** (a real
no-go, e.g. de Branges/Conrey–Li), **CIRCULAR** (= RH restated, e.g. Weil positivity), or **UNCONSTRUCTED**
(an open road — name the precise missing object).

## The unifying question (forced by Theorem B′)

Theorem B′ proved: **the positivity that is RH (`F†=F̄`, the `(d,0)` signature) is NOT forced by any
structural/algebraic datum** (duality, similitude, coherence) — off-line worlds are structurally consistent.
Therefore **any genuine proof of RH must supply that positivity from *analysis*** — estimates, a constructed
self-adjoint operator, a measure-theoretic positivity — *outside* the structural data. So for each strategy:

> **Positivity source:** does it supply the RH-positivity from a genuine **new analytic source** (a live road),
> or does it **reduce to the circular Weil positivity** (the audit wall), or is its prerequisite
> **contradictory** (a no-go)? The live road is: *unconstructed analytic object, not contradictory, with a
> positivity source independent of the structural data.*

## Anchor + falsifier (kept)
- **Anchor:** the function-field analogue — over `𝔽_q(C)` RH is Weil's theorem; does the strategy have a
  function-field version, and is its analytic content there a theorem or vacuous?
- **DH:** fails for Davenport–Heilbronn (no Euler product). `[established]/[partial]/[heuristic]`.

## The strategies (to be mapped)
- **(HP) Hilbert–Pólya** — a self-adjoint operator `H` with `spec(H) = {γ : ζ(½+iγ)=0}`. Prerequisite: `H`.
  Contradictory or unconstructed? (Bare self-adjointness is RH-neutral; is *a canonical* `H` impossible or
  merely unbuilt?)
- **(dB) de Branges / Conrey–Li** — a Hilbert space of entire functions whose structure forces real zeros.
  Conrey–Li proved de Branges's *specific* positivity hypotheses incompatible with known facts about `ζ`.
  Map precisely: is this a no-go for the *whole* de Branges program or only the specific version?
- **(BN) Beurling–Nyman** — RH ⟺ the indicator `1_{(0,1)}` lies in the `L²(0,1)`-closure of
  `span{ρ(θ/x)}` (fractional parts). Prerequisite: the approximation. Contradictory, circular, or open?
- **(W) Weil positivity / explicit formula** — RH ⟺ the Weil functional `W(f)=Σ_ρ \hat f(ρ) ≥ 0`. The audit:
  CIRCULAR. Confirm and state the precise reason (the positivity IS RH).
- **(BK) Berry–Keating / quantum chaos** — the zeros as eigenvalues of a quantization of `xp` / a chaotic
  Hamiltonian. Prerequisite: the quantization (a self-adjoint operator with the right spectrum + dynamics).
  Heuristic; contradictory or unconstructed?
- **(C) Connes trace formula / spectral realization** — the explicit formula as a trace over the adèle class
  space; the zeros as an *absorption* spectrum. Prerequisite: the trace positivity = the Weil positivity.
  Circular or a genuine new analytic source?

## Endpoint
A complete two-sided map: the geometric roads (closed, by Theorems A/B′) and the analytic roads (each
classified contradictory / circular / open), with the **live analytic road(s)** named precisely — the
unconstructed analytic object whose construction would supply the RH-positivity that no structure can.
