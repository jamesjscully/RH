# XX - Bridge B1 executed: the scale-blindness theorem (T1), the Tate-curve liquid calibration (T2), the fracture-corner bookkeeping (T3), and LS3 posed at adoption grade

Status: fresh-context worker XX, 2026-06-11, under the charter (doc 38,
bridge B1). Required reading executed in order: doc 38;
MM-liquid-slot.md IN FULL (the LS1-LS6 spec, the literature map, the
T1-T3 verdicts, the Route B block at LS3+LS4); FF-kappa-on-xbar.md
(Prop FF.1, FFG2 Aut(R/Z) rigidity); QQ-native-face.md (Delta_p - the
LS4 test data); refs read at theorem level THIS SESSION (text extracted
from the archived PDFs and quoted below from the extractions):
efimov-2024-k-theory-localizing-invariants-large-categories.pdf
(arXiv:2405.12169), clausen-scholze-2022-condensed-complex-geometry.pdf,
scholze-clausen-analytic-geometry-lectures.pdf (via MM's verified
quotations), plus JJ AJ3 and BB-r2/comb sections (grep-verified).

Witness (NEW, pre-registered, fail-closed, exit-gated):

    python3 -m scripts.numerics.witness.prime_xx_b1_liquid
    (gates XB1-XB8; exit 0 iff ALL PASS)

DISCIPLINE RECORD: section 0 (registrations, nulls, gate list) was
written BEFORE the witness file existed; the witness was then written
to the registered gates and run. FULL DISCLOSURE: the verdict prose of
secs 2.4/3.4 was DRAFTED from the registered expectations before the
first run and CONFIRMED UNCHANGED by it - the witness passed ALL
GATES on its first complete invocation (exit 0), deterministic across
3 runs (logs /tmp/xx_run2-3.log diff-identical); no gate predicate,
tolerance, or registered reading was amended at any point. Had any
gate failed, the drafted verdicts would have been struck and the
failure reported full-value (fail-closed). One post-run edit,
disclosed: a vacuous XB8 transition clause was replaced by a real
iteration check (strengthening only; rerun ALL PASS, exit 0). T1 and the LS3 section are citation/derivation
work and carry no witness weight. F-a: no zeta values, no zeta
continuation, no zero-side input anywhere; kappa = pi appears ONLY as
the required-output clause of the LS3 conjecture (comparison frame).
G-INT6: the Gaussian e^{-pi x^2} is the one logged analytic import
(JJ/QQ lineage); every other ingredient below is cited or exact.

## 0. Registrations (written before the witness was first run)

PRE-REGISTERED NULL FOR T2 (MM sec 3 Route A, restated): the Tate-curve
liquid trace data, transported through the q-grading to the banked
one-place comb, is SCALE-FREE: every trace-layer number the printed
liquid theorems output for X_p = C^x/p^Z is p-independent (chi(L_d)=d,
residue = 1), the comb identity holds with atom weight = atom spacing
= 2pi/log p (BB-r2 at liquid level), and NO normalization beyond the
banked 2pi appears. Route A is a calibration; a nonzero reading (any
p-dependent trace number, any new constant) would be a reportable
shock, fail-closed.

PRE-REGISTERED PREDICTION FOR T3: the liquid/condensed R corner does
NOT repair the arithmetic fracture square itself (R is fracture-inert:
all finite-place completions of R vanish); the new nonzero corner
appears one layer up, in the LATTICE/cocompactness data - the quotient
S_p = (Q_p x R)/Z[1/p] exists as a compact connected condensed group
where spectra have only a dense image, with covolume pinned to 1 by
the product formula. Either half failing = reportable.

GATES (fail-closed; exact Fractions/integers for algebra, flint arb
prec 300 for analytic values, certified tails folded into tolerances):

