# NG-omin — does o-minimal TAMENESS force the radius (Step B), or only finiteness/algebraicity (Step A)? [NEW-GEOMETRY candidate #1 · DEF · sourced + falsify-anchored]

**Charter:** `research/new-geometry-program.md` (spec `P*`: a finite/dualizable archimedean fibre with a
self-map whose spectrum is rigid by a *structural symmetry*, no finite field; novelty test = force `|α|=√q`
on the `𝔽_q` anchor without zeros AND fail for DH). **Candidate:** TAME / O-MINIMAL geometry — the bet that
**BKT o-minimal GAGA properizes transcendental archimedean objects** (it forces period maps to be algebraic),
so the archimedean proper boundary might be a *tame-finiteness* and the radius forced by o-minimal
algebraicity. **Anchor:** `scripts/numerics/witness/falsify.py` (re-run live, taxonomy reproduced), R2
(`schmid_sl2_orbit_radius.py`), PP-synthesis. **Sources:** Bakker–Klingler–Tsimerman (Invent. math. 232,
2023; arXiv:1811.12230), Peterzil–Starchenko (definable Chow), van den Dries–Macintyre–Marker, van den
Dries–Speissegger.

ANGLE (the sharp question): IF the archimedean fibre could be made o-minimally tame/proper, would that
FORCE the radius `|α|=√q` (Step B) the way BKT force period-map algebraicity — or only the FE (Step A)?

---

## The decisive result, in one line

> **The candidate is a NO-GO BLUEPRINT.** O-minimality is real archimedean tame geometry and it really does
> *properize* a transcendental object — **but the object it properizes is a finite-dimensional POLARIZED VHS
> over an ALGEBRAIC base, and the positivity (polarization, Hodge–Riemann, Griffiths-bundle ampleness) is an
> INPUT, not an output.** O-minimal GAGA delivers **ALGEBRAICITY = finiteness/properness = Step A**, with the
> radius/positivity **already assumed in the polarized datum.** And the actual archimedean fibre of
> `\overline{Spec ℤ}` — the `Γ`-factor / `ζ` itself — is **provably NOT o-minimally definable** (van den
> Dries–Macintyre–Marker): it is **WILD**, the obstruction being *exactly the infinitely many poles*
> `{0,−1,−2,…}` = the same infinite-dimensional / log-Frobenius signature PP-synthesis already named. So
> o-minimality does not even *reach* the archimedean fibre, let alone force its radius.

Two independent failures, each fatal, and they point the same way: **tameness gives Step A (finiteness) and
the radius decouples again — the program-wide count/radius split, now in o-minimal form — AND the archimedean
fibre is outside o-minimality entirely.**

---

## Test (1) — In BKT, does o-minimal GAGA give Step A (finiteness) or genuinely Step B (the radius)?

**Step A only. Purity/positivity is a SEPARATE INPUT, even in BKT.** [sourced]

The BKT theorem (`o-minimal GAGA and a conjecture of Griffiths`, Invent. math. 232 (2023), arXiv:1811.12230):
*proper definable images of complex algebraic spaces are algebraic*; applied to period maps, *the image is
quasi-projective and the Griffiths bundle is ample.* Reading the input/output ledger precisely:

- **INPUT:** a **polarizable** integral **pure** variation of Hodge structures (so the period domain `D=G/V`
  is built from a **polarized** Hodge structure — the Hodge–Riemann bilinear relations / positivity are part
  of the data). The Griffiths–Schmid theorem (negative holomorphic sectional curvature of the Hodge metric in
  horizontal directions) — which is the *given* polarization — is what makes the **Griffiths bundle ample**.
  Ampleness/positivity is **carried in by the Hodge metric**, not produced by o-minimality.
- **O-MINIMALITY supplies:** **definability** of the period map. This is itself powered by **Schmid's
  nilpotent-orbit / SL(2)-orbit asymptotics** (the norm estimates near the boundary are `ℝ_{an,exp}`-definable).
- **OUTPUT of GAGA:** **ALGEBRAICITY** — a finiteness/properness statement (definable + proper ⟹ algebraic).

