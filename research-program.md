# Research Program Spec: A Quantitative Witness-Constraint Route to RH

## 1. Mission

The goal of this research program is to produce an unconditional proof of the Riemann hypothesis. Nothing less is the target.

The intended proof is not a conditional framework, a numerical verification scheme, a reformulation of RH, or a collection of analogies between known criteria. The program aims to build a theorem-driven route that starts from established RH-equivalent analytic structures, develops finite quantitative witness systems inside them, and proves that any zero of \(\zeta(s)\) off the critical line would force a finite obstruction incompatible with a controlled limiting approximation path.

The central thesis is:

> RH should be attacked through witness systems whose finite truncations carry both forward approximation information and reverse obstruction information in the same coordinates.

An RH-equivalent formulation is strategically useful only if it provides all of the following:

1. An exact critical theorem equivalent to RH.
2. An off-critical forward theorem that yields genuine zero-free regions or positivity consequences.
3. A finite-dimensional hierarchy with computable error, conditioning, and tail control.
4. A reverse theorem showing that a hypothetical off-critical zero creates a visible finite defect in the same coordinates.
5. A coupled limiting theorem showing that the forward approximation reaches the critical boundary without losing reverse visibility.

The proof strategy is therefore organized around quantitative witness-constraint systems rather than around isolated RH reformulations.

## 2. Guiding Principle

Many exact criteria for RH are known. Most are not proof strategies by themselves. A criterion becomes a possible proof vehicle only when it has finite, quantitative, stable structure.

The key failure mode is proving the wrong kind of approximation. For example, in Hardy-space versions of the Nyman-Beurling-Baez-Duarte program, a family can be dense in a weak or compact-open topology unconditionally while density in the critical Hilbert topology remains equivalent to RH. This shows that topology, norm, finite compression, and limiting process are not bookkeeping details. They are part of the theorem.

This program therefore treats a proof route as a coupled finite-limit problem:

\[
N \to \infty,\qquad \theta \downarrow \theta_c,
\]

where \(N\) is a finite witness level and \(\theta\) is an off-critical deformation parameter approaching the critical parameter \(\theta_c\). The route succeeds only if forward error tends to zero while reverse obstruction remains detectable at finite resolution.

## 3. Primitive Object

The primitive object is a quantitative witness-constraint system

\[
\mathfrak W =
(\Theta,\theta_c,\{\mathcal H_\theta\},\{C_\theta\},
\{V_N(\theta)\},\{D_\theta\},\{Q_{N,\theta}\},
\{L_{N,\theta}\},T).
\]

The components are:

- \(\Theta\): a parameter space of analytic or Hilbert/Banach environments.
- \(\theta_c\): the critical parameter corresponding to RH.
- \(\mathcal H_\theta\): ambient function spaces, preferably Hilbert spaces in the proof spine.
- \(C_\theta\): the target constraint at parameter \(\theta\). This may be a target vector, a closed range condition, a divisibility condition, or a positivity cone.
- \(V_N(\theta)\): finite witness spaces at level \(N\).
- \(D_\theta\): dual or extremal data, such as reproducing kernels, annihilators, Toeplitz kernels, or biorthogonal systems.
- \(Q_{N,\theta}\): finite quadratic forms, Gram matrices, projection data, or finite-minor systems.
- \(L_{N,\theta}\): explicit loss terms: truncation error, conditioning loss, transport loss, tail error, and deformation loss.
- \(T\): quantitative transports between avatars.

The finite witness spaces should be generated from effectively presented countable algebraic data with finite truncations, not necessarily from a finitely generated semigroup. A typical form is

\[
V_N(\theta)
=
\operatorname{span}
\{\mu_{\theta,j}\rho_\theta(g)\kappa_{\theta,j}
: g\in I_N,\ 1\le j\le r\},
\]

where \(I_N\) is finite and nested, \(r<\infty\), and \(\rho_\theta\) is an action of a semigroup, monoid, module, or related operator family.

The replacement of “target vector plus span” by “target constraint plus finite witness data” is deliberate. Some RH structures are closure problems, some are module/range problems, and some are positivity problems. The primitive object must be broad enough to include all three without forcing them into one artificial template.

## 4. Core Hierarchy

