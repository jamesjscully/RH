# ZZ - M1: the solenoid Lefschetz - the composition of the cycle's three headline facts, executed

Status: fresh-context worker ZZ, 2026-06-11. Doc 39 sec 4 move M1
(the critic's composition: transplant YY's embryo onto XX's solenoid
rung, under WW's conformance instrument). Required reading executed in
order: doc 39, doc 38, YY-b2-second-evaluation.md IN FULL (P3 is the
decision instrument), XX-b1-liquid.md (S_p; T1 + complement N1-N5),
WW-silhouette-dossier.md (shape law; the BC1 12-number test).
Inherited witnesses rerun by me BEFORE any new work:
prime_yy_second_evaluation_audit (ALL PASS Y1-Y7, exit 0),
prime_ww_silhouette (ALL PASS WW1-WW14, exit 0),
prime_xx_b1_liquid (ALL PASS XB1-XB8, exit 0).

New witness (pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_zz_solenoid_lefschetz
    (gates Z1-Z8; exit 0 iff ALL PASS)

DISCLOSURE (YY/XX precedent): sections 0-3 (the derivations, the P3
adjudication, the registered expectations, the gate list) were written
BEFORE the witness file existed; the witness was then written to the
registered gates and run; the verdict sections (4-7) were filled after.
Every decision gate is exact integer/Fraction arithmetic; mpmath dps 50
only for the Z6/Z7 analytic values (registered coarse tolerances - the
decisions there have margins > 0.5). NO ZEROS CONSUMED: no fork_lib
import, no freeze step required (every quantity below is
algebra/counting on the solenoid or closed-form Gamma data).

PRE-REGISTERED EXPECTATIONS (both ways carried, fail-closed):
(E-a) the two evaluations agree exactly (count = |Lefschetz| via the
product formula) - a mismatch would be a reportable shock (it would
mean classical solenoid dynamics is wrong);
(E-b) the P3 verdict is expected to be the PONTRYAGIN/INVERSE-LIMIT
TRANSPORT KILL (full value, pre-authorized by the task card); the
alternative (a genuine two-evaluation surviving the transport
adjudication) would be an escalation at NN-grade scrutiny;
(E-c) the BC1 12-number test is expected NONCONFORMANT for the flow's
intrinsic defect (the solenoid carries no Gaussian); conformance would
be a shock requiring freeze-grade review of WW's exclusion clause.

## 0. The object and the two evaluations, derived exactly

### 0.1 Setting

S_p = (Q_p x R)/Z[1/p] (XX T3, witnessed XB7): compact connected
abelian, Pontryagin dual S_p-hat = Z[1/p] (discrete), Cech
H^0(S_p; Z) = Z, H^1(S_p; Z) = Z[1/p] (XB8; H^1(X;Z) = Hom(X,T) =
X-hat for compact connected abelian X, natural iso), H^{>=2} = 0
(colim of circle cohomology). End(S_p) = Z[1/p] acting by
multiplication (dual to multiplication on Z[1/p]); x p is an
AUTOMORPHISM (1/p is in the ring). Under the tower presentation
S_p = lim(S^1 <- S^1, z -> z^p), the map x p is the shift.

### 0.2 Evaluation A - the periodic-point count (classical; derived)

For alpha in Z[1/p], alpha != 1-root case excluded (alpha^w != 1):

    Fix(x alpha^w) = ker(alpha^w - 1 : S_p -> S_p)   (definitional)
    #ker(g)        = #coker(g-hat : Z[1/p] -> Z[1/p]) (Pontryagin)
    coker(x beta on Z[1/p]) = Z[1/p]/(b) = Z/|b|,  where
        beta = alpha^w - 1 = b p^m, b in Z, p does not divide b,
    so #Fix(x alpha^w) = |b| = |alpha^w - 1|_oo * |alpha^w - 1|_p.

THE CLASSICAL ANSWER IS A PRODUCT-FORMULA EXPRESSION over exactly the
solenoid's two places S = {p, oo} (Lind-Ward 1988, "Automorphisms of
solenoids and p-adic entropy", ETDS 8, where also h(x alpha) =
sum_{v in S} log^+ |alpha|_v). Specializations, all to be witnessed:

```text
alpha = p:    #Fix(p^w) = (p^w - 1) * 1        carried at oo alone
                                               (|p^w - 1|_p = 1: the
                                               SAME p-blindness as
                                               YY W3b, v_p(q^w-1)=0)
alpha = 1/p:  #Fix = ((p^w-1)/p^w) * p^w       carried at p alone -
              = p^w - 1                        same count, places
                                               SWAPPED
alpha = 3/2 on S_2 (w-th power):               BOTH places active:
              #Fix = ((3^w-2^w)/2^w) * 2^w = 3^w - 2^w
alpha = 4 on S_3, w even:                      p-adic factor active:
              #Fix = (4^w - 1) * |4^w - 1|_3 < 4^w - 1
```

### 0.3 Evaluation B - the trace on H^*

x alpha^w acts on H^0 = Z as identity (connected space): trace 1. On
H^1 = Z[1/p]: multiplication by alpha^w. Z[1/p] has INFINITE rank over
Z - the naive Z-trace is undefined. The pre-registered options:

(z-i) INVERSE-LIMIT / FINITE-LEVEL TRACES: H^1 = colim(Z -p-> Z); for
alpha = p the endomorphism acts on EVERY level-k copy of Z as
multiplication by p^w, commuting with the bonding maps. The
finite-level trace is p^w AT EVERY LEVEL - the tower of traces is
CONSTANT and its limit exists trivially. Equivalently and more
honestly: H^1 is FREE OF RANK 1 over the base ring Z[1/p], and the
trace of x alpha^w over that base is alpha^w in Z[1/p]. NO
REGULARIZATION IS NEEDED - what is needed is a base change of the
coefficient ring (Z -> Z[1/p]). The Lefschetz element is

    L(alpha^w) = tr H^0 - tr H^1 = 1 - alpha^w  in Z[1/p].

(z-ii) THE PAIR: the trace is an element of Z[1/p], not a cardinality.
The count is recovered from it by the PRODUCT FORMULA over the
solenoid's places:

    #Fix(x alpha^w) = prod_{v in {p, oo}} |L(alpha^w)|_v.

This is where the archimedean place enters: |.|_oo applied to the
algebraic Lefschetz element. For alpha = p the oo-factor carries
everything; for alpha = 1/p the p-factor does; for alpha = 3/2 both
are load-bearing. NEITHER PLACE SUFFICES UNIFORMLY - the pair is
forced (registered gate Z2).

(z-iii) divergence: FALSE - nothing diverges once the base ring is
right.

READING (registered): z-i and z-ii are BOTH true and compatible; the
"regularization" question dissolves into a base-change plus the
product formula. The unit's entrance is NOT in the trace (which is
algebraic, place-free) but in the TRACE -> COUNT BRIDGE: the
archimedean absolute value of the Lefschetz element. That is the same
covolume-1/product-formula fact as XB7 - bookkeeping the program
already owns, not new structure.

