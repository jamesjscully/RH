# Complex-structure / Hermitian self-pairing — the named next axiom (NEXT #1/#2)

**Date:** 2026-06-06. **Item:** AGENDA NEXT #1/#2 (CONSTRUCT, load-bearing). Build the **complex
structure `J` (`J²=−Id`)** that the real FE-invariant archimedean metric lacks, so `AJ` is genuinely
**antisymmetric** (a Hermitian intersection form, the Kähler/Hodge `(1,ρ−1)` proper). Decisive test:
does the Hermitian inertia **FLIP** on-line vs off-line with the FE-forced Weil pair, where every REAL
form (symmetric `TᵀAT`, real-θ-twisted `TᵀAΘT`) was congruence-LOCKED?

Module: `scripts/numerics/witness/complex_structure_pairing.py`. Tags **[THM]/[computed]/[CONJ]**.

## What was built (and certified EXACTLY)

The real θ-twist closed because the archimedean Gram `A` is **FE-invariant** (`ΘAΘ=A` exact), which
forces `AΘ` symmetric (`antisym(AΘ)=0` exact) — a real twist carries **zero phase**. The repair the
agenda named: a complex structure `J` with `J²=−Id`, **`A`-orthogonal** (`JᵀAJ=A`), so that the
Kähler form `ω := AJ` is genuinely antisymmetric.

**[THM] The exact Kähler identity.** With `A=Aᵀ`, `(AJ)ᵀ=JᵀA`. If `J` is `A`-orthogonal and
`J²=−Id` (so `J⁻¹=−J`), then `JᵀA = (JᵀAJ)J⁻¹ = AJ⁻¹ = −AJ`, i.e. **`AJ` is antisymmetric** — exact.

**[computed] `A` is INDEFINITE** (`sig(A)=(4,4,0)`, `(6,4,0)`, …): the archimedean density
`Re ψ(¼+ir/2)` is **not sign-definite**, so `A^{1/2}` does not exist as a real metric. This is itself
load-bearing (`A` is a pseudo-metric, not Riemannian). I therefore built the `A`-orthogonal complex
structure for the **indefinite** `A`: write `A=BSB` with `B=V√|d|Vᵀ`, `S=V·sign(d)·Vᵀ` the signature
operator; set `J=B⁻¹KB` with `K` an **`S`-orthogonal** complex structure (`KᵀSK=S`, `K²=−Id`, built
block-wise pairing equal-sign eigendirections). Then `JᵀAJ=B(KᵀSK)B=A` and `J²=B⁻¹K²B=−Id`, both exact.

**[computed] Certification (clean even-`(p,q)` bases, dim 8 and 10):**
- `‖J²+Id‖ = 2.0e-14` / `4.1e-14` (J²=−Id).
- `‖JᵀAJ−A‖ = 3.4e-14` / `8.6e-14` (J exactly `A`-orthogonal). *(Raw FE block-`J₀` is NOT
  `A`-orthogonal: `‖J₀ᵀAJ₀−A‖=5.9` — because `A` is not block-diagonal in the FE planes; the
  `A`-compatible construction is essential.)*
- `‖sym(AJ)‖ = 5.0e-15` / `4.9e-14` (ω=AJ **exactly antisymmetric**) while `‖antisym(AJ)‖ = 6.14` /
  `7.65` — **the phase the real twist could not carry** (`antisym(AΘ)=0` exact, recomputed here).
- **`‖[A,J]‖ = 6.48` ≠ 0** — `J` does NOT commute with `A`, unlike the real `Θ` (which DID commute,
  the relocation obstruction). So `J` genuinely escapes the predicted "commute-and-relocate" trap.
- `H = A + iω` is exactly Hermitian (`‖H−H†‖ = 1.0e-14`).

The dim-6 basis has `(p,q)=(3,3)` **odd**, where my block construction leaves a small residual
(`‖JᵀAJ−A‖=0.33`); the two even-`(p,q)` bases (dim 8, 10) are the exact, load-bearing cases.

## The decisive falsifier (C4) — and the precise obstruction

Plant the FE-forced Weil pair `(β,1−β)` in the prime-shift correspondence `T`, restrict to `J`'s
support, and take the inertia of the Hermitian self-pairing `Tᵀ H T` (and of the holomorphic
projection `((Id−iJ)T)† A (Id−iJ)T`). The plant couples strongly to `J` (`‖[T,J]‖≈20`) and
`det T≠0` (`≈1.7e-6`).

