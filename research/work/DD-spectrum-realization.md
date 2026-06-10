# DD - Spectrum-level realization of Z's glued object G (C5''' front): the Brown-Comenetz route

Status: fresh-context worker DD, 2026-06-10. Doc 29 ranked front 4
(pose-and-probe; precise partial result over vague attempt). Required
reading executed in order: doc 28, doc 29, Z-u2-gluing.md IN FULL,
U-f1-probes.md (Conjecture U.2 clauses (a)-(d); owed N1/N2),
S-thr-p2.md (Theorem S.1 + square), M-thr-fold-test.md; refs re-read at
load-bearing points: QS21 (Props 6.13/6.14 verbatim, Rem 6.23, formula
(3.1), Appendix A Thm A.2 / Props A.3-A.5 verbatim from the archived
extraction), QS19/DMPR/HW via the S/U/M transcriptions.

Witness (NEW, ALL PASS on first run, exit-code gated):
scripts/numerics/witness/prime_int_dd_bc_dual.py (gates DDG1-DDG7,
pre-registered fail-closed readings in the docstring, written before
the first run; exact F_2 arithmetic throughout, no numerics at all).

NEW ARCHIVES (research/proof/refs/): dwyer-greenlees-iyengar2006-
duality-algebra-topology.pdf (+ dgi2006.txt; Matlis duality = the
p-primary part of Brown-Comenetz duality, their framework);
greenlees-meier2017-gorenstein-duality-real-spectra.pdf (+
greenlees-meier2017.txt; C_2-equivariant Anderson/Gorenstein duality
is theorem-grade for Real spectra: KR [Heard-Stojanoska 1401.2581],
BPR<n>, tmf_1(3) - the precedent that clause (iii)'s demand is not
exotic).

HEADLINE (three results, one no-go, one posed lemma):

1. BC ROUTE VERDICT: SPLIT, with both halves exact. The plain
   Brown-Comenetz dual of THR(F_2)^{tC_2} does NOT have homotopy D'
   (Erdos-Kaplansky: the full dual of F_2[[z]] is too big). The
   continuous BC dual of the z-adic TOWER of truncations matches D'
   EXACTLY: the dual tower is isomorphic to Z's multiplication-by-z
   tower via the level-N residue self-dualities, with colimit labels
   reproducing Z's insertions iota_N verbatim (DDG1) and the
   divided-power multiplication falling out of the dual Hopf structure
   (DDG2). U.2's "divided-power dual" IS the homotopy of the
   continuous Brown-Comenetz dual of the THR Tate tower - a theorem at
   the level stated (sec 2), not a conjecture.
2. REALIZATION OF G AS AN HONEST SPECTRUM (Theorem DD.3, modulo
   Theorem S.1): X-bar := fib( X x X' --(q - aug')--> Y ) with
   X = THR(F_2)^{tC_2}, Y = (HF_2)^{tC_2} (the Lin spectrum),
   X' = colim(X_0 --z--> X_1 --> ...) the colimit of truncations, has
   pi_* X-bar = G exactly (Mayer-Vietoris; DDG4). Clause (i) of the
   task is REACHED at module level, with zero free choices
   (Aut_Y(Y) = F_2^x = 1).
3. THE E-K NO-GO RESHAPES U.2(a) (fail-closed deliverable): NO honest
   spectrum T with pi_* T = G can satisfy a plain self-duality
   D_{F_2}(T) = Sigma T - the profinite half of G dualizes to
   something of dimension 2^{2^{aleph_0}} per slot. U.2(a) must be
   amended to CONTINUOUS self-duality in a filtered/pro-ind (or
   condensed) category. The sharp realization statement is Conjecture
   DD.4 (sec 4).
