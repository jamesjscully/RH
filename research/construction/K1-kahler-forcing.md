# K1 — the KEYSTONE: is `P_∞ ⪰ 0` (`c=D`) forced by a Hodge–Riemann/Kähler structure? [coherence-checked · anchored vs 𝔽_q]

**Charter:** `construction-program.md` §0 (the polarization is a duality pairing, NOT a metric), §1
C4/C5 (`P` = canonical pairing of `D`, positivity ⟺ RH), Pillar C (positivity from coherence).
**Mandate (AGENDA K1):** the whole polarized arithmetic Hodge category now rests on ONE positivity —
`P_∞ ⪰ 0` (= the archimedean `c=D`, M3b). K1 asks whether that positivity is **forced by a
Hodge–Riemann/Kähler structure** (a *geometric* datum, not the zeros), as classical Hodge theory
promises. **ANCHOR:** over `𝔽_q` the "Kähler class" = the ample class / cup product; verify `P_∞`'s
positivity follows from it with no zeros assumed; then state precisely what an archimedean Kähler class
on `S²/ℤ` must be. **Module:** `scripts/numerics/witness/kahler_forcing.py`
(run: `python3 -m scripts.numerics.witness.kahler_forcing`). **Falsifier row added** (`falsify.py`, → 50).

---

## The result is sharper than the agenda hoped — a LOAD-BEARING finding, not a clean win

The agenda's optimistic framing was: "in classical Hodge theory `c=D` is *forced* by a Kähler form via
the Hodge–Riemann relations — a *geometric* datum, not the zeros — so the keystone is *construct one
geometric form*." Executing the `𝔽_q` anchor shows the forcing is real **but factors**, and the piece
that does the actual work is, over `𝔽_q`, **literally the RH radius**. This is the honest terminus K5
asked for: the keystone *locates* the irreducible residue, it does not dissolve it.

### STEP A — the cup product `E` ALONE is INDEFINITE (the naive reading is FALSE) [computed]

The weight-1 cup product `E` (the symplectic Weil pairing — the "ample"/polarization datum on `H^1`) is
**antisymmetric**, and the Rosati form `Tr(z·z^†)` it induces on `End(H^1)` (with `z^† = E^{-1}z^T E`) is
**INDEFINITE**: signature `(2,0,2)` at `g=1`, `(8,0,8)` at `g=2`, `(18,0,18)` at `g=3` (computed). So the
cup product **by itself does NOT force the Hodge–Riemann positivity**. The naive "the ample class forces
`c=D` for free" is refuted on the anchor.

### STEP B — the positivity needs the WEIL OPERATOR `C_W` (the `(p,q)` Hodge structure) [computed]

The TRUE Hodge–Riemann positive form is `P_∞(x,y) = E(C_W x, x̄)`, with the **Weil operator
`C_W = i^{p−q}`** inserted. WITH `C_W`, `P_∞` is **positive-definite** on `H^{1,0}`: min eig `+2.03`
(`g=1`), `+4.72` (`g=2`), `+6.17` (`g=3`), all seeds — exactly Riemann's second bilinear relation. So the
forcing datum is **not `E` alone but the PAIR `(E, C_W)`** = the *polarized* Hodge structure; `C_W` (the
`(p,q)` grading) is the Kähler class that makes the indefinite cup product definite.

### STEP C — over `𝔽_q`, `C_W` IS the radius `|α|=√q` = RH (the keystone's residue) [5 Weil curves]

Over `𝔽_q` the weight-1 Weil operator on `H^1` is supplied by Frobenius being a **weight-1 Weil number**
`α = √q · e^{iθ}`: the `(p,q)` splitting / the rotation by `θ` exists **iff** there is a uniform radius
`√q` — i.e. **iff `|α| = √q`, which IS RH for the curve**. Computed (`q=2,5,7,11,13`): on-line a single
radius `√q` ⟹ `C_W` exists (`c=D`); an off-circle plant `{r√q, √q/r}` has **two different moduli** ⟹ **no
uniform radius** ⟹ **no weight-1 `C_W`** ⟹ no `c=D`. So over `𝔽_q` the **Kähler datum `C_W` and the RH
statement `|α|=√q` are LITERALLY the same datum**.

---

## The keystone factorization (the honest terminus, K5)

