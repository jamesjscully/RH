# NG candidate 3 — SYNTHESIS: the C*/Hermitian-self-duality test and the FORMALIZATION of the geometric no-go

**Charter.** `research/new-geometry-program.md`, candidate 3 (the last categorical door). Does a
*-autonomous / dagger-compact / C*-tensor / Hermitian-self-dual structure on the Frobenius datum **FORCE**
the polarization positivity — Step B, the radius `|α|=√q = F†=F̄ =` RH `=` compact motivic Galois (via
Doplicher–Roberts) — **from the duality itself**, the one place positivity might be *built into* the duality
rather than *imported* as a fiber functor? Or is positive-definiteness still an extra input, so the off-line
spectrum lives in a consistent indefinite/Krein *-category and the geometric no-go is **complete**?

**Verdict: `NOGO_COMPLETE`.** Concordant across all three angles, and **verified directly on the Frobenius
datum this session** (both numerics reproduced, the apparent angle-1/angle-2 divergence resolved — it is not
a contradiction but the load-bearing point itself).

---

## 1. Judge question 1 — does C*/Doplicher–Roberts force positivity, or is requiring C* = requiring RH?

**Doplicher–Roberts is the real theorem and it is engaged honestly: it genuinely gives compactness FROM the
duality — but only once positivity is already an axiom of the input category.** DR/Longo–Roberts: a *symmetric
tensor **C\***-category with conjugates, subobjects, direct sums, `End(𝟙)=ℂ`* reconstructs a unique **compact**
group. The compactness is **downstream of the C*-positivity axiom** (Longo–Roberts: conjugates + `f*f≥0` ⟹
positive intrinsic dimension; the standard conjugate solution is positive *because* of positivity). DR does
**not** manufacture positivity from tensor/duality coherence — it *consumes* a positive category and *emits*
compactness. Drop to the bare *-category / Krein-C* level and DR reconstructs a (possibly non-compact /
indefinite) object: the off-line model.

**Requiring C*/positive-definite IS requiring RH — verified.** Two equivalent measurements, both reproduced:

- **At the FE/declared scalar `q`** (`cstar_hermitian_witness.py`, FE-paired datum, `q=7, d=6`, normalized at
  the FE radius `√q`): a non-degenerate invariant Hermitian form `g` (`U*gU=g`, `U=F/√q`) **exists at every
  radius** (invariance residual `~1e-15`, exact), but its **signature** is `(d,0)` **positive-definite
  on-line** and flips to `(k,k)` **indefinite/Krein off-line** — reproduced `(6,0)` on-line vs `(3,3)`
  off-line for both `ratio=1.0` and `1.3`. The *-structure (Step A, non-degeneracy) is **free** at every
  radius; positive-definiteness (Step B, C*) is the **strict extra restriction** to the `(d,0)` subclass.
  *Mechanism (Sylvester inertia):* the FE involution pairs `eigvec(μ)` with `eigvec(1/μ̄)` (`μ=eig/√q`); on
  the circle (`|μ|=1`) this is a definite diagonal pairing, off the circle (`μ≠1/μ̄`) it is forced into
  hyperbolic `(+,−)` blocks. Off-circle ⟹ indefinite, exactly and robustly.
- **The own-modulus escape, closed.** Angle 2 found that a **single conjugate pair** `α=re^{±it}` normalized
  at its **own modulus `r`** is trivially unitarizable (one circle) and carries a **positive-definite**
  invariant form `(+2,−0)` at every radius — *reproduced* (residual `<5e-16`). But the **honest** FE datum is
  not a single pair: the FE involution `α↔q/ᾱ` forces eigenvalues `{√q·ρ·e^{it}, √q·e^{it}/ρ}` of **UNEQUAL
  moduli** off-line (reproduced: `|eig|={1.70,1.89,3.70,4.12}`). Unequal moduli ⟹ **no** single own-circle ⟹
  **no** positive-definite invariant similitude form for the genuine multi-eigenvalue datum. So angle 2's
  positivity is real only for the single-pair toy; for the real datum it collapses to the self-referential
  degree `N(α)=|α|²` (`rosati_circularity_skeptic.py`: `F·F†=28=r²≠q` off-circle). **C* at F's own degree is a
  tautology; C* at the externally prescribed `q` exists off-line only as a Krein form, never positive.**

**Conclusion to Q1: C*/DR does NOT force positivity from the duality.** It forces *compactness from
positivity*, and the positive form it certifies is glued to the **self-referential** degree `|α|²=N(α)`, never
to an independently given `q`. Demanding the C* form at the arithmetic `q` is demanding `(d,0)` off-line,
which the FE pairing forbids off-circle — i.e. demanding `|α|=√q` — i.e. **circular: C* = positive = on-line =
RH.** This is the Doplicher–Roberts circularity made exact and checked on the datum.

## 2. Resolving the angle-1 / angle-2 apparent divergence (it is the finding, not a conflict)

Angle 1 reported off-line `(k,k)` **indefinite**; angle 2 reported off-line `(+,0)` **positive-definite**.
Both are correct; they normalize the form by **different scalars**, and the gap between those scalars is
exactly Step B:

| | scalar normalizing the form | datum | off-line signature | meaning |
|---|---|---|---|---|
| **angle 1** | the **FE / arithmetic** radius `√q` (`s=q`) | full FE-paired (the honest Frobenius) | **`(k,k)` Krein** | the *arithmetic* radius — RH — is NOT carried off-line |
| **angle 2** | F's **own** modulus `r` (`s=\|α\|²`) | single conjugate pair (one circle) | **`(d,0)` C\*** but at the **wrong scale** | positivity is free at the *self-referential* degree |

Reconciled and verified: the **honest FE datum** off-line has **unequal moduli**, so (i) the FE-anchored form
is `(k,k)` (angle 1, reproduced `(3,3)`), and (ii) the own-modulus positive form **does not exist** for the
multi-eigenvalue datum at all (angle 2's `(+,0)` is a single-pair artifact; the multi-eig FE datum collapses
to the self-referential degree, Rosati skeptic). **Both angles say the same thing:** the duality emits a
non-degenerate form (free) and even, in degenerate cases, a sign — but **never the positive sign anchored to
the external arithmetic scalar `q`.** Step B = positivity-at-`q` is the import. *(Angle 3 states this exactly:
C* is satisfiable off-line at the own degree; the self-duality at the declared `q` exists iff on-line.)*

## 3. Judge question 2 — THE VERDICT

**`NOGO_COMPLETE`.** Off-line is **NOT** made inconsistent by *-autonomy or by the C* axiom; it is a
**consistent indefinite/Krein *-category** — a *named, published* structure (Bertozzini–Conti–Lewkeeratiyutkul,
*Krein C\*-categories*, arXiv:1112.5996: a *-category with indefinite inner product + fundamental symmetry `J`,
the C*-positivity axiom *replaced*). The off-line / non-polarizable / Krein spectrum is its canonical
inhabitant. Positive-definiteness (C*) is a **strict extra restriction** to the `(d,0)` subclass, identical in
status to candidate 2's polarized fiber functor and candidate 1's properness. **Off-line is consistent ⟹
positivity is EXTRA ⟹ the no-go holds.** The verdict is *not* `EXCEPTION_NEW_GEOMETRY`: the C*-axiom does not
make the off-line datum inconsistent (it is satisfiable off-line at the own degree, and the bare duality is
satisfiable with a Krein form), so no coherence theorem can exclude the off-line model.

This **resolves candidate 2's single named open proposition** — *"no coherence theorem emits a SIGN (positive
self-duality) from a SIGN-FREE non-degenerate self-duality"* — **in the affirmative / no-go direction**,
verified directly on the Frobenius datum: a non-degenerate Hermitian self-duality carries no canonical sign
(Stehouwer–Steinebrunner arXiv:2304.02928: an anti-involution permits indefinite/Krein structures; the
dagger/C* category is built by *restricting* to the positive-definite subclass — positivity is a separate
axiom), and where a sign IS forced (equal moduli) it is glued to the self-referential scale, never the
arithmetic `q` (Deligne–Milne: the Weil form `Tr(u·u^φ)>0` is an extra axiom giving a *compact* `Aut^⊗(ω)`).

## 4. Judge question 3 — THE FORMAL NO-GO, with precise scope

> **(Geometric / categorical no-go — provable form.)** Let a *coherence-without-a-finite-ground* structure be
> any of: a rigid tensor category, a *-autonomous / Hermitian-self-dual category, a (Krein-)C*-category, a
> six-functor formalism, or an o-minimal structure, **carrying the Frobenius/FE datum but with no externally
> specified finite ground `𝔽_q` in its axioms.** Then **Step A** — finite-dimensionality, perfect duality,
> the functional equation `F·F† = [deg]` — is **forced** by the structure, archimedean-natively. But **Step
> B** — the radius `|α|² = q = F†=F̄ =` compact motivic Galois `=` RH — is **NOT forced**: every such structure
> admits the **off-line / indefinite / Krein model** as a consistent object, in which the self-duality holds
> with indefinite signature at the self-referential degree `|α|²`. The positive-definite C*-polarization at
> the *arithmetic* radius `q` is an **irreducible external input**, equivalent to specifying a finite ground —
> which `Spec ℤ` provably lacks at `∞`.

**Status: a THEOREM at a precise scope, modulo the standard reconstruction theorems** (Deligne–Milne
Tannakian; Doplicher–Roberts / Longo–Roberts; van den Dries o-minimal finiteness). The scope is exactly:
*RH (Step B) is not forced by coherence-without-a-finite-ground.* For **each** named structure the
off-line/indefinite model is **exhibited** as a consistent object — candidate 1: the archimedean fibre is
provably WILD (`Γ_ℝ` pole spectrum `{0,−2,−4,…}` non-definable in any o-minimal structure, so nothing
obstructs the *open* model); candidate 2: `Rep(⟨F⟩_Zar)` off-line, computed; candidate 3: the Krein-C*
category off-line + C* only at the own degree, computed this session + the published Krein-C* structure. None
forbids the off-line model, so none forces Step B. **This is independence from a class of methods, NOT logical
undecidability of RH** — it is the precise limit of *geometry-by-coherence*.

