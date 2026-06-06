# M3b — the archimedean coherence of `(P_∞, D, c)`: `C_W` commutes with `D` up to `ℚ(−w)`, Frobenius-free [COHERENCE · anchored vs polarized-HS]

**Charter:** `construction-program.md` §1 clauses C2 (`(p,q)` grading + conjugation `c`), C4 (`P` =
canonical pairing of `D`), §0 design law (the polarization is the duality pairing, **never a metric**).
**Mandate (AGENDA M3b):** prove `P_∞` is **functorial** in the Hodge datum and that the **Weil operator
`C_W` commutes with the duality `D` up to the Tate twist `ℚ(−w)`** — so `(P_∞, D, c)` is a coherent
triple at `∞`, the **archimedean mirror of M2c′(A)/(B)** (`fe_morphism_rosati_compat.md`), with RH read
**archimedeanly** as the degeneration `c = D` (no Frobenius). **Built on:** M3
(`M3-archimedean-hodge-polarization.md`, which INVENTED `P_∞(x,y) = S(C_W x, κ y)` with the Weil operator
`C_W = i^{p−q}` replacing Frobenius and the intrinsic real structure `κ`). **Module:**
`scripts/numerics/witness/archimedean_coherence.py`
(run: `python3 -m scripts.numerics.witness.archimedean_coherence`). **Falsifier row added** (`falsify.py`,
now 49 rows).

---

## The translation dictionary: M2c′ → M3b (strip Frobenius, replace `q` by `(−1)^w`)

M2c′ proved the coherence of `(C, ω_∞, D, P)` on the **FF anchor**, where `c`, the Weil operator, and
the **multiplier `q`** were all *borrowed from Frobenius* (`c : α ↦ ᾱ` coinciding with `D : α ↦ q/α` on
`|α| = √q`; the Tate twist read off `Tr(F F^†)/Tr(Id Id^†) = q`). At the archimedean place `∞` there is
**no Frobenius**. M3 supplied the intrinsic replacement; M3b proves every M2c′ coherence fact survives
the substitution

| Frobenius / FF (M2c′) | archimedean / `∞` (M3b) |
|---|---|
| Frobenius `F` (the `q`-similitude `F^T E F = q E`) | **Weil operator `C_W = i^{p−q}`** (the `(p,q)` grading as an operator) |
| cup product `E` | cup-product duality `S` (`S^T = −S`, weight 1) |
| Frobenius weight `q` (= base-field size) | **`(−1)^w`** (= weight **parity**, a SIGN; for `w=1`: `C_W^2 = −1` = the complex structure `J`) |
| `c : α ↦ ᾱ` borrowed from Frobenius | `c = κ`, the **intrinsic real structure** `V = V_ℝ ⊗ ℂ` |
| morphism square `E F = q F^∨ E` (M2c′ A1) | **`D(C_W) = C_W^{−1}`** (the `C_W`–`D` 2-cell, B3 below) |
| `c = D ⟺ |α| = √q ⟺ RH` (M2c′ B4) | **`c = D` ⟺ polarized type `Y > 0`** (the Hodge-type alignment, C3 below) |

The genuinely new structural content is the row **`q ↦ (−1)^w`**: the Frobenius weight is replaced by the
**parity of the Hodge weight** — a sign, not a number, because `ℤ` has no Frobenius weight to supply `q`.

---

## [COHERENCE] The three facts (EXACT on the weight-1 polarized-HS anchor, `g = 1, 2, 3`, multiple seeds)

The anchor is the M3 model: `V = H^1(C)` of a genus-`g` curve at `∞`, `V = H^{1,0} ⊕ H^{0,1}`, cup product
`S = J = \begin{psmallmatrix}0&I\\-I&0\end{psmallmatrix}`, period matrix `[I; Z]`, `Z = X + iY`, `Y > 0`,
`C_W = i` on `H^{1,0}`, `−i` on `H^{0,1}`.

### (A) `P_∞` is FUNCTORIAL — the archimedean mirror of M2c′(A) "`φ_FE` is a morphism, not a matrix"

A morphism of polarized Hodge structures `f : (V, F^•, κ) → (V', F'^•, κ')` (here realized as a symplectic
base change `M ∈ Sp(2g)`, `M^T S M = S`) satisfies:

- **`f` commutes with the Weil operator:** `f ∘ C_W = C_W' ∘ f` (residual `≤ 2.7e-15` all `g`/seeds). The
  Weil operator `C_W = i^{p−q}` is determined *only by the `(p,q)` grading*, so **any** HS-morphism
  commutes with it — `C_W` is a **natural transformation**, not a coordinate choice.
- **`f` is an isometry of the duality:** `M^T S M = S` (residual `≤ 3.3e-16`).
- **`f` intertwines the polarization:** `f^* P_∞' = P_∞`, i.e. `M^* H' M = H` (residual `≤ 3.6e-15`).

