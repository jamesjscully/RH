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

## Trajectory Checks

The active PFV2 target chain is machine-tracked in:

```text
research/proof/target-ledger.json
```

Run:

```bash
python3 scripts/automation/check_proof_targets.py
```

This validates the doc-to-doc target transitions and checks that
`README.md`, `HANDOFF.md`, `TODO.md`, `61`, `129`, `134`, and `139`
agree on the live target. It also rejects keyword-only stubs: shot
docs must carry candidate/gate/verdict/next-target/kill-condition
sections, and no-go docs must carry covered-class/lemma/proof/
surviving-escape/kill-condition sections with exact target-transition
claims. The repository guard also runs this check:

```bash
scripts/automation/guard.sh
```

The current PFV2 gate criteria also have a small executable
calibration harness:

```bash
python3 -m scripts.numerics.witness.pfv2_gate_calibration
```

It does not construct PFV2. It checks a structural toy source record
against the present gate logic, reports every failed gate for known
false-positive classes, and leaves only the declared schema-survivor
profile. It also fails if `target-ledger.json` moves to a new current
target without updating the calibration object.

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

49. `49-b0-tate-rr-calibration.md`
    Lands the smallest honest construction object from doc 46:
    `B0=(L0,b0,R0/T0,tr0,comb_p,Count0)`. The witness
    `prime_b0_tate_rr_calibration.py` verifies RR/trace scale-freeness,
    the p^Z Poisson address, absence of promotion fields, and the Epstein
    replacement guard. Verdict: calibration floor only, not the carrier.

50. `50-external-falsification-packets.md`
    Converts doc 47 into sendable expert packets for liquid analytic
    geometry, trace/localizing-invariant theory, arithmetic topology, and
    no-go/comparison reviewers. Each packet has exact YES/NO/UNKNOWN answer
    formats, clause consequences, rejection rules, and a short reading list.

51. `51-scale-blind-localizing-trace-no-go.md`
    First broad no-go from doc 48. Conditional on the Efimov statements as
    cited in MM/XX, bare sheaf categories `Shv(R/(log p)Z; C)` and their
    continuous localizing-invariant traces forget `log p`; this kills cheap
    liquid-circle/localizing-trace candidates while leaving metric,
    analytic-ring, equivariant, and kernel-trace escapes open.

52. `52-transport-self-supplied-second-evaluation-no-go.md`
    Broad no-go for doc 45 clause E. Transport comparisons,
    regularizations of one object, coker=det algebra, TP/TR/Witt transport,
    and acting-degree/self-supplied spectra fail P3 independence, nonempty
    odd-slot, unforced-eigenvalue, or contentful-comparison gates.

53. `53-carrier-blind-poisson-epstein-no-go.md`
    Broad no-go for carrier-blind LCA/lattice/theta/Poisson/multiset
    formalisms. If the same LS4-like trace/coupling computes for Epstein
    or DH controls, B2/B3 fail before any sign test; the `x^2+5y^2`
    represented-norm monoid gives the concrete guard.

54. `54-b1-admission-gate.md`
    Construction gate after B0. A proposed B1 must name the first retained
    `log p` structure, state LS3 status, write an LS4-like same-form
    coupling, and show Epstein death at carrier/effectivity before it is
    worth building witnesses or discussing positivity.

55. `55-one-place-inserted-unit-no-go.md`
    Broad no-go for doc 45 clause C. Signs or payment constants depending
    on a chosen/movable unit are slot data; one-place bookkeeping cannot
    prove global threading without product-formula or KMS-beta=1/2
    assembly.

56. `56-strict-face-positivity-no-go.md`
    Broad no-go for doc 45 clause D/BC13. Positivity on a strict square,
    ku face, max-Gram face, rung tower, finite panel, or other proper
    subcone cannot prove full graph-cone exhaustion or uniformity; inserted
    repairs also fail candidate-native unit and forced-nonnegativity gates.

57. `57-p-complete-archimedean-blindness-no-go.md`
    Reusable gate for purely p-complete TP/TR/Witt/prismatic constructions.
    Without internal archimedean `R/T`, structural `iota`, and same-form LS4
    coupling, they remain p-adic supply/address shadows; TR/Witt transport
    also fails P3 independence and unforced-eigenvalue gates.

58. `58-max-gram-signature-insufficiency-no-go.md`
    Reusable insufficiency gate for Lorentzian signature, max-Gram,
    norm-Gram, and stress-flow certificates. They can certify shape and
    supply constraints, but they do not supply independent `Count`,
    native `H_odd`, contentful `Compare`, or BC13 exhaustion by themselves.

59. `59-zero-import-circularity-no-go.md`
    Protocol gate for zero-side data. Zeta zeros, zero-side signs,
    zero-side eigenvalues, or RH-line information may enter only after the
    candidate is frozen and only as comparison/fork diagnosis; using them
    to construct the carrier, slot, unit, positivity, or comparison is
    circular.

60. `60-gate-stack-and-b1-escape-profile.md`
    Consolidates docs 49-128 into the operational G60 gate stack. It states
    the pre-witness checklist, the smaller B1 admission rule, the full
    candidate theorem obligations T_A-T_E, and the next valid work after
    the doc-48 no-go list.

61. `61-external-answer-ledger.md`
    Operational ledger for answers to the doc-50 external falsification
    packets. It records each answer against doc-45 clauses and G60 gates
    before any trajectory update is made.

62. `62-scale-blind-citation-audit.md`
    Citation/dependency audit for doc 51. It checks the archived Efimov PDF
    against the XX/MM transcriptions, confirms the core bare-circle
    scale-blind statement as directly citable, and separates the full
    lattice-diagram claim as a derived naturality lemma needing polished
    proof wording.

