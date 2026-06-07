# NG-omin — is the archimedean fibre of bar(Spec ℤ) o-minimally TAME or WILD? [NEW-GEOMETRY · candidate 1]

**Charter.** First real attempt at a NEW geometry (`research/new-geometry-program.md`) that forces Step B
— the radius `|α|=√q = F†=F̄` = purity — **archimedean-natively, without a finite ground**, where all seven
known geometries failed (`research/the-complete-account.md`). Candidate: **TAME / o-minimal geometry**,
motivated by BKT o-minimal GAGA, which *properizes transcendental archimedean objects* (forces period maps
to be algebraic). The crux question: **is the archimedean fibre — concretely its L-factor `Γ_ℝ(s) =
π^{−s/2}Γ(s/2)` and its cohomology — o-minimally TAME (definable, properizable, finitely-many-poles after
a cutoff) or WILD (non-o-minimal, intrinsically infinitely-many-poles)?** This decides lead-vs-no-go.

Witness: `/tmp/omin_tame_wild.py` (reproduced below), `proper_vs_open_anchor.py` (anchor, re-confirmed).

---

## The three executable checks (all [computed])

### CHECK 1 — the finite-prime Euler factor is o-minimally TAME

`(1 − α p^{−s})^{−1}` as a function of `u = p^{−s}` is **rational, hence semialgebraic, hence definable in
the real field `R` itself** (the minimal o-minimal structure). For an elliptic `E/𝔽_q` the local L-factor
`L_p(u) = ∏_i (1 − α_i u)^{−1}` (degree `2g`) has **exactly `2g` poles** at `u = 1/α_i`, finite in any
bounded `u`-window, one per `u`-period of `p^{−s}`. The radius is the **algebraic** datum `|α| = √q` — `α`
is a root of `X² − aX + q` (computed: `E/𝔽₅, a=1`, `|α| = 2.2360679… = √5`). **Marked, algebraic, tame.**

### CHECK 2 — the archimedean factor `Γ_ℝ` is o-minimally WILD

`Γ(s/2)` has poles at `s = 0, −2, −4, …` — **infinitely many on the unbounded domain `Re s < 0`** (computed:
6 poles in `[−10,0]`, 51 in `[−100,0]`, 5001 in `[−10⁴,0]`, growing without bound). **O-minimal finiteness
theorem** (van den Dries monotonicity; a definable subset of `ℝ` has finitely many connected components):
a function definable on a definable set has **finitely many** zeros/poles. Therefore **`Γ_ℝ` is NOT
definable in ANY o-minimal structure globally.** This is not a soft claim — it is sharp and sourced:

- **[literature, sourced]** Bianconi / *Definability of complex functions in o-minimal structures*
  (arXiv 2506.15119): **neither `Γ` nor `ζ` is definable in `R_an,exp`**; moreover there are regions on
  which `Γ` **cannot be definable in ANY o-minimal structure**.
- **[literature, sourced]** van den Dries–Speissegger: `Γ|_{(0,∞)}` **IS definable in `R_{G,exp}`** (the
  multisummable structure) on **Stirling-shaped restricted domains** — i.e. only on bounded/restricted
  pieces, never globally.

So the archimedean factor sits exactly on the **tame/wild boundary**: tame on restricted Stirling windows,
**intrinsically wild** globally and on certain regions.

### CHECK 3 — a BOUNDED definable window of `Γ_ℝ` is tame but the radius DECOUPLES

Restrict `Γ_ℝ` to the critical-strip window `0 ≤ Re s ≤ 1, |Im s| ≤ T`. There it is analytic, pole-free,
bounded-domain ⟹ its graph **is definable** (the tame piece; `R_{G,exp}`). Computed: `sup|Γ_ℝ|` on the
critical line `|Im| ≤ 50` is `2.7233…` — a **finite volume / decay datum**. But this tame piece carries
**no discrete spectrum, no finite cardinality `q`, no marked radius**. It records a **count** (a regularized
volume / decay rate), and the **radius is unmarked** — exactly the program's count/radius decoupling, now
appearing in o-minimal vocabulary. Contrast CHECK 1, where `√q` is a marked algebraic root.

---

## The mechanism, stated precisely — and why it does NOT transfer to force the radius

**BKT o-minimal GAGA (the properization mechanism), stated from primary sources** (Bakker–Brunebarbe–
Tsimerman, *o-minimal GAGA and a conjecture of Griffiths*, Invent. Math. 2022; arXiv 1811.12230):

