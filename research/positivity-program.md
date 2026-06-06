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
| reflection positivity (OS/QFT) | *thread 1* | **RH-neutral UNLESS the reflection acts on the prime/adelic structure**; the Weil form is already a Hankel-positivity problem (CC20). The prime-place reflection `θ` is the open object — **live** |
| automorphic / RTF positivity | *thread 4* | **dispersing** — period/Waldspurger positivity is central-value (`L(½)≥0`), not zeros; not Euler-borne; fails DH (termwise on the GL(1) summands). DEMOTED |
| QSM / KMS (Bost–Connes) | *thread 5* | **the one new lever** — Euler-borne AND *DH-refusing* (QSM can't represent DH at all). But real-axis, **RH-silent** (doesn't see the zeros). **Live, the strongest candidate** |
| naive Yamabe / conformal Laplacian | wrong sign | dead (negative curvature) |

## D. Honest framing
This is decades-deep foundations work; we are not going to construct `h_∞` in an afternoon. The point
of this file is to (1) keep every live thread, (2) grow the auditor so we always know exactly which
structures transfer and where they break, and (3) run every candidate positivity through the kill-test
so we never re-walk a locked door. When a thread surfaces a genuine new positivity lever, it goes
through the scaffold *first*.

---

## E. Durable lessons from the thread audit (2026-06-06)

1. **The Euler product is the *sole* discriminator — now 6 independent confirmations.** Archimedean,
   functional-equation, spectral (self-adjoint), period/automorphic, GUE/determinantal, and conformal
   data are ALL RH-neutral — they hold verbatim for Davenport–Heilbronn. **Corollary (a hard filter):
   any positivity not built on the Euler product is dispersing.** Every thread re-derived this.
2. **The knife-edge (thread 0, the cleanest statement of *why*).** CC20's archimedean positivity is
   NOT self-sufficient: it *loses* positivity on intervals and is restored **only by the exact prime
   `p=2`** — the sign fails outside a window of size `<10⁻³` around `p=2`. It needs the *actual
   arithmetic prime, not a nearby real*. That is the BGS §6.3 corner obstruction, localized.
