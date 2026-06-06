# M4B — The self-intersection of the arithmetic diagonal of `S²/ℤ` on the weight-2 NS lattice, as a representability problem [BUILD/REPRESENT · anchored vs 𝔽_q]

**Charter:** `construction-program.md` §1 (the carrier the descent must supply), §4 (anchor first),
§5 (M4). **Built on:** M4A (`M4A-weight-carrier.md`), which decided the descent's carrier is **`gr^W_2`**
— the weight-2 Néron–Severi lattice `H^1(C)⊗H^1(C) ⊂ H^2(C×C)`, eigenvalues `αᵢαⱼ`, `|αᵢαⱼ|=q`.
**Module:** `scripts/numerics/witness/ns_diagonal_representability.py`
(run: `python3 -m scripts.numerics.witness.ns_diagonal_representability`). **Falsifier row added**
(`falsify.py`, 45 rows). **Beware (DONE):** `square_representability.py` closed the **naive product**
`S×S` (its `H^1⊗H^1` factorizes as base⊗base, RH-silent); M4B must build the lattice with an
**INDECOMPOSABLE** diagonal, not a tensor-product form.

---

## The deliverable — the representability functor and the distinguished diagonal

[DEF · the representability frame.] Rationally, the weight-2 NS lattice of `C×C` (genus `g`) splits as

```
  NS(C×C) ⊗ ℚ  =  ⟨C×pt⟩ ⊕ ⟨pt×C⟩ ⊕ End(H^1(C)),
```

the two **fiber classes** `f=C×pt`, `f'=pt×C` spanning the hyperbolic product part
(`f²=f'²=0`, `f·f'=1`, signature `(1,1)`), and `End(H^1)` the **transcendental/correspondence** part
where Frobenius and the diagonal live. A correspondence `Z⊂C×C` is **represented** by the triple

```
  rep_NS(Z) = ( d₁ = Z·(pt×C),  z = action of Z on H^1(C),  d₂ = Z·(C×pt) ),
```

and the NS intersection pairing of `a=(d₁,z,d₂)`, `b=(e₁,w,e₂)` is

```
  a · b  =  d₁e₂ + d₂e₁  −  Tr(z∘w)                                          (*)
```

— the hyperbolic fiber pairing plus the `H^1⊗H^1` (weight-2 middle) trace term with the alternating
Künneth sign. The **distinguished object** is the diagonal `Δ = rep_NS(diagonal) = (1, Id_{H^1}, 1)`.

> **[DEF · the M4B representability problem].** Over `ℤ`: what represents the functor
> `rep_NS : Corr → (ℤ-lattice, form (*))` for `ζ`? An arithmetic object carrying (i) a "diagonal"
> with an **indecomposable** `End`-component, (ii) a Frobenius/Hecke graph `Γ` with
> `Δ·Γₙ =` the explicit-formula trace (the analogue of `#C(𝔽_{qⁿ})`), and (iii) the form `(*)` on
> `End` **Euler-assembled** from the Satake products `αᵢ(p)αⱼ(p)` across **all primes** — the global
> object M2d proved no single prime supplies.

---

## The decisive anchor findings (EXACT over the Weil curves)

ANCHOR FIRST (the one place the mechanism is a theorem), 5 Weil curves `g=1`, `q=2,5,7,11,13`:

**(1) The lattice carries `Δ` and `Γ_F`; the self-intersection IS the Lefschetz trace.**
`Δ=(1,Id,1)`, `Γ_{Fⁿ}=(qⁿ, Fⁿ, 1)`, and via `(*)`:

```
  Δ · Γ_{Fⁿ}  =  1·1 + 1·qⁿ − Tr(Fⁿ)  =  qⁿ + 1 − Σ αᵢⁿ  =  #C(𝔽_{qⁿ}).
```

Verified EXACT (`<1e-12`) for `n=1,2,3` on all curves (e.g. `q=5`: `4, 32, 148`; `q=13`: `9, 171,
2268`). **The Lefschetz fixed-point formula is the NS self-intersection of the arithmetic diagonal
against the Frobenius graph** — exactly the structure the descent must reproduce: the diagonal pairs
against Frobenius powers to give the Euler-borne point counts / the explicit-formula trace.

**(2) The diagonal is INDECOMPOSABLE — the `square_representability` trap avoided.**
The `End(H^1)`-component of `Δ` is `Id ≠ 0` (NS-norm `‖Id‖=√(2g)=1.414`), while **every product/fiber
class acts as `0` on `H^1`** (a divisor pulled back from a factor is supported on a fiber and kills
`H^1`; measured `‖End(fiber)‖=0.0000`). So `Δ ∉ ⟨C×pt, pt×C⟩` — it has a genuine **primitive
(transcendental) component**. The naive product surface's Künneth slot factored
(`square_representability.py`) because it used the **product** classes; the **diagonal does not factor**
— it is the indecomposable correspondence M4B was asked to build. `Δ·Δ = 2−2g = χ(C)` (finite).

**(3) The Hodge index on the primitive `End`-part = RH, via the Rosati polarization (not a bare trace).**
The intersection form on the primitive `End`-part, made a **polarization**, is `⟨z,w⟩ = Tr(z·w^†)` with
the **Rosati adjoint** `w^† = E^{-1}w^T E` (`E` = cup product / Weil pairing, `F^T E F = qE` verified
residual `0.0`). Rosati positivity `Tr(z z^†) > 0` is the **Weil positivity = RH**. On Frobenius:

```
  Tr(F F^†) = Σ αᵢ αᵢ^† = Σ |αᵢ|² = 2gq    ON-circle   (each αα^†=q)        [=4,10,14,22,26 verified]
```

The **primitive diagonal self-intersection** (trace-zero `F₀ = F − (Tr F/2g)Id`): `−Tr(F₀F₀^†) < 0`
ON-circle (Weil neg-definite; `−3.5,−8,−13.5,−17.5,−13.5`) and **FLIPS to `> 0` OFF-circle** (plant
`{r√q, √q/r}`, product `q`, `|·|≠√q`; `+0.69,+1.74,+2.43,+3.82,+4.51`) — the `(0,1,1)→(1,0,1)` inertia
flip of M2 / `euler_movable_inertia.py`, now **read on the weight-2 NS lattice**. The Hodge index on
NS-primitives is negative-definite ⟺ `|αᵢ|=√q` ⟺ RH.

---

## What M4B sharpens (the descent's target, now concrete)

> **[for M4].** The descent's deliverable is not "a lattice" but a **representability functor**
> `rep_NS` with the form `(*)`, a **distinguished indecomposable diagonal** whose `End`-component is
> not a product class, and a **Frobenius/Hecke graph** `Γ` realizing `Δ·Γₙ = ` the explicit-formula
> trace. The `ℤ` analogues are typed: `Δ·Γₙ` ↔ `Σ_ρ (…)` (the explicit formula); the `End`-form `(*)`
> ↔ the cross-place coupling `W_∞ ≥ Σ_p W_p`, **Euler-assembled** from `αᵢ(p)αⱼ(p)` across all primes;
> the indecomposability requirement ↔ the diagonal must NOT factor through one place (the
> `square_representability` / `hecke_correspondence` factorization trap). The Hodge index on
> NS-primitives, negative-definite ⟺ RH, is M1's C4 categorical duality pairing **on the weight-2
> lattice** — the M4C task.

---

## Falsifier verdict (M4B — an FF anchor / representability spec, CIRCULAR over `ℤ` as expected)

- **Euler-ASSEMBLED YES** — the form `(*)` reads `Tr(Fⁿ)=Σαᵢⁿ` = the Euler-borne Frobenius/Satake
  data; the weight-2 eigenvalues `αᵢαⱼ` are products of Satake `αᵢ`. **DH has no `f×f` product ⟹ no
  `End`-Frobenius ⟹ the `S²/DH` diagonal has no indecomposable correspondence component to
  self-intersect.** DH-failing.
- **SEES-ZEROS YES** — the primitive Hodge index `−Tr(F₀F₀^†)` flips sign when a zero leaves the circle
  (`|αᵢ|≠√q`), the `(0,1,1)→(1,0,1)` inertia flip on the weight-2 lattice.
- **INDEPENDENT NO** — over `𝔽_q` this **is** the Weil Hodge-index theorem = RH ⟹ **CIRCULAR over `ℤ`**,
  expected and correct for an anchor.

**NEW content (not circular):** the self-intersection of the arithmetic diagonal is the **functor
`rep_NS` with the explicit form `(*)`**; the diagonal is **INDECOMPOSABLE** (`End`-component `Id`,
norm `√(2g)`, not a product class — the `square_representability` factorization trap avoided); and
`Δ·Γ_{Fⁿ}=#C(𝔽_{qⁿ})` realizes the **Lefschetz trace as the NS self-intersection**, the FF archetype of
the explicit-formula trace. The `ℤ`-question is now sharp: what represents `rep_NS` for `ζ`,
Euler-assembled from `αᵢ(p)αⱼ(p)` across all primes.

---

## Verdict

`[BUILD/REPRESENT · anchored vs 𝔽_q]` — **the self-intersection of the arithmetic diagonal of `S²/ℤ`
on the weight-2 NS lattice is the representability functor `rep_NS : Corr → (lattice, form (*))` with
the distinguished diagonal `Δ=(1,Id,1)`**, anchored EXACTLY on 5 Weil curves: `Δ·Γ_{Fⁿ}=#C(𝔽_{qⁿ})`
(the Lefschetz trace = the NS self-intersection), `Δ` is **indecomposable** (`End`-component `Id≠0`,
not a product class — avoiding the closed naive-product trap), and the primitive Hodge index via the
**Rosati polarization** `Tr(z w^†)` is negative-definite ⟺ `|αᵢ|=√q` ⟺ RH (the weight-2 inertia flip).
**Not overclaimed:** this builds and types the FF representability spec; the `ℤ` lattice is untouched
and the FF anchor is CIRCULAR over `ℤ` as expected. **Successors named:** M4C (the Hodge index on
`gr^W_2`-primitives as M1's C4 categorical duality pairing, **on this NS lattice** — now with the
explicit form `(*)` and the Rosati polarization in hand); M4 re-targeted (the descent must build
`rep_NS` for `ζ`, Euler-assembling the form `(*)` from `αᵢ(p)αⱼ(p)`); a new item — **build the FF
`g=2` NS lattice (rank `16`) and confirm the indecomposable diagonal / Hodge-index flip persists at
genuine non-semidefinite rank**, the M4C/M2c `g=2` anchor.
