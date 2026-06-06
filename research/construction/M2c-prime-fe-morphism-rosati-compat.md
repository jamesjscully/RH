# M2c′ — `φ_FE` is a rigid-tensor MORPHISM, and `c` is compatible with `D` up to the Tate twist `ℚ(−1)` [COHERENCE · anchored vs 𝔽_q]

**Charter:** `construction-program.md` §1 clauses C2 (`(p,q)`/`c`), C3 (`D` = FE), C4 (`P` = canonical
pairing of `D`); §0 design law (the polarization is the duality pairing, never a metric). **Contract:**
`M1-universal-property-S_Z.md` (the quadruple `(𝒞, ω_∞, D, P)` must be a polarized object of a *rigid
(p,q)-graded tensor category*, the 2-categorical glue of M1 §0). **Built on:** M2 (the FF datum), M4B
(form `(*)` + Rosati), M4C (`D∘D≅id` on `gr^W_2`, `P_NS = ev∘(1⊗φ_FE) = Tr(z w^†)` to `0`, the `g=2`
rank-16 non-semidefinite anchor). **Module:** `scripts/numerics/witness/fe_morphism_rosati_compat.py`
(run: `python3 -m scripts.numerics.witness.fe_morphism_rosati_compat`). **Falsifier row added** (`falsify.py`).

---

## The task — the REMAINDER of M2c/M4D

