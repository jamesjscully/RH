# NG candidate 3 — the C*/Hermitian-self-duality test AND the geometric-no-go FORMALIZATION

**Charter.** `research/new-geometry-program.md`, candidate 3: does a *-autonomous / Hermitian-self-dual /
C*-category structure on the Frobenius datum **FORCE** the polarization positivity (Step B: the radius
`|α|=√q = F†=F̄ = RH =` compact motivic Galois) from the **duality itself** — the one place positivity
might be *built in* rather than *imported* — or is positivity still an extra input, **completing the
geometric no-go**? Candidate 1 imported **properness**; candidate 2 imported **polarizability** and proved
the off-line Frobenius generates a **CONSISTENT non-polarizable rigid Tannakian category**. Candidate 3 is
the last open door: the synthesis (`NG-frob-synthesis.md` §5) compressed the whole no-go to one checkable
proposition — *"no coherence theorem emits a SIGN (positive self-duality) from a SIGN-FREE non-degenerate
self-duality."* This log audits the C*/Doplicher–Roberts route against exactly that, and formalizes the
endpoint.

**Verdict: `NOGO_COMPLETE`.** The off-line Frobenius admits a consistent **Krein / indefinite *-structure**
(a real, published categorical object), and the C*/positivity axiom — the one thing that *does* force a
positive self-duality and a compact group (Doplicher–Roberts) — forces it **only relative to F's own
self-referential degree `|α|²`, never relative to the externally declared `q`**. C* is the imported extra,
identical to candidates 1/2's import at the same wall. The duality does **not** build in the radius.

---

## 1. The sharp hierarchy: *-category ⊋ Krein-C* ⊋ C* — and where off-line lives

The question hinges on a distinction the program had not yet made precise: **what exactly does "*-structure"
mean, and at which level does positivity enter?** Three published, distinct levels (sources §6):

| structure | involution `*` | inner product / metric | positivity axiom `f*f≥0`, `‖f*f‖=‖f‖²` | off-line F consistent? |
|---|---|---|---|---|
| **\*-category** | yes (conjugate-linear, `(a*)*=a`) | a non-degenerate Hermitian `H` (any signature) | **NO** | **YES** (indefinite H) |
| **Krein C\*-category** | yes | **indefinite** Hermitian + a fundamental symmetry `J`, `J²=1` | replaced by `J`-positivity | **YES** (this IS the off-line model) |
| **C\*-category** | yes | **positive-definite** `H` | **YES** | only at `|α|²=`own degree |

Bertozzini–Conti–Lewkeeratiyutkul, *Krein C*-categories* (arXiv:1112.5996), is decisive: a **Krein
C*-category** is a genuine, axiomatized, consistent categorical structure carrying an **indefinite** inner
product, with the C*-positivity axiom *replaced* by a fundamental symmetry handling the indefinite metric.
**This is precisely the categorical home of the off-line / non-polarizable / Krein spectrum.** The off-line
model is not a degenerate non-object; it is a named structure in the literature.

So "*-autonomy / Hermitian self-duality" by itself sits at the **\*-category** level — and that level is
**sign-free**: a non-degenerate Hermitian form carries no canonical sign. Positivity (C*) is a *strictly
stronger, separate* axiom. This already answers the charter at the structural level: **a Hermitian
self-duality does NOT force positive-definiteness; it admits an indefinite (Krein) realization.**

## 2. The decisive numerics — off-line carries a consistent Hermitian self-duality

`frob_block(r,t)` (2×2 real Frobenius, eigenvalues `r e^{±it}`), `q=7`, computed this session.

**(a) At F's OWN degree `|α|²` — a pos-def invariant H ALWAYS exists (a genuine C*-structure off-line):**
solving `F* H F = |α|²·H` for Hermitian `H`, the averaged form `H=P⁻* P⁻¹` is **positive-definite** with
residual `≤ 3e-14` at every radius:

| case | `\|α\|²` (= own degree) | invariant **pos-def** H exists | invariant **indefinite/Krein** H exists |
|---|---|---|---|
| ON-LINE `r=√q` | 7.000 | **True** | **True** |
| OFF-LINE `r=1.3√q` | 11.830 | **True** | **True** |
| OFF-LINE `r=0.6√q` | 2.520 | **True** | **True** |

Off-line F is `H`-unitary up to the scalar `|α|²` for a **positive-definite** `H`. By Doplicher–Roberts the
generated symmetric C*-tensor category with conjugates reconstructs a **compact group** — for **every**
off-line F. The C*-structure is consistent off-line. (It also admits the indefinite/Krein H — both signs
live there.) **Off-line is NOT made inconsistent by *-autonomy or by C*; the C* axiom is satisfiable
off-line.**

**(b) At the DECLARED degree `q` — no invariant Hermitian form exists at all, off-line:**

| case | invariant Hermitian H with `F* H F = q·H` (pos-def OR Krein) |
|---|---|
| ON-LINE `r=√q` | **exists** (2-dim space) |
| OFF-LINE `r=1.3√q` | **0 — none, of any signature** |
| OFF-LINE `r=0.6√q` | **0 — none, of any signature** |