63. `63-scale-blind-diagram-naturality-lemma.md`
    Supplies the local diagram lemma isolated in doc 62. The bare diagrams
    `lZ -> R -> R/lZ` are isomorphic by scaling, so any functorial
    localizing-invariant observable of the bare diagram is independent of
    `l`; enriched metric/liquid/equivariant/kernel data remain outside the
    lemma.

64. `64-epstein-carrier-guard-lemma.md`
    Proof-level version of the concrete Epstein guard used in docs 49, 53,
    54, and 60. For `Q=x^2+5y^2`, the theta/count shadow survives, but
    represented-norm factorization already fails to supply a free
    prime-power valuation/tower address at `36=4*9=6*6`.

65. `65-p3-independence-normal-form.md`
    Proof lemma for the second-evaluation gate. It isolates the P3 normal
    form from YY/ZZ: independent larger domains, contentful comparison, and
    nonzero unforced odd spectrum. Transport, formal agreement,
    self-supplied spectra, and empty spectra fail this normal form.

66. `66-unit-covariance-and-threading-lemma.md`
    Proof lemma for the C-side gate. It isolates the doc-43/AB lesson:
    signs and constants that change under admissible self-dual unit
    replacement are slot data, one-place bookkeeping cannot prove global
    threading, and the surviving object-level target is candidate-native
    unit plus covariant local deficit/global payability/depth wall.

67. `67-bc13-exhaustion-normal-form.md`
    Proof lemma for the D-side gate. It isolates the BC13 exhaustion
    normal form: proper-face positivity is not full class/scale
    exhaustion unless it comes with native nonnegativity, native unit
    covariance, a full-cone exhaustion theorem, and uniform
    support-filtration persistence.

68. `68-archimedean-escape-normal-form.md`
    Proof lemma for the p-complete/archimedean gate. It isolates the
    escape normal form for TP/TR/Witt/prismatic-origin data: internal
    `R/T`, structural `iota`, same-form LS4 coupling, non-transport
    `Count`, and unforced nonzero `H_odd`.

69. `69-zero-free-freeze-normal-form.md`
    Proof lemma for the zero-import gate. It isolates the required
    factorization `candidate construction C -> frozen record F ->
    optional zero comparison Z`, with zero-free suppliers and
    reproducibility records for every load-bearing choice before any
    zero-side contact.

70. `70-gram-diagnostic-normal-form.md`
    Proof lemma for the max-Gram/signature/stress-flow gate. It keeps
    Gram packages in their correct role as shape, supply, diagnostic,
    or compatibility data unless they add independent `Count`,
    `H_odd`, contentful `Compare`, and full native
    positivity/exhaustion data.

71. `71-b1-proposal-ledger.md`
    Operational ledger for the next post-B0 construction. It records
    the required B1 fields, admission tests, optional promotion audit,
    and initial candidate slots; no slot is currently advanced.

72. `72-initial-b1-slot-entries.md`
    Populates the B1 ledger for the initial slots. S1 liquid/gaseous
    trace, S2 metric/equivariant circle trace, S3 explicit
    comb-continuum kernel, and S5 A6/LT76 liquid trace route are HOLD;
    S4 pure p-complete is REJECT unless upgraded to a structural
    archimedean hybrid.

73. `73-s3-kernel-preregistration.md`
    Pre-registers the S3 explicit kernel target before any witness. It
    freezes the carrier interface, B0-inherited test family,
    Epstein/DH formability guards, zero-free fields, and overclaim
    boundaries; `K_B1` remains the required blank.

74. `74-s3-generic-kernel-carrier-blindness.md`
    Proof lemma for the S3 slot. Any kernel factoring only through
    theta/count/Poisson, represented-norm, LCA/lattice, or generic
    discrete-measure shadows computes for Epstein controls and is
    carrier-blind; a surviving `K_B1` must require valuation/depth
    carrier data.

75. `75-kb1-ansatz-ledger.md`
    Construction ledger for the remaining S3 `K_B1` formula shapes:
    depth-weighted one-place combs, two-place valuation-vector
    kernels, HH graph-index lifts, determinant/coker variants, and
    depth-wall stress kernels. None is advanced.

76. `76-liquid-trace-theorem-target.md`
    External theorem target for the best remaining A6/S3 route. It
    states the positive liquid trace package LT76.1-LT76.7 and the
    negative theorem targets NO76.1-NO76.5 that would decide whether a
    trace-retentive, carrier-selective `K_B1` can exist.

77. `77-liquid-trace-expert-packet.md`
    Focused sendable packet for liquid/gaseous geometry and
    trace-of-kernels experts. It asks for an ADVANCE/KILL/SHARPEN
    answer on the LT76/NO76 liquid trace target and gives rejection
    rules plus the landing rule for doc 61.

78. `78-lt76-local-status-audit.md`
    Local audit of the LT76 target. Bare sheaf/localizing-invariant
    scale-collapse is proved, and Route A/B0 calibration is banked, but
    no broad real liquid/gaseous trace no-go or construction is proved.

79. `79-side-block-archimedean-no-go.md`
    Proof lemma for A4/LS4. A trace of the form banked comb value plus
    separate archimedean block, correction, determinant readout, or
    normalization is not a same-form comb-continuum coupling.

80. `80-late-scale-insertion-no-go.md`
    Proof lemma for A1 scale retention. Appending `log p`, `2pi/log p`,
    density, or normalization after a scale-blind trace/localizing
    invariant has been computed is external normalization, not retained
    candidate structure.

