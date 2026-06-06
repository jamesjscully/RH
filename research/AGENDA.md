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

1. **[CONSTRUCT · load-bearing · COUPLE modulus⊗phase — the explicit-formula domination `W_∞≥Σ_p W_p`
   as the SINGLE functional]** DONE #0 (this pass) tested NEXT #1's phase on-ramp (a) executably as a
   *density* `w(t)=−(1/2π)d arg S/dt` and found the PHASE/winding is the RIGHT half (vs the RH-silent
   sym² MODULUS) but is itself **CIRCULAR**: it sees-zeros only via the **GLOBAL** winding (Birman–Krein
   count, ζ 12.96 vs off-line 14.92) — **counting ≠ forcing**; the **LOCAL** on-line density-positivity
   `w(t)≥0` is **RH-NEUTRAL** (the off-line plant stays `w≥0` on `Re=½`; the backward winding `≈−2500`
   lives at `Re=Re(ρ₀)/2=0.4`, the resonance line, NOT on ½ — so off-line-ness is read off the resonance
   LOCATION, = ¬RH geometrically, not forced); and the only DOMINATOR of the signed prime phase is the
   **archimedean `Γ_ℝ` background**, which DH shares (NOT Euler-borne). **DECISIVE LESSON: neither half
   forces alone** — modulus (sym²) is Euler-borne+independent but RH-silent (blind to the line); phase
   (winding) sees-zeros but is a count whose local positivity = RH with an RH-neutral dominator. So the
   certificate **must COUPLE** the Euler-borne sym² modulus (which DH structurally LACKS) to the
   line-detecting phase **in one functional whose positivity is precisely the domination `W_∞ ≥ Σ_p W_p`**
   (the explicit-formula inequality = the standing wall, now reached from the argument-principle side:
   the *prime* phase is signed, the *archimedean* phase must dominate it). Concrete on-ramps: **(a)** does
   the sym²/RS Euler product supply an Euler-borne LOWER BOUND on the prime phase `w_zeros` that DH lacks
   — i.e. is `log L(s,sym²)` the missing dominating phase (Euler-borne, unlike `Γ_ℝ`)? Test: is the sym²
   *phase* (not modulus) `arg L(½+it,sym²f)` a quantity DH cannot form, and does it bound `w_zeros`?
   **(b)** the `log m = log|h|² + i·arg m` split (still open from old NEXT #1): does it make the
   *coupling* explicit — modulus and phase as one complex log whose total positivity (a Jensen/Nevanlinna
   `log|m|` + winding identity) is the wall? Falsifier: a modulus alone is RH-SILENT; a phase alone is
   CIRCULAR (counting); the content is the COUPLED domination, Euler-borne on BOTH halves.
2. **[ANCHOR]** Verify the analog in the **Selberg / hyperbolic-surface** case: does the line-forcing
   quantity there (the spectral parameter / Selberg-zeta resonance condition, self-adjoint Laplacian)
   coincide with the Petersson/Maass norm, or — as in the function field — is the norm a *separate,
   RH-silent* central value while the line is forced by a different (self-adjointness) mechanism? Predict
   from DONE #1: the norm and the line-forcing are DISTINCT; confirm or break.
3. **[CONSTRUCT]** Condensed **stack-of-norms** (Clausen–Scholze / F. Charles): can it realize a
   surface over `\overline{Spec ℤ}` with self-intersection `= ‖f‖²`? Where exactly does the
   "archimedean Deligne–Illusie ⟶ Kähler" open question sit relative to this target?
5. **[CONSTRUCT]** **Tropical / Connes–Consani** square: the diagonal self-intersection in the `q→1`
   limit — does it carry the `‖f‖²` target, and where does it diverge?
6. **[CONSTRUCT · representability]** Is **"the square root of the Rankin–Selberg/Petersson
   edge-positivity"** functor representable (Brown representability / a moduli description)? What object
   would represent it?
7. **[DEFORM]** Trace the `C×C` Hodge index through the `q→1` degeneration explicitly; identify the
   **obstruction-cocycle** (what breaks) — that names the next axiom (pass-four input).

> **CAVEAT on items 3–7 (post DONE #1 + #2):** all five were written with the **`‖f‖²`
> self-intersection target**, which was refuted (DONE #1), and its first correction `deg·χ` (a NUMBER)
> was then shown RH-silent + not-even-Euler-borne (DONE #2). The corrected target is **the signature
> `(1, ρ−1)` of the negative-definite intersection FORM on `H¹_prim`** (item 1), *not any number*. So
> for items 3–7: the construction must realize an object whose intersection FORM has the Hodge-index
> SIGNATURE — replace every "self-intersection `=‖f‖²`" with "intersection form has signature
> `(1, ρ−1)`, negative-definite on the primitive part."

## DONE
(the loop appends here, newest first)

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
