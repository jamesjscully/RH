# PA — does type II_1 finiteness (the CONTINUOUS DIMENSION / trace, Connes' direction) supply the archimedean RADIUS, coupling R10's count to the modulus? [DECISION · DEF · coherence-checked vs 𝔽_q]

[DEAD_END — 2026-06-06] Module: `scripts/numerics/witness/von_neumann_typeII1.py`
(run: `python3 -m scripts.numerics.witness.von_neumann_typeII1`). Builds a MINIMAL, COMPUTABLE II_1
model and tests the 𝔽_q anchor; all asserts pass.

## The mandate (the R8/R10 type obstruction, attacked at the II_1 level)

R8 surveyed the missing `|κ(∞)|` and proved it cannot be a **cardinality**, **continuum**, **length**,
or **index** (all four fail by type). R10 found that **compactness** supplies a finiteness (a
regularized *trace* = the explicit formula = the COUNT) that cardinality could not — but **splits** on
the radius (the trace gives the count/location, purity is a separate input = Weil II = RH).

This pass attacks Connes' direction at its sharpest: a **type II_1 factor** has a trace `τ` that is a
genuinely *different type of finiteness* — a **continuous dimension** `dim_M : Proj(M) → [0,1]`, finite
and normalized (`τ(1)=1`), not any of the four R8 surveyed. The hope (a real one, worth a real attempt):
the II_1 trace `τ(aⁿ) = ∫ zⁿ dμ_a` couples the COUNT (the moments = location) to the RADIUS (the
modulus `|z| = q^{w/2}` of the spectral support), recovering `q^{1/2}` over 𝔽_q WITHOUT assuming the zeros.

## What was BUILT (a minimal computable II_1 model — not gestured at)

`M = L(ℤ) ≅ L^∞(S¹)`, the group von Neumann algebra of `ℤ` = the most transparent II_1 factor, with
trace `τ(f) = ∫_{S¹} f dθ/2π = f̂(0)` (the Haar mean; `τ(1)=1`, a continuous dimension: every spectral
projection has `dim_M =` Haar measure of its support). Frobenius eigenvalues `{αᵢ}` of `C/𝔽_q` are
realized as the essential range of a uniform-arc multiplication operator `a` affiliated to `M`. Then:

- `τ(aⁿ) = (1/N) Σᵢ αᵢⁿ` — the AVERAGED moments = the location/count data;
- `τ(|a|²) = (1/N) Σᵢ |αᵢ|² = q` for a PURE (Weil II) config, so `√(τ(|a|²)) = √q` **looks like the radius**.

## The decisive computation (the split RECURS at the II_1 level — COMPUTED, asserts pass)

`√(τ(|a|²)) = √q` is the **L²-AVERAGE** of the moduli, NOT the radius (the uniform modulus bound / max).
A **trace-preserving off-purity redistribution** (push one eigenvalue to `r₁ > √q`, pull its pair to
`r₂ < √q` with `r₁² + r₂² = 2q`) leaves `τ(|a|²) = q` **UNCHANGED** while **breaking purity**:

| curve (q) | `τ(|a|²)` pure | radius-dev pure | `τ(|a|²)` off-purity | radius-dev off-purity |
|:--|:--:|:--:|:--:|:--:|
| `E/F₅` | 5.0 | 0.0 | **5.0 (same)** | 1.79 (broken) |
| genus-2 `/F₉` | 9.0 | 0.0 | **9.0 (same)** | 2.40 (broken) |
| genus-2 `/F₂` | 2.0 | 0.0 | **2.0 (same)** | 1.13 (broken) |

The II_1 trace reads the AVERAGED moment (a **count-determined** quantity — a moment of the spectral
measure, the LOCATION data); the **radius** (the modulus bound, purity) is exactly the quantity
invisible to all moments of fixed total mass. This is M4r's determinant-neutral redistribution lifted
to the II_1 trace: the FE/trace couple the PRODUCT/average of moduli, never the individual radii.

## The DEEPER, II_1-SPECIFIC killer (the genuinely new content of this pass)

Beyond the trace value, the genuinely **II_1-specific** invariant is the **continuous (Murray–von
Neumann) dimension** itself. It is NORMALIZED `τ(1)=1` — that normalization is *what makes II_1
"finite"*. But the radius `q^{w/2}` is a **SCALE** of the spectral support, and `τ(1)=1` normalizes away
ALL scale: the range-projection dimension `dim_M` is **INVARIANT under `a ↦ λa`** (the radius scaling).
COMPUTED: `λ = 1, 2, ½` move `max|αᵢ| = 3, 6, 1.5` (the radius scales) while `dim_M(range proj) = 1`
stays fixed.

> **The very normalization that DEFINES type II_1 finiteness is EXACTLY what annihilates the radius.**

A scale survives only in the **II_∞ crossed product `M ⋊ ℝ₊*`** — which is precisely Connes' **scaling
site** (R3) — where the scale-carrier is the `ℝ₊*` **CONTINUUM**, the R8 **WRONG TYPE**. So the II_1
route does not cross the type gap; it *re-derives* it: the continuous dimension is a scale-free
finiteness (gives the count), and the radius-scale lives in the `ℝ₊*` continuum it was crossed with.

