# S - The p = 2 anomaly of the reflection fold: THR(F_2)^{tC_2} and the p = 2 fold structure

Status: worker S, fresh context, 2026-06-10. Section 1 (pre-registration)
written BEFORE the source-assembly, computation, witness, and literature
sections below it; the lead can verify ordering by the file history of this
single write plus the witness timestamps. Required reading done in full:
doc 24, M-doc (M-thr-fold-test.md), N-doc sec 1.4 (the base; K = -2{2}).

## 1. PRE-REGISTERED READINGS (before computing)

The task's registered dichotomy:

```text
(s1) MODIFIED FOLD: p = 2 is the odd-p fold plus a computable correction;
     state the corrected ladder and its regularized characteristic
     function; check for a Gamma_R vs Gamma_C doubling artifact.
(s2) GENUINELY ANOMALOUS: the Euler-class obstruction is permanent; the
     reflection-fold mechanism breaks at 2; the archimedean carrier cannot
     be THR alone; state the entanglement with CC's {2} as a finding.
```

My refined sub-readings, registered now, each with fail criteria:

```text
S-r1 (verdict shape): expected outcome is a SPLIT verdict -- s2 with
     fully computed structure: the two odd-p vanishings that constitute
     the fold mechanism (Phi^{C_2} = 0 and (-)^{tC_2} = 0) BOTH fail at
     p = 2, permanently (they are forced by (HF_2)^{tC_2} != 0 and by
     DMPR's Euler classes), so the clean fold is NOT recoverable on
     THR(F_2); but the deviation is computable in closed form with NO
     blocked spectral-sequence differentials, and it contains an
     s1-component: a Gamma_R -> Gamma_C eigenvalue-degeneration doubling.
     FAIL: if differentials/extensions block the Tate computation, the
     verdict becomes the blocked-statement deliverable instead.
S-r2 (the Tate): pi_* THR(F_2)^{tC_2} is, degreewise, the PRODUCT
     completion of the collapsed Tate E_2-page: each pi_j isomorphic to
     F_2[[z]] (z of degree 0), globally F_2[[z]][t^{+-1}] with |t| = -1,
     z = t^2 x, x the Bokstedt class; equivalently
     THR(F_2)^{tC_2} = prod_{n>=0} Sigma^{2n} (HF_2)^{tC_2}
     = (Lin line) tensor-hat (weight-completed disk). Mechanism to be
     proved: DMPR Thm 5.18's genuine splitting THR(F_2) = wedge_{n>=0}
     Sigma^{n rho} HF_2 forces Borel formality (each summand's Borel
     type has homology in a single degree), so E_2 = E_infty; the
     wedge-vs-product correction is controlled degreewise by
     connectivity. FAIL: if the DMPR splitting is not as genuine
     C_2-spectra, or the degreewise finiteness argument for the norm
     cofiber fails, withdraw and restate.
S-r3 (doubling artifact -- the s1-component): the res-visible weight
     ladder of THR(F_2)^{C_2} = F_2[xbar, y] is carried by F_2[xbar]
     (res xbar = x, weight 1) and is the UNFOLDED ladder {n >= 0},
     spacing 1 -- because the Weyl eigenvalue selection (-1)^n that
     produces the fold at odd p DEGENERATES mod 2 (both F_infinity
     eigenvalues +-1 coincide). Regularized characteristic function
     prod_reg{s+n} = sqrt(2pi)/Gamma(s): the Gamma_C shape, and EXACTLY
     the product of the two folded Gamma_R sectors:
     prod_reg{s+n} = prod_reg{s+2n} * prod_reg{s+2n+1}, mirrored by
     Legendre Gamma_R(s) Gamma_R(s+1) = Gamma_C(s). So the doubling
     artifact the task asks about IS present and is exactly Gamma_R vs
     Gamma_C. FAIL: witness gates on these identities fail, or the
     weight dictionary does not force the unfolded reading.
S-r4 (Euler tower -- the s2-component): the y-tower (|y| = 1, res y = 0,
     RO-lift x~a, weight content 0) has NO odd-p analogue and no ladder
     reading through the doc-19/20 dictionary; the full degree-graded
     fixed-point carrier F_2[xbar, y] (Poincare series 1/((1-q)(1-q^2)))
     has regularized characteristic function of BARNES Gamma_2(s | 1,2)
     type with QUADRATIC anomalous dimension
     zeta_B(0, s | 1,2) = s^2/4 - 3s/4 + 11/24 -- a rank-2/surface-like
     Gamma-factor, not a corrected rank-1 ladder. FAIL: anomalous
     dimension comes out linear (then the anomaly reading is withdrawn
     and p = 2 is s1 after all).
S-r5 (2-adic entanglement of the real place): the nonvanishing Tate
     carries, per weight n >= 0, a full two-sided degree line of period
     1 (HALF the TP periodicity 2), and the weight direction is
     COMPLETED: duality completion -- which at odd p does not happen at
     the reflection, the program's archimedean signature -- DOES happen
     at p = 2, and what it completes is exactly the 2-adic Euler-factor
     ladder. The CC link (K = -2{2}) is recorded as a structured rhyme
     only, with N-doc 1.4(b)'s caveat (the {2}-support of K is
     bookkeeping) quoted against overclaiming. FAIL: the computed Tate
     has no weight-complete structure or no per-weight full line.
```

