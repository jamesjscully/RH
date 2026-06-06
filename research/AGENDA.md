# RH Research Agenda — autonomous loop

The `research-loop` workflow does the **top item under NEXT**, commits a result, moves the item to
DONE with a one-line finding, and appends any new items its work surfaced. Re-invoke the workflow to
continue. The agenda is the program driver; keep NEXT prioritized (load-bearing / falsifiable first).

**DISCIPLINE (every item).** §8 — certify load-bearing numerics (python-flint/mpmath, no bare floats),
never overclaim, **honest negatives are valuable** ("RH-silent" / "circular" / "the spec fails" are
real findings). Run every positivity candidate through `scripts/numerics/witness/falsify.py`'s three
axes (Euler-borne / sees-zeros / independent). Tag [THM] / [CONJ] / [computed]. Standing context: the
method is the bridge-building loop (`research/method.md`); the frontier is **RH ⟸ a self-product
surface over `Spec ℤ` whose self-intersection is the Petersson norm `‖f‖²`** (`research/work/
F-sym2-os-bridge.md`); the wall is the cross-place coupling (8 Euler-product confirmations,
`research/positivity-program.md` §E–L).

## NEXT

**HEADLINE — pass-3 convergence (modulus⊗phase).** RH = a **ζ-intrinsic, Euler-borne coupling of
MODULUS and PHASE**. The available positivities (sym²/`‖f‖²`, the von-Mangoldt prime sum) are
MODULUS/edge (RH-silent for the line) or a *borrowed sibling's* phase (RH-silent, decoupled from ζ —
forces `Δ`'s RH, not ζ's). The line is the **PHASE condition `θFθ=F^*`** = reality of ζ's own Frobenius
= the Hodge signature `(1,ρ−1)`. Wall: a **ζ-intrinsic** dominator (built from ζ's own primes `Λ(n)`)
Euler-borne on BOTH halves = `W_∞ ≥ Σ_p W_p`. **Corrected construction target: a ζ-intrinsic object
whose intersection FORM has the Hodge signature `(1,ρ−1)` (the reality/phase structure)** — NOT a
number, NOT a modulus, NOT a borrowed sym². The analytic branch has converged; **ATTACK CONSTRUCTION.**

1. **[CONSTRUCT · load-bearing]** The NAIVE product surface `S × S` is now CLOSED (DONE #0/top):
   its Künneth cross slot `C = A⊗P + P⊗A` FACTORIZES through the base single-place forms (the
   archimedean factor `A` is exactly DH-shared, `max|A_ζ−A_DH|=0`; on=off-line signature, RH-silent).
   The measurement: the second dimension is NECESSARY but the **product** surface is the WRONG one — its
   `H¹⊗H¹` splits as `base⊗base`, so the diagonal `Δ` is DECOMPOSABLE and `Δ·Δ` reduces to base data.
   **Sharpened target: a NON-PRODUCT surface whose `H¹⊗H¹` does NOT split as `base⊗base` — i.e. a Hodge/
   Néron–Severi class NOT of product type, so the diagonal is an INDECOMPOSABLE correspondence = the
   missing `End(S²/ℤ)`.** This UNIFIES the "second dimension" target with the three prior names of the
   missing algebra: the polarization relation `F^†=(deg)F^{-1}` (`frobenius_self_norm.py`), the Rosati
   off-diagonal `Tr F` *as a correspondence* (`off_diagonal.py`), the BGS §6.3 Kähler `c₁(H,k)`
   (`arakelov_signature.py`). Concretely attack: (i) is there a ζ-intrinsic NON-product 2-dim object
   (the diagonal indecomposable) — does the condensed/tropical corner (NEXT #2/#3) supply one? (ii)
   what algebraic structure on the base makes `Δ` indecomposable (a Hecke/correspondence module, NOT a
   tensor square)? Run the falsifier on any candidate: does its `H¹⊗H¹` slot fail to factor through the
   base (NOT `A⊗P+P⊗A`), and does its signature DISTINGUISH on- from off-line? falsify.py.
2. **[CONSTRUCT]** Condensed **stack-of-norms** (Clausen–Scholze / F. Charles): realize the ζ-intrinsic
   object with the **signature `(1,ρ−1)` / phase structure** (corrected from `‖f‖²`). Where does the
   "archimedean Deligne–Illusie ⟶ Kähler" open question sit relative to the *reality/phase* target?
3. **[CONSTRUCT]** **Tropical / Connes–Consani** square: in the `q→1` limit of the Frobenius
   self-pairing, does the **phase/reality** structure (not the modulus) survive, and where does it diverge?
4. **[CONSTRUCT · representability]** What functor does the **ζ-intrinsic modulus⊗phase coupling**
   represent (Brown representability / moduli)? The square root taking the edge-modulus to the line-phase.
5. **[DEFORM]** Trace the `C×C` Hodge index (the *phase*/signature, NOT the modulus) through `q→1`; the
   obstruction-cocycle names the next axiom.
6. **[ANCHOR]** Selberg/hyperbolic: confirm the line-forcing is the **self-adjointness/phase**, DISTINCT
   from the Maass/Petersson norm (modulus). Predicted distinct (DONE) — confirm or break.
7. **[analytic · demoted — converged]** The `log m = log|h|² + i·arg m` split: does a complex-log total
   positivity (Jensen/Nevanlinna `log|m|` + winding) make modulus⊗phase ONE identity? Lower priority —
   prefer construction.

## DONE
(the loop appends here, newest first)

- **2026-06-06 — Attacked the surface `S²/ℤ` DIRECTLY as a representability question (NEXT #1, after the
  metric route closed) and CLOSED the naive product surface `S × S`: its Künneth cross slot FACTORIZES
  through the base single-place forms — the second dimension is necessary but the PRODUCT is the wrong
  one (decomposable diagonal). Sharpens the target to a NON-PRODUCT surface = the missing `End(S²/ℤ)`.**
  [CONSTRUCT · load-bearing → product surface dead; points to an indecomposable diagonal].
  `scripts/numerics/witness/square_representability.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-square-representability.md`. **Finding [THM+computed]:** made the `H¹(S²)`-over-ℤ
  representability obstruction executable. (1) The `Δ·Δ=∞` wall regularizes: `(Γ_λ·Δ)=1/|1−λ|~1/|u|` at
  the corner, the divergence is a UNIVERSAL Coulomb tail (DH-shared, geometry-only), with an
  **ε-INDEPENDENT finite part `+0.161`** (computed at ε=1e-3,1e-4). (2) The candidate representing object
  carries the Künneth cross slot `C = A⊗P + P⊗A` (`A`=archimedean `Re ψ` Gram, `P`=finite `Λ(n)` Gram).
  **DECISIVE COMPUTED FACT:** `C` is BY CONSTRUCTION a function of the BASE forms `(A,P)` alone — the
  product surface's `H¹⊗H¹` FACTORIZES as `base⊗base`. The archimedean factor `A` is EXACTLY DH-shared
  (`max|A_ζ−A_DH|=0`, robust across 3 bases), so `C` is the base prime form `P` (Euler-borne, inherited)
  MODULATED by the DH-shared `A` (Kronecker bound `cross_diff≤2‖A‖‖P_ζ−P_DH‖` tight). So `C` differs ζ/DH
  (axis1 Euler-borne YES, inherited) but its signature does NOT distinguish on-line vs off-line plants
  (`sig_on=sig_off=(12,13,0)`, robust across 3 bases) → sees-zeros NO. **Verdict: Euler-borne YES
  (inherited from `P`), sees-zeros NO, independent NO → RH-SILENT.** **21st Euler-product confirmation.**
  Decisive lesson: the second dimension is NECESSARY (the square root `|α|=q^{1/2}` is genuinely 2-dim)
  but the NAIVE product `S × S` is the WRONG second dimension — it buys nothing the 1-dim base lacked,
  the cross-place coupling is STILL a perturbation of the one archimedean place, now tensored. The needed
  object is a **NON-PRODUCT surface whose `H¹⊗H¹` does NOT split as `base⊗base`** — a Hodge/Néron–Severi
  class NOT of product type, so the diagonal is an **INDECOMPOSABLE correspondence = the missing
  `End(S²/ℤ)`**. UNIFIES the "second dimension" target with the three prior names of the missing algebra
  (polarization relation / Rosati correspondence / BGS §6.3 Kähler). Honest subtlety: the coarse 4–5
  center Gaussian basis; load-bearing EXACT facts are `max|A_ζ−A_DH|=0`, the by-construction
  factorization `C=A⊗P+P⊗A`, the ε-independent finite part, and the basis-robust on=off-line signature.
- **2026-06-06 — Tested NEXT #1's sharpened target (a ζ-intrinsic Green-current/metric perturbation
  making the finite Euler piece dominate the DH-shared archimedean Kähler form) and CLOSED the
  metric-perturbation route: it dissolves into an EXHAUSTIVE dichotomy with no third option — the
  archimedean place cannot be made ζ-intrinsic while fixing ζ's zeros.** [CONSTRUCT · load-bearing →
  metric handle on §6.3 dead; points to the SECOND DIMENSION].
  `scripts/numerics/witness/green_current_perturbation.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-green-current-perturbation.md`. **Finding [THM+computed]:** a Green-current/
  metric perturbation of the archimedean place = a change of the archimedean local factor `L_∞` = an
  additive correction `g(r)` to the `Γ_ℝ` density `Re ψ(¼+ir/2)`. Made the structural dichotomy
  executable, exhaustive: **CASE 1** (metric/gauge perturbation keeping ζ's completed Weil form
  `W=A−P`) = a CONGRUENCE `W↦SᵀWS`, signature INVARIANT by **Sylvester's law of inertia** (verified
  ζ-intrinsic `S=I+ε·L[Λ]`, `(1,0,4)→(1,0,4)`) → cannot flip indefinite→definite → **RH-SILENT**;
  **CASE 2** (nonzero additive archimedean density `g_Λ(r)=Σ Λ(n)cos(r log n)/√n`, computed
  `‖g_Λ‖₂=40.8`, `max|A'−A|=66.6`) genuinely Euler-borne and changes `A`, BUT a nonzero additive
  archimedean density changes `L_∞`, hence the completed `L=L_∞·L_fin`, hence the FE and the **ZERO
  SET** — not ζ's zeros (mechanically `g_Λ` = the prime side reflected onto `∞`, double-counting, not a
  new dominator); **STEELMAN/3rd option** (perturb `A`, compensate in `P`, keep `W` fixed) = VACUOUS:
  "`W` positive" depends on `W` ALONE and the zeros are read from `W`, so holding `W` fixed (preserving
  ζ's zeros) holds the signature fixed regardless of the `A,P` split (verified `max|W_comp−W|=4e-16`,
  `(1,0,4)` unchanged) → collapses to Case 1. **THE PIN (executable EQUALITY):** "finite piece
  dominates" (`A'≠A`) == "archimedean density changed" (`g≠0`) == "`L_∞` changed" == "different
  L-function / not ζ's zeros" at every swept scale `{0,¼,½,1}`. **Verdict: Euler-borne YES (only the
  L-changing Case 2), sees-zeros YES (Case 2 moves the zero SET, doesn't see ζ's), independent NO →
  CIRCULAR / RH-SILENT split.** **20th Euler-product confirmation.** Decisive lesson: the Euler content
  is structurally confined to the finite places and the archimedean dominator is structurally DH-shared;
  **no LOCAL-metric move couples them** — the archimedean place is not free to vary ζ-intrinsically
  while fixing ζ's zeros. The §6.3 metric/Green-form handle is **dead** (not a gap — a non-existent
  degree of freedom). The dichotomy is the measurement: the missing structure is **not a metric on the
  1-dim base `bar(Spec ℤ)`, it is the SECOND DIMENSION** (the surface `S²/ℤ`, where the cross-place
  coupling is intrinsic to the geometry). Re-prioritizes NEXT #1 from a metric-perturbation hunt to a
  direct surface/representability attack; honest subtlety: the `(1,0,4)` is the same coarse 5-dim model,
  load-bearing facts are the inertia theorem + the exact `4e-16` compensation identity + the scale-sweep
  equality (basis-robust).
