# AN-HP — Hilbert–Pólya: a self-adjoint `H` with `spec(H) = {γ}`. Verdict: OPEN_ROAD (operator unbuilt, not forbidden), with its only *constructed* instance (Connes–Moscovici) CIRCULAR (self-adjointness = Weil positivity).

**Charter:** `research/analytic-strategies-map.md` (strategy HP), `research/positivity-program.md` (the audit, Tracker §C row "self-adjointness (Hilbert–Pólya) — RH-neutral (stone 1)"), `research/WRITEUP-geometric-obstruction.md` (Theorem B′: positivity not structural; §7 names HP-*as-analysis* as a surviving road).
**Anchor + falsifier:** function-field `H` = Frobenius (self-adjoint by Weil = a THM); DH litmus via `falsify.py`.
**Prior program contact:** stone 1 (`MEMORY: rh-lift-program`), R3/R3b (Connes scaling, Bost–Connes), thread 5 (NCG). This note classifies HP as a whole and pins the discriminator.

---

## 1. The strategy and its prerequisite

**HP:** a self-adjoint operator `H` on a Hilbert space with `spec(H) = {γ : ζ(½+iγ)=0}` (imaginary parts of the nontrivial zeros). `H=H*` ⟹ real spectrum ⟹ all `γ∈ℝ` ⟹ all zeros on `Re s=½` ⟹ RH.

**Prerequisite:** a **canonical self-adjoint `H` whose spectrum is EXACTLY the zeros.** Two halves, and the whole classification turns on separating them:
- (P-real) `H` is self-adjoint (⟹ real spectrum). *This is FREE for any operator one writes down self-adjointly.*
- (P-spec) the spectrum of that `H` is **exactly** `{γ}` — not a smooth approximation, not the UV-asymptotics, not an absorption (missing) spectrum.

The content is entirely in (P-spec). Bare self-adjointness (P-real) is RH-neutral: *every* self-adjoint operator has real spectrum, so producing one is no progress unless its spectrum is *pinned to the zeros*, and pinning it there is the whole problem.

---

## 2. Is the prerequisite CONTRADICTORY, CIRCULAR, or UNCONSTRUCTED? — the three-way split

The honest answer is that HP is **not one strategy** but a family, and its members land in different cells. The map:

### 2.1 Is there a NO-GO (an obstruction to `H`)? — NO for the general `H`; a real boundary obstruction for the *naive physical* `H`.

- **No general no-go.** Unlike de Branges (Conrey–Li 2000 *refuted the specific positivity hypotheses* [THM, scoped]), there is **no theorem forbidding a self-adjoint operator with `spec = {γ}`.** The function-field anchor proves such an operator EXISTS in the parallel universe (Frobenius on `H¹_ét`, self-adjoint for the Weil pairing — Weil's theorem). The zeros are a discrete real set of the right counting density `N(T)~(T/2π)log(T/2πe)`; a self-adjoint operator with that spectrum is a routine spectral-theory object *in the abstract* (take multiplication by `γ` on `ℓ²` of the zeros). So **(P-real)+(P-spec) is not contradictory** — the difficulty is that the *abstract* such `H` is a tautology (it presupposes the zeros), and a *canonical analytic/geometric* `H` (one built from `ζ` without listing its zeros) is **UNCONSTRUCTED.**

- **A genuine partial no-go for the naive `xp` route [established, scoped].** Berry–Keating's `H=xp` and its self-adjoint quantizations [Sierra, arXiv:1102.5356; Berry–Keating 1999] reproduce only the **smooth (Weyl) counting term** `⟨N(E)⟩` of the zeros, never the fluctuations (the actual `γ`'s). Making `xp` self-adjoint requires a boundary condition (an angle `θ`), and the resulting spectrum is Pólya's *fake* zeta, not `ζ`. The fluctuation/arithmetic part needs the primes put in by hand (Rindler/Dirac-with-prime-potential models, arXiv:1404.4252) and no such model has been made self-adjoint *with the actual zeros as spectrum*. This is a **real obstruction to the naive physical `H`** (not to HP in general): the smooth part is free (archimedean, DH-shared), the arithmetic fluctuation is the deep half — *exactly the program's count/radius and edge/line splits, in spectral-physics language.*

- **The natural-boundary obstruction [established].** Functional integrals / partition functions whose would-be self-adjoint `H` has the `γ`'s as spectrum run into the fact that the Dirichlet series attached to such sequences have a **natural boundary** — they cannot be continued, blocking the standard QFT construction of `H` [the "bosonic QFT" obstruction, Schumayer–Hutchinson and arXiv:1305.3342]. This is a *partial* no-go for one *construction method*, not for the existence of `H`.

