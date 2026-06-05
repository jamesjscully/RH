# Research Agenda

## Current Priority

Build the formal and computational base for the Hardy-module proof spine.

## Phase 0: Infrastructure

- [x] Create Lean 4 Lake project.
- [x] Add abstract witness-system skeleton.
- [x] Add research log and theorem-tracking files.
- [x] Confirm `lake build RH` passes.
- [x] Add local WhippleScript and Loft automation dependencies.
- [x] Add initial WhippleScript research workflow.
- [x] Initialize Loft issue repository and seed initial work items.
- [x] Confirm `scripts/automation/check.sh` passes.
- [ ] Decide whether and when to add Mathlib.

## Phase 1: Abstract Strategy

- [x] State abstract witness systems.
- [x] State quantitative profiles.
- [x] State abstract contradiction mechanism.
- [ ] Strengthen contradiction mechanism so it tracks a named hypothetical zero predicate.
- [ ] Add toy finite-dimensional model with nontrivial forward/reverse predicates.
- [ ] Add theorem-status links from Lean stubs to research notes.

## Phase 2: Finite Hardy-Module Package

- [ ] Define the half-plane parameter \(\tau>1/2\) formally.
- [ ] Define Dirichlet polynomial witness spaces \(V_N(\tau)\).
- [ ] Derive finite Gram matrix entries for \(\|\phi_\tau D_N\|^2\).
- [ ] Derive target vector for projecting \(u\) onto \(V_N(\tau)\).
- [ ] Track condition numbers as \(\tau\downarrow1/2\).

## Phase 3: Reverse Visibility

- [ ] Write raw reproducing-kernel lower bound at a hypothetical zero \(\rho\).
- [ ] Include jet functionals for multiple zeros.
- [ ] Project evaluation kernels against finite witness spaces.
- [ ] Estimate reverse signal as a function of \(N,\tau,T\).
- [ ] Define first candidate resolution function \(R_\tau(N)\).

## Phase 4: Coupled Path

- [ ] Formulate candidate scalings \(N_m,\tau_m\).
- [ ] Compare forward error, reverse modulus, and conditioning loss.
- [ ] Identify whether the base path survives or fails.

## Phase 5: Secondary Tracks

- [ ] Kernel/co-Poisson/Sonine normal-form notes.
- [ ] Bohr-lift/prime-graded diagnostics.
- [ ] Explicit-formula positivity transport requirements.
