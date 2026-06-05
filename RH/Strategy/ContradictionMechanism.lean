import RH.Witness.Hierarchy

/-!
Abstract contradiction mechanism.

This is the first formal theorem target for the whole project. It says that
forward convergence, reverse obstruction, and a positive reverse gap are
logically incompatible for a hypothetical off-critical zero. The current
statement is deliberately abstract; later versions should replace the three
assumptions with concrete analytic hypotheses.
-/

namespace RH.Strategy

open RH

theorem contradiction_from_forward_and_reverse
    (W : WitnessSystem)
    (path : WitnessPath W)
    (Zero : Type)
    (forward : ForwardConvergence W path)
    (reverse : ReverseObstruction W path Zero)
    (gap : PositiveReverseGap W path Zero)
    (incompatible :
      ForwardConvergence W path →
      ReverseObstruction W path Zero →
      PositiveReverseGap W path Zero →
      False) :
    False :=
  incompatible forward reverse gap

end RH.Strategy
