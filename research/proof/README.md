# Prime-Toeplitz proof scaffold

This directory is the theorem/proof track. The goal is to keep the
proof attempt separate from numerical diagnostics while preserving the
conventions those diagnostics fixed.

Operating mode (fixed in the 2026-06-14 reset, doc 129):
**numerics + no-go theorems + sharp narrowing**. Every cycle ships a
certified numerical witness OR a no-go theorem with a named mechanism.
A schema with no witness is not a document.

## Objective

Prove the pole-killed Prime-Toeplitz domination theorem `P_Euler <=
W_infty` on the Sonin support filtration. In the L2-orthogonal splitting
`H_R = H_L + shell`, with `M_R = [[A, C],[C*, D]]`, the load-bearing
target is the Schur inequality `C* A^{-1} C <= D`.

## Discipline checks

```bash
python3 scripts/automation/check_proof_targets.py   # discipline guard
python3 scripts/automation/check_frontier_map.py     # structured frontier map guard
scripts/automation/guard.sh                          # full commit guard
```

The discipline guard (rewritten in the reset) enforces three things via
`target-ledger.json`: the no-go bank docs exist and are titled; the
navigation docs agree on the restored front; and the dead
construction-naming lineage stays QUARANTINED to the doc-129 autopsy
(the banned token and the long-hyphenated regress signature may not
reappear in any other proof doc). See doc 129 for why.

## Index

### The tracking arc (00-16)

```text
00  reduction nested-target => RH (CC20 + Weil converse; O1-O4)
00a O3 converse: off-line zero forces a negative admissible test
01  Sonin/Schur scaffold; closed filtration; shift-invariance lemma
02  exact Euler/Chebyshev transgression identity
03  Schur first-variation; critical/boundary stress kernels
04  storage/Riccati target; exact-minus-smooth sign convention
05  finite Schur-complement update identity; the negative Riccati square
06  proof outline + formalization markers
07  active-debt geometric lemma; edge-profile convolution
08  default T1 certificate (Sylvester/interval, 2D shell)
09  R1 inverse analysis: exponential margin decay kills slack estimates;
    cluster obstruction; window dial (short-interval PNT at 7/12)
10  realization spec (passive prime-side; E1-E4, graveyard G1-G6)
11  edge-window factorization; exact edge-convolution identity (PROVEN)
12  edge-compliance reduction; the tracking form (DERIVED, val 2e-5)
13  TRACKING EQUIVALENCE: RH <=> uniform tau < 1 (terminal; DH fails)
14  fork protocol (F1/F2/F3, P1/P2)
15  second-description spec (S1-S5)
16  R-SQ doubled lab: two-variable conservation; the trichotomy
```

### The R-INT arc (17-40)

```text
17  count-fingerprint pipeline; self-duality = FE as count duality; Hall
18  derived square = THH(Z); <Delta,Delta> = zeta'(0); wall = PROPERNESS
19  C5: THH count ladders ARE the EF supply side; von Mangoldt = THH(F_p)
20  Tate-ladder self-dual [CORRECTED]: KMS-1/2 is a scheme datum
21  fleet synthesis; ku ladder; CC proven integer RR; gate G-INT6
22  genus audit: CC-vs-THH clash is invariant-level
23  Adams family signature (fail-closed negative)
24  reflection fold: archimedean fold on C_2 fixed points; parity lemma
25  p=2 anomaly computed (THR(F_2)^{tC_2} closed form; Barnes Gamma_2)
26-31 cycle syntheses: monoid + compactify; PFD spec + line closure
32-37 index attack + face/stress rounds (unit insertion, slot-data demotions)
38-40 strategic charter: OC1-OC4 + BC13 + BC-E3'; the liquid address/type
```

### The spec + construction + external branches (41-50)

```text
41  testable normal form (M-C/M-A/M-B)
42  M-C carrier classification (no carrier passes BC-E3'/BC13)
43  M-A self-dual LP audit (Hermite unit flips the deep cell)
44  M-B g2 exhaustion boundary (NN kills the strict-square proxy)
45  THE SPEC, final form (candidate package, clauses, residue, checklist)
46  construction blueprint (liquid index carrier; restricts to B0)
47  external scoping questions (field-native)
48  negative-theorem targets
49  B0 Tate-RR calibration (witness; calibration floor, not the carrier)
50  external falsification packets (sendable)
```

### The no-go bank (51-70) - the primary product

