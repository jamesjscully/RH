# EE - DD.4 on the Lin block (THEOREM, shift pinned), the g2 Borel computation (executed: REFUTES N1-b), and the torsor (Lin-trivial, unreduced elsewhere)

Status: fresh-context worker EE, 2026-06-10. Doc 30 ranked front 1.
Required reading executed in order: doc 30, DD-spectrum-realization.md
IN FULL, Z-u2-gluing.md, S-thr-p2.md (Theorem S.1 + square); refs
re-read at load-bearing points: dgi2006.txt (Gorenstein/Matlis
framework, def at "Hom_R(k,R) = Sigma^a k"), greenlees-meier2017.txt
(Def 1.2 Gorenstein duality of shift b; C_2-equivariant Anderson
self-duality precedents KR [HS14], tmf_1(3) [HM16]; GM Mem AMS 543 in
their bibliography), QS21 verbatim (Props 6.13/6.14, Def 6.8, Rem 6.23,
Thm 6.20-6.22 region, formula (3.1), Appendix A: Thm A.2 [HNS], Props
A.3/A.4/A.5, Prop A.6, Lemma A.7 - the A.6/A.7 statements are NEW
transcriptions beyond DD's), DMPR via extraction (Thm 5.18 verbatim at
lines 314/4837-4841). Inherited witness rerun before any new work:
prime_int_dd_bc_dual.py ALL PASS (DDG1-DDG7, exit 0).

Witness (NEW): scripts/numerics/witness/prime_int_ee_dd4_lin.py
(gates EEG1-EEG8, pre-registered fail-closed readings in the docstring,
written before the first run; ALL PASS first run, exit 0; exact F_2 /
integer arithmetic, no numerics).

HEADLINE (one theorem, one executed computation with a REFUTATION, one
fail-closed torsor verdict):

1. THEOREM EE.1: the Lin-block clause of Conjecture DD.4 is a THEOREM
   in Mod_Y, with the duality datum UNIQUE (not just existing) and the
   shift pinned: Y ~ Sigma^1 I(Y) covering exactly the m = 0 component
   of Z's K2 pairing ((j,0) -> (1-j,0); degree-sum 1, weight-sum 0).
   FIX TO DD.4's STATEMENT: the display must read
   Xbar ~ Sigma I^cont(Xbar), NOT I^cont(Xbar) ~ Sigma Xbar - DD's
   own gluing maps (X' = colim Sigma I(X_N), aug' = colim Sigma
   I(unit_N), "Sigma I(Y) = Y") already use the first convention; the
   display is off by Sigma^2 against the construction. The discrepancy
   is invisible in Mod_Y (t-periodicity) - the invariant content of
   the pin is the bigraded slot statement: the duality pairs (j,m)
   with (1-j,-m), dualizing character (degree, weight) = (1, 0), the
   residue line t^{-1} = H-hat^{-1}(C_2; F_2).
2. THEOREM EE.2 (g2 executed; fail-closed full value): the finite
   Borel computation REFUTES Lemma N1-b as DD posed it. The image of
   QS21's class u under forget-then-can (+ Thom collapse) in
   pi_{-2} THR(F_2)^{tC_2} = t^2 F_2[[z]] is 0 - not t^2 (1-unit).
   Mechanism: pi^{C2}_{(-2,-1)} THR(F_2) = 0 (exact cone enumeration
   from DMPR 5.18 + HK01/QS21 6.13), so ANY composite that forgets the
   parametrized circle kills u by naturality, before the Tate is even
   reached. Two independent corroborations (multiplicative relation,
   Stiefel-Whitney bottom quotient) agree. The correct vehicle for the
   t-shadow is the GEOMETRIC route (QS21 A.2/A.5-A.7), re-posed
   precisely in sec 4.
3. TORSOR (g3): trivial ON the Lin block (EE.1's uniqueness - there is
   literally one duality datum at m = 0), but this does NOT reduce the
   torsor: every 1-unit (1+z)^k restricts to the identity at m = 0 (the
   augmentation), so the torsor's support is exactly weights >= 1 and
   the Lin clause was never where it lived. New positive fact: leading
   z-coefficients are torsor-INVARIANT, so the re-posed N1-b has a
   well-defined, torsor-free leading-term question. And EE.2 removes
   the N1-b leg of DD's one-torsor reading as stated (no surviving
   unit to pin on the Borel route): the identification must be carried
   by the kappa-nullity and (1+z)-defect legs alone.

