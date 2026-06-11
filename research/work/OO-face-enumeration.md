# OO - Face enumeration: every reasonable alternative face/embedding for the index inequality, gated (doc 35 option 2, user-directed)

Status: fresh-context worker OO, 2026-06-10. Enumeration/gating only - NO
witnesses run; all numbers cited are banked. Required reading executed in
order: doc 35 (the N-c verdict + final gap spec), NN-graph-class-test.md IN
FULL, docs 33/34, LL-square-dual.md, HH-weil-restriction-fork.md,
I-c6-ku-square.md, W-monoid-frobenius.md, Z-u2-gluing.md,
DD-spectrum-realization.md, GG-global-cancellation.md; consulted for the
candidate set: doc 23 secs 5-6, N-cc-square-posing.md (dim_S, M1-M6).

## 0. The kill to evade, stated once

NN (certificate-grade, both registered sub-modes): under the FORCED lattice
dictionary [p^k] <-> depth-k comb class,

- the dual of every depth-1 class carries an EXACT continuum hole -1/u
  (Theta^dual = theta - 1/u, two routes, 4e-90); an inserted ATOM cannot
  cancel a CONTINUUM deficit; margin -> -e^{-a}/2, all p, all a;
- (p; 2) classes, p >= 5, fail RECURRENTLY: onset exactly at window entry
  a = 2 log p, period log p^2, negative-phase fraction 0.25 -> 0.38
  growing toward the d=1 limit; (11;2) at a = 4.96 certified -2.21e-3;
- the FE-transported cone interior fails 5/5 (~ -e^{-a}/2: the shadow
  deficit);
- the K2 pairing DOES NOT EXIST off the integer lattice (no per-lattice
  Poisson for real depth) - NN sec 1.4, a structural finding;
- the breakage is comb-determined, NOT zero-correlated (z < 3 frozen).

NN's honest limit: this kills the VERBATIM extension under the forced
lattice dictionary, not every conceivable embedding. A surviving face must
realize at least one of:

```text
E1  NATIVE DUALS: the pairing exists ON the face (no FE-transport).
    Known native-pairing carriers: Z's G / DD's Xbar (perfect residue
    pairing (j,m) <-> (1-j,-m), Lin block theorem-grade); TR/Witt/TC
    (fib(can - phi) in CycSp); CC's Pontryagin-Serre duality (curve
    level, S[+-1] only).
E2  ATOMS THAT ARE NOT DEPTH-1 LATTICE STEPS: the ku lcm-ladder's cells
    are GLOBAL (one cell per prime power q at admissible weights), not
    per-place; K(F_q)'s pi_{2w-1} = Z/(q^w - 1) GROW with w.
E3  STRUCTURAL RE-WEIGHTING that cancels the continuum hole: GG's
    survivor normalization (one continuum unit per place, FORCED by
    global existence, GG4); HH's Theta damping read as the MEASURE on
    classes (joint cancellation), not as the test class.
```

A second structural fact constrains everything: the hole -1/u lives ONLY
on depth-1 classes. The (p;2) breakage (the (N-c-full) mode) is NOT a
hole - it is a race failure (twist surplus ~ rho_T near 1 vs the dual
fine structure) at window-entry phases. Any E3 mechanism aimed at the
hole is a priori INERT on (p;2); a surviving face must answer BOTH
failure modes. This split is used in every gate below.

## 1. The candidate faces, each with (i) evasion mechanism, (ii) first
## computation, (iii) kill criterion, (iv) carrier guard, (v) cost

### F1. GG-survivor re-embedding (zero-mode subtraction as the chi normalization)

