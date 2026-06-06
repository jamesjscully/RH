# PA — does DOUBLING the archimedean place (a 'ghost prime' / a degree-2 closed point from the (p,q) pair + complex conjugation c) supply the RADIUS `q^{w/2}` (N4), or only R2's free parity `(−1)^w`? [DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §0 (categorical/duality not metric), §2 (the `(p,q)` enrichment). **Block:** the RESIDUE (the radius, the proven terminus R8/R10). **Built on:** R2 (Schmid's `N` gives the parity `(−1)^w`, not the radius — the free phase), R5/R6 (the `(p,q)=H^{1,0}⊕H^{0,1}` rank-2 Jordan-2 minimal carrier; *room ≠ usage*), R8 (the radius = a finite CONSTANT-FIELD cardinality `|κ|=q^{deg}`, absent at `∞` — a TYPE obstruction: continuum/length/index, never a cardinality), R3b-BC (the `q→1` limit DELETES the ground field; *discreteness ≠ finite base size*), R10 (compactness gives the COUNT, the radius is a SEPARATE input).
**Module:** `scripts/numerics/witness/doubled_place_ghost_prime.py` (run: `python3 -m scripts.numerics.witness.doubled_place_ghost_prime`). **Falsifier:** DISPERSING (computed).

---

## The angle (concrete)

The archimedean place ALONE is a single continuum — no finite size (R8: residue field `ℝ`/`ℂ`, cardinality = continuum). ATTEMPT to manufacture a FINITE structure by **DOUBLING**, exploiting the order-2 structure already present at `∞`:

- the `(p,q)` grading `H_ℂ = H^{1,0} ⊕ H^{0,1}` (the weight-1 two-dimensionality = the R5/R6 Jordan-2 minimal carrier);
- complex conjugation `c` (order 2) swapping `H^{1,0} ↔ H^{0,1}`.

**The 𝔽_q analogy under test.** Over a curve `C/𝔽_q`, a CLOSED POINT `x` of **degree 2** has residue field `κ(x)=𝔽_{q²}`, splits into a conjugate PAIR over `𝔽̄_q` swapped by `Gal(𝔽_{q²}/𝔽_q)` (order 2 = a restricted Frobenius), and has NORM `N(x)=q^{deg(x)}=q²`. So a degree-2 point's Galois involution swaps a conjugate pair, and the pair's NORM supplies a power of `q`. **Question:** is the archimedean `(p,q)` pair, swapped by `c` (order 2), the analogue of such a degree-2 place whose 'norm' supplies `q`?