The program uses a graded hierarchy instead of a binary notion of “strong admissibility.” This prevents the research class from becoming vacuous.

An **E-system** has an exact critical theorem equivalent to RH.

An **F-system** adds an off-critical forward theorem: finite or limiting progress at parameter \(\theta>\theta_c\) implies a genuine zero-free region, positivity statement, or other unconditional theorem.

A **C-system** adds finite compression: explicit finite-dimensional projections, Gram matrices, tail bounds, conditioning estimates, and loss ledgers.

A **D-system** adds explicit dual/extremal machinery: reproducing kernels, annihilators, jet functionals, Toeplitz kernels, de Branges-Rovnyak spaces, biorthogonal systems, or equivalent structures.

An **R-system** adds same-coordinate reverse detection: a hypothetical zero off the critical line produces a finite obstruction in the same coordinates used for forward approximation.

An **S-system** adds scale-stable limiting control: one can couple \(N\to\infty\) and \(\theta\downarrow\theta_c\) so forward convergence and reverse visibility survive simultaneously.

A **P-system** adds a certified positivity backend, such as an explicit-formula, Weil-functional, Toeplitz-minor, or de Bruijn-Newman-type positivity system, with quantified transport from the core finite coordinates.

The immediate target is not to classify all possible systems. It is to build one E/F/C/D/R/S system in a concrete base class and use it to prove RH.

## 5. Base Class

The initial proof spine should live in the Hardy-module / weighted-deformation class.

This class is chosen because it already contains several necessary ingredients in connected form:

- Exact Hardy-space closure criteria equivalent to RH.
- Semigroup and cyclicity structure.
- Module/range criteria in Hardy spaces of half-planes.
- Reproducing-kernel and annihilator mechanisms.
- Orthogonal complement and biorthogonal infrastructure.
- Weighted or off-critical deformations that imply actual zero-free half-planes.
- Finite Hilbert projection problems with Gram matrices and constructive approximants.

The base system has two primary avatars.

### 5.1. Critical Hardy Avatar

In Noor-type Hardy-space coordinates, define

\[
h_k(z)
=
\frac{1}{1-z}
\log\left(\frac{1+z+\cdots+z^{k-1}}{k}\right),
\qquad k\ge 2.
\]

The critical finite spaces are

\[
\mathcal N_N^c
=
\operatorname{span}\{h_k:2\le k\le N\}
\subset H^2(\mathbb D),
\]

with target \(1\). The critical exact theorem has the form

\[
\mathrm{RH}
\iff
1\in \overline{\operatorname{span}\{h_k:k\ge 2\}}^{H^2(\mathbb D)}.
\]

This avatar is important because it is an exact RH-equivalent Hilbert-space statement and carries semigroup structure through operators such as

\[
(W_n f)(z)=(1+z+\cdots+z^{n-1})f(z^n).
\]

It also warns that weaker topologies are insufficient.

### 5.2. Half-Plane Module Avatar

In Wei-Wu-type half-plane coordinates, let

\[
\Omega_\tau=\{s\in\mathbb C:\Re(s)>\tau\},
\qquad
\tau>1/2,
\]

and set

\[
\phi_\tau(s)=\frac{s-1}{s^2}\zeta(s),
\qquad
u(s)=\frac{s-1}{s^2}.
\]

The finite module witness spaces are

\[
V_N(\tau)=
\left\{
\phi_\tau(s)D_N(s):
D_N(s)=\sum_{n\le N}a_n n^{-s}
\right\}
\subset H^2(\Omega_\tau).
\]

The module/range principle says, in suitable Hardy half-plane settings, that zero-freeness of \(\phi\) in \(\Omega_\tau\) is equivalent to density or closed-range conditions for multiplication by \(\phi\). Zeros become annihilators naturally: if \(\rho\) is a zero of \(\zeta\) in \(\Omega_\tau\), then every element of \(V_N(\tau)\) vanishes at \(\rho\).

This makes the half-plane module avatar the natural place to build reverse detection.

### 5.3. Transport Requirement

The critical disk model and the half-plane module model must be connected by explicit Mellin/Cayley/Hardy transports with quantified norm comparison.

Qualitative equivalence is not enough. Every transport must carry inequalities for:

- forward approximation error,
- reverse modulus,
- positivity margin,
- conditioning profile,
- truncation resolution,
- loss terms.

The proof spine depends on quantitative transport, not formal analogy.

## 6. Quantitative Invariants

The following invariants should be defined and tracked for every candidate system.

### 6.1. Forward Error

\[
E_{N,\theta}
=
\operatorname{dist}_{\mathcal H_\theta}(C_\theta,V_N(\theta)),
\]

or the corresponding finite constraint defect.

This measures how well finite witnesses satisfy the target constraint.

### 6.2. Forward Frontier

\[
\sigma_N(\theta)
\]

is the zero-free line, positivity region, or analytic frontier obtained from a finite or limiting statement at parameter \(\theta\).

The forward theorem must turn finite approximation into an actual mathematical consequence, not just a smaller norm.

### 6.3. Reverse Modulus

\[
G_{\mathfrak W}(\rho;N,\theta)
\]

is the defect forced at finite level \(N\) by a hypothetical zero \(\rho=\beta+iT\) off the critical line.

The reverse modulus must be in the same finite coordinates as the forward error.

### 6.4. Truncation Resolution

\[
R_\theta(N)
\]

measures which zero locations and height scales are visible at level \(N\) and parameter \(\theta\).

This is essential because a finite hierarchy can miss a zero even when the ambient infinite space detects it.

### 6.5. Conditioning Profile

\[
\kappa_{N,\theta}
\]

measures the stability of the finite Gram matrix, projection problem, basis, transport, or extremal construction.

Conditioning loss is not secondary. A proof can fail because the forward frontier improves slower than the geometry degenerates.

### 6.6. Loss Budget

\[
L_{N,\theta,T}
\]

collects all quantitative losses:

- tail truncation,
- finite-dimensional projection error,
- transport distortion,
- conditioning blow-up,
- deformation loss,
- kernel localization loss,
- height-dependent decay.

Every theorem in the proof spine must state where its losses enter.

### 6.7. Signal-to-Slack Ratio

The useful quantity is not just \(E\) or \(G\), but the gap

\[
G_{\mathfrak W}(\rho;N,\theta)-L_{N,\theta,T}-E_{N,\theta}.
\]

To contradict an off-line zero, this gap must eventually be positive along the coupled path.

## 7. Two Scales of Reverse Visibility

Reverse detection must account for two independent scales.

First, there is the local spectral scale at height \(T\). If

\[
\rho=\beta+iT,\qquad \beta>1/2,
\]

then the local zero-spacing scale suggests the normalization

\[
\delta_T
=
\frac{2\pi(\beta-1/2)}{\log T}.
\]

Second, there is the finite resolution scale of the witness hierarchy:

\[
\nu_{N,\theta}
=
(\beta-\sigma(\theta))R_\theta(N).
\]

A reverse theorem depending only on \(\delta_T\) is not enough. The finite system must also resolve the zero at its current truncation and deformation level.

The correct reverse modulus should therefore have the form

\[
G_{\mathfrak W}
=
G_{\mathfrak W}(\delta_T,\nu_{N,\theta};N,\theta,T).
\]

The coupled path must satisfy a condition of the schematic form

\[
R_{\theta_m}(N_m)(\theta_m-\theta_c)\to\infty,
\]

so that the hierarchy becomes fine enough faster than the deformation approaches the critical boundary.

## 8. Central Theorem Package

The program hinges on three theorem packages in the base Hardy-module / weighted-deformation class.

### Theorem A: Finite Compression With Explicit Losses

For each \(\tau>1/2\) and \(N\), prove an explicit finite-dimensional representation of

\[
\operatorname{dist}_{H^2(\Omega_\tau)}
\left(u,V_N(\tau)\right)^2.
\]

The desired form is a finite Gram-matrix formula:

\[
\operatorname{dist}(u,V_N(\tau))^2
=
\|u\|^2
-b_{N,\tau}^*G_{N,\tau}^{-1}b_{N,\tau}
+\operatorname{Err}_{N,\tau},
\]

with:

- explicit entries of \(G_{N,\tau}\),
- explicit target vector \(b_{N,\tau}\),
- certified tail error \(\operatorname{Err}_{N,\tau}\),
- condition-number estimates for \(G_{N,\tau}\),
- stable algorithms for finite projection.