**[computed] NO FLIP.** Robust across the two clean bases:
- dim 8: Hermitian inertia `(2,2,4)` on-line **=** `(2,2,4)` off-line; holo `(2,2,4)` = `(2,2,4)`.
- dim 10: Hermitian inertia `(3,2,5)` = `(3,2,5)`; holo `(3,2,5)` = `(3,2,5)`.

(Baselines, same support: real-symmetric `(4,4,0)`=`(4,4,0)` and `(6,4,0)`=`(6,4,0)`; real-θ-twist
`(4,4,0)`=`(4,4,0)` and `(5,5,0)`=`(5,5,0)` — all congruence-locked, as before.)

**[THM] WHY — the precisely-named obstruction (Sylvester for Hermitian forms).** The agenda hoped the
Hermitian form's inertia is "NOT congruence-preserved". **That hope is false.** Sylvester's law of
inertia holds for Hermitian forms under any invertible **`*`-congruence**: `inertia(T*HT)=inertia(H)`
for `det T≠0`. The prime-shift correspondence `T` is **REAL**, so `TᵀHT = T*HT` is a `*`-congruence,
and the inertia is locked to `inertia(H)`. Verified directly (`inertia(T_on·H·T_onᵀ)=inertia(H)` for
both plants) and on a generic Hermitian `H` (random real `Tr`: `inertia(TrᵀHTr)=inertia(H)` exactly;
only a **complex non-`*` `T`-congruence** moves it — but that produces a non-Hermitian matrix, the
wrong object). And `inertia(H)` is built from the **DH-shared `A`** (`max|A_ζ−A_DH|=0`) and the
FE-derived `J` (also FE/metric data) — so it is **DH-shared, RH-silent**.

**Verdict: Euler-borne YES (`op_diff≈1.80`), sees-zeros NO (no inertia flip), independent NO →
RH-SILENT.** **24th Euler-product confirmation.**

## The decisive lesson (the obstruction, sharpened past the real-twist wall)

The complex structure `J` does everything the agenda asked: `J²=−Id`, `A`-orthogonal, `ω=AJ` genuinely
antisymmetric (real phase the real twist could not carry), `[A,J]≠0` (escapes commute-and-relocate).
**It still fails to see the line, for a reason STRONGER than "FE-invariance kills real twists":**

> **Sylvester's law of inertia is identical for Hermitian forms.** A real plant `T` self-pairing a
> fixed Hermitian `H` is a `*`-congruence, so `inertia(TᵀHT)=inertia(H)` — locked to the DH-shared
> `A,J` data, blind to where `T`'s eigenvalues (the zeros) sit. Promoting the form from **symmetric**
> to **Hermitian** does NOT escape the congruence-lock; it only enlarges the fixed background `H` whose
> inertia the real plant cannot move.

This unifies the whole self-pairing thread (DONE: symmetric `TᵀAT`, real-θ-twist `TᵀAΘT`, now Hermitian
`TᵀHT`) under ONE named wall: **any self-pairing of the form `(plant)ᵀ (fixed DH-shared form)(plant)`
is inertia-locked by Sylvester** — symmetric OR Hermitian. The line-content (a flip) requires the form
the plant pairs against to itself **depend on the plant's eigenvalue locations** (the zeros), i.e. the
zeros must enter the *form*, not just the *congruence factor*. That is exactly the Weil
explicit-formula coupling `W_∞ ≥ Σ_p W_p` — the standing wall — now reached from the
complex-structure/Kähler side.

**The complex structure is NOT the missing degree of freedom for line-detection.** Phase (the
antisymmetric `ω`) is real and genuinely present in `H`, but it sits in `H`'s **fixed inertia**, which
a real congruence cannot vary. The `(1,ρ−1)` signature cannot be made plant-sensitive by ANY
`J`-Hermitian self-pairing of a DH-shared form.

## Honest subtleties
- Coarse chiral Gaussian bases (support dim 6–10); the load-bearing EXACT facts are `J²=−Id` and
  `JᵀAJ=A` (`~1e-14`, the two even bases), `sym(AJ)=0` / `antisym(AJ)≠0`, `[A,J]≠0`, `det T≠0`,
  `inertia(TᵀHT)=inertia(H)` (verified directly AND structurally via Sylvester-Hermitian), and no
  on/off-line flip. The dim-6 odd-`(p,q)` case carries a small `0.33` orthogonality residual (noted).
- `A`'s indefiniteness (`A^{1/2}` nonexistent) is a genuine finding: the archimedean pseudo-metric is
  not a Kähler metric in the positive-definite sense — the Hodge `(1,ρ−1)` structure it could carry is
  the indefinite (Lorentzian-type) one, consistent with the single `+` of the arithmetic Hodge index.