**Success criteria (disciplined, from R2/R8/R10):** (A) the `c`-swap must supply a NUMBER `q` (a radius), not a SIGN (`(−1)^w` = `det` of the swap = R2's free datum); (B) the same degree-2 construction must ANCHOR — recover `q^{1/2}` over `𝔽_q` without assuming the zeros; (C) it must FAIL for DH.

---

## What got BUILT and COMPUTED (no zeros assumed)

**[1] The 𝔽_q degree-2 anchor — radius is `f(q)`, the swap-sign is `q`-independent.** Built a genuine degree-2 closed point: the order-2 Galois swap `[[0,1],[1,0]]` (sign `−1`), residue cardinality `q²`, norm `q²`, weight-1 Frobenius radius `q^{1/2}`. COMPUTED for `q=4,9,25`: radii `2,3,5` (DISTINCT), **swap-sign `−1` CONSTANT**. So the radius tracks the **ground field `q`**, NOT the swap. **Anchor PASSES** — but it pins the radius to the constant-field cardinality, not to the doubling.

**[2] The archimedean double — every scalar is a SIGN or a METRIC.** Built `H^{1,0}⊕H^{0,1}` with `c=[[0,1],[1,0]]` (`det c=−1`, order 2) and the Weil operator `C=diag(i,−i)`, `C²=−I=(−1)^w`. The ONLY scalars a real/complex polarized weight-1 Hodge structure of dim 2 furnishes: `det(c)=−1` (a sign), `C²=−1` (a sign), the Hodge norm `‖·‖_h` (a METRIC = continuum, Sylvester-locked by §0). **`available finite norm q = None`.** No Frobenius eigenvalue, no modulus `q^{1/2}`, no finite point-norm.

**[3] The norm-conversion test — the crux.** Over `𝔽_q` the swap-sign (`−1`, always) and the norm (`q²`, varies) are INDEPENDENT data: the swap exists for every `q`, so it CANNOT determine `q`. The radius-giving NORM is the cardinality of the GROUND FIELD under the conjugate pair. At `∞` the swap exists (`c` is a genuine order-2 involution of the `(p,q)` pair), but the ground field is `𝔽_1`/continuum: the `q` is MISSING.

**[3b] The decisive collapse — the 'ghost prime' IS the degree-2 `𝔽_1`-point.** The archimedean double is literally a degree-2 point over the would-be base `𝔽_1` (`|𝔽_1|=1`). Its norm is `1²=1`, weight-1 radius `1^{1/2}=1` — **the circle collapses to a point**. This is EXACTLY the R3b-BC `q→1` evaporation (`q=5,3,2,1.5,1.1,1.001 → 1`), now reached from the degree-2-point angle: doubling the `𝔽_1`-point gives a degree-2 `𝔽_1`-point, whose norm `1^{deg}=1` is still the collapsed radius. **The doubling raises the DEGREE, not the BASE.**

---

## Verdict — DEAD_END / CIRCULAR: doubling gives the COUNT (degree 2) + R2's free parity, NOT the radius

> **[DEF · PA verdict].** Doubling the archimedean place via the `(p,q)` pair + conjugation `c` supplies the **degree-2 PAIRING** — a genuine order-2 structure (two conjugate "points", a Galois-type involution `c`) — and its `det`/`C²` deliver R2's **free parity `(−1)^w`**. It does NOT supply the **radius `q^{w/2}` (N4)**. Over `𝔽_q` a degree-2 point's radius `q^{1/2}` and norm `q²` come from the **ground-field cardinality `q`** under the pair, NOT from the order-2 swap (sign `−1`, `q`-independent: `q=9` vs `q=25` give the SAME swap, DIFFERENT radii `3,5`). At `∞` the swap exists but the ground field is `𝔽_1` (`|𝔽_1|=1`): the degree-2 `𝔽_1`-point has norm `1²=1`, radius `1` — the circle collapses (R3b `q→1`). **The doubling raises the DEGREE (the count), not the BASE (the radius).**

**Why this is the expected outcome, made exact (the re-coupling).** The whole R-thread separates COUNT from RADIUS. Doubling addresses the COUNT side: a degree-2 point is a counting/edge datum (how many geometric points, with what Galois action — an Euler-product-flavored count). The order-2 swap's only intrinsic invariants are `{order 2, sign −1, trace 0, det −1, charpoly x²−1}` — **all `q`-independent**. To extract `q` from a 2-element structure one must ALREADY have a `q`-element ground field UNDER it; the swap permutes the pair but supplies no cardinality. So the construction **re-derives R2's free parity** for the radius, exactly as warned. This is the count-vs-radius re-coupling at the degree-2-point level: doubling is a finer COUNT (degree 2 instead of 1), and the count is free; the radius is the ground-field norm `|𝔽_q|^{deg}`, which needs the `|𝔽_q|` the archimedean place lacks (R8 type obstruction).

**The type obstruction, restated via doubling.** R8: the missing datum is a finite CONSTANT FIELD, and `Spec ℤ` has none at `∞`. Doubling does not manufacture one — `|𝔽_1^{(2)}| = 1² = 1`, still not a finite `q>1`. The "ghost prime" is a degree-2 `𝔽_1`-point, not a degree-1 `𝔽_q`-point; raising the degree over `𝔽_1` keeps the base `1`. The norm `q^{deg}` is finite-and-`>1` **iff** the base `q>1`, which is precisely the absent constant field.

---

## Falsifier verdict (DISPERSING — characterization, not a `ℤ`-candidate)

- **euler_borne = NO (on the datum actually furnished).** A degree-2 closed point requires a curve over a finite field ⟹ Frobenius ⟹ an Euler product; DH (no product) has NO Frobenius, NO closed point — the degree-2-point STRUCTURE is unposable for DH. BUT the only datum the ARCHIMEDEAN double actually furnishes is the parity `(−1)^w` via the `c`-swap, and that is **DH-SHARED** (DH has the same `Γ_ℝ` archimedean Hodge type, the same `c`, the same `(p,q)`). So like R2/R3/R3b, this pass is Euler-SILENT on the datum it furnishes; the Euler-borne part (the `q`-norm) is exactly the part it CANNOT build at `∞`.
- **sees_zeros = NO.** The furnished datum is the parity (radius-silent: `q=9` vs `q=25`, same parity, different radius). Only N4 sees the zeros, and N4 is absent.
- **independent = NO.** The radius = the constant-field cardinality = the even split = purity = RH (the solved case over `𝔽_q`).

→ `classify(False, False, False) = DISPERSING` (computed). The doubling is the **degree-2 COUNT + R2's free parity** half; the RADIUS is not here.

**Ladder `DH < ζ < FF`.** DH: no Frobenius ⟹ no closed point ⟹ the degree-2-point construction is unposable. ζ: the `c`-swap of `(p,q)` IS a genuine order-2 degree-2 structure (the pairing exists, DH-shared, the parity free), but the base under it is `𝔽_1` (`|𝔽_1|=1`), so the degree-2 norm is `1` and the radius collapses — UNMARKED. FF: a degree-2 closed point of `C/𝔽_q` has residue field `𝔽_{q²}`, norm `q²`, weight-1 radius `q^{1/2}` MARKED — by the **constant field `q` under the curve**, not by the order-2 swap.

---

## Not overclaimed / successor

**Not overclaimed:** PA decides the doubling angle — the `c`-swap of the `(p,q)` pair supplies the degree-2 PAIRING (a count) and R2's free parity, NOT the radius; the radius is the ground-field norm `|𝔽_q|^{deg}` the archimedean base (`𝔽_1`) lacks. It does NOT prove no future structure could supply the constant field; it confirms that **raising the degree over `𝔽_1` does not raise the base** (`1^{deg}=1`), so doubling re-couples to the same count-vs-radius / type obstruction (R8) the whole R-thread reaches. **The honest finding the prompt anticipated:** doubling gives back R2's free parity `(−1)^w` for the radius, plus a degree-2 COUNT — both free; the radius (the ground-field cardinality) is untouched.

**Successor:** the residue is unchanged — supply a finite constant field `q>1` at `∞`. Doubling shows that a degree-`d` structure over `𝔽_1` has norm `1^d=1` for every `d`, so NO amount of degree-raising at `∞` manufactures the base; the missing datum is base-`>1`, not degree-`>1`. This is the 47th confirmation of the constant-field type obstruction (R8), reached from the degree-2-point / doubling angle: **the ghost prime is a degree-2 `𝔽_1`-point, and `|𝔽_1|=1` is exactly the absent radius.**

---

## Verdict

`[DEF · coherence-checked vs 𝔽_q]` — **DOUBLING the archimedean place (a degree-2 closed point built from the `(p,q)=H^{1,0}⊕H^{0,1}` pair + complex conjugation `c`) supplies the degree-2 PAIRING (a COUNT: two conjugate points, an order-2 Galois-type involution) and R2's FREE PARITY `(−1)^w` (the `c`-swap sign), but NOT the radius `q^{w/2}` (N4).** COMPUTED: over `𝔽_q` the radius `q^{1/2}` and norm `q²` track the ground-field cardinality `q` (radii `2,3,5` for `q=4,9,25`), while the swap-sign is constant `−1` (so the swap CANNOT determine `q`); the archimedean double furnishes only signs (`det c=−1`, `C²=−1`) and metrics (Hodge norm, continuum), `available finite norm q = None`; and the "ghost prime" is literally a degree-2 `𝔽_1`-point with norm `1²=1`, radius `1` — the R3b `q→1` collapse. **DISPERSING** (computed): the furnished parity is DH-shared, radius-silent, and `=` purity `=` RH over `𝔽_q`. **The exact re-coupling:** doubling raises the DEGREE (a finer count, free) not the BASE (the radius); the radius is the constant-field norm `|𝔽_q|^{deg}` the archimedean base `𝔽_1` lacks — the R8 type obstruction, now confirmed from the degree-2-point angle. A restatement of the same wall, NOT a lead.
