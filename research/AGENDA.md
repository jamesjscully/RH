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

## NEXT — THE RESIDUE: the archimedean weight-monodromy (the irreducible atom)

**State (keystone pass complete, honest terminus reached).** The full framework is built + validated;
RH is peeled to ONE irreducible atom: **the even split `|α|=|β|` = the Frobenius is a fixed point of the
polarization involution = purity = the archimedean weight-monodromy.** Every framework piece (cup product
`E`, the `*`-involution, the determinant edge `αβ=p^{k-1}`, the Hodge–Riemann implication) is FREE/Euler-
borne; the radius is the residue. **This pass attacks the residue itself — frontier characterization, not
an expected proof.** The precise shape: over `𝔽_q` the even split is forced by the **weight-monodromy** —
Deligne's nilpotent `N` (geometric monodromy) whose filtration = the weight filtration (Weil II). *Is
there an archimedean nilpotent `N` whose weight filtration forces `|α|=|β|`?* **R3 (DONE) converted the
residue once more:** the Connes–Consani scaling site SUPPLIES the `ℝ_{>0}^×`-grading R2 named-missing, yet
its radius is the FE/Haar self-dual axis (DH-shared, free), not the arithmetic `q` — over `𝔽_q` the `q` is
the DISCRETE Frobenius gap, while the archimedean scaling is CONTINUOUS. The residue is now the
**DISCRETE/GAPPED base size at `∞`** = the analogue of "the residue field is finite" (`|𝔽_q|=q`).

R3b. **[RESIDUE · the DISCRETE/GAPPED base size at `∞` — NOW THE TOP ITEM, sharpened by R3]** R3 (DONE)
   PROVED the Connes–Consani scaling site **DOES** carry R2's named-missing `ℝ_{>0}^×`-grading (`θ=t∂_t`,
   the absolute Frobenius `Fr_λ`) AND marks a distinguished radius `Re s=½` — but that radius is the
   **FE/Haar SELF-DUAL axis** (DH-shared: the DH surrogate has a FE ⟹ the same `½`), **NOT** the arithmetic
   `q`: over `𝔽_q` the scale `q=|𝔽_q|` is the **DISCRETE Frobenius GAP** (the marked generator of `q^ℤ`),
   while the archimedean scaling `ℝ_{>0}^×` is **CONTINUOUS / homogeneous** (no marked generator, gapless
   spectrum `t^{iτ}`). **R3 CONVERTED the residue:** it is NOT "an `ℝ_{>0}^×`-grading" (the scaling site
   supplies it) but a **DISCRETE/GAPPED refinement carrying a finite base size — the archimedean analogue
   of "the residue field is FINITE" (`|𝔽_q|=q`)**. The continuum-to-discrete datum: a *spectral gap* at `∞`
   playing the role `|𝔽_q|=q` plays over `𝔽_q`. **R3b's task:** is there ANY archimedean spectral gap / a
   discrete refinement of the scaling action (a `ℚ_{>0}`-graded line à la `𝔽₁`/GANTM, the K6 non-metric
   degree, a Bost–Connes-type discrete-multiplier on the scaling site) reproducing the FF Frobenius gap
   `q^{k/2}` on `gr^M_k`? Anchor: build the FF discrete `q^ℤ` in the same language; deform `q→1` and ask
   what survives. (Falsify: the gap must be DH-distinguishing — DH's continuous scaling has the same
   gapless self-dual axis, no gap to match.)