### 0.4 Entropy

h(x alpha) = sum_{v in {p, oo}} log^+ |alpha|_v (Lind-Ward): for
alpha = p: log p + 0; for alpha = 1/p: 0 + log p (same entropy,
opposite carrying place); for alpha = 3/2 on S_2: log(3/2) + log 2 =
log 3. Also h = lim_w (1/w) log #Fix(alpha^w) (witnessed Z6). The
scale log p IS produced by a non-sheaf invariant - T1 is evaded via
its complement (N1/N3: the metric/group/measure data the homotopy type
forgets). HONEST DEMOTION, registered: the entropy is log of the
H^1-eigenvalue, i.e. log of the chosen map's own degree - the scale is
SUPPLIED by the endomorphism, not read from the category. The
solenoid-with-map carries (address, scale) = (Z[1/p], log p), but both
are inputs of the construction, not outputs of a trace.

## 1. P3 EXECUTED on the pair (count, trace)

Applying YY sec 1 verbatim.

### 1.1 P3-a direction 1 (B moves, A's carrier dies)

The spectral expression lambda^w - 1 is defined for EVERY lambda
(rational, real). The carrier predicate for the count is
lambda * Z[1/p] subset Z[1/p], i.e. lambda in Z[1/p]: for lambda with
a prime q != p in its denominator (1/3 on S_2, 1/2 on S_3, 5/6 on S_5,
2/7 on S_2) the endomorphism does not exist - no map, no count - while
the spectral value moves freely (gate Z4). QUADRATIC SHARPENING: for
lambda = 1 + sqrt(2) (Pell unit), lambda^w - 1 is irrational for all
w >= 1, while EVERY compact-abelian carrier realizing eigenvalue
lambda (the companion-matrix torus [[2,1],[1,0]]) computes the GALOIS
PRODUCT |det(A^w - I)| = |N(lambda^w - 1)| in Z - an integer. The
carrier can compute the norm but can NEVER compute the single
eigenvalue's expression: the count side demands the full place/Galois
orbit (gate Z4b). Direction 1 PASSES formally.

