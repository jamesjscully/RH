# M4C — The weight-2 NS Hodge index IS M1's canonical duality pairing (NOT a metric); `D∘D≅id` on the lattice [COHERENCE · anchored vs 𝔽_q]

**Charter:** `construction-program.md` §0 (the design law: the polarization is the **canonical pairing
of the duality `D`, NEVER a metric**) + §1 clause C4. **Contract:** `M1-universal-property-S_Z.md` C4
(`P = ev∘(1⊗φ_{FE})`) and the involutive duality `D∘D≅id`. **Built on:** M4A (`gr^W_2` is the carrier),
M4B (the explicit intersection form `(*)` `a·b=d₁e₂+d₂e₁−Tr(z∘w)` and the Rosati polarization
`Tr(z w^†)`). **Module:** `scripts/numerics/witness/ns_hodge_index_duality.py`
(run: `python3 -m scripts.numerics.witness.ns_hodge_index_duality`). **Falsifier row added** (`falsify.py`).

---

## The task — lift M2's C4 fact from the weight-1 `H^1` to the weight-2 NS lattice

M2 proved, **on the weight-1 carrier `H^1`**, that the FF polarization
`P_duality = ev∘(1⊗φ_{FE}) = Tr(φψ^†)` equals the "metric-looking" Gram to `0.00e+00` — so the
polarization is the **canonical pairing of the duality `D`, not a chosen metric** (charter §0). M4A/M4B
then re-typed the carrier: the RH content of the self-product surface lives at **weight 2**, on the
Néron–Severi lattice `gr^W_2 = End(H^1)` (eigenvalues `αᵢαⱼ`, `|αᵢαⱼ|=q`), with M4B's form `(*)` and
the Rosati polarization `Tr(z w^†)` in hand. **M4C checks that the M2 C4 fact survives the lift** —
that the weight-2 NS Hodge index is M1's C4 categorical duality pairing, not a metric.

### The structure made precise — the duality `D` on the weight-2 lattice

The transcendental part of the weight-2 NS lattice is `End(H^1) = H^1 ⊗ (H^1)^∨`. M1's duality `D`,
restricted to this tensor square, is the involution
```
  D : End(H^1) → End(H^1),   z ↦ z^† = E^{-1} z^T E       (the two-sided Rosati / Poincaré adjoint),
```
the **same Rosati** that plays M1's complex conjugation `c` on `H^1`, now acting on `End(H^1)` by
conjugation of endomorphisms. Two facts make it a genuine categorical duality on the lattice:

- **(D-INVOL)** `D∘D = id`: `(z^†)^† = z` exactly, because `E^{-1}(E^{-1}z^TE)^TE = E^{-1}E^Tz(E^{-1})^TE = z`
  (the cup product `E` is alternating, `E^T=−E`, the two signs cancel). The weight-2 lattice is a
  **dualizable (rigid)** object: M1's involutive-duality axiom holds **on `gr^W_2`**, not merely on `H^1`.
  *(This is the M2c involutivity check, now performed on the weight-2 lattice.)*
- **(D-EVAL)** The canonical evaluation pairing of `D` on `End(H^1)` is
  `P_NS(z,w) = ev∘(1⊗φ_{FE})(z⊗w) = Tr(z·D(w)) = Tr(z w^†)`, where `ev` is the categorical trace (the
  weight-2 Künneth evaluation) and `φ_{FE}=D`. This **IS** M4B's Rosati polarization `Tr(z w^†)`, now
  exhibited as the canonical pairing of `D` — the weight-2 analogue of M2's C4. No metric is chosen
  (`E` is the cup product, `ev` the trace), so it evades the §0 Sylvester no-go **by construction**.

The NS-primitive subspace is the trace-zero part `End₀(H^1) = {z : Tr z = 0}` (M4B's
`F₀ = F − (Tr F/2g)Id`); the weight-2 Hodge index is `−P_NS(z₀,z₀) = −Tr(z₀ z₀^†)`.

---

## The decisive anchor findings (EXACT; `g=1` NS rank 4, `g=2` NS rank 16)

**(i) `D∘D = id` ON the weight-2 lattice — `gr^W_2` is rigid.** `max‖D(D(z))−z‖ = 0.00e+00` over a
spanning basis of `End(H^1)`, for `g=1` (NS rank 4) AND `g=2` (NS rank 16). M1's involutive-duality
axiom holds on the weight-2 lattice, not only on `H^1`.

