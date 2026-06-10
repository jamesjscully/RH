# U - Fork F1 run against the p = 2 Tate square: the residual Weyl finally ACTS at 2 - and it SHEARS the weight disk instead of negating the ladder. F1 resolves NEGATIVE for the THR carrier; the lambda^{1/2} kill-test is PASSED (t is the double-cover headroom); the only surviving carrier class is the duality layer (C5'''), now with an exact interface

Status: fresh-context worker U, 2026-06-10 (relaunch; the prior attempt
left no artifacts). Required reading executed in order: doc 24 (as
amended - forcing form of H-r3, fork F1), doc 25, doc 26,
O-hr3-formulation.md IN FULL (probes 4.7, Prop A6, obstructions
O-1/O-2/O-3), S-thr-p2.md IN FULL (Theorem S.1, the complete Tate
square with maps, KMS-1/2 per weight, pi_0 = F_2[[z]]). Refs re-read at
the load-bearing points: quigley-shah2021 (txt + Appendix A region of
the archived extraction: Props 6.13, 6.14, A.3, A.4, A.5, A.6 read
verbatim), dotto-moi-patchkoria-reeh2017 (Cor 5.19, Cor 5.20,
Prop 5.22 WITH PROOF, proof of Thm 5.18 - read verbatim from the
extraction), hahn-wilson2019 (not load-bearing here; descent picture
only via the S-doc).

Witness (NEW, ALL PASS, exit-code gated):
scripts/numerics/witness/prime_int_u_f1_probes.py (gates G0-G6,
pre-registered fail-closed readings R-G0..R-G6 in the docstring; one
registered reading amended post-run for an even-N truncation artifact,
recorded verbatim in the docstring and in sec 5 below - the
mathematical content of that gate passed unmodified on the first run).

HEADLINE (three verdicts, one new computed structure):

1. PROBE 1 NEGATIVE - BUT NOT EMPTY. No structure map in S's square
   inverts degree: t -> t^{-1} is "merely an algebra symmetry"
   (ungraded ring involution; not graded; not realizable by any
   spectrum-level self-map; weightwise realizable only as a duality).
   The genuinely NEW finding: combining QS21 Props A.3/A.4
   (theorem-grade: the residual Weyl mu_2 of O(2) swaps the two tensor
   factors of Phi^{C_2}THR(F_2)) with S's Tate square FORCES, by exact
   valuation bookkeeping, the first nontrivial residual-Weyl action on
   a nonvanishing reflection Tate:

       phi: t -> t(1+z)^{-1},   z -> z(1+z)^{-1} = z + c,
       c := z^2/(1+z)  invariant   (witness G2, exact)

   - an Artin-Schreier-shaped unipotent SHEAR of the weight disk,
   degree-preserving, IDENTITY on the Lin line (z = 0). It is not
   negation, and on the weight-0 / Spec F_2 layer where L-hom is posed
   it is invisible: obstruction O-1's vacuity propagates to p = 2.
   Byproduct: Phi(x~) = w_1 + w_2 (the swap-invariant vector) is
   FORCED, and the weight disk is a wildly ramified Z/2 double cover
   of its Weyl-invariant disk F_2[[c]] (witness G3).

2. PROBE 2 / lambda^{1/2} KILL-TEST: PASSED, the first carrier to
   survive it. t^2 = z/x occupies exactly the degree -2, weight-0
   v-slot, so t is a canonical square root of the VERTICAL periodicity
   = an index-2 refinement of the character lattice = precisely O Prop
   A6's double cover of the orbit circle (witness G4). t supplies NO
   weight/eigenvalue square root (no z^{1/2}); the missing
   identifications (N1), (N2) are stated precisely in sec 3. Necessary
   condition met; supply still absent.