4. N1 (t vs Hesselholt's v): posed as Lemma N1 (sec 5) with QS21's
   contributions transcribed and the remaining gap split into three
   named components, one of which is a FINITE Borel computation
   against S.1's square (the minimal next computation). New reading:
   the unit ambiguity in N1, the (1+z)-unit equivariance defect of the
   tower (DDG7), and Z's kappa nullity are the SAME 1-unit torsor.

## 1. Conventions (pinned)

I := the 2-primary Brown-Comenetz dual, I(M) = F(M, I_{Q/Z}). For any
spectrum M, pi_j I(M) = Hom(pi_{-j} M, Q/Z) EXACTLY (Q/Z injective: no
Ext correction). All objects here are HF_2-modules (unit
HF_2 -> (HF_2)^{hC_2} -> Y := (HF_2)^{tC_2}; the Tate of an
HF_2-module-with-C_2-action is a Y-module), so all homotopy is
F_2-vector spaces and Hom(-, Q/Z) = Hom(-, F_2): I = the F_2-linear
dual, and I(M) = F_Y(M, I(Y)) for Y-modules. Two theorem-grade anchor
facts: I(HF_2) = HF_2 (BC self-duality of HF_2), and the Lin-line Tate
duality D_{F_2}(Y) = Sigma Y (Greenlees-May; genuinely C_2-equivariant
- the only U.2(b) clause already in the literature, per Z sec 8).
In Mod_Y all integer suspensions are canonically trivialized
(t in pi_{-1} Y is the unique nonzero class of H-hat^1(C_2; F_2);
multiplication by t is an equivalence): degree bookkeeping below is
carried by the internal weight grading, as in Z.

Objects (Theorem S.1): X := THR(F_2)^{tC_2}, pi_j X = t^{-j} F_2[[z]];
truncations X_N := X/z^{N+1} (finite free Y-modules of rank N+1, the
z-adic tower, X = lim X_N); X_0 = Y = the Lin line.

## 2. The BC computation (exact; witnessed)

### 2.1 Plain level: MISMATCH (Theorem DD.1)

pi_j I(X) = Hom_{F_2}(pi_{-j} X, F_2) = Hom_{F_2}(F_2[[z]], F_2),
which by Erdos-Kaplansky has F_2-dimension 2^{2^{aleph_0}} - it
strictly contains the countable D'_j and is NOT it. (U sec 4.2 found
this for D_{F_2}; the BC dual is the same functor here.) So the answer
to the task's direct question - "is D' the homotopy of I_{Z/2} of the
THR Tate construction?" - is NO for the Tate construction as a plain
spectrum. This is not a defect of the route; it is the precise reason
the realization must be filtered (sec 4).

### 2.2 Tower level: EXACT MATCH (Theorem DD.2)

Claim: the BC dual of the z-adic tower is Z's multiplication-by-z
tower, and its colimit homotopy is D' with Z's own labels.

(a) Each truncation is SELF-dual: the level-N residue pairing
    <a, b>_N = (coeff of t^{-1} z^N in ab) on pi_j X_N x pi_{1-j} X_N
    is perfect with permutation Gram implementing the weight flip
    m <-> N-m (DDG3; = U's G6 re-derived from the dual side). In
    Mod_Y this realizes spectrum-level: X_N is finite free, so
    I(X_N) = Sigma F_Y(X_N, Y) is finite free of the same rank, and
    the pi_*-isomorphism s_N: z^m |-> (z^{N-m})^* is realized by a
    Y-module equivalence (maps of free Y-modules are detected on
    pi_*). The flip center N/2 runs away with N - U's divergence,
    now visible as the N-dependent dualizing shift.
(b) The dual tower {I(X_N), dual of the quotients} is conjugated by
    the s_N into the (x z)-tower: p_N^* o s_N = s_{N+1} o (x z),
    an exact matrix identity at every level (DDG1). Squares of free
    Y-modules commuting on pi_* commute; so the tower isomorphism is
    spectrum-level in Mod_Y.
(c) Hence colim_N Sigma I(X_N) = colim(X_0 --z--> X_1 --> ...) =: X',
    and pi_* X' = D' exactly: stable labels gamma_m = (z^m)^*, the
    composite label of s_N(z^m) is gamma_{N-m} = Z's iota_N (DDG1),
    and the multiplication dual to the (forced, weight-graded
    additive) coproduct is the divided-power algebra, Lucas digit law
    and gamma_{2^k}^2 = 0 included (DDG2). Matlis biduality on
    truncations (lim/colim swap) is exact (DDG5).

So: THE BC DUAL OF THE F_2[[z]]-TOWER IS EXACTLY THE DIVIDED-POWER
COLIMIT, as the task conjectured - with the caveat that "tower" is
essential. U.2's duality clause, restricted to the weight branches, is
hereby a THEOREM at the filtered Y-module level: D' = pi_* of the
continuous BC dual I^cont(X-pro) := colim_N I(X_N) of the pro-object
X-pro = {X_N}. Grade: derived-structural (rides on Theorem S.1; the
free-module realization steps are standard Mod_Y algebra).

## 3. The glued spectrum (Theorem DD.3): G is realized

Define (all data canonical in Mod_Y; G-INT6 ledger in sec 7):

    q : X -> X_0 = Y                  (tower projection, a ring map)
    aug' := colim_N Sigma I(unit_N) : X' -> Sigma I(Y) = Y
           (the BC dual of the unit Y -> X_N, i.e. the
            gamma_0-coefficient; = top-weight projection under iota_N)
    X-bar := fib( X x X' --(q, aug') difference--> Y )
           = the homotopy pullback X x_Y X'.

