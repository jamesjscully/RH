# W - The monoid-level Frobenius family: the pairing homes mapped, the F_p Euler factor transcribed as a Frobenius-graph pairing, the bidegree number obtained, and the Castelnuovo index shape CERTIFIED on the geometric family

Status: doc-26 front 4 executed 2026-06-10. Witness:
prime_monoid_frobenius_shadow.py (ALL PASS, exit-code gated, 0.5 s;
readings P1-P4 and R-a/b/c pre-registered in the docstring; the
signature explorations that preceded gate registration are disclosed in
sec 7). New refs archived: mccandless2021-curves-ktheory-tr.pdf/.txt
(arXiv:2102.08281v4), morava2024-delta-rings-prisms-homotopy.pdf/.txt
(arXiv:2401.12336). Primary transcription sources: Hesselholt
1602.01980 (refs/hesselholt2016.txt, read verbatim), Nikolaus-Scholze
arXiv:1707.01799, Quillen (Ann. of Math. 96 (1972) 552-586).

Honest headline: NO new spectrum-level object is constructed here. The
deliverables are (1) the precise map of where a "graph of Frobenius"
pairing can and cannot live, with two named blockers sharpened to
no-go's where provable; (2) the complete pi_*-shadow algebra of the
non-invertible family, witnessed exactly; (3) the bidegree number doc
23's corrected Castelnuovo form needs; (4) a small exact theorem (the
max-Gram lemma) + a certified-perturbation gate showing the monoid
family DOES carry the Lorentzian (1, n) index shape that worker P
proved the invertible family cannot.

## 0. Result summary

```text
carrier 1 (cyclotomic phi_p)   EXISTS canonically; graph pairing lives in
                               CycSp, NOT in bimodules; the Lefschetz
                               object is TC, the Witt object is TR, the
                               determinant object is TP (x)_{W,iota} C;
                               at p it is provably BLIND to the degree
                               growth (v_p(q^w - 1) = 0) -- Hesselholt's
                               iota: W -> C is the step that repairs it.
carrier 2 (non-invertible      PERIODIC no-go (proved, one line): no
  psi^p on K-theory)           multiplicative psi^p on KU or KU_p, ever.
                               Connective E_1 psi^p: ku -> ku UNLOCATED
                               (blocker A''). What exists at p: McClure/
                               Hopkins theta (Frobenius lift on pi_0 of
                               K(1)-local E_infinity rings = delta-ring
                               structure), and Quillen's fixed-point
                               object K(F_q) = fib(psi^q - 1).
the shadow                     branch (i) collapses TAME (Z/(k-l)); the
                               fixed-point object grows UNCONDITIONALLY:
                               |pi_{2w-1}| = q^w - 1 = 1/|zeta(F_q,-w)|.
bidegree number                d_2 = p: phi(v) = p v (Hesselholt Prop
                               4.2) = psi^p on the Bott line; per weight
                               w: p^w; bidegree = NORM of the Bott
                               eigenvalue (p-adic norm 1 = P's (1,1);
                               archimedean norm p = the FF (1, q)).
Castelnuovo                    the geometric family {psi^{p^i}} log-Gram
                               = (w log p) max(i,j) + E; max-Grams are
                               ALWAYS Lorentzian (1, n) (exact lemma);
                               certified for w >= 3,2,2,1 at p = 2,3,5,
                               >=7; t-window n-STABLE containing 0
                               (doc 23's escape repaired). Low weights
                               at p = 2, 3 fail: the prime-2 anomaly.
```

## 1. Carrier 1: the cyclotomic Frobenius and its three pairing homes

### 1.1 Why there is no bimodule graph (precise undefinability)

phi_p: THH(R) -> THH(R)^{tC_p} is a map of spectra with S^1-action
(S^1 = S^1/C_p on the target), E_infinity over the Tate diagonal of the
sphere (NS III.1-III.3). It is NOT of the form THH(R; M) -> THH(R) for
any R-bimodule M, and no bimodule Gamma_{phi_p} exists with
<Gamma_{phi_p}, Delta> = THH(R; Gamma_{phi_p}): a bimodule presentation
would require an R (x)_S R-linear self-map of R, i.e. a ring self-map
of R itself; phi_p is instead linear only over the TATE-VALUED
Frobenius S -> S^{tC_p} of the base. The twist sits in the sphere, not
in the coefficients - this is the structural reason P's blocker (A)
exists at all. Fail-closed: at the bimodule level "the graph of the
cyclotomic Frobenius" is undefinable, full stop.

