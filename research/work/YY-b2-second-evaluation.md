# YY - Bridge B2: the second-evaluation audit of the banked corpus (G-CH3 retroactive)

Status: fresh-context worker YY, 2026-06-11. Charter doc 38 bridge B2
(sec 3) + gate G-CH3 applied retroactively to the banked corpus.
Required reading executed in order: doc 38, UU-ku-castelnuovo.md (the
characterization: Weil's #Fix has TWO independent evaluations, every
ku-face entry has ONE), doc 14 (fork protocol F1-F3/P1-P2 - extended
here to P3), proof/README.md, doc 19, W-monoid-frobenius.md,
HH-weil-restriction-fork.md, I-c6-ku-square.md, KK-L1-density-rr.md,
SS-ku-inequality-proof.md; consulted for named identities:
P-c6pp-twisted.md (the Lefschetz law), QQ-native-face.md sec 1.5
(Delta_p's mean).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_yy_second_evaluation_audit
    (gates Y1-Y7)

DISCLOSURE (SS/UU precedent): sections 1-4 (the P3 criterion, the audit
table with verdicts, the gate registrations) were written BEFORE the
witness was first run. Every gated quantity is an exact integer /
Fraction identity or a high-precision constant DERIVED in the named
source; nothing is fitted. NO ZEROS CONSUMED anywhere in this memo or
its witness: no fork_lib import, hence NO FREEZE STEP is required (the
task's expectation "zero contact: none" holds by construction - the
audit is about supply-side identities only).

HEADLINE (registered before the run, both ways carried): the expected
clean negative holds for 15 of 17 audited identities - each is ONE
evaluation with its transport named. ONE banked number passes the P3
independence test: q^w - 1 (Quillen's K(F_q) = fib(psi^q - 1), W-doc
sec 2.3/W2a), together with its determinant dress (Hesselholt Theorem A
at Spec F_q, W-doc sec 1.3). G-CH3 escalation duty therefore applies
and is discharged at NN-grade scrutiny (3 deterministic runs, BOTH
deformation directions witnessed, carrier guard) - and the finding is
DE-ESCALATED to EMBRYO grade: the pair is a genuine two-evaluation in
Weil's sense, but the spectrum its agreement constrains is provably
empty (zeta(F_q, s) has no zeros; the Adams eigenvalues q^w are forced
supply data). The trace-methods world contains clause 6 in embryo,
exactly at Quillen + DGM; the blockers that stop the embryo globalizing
are W-doc's B1-B3, i.e. the program's one wall.

## 1. Fork-test P3 (the criterion, proposed verbatim for doc 14)

The foundation, made checkable. Weil's two evaluations of #Fix(F^w) are
independent because they factor through DIFFERENT STRUCTURES - geometric
points of C(F_bar) on one side, l-adic cohomology on the other - whose
agreement is a THEOREM with content (Lefschetz). Two computational
routes through the same structure (a Poisson pair, a coker rewritten as
a determinant, a regularized series and its own continuation) are ONE
evaluation. The operational form, written so a witness can decide it:

```text
P3 (second-evaluation test; G-CH3's checkable form). Given a banked
identity "A = B" for a number N, call A and B INDEPENDENT EVALUATIONS
iff all three hold:

(P3-a) DIFFERENT STRUCTURES (extension test). Each side has a natural
   domain of definition strictly larger than the agreement locus:
   there is a deformation family in which B stays defined and moves
   while A's carrier ceases to exist (or stays constant), AND a
   deformation family in which A moves while B is untouched. If every
   step of the proof of A = B is an isomorphism / substitution /
   regularization INSIDE one structure, it is ONE evaluation: record
   the transport. (This is F2's deformation kill, repurposed from sign
   mechanisms to evaluations.)
(P3-b) CONTENT. The agreement A = B on the common locus is a theorem
   whose proof consumes structure beyond the definitions of A and B
   (Weil: Lefschetz trace; height 0: Quillen's fib(psi^q - 1)).
   An equality holding BY CONSTRUCTION of one side (doc 38 P4's
   pre-registered failure mode) fails P3-b.
(P3-c) NONTRIVIAL SPECTRUM (decision grade). The agreement constrains
   at least one unforced spectral parameter. A pair passing (a)+(b)
   with an empty/forced spectrum is recorded EMBRYO grade: the
   pattern without the decision content.

Verdicts: ONE-EVALUATION (name the transport) / TWO-EVAL EMBRYO
(passes a+b, fails c) / TWO-EVAL DECISION (passes all three - the
clause-6 object; none expected to exist in the banked corpus, since
its existence on the zeta carrier is RH-grade).
```

Remark (why (a) is the right test): in the FF proof the trace side
extends to ALL cohomological correspondences (most not algebraic - the
count is undefined there) and the count side extends to arbitrary
set-maps (the trace is undefined there); the agreement locus -
algebraic correspondences - is cut by a theorem. That extension
asymmetry is exactly what no coordinate change can fake: a transport
has, by definition, the SAME natural domain on both sides.

## 2. The audit table (one line per banked identity)

Verdict column registered before the witness ran; witness gates in
brackets where the decisive computation is mechanical.

```text
#  identity (provenance)                  verdict      transport / decisive P3 fact
-- -------------------------------------- ------------ --------------------------------------------
1  Lambda(p^i) = log|THH_2i(F_p)|         ONE-EVAL     the dictionary n = p^i <-> ladder entry is the
   (doc 19 sec 3)                                      COMPARISON MAP; doc 19 sec 6 itself: "EF-equal
                                                       by construction". Adds integrality, not a
                                                       second evaluation.
2  archimedean supply = char. function    ONE-EVAL     Lerch/zeta regularization = analytic
   of THH(Z)_tors (doc 19 sec 2)                       continuation of the same series.
3  HH.1: Lambda(p^k) = -<d_k,d_k>_M       ONE-EVAL     finite linear algebra on the degree data that
   (HH thm HH.1)                                       DEFINE M = (log p) MAX; the d-frame transport
                                                       [Y4d, exact]. UU already: the cross term B'
                                                       has one evaluation; same for the diagonal.
4  lcm ladder |T_2w| = lcm(1..w+1)/w(w+1) ONE-EVAL     three routes (enumeration / sieve / closed
   (I-doc K2-K3)                                       form), all through Lee's presentation + prime
                                                       factorization: one structure [Y4a, exact].
5  <Delta,Delta>_tors = zeta'(0)          ONE-EVAL     the "second route" IS -zeta'(s) continued: the
   = -(1/2)log 2pi (doc 18)                            regularization scheme is the analytic object
                                                       itself [Y4b]. No independent evaluation.
6  TR(F_p) = W(F_p) (W-doc 1.4;           ONE-EVAL     natural isomorphism TR_0(A;p) = W(A) for ALL
   Hesselholt-Madsen Thm F)                            rings (functor-level transport): every
                                                       deformation moves both sides together. At F_p
                                                       the Frobenius is the IDENTITY on W(F_p) [Y5i],
                                                       so the fixed-point dress is definitional.
                                                       Independence enters one theorem later: see
                                                       sec 3.2 (DGM) - routes to row 9.
7  W(Z)^{F=1} = Z (W-doc 1.4, Dwork)      ONE-EVAL     ghost triangular solve + Fermat integrality
                                                       [Y5ii]; the "fixed locus = diagonal" reading
                                                       is a dress on one computation.
8  Lefschetz law: pairing cardinality     ONE-EVAL     coker = det at rank 1 (definitional linear
   = |det(1 - d psi^alpha | w)|_p^{-1}                 algebra) [Y4e]; "Lefschetz" in name only: no
   (P-doc 2a, witness W7)                              independent point count exists on Spec ku.
9  q^w - 1 = #Fix(Fr_q^w | G_m(F_q-bar))  TWO-EVAL     PASSES P3-a,b: geometric Fix-count in an
   = |K_{2w-1}(F_q)|                      EMBRYO       explicit field [Y1] vs Adams-eigenvalue coker
   = |coker(psi^q - 1 | pi_2w)|                        (psi^q - 1 on the weight-w line) [Y1];
   (W-doc 2.3, W2a; Quillen 1972)                      independence BOTH ways [Y2, Y3]; agreement =
                                                       Quillen's theorem (consumed structure: the
                                                       +-construction / homotopy fixed points of
                                                       psi^q). FAILS P3-c: zeta(F_q,s) has no zeros;
                                                       the eigenvalue ladder q^w is forced. Sec 3.1.
10 Hesselholt Thm A at Spec F_q:          TWO-EVAL     the same pair as row 9 in determinant dress:
   zeta(F_q,s) = det_inf(s - Theta | TP)  EMBRYO       count-defined zeta vs regularized Frobenius
   (W-doc 1.3)                                         determinant on TP (x)_{W,iota} C. The
                                                       agreement consumes phi(v) = pv + iota. P3-c
                                                       fails identically (TP_od = 0: the odd slot -
                                                       where zeros would live - is EMPTY at a point).
11 FE identities (SS.1; PP KU1: comb sum  ONE-EVAL     coset Poisson is the transport (SS proved it
   = dual sum, two routes to 1e-178)                   an identity); SS's own framing: two routes,
                                                       one structure.
12 Delta_p mean = gamma + log pi          ONE-EVAL     Frullani substitution: both sides are the
   (QQ sec 1.5)                                        same integral [Y4c].
13 KK.L1: chi_tw -> a + log rho(m)        ONE-EVAL     Euler-Maclaurin transport on one monoid comb;
   (KK thm L1)                                         count and density live on the same structure.
14 vdGS RR: h^0(D) - h^0(K-D) =           ONE-EVAL     Poisson transport; both sides are theta-count/
   deg D - (1/2)log|d| (doc 19 sec 5)                  degree data of the same lattice.
15 genus pair (-2 log 2, +(1/2)log 2pi)   NOT A PAIR   doc 22 proved the clash is invariant-level:
   (doc 22)                                            two different OBJECTS, not two evaluations of
                                                       one number. Explicitly not a sleeper.
16 q^w - 1 = prod_{d|w} Phi_d(q); adelic  ONE-EVAL     cyclotomic factorization redistributes
   v_ell ladder (W-doc W3)                             evaluation 9-B over places: a transport of
                                                       one side of row 9, not a third evaluation.
17 Barnes d2 = h^2/2 rank-2 carrier       ONE-EVAL     (from record, UU's inherited witness): a
   (prime_int_gc_k3_barnes_rank)                       derivation within one structure; no second
                                                       route is held in the bank.
```

ZERO SLEEPERS AT DECISION GRADE; ONE pair at embryo grade (rows 9-10,
one number in two dresses). Every other banked identity is a transport,
named above. This is the full-value fail-closed outcome the task card
pre-authorized, sharpened: the corpus does hold the Weil PATTERN, at
the one place where it is a theorem and the spectrum is empty.

## 3. The embryo, examined (G-CH3 escalation discharged)

### 3.1 The Quillen pair (rows 9-10)

The number: N(q, w) = q^w - 1. Evaluation A (geometric count):
#Fix(Fr_q^w) on G_m(F_q-bar) = #F_{q^w}^x, computed in the witness by
literal enumeration in an explicitly constructed field F_{q^{2w}}
(polynomial arithmetic over F_p, irreducible modulus found by trial
division; the ambient is strictly larger than the fixed field, so the
count is a count, not a tautology). Evaluation B (homotopy/spectral):
|coker(psi^q - 1 : pi_{2w} KU -> pi_{2w} KU)| - the Adams eigenvalue
q^w on the weight-w line, i.e. det(1 - Fr | weight w) up to sign.
Agreement: Quillen 1972, K(F_q) = fib(psi^q - 1) (space level,
integral) - a theorem whose proof consumes the +-construction and the
ell-adic comparison, far beyond either definition. P3-a both ways:

```text
direction 1 (B moves, A's carrier dies): psi^k - 1 is defined and
  |k^w - 1| moves for EVERY integer k >= 2; a field with k elements
  exists iff k is a prime power (order = char^dim). Witnessed [Y2]:
  for every non-prime-power k <= 100, the spectral value is a
  well-defined integer while the carrier predicates fail (CRT
  idempotent e != 0,1 with e^2 = e in Z/k exhibited; the ku-cell comb
  address also dies: SS Lemma A's iff, rerun).
direction 2 (A moves, B untouched): the semilinear twists
  sigma_c(x) = c x^q (c in F^x) deform the geometric Frobenius; the
  fixed count jumps from q (c = 1) to 1 or q per the (q-1)-power
  class of c [Y3, exact enumeration + the partition identity
  sum_c (count - 1) = q^{2}-1], while psi^q on pi_* carries no c at
  all. The count side has deformation freedom the spectral side
  cannot see.
```

P3-b: passes (Quillen). P3-c: FAILS, provably - zeta(F_q, s) =
1/(1 - q^{-s}) is zero-free; equivalently (row 10's dress) TP_od(F_q)
= 0: Hesselholt's odd-degree determinant slot, the place where zeros
would sit, is empty for a point. The agreement of the two evaluations
constrains nothing because there is nothing unforced to constrain.
VERDICT: TWO-EVAL EMBRYO. Escalation per G-CH3 was applied (3
deterministic runs, deformations both ways, carrier guard) and the
de-escalation to embryo is itself a proved fact (TP_od = 0), not a
judgment call.

### 3.2 TR(F_p) = W(F_p), the special question answered

Is the Witt side an independent evaluation of the count side, or
definitionally the same? DEFINITIONALLY THE SAME, twice over:

1. TR_0(A; p) = W(A) is a natural isomorphism of functors on ALL rings
   (HM Thm F; McCandless's corepresentability makes TR itself the
   universal Frobenius-lift receptacle). A natural iso is the purest
   form of transport: no deformation of A separates the sides. P3-a
   fails at functor level.
2. At A = F_p the Witt Frobenius is the IDENTITY (F = id on W(F_p) =
   Z_p; witnessed at component level, [Y5i]): the "fixed points of
   Frobenius" dress W(F_p)^{F=1} = Z_p is the whole ring fixing
   itself. There is no count being matched; there is one object with
   two names.

WHERE independence genuinely enters the trace world: one theorem later.
K(F_p)^_p = TC(F_p)^_p (DGM): the left side carries Quillen's
GEOMETRIC evaluation (row 9), the right side the cyclotomic
fixed-point evaluation ((can - phi) acting by p^w - 1 on weight-w
lines, W-doc 1.4). That IS a Weil-shaped agreement of two structures -
and the banked p-adic blindness (W3b: v_p(q^w - 1) = 0 for all w)
says the trace side at p sees exactly the part of the count that is
trivial; the entire degree growth lives at ell != p and at the
archimedean place, reachable only through iota (W 1.5). So: the
trace-methods world contains clause 6 in embryo - the pattern is
Quillen + DGM - and the embryo's non-globalization is PRECISELY
blockers B1-B3 (p-completeness; no linearization of phi over Z; no
iota for the square's prism). The answer shapes clause 6 as the task
hoped: the missing object is not a new kind of identity, it is the
EXISTING identity's meeting point moved to a carrier whose spectrum
is nonempty.

### 3.3 The nearest misses and their boundary conditions (inverse-problem feed)

Each near-miss, with the exact structure that would upgrade it
(boundary conditions BC1-BC4 for WW's inverse problem):

```text
BC1 EXTENSION ASYMMETRY (from rows 9/10 vs all transports): a genuine
    second evaluation has a strictly larger natural domain on EACH
    side, with the agreement locus cut by a theorem (Y7's measured
    shape: spectral side defined for all k, geometric side exactly on
    prime powers, agreement everywhere both exist). Any clause-6
    candidate must present this shape on arrival; an evaluation
    defined on exactly the count's data is a transport (15 of 17
    rows). This is the arrival-test form of G-CH3.
BC2 RIGIDITY SPLIT (from UU + row 9): Weil's extraction needs the
    count side RIGID (intersection theory pins it; no deformation
    freedom on the agreement locus) and the spectral side FREE
    (unknown eigenvalues). The height-0 pair has the split with the
    freedom on the wrong side (Y3: the COUNT deforms, the spectrum is
    forced); the ku face has rigidity on BOTH sides (UU: every entry
    supply-determined). The missing object must place the UNKNOWN on
    the spectral side of an agreement theorem.
BC3 NONEMPTY ODD SLOT (from row 10): TP_od = 0 at a point is WHY the
    embryo is asleep. The upgrade is literally "TP_od != 0 for the
    compactified square with an iota": a global object whose odd
    determinant slot is nonempty and whose even/odd determinant
    quotient is forced to equal an independently defined count-zeta.
    Same slot as HH sec 3 / doc 31 exit B / BB / QQ / UU sec 4(ii):
    the missing timelike/archimedean unit, now in trace dress.
BC4 TR UPGRADE (from 3.2): for the trace world specifically - a
    DGM-type comparison over a base where BOTH sides are nontrivial
    at the same place: the count side global (all ell + infinity, the
    actual size q^w - 1), the trace side currently p-blind. iota is
    the local shim that re-archimedeanizes; its square-level absence
    (B3) is the named obstruction. "Witt vectors ARE fixed-point
    data" is true but spent at functor level; what is NOT spent is a
    Witt-against-count agreement at a place where the count is
    unforced.
```

## 4. PRE-REGISTERED GATES (written before the first run)

Evaluation rules: exact integer / Fraction arithmetic for every
decision gate (fields built by explicit polynomial arithmetic;
irreducibility by trial division; valuations exact); mpmath at dps
50-60 for the two numeric transports (Y4b, Y4c) with registered
tolerances 1e-40, 1e-30 (analytic identities, not decisions). No
flint needed; no fork_lib; no freeze.

```text
Y1 THE AGREEMENT (rows 9-10, exact): for (q, w) over 18 registered
   cases (q in {2,3,4,5,7,8,9}, q^w <= 81): in the explicitly
   constructed field F_{q^{2w}}, #{x : x^{q^w} = x} = q^w by literal
   enumeration; nonzero count q^w - 1 = |coker(psi^q - 1)| on the
   weight-w line (integer arithmetic) = 1/|zeta(F_q, -w)| (exact
   Fraction, zeta = 1/(1 - q^{-s})). FAIL: any mismatch.
Y2 P3-a DIRECTION 1: for every k in 2..100: spectral value k^w - 1
   defined (exact, w <= 6); k non-prime-power <=> a CRT idempotent
   e != 0,1, e^2 = e exists in Z/k <=> the cell comb {w : k | w(w+1)}
   has > 2 residues (SS Lemma A rerun). FAIL: any k violating either
   iff, or any prime-power control failing.
Y3 P3-a DIRECTION 2: for q in {3,4,5,9}, ambient F_{q^2}: for every
   c in F^x, #Fix(x -> c x^q) enumerated; gates: (i) the count MOVES
   (min over c < count(1) = q or max > ...; concretely: values in
   {1, q} with both attained); (ii) the classification law (count =
   q iff c^{q+1} = 1, else 1); (iii) the partition identity
   sum_c (count(c) - 1) = q^2 - 1; (iv) the spectral value q - 1 is
   c-independent (structural; recorded). FAIL: any clause.
Y4 THE TRANSPORTS (one-evaluation verdicts witnessed):
   a) lcm ladder: w <= 300: lcm(1..w+1) via gcd-fold = sieve product
      prod_{p <= w+1} p^{floor(log_p(w+1))}; w(w+1) | lcm. Exact.
   b) Bokstedt/zeta-reg: |-zeta'(0) - (1/2)log(2 pi)| < 1e-40
      (mpmath dps 60): the regularized route is -zeta'(s) itself.
   c) Frullani/Delta_p: |2(int_0^1 (1-e^{-pi x^2})dx/x -
      int_1^oo e^{-pi x^2}dx/x) - (gamma + log pi)| < 1e-30.
   d) HH.1 diagonal (exact Fractions, n <= 10): d_k^T MAX d_l =
      -delta_kl; e_0 null; <e_0, d_k> = 1 (coefficients of log p).
   e) Lefschetz=coker (exact): p in {3,5}, alpha in {1+p, 1+2p,
      1+p+p^2}, w <= 12: v_p(alpha^w - 1) = v_p(alpha - 1) + v_p(w)
      (LTE), and the pairing cardinality p^{v_p(alpha^w-1)} is the
      rank-1 coker BY DEFINITION - recorded as the transport.
   FAIL: any clause.
Y5 WITT (exact, ghost arithmetic over Fraction):
   i)  F = id on W(F_p): for p in {2,3} all p^5 component vectors
       (length 5), p = 5 all 5^4 (length 4): the universal Frobenius
       components F(x)_i are INTEGERS and F(x)_i = x_i mod p.
   ii) W(Z)^{F=1} = Z: for p in {2,3,5}, c in -20..20: the unique
       Witt vector with constant ghost (c,c,c,c) has ALL components
       in Z (Dwork integrality). FAIL: any clause.
Y6 CARRIER GUARD (exact): Epstein x^2 + 5y^2: 4, 6, 9 represented
   and irreducible in the represented-norm monoid; 36 = 4*9 = 6*6
   two distinct irreducible factorizations -> no valuation -> the
   geometric evaluation (a field/cell address) is unformable; DH:
   non-prime-power supports (Y2's predicate) + negative weights
   (HH H6b, cited) - the AGREEMENT theorem has no carrier; the
   spectral evaluation alone survives (that asymmetry IS P3-a).
   FAIL: any exact clause.
Y7 THE AGREEMENT LOCUS (P3-a summary, exact): {k <= 100 : geometric
   carrier exists} = {prime powers} (from Y2), a PROPER subset of
   {k : spectral defined} = all k; agreement verified at every
   common point sampled in Y1. FAIL: set mismatch.
```

Registered verdict logic: ALL PASS -> the table of sec 2 stands as
written (15 transports + 1 embryo pair + 1 non-pair); any Y1-Y3
failure would refute the embryo claim (reportable shock - it would
mean a banked theorem is wrong); any Y4/Y5 failure would refute a
ONE-EVAL verdict and PROMOTE that row to candidate-two (escalation).

---- verdict section written after the runs ----

## 5. VERDICT: THE REGISTERED OUTCOME, EXACTLY - 15 TRANSPORTS, 1 NON-PAIR,
## 1 TWO-EVALUATION PAIR AT EMBRYO GRADE; NO DECISION-GRADE SLEEPER

Witness ALL PASS (Y1-Y7, exit 0, FIRST RUN UNTOUCHED - no gate, no
constant, no code amended after the first run; deterministic across 3
runs, byte-identical logs /tmp/yy_run{1,2,3}.log; < 1 s). The G-CH3
escalation protocol was applied to the one affirmative (triple rerun +
both deformation directions as perturbation control + carrier guard);
the de-escalation to embryo grade is a proved fact (TP_od(F_q) = 0 /
zeta(F_q, s) zero-free), not a judgment.

```text
Y1  18 cases (q in {2,..,9}, q^w <= 81): the fixed-subfield count
    enumerated in an explicitly built F_{q^{2w}} = q^w exactly;
    G_m part = |coker(psi^q - 1)| = 1/|zeta(F_q,-w)| (Fraction).  PASS
Y2  k <= 100: spectral value k^w - 1 defined at ALL 99 moduli; the
    64 non-prime-powers ALL killed three ways (no field order, CRT
    idempotent exhibited, cell comb > 2 cosets); 35 prime powers all
    clean.  PASS (P3-a direction 1: B extends, A's carrier dies)
Y3  q in {3,4,5,9}: twisted Frobenii c x^q move the geometric count
    over exactly {1, q} (both attained; classification law c^{q+1}=1
    and partition sum_c (count-1) = q^2-1 exact), while the spectral
    side carries no c.  PASS (P3-a direction 2: A moves, B blind)
Y4  transports witnessed: (a) lcm two routes = one factorization,
    w <= 300 exact; (b) -zeta'(0) = (1/2)log 2pi to 8e-62;
    (c) Frullani = gamma + log pi to < 1e-30 (diff 0.0 at dps 50);
    (d) HH.1 d-frame exact at n <= 10; (e) LTE/coker exact.  PASS
Y5  Witt: F(x)_i integral and = x_i mod p for ALL component vectors
    (p in {2,3} length 5; p = 5 length 4) - F = id on W(F_p) at
    component level; Dwork integrality of constant-ghost vectors
    (p in {2,3,5}, |c| <= 20).  PASS (TR = W is a transport)
Y6  Epstein: 1,4,6,9,36 represented; 4, 6, 9 irreducible; 36 = 4*9
    = 6*6 -> no valuation; DH by Y2's predicates + HH H6b.  PASS
Y7  agreement locus = the 35 prime powers <= 100, proper in the
    99-point spectral domain.  PASS (the P3-a shape, measured)
```

## 6. What the audit settles

(i) THE CLEAN NEGATIVE, with transports named (sec 2 table stands as
registered): no banked identity except rows 9-10 has two independent
evaluations. The recurring transports are exactly four: dictionary/
comparison-map (rows 1, 2), Poisson (11, 14), regularization-is-the-
continuation (2, 5), and finite linear algebra on defining data
(3, 8, 16). This SHARPENS clause 6's difficulty as the task card
intended: two years of banked exact identities produced two routes to
many numbers and a second evaluation of essentially none.

(ii) THE EMBRYO IS REAL AND LOCATED: q^w - 1 is the one banked number
with two independent evaluations (geometric Frobenius count; Adams-
eigenvalue determinant), agreement by Quillen's theorem, independence
certified BOTH ways by the P3 deformation tests. Its determinant dress
is Hesselholt's Theorem A at Spec F_q. The Weil pattern is therefore
PRESENT in the trace-methods corpus - at precisely the carrier whose
spectrum is empty. Clause 6 is not a request for a new kind of
identity; it is the request to move THIS identity's agreement locus to
a carrier with a nonempty odd slot (BC3) - the same archimedean seat
named by HH/31-B/BB/QQ/UU.

(iii) THE TR QUESTION ANSWERED (task item 3, special attention):
Witt = fixed-point data is DEFINITIONAL (natural iso + F = id at F_p,
both witnessed at their computational cores); the trace world's
genuine second evaluation enters at DGM (K = TC), where the banked
p-adic blindness (v_p(q^w - 1) = 0) shows the two evaluations
currently meet only where the content is trivial: the p-complete
trace evaluates the empty p-part of the count. BC4 is the precise
upgrade demand.

(iv) THE INVERSE-PROBLEM FEED: BC1 (extension asymmetry as an
arrival test - operational G-CH3), BC2 (rigidity split: unknown on
the spectral side), BC3 (nonempty odd determinant slot), BC4 (a
DGM-type comparison nontrivial at one place) are boundary conditions
on the WW silhouette: any structure whose trace produces the shadows
must ALSO present the Y7 locus shape.

## 7. G-INT6 ledger

```text
input                          choices spent
audit scope (17 identities)    the task card's list + every banked
                               identity found in required reading;
                               completeness relative to the corpus map
                               (proof/README + work/), not absolute
P3 criterion                   derived from doc 14 F2/P1-P2 + UU's
                               characterization; clause (c) [spectrum]
                               added by me - LOGGED as the one design
                               choice (it is what separates "escalate"
                               from "embryo"; without it row 9 would
                               escalate vacuously)
Y1 ambient F_{q^{2w}}          forced (the count must live in a field
                               STRICTLY larger than the fixed field,
                               else it is a tautology)
Y3 twist family c x^q          the standard semilinear deformation
                               class (H^1-shaped); chosen as the
                               minimal geometric deformation; logged
grids (k <= 100, w <= 6, ...)  calibration, registered before run 1
zeros                          NONE consumed (no fork_lib, no freeze)
```

Carrier guard: Y6 (Epstein two-factorization kill, exact; DH by Y2 +
HH H6b). The only constructed object in this memo is the P3 test
itself; it consumes nothing arithmetic. Freeze protocol: NOT TRIGGERED
- no quantity in this memo touches or could touch zero positions.

## 8. Honest limits

- The audit's completeness is relative to the banked-corpus map
  (proof/README.md + the work/ files in the required-reading closure);
  identities in unread cycle docs are covered only insofar as the
  README synopses expose them. Row 17 is from record, not re-derived.
- P3-c ("nontrivial spectrum") is my addition to the criterion; it is
  what makes the verdict "embryo" rather than "sleeper". If the
  program later prefers the bare (a)+(b) criterion, row 9 is a PASS
  and the escalation stands - the deformation evidence is witnessed
  either way.
- Y1's evaluation B is the pi_*-level Adams eigenvalue (the banked
  shadow, W-doc sec 2.3); the spectrum-level fib(psi^q - 1) = K(F_q)
  is Quillen's theorem, cited not recomputed. The witness certifies
  the two NUMBERS and their deformation behavior, not the homotopy
  theory.
- Y5 witnesses F = id and Dwork integrality at truncation lengths
  4-5; the natural-iso TR_0 = W (HM Thm F) is cited, not recomputed
  (no THH machinery here).
- The embryo finding makes no claim that globalizing it is possible -
  B1-B3 stand exactly as W-doc proved them; the finding is that the
  inverse problem's clause 6 has a nonvacuous local model, which
  constrains the search (BC1-BC4) without advancing it.

## 9. Hand-off

```text
VERDICT:    ZERO decision-grade sleepers. 15 of 17 banked identities
            are ONE evaluation with transport named (sec 2); 1 is a
            non-pair (genus clash); 1 pair - q^w - 1 (Quillen) with
            its Hesselholt-Thm-A dress - passes P3-a/b BOTH ways and
            fails P3-c provably: TWO-EVAL EMBRYO.
P3:         stated in sec 1 in doc-14-ready form (extension test +
            content + spectrum); proposed as the standing G-CH3
            arrival test.
TR ANSWER:  Witt = fixed points is definitional (functor transport;
            F = id at F_p, witnessed); the trace world's true second
            evaluation is Quillen-vs-TC via DGM, currently meeting
            only on the trivial p-part - clause 6 in embryo, blocked
            by exactly B1-B3.
BOUNDARY    BC1 extension asymmetry (arrival test), BC2 rigidity
CONDITIONS: split (unknown on the spectral side), BC3 nonempty odd
            determinant slot (TP_od != 0 globally), BC4 a DGM-type
            comparison nontrivial at one place. Feed to WW's inverse
            problem.
WITNESS:    prime_yy_second_evaluation_audit.py (Y1-Y7, ALL PASS,
            exit 0, first run untouched, deterministic x3, < 1 s;
            no zeros consumed, no freeze needed).
```
