# The missing object — a precise characterization (2026-06-06)

Synthesis of the function-field template, the analytic shadow (`weil_form.py`), and three
independent programs (`arakelov-arithmetic-surface.md`, `connes-consani-scaling-site.md`,
`deninger-spectral-cohomology.md`). Throughout, **[THM]** = theorem, **[PROG]** = program /
defined-but-incomplete, **[CONJ]** = conjectural, **[AN]** = analogy.

The three programs are different attempts at the *same* object. They specify it to remarkable
precision and **converge on the same irreducible gap**. This file states the object's required
properties, what exists, and exactly what is missing.

---

## 1. The template that works (function fields) — the dictionary

For a smooth projective curve `C/𝔽_q`, RH for `ζ_C` is **[THM]** (Weil 1948). The machine:

| ingredient | object |
|---|---|
| the zeros `α_i` of `ζ_C` | eigenvalues of **Frobenius** `Fr` on `H¹_ét(C̄, ℚ_ℓ)` (dim `2g`) |
| functional equation | **Poincaré duality** `H¹ × H¹ → H²` |
| `ζ_C` itself | `det(1 − Fr·t \mid H^•)` — a **Lefschetz trace formula** `#C(𝔽_{q^n}) = Σ_i (−1)^i Tr(Fr^n\mid H^i)` |
| **RH** (`\|α_i\|=q^{1/2}`) | **positivity of the intersection pairing on the surface `C × C`**: `(D·D) ≤ 0` on the primitive part (Hodge index / Castelnuovo), applied to `D = Γ_Fr − (\ldots)Δ` |

The proof is *geometric positivity on a surface*. RH is **not** an analytic accident there; it is
the Hodge index theorem on `C×C`.

## 2. The required properties of the missing object (what it MUST be)

The number-field analogue must be a **2-dimensional arithmetic object** — call it `S²` (the "square"
/ the arithmetic `C×C`) — carrying:

1. **A cohomology `H¹`** whose Frobenius/flow eigenvalues are exactly the nontrivial zeros `ρ` of
   `ζ` (so `Tr(Fr^t \mid H¹) = Σ_ρ e^{tρ}`). **[CONJ]** in every program.
