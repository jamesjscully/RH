# The off-diagonal `Tr(F)` is NOT the wall — the wall is the OTHER diagonal `⟨F,F⟩=deg(F)` (2026-06-06)

**Item (AGENDA NEXT #1).** Attack the single missing entry of the Rosati Gram (DONE #1): *what gives
the off-diagonal `Tr(F)` an unconditional ℤ-meaning AND the Cauchy–Schwarz bound?* Two handles:
(a) is `Tr(F)` the explicit-formula prime sum, and does the diagonal `⟨F,F⟩` exist unconditionally
(a "Frobenius norm" over ℤ)? (b) the BGS positive-Green-form obstruction = where Cauchy–Schwarz fails.

**Module.** `scripts/numerics/witness/off_diagonal.py` (+ `falsify.py` registry row). Three parts,
all certified (python-flint `acb` zeros, `arb` von Mangoldt, exact identities).

## Findings [THM + computed]

**Part A, handle (a) — the entry identification, with a decisive asymmetry.**
- **(a.1) `Tr(F)` over ℤ = the von Mangoldt prime sum** — CONFIRMED. `c_ζ(n) = Λ(n)` to err `2.5e-60`;
  `Λ(n)≥0`, prime-power supported; DH's prime-side has negative coeffs (Euler-borne). The off-diagonal
  is the **arithmetic side** of the explicit formula — an honest **RH-independent number** (the analog
  of the integer `a = #C(𝔽_q) − (q+1) = Tr Frob`). **So the off-diagonal IS available over ℤ.**
- **(a.2) the SECOND diagonal `⟨F,F⟩` does NOT exist as an unconditional norm over ℤ** — this is the
  crack. Over `𝔽_q`, `⟨F,F⟩ = Tr(F·F') = deg(F) = 2q`, the self-pairing of the Frobenius
  **correspondence**, an RH-independent integer. Over ℤ there is no correspondence, so `⟨F,F⟩` can only
  be written as a **sum over the zeros** `Σ_ρ|φ̂_F(γ_ρ)|²`, which is a genuine non-negative norm **iff
  the `γ_ρ` are real** — i.e. iff RH. (Computed: planting one off-line zero makes the diagonal entry
  cease to be a Hermitian square and exceed the on-line value.)

**Part B, handle (b) — the Cauchy–Schwarz sees the zeros but IS the Weil-form PSD-ness.** Built the
genuine Weil Toeplitz form (cf. `weil_form.py`, validated) on translate test vectors:
- on-line: Weil Gram min eig `−3.4e-16` (PSD); **all** `2×2` minors `≥0` → every Cauchy–Schwarz holds.
- off-line (β=0.85 planted zero): Weil Gram min eig **`−2.29`** (indefinite); a pair `(i,j)` has
  `2×2` minor det `−0.84` < 0 → **a Cauchy–Schwarz is VIOLATED**.
So `|Tr F|² ≤ ⟨Id,Id⟩⟨F,F⟩` is *exactly* the PSD-ness of the Weil form = all `γ` real = **RH**.
*Honest subtlety recorded:* the **single** `(Id,F)` `2×2` restriction is too coarse to register one
faint off-line zero (a `2×2` sub-form can stay PSD while the full form is indefinite) — the equivalence
is at the level of the **full** Weil Gram, not the lone `2×2`. (My first model made this error and
stayed PSD off-line; corrected to the full Toeplitz form.)

**Part C — the `𝔽_q` control: there `a²≤4q` is a THEOREM about FIXED integers.** Tabulated
`q∈{4,5,7,8,9,11,13,25}`: every integer `a` with `a²≤4q` is realized by a variety, and **no** variety
has `a²>4q` (Hasse–Weil). The Cauchy–Schwarz is **automatic** — it is forced by the *existence of the
algebra* `End(Jac)` carrying the positive Rosati form, not an extra hypothesis. The content over `𝔽_q`
is the **existence of the algebra**, not the inequality.

## Falsifier verdict: CIRCULAR (13th Euler-product confirmation)
Euler-borne **YES** (the off-diagonal = prime sum; DH-refusing). Sees-zeros **YES** (Weil Gram flips
indefinite, CS violated off-line). Independent **NO**.

**The decisive correction to DONE #1.** DONE #1 named "the off-diagonal `Tr(F)`" as the single missing
entry. **That is wrong by one index.** The off-diagonal `Tr(F)` is in fact the entry that **DOES** have
an RH-independent ℤ-meaning (the prime sum). The entry with **no** unconditional ℤ-meaning is the
**second diagonal `⟨F,F⟩ = deg(F)`** — the **Frobenius self-norm**. It is missing for *exactly* the
same reason `End(S²/ℤ)` is missing: there is no surface/correspondence whose degree to take. So:

> **The Cauchy–Schwarz `|Tr F|² ≤ ⟨Id,Id⟩⟨F,F⟩` has two known/independent entries
> (`⟨Id,Id⟩=‖f‖²` edge norm; `Tr F` = prime sum) and ONE RH-conditional entry, the diagonal
> `⟨F,F⟩=deg(F)`. Bounding the CS = bounding `⟨F,F⟩` below by `|Tr F|²/⟨Id,Id⟩` = dominating the prime
> sum by an unconditional Frobenius degree = the cross-place coupling `W_∞ ≥ Σ_p W_p`, once more.**

This **unifies** "the missing off-diagonal" and "the missing algebra of correspondences" (which DONE #1
*suspected* were the same gap) into a single sharp object: **the Frobenius self-norm `deg(F)` over ℤ**.
The wall is unmoved but its location is corrected — and it is now a *degree/self-intersection of a
correspondence*, reconnecting directly to the signature/Hodge-index thread (the self-intersection form
on `H¹_prim`, DONE #2): `deg(F)` is precisely the diagonal self-intersection whose existence the
function-field surface supplies and ℤ does not.

Tags: [THM] (Honda–Tate `a²≤4q`; CS ⟺ PSD; `c_ζ=Λ`), [computed] (the explicit-formula Gram + Weil
Toeplitz tests), [honest-negative] (handle circular; DONE #1 corrected by one index).
