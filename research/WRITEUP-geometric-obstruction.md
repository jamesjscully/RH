# Two no-go theorems for the geometric strategy on the Riemann Hypothesis, and the char-0/char-p divide

*A self-contained account of the program's results. 2026-06-06.*

## Abstract

We study the obstruction to importing Weil's function-field proof of the Riemann Hypothesis (RH) into the
number-field setting. We (i) reduce RH to a single **reality condition** `F† = F̄` (the Rosati/arithmetic
adjoint equals complex conjugation) on a polarized arithmetic Hodge category; (ii) prove a **Geometric
No-Go** — no coherence structure (rigid-tensor/Tannakian, `C*`/Hermitian, o-minimal/tame) forces the
polarization positive-definite, because off-line spectra are *consistent objects* in each; and (iii) prove
a **Foundational No-Go** — a finite additive characteristic at the archimedean place is *contradictory* with
`ℚ` being a field of characteristic 0, so the finite ground Weil's proof requires at `∞` does not merely
fail to exist, it is forbidden. The unifying mechanism is a **count/radius decoupling**: the reality is
multiplicative and free at every place; the scale `q=|𝔽_q|` is additive (a characteristic) and exists only
over a genuine finite field. Calibration: the Foundational No-Go is a theorem (resting on Ostrowski's
theorem, the definition of characteristic, and the finite-semifield classification); the Geometric No-Go is
established for the strongest candidate structures and argued by exhaustion across the rest.

---

## 1. The strategy and the two results

Over a smooth projective curve `C/𝔽_q`, RH for `ζ_C` is **Weil's theorem**: the Frobenius eigenvalues on
`H¹` satisfy `|α| = q^{1/2}` (purity), forced by the **Hodge index theorem** on the surface `C×C` — a
*geometric* positivity that holds *because* `C×C` is projective over the finite field `𝔽_q`. The "geometric
strategy" for RH over `ℚ` is to build the analogous projective surface over a finite ground for `Spec ℤ`
(the `𝔽₁`/absolute-geometry program). This note proves that strategy is **foreclosed**:

- **Theorem A (Foundational No-Go, §5).** A finite additive characteristic at the archimedean place `∞` of
  `ℚ` is contradictory with `ℚ` having characteristic 0. The finite ground at `∞` that the geometric
  strategy requires *cannot exist* — not for lack of construction, but by definitional identity:
  *archimedean ≡ characteristic 0*.
- **Theorem B (Geometric No-Go, §4, scoped).** Independently of (A), no coherence structure on the
  Frobenius datum forces the polarization positive-definite at the arithmetic scale; off-line spectra
  (RH-violating) are consistent objects in each structure tested. The positivity (= RH) is an irreducible
  external input requiring a real geometric origin — which by (A) `ℚ` lacks at `∞`.

## 2. The reduction: RH ⟺ the reality condition `F† = F̄`

We build a **polarized arithmetic Hodge category** with a universal property whose representing object
`𝕊_ℤ` carries: a Frobenius/flow `F` with `Tr(Fᵗ|H¹) = Σ_ρ e^{tρ}` (zeros = spectrum); a `(p,q)`-grading at
`∞`; a structural duality `D` realizing the functional equation; a **categorical** polarization `P` (the
canonical pairing of `D`, *not* a chosen metric). Validated on the function-field anchor to genus 2: the
polarization equals the Gram exactly (`P_duality = P_gram`), and Weil's proof is reproduced from the new
definitions. (Details: `research/construction/M*.md`.)

The construction reduces RH to one positivity, and peeling that positivity to its atom gives:

> **`RH ⟺ F† = F̄`** — the arithmetic (Rosati) adjoint equals the analytic (complex-conjugation) adjoint;
> equivalently `|α|² = deg` per eigenvalue (the eigenvalues lie on the circle `|α|=√q`).

Three classically separate formulations coincide on this condition (each reached independently):
**(reality)** the eigenvalues are conjugation-stable on the line; **(Hodge–Riemann)** the polarization is
proportional to the Hodge metric; **(Hilbert–Pólya)** `F/√q` is unitary / self-adjoint spectrum.

## 3. The count/radius decoupling (the unifying mechanism)

The condition `F† = F̄` factors, and the factorization is the heart of everything:

- **`F·F† = [deg]` (the functional equation) is FREE** — a formal consequence of rigidity/duality, holding
  at *every* radius (off-line too). It is the **multiplicative** datum: the involution, `Gal`, the reality.
  [Computed: `F·F† = q·I` exactly for off-line `F`, while `|α|² ≠ q`.]
- **`|α| = √q` (the radius) is the deep half** — `q/α = ᾱ`, i.e. `F† = F̄`. This is the **additive** datum:
  `q = |𝔽_q|` is the order of the additive group, the *characteristic*.

> **Count/radius decoupling.** The *reality* (`F† = F̄` as an involution) is multiplicative and free at
> every place. The *scale* `q` is additive — the cardinality of a finite constant field. Over `𝔽_q` they
> are married by a single Frobenius `x↦x^q` doing `+` and `×` at once, with `q` the one number tying
> additive cardinality to multiplicative degree. At `∞` the marriage is broken: one gets the reality
> without the scale.

