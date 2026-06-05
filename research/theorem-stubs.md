# Theorem Stubs

Status labels:

- `informal`: only in prose.
- `lean-stated`: formal statement exists.
- `toy-proved`: proved in a toy model.
- `partial`: meaningful partial proof exists.
- `blocked`: known obstacle.
- `false`: disproved as stated.
- `obsolete`: replaced by a better theorem.

## Abstract Contradiction Mechanism

Status: `lean-stated`

Lean: `RH/Strategy/ContradictionMechanism.lean`

Informal statement:

Forward convergence, reverse obstruction, and a positive reverse gap are incompatible for a hypothetical off-critical zero.

Current issue:

The Lean statement is deliberately abstract and uses an explicit incompatibility assumption. Next step is to encode the zero predicate and gap inequality more structurally.

## Theorem A: Finite Compression With Explicit Losses

Status: `lean-stated`

Lean: `RH/Strategy/TheoremA_FiniteCompression.lean`

Informal statement:

\[
\operatorname{dist}(u,V_N(\tau))^2
=
\|u\|^2-b_{N,\tau}^*G_{N,\tau}^{-1}b_{N,\tau}
+\operatorname{Err}_{N,\tau}
\]

with explicit Gram entries, target vector, error, and conditioning estimates.

Current issue:

The analytic definitions of \(H^2(\Omega_\tau)\), \(u\), \(\phi_\tau\), and \(V_N(\tau)\) are not yet formalized.

## Theorem B: Finite Reverse Visibility

Status: `lean-stated`

Lean: `RH/Strategy/TheoremB_ReverseVisibility.lean`

Informal statement:

If \(\rho=\beta+iT\) is a zero of \(\zeta\) with \(\beta>\tau>1/2\), then finite witness spaces \(V_N(\tau)\) have same-coordinate reverse lower bounds:

\[
\operatorname{dist}(u,V_N(\tau))
\ge
G(\delta_T,\nu_{N,\tau})-L_{N,\tau,T}.
\]

Current issue:

Raw evaluation kernels are easy conceptually but likely too weak. Need projected reverse packets with height and truncation dependence.

## Theorem C: Coupled Path

Status: `lean-stated`

Lean: `RH/Strategy/TheoremC_CoupledPath.lean`

Informal statement:

Choose \(N_m\to\infty\), \(\tau_m\downarrow1/2\) so forward convergence reaches the critical boundary while reverse visibility survives.

Current issue:

Depends on the resolution function \(R_\tau(N)\), conditioning estimates, and Theorem B.
