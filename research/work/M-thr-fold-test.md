# M - Gate C5''-infty first checkpoint: the reflection-Tate fold test on THR(F_p)

Status: executed 2026-06-10 (worker M, fresh context). Primary sources
read and archived (research/proof/refs/): Dotto-Moi-Patchkoria-Reeh
arXiv:1711.10226 = JEMS 23 (2021) 63-152 (dotto-moi-patchkoria-reeh2017-
thr.pdf, already archived by J); Quigley-Shah arXiv:2112.07462
(quigley-shah2021-two-theories-real-cyclotomic.pdf, NEW); Quigley-Shah
arXiv:1909.03920 (quigley-shah2019-parametrized-tate-real-cyclotomic.pdf,
NEW); Hahn-Wilson arXiv:1911.05687 = Adv. Math. 387 (2021) 107839
(hahn-wilson2019-thr-segal.pdf, NEW); Dotto-Moi-Patchkoria
arXiv:2106.04891 (dotto-moi-patchkoria2021-geometric-fixed-tcr.pdf, NEW).
Witness: prime_int_thr_fold.py (ALL PASS, exit-code gated; W1-W3 cover
exactly the analytic claims made here).

HEADLINE (fail-closed, the one-line version): r1 as pre-registered FAILS
-- the C_2-Tate construction does not fold the ladder, because at odd p
it is CONTRACTIBLE, and the dihedral S^1-Tate (TPR) keeps the FULL
ladder. But the fold the gate wants (half-line, start 0, spacing
doubled = the Gamma_R shape) IS in the literature-computed objects: it
is carried by the genuine C_2-FIXED POINTS of THR(F_p) (p odd), a
relocation of carrier, flagged post-hoc. The reflection sector folds by
taking fixed points, not Tate; the Tate construction is exactly the
wrong functor at a reflection. r2 then passes on the fixed-point
carrier and fails on the Tate carrier. r3: a clean parity lemma shows
KMS-1/2 is the UNIQUE reflection-equivariant scheme in the relevant
family (derivation, elementary); what is still missing is any theorem
that the homotopy-theoretic C_2 acts on the analytic determinant layer.

## 1. Pre-registered readings (registered before the computation
## sections were written; r1, r2 verbatim from the J-doc sec 5)

```text
r1 (LADDER FOLD): does the C_2-Tate construction THR(F_p)^{tC_2} (and
    the O(2)-relative / dihedral-Tate constructions) fold the weight
    grading Z -> {n >= 0} with spacing doubled (the Gamma_C -> Gamma_R
    fold)?
r2 (ANOMALOUS DIMENSION): does the associated regularized
    characteristic function have anomalous dimension (1-s)/2
    (half-ladder) rather than 0 (full ladder)?
r3 (SCHEME SELECTION, registered THIS pass, before computing): does
    the C_2-fixed/real structure single out the conjugation-symmetric
    regularization scheme on the folded ladder, i.e. pair each
    eigenvalue with its conjugate? Pass criterion: a precise structural
    statement with explicit hypotheses, each part marked derivation vs
    reading; fail criterion: the C_2 structure is compatible with the
    prefactor-free scheme as easily as with the symmetric one (no
    selection).
```

Evaluation rules fixed in advance:

- "C_2-Tate constructions" is read as the three constructions that
  exist in the literature for the genuine C_2-spectrum THR(F_p):
  (T1) the reflection Tate THR(F_p)^{tC_2} (Tate of the underlying
  spectrum with the Weyl C_2 = reflection action);
  (T2) the C_2-parametrized S^1-Tate TPR(F_p) := THR(F_p)^{tC_2 S^1}
  (Quigley-Shah's real periodic homology -- the real refinement of TP,
  i.e. the O(2)-relative construction);
  (T3) the parametrized mu_p-Tate THR^{t_{C_2} mu_p} (the real
  cyclotomic Frobenius target, dihedral D_{2p}; this is the
  finite-place machine, listed for completeness, not an archimedean
  candidate).
- "Weight grading": the x-power grading of DMPR's Theorem 5.18 (the
  real refinement of the Bokstedt grading used by docs 18-20); weights
  are read on fixed-point/Tate objects through the restriction map to
  underlying THH/TP, where the doc-19/20 dictionary lives.
- The fold target shape, from gate (infty-1): half-line {n >= 0},
  start 0, spacing doubled relative to the unfolded grading.
