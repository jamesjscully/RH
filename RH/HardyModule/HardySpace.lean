import RH.HardyModule.HalfPlane

/-!
Hardy-space avatars used by the proof spine.
-/

namespace RH.HardyModule

structure DiskHardyAvatar where
  targetName : String := "1"

structure HalfPlaneHardyAvatar where
  multiplierName : String := "((s - 1) / s^2) * zeta(s)"
  targetName : String := "(s - 1) / s^2"

end RH.HardyModule