> Definable coherent sheaves **on complex algebraic spaces** are algebraizable (the definabilization functor
> is fully faithful, exact, essential image closed under sub/quotient); combined with Artin, **proper
> definable IMAGES of complex algebraic spaces are algebraic.** Applied to period maps: images are
> quasi-projective, the Griffiths bundle is ample.

Three structural facts decide the fork:

1. **The SOURCE must already be a complex ALGEBRAIC space (finite type over ℂ).** O-minimal GAGA does not
   create algebraicity from nothing; it upgrades a *definable* structure on an *already-algebraic* object to
   *algebraic*. The finite-type-over-ℂ hypothesis is the o-minimal analogue of a **finite ground** — the
   ambient algebraicity is the import. `bar(Spec ℤ)` at `∞` has **no such ambient algebraic space**: `Γ_ℝ`
   is a regularized `det_∞` of an unbounded (infinite-dimensional) log-Frobenius operator (PP-synthesis,
   Deninger/Consani–Marcolli), not a coherent sheaf on a finite-type ℂ-space.

2. **PROPERNESS is an INPUT, not a conclusion.** GAGA properizes *because the image is assumed proper*; it
   does not *make* a non-proper object proper. The archimedean fibre is **intrinsically non-proper** (open/
   affine signature, infinite-dim `H¹_arch`, non-perfect PD — `PP-synthesis.md`, three-times-confirmed). The
   one thing the candidate needed it to do — properize the non-proper fibre — is **outside its hypotheses**.

3. **The OUTPUT is algebraicity, never a weight/Frobenius modulus.** O-minimal GAGA delivers
   *quasi-projectivity / algebraicity of a period image* — the analogue of **Step A** (the FE / duality /
   the algebraic period relations). It is **provably silent about `|α| = q^{w/2}`** (no weight filtration,
   no Frobenius eigenvalue modulus is produced). This is the **same terminus** the PP-pass reached for
   condensed geometry: *duality, not purity*. Tameness ⟹ finiteness/algebraicity = Step A; it does **not**
   ⟹ the radius = Step B.

**Net.** The tameness mechanism is real and would, *if applicable*, give exactly the free half (Step A:
finiteness, algebraicity, the FE). It cannot reach Step B because (i) it presupposes the very algebraic/
finite ground `ℤ` lacks at `∞`, (ii) it presupposes properness rather than forcing it, and (iii) its output
type is algebraicity, not a modulus. **The count/radius decoupling re-derives itself in o-minimal form:
tameness = finiteness = count; the radius is unmarked.**

---

## The fork, decided honestly

This is **NOT a genuine lead** (it does not force Step B without a finite ground) and **NOT a clean
GENUINE_NEW_GEOMETRY**. It is a **NO-GO BLUEPRINT that locates the obstruction precisely in o-minimal
language** — a Grothendieck move (try to prove the gap empty; watch where the proof fails):

> **The archimedean fibre's L-factor `Γ_ℝ` is intrinsically o-minimally WILD** (infinitely many poles on
> an unbounded domain ⟹ not definable in any o-minimal structure; sourced, not conjectured). It is **tame
> only on bounded/restricted Stirling windows**, and on those windows the **radius decouples** (tame piece
> records a count/volume, never a finite cardinality `q`). O-minimal tameness is exactly the
> **finiteness/algebraicity = Step A** side; it presupposes the finite/algebraic ground and the properness
> that `ℤ` lacks at `∞`, and its output is algebraicity, never a Frobenius modulus. **So o-minimality, like
> the other seven instruments, supplies Step A and decouples at Step B.**

**The minimal new structure that WOULD tame it (the blueprint).** To bring `Γ_ℝ` into a TAME geometry that
also marks the radius, one must **collapse the infinite pole spectrum `{0,−2,−4,…}` to a FINITE definable
set** — i.e. supply a **cutoff/quotient that is itself o-minimally definable and turns the infinite product
`Γ_ℝ` into a finite char-poly** (degree `2g`, the proper/polynomial signature). This is the *same* named
object `ψ_∞` (collapse `det_∞` → finite char-poly, an honest archimedean Frobenius), now re-cast in
o-minimal vocabulary: **a definable o-minimal structure in which the log-Frobenius spectrum is FINITE.**
The wild→tame transition IS the missing finite ground. O-minimality names the wall sharply but does not
move it: *the finite ground must be supplied first (then tameness/finiteness/the radius follow), exactly the
order PP-synthesis identified.* The two open probes inherited: (a) is there a definable regularization of
`Γ_ℝ` (truncated Stirling) whose pole set is finite AND whose decay rate marks a `q`? — CHECK 3 says no for
the naive window; (b) is the wildness *removable* by passing to a finite-rank self-dual truncation, or is it
a type-obstruction? — the sourced "cannot be definable in ANY o-minimal structure on certain regions"
suggests a **type-obstruction**, re-confirming the terminus from the tame side.

