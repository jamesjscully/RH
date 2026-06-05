import RH.Basic.Hardy

/-!
Half-plane objects for the Hardy-module proof spine.
-/

namespace RH.HardyModule

structure HalfPlaneParameter where
  name : String

def criticalHalfPlane : HalfPlaneParameter := { name := "Re(s) > 1/2" }

end RH.HardyModule
