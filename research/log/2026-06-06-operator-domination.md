# Operator inequality A ⪰ P — the Weil domination directly (NEXT #1, the corrected target)

**Date:** 2026-06-06
**Module:** `scripts/numerics/witness/operator_domination.py` (+ 1 `falsify.py` row)
**Agenda item:** NEXT #1 — return to the Weil explicit-formula domination `W_∞ ≥ Σ_p W_p` DIRECTLY
as the operator inequality `A ⪰ P`, the form being `W = A − P` (NOT a congruence `Tᵀ(·)T`, so
Sylvester does not apply). Test whether it SEES the off-line plant where every congruence did not.

---

## What was built [computed]

The two explicit Gram matrices the agenda named, on an even-Gaussian basis (reusing the
`arakelov_signature.py` primitives, one-place 5-dim model):

- **`A`** — the archimedean `Γ_ℝ` Gram, `A[i,j] = ∫ ĥᵢ(r) ĥⱼ(r) (1/2π)Re ψ(¼+ir/2) dr` (DH-shared).
- **`P`** — the prime Gram, `P[i,j] = Σ_n Λ(n) hᵢ(log n) hⱼ(log n)/n` (Euler-borne).
- **`W = A − P`** — the Weil quadratic form. `RH ⟺ W ⪰ 0 ⟺` the operator inequality `A ⪰ P`.

This is the first object in the self-pairing thread that is **NOT** a congruence `(plant)ᵀ(fixed
form)(plant)`: it is the **difference** of two fixed forms. Sylvester's law of inertia is structurally
inapplicable to `A − P`. So if `P` carries the zeros, this could be the first object that flips.

## Computed facts (one-place 5-dim model)

| object | signature `(+,0,−)` | note |
|---|---|---|
| `A` (archimedean) | `(3,0,2)` | **INDEFINITE** (`Re ψ(¼+ir/2)` not sign-definite — `A^{1/2}` ∄) |
| `P` (prime, `Λ`) | `(5,0,0)` | **PSD** (`Λ ≥ 0`, prime-power supported) |
| `W = A − P` | `(1,0,4)` | `min eig(W) = −8.17` ⟹ `A ⪰ P` is **FALSE** at one place |

(`(1,0,4)` is the coarse one-place model, NOT claimed to be the true `(1,ρ−1)` — same caveat as
`arakelov_signature.py`.)

## The decisive finding — the agenda's hope is REFUTED [THM-flavored + computed]

The agenda's hope (verbatim): *"the first object where the form depends on the zero locations (through
`P` carrying the planted resonance), so Sylvester does NOT apply."* This is **false**, exhaustively, by
a clean dichotomy with no third option (the same shape as `green_current_perturbation.py` /
`square_representability.py`):

### (R1) The ARITHMETIC `P` is zero-location-INDEPENDENT.

`P` is built from `Λ(n)` = the `n`-th coefficient of `−ζ'/ζ` = a property of zeta's **Euler product**,
NOT of where its zeros sit. **There is no "plant an off-line zero" operation that changes `Λ(n)` while
keeping ζ being ζ**: ζ has the zeros it has, and `Λ(n)` is fixed. Verified:
- `max|P_from(−ζ'/ζ) − P_from(Λ)| = 0.0` exactly — `P` has no `β`/zero-location knob.

So the arithmetic `W = A − P` is a **FIXED, zero-INDEPENDENT matrix**; its inertia CANNOT flip
on/off-line. **Sylvester was never the obstruction here — there is no plant to apply it to.** The
agenda's hope conflated "the form `A − P` is not a congruence" (true) with "the form depends on the
zero locations" (false for the arithmetic `P`).

- **Euler-borne YES**: `max|A_ζ − A_DH| = 0.0` exactly (DH-shared), `max|P_ζ − P_DH| = 0.84` (the
  Euler content is in `P`).
