# Re-running method.md step 2 with the CORRECTED line-forcing mechanism (2026-06-06)

**Item (AGENDA NEXT #1, [BACK UP TO PASS TWO · HIGH · load-bearing]).** DONE #1 refuted A5: the Weil
line-forcing self-intersection is **not** the Petersson norm `‖f‖²` but `Γ_q·Γ_q = q·(Δ·Δ)`, an Euler
characteristic scaled by `q = #𝔽_q = deg(Frob)`. Re-run `method.md` step 2 with the corrected
mechanism: what over `ℤ` plays the role of the `q`-scaled self-intersection whose root is the line, and
where (if at all) does `‖f‖²` legitimately enter?

**Module:** `scripts/numerics/witness/a5_corrected.py` (exact integer intersection numbers; `numpy`
for the Hodge-index signature; `mpmath` for the `√q` log-ratio). Tags **[THM]** / **[computed]** /
**[CONJ]**.

---

## Step 1 redone — MECHANISM (object-free, corrected) [THM]

The square root that puts the zeros on the line is the root of **`deg(F)` — the degree of a self-map /
the size of the base field**, carried by the self-intersection of the *graph* of an endomorphism:

> `Γ_F · Γ_F = deg(F) · (Δ·Δ)`   (Δ = `Γ_id`, `deg(id)=1`; Frobenius: `deg = q`).

Verified exactly on `C×C` for `g=0,2,3` and `F ∈ {id, Frob_q, Frob_{q²}, [2], [3]}`: the ratio
`Γ_F·Γ_F / Δ·Δ` equals `deg(F)` identically (§1 of the module). The line is then literally
`Re s = log(q^{1/2})/log q = ½` for **every** `q` (§2) — the `½` is the log-ratio of the degree's
square root to the degree. **There is no modular form, no L-value, no norm in the forcing input** —
only (i) an Euler characteristic `Δ·Δ = 2−2g` and (ii) a **degree** `deg(F)` of a correspondence.

## Step 2 redone — AXIOMS, and the falsifier verdict on the corrected target [computed → honest negative]

Naively the corrected axiom reads: *RH `⟸` a surface whose graph self-intersection carries the
**degree-scaled Euler characteristic** `deg(F)·(Δ·Δ)`, whose root is the line.* Scoring this corrected
**number** on `falsify.py`'s three axes (§4):

| axis | corrected target `deg(F)·(Δ·Δ)` | vs. the refuted `‖f‖²` |
|---|---|---|
| **Euler-borne** | **NO** — neither `deg(Frob)=q` nor `Δ·Δ=2−2g` touches the Euler product; Davenport–Heilbronn also has a functional-equation scaling + an archimedean Euler characteristic | `‖f‖²` *was* Euler-borne (needed Satake params, DH-refused) |
| **sees-zeros** | the **mechanism** (Hodge index) does; the **number** `deg·χ` does not — a single scalar carries no zero locations | both RH-silent as numbers |
| **independent** | over `𝔽_q` unconditional; over `ℤ` conditional on the (non-existent) surface | same |

**Verdict [computed]: the corrected target is RH-SILENT *and not even Euler-borne* — strictly worse
than `‖f‖²` as a candidate.** `deg(F)·(Δ·Δ)` is pure *topology × base-field-size*, a datum a DH-type
L-function carries verbatim (it too has a conductor/scaling and a Γ-factor Euler characteristic).

## The decisive relocation — the RH content is the FORM's SIGNATURE, not any NUMBER [THM + computed]

Chasing the self-intersection *number* (whether `‖f‖²` or `deg·χ`) is **the wrong kind of object**. The
genuine Weil mechanism is the **Hodge index theorem**: the intersection form on `NS(S)` (rank `ρ`) has
signature `(1, ρ−1)` — one positive eigenvalue (the ample class), the rest **negative**. Weil's RH
bound is the negativity `(D·D) ≤ 0` for `D` in the *primitive part* (orthogonal to the ample/fiber
classes); the self-intersection number `Δ·Δ = deg·χ` is merely a **value the negative-definite form is
evaluated on**, not the source of the forcing.

Verified concretely (§5): the `NS`-sublattice `⟨f₁,f₂,Δ⟩` of `E×E` (`g=1`) has Gram
`[[0,1,1],[1,0,1],[1,1,0]]`, eigenvalues `{−1,−1,2}`, signature `(1,2) = (1, ρ−1)` — exactly the Hodge
index prediction. **The RH-forcing content is the signature of the intersection FORM.**

## Where over `ℤ` the corrected analog lands (three candidates, §3) [CONJ]

There is **no single base field over `ℤ`** to supply a finite `q`:
- **(a)** a *literal* degree `q`: none — Connes–Consani replace `deg(Frob)=q` by the full real scaling
  flow `ℝ₊*` (the archimedean module). The "line = root of the scaling" then collapses to the **fixed
  locus of `u↦−u` (= `s↦1−s`)** — i.e. the bare functional equation, which is **RH-neutral** (holds for
  DH). [Auditor row 1.]
- **(b)** `deg(arith. Frobenius)·(Δ·Δ)` on a surface over `𝔽₁`/the arithmetic site: this is the
  **continuous-Frobenius `Δ·Δ=∞` corner** (the Janus corner, positivity-program §G) — the degree is
  *infinite*, so `deg·χ` diverges. The corrected target **lands exactly on the known wall, now correctly
  named: a degree × Euler characteristic, not `‖f‖²`.**
- **(c)** the archimedean Γ-weight in the explicit formula: re-expresses the line as the cross-place
  margin `W_∞ ≥ Σ_p W_p` (positivity-program §I); no new number.

## Where does `‖f‖²` legitimately enter? [THM, from DONE #1 + this pass]

`‖f‖²` is **RH-silent scaffolding, not the forcing input** — confirmed. It is the `s=1` residue
(Arakelov height / Petersson norm), the *edge* quantity (Worker E), and the genuine "self-intersection
= RS-L-value" theorem (Yun–Zhang) is a *derivative at `s=½` on Shtukas* (Gross–Zagier, RH-silent). The
corrected mechanism shows the line is forced **upstream of any L-value**, by the signature of an
intersection form. `‖f‖²` enters only as one possible *value* in the lattice, never as the forcing.

## NET — the located output of pass-three

Two passes pinned the surface to a **self-intersection number** (`‖f‖²`, then refuted, then `deg·χ`,
now shown RH-silent and not-even-Euler-borne). **Both fail for the same structural reason: the line is
not forced by a number at all.** The corrected target is the **negative-definite intersection FORM on
the primitive cohomology `H¹_prim` of a surface over `ℤ`** — RH `⟺` that form has the Hodge-index
signature `(1, ρ−1)`. This is the 10th confirmation of the standing wall and, importantly, it
**dissolves the "self-intersection = norm" framing entirely**: the program should stop hunting a
self-intersection *number* and target the *signature* of an intersection *form*. That reconnects
directly to the OS/reflection-positivity thread (a form's signature *is* a positivity), but now with
the correct geometric object identified.

### Honest status / non-overclaim
This pass produces **no new positivity** and **no construction**. It is an honest negative + a
relocation: it kills the corrected-number target (`deg·χ`) on the falsifier, proves the forcing is the
form's signature (verified on `E×E`), and re-aims the construction question. Whether the
negative-definite `H¹_prim` form over `ℤ` is realizable is the wall, unmoved but re-posed as a
**signature** rather than a **number**.

---
### Sources
- A. Weil, intersection-theoretic RH; Hartshorne *Alg. Geom.* V.1 (Hodge index thm, signature
  `(1,ρ−1)`); Hindry–Silverman *Diophantine Geometry* App. A; Lorenzini, *Invitation to Arithmetic
  Geometry*.
- Connes–Consani, *Scaling site* / arithmetic site (`deg(Frob)=q ⟶ ℝ₊*` scaling flow).
- Prior loop: `research/log/2026-06-06-a5-function-field-refuted.md` (DONE #1).
