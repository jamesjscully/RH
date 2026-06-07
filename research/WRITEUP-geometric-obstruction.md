# Two no-go theorems for the geometric strategy on the Riemann Hypothesis, and the char-0/char-p divide

*A self-contained account of the program's results. 2026-06-06.*

---

## 0. Preface for the non-specialist — what was and was not achieved

The Riemann Hypothesis (RH) is open for the ordinary whole numbers, but it is a **theorem** for a parallel
universe of "numbers" called *function fields* (polynomials over a finite field) — proved by André Weil in
1948 using geometry: he built a surface and used a positivity theorem (the Hodge index theorem) about it.
For seventy years the dream has been to import that geometric proof to the ordinary integers. This is the
"field with one element" / "absolute geometry" program of Connes, Consani, Deninger, and others.

**This work does not prove or disprove RH.** What it does is map, precisely and to the bottom, *why the
geometric strategy resists* — and the conclusion is sharp:

> **The geometric strategy cannot work for the ordinary integers — not because it is hard, but because it
> asks for something that is logically contradictory.**

The analogy is exact and is the key to everything. In the function-field universe, *every* place (every
"point," including the one "at infinity") sits over a **finite field of constants** — a finite ground. For
the integers, every prime `p` also sits over a finite ground (the field with `p` elements). But there is one
exceptional place — the "place at infinity," which is the *real numbers* — and the real numbers are **not
finite and have no finite ground.** Weil's proof needs a finite ground at *every* place. The integers have
one everywhere except at infinity.

We prove this gap is **irreparable**. "The place at infinity is, by its very definition, *characteristic
zero*" — and a finite ground there would force a contradiction (a prime number equal to zero). We also prove
that no clever modern machinery (categories, homotopy theory, condensed mathematics, the Fargues–Fontaine
curve, the field with one element in all its known forms) repairs it: each supplies the *easy* half of what
RH needs (a symmetry, the "functional equation") for free, but the *hard* half (the positivity that is RH
itself) is, in every one of them, an external input that only a genuine finite ground provides.

**The upshot.** If RH is provable at all, the proof cannot go through giving the place at infinity a finite
ground — that road is now closed with a proof. RH must be reached either by pure analysis (the classical
analytic theory, the explicit formula, a self-adjoint-operator approach pursued as *analysis*, not geometry)
or by genuinely new foundations in which what "infinity" and "a number" mean are reconceived from scratch —
which nobody currently knows how to do. The value of this work is a complete, honest map: it shows every
geometric road and the single bedrock under all of them, and names that bedrock precisely.

---

## Abstract

We study the obstruction to importing Weil's function-field proof of RH into the number-field setting. We
(i) reduce RH to a single **reality condition** `F† = F̄` on a polarized arithmetic Hodge category; (ii)
prove a **Geometric No-Go** — no coherence structure (rigid-tensor/Tannakian, `C*`/Hermitian, o-minimal)
forces the polarization positive-definite, because off-line spectra are *consistent objects* in each; and
(iii) prove a **Foundational No-Go** — a finite additive characteristic at the archimedean place is
*contradictory* with `ℚ` being characteristic 0, so the finite ground Weil's proof requires at `∞` is not
missing but forbidden. The unifying mechanism is a **count/radius decoupling**: the reality is multiplicative
and free at every place; the scale `q=|𝔽_q|` is additive (a characteristic) and exists only over a genuine
finite field. **Calibration:** the Foundational No-Go is a theorem (Ostrowski + the definition of
characteristic + the finite-semifield classification); the Geometric No-Go is established with computed
witnesses for the strongest candidate structures and argued by exhaustion across the rest.

---

## 1. The strategy and the two results

Over a smooth projective curve `C/𝔽_q`, RH for `ζ_C` is **Weil's theorem** [W1948]: the Frobenius eigenvalues
on `H¹` satisfy `|α| = q^{1/2}` (purity), forced by the **Hodge index theorem** on `C ×_{𝔽_q} C` — a
*geometric* positivity holding *because* the surface is projective over the finite field `𝔽_q`. The geometric
strategy for RH/`ℚ` builds the analogous projective surface over a finite ground for `Spec ℤ` (the
`𝔽₁`-program). This note proves the strategy is **foreclosed**:

