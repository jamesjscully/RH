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

## CLOSED — the form/operator impossibility map (pass 3–4, verified vs 𝔽_q)
RH = ζ-intrinsic Euler-borne coupling of MODULUS⊗PHASE = `W_∞ ≥ Σ_p W_p`. Every static (form/operator)
route to it is now closed with a structural reason (logs: `2026-06-06-*pairing*.md`, `*-domination.md`):
- **self-pairing forms** (symmetric/θ-twist/Hermitian/oriented, real OR complex plant) — **Sylvester
  inertia-locked** for any `*`-congruence of a fixed DH-shared background. [THM-flavored]
- **operator domination** — no operator is both Euler-borne-independent AND zero-tracking.
- **zero-side Gram** — circular + not Euler-borne.
The open object survives unscathed: **a structure that genuinely depends on the zero LOCATIONS** = the
Frobenius/`(p,q)`/Deninger archimedean-Hodge action (deep construction). 28 Euler/wall confirmations.

## CLOSED — the de Bruijn–Newman / `Λ≤0` (dynamical) branch (audited, pass 1–2)
The dynamical route (`RH ⟺ Λ≤0`, dBN heat flow `e^{−tD²}`) is **genuinely DISTINCT on the INERTIA
axis** — the flow is a 1-param semigroup, NOT a `*`-congruence, and it CHANGES the real-root count, so
it ESCAPES the Sylvester lock that closed every static form (the one structurally new thing the whole
audit produced). **But it stalls at the SAME wall on the Euler/location axis**, for the same reason
(logs `2026-06-06-dbn-anchor.md`, `-dbn-flow-functional.md`):
- **the only unconditional lever (Rodgers–Tao `Λ≥0`)** uses GUE/Montgomery pair correlation, which is
  UNIVERSAL (a pure Hermitian random matrix with no Euler product carries the same level repulsion,
  `P(gap<0.25mean)` GUE `0.020` vs Poisson `0.220`) — RH-silent on the Euler axis, and wrong-direction.
- **the open object it named — an Euler-borne flow functional monotone toward reality** — was built and
  SPLITS like every static functional: the modulus reading `Σ|Im P(γ)|` is Euler-borne + sees `|Im|` but
  is `sign Im`-blind and `→0 ⟺ RH` (circular); the only reading that sees `sign Im` (`Σ Im P(γ)`) is
  IDENTICALLY 0 on the FE-forced conjugate config (`+Im`/`−Im` cancel). The dBN generator is Euler-FREE;
  the primes ride passively (initial datum only); `sign Im` is conjugation-odd, Euler functionals are
  conjugation-even. 30th wall confirmation. **Verdict: distinct endpoint on inertia, SAME wall on the
  Euler/location axis.** The program returns to the static frontier below.

## NEXT — CONSTRUCTION MODE  (charter: `research/construction-program.md`; method: `research/method.md`)