- **2026-06-06 — Tested NEXT #1 (the Arakelov self-intersection / arithmetic Hodge index signature
  `(1,ρ−1)` on `bar(Spec ℤ)`, ζ-intrinsically) and located BGS §6.3 EXACTLY: the signature is REAL and
  its negativity IS the Weil positivity, but the dominating positive piece (archimedean Kähler `Γ_ℝ`) is
  DH-SHARED (identical Gram), so it is NOT Euler-borne — the Euler content sits only in the DOMINATED
  finite-place prime piece.** [CONSTRUCT · load-bearing → §6.3 pinned to two named blocks].
  `scripts/numerics/witness/arakelov_signature.py` (+ 1 `falsify.py` row + auditor row),
  `research/log/2026-06-06-arakelov-signature.md`. **Finding [THM+computed]:** made the arithmetic
  intersection pairing on `bar(Spec ℤ)` executable from the **Weil explicit formula** [THM: Moriwaki
  1994 alg-geom/9403011 Thm B / Faltings–Hriljac]: its two negative pieces are exactly the two sides of
  the explicit formula — **(i) FINITE places** `(D_F²·H)≤0` (Lemma 1.3/Zariski) `= −Σ Λ(n)h(log n)/√n`,
  **(ii) ARCHIMEDEAN** `∫φ dd^c φ≤0` (Lemma 1.1.1, `= −∫|∂φ|²`) `= +(1/2π)∫ ĥ Re ψ(¼+ir/2)`. **DECISIVE
  COMPUTED SPLIT:** the archimedean Kähler Gram `A` is **IDENTICAL for ζ and DH** (`max|A_ζ−A_DH|=0.0`
  exactly — depends only on the shared `Γ_ℝ` factor `Re ψ`), so the **dominating positive piece is
  DH-shared, NOT Euler-borne**; the Euler content is ONLY in the finite-place prime Gram `P` (signature
  ζ `(5,0,0)` `Λ≥0` prime-power-supported vs DH `(3,0,2)` mixed-sign), which enters `W=A−P` with a MINUS
  sign (dominated, not dominating). **WHERE §6.3 BLOCKS:** (a) `bar(Spec ℤ)` is arithmetically a CURVE
  (1-dim base) — NO ample polarization of positive dim to carry `(1,ρ−1)`; the signature needs the
  **surface `S²/ℤ`** (= `F-sym2-os-bridge` A5, the missing object / no `H¹(S²)` over `ℤ`); (b) even
  granting the surface, **Moriwaki Thm 1.1 (ii) requires `c₁(H,k)` KÄHLER = a POSITIVE Green form = BGS
  §6.3, which CAN FAIL = CC20's archimedean knife-edge** (positivity restored only by the exact prime).
  **Verdict: Euler-borne partial (only the dominated finite piece), sees-zeros YES (it IS the Weil form),
  independent NO → CIRCULAR.** **19th Euler-product confirmation.** Decisive lesson: the arithmetic Hodge
  index theorem is the RIGHT `(1,ρ−1)` structure and the §6.3 positivity is RH content, but qua
  *archimedean* positivity it is DH-shared/RH-SILENT — RH = the cross-place coupling making the
  finite-place Euler piece DOMINATE the archimedean background (= `W_∞ ≥ Σ_p W_p` in
  arithmetic-intersection language). Honest subtlety: the 5-dim Gaussian-basis `W` signature `(1,0,4)` is
  a coarse finite-rank model (NOT claimed to be the exact `(1,ρ−1)`); the load-bearing EXACT facts are
  `max|A_ζ−A_DH|=0` and the `P`-signature split. Sharpens NEXT #1 to a *Green-current/metric*
  construction whose positivity depends on `Λ(n)`, not just `Re ψ`.