## The 𝔽_q anchor — HONEST NEGATIVE

`τ` does **NOT** recover `q^{1/2}` as the RADIUS without assuming the zeros. `√(τ(|a|²)) = √q` is the
L²-average of `|αᵢ|`, equal to `√q` for ANY config with `Σ|αᵢ|² = Nq` — including off-line ones. To get
the radius (max `= √q`, uniform modulus) one must ASSUME purity = Weil II = the very thing. The trace
recovers the COUNT; the radius needs purity ON TOP.

## The DH litmus — FAILS (this construction does NOT fail to exist for DH)

A II_1 factor `L(ℤ)` with its trace EXISTS for ANY L-function's data — it requires **no Euler product**.
The construction "distribute eigenvalues as the spectral support of an affiliated operator and average
via `τ`" needs only a spectral measure, which DH HAS (its Dirichlet coefficients give moments). So a
II_1 factor with a trace can be built over the DH spectral data too. It is the **Euler product**
(Frobenius/Satake giving the *pure* radius) that DH lacks — and the trace does not see it. **The II_1
trace is NOT DH-distinguishing**: it fails the DH litmus a real lead must pass.

(Contrast R10's *regularized determinant* `det_∞`, which IS DH-vacuous — no Frobenius ⟹ no `det(1−Fr·T)`
⟹ nothing for `det_∞` to be the analogue OF. The bare II_1 trace is weaker than `det_∞` on the DH axis:
it survives over DH spectral data because it only needs moments, not a Frobenius.)

## Verdict — DEAD_END (a precise one: the split recurs AND the DH litmus fails)

The type II_1 trace is genuinely a **different type of finiteness** (passes the R8 type obstruction *as
a type* — a continuous dimension, not cardinality/continuum/length/index) and supplies the **COUNT**
(averaged moments = location, like R10's nuclear trace). But:

1. **It does NOT couple the count to the RADIUS.** `√(τ(|a|²))` is the L²-AVERAGE of the moduli,
   INVARIANT under a purity-breaking redistribution (`r₁²+r₂²=2q`) — a count-determined quantity, not
   the modulus bound. The R10 / M4r count-vs-radius split recurs verbatim at the II_1 trace level.
2. **The II_1-specific invariant (continuous dimension) is scale-FREE by the `τ(1)=1` normalization** —
   the radius is a scale, so the defining normalization of II_1 finiteness annihilates it; the scale
   survives only in the `M ⋊ ℝ₊*` = scaling-site (R3) continuum, the R8 wrong type.
3. **It FAILS the DH litmus** — a II_1 trace exists over any spectral measure (DH included); it is not
   DH-distinguishing.

This is **not circular** (not a restatement of RH — it is a concrete construction that demonstrably
fails on two independent axes) and **not overclaimed** (it does not prove no future von-Neumann
structure could carry purity; it pins why *this* one cannot). The honest result: the II_1 trace gives
DISCRETENESS + COUNT (the finiteness cardinality could not), never the RADIUS — the radius is a SCALE
the normalized continuous dimension cannot see, and is the separate archimedean `N` (R1) / purity input.

## Falsifier classification (Euler-silent terminus-characterizer, like R1–R10)

- **EULER-BORNE — NO**, and *worse than R10*: the II_1 trace does **not** even fail for DH (it exists
  over DH spectral data). The DH-distinguishing object is the Euler product / Frobenius the trace cannot
  see.
- **SEES-ZEROS — partial**: `τ(aⁿ)` sees the zero *locations* (moments), but the radius datum
  `τ(|a|²)` is INVARIANT under off-line redistribution ⟹ blind to the radius/purity.
- **INDEPENDENT — NO**: the radius-marking input is purity = Weil II = RH; the II_1 trace supplies only
  the count.

→ DEAD_END / DISPERSING-by-design, but a *sharper* dead-end than R10 on the DH axis (the bare II_1
trace is not DH-distinguishing where `det_∞` was). Ladder `DH < ζ < FF`: DH has moments (a II_1 trace
can be built) but no pure radius; ζ has the II_1 trace (count) but the radius is a scale the normalized
dimension cannot see; FF has the radius as **purity (Deligne/Weil II)**, a separate positivity input
the trace structure does not force.

## The sharpened residue (this pass's refinement of R10)

R10: "compactness supplies the trace/count, purity is a separate input." PA refines: **even a type II_1
*continuous dimension* — the subtlest finiteness, genuinely a different type — supplies the count but is
scale-free by its defining normalization, so it cannot carry the radius (a scale); the radius-scale
lives only in the `ℝ₊*` continuum of the II_∞ crossed product (R3's wrong type).** The radius needs the
archimedean `N` / Hodge–Riemann positivity `P_∞ ⪰ 0` (M3/K1/M4r) ON the spectrum, which neither the
trace value nor the continuous dimension carries. The convergence point of the R-thread and K-thread
holds: the missing object is a *positivity that is the modulus bound*, not any flavor of trace/count.
