# Resonance kernel — candidate (b), the Gram of the ZEROS — CLOSES the form-carries-the-zeros branch

**Item (AGENDA NEXT #1).** After `operator_domination.py` refuted candidate (a) (the prime side
`W = A − P`: Euler-borne but zero-location-blind), the agenda named the ONLY surviving
"form-carries-the-zeros" object: candidate (b), a **Gram of the zeros themselves**
`K_ij = Σ_ρ φ̂(γ_ρ; cᵢ) φ̂(γ_ρ; cⱼ)`, PSD iff all `γ_ρ` real (iff RH). Build `K`; run the falsifier to
decide whether it is an **independent** positivity certificate or merely `= weil_form.py`'s spectral
side (the Weil/Li positivity, CIRCULAR).

**Module.** `scripts/numerics/witness/resonance_kernel.py` (+ 1 `falsify.py` registry row).

## [THM] The object and its decisive structure

`V_{ρ,i} = φ̂(γ_ρ; cᵢ)` (rows indexed by zeros, columns by test-function centers), and
**`K = VᵀV`** — the **SYMMETRIC** outer product, NOT the Hermitian `V*V`. This is load-bearing:
the Weil explicit formula is `Σ_ρ ĥ(γ_ρ)` with `ĥ` the **even** real Fourier transform evaluated at
the (possibly complex) `γ_ρ`, so the bilinear is `φ̂(γ_ρ;cᵢ)φ̂(γ_ρ;cⱼ)` with **no conjugation**.

- For a **real** `γ_ρ`: contribution `a aᵀ` (PSD).
- For an **off-line** `γ_ρ = T − id` (`d = β − ½ ≠ 0`): the conjugation-closed contribution is
  `v vᵀ + v̄ v̄ᵀ = 2 Re(v vᵀ) = 2(a aᵀ − b bᵀ)` with `v = a + ib` — an **INDEFINITE** rank-2 block
  (one `+`, one `−`). So **`K ⪰ 0 ⟺ all γ_ρ real ⟺ RH`**.

(The Hermitian `V*V` gives `a aᵀ + b bᵀ`, PSD always — it would MISS the flip. That is the wrong
object; the Weil form is the symmetric one. Computed both: off-line, symmetric min eig `−0.0024`,
Hermitian min eig `+1.4e-7`.)

## [computed] The four experiments (5 centers, width 0.05, 200 ζ zeros)

1. **TRUE zeros — PSD by construction.** `sig(K) = (5,0,0)`, `min eig = +0.0067`. A Gram of REAL
   vectors.
2. **SEES-ZEROS — YES.** Plant an off-line zero `β = 0.8` (one row of `V` complex): `sig` flips to
   `(4,0,1)`, `min eig = −0.0024 < 0`. PSD-ness breaks.
3. **THE DECISIVE IDENTITY — INDEPENDENT NO (verified to `1.4e-17`).** For any `x`,
   `xᵀKx = Σ_ρ g(γ_ρ)²` with `g(γ) = Σ_i x_i φ̂(γ;cᵢ)`. This is **EXACTLY** the Weil
   explicit-formula ZERO SIDE = `weil_form.py`'s spectral form `W = Σ_ρ |Σ_a c_a φ̂_a(γ_ρ)|²`. `K` is
   its Gram representation. PSD-ness of `K` = "every `γ_ρ` is real" = RH, with **no** independent
   certificate: `K = VᵀV` is PSD iff `V` is real iff the zeros are real — a certificate of `K ⪰ 0`
   would BE a proof of RH.
4. **NOT EULER-BORNE.** `K` is built from the ZEROS ONLY and never references `Λ(n)`. A DH-like zero
   multiset (off-line zeros, no Euler product) is **equally constructible** and gives `K` indefinite,
   `sig (4,0,1)`, `min eig −0.009`. `K` reads whatever zeros it is handed — a **zero-side detector**
   (like the Li coefficients), NOT an Euler-product detector.

## Verdict (three-axis falsifier)

**Euler-borne NO** (reads zeros, agnostic to the product → DH-constructible) · **sees-zeros YES**
(by construction) · **independent NO** (= the Weil zero side, to `1.4e-17`). The classifier returns
**DISPERSING** (Euler axis dominates), and on the other axes **CIRCULAR**. **28th confirmation of the
standing wall.**

## [THM-flavored] Decisive lesson — the two candidates PINCER the wall

The "form-carries-the-zeros" branch is now CLOSED by an exhaustive two-candidate pincer:

- **candidate (a)** = the **prime side** `A − P` (`operator_domination.py`): Euler-borne YES, but
  `Λ(n)` is a property of ζ's Euler PRODUCT, not of where the zeros sit → **zero-location-blind /
  RH-silent**.
- **candidate (b)** = the **zero side** `K = VᵀV` (this work): sees-zeros YES, but it IS the Weil zero
  side (circular) AND it reads the zeros directly, agnostic to the product (**not** Euler-borne).

**No finite-rank real or complex form is simultaneously Euler-borne, independent, AND zero-tracking.**
Zero locations live in the **zeros**; Euler data lives in the **primes**. The only object coupling them
is the cross-place coupling `W_∞ ≥ Σ_p W_p` (= the missing object). This is the same pin the whole
self-pairing thread reached (Sylvester locks every `*`-congruence, 26 confs) and the non-congruence
difference `A − P` reached (candidate (a), 27th) — now closed from the zero side too.

## Honest subtleties

- The signature flip requires the test-basis to not vanish at the zero ordinates `γ ≈ 14–50`: the wide
  Gaussian (`width 0.35`, `weight_sigma 0.12`) used by `operator_domination.py` collapses `K` to
  `O(1e-12)` (everything within tol of 0, degenerate `(0,5,0)`). The load-bearing run uses `width 0.05`
  so `φ̂(14) = O(1)`; the off-line min eig `−0.0024` is then a genuine real negative eigenvalue, robust
  across `width ∈ {0.02,0.03,0.05}` and damping `weight_sigma ∈ {0, 0.05, 0.08}`.
- The single off-line plant flips the GLOBAL Gram only when the planted zero is not swamped by the
  ~160 on-line PSD rows; with no damping the rank-2 indefinite block (`min eig −0.0024`) still
  dominates because the on-line contributions are spread across centers. This matches `weil_form.py`'s
  Toeplitz flip (`−0.0` → indefinite).
- Load-bearing EXACT facts: the identity `xᵀKx = Σ_ρ g(γ_ρ)²` to `1.4e-17`; the symmetric-vs-Hermitian
  distinction (`−0.0024` vs `+1.4e-7`); the on→off signature flip `(5,0,0)→(4,0,1)`; the
  DH-constructibility `(4,0,1)`.

Tags: **[THM]** (`xᵀKx = Σ_ρ g(γ_ρ)²` = the Weil zero side; `K ⪰ 0 ⟺` RH; `K` reads zeros not primes),
**[computed]** (the identity, the flip, the DH-constructibility, the symmetric/Hermitian split).
