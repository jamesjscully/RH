# O - H-r3 formulated, split, and half-discharged: the analytic half is a theorem (scheme rigidity), the homotopy half is isolated as a single negation-supply lemma that NO currently computed C_2-structure provides

Status: fresh-context worker O, 2026-06-10. Required reading executed in
order (docs 20 incl. CORRECTION sections, 21 secs 2-3, 24; J-doc secs 4-5;
M-doc parity lemma / H-r3 / TPR derivation). Primary sources re-read at the
load-bearing points: Hesselholt arXiv:1602.01980 Sec 7 (det_inf definition,
Prop 7.1, Rem 7.2; refs/hesselholt2016.txt read verbatim), Deninger 1992
Invent. 107 Convention (2.1)-(2.2) + Prop 2.3 incl. the proof's branch steps
(refs/deninger1992-local-l-factors.pdf pp. 142-143 read from the scan).
Witness (NEW, ALL PASS, exit-code gated):
scripts/numerics/witness/prime_int_hr3_scheme_rigidity.py (gates G1-G7,
pre-registered readings R-G1..R-G7 in the docstring).

HEADLINE. H-r3 splits cleanly into an analytic half and a homotopy half,
and the split is NOT where doc 24 put it.

- ANALYTIC HALF: PROVED (Theorem A1 below, elementary but airtight):
  negation-naturality of the regularized determinant forces the vacuum
  slope c = 1/2 - the symmetric/KMS-1/2 scheme - uniquely within the
  zeta-regularization class, up to an EF-invisible constant. Strengthened
  by Lemma A0 + Corollary A2 (new): EVERY pointwise branch convention
  (Deninger's, Hesselholt's, and all window variants) has INTEGER vacuum
  slope, so no branch convention whatsoever can produce KMS-1/2 - the
  symmetric scheme is not a branch choice but a C_2-average, and it
  requires a square root lambda^{1/2} of the Frobenius eigenvalue
  (Prop A6: the symmetric det lives on a DOUBLE COVER of the eigenvalue
  space - a new, 2-primary structural pointer).
- HOMOTOPY HALF: NOT DISCHARGED, and sharpened into an obstruction
  report. The C_2-structures actually computed in the literature act on
  the eigenLINES of the determinant input (by signs), not on the ladder
  POINTS; every one of them either commutes with the determinant data
  (forcing nothing - Obstruction O-1: the residual Weyl action v -> -v
  is VACUOUS for the scheme question) or yields only the Schwarz
  reflection constraint (which Prop A4 shows selects nothing). What
  H-r3 needs is LADDER NEGATION (Theta -> -Theta covering s -> -s),
  i.e. reversal of the FROBENIUS FLOW circle; the real cyclotomic C_2
  reflects the TATE circle and is Frobenius-EQUIVARIANT, not
  Frobenius-inverting. The residue is one precisely stated lemma
  (H-r3-min, sec 4.6) plus one fork (F1) about whether the
  inversion-twist on C_p in the real cyclotomic structure reaches the
  determinant layer. Doc 24's wording of H-r3 is UNDER-SPECIFIED: as
  written ("the C_2 acts on the analytic determinant layer") it is
  satisfiable by the existing linear action and then forces nothing;
  the forcing version must demand negation. Proposed rewording in
  sec 5.

Guards observed: no RH/zero-side input (one purity warning flagged where
it threatens, sec 4.5); DH/Epstein carrier guard stated for the analytic
half (sec 3.8 - the analytic theorem is deliberately carrier-blind, so
carrier discrimination must come entirely from the homotopy half);
G-INT6 DOF ledger in sec 6.

## 0. Conventions and one name-collision warning

Throughout: q = p^r, t := 2 pi / log q, ladder variable w := s - alpha
(alpha a choice of log_q of the Frobenius eigenvalue lambda = q^alpha),
full vertical ladder

    Lambda_w := { w + i t nu : nu in Z }  (the det_inf input multiset of
    s id - Theta on one Frobenius eigenclass; Hesselholt Rem 7.2).

Scheme family (M-doc r3, pinned by J-doc witness G4):
f_c(w) = q^{cw}(1 - q^{-w}); c = 0 is Deninger/Hesselholt, c = 1/2 is
the symmetric/KMS-1/2 scheme, f_{1/2}(w) = 2 sinh(w log q / 2).

