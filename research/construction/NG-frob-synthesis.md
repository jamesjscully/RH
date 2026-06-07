# NG synthesis — candidate 2: FROBENIUS-FIRST / Tannakian reconstruction [SYNTHESIS JUDGE]

**Charter.** `research/new-geometry-program.md` — SECOND candidate of a new geometry to force Step B
(the radius `|α|=√q = F†=F̄` = purity = compactness of the motivic Galois group / `F` unitary)
**archimedean-natively, without a finite ground**. This is **the explicit test of whether the geometric
no-go conjecture is FALSE**: candidate 2 is the one approach that tries to *CREATE* the finite spectrum
(posit the Frobenius, reconstruct the space Tannakian-style) rather than *import* it. Binary, stated in the
charter: does it FORCE `F·F†=[q]` from consistency (gap `P*` non-empty → new geometry, no-go FALSE), or
does positing the Frobenius *import* the finite ground (second instance of the no-go)?

Three independent angle-investigations were run:
1. **Frobenius-first / Tannakian reconstruction** (Deligne–Milne reconstruction; Connes–Marcolli motivic
   Galois `U*`; Connes adele-class-space spectral realization) — does reconstruction-*coherence* single out
   the polarized case?
2. **Off-line skeptic witness** (`frob_tannakian_compactness.py` + `rosati_circularity_skeptic.py`) — is the
   off-line spectrum INCONSISTENT (create) or does it generate a consistent non-polarizable category (import)?
3. **Grothendieck move** — attempt to PROVE "the radius is always imported," watch where the proof fails;
   isolate the one categorical structure that MIGHT force a polarized fiber functor (the blueprint for
   candidate 3).

**All three return the same verdict — `NOGO_EVIDENCE`, IMPORTED — by three independent routes, and the
sourcing is real.** This synthesis adjudicates and was checked against an independent re-run of the witness.

---

## 1. Is the Tannakian / Frobenius-first reconstruction GENUINE, and is Step A FREE? — YES and YES

**The reconstruction is real and is a living theorem.** Deligne–Milne (*Tannakian Categories*, Thm 2.11): a
neutral Tannakian category over `ℂ` — a rigid abelian `k`-linear symmetric-monoidal category with a fiber
functor — is exactly `Rep(G)` for an affine group scheme `G`. The Frobenius-first instance is REALIZED, not
aspirational: Connes–Marcolli reconstruct a **motivic Galois group `U* = U ⋊ 𝔾_m`** from equisingular flat
bundles; Connes' adele-class-space gives the zeros as the spectrum of a scaling/Frobenius-analogue with
Weil's explicit formula as a Lefschetz trace. For ANY invertible `F` on `V=ℂ^d`, `G := ⟨F⟩_Zar` (Zariski
closure of `{Fⁿ}` in `GL(V)`) is a perfectly good affine algebraic group and `Rep(⟨F⟩_Zar)` a perfectly good
neutral Tannakian category. **RECONSTRUCTION: REAL.**

**Step A (finite-dim / duality / FE) is FREE — supplied archimedean-natively with no finite ground.**
Rigidity manufactures Step A for free: every object of a rigid tensor category is dualizable
(`X → X^∨`, `D·D=id`, `dim = trace in End(1)=k`), and the fiber functor lands in **finite-dimensional** Vec.
Concretely [computed, re-run this session, `q=7`]:
- `V**=V` (reflexive); dual action `(F⁻¹)ᵀ` with eigenvalues `1/α` (`dual=1/α` True every case);
- perfect **FE pairing** `V⊗V → det = [q]` sending `α ↔ det/α` — exists **at any radius**.

Verified identically ON-LINE (`r=√q`) and BOTH OFF-LINE (`r=1.3√q`, `r=0.6√q`): Step A holds at every radius
with no radius input. **This is the candidate's GENUINE PROGRESS** — the cleanest derivation in the program of
the FE half (finite-dimensionality + perfect duality + `F·F†=[q]`), archimedean-native, no finite ground.
It matches the program-wide finding (Step A = the FE = condensed / six-functor duality, radius-blind).
**STEP A FREE: PASS.** But — Step A was never the residue.

## 2. THE BINARY — is Step B CREATED or IMPORTED? — IMPORTED, decisively

**The off-line spectrum is CONSISTENT, not inconsistent.** This is the load-bearing fact and it is the one
that decides the binary against "create." [computed, independently re-run this session]: for OFF-LINE `F`
the reconstruction *closes* —
- tensor powers `V^{⊗k}` have **finite spectra** at any radius;
- the Lefschetz / explicit-formula traces `Tr(Fⁿ)` are **finite & well-defined** off-line
  (`r=1.3√q`: `Tr(Fⁿ)=[5.26, 4.02, −41.08, −263.73, −901.53]`);
