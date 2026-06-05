# Definitions Tracker

This file tracks the Lean status of each concept; the rows reflect the (unchanged)
placeholder Lean files. For the corrected *roles* of these concepts see
[`tracker.md`](tracker.md): the "reverse modulus" / "reproducing kernel packet" rows
belong to the **Barrier Oracle** (a cheap `N`-uniform evaluation bound, not a
bottleneck), and the forward/arithmetic side is where the real work lives.

| Concept | Informal Status | Lean Location | Lean Status | Notes |
|---|---|---|---|---|
| Witness system | Specified in research program | `RH/Witness/ConstraintSystem.lean` | abstract skeleton | Needs analytic refinement |
| Witness path | Specified | `RH/Witness/FiniteWitness.lean` | skeleton | Coupled \(N,\theta\) path |
| Distance sequence | Specified | `RH/Witness/QuantitativeInvariants.lean` | **real** (`WitnessDistances`, ℚ-valued, nonneg) | abstract `dist(u,V_N(τ))` |
| Forward convergence | Specified | `RH/Witness/DistanceSequence.lean` | **real** (`ForwardConvergence=TendstoZero`) | the RH-equivalent side |
| Reverse obstruction | Specified | `RH/Witness/DistanceSequence.lean` | **real** (`ReverseObstruction=UniformPositiveFloor`) | barrier oracle; `hardy.barrier_bound` |
| Contradiction mechanism | Specified | `RH/Strategy/ContradictionMechanism.lean` | **proved** (`forward_reverse_incompatible`) | real, not a tautology |
| Loss budget | Specified | `RH/Witness/QuantitativeInvariants.lean` | placeholder type family | Needs additive ledger |
| Quantitative morphism | Specified | `RH/Witness/Morphisms.lean` | structural placeholder | Needs inequalities |
| E/F/C/D/R/S/P hierarchy | Specified | `RH/Witness/Hierarchy.lean` | class skeletons | Need examples |
| Critical Hardy avatar | Specified | `RH/HardyModule/HardySpace.lean` | name placeholder | Needs actual \(H^2(\mathbb D)\) |
| Half-plane module avatar | Specified | `RH/HardyModule/HardySpace.lean` | name placeholder | Needs \(H^2(\Omega_\tau)\) |
| Dirichlet witness spaces | Specified | `RH/HardyModule/DirichletPolynomialWitnesses.lean` | placeholder | Needs coefficients and functions |
| Reproducing kernel packet | Specified | `RH/HardyModule/ReproducingKernels.lean` | placeholder | Needs kernel formula |
| Evaluation functional | Specified | `RH/HardyModule/EvaluationFunctionals.lean` | placeholder | Needs bounded linear functional |
| Gram matrix data | Specified | `RH/HardyModule/GramMatrices.lean` | placeholder | Needs finite matrix formalization |
