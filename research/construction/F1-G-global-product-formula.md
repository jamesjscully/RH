# F1 ground (G) — the GLOBAL / PRODUCT-FORMULA scale: does `∏_v |x|_v = 1` supply the archimedean arithmetic scale `q` (the scaled conjugation), or reproduce the audit's EDGE? [DECISION · coherence-checked vs 𝔽_q · SCALE_FREE_CLOSED]

2026-06-06. Candidate ground **(G)** from `research/f1-construction.md`: the scale at `∞` borrowed from the primes via the product formula (Artin–Whaple) `∏_v |x|_v = 1`, coupling infinity to all primes — "the archimedean size is minus the sum of the prime sizes." The hope: `𝔽₁`'s finiteness at `∞` is **global**, not local — the archimedean Frobenius = minus the sum of the prime Frobenii, supplied through the adelic/explicit-formula coupling. Modules: inline mpmath 30–40 dps (this log); anchors `explicit_formula.py` (DH falsified, COMPUTED), product-formula on `𝔽_q(P¹)` and the Frobenius FE-vs-radius split (COMPUTED, this log). Builds on R3/R3b (continuous + periodic-orbit scaling → edge/length, not radius), R8 (residue field = constant-field cardinality, type obstruction), R10 (Connes' regularized trace = the count, not the radius), PP-synthesis (Step A free / Step B = RH), the audit (`W_∞ ≥ Σ_p W_p` = the edge wall).

## The mandate (the scaled-conjugation test for ground G)

`𝔽₁ ⟺ a SCALED CONJUGATION`: the archimedean place HAS the reality (`F†=F̄`, the order-2 conjugation `Gal(ℂ/ℝ)`) but LACKS an arithmetic SCALE `q`. Decisive test for **G**: does the product formula / adelic coupling SUPPLY that `q` GLOBALLY — i.e. is the archimedean term of the explicit formula, coupled to the primes, a genuine arithmetic radix `q` marking `|α|=√q`? Or does going global only reproduce the audit's **edge** (`Re s=1`, the FE/abscissa), never the **line** (`Re s=½`, the radius)?

---

## What got computed (exact, mpmath; reproduced this pass)

**[1] ANCHOR — the product formula on `𝔽_q(C)` recovers the DEGREE/EDGE constraint, NOT the per-eigenvalue radius.** [computed, anchor]
On `𝔽_q(P¹)`, `q=5`, `x=(t−a)/(t−b)`: `|x|_a = q^{−1}` (zero), `|x|_b = q^{+1}` (pole), product `= 1`. The product formula `∏_v |x|_v = 1` is equivalent to `Σ_v deg(v)·ord_v(x) = 0` — **`deg(div(x)) = 0`, the degree-0 constraint = the EDGE/determinant datum.** The base `q` APPEARS inside each `|x|_v = q^{−deg(v)ord_v(x)}` **because the finite constant field `𝔽_q` already lies under the curve** — the product relation does not manufacture it; it consumes it. The product formula recovers the **degree/FE constraint**, never `|α|=√q`.

**[2] The GLOBAL product fixes the DETERMINANT/FE (Step A); the RADIUS (Step B = RH) is EXTRA and INVISIBLE to it.** [computed, decisive]
Frobenius on `H¹(C)`, genus 1, `q=5`. Two configs with the **same global product** `α₁α₂ = q = 5` (FE / Poincaré-duality coupling intact):
- **PURE** (RH holds): `|α₁|=|α₂|=√q=2.236`.
- **OFF-LINE** (RH fails, `r=1.8`): `|α₁|=4.025`, `|α₂|=1.242` — product still `= 5.000`.

> Both satisfy `α₁α₂=q` (the global / product-formula / functional-equation coupling). **The product formula CANNOT distinguish them.** The radius `|α|=√q` is an EXTRA condition (Weil II / purity) the global product never sees. **Step A (the product `αα′=q`) is GLOBAL and free; Step B (the per-eigenvalue radius) is the residue.**