```text
XB1 TATE-CURVE RR (exact): on X_p = C^x/q^Z, q = 1/p, p in {2,3,5}:
    sections of the degree-d automorphy bundle L_d (f(qz) = z^{-d}f(z))
    have h^0 = d for d in 1..6 (recursion a_{n+d} = q^n a_n: d free
    orbits, quadratic exponent growth certified by exact second
    differences = +d), h^0(L_{-d}) = 0 (second difference -d: blow-up,
    only 0 decays), h^0(O) = 1 (a_n(q^n - 1) = 0 forces a_n = 0,
    n != 0). chi(L_d) = d = deg(L_d): the HRR number, integer-exact,
    p-INDEPENDENT (null clause). Theta functional equation for d = 1:
    coefficient identity n(n-1)/2 + n = n(n+1)/2, exact integers.
XB2 SERRE/RESIDUE NORMALIZATION (arb): (1/(2 pi i)) oint dz/z = 1 on
    |z| = 1 (trapezoid N = 256, tol 1e-20): the trace number is 1,
    constant-free, p-independent; the period integrals of dz/z are
    2 pi i (vertical cycle) and log q = -log p (radial cycle): the
    circumference enters the PERIOD LATTICE only, never the trace.
XB3 TRANSPORTED COMB = BANKED COMB (arb): Poisson identity on
    (log p)Z <-> (2pi/log p)Z against Gaussian tests phi_s
    (s in {1, 1/2}), p in {2,3,5} and the scaling control p -> p^2:
    sum_n phihat(n log p) = (2pi/log p) sum_k phi(2pi k/log p) to
    1e-25 with certified tails; weight/spacing = 1 recorded (BB-r2
    replication through the q-grading address). NULL: no constant
    beyond the banked 2pi.
XB4 CARRIER CLAUSE (exact): the q-grading address group p^Z is a free
    rank-1 valuation monoid (v(p^a p^b) = a + b, bijective address);
    recorded as the carrier contrast for XB5.
XB5 EPSTEIN KILL-TEST AT THE T2 COUPLING (exact + arb): Q(x,y) =
    x^2 + 5y^2: (a) carrier death: 36 = 4*9 = 6*6 with 4, 6, 9
    irreducible in the represented-value monoid (exact enumeration);
    no valuation, no q-expansion address -> the XB3/XB4 coupling is
    UNDEFINABLE; (b) PD/theta ALIVE: theta_Q(s) =
    (1/(s sqrt 5)) theta_Q*(1/s), Q* = x^2 + y^2/5, at s in
    {1/2, 1, 2} to 1e-25. REQUIRED profile: death at the coupling
    with the theta layer alive (JJ AJ7 / MM 4.3). A coupling that
    computes for Epstein = vacuous, route dies.
XB6 R IS FRACTURE-INERT (exact): (a) divisibility certificates
    (n x = r solvable in Q exactly, all sample n, r) + the
    non-divisibility contrast (p x = 1 unsolvable in Z/p^k, exact)
    - the finite-level instances of R (x) Z/n = 0, Tor(R, Z/n) = 0,
    R^wedge_p = 0; (b) AJ3 replication: minimal denominator of
    ((1/p))_{p in S} in the A_f corner = primorial(S), unbounded
    (exact Fractions, |S| <= 8).
XB7 THE NEW CORNER EXISTS WITH R PRESENT (exact): p in {2,3,5}:
    (a) WITHOUT R: Z[1/p] dense in Q_p (digit partial sums: v_p(x - z)
    >= 12 on deterministic samples) - no discrete corner; (b) WITH R:
    Z[1/p] discrete cocompact in Q_p x R: fundamental domain
    Z_p x [0,1) - existence + uniqueness of the representative on
    exact samples (uniqueness via Z[1/p] cap Z_p = Z, denominator
    check, + window (-1,1)); covolume = 1 and product formula
    |p^k|_p |p^k|_oo = 1 exact for k in -6..6; (c) torsion shadow of
    the corner = the banked Prufer comb: orders in Z[1/p]/Z are exact
    p-powers.
XB8 ADDRESS/SCALE SPLIT ON THE CORNER (exact bookkeeping): Cech
    H^1(S_p) = colim(Z --p--> Z) = Z[1/p]: directed-system bookkeeping
    exact at finite level; Z[1/p] != Z[1/q] (denominator check: the
    corner is PLACE-ADDRESSED) while the system is defined over Z with
    no occurrence of log p (the corner is SCALE-FREE) - the
    address/scale split as exact structure.
```

## 1. T1 - THE SCALE-BLINDNESS THEOREM (citable; the door-closer that names the door)

### 1.1 Efimov's theorems, transcribed (arXiv:2405.12169, archived PDF, text extracted this session)