This theorem turns the witness problem into controlled finite-dimensional linear algebra.

### Theorem B: Finite Reverse Visibility in the Same Coordinates

This is the central bottleneck.

Assume \(\rho=\beta+iT\) is a zero of \(\zeta\) with \(\beta>\tau>1/2\). Then every element of

\[
V_N(\tau)=\{\phi_\tau D_N\}
\]

vanishes at \(\rho\). Evaluation and jet functionals at \(\rho\) therefore annihilate \(V_N(\tau)\). In reproducing-kernel language, they define elements of \(V_N(\tau)^\perp\).

The raw evaluation lower bound is real but too weak. The theorem must construct localized reverse packets

\[
\psi_{N,\tau,\rho}\in V_N(\tau)^\perp
\]

from evaluation kernels, jets, finite Gram sections, and biorthogonal machinery such that

\[
\operatorname{dist}(u,V_N(\tau))
\ge
G(\delta_T,\nu_{N,\tau})-L_{N,\tau,T}.
\]

The lower bound must be:

- explicit,
- positive whenever the zero is visible at finite resolution,
- stable in height,
- stated in the same finite coordinates as Theorem A,
- compatible with the coupled limit \(\tau\downarrow 1/2\), \(N\to\infty\).

If this theorem cannot be proved with the required scale behavior, the current strategy fails for intrinsic reasons.

### Theorem C: Coupled Path to the Critical Line

Construct a path

\[
\tau_m\downarrow 1/2,\qquad N_m\to\infty
\]

such that:

\[
\operatorname{dist}(u,V_{N_m}(\tau_m))\to 0,
\]

while simultaneously:

\[
R_{\tau_m}(N_m)(\tau_m-1/2)\to\infty,
\]

\[
L_{N_m,\tau_m,T}\to 0
\]

for every fixed hypothetical off-line zero \(\rho=\beta+iT\), and the conditioning profile remains controlled enough for the finite lower bounds to survive.

If RH failed, Theorem B would eventually force a positive lower bound on the same distances that Theorem C drives to zero. That contradiction would prove RH.

## 9. Intended Contradiction Mechanism

The target proof has the following logical shape.

Assume RH fails. Then there exists a zero

\[
\rho=\beta+iT,\qquad \beta>1/2.
\]

Choose a path \((N_m,\tau_m)\) with

\[
\tau_m\downarrow 1/2,\qquad N_m\to\infty,
\]

and eventually \(\tau_m<\beta\).

By the forward theorem,

\[
\operatorname{dist}(u,V_{N_m}(\tau_m))\to 0.
\]

By the finite reverse theorem, the zero \(\rho\) forces

\[
\operatorname{dist}(u,V_{N_m}(\tau_m))
\ge
G(\delta_T,\nu_{N_m,\tau_m})-L_{N_m,\tau_m,T}.
\]

By the coupled path theorem, for sufficiently large \(m\),

\[
G(\delta_T,\nu_{N_m,\tau_m})-L_{N_m,\tau_m,T}>0.
\]

This contradicts the forward convergence. Therefore no such zero exists, and RH follows.

Everything in the program is subordinate to making this contradiction rigorous and unconditional.

## 10. Secondary Tracks

Several other structures are important, but they should not enter the proof spine until they preserve finite margins and reverse moduli quantitatively.

### 10.1. Kernel / Co-Poisson / Sonine Normal Forms

Kernel-generated Nyman-Beurling-Baez-Duarte systems, co-Poisson transforms, and Sonine/de Branges spaces are likely the best long-range source of normal forms. They may reveal canonical dual structures, spectral models, and rigidity theorems.

For now, this track should be used to search for margin-preserving normal forms and alternative reverse packets.

### 10.2. Bohr Lift and Prime-Graded Models

Dirichlet-series and multiplicative witness systems naturally lift to the infinite polydisk through the Bohr transform. Prime-graded coordinates may expose cyclicity, module structure, and arithmetic locking.

This track is valuable for understanding multiplicative structure, but it must be quantitatively connected to the base Hardy-module coordinates before it can affect the proof spine.

