# M3 — the archimedean Hodge polarization `P_∞`: the `(p,q)` duality datum at `∞`, no Frobenius [INVENT · anchored vs polarized-HS]

**Charter:** `construction-program.md` §1 clause C2 (`(p,q)` grading + `c`), C4 (`P` = canonical pairing
of `D`), §0 design law (the polarization is the duality pairing, **never a metric**), §5 M3 (*invent the
one genuinely new structure — the archimedean Hodge polarization that supplies the reality/phase, check
it is NOT a `*`-congruence*). **Contract:** `M1-universal-property-S_Z.md` (the quadruple `(𝒞, ω_∞, D, P)`
must carry, at `∞`, a `(p,q)` grading whose conjugation `c` is part of the structure). **Built on:** M2 /
M2c′ / M4C — which built `(𝒞, ω_∞, D, P)` as a coherent rigid `(p,q)`-graded tensor object **but only on
the FF anchor**, where `c` and the Weil operator were *borrowed from Frobenius*. **Module:**
`scripts/numerics/witness/archimedean_hodge_polarization.py`
(run: `python3 -m scripts.numerics.witness.archimedean_hodge_polarization`). **Falsifier row added** (`falsify.py`).

---

## The gap M3 fills — strip Frobenius off the conjugation

On the FF anchor the Hodge conjugation `c` and the Weil/`(p,q)` operator were *modeled through the
Frobenius spectrum*: `c : α ↦ ᾱ`, coinciding with the duality `D : α ↦ q/α` **exactly on the circle**
`|α| = √q` (M2c′ B4: `c = D ⟺ RH`). That is fine over `𝔽_q` — there is a Frobenius. **At the archimedean
place `∞` there is no Frobenius.** The `(p,q)`/reality datum cannot be read off a Frobenius spectrum; it
must be **invented intrinsically**, from a Hodge structure alone, and — by the §0 design law — its
polarization must be the **canonical pairing of the duality, never a `*`-congruence of a chosen metric**.

This is the *one genuinely new structure* §5 M3 asked for: the archimedean reality/phase carrier.

---

## [DEF] The archimedean Hodge datum `(V, F^•, D, W, c, P_∞)`

| symbol | datum | role |
|---|---|---|
| `V` | finite-dim `ℂ`-space with a **real structure** `V = V_ℝ ⊗ ℂ`, conjugation `κ` | the carrier |
| `F^•` | a decreasing Hodge filtration; weight-`w` decomposition `V = ⊕_{p+q=w} V^{p,q}`, `κ(V^{p,q}) = V^{q,p}` | the `(p,q)` grading |
| `D` | a **structural (Serre/Verdier) duality** `D : V → V^∨(−w)`, non-degenerate, `(−1)^w`-symmetric | the FE / cup-product pairing **as a morphism** (the archimedean analogue of `E`) |
| `W` | the **Weil operator** `C_W = i^{p−q}` on `V^{p,q}` | the `(p,q)` grading **made an operator** — the reality/phase the FF borrowed from Frobenius, now supplied by `(p,q)`, **no base field, no `q`** |
| `c` | the Hodge conjugation `= κ` (anti-linear, `V^{p,q} → V^{q,p}`) | **intrinsic** — it is the real structure, not Frobenius |
| `P_∞` | the **archimedean Hodge polarization** `P_∞(x,y) := S(C_W x, κ y)`, where `S(x,y) = ⟨x, D y⟩` | the **Hodge–Riemann form** |

**The polarization.** `P_∞(x,y) = S(C_W\,x,\,κ y) = \mathrm{ev}\circ(1\otimes D)\circ(C_W\otimes κ)(x,y)`.
In matrices: `P_∞` is the Hermitian form `H = C_W^† S` (with `S` the antisymmetric cup product), and
`x^* H x = S(C_W x, \bar x)` is the classical Hodge–Riemann quantity.

**The design-law point (§0), made structural.** Every ingredient of `P_∞` is *forced* by the Hodge datum:
`S = ⟨·, D·⟩` is the duality, `C_W` is fixed by the `(p,q)` grading, `κ` is the real structure. **No inner
product is ever chosen.** `P_∞` is the canonical pairing of `D` pre-composed with `C_W` and `κ` — exactly
the FF's C4 (`P = ev∘(1⊗φ_FE)`, M2/M4C), now at `∞` with `C_W` in place of the Frobenius-borrowed
conjugation. The Hodge–Riemann bilinear relations then make `P_∞` **positive-definite on the primitive
part** — but that positivity is a *property of the canonical pairing*, not the choice of a metric.