## 1. Registration discipline (disclosed)

The witness docstring (R-EEG1..R-EEG8) was written before the first
run; ALL PASS first run; no gate amended. The readings encode
design-stage hand derivations (this is disclosed, as in Z/DD): in
particular the refutation EEG4 was found by hand (the cone enumeration
plus the naturality argument of sec 3.1) and REGISTERED as the
expected outcome, with the explicit fail-closed clause that any
nonzero slot found would resurrect N1-b and falsify this doc.

## 2. Theorem EE.1: the Lin-block clause of DD.4, proved and pinned

Conventions as in DD sec 1: Y = (HF_2)^{tC_2}, pi_* Y = F_2[t^{+-1}],
|t| = -1 (S.1 sec 2; Greenlees-May, Mem AMS 543 - the Tate SS for
C_2 collapses to H-hat^*(C_2; F_2)); I = the 2-primary Brown-Comenetz
dual, pi_j I(M) = Hom(pi_{-j} M, Q/Z) exactly (Q/Z injective), which
for our F_2-homotopy objects is the F_2-linear dual.

THEOREM EE.1. (a) Let res: pi_1 Y -> F_2 be the t^{-1}-coefficient
(an isomorphism; t^{-1} is the unique nonzero class of
H-hat^{-1}(C_2; F_2)). By Brown-Comenetz representability
([W, Sigma I_{Q/Z}] = Hom(pi_1 W, Q/Z)) res is represented by a map
r: Y -> Sigma I_{Q/Z}, and the adjoint of r o mu : Y ^ Y -> Sigma
I_{Q/Z} is a Y-module map

    lambda : Y -> Sigma I(Y).

(b) lambda is an equivalence: on pi_* it induces lambda(t^a) =
(t^b |-> res(t^{a+b})), nonzero in every degree between 1-dimensional
F_2-spaces. The induced pairing is <t^a, t^b> = delta_{a+b,-1}:
perfect, Gram = the permutation j <-> 1-j - EXACTLY the Lin-block
(m = 0) component of Z's K2 pairing (ZG3/DDG6), i.e. the restriction
of the G-involution (j,m) -> (1-j,-m) to m = 0. [EEG1]
(c) UNIQUENESS. Y-module maps Y -> Sigma I(Y) are classified by
pi_0 Sigma I(Y) = Hom(pi_1 Y, F_2) = F_2: there is exactly ONE nonzero
map, namely lambda, and it is an equivalence. (This re-derives
Aut_{Mod_Y}(Y) = F_2^x = 1 from the dual side.) [EEG3]
(d) SHIFT PIN. For every d there is likewise a unique nonzero
Y-module map Y -> Sigma^d I(Y), and it is an equivalence (t
trivializes integer suspensions): the shift is NOT pinned by Mod_Y
structure. What pins it is the induced pairing: degree-sum d
reproduces Z's Lin block iff d = 1 [EEG2]. The invariant (home-
independent) form of the pin: the duality pairs slot (j,m) with
(1-j,-m); the dualizing character is (1,0), the residue line. In the
suspension notation DD.4 must be written

    Xbar ~ Sigma I^cont(Xbar)    (equivalently I^cont(Xbar) ~
                                  Sigma^{-1} Xbar),

matching DD's own construction (X' = colim Sigma I(X_N); Sigma I(Y) =
Y; aug' = colim Sigma I(unit_N)). DD's display "I^cont(Xbar) ~ Sigma
Xbar" is off by Sigma^2 against these - harmless in Mod_Y, but the
statement should be corrected before it is transplanted to any home
where the t-trivialization is not ambient.
(e) EQUIVARIANCE (cited, not re-proved): the genuine C_2-equivariant
upgrade of this self-duality is Greenlees-May (Mem AMS 543; the one
U.2(b) clause in the literature, per Z sec 8 / DD conventions). The
Mod_Y-level proof above is self-contained and is what the K2 pairing
needs; classical corroboration: cup-product duality of Tate cohomology
of finite groups (Cartan-Eilenberg Ch. XII; here verified directly
from the ring F_2[t^{+-1}]). The Gorenstein reading: lambda says
exactly that Y -> 0... more usefully, that the "ring" F_2[t^{+-1}] is
self-dual with shift 1 - the degree-0 instance of the DGI shape
Hom_R(k, R) ~ Sigma^a k (dgi2006, Gorenstein definition) and of
Greenlees-Meier Def 1.2 (Gorenstein duality of shift b), whose
C_2-equivariant instances (KR, tmf_1(3)) are the archived precedent.