- duals + evaluation/coevaluation exist ⇒ **rigid**; `consistent rigid tensor cat = True` off-line.

So `Rep(⟨F⟩_Zar)` is a **consistent rigid Tannakian category for off-line `F`** — it is merely
**NON-polarizable / has a non-compact motivic Galois / Sato–Tate group** (a surviving `𝔾_m` factor of ratio
`|α|/√q`). **No rigidity, coherence, trace, fiber-functor, or `F·F†` condition is violated off-line.**

**Step B holds ONLY on-line, and it is an EXTRA positive structure:**

| case | `\|α\|` | on-line | Sato–Tate closure COMPACT | invariant pos-def `H` (polarizable) |
|---|---|---|---|---|
| ON-LINE `r=√q` | 2.6458 | yes | **True** | **True** |
| OFF-LINE `r=1.3√q` | 3.4395 | no | **False** | **False** |
| OFF-LINE `r=0.6√q` | 1.5875 | no | **False** | **False** |

The normalized closure `⟨F/√q⟩_Zar` is compact iff the moduli `=1` iff `|α|=√q`; equivalently `F/√q`
preserves a positive-definite Hermitian form iff on-line. An off-unit-circle semisimple map preserves **no**
positive-definite form (expanding/contracting eigendirection). **Polarizability / compactness — the radius
`|α|=√q = F†=F̄` — is a chosen positive fiber functor / Deligne's sesquilinear positivity, an EXTRA datum on
top of rigidity, NOT forced by any consistency or coherence condition of the reconstruction.**

**Reconstruction-coherence makes the WRONG group — the largest, not the polarized, one.** Angle 1's sourced
structural fact: the reconstructed motivic Galois group is the **UNIVERSAL / free** object on the tensor
datum — Connes–Marcolli's `U` is pro-unipotent with a **FREELY generated Lie algebra** (one generator per
positive degree), `𝔾_m`-action. A free pro-unipotent group carries **no** positivity / compactness /
unitarity constraint. Coherence produces the *largest* group consistent with the data; it does not single out
the polarized / reductive / compact case. The Tannakian category of **mixed** motives is perfectly consistent
**without** purity. Reconstruction is consistent for non-pure objects and for off-line spectra alike.

