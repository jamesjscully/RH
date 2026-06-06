# Zeros in the FORM, not the congruence — the corrected target CLOSED by reality (2026-06-06)

**Item (AGENDA NEXT #1, the corrected target after the self-pairing family closed).** The whole
self-pairing family `(plant)ᵀ(fixed DH-shared form)(plant)` is inertia-locked by Sylvester's law of
inertia (symmetric AND Hermitian; DONE #0). The corrected construction target: build an object where
the **zeros enter the FORM ITSELF, not as the congruence factor `T`** — a form `B(T)` whose inertia
depends on the plant's OWN spectrum. The agenda named two concrete candidates: the **non-self-adjoint
part `Ω(T)=T−Tᵀ`** and the **self-commutator/Poisson form `C(T)=[T,Tᵀ]`**.

`scripts/numerics/witness/zero_in_form_pairing.py` (+ 1 `falsify.py` row).

## What was built [computed]

Three forms built **FROM `T`'s own entries** (NOT congruences of any fixed form, so Sylvester does not
apply) on the chiral archimedean model (reusing `theta_twisted_pairing` primitives):

- `Ω(T) = T − Tᵀ` — the raw non-self-adjoint (antisymmetric) part.
- `Ω_θ(T) = T − Θ Tᵀ Θ` — the **FE-defect**: `T` minus its FE-adjoint. On-line / RH content is
  `T = Θ Tᵀ Θ` (FE-self-adjointness); off-line-ness is an FE-asymmetry, which `Ω_θ` is built to expose.
- `C(T) = T Tᵀ − Tᵀ T` — the **self-commutator = normality defect** (symmetric, traceless). `T` normal
  ⟺ `C=0`. A real-spectrum (= on-line) operator is normal; an off-line zero makes `T` non-normal.

Decisive falsifier: plant the FE-forced Weil pair `(β,1−β)` and ask whether ANY of these `T`-built
inertiae **flip** on-line (`β=½`) vs off-line (`β=0.6`).

## Finding [THM + computed] — RH-SILENT, closed by REALITY (not by the congruence-lock)

**(1) The two-sided ζ-intrinsic prime-shift `T` is EXACTLY symmetric AND EXACTLY FE-self-adjoint.**
Computed exact facts, all bases (dim 7, 9, 11): `‖T−Tᵀ‖ = 0.0`, `‖T − Θ Tᵀ Θ‖ = 0.0`. The reason is
structural: the two-sided shift kernel `exp(−(cᵢ−cⱼ−u)²/4w²) + exp(−(cᵢ−cⱼ+u)²/4w²)` is **even in
`cᵢ−cⱼ`** (the `±log n` sum), hence symmetric in `i↔j`; and the FE plant uses the same even kernel.
So **every `T`-built form vanishes identically** `Ω=Ω_θ=C=0` — inertia `(0,0,n)` on AND off line. No
inertia to flip. (`Θ A Θ = A` exact and `max|A_ζ−A_DH|=0` reconfirmed.)

**(2) STEELMAN — the genuinely NON-normal causal Frobenius operator STILL does not flip.** To give the
forms a fighting chance I built the **one-directional (causal) prime shift** `(Tf)(u)=Σ Λ(n)/√n
f(u−log n)` — the genuine Frobenius/transfer operator. This IS genuinely non-self-adjoint and
non-normal: `‖T−Tᵀ‖ ≈ 4.6 ≫ 0`, `‖[T,Tᵀ]‖ ≈ 54 ≫ 0`. **Yet its `T`-built inertiae do NOT flip:**

| form | on-line (β=½) | off-line (β=0.6) | flips? |
|---|---|---|---|
| `sig(C)` (normality defect) | `(4,4,1)` | `(4,4,1)` | NO |
| `sig(sym Ω_θ)` (FE-defect) | `(0,0,9)` | `(0,0,9)` | NO |
| `‖Ω‖`, `‖C‖` | 4.6176, 53.96 | 4.6210, 54.05 | monotone-in-β noise only |

The norms move only at the 3rd–4th decimal — the same `β`-monotone scalar noise the agenda already
flagged (not line-specific). Robust across bases.

**Verdict: Euler-borne YES (`op_diff≈1.80`), sees-zeros NO, independent NO → RH-SILENT. 25th
Euler-product confirmation.**

## Decisive lesson — the wall is REALITY, not the congruence-lock [THM-flavored]

The non-congruence escape does NOT help, and the reason names the obstruction more precisely than
Sylvester:

> **The FE-forced Weil pair `(β,1−β)` is REAL, and the zero pair `(ρ, ρ̄)` is CONJUGATION-SYMMETRIC.
> `sign(Im ρ)` is an INTRINSICALLY COMPLEX datum. Complex conjugation `ρ ↔ ρ̄` — which maps `+Im` to
> `−Im` at identical real weight — is a SYMMETRY of ALL real data. Therefore NO REAL form's inertia
> (congruence OR non-congruence, symmetric OR non-normal) can encode `sign(Im ρ)`.**

The off-line-ness enters every real form only as `|ρ|`- / `β`-symmetric **MODULUS** data, never as the
`sign(Im)` **PHASE**. The agenda's question — "is there a ζ-intrinsic form whose inertia = `sign(Im ρ)`
data?" — is answered **no, not over the reals**: the very thing that would have to be detected is
killed by conjugation symmetry before any form is built.

This **unifies and supersedes** the Sylvester congruence-lock. DONE #0 read the wall as "the form is
fixed; a real congruence cannot move its inertia." The sharper reading: even a form that genuinely
*varies with `T`* (non-congruence, non-normal) cannot move with `sign(Im ρ)`, because `sign(Im ρ)` is
not present in any real datum. The congruence-lock was a *symptom*; the disease is **reality**.

## Where this points (the next axiom)

A form whose inertia tracks `sign(Im ρ)` requires complex conjugation to be **BROKEN** — a genuinely
holomorphic object with a chosen orientation: a `(1,0)`-form, or a polarization carrying an orientation
(the Hodge `(1,ρ−1)` decomposition is exactly the place where `H^{p,q}` and `H^{q,p}` are distinguished
by conjugation). The `complex_structure_pairing` `J` supplied a complex structure but kept a Hermitian
(conjugation-INVARIANT) form, so its inertia was still real/congruence-locked. The missing object must
pair against a form on which conjugation acts NON-trivially — i.e. the genuine Hodge `(p,q)`
bigrading, not just `A + iω` with `ω` real-antisymmetric. The Weil coupling `W_∞ ≥ Σ_p W_p` enters
here as the statement that the `(1,0)` and `(0,1)` weights are dominated by the diagonal — reached from
the **oriented/holomorphic** side, not the real-inertia side.

## Honest subtleties
- Coarse chiral Gaussian bases (dim 7–9–11); the load-bearing facts are the **EXACT** vanishing
  `‖T−Tᵀ‖=0`, `‖T−ΘTᵀΘ‖=0` (two-sided `T`) and the **no-flip** of the genuinely non-normal causal
  operator's `sig(C)=(4,4,1)`, `sig(sym Ω_θ)=(0,0,9)`, robust across bases.
- The causal operator is a genuine non-normal ζ-intrinsic object (`‖[T,Tᵀ]‖≈54`), so the no-flip is
  not an artifact of a degenerate (symmetric) `T` — it is the reality obstruction biting a genuinely
  asymmetric form.
- `independent=False` is set unconditionally (no flip appeared, so the independence axis is moot); had
  a flip appeared it would still have been the Weil/explicit-formula content unless a new positivity
  were proved.
