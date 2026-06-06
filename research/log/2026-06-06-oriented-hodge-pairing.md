# Oriented signed Hodge weight — the corrected "complex conjugation acts non-trivially" target

**Item:** AGENDA NEXT #1 (CONSTRUCT, load-bearing) — build the oriented `(1,0)`/holomorphic form the
prior pass named, after the conjugation-INVARIANT Hermitian `A + iω` (complex_structure_pairing) and
the entire REAL-form family (zero_in_form_pairing) closed.

**Module:** `scripts/numerics/witness/oriented_hodge_pairing.py` (+ 1 `falsify.py` row).

## What the agenda asked for, verbatim

Build the holomorphic `(1,0)` projector `P^{1,0}=½(Id−iJ)`, `P^{0,1}=½(Id+iJ)`, and pair the plant
against the ORIENTED signed Hodge weight (NOT the conjugation-symmetric sum)

> `Q(x) = ⟨P^{1,0}x, P^{1,0}x⟩_A − ⟨P^{0,1}x, P^{0,1}x⟩_A`,

test whether THAT flips on/off-line, with the off-line plant injecting a genuine `γ` (height/phase),
not just the conjugation-symmetric real Weil pair `(β,1−β)`.

## Finding [THM + computed]

### (O2) The decisive algebra — the oriented form COLLAPSES to `−iω`

As a Hermitian matrix, a short exact computation (verified `~1e-15`) gives

```
Q = (P^{1,0})^* A P^{1,0} − (P^{0,1})^* A P^{0,1} = −(i/2)(A J − J^T A).
```

The `A`-orthogonal complex structure (`J²=−Id`, `J^T A J = A`) satisfies the EXACT identity
`J^T A = −A J` (proved in complex_structure_pairing). Substituting:

```
Q = −(i/2)(A J − (−A J)) = −i (A J) = −i·ω,     ω = A J  the Kähler 2-form.
```

So **the ORIENTED signed Hodge weight IS `−iω`** — a FIXED Hermitian matrix (ω real antisymmetric ⟹
`−iω` Hermitian), namely the imaginary/Kähler part of the very `H = A + iω` that
complex_structure_pairing already closed. Computed `‖Q − (−iω)‖ ≈ 5e-14` on the EVEN-`(p,q)` bases
(support dim 8, 10), where `J` is exactly `A`-orthogonal (`‖J^T A J − A‖ ≈ 5e-14`,
`‖J^T A + A J‖ ≈ 5e-14`).

The conjugation-SYMMETRIC sum (what the prior pass used) is exactly `A`:
`‖(P^{1,0})^* A P^{1,0} + (P^{0,1})^* A P^{0,1} − A‖ ≈ 5e-14`. So "orientation" (signed weight vs
symmetric sum) only changes WHICH fixed Hermitian background you pair against (`−iω` vs `A`) — not the
lock.

`inertia(Q) = inertia(−iω) = (4,4,0)` (dim 8), `(5,5,0)` (dim 10).

### (O3a) REAL FE-pair plant — no flip (as predicted, `*`-congruence)

The prime-shift plant `T` is REAL, so `T^T Q T = T^* Q T` is a `*`-congruence; for `det T ≠ 0`
Sylvester's law of inertia for Hermitian forms gives `inertia(T^T Q T) = inertia(Q)`. Computed:
signed-Hodge inertia does NOT flip on-line (`β=½`) vs off-line (`β=0.6`, FE-forced Weil pair):
`(4,4,0)=(4,4,0)` dim 8, `(5,5,0)=(5,5,0)` dim 10. (det `T_on` `~4e-3` dim 8, `~3e-7` dim 10, `≠0`.)

### (O3b) STEELMAN — genuinely COMPLEX ORIENTED plant — STILL no flip

The agenda explicitly asks for a plant that injects a genuine `γ`/phase, breaking `ρ↔ρ̄`. I built the
genuinely complex oriented plant `T_c` carrying the `(1,0)` phase `e^{iγu}` (NOT the
conjugation-symmetric `cos(γu)`), so the conjugate orientation is `γ → −γ`, a DIFFERENT plant. It is
genuinely J-coupled: `‖[T_c, J]‖ ≈ 16–22`, `det T_c ≠ 0`.