(i) E3-a. GG4 (witnessed exact): the global survivor trace exists ONLY
after subtracting one continuum unit per place - a FORCED normalization,
not a choice (it is the existence mechanism, GG3). Applied class-wise:
re-define the dual count of a class with depth-1 places by restoring the
continuum unit per depth-1 place, i.e. Theta^dual_GG(u) := Theta^dual(u)
+ n_1(D)/u. Design-stage observation (derivable from NN P1's closed form,
no run needed): at d = 1 this gives Theta^dual + 1/u = theta(u) EXACTLY -
the repaired dual is the self-dual Jacobi theta, and the margin becomes
AJ4's canonical positive margin. The k = 1 slice is repaired EXACTLY, by
a banked, globally-forced normalization - zero new choices.
(ii) First computation: a witness re-running NN's census with chi_GG;
decision set = NN's G4 family. The REAL decision cell is (11;2) at
a = 4.96 and the (p;2) period scans - where n_1(D) = 0 and the
subtraction is provably inert.
(iii) Kill criterion: (a) any certified negative on the (p;2) window-entry
phases (expected: UNCHANGED -2.21e-3 at (11;2), since the mechanism is
inert there - this is the registered prediction); (b) over-subtraction on
previously-holding mixed classes containing depth-1 places. NN-style
breakage map = same comb-periodic negatives at depth 2. If killed: the
verdict sharpens to "the hole is curable by GG's forced unit; the RACE is
not" - the gap spec's class/scale coupling confirmed from a second side.
(iv) Carrier guard: inherited intact (comb/valuation: LL7, NN G6 - the
construction is unformable off unique factorization). Formable.
(v) Cost: DAYS (banked machinery; one witness).

### F2. Theta-weighted aggregate face (HH's damping as the measure)

(i) E3-b. Stop demanding per-class positivity on cone generators; pose the
inequality on the Theta_p-WEIGHTED aggregates (the KMS-1/2 series as the
measure over ladder steps) and on the rung flow D_R. Positive banked
evidence: ALL 14 rung towers D_R hold (+0.05..+0.16); the per-place
aggregate sum_k p^{-k/2} m+(d_k) pits the k=1 deficit -e^{-a}/2 against
deep-step surpluses. HH's measurement says Weil positivity IS a joint
cancellation, never per-coordinate - per-class positivity was always a
STRONGER demand than RH-at-rung needs.
(ii) First computation, two parts, both cheap: (a) numeric: Theta-weighted
per-place and per-rung aggregates of NN's banked margins at matched rungs
and at the (p;2) window-entry phases; (b) STRUCTURAL (the decisive one, an
LP/conic hand computation): determine whether the unit-repaired inequality
on the aggregate family IMPLIES dual-cone membership (1,Theta) in K_R^* at
the rung - i.e. whether the breaking single-place (p;2) directions are
unavoidable extreme rays of HH's moment cone (PSD-Toeplitz image, H5a).
(iii) Kill criterion: (a) a certified negative aggregate at any rung/phase;
(b) the LP shows (p;2) steps are exposed/extreme in the admissible image
cone (then aggregate positivity cannot certify membership: face dies
structurally); (c) the aggregate statement reduces to verbatim Weil
positivity on the class (doc 16 level-1: no face gain - the test must
show the aggregate is computable from the comb side WITHOUT the EF).
(iv) Carrier guard: HH H6 verbatim (tower address + Lambda = -<d,d>;
DH unformable twice over). Formable.
(v) Cost: DAYS (numerics) + ~1 week (the conic argument).

### F3. H^1-reinterpretation on an enlarged lattice (the deficit as a genuine h^1)

