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

1. **[CONSTRUCT · load-bearing · the polarization relation `F·F^†=deg·Id`]** The Frobenius self-norm
   `⟨F,F⟩=deg(F)` does NOT have a single `ℤ`-meaning (DONE #0 this pass): it SPLITS into an unconditional
   RH-SILENT number (algebraic Rosati `2gq` = Arakelov `ĥ_NT`, blind to the zeros) and a forcing
   RH-conditional norm (Hilbert `Σ|α|²` = CC20 archimedean diagonal), **separated by exactly the
   polarization relation `F^† = (deg)·F^{-1}`** (the operator identity `F·F^† = (deg)·Id` in `End(Jac)`).
   So the wall is now a SINGLE OPERATOR RELATION, not a missing object: **build a `ℤ`-algebra `A` (the
   would-be `End(S²/ℤ)`) with the explicit-formula prime-sum element `F` and an involution `†` s.t.
   `F·F^† = c·Id` UNCONDITIONALLY (the polarization), with `†` POSITIVE (`F^†=F^*`, the Hilbert adjoint)
   being RH.** Two concrete on-ramps surfaced this pass: **(1) the Bost–Connes/QSM algebra** already has
   `ℤ`, a `ζ`-partition function, and a modular involution `σ_t` — does its `F·F^†` close to a scalar (a
   KMS/modular relation), and is the resulting `c` the polarization degree? **(2) the CC20 Sonin/Toeplitz
   compression** — is `S θ S = (deg)·Id` on Sonin's space the missing operator identity (`F^†=(deg)F^{-1}`
   as the scaling-flow adjoint)? Falsifier discipline: the unconditional value is RH-SILENT (handle a/b
   only ever supply the wrong-divisor channel); the content is the POSITIVITY `F^†=F^*` = RH.
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
