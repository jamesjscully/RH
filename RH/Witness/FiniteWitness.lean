import RH.Witness.ConstraintSystem

/-!
Finite witness levels and paths through the system.
-/

namespace RH

structure WitnessPath (W : WitnessSystem) where
  level : Nat → Level
  param : Nat → W.Param

structure FiniteWitnessData (W : WitnessSystem) where
  level : Level
  param : W.Param
  witness : W.Witness level param

end RH
