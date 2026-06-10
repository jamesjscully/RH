# T - The branch fork: DECIDED at filtration 0 (branch (i), three normalizations), abutment pinned to two named ambiguities at degree 2p

Status: 2026-06-10, worker T (fresh context, resuming a cut-off
predecessor). Witness: prime_twisted_fork_filtration_zero.py (inherited
half-finished; validated, corrected, extended; ALL PASS, exit-gated,
~4 s). Lineage: P-doc (research/work/P-c6pp-twisted.md) sec 3 fork (N)
and sec 5 branches; doc 26 front 1; W-doc sec 9 ("doubly consequential").
Citation-grade input: Lee arXiv:2206.02411v3 (refs/), statements
re-verified against the PDF this session: Def 3.1.1, Prop 3.1.3, Lem
3.1.5, Prop 2.2.2, Def 3.2.4, Lem 3.2.8(d), Prop 4.1.1, COR 4.1.2 (the
s <= 2 concentration - the predecessor miscited it as Prop 4.1.1), Prop
4.1.5, Cor 4.1.6. Setup as in P-doc: p odd, everything p-complete,
alpha = 1 + u p^c wild, canonical instance alpha = 1+p; X(alpha) =
THH(ku_p; ku_{(1,psi^alpha)}).

## 1. Verdict

THE FORK (N) AT FILTRATION 0 IS SETTLED: BRANCH (i). The weight-diagonal
(1 - alpha^w) does NOT act per weight-line in the filtration-0
differential, in every normalization that exists:

- pi_*-ring/bar normalization: ideal collapse is a THEOREM (sec 3) -
  exact integer homology of the honest twisted bar complex, all HH
  degrees, uniform Z/p^c, no rank part.