3. **QSM/KMS is the only genuinely new lever (thread 5).** The Bost–Connes free-energy positivity with
   `Z(β)=ζ(β)=∏_p(1−p⁻ᵝ)⁻¹` is the *only* candidate that is Euler-borne **and** DH-*refusing* (it
   doesn't represent DH at all). Its limit: it lives on the real `β`-axis and is **RH-silent**.
4. **Reflection positivity needs a prime-place reflection (thread 1).** RP is RH-neutral on the
   archimedean/scaling geometry; the open object is an involution `θ` acting on the **prime** places
   making the Weil form `W=⟨θh,h⟩` an OS pairing. The Weil form is already a Hankel-positivity problem.
5. **Geometry home = condensed; prismatic is orthogonal to `∞` (threads 2+3).** The condensed
   stack-of-norms over the extended Berkovich spectrum is the closest existing compactified corner
   (with archimedean coherent duality + an "archimedean Deligne–Illusie ⟶ Kähler" open question that
   is *our* target). Prismatic/q-de Rham is a **finite-place** theory (`q=1` = cyclotomic, not `∞`) —
   **shelved**.
6. **RTF/Langlands is dispersing for *zeros* (thread 4).** Its positivity is central-value, downstream
   of RH; beyond-endoscopy reaches poles, not zeros. Demoted.

## F. The convergent lead, and the next directions

**Threads 1, 5, and 6 converge on one target:**

> **A reflection-positive continuation of the Euler-product free energy `F(β) = −log ζ(β)` from the
> real `β`-axis (where its KMS/convexity positivity is Euler-borne and DH-refusing) to the critical
> line — made to *see the zeros*, with a DH surrogate that *breaks* it.**

This is the first new, Euler-borne, DH-refusing, kill-testable lever the audit produced. Next
directions (workers spawned 2026-06-06):

- **(A) The convergent lead — QSM free-energy reflection positivity.** Build `F(β)=−log ζ(β)`, its
  real-axis KMS convexity, the continuation through `β=1` toward the symmetric point, the reflection
  structure, and the DH-surrogate kill-test. *Does it see the zeros, or stall on the real axis?*
- **(B) The prime-place reflection / adelic Hankel form.** Write `W = W_∞ + Σ_p W_p` as a Gram/Hankel
  matrix; search for the prime-place involution `θ` making it OS; kill-test against DH on the existing
  scaffold.
- **(C) Semilocal `{∞,2}` positivity (CC20 extension).** The minimal place-crossing: does the `ℚ_2`
  term enter CC20's trace-remainder with the sign keeping `Id−K` positive? Kill-test: ζ has `(1−2⁻ˢ)`,
  DH does not → predicted to fail for DH.
- **(deferred) Δ·Δ on the condensed stack of norms** — the geometric home; more abstract, queued.

The unifying question across A/B/C: **how does the Euler product enter a positivity that sees the
zeros** — the place-crossing. All three are kill-testable against DH on `weil_form.py` /
`scattering_forcing.py`.

## G. Thread 6 (two-worlds merger) — folded in
The merger (Connes–Consani Arithmetic⊕Scaling Site; Deninger foliated systems) is genuinely both
worlds, and the two positivities **unify at "trace = intersection"**: `Q(f) = −(D_f·D_f) = ‖Pf‖²`
makes Hodge-index negativity and operator self-adjointness the *same number* — **proven at the single
archimedean place (CC20)**. It does **not** globalize: the merger **inherits both obstructions and they
coincide** — no `H¹(S²)` (geometric), continuous-Frobenius `Δ·Δ=∞` (the Janus corner), resonances ≠
self-adjoint eigenvalues (non-compact; Selberg-RH needs *compact*). Net: the merger is the **tightest
localization** of the wall — RH ⟺ globalize CC20 past one place — triangulated from three directions
(Hodge square / Selberg spectral / scattering resonances) onto one functional. **Concrete kill-test
(thread 6):** express `Q(f)` two ways — (A) scaling-compression trace `Tr(ϑSϑ*)`, (B) Birman–Krein
scattering-phase `d/dt arg S(½+it)` — and test the equality `(A)=(B)` against `S_offline`. If the
off-line control passes both, the bridge is RH-neutral and the forcing is pinned to a specific
**cross-place term** of the semilocal trace formula; if it fails, that term is the first Euler-borne
forcing object. Needs no `H¹(S²)`; immediately falsifiable.

**All roads now lead to one place:** the **cross-place (archimedean↔prime) term** of the semilocal
trace formula — the Euler-product coupling that must enter a positivity seeing the zeros. Workers
A/B/C are three on-ramps to it.

## H. Worker results A/B + the falsifier upgrade (2026-06-06)

**Worker A (QSM free energy)** — `qsm_free_energy.py`, `research/work/A-qsm-free-energy.md`.
Real-axis KMS positivity of `F(β)=−log ζ(β)` is **certified, Euler-borne, DH-refusing** — but the
continuation does NOT see the zeros (the OS-positive KMS correlator is positive from `Λ(n)≥0` alone,
independent of where ζ vanishes). **Verdict: RH-SILENT.**

**Worker B (prime-place reflection)** — `prime_reflection.py`, `research/work/B-prime-reflection.md`.
No prime-place involution `θ` exists: `u↦−u` is exactly the archimedean reflection; the only reflection
the primes carry is the Gram doubling `W_p=P_pP_pᵀ` whose OS-positivity is identically `sign Λ` — the
Euler product in a Hankel skin. Discriminates ζ/DH but at the coefficient level. **Verdict: RH-SILENT
(thread-1 prime-`θ` closed negatively, 6th Euler-product confirmation).** Bonus: the Birman–Krein
phase winding `(1/2π)∮ d arg S(½+it)` DOES see an off-line zero (ζ:−12.96, off-line:−14.92) — counts,
doesn't force.

**Both hand off to the same object:** the cross-place margin `W_∞ ≥ Σ_p W_p` continued to the critical
line (= thread 0 / Worker C).

**The falsifier upgrade — `scripts/numerics/witness/falsify.py`.** The audit forced a third axis. A
candidate is now scored on:
1. **Euler-borne** (fails for DH) — necessary, *cheap*;
2. **sees-zeros** (sensitive to a planted off-line zero — depends on zero LOCATIONS, not just real-axis
   coefficients) — the **new, decisive axis** (`offline_sensitivity`);
3. **independent** (provable without assuming RH).

Verdicts: **DISPERSING** / **RH-SILENT** (Euler-borne but blind to the zeros — the new category that
catches QSM & prime-Gram) / **CIRCULAR** (= Weil/Li) / **FORCING** (the prize, still empty). Lesson
baked into tooling: *passing the DH kill-test is necessary but cheap; the content is sees-zeros.* Run
every future candidate through all three axes via `falsify.py` before believing it.

## I. The continuation problem — the approach (2026-06-06)

The audit isolated RH to the **continuation of the Euler-borne positivity across the archimedean↔prime
divide**. Stated precisely: the explicit formula is a **Fourier/Poisson duality** between the prime
scales `{log p^k}` and the zeros/archimedean spectrum; the Weil positivity `Σ_ρ|φ̂(γ)|² = W_∞(φ) −
Σ_p W_p(φ) ≥ 0` is a **sign-uncertainty inequality** under that duality (a function and its transform
cannot both concentrate against the primes without archimedean spectral cost).

**Lead approach — Fourier optimization → exact interpolation (the Viazovska-era machinery).** This is
exactly the problem class revolutionized post-2016:
- classical: Beurling–Selberg extremal functions in the explicit formula (partial/conditional);
- LP bound: Cohn–Elkies + the Bourgain–Clozel–Kahane sign-uncertainty;
- the lever: **Radchenko–Viazovska Fourier interpolation + Viazovska modular magic functions** (exact
  extremals where only LP bounds existed; solved sphere packing dims 8, 24).

The bet: an exact **modular** magic function for the explicit-formula sign-uncertainty would be
**Euler-borne** (modular forms carry the primes — *not* RH-silent) AND **sees-zeros** (interpolation
nodes = the zeros) — the first candidate that could fill the empty **FORCING** slot. Worker D is on it.

**Complementary handles.** (i) The **Hankel moment problem** — Weil form is Hankel (worker B), so RH ⟺
the Li sequence is a Hamburger moment sequence ⟺ a positive spectral measure exists; the continuation
= constructing it. (ii) The **dBN flow** (set aside) — the dynamical version of the same continuation.

**Discipline.** Any continuation candidate must clear all three `falsify.py` axes; Euler-borne +
sees-zeros is the bar (QSM/prime-Gram failed at sees-zeros). The Fourier/modular route clears both by
construction — so it fails *honestly* (FORCING or a located wall), not RH-silently.
