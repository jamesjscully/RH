# θ-twisted self-pairing: FE-invariance relocates the Sylvester lock, no phase carried (2026-06-06)

**Item (AGENDA NEXT #1, CONSTRUCT · load-bearing).** `hecke_correspondence.py` established that the
ζ-intrinsic non-product Hecke correspondence `T` (the explicit-formula prime side as an operator) is
genuinely indecomposable (`‖[T,A]‖ ≫ 0`) but its **symmetric** graph self-pairing `F = TᵀAT` is a
Sylvester congruence of the DH-shared archimedean metric `A`, hence `sig(F)=sig(A)` for any plant →
RH-silent. The obstruction was renamed: *symmetric congruences preserve inertia.* The sharpened
sub-target it surfaced: a **phase-carrying / θ-twisted pairing `Tᵀ A θ T`** (θ = the FE involution)
whose signature is NOT congruence-locked to `A` — recovering the off-diagonal/phase info the
symmetrization throws away. This pass builds and falsifies exactly that object.

`scripts/numerics/witness/theta_twisted_pairing.py` (+ 1 `falsify.py` registry row).

## What was built

The FE involution `θ: s ↦ 1−s` (i.e. `t ↦ −t`, i.e. `u ↦ −u` in the log-scale coordinate) on the
archimedean Mellin model. **The trap, avoided:** the *symmetric* Gaussian basis used by
`hecke_correspondence.py` (`g_c(u) = e^{−(u−c)²/2w²} + e^{−(u+c)²/2w²}`) is already θ-symmetric, so θ
acts as the identity and `Tᵀ A θ T` collapses to the RH-silent symmetric congruence. To give θ a
genuine chance, this module uses a **CHIRAL (one-sided) basis** `g_c(u) = e^{−(u−c)²/2w²}` with centers
placed in ±pairs, so θ is a true reflection permutation `Θ` (`g_c ↦ g_{−c}`), verified non-trivial:
`‖Θ − Id‖ = 4.0`, `‖Θ² − Id‖ = 0` (involution) [computed].

The candidate self-pairing is `F_θ := Tᵀ A Θ T`; its symmetric part carries the Hodge/Weil signature.

## Finding [THM + computed] — the twist relocates the Sylvester lock; it does NOT break it

**(D2 — apparent progress, then explained away.)** Inserting θ DOES move the signature off `sig(A)`:
on the chiral dim-7 basis `sig(A)=(4,3,0)` but `sig(sym(TᵀAΘT))=(3,4,0)`. So the twist is not
congruence-locked to `A` — Sylvester-on-`A` is escaped. **But the decisive structural computation
shows why this is hollow:**

**The archimedean Gram `A` is FE-INVARIANT: `Θ A Θ = A` EXACTLY** (`max diff = 0`) [THM/computed]. The
reason is theorem-level: the archimedean `Γ_ℝ` density `Re ψ(¼ + ir/2)` is **even in `r`** — which is
precisely the FE reflection `t ↦ −t` — so the Gram it induces is invariant under the FE. This forces
two exact consequences:

1. **`A` and `Θ` COMMUTE:** `AΘ = ΘA`, equivalently `antisym(AΘ) = (AΘ − ΘA)/2 = 0` (exact). Hence
   `B := AΘ` is itself a **symmetric** matrix.
2. **The twist carries ZERO phase:** the antisymmetric part of `F_θ` is
   `Tᵀ antisym(AΘ) T = 0` (exact; numerically `‖antisym F_θ‖ ≈ 1e−14`). The very thing the twist was
   supposed to supply — the off-diagonal/phase information — is identically absent.

Therefore `F_θ = Tᵀ B T` is a **symmetric congruence of the symmetric matrix `B = AΘ`**, and by
**Sylvester's law of inertia** `sig(F_θ) = sig(B) = sig(AΘ)` for any invertible plant. The θ-twist did
not escape the congruence trap — **it merely RELOCATED it from `A` to `AΘ`.** Verified directly:
`sig(sym(TᵀAΘT)) = (3,4,0)` for **all** `β ∈ {0.5, 0.55, 0.6, 0.7, 0.8, 0.9}` (det `T ≠ 0` throughout)
— plant-independent, exactly as `sig(A)` was for the untwisted form.

**(D3 — the falsifier, decisive.)** The twisted signature does NOT flip on-line (`β=½`) vs off-line
(`β=0.6`, planted with its FE-forced Weil partner `1−β`, the `signature_forcing.py` standard):
`sig = (5,4,0)` on BOTH, robust across all three chiral bases (dim 7, 9, 11). The scalar twisted
self-int moves (`−20.96` on vs `−19.01` off) but that is the same monotone-in-`β` tail noise, not
line content.

**Verdict (falsify.py three axes): Euler-borne YES (`T_ζ ≠ T_DH`, op_diff `≈ 1.80`), sees-zeros NO
(twisted signature congruence-locked to `AΘ`, plant-independent), independent NO → RH-SILENT.**
**23rd Euler-product confirmation.**

## Decisive lesson — a STRONGER, precisely-named obstruction than Sylvester-on-A

The previous obstruction was "symmetric congruences preserve inertia (Sylvester)" — which seemed to
leave a door open: a `θ`-twisted (non-symmetric) pairing. This pass **closes that door and names a
stronger fact:**

> **The archimedean metric `A` is FE-invariant (`Θ A Θ = A`), which forces `A` and `Θ` to commute.
> Consequently ANY real `θ`-twisted self-pairing `Tᵀ A Θ T` is (i) automatically SYMMETRIC (carries no
> phase) and (ii) a symmetric congruence of the fixed symmetric metric `AΘ` — so its inertia is
> congruence-locked to `sig(AΘ)`, plant-independent, RH-silent. The real `θ`-twist RELOCATES the
> Sylvester lock from `A` to `AΘ`; it does not break it.**

This is why a *real* phase cannot appear: phase is an *antisymmetric/Hermitian* datum, and the
FE-invariance of `A` annihilates the antisymmetric part of `AΘ`. The `(1, ρ−1)` Hodge/phase signature
cannot be carried by any real `θ`-twist of the DH-shared archimedean form. To carry phase one needs
either (a) a **complex/Hermitian** twist (`θ → iθ`-like, a `J` with `J² = −Id`, so `AJ` is
genuinely *antisymmetric* and not congruence-locked the same way), or (b) a metric `A` that is **NOT
FE-invariant** — but `A`'s FE-invariance is exactly its DH-shared archimedean nature (the `Γ_ℝ` factor),
so route (b) re-collides with "the archimedean place is structurally DH-shared / not free to vary
ζ-intrinsically" (the green-current dichotomy, `green_current_perturbation.py`). The live route is (a):
a **complex structure / Hermitian (anti-symmetric real) intersection form**, where `J²=−Id` makes the
twisted pairing genuinely non-congruence-locked.

This re-converges with the HEADLINE modulus⊗phase reading: a *real symmetric* self-pairing is a
modulus (norm-square), Sylvester-locked; the phase `(1, ρ−1)` lives in an *antisymmetric/Hermitian*
form, which a real θ-twist of an FE-invariant metric cannot produce.

## Honest subtleties

- Coarse chiral Gaussian bases (dim 7/9/11); the **load-bearing EXACT facts** are: `Θ A Θ = A`
  (max diff 0), `antisym(AΘ) = 0` (so `AΘ = ΘA`), `Tᵀ antisym(AΘ) T = 0` (zero phase), the
  plant-independence `sig(sym(TᵀAΘT)) = (3,4,0)` for all swept `β` (det `T ≠ 0`), and the no-flip
  `(5,4,0)` on/off-line across 3 bases.
- On the chiral basis the *untwisted* `sig(TᵀAT)` occasionally differs from `sig(A)` by one zero
  eigenvalue (`det T ≈ 1e−8`–`1e−11`, near-degenerate on the larger bases) — a numerical-rank artifact
  of the coarse basis, not a real escape; the dim-7 basis (`det T ≈ 4e−5`, well-conditioned) shows the
  clean Sylvester equality `sig(TᵀAT) = sig(A) = (4,3,0)`. The twisted-form conclusion (relocated
  congruence, no flip) is robust regardless.
- `T` is the explicit-formula prime-shift operator (ζ-intrinsic surrogate for a Hecke `T_n`), as in
  `hecke_correspondence.py`; `θ` is the genuine FE involution.

## What it surfaces

The real-θ-twist route is **dead** for the same deep reason the green-current route was: the FE-invariance
of the DH-shared archimedean metric. The next axiom is sharply named: a **complex structure `J`
(`J² = −Id`) on the surface** — a Hermitian / genuinely antisymmetric intersection form `Tᵀ A J T` whose
inertia is NOT preserved under congruence (because `AJ` is antisymmetric, not symmetric). This is the
Kähler/Hodge `(1, ρ−1)` structure proper: the phase lives in the complex/symplectic part, never in a
real symmetric congruence. New NEXT items below.
