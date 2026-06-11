# Prime-Toeplitz proof scaffold

This directory is the theorem/proof track extracted from
`research/work/H-proof-program.md`. The goal is to keep the proof attempt separate from numerical
diagnostics while preserving the conventions those diagnostics fixed.

## Objective

Prove the pole-killed Prime-Toeplitz domination theorem:

```text
P_Euler <= W_infty
```

on the Sonin support filtration. In nested form, for `H_L subset H_R`,

```text
M_R = W_infty - P_Euler(R)
```

must be a positive extension from `H_L` to `H_R`. Equivalently, in the `L2`-orthogonal splitting

```text
H_R = H_L + shell,
M_R = [ A  C  ]
      [ C* D  ],
```

the load-bearing target is the Schur inequality

```text
C* A^{-1} C <= D.
```

## Current files

0. `00-reduction-to-rh.md`
   Records the reduction `nested target => RH` with its provenance (Connes-Consani
   arXiv:2006.13771 + Weil's converse) and the four certification obligations O1-O4, including
   the CC20 base-case anchor (`A_infty >= 0` on the pole-killed Sonin space for support below
   `log 2` is CC20's theorem). Fixes the program's one-line shape: extend CC20's archimedean
   positivity past support `log 2`, paying with exact Euler atoms.

0a. `00a-detection-lemma.md`
   The O3 converse: an off-line zero forces a negative admissible test. The polynomial-
   prefactor device `h = (-D^2)(-D^2+1/4)G` makes pole-killing free; the phase-tuned
   two-member window produces the negative quadruple; on-line and attained-supremum
   interference are estimated; the unattained-supremum case is reduced to one stated
   averaging sub-lemma.

1. `01-sonin-schur-scaffold.md`
   Defines the continuum support spaces, pole-killing functionals, inclusion maps, and the Schur
   block target. It proves the first structural lemma: the Sonin spaces form a closed filtration, and
   Euler atoms with shift past the old support do not change the old block.

2. `02-euler-chebyshev-transgression.md`
   Begins the first arithmetic lemma. It proves the exact Euler/Chebyshev transgression identity
   behind the storage target:

   ```text
   sum Lambda(n) phi(log n) - int phi(U)e^U dU
     = phi(B)F(B) - phi(a)F(a) - int_a^B F(U)phi'(U)dU.
   ```

3. `03-schur-stress-kernels.md`
   Proves the Schur transfer first-variation formula, defines critical and boundary stress kernels,
   and isolates the first-crossing boundary class where the Lorentz stress becomes
   `k(U)=B_U(x-y,x-y)`.

4. `04-storage-riccati-target.md`
   Fixes the sign convention for exact-minus-smooth Euler residuals at a Schur boundary and states
   the Riccati/storage inequality that must replace naive pointwise residual monotonicity.

5. `05-finite-riccati-identity.md`
   Proves the exact finite Schur-complement update identity
   `S_+ = S + Q - R* A_+^{-1} R`, identifying the negative Riccati square the storage certificate
   must pay for.

6. `06-proof-outline-and-formalization.md`
   Collects the current proof skeleton, records what the finite Riccati diagnostic says, and marks
   which pieces are ready for eventual Lean formalization.

7. `07-active-debt-geometric-lemma.md`
   Converts the late active debt stress near the support edge into a one-sided edge-profile
   convolution and states the finite weighted-average repair inequality now being tested.

8. `08-default-t1-certificate.md`
   Records the simplified default T1 endpoint: for the exact active-23 residual cell, the finite
   matrix `H=S+G` is positive definite on the whole two-dimensional shell. This reduces the default
   sector theorem to a small Sylvester/interval certificate.

9. `09-inverse-analysis.md`
   The R1 risk-rung results: exponential margin decay kills slack-bearing estimates
   (certificates must be exact identities with terminal sign / KYP shape); the cluster
   obstruction (Maynard triples) kills per-cell repair lemmas unconditionally; the window
   dial locates the unconditional arithmetic input (short-interval PNT at 7/12) and the
   conserved difficulty; one-place passivity proposed and refuted the same day; drop-one
   and KMS-exponent rigidity show positivity is an irreducibly collective interference
   lattice pinned at beta=1/2.

Related witness:

```text
scripts/numerics/witness/prime_defect_active_debt_current.py
scripts/numerics/witness/prime_defect_active_atom_shift.py
scripts/numerics/witness/prime_defect_edge_cone.py
scripts/numerics/witness/prime_defect_shell_landscape.py
scripts/numerics/witness/prime_defect_default_t1_certificate.py
scripts/numerics/witness/prime_defect_t1_error_budget.py
scripts/numerics/witness/prime_defect_t1_stability.py
scripts/numerics/witness/prime_defect_t1_arb_components.py
scripts/numerics/witness/prime_defect_t1_winf_tail.py
scripts/numerics/witness/prime_defect_export_julia_reduced.py
scripts/numerics/julia/active23_ad.jl
scripts/numerics/witness/prime_ladder_scaling.py
scripts/numerics/witness/prime_single_place_passivity.py
scripts/numerics/witness/prime_interference_rigidity.py
scripts/numerics/witness/prime_killing_resonance.py
scripts/numerics/witness/prime_margin_law.py
scripts/numerics/witness/prime_edge_compliance.py
scripts/numerics/witness/prime_edge_tracking.py
scripts/numerics/witness/prime_edge_residual_zerosum.py
scripts/numerics/witness/certify_chain.py
```

10. `10-realization-spec.md`
    The post-R1 construction target: a passive prime-side realization whose energy identity
    is the explicit formula; must-encodes E1-E4, graveyard guards G1-G6, sub-targets S1-S3
    with outcomes (S1: one-mode state confirmed; S2: no channel decomposition - fail-closed).

11. `11-edge-window-factorization.md`
    PROVEN: dead upper half-edge, terminal-window factorization, and the exact
    edge-convolution identity I(U) = (q_x * r_y)(w(U)) with the exact rank bound -
    old-shell coupling is the one-sided convolution of edge profiles.

12. `12-edge-compliance-reduction.md`
    DERIVED EXACTLY: within an edge the old block freezes (E_A = 0), the whole chain is
    quadratic, and the old space acts only through compliance alpha = u*A^{-1}u and shell
    vector b; S_N = S_0 + sum E_D - vb* - bv* - alpha vv*; validated to 2e-5; the
    completed square gives the tracking form.

13. `13-tracking-equivalence.md`
    R-TRACK TERMINAL RESULT: tracking is real (cos -> +0.9995, DH fails as a tracking
    failure with tau = 1.554 > 1), and the residual r = v + b/alpha IS the zero
    cross-correlation (verified vs 5000 zeros) - the tracking theorem is zero-repulsion
    restated. The program's product: RH <=> uniform tau < 1 along the one-mode recursion,
    plus the certified reduction and the no-go map.

14. `14-fork-protocol.md`
    STANDING DISCIPLINE: the derivedness detector (F1 value fork via fork_lib, F2
    deformation kill, F3 slack audit) plus the positive criteria P1 (extra information)
    and P2 (DH killed by carrier non-existence; necessary not sufficient - BC caveat).

15. `15-second-description-spec.md`
    The spec for a description of the Weil form not passing through the explicit formula
    (S1 carrier orthogonal to prime positions, S2 non-scheme doubling, S3 native discrete
    positivity, S4/S4' comparison on the full locus, S5 fork compliance), with the
    prior-art audit of all candidate carriers and their walls.

16. `16-doubled-lab-conservation.md`
    R-SQ TERMINAL RESULT: the doubled (pair) laboratory - exact closure, the finite
    Goldston-Montgomery identity, phase-free frequency-localized detection with measured
    threshold, and the TRICHOTOMY (free-blind / level-1 Bochner / the index = RH): the
    two-variable conservation law. Sharpest wall: doubling is cheap; an integer-valued
    intersection pairing is the entire cost. Witnesses: prime_pair_closure,
    prime_pair_fork, prime_pair_dh_growth, prime_pair_localization,
    prime_pair_castelnuovo, fork_lib.

17. `17-integer-search.md`
    R-INT FIRST PASS: the count-fingerprint pipeline (calibrated machine-exact), the
    grammar refinements (self-duality = the FE as count duality; temperedness; the
    Epstein boundary => the reachable set is the Selberg class with cardinality
    coefficients), and C4: Hall self-dual-grade forms are positive definite (a metric,
    no index) because the Euler form vanishes identically on finite Z-modules
    (|Ext^1| = |Hom| - "Spec Z is 1-dimensional", categorically). Redirect: C4'.
    Witnesses: count_fingerprint, count_hall_signature.

18. `18-derived-square-thh.md`
    R-INT SECOND PASS (C4' executed): the diagonal's derived self-intersection in the
    square Z (x)^L_S Z IS THH(Z); Bokstedt's torsion gives <Delta,Delta>_tors =
    zeta'(0) = -(1/2) log 2pi < 0 - the first sign-bearing pairing on an arithmetic
    square, its value the archimedean constant produced from integer torsion counts;
    genus reading g_Z ~ 1.459 > 1. Wall relocated to PROPERNESS over the sphere
    (nothing truncates the affine square's Ext tower; the zeros sit behind the global
    Euler characteristic). New fronts: C5 (TP-style compactification / S-arithmetic
    Riemann-Roch), C6 (Frobenius family via Adams operations on KU ^ KU).
    Witness: prime_int_derived_square.

19. `19-properness-supply.md`
    R-INT THIRD PASS (C5 first pass): properness decomposed (finiteness / duality /
    Riemann-Roch / section counts); the diagonal's S^1-weighted characteristic function
    is sqrt(2pi)/Gamma(s+1) with digamma log-derivative (the EF's archimedean supply
    shape, s=0 recovering zeta'(0)); von Mangoldt IS the THH(F_p) log-cardinality
    dictionary (categorical deformation kill: DH atoms have no carrier); the ENTIRE
    supply side of the explicit formula = THH count ladders. Sharpest wall: properness
    = Poisson summation as a theorem about ring spectra (classical face vdGS theta-RR;
    char-p face Hesselholt's properness hypothesis; S-level open).
    Witness: prime_int_thh_supply.

20. `20-tate-ladder-selfdual.md` [CORRECTED 2026-06-10]
    R-INT C5' diagnostic: duality completion generates the FULL LADDER (the local
    factor with p^(s/2) appears under the symmetric regularization scheme); the
    degenerate archimedean ladder gives sqrt(2pi)/Gamma(s/2) with the 1/4-shift
    digamma on the critical line. CORRECTED in place (secs 2-3, 6): KMS-1/2 is a
    SCHEME datum, not a ladder datum - Deninger 1992 Prop 2.3 / Hesselholt select
    the prefactor-free scheme; realization inputs are 3-for-4 + a scheme-dependent
    fourth whose selection principle is open (= the archimedean/C_2 question, gate
    C5''-infty). Witnesses: prime_int_tate_ladder, prime_int_deninger_convention.

21. `21-fleet-synthesis.md`
    Verified four-front fleet synthesis (workers I/J/K/L in research/work/): the ku
    ladder |T_2w| = lcm(1..w+1)/(w(w+1)) (global EF supply in one object, even-degree
    / positive sign); the scheme separation refuting doc 20's headline; CC's PROVEN
    integer Riemann-Roch + Serre duality for compactified Spec Z (the missing object
    exists at curve level); T1 interval-CERTIFIED (R2 closed). Three tensions
    (scheme, genus clash, sign flip) collapsed into the pre-registered front gate
    Q-SCHEME; new standing gate G-INT6 (degrees-of-freedom audit, O_K negative
    control). Witnesses: prime_int_ku_ladder, prime_int_deninger_convention,
    prime_defect_t1_interval_certificate.

22. `22-genus-audit.md`
    Q-SCHEME first gate executed: the CC-vs-THH genus clash is INVARIANT-LEVEL (no
    unit reconciles; different objects, both correct - the wall is now measured by
    the pair (-2 log 2, +(1/2) log 2pi)); doc 18's sign is native to the count
    reading only (operator reading flips at c = 2pi) and the genus number is demoted
    to calibration; the G-INT6 ring-bearing control is live
    (<Delta,Delta>_{O_K} = d zeta'(0) + (1/2)log|d_K| via Lindenstrauss-Madsen,
    discriminating, tracks xi_K's |d|^{s/2}). Witness: prime_int_genus_audit.

23. `23-adams-family-signature.md`
    C6''' first pass, fail-closed NEGATIVE: the bare Adams family Gram log|k-l| is not
    Lorentzian (signature ~(0.43n, 0.57n)); the constant-diagonal window escapes
    linearly - the FF Castelnuovo form needs the bidegree correction and a k-dependent
    diagonal, both supplied only by the full Adams-twisted THH (C6'' promoted to
    primary). Witness: prime_int_adams_family_signature (refutation-grade).

24. `24-reflection-fold.md`
    C5''-infty first checkpoint (worker M, verified): the archimedean fold lives on
    C_2 FIXED POINTS (Tate contractible at odd p; THR(F_p)^{C_2} = F_p[y], |y|=4 =
    the half-line spacing-2 ladder); functor dichotomy rotations->Tate->full ladder
    vs reflections->fixed points->folded ladder; the C_2-involution realizes Serre's
    F_infinity eigenvalue selection. PARITY LEMMA: c = 1/2 is the unique
    reflection-equivariant scheme - KMS-1/2 forced by real equivariance, conditional
    on the single named hypothesis H-r3. Witness: prime_int_thr_fold.

25. `25-p2-computed.md`
    The p=2 anomaly COMPUTED (worker S, new theorem: THR(F_2)^{tC_2} closed-form):
    at 2 the real place degenerates to a complex place (Legendre duplication
    mirrored); the permanent part is rank-2 (Barnes Gamma_2); the reflection sector
    exhibits the 2-adic Euler factor in self-dual KMS-1/2 form. Convergence: the
    scheme selector lives at the prime 2 (O's lambda^{1/2} + S's geometric KMS-1/2
    + CC's K = -2{2}). Witness: prime_int_thr_p2_anomaly.

26. `26-cycle-synthesis.md`
    All-fronts cycle synthesis (workers O/P/Q/R/S): two new theorems (H-r3 analytic
    half; THR(F_2)^{tC_2}), three corrections propagated, T1+T2 certificate-grade,
    the strict CC square carries invisible square data (grading = the bridge), the
    Adams group cannot carry Castelnuovo growth (monoid/Frobenius required). The
    address: the prime 2 and the monoid. Ranked live fronts in sec 4.

27. `27-cycle3-synthesis.md`
    Cycle-3 synthesis (workers T/U/V/W/X): the max-Gram lemma + first certified
    Lorentzian family (product formula splits the two faces); the full ladder
    certificate-grade incl. the DH control certified failing; F1 negative for THR
    (the Weyl shears; scheme = archimedean = properness = ONE question, C5''');
    fork (N) = branch (i) at filtration 0 with the abutment literature-decidable;
    the grading bridge refuted - the strict square's universal invariant is the
    monoid ring of Z\0. Three-deep convergence: MONOID and COMPACTIFY. Proposed
    next object (pending sign-off): the product-formula determinant category.

28. `28-product-formula-spec.md`
    The PFD spec (user-approved direction): the compactified archimedean object
    POSED as a structure - local determinant ladders + the degenerate sector,
    glued by the PRODUCT FORMULA, with Poisson/the extension of U's finite-level
    residue pairings as the defining property (Conjecture U.2 = the p=2
    instance; Hesselholt's iota made structural). Kill-test battery K1-K6
    pre-registered (scale out not in; negation restored => KMS-1/2 forced;
    Barnes Gamma_2; Q's pole evaded; carrier fatality; zero free choices);
    failure modes F-a/b/c named in advance.

29. `29-cycle4-synthesis.md`
    PFD-launch cycle (workers Y/Z/AA): fork closed ((L) = NO via Kane - the Euler
    supply is NOT in the invertible Adams family, decided); the PFD has a
    CC-internal strict model (the norm IS the MAX face; product formula as an
    identity of invariants); U.2 executed with K2 PASS - KMS-1/2 FORCED at p = 2
    (realization input 4 regains a carrier at instance level); K1 = cross-place
    with the mechanism named (the glued object is exactly scale-free). Next: PFD
    step 2, the global assembly - does the EF's archimedean constant emerge from
    the cross-place trace?

30. `30-cycle5-synthesis.md`
    PFD step-2 cycle (workers BB/CC/DD): the object EXISTS (Xbar, pi_* = G, theorem
    mod S.1); D' is the continuous Brown-Comenetz dual (plain BC unsatisfiable -
    U.2 repaired to Conjecture DD.4); K1 = B3 with a proven equivariance no-go
    (the FE layer is scale-blind - the vacuity guard is now quantitative; missing
    ingredient = the archimedean Poisson exchange, the Gaussian's seat); gluing
    not 2-specific (p = 3, 5); K3 PASS (s(s-1) candidate self-dual under the
    forced recentring); K4 PASS by DUALITY CANCELLATION (a third evasion
    mechanism). The remainder is one conjecture: DD.4, whose duality does triple
    duty (scheme + pole + scale). Ranked continuations in sec 3.

31. `31-line-closure.md`
    Cycle-6 synthesis + PFD line closure: DD.4's Lin clause PROVEN (singleton
    datum; display fixed); N1-b refuted and re-posed; the cancellation
    globalizes (duality = existence mechanism; renormalized survivor = the EF
    prime-side shell); the scale EXPELLED from torsion (Prop FF.1) - DD.4's
    duty drops to scheme + pole. Two named exits: (A) DD.4 on weights >= 1,
    (B) the archimedean unit, triply specified (comb-continuum coupling, one
    unit per place, rational/Anderson layer). The index/density layer (the
    zeros) stands guarded behind both.

32-37. `32-index-attack-charter.md` through `37-stress-round.md`
    The index attack and face/stress rounds: the strict square makes the
    index inequality posable, the unit insertion repairs it with zero slack,
    deep-face tests demote several apparent obstructions to slot data, and
    the remaining target becomes a coupled archimedean unit rather than a new
    finite-window estimate.

38. `38-strategic-charter.md`
    Switches the program from search to construction-by-interface. Standing
    gates become lesson elevation, full-ledger scoring, the second-evaluation
    principle, and a critic worker every cycle.

39. `39-charter-cycle1.md`
    Cycle 1 under the charter: Delta_p's Gaussian silhouette is shape-complete
    but mechanism-empty; the solenoid supplies address without scale/unit; the
    Quillen pair is a true two-evaluation embryo with empty spectrum.

40. `40-charter-cycle2.md`
    Final-form spec before characterization: object conditions OC1-OC4 plus
    BC13 and BC-E3'. The satisfier's address is the liquid layer and its type
    is an index/Gram on the Frobenius cone with unforced odd-slot eigenvalues.

41. `41-missing-structure-characterization.md`
    Consolidates docs 34 and 38-40 into a testable normal form: candidate
    package, object conditions, slot-data demotions, arrival gates, fast
    falsifiers, and dispatchable consequences M-C/M-A/M-B.

42. `42-mc-carrier-classification.md`
    Executes M-C over the promoted banked carrier families. No carrier passes
    BC-E3'/BC13 at decision grade; the residue is ku-face supply plus
    liquid/metrized address plus index/Gram positivity plus Quillen-style
    second-evaluation independence.

43. `43-ma-self-dual-lp-audit.md`
    Executes M-A from RR/AB witness evidence. The banked Gaussian deep-cell
    obstruction is slot data: a self-dual Hermite unit flips `(11;2)@4.96`.
    OC2 remains k=1 local deficit plus global threading; OC3 keeps the
    unit-free depth wall.

44. `44-mb-g2-exhaustion-boundary.md`
    Resolves M-B against current evidence. NN kills the strict-square /
    hand-inserted-unit proxy for BC13 exhaustion on Frobenius-graph classes;
    a live M-B requires a future liquid/index candidate with its own unit.

45. `45-final-missing-structure-spec.md`
    Consolidates the characterization into the current final specification:
    candidate package, required clauses, negative boundary, positive residue,
    evidence matrix, arrival checklist, and next valid work.

46. `46-construction-blueprint-liquid-index-carrier.md`
    Construction-facing branch from doc 45. It proposes the live tuple's
    native objects, then restricts the buildable start to B0: a Tate-curve /
    liquid-RR trace against the p^Z graded comb, used only to calibrate the
    bank embedding and run the Epstein carrier guard.

47. `47-external-scoping-questions.md`
    External-scoping branch from doc 45. It translates the missing structure
    into field-native questions for condensed/liquid analytic geometry,
    trace/localizing invariants, and arithmetic topology, with YES/NO evidence
    and rejection rules.

48. `48-negative-theorem-targets.md`
    Negative-theorem branch from doc 45. It turns the classified failures into
    reusable no-go targets: scale-blind localizing traces, carrier-blind
    Poisson/Epstein formalisms, inserted or one-place units, strict-face
    positivity, and transport/self-supplied second evaluations.

This extracts the late active Schur-debt direction and reports the smooth-vs-atom arithmetic current
on the debt stress, including the boundary edge-profile diagnostic and the repair atom
location/weight sensitivity. The edge-cone witness computes the one-sided convolution target
directly and tests coefficient perturbations. The shell-landscape witness checks whether the
edge-cone inequality is needed on all shell directions or only on the Schur-negative sector. The
default T1 certificate witness computes `H=S+G`, checks the two-by-two Sylvester endpoint, and
verifies the beta-surplus identity. The T1 error-budget witness gives a conservative post-cell
block enclosure target, and the Arb component witness starts replacing Fourier-grid atom blocks
and smooth-cell blocks with compact rigorous overlap integrals. The W_inf tail witness tests finite
cutoffs, a tail envelope, and endpoint sensitivity for the archimedean block. The T1 stability
witness probes numerical sensitivity of the matrix endpoint before interval certification. The
Julia witness differentiates the reduced shell-direction objective through QuadGK integrals with
ForwardDiff.

## Rules of engagement

- Work in the log variable `u`.
- Use positive-type tests `g = h * h#`.
- Treat the prime term as a Toeplitz correlation `g(log n) = <h, tau_log(n)h>`.
- Kill the pole functionals before asking for positivity.
- Do not use zero-side positivity or any RH-equivalent positivity input.
- Do not replace the exact Euler measure by smooth PNT density before proving the Schur estimate.
- FORK PROTOCOL (doc 14, standing): before investing in any proposed mechanism or object,
  run F1 (zero-side image via `fork_lib` - candidate == image means coordinate change, abandon
  as attack), F2 (deformation kill on DH / beta != 1/2 / smooth), F3 (slack audit). A genuine
  candidate must carry extra information (P1) and fail DH by non-existence of its carrier (P2);
  see doc 15 for the second-description spec.

## Current path (program closure - see TODO.md R-TRACK outcome and doc 13)

1. R-TRACK is resolved fail-closed: the tracking residual is exactly a zero
   cross-correlation (doc 13), so no estimate-based attack surface remains. The
   program's terminal deliverables are (a) the certified reduction, (b) the exact
   structure theory (docs 11-13: RH as uniform tau < 1 along a one-mode scalar
   recursion), (c) the no-go map (every shortcut killed by its own witness).
2. O3 Case B: anchored to the classical Li-coordinate detection (Bombieri 2000,
   archived in refs/); Lemma B2 proven in 00a section 6'; remaining = Lemma B1
   (even + p^2-weighted Li detection; check Yoshida 1992 for weight-robustness).
3. Regression gate: `python3 -m scripts.numerics.witness.certify_chain` re-derives
   the load-bearing claims (C1-C5) and exits nonzero on any flip. Run it after any
   change to the ladder stack or before citing the chain.
4. Background, refutation-grade only: T1 interval certification (Galerkin
   compression can refute, never prove).
