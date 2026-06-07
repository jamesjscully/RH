# NG candidate 2 — Frobenius-first / Tannakian reconstruction: NOGO-DIRECTION [judge]

**Charter.** `research/new-geometry-program.md` candidate (2): take the **Frobenius as primitive** (an
abstract self-map with the explicit-formula Lefschetz trace and the scalar relation `F·F† = [q]`) and
*define* the space as what it coherently acts on (Tannaka for a dynamical datum). The bet: the radius
`|α|=√q = F†=F̄` = purity = **Step B** is forced by **reconstruction-coherence**, not imposed. This is the
ONE approach that tries to **CREATE** the finite spectrum rather than **IMPORT** it — hence the precise
test of whether the geometric no-go (candidate 1, NOGO_BLUEPRINT) is FALSE.

**Angle taken.** The Grothendieck move: attempt to PROVE non-existence (the no-go), and watch where the
proof fails. Claim under test: *every Frobenius-first reconstruction either (a) gives only Step A
(finite-dim/duality) and imports Step B (the radius/compactness), or (b) imports the finite ground by
POSITING the finite (unitary/real) spectrum — i.e. NO reconstruction CREATES the radius.*

---

## 1. The forcing-mechanism survey inside Tannakian reconstruction

A Tannakian category `T` over a field `k`, **rigid** (every object dualizable) + a **fiber functor**
`ω: T → Vec_k`, reconstructs an affine group scheme `G = Aut⊗(ω)` with `T ≃ Rep(G)` (Deligne–Milne,
*Tannakian Categories*; Saavedra Rivano). Map the mechanisms onto the Step A / Step B ledger:

| Mechanism | What it gives | Step |
|---|---|---|
| **Rigidity** (duals exist, `D∘D=id`) | the duality pairing `α ↔ q/α`, the FE | **A (free)** |
| **Existence of a fiber functor** `ω` | finite-dimensionality, `G = Aut⊗(ω)` affine | **A (free)** |
| **A POLARIZED / positive fiber functor** (a `ℝ`-structure with compatible **positive-definite** sesquilinear forms = a polarization, Deligne–Milne §4) | `G` is **reductive** / has a **COMPACT real form** = the spectrum is **unitary** = `|α|=√q` | **B (deep)** |

The literature is unambiguous on the third row (verified, web): *"the polarization forces the Tannakian
structure group to be reductive because it gives rise to a **compact mod center real form**"*; *"polarization
consists of compatible families of **sesquilinear forms having certain positivity properties** … this
positivity structure is what drives the compactness."* The motivic Galois group is reductive **because the
absolute Hodge structure is polarized** (Deligne, *Hodge Cycles*; the category is reductive *iff* polarized).

> **The polarized/positive fiber functor is the ONLY route to Step B inside Tannakian reconstruction.**
> Rigidity → duality (Step A). A fiber functor → finite-dim (Step A). **Compactness/the radius enters
> exactly and only through POSITIVITY of the polarization** — and positivity is the program's audit-wall
> positivity, an **external input** (an `ℝ`-structure with a sign condition, not a categorical coherence).

This is the same atom as every instrument in `the-complete-account.md`: **Step A free, Step B = a
positive/polarized structure = imported.** Tannaka does not change the wall; it *names* it as the
positivity of the fiber functor.

---

## 2. The decisive skeptic witness — a CONSISTENT off-line Frobenius-first datum

If the no-go is right, positing `F` with `F·F†=[q]` and reconstructing must leave the radius FREE: there
must exist a **consistent, rigid, self-dual Tannakian datum with off-circle eigenvalues** (a category that
is rigid but **not polarizable**). Built it [computed]:

Take the weight-1 fibre `H¹ = ⟨e₁,e₂⟩`, the duality `D` = the perfect Poincaré pairing valued in
`ℚ(−1) = q` (anti-diagonal swap `α ↔ q/α`), and `F = diag(a, q/a)`. Then:

- **Step A is forced FREE for every `a`:** `det F = q` always; the char-poly `x² − (a+q/a)x + q` has product
  of roots `= q` — the functional equation / perfect pairing holds at **every** radius. The rigid self-dual
  structure manufactures the duality `F·F†=[q]` with NO constraint on `|a|`.
- **Step B is an EXTRA, unforced condition:** `|α|=√q ⟺ |a|²=q ⟺ a = q/ā ⟺ F†=F̄` (arithmetic adjoint =
  conjugate). Tested three data, all consistent rigid self-dual Tannakian objects:
  - `a=√7`: `|eig| = {2.6458, 2.6458}` — on-circle (radius marked). ✔
  - `a=5`:  `det=7` but `|eig| = {5, 1.4}` — **OFF-circle, fully consistent, NOT polarizable.**
  - `a=0.99+2i`: `det=7`, `|eig| = {2.23, 3.14}` — **off-circle, consistent.**