81. `81-scale-retention-decision-ledger.md`
    Operational A1 ledger for future B1/A6 claims. It records the
    pre-trace object, structural scale carrier, trace theorem,
    deletion test, late-insertion audit, and same-form coupling status
    before G60.2 or LT76.1 can be marked advanced.

82. `82-factor-through-scale-collapse-no-go.md`
    Bounded NO76.1 proof lemma. Any claimed enriched trace whose
    load-bearing data factors through the bare scale-blind diagram or
    localizing-invariant output is still scale-blind; live escapes must
    prove non-factorization before trace.

83. `83-lt76-response-scoring-rubric.md`
    External-answer rubric for the liquid trace theorem target. It
    scores replies as ADVANCE, KILL, SHARPEN, DEMOTE, or OUT_OF_SCOPE
    and requires doc-61 landing before any gate or trajectory update.

84. `84-non-factorization-theorem-target.md`
    Positive A1 escape target. It states what an enriched
    liquid/metric/equivariant/kernel trace must prove to avoid doc-82
    factor-through collapse without claiming full B1 admission.

85. `85-trace-detection-required-no-go.md`
    A1 false-positive guard. Non-isomorphic enriched objects do not
    advance scale retention unless the load-bearing trace, trace
    domain, or frozen trace value detects the enrichment before
    evaluation.

86. `86-same-form-coupling-decision-ledger.md`
    LS4 positive ledger. It requires one mixed trace object receiving
    both the banked comb and the continuum before evaluation before
    G60.5 or LT76.5 can be marked advanced.

87. `87-carrier-selectivity-decision-ledger.md`
    Carrier-selectivity ledger for G60.1/LT76.6. It requires a named
    first Euler-carrier map that is unformable for Epstein/DH controls
    while theta/count shadows remain meaningful.

88. `88-traceability-proper-pushforward-ledger.md`
    LT76.3 legality ledger. It requires a named duality, properness,
    nuclearity, or trace-class theorem for `T_C -> pt` before `Tr_L`
    can be used in A1, LS4, or carrier claims.

89. `89-conservative-bank-embedding-ledger.md`
    LT76.4 bank-preservation ledger. It requires a conservative map
    from B0 into the proposed trace package preserving the p^Z comb,
    q/log p address, Count0/RR layer, and Epstein guard.

90. `90-internal-archimedean-objects-ledger.md`
    LT76.2/G60.3 ledger for internal archimedean objects. It requires
    structural `R_L`, `T=R/Z`, and archimedean completion in `L1`,
    not p-complete notation, side blocks, or external readouts.

91. `91-zero-free-freeze-ledger.md`
    LT76.7/G60.10 freeze ledger. It requires zero-free suppliers,
    frozen records, reproducibility data, and named first zero contact
    before any zero-side comparison can touch the candidate.

92. `92-lt76-ledger-admission-matrix.md`
    Synthesis/router for LT76.1-LT76.7. It maps each clause to its
    ledger, verdict names, NO76 routing, and no-cross-inference rule
    before any B1 routing or gate-stack update.

93. `93-s3-free-weight-kernel-no-go.md`
    Proof lemma for S3. It rejects valuation/depth-decorated kernels
    whose weights, windows, bilinear forms, stress parameters,
    determinant wrappers, or codomains are externally supplied rather
    than derived by a candidate same-form trace.

94. `94-s3-trace-derived-form-theorem-target.md`
    S3 positive escape target after doc 93. It requires a named L1
    trace theorem deriving the mixed object `M_C` and same-form
    codomain `F_C` that reads carrier depth, or routes the ansatz to
    the exact collapse mode.

95. `95-s3-trace-derived-form-expert-packet.md`
    Sendable packet for the doc-94 S3 question. It asks trace, index,
    kernel, and categorical-trace experts for ADVANCE/KILL/SHARPEN
    answers on whether the carrier-reading codomain can be
    trace-derived, and whether the trace domain is strict enough to
    exclude Epstein/DH before first carrier-consuming evaluation.

96. `96-external-dispatch-message-bank.md`
    Short dispatch messages for the two focused external fronts:
    LT76 liquid trace and S3 trace-derived form/codomain, including the
    strict Euler-carrier trace-domain criterion from doc 98. It also
    lists the doc-61 landing fields needed before reply propagation.

97. `97-monoid-functorial-carrier-overreach-no-go.md`
    S3 carrier-overreach proof lemma. It rejects trace-derived-looking
    forms whose naturality domain includes represented-norm,
    commutative-monoid, or measure shadows that still accept
    Epstein/DH controls.

98. `98-strict-euler-carrier-trace-domain-target.md`
    S3 strict-domain theorem target. It asks for a trace domain that
    excludes Epstein/DH at the first carrier-consuming map while still
    supporting trace legality, conservative bank embedding,
    same-form coupling, and zero-free freeze.

99. `99-s3-strict-domain-local-status-audit.md`
    Local S3 status audit after docs 73/74/93/94/97/98. It records that
    no witness is licensed, rejects generic shadows/free weights/
    overbroad naturality, and leaves only a strict ECar_L1 record or a
    broad no-go against that class.

100. `100-mixed-object-shadow-enlargement-no-go.md`
     Conditional S3 no-go for the doc-99 hardening target. If the mixed
     object and trace/codomain are functorial in broad shadow data before
     primitive carrier checking, Epstein/DH controls still enter and doc
     97 carrier overreach applies.

