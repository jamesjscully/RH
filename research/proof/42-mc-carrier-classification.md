# 42 - M-C carrier classification against BC-E3'

Status: 2026-06-11. First-pass execution of doc 40/41 move M-C over
the carrier families promoted in docs 17-41 and their worker records.
This is a classification of banked evidence, not a new computation.

## 1. Gate

The decision gate is doc 41's BC-E3' plus BC13:

```text
BC-E3'
  nonempty odd determinant/cohomological/spectral slot whose
  eigenvalues are not definitionally supplied by the acting
  map/correspondence.

BC13
  forced-nonnegative index/Gram/count values, and class/scale
  exhaustion of the doc-00 core / Frobenius-graph cone.
```

Verdict labels used below:

```text
EMPTY            odd slot absent.
SELF-SUPPLIED    odd slot present, but eigenvalues are the acting
                 map's own degree/input.
TRANSPORT        two presentations are one evaluation by natural
                 isomorphism, Poisson, coker=det, or regularization.
STRICT-FACE      positivity/effectivity is certified only on a strict
                 family or scanned face, not the full graph cone.
SLOT-DATA        depends on the inserted unit/test slot; not object data.
CARRIER-BLIND    runs on Epstein/DH or discriminates only after an
                 EF-derived computation.
ADDRESS-ONLY     localizes where the object must live, but is not yet
                 a constructed carrier.
SURVIVOR         passes BC-E3' and BC13 at decision grade.
```

## 2. Classification Table

```text
carrier / family                         verdict                 source / decisive reason
---------------------------------------- ----------------------- ---------------------------------------------
Finite-field Quillen / K(F_q)             EMPTY + SELF-SUPPLIED   YY rows 9-10; W 1.3. Two-eval embryo
                                                                   q^w - 1 exists, but zeta(F_q,s) has no
                                                                   zeros and TP_odd(F_q)=0; Adams eigenvalue
                                                                   q^w is forced supply data.

TP/TR/Witt at F_p                         TRANSPORT / EMPTY       YY 3.2; W 1.4. TR_0(A;p)=W(A) is a
                                                                   natural isomorphism; at F_p Frobenius on
                                                                   W(F_p)=Z_p is identity. TC/TP has the
                                                                   point-case empty odd slot.

Cyclotomic Frobenius carrier              SELF-SUPPLIED / BLOCKED W 1.1-1.6. The graph lives in CycSp/TC,
                                                                   not bimodules; F_q works only after iota,
                                                                   while the Spec Z square has p-completeness,
                                                                   semilinearity, and no-iota blockers.

Solenoid S_p = (Q_p x R)/Z[1/p]           SELF-SUPPLIED           ZZ sec 5; doc 40. H^1(S_p)=Z[1/p] is a
                                                                   nonempty odd slot, but the eigenvalue is
                                                                   multiplication-by-p's own degree; the
                                                                   agreement is Pontryagin/inverse-limit
                                                                   transport.

Bare circle / Shv(R/(log p)Z)             ADDRESS-FAIL            XX T1. Localizing invariants of bare sheaf
                                                                   categories see only S^1 / homotopy data and
                                                                   are scale-blind; log p must live in enriched
                                                                   coefficients, analytic rings, equivariance,
                                                                   or kernels.

Anderson dual I_Z on banked spectra       ADDRESS-ONLY            JJ AJ1-AJ3. THH(Z) has a rank-one rational
                                                                   layer, but mod-p/Xbar towers have I_Q=0 and
                                                                   the rational layer place-splits only through
                                                                   A_f; the archimedean R slot is absent.

Strict square theta/vdGS h^0              STRICT-FACE             JJ AJ4-AJ7; doc 33. Effectivity fires and
                                                                   Epstein dies at effectivity, but genuinely
                                                                   square twists have divergent duals; the
                                                                   square-level RR dual is the missing object.

LL strict-family dual unit                STRICT-FACE / SLOT-DATA doc 34; AC. With hand-inserted unit the
                                                                   strict-family inequality is posable and
                                                                   repairs with zero slack, but extension to
                                                                   Frobenius-graph classes is exactly the gap.

Frobenius-graph / max-Gram face           STRICT-FACE             HH; NN; docs 35,37. Lambda(p^k) =
                                                                   -<d_k,d_k> homes the prime side, but the
                                                                   defect is W_infty and graph-class extension
                                                                   fails recurrently; no forced-positive
                                                                   second evaluation spans the full cone.

ku face / two-coset comb                  TRANSPORT + STRICT-FACE SS; UU; docs 36-37. Best banked supply
                                                                   structure: all-(q,a) theorem, carrier guard
                                                                   iff prime powers, depth wall exact. But every
                                                                   entry has one evaluation; the independent
                                                                   spectral evaluation is missing.

2D ku Castelnuovo posing                  TRANSPORT / STRICT-FACE UU. Hodge-index shape is posing-dependent
                                                                   and supply-grade; discriminant entries are
                                                                   congruence/entry-determined. The Weil
                                                                   fixed-point slot is occupied by Lambda-m+,
                                                                   not an independent spectral count.

THR(F_2) Tate square / p=2 anomaly        SELF-SUPPLIED / BLOCKED U; docs 24-26. It supplies 2-primary
                                                                   headroom and a nonzero reflection corner,
                                                                   but the residual Weyl shears rather than
                                                                   negates; THR-alone carrier is closed and the
                                                                   remaining duality layer is only an interface.

Product-formula / Xbar / PFD carrier      ADDRESS-ONLY            docs 28-31; GG. Global cancellation and
                                                                   survivor combs exist distributionally; scale
                                                                   is expelled from torsion and the remaining
                                                                   duty is the archimedean unit / Poisson
                                                                   exchange. Not a BC-E3' carrier.

GG global survivor aggregate              SLOT-DATA / ADDRESS     GG; docs 31,34. Renormalized survivor
                                                                   existence names one continuum unit per place,
                                                                   but the survivor comb is a shadow/coupling
                                                                   datum, not an unforced odd-slot spectrum.

Norm-Gram / signature flow                CARRIER-BLIND           II; HH; docs 33,37. Lorentzian signatures
                                                                   and max-Grams are certified but structurally
                                                                   blind to zeros or run on Epstein-shaped
                                                                   degree data; integer signature response is
                                                                   too small and density-dominated.

Delta_p / Gaussian silhouette             SLOT-DATA               WW/QQ/AB; docs 39-40. Complete Fourier
                                                                   silhouette is the inserted unit's local Tate
                                                                   data. AB proves shape/payment constants are
                                                                   covariant slot data, not object data.

Liquid/metrized slot                      ADDRESS-ONLY            MM/XX; doc 41. The only remaining address:
                                                                   internal R with Fourier / enriched liquid
                                                                   coefficients where log p can live. No printed
                                                                   proper archimedean square carrier is banked.
```

