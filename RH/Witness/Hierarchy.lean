import RH.Witness.Morphisms

/-!
Graded hierarchy of witness systems.
-/

namespace RH

class ExactCritical (W : WitnessSystem) where
  exactCritical : Prop

class OffCriticalFrontier (W : WitnessSystem) where
  offCriticalFrontier : Prop

class FiniteCompression (W : WitnessSystem) where
  finiteCompression : Prop

class DualExplicit (W : WitnessSystem) where
  dualExplicit : Prop

class ReverseDetecting (W : WitnessSystem) where
  reverseDetecting : Prop

class ScaleStable (W : WitnessSystem) where
  scaleStable : Prop

class PositivityBackend (W : WitnessSystem) where
  positivityBackend : Prop

structure ProofSpineSystem (W : WitnessSystem) where
  exact : ExactCritical W
  frontier : OffCriticalFrontier W
  compression : FiniteCompression W
  dual : DualExplicit W
  reverse : ReverseDetecting W
  stable : ScaleStable W

end RH