Evaluation rules fixed in advance: weights are read through res and
RO(C_2)-lifts exactly as in the M-doc (weight = Bokstedt x-power via res;
fail-closed if res-invisible). The doc-19/20 pipeline conventions for
regularized products (Lerch/Hurwitz, scale anomaly = zeta_L(0)) are
reused unchanged from witness prime_int_thr_fold.py. Any
spectral-sequence differential I cannot determine is reported as an
unknown with its exact (r, bidegree) location, never guessed. Literature
search for prior computation of THR(F_2)^{tC_2} is mandatory before
claiming novelty; anything found is archived and cited, and supersedes my
derivation where it overlaps.

## 2. Inputs transcribed (theorem numbers; archived sources)

Conventions as in the M-doc: pi_{s,t} = [S^{s,t}, -]^{C_2}, S^{s,t} =
S^{t sigma} ^ S^{s-t}; rho = 1 + sigma; "weight" = Bokstedt x-power read
through res. New archives this pass (research/proof/refs/):
hornbostel-park2023-thr-perfectoid.pdf (arXiv:2310.11183, J. Topology
2025), lewis2024-real-bokstedt-ss.pdf (arXiv:2408.07188),
angelini-knoll-gerhardt-hill2021-real-witt.pdf (arXiv:2111.06970).

- [DMPR Thm 5.18] (verbatim from the archived PDF, p. 55): "There is a
  stable equivalence of Z/2-equivariant ring spectra TH_{F_p}(S^{2,1})
  -> THR(F_p)", TH_{F_p}(S^{2,1}) = the free associative HF_p-algebra
  on S^{2,1}; "in particular pi_{*,*}THR(F_p) = (HF_p)_{*,*}[x~],
  |x~| = (2,1)". QS's restatement [QS21 Thm 6.2] makes the underlying
  module explicit: TH_{F_p}(S^{2,1}) = V_{n>=0} Sigma^{2n,n} HF_p.
  THIS IS THE LOAD-BEARING INPUT: THR(F_2) splits as a wedge of
  regular-representation suspensions of the genuine HF_2.
- [DMPR Cor 5.20] (verbatim): pi_*(THR(F_2)^{Z/2}) = F_2[xbar, y],
  |y| = 1, |xbar| = 2; xbar = x~u -> x under res, y = x~a -> 0
  (a = Euler class, bidegree (-1,-1); u of bidegree (0,-1); [HK01
  Prop 6.2] for (HF_2)_{*,*}).
- [DMPR Prop 5.22] (verbatim): Phi^{Z/2}THR(F_p) contractible for p
  odd; for p = 2, pi_* Phi^{Z/2}THR(F_2) = F_2[w_1, w_2],
  |w_1| = |w_2| = 1; proof via Phi^{Z/2}THR(F_p) ==
  Phi^{Z/2}HF_p ^L_{HF_p} Phi^{Z/2}HF_p and pi_* Phi^{Z/2}HF_2 = F_2[w],
  |w| = 1 [HK01], [Wil17]. From the proof of 5.18 (free algebra on
  S^{2,1}, Phi(S^{2,1}) = S^1): the two generators are w_1 = w (the
  HF_2-geometric class) and w_2 = Phi(x~).
