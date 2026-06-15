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
    why docs 129-196 (the deleted "assault" era) produced nothing, and
    bans re-entry. The only doc permitted to name the dead lineage.
```

## Witnesses

`scripts/numerics/witness/` holds ~200 fail-closed witnesses, each run
via `python3 -m scripts.numerics.witness.<name>` (exit 0 = the recorded
claim reproduces; stack: python-flint ball arithmetic, numpy). Key
witnesses are cited inline in the docs they certify.
