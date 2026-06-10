# AA - THH of CC's compactified object, strict layer: the norm IS the archimedean half of the product formula on V's character

Status: executed 2026-06-10 (fresh context, worker AA). Task: doc 27
ranked front 3 (cheap probe), feeding doc 28 step 2. Inputs: docs 27,
28; N-cc-square-posing.md (M1-M6); Q-cc-ftest.md incl. postscript;
V-grading-bridge.md in full (Theorem V.1); W-monoid-frobenius.md secs
4-5 (MAX/MIN faces, W6d); doc 19 sec 3 (supply ladders); the three
archived CC PDFs. Witnesses rerun this session: prime_cc_strict_smash_q1
(ALL PASS), prime_cc_grading_invariant_kernel (ALL PASS). New witness
(ALL PASS, exit-gated):

    python3 -m scripts.numerics.witness.prime_cc_thh_norm_filtration

Discipline: no RH / zero-side input; G-INT6 (zero free choices: the
norm is CC's, the character is V's theorem); fail-closed; carrier guard
run explicitly.

HEADLINE. The pre-registered reading is CONFIRMED at the strict layer,
exactly: CC's norm datum (the ||.||-structures of the 2022/2023 papers),
transported along V's universal character chi : (HZ ^ HZ)(1_+) ->
Z[Z\0], is PRECISELY the archimedean filtration of the monoid ring
(weight of the generator [A] = |A|; exact on monoid classes; the cyclic
bar faces preserve it EXACTLY). On the geometric family {[p^i]} the
norm-Gram is the MAX face -- certified Lorentzian (1, n) for all
p in {2,3,5,7,11}, w in {1,2,3}, n+1 <= 13, with NO low-weight anomaly
(strictly better conditioned than W's analytic error term, which fails
at (p,w) = (2,<=2),(3,1)) -- while the p-adic valuations of the SAME
character classes are the MIN face (PD). The two faces recompose W's
rank-2 product-formula split on one CC-internal object: at the strict
THH layer, THE CC NORM IS THE ARCHIMEDEAN HALF OF THE PRODUCT FORMULA,
and the PFD spec's gluing (doc 28 sec 1) has a CC-internal strict
model. What is still missing is the DEGREE (V's verdict stands): the
norm supplies weights, not degrees; the derived version is posed in
sec 5 with its exact missing-ingredient list.

## 0. Pre-registration and disclosures

Fixed before any run (the task card's "expected shape", adopted as the
tested reading): the norm filters the monoid ring Z[Z\0] by |n| -- the
strict THH of the COMPACTIFIED object carries the ARCHIMEDEAN filtration
of the monoid ring. Gates N1-N9 in the witness docstring; branch tables
for N5 (anomaly recording against W's w_0 thresholds).

DISCLOSURES. (a) The N5 signature was explored numerically at
(p <= 7, w = 1, n+1 <= 12) BEFORE gate registration (W-doc protocol);
p = 11, w in {2,3}, n+1 = 13 were unexplored predictions and PASSED.
(b) First N5 run returned None (uncertifiable) on every instance: the
i = 0 diagonal entry is log 1 = 0 exactly, an exactly-zero leading
pivot. Repair = reverse the index order (signature is invariant under
symmetric permutation); a numerical-method fix, no gate changed.

## 1. The normed object and the forced filtration (zero choices)

CC's compactified structure is the total-mass filtration: ||HZ||_n(F) =
{phi in HZ(F) : Sum_{F\*} |phi(x)| <= n}, a sub-S[+-1]-module of HZ
(2022 sec 2; the H^0 objects of both RR theorems are exactly these).
The multiplicative rule on norms is THEIRS, not ours: the proof of 2022
Lemma 5.1 uses that m : HR(X) ^ HR(Y) -> HR(X ^ Y) restricts to
||HR||_lam ^ ||HR||_mu -> ||HR||_{lam mu} ("meaningful in view of [2]
(Proposition 6.1)" -- CC-Consani JNT 2016), and the division shape
Hom_S(||HR||_lam, ||HR||_mu) = ||HR||_{mu/lam} is the lemma itself.
Hence on the strict square the norm filtration is forced:

    F_t (HZ^HZ)(1_+) = union over lam*mu <= t of
                       Image[(||HZ||_lam ^ ||HZ||_mu)(1_+)],
    N(x) = min{lam*mu : x has a representative (a,b,S) with
               mass(a) <= lam, mass(b) <= mu}.

(The image is exactly the classes containing a small representative;
pushforwards never increase mass, |Sum| <= Sum|.|.) Collapsing the
two-parameter filtration by the PRODUCT is Lemma 5.1's own rule.

## 2. Theorem AA.1 (the strict layer; hand proofs + witness N1-N4)

Let chi = chi_col be V's character (Thm V.1), ||Sum c_A [A]||_arch =
Sum |c_A| |A| the archimedean l1-weighted norm on Z[Z\0].

(i) CONTRACTION: ||chi(x)||_arch <= N(x). Proof: for a representative
with masses (lam, mu), every column sum has |A_j| <= mass(a) <= lam and
Sum_j |b_j| <= mu, so Sum_j |b_j||A_j| <= lam mu; bucket cancellation
only helps. Also |e(x)| <= ||chi(x)||_arch. [N1: 42,154 representatives,
0 violations.]

(ii) LOWER BOUND (the sharpening): for any class x and any bucket A
with net coefficient c_A != 0, some column of every representative has
sum exactly A (bucket nets are class invariants, V.1), so lam >= |A|;
and mu >= Sum_j |b_j| >= Sum_A |c_A|. Hence
N(x) >= (max_{c_A != 0} |A|) * (Sum_A |c_A|).

(iii) MONOID-CLASS EXACTNESS: N([A]) = |A| (single-cell representative
attains the bound from (ii)). The norm weight of the monoid generator
is the archimedean absolute value, and it is multiplicative on
generators -- the filtration restricted to the monoid is the
archimedean grading w_infty([A]) = log|A|. [N3: bounded representative
search finds nothing below |A|, A <= 6.]

(iv) DIFFERENCE CLASSES: N([p^i] - [p^j]) = 2 p^max(i,j) exactly.
Upper: the shared-row representative a = (p^j, p^i - p^j), b = (1,-1),
S = {(0,0),(1,0),(0,1)} -- masses (p^i, 2); lower from (ii). [N4.]

(v) THE BAR COMPLEX IS NORM-FILTERED, EXACTLY: the cyclic bar
N^cy(HZ) (V's complex: level q = (q+1)-fold strict smash, faces
multiply adjacent slots, d_q cyclic) preserves the mass product ON THE
NOSE: the merged slot is the full outer product and Sum|u_x v_y| =
(Sum|u_x|)(Sum|v_y|); degeneracies insert the unit (mass 1); the cyclic
operator permutes. So the strict cyclic bar of CC's normed object is a
CYCLIC OBJECT IN NORM-FILTERED Gamma-sets, and its HH_0-level universal
invariant is the monoid ring Z[Z\0] WITH the archimedean filtration.
[N2: 595,318 face instances, exact equality everywhere.]

This is the first place CC's boundary/compactification datum touches a
THH-type invariant, and it touches it as |.|_infty. The pre-registered
reading is confirmed exactly, not approximately.

## 3. The norm-filtration verdict: YES, it is the MAX face (N5-N7)

The KEY QUESTION (task card): does the norm filtration reproduce the
archimedean MAX face the way the p-adic valuations give the MIN faces?

YES, in the following precise, witnessed sense. On the geometric family
{[p^{wi}]}_{i=0..n} (W's family, forced by the FF configuration):

```text
norm-Gram   M[i,j] = log N([p^wi] - [p^wj]) = w max(i,j) log p + log 2
            (i != j; diag = w i log p, the norm weight of [p^wi]):
            = (w log p) MAX_n + log2 (J - I).
            CERTIFIED signature (1, n) -- arb LDL, every pivot
            ball-certified -- for ALL p in {2,3,5,7,11}, w in {1,2,3},
            n+1 in {3,5,8,13}.  NO low-weight anomaly: where W's
            analytic error E[i,j] = log(1 - p^{-w|i-j|}) breaks
            Lorentz at (2, w<=2) and (3, 1), the CC-norm error
            log2(J - I) (J PSD rank 1 aligned with the positive
            direction, -log2 I a uniform negative shift) keeps the
            index shape at every tested weight including (2,1).
v_p-Gram    v_p(e([p^wi] - [p^wj])) = w min(i,j) exactly: the MIN
            face, PD on i >= 1 (exact integer minors, W6c formula),
            PSD with the [1]-kernel at i = 0.  [N6]
the split   MAX + MIN = u 1^T + 1 u^T (u = degree vector): the two
            faces of the SAME character classes recompose the rank-2
            decomposition of W's max-Gram lemma; and on monoid classes
            log N([A]) = Sum_p v_p(A) log p EXACTLY (A <= 20000) --
            the product formula as an identity between the CC-norm
            weight and the valuation weights of one object.  [N7]
```

CONSEQUENCE FOR DOC 28 (step 2): the PFD gluing demand -- "the p-adic
MIN faces and the archimedean MAX face are two readings of ONE object"
-- has a CC-INTERNAL STRICT MODEL: the object is V's character lattice
Z[Z\0]; the archimedean reading is CC's own norm transported along chi
(theorem-sourced: 2022 sec 2 + Lemma 5.1/[2] Prop 6.1); the p-adic
readings are the valuations of the bucket labels (unique factorization
of Z); the identification is literal factorization. K6 holds at this
layer: zero free choices were spent (sec 7 ledger). What this model
does NOT have: degrees (V), H^1/duality content, any zero-side
statement. It is the strict shadow of the gluing, not the gluing.

## 4. Supply-ladder contact (doc 19) and Q's no-go, revisited

- w_infty([p^i]) = i log p = Sum_{j=1..i} Lambda(p^j) with Lambda(p^j)
  = log|THH_{2j}(F_p)| = log p (doc 19 sec 3): the norm-Gram DIAGONAL
  on the geometric family is the cumulative supply ladder. The VALUES
  carry zero choices (both sides are theorem-sourced numbers); the
  INDEX dictionary (tower step j <-> THH degree 2j) is
  observation-grade -- exactly V's missing grading. Values yes,
  degrees no. [N8]
- Q 5.4 placement (important for the derived pose): the archimedean
  filtration's weight set is {log k : k >= 1} -- NOT a b-adically
  geometric set, and NOT quantized. Q's pole no-go applies to QUANTIZED
  (dim_S-rounded) towers; the norm filtration lives on the
  pre-quantization side, where the smooth tower regularizes
  (Sum_reg log_2 k exists; Q sec 5.3). The compactified strict THH
  keeps the regularizable datum; it dies only if one applies dim_S.
  This is the precise sense in which the norm filtration is the
  CARDINALITY-level (R(iii)-strong-compatible) carrier the F-WEAK
  bypass asked for -- still ungraded.

## 5. The derived version, posed (layer 3; nothing here is claimed)

POSED OBJECT: THH^{||.||}(Z) := the realization of the cyclic object
{(||HZ||-filtered (q+1)-fold DERIVED smash)}_q in a category of normed
(filtered) S-modules, with the filtration collapse rule Pi lam_i (sec 1,
theirs) and the cyclic structure of sec 2(v). The strict E_0-layer is
computed in this document: the character lattice Z[Z\0] with the
archimedean filtration, faces exact.

EXACT MISSING INGREDIENTS (N-doc M-list extended):
1. M4 (monoidal tolerant modules): the NORM half of the smash exists
   ([2] Prop 6.1, used in sec 1); the TOLERANCE half (the relation on
   E_1 ^ E_2) is still undefined. CC's ||D||-objects carry norm AND
   tolerance at the curve level; the square needs both.
2. M3 (higher pi_n^T / long-complex Dold-Kan): realization of the
   simplicial direction with tolerance at every level; nothing in
   print past pi_1^T.
3. Q-T3 (derived replacement compatible with the norm): a cofibrant
   replacement of HZ as a NORMED S-algebra -- a "normed model
   structure" with no print precedent. Nearest existing template: the
   filtered/Rees-construction THH of BMS (bms2018, archived) -- the
   p-adic analogue; no archimedean version exists.
4. THE ABUTMENT: the norm filtration induces a spectral sequence of
   the filtered cyclic object; demand its E_1 in terms of the
   associated graded (the strict layer computed here) and its
   abutment = THH(Z) with an ARCHIMEDEAN weight filtration. This SS is
   the first object in which V's missing DEGREE (the simplicial/THH
   axis) and this document's WEIGHT (the norm axis) coexist; the
   program's R(iii)-strong demand becomes: the degree-(2k-1) line
   carries weight log k. That statement -- not any strict computation
   -- is where the Bokstedt tower would meet the supply ladder.
5. Base S[+-1] (M6/Q's caveat) for the real/THR flavor; untouched.

FAIL-CLOSED note: items 1-3 are prerequisites, not gaps in an argument;
no part of secs 2-3 depends on them.

## 6. Carrier guard (layer 4; N9 + audit)

Where the construction dies for Epstein (lattice L = Z^2,
Q(x,y) = x^2 + 5y^2, metric only -- it has a norm, no multiplication):

```text
E1 ALIVE (carrier-blind): HL ^ HL, the CC norm filtration on HL, the
   transport chi into Z[L\0], and the ARCH-NORM GRAM: witnessed
   Lorentzian (1, n) on the degree-separated family v_i = (3^i, 1)
   [N9 PASS -- and its PASS is the guard's content: the archimedean
   MAX face ALONE discriminates nothing, exactly as K-doc sec 0
   demands of every PD-flavored layer].
E2 DEAD: the monoid ring. Z[L\0] is a free abelian group on a SET; no
   mu => no multiplication of bucket labels => Thm V.1(iii) has no
   target. The character exists; the CHARACTER ALGEBRA does not.
E3 DEAD: the MIN faces. No factorization of bucket labels => no v_p
   => no valuation Grams.
E4 DEAD: the product formula. log||v|| = Sum_p v_p(v) log p is not
   even formable: the right side has no terms. The gluing of sec 3
   has ONE SIDE for Epstein.
E5 DEAD: the cyclic bar. Every face consumes mu (V sec 5): levels
   >= 1 of N^cy do not exist. There is no strict THH of "compactified
   Epstein" to compute.
DH: no carrier group at all; dies at E1 (before the norm).
```

This is the doc 28 K5 profile, sharpened: CC's norm alone is
carrier-blind; it becomes the archimedean HALF OF THE PRODUCT FORMULA
only over a carrier with multiplication and unique factorization. The
discriminating content is in the coupling, never in the norm.

## 7. G-INT6 ledger

```text
claim                       choices spent            constraints matched
sec 1 filtration/product    0 (CC 2022 sec 2,        their Lemma 5.1 +
rule                        Lemma 5.1, [2] Prop 6.1) [2] Prop 6.1: SOURCED
Thm AA.1 (i),(iii),(v)      0 (chi = V.1, forced)    hand proofs + N1-N3
                                                     exact: DERIVATION
Thm AA.1 (iv) N = 2p^max    0                        hand proof + N4
                                                     bounded search:
                                                     DERIVATION
sec 3 MAX face (1,n)        family {p^i} (W's,       60 certified
                            FF-forced); sizes        signatures incl.
                            (calibration)            unexplored
                                                     predictions: LAW
sec 3 product-formula       0                        exact identities
split                                                (N6, N7): DERIVATION
sec 4 supply contact        index dictionary         values exact;
                            (1 choice, unmatched)    OBSERVATION-grade
sec 5 derived pose          n/a (posed, not          fail-closed: zero
                            claimed)                 claims
```

## 8. Honest limits

- N(x) lower bounds are hand proofs (Thm AA.1(ii), via V.1's bucket-net
  invariance); the witness searches are bounded confirmations (dims
  <= 2x3, bounded entries), not exhaustive over all representatives.
  The hand proof is the load-bearing item; the search guards against
  algebra slips.
- The search space in N3/N4 is "representatives with matching chi",
  a SUPERSET of the class (class membership is undecidable by chi
  alone); inclusion goes the safe way: nothing below the bound in the
  superset implies nothing below it in the class.
- Signature certificates only at the listed (p, w, n) -- no asymptotic
  claim (doc 13's wall respected). No analogue of W's n-independent
  Weyl criterion is proven here: interlacing gives n_+ <= 2 for all n;
  the pin to (1, n) is per-instance certification.
- Thm V.1(ii)'s completeness is window-scoped (V's limit, inherited):
  invariants of non-column/row shape are unclassified; the norm could
  carry MORE than the archimedean filtration on such invariants.
- Over S; the S[+-1] relative smash not redone (Q/V caveat stands).
  CC's [2]/[3]/[4]/[5] remain unarchived; the [2] Prop 6.1 product
  rule is taken from CC 2022's explicit citation in the Lemma 5.1
  proof, read in the archived PDF this session.
- Sec 4's degree dictionary is an unmatched choice (observation);
  sec 5 is a demand sheet. No statement touches zeros, the explicit
  formula's spectral side, or any RH-conditional input.

## 9. Sources

- connes-consani-2022-riemann-roch-specZbar.pdf: sec 2 (||HZ||_n,
  ||HR||_{e^a}, total mass), Lemma 5.1 + proof (m-maps, [2] Prop 6.1
  citation), Prop 3.3, Def A.2.
- connes-consani-2023-riemann-roch-ring-Z.pdf: Def 2.1, Thm 3.3 (the
  over-S normed dimensions; context).
- connes-consani-2026-jacobian-specZbar.pdf: sec 1 framing only.
- Program docs: research/proof/19, 27, 28; research/work/N, Q, V, W.
- Witnesses: prime_cc_thh_norm_filtration.py (new, this doc);
  prime_cc_strict_smash_q1.py, prime_cc_grading_invariant_kernel.py
  (rerun, ALL PASS).