This decoupling is the invariant that recurs at every level below.

## 4. Theorem B — the Geometric No-Go (scoped)

**Setup.** A *Frobenius datum* is a finite-rank `F` with the explicit-formula trace and a self-duality
`F·F† = [deg]` w.r.t. a non-degenerate pairing. RH for the datum is `|α| = √q` (Step B). We ask whether any
*coherence structure* on the datum forces Step B.

**Theorem B.** For each of the strongest candidate structures, Step B is **not** forced, and RH-violating
(off-line) data are consistent:

1. **(Tannakian / rigid tensor.)** An off-line `F` generates a consistent rigid tensor category; it is
   merely **non-polarizable** (non-compact motivic Galois / Sato–Tate group, a residual `𝔾_m` of ratio
   `|α|/√q`). No rigidity, duality, trace, or `F·F†` condition is violated. *[computed]*
2. **(`C*` / Hermitian.)** The invariant Hermitian form exists and is non-degenerate at every radius; its
   **signature is `(d,0)` positive-definite iff on-line, `(k,k)` Krein iff off-line** *[computed: `(6,0)`
   vs `(3,3)`]*. Positive-definiteness is a strict extra restriction. Doplicher–Roberts (compact group
   from a `C*`-tensor category) **consumes** positivity as an axiom; it never manufactures it from
   tensor/duality coherence — demanding the `C*` form at the arithmetic scale *is* demanding `|α|=√q`.
3. **(o-minimal / tame.)** Purity over `𝔽_q` is Deligne **proper-pushforward** purity (smooth proper ⟹
   pure). Over `ℚ` the archimedean factor `Γ_ℝ(s)=π^{-s/2}Γ(s/2)` has an **infinite-discrete pole
   spectrum** `{0,−2,−4,…}`, hence is **non-o-minimal** (van den Dries finiteness) — the signature of an
   *open/non-proper* fibre. o-minimal GAGA (Bakker–Brunebarbe–Tsimerman) takes properness as an **input**;
   it does not manufacture the proper boundary.

**Consequence.** No structure in this class forces the polarization positive-definite at the arithmetic
scale. The positivity (= RH) is an external input requiring a *real geometric origin* (a projective surface
over a finite ground); by Theorem A, `ℚ` lacks one at `∞`.

**Calibration.** Statements 1–3 are established (computed/cited) for the named structures — the strongest of
their kinds. The universal "no coherence structure forces Step B" is an **exhaustion** across these plus the
audit's instruments (Weil/Li positivity, Bost–Connes QSM, sym²/Rankin–Selberg, dBN flow, prismatic/`q`-de
Rham, condensed/six-functor), each failing identically (Step A free, Step B = an external positivity). It is
theorem-shaped and strongly-evidenced, not a single general proof; the common mechanism (off-line data are
consistent in every coherence structure) is its content.

## 5. Theorem A — the Foundational No-Go (the char-0/char-p divide is irreducible)

This is the program's main theorem. It uses only standard results.

**Definitions.** For a place `v` of a number field, `κ(v)` is its residue field; `char` of a field is the
additive order of `1` (`0` if `n·1 ≠ 0` for all `n>0`). The *scaled-conjugation* object the geometric
strategy needs at `∞` is one carrying both the reality `F†=F̄` (multiplicative) and a finite scale `q ≥ 2`
(a finite additive characteristic = a finite residue field `𝔽_q`).

**Lemma A1 (Ostrowski).** The places of `ℚ` are exactly the `p`-adic places (one per prime, `κ = 𝔽_p`,
non-archimedean) and a unique archimedean place `∞` (the completion is `ℝ`, `κ(∞) = ℝ`).

**Lemma A2 (equivalences at a place).** For a place `v` of `ℚ` the following are equivalent: (i) `v` is
non-archimedean (ultrametric); (ii) `κ(v)` is finite; (iii) `κ(v)` has positive characteristic; (iv) `v`
carries a finite additive characteristic. *(Standard: ultrametric ⟺ `p`-adic ⟺ finite residue field of
char `p`; the Archimedean property `n·1 ↛ 0` is the literal negation of finite additive order of `1`.)*

**Theorem A.** There is no scaled-conjugation object at `∞`. Equivalently, a finite additive characteristic
at `∞` is contradictory with `ℚ` being characteristic 0.

*Proof.* By A1, `∞` is archimedean with `κ(∞) = ℝ ⊇ ℚ`. A finite additive characteristic at `∞` means
`p·1 = 0` in `κ(∞)` for some prime `p`; since `ℚ ⊆ κ(∞)`, this forces `p·1 = 0` in `ℚ`, contradicting
`char ℚ = 0` (`p ≠ 0` in `ℚ`). Equivalently by A2, a finite additive characteristic at `∞` would make `∞`
non-archimedean (`p`-adic) — but `∞` is *defined* as the archimedean place; ultrametrizing it changes which
place it is. ∎

