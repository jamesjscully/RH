import RH.HardyModule.EvaluationFunctionals

/-!
Finite Gram-matrix package for Theorem A.
-/

namespace RH.HardyModule

structure GramMatrixData where
  level : Nat
  tau : HalfPlaneParameter
  entryFormulaName : String
  targetVectorName : String
  errorTermName : String

def placeholderGramMatrixData (N : Nat) (tau : HalfPlaneParameter) : GramMatrixData :=
  { level := N
    tau := tau
    entryFormulaName := "to be derived"
    targetVectorName := "to be derived"
    errorTermName := "to be bounded" }

end RH.HardyModule
