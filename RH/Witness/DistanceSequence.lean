/-!
The genuine contradiction mechanism, over rational distance sequences.

This replaces the earlier tautological theorem (which assumed an explicit
`incompatible` hypothesis equal to its own conclusion).  Here the contradiction
is real: a sequence of (nonnegative) distances cannot simultaneously

  * tend to `0`            -- forward convergence (the hard, RH-equivalent side), and
  * sit above a positive floor for every level `N`   -- the barrier oracle's output
    (the trivial, `N`-uniform reverse obstruction).

Distances `dist(u, V_N(τ))` are modelled abstractly as `d : Nat → Rat`.  The
forward and reverse hypotheses are genuine predicates, and `False` is derived
from order facts alone -- nothing smuggles in the conclusion.
-/

namespace RH

/-- Forward convergence: the distance sequence tends to `0`.
    (Distances are nonnegative, so no absolute value is needed.) -/
def TendstoZero (d : Nat → Rat) : Prop :=
  ∀ ε : Rat, 0 < ε → ∃ N : Nat, ∀ n : Nat, N ≤ n → d n < ε

/-- The barrier oracle's output: a positive lower bound holding at *every* level
    `N`.  For an off-critical zero `ρ` with `τ < β`, `φ_τ(ρ)=0` annihilates every
    `V_N(τ)`, giving `dist(u,V_N(τ)) ≥ |u(ρ)|√(2(β−τ)) > 0` uniformly in `N`. -/
def UniformPositiveFloor (d : Nat → Rat) : Prop :=
  ∃ c : Rat, 0 < c ∧ ∀ n : Nat, c ≤ d n

/-- **Contradiction mechanism (real version).**  A distance sequence cannot both
    converge to `0` and stay above a positive floor.  This is the abstract core
    of the route: forward convergence and the reverse obstruction are genuinely
    incompatible for a hypothetical off-critical zero. -/
theorem forward_reverse_incompatible
    (d : Nat → Rat)
    (forward : TendstoZero d)
    (reverse : UniformPositiveFloor d) : False := by
  obtain ⟨c, hc, hfloor⟩ := reverse
  obtain ⟨N, hN⟩ := forward c hc
  have hlt : d N < c := hN N (Nat.le_refl N)
  have hge : c ≤ d N := hfloor N
  exact absurd hge (Rat.not_le.mpr hlt)

end RH
