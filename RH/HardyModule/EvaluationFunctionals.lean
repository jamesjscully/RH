import RH.HardyModule.ReproducingKernels

/-!
Evaluation and jet functionals at hypothetical zeta zeros.
-/

namespace RH.HardyModule

structure EvaluationFunctional where
  pointName : String

structure JetFunctional where
  pointName : String
  order : Nat

end RH.HardyModule
