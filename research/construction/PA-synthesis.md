# PA-synthesis — the radius attack: 6 creative angles, judged

**Mandate.** One open ingredient of the construction: a radius-giving finite ground at the
archimedean place (R8/R10 — the 𝔽₁ purity input). Compactness/finiteness gives the COUNT; the
RADIUS `q^{w/2}` is a separate input of a type that is NOT cardinality/continuum/length/index.
Six angles attacked it. This file judges them honestly.

**Verification done.** All three named witness modules run clean and self-classify as the JSON
claims (`von_neumann_typeII1.py`, `recouple_count_radius.py`, `doubled_place_ghost_prime.py` all
EXIT 0, asserts pass). M4r's determinant-/pairing-neutral redistribution (the load-bearing
counterexample every angle re-derives) is confirmed in `M4r-radius-descent-assembly.md`: the
config `{4.475, 2.011, 2.011, 4.475}` has `∏|α|=81 ✓`, FE-pairings `{9,9} ✓`, yet is OFF the even
split — invisible to every determinant/trace/pairing datum.

---

## 1. Is there a REAL LEAD?

**No.** Zero of the six angles supplies the radius. The verdicts:

| angle | gives_radius | anchor (F_q→√q w/o zeros?) | DH litmus | verdict |
|---|---|---|---|---|
| II₁ trace (Connes spectral) | no | FAIL (reads L²-avg, not max) | **FAIL** (trace exists over any measure) | DEAD_END |
| char-1 tropical fixed-point | no | FAIL (scale-covariant) | PASS (lattice piece only) | DEAD_END |
| single archimedean F_inf re-couple | circular | PASS-as-negative | PASS | DEAD_END (CIRCULAR) |
| q→1 tangent (speed not cardinality) | circular | FAIL (consumes √q to return slope) | PASS (inherited) | DEAD_END (CIRCULAR) |
| local-arch RS positivity (Γ_R / P_inf) | no | FAIL (rescale-invariant) | **FAIL** (Γ_R is DH-shared) | DEAD_END (DISPERSING) |
| doubled "ghost prime" (p,q)+c | no | PASS-but-pins-to-ground-field | FAIL on furnished datum | DEAD_END |

No angle clears all three bars (anchor without zeros + fails-for-DH + non-circular). Two angles
(II₁ trace, local-arch RS) additionally **fail the DH litmus** — they are strictly weaker than they
look, because the object they build exists over DH spectral data too. Two (re-couple, q→1) are
explicitly **CIRCULAR** — they reduce to `F F† = q·Id` = purity = RH, or consume `√q` to return
the exponent. One (char-1) is scale-covariant by construction. One (doubling) raises the DEGREE
(a finer count) not the BASE (the radius).

---

## 2. The SHARPEST unifying reason (all dead-end)

A single mechanism kills all six, and it is the same one R8/R10/M4r already isolated, now
stress-tested from six independent creative directions and surviving each:

> **Every archimedean structure one can build supplies the COUNT (a trace / determinant /
> geometric-mean / averaged-moment / degree / location-exponent) and is provably BLIND to the
> RADIUS (the per-eigenvalue modulus bound `|α_i| = q^{w/2}`), because the radius is the
> AM–GM EQUALITY CASE / the SCALE, and every available archimedean invariant is either an
> AVERAGE (det, trace, L²-norm — fixes only the geometric/arithmetic mean) or SCALE-FREE BY
> NORMALIZATION (the II₁ trace `τ(1)=1`; the homogeneous FE fixed-set; the Γ_R-form invariant
> under uniform rescale).**

The structural decomposition that makes this exact (from the re-couple angle, confirmed in
`recouple_count_radius.py`):

- **COUNT is additive** — a trace / Lefschetz number ~ `q^n`, fixes `(det F)^{1/2g} = q^{1/2}`,
  the GEOMETRIC MEAN of the moduli.
- **RADIUS is multiplicative** — the EQUALITY case `|α_i| = q^{1/2}` for EVERY `i`.
- Over **𝔽_q** these fuse because `F = x^q` is a **ring endomorphism** whose single arithmetic
  `q` is simultaneously the field cardinality (count, trace-source) and the q-th-power scaling
  (radius, modulus). One `q`, two roles, by construction.
- At **infinity** there is NO scaling field-endomorphism: the counting/Galois maps (id,
  conjugation) are **isometries** (modulus 1, computed), and the scaling character `|·|^s` has
  **no fixed points** (no count). The two roles are carried by *orthogonal* operators. The only
  relation that re-fuses them — `F_inf F_inf† = q·Id` — **IS** purity = Weil/Connes positivity =
  RH. Substituting it is circular.

Why this is a **type** fact, not a contingent failure (R8): the missing datum is a finite
constant-field **cardinality** `|κ(t=0)| = q > 1` under the conjugate pair. The doubling angle
proves degree-`d` over 𝔽₁ gives norm `1^d = 1` for ALL `d` — raising the degree never raises the
base. The q→1 angle proves `1^anything = 1` so the value at the 𝔽₁ point determines nothing, and
Spec ℤ has no q-interval to differentiate along. The II₁ angle proves the continuous-dimension
finiteness (`τ(1)=1`) is scale-free *by the very normalization that defines II₁ finiteness*.
**The finiteness that gives discreteness/count cannot, by its defining normalization, see a scale.**