**Net on the no-go axis:** the general `H` is **UNCONSTRUCTED, not forbidden** (the FF anchor proves existence is consistent). Specific naive routes (`xp`, QFT partition function) have established *partial* obstructions — they deliver the smooth/archimedean half free and stall on the arithmetic/fluctuation half.

### 2.2 The one route where `H` IS essentially constructed — Connes–Moscovici — is CIRCULAR.

This is the decisive finding, and it is *new since 2020* (post-dates most HP folklore). Connes' adele-class-space realization [Connes 1999, *Selecta* math/9811068] and the Connes–Moscovici **prolate spheroidal operator** [arXiv:2112.05500, 2021; PNAS 2022; *Zeta zeros and prolate wave operators* 2023] give the closest thing to a constructed `H`. The literature is explicit on both points that kill it as a *proof*:

1. **The zeros are an ABSORPTION spectrum, not the literal spectrum** [established, quoted]. Connes 1999: "the critical zeros are interpreted as the **absorption** spectrum of an unbounded operator" — they are the lines *missing* from a continuous spectrum, not eigenvalues present. The Connes–Moscovici self-adjoint prolate operator `W` does **not** have the zeros as its spectrum; rather "the restriction of `W` to the complement of a special interval `J` admits negative eigenvalues whose **ultraviolet behavior reproduce that of the squares of zeros**" (arXiv:2112.05500 abstract, verified). So even the best constructed self-adjoint operator gives the zeros only **asymptotically / as an absorption set**, confirming (P-spec) is NOT met by a clean "spectrum = zeros".

2. **Self-adjointness is NOT enough — RH reduces to Weil positivity** [established, quoted]. The same paper: this "fits with the proof of **Weil's positivity at the archimedean place**, which uses the compression of the scaling action to the **Sonin space**." And the trace-formula realization [Connes 1999; Connes–Consani] makes the explicit formula a trace over the adele class space, where **RH ⟺ positivity of the Weil distribution** — i.e. self-adjointness/`H=H*` of the operator is *equivalent to* the trace (Weil) positivity, which *is* RH. The operator's self-adjointness is the **conclusion one is trying to force**, not a free input: in the absorption picture, `H` is self-adjoint **iff** the Weil pairing is positive **iff** RH.

