# NG candidate 3 — the *-autonomous / C*-categorical / Hermitian-self-duality escape — NO-GO COMPLETION

**Charter.** `research/new-geometry-program.md`; blueprint from candidate 2
(`research/construction/NG-frob-synthesis.md` §5): the no-go proof becomes a theorem iff one shows
**"no categorical coherence theorem emits a SIGN (a positive self-duality) from a SIGN-FREE
non-degenerate self-duality."** Candidate 3 is the one place positivity might be **built into the
duality** rather than imported as a fiber functor: demand a **HERMITIAN self-duality** — a
*-autonomous / dagger-compact / **C*-tensor** category with a conjugate-linear dualizing pairing
that is **positive by axiom**. The real theorem to engage is **Doplicher–Roberts**: a symmetric
**C*-tensor** category with conjugates reconstructs a **COMPACT** group — literally "compactness
from the duality." Decisive question: does ζ's Frobenius datum form a **C*-category WITHOUT
assuming the radius**, or is "C*" = "positive" = "on-line" = RH (circular)?

**VERDICT: NOGO_COMPLETE.** Positivity is **IMPORTED** (EXTRA), not forced. The *-autonomous /
Hermitian self-duality is **CONSISTENT off-line** as an **indefinite (Krein) *-structure**; the
C*/dagger/polarization positivity is a **strict extra restriction** to the positive-definite
subclass. Demanding "C*" of ζ's datum **is** demanding the radius (= RH) — the Doplicher–Roberts
circularity, now made exact. This is the **third independent instance of the geometric no-go**, and
it closes the single door candidate 2 named: **a non-degenerate self-duality carries no canonical
sign; the sign (positivity) is always the import.**

---

## 1. The structure DOES apply to the Frobenius datum — and it splits exactly at positivity

The *-autonomous / dagger / C* layer is real and applies, but it **factors into two strata**, and
the literature names the split precisely:

- **Anti-involution / *-structure (Hermitian, conjugate-linear) — Step A, FREE.** A `*`-structure
  is an anti-involution / non-degenerate conjugate-linear (Hermitian) pairing. **Stehouwer–
  Steinebrunner, *Dagger categories via anti-involutions and positivity* (arXiv:2304.02928):** an
  anti-involution alone permits **indefinite / Krein-type** structures; it does **not** enforce
  positive-definiteness. The dagger/C* category is built by taking the Hermitian completion **and
  then RESTRICTING to the positive-definite subclass** — positivity is a **separate axiom**, not
  automatic from the *-structure.
- **C* / dagger / polarization (positive-definite) — Step B, the IMPORT.** Only the extra
  positive-definiteness gives a C*-category. **Doplicher–Roberts** (nLab; Deligne–Milne polarization
  theorem): a **symmetric C*-tensor category with conjugates** → a **compact** group; **Deligne**'s
  polarization = a **Weil form** `φ` with `Tr(u·u^φ) > 0` (the positivity) → neutral fiber functor
  with `Aut^⊗(ω)` **compact**. Compactness is the **consequence of the positivity**, not of the
  bare duality.

So the *-categorical structure **builds positivity into the duality ONLY when you upgrade
anti-involution → C*** — and that upgrade is exactly the polarization-positivity candidate 2 found
imported. The structure applies; it does **not** manufacture the sign.

## 2. The decisive witness — off-line is a CONSISTENT Krein *-category (positivity is extra)

`scripts/numerics/witness/cstar_hermitian_witness.py` (anchor `q`, FE-paired data). The honest
test: take an off-line `F` that **satisfies Step A** (the FE-pairing `α ↔ q/ᾱ`, which candidate 2
proved holds off-line), normalize `U = F/√q`, and construct the **maximal `U`-invariant
non-degenerate Hermitian form `g`** (`U* g U = g`) — the conjugate-linear dualizing pairing of the
*-autonomous / Hermitian self-duality. Read its **inertia**.

| case | `|eig|/√q` | Hermitian self-duality `g` exists, non-deg | signature `(n₊,n₋)` | **positive-definite (C*)** |
|---|---|---|---|---|
| ON-LINE `|α|=√q` | all `=1` | **True** | `(6,0)` | **True** |
| OFF-LINE (FE-paired) | spread `≠1` | **True** | `(3,3)` **indefinite/Krein** | **False** |
| OFF-LINE (ratio 1.3) | spread `≠1` | **True** | `(3,3)` **indefinite/Krein** | **False** |