**This is a STRONGER terminus than R8/R10 standing alone.** R8 named the gap (no finite residue
field at ∞). These six angles are the adversarial closure: the gap survives (i) a genuinely
different TYPE of finiteness (II₁ continuous dimension — the one type that passes R8's type table
as a type), (ii) a self-consistency/fixed-point reframing (no cardinality needed), (iii) a
single-operator count↔radius re-coupling (the most direct attack on the decoupling), (iv) a
derivative/speed reframing (escape the cardinality table via a rate), (v) a local-archimedean
positivity distinct from the global edge, and (vi) a degree/base reframing (𝔽₁ ghost prime).
Each was BUILT and COMPUTED, not hand-waved; each fails on a *named, decidable* axis. That is the
discipline's verdict: **the count↔radius decoupling at the archimedean place is robust across all
known and these six creative angles** — it is not an artifact of any one framing.

---

## 3. Honest bottom line

**The radius is a confirmed irreducible open ingredient — NOT a lead.** The precise reason: at the
archimedean place the COUNT and the RADIUS are carried by orthogonal data (additive trace /
isometric Galois vs multiplicative scaling), the 𝔽_q ring-endomorphism `x^q` that fuses them has
no archimedean analogue, and the only relation that re-fuses them (`F_inf F_inf† = q·Id`) is purity
itself = RH. Every average/normalized/homogeneous invariant fixes the geometric mean (the count),
never the per-eigenvalue equality case (the radius). **A restatement of RH is not a lead, and four
of six angles reduce to exactly that restatement.**

### The ONE not-yet-tried synthesis worth a single more attack

The six angles *converge* on a single residue that none of them is, but that all of them point at —
and which is genuinely NOT yet built:

> A **SCALE-SENSITIVE positivity** — a Hodge–Riemann bilinear relation at infinity whose
> **EQUALITY CLAUSE** (not its inequality, not a trace, not a determinant) is the per-eigenvalue
> modulus bound `|α_i| = q^{1/2}`, acting as a **polarization on the continuous-dimension module**
> (the II₁ spectrum), such that its equality clause is **provably unavailable** without an
> 𝔽_q-deformation germ.

This is the *intersection* of the residues the angles individually hand off:
- II₁ angle: "the next object must be a SCALE-SENSITIVE positivity, not any normalized trace."
- re-couple angle: "must enforce the AM–GM EQUALITY case, not the determinant constraint."
- char-1 angle: "demand the lattice be SELF-DUAL under the polarization (unimodular, D-self-dual)
  — does principal-polarization force `|α|=q^{1/2}`?"
- q→1 angle: "is there a q→1 invariant of the MODULUS BOUND (on-circle) that admits a germ at q=1
  without an 𝔽_q-interval?"

**The honest caveat — why this is one attack, not a program:** the strong prediction (from the
Rosati/Hodge-index thread, M3/M4r/K1) is that this too is **CIRCULAR** — the polarization
positivity's equality clause **IS** the radius `F F† = q·Id`, not a forcing of it. Three of the
six angles already predict this outcome explicitly. So this is a *decidable test of circularity*,
not a hopeful lead: build the equality-clause positivity on the II₁/Connes spectrum and check
whether its EQUALITY case is `F F† = q·Id` (circular, terminus confirmed) or a SEPARATE coherence
(e.g. a primitivity / Lefschetz-decomposition equality not equal to Weil positivity — the first
genuine lead).

### (a)–(e) one-liners

- **(a) Leads found:** none. 0/6 supply the radius; 2/6 fail the DH litmus, 2/6 are explicitly
  circular, 1/6 scale-covariant, 1/6 raises degree-not-base.
- **(b) Sharpest unifying reason:** every archimedean invariant is an AVERAGE (det/trace/
  geometric-mean) or SCALE-FREE BY NORMALIZATION, so it fixes the COUNT (geometric mean of moduli)
  but is blind to the RADIUS (AM–GM equality case); the 𝔽_q ring-map `x^q` that fuses count and
  radius has no archimedean analogue, and the only relation re-fusing them is `F F†=q·Id` = RH.
- **(c) Confirmed terminus:** the radius `q^{w/2}` is the irreducible open ingredient — a finite
  constant-field cardinality `q>1` under the conjugate pair, of a type (a SCALE) that no count/
  trace/degree/normalized-dimension at the archimedean place can manufacture (R8 type obstruction,
  now adversarially closed across 6 angles).
- **(d) One decidable next step:** build a SCALE-SENSITIVE Hodge–Riemann positivity on the II₁/
  Connes continuous-dimension module and test whether its EQUALITY CLAUSE equals `F F†=q·Id`
  (circular → terminus confirmed) or is a separate primitivity/Lefschetz equality (first genuine
  lead). Predicted circular by M3/M4r/K1.
- **(e) Honest odds:** the synthesis attack is ~10–15% to be non-circular (the prior from three
  independent angles is "predicted circular"); the terminus itself is robust. Most likely outcome:
  the test confirms the irreducible open ingredient rather than opening it.