**Verdict on this route:** **CIRCULAR.** Self-adjointness = trace positivity = Weil positivity = RH (the audit's wall, here as an operator identity). This is the `R3` finding (`construction/R3-connes-consani-scaling-radius.md`): the scaling/spectral realization is *equivalent to RH, not a forcing* — the operator marks the self-dual axis (free, DH-shared) but leaves open whether the spectrum sits ON it (= RH).

### 2.3 Synthesis: HP = OPEN_ROAD with a CIRCULAR floor.

> The prerequisite "a canonical self-adjoint `H` with `spec(H)={γ}`" is **not contradictory** (FF anchor: consistent; no Conrey–Li-style refutation exists). It is **UNCONSTRUCTED** for the general/abstract `H`. The *only place it has been essentially constructed* — Connes–Moscovici / adele class space — delivers it **CIRCULARLY**: there, `H=H*` ⟺ Weil positivity ⟺ RH, and the zeros appear only as an absorption/UV-asymptotic spectrum, not the literal one.
>
> **So HP is an OPEN_ROAD whose floor is CIRCULAR:** the missing object is *not* "a self-adjoint operator" (those are cheap, and the only canonical one circularly equals Weil positivity) but **a NON-CIRCULAR construction of `H` — one that produces self-adjointness from an independent analytic source, not from the positivity it is meant to prove.**

---

## 3. The positivity source — GENUINE_ANALYTIC or REDUCES_TO_WEIL?

Self-adjointness IS the positivity (`H=H*` ⟺ real spectrum ⟺ the `(d,0)` signature of Theorem B′). The question forced by Theorem B′: is this positivity supplied by a **new analytic source** (a constructed operator, a measure, an estimate) *independent of the structural data*, or does it **reduce to the circular Weil positivity**?

- **The only constructed `H` (Connes–Moscovici) → REDUCES_TO_WEIL** [established]. Its self-adjointness is *literally* the Weil positivity at the archimedean place (the Sonin-space compression). No independent source: the positivity is the trace positivity, which is RH. This is the same wall the audit hit from 8+ directions (`positivity-program.md` §C, §L: the certificate ladder — the operator's self-adjointness is the LINE certificate, still empty).

- **Could a *new* `H` supply a GENUINE analytic source?** In principle yes — that is what keeps HP an OPEN_ROAD rather than CIRCULAR outright. A self-adjoint differential/pseudodifferential operator built from an *independent* analytic mechanism (a Kähler/Hodge–Riemann form on the missing surface — `construction/M3.md` keystone; a reflection-positive prime-place structure — `positivity-program.md` thread 1; an exact modular interpolation extremal whose self-adjointness comes from its *Euler/Hecke* dual certificate, not Eisenstein — worker D/E) would supply positivity from analysis, not from the assumed trace positivity. **But none is constructed**, and every *attempted* source so far either reduces to Weil (Connes), is RH-silent (QSM/Bost–Connes — real-axis, doesn't see zeros; R3b), or delivers only the smooth/edge half (`xp`/Weyl term; sym²/edge).

**Verdict on positivity source: REDUCES_TO_WEIL** for the realized strategy. The genuine-analytic source is *the missing object*, not a feature HP currently has.

---

## 4. Anchor (function field) and DH litmus

- **Anchor [THM]:** over `𝔽_q(C)`, `H` = Frobenius on `H¹_ét`, self-adjoint for the Weil/intersection pairing; self-adjointness is **Weil's theorem** (Hodge index on `C×C`). So the FF analogue exists and its analytic content is a **theorem** — but the self-adjointness there is *supplied by the finite-ground geometry* (the polarization positivity from the projective surface over `𝔽_q`). Over `ℚ` that ground is *forbidden at `∞`* (Theorem A). The FF `H` does NOT transfer because its self-adjointness's *source* (geometric positivity over a finite field) is exactly what `∞` lacks. **This is the cleanest statement of why HP is hard: the operator's reality is a THEOREM over `𝔽_q` precisely because a finite ground supplies the polarization positivity; at `∞` the operator can be written but its self-adjointness must come from analysis no structure provides (Theorem B′).**

- **DH litmus [established, via falsify.py + R3]:** bare self-adjointness / the unitary scaling structure is **DISPERSING** — it holds verbatim for Davenport–Heilbronn (DH has a functional equation ⟹ a self-dual axis `½` ⟹ a unitary/self-adjoint scaling realization with the *same* archimedean `Γ_ℝ` structure), with no Euler product. The Connes–Moscovici prolate operator's archimedean Sonin-space positivity is the DH-shared `W_∞` piece (`positivity-program.md` §H/§K: `max|A_ζ−A_DH|=0`). So HP's self-adjointness FAILS the Euler-borne test at the archimedean place: **PASS the DH-falsification test means "fails for DH"; HP's bare self-adjointness does NOT fail for DH ⟹ it does not even isolate the Euler product.** The Euler content would have to enter via the *arithmetic* (absorption / prime-fluctuation) part — which is exactly the uncderstructed/circular half.

`falsify.py` placement: bare self-adjointness / unitary scaling = **DISPERSING** (RH-neutral, holds for DH); the Connes trace-positivity realization = **CIRCULAR** (Euler-borne, sees zeros, but its positivity IS the Weil/Li positivity). Neither reaches **FORCING**.

---

## 5. The precise missing object (what `H` must be)

The OPEN_ROAD names a concrete unconstructed object:

> **A canonical self-adjoint operator `H` on an explicitly given Hilbert space, built from `ζ` by an analytic/geometric procedure that does NOT presuppose the zeros, whose self-adjointness is forced by an INDEPENDENT positivity (not the trace/Weil positivity it would prove), and whose spectrum is EXACTLY `{γ}` (not the absorption set, not the UV-asymptotics, not the Weyl smooth term).**

Equivalently, in the program's localization: **make the Connes–Moscovici prolate operator's self-adjointness/Sonin positivity come from an Euler-borne, zero-seeing source** — a Kähler/Hodge–Riemann form on the missing arithmetic surface `S²/ℤ` (`M3`/`M4`), or a reflection-positive prime-place involution (thread 1), or a Hecke/Euler (not Eisenstein) dual certificate (worker E). The operator is the *shadow* of the missing surface positivity; HP and the geometric program converge on the SAME missing object — the global/equivariant extension of CC20's archimedean positivity to the primes (`W_∞ ≥ Σ_p W_p`, the cross-place coupling).

This is why HP is **not** a fourth independent road: stone 1 already recorded it (resonances ≠ self-adjoint eigenvalues; the unitary structure reflects, doesn't force), and `R3`/`R3b` recorded that the scaling/Bost–Connes realizations give the free self-dual axis / real-axis KMS, never the arithmetic `q` / the zero locations. HP's missing object = the program's missing object.

---

## 6. Distinguished claims

- [established] No theorem forbids a self-adjoint `H` with `spec={γ}` (no HP analogue of Conrey–Li); FF anchor proves consistency.
- [established] Connes–Moscovici (2021/22) constructed a self-adjoint operator whose **UV behavior reproduces the squares of the zeros** as **negative eigenvalues in the Sonin space** — an absorption-type, asymptotic match, **not** `spec = {γ}` (quoted from arXiv:2112.05500).
- [established] In the adele-class / trace-formula realization, **RH ⟺ positivity of the Weil distribution**; the operator's self-adjointness is *equivalent to*, not a free route to, that positivity (Connes 1999; confirmed by the prolate Sonin-space link). → CIRCULAR / REDUCES_TO_WEIL.
- [established, scoped] `xp` quantizations deliver only the Weyl smooth counting term (archimedean, DH-shared); the arithmetic fluctuations / primes / actual zeros are not produced self-adjointly — a partial no-go for the naive physical `H`.
- [established] Natural-boundary obstruction blocks the QFT-partition-function construction of `H` — a partial no-go for one method.
- [partial] A non-circular `H` (self-adjointness from an independent positivity) is consistent but unconstructed = the OPEN_ROAD.

---

## 7. Verdict

**OPEN_ROAD** (the prerequisite is unconstructed, not contradictory) **with a CIRCULAR floor and a REDUCES_TO_WEIL positivity source for its only realized instance.**

- prerequisite_status: **UNCONSTRUCTED** (general `H` unbuilt and not forbidden; the FF anchor proves existence is consistent; the one essentially-constructed instance — Connes–Moscovici — is circular). Not CONTRADICTORY (no Conrey–Li-style refutation), not purely CIRCULAR (the abstract operator is consistent and a *new* analytic source is not excluded).
- positivity_source: **REDUCES_TO_WEIL** — self-adjointness of the only constructed `H` IS the Weil positivity at `∞` (Sonin compression); no independent analytic source has been realized. A genuine analytic source = the missing object.
- dh: **DISPERSING** for bare self-adjointness / unitary scaling (holds for DH, RH-neutral); the trace-positivity realization is Euler-borne but **CIRCULAR**. So on the falsifier the strategy is DISPERSING (bare) → CIRCULAR (Connes), never FORCING.
- missing_object: **a non-circular self-adjoint `H` whose self-adjointness is forced by an Euler-borne, zero-seeing positivity independent of the trace/Weil positivity, with spectrum EXACTLY `{γ}`** — identical to the program's global cross-place positivity `W_∞ ≥ Σ_p W_p` / the archimedean Kähler form on the missing surface.

**One line.** Hilbert–Pólya is foreclosed in its naive form (`xp` gives only the smooth archimedean half; bare self-adjointness is DH-shared / RH-neutral) and CIRCULAR in its one rigorous incarnation (Connes–Moscovici: the zeros are an absorption/UV spectrum and self-adjointness = Weil positivity = RH); what survives is an OPEN_ROAD whose missing object is *not an operator* but the **independent positivity that would make the operator self-adjoint** — the same cross-place Euler-borne positivity every road in this program converges on.

---

## References
- Berry, Keating, *H=xp and the Riemann zeros* (1999); G. Sierra, arXiv:1102.5356 (`H=xp` revisited).
- A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. (1999), math/9811068 (absorption spectrum; RH ⟺ Weil positivity as trace positivity).
- A. Connes, C. Consani, *The scaling Hamiltonian* (arXiv:1910.14368).
- A. Connes, H. Moscovici, *Prolate spheroidal operator and Zeta*, arXiv:2112.05500 (2021); PNAS 119 (2022); *Zeta zeros and prolate wave operators* (2023) — self-adjoint operator, UV-asymptotics of zero-squares, Sonin-space Weil positivity.
- J.B. Conrey, X.-J. Li (2000) — de Branges no-go (contrast: HP has none).
- Schumayer, Hutchinson; arXiv:1305.3342 (bosonic QFT / natural-boundary obstruction).
- Internal: `research/positivity-program.md` §C/§H/§K/§L; `research/construction/R3-*`, `R3b-*`; `MEMORY: rh-lift-program` (stone 1); `research/WRITEUP-geometric-obstruction.md` Thm A/B′.