M4C already PROVED, on the weight-2 NS lattice `gr^W_2 = End(H^1)`:
- **`D∘D = id`** (the lattice is rigid/dualizable) — the M2c involutivity check, on weight 2;
- **`P_NS = ev∘(1⊗φ_FE) = Tr(z w^†)`** to `0.00e+00` — the polarization is the canonical duality
  pairing, NOT a metric (M1's C4 / §0 design law, on the weight-2 carrier);
- the **`g=2` rank-16 non-semidefinite anchor** (so the `g=1` `(0,1,1)` was a rank artifact, confirmed) —
  the M2c/M4D trace-kernel concern.

So **involutivity + trace-kernel are DONE.** M2c′ supplies the two remaining coherence facts that
upgrade `(𝒞, ω_∞, D, P)` from "a matrix in a basis" to a **functor of a rigid tensor category**:

1. **`φ_FE` is a genuine MORPHISM** of the rigid tensor category — not just a matrix.
2. **`c` (the Hodge conjugation) is COMPATIBLE with `D` (the duality)** up to the weight-2 Tate twist
   `ℚ(−1)`: `c` exchanges the Hodge lines AND commutes with `D` modulo the twist.

---

## (A) `φ_FE` is a morphism of the rigid tensor category

**(A1) `φ_FE` is `Φ`-equivariant up to the Tate twist `ℚ(−1)`.** View `φ_FE` as the cup-product iso
`E : H^1 → (H^1)^∨(−1)` (non-degenerate, the Poincaré/Weil pairing). To be a *morphism in the category
of Frobenius-modules* it must intertwine `Φ` with the Frobenius on the (Tate-twisted) dual — the
naturality square
```
        H^1   --F-->   H^1
         |               |
       φ_FE            φ_FE
         v               v
   (H^1)^∨(−1) --q·F^∨--> (H^1)^∨(−1)
```
must commute, i.e. `E F = q · F^∨ E` with `F^∨ = (F^{-1})^T` (the dual of an iso). This is *equivalent*
to the Weil similitude `F^T E F = q E`.

> **EXACT (5 `g=1` curves):** `max|E F − q F^∨ E| ≤ 1e-15` (`0.00e+00` at `q=5`); the morphism square
> commutes for all six curves. So `φ_FE` **intertwines Frobenius with its Tate-twisted dual** — it is a
> morphism of Frobenius-modules, NOT an arbitrary matrix. The Tate twist `ℚ(−1)` (multiplier `q`) is
> exactly the discrepancy that makes the square commute: `φ_FE` is a morphism `H^1 → (H^1)^∨(−1)`, the
> functional equation `s ↔ 1−s` realized categorically.

**(A2) the induced duality `D = (·)^†` on `End(H^1)` is a TENSOR duality.** A duality of the *rigid
tensor* category (not a mere linear involution of a lattice) must be an **anti-automorphism of the
endomorphism algebra** fixing the unit: `(zw)^† = w^† z^†` and `D(Id) = Id`. (An anti-automorphism of
`End(V)` IS the dual functor on `V ⊗ V^∨`.)

> **EXACT (all six curves, `g=1` & `g=2`):** `(zw)^† = w^† z^†` to `0.00e+00` over a spanning basis, and
> `D(Id) = Id` to `0.00e+00` (the unit = the polarization class `Id`, M4B's `F₀` complement). So `D` is
> the duality of the **rigid tensor category** `⟨End(H^1), ∘, Id⟩`, the carrier of `gr^W_2`.

---

## (B) `c` is compatible with `D` up to the Tate twist `ℚ(−1)`

On `H^1`, `c` (Hodge conjugation, `α ↦ ᾱ`) and `D` (FE/Poincaré duality, `α ↦ q/α`) are **genuinely
different maps** — they coincide only on `|α| = √q`. The compatibility is a *structural 2-cell*, not an
equality, and it is RH-INDEPENDENT (it is the FE-borne structure; RH is its *degeneration*).

**(B1) `c` and `D` are commuting involutions.** `c∘c = id`, `D∘D = id`, and `D∘c = c∘D` EXACTLY (both send
`α ↦ q/ᾱ`, and `q` is real). So `{c, D}` generate a **Klein four-group `ℤ/2 × ℤ/2`** acting on the rigid
lattice — this IS "`c` is compatible with `D`."

> **EXACT (all six curves, ON *and* OFF circle):** `D∘D=id`, `c∘c=id`, `D∘c=c∘D` all to `0.00e+00`,
> off-circle too. The commutation is structural (FE-borne), not RH-dependent.

**(B2) `c` exchanges the Hodge lines `H^{1,0} ↔ H^{0,1}`** — the `α`- and `(q/α)`-eigenlines (C2's
requirement; verified in M2/`conjugation_parity_ff.py`, `α^† = ᾱ` on the line).

**(B3) the Tate twist `ℚ(−1)` is the multiplier.** The product `c·D : α ↦ q/ᾱ` is the
Frobenius-similitude direction, with weight-2 normalization
$$
\frac{\mathrm{Tr}(F F^†)}{\mathrm{Tr}(\mathrm{Id}\,\mathrm{Id}^†)} \;=\; \frac{2gq}{2g} \;=\; q \;=\; \mathbb{Q}(-1).
$$

> **EXACT (all six):** `Tr(F F^†) = 2gq`, `Tr(Id Id^†) = 2g`, ratio `= q` exactly. "`c` compatible with
> `D` **up to the Tate twist**" means `c∘D` acts as the twist `ℚ(−1)` on the spectrum.

**(B4) THE LOAD-BEARING SEPARATION: `c = D` on `H^1` ⟺ RH.** The structural compatibility (B1–B3) holds
*always* (FE-borne); the *coincidence* `c = D` is RH (the Hodge lines align with the conjugate lines).

> **EXACT (all six):** `|c(F) − D(F)| = 0.00e+00` on-circle (`c = D`, RH) and `> 1` off-circle
> (`c ≠ D`, RH fails). **RH is the DEGENERATION of the Klein four-group to a `ℤ/2`** — `c` and `D` fuse.
> This is exactly C2's "`c`-EVEN inertia" reading (DONE #31): RH is the *coincidence of two structures*,
> not the value of a `c`-odd functional. The `c`-odd datum vanishes on every FE-symmetric spectrum;
> the live content is `c = D` (an even, structural coincidence).

---

## What M2c′ completes (the categorical object is now coherent)

> **[for M3/M4].** M1's contract asks `(𝒞, ω_∞, D, P)` to be a polarized object of a *rigid `(p,q)`-graded
> tensor category*. M4C gave `D∘D = id` and `P = ev∘(1⊗φ_FE)` (NOT a metric) on `gr^W_2`. M2c′ supplies
> the two remaining coherence facts: **`φ_FE` is a MORPHISM** (A1 `Φ`-equivariant up to `ℚ(−1)`; A2 `D` a
> tensor anti-automorphism), and **`c` is COMPATIBLE with `D`** up to the Tate twist (B1 commuting
> involutions; B2 exchanges Hodge lines; B3 `c·D` = twist; B4 RH = the coincidence `c = D`). Together with
> M4C the quadruple is a **coherent 2-categorical datum** on the weight-2 carrier — the well-typed target
> M3's archimedean `(p,q)`/condensed datum deforms into. The `ℤ`-hardness is unchanged: the single hinge
> **C3b** (the Euler-borne radius `μ`), to be realized as M4's Euler-assembly of `P_NS` on the *global*
> weight-2 lattice.

---

## Falsifier verdict (M2c′ — a COHERENCE check on the FF anchor, CIRCULAR over `ℤ` as expected)

- **Euler-ASSEMBLED YES** — the morphism square `E F = q F^∨ E` and the twist `Tr(F F^†) = 2gq` read the
  Frobenius `q`-similitude (the Euler/Satake data). DH has no Frobenius weight ⟹ no `φ_FE` morphism
  square ⟹ no Tate twist ⟹ no coherent object. DH-failing.
- **SEES-ZEROS YES** — the coincidence `c = D` (B4) holds ⟺ `|α| = √q` ⟺ RH (fails off-circle).
- **INDEPENDENT NO** — over `𝔽_q` the `c = D` coincidence IS the Weil/Riemann positivity = RH ⟹
  **CIRCULAR over `ℤ`**, expected and correct for a coherence check on the anchor.

**NEW content (not circular):** `φ_FE` is a genuine rigid-tensor **MORPHISM** (`Φ`-equivariant up to
`ℚ(−1)` + `D` a tensor anti-automorphism), and `c` is a **COMMUTING INVOLUTION** compatible with `D` up
to the Tate twist, with **RH = the Klein-four degeneration `c = D`** (the `c`-EVEN reading). The
categorical object `(𝒞, ω_∞, D, P)` is now COHERENT — the M2c/M4D remainder, done.

---

## Verdict

`[COHERENCE · anchored vs 𝔽_q]` — the M2c/M4D **remainder** is established on the weight-2 carrier:
**(A)** `φ_FE` is a genuine MORPHISM of the rigid tensor category — `Φ`-equivariant up to the Tate twist
(`E F = q F^∨ E`, `≤1e-15`) and inducing a TENSOR duality `D` (anti-automorphism `(zw)^†=w^† z^†` and
`D(Id)=Id`, both `0.00e+00`); **(B)** `c` is COMPATIBLE with `D` up to `ℚ(−1)` — they are **commuting
involutions** (Klein `ℤ/2 × ℤ/2`, `0.00e+00` on/off circle), `c` exchanges the Hodge lines, the twist
`q = Tr(F F^†)/Tr(Id Id^†)` is the `c·D` multiplier, and **RH is the degeneration `c = D`** (separation
`0` on-circle, `>1` off-circle, all six curves). Verified EXACT at `g=1` (rank 4) and `g=2` (rank 16).
**Not overclaimed:** an FF anchor / coherence check, CIRCULAR over `ℤ` as expected; the new content is
that `(𝒞, ω_∞, D, P)` is now a coherent 2-categorical object (morphism + commuting-involution
compatibility), the well-typed target M3 deforms into. **Successors named:** M3 (the archimedean
`(p,q)`/condensed datum supplying `c` and the Hodge `L`, checked `≠ *`-congruence) — now with the
weight-2 categorical target fully coherent; M4 (Euler-assemble `P_NS` / the form `(*)` on the GLOBAL
weight-2 lattice, the single hinge C3b).