- **Theorem A (Foundational No-Go, §5).** A finite additive characteristic at the archimedean place `∞` of
  `ℚ` is contradictory with `ℚ` having characteristic 0. The finite ground at `∞` the strategy requires
  cannot exist — by the definitional identity *archimedean ≡ characteristic 0*.
- **Theorem B (Geometric No-Go, §4, scoped).** Independently, no coherence structure on the Frobenius datum
  forces the polarization positive-definite; off-line (RH-violating) spectra are consistent in each. The
  positivity (= RH) is an external input requiring a real geometric origin — which by (A) `ℚ` lacks at `∞`.

## 2. The reduction: RH ⟺ the reality condition `F† = F̄`

We construct a **polarized arithmetic Hodge category** whose representing object `𝕊_ℤ` carries: a Frobenius
`F` with `Tr(Fᵗ|H¹)=Σ_ρ e^{tρ}`; a `(p,q)`-grading at `∞`; a structural duality `D` (the functional
equation); a **categorical** polarization `P` = the canonical pairing of `D`, *not* a chosen metric.
Validated on the function-field anchor to genus 2: `P_duality = P_gram` exactly, and Weil's proof is
reproduced from the new definitions (`research/construction/M*.md`). Peeling the resulting single positivity
to its atom:

> **`RH ⟺ F† = F̄`** — the arithmetic (Rosati) adjoint equals the analytic (conjugation) adjoint;
> equivalently `|α|² = deg` per eigenvalue. The three classical formulations — reality, Hodge–Riemann
> metric-compatibility, Hilbert–Pólya self-adjointness — coincide on this condition.

## 3. The count/radius decoupling (the unifying mechanism)

`F† = F̄` factors, and the factorization recurs at every level:

- **`F·F† = [deg]` (the functional equation) is FREE** — formal from rigidity/duality, holding at every
  radius (off-line too). The **multiplicative** datum: the involution, `Gal`, the reality. [Computed:
  `F·F†=q·I` exactly off-line while `|α|²≠q`.]
- **`|α|=√q` (the radius) is the deep half** — `q/α=ᾱ`. The **additive** datum: `q=|𝔽_q|` is the order of
  the additive group, the *characteristic*.

> **Count/radius decoupling.** Reality (multiplicative) is free at every place; scale `q` (additive
> characteristic) exists only over a finite field. Over `𝔽_q` one Frobenius `x↦x^q` marries `+` and `×` with
> `q` the single number tying additive cardinality to multiplicative degree. At `∞` the marriage breaks: one
> gets the reality without the scale.

## 4. Theorem B — the Geometric No-Go (scoped), with exhaustion table

**Setup.** A *Frobenius datum* is a finite-rank `F` with the explicit-formula trace and a self-duality
`F·F†=[deg]`. RH for the datum is `|α|=√q` (call it **Step B**); the duality/FE is **Step A**.

**Theorem B.** No coherence structure on the datum forces Step B. In every structure tested, Step A is free
and archimedean-native, while off-line (`|α|≠√q`) data are *consistent objects* and Step B is an external
positivity. The exhaustion (each row: what is free, why Step B fails, the witness):

