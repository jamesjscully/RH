import RH.Witness.FiniteWitness

/-!
Quantitative invariants tracked by the proof strategy.

For the first formal layer these are represented abstractly as predicates over
paths. Later modules should replace them with analytic definitions in concrete
models.
-/

namespace RH

structure QuantitativeProfile (W : WitnessSystem) where
  forwardError : Level → W.Param → Type
  reverseModulus : Level → W.Param → Type
  lossBudget : Level → W.Param → Type
  conditioning : Level → W.Param → Type
  resolution : Level → W.Param → Type

structure ForwardConvergence (W : WitnessSystem) (path : WitnessPath W) : Prop where
  holds : True

structure ReverseObstruction (W : WitnessSystem) (path : WitnessPath W) (Zero : Type) : Prop where
  holds : True

structure PositiveReverseGap (W : WitnessSystem) (path : WitnessPath W) (Zero : Type) : Prop where
  holds : True

end RH
