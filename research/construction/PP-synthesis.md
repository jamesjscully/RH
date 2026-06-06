# PP-synthesis — "reality = properness of the archimedean fibre": GENUINE FRAME, GEOMETRIC TERMINUS [SYNTHESIS · judge]

**Charter under judgment.** RH residue = `F†=F̄` (Rosati adjoint = conjugation = `|α|=√deg` = the line),
reframed as PROPERNESS of the archimedean fibre of `bar(Spec ℤ)`, because over `𝔽_q` purity (`F†=F̄`) IS
Deligne **proper-pushforward purity** (smooth proper ⟹ pure cohomology ⟹ perfect Poincaré duality ⟹
Rosati adjoint = conjugate). The bet: compactify the archimedean fibre and properness FORCES reality (no
imposed positivity), with condensed/analytic geometry (Clausen–Scholze) as the living tool.

**Inputs judged.** Three angle-logs, all anchored on real `𝔽_q` curves, no zeros assumed:
`PP-proper-vs-open-anchor.md` (GENUINE_LEAD-as-anchor, 4fb704d), `PP-archimedean-non-properness.md`
(PARTIAL, 28b2f9b), `PP-condensed-compactification.md` (TERMINUS_GEOMETRIC, d13846c). The anchor witness
`scripts/numerics/witness/proper_vs_open_anchor.py` was **re-run live for this synthesis** and reproduces
exactly: proper `H¹` pure (`|α|=√q`, all 4 of `(q,a)=(5,1),(7,3),(11,-2),(13,4)`); open `H¹_c` mixed
(weight-0 drop, ≥2 pts removed); `F†=F̄` forced on the pure part; **skeptic control (3b) off-line
`q/α ≠ ᾱ`** while the pairing `α·β=q` still holds.

---

## The three angles AGREE on every fact and DISAGREE only on the label

This is the decisive observation of the synthesis. The three verdicts —
GENUINE_LEAD / PARTIAL / TERMINUS_GEOMETRIC — look like a disagreement, but they are **three names for one
fact-set**. Every angle independently established, with no contradictions:

1. **Purity over `𝔽_q` IS genuinely proper-pushforward purity** (a real theorem, anchor [computed] in all
   three): smooth proper curve ⟹ single Frobenius modulus `√q` ⟹ `F†=F̄`; open/non-proper curve ⟹ mixed
   weights `{0,1}` / `{1,5}` ⟹ purity LOST. The reframe "reality = properness" is **structurally correct.**
2. **Properness factors into Step A (free) + Step B (deep), and ONLY Step A is forced by properness.**
   - **Step A — FREE:** perfect Poincaré pairing `H¹×H¹→H²=ℚ(−1)` ⟹ `α ↔ q/α` ⟹ the functional equation
     `F·F†=q·id`. A formal consequence of properness/smoothness. **Holds at every radius** (skeptic
     control 3b; off-line multiset `{5,1.8,1.8,5}` with correct count, variance>0).
   - **Step B — DEEP:** `|α|=√q` (the radius) ⟹ `q/α=ᾱ` ⟹ `F†=F̄`. This is **Weil II** = Deligne RH over
     `𝔽_q`, whose only known proof is **Rankin-squaring positivity** ("squares of reals are nonnegative"),
     which is **finite-field-bound** and (Kedlaya) "not very compatible" with the archimedean place.
   So **properness ENABLES but does not constitute reality.** Properness gives the duality/FE; the radius
   is a separate theorem. All three angles say this identically (the program's own count/radius decoupling,
   here *re-derived from properness*).