Invariance error `|U*gU − g|/|g| ~ 1e-15` — the off-line Krein *-structure is **exact**, not noise.
**Robustness sweep** `q ∈ {4,7,11,13,25}`, `d ∈ {4,6,8}`, 4 seeds: on-line **always** `(d,0)`
positive-definite; off-line FE-paired **always** indefinite `(k,k)`. Structural, not an artifact.

**The mechanism (Sylvester inertia, predicted by `the-complete-account.md` §3/§5):** an honest
Frobenius/Weil datum carries eigenvalue FE-pairs `{α, q/ᾱ}`. The invariant Hermitian form pairs the
eigenvector of `μ` with that of `1/μ̄` (`μ = eig/√q`). On the circle (`|μ|=1`) the pairing is
**diagonal and definite** (`+1`); off the circle (`|μ|≠1`) `μ ≠ 1/μ̄`, so the form must pair `μ`
with `1/μ̄` in a **hyperbolic `(+,−)` block** — signature 0, **indefinite**. The *-structure
**exists at every radius** (Step A free, non-degenerate); its **signature flips to indefinite
exactly off the line**. Positive-definiteness ⟺ `|α|=√q` ⟺ RH.

> **A non-degenerate (Hermitian) self-duality carries no canonical sign.** The *-autonomous /
> Hermitian layer gives the **non-degenerate** pairing for free (on AND off line); the **sign**
> (positive-definite = C* = compact = radius) is a **strict extra restriction**. This is the
> candidate-2 door — "no coherence theorem emits a sign from a sign-free self-duality" — verified
> as a **fact about the Frobenius datum**, not a conjecture.

## 3. The Doplicher–Roberts circularity, made exact

DR is the strongest possible engine for "compactness from duality" — and it is exactly where the
circularity lives:

- DR reconstructs a **compact** group from a **C*-tensor** category. The C* axiom **is** the
  positivity: norms `‖a‖² = ‖a*a‖`, the `*` gives **positive** inner products, conjugates satisfy
  the positivity/standardness conditions.
- ζ's Frobenius datum forms a **consistent *-category WITHOUT the radius** — but it is a **Krein /
  indefinite** *-category off-line (witness §2), **not** a C*-category. To call it "C*" you must
  impose positive-definiteness = signature `(d,0)` = `|α|=√q` = **on-line = RH**.
- Therefore **feeding Doplicher–Roberts a "C*-category" for ζ already presupposes the radius.**
  "C*" = "positive" = "on-line" = RH. DR delivers compactness **from** positivity; it does not
  manufacture positivity. **`C*-input ⟹ RH` is circular**; the only non-circular input is the bare
  Krein *-structure, which DR cannot consume (it requires positivity) and which is **compact-group-
  free** (the indefinite-metric / non-compact `O(p,q)`-type symmetry survives off-line).

This is the same wall as candidate 2's Tannakian polarization (Deligne Weil-form positivity) and
the audit's Sylvester-inertia lock — reached now through the *-autonomous / C* door, the one place
positivity might have been structural. It is not: **positivity is the C* axiom, and the C* axiom is
the radius.**

## 4. Anchor `F_q` and DH

- **Anchor.** Over `𝔽_q` the on-line datum `|α|=√q` makes `g` positive-definite (signature `(d,0)`)
  — the polarized/compact Sato–Tate case — recovered for every `q` without assuming the zeros. But
  positivity is downstream of `|α|=√q` (Weil II / Deligne purity), **imported into** the C*-category,
  not produced by it. The *-structure itself exists off-line too (Krein). **The radius does not
  transfer through the *-axiom; only its consequence (positivity) is read off when the radius is
  already present.** Anchor lands on the no-go side.
- **DH — FAILS in the NO-GO way.** Davenport–Heilbronn has **no Euler product ⇒ no Satake/Frobenius
  datum ⇒ no `F`** — the C*/Hermitian self-duality construction has **NO INPUT** for DH
  (input-empty / type-vacuous, same as candidates 1–2). Where a datum exists, the *-category
  distinguishes the on-line (C*) from off-line (Krein) case **only by the imported positivity**,
  never at the free Step-A self-duality. **DH-blind at Step B = NOGO**, not a healthy "fails to
  exist" gate.

## 5. Verdict — NOGO_COMPLETE (the geometric no-go gains its THIRD instance and closes)