- [QS21 Sec 6.1 opening, verbatim]: "both the C_2-geometric fixed
  points Phi^{C_2}F_p and the C_2-Tate construction (HF_p)^{tC_2} are
  trivial, so the same holds for THR(HF_p) ... THR(HF_p) is both Borel
  torsion and Borel complete" -- FOR p ODD ONLY (their Sec 6.1). Their
  p = 2 section computes TCR^-/TPR (parametrized S^1-Tate), NOT the
  reflection Tate.
- [QS-par, arXiv on parametrized Tate, archived txt line 3297ff]: "(i)
  p odd: (-)^{tC_2} vanishes identically on p-complete spectra ...
  (ii) p = 2: the restriction of (-)^{tC_2} to bounded-below Borel
  C_2-spectra inverts 2-adic equivalences and is valued in 2-complete
  spectra." The dichotomy that makes p = 2 the only interesting
  reflection-Tate prime.
- [HW = Hahn-Wilson, arXiv:1911.05687, Thm 1.8 + Thm A]: N_{C_2}F_2 is
  Borel complete (the C_2-Segal conjecture = Lin's theorem, reproved);
  THR(F_2) = F_2 (x)_{NF_2} F_2 is their basic descent datum, computed
  as a Hopf algebroid (x~ primitive, |x~| = rho, comodule algebra
  F_2[a,u]). Note: Borel completeness of the NORM does NOT transfer to
  THR(F_2) (a relative tensor/colimit of complete objects); indeed we
  compute below that THR(F_2) is NOT Borel complete.
- (HF_2)^{tC_2}: pi_* (HF_2)^{tC_2} = H-hat^{-*}(C_2; F_2) =
  F_2[t^{+-1}], |t| = 1 in COHOMOLOGICAL grading, i.e. t in HOMOTOPY
  degree -1. Source: Greenlees-May, "Generalized Tate cohomology",
  Mem. AMS 543 (1995) (Tate spectral sequence, E_2 = H-hat^*(G; pi_*X),
  collapsing for X = HM to H-hat^*(G;M); cited by both QS papers).
  Verified independently below (the one-line Tate SS collapses; the
  norm H_0(C_2;F_2) -> H^0(C_2;F_2) is multiplication by 2 = 0, so
  H-hat^0 = F_2 and t is invertible by periodicity of complete
  resolutions for cyclic groups). Convention pinned: |t|_homotopy = -1.

Literature search (mandatory per registration): no computation of
THR(F_2)^{tC_2} (reflection/Weyl C_2-Tate) exists in DMPR, QS19, QS21,
DMP21, HW (all archived, all checked), nor in the 2023-2025 wave found
by search: Hornbostel-Park (THR of perfectoid rings, real BMS -- no
reflection Tate), Lewis (Real Bokstedt SS tools), AKGH (THR via the
norm, Real Witt vectors), Park (THR of schemes), motivic THR. Search
terms used: real topological Hochschild + Tate/C_2-Tate/tC_2 + F_2,
Lin's theorem + THR, Segal conjecture + THR, Borel complete + THR.
The computation below is, to the best of this search, NEW.

## 3. THEOREM (the missing corner, computed)

THEOREM S.1. There is an equivalence of spectra

    THR(F_2)^{tC_2}  ~=  prod_{n>=0} Sigma^{2n} (HF_2)^{tC_2},

and the canonical comparison map to the product is the equivalence. On
homotopy, with t the (HF_2)^{tC_2}-class (|t| = -1) and x the Bokstedt
class (|x| = 2, the image of x~):

    pi_j THR(F_2)^{tC_2} ~= prod_{b>=0} F_2 . {t^{2b-j} x^b}  for ALL j in Z,

i.e. as a graded module over pi_*(HF_2)^{tC_2} = F_2[t^{+-1}]:

    pi_* THR(F_2)^{tC_2} ~= F_2[t^{+-1}] (x)-hat F_2[x]
                         ~= F_2[[z]][t^{+-1}],   z := t^2 x, |z| = 0,

the x-adically COMPLETED (degreewise product) Laurent ring: every
homotopy group is a copy of F_2[[z]]. In particular THR(F_2)^{tC_2} is
very far from zero (the odd-p vanishing fails maximally), THR(F_2) is
NOT Borel complete, and the Tate spectral sequence
E_2 = H-hat^*(C_2; F_2[x]) = F_2[t^{+-1}] (x) F_2[x] (the M-doc sec 4
"missing computation" page) COLLAPSES: there are NO differentials and
no hidden extensions; the abutment is the degreewise completion of the
E_2-page. Similarly

    THR(F_2)^{hC_2} ~= prod_{n>=0} Sigma^{2n} (HF_2)^{hC_2},
    pi_j THR(F_2)^{hC_2} = prod_{b >= max(0, ceil(j/2))} F_2 . {t^{2b-j} x^b}

(the t-nonnegative part, degreewise completed).

PROOF (five steps, each rigor-marked).

(1) [transcription] DMPR Thm 5.18: THR(F_2) ~= V_{n>=0} Sigma^{n rho}
    HF_2 as genuine C_2-spectra (a fortiori as Borel C_2-spectra).

(2) [derivation, standard equivariant stable homotopy] For any Borel
    C_2-spectrum Y, (Sigma^{n rho} Y)^{tC_2} ~= Sigma^{2n} Y^{tC_2}.
    Mechanism: X^{tC_2} = (E~C_2 (x) F(EC_2+, X))^{C_2}; suspension by
    n sigma passes through F(EC_2+,-) and (x); on E~C_2-local objects
    the Euler class a: S^0 -> S^{sigma} is invertible (E~C_2 =
    colim_a S^{n sigma}), so Sigma^{n sigma} ~= Sigma^n there. Hence
    (Sigma^{n rho} HF_2)^{tC_2} ~= Sigma^{2n} (HF_2)^{tC_2}, with
    pi_* = F_2[t^{+-1}] shifted by 2n.
    Equivalent formulation (mod-2 Thom isomorphism of the sign line):
    Sigma^{sigma} HF_2 ~= Sigma^1 HF_2 already as BOREL HF_2-modules,
    so Borel-ly THR(F_2) ~= V_n Sigma^{2n} HF_2 with TRIVIAL actions:
    this is the formality that the M-doc feared would need HW's
    Hopf-algebroid control. It is free, from DMPR 5.18: in
    D(F_2[C_2]) = D(F_2[eps]), the summand Sigma^{n rho}HF_2 is the
    complex of cellular chains C~_*(S^{n rho}; F_2), whose homology is
    concentrated in the single degree 2n; any complex with homology in
    one degree is formal. No k-invariants survive.

(3) [derivation] Wedge = product: the summands' underlying and fixed
    connectivities tend to infinity, so V_n Sigma^{n rho}HF_2 ->
    prod_n Sigma^{n rho}HF_2 is an equivalence (degreewise finitely
    many summands contribute to each homotopy group of each corner).

(4) [derivation, the degreewise control replacing "Tate commutes with
    colimits" -- NOT assumed] Write X = THR(F_2), X_n = Sigma^{n rho}
    HF_2. Homotopy fixed points preserve products: pi_j X^{hC_2} =
    prod_n pi_j X_n^{hC_2} = prod_{b >= max(0,ceil(j/2))} F_2 (each
    factor H^{2b-j}(C_2;F_2)). Homotopy orbits preserve wedges:
    pi_j X_{hC_2} = (+)_n H_{j-2n}(C_2; F_2) = F_2^{floor(j/2)+1}
    (j >= 0) -- FINITE in each degree. By naturality the norm map is
    diagonal with components Nm_n, and each Nm_n = 0 on homotopy: for
    trivial action the only degree where source and target overlap is
    pi_{2n}, where the norm is multiplication by |C_2| = 2 = 0. The
    norm cofiber LES therefore splits into short exact sequences
       0 -> pi_j X^{hC_2} -> pi_j X^{tC_2} -> pi_{j-1} X_{hC_2} -> 0,
    and the canonical map X^{tC_2} -> prod_n X_n^{tC_2} is compatible
    with the componentwise sequences, iso on the fixed part (step 4a)
    and iso on the (degreewise finite, sum = product) orbit part.
    Hence a pi_*-isomorphism. QED for the additive/module statement.

(5) [derivation with caveat] Ring structure: the Tate of a C_2-ring is
    a ring, the unit gives F_2[t^{+-1}] -> pi_*, and x is the image of
    xbar under can: THR^{C_2} -> THR^{hC_2} -> THR^{tC_2} (or of x~ on
    the collapsed E_infty-page). The multiplication is the completion
    of the E_infty-page multiplication; the identification
    pi_* = F_2[[z]][t^{+-1}] is canonical up to filtration-preserving
    choice of the generator x (possible higher-z corrections to any
    chosen lift are absorbed by re-choosing x). The associated-graded
    and module statements are unconditional.

CROSS-CHECKS (all exact, witness W0, ALL PASS):
- Isotropy corner: the same five steps give pi_* THR(F_2)^{hC_2} as
  stated, and reproduce DMPR's two computed corners independently:
  Phi^{C_2}THR(F_2) = V_n Sigma^n Phi^{C_2}HF_2 with pi_* =
  F_2[w] (x) F_2[Phi x~] = F_2[w_1, w_2] (matches Prop 5.22), and the
  a-inversion of pi_{*,*} = (HF_2)_{*,*}[x~] reproduces Cor 5.20.
- Tate-square consistency, degreewise integer bookkeeping: with
  fix_j = floor(j/2)+1, Phi_j = j+1, orb_j = floor(j/2)+1,
  codim(hfix_j in Tate_j) = ceil(j/2), the two zero-norm short exact
  sequences demand fix_j + orb_{j-1} = Phi_j and codim_j = orb_{j-1}:
  both hold exactly for all j <= 400 (W0a, W0b).

## 4. The complete p = 2 Tate square (corners AND maps)

```text
corner                pi_*                                  status
THH(F_2) (underlying) F_2[x], |x| = 2                       Bokstedt
THR^{C_2}             F_2[xbar, y], |xbar| = 2, |y| = 1     DMPR Cor 5.20
Phi^{C_2}             F_2[w_1, w_2], |w_i| = 1              DMPR Prop 5.22
THR_{hC_2}            (+)_n Sigma^{2n} H_*(C_2;F_2)         this doc (step 4)
THR^{hC_2}            F_2[t][[x]]  (degreewise product)     this doc, NEW
THR^{tC_2}            F_2[[z]][t^{+-1}], z = t^2x, |z| = 0  this doc, NEW
```

The maps (all derived, sec 3 cross-checks + DMPR proof of 5.18):

- fix -> Phi: xbar |-> w_1 w_2, y |-> w_2 (w_2 = Phi(x~), w_1 = the
  HF_2-class; Phi(u) = w_1, Phi(a) = 1). INJECTIVE; coker ~=
  Sigma(orbits) degreewise (W0a). The p = 2 genuine fixed points are
  ENTIRELY geometric -- zero Borel-torsion content; equivalently the
  transfer (orbit -> fixed) map is ZERO on homotopy in all degrees.
- fix -> hfix: xbar |-> x, y |-> t x (mod higher z-filtration);
  injective. Derived: hfix -> Tate is injective (norm = 0), the square
  commutes, and y's Tate image equals w_2's image t^{-1}z = tx != 0.
  So F_2[xbar,y] = the POLYNOMIAL subring F_2[x, tx] of the completed
  F_2[t][[x]]: the genuine fixed points are the uncompleted part; the
  failure of Borel completeness is exactly the degreewise completion.
- Phi -> Tate: w_1 |-> t^{-1}, w_2 |-> tx = t^{-1}z; injective.
- hfix -> Tate: the degreewise inclusion (t-nonnegative part);
  coker_j ~= pi_{j-1} orbits (W0b). NOTE: Tate is NOT the naive
  t-localization of the completed hfix (localization and degreewise
  completion do not commute); both are localizations-then-completions
  of the same polynomial page.

## 5. The p = 2 fold structure (what replaces the clean fold)

### 5.1 Fixed points: fold core x doubling x Euler tower

Exact three-factor decomposition (W0c, coefficientwise):

    F_2[xbar, y] = F_2[xbar^2]  (x)  {1, xbar}  (x)  F_2[y]
                   fold core         eigenvalue       Euler tower
                   |xbar^2| = 4      doubling         |y| = 1
                   weights {2n}      weight parity    weight 0
                   = odd-p F_p[y]    restored         res-invisible

- FOLD CORE: F_2[xbar^2], degree 4, res(xbar^2) = x^2 -- precisely the
  odd-p folded ladder (DMPR Cor 5.19 shape). The fold does not vanish
  at 2; it is dressed.
- DOUBLING (the s1-component; the task's "Gamma_R vs Gamma_C doubling
  artifact" -- ANSWER: YES, it appears, in exactly this form): the
  odd-p fold mechanism is Serre's F_infinity-eigenvalue selection: the
  Weyl group acts on weight n by (-1)^n and the fixed sector keeps
  even n. Mod 2 the two eigenvalues +-1 COLLIDE: (-1)^n == 1, no
  selection, BOTH parities survive -- the factor {1, xbar}. The
  res-visible weight ladder is the UNFOLDED {n >= 0}, spacing 1
  (carried by F_2[xbar], res xbar^n = x^n). Its regularized
  characteristic function (doc-19/20 pipeline, witness W1):
      prod_reg_{n>=0}(s + n) = sqrt(2pi)/Gamma(s)   -- the Gamma_C
  shape -- and the degeneration is EXACT at the level of regularized
  products (W2):
      prod_reg{s+n} = prod_reg{s+2n} . prod_reg{s+2n+1},
  the multiplicative mirror of Legendre Gamma_R(s)Gamma_R(s+1) =
  Gamma_C(s) (W3). Reading: at p = 2 the reflection sector behaves
  like a COMPLEX place -- the real place seen at 2 fails to be real,
  it is the doubled/complexified place. Anomalous dimension of this
  component: zeta_H(0,s) = 1/2 - s (affine, rank 1), vs (1-s)/2 for
  the odd-p fold (W3).
- EULER TOWER (the s2-component): F_2[y], |y| = 1, y = x~a, weight 0,
  res y = 0 -- no odd-p analogue, no ladder reading through the
  dictionary (res-invisible: by the registered evaluation rule this is
  reported as outside the fold, fail-closed). It is the shadow of
  Phi^{C_2} != 0 (y |-> w_2): the Euler-class direction. Its effect on
  the regularized characteristic function of the full degree-graded
  carrier {2i + k : i,k >= 0} is to raise the RANK: the zeta function
  is Barnes zeta_2(u, s | 1, 2), and (W4, two independent routes)
      zeta_2(0, s | 1,2) = s^2/4 - 3s/4 + 11/24   -- QUADRATIC.
  Any rank-1 ladder has AFFINE zeta_L(0, s); the second s-difference
  1/2 != 0 certifies rank 2 (W4b). The p = 2 fixed-point carrier is a
  BARNES Gamma_2(s | 1, 2) object -- a two-period (surface-like)
  Gamma-factor, not a corrected Gamma_R. (Observation, not used: Barnes
  double-Gamma factors are exactly what Manin/Kurokawa assign to the
  "compactified Spec Z over F_1"; the second period equals 2.)

### 5.2 Tate: the duality completion DOES happen at 2, and it is 2-adic

At odd p the program's structural signature was: the Tate VANISHES at
the reflection = no duality completion at the archimedean sector. At
p = 2 (Theorem S.1):

    THR(F_2)^{tC_2} = (Lin line F_2[t^{+-1}])  (x)-hat  (weight disk F_2[[z]])

- The weight direction z = t^2 x (weight 1, degree 0) is COMPLETED:
  the Tate contains the full weight tower {n >= 0} of THH(F_2),
  z-adically completed -- through the doc-19/20 dictionary
  (weight n <-> 2^{-ns} supply), the COMPLETE 2-adic Euler-factor
  ladder of (1 - 2^{-s})^{-1}.
- Per weight n the Tate carries a FULL two-sided degree line (the
  F_2[t^{+-1}]-factor). A full vertical ladder regularized in the
  reflection-equivariant (KMS-1/2, M-doc r3) scheme has characteristic
  function (W5, exact identity + scale-freeness):
      2 sinh((s+n) log2 / 2) = 2^{(s+n)/2} (1 - 2^{-(s+n)}),
  the SELF-DUAL-COMPLETED Euler factor at q = 2, anomalous dimension 0.
- The t-periodicity is 1, HALF of TP's periodicity 2 (QS21: the TPR
  class has degree rho, the underlying TP class degree 2; the
  reflection-Tate class t has degree 1). Reading (flagged, not a
  theorem): a period-1 line corresponds under the doc-19/20 dictionary
  to a vertical ladder of modulus q^{1/2} = sqrt 2 -- the half-weight /
  q^{s/2}-prefactor signature, the same half that KMS-1/2 and Gamma_R's
  half-powers carry. The real place does not see the prime 2; it sees
  its square root.
- pi_0 THR(F_2)^{tC_2} = F_2[[z]]: the reflection-Tate at 2 is not a
  point but a FORMAL DISK in the weight direction (1-dimensional formal
  moduli). At odd p this ring is 0; for TP(F_p), pi_0 = Z_p (a point of
  Spf Z_p). Observation: the only place where the reflection sector
  acquires a geometric direction is p = 2.

## 6. Verdict: s1/s2

REGISTERED ANSWER (matches pre-registration S-r1 exactly; no carrier or
verdict relocation needed this time):

(s2), WITH THE ANOMALY FULLY COMPUTED -- and containing the (s1)
doubling artifact as one of its two factors. Precisely:

1. The reflection-fold mechanism of doc 24 (eigenvalue selection +
   Tate vanishing + geometric-fixed-point vanishing) breaks at p = 2
   PERMANENTLY: all three ingredients fail, and the failures are
   forced by mod-2 facts that no modification of the functor repairs
   ((HF_2)^{tC_2} = F_2[t^{+-1}] != 0 -- Lin territory; Euler class
   a != 0 on (HF_2)_{*,*}; (-1) == 1 mod 2). The Euler-class
   obstruction is permanent: THR alone cannot carry a clean
   archimedean fold at 2.
2. But nothing is blocked: THR(F_2)^{tC_2} is computed in closed form
   (Theorem S.1; no unknown differentials -- the M-doc's feared
   non-formality is refuted by DMPR 5.18 formality), and the p = 2
   fold structure factorizes exactly:
       fixed points = (odd-p fold core) x (Gamma_R -> Gamma_C
       eigenvalue-degeneration doubling) x (Euler tower),
   with regularized characteristic data: Gamma_C shape on the
   res-visible ladder (the s1-component: a genuine Gamma_R vs Gamma_C
   doubling artifact -- at 2 the real place degenerates to a complex
   place), upgraded by the Euler tower to a rank-2 Barnes
   Gamma_2(s | 1,2) with quadratic anomalous dimension
   s^2/4 - 3s/4 + 11/24 (the s2-component: not a ladder correction).
3. THE ENTANGLEMENT FINDING (for the program ledger): duality
   completion, which the archimedean sector must NOT undergo (the
   odd-p Tate-vanishing was the structural form of this), HAPPENS at
   the reflection at p = 2, and what gets completed is exactly the
   2-adic Euler-factor ladder, in self-dual (KMS-1/2) form, times a
   weightless Lin line of HALF the TP periodicity. The real place is
   2-adically entangled in this precise computed sense: the
   would-be-archimedean carrier at 2 contains the completed local
   factor AT 2 rather than a Gamma-factor. Consequently any
   compactified THR-based archimedean object must either (a) work
   away from 2 (THR(Z)[1/2], where DMPR's splitting restores the
   clean fold -- M-doc sec 4 reading), with the place at 2 and the
   place at infinity treated as ONE entangled pair, or (b) supply a
   new carrier at 2. CC-square rhyme (flagged as rhyme, NOT a
   derivation, per N-doc 1.4(b): the {2}-support of K = -2{2} is
   bookkeeping, deg K = -2 log 2 = -log 4 is the invariant content):
   CC's base also refuses to separate the real place from the prime 2
   (dualizing scale 1/4, deg K = -log 4); here the homotopy-theoretic
   reflection sector at 2 likewise refuses, with factors of 2 and 4
   appearing as: |y| = 1 vs |xbar| = 2 vs |xbar^2| = 4; t-period 1 vs
   TP-period 2; second Barnes period 2. No numerical identification is
   claimed.

## 7. DOF audit (G-INT6)

- Theorem S.1: zero free parameters; inputs are one published theorem
  (DMPR 5.18) plus standard equivariant stable homotopy (isotropy
  separation, Thom iso mod 2, norm cofiber); the wedge/product step is
  degreewise-finite bookkeeping (W0).
- Sec 5 decomposition: exact ring factorization (W0c integer-exact);
  the ladder readings spend ONLY the doc-19 weight dictionary already
  spent by docs 19/20/M; the characteristic functions are
  affine-invariant consequences (W1-W5, all exact identities, no
  fitting). The Barnes constant 11/24 is forced, not chosen.
- Sec 6.3 readings flagged as readings: sqrt(2)-modulus of the Lin
  line; Euler-factor interpretation of the z-disk; CC rhyme. None is
  load-bearing for the verdict.

## 8. Honest limits

- Ring structure of pi_* THR(F_2)^{tC_2}: the module-over-F_2[t^{+-1}]
  and associated-graded statements are unconditional; the closed-form
  ring identification F_2[[z]][t^{+-1}] is up to filtration-preserving
  re-choice of the generator x (step 5 caveat). No consequence drawn
  here depends on the difference.
- fix -> hfix: y |-> tx is a leading-term (mod z^2-filtration)
  statement; the exact image is not pinned. Harmless for all claims.
- The Tate SS "collapse" is stated as: the abutment equals the
  degreewise completion of E_2 = F_2[t^{+-1}](x)F_2[x]. The
  completion is part of the answer (conditional convergence), not an
  extension problem left open.
- All ladder/Gamma readings go through the doc-19/20 dictionary
  (weight = x-power via res); the y-tower is res-invisible and is
  treated fail-closed as NON-ladder data (its Gamma_2 reading uses the
  degree grading instead, and that choice is flagged: degree vs weight
  is a convention boundary the lead should adjudicate before this
  enters a gate).
- Nothing here constructs the archimedean object or touches THR(Z) at
  2 (still open in the literature; DMPR compute THR(Z) only away from
  2). The verdict constrains carriers; it does not produce one.
- No RH/zero-side input; all sources are supply-side homotopy theory.
- Literature: absence-of-computation is as of this search (sec 2);
  Hornbostel-Park 2310.11183 v3 (July 2025) was checked by abstract
  and search only, not read line-by-line; if its THR(F_p)-perfectoid
  refinements contain a reflection-Tate statement it supersedes the
  novelty claim (not the math).

## 9. Next steps (ranked, for the lead)

1. Adopt the gap-ledger update for doc 24 sec 3: "THR(F_2)^{tC_2} not
   in the literature" -> computed (Theorem S.1); p = 2 verdict s2 with
   computed structure; the doubling artifact and the 2-adic
   entanglement are now statements, not flags.
2. The away-from-2 route: DMPR's THR(Z)[1/2] splitting makes the odd-p
   fold analysis apply verbatim; the p = 2 + infinity ENTANGLED PAIR
   should be posed as a single compactification datum (matches both
   the CC rhyme and the K-doc/N-doc base findings). Concretely: pose
   the reflection sector of a compactified THR(Z) as an object over
   Spec Z[1/2] u {entangled fiber at (2, infinity)}.
3. The Lin-line question: whether the weightless F_2[t^{+-1}] factor
   is the homotopy-theoretic carrier of the program's missing 1/(2pi)
   scale (it is exactly the part of the p = 2 Tate with no Euler/weight
   content, and its period-halving is the q^{1/2} signature). A
   targeted question: compute the residual transfer/Frobenius
   structure on THR(F_2)^{tC_2} (e.g. the map from
   Phi^{C_2}THR(F_2) = F_2[w_1,w_2], w_1 |-> t^{-1}, w_2 |-> tx) and
   ask whether the KMS-1/2 scheme is forced on the z-disk by the
   C_2-equivariant multiplication -- a finite, posed question one rung
   below H-r3.
4. Check Hornbostel-Park in full (archived) for any overlap.
