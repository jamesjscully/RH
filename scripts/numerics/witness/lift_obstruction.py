"""The two-variable lift obstruction, concretely: why the Frobenius Ψ_λ don't lift to the square.

The single load-bearing blocker (geometry-of-the-square.md §4): the characteristic-1 Frobenius
correspondences Ψ_λ (= Γ_λ, the graphs of scaling-by-λ) compose fine on the CURVE but do not lift to
a family of finite-self-intersection cycles on the SQUARE S². This module shows *exactly why*, by
computing the intersection of Γ_λ with the diagonal and contrasting it with the function-field case.

The mechanism (computed below):

1. **`(Γ_λ · Δ) = Tr(ϑ_λ) = 1/|1−λ|`.** The Frobenius correspondence Γ_λ is the graph of the scaling
   ϑ_λ: f(x) ↦ f(λx). Its intersection with the diagonal is the Atiyah–Bott/Lefschetz trace: a single
   fixed point x=0 (the archimedean place), contributing `1/|1−dϑ| = 1/|1−λ|`.

2. **It DIVERGES as `λ → 1`** — and `λ=1` is the identity, where `Γ_1 = Δ` itself. So the diagonal
   self-intersection `Δ·Δ = lim_{λ→1} 1/|1−λ| = ∞`. Near `λ=1`, in `u = log λ`, `1/|1−λ| ~ 1/|u|` —
   the raw geometric form of the corner kernel `K_∞(u) ~ −1/(2|u|)` we computed (corner_defect.py).
   The Weil explicit formula's archimedean term `∫ f(λ)/|1−λ| d*λ` is a *principal value precisely
   because of this divergence*; the regularization is the corner singularity / CC20's `δ'`-jump at ρ=1.

3. **Over `𝔽_q` it is always FINITE.** `Tr(Fr^n) = #Fix(Fr^n) = q^n + 1 − (α^n+ᾱ^n)`, `|α|=√q`. The
   Frobenius eigenvalues never equal 1, so the discrete semigroup `{Fr^n}` never hits the identity, and
   every diagonal intersection (and `Δ·Δ = 2−2g`) is finite.

**The obstruction, stated.** Composing/lifting Γ_λ to the square requires intersecting with the
diagonal; that intersection is `1/|1−λ|`, finite for `λ≠1` but **infinite at `λ=1` (the diagonal
itself)**. Over `𝔽_q` the Frobenius is a *discrete semigroup that avoids the identity* (Δ·Δ finite);
over `ℤ` the scaling is the *continuous group `ℝ₊^*` that contains `λ=1`* (Δ·Δ = ∞). The very
continuity that makes the geometry "real-number-like" (`Aut(ℝ_max) = ℝ₊^*`, a real Frobenius) is what
puts the identity inside the group and makes the diagonal self-intersection diverge. **Gift and wound
are the same feature.** Cohomological face: `H¹(S²)` would carry `Tr(Γ_λ|H¹) = Σ_ρ λ^ρ`, but the
diagonal class cannot decompose with a finite `H¹⊗H¹` piece (`Δ·Δ = ∞`) — equivalently, no `H¹` on
the square. A resolution must regularize the `λ=1` divergence with the *RH sign*, equivariantly (CC20
get the sign at one place but break equivariance) — the open problem.

Run:  python3 -m scripts.numerics.witness.lift_obstruction
"""
from __future__ import annotations

import numpy as np


def diagonal_trace(lam):
    """(Γ_λ · Δ) = Tr(ϑ_λ) = 1/|1−λ| — Atiyah–Bott trace, single archimedean fixed point x=0."""
    return 1.0 / abs(1.0 - lam)


def fq_fixed_points(q, alpha, n):
    """#Fix(Fr^n) = q^n + 1 − (α^n + ᾱ^n) for a genus-1 curve over F_q (|α|=√q) — always finite."""
    return q ** n + 1 - 2 * (alpha ** n).real


def summary():
    print("The two-variable lift obstruction: why Ψ_λ don't lift to the square\n")

    print("[1] (Γ_λ·Δ) = Tr(ϑ_λ) = 1/|1−λ| diverges as λ→1 (the identity = the diagonal Δ):")
    for lam in [0.5, 0.9, 0.99, 0.999, 1.001, 1.01, 1.1]:
        print(f"      λ={lam:6.3f}   (Γ_λ·Δ)={diagonal_trace(lam):10.2f}")
    print("      => Γ_1 = Δ; Δ·Δ = lim 1/|1−λ| = ∞.  The diagonal self-intersection diverges.")

    print("\n[2] near λ=1 (u=log λ): 1/|1−λ| ~ 1/|u| -- the raw form of the corner K_∞(u)~−1/(2|u|):")
    for u in [0.1, 0.05, 0.02, 0.01]:
        lam = np.exp(u)
        print(f"      u={u:.2f}   1/|1−λ|={diagonal_trace(lam):8.3f}   1/|u|={1/abs(u):8.3f}   ratio={diagonal_trace(lam)*abs(u):.4f}")

    print("\n[3] over F_q the SAME trace is FINITE (Frobenius eigenvalues |α|=√q never equal 1):")
    al = np.sqrt(4) * np.exp(1j * 1.0)
    for n in [1, 2, 3, 5, 10]:
        print(f"      n={n:2d}   #Fix(Fr^n)={fq_fixed_points(4, al, n):12.1f}   (finite; Δ·Δ=2−2g=0)")

    print("\n[obstruction] char-1 Frobenius = the CONTINUOUS group ℝ₊^* (contains λ=1 ⟹ Δ·Δ=∞);")
    print("  char-p Frobenius = a DISCRETE semigroup avoiding the identity (Δ·Δ finite). The continuity")
    print("  that makes the geometry real-number-like is exactly what makes the diagonal self-")
    print("  intersection diverge. To lift Ψ_λ to the square one must regularize the λ=1 divergence")
    print("  with the RH sign, equivariantly -- CC20 get the sign at one place but break equivariance.")


if __name__ == "__main__":
    summary()
