# NG candidate 3 — the *-autonomous / C* / dagger-compact off-line test [NO-GO COMPLETION]

**Charter.** `research/new-geometry-program.md`. Candidate 3 was named by candidate 2's Grothendieck move
(`NG-frob-synthesis.md` §5) as the **single unclosed door**: a *-autonomous / Hermitian-self-dual / C*-category
structure is the one place positivity might be **built into the duality** rather than imported. The decisive
question, stated as the falsifiable audit:

> Does a *-autonomous / Hermitian-self-dual / C*-category structure **FORCE** the polarization positivity
> (Step B: `|α|=√q` = `F†=F̄` = RH = compact motivic Galois) **from the duality itself**, making the off-line
> Frobenius datum **INCONSISTENT** (→ EXCEPTION, new geometry) — or does the off-line datum still admit a
> consistent *-structure, so positive-definiteness (C*) is the imported extra (→ NOGO_COMPLETE)?

**Prior result (candidate 2, `NG-frob-synthesis.md`):** off-line `F` generates a CONSISTENT non-polarizable
rigid Tannakian category. The sharpening here: the C* / dagger upgrade is exactly where a *non-degenerate*
self-duality (sign-free) might be forced to a *positive* (signed) one. Doplicher–Roberts is the real theorem
to engage: a compact group is reconstructed from a genuine **C\* (positive)** tensor category; an indefinite
*-category gives a non-compact real form. So the binary is: **does ζ's Frobenius datum give a C\*-category
without assuming the radius?**

---

## The decisive computation

Datum: `F` = 2×2 "Frobenius" block with a conjugate eigenvalue pair `α = r·e^{±it}`, `|α| = r`. On-line
`r = √q`; off-line `r = 1.3√q` (Re ρ > ½) and `r = 0.6√q` (Re ρ < ½). `q = 7`, anchored to `𝔽_q`.

### Test 1 — the C* (positive-definite) invariant form, anchored to F's OWN modulus

A *-autonomous / Hermitian-self-dual structure on `(V,F)` is a non-degenerate sesquilinear `H` with `F` a
**similitude**: `F* H F = μ·H` for a weight `μ`. The C* (Hilbert) condition is `H > 0` — then `F/√μ` is
`H`-unitary. The naive expectation (EXCEPTION) is that `H > 0` forces `μ = q`, i.e. `|α| = √q`. **It does not.**

Building the form from `F` ALONE — `μ = |det F| = r²`, F's intrinsic degree, with no imported external `q`:

| case | `\|α\|` | intrinsic `μ=\|detF\|` | # Hermitian solutions of `F*HF=μH` | a POSITIVE-DEFINITE one exists? |
|---|---|---|---|---|
| ON-LINE `r=√q` | 2.6458 | 7.00 | 4 | **YES** (sig `(+2,−0)`) |
| OFF-LINE `r=1.3√q` | 3.4395 | 11.83 | 4 | **YES** (sig `(+2,−0)`) |
| OFF-LINE `r=0.6√q` | 1.5875 | 2.52 | 4 | **YES** (sig `(+2,−0)`) |

Equivalently and cleanly: **`F/r` is unitarizable at EVERY radius** — `F/r` has eigenvalues on the unit
circle for any `r` (residual `‖(F/r)*H(F/r) − H‖/‖H‖ < 4e-16` in all three cases), so an invariant
**positive-definite** `H` exists on-line AND off-line. A semisimple map with all eigenvalue moduli equal is
unitarizable after dividing by its own modulus. **Positivity needs only `|α_i|` all EQUAL (one circle), NOT
`|α| = √q`.** [computed, this session]

### Test 2 — the EXTERNAL-`q` similitude is the circular import

Imposing the *external* `q` as the multiplier — `F* H F = q·H`, `q=7` fixed — gives the opposite, and it is
the trap:

| case | `\|α\|` | `# Hermitian solutions of F*HF=q·H` |
|---|---|---|
| ON-LINE `r=√q` | 2.6458 | 4 (incl. a positive-definite one) |
| OFF-LINE `r=1.3√q` | 3.4395 | **0** |
| OFF-LINE `r=0.6√q` | 1.5875 | **0** |