### 10.3. Explicit-Formula and Positivity Systems

Weil positivity, Li coefficients, de Bruijn-Newman deformations, Toeplitz minors, and finite positivity obstructions provide a powerful laboratory.

However, positivity only becomes part of the main proof after one constructs an explicit intertwiner from finite Hardy-module witness coordinates to explicit-formula test-function coordinates with certified margin control.

Until then, positivity remains a secondary obstruction and diagnostics track.

## 11. Immediate Work Plan

The next phase should focus on concrete theorem development rather than further abstraction.

### 11.1. Build the Finite Half-Plane Extremal Problem

Derive the exact Gram matrix for

\[
\|\phi_\tau D_N\|_{H^2(\Omega_\tau)}^2
\]

and the exact target vector for projecting \(u\) onto \(V_N(\tau)\).

Deliverables:

- closed formulas for matrix entries,
- numerical validation at finite \(N\),
- asymptotic estimates as \(N\to\infty\),
- condition-number profiles as \(\tau\downarrow 1/2\).

### 11.2. Construct Raw Reverse Functionals

For a hypothetical zero \(\rho\), construct evaluation and jet annihilators explicitly in \(H^2(\Omega_\tau)\).

Deliverables:

- reproducing kernel formulas,
- jet kernel formulas for multiple zeros,
- raw lower bounds for \(\operatorname{dist}(u,V_N(\tau))\),
- height-dependence of those lower bounds.

### 11.3. Improve Reverse Packets

Strengthen raw evaluation defects using finite Gram sections, orthogonal projections, and biorthogonal systems.

Deliverables:

- projected kernel packets \(\psi_{N,\tau,\rho}\),
- lower bounds depending on both \(T\) and \(N\),
- explicit loss from localization and projection,
- comparison with Nyman/Baez-Duarte distance behavior.

### 11.4. Determine Resolution Scale

Define and estimate \(R_\tau(N)\) for the finite Dirichlet hierarchy.

Deliverables:

- heuristic model for visibility of a zero \(\rho=\beta+iT\),
- rigorous upper and lower resolution estimates,
- relation to \(N^{\beta-\tau}\)-type terms where appropriate,
- compatibility with local zero-spacing normalization.

### 11.5. Connect Off-Critical Deformations

Use weighted Hardy/Dirichlet deformation results to define the forward frontier \(\sigma(\tau)\) and the approach to \(\tau=1/2\).

Deliverables:

- precise statement of forward theorem used,
- loss ledger for deformation,
- coupling conditions between \(N\) and \(\tau\),
- identification of conditioning barriers.

### 11.6. Search for Obstruction Theorems

Treat failures as valuable. Prove impossibility results where appropriate.

Possible obstruction theorems:

- a witness class cannot be reverse-detecting,
- a transport destroys conditioning,
- reverse packets decay too fast in height,
- \(R_\tau(N)\) grows too slowly,
- positivity margins cannot be preserved.

Such results would prune the program and prevent wasted work.

## 12. Standards for Mathematical Progress

Progress should be measured by theorem packages, not by new vocabulary.

The following count as meaningful progress:

- A finite Gram formula with controlled error.
- A condition-number estimate strong enough to inform the coupled path.
- A same-coordinate reverse lower bound.
- A resolution theorem for \(R_\tau(N)\).
- A transport theorem preserving margins and reverse signal.
- A rigorous obstruction theorem eliminating a class.
- A verified finite positivity obstruction connected to witness coordinates.
- A proof that a secondary normal form preserves the base finite invariants.

The following do not count as proof progress by themselves:

- Another RH-equivalent criterion with no finite reverse theorem.
- Qualitative transport with no norm or loss control.
- Density in a non-critical topology.
- Positivity analogies without an explicit intertwiner.
- Numerical evidence without certified finite inequalities.
- A universal classification program before the base theorem package exists.

## 13. Known Risks

### 13.1. The Reverse Theorem May Encode RH

The finite reverse theorem may be as hard as RH itself. This is acceptable only if the theorem is sharply localized and produces intermediate unconditional estimates. If it cannot be decomposed into meaningful subtheorems, the strategy is probably too opaque.

### 13.2. Height Leakage