101. `101-shadow-stable-operation-audit.md`
     Operation-level router for doc 100. It classifies common ways of
     forming M_C or F_C as shadow-stable unless they require primitive
     Euler-carrier fields before the mixed object, codomain, or trace
     exists.

102. `102-s3-ansatz-operation-audit.md`
     Filled operation audit for the doc-75 A0-A6 S3 ansatz classes. It
     keeps only strict ECar_L1-first variants on HOLD and routes
     shadow-stable mixed-object constructions to docs 100 and 97.

103. `103-strict-first-carrier-map-record.md`
     Positive-side first-map record for S3. It requires a candidate to
     name the strict source object, first primitive carrier-consuming
     map, operation order, and Epstein/DH exclusion before returning to
     the full doc-98 strict-domain target.

104. `104-s3-first-map-current-ledger.md`
     Current filled first-map ledger for the surviving doc-75 S3 ansatz
     classes. It records that A1/A2/A3/A5/A6 are still
     `FIRST_MAP_HOLD`, A4 routes to shadow/free-weight rejection unless
     strict-first-map data is supplied, and no class has
     `FIRST_MAP_PASS`.

105. `105-lt76-trace-operation-overreach-audit.md`
     Conditional LT76/A6 audit. If a liquid trace package forms M_C or
     Tr_L through broad measure/kernel/trace-class operations before
     primitive carrier checking, Epstein/DH controls still enter and
     LT76.6 carrier selectivity fails.

106. `106-lt76-trace-operation-current-ledger.md`
     Current LT76 ledger after doc 105. It records no local LT76 PASS
     entries, routes broad trace-operation packages to doc-105
     overreach, and leaves only strict carrier-consuming trace packages
     as HOLD targets.

107. `107-carrier-overreach-meta-lemma.md`
     Theorem-shaped meta-lemma extracting the common mechanism behind
     docs 97, 100, and 105: shadow-functorial constructions before
     primitive carrier checking let Epstein/DH controls enter and fail
     carrier selectivity.

108. `108-carrier-overreach-proof-skeleton.md`
     The theorem-polish skeleton for doc 107. It records the precise
     hypotheses, branch verdicts, dependency table, instantiation
     checklist, and strict-first-map escape clause for the broad
     carrier-overreach no-go class.

109. `109-strict-first-map-relabeling-no-go.md`
     Doc-103 hardening lemma. It rejects first-map records that merely
     relabel or decorate shadow data with carrier names instead of
     making primitive Euler-carrier fields structural before M_C, F_C,
     or Tr_L exists.

110. `110-strict-first-map-expert-packet.md`
     Narrow external packet for the doc-103 prerequisite. It asks
     experts to ADVANCE/KILL/SHARPEN whether a strict source S_C and
     first carrier-consuming map kappa_C can exist before any
     shadow-stable S3 trace/codomain construction.

111. `111-strict-prefix-erasure-no-go.md`
     Post-doc-103 hardening lemma. It rejects proposals that name a
     plausible strict first map but then forget the consumed primitive
     carrier field before forming M_C, F_C, or Tr_L.

112. `112-late-carrier-reintroduction-no-go.md`
     Downstream repair guard. It rejects proposals that first form a
     shadow-stable trace package and only later add carrier fields
     through weights, codomains, normalizations, regularizations, or
     second maps.

113. `113-s3-strict-route-admission-matrix.md`
     Current S3 router after docs 109-112. It records the admission
     order, verdict matrix, minimal positive record, and current
     no-witness status for strict S3 proposals.

114. `114-lt76-strict-trace-admission-matrix.md`
     Current LT76/A6 router after docs 92, 105, 106, 108, and 112. It
     records the strict trace admission order, verdict matrix, minimal
     positive record, and current no-witness status.

115. `115-current-external-decision-queue.md`
     Operational dispatch queue. It lists the active LT76, S3
     first-map, S3 trace-derived codomain, and no-go-reviewer questions
     with packet choices and ADVANCE/KILL/SHARPEN criteria.

116. `116-current-b1-admission-board.md`
     Current B1 board after docs 113-115. It records S1-S5 and S3
     A0-A6 statuses, witness blockers, and decision-grade next actions.

117. `117-a2-two-place-calibration-record.md`
     Smallest post-B0 calibration record. It fills the A2 two-place
     valuation-vector route as FIRST_MAP_HOLD / HOLD_STRICT_ROUTE and
     explicitly blocks any witness license.

118. `118-traceable-envelope-collapse-no-go.md`
     Broad no-go skeleton for strict prefixes whose trace legality is
     obtained only through a carrier-forgetting traceable envelope.

119. `119-current-strict-first-map-dispatch.md`
     Current sendable dispatch and landing template for the S3 strict
     first-map external question.

120. `120-traceable-envelope-operation-audit.md`
     Operational audit for applying doc 118 to Morita, localizing,
     trace-class, liquid/kernel, and related traceable-envelope routes.

121. `121-traceable-envelope-current-ledger.md`
     Current no-pass ledger for doc 120: no S3/LT76 route has a
     carrier-reflecting traceable-envelope pass.

122. `122-carrier-reflecting-envelope-theorem-target.md`
     Positive theorem target for escaping doc 118 by proving a
     carrier-reflecting traceable envelope.

123. `123-carrier-reflecting-envelope-expert-packet.md`
     Sendable expert packet for deciding the carrier-reflecting
     envelope target.

124. `124-current-external-priority-board.md`
     Current priority board for the external queue: doc119 before
     doc123 unless a concrete envelope Q is already named.

125. `125-decorated-envelope-reflection-no-go.md`
     Bounded no-go rejecting inert marks, labels, metadata, or
     post-completion tags as carrier-reflecting envelope data.