### 1.2 The homes that DO exist (transcription, citation-grade)

The cyclotomic structure relocates the graph formalism one categorical
level up. THH(R) - which IS the self-pairing <Delta, Delta> of the
square - becomes an object of CycSp carrying phi, and:

  (H1) Lefschetz fixed-point OBJECT:
       TC(R) = map_CycSp(1, THH(R)),  1 = THH(S) = the cyclotomic
       sphere (trivial S^1-action, phi = the Tate-diagonal unit)
       (Nikolaus-Scholze, for
       bounded-below; conjectured by Kaledin, proved p-complete by
       Blumberg-Mandell; McCandless Rem 1.2.2 for this formulation).
       "Hom(triv, THH)" from the task prompt is exactly this.
  (H2) Witt/curves level: TR(X) = map_CycSp(~THH(S[t]), X), valued in
       SPECTRA WITH FROBENIUS LIFTS (McCandless Thm B, archived;
       refines Blumberg-Mandell; Krause-Nikolaus p-typically). TR is
       corepresented by the reduced THH of the flat affine line - the
       graph calculus against the AFFINE-LINE Frobenius, with TR_0(A;p)
       = W(A) (Hesselholt-Madsen Thm F; hesselholt2016.txt l.390-394).
       Witt vectors = the universal Frobenius-lift data; the
       F-fixed-points are the Lefschetz data (sec 1.4).
  (H3) determinant level (the EQUATION home): TC = fib(can - phi:
       TC^- -> TP). TC^- is the correspondence space carrying both the
       degeneration to the diagonal (can) and the Frobenius graph
       (phi); TP is the ambient; TC is the intersection object. The
       NUMBER extraction is Hesselholt's Theorem A.

### 1.3 The F_p shadow: the local Euler factor AS a Frobenius-graph pairing