VERDICT: the Lin-block clause of Conjecture DD.4 - "restricting on the
gluing locus to the Greenlees-May Lin duality" - is a THEOREM, with
uniqueness, and DD.4's shift is now pinned. What remains conjectural
in DD.4 is unchanged but sharper: the one-object functoriality (the
pro-ind home) and the branch-exchange clause; the gluing-locus clause
is discharged.

## 3. Theorem EE.2: the g2 computation, executed - N1-b is FALSE as posed

DD's Lemma N1-b claimed: under THR(F_2)^{hC_2 S^1} -> THR(F_2)^{hC_2}
-> THR(F_2)^{tC_2} (forget the parametrized circle, then can), plus
mod-2 Thom collapse, u |-> t^2 . (1-unit of F_2[[z]]). DD registered
the expected output "u |-> t^2 + O(z)". The computation gives 0.

### 3.1 The kill (exact, finite)

THEOREM EE.2. pi^{C2}_{(-2,-1)} THR(F_2) = 0. Consequently the image
of u in pi_{-2} THR(F_2)^{tC_2} = t^2 F_2[[z]] under DD's composite
is 0.

PROOF. (i) DMPR Thm 5.18: pi_{**} THR(F_2) = (HF_2)_{**}[x~],
|x~| = (2,1). (ii) HK01 Prop 6.2 / QS21 Prop 6.13: (HF_2)_{**} =
F_2[tau, rho] (+) negative cone {theta tau^{-a} rho^{-b}}, with
|tau| = (0,-1), |rho| = (-1,-1), |theta| = (0,2). A class in bidegree
(-2,-1) - k(2,1) = (-2-2k, -1-k), k >= 0, would need: positive cone
b = 2+2k, a = -1-k < 0 (none); negative cone first coordinate
b >= 0 != -2-2k < 0 (none). Exhaustive enumeration: EEG4. (iii) The
forget map is a map of C_2-spectra TCR^-(F_2) -> THR(F_2) (the unit of
the parametrized fixed points); u in pi^{C2}_{(-2,-1)} TCR^-(F_2) maps
to pi^{C2}_{(-2,-1)} THR(F_2) = 0. Every further stage of the
composite (genuine-to-Borel, can, Thom collapse) is a natural functor
or natural transformation applied AFTER the forget; by naturality the
image of u is the image of 0. (Both orders of "forget" and
"Borel-ize" agree, again by naturality.) QED.

Meanwhile the SOURCE slot is not degenerate: pi^{C2}_{(-2,-1)} of
(HF_2)^{hC2 S^1} = (+)_i Sigma^{-2i,-i} HF_2 (QS21 Prop 6.14) is F_2,
contributed exactly by the i = 1 cell [EEG4]: u exists, is the unique
nonzero class in its bidegree at the bottom of the x-adic filtration
(QS21 Def 6.8), and dies because of where it lands, not where it
lives. The contrast class x~ (bidegree (2,1)) survives.

### 3.2 Two independent corroborations