- descent-side (Lee's vessel): NO counital twisted-comodule realization
  of the twisted descent E_1 exists at all (Theorem T.1, sec 4) - in
  particular none in which (1-alpha) could sit at filtration 0, weight 1.
- skeletal/cyclic-bar filtration (NEW, unconditional - does not consume
  blocker (A)): |E^2_{0,2w}| <= p^c, so the LTE bump p^{c+v_p(w)} is
  IMPOSSIBLE at skeletal filtration 0 (Theorem T.3, sec 5).

THE ABUTMENT FORK STAYS OPEN, now localized exactly: pi_{2p} X(1+p) is
undecidable below two named ambiguities (sec 6) - (L) the connective
lattice ku_{2p}(ku)_p (which divided/binomial classes exist), and (S) the
relative p-adic unit of the twisted differential at Lee's mu/lambda_1
tower locus. Degree 2p sits AT the first ambiguity, not below it; even
degrees <= 2p-2 are below it and agree across all candidate laws
(Z/p^c). If branch (ii)'s tower reaches the abutment it enters at
filtration >= 1 or as an extension - the local Euler supply
(-zeta_p'/zeta_p)(s) and the s = 0 pole have NO filtration-0 home.

## 2. The inherited witness: validation report

The predecessor left a well-formed witness referencing an unwritten
T-doc and a "counital no-go theorem T.1". Disposition:

- T1 (twisted bar complex): VALIDATED INDEPENDENTLY. Re-derived the
  differential convention (left action twisted, x.m = phi(x)m, last face
  carries alpha^{a_n}; weight-w rank of C_n = binom(w,n)); re-derived the
  expected homology by the Koszul model (R^e = Z_p[beta_1,beta_2], R =
  R^e/(beta_1 - beta_2) regular, so HH = [R -(alpha-1)beta-> R]: HH_0
  uniform Z/p^c, HH_{>=1} = 0) - matches the bar-level SNF output, which
  is the stronger statement (no Koszul shortcut in the gated path).
  ADDED: a pure-python Smith-reduction cross-check of every flint SNF
  (module invariants: rank, volume, p-primary type) and the binom(w,n)
  rank gate. Untwisted HKR control already present, passes.
- T2 (LTE weight-line), T4 (g_alpha coordinates), T5 (s = 0 trichotomy):
  re-derived by hand (binomial valuations; the Dirichlet closed forms
  including residue -1/2 and finite part zeta'(0) + (1/4 - c/2) log p).
  Correct as inherited. T4's three-way table conflated the two
  truncation candidates (MU-relative dies at w = p-1, numerical at
  w = p); FIXED - under the numerical candidate (the one the
  unconditional T6 row probes), pi_{2(p-1)} is fork-blind and the
  trichotomy opens at 2p.
- T3 ("counital no-go"): the intended theorem WAS reconstructible and is
  SOUND after two repairs (sec 4): the citation fix (s <= 2 is Lee Cor
  4.1.2; also added the cleaner unconditional vanishing line t >= 4s),
  and the honest bridge for input (ii) - the bar complex's rational row
  does not by itself compute sphere-level pi_2 X (x) Q; Lemma T.2
  supplies the missing comparison. The witness model of the degree-2
  line was verified against Lee's actual definitions (A = THH(ku/MU)
  free over ku_* on sigma^2 x_{i>=2}-monomials by Prop 2.2.2; Gamma =
  THH(MU/MU (x) MU) an MU_*-Hopf ALGEBRA - eta_L = eta_R, so no
  algebroid ambiguity - free on sigma^2 b_i, |sigma^2 b_i| = 2i+2;
  x_1 |-> beta, x_{i>=2} |-> 0 per Def 3.2.4).
- ADDED T6 (sec 5-6): the unconditional skeletal s = 0 row, the lattice
  trichotomy, Theorem T.3, and the mu-locus rigidity gates.

## 3. (N) at filtration 0, exactly - and the precise scope

THEOREM (bar level; witness T1). For R = Z_p[beta], phi(beta) =
alpha beta wild, the normalized two-sided bar complex of (R, R_phi) has,
per weight w >= 1: H_0 = Z/p^c uniform (the relation module is the IDEAL
((1-alpha)beta), generated in weight 1), H_n = 0 for all n >= 1 -
including the cotangent line (rational Betti numbers all vanish, w >= 1).
Untwisted control reproduces HKR (Z_p + Z_p per weight).

WHAT THIS DECIDES: the filtration-0/pi_*-ring layer of any filtration of
X(alpha) whose associated graded begins with the homotopy-ring bar
construction (the colimit normalization). The weight-graded
"pre-relation" normalization [Z_p -(1-alpha^w)-> Z_p] per weight line
(= T2, the LTE tower) is NOT the homology of this layer; multiplicative
structure eats the tower - exactly P-doc's ideal collapse, now at full
bar depth instead of the Koszul shadow.

WHAT IT DOES NOT DECIDE (P-doc sec 3 (N), honest-limits item 3): the
descent E_2 rows at s >= 1 and the abutment. The shadow is relative to
Z_p; ku is not an HZ_p-algebra; everything Lee's sphere-level tower
carries (the lambda_2 F-lattice, the T-torsion, the mu/lambda_1 towers)
is invisible here and can change abutment cardinalities by extensions.
Filtration-0 exactness therefore settles the fork AS POSED ("does
(1-alpha^wt) enter the filtration-0 differential line by line?") - NO -
but does not by itself compute any pi_{2w} X.

## 4. Theorem T.1 (counital no-go), reconstructed and proved

Statement. There is no counital Gamma_*-comodule structure psi on
(transported) A_* whose cobar complex CB_{Gamma_*}((A_*)_psi) is the
twisted descent E_1 (the levelwise identification P-doc sec 3 input (A)
would provide). Equivalently: the (A)-vessel, as posed, is dead for
every wild alpha; the twist must deform the levelwise identification
itself, not just the coaction.

Proof. (1) (A (x)_{MU_*} Gamma)_2 = Z_p{beta (x) 1} (witness T3 gate;
Gammabar and Abar start in degrees 4 and 6). Counitality pins
psi(beta) = beta (x) 1, so D^0(beta) = 0 and E_2^{0,2} = Z_p beta.
(2) The normalized cobar of any connective comodule satisfies
Ext^{s,t} = 0 for t < 4s (Gammabar = ker(counit) is concentrated in
internal degrees >= 4: the counit is an iso on the MU_*-line and
sigma^2 b_i has degree 2i+2 >= 4). Every d_r out of (0,2) targets
(r, r+1) with r+1 < 4r: dead; every E_infty^{s,s+2} with s >= 1 has
s+2 < 4s: dead. (Independently: parity + the s <= 2 concentration, Lee
Cor 4.1.2.) (3) The twisted descent tower converges strongly (Lee Lem
3.1.5 verbatim: THH(MU) -> MU is 2-connective - THH(MU) =
MU (x) Lambda(sigma b_i), |sigma b_i| >= 3 - and the module is
connective). Hence pi_2 X(alpha) = E_infty^{0,2} = Z_p. (4) But
pi_2 X(alpha) (x) Q = 0 by Lemma T.2. Contradiction. QED.

LEMMA T.2 (the rational bridge - the predecessor's missing step). The
skeletal (cyclic-bar) filtration of X(alpha) is unconditional; its E^1
has E^1_{s,t} = pi_t(ku_p (x) (ku/S)^{(x) s})-normalized with faces =
multiplications and one psi^alpha-rotated face. Rationally
pi_*(ku_p (x) ku^{(x) s}) (x) Q = Q_p[beta_0, ..., beta_s] (ONE
p-complete factor; ku finite type; so Q_p (x)_Q Q[beta]^{(x) s} - no
Omega_{Q_p/Q} interference, which is exactly what would poison a naive
rationalization of a p-complete THH), and the twisted face acts by
beta_s |-> alpha beta_s with alpha = 1+p INTEGRAL, so the whole
rationalized E^1 is the T1 bar complex (x) Q. Its homology is Q_p in
degree 0, weight 0, and nothing else (T1 rational row, gated). Strong
convergence + degreewise-f.g. stages let the rationalization pass to the
abutment: pi_0 X (x) Q = Q_p, pi_n X (x) Q = 0 for n >= 1. QED.

(T.2 is itself fork-relevant beyond T.1: the RATIONAL abutment is fully
decided - P-doc P2's "rationally Q_p in degree 0" is now a proof, not an
assertion.)

Scope of T.1. It kills one vessel - cobar-of-counital-comodule on
transported A_* - not the descent tower itself (which exists and
converges) and not branch (ii) at the abutment. Its fork content:
filtration 0 of any comodule-cobar descent CANNOT carry the weight
diagonal at w = 1 (counitality forces D^0(beta) = 0 before any
contradiction is even invoked), and no such realization exists anyway.
Practical consequence for blocker (A): even if structured Adams
operations on MU_p are found, the levelwise identification cannot be
"transport A_* and twist the coaction" - the KMN-style rebuild (P-doc
O3) is forced, not optional.

## 5. The unconditional skeletal route (NEW): the s = 0 row is a lattice
   question and branch (ii) is excluded there

The cyclic bar construction of X(alpha) needs only the GHM E_infinity
psi^alpha on ku_p - NOT blocker (A). Its skeletal SS converges strongly
(connective, exhaustive). The s = 0 row is computable in closed form:
for a class xi in pi_{2w}(ku_p (x) ku) with rational coordinate function
f (xi = sum c_b beta_0^{w-b} beta_1^b, f(t) = sum c_b t^b),

    d^1(xi) = (f(1) - f(alpha)) beta^w,

because d_0 = multiplication (f(1)) and d_1 = multiplication after
psi^alpha on the right factor (f(alpha)). So

    E^2_{0,2w} = Z_p beta^w / { f(1) - f(alpha) : f in L_w },

L_w = the CONNECTIVE LATTICE of pi_{2w}(ku_p (x) (ku/S)) coordinate
functions. Witness T6a gates the trichotomy of candidate lattices:

```text
lattice L_w                      image ideal at weight w     law
monomials only (no mixing)       (alpha^w - 1)               LTE p^{c+v_p(w)}  [= branch (ii)]
Z_p[beta_0, beta_1] (small)      (alpha - 1)                 UNIFORM p^c       [= branch (i)]
+ binomial/numerical classes     staircase                   p^{max(c - floor(log_p w), 0)}
  (KU_0 KU-style)                                            (c = 1: DEATH at w >= p)
```

THEOREM T.3 (s = 0 exclusion; witness T6b). The true L_w contains the
monomial classes (Kunneth images of beta_0^{w-b} (x) beta_1^b), so the
image ideal contains (alpha - 1) and |E^2_{0,2w}| <= p^c. At p | w this
is strictly smaller than branch (ii)'s p^{c+v_p(w)}: THE LTE BUMP CANNOT
LIVE AT SKELETAL FILTRATION 0. Combined with secs 3-4: no filtration-0
home for the local Euler supply, in any of the three normalizations.

Low-degree abutment payoff (flagged, not gated): torsion from sphere
cells first enters the skeletal E^1 at internal degree 2p-2 (the alpha_1
cell, pi_{2p-3} S), affecting total degrees >= 2p-1 only. Under two
flags - (f1) pi_*(ku^{(x) s})_p even and torsion-free in internal
degrees <= 2p-2, (f2) the torsion-free lattice embeds in the KU-numerical
one (so the image valuation is >= c for w <= p-1, T6a staircase) - the
first p-1 weights are decided at the ABUTMENT:

    pi_{2w} X(1+p) = Z/p   (1 <= w <= p-1),   pi_odd = 0 below 2p-3.

This is P1's uniform half-ladder, now in honest degrees, conditional
only on standard connective K-theory bookkeeping (flags f1-f2), not on
(A) or (N).

## 6. pi_{2p} X(1+p): the first ambiguity, located exactly

Two independent unknowns meet at total degree 2p, and the witness gates
the arithmetic of both:

(L) THE LATTICE (filtration 0): is the k = p binomial/divided class
    (coordinate binom(t,p)-type; equivalently Adams' t_1-divided class)
    present in the connective ku_{2p}(ku)_p? If YES: f(1) - f(alpha) =
    -binom(1+p, p) = -(1+p), a UNIT - weight p DIES at filtration 0
    (truncated law; D(s) entire, no zeta factor). If NO (lattice stays
    small at 2p): Z/p^c survives (branch (i) law). This is a
    LITERATURE-DECIDABLE question about ku (x) ku (Adams-Clarke K_*K
    numerical forms; Kane / Lellmann for the connective Adams summand;
    Angeltveit-Hill-Lawson THH(l)) - next step 1.

(S) THE TWISTED DIFFERENTIAL UNIT (filtration >= 1): at Lee's tower
    locus the untwisted coefficient is exactly kp (Lem 3.2.8(d) + Prop
    4.1.5); the twist adds the eigenvalue term (1 - alpha^{(p-1)k}) with
    an unknown relative p-adic unit theta (O3: the honest twisted
    cosimplicial/cyclic structure was never built). Gated arithmetic
    (T6c-e): for alpha = 1+p the two terms have EQUAL valuation
    1 + v_p(k) and equal-up-to-sign unit parts - one sign cancels
    (>= 2 + v_p(k)), the other is exact - so BOTH Z/p and Z/p^2 outcomes
    for pi_{2p} are realizable depending on theta. NEW RIGIDITY: the
    ambiguity is SPECIFIC to u = +-1 mod p (T6d: for alpha = 1 + up,
    u != +-1, neither sign cancels) and to c = 1 (T6e: for c >= 2 the
    eigenvalue term is subleading and the law v = 1 + v_p(k) is forced
    for ANY theta).

FAIL-CLOSED VERDICT: pi_{2p} X(1+p) is UNDECIDABLE below ambiguities
(L) and (S); the three-way table (i) Z/p / (ii) Z/p^2 / truncated 0 is
fully alive at 2p, and 2p is the FIRST such degree. PRE-REGISTERED
DODGE (new, from T6d/T6e): compute pi_{2p} X(1+3p) (or any u != +-1) -
there the (S)-ambiguity is rigid and only (L) remains; similarly
X(1+p^2) kills (S) by subleading valuation. A computation that resolves
(L) plus one rigid instance pins theta for the canonical alpha = 1+p by
the family transport law (P-doc 2a).

## 7. The s = 0 pole test (P's decider (b)), status

The trichotomy is witnessed at certificate grade (T5, arb prec 350):
branch (i) regular with value -(c/2) log p; branch (ii) simple pole,
residue -1/2, finite part zeta'(0) + (1/4 - c/2) log p; truncated
ENTIRE with no zeta factor at all. What this session adds: the pole, if
it appears, is now PROVABLY a filtration->=1/extension phenomenon
(Theorem T.3) - "the local Euler supply enters the twisted family as a
factor" (doc 26 front 1) can only mean: through the sphere-cell towers,
never through the ring-level layer. The experimental discriminator is
unchanged and waits on (L)/(S).

## 8. G-INT6 ledger

Free choices: p (grid {3,5,7,11}), alpha-instances (canonical 1+p;
rigidity grids u in {3,4}, c in {2,3} - chosen to span the regimes, not
tuned); the three candidate lattices (pre-registered as the three
filtration-0 laws already in play, not invented post hoc); W1MAX = 9,
cross-check w <= 5 (cost-bounded). Matched constraints with zero
remaining parameters: the bar homology grid (exact SNF, two independent
implementations); the Koszul re-derivation; the rank law binom(w,n);
d o d = 0; the lattice trichotomy laws on the full grid (incl. the
c >= 2 staircase, a new exact law); the sign-cancellation regimes
(three, exact); the T5 closed forms re-derived analytically. Fitted
objects: NONE. The fork outcome at the abutment is recorded as
ignorance with named blockers, not resolved by preference; the decided
part (filtration 0) is three theorems, not a reading.

## 9. Carrier guard

Every object consumes the E_infinity ring map psi^alpha: the twisted
bimodule, the g_alpha FGL cocycle, the eigenvalue action alpha^w, the
skeletal d^1 = f(1) - f(alpha), the lattice question itself (it is a
question about ku (x) ku as a psi^alpha-module). DH/Epstein: no ring, no
bimodule, no cocycle, no lattice - dead at the object. Necessary filter,
not sufficient.

## 10. Honest limits

1. Theorems T.1/T.2 are paper-level derivations whose ARITHMETIC
   ingredients are gated; the spectral-sequence formalism (skeletal SS
   identification, strong convergence transfer, rationalization of a
   strongly convergent f.g. SS) is standard but not machine-checked.
2. Lemma T.2 needs pi_*(ku^{(x) s+1}) (x) Q = Q_p[beta_0..beta_s]:
   standard (rational evenness of ku smash powers), asserted from
   finite-type + Kunneth, not re-proved.
3. The sec 5 low-degree abutment values carry flags f1-f2 (evenness/
   torsion-freeness of ku (x) ku homotopy below 2p-2, and the embedding
   into the numerical lattice). Plausible, literature-checkable,
   unverified here.
4. The (S)-ambiguity description assumes P-doc 5.1's identification of
   the two competing terms at the mu-locus (Lee's kp + eigenvalue);
   the unknown theta is exactly O3's unbuilt twisted cyclic structure.
   Nothing is claimed about which theta is realized.
5. T6's "numerical lattice" is a CANDIDATE for ku_{2*}ku_p (upper
   lattice KU-side); the true connective lattice is open input (L).
6. Inherited from P-doc: Lee transcription risks (its sec 8.4);
   tau o psi^alpha coherence (its 2b caveat) - neither is load-bearing
   here.

## 11. Next steps (ranked)

1. RESOLVE (L) [literature, sharply posed]: the additive structure of
   ku_{2p}(ku)_p / l_{2p}(l)_p - is the binom(t,p)-class connective?
   (Adams-Clarke K_*K; Kane bo/bu-resolutions; Lellmann connective
   co-operations; Angeltveit-Hill-Lawson.) EITHER answer collapses the
   three-way table to two and decides the filtration-0 fate of weight p.
2. RUN THE DODGE: pi_{2p} X(1+3p) via the skeletal route (only (L)
   bites there, T6d); then transport (P-doc 2a) constrains theta for
   the canonical instance.
3. Settle flags f1-f2 (low-degree ku (x) ku bookkeeping) to promote the
   sec 5 abutment values pi_{2w} X = Z/p (w <= p-1) to theorem grade -
   the first unconditional twisted homotopy groups of the program.
4. The KMN rebuild (P-doc O3) remains the structural answer to (S);
   T.1 now proves it is unavoidable (no comodule shortcut exists).
5. Feed the decided filtration-0 law into W-doc sec 9's "doubly
   consequential" consumer: the per-weight Lorentzian scaling cannot be
   sourced at filtration 0 - if the geometric family's index shape needs
   the LTE tower, it needs the sphere-cell towers, i.e. the same (L)/(S)
   gate. One gate, two consumers.