> **The *-autonomous / dagger / C*-categorical / Hermitian-self-duality structure DOES apply to
> ζ's Frobenius datum, but it FACTORS exactly at positivity. The anti-involution / Hermitian
> (conjugate-linear) self-duality is FREE and CONSISTENT OFF-LINE — an INDEFINITE (Krein)
> *-structure, signature `(k,k)`, exact and robust across `q,d,seed`. The C*/dagger/polarization
> positive-definiteness — signature `(d,0)` = compact Galois (Doplicher–Roberts) = `|α|=√q` =
> `F†=F̄` = RH — is a STRICT EXTRA RESTRICTION to the positive-definite subclass, NOT forced by
> the *-structure. A non-degenerate Hermitian self-duality carries NO canonical sign; the sign is
> the import. Demanding "C*" of ζ's datum IS demanding the radius (circular): C* = positive =
> on-line = RH.**

`positivity_forced_or_extra = EXTRA`. `offline_test`: off-line `F` is **Hermitian-self-dual but
non-positive (Krein)** — positivity is the extra, **NO-GO**; *-autonomy does **not** make off-line
inconsistent. This is the **decided form** of candidate 2's open door: the answer to "does a
coherence theorem emit a sign from a sign-free self-duality?" is **NO — verified on the Frobenius
datum.** Three instances now in: candidate 1 imports **properness**, candidate 2 imports
**polarizability**, candidate 3 imports **the C*/positivity sign**. **All three CREATE Step A
(the free non-degenerate self-duality) and IMPORT Step B (the positive sign), at exactly the same
wall.** The geometric no-go is no longer one-door-open: the last categorical structure that might
have built positivity into the duality (the C*/Hermitian one) provably does not — it **restricts**
to positivity, and that restriction is the radius.

**The no-go is provable-shaped → now substantiated:** *no metric-free / sign-free categorical
structure forces the positive self-duality; Step B is always an imported positivity (C* = the
radius = RH).* RH is not forceable by a positivity-free geometry; the residue `ψ_∞` is precisely the
**finite ground at `∞`** that would supply the sign, which `ℤ` lacks.

## 6. Next step

Close the new-geometry program's categorical branch. The no-go now has **three concordant
instances** and the candidate-2 door is **shut** (the sign is not emitted by *-autonomy/C*). The
only remaining non-categorical escape is a **genuine finite ground / self-adjoint geometry at `∞`**
(`ψ_∞` = `𝔽₁` / Hilbert–Pólya) that **supplies the positive *-structure as data**, not as a
coherence theorem — i.e. forces the off-line Krein signature `(k,k)` to be unreachable by making the
datum live in a category where every self-duality is automatically definite. No such geometry is in
the literature; producing it is the open frontier.

---

### Numerics (this session, anchor `q`)
- `cstar_hermitian_witness.py`: on-line `g` positive-definite `(d,0)`; **off-line FE-paired `g`
  non-degenerate but indefinite `(k,k)`** (`q=7,d=6`: `(3,3)`); invariance `|U*gU−g|/|g| ~ 1e-15`.
  Robustness `q∈{4,7,11,13,25}, d∈{4,6,8}`, 4 seeds: on-line **always** `(d,0)`, off-line **always**
  indefinite. → off-line consistent Krein *-category → **positivity EXTRA → NOGO_COMPLETE**.
- DH: no Euler product → no Frobenius datum → construction input-empty → DH-blind at Step B.

### Sources
- Stehouwer–Steinebrunner, *Dagger categories via anti-involutions and positivity*
  (arXiv:2304.02928): anti-involution (*-structure) permits **indefinite/Krein**; dagger/C* =
  the **EXTRA positivity restriction** to positive-definite Hermitian fixed points.
- Doplicher–Roberts reconstruction (nLab `Doplicher-Roberts+reconstruction+theorem`): a symmetric
  **C*-tensor** category with conjugates → a **compact** group. Compactness = consequence of the
  C*/positivity axiom.
- Deligne–Milne, *Tannakian Categories*; Milne, *Polarizations and Grothendieck's Standard
  Conjectures*: **Weil form** `Tr(u·u^φ)>0` = polarization = **extra structure**, not automatic;
  with a symmetric polarization `Aut^⊗(ω)` is a **compact** ℝ-group. Positivity = Rosati positivity.
- Tannaka–Krein: compact group ⟺ category of **unitary** (positive) reps; indefinite drops
  compactness.
- Cross-refs: `NG-frob-synthesis.md` §5 (the named door), `the-complete-account.md` §3/§5
  (Sylvester-inertia / `F†=F̄` / Krein off-line).