Transcribed from Hesselholt 1602.01980 (verbatim source in refs):

  - TP_*(F_q) = W(F_q)[v^{+-1}], v in TP_{-2}, with a canonical
    W(F_q) = TP_0 (his Sec 4); the meromorphic cyclotomic Frobenius
    satisfies phi(v) = p v (Prop 4.2) - THE non-invertible eigenvalue.
  - On the weight-w line of TP (x)_{W,iota} C the geometric Frobenius
    acts as Fr*_q = q^w phi^r (his p.21, last formula). On TP(F_q)
    itself: q^w (q^{-w}) = 1 (witness W4b, exact), so
    Theta = log_q(Fr*) has eigenvalue ladder (2 pi i / log q) Z, one
    line per v-power: doc 20's FULL LADDER, now derived from
    phi(v) = pv + the weight grading + iota, not assumed.
  - Theorem A: zeta(X, s) = det_inf(s id - Theta | TP_od (x)_{W,iota} C)
    / det_inf(... | TP_ev ...) for X smooth proper over F_q. For
    X = Spec F_q: TP_od = 0 and det_inf over the full ladder =
    1 - q^{-s} (Deninger's identity, Rem 7.2) - the PREFACTOR-FREE
    scheme, exactly as doc 20 correction C1 recorded. So
    zeta(F_q, s) = 1/(1 - q^{-s}) is literally the regularized
    characteristic function of log(Frobenius) acting on the Tate
    construction of the self-pairing <Delta, Delta>.

The integer-points shadow of the same statement (witness W2a, exact):
the weight-w fixed-point cardinality q^w - 1 equals 1/|zeta(F_q, -w)|.
The Euler factor evaluated at negative integers IS the shadow tower.

### 1.4 The Witt/Lefschetz dictionary and the TR/TC tables

  - TR^n_*(F_p; p) = W_n(F_p)[alpha_n] with F(alpha_n) = alpha_{n-1},
    R(alpha_n) = p alpha_{n-1} (Thm 3.1 + Rem 4.3). Hence
    TR_*(F_p; p) = lim_R = W(F_p) = Z_p concentrated in degree 0 (the
    p^i-twisted transition pro-systems vanish; Mittag-Leffler), while
    TF_*(F_p; p) = Z_p[alpha]. "TR(F_p) = W(F_p) = Z_p" - the Witt
    vectors are the degree-0 Lefschetz data, exactly the task's gloss.
  - TC(F_p) = Z_p (+) Sigma^{-1} Z_p: on weight w >= 1 lines (can-phi)
    acts by p^w - 1 (up to unit), a p-adic UNIT (witness W4a); weight 0
    gives ker = coker = Z_p in degrees 0, -1 (NS IV.4). pi_0 TC(F_p) =
    W(F_p)^{F=1} = Z_p = the H^0 of the Frobenius flow; pi_{-1} = the
    coinvariants = H^1: the pole structure of 1/(1 - p^{-s}) at s = 0.
  - W(Z)^{F=1} = Z: F-fixed p-typical Witt vectors of Z are exactly the
    ghost-constant ones, which lift integrally (Dwork; witness W5,
    exact ghost arithmetic over Q). The fixed locus of Frobenius on the
    arithmetic-plane coordinate ring's Witt lift is the DIAGONAL Z.
  - TC(Z; p) low degrees (Bokstedt-Madsen, Asterisque 226 (1994), p
    odd; Rognes, J. Pure Appl. Algebra 134 (1999) at p = 2; assembled
    via K(Z_p; Z_p) = TC(Z; Z_p) in degrees >= 0, Hesselholt-Madsen +
    DGM): pi_{-1} = Z_p, pi_0 = Z_p, pi_1 = Z_p (p odd; extra Z/2 at
    p = 2). NOT re-derived; recorded for the global ledger and not
    load-bearing below. The odd-degree towers of TC(Z;p) hold the
    p-parts of K_{2w-1}(Z) - zeta-value cardinalities - the global
    shadow of the same mechanism (flag only).

### 1.5 The p-adic blindness, and what Hesselholt's iota really does

v_p(q^w - 1) = 0 for every w >= 1 (witness W3b/W4a): the p-COMPLETE
cyclotomic pairing at p sees only the weight-0 line. ALL of the degree
growth of det(1 - Fr) lives at the OTHER primes (sec 3) and at the
archimedean place. Hesselholt's Theorem A nevertheless extracts the
full Euler factor from p-complete data because of the embedding
iota: W(F_q) -> C - the coefficients of TP are a p-adic ring that
HAPPENS to embed in C, and the regularized determinant is taken of the
iota-image. The re-archimedeanization is a separate, load-bearing move.

### 1.6 The Spec Z / square analogue, posed and blocked

Wanted: zeta(s) ~ det_inf(s id - Theta | "TP_od(HZ (x)_S HZ)") /
det_inf(... ev). Blockers, sharpened from the BMS triple (doc 20
superseded note, J-doc sec 2):

  (B1) TP technology is p-complete throughout; the square's rational/
       archimedean data (sqrt(2pi), doc 18) is invisible to it.
  (B2) phi on TP of p-adic rings is semilinear over the prism. The F_q
       case evades this ONLY because the coefficient ring W(F_q) has
       phi^r W-LINEAR (r-th power of Frobenius is linear over the fixed
       field of a FINITE field) and W^{phi=1} = Z_p. Over Z there is no
       finite r: no linearization, no eigenvalue ladder, no Theta.
  (B3) no iota: W(F_q) -> C exists because W(F_q) is a finite unramified
       extension of Z_p; the square's TP coefficients (Nygaard-complete
       prisms) admit no complex embedding. Sec 1.5 says iota is exactly
       the archimedean step - so B3 is not a technicality, it is the
       program's properness/Poisson wall (doc 19 sec 5) in coordinates.

Fail-closed deliverable: carrier 1 supplies the LOCAL pairing at every
p, canonically and non-invertibly; what it cannot supply, provably in
the present technology, is the global/archimedean assembly - the same
single wall, now with the F_q-proof's load-bearing finiteness inputs
(linearity of phi^r, existence of iota) named precisely.