So `P_∞` is functorial: the polarization is a natural pairing of the Hodge datum, the archimedean analogue
of M2c′(A) (`φ_FE` a genuine rigid-tensor morphism, not a matrix in a basis).

### (B) `C_W` COMMUTES with `D` up to the Tate twist `ℚ(−w)` — the archimedean `q`-similitude

This is the load-bearing mirror of M2c′(A1)'s morphism square `E F = q F^∨ E`, with `q ↦ (−1)^w`:

- **(B1) `C_W` is an isometry of `S`:** `C_W^T S C_W = S` (residual `≤ 4.6e-16`) — the archimedean
  `q`-similitude with multiplier **normalized to `1`**, because `i^{p−q}·i^{q−p} = i^0 = 1` (the Weil
  operator preserves the cup product on a dual `(p,q)/(q,p)` pair).
- **(B2) the central twist `C_W^2 = (−1)^w` on `V`** (residual `≤ 5.0e-15`; `= −I` at weight 1). On
  `V^{p,q}` with `p + q = w`, `C_W^2 = i^{2(p−q)} = (−1)^{p−q} = (−1)^{p+q} = (−1)^w` (since `p−q ≡ p+q`
  mod 2). **This `(−1)^w` is the archimedean analogue of the Frobenius weight `q`** — a *sign* (the weight
  parity), not a base-field size. For weight 1 it is `C_W^2 = −1`, the **complex structure `J`** of the
  Hodge filtration — exactly the reality datum `ℤ` has no Frobenius to supply.
- **(B3) the `C_W`–`D` 2-cell:** `D(C_W) = C_W^{−1}` (residual `≤ 2.7e-15`), where `D(z) = S^{−1} z^T S` is
  the Poincaré/Rosati duality on endomorphisms. Since `C_W^2 = (−1)^w`, this reads `D(C_W) = (−1)^w C_W`,
  i.e. **the Weil operator intertwines `D` with its `(−1)^w`-twisted self** — the archimedean morphism
  square, the mirror of `E F = q F^∨ E`.

### (C) The triple `(P_∞, D, c)` is COHERENT; RH read ARCHIMEDEANLY = `c = D`

Mirror of M2c′(B1)–(B4):

- **(C1) `c = κ` and `D` are commuting involutions** on `End(V)`: `D∘D = id`, `c∘c = id`, `D∘c = c∘D`,
  all **`0.0e+00` exact** over a spanning basis — a Klein `ℤ/2 × ℤ/2`, RH-independent (mirror of B1, now
  with `c` the *intrinsic* real structure).
- **(C2) `c` exchanges the Hodge lines** `H^{1,0} ↔ H^{0,1}` (`‖P_{10}∘c(H^{1,0})‖ ≤ 1.8e-15`) — the M3
  fact, re-confirmed as part of the triple (mirror of B2).
- **(C3) THE ARCHIMEDEAN SEPARATION — `c = D` ⟺ the polarized type `Y > 0`.** Over `𝔽_q`, M2c′(B4) had
  `c = D ⟺ |α| = √q ⟺ RH`. At `∞` there is no `q`; the mirror is the **Hodge-type alignment**: `P_∞ > 0`
  on `H^{1,0}` (the primitive part) — i.e. the conjugation `c` and the duality `D` induce the *same*
  positive form — **iff** the polarized type `Y > 0`. Sweeping Riemann's second relation `Y → (1−2t)|Y|`:

  | `t` (sweep) | `0.00` | `0.25` | `0.49` | `(0.50: Y=0)` | `0.51` | `0.75` | `1.00` |
  |---|---|---|---|---|---|---|---|
  | min eig `P_∞|_{H^{1,0}}` (`g=1`) | `+2.03` | `+1.02` | `+0.04` | degenerate | `−0.04` | `−1.02` | `−2.03` |
  | min eig `P_∞|_{H^{1,0}}` (`g=2`) | `+4.72` | `+2.36` | `+0.09` | degenerate | `−0.19` | `−4.65` | `−9.31` |

  A **monotone flip** `+ → −` through the degeneration `Y = 0`, all `g`. So the archimedean reading of
  RH = `c = D` is: **the reality structure `c` and the cup-product duality `D` agree on the primitive
  part iff the Hodge type is polarized** — the `(p,q)` analogue of "a zero ON vs OFF the critical line",
  supplied by the Weil operator `C_W`, **not** by a Frobenius weight.

---

## Why this completes M3 → `(P_∞, D, c)` is a coherent triple at `∞`

M3 *invented* `P_∞` Frobenius-free; M3b proves it is **coherent**:
- **(A)** `P_∞` is functorial — a natural pairing of the Hodge datum (the Weil operator is natural);
- **(B)** `C_W` commutes with `D` up to the Tate twist `ℚ(−w)`, multiplier `(−1)^w` = the weight parity
  (a *sign* replacing the Frobenius weight `q`) — the archimedean `q`-similitude;