| structure / instrument | Step A (free) | why Step B is not forced (failure mode) | witness / ref |
|---|---|---|---|
| **Tannakian / rigid tensor** | finite-dim, duality, FE | off-line `F` generates a **consistent non-polarizable** category (non-compact motivic Galois, residual `𝔾_m`); no axiom violated | `NF`/`frob_tannakian`; Deligne–Milne [DM1982] |
| **`C*` / Hermitian** | the invariant form exists, non-degenerate | signature **`(d,0)` on-line vs `(k,k)` Krein off-line** (`(6,0)` vs `(3,3)`); Doplicher–Roberts *consumes* positivity, never makes it | `cstar_hermitian_witness.py`; [DR1989] |
| **o-minimal / tame** | proper-pushforward purity over `𝔽_q` | `Γ_ℝ(s)` has infinite-discrete poles ⟹ **non-o-minimal** (open/affine signature); GAGA takes properness as *input* | `proper_vs_open_anchor.py`; [BBT2022],[vdD1998] |
| **Weil / Li positivity** | the explicit-formula form | PSD ⟺ RH — **circular** (= RH restated) | `weil_form.py` |
| **Bost–Connes QSM** | KMS states, partition function | free energy is **RH-silent** (does not see zero locations) | `qsm_free_energy.py`; [BC1995] |
| **sym² / Rankin–Selberg** | Euler-borne, independent | forces the **edge `Re s=1`** (Siegel), never the line | `hecke_certificate.py` |
| **de Bruijn–Newman flow** | dynamics + zero statistics | escapes the static lock but the **GUE lever is universal/RH-silent**; reduces to the same wall | `xi_jensen.py`, `falsify.py` |
| **prismatic / `q`-de Rham** | `q`-deformed FE | finite-prime-indexed, **archimedean-blind**; `Γ_q` is *more* infinite (2-D pole lattice) | `QD-q-deformation-boundary.md` |
| **condensed / six-functor** | coherent duality (the FE) | supplies Step A only; Step B (radius) provably not | `PP-*` |
| **abelian-variety / Rosati** | `F·F†=[deg]` (free tautology) | the scalar is free; `F†=F̄` (positive-definite) **is** RH | `RF-*`; rosati_reflection.py |

**Calibration.** Rows 1–3 are the strongest of their kind, established with computed witnesses; the universal
claim is an **exhaustion** across the table. The common mechanism — *off-line spectra are consistent in every
coherence structure; positive-definiteness is always a strict extra input* — is its content. (Detail:
`research/the-complete-account.md`, `research/positivity-program.md`, `research/construction/`.)

## 5. Theorem A — the Foundational No-Go (formal)

Standard inputs only. We use: a *place* `v` of `ℚ` (an equivalence class of nontrivial absolute values); its
completion `ℚ_v`; the residue field `κ(v) = 𝒪_v/𝔪_v` when `v` is non-archimedean (`𝒪_v` the valuation ring);
and `char` = the additive order of `1`. The Weil hypothesis at a place is "`κ(v)` is a finite field `𝔽_{q_v}`
and Frobenius acts with eigenvalue-modulus `q_v^{w/2}`."