## 2. Carrier 2: non-invertible psi^p - existence audit

### 2.1 The periodic no-go (proved)

Any E_1-ring map f: KU -> KU (or KU_p -> KU_p) sends the unit
beta in pi_2 to a unit. psi^p requires f(beta) = p beta, a non-unit.
Hence NO multiplicative psi^p exists on ANY periodic model - integral,
p-local, or p-complete. (One line, but it upgrades P's "(A): unlocated"
to "impossible" on the periodic side; GHM's E_infinity moduli Z_p^x for
KU_p was already only units, and the stable-operation algebra
K^0(KU_p) = Cont(Z_p^x, Z_p) (Adams-Harris-Switzer/Madsen-Snaith-
Tornehave line) has no evaluation at p either - the no-go is consistent
with everything located.) Geometric reading: Spec KU = G_m carries only
the automorphism GROUP Z_p^x; the monoid endomorphisms (x -> x^p,
graphs with degree) live on Spec ku = A^1: the monoid forces the
CONNECTIVE/integral model, and the doc-19 properness step must
compactify A^1 -> P^1, not G_m.

### 2.2 What exists at p (literature, archived)

  (a) Unstable psi^p on K^0(X) (lambda-ring structure): classical.
  (b) McClure's operation in p-adic K-theory (Bull. AMS 8 (1983) 67-72;
      BMMS H_infinity book): on pi_0 of any K(1)-local E_infinity ring
      there are theta and psi with psi(x) = x^p + p theta(x), psi a
      ring map and a FROBENIUS LIFT - the theta-algebra/delta-ring
      structure (Hopkins, "K(1)-local E_infinity ring spectra" notes).
      For KU_p this psi IS psi^p - as an operation on homotopy, never
      as a spectrum self-map. Morava's notes (arXiv:2401.12336,
      archived) read exactly this as a prismatic/delta-structure - the
      "spherical delta-ring" direction is the current research home of
      blocker (A'').
  (c) The Tate-valued Frobenius R -> R^{tC_p} of any E_infinity ring
      (NS III.1): always exists; its THH-avatar is carrier 1. The
      trace-methods world supplies psi^p exactly in cyclotomic/
      delta-ring form - never as a twisted bimodule.

### 2.3 The named blocker and the workaround that already exists

(A'') An E_1-ring map psi^p: ku -> ku with pi_{2w} = p^w (equivalently
a delta/Frobenius-lift structure on ku lifting (b)): NOT located;
required for the twisted bimodule ku_{(1, psi^p)} and hence for the
honest twisted THH pairing. Fail-closed: the monoid-level TWISTED
BIMODULE is undefinable at current literature level, integrally
(no map located) and p-completely (sec 2.1 kills every periodic
route; no connective construction known).

The workaround (already a theorem): Quillen's fixed-point object.
K(F_q) = BGL(F_q)^+ x Z = F psi^q = fib(psi^q - 1) (space level,
integral, Quillen 1972); spectrum level ell-adically for every prime
ell not dividing q, where psi^q is the STRUCTURED member q in Z_ell^x
of P's invertible family at ell. Homotopy: pi_{2w-1} = Z/(q^w - 1) =
K_{2w-1}(F_q), pi_{2w} = 0 (w >= 1). The fixed-point object needs no
bimodule and no fork: its weight-w cardinality is q^w - 1
unconditionally. This is the monoid-level carrier that EXISTS.

## 3. The shadow computation and where the growth actually is