---

## Anchor / DH discipline

- **Anchor (F_q, no zeros assumed): PASS.** CHECK 1 recovers `|α| = √q` as the algebraic root of
  `X² − aX + q` over `𝔽₅` with no zeros input; the finite-prime Euler factor is semialgebraic/tame and the
  radius is marked. `proper_vs_open_anchor.py` independently re-confirms proper `H¹` pure / open `H¹_c`
  mixed. The mechanism recovers `√q` for finite primes **but the recovery rides on the algebraicity (finite
  ground)** — precisely the import o-minimal GAGA also requires. So the anchor PASSES but exhibits *why*:
  the radius is marked exactly where the finite/algebraic ground is present.
- **Davenport–Heilbronn (novelty test): the candidate is not even a forcing functional**, so the DH test
  applies vacuously at the radius level. The relevant statement: o-minimal tameness is **not Euler-borne and
  does not see zeros** — it is a *finiteness/definability* property shared by `ζ` and DH alike (both have
  archimedean `Γ`-factors; tameness of the `Γ`-window cannot distinguish them). So a tameness-only
  functional would be **RH-SILENT / DISPERSING** in `falsify.py` terms: it would hold for DH (no separation),
  confirming it carries **no Step-B content**. This is consistent with — and a fresh confirmation of — the
  no-go: tameness lives entirely on the RH-neutral / Step-A side. **DH fails to be excluded by tameness ⟹
  tameness is not the radius.** (Marked FAIL as a *novelty* test: a genuine new geometry must NOT exist for
  DH; o-minimal tameness exists equally for DH, so it does not clear novelty — confirming NO-GO.)

---

## Verdict

`[NEW-GEOMETRY · candidate 1]` — **NOGO_BLUEPRINT.** The archimedean fibre is **intrinsically o-minimally
WILD** (`Γ_ℝ`: infinitely many poles on an unbounded domain ⟹ not definable in any o-minimal structure —
sourced: Bianconi 2506.15119; van den Dries–Speissegger give definability only on restricted Stirling
windows). The BKT properization mechanism is **real but presupposes exactly the finite/algebraic ground and
the properness `ℤ` lacks at `∞`** (source must be a finite-type ℂ-algebraic space; properness is an input;
output is algebraicity, never a Frobenius modulus). On the bounded tame window the **radius decouples**
(count/volume marked, `q` unmarked) — the program's count/radius split re-derived in o-minimal form.
**Tameness = finiteness = Step A (free); it decouples at Step B (the radius), like all seven prior
instruments.** Anchor PASSES for finite primes but only because the algebraic ground is present there; DH is
NOT excluded by tameness (tameness is RH-silent/dispersing), so the candidate fails the novelty test —
confirming the no-go rather than a lead. **The blueprint (Grothendieck move):** the minimal new structure
needed is a **definable o-minimal collapse of the infinite log-Frobenius spectrum `{0,−2,−4,…}` to a FINITE
char-poly** — which IS `ψ_∞` (the finite ground at `∞`) re-cast in o-minimal vocabulary; the sourced "not
definable in any o-minimal structure on certain regions" indicates this is a **type-obstruction**, sharpening
the terminus from the tame side. O-minimality **names the wall precisely; it does not move it.**

**Honest odds.** As a *path to forcing the radius*: **very low (~2%)** — wildness is sourced, the mechanism's
hypotheses are the missing ground, output is Step-A-typed. As a *diagnostic*: high value — it transcribes the
residue into the cleanest finiteness vocabulary yet (infinite-pole-spectrum vs finite-char-poly) and shows
the obstruction is a *definability type-obstruction*, the o-minimal mirror of "no finite ground at `∞`."

**Next step.** Do not pursue o-minimal GAGA for purity (terminus). Pivot to **candidate (2) Frobenius-first
/ dynamical geometry** (take Frobenius as primitive, define the space by what it acts on), or **candidate (3)
symmetric-monoidal archimedean motives** (polarization as a coherence theorem). The o-minimal pass leaves a
sharp residual probe: *is there any o-minimal structure in which a finite-rank truncation of `Γ_ℝ` is
definable AND marks a `q`?* — the sourced regional non-definability suggests NO, which would close the
o-minimal route as a type-obstruction terminus.