126. `126-carrier-reflecting-envelope-admission-matrix.md`
     Operational matrix for envelope-mediated trace proposals, routing
     docs 118/120/121/122/125 in order.

127. `127-carrier-reflecting-envelope-current-ledger.md`
     Current no-pass ledger for doc126: no carrier-reflecting envelope
     pass and no witness license.

128. `128-carrier-reflecting-envelope-response-rubric.md`
     External-answer scoring rubric for doc123 carrier-reflecting
     envelope replies.

129. `129-b1-candidate-assault-ledger.md`
     Candidate-driven operating ledger: attack A2/S3, A6/LT76, A3,
     and S2 directly, and license new no-goes or witnesses only when a
     concrete shot fails in a way that sharpens the criteria.

130. `130-a2-strict-first-map-assault.md`
     First candidate-driven attack on A2/S3: names the PFV2-FIRST
     theorem needed for a product-formula valuation-pair strict source,
     records FIRST_MAP_HOLD, and keeps A2 witness work blocked.

131. `131-a6-lt76-strict-trace-assault.md`
     Candidate-driven A6/LT76 attack: demotes broad liquid trace-class
     packages for B1 purposes, names the surviving LCT-FIRST strict
     trace theorem target, and keeps A6 witnesses blocked.

132. `132-a3-hh-graph-index-assault.md`
     Candidate-driven A3 attack: names the HHG-FIRST theorem needed to
     turn HH graph-index data into primitive carrier object data,
     records FIRST_MAP_HOLD, and blocks Gram/index witness promotion.

133. `133-s2-metric-equivariant-circle-assault.md`
     Candidate-driven S2 attack: fills the metric/equivariant circle
     deletion-test record, names METEQ-A1 as the surviving enriched
     scale-retention theorem target, and keeps S2 witnesses blocked.

134. `134-b1-assault-followup-board.md`
     Operational follow-up queue for PFV2-FIRST, LCT-FIRST,
     HHG-FIRST, and METEQ-A1, with sendable questions and landing
     rules for PASS/KILL/SHARPEN answers.

135. `135-pfv2-coordinate-pair-obstruction.md`
     Bounded internal PFV2 result: rejects coordinate-pair
     B0_p x B0_q plus labels/relations as a strict first map and
     starts the refinement from PFV2-FIRST toward structural source
     data.

136. `136-lct-broad-trace-obstruction.md`
     Bounded internal A6/LT76 result: rejects broad liquid trace-class
     circle packages under doc-105 overreach hypotheses and sharpens
     the live A6 target to LCT-STRICT.

137. `137-hhg-diagnostic-shadow-obstruction.md`
     Bounded internal A3 result: rejects or demotes HH graph/index
     diagnostic-shadow packages and sharpens the live A3 target to
     HHG-STRUCTURAL.

138. `138-meteq-late-factor-obstruction.md`
     Bounded internal S2 result: rejects factor-through or late scale
     insertion metric/equivariant enrichments and sharpens the live S2
     target to METEQ-DETECTED.

139. `139-sharpened-assault-dispatch-packets.md`
     Sendable packet bank for the four sharpened targets:
     PFV2-ADELIC-LOCAL, LCT-STRICT, HHG-STRUCTURAL, and METEQ-DETECTED,
     with a universal landing record.

140. `140-pfv2-structural-source-axiom-audit.md`
     Internal PFV2 source-axiom audit: rejects marked-product and
     marked-monoid versions, leaving UFD/factorization-domain and
     adelic/product-formula source objects as HOLD subfamilies.

141. `141-pfv2-ufd-source-boundary.md`
     Internal PFV2 UFD source audit: demotes bare UFD/factorization
     pairs to source-control partial and creates the intermediate
     PFV2-GLOBAL stage before the adelic-local refinement.

142. `142-pfv2-adelic-source-boundary.md`
     Internal PFV2 adelic source audit: demotes bare all-places
     product-formula bookkeeping and sharpens the live A2 target to
     PFV2-ADELIC-LOCAL.

143. `143-pfv2-adelic-local-source-record.md`
     Smallest honest PFV2-ADELIC-LOCAL source record: accepts
     PFV2_local_record(p,q) only as calibration, isolates
     PFV2-COMP-REFLECT as the decisive complement-reflection theorem,
     and keeps A2 witnesses blocked.

144. `144-lct-strict-src0-record.md`
     Smallest LCT-STRICT source record: names LCT-STRICT-SRC0(alpha)
     as the immediate strict source/first-map target before full trace
     machinery, with LCT-STRICT-REFLECT as the follow-up theorem if
     trace legality and carrier reflection cannot be separated.

145. `145-hhg-source-1-record.md`
     Smallest HHG-STRUCTURAL source record: names HHG-SOURCE-1 as the
     immediate HH_C/kappa_HH source-level target, requiring object
     graph-depth data, control non-formability, and one downstream
     load-bearing slot before any witness.

146. `146-meteq-mintrace-record.md`
     Smallest METEQ-DETECTED trace-detection record: names
     METEQ-MINTRACE as the frozen (O_l,D_l,Tr_l) target and requires a
     deletion theorem before any metric/equivariant witness is
     licensed.

147. `147-pfv2-relative-divisor-complement-shot.md`
     Concrete PFV2-COMP-REFLECT shot: tests the relative
     divisor/idele complement PFV2-REL-DIV(p,q), records local
     complement-structural progress, and sharpens the immediate A2
     theorem target to PFV2-REL-FIRST.

