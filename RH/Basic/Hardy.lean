/-!
Hardy-space naming layer.

The concrete Hardy-space construction is deliberately deferred. The current
types provide stable names for theorem statements, logs, and future
formalization targets.
-/

namespace RH

structure HardyDiskSpace where
  tag : Unit := ()

structure HardyHalfPlaneSpace where
  tauName : String := ""

end RH