**Lemma A1 (Ostrowski's theorem [O1916]).** Every nontrivial place of `ℚ` is equivalent to exactly one of:
the `p`-adic absolute value `|·|_p` (one per prime `p`; non-archimedean; `ℚ_p`; `κ = 𝔽_p`), or the usual
absolute value `|·|_∞` (archimedean; `ℚ_∞ = ℝ`). *(Standard; see [Ne1999, II §3], [Ca1986].)*

**Lemma A2 (place type ⟺ residue characteristic).** For a nontrivial place `v` of `ℚ` the following are
equivalent: **(i)** `v` is non-archimedean (`|x+y|_v ≤ max(|x|_v,|y|_v)`); **(ii)** `ℤ` is bounded in `ℚ_v`
(`|n|_v ≤ 1 ∀n∈ℤ`); **(iii)** `v` has a finite residue field `κ(v)`; **(iv)** `char κ(v) = p > 0`. The
negations are equivalent in turn: `v` archimedean ⟺ the Archimedean property holds (`∀x ∃n: |n·1|_v>|x|_v`)
⟺ `ℚ_v ⊇ ℝ ⊇ ℚ` ⟺ `char(ℚ_v)=0`. *(Standard valuation theory: non-archimedean ⟺ ultrametric ⟺ a discrete
valuation with finite residue field, for `ℚ`; the Archimedean property `n·1↛0` is literally the negation of
finite additive order of `1`.)*

**Theorem A.** There is no object furnishing the archimedean place `∞` of `ℚ` with a finite additive
characteristic (equivalently, with a finite residue field). Hence the Weil hypothesis fails at `∞`, and not
contingently: it is contradictory with `char ℚ = 0`.

*Proof.* By A1, `∞` is archimedean and `ℚ_∞ = ℝ ⊇ ℚ`. Suppose a finite additive characteristic `p>0` were
furnished at `∞` — i.e. `p·1 = 0` in the residue/completion datum `k` carrying the place, where `ℚ ⊆ k`
(every completion of `ℚ` contains `ℚ`; for `∞`, `ℚ ⊆ ℝ = k`). Restricting to `ℚ ⊆ k`, `p·1 = 0` in `ℚ`. But
`char ℚ = 0`, so `p·1 = p ≠ 0` in `ℚ` — contradiction. Equivalently by A2, a finite additive characteristic
at `∞` is equivalent to `∞` being non-archimedean, contradicting A1's classification of `∞` as *the*
archimedean place. ∎

**Proposition A3 (the characteristic-1 diagnostic — relaxing "field").** Suppose one drops the field axiom to
admit a finite additive characteristic on a *semifield*. The only finite semifield with idempotent addition
(`a⊕a=a`, "characteristic 1") is the Boolean semifield `𝔹=({0,1},max,·)`, whose multiplicative group `𝔹^×`
has order `1` [CC2009, §2.6; L]. Therefore any finite-additive-characteristic structure at `∞` avoiding a
finite field is characteristic-1, forcing the scale `q = |𝔽_q^×|+1` to `q = |𝔹^×|+? = 1`. More directly: a
finite scale `q ≥ 2` has `q−1 ≥ 1` units forming the cyclic group `μ_{q−1}` of `(q−1)`-th roots of unity
(multiplicative torsion), whose existence with a compatible additive structure of finite characteristic is
exactly a finite field `𝔽_q` (char `p`). Hence **a finite additive characteristic and a nontrivial finite
multiplicative scale coexist only on a genuine finite field.** ∎

**Corollary A4 (RH is char-0-hard, formally).** Weil's proof of RH/`𝔽_q(C)` requires `C` projective over the
finite field `𝔽_q`, hence a finite residue field at *every* place of `𝔽_q(C)` (including its place at
infinity, whose residue field is a finite extension of `𝔽_q`). The number-field analogue requires a finite
residue field at every place of `ℚ`; by Theorem A this fails at `∞`, and by Proposition A3 it is irreparable
by weakening "field" to "semifield." The Weil/Hodge-index strategy therefore does not transfer to `ℚ`. ∎

**The identity (the content of A1–A4 in one line).**
> *archimedean place* ≡ *residue field `⊇ ℚ`* ≡ *characteristic 0* ≡ *torsion-free addition (`n·1↛0`)* ≡
> *all primes inverted (chromatic height 0, `𝕊[1/p:∀p]`)* ≡ *non-ultrametric (Ostrowski)*.
A finite additive scale at `∞` negates the last four clauses, hence the first.

**Independent confirmation (2026).** In Connes–Consani's `Jac(\overline{Spec ℤ})`, the finite additive scale
a place carries is the circle `C_p ≅ ℝ/(log p)ℤ` (a strictly finite-prime phenomenon); `∞` is the degenerate
fixed point `C_∞={(ℤ,0)}` where the circle collapses to a point. The only torsion `∞` carries is the
**multiplicative** `ℚ/ℤ` (roots of unity = the reality), never the additive scale [CC2026].

## 6. The `𝔽₁`-exhaustion (support for Theorem A)

No candidate finite ground supplies an archimedean arithmetic scale; each fails by the count/radius
decoupling. **Bases:** sphere spectrum `𝕊` (homotopy cardinality = a count, not the radius; [CC2023]);
tropical/char-1 (`q→1`); Borger–Witt (finite-prime-indexed, no `ψ_∞`; [Bo]); monoid/Deitmar–Soulé (valuation
continuum; [De],[So]); Tate-twist period (`2π`, transcendental); global/product-formula (the audit edge).
**Degeneration:** the archimedean Fargues–Fontaine/twistor curve ([FF2018]; [VZ2024]; [CC2026]) has residue
field `ℂ`, `Gal(ℂ/ℝ)` of modulus 1, slope `½` — the reality, no scale; the `p`-adic FF carries `q` only by
*importing* `Spec 𝔽_p` via Witt vectors, and `ℝ` has none to import. (Detail: `research/f1-construction.md`,
`research/construction/F1-*.md`, `CN-*.md`.)

## 7. Scope, consequences, honest status

**Proven.** Theorem A and Proposition A3 are theorems (standard inputs). The reduction `RH⟺F†=F̄` and the
count/radius decoupling are constructive and validated on the function-field anchor.

**Theorem-shaped (not one general proof).** Theorem B is established for the strongest structures (computed
witnesses) and argued by exhaustion across the rest; its content is the common mechanism (off-line
consistency; positivity always external).

**Not claimed.** We neither prove nor disprove RH. Theorem A is *not* undecidability — it is the precise
limit of one strategy. That the char-0/char-`p` divide obstructs RH is the founding intuition of the
`𝔽₁`-program; the contribution here is its **formalization as a contradiction** plus the **exhaustion**.

**Consequence.** If RH is provable, the proof cannot route through a finite ground at `∞` (closed by Theorem
A). RH must be approached on the archimedean/char-0 side — analytic number theory, the explicit formula, de
Branges / Hilbert–Pólya *as analysis* (a self-adjoint operator built without an underlying finite-ground
geometry) — or by a new foundation reconceiving *archimedean ≡ characteristic 0*, which no current framework
achieves.

**One line.** Over function fields RH is a theorem because the finite ground is present; over `ℚ` the
geometric strategy is foreclosed because the finite ground at `∞` is not missing but *forbidden*
(*archimedean ≡ characteristic 0*), and the positivity RH needs is, in every coherence structure, an external
input only a finite ground supplies.

---

## References

- [O1916] A. Ostrowski, *Über einige Lösungen der Funktionalgleichung φ(x)φ(y)=φ(xy)*, Acta Math. 41 (1916).
- [Ne1999] J. Neukirch, *Algebraic Number Theory*, Springer (1999), II §3.
- [Ca1986] J.W.S. Cassels, *Local Fields*, LMS (1986).
- [W1948] A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent* (1948).
- [De1980] P. Deligne, *La conjecture de Weil II*, Publ. IHÉS 52 (1980).
- [DM1982] P. Deligne, J. Milne, *Tannakian Categories*, in *Hodge Cycles, Motives, and Shimura Varieties*, LNM 900 (1982).
- [DR1989] S. Doplicher, J. Roberts, *A new duality theory for compact groups*, Invent. Math. 98 (1989).
- [BBT2022] B. Bakker, Y. Brunebarbe, J. Tsimerman, *o-minimal GAGA and a conjecture of Griffiths*, Invent. Math. (2022); also Y. Peterzil, S. Starchenko, definable complex analysis.
- [vdD1998] L. van den Dries, *Tame Topology and o-minimal Structures*, LMS Lecture Notes 248 (1998).
- [BC1995] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions...*, Selecta Math. (1995).
- [CC2009] A. Connes, C. Consani, *Characteristic 1, entropy and the absolute point* / arXiv:0911.3537, §2.6.
- [L] P. Lescot, *Algèbre absolue* (characteristic one).
- [CC2023] A. Connes, C. Consani, *Riemann–Roch for `\overline{Spec ℤ}` / over the sphere spectrum* (2023).
- [CC2026] A. Connes, C. Consani, *`Jac(\overline{Spec ℤ})` and the circles `ℝ/(log p)ℤ`* (2026); as located in the literature search — to be verified against the published reference.
- [FF2018] L. Fargues, J.-M. Fontaine, *Courbes et fibrés vectoriels en théorie de Hodge p-adique*, Astérisque 406 (2018).
- [VZ2024] E. Viehmann et al., the twistor `ℙ¹` / archimedean Fargues–Fontaine analogue (2024); as located in the literature search.
- [Bo] J. Borger, *Λ-rings and the field with one element*.
- [De],[So] A. Deitmar, *Schemes over `𝔽₁`*; C. Soulé, *Les variétés sur le corps à un élément*.

*Recent references ([CC2026],[VZ2024]) were located via literature search during the program and are cited by
description; their exact bibliographic data should be verified before external use.*
