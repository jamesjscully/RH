# K2r-fix — the reality datum `κ`: a FREE descent condition (the phase), but RADIUS-SILENT by the algebra of conjugations [coherence-checked · anchored vs 𝔽_q / Δ]

**Charter:** `construction-program.md` **§0** (the polarization is a **DUALITY / `*`-involution, NEVER a
metric**), §1 clause C2 (`(p,q)` grading + conjugation `c`), Pillar B (the object by descent).
**Mandate (AGENDA K2r-fix, the KEYSTONE reality datum, HIGH priority):** K2r-split RELOCATED the residue
from "the even split" to the **reality condition** "Frobenius ∈ `Fix(σ_d)`" — over `𝔽_q` the
`q`-Weil-number theorem = "**Frobenius commutes with geometric conjugation**" = the *reality of the
realization* (Deligne purity). K2r-fix attacks that residue: **is there a REAL/condensed structure `κ`
on the weight-2 carrier over `ℤ` (M3b's `κ`, the `c`-fixed locus) whose descent datum FORCES the Satake
pair to be `σ_d`-fixed — or is that real structure itself only available AFTER purity?**
**Module:** `scripts/numerics/witness/reality_datum_kappa.py`
(run: `python3 -m scripts.numerics.witness.reality_datum_kappa`). **Falsifier row added** (`falsify.py`, → 53).

---

## The deliverable — the algebra of conjugations, and the radius/phase orthogonality it forces

The reality condition "Frobenius ∈ `Fix(σ_d)`" decomposes as: the Frobenius `F` commutes with a
**conjugation** `c` on the realization (`c∘F = F∘c`). A conjugation is an **antilinear involution**; its
fixed locus `V^c` is the "real points" = M3b's `κ`. K2r-fix asks whether such a `c` can be the missing
forcing datum. The decisive structural fact is an elementary classification:

> **[DEF + LEMMA · the algebra of conjugations].** On a 1-dim eigen/determinant line `ℂ`, an antilinear
> map `c(z) = μ·\bar z` is an **involution** (`c∘c = id`) **iff** `μ\barμ = |μ|^2 = 1`, i.e. `μ = e^{iθ}`.
> Its **fixed locus** is `{z : μ\bar z = z}`; writing `z = r e^{iφ}`, this is `e^{iθ} r e^{-iφ} = r e^{iφ}`
> ⟺ `θ = 2φ` — **a PHASE condition, INDEPENDENT of the radius `r`.**
> **Corollary (radius-silence).** Every conjugation `c` (`|μ|=1`) is **RADIUS-SILENT**: its fixed locus is
> a *ray* (a phase), never a radius. The reality datum `κ = V^c` cannot constrain `|α|`.

This converts K2r-fix into a typed, computable question and the answer is a clean **orthogonality**: the
reality datum (any conjugation) and the radius (the even split = purity = RH) live on **independent axes**.

---

## The decisive structural finding — `κ` is FREE (the phase) but RADIUS-SILENT (orthogonal to RH)

Executed (`reality_datum_kappa.py`, exact `mpmath` 40 dps; `f = Δ`, arithmetic Satake; 5 Weil curves; DH
type-level). Five computed facts:

### [1] Every conjugation `c(z) = μ\bar z` (`|μ|=1`) is RADIUS-SILENT — `Fix(c)` is a PHASE, never a radius
For `μ ∈ {1, e^{0.7i}, i}`: `c` is a genuine antilinear involution (inv. err `≤2.3e-41`, antilinearity
`≤9.2e-41`), and **all three radii** `r ∈ {0.5, 3, 100}` on the fixed ray `φ = θ/2` are `c`-fixed (err
`~0` / `7.3e-40`), while an off-ray point (wrong phase) is moved (`2.88`). **`Fix(c)` is a RAY (phase),
radius-unconstrained** — `κ` CANNOT supply the radius. This is M3b's "`(−1)^w` is radius-silent" upgraded
to a **theorem about the structure of conjugations**.

### [2] `σ_d(z) = d/\bar z = (d/|z|^2)·z` — a pure RADIAL inversion; its radius is the SCALE `d`, not a conjugation
The determinant-canonical involution **decomposes with the conjugation CANCELLING**: `d/\bar z =
d·z/(z\bar z) = (d/|z|^2)·z` (verified EXACTLY, residual `~1e-35` to `0`, primes 2..11). So `σ_d` is a
**radial inversion about `\sqrt d`** along the *same ray* — purely a **radius** map, **no phase content**.
Its radius `\sqrt d` is the **Euler-borne SCALE** `d = p^{k−1}` (the K2r determinant edge). **The reality
`κ` (a conjugation, phase) and the radius `\sqrt d` (the scale `d`) are ORTHOGONAL data.**

### [3] THE FORK RESOLVED — `[c_0, F] = 0` is the FE/phase-reality, holds at ANY radius (a PLANT confirms)
Realize the FE-conjugation `c_0 = (\text{swap})∘\overline{(·)}` on the 2-dim carrier `F = \mathrm{diag}(α,β)`:
`c_0 F = F c_0` ⟺ `β = \barα` (eigenvalues conjugate-paired) — the **FE/phase-reality**. Verified `[c_0,F]=0`
for the genuine Ramanujan pairs (all primes). **THE DECISIVE PLANT:** an off-radius but **conjugate-paired**
pair `β' = \barα'` with `|α'| = 1065761 ≠ \sqrt d = 534146` **STILL** satisfies `[c_0,F] = 0` — `κ` is
**BLIND to the radius defect**. The reality datum forces the *phase/reality* (the conjugate-pairing = the FE),
**NOT** the even split.

### [4] FF anchor — the reality SPLITS: `[c_0,F]=0` is the FE (free), `|α|=\sqrt q` is the purity theorem
Over `𝔽_q` (5 curves `q=2,5,7,11,13`): `[c_0,F]=0` (the conjugate-pairing) holds **for free** = the FE,
and `|α|=\sqrt q` is the **separate** Deligne-purity theorem (`q-real? True` all curves). So `κ` (= `c_0`) is
**free + radius-silent**; the radius is the theorem. The FORK resolves: **FORK 1 (free) for the PHASE; the
RADIUS is orthogonal — not "after purity", just not a conjugation at all.**

### [5] DH falsifier — `c_0` EXISTS for DH (it has a FE), is DH-SHARED + radius-silent; the radius is the only DH-distinguisher
DH **has** a functional equation ⟹ the conjugate-pairing `[c_0,F]=0` holds for DH too ⟹ `c_0` is
**DH-SHARED** (the reality/phase half does NOT distinguish DH). But DH has no Euler product ⟹ no determinant
`d` ⟹ **no radius `\sqrt d` to match** — the even-split question is **VACUOUS** for DH. The **radius** (the
determinant edge + its even split) is the **only DH-distinguishing datum**, and `κ` does not carry it.
Carrier ladder: **DH (`c_0`, no `d`) < `ζ` (`c_0` + `d`, open split) < FF (`c_0` + `d` + purity theorem)**.

---

## The K2r-fix result — the reality datum SPLITS: phase free + radius-silent, radius = the irreducible RH

| component | datum | status |
|---|---|---|
| `κ = c_0` (the unit conjugation, M3b's real structure) | bare complex conjugation realizing the FE; antilinear involution `\|μ\|=1` | **FREE (available over `ℤ` before purity; FORK 2 FALSE)** |
| `Fix(c_0)` / the commutation `[c_0,F]=0` | `= β=\barα` = the FE/phase-reality (conjugate-pairing) | **FREE, but a PHASE condition — radius-silent** |
| the **radius** `\|α\|=\sqrt d` (`σ_d`'s scale `d`) | `= (d/\|z\|^2)z`, a radial inversion; the even split = purity | **the irreducible RH — ORTHOGONAL to every conjugation** |

**The honest answer to K2r-fix:** the real/condensed structure `κ` **IS** available over `ℤ` for free (the
canonical conjugation `c_0`, M3b-coherent) and FORCES the **phase-reality** (the FE / conjugate-pairing) —
so **FORK 2 ("`κ` is only available after purity") is FALSE**. But `κ` is **RADIUS-SILENT by the algebra of
conjugations** (`|μ|=1` ⟹ a phase condition, never a radius), and the radius `|α|=\sqrt d` (the even split =
purity = RH) is **ORTHOGONAL** to every conjugation — it is the **scale `d`**, an Euler datum no real
structure supplies. **`κ` is FREE but the WRONG HALF.**

---

## Falsifier verdict (K2r-fix — a coherence check on the reality half; the radius is the irreducible residue)

- **EULER-BORNE — NO** (on the reality half). `κ = c_0` is bare complex conjugation; it EXISTS for DH (DH has
  a FE ⟹ the conjugate-pairing holds). The reality/phase half is **DISPERSING** (free, DH-shared).
- **SEES-ZEROS — YES** (only the radius half, via `σ_d`'s scale). `κ` itself is blind: the planted off-radius
  conjugate-paired pair still satisfies `[c_0,F]=0`.
- **INDEPENDENT — NO.** The radius `|α|=\sqrt d` = the even split = Ramanujan/RH; over FF Deligne purity.

Tabled **DISPERSING-on-the-reality-half** (`euler_borne=False`): the keystone is **NOT** the reality datum —
`κ` is the **wrong half** (phase, free, radius-silent). **NEW content:** K2r-fix proves a **theorem** sharpening
M3b — *the archimedean reality datum is radius-silent BECAUSE conjugations (`|μ|=1`) carry only phase, never a
radius* — and resolves the reality/radius fork as an **orthogonality**: `κ` (the FE/phase-reality) is free over
`ℤ` and DH-shared; the radius (the even split = purity = RH) is the **scale `d`**, an Euler datum **orthogonal
to every conjugation**, which **must be Euler-ASSEMBLED in the descent (M4r), not supplied by a real structure.**

---

## Verdict

`[coherence-checked · anchored vs 𝔽_q / Δ]` — K2r-fix executed the reality-datum fork with the **algebra of
conjugations** and found the honest seam: **the real/condensed structure `κ` (the canonical conjugation `c_0`,
M3b's real structure) IS available over `ℤ` FOR FREE** (bare complex conjugation realizing the FE) — **FORK 2
is FALSE** — and it FORCES the **phase-reality** (the FE / conjugate-pairing `β=\barα`). **BUT `κ` is
RADIUS-SILENT by a theorem:** every antilinear involution `c(z)=μ\bar z` is involutive iff `|μ|=1`, and its
fixed locus is a **phase** condition (`θ=2φ`), **never a radius**; a planted off-radius conjugate-paired pair
still commutes with `c_0`. The radius `|α|=\sqrt d` (the even split = purity = RH) is `σ_d`'s **scale `d`**, an
Euler datum **ORTHOGONAL to every conjugation**. **Not overclaimed:** this does not build the radius (that is
RH); it **resolves the reality/radius fork** — `κ` is free (the phase) but the wrong half (radius-silent) — and
proves *why* (the algebra of conjugations), pinning the irreducible residue as the **radius, which must be
Euler-assembled (M4r), not supplied by any real structure.**

**Successors named:**
- **M4r is now the SOLE live keystone item** — the radius is the irreducible residue, ORTHOGONAL to `κ`; the
  reality (phase) half is settled (free, radius-silent). The descent must **Euler-ASSEMBLE the radius `\sqrt d`
  per prime** (the scale, not a conjugation) against the radius-silent `(P_∞, D, c)` at `∞`.
- **K6 [the scale as a NORM, not a conjugation]** — since the radius is `σ_d`'s **scale `d`** (a radial datum,
  not a phase), and §0 forbids metrics: is there a **non-metric** Euler-borne structure (a *valuation* / a
  *graded line with a degree*, e.g. the determinant of Frobenius as a `ℚ_{>0}`-graded GANTM datum) whose
  "size" is `\sqrt d` per prime WITHOUT being a `*`-congruence? The scale is a 1-dim *degree*, not a Gram form —
  this may evade Sylvester where a metric cannot. (falsify: must be Euler-borne, DH-absent, see the radius plant.)
- **K2 re-pointed:** the condensed object supplies `c_0` (the phase, free, radius-silent) — it must additionally
  carry the **scale/degree** `\sqrt d`, which is NOT a conjugation; the condensed framework's contribution to the
  keystone is the **radius/degree carrier**, not the reality datum (now settled as free + insufficient).
