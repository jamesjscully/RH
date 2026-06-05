import RH.Witness.FiniteWitness
import RH.Witness.DistanceSequence

/-!
Quantitative invariants tracked by the proof strategy.

The forward/reverse invariants are now genuine predicates over an (abstract,
rational) distance sequence `dist(u, V_N(τ))`, not `True` placeholders.  This is
what makes the contradiction mechanism a real theorem (see
`RH/Strategy/ContradictionMechanism.lean`).
-/

namespace RH

structure QuantitativeProfile (W : WitnessSystem) where
  forwardError : Level → W.Param → Type
  reverseModulus : Level → W.Param → Type
  lossBudget : Level → W.Param → Type
  conditioning : Level → W.Param → Type
  resolution : Level → W.Param → Type

/-- The forward distance sequence `dist(u, V_N(τ))` along a path, modelled
    abstractly as a nonnegative rational sequence indexed by the witness level. -/
structure WitnessDistances (W : WitnessSystem) (path : WitnessPath W) where
  dist : Nat → Rat
  nonneg : ∀ n, 0 ≤ dist n

/-- **Forward convergence** (the hard, RH-equivalent side): the distances tend to
    `0`.  Unconditional convergence along `τ ↓ 1/2` is RH. -/
def ForwardConvergence {W : WitnessSystem} {path : WitnessPath W}
    (D : WitnessDistances W path) : Prop :=
  TendstoZero D.dist

/-- **Reverse obstruction** (the trivial, `N`-uniform barrier-oracle side): a
    hypothetical off-critical zero forces a positive floor on the *same*
    distances, at every level `N`. -/
def ReverseObstruction {W : WitnessSystem} {path : WitnessPath W}
    (D : WitnessDistances W path) : Prop :=
  UniformPositiveFloor D.dist

end RH
