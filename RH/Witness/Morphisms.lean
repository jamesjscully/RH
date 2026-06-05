import RH.Witness.QuantitativeInvariants

/-!
Quantitative morphisms between witness systems.

The research spec requires morphisms to preserve more than formal structure:
they must carry forward error, reverse signal, positivity margins, and
conditioning with explicit losses. The first layer records that requirement as
named fields to be refined later.
-/

namespace RH

structure QuantitativeMorphism (W W' : WitnessSystem) where
  mapParam : W.Param → W'.Param
  mapLevel : Level → Level
  preservesForward : Prop
  preservesReverse : Prop
  controlsLoss : Prop
  controlsConditioning : Prop

infix:50 " ⪯q " => QuantitativeMorphism

end RH