NAME COLLISION (load-bearing): the task brief's "C_2 ... inducing
w -> -w on the TPR ladder" overloads "w". The RING generator
w = v^2 in pi_*^{C_2} TPR(F_p) = Z_p[w^{+-1}] (M-doc sec 3.3) is FIXED
by the involution: the Weyl action is v -> -v, so g(v^2) = (-v)^2 = v^2.
There is no "w -> -w" on the ring generator; on the FIXED-POINT ring the
residual action is trivial by construction. The only meaningful reading
of "w -> -w" is on the DETERMINANT VARIABLE w = s - alpha, i.e. ladder
negation Lambda_w -> -Lambda_w = Lambda_{-w}; that reading is exactly
the open homotopy half analyzed below. Every "w" below is the
determinant variable unless explicitly marked "ring generator".

## 1. FORMULATION of H-r3

### 1.1 (a) The object carrying the determinant layer

Exact transcription (Hesselholt Sec 7 + Cor 6.9; Deninger 1992 Sec 1-2):

- Input category: X smooth proper over k = F_q; W = W(k); a CHOICE of
  embedding iota: W -> C.
- The determinant layer of X is the pair

      DetIn(X) := ( V_X := TP_*(X) (x)_{W,iota} C  (graded, od/ev split),
                    Theta_X : V_X -> V_X ),

  where Theta_X is a C-linear graded derivation solving q^{Theta} =
  Fr_q^* with Theta(v) = (2 pi i / log q) v on the periodicity class
  v in TP_{-2}(k) (Hesselholt Thm A statement; the log-multivaluedness
  ambiguity is (2 pi i/log q) Z per eigenvalue, Rem 7.2). Properness
  enters as finiteness: each TP_j(X) (x) C is finite-dimensional
  (Cor 6.9), so Deninger's conditions (1)-(2) typecheck and the
  generalized eigenspaces of Theta on the 2-periodicized V_X are the
  full vertical ladders Lambda over each Frobenius eigenvalue.