No row is a decision-grade SURVIVOR.

## 3. Positive Residue

The classification is not a negative washout. It leaves a precise
residue:

```text
best supply carrier
  The ku face. It gives a theorem-grade one-dimensional supply
  structure, exact prime-power carrier guard, and the depth wall. It
  fails exactly because it has one evaluation.

best address
  The liquid/metrized layer. Bare topology is scale-blind; solenoids
  self-supply; Anderson duality supplies finite-adic rational data but
  misses the archimedean R slot. Therefore the missing carrier, if it
  exists, must be built in enriched/metrized liquid coefficients or an
  equivalent non-bare trace/kernel setting.

best sign form
  The index/Gram face. HH homes the prime side exactly, and the strict
  square/vdGS layer makes h^0/effectivity fire. It fails only at the
  square-level duality and full graph-cone exhaustion.

best second-evaluation pattern
  Quillen over F_q. It has genuine independent evaluations but empty /
  forced spectrum. It specifies the pattern to transplant, not the
  target carrier.
```

Thus the missing structure is the simultaneous merger of four things
that exist separately in the bank:

```text
ku-face supply and depth wall
+ liquid/metrized scale address
+ index/Gram forced positivity
+ Quillen/Weil second-evaluation independence
```

The banked corpus contains each shadow separately and no object that
contains all four.

## 4. Consequences

M-C's result changes the next work:

```text
1. Do not keep searching the banked carriers for a sleeper. The
   first-pass table finds none at decision grade.

2. Treat the ku face as the supply model, not as the missing object.
   Its role is to constrain any future liquid carrier: it must preserve
   the prime-power comb, depth wall, and evasion-not-surplus theorem
   while adding an independent spectral evaluation. After doc 43, do
   not include the Gaussian `(11;2)@4.96` failure itself in this
   constraint; that cell is unit-slot phase data.

3. Treat liquid/metrized coefficients as mandatory, not optional. Any
   candidate built only from bare Shv(S^1), solenoid entropy, p-complete
   TP, or plain spectra repeats an already classified failure.

4. Run M-A only to decide whether a unit-independent deep obstruction
   joins OC2. M-C already says M-A cannot by itself construct BC-E3'.

5. Run M-B only as a BC13 exhaustion test on a genuinely liquid/index
   candidate. Re-running it on the strict square, ku face, or max-Gram
   face will reproduce known STRICT-FACE failures.
```

## 5. Updated Characterization

After M-C, doc 41's communicable form tightens to:

```text
Find a liquid/metrized enhancement of the ku/index carrier whose
prime-power comb remains structurally unavailable for DH/Epstein, whose
Frobenius-graph index/Gram values are intrinsically nonnegative over the
full Sonin core, and whose comparison with a count evaluation has a
nonempty odd spectral slot with eigenvalues supplied by the carrier
rather than by the acting map.
```

This is still not a construction. It is a sharper negative statement:
the banked carrier list has no hidden survivor; the missing structure
must be new at the liquid/index/second-evaluation interface.