- **2026-06-06 — Tested NEXT #1 on-ramp (a) executably with the GENUINE sym²Δ (Ramanujan τ, Satake
  product) and REFUTED it: the sym² PHASE is RH-SILENT, blind to ζ's zeros — same failure as the sym²
  MODULUS. "Euler-borne / DH-lacks" ≠ "couples to ζ's line"; the missing dominator must be
  ζ-INTRINSIC.** [CONSTRUCT · load-bearing → on-ramp (a) closed]. `scripts/numerics/witness/sym2_phase.py`
  (+ 1 `falsify.py` row), `research/log/2026-06-06-sym2-phase.md`. **Finding [THM+computed]:** built the
  real sym² of weight-12 `Δ` (`τ(p)` verified vs Deligne `|τ(p)|≤2p^{11/2}`; Satake `αβ=p^{11}` exact),
  formed `arg L(½+it,sym²Δ)` and its density on the line, compared to ζ's prime-phase density `w_zeros`.
  **[A] axis 1 EULER-BORNE maximally:** DH has no Satake ⟹ `L(s,sym²)` **cannot be formed at all** (the
  object's existence needs the Hecke product). **[C] axis 3 FATAL:** source-audit confirms
  `arg L(½+it,sym²Δ)` references neither ζ nor `S_offline` — it is a **fixed background curve built only
  from `Δ`'s Satake data**, does NOT move when an off-line zero is planted in ζ, whereas ζ's own
  `w_zeros` does (`t=11`: `−0.23194→−0.23697`). **[B] the apparent "domination"** `|d/dt arg L(sym²Δ)|≥
  |w_zeros|` at every sampled `t` is **between two unrelated L-functions** — NOT an explicit-formula
  coupling, does not track ζ's zeros; the sym² phase bounds `Δ`'s OWN zeros (Deligne, a theorem), not
  ζ's. **Verdict: Euler-borne YES (maximally), sees-zeros NO, independent YES → RH-SILENT** (same box as
  the sym² modulus, DONE #0). **18th Euler-product confirmation.** Decisive lesson: conflating
  "Euler-borne/DH-lacks" with "couples to ζ's line" is the trap — `L(s,sym²f)` is a **sibling**
  L-function (ζ is GL(1), has no sym² of its own); borrowing a cusp form's sym² buys Euler-borne-ness
  only by changing the L-function, **losing the coupling to ζ**. Sharpens the wall: the missing
  dominator must be **ζ-INTRINSIC** (built from ζ's primes `Λ(n)`, coupled to ζ's zeros by the explicit
  formula) AND Euler-borne — on ζ's own prime phase the contribution is SIGNED (DONE #0). Closes on-ramp
  (a); leaves on-ramp (b) (`log m=log|h|²+i·arg m` split) as the live route + surfaces the ζ-intrinsic
  signed-prime-phase lower-bound sub-item (= `W_∞≥Σ_p W_p` on ζ's own primes).
- **2026-06-06 — Built NEXT #1's PHASE certificate (on-ramp a) as a winding DENSITY and ran the
  falsifier: the phase is the RIGHT half (vs the RH-silent modulus) but is CIRCULAR — it sees-zeros
  only via the GLOBAL winding (counting ≠ forcing); the LOCAL on-line density-positivity is RH-neutral;
  the only dominator is the archimedean Γ_ℝ phase (DH-shared, not Euler-borne).** [CONSTRUCT ·
  load-bearing → phase half pinned; neither half forces alone].
  `scripts/numerics/witness/phase_winding.py` (+ 1 sharpened `falsify.py` row),
  `research/log/2026-06-06-phase-winding-certificate.md`. **Finding [THM+computed]:** the
  scattering-phase winding density `w(t)=−(1/2π)d arg S(½+it)/dt` splits `w=w_arch−w_zeros` —
  `w_arch=(1/π)dθ/dt` the **archimedean `Γ_ℝ`** (Riemann–Siegel `θ`) phase (smooth, positive, Euler-FREE,
  **shared verbatim with DH**), `w_zeros` the resonance Poisson kernels (width = off-line distance).
  **[B] sees-zeros via the GLOBAL winding** (Birman–Krein: `N_ζ=12.960` vs `N_off=14.919` over `[2,30]`).
  **[C] DECISIVE HONEST NEGATIVE — local density-positivity is RH-NEUTRAL:** my hypothesis (off-line ⟹
  `w<0` on the line) was refuted by the test — the off-line plant stays `w≥0` on `Re=½` (`min w=+4.2e-2`);
  the backward winding (`w≈−2498`) lives **at `Re s=Re(ρ₀)/2=0.4`**, the resonance line, NOT on `½`
  (verified `Re`-sweep `0.5:+4.0 → 0.45:+5.1 → 0.4:−2498 → 0.35:−1.6`). So off-line-ness is read off the
  resonance LOCATION (= ¬RH geometrically), not forced by an on-line positivity. **[D] kill-test:** the
  only DOMINATOR of the signed prime phase is `w_arch` = the `Γ_ℝ` background, which the archimedean-only
  `S_inf` (no Euler product, no zeros) carries identically ⟹ **DH-shared, NOT Euler-borne.** **Verdict:
  Euler-borne (the dominating positivity) NO, sees-zeros YES (global only), independent NO → CIRCULAR**
  (same box as the prior Birman–Krein row, now sharpened: the PHASE is a WINDING COUNT, counting ≠
  forcing). **17th Euler-product confirmation.** Decisive lesson: **neither half forces alone** — modulus
  (sym²) Euler-borne+independent but RH-silent; phase (winding) sees-zeros but a count with an RH-neutral
  dominator. Surfaces NEXT #1: COUPLE the Euler-borne sym² modulus to the line-detecting phase in ONE
  functional = the explicit-formula domination `W_∞≥Σ_p W_p` (the wall, reached from the
  argument-principle side: prime phase signed, archimedean phase must dominate); on-ramps (a) is
  `log L(s,sym²)` an Euler-borne dominating phase DH lacks? (b) the `log m=log|h|²+i·arg m` split as the
  explicit coupling.
- **2026-06-06 — Tested BOTH NEXT #1 on-ramps for proving the positivity `θFθ=F^*` independently:
  neither works — (a) reduces to the open cross-place coupling (CIRCULAR, but UNIFIES with the wall);
  (b) the sym² norm-square controls the MODULUS not the PHASE (RH-SILENT). The reality is a PHASE
  condition.** [CONSTRUCT · load-bearing → gap pinned to a PHASE/winding condition].
  `scripts/numerics/witness/positivity_reality.py` (+ 2 `falsify.py` rows + auditor row),
  `research/log/2026-06-06-positivity-reality.md`. **Finding [THM+computed]:** the residual gap
  `θFθ=F^*` ⟺ `m(1−s)=conj m(s)` ⟺ resonances on `Re s=¼` is a **REALITY = PHASE condition** on the
  symbol. **On-ramp (a)** CC20's windowed positivity `Tr(ϑ(g)Sϑ(g)*)≥0` (supp `g⊂|u|≤L`) = the explicit
  formula on the window; its uncertified **DEFECT** is the out-of-window von-Mangoldt prime tail
  `Σ_{log n>L}Λ(n)g(log n)/√n` (computed `0.168→1.5e-2→6e-4→1.1e-5` as `L:2→3→4→5`, a genuine
  shrinking prime tail) = `off_diagonal.py`'s `Tr F` = the cross-place coupling `W_∞≥Σ_p W_p`. So
  `θFθ=F^*` **reduces, modulo the windowed-unconditional part, to that OPEN coupling** → **CIRCULAR**,
  but it **UNIFIES this pass with the standing wall** (CC20 finite-rank defect = prime-sum off-diagonal =
  ONE object). **On-ramp (b)** the sym²/RS square-modulus `m=|h|²·phase` supplies `|m|=|h|²` (the
  **MODULUS**, the edge `L(1,sym²)` Siegel positivity, unconditional). **Decisive MODULUS/PHASE split:**
  `|M(½+it)|=1` on the critical line for **BOTH** RH-true `M` **AND** the off-line plant `M_off`
  (verified `<1e-10` at `t∈{6,12,20,30}`, FE-forced, holds for DH) — while only the **resonance LOCATION**
  (phase event at `Re=Re(ρ₀)/2=0.4≠¼`) distinguishes them. So the square-modulus controls the **WRONG
  HALF** (modulus not phase) → **RH-SILENT** (Euler-borne YES, sees-zeros NO, independent YES); the SAME
  edge→line gap as Worker E, now **MODULUS→PHASE**. **16th Euler-product confirmation; first to test both
  NEXT #1 on-ramps executably.** Sharpens the gap to a **PHASE/`arg m` condition** whose obstruction is
  the prime tail and whose one available positivity (sym² `|h|²`) is the wrong (modulus) half → surfaces
  NEXT #1: a phase/winding (argument-principle, Birman–Krein) certificate from the prime data, not a
  norm-square.
- **2026-06-06 — Tested both on-ramps for the polarization relation `F·F^†=c·Id`: the RELATION is NOT
  the wall — it is the (free) functional equation; the POSITIVITY `θFθ=F^*` is the whole problem.**
  [CONSTRUCT · load-bearing → gap localized WITHIN the operator identity].
  `scripts/numerics/witness/polarization_relation.py` (+ 2 `falsify.py` rows),
  `research/log/2026-06-06-polarization-relation.md`. **Finding [THM+computed]:** built the archimedean
  model `H=L²(ℝ₊*,du/u)` where on-ramp (2) lives — `θ`=inversion `f(u)↦f(1/u)`=FE `s↦1−s`, scaling flow
  `U_λ`, `F`=Weil operator=mult by symbol `m(s)`. The polarization `F^†:=θFθ` gives `F·F^†`=mult by
  `m(s)m(1−s)`; `=c·Id` ⟺ the **unitary functional equation** `\|m\|=√c` on the line. **Decisive split:**
  (RELATION) `M(s)M(1−s)=1` for `M=Λ(2s−1)/Λ(2s)` verified to `~1e-31` for BOTH RH-true AND a planted
  off-line-zero plant, AND for **Davenport–Heilbronn** (`1e-9`, incl. near its known off-line zero
  `β=0.8085`) — it follows ONLY from the FE, so the relation holds verbatim for the RH-false function:
  **Euler-borne NO, sees-zeros NO → DISPERSING**; (POSITIVITY) `θFθ=F^*` ⟺ `m(1−s)=conj m(s)` ⟺
  resonances (poles of `M` at `ρ/2`) on `Re s=¼` — the off-line plant moves one to `Re=Re(ρ₀)/2=0.4≠¼`:
  **Euler-borne YES, sees-zeros YES, independent NO → CIRCULAR**. **So the polarization RELATION
  `F^†=(deg)F^{-1}` already EXISTS over `ℤ`/`∞` (it is the FE conjugation `θFθ`) — it is NOT a missing
  structure; the missing object is an INDEPENDENT proof of the POSITIVITY `†=*` = the open Weil/CC20
  positivity.** On-ramp (1) Bost–Connes `σ_t=Ad(ζ^{it})`: same split — the KMS modular unitarity is the
  relation (RH-silent, cf. `qsm_free_energy.py`), positivity (trace/`†=*`) is RH. **15th Euler-product
  confirmation.** First to localize the gap WITHIN the operator identity (relation-half free,
  positivity-half = whole problem); removes "construct the polarization relation" from the wall and pins
  the residual to `θFθ=F^*`. Surfaces NEXT #1 on-ramps: (a) is the CC20 finite-rank positivity defect
  the same `W_∞≥Σ_p W_p`? (b) does sym² supply the reality `m=\|h\|²·phase`?
- **2026-06-06 — Attacked the WALL `⟨F,F⟩=deg(F)`: it SPLITS into an RH-silent number and a circular
  form, separated by ONE polarization relation `F^†=(deg)·F^{-1}`.** [CONSTRUCT · load-bearing → wall
  pinned to a single operator identity]. `scripts/numerics/witness/frobenius_self_norm.py` (+ 2
  `falsify.py` rows), `research/log/2026-06-06-frobenius-self-norm.md`. **Finding [THM+computed]:**
  `⟨F,F⟩=deg(F)` has no single `ℤ`-meaning — it is TWO inequivalent objects coinciding over `𝔽_q` *only
  because RH holds there*: (i) **ALGEBRAIC/Rosati** `Tr(F·qF^{-1})=2gq` (uses ONLY the polarization `q`,
  RH-BLIND — verified: a planted off-line zero leaves it `28.0→28.0`) `=` Faltings–Hriljac `ĥ_NT`, an
  unconditional `ℤ`-number but the height of a point on a FIXED curve's `J(X_K)` with no `ζ` in it (the
  "wrong divisor") → **RH-SILENT**; (ii) **HILBERT/spectral** `Tr(F·F^*)=Σ|α|²` `=` CC20 archimedean
  diagonal `W_∞`, SEES the zero (`28.0→30.25` off-line) but `algebraic=Hilbert` (`F^†=F^*`) IS RH →
  **CIRCULAR**. Adjunction control exact (`Γ_F·Γ_F=q(2−2g)`, `g∈{1,2,3} q∈{5,7,9}`). **The two are
  separated by EXACTLY the operator identity `F·F^†=(deg)·Id` (`F^†=qF^{-1}`, the deg-`q` polarization),
  provided over `𝔽_q` by `End(Jac)` and missing over `ℤ`.** So "give `⟨F,F⟩` an unconditional meaning"
  = "construct `End(S²/ℤ)` with a POSITIVE Rosati `F^†=(deg)F^{-1}`" — the same missing
  correspondence-algebra, now pinned to ONE relation. **Both named handles classified:** (a) Arakelov
  `ĥ_NT` = unconditional value but RH-silent channel; CC20 `Δ·Δ_arch` = sees-zeros but BGS §6.3-open
  (circular); (b) `q→1` of `2gq` = RH-silent scalar unless it enters as a form's diagonal (then
  circular). **14th Euler-product confirmation.** Sharpens the wall from "the self-norm is missing" to
  "the POLARIZATION RELATION `F^†=(deg)F^{-1}` is missing"; surfaces two on-ramps (Bost–Connes modular
  `σ_t`; CC20 Sonin `SθS=(deg)Id`) → NEXT #1.