**We are BUILDING the object — a polarized arithmetic Hodge category over `\overline{Spec ℤ}` — not
auditing.** Each item DEFINES a structure / BUILDS a minimal model / PROVES a coherence lemma / INVENTS
notation, and runs `falsify.py` where applicable (does the polarization depend on the zero LOCATIONS?
does the construction FAIL to exist for DH?). **Design law (the audit's gift):** the polarization is
**CATEGORICAL — a duality pairing — never a metric** (metrics are Sylvester-inertia-locked, dead by §0).
**Anchor first:** nothing is admitted for `ℤ` until it is built for **function fields in the same
language** and shown to reproduce the Weil/Hodge-index proof. Wrong definitions are expected — each one
*names the next*; that is convergence, not drift.

M2. **[ANCHOR-BUILD · load-bearing]** Build the polarized arithmetic Hodge category **for a function
   field** (e.g. an elliptic curve over `𝔽_q`) *in this language*, and verify it **reproduces the Weil
   RH proof** with polarization = the categorical duality pairing (NOT a metric). If it can't redo the
   solved case, the language is wrong — say so and propose the fix. The minimal working model.
   **CONTRACT TO HIT (M1, `construction/M1-universal-property-S_Z.md`):** exhibit `H^•(C/𝔽_q)` as a
   `ζ`-Hodge datum satisfying clauses **C1–C6**; the FF columns of M1's table are the acceptance test
   (C1 Lefschetz trace; C2 `c=†`Rosati, positivity `c`-EVEN; C3a Weil pairing `Φ^TEΦ=qE`; **C3b `μ=√q`
   = the Frobenius weight**; C4 `⟨φ,ψ⟩=Tr(φψ†)` = canonical pairing of `D`, no metric; C5 signature flip
   `(0,1,1)→(1,0,1)`). Verify the C4 pairing is built as the Poincaré-duality evaluation, NOT a chosen
   Gram metric — that distinction is the whole point of the language.
M2b. **[DEFINE · the hinge clause C3b]** M1 self-localized ALL residual `ℤ`-hardness into **C3b: the
   critical radius `μ` (=`Re s=½`) must be Euler-borne**, the way `μ=√q` is the Frobenius weight over
   `𝔽_q` (DONE #32). Define, precisely, what it would MEAN for a `ζ`-intrinsic object's similitude
   multiplier `μ` in `Φ^*φ_{FE}Φ=μφ_{FE}` to be **read off the local Euler factors `{L_p}`** rather than
   the FE — i.e. write C3b as a representability sub-problem (the radius datum as a functor of the local
   factors). This is the prize AND the DH-falsifier (C6) in one clause; sharpen it before M4 tries to
   construct it.
M3. **[INVENT]** Define the **archimedean Hodge polarization**: the `(p,q)`/condensed duality datum at
   `∞` supplying the reality/phase. Coin notation; state its axioms; check it is **not a `*`-congruence**
   (passes the §0 no-go by construction) and is condensed-archimedean (the duality Arakelov lacks).
M4. **[DESCENT]** Specify the **duality-descent gluing**: how `{Euler factors at primes} ∪ {Γ_ℝ (p,q) at ∞}`
   glue to a global object whose polarization **is** the explicit-formula quadratic form (so `W_∞≥Σ_p W_p`
   is a descent constraint, not a hope).
M5. **[FALSIFY]** Run M2–M4's objects through `falsify.py`: confirm sees-zeros (polarization depends on
   zero locations) AND DH-failure (no Euler product ⟹ no object).

## CLOSED — the form/operator impossibility map (pass 3–4, verified vs 𝔽_q)
RH = ζ-intrinsic Euler-borne coupling of MODULUS⊗PHASE = `W_∞ ≥ Σ_p W_p`. Every static (form/operator)
route to it is now closed with a structural reason (logs: `2026-06-06-*pairing*.md`, `*-domination.md`):
- **self-pairing forms** (symmetric/θ-twist/Hermitian/oriented, real OR complex plant) — **Sylvester
  inertia-locked** for any `*`-congruence of a fixed DH-shared background. [THM-flavored]
- **operator domination** — no operator is both Euler-borne-independent AND zero-tracking.
- **zero-side Gram** — circular + not Euler-borne.
The open object survives unscathed: **a structure that genuinely depends on the zero LOCATIONS** = the
Frobenius/`(p,q)`/Deninger archimedean-Hodge action (deep construction). 28 Euler/wall confirmations.

## CLOSED — the de Bruijn–Newman / `Λ≤0` (dynamical) branch (audited, pass 1–2)
The dynamical route (`RH ⟺ Λ≤0`, dBN heat flow `e^{−tD²}`) is **genuinely DISTINCT on the INERTIA
axis** — the flow is a 1-param semigroup, NOT a `*`-congruence, and it CHANGES the real-root count, so
it ESCAPES the Sylvester lock that closed every static form (the one structurally new thing the whole
audit produced). **But it stalls at the SAME wall on the Euler/location axis**, for the same reason
(logs `2026-06-06-dbn-anchor.md`, `-dbn-flow-functional.md`):
- **the only unconditional lever (Rodgers–Tao `Λ≥0`)** uses GUE/Montgomery pair correlation, which is
  UNIVERSAL (a pure Hermitian random matrix with no Euler product carries the same level repulsion,
  `P(gap<0.25mean)` GUE `0.020` vs Poisson `0.220`) — RH-silent on the Euler axis, and wrong-direction.
- **the open object it named — an Euler-borne flow functional monotone toward reality** — was built and
  SPLITS like every static functional: the modulus reading `Σ|Im P(γ)|` is Euler-borne + sees `|Im|` but
  is `sign Im`-blind and `→0 ⟺ RH` (circular); the only reading that sees `sign Im` (`Σ Im P(γ)`) is
  IDENTICALLY 0 on the FE-forced conjugate config (`+Im`/`−Im` cancel). The dBN generator is Euler-FREE;
  the primes ride passively (initial datum only); `sign Im` is conjugation-odd, Euler functionals are
  conjugation-even. 30th wall confirmation. **Verdict: distinct endpoint on inertia, SAME wall on the
  Euler/location axis.** The program returns to the static frontier below.

## NEXT — the static frontier (the surviving load-bearing items)

The audit's standing result: **no finite-rank form/operator AND no Euler-borne flow functional is
simultaneously Euler-borne, independent, AND zero-location-tracking** — `sign Im ρ` lives in the zeros,
`Λ(n)` lives in the primes, and the only object coupling them is the INEQUALITY `W_∞ ≥ Σ_p W_p` = the
self-intersection `‖f‖²` (the missing surface, `F-sym2-os-bridge.md`).

**CORRECTED FRAMING (2026-06-06, `conjugation-parity-ff`): there is ONE wall, not two.** Auditing the
WORKING function-field proof (where the `C×C` Hodge index IS a theorem) shows Weil forces the line with
a **conjugation-EVEN** positive form `Tr(φφ†)=Σ|αᵢ|²=2gq` (the Rosati `†:α↦q/α` IS the FF complex
conjugation; each term `α·α†=q` exactly). He NEVER reads one zero's side (no odd functional) — he reads
the **SIGNATURE/inertia degeneracy** of an EVEN positive-*semi*definite form (the line = its kernel
locus). The unique conjugation-ODD datum (`u=Σ log(α²/q)`) flips sign under `†` and VANISHES on every
FE-symmetric spectrum (the `E_signed≡0` cancellation, DONE #25/#30). **So "the missing object must be
conjugation-ODD" was a MIS-NAMING of the inertia-degeneracy of an even form.** The real-and-only wall is
the **SYLVESTER inertia-lock**: an EVEN positive form whose signature is MOVABLE by the Euler/prime data
(so a planted off-line pair degenerates it). The live routes, re-prioritized to that single wall:

1. **[THE RADIUS PROBLEM · load-bearing · sharpest, replaces the abstract "Euler-movable inertia"]**
   `euler_movable_inertia.py` (DONE, just now) EXECUTED the FF archetype and found: the even Hodge-index
   form's inertia IS genuinely Euler-MOVABLE over `𝔽_q` (an off-circle Frobenius pair flips the
   primitive sig `(0,1,1)→(1,0,1)`, "gains a `+`", EXACTLY `= Σ|αᵢ|²−2gq` the modulus defect), so the
   corrected NEXT #1 spec is SATISFIABLE in the FF — BUT the moving quantity is a conjugation-EVEN
   MODULUS measured against the **circle radius `√q`**, and `√q` is the EULER datum (the Frobenius
   weight); a generic non-Satake pairing flips identically, so the Satake `q` only sets the radius.
   The decisive gap, now named: **over `𝔽_q` the Euler product SETS the radius `√q`; over `ℤ` the
   radius `Re s=½` is the FE FIXED LOCUS, Euler-INDEPENDENT (DH shares it).** So the missing object is
   NOT "an even form with movable inertia" (the FF has one) but **an Euler datum over `ℤ` that sets the
   critical radius `Re s=½` the way `q` sets `√q`.** THE OPEN QUESTION: is there ANY ζ-intrinsic object
   over `ℤ` whose critical radius is read off the Euler/prime data rather than the FE? The certificate
   ladder (`§L`) restated: the Euler product anchors the **edge `Re s=1`** (abscissa of abs.
   convergence, Worker E); the FE anchors the **centre `Re s=½`**. Probe: does ANY Euler-product
   feature anchor at `½` and not just `1`? **Falsifier in advance:** the candidate's critical radius
   must be DH-distinguishing (an Euler datum), not the FE-shared `Re s=½`.
2. **[the `q→1` degeneration WITH the radius tracked · load-bearing]** Now that the radius `√q` is
   identified as THE Euler-borne invariant carrying the inertia-flip (DONE, `euler_movable_inertia.py`),
   the `q→1` degeneration of the `C×C` Hodge index has a tracked target: `√q → 1`, the circle collapses
   to the point. **What is the `q→1` image of "`√q` is the Frobenius weight"** — does the Frobenius-weight
   radius survive as an EULER datum over `𝔽₁`/the Scaling Site, or does it become the FE locus? Make this
   executable in the Connes–Consani Scaling Site / F. Charles' archimedean Deligne–Illusie corner, with
   the **radius** (not the abstract inertia) as the tracked invariant. (This is the concrete `q→1`
   question prior passes deferred, now with the load-bearing invariant pinned by DONE.)
3. **[A5 · the reflection that pairs `s=1` to `s=½` · load-bearing]** The OS/A4 reduction
   (`F-sym2-os-bridge.md` pass 1): the sym²/Rankin–Selberg edge norm-square is anchored at `s=1`
   (`Res_{s=1}L(s,f×f̄)=‖f‖²>0`, a theorem); A5 is the structure under which it becomes OS-positive
   across `s=½`. Axiomatize what *represents* the pairing of the `s=1` residue to the `s=½` form (the
   `h_∞` corner-compactification in OS language) and test whether ANY natural pairing carries the
   Petersson residue from `s=1` to a positive form at `s=½`, for sym²Δ vs the DH-surrogate. The
   informative probe is structural (A5), NOT the circular min-eig of `B(θ·,·)` (which is `>0 ⟺ RH`).
   Note: this is an EVEN-form positivity (consistent with the corrected framing).

## DONE
(the loop appends here, newest first)

- **2026-06-06 — M1 [DEFINE]: wrote the universal property of `𝕊_ℤ` as a representing-object contract
  C1–C6 over `ζ`-Hodge data, with the polarization CATEGORICAL (C4 = canonical evaluation pairing of the
  duality `D` pre-composed with the FE iso, NO metric — §0-clean by construction) and the one-line lemma
  C5 `axioms ⟹ RH` made formal.** [DEF · the contract, formal].
  `research/construction/M1-universal-property-S_Z.md`. **What got DEFINED:** the functor of points
  `𝔖(𝒞,ω_∞,D,P) = {X satisfying C1–C6}/≅`, with `𝕊_ℤ` its representing object; the ambient
  polarizable/`(p,q)`-graded/`𝕊`-linear/condensed-archimedean 2-category (the §2 Pillar-A glue), with
  **no metric anywhere** (the pairing lives in `𝒞` via `D`; the Hodge functor only grades + supplies `c`).
  Six clauses, each stated as a condition on `X` with the FF THEOREM beside it as the anchor: **C1** `Φ`
  with `spec=zeros`, `Tr=`explicit formula (FF: Lefschetz); **C2** `(p,q)` grading + `c` anti-linear
  exchanging `H^{p,q}↔H^{q,p}` (FF: `c=†`Rosati, verified `1e-9`; load-bearing correction DONE #31 baked
  in — positivity must be `c`-EVEN inertia, NOT a `c`-odd functional); **C3** `D(X)≅X` = FE, **split into
  C3a** (the relation `Φ^*φ_{FE}Φ=μφ_{FE}`, FE-borne/DH-shared/RH-silent-if-alone) **and C3b** (the VALUE
  `μ`=critical radius must be Euler-borne); **C4** `⟨x,y⟩_D=`ev∘(1⊗φ_{FE}) = canonical pairing of `D` (FF:
  Rosati `Tr(φψ†)`); **C5** `⟨·,·⟩_pol>0` on `H^1_prim` ⟺ RH; **C6** no object for DH (no Euler product ⟹
  no `μ`). **THE DECISIVE STRUCTURAL OUTPUT:** the contract **self-localizes** — C1/C2/C4/C6 are
  definitions we can make (theorems in the FF), the one-line lemma makes C5 `axioms⟹RH` formal, and **ALL
  residual hardness collapses into C3b** ("the Euler product sets `Re s=½` the way `q` sets `√q`"). This is
  NOT new hardness: it is the program's 32-confirmation wall, now sitting in its correct place as a SINGLE
  CLAUSE of a universal property, where a definition (M4 descent: construct `μ` from the local factors) can
  attack it — and **the same clause C3b is the prize AND the built-in DH-falsifier (C6)**, exactly as the
  audit predicted (Euler-borne axis is now a contract clause, not an after-the-fact test). FF columns
  re-verified live: on-circle sig `(0,1,1)`, off-circle flip `(1,0,1)`, flip-eig `=Σ|αᵢ|²−2gq` (`match=True`
  every `r`). **No falsifier run (M1 is a definition, not a candidate object);** falsifier-bearing clauses
  C3b/C6 written so M2–M5's OBJECTS are testable against a fixed standard. **Honest residue:** C5's lemma
  is only as strong as C3b, which is not yet constructed — that is the point (hardness correctly PLACED,
  not hidden). **Successors added:** M2b [DEFINE the hinge clause C3b as a representability sub-problem —
  the radius datum as a functor of the local Euler factors] inserted after M2; M2's acceptance test pinned
  to the M1 contract table.

- **2026-06-06 — EXECUTED the corrected NEXT #1/#2 spec ("an EVEN positive form whose inertia is
  Euler-MOVABLE — an off-line plant degenerates the signature") in the ONE place the Hodge index is a
  THEOREM (the function field), testing the agenda's own NEXT #2 assertion, and found: the assertion is
  LITERALLY TRUE — the FF DOES have Euler-movable inertia — BUT the three-axis falsifier locates WHY it
  does not transport to `ℤ`: the moving quantity is a conjugation-EVEN MODULUS against the circle radius
  `√q`, and `√q` is the EULER datum, while over `ℤ` the radius `Re s=½` is the FE FIXED LOCUS
  (Euler-independent).** [CONSTRUCT/EXECUTE · load-bearing → first concrete realization of
  Euler-movable inertia; gap renamed to THE RADIUS PROBLEM]. `scripts/numerics/witness/euler_movable_inertia.py`
  (+1 `falsify.py` row), `research/log/2026-06-06-euler-movable-inertia.md`. **Finding [computed+THM,
  exact, falsifier CIRCULAR]:** built Frobenius `F` on `H¹(E)` (companion `T²−a₁T+q`), the polarization
  `E` (`FᵀEF=qE`, residual `<1e-15`), the Rosati adjoint `φ†=E⁻¹φᵀE` (= the FF conjugation `α↦q/α`),
  and the PRIMITIVE Hodge-index form `−Tr(F₀F₀†)` on the trace-zero `F₀=F−(trF/2g)Id`. **(1) The
  assertion is TRUE:** on-circle (5 RH curves `q=5,7,11,13,2`) primitive sig `(0,1,1)`, neg eig `=−2gq`
  exactly; off-circle plant `{r√q,√q/r}` (product `q`, `|·|≠√q`) FLIPS the neg eig to POSITIVE, sig
  `(0,1,1)→(1,0,1)`, monotone in `r` ("the signature gains a `+`") — **Euler-movable inertia is REAL in
  the FF; the corrected spec is SATISFIABLE there (first concrete archetype).** **(2) The falsifier
  pins the non-transport:** the flipping eigenvalue equals EXACTLY the MODULUS DEFECT `Σ|αᵢ|²−2gq`
  (match `1e-9` every `r`) — conjugation-EVEN (symmetric under `|α|↔q/|α|`; `r` and `1/r` give identical
  sig `(1,0,1)` — HOW FAR not WHICH SIDE, the 31-conf modulus/phase split); the flip does NOT need the
  Satake polarization (a generic non-`q`-similitude pairing = DH-like flips identically — the Satake `q`
  only RESCALES `E`); what the Euler data supplies is the **circle RADIUS `√q`** (the Frobenius weight =
  base-field size, `α·α†=q` the Satake relation DH lacks; `Σ|αᵢ|²=2gq` exact on-circle). **THE DECISIVE
  GAP, named:** over `𝔽_q` the radius `√q` is an EULER datum (Frobenius weight) so off-circle is an
  Euler-ANCHORED modulus and inertia IS Euler-movable; over `ℤ` the analogue radius `Re s=½` is the FE
  FIXED LOCUS, NOT supplied by any Euler datum (`Λ(n)` doesn't set it; it is the FE-invariant DH-shared
  `A`) ⟹ the modulus defect is measured against a FE-borne radius ⟹ Sylvester-LOCKED to `A` (the 31
  confs). So the missing `ℤ`-object is NOT "an even form with movable inertia" (the FF has one) but
  specifically **an Euler datum over `ℤ` that SETS the critical radius `Re s=½` the way `q` sets `√q`** —
  but `Re s=½` is the FE fixed locus, Euler-INDEPENDENT (DH-shared). = `W_∞≥Σ_p W_p` sharpest: the primes
  must SET THE LINE, but over `ℤ` the line is set by the FE not the primes. **Verdict: Euler-borne YES
  (radius `√q` = Frobenius weight), sees-zeros YES (off-circle flips inertia), independent NO (modulus
  defect off the spectrum = Weil positivity) → CIRCULAR. 32nd wall confirmation — the FIRST to exhibit
  Euler-movable inertia CONCRETELY and locate the gap as "Euler sets the radius over `𝔽_q`, the FE sets
  it over `ℤ`."** **DECISIVE LESSON:** the corrected NEXT #1 framing was right that the FF escapes the
  Sylvester lock (its inertia genuinely moves) but the escape is FF-specific for ONE reason — the Euler
  product OWNS the radius `√q`. Re-specifies the program: the open object is not "movable inertia" (had)
  but **the RADIUS being Euler-borne** (new NEXT #1: is any ζ-intrinsic critical radius read off the
  primes not the FE? — the certificate ladder, Euler→edge `Re s=1`, FE→centre `Re s=½`); and the `q→1`
  degeneration now tracks `√q→1` as the invariant (new NEXT #2). Honest subtlety: `g=1` (`2×2`), so
  on-circle is the semidefinite `(0,1,1)` (the `+0` is the trace-removal kernel); load-bearing EXACT
  facts are neg eig `=−2gq`, the flip `(0,1,1)→(1,0,1)`, the EXACT flip-eig `=Σ|αᵢ|²−2gq`, the `r↔1/r`
  invariance, and the generic-pairing same-flip — none depend on the dimension. "Euler-movable inertia
  is real in the FF" is a POSITIVE structural finding (refutes the alternative negative); the CIRCULAR
  verdict is over `ℤ` (modulus defect against an Euler-set radius the primes don't supply over `ℤ`).

- **2026-06-06 — Audited NEXT #1's FALSIFIER-IN-ADVANCE itself ("the missing ℤ-surface self-pairing
  must be conjugation-ODD") in the ONE place the `C×C` Hodge-index mechanism is a THEOREM (the function
  field) and REFUTED it as a requirement: Weil forces the line with a conjugation-EVEN positive form.
  The agenda's "two walls (Sylvester + conjugation-evenness)" collapse to ONE — the conjugation wall was
  a MIS-NAMING of the inertia-degeneracy of an even form.** [META/STRUCTURAL · load-bearing → corrects the
  agenda's framing; ONE wall = Sylvester inertia]. `scripts/numerics/witness/conjugation_parity_ff.py`
  (+ 1 `falsify.py` row), `research/log/2026-06-06-conjugation-parity-ff.md`. **Finding [THM-flavored +
  computed, EXACT integer Weil polynomials, 4 curves g=1,2 over `𝔽_{2,5,7,11}`]:** (1) the **Rosati
  involution `†:α↦q/α` IS the FF complex conjugation** — on `|α|=√q`, `q/α=ᾱ`, verified `α†=conj(α)` all
  eigenvalues — so it is EXACTLY the agenda's "conjugation" (`ρ↔ρ̄`), and RH ⟺ `α†=ᾱ ∀i`. (2) **Weil's
  line-forcing form `Tr(φφ†)` is maximally conjugation-EVEN:** its Frobenius diagonal
  `⟨F,F⟩=Σᵢαᵢαᵢ†=Σᵢq=2gq` (each term `α·(q/α)=q` EXACTLY, RH-blind constant `10,14,22,8`); odd part
  identically 0, `F_even` invariant under `J:α↦q/α` verified. (3) **the unique conjugation-ODD spectral
  datum `u=Σ log(α²/q)` (the orientation) FLIPS sign under `†`** (`u(J-set)=−u(set)` verified) **and
  VANISHES on every FE-symmetric Weil spectrum** (`Re u≈10⁻¹⁶`, all 4 curves) — the SAME `E_signed≡0`
  conjugation cancellation that closed the static (DONE #25) AND dynamical (DONE #30) branches.
  **DECISIVE CORRECTION:** the agenda's "must be conjugation-ODD" is REFUTED — the archetype that WORKS
  forces the line with an EVEN form. Weil reads the **SIGNATURE/inertia degeneration** of an even
  positive-SEMIdefinite form (line = its kernel locus, `Δ⊥·Δ⊥` from `<0` to `=0` on-circle), NEVER one
  zero's side (no odd functional exists in his proof). "Conjugation-odd" was a MIS-NAMING of the
  inertia-degeneracy of an even form; the two "walls" are NOT independent. **Verdict (meta-audit, not a
  positivity candidate): the FF archetype is itself CIRCULAR over `ℤ`; the load-bearing output is the
  PARITY structural fact. 31st wall confirmation, the first to correct the agenda's framing to ONE wall
  (Sylvester inertia).** **DECISIVE LESSON:** RH needs an EVEN positive form whose **inertia is MOVABLE
  by the Euler/prime data** (so a planted off-line pair degenerates the signature), NOT a conjugation-odd
  form. Re-specifies NEXT #1 (drop "conjugation-odd"; the test is "inertia not Sylvester-locked to the
  DH-shared `A`, but moved by the primes") and re-reads `operator_domination.py` (DONE #27) as the
  sharpest statement of the single wall (new NEXT #2: build the `𝔽_q→1` degeneration of the
  primitive-part negative-definiteness with the prime data supplying the polarization). Honest subtlety:
  the parity facts are EXACT identities (`α·α†=q`, `r∘J=1/r`), curve-independent; the genus-2
  `T⁴−T³+2T²−2T+4` is a valid `q=2` real Weil polynomial; the `2πi` branch ambiguity sits in `Im u`,
  irrelevant to the (modulus-orientation) parity; this resurrects NO closed candidate, it re-specifies
  the OPEN target more accurately.

- **2026-06-06 — Built the dBN open object (NEXT #1): a FLOW FUNCTIONAL built from `Λ(n)` that should
  be MONOTONE toward reality under the dBN flow (a *dynamical* `W_∞≥Σ_p W_p`, escaping both defects of
  the RT/GUE lever), and CLOSED the dynamical branch — the candidate SPLITS exactly as pre-tested:
  modulus-monotone + Euler-borne but `sign Im`-blind/circular, and the only `sign Im`-sensitive reading
  is annihilated by the FE conjugation. Distinct endpoint on inertia, SAME wall on the Euler/location
  axis.** [CONSTRUCT · load-bearing → dBN frontier closed; program returns to the static surface].
  `scripts/numerics/witness/dbn_flow_functional.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-dbn-flow-functional.md`. **Finding [computed+THM-flavored, falsifier
  CIRCULAR/split]:** the dBN generator `e^{−tD²}`/log-gas is EULER-FREE; `Λ(n)` enters dBN ONLY via the
  initial datum, so a "flow functional from `Λ(n)`" can only be the Euler data RIDING PASSIVELY on the
  flowing config. Candidate `E_Λ=Σ_γ Im P(γ)`, `P(γ)=Σ_n Λ(n)/√n e^{−σ²(log n)²}cos(γ log n)` = the
  off-line PRIME defect of the Weil explicit formula on the dBN-flowed zeros. **(i) modulus reading
  `Σ|Im P|`:** Euler-borne YES (sign-scramble `Λ`→`|diff|=1.33`), sees-zeros YES (`0.0`→`0.286`
  on→off-line; corr `+1.00` with `max|Im root|` under flow), but `|·|` is a MODULUS (symmetric under
  `γ↔conj γ`, measures HOW FAR not WHICH SIDE) and `→0 ⟺ Λ≤0 = RH` = weil_form PSD-iff-RH → INDEPENDENT
  NO → **CIRCULAR**. **(ii) signed reading `Σ Im P`** (the only one seeing `sign Im`): **IDENTICALLY 0**
  on any FE-symmetric config (verified `max|E_signed|=0.00e0` across the flow) — the `+Im`/`−Im`
  conjugate zeros CANCEL = the conjugation symmetry `ρ↔ρ̄` that closed the whole real-form family
  (DONE #25). **(iii) the flow gives NO independent help:** the Euler-free generator decides reality,
  the primes only WATCH. **Verdict: Euler-borne YES, sees-zeros YES, independent NO → CIRCULAR;
  the `sign Im`-reading vacuous.** No Euler-borne flow functional is reality-MONOTONE under the
  Euler-free dBN flow → the dynamical `W_∞≥Σ_p W_p` does NOT materialize. **30th wall confirmation,
  closing the dBN frontier.** DECISIVE LESSON: the dynamical branch is genuinely distinct on the
  *inertia* axis (the anchor's real finding — the flow escapes Sylvester) but the open object it named
  hits the IDENTICAL conjugation wall — `sign Im` is conjugation-ODD, every Euler-borne functional is
  conjugation-EVEN (a modulus); the flow generator carries no primes; the primes ride passively. Returns
  the program to the static surface frontier (new NEXT #1 surface representability, #2 A5 reflection,
  #3 the conjugation-odd Euler-borne polarization). Honest subtlety: flow demos use small synthetic
  polynomials (flow exact on polynomials); the load-bearing facts are the EXACT conjugation
  cancellation `E_signed≡0` (any FE-symmetric multiset, basis-independent) and the Euler-borne diff
  `1.33`, not the small-config numerics; `E_modulus`'s reality-tracking is by construction (trivial),
  the content is that the `sign Im` reading is annihilated.

- **2026-06-06 — Did the dBN ANCHOR (NEXT #1) and folded in the GUE kill-test (NEXT #4): mapped
  Rodgers–Tao's mechanism precisely, made the forward/backward asymmetry and the GUE-universality
  EXECUTABLE, and reached the verdict — the dynamical branch is genuinely DISTINCT on the INERTIA
  axis (the flow `e^{−tD²}` ESCAPES the Sylvester `*`-congruence lock that closed every static form),
  but its only unconditional lever (GUE/Montgomery pair correlation) is UNIVERSAL/RH-silent and
  wrong-direction, so `Λ≤0`=RH reduces to the SAME per-zero location/phase wall `W_∞≥Σ_p W_p`.**
  [ANCHOR · load-bearing → dBN branch audited; distinct endpoint, same wall].
  `scripts/numerics/witness/dbn_anchor.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-dbn-anchor.md`. **Finding [THM+computed, falsifier DISPERSING]:**
  RT (arXiv:1801.05914) prove `Λ≥0` by CONTRADICTION — assume `Λ<0`, the backward log-gas flow
  `d/dt x_j=−2Σ 1/(x_k−x_j)` forces local equilibrium (AP/picket-fence spacing) at `t=0`, contradicted
  by Montgomery GUE pair correlation `1−(sin πu/πu)²` (zeros too repulsive/rigid to have equilibrated).
  **WHY `≥` NOT `≤`:** `≥` is a LOWER-bound-on-disorder = a STATISTICS (bulk/2-point/MODULUS) bound;
  RH=`Λ≤0` forbids a SINGLE off-line pair = a zero-LOCATION (`sign Im`/PHASE) bound a 2-point statistic
  cannot see (one off-line pair is measure-zero in pair correlation) — the SAME modulus/phase split that
  closed the static forms. **[Q1 COMPUTED] forward/backward asymmetry:** `Var(roots)` monotone in flow
  time (`2.500,2.580,2.660,2.740,2.820` at `t=−.02..+.02`); forward DISPERSES (`dVar=+0.16`), backward
  CONTRACTS (`−0.16`) — forward flow has NO Lyapunov purchase on reality. **[Q2 COMPUTED] the flow
  ESCAPES Sylvester:** `e^{−tD²}` is a 1-param semigroup on the POLYNOMIAL, not a `*`-congruence
  `Tᵀ(·)T`; it CHANGES the real-root count (a complex pair → all-real after flow, `Λ=0.186`) — the ONE
  place the dynamical branch is structurally NEW vs the closed static family. **[Q4 DECISIVE KILL-TEST]
  the GUE lever is UNIVERSAL, NOT Euler-borne:** computed small-gap depletion (level repulsion)
  `P(gap<0.25·mean)` = GUE `0.020` (pure Hermitian random matrix, NO Euler product) vs Poisson `0.220`
  (~11×) vs AP `0.000` — GUE-without-arithmetic carries the EXACT repulsion the RT contradiction needs
  ⟹ RH-silent on the Euler axis (lit.: DH off-line zeros have "essentially different" stats, but the
  GUE INPUT is the universality class). **Verdict: Λ sees-zeros YES, flow escapes Sylvester YES
  (distinct endpoint), BUT the unconditional lever Euler-borne NO (universal GUE), wrong-direction →
  DISPERSING; `Λ≤0` reduces to the SAME wall `W_∞≥Σ_p W_p` read dynamically. 29th confirmation, now
  from the dynamical side.** **DECISIVE LESSON:** the dBN route is NOT a reformulation (it has a genuinely
  different, non-inertia-locked endpoint — the flow is the first object in the whole audit to change the
  realness-count), but it stalls at the SAME place for the SAME reason: no Euler-borne object controls
  zero LOCATIONS. The precise open object it leaves = a **flow functional built from `Λ(n)` monotone
  toward reality** (a dynamical `W_∞≥Σ_p W_p`), which RT do NOT supply (their lever is the universal
  GUE statistics). Surfaces NEXT #1 (construct/falsify that functional), #2 (the prime↔flow coupling —
  Euler data enters dBN only via the initial datum, washed into the GUE bulk by the smoothing), #3
  (close-or-continue). Honest subtlety: variance/Sylvester demos use small synthetic polynomials (flow
  exact on polynomials; the structural facts — count-change, dispersion, GUE depletion `0.020` vs
  `0.220` — are robust + lit.-matched); the `≥`/`≤` asymmetry and GUE-universality are [THM]/literature.

- **2026-06-06 — Built NEXT #1's candidate (b), the RESONANCE KERNEL `K = VᵀV` (a Gram of the ZEROS,
  `V_{ρ,i}=φ̂(γ_ρ;cᵢ)`), and CLOSED the entire "form-carries-the-zeros" branch: `K` SEES the zeros but IS
  the Weil zero side (circular) AND reads the zeros directly, agnostic to the Euler product (NOT
  Euler-borne) — the dual of candidate (a)'s prime side, the two PINCER the wall.** [CONSTRUCT ·
  load-bearing → both single-form branches closed; the coupling is an INEQUALITY between the two sides,
  not a single form]. `scripts/numerics/witness/resonance_kernel.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-resonance-kernel.md`. **Finding [THM+computed]:** `K = VᵀV` is the
  **SYMMETRIC** Gram (NOT Hermitian `V*V` — the Weil form uses the even `ĥ(γ_ρ)`, no conjugation; this
  is load-bearing: symmetric off-line min eig `−0.0024` vs Hermitian `+1.4e-7` which would MISS the
  flip). **COMPUTED (5 centers, width 0.05, 200 ζ zeros):** TRUE zeros `sig(K)=(5,0,0)` PSD, min eig
  `+0.0067` (a Gram of REAL vectors); plant off-line `β=0.8` → one row of `V` COMPLEX, contribution
  `v vᵀ+v̄ v̄ᵀ=2(a aᵀ−b bᵀ)` INDEFINITE, `sig→(4,0,1)`, min eig `−0.0024<0` — **SEES-ZEROS YES**. **THE
  DECISIVE IDENTITY (verified to `1.4e-17`):** for any `x`, `xᵀKx=Σ_ρ g(γ_ρ)²` with
  `g(γ)=Σ_i x_i φ̂(γ;cᵢ)` — EXACTLY the Weil explicit-formula ZERO SIDE = `weil_form.py`'s spectral form.
  `K` is its Gram representation; PSD-ness of `K`= "every `γ_ρ` real" = RH, with NO independent
  certificate (`K=VᵀV` PSD iff `V` real iff zeros real; a certificate would BE a proof of RH) →
  **INDEPENDENT NO / CIRCULAR**. **AND NOT EULER-BORNE:** `K` is built from the ZEROS ONLY, never
  references `Λ(n)`; a DH-like zero multiset (off-line zeros, no Euler product) is equally constructible
  and gives `K` indefinite `(4,0,1)`, min eig `−0.009` — `K` reads whatever zeros it is handed, a
  ZERO-SIDE detector (like the Li coefficients), NOT an Euler-product detector. **Verdict: Euler-borne
  NO, sees-zeros YES, independent NO → DISPERSING (Euler axis) / CIRCULAR. 28th confirmation.**
  **DECISIVE LESSON — the two candidates PINCER the wall, branch CLOSED:** candidate (a) = the prime
  side `A−P` (Euler-borne YES, zero-location-blind, RH-silent); candidate (b) = the zero side `K=VᵀV`
  (sees-zeros YES, circular, NOT Euler-borne). **No finite-rank real/complex form is simultaneously
  Euler-borne, independent, AND zero-tracking** — zero locations live in the ZEROS, Euler data in the
  PRIMES; the only object coupling them is the INEQUALITY `W_∞ ≥ Σ_p W_p` (= the missing object).
  Re-promotes the cone-optimized scalar `W_∞ ≥ Σ_p W_p` place-count sweep to NEXT #1 as the FIRST
  candidate that is BOTH sides at once (an inequality, not a form). Honest subtlety: the flip needs a
  test-basis non-vanishing at `γ≈14–50` (`width 0.05`, not the wide `0.35` of `operator_domination.py`
  which collapses `K` to `O(1e-12)`); load-bearing EXACT facts are the identity `1.4e-17`, the
  symmetric/Hermitian split, the on→off flip `(5,0,0)→(4,0,1)`, and the DH-constructibility `(4,0,1)`.
- **2026-06-06 — Built NEXT #1's CORRECTED target DIRECTLY (the operator inequality `A ⪰ P`, the form
  `W = A − P` being NON-congruence so Sylvester is inapplicable) and REFUTED the agenda's hope: the
  arithmetic prime form `P` is zero-location-INDEPENDENT (`Λ(n)` is a property of the Euler PRODUCT, not
  the zeros), so `A − P` is a FIXED matrix that cannot flip; the only zero-bearing `P` is the spectral
  zero side = the Weil positivity (circular). NO single `P` is both Euler-borne-independent AND
  zero-bearing.** [ANALYTIC · load-bearing → candidate (a) closed; resonance-kernel (b) is the only
  surviving form-carries-zeros object]. `scripts/numerics/witness/operator_domination.py` (+ 1
  `falsify.py` row), `research/log/2026-06-06-operator-domination.md`. **Finding [THM-flavored+computed]:**
  built the two EXPLICIT Gram matrices `A` (archimedean `Γ_ℝ`) and `P` (prime `Λ(n)`) and the Weil form
  `W = A − P` — the FIRST object in the thread that is NOT a congruence `(plant)ᵀ(fixed form)(plant)` (it
  is a DIFFERENCE of two fixed forms, Sylvester structurally inapplicable). **COMPUTED (one-place 5-dim):**
  `sig(A)=(3,0,2)` INDEFINITE, `sig(P)=(5,0,0)` PSD (`Λ≥0`), `sig(W=A−P)=(1,0,4)`, `min eig(W)=−8.17`
  (`A ⪰ P` FALSE). **DECISIVE DICHOTOMY (exhaustive, no third option — same shape as
  `green_current_perturbation`/`square_representability`):** **(R1)** the ARITHMETIC `P` is built from
  `Λ(n)` = a property of zeta's EULER PRODUCT, NOT of where its zeros sit — there is NO 'plant an off-line
  zero' operation that changes `Λ(n)` while keeping ζ being ζ (verified `max|P_from(−ζ'/ζ)−P_from(Λ)|=0`,
  `P` has no `β`/zero-location knob). So the arithmetic `W=A−P` is a FIXED zero-INDEPENDENT matrix, its
  inertia CANNOT flip on/off-line — **Sylvester was never the obstruction here, there is no plant to apply
  it to.** Euler-borne YES (`max|A_ζ−A_DH|=0` exact DH-shared, `max|P_ζ−P_DH|=0.84` Euler-borne),
  sees-zeros NO → RH-SILENT. At one place `A ⪰ P` does not even discriminate ζ from DH (`sig W_ζ=(1,0,4)`,
  `sig W_DH=(2,0,3)`, both indefinite — `semilocal_2.py` coarseness). **(R2)** the ONLY `P` that carries
  the zero locations is the SPECTRAL `P_spec` = the explicit-formula ZERO SIDE `W=Σ_ρ ĥ(γ_ρ)`: PSD on true
  zeros (`min eig −0.0`), PSD LOST with a planted off-line zero (`min eig −1.49`) — it SEES the zeros, but
  it IS the zero side = PSD iff RH = the Weil positivity (CIRCULAR), and its `P` is whatever the zeros
  dictate (a different L-function's prime side, cf `green_current` CASE 2), NOT zeta's `Λ(n)`. **THE PIN:**
  NO single `P` is BOTH Euler-borne-independent AND zero-bearing; `A ⪰ P` is RH-silent for the arithmetic
  (Euler-borne) `P` and circular for the spectral (zero-bearing) `P`. **Verdict: Euler-borne YES,
  sees-zeros NO (arithmetic), independent NO (spectral=Weil) → RH-SILENT / CIRCULAR split. 27th
  Euler-product confirmation.** **DECISIVE LESSON:** the corrected NEXT #1 target ("the form must depend on
  the zero LOCATIONS, not be a congruence") is realizable ONLY as the zero side itself (circular) — the
  Euler-borne prime data `Λ(n)` is structurally zero-location-BLIND. Both halves of the program now meet:
  congruence self-pairings are inertia-locked (Sylvester, 26 confs); the non-congruence difference `A−P`
  is zero-independent for Euler-borne `P` and = the Weil positivity for zero-bearing `P`. Neither reaches a
  `P` simultaneously Euler-borne, independent, AND zero-tracking — that object is the cross-place coupling
  `W_∞ ≥ Σ_p W_p` itself. Surfaces the resonance-kernel candidate (b) as the only surviving
  form-carries-zeros object (new NEXT #1) and the cone-optimized scalar `W_∞ ≥ Σ_p W_p` place-count sweep
  (new NEXT #2). Honest subtlety: the `(1,0,4)` is the coarse one-place 5-dim model (NOT the true
  `(1,ρ−1)`); load-bearing EXACT facts are `max|A_ζ−A_DH|=0`, `max|P_from(−ζ'/ζ)−P_from(Λ)|=0` (arithmetic
  `P` zero-independent), `max|P_ζ−P_DH|=0.84`, and the spectral PSD flip `−0.0→−1.49`.
- **2026-06-06 — Built NEXT #1's CORRECTED target (the ORIENTED signed Hodge weight, on which complex
  conjugation acts non-trivially) and CLOSED the oriented/holomorphic escape: the signed Hodge form
  COLLAPSES (exact) to `Q=−iω`, a FIXED Hermitian background, and even a genuinely COMPLEX ORIENTED
  plant does not flip it — Sylvester holds for ANY invertible `*`-congruence, real OR complex.**
  [CONSTRUCT · load-bearing → the WHOLE self-pairing family is now exhausted; the form must depend on the
  zero LOCATIONS]. `scripts/numerics/witness/oriented_hodge_pairing.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-oriented-hodge-pairing.md`. **Finding [THM+computed]:** built the holomorphic
  `(1,0)` projector `P^{1,0}=½(Id−iJ)` and the ORIENTED signed Hodge weight
  `Q(x)=⟨P^{1,0}x,P^{1,0}x⟩_A−⟨P^{0,1}x,P^{0,1}x⟩_A` (NOT the conjugation-symmetric sum). **DECISIVE
  ALGEBRA (exact, even-`(p,q)` bases dim 8,10):** `Q=−(i/2)(AJ−JᵀA)`, and the `A`-orthogonality identity
  `JᵀA=−AJ` (`‖·‖≈5e-14`) COLLAPSES it to **`Q=−iω=−i·AJ`** — the ORIENTED form IS the Kähler 2-form, a
  FIXED Hermitian matrix (the imaginary part of the very `H=A+iω` `complex_structure_pairing` closed);
  the conjugation-SYMMETRIC sum is exactly `A` (`‖Q_sum−A‖≈5e-14`). So 'orientation' changes WHICH fixed
  Hermitian background (`−iω` vs `A`) but NOT the lock. **FALSIFIER:** (a) REAL FE-pair plant —
  `inertia(TᵀQT)` does NOT flip on/off-line (`(4,4,0)=(4,4,0)` dim8, `(5,5,0)=(5,5,0)` dim10). (b)
  **STEELMAN — genuinely COMPLEX ORIENTED plant `e^{iγu}`** (the `(1,0)` phase, NOT `cos(γu)`;
  `‖[T_c,J]‖≈16–22` genuinely J-coupled, `det≠0`): STILL no flip on/off-line AND does NOT distinguish
  `+γ` from `−γ` (the oriented form does not even see the plant's phase orientation). **REASON, the
  STRONGEST naming yet [THM]: Sylvester's law of inertia holds for ANY invertible `*`-congruence, REAL OR
  COMPLEX** (verified on generic complex Hermitian `Q`). So the wall was NEVER the reality of the PLANT
  (the agenda's hope that a complex/oriented plant escapes is WRONG) — it is that ANY
  `(plant)^*(fixed Hermitian form)(plant)` is inertia-locked, period. `inertia(Q)=inertia(−iω)`
  DH-shared (`A` FE-derived, `max|A_ζ−A_DH|=0`). **Verdict: Euler-borne YES (`op_diff≈1.80`), sees-zeros
  NO, independent NO → RH-SILENT. 26th Euler-product confirmation.** **DECISIVE LESSON:** orienting the
  FORM does not help because the lock is the **congruence structure of self-pairing**, not the reality of
  the data; the agenda's "reality is the disease" was correct that no real form encodes `sign(Im ρ)`, but
  the proposed cure (complex/oriented form + plant) fails for the stronger reason that Sylvester holds
  over ℂ. UNIFIES the WHOLE self-pairing family (symmetric `TᵀAT`, real-θ-twist `TᵀAΘT`, Hermitian
  `Tᵀ(A+iω)T`, oriented `T^*(−iω)T`; real OR complex plant) under ONE wall in its strongest form. **A
  flip requires the FORM the plant pairs against to itself DEPEND ON THE ZERO LOCATIONS** = the Weil
  coupling `W_∞≥Σ_p W_p` / the operator domination `A⪰P` (re-promoted to NEXT #1). Honest subtlety: the
  odd-`(p,q)` basis (dim 6) carries a `0.33` `A`-orthogonality residual; load-bearing EXACT facts are the
  even-`(p,q)` cases — `Q=−(i/2)(AJ−JᵀA)`, `JᵀA=−AJ`, the collapse `Q=−iω`, `Q_sum=A`, the no-flip of
  both real and complex/oriented plants, and the generic-matrix complex-`*`-congruence inertia
  preservation.
- **2026-06-06 — Built NEXT #1's CORRECTED target (the zeros enter the FORM, not the congruence) as the
  named non-congruence forms `T−Tᵀ`, `T−ΘTᵀΘ`, `[T,Tᵀ]`, and CLOSED it by a STRONGER obstruction than
  Sylvester: `sign(Im ρ)` is intrinsically COMPLEX and conjugation `ρ↔ρ̄` is a symmetry of all real
  data, so NO real form's inertia can encode it. The wall is REALITY, not the congruence-lock.**
  [CONSTRUCT · load-bearing → the entire REAL-form family closed; the phase needs an oriented/holomorphic
  form]. `scripts/numerics/witness/zero_in_form_pairing.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-zero-in-form-pairing.md`. **Finding [THM+computed]:** built three forms FROM
  `T`'s OWN entries (NOT congruences `(plant)ᵀ(fixed form)(plant)`, so Sylvester does not apply): the
  non-self-adjoint part `Ω=T−Tᵀ`, the FE-defect `Ω_θ=T−ΘTᵀΘ` (on-line ⟺ `T=ΘTᵀΘ` FE-self-adjoint), and
  the self-commutator/normality-defect `C=[T,Tᵀ]` (`=0` ⟺ `T` normal ⟺ real spectrum). **(1) EXACT
  vanishing:** the two-sided ζ-intrinsic prime-shift `T` is **EXACTLY symmetric AND FE-self-adjoint**
  (`‖T−Tᵀ‖=0`, `‖T−ΘTᵀΘ‖=0`, all bases — the `±log n` kernel `exp(−(cᵢ−cⱼ−u)²)+exp(−(cᵢ−cⱼ+u)²)` is even
  in `cᵢ−cⱼ`), so ALL `T`-built forms VANISH `(0,0,n)` on AND off line: no inertia to flip. **(2)
  STEELMAN — the genuinely NON-normal CAUSAL Frobenius operator** (one-directional `(Tf)(u)=Σ Λ(n)/√n
  f(u−log n)`, `‖T−Tᵀ‖≈4.6≫0`, `‖[T,Tᵀ]‖≈54≫0` genuinely non-normal): its `T`-built inertiae STILL do
  NOT flip — `sig(C)=(4,4,1)=(4,4,1)`, `sig(sym Ω_θ)=(0,0,9)=(0,0,9)`; `‖Ω‖,‖C‖` move only at the
  3rd–4th decimal (`β`-monotone noise, not line content). **Verdict: Euler-borne YES (`op_diff≈1.80`),
  sees-zeros NO, independent NO → RH-SILENT. 25th Euler-product confirmation.** **DECISIVE LESSON
  (supersedes the Sylvester congruence-lock), named:** the FE-forced Weil pair `(β,1−β)` is REAL and the
  zero pair `(ρ,ρ̄)` is CONJUGATION-SYMMETRIC; `sign(Im ρ)` is an intrinsically COMPLEX datum, and
  complex conjugation `ρ↔ρ̄` (mapping `+Im`→`−Im` at identical real weight) is a SYMMETRY of ALL real
  data, so **NO REAL form's inertia — congruence OR non-congruence, symmetric OR non-normal — can encode
  `sign(Im ρ)`.** Off-line-ness enters every real form only as `|ρ|`/`β`-symmetric MODULUS, never as the
  `sign(Im)` PHASE. The congruence-lock (DONE #1) was a *symptom*; the disease is **reality**. CLOSES the
  whole real-form branch (the corrected non-congruence escape does NOT help). **Points to the next
  axiom:** a form on which complex conjugation acts NON-trivially — a genuine Hodge `(p,q)` bigrading
  distinguishing `H^{p,q}`/`H^{q,p}` (oriented `(1,0)`-form / oriented polarization), NOT the
  conjugation-INVARIANT Hermitian `A+iω` of `complex_structure_pairing` (which kept inertia real). Honest
  subtlety: coarse chiral bases (dim 7,9,11); load-bearing EXACT facts are `‖T−Tᵀ‖=0`, `‖T−ΘTᵀΘ‖=0`
  (two-sided), and the no-flip of the genuinely non-normal causal `sig(C)=(4,4,1)`, `sig(sym Ω_θ)=(0,0,9)`,
  robust across bases.
- **2026-06-06 — Built NEXT #1/#2's named next axiom (the COMPLEX structure `J`, `J²=−Id`, making the
  intersection form HERMITIAN/Kähler) EXACTLY, and CLOSED it — STRONGER than the real-twist wall: the
  whole self-pairing family is exhausted because Sylvester's law of inertia is IDENTICAL for Hermitian
  forms.** [CONSTRUCT · load-bearing → complex/Hermitian route dead; the zeros must enter the FORM, not
  the congruence]. `scripts/numerics/witness/complex_structure_pairing.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-complex-structure-pairing.md`. **Finding [THM+computed]:** built the
  `A`-orthogonal complex structure `J` (`J²=−Id`, `JᵀAJ=A`) the agenda named. **EXACT facts (clean
  even-`(p,q)` bases dim 8,10):** `‖J²+Id‖≈1e-14`, `‖JᵀAJ−A‖≈1e-14`; the Kähler form `ω=AJ` is
  **EXACTLY antisymmetric** (`‖sym(AJ)‖≈1e-15`) with `‖antisym(AJ)‖≈6–7.6` — **the phase the real
  θ-twist could NOT carry** (`antisym(AΘ)=0` exact); and crucially **`‖[A,J]‖≈6.5 ≠ 0`** so `J` does NOT
  commute with `A` — it ESCAPES the predicted commute-and-relocate obstruction. `H=A+iω` exactly
  Hermitian (`‖H−H†‖≈1e-14`). **Load-bearing side-finding:** `A` is **INDEFINITE** (`sig(A)=(4,4,0)`,
  `(6,4,0)` — `Re ψ(¼+ir/2)` not sign-definite, `A^{1/2}` nonexistent), so I built `J=B⁻¹KB` via the
  signature operator (`A=BSB`, `K` `S`-orthogonal). **DECISIVE FALSIFIER (C4): NO FLIP.** Plant the
  FE-forced Weil pair, `‖[T,J]‖≈20`, `det T≠0`: the Hermitian inertia of `TᵀHT` does NOT flip on-line vs
  off-line — `(2,2,4)=(2,2,4)` (dim 8), `(3,2,5)=(3,2,5)` (dim 10), robust (holo projection identical).
  **STRONGER obstruction than real-twist FE-invariance, named [THM]: Sylvester's law of inertia is
  IDENTICAL for Hermitian forms.** The prime-shift plant `T` is **REAL** ⟹ `TᵀHT=T*HT` is a
  `*`-congruence ⟹ `inertia(TᵀHT)=inertia(H)` for `det T≠0` (verified directly AND on a generic
  Hermitian `H`: only a complex NON-`*` `T`-congruence moves inertia, producing a non-Hermitian matrix =
  wrong object); `inertia(H)` is built from the DH-shared `A` and FE-derived `J` ⟹ DH-shared. **Verdict:
  Euler-borne YES (`op_diff≈1.80`), sees-zeros NO, independent NO → RH-SILENT. 24th Euler-product
  confirmation.** **Decisive lesson:** promoting the self-pairing from symmetric to Hermitian does NOT
  escape the congruence-lock — it only enlarges the fixed background `H` whose inertia a real congruence
  cannot move. UNIFIES the whole self-pairing thread (symmetric `TᵀAT`, real-θ-twist `TᵀAΘT`, Hermitian
  `TᵀHT`) under ONE wall: any `(plant)ᵀ(fixed DH-shared form)(plant)` is inertia-locked by Sylvester,
  symmetric OR Hermitian. A flip requires the FORM the plant pairs against to itself depend on the zero
  LOCATIONS = the Weil coupling `W_∞≥Σ_p W_p`, reached from the Kähler/complex-structure side. **The
  complex structure is NOT the missing line-detecting freedom** — phase is real and present in `H`'s
  FIXED inertia, which a real congruence cannot vary. Honest subtlety: coarse chiral bases; dim-6
  odd-`(p,q)` carries a `0.33` orthogonality residual (the two even bases are the exact cases);
  load-bearing EXACT facts are `J²=−Id`, `JᵀAJ=A`, `sym(AJ)=0`/`antisym(AJ)≠0`, `[A,J]≠0`, `det T≠0`,
  `inertia(TᵀHT)=inertia(H)`, and no on/off-line flip.
- **2026-06-06 — Attacked NEXT #1's sharpened sub-target (a PHASE-carrying / `θ`-twisted self-pairing
  `Tᵀ A θ T` whose signature is NOT congruence-locked to `A`) and CLOSED the real-θ-twist route: the
  archimedean metric is FE-INVARIANT, which forces ANY real twist to be a symmetric congruence of `AΘ`
  (no phase) — the twist RELOCATES the Sylvester lock, it does not break it. Names a STRONGER obstruction
  than Sylvester and points to the COMPLEX structure `J` (`J²=−Id`).** [CONSTRUCT · load-bearing → real
  twist dead; phase needs a complex/Hermitian form]. `scripts/numerics/witness/theta_twisted_pairing.py`
  (+ 1 `falsify.py` row), `research/log/2026-06-06-theta-twisted-pairing.md`. **Finding [THM+computed]:**
  built the FE involution `θ:u↦−u` on a CHIRAL (one-sided) Gaussian basis where `Θ` is a genuine
  reflection (`‖Θ−Id‖=4`, `Θ²=Id` — avoiding the trap that on the θ-SYMMETRIC basis `θ=Id` collapses to
  the symmetric congruence). The twisted pairing `F_θ=TᵀAΘT` DOES move the signature off `sig(A)` (dim7:
  `sig(A)=(4,3,0)` vs `sig(F_θ)=(3,4,0)`), seemingly escaping Sylvester-on-`A`. **But the decisive
  structural computation is EXACT and kills it:** the archimedean Gram `A` is **FE-INVARIANT,
  `Θ A Θ = A`** (max diff `0`, because `Re ψ(¼+ir/2)` is EVEN in `r` = the FE `t↦−t`), which forces `A`
  and `Θ` to **COMMUTE** (`AΘ=ΘA`, `antisym(AΘ)=0` exact). Two exact consequences: (i) `F_θ=Tᵀ(AΘ)T` is
  SYMMETRIC and `Tᵀ antisym(AΘ) T=0` exactly — **the twist carries ZERO phase**; (ii) it is a symmetric
  congruence of the symmetric metric `B=AΘ`, so by Sylvester `sig(F_θ)=sig(AΘ)` for any invertible plant
  — the twist **RELOCATES** the lock from `A` to `AΘ`, does not break it. Plant-independence verified:
  `sig(sym(TᵀAΘT))=(3,4,0)` for ALL `β∈{0.5..0.9}` (det `T≠0`). **Falsifier (D3):** the twisted
  signature does NOT flip on-line (`β=½`) vs off-line (`β=0.6`, FE-forced Weil pair): `(5,4,0)` both,
  robust 3 chiral bases (dim 7,9,11). **Verdict: Euler-borne YES (op_diff≈1.80), sees-zeros NO,
  independent NO → RH-SILENT.** **23rd Euler-product confirmation.** Decisive lesson — a STRONGER,
  precisely-named obstruction than "Sylvester preserves inertia": phase is an antisymmetric/Hermitian
  datum, and **FE-invariance of the DH-shared archimedean `A` annihilates the antisymmetric part of any
  REAL θ-twist** — so a real symmetric self-pairing is always a modulus (congruence-locked), and the
  `(1,ρ−1)` phase cannot be carried by ANY real twist of the FE-invariant archimedean metric. Re-collides
  with the green-current dichotomy (perturbing `A` to break FE-invariance changes `L_∞` / the zero set).
  Points to the named next axiom: a **COMPLEX structure `J` (`J²=−Id`)** making `AJ` genuinely
  ANTISYMMETRIC (Hermitian intersection form, inertia NOT congruence-preserved) = the Kähler/Hodge
  `(1,ρ−1)` proper. Honest subtlety: coarse chiral bases; load-bearing EXACT facts are `ΘAΘ=A`,
  `antisym(AΘ)=0`, `Tᵀantisym(AΘ)T=0`, plant-independent `sig=(3,4,0)`, and no on/off-line flip.
- **2026-06-06 — Attacked NEXT #1's SHARPENED target (a NON-PRODUCT correspondence whose `H¹⊗H¹` does
  not split as `base⊗base`) via the ζ-intrinsic HECKE correspondence, and got a TWO-PART result:
  indecomposability is ACHIEVED (`‖[T,A]‖≫0`) but its symmetric self-intersection is a Sylvester
  congruence of the DH-shared archimedean metric, hence RH-SILENT.** [CONSTRUCT · load-bearing → prongs
  i & ii answered; obstruction renamed to "break the `A`-congruence"].
  `scripts/numerics/witness/hecke_correspondence.py` (+ 1 `falsify.py` row),
  `research/log/2026-06-06-hecke-correspondence.md`. **Finding [THM+computed]:** built the ζ-intrinsic
  Hecke-like correspondence = the explicit-formula prime side AS AN OPERATOR `(Tf)(u)=Σ Λ(n)/√n
  (f(u−log n)+f(u+log n))/2` (Eichler–Shimura: `Frob` IS such a correspondence; ζ being GL(1) has no
  Hecke eigenform, so this is the ζ-intrinsic surrogate). **(1) INDECOMPOSABILITY ACHIEVED (prongs i &
  ii):** `T` is genuinely NON-PRODUCT — `‖[T,A]‖~30–47 ≫ 0` (robust 3 bases) while the diagonal `Δ=Id`
  has `‖[Id,A]‖=0` EXACTLY; off-diagonality (the Hecke shift) supplies the non-product Néron–Severi class
  the agenda asked for, `H¹⊗H¹` via `Γ_T` does NOT factor as `base⊗base`. **(2) BUT the graph
  SELF-INTERSECTION washes it out:** `F=TᵀAT` is a CONGRUENCE of the archimedean metric `A` (`det T≠0`),
  so by **Sylvester's law of inertia** `sig(F)=sig(A)` for ANY plant; `sig(A)` is DH-shared
  (`max|A_ζ−A_DH|=0`), so the signature does NOT flip on- vs off-line with the FE-forced Weil pair
  (`(3,2,0)` both, robust 3 bases). The scalar self-int DOES move (`31519` on vs `29966` off) but that is
  monotone-in-`β` noise, NOT line-specific (signature is the genuine Weil content). **Verdict: Euler-borne
  YES, non-product YES, sees-zeros via scalar YES but SIGNATURE congruence-locked to DH-shared `A` →
  RH-SILENT.** **22nd Euler-product confirmation.** Decisive lesson: indecomposability of the OPERATOR is
  necessary but symmetrizing into the graph self-pairing `TᵀAT` (a NORM-SQUARE = the MODULUS) re-collapses
  to a congruence of `A`, blind to the line — the **SAME Sylvester-congruence trap** as the green-current
  route (CASE 1). Two distinct construction routes hit the identical obstruction: any object built as a
  congruence of the archimedean form is signature-locked → RH-silent. Renames the obstruction precisely:
  the missing `End(S²/ℤ)` must couple non-productness to the PHASE/reality — a `θ`-twisted/anti-symmetric
  pairing that BREAKS the `A`-congruence (Sylvester preserves inertia; phase must escape it), NOT a
  symmetric `TᵀAT`. Re-converges with the HEADLINE modulus⊗phase reading: `Γ_T·Γ_T=Tr(T^*T)` is a
  norm-square = the modulus, which cannot carry the `(1,ρ−1)` phase signature. Honest subtlety: coarse
  5–7 center basis; load-bearing EXACT facts are `‖[Id,A]‖=0`, `‖[T,A]‖≫0` (3 bases), `det T≠0`, and the
  Sylvester congruence `sig(TᵀAT)=sig(A)` (verified directly, plant-independent, basis-robust).
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