- **(C)** `(P_∞, D, c)` is a coherent triple (`c, D` commuting involutions; `c` swaps the Hodge lines),
  and RH read archimedeanly is the degeneration `c = D` = the Hodge-type alignment `Y > 0`.

This is the **archimedean mirror of M2c′(A)/(B)**: the well-typed, **coherent** archimedean half that M4's
descent glues to the prime Euler factors. With M2c′ (the weight-2 FF half) and M3 (the invented datum),
the categorical object `(𝒞, ω_∞, D, P)` now has a coherent archimedean place.

---

## Falsifier verdict (M3b — a COHERENCE check on the archimedean/Hodge anchor; Euler-SILENT by design)

- **EULER-ASSEMBLED — NO, BY DESIGN.** The archimedean triple is the place at `∞` (the `Γ`-factor),
  **DH-shared**. The multiplier `(−1)^w` is a **sign** (the weight parity), **not an Euler datum** — it does
  not distinguish `ζ` from Davenport–Heilbronn. M3b's job is **coherence** of the reality/phase half, not
  Euler-discrimination; the cross-place coupling is M4's descent. Tabled **DISPERSING-by-design**
  (`euler_borne = False`) — the archimedean half, not a standalone RH-form.
- **SEES-ZEROS — YES** (the Hodge-type analogue): the `c = D` alignment (C3) holds ⟺ `Y > 0` and fails
  when the `(p,q)` type degenerates (`Y < 0`).
- **INDEPENDENT — NO** on the anchor: the "`c = D` ⟺ polarized" fact IS the Hodge–Riemann relation
  (= the solved case).

**NEW content (not circular):** the archimedean coherence of `(P_∞, D, c)` is **proven Frobenius-free** —
`C_W` commutes with `D` up to `ℚ(−w)` with multiplier `(−1)^w` (a *sign* replacing the Frobenius weight
`q`), `P_∞` is functorial, and RH = the archimedean `c = D` = the Hodge-type alignment. The archimedean
mirror of M2c′(B) is **complete**.

---

## The structural lesson M3b surfaces (the next hinge, sharpened)

M2c′ read the Tate multiplier as the **Frobenius weight `q`** (a base-field size, an Euler/Satake datum);
M3b reads its archimedean mirror as **`(−1)^w`** (a *sign*, the weight parity, DH-shared). **This is the
hinge C3b in its sharpest archimedean form:** the FF's multiplier *carries the radius* (`√q` is the
Euler-borne Frobenius weight), but the archimedean multiplier `(−1)^w` is a sign that carries **only the
reality**, not the radius. So the archimedean half supplies the `(p,q)`/reality structure but is **radius-
silent** — exactly why the centre `Re s = ½` must come from the **gluing** (M4's descent), where the
prime Euler factors (carrying `√q`-analogues per prime via the Satake products `αᵢ(p)αⱼ(p)`) meet the
archimedean `(−1)^w` sign. **The Frobenius weight `q` does not survive to `∞` as a number — only as a
parity — so the radius must be Euler-assembled in the descent, never read off the archimedean place.**

---

## Verdict

`[COHERENCE · anchored vs polarized-HS]` — the **archimedean coherence of `(P_∞, D, c)`** is proven
Frobenius-free, the mirror of M2c′(A)/(B). Three EXACT facts on the weight-1 polarized-HS anchor
(`g = 1, 2, 3`): **(A)** `P_∞` FUNCTORIAL (a morphism of HS commutes with `C_W` and intertwines `P_∞`,
residuals `≤ 3.6e-15`); **(B)** `C_W` COMMUTES with `D` up to `ℚ(−w)` — isometry of `S` (mult `1`),
`C_W^2 = (−1)^w` (the central twist, a *sign* replacing the Frobenius weight `q`), `D(C_W) = C_W^{−1}`
(the `C_W`–`D` 2-cell); **(C)** the triple is COHERENT (`c, D` commuting involutions `0.0e+00`; `c` swaps
Hodge lines) and RH read archimedeanly = `c = D` = the Hodge-type alignment (`P_∞ > 0 ⟺ Y > 0`, monotone
flip). **Not overclaimed:** a coherence check on the archimedean half, **Euler-silent by design** (the
`Γ`-factor is DH-shared; `(−1)^w` is a sign, not an Euler datum). **Successors named:** M4 (the descent
now has a *coherent* archimedean input `(P_∞, D, c)` to glue, with the sharpened constraint: the radius is
Euler-assembled in the gluing because `(−1)^w` carries only reality, not radius); M3c [condensed upgrade —
realize `(V, F^•, κ)` as a Clausen–Scholze condensed/analytic object, the "condensed-archimedean structure
Arakelov lacks", with `C_W` and the `(−1)^w` twist now coherent].
