import RH.HardyModule.GramMatrices
import RH.Witness.QuantitativeInvariants

/-!
Theorem A target: finite compression with explicit losses.

Status: TARGET ONLY — not formalized as a theorem (no vacuous `True` stub).  The
real statement needs the analytic layer (`H²(Ω_τ)`, the Gram matrix `G_{N,τ}`,
the projection identity) and therefore Mathlib; it is tracked in
`research/tracker.md` (Workstream A / N4) and validated numerically in
`scripts/numerics/witness/hardy.py`:

    dist(u, V_N(τ))² = ‖u‖² − b_{N,τ}* G_{N,τ}⁻¹ b_{N,τ} + Err_{N,τ}.

This module records only the *statement metadata*; it deliberately proves nothing.
-/

namespace RH.Strategy.TheoremA

open RH

structure FiniteCompressionTarget where
  statementName : String :=
    "dist(u, V_N(tau))^2 equals finite Gram expression plus controlled error"
  /-- Where the certified tail error `Err_{N,τ}` enters (the truncation remainder
      of the spectral integral; needs an explicit `|ζ(τ+it)|` bound). -/
  tailErrorName : String := "Err_{N,tau} (certified truncation remainder)"

end RH.Strategy.TheoremA
