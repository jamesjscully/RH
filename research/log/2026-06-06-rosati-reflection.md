# The unified axiom IS the Rosati reflection — and the wall is one off-diagonal entry (2026-06-06)

Task (AGENDA NEXT #1): re-run `method.md` step 2 with the **unified axiom** — *(sym² coefficients form
a norm-square at the edge `s=1`) ⟹ (the `H¹_prim` intersection form is negative-definite / the OS form
is positive at `s=½`)* — attacking the **single shared positivity**, using the named lever: **Rosati
positivity `F*F=q` is a THEOREM over `𝔽_q`; what is its `ℤ`-analog?** Decisive question:
**is there a reflection/involution under which the edge norm-square becomes the negative-definite
primitive form at the centre?**

Module: `scripts/numerics/witness/rosati_reflection.py` (+ `falsify.py` registry row). Tags: [THM]
(Rosati positivity over `𝔽_q`, Weil), [computed] (the executable edge→centre chain), [CONJ] (the
`ℤ`-analog).

---

## The answer to the decisive question: YES — the reflection is the Rosati involution, and it is a THEOREM over `𝔽_q`

Made the function-field archetype **executable end to end** (`q=7`, elliptic curve, all checks exact):

1. **EDGE NUMBER [THM, unconditional].** The Rosati identity `F·F' = q = deg(Frob)`, where `F'` is the
   Rosati adjoint (eigenvalue `q/α`). Verified `α·(q/α)=q` exactly for every eigenvalue — *true
   off-line too* (it is the degree, not RH). **This is the function-field `‖f‖²`:** both are "the
   norm-square at the edge" (`F·F'=q=deg`; `‖f‖²=Res_{s=1}L(s,f×f̄)`).

2. **THE REFLECTION [THM].** `θ(α)=q/ᾱ` is the Rosati involution on eigenvalues `=` the functional
   equation `s↦1−s`. Its **fixed locus is exactly `|α|=√q ⟺ Re s=½`** (`|θ(α)−α|=6e-16` on-line).

3. **THE LEVER [THM over `𝔽_q`].** The Rosati trace form `⟨φ,ψ⟩=Tr(φψ')` restricted to `span_ℝ{Id,F}`
   is the `2×2` Gram `M=[[2,a],[a,2q]]` (with `a=Tr F`), and **`M ⪰ 0 ⟺ a²≤4q ⟺ |α|=√q ⟺` RH for the
   curve.** Computed the full edge→centre chain on 5 planted curves over `𝔽_7` — on-line (`a=1,5`),
   the boundary (`a²=4q`, det`=0`, semidefinite), and off-line (`a=6,7`, det`<0`): **positive-
   SEMIdefiniteness tracks the line in all 5 cases** (semidef `⟺` on-line, including the boundary).
   So the Rosati positivity, sourced by the edge degree `F·F'=q`, **SEES THE ZEROS by construction**.