- **sees-zeros NO**: `P` (hence `W`) is zero-independent.
- At one place `A ⪰ P` does not even discriminate ζ from DH: `sig(W_ζ)=(1,0,4)`, `sig(W_DH)=(2,0,3)`,
  both indefinite, both `A ⪰ P` false (same coarseness as `semilocal_2.py` — the prime perturbation is
  too weak at one place to flip the sign).

### (R2) The only `P` that DOES carry the zero locations is the spectral zero side itself.

The explicit formula lets us trade the prime side for the **zero side** `W(h,h) = Σ_ρ ĥ(γ_ρ)`. Built
as a Toeplitz Gram (reusing `weil_form.py`):
- TRUE zeros: `min eig = −0.0` ⟹ PSD ⟹ `A ⪰ P` holds (all `γ_ρ` real).
- PLANTED off-line zero (`β = 0.8`, `γ = T − i(β−½)` COMPLEX): `min eig = −1.49` ⟹ PSD **lost**.

So the spectral `P_spec` **SEES the off-line plant** — but it **IS the zero side** = PSD iff all `γ_ρ`
real = the Weil positivity (**CIRCULAR**), and its "`P`" is whatever the zeros dictate (the prime side
of a *different* L-function with that off-line zero, exactly `green_current_perturbation.py` CASE 2),
NOT zeta's `Λ(n)`.

## The pin (the load-bearing equality)

**NO single `P` is BOTH Euler-borne-independent AND zero-bearing.** The operator inequality `A ⪰ P` is:
- **RH-SILENT** for the arithmetic (Euler-borne, independent) `P` — `Λ(n)` is zero-location-blind;
- **CIRCULAR** for the spectral (zero-bearing) `P_spec` — it is the zero side = the Weil positivity.

The operator inequality does NOT escape the wall — it **re-expresses** it: making zeta's OWN `Λ(n)`
(the arithmetic, Euler-borne `P`) force the zero side IS the cross-place coupling `W_∞ ≥ Σ_p W_p` =
the missing object. The zero locations live in the **zeros**; the Euler data lives in the **primes**;
coupling them is the unmoved wall.

## Falsifier verdict

**Euler-borne YES** (arithmetic `P` carries the Euler product, `A` DH-shared), **sees-zeros NO**
(arithmetic `P` is zero-independent), **independent** splits (arithmetic independent but RH-silent;
spectral sees-zeros but circular) → **RH-SILENT** (arithmetic reading) / **CIRCULAR** (spectral
reading). **27th Euler-product confirmation.**

## Decisive lesson

The corrected NEXT #1 target — "the form must depend on the zero LOCATIONS, not be a congruence" — is
**realizable only as the zero side itself** (circular). The Euler-borne prime data `Λ(n)` is
**structurally zero-location-blind**: it is a fact about the Euler product, and the explicit formula
that ties it to the zeros is precisely the identity whose positivity is RH. So the two halves of the
self-pairing program now meet:
- **congruence self-pairings** (`TᵀAT`, `TᵀAΘT`, `Tᵀ(A+iω)T`, oriented): inertia-locked by Sylvester
  to a DH-shared fixed background (RH-silent, 26 confirmations);
- **non-congruence difference** `A − P` (this work): for the Euler-borne `P` it is zero-independent
  (RH-silent); for the zero-bearing `P` it is the Weil positivity (circular).

Neither side of the program reaches a `P` that is simultaneously Euler-borne, independent, AND tracks
the zero locations — that object is the cross-place coupling itself.

## Honest subtleties

- The `(1,0,4)` signature is the same coarse one-place 5-dim Gaussian model as `arakelov_signature.py`
  (NOT the true `(1,ρ−1)`). The **load-bearing exact facts** are: `max|A_ζ − A_DH| = 0` (DH-shared),
  `max|P_from(−ζ'/ζ) − P_from(Λ)| = 0` (arithmetic `P` zero-independent), `max|P_ζ − P_DH| = 0.84`
  (Euler-borne), and the spectral PSD flip `−0.0 → −1.49` on planting an off-line zero.
- The dichotomy R1/R2 is the **structural content**, not the numerics: `Λ(n)` having no zero-location
  knob is a fact about the Euler product, robust to the basis/model.