So o-minimal GAGA is a **finiteness theorem**: it turns "transcendental but tame + proper" into "algebraic."
That is **Step A** (the duality/finiteness/FE family) in pure form. The **radius/purity is the polarization,
which is assumed at the start.** BKT never *forces* positivity; it transports an *already-polarized* object to
the algebraic category. **Algebraicity of the period map does NOT imply purity — purity is the input.**

This is exactly the R2 result, re-derived from the o-minimal side. R2 (`schmid_sl2_orbit_radius.py`) already
proved **Schmid's SL(2)-orbit `N` gives (N1)–(N3) + the weight parity `(−1)^w`, NOT (N4) the radius**: the
SL(2)-orbit lives entirely in the **DH-shared archimedean Hodge data** (phase-only, radius-silent), and the
**one real-analytic scale it carries — the Hodge-norm growth exponent `k−w` — is a divergent metric RATE whose
renormalization needs a free constant = the missing `q`.** o-minimality is built *on top of* Schmid's norm
estimates; it inherits Schmid's phase/radius split. **Tameness packages the SL(2)-orbit asymptotics into a
definable function and gets finiteness; it cannot manufacture the `q` the SL(2)-orbit lacks.**

---

## Test (2) — Is there a tame route to `|α|=√q` over `𝔽_q` that bypasses Weil II positivity?

**No. Over `𝔽_q`, tameness/finiteness is FREE (the cohomology is already finite-dimensional and algebraic —
no o-minimality needed); the radius is Weil II = Rankin-squaring positivity, untouched by tameness.** [anchor]

The anchor is decisive precisely because over `𝔽_q` the "tameness" o-minimality would supply is **already
present for free and is still not the radius**:

- `ℓ`-adic cohomology of a smooth proper curve `C/𝔽_q` is **finite-dimensional and algebraic by
  construction** — there is no transcendental archimedean object to properize, so o-minimal GAGA has *nothing
  to do*. The finiteness (Step A) is the finite ground itself.
- The radius `|α|=√q` is **Weil II** (Deligne), whose only proof is **Rankin-squaring positivity** on a proper
  family (`sym²`, `X×X`), which is **finite-field-bound** (Kedlaya: "not very compatible" with `∞`).
- **Tameness is orthogonal to this positivity.** o-minimality is a *finiteness/definability* property; it
  produces *algebraicity*, never *a modulus*. There is no theorem of the form "definable ⟹ eigenvalues have a
  prescribed absolute value." Definability constrains the *shape* of a set (finite stratification, no
  oscillation), not the *spectral radius* of a self-map on it.

