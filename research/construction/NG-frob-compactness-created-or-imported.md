# NG candidate 2 (Frobenius-first / Tannakian reconstruction) — compactness CREATED or IMPORTED?

**Charter.** `research/new-geometry-program.md`, candidate (2): take the **Frobenius as primitive** (an
abstract invertible self-map `F` with the explicit-formula Lefschetz trace and `F·F†=[q]`) and
*reconstruct* the space Tannakian-style as `Rep(⟨F⟩_Zar)` — the rep category of the algebraic (motivic
Galois / Sato–Tate) group `⟨F⟩` it generates. This is **the one candidate that tries to CREATE the finite
spectrum** rather than import it (candidate 1, o-minimal, was NOGO_BLUEPRINT: properness always an INPUT).

**The decisive binary (this pass).** Tannakian / finite-dim structure gives **Step A** (duality, finiteness,
the functional equation). **Step B** = the radius `|α|=√q` = `F†=F̄` = **the Frobenius is UNITARY** = **the
motivic Galois / Sato–Tate group is COMPACT** = **the category is POLARIZABLE** (admits a positive fiber
functor). Question: does Frobenius-first reconstruction **FORCE** compactness/polarizability from
*consistency*, or is it **IMPORTED** (assumed)?

Computation: `scripts/numerics/witness/frob_tannakian_compactness.py` (`[BUILT] [computed]`), cross-checked
against `rosati_circularity_skeptic.py` (re-run, confirmed). `q=7`.

---

## 1. Step A (rigidity / duality / FE) is FREE at every radius — confirmed

For an invertible `F` on `V=ℂ^d`, the rigid Tannakian data are automatic and **radius-independent**:
- `V**=V` (finite-dim reflexive); the dual action on `V*` is the contragredient `(F⁻¹)ᵀ`, with eigenvalues
  `1/α` (verified `dual eigenvalues = 1/α` True on every case);
- the **FE / perfect pairing** `V⊗V → det = [q]` sends `α ↔ det/α` — a perfect Poincaré pairing that
  **exists at any radius**.

Computed for ON-LINE (`r=√q`) and both OFF-LINE cases (`r=1.3√q`, `r=0.6√q`): Step A holds identically.
**Step A is FREE — supplied by the rigid Tannakian structure with no radius input. PASS.** (This matches the
program-wide finding: Step A = the FE = condensed/six-functor duality, holds at every radius; `PP-*`, M-pass.)

## 2. The reconstruction is CONSISTENT off-line — compactness is NOT forced

A **neutral Tannakian category over `ℂ` is exactly `Rep(G)` for an affine group scheme `G`** (Deligne–Milne,
*Tannakian Categories*, Thm 2.11) — a rigid abelian tensor category with a fiber functor. For **any**
invertible `F`, `G := ⟨F⟩_Zar` (the Zariski closure of `{Fⁿ}` in `GL(V)`) is a perfectly good affine
algebraic group, and `Rep(⟨F⟩_Zar)` is a perfectly good neutral Tannakian category. **Off-line is not
inconsistent — it just produces a different (non-compact) `G`.** Verified computationally that the
reconstruction *closes* off-line:
- tensor powers `V^{⊗k}` have **finite spectra** (`|spec V^{⊗2}|=4`, …) at any radius;
- the **Lefschetz / explicit-formula traces** `Tr(Fⁿ)` are finite & well-defined off-line
  (e.g. off-line `r=1.3√q`: `Tr(Fⁿ)=[5.26, 4.02, −41.08, −263.7, −901.5]`);
- duals + evaluation/coevaluation exist ⇒ **rigid**.

So **`Rep(⟨F⟩_Zar)` is a consistent rigid tensor category for OFF-LINE `F`.** The off-line datum generates a
genuine Tannakian reconstruction. **No consistency/coherence condition is violated.**

## 3. Step B (compactness / polarizability) holds ONLY on-line — IMPORTED

The Sato–Tate-normalized Frobenius `F/√q` has eigenvalue moduli `|α|/√q`. The normalized closure
`⟨F/√q⟩_Zar` is **compact (real points)** iff those moduli `=1`, i.e. **iff `|α|=√q` (on-line)**. Equivalently
`F/√q` admits an **invariant positive-definite Hermitian form** (a polarization / unitary fiber functor) iff
on-line. Computed:

| case | `|α|` | on-line | Sato–Tate closure COMPACT | invariant pos-def `H` (polarizable) |
|---|---|---|---|---|
| ON-LINE `r=√q` | 2.6458 | yes | **True** | **True** |
| OFF-LINE `r=1.3√q` | 3.4395 | no | **False** | **False** |
| OFF-LINE `r=0.6√q` | 1.5875 | no | **False** | **False** |

