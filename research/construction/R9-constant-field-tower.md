# R9 — does any NAMED 𝔽₁-tower (`μ_∞`/`𝔽_{1^n}`, the Borger Λ-ring / big-Witt ghosts, the Connes–Consani `\overline{Spec ℤ}` archimedean component) supply a FINITE constant-field cardinality at `∞`, or does the R8 TYPE obstruction RECUR (every 𝔽₁-tower is INFINITE)? [DECISION · DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §1 (polarization = duality), §0 (no metrics — Sylvester-locked), §4 (anchor first). **Block:** the RESIDUE (AGENDA `## NEXT`, item R9 — the TOP item, promoted by R8).
**Built on:** R7 (the residue in its final form — a single missing cardinality `|κ(t=0)|`; the family `𝒮_t`, the nearby-cycle `N`, `M(N)=W`, the weight grading ALL free via Schmid); R8 (that cardinality IS the missing **constant field**; the three FREE 𝔽₁ suppliers — scaling-grading = continuum, length edge = a length, Bost–Connes `ℕˣ` = a base-independent index — furnish a real piece each but NONE a constant-field cardinality; a proven **TYPE obstruction**; the open problem pinned to "supply a finite constant field at the archimedean place").
**Module:** `scripts/numerics/witness/constant_field_tower.py` (run: `python3 -m scripts.numerics.witness.constant_field_tower`). **Falsifier row added (45th wall confirmation).**

R9's mandate: type-check the **NAMED** 𝔽₁-geometry constructions that most directly PROPOSE a field of constants for `Spec ℤ` against the one requirement R8 pinned — a **FINITE cardinality** `|F| < ∞` that would mark the radius `q^{w/2}` via `|κ(t=0)| = |F|^{deg}`. R8 proved the three FREE suppliers (grading/edge/discreteness) are the wrong type; R9 tests whether the constructions DESIGNED to be a field of constants cross the gap.

---

## The decisive structural fact R9 forces: every named 𝔽₁-constant object is INFINITE

