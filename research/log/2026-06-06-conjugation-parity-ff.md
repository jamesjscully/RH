# Conjugation-parity of the WORKING function-field proof — settling NEXT #1's falsifier-in-advance (2026-06-06)

**Item:** AGENDA NEXT #1 (surface · representability · load-bearing). The frontier wants RH ⟸ a
self-product surface over `Spec ℤ` whose self-intersection is `‖f‖²`. The agenda states a *falsifier
in advance*, distilled from 30 wall confirmations:

> "does the candidate's self-pairing escape BOTH the Sylvester congruence-lock AND the
> conjugation-evenness (the two walls that closed everything so far)? **It must be conjugation-ODD.**"

Before building yet another ℤ-surface candidate, I audited this **requirement itself** in the one place
the `C×C` Hodge-index mechanism is a THEOREM: the function field. The decisive question — in Weil's
*working* proof, is the line-forcing self-intersection form conjugation-EVEN or conjugation-ODD?

`scripts/numerics/witness/conjugation_parity_ff.py` (+ 1 `falsify.py` row).

## What was computed [computed, EXACT — integer Weil polynomials, no bare floats on load-bearing facts]

Four curves with RH holding (real Weil polynomials): `E/𝔽_5` (`a₁=2`), `E/𝔽_7` (`a₁=−3`), `E/𝔽_11`
(`a₁=5`), and a genus-2 curve over `𝔽_2` (`P=T⁴−T³+2T²−2T+4`).

1. **The Rosati involution IS the FF complex conjugation [THM, verified].** `†:α↦q/α` is the
   polarization-adjoint on `End(Jac)` / the transpose of correspondences on `C×C`. On the line
   `|α|=√q`, `q/α = ᾱ` — verified `α†=conj(α)` for all eigenvalues, all 4 curves. So `†` is *exactly*
   the agenda's "conjugation" (`ρ↔ρ̄`): the FF avatar of complex conjugation, RH ⟺ `α†=ᾱ` for all `i`.

2. **The line-forcing form is maximally conjugation-EVEN [THM+computed].** Weil's positivity (Hodge
   index / Castelnuovo–Severi) is `⟨φ,ψ⟩=Tr(φψ†)` positive-definite. Its Frobenius diagonal is
   `⟨F,F⟩ = Tr(FF†) = Σᵢ αᵢαᵢ† = Σᵢ q = 2gq` — because `α·(q/α)=q` **EXACTLY for every eigenvalue**,
   independent of RH. Each term is the `J`-paired product `a·a†`, so the form is **even by
   construction**: odd part identically 0; `F_even` invariant under `J:α↦q/α` verified (`= 2gq`:
   `10,14,22,8`).

3. **The unique conjugation-ODD spectral datum vanishes [THM+computed].** The only `J`-odd functional
   is the orientation `u(α)=log(α²/q)` (`r=α²/q` is the phase-squared; under `J`, `r↦1/r`, so
   `u↦−u`). The total orientation `u=Σ log(αᵢ²/q)` **flips sign under `J`** (verified
   `u(J-set)=−u(set)`) and is **identically 0 on every FE-symmetric Weil spectrum** (`Re u ≈ 10⁻¹⁶`,
   all 4 curves) — this is **the same `E_signed≡0` conjugation cancellation** that closed the entire
   static real-form family (DONE #25) AND the dynamical dBN branch (DONE #30): the `+Im`/`−Im`
   conjugate pair cancels.

## The finding [THM-flavored, REVISES a foundational agenda requirement]

**In the archetype that WORKS, the line is forced by a conjugation-EVEN positive form — NOT a
conjugation-odd one.** The agenda's falsifier-in-advance ("the missing ℤ-surface self-pairing must be
conjugation-ODD") is **refuted as a REQUIREMENT**:

- Weil never reads ONE zero's side (there is no odd functional in his proof). He reads the
  **SIGNATURE/inertia** of an EVEN positive-*semi*definite form: the line is its **degeneration locus**
  (the kernel vector / `Δ⊥·Δ⊥=0` on-circle), a Sylvester-inertia statement, not an odd-functional sign.
- Conjugation-ODDness is a property *only* of "which side is THIS one zero on" — which **no positive
  form has** (even OR over `ℤ`), and which Weil's proof **never needs**. The 30 confirmations correctly
  found that no Euler-borne form is conjugation-odd; the *mistake* was concluding the missing object
  must therefore be odd. The working model shows the opposite: the missing object is EVEN, and the line
  is its inertia degeneracy.
- **The two "walls" are NOT independent.** "Conjugation-odd" was a **mis-naming of the inertia
  degeneracy of an even form**. There is **one wall**: the Sylvester inertia-lock. RH needs an EVEN
  positive form whose **signature/inertia is MOVABLE by the Euler/prime data** (so a planted off-line
  pair degenerates it). That is exactly `operator_domination.py`'s `A⪰P` read correctly: the inertia of
  `W=A−P` must flip with the line, and the obstruction (DONE #27) is that the Euler-borne `P` is
  zero-location-blind while the zero-bearing `P` is the Weil form — the SAME wall, now seen to be the
  *only* wall.

## Falsifier verdict

`conjugation_parity_ff.py` is a **meta/structural audit**, not a positivity candidate. Tabled
Euler-borne=Y (the FF Hodge form needs the Frobenius/Satake lattice DH lacks), sees-zeros=Y (the
signature degenerates on-circle), independent=N (= the Weil positivity) → the FF archetype is itself
**CIRCULAR over ℤ**; its value is the **parity structural fact**. **31st wall confirmation**, and the
first to *correct the agenda's framing* from two walls to one (Sylvester inertia).

## Honest subtleties

- The genus-2 Weil polynomial `T⁴−T³+2T²−2T+4` is a valid `q=2` real Weil polynomial (all roots
  `|α|=√2`, verified); the parity facts are basis/curve-independent (they are exact identities
  `a·a†=q`, `r∘J=1/r`), not numerics of these specific curves.
- The branch-cut in `Σ log(α²/q)` is handled by checking `Re u` (the modulus-orientation, which is the
  conjugation-odd content); the `2πi` ambiguity is in the imaginary part and irrelevant to the parity.
- This does NOT resurrect any closed candidate; it re-specifies the OPEN target (NEXT #1) more
  accurately: an even form with Euler-movable inertia, not an odd form.
