import RH.HardyModule.DirichletPolynomialWitnesses

/-!
Reproducing-kernel targets for reverse visibility.
-/

namespace RH.HardyModule

structure ReproducingKernelPacket where
  level : Nat
  tau : HalfPlaneParameter
  pointName : String

end RH.HardyModule
