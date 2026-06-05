import RH.Witness.QuantitativeInvariants
import RH.Strategy.ContradictionMechanism

/-!
Toy models for testing witness-system definitions.
-/

namespace RH.Experiments.ToyModels

open RH

def finiteToyWitnessSystem : WitnessSystem where
  Param := Unit
  crit := ()
  Space := fun _ => Unit
  Constraint := fun _ => Unit
  Witness := fun _ _ => Unit

def finiteToyPath : WitnessPath finiteToyWitnessSystem where
  level := fun n => n
  param := fun _ => ()

theorem toyContradictionUnderIncompatibility
    (incompatible :
      ForwardConvergence finiteToyWitnessSystem finiteToyPath →
      ReverseObstruction finiteToyWitnessSystem finiteToyPath Unit →
      PositiveReverseGap finiteToyWitnessSystem finiteToyPath Unit →
      False) :
    False :=
  RH.Strategy.contradiction_from_forward_and_reverse
    finiteToyWitnessSystem
    finiteToyPath
    Unit
    { holds := trivial }
    { holds := trivial }
    { holds := trivial }
    incompatible

end RH.Experiments.ToyModels