3. PROBE 3 / F1 VERDICT: NEGATIVE FOR THE THR CARRIER, stated plainly
   per the doc-24 risk clause. Negation-as-duality exists at EVERY
   finite weight truncation (perfect residue pairing, weight flip
   m <-> N-m) and dies on S's completed object: the z-adic completion
   - the very "duality completion at 2" of S-r5 - is exactly what
   breaks s -> -s (witness G6). The full Tate is NOT self-dual
   (disk/co-disk); the unique self-dual locus is the weightless Lin
   line. Of doc 24's two escape routes ("rho-graded parametrized layer
   or a duality layer"), the first is now CLOSED (the rho/Weyl layer
   acts - by the shear - and does not negate); the duality layer /
   C5''' is the only remaining carrier class, and it inherits an exact
   interface spec (Conjecture U.2, sec 4.3).

Guards: fail-closed throughout; no RH/zero-side input (all carriers are
finite-place shadows; purity warning of O 4.5 never triggered - all
analysis at weight-centered ladders). G-INT6 ledger in sec 5.

## 0. Objects on the table (conventions pinned)

S's Tate ring (Theorem S.1, ring caveat inherited):

    R := pi_* THR(F_2)^{tC_2} = F_2[[z]][t^{+-1}],
    |t| = -1, |z| = 0, z = t^2 x, x = Bokstedt image (|x| = 2),
    weight(z) = weight(x) = 1, weight(t) = 0;  pi_j R = t^{-j} F_2[[z]].

S's square maps used: fix -> Phi (xbar -> w_1w_2, y -> w_2); Phi ->
Tate (w_1 -> t^{-1}, w_2 -> tx); hfix -> Tate (t-nonnegative
inclusion); transfer orbits -> fix is ZERO. Determinant layer (O 1.1):
DetIn(Spec F_q) = (C[v^{+-1}], Theta), ladder negation N: (V, Theta) ->
(V, -Theta) covering s -> -s; on the reflection side, per weight n the
full t-line is the vertical ladder, so N restricted to S's objects =
DEGREE INVERSION (t -> t^{-1} per weight) plus weight inversion
(n -> -n) for the off-center part. Doc-19/20 dictionary throughout
(weight n <-> 2^{-ns} supply; degree periodicity <-> vertical lattice).

Residual Weyl bookkeeping (group theory, pinned): N_{O(2)}(<sigma>) =
{1, lambda_pi, sigma, lambda_pi sigma}, so W_{O(2)}(C_2) = C_2
generated by the CENTRAL rotation lambda_pi. Two consequences used
below: (i) lambda_pi acts on every corner of S's square by ring maps
commuting with all structure maps; (ii) lambda_pi conjugates rotations
TRIVIALLY (it is central) - the element of O(2) that inverts the
rotation flow is sigma itself, which the reflection-Tate construction
CONSUMES. The inversion is spent before the Tate corner exists.

## 1. Pre-registered readings

Registered in the witness docstring (R-G0..R-G6, fail criteria
included) BEFORE the first run; verdict-level readings registered here
in the same form:

```text
U-r1 (probe 1): NO structure map or automorphism of S's square inverts
     degree; the residual Weyl action exists, is degree-preserving,
     and is trivial on the Lin line. Expected verdict: NEGATIVE for
     negation supply. FAIL: any degree-inverting graded automorphism,
     or a valuation-consistent swap forcing degree mixing.
U-r2 (kill-test): t passes A6's necessary condition (period-1
     invertible class = index-2 vertical refinement); t supplies no
     weight square root; verdict NOT KILLED, with identifications
     (N1)/(N2) still owed. FAIL: t^2 not in the v-slot, or a
     half-weight element exists.
U-r3 (verdict): F1 NEGATIVE for the THR carrier; remaining carrier
     class duality layer / C5''' with the disk/co-disk interface.
     FAIL: any probe yields a spectrum-level negation supply.