(i) E1/E3 hybrid - NN's own named loophole ("a larger divisor lattice with
genuine H^1/K_sq classes"). On a curve RR is h^0 - h^1 = chi; the forced
dictionary set h^1 = 0 and read every deficit as FAILURE. If the
window-entry deficits are a genuine nonnegative count h^1(D) with its own
carrier, the index inequality holds AS STATED on the enlarged lattice and
NN's negatives become its h^1 spectrum. Suggestive banked shape: the d=1
deficit is e^{-a}/2 (1+o(1)) - a half-unit at the boundary, EF-boundary-
term flavored; deficits onset exactly at generator window entry (a
divisor-crossing event).
(ii) First computation: structure tests on the banked -m+ values: is
-m+ = log(1 + positive comb-structured series) with place-additivity over
mixed classes and monotone window-entry behavior? (Pure post-processing of
NN's frozen series + a small refinement witness.)
(iii) Kill criterion: deficits not count-shaped (sign-indefinite additivity,
non-monotone phase structure), or h^1 definable ONLY as max(0, -m+) - a
relabeling that spends an unbounded fit (G-INT6 kill: a face whose h^1 has
no independent construction is the gap object renamed).
(iv) Carrier guard: AT RISK - formable only if h^1 acquires a
carrier-consuming definition (comb/valuation input); a relabeled h^1 has
no carrier and fails R(v)-style fatality. This is the gate to watch.
(v) Cost: DAYS for the structure tests; the construction (if they pass) is
open-ended.

### F4. The ku/lcm face (true even/positive torsion + doc 23 secs 5-6 corrected Castelnuovo)

(i) E2, genuinely: |T_2w| = lcm(1..w+1)/(w(w+1)) - the cells are GLOBAL
(one per prime power q, sieve w mod q not in {0, q-1}), assembled inside
the homotopy theory by the fracture square; no per-place depth-1 step
exists to carry a hole. Three properties no other face has: positivity is
DEFINITIONAL (cardinality >= 1: L(w) = psi(w) + Lambda(w+1) - log w(w+1)
>= 0 is the program's "positivity by definition" demand realized at supply
level); the torsion pairs POSITIVELY (even degrees, filtration-2 parity -
the sign the index needs); the increment L(w) - L(w-1) = Lambda(w+1) -
log((w+1)/(w-1)) is EXACTLY the EF supply shape with the archimedean
density inside the cardinality with the right sign. The Lorentzian index
shape is certified on the geometric family {psi^{p^i}} (max-Gram lemma,
W secs 5.1-5.2; n-stable t-window containing 0 - doc 23's escape
repaired).
(ii) First computation - the CHEAP GATE, posed in I-doc sec 8 as C6': fix
the determinant scheme and compute the finite part of D_ku(s) at s = 0.
The banked catalogue already shows a SIMPLE POLE at s = 0, residue -1,
from the log(w+1) piece. The gate question: is that pole the SAME
one-continuum-unit obstruction (GG4's zero mode / LL's -1/u) in global
dress? Registered expectation: YES in shape (one archimedean log ladder
uncancelled) - but here the object ALSO contains psi(w), i.e. the
candidate counterweight is INTERNAL to the same cardinality, which is
exactly what every lattice face lacked.
(iii) Kill criterion: (a) the s = 0 finite part requires a scheme choice
that is a fit (the I-doc scheme obstruction unresolved: face not posable);
(b) NN-style breakage = the dual/index statement, once posed, carries an
uncancelled continuum term at the boundary weights w, w+1 (the -log w(w+1)
is the archimedean DEBIT: if the index inequality on this face localizes
to "psi(w) + Lambda(w+1) >= log w(w+1) with slack tracking tau" and the
slack is again e^{-a}/2-scale at entry phases, the kill transports);
(c) the full face needs the square-level dual that doc 19-20 prove absent
(properness wall) - the COMPLETION is walled even if the gate passes.
(iv) Carrier guard: the strongest in the corpus - categorical (no ring =>
no THH => no square; FGL-denominator arithmetic; I-doc G-INT3). Formable.
(v) Cost: ~1 WEEK for the C6' gate (flint zeros witness + scheme
bookkeeping); MONTHS for C6'' (the twisted-THH diagonal, the minimal
computable instance posed in I-doc sec 6); the duality completion is
spine-grade (external wall).

### F5. Native-pairing face on Z's G / DD's Xbar

(i) E1, the cleanest in principle: on G the duality is a STRUCTURE MAP -
perfect residue pairing (j, m) <-> (1-j, -m), unit slot pairing with
itself in the Lin block (the +1 counted once, INSIDE the pairing - the FE
on G is homogeneous by construction); spectrum realization Xbar exists
(DD.3); the scheme is FORCED c = 1/2 (ZG4, O's A1); the Lin-block duality
datum is UNIQUE (EE.1, no torsor). Nothing here is FE-transported.
(ii) First computation: transport test - under the forced c = 1/2 scheme
and the spent doc-19/20 dictionary, compute what G's native pairing
induces as the DUAL COUNT on the depth-1 class, and check against LL's
Theta^dual: is the hole -1/u ABSENT natively (the unit slot supplies it),
or does extracting real-valued magnitudes from the F_2/char-2 object
re-import the FE transport?
(iii) Kill criterion: (a) the induced dual count equals the FE-transported
one (hole intact: the native pairing is the K2 pairing in disguise - no
new face); (b) magnitudes require an insertion (G is scale-free, K1: the
archimedean size of h^0 cannot come from p = 2 alone - if the only bridge
is a logged magnitude import, G-INT6 demotes the face to a diagnosis);
(c) the global version re-imports GG's zero mode at assembly (registered
expectation: it does - GG4 says the scale/continuum datum is a relation
BETWEEN places, and G is one place).
(iv) Carrier guard: via Theorem S.1's ring (DD sec 7: no ring => no Tate
=> no tower => no Xbar). Formable.
(v) Cost: 1-2 WEEKS (scheme transport + a uniqueness lemma; mostly hand
work against banked objects).