Both q and aug' are surjective on homotopy (each hits F_2[t^{+-1}]),
so Mayer-Vietoris degenerates to short exact sequences

    0 -> pi_j X-bar -> pi_j X (+) pi_j X' -> pi_j Y -> 0,

and pi_j X-bar = {(a, b) : a|_{weight 0} = b|_{gamma_0}} = D (+)_Lin
D' = G_j - one slot per weight in Z, weight 0 once (DDG4: kernel
dimension 2M+1 per truncation window, weight map bijective onto
{-M..M}). The ring structure: q is the quotient by the ideal (z) and
aug' is dual to the unit; at pi_* the fiber product of rings is Z's
nodal G (Z sec 2.3(ii)). [Spectrum-level E_infty structure on X-bar:
plausible (pullback of ring maps) but the ring-map property of aug'
at spectrum level is NOT verified here; flagged.]

This discharges clause (i) of the task as a theorem modulo Theorem
S.1: a genuine spectrum whose homotopy recovers S's Tate disk D and
the forced divided-power dual D' glued along the Lin line, with the
gluing locus literally the Lin spectrum Y and the gluing maps the
tower projection and the BC-dual of the unit. No pro-structure is
needed for EXISTENCE - only for the duality (next).

## 4. The realization conjecture, sharp (Conjecture DD.4)