**The circularity trap (the program's reality-condition wall).** The only way Frobenius-first forces Step B
is to **posit** at the outset that `F` is unitary / has real spectrum / lies on `|α|=√q` — but that is
**positing the radius = positing RH**, circular. Angle 1 sharpens this on the Hilbert-space side: in Connes'
rapidly-decaying (non-positive) setting ALL zeros contribute as **resonances**, and RH ⟺ a positivity of the
Weil trace pairing that is **NOT automatic**; only the positive `L²` fiber functor selects critical-only
zeros, and *that* positivity IS the audit-wall positivity (RH ⟺ trace positivity = Weil/Li, CIRCULAR).
The integrality reading (`rosati_circularity_skeptic.py`, re-run) makes it exact: an algebraic-integer
endomorphism satisfies `|α|²=N(α)=deg` automatically, but `deg` is `α`'s **own** norm read off `α`, never an
independently given `q` (off-circle: `F·F† = 11.83, 3.43, 28.0 ≠ q`). `F·F†=[deg]` forces the circle only
**relative to `F`'s self-referential degree**; anchoring to the arithmetic `q` is the **external/imported**
datum.

**Anchor — compactness is Weil-II-imported.** Over `𝔽_q` the Frobenius DOES generate the Tannakian category
of motives with finite-dim `H¹` of rank `2g` — reconstruction reproduces the `𝔽_q` picture. But the modulus
`|α|=√q` (Sato–Tate compactness, reductive/polarized Galois group) is **Weil II** — an EXTRA theorem
(Rankin-squaring + monodromy of a degenerating family) imported INTO the category, not a coherence constraint
OF it. The algebraic Sato–Tate group `ST(A)` is *defined* as a maximal compact of `TL(A)(ℂ)` and the
Frobenius enters NORMALIZED `g' = q^{−1/2}g`, landing norm-1 precisely BECAUSE `|α|=√q` already holds.
**Compactness is downstream of purity, not upstream.** The analogy with `𝔽_q` HOLDS and lands on the no-go
side — the radius does not transfer.

**`radius_created_or_imported = IMPORTED`. Off-line spectrum = CONSISTENT non-polarizable category = the
import signature.** (If off-line had been INCONSISTENT — no Tannakian reconstruction at all — the no-go would
be FALSE. It is not: the reconstruction closes off-line.)

## 3. DH — FAILS in the NO-GO way (DH-blind at Step B)

Two readings, same verdict. (a) DH shares ζ's Γ-factor, FE, duality `D`, and the `F·F†=[q]` tautology, so the
Tannakian Step-A machinery and the resonance trace-formula apply to DH **verbatim** — the construction EXISTS
for DH with off-line resonances and draws **no z/DH distinction at the radius** (the difference lives entirely
in the imported positivity). (b) At the input-existence level DH has **no Euler product ⇒ no Satake/Frobenius
datum ⇒ no `F`** — "fails to exist for DH" only in the trivial input-empty sense (same type-level vacuity as
candidate 1 and the purity-functor `LocFac`-empty finding). Either way: **DH-blind at Step B = NOGO**, not a
healthy "fails to exist" gate. The radius is never produced from inside, so the candidate cannot tell ζ from
DH where it matters.

---

## 4. VERDICT — NOGO_EVIDENCE (the geometric no-go gains its SECOND instance)

> **Frobenius-first / Tannakian reconstruction is GENUINE and gives Step A FREE (rigidity = finite-dim +
> duality + FE = `F·F†=[q]` at every radius — the cleanest FE derivation in the program). But it does NOT
> CREATE Step B. The off-line spectrum generates a fully CONSISTENT non-polarizable rigid Tannakian category
> `Rep(⟨F⟩_Zar)` with a non-compact motivic Galois / Sato–Tate group. Compactness / polarizability — the
> radius `|α|=√q = F†=F̄` — is the EXTRA positive fiber functor = the audit-wall positivity, external,
> IMPORTED (over `𝔽_q` literally via Weil II / Deligne purity), never forced by any consistency, coherence,
> rigidity, or trace condition. Reconstruction-coherence makes the FREE/universal (pro-unipotent) group, not
> the polarized one. Positing a unitary / real-spectrum Frobenius IS positing RH (circular).**

This is **NOT a restatement of RH dressed up** — the anchor `det F = q` is recovered for every `a` without
importing the zeros; the circularity is *identified*, not hidden. It is a **second confirmed instance of the
geometric no-go**: candidate 1 (o-minimal) imports **properness**; candidate 2 (Frobenius-first) imports
**positivity / polarizability**. **Both CREATE Step A, both IMPORT Step B, at exactly the same wall.** The
no-go conjecture is **NOT falsified — it is reinforced.** The candidate creates the finite *category* but not
the *compact / polarized* structure that is the radius, exactly where it claimed to create it.

**The progress that is real:** Step A is now **provably free from rigidity** (verified at three radii). This
**isolates the residue** to a single point — Step B = **FIBER-FUNCTOR SELECTION = positivity = `F†=F̄`**.
Candidate 2 also proves the reconstruction **ADMITS a non-positive fiber functor** (the resonance / off-line
setting). So the only surviving escape is a **coherence theorem forcing the positive fiber functor to be
UNIQUE** — polarization as a categorical *theorem*, not an axiom.

---

## 5. THE EXACT FAILURE POINT OF THE NO-GO PROOF — blueprint for candidate 3

The Grothendieck move (angle 3) located the **one unclosed door**, and it is the precise pivot to candidate 3:

> **The no-go proof would become a theorem if one could show: NO categorical coherence theorem emits a SIGN
> (a positive self-duality) from a SIGN-FREE non-degenerate self-duality.** Rigidity / `*`-autonomy /
> self-duality give a non-degenerate pairing `V⊗V → 𝟙`, but a non-degenerate form **carries no canonical
> sign**; only a positive ambient structure (C\*/Hilbert/`L²`, a chosen positive fiber functor) forces
> compactness (Doplicher–Roberts: compact group reconstructed from a C\*/positivity structure;
> reductive-from-polarization). **That positivity IS the import.**

So the **categorical structure that MIGHT force Step B** — the single feature candidate 3 must supply, and the
exact place to audit it — is:

> **A CANONICAL POSITIVE (polarized) fiber functor produced as a COHERENCE THEOREM of a symmetric-monoidal
> category of archimedean motives — a forced unitary structure derived from `*`-autonomy / self-duality
> WITHOUT assuming a metric, a weight, or a C\*/Hilbert ambient.**

This is the sharpened statement of `ψ_∞`: not just "collapse the Γ-pole spectrum to a degree-`2g` char-poly"
(candidate 1's blueprint) but **"force the positive fiber functor to be UNIQUE."**

**The decisive test for candidate 3 (stated as a falsifiable audit):**
- Does the claimed coherence theorem produce the positive fiber functor **WITHOUT** secretly assuming a
  positive ambient (C\*/Hilbert/metric/weight)? If it re-imports a metric → **third instance of the no-go**,
  and the no-go becomes provable.
- The sharp open question — proving the no-go is a **theorem** — is exactly:
  **"No coherence theorem emits a sign from a sign-free non-degenerate self-duality."** Candidates 1 and 2
  both failed at this positivity/polarization step; if candidate 3's coherence theorem also silently assumes a
  positive ambient (expected, since a non-degenerate form has no canonical sign), then **Step B = positivity
  = always an external input** is upgraded from conjecture to theorem.

---

## 6. Honest next step — and is the no-go now provable?

**Close Frobenius-first as a Step-B route.** Terminus: polarizability = Deligne-positivity = a chosen
positive fiber functor = external; the rigid Tannakian structure is **radius-blind**; reconstruction-coherence
emits the free/universal group, not the polarized one. Do NOT seek a reconstruction-coherence route to the
radius — the off-line category is consistent, so coherence cannot exclude it.

**Proceed to candidate 3** (symmetric-monoidal archimedean motives, polarization as a coherence theorem)
carrying the **sharpened wall and the explicit warning**: candidates 1 AND 2 both failed at exactly the
positivity/polarization step (properness / polarizability). Test candidate 3 by the single audit above —
does the coherence theorem force a POSITIVE self-duality from a sign-free one *without* re-importing a
metric/weight/C\*-structure, or merely re-import it?

**Is the geometric no-go now provable?** **Two of three instances are in (properness imported; positivity
imported), and the failure has been compressed to a single, clean, candidate-independent statement** —
"no coherence theorem emits a sign from a sign-free non-degenerate self-duality." This is now a **precise,
checkable mathematical proposition**, not a heuristic. **The no-go is one instance from a theorem:** if
candidate 3's coherence theorem is shown to silently assume a positive ambient, the conjecture closes as
*RH is not forceable by a metric-free geometry — Step B is always an imported positivity*. The no-go is not
yet proven (candidate 3 is the last open door), but it is now **provable-shaped** and the door is named.

---

### Numerics reproduced this session (independent re-run of the witness)

- `frob_tannakian_compactness.py` (`q=7`): Step A (invertible / dual=1/α / perfect FE pairing) **True at all
  three radii**; off-line `Rep(⟨F⟩_Zar)` **consistent** (finite tensor spectra, well-defined
  `Tr(Fⁿ)`, duals close); Sato–Tate closure **COMPACT / polarizable True ON-LINE, False BOTH OFF-LINE**.
  → off-line consistent non-polarizable category → **COMPACTNESS IMPORTED → NOGO**.
- `rosati_circularity_skeptic.py` (re-run): off-circle admits positive Rosati polarization at **every** radius;
  `F·F† = r² = |α|² ≠ q` off-circle (`11.83, 3.43, 28.0`); integrality `|α|=√(deg)` = self-referential
  tautology, never an independent `q`.

### Sources
- Deligne–Milne, *Tannakian Categories* (Thm 2.11): neutral Tannakian = rigid abelian ⊗-cat + fiber functor
  = `Rep(G)`; **polarization** = compatible sesquilinear forms WITH positivity = an EXTRA structure.
- Connes–Marcolli, *Renormalization, the Riemann–Hilbert correspondence, and motivic Galois theory*:
  motivic Galois `U* = U ⋊ 𝔾_m`, `U` pro-unipotent with FREELY generated Lie algebra (one generator/degree).
- Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*: adele-class
  space, zeros as spectrum / resonances, Weil explicit formula = Lefschetz trace; RH ⟺ trace positivity.
- Weil II / Deligne purity; algebraic Sato–Tate (`ST(A)` = max compact of `TL(A)(ℂ)`, normalized `q^{−1/2}g`).
- Doplicher–Roberts: compact group reconstructed from a C\*/positivity (Tannakian) structure.

### Angle logs
- `research/construction/NG-frob-tannakian-reconstruction.md` (reconstruction / coherence → free group)
- `research/construction/NG-frob-compactness-created-or-imported.md` (off-line skeptic witness)
- `research/construction/NG-frob-nogo-direction.md` (Grothendieck no-go-proof direction)