### F6. TR/Witt/K(F_q) face (the Lefschetz fixed-point carrier)

(i) E1 + E2: TC = fib(can - phi) is a native pairing home (no bimodule, no
transport - W sec 1.2); K(F_q) = fib(psi^q - 1) has UNCONDITIONAL growing
atoms pi_{2w-1} = Z/(q^w - 1) = 1/|zeta(F_q, -w)|; the Euler factor IS the
regularized characteristic function of log Frobenius on the Tate
construction (Hesselholt Thm A, transcribed). This is the face where the
analogue of RH is a THEOREM (Weil) - maximal evasion plausibility in
shape.
(ii) First computation: none cheap that is new. The face's obstructions are
the BANKED blockers B1-B3 (W sec 1.6): p-complete technology blind to the
archimedean data; no linearization of phi over Z (no finite r); no iota
(no complex embedding of the square's prism coefficients) - and W3b: the
p-part of q^w - 1 is EMPTY (the pairing at p is blind to its own growth;
the growth is the Euler product over the OTHER places, i.e. the global
assembly is the whole content). The honest first step is a WATCH ITEM:
real-cyclotomic Gorenstein/BC duality (DD: not in the literature) or the
spherical delta-ring program ((A'') hunt) moving.
(iii) Kill criterion: already in hand as a wall, not a kill - B1-B3 are
provable in current technology. NN-style breakage, if the wall fell, would
be GG's zero mode at the place-assembly (the iota step is exactly the
archimedean move, W sec 1.5).
(iv) Carrier guard: ring/field/cyclotomic structure consumed everywhere
(W sec 7). Formable.
(v) Cost: BLOCKED-EXTERNAL (spine-grade, multi-year; not an option-2
candidate to spend on - record and park).

### F7. CC dim_S face (quantized integer dimensions)

