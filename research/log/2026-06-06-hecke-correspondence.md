# Hecke (non-product) correspondence: indecomposability achieved, self-intersection RH-silent (2026-06-06)

**Item (AGENDA NEXT #1, CONSTRUCT · load-bearing).** After `square_representability.py` CLOSED the
naive product surface `S × S` (its Künneth cross slot `C = A⊗P + P⊗A` factorizes through the base
single-place forms, decomposable diagonal, RH-silent), the sharpened target is a **NON-PRODUCT surface
whose `H¹⊗H¹` does NOT split as `base⊗base`** — an indecomposable diagonal correspondence = the missing
`End(S²/ℤ)`. Two concrete prongs: (i) is there a ζ-intrinsic non-product 2-dim object? (ii) what
algebraic structure on the base makes `Δ` indecomposable (a Hecke/correspondence module, NOT a tensor
square)? This pass attacks both via the **Hecke correspondence**.

`scripts/numerics/witness/hecke_correspondence.py` (+ 1 `falsify.py` registry row).

## What was built

The classical source of indecomposable correspondences is the **Hecke correspondence** `T_n`: on a
modular/Shimura surface, the graph `Γ_{T_n} = {(x, T_n x)} ⊂ S × S` is NOT of product type, and the
**Eichler–Shimura relation** writes the Frobenius itself as a Hecke correspondence
`Frob_p = T_p − p·Frob_p^∨` [THM]. So the very object whose eigenvalues are the zeros is a non-product
Hecke correspondence — the prototype of a Néron–Severi class not of product type.

**ζ-intrinsic realization (prong i).** ζ is GL(1) and has no Hecke eigenform of its own, but the
explicit formula gives ζ an intrinsic prime-shift operator on the spectral model `H = L²(ℝ, du)`
(`u = log` scale; the SAME Gaussian-basis archimedean model as `square_representability.py` /
`arakelov_signature.py`):

    (T f)(u) = Σ_{n≥2} (Λ(n)/√n) [ f(u−log n) + f(u+log n) ] / 2

= the **arithmetic side of the Weil explicit formula AS AN OPERATOR**. `T` genuinely SHIFTS by `log n`
(`T ≠ Id`, `T` is not a rank-1 product `|a⟩⟨b|`). Its graph `Γ_T` is the ζ-intrinsic non-product
correspondence. DH has its own signed, non-prime-power-supported `c_DH(n)`, giving a different operator
`T_DH` — axis 1 (Euler-borne) is built in.

## Finding [THM + computed]

**(1) The indecomposability IS achieved — genuine progress on prongs (i) & (ii).** The Hecke
correspondence is computably NON-PRODUCT. Measuring `‖[T, A]‖` (the commutator with the archimedean
metric `A` = the place-grading; a correspondence factors as `base⊗base` iff it commutes with the
place-grading):

| basis | `‖[Δ=Id, A]‖` | `‖[T, A]‖` | non-product? |
|---|---|---|---|
| 5-center `[0,l2,l3,l5,l7]` | **0.0** (exact) | **46.97** | YES |
| 6-center `+l11` | 0.0 | 45.24 | YES |
| 7-center `+l13` | 0.0 | 30.00 | YES |

The diagonal `Δ = Id` trivially commutes with `A` (factorizes, `‖[Id,A]‖ = 0` exactly); the prime-shift
operator `T` does NOT (`‖[T,A]‖ ~ 30–47 ≫ 0`, robust across 3 bases). **So off-diagonality (the graph of
a Hecke operator) DOES supply the indecomposability the agenda asked for** — `H¹⊗H¹` via `Γ_T` does not
factor as `base⊗base`. This answers prong (i) affirmatively: a ζ-intrinsic non-product 2-dim object
exists (the explicit-formula prime-shift operator's graph), and prong (ii): the structure that makes it
indecomposable is the **off-diagonal Hecke/shift action** (`[T, A] ≠ 0`), not a tensor square.

**(2) BUT the graph SELF-INTERSECTION washes it out — RH-SILENT. [THM]** The decisive computed fact:
the graph self-pairing form `F = TᵀAT` (the `H¹⊗H¹` self-intersection in the Hilbert/CC20 `W_∞` reading)
is a **CONGRUENCE** of the archimedean metric `A`. Since `T` is invertible (`det T ≈ 1.6e−4 ≠ 0`), by
**Sylvester's law of inertia** `sig(F) = sig(A)` for ANY plant. And `sig(A)` is the **DH-shared**
archimedean signature (`max|A_ζ − A_DH| = 0` exactly, inherited from `arakelov_signature.py`). So:

- the graph-pairing signature does NOT flip on-line vs off-line, even with the FE-forced Weil pair
  (`β` and its partner `1−β`, the genuine off-line plant that `signature_forcing.py` showed flips a
  real intersection form): `sig_online = sig_offline = (3,2,0)` (and `(4,2,0)`, `(3,3,1)` on the 6- and
  7-center bases) — **robust across all 3 bases**;
- verified directly: `sig(T_offᵀ A T_off) = sig(A)` regardless of the plant (Sylvester congruence).

The bare *scalar* self-intersection `Tr(TᵀATA)` DOES move (`31519` on-line vs `29966` off-line), but
that is **monotone-in-`β` noise** — the `e^{(β−½)u}` tail grows with `β` regardless of arithmetic — NOT
line-specific. The genuine Weil/RH content is the SIGNATURE, which is congruence-locked to `A`.

**Verdict: Euler-borne YES (`T_ζ ≠ T_DH`, `op_diff = 3.60`), non-product YES (`‖[T,A]‖ ≫ 0`),
sees-zeros via scalar self-int YES but the SIGNATURE (genuine Weil content) is congruence-locked to the
DH-shared `A` → RH-SILENT.** **22nd Euler-product confirmation.**

## Decisive lesson

Indecomposability of the OPERATOR is **necessary but not sufficient**: the prime-shift operator `T` is a
genuine non-product correspondence (`[T,A] ≠ 0`), but **symmetrizing it into its graph self-pairing
`TᵀAT` re-collapses to a congruence of the DH-shared archimedean form `A`** — the MODULUS, blind to the
line. This is the **SAME Sylvester-congruence trap** that closed the green-current route
(`green_current_perturbation.py` CASE 1: a metric/gauge perturbation keeping ζ's Weil form is a
congruence `W ↦ SᵀWS`, signature-invariant). Two distinct construction routes (a metric perturbation;
a non-product correspondence's self-intersection) hit the **identical** obstruction: any object built as
a congruence of the archimedean form is signature-locked, hence RH-silent.

So the missing `End(S²/ℤ)` is NOT supplied by the explicit-formula prime-shift operator as a
correspondence. The needed object must **couple the non-productness to the PHASE/reality** — it must be
something OTHER than a congruence `TᵀAT` of the DH-shared archimedean metric. This re-converges with the
HEADLINE/pass-3 reading (RH = a ζ-intrinsic coupling of MODULUS and PHASE): the self-INTERSECTION
`Γ_T·Γ_T = Tr(T^*T)` is manifestly a NORM-SQUARE = the MODULUS of `T`, and a norm-square cannot carry the
phase/reality `(1, ρ−1)` Hodge signature. The off-diagonal Hecke structure lives in `T` itself (the
non-commutativity), but the self-pairing throws away the phase by symmetrizing.

## Honest subtleties

- The coarse 5–7 center Gaussian basis; the load-bearing EXACT facts are `‖[Id,A]‖ = 0`, `‖[T,A]‖ ≫ 0`
  (robust 3 bases), `det T ≠ 0`, and the Sylvester congruence `sig(TᵀAT) = sig(A)` (verified directly,
  basis-robust, plant-independent).
- `T` is the explicit-formula prime side as an operator (an analog of the Hecke `T_n`), not a literal
  Hecke operator on a modular surface (ζ being GL(1) has none); the Eichler–Shimura framing motivates
  the construction but the executable object is ζ-intrinsic by the prime-shift action.
- The non-productness `[T,A] ≠ 0` is genuine and basis-robust; the negative is specifically that the
  **self-intersection** (not the operator) is signature-locked.

## What it surfaces

The sharpened sub-target: a ζ-intrinsic non-product correspondence whose self-pairing is NOT the
symmetric congruence `TᵀAT` (the modulus) but carries the off-diagonal/phase information — e.g. an
ANTI-symmetric or `θ`-twisted pairing `Tᵀ A θ T` (θ = the FE involution) whose signature is NOT
congruence-locked to `A`. The Sylvester obstruction is precisely that symmetric congruences preserve
inertia; a phase-carrying pairing must break the congruence form.