**[3] CAVEAT (ruthless) — the archimedean `|·|_∞` is the CONTINUUM `ℝ_{>0}`, normalized by the product; NOT a finite `q`.** [computed]
Over `ℚ`, `x=6=2·3`: `|6|₂=½`, `|6|₃=⅓`, `|6|_∞=6`; product `= 1`. The archimedean size IS "minus the sum of the prime sizes" — genuinely GLOBAL, borrowed. **But its base is the continuum `ℝ_{>0}`** (the usual real absolute value), not a power of a finite field. At finite `p` the size lives in the **discrete** group `p^ℤ` (base `p`); at `∞` it lives in the **continuum** `ℝ_{>0}`. The product formula COUPLES them but does **not transmute the continuum into a finite `q`** — it is exactly the R3/R8 type obstruction (continuum / wrong type), reached now from the global/adelic angle. The "minus the sum of the primes" is a **real number**, not a `q`-power.

**[4] EDGE vs LINE — the archimedean term of the explicit formula carries the FE-symmetric axis (`½`), DH-SHARED.** [structural/computed]
The Weil explicit formula couples zeros and primes: `Σ_ρ h(γ) = Σ_p (prime side) + W_∞`, with `W_∞ = (1/2π)∫ h(r)[Γ_ℝ′/Γ_ℝ(½+ir)+c.c.]dr`, built from `Γ_ℝ(s)=π^{−s/2}Γ(s/2)` — an **INFINITE product** (pole tower `0,−2,−4,…`, the open/affine signature, PP). Its only "scale" is the **FE-symmetric center `Re s=½`** (the fixed locus of `ξ(s)=ξ(1−s)`). But **DH also satisfies `ξ_DH(s)=ξ_DH(1−s)`** — the symmetry axis `½` is **DH-SHARED = Step A**. Pinning the zeros TO that axis is **Weil's positivity of the explicit-formula quadratic form = RH (circular)**, exactly R10's finding at the trace level. The global coupling delivers the COUNT/location (`Σ_ρ` = the explicit formula, Connes' regularized trace) and the FE axis as a SYMMETRY, never the per-eigenvalue modulus.

**[5] DH falsified.** [computed, `explicit_formula.py`] DH has **no Euler product** ⟹ its prime-side coefficients `c_DH(n)` are neither nonnegative nor prime-power-supported (negative at `n=3,4,9,12,…`; off-prime-power support at `n=6,12,14,…`). With no Euler factors there is **no per-prime local size, no `|·|_p` discrete `q^ℤ` structure, hence no product-formula coupling of finite places to `∞`** in the arithmetic-geometric (Frobenius) sense. The global/product-formula `𝔽₁` route is **unposable for DH** — it requires the Euler product to have the per-place radices at all. G correctly DIES for DH.

---

## The crux — does GLOBAL add the radius-scale, or recurse to the audit's EDGE? (ruthless)

**It recurses to the EDGE.** The product formula / adelic coupling supplies, with full rigor and for free:
- **(A) the FE / determinant coupling** `∏_v |x|_v = 1` ⟺ `deg(div)=0` ⟺ `α·α′=q` (Step A, item [1]/[2]);
- **(B) the FE-symmetric center `Re s=½`** as the fixed locus of `ξ(s)=ξ(1−s)` (item [4]) — but **DH-shared**, the abscissa-of-symmetry, not the radius;
- **(C) the regularized trace / explicit formula** (Connes, R10) — the COUNT/location of the zeros, the finiteness a continuum/colimit cannot block.

It does **not** supply:
- the **per-eigenvalue radius** `|α|=√q` (item [2]: invisible to the product; the off-line config satisfies every global relation);
- a **finite arithmetic `q` at `∞`** (item [3]: the archimedean factor is the continuum `ℝ_{>0}`, "minus the sum of the primes" = a real number, not a finite base — the R8 constant-field type obstruction, global angle);
- the **cross-place forcing** `W_∞ ≥ Σ_p W_p` at the LINE — the audit proved this coupling gives the **half-plane / edge `Re s=1`** (Siegel), and the reflected centre `Re s=½` is EMPTY of independent forcing.

> **The global route reproduces the audit's edge, not the radius.** "The archimedean Frobenius = minus the sum of the prime Frobenii" is **true for the LOCATION/EDGE half** (the explicit-formula coupling, the FE center) — it is precisely Connes' trace = the count (R10). But the **radius / per-eigenvalue modulus** is NOT "minus the sum of the prime moduli": each `|α_p|=√p` is a SEPARATE purity statement at each prime (Weil II), and the global sum couples their LOCATIONS (the explicit formula), never their per-eigenvalue equality. The scaled conjugation needs the **modulus** marked at `∞`; the product formula marks the **location-axis** at `∞` (the FE center `½`), which DH shares.

## Is the global archimedean scale an arithmetic `q`? — NO: it is the continuum + the abscissa.

Two distinct "scales" the global structure offers at `∞`, both wrong-type:
1. **The continuum `ℝ_{>0}`** (the archimedean `|·|_∞`, item [3]) — base `R3`'s `ℝ_{>0}^×`, no marked finite `q`, exactly R3/R8's continuum type obstruction.
2. **The FE-symmetric center `½`** (item [4]) — a self-referential / symmetry-axis scale, **DH-shared**, the abscissa of the functional equation, not the radius. A scale that is "the FE fixed locus" is **not an arithmetic `q`**: it is the Step-A axis the whole program has separated from the radius since R3.

Neither is a finite arithmetic radix. The genuine `q` only ever enters at the **finite** places (where the constant field `𝔽_q` lies under the curve, item [1]) — the archimedean place is the one place where the product formula's factor is the continuum, with no finite base to borrow because **`Spec ℤ` has no constant field at `∞`** (R8). The product formula borrows the archimedean SIZE globally, but the thing it borrows is a real number (a location/volume), not a finite-field cardinality (a radius).

---

## Verdict — SCALE_FREE_CLOSED (WRONG_SCALE: continuum + FE-abscissa; the audit EDGE, global angle)

> **[DECISION · G verdict].** The product formula `∏_v |x|_v=1` genuinely makes the archimedean size **GLOBAL** ("minus the sum of the prime sizes," computed `x=6`), and the global/adelic coupling supplies — for free — the **FE/determinant coupling** (`α·α′=q`, Step A), the **FE-symmetric center `Re s=½`** (the symmetry axis), and **Connes' regularized trace** (the explicit-formula COUNT/location, R10). **But it does NOT supply the archimedean arithmetic scale `q`.** (i) The global product is the **degree-0 / FE / determinant** datum — two Frobenius configs with the SAME product `α₁α₂=q=5` but radii `{2.24,2.24}` (pure) vs `{4.03,1.24}` (off-line) are **indistinguishable** to it (COMPUTED): the radius is EXTRA and invisible. (ii) The archimedean factor `|·|_∞` is the **continuum `ℝ_{>0}`** (a real number, "minus the sum of the primes"), normalized by the product — **not a finite base** (the R3/R8 continuum/constant-field type obstruction, global angle): the product COUPLES the discrete `p^ℤ` at finite places to the continuum at `∞` but never transmutes it into a finite `q`. (iii) The only "scale" the archimedean explicit-formula term marks is the **FE-symmetric center `½`**, which **DH SHARES** (`ξ_DH(s)=ξ_DH(1−s)`) — the abscissa of symmetry (Step A), not the radius; pinning the zeros TO it is **Weil positivity = RH (circular)**. So **going global REPRODUCES the audit's EDGE** (`W_∞ ≥ Σ_p W_p` = the half-plane / FE-axis coupling), never the line: "the archimedean Frobenius = minus the sum of the prime Frobenii" holds for the **LOCATION/count** (Connes' trace) but NOT for the per-eigenvalue **modulus** (purity is per-place, not a global sum). **DH dies** (no Euler product ⟹ no per-prime `|·|_p` radix ⟹ no product-formula coupling of finite places to `∞` in the Frobenius sense — unposable). **SCALE_FREE_CLOSED: ground G carries the reality and the global LOCATION-coupling, but its archimedean scale is the continuum `ℝ_{>0}` plus the FE-abscissa `½` — wrong type, DH-shared, the audit EDGE — not an arithmetic `q`.**

## The five-line decision (as required)

- **(a) Does the product formula make the archimedean scale GLOBAL?** YES — `|·|_∞` is genuinely "minus the sum of the prime sizes" (`x=6`: `|6|₂|6|₃|6|_∞ = 1`, COMPUTED). The archimedean size is borrowed from the primes globally. Premise real.
- **(b) Is that global scale an arithmetic `q`?** NO — it is the **continuum `ℝ_{>0}`** (a real number, R3/R8 wrong type), normalized by the product; the discrete `q^ℤ` lives only at finite places, where `𝔽_q` is already under the curve. The product couples but does not transmute the continuum into a finite base.
- **(c) Does it supply the radius, or recurse to the EDGE?** **The EDGE.** The global product fixes the FE/determinant (`α₁α₂=q`, Step A) — two configs with the same product but different radii are indistinguishable (COMPUTED, `{2.24,2.24}` vs `{4.03,1.24}`). The archimedean explicit-formula term carries the **FE center `½`** (DH-shared, the abscissa), not the modulus. `W_∞ ≥ Σ_p W_p` = the half-plane/edge, the line is empty (audit).
- **(d) "Archimedean Frobenius = minus the sum of prime Frobenii"?** TRUE for the **location/count** (Connes' regularized trace = the explicit formula, R10) — NOT for the **radius**: purity `|α_p|=√p` is a SEPARATE per-place statement, not a global sum; the coupling sums LOCATIONS, never per-eigenvalue moduli.
- **(e) Honest verdict + residual.** **SCALE_FREE_CLOSED (WRONG_SCALE).** G is the **audit EDGE reached from the global/product-formula angle**: it supplies Step A (FE coupling), the FE-axis `½` (DH-shared), and Connes' count, but the archimedean factor is the continuum and the radius is invisible to every global relation. Residual: the radius is **per-place purity ON the discrete spectrum** (R10/R11) — a modulus bound `|α|=√q` that is NOT a global sum of locations and NOT the FE-symmetric axis. The product formula is the wrong instrument: it couples sizes/locations adelically; the radius is the per-eigenvalue equality (AM–GM equality case) that no global SUM detects.

## Falsifier row (G — terminus-characterizer, Euler-silent by design)

- **EULER-BORNE — partial/by-design.** The product-formula coupling of finite places to `∞` REQUIRES the Euler product (per-prime `|·|_p` radices); DH (no Euler product) has no such coupling — `explicit_formula.py` COMPUTED the DH prime-side as non-nonnegative / off-prime-power. So G's *posability* is Euler-borne, but G itself type-checks the global scale (continuum + FE-axis), not a standalone `ℤ`-positivity → DISPERSING-by-design.
- **SEES-ZEROS — the location yes, the radius no.** The explicit formula / Connes' trace sees the zero LOCATIONS (the count); the global product is RADIUS-silent (two configs, same product, different radii — COMPUTED).
- **INDEPENDENT — NO.** The FE-axis `½` is DH-shared; pinning zeros to it = Weil positivity = RH.

→ **DISPERSING-by-design** (global-angle terminus-characterizer, Euler-silent like R1–R10). **Ladder `DH < ζ < FF`:** DH not even product-posable (no `|·|_p` radices, no coupling); `ζ` the `q→1`/`𝔽₁` place — the product formula couples discrete finite places `p^ℤ` to the **continuum** `ℝ_{>0}` at `∞`, supplying the FE/edge and Connes' count but **no finite archimedean `q`**, radius UNMARKED; FF a curve over a finite constant field `𝔽_q` — `|x|_v = q^{−deg·ord}` with ONE shared `q`, the product formula = `deg(div)=0` (the EDGE), and the radius `|α|=√q` supplied SEPARATELY by Weil II (the finite constant field under the curve), not by the product. Confirms R3b/R8/R10 from the global/product-formula angle.
