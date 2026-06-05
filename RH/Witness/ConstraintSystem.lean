import RH.Basic.Notation

/-!
Abstract witness-constraint systems.

This is the formal skeleton of the research program. It is intentionally
minimal: the first goal is to make the strategy's logical dependencies precise
before specializing to Hardy spaces and zeta.
-/

namespace RH

structure WitnessSystem where
  Param : Type
  crit : Param
  Space : Param → Type
  Constraint : (θ : Param) → Type
  Witness : Level → (θ : Param) → Type

namespace WitnessSystem

variable (W : WitnessSystem)

abbrev CriticalSpace : Type := W.Space W.crit
abbrev CriticalConstraint : Type := W.Constraint W.crit

end WitnessSystem

end RH
