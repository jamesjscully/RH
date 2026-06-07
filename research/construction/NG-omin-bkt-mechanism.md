# NG / o-minimal-tame geometry — the BKT mechanism, and where it fails for the radius [NEW-GEOMETRY · candidate 1]

**Charter.** First real attempt at a NEW geometry that would force Step B — the radius `|α|=√q = F†=F̄` =
purity — **archimedean-natively, without a finite ground**, where all seven known geometries failed
(`research/the-complete-account.md`, `research/new-geometry-program.md`). The candidate: **tame /
o-minimal geometry**, on the bet that Bakker–Klingler–Tsimerman (BKT) o-minimal GAGA "properizes
transcendental archimedean objects" (forces period maps algebraic). This log pins down EXACTLY what that
mechanism is, finds the precise tame/wild dividing line, and tests it against the target.

---

## 1. The BKT mechanism, stated precisely [checked — real theorems]

Three layered theorems, all real, cited:

1. **Definable Chow (Peterzil–Starchenko, Duke 2013; Tame Complex Analysis).** A closed analytic subset of
   a complex algebraic variety that is **also definable** in an o-minimal structure is **algebraic**.
   Engine: a **Liouville/finiteness** theorem — *a definable holomorphic function has no essential
   singularity*, hence **entire definable holomorphic functions are exactly polynomials**, and *a definable
   real-analytic function ≢ 0 has finitely many zeros*. (arXiv 2506.15119; researchgate "Tame Complex
   Analysis and o-minimality".)

2. **o-minimal GAGA (Bakker–Brunebarbe–Tsimerman, Invent. math. 2022; arXiv 1811.12230).** For a separated
   algebraic space `S/ℂ` with its definable analytification `S^def`, the functor `Coh(X)→Coh(X^def)` is
   fully faithful, exact, essential image closed under sub/quotients. Combined with **Artin's algebraization
   theorems**, this gives the load-bearing corollary:

   > **PROPER definable images of complex algebraic spaces are algebraic.**

3. **Definability of period maps (Bakker–Klingler–Tsimerman; Bakker–Brunebarbe–Klingler–Tsimerman, mixed
   case).** A period map of an admissible (graded-polarized, integral) VHS is **definable in `R_an,exp`**.
   The definability comes from giving the arithmetic quotient `Γ\D` a definable structure **via Siegel
   sets** — a **bounded fundamental domain** in the relevant directions — plus a fine description of the
   asymptotics **near the boundary** (the bounded-domain restriction is exactly where `R_an` is o-minimal).

**The mechanism, distilled.** The period map `φ : S → Γ\D` is *transcendental* (an integral of forms, no
algebraic formula) but becomes **DEFINABLE** in `R_an,exp` because (a) the universal cover sees only
restricted analytic functions on a Siegel set (bounded), and (b) `exp` handles the nilpotent-orbit
boundary asymptotics. Then o-minimal GAGA + Artin **converts (definable + PROPER) ⟹ ALGEBRAIC**. So:

> **O-minimality converts archimedean transcendence into algebraicity/finiteness — but ONLY for objects
> that are (i) DEFINABLE and (ii) PROPER. Properness is an INPUT, not an output.** O-minimality supplies
> *tame finiteness* (the Definable Chow/Liouville finiteness, the o-minimal cell decomposition); Artin
> algebraization supplies the *properness→projectivity* step. The o-minimal structure does **not
> manufacture** properness — it converts an *already-proper* definable image into an algebraic one.

This is the decisive structural fact for the verdict (§4).

---

## 2. The exact tame/wild dividing line [checked — and it is sharp]

The dividing line is the **finiteness of the definable subsets of `ℝ`**: every definable subset of `ℝ`
in an o-minimal structure is a finite union of points and intervals. Consequences, all checked:

| object | domain | tame (o-min. definable)? | reason |
|---|---|---|---|
| `sin`, `cos` | whole `ℝ` | **WILD** | infinitely many zeros → infinite discrete definable set, forbidden |
| restricted `sin↾[0,2π]` | bounded | **TAME** | `R_an` is o-minimal on restricted analytic functions |
| `Γ(x)` | `(0,+∞)` | **TAME** in `R_{G,exp}` | NO poles there; `logΓ` is log-convex, multisummable-series-definable (arXiv 2506.15119: `logΓ(x)=(x−½)log x − x + ½log 2π + φ`, `φ∈R_G`). **NOT** definable in `R_an,exp`. |
| `Γ(s)` | whole line / `ℂ` | **WILD** | **infinitely many poles** at `0,−1,−2,…` → infinite discrete definable set, forbidden in *any* o-minimal structure |
| `Γ_ℝ(s)=π^{−s/2}Γ(s/2)` | critical strip / whole `s` | **WILD** | poles `{0,−2,−4,…}` infinite |
| `ζ(s)` | bounded region / `Re s>1` strip | **TAME** (constructible: a structure making `ζ` definable exists, even one with both `Γ`,`ζ` — achieved 2024) | restricted to a region with finitely many zeros |
| `ζ(s)` | whole critical line `Re s=½` | **WILD** | infinitely many zeros (the very object of RH) → infinite discrete set, forbidden |

[computed — `scripts`-level check, this log]: confirmed `Γ_ℝ` blows up at `s=0,−2,−4,−6` (poles `~2e12…1e13`),
i.e. the pole set is genuinely infinite-discrete; and the `𝔽_q` anchor local factor `L_p(T)=1−aT+qT²`
(`q=7,a=3`) has exactly **2** zeros with `|α|=√7=2.6458` (proper/pure) — a **finite** definable set.

> **The dividing line is EXACTLY proper↔open / polynomial↔infinite-product:** a **proper** fibre gives a
> **polynomial** local factor (degree `2g`, **finitely many** zeros) — a *tame* definable set; the
> **archimedean** `Γ_ℝ` factor is an **infinite product** with **infinitely many** poles — a *wild*,
> NON-o-minimally-definable set on the unbounded/critical domain. "**Tame = proper**" and "**wild =
> open/non-proper**" is a **GENUINE correspondence**, not an analogy. It coincides exactly with the M2d /
> R6–R8 / PP signature the program already isolated.

---

## 3. Anchor on `𝔽_q` — does o-minimality recover `√q` without assuming zeros? [computed]

The `𝔽_q` local factor is a polynomial — already tame, already finite, **with no o-minimal input needed**.
O-minimality adds nothing on the finite-prime side: the Weil/Deligne radius `|α|=√q` there comes from
**Rankin positivity on the proper family** (Weil II), not from any tameness. O-minimal GAGA's content
on `𝔽_q`-geometry is *empty* (everything is already algebraic and finite). So:

> **ANCHOR: o-minimality does NOT recover `√q` by a new mechanism — over `𝔽_q` the polynomial factor is
> already tame/finite/algebraic, and the radius is supplied by the finite-field Rankin positivity, not by
> tameness. PASS as a *consistency* check (tame = proper = pure holds), FAIL as a *forcing* (tameness is
> downstream of properness, which is downstream of the finite ground).**

This is the same split the program found everywhere: tameness ↔ Step A finiteness/duality; the radius is
Step B and decouples.

---

## 4. Does tame-ness FORCE the radius (Step B), or only the FE (Step A), or fall outside o-minimality?

**It falls OUTSIDE o-minimality at the exact place the radius lives — a clean NO-GO with a sharp blueprint.**

The reasoning chain, ruthlessly:

- **(a) The target object is WILD on its own domain.** The radius `|α|=√q` lives at the **archimedean
  place**, encoded by `Γ_ℝ(s)` on the **critical strip / unbounded `s`**, and equivalently by the zeros of
  `ξ(s)` on `Re s=½` — both have **infinitely many** poles/zeros, hence are **NOT definable in any
  o-minimal structure** on that domain (§2). The very feature that *is* RH (infinitely many critical zeros)
  is the feature that **forbids o-minimal definability**. BKT properizes *definable* objects; the
  archimedean fibre is **not definable** where it matters. **The bet's premise fails at the door.**

- **(b) Even granting definability, properness is an INPUT, not an output.** BKT's algebraization is
  "**PROPER** definable images are algebraic." O-minimality + Artin convert *already-proper* transcendental
  objects to algebraic ones; they do **not create** the proper boundary. But our entire residue (PP-synthesis,
  R6–R8) is precisely the **missing proper boundary** of the archimedean fibre. So even on a bounded region
  where `Γ_ℝ` *is* tame, o-minimal GAGA needs the proper compactification **handed to it** — which is `ψ_∞`,
  the unconstructed object. **Tameness is downstream of properness; it cannot supply it.** Period maps work
  because the VHS *comes from a proper algebraic family over a quasi-projective base* — the properness is
  imported from algebraic geometry over a field, exactly the finite ground `ℤ` lacks at `∞`.

- **(c) Where tameness DOES land: Step A, the FE/finiteness — and only on bounded pieces.** On a *bounded*
  region the period-type data is tame, giving o-minimal finiteness (cell decomposition, Definable Chow
  finiteness, bounded transcendence). This is the **count/duality** side — Step A — and it is precisely the
  RH-silent half (`ξ(s)=ξ(1−s)` is a tame symmetry of a definable bounded piece; it holds at every radius).
  Tameness gives **finiteness of the zero count in a box** (a Jensen/argument-principle finiteness), never
  the **location** `Re s=½`. This is the **count/radius decoupling in o-minimal form**: o-minimality bounds
  the *number* of zeros in a definable region; it is structurally blind to their *radius/line*.

> **FORCES_RADIUS verdict: NO_GO.** Tameness does not force `|α|=√q`. It does not even force the FE as a new
> mechanism (the FE is a bounded-domain tame symmetry, Step-A-only and already free). The radius is wild —
> it lives exactly where o-minimality forbids definability (infinitely many critical zeros) — and the one
> thing o-minimal GAGA could give (algebraicity) requires **properness as an input**, which is the missing
> object. **O-minimality is a finiteness theory for ALREADY-PROPER definable objects; it cannot
> manufacture the proper boundary that the radius requires.**

---

## 5. Falsify DH [computed/structural — PASS]

Davenport–Heilbronn `F(s)` has **no Euler product**, hence no proper local-factor structure and no VHS /
period map to be definable about. There is no admissible polarized VHS whose period map would be the
carrier, so the o-minimal GAGA machine has **no object to act on** — the candidate geometry **fails to
exist for DH**, exactly as required by the novelty test. Moreover DH has **zeros off the line** and **on
it**: its critical-zero set is still infinite-discrete (wild), so it too is non-definable on the line —
o-minimality draws **no** distinction between `ζ` and DH at the radius (both wild). This is the sharp way
tameness fails the novelty test as a *forcing*: it would be **blind to the very difference** (Euler product
⟹ on-line) that RH is about. **PASS (fails for DH) — but vacuously, because it forces nothing for `ζ` either.**

---

## 6. What minimal new structure would tame it (the Grothendieck blueprint)

The NO-GO **locates itself precisely** and hands the next move:

> The archimedean fibre is **wild** because `Γ_ℝ` has **infinitely many poles** on the unbounded critical
> domain = **infinitely many archimedean "zeros/weights"** = the **infinite-dimensional `H¹_arch`** of
> PP-synthesis = the **open/affine signature** = the **missing proper boundary**. To make it **tame
> (definable, finitely many poles, polynomial factor)** is **exactly** to collapse the infinite product
> `Γ_ℝ` to a **finite char-poly** — i.e. to construct the **proper boundary / finite ground `ψ_∞`**.

So o-minimality does **not** evade the wall; it **renames it in finiteness language and confirms it from a
seventh direction**: *the obstruction is precisely that the archimedean fibre is NON-o-minimally-definable
on the radius-domain (infinitely many critical poles/zeros), and o-minimal GAGA cannot remedy this because
it needs properness/definability as input.* The minimal new structure required is **the same `ψ_∞`**:
a finite-dimensional, proper (tame, finitely-many-zeros) archimedean fibre. **Tameness becomes a
diagnostic test for `ψ_∞`, not a construction of it:** *`ψ_∞` exists ⟺ the archimedean fibre is o-minimally
tame on the critical domain.* Currently it is provably **wild** there.

---

## 7. Verdict

`[NEW-GEOMETRY · candidate 1 — o-minimal/tame]` — **NOGO_BLUEPRINT.** The BKT mechanism is real and
precisely understood: o-minimality + Artin convert **(definable + PROPER)** archimedean-transcendental
objects to **algebraic/finite** ones (period-map images quasi-projective). The tame/wild dividing line is
**sharp and is exactly proper↔open**: a proper fibre = polynomial local factor = **finitely many** zeros =
tame; the archimedean `Γ_ℝ` = infinite product = **infinitely many** poles = **WILD** on the unbounded
critical domain — non-definable in *any* o-minimal structure ("tame = proper, wild = open/non-proper" is a
**genuine correspondence**, not analogy; it coincides with M2d/R6–R8/PP). **The radius lives exactly where
o-minimality forbids definability** (infinitely many critical zeros = the content of RH), and even granting
definability, **properness is an INPUT to BKT, not an output** — o-minimality cannot manufacture the proper
boundary `ψ_∞` that the radius requires. So: tameness forces neither the radius (Step B) nor a new FE; it is
a **finiteness theory for already-proper objects** that, applied honestly, **renames the wall in
finiteness/definability language and confirms it from a seventh direction** — the missing object is exactly
"make the archimedean fibre o-minimally tame on the critical domain = collapse `Γ_ℝ` to a finite char-poly
= `ψ_∞`." **DH: PASS (no Euler product ⟹ no VHS ⟹ no object), but vacuously — o-minimality is blind to the
`ζ`/DH difference at the radius (both wild), so it fails the novelty test as a *forcing*.** **Not circular**
(no zeros imported). **The honest gain: a precise NO-GO that converts `ψ_∞` into a definability criterion
and supplies the blueprint — the new structure must make the critical archimedean fibre tame, which is
forbidden as long as `H¹_arch` is infinite-dimensional / the fibre is open.**

**Honest odds.** As a path to forcing the radius: **~0%** — the target is provably wild on its own domain,
and BKT needs properness as input. As a **diagnostic/blueprint**: high value — gives the cleanest finiteness
characterization of `ψ_∞` yet ("o-minimally tame on the critical strip"), and confirms the wall a seventh way.

**Next step.** Stop seeking o-minimality as a *forcing* (provably wild at the radius). Either (i) test
candidate (2) Frobenius-first/dynamical geometry, where properness/finiteness is taken primitive rather
than required as input; or (ii) sharpen the diagnostic: is there a *bounded* tame model of the critical
strip (a finite definable truncation of `Γ_ℝ`) whose Definable-Chow algebraization marks a radius — or does
every bounded truncation give finiteness with the radius unmarked (re-confirming the count/radius split in
o-minimal form, closing tameness as a type-obstruction terminus)?