An off-unit-circle semisimple map preserves **no** positive-definite Hermitian form (it has an
expanding/contracting eigendirection); equivalently a `𝔾_m` factor of ratio `|α|/√q` survives in the
normalized closure. **Polarizability / compactness is an EXTRA positive structure (a chosen positive fiber
functor / a Hodge-type polarization with Deligne's sesquilinear positivity), holding only on-line, NOT
implied by — and not forced by — rigidity (Step A).** This is exactly Deligne's notion of a *polarization* as
an additional positivity datum on a Tannakian category, not part of the rigid structure.

**Cross-check (Rosati skeptic, `rosati_circularity_skeptic.py`, re-run):** an off-circle conjugate pair admits
a **positive Rosati polarization** (`H` pos-def True, Rosati form pos-def True) for **every** radius, and
`F·F† = r² = |α|²`, the **self-referential degree** — never the externally prescribed `q` (off-circle:
`F·F† = 11.83, 3.43, 28.0` for `r=1.3√q, 0.7√q, 2.0√q`; `==q? False`). The positivity sails straight through
off-line eigenvalues. `F·F†=[deg]` is a **free tautology** relative to `F`'s own degree; pinning that degree
to an independent `q` (= the radius) is **external**.

## 4. The circularity trap — positing a unitary `F` = positing RH

The only way Frobenius-first forces Step B is to **posit** at the outset that `F` is unitary / has real
spectrum / has all eigenvalues on `|α|=√q` — but that is **positing the radius = positing RH**, circular. The
integrality reading (`rosati_circularity_skeptic.py` part C) makes the circularity exact: an algebraic-integer
endomorphism `α` of an AV satisfies `|α|²=N(α)=deg` **automatically**, but `deg` is `α`'s **own** norm read
off `α`, not an independently given `q`. The circle `|α|=√(deg)` is forced **relative to the wrong
(self-referential) degree**; to anchor it to the arithmetic `q` you must **declare which circle is critical** —
an external datum, the imported finite ground.

## 5. DH falsification

The Frobenius-first reconstruction takes `F` as primitive. **Davenport–Heilbronn has no Euler product ⇒ no
Satake/Frobenius datum ⇒ no `F` ⇒ no input to the reconstruction** (the same type-level vacuity as the
purity-functor `LocFac`-empty finding, `radius_functor.py`/`purity_carrier.py`). So the candidate "fails to
exist for DH" only in the trivial input-empty sense; it draws **no radius distinction** between ζ and DH —
because the radius is never produced from the inside. **DH: FAIL** (Step-B-blind, exactly as candidate 1).

## 6. VERDICT — NOGO_EVIDENCE (compactness IMPORTED)

> **Frobenius-first reconstruction gives Step A FREE (rigidity/duality/FE at every radius) but does NOT
> create Step B.** Off-line spectrum generates a **fully consistent non-polarizable rigid Tannakian category**
> `Rep(⟨F⟩_Zar)` with a non-compact motivic Galois / Sato–Tate group. **Compactness / polarizability (the
> radius `|α|=√q = F†=F̄`) is the EXTRA positive fiber functor — the audit-wall positivity, external —
> IMPORTED (over `𝔽_q` literally via Weil II / Deligne purity), not forced by any consistency, coherence,
> rigidity, or trace condition of the reconstruction.** Positing a unitary / real-spectrum Frobenius *is*
> positing RH (circular); `F·F†=[deg]` forces the radius only against `F`'s self-referential degree, never an
> independent `q`. **This is the SECOND instance of the geometric no-go: the finite-spectrum-FIRST candidate
> imports the radius exactly where it claimed to create it.**

`radius_created_or_imported = IMPORTED`. The blueprint is confirmed twice (o-minimal: properness imported;
Frobenius-first: polarizability/compactness imported). The geometric no-go conjecture survives: **every
purity-forcing geometry imports a finite ground; the Tannakian reconstruction creates the finite *category*
but not the *compact* (polarized) structure that is the radius.**

## 7. Honest next step

Close Frobenius-first as a Step-B route (terminus: polarizability is Deligne-positivity, an external datum;
the Tannakian rigid structure is radius-blind). The residue is unchanged and now sharper: the missing object
`ψ_∞` is precisely **a canonical *positive* fiber functor on the archimedean Frobenius category** — a
polarization that `𝔽_q` gets from Weil II and `ℤ` lacks at `∞`. Proceed to candidate (3) (symmetric-monoidal
archimedean motives with polarization positivity as a *coherence theorem*) carrying the explicit warning:
candidates 1 and 2 both failed at exactly the positivity/polarization step — test (3) by whether the
coherence theorem produces the *positive* fiber functor **without** assuming a metric/weight, or merely
re-imports it.

---

### Numerics this session

- `frob_tannakian_compactness.py`: Step A True all radii; off-line `Rep(⟨F⟩_Zar)` consistent (finite spectra,
  well-defined `Tr(Fⁿ)`); Sato–Tate closure compact / polarizable **True on-line, False both off-line**.
- `rosati_circularity_skeptic.py` (re-run): off-circle admits positive Rosati polarization at every radius;
  `F·F† = r² = |α|² ≠ q` off-circle (`11.83, 3.43, 28.0`); integrality forces `|α|=√(deg)` = tautology.

### Sources

- Deligne–Milne, *Tannakian Categories* (jmilne.org/math/xnotes/tc2022.pdf): neutral Tannakian = rigid
  abelian ⊗-cat with a fiber functor = `Rep(G)`, `G` an affine group scheme (Thm 2.11); **polarization** = a
  compatible family of sesquilinear forms with **positivity** = an EXTRA structure, not part of rigidity.
- Tannakian formalism (en.wikipedia.org/wiki/Tannakian_formalism): the fiber functor / Galois-group
  reconstruction; `Rep(G)` for any affine `G`.