- The analytic functional on this object: Deninger's det_inf, which
  REQUIRES a branch datum - Hesselholt fixes -pi < Arg <= pi
  (Sec 7, "The definition requires a choice of principal branch
  Arg(lambda)"); Deninger 1992 fixes Convention (2.1), arg in
  (-3 pi/2, pi/2] - and the choice is exactly the scheme (doc 20 C1).
- COMPLETION CAVEAT (BMS obstruction, J-doc sec 2): this object exists
  at finite places only; everything is p-complete and Frobenius-linear
  only over F_q. H-r3 is posed at this finite-place carrier, as the
  local shadow of the archimedean mechanism (same fork discipline as
  the M-doc fold test).

### 1.2 (b) What the C_2 acts on - the candidate actions, inventoried

The real refinement THR(F_q) (DMPR) is a genuine C_2-spectrum; the
parametrized constructions TPR = (-)^{t_{C_2} S^1} (QS21 Def 6.3)
refine TP. The C_2-structures that are THEOREM-GRADE in the literature,
with their precise shadows on DetIn:

```text
(i)   residual Weyl action W(O(2)/S^1) = C_2 on TP:   v -> -v
      [QS21 Prop 6.14: the parametrized Tate class has RO(C_2)-degree
      rho; M-doc 3.3(a)].  On V_X: the C-LINEAR map acting on the
      weight-m line by (-1)^m.
(ii)  the involution on THH-weights: (-1)^k on pi_{2k} THH(F_p)
      [DMPR, doc 24 sec 1].  Same shape: signs on lines.
(iii) real cyclotomic Frobenius: phi is a map of C_2-spectra (the C_2
      acts on the target Tate construction through INVERSION on
      C_p < S^1: sigma c sigma^{-1} = c^{-1}) [DMPR Sec 2; QS19].
      Shadow on DetIn: Fr_q^* COMMUTES with the C_2-action.
(iv)  the orientation statement: the reflection conjugates the rotation
      one-parameter subgroup to its inverse, g lambda_theta g^{-1} =
      lambda_{-theta} in O(2) (group theory; genuinely realized by the
      C_2 of THR).
```

What H-r3 NEEDS the C_2 to do on DetIn (this is the candidate named in
the task, made precise): act by LADDER NEGATION,

    N: (V, Theta) |-> (V, -Theta)   covering   s |-> -s,

equivalently invert the multiplicative Frobenius data q^{Theta} |->
q^{-Theta} together with the vertical lattice orientation. On the
eigenvalue multiset: Lambda_w |-> -Lambda_w = Lambda_{-w}; on the
scheme family this is the parity lemma's w -> -w.

### 1.3 (c) The equivariance demand on the det functor

Calibration from finite dimensions: for dim V < infty,
det(s id - (-Theta)) = (-1)^{dim V} det(-s id - Theta) - negation
changes the characteristic function by composition with s -> -s and a
CONSTANT unit. The weakest functoriality demand compatible with this:

    DEF (negation-naturality). A regularization scheme R on the
    vertical-ladder family is negation-natural if there is a constant
    unit u in C^* (allowed to depend on q, NOT on w) with

        R(Lambda_{-w}) = u * R(Lambda_w)   for all w.

    Since -Lambda_w = Lambda_{-w}, this reads f(-w) = u f(w) for the
    scheme value f.

NOTE WHAT IS NOT ASSUMED (anti-smuggling): we do not assume the
continuation is symmetric, self-dual, or KMS-anything; we assume only
that the rule transforms under negation by a constant unit - the shape
forced on any functor that extends the finite-dimensional determinant
and is invariant under isomorphisms of pairs (V, Theta). The symmetry
of the continuation is then DERIVED (Theorem A1). The geometric supply
of the negation map N itself is NOT assumed either - it is exactly the
homotopy half, left open.

### 1.4 H-r3, restated with full precision

    H-r3 (forcing form; replaces doc 24's wording). There exists a
    factorization of Hesselholt's determinant-layer construction
    X |-> DetIn(X) through a C_2-equivariant enhancement, where the
    C_2 is induced by the O(2)/real-cyclotomic structure of THR and
    acts on DetIn by ladder negation N covering s -> -s; and the
    regularized determinant used in Theorem A is natural for this
    C_2 in the sense of 1.3.

    SPLIT:  H-r3 = H-r3(an)  AND  H-r3(hom), where
    H-r3(an): negation-naturality forces the symmetric scheme c = 1/2
        (an assertion about regularized products only);
    H-r3(hom): the geometric C_2 of THR supplies the negation map N on
        DetIn (an assertion about homotopy theory only).

Given both halves, the parity lemma chain closes: real structure =>
negation-naturality => c = 1/2 => KMS-1/2 prefactor q^{w/2} - the
fourth realization input (doc 10) derived rather than chosen.

## 2. REDUCTION: the minimal lemmas

    L-an (scheme rigidity; PROVABLE, proved in sec 3). Any
    negation-natural scheme value in the zeta-regularization class on
    the full vertical ladder equals e^{a} * 2 sinh(w log q / 2) for
    some constant a (EF-invisible), and the unit is forced to u = -1.
    Moreover no pointwise branch convention is negation-natural
    (integer-slope obstruction), and the unique negation-natural value
    is the C_2-average of any branch convention with its C_2-image
    (up to mu_4), fixed exactly by the pair-modulus construction.

    L-hom (negation supply; OPEN - the true residue of H-r3). The
    real/O(2)-structure of THR(F_q) induces on DetIn(Spec F_q) =
    (C[v^{+-1}], Theta), Theta(v^m) = m (2 pi i/log q) v^m, the
    negation isomorphism N covering s -> -s. (Spec F_q is the minimal
    non-circular case: lambda = 1, alpha = 0, no horizontal Frobenius
    data, no purity input needed - see 4.5. If L-hom holds there, the
    general fiberwise statement follows on each unitarized eigenclass,
    with the purity caveat of 4.5 for the unitarization.)

If L-hom is proved, H-r3 is discharged by L-an and the doc-24 chain
closes; the scheme question reduces to pure homotopy theory, namely
L-hom. The rest of this doc proves L-an (sec 3) and shows why L-hom is
not currently provable, locating exactly what is missing (sec 4).

## 3. THE ANALYTIC HALF: proofs

### 3.1 Setup: schemes as branch data

A zeta-regularized product over an admissible multiset Lambda needs,
for its definition, a branch assignment beta: Lambda -> R with
beta(lambda) in arg(lambda) + 2 pi Z, since lambda^{-sigma} :=
e^{-sigma(log|lambda| + i beta(lambda))}; then zeta_{Lambda,beta}(sigma)
= sum lambda^{-sigma}, continued, and D = e^{-zeta'(0)}. Two
elementary facts (proofs immediate from d/dsigma e^{-sigma L}|_0 = -L):

- (finite invisibility) changing beta by 2 pi k on FINITELY many points
  multiplies D by e^{2 pi i k} = 1: only the asymptotic window matters.
- (window data) the vertical ladder has two ends, nu -> +-infinity,
  where arg(w + i t nu) -> +-pi/2; an "eventually windowed" scheme is
  classified by the end sheets (a_+, a_-) in Z^2:
  beta -> pi/2 + 2 pi a_+ (upper end), -pi/2 + 2 pi a_- (lower end).

### 3.2 Lemma A0 (window classification). [witness G1, 3e-15]

For every (a_+, a_-) in Z^2, the windowed scheme value on Lambda_w is

    D_{a_+,a_-}(w) = (-1)^{a_+ + a_-} q^{-(a_+ - a_-) w} (1 - q^{-w}).

PROOF. Split nu = 0 / nu >= 1 / nu <= -1. With a := -i w / t:
upper sum = e^{-sigma L_+} zeta_H(sigma, 1 + a), lower sum =
e^{-sigma L_-} zeta_H(sigma, 1 - a), L_+- = log t + i(+-pi/2 + 2 pi
a_+-) (the modulus |w + i t nu| ~ t|nu| and the eventually-constant
window give exactly these prefactors; finitely many small-|nu|
deviations are invisible by 3.1). Using zeta_H(0, x) = 1/2 - x and
zeta_H'(0, x) = log Gamma(x) - (1/2) log 2 pi:

    D = w * exp[L_+ (-1/2 - a) + L_- (-1/2 + a)]
          * (2 pi) / (Gamma(1 + a) Gamma(1 - a)).

Gamma(1+a)Gamma(1-a) = pi a / sin(pi a), so the Gamma block is
2 sin(pi a)/a; w/a = i t; (L_+ + L_-)/2 = log t + i pi (a_+ + a_-);
L_+ - L_- = i pi (1 + 2(a_+ - a_-)). Assembling, with e^{-2 pi i a} =
e^{-2 pi w / t} = q^{-w}:

    D = (-1)^{a_+ + a_-} e^{-2 pi i a (a_+ - a_-)} (1 - e^{-2 pi i a})
      = (-1)^{a_+ + a_-} q^{-(a_+ - a_-) w} (1 - q^{-w}).   QED

Sanity anchors (witnessed): (a_+, a_-) = (0,0) gives 1 - q^{-w} - the
vertical principal branch = Deninger's Convention (2.1) value (J-doc G4
showed these two agree; G1 re-verifies); (0,1) gives -q^{w}(1-q^{-w}),
which will be identified as the C_2-image of Deninger's scheme in 3.5.

### 3.3 Theorem A1 (scheme rigidity / forced vacuum). [witness G2]

Let f(w) = e^{P(w)} (1 - q^{-w}) with P a polynomial (the
zeta-regularization class has deg P <= 1 - the Dirichlet series of the
ladder has abscissa 1, and every construction exhibited here lands in
deg <= 1; the theorem needs no degree bound). If f(-w) = u f(w) for a
constant unit u, then

    P_odd(w) = (log q / 2) w   exactly (all higher odd coefficients 0),
    u = -1,
    P_even free  (within the zeta class: a constant a).

Hence every negation-natural zeta-class scheme value is

    f(w) = e^{a} * q^{w/2} (1 - q^{-w}) = e^{a} * 2 sinh(w log q / 2):

the symmetric/KMS-1/2 scheme, up to the EF-invisible constant e^{a}
(same status as the 2^{+-1/2}'s of doc 20 C3). The vacuum SLOPE -
the only EF-visible scheme datum, and the entire content of the
KMS-1/2 prefactor - is FORCED to c = 1/2.

PROOF. 1 - q^{w} = -q^{w}(1 - q^{-w}), so f(-w) = u f(w) reads
e^{P(-w) - P(w) + w log q + i pi} = u, i.e. -2 P_odd(w) + w log q =
const. A polynomial identity: P_odd(w) = (log q/2) w and the constant
is 0, whence u = e^{i pi} = -1. QED

REMARK (why u must be constant): in finite dimensions the unit is
(-1)^{dim V}, independent of s; allowing u = u(w) would permit every
scheme (take u = f(-w)/f(w)) and is not functoriality of anything.

### 3.4 Corollary A2 (NEW; strengthens the J-doc separation). No
pointwise branch convention - no choice of argument window whatsoever,
Deninger's, Hesselholt's, or any other - is negation-natural, and none
can ever produce the KMS-1/2 prefactor: by A0 their vacuum slopes are
INTEGERS, and by A1 naturality demands slope 1/2. The symmetric scheme
is not a "better branch choice"; it is not a branch choice at all.
[This upgrades doc 21's T-a from "the existing theorem selects the
prefactor-free scheme" to "the prefactor CANNOT be selected by any
convention of the kind the existing theorems use".]

### 3.5 Proposition A3 (where Deninger breaks the symmetry, exactly).
[witness G1, G3]

Deninger's Convention (2.1) (Invent. 107 p. 142, read from the scan):
"arg(z + a_nu) in (-3 pi/2, pi/2] for |nu| >> 0", operationalized in
(2.2): arg(z - nu) = arg(nu - z) - pi, and used in the Prop 2.3 proof
step prod_{nu>=1}(z - nu) = prod e^{-i pi}(nu - z), extracting the
phase e^{-i pi (zeta(0, -z) - 1)}. The orientation choice is the
"- pi": at the NEGATIVE end of the (rotated) ladder he assigns the
-pi sheet rather than +pi - i.e. he picks a generator of the deck
group of the log cover, equivalently an orientation of C \ {0},
equivalently an orientation of the orbit circle. Under negation
z -> -z the two ends swap and the window (-3 pi/2, pi/2] maps to
(-pi/2, 3 pi/2] - a DIFFERENT convention (the +pi sheet): no single
window is negation-stable, which is Corollary A2 in convention form.

The C_2-IMAGE of Deninger's scheme is the (0,1)-window scheme of A0:
P_-(w) = 1 - q^{w} = -q^{w} (1 - q^{-w}) (slope 1, the "miracle"
identity run with the opposite orientation). The C_2-AVERAGE:

    sqrt( P_+(w) P_-(w) ) = (mu_4 unit) * q^{w/2} (1 - q^{-w}),

(witness G3: the unit lands in {+-i} on the tested grid - the
ambiguity of regularizing the sign count, (-1)^{zeta(0,.)}, a fourth
root of unity), while the PAIR-MODULUS construction (doc 20 W3:
pair the ladder point w + i t nu with w - i t nu, regularize the
positive pair products) assembles to exactly + 2 sinh(w log q / 2)
with unit +1 (witness G3, tail-limited 4e-7). So: symmetric scheme =
geometric mean of Deninger and his mirror, with the mu_4 torsion
resolved by the pair construction.

### 3.6 Proposition A4 (conjugation selects NOTHING - a correction to
the program's gloss). [witness G4]

The internal involution of a single ladder (real w): conjugation
lambda -> conj(lambda), i.e. nu -> -nu with w fixed, maps Lambda_w to
itself. Naturality under IT is the Schwarz reflection f(conj w) =
conj f(w) - and EVERY real-c scheme satisfies Schwarz (witness G4,
exact). In particular the principal window (c = 0, prefactor-free) is
perfectly conjugation-natural. Therefore the recurring gloss "the
symmetric scheme is the regularization respecting a real structure
(eigenvalues paired with conjugates)" (doc 20 C1, J-doc sec 4) is
IMPRECISE in a way that matters: pairing-with-conjugates is satisfied
by the scheme that Hesselholt's theorem selects, prefactor-free. The
selecting involution is NEGATION Lambda -> -Lambda (w -> -w), which on
a centered eigenclass is the LOCAL FUNCTIONAL-EQUATION flip - not
conjugation. Any future derivation that obtains c = 1/2 from
conjugation alone is wrong or circular. (This sharpens, not
contradicts, the M-doc: its parity lemma already used w -> -w; what it
glossed as "pair each eigenvalue with its conjugate" is the harmless
half of the structure.)

### 3.7 Proposition A5 (principal-value characterization). [witness G5]

The balanced truncations, renormalized by w-INDEPENDENT constants,
converge to the symmetric scheme and to nothing else:

    prod_{|nu| <= N} (w + i t nu) / prod_{1 <= nu <= N} (t nu)^2
        -> (2 / log q) * sinh(w log q / 2)   (N -> infinity),

with exact oddness at every finite N (witness G7: P_N(-w) = -P_N(w),
machine-exact - negation-naturality is the regularized shadow of an
exact finite symmetry, which is why it is the right demand to put on
the continuation). Fixed end-offsets wash out (O(1/N), witness G5);
asymmetric ratio-r truncations [-N, rN] drift by exactly
exp(-i (w/t) log r) (witness G5) - the asymmetry cost is again a
vacuum-slope term. So KMS-1/2 = the Cauchy-principal-value Euler
factor: the unique scheme obtainable as a limit of C_2-balanced finite
windows. (Carrier-blind remark: this is the analytic identity that
doc 20's W3 exhibited; the new content is uniqueness and the exact
form of the drift under unbalancing.)

### 3.8 Proposition A6 (the mu_2 obstruction: KMS-1/2 needs
lambda^{1/2}). [witness G6]

Recentering the ladder by one lattice step (alpha -> alpha + i t,
w -> w - i t; same multiset Lambda, same Frobenius eigenvalue lambda)
FIXES every integer-c scheme - they are functions of lambda alone, as
a determinant of Frobenius data should be (Hesselholt Rem 7.2: the
value depends only on lambda) - but FLIPS THE SIGN of f_{1/2}:
q^{(w - i t)/2} = -q^{w/2}. So the symmetric det is NOT a function of
(s, lambda); it is a function of (s, lambda^{1/2}): single-valued only
on the DOUBLE COVER of the eigenvalue space (equivalently: of the
orbit circle). Consequences:

- any homotopy-theoretic carrier of H-r3 must supply a CANONICAL
  square root of the Frobenius eigenvalue (a 2-primary datum). This is
  the classical metaplectic/Weil 1/2-twist surfacing inside the
  program, and it converges with the program's standing 2-adic/real
  entanglement: the p = 2 anomaly (doc 24 gap ledger), CC's
  distinguished point at 2 (K = -2{2}), and the mu_4 torsion of A3.
- the C_2-average construction (A3) has its mu_4 ambiguity precisely
  because no canonical lambda^{1/2} was chosen; the pair-modulus
  construction resolves it on the REAL-w slice only.

CARRIER GUARD (DH/Epstein): Theorems A0-A6 are pure analysis and are
deliberately carrier-blind - they hold for any ladder of the right
shape, including Epstein-type ladders with no ring under them. The
analytic half must NEVER be cited as carrier-sensitive evidence; all
carrier discrimination in H-r3 lives in the homotopy half (no ring =>
no THR => no geometric C_2 => no forcing), inheriting the M-doc's
P2-grade kill.

## 4. THE HOMOTOPY HALF: obstruction report (honest; nothing faked)

The question: does the geometry supply the negation map N of 1.2?
Answer at every currently computable level: NO - and the failures are
informative. Throughout, DetIn(Spec F_q) = (C[v^{+-1}], Theta),
Theta(v^m) = m (2 pi i / log q) v^m (Bott-power grading; for general X
tensor with the finite-dimensional horizontal data).

### 4.1 Obstruction O-1 (vacuity of the linear residual Weyl action).
[witness G7]

The theorem-grade C_2 on TP (1.2(i)): g(v^m) = (-1)^m v^m, C-linear.
Then g Theta g^{-1}(v^m) = (-1)^m Theta((-1)^m v^m) = Theta(v^m):
g COMMUTES with Theta (g is scalar on each graded line; Theta is
graded), and likewise with Fr_q^* (Fr(v) = v). So g is an internal
automorphism of DetIn, and equivariance of ANY isomorphism-invariant
determinant under it is automatic - for every scheme. The constraint
content of "det is equivariant for the residual Weyl group
W(O(2)/S^1) = C_2" is ZERO. Consequence for doc 24: H-r3 as worded
("the C_2 of THR genuinely acts on the analytic determinant layer ...
the regularized-determinant functor can be made C_2-equivariant") is
TRUE-BUT-VACUOUS under the action that demonstrably exists; in that
reading it permits the symmetric scheme without forcing it - exactly
the failure mode the parity lemma was supposed to overcome. The
forcing version must demand negation (sec 1.4). Same verdict for the
(-1)^k involution on pi_{2k} THH (1.2(ii)): signs on lines.

LINES vs POINTS (the crisp form of the gap): the computed C_2 acts on
the eigenLINES of the determinant input and acts TRIVIALLY on the
ladder POINT SET. Acting on lines is exactly what the FOLD needs (the
fixed sector keeps the (+1)-lines: doc 24 sec 1, Serre's F_infinity
selection - real work, done by this action). Acting on points
(negation) is what the SCHEME needs - and no computed structure does
it. The fold question and the scheme question, which gate C5''-infty
listed side by side as (infty-1') and (infty-3'), are therefore
structurally INDEPENDENT: solving one does not advance the other.

### 4.2 Obstruction O-2 (the antilinear reading gives only Schwarz).

If the real structure is read iota-semilinearly (the C_2 covering
complex conjugation through iota: W -> C - the only reading in which
"complex conjugation on the S^1" literally conjugates scalars), then
conjugating Theta by the antilinear g negates the VERTICAL spacing
(g(i v) = -i g(v)) and conjugates the horizontal data: the ladder maps
Lambda -> conj(Lambda). For real alpha this is the INTERNAL conjugation
of 3.6, and the naturality it imposes is Schwarz reflection - which
Prop A4 proved selects NOTHING (the prefactor-free scheme satisfies
it). The antilinear reading is the correct formalization of
"eigenvalues paired with conjugates", and it is exactly as
non-selective as A4 says.

### 4.3 Obstruction O-3 (the real cyclotomic Frobenius is equivariant,
not inverted).

The real cyclotomic structure makes phi a C_2-EQUIVARIANT map
(1.2(iii)): the C_2 commutes with Frobenius. It does not conjugate
Fr to Fr^{-1}. So the horizontal half of negation (alpha -> -alpha,
lambda -> lambda^{-1}) is NOT supplied by THR's C_2 on any eigenclass
with lambda != lambda^{-1}. (For a commutative ring the real structure
comes from the identity anti-involution; the q-power Frobenius is
untouched by it. Nothing in DMPR/QS19/QS21 inverts Frobenius;
checked against the M-doc's transcriptions and the structure maps.)

### 4.4 The two circles (where the M-doc's gloss jumped).

The M-doc r3 justified w -> -w by "the reflection inverts the flow,
g lambda_theta g^{-1} = lambda_{-theta}". The group fact is right
(1.2(iv)) but it concerns the TATE/THH circle, which the Tate
construction CONSUMES: there is no residual circle action on TP, and
Theta is not the generator of one - it is the log-Frobenius, whose
vertical lattice merely REMEMBERS the circle (Hesselholt's "most
general solution" choice; J-doc 1.1). The ladder negation H-r3 needs
is reversal of the FROBENIUS FLOW circle (the orbit circle
R/(log q) Z of doc 20 sec 3 - circumference log q, characters
(2 pi i/log q) Z). These are different circles, and the program has
already once paid for conflating ladder structure with what a functor
actually does (M-doc r1: "Tate" was the wrong functor at a
reflection). The cyclotomic structure is what identifies the two
circles' arithmetic content - which is why the one genuinely open
question (F1 below) is whether the INVERSION-twist on C_p in the real
cyclotomic structure descends to the determinant layer.

### 4.5 Purity warning (zero-side adjacency - flagged, not used).

For general X, negation on a NON-centered eigenclass needs the
unitarization lambda -> lambda / q^{j/2} (center the ladder), i.e.
|lambda| = q^{j/2} - Weil/Deligne purity, which is function-field RH:
zero-side input by the program's standards (doc 21 sec 4 already
flags that Hesselholt imports the FF zeros whole). The MINIMAL case
Spec F_q (lambda = 1) needs no purity: that is why L-hom (sec 2) is
posed there. Any future proof of H-r3(hom) that quietly unitarizes a
general eigenclass has imported purity; on Spec F_q there is nothing
to import. (Also note: the unitarization is itself a lambda^{1/2}-type
twist - the A6 double cover again.)

### 4.6 The residue, stated as precisely as the evidence allows

    L-hom (restated): the O(2)/real-cyclotomic structure of THR(F_q)
    induces on DetIn(Spec F_q) the negation isomorphism
    N: (C[v^{+-1}], Theta) -> (C[v^{+-1}], -Theta) covering s -> -s.

    FORK F1 (the one open mechanism): the real cyclotomic C_2 acts on
    the target of phi_p through INVERSION on C_p (1.2(iii)). Does this
    inversion-twist, pushed through the construction that produces
    Theta (the passage q^{Theta} = Fr* with its orientation choice
    Theta(v) = +(2 pi i/log q) v), negate the determinant input - i.e.
    is the C_2-conjugate of the (V, Theta_+)-solution canonically the
    (V, Theta_-)-solution? Equivalently: does the reflection exchange
    the two orientations of the orbit circle AT THE DETERMINANT LAYER,
    not merely in the group O(2)?

    Evidence inventory: at the level of underlying homotopy groups the
    answer is NO everywhere I can compute (O-1: everything commutes;
    the halves of the ladder are NOT exchanged - the C_2 preserves
    Bott degree, and v^m <-> v^{-m} is degree-inverting, a duality,
    not an automorphism). If F1 has a positive answer it must come
    from the genuine/parametrized layer (the rho-graded periodicity
    u with |u| = rho, x u = 1 [QS21 Prop 6.14] is where the
    reflection-twist of the Tate direction is recorded) or from a
    DUALITY layer not yet in the construction: ladder negation
    restricted to the vertical lattice IS the swap of the two halves
    of the Tate ladder, i.e. exactly the duality-completion symmetry
    (doc 20: the completion generates the full ladder; its two halves
    are TC^--side and cofiber-side). "The reflection acts by the
    duality" is a statement about a COMPACTIFIED/self-dual object -
    which is C5'''s burden, not a property of TP(F_q) alone.
    UNVERIFIED either way; this is the wall, relocated by one step
    and now carrying the A6 constraint: whatever supplies N must also
    supply a canonical lambda^{1/2} (double cover datum), or the
    forced determinant is only defined up to mu_2.

### 4.7 What would discharge L-hom (concrete probes, ranked)

1. F1 at p odd, RO(C_2)-graded: compute the C_2-twisted automorphism
   group of TPR(F_p) over the parametrized sphere and check whether
   the orbit-circle reflection is realized with a nontrivial shadow on
   the (V, Theta) groupoid (the M-doc's route-(a) Borel computation is
   the place to start; the answer at pi_* is "commutes", so the
   content, if any, is in the rho-graded extensions / k-invariants).
2. The M-doc's step-3 candidate sharpened by A6: TR with its real
   structure and the Witt-vector anti-involution (DMP arXiv:1901.02195)
   - pose: does the real structure on TR(F_q) supply the DOUBLE COVER
   (a canonical lambda^{1/2} on characteristic polynomials)? A6 says
   this is a NECESSARY feature of any carrier, so it is also a cheap
   kill-test: a candidate carrier with no 2-primary headroom is dead
   on arrival.
3. The duality route: formulate "reflection = duality on the
   compactified object" inside the C5''' properness vehicle (log-THH
   residue sequences / CC's S-valued RR); this is where the
   degree-inverting v^m <-> v^{-m} can live lawfully.

## 5. Proposed doc-24 amendment (for the lead)

Replace the H-r3 statement of doc 24 sec 2 by the sec 1.4 forcing form,
and add: "The analytic half H-r3(an) is a theorem
(O-doc Thm A1 + Cor A2 + Props A3-A6, witness
prime_int_hr3_scheme_rigidity.py): negation-naturality forces c = 1/2
up to an EF-invisible constant; no branch convention has half-integer
slope; the symmetric value is the C_2-average / principal value; and
it requires a canonical lambda^{1/2} (double cover). The open content
of H-r3 is exactly H-r3(hom) = L-hom (negation supply at Spec F_q),
with fork F1; the residual Weyl action v -> -v is VACUOUS for this
purpose (O-doc O-1), the antilinear reading gives only Schwarz (O-2,
A4), and the real cyclotomic Frobenius is equivariant, not inverted
(O-3)." The doc-24 phrase "the real structure does not merely permit
the symmetric scheme, it FORCES it - conditional on H-r3" remains
correct with H-r3 read in the forcing form; in the permissive form it
is vacuously satisfiable and forces nothing.

## 6. DOF audit (G-INT6)

- Sec 3 (analytic half): zero free parameters. The scheme class
  (windows + zeta-type continuations) is not chosen to fit - A0 is a
  classification, and the forced slope 1/2 is a one-parameter-family
  pin against a continuum (#constraints > #choices). The EF-invisible
  constant e^{a} is recorded as NOT forced (a residual choice, same
  bucket as Deninger's 2^{-1/2}).
- The negation-naturality DEMAND (1.3) is calibrated by the
  finite-dimensional determinant and the exact finite-level parity
  (G7) - both parameter-free - but the demand binds only if the
  geometry supplies N: that conditionality is the entire point and is
  carried as L-hom, not spent silently.
- Sec 4 (homotopy half): no claims made beyond transcribed theorems
  (cited inline) plus three one-line computations (O-1 commutation;
  O-2 antilinear conjugation; the recentering sign of A6), each
  witnessed or immediate. Verdicts are fail-closed: NO currently
  computed structure supplies N.
- Witness: 7 gates, pre-registered fail-closed readings R-G1..R-G7 in
  the docstring, exit-code gated, ALL PASS at tolerances 1e-12
  (assembled identities), 1e-4 (tail-limited products), 0.0 (exact
  finite checks).

## 7. Honest limits

- The analytic theorems classify SCHEMES of zeta/branch type. A
  hypothetical regularization wholly outside the exp-polynomial
  ambiguity class is not excluded by A1's proof as written; I know of
  no such construction, and the zeta class is the one all sources use
  (Deninger conditions (1)-(2)). Recorded as a class assumption, not
  hidden.
- L-hom/F1 is genuinely open and I could not move it; everything
  computable says the needed structure is invisible at pi_*-level. If
  F1 resolves NEGATIVELY at the parametrized level too, then THR's
  C_2 cannot force the scheme, and the forcing must come from the
  compactified/duality object (C5''') or nowhere - that would demote
  the doc-24 selection mechanism from "candidate answer path" back to
  "calibration", and the realization-spec input 4 would again have no
  carrier. State this plainly: H-r3 is currently a NAMED hypothesis
  with a proven analytic half, a necessary 2-primary feature (A6), and
  no proven geometric supply.
- p = 2: untouched here (the odd-p obstructions are already decisive
  for the formulation); A6 suggests the 2-primary direction is where
  the supply must live, which makes the missing THR(F_2)^{tC_2}
  computation (M-doc sec 4) MORE interesting, not less.
- No archimedean claims anywhere: everything is at the finite-place
  shadow, per the standing fork discipline.
