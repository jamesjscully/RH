import RH.Witness.QuantitativeInvariants

/-!
Barrier Oracle (formerly "Theorem B: Finite Reverse Visibility").

Corrected role: this is the *easy, classical, `N`-uniform* direction, not the
central bottleneck.  For an off-critical zero `ρ=β+iT` and `τ∈(1/2,β)`,
`φ_τ(ρ)=0` annihilates every `V_N(τ)`, giving the explicit evaluation bound
`dist(u,V_N(τ)) ≥ |u(ρ)|·√(2(β−τ)) > 0` for all `N` (kernel norm
`‖k_ρ^{(τ)}‖² = 1/(2(β−τ))`, verified numerically).  Abstractly, any such floor
is a `ReverseObstruction`.
-/

namespace RH.Strategy.TheoremB

open RH

structure ReverseVisibilityTarget where
  statementName : String :=
    "off-line zero forces a positive N-uniform floor on dist(u, V_N(tau))"

/-- The barrier oracle: a positive evaluation floor `c ≤ dist(u, V_N(τ))` holding
    at every level `N` is exactly a `ReverseObstruction`.  Trivial by design —
    the oracle is a guardrail, not a proof ingredient. -/
theorem barrier_oracle {W : WitnessSystem} {path : WitnessPath W}
    (D : WitnessDistances W path) (c : Rat) (hc : 0 < c)
    (floor : ∀ n, c ≤ D.dist n) :
    ReverseObstruction D :=
  ⟨c, hc, floor⟩

end RH.Strategy.TheoremB