3. **The archimedean fibre is genuinely NON-PROPER, precisely located.** `Γ_ℝ(s)=π^{−s/2}Γ(s/2)` is a
   **zeta-regularized determinant of an UNBOUNDED operator** (Deninger / Consani–Marcolli) — the *logarithm*
   of Frobenius, a derivation, not a Frobenius automorphism — on an **INFINITE-dimensional** `H¹_arch`
   (pole spectrum `{0,−2,−4,…}`). A proper fibre gives a **polynomial** local factor (finite char-poly,
   degree `2g`); the `Γ`-factor is an infinite product. Hence: infinite-dim cohomology, **non-perfect
   Poincaré duality**, no finite-weight `H²=ℚ(−1)`, no finite `q` for `|α|²=q` to equal. This is the
   **same open/affine signature** as `H¹_c(U)` (the open curve's boundary weight-0 drop) — `deg P=0`,
   infinite denominator — the M2d match.

The labels differ only in **where each angle stops on the same ladder**:
- "GENUINE_LEAD" (angle 1) = *the frame is right and the obstruction is a living geometric one* (compactify
  the fibre) — true, but it is an **anchor**, and its own skeptic control proves properness does NOT force
  reality, so the "lead" is the frame, not a forcing.
- "PARTIAL" (angle 2) = *properness is necessary, real, missing at `∞`, but not a discharged corollary* —
  the honest middle, identical facts.
- "TERMINUS_GEOMETRIC" (angle 3) = *the missing Step-B object is intrinsically non-compactifiable in the
  one living candidate theory checked* — the same facts, plus the **negative result** that condensed
  geometry supplies the wrong theorem (duality, not purity).

**There is no genuine contradiction.** The synthesis verdict is the conjunction:
**the frame is GENUINE and the residue is a clean GEOMETRIC TERMINUS** — these are compatible, because the
frame being right is exactly what makes the terminus *sharp* (it names what is missing precisely).

---

## Answering the three judge questions, with the discipline

### (1) Is "proper ⟹ pure ⟹ F†=F̄" a genuine FREE mechanism, anchored, recoverable without zeros?

**PARTLY — and the honest part is the load-bearing one.** Anchored: YES, unconditionally over `𝔽_q`
(re-run live; proper pure, open impure, `F†=F̄` on the pure part, all without zeros). **But the skeptic
control (3b) is decisive and it CUTS AGAINST the strong reading:** the perfect pairing alone gives only
`α·β=q` (Step A), which holds at *every* radius; `q/α=ᾱ` (reality) holds **only** at `|α|=√q`. So:

> **Properness forces the FUNCTIONAL EQUATION (Step A) for free; it does NOT force REALITY (Step B).**
> The reality is the radius `|α|=√q` = Weil II = RH over `𝔽_q`, a separate deep theorem (Rankin
> positivity on the proper family). Properness *enables* that positivity (finite-dim, perfect PD,
> polynomial L-factor) but is not it.

**Is the dead "imposed positivity" branch bypassed?** Subtly: the positivity is **NOT imposed** — over
`𝔽_q` it is a *theorem on a proper family* (Rankin/`sym²`/`X×X`), genuinely free given the finite field.
So the reframe converts "**impose a positivity**" into "**supply the proper compactification on which the
Rankin positivity is RUNNABLE.**" That is a real and *strictly sharper* relocation — but it is **not** a
free forcing of `F†=F̄`. So: **the dead positivity branch is bypassed as a FRAMING (positivity becomes a
consequence of a proper structure, not an axiom), but the missing object is now the proper structure, and
it is exactly as missing as before.** Honest score: the FRAME advances; the WALL does not move.

### (2) Is the non-properness the precisely-located residue = R6/R7/R8 correctly renamed?

**YES — and this is the synthesis's strongest, fully-earned claim.** The residue is located at one
concrete structural fact, reached independently three times and matching M2d/R6/R7/R8:

> The archimedean fibre has **infinite-dimensional cohomology** (`Γ_ℝ` = regularized `det_∞` of a
> *log-Frobenius* unbounded operator), hence **non-perfect Poincaré duality** and **no finite-weight `H²`
> carrying a finite cardinality `q`**. This is the **open/affine signature** of `H¹_c(U)` (boundary
> weight-0 drop) transcribed to `∞`.

The renaming is genuine and sharpening: R6/R7/R8's "missing finite constant/residue field at `∞`
(`|κ(∞)|`, `κ(t=0)=ℂ` continuum)" is **the same atom** as "a missing **proper boundary / weight-pure top
class** that would make `H¹_arch` finite-dim with perfect PD." Over `𝔽_q` that boundary is exactly the
finite constant field supplying the weight-pure `(1−qT)^{−1}`. The infinite-dimensionality (angle 3) and
the no-finite-`q` (angles 1,2) are **the same obstruction in two vocabularies** (analytic / cohomological).
**This is a real gain: the residue is now a NAMED geometric object (a missing proper boundary), not a vague
"finite field."**

### (3) THE DECISION — compactifiable (lead) or intrinsically not (geometric terminus)?

**In the only living candidate theory actually checked against its primary sources (condensed/analytic
geometry, Clausen–Scholze), the answer is INTRINSICALLY NOT — a clean GEOMETRIC TERMINUS.** The discipline
demands I distinguish "aspirational" from "lead," and here the negative result is *concrete and sourced*,
not a failure of imagination:

- **[checked, Lectures XIII–XV]** Clausen–Scholze complex-analytic geometry proves **Serre duality + GAGA +
  HRR** — *coherent / Dolbeault* duality. Not a weight filtration, not a Frobenius, not `|α|=q^{w/2}`.
- **[checked, Scholze 2510.26269 v2, Jan 2026]** The six-functor formalism gives abstract
  **Poincaré–Verdier duality** (`f^!`, `f_!`, dualizing complexes, even proper base change without
  properness) but is **provably agnostic about weights and Frobenius eigenvalues.** **Duality ≠ purity.**
- **[checked, Kedlaya Weil II]** Purity's only known proof is **Rankin positivity over a finite field**,
  archimedean-incompatible. Abstract proper-pushforward does **not** formally yield purity.
- **[checked, Deninger/Consani–Marcolli]** The archimedean fibre is **intrinsically non-compact**:
  infinite-dim cohomology, only a *log* of Frobenius. A proper fibre would give a polynomial; `Γ_ℝ` is an
  infinite product.

> **VERDICT: GEOMETRIC TERMINUS, not a condensed-geometry lead.** The frame ("reality = properness") is
> genuine and the residue is precisely a missing proper structure — but the **one living theory that does
> honest archimedean geometry supplies DUALITY, which is exactly the RH-silent Step A, and is silent on
> PURITY (Step B), which is the residue.** This is the same atom as R8 (no finite ground at `∞`) reappearing
> as infinite-dimensionality / log-vs-honest Frobenius. **A finite-dim pure cohomology at `∞` would BE the
> missing `ψ_∞`.** The terminus is *sharper* than R8's finite-cardinality statement because it names the
> missing object structurally (proper boundary / weight-pure top class collapsing the `det_∞` to a finite
> char-poly) and identifies the precise reason the obvious living tool cannot supply it (it delivers
> duality, not purity).

**Is there ANY honest residual lead?** One, and it must be stated as **aspirational, not a lead**, to keep
the discipline: the next construction below is a *target object*, not a theorem-in-hand. There is no known
applicable proper-pushforward purity theorem in condensed geometry (checked); so calling this a "lead"
would overstate. It is a **well-posed terminus with a sharp open construction**, which is more than R8 had.

---

## The precise next construction (aspirational target, stated exactly)

What must be built (the named object `ψ_∞`), stated as the synthesis distilled it:

> **Collapse the log-Frobenius `det_∞` to a finite char-poly.** Construct an archimedean fibre whose
> cohomology `H¹_arch` is **finite-dimensional** with a **PERFECT Poincaré pairing valued in a
> weight-pure `H²≅ℚ(−1)` carrying a finite cardinality `q_∞`** (an *honest* archimedean Frobenius `F_∞`,
> NOT its logarithm `Φ`). Concretely the lift `Φ ⟼ F_∞ = exp` that turns the infinite gamma-spectrum
> `{0,−2,−4,…}` (unbounded derivation, infinite product `Γ_ℝ`) into a finite Frobenius spectrum
> (polynomial local factor). **The required proper-pushforward theorem does not exist** in condensed
> geometry as checked (it gives Serre/Verdier *duality*, agnostic on weights); so the construction must
> *first* supply the finite ground (the weight-pure top class / finite constant field at `∞`), and only
> *then* would a Rankin-squaring positivity become runnable to force `|α|=√q_∞`. **Order matters: finite
> ground FIRST (the missing object), positivity SECOND (free once the ground exists).**

Two concrete probes the logs leave open (both *tests of the terminus*, not leads):
- Does any zeta-regularized-determinant / finite-rank self-dual truncation of `Γ_ℝ` yield a finite perfect
  Poincaré pairing with a marked radius — or does *every* regularization keep the trace finite but leave
  the **radius unmarked** (`q` absent)? If the latter, re-confirms the terminus from the analytic side.
- Does the foliated-dynamics / leafwise-cohomology program (Deninger conjecture, arXiv 2410.20758) ever
  produce **finite-dim** leafwise cohomology, or is it also intrinsically infinite-dim? (Decides whether
  *any* living theory escapes the log-Frobenius wall.)

---

## What is genuinely different from the dead positivity branch

The dead branch was: **impose** a positivity/reality on the archimedean datum (Li/Weil/Rosati positivity
asserted as a hypothesis) — circular, because the positivity IS the radius IS RH (RF-synthesis:
`F†·F=scalar = RH`; the radius is free given degree, `deg=q` is RH). The PP reframe is genuinely different
in **kind**:

> **Positivity stops being an axiom and becomes a COROLLARY of a geometric structure (properness).** Over
> `𝔽_q` the Rankin positivity is not imposed — it is a theorem on the proper family. So the question is no
> longer "why is this positivity true?" (unanswerable as an axiom) but "**can the archimedean fibre be made
> proper?**" — a construction in a living theory (condensed geometry / Deninger flow). That is a real shift:
> from *imposing a metric* to *building a space*. **But** — and this is why it is a terminus, not a lead —
> the building has been *checked against the live tool and fails*: condensed geometry supplies the duality
> (Step A) and is silent on the purity (Step B), and the fibre is intrinsically infinite-dim. **So the
> reframe relocates the wall onto firmer, better-named ground (a missing proper boundary, testable in a
> real theory) without moving it.** The advance is *diagnostic precision*, not progress past the wall.

---

## Synthesis verdict

`[SYNTHESIS · judge]` — **GENUINE FRAME / GEOMETRIC TERMINUS (not a condensed-geometry lead).** The reframe
"`F†=F̄` = properness of the archimedean fibre" is **structurally correct and anchored unconditionally over
`𝔽_q`** (re-run live: proper pure, open impure, `F†=F̄` forced on the pure part, no zeros). It **factors the
residue cleanly**: properness FORCES the perfect-pairing functional equation (Step A, RH-silent, present at
`∞` via `ξ(s)=ξ(1−s)`); the RADIUS `|α|=√q` (Step B, = `F†=F̄`) is Weil II / Rankin-positivity = RH, which
properness *enables* but does not *constitute*. The non-properness at `∞` is the **precisely-located
residue** — infinite-dim `Γ`-cohomology (regularized `det_∞` of a *log*-Frobenius), non-perfect PD, no
finite `q` — the **same atom as R6/R7/R8 correctly renamed** as a *missing proper boundary / weight-pure top
class*, sharper than "a finite field." **The decision:** the one living candidate (condensed/analytic
geometry, checked against primary sources) supplies **DUALITY, not PURITY** — Serre/Verdier self-pairing is
exactly the RH-silent Step A and is provably agnostic about weights/Frobenius; purity's only proof imports a
finite field absent at `∞`. So the fibre is **intrinsically non-compactifiable in that theory** = a clean
GEOMETRIC TERMINUS, with a **sharply named** open object `ψ_∞` (collapse the log-Frobenius `det_∞` to a
finite char-poly: an honest archimedean Frobenius / finite ground, *then* positivity is free). **NOT
CIRCULAR** (no zeros imported anywhere; the skeptic control explicitly excludes "properness-alone-forces-
reality"). **Genuinely different from the dead positivity branch** — positivity becomes a corollary of a
geometric structure rather than an imposed axiom — but the structure has been checked against the live tool
and is missing: the reframe **relocates the wall onto firmer, better-named ground without moving it.**

**Honest odds.** As a *frame*: high value (correctly converts "impose positivity" → "build a proper fibre,"
names the residue structurally). As a *path to a proof via condensed geometry*: **low** (~3–5%) — the
checked theorems are duality, not purity, and the fibre is intrinsically infinite-dim; no applicable
proper-pushforward purity theorem exists there. The real probability mass sits on whether **any** theory
(Deninger foliated dynamics, a genuine archimedean Frobenius, or an unbuilt finite-ground construction)
can collapse the `det_∞` to a finite char-poly — the log-Frobenius-to-Frobenius lift — which is `ψ_∞`
itself and remains unconstructed.

**Next step.** Stop probing condensed geometry for purity (terminus confirmed three ways). Target the
`det_∞ ⟶` finite-char-poly collapse directly: test whether **any** regularization/truncation of `Γ_ℝ`
yields a finite perfect-PD object with a MARKED radius, and whether Deninger's leafwise cohomology is ever
finite-dim. If every route keeps the trace finite but the radius unmarked, that *closes* `ψ_∞` as a
type-obstruction terminus (the finite ground `ℤ` lacks at `∞`) from the proper-pushforward side — the
sharpest statement of the wall the program has reached.