```text
51 scale-blind localizing trace     52 transport/self-supplied 2nd eval
53 carrier-blind Poisson/Epstein    54 B1 admission gate
55 one-place/inserted unit          56 strict-face positivity
57 p-complete archimedean blindness 58 max-Gram/signature insufficiency
59 zero-import circularity          60 G60 gate stack + escape profile
61 external answer ledger           62 scale-blind citation audit
63 scale-blind diagram lemma        64 Epstein carrier guard lemma
65 P3 independence normal form      66 unit-covariance/threading lemma
67 BC13 exhaustion normal form      68 archimedean escape normal form
69 zero-free freeze normal form     70 Gram diagnostic normal form
```

### No-go survivors kept from the deleted 71-128 band

```text
74  generic-kernel carrier blindness   79  side-block archimedean
80  late scale insertion               82  factor-through scale collapse
85  trace-detection required           93  free-weight kernel
97  monoid-functorial carrier overreach 100 mixed-object shadow enlargement
107 carrier-overreach meta-lemma       108 carrier-overreach proof skeleton
109 strict-first-map relabeling        111 strict-prefix erasure
112 late carrier reintroduction        118 traceable-envelope collapse
125 decorated-envelope reflection
```

### The reset

```text
129 autopsy + standing no-go: the construction-naming regress. Records
    why the deleted candidate-driven "assault" era produced nothing, and
    bans re-entry. The only doc permitted to name the dead lineage.
130-653 post-reset construction/no-go cycles: analytic faces closed,
    End(S^2/Z) construction arc opened, R1 sharpened by the Weyl-shear
    H^1 obstruction (138), the N1-b' full-line support no-go (139),
    the bottom-class nilpotence no-go (140), and the dlog normalization
    no-go (141), the bottom-class localization collapse no-go (142), and
    the free Laurent insertion no-go (143), and the projection-choice no-go
    (144), the torsor-splitter insertion no-go (145), and the
    quotient-to-line no-go (146), the shift-coinvariant line no-go (147),
    the shift-telescope no-go (148), and the formal shift-operator no-go
    (149), the endomorphism-envelope no-go (150), and the idempotent-corner
    no-go (151), the trace-minimal-idempotent no-go (152), and the
    conjugacy-invariant-idempotent no-go (153), and the support-flag
    idempotent no-go (154), the incidence-path-algebra no-go (155), and
    the groupoid-completion no-go (156), and the stabilizer-loop no-go
    (157), the connection-holonomy no-go (158), and the Rees-filtration
    no-go (159), the Rees-monodromy no-go (160), the filtered-extension
    no-go (161), the derived-extension no-go (162), the pro-support
    completion no-go (163), the Tate-dual completion no-go (164), and the
    evaluation-boundary-glue no-go (165), the hyperbolic-swap no-go (166),
    the Lagrangian-polarization no-go (167), the opposite-Lagrangian graph
    no-go (168), the graph-boundary extraction no-go (169), the
    orientation-normalization no-go (170), the quadratic-refinement no-go
    (171), the Darboux-frame no-go (172), the symplectic-quotient no-go
    (173), the symplectic-stabilizer-stack no-go (174), the
    symplectic-stabilizer-cohomology no-go (175), the
    symplectic-building-Steinberg no-go (176), the finite
    Weyl-Coxeter-apartment monodromy no-go (177), the finite
    Hecke-Iwahori double-coset algebra no-go (178), the affine
    Weyl-Hecke translation lattice no-go (179), the affine
    Grassmannian-Schubert-convolution no-go (180), the geometric
    Satake dual-representation no-go (181), the principal
    cocharacter no-go (182), the Kostant-section no-go (183), and the
    Springer-Steinberg no-go (184), the Hitchin-cameral no-go (185), the
    Hitchin Picard-Prym no-go (186), the CC Pic/Jacobian square no-go
    (187), the CC strict-square divided-power no-go (188), and the
    CC graded-tolerance no-go (189), the CC finite-part
    renormalization no-go (190), the CC non-geometric exactness
    selector no-go (191), the CC cutoff-aggregation no-go (192), and
    the CC strict-bar-grading no-go (193), and the CC naive
    tolerant-smash no-go (194), and the CC norm-filtration no-go (195),
    and the derived THH diagonal no-go (196), the ku square /
    Adams-shadow no-go (197), the monoid Frobenius shadow no-go (198),
    the real-cyclotomic negation no-go (199), the lambda-half cover
    no-go (200), the static product surface no-go (201), the
    archimedean family residue-field no-go (202), the named F1
    constant-tower no-go (203), the regularized determinant radius
    no-go (204), the type II_1 trace no-go (205), the
    single-Frobenius recoupling no-go (206), the
    Frobenius-first Tannakian compactness no-go (207), the
    local purity-carrier no-go (208), the radius-descent assembly
    no-go (209), the Rosati self-degree no-go (210), the NS square
    anchor/spec (211), the diagonal-trace graph no-go (212), the
    finite-trace realization no-go (213), the isospectral graph-carrier
    no-go (214), the integral q-similitude graph no-go (215), the
    unitary-projection graph no-go (216), the cyclic graph-algebra no-go
    (217), the formal NS-envelope no-go (218), the formal
    correspondence-composition no-go (219), the formal adjoint/projection
    no-go (220), the projection-formula quotient no-go (221), the
    presented correspondence-carrier no-go (222), the numerical/GNS
    quotient no-go (223), the Karoubi-semisimple completion no-go (224),
    the perfect-Morita-envelope no-go (225), the smooth-proper
    CY-Mukai no-go (226), the NC-Hodge realization no-go (227), the
    Weil-standard package no-go (228), the six-functor trace no-go (229),
    the prismatic-syntomic package no-go (230), the adelic
    restricted-product assembly no-go (231), the automorphic
    trace-formula packet no-go (232), the Galois compatible-system
    no-go (233), the Tate fixed-subspace no-go (234), the
    CM-Shimura carrier no-go (235), the Chow-Hilbert cycle-moduli
    no-go (236), the derived cycle-stack no-go (237), the
    bivariant-operational Chow no-go (238), the motivic-cohomology
    regulator no-go (239), the triangulated-motives carrier no-go (240),
    the condensed-liquid analytic carrier no-go (241), the
    perfectoid-diamond FF-curve no-go (242), the Arakelov arithmetic
    intersection no-go (243), the Bost-Connes / adele-class spectral
    no-go (244), the operator K-theory / KK assembly no-go (245), the
    algebraic K-theory / cyclotomic trace no-go (246), the
    Weil-etale / L-function special-value no-go (247), the
    epicyclic Frobenius-lift no-go (248), the Witt/Lambda/delta-ring
    no-go (249), the Tambara/Mackey norm-transfer no-go (250), the
    anabelian fundamental-group no-go (251), the span/profunctor
    bicategory no-go (252), the topos/hyperdescent shape no-go (253), the
    shtuka/Hecke-stack no-go (254), the relative-trace/period no-go
    (255), the square-carrier contract/spec (256), the DD.4/SCC
    interface spec (257), the coinduced-DD.4-extension no-go (258), the
    bar-resolution-boundary no-go (259), the mapping-cone-nullhomotopy
    no-go (260), the jet-deletion no-go (261), the obstruction-quotient
    no-go (262), the norm-one-Hilbert90 no-go (263), the
    Frobenius-root-extension no-go (264), the perfection-colimit no-go
    (265), the root-shift-telescope no-go (266), the
    Laurent-field-Hilbert90 no-go (267), the valuation-parity-cover no-go
    (268), the valuation-degree-character no-go (269), the degree-pair-codec
    no-go (270), the endpoint-valuation-register no-go (271), the
    endpoint-swap-boundary no-go (272), the oriented-endpoint-difference
    no-go (273), the endpoint-parity-saturation no-go (274), the
    endpoint-parity-tag no-go (275), the carrier-first categorical
    square contract/spec (276), the Cartier-boundary-normal no-go (277),
    the oriented-boundary-complex no-go (278), the boundary-even-lattice
    no-go (279), the hyperbolic-plane/Rosati no-go (280), the
    trace-augmented-hyperbolic no-go (281), the
    End-augmented-hyperbolic no-go (282), the
    positive-Rosati-End-envelope no-go (283), the
    projection-forced-positive-envelope no-go (284), the
    fiber-product-saturated-positive-envelope no-go (285), the
    Qbar-shell-positive-envelope no-go (286), the
    represented-carrier gate contract/spec (287), the
    represented-carrier candidate-matrix no-go (288), the
    CC-product-boundary-endpoint-bundle no-go (289), the
    CC-product-repNS-graft no-go (290), the
    CC-product-square-cycle-category no-go (291), the
    CC-product-square-cycle-exact-completion no-go (292), the
    CC-product-square-cycle-descent-stack no-go (293), the
    CC-product-square-cycle-hyperdescent no-go (294), the
    CC-product-square-cycle-moduli-stack no-go (295), the
    CC-product-square-cycle-Yoneda-functor no-go (296), the
    CC-product-square-cycle-reflective-completion no-go (297), the
    CC-product-square-cycle-pro-representable-limit no-go (298), the
    CC-product-square-cycle-Artin-representability no-go (299), the
    CC-product-square-cycle-Tannakian-reconstruction no-go (300), the
    CC-product-square-cycle-universal-property-recognition no-go (301), the
    CC-product-square-cycle-equivalence-univalence no-go (302), the
    CC-product-square-cycle-contractible-choice-space no-go (303), the
    CC-product-square-cycle-homotopy-quotient no-go (304), the
    CC-product-square-cycle-Rezk-completion no-go (305), the
    CC-product-square-cycle-model-replacement no-go (306), the
    CC-product-square-cycle-Bousfield-localization no-go (307), the
    missing-object frontier / Qbar_BECD spec (308), the Qbar_BECD
    Phase-A sieve/spec (309), the Qbar_BECD endpoint-fixed boundary
    sieve/spec (310), the Qbar_BECD boundary-source matrix/spec (311), the
    Qbar_BECD oriented-Cartier boundary contract/spec (312), the
    Qbar_BECD oriented-Cartier residual sieve/spec (313), the
    Qbar_BECD boundary self-duality interface/spec (314), the
    Qbar_BECD boundary-defect duality contract/spec (315), the
    Qbar_BECD boundary twist-pinning contract/spec (316), the
    Qbar_BECD boundary component anchor contract/spec (317), the
    Qbar_BECD boundary fiber anchor contract/spec (318), the
    Qbar_BECD boundary fiber localization contract/spec (319), the
    Qbar_BECD boundary pushforward compatibility contract/spec (320), the
    Qbar_BECD formation-level control death contract/spec (321), the
    Qbar_BECD joint formation coupling contract/spec (322), the
    Qbar_BECD effectivity-domain first-generator contract/spec (323), the
    Qbar_BECD internal effectivity-domain contract/spec (324), the
    Qbar_BECD effectivity first-generator orientation contract/spec (325),
    the Qbar_BECD strict-square effectivity extraction contract/spec (326),
    the Qbar_BECD strict-square character-stratum functor contract/spec
    (327), the Qbar_BECD strict-square signed-character effectivity
    contract/spec (328), the Qbar_BECD strict-square boundary-cancellation
    contract/spec (329), the Qbar_BECD strict-square boundary-convolution
    module contract/spec (330), the Qbar_BECD strict-square
    boundary-stratum product contract/spec (331), the Qbar_BECD
    strict-square product internal-effectivity image contract/spec (332),
    the Qbar_BECD strict-square product mixed-support subtower
    contract/spec (333), the Qbar_BECD strict-square product
    mixed-support orbit-closure contract/spec (334), and the Qbar_BECD
    strict-square product multiplier-transport composition contract/spec
    (335), the Qbar_BECD strict-square product multiplier DD.4 naturality
    contract/spec (336), the Qbar_BECD strict-square product multiplier
    endpoint-degree naturality contract/spec (337), the Qbar_BECD
    strict-square product multiplier pushforward naturality contract/spec
    (338), the Qbar_BECD strict-square product multiplier graph/Rosati/count
    naturality contract/spec (339), the Qbar_BECD strict-square product
    multiplier control-death naturality contract/spec (340), and the
    Qbar_BECD strict-square product multiplier source-typed formation-gate
    contract/spec (341), and the Qbar_BECD strict-square product multiplier
    represented source-fiber contract/spec (342), and the Qbar_BECD
    strict-square product multiplier cartesian-coherence contract/spec (343),
    and the Qbar_BECD strict-square product multiplier square-layer coherence
    contract/spec (344), and the Qbar_BECD strict-square product multiplier
    monoidwide square-layer coherence contract/spec (345), and the
    Qbar_BECD strict-square product multiplier monoidwide DD.4
    boundary-certificate contract/spec (346), and the Qbar_BECD
    strict-square product multiplier boundary-certificate cancellation-module
    contract/spec (347), and the Qbar_BECD strict-square product multiplier
    boundary-certificate exact-naturality contract/spec (348), and the
    Qbar_BECD strict-square product multiplier boundary-certificate
    exact-source self-duality contract/spec (349), and the Qbar_BECD
    strict-square product multiplier self-dual exact-source formation-gate
    contract/spec (350), the Qbar_BECD strict-square product multiplier
    self-dual exact-source formation-coherence contract/spec (351), the
    Qbar_BECD strict-square product multiplier self-dual exact-source
    coherence-coupling contract/spec (352), and the Qbar_BECD strict-square
    product multiplier self-dual exact-source coherence-coupling
    representability contract/spec (353), and the Qbar_BECD strict-square
    product multiplier self-dual exact-source coherence-coupling
    subrepresenter contract/spec (354), and the Qbar_BECD strict-square
    product multiplier self-dual exact-source coherence-coupling
    subrepresenter finite-limit contract/spec (355), and the Qbar_BECD
    strict-square product multiplier self-dual exact-source coherence-coupling
    subrepresenter constraint-morphism contract/spec (356), and the Qbar_BECD
    strict-square product multiplier self-dual exact-source coherence-coupling
    subrepresenter constraint-product contract/spec (357), and the Qbar_BECD
    strict-square product multiplier self-dual exact-source coherence-coupling
    subrepresenter constraint-component contract/spec (358), and the
    Qbar_BECD strict-square product multiplier self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone contract/spec
    (359), and the Qbar_BECD strict-square product multiplier self-dual
    exact-source coherence-coupling subrepresenter constraint-component-cone
    cartesian contract/spec (360), and the Qbar_BECD strict-square product
    multiplier self-dual exact-source coherence-coupling subrepresenter
    constraint-component-cone cartesian-coherence contract/spec (361), and the
    Qbar_BECD strict-square product multiplier self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone
    cartesian-coherence globular-modification contract/spec (362), and the
    Qbar_BECD strict-square product multiplier self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone
    cartesian-coherence globular-modification boundary-fiber contract/spec
    (363), and the Qbar_BECD strict-square product multiplier self-dual
    exact-source coherence-coupling subrepresenter constraint-component-cone
    cartesian-coherence globular-modification boundary-fiber cartesian
    contract/spec (364), and the Qbar_BECD strict-square product multiplier
    self-dual exact-source coherence-coupling subrepresenter
    constraint-component-cone cartesian-coherence globular-modification
    boundary-fiber cartesian-coherence contract/spec (365), and the
    Qbar_BECD strict-square product multiplier self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone
    cartesian-coherence globular-modification boundary-fiber
    cartesian-coherence globular-modification contract/spec (366), and the
    Qbar_BECD strict-square product multiplier self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone
    cartesian-coherence globular-modification boundary-fiber
    cartesian-coherence globular-modification boundary-fiber contract/spec
    (367), and the Qbar_BECD strict-square product multiplier self-dual
    exact-source coherence-coupling subrepresenter constraint-component-cone
    cartesian-coherence globular-modification boundary-fiber
    cartesian-coherence globular-modification boundary-fiber cartesian
    contract/spec (368), and the Qbar_BECD categorical closure self-dual
    exact-source coherence-coupling subrepresenter finite-limit totalization
    contract/spec (469), and the Qbar_BECD categorical closure self-dual
    exact-source coherence-coupling subrepresenter constraint-morphism
    totalization contract/spec (470), and the Qbar_BECD categorical closure
    self-dual exact-source coherence-coupling subrepresenter
    constraint-product totalization contract/spec (471), the Qbar_BECD
    categorical closure self-dual exact-source coherence-coupling
    subrepresenter constraint-component totalization contract/spec (472), and
    the Qbar_BECD categorical closure self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone totalization
    contract/spec (473), and the Qbar_BECD categorical closure self-dual
    exact-source coherence-coupling subrepresenter constraint-component-cone
    cartesian totalization contract/spec (474), and the Qbar_BECD categorical
    closure self-dual exact-source coherence-coupling subrepresenter
    constraint-component-cone cartesian-coherence totalization contract/spec
    (475), and the Qbar_BECD categorical closure self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone cartesian-
    coherence globular-modification totalization contract/spec (476), and the
    Qbar_BECD categorical closure self-dual exact-source coherence-coupling
    subrepresenter constraint-component-cone cartesian-coherence
    globular-modification boundary-fiber totalization contract/spec (477),
    and the Qbar_BECD categorical closure self-dual exact-source
    coherence-coupling subrepresenter constraint-component-cone cartesian-
    coherence globular-modification boundary-fiber cartesian totalization
    contract/spec (478), and the Qbar_BECD categorical closure self-dual
    exact-source coherence-coupling subrepresenter constraint-component-cone
    cartesian-coherence globular-modification boundary-fiber
    cartesian-coherence totalization contract/spec (479), and the Qbar_BECD
    categorical closure self-dual exact-source coherence-coupling
    subrepresenter constraint-component-cone cartesian-coherence
    globular-modification boundary-fiber cartesian-coherence
    globular-modification totalization contract/spec (480), and the
    Qbar_BECD categorical closure finite coherent source-presentation
    totalization contract/spec (481), and the Qbar_BECD categorical closure
    coherent source-presentation finite-limit realization contract/spec
    (482), and the Qbar_BECD categorical closure coherent source-presentation
    eta-factorization contract/spec (483), and the Qbar_BECD categorical
    closure coherent source-presentation eta-lift universal-cone
    contract/spec (484), and the Qbar_BECD categorical closure coherent
    source-presentation eta-lift cartesian universal-cone contract/spec
    (485), and the Qbar_BECD categorical closure coherent source-presentation
    eta-lift cartesian-coherence contract/spec (486), and the Qbar_BECD
    categorical closure coherent source-presentation eta-lift cartesian-
    coherence globular-modification contract/spec (487), and the Qbar_BECD
    categorical closure coherent source-presentation eta-lift cartesian-
    coherence globular-modification boundary-fiber contract/spec (488), and
    the Qbar_BECD categorical closure coherent source-presentation eta-lift
    cartesian-coherence globular-modification boundary-fiber cartesian
    contract/spec (489), and the Qbar_BECD categorical closure coherent
    source-presentation eta-lift cartesian-coherence globular-modification
    boundary-fiber cartesian-coherence contract/spec (490), and the
    Qbar_BECD categorical closure coherent source-presentation eta-lift
    cartesian-coherence globular-modification boundary-fiber cartesian-
    coherence globular-modification contract/spec (491), and the Qbar_BECD
    categorical closure coherent source-presentation eta-lift cartesian-
    coherence globular-modification boundary-fiber cartesian-coherence
    globular-modification finite-index closure contract/spec (492), and the
    Qbar_BECD categorical closure coherent source-presentation eta-lift
    cartesian-coherence globular-modification boundary-fiber cartesian-
    coherence globular-modification finite-index equalizer-idempotent
    contract/spec (493), and the Qbar_BECD categorical closure coherent
    source-presentation eta-lift cartesian-coherence globular-modification
    boundary-fiber cartesian-coherence globular-modification finite-index
    equalizer-idempotent monic-cancellation contract/spec (494), and the
    Qbar_BECD categorical closure coherent source-presentation eta-lift
    cartesian-coherence globular-modification boundary-fiber cartesian-
    coherence globular-modification finite-index equalizer-identity
    universal-mediator contract/spec (495), and the Qbar_BECD categorical
    closure coherent source-presentation eta-lift cartesian-coherence
    globular-modification boundary-fiber cartesian-coherence globular-
    modification finite-index equalizer-identity universal-mediator
    multiplier-naturality contract/spec (496), and the Qbar_BECD categorical
    closure coherent source-presentation eta-lift cartesian-coherence
    globular-modification boundary-fiber cartesian-coherence globular-
    modification finite-index equalizer-identity universal-mediator
    DD.4-certificate contract/spec (497), and the Qbar_BECD categorical
    closure coherent source-presentation eta-lift cartesian-coherence
    globular-modification boundary-fiber cartesian-coherence globular-
    modification finite-index equalizer-identity universal-mediator exact-
    BCF-certificate contract/spec (498), and the Qbar_BECD categorical
    closure coherent source-presentation eta-lift cartesian-coherence
    globular-modification boundary-fiber cartesian-coherence globular-
    modification finite-index equalizer-identity universal-mediator self-dual
    exact-BCF-certificate contract/spec (499), and the Qbar_BECD categorical
    closure coherent source-presentation eta-lift cartesian-coherence
    globular-modification boundary-fiber cartesian-coherence globular-
    modification finite-index equalizer-identity universal-mediator
    formation-gated self-dual exact-BCF-certificate contract/spec (500), and
    the Qbar_BECD categorical closure coherent source-presentation eta-lift
    cartesian-coherence globular-modification boundary-fiber cartesian-
    coherence globular-modification finite-index equalizer-identity
    universal-mediator formation-coherent self-dual exact-BCF-certificate
    contract/spec (501).
```

## Witnesses

`scripts/numerics/witness/` holds ~200 fail-closed witnesses, each run
via `python3 -m scripts.numerics.witness.<name>` (exit 0 = the recorded
claim reproduces; stack: python-flint ball arithmetic, numpy). Key
witnesses are cited inline in the docs they certify.