(i) Nominally E1 (native Pontryagin-Serre duality, dualizing scale 1/4
pinned by RR-symmetry) - but the dimension is a QUANTIZED log-count with
resolution one base-unit (log 2 over S). NN's decision-grade deficits are
e^{-a}/2-scale - BELOW the quantization floor at every decision point.
(ii) First computation (optional, demonstrative only): evaluate the
dim_S-rounded margins on NN's breaking classes - registered expectation:
every deficit rounds to 0 and the inequality "holds" VACUOUSLY.
(iii) Kill criterion: already met twice over in banked results: (a) II's
design theorem (doc 33): an integer observable with bounded zero-response
against an O(1) quantization floor is structurally blind - h^0 must GROW,
and rounded dim_S margins carry no RH content (doc 13: the margins ARE the
content); (b) the square is UNFORMABLE in the published formalism (N-doc
M1-M6: no pi_2^T, no 2-adelic theory, no monoidal tolerance, no Kunneth,
base mismatch) and R(iii)-weak is lossy (sum (-1) ceil(log_2 k) is not
zeta'(0): a different invariant).
(iv) Carrier guard: formable at curve level (N-doc sec 5); the square
object does not exist to guard.
(v) Cost: zero to certify (cite); a demonstrative witness if wanted: days.
VERDICT: DEAD-ADJACENT - enumerate, cite, do not spend.

### F8. Anderson/rational-layer duality (noted for completeness)

FF's conditional finding (DD postscript): I^cont is not the
Poisson-exchange carrier; the scale needs a rational/Anderson layer.
An Anderson-dual face (I_Z instead of I_{Q/Z}; Greenlees-Meier precedent)
is the spectrum-level home where a CONTINUUM (rational) layer is native -
i.e. the only candidate whose unit is continuum-flavored BY CONSTRUCTION.
No computation is posable today (the real-cyclotomic Anderson statement
does not exist in the literature). Status: WATCH ITEM attached to F6's
external dependency; not a separate spend.

## 2. Ranking (evasion plausibility x cheapness; G-INT6 discipline)

Scores are judgment calls disclosed as such; cheapness is from banked cost
estimates; "choices" = new unbanked choices the face must spend (the
G-INT6 axis: fewer = better).

```text
rank  face                          evasion  plaus.  cost      choices  score
1     F1 GG zero-mode re-embed      E3-a     med     days      0 (forced) HIGH
      (exact repair at d=1 derivable from P1; decisive on (p;2) fast;
       either outcome full-value: survival OR second-side confirmation
       of the class/scale-coupled spec)
2     F2 Theta-weighted aggregate   E3-b     med     days-1wk  1 (logged: HIGH
      (all 14 D_R hold - the only positive census signal; the LP kill    aggregate
       is cheap and structural; main risk: collapses to level-1)         family)
3     F3 H^1 reinterpretation       E1/E3    med     days      0 for the MED-HIGH
      (cheap structure tests on frozen data; high relabeling risk,       tests
       carrier guard at risk - gate hard)
4     F4 ku/lcm + Castelnuovo       E2       high    1wk gate; 1 (det     MED
      (best structural fit in the corpus - global atoms, definitional    scheme -
       positivity, even/positive torsion, certified (1,n) - but the      the banked
       completion sits behind the properness wall; spend on the C6'      obstruction)
       gate only)
5     F5 native G/Xbar              E1       low-med 1-2wk     1 (magnitude MED-LOW
      (native homogeneous pairing is real; char-2 magnitude gap is       bridge)
       the registered killer; K1 says no scale at one place)
6     F6 TR/Witt/K(F_q)             E1+E2    high    blocked   external   PARK
      (shape-perfect, provably walled at B1-B3; growth lives at the
       other places = the global assembly IS the gap; watch item)
7     F7 CC dim_S                   (E1)     nil     0 (cite)  -          DEAD-ADJ
8     F8 Anderson layer             E1       unknown blocked   external   WATCH
```

Recommended spend order: F1 + F2 in one cycle (shared witness
infrastructure, both gate the SAME decision cell (p;2)/window-entry);
F3's structure tests ride along free (post-processing). Then F4's C6'
gate. F5 only if F1/F2 leave the E1 channel undecided. F6/F8 are parked
external watch items, F7 is cited dead-adjacent.

## 3. Provably dead already (cite; do not re-litigate)

```text
1  Verbatim lattice-dictionary face on graph classes - NN (N-c, both
   sub-modes, certificate-grade); doc 35.
2  Strict-family inequality as spine target - LL postscript + NN
   (small-place artifact; safe cells exactly p in {2,3}).
3  margin <-> tau identification - NN G5 (|log ratio| to 1.91,
   Spearman -0.499: no tracking).
4  K2-paired duals OFF the integer lattice - NN sec 1.4 (no per-lattice
   Poisson for real depth; the pairing does not exist there). Kills any
   real-cone re-embedding needing paired duals off-lattice.
5  Integer-signature observable face - II (doc 33 probe 2, verdict s-c:
   structurally blind by design theorem; bounded zero-amplitude vs
   quantization floor).
6  Bare Adams family Gram log|k-l| - doc 23 (R-c: not Lorentzian;
   window escapes linearly).
7  Invertible/p-adic Adams families - P's theorem (doc 23 sec 5): groups
   carry no degrees, ultrametric/Parisi not Lorentzian; degree growth
   provably cannot come from any invertible family.
8  Multiplicative psi^p on periodic K-theory - W sec 2.1 (one-line
   no-go: beta -> p beta is a non-unit).
9  Bimodule graph of the cyclotomic Frobenius - W sec 1.1 (undefinable,
   full stop; the twist sits in the sphere).
10 Plain BC self-duality of Xbar / U.2(a) as stated - DD.1/DD.4
   (Erdos-Kaplansky no-go); N1-b route refuted by EE.2.
11 Sector-N / chi_0 normalizations of the square dual - LL5 (doubly-
   exponential failure; -> 2 log rho).
12 zeta(0)-flavored branch-split regularizations - LL sec 0 (rejected
   at design time, F-a-adjacent).
13 Everything off the unique-factorization carrier (Epstein, DH) -
   LL7, NN G6, GG6, HH H6, W sec 7: unformable, not merely false.
14 CC dim_S SQUARE - N-doc M1-M6 (object not definable in the published
   formalism) + R(iii)-weak lossiness; the curve-level face is vacuous
   at decision scale (F7 above; II's theorem).
```

## 4. The exhaustion criterion

Option 2 (the face hunt) is EXHAUSTED, and the program moves to the
preprint (option 3: the certified equivalences + no-go map), when ALL of
the following verdicts are banked - each fail-closed, arb-certified at the
named decision points, carrier guards formable, zero fits:

```text
X1 (E3 closed):  F1's witness certifies the (p;2) window-entry negatives
   UNCHANGED under the forced GG normalization (the subtraction is inert
   at depth >= 2, as registered), AND F2 either (a) certifies a negative
   aggregate at some rung/phase, or (b) the conic computation shows the
   (p;2) directions are unavoidable extreme rays (aggregate positivity
   cannot certify membership), or (c) the aggregate face is shown
   EF-equivalent (level-1: no face gain).
X2 (E1 closed):  F5's transport test shows the native G/Xbar pairing
   either reproduces the FE-transported dual (hole intact) or requires a
   logged magnitude import (insertion - demoted); AND the canonical-
   completion uniqueness lemma is recorded: the ONLY homogeneous
   completion of the comb FE is the continuum unit itself (the gap
   object, not a face).
X3 (E2 closed):  F4's C6' gate returns either "scheme unfixable without a
   fit" or "the s = 0 obstruction is the same one-continuum-unit zero
   mode in global dress" (kill transports), with the completion wall
   (square duality, doc 19-20) re-confirmed as external; AND F6/F8 are
   recorded as BLOCKED-EXTERNAL at B1-B3 / missing real-cyclotomic
   duality (watch items, not open faces).
X4 (loophole closed):  F3's structure tests show the deficits are not
   count-shaped, or h^1 is definable only as max(0, -m+) (relabeling,
   G-INT6 kill).
```

If ANY of X1-X4 instead returns a SURVIVAL (a face where the inequality
holds on the full decision set including (11;2)-type cells and the
window-entry phases, with no unbanked choice spent), option 2 has
produced a new target and the spine inherits IT, not the strict-family
inequality.

Negative closure of X1-X4 would mean: every identified evasion channel
(E1, E2, E3, plus the H^1 loophole NN itself named) has either a
certified kill or a named external blocker of spine grade. The honest
residue would then be exactly doc 35's two roads: the LS3/LS4 spine with
the sharpened class/scale-coupled unit spec, and the publishable no-go
map - i.e. option 2 ends where doc 34 sec 2's conservation law said it
must: the coupled unit cannot be inserted, only derived.

## 5. Honest limits

- This is an enumeration, not a search proof: "every reasonable face" =
  every face constructible from the banked corpus plus the three evasion
  mechanisms NN's kill admits. A face outside the corpus (new carrier,
  new duality) is by definition not gated here; X3's watch items are the
  monitored entry points.
- Plausibility scores in sec 2 are judgment; the cheapness and choice
  counts are from banked costs and ledgers. No numerics were run; every
  cited number is from a banked, lead-rerun witness.
- F1's "exact repair at d=1" is read off NN P1's closed form by hand
  (theta = Theta^dual + 1/u at d=1); it is design-stage derivation, to be
  gated fail-closed by F1's witness, not a result of this doc.
- The (p;2)-vs-hole mode split (sec 0) is my structural reading of NN
  secs 3-4; the F1/F2 witnesses test it fail-closed (if the GG
  subtraction DOES move (p;2), the split is wrong and that is itself
  reportable).
- F6's "shape-perfect" assessment leans on transcribed literature
  (Hesselholt Thm A etc.) at the grade W-doc assigned it.
