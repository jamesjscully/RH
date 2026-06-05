import RH.HardyModule.HardySpace

/-!
Multiplication-range avatar.
-/

namespace RH.HardyModule

structure MultiplicationRangeAvatar where
  phiName : String
  rangeConstraintName : String

def zetaRangeAvatar : MultiplicationRangeAvatar :=
  { phiName := "((s - 1) / s^2) * zeta(s)"
    rangeConstraintName := "u lies in closure/range of M_phi" }

end RH.HardyModule