So over the anchor, the o-minimal route gives finiteness (which is free anyway) and **leaves the radius exactly
to Weil-II positivity — the wall.** The count/radius decoupling (the program's invariant) **recurs in o-minimal
form: tameness = the count/finiteness; the radius is positivity, decoupled.**

---

## Test (3) — Ruthless: is "tame ⟹ radius" genuine, or does the radius decouple again?

**It decouples again — AND, worse, the archimedean fibre is not even tame.** This is the second, independent
fatal failure, and it is the more fundamental one. [sourced — the crux fact]

**The archimedean fibre of `\overline{Spec ℤ}` is WILD (non-o-minimal):**

> **Theorem (van den Dries–Macintyre–Marker).** Euler's `Γ` restricted to `(0,∞)` — and the Riemann `ζ`
> restricted to `(1,∞)` — are **NOT definable in `ℝ_{an,exp}`.** The obstruction is the **infinitely many
> poles** `{0,−1,−2,…}` (resp. the infinitely many zeros): an o-minimal function has **finitely many** zeros
> on any interval, so a function with infinitely many poles/zeros cannot be definable in any o-minimal
> structure containing `R_an` — the **infinitude of the pole spectrum is a hard o-minimality obstruction.**

This is the **same atom** PP-synthesis isolated from the analytic side: `Γ_ℝ(s)=π^{−s/2}Γ(s/2)` is the
**regularized determinant of a log-Frobenius unbounded operator** with **infinite** pole spectrum
`{0,−2,−4,…}` — an **infinite product**, the open/affine `H¹_c` signature, infinite-dimensional cohomology.
**That infinite spectrum is *precisely* what o-minimality forbids.** The non-properness (PP), the
infinite-dimensionality (PP), and the **non-o-minimality (here)** are **one obstruction in three vocabularies**:

| vocabulary | the obstruction |
|---|---|
| PP / cohomological | infinite-dim `H¹_arch`, non-perfect Poincaré duality, no finite-weight `H²=ℚ(−1)` |
| analytic | `Γ_ℝ` = infinite product, regularized `det_∞` of a *log*-Frobenius |
| **o-minimal (this pass)** | **`Γ`/`ζ` have ∞-many poles/zeros ⟹ NOT definable in any o-minimal structure over `R_an`** |

So the bet "the archimedean proper boundary is a tame-finiteness" is **false at the root**: the archimedean
fibre is the **canonical NON-tame object** — it is the standard textbook *counterexample* to o-minimal
definability. o-minimality is a finiteness theory; the `ζ`-fibre is the prototype of archimedean *infinitude*.

**The one escape — and why it does not help.** Van den Dries–Speissegger built larger o-minimal structures
(`ℝ_{𝒢}, exp` with generalized power series) in which `Γ|_{(0,∞)}` **is** definable. But (i) this is `Γ` on a
**half-line**, a tame *germ*, not the meromorphic function with its pole spectrum — the poles (the local-factor
data, the would-be Frobenius eigenvalues) are exactly what is *thrown away* to gain definability; and (ii)
definability of `Γ|_{(0,∞)}` in `ℝ_𝒢` is **still only a shape/finiteness statement** — it carries no modulus,
no `q`, no radius. Enlarging the structure to swallow the germ **does not create a Frobenius**; it just
confirms test (1)/(2): even *granting* tameness, you get finiteness, never the radius.

---

## Falsify DH — does tameness fail for Davenport–Heilbronn? (the novelty test)

**FAIL — tameness is DH-SHARED, hence RH-silent.** The DH function has the **same `Γ`-factor / archimedean
fibre** as `ζ` (it is a linear combination of two Dirichlet `L`-functions with the same `Γ_ℝ`-completion and
the same functional equation). Therefore:

- Whatever o-minimal status the archimedean fibre has, **DH has the identical status** (same poles, same
  non-definability, same period-map / SL(2)-orbit Hodge data). This is exactly the R2 falsifier row: *Schmid's
  `N` is DH-shared, hence cannot be the discriminator.*
- A tameness-based forcing would, if it existed, apply to DH verbatim — but **DH violates RH** (Davenport–
  Heilbronn: zeros off the line). So a tame "radius forcing" cannot exist (it would prove a false statement),
  **or** tameness is RH-silent on the archimedean fibre. The latter is the case.

So the candidate **fails the novelty test**: it does not distinguish `ζ` from DH. Tameness is an archimedean
*background* property both share — it is **Step-A-flavored / DH-shared**, never the Euler-borne, zero-seeing,
radius-forcing object `P*` demands. Registered as a falsifier entry analogous to R2: **`euler_borne=False`
(the tame/Hodge archimedean datum is DH-shared and radius-silent).**

---

## Where the proof of "the gap is empty" fails — the blueprint (Grothendieck move)

The honest fork asks: try to prove *every* purity-forcing geometry imports a finite ground, and watch where it
fails. For o-minimality the failure point is **sharp and locates the minimal missing structure**:

> o-minimality is a **finiteness theory for SHAPES** (definable sets: finite stratification, no infinite
> oscillation, tame topology). It properizes by **bounding complexity**, and its outputs are
> **finiteness/algebraicity** (Step A). The **radius is a SPECTRAL MODULUS of a SELF-MAP**, a *metric/arithmetic*
> datum of an *endomorphism*, not a shape complexity. **No finiteness-of-shape theorem produces a
> prescribed-modulus theorem.** This is the count/radius decoupling stated category-theoretically: o-minimality
> lives in the **count column** (it is a *theory of finiteness*), and Step B lives in the **radius column.**

The **minimal new structure that would tame the archimedean fibre** — and the precise reason o-minimality
cannot supply it — is: an object that **collapses the infinite pole spectrum `{0,−2,−4,…}` of `Γ_ℝ` to a
FINITE char-poly** (the `det_∞ ⟶` polynomial collapse, the `log`-Frobenius `⟶` honest Frobenius lift `ψ_∞`).
That collapse is what makes the fibre o-minimally tame in the first place (finitely many poles), AND it is what
supplies a finite `q` for `|α|²=q`. **So tameness and the radius would be forced by the SAME missing object —
but o-minimality presupposes that object (a finite pole set) rather than constructing it.** The archimedean
fibre is non-o-minimal *because* it lacks `ψ_∞`; supplying `ψ_∞` is *prior to* any o-minimal statement.
**O-minimality is downstream of the finite ground, not a substitute for it.**

This is the **same terminus as R8** (no finite residue field / finite ground at `∞`), reached from a genuinely
new direction (tame topology), and it **sharpens R8's diagnosis**: the finite ground is needed not only for the
Frobenius to be algebraic but **for the archimedean fibre to be o-minimal at all.** Non-o-minimality of `ζ` is
a *new, sourced, independent witness* of the missing finite ground.

---

## Verdict

`[NEW-GEOMETRY #1 · NO-GO BLUEPRINT, collapsing to TERMINUS_STEP_A]` — **O-minimal/tame geometry does NOT force
the radius (Step B); it forces FINITENESS/ALGEBRAICITY (Step A), with positivity/purity assumed as an INPUT
(the polarized VHS, the Griffiths-bundle ampleness from the Hodge metric), exactly as Schmid's SL(2)-orbit
gives parity-not-radius (R2).** Over the `𝔽_q` anchor, tameness is **free and still not the radius** (the
cohomology is already finite/algebraic; `|α|=√q` is Weil-II/Rankin positivity, untouched). The radius
**decouples again — the program-wide count/radius split in o-minimal form** (o-minimality = the count/finiteness
column). **And the deeper, independent fatal fact:** the archimedean fibre of `\overline{Spec ℤ}` — the
`Γ`-factor / `ζ` — is **provably NON-o-minimal** (van den Dries–Macintyre–Marker: `Γ|_{(0,∞)}`, `ζ|_{(1,∞)}`
not definable in `ℝ_{an,exp}`), the obstruction being **exactly the infinitely many poles** = the same
infinite-dim / log-Frobenius / open-affine signature PP already isolated. So o-minimality does not even **reach**
the fibre. **Fails DH** (the `Γ`-factor / archimedean Hodge datum is DH-SHARED ⟹ RH-silent, not a
discriminator) — so it also **fails the novelty test for the wrong reason** (it is Step-A/background, not a
new Step-B object). **Genuinely different from a re-skin?** Partly: o-minimality is a real *new* archimedean
geometry and a real properization mechanism — but it properizes the *wrong* (finite, polarized, algebraic-base)
object and is *blocked* on the actual fibre. **The blueprint it yields:** the minimal missing structure that
would make the fibre tame is *the same* `ψ_∞` (collapse the infinite `Γ`-pole spectrum to a finite char-poly /
honest Frobenius / finite ground) — **o-minimality is downstream of the finite ground, not a substitute for
it** — giving a **new, sourced, independent witness of R8's missing finite ground at `∞`** (the fibre is
non-o-minimal *because* `ℤ` lacks the finite ground at `∞`). NOT CIRCULAR (no zeros used anywhere; falsifier
re-run live, taxonomy reproduced). **Honest odds as a path to Step B: ~0%** (a finiteness-of-shape theory
cannot produce a spectral-modulus theorem); **value as a blueprint: real** (it converts "no finite ground" into
"non-o-minimal fibre," a sharper, sourced, tame-topology statement of the same wall).

**Next step.** Close o-minimality as a Step-B route (done — terminus). The blueprint says: the radius and the
tameness are forced by the *same* missing `ψ_∞` (finite `Γ`-pole spectrum). So **do NOT seek a tame route to the
radius**; instead test candidates #2/#3 (Frobenius-first dynamical / symmetric-monoidal archimedean motives) for
whether they construct the finite pole spectrum *first* (the finite ground), after which both tameness and the
radius would follow free — order: **finite ground FIRST, tameness + positivity SECOND.** Concretely: ask whether
any of the von-Dries–Speissegger enlargements (`ℝ_𝒢`) that *do* swallow `Γ|_{(0,∞)}` retain ANY modulus/`q`
datum (they do not — they keep finiteness, drop the poles), which would *re-confirm* this terminus from the
enlarged-structure side.
