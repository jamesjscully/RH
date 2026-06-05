import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic

/-!
Toy Theorem A (rank-1 finite compression), the genuine `N = 1` case of the
finite Gram identity, proved in a real inner-product space.

The squared distance from `u` to the line `span{v}` is the minimum over `a` of
`‖u - a • v‖²`, and it equals the one-term Gram expression
`‖u‖² - ⟪u,v⟫² / ⟪v,v⟫`.  This is the honest, non-vacuous toy that the earlier
vacuous `True`-valued scaffold stood in for.
-/

namespace RH.Experiments.ToyGram

open scoped RealInnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Expansion of `‖u - a • v‖²` as a real quadratic in `a`. -/
theorem norm_sub_smul_sq (u v : E) (a : ℝ) :
    ‖u - a • v‖ ^ 2 = ⟪u, u⟫ - 2 * a * ⟪u, v⟫ + a ^ 2 * ⟪v, v⟫ := by
  rw [← real_inner_self_eq_norm_sq]
  simp only [inner_sub_left, inner_sub_right, real_inner_smul_left, real_inner_smul_right]
  rw [real_inner_comm v u]
  ring

/-- **Toy Theorem A.**  The minimum of `‖u - a • v‖²` over the line `span{v}` is the
    one-term Gram expression `‖u‖² - ⟪u,v⟫²/⟪v,v⟫`.  `IsLeast` packages both that the
    value is attained (at `a = ⟪u,v⟫/⟪v,v⟫`) and that it lower-bounds every `a`. -/
theorem toy_finite_compression (u v : E) (hv : v ≠ 0) :
    IsLeast (Set.range fun a : ℝ => ‖u - a • v‖ ^ 2)
      (⟪u, u⟫ - ⟪u, v⟫ ^ 2 / ⟪v, v⟫) := by
  have hvpos : 0 < ‖v‖ := norm_pos_iff.mpr hv
  have hI : 0 < ⟪v, v⟫ := by rw [real_inner_self_eq_norm_sq]; exact pow_pos hvpos 2
  have hIne : ⟪v, v⟫ ≠ 0 := ne_of_gt hI
  constructor
  · -- attained at the projection coefficient a = ⟪u,v⟫/⟪v,v⟫
    refine ⟨⟪u, v⟫ / ⟪v, v⟫, ?_⟩
    dsimp only
    rw [norm_sub_smul_sq]
    field_simp
    ring
  · -- lower bound for every a:  reduces to 0 ≤ (a⟪v,v⟫ - ⟪u,v⟫)²
    rintro y ⟨a, rfl⟩
    dsimp only
    rw [norm_sub_smul_sq]
    have hdiv : ⟪u, v⟫ ^ 2 / ⟪v, v⟫ * ⟪v, v⟫ = ⟪u, v⟫ ^ 2 :=
      div_mul_cancel₀ _ hIne
    nlinarith [sq_nonneg (a * ⟪v, v⟫ - ⟪u, v⟫), hI, hdiv]

end RH.Experiments.ToyGram