The Hermitian self-duality at the **externally declared radius `q`** exists **iff on-line**. But this is
not C* forcing the radius — it is the *definition* of on-line restated: `F* H F = q·H` with `q` declared
**is** `|α|²=q` **is** RH.

## 3. The exact circularity — C* forces the SELF-REFERENTIAL radius, not the arithmetic one

Reading (a)+(b) together gives the candidate-3 answer with full precision, and it is the **same circularity
the Rosati skeptic (candidate 2) found**, now at the C*/Doplicher–Roberts level:

> **C*/Doplicher–Roberts DOES force a positive self-duality and a compact group — but it certifies
> `|α|² = `(F's own degree), a self-referential tautology, NEVER `|α|² = q` for an independently given `q`.**

- `F·F† = |α|²` is forced by the C*-structure — but `|α|²` is read **off F itself** (its own norm = its own
  degree), exactly the integrality tautology `N(α)=|α|²` of `rosati_circularity_skeptic.py`
  (`F·F† = 11.83, 2.52 ≠ q` off-line). Doplicher–Roberts upgrades this from "a positive form exists" to "a
  compact group exists," but the radius it certifies is still the self-referential one.
- The arithmetic content — RH — is `|α|² = q` with `q` the **field size of the finite ground**, an
  *external, independently specified* number. C*-positivity at the declared `q` (table (b)) exists only
  on-line. **Declaring `q` to be F's degree is declaring RH.** This is the import, made exact.

So the **SIGN is not emitted by the duality**: the *-autonomous (sign-free) self-duality `F* H F = s·H`
holds at `s=|α|²` with H of *either* sign (pos-def or Krein). To pin the **positive** sign **and** the
**arithmetic** scalar `q` simultaneously requires choosing the positive fiber functor AND anchoring `s=q`
externally — neither is forced by coherence. **Candidate 2's open proposition is confirmed FALSE-for-forcing:
no coherence theorem emits the arithmetic sign+radius; C* emits only the self-referential one.**

## 4. Doplicher–Roberts engaged honestly — it is the real theorem, and it imports positivity

DR (sources §6, nLab; Müger): a **symmetric tensor *-category with conjugates, subobjects, direct sums,
`End(𝟙)=ℂ`** reconstructs a unique **compact** group. The load-bearing input is the **C*-positivity** baked
into "conjugates in a *-category" (Longo–Roberts: conjugates + C* ⟹ positive intrinsic dimension; the
standard solution of the conjugate equations is positive *because* of `f*f≥0`). DR's compactness is
**downstream of the C*-positivity axiom**, which is an *input*, not manufactured by the tensor coherence.
Drop positivity to the bare *-category / Krein-C* level and the reconstruction yields a (possibly
non-compact / indefinite) object — the off-line model. DR is therefore **not** a counterexample to the
no-go: it is its sharpest confirmation. It forces compactness **from** positivity; it does **not** force
positivity from the duality. **"Does zeta's datum give a C*-category without assuming the radius?" — NO:
it gives a *-category (Step A, free) at the declared `q` only on-line; the C* upgrade IS the radius.**

## 5. DH — FAILS in the no-go way (DH-blind at Step B, input-empty at Step A)

Two readings, same verdict (identical to candidates 1, 2). (a) **Input-empty:** DH has no Euler product ⟹
no local Frobenius `F_p` ⟹ no Tannakian / *-category / Krein / C* datum to carry any duality — the
construction does not exist for DH in the trivial type-vacuous sense. (b) **Radius-blind where it does
apply:** given any F, the *-/Krein/C* machinery certifies `|α|²=`own degree verbatim, drawing **no
zeta/DH distinction at the radius** — the distinction lives entirely in the externally imported `q`. Either
way DH-blind at Step B = **FAIL**, not a healthy "fails to exist" gate. The candidate cannot tell ζ from DH
where it matters. `falsify.py` axes: Step A is DISPERSING (holds for any F, DH-blind); Step B is CIRCULAR
(positive self-duality at the declared `q` ⟺ RH).

## 6. THE FORMALIZATION — the geometric no-go, stated at its provable scope

Three instruments, three independent routes, **one wall**, now closed:

| candidate | mechanism (Step A, FREE) | Step B import |
|---|---|---|
| 1 o-minimal | BKT o-minimal GAGA properizes transcendental periods | **properness** (the archimedean fibre is provably WILD: `Γ_ℝ` pole spectrum `{0,−2,−4,…}` non-definable) |
| 2 Frobenius-first | rigidity = finite-dim + duality + FE = `F·F†=[deg]` at every radius | **polarizability** (off-line = consistent non-polarizable rigid Tannakian cat) |
| 3 C*/Hermitian | *-autonomy = Hermitian self-duality `F* H F = s·H` at `s=|α|²`, any signature | **C*-positivity at the declared `q`** (off-line = consistent **Krein** *-category; C* forces only the self-referential radius) |

**The theorem-shaped statement, with scope made precise:**

> **(Geometric / categorical no-go, provable form.)** Let a "coherence-without-a-finite-ground" structure be
> any of: a rigid tensor category, a *-autonomous / Hermitian-self-dual category, a (Krein-)C*-category, a
> six-functor formalism, or an o-minimal structure, **carrying the Frobenius/FE datum but no externally
> specified finite ground `𝔽_q`.** Then **Step A** (finite-dimensionality, perfect duality, the functional
> equation `F·F† = [deg]`) is **forced** by the structure, archimedean-natively. But **Step B** (the radius
> `|α|² = q = F†=F̄ =` compact motivic Galois `=` RH) is **NOT forced**: every such structure admits the
> **off-line / indefinite / Krein model** as a consistent object, in which the self-duality holds with
> indefinite signature at the self-referential degree. The positive-definite C*-polarization at the
> *arithmetic* radius `q` is an **irreducible external input** equivalent to specifying a finite ground —
> which `Spec ℤ` provably lacks at `∞`.

**Is this PROVABLE as stated?** For each named structure, the off-line/indefinite model is **EXHIBITED** as
a consistent object (candidate 1: wild fibre, no definable finiteness obstructs the *open* model; candidate
2: `Rep(⟨F⟩_Zar)` off-line, computed; candidate 3: Krein-C* off-line + pos-def C* at own degree, computed +
the published Krein-C*-category structure). So **at the scope of these instruments the no-go is a theorem
modulo the standard reconstruction theorems** (Deligne–Milne Tannakian; Doplicher–Roberts/Longo–Roberts;
van den Dries o-minimal finiteness): each admits the off-line model, hence none forces Step B.

**Where could it FAIL — the one structure that forbids the indefinite model?** Only a structure whose
**axioms are inconsistent with an indefinite invariant form** could force C*-positivity from the duality.
The candidate was the C*/DR route — and it **does not** forbid the off-line model: C* is satisfiable
off-line (at the own degree), and the *bare* duality is satisfiable with a Krein form. The surviving logical
escape (candidate 4, below) is a structure that **welds the scalar `s` to an externally specified `q`** at
the categorical level — i.e. that contains the finite ground in its axioms. But that is **importing the
finite ground**, not manufacturing it, so it does not falsify the no-go; it instantiates it.

## 7. Honest status — theorem, conjecture, or surviving gap?

- **It is a THEOREM at a precise scope, NOT "RH is undecidable."** The scope is exactly:
  *RH (Step B) is not forced by coherence-without-a-finite-ground.* For every coherence structure that does
  not put a finite ground into its axioms, the off-line/indefinite model is consistent, so Step B is not
  forced. This is independence **from a class of methods**, not logical independence of RH.
- **The mechanism is uniform and proven, not heuristic:** Step A free + off-line consistent + positivity
  forced only at the **self-referential** degree. The "sign-from-sign-free" proposition is now **resolved
  in the no-go direction** for the C* case: C* emits a sign, but glued to the wrong (self-referential)
  radius; the arithmetic radius requires the external `q`.
- **Surviving gap (the genuine `ψ_∞` / candidate-4 frontier):** a structure whose axioms **simultaneously**
  (i) emit the positive sign AND (ii) anchor the scalar to an *arithmetically* specified `q` — i.e. a
  **real geometric origin: a variety over a finite ground, archimedean-natively**. This is exactly the
  `𝔽₁` / finite-field-at-`∞` / Hilbert–Pólya open object. The no-go says **coherence alone cannot supply
  it**; it does **not** say no geometry can. That object is not in the literature and is not constructed
  here. **This is the honest residue, unchanged in content but now sharpened: the missing input is a finite
  ground, and the no-go proves no coherence structure substitutes for it.**

`positivity_forced_or_extra = EXTRA` (C* at the arithmetic radius is the import; off-line is Krein-consistent).

---

### Numerics reproduced this session
- `frob_block` (`q=7`): invariant Hermitian `F* H F = s·H` — at `s=|α|²` (own degree): **pos-def AND
  indefinite** H exist, every radius (residual `≤3e-14`); at `s=q` (declared): exists **iff on-line**
  (off-line: 0 forms of any signature). ⟹ C* satisfiable off-line at own degree; the arithmetic radius `q`
  is external. **NOGO.**
- Consistent with `rosati_circularity_skeptic.py`: `F·F†=|α|²=N(α)≠q` off-line — the self-referential
  tautology, now at C*/DR level.

### Sources
- Bertozzini–Conti–Lewkeeratiyutkul, *Krein C*-categories* (arXiv:1112.5996): a *-category with **indefinite**
  inner product + fundamental symmetry; positivity axiom replaced — the consistent indefinite/off-line model.
- Doplicher–Roberts reconstruction (nLab; Müger 2006; Longo–Roberts): symmetric tensor **C*-**category with
  conjugates ⟹ compact group; compactness **downstream of the C*-positivity input**, not of tensor coherence.
- Deligne–Milne, *Tannakian Categories* (§polarizations): a **Weil form** has positivity `Tr(u∘u^φ)>0` as a
  **separate axiom**; a polarization = compatible sesquilinear forms WITH positivity = an EXTRA structure.
- van den Dries o-minimal finiteness (candidate 1); Connes–Marcolli motivic Galois (candidate 2 free group).