148. `148-pfv2-classical-relative-divisor-obstruction.md`
     Bounded no-go from the doc-147 shot: rejects the ordinary
     classical relative divisor/idele tuple as all-places assembly plus
     p,q marking, leaving PFV2-REL-UPROP as the surviving A2 target.

149. `149-pfv2-formal-relative-uprop-obstruction.md`
     Bounded no-go for formal relative universal properties: rejects
     slice/fiber/pullback/comma-category repairs as marked all-places
     sources, leaving PFV2-REL-REFLECT as the surviving A2 target.

150. `150-pfv2-postglobal-reflector-obstruction.md`
     Bounded no-go for post-global reflectors/localizations/envelopes:
     rejects applying a relative reflector after an all-places source
     already exists, leaving PFV2-REL-DESCENT as the surviving A2
     target.

151. `151-pfv2-preglobal-descent-shot.md`
     Concrete PFV2-REL-DESCENT shot: defines PFV2-DESC(p,q), records
     local source-priority and complement-structural progress, and
     sharpens the active A2 target to PFV2-DESC-SELECT.

152. `152-pfv2-effective-descent-collapse.md`
     Bounded no-go from the PFV2-DESC shot: rejects ordinary effective
     descent presentations equivalent to all-places objects with p,q
     marking, leaving PFV2-DESC-RESIDUAL as the active A2 target.

153. `153-pfv2-residual-descent-source-record.md`
     Concrete PFV2-DESC-RESIDUAL source record: defines
     PFV2-RES(p,q), makes the residual datum rho explicit, and
     sharpens the active A2 target to PFV2-RHO-SELECT.

154. `154-pfv2-rho-marking-collapse.md`
     Bounded no-go from the PFV2-RHO-SELECT target: rejects rho that
     is only p,q marking, complement bookkeeping, or scalar defect
     data, leaving PFV2-RHO-NONTRIVIAL as the active A2 target.

155. `155-pfv2-rho-obstruction-defect-collapse.md`
     Bounded no-go from PFV2-RHO-NONTRIVIAL: rejects obstruction or
     defect rho that vanishes on successful assembly or is only a
     scalar error, leaving PFV2-RHO-SURVIVES as the active A2 target.

156. `156-pfv2-rho-torsor-extension-shot.md`
     Concrete PFV2-RHO-SURVIVES shot: tests torsor/extension/cocycle
     residual data, records local nontrivial-rho progress, and sharpens
     the active A2 target to PFV2-TOR-SELECT.

157. `157-pfv2-torsor-decoration-collapse.md`
     Bounded no-go from PFV2-TOR-SELECT: rejects torsor/extension/
     cocycle residuals that are only gauge, presentation, ordinary
     decoration, automorphism labels, or coherence witnesses, leaving
     PFV2-TOR-NATIVE as the active A2 target.

158. `158-pfv2-native-torsor-source-record.md`
     Concrete PFV2-TOR-NATIVE source record: defines
     PFV2-NATIVE-TOR(p,q) with a carrier-native band/groupoid G_car,
     tau_car, bank_iota, and surv fields, records local native-position
     progress, and sharpens the active A2 target to PFV2-TOR-CARRIER.

159. `159-pfv2-carrier-torsor-formability-collapse.md`
     Bounded no-go from PFV2-TOR-CARRIER: rejects broadly functorial
     carrier-torsor/groupoid packages formable by local-shadow controls,
     leaving PFV2-TOR-EULER-BAND as the active A2 target.

160. `160-pfv2-euler-band-valuation-shot.md`
     Concrete PFV2-TOR-EULER-BAND shot: tests whether the
     product-formula valuation vector can define an Euler band/groupoid
     G_E and torsor tau_E, records local Euler-field placement progress,
     and sharpens the active A2 target to PFV2-EULER-OP.

161. `161-pfv2-linear-pf-operation-collapse.md`
     Bounded no-go from PFV2-EULER-OP: rejects scalar
     product-formula balance, affine-hyperplane, and normalization
     torsor operations as broad/control-formable, leaving
     PFV2-EULER-TOWER-OP as the active A2 target.

162. `162-pfv2-euler-tower-operation-shot.md`
     Concrete PFV2-EULER-TOWER-OP shot: defines
     PFV2-TOWER-OP(p,q), requiring atom, comb, valuation, structural
     length, product-formula, and effectivity fields before assembly,
     and sharpens the active A2 target to PFV2-TOWER-EFFECTIVE.

163. `163-pfv2-effective-tower-marking-collapse.md`
     Bounded no-go from PFV2-TOWER-EFFECTIVE: rejects effective tower
     operations that are only marked monoid data, bare UFD/factorization
     pairs, or independent towers plus a later PF relation, leaving
     PFV2-TOWER-GLOBAL as the active A2 target.

164. `164-pfv2-global-tower-source-shot.md`
     Concrete PFV2-TOWER-GLOBAL shot: defines
     PFV2-GLOBAL-TOWER(p,q), a simultaneous global product-formula
     tower source object, and sharpens the active A2 target to
     PFV2-GLOBAL-PF-AXIOM.

165. `165-pfv2-global-pf-allplaces-collapse.md`
     Bounded no-go from PFV2-GLOBAL-PF-AXIOM: rejects all-places
     adelic/divisor/idele/product-formula sources whose p,q tower data
     are selected after the global object exists, leaving
     PFV2-GPF-LOCAL as the active A2 target.

166. `166-pfv2-gpf-local-source-shot.md`
     Concrete PFV2-GPF-LOCAL shot: defines PFV2-GPF-LOCAL(p,q), a
     p,q+complement global product-formula tower source formed before
     all-places assembly, records local source-priority and complement
     schema progress, and sharpens the active A2 target to
     PFV2-GPF-SELECT.

