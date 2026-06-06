# R1 — the residue as the MONODROMY-WEIGHT question; the archimedean `N` pinned [DEF · coherence-checked vs 𝔽_q]

**Charter:** `construction-program.md` §1 (the polarization = duality, §0 design law), §4 (anchor
first). **Built on:** the keystone terminus (M3b, M4r, K2r-fix) — RH peeled to ONE irreducible atom:
the **even split `|α|=|β|`** = the Frobenius is a fixed point of the polarization involution = **purity**
= the archimedean weight-monodromy. **Mandate (AGENDA R1):** state the residue precisely as the
**monodromy-weight** question, pin down what an archimedean `N` must be and what "`M(N)=W` forces the
even split" requires, and **anchor on the FF datum that `M(N)=W ⟹ purity` with no zeros assumed.**
**Module:** `scripts/numerics/witness/weight_monodromy_residue.py`
(run: `python3 -m scripts.numerics.witness.weight_monodromy_residue`). **Falsifier row added** (now 35).

---

## The mechanism, stripped (object-free) — why `M(N)=W` IS the even split

A nilpotent endomorphism `N` on a finite-dim `V` (`N^{m+1}=0`) carries a **unique** increasing
**monodromy filtration** `M_•` centered at a weight `w`, characterized by

> `N·M_k ⊆ M_{k−2}` **and** `N^j : gr^M_{w+j} \xrightarrow{\sim} gr^M_{w−j}` (iso, all `j≥0`).

This is Jacobson–Morozov: `N` is the lowering operator of an `𝔰𝔩₂`-triple `(e,h,f)`, `h` acts on
`gr^M_k` by the scalar `k−w`, and the iso `N^j : gr_{w+j} ≅ gr_{w−j}` **is Hard Lefschetz** for that
`𝔰𝔩₂`. **The filtration is symmetric about `w` by construction** — and crucially this symmetry uses
**no eigenvalue and no zero location**; it is pure linear algebra of `N`.

**Weight-monodromy** (the load-bearing hypothesis, a THEOREM in the curve/abelian-variety case,
Grothendieck/Deligne, Weil II): the combinatorial `M(N)` **coincides with the arithmetic weight
filtration `W`** — the one on which Frobenius acts with `|eigenvalue| = q^{k/2}` on `gr^W_k`. Then:

> **`M(N)=W` ⟹ the even split.** The symmetry of `M(N)` about `w` transports to the **weights**: the
> weights are symmetric about `w`, and the `N`-**primitive centre** (`j=0`, where `N` acts as `0` on
> the graded) sits at **exactly** weight `w`, i.e. `|α| = q^{w/2}`. **Purity of the centre IS `M(N)=W`
> at `j=0`.** For a smooth proper curve `N=0`, `M(0)` is concentrated at `w` (pure) — the even split is
> immediate; the degeneration `N≠0` is the general mechanism, smooth being the `N=0` special case.

So over `𝔽_q` the even split is **not an extra hypothesis** — it is `M(N)=W`, a theorem.

---

## The FF anchor (exact rational linear algebra; `g=1,2,3`; NO zeros assumed)

Built a **genuine nilpotent `N`** on `H^1` (dim `2g`, weight `w=1`) from the geometry of a
degenerating family, and computed `M(N)` **purely from `N`** (Jordan structure via the rank sequence
`r_k = rank N^k`), with **no arithmetic / no eigenvalue input**:

| model | `N` | `M(N)` graded dims | symmetric about `w=1`? | even split |
|---|---|---|:--:|---|
| **smooth** curve | `N=0` | `{1 : 2g}` | trivially (pure) | `|α|=q^{1/2}` immediately |
| **semistable** (max-degenerate, Mumford) | `[[0,0],[I,0]]`, index 2, rank `g` | `{0:g, 2:g}` | **YES** (`dim gr_2 = dim gr_0 = g`) | centre via `0↔2` Hard-Lefschetz pairing |
| **partial** (pinch `g−1`, keep 1 abelian handle) | index 2, rank `g−1` | `{0:1, 1:2, 2:1}` | **YES** | **populated centre `gr^M_1` carries 2 eigenvalues of `|α|=q^{1/2}`, the even split VISIBLE** |

Every symmetry verdict is read off `N`'s Jordan blocks (`N^j: gr_{w+j} ≅ gr_{w−j}`), **using no zero.**
The semistable model has an empty `gr_1` (the even split appears as the `0↔2` pairing about the
centre); the **partial** model populates `gr_1` explicitly, so `|α|=q^{(1/2)}` at the centre is shown
directly. Both confirm: **`M(N)` is symmetric about `w` by Jacobson–Morozov, and `M(N)=W` then forces
`|α|=q^{w/2}`** — the residue's mechanism, anchored.

---

## The archimedean `N`, PINNED to four axioms (the residue handed to R2/R4)

An archimedean `N` forcing `|α|=|β|` (the even split at `∞`) must be a nilpotent operator on the
archimedean realization `V_∞ = H^1 ⊗ ℂ` with the `(p,q)` Hodge datum, satisfying **all** of:

- **(N1) NILPOTENT** — `N^{w+1}=0` on the weight-`w` piece (so `M(N)` exists and is finite).
- **(N2) A `(−1,−1)`-MORPHISM of the polarized HS** — `N(F^p) ⊆ F^{p−1}`, compatible with the real
  structure `c` (`N` shifts `(p,q)` by `(−1,−1)`); this is exactly the type of a monodromy log /
  limiting MHS nilpotent.