2. **A Lefschetz trace formula** equal to the **Weil explicit formula** — the contributions are the
   **archimedean place** (the "fixed point", a digamma `Γ_ℝ` term) and the **primes** (the "closed
   orbits", `Λ(n)` at `log p^k`). The explicit formula *is* this trace **[THM, analytically]**; its
   realization as a geometric Lefschetz formula is **[PROG/CONJ]**.
3. **Poincaré/Serre duality** = the functional equation. **[CONJ]** on the square.
4. **An intersection pairing whose positivity is RH** — `(Δ·Γ_Fr) ≤ 0` / Hodge index / self-
   adjointness of the flow generator / Weil positivity. **This is the forcing structure.** **[CONJ]**.

## 3. The analytic shadow — the concrete object the geometry must explain (`weil_form.py`)

Property 2+4 have a concrete, computable form **now**, independent of any geometry: the **Weil
quadratic form**

  `W[a,b] = Σ_ρ φ̂_a(γ_ρ) \overline{φ̂_b(γ_ρ)}`   (spectral)   `= (∞: digamma) + (poles) − (primes: Λ(n))`  (arithmetic).

Verified (`weil_form.py`): `W` **is the RH-detector** — PSD on the true real zeros (min eig
`~−3e−16`), and a single planted off-line zero (`β=0.8`) breaks PSD (min eig `−1.49`). Positivity is
**manifest on the spectral (zero) side iff RH**, and **hidden on the arithmetic side**. *Making the
arithmetic-side positivity manifest, as a geometric intersection positivity, is the missing object's
entire job.* The archimedean term is the digamma `Γ_ℝ` factor — **RH-neutral** (shared identically
with Davenport–Heilbronn; `2026-06-06-edge-is-dispersing.md`); the primes are the RH-content.

## 4. What the three programs supply — and the one convergent gap

| program | the object it gives | what is built | the gap (verbatim-grounded) |
|---|---|---|---|
| **Connes–Consani Scaling Site** | the topos `(N̂^×, ℤ_max)`; its `ℝ_+^{max}`-points **= the adèle class space** [THM]; scaling flow = Frobenius; `ζ̂` = Lefschetz counting zeta as `q→1` [THM]; candidate `C×C` = the **square `S²`** | Riemann–Roch **[THM] on the 1-D prime orbits `C_p`**; Frobenius corr. `Ψ_λ`; the archimedean reduction `W_∞(g⋆g^*) ≥ Tr(ϑ S ϑ^*)` [THM, one place, conditional] | **No `H¹` / Riemann–Roch / Serre duality on the square `S²`** ("open at this time"); the **existence/effectivity half** (sign of `D·D` → effective divisor) is missing; the diagonal self-intersection / `logΛ` term is undefined; the complex lift loses the canonical Frobenius. |
| **Arakelov surface** | `\overline{Spec ℤ}` and arithmetic surfaces `X→Spec ℤ` [THM]; arithmetic Chow groups + intersection pairing (finite places + archimedean Green's function) [THM] | the **arithmetic Hodge index theorem** [THM] (Faltings–Hriljac: pairing neg-definite on the primitive part `= −ĥ_NT`) | it is **the right positivity on the WRONG surface** — a *relative curve* (the 2nd factor is the base, not a curve), with no Frobenius/diagonal whose self-intersection is the `ζ`-zero sum. The **self-product `Spec ℤ × Spec ℤ` does not exist** (`𝔽₁`); its archimedean diagonal term is the **BGS §6.3 positive-Green-form obstruction, which can genuinely fail**. |
| **Deninger / Connes spectral** | a (non-existent) **foliated dynamical system** `(X,φ^t,ℱ)`: closed orbits = primes, fixed points = `∞`, leafwise `H̄¹` carrying the flow generator `Θ`; zeros = `spec(Θ)`; `ζ̂` = regularized `det_∞(s−Θ)` [CONJ]. Connes' surrogate = the Scaling-Site square. | the **explicit formula = trace formula** [THM, semilocal]; zeros as an **absorption spectrum** on the adèle class space; self-adjointness ⇒ RH in a **toy foliated model** [THM] | the space is **unconstructed** (manifolds *provably excluded*); the **Lefschetz formula with fixed points is open** (dim > 1); the `det_∞ = ζ̂` identification and the **global Weil positivity** are unproven and only *equivalent* to RH. Connes' own statement: the missing piece is **"an intersection theory and a Riemann–Roch theorem on the square of the arithmetic site."** |

## 5. The precise characterization — what is missing, stated once

All three programs build the **object's points, its Frobenius flow, its 1-dimensional (prime-orbit /
archimedean) data, and the Lefschetz/trace identity** — and all three stop at the **same wall**:

> **The cohomology `H¹` on the square `S²` (the arithmetic `C×C`) — the `2g`-dimensional space that
> carries the zeros — has no construction, and with it neither does the intersection theory / Serre
> duality / Riemann–Roch on the square, nor the intersection positivity (`Δ·Γ_Fr ≤ 0` / self-
> adjointness / Weil positivity) that would *be* RH.**

Two things make this gap *irreducible*, not cosmetic:

1. **The positivity can genuinely fail.** BGS §6.3 proves positive Green forms do not always exist;
   Connes–Consani isolate the obstruction to the "small square" `Δ=[0,1]²` (a derivative jump at
   `ρ=1`, the analytic shadow of `Δ·Δ`). So the geometry must *force* a positivity that is false in
   general — exactly what an `H¹` with Serre duality provides over function fields, and exactly what
   is absent over `ℤ`.
2. **Without it the frameworks reduce RH only to Weil positivity** — the **only-known-equivalent,
   dispersing** endpoint (STRATEGY §1). They supply the *object on which a forcing structure would
   live*, not the forcing structure. The reverse force is precisely the missing `H¹`/positivity.

The archimedean / digamma / functional-equation data that all three programs *do* handle is the
**RH-neutral** part (it is shared with Davenport–Heilbronn — three independent confirmations:
`edge-is-dispersing`, the descent triviality, Angle 3). The RH content is the **subleading
intersection-positivity on the square**, which is exactly what does not exist.

## 6. Bottom line

The missing object is **specified to extraordinary precision** — a 2-dimensional arithmetic object
with an `H¹` realizing the zeros as flow/Frobenius eigenvalues, a Lefschetz trace formula equal to
the Weil explicit formula, Serre duality equal to the functional equation, and an intersection
positivity equal to RH — and its analytic shadow (the Weil form, `weil_form.py`) is a concrete,
computable, demonstrated RH-detector. **What does not exist is the `H¹` on the square and its
intersection positivity** — the single reverse-force-bearing ingredient, which (BGS §6.3) cannot be
true for purely formal reasons and so demands a genuine geometry over `Spec ℤ` (the `𝔽₁` /
Connes–Consani / Deninger program). That is the precise location, shape, and irreducibility of the
missing object — as far as honest characterization can take us without constructing it.
