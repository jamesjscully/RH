import RH.Basic.DirichletSeries
import RH.HardyModule.MultiplicationRange

/-!
Finite Dirichlet-polynomial witness spaces.
-/

namespace RH.HardyModule

structure DirichletWitnessSpace where
  level : Nat
  tau : HalfPlaneParameter

def dirichletWitnessSpace (N : Nat) (tau : HalfPlaneParameter) : DirichletWitnessSpace :=
  { level := N, tau := tau }

end RH.HardyModule