**The three-instrument pattern, closed at one wall:**

| candidate | mechanism (Step A, FREE) | Step B import | off-line model (consistent) |
|---|---|---|---|
| 1 o-minimal | BKT o-minimal GAGA properizes transcendental periods | **properness** | wild fibre / open model |
| 2 Frobenius-first | rigidity `= F·F†=[deg]` at every radius | **polarizability** | non-polarizable rigid Tannakian cat |
| 3 C*/Hermitian | *-autonomy `= F*HF=s·H`, any signature | **C*-positivity at the arithmetic `q`** | indefinite **Krein C\*-category** |

All Step A free; all Step B imported; all at the same wall; all admitting the off-line model. **The
categorical branch of the new-geometry program is closed.**

## 5. DH — FAILS in the no-go way (not a healthy gate)

(a) **Input-empty at Step A:** DH has no Euler product ⟹ no local Frobenius `F_p` ⟹ no Tannakian / *- / Krein
/ C* datum to carry any duality — type-vacuous, same as candidates 1–2. (b) **Radius-blind at Step B where a
datum exists:** the *-/Krein/C* machinery certifies `|α|²=`own degree verbatim for DH-style off-line spectra,
drawing **no ζ/DH distinction at the radius** — the distinction lives entirely in the externally imported `q`.
`falsify.py` axes: Step A DISPERSING (holds for any F), Step B CIRCULAR (positive self-duality at the declared
`q` ⟺ RH, no independent certificate). DH-blind at Step B = **FAIL**, the no-go way.

## 6. Surviving gap (candidate 4) and the honest meaning

**The no-go does NOT close RH; it relocates the missing input precisely.** The one logical escape it does not
touch — because it is *not* coherence-without-a-finite-ground — is a structure whose axioms **simultaneously**
(i) emit the positive sign AND (ii) anchor the duality scalar `s` to an *arithmetically* specified `q`: a
**real geometric origin** (a variety over a finite ground, supplied archimedean-natively) — the `𝔽₁` /
finite-field-at-`∞` / Hilbert–Pólya object `ψ_∞`. Such a category would be one *in which every self-duality is
automatically definite at the arithmetic scale*, making the off-line Krein signature `(k,k)` unreachable — not
by a coherence theorem (proven impossible here) but by containing the finite ground as **data**. No such object
is in the literature; producing it (forcing `F†=F̄` at `∞`, the finite ground `ℤ` lacks at infinity) is the
open frontier. The no-go proves **coherence alone cannot substitute for the finite ground**; it does **not**
prove no geometry can.

**What this no-go says about RH:** the radius `|α|=√q` — purity, RH — is **not a sign/positivity fact that any
duality, *-structure, polarization coherence, or compact-group reconstruction can emit**. It is the **imported
arithmetic scale** of a finite ground. Every known instrument and now the entire categorical/coherence branch
imports it; none manufactures it from a metric-free archimedean fibre. **Crossing it requires the one input
the program has isolated and the literature does not supply: a finite ground at `∞` (`ψ_∞` / `𝔽₁` /
Hilbert–Pólya) that fixes the scale archimedean-natively** — the sole surviving non-categorical escape, and the
honest residue of the new-geometry program.

`positivity_forced_or_extra = EXTRA` (C* at the arithmetic radius is the import; off-line is Krein-consistent).

---

### Numerics reproduced/verified this session
- `cstar_hermitian_witness.py` (`q=7, d=6`, FE-paired): invariance residual `~1e-15`; signature **`(6,0)`
  on-line, `(3,3)` off-line** for `ratio∈{1.0,1.3}`. Non-degeneracy free, positivity flips off-line.
- Own-modulus single-pair toy (angle 2): `(+2,−0)` at every radius, residual `<5e-16` — but the **honest
  FE datum off-line has UNEQUAL moduli** (`{1.70,1.89,3.70,4.12}`), so the own-modulus positive form does not
  exist for the genuine datum; it collapses to the self-referential degree (`rosati_circularity_skeptic.py`:
  `F·F†=28=r²≠q`).
- FE datum at scalar `s=q`: solution space dim **6 on-line vs 4 off-line**; the off-line forms are all
  **`(3,3)` indefinite** — the q-anchored positive form exists iff on-line (= RH restated).

### Sources (real theorems engaged)
- **Doplicher–Roberts / Longo–Roberts** (nLab; Müger 2006): symmetric tensor **C\***-category with conjugates
  ⟹ compact group; compactness downstream of the C*-positivity input, not of tensor coherence.
- **Bertozzini–Conti–Lewkeeratiyutkul**, *Krein C\*-categories* (arXiv:1112.5996): the consistent indefinite
  off-line model — positivity replaced by a fundamental symmetry.
- **Stehouwer–Steinebrunner** (arXiv:2304.02928): anti-involution permits indefinite/Krein; dagger/C* =
  restriction to the positive-definite subclass — positivity a separate axiom.
- **Deligne–Milne**, *Tannakian Categories*: the Weil-form positivity `Tr(u∘u^φ)>0` is a separate polarization
  axiom giving a compact `Aut^⊗(ω)`.