167. `167-pfv2-gpf-effective-descent-collapse.md`
     Bounded no-go from PFV2-GPF-SELECT: rejects GPF local sources that
     are ordinary effective-descent presentations equivalent to
     all-places objects with p,q marking, leaving PFV2-GPF-RESIDUAL as
     the active A2 target.

168. `168-pfv2-gpf-residual-monodromy-shot.md`
     Concrete PFV2-GPF-RESIDUAL shot: defines
     PFV2-GPF-RMON(p,q), a residual p,q+complement monodromy/action
     class inside the local GPF source, records local residual-source
     schema progress, and sharpens the active A2 target to
     PFV2-GPF-RMON-SELECT as the next deciding theorem.

169. `169-pfv2-gpf-rmon-presentation-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-SELECT: rejects residual
     monodromy/action classes that are only presentation, gauge, or
     coherence data for assembly, leaving PFV2-GPF-RMON-NATIVE as the
     active A2 target.

170. `170-pfv2-gpf-rmon-commutator-shot.md`
     Concrete PFV2-GPF-RMON-NATIVE shot: defines
     PFV2-GPF-RMON-COMM(p,q), a p/q tower commutator or holonomy
     action on the structural complement, records local native-action
     schema progress, and sharpens the active A2 target to
     PFV2-GPF-RMON-COMM-SELECT as the next deciding theorem.

171. `171-pfv2-gpf-rmon-commutator-scalar-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-COMM-SELECT: rejects
     commutator/holonomy classes that are only scalar product-formula
     balance, p,q marking, complement bookkeeping, or abelian
     compatibility, leaving PFV2-GPF-RMON-COMM-NONSCALAR as the active
     A2 target.

172. `172-pfv2-gpf-rmon-filtered-action-shot.md`
     Concrete PFV2-GPF-RMON-COMM-NONSCALAR shot: defines
     PFV2-GPF-RMON-FILT(p,q), a filtered non-scalar p/q action residue
     on the structural complement, records local filtered-residue
     schema progress, and sharpens the active A2 target to
     PFV2-GPF-RMON-FILT-SELECT as the next deciding theorem.

173. `173-pfv2-gpf-rmon-filtration-bookkeeping-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-FILT-SELECT: rejects filtered
     action proposals where the filtration is only degree/order/
     valuation/support bookkeeping determined by scalar/readout data,
     leaving PFV2-GPF-RMON-FILT-STRUCT as the active A2 target.

174. `174-pfv2-gpf-rmon-extension-depth-filtration-shot.md`
     Concrete PFV2-GPF-RMON-FILT-STRUCT shot: defines
     PFV2-GPF-RMON-EXTDEPTH(p,q), an extension-depth filtration on the
     structural complement generated by simultaneous p/q tower action,
     records local extension-depth schema progress, and sharpens the
     active A2 target to PFV2-GPF-RMON-EXTDEPTH-SELECT as the next
     deciding theorem.

175. `175-pfv2-gpf-rmon-passive-extension-depth-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EXTDEPTH-SELECT: rejects
     structural or extension-depth filtrations that are passive
     functorial invariants of the complement or broad filtered local
     category, leaving PFV2-GPF-RMON-EXTDEPTH-ACTIVE as the active A2
     target.

176. `176-pfv2-gpf-rmon-commutator-extension-shot.md`
     Concrete PFV2-GPF-RMON-EXTDEPTH-ACTIVE shot: defines
     PFV2-GPF-RMON-EXTCOMM(p,q), a commutator-extension operator
     Delta_{p,q} whose iterated extension/cone operations generate the
     active filtration, records local commutator-extension schema
     progress, and sharpens the active A2 target to
     PFV2-GPF-RMON-EXTCOMM-SELECT as the next deciding theorem.

177. `177-pfv2-gpf-rmon-formal-ambient-extcomm-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EXTCOMM-SELECT: rejects
     commutator-extension packages where Delta_{p,q} or its
     cones/extensions are supplied by broad ambient additive, stable,
     derived, completed, or traceable-envelope closure, leaving
     PFV2-GPF-RMON-EXTCOMM-NATIVE as the active A2 target.

178. `178-pfv2-gpf-rmon-effectivity-boundary-commutator-shot.md`
     Concrete PFV2-GPF-RMON-EXTCOMM-NATIVE shot: defines
     PFV2-GPF-RMON-EFFCOMM(p,q), an effectivity-boundary commutator
     Delta_{p,q}^{Eff} inside Eff_{p,q}, records local
     effectivity-boundary schema progress, and sharpens the active A2
     target to PFV2-GPF-RMON-EFFCOMM-SELECT as the next deciding
     theorem.

179. `179-pfv2-gpf-rmon-effcomm-descent-coherence-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFCOMM-SELECT: rejects
     effectivity-boundary commutators whose boundary is only
     effective-descent coherence, assembly gauge, or compatibility
     bookkeeping, leaving PFV2-GPF-RMON-EFFCOMM-RESIDUAL as the active
     A2 target.

180. `180-pfv2-gpf-rmon-effcomm-residual-fiber-shot.md`
     Concrete PFV2-GPF-RMON-EFFCOMM-RESIDUAL shot: defines
     PFV2-GPF-RMON-EFFFIBER(p,q), a fixed-readout residual fiber
     Fib_Eff^{res}(Read_{desc}) for effectivity-boundary commutator
     data, records local residual-fiber schema progress, and sharpens
     the active A2 target to PFV2-GPF-RMON-EFFFIBER-SELECT as the next
     deciding theorem.