| ingredient | type | status |
|---|---|---|
| `E` (cup product) | GEOMETRIC, zero-free, DH-shared, **INDEFINITE alone** | **free** |
| `C_W` (Weil operator) | the `(p,q)`/**RADIUS** datum; over `𝔽_q` it IS `|α|=√q` | **= RH** |
| Hodge–Riemann: `(E, C_W)` polarized ⟹ `P_∞ ⪰ 0` on primitives = `c=D` | the implication | **formal** |

So `c=D` is **not forced "for free"**: the cup product `E` is free and the Hodge–Riemann *implication* is
formal/geometric, but the **Weil operator `C_W`** — the radius/`(p,q)` splitting that makes `E` definite —
is over `𝔽_q` **exactly the RH radius**. This is the precise Hodge-theoretic form of **M3b's
"radius-silent `(−1)^w`" lesson**: the archimedean Kähler class carries `C_W`'s **PHASE/reality** (the sign
`(−1)^w`, the weight parity) but **NOT its RADIUS** — and the radius is the whole problem. The irreducible
residue, now precisely named: **supply `C_W`'s RADIUS over `ℤ` from a geometric/Euler source, not from RH.**

---

## What an archimedean Kähler class on `S²/ℤ` must be (the K2/K3 target, precisely typed)

K1 converts the vague "construct one geometric form" into a typed object:

- **NOT a chosen positive Green form** (Arakelov: Sylvester-inertia-locked by §0; and BGS §6.3 is exactly
  where a chosen positive Green form can *fail*) —
- **but a CANONICAL Weil operator `C_W`** on the archimedean `(p,q)`-graded `H^2(\overline{S²/ℤ})`, whose
  **RADIUS** (the scale fixing `|α|=√q` at the weight-1 descent, i.e. the centre `Re s=½`) is supplied by
  the **EULER assembly** of the prime Satake products `αᵢ(p)αⱼ(p)`, NOT by a metric and NOT by RH.
- **K2 (condensed)** must PRODUCE this `C_W` as a condensed/analytic structure map (the radius-free
  reality carrier of M3c, now seen to need a radius from elsewhere);
- **K3 (forcing lemma)** is then the *formal* Hodge–Riemann implication `(E, C_W)` polarized ⟹ `c=D`;
- the **open residue** is `C_W`'s RADIUS = **M4's Euler descent** (M4r: the per-prime `√q`-analogues
  assemble the global centre against the radius-silent `(P_∞, D, c)` at `∞`).

---

## Falsifier verdict (K1 — an anchor/forcing check; the keystone FACTORS the axes)

- **EULER-ASSEMBLED — SPLIT (the keystone's content).** The cup product `E` is Euler-**silent**
  (DH-shared); `C_W`'s RADIUS (`|α|=√q`) is Euler-**borne** (the Frobenius weight); the Hodge–Riemann
  implication is **formal** (neither). K1 LOCATES the Euler content in `C_W`'s radius — M4's exact target.
- **SEES-ZEROS — YES**, but only through `C_W`: `P_∞ ⪰ 0` sees the zeros solely via `C_W`'s radius; `E`
  alone is blind.
- **INDEPENDENT — NO.** The *implication* `(E, C_W)` polarized ⟹ `c=D` is independent (Hodge–Riemann,
  geometric, no RH); **but the HYPOTHESIS** "`C_W` is the weight-1 Weil operator" over `𝔽_q` **IS**
  `|α|=√q` = RH. So K1 is **CIRCULAR over `𝔽_q` in the precise sense that the Kähler datum `C_W` = the RH
  radius** — and that circularity is the keystone's irreducible residue.

Tabled CIRCULAR (`euler_borne=Y / sees_zeros=Y / independent=N`), the FF archetype verdict; the NEW
content is the **factorization** and the precise naming of the residue.

---

## Verdict

`[coherence-checked · anchored vs 𝔽_q]` — K1 executed the keystone on the `𝔽_q` anchor and found the
honest seam: **the cup product `E` alone is indefinite** (Step A, `(2,0,2)`/`(8,0,8)`/`(18,0,18)`); **the
Hodge–Riemann positivity `P_∞ ⪰ 0` needs the Weil operator `C_W`** (Step B, min eig `+2.03…`); and **over
`𝔽_q` `C_W` exists iff `|α|=√q` = RH** (Step C, 5 curves). So `c=D` is **not Kähler-forced for free**: the
forcing **factors** as (free geometric `E`) + (formal Hodge–Riemann implication) + (the **Weil operator
`C_W`, whose RADIUS over `𝔽_q` IS the RH critical line**). The keystone thus **does not dissolve RH**; it
**locates the single irreducible geometric residue** — `C_W`'s radius — and types it precisely: an
archimedean Kähler class on `S²/ℤ` must be a canonical Weil operator whose radius is Euler-assembled from
the Satake products, not a chosen metric. **Not overclaimed:** this is the honest terminus K5 wanted, with
the residue named and handed to K2/K3/M4r, not a clean forcing of RH.

**Successors named:** K2 re-pointed (the condensed archimedean structure must produce a Weil operator
`C_W` with an Euler-assembled radius, not a Green form); K3 sharpened (the forcing lemma is the *formal*
`(E,C_W)`-polarized ⟹ `c=D` — the hardness is NOT here, it is in `C_W`'s radius); a HIGH-priority item
**K2r/M4r** — construct `C_W`'s RADIUS over `ℤ` (the centre `Re s=½`) from the Euler assembly of
`αᵢ(p)αⱼ(p)`, the one piece the Hodge–Riemann forcing does not supply.
