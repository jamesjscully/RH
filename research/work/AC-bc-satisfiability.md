# AC - BC joint-satisfiability (M3): the twelve BCs are a shape spec, not a positivity spec; the missing clause named

Status: fresh-context worker AC, 2026-06-11. Charter doc 39 sec 4 move
M3 (the conservation law's formal self-test). Required reading executed
in order: doc 39, WW-silhouette-dossier.md in full (BC1-BC12, the
null-hypothesis verdict), docs 34 + 37 (six-clause spec; FE-blindness
and evasion-not-surplus), doc 13 (the banked equivalence
RH <=> uniform tau_r < 1, the comparison target), YY (P3 + BC-E1..E4),
doc 14 (fork protocol).

DISCIPLINE: this is a LOGICAL analysis, not a construction; no witness
is required and none is fabricated (fail-closed: numerics did not
arise). F-a: every contact with zero data below is labeled
[COMPARISON/LOGIC] - zero data is used only to test what satisfaction
would IMPLY, never as input to any new claim. G-INT6 ledger sec 6.
BC numbering: WW's canonical BC1-BC12 (doc 39 registry); YY's four are
BC-E1..E4.

## 0. The question and the answer in one paragraph

M3 asks: does any (category, trace) satisfying all twelve BCs differ
from RH? ANSWER (defended below): the twelve BCs AS STATED are jointly
satisfiable in a non-RH world - verdict SAT-WEAKER - because every BC
is either supply-side (zero-free by construction, hence RH-independent)
or, in the case of BC6, demands AGREEMENT and INDEPENDENCE but not
POSITIVITY of the agreed value. The dossier is therefore incomplete as
a characterization of RH by exactly one clause, which this memo names
(BC13, sec 4): the second evaluation must be FORCED NONNEGATIVE
(effectivity/index) UNIFORMLY IN SCALE on a class family EXHAUSTING the
doc-00 filtration core. With BC13 adjoined, satisfiability becomes
equivalent to RH at stated grade (sec 3) - the zero-shortcut
confirmation - and possibly STRICTLY STRONGER at P3 grade (flagged,
sec 3.2). The conservation law survives M3: no reading of the spec is
cheaper than the theorem.

## 1. THE IMPLICATION MAP (what each BC's satisfaction implies about zeta's zeros)

Partition per the task. "FE-layer" = satisfiable by the null structure
(Tate's thesis at the real place read backwards, WW sec 6), hence by
the FE-blindness theorem (BB/S7: the FE layer is kappa-blind, exact;
doc 37: reproducing the FE determines nothing) RH-VACUOUS on its own.

```text
BC   layer  zero-location content of satisfaction
BC1  FE     NONE. The shape law is the Gaussian deficit's Mellin data
            (NS1, hand-derived, no zero input). Null structure passes.
BC2  FE     NONE. Integer charge ledger = coset Poisson bookkeeping.
BC3  FE     NONE. Payment constants are Gaussian/theta integrals.
BC4  index* SEE SEC 1.1. As stated (per-place infeasible, global
            feasible AT THE SCANNED WINDOW a = 4.96) it is a finite
            supply-side computation: NONE. Its UNIFORM-in-a
            strengthening is where zero content enters (sec 1.1).
BC5  FE     NONE. Unique factorization, exact integers.
BC6  index  SEE SEC 1.2. As stated (independent evaluation + agreement
            a theorem): NONE by itself - agreement with a possibly
            NEGATIVE margin is not excluded by the text. Zero content
            enters only when positivity of the agreed value is added.
BC7  FE     NONE. kappa = pi at the density layer; FE kappa-blind by
            theorem - the clause explicitly disclaims FE-layer content.
BC8  FE     NONE directly. The zero-slack finding (LL/SS.4) is the
            conservation signature: it FORBIDS satisfaction by padding,
            i.e. constrains HOW a satisfier exists, not WHERE zeros are.
BC9  FE     NONE. W_inf's signedness is unconditional EF-archimedean
            data (HH, comparison-flagged in WW itself).
BC10 FE     NONE. Corollary of BC1.
BC11 FE     NONE about zeros. A carrier/formability demand on C
            (doc 14 P2): it gates WHICH objects can pose the BCs,
            not where their zeros lie.
BC12 FE     NONE. A type constraint on tr (not cardinality-valued on
            the deficit channel; deficits in (0, log 2)). Negative
            content only: it BLOCKS the naive integrality route to
            positivity on that channel - see sec 2 gap (g1').
```

Tally: ten BCs are unambiguously FE-layer/supply-side - all were
computed under F-a with zeros NEVER consumed (WW ledger), so their
truth values are theorems of the comb/Gaussian apparatus and are
logically independent of zero locations. The two candidates for index
content, BC4 and BC6, carry it only in strengthened forms.

### 1.1 BC4: does realizing the global aggregate as a trace force its positivity?

No, not as stated. Two separate gaps:

(a) BC4's certified content is A_g(4.96) = +3.03e-2 > 0 plus per-place
infeasibility - a FINITE list of supply-side numbers. A structure
reproduces them iff its trace flow matches the comb data; this is
RH-independent (the numbers were computed with no zero contact).

(b) "Realizing the aggregate as a trace" forces positivity ONLY if tr
is a POSITIVE trace (a state/dimension function) - and nothing in
BC1-BC12 demands that tr be positive. A signed trace (which BC9
actively REQUIRES on the archimedean coordinate - the cancellation is
load-bearing, a PD block is excluded) can realize any real value. So
BC4-satisfaction does not even force the scanned-window number's sign;
it CITES it. The implication chain from BC4 to zero locations begins
only at the uniform statement "A_g(a) > 0 for all a on every admissible
class" - which is NOT in the dossier (WW honest limit 1: "Nothing here
proves the global aggregate positive for all a").

### 1.2 BC6: the implication chain to doc 13's tau < 1, every gap marked

Suppose (C, tr) satisfies BC6: some pairing <W, g> has evaluation E1
(supply: Lambda_p, log q, m+ data) and evaluation E2 (independent),
with E1 = E2 a theorem. The chain to RH, as far as it goes:

```text
step 1  E2 forced nonnegative (a count/dimension/Gram norm or an
        integer > -1 per doc 14 sec 4)            [GAP g1: NOT in BC6]
step 2  => the assembled margin m+(g, a) = E1 = E2 >= 0 on the classes
        g and scales a that C actually carries     [follows from g1]
step 3  => S_N >= 0 on each edge whose shell basis the class family
        spans                                      [GAP g2: coverage]
step 4  => tau_r < 1 per edge (doc 13 pencil equivalence; needs
        BULK_r > 0 - certified on the computed ladder, open
        asymptotically)                            [GAP g3: uniformity]
step 5  uniform tau_r < 1 along the filtration <=> RH (doc 13 sec 3
        + 4', banked, both directions; doc 00 + 00a reduction)
```

GAP g1 (positivity): BC6 demands independence + agreement, not sign.
YY's P3 (a/b/c) screens for genuineness of the PAIR; even P3-DECISION
grade does not force E2 >= 0. The FF conjunction's "effectivity" clause
(doc 32/34) is exactly this demand, and it is NOT among the twelve BCs.
GAP g1' (sharpening, from BC12): the nonnegativity CANNOT come from
reading the deficit channel as a cardinality (deficits sub-quantization,
in (0, log 2)); the integer must sit at the INDEX level (chi/N(D),
doc 34 KK: integer > -1 => >= 0), with the continuum deficits inside
the renormalized h^0_ren. The positivity source is constrained to one
mechanism before it is even demanded.
GAP g2 (class coverage): the BCs constrain tr on the strict family /
certified Lorentzian face. Doc 34 sec 3, verbatim: whether the
strict-family inequality extends to the Frobenius-graph classes (HH's
cone) WHERE THE ZEROS LIVE is untested. Nothing in BC1-BC12 forces C's
class family to exhaust the doc-00 smooth core (even, real, C_c^infty,
hat h(0) = hat h(i/2) = 0, all R). A structure could satisfy all twelve
on a class family that misses the resonant directions entirely.
GAP g3 (scale uniformity): same as 1.1(b) - all certified feasibility
is scanned-window; RH needs every edge of an infinite filtration.

## 2. THE TWO DIRECTIONS

### 2.1 Forward: [exists (C, tr) |= BC1-BC12 + index inequality on its classes] => RH-at-its-classes

PRECISE FORM (the strongest true statement I can assemble from banked
results): let (C, tr) satisfy BC1-BC12, and suppose additionally
(INDEX) its BC6 pairing value is forced nonnegative on every class/
scale it carries (= h^0_ren >= 0 there, LL's identical equivalence to
the index inequality). Then for every test h in the linear span of the
carried classes, the doc-00 margin form satisfies M_R(h, h) >= 0
(steps 2-3 above; the identification of margin form with the Weil/
spectral side is doc 09 6''' + doc 13 fork (ii), banked). That IS Weil
positivity restricted to the carried test class. If the carried classes
exhaust the doc-00 core for a sequence R -> infinity, doc 00's
reduction gives RH in full; if not, one gets zero-freeness only against
the carried tests (partial: no zero whose oscillation profile is
spanned - [COMPARISON/LOGIC] doc 13's r = zero cross-correlation makes
"carried test" = "detectable zero" exact).

WEAKEST LINK, named: GAP g2 (class exhaustion). g1 is closed by
HYPOTHESIS in this direction (the task's "with the index inequality
holding"); g3 is the uniformity half of g2 (one compound gap:
"all classes, all scales"). So the forward chain is: BC-sat + INDEX
+ EXHAUSTION => Weil positivity on the core => RH, with EXHAUSTION the
unbanked step. This gap is not a new no-go - it is the actual remaining
mathematics, and it is exactly doc 34 sec 3's named open question
(strict family -> Frobenius-graph cone). M3 adds: no BC currently
witnesses it, so a candidate could pass all twelve and still be a
strict-family-only object.

### 2.2 Backward (the conservation check): does RH imply a satisfier exists?

AT STATED GRADE: YES. Construction sketch (existence, not program-legal
input - the existential quantifier in M3 ranges over mathematics, not
over F-a-compliant moves): take the null structure for the shape axis
(WW sec 6 satisfies BC1-BC5, BC7-BC12 unconditionally - no RH needed).
For BC6: on RH, the Weil form W(g * g~) is PSD on the doc-00 core
(classical equivalence, doc 00 O3 anchoring); GNS-complete to a Hilbert
space H_W carrying the scaling flow; let E2(<W, g>) := ||v_g||^2_{H_W}
(the Gram evaluation). E2 is defined from the zero-side spectral data,
not from (Lambda_p, log q, i, m+) - it meets BC6's letter ("an
evaluation INDEPENDENT of the supply data"); the agreement E1 = E2 is
the explicit formula, a theorem. INDEX holds tautologically (a norm is
nonnegative); EXHAUSTION holds (the GNS space is built on the full
core). [COMPARISON/LOGIC throughout: zeros enter as the constructed
object's material, which is the point being tested.] So at stated
grade, on RH the spectral side supplies the second evaluation
tautologically - doc 13's equivalence read backwards.

AT P3 GRADE: OPEN, and plausibly NO. The GNS satisfier is doc 38 P4's
pre-registered failure mode verbatim ("needing zero-side input - the
P1-fork in ultimate form"), and by doc 13 fork (ii) + doc 14's
conservation law, the zero side is the EF TRANSPORT of the supply side
- YY's P3-a fails (no deformation freedom independent of the zeros; the
two sides are one analytic object continued; YY rows 2/5 classified
precisely this pattern ONE-EVAL). RH gives the INEQUALITY; it does not
obviously furnish a SECOND STRUCTURE in Weil's sense (compare: RH for
function fields was true before, and independently of, any cohomology
existing - truth of the bound does not conjure the category).

### 2.3 The two-direction verdict

```text
stated grade:  BC1-12 + INDEX + EXHAUSTION  <=>  RH
               (forward: sec 2.1 via banked docs 00/09/13;
                backward: sec 2.2 GNS) - EQUIVALENT. The spec with the
               missing clause restored is EXACTLY as hard as the
               theorem: zero-shortcut CONFIRMED; the program's value is
               the reformulation's tractability, not a discount.
P3 grade:      BC1-12 + INDEX(P3) + EXHAUSTION  =>  RH, converse OPEN
               - possibly STRICTLY STRONGER (sat-stronger flag, but
               only at this grade): the program would be proving
               "a Weil-cohomology-like structure exists for zeta",
               which implies RH and may exceed it. Not an error - a
               stronger target is conservation-legal - but it must be
               priced: no satisfiability-style argument can be expected
               to run BACKWARD from RH at P3 grade.
```

## 3. THE NON-RH SOLUTION TEST (BC by BC)

Could all twelve be satisfied in a world where RH is false? The
coherent form of the counterfactual (zeta's own primes determine its
zeros, so "zeta with an off-line zero" is not a consistent object) is:
(i) which BCs are logically independent of zero locations, and (ii) the
DH model - a genuine FE-bearing object with off-line zeros - as the
certified picture of what failure looks like. [COMPARISON/LOGIC: all
DH/tau numbers below are doc 13's banked certificates.]

```text
BC1-BC3, BC5, BC7-BC12: SUPPLY-SIDE, RH-INDEPENDENT. Each was computed
  with zeros never consumed; each is a theorem about combs/Gaussians/
  exact integers. An off-line zero changes none of them. They would be
  satisfied (by the null structure, among others) in any world.
BC4 as stated: scanned-window numbers, supply-side: RH-INDEPENDENT.
  BC4 uniform-in-a: this is where an off-line zero bites FIRST.
  [COMPARISON] doc 13's DH control: on DH's living edge tau = 1.3456 >
  1 ball-certified, x^T S_N x <= -0.2822 - an off-line zero makes the
  global aggregate INFEASIBLE at its resonant scale. Failure mode:
  threading fails at some a.
BC6 as stated (agreement + independence): RH-INDEPENDENT - an honest
  second evaluation in a non-RH world would simply AGREE WITH A
  NEGATIVE MARGIN at the resonant class/scale. Agreement is symmetric;
  it certifies the value, not its sign. The dossier text nowhere
  forbids E1 = E2 < 0.
BC6 + INDEX: this is where RH bites EXACTLY. If E2 is forced
  nonnegative and agreement is a theorem, then an off-line zero gives
  [COMPARISON: doc 13 tau > 1 <=> exists h with margin < 0] a class on
  which E1 < 0 = E2 >= 0: contradiction. The structure cannot exist.
  The off-line zero's bite point is the AGREEMENT WITH A FORCED-SIGN
  EVALUATION - precisely Weil's mechanism, precisely what BC6 as
  stated omits.
```

VERDICT: SAT-WEAKER as stated. The twelve BCs are jointly satisfiable
in a non-RH world: take the null structure for the ten FE-layer
clauses; BC4's stated content is finite supply data; for BC6, any
genuine two-evaluation pair whose agreed values are unconstrained in
sign (YY's embryo q^w - 1 is the existence proof of the PATTERN at a
carrier with empty spectrum; a non-RH world version would carry signed
agreed values). The dossier is INCOMPLETE, and the missing clause is
not another shape datum - the shape axis is closed (WW: determined-and-
classical) - it is:

## 4. BC13 (the missing clause, proposed)

```text
BC13 (INDEX POSITIVITY + EXHAUSTION). The BC6 second evaluation takes
  values forced nonnegative by what they are (a dimension, a count, a
  Gram norm; per BC12 + doc 14 sec 4 the forcing integer must sit at
  the index level, not the deficit channel), and the class/scale family
  on which the agreement theorem holds exhausts the doc-00 filtration
  core (all shells, all R; equivalently: spans HH's Frobenius-graph
  cone, doc 34 sec 3). EXCLUDES: signed/indefinite second evaluations;
  strict-family-only satisfiers; scanned-window feasibility passed off
  as global.
```

With BC13: BC-satisfiability <=> RH at stated grade (sec 2.3);
=> RH at P3 grade with the converse open. Without BC13: satisfiable in
non-RH worlds; ten clauses RH-vacuous by the FE-blindness theorem, the
other two RH-silent as stated. M3's conservation reading: the dossier
correctly priced the SHAPE of the missing object at zero (null
structure passes) and stored the ENTIRE difficulty in BC6 - but BC6's
text banked the independence demand and not the positivity demand. The
difficulty did not leak; it sits in the clause the dossier has not yet
written down. E1's stamp (BC1 necessary-not-sufficient) extends to the
full dozen.

## 5. Consequences for the program (one paragraph each)

(i) The standing arrival gate (doc 39 E1) is unchanged but its scope is
now proved: passing ALL TWELVE BCs certifies shape only; the
kill-or-keep decision content of any LS3/LS4 candidate is BC13.
(ii) Doc 34 sec 3's open question (Frobenius-graph extension) is
promoted from "untested limit" to "constituent of the only clause that
distinguishes the spec from a non-RH-world satisfiable one" - the cheap
fail-closed test named there (hand-inserted unit on the graph classes)
is the direct numerical probe of GAP g2 and is the natural M-move.
(iii) The P3-grade flag (sec 2.3) should be recorded in the registry:
if the spine ever claims BC-satisfiability as a TARGET, state which
grade; at P3 grade the target may be strictly stronger than RH.

## 6. G-INT6 ledger

```text
input                          choices spent
BC1-BC12, exclusions           WW verbatim (canonical numbering)
six clauses, FF conjunction    docs 34/37/32, cited
tau/DH certificates            doc 13, COMPARISON/LOGIC ONLY - no zero
                               data enters any new claim; used solely
                               to model what BC failure looks like
GNS construction (sec 2.2)     standard functional analysis on a
                               banked equivalence; existence argument,
                               flagged as P4's failure mode itself
BC13 wording                   the ONE design choice of this memo:
                               composed from FF-effectivity (doc 32) +
                               doc 34 sec 3's named gap + WW honest
                               limit 1 - zero new mathematical content,
                               consolidation only
zeros                          NONE consumed as input; no fork_lib,
                               no freeze; all contact labeled
witnesses                      NONE (logical analysis; fail-closed:
                               nothing to gate)
```

## 7. Honest limits

- Sec 2.1's forward chain leans on doc 13's equivalence whose
  asymptotic side is a REDUCTION (doc 00 O1-O4 anchored classically),
  not a from-scratch proof; the chain is as strong as that bank.
- Sec 2.2's stated-grade backward direction constructs a satisfier
  whose BC6 reading is contestable: if the program insists BC6 already
  MEANS P3-grade independence (a defensible reading of "INDEPENDENT"),
  then the verdict shifts from SAT-WEAKER to "BC6 possibly
  unsatisfiable-as-meant in ANY world until a genuine structure is
  built" - the non-RH test then returns UNDECIDABLE-as-stated rather
  than sat-weaker, but the operative conclusion (BC13 needed; shape
  axis RH-silent) is identical under both readings.
- The ten-clause RH-independence claims are at the level of the BCs AS
  CERTIFIED (finite computations, exact identities); a future uniform
  strengthening of any of them could acquire index content.
- No new mathematics: every step is an arrangement of banked theorems;
  the memo's value is the partition, the gap names, and BC13.

## 8. Hand-off

```text
VERDICT:   SAT-WEAKER as stated (twelve BCs satisfiable in a non-RH
           world; ten FE-layer clauses RH-vacuous by the FE-blindness
           theorem, BC4/BC6 RH-silent as stated). Missing clause
           BC13 proposed (index positivity + class/scale exhaustion).
           With BC13: equivalence to RH at stated grade (zero-shortcut
           CONFIRMED, conservation law holds); at P3 grade possibly
           strictly stronger (flagged).
WEAKEST    forward chain: GAP g2/g3 - class-and-scale exhaustion
LINK:      (doc 34 sec 3's Frobenius-graph extension). The genuine
           remaining mathematics, not a new no-go.
NEXT:      the cheap probe of g2 already named in doc 34 sec 3
           (hand-inserted unit on the graph classes, fail-closed).
FILES:     research/work/AC-bc-satisfiability.md (this memo only).
```