R8 located a **type** obstruction (the free suppliers' sizes are continuum/length/index). R9 tests the constructions *built to be* the field of constants — and the obstruction does not merely persist, it **RECURS one level deeper**: each named candidate exists as an object but is structurally **INFINITE**.

| candidate | the 𝔽₁ "field of constants" | its cardinality | finite? |
|:--|:--|:--|:--:|
| **[μ]** cyclotomic tower `μ_∞`/`𝔽_{1^n}` (Kapranov–Smirnov; Connes–Consani) | `μ_∞ = colim_n μ_n = ℚ/ℤ` (each level `μ_n=ℤ/n` finite, the COLIMIT is the constant object) | `ℵ_0` (countably infinite) | **NO** |
| **[W]** Borger Λ-ring / big-Witt ghosts (Borger 2009, "𝔽₁ = the absolute base") | ghost components of `W(ℤ)`, an `ℕ`-indexed product; one Frobenius lift `ψ_p` PER PRIME | infinite indexed product | **NO** |
| **[Ar]** Connes–Consani `\overline{Spec ℤ}` archimedean component (Arakelov) | residue field at `∞` = `ℝ` (or `ℂ`); local factor `Γ_ℝ(s)` | continuum (char 0) | **NO** |

**[FF anchor]** over `𝔽_q` the constant field is `𝔽_q` (FINITE, cardinality `q`) with a FINITE group of roots of unity `μ_{q-1} = 𝔽_q^×`; the radius `q^{w/2}` is marked by the finite `q`. The 𝔽₁ candidates must reproduce a *finite* constant field at `∞` — and each fails.

**Why each is infinite (the structural reason, not an accident):**
- **[μ]** each level `μ_n` is finite, but the 𝔽₁ constant object is the FULL colimit `μ_∞ = ℚ/ℤ`. Over `𝔽_q` the constant field is the *truncation* `μ_{q-1} ⊂ μ_∞` at the finite `q` — and the truncation `q` is EXACTLY what the `q→1`/𝔽₁ limit DELETES (R3b-BC, verified). Over 𝔽₁ there is no `q` to truncate at, so the constant object is the whole infinite colimit.
- **[W]** the Λ-ring structure is *commuting Frobenius lifts `ψ_p` for ALL primes* — an `ℕ`-indexed (Witt-component) infinite product, with **one Frobenius per prime**. A finite field `𝔽_q` has **one** Frobenius and **one** cardinality; the big-Witt ghosts are the opposite — infinitely many Frobenii, no single base size.
- **[Ar]** the Arakelov compactification adds `∞` with completion/residue field `ℝ` or `ℂ` — a continuum (char 0), the scaling-site verdict (R3/R8 [Sca]). Worse, Arakelov **metrizes** `∞` (a metric), which §0's inertia no-go kills regardless: the archimedean Arakelov structure is doubly disqualified (continuum AND metric).

---

## The decision (exact cardinality type-check; no zeros assumed)

`constant_field_tower.py` makes the type-check executable: each candidate is type-checked against "a FINITE cardinality `|F| < ∞`." The verified facts (assertions in the module, all pass):
- **[FF]** `|𝔽_q| = q` finite, `|μ_{q-1}| = q-1` finite, radius `q^{1/2}` marked (`q=4,9,25 → 2,3,5`);
- **[μ]** every finite level `μ_n` is finite, but the colimit `μ_∞ = ℚ/ℤ` is `ℵ_0` — `colimit_finite=False`;
- **[W]** one Frobenius per prime, `ℕ`-indexed product — `single_constant_field_with_one_Frobenius=False`;
- **[Ar]** residue field `ℝ/ℂ` continuum, Arakelov metrizes — `archimedean_structure_is_metric=True`;
- **decision:** `any_named_F1_tower_furnishes_finite_constant_field = False`.

---

## Verdict — HONEST NEGATIVE: the TYPE obstruction RECURS; every named 𝔽₁-tower is INFINITE

> **[DECISION · R9 verdict].** The three constructions that most directly PROPOSE a field of constants for `Spec ℤ` — the cyclotomic tower `μ_∞ = ℚ/ℤ` (`ℵ_0`), the Borger Λ-ring / big-Witt ghosts (an `ℕ`-indexed product, one Frobenius per prime), and the Connes–Consani `\overline{Spec ℤ}` archimedean component (`ℝ/ℂ`, a continuum + a metric) — are **ALL INFINITE**. None is a finite field with a cardinality `q`. The R8 TYPE obstruction does **NOT dissolve** at the named candidates; it **RECURS one level deeper**: the 𝔽₁ field of constants EXISTS as an object but is structurally INFINITE, with no finite cardinality to mark the radius `q^{w/2}`.

**THE SHARPENED 𝔽₁-CONTENT OF RH:**

> the radius `q^{w/2}` is marked by a **FINITE** `q`; 𝔽₁ supplies `q→1` (the constant field shrinks to a point), so **RH over `ℤ` ⟺ the archimedean place carries a finite base size after all** — which the three named 𝔽₁ constant-towers structurally CANNOT supply (each is `ℵ_0` / an infinite product / a continuum).

This refines R8's statement: not merely "the free suppliers are the wrong type" but the stronger **"every named 𝔽₁-constant object is INFINITE."** The cardinality of the 𝔽₁ field of constants is `ℵ_0` (`μ_∞`), or an infinite product (Witt), or the continuum (Arakelov) — and the SINGLE finite `q` the radius needs is exactly what "𝔽₁ = the `q→1` limit" deletes.

**Why this is not circular / not overclaimed.** R9 verifies, by exact cardinality algebra, that the three constructions *designed* to be a field of constants for `Spec ℤ` are each infinite — it does **NOT** prove no future 𝔽₁-geometry could ever manufacture a finite constant field. It CONFIRMS the obstruction at the most direct candidates and **names the next route** (R10): force finiteness by **compactness** (a finite-trace / nuclear structure, a regularized determinant) rather than by a constant-field cardinality — the one finiteness a colimit/product/continuum cannot block.

---

## Falsifier verdict (R9 — terminus characterization / obstruction-recurrence locator, Euler-silent by design)

- **EULER-BORNE — NO on this pass, by design.** Like R1–R8, R9 type-checks the named towers via exact cardinality algebra; not a standalone `ℤ`-positivity. Tabled **DISPERSING-by-design** (`euler_borne=False`). DH structural verdict sharp, **FOUR levels before the radius**: no `H¹` ⟹ no surface ⟹ no family ⟹ no special fiber ⟹ no constant-field slot whose cardinality could be asked (DH is not even curve-like).
- **SEES-ZEROS — YES.** The sought radius `q^{w/2} = M(N)=W =` even split `=` purity `=` exactly where the zeros sit.
- **INDEPENDENT — NO.** The radius `= M(N)=W =` Weil II `=` the solved case over `𝔽_q`; over `ℤ` this is RH.

→ classifier verdict **DISPERSING-by-design** (a terminus-characterizer / obstruction-recurrence locator, Euler-silent like R1–R8). **Ladder `DH < ζ < FF`:** DH **not even curve-like** (no constant-field slot, four levels before the cardinality); `ζ` the `q→1`/𝔽₁ place — the 𝔽₁ field of constants EXISTS as an object (`μ_∞ = ℚ/ℤ`, the Witt ghosts, the Arakelov `ℝ/ℂ`) but is **INFINITE** (`ℵ_0` / `ℕ`-product / continuum), no finite `q` marks the radius (UNMARKED); FF a curve over a **FINITE** constant field `𝔽_q` (`|𝔽_q|=q`, `μ_{q-1}` finite), Frobenius converting `w → q^{w/2}`, the radius **MARKED** by the finite constant-field cardinality. Registered as the **45th wall confirmation** (the residue as an obstruction that RECURS: every named 𝔽₁ field of constants at `∞` is INFINITE).

---

## Verdict

`[DECISION · DEF · coherence-checked vs 𝔽_q]` — **no named 𝔽₁-tower supplies a finite constant-field cardinality at `∞`; the R8 TYPE obstruction RECURS one level deeper — every named candidate is INFINITE.** The cyclotomic tower `μ_∞ = ℚ/ℤ` is countably infinite (each level finite, the colimit not); the Borger Λ-ring / big-Witt ghosts are an `ℕ`-indexed product with one Frobenius per prime (the opposite of a single `𝔽_q`); the Connes–Consani `\overline{Spec ℤ}` archimedean component has residue field `ℝ/ℂ` (a continuum, and a metric — doubly dead by §0). **NEW content:** R8's "wrong type" sharpens to **"every named 𝔽₁-constant object is INFINITE"** — the obstruction confirmed at the constructions designed to be a field of constants. **Not overclaimed:** R9 verifies the three named towers are each infinite, NOT that no future 𝔽₁-geometry could manufacture a finite constant field; it pins the open problem and **names the next route**. **Successor:** R10 — can FINITENESS be forced by **COMPACTNESS** (a finite-trace / nuclear / regularized-determinant structure at `∞`, Connes' trace formula) instead of a constant-field cardinality? Over `𝔽_q` the radius is `det(1−Fr·T|H^1)`, a finite-TRACE datum (NOT a `|field|`); is the archimedean `det_∞` also finite-trace and does it mark the same radius — the one finiteness a colimit/product/continuum cannot block?