- FAIL-CLOSED: if no Tate-type construction folds, say so; a fold
  carried by a different functor is reported as a carrier relocation,
  not as a pass of r1-as-posed.

## 2. Inputs transcribed (theorem numbers; all from archived PDFs)

Conventions: pi_{s,t} = [S^{s,t}, -]^{C_2}, S^{s,t} = S^{t sigma} ^
S^{s-t}; total degree s, weight t; rho = 1 + sigma (regular rep), so
bidegree (2,1) = degree rho.

- [DMPR Thm 5.18]: TH_{F_p}(S^{2,1}) -> THR(F_p) is an equivalence of
  C_2-ring spectra, i.e. THR(F_p) = V_{n>=0} Sigma^{2n,n} HF_p, and
  pi_{*,*} THR(F_p) = (HF_p)_{*,*}[x~], |x~| = (2,1). The Bokstedt
  generator x in pi_2 THH(F_p) is res(x~): the circle weight n is
  refined to the RO(C_2)-degree n*rho. (Same for any perfect k of
  char p by [QS21 Prop 6.26] = [DMP21 Rem 5.14 extended].)
- [DMPR Cor 5.19] (p odd): pi_* (THR(F_p)^{C_2}) = F_p[y], |y| = 4,
  res(y) = x^2; proof via (HF_p)_{*,*} = F_p[u^{+-1}], u in bidegree
  (0,2) [HK01 p. 338], y = u^{-1} x~^2.
- [DMPR Cor 5.20] (p = 2): pi_* (THR(F_2)^{C_2}) = F_2[xbar, y],
  |xbar| = 2, |y| = 1; xbar = x~u -> x, y = x~a -> 0 (a = Euler class).
- [DMPR Prop 5.22]: Phi^{C_2} THR(F_p) contractible for p odd;
  pi_* Phi^{C_2} THR(F_2) = F_2[w_1, w_2], |w_i| = 1.
- [QS21 Def 6.3]: TCR^-(X) := X^{hC_2 S^1}, TPR(X) := X^{tC_2 S^1}
  (C_2-parametrized homotopy-fixed/Tate constructions for the
  parametrized circle; underlying objects are TC^-, TP).
- [QS21 Sec 6.1, opening] (p odd): (HF_p)^{tC_2} = 0 and
  Phi^{C_2} HF_p = 0, "so the same holds for THR(HF_p)": THE
  REFLECTION TATE IS CONTRACTIBLE AT ODD p, and THR(F_p) is Borel
  torsion and Borel complete. [QS21 Lem 6.4]: TCR^-(HF_p), TPR(HF_p),
  TCR(HF_p) are Borel torsion and Borel complete.