**Conclusion (step 1+2, the mechanism named).** The reflection the agenda asked for **exists and is the
Rosati involution**; "the edge norm-square becomes the negative-definite primitive form at the centre"
is, in the function field, **literally a theorem**: positive-definiteness of the Rosati trace form
(= `−1×` the primitive intersection form, DONE #1) is sourced at the edge by `F·F'=q` and forces
`|α|=√q` at the centre. The two threads (geometric Hodge-index, analytic OS/sym²) and the reflection
mechanism are **one and the same Rosati positivity**.

## Where the implication holds, and where it must be supplied (the `ℤ`-analog audit)

| link | `ℤ`-analog | status |
|---|---|---|
| (i) edge number `F·F'=q` | Petersson residue `‖f‖²=Res_{s=1}L(s,f×f̄)>0` | **AVAILABLE, unconditional** (Siegel bound, Worker E) — the `s=1` diagonal `⟨Id,Id⟩` |
| (ii) reflection `θ`=Rosati | functional equation `s↦1−s`, fixed locus `Re s=½` | **AVAILABLE, unconditional** — but acts on the **spectral parameter only**, not on an algebra of correspondences (no surface over `ℤ`) |
| (iii) **Rosati positivity** `Tr(φφ')>0` | pos-def of the Rosati Gram `[[⟨Id,Id⟩, Tr F],[Tr F, ⟨F,F⟩]]` | **THE WALL = RH** |

**The one open implication, named to a single matrix entry.** Both `ℤ`-ingredients of the reflection
transfer — the edge diagonal `‖f‖²` (have it) and the reflection FE (have it). What is missing is the
**OFF-DIAGONAL cross term `Tr(F)=a`**, coupling the edge-norm `Id` to Frobenius `F`. The edge
norm-square supplies only the **diagonal `⟨Id,Id⟩`** of the Rosati Gram; the line `a²≤4q` needs the
**whole `2×2`**, hence the off-diagonal. **The reflection `θ`=FE does NOT manufacture a positive matrix
from one positive diagonal entry.**

That off-diagonal `Tr(F)` **is** the cross-place coupling `W_∞ ≥ Σ_p W_p` / the explicit formula / the
primes — the standing wall, now re-derived from the Rosati form and **pinned to a named entry**.

## Falsifier verdict [computed]

Candidate: *RH `⟸` the Rosati Gram `[[‖f‖²-analog, Tr F],[Tr F, ⟨F,F⟩]]` positive-definite.*

- **Euler-borne — YES.** Built on `F`=Frobenius/Hecke (Satake) and the edge `‖f‖²`=sym² residue;
  neither exists for Davenport–Heilbronn (no Euler product). Same DH-refusal as the sym²/signature
  candidates.
- **sees-zeros — YES.** Positive-semidefiniteness tracks the line exactly over `𝔽_q` (det `=4q−a²≥0
  ⟺ |α|=√q`, all 5 planted cases). The off-diagonal `Tr(F)` **is** the eigenvalue location.
- **independent — NO.** Over `𝔽_q` it is the Hodge-index theorem on `C×C`; over `ℤ` the full `2×2`
  positivity (`a²≤4q`-analog) is exactly RH. The diagonal `‖f‖²` is unconditional; the off-diagonal
  is the wall.

**VERDICT: CIRCULAR** (= Weil positivity over `ℤ`), the **same box** as the signature / Weil–Li form.
**12th Euler-product confirmation.** New, sharper content: the unified axiom's missing piece is now a
**single named matrix entry** — the off-diagonal Rosati coupling `Tr(F)` — and RH is the
**Cauchy–Schwarz inequality `|Tr F|² ≤ ⟨Id,Id⟩·⟨F,F⟩`** that the primes must satisfy. The reflection
`θ`=FE turns the edge norm-square into the centre form **only if** that off-diagonal is supplied; the
reflection alone does not.

## Honest status — what this is and is not

This does **not** prove the implication; it is CIRCULAR. But the loop did its job (method.md
discipline): it converted "is there a reflection carrying edge→centre?" into a sharp **YES, the Rosati
involution**, executable, sees-zeros — and then **located the gap to one off-diagonal entry**. The
edge→line wall is unmoved but **re-posed as a Cauchy–Schwarz on the Rosati Gram**: have the diagonal
(`‖f‖²`, unconditional), have the reflection (FE), need the off-diagonal `Tr(F)` bound. This is strictly
sharper than "make the OS form positive": it names *which* coupling, and that it is exactly the primes.

## Two subtleties recorded honestly

- **Semidefinite, not definite, on the line.** RH for the curve is `a²≤4q` = positive-*semi*definite
  (the boundary `a²=4q`, supersingular, has det`=0`, on-line). Strict definiteness is `a²<4q` (strictly
  inside). The correct tracking statement is **semidefiniteness `⟺` on-line** — fixed in the module
  (an earlier draft used strict definiteness and mis-flagged the boundary).
- **The reflection acts on `s`, not on an algebra over `ℤ`.** Over `𝔽_q` the Rosati involution permutes
  *actual correspondences* in `End(Jac)`; over `ℤ` the FE involution acts only on the spectral
  parameter — there is no `End(S²/ℤ)` for it to be an algebraic involution on. This is the first crack
  and is why the off-diagonal `Tr(F)` (which over `𝔽_q` is `Tr` of a genuine endomorphism) has no
  unconditional `ℤ`-definition: **the missing off-diagonal entry and the missing algebra-of-
  correspondences are the same gap.**