**(ii) `P_NS = ev∘(1⊗φ_{FE})` EQUALS the Rosati Gram to `0.00e+00` — the C4 design law, on weight 2.**
Building the weight-2 pairing two ways — `P_dual(z,w)=Tr(z·D(w))` (canonical co-evaluation of `D`) and
`P_gram(z,w)=Tr(z w^†)` (M4B's Rosati Gram) — gives `max|P_dual−P_gram| = 0.00e+00` over a spanning basis
of `End(H^1)`, all 6 curves. **The weight-2 NS polarization is FORCED by the cup product, NOT a chosen
metric** — M2's C4=0 fact, lifted from the weight-1 `H^1` to the weight-2 NS lattice.

**(iii) The off-circle inertia flip IS the weight-2 Hodge index of `D`.** On NS-primitives `End₀`,
`−Tr(F₀F₀^†)` is negative on-circle (`g=1`: `−3.5,−8,−13.5,−17.5,−13.5`; `g=2`: `−7.75`) and **gains a
`+`** off-circle (plant `{r√q, √q/r}`, product `q`, `|·|≠√q`: `g=1` signature `(0,1,1)→(1,0,1)`; `g=2`
`−7.75→−1.66`, gains a `+`), the flip eigenvalue `= Σ|αᵢ|²−2gq` (the modulus defect). This is the SAME
`(0,1,1)→(1,0,1)` flip of M2/M4B — now exhibited as **the Hodge index of the canonical duality pairing
`P_NS = ev∘(1⊗φ_{FE})`** on the weight-2 lattice. Negative-definite on NS-primitives ⟺ `|αᵢ|=√q` ⟺ RH.

### The load-bearing fix (settles the M4D / M2c concern in passing)

The first build used a **companion-matrix** Frobenius with a fixed block cup product; at `g=2` this gave
`F^T E F = qE` residual `4.0` (not a `q`-similitude) — the off-circle `g=2` row then read FALSE, a
construction artifact, not structure. The fix: build `F` and `E` **together in the Rosati-paired basis**
(each Weil pair `(α, q/α)` → block `diag(α, q/α)` with `E`-block `[[0,1],[-1,0]]`, so `α·(q/α)=q` gives
the similitude **by construction**, on or off the circle). Residual drops to `2e-15` at `g=2`, and the
three facts persist at genuine rank 16: `Tr(F F^†)=8=2gq`, on-circle H-index `−7.75<0`, flip `True`.
**So the `g=1` `(0,1,1)` semidefiniteness was a trace-kernel/rank artifact, not structure** — exactly the
M2c/M4D question, answered here: the weight-2 Hodge index is genuinely non-semidefinite and the flip
mechanism survives at real rank.

---

## What M4C establishes (M1's C4, on the descent's actual carrier)

> **[for M4].** The polarization the descent must build is now pinned as a **categorical object on the
> weight-2 NS lattice**: a rigid dualizable lattice (`D∘D≅id`) whose polarization is the **canonical
> evaluation `ev∘(1⊗φ_{FE})` of its duality** (`= Tr(z w^†)` to `0`), NOT a metric, with the Hodge index
> on NS-primitives = RH. M1's C4 / charter §0 design law is therefore satisfied **on `gr^W_2`** — the
> place M4's `ζ`-descent must assemble the form `(*)` (Euler-assembled from `αᵢ(p)αⱼ(p)` across all
> primes, M4B). The remaining `ℤ`-hardness is unchanged: the single hinge C3b (the Euler-borne radius),
> now to be realized as the Euler-assembly of `P_NS` on the global weight-2 lattice.

---

## Falsifier verdict (M4C — a COHERENCE check on the FF anchor, CIRCULAR over `ℤ` as expected)

- **Euler-ASSEMBLED YES** — `P_NS` reads `Tr(z w^†)`, whose Frobenius value `Tr(F F^†)=Σ|αᵢ|²=2gq` is
  the Euler-borne Satake data; the weight-2 eigenvalues `αᵢαⱼ` are Satake products. DH has no `f×f`
  product ⟹ no `End(H^1)`-Frobenius ⟹ no weight-2 lattice ⟹ no `P_NS`. DH-failing.
- **SEES-ZEROS YES** — the weight-2 Hodge index `−Tr(z₀ z₀^†)` flips when a zero leaves `|αᵢ|=√q`.
- **INDEPENDENT NO** — over `𝔽_q` this **is** the Weil Hodge-index theorem = RH ⟹ **CIRCULAR over `ℤ`**,
  expected and correct for a coherence check on the anchor.

**NEW content (not circular):** `D∘D = id` **ON** the weight-2 lattice (it is rigid/dualizable), and
`P_NS = ev∘(1⊗φ_{FE}) = Tr(z w^†)` to `0.00e+00` — so M1's C4 ("the polarization is the canonical
duality pairing, NOT a metric") is now established **on the weight-2 NS lattice** where M4's descent
must build it; and the `g=2` rank-16 anchor confirms the Hodge index is genuinely non-semidefinite
(the `g=1` semidefiniteness was a rank artifact), settling the M2c/M4D concern.

---

## Verdict

`[COHERENCE · anchored vs 𝔽_q]` — **M1's C4 holds on the weight-2 NS lattice `gr^W_2`**: the duality
`D : z↦z^†` is **involutive** (`D∘D=id`, `0.00e+00`, the lattice is rigid), its **canonical evaluation
pairing** `P_NS=ev∘(1⊗φ_{FE})=Tr(z·D(w))` equals the Rosati Gram `Tr(z w^†)` to `0.00e+00` (the
polarization is the duality pairing, **NOT a metric** — the §0 design law lifted from weight 1 to weight
2), and the **off-circle inertia flip** `(0,1,1)→(1,0,1)` is the **Hodge index of `P_NS`** on
NS-primitives (neg-definite ⟺ `|αᵢ|=√q` ⟺ RH). Verified EXACT at `g=1` (rank 4) and `g=2` (rank 16); the
load-bearing fix (build `F,E` in the Rosati-paired basis so `F^TEF=qE` holds by construction) confirms
the `g=2` Hodge index is genuinely non-semidefinite, settling the M2c/M4D trace-kernel concern. **Not
overclaimed:** an FF anchor / coherence check, CIRCULAR over `ℤ` as expected; the new content is that the
C4 categorical-not-metric design law now holds on the weight-2 carrier M4's descent must build.
**Successors named:** M2c is now largely subsumed (involutivity + the `g=2` non-semidefiniteness done on
`gr^W_2`); what remains is **(M2c′)** prove `φ_{FE}` is a *morphism* (not just a matrix) and `c` is
compatible with `D` up to the Tate twist, as a functor of a rigid tensor category; and **(M4′)** the
descent now has a fully-typed target — Euler-assemble `P_NS` (the form `(*)`) on the GLOBAL weight-2
lattice from `αᵢ(p)αⱼ(p)`, the single hinge C3b.