R4. **[RESIDUE · the missing operator — PARTLY DONE by R1, residual = the EXISTENCE/construction; re-pointed
   by R3 to the CONTINUITY obstruction]** R1 STATED the four axioms (N1)–(N4) AND located the obstruction;
   R2/R3 showed both candidate archimedean structures (Schmid's Hodge `N`, the scaling generator `θ`) supply
   (N1)–(N3)+a FREE marked radius but NOT the arithmetic `q`, for the SAME reason: the archimedean place is
   **continuous** (no finite residue field). The residual R4 question, re-pointed: is there ANY construction
   supplying a `q`-carrying archimedean object — a degeneration of the would-be motive of `ζ` (`S²/ℤ`, M2d),
   a discrete refinement of the scaling site (R3b), a Bost–Connes / quantum-statistical `q`-multiplier — or
   is the **continuity of the archimedean scaling** (the `𝔽₁`-analogue of "`Spec ℤ` has no constant field /
   no finite residue field at `∞`") the precisely-located irreducible obstruction? Falsify: the putative `N`
   must fail to exist for DH
R4. **[RESIDUE · the missing operator — PARTLY DONE by R1, residual = the EXISTENCE/construction]** R1
   already STATED the four axioms (N1)–(N4) an archimedean `N` must satisfy AND located the obstruction
   (`ℤ` lacks the geometric degeneration `𝔽_q` uses to supply `N`; DH fails at (N3): no `W`). The residual
   R4 task is now narrower: given R2/R3's verdicts, is there ANY construction supplying an `N` meeting
   (N1)–(N4) — a degeneration of the would-be motive of `ζ` (the `S²/ℤ` surface, M2d), a real-analytic
   limiting structure, or a scaling-site nilpotent — or is the non-existence of such a degeneration over
   `ℤ` the precisely-located irreducible obstruction? Falsify: the putative `N` must fail to exist for DH
   (R1 confirmed: (N3) vacuous for DH).
R5. **[SYNTHESIS — the shape of the missing idea]** Either a genuine archimedean `N` (a real lead), or
   the precisely-located obstruction = the single thing whose construction is the open problem. This is
   the true terminus: the residue characterized to the atom, the missing idea's shape named.

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

## NEXT — THE KEYSTONE: force `P_∞ ⪰ 0` (`c=D`) by an archimedean Kähler / Hodge–Riemann structure

**State (build pass complete).** The whole polarized arithmetic Hodge category is BUILT and validated
on the FF anchor (M1–M4, to genus 2). The genuinely-new structure is invented: `P_∞(x,y)=S(C_W x,κ y)`
(M3) — the archimedean `(p,q)` polarization via the Weil/Hodge `C`-operator `C_W`, categorical (NOT a
metric), Frobenius-free. **RH = archimedean `c=D` = `P_∞ ⪰ 0` (M3b).** The entire edifice now rests on
ONE positivity. **It is NOT circular to attack** because in classical Hodge theory `c=D` is *forced* by a
**Kähler form** via the **Hodge–Riemann relations** — and a Kähler form is a *geometric* datum, not the
zeros. So the keystone is *construct one geometric form*, with Hodge–Riemann doing the forcing.

K7. **[KEYSTONE · the redistribution falsifier — NOW THE SOLE LIVE KEYSTONE, named by M4r]** M4r (DONE)
   PROVED a no-go on the descent: the global even split (`Re s=½`) is a **CONJUNCTION, NOT a rigidity** — a
   determinant-neutral, pairing-neutral **modulus redistribution** moves eigenvalues OFF the even split at
   several places while preserving EVERY Euler/FE datum (the global determinant `q^g` AND every Poincaré
   pairing). So the descent **cannot** read the centre off the Euler/FE data, and the radius relocates ENTIRELY
   onto the archimedean positivity `P_∞ ⪰ 0` — **the unique structure that fails under the redistribution.**
   MAKE THIS THE EXECUTABLE KEYSTONE TEST: on the FF anchor, compute `P_∞`/the Hodge–Riemann form on the
   redistributed (off-even) global `H^1` and confirm it goes INDEFINITE while the genuine (even) one is
   definite — establishing `P_∞ ⪰ 0` is the **ONLY discriminator** of the redistribution, hence `c=D ⟺` (no
   redistribution) `⟺` uniform `C_W` radius `⟺` RH. The keystone is now precisely: **force the uniformity of
   the `C_W` radius** (= "no balanced redistribution"), the one thing the descent provably cannot supply.
   (falsify: the redistribution must be DH-vacuous — DH has no `H^1`/determinant → no eigenvalues to
   redistribute → the discriminator `P_∞` has empty domain.)
K6. **[KEYSTONE · the scale as a NON-METRIC DEGREE, named by K2r-fix — RE-SCOPED by M4r]** Since the radius is
   `σ_d`'s **scale `d`** — a 1-dim *radial/degree* datum, NOT a phase and NOT (yet) a Gram form — and §0 forbids
   metrics: is there a **non-metric** Euler-borne structure (a *valuation* / a *graded line with a degree* — e.g.
   the determinant of Frobenius as a `ℚ_{>0}`-graded `𝔽₁`/GANTM datum, Connes–Consani) whose per-prime "size" is
   `√d` WITHOUT being a `*`-congruence of a fixed background? **M4r SHARPENED the bar:** a *degree* on a graded
   line is a function of the determinant (the PRODUCT of moduli), and M4r proved the product is invisible to the
   redistribution — so a *degree alone is RADIUS-SILENT for the same reason `κ` is.* K6 must therefore supply a
   per-place degree that is NOT a function of the global determinant (it must see the INDIVIDUAL moduli, which
   the redistribution shows no FE/Euler scalar does) — i.e. K6 collapses INTO K7 unless the graded structure
   carries a positivity. (falsify: must distinguish the redistributed config the determinant cannot.)
K2. **[KEYSTONE · condensed — RE-POINTED by K2r-fix: the RADIUS/DEGREE carrier, not the reality datum]** Realize
   the archimedean structure in **condensed/analytic geometry** (Clausen–Scholze; F. Charles' stack-of-norms).
   K2r-fix settled the reality datum: the condensed object supplies `c_0` (the phase, FREE, radius-silent) — it
   must ADDITIONALLY carry the **scale/degree `√d`**, which is NOT a conjugation. So the condensed framework's
   contribution to the keystone is the **radius/degree carrier** (the canonical Weil operator `C_W`'s RADIUS,
   not its phase `(−1)^w`, and not the free involution `σ_d`). This is the one framework flagged right-kind-
   untried — now with the radius/scale (not the reality, now settled free) as the precise target.
K3. **[KEYSTONE · the forcing lemma — SHARPENED by K1, then by M4r]** The forcing lemma "archimedean Kähler ⟹
   `c=D`" is the **FORMAL** Hodge–Riemann implication `(E, C_W)` polarized ⟹ `P_∞ ⪰ 0` (K1: the hardness is NOT
   here). BGS §6.3 (positive Green form can fail) is EVADED because `P_∞` is the categorical pairing `E(C_W·,·̄)`,
   not a metric — but the hardness RELOCATES into supplying `C_W`'s radius (K2r). **M4r pins the hypothesis
   exactly:** the forcing lemma's input "`C_W` has UNIFORM radius" is precisely "no balanced modulus
   redistribution", and M4r proved that uniformity is NOT a function of the determinant/FE data — so K3's open
   problem is entirely: **force the uniformity of the `C_W` radius**, identical to K7. State K3 as: the forcing
   is free GIVEN `C_W`'s uniform radius; the open problem is supplying that uniformity (the redistribution-free
   condition), which the descent provably cannot.
K4. **[FALSIFY]** `P_∞` / the Kähler class for **Davenport–Heilbronn**: does it FAIL to exist (no Euler
   product ⟹ no Frobenius weight ⟹ no `C_W` ⟹ no Kähler)? Run `falsify.py`: sees-zeros (via `c=D`),
   DH-failure (structural).
K5. **[SYNTHESIS]** Verdict: does the archimedean-Kähler keystone **force RH**, or does it locate the
   single irreducible geometric residue (the one form whose existence is the open problem)? Either is the
   honest terminus of the construction.

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

M3c. **[INVENT · condensed upgrade]** Realize `(V, F^•, κ)` as a **condensed/analytic** object (Clausen–
   Scholze) so the "condensed-archimedean structure Arakelov lacks" (§2 Pillar A) is explicit, not just
   finite-dim linear algebra — the archimedean place as a condensed `(p,q)`-datum. Falsify: still
   §0-clean (duality pairing, not a metric), still Euler-silent-by-design (the `Γ`-factor). **M3b sharpened
   the target:** the Weil operator `C_W` and the central twist `C_W²=(−1)^w` (a SIGN, the weight parity)
   must be the condensed structure maps — the `(−1)^w` carries *only reality*, NOT the radius (radius-silent
   at `∞`), so the condensed object is the radius-free reality carrier.
M4r. **[DESCENT · the radius-assembly hinge, named by M3b]** M3b's structural lesson: the FF multiplier is
   the Frobenius weight `q` (carries the radius `√q`, Euler-borne), but its archimedean mirror `(−1)^w` is a
   SIGN (carries only reality, radius-silent). So the centre `Re s=½` CANNOT be read off the archimedean
   place — it must be **Euler-assembled in the descent**, where the prime Satake products `αᵢ(p)αⱼ(p)` meet
   the archimedean `(−1)^w` sign. Specify, in the M4 gluing, the precise map by which the per-prime radius
   data (`√q`-analogues) ASSEMBLE the global centre against the radius-silent `(P_∞,D,c)` at `∞`. (= C3b in
   its sharpest cross-place form; falsify: the assembled radius must be DH-distinguishing, an Euler datum.)
M4. **[DESCENT · fully typed by M4A/B/C; archimedean input `P_∞` now built (M3)]** Specify the **duality-descent gluing**: how `{Euler factors at
   primes} ∪ {Γ_ℝ (p,q) at ∞}` glue to a global object whose polarization **is** the explicit-formula
   quadratic form (so `W_∞≥Σ_p W_p` is a descent constraint, not a hope). **Target now fully typed:** the
   global **weight-2 NS lattice `gr^W_2`** of `S²/ℤ` — a rigid dualizable lattice (M4C: `D∘D≅id`) whose
   polarization is the **canonical evaluation `P_NS=ev∘(1⊗φ_{FE})=Tr(z w^†)` of its duality, NOT a metric**
   (M4C: `=0` exact, §0-clean), with the Hodge index on NS-primitives = RH. The descent must
   **Euler-ASSEMBLE the form `(*)`** (M4B) on this lattice from the Satake products `αᵢ(p)αⱼ(p)` across ALL
   primes (M2d: no single prime supplies it), i.e. realize `P_NS` for `ζ` as the cross-place coupling. The
   **purity functor** `(·)^{1/2}` then descends the weight-2 edge `|αᵢαⱼ|=q` (`Re s=1` of `f×f̄`, the
   Petersson pole) to the weight-1 centre `|αᵢ|=√q` (`Re s=½`). C3b = "the Euler assembly SETS the centre
   `Re s=½` the way `q` sets `√q`", Euler-sourced, NOT borrowed from the FE.
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

- **2026-06-06 — R3 [RESIDUE · DEF · coherence-checked vs 𝔽_q]: PROVED the Connes–Consani scaling site
  SUPPLIES R2's named-missing `ℝ_{>0}^×`-grading (`θ=t∂_t`, the absolute Frobenius) AND marks a
  distinguished radius `Re s=½`, but that radius is the FE/Haar SELF-DUAL axis (DH-shared, FREE), NOT the
  arithmetic `q` — over `𝔽_q` the `q=|𝔽_q|` is the DISCRETE Frobenius GAP, while the archimedean scaling
  `ℝ_{>0}^×` is CONTINUOUS/homogeneous (gapless, no marked `q`); the residue CONVERTS from "an
  `ℝ_{>0}^×`-grading" to a "DISCRETE/GAPPED base size at `∞`" = the analogue of "the residue field is
  finite" (`|𝔽_q|=q`).** [RESIDUE · DEF · coherence-checked vs 𝔽_q].
  `research/construction/R3-scaling-site-radius.md`, `scripts/numerics/witness/scaling_site_radius.py`
  (+1 `falsify.py` row → 37th wall, DISPERSING-by-design = Euler-silent characterization, like R1/R2/M2d).
  **What got CHECKED (exact mpmath 40dps; `w=1`):** **[A]** the scaling site carries the `ℝ_{>0}^×`-grading
  Schmid's `N` lacked — `θ(t^s)=s·t^s` verified (`|lhs−rhs|~1e-20` at `s=½, ½+14.13i, 2`), and the
  `|·|^{1/2}`-normalized unitary axis MARKS `Re s=½` (fixed point of `s↔1−s`). R2's demand "produce a
  SCALE not just a centering" is MET. **[B]** but `½` is the FE/Haar SELF-DUAL point: Haar `d*t=dt/t`
  inversion-symmetric (density ratio `==1`), and the SAME scaling site / self-dual `½` arises for the DH
  surrogate (FE, no Euler product) — `ζ`-axis `= DH`-axis `= ½` exactly, DH-SHARED. **[C]** FF contrast:
  over `𝔽_q` the scaling is the DISCRETE `q^ℤ`, `q=|𝔽_q|≥2` the residue-field cardinality MARKING the scale
  and forcing `|α|=q^{w/2}` (computed `2,3,5` for `q=4,9,25`); the archimedean `ℝ_{>0}^×` is
  HOMOGENEOUS/transitive (verified `marked_q_exists=False`), gapless spectrum `t^{iτ}` (all modulus 1) — no
  marked `q`. The crux: **`q` is the SPECTRAL GAP of the discrete Frobenius `q^ℤ`; the archimedean scaling
  has CONTINUOUS spectrum (no gap)**. **[D]** the Connes–Consani spectral realization (zeros = scaling
  spectrum, RH = "spectrum on the axis `½`"; on-line all-on-axis, off-line max dev `0.2`) is EQUIVALENT to
  RH, not a proof — the site supplies the grading + marks the axis (N1–N3), leaves OPEN whether the spectrum
  sits on it (N4). **Falsifier verdict:** EULER-BORNE NO on this pass (the scaling-`½` is the FE/Haar
  self-dual point, DH-shared — DH has a FE hence the same axis, CANNOT be the discriminator; the
  DH-distinguishing datum is the arithmetic gap `q` the continuous scaling lacks), SEES-ZEROS YES (only via
  "spectrum on the axis" = N4 = RH), INDEPENDENT NO (the realization = RH = the solved case over `𝔽_q` via
  the discrete Frobenius) → DISPERSING-by-design, DH ladder `DH=ζ` on the scaling self-dual axis `< FF`
  (which adds the discrete Frobenius gap `q`). **NEW content:** the M3b/R2 lesson made precise at the
  scaling-site / `𝔽₁` altitude — the scaling site reaches *exactly as far as Schmid* (the grading + a FREE
  marked radius) and the irreducible residue is the same atom but now sharply named: an **arithmetic,
  finite, GAPPED base size at `∞`** (the analogue of `|𝔽_q|=q`), which neither the continuous archimedean
  scaling nor the Hodge SL(2)-orbit supplies. The obstruction is the **continuity of the archimedean place**
  (the `𝔽₁`-analogue of "`Spec ℤ` has no finite residue field at `∞`"). **Successors added:** R3b promoted
  to TOP ITEM [the DISCRETE/GAPPED base size at `∞`: is there an archimedean spectral gap / discrete
  refinement of the scaling action — a `ℚ_{>0}`-graded line, the K6 non-metric degree, a Bost–Connes-type
  discrete multiplier — reproducing the FF Frobenius gap `q^{k/2}`?]; R4 re-pointed to the CONTINUITY
  obstruction (both archimedean candidates fail for the same reason: the archimedean place is continuous /
  has no finite residue field).

- **2026-06-06 — R2 [RESIDUE · DEF · coherence-checked vs 𝔽_q]: PROVED Schmid's SL(2)-orbit `N`
  supplies (N1)–(N3) + the FREE weight parity `(−1)^w` but NOT (N4) the radius — the M3b lesson recurs;
  the missing archimedean `N` must couple the `(p,q)`-grading to an ARITHMETIC SCALE `q` at `∞`, which
  the Hodge SL(2)-orbit (DH-shared, phase-only) cannot supply.** [RESIDUE · DEF · coherence-checked vs
  𝔽_q]. `research/construction/R2-schmid-sl2-orbit-radius.md`,
  `scripts/numerics/witness/schmid_sl2_orbit_radius.py` (+1 `falsify.py` row → 36th wall confirmation,
  DISPERSING-by-design on the SL(2)-orbit/Hodge half). **What got CHECKED (exact mpmath 40dps; weight-1
  HS; Jordan-structured `N`):** **[1]** Schmid's `N` gives (N1)–(N3) at `∞` — the `sl_2` symmetry of
  `M(N)=W` is pure Hodge/filtration data (NO zeros, NO `q`): Jordan `[1,1],[2],[3],[2,2]` → `M(N)=W`
  weights `[1,1],[0,2],[−1,1,3],[0,0,2,2]`, all symmetric about `w=1`. **[2]** its centering delivers the
  WEIGHT PARITY `C²=(−1)^w=−1` (a SIGN, M3b's phase), and (N4)'s radius `|α|=q^{k/2}` CANNOT be read off
  Schmid's `N` alone (`q_available=False`): a real/complex polarized HS carries no Frobenius eigenvalue,
  no base size `q`. **[3]** the parity is RADIUS-SILENT — `q=9` vs `q=25` give SAME parity `−1`, DIFFERENT
  radii `3` vs `5`; fixing parity does not pin `|α|`, the radius is ORTHOGONAL to the SL(2)-orbit phase
  datum (= K2r-fix). **[4]** FF cross-check: over `𝔽_q` the SAME Schmid `N` exists (degenerating curves)
  and the radius IS forced — but ONLY because the `ℓ`-adic Frobenius supplies `q` (centre radii `2,3,5`
  for `q=4,9,25`, from the Frobenius NOT Schmid's `N`); the Hodge/SL(2) data is IDENTICAL between `𝔽_q`
  and `∞`, the EXTRA ingredient is the base size `q`. **Falsifier verdict:** EULER-BORNE NO on this pass
  (the SL(2)-orbit/Hodge data is Euler-SILENT = the DH-SHARED archimedean structure: DH has the same
  `Γ`-factor/archimedean Hodge type, so Schmid's `N` exists for DH too and is radius-silent for BOTH — the
  SHARP DH verdict: Schmid's `N` is DH-shared, CANNOT be the discriminator, (N4)'s `q` is the only
  DH-distinguishing datum and Schmid does not carry it; `DH=ζ` on the SL(2) datum `< FF` which adds the
  arithmetic Frobenius), SEES-ZEROS YES (only via (N4), which Schmid lacks), INDEPENDENT NO (`M(N)=W ⟹`
  purity over FF) → DISPERSING-by-design: the SL(2)-orbit is the PHASE half (free, DH-shared,
  radius-silent), the radius is NOT here. **NEW content:** the M3b lesson made precise at the level of the
  monodromy `N` — Schmid's archimedean weight-monodromy theorem reaches (N1)–(N3) + parity but the radius
  `q^{w/2}` is an arithmetic datum no archimedean Hodge structure possesses; the residue is RE-SHARPENED to
  "an archimedean base size `q` coupling the `(p,q)`-grading to a modulus", exactly what R3 (Connes–Consani
  scaling/absolute Frobenius) must supply. **Successors added:** R3 promoted to TOP ITEM with the sharpened
  success criterion (the scaling `N` must carry an arithmetic scale `q` at `∞`, not another `(p,q)`
  centering); R3b [the arithmetic scale at `∞` as an `ℝ_{>0}`-graded line / valuation, connecting to
  `𝔽₁`/GANTM and the K6 non-metric degree — does any archimedean grading reproduce the FF Frobenius scale
  `q^{k/2}`?].
  **HARDENING (later same-day pass — the norm-estimate loophole CLOSED):** the original R2 argued "no `q`
  at `∞`" but did not engage **Schmid's NORM ESTIMATE** `‖v‖²_t ∼ (log 1/|t|)^{k−w}`, which superficially
  *is* an archimedean scale and could have rescued (N4). Added `[3b]` to the module + doc proving it
  **fails (N4) three independent ways** (exact, executed): **(i)** the growth exponent `k−w` *equals* the
  `M(N)`-weight shift = the `sl_2` `h`-eigenvalue — the SAME datum as the centering, no new info (verified
  `gr^M_{0,1,2}→` exponents `−1,0,1`); **(ii)** it is a DIVERGENT RATE, not a value — `(log 1/|t|)^1 =
  2.30, 6.91, 11.5` for `t=10^{−1},10^{−3},10^{−5}` (`→∞`, never `3` or `5`); renormalizing to a finite
  radius needs a FREE positive constant Schmid does not fix (`exponent_pinned=True, radius_free=True`) =
  exactly the missing `q`; **(iii)** it is a **METRIC** — Sylvester-inertia-locked by charter §0
  (DH-shared background) = the FORBIDDEN kind of scale. **Net:** R2's verdict is now rigorous against the
  obvious objection, and the R3 success criterion is **sharpened to three requirements** the SL(2)-orbit
  fails — the scaling `N`'s radius must be **(a) categorical not metric** (evade §0), **(b) a finite value
  not a divergent rate**, **(c) new beyond the centering exponent `k−w`**. (36th wall confirmation row
  updated accordingly; no new row.)

- **2026-06-06 — R1 [RESIDUE · DEF · coherence-checked vs 𝔽_q]: STATED the residue as the
  MONODROMY-WEIGHT question and ANCHORED the mechanism on 𝔽_q with NO zeros assumed — over `𝔽_q` the even
  split `|α|=q^{w/2}` is `M(N)=W` (the monodromy filtration of the GEOMETRIC nilpotent = the weight
  filtration, a THEOREM in the curve case), and the symmetry of `M(N)` — intrinsic to `N` by
  Jacobson–Morozov, using NO eigenvalue/zero — transports via `M(N)=W` to force purity; PINNED the
  archimedean `N` to four axioms and LOCATED the obstruction.** [RESIDUE · DEF · coherence-checked vs 𝔽_q].
  `research/construction/R1-weight-monodromy-residue.md`,
  `scripts/numerics/witness/weight_monodromy_residue.py` (+1 `falsify.py` row → 35, DISPERSING-by-design =
  Euler-silent characterization, like M2d/M3b). **MECHANISM (object-free):** a nilpotent `N` (`N^{m+1}=0`)
  has a UNIQUE monodromy filtration `M(N)` centered at `w` with `N^j: gr^M_{w+j}≅gr^M_{w−j}`
  (Jacobson–Morozov / `𝔰𝔩₂` Hard-Lefschetz) — SYMMETRIC about `w` BY CONSTRUCTION, using no zeros;
  weight-monodromy `M(N)=W` transports that symmetry to the weights (`|α|=q^{k/2}` on `gr^W_k`), so the
  `N`-primitive CENTRE (`j=0`) sits at EXACTLY `w` ⟹ `|α|=q^{w/2}` = the EVEN SPLIT (purity of the centre
  IS `M(N)=W` at `j=0`). **FF ANCHOR (exact rational lin alg, `g=1,2,3`, NO zeros):** built genuine `N` on
  `H^1` — (i) SMOOTH `N=0`, `M(0)={1:2g}` pure immediately; (ii) SEMISTABLE max-degenerate `[[0,0],[I,0]]`
  index 2, `M(N)={0:g,2:g}` symmetric (centre via `0↔2` pairing); (iii) PARTIAL (pinch `g−1`, keep 1
  abelian handle) `M(N)={0:1,1:2,2:1}` symmetric with the POPULATED weight-1 centre carrying 2 eigenvalues
  `|α|=q^{1/2}`, the even split VISIBLE. All symmetry computed from `N`'s Jordan structure (rank sequence),
  no zero read. **ARCHIMEDEAN `N` PINNED to four axioms:** (N1) nilpotent `N^{w+1}=0`; (N2) a `(−1,−1)`-
  morphism of the polarized HS (`N(F^p)⊆F^{p−1}`, `c`-compatible); (N3) `M(N)=W` (the archimedean weight-
  monodromy); (N4) RADIUS compatibility (on `gr^M_k` the `C_W` radius/scale `d` has modulus `q^{k/2}`).
  **OBSTRUCTION located:** over `𝔽_q` `N` is GEOMETRIC (the log of LOCAL MONODROMY of a degenerating family,
  a Picard–Lefschetz vanishing cycle, NOT a function of zeros); over `ℤ`/`∞` there is no degenerating family
  in hand to supply `N` — the open problem is UPSTREAM (supply the `N` whose `M(N)` could equal `W`, mirror
  of M2d's "build the carrier"). **Falsifier verdict:** EULER-BORNE NO on this pass (a characterization/
  anchor, Euler-silent like M2d/M3b — tabled DISPERSING-by-design), but the DH STRUCTURAL verdict is sharp:
  DH has no Euler product ⟹ no `W` ⟹ (N3) `M(N)=W` VACUOUS ⟹ the weight-monodromy structure `(N,W)` FAILS
  TO EXIST for DH at (N3); ladder `DH<ζ<FF`. SEES-ZEROS YES (even split = purity = where the zeros sit),
  INDEPENDENT NO (`M(N)=W ⟹` purity = Weil II = the solved case). **NEW content:** the residue is now a
  SINGLE geometric question — *is there an archimedean nilpotent `N` (a `(−1,−1)`-morphism of the polarized
  HS) with `M(N)=W` forcing the RADIUS?* — with the FF anchor proving the mechanism is
  `M(N)=W`-with-no-zeros, sharpening M3b/M4r's "radius must be Euler-assembled, never read off `∞`" to its
  precise positive form: the radius WOULD be forced if an archimedean `N` with `M(N)=W` existed, and that
  existence (the degeneration over `ℤ`) is the irreducible open object. **Successors:** R2 promoted to TOP
  (Schmid SL(2)-orbit: does its nilpotent satisfy (N4) — the radius — or only (N1)–(N3)+free parity?); R4
  re-scoped (R1 already did the axioms + obstruction; residual = the EXISTENCE/construction of `N`); R3
  sharpened (is the scaling generator nilpotent with `M(N)=W` at the right `q^{k/2}` scale?).

- **2026-06-06 — M4r [KEYSTONE · coherence-checked · anchored vs 𝔽_q / Δ]: executed the radius-DESCENT
  assembly at the GLOBAL altitude M2d proved is the right one (the single glued weight-1 carrier `gr^W_1`,
  not per-prime) and found a THEOREM-grade no-go: the global even split (`Re s=½`) is a CONJUNCTION, NOT a
  RIGIDITY — a determinant-neutral, pairing-neutral modulus REDISTRIBUTION breaks the even split at several
  places while preserving EVERY Euler/FE datum, so the descent CANNOT read the centre off the Euler/FE data;
  the radius relocates ENTIRELY onto the archimedean positivity `P_∞ ⪰ 0`.** [KEYSTONE · coherence-checked ·
  anchored vs 𝔽_q / Δ]. `research/construction/M4r-radius-descent-assembly.md`,
  `scripts/numerics/witness/radius_descent_assembly.py` (+1 `falsify.py` row → 34th wall confirmation, CIRCULAR
  with a no-go-on-the-descent). **The gap closed:** K2r/-split/-fix all worked PER PRIME (each prime's even
  split = Ramanujan/RH, circular per prime); M2d proved purity is intrinsically GLOBAL for `ζ` (no single prime
  carries `gr^W_1`). M4r asks the descent question at the right altitude: is the GLOBAL even split a RIGIDITY
  (radii at different places linked by Euler/FE, descent ADDS content) or a CONJUNCTION (radii independent,
  descent adds nothing)? **What got CHECKED (exact mpmath 40dps):** FF genus-2/`q=9`, `H^1` eigenvalues in 2
  conjugate-dual pairs. A balanced modulus redistribution (`|α_1|=r√q,|α_3|=√q/r`; `|α_2|=√q/r,|α_4|=r√q`)
  preserves the global determinant `∏α_i=q^g=81` AND both Poincaré pairings `{9,9}`, yet breaks the even split
  at 2 places (moduli `{4.475,2.011,2.011,4.475}` vs `√q=3`): (det PRESERVED) ∧ (pairing PRESERVED) ∧ (even
  split BROKEN) ⟹ the global even split is NOT forced by (determinant+pairing) — a CONJUNCTION, not a rigidity.
  The FE fixes the PRODUCT of moduli (`=q^g`, the global edge, FREE) but NOT the individual moduli. `ζ` MIRROR
  (`f=Δ`, `p=5,7`, `δ=0.3`): plant off-even at BOTH primes preserving each determinant `p^{k−1}`; the global
  determinant product is UNTOUCHED (`9.65e16` before=after), both off-even — the global FE `s↔k−1−s` couples NO
  two primes' moduli, primes modulus-INDEPENDENT. DH: no Euler product ⟹ empty domain at step 0 (no edge, no
  carrier), strictly before the rigidity question; ladder `DH<ζ<FF`. **Falsifier verdict:** EULER-BORNE YES
  (the product/edge assembles; DH empty domain), SEES-ZEROS YES (only through the positivity that fails under
  redistribution; the determinant/pairing data are BLIND to it), INDEPENDENT NO (the discriminator `P_∞⪰0` =
  Weil/Hodge = RH) → **CIRCULAR**, with NEW content a **NO-GO ON THE DESCENT**: the radius is not a descent
  constraint at all — no determinant/FE quantity is a function of the individual radii. **NEW content:** the
  descent assembles the global determinant (the PRODUCT of radii = the edge `Re s=1`, the `‖f‖²` pole),
  Euler-borne RH-free, but the radius RESIDUE (the global even split = the centre `Re s=½`) has NO cross-place
  rigidity — the FE/Euler data couple the PRODUCT of radii, never the individual radii. This is K2r-fix's "the
  radius must be Euler-assembled" made PRECISE and then BOUNDED: the assembly gives the product, never the
  split. The unique structure distinguishing the redistributed (off-even) from the genuine (even) config —
  both with identical determinant and pairings — is `P_∞⪰0`, the archimedean keystone, which is NOT a function
  of the determinant. **Successors added:** K7 promoted to SOLE LIVE KEYSTONE [the redistribution falsifier —
  compute `P_∞` on the redistributed global `H^1`, confirm it goes indefinite while the even one is definite,
  establishing `P_∞⪰0` is the ONLY discriminator; the keystone is now FORCE THE UNIFORMITY OF THE `C_W`
  RADIUS]; K3 sharpened (the forcing lemma's hypothesis "`C_W` has uniform radius" = "no redistribution",
  identical to K7); K6 re-scoped (a *degree* is a function of the determinant = the product, hence
  radius-silent like `κ` — K6 collapses into K7 unless the graded structure carries a positivity).

- **2026-06-06 — K2r-fix [KEYSTONE · coherence-checked · anchored vs 𝔽_q / Δ]: resolved the reality/radius
  fork with the ALGEBRA OF CONJUGATIONS — the real/condensed structure `κ` (M3b's `c_0`) IS available over `ℤ`
  FOR FREE (FORK 2 FALSE) and forces the PHASE-reality (the FE / conjugate-pairing `β=\barα`), but it is
  RADIUS-SILENT BY A THEOREM, and the radius `|α|=√d` (the even split = purity = RH) is `σ_d`'s SCALE `d`,
  ORTHOGONAL to every conjugation — `κ` is FREE but the WRONG HALF.** [KEYSTONE · coherence-checked · anchored
  vs 𝔽_q / Δ]. `research/construction/K2r-fix-reality-datum-kappa.md`,
  `scripts/numerics/witness/reality_datum_kappa.py` (+1 `falsify.py` row → 53, DISPERSING-on-the-reality-half).
  **What got CHECKED (exact mpmath 40dps; `f=Δ`; 5 Weil curves; DH type-level):** **[1]** every antilinear
  involution `c(z)=μ\bar z` is involutive IFF `|μ|=1`, and `Fix(c)` is a PHASE condition `θ=2φ`, NEVER a
  radius — verified all 3 radii `{0.5,3,100}` on the fixed ray are `c`-fixed (err `~0`), off-ray moved; so
  `κ` is RADIUS-SILENT by a THEOREM (sharpens M3b's `(−1)^w`-radius-silence). **[2]** `σ_d(z)=d/\bar z=(d/|z|²)z`
  EXACTLY (conj CANCELS, residual `~1e-35`): a pure RADIAL inversion about `√d`; its radius is the Euler-borne
  SCALE `d`, NOT a conjugation — reality (`κ`) and radius (scale `d`) ORTHOGONAL. **[3]** THE FORK: `[c_0,F]=0`
  (`c_0`=swap∘conj realizing the FE) `⟺ β=\barα` = the FE/phase-reality, holds at ANY radius — a PLANTED
  off-radius conjugate-paired pair (`|α'|=1065761≠√d=534146`) STILL satisfies `[c_0,F]=0`: `κ` BLIND to the
  radius defect. **[4]** FF anchor (5 curves): `[c_0,F]=0` is the FE (free), `|α|=√q` the SEPARATE Deligne-purity
  theorem; `κ` free + radius-silent, the radius is the theorem. **[5]** DH: `c_0` EXISTS (DH has a FE ⟹
  conjugate-pairing holds) ⟹ `κ` DH-SHARED + radius-silent; DH has no `d` ⟹ no radius to match (even-split
  VACUOUS); the radius is the ONLY DH-distinguisher and `κ` does not carry it. Carrier ladder `DH(c_0,no d) <
  ζ(c_0+d) < FF(c_0+d+purity)`. **Falsifier verdict (a coherence check on the reality half):** EULER-BORNE NO
  on the reality half (`κ=c_0` exists for DH) → DISPERSING; SEES-ZEROS YES (only the radius half, via `σ_d`'s
  scale; `κ` itself blind); INDEPENDENT NO (radius = even split = RH). Tabled **DISPERSING-on-the-reality-half**
  (`euler_borne=False`): the keystone is NOT the reality datum — `κ` is the WRONG HALF (phase, free,
  radius-silent). **NEW content:** a THEOREM — the archimedean reality datum is radius-silent BECAUSE
  conjugations (`|μ|=1`) carry only phase, never a radius — resolving the reality/radius fork as an
  ORTHOGONALITY: `κ` (the FE/phase) is free over `ℤ` (FORK 2 FALSE) and DH-shared; the radius (the even split =
  purity = RH) is the SCALE `d`, an Euler datum orthogonal to every conjugation, which must be Euler-ASSEMBLED
  (M4r), NOT supplied by a real structure. **Successors added:** M4r promoted to SOLE LIVE KEYSTONE (assemble the
  per-prime SCALE/radius `√d` against the radius-silent `(P_∞,D,c)`); K6 [the scale as a NON-METRIC DEGREE — a
  valuation / `ℚ_{>0}`-graded `𝔽₁` line whose size is `√d`, not a Gram form, may evade Sylvester]; K2 re-pointed
  (condensed object supplies `c_0` free + radius-silent; it must carry the SCALE/degree `√d`, not the reality).

- **2026-06-06 — K2r-split [KEYSTONE · coherence-checked · anchored vs 𝔽_q / Δ]: attacked the relocated
  residue with the charter §0 design law (the polarization must be a `*`-INVOLUTION / duality, NOT a metric)
  and found the §0 duality is the FREE half — the `*`-involution `σ_d(z)=d/\bar z` (the polarization/Rosati
  adjoint on the weight-2 determinant line) EXISTS FOR FREE from the Euler-borne determinant edge `d=p^{k−1}`,
  is `*`-clean (involutive + antilinear, NOT a metric), and its fixed locus IS the even split — BUT its
  existence does NOT FORCE the Frobenius/Satake pair onto `Fix(σ_d)`; "the pair lies on `Fix(σ_d)`" is the
  irreducible RH.** [KEYSTONE · coherence-checked · anchored vs 𝔽_q / Δ].
  `research/construction/K2r-split-even-split-involution.md`,
  `scripts/numerics/witness/cw_even_split_involution.py` (+1 `falsify.py` row → 52, CIRCULAR). **What got
  CHECKED (f=Δ, arithmetic Satake, exact mpmath 40dps, primes 2..19; 5 Weil curves; DH type-level):** **[1]**
  `σ_d(z)=d/\bar z` is a GENUINE `*`-involution — `σ_d∘σ_d=id` to `~1e-34`, ANTILINEAR (a `*`-structure, the
  thing a metric is NOT, §0), definable from the determinant `d=p^{k−1}` (K2r's Euler-borne edge) ALONE with
  NO radius input, `Fix(σ_d)={|z|=√d}`=the even-split radius → **the DUALITY is the FREE half**. **[2]**
  `Fix(σ_d)` on a det-`d` pair == the even split `|α|=|β|=√d`; the genuine Ramanujan pair LIES on `Fix(σ_d)`
  (True all primes = Deligne) but this is a SEPARATE condition `|α|=√d`, NOT forced by `σ_d`'s existence.
  **[3]** PLANT off-Ramanujan at `p=11` (`δ=0.3`): determinant `285311670611=p^{11}` PRESERVED → `σ_d`
  UNCHANGED (exists verbatim), but `|α′|=1065761≠|β′|=267707≠√d=534146` → pair NOT on `Fix(σ_d)`: the duality
  EXISTS but does NOT FORCE the pair onto its fixed locus. **[4]** FF ANCHOR: over `𝔽_q` the pair is on
  `Fix(σ_q)` UNCONDITIONALLY — but NOT because `σ_q` forces it: because the Frobenius is a `q`-WEIL NUMBER
  (`|α|=√q`), Deligne's purity = RH for the curve, a THEOREM EXTERNAL to `σ_q` (5 curves). **[5]** DH: no
  Euler product → no Satake → no determinant `d` → `σ_d` has EMPTY DOMAIN (it is BUILT from `d`): even the
  FREE half (the duality) does not exist for DH; carrier ladder DH<ζ<FF. **Falsifier verdict
  (anchor/coherence):** EULER-BORNE YES (`σ_d` built from `d`; DH no `d`→no `σ_d`), SEES-ZEROS YES (pair-on-
  `Fix` moves under the plant; `σ_d` itself blind), INDEPENDENT NO (pair-on-`Fix`=`|α|=√d`=Ramanujan/RH) →
  **CIRCULAR**, sharpened to "the DUALITY is free and `*`-clean; the Frobenius's FIXEDNESS under it is the
  irreducible RH". **NEW content:** the charter §0 design law shows its TEETH — a `*`-involution (duality,
  not metric) is exactly the right structure and is FREE from the Euler-borne determinant edge, but **a
  duality cannot force its own fixed points**; RH RELOCATES to its sharpest form: **"the Frobenius/Satake
  pair is a FIXED POINT of the polarization duality `σ_d`"**, over `𝔽_q` the `q`-Weil-number theorem
  (Frobenius commutes with geometric conjugation = the reality of the realization), over `ℤ` the open RH.
  **Successors added:** K2r-fix [the reality datum — is "Frobenius ∈ `Fix(σ_d)`" a `Gal`/descent condition
  supplied by a condensed/real structure (M3b's `κ`, the `c`-fixed locus) over `ℤ`, or only available after
  purity?]; K2 re-pointed (the condensed object must produce the FIXED-POINT/reality condition, not the free
  involution `σ_d` nor the free edge); K3 unchanged (forcing free given `C_W`; `C_W`'s radius = the
  Frobenius's `σ_d`-fixedness).

- **2026-06-06 — K2r [KEYSTONE · coherence-checked · anchored vs 𝔽_q / Δ]: executed the named residue —
  assemble `C_W`'s RADIUS over `ℤ` from the per-prime Satake products `αᵢ(p)αⱼ(p)` — and FACTORED the
  assembly into a FREE cross-place edge and a HARD per-prime even split (sharper than the agenda's
  "Euler-assemble the radius" framing): the weight-2 EDGE = the determinant `|α(p)β(p)|=p^{k−1}` assembles
  UNIFORMLY across all primes, Euler-borne + RH-FREE; the residue RELOCATES to the per-prime EVEN SPLIT
  `|α|=|β|=p^{(k−1)/2}` = the M2b purity `(·)^{1/2}` = Ramanujan/RH.** [KEYSTONE · coherence-checked ·
  anchored vs 𝔽_q / Δ]. `research/construction/K2r-cw-radius-assembly.md`,
  `scripts/numerics/witness/cw_radius_assembly.py` (+1 `falsify.py` row → 51, CIRCULAR). **What got CHECKED
  (multi-prime anchor `f=Δ`, Ramanujan τ, weight 12, `H^1` weight `k−1=11`, arithmetic Satake `α,β`=roots
  of `X²−τ(p)X+p^{k−1}`, exact mpmath 40dps, 16 primes 2..53):** **[1]** the weight-2 EDGE per prime = the
  DETERMINANT `|α(p)β(p)|=p^{k−1}` EXACTLY (all primes `<1e-15` rel) → the edge exponent `γ=k−1=11` is
  UNIFORM across all primes, read off the Satake matrix's DETERMINANT (no eigenvalue moduli) — Euler-borne,
  RH-INDEPENDENT; THE CROSS-PLACE EDGE ASSEMBLES FOR FREE. **[2]** the weight-1 CENTRE radius `C_W` needs =
  the EVEN SPLIT `|α(p)|=|β(p)|=p^{(k−1)/2}` (all primes `<1e-20` rel) = the purity square root of the
  determinant = Ramanujan/Deligne = the RH analogue for `f`. **[3]** PLANT off-Ramanujan at `p=11` (`δ=0.3`)
  with `α'β'=p^{k−1}` but `|α'|=p^{(k−1)/2+δ}`: determinant edge PRESERVED (`285311670611=p^11`, both sides),
  even split BROKEN (`|α'|=1096674 ≠ |β'|=260161 ≠ √=534146`) — the assembly's EDGE is INSENSITIVE to the
  plant; ONLY the even split sees it. **[4]** FF ANCHOR (single place): the assembly DEGENERATES (one base
  size `q`), det edge `=q` free, even split `|α|=√q` = Deligne purity (5 curves) — WHY the FF gets the
  radius for free: no cross-place assembly, the single place's determinant IS the edge. **[5]** DH: no Euler
  product → no Satake → EMPTY DOMAIN, the edge cannot even be formed; carrier ladder `DH<ζ<FF`. **Falsifier
  verdict (anchor/assembly):** EULER-ASSEMBLED SPLIT (the determinant edge IS assembled uniformly + RH-FREE;
  the even split needs Satake but is NOT supplied by the assembly — it is the purity root), SEES-ZEROS YES
  (only through the even split — the determinant edge is blind to the off-Ramanujan plant), INDEPENDENT NO
  (the even split = Ramanujan/RH = Deligne purity over FF) → **CIRCULAR** over the anchor in the precise
  sense: the even split of the assembled edge = the RH radius. **NEW content:** the cross-place coupling (the
  determinant edge `p^{k−1}`) is the FREE half of the radius assembly (uniform across all primes,
  RH-independent); the irreducible residue is the per-prime EVEN-SPLITTING of the assembled weight-2 edge
  into two equal weight-1 factors — the keystone residue sharpened from "the radius" to "the even split of
  the assembled determinant". **Successors added:** K2r-split [the relocated residue — is the even split of
  the determinant line `p^{k−1}` forced by a geometric/condensed `*`-involution whose fixed locus is
  `|α|=|β|`, or the irreducible RH?]; K2 re-pointed (the condensed object must produce the EVEN SPLIT of the
  assembled determinant edge, not the edge — the edge is free); K3 unchanged (the Hodge–Riemann forcing is
  free given `C_W`; `C_W`'s radius = the per-prime even split).

- **2026-06-06 — K1 [KEYSTONE · coherence-checked · anchored vs 𝔽_q]: executed the keystone — is `P_∞⪰0`
  (`c=D`) FORCED by a Hodge–Riemann/Kähler structure? — and found the forcing FACTORS: `c=D` is NOT
  Kähler-forced "for free"; the cup product `E` ALONE is INDEFINITE, the Hodge–Riemann implication is
  formal, and the Weil operator `C_W` that makes `E` definite is over `𝔽_q` LITERALLY the RH radius
  `|α|=√q`. The keystone LOCATES the single irreducible residue (`C_W`'s radius), it does not dissolve
  RH.** [KEYSTONE · coherence-checked · anchored vs 𝔽_q]. `research/construction/K1-kahler-forcing.md`,
  `scripts/numerics/witness/kahler_forcing.py` (+1 `falsify.py` row → 50, CIRCULAR). **What got CHECKED
  (FF/polarized-HS anchor, all EXACT):** **STEP A** the cup product `E` (symplectic Weil pairing, the
  "ample"/polarization datum) gives an INDEFINITE Rosati form `Tr(z z^†)` — sig `(2,0,2)` `g=1`, `(8,0,8)`
  `g=2`, `(18,0,18)` `g=3` — so `E` by ITSELF does NOT force Hodge–Riemann positivity (the naive "ample
  forces `c=D` for free" is FALSE). **STEP B** with the WEIL OPERATOR `C_W=i^{p−q}` inserted,
  `P_∞(x,y)=E(C_W x,x̄)` IS positive-definite on `H^{1,0}` (min eig `+2.03,+4.72,+6.17,…>0`, all g/seeds)
  = Riemann's 2nd relation; the forcing datum is the PAIR `(E,C_W)` = the POLARIZED HS, `C_W` the Kähler
  class that makes `E` definite. **STEP C** over `𝔽_q` the weight-1 `C_W` exists ⟺ Frobenius is a weight-1
  Weil number `α=√q·e^{iθ}` ⟺ a UNIFORM radius `√q` ⟺ `|α|=√q` = RH; an off-circle plant `{r√q,√q/r}` has
  TWO moduli ⟹ no uniform radius ⟹ no `C_W` ⟹ no `c=D` (5 curves `q=2,5,7,11,13`). **So over `𝔽_q` the
  Kähler datum `C_W` and RH (`|α|=√q`) are LITERALLY the same datum.** **THE KEYSTONE FACTORIZATION (K5
  terminus):** `(E)` GEOMETRIC/zero-free/DH-shared/INDEFINITE-alone [free]; `(C_W)` the `(p,q)`/RADIUS
  datum, `=|α|=√q`=RH over `𝔽_q` [=RH]; Hodge–Riemann `(E,C_W)`-polarized ⟹ `P_∞⪰0`=`c=D` [formal]. This
  is M3b's "radius-silent `(−1)^w`" lesson AS a Hodge forcing: the archimedean Kähler class carries `C_W`'s
  PHASE/reality (the sign `(−1)^w`) but NOT its RADIUS — the radius is the whole problem. **Falsifier
  verdict (anchor/forcing, the keystone FACTORS the axes):** EULER-ASSEMBLED SPLIT (`E` Euler-silent
  DH-shared; `C_W`'s RADIUS Euler-borne=Frobenius weight; the implication formal — K1 LOCATES the Euler
  content in `C_W`'s radius), SEES-ZEROS YES (only through `C_W`), INDEPENDENT NO (the implication is
  independent/Hodge–Riemann, but the HYPOTHESIS "`C_W`=weight-1 Weil op" over `𝔽_q` IS `|α|=√q`=RH) →
  **CIRCULAR over `𝔽_q`** in the precise sense that the Kähler datum `C_W` = the RH radius. **NEW content:**
  the keystone is NOT attackable "for free" — the forcing factors as (free `E`) + (formal Hodge–Riemann) +
  (the Weil operator `C_W`, whose RADIUS over `𝔽_q` IS the RH critical line); an archimedean Kähler class on
  `S²/ℤ` must be a CANONICAL Weil operator `C_W` whose radius is Euler-assembled from the Satake products,
  NOT a chosen Green form (BGS §6.3 evaded because `P_∞` is the categorical pairing, not a metric).
  **Successors added:** K2r [the named residue — construct `C_W`'s RADIUS over `ℤ` (`Re s=½`) from the Euler
  assembly of `αᵢ(p)αⱼ(p)`, the one piece the forcing does not supply]; K2 re-pointed (the condensed object
  must PRODUCE `C_W`, not a Green form); K3 sharpened (the forcing lemma is FREE given `C_W`; the hardness is
  entirely `C_W`'s radius).

- **2026-06-06 — M3b [COHERENCE · anchored vs polarized-HS]: proved the archimedean MIRROR of M2c′(A)/(B)
  — `(P_∞, D, c)` is a COHERENT triple at `∞`, Frobenius-free: `P_∞` is FUNCTORIAL and the Weil operator
  `C_W` commutes with the duality `D` up to the Tate twist `ℚ(−w)`, with multiplier `(−1)^w` (a SIGN, the
  weight PARITY) replacing the Frobenius weight `q`; RH read archimedeanly = the degeneration `c=D` = the
  Hodge-type alignment `P_∞>0 ⟺ Y>0`.** [COHERENCE · anchored vs polarized-HS].
  `research/construction/M3b-archimedean-coherence.md`,
  `scripts/numerics/witness/archimedean_coherence.py` (+1 `falsify.py` row → 49). **The translation M2c′→M3b:**
  Frobenius `F` → Weil operator `C_W=i^{p−q}`; cup product `E` → duality `S` (`S^T=−S`); Frobenius weight
  `q` → `(−1)^w` (weight parity, a SIGN; `w=1`: `C_W²=−1` = the complex structure `J`); `c` borrowed from
  Frobenius → `c=κ` intrinsic; morphism square `EF=qF^∨E` → `D(C_W)=C_W^{−1}`; `c=D⟺|α|=√q⟺RH` → `c=D⟺Y>0`.
  **What got CHECKED (weight-1 polarized-HS anchor, `g=1,2,3`, multiple seeds, all EXACT):** **(A) `P_∞`
  FUNCTORIAL** — a morphism `f` of HS (symplectic base change `M`, `M^T S M=S` to `3e-16`) COMMUTES with
  the Weil operator (`f C_W=C_W' f` to `2.7e-15` — `C_W` is NATURAL, depends only on `(p,q)`) and INTERTWINES
  the polarization (`f^* P_∞'=P_∞` to `3.6e-15`) = the mirror of M2c′(A) "`φ_FE` a morphism not a matrix".
  **(B) `C_W` COMMUTES with `D` up to `ℚ(−w)`** — B1 `C_W` is an ISOMETRY of `S` (`C_W^T S C_W=S` to `4.6e-16`,
  the archimedean `q`-similitude, multiplier normalized to `1` since `i^{p−q}i^{q−p}=1`); B2 the CENTRAL TWIST
  `C_W²=(−1)^w` on `V` (`=−1` at weight 1, to `5e-15`) = the archimedean analogue of the Frobenius weight `q`,
  a SIGN (the weight parity) NOT a base-field size; B3 the `C_W`–`D` 2-cell `D(C_W)=C_W^{−1}` to `2.7e-15`
  (the Weil op intertwines `D` with its `(−1)^w`-twisted self) = the mirror of M2c′(A1)'s square `EF=qF^∨E`.
  **(C) the triple `(P_∞,D,c)` COHERENT** — C1 `c=κ`,`D` COMMUTING INVOLUTIONS (`DoD=coc=Dc−cD=0.0e+00`
  exact, a Klein `ℤ/2×ℤ/2`, RH-independent); C2 `c` exchanges the Hodge lines (to `1.8e-15`); C3 THE
  ARCHIMEDEAN SEPARATION — RH = `c=D` = the HODGE-TYPE ALIGNMENT: `P_∞>0` on `H^{1,0}` (`c,D` align on the
  primitive part) ⟺ the polarized type `Y>0`, sweeping `Y>0`(`+2.03`) through `Y=0`(degenerate) to `Y<0`
  (`−2.03`) a MONOTONE flip all `g` — the `(p,q)` analogue of "a zero ON vs OFF the critical line", supplied
  by `C_W` NOT a Frobenius weight. **Falsifier verdict (a COHERENCE check on the archimedean half, the place
  at `∞`):** EULER-ASSEMBLED NO **BY DESIGN** — the archimedean triple is the `Γ`-factor, DH-SHARED; the
  multiplier `(−1)^w` is a SIGN (weight parity), NOT an Euler datum, so it does not distinguish `ζ` from DH;
  M3b's JOB is COHERENCE of the reality/phase half, the cross-place coupling is M4's descent. Tabled
  **DISPERSING-by-design** (`euler_borne=False`), the archimedean HALF, NOT a standalone RH-form. SEES-ZEROS
  YES (the Hodge-type alignment holds ⟺ `Y>0`). INDEPENDENT NO on the anchor (= the Hodge–Riemann relation).
  **NEW content:** the archimedean coherence of `(P_∞,D,c)` is PROVEN Frobenius-free — `C_W` commutes with `D`
  up to `ℚ(−w)` (multiplier `(−1)^w`, a SIGN replacing the Frobenius weight `q`), `P_∞` FUNCTORIAL, RH = the
  archimedean `c=D` = the Hodge-type alignment; the mirror of M2c′(B) is COMPLETE. **The structural lesson
  (sharpens the next hinge):** the FF multiplier `q` *carries the radius* `√q` (Euler-borne), but its
  archimedean mirror `(−1)^w` is a SIGN carrying *only reality*, radius-SILENT — so `Re s=½` CANNOT be read
  off `∞`; it must be **Euler-assembled in the descent**. **Successors added:** M4r [DESCENT — specify the
  radius-assembly: per-prime Satake products `αᵢ(p)αⱼ(p)` assemble the global centre against the radius-silent
  `(P_∞,D,c)` at `∞`, = C3b cross-place]; M3c re-pointed (`C_W` and the `(−1)^w` twist as the condensed
  structure maps, the radius-free reality carrier).

- **2026-06-06 — M3 [INVENT · anchored vs polarized-HS]: INVENTED the archimedean Hodge polarization
  `P_∞(x,y)=S(C_W x, κ y)` — the `(p,q)`/reality datum at `∞`, FROBENIUS-FREE: the `(p,q)` grading carried
  by the WEIL OPERATOR `C_W=i^{p−q}` (the reality the FF borrowed from Frobenius, now supplied by `(p,q)`,
  no `q`) and the conjugation by the INTRINSIC real structure `κ`, with `P_∞` the CANONICAL pairing of the
  cup-product duality `S` (`H=C_W^† S` exactly, NOT a metric — §0-clean), positivity reading the `(p,q)`
  type, Frobenius-limit = the FF `c` with `q` stripped.** [INVENT · anchored vs polarized-HS].
  `research/construction/M3-archimedean-hodge-polarization.md`,
  `scripts/numerics/witness/archimedean_hodge_polarization.py` (+1 `falsify.py` row → 48). **The gap M3
  fills:** M2/M2c′/M4C built `(𝒞,ω_∞,D,P)` only on the FF anchor, where `c` and the Weil op were BORROWED
  from Frobenius (`c:α↦ᾱ` = `D:α↦q/α` on `|α|=√q`); at `∞` THERE IS NO FROBENIUS, so the `(p,q)`/reality
  datum must be invented intrinsically, with the polarization a duality pairing not a metric (§0). **What
  got DEFINED:** the archimedean datum `(V,F^•,D,W,c,P_∞)` — real structure `V=V_ℝ⊗ℂ` (`κ`), Hodge
  filtration `F^•`, structural duality `D:V→V^∨(−w)` (= `S=⟨·,D·⟩`), Weil operator `C_W=i^{p−q}`,
  conjugation `c=κ`, polarization `P_∞(x,y)=S(C_W x, κ y)=ev∘(1⊗D)∘(C_W⊗κ)` = the Hodge–Riemann form.
  **What got BUILT (FF/Hodge anchor, weight-1 polarized HS = `H^1` of a genus-`g` curve, period matrix
  `[I;Z]`, `Z=X+iY`, `Y>0`; `g=1,2,3`, multiple seeds, EXACT):** **(1) ANCHOR** `P_∞` POSITIVE-DEFINITE on
  `H^{1,0}` (min eig `+2.03,+3.35,+4.72,…>0`) = the classical weight-1 Hodge–Riemann/Riemann relation,
  reproduced; **(2) DESIGN-LAW (§0)** `H=C_W^† S` EXACTLY (factor resid `0.0e+00`) — the CANONICAL pairing
  of the duality, NO chosen metric; `S` is the ANTISYMMETRIC cup product (`‖S+Sᵀ‖=0.0e+00`, `Sᵀ=−S`),
  exactly what a metric is NOT; **(3) §0 NO-GO ESCAPE** `P_∞`'s positivity reads the HODGE TYPE — with `S`
  FIXED, `Y>0` (polarized, `+2.03`) → `Y=0` (filtration degenerates) → `Y<0` (anti-polarized, `−2.03`),
  MONOTONE flip, all `g` — the archimedean analogue of 'moved by the zero location', a flip NO `*`-
  congruence `x^*A x` of a fixed background can produce (Sylvester-immune by CONSTRUCTION: no fixed `A` +
  variable plant; the `(p,q)` grading IS the variable); **(4) FROBENIUS LIMIT** `κ` swaps the Hodge lines
  `H^{1,0}↔H^{0,1}` (`‖P_{10}∘κ(H^{1,0})‖=0.0e+00/1.8e-15`) = the FF's `c` with the weight `q` STRIPPED —
  the deformation `ℤ` needs (`ℤ` has no Frobenius weight; `Re s=½` must come from the archimedean `(p,q)`
  structure, the open C3b). **Falsifier verdict (an INVENTED+ANCHORED archimedean datum, NOT a standalone
  `ℤ`-candidate):** EULER-ASSEMBLED NO **BY DESIGN** — the archimedean datum is the `Γ`-factor at `∞`,
  DH-SHARED; M3's JOB is reality/phase, NOT Euler-discrimination; the cross-place coupling is M4's descent.
  Tabled **DISPERSING-by-design** (`euler_borne=False`) with the explicit note that it is the archimedean
  HALF and must NOT be scored as a finished RH-form. SEES-ZEROS YES (the hodge-type flip), INDEPENDENT NO
  on the anchor (Hodge–Riemann = Riemann relations = the solved case). **NEW content:** the `(p,q)`/reality
  datum at `∞` is INVENTED Frobenius-free (Weil operator `C_W` + real conjugation `κ`), with `P_∞` the
  canonical duality pairing (§0-clean, `H=C_W^† S` exact, NOT a metric) whose positivity reads the `(p,q)`
  type and whose Frobenius limit recovers the FF `c` — the well-typed archimedean input M4's descent glues
  to the prime Euler factors (the piece M2c′ named "the target M3's archimedean datum deforms into").
  **Successors added:** M3b [COHERENCE — `P_∞` functorial + `C_W` commutes with `D` up to `ℚ(−w)`, the
  archimedean mirror of M2c′(B), RH = `c=D` read archimedeanly]; M3c [condensed upgrade — `(V,F^•,κ)` as a
  Clausen–Scholze condensed/analytic object, the "condensed-archimedean structure Arakelov lacks"]; M4
  re-tagged (its archimedean input `P_∞` now built, ready to glue to the prime Euler factors).

- **2026-06-06 — M2c′ [COHERENCE · anchored vs 𝔽_q]: completed the M2c/M4D REMAINDER — `φ_{FE}` is a
  genuine MORPHISM of the rigid tensor category (not a matrix), and `c` is COMPATIBLE with `D` up to the
  weight-2 Tate twist `ℚ(−1)`, so `(𝒞,ω_∞,D,P)` is now a coherent 2-categorical object; RH = the Klein-4
  degeneration `c=D`.** [COHERENCE · anchored vs 𝔽_q].
  `research/construction/M2c-prime-fe-morphism-rosati-compat.md`,
  `scripts/numerics/witness/fe_morphism_rosati_compat.py` (+1 `falsify.py` row → 47). **What got CHECKED
  (FF anchor, `g=1` rank 4 `q=2,5,7,11,13` AND `g=2` rank 16 `q=2`, all EXACT):** M4C had already done
  `D∘D=id` on `gr^W_2`, `P_NS=ev∘(1⊗φ_{FE})=Tr(z w^†)` (NOT a metric), and the `g=2` non-semidefinite
  anchor (involutivity + trace-kernel DONE). M2c′ supplies the two remaining coherence facts.
  **(A) `φ_{FE}` is a MORPHISM:** (A1) `Φ`-EQUIVARIANT up to `ℚ(−1)` — the naturality square `E F = q F^∨ E`
  (`⟺ FᵀEF=qE`, the Weil `q`-similitude) commutes to `≤1e-15` all curves, so `φ_{FE}` intertwines
  Frobenius with its Tate-twisted dual (a morphism of Frobenius-modules, not an arbitrary matrix); (A2) the
  induced `D=(·)^†` is a TENSOR duality — an anti-automorphism of `End(H^1)` (`(zw)^†=w^†z^†` to `0`) fixing
  the unit (`D(Id)=Id` to `0`). **(B) `c` COMPATIBLE with `D` up to `ℚ(−1)`:** (B1) `c,D` are COMMUTING
  INVOLUTIONS — `c∘c=id`, `D∘D=id`, `D∘c=c∘D` all `0.00e+00` ON AND OFF circle (a Klein `ℤ/2×ℤ/2`,
  RH-INDEPENDENT); (B2) `c` exchanges the Hodge lines `H^{1,0}↔H^{0,1}`; (B3) the Tate twist
  `q=Tr(F F^†)/Tr(Id Id^†)=2gq/2g` is the `c·D` similitude multiplier (exact all 6); (B4) **THE SEPARATION**
  `c=D` on `H^1` ⟺ RH — `|c(F)−D(F)|=0` on-circle (`c=D`, RH) but `>1` off-circle (`c≠D`, RH fails), so
  **RH = the DEGENERATION of the Klein four-group to a `ℤ/2`** (`c,D` fuse) = the `c`-EVEN reading of C2
  (Hodge lines align with conjugate lines), NOT a `c`-odd functional (the `c`-odd datum vanishes on
  FE-symmetric spectra, DONE #31/#25/#30). **Falsifier verdict (anchor/coherence, not a `ℤ`-candidate):**
  euler-assembled Y (morphism square + twist read the Frobenius `q`-similitude/Satake; DH no Frobenius
  weight ⟹ no morphism square ⟹ no Tate twist ⟹ no coherent object), sees-zeros Y (`c=D` ⟺ `|α|=√q` ⟺ RH),
  independent N (`c=D` = Weil/Riemann positivity) → **CIRCULAR** over `ℤ`, expected. **NEW content:**
  `φ_{FE}` is a genuine rigid-tensor MORPHISM (`Φ`-equivariant up to `ℚ(−1)` + `D` a tensor
  anti-automorphism) and `c` is a COMMUTING INVOLUTION compatible with `D` up to the Tate twist, with
  RH = the Klein-4 degeneration `c=D` — `(𝒞,ω_∞,D,P)` is now a COHERENT 2-categorical object (the M2c/M4D
  remainder), the well-typed target M3's archimedean datum deforms into. **Successors added:** M3 re-tagged
  (now has a fully-coherent weight-2 target); M4 unchanged (Euler-assemble `P_NS`/form `(*)` on the GLOBAL
  weight-2 lattice — the single hinge C3b).

- **2026-06-06 — M4C [COHERENCE · anchored vs 𝔽_q]: lifted M2's C4 fact (polarization = canonical
  duality pairing, NOT a metric) from the weight-1 `H^1` to the WEIGHT-2 NS lattice `gr^W_2=End(H^1)`,
  and in passing settled the M2c/M4D `g=2` concern — `D∘D=id` ON the lattice and `P_NS=ev∘(1⊗φ_{FE})=
  Tr(z w^†)` to `0.00e+00`, the off-circle inertia flip IS the weight-2 Hodge index, genuinely
  non-semidefinite at rank 16.** [COHERENCE · anchored vs 𝔽_q].
  `research/construction/M4C-ns-hodge-index-duality.md`,
  `scripts/numerics/witness/ns_hodge_index_duality.py` (+1 `falsify.py` row → 46). **What got CHECKED (FF
  anchor, `g=1` NS rank 4 `q=2,5,7,11,13` AND `g=2` NS rank 16 `q=2`, all EXACT):** the duality
  `D:End(H^1)→End(H^1)`, `z↦z^†=E^{-1}z^TE` (M1's `c`/Rosati acting by conjugation of endomorphisms).
  **THREE EXACT FACTS:** (i) **`D∘D=id` ON the weight-2 lattice** — `max‖D(D(z))−z‖=0.00e+00` over a
  spanning basis, `g=1` and `g=2`; `gr^W_2` is RIGID/dualizable, M1's involutive-duality axiom holds on
  the lattice, not only on `H^1` (the M2c involutivity check, on weight 2). (ii) **`P_NS=ev∘(1⊗φ_{FE})=
  Tr(z·D(w))` EQUALS the M4B Rosati Gram `Tr(z w^†)` to `max|P_dual−P_gram|=0.00e+00`** over a spanning
  basis — the weight-2 polarization is FORCED by the cup product, NOT a chosen metric (M2's C4=0 lifted
  weight-1→weight-2; evades the §0 Sylvester no-go by construction). (iii) **the off-circle inertia flip
  IS the weight-2 Hodge index of `P_NS`**: `−Tr(F₀F₀^†)` neg on-circle (`g=1`: `−3.5,−8,−13.5,−17.5,
  −13.5`; `g=2`: `−7.75`) GAINS a `+` off-circle plant `{r√q,√q/r}` (`g=1` `(0,1,1)→(1,0,1)`; `g=2`
  `−7.75→−1.66`), flip `=Σ|αᵢ|²−2gq`, all six `FLIP=True`. **LOAD-BEARING FIX (settles M2c/M4D):** the
  first build's companion Frobenius gave `F^TEF=qE` residual `4.0` at `g=2` (not a `q`-similitude) → a
  FALSE artifact; building `F,E` TOGETHER in the Rosati-paired basis (`(α,q/α)→diag` blocks, similitude
  by construction, resid `2e-15`) makes the `g=2` rank-16 case genuinely non-semidefinite and all three
  facts persist (`Tr(F F^†)=8=2gq`, on-circle H-idx `−7.75<0`, flip True) — **so the `g=1` `(0,1,1)`
  semidefiniteness was a rank artifact, NOT structure**, exactly the M2c/M4D question, answered.
  **Falsifier verdict (anchor/coherence, not a `ℤ`-candidate):** euler-assembled Y (`P_NS` reads
  `Tr(z w^†)`, `Tr(F F^†)=Σ|αᵢ|²=2gq` Satake; DH no `f×f` ⟹ no `End`-Frobenius ⟹ no weight-2 lattice ⟹
  no `P_NS`), sees-zeros Y (Hodge index flips off-circle), independent N (=Weil Hodge-index theorem) →
  **CIRCULAR** over `ℤ`, expected. **NEW content:** `D∘D=id` ON `gr^W_2` (rigid) and `P_NS=ev∘(1⊗φ_{FE})=
  Tr(z w^†)` to `0` — M1's C4 "duality pairing, NOT a metric" now established on the weight-2 carrier
  M4's descent must build; the `g=2` rank-16 anchor confirms genuine non-semidefiniteness. **Successors
  added:** M2c′ (the REMAINDER of M2c/M4D — prove `φ_{FE}` is a morphism and `c` compatible with `D` up
  to the Tate twist; involutivity + `g=2` already done here); M4 re-typed (the descent's target is now
  fully pinned — Euler-assemble `P_NS`/the form `(*)` on the GLOBAL weight-2 lattice from `αᵢ(p)αⱼ(p)`).

- **2026-06-06 — M4B [BUILD/REPRESENT · anchored vs 𝔽_q]: specified the SELF-INTERSECTION of the
  arithmetic DIAGONAL of `S²/ℤ` on M4A's weight-2 NS lattice as a REPRESENTABILITY functor `rep_NS`,
  with the explicit intersection form `(*)` and the diagonal proven INDECOMPOSABLE — avoiding the
  closed naive-product trap.** [BUILD/REPRESENT · anchored vs 𝔽_q].
  `research/construction/M4B-ns-diagonal-representability.md`,
  `scripts/numerics/witness/ns_diagonal_representability.py` (+1 `falsify.py` row → 45). **What got
  BUILT (FF anchor, 5 Weil curves `g=1` `q=2,5,7,11,13`, all EXACT):** the functor `rep_NS : Corr →
  (ℤ-lattice, form (*))`, `Z↦(d₁=Z·(pt×C), z=action on H^1, d₂=Z·(C×pt))`, with
  `NS(C×C)⊗ℚ=⟨C×pt⟩⊕⟨pt×C⟩⊕End(H^1)` and pairing `a·b = d₁e₂+d₂e₁−Tr(z∘w)` `(*)`, diagonal `Δ=(1,Id,1)`.
  **THREE EXACT ANCHOR FACTS:** (1) `Δ·Γ_{Fⁿ}=1·1+1·qⁿ−Tr(Fⁿ)=qⁿ+1−Σαᵢⁿ=#C(𝔽_{qⁿ})` — **the Lefschetz
  trace IS the NS self-intersection** (verified `n=1,2,3` all curves `<1e-12`, e.g. `q=5`: `4,32,148`);
  (2) `Δ` is **INDECOMPOSABLE** — its `End(H^1)`-component is `Id≠0` (norm `√(2g)=1.414`) while every
  product/fiber class acts as `0` on `H^1` (`‖End(fiber)‖=0`), so `Δ∉⟨C×pt,pt×C⟩` — a genuine
  primitive/transcendental component, **AVOIDING the `square_representability` factorization trap (this
  is NOT a tensor form)**, `Δ·Δ=2−2g=χ(C)`; (3) the Hodge index on the primitive `End`-part via the
  **Rosati polarization** `Tr(z w^†)` (`w^†=E^{-1}w^T E`, `F^T E F=qE` resid `0`): `Tr(F F^†)=Σ|αᵢ|²=2gq`
  on-circle (`4,10,14,22,26`), primitive `−Tr(F₀F₀^†)` NEG on-circle (`−3.5,−8,−13.5,−17.5,−13.5`) FLIPS
  POS off-circle plant `{r√q,√q/r}` (`+0.69,+1.74,+2.43,+3.82,+4.51`) — the `(0,1,1)→(1,0,1)` inertia
  flip of M2/`euler_movable_inertia.py` now **READ ON the weight-2 NS lattice**, neg-def ⟺ `|αᵢ|=√q` ⟺
  RH. **THE ℤ-QUESTION NOW SHARP:** what represents `rep_NS` for `ζ` — an object with an indecomposable
  diagonal (`End`-component ≠ product class), a Frobenius/Hecke graph with `Δ·Γₙ=` the explicit-formula
  trace, and the form `(*)` on `End` **Euler-assembled** from `αᵢ(p)αⱼ(p)` across ALL primes (M2d proved
  no single prime supplies it). **Falsifier verdict (anchor, not a `ℤ`-candidate):** euler-assembled Y
  (`Tr(Fⁿ)=Σαⁿ` Satake; DH no `f×f` ⟹ no `End`-Frobenius ⟹ `S²/DH` diagonal has no indecomposable
  component to self-intersect), sees-zeros Y (Hodge index flips off-circle), independent N (= the Weil
  Hodge-index theorem) → **CIRCULAR** over `ℤ`, expected. **NEW content:** the self-intersection of the
  diagonal is the FUNCTOR `rep_NS` with explicit form `(*)`; the diagonal is INDECOMPOSABLE (avoids the
  closed naive-product trap); `Δ·Γ_{Fⁿ}=#C` realizes the Lefschetz trace as the NS self-intersection.
  **Successors added:** M4C re-pointed (the Hodge index as M1's C4 categorical pairing **on this lattice
  with `(*)`+Rosati in hand**), M4D [BUILD the `g=2` rank-16 NS anchor — confirm the three facts persist
  at genuinely non-semidefinite rank, the M2c trace-kernel check].

- **2026-06-06 — M4A [DEFINE/BUILD · anchored vs 𝔽_q]: BUILT the weight-graded carrier the descent must
  supply and CORRECTED M2d's naming — the carrier is `gr^W_2` (the weight-2 Néron–Severi lattice
  `H^1⊗H^1` of the self-product surface, eigs `αᵢαⱼ`, `|αᵢαⱼ|=q`), NOT the `gr^W_1` M2d named (a
  redundant double of the curve's `H^1`). The M2b/M2d purity square root is correctly typed
  weight-2 → weight-1: Petersson edge `|αᵢαⱼ|=q` (`Re s=1` of `f×f̄`) → line `|αᵢ|=√q` (`Re s=½`).**
  [DEFINE/BUILD · anchored vs 𝔽_q]. `research/construction/M4A-weight-carrier.md`,
  `scripts/numerics/witness/weight_carrier.py` (+1 `falsify.py` row → 44). **What got BUILT (FF anchor,
  6 Weil curves `g=1` `q=2,5,7,11,13` and `g=2` `q=2`, all PASS exact to `<1e-14`):** via Künneth
  `H^n(C×C)=⊕_{i+j=n}H^i⊗H^j` + Deligne purity (`weight(H^i⊗H^j)=i+j`), the self-product surface `S=C×C`
  supplies TWO graded carriers: (i) `gr^W_1 H^•(C×C)=H^0⊗H^1⊕H^1⊗H^0`, rank `4g`, eigs `{1·αᵢ}` = **two
  copies of the curve's `H^1`** (NO new content), and (ii) the WEIGHT-2 middle `H^1(C)⊗H^1(C)⊂H^2(C×C)`,
  rank `4g²`, eigs `{αᵢαⱼ}`, `|αᵢαⱼ|=q` — the **NS lattice** where the diagonal `Δ` and graph `Γ_F`
  live, `Δ·Γ_{Fⁿ}=#C(𝔽_{qⁿ})`, and Weil's Hodge-index (= RH) operates. **THE DECISIVE M4A FINDING (the
  loop correcting the agenda):** M2d asked for `gr^W_1`, but the self-product surface delivers its RH
  content at WEIGHT 2 (`gr^W_2`), whose eigenvalues are PRODUCTS `αᵢαⱼ`, NOT the single zeros `αᵢ`. The
  "weight-1 carrier" is the SHADOW (diagonal pullback `C↪C×C`) of the weight-2 lattice. This explains
  WHY M2d found no per-prime weight-1 carrier: the load-bearing carrier is the GLOBAL weight-2 lattice,
  Euler-assembled from products `αᵢ(p)αⱼ(p)` across ALL primes, never one prime. **THE PURITY SQUARE ROOT
  CORRECTLY TYPED weight-2 → weight-1:** the surface's edge is weight 2 (`|αᵢαⱼ|=q` = the Petersson pole
  of `L(s,f×f̄)=ζ·L(s,sym²f)` at `s=1`, `Res=‖f‖²>0`, `F-sym2-os-bridge.md`); `(·)^{1/2}` descends it to
  the curve's weight-1 centre `|αᵢ|=√q` (`Re s=½`), verified `√q=|αᵢ|` all 6 curves. M2d's per-prime
  search looked one weight too low. **Falsifier verdict (anchor, not a `ℤ`-candidate):** euler-assembled
  Y (`αᵢαⱼ` products of Satake `αᵢ`; DH no `sym²`/`f×f̄` ⟹ no weight-2 lattice ⟹ `S²/DH` not a carrier),
  sees-zeros Y (purity `|αᵢαⱼ|=q ⟺ |αᵢ|=√q ⟺ RH`; NS Hodge index flips when a zero leaves the line),
  independent N (FF Hodge index=Deligne=Weil) → CIRCULAR over `ℤ`, expected. NEW content: the carrier
  WEIGHT is 2 not 1; the purity sqrt is weight-2 → weight-1; the carrier is the global self-product NS
  lattice. **Successors added:** M4B [BUILD/REPRESENT the weight-2 NS lattice over `ℤ` — what represents
  the self-intersection of the arithmetic diagonal of `S²/ℤ`; beware `square_representability.py` closed
  the NAIVE product, the diagonal must be INDECOMPOSABLE], M4C [the Hodge index on `gr^W_2`-primitives as
  M1's C4 categorical duality pairing, on the weight-2 lattice]; M4 re-targeted to the weight-2 piece.

- **2026-06-06 — M2d [DEFINE · coherence-checked]: DECIDED the typing question M2b left open — the purity
  functor `rad=(·)^{1/2}∘(edge) : LocFac→𝔾_m` is NOT well-typed PER-PRIME for `ζ`, because the `(·)^{1/2}`
  step needs a weight-1 carrier `gr^W_1` that no single prime supplies; purity is INTRINSICALLY GLOBAL for
  `ζ`, a condition on the weight filtration of the GLUED object. Re-routes M4 → M4A (build the carrier
  first).** [DEF · coherence-checked vs 𝔽_q]. `research/construction/M2d-purity-carrier.md`,
  `scripts/numerics/witness/purity_carrier.py` (+1 `falsify.py` row). **What got DEFINED:** the INPUT SLOT
  of the purity functor per place = the weight-1 graded piece `gr^W_1`, whose rank = DEGREE of the local
  zeta-factor numerator `P` (in `L=P/Q`, `P` carries the weight-1 `αᵢ`); the `(·)^{1/2}` purity step has an
  input at a place iff `deg P>0`. **THE DECISIVE EXACT FACT (computed, integer degrees):** per-prime the
  carrier is EMPTY for BOTH FF local factors `L_x=(1−T^d)^{-1}` (numerator deg 0) AND `ζ`'s primes
  `L_p=(1−p^{-s})^{-1}` (numerator deg 0) — a local factor is a weight-0 "point" in BOTH; **the difference is
  NOT at the prime** (`ζ`'s prime factor is EXACTLY an FF degree-1 point `(1−T)^{-1}`). The FF ASSEMBLES a
  GLOBAL rank-`2g` `H^1(C)` from its local factors via the curve (Lefschetz `N_n=q^n+1−Σαᵢⁿ`, `g=1,2,3` →
  deg 2,4,6); `ζ`'s primes assemble NO weight-1 cohomology (`Spec ℤ` 0-diml arithmetically), and `ζ`'s "`H^1`"
  (the nontrivial zeros) is NOT realized as the weight-1 cohomology of any geometric carrier — that missing
  carrier IS the surface `S²/ℤ` (`F-sym2-os-bridge.md`). **TYPING VERDICT:** `rad_edge` (the abscissa `Re s=1`)
  IS well-typed for `ζ` (local, per M2b); `rad=(·)^{1/2}∘(edge)` is NOT well-typed PER-PRIME (no per-prime
  `gr^W_1` to halve); it requires a GLOBAL glued object SUPPLYING `gr^W_1` first. So **C3b is NOT a per-prime
  condition** — it is a condition on the WEIGHT FILTRATION of the glued object; purity is intrinsically global
  for `ζ`. **The precise sense in which C3b is OPEN:** not "prove purity" but "BUILD the carrier purity would
  be a property of" — over `𝔽_q` purity is a theorem ABOUT a pre-existing geometric `H^1`; over `ℤ` there is
  no carrier yet, so construction must precede purity. **C6/DH STRICT-refined to a ladder `DH<ζ<FF`:** FF
  (edge Y, global carrier Y=the curve → purity THEOREM), `ζ` (edge Y, global carrier OPEN=`S²/ℤ` → purity
  OPEN), DH (edge N, no Euler product → purity N/A) — DH lacks even the edge. **Falsifier verdict (DEF/coherence,
  not a `ℤ`-candidate):** the FF-archetype verdict stays euler-borne Y / sees-zeros Y / independent N=Weil purity
  → CIRCULAR over `ℤ`; the NEW content is the typing fact (per-prime carrier empty IDENTICALLY in FF and `ℤ`,
  so the hardness is the GLOBAL carrier, not per-prime). **Successor added:** M4A [DEFINE/BUILD the weight-1
  carrier `gr^W_1` the descent must supply BEFORE purity acts — `S²/ℤ` `H^1` / Connes–Consani `H^•` / condensed
  weight filtration on `ξ`; anchor on the FF rank-`2g` `H^1`; falsify: Euler-assembled + purity sees zeros].

- **2026-06-06 — M2b [DEFINE · anchored]: wrote the hinge clause C3b as a REPRESENTABILITY sub-problem —
  the radius datum is a FUNCTOR `rad : LocFac → 𝔾_m` of the local Euler factors `{L_p}` — and ANCHORED it
  in the FF, where it REFINES to a PURITY functor `rad=(·)^{1/2}∘(edge-abscissa)`: the Euler product gives
  the EDGE `q` directly (exact, functorial), the CENTRE `√q` via DELIGNE PURITY.** [DEF · anchored vs 𝔽_q].
  `research/construction/M2b-radius-functor-C3b.md`, `scripts/numerics/witness/radius_functor.py`
  (+1 `falsify.py` row). **What got DEFINED:** C3b holds for `X` iff there is a functor `rad : LocFac → 𝔾_m`
  (LocFac = local-Euler-factor data) with a natural iso `rad({L_p(X)})≅μ(X)` **factoring through the local
  product** (= "Euler-borne"); C6/DH built in (LocFac empty for DH ⟹ no input ⟹ no `μ`). **What got BUILT
  (FF anchor, 5 Weil curves `q=2,5,7,11,13`, all PASS):** `rad_edge:{L_x}↦q` = the abscissa / rightmost pole
  `T=1/q` of `Z_C=∏_x L_x` (`q=#𝔸¹(𝔽_q)`, purely local, EXACT, no zeros used), verified a genuine FUNCTOR —
  naturality under base change `C/𝔽_q→C/𝔽_{q^k}` exact (`rad_edge(C/𝔽_{q^k})=q^k`, `k=1,2,3`); read the hard
  way `N_n^{1/n}→q` with subleading `O(q^{n/2})` = the `√q` zeros. **THE DECISIVE STRUCTURAL OUTPUT — C3b
  refines to a PURITY functor:** `rad_edge` gives only the EDGE `q` (Worker E's `Re s=1`); the CENTRE radius
  `√q=(edge)^{1/2}` comes via **Deligne purity** (`H^1` pure of weight 1, `(rad_edge)^{1/2}=|α|` to machine
  prec all 5 curves). So **`ℤ`-C3b = "`ζ`'s local factors are PURE of weight 1"**; the radius functor is
  `(·)^{1/2}∘(edge-abscissa)`. **Answers M2's question** (upgrade the FE's `μ=1`?): the upgrade is NOT a new
  multiplier (`μ` stays `1` for `s↔1−s`, C3a DH-shared) but a **SEPARATE Euler datum — the edge abscissa `q`
  — whose square root via purity sets the centre.** **C6/DH now TYPE-LEVEL:** `rad_edge`'s domain LocFac is
  EMPTY for DH (no product ⟹ no `{L_p}`), so the functor doesn't type-check, while `rad_FE=1` survives
  (DH-shared) — the cleanest C6 yet. **Falsifier verdict (anchor, not `ℤ`-candidate):** Euler-borne Y
  (`rad_edge` reads the local product), sees-zeros Y (purity `(edge)^{1/2}=√q` = where the zeros sit),
  independent N (purity=Deligne=FF Weil positivity) → CIRCULAR over `ℤ`, expected (`𝔽_q` owns the radius via
  purity). **Not overclaimed:** defines/anchors the functor; the `ℤ` problem is untouched and now reads
  "construct an Euler-sourced weight/purity structure on `ζ`'s local factors". **Successors added:** M2d
  [DEFINE the per-prime weight/purity structure — `ζ` has no `H^1` at a single prime, so purity needs the
  GLOBAL glued carrier; decide if `rad:LocFac→𝔾_m` is even well-typed for `ζ` or needs the surface `S²/ℤ`
  first]; M4 re-routed (the descent must FIRST supply the weight-1 carrier, THEN purity sets `Re s=½`).

- **2026-06-06 — M2 [ANCHOR-BUILD]: assembled `H^•(C/𝔽_q)` as ONE categorical `ζ`-Hodge datum
  `(𝒞,ω_∞,D,P)` satisfying the M1 contract C1–C6, reproducing the Weil RH proof with the polarization =
  the CANONICAL DUALITY PAIRING (NOT a metric) — DECISIVE C4 check `P_duality − P_gram = 0.00e+00`
  EXACT.** [BUILT · coherence-checked vs 𝔽_q]. `research/construction/M2-ff-hodge-datum.md`,
  `scripts/numerics/witness/ff_hodge_datum.py` (+1 `falsify.py` row). **What got BUILT:** the class
  `FFHodgeDatum(q,a1)` packaging Frobenius `Φ=F`, cup product `E`, Rosati `†=c`, and the primitive
  Hodge-index form as a single object, with `check_C1…C5` each returning PASS/FAIL vs the M1 table. **ALL
  clauses PASS, 5 Weil curves `q=2,5,7,11,13`:** C1 (`spec Φ={αᵢ}`=zeros, `Tr Φ=a₁`=Lefschetz), C2
  (`c=†`Rosati anti-linear, `α†=ᾱ` on `|α|=√q` to `1e-10`, exchanges Hodge lines), C3a (`FᵀEF=qE`
  residual `<1e-12`), C3b (`μ=q`=Frobenius weight, radius `√q` read off `μ`), C4 (**the load-bearing
  test**), C5 (Hodge-index inertia `(0,1,1)→(1,0,1)` off-circle, flip eig `=Σ|α|²−2gq` exact, re-derived
  THROUGH `P_duality`). **THE DECISIVE OUTPUT — C4 holds CATEGORICALLY:** the polarization is built TWO
  ways — `P_duality(φ,ψ)=ev∘(1⊗φ_{FE})=Tr(φ·D(ψ))` (the canonical co-evaluation of the rigid duality `D`,
  where `D(ψ)`=dual of `ψ` under the cup product `E`, NO metric referenced) and `P_gram=Tr(φψ†)` (the
  metric-looking Gram) — and they are **identical to `0.00e+00`** over a spanning basis of `End(H^1)`. So
  the metric appearance is a coordinate artifact: the pairing is FORCED by the cup product, not chosen —
  exactly the §0 design law (what Arakelov's chosen archimedean metric is NOT), and why the FF object
  evades the §0 Sylvester no-go *by construction* (the no-go bites only `*`-congruences of a *chosen*
  background; here there is no chosen background, only the canonical duality). **THE LANGUAGE PASSES THE
  SOLVED CASE** → admitted for the `ℤ` deformation. **Falsifier verdict (anchor, not `ℤ`-candidate):** the
  FF archetype's CIRCULAR-over-`ℤ` (Euler-borne Y via radius `√q`/C3b, sees-zeros Y via the flip/C5,
  independent N = Weil positivity) — expected and correct, because over `𝔽_q` the Euler product OWNS the
  radius. **The sole `ℤ`-hardness localizes into the single hinge C3b** (confirmed in the working model:
  every other clause is a categorical structure on one object); **C6 DH-failure is structural** (no
  Frobenius weight ⟹ no `μ` ⟹ no similitude relation C3a ⟹ no object — the built-in falsifier). **Not
  overclaimed:** this validates the LANGUAGE on the anchor; the `ℤ` problem is untouched, living entirely
  in C3b. **Successors added:** M2b sharpened (the `{L_p}↦μ` functor, with M2's observation that the FE
  similitude is multiplier-1 and must be upgraded to an Euler-read `μ`); M2c [COHERENCE: prove the datum
  is a functorial object of a rigid tensor category — `D∘D≅id`, `φ_{FE}` a morphism, `c` compatible with
  `D` — and redo at `g=2` to confirm the `g=1` semidefiniteness was the trace-kernel artifact].

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
