# A5 in the function-field case: the anchor is a FALSE WELD (2026-06-06)

**Item (AGENDA NEXT #1, [ANCHOR · load-bearing]):** Verify A5 in the function-field case. A5
(`research/work/F-sym2-os-bridge.md`, pass two) claims: over `𝔽_q`, the **self-intersection number on
`C×C` that produces the Weil square root `|α|²=q → |α|=q^{1/2}`** IS a **Rankin–Selberg / Petersson-norm
analog** (`‖f‖² = Res_{s=1} L(s, f×f̄)`). The agenda flagged: *if A5 fails where everything is provable,
the sym²→surface reduction is wrong.*

**Module:** `scripts/numerics/witness/a5_function_field.py` (exact integer intersection numbers, no bare
floats; `mpmath` only for the `√q` Weil-bound check). Verdict reproduced below.

---

## What is actually true over `𝔽_q` (THEOREMS) [THM]

**Weil's RH proof on `C×C`** uses these intersection numbers (Hartshorne V; Hindry–Silverman App.;
Lorenzini):
- `Δ·Δ = 2−2g = χ_top(C)` — a **topological Euler characteristic** (deg of the tangent bundle).
- `Γ_q·Γ_q = q(2−2g)` — Frobenius scales by `q`.
- `Δ·Γ_q = #C(𝔽_q) = q+1−Σα_i` (Lefschetz).
- fibers `f₁,f₂`: `f_i²=0`, `f₁·f₂=1`, `Δ·f_i=1`, `Γ_q·f₁=q`, `Γ_q·f₂=1`.

The **square root** `q → q^{1/2}` comes from the **Hodge index / Castelnuovo–Severi inequality**:
project `Γ_q` off `⟨f₁,f₂⟩`; the form is negative-definite on the primitive part ⟹ `|Σα_i| ≤ 2g√q` ⟹
`|α_i|=√q`. Verified on concrete elliptic curves (g=1), e.g. `q=5,a₁=2`: `|α|=2.236068=√5`, RH holds.
**The factor whose root gives the line is `q = #𝔽_q = deg(Frob)` — sitting in `Γ_q·Γ_q = q·Δ·Δ` — an
Euler-characteristic-times-`q`, with NO modular form, NO `f`, NO sym² in it.**

## The decisive test [computed]

Compare, as numbers, on `E/𝔽_5` (RH holds):
- **(W)** Weil's RH-producing self-intersections: `Δ·Δ = 0`, `Γ_q·Γ_q = 0` (`g=1`), the `q` entering via
  `Γ_q·f₁ = q`. Nature: **Euler characteristic** of one curve.
- **(RS)** the honest function-field Petersson/Rankin–Selberg residue analog: `h = #Jac(𝔽_q) = P(1) = 4`,
  a **class-number / Jacobian mass** — the `Res_{s=1} L(s,f×f̄)=‖f‖²` analog.

`(W) == (RS)?` → **FALSE.** Different numbers, different objects, different `s`-values.

## Steelman — three sophisticated readings, each still fails [THM/computed]

1. **"the `q` in `Γ·Γ` is the `|α|²`"** — true, but `q=#𝔽_q=deg Frob`, **not** a Petersson norm. A5's
   *specific identification* (self-intersection `= ‖f‖²`) is the part that fails.
2. **"the genuine self-intersection = RS-L-value theorem over `𝔽_q`"** — this EXISTS: **Yun–Zhang**,
   *Shtukas and the Taylor expansion of L-functions* (Annals 2017/2019; cf. arXiv:1512.02683,
   1707.00213): `(self-intersection of the π-isotypic Heegner–Drinfeld cycle on moduli of PGL₂-Shtukas
   with r legs) = L^{(r)}(π, 1/2)`. **BUT:** (a) it is a **DERIVATIVE at the CENTRAL point `s=1/2`**,
   not the **residue at `s=1`** that equals `‖f‖²`; (b) it lives on **moduli of Shtukas**, NOT Weil's
   `C×C`; (c) it is a **Gross–Zagier special-value formula — it does NOT prove RH** and is silent on the
   location of the other zeros (the central-value / period failure mode already demoted in
   `positivity-program.md` §C, §J: "central-value, not zeros").