pi_*-shadow over Z (the bar-complex algebra, elementary, as P did):
R = Z[beta], psi^k(beta) = k beta, bimodule R_(psi^k, psi^l):

  - branch (i) (ideal collapse, ungraded HH_0 = R/({(k^j - l^j)
    beta^j})): weight-w piece Z/gcd_{j<=w}(k^j - l^j) = Z/(k - l)
    (witness W1, exact): UNIFORM - and for (k,l) = (p,1) it is the TAME
    Z/(p-1). The pre-registered "towers now grow" is REFUTED in branch
    (i): the ideal collapse eats the growth exactly as it ate P's LTE
    tower. Honest: the fork (N) relocates, it does not disappear.
  - branch (ii) (weight-diagonal) and - unconditionally - the
    FIXED-POINT object: weight-w cardinality |k^w - l^w|; for (q, 1):
    q^w - 1 = |K_{2w-1}(F_q)| = 1/|zeta(F_q, -w)| (witness W2a), with
    the degree recursion q^{w+1} - 1 = q(q^w - 1) + (q - 1) (W2b) and
    LINEAR log-growth ~ w log q (W2c). The pre-registration P1 is
    CONFIRMED on this carrier: degree growth = what Castelnuovo needs
    and the invertible family provably lacked.

Adelic structure of the growth (witness W3, exact): for every prime
ell, v_ell(q^w - 1) = [d_ell | w] (v_ell(q^{d_ell} - 1) + v_ell(w))
(odd ell, d_ell = ord_ell(q); 2-adic variant at ell = 2; ZERO at
ell | q). Each factor is precisely P's invertible-family tower at ell:
tame periodic excess (period d_ell, his W5) + wild LTE tower
(v_ell(w), his W1). The monoid-level Lefschetz number is the EULER
PRODUCT of the group-level towers over all other primes - the
multiplicative monoid of integers as the irreducible carrier, now as an
exact identity (and q^w - 1 = prod_{d | w} Phi_d(q), W3c: the graded
pieces are indexed by the divisor monoid). The p-part is EMPTY: the
p-complete pairing at p is blind to its own degree growth (W3b) -
consistency between P's theorem and the growth being real.

