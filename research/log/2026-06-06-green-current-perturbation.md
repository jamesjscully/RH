# The ζ-intrinsic Green-current/metric perturbation (NEXT #1, sharpened): an EXHAUSTIVE dichotomy with no third option — the metric freedom is signature-locked OR it changes the L-function (2026-06-06)

**Item (AGENDA NEXT #1, load-bearing).** The Arakelov pass (DONE #0/top) pinned the §6.3 block and
sharpened NEXT #1 to a concrete construction question:

> Is there a **ζ-intrinsic Green-current / metric perturbation** (off the DH-shared `Γ_ℝ`
> background, built from ζ's own primes `Λ(n)`) that makes the **finite-place** `(D_F²·H)` the
> DOMINANT term — i.e. a **positive Green form whose positivity DEPENDS on `Λ(n)`, not just on
> `Re ψ`**? This is exactly where §6.3's "can fail" must become "holds ⟺ RH".

Module: `scripts/numerics/witness/green_current_perturbation.py` (+ 1 `falsify.py` row).

---

## The setup it builds on

The Arakelov Weil form on `bar(Spec ℤ)` is `W = A − P` with
- `A` = archimedean Kähler/Green form (the `Γ_ℝ` kernel `Re ψ(¼+ir/2)`), **identical for ζ and DH**
  (`max|A_ζ−A_DH| = 0`, the prior pass's decisive computed fact);
- `P` = finite-place prime Gram (`Σ_n c(n) hᵢ(log n)hⱼ(log n)/n`), the only Euler-bearing piece, and
  it enters `W` with a **MINUS** sign (dominated, not dominating).

The question is whether a metric perturbation of the archimedean place can flip this — make `P`
dominate, ζ-intrinsically.

## What I built and the decisive finding [THM + computed]

A "Green-current / metric perturbation of the archimedean place" is, concretely, a change of the
**archimedean local factor `L_∞(s)`** = an additive correction `g(r)` to the archimedean density
`Re ψ(¼+ir/2)`. I made the structural dichotomy **executable** and found it is **exhaustive — there is
no third option**:

**CASE 1 — a metric/gauge perturbation that KEEPS ζ's completed Weil form `W` (a congruence
`W ↦ Sᵀ W S`).** By **Sylvester's law of inertia** the signature is invariant. Verified with a genuine
ζ-intrinsic frame change `S = I + ε·L[Λ]` (`L` built from `Λ(n)` localized at the basis log-scales,
`det S ≠ 0`): signature `(1,0,4) → (1,0,4)`, **unchanged**. **A ζ-intrinsic frame change CANNOT flip
the indefinite Weil form to definite → RH-SILENT.**

**CASE 2 — a nonzero additive archimedean density.** The most natural ζ-intrinsic correction is to
place ζ's OWN prime data at infinity:
`g_Λ(r) = Σ_n Λ(n) cos(r log n)/√n`. Computed `‖g_Λ‖₂ = 40.8 ≠ 0`, and it genuinely changes the
archimedean Gram (`max|A'−A| = 66.6`). **But a nonzero additive correction to the archimedean density
changes `L_∞`, hence the completed `L = L_∞·L_fin`, hence the functional equation and the ZERO SET.**
The perturbed object's zeros are **not ζ's zeros** — it reads off a *different* function. (Mechanically
`g_Λ` is the prime side reflected onto the archimedean place: it DOUBLE-COUNTS the primes, not a new
positive dominator.)

**STEELMAN — the "third option": perturb `A`, compensate in `P`, keep `W` fixed.** A critic's escape:
change both places so the completed form is unchanged. **Vacuous for positivity.** "`W` positive" is a
property of `W` **alone**, and the zeros are read from `W`; so holding `W` fixed (= preserving ζ's
zeros) holds its **signature** fixed **regardless of how `A,P` are split** — verified
`max|W_comp − W| = 4e-16`, signature `(1,0,4)` unchanged. Relabeling the dominator does not change the
difference. **Collapses to Case 1 (RH-silent).**

**THE PIN (an executable EQUALITY).** Sweeping the correction scale `{0, ¼, ½, 1}`: the boolean
"finite piece can newly dominate" (`A' ≠ A`) is **identical, at every scale**, to "archimedean density
changed" (`g ≠ 0`) = "`L_∞` changed" = "different L-function / not ζ's zeros". There is **no scale**
where `P` newly dominates while ζ's zeros are preserved.

## Falsifier verdict

- **Euler-borne?** The perturbation is built from `Λ(n)`, so a *nonzero* one is Euler-borne by
  construction — but Case 1 (the form-preserving freedom) is inertia-locked and RH-silent; only Case 2
  is Euler-borne AND changes the form, and it does so by changing `L_∞`.
- **sees-zeros?** Only Case 2 moves anything, and it moves the **zero set itself** (changes `L_∞`) —
  it does not see ζ's zeros, it replaces them. Case 1 preserves the zeros but cannot change positivity.
- **independent?** NO — by the executable equality, "metric perturbation lets the finite piece
  dominate" ⟺ "`L_∞` changed" ⟺ "a different L-function". Making the finite Euler piece dominate ζ's
  OWN Weil form without changing ζ **is** the Weil positivity `W = A − P ⪰ 0` = RH.

> **VERDICT: CIRCULAR / RH-SILENT split — the sharpened target dissolves into an exhaustive
> dichotomy.** There is **no ζ-intrinsic Green-current degree of freedom** that dominates ζ's own Weil
> form off the DH-shared background: any honest metric freedom (Case 1 / steelman) is **signature-locked
> by Sylvester's inertia → RH-SILENT**; any perturbation that actually changes the form (Case 2)
> **changes `L_∞` → a different L-function**. Making the finite Euler piece dominate **IS** the Weil
> positivity (CIRCULAR). **20th Euler-product confirmation.**

## Honest subtleties (do not fool ourselves)

- The `(1,0,4)` signature is the same **coarse 5-dim finite-rank model** as the prior pass — NOT
  claimed to be the exact `(1,ρ−1)`. The load-bearing facts here are structural and basis-robust:
  (i) Sylvester inertia (a theorem, holds for any `W`, any invertible `S`); (ii) the **exact equality**
  `max|W_comp − W| = 4e-16` (a congruence-with-compensation is identity-on-`W`); (iii) the
  scale-sweep equality "`A'≠A` ⟺ `g≠0`" (definitional). The numerics illustrate theorems; they are not
  load-bearing floats.
- "Changing `L_∞` changes the zero set" is the standard fact that the completed `Λ(s)=L_∞(s)L_fin(s)`
  determines the zeros; the archimedean factor is not free to vary while fixing `L_fin` and the zeros.
  The only archimedean freedom that fixes the zeros is the *trivial* one (rescaling/normalization),
  which is the Case-1 gauge.

## What this sharpens / closes

This **closes the construction route NEXT #1 named as a Green-current/metric perturbation**: it is a
genuine *dichotomy*, not a gap to push on. The metric-perturbation handle on §6.3 is dead — not because
the analysis is hard, but because the degree of freedom **does not exist** in the form the target asked
for (the archimedean place cannot be made ζ-intrinsic while fixing ζ's zeros). The Euler content is
structurally confined to the finite places, and the archimedean dominator is structurally DH-shared;
**no local-metric move couples them** — the coupling, if it exists, must be **global / cross-place**,
not a perturbation of one place.

This **re-confirms** the standing wall (`W_∞ ≥ Σ_p W_p` is the Weil positivity, no local lever buys it)
and **removes a candidate**: the next pass should NOT look for a metric/Green-form perturbation but for
a genuinely **two-place / surface** object (the `S²/ℤ` self-product, A5) where the cross-place coupling
is intrinsic to the geometry, not a perturbation. The dichotomy here is itself the measurement: the
missing structure is **not a metric on `bar(Spec ℤ)`** (a curve) — it is the **second dimension**.

Sources:
- A. Moriwaki, *Hodge index theorem for arithmetic cycles of codimension one*, arXiv:alg-geom/9403011.
- J.-B. Bost, H. Gillet, C. Soulé, *Heights of projective varieties and positive Green forms*,
  JAMS 7 (1994) 903–1027 (§6.3).
- Sylvester's law of inertia (signature invariant under congruence) — standard.