> **Off-line generates a CONSISTENT non-polarizable Tannakian category.** The rigid + fiber-functor
> structure (Step A) sails straight through it. The positive polarization that would force `|a|²=q`
> (Step B) is **the external sign condition** — exactly the audit-wall positivity, never a coherence
> consequence. Positing a *unitary / real-spectrum* `F` = positing `|a|²=q` = **positing RH = circular.**

`scripts/numerics/witness/` discipline reproduced: `det F = q` (the pairing) is the RH-SILENT Step A
present at every radius; the radius is the SEES-ZEROS content the positivity must supply externally.

---

## 3. Where could the no-go proof FAIL? — the *-autonomous / self-dual-forcing probe (the gap for candidate 3)

The only way Frobenius-first could CREATE Step B is if a **categorical structure forced a polarized fiber
functor from consistency alone** — positivity as a **coherence theorem**, not an axiom. Candidates:

- **Rigid `⟹` reductive?** NO. Rigidity gives duals (Step A); the reconstructed `G` of the off-line datum
  above is a torus `𝔾_m` (acting by `diag(a, q/a)`), perfectly rigid, **non-compact**, non-polarized. Duals
  ≠ positive duals.
- **A `*`-autonomous / self-dual structure forcing positivity?** This is the precise gap. A `*`-autonomous
  category has a dualizing object and a self-duality, but the dual pairing is **non-degenerate, not
  positive-definite**. Self-duality `D∘D=id` is the FE (Step A); **positivity of `D` (the pairing is a
  *positive* Hermitian form) is strictly more** and is NOT a coherence consequence of `*`-autonomy
  (the off-line witness is self-dual yet non-positive). Compact closed / `*`-autonomous structure forces
  *trace* and *dimension* (Step A counts), never a *sign*.
- **A `C*`/Hilbert (positive) symmetric-monoidal structure** (Doplicher–Roberts: a symmetric tensor
  `C*`-category with conjugates reconstructs a **compact** group) — this DOES force compactness, **but only
  because the `C*`/Hilbert structure has positivity built into the norm axiom** (`‖a*a‖=‖a‖²`, a *positive*
  inner product). That is **IMPORTING** the positive fiber functor as the ambient axiom, not deriving it.
  Doplicher–Roberts is precisely "compactness from a *positive* (`C*`) structure" — the audit wall in
  categorical clothing. (Candidate 3 = "symmetric-monoidal archimedean motives with polarization a coherence
  theorem" lives exactly here, and inherits exactly this circularity: the coherence theorem needs a positive
  ambient structure.)

> **The proof of "always imported" does NOT fail.** Every categorical route to Step B (reductive form,
> compact form, `C*`/Doplicher–Roberts) requires a **positivity already present in the ambient structure**
> (a polarization, a Hilbert inner product, a `C*`-norm). Self-duality / `*`-autonomy / rigidity give the
> *pairing* and the *FE* (Step A) with no sign; the **sign is the import.** There is no categorical
> coherence theorem that manufactures positive-definiteness from a non-degenerate self-duality. This is the
> sharpened restatement of the audit wall as a no-go.

---

## 4. The anchor `𝔽_q` — Sato–Tate compactness is Weil-II imported (NOT free)

The Frobenius-first datum over `𝔽_q` is exactly the Sato–Tate / algebraic-Sato–Tate group construction.
Verified (web, Fité–Kedlaya–Sutherland; algebraic Sato–Tate, arXiv:1109.4449): the Sato–Tate group `ST(A)`
is defined as a **maximal compact subgroup** of the (Tannakian, motivic) group `TL(A)(ℂ)`, and the
Frobenius enters as the **NORMALIZED** `g' = q^{−1/2} g_p`, which *"belongs to a group with eigenvalues of
norm 1, and therefore belongs to a conjugate of the Sato–Tate group."*

> The eigenvalues-of-norm-1 property — i.e. `|q^{−1/2}α| = 1` ⟺ `|α|=√q` — is **exactly the Weil-II purity
> bound**, and it is the PREREQUISITE for `g'` to land in the maximal compact `ST`. The compact form is
> **downstream of `|α|=√q`, not upstream.** Sato–Tate compactness is **Weil II imported**: Deligne's purity
> is what makes the unitarized Frobenius land in a compact group; the Tannakian/motivic reconstruction
> supplies the *group* (Step A: a reductive `G`, duality, the Mumford–Tate / motivic Galois) but the
> **compactness of the relevant real form is conditioned on purity already holding.**

So on the anchor — the one place the radius is a *theorem* — the Frobenius-first reconstruction **imports**
the radius (Weil II → unitarized Frobenius → compact ST). It does not create it. This is the F_q
confirmation of the no-go direction: even where Step B is TRUE, the Tannakian machine receives it as input.

---

## 5. Falsify DH

