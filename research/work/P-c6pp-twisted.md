# P - C6'' executed at obstruction depth: the Adams-twisted square is a GROUP pairing, the wild twist converts excess to counts, and the full descent twist blocks at two named inputs

Status: C6'' (promoted to PRIMARY by doc 23 sec 4) executed 2026-06-10.
Witness: prime_twisted_adams_ku.py (ALL PASS, exit-code gated, ~3 s;
readings W1-W8 pre-registered in the docstring). Citation-grade input:
Lee arXiv:2206.02411v3 (archived; section/theorem numbers cited per
ingredient below); Goerss-Hopkins-Miller for the E_infinity psi^alpha on
ku_p^ (as recorded in I-doc sec 6). Honest headline: the FULL twisted
descent spectral sequence was NOT run to an unconditional E_2; it blocks
at two precisely named missing inputs (sec 3). What IS unconditional:
the family structure theorems (sec 2), the derived pi_*-shadow computed
completely (sec 4), the mod-(p,beta) layer (twist-invisible, sec 4.3),
the branch fork with discriminating signatures (sec 5), and every
cardinality law in the witness. No spectral-sequence differential is
asserted beyond these.

Conventions: p ODD prime, everything p-complete (Lee Sec 3.2 standing
assumption; LTE and Lee's Lemma 4.1.3(b) both fail at p = 2). alpha in
Z_p^x; the wild instance is alpha = 1 + p, more generally
alpha = 1 + u p^c (u unit), c = v_p(alpha - 1) >= 1.

## 1. The object, and what "compute it" turned out to mean

The posed instance (I-doc sec 6): the graph pairing

    X(alpha) := <Gamma_id, Gamma_psi^alpha>
             = THH(ku_p^; (ku_p^)_{(1, psi^alpha)})
             = ku (x)_{ku (x)_S ku} ku_{psi^alpha},

graph calculus per Campbell-Ponto (I-doc sec 6 refs). Since psi^alpha is
an E_infinity AUTOMORPHISM (GHM + connective cover), X(alpha) is the
pushout in E_infinity rings of (mult) and (mult o (1 (x) psi^alpha)):
the DERIVED FIXED LOCUS of psi^alpha on "Spec ku" over the sphere. This
geometric reading does real work below: fixed loci of automorphisms are
Lefschetz objects, and every computed cardinality comes out in
det(1 - d psi)-form.

## 2. Unconditional structure theorems (P3, part 1)

(2a) TRANSPORT. For automorphisms f, g of ku_p^ and the graph bimodule
ku_{(f,g)}, conjugating the whole picture by f^{-1} gives

    <Gamma_f, Gamma_g> = THH(ku; ku_{(f,g)}) ~ THH(ku; ku_{(1, g f^{-1})})
                       = X(g f^{-1}).

The p-complete Adams family is the GROUP Z_p^x; the entire family Gram
is the one-variable function X on Z_p^x. Three corollaries:

  - TRUE DIAGONAL: <Gamma_alpha, Gamma_alpha> = X(1) = THH(ku_p^) for
    EVERY alpha - the untwisted lcm ladder (I-doc), p-part
    v_p(|T_2w|) = floor(log_p(w+1)) - v_p(w) - v_p(w+1)  (witness W8).
  - RATIO LAW: <Gamma_(1+p)^k, Gamma_(1+p)^l> = X((1+p)^{l-k}); per
    weight the shadow valuation is 1 + v_p(k-l) (+ v_p(w) in branch
    (ii), sec 5): the doc-23 matrix log|k-l| reappears P-ADICALLY
    (witness W4, exact). The p-adic log-distance is an ULTRAMETRIC: the
    family Gram is hierarchical (Parisi-type), a different spectral
    universe from the archimedean log|k-l| that doc 23 refuted.
  - BIDEGREE VERDICT (doc 23's question): the expected "(1, alpha)"
    is REFUTED as a homological bidegree. All graphs in the p-complete
    family are graphs of AUTOMORPHISMS - invertible, "degree 1 on both
    rulings", bidegree (1,1). There is no Frobenius-degree growth in
    Z_p^x. Where alpha actually lives: in the NORMAL data - psi^alpha
    acts on the weight-w line by alpha^w, and every pairing cardinality
    below is |det(1 - d psi^alpha | weight-w)|_p^{-1} = p-part of
    (alpha^w - 1): a local Lefschetz fixed-point count (witness W7).

(2b) FIBER CLASSES. The ruling analogue on the square is the residue
bimodule Z_p with BOTH actions through the truncation ku -> Z_p = tau_{<=0}ku.
Pairing with any graph: psi^alpha induces the identity on pi_0, so at
the level of homotopy the left structure tau o psi^alpha = tau and

    <Gamma_alpha, F> = THH(ku; Z_p)  for every alpha in Z_p^x
                     = Z_p ⊕ [ (+)_k Sigma^{2pk-1} Z/p^{1+v_p(k)} ] (x) Lambda(lambda_2)

(Lee Cor 4.1.6 = Ausoni Cor 6.9). The fiber column of the Gram is
CONSTANT - the exact analogue of Gamma . F = 1 on the FF surface, and
consistent with (2a): no degree growth anywhere in the family.
(Coherence caveat: tau o psi^alpha ~ tau as E_infinity maps is asserted
at homotopy level; the space-level identification is plausible but
unverified - flagged, not load-bearing for anything below.)

(2c) CONSEQUENCE FOR DOC 23. The Castelnuovo correction
C[k,l] = <G_k,G_l> - u(d_1(k)d_2(l)+d_1(l)d_2(k))/2 DEGENERATES for this
family: d_1 = d_2 = 1 identically, so the correction is the constant
shift that doc 23 already excluded. The Frobenius-degree mechanism the
FF index needs CANNOT come from the p-complete Adams group. The
non-invertible directions are psi^p (not in Z_p^x; integral E_1
refinement on ku unlocated, I-doc sec 6) - and the structural Frobenius
at p on THH itself is the CYCLOTOMIC Frobenius THH -> THH^{tC_p}, which
is not an Adams operation. Transferable verdict: the degree-growth slot
of the index argument must be fed by the cyclotomic/TC layer (or by an
integral psi^k with k non-unit), not by the Adams family. This sharpens
doc 23 sec 3 rather than executing it.

## 3. The twisted descent SS: what twists cleanly, and the two blocks

Lee's tower (untwisted), ingredient by ingredient, with twist status:

```text
ingredient                         Lee ref        twists?
cosimplicial descent diagram       Def 3.1.1      YES - exists verbatim
  for the THH(MU)-module                          for the twisted module
  THH(ku; M), M = ku_{(1,psi^a)}                  (M connective)
strong convergence                 Lem 3.1.5      YES - THH(MU) -> MU is
                                                  1-connective (THH_1(MU)
                                                  = 0), module connective
levelwise identification           Prop 3.2.3,    BLOCKED (O1-O3 below)
  E_1 = CB_{Gamma_*}(A_*)          Prop 3.1.3,
  as cobar of a comodule           Lem 3.2.2
generator/coaction formulas        Def 3.2.4,     twist computable on
                                   Lem 3.2.8      leading terms IF the
                                                  comodule exists (sec 5)
mod-(p,beta) Ext                   Prop 4.1.1     UNCHANGED by the twist
                                                  (unconditional, sec 4.3)
v_0-/beta-Bockstein towers         Prop 4.1.5,    branch-dependent
                                   Thm 4.2.1      (sec 5)
```

The obstruction chain, precisely:

O1 (psi^alpha is not MU-linear). psi^alpha o (orientation MU -> ku)
classifies the formal group law x + y + (alpha beta) x y, not
x + y + beta x y. The two orientations differ by the strict isomorphism

    g_alpha(x) = ((1 + beta x)^alpha - 1) / (alpha beta)
               = x + sum_{k>=2} (binom(alpha,k)/alpha) beta^{k-1} x^k,

witnessed exactly as series (W3). For alpha = 1+p this is a POLYNOMIAL
of degree p+1; its b_{k-1}-coordinates are p-divisible for
2 <= k <= p-1, and the FIRST UNIT coordinate is the t_1 = b_{p-1}
coordinate (times beta^{p-1}) - the twist's first unit-level interaction
sits exactly on Lee's lambda_1-locus, the source of his torsion towers
(Prop 4.1.5). Every coordinate carries beta^{>=1}.

O2 (no relative bimodule). A ku (x)_MU ku-module must have its two
MU-restrictions identified; the twisted bimodule's are (orientation) and
(psi^alpha o orientation), which differ by O1. One can move the twist
onto either leg of the relative square (ku with the psi^{1/alpha}-twisted
orientation), but then the OTHER graph (the diagonal) stops being a
module over the same square. The two graphs cannot be made relative to
MU simultaneously: the relative square over MU has no room for the
twist, because MU pins the orientation and psi moves it.

O3 (the naive combinatorial twist is inconsistent). Composing only the
last coface of Lee's cosimplicial object with psi^alpha violates the
cosimplicial identity s^0 d^1 = id (s^0 of the twisted d^1 is psi^alpha,
not the identity). The correct twisted object must thread the twist
through the full cyclic/bimodule structure (the technology of
Krause-McCandless-Nikolaus, arXiv:2302.07686, is the natural home); its
normalized complex is NOT obtained from Lee's cobar by decorating one
map. This is where the two computational branches of sec 5 split.

THE TWO NAMED MISSING INPUTS (fail-closed deliverable):

(A) An E_infinity (or E_2-with-orientation-compatibility) refinement of
    psi^alpha on MU_p^ making the orientation square commute up to the
    g_alpha-twist. Status: NOT located in the literature (classical
    stable Adams operations on MU exist, Novikov; their structured
    multiplicative refinement on MU_p^ is the open point - note BP is
    not even E_infinity, Basterra-Mandell territory). Given (A), the
    whole tower twists levelwise: the levelwise homotopy is A_* (x)
    Gamma_*^{(x) s} transported by the MU-level automorphism, E_1
    becomes the cobar of a genuine twisted comodule (A_*)_alpha whose
    coaction is Lee's eta_R composed with the g_alpha-cocycle, and the
    coaction on Lee's generators is computable from Lemma 3.2.8 plus
    the W3 coordinates.

(N) The normalization question: in the correct twisted complex, does
    the diagonal weight operator (1 - alpha^{wt}) enter the filtration-0
    differential LINE BY LINE in the weight grading (branch (ii)), or
    only through the multiplicative ideal relations as in the honest
    pi_*-shadow (branch (i))? Equivalently: does the motivic/even
    filtration of the twisted object grade by Adams weight before or
    after the ring relations are imposed? The toy model (sec 4) proves
    branch (i) for the Z_p-relative shadow; the sphere-level answer
    needs (A) + the O3 combinatorics. This is the single sharpest
    question the next worker should attack.

Mapping to the task's fallback menu: "relative THH over ku of the
twisted bimodule" is trivial (THH^{ku}(ku; M) = M); the meaningful
relative shadow is over MU and is exactly what O2 blocks; "HH of pi_*
with twisted coefficients" is computed COMPLETELY below (not just low
degrees - the twisted complex is Koszul-small); the first k-invariant
correction is subsumed in the branch fork (the sphere cells enter
through the mu/lambda towers, sec 5.3).

## 4. The rigorous shadows (unconditional)

### 4.1 The derived pi_*-shadow, complete

R = Z_p[beta], phi(beta) = alpha beta. R is a complete intersection over
R (x)_{Z_p} R via the regular element beta_1 - beta_2 (Koszul), so the
twisted Hochschild complex over Z_p is EXACTLY the two-term complex

    HH^{Z_p}(R; R_phi) = [ R --(1-alpha)beta--> R ]   (degrees 1, 0):

    HH_0 = R/((1-alpha)beta) = Z_p (weight 0)  (+)  (+)_{w>=1} Z/p^c,
    HH_1 = ker = 0           (c = v_p(alpha-1); witness W2).

Two readings, both exact:

  - TRANSVERSALITY (P2): HH_1 = 0 - the twist kills the cotangent/excess
    line that the untwisted diagonal carries (HH_1 = Omega^1, the rank
    part). Above weight 0 the shadow is pure torsion. The graph is
    transverse to the diagonal; the only excess is the unit Z_p at
    weight 0 (the fixed point 0 of the multiplicative flow).
  - IDEAL COLLAPSE: the per-weight cardinality is the UNIFORM Z/p^c
    (the THH(F_p) half-ladder with multiplicity c), NOT the LTE tower:
    the ideal ((alpha^j - 1) beta^j : j) contains (alpha-1)beta .
    beta^{w-1}, so the weight-w quotient is Z_p/(alpha-1). The
    weight-graded single-relation cokernel Z_p/(alpha^w - 1) =
    Z/p^{c + v_p(w)} differs from it by exactly v_p(w) (witness W2,
    "branch discriminator"). Multiplicative structure EATS the tower.

What this shadow captures: the filtration-0 ring-level layer (the
analogue of Lee's E_2^{0,*} world). What it misses: all sphere cells -
Lee's F-lattice (lambda_2-line), the T-torsion, the mu/lambda_1 towers -
i.e. everything that made the untwisted ku square interesting.

### 4.2 Tame/wild dichotomy, sharpened (corrects I-doc sec 3.7 slightly)

Witness W5, exact Teichmuller lift. Tame alpha (finite order d | p-1):
alpha^w = 1 exactly when d | w - the fixed locus is the SUBLATTICE
Z_p[beta^d], i.e. PERIODIC EXCESS LINES, not "trivial": the correct
Lefschetz picture for a finite-order automorphism (positive-dimensional
fixed locus), and the analogue of Frobenius graphs meeting the diagonal
over every F_{q^d}. Off the sublattice: unit-transverse, zero torsion.
Wild alpha (infinite order): finite valuation at every w >= 1 - no
excess above weight 0, fully count-grade. The orbit dichotomy of doc 20
appears inside the family as compact-vs-free directions of Z_p^x.

### 4.3 The mod-(p, beta) layer: the twist is INVISIBLE there

Two independent reasons, both witnessed: the diagonal eigenvalues
alpha^w = 1 mod p (alpha = 1+p; W1), and every g_alpha-cocycle
coordinate carries beta^{>=1} (W3). So in BOTH branches of sec 5 the
twisted mod-(p,beta) Ext equals Lee's Prop 4.1.1:

    Ext_{Gamma_*}((A_*/(p,beta))_alpha) = F_p[mu] (x) Lambda(lambda_1, lambda_2),

mu = sigma^2 x_{p-1}, lambda_1 = sigma^2 t_1, lambda_2 = sigma^2 b_1.
The twist lives entirely in the BOCKSTEIN differentials. This is the
twisted-instance face of a doc-19/20 refrain: the F_p-fiber cannot see
the wild direction; only the integral/Bockstein layer can.

## 5. The branch fork (pre-registered signatures; no differentials faked)

Both branches agree on: sec 4.3; transversality (rationally X(alpha) =
Q_p in degree 0 - every (1-alpha^w) is invertible in Q_p, including the
would-be sigma-line: the toy's injective Koszul differential kills
d(beta) too); and the LTE LAW as the universal tower law (W1):

    v_p(alpha^w - 1) = c + v_p(w),   alpha = 1 + u p^c.

(5.1) BRANCH (i) - ideal collapse (toy-supported). Filtration-0 quotient
per weight: uniform Z/p^c. The twist still deforms the towers: under
(A), D0^tw(mu^k) acquires both Lee's kp-term (Lem 3.2.8(d), Prop 4.1.5)
and the eigenvalue term (1 - alpha^{(p-1)k}) mu^k-direction, and these
have EXACTLY EQUAL valuation: v_p(kp) = 1 + v_p(k) =
v_p(alpha^{(p-1)k} - 1) (W1 with w = (p-1)k). The tower law
Z/p^{1 + v_p(k)} at the mu/lambda_1-locus is therefore ROBUST across the
twist - same grading law, possibly relocated generators. (Consistent
with W3: the twist's first unit coordinate sits on the t_1-locus.)

(5.2) BRANCH (ii) - weight-diagonal. If the motivic filtration of the
twisted object grades by Adams weight before ring relations, the
collapsed rank part converts weight-by-weight:

    Z_p[beta]  (excess/rank of the diagonal)
      |-->  (+)_{w>=1} Z/p^{c + v_p(w)}   (the LTE tower),

i.e. the K(F_q)/image-of-J ladder (|K_{2w-1}(F_q)| = q^w - 1 with
alpha playing q) appears as the converted rank part. P1's two phrasings
name exactly these two branches.

(5.3) DISCRIMINATING SIGNATURES (pre-registered for whoever resolves
(N); witness W6 verifies both closed forms):

```text
                       branch (i)              branch (ii)
per-weight ladder      log p^c (uniform)       log p^{c+v_p(w)}
D_alpha(s)             c log p zeta(s)         c log p zeta(s)
                                                + zeta(s) (-zeta_p'/zeta_p)(s)
s = 0                  NO pole;                simple pole, residue -1/2
                       value -(c/2) log p      (Abel constant); finite part
                                               zeta'(0) + (1/4 - c/2) log p
```

Branch (ii)'s transform factors as (global zeta as weight-counting
measure) x (the LOCAL von Mangoldt supply at p): the doc-19 local ladder
would be produced by a single wild twist at the completed place, with
the archimedean constant zeta'(0) reappearing in the finite part shifted
by a local term. Branch (i) instead reproduces doc 18's local F_p-square
constant -(1/2) log p (c = 1) with the opposite sign (even-degree
placement). Either outcome is informative; the s = 0 behaviour (pole vs
no pole) is the cleanest experimental discriminator.

(5.4) Lefschetz/Pochhammer reading (both branches, W7): through weight
W the branch-(ii) count is the p-adic Pochhammer
v_p(prod_{w<=W}(alpha^w - 1)) = sum (c + v_p(w)) - the (alpha;alpha)_inf
eta-type determinant det(1 - psi^alpha | (+)_w Z_p beta^w)^{-1} as a
regularized cardinality. (Bost-Connes-adjacent shape; one-line flag,
not pursued.)

## 6. Verdicts on the pre-registered readings

P1 (wild pairing reproduces the local ladder): CONFIRMED IN SHAPE,
BRANCH-DEPENDENT IN LOCATION. The task's P1 conflates two ladders: the
THH(F_p) half-ladder (uniform Z/p) and the LTE tower Z/p^{1+v_p(w)}.
The derived pi_*-shadow PROVES the uniform half-ladder (branch (i),
ideal collapse) for the ring-level layer; the LTE tower appears either
on the converted rank part (branch (ii)) or - robustly, in BOTH
branches - at the mu/lambda_1 tower locus via the exact valuation
balance v_p(kp) = v_p(alpha^{(p-1)k} - 1). The LTE law itself is
witnessed exactly (W1). The Lambda-structure (1 + v_p(w) = v_p(pw))
is present wherever the tower forms.

P2 (no rank part, transverse, fully count-grade): CONFIRMED for wild
alpha, unconditionally at shadow level and rationally at sphere level
(everything above weight 0 is torsion; the cotangent excess line dies;
weight-0 unit Z_p remains - the fixed point of the flow). SHARPENED for
tame alpha: periodic excess sublattice Z_p[beta^d], not triviality.

P3 (diagonal, fiber data, bidegree): ANSWERED STRUCTURALLY (sec 2):
true diagonal = untwisted THH(ku_p) for every family member (transport);
fiber pairings constant = THH(ku; Z_p) (Lee Cor 4.1.6); bidegree (1,1)
- the "(1, alpha)" expectation is refuted as bidegree and relocated to
the normal-eigenvalue data det(1 - d psi^alpha) = prod (1 - alpha^w).
Doc-23 consumer matrices supplied: per weight w, off-diagonal
1 + v_p(k_i - k_j) (+ v_p(w) in branch (ii)), diagonal
v_p(|T_2w|) = floor(log_p(w+1)) - v_p(w) - v_p(w+1) plus the excess
slot. Exploratory signature probe (ungated, W8): the hierarchical
matrices are NOT Lorentzian at the probed weights - signature flips
between indefinite (+3,-6) at diagonal-0 weights (w+1 a p-power) and
positive (semi)definite at large-diagonal weights. The Castelnuovo
question remains open AND the family now provably lacks the degree
mechanism (sec 2c): the index pressure must come from the cyclotomic
Frobenius / non-invertible operations, not from Z_p^x.

## 7. G-INT6 ledger (degrees of freedom vs constraints)

Free choices: p (odd, any - witnessed across {3,...,13}); alpha = 1+p
(canonical: a topological generator of the wild part 1 + pZ_p; the
c-dependence is tracked symbolically, not tuned); p-completion (FORCED:
GHM E_infinity Adams operations exist only p-completely - a structural
constraint, not a knob); branch (i)/(ii) (NOT chosen - held open as a
fork with discriminating signatures). Matched constraints with zero
remaining parameters: the LTE law (infinitely many exact integer
identities); the ratio/group law (Gram depends only on g f^{-1});
the valuation balance at the lambda_1-locus; the tame periodic-excess
pattern; the Dirichlet closed form with the local Euler factor; the
Pochhammer identity; the diagonal p-part formula. Ledger: heavily
constraint-positive; the only fitted object is NONE - the branch fork
is recorded as ignorance, not resolved by preference.

Carrier guard: every construction above consumes the E_infinity ring
map psi^alpha - the family group, the transport, the twisted bimodule,
the FGL conjugation g_alpha. DH/Epstein have no ring, hence no THH, no
Adams operations, no graphs, no fixed-locus counts: dead at the
definition of the OBJECT, before any computation. (Necessary filter,
not sufficient - as always.)

## 8. Honest limits

1. The headline limitation: the unconditional twisted E_2 over the
   sphere is NOT computed. Inputs (A) and (N) of sec 3 are the precise
   blockers; everything in sec 5 above filtration 0 is conditional on
   (A) and forked on (N). No claim of any specific differential beyond
   the valuation-balance observation (which is a statement about the
   coefficients appearing, not about which classes survive).
2. The transport lemma and family-group corollaries are bimodule-level
   arguments; coherence of tau o psi^alpha ~ tau (sec 2b) is asserted
   at homotopy level only.
3. The toy shadow is relative to Z_p; ku is not an HZ_p-algebra, so the
   shadow's authority is exactly "the ring-level/filtration-0 layer",
   no more.
4. Lee transcription risks are inherited from the I-doc (its sec 7
   point 1); nothing here re-derives his presentation.
5. The exploratory signature probe (W8) is ungated and reads small
   sections only; no Castelnuovo conclusion is drawn from it.

## 9. Next steps (ranked)

1. Resolve (N) [doc-scale, sharply posed]: build the twisted cyclic
   object with KMN polygonic/TR-with-coefficients technology for the
   single automorphism psi^alpha and extract its motivic filtration in
   weights <= p: the FIRST place branches (i)/(ii) differ is the
   weight-1 beta-line in total degree 2 (branch (i): Z/p^c from the
   ideal; branch (ii): Z/p^{c} too - they first DIFFER at w = p:
   Z/p^c vs Z/p^{c+1}); a single honest computation of pi_{2p} X(1+p)
   decides the fork. The s = 0 pole dichotomy (5.3) is the global
   shadow of the same decision.
2. Settle (A) [literature + obstruction theory]: structured Adams
   operations on MU_p^; even a negative settles which machine (Lee's
   descent vs KMN) is the right vessel.
3. Doc-23 continuation: feed the hierarchical per-weight matrices into
   the C4 protocol properly (ultrametric Gram theory is exactly
   solvable - Parisi diagonalization); decide whether the index
   question at the p-complete square is well-posed at all without the
   cyclotomic degree direction (sec 2c suggests it is not, which is
   itself a doc-17-fork-relevant finding).
4. The O_K control (doc 21 G-INT6): the same twisted construction for
   psi^alpha on ku_p with K-coefficients should produce Dedekind-local
   ladders; a dictionary that maps it to zeta's supply would expose
   fitting.