- [QS21 Thm 6.5 / Thm 6.6]: TCR(HF_p) = HZ_p + Sigma^{-1} HZ_p (all p).
- [QS21 Prop 6.13 = HK01 Prop 6.2]: (HF_2)_{*,*} = F_2[tau, rho'] +
  (F_2[tau, rho']/(tau^inf, rho'^inf)){theta}, |tau| = (0,-1),
  |rho'| = (-1,-1), |theta| = (0,2).
- [QS21 Prop 6.14]: (HF_2)^{tC_2 S^1} has pi_{*,*} =
  (HF_2)_{*,*}((u)), |u| = (-2,-1), with x u = 1: THE PARAMETRIZED
  TATE PERIODICITY CLASS HAS DEGREE rho, not 2.
- [QS21 Thm 6.20]: pi_*^{C_2} TCR^-(HF_2) and pi_*^{C_2} TPR(HF_2)
  explicitly (Z_2[tau^2 u^{-2}, rho' u^{-1}]/(2 rho' u^{-1}){1} +
  Z/2{theta u^2} + F_2-families for TPR).
- [QS21 Rem 6.23]: abstract isomorphisms of RO(C_2)-graded groups
  pi_{*,*} TCR^-(HF_2) = (HZ_2)_{*,*}[x, u]/(xu - 2),
  pi_{*,*} TPR(HF_2) = (HZ_2)_{*,*}[u^{+-1}]  -- the real refinements
  of TC^-(F_2) = Z_2[x,u]/(xu-2) and TP(F_2) = Z_2[u^{+-1}], with the
  generators in degree +-rho.
- [QS21 Rem 6.24] (p odd): (HF_p)_{*,*} is sparse; the x-adic spectral
  sequences for TCR^-(HF_p), TPR(HF_p) have E_2 =
  (+)_{i} (HF_p)_{*,*}[[u]]{x^i} and collapse at E_2; extensions as at
  p = 2.
- [HW Thm A, Thm 1.8] (arXiv:1911.05687): THR(F_2) as a Hopf
  algebroid (x primitive of degree rho over the comodule algebra
  F_2[a, u]); consequence: N_{C_2} F_2 is Borel complete (the C_2
  Segal conjecture, reproved). Used here only as the p = 2 landscape.
- [DMP21 arXiv:2106.04891]: TCR(Hk) for perfect fields via the genuine
  real-cyclotomic approach; geometric-fixed-point formulas. No
  reflection-Tate of THR(F_p) is computed there either (checked).

## 3. Computation, p odd (the clean case)

### 3.1 (T1) The reflection Tate: ZERO

Transcription [QS21 Sec 6.1]: THR(F_p)^{tC_2} = 0. (Mechanism, for the
record: the underlying spectrum with its Weyl action is a Borel
HF_p-module with trivial action on HF_p, so the Tate construction is a
module over HF_p^{tC_2}, whose homotopy is Tate cohomology
H-hat^*(C_2; F_p) = 0 since 2 is invertible.) Also Phi^{C_2} = 0
[DMPR Prop 5.22]. The pre-registered carrier of r1 carries NO ladder:
nothing to fold. r1 fails on (T1) by vanishing, not by mis-shape.

### 3.2 The genuine fixed points: THE FOLD IS HERE

[DMPR Cor 5.19]: pi_* THR(F_p)^{C_2} = F_p[y], |y| = 4, res(y) = x^2.
Since Tate and geometric fixed points both vanish, the Tate square
gives THR(F_p)^{C_2} = THR(F_p)^{hC_2}; cross-check (derivation, mine):
x~ has weight 1, so the Weyl generator acts on res(x~) = x by
(-1)^1 = -1 (a class in pi_{s,t} restricts to an underlying class on
which the Weyl action is (-1)^t: the action on the S^{t sigma} factor
of the source sphere has degree (-1)^t). The HFPSS
H^*(C_2; F_p[x]) => pi_* THR^{hC_2} collapses (p odd), leaving the
invariants F_p[x^2] in degrees 4n -- matching F_p[y] exactly.

THE FOLD, read through the weight dictionary: the THH(F_p) weight
ladder {n >= 0} (x^n, degree 2n) folds to

    {2n : n >= 0}        (y^n = x^{2n}, degree 4n)

-- HALF-LINE, START 0, SPACING DOUBLED. This is precisely the
Gamma_C -> Gamma_R ladder fold of gate (infty-1) (the Gamma_C-shaped
input {n >= 0, spacing 1} mapping onto its even sub-ladder), and the
selection mechanism is literally Serre's recipe at a real place: the
reflection acts on the weight-n line by (-1)^n, and the fixed sector
keeps the F_infty-eigenvalue-(+1) classes (even n), discarding the
(-1) classes (odd n) -- the Gamma_R(s) vs Gamma_R(s+1) split.
Multiplicative shadow (dictionary remark): the folded local supply
sum_{n} log p * p^{-2ns} is the supply of (1 - p^{-2s})^{-1} =
[(1-p^{-s})(1+p^{-s})]^{-1}: the fixed sector computes the NORM over
the conjugate pair of characters -- eigenvalue pairing in
multiplicative form (relevant to r3).

### 3.3 (T2) The dihedral / parametrized S^1-Tate TPR: full ladder, no fold

From [QS21 Rem 6.23/6.24] the RO(C_2)-graded answer is Laurent on an
invertible class of degree rho over (HZ_p)_{*,*}. Integer-graded
shadow (derivation, mine, two independent routes agreeing):

(a) Borel route: TPR(HF_p) is Borel complete [QS21 Lem 6.4], so
    pi_*^{C_2} TPR = pi_* (TP(F_p)^{hC_2}) with the residual Weyl
    action on pi_* TP(F_p) = Z_p[v^{+-1}]. The Tate class is the
    restriction of a weight-(-1) class [QS21 Prop 6.14], so the Weyl
    action is v -> -v; p odd, HFPSS collapses; invariants
    Z_p[v^{+-2}], degrees in 4Z.
(b) x-adic route: the E_infty of [QS21 Rem 6.24] has integer-degree
    monomials x^i u^j tau-classes exactly in degrees 4Z, with the
    Z_p-extensions as at p = 2.

So

    pi_*^{C_2} TPR(F_p) = Z_p[w^{+-1}], |w| = 4, res(w) = v^2 (up to
    unit):   FULL ladder {2n : n in Z}, spacing doubled, NOT folded
    to a half-line.

Likewise pi_*^{C_2} TCR^-(F_p) = Z_p[a, b]/(ab - p^2), |a| = 4,
|b| = -4 (invariants Z_p[u^2, v^2] of TC^-(F_p) = Z_p[u,v]/(uv - p)
under u -> -u, v -> -v). The real/dihedral refinement of the
TP-machine DOUBLES the spacing but does NOT truncate the ladder to a
half-line. (T3), for completeness, is the real cyclotomic Frobenius
target and reproduces the finite-place rotation machinery [QS19 Sec
6-7]; it is not a fold candidate and was not registered as one.

### 3.4 Summary table, p odd (weights via restriction)

```text
object                       homotopy (fixed/integer)    weight ladder
THH(F_p)        (input)      F_p[x],  |x| = 2            {n >= 0}, sp 1
TP(F_p)         (input)      Z_p[v^{+-1}], |v| = 2       Z, sp 1
THR^{tC_2}      (T1)         0                           NONE
THR^{C_2}=^{hC_2}            F_p[y],  |y| = 4            {2n: n>=0}, sp 2  <- THE FOLD
TPR^{C_2}       (T2)         Z_p[w^{+-1}], |w| = 4       2Z, sp 2
TCR^{-,C_2}                  Z_p[a,b]/(ab - p^2)         two-sided, sp 2
```

The orbit dichotomy of doc 20 sec 3 is realized as a FUNCTOR
dichotomy: at free rotation orbits the ladder-completing functor is
Tate (THH -> TP, half -> full: the duality completion); at the
reflection (the subgroup with fixed points on the circle) the
ladder-folding functor is genuine FIXED POINTS, and the Tate
construction there is zero. Half-line vs full line is decided by the
connective side (THR vs TPR), exactly as non-equivariantly (THH vs
TP); the real structure contributes the spacing-doubling and the
even-eigenvalue selection. The archimedean recipe (half-line, start 0,
spacing 2) = fixed points of the CONNECTIVE real object -- the
archimedean sector is the one place where one must NOT Tate-complete,
which matches Deninger's degenerate (uncompleted) half-ladder at
infinity (doc 20 sec 3) and the absence of a residual circle action on
the reflection-fixed sector (the centralizer of a reflection in O(2)
is finite: the flow honestly degenerates there).

## 4. Computation, p = 2 (the residue characteristic of the C_2)

- Fixed points DO NOT fold cleanly: pi_* THR(F_2)^{C_2} = F_2[xbar, y]
  with |xbar| = 2, |y| = 1 [DMPR Cor 5.20] -- classes in EVERY degree
  >= 0; the Euler class a (nonzero only at p = 2) produces the
  y-family and destroys the even-weight selection.
- Phi^{C_2} THR(F_2) = F_2[w_1, w_2], |w_i| = 1 [DMPR Prop 5.22].
- THR(F_2)^{tC_2} is NOT zero ((HF_2)^{tC_2} != 0) and is NOT computed
  in any source found (DMPR, QS19, QS21, HW, DMP21 all checked; QS21
  compute the parametrized S^1-Tate instead). MISSING COMPUTATION,
  precisely: the Tate spectral sequence
  H-hat^*(C_2; pi_* THH(F_2)) = F_2[t^{+-1}] (x) F_2[x] =>
  pi_* THR(F_2)^{tC_2} (Weyl action trivial on homotopy mod 2;
  differentials unknown -- they encode the k-invariants of the Borel
  C_2-structure, i.e. the non-formality that HW's Hopf-algebroid data
  should control). Three corners of the Tate square are known
  (THR^{C_2}, Phi^{C_2}, and THR^{hC_2} via the same unknown
  differentials); resolving it is a finite, well-posed computation.
- p = 2 reading (observation, not a claim): the clean fold exists
  exactly when 2 is invertible -- the reflection sector behaves like
  "the archimedean place seen away from 2". DMPR's THR(Z)[1/2] =
  HZ[1/2] v V_k Sigma^{2k-1,k} H(Z/k)[1/2] refines doc 18's torsion
  ladder Z/k, deg 2k-1, weight k to RO-degree k*rho - 1: the canonical
  circle weight of docs 18-19 is genuinely a REAL (sigma-multiplicity)
  weight away from 2. The same fold analysis applies verbatim there.

## 5. Verdicts

### r1: FAIL as pre-registered; the fold exists with carrier relocated
###     to the genuine fixed points (post-hoc reading, flagged)

The C_2-Tate construction does not fold the weight grading: (T1) is
contractible at odd p (no ladder at all), nonzero but uncomputed at
p = 2; (T2) TPR retains the FULL ladder with doubled spacing (no
half-line truncation). FAIL-closed on the registered carrier. The
pre-registered fold SHAPE -- Z-half-line, start 0, spacing doubled --
is exactly realized by THR(F_p)^{C_2} (= ^{hC_2}) at odd p
[DMPR Cor 5.19], with the even/odd eigenvalue selection of Serre's
real-place recipe. This is a carrier correction of the same kind as
doc 20's C1 (ladder vs scheme): the gate (infty-1) should read "the
REFLECTION-FIXED sector carries the folded half-ladder; the
reflection-TATE sector is zero". The THR candidate survives, sharpened,
NOT killed: the fail is in which functor was named, not in the
geometry (the fold is local and reflection-driven, as the J-doc
anticipated; "Tate" was the wrong completion to ask for at a fixed
point, and its vanishing is itself the structural signature that
duality completion must not happen at the archimedean sector).

### r2: PASS on the fixed-point carrier; FAIL on the Tate carriers
###     (conditional exactly as r1)

The folded fixed-point ladder {s + 2n : n >= 0} has regularized
characteristic function prod_reg_{n>=0}(s + 2n) =
2^{(1-s)/2} sqrt(2pi)/Gamma(s/2) (witness W1) -- the Gamma_R shape --
with anomalous dimension zeta_H(0, s/2) = (1-s)/2 != 0 (witness W2a:
the value scales as kappa^{-(1-s)/2}), as gate (infty-2) demands. The
Tate-side objects give the wrong answer: TPR's full folded ladder has
anomalous dimension 0 (witness W2b: the symmetric-scheme value
2 sinh(ell z/2) is exactly scale-free), and (T1) has no characteristic
function. So the half-ladder/anomalous-dimension signature follows
from the fixed-point fold and ONLY from it. (The 1/(2pi) scale itself
-- gate (infty-2)'s second half -- is still not produced by anything
here; at F_p the folded ladder is a weight ladder, not an eigenvalue
ladder, and the scale is data the compactified object must supply,
unchanged from J-doc C2.)

### r3: CONDITIONAL PASS -- a selection lemma with one explicit
###     unproven hypothesis

LEMMA (derivation, mine; witness W3). Parametrize the regularization
schemes on the full vertical ladder L(alpha) = {alpha + (2 pi i/log q)
Z} by their vacuum term: D_c(s) = q^{c(s-alpha)}(1 - q^{-(s-alpha)}),
c in R. (This family is exactly what the three-scheme comparison of
prime_int_deninger_convention.py G4 exhibits: c = 0 is the
Deninger/Hesselholt arg-convention scheme, c = 1/2 the
conjugation-symmetric scheme, and any two schemes differ by the
half-sum ambiguity q^{c(s-alpha)}.) The reflection acts on the ladder
data by inverting the flow, Theta -> -Theta, i.e. on the
characteristic variable by w := s - alpha -> -w. Writing f_c(w) :=
D_c(alpha + w) = q^{cw}(1 - q^{-w}):

    f_c(-w) = -q^{(1-2c)w} f_c(w)     (exact identity),

so f_c has definite parity under the reflection iff c = 1/2 (odd
parity; f_{1/2}(w) = 2 sinh(w log q / 2), the KMS-1/2 / self-dual
scheme). A reflection-EQUIVARIANT scheme -- one rule, applied
uniformly, commuting with ladder inversion -- is therefore unique, and
it is the symmetric one. Verified numerically on a (q, w, c) grid
(witness W3, defect < 1e-13 iff c = 1/2).

HYPOTHESIS H-r3 (open; this is what separates the lemma from a
theorem): the C_2-real structure of THR acts on the analytic
determinant layer by ladder inversion, and the determinant assigned to
the real object must be C_2-equivariant. What IS homotopy-theoretic:
the reflection conjugates the rotation flow (g lambda_theta g^{-1} =
lambda_{-theta} in O(2), realized genuinely by THR's C_2-structure
[DMPR Sec 2; QS19]), and the fixed-point fold of sec 3.2 shows this
C_2 genuinely reaches the weight grading (it implements the
even-eigenvalue / conjugate-pair selection -- sec 3.2's norm-factor
remark (1-p^{-2s}) = prod over the conjugate pair is eigenvalue
pairing in multiplicative form). What is NOT: there is no determinant
layer on spectra at all (that is the whole C5'' gap), so no theorem
can currently force H-r3. CONSISTENCY NOTE (resolving the J-doc's
Spec F_q kill within the real setting): no contradiction with
Hesselholt's Theorem A -- Theorem A computes the NON-equivariant TP
determinant, where no reflection acts and the arg-convention scheme is
selected; the lemma says only that an invariant built from the REAL
object, if any exists, must carry the symmetric scheme and hence the
q^{s/2} prefactors, i.e. would compute the SELF-DUAL completion of
zeta(Spec F_q) rather than zeta itself. That is exactly the KMS-1/2
normalization the realization spec wants (doc 10 input 4): the scheme
question and the archimedean question remain one question, now with
the selection mechanism isolated in one hypothesis.

## 6. DOF audit (G-INT6)

- Sec 3 fold claims: exact structural identities transcribed from
  published theorems (DMPR 5.19/5.22, QS21 Sec 6); zero free
  parameters once the weight dictionary (weight = x-power, read
  through res) is fixed -- and that dictionary is the SAME one doc 19
  already spent. No new choices; the fold {n} -> {2n} and the
  half-vs-full dichotomy are not fittable (integer gradings).
- Sec 5 r2: the Gamma(s/2) shape and (1-s)/2 are affine-invariant
  consequences of the folded ladder (witnessed); the 1/(2pi) scale and
  the eigenvalue dictionary are NOT derived (unchanged debt).
- Sec 5 r3 lemma: zero free parameters within the stated family; the
  family itself (vacuum-term ambiguity) is pinned by the G4 witness of
  the J-pass. The load-bearing unproven step is H-r3, stated.

## 7. Honest limits

- THR(F_2)^{tC_2}: not computed here or in the literature; precise
  missing computation stated in sec 4. It does not affect the odd-p
  verdicts but is the only way to test whether the p = 2 anomaly
  (Euler-class families, no clean fold) propagates to the Tate level.
- The fold test runs at FINITE places (THR(F_p)), as the J-doc
  pre-registered ("decisive orientation; the fold is local"). Nothing
  here constructs the archimedean object: the compactified real square
  with a reflection sector over Spec Z does not exist, and the
  RO(C_2)-refinement of THR(Z) at the prime 2 (where the reflection
  sector is interesting) is still open even at the THR level (DMPR
  compute it only away from 2 + geometric fixed points).
- Weights on folded objects are read through res; there is no residual
  circle action on the reflection-fixed sector (centralizer
  finiteness), so "weight" there is inherited, not intrinsic. I regard
  this as structurally correct for the archimedean reading (the flow
  degenerates at the fixed point), but it is a reading, not a theorem.
- r3 remains conditional on H-r3; no claim that homotopy theory
  currently selects the symmetric scheme.
- No RH/zero-side input anywhere; all sources are supply-side
  homotopy theory.

## 8. Next steps (ranked)

1. Gate (infty-1) REVISED for the lead to adopt: replace "Tate-type
   construction at a reflection C_2" by "genuine fixed points at a
   reflection C_2 of the connective real object" (sec 3.4 dichotomy);
   the Tate construction's vanishing at the reflection should be
   listed as a positive structural check (no duality completion at
   the archimedean sector), not a defect.
2. THR(F_2)^{tC_2} via the Tate square + HW's Hopf-algebroid control
   of the differentials (finite computation; tests the p = 2 anomaly).
3. H-r3 hunt: the only existing candidate for a determinant-bearing
   layer with an involution is the characteristic-polynomial /
   Witt-vector package with anti-involution (DMP arXiv:1901.02195,
   Witt vectors with coefficients; TR with its real structure) --
   pose: does the real structure on TR(F_p) force the symmetric
   scheme on the characteristic polynomial of Frobenius? That is a
   finite question one rung below Deninger's det_inf.
4. The archimedean object proper: the fold mechanism now being
   fixed-points-of-connective-real, the C5''' properness vehicle
   (log-THH residue sequences, CC's S) should be probed for a REAL
   (C_2/O(2)-equivariant) refinement -- the reflection sector of a
   compactified THR(Z) is the carrier this test points at.