### 1.2 P3-a direction 2 (A moves, B untouched)

REGISTERED DISANALOGY with YY's Y3: on S_p the affine twists
x -> alpha x + c move NOTHING - Fix is a torsor under ker(1 - alpha):
#Fix(px + c) = p - 1 for every c (gate Z5a). The geometric side of the
solenoid pair has STRICTLY LESS deformation freedom than the F_q side
(where the semilinear twists moved the count over {1, q}). The freedom
that does exist lives at the agreement's content level - the circle:
perturb f(theta) = p*theta by an exact piecewise-linear wiggle
(rational breakpoints, Fraction arithmetic): with epsilon = 2/5,
triangle wave of period 1/2 and slopes +-8, the raw fixed-point count
moves 1 -> 5 (p = 2) while the SIGNED count (Hopf indices
sgn(1 - f')) stays = L = 1 - p = -1 and the degree (trace side) is
untouched - exact, gate Z5. On the solenoid itself the wiggle
F(x) = px + iota(u(pi_0(x))) (u : S^1 -> R into the R-leaf through 0)
exists, is homotopic to x p through F_t (H^* action invariant), and
its fixed-point equation (1-p)x = iota(u(pi_0 x)) decouples through
pi_0 to the circle count with finite fibers - stated, not enumerated
(the witnessed core is the circle level, which is where the content
sits; see 1.3). Direction 2 PASSES formally, with the freedom located
at circle level.

### 1.3 P3-b (content) - THE ADJUDICATION

The agreement proof for the pair AS COMPUTED (group endomorphisms,
the only locus where the solenoid count is defined and exact) is the
chain of sec 0.2:

    Fix = ker            definitional (group structure)
    #ker = #coker(dual)  Pontryagin duality - NATURAL ISO
    X-hat = H^1          natural iso (compact connected abelian)
    #coker = prod |.|_v  Smith/localization + product formula -
                         finite linear algebra on defining data

EVERY step is an isomorphism or definitional linear algebra inside
ONE structure (the dual pair (S_p, Z[1/p])). Per P3-a's transport
clause verbatim, this is ONE EVALUATION: transport = Pontryagin
duality composed with inverse-limit/colimit bookkeeping and the
product formula. The extension asymmetry of 1.1/1.2 is real but NOT
cut by a theorem on the solenoid: the locus where content would have
to live - non-affine continuous maps of S_p, where direction-2
freedom sits - is exactly where NO Lefschetz fixed-point theorem
exists (S_p is not an ANR and not even movable in the shape-theoretic
sense; the classical FPT hypotheses all fail). The only genuine
content in the whole picture is the CIRCLE's Hopf index theorem
(signed count = 1 - deg for arbitrary continuous circle maps,
degree theory), and the solenoid agreement is that fact transported
up the tower on the affine locus. Contrast Quillen (YY row 9): no
duality relates G_m(F_q-bar) points to KU - the agreement there
consumes the +-construction. Here the agreement consumes nothing
beyond duality.

### 1.4 P3-c (spectrum)

What does the agreement constrain? The eigenvalue of x p on H^1 - p
itself, i.e. THE MAP'S OWN DEGREE, forced by construction. The
dynamical zeta is exactly computable:

    zeta_{x p}(z) = exp(sum_w #Fix(p^w) z^w / w) = (1 - z)/(1 - pz),
    in s-coordinates (z = p^{-s}):  (1 - p^{-s})/(1 - p^{1-s}):

poles on Re s = 0, zeros on Re s = 1 - both combs at the place's own
frequencies 2 pi n / log p (the S11/BC5 spectrum!), and "RH for the
solenoid" (zeros on Re s = h/log p = 1) is TRIVIALLY TRUE AND EMPTY:
the zero line is the entropy restated, supplied by the map. NO
UNFORCED SPECTRAL PARAMETER EXISTS. P3-c FAILS.

### 1.5 Registered P3 verdict logic

ONE-EVALUATION (Pontryagin/inverse-limit transport) at solenoid grade;
the residual genuine (a)+(b) micro-pair is the circle Hopf pair, which
is WEAKER than the Quillen embryo (its agreement theorem is
1-dimensional degree theory; its spectrum is the homotopy class's
degree, forced) and fails P3-c identically. THE KILL IS FULL-VALUE,
as the task card pre-authorized. The decisive sharpening it buys is
sec 5's BC-E3 amendment.

## 2. The BC1 conformance test (WW's 12-number instrument)

### 2.1 The flow's per-place trace defect, derived

The suspension flow of x p on S_p has closed orbits at t = w log p.
The natural smoothed-vs-exact comparison (CERT 1's language: smoothed
self-dual count against exact partition count): the equilibrium/Haar
prediction at time w log p is p^w = e^{wh}; the exact count is
p^w - 1. Weighting orbit atoms by #Fix(p^w)/p^w gives the per-place
flow trace

    nu_p = sum_{w>=1} (log p)(1 - p^{-w}) delta_{w log p}
         = Lambda-comb + DEFECT,  DEFECT = -sum_w (log p) p^{-w}
                                            delta_{w log p},

(equivalently: nu_p is the atom expansion of -d/ds log zeta_{x p}(s)).
The defect's transform at the place's OWN frequencies
xi_n = 2 pi n / log p is EXACT and FLAT:

    DEFECT-hat(xi_n) = -(log p) sum_w p^{-w} e^{-2 pi i n w}
                     = -(log p)/(p - 1)   for ALL n  (exact identity).

### 2.2 The 12-number comparison, registered

Shape law (WW S2): mode_0 = gamma + log pi = +1.7219...; mode_n =
-Re Gamma_R(2 pi i n / log p) for n >= 1, collapsing doubly fast.
Flow defect: mode_n = -(log p)/(p-1) for all n: -0.693 / -0.549 /
-0.402 / -0.324 at p = 2/3/5/7 - WRONG SIGN and p-DEPENDENT at n = 0
(vs the universal +1.7219), and FLAT in n (ratio r_n = mode_n/mode_0
= 1 exactly) where the shape law collapses (|r_1| < 0.1 at all
p <= 7). REGISTERED GATES (Z7): |flow - shape| > 0.5 at n = 0 for all
four p; |r_1^flow - r_1^shape| > 0.5 and |r_2^flow - r_2^shape| > 0.5
at all four p: NONCONFORMANT at all 12 numbers. RECORD (no gate): the
solenoid's orbit-length comb is (log p)Z - the comb ADDRESS is the
banked one (tautologically conformant; it is XB3's comb); the failure
is strictly at the UNIT level: the solenoid's intrinsic defect is
p-adic-geometric (the Euler tail p^{-w}), not the archimedean Gaussian
silhouette. Consistent with WW BC1's exclusion ("any non-Gaussian
unit changes every c_n") and with XX's three-row ladder: the solenoid
is place-addressed but the unit's scale-silhouette must come from the
liquid layer.

## 3. PRE-REGISTERED GATES (written before the witness existed)

Exact = integer/Fraction; numeric = mpmath dps 50, coarse registered
tolerances.

```text
Z1 THE COUNT (exact): p in {2,3,5}, w <= 6: (a) coker route:
   Z[1/p]/(p^w - 1) = Z/(p^w - 1) (p invertible mod m witnessed);
   (b) enumeration route: the m = p^w - 1 candidates x_j = j/m are
   fixed, pairwise distinct in S_p ((i-j)/m in Z[1/p] iff m | i-j,
   exact), and complete (any fixed point lies in (1/m)Z[1/p]/Z[1/p]
   = Z/m). #Fix(p^w) = p^w - 1 both routes. FAIL: any mismatch.
Z2 PRODUCT FORMULA / z-ii (exact): cases (p, alpha) in
   {(2,2), (2,1/2), (2,3/2), (3,4), (3,1/3), (5,1/5), (7,2)},
   w <= 6: |coker(alpha^w - 1)| = |alpha^w - 1|_oo * |alpha^w - 1|_p
   exactly (Fraction absolute values); at least 4 (case, w) instances
   with the p-adic factor != 1; the alpha <-> 1/alpha count symmetry
   with carrying place SWAPPED (recorded per case). FAIL: any.
Z3 TRACE TOWER / z-i (exact): alpha = p, levels k <= 6: level trace
   = p^w constant; L = 1 - p^w; prod_v |L|_v = Z1's count. General
   alpha of Z2: L = 1 - alpha^w in Z[1/p], prod_v |L|_v = Z2's count.
   FAIL: any.
Z4 P3-a DIRECTION 1 (exact): (a) lambda in {1/3 on S_2, 1/2 on S_3,
   5/6 on S_5, 2/7 on S_2}: spectral lambda^w - 1 defined (Fraction),
   carrier predicate lambda*Z[1/p] subset Z[1/p] FAILS (denominator
   prime != p exhibited); controls alpha in Z[1/p] pass the
   predicate. (b) Pell: lambda = 1 + sqrt(2): for w <= 8,
   lambda^w = a_w + b_w sqrt(2) with b_w >= 1 (so lambda^w - 1
   irrational); A = [[2,1],[1,0]]: |det(A^w - I)| = |N(lambda^w - 1)|
   = |(a_w - 1)^2 - 2 b_w^2| in Z, >= 1: the carrier computes the
   norm, never the single eigenvalue. FAIL: any clause.
Z5 P3-a DIRECTION 2 (exact): (a) affine rigidity: p in {2,3,5},
   sampled c: #Fix(px + c) = p - 1 (the torsor count via
   #ker(1-p) = p - 1, c-independent; exact). (b) PL wiggle, p = 2,
   epsilon = 2/5, triangle wave period 1/2 slopes +-8: piecewise
   Fraction solve: raw count = 5, signed count = -1 = 1 - p,
   degree = 2 (f(theta+1) = f(theta) + 2, structural); control
   epsilon = 0: raw = 1 = |L|. FAIL: any.
Z6 ENTROPY (exact ledger + numeric): ledgers log^+|p|_oo + log^+|p|_p
   = log p + 0, swapped for 1/p, and log(3/2)+log 2 = log 3 for 3/2
   on S_2 (exact bookkeeping of log^+ via Fractions/valuations,
   identity checked at dps 50, tol 1e-30); growth route:
   |(1/w) log(#Fix from Z2) - h| < 2 p_eff^{-w}/w at w = 40
   (tol checked numeric, alpha = p case and alpha = 3/2 case with
   h = log 3). FAIL: any.
Z7 BC1 CONFORMANCE (numeric, decisive margins > 0.5): flow modes
   -(log p)/(p-1) (closed form; ALSO recomputed as a truncated sum,
   agreement < 1e-30); shape modes: mode_0 = gamma + log pi, mode_n
   = -Re Gamma_R(2 pi i n/log p) (mpmath); for p in {2,3,5,7}:
   |flow_0 - shape_0| > 0.5; |r_1^flow - r_1^shape| > 0.5;
   |r_2^flow - r_2^shape| > 0.5 (r_n = mode_n/mode_0). Registered:
   NONCONFORMANT at all 12. FAIL: any margin < 0.5 (i.e. any
   conformance = shock, fail-closed).
Z8 CARRIER GUARD (exact): Epstein x^2 + 5y^2: 4, 6, 9 represented
   irreducible, 36 = 4*9 = 6*6 (rerun); WHERE THE SOLENOID DIES:
   (a) Z[1/4] = Z[1/2] (1/2 = 2/4, exact ring equality both
   inclusions): the cocompact construction CANNOT remember the
   irreducible 4 - it factors through prime support; (b)
   lattice(4*9) = Z[1/2,1/3] = lattice(6*6) while the irreducible
   multisets {4,9} != {6,6} (exponent vectors (2,0)+(0,2) vs
   (1,1)+(1,1): equal sums, different multisets, exact): the
   per-irreducible solenoid address/entropy ladder is unformable
   without primes; (c) #Fix(x 36) on the Z[1/6]-solenoid = 35
   through EITHER factorization (the object never sees the
   factorization). DH: no carrier monoid (record). FAIL: any.
```

Registered verdict logic: ALL PASS -> E-a/E-b/E-c stand as written
(secs 1.5, 2.2); any Z1-Z3 failure = reportable shock (classical
dynamics broken); a Z7 conformance = shock + freeze-grade review;
Z4/Z5 failures would refute the P3-a claims and re-open the
adjudication.

---- verdict sections written after the runs ----

## 4. VERDICT: ALL PASS (Z1-Z8, exit 0) - THE COMPOSITION COMPUTES,
## AND THE AGREEMENT IS THE PRE-REGISTERED TRANSPORT KILL

Witness ALL PASS (Z1-Z8, exit 0; deterministic across 3 runs, logs
/tmp/zz_run{1,2,3}.log byte-identical; < 1 s). ONE ENGINEERING FIX,
disclosed: run 1 aborted on a KeyError in Z3 (the alpha = p bridge
check looked up the Z2 case dictionary, which does not contain
(3, 3)/(5, 5); fixed to compare against Z1's count p^w - 1 directly -
computational lookup only, no gate predicate, tolerance, or registered
reading was amended). All gates then passed on the first complete
evaluation.

```text
Z1 #Fix(p^w) = p^w - 1 exact, both routes (coker + literal
   enumeration with distinctness/completeness), p in {2,3,5}, w <= 6.
Z2 count = |alpha^w - 1|_oo * |alpha^w - 1|_p exact at 42 (case, w)
   instances; 32 instances with p-adic factor != 1; place-swap
   symmetry alpha <-> 1/alpha exact (oo-carried vs p-carried,
   same count, p in {2,3,5}, w <= 6).
Z3 tower traces constant = p^w (levels 0..6); L = 1 - alpha^w in
   Z[1/p]; prod_v |L|_v reproduces Z1/Z2 at every instance.
Z4 direction 1: four non-carriers killed by exact denominator
   witness with spectral value alive; Pell: b_w >= 1 (w <= 8),
   |det(A^w - I)| = |N(lambda^w - 1)| exact integers
   {2, 4, 14, 32, 82, 196, 478, 1152}: the carrier computes the
   norm, never the single irrational eigenvalue expression.
Z5 direction 2: affine rigidity #Fix(px+c) = p-1 all c (exact);
   PL wiggle raw count 1 -> 5 with signed count -1 = 1 - p invariant
   and degree 2 structural; control epsilon = 0 raw = 1.
Z6 entropy ledgers exact (log p / swapped / log 3); growth route
   converges within registered bounds at w = 40.
Z7 NONCONFORMANT AT ALL 12 NUMBERS, margins all > 0.5 (smallest
   margin 0.9159 at (p=7, n=1); n=0 margins > 2.0: flow means
   -(log p)/(p-1) vs the universal +1.7219; flow modes flat in n,
   shape modes Gamma_R-collapsing); closed form vs truncated sum
   < 1e-30.
Z8 Epstein: Z[1/4] = Z[1/2] exact; lattice(4*9) = lattice(6*6) with
   distinct irreducible multisets; #Fix(x 36) = 35 through either
   factorization; DH no carrier. The solenoid functor factors
   through prime support - without unique factorization the
   per-irreducible address does not exist.
```

## 5. What M1 settles

(i) THE TWO EVALUATIONS, EXACTLY: #Fix(x p^w | S_p) = p^w - 1 =
|coker(x(p^w - 1) | Z[1/p])|, and L = 1 - p^w with the trace taken in
the base ring Z[1/p] (rank-1 free; finite-level traces constant);
count = prod_{v in {p, oo}} |L|_v. The Lefschetz number of the
solenoid is the QUILLEN NUMBER (q^w - 1 at q = p) relocated to a
carrier with nonempty odd slot - the composition the critic asked for
is real and exactly computable.

(ii) Z-READING: z-i TRUE (trace exists via the tower, constant
levels; equivalently base-change to Z[1/p] - no regularization);
z-ii TRUE AND LOAD-BEARING (the count IS the product-formula
expression; witnessed with each place separately carrying the count
under alpha <-> 1/alpha and both active for alpha = 3/2); z-iii
FALSE. The unit's entrance is NOT in the trace: it is |.|_oo applied
to the algebraic Lefschetz element at the trace->count bridge - the
product formula's archimedean factor, i.e. the covolume-1 fact (XB7)
the program already owns. For alpha = p the p-adic factor is
identically 1: the SAME p-blindness as YY W3b - the trace at p sees
exactly the trivial part of the count, here as there.

(iii) P3 VERDICT: ONE-EVALUATION - PONTRYAGIN/INVERSE-LIMIT TRANSPORT
(the pre-registered full-value kill). P3-a passes formally both ways
(Z4, Z5), but the agreement proof on the computable locus is a chain
of natural isomorphisms (Fix=ker, Pontryagin, X-hat = H^1,
Smith/product formula) inside the dual pair - P3-a's transport clause
applies verbatim. The extension asymmetry is not cut by a theorem on
the solenoid: where direction-2 freedom lives (non-affine maps), no
Lefschetz FPT exists (S_p is not an ANR, not movable); the only
content is the circle's Hopf index theorem, transported up the tower.
P3-c fails decisively: the constrained spectrum is the map's own
degree p; the dynamical zeta (1-p^{-s})/(1-p^{1-s}) has its zeros on
Re s = 1 = h/log p BY SUPPLY - solenoid-RH is true and empty. The
embryo transplanted onto the nonempty odd slot DOES NOT WAKE.

(iv) WHY IT DOES NOT WAKE - THE SHARPENING (the cycle's real
purchase): BC-E3 demanded a NONEMPTY odd slot; the solenoid delivers
one (H^1 = Z[1/p] != 0) and the agreement still has no decision
content, because the odd slot's eigenvalue is FORCED - supplied by
the endomorphism's own construction. NONEMPTY IS NOT ENOUGH. The
demand composes with BC2 (rigidity split) into the corrected form:

    BC-E3' (amended): a nonempty odd determinant slot whose
    eigenvalues are NOT definitionally supplied by the acting
    map/correspondence - the slot must be filled by the structure,
    queried by the map, with the unknown on the spectral side.

The solenoid fails BC-E3' in the complementary way to F_q: at F_q the
slot is empty (TP_od = 0); on S_p the slot is nonempty but
self-supplied. The missing object must do neither.

(v) BC1 CONFORMANCE: NONCONFORMANT at all 12 numbers (Z7) - exactly
as registered. The solenoid flow's intrinsic defect is the Euler tail
-(log p) p^{-w} (flat modes -(log p)/(p-1), wrong sign, p-dependent
mean), not the Gaussian/Gamma_R silhouette. The solenoid supplies the
ADDRESS (the (log p)Z orbit comb, tautologically the banked comb) and
exact counts; the unit's archimedean silhouette is not in it -
consistent with the three-row ladder (scale-silhouette lives in the
liquid layer) and with WW's BC1 exclusion clause. The two instruments
(P3, BC1) agree: the solenoid is a CARRIER-GRADE object, not a
unit-grade one.

(vi) ENTROPY DEMOTED HONESTLY: h = log p is scale through a non-sheaf
invariant (T1 evaded via N1/N3), but it is log of the forced
H^1-eigenvalue - supplied, not read. Lind-Ward's h = sum_v log^+ is
the product formula again. The solenoid evades T1 only by carrying p
in its own definition.

## 6. G-CH2 full-ledger score (the package: (S_p, x p, H^*, counts))

```text
C1 (kappa = pi, density read)   FAIL - no pi anywhere; integer counts.
C2 (continuum unit per place)   FAIL - defect is p-adic-geometric
                                (Z7); no continuum payment.
C3 (rational/Anderson layer)    CONTACT (new!): H^1 = Z[1/p] is a
                                rational-layer object sitting in an
                                odd cohomological slot - the FIRST
                                banked object touching the C3 column
                                at all; no mechanism (nothing
                                Anderson-fractures), but the column
                                is no longer empty of addresses.
C4 (signed archimedean, joint)  FAIL - |.|_oo enters unsigned.
C5 (FE homogenizer unit class)  FAIL - no FE layer.
C6 (second evaluation)          FAIL at decision grade - sec 5(iii).
FF index shape                  PASS-shaped (1 - alpha^w = h^0 - h^1).
FF integrality                  PASS (counts, ledgers integer-exact).
FF effectivity                  PARTIAL (counts >= 1 trivially; no
                                h^0 >= 0 mechanism).
FF monoid family                PASS (p^Z address; dies on Epstein at
                                the prime-support collapse, Z8).
FF growing observable           FAIL (growth is in the iterate w, one
                                evaluation; the depth wall needs
                                growth in the window a against a
                                second evaluation).
```

Score ~4/11 with one new column entry (C3 contact). Carrier guard:
Z8 - the solenoid functor factors through prime support (Z[1/4] =
Z[1/2]; lattice blind to the factorization 4*9 vs 6*6): no
Z[1/q]-cocompact structure exists per Epstein-irreducible; the Euler
product is load-bearing for the ADDRESS itself.

## 7. G-CH1, ledger, limits, hand-off

G-CH1 (which footnote should be a gate): BC-E3' (sec 5(iv)) - every
arriving odd-slot candidate must answer "WHO SUPPLIES THE SLOT'S
EIGENVALUE?" on arrival; self-supplied (by the acting map's
construction) = embryo-asleep regardless of nonemptiness. Propose as
a standing amendment to P3-c and to the BC-E3 registry entry.

G-INT6 ledger:

```text
input                       choices spent
S_p, H^*, counts            XX XB7/XB8 + classical (Lind-Ward 1988,
                            Pontryagin duality, Cech continuity) -
                            derived in sec 0, witnessed exact
alpha sample set (Z2/Z4)    calibration, registered before run 1;
                            chosen to exhibit each place carrying
PL wiggle (Z5)              the minimal exact non-affine deformation
                            (rational breakpoints); LOGGED design
                            choice - sin-wiggles would need numerics
flow-defect normalization   #Fix/p^w (Haar/equilibrium weighting) -
                            LOGGED as the one Z7 design choice; the
                            FLATNESS of the modes at xi_n is
                            normalization-free (any one-sided
                            geometric weighting is flat there), so
                            the nonconformance does not depend on it
zeros                       NONE consumed (no fork_lib); freeze NOT
                            TRIGGERED (expected none: confirmed)
```

Honest limits:
- The solenoid wiggle (1.2) is constructed and its homotopy
  invariance argued, but its fixed points are not enumerated on S_p;
  the witnessed direction-2 core is the circle level. Since the
  verdict is the transport kill, this weakens nothing the verdict
  uses (it could only have strengthened an escalation that did not
  happen).
- "No Lefschetz FPT for solenoids" is cited at the hypothesis level
  (non-ANR, non-movable - classical shape theory); no counterexample
  to a putative solenoid FPT is constructed here.
- Z7's flow-trace normalization is one of several conventions
  (Ruelle/Guillemin weightings differ by the (1 - p^{-w}) factor's
  placement); the ledger logs it, and the decisive flatness-at-xi_n
  is convention-independent.
- Lind-Ward is cited for the general formula; the witness proves the
  instances it uses (Z1-Z3 are self-contained exact computations).
- The C3 "contact" is an address-level observation, not a computed
  C3 shadow; WW's empty-column caveat stands.

Hand-off:

```text
EVALUATIONS: #Fix(x p^w | S_p) = p^w - 1 (exact, two routes);
             L = 1 - p^w, trace in the base ring Z[1/p] (tower
             constant); count = prod_{v in {p,oo}} |L|_v (z-i AND
             z-ii; z-iii false). The unit enters at the trace->count
             bridge as |.|_oo - the product formula, not a
             regularization.
P3:          ONE-EVALUATION - Pontryagin/inverse-limit transport
             (pre-registered kill, full value). P3-a passes both
             ways formally; the agreement proof is a natural-iso
             chain; the content locus (non-affine maps) has no FPT
             on the non-ANR solenoid; P3-c fails (spectrum = the
             map's own degree; solenoid-RH true and empty).
SHARPENING:  BC-E3' - nonempty odd slot is NOT enough; the slot's
             eigenvalues must be unforced (not supplied by the
             map's construction). F_q fails by emptiness, S_p by
             self-supply; the missing object must do neither.
             Proposed as a standing gate (G-CH1).
BC1:         NONCONFORMANT at all 12 numbers (margins > 0.5): the
             solenoid carries the comb address, not the Gaussian
             silhouette. P3 and BC1 agree: carrier-grade, not
             unit-grade.
WITNESS:     prime_zz_solenoid_lefschetz.py (Z1-Z8, ALL PASS,
             exit 0, deterministic x3; no zeros, no freeze).
```