(a) MULTIPLICATIVE (uses g1-grade input, so corroboration only): QS21
Thm 6.20-6.22 region establishes "2 is detected by ux" in
pi^{C2} TCR^-(F_2); (6.8a) as groups makes the bidegree-(0,0) slot
Z_2{1}, so xu = 2 eps + (x-adic filtration >= 2), eps a 2-adic unit.
The forget-then-can composite is a map of E_infty-rings; the target
pi_* THR(F_2)^{tC_2} = F_2[[z]][t^{+-1}] is a char-2 DOMAIN (S.1) and
x |-> x . (1-unit) = z t^{-2} (unit) != 0 (S.1's square: fix -> hfix
sends xbar to x mod higher filtration; hfix -> Tate injective). So
image(u) . (z . unit) = image(2) + image(filtration >= 2) lies in
z^2 F_2[[z]]: the constant term of image(u) dies [EEG5(ii)]; under the
full multiplicative reading of Rem 6.23 (xu = 2 exactly, QS's "finer
analysis") image(u) . image(x) = 0 forces image(u) = 0 outright
[EEG5(i)]; and the self-consistency valuation inequality (the
correction T lies in the (x^k u^k, k >= 2)-ideal, so val(zf) = 1 + v
>= 2 + 2v) has no solution [EEG5(iii)]. The real refinement of
Nikolaus-Scholze's uv = p relation thus behaves OPPOSITELY at the
Weyl C_2: the reflection Tate is x-COMPLETE (z-adic), not x-local -
it kills the negative-degree class and keeps the positive one
(non-invertibly), where the dihedral Cp-Tate does the reverse.
(b) BOTTOM QUOTIENT / STIEFEL-WHITNEY (elementary, no g1): mod z the
composite is the Borel restriction along the reflection C_2 < O(2)
(Borel construction of B_{C2}S^1 = CP^infty with conjugation is
BO(2)). u's Borel shadow lies in H^2(BO(2); F_2) = F_2{w_1^2, w_2}
over the generator of H^2(BS^1); EE.2 + naturality pin it to pure w_2
(byproduct: the HK01-splitting ambiguity w_2 + a w_1^2 is resolved,
a = 0); and w_2(taut_2)|_{C_2} = w_1(1) w_1(sign) = 0 [EEG6].
Constant term 0, again.

### 3.3 What N1 looks like after EE.2

```text
N1-a (res(u) = v . unit in TP(F_2)): UNTOUCHED. Still needs g1
     (Rem 6.23 multiplicativity). EE.2 does not bear on it: v lives in
     the S^1-Tate, which does not factor through forgetting S^1.
N1-b: REFUTED as posed. The Borel/Thom t^2-slot (integer degree -2)
     carries the mod-2 shadow of the v-slot, and that shadow is 0.
     DD's own bookkeeping already said the GEOMETRIC shadow lands in
     degree s - w = -1 (the t-slot); the Borel collapse (degree s =
     -2) was the v-slot read twice. One class, two shadows survives -
     but the second shadow is geometric, not Borel.
N1-b' (RE-POSED, precise): QS21 A.5-A.7 supply the geometric carrier:
     pi_* THR(F_2)^{phiC2 h mu2} = F_2[w, y] (+) (transfer classes),
     |y| = -1, |w| = 2, w = w_1 w_2; Tate: F_2[w, y^{+-1}] (A.6); can:
     y |-> y, w |-> w, transfer classes |-> 0 (A.7). The dihedral-
     geometric line F_2[y^{+-1}] is degree-matched to the Lin line
     (|y| = |t| = -1) and S.1's Phi -> Tate dictionary sends
     w = w_1 w_2 |-> t^{-1} . tx = x (degree 2, weight 1) [EEG8].
     OWED STATEMENT: under HNS Thm A.2's fiber formula, the comparison
     of the mu2-geometric line y with the Weyl-Tate line t - "two Tate
     constructions" in QS21's own sense. Its leading coefficient is
     torsor-invariant (sec 5), hence well-posed. NOT proved here.
g1:  unchanged in content; after EE.2 it is no longer blocking g2
     (g2 is ANSWERED) - it blocks only N1-a's "up to unit" and any
     multiplicative use of (6.8a/b).
```

## 4. The torsor (g3) after EE.1 + EE.2

(i) ON the Lin block the torsor is TRIVIAL, as a theorem: EE.1(c)
says the set of duality data is a singleton; there is nothing to
normalize at m = 0. [EEG3]
(ii) But the Lin clause does NOT reduce the torsor where it matters:
the torsor acts through 1-units (1+z)^k (DDG7b orbit; Z's kappa,
nullity 43 in truncation), and every 1-unit restricts to the identity
on the m = 0 slot (augmentation = 1). Support of the torsor = weights
>= 1, exactly. FAIL-CLOSED VERDICT: not reduced by the Lin block; the
duality "pins the unit there" only in the empty sense that there was
never a choice there. [EEG7]
(iii) Positive yield: leading z-coefficients of nonzero classes are
torsor-INVARIANT ((1+z)^k preserves valuation and leading term)
[EEG7]. So the re-posed N1-b' has a torsor-free leading-coefficient
question, and EE.2's "0" is itself torsor-independent.
(iv) The one-torsor reading (DD sec 4.1): the N1-leg as stated ("the
1-unit in N1-b is defined up to the shear orbit") is now VACUOUS -
there is no surviving unit on the Borel route. The identification
must be restated on the kappa-nullity and (1+z)-defect legs (which
stand, DDG7 re-run PASS), plus the re-posed N1-b' unit if/when it is
nonzero. The dlog(1+z)-normalization remains the candidate pinning.

## 5. Honest limits

- EE.1 is a Mod_Y (Borel-level) theorem; the genuine C_2-equivariant
  clause is cited (Greenlees-May Mem AMS 543, not archived as txt -
  cited via S.1 sec 2's verified collapse + Z sec 8; the memoir's
  theorem number is NOT independently verified here, flagged).
  The O(2)-structure (U.2(b) proper) is untouched.
- EE.1 pins the shift only up to the ambient t-trivialization; the
  invariant content is the (1,0) dualizing character. Any home for
  DD.4 in which t does not act invertibly would need the Sigma^2
  bookkeeping redone (none of the candidate homes has this issue).
- EE.2 rides on DMPR 5.18 + HK01 6.13 (published) and naturality only;
  it does NOT ride on S.1. The corroborating route (a) rides on S.1
  and on the detection reading of QS21 6.20-6.22 ("2 detected by ux"),
  transcribed but not re-derived. If DD's composite was intended to
  NOT factor through the S^1-forgetful unit map (no such reading is
  visible in N1-b's wording), the refutation would need revisiting;
  the geometric re-pose N1-b' is exactly the repair for that
  eventuality too.
- N1-b' is POSED, not proved: the y-vs-t comparison needs HNS Thm A.2
  (attributed-forthcoming) made precise on THR(F_2), which is beyond
  the archived extractions.
- The bidegree-(0,0) sparsity used in 3.2(a) ((6.8a) gives Z_2{1})
  is read off the displayed group; negative-cone contributions of
  HZ2_{**} in bidegrees (-2m,-m) were checked for HF_2-patterns only;
  this is one reason route (a) is corroboration, not the proof.
- Carrier guard (K5): every object here is built from S.1's ring /
  DMPR's splitting / HK01's cones - no ring => no tower => no Y, no
  Xbar; DH/Epstein die at X_0 as before. No RH/zero-side input
  anywhere; no continuation of zeta is seen (the F-a guard inherited:
  divided powers still refuse F_2((z))).

## 6. G-INT6 ledger

- Inputs spent: Theorem S.1 (+ caveats, inherited; routes (a)/EEG8
  only); DMPR Thm 5.18; HK01 Prop 6.2 (= QS21 6.13); QS21 Props
  6.14/A.3-A.7, Def 6.8, Rem 6.23 (detection reading), Thm A.2
  (attributed-forthcoming; used only in the POSED N1-b'); BC
  representability + Q/Z injectivity (theorem); Greenlees-May
  (cited); DGI/Greenlees-Meier (framing only, no statement spent).
- Zero free choices: lambda is forced (unique nonzero Y-module map);
  res is canonical (t^{-1} the unique nonzero class of H-hat^1); the
  refutation EE.2 has no choices at all.
- Non-unique data: none introduced; the inherited kappa/1-unit torsor
  is analyzed (sec 4), not extended.
- Registration: EEG1-EEG8 written before first run; ALL PASS first
  run; no gate amended. Inherited DD witness rerun PASS before work.

## 7. Hand-off (for the lead)

```text
LIN BLOCK:  THEOREM (EE.1): Y ~ Sigma I(Y), unique datum, induces
            exactly Z's K2 Lin block (j,0) -> (1-j,0).  DD.4's clause
            discharged; statement to be amended to
            Xbar ~ Sigma I^cont(Xbar) (dualizing character (1,0)).
g2:         EXECUTED, answer 0: N1-b REFUTED (EE.2; finite cone
            enumeration + naturality; two corroborating routes).
            The reflection Tate is x-complete, not x-local: it kills
            u and keeps x - opposite to the dihedral Cp-Tate.
N1 NOW:     g1 unchanged (blocks N1-a only); g2 CLOSED (negatively);
            g3's N1-leg vacuous.  New owed item N1-b': compare the
            geometric line y (QS21 A.5-A.7, can(y) = y) with the Lin
            line t under HNS A.2 - degree/weight slots check out
            (EEG8), leading coefficient torsor-free.
TORSOR:     trivial on Lin (theorem, not normalization); support =
            weights >= 1; NOT reduced; leading coefficients are
            torsor-invariants (usable).  dlog(1+z) still the pinning
            candidate.
DD.4 LEFT:  the pro-ind home + branch exchange (now with the gluing
            clause proved and the shift fixed); ranked next per DD:
            solid/condensed F_2[[z]]-transcription of DGI.
```