Raw evaluation defects decay badly with height. Any successful reverse packet must overcome or precisely balance this decay.

### 13.3. Conditioning Blow-Up

As \(\tau\downarrow1/2\), finite Gram matrices and transports may become ill-conditioned. If the conditioning loss dominates the reverse signal, the path theorem fails.

### 13.4. Noncommuting Limits

The limits \(N\to\infty\), \(\tau\downarrow1/2\), and \(T\to\infty\) may not commute. The proof must specify the order and coupling of limits explicitly.

### 13.5. False Universality

The original broad representation-theoretic vision may be too ambitious. The current program deliberately avoids relying on global universality.

### 13.6. Positivity Without Transport

Explicit-formula positivity is powerful but irrelevant to the proof spine unless it is quantitatively connected to the finite witness coordinates.

## 14. Development Ethic

The program should remain theorem-first.

Every abstraction must earn its place by producing one of:

- a finite computation,
- a norm estimate,
- a lower bound,
- a transport inequality,
- a conditioning estimate,
- a limit theorem,
- an obstruction theorem.

The purpose of the witness-system language is not to rename known RH criteria. It is to enforce a proof discipline: forward approximation and reverse obstruction must meet in the same finite coordinates, with all losses visible.

## 15. Strategic Endpoint

The program succeeds if it proves the following unconditional statement.

There exists a Hardy-module / weighted-deformation witness-constraint system and a coupled path

\[
(N_m,\tau_m),\qquad N_m\to\infty,\quad \tau_m\downarrow1/2,
\]

such that:

1. The forward distances satisfy

\[
\operatorname{dist}(u,V_{N_m}(\tau_m))\to0.
\]

2. For every hypothetical zero \(\rho=\beta+iT\) with \(\beta>1/2\), the same finite coordinates satisfy

\[
\operatorname{dist}(u,V_{N_m}(\tau_m))
\ge
G(\delta_T,\nu_{N_m,\tau_m})-L_{N_m,\tau_m,T},
\]

and the right-hand side is eventually positive.

3. The transports connecting the critical Hardy avatar, half-plane module avatar, and weighted-deformation avatar preserve the required inequalities.

These statements would contradict the existence of any zero off the critical line. Therefore they would prove the Riemann hypothesis.

That is the objective of this research program.

## Appendix A. Established Inputs to Use

This section records the main existing mathematical structures that motivate the program. These inputs are not assumed to prove RH. They are starting points, tools, and constraints.

### A.1. Nyman-Beurling-Baez-Duarte Closure

The Nyman-Beurling criterion and Baez-Duarte's discrete refinement give the prototype of a witness system: a target vector, a structured family of witnesses, and an exact RH-equivalent closure statement.

This input motivates:

- target-plus-span formulations,
- finite truncations indexed by integer dilation,
- approximation distances,
- the need to distinguish critical topology from weaker topologies.

### A.2. General Kernel and Co-Poisson Criteria

Baez-Duarte's broader kernel criteria and related co-Poisson/Muntz transforms show that the classical witness family is not isolated. There are kernel-generated families with necessity and sufficiency theorems under analytic hypotheses.

This input motivates:

- kernel normal forms,
- transport between witness systems,
- Sonine/de Branges tracks,
- broader classes of witness constructors.

### A.3. Hardy-Space Transport

Hardy-space formulations, especially the disk model with functions \(h_k\), supply an exact Hilbert-space RH criterion and expose semigroup structure through weighted composition operators.

This input motivates:

- the critical Hardy avatar,
- explicit Hilbert geometry,
- semigroup/cyclicity analysis,
- the warning that compact-open density is too weak.

### A.4. Half-Plane Module/Range Criteria

Wei-Wu-type Hardy half-plane criteria interpret zero-freeness through multiplication ranges. For suitable \(\phi\), closure of \(\operatorname{Ran}(M_\phi)\) is equivalent to nonvanishing of \(\phi\) in a half-plane.

This input motivates:

- the half-plane module avatar,
- the use of \(\phi(s)=((s-1)/s^2)\zeta(s)\),
- finite Dirichlet-polynomial module spaces,
- evaluation and jet annihilators at zeros.

### A.5. Dual and Biorthogonal Infrastructure