Off-line there is **no** invariant Hermitian form at all relative to the external `q`. This *looks* like
positivity forced — but it is **anchoring to the arithmetic `q` that produced the obstruction**, not the
*-structure. The `q` is exactly the imported finite-ground datum the whole program identifies (it is
`rosati_circularity_skeptic.py`'s `F·F† = r² ≠ q` off-circle, re-derived on the Hermitian-form side). The
*-autonomous structure built honestly from `F` (Test 1) uses `r²`, not `q`, and is positive-definite at every
radius. **The "forcing" is the circularity, caught.**

### Test 3 — where the genuine Krein/indefinite case lives (and why ζ is not in it)

The indefinite (Krein/Pontryagin) regime appears only with **UNEQUAL moduli**. `F = diag(2, 0.5)` (moduli
`2 ≠ 0.5`): the single-multiplier C* similitude form FAILS (no positive form pairs two different circles);
only an **indefinite** `(+1,−1)` form survives (at `μ=1`, pairing `α` with `1/ᾱ`). **But the ζ/Frobenius
datum is a single Weil-number conjugate pair — equal modulus by construction** — so it is ALWAYS in the
C*/positive case relative to its own modulus, never pushed into the Krein regime by anything intrinsic, and
never forced onto `√q`. [computed]

---

## Anchor (`𝔽_q`) and DH

**Anchor.** Over `𝔽_q` the genuine geometric Frobenius DOES land on `|α|=√q` — but that is **Weil II**
(Rankin-squaring + degeneration monodromy), an external theorem fixing the *scale* `√q`, exactly the imported
datum. The *-/C* structure reproduces the equal-modulus → unitarizable picture for **every** `r`; it supplies
the positive form but not the *value* of the radius. Compactness is downstream of purity, not upstream
(matches `NG-frob-synthesis.md` §2). [computed: the positive-definite `H` exists at all three radii.]

**DH — FAILS (DH-blind at Step B).** `falsify.py` (re-run this session) confirms the program-wide verdict:
no FORCING functional exists; the closest Hermitian/Gram forms are **CIRCULAR** (PSD ⟺ all zeros real ⟺ RH,
no independent certificate) and a DH-like off-line zero multiset is **equally constructible**, giving the same
indefinite signature — "the form reads whatever zeros it is handed." The C* positivity here is anchored to
`F`'s own modulus, so it draws **no z/DH distinction at the radius**: DH shares the FE / duality / equal-modulus
structure and admits the same own-modulus C* form. **DH-blind at Step B = NOGO**, not a healthy "fails to exist."

---

## Verdict — NOGO_COMPLETE

> **The *-autonomous / Hermitian-self-dual / C\* upgrade does NOT force positivity onto the radius `√q`.**
> The off-line Frobenius datum admits a **positive-definite (C\*/Hilbert)** invariant Hermitian form at EVERY
> radius — relative to its OWN modulus `r²` — so it is a consistent **C\*-category**, not merely an indefinite
> Krein one. The off-line datum is therefore **CONSISTENT**, never inconsistent. **Positive-definiteness is
> FREE (it follows from equal eigenvalue moduli = one circle = semisimple unitarizability-after-scaling); what
> is IMPORTED is the *anchoring of the scale to the external `√q`*** — Weil II / the finite ground. Requiring
> the C\* multiplier to be the arithmetic `q` (Test 2: no off-line solution) is precisely **requiring RH** —
> the circularity, caught red-handed.

So the one place positivity might have been *built into the duality* does **not** build it in: a *-autonomous /
dagger-compact structure gives a *non-degenerate, even positive-definite* self-duality **at any radius**, and
the radius `√q` is a separate scale-fixing input. **Doplicher–Roberts gets a compact group from a C\*-category
— but ζ's datum is a C\*-category at every radius, so DR reconstructs a compact group OFF-line too (compact
relative to the wrong, self-referential, scale).** The compact group is real; pinning its scale to `√q` is not.

**This COMPLETES the geometric no-go.** Candidate 1 imports **properness**; candidate 2 imports
**polarizability**; candidate 3 imports **the scale of the positive form** (the external `√q`) — and on the
sign question it goes further: positivity here is not even an *extra* choice, it is **automatic** (equal
moduli), with only the radius value imported. Across all three the same wall:

> **No coherence / duality / *-structure emits the VALUE `√q` (the arithmetic scale) from a self-duality.**
> A non-degenerate self-duality has no canonical sign; even when the sign is forced positive (equal moduli),
> the **scale** of the form — `r²` vs the arithmetic `q` — is a free external anchor. **Step B = the radius
> `√q` is always an imported finite-ground scale.** The geometric no-go is now a checked, candidate-independent
> proposition: positivity/sign was never the obstruction — the **arithmetic scale `√q`** is, and no metric-free
> geometry manufactures it.

**Off-line test (the schema's question):** an off-line `F` is **Hermitian-self-dual AND positive-definite (C\*)
relative to its own modulus** — *-autonomy does NOT make it inconsistent. Positivity is not even the extra; the
extra is the **scale `√q`**. → positivity NOT forced onto the radius → no-go complete.

---

### Numerics this session
- Invariant-similitude solver `F*HF=μH` (nullspace of `Fᵀ⊗F* − μI`, Hermitized): with intrinsic `μ=|detF|=r²`,
  a positive-definite `H` exists at all three radii (sig `(+2,−0)`); with external `μ=q`, **zero** off-line
  solutions. `F/r` unitarizable at every radius (invariance residual < 4e-16).
- Unequal-moduli `diag(2,0.5)`: C* form fails, only indefinite `(+1,−1)` survives — the Krein regime ζ's
  equal-modulus datum never enters.
- `falsify.py`: no FORCING; Hermitian/Gram forms CIRCULAR, DH equally constructible (DH-blind at Step B).

### Sources (real theorems engaged)
- **Doplicher–Roberts** (duality for compact groups): a compact group is reconstructed from a **C\* (positive)**
  symmetric tensor category with conjugates and positive dimensions. Engaged: ζ's datum is C\* at every radius,
  so DR yields a compact group off-line too — relative to F's own scale, not `√q`.
- Deligne–Milne, *Tannakian Categories* Thm 2.11: neutral Tannakian = `Rep(G)`; **polarization = sesquilinear
  forms WITH positivity** = extra structure. Confirmed: positivity here free (equal moduli), scale imported.
- Weil II / Deligne purity, algebraic Sato–Tate (`ST(A)` = max compact of `TL(A)(ℂ)`, normalized `q^{−1/2}g`):
  fixes the *scale* `√q` — the imported anchor.
- Krein/Pontryagin-space *-representations: indefinite-metric reps give **non-compact real forms** — the regime
  ζ's equal-modulus datum avoids, so it stays C* (positive) without buying the radius.