## 4. The bidegree ledger (doc 23's number)

  - d_1 = 1 always (graphs of maps).
  - d_2(psi^k) on the Bott/ruling line = k; per weight w: k^w. For the
    cyclotomic Frobenius: phi(v) = p v (Hesselholt Prop 4.2):
    d_2(phi_p) = p. THE single number doc 23's corrected Castelnuovo
    form needs: the FF Frobenius graph bidegree (1, q) is realized at
    the monoid level as (1, p), and per weight as (1, p^w).
  - Norm-dependence resolves the doc-23/P tension: bidegree = the NORM
    of the Bott eigenvalue. p-adic norm of k in Z_p^x is 1: P's (1,1)
    verdict for the invertible family. Archimedean norm of the
    non-invertible k is k: doc 23 sec 3's "(1, k)" guess - both were
    right in their own norm; the product formula ties them.
  - The pi_0/truncation fiber classes pair psi-INDEPENDENTLY (psi = id
    on pi_0; P's 2b): bidegree is NOT visible on pi_0-fibers; it is
    read on the weight lines (the graded rulings).
  - Degree zeta (witness W9): sum_w d_2|_w q^{-ws} = q^{1-s}/(1-q^{1-s})
    - the local factor of zeta(s - 1), the H^2/pole factor of the FF
    surface dictionary: the rank-part hook doc 19 reserved.

## 5. The Castelnuovo signature: a lemma, a certificate, and the repair of doc 23

### 5.1 The max-Gram lemma (exact; witness W6)

Let a_0 < a_1 < ... < a_n be real, a_n > 0, and M[i,j] = max(a_i, a_j).
Then M = u 1^T + 1 u^T - MIN (u = (a_i), MIN[i,j] = min(a_i,a_j));
the rank-2 part has signature (1,1) and MIN is PSD (PD on positive
a_i: det MIN = a_0 prod(a_{i+1} - a_i), W6c), so n_+(M) <= 1 (Weyl subadditivity);
trace(M) = sum_i a_i > 0 forces n_+ = 1; and det M = (-1)^n a_n
prod(a_{i+1} - a_i) != 0 (W6a) kills the kernel. SIGNATURE (1, n) -
the Castelnuovo/Hodge-index shape is AUTOMATIC for any family whose
log-pairing is max(deg_i, deg_j): the tropical/archimedean law
"size of difference of dominant terms = dominant degree". Dually the
p-adic valuation Gram is MIN - ultrametric, PSD: P's Parisi finding.
One pairing, two faces, split by the product formula (W6d):

    |p^{iw} - p^{jw}| = p^{w min(i,j)} (p^{w|i-j|} - 1):
    v_p-Gram = w MIN (PSD, hierarchical)   [P's universe]
    log-Gram = (w log p) MAX + E           [the index universe]

Corollary (P's refutation rederived): an invertible family has all
log-degrees ZERO (|alpha|_p = 1), the max-Gram vanishes identically -
groups carry no index shape because they carry no degrees. And doc 23's
negative is EXPLAINED: the family {psi^1..psi^n} has log|k - l| which
is NOT a max-Gram (consecutive integers are not degree-separated); the
FF configuration {Delta, Gamma_F, Gamma_F^2, ...} is geometric, and its
arithmetic analogue {psi^{p^0}, ..., psi^{p^n}} is exactly the family
where log|p^i - p^j| = max(i,j) log p + O(p^{-|i-j|}).

### 5.2 The certificate (witness W7) and the measured table (W8)

Per-weight log-Gram of the geometric family, degree diagonal
(M[i,i] = w i log p, the k-dependent diagonal doc 23 sec 3 predicted):
M = (w log p) MAX_n + E, E[i,j] = log(1 - p^{-w|i-j|}), ||E||_2 <=
||E||_inf <= 2x/(1-x)^2 with x = p^{-w} (exact rational bound).
Exact gates: MAX_n has exactly ONE eigenvalue above -1/4 (Descartes on
the integer characteristic polynomial, shifted; n <= 24), so by Weyl
the true Gram has signature (1, n) whenever

    2x/(1-x)^2 < (w log p)/4      (log p >= rational atanh partial sum).

CERTIFIED Lorentzian: all (p, w) with w >= 3, 2, 2, 1 for p = 2, 3, 5,
>= 7 (and everything above). Measured thresholds: w_0(2) = 3,
w_0(3) = 2, w_0(5) = 1. Measured NON-Lorentzian: p = 2 at w <= 2,
p = 3 at w = 1 (signatures ~ (0.55n, 0.45n)): the LOW-WEIGHT anomaly
sits at 2 (and 3) - the doc-26 prime-2 address surfacing again, this
time as the place where the archimedean corrections overwhelm w log p.
Full monoid section {1..9}: Lorentzian (1, 8) by w = 16 (measured,
W8c): ANY degree-separated section becomes Lorentzian at large weight.

t-window (W8d): with the degree diagonal, the window of admissible
diagonal shifts t is n-STABLE and contains t = 0 with margin
>= (w log p)/4 - ||E|| (t_hi = 0.31, 0.29, 0.28 at n = 8, 16, 32 for
p = 2, w = 3) - doc 23's linearly ESCAPING window (t_lo ~ 0.45 n) is
repaired exactly by letting the diagonal grow with the degree, i.e. by
the k-dependent diagonal that the FF form Gamma_{F^n}^2 ~ q^n chi
dictates. The homotopy theory now only needs to pin the true
self-pairing inside a FAT, n-independent window.

### 5.3 What this does and does not establish

Does: the index mechanism doc 17/23 sought EXISTS at the monoid level,
is stable at scale, has its positive direction along the degree vector,
and is certified (not fitted) wherever the rational criterion holds.
Does not: identify the true diagonal (needs the blocked twisted THH /
(A''), same as doc 23 sec 3); decide fork (N) (the per-weight reading
is branch-(ii)-shaped; the {p^i}-family is max-Gram even in branch (i)
since |p^i - p^j| itself is degree-separated - the verdict is
fork-robust for THIS family, gate W1+W6d); produce any zero-side
statement (fork discipline: nothing here touches the zeros).

## 6. Verdicts on the task's pre-registrations

  - "shadow towers should now GROW with w": CONFIRMED on the
    fixed-point carrier and branch (ii) (q^w - 1, linear log-growth,
    W2); REFUTED in branch (i) (tame collapse Z/(k-l), = Z/(q-1) for
    (q,1); W1). The fork
    relocates; the unconditional carrier of growth is Quillen's
    fixed-point object, not the pairing presentation.
  - "p-part of p^w - 1-type data": sharper than expected - the p-part
    is exactly EMPTY (W3b), the growth is the Euler product of the
    invertible towers at ell != p (W3a): the monoid family is the
    adelic assembly of P's group families.
  - "the (1, q) of the FF Frobenius graph": OBTAINED: d_2 = p
    (phi(v) = pv / psi^p on Bott), p^w per weight; norm-dependent
    ledger reconciling P's (1,1) with doc 23's (1,k) (sec 4).
  - Lorentzian reading R-a: CONFIRMED as certified (sec 5.2), with the
    honest low-weight holes at p = 2, 3 recorded.

## 7. G-INT6 ledger (degrees of freedom vs constraints)

Free choices: the geometric family {psi^{p^i}} (forced by the FF
configuration {Gamma_{F^n}}, not tuned); the diagonal model (degree +
t, the doc-17/23 open-slot protocol, window reported); grids. The
constant -1/4 is a DISCOVERED spectral bound of MAX_n (gated exactly),
not a knob. Matched constraints with zero remaining parameters: W1-W6,
W9 are exact integer/rational identities (hundreds of instances); W7 is
a certified inequality chain (exact Descartes + rational log bounds +
Weyl); W8's w_0 thresholds are measured laws, recorded not fitted.
DISCLOSURE: the signature structure was found by exploration BEFORE the
gates were registered (same protocol as doc 23's outcome recording);
the witness asserts the certified chain and the measured laws
fail-closed, exit-gated. Carrier guard: every object consumes ring or
cyclotomic structure - psi^k are ring operations on K-theory, phi_p
needs the cyclotomic structure of THH, the Witt gates consume W(-) + F
functoriality, K(F_q) needs the field. DH/Epstein: no ring, no
lambda-operations, no THH, no W(-), no K(F_q): dead at the object
level, before any computation (necessary filter, not sufficient).

## 8. Honest limits

1. No new spectrum-level object: blockers (A'') and (B1)-(B3) stand;
   all spectrum-level statements are transcriptions (Hesselholt, NS,
   McCandless, Quillen), cited per item; transcription risk is the
   usual one and hesselholt2016 is the only source read verbatim
   end-to-end here.
2. Fork (N) untouched: P's branch decider (pi_{2p} X(1+p) / the s = 0
   pole test) remains the sharpest next computation; sec 5's verdict is
   fork-robust only for the geometric family.
3. The Lorentzian certificate covers the geometric family with the
   MODELED diagonal; the true diagonal is exactly what the blocked
   twisted computation must supply. The full monoid section is
   measured, not certified. Low-weight p = 2, 3 holes are real.
4. The TC(Z)/TR(Z) low-degree table (sec 1.4) is assembled from
   standard results and NOT re-derived; it is not load-bearing.
5. Sec 1.5's "iota is the archimedean move" is structural commentary
   on Hesselholt's proof, not a theorem about the square; its precise
   square-side formulation is the C5''-infty / properness wall.

## 9. Next steps (ranked)

1. (unchanged, still first) P's fork decider: pi_{2p} X(1 + p) or the
   s = 0 pole dichotomy - now doubly consequential since branch (ii)
   is also where the per-weight Lorentzian scaling lives.
2. The (A'') hunt, sharply posed: an E_1 psi^p: ku -> ku with
   pi_{2w} = p^w - the "spherical delta-ring" program (Morava notes,
   McClure theta) is the live literature direction; EITHER outcome
   closes carrier 2 (a no-go would leave carrier 1 as the unique
   monoid carrier, itself a doc-17-fork-grade fact).
3. Feed the certified (1, n) family into the doc-17 C4 comparison
   step: with the index shape now available, ask whether a
   signature-constrained combination reproduces the EF fingerprint;
   the t-window landmarks (0 in window, width (w log p)/4 - ||E||)
   meet the doc 18/23 scheme constants.
4. Pose the square-side iota (sec 1.6 B3) as a precise C5''-infty
   sub-question: what replaces "W(F_q) embeds in C" for the Nygaard
   prism of the square - the same 2-primary/real-cyclotomic territory
   as O's lambda^{1/2} and S's Tate square (doc 26 front 2 link).
