import RH.Witness.QuantitativeInvariants
import RH.Strategy.ContradictionMechanism

/-!
Toy models exercising the (real) contradiction mechanism on concrete rational
distance sequences.  These are non-vacuous: `zeroDistances` genuinely converges
(forward holds, no floor), `flooredDistances` genuinely has a floor (reverse
holds), and the mechanism then *proves* the floored sequence cannot converge.
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

/-- A sequence that converges to `0` (in fact is `0`): forward holds, no floor. -/
def zeroDistances : WitnessDistances finiteToyWitnessSystem finiteToyPath where
  dist := fun _ => 0
  nonneg := fun _ => by decide

theorem zero_forward : ForwardConvergence zeroDistances :=
  fun _ε hε => ⟨0, fun _ _ => hε⟩

/-- A sequence sitting at a positive floor: reverse holds (here `c = 1`). -/
def flooredDistances : WitnessDistances finiteToyWitnessSystem finiteToyPath where
  dist := fun _ => 1
  nonneg := fun _ => by decide

theorem floored_reverse : ReverseObstruction flooredDistances :=
  ⟨1, by decide, fun _ => by show (1 : Rat) ≤ (1 : Rat); decide⟩

/-- The mechanism fires: a sequence with a positive floor cannot converge to `0`. -/
theorem floored_cannot_converge : ¬ ForwardConvergence flooredDistances :=
  fun forward =>
    RH.Strategy.contradiction_from_forward_and_reverse
      flooredDistances forward floored_reverse

end RH.Experiments.ToyModels