Work on orthogonal complements, Toeplitz kernels, de Branges-Rovnyak spaces, and complete biorthogonal sequences supplies the kind of dual machinery needed to convert failure of closure into explicit obstruction.

This input motivates:

- reverse packets,
- projected kernel functionals,
- finite dual extremal problems,
- same-coordinate lower bounds.

### A.6. Weighted and Off-Critical Deformations

Weighted Hardy and Dirichlet-space deformation results show that approximation properties away from the critical parameter can imply actual zero-free half-planes.

This input motivates:

- the off-critical forward frontier,
- paths \(\tau\downarrow1/2\),
- conditioning analysis near the critical boundary,
- finite Hilbert projection algorithms.

### A.7. Arithmetic Locking

Several formulations force coefficient limits related to the Mobius function. This indicates that successful finite witnesses cannot be arbitrary analytic approximants; they must eventually lock onto arithmetic structure.

This input motivates:

- coefficient diagnostics,
- prime-graded models,
- Bohr-lift investigations,
- rigidity tests for finite witnesses.

### A.8. Explicit-Formula and Positivity Criteria

Weil positivity, Li coefficients, de Bruijn-Newman deformations, and finite Toeplitz-minor obstructions show that RH can be encoded in positivity systems.

This input motivates:

- positivity diagnostics,
- finite obstruction laboratories,
- possible future backends,
- strict separation between unconditional proof spine and conditional shadow models.

## Appendix B. First Milestones

The first milestones should be concrete enough to fail.

### B.1. Finite Gram Matrix Notebook

Produce explicit formulas and computations for the finite half-plane module extremal problem:

\[
\operatorname{dist}(u,V_N(\tau))^2.
\]

Minimum output:

- formulas for \(G_{N,\tau}\) and \(b_{N,\tau}\),
- numerical computations for small and medium \(N\),
- plots or tables of \(\kappa(G_{N,\tau})\) as \(\tau\downarrow1/2\),
- observed scaling laws.

### B.2. Raw Evaluation Bound

For a hypothetical zero \(\rho\), write down the exact reproducing-kernel lower bound implied by evaluation at \(\rho\), including height dependence.

Minimum output:

- kernel norm in \(H^2(\Omega_\tau)\),
- value of \(u(\rho)\),
- raw lower bound,
- explanation of why the raw bound is insufficient.

### B.3. Projected Reverse Packet

Project evaluation and jet kernels against finite witness spaces to construct \(\psi_{N,\tau,\rho}\in V_N(\tau)^\perp\).

Minimum output:

- finite formula for the projected packet,
- lower bound in terms of the same Gram data as the forward problem,
- numerical behavior as \(N,T,\tau\) vary,
- first estimate of the resolution function \(R_\tau(N)\).

### B.4. Transport Ledger

Write the exact norm-comparison ledger between the disk Hardy avatar and half-plane module avatar.

Minimum output:

- operator map,
- domain and range spaces,
- norm distortion bounds,
- finite truncation mismatch,
- loss term entering \(L_{N,\theta,T}\).

### B.5. Coupled-Path Feasibility Test

Before attempting a proof, test whether plausible scalings can satisfy:

\[
R_{\tau_m}(N_m)(\tau_m-1/2)\to\infty
\]

while keeping conditioning loss below reverse signal.

Minimum output:

- candidate scalings for \(N_m\) and \(\tau_m\),
- estimated forward error,
- estimated reverse modulus,
- estimated conditioning loss,
- explicit reason the path survives or fails.

## Appendix C. Working Rules

The program should follow these rules.

1. Every new abstraction must produce a finite inequality, a transport estimate, a reverse lower bound, or an obstruction theorem.
2. Every finite theorem must state its topology and norm.
3. Every transport must state its losses.
4. Every use of positivity must specify the finite coordinates it receives from the witness system.
5. Every limiting statement must specify the coupling of \(N\), \(\theta\), and \(T\).
6. Every conditional construction must be labeled as a shadow model and kept out of the proof spine.
7. Failed theorem attempts should be converted into obstruction results whenever possible.

The program is ambitious by design. Its standard is an unconditional proof of RH, and its discipline is that every step must move toward a finite same-coordinate contradiction for hypothetical off-line zeros.
