# 03 — Investigation: is the integrality–summability dichotomy fundamental?

Status: INVESTIGATION / proof-scoping, 2026-06-29. Decision-support for a
possible pivot (user-requested: "investigate proving the dichotomy fundamental;
no full pivot yet"). This is NOT a cycle deliverable, NOT a no-go in the bank,
NOT a sub-object. It scopes whether the doc-02 dichotomy can become a theorem,
states the candidate, the proof routes, the quantification class, the risks, and
a recommendation. Carries one new Census witness (gf_dichotomy_jump_density).

## The candidate theorem (two-sided)

```text
Setup. A DIMENSION THEORY assigns to the cohomology of a divisor (equivalently
to the truncations ||HZ||_n / the tower entries Z/k) an integer dimension, such
that the diagonal self-intersection on the self-product, <Delta,Delta>, is the
zeta-regularized total of the dimension tower (the prior arc's doc 18 model:
in the DERIVED theory <Delta,Delta> = Sum_reg log k = zeta'(0)).

CANDIDATE THEOREM. For every dimension theory in the class C (additive /
localizing, integer-valued; defined below):
  (A)  if it is SCALE-AWARE -- its dimension tracks the entropy log_b(size) to
       O(1) -- then its regularized total DIVERGES (defect Dirichlet series has
       a simple pole at s=0, residue proportional to 1/log b != 0); no finite
       integer intersection number exists;
  (B)  else it is SCALE-BLIND -- invariant under the scaling that separates
       divisors -- and carries no intersection content at all.
In neither case is there an integer-valued intersection form carrying the
archimedean datum zeta'(0). Equivalently: integrality and archimedean
regularization cannot coexist in one additive dimension theory over Z.
```

## Side A — the new, provable part (the scale-aware horn)

Proof structure, four steps; the combinatorial core is now Census-certified:

```text
A1. EFFECTIVE => LOG GROWTH. An effective integer dimension counts a minimal
    generating set; a balanced-b generating set of size d covers ~ b^d
    elements, so covering a size-N object needs d = log_b N + O(1). CC Prop 3.3
    is the exact instance: dim ||HZ||_n = ceil(log_3(2n+1)). [Forced by
    counting. Grade: Reading + Certified instance.]

A2. INTEGER + LOG-TRACKING => GEOMETRIC JUMPS, density EXACTLY 1/log b.
    The jump set J = {k : D(k) > D(k-1)} of any integer monotone D = log_b k +
    O(1) is geometric: #{jumps <= K} / log K -> 1/log b. CENSUS-CERTIFIED this
    cycle, universal across ceiling / floor / round / offset staircases and
    bases b=2,3, to machine precision (relerr 0.0000):
      gf_dichotomy_jump_density  [ALL PASS, exit 0].
    The scale-blind controls (constant, identity) do NOT track => confirms
    "tracks log_b" is exactly the hypothesis that forces the geometric jumps.
    [Grade: Census (exact integer arithmetic, k <= b^16).]

A3. GEOMETRIC JUMPS => SIMPLE POLE AT s=0. The atom (jump) part of the defect,
    Sum_{k in J} k^{-s} ~ c^{-s}/(1 - b^{-s}), has a simple pole at s=0 with
    residue 1/log b; the complementary log-periodic sawtooth is regular at s=0.
    So the defect series D_delta(s) = Sum (D(k)-log_b k) k^{-s} has a simple
    pole at s=0, residue ∝ 1/log b != 0. [Certified for the ceiling:
    prime_cc_quantization_defect, residue -1/(2 log b). The mechanism depends
    only on A2 (geometric atoms), now shown shape-independent.]

A4. => DIVERGENT REGULARIZED TOTAL. Sum_reg D = (1/log b)(1/2 log 2pi) [finite
    log-part] + D_delta(0) = infinity. No finite integer <Delta,Delta>. QED(A).
```

**The single genuine obligation.** A1, A2 (Census), A3-for-ceiling (Certified)
are in hand. The one open analytic step is A3 for GENERAL staircases: "the
sawtooth part of (integer staircase − log_b) is regular at s=0." This is a
self-contained, classical-flavor lemma (Mellin transform of a bounded
log-periodic function; its only s=0 contribution is the geometric atom set).
Low risk; it is the concrete next-cycle task. **Side A reduces to this one
elementary Dirichlet lemma.**

## Side B — already a theorem (the scale-blind horn)

```text
The summable / regularizable additive invariants are exactly the CONTINUOUS
(filtered-colimit-preserving) localizing invariants, and these are SCALE-
INVARIANT by theorem: Efimov, continuous K-theory / "K-theory of large
categories", arXiv:2405.12169 (the prior arc's doc MM: "Efimov traces
scale-blind by theorem", = FF.1 one categorical level up). A scale-invariant
trace cannot distinguish divisors of different degree, so it carries no
intersection content. Side B needs no new proof -- it is cited.
```

## The load-bearing definition: the class C (scope honesty)

```text
C = additive / localizing, integer-valued invariants. This class CONTAINS every
construction the program has tested across all venues: CC's integer dimension,
dim_S, THH/Bokstedt towers, K-theory ranks, Euler characteristics, Bost-Connes,
Borisov, Efimov continuous traces. The theorem quantifies over C and is SILENT
outside it.

OUTSIDE C: a NON-ADDITIVE, or non-effective, integer intersection form. That is
exactly where a construction -- if one exists -- must live.

THE SQUEEZE (the sharp form of the question). The CHARTER's success spec S1
demands the object be CANONICAL / forced / no-choice. Additive/localizing
invariants ARE the canonical ones; non-additivity means a noncanonical choice,
which S1 forbids as a category error. So:
    fundamentality(A+B): no canonical (additive) dimension theory gives the
                         integer intersection form;
    rigidity(S1):        the object must be canonical.
If these close, the object is impossible WITHIN the canonical class -- the
CHARTER's bounded-negative terminus. The only escape is a canonical-but-
non-additive integer intersection form, which is exotic and itself in tension
with S1. This convergence (fundamentality meets rigidity) is the strongest
internal evidence the dichotomy is real.
```

## Risks (honest weak links)

```text
W1 (low). Side A's general-staircase sawtooth lemma (A3) unproven for shapes
   other than the ceiling. Mitigation: standard Mellin; the combinatorial core
   (A2) is already universal. The concrete next-cycle deliverable.

W2 (MEDIUM -- the real weak link). The identification "<Delta,Delta> = the
   regularized total of the dimension tower" rests on the prior arc's doc-18
   model (derived theory). For the INTEGER theory the analog must be checked:
   does the integer self-intersection genuinely equal Sum_reg of the integer
   dims, or could the square's structure regularize differently (e.g. a
   2-variable zeta with its own continuation that is finite where the 1-variable
   one poles)? This is the CC product-joint that 2205.01391 does NOT build
   (doc 02 A), so the model is currently an analogy. Grade: Reading. Must be
   pinned before the theorem is claimed.

W3 (scope, not a flaw). Fundamentality is RELATIVE to C. It does not exclude an
   exotic non-additive construction; it proves no ADDITIVE/canonical route
   works. This is a strong, bounded result -- and it does NOT disprove RH
   (existence => RH, not iff). State the scope; do not overclaim "RH-grade
   impossibility".
```

## Recommendation

```text
PURSUE, but do NOT pivot yet. The dichotomy is plausibly a provable BOUNDED
fundamentality theorem: side B is already proven (Efimov); side A reduces to one
elementary Dirichlet lemma whose combinatorial core is Census-certified this
cycle; and the class C contains every tested construction. The squeeze
(fundamentality meets the rigidity spec) is the strongest signal yet that the
wall is structural, not a list of failed machines.

GATE THE PIVOT on closing the two weak links in ONE focused cycle:
  (1) prove A3's sawtooth lemma for general staircases (W1, low risk);
  (2) pin the W2 identification: does the integer self-intersection on the
      self-product genuinely equal the regularized dimension tower, or does a
      2-variable continuation escape the pole? This is the load-bearing
      question -- if a 2-variable zeta regularizes the divergence (finite where
      the 1-variable poles), the dichotomy LEAKS and side A is incomplete.

If (1) and (2) both hold, THEN pivot: write the fundamentality theorem as the
program's bounded-negative result (route-dead within the canonical class,
RH-neutral). If (2) leaks, the leak IS the construction handle -- the 2-variable
regularization would be the missing self-product structure, and the program
swings back to positive. Either way, (2) is the decisive next probe.
```

## Witness

```text
Census (new, lead-run this cycle, exit 0):
  python3 -m scripts.numerics.witness.gf_dichotomy_jump_density   [ALL PASS]
  -- universal geometric jump density 1/log b across ceiling/floor/round/offset
     staircases, bases 2 and 3 (relerr 0.0000); scale-blind controls excluded.
     Certifies A2 (the combinatorial core of side A).
Certified (reused): prime_cc_quantization_defect -- A3 for the ceiling
  (pole residue -1/(2 log b)).
Cited (literature theorem): Efimov arXiv:2405.12169 -- side B.
```

## Next (the gating cycle, if approved)

Cycle 2': close W1 (general sawtooth lemma) + W2 (the 2-variable identification
-- does a self-product zeta escape the s=0 pole?). W2 is the decisive probe: it
decides whether the dichotomy is fundamental (=> bounded-negative pivot) or
leaks at the 2-variable level (=> the leak is the construction handle, swing
positive).