- **2026-06-06 — Attacked the single missing Rosati entry: it is NOT the off-diagonal — the off-diagonal
  is available (the prime sum); the WALL is the OTHER diagonal `⟨F,F⟩=deg(F)`, the Frobenius
  self-norm.** [CONSTRUCT · load-bearing → DONE #1 corrected by one index].
  `scripts/numerics/witness/off_diagonal.py` (+ `falsify.py` row),
  `research/log/2026-06-06-off-diagonal-self-norm.md`. **Finding [THM+computed]:** Three parts, all
  certified. (A.1) The off-diagonal `Tr F` over `ℤ` IS the von Mangoldt PRIME SUM (`c_ζ(n)=Λ(n)` to
  `2.5e-60`; the *arithmetic* side of the explicit formula) — an honest RH-INDEPENDENT number, analog of
  the integer `a=#C(𝔽_q)−(q+1)`. **So the off-diagonal IS available over `ℤ`, contra DONE #1.** (A.2)
  The entry with NO unconditional `ℤ`-meaning is the SECOND DIAGONAL `⟨F,F⟩=deg(F)`: over `𝔽_q`=`2q`
  (self-pairing of the Frobenius *correspondence*, RH-independent); over `ℤ` no correspondence exists, so
  `⟨F,F⟩=Σ_ρ|φ̂_F(γ_ρ)|²` is a norm IFF the `γ_ρ` are real = RH (computed: an off-line zero makes it
  cease to be a Hermitian square). (B) The Cauchy–Schwarz `|Tr F|²≤⟨Id,Id⟩⟨F,F⟩` SEES the zeros (Weil
  Toeplitz Gram min eig `−3.4e-16` on-line PSD → `−2.29` off-line indefinite, a `2×2` minor det `−0.84`
  VIOLATES CS) but IS the PSD-ness of the Weil form = RH. *Honest subtlety:* the lone `(Id,F)` `2×2` is
  too coarse to register one faint off-line zero — equivalence is at the FULL Gram (first model erred
  here, corrected to the validated Toeplitz form). (C) `𝔽_q` control: `a²≤4q` is a THEOREM about FIXED
  integers (Hasse–Weil, `q∈{4..25}`) — automatic from the *existence of `End(Jac)`*, not a hypothesis.
  **Verdict: Euler-borne YES, sees-zeros YES, independent NO → CIRCULAR.** 13th Euler-product
  confirmation. **Sharpens + corrects DONE #1:** the wall is the **Frobenius self-norm `deg(F)`**, which
  *unifies* "missing off-diagonal" and "missing correspondence-algebra" into one object (a diagonal
  self-intersection of a correspondence over `ℤ`), reconnecting to the signature/Hodge-index thread
  (DONE #2). Bounding CS = dominating the prime sum by an unconditional Frobenius degree = `W_∞≥Σ_p W_p`.
- **2026-06-06 — Re-ran method.md step 2 with the UNIFIED axiom: the reflection IS the Rosati
  involution (a THEOREM over `𝔽_q`), and the wall is ONE off-diagonal matrix entry.** [CONSTRUCT ·
  load-bearing → mechanism named + wall pinned]. `scripts/numerics/witness/rosati_reflection.py` (+
  `falsify.py` row), `research/log/2026-06-06-rosati-reflection.md`. **Finding [THM+computed]:** the
  decisive question ("is there a reflection under which the edge norm-square becomes the neg-def
  primitive form at the centre?") is answered **YES — the Rosati involution `θ(α)=q/ᾱ`=FE**, executable
  end-to-end over `𝔽_q`: edge number `F·F'=q=deg` (=the FF `‖f‖²`, true off-line too) → reflection `θ`
  (fixed locus `|α|=√q=Re s=½`) → **Rosati positivity `M=[[2,a],[a,2q]] ⪰ 0 ⟺ a²≤4q ⟺ |α|=√q` =RH for
  the curve** (semidefiniteness tracks the line in all 5 planted cases incl. the boundary). `ℤ`-audit:
  the **diagonal `⟨Id,Id⟩=‖f‖²` (unconditional, Siegel) and the reflection FE both transfer**; the only
  missing piece is the **OFF-DIAGONAL `Tr(F)`** = the primes/cross-place coupling `W_∞≥Σ_p W_p`. So RH =
  the **Cauchy–Schwarz `|Tr F|² ≤ ⟨Id,Id⟩⟨F,F⟩`** on the Rosati Gram — the reflection alone does NOT
  make a positive `2×2` from one positive diagonal entry. Falsifier: **Euler-borne YES, sees-zeros YES,
  independent NO → CIRCULAR** (=Weil positivity over `ℤ`, same box as signature/Weil–Li). **12th
  Euler-product confirmation; sharpens the edge→line wall from "make the OS form positive" to a SINGLE
  NAMED off-diagonal entry.** Honest subtleties recorded: (i) line=`a²≤4q`=positive-*semi*definite (not
  strict; boundary supersingular has det=0 on-line); (ii) over `ℤ` `θ`=FE acts on the spectral
  parameter only, not on an `End(S²/ℤ)` — **the missing off-diagonal and the missing algebra-of-
  correspondences are the same gap.**
- **2026-06-06 — Ran the SIGNATURE through the falsifier (method.md step 4): the verdict DOES change,
  NUMBER→FORM moves RH-SILENT→CIRCULAR, and the geometric/OS threads UNIFY.** [CONSTRUCT · load-bearing
  → relocation confirmed + thread unification]. `scripts/numerics/witness/signature_forcing.py` (+
  `falsify.py` registry row), `research/log/2026-06-06-signature-forcing.md`. **Finding [THM+computed]:**
  Made the Hodge-index signature *executable* via the genuine Weil RH-defect form `P=diag(|α_k|²−q)`
  (Rosati `F*F=q`): under RH identically zero, signature `(0,2g,0)`; planting one off-circle eigenvalue
  *with its FE-forced Weil partner* (`q/β̄`, opposite side of `q`) flips it to `(1,2g−2,1)` — so a
  **SIGNATURE SEES ZEROS** (computed q=7,g=2, all blow factors) where a NUMBER cannot. Euler-borne YES
  (the form needs a Satake lattice DH lacks; strictly stronger than `deg·χ`). So the falsifier verdict
  **changes**: `RH-SILENT` (both numbers) → **`CIRCULAR`** (the signature = Weil positivity over `ℤ`),
  the SAME box as the canonical Weil/Li form — *not* the prize, but the correct forcing functional with
  only the independent proof missing. **Decisive step-4 identification:** by Sylvester, signature
  `(1,ρ−1)` `⟺` neg-def primitive part `⟺` `−1×`(form) is pos-def `⟺` an inner product `⟺` **the OS/GNS
  Hilbert space (A4 of `F-sym2-os-bridge`)** — the geometric Hodge-index target and the analytic OS/sym²
  target are **ONE positive-definite form**. 11th wall confirmation, first to *unify* the two threads;
  collapses NEXT to a single shared positivity. First model (naive Gram `Re(u_iū_j)`) failed honestly
  (rank≤2, blind to the circle) and was corrected to the Rosati form.
- **2026-06-06 — Re-ran step 2 with the corrected mechanism: the line is a FORM's SIGNATURE, not a
  NUMBER.** [BACK UP · load-bearing → honest negative + relocation].
  `scripts/numerics/witness/a5_corrected.py`, `research/log/2026-06-06-a5-corrected-mechanism.md`.
  **Finding [THM+computed]:** the corrected forcing input `Γ_F·Γ_F = deg(F)·(Δ·Δ)` (verified exactly:
  ratio `= deg(F)` for `F∈{id,Frob_q,Frob_{q²},[2],[3]}`, line `= log(q^{1/2})/log q = ½` for every
  `q`) is, on the falsifier, **RH-SILENT *and not even Euler-borne*** — `deg·χ` is pure
  topology×base-field-size, carried by DH too (strictly **worse** than `‖f‖²`, which at least
  DH-refused). The decisive relocation: the RH content is the **Hodge-index SIGNATURE `(1, ρ−1)`** —
  negative-definiteness of the intersection FORM on the primitive part — verified on `E×E` (Gram
  `[[0,1,1],[1,0,1],[1,1,0]]`, eigenvalues `{−1,−1,2}`, signature `(1,2)`). The self-intersection
  *number* (`‖f‖²` OR `deg·χ`) is merely a value the form is evaluated on. **Both the `‖f‖²` axiom and
  its correction are the WRONG KIND of object: the line is forced by a FORM's signature, not a NUMBER.**
  `‖f‖²` confirmed RH-silent scaffolding (enters only as a lattice value, never as forcing). 10th wall
  confirmation; relocates the target to the negative-definite `H¹_prim` form over `ℤ` (NEXT #1, reconnects
  to the OS/reflection-positivity thread).
- **2026-06-06 — A5 in the function-field case: REFUTED (false weld).** [ANCHOR · load-bearing →
  honest negative]. `scripts/numerics/witness/a5_function_field.py`,
  `research/log/2026-06-06-a5-function-field-refuted.md`. **Finding [THM+computed]:** Weil's
  line-forcing self-intersection on `C×C` is `Δ·Δ=2−2g` / `Γ_q·Γ_q=q(2−2g)` — an **Euler characteristic
  times `q=#𝔽_q`**, with NO modular form in it — verified yielding `|α|=√q` on elliptic curves (q=5,7,
  11,13). It is **NOT** the Petersson/Rankin–Selberg residue `‖f‖²`. The genuine "self-intersection =
  RS L-value" theorem over `𝔽_q` is **Yun–Zhang** (Shtukas; `=L^{(r)}(1/2)`) — a **DERIVATIVE at `s=1/2`
  on moduli of Shtukas (not `C×C`), Gross–Zagier-type, RH-SILENT**. Three steelman readings all fail.
  **A5 conflates two distinct theorems on distinct spaces about distinct `s`-values** ⟹ the pass-two
  axiom "surface self-intersection `=‖f‖²`" pins the wrong number; the bridge's central analogy fails
  *at the function-field archetype*. 9th wall confirmation, first one *inside* the FF model. Triggered
  HIGH-priority back-up item (NEXT #1).