3. **"`‖f‖²` IS an Arakelov self-intersection"** — true (Petersson norm = a height of a metrized Hodge
   bundle / cycle, Bost–Kühn), but that self-intersection sits at **`s=1` (the edge)** — exactly Worker
   E's edge quantity, which is **RH-silent**. It does **not** carry the square root forcing `Re s=1/2`.

**NET (the located failure).** A5 welds two mechanisms that, in the function field where everything is
provable, are **separately real but DISTINCT theorems on DISTINCT spaces about DISTINCT `s`-values**:

| mechanism | object / space | what it computes | forces the line? |
|---|---|---|---|
| Hodge-index square root `q→q^{1/2}` | `Δ,Γ_q` on `C×C` | Euler char `2−2g`, times `q` | **YES** (this is RH) |
| Petersson/RS residue `‖f‖²` | Arakelov cycle (s=1) / Shtukas (s=1/2) | an L-VALUE (residue or `L^{(r)}(1/2)`) | **NO** (Gross–Zagier, RH-silent) |

A5 demands **one object that is both** the line-forcing square root **and** `‖f‖²`. **No such object
exists over `𝔽_q`.** A5's central identification is a **false weld** of the RH mechanism onto the
RS-period mechanism.

## Falsifier verdict (the three axes, applied to A5 as a candidate forcing structure)

A5 is the *anchor of a construction program*, not a numeric positivity, but scored on the axes its
honest status is exactly the audit's recurring pattern:
- **Euler-borne:** the `‖f‖²` half is Euler-borne (no sym² for DH). ✓ for that half.
- **sees-zeros:** the `‖f‖²` half is an L-VALUE (residue at `s=1` / derivative at `s=1/2`) —
  **RH-SILENT** (Gross–Zagier-type); the line-forcing half (Hodge index) has NO Euler product.
- **independent:** the Hodge-index half is unconditional; but it is the genuinely-different object.

So A5 is the same **edge/central-value vs line** split the program has hit 8 times — now confirmed *at
the function-field archetype itself*. **The analogy the bridge leans on does not hold where it is
checkable.** [Tag: this is the **9th** confirmation of the standing wall, and the **first** that
locates the wall *inside the function-field model*, not just over `ℤ`.]

## Consequence for the program

The F-sym2-os-bridge "pass two" lemma — *"A5 + Hodge index ⟹ RH, the same one-line Weil argument with
the input pinned: the positive self-intersection it needs IS the Petersson norm"* — is **unsound at its
premise**: the self-intersection the Weil argument needs is the **Euler-characteristic-borne `q`-factor**,
NOT `‖f‖²`. Pinning the surface's self-intersection to `‖f‖²` is pinning it to the **wrong number**.
The reduction "RH ⟸ a self-product surface whose self-intersection is `‖f‖²`" inherits this: such a
surface, if built, would compute an **L-value (RS residue/derivative)**, which is **RH-silent** — it
would NOT reproduce Weil's line-forcing argument.

**This requires backing up to pass-two and re-choosing the axiom** (added to AGENDA, HIGH priority).

---
### Sources
- A. Weil, intersection-theoretic RH proof; exposition: Hartshorne *Algebraic Geometry* V; Hindry–
  Silverman *Diophantine Geometry* App. A; D. Lorenzini, *Invitation to Arithmetic Geometry*.
- Survey: B. Poonen / N. Katz expositions of "RH over finite fields, Weil to present" (arXiv:1509.00797).
- Z. Yun, W. Zhang, *Shtukas and the Taylor expansion of L-functions*, Ann. of Math. (arXiv:1512.02683,
  1712.08026); *A Gross–Kohnen–Zagier formula for Heegner–Drinfeld cycles* (arXiv:1707.00213).