```

All three resolved AS REGISTERED (witness ALL PASS; the single
amendment - G3's even-N truncation artifact - is bookkeeping, recorded
in sec 5).

## 2. PROBE 1 (O's rank 1): structure maps and the residual Weyl

### 2.1 O's statement, transcribed verbatim (O-doc 4.7, item 1)

    "F1 at p odd, RO(C_2)-graded: compute the C_2-twisted automorphism
    group of TPR(F_p) over the parametrized sphere and check whether
    the orbit-circle reflection is realized with a nontrivial shadow on
    the (V, Theta) groupoid (the M-doc's route-(a) Borel computation is
    the place to start; the answer at pi_* is "commutes", so the
    content, if any, is in the rho-graded extensions / k-invariants)."

Adaptation (per doc 25 sec 3 / doc 26 front 2): run it at p = 2 against
S's square - the automorphism/structure-map inventory of
THR(F_2)^{tC_2}, where for the first time the reflection corner is
nonzero and the residual Weyl has something to act on.

### 2.2 Rigidity: nothing graded inverts t (theorem-grade) [G1]

The degree-(-1) component of R is t.F_2[[z]] (the only monomials
t^a z^b of degree -a = -1 have a = 1). Hence EVERY graded ring
automorphism sends t -> t.(unit of F_2[[z]]) - no graded automorphism,
of whatever geometric origin, can send t to t^{-1} (degree +1). The
candidate involution

    iota: t -> t^{-1}, z -> z   (hence x = t^{-2}z -> t^2 z)

IS a well-defined ring involution of the UNGRADED ring (witness G1) -
this answers the task's load-bearing question: t -> t^{-1} is MERELY AN
ALGEBRA SYMMETRY. A spectrum-level self-map induces a degree-preserving
map on homotopy, so iota is not realized by any equivariant (or even
plain) self-equivalence; the only spectrum-level constructions that
invert degree are DUALITIES - taken up in sec 4. Inventory of S's
structure maps against degree inversion: can (selects the t-nonnegative
half - breaks the symmetry, does not flip it); Phi -> Tate
(degree-preserving, injective); t-periodicity (a shift, not an
inversion); the z-disk (z is not invertible: weight inversion has no
home); transfer (zero). NONE implements w -> -w or t -> t^{-1}.

### 2.3 The residual Weyl at the Tate corner: the forced shear [G0, G2]

New theorem-grade inputs (verbatim from the QS21 extraction, Appendix
A; their mu_2 is the residual Weyl rotation, witness their proof line):

    [QS21 Prop A.3] "The mu_2-action on THR(R)^{phiC2} ~= R^{phiC2}
    (x)_{R^e} R^{phiC2} is given by swapping factors." Proof: "the
    residual mu_2-action is determined by the rotation action of mu_2
    on S^sigma that swaps the points of S^0 = {+-1}."
    [QS21 Prop A.4] "The residual mu_2-action on
    pi_* THR(HF_2)^{phiC2} ~= F_2[w_1, w_2] swaps w_1 and w_2."
    (Their w_1, w_2 are the two Kunneth/tensor classes of DMPR
    Prop 5.22's formula Phi^{C_2}HF_2 ^_{HF_2} Phi^{C_2}HF_2.)

Derivation (exact, witnessed; the one new computation of this doc).
Write the degree-1 slice of pi_* Phi^{C_2}THR(F_2) in WEDGE coordinates
(DMPR 5.18 splitting): e' = the n = 0 base class, f' = Phi(x~) = the
n = 1 summand class. Three facts force everything:

(a) The canonical map Phi^{C_2} -> (-)^{tC_2} (geometric fixed points
    of the Borel completion) is DIAGONAL on the splitting: naturality
    against the summand projections/inclusions kills all
    cross-components. Per summand the target degree-1 group is
    ONE-dimensional (G0), so the images are exact, with no
    higher-filtration wiggle:

        e' -> t^{-1} (z-valuation 0),   f' -> tx = t^{-1}z (valuation 1),
        e' + f' -> t^{-1}(1 + z) (valuation 0).

(b) lambda_pi is central, so it acts on the whole square by ring maps
    and Phi -> Tate is equivariant. Any ring automorphism of R
    preserves degree AND z-valuation degreewise (pi_0 = F_2[[z]] is
    local and intrinsic; each pi_j is free of rank 1 over it).

(c) QS A.4: the action on the Phi corner exchanges the two TENSOR
    classes {w_1, w_2} - a 2-element subset of the 3 nonzero vectors
    {e', f', e' + f'} of the degree-1 slice.

By (b) the exchanged pair must have EQUAL valuation; by (a) the
valuations are (0, 1, 0): the unique consistent identification is

    {w_1, w_2} = {e', e' + f'},  i.e.  Phi(x~) = w_1 + w_2,

the swap-INVARIANT vector (witness G2: unique valuation-consistent
pair). The induced involution of R is then forced exactly:

    phi(t^{-1}) = t^{-1}(1+z),  phi(tx) = tx
    ==>  phi(t) = t(1+z)^{-1},  phi(x) = x(1+z),  phi(z) = z(1+z)^{-1}.

Witnessed exactly (G2): phi is a ring involution, degree-preserving,
valuation-preserving, fixes tx, restricts to the IDENTITY on the Lin
line (z = 0) and on gr_z, and is genuinely nontrivial (phi(z) =
z + z^2 + ...). Grade: DERIVED-STRUCTURAL - theorem-grade inputs (QS
A.3/A.4, DMPR 5.18/5.22) plus Theorem S.1 (with its ring caveat: under
filtration-preserving re-choice of x the formula conjugates; the
invariant content - degree-preserving, unipotent, identity on Lin line
and gr_z - is choice-free).

### 2.4 What the shear is, and what it is not [G3]

It IS new 2-primary structure: phi(z) = z + c with c = z^2/(1+z)
invariant, z^2 + cz + c = 0 over F_2[[c]] (phi(z) is the second root) -
the weight disk is a wildly ramified Z/2 double cover of its
Weyl-invariant disk F_2[[c]] (witness G3; Artin-Schreier shape, the
characteristic-2 signature). The first time in the program a residual
Weyl element acts nontrivially on a nonvanishing reflection-Tate
corner. (Observation, zero weight: under the dictionary z <-> 2^{-s}
the orbit z -> z/(1+z) pairs the Euler variable with its
alternating-series twin 2^{-s}/(1 + 2^{-s}); recorded, not used.)

It is NOT negation, for three independent reasons: (i) it preserves
degree - ladder negation must invert it (cover s -> -s); (ii) it acts
in the WEIGHT direction (horizontal), and even there it is unipotent,
not the inversion n -> -n; (iii) on the weight-0 layer - the Lin line,
the exact home of L-hom's minimal case Spec F_2 - it is the IDENTITY.
Obstruction O-1 (vacuity on the determinant layer) propagates to p = 2
in sharpened form: at odd p the residual structures commuted because
they were linear on lines; at 2 the residual Weyl finally moves
something, and what it moves is concentrated in positive weight
filtration, invisible to DetIn(Spec F_2). Also note the group-theoretic
ceiling of sec 0: lambda_pi is central, so no residual Weyl at the
reflection corner can ever invert the rotation flow - the
flow-inverting element sigma is consumed by the Tate construction
itself. PROBE 1 VERDICT: NEGATIVE for negation supply; positive yield =
the shear + the forced Phi(x~) = w_1 + w_2.

## 3. PROBE 2 (O's rank 2): the lambda^{1/2} kill-test [G4, G5]

### 3.1 O's statements, transcribed verbatim

Probe (O-doc 4.7, item 2):

    "The M-doc's step-3 candidate sharpened by A6: TR with its real
    structure and the Witt-vector anti-involution (DMP
    arXiv:1901.02195) - pose: does the real structure on TR(F_q)
    supply the DOUBLE COVER (a canonical lambda^{1/2} on
    characteristic polynomials)? A6 says this is a NECESSARY feature
    of any carrier, so it is also a cheap kill-test: a candidate
    carrier with no 2-primary headroom is dead on arrival."

Kill-test source (O-doc Prop A6, the operative sentences): recentering
the ladder by one lattice step "FIXES every integer-c scheme ... but
FLIPS THE SIGN of f_{1/2}"; "the symmetric det is NOT a function of
(s, lambda); it is a function of (s, lambda^{1/2}): single-valued only
on the DOUBLE COVER of the eigenvalue space (equivalently: of the
orbit circle)"; "any homotopy-theoretic carrier of H-r3 must supply a
CANONICAL square root of the Frobenius eigenvalue (a 2-primary datum)."

### 3.2 Run against S's square: what t is a square root OF

Exact bookkeeping (witness G4): t^2 = z/x sits in the DEGREE -2,
WEIGHT-0 slot - the slot of the TP periodicity class v. So t is a
canonical square root of the vertical periodicity datum, i.e. (through
the doc-19/20 dictionary: degree periodicity <-> vertical lattice) an
INDEX-2 REFINEMENT of the vertical character lattice: period 1 against
TP's period 2 (S-doc sec 5.2). A6's double cover is "of the eigenvalue
space (equivalently: of the orbit circle)", and the character side of
that equivalence is exactly the half-character q^{w/2}: witnessed at
q = 2 (G4), every integer-c scheme is single-valued on the orbit
circle (f_c(w + t_sp) = f_c(w)), while f_{1/2} flips on one loop and
closes on the DOUBLE loop (f_{1/2}(w + 2t_sp) = f_{1/2}(w)). A
degree-halved periodicity class is precisely the headroom on which
q^{w/2} becomes an integral character. The rho-graded mediator is
already in the literature for the base: QS21 Prop 6.14 (verbatim:
"pi^{C2}_{**}(HF_2^{tC2 S^1}) ~= HF2_{**}((u)), where |u| = (-2,-1)") -
a single rho-graded class whose underlying shadow occupies the
degree -2 (v) slot and whose geometric/reflection shadow occupies the
degree -1 (t) slot. The double cover IS the rho-grading, seen from its
two integer shadows.

What t does NOT supply: any square root of the WEIGHT/eigenvalue
grading. The weight monoid of R is Z_{>=0} (generators: wt(t) = 0,
wt(z) = 1); there is no z^{1/2} (G4). So per-weight recentering
lambda_n = 2^{-n} -> 2^{-n/2} has no carrier in R itself; what R
carries is the s-direction half-character. Under A6's "equivalently"
these are the same demand at a CENTERED ladder - which is exactly the
L-hom locus Spec F_2 - so for the minimal case the headroom is the
right kind.

GUARD against over-reading doc 25 (witness G5, registered): S-r5's
"self-dual KMS-1/2 form appears geometrically" is SCHEME-APPLIED, not
scheme-forced: the identity 2^{(s+n)/2}(1 - 2^{-(s+n)}) =
2 sinh((s+n) log2/2) is what the SYMMETRIC scheme assigns to the full
t-line; the c = 0 scheme on the SAME carrier line gives (1 - 2^{-(s+n)})
with w-DEPENDENT negation ratio (witnessed: ratio constant -1 for
c = 1/2; non-constant for c = 0). S's computation supplies the CARRIER
(full vertical line per weight, for the first time at a reflection);
the scheme selection is still exactly L-hom. Doc 25's sentence should
be cited only in this form.

### 3.3 Kill-test verdict, and the identifications owed

VERDICT: NOT KILLED - the first candidate carrier in the program with
A6's necessary 2-primary headroom (odd-p TPR: period 2, no half class;
odd-p reflection Tate: zero; S's square at 2: period-1 t present).
Survival is a necessary condition only. To convert headroom into the
canonical lambda^{1/2} two identifications are owed:

    (N1) [comparison] A dihedral/real-cyclotomic comparison map under
    which Hesselholt's periodicity v corresponds to t^2 = z/x - e.g.
    realizing t and v as the two integer shadows of one rho-graded
    class (QS21 Prop 6.14 pattern; their description (3.1) of
    (X^{tC_2 mu_p})^{phiC_2} and the QS19 parametrized layer are the
    natural vehicles). Status: stated, not constructed.
    (N2) [normalization] Compatibility with Hesselholt's Theta
    normalization (Theta(v) = (2 pi i/log q) v): the determinant-layer
    enhancement at 2 must read its character lattice from the
    t-grading, so the lattice spacing halves to (pi i/log 2) and
    q^{w/2} becomes integral. Status: a convention-boundary question
    (the doc-25 degree-vs-weight flag), adjudication owed to Q-SCHEME.

## 4. PROBE 3 (O's rank 3): the duality route, and the F1 verdict [G6]

### 4.1 O's statement, transcribed verbatim (O-doc 4.7, item 3)

    "The duality route: formulate 'reflection = duality on the
    compactified object' inside the C5''' properness vehicle (log-THH
    residue sequences / CC's S-valued RR); this is where the
    degree-inverting v^m <-> v^{-m} can live lawfully."

### 4.2 Run against S's square: duality lives at every finite level and
dies in the completion

Weightwise, negation IS realizable as a duality: the Lin line satisfies
Tate duality, D_{F_2}((HF_2)^{tC_2}) ~= Sigma (HF_2)^{tC_2} (perfect
pairing H-hat^i (x) H-hat^{-1-i} -> F_2; Greenlees-May), whose pi_*
shadow is exactly t -> t^{-1} up to the unit shift - O 4.6's "duality,
not automorphism", for the first time with a NONVANISHING carrier at a
reflection. On the weight-truncated object R/z^{N+1} this assembles to
a perfect residue pairing (witness G6, exact, all N <= 6, all degrees
tested):

    <a, b> := coeff of t^{-1} z^N in ab :  pi_j x pi_{1-j} -> F_2,

perfect and ANTIDIAGONAL: weight m pairs with weight N - m. Finite-level
Serre-type self-duality with a weight FLIP - the degree-inverting
structure O predicted, living lawfully on the truncation. But the flip
is m <-> N - m: its "center" N/2 runs away with the truncation, and the
limit pairing is identically zero on finite-weight elements (G6: for
every fixed pair the value is eventually 0). On the completed object
the duality is gone altogether: D_{F_2}(F_2[[z]]) has F_2-dimension
2^{2^{aleph_0}} (Erdos-Kaplansky) and is not the disk - the dual of
S's Tate is a DIVIDED-POWER co-disk in the weight direction, a
different object. The unique self-dual locus is weight 0 = the Lin
line, the part with no Euler content.

Read structurally: S-r5's "duality completion DOES happen at 2" is a
completion of the DEGREE direction per weight (full t-lines) PLUS a
one-sided z-adic completion of the weight direction - and that
one-sidedness is precisely the convergence half-plane of the local
Euler factor (1 - 2^{-s})^{-1}. The same move that produces the
completed 2-adic Euler ladder destroys s -> -s: the functional-equation
flip cannot live on a one-sidedly completed object. This is the exact
p = 2 form of O 4.6's "'the reflection acts by the duality' is a
statement about a COMPACTIFIED/self-dual object".

### 4.3 F1 verdict and the surviving conjecture

F1 RESOLVES NEGATIVE FOR THE THR CARRIER. Stated plainly, per the
doc-24 risk clause ("if F1 resolves negative, THR's C_2 cannot force
the scheme and realization input 4 loses its only carrier"): at odd p
the C_2-structures commute with everything (O-doc); at p = 2 - the new
territory, the only prime with a nonvanishing reflection Tate - every
equivariant structure in S's computed square is degree-preserving, the
residual Weyl acts by the shear (trivially on the L-hom locus), the
flow-inverting element sigma is consumed by the construction, and the
abstract t -> t^{-1} is an ungraded algebra symmetry with no
spectrum-level realization on the completed object. THR's geometric
C_2 does not supply ladder negation ANYWHERE it has been computed, and
at 2 the obstruction is now exact rather than absence-of-evidence.
Realization input 4 (doc 10) has no THR carrier. Doc 24's escape clause
named two candidate layers; this run closes one and a half of them:
the rho-graded/parametrized layer ACTS (the shear - so it is no longer
terra incognita) and does not negate; what survives is ONLY the
duality layer / C5''' - and for it, S's square now supplies a precise
interface:

    CONJECTURE U.2 (L-hom, duality-layer instance at p = 2; the
    surviving form). There exists a compactification T of THR(F_2) in
    C_2-spectra with O(2)-structure (properness vehicle: log-THR
    residue sequence / S-valued RR), with an open-part map
    j: THR(F_2)^{tC_2} -> T^{t}, such that:
    (a) [self-duality] D_{F_2}(T^{t}) ~= Sigma T^{t}, restricting on
        weight 0 to the Lin-line Tate duality;
    (b) [geometric supply] the self-duality is INDUCED by the
        O(2)/real structure (the reflection acting as the duality) -
        this clause, not (a), is the content of L-hom - and under the
        doc-19/20 dictionary it covers s -> -s with constant unit
        u = -1 in the naturality sense of O-doc 1.3;
    (c) [weight compactification] the weight direction of T^{t} glues
        F_2[[z]] to its divided-power dual along weight 0 (the
        sum/product reconciliation of 4.2) - i.e. completes the
        one-sided Euler ladder to a negation-stable object;
    (d) [A6 discharge] the periodicity of T^{t} is the period-1 class
        t, with (N1)+(N2) of sec 3.3, so the forced determinant is
        single-valued (no mu_2 ambiguity).
    Proof requires: construction of T (C5'''s standing burden, now
    with a target shape), computation of its Tate square, equivariance
    of the duality, and the (N2) normalization. Given U.2, L-hom holds
    at Spec F_2, and with O's L-an the doc-24 chain closes AT p = 2;
    the odd-p and archimedean instances would still need their own
    carriers (the entangled-pair reading of S-doc sec 9.2).

Fail-closed addendum: nothing in this doc is evidence FOR U.2 beyond
consistency (finite-level duality exists; the interface is
non-contradictory). If C5''' produces no such T, the forcing of
KMS-1/2 has no homotopy carrier at all, and doc 24's scheme-selection
answer path is dead - that statement should be carried verbatim into
the next gate review.

## 5. G-INT6 DOF ledger

- Zero fitted parameters anywhere. All claims are exact F_2 algebra
  (G0-G3, G6), integer bookkeeping (G4 ring side), or 1e-12 identities
  (G4 numerics, G5).
- Inputs spent: Theorem S.1 + S's square maps (S-doc, with its ring
  caveat - inherited and flagged at the shear); QS21 Props A.3/A.4,
  6.13/6.14 (published theorem-grade, read verbatim from the archived
  extraction); DMPR 5.18/5.20/5.22 with proofs (same); the doc-19/20
  dictionary (already spent by docs 19/20/24/25; no new dictionary
  choices).
- The one derivation (the shear) spends NO free choices: the candidate
  set {e', f', e'+f'} is the full degree-1 slice, and the
  valuation-consistency pin is 1-of-3 with the other two refuted
  (witnessed). Its grade is derived-structural, not theorem, because
  the lambda_pi-equivariance of the corner maps is used from the
  formal functoriality of (-)^{tC_2} on C_2-spectra with commuting
  action, not from a worked O(2)-model; flagged in sec 6.
- Registration discipline: R-G0..R-G6 written before the first run;
  first run failed G3 at even N; cause identified as a top-degree
  truncation artifact (z^{N-1} spuriously fixed because its correction
  lands at z^N); gate re-specified with the artifact-aware count and
  the amendment recorded verbatim in the docstring. The three exact
  identities of G3 and all odd-N dimensions passed unmodified on the
  first run. No other gate was touched after first execution (two
  earlier all-fail runs were sign-convention bugs in the test harness
  encoding of t-exponents, fixed before any gate logic ran clean;
  recorded here for completeness).
- Readings flagged as readings: the alternating-Euler observation
  (2.4); the dictionary readings of t-period-halving (inherited flag
  from S-doc 5.2); doc-25's "appears geometrically" downgraded to
  scheme-applied (G5) - a GUARD, not a new reading.

## 6. Honest limits

- Everything rides on Theorem S.1 (new to the literature, worker S's
  computation, lead-rerun but not independently re-derived here). The
  shear formula inherits S.1's generator-choice caveat: under
  filtration-preserving re-choice of x it conjugates; the invariant
  content (unipotent, degree-preserving, identity on Lin line and
  gr_z, Z/2-cover with valuation-2 invariant uniformizer) is
  choice-free.
- The identification of QS21's mu_2 with the residual Weyl W_{O(2)}(C_2)
  = <lambda_pi> rests on their proof line ("rotation action of mu_2 on
  S^sigma") plus the group theory of sec 0; if their mu_2 were some
  other C_2 the NAME changes but the derived Tate involution and both
  verdicts do not.
- lambda_pi-equivariance of Phi -> Tate is formal functoriality; I did
  not exhibit the point-set O(2)-model (Hogenhaven-style) underlying
  it. A reader wanting theorem-grade should check QS21 secs 2-3
  (dihedral recollements) suffice; flagged.
- The non-self-duality of the completed Tate is established at the
  pi_*/F_2-module level (Erdos-Kaplansky). An exotic self-duality
  invisible to homotopy is not excluded; it would have to be invisible
  to pi_* entirely, which no determinant-layer construction in this
  program could use anyway.
- Probe 2's TR/Witt-anti-involution half (DMP 1901.02195) was NOT run:
  the task scoped the probes against S's square, and S's square does
  not contain TR. The A6 kill-test was run in its stead, as O's own
  sharpening prescribes. TR at 2 with the anti-involution remains an
  unexamined corner (it would be the natural place to seek (N1)).
- No archimedean claims; no RH/zero-side input; all statements live at
  the finite-place shadow per the standing fork discipline.

## 7. Hand-off table (for the lead)

```text
probe 1 (structure maps / residual Weyl):  NEGATIVE for negation.
   New: forced Weyl shear t -> t/(1+z), z -> z + c; Phi(x~) = w_1+w_2;
   disk = Z/2-cover of F_2[[c]].  [G0-G3]
probe 2 (lambda^{1/2} kill-test):          PASSED (not killed).
   t = canonical sqrt of the v-slot (vertical double cover); no weight
   sqrt; identifications (N1),(N2) owed.  [G4, G5 guard]
probe 3 (duality route):                   F1 NEGATIVE for THR carrier.
   Finite-level residue duality (weight flip m <-> N-m), degenerate in
   the completion; disk/co-disk obstruction; Conjecture U.2 = the
   surviving L-hom instance, interface (a)-(d).  [G6]
doc-24 update owed: (infty-3'') L-hom/F1: THR-alone carrier CLOSED at
   odd p (O) and at p = 2 (this doc); rho/parametrized escape route
   closed (the Weyl layer acts and shears); remaining carrier class:
   duality layer / C5''' via Conjecture U.2.  Realization input 4
   currently has NO carrier.
```