Setting (Efimov's, from the surrounding text of the statements): X is
a locally compact Hausdorff space; C is a presheaf on X with values in
Cat^dual_st (presentable stable dualizable categories with strongly
continuous functors); Shv(X; C) is the category of C-valued sheaves,
which is dualizable [Lur18]. For a localizing invariant
F : Cat^perf -> E, F^cont denotes its continuous extension to
dualizable categories (the right Kan extension along
Ind : Cat^perf -> Cat^dual_st).

THEOREM 0.2 (Efimov, verbatim from the extraction). "With the above
notation, let E be a presentable stable infinity-category, and
F : Cat^perf -> E a localizing invariant which commutes with filtered
colimits. Then we have a natural isomorphism

    F^cont(Shv(X; C)) ~ Gamma_c(X, F^cont(C))."

(Its sheaf-level form is Theorem 6.11: U^cont_loc(Shv(X; C)) =
Gamma_c(X, (U^cont_loc(C))^sharp) in Mot^loc, "hence this also holds
for any finitary localizing invariant, for example, for K-theory.")

PROPOSITION 4.18 (Efimov, verbatim). "For a dualizable category C we
have

    U^cont_loc(Shv(R; C)) ~ Omega U^cont_loc(C),
    U^cont_loc(Shv(R cup {-oo}; C)) = 0.

Hence, the same holds for any finitary localizing invariant, for
example, for K-theory."

THEOREM 6.1 (Efimov, verbatim). "Let X be a finite CW complex,
considered as a topological space. Let C be a dualizable category.
Then for any accessible localizing invariant F : Cat^perf -> E we
have an isomorphism

    F^cont(Shv(X; C)) ~ F^cont(C)^X.

Here in the right hand side we consider X as an object of S^fin"
(finite spaces, i.e. X enters only through its homotopy type).

Hypotheses, listed exactly: (i) constant coefficients C dualizable
(6.1) or a Cat^dual_st-valued presheaf (0.2); (ii) F a LOCALIZING
invariant of Cat^perf (sends Verdier quotients to fiber sequences),
accessible (6.1) or finitary/filtered-colimit-preserving (0.2);
(iii) the invariant is applied to the BARE category Shv(X; C);
(iv) everything is Sp-linear (Cat^perf, Mot^loc are over spectra).

### 1.2 Corollary XX.1 (the program-facing no-go)

COROLLARY XX.1 (scale-blindness of sheaf-theoretic traces). Let
T_p = R/(log p)Z with its quotient topology, and let C be any
dualizable category. Then:

(a) For every accessible localizing invariant F : Cat^perf -> E,

    F^cont(Shv(T_p; C)) ~ F^cont(C)^{S^1},

    naturally and INDEPENDENTLY of p. More precisely the assignment
    p -> F^cont(Shv(T_p; C)) factors through the homotopy type S^1,
    which is the same for all p.

(b) The same holds for the full lattice diagram: the image under
    F^cont(Shv(-; C)) of the diagram ((log p)Z -> R -> T_p) is
    naturally equivalent to the image of the p-independent homotopy
    diagram (Z -> * -> BZ); in particular
    F^cont(Shv(R; C)) ~ Omega F^cont(C) for all p (Prop 4.18), with
    p-independent comparison maps.

(c) Hence NO function of the data {F^cont(Shv(T_p; C)), the induced
    functor maps, natural traces among them} can distinguish log p
    from log q, and a fortiori none can produce BB's gate observable
    c_oo = -(1/2) log kappa as a function of such data. No
    sheaf-theoretic trace on Shv(R/(log p)Z) distinguishes p.

PROOF. Two layers, in increasing strength.

(Elementary layer, stated for honesty.) The scaling map
x -> x / log p is a HOMEOMORPHISM T_p ~ R/Z = S^1: circumference is
metric data, not topological data. Hence already Shv(T_p; C) ~
Shv(S^1; C) as categories, for constant coefficients, and EVERY
invariant whatsoever of the bare category is p-independent. This
layer needs no theorem.

(Efimov layer, what the theorem adds.) The elementary layer leaves
open that p might be recovered from the FUNCTORIAL position of
Shv(T_p; C) among sheaf categories - from the maps induced by
R -> T_p, by the lattice inclusion, by correspondences, or by
non-homeomorphic comparison spaces, since the scaling homeomorphism
does not commute with a fixed identification of the R's. Theorem 6.1
closes this: T_p is a finite CW complex, so F^cont(Shv(T_p; C))
depends only on the object S^1 of S^fin, NATURALLY in the space; and
Theorem 0.2/Prop 4.18 compute the invariant of every space in the
lattice diagram as a proper-homotopy-invariant functional
(Gamma_c(X, -)) of p-independent data. In the homotopy category the
diagram ((log p)Z -> R -> T_p) is (Z -> * -> BZ) for every p, and
all induced maps on invariants are the corresponding p-independent
maps. Any natural trace built from localizing-invariant data of
these categories therefore takes equal values at p and q. QED.

This is Prop FF.1's pattern one level up, now CITABLE AS THEOREM
rather than analogy (MM 2(c) located it; this section is the
transcription + derivation MM mandated). It retires permanently the
cheap version of the liquid route: kappa cannot come from any
sheaf-theoretic/localizing-invariant trace on the topological circle.

### 1.3 What the proof does NOT cover (the named door; B4 lives here)

The hypotheses of 1.1 are sharp, and each failure mode is a distinct
enrichment. The complement, stated exactly:

```text
N1 NON-CONSTANT METRIZED COEFFICIENTS: Theorem 0.2 allows a presheaf
   C of coefficients, but then F^cont(Shv(X; C)) = Gamma_c(X,
   F^cont(C)) - the answer can depend on p ONLY through the
   coefficient presheaf. A presheaf U -> Mod_{O_liq(U)} whose values
   carry the metric (liquid growth conditions are not invariant
   under the scaling homeomorphism) is NOT excluded by the theorem;
   the theorem rather LOCALIZES the only possible carrier in the
   coefficients. This is the exact sense in which "the carrier must
   be the metrized object" (MM 2(c)).
N2 MODULE CATEGORIES OVER ANALYTIC RINGS: Mod_{O(T_p)}(Liq(R)) - the
   liquid modules over the FUNCTION ALGEBRA with its norms - is not
   of the form Shv(X; constant C); nothing in Efimov theory computes
   its invariants (MM 2(d): no THH/K of liquid analytic rings in
   print). The theorems are silent here.
N3 EQUIVARIANT/PARAMETRIZED REFINEMENTS: the rotation action of the
   GROUP T_p on Shv(T_p; C) and genuine-equivariant or parametrized
   localizing invariants over the family of groups {T_p}_p are
   outside the statements (which are absolute and non-equivariant).
   The group T_p, unlike its underlying space, has Aut_top = {+-1}
   rigidity (FF FFG2) - the group structure is exactly what the
   homotopy type forgets.
N4 TRACES OF NONTRIVIAL KERNELS: the theorems compute the ABSOLUTE
   invariant. LS4's tr_L is the trace of a specific
   object/endofunctor (the banked comb b(comb_p) against R);
   correspondence-level data (kernels, microlocal/Fourier-Sato
   structure, singular support - cf. Zhang arXiv:2506.02329) is
   covered only insofar as it is natural in the bare space.
N5 NON-Sp-LINEAR BASES: the whole trace theory (incl. Efimov
   arXiv:2510.17010 rigidity) is Sp-linear; a liquid-linear or
   gaseous-linear localizing-motive theory, where the unit and the
   dualizing data themselves are liquid, does not exist in print
   (MM 2(c)/(d)) and is not constrained by these theorems.
```

B4 (doc 38) = engineer the minimal enrichment among N1-N5 that sees
circumference. The LS3 conjecture (sec 4) lives at N2+N3+N5
simultaneously: liquid module category, group-rigidity datum, liquid
base.

## 2. T2 - ROUTE A EXECUTED: the Tate-curve liquid calibration vs the banked comb

### 2.1 The printed inputs (all theorem-grade, archived)

- THEOREM 13.6 (Clausen-Scholze, Condensed Mathematics and Complex
  Geometry, verbatim from the extraction): "For a d-dimensional
  smooth map f : X -> Y of (generalized) complex-analytic spaces,
  there is a natural isomorphism f^! M ~ f^* M (x)_{O_X}
  Omega^d_{X/Y}[d] of functors C_Y -> C_X." For X proper over
  Y = pt: "the usual Serre duality, extended from coherent sheaves
  to all 'liquid quasicoherent sheaves'": the dual of RGamma(X, M)
  is RGamma(X, M^v (x) Omega^d_X)[d].
- THEOREM 13.10 (GAGA, verbatim): "The fully faithful functor
  D_pc(X) -> D_pc(X^an) is an equivalence of infinity-categories."
  ("the mere fully faithfulness already includes the comparison of
  cohomology.")
- HRR (Lectures XIV-XV): chi(X, V) = int_X ch(V) Td(T_X), proved for
  compact complex manifolds with the Chern character valued in HODGE
  cohomology (Hdg(X) = (+)_i Omega^i[i]); MM's observation stands in
  the text: the normalization is deliberately constant-free (no 2pi
  anywhere in the trace layer).

CONSEQUENCE used below: for the Tate curve X_p = C^x/p^Z (= C^x/q^Z,
q = 1/p, a compact complex manifold of dimension 1), the liquid
cohomology of (pseudo)coherent objects IS the classical coherent
cohomology (13.10 + 13.6), so the classical theta/Laurent computation
below computes the LIQUID trace data - this is what makes Route A
executable today, and is the entire point of the calibration: the
formalism's first contact with our objects.

### 2.2 The computation (witnessed, XB1-XB4)

Sections of the degree-d bundle L_d (automorphy f(qz) = z^{-d} f(z))
are Laurent series sum a_n z^n with a_{n+d} = q^n a_n: d free orbits
n mod d, exponent second difference exactly +d (theta-type quadratic
decay, certified exact), so h^0(L_d) = d; the dual recursion blows up,
h^0(L_{-d}) = 0 = h^1(L_d) (Serre, Omega ~ O); h^0(O) = h^1(O) = 1.
HRR reads chi(L_d) = deg(L_d) = d: INTEGER, p-INDEPENDENT. The Serre
trace is the residue res(dz/z) = 1 (Hodge-normalized: constant-free);
the circumference log p and the banked 2pi appear ONLY in the period
lattice of dz/z (radial period log q = -log p, vertical period
2 pi i) - i.e. only in the ADDRESS data, never in a trace number.

THE COUPLING TO THE BANK: the q-expansion grading of sections is by
the lattice p^Z (the monoid address of JJ/AA: a free rank-1 valuation,
XB4); its |.|-image is (log p)Z subset R, whose Pontryagin/Poisson
exchange is the banked one-place comb: pairing against Gaussian tests,

    sum_n phihat(n log p) = (2pi/log p) sum_k phi(2pi k/log p),

atom weight = atom spacing = 2pi/log p (XB3) - BB-r2's banked
identity, reproduced through the Tate-curve grading.

### 2.3 The Epstein kill-test at this coupling (XB5)

Replace p^Z by the represented-value monoid of Q(x,y) = x^2 + 5y^2
(JJ AJ7's form). The theta/PD layer MUST survive and does:
theta_Q(s) = (1/(s sqrt 5)) theta_{Q^*}(1/s) certified (Poisson is
lattice-blind). The COUPLING dies: 36 = 4*9 = 6*6 with 4, 6, 9
irreducible (exact) - no valuation, no tower address, no q-expansion
grading, so the XB3/XB4 transport is UNDEFINABLE for Epstein. Death
at the coupling with the count/theta alive: exactly the required
profile (MM 4.3). The T2 coupling is NOT vacuous.

### 2.4 Verdict (filled after the run)

WITNESS ALL PASS (XB1-XB8, exit 0, deterministic; see witness header
for the engineering record). THE PRE-REGISTERED NULL IS CONFIRMED,
CERTIFIED: every trace-layer number is p-independent (chi(L_d) = d
exact; residue 1 to 1e-20; comb identity to the 1e-25 gate tolerance
with weight/spacing = 1 at p in {2,3,5} and at the p -> p^2 control);
no
normalization beyond the banked 2pi appears anywhere. Route A is
banked AS A CALIBRATION: the in-print liquid formalism (Serre 13.6 +
GAGA 13.10 + HRR XIV-XV) touches the program's objects for the first
time, reproduces the banked comb through the q-grading, produces no
kappa at one place (BB-r2 at liquid level, as registered), and its
coupling passes the Epstein guard. The calibration also CONFIRMS in
the formalism what MM verified in the text: the printed liquid trace
layer is constant-free - nothing in it can derive kappa; that burden
sits entirely on LS3 (sec 4).

## 3. T3 - FRACTURE-CORNER BOOKKEEPING: what the condensed/liquid square ADDS

### 3.1 The banked spectra-level corner (JJ AJ3, restated exactly)

The rational layer of the Anderson unit does not place-split: it is
ONE global Q. The fracture-square corner holding the per-place
rational data is (prod_p Z_p) (x) Q = A_f (restricted product =
bounded denominators; witnessed at finite level by unbounded minimal
denominators, re-certified XB6b). The completion A = A_f x R has NO
fracture slot for R in plain spectra: the infinite place is
structurally absent (JJ: "absent, not merely undetermined").

### 3.2 What the condensed R corner does NOT do (XB6)

The arithmetic fracture square is algebra, and it is UNCHANGED in
Cond(Ab)/liquid: the square of Z still has corners Q, prod_p Z_p,
A_f. The object R, now present, is FRACTURE-INERT: R (x) Z/n = 0 and
Tor_1(R, Z/n) = 0 (divisible + torsion-free; finite-level instances
certified XB6a), hence R/p^k R = 0 and R^wedge_p = lim R/p^k = 0:
every finite-place corner of R vanishes, and R's own fracture square
is (R; R, 0, 0). REGISTERED PREDICTION CONFIRMED: the liquid R does
not repair the square - there is no fourth corner of the SAME square.
(This is FF 1.2 from the other side: R is invisible mod p for the
same reason the mod-p world is kappa-blind.)

### 3.3 What it DOES add: the cocompactness corner (XB7, XB8)

The new object appears one layer up, where the lattice meets its
completions. At one place, exactly:

```text
WITHOUT R (spectra-shadow situation): Z[1/p] subset Q_p is DENSE
  (digit partial sums, certified): no discrete complement, no
  quotient of the right shape - the "corner" is a dense image.
WITH R (condensed situation): Z[1/p] subset Q_p x R is DISCRETE
  COCOMPACT: fundamental domain Z_p x [0,1) (existence + uniqueness
  certified exact; uniqueness pivot Z[1/p] cap Z_p = Z), and the
  covolume is 1 BY THE PRODUCT FORMULA |p^k|_p |p^k|_oo = 1 (exact).
  The quotient S_p = (Q_p x R)/Z[1/p] EXISTS as a compact connected
  condensed abelian group - the p-solenoid.
```

The corner object S_p has exactly the two layers the program's
dictionary demands (FF 1.1's "no slot" row, materialized): its
TORSION shadow is the banked Prufer comb Z[1/p]/Z ~ Z(p^oo) (orders
exact p-powers, XB7c) = what plain spectra retain (the I_{Q/Z}
layer); its CONNECTED layer is the R-fiber = exactly the datum the
torsion shadow deletes. Globally the same bookkeeping glues over all
places: A = A_f x R is the unique completion making Q cocompact
(covolume 1 = the product formula), which is LS2(ii)'s clause in
checkable form.

### 3.4 The address/scale split, now theorem-shaped (XB8 + T1)

The three-row ladder, exact:

```text
object            sheaf-level invariants        what it carries
T_p (circle)      F^cont(C)^{S^1}, all p alike  NOTHING (T1: blind)
S_p (solenoid)    Cech H^1(S_p) = colim(Z -p-> Z) = Z[1/p]: PLACE-
                  ADDRESSED (Z[1/p] != Z[1/q], exact) but SCALE-FREE
                  (the directed system is over Z; no log p anywhere)
Mod_{O(T_p)}      not computed by anything in print (T1 N2): where
(liquid)          log p must live - LS3's home
```

Note the precise fit with T1: S_p is compact Hausdorff but NOT a
finite CW complex, so Theorem 6.1 does not apply to it; Theorem
0.2/6.11 DOES, and the answer (Gamma_c over the solenoid) is
p-dependent through the SHAPE Z[1/p] - the new corner carries the
place ADDRESS at sheaf level while still carrying no SCALE. The
fracture-corner addition is therefore: address into the sheaf layer
(solenoid corner, free, from printed structure), scale still and
only in the metrized/liquid layer (the named door). VERDICT
(registered prediction confirmed, witnessed XB6-XB8): the condensed
square adds a nonzero corner NOT in the fracture square but in the
cocompactness layer, with the product formula as its covolume
normalization - the exact category-level locus where LS2(ii) sits.

## 4. LS3 POSED AT ADOPTION GRADE (the communicable artifact)

This section is self-contained: a condensed-mathematics expert can
evaluate it without reading the program. Notation is standard
(Clausen-Scholze liquid/gaseous categories).

### 4.1 Conjecture (liquid Fourier self-duality with Gaussian fixed unit)

Let C = D(Liq_{p'}(R)) for some 0 < p' <= 1 (Scholze, Lectures on
Analytic Geometry, Thm 6.5/6.6: an abelian category of p'-liquid
condensed R-vector spaces with a unique symmetric monoidal tensor),
or its gaseous light-condensed variant. Write R for the liquid
analytic ring on the condensed reals, T = R/Z (condensed circle
group). Recall the classical rigidity Aut_{TopGrp}(R/Z) = {+-1}.

CONJECTURE LS3. There exist
(i)  a "Schwartz object" S(R) in Mod_R(C): a nuclear R-module object
     stable under the unitary R-action and under multiplication by
     characters, with a trace-class structure map to the unit;
(ii) an internal duality F : S(R) -> S(R) with kernel a character
     pairing e : R x R -> T, such that F o F = (-1)^* (inversion),
     and F extends to an equivalence Mod_R-type Fourier duality;
such that
(iii) RIGIDITY PINS THE TORSOR: the normalization freedom of (e, F)
     (a priori a torsor under R^x_{>0} from rescaling the character
     and the invariant functional) is reduced BY the internal group
     rigidity Aut(T) = {+-1} to exactly {+-1} - no continuous
     normalization survives;
(iv) GAUSSIAN FIXED UNIT: F has a fixed point g in S(R), unique up
     to the {+-1} of (iii), and under the comparison functor to
     classical functions g maps to x -> e^{-pi x^2}.

OUTPUT: the constant pi is then a THEOREM of C: the unique self-dual
pair (invariant functional, fixed unit) determines the normalization
e^{-pi x^2} internally - "we choose e^{-pi x^2}" (van der Geer-Schoof,
Tate) becomes forced. In the program's gate notation: kappa = pi OUT,
never inserted.

### 4.2 Expected proof inputs, all from the printed corpus

```text
- Liq foundations: Analytic.pdf Thm 6.5 (category + tensor), Thm 6.6
  (the hard kernel theorem; Lean-verified).
- Internal-duality template with liquid coefficients: Complex.pdf
  Thm 13.6 (Serre duality, liquid), Thm 12.15/12.18 (finiteness/
  nuclearity for proper maps), Lect XIV-XV (HRR trace formalism,
  Hochschild functoriality via [HSS17]).
- The p-adic structural precedent: Anschutz-Le Bras arXiv:2111.11116
  (a Fourier self-duality internal to a CS-style analytic category,
  kernel supplied by a geometric character object) - the SHAPE proof
  of concept; the archimedean instance is what LS3 asserts.
- The rigidity pin: Aut_top(R/Z) = {+-1} (classical theorem).
- The no-go boundary (this doc, T1): the duality CANNOT be
  sheaf-theoretic over the bare space (Efimov 2405.12169 Thm 0.2/
  6.1); it must live on the liquid module category of the analytic
  ring (N2/N5 of sec 1.3). Any proposed proof that factors through
  Shv(topological circle) is wrong by theorem.
- KNOWN GAP (honest): nothing in print supplies a 6-functor or trace
  theory for gaseous/liquid R itself (MM 2(d)); clause (i) is where
  that foundation is consumed.
```

### 4.3 The three demand-side certificates LS3+LS4 must reproduce

These are certified numerical/exact facts (program witnesses, all
fail-closed, cited); any candidate theory is FALSIFIED by missing
any one. Stated self-contained:

```text
CERT 1 (the per-place deficit and its mean). Define d(x) = 1 -
  e^{-pi x^2} - e^{-pi/x^2} and Delta_p(a) = sum_{m in Z}
  d(e^{-a} p^m). Then Delta_p is exactly log p-periodic, maximal at
  a = 0 mod log p, and its period-mean satisfies

      mean(Delta_p) * log p = gamma + log pi   (certified 1.5e-36;
      proof: Frullani, int_R d(e^u) du = gamma + log pi).

  DEMAND: the theory's per-place trace defect (the failure of the
  smoothed self-dual count against the exact partition count) must
  BE Delta_p - in particular its mean must produce gamma + log pi
  with no explicit-formula input. [QQ-native-face.md, gate QQ7]
CERT 2 (the zero-charge ledger). Define the continuum charge of a
  defect as (point count) - (comb density) x (length removed). The
  certified ledger: band-shaped defects carry charge EXACTLY 0 and
  are absorbable by finite bookkeeping; the d = 1 hole carries
  charge EXACTLY -1 and is not (an atom cannot cancel a continuum).
  DEMAND: LS4's regularization (one continuum unit subtracted per
  place) must produce charge exactly -1 per place, not
  approximately. [TT-truncated-face.md sec 1.1; NN/PP distinguishers]
CERT 3 (the threading law). Certified: the per-place positivity
  problem is EXACTLY infeasible at every place, while the global
  aggregate (coupled through the product formula) is feasible; the
  per-place deficits do NOT add (two-place colimit deficit
  non-summable; finite failure box [0..3]^2 at T = {2,3} certified:
  Delta_box > Delta_2 + Delta_3). DEMAND: the self-dual unit must
  restrict to each place infeasibly and couple feasibly ONLY through
  the product formula - the trace must thread places, not pad them.
  [doc 36 sec 1 (RR's residue); QQ gate QQ8]
```

### 4.4 Evaluation criteria for an adopting expert

(a) Consistency of (iii) with (iv) is the open mathematics: whether
the {+-1}-pinning and a Gaussian fixed point can coexist with a
liquid-internal kernel is exactly what makes this a conjecture, not
a definition. (b) The Epstein guard (sec 5) is the vacuity test:
a construction whose trace coupling also computes for a
non-multiplicative lattice proves nothing about the demand side.
(c) The deliverable that would change the program's status: clause
(iii) alone, even without (iv), would already pin BB's normalization
torsor and convert kappa from comparison to measurement.

## 5. THE EPSTEIN KILL-TEST FOR LS4 (standing gate, restated for adoption)

MM's mandate (MM 4.3), now with a passed instance (XB5): any
constructed instance of the LS4 trace coupling must be run against
the Epstein form Q(x,y) = x^2 + 5y^2 BEFORE banking. REQUIRED death
profile: the theta/PD/Poisson layer SURVIVES (the formalism is
lattice-blind, and must be); the COUPLING THROUGH THE BANK is
UNDEFINABLE (not false - undefinable: the represented-value monoid
has no valuation: 36 = 4*9 = 6*6 with 4, 6, 9 irreducible, certified
exact); death occurs at effectivity, matching JJ AJ7's profile; DH
dies earlier (no carrier group at all, LS1). A COUPLING THAT
COMPUTES FOR EPSTEIN IS VACUOUS AND KILLS THE ROUTE regardless of
how much of R1-R3 has been built. XB5 certifies the T2 instance
passes; every future LS4 instance inherits this gate verbatim.

## 6. G-INT6 LEDGER

```text
input                          choices spent
Efimov Thm 0.2/4.18/6.1        cited verbatim from archived PDF
                               (transcription, 0 choices)
CS Complex.pdf 13.6/13.10/HRR  cited verbatim from archived PDF
Aut_top(R/Z) = {+-1}           cited theorem (FF FFG2 lineage)
Gaussian e^{-pi x^2}           THE one analytic import (JJ/QQ,
                               logged; in LS3 it is OUTPUT (iv),
                               never input)
Tate-curve model X_p           forced by MM Route A (the unique
                               compact complex shadow of T_p with
                               q-grading = the banked address)
fundamental domain Z_p x [0,1) calibration choice of representative
                               (any translate works; covolume is
                               choice-independent = product formula)
test Gaussians s in {1, 1/2}   exhibition device (BB GB1 reuse)
kappa = pi                     comparison/required-output ONLY
                               (LS3 clause (iv) + output line; F-a)
zeros                          NONE anywhere; freeze never triggered
```

## 7. HONEST LIMITS

- T1 is a NO-GO about sheaf-theoretic/localizing-invariant traces
  with the stated hypotheses; sec 1.3's complement N1-N5 is exactly
  what it does not rule out, and nothing here constructs any of it.
- T2 is a CALIBRATION, registered as such in advance: its value is
  contact (printed liquid theorems against banked objects) and the
  certified null, not new structure. The liquid-classical agreement
  is by GAGA/Serre for the compact curve; the witness computes the
  classical side exactly/numerically and the identification is the
  cited theorems' content, not a computation of liquid cohomology
  from scratch.
- T3's solenoid bookkeeping is finite-level exact + classical
  citations (Cech H^1 of the solenoid); no condensed-category
  computation is performed; "S_p exists as a condensed group" is
  printed-structure bookkeeping, and the claim is deliberately
  category-light (quotient of locally compact groups).
- The uniqueness clause in XB7b is certified on samples with the
  pivot Z[1/p] cap Z_p = Z checked at finite denominators; the
  general statement is classical and cited, not re-proved.
- LS3's consistency ((iii)+(iv) coexisting) is OPEN - posed, not
  evidenced; the gaseous-foundations dependency (MM sec 2(a)) is
  inherited by clause (i) and is outside the program's control.
- Nothing here touches the index/positivity demand (doc 21 sec 4);
  a proved LS3 supplies the symmetry layer only.
- No RH / zero-side input anywhere; the EF appears only inside the
  cited certificates' provenance (their docs), not in any derivation
  here.

## 8. HAND-OFF (for the lead)

```text
T1:  DONE, citable. Efimov 0.2/4.18/6.1 transcribed verbatim;
     Corollary XX.1: no sheaf-theoretic trace on Shv(R/(log p)Z)
     distinguishes p (two-layer proof: scaling homeomorphism +
     homotopy-type factorization, naturality included). Complement
     N1-N5 named exactly = B4's door: metrized coefficients, liquid
     module categories, equivariance-with-group-rigidity, kernel
     traces, non-Sp-linear bases.
T2:  DONE as registered: calibration, null confirmed certified
     (XB1-XB5): liquid trace layer constant-free and p-independent;
     comb reproduced through the q-grading (weight/spacing = 1,
     BB-r2 at liquid level); Epstein guard passed (coupling
     undefinable, theta alive). First contact of the in-print
     liquid formalism with banked objects: banked.
T3:  DONE, both registered predictions confirmed (XB6-XB8): R is
     fracture-INERT (no new corner in the square - mod-p
     invisibility is the same fact as FF's kappa-blindness); the
     ADDED corner is the cocompactness layer: S_p = (Q_p x R)/Z[1/p]
     compact connected, covolume 1 = product formula, torsion shadow
     = banked Prufer comb, connected layer = the deleted continuum.
     Three-row ladder: circle = blind; solenoid = place-addressed,
     scale-free; liquid module category = where scale must live.
LS3: POSED AT ADOPTION GRADE (sec 4): standalone conjecture,
     hypotheses + printed proof inputs + output (kappa = pi as
     theorem) + the three demand-side certificates (Delta_p mean =
     (gamma + log pi)/log p; zero-charge -1; threading law) +
     evaluation criteria. Communicable without program context.
GATE: the Epstein kill-test for LS4 restated as a standing gate
     (sec 5) with its first passed instance.
WITNESS: prime_xx_b1_liquid.py (XB1-XB8, ALL PASS, exit 0).
NEXT: B4 should start from sec 1.3's N3 (equivariant trace with the
     group rigidity datum) x N2 (liquid module category): the two
     complements that intersect LS3's home.
```