181. `181-pfv2-gpf-rmon-efffiber-trivial-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFFIBER-SELECT: rejects
     fixed-readout residual fibers that are empty, singleton,
     contractible, or forced to the descent-coherent/readout-determined
     point, leaving PFV2-GPF-RMON-EFFFIBER-NONTRIVIAL or another
     nontrivial fixed-readout residual source as the active A2 target.

182. `182-pfv2-gpf-rmon-efffiber-pair-shot.md`
     Concrete PFV2-GPF-RMON-EFFFIBER-NONTRIVIAL shot: defines
     PFV2-GPF-RMON-EFFPAIR(p,q), a same-readout pair
     rho_G^{fib,0}, rho_G^{fib,1} with fiber-internal difference
     delta_rho_G^{fib}, records local residual-pair schema progress,
     and sharpens the active A2 target to
     PFV2-GPF-RMON-EFFPAIR-SELECT as the next deciding theorem.

183. `183-pfv2-gpf-rmon-effpair-identification-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFPAIR-SELECT: rejects
     same-readout residual pairs whose two classes are identified by
     descent/readout/shadow equivalence before first-map use, leaving
     PFV2-GPF-RMON-EFFPAIR-SEPARATED as the active A2 target.

184. `184-pfv2-gpf-rmon-effpair-separator-shot.md`
     Concrete PFV2-GPF-RMON-EFFPAIR-SEPARATED shot: defines
     PFV2-GPF-RMON-EFFSEP(p,q), a same-readout residual pair equipped
     with a fiber-internal separator sep_G^{fib}, records local
     separator schema progress, and sharpens the active A2 target to
     PFV2-GPF-RMON-EFFSEP-SELECT as the next deciding theorem.

185. `185-pfv2-gpf-rmon-effsep-external-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-SELECT: rejects
     separators that distinguish only after changing readout, choosing
     representatives, passing through bookkeeping/shadows, or using
     downstream diagnostics, leaving PFV2-GPF-RMON-EFFSEP-INTERNAL as
     the active A2 target.

186. `186-pfv2-gpf-rmon-effsep-control-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-INTERNAL: rejects
     internal separators whose defining rule is still available to
     Epstein/DH controls while theta/count shadows remain meaningful,
     leaving PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED as the active A2
     target.

187. `187-pfv2-gpf-rmon-effsep-bank-replacement-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-CONTROL-EXCLUDED:
     rejects separator sources that replace or erase the B0_p/B0_q
     banks, leaving PFV2-GPF-RMON-EFFSEP-BANKED as the active A2
     target.

188. `188-pfv2-gpf-rmon-effsep-downstream-erasure-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-BANKED: rejects
     separators erased before M_C/F_C/Tr_L or the strict trace
     interface, leaving PFV2-GPF-RMON-EFFSEP-LOADBEARING as the active
     A2 target.

189. `189-pfv2-gpf-rmon-effsep-downstream-load-shot.md`
     Concrete PFV2-GPF-RMON-EFFSEP-LOADBEARING shot: defines
     PFV2-GPF-RMON-EFFSEP-DLOAD(p,q), a first downstream load slot
     DLoad_G^{sep} receiving sep_G^{fib} or delta_rho_G^{fib}, records
     local downstream-load schema progress, and sharpens the active A2
     target to PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT as the next deciding
     theorem.

190. `190-pfv2-gpf-rmon-effsep-dload-insensitive-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-SELECT: rejects
     downstream load slots unchanged by changing sep_G^{fib} or
     delta_rho_G^{fib}, leaving
     PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE as the then-active A2 target.

191. `191-pfv2-gpf-rmon-effsep-dload-forgetful-route-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-SENSITIVE: rejects
     separator-sensitive DLoad_G^{sep} slots whose only trace-legal
     route to M_C/F_C/Tr_L forgets sep_G^{fib} or delta_rho_G^{fib},
     leaving PFV2-GPF-RMON-EFFSEP-DLOAD-NONFORGETFUL as the then-active
     A2 target.

192. `192-pfv2-gpf-rmon-effsep-dload-sidecar-route-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-NONFORGETFUL:
     rejects nonforgetful routes that preserve sep_G^{fib} or
     delta_rho_G^{fib} only as unconsumed sidecar data, leaving
     PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED as the then-active A2 target.

193. `193-pfv2-gpf-rmon-effsep-dload-split-consumption-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-CONSUMED: rejects
     first separator-consuming trace-facing operations that split into
     independent p-bank and q-bank consumers, leaving
     PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED as the then-active A2
     target.

194. `194-pfv2-gpf-rmon-effsep-dload-mixed-control-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-CONSUMED:
     rejects mixed p/q separator-consuming operations that are still
     formable for Epstein/DH or broad shadow controls, leaving
     PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE as the then-active A2
     target.

195. `195-pfv2-gpf-rmon-effsep-dload-free-trace-codomain-collapse.md`
     Bounded no-go from PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE:
     rejects mixed carrier-selective consumers whose trace codomain,
     trace wrapper, determinant target, or regularized value is
     supplied externally, leaving
     PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-NATIVE as the
     then-active A2 target.

196. `196-pfv2-gpf-rmon-effsep-dload-native-trace-insensitive-collapse.md`
     Bounded no-go from
     PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-NATIVE: rejects
     native trace interfaces whose actual trace value, determinant,
     kernel, regularized value, or comparison output is unchanged by
     sep_G^{fib} or delta_rho_G^{fib}, leaving
     PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-SENSITIVE as the
     active A2 target.

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