**Proposition A3 (the characteristic-1 diagnostic — why even changing foundations fails).** The only way to
supply a finite additive characteristic to `∞` without a finite field is **characteristic 1** (idempotent
addition, `n·1 = 1`). But the only finite characteristic-1 semifield is `𝔹 = {0,1}` with `|𝔹^×| = 1`
(finite-semifield classification, Connes–Consani/Lescot), forcing the scale `q = 1`. Hence: a finite scale
`q ≥ 2` requires multiplicative torsion (a root of unity `⟹` a finite field `⟹` char `p`); idempotence
(which supplies the additive characteristic) forces the multiplicative group trivial. **The additive
characteristic and a nontrivial multiplicative scale are mutually exclusive off a genuine finite field.**

**Corollary A4 (RH is char-0-hard, formally).** The Weil/Hodge-index derivation of purity requires `C`
projective over a *finite field*; its number-field analogue requires a finite ground at `∞`, which by
Theorem A does not exist. The geometric strategy is therefore not difficult-at-`∞` but **foreclosed-at-`∞`**.

**The identity (the deepest statement).** Theorem A is the chain of definitional equivalences
> *archimedean place* ≡ *residue field `⊇ ℚ`* ≡ *characteristic 0* ≡ *torsion-free addition (`n·1 ↛ 0`)* ≡
> *all primes inverted (chromatic height 0, `𝕊[1/p : ∀p]`)* ≡ *non-ultrametric (Ostrowski)*.
A finite additive scale negates the last four clauses, hence the first.

**Independent confirmation (Feb 2026).** In Connes–Consani's `Jac(\overline{Spec ℤ})`, the finite additive
scale a place carries is the circle `C_p ≅ ℝ/(log p)ℤ` — a *strictly finite-prime* phenomenon — and `∞` is
the degenerate fixed point `C_∞ = {(ℤ,0)}` where that circle collapses to a point. The only torsion `∞`
carries is the **multiplicative** `ℚ/ℤ` (roots of unity = the reality), never the additive scale.

## 6. The `𝔽₁`-exhaustion (support for Theorem A)

Theorem A is corroborated by an exhaustive survey: no candidate finite ground supplies an archimedean
arithmetic scale, each failing by the count/radius decoupling. **Bases:** sphere spectrum `𝕊` (homotopy
cardinality = a count, not the radius); tropical/characteristic-1 (`q→1` dequantized); Borger–Witt
(finite-prime-indexed, no `ψ_∞`); monoid/Deitmar–Soulé (valuation continuum); Tate-twist period (`2π`, a
transcendental, not a finite `q`); global/product-formula (the audit edge). **Degeneration:** the
archimedean Fargues–Fontaine / twistor curve (real and current — Viehmann–Zeff 2024, Connes–Consani 2026)
has residue field `ℂ` (continuum), `Gal(ℂ/ℝ)` of modulus 1, slope `½` — the reality, no scale `q`. The
`p`-adic FF curve carries `q` only by *importing* `Spec 𝔽_p` via Witt vectors; `ℝ` has no finite residue to
import. (Details: `research/f1-construction.md`, `research/construction/F1-*.md`, `CN-*.md`.)

## 7. Scope, consequences, and honest status

**What is proven.** Theorem A is a theorem (standard inputs). Proposition A3 is a theorem (finite-semifield
classification). The reduction `RH ⟺ F†=F̄` and the count/radius decoupling are established constructively
and validated on the function-field anchor. Theorem B is established for the strongest candidate structures
and argued by exhaustion across the rest (theorem-shaped, strongly-evidenced; not one general proof).

**What is not claimed.** We do not prove or disprove RH. Theorem A is *not* an undecidability statement; it
is the precise limit of one strategy. That the char-0/char-`p` divide obstructs RH is the founding intuition
of the `𝔽₁` program; the contribution here is its **formalization as a foundational contradiction** and the
**exhaustion** showing every geometric route hits it.

**Consequence.** If RH is provable, the proof cannot route through giving `∞` a finite ground: that road is
closed by Theorem A. RH must be approached either (i) by methods living entirely on the archimedean/char-0
side — analytic number theory, the explicit formula, de Branges / Hilbert–Pólya **as analysis** (a
self-adjoint operator constructed *without* an underlying finite-ground geometry) — or (ii) by a genuinely
new foundation in which the identity *archimedean ≡ characteristic 0* is itself reconceived. The latter is
not a theorem to prove but a foundation to invent, and no current framework achieves it.

**One-line summary.** Over function fields RH is a theorem because the finite ground is present; over `ℚ`
the geometric strategy is foreclosed because the finite ground at `∞` is not missing but *forbidden* —
*archimedean ≡ characteristic 0* — and the positivity RH needs is, in every coherence structure, an external
input that only a finite ground supplies.

---

*Sources in-repo: `research/the-complete-account.md` (full arc); `research/positivity-program.md` (the
audit); `research/construction/` (M/R/PA/RF/PP/NG/F1/CN/NF logs); `research/f1-construction.md`,
`research/new-foundations.md` (the two no-gos); `scripts/numerics/witness/` (anchors + falsifier).*
