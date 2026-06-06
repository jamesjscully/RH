# The positivity program — threads + the analogy auditor (living, opened 2026-06-06)

The construction (`the-lift-program.md`) isolated the entire difficulty to **one positivity**: a
geometric proof that the Weil operator is `⪰ 0` (`λ_n ≥ 0`), equivalently the **equivariant global
extension of CC20's archimedean positivity to the primes** = a positive Green form / metric `h_∞`.
This file keeps the live threads toward that positivity, and grows the **analogy auditor** — a
mechanical record of which function-field structures transfer (and where they break) and which
positivity mechanisms survive the kill-test (fail for DH/Epstein, see the Euler product).

**Standing kill-test (the falsifier).** Any candidate positivity mechanism must (a) be Euler-product-
borne, (b) fail for Davenport–Heilbronn (same `Γ_ℝ`, off-line zeros) and Epstein, (c) not reduce to
the assumed `λ_n ≥ 0` (circular) or to a known graveyard route. Scaffold: `scattering_forcing.py`
(`λ_n`, `S_offline`), `weil_form.py` (PSD ⟺ RH), `harness.py`.

---

## A. The threads (do not lose sight)

| # | thread | the positivity hypothesis it offers | status / next |
|---|---|---|---|
| **0** | **CC20 global/equivariant extension** | the archimedean `W_∞ ≥ Tr(ϑSϑ*) ≥ 0` extended past one place, equivariantly, to dominate the primes | the *live edge*. Next: state-of-art since 2020 — what's been tried, where it stalls |
| **1** | **Reflection positivity** (OS / QFT / stat-mech) | RH = Osterwalder–Schrader/reflection positivity of a Euclidean field theory or stat-mech model; GUE is the hint | underexplored positivity source. Next: is there a reflection-positive model whose OS-positivity = Weil positivity? |
| **2** | **Condensed / analytic geometry** (Clausen–Scholze) | the *foundations* for archimedean coherent cohomology + duality on the arithmetic site (the liquid/analytic structure) | right framework, untried here. Next: can it define `H¹(S²)` + the archimedean Green form with the right sign? |
| **3** | **Prismatic / q-de Rham** (Bhatt–Scholze) | a cohomology unifying the local theories; the dream is an *archimedean prism* giving `H¹` over `\overline{Spec ℤ}` | speculative bridge. Next: is there an archimedean/global prismatic analog, and does it carry a positivity? |
| **4** | **Langlands / relative trace formula** | the positivity of the automorphic spectral side / relative-trace-formula periods (beyond-endoscopy) | huge, diffuse. Next: does any RTF positivity specialize to the Weil positivity for ζ and fail for DH? |
| **5** | **Noncommutative geometry** (Connes) | the operator/spectral-triple positivity; the BC-system / QSM KMS positivity | mature, stalls at positivity. Next: where exactly does the NCG positivity stall, and is QSM-KMS a genuine new lever? |
| **6** | **The two-worlds merger** (function-field ⊕ Selberg) | RH is *proven* in two worlds — function fields (geometric: Frobenius+Hodge) and hyperbolic/Selberg (spectral: self-adjoint Laplacian). The object is their **fusion**, and the merger forces the positivity neither has alone | the cross-cutting bet (our conformal-scattering work showed they meet at the archimedean conformal boundary). Next: what *exactly* must an object be to be both at once, and where do the two positivities (Hodge / spectral) become one? |

## B. The analogy auditor — function-field → ℤ dictionary (transfers / breaks)

| function-field structure | over `ℤ` | status / breakpoint |
|---|---|---|
| Frobenius `Fr` (discrete) | scaling `ℝ₊^*` (continuous) | **breaks**: continuous group contains the identity ⟹ `Δ·Δ=∞` (`lift_obstruction.py`) |
| `H¹_ét` (curve) | CC2023 `H¹` over 𝕊 [THM] | transfers on the **curve**; not on the square |
| `C×C` (projective surface) | the square `S²` | **breaks**: no `H¹(S²)`; `Ψ_λ` don't lift to two variables |
| Poincaré/Serre duality = FE | CC2023 Serre duality [THM] | transfers on the curve |
| Lefschetz trace = explicit formula | Weil explicit formula [THM] | transfers (analytically) |
| ample cone / polarization | the archimedean metric `h_∞` | **breaks/open**: positive Green form can fail (BGS §6.3) |
| Hodge index `(D·D)≤0` ⟹ RH | the Weil positivity `λ_n≥0` | **the wall** — RH itself; the whole program reduces here |

*(Auditor grows as threads report: each adds rows for the structure it builds and the exact breakpoint.)*

## C. The positivity-candidate tracker (kill-test status)

| positivity mechanism | kill-test | verdict |
|---|---|---|
| Hodge index / Kähler | — | right idea; blocked by non-compact corner (`Δ·Δ=∞`) |
| self-adjointness (Hilbert–Pólya) | reflects not forces | **RH-neutral** (stone 1); resonances ≠ self-adjoint eigenvalues |
| de Branges reproducing-kernel | over-proves | **falsified** (Conrey–Li 2000) |
| Nyman–Beurling / Hardy | holds for DH | **dispersing** |
| naive Yamabe / conformal Laplacian | wrong sign | **dead** (object is negatively curved) |
| reflection positivity (OS/QFT) | *thread 1* | **untested** — most promising unexplored source |
| automorphic / RTF positivity | *thread 4* | **untested** |
| QSM / KMS (BC system) | *thread 5* | **untested** |

## D. Honest framing
This is decades-deep foundations work; we are not going to construct `h_∞` in an afternoon. The point
of this file is to (1) keep every live thread, (2) grow the auditor so we always know exactly which
structures transfer and where they break, and (3) run every candidate positivity through the kill-test
so we never re-walk a locked door. When a thread surfaces a genuine new positivity lever, it goes
through the scaffold *first*.