---

## [BUILT] The anchor — a weight-1 polarized Hodge structure reproduces the solved case

The minimal nontrivial model: `V = H^1(C)` of a genus-`g` curve at `∞`, `V = H^{1,0} ⊕ H^{0,1}`, `κ` the
real structure swapping them, `S` the symplectic cup product `J = \begin{psmallmatrix}0&I\\-I&0\end{psmallmatrix}`,
`C_W = i` on `H^{1,0}`, `−i` on `H^{0,1}`. `H^{1,0}` is the column span of a Riemann period matrix `[I; Z]`,
`Z = X + iY`, **`Y > 0`** (Riemann's second bilinear relation = the polarization condition).

**Four EXACT anchor facts** (`g = 1, 2, 3`, multiple seeds — `numpy`, residuals to machine precision):

1. **ANCHOR — Hodge–Riemann positivity.** `P_∞` restricted to `H^{1,0}` is **positive-definite**
   (`min eig = +2.03, +3.35, +4.72, …  > 0` all `g`/seeds) — the classical weight-1 Hodge–Riemann /
   Riemann bilinear relation (`i·S(x, x̄) > 0` for `0 ≠ x ∈ H^{1,0}`), the abelian-variety / Jacobian
   positivity, **reproduced**.

2. **DESIGN-LAW (§0).** `H = C_W^† S` **exactly** (factor residual `0.0e+00`): `P_∞` IS the canonical
   pairing of the duality `S` twisted by `C_W` and `κ`, *no chosen metric*. And `S` is the
   **antisymmetric** cup-product duality (`‖S + Sᵀ‖ = 0.0e+00`, `Sᵀ = −S`) — exactly what a metric
   (`S = Sᵀ`) is **not**.

3. **§0 NO-GO ESCAPE — `P_∞` reads the `(p,q)` TYPE.** With the duality `S` *fixed*, sweep Riemann's
   second relation: `Y > 0` (polarized, `P_∞ = +2.03`) → `Y = 0` (the filtration degenerates,
   `H^{1,0}=H^{0,1}`) → `Y < 0` (anti-polarized, `P_∞ = −2.03`), a **monotone flip**, all `g`. The
   positivity of `P_∞` is **moved by the Hodge type**, not by a `*`-congruence — the archimedean analogue
   of "moved by the zero location". **No `*`-congruence `x^* A x` of a fixed (DH-shared) background `A`
   can produce this flip** (Sylvester-immune *by construction*: there is no fixed `A` with a variable
   plant; **the `(p,q)` grading itself is the variable**). This is precisely the §0 design law satisfied:
   the polarization is not a congruence of a fixed archimedean background.

4. **FROBENIUS LIMIT — recovers the FF `c` with `q` stripped.** `κ` swaps the Hodge lines
   `H^{1,0} ↔ H^{0,1}` (`‖P_{10}∘κ(H^{1,0})‖ = 0.0e+00 / 1.8e-15`), i.e. it IS the FF's `c` exchanging the
   Hodge lines (M2c′ B2), **with the weight `q` removed.** On the unit circle `α = e^{iθ}` (the FF circle
   `|α| = √q` rescaled to radius 1) the archimedean `κ = (\,\bar{\cdot}\,)` coincides with the FF
   conjugation; the archimedean datum is the FF's `c` *without the Frobenius weight* — exactly the
   deformation `ℤ` needs, since **`ℤ` has no Frobenius weight** and the critical radius `Re s = ½` must come
   from the archimedean `(p,q)` structure, not from a `q` (the open hinge C3b).

---

## Why this is the right archimedean object (and what it deliberately does NOT do)

- **It is `(p,q)`/condensed, not metric.** The reality/phase is carried by the *Weil operator* `C_W` (a
  grading operator) and the *real structure* `κ` — categorical data — and the pairing is the duality `S`,
  not a Hilbert metric. This is the "duality Arakelov lacks" (§2 Pillar A): Arakelov *chooses* an
  archimedean metric (→ a `*`-congruence → Sylvester-dead, §0). `P_∞` chooses nothing.

- **Its positivity is the Hodge index, formally.** On the anchor, `P_∞ > 0` on primitives is the
  Hodge–Riemann relation — a *theorem*, the same one M2 reproduced for the FF, now seen as the
  archimedean `(p,q)` statement. This is Pillar C ("positivity from coherence") on the archimedean half.

- **It is deliberately Euler-SILENT.** `P_∞` *alone* is the place at `∞` — the `Γ`-factor — which is
  **DH-shared** (the functional equation's archimedean factor is the same for `ζ` and Davenport–Heilbronn).
  M3's job is the **reality/phase carrier**, *not* Euler-discrimination. The Euler content — the
  cross-place coupling `W_∞ ≥ Σ_p W_p` — enters only at **M4 (descent)**, when `P_∞` is glued to the prime
  Euler factors. We record this honestly: M3 builds the **archimedean half**; it is **not** a standalone
  RH-form and must not be scored as one.

---

## Falsifier verdict (M3 — an INVENTED + ANCHORED archimedean datum; the `ℤ`-deformation is the open C3b/M4)

- **EULER-ASSEMBLED — NO, BY DESIGN.** The archimedean datum is the `Γ`-factor at `∞`, **DH-shared**. As
  a standalone it does *not* distinguish `ζ` from DH — and that is the whole point: it is the reality/phase
  half, whose Euler content is M4's gluing. Tabled `DISPERSING`-by-design (`euler_borne = False`), with
  the explicit note that scoring it as a finished RH-form would be a category error.
- **SEES-ZEROS — YES** (the Hodge-type analogue): `P_∞`'s positivity flips with the `(p,q)` type
  (`Y > 0 → Y < 0`).
- **INDEPENDENT — NO** on the anchor: Hodge–Riemann positivity IS the Riemann relations (= the solved case).

**NEW content (not circular):** the `(p,q)`/reality datum at `∞` is **invented Frobenius-free** as the
**Weil operator `C_W` + real conjugation `κ`**, with `P_∞` the **canonical duality pairing** (§0-clean,
NOT a metric, `H = C_W^† S` exactly) whose positivity **reads the `(p,q)` type** and whose **Frobenius
limit recovers the FF `c`** (`q` stripped). This is the well-typed archimedean input that M4's descent
must glue to the prime Euler factors — the missing piece M2c′ named ("the well-typed target M3's
archimedean `(p,q)`/condensed datum deforms into").

---

## Verdict

`[INVENT · anchored vs polarized-HS]` — the **archimedean Hodge polarization** `P_∞(x,y) = S(C_W x, κ y)`
is defined intrinsically (no Frobenius), with the `(p,q)` grading carried by the **Weil operator
`C_W = i^{p−q}`** and the reality by the **real-structure conjugation `κ`**. Four EXACT facts on the
weight-1 polarized-HS anchor (`g = 1, 2, 3`): **(1)** `P_∞` positive-definite on `H^{1,0}` (Hodge–Riemann,
reproduced); **(2)** `P_∞ = C_W^† S` exactly — the **canonical pairing of the duality**, NO metric, `S`
the antisymmetric cup product (`Sᵀ = −S`, what a metric is not); **(3)** `P_∞` reads the **Hodge type**
(`Y > 0 → Y < 0` flips positivity, the §0 NO-GO escape — Sylvester-immune by construction, the `(p,q)`
grading is the variable); **(4)** the **Frobenius limit** recovers the FF `c` with `q` stripped. **Not
overclaimed:** an invented + anchored archimedean datum, **Euler-silent by design** (the `Γ`-factor is
DH-shared) — the reality/phase half, whose Euler content is M4's descent. **Successors named:** M4 (the
duality-descent gluing of `{Euler factors at primes} ∪ {P_∞ at ∞}` into the global weight-2 NS
polarization; the single hinge C3b = how the Euler assembly sets the centre `Re s = ½` the way `q` set `√q`,
now that the archimedean `Re s = ½`-side datum `P_∞` exists Frobenius-free); M3b [coherence — prove
`P_∞` is functorial in the Hodge datum and the **Weil operator `C_W` commutes with the duality `D` up to
the Tate twist `ℚ(−w)`**, the archimedean analogue of M2c′ (B), so `(P_∞, D, c)` is a coherent triple at
`∞`]; M3c [condensed-archimedean upgrade — realize `(V, F^•, κ)` as a **condensed/analytic** object so the
"condensed-archimedean structure Arakelov lacks" (§2 Pillar A) is explicit, not just finite-dim linear
algebra].