Result: the signed-Hodge inertia of `T_c^* Q T_c` STILL does NOT flip on-line vs off-line
(`(4,4,0)=(4,4,0)` dim 8, `(5,5,0)=(5,5,0)` dim 10), AND does NOT distinguish `+γ` from `−γ` off-line
(`(4,4,0)=(4,4,0)`). The oriented form does not even see the orientation of the plant's phase.

### Why — the strongest naming of the wall yet [THM]

`Q` is Hermitian; `T_c` is invertible. **Sylvester's law of inertia holds for ANY invertible
`*`-congruence, REAL OR COMPLEX** — verified directly on a generic complex Hermitian `Q`:
`T_c^* Q T_c` preserves `inertia(Q)` for all invertible complex `T_c`. So the wall was NEVER the
reality of the PLANT (the agenda's hope that a complex/oriented plant escapes the lock is wrong) — it
is that ANY self-pairing `(plant)^*(fixed Hermitian form)(plant)` is inertia-locked, period.

`inertia(Q) = inertia(−iω)` is built from the FE-derived `J` and the DH-shared `A`
(`max|A_ζ − A_DH| = 0`) ⟹ DH-shared.

## Falsifier verdict

**Euler-borne YES** (`op_diff ≈ 1.80`), **sees-zeros NO** (no flip, real or complex/oriented plant),
**independent NO** → **RH-SILENT.** **26th Euler-product confirmation.**

## Decisive lesson

Orienting the FORM (signed Hodge weight vs conjugation-symmetric sum) does NOT help, because the lock
is the **congruence structure of self-pairing**, not the reality of the data. The agenda's diagnosis
"the disease is reality / conjugation is a symmetry of all real data" was correct that no REAL form's
inertia encodes `sign(Im ρ)` — but the proposed cure (a complex/oriented form + a complex/oriented
plant) does not work either, for a STRONGER reason: Sylvester holds for any invertible congruence over
ℂ. The signed Hodge weight collapses to `−iω`, a fixed Hermitian background whose inertia no invertible
congruence — real, complex, oriented — can move.

This UNIFIES the entire self-pairing family under ONE wall, now stated in its strongest form:

> any `(plant)^*(fixed DH-shared form)(plant)` — symmetric `T^T A T`, real-θ-twist `T^T AΘ T`,
> Hermitian `T^T(A+iω)T`, oriented signed-Hodge `T^* (−iω) T`, real OR complex plant — is
> inertia-locked by Sylvester. A flip requires the FORM the plant pairs against to ITSELF depend on
> the zero LOCATIONS = the Weil coupling `W_∞ ≥ Σ_p W_p`.

## Honest subtleties

- The odd-`(p,q)` basis (support dim 6, from chiral `[l2,l3,l5]`) carries a `0.33` `A`-orthogonality
  residual `‖J^T A J − A‖` (the same coarse-basis subtlety recorded in the
  complex_structure_pairing log: odd `(p,q)` cannot be exactly paired by the S-orthogonal complex
  structure). The load-bearing EXACT cases are the even-`(p,q)` bases dim 8 (`[l2,l3,l5,l7]`) and dim
  10 (`[l2,l3,l5,l7,l11]`), where every identity holds to `~5e-14`.
- Load-bearing EXACT facts: `Q = −(i/2)(AJ − J^T A)`; `J^T A = −AJ`; the collapse `Q = −iω`
  (`~5e-14`); `Q_sum = A` (`~5e-14`); the no-flip of both the real FE-pair plant and the genuinely
  complex/oriented plant; and the generic-matrix verification that complex invertible `*`-congruences
  preserve Hermitian inertia.

## What this surfaces

The oriented/holomorphic escape (the whole right edge of the pass-5 "reality" diagnosis) is now closed
TOO. The lock is the congruence structure of self-pairing itself. This re-promotes, decisively, the
remaining route: the FORM must depend on the zero LOCATIONS, which is exactly the Weil domination
`W_∞ ≥ Σ_p W_p` as an operator inequality `A ⪰ P` on the two EXPLICIT Gram matrices (current NEXT #2) —
NOT another self-pairing of a fixed form. Pair the indefinite archimedean `A` against the Euler-borne
prime `P` directly and test whether `A − P` PSD-ness sees the off-line plant where every congruence
did not.