Davenport–Heilbronn: no Euler product ⟹ no Frobenius datum ⟹ **no `F·F†=[q]` scalar**, no rigid self-dual
`H¹`, **no Tannakian object at all**. The Frobenius-first construction is **vacuous for DH** — it never
gets off the ground (there is no `F` to posit). `falsify.py` axis-1: a genuine geometry must FAIL to exist
for DH. Frobenius-first passes this gate **but only at the object-existence level (Step A)** — and that is
not the discriminator we need: a *radius-forcing* would be the content, and the off-line witness (§2) shows
the radius is NOT forced even when the object DOES exist (ζ-side). So the DH test is passed vacuously, while
the **radius remains free on the ζ-side** — the same pathology as candidate 1 (blind at Step B), now in
Tannakian form. **DH: FAILS to exist (correct), but the candidate is blind at the radius, so this is no-go
evidence, not a forcing.**

---

## 6. The sharpest version of the no-go (theorem-shaped)

> **Tannakian no-go (Step B = positivity = always an external input).** Let `(T, ω)` be a rigid Tannakian
> category with fiber functor reconstructing `G = Aut⊗(ω)` and a Frobenius datum `F` with `F·F†=[q]`. Then:
> rigidity and `ω` force **Step A** (finite-dim, duality, the FE `det F = q`) *intrinsically and for free*;
> but `|α|=√q` (**Step B**, `F†=F̄`, the compact/reductive real form) holds **iff** `ω` is **polarized
> (positive)**, and **positivity is not a coherence consequence** of rigidity, `*`-autonomy, or self-duality
> — there exist consistent rigid self-dual non-polarizable data with off-circle spectrum (§2). Hence **no
> Frobenius-first reconstruction CREATES the radius; the radius is the positivity of the fiber functor =
> the imported finite ground / the audit-wall positivity.** Positing a unitary/real-spectrum Frobenius =
> positing RH (circular).

The genuine gap (where one *could* hope candidate 3 escapes): a categorical structure that forces a
**positive** self-duality from consistency. The probe of §3 indicates this gap is **empty** — every known
compactness-from-category theorem (reductive-from-polarization, Doplicher–Roberts compact-from-`C*`) feeds
on a positivity already in the axioms. The honest residual for candidate 3 is precisely: *find a coherence
theorem that emits a sign from a non-degenerate (sign-free) self-duality.* None is known; the structure of
the proof suggests none exists (a non-degenerate form has no canonical sign).

---

## 7. Verdict

**NOGO_EVIDENCE.** Frobenius-first / Tannakian reconstruction gives **Step A free** (rigidity = duality;
fiber functor = finite-dim; `det F=q` = FE at every radius) and **imports Step B** (the radius = the
POSITIVE/polarized fiber functor = compact real form = audit-wall positivity, external). The decisive
witness: a **consistent rigid self-dual non-polarizable** Frobenius datum with **off-circle eigenvalues**
(`a=5`, `a=0.99+2i`, both `det=q`) — off-line generates a consistent non-polarizable category; the
positivity that would force `|α|=√q` is never a coherence consequence of rigidity / `*`-autonomy /
self-duality (only a `C*`/Hilbert/positive ambient structure forces compactness, and that IS the import).
**Anchor confirms it:** Sato–Tate compactness is Weil-II imported — the unitarized Frobenius is norm-1
*because* `|α|=√q` already holds. **DH:** the object fails to exist (no Euler product, no `F`), so passed
vacuously, but the candidate is **blind at the radius** even on the ζ-side. This is the **second instance
of the geometric no-go**: positing the Frobenius does NOT create the finite spectrum — the radius re-enters
as the positivity of the polarization, exactly the external input candidate 1 found as properness. The
no-go conjecture is **NOT refuted; it is reinforced**, with the wall now sharply named as
**positivity-of-the-fiber-functor is not a Tannakian coherence theorem.**

**Honest gap (candidate 3 blueprint):** the *only* unclosed door is a coherence theorem forcing a
**positive** self-duality from a sign-free non-degenerate one. The §3 analysis argues this door is closed
(no canonical sign on a non-degenerate form), but a full proof of "no such coherence theorem exists" is the
sharp open question. Candidate 3 (symmetric-monoidal archimedean motives, polarization-as-coherence) should
be tested *exactly* against this: does its claimed coherence theorem secretly assume a positive ambient
(`C*`/Hilbert) structure? If yes (expected), the no-go is a theorem.

---

### Numerics reproduced this session
- Self-dual Frobenius datum `F=diag(a,q/a)`, `q=7`: `det F = 7` for **all** `a` (Step A free); `|eig|=√7`
  only at `|a|²=q`. Off-line `a=5 → |eig|={5,1.4}`, `a=0.99+2i → |eig|={2.23,3.14}`: consistent,
  non-polarizable, `det=7`. (Step B = extra positivity, unforced.)
- Anchor: Sato–Tate `ST(A)` = maximal compact of `TL(A)(ℂ)`; normalized `g'=q^{−1/2}g` is norm-1 **because**
  `|α|=√q` (Weil II) — compactness imported. [web-verified: arXiv:1109.4449, Fité–Kedlaya]