The E-K no-go (DD.1) applies to X-bar itself: pi_* I(X-bar) contains
the full dual of the profinite half - I(X-bar) != Sigma X-bar for ANY
honest spectrum with homotopy G. Fail-closed consequence carried back
to U: U.2(a) ("D_{F_2}(T^t) = Sigma T^t") is UNSATISFIABLE as stated
at pi_*-level G and must be amended to a continuous duality. The
repaired statement:

    CONJECTURE DD.4 (continuous BC self-duality; the C5''' theorem
    shape). Equip X-bar with its pro-ind filtration: the pro-half
    {X_N} on the D-branch, the ind-half {Sigma I(X_N)} on the
    D'-branch, glued at X_0 = Y = Sigma I(X_0). In a stable category
    where the continuous BC dual I^cont (:= colim I(-) on pro-halves,
    lim I(-) on ind-halves) is defined and lax symmetric monoidal
    (candidate homes: filtered spectra; pro-ind/Tate objects in
    Mod_Y; condensed/solid F_2-spectra),

        I^cont(X-bar) = Sigma X-bar,

    the equivalence EXCHANGING the two branches (DD.2's tower
    conjugation), restricting on the gluing locus to the
    Greenlees-May C_2-equivariant Lin duality, and inducing on pi_*
    exactly Z's perfect G-pairing (witnessed: DDG6 - evaluation
    reproduces Z's table, Gram = permutation (j,m) <-> (1-j,-m)).

What is already proved of DD.4: everything pi_*-level and everything
truncation-level (DDG1-DDG6 + the free-Y-module realizations of sec
2.2); the conjectural content is FUNCTORIALITY - one categorical home
where the branchwise duals assemble to one involution of one object.
Literature support, archived: DGI 2006 (Matlis duality is the
p-primary part of BC duality - our pro/ind pair is their
complete/torsion pair for the "ring" F_2[[z]], so DD.4 is a Gorenstein
-duality-with-shift statement in their sense); Greenlees-Meier 2017 /
Heard-Stojanoska (C_2-equivariant Anderson self-duality is
theorem-grade for Real spectra - the demand that the duality be
equivariant is not exotic). NOT found in the literature: any BC/
Anderson duality statement for cyclotomic or real-cyclotomic spectra
as such (searched: BC dual cyclotomic, Anderson duality real,
dualizing cyclotomic spectra, NS Tate duality); nearest neighbors are
Blumberg-Mandell Tate-Poitou (Anderson duality over S, etale side;
already archived/assessed in K-doc sec b) and the Gorenstein
literature above. A real-cyclotomic Gorenstein duality would be new.

### 4.1 Clause (iii): the O(2)-structure (open; localized)

What is established: the gluing locus duality is genuinely
C_2-equivariant (Greenlees-May); the Weyl shear phi acts compatibly
with the whole tower (DDG7: valuation-preserving involution on each
X_N commuting with the quotients, hence acting on the dual tower;
fixes gamma_0). What obstructs naive equivariance: (x z) is
phi-equivariant only up to the 1-unit (1+z)^{-1} (exact identity,
DDG7b), and the level-N self-duality is NOT a phi-isometry (defect
witnessed nonzero, DDG7c) - equivariance of the duality exists only
on the GLUED object, exactly Z's kappa mechanism (ZG7). READING
(flagged): the 1-unit torsor in DDG7b, the unit ambiguity (g3) of
Lemma N1 below, and Z's kappa nullity-43 are one and the same
non-uniqueness; pinning any one pins all three. The genuine
O(2)-structure on X' and X-bar (U.2(b) proper) remains the open half
of C5'''; it is NOT reached here.

## 5. N1: the dihedral comparison (posed as a lemma; QS21 transcribed)

What QS21 actually provides (verbatim from the archived extraction):

    [Prop 6.14] "pi^{C2}_{**}(HF_2^{hC2 S^1}) = HF2_{**}[[u]],
    pi^{C2}_{**}(HF_2^{tC2 S^1}) = HF2_{**}((u)), where
    |u| = (-2,-1)."
    [Rem 6.23] "abstract isomorphisms ... pi_{**}(TPR(HF_2)) =
    (HZ_2)_{**}[u^{+-1}]" with the finer multiplicative analysis
    "left to the interested reader".
    [Thm A.2, attributed to forthcoming Harpaz-Nikolaus-Shah] "Let X
    be a real cyclotomic spectrum that is underlying bounded-below.
    There is an equivalence TCR(X)^{phi mu_2} =
    fib(X^{phiC2 h mu_2} -> X^{phiC2 t mu_2})" via the projection of
    (phi_2)^{phiC2} with respect to the description (3.1) of
    (X^{tC2 mu_2})^{phiC2}.
    [Props A.3/A.4] the residual mu_2 swaps the two tensor factors of
    THR(R)^{phiC2}; on F_2[w_1, w_2] it swaps w_1, w_2.

Degree bookkeeping that makes u the mediator (exact): |u| = (-2,-1)
means underlying shadow in integer degree -2 (Hesselholt's v-slot of
TP(F_2)) and sigma-collapsed shadow in degree -2 with one sigma
replaced by 1 - under the mod-2 Thom trivialization Sigma^sigma HF_2 =
Sigma HF_2 (S.1 proof step 2) an RO-degree (s,t) class lands in
integer degree s in Mod_Y; while its GEOMETRIC shadow (phi^{C2},
S^{sigma} |-> S^0) lands in degree s - t = -1: the t-slot. One
rho-graded class, two integer shadows, in the v- and t-slots
respectively - exactly U's Probe-2 demand.

    LEMMA N1 (posed; the owed identification). Let u be the TPR(F_2)
    periodicity class (QS21 6.8b). Then:
    (N1-a) res(u) = v . (unit of Z_2) in pi_{-2} TP(F_2)
           [Hesselholt's class];
    (N1-b) under the composite THR(F_2)^{hC_2 S^1} -> THR(F_2)^{hC_2}
           -> THR(F_2)^{tC_2} (forget the parametrized circle, then
           can), followed by the mod-2 Thom collapse of the
           sigma-twist, the image of u is t^2 . (1-unit of F_2[[z]])
           in pi_{-2} THR(F_2)^{tC_2} = t^2 F_2[[z]].
    Consequently t^2 and v are the two integer shadows of the single
    rho-graded class u, t is the sigma-collapse square root (the A6
    double cover = the rho-grading, as U read it), and N2's t-lattice
    (already FORCED by Z's ZG8) acquires its dihedral comparison.

Remaining gap, split (each component finite and named):

    (g1) MULTIPLICATIVITY of QS21 Rem 6.23: only the RO(C_2)-graded
         group isomorphism is in print; the ring identification (and
         hence "res(u) = v up to unit" rather than "some degree--2
         class") is the "finer analysis" QS21 left to the reader.
    (g2) THE FORGET-MAP IMAGE (the minimal first computation): compute
         the composite of (N1-b) on the class u against S.1's computed
         square. All corners and maps are known (S doc sec 4); the
         x-adic filtration method of QS21 sec 6.2 applies; this is a
         finite Borel computation. Expected output: u |-> t^2 + O(z)
         with the O(z) tail exactly a 1-unit multiple.
    (g3) UNIT PINNING: the 1-unit in (N1-b) is well-defined only up to
         the shear orbit (DDG7b/Z-kappa torsor, sec 4.1). A canonical
         pinning = a canonical kappa = a phi-invariant normalization
         (e.g. through the invariant form dlog(1+z)); open.

Status: N1 is NOT proved here (it is spectrum-level and was not
reachable from G alone, as Z sec 5.2 said); what is new is the precise
route (N1-b), the reduction to (g1)-(g3), and the identification of
(g3) with the existing kappa torsor.

## 6. Honest assessment (the task's clause-by-clause verdict)

```text
(i)  fixed/Tate invariants recover both halves glued along Lin:
     THEOREM-GRADE REACHED (DD.3; X-bar honest spectrum, pi_* = G;
     witnessed DDG4; rides on Theorem S.1).  Pro-structure NOT needed
     for existence.
(ii) pairing induced by spectrum-level duality: SPLIT.  Tower-level
     continuous BC duality = THEOREM (DD.2, DDG1-DDG3, DDG5-DDG6);
     plain-spectrum self-duality = REFUTED (E-K no-go; U.2(a) must be
     amended); one-object functorial statement = CONJECTURE DD.4
     (named, sharp, with a categorical home to be chosen).
(iii) O(2) covers s -> -s: OPEN; localized to the 1-unit torsor +
     genuine O(2)-structure on X' (sec 4.1); N1 posed with gaps
     (g1)-(g3), minimal first computation = (g2).
```

Minimal first computations, ranked: (1) g2 (finite, all inputs
computed); (2) DD.4 in solid/condensed F_2-modules over F_2[[z]] -
the DGI complete/torsion machinery is already written there, so this
may be a transcription rather than a theorem; (3) the C_2-equivariant
upgrade of the truncation self-dualities (Greenlees-Meier toolbox).

## 7. G-INT6 ledger and guards

- Inputs spent: Theorem S.1 (+ its ring caveat, inherited);
  Greenlees-May Lin duality (theorem); I(HF_2) = HF_2 and Q/Z
  injectivity (theorem); Erdos-Kaplansky (theorem); Matlis/divided-
  power algebra (theorem; re-witnessed exactly); QS21 6.13/6.14/6.23/
  (3.1)/A.2-A.4 (published or attributed-forthcoming, transcribed
  verbatim); DGI 2006 + Greenlees-Meier 2017 (archived this pass).
  No RH/zero-side input anywhere.
- Zero free choices in the construction: D' forced (Z L1-L2); q =
  tower projection; aug' = BC dual of the unit; the identification
  Sigma I(Y) = Y is Greenlees-May and Aut_{Mod_Y}(Y) = pi_0(Y)^x =
  F_2^x = 1 (no unit ambiguity at the gluing locus); t is the unique
  nonzero class of H-hat^1(C_2; F_2).
- The one non-unique datum: the 1-unit torsor of sec 4.1/(g3),
  inherited from Z (kappa, nullity 43), now identified across three
  appearances - disclosed, not load-bearing for DD.1-DD.3.
- Carrier guard (K5): every object here is built from S.1's ring -
  no ring => no Tate => no tower => no X', no X-bar. DH/Epstein die
  at X_0. The construction never sees zeta's continuation (the F-a
  guard of Z sec 6 is inherited: the divided-power side refuses
  F_2((z))).
- Registration discipline: DDG1-DDG7 readings written in the witness
  docstring before the first run; ALL PASS first run; no gate or
  reading amended at any point.

## 8. Hand-off (for the lead)

```text
BC ROUTE:   plain dual MISMATCH (E-K), tower dual EXACT MATCH; D' =
            pi_* of the continuous BC dual of the z-adic tower
            (theorem at filtered Mod_Y level; DDG1-DDG2).
REALIZED:   X-bar = X x_Y X' honest spectrum, pi_* = G (DD.3, DDG4);
            clause (i) of C5''' discharged at module level.
RESHAPE:    U.2(a) as stated is UNSATISFIABLE for pi_* = G (E-K);
            amend to continuous self-duality => Conjecture DD.4
            (filtered/condensed; DGI Gorenstein shape; real-cyclotomic
            BC duality NOT in the literature - genuinely new target).
N1:         posed as Lemma N1 via the rho-class u (QS21 6.14/6.23 +
            Thm A.2 transcribed); gaps g1 (multiplicativity), g2
            (finite Borel computation against S.1 - DO THIS FIRST),
            g3 (1-unit pinning = Z's kappa torsor, same object).
N2:         unchanged (forced by Z); N1-b would supply its dihedral
            comparison.
OPEN:       genuine O(2)-structure on X' / X-bar (U.2(b) proper);
            E_infty on X-bar; the categorical home for I^cont.
```

## Postscript (2026-06-10, worker EE): display correction + clause 1 proven + g2 refuted

Theorem EE.1 (research/work/EE-dd4-lin.md) PROVES the Lin-block clause:
the duality datum is the UNIQUE nonzero Y-module map Y -> Sigma I(Y)
(singleton - no torsor on the Lin block), inducing Z's K2 Lin block
exactly. DISPLAY FIX: DD.4 must read Xbar ~ Sigma I^cont(Xbar) - this
doc's display I^cont(Xbar) ~ Sigma Xbar is off by Sigma^2 against its
own gluing maps (invisible in Mod_Y; fix before transplanting).
Theorem EE.2 REFUTES N1-b: u -> 0 in pi_{-2}THR(F_2)^{tC_2} (the
bidegree slot vanishes; two independent corroborations; the Weyl Tate
is x-COMPLETE, opposite to the dihedral Tate) - g2 closed negatively;
re-posed as N1-b' on the geometric t-shadow (QS21 A.5-A.7). The
one-torsor reading loses its N1 leg; the torsor's support is exactly
weights >= 1 (Lin block torsor-free as a theorem); leading
z-coefficients are torsor-invariant. Also (worker FF, conditional):
I^cont is NOT the Poisson-exchange carrier - DD.4's triple duty drops
to double (scheme + pole); the scale needs a rational/Anderson layer.
