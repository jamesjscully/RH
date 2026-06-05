import RH.HardyModule.GramMatrices
import RH.Witness.Hierarchy

/-!
Theorem A target: finite compression with explicit losses.
-/

namespace RH.Strategy.TheoremA

open RH

structure FiniteCompressionTarget where
  statementName : String :=
    "dist(u, V_N(tau))^2 equals finite Gram expression plus controlled error"

def finiteCompressionStub : Prop := True

theorem theoremA_scaffold : finiteCompressionStub := by
  trivial

end RH.Strategy.TheoremA
