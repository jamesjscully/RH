# method.md step 4 with the SIGNATURE target: does the falsifier change verdict for a FORM vs a NUMBER? (2026-06-06)

**Item (AGENDA NEXT #1, [CONSTRUCT · load-bearing · the relocated target]).** DONE #1+#2 refuted both
self-intersection *numbers* (`‖f‖²` RH-silent; its correction `deg(F)·(Δ·Δ)` RH-silent **and not even
Euler-borne**) and relocated the target to the **Hodge-index SIGNATURE `(1, ρ−1)` of the intersection
FORM on `H¹_prim`** — negative-definiteness of the form on the primitive part. The sharp falsifiable
question: **does the `falsify.py` verdict change when the candidate is a form's SIGNATURE rather than a
number?**

**Module:** `scripts/numerics/witness/signature_forcing.py` (made the signature EXECUTABLE; numpy
eigen-signatures, mpmath for `√q`). Registry row added to `falsify.py`. Tags **[THM]** / **[computed]**
/ **[CONJ]**.

---

## What I built (the signature made executable) [THM-backed + computed]

The decisive move: a signature is only a real falsifier test if it is *executable* and *responds to
zero locations*. I built the genuine Weil RH-positivity form on `H¹(C)` (NOT a toy):

- Frobenius `F` on `H¹(C)` (dim `2g`) satisfies the Rosati adjunction `F*F = q = deg(Frob)`; Weil's
  RH-positivity (= Hodge index on `C×C` restricted to correspondences = Rosati/trace form positive-
  definite) is the statement `q·I − F*F = 0`, i.e. **every `|α_k| = √q`** [THM, Weil 1948].
- The genuine **RH-defect FORM** is `P = diag(|α_k|² − q)`. Under RH it is **identically zero**:
  signature `(0, 2g, 0)`. [computed: q=7, g=2 ⟹ `defect_eigs = [0,0,0,0]`.]

## The SEES-ZEROS test for a FORM (the analog of `falsify.offline_sensitivity`) [computed]

First pass used a naive Gram `Re(u_iū_j)` and **failed honestly** (rank ≤ 2 regardless of the circle ⟹
`CHANGED=False`) — a wrong model, discarded. The corrected, mechanism-faithful form *does* see zeros:

Plant one off-circle eigenvalue `β` (with `|β| = blow·√q`) **with its functional-equation-forced Weil
partner** `q/β̄` (`|·|² = q²/|β|² < q`). The two land on **opposite sides of `q`**, so the defect
signature splits:

| blow `|α|/√q` | ON-line sig | OFF-line sig | changed? |
|---|---|---|---|
| 1.3 | `(0,4,0)` | `(1,2,1)` | **True** |
| 1.6 | `(0,4,0)` | `(1,2,1)` | **True** |
| 2.5 | `(0,4,0)` | `(1,2,1)` | **True** |

**This is the structural reason a SIGNATURE sees zeros where a NUMBER cannot:** the signature is a
*simultaneous* constraint on all eigenvalues at once; a single off-line zero (with its FE partner)
forces a sign change. A self-intersection *number* `Δ·Δ = deg·χ` is one scalar, blind to where the
`α`'s sit (DONE #2).

## The EULER-BORNE test for the FORM [THM]

The form lives on a **Satake/Frobenius eigenvalue lattice** `{α_k}`. Davenport–Heilbronn is a *sum* of
two Dirichlet L-functions with **no Euler product ⟹ no single set of Satake parameters ⟹ the
intersection FORM cannot be constructed at all**. Same DH-refusal as `‖f‖²` (which needed Satake
params) — but **strictly stronger than `deg·χ`**, which DH carries verbatim (a degree and an Euler
characteristic exist for DH). The *form's existence* requires the Euler/Hecke product.

## THE LOAD-BEARING VERDICT: the falsifier verdict DOES change [computed]

| candidate | Euler-borne | sees-zeros | independent | verdict |
|---|---|---|---|---|
| `‖f‖²` (NUMBER, pass-two) | Y | **N** | Y | **RH-SILENT** |
| `deg(F)·(Δ·Δ)` (NUMBER, DONE #2) | **N** | N | — | **RH-SILENT** (worse) |
| **SIGNATURE of the FORM on `H¹_prim`** | **Y** | **Y** | **N** (=Weil over ℤ) | **CIRCULAR** |

**The relocation from NUMBER to FORM moves the target out of the RH-silent graveyard into the CIRCULAR
box** — the *same box as the canonical Weil/Li forcing functional*. This is the honest, calibrated
finding: it is **not** FORCING (the prize is still empty), and the verdict does **not** claim the wall
is crossed. What changed is that the signature is now on the **correct forcing functional** whose *only*
defect is the missing independent proof — exactly the Weil positivity `λ_n ≥ 0`, restated as a
signature. The `falsify.py` registry now scores it `CIRCULAR`, side by side with the Weil form.

## STEP 4 — the UNIVERSAL PROPERTY, and the loop-closing identification [THM-level, CONJ over ℤ]

`method.md` step 4 asks what the object **represents**. By Sylvester + the spectral theorem, a signature
`(1, ρ−1)` *is the same data as* a splitting `L⊗ℝ = L₊ ⊕ L₋` with `L₊` the 1-dim ample/polarization
line and `L₋` **negative-definite**. And:

> **`−1 ×` (intersection form on `H¹_prim`) is POSITIVE-DEFINITE ⟺ it is an INNER PRODUCT ⟺ the OS/GNS
> Hilbert space (A4 of `F-sym2-os-bridge.md`).**

So the **geometric** Hodge-index signature and the **analytic** OS/sym² positivity (A4) are **the same
positive-definite form on the primitive/centre part**, arrived at from opposite sides. The signature
relocation therefore **closes the loop** with the OS/reflection-positivity bridge: both demand
positive-definiteness of one form on the primitive part, and the single remaining open thing is
identical — *make that positivity independently provable* (= supply the reflection positivity / the
`h_∞` metric), **not find a different number**.

The object's universal property: it represents the functor `T ↦ {(1, ρ−1)-polarized self-dual
T-lattices with negative-definite primitive part and Frobenius/flow trace = the explicit formula}`,
equivalently the OS/GNS-completion whose generator's spectrum is the zeros.

## NET — the located output [honest, non-overclaim]

- **The falsifier verdict changes for a FORM vs a NUMBER** (the item's question, answered executably):
  `RH-SILENT` (numbers) → `CIRCULAR` (signature). [computed, decisive.]
- **No new positivity, no construction, wall unmoved.** CIRCULAR is *not* the prize; it means the
  signature is the correct forcing functional with no independent proof — i.e. it IS the Weil
  positivity, now correctly typed as a form's signature rather than mis-typed as a self-intersection
  number.
- **The loop closes:** the relocated geometric target (negative-definite `H¹_prim` form) and the
  analytic OS target (A4 of the sym² bridge) are **one positive-definite form**. 11th wall confirmation,
  but the first that *unifies* the geometric and analytic threads onto a single object — so the next
  pass should attack the *one* shared positivity, not two parallel ones.
- **Why this is not progress past the wall:** `independent = N` because no surface `S²/ℤ` with
  `H¹_prim` exists; over `ℤ` the signature condition is `λ_n ≥ 0 ≡ RH`. The genuine open content is the
  implication *(sym² coefficients are a norm-square) ⟹ (the `H¹_prim` form is negative-definite =
  OS-positive)* — the edge→line wall, unchanged.

### Honest status
This pass produces an **executable falsifier upgrade** (the signature SEES-ZEROS probe) and a **verdict
relocation** (NUMBER→FORM moves RH-SILENT→CIRCULAR), plus the **geometric/analytic unification** (same
positive-definite form). It does **not** prove negative-definiteness over `ℤ`, does not construct the
surface, and does not claim to clear `independent`. The signature is CIRCULAR = RH, by design.

---
### Sources
- A. Weil, *Sur les courbes algébriques et les variétés qui s'en déduisent* (1948); the Rosati/trace
  positivity `F*F = q`. Hartshorne *Alg. Geom.* V.1 (Hodge index, signature `(1, ρ−1)`); Hindry–
  Silverman *Diophantine Geometry* App. A. Mumford, *Abelian Varieties* (Rosati involution positivity).
- Osterwalder–Schrader reconstruction (positive form = inner product = self-adjoint generator);
  `research/work/F-sym2-os-bridge.md` A4 (the sym² OS positivity).
- Prior loop: `research/log/2026-06-06-a5-corrected-mechanism.md` (DONE #1+#2, the signature relocation).