- **(N3) `M(N)=W`** — the monodromy filtration centered at `w` **coincides with the archimedean weight
  filtration `W`**: the **archimedean weight-monodromy.**
- **(N4) RADIUS COMPATIBILITY** — on `gr^M_k` the archimedean "Frobenius" (the `C_W` **radius** / the
  scale `d` of M3b/K2r-fix, the Euler-borne half) has modulus `q^{k/2}`, so `M(N)=W` transports `M(N)`'s
  symmetry to the **radius** (not merely the parity).

**The obstruction located (what `ℤ` lacks that `𝔽_q`'s degeneration provides).** Over `𝔽_q` the
nilpotent `N` **comes from geometry** — it is the log of the **local monodromy** of a degenerating
family (a Picard–Lefschetz vanishing cycle / a node), a geometric datum, **not a function of the
zeros.** Over `ℤ` / at `∞` there is **no degenerating family in hand** to supply `N`. This is the
precise upstream gap: the residue is not "prove `M(N)=W`" but "**supply the geometric `N` whose
`M(N)` could equal `W`.**" (Mirror of M2d's lesson: the open problem is upstream — *build the carrier*
purity is a property of; here, *supply the `N`* whose monodromy filtration is the weight filtration.)

---

## DH falsifier (the archimedean weight-monodromy must FAIL to exist for Davenport–Heilbronn)

DH has **no Euler product ⟹ no Frobenius weight ⟹ no weight filtration `W`** to identify `M(N)` with.
Even if a formal nilpotent `N` could be written, **(N3) `M(N)=W` is VACUOUS**: there is no `W` (no
`|α|=q^{k/2}` structure, no Satake). So the archimedean weight-monodromy **structure `(N, W)` with
`M(N)=W` FAILS TO EXIST for DH at (N3).** Ladder `DH < ζ < FF`: DH has **no `W`** (no monodromy-weight
question at all); `ζ` has a putative `W` (the would-be purity) and an **OPEN** archimedean `N`; FF has
both (`N` geometric, `M(N)=W` a theorem).

---

## Falsifier verdict (R1 — a characterization/coherence result, Euler-silent by design)

- **EULER-BORNE — NO ON THIS PASS, by design.** Like M2d/M3b, R1 **types/characterizes** the residue
  and **anchors** it on `𝔽_q`; it is not a standalone `ℤ`-positivity form. Tabled **DISPERSING-by-
  design** (`euler_borne=False`). The **structural** DH verdict is nonetheless sharp: `(N3)` is vacuous
  for DH (no `W`), so the weight-monodromy structure does not exist for DH.
- **SEES-ZEROS — YES.** The even split = purity = exactly where the zeros sit (the radius).
- **INDEPENDENT — NO.** `M(N)=W ⟹` purity = Weil II = the solved case; over `ℤ` this is RH.

**NEW content (not circular):** the residue is now stated as a **single, geometric question** — *is
there an archimedean nilpotent `N` (a `(−1,−1)`-morphism of the polarized HS) with `M(N)=W` forcing the
radius?* — with the FF anchor proving the **mechanism is `M(N)=W`-with-no-zeros** (the symmetry of
`M(N)` is intrinsic to `N`; `M(N)=W` transports it to force `|α|=q^{w/2}`), and the obstruction located
**upstream**: `ℤ` lacks the geometric degeneration that supplies `N`. This sharpens the keystone's
"the radius must be Euler-assembled, never read off the archimedean place" (M3b/M4r) to its **precise
positive form**: the radius would be forced **if** an archimedean `N` with `M(N)=W` existed — and that
existence (the degeneration over `ℤ`) is the irreducible open object.

---

## Verdict

`[DEF · coherence-checked vs 𝔽_q]` — **the residue is the MONODROMY-WEIGHT question.** Over `𝔽_q` the
even split `|α|=q^{w/2}` is `M(N)=W` (the monodromy filtration of the geometric nilpotent = the weight
filtration), a theorem; the symmetry of `M(N)` — **intrinsic to `N`, no zeros** — transports to the
weights via `M(N)=W` and forces purity. **Anchored EXACTLY** on the FF semistable/partial datum
(`g=1,2,3`, exact Jordan computation): `M(N)` is symmetric about `w=1` by Jacobson–Morozov, and
`M(N)=W ⟹` the even split with **no eigenvalue/zero read**; the partial model shows the populated
weight-1 centre carrying the `|α|=q^{1/2}` eigenvalues directly. The archimedean `N` is **pinned to four
axioms (N1)–(N4)**; the **obstruction** (`ℤ` lacks the geometric degeneration `𝔽_q` uses to supply `N`)
is located and handed to **R2** (Schmid's SL(2)-orbit, where archimedean weight-monodromy IS a theorem
for a degenerating family of Hodge structures: does its `N` give the **radius** or only the free parity
`(−1)^w`?). **DH fails at (N3):** no `W` ⟹ no monodromy-weight question. **Not overclaimed:** this
characterizes the residue and proves the FF mechanism uses no zeros; it does not construct the
archimedean `N`. **Successor named:** R2 — does Schmid's SL(2)-orbit nilpotent supply an `N` satisfying
(N1)–(N4), in particular (N4) the RADIUS (not just the free parity)?
