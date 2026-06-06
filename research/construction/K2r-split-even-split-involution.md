# K2r-split — is the EVEN SPLIT forced by a `*`-involution (a DUALITY, not a metric)? [coherence-checked · anchored vs 𝔽_q / Δ]

**Charter:** `construction-program.md` **§0** (the decisive design law: the polarization must be
**CATEGORICAL — a duality pairing / `*`-involution — NEVER a metric**; metrics are Sylvester-inertia
-locked, dead), Pillar B (the object by descent). **Mandate (AGENDA K2r-split, the relocated residue,
HIGH priority):** K2r FACTORED `C_W`'s radius assembly into (i) the FREE cross-place **determinant
edge** `|α(p)β(p)| = p^{k−1}`, uniform across all primes, Euler-borne + RH-free, and (ii) the HARD
per-prime **even split** `|α(p)|=|β(p)|=p^{(k−1)/2}` = purity `(·)^{1/2}` = Ramanujan/RH. K2r-split
attacks that residue **with the charter's §0 design law**: the missing structure must be a
**`*`-involution** (a duality), not a metric. **THE QUESTION:** does a `*`-involution `σ` on the
weight-2 determinant line, whose fixed locus is exactly the even split `|α|=|β|`, **FORCE** the
Frobenius/Satake pair onto that locus — or is "the pair lies on `Fix(σ)`" itself the RH statement?
**Module:** `scripts/numerics/witness/cw_even_split_involution.py` (run:
`python3 -m scripts.numerics.witness.cw_even_split_involution`). **Falsifier row added** (`falsify.py`, → 52).

---

## The deliverable — the determinant-canonical `*`-involution and the dichotomy it exposes

> **[DEF · the determinant-canonical `*`-involution].** Given the per-prime weight-2 **determinant**
> datum `d = α(p)β(p) = p^{k−1}` (the K2r EDGE — Euler-borne, free), define on the determinant line
> `  σ_d(z) := d / \overline{z}.  `
> This is the **polarization/Rosati adjoint**: it is **involutive** (`σ_d∘σ_d = id`), **antilinear**
> (conjugate-linear — a genuine `*`-structure, **NOT a metric**, charter §0-compliant), and definable
> from the **determinant `d` alone** + complex conjugation (no radius presupposed). Its fixed locus is
> `  Fix(σ_d) = { z : σ_d(z)=z } = { z\bar z = d } = { |z| = \sqrt d }  ` — the **even-split radius**.

This converts K2r-split into a typed, computable question, and the answer **factors the same way K2r
did**, now one level deeper — at the level of the involution itself.

---

## The decisive structural finding — the DUALITY is free; the Frobenius's FIXEDNESS is the residue

Executed on `f = Δ` (Ramanujan τ, weight 12, `H¹` weight `k−1=11`, arithmetic Satake `α,β` = roots of
`X² − τ(p)X + p^{k−1}`, all exact `mpmath` 40 dps; primes 2..19; 5 Weil curves; DH type-level).

### [1] `σ_d` is a genuine `*`-involution, definable from the determinant edge ALONE — the DUALITY is FREE
`σ_d∘σ_d = id` to `≤1e-34` (involutive) and `σ_d` is **antilinear** (`z↦d/\bar z`, conjugate-linear —
a `*`-structure, the thing a metric is **not**, charter §0). It is built from `d = p^{k−1}` — the
K2r **Euler-borne determinant edge** — and conjugation, with **no radius input**. Its fixed locus is
`Fix(σ_d) = {|z|=\sqrt d}` = the even-split radius (verified: a point at radius `√d` is fixed to
`<1e-35`, a point off the radius is moved by `O(\sqrt d)`). **The duality — the involution — is the
FREE half**, exactly the charter §0 promise that a duality is *structural*.

### [2] (A) `Fix(σ_d)` on a det-`d` pair = the even split; (B) the GENUINE pair lies on it — a SEPARATE fact
For a det-`d` pair `{α, β=d/α}`: `Fix(σ_d)` restricted to the pair **IS** the even split
`|α|=|β|=\sqrt d`. The genuine Ramanujan pair **lies on** `Fix(σ_d)` — `True` for all primes (= Deligne).
**But this is a SEPARATE condition** `|α|=\sqrt d`, = Ramanujan/Deligne (a theorem here), **NOT forced by
`σ_d`'s existence**.

### [3] THE PLANT — off-Ramanujan: `σ_d` UNCHANGED, but the pair is NO LONGER on `Fix(σ_d)`
Plant `{α′,β′}` at `p=11` with `α′β′ = p^{k−1}` (**same determinant `d` ⟹ same `σ_d`, the involution
exists verbatim**) but `|α′|=p^{(k−1)/2+0.3}`. Computed: determinant `= 285311670611 = p^{11}`
**PRESERVED** (so `σ_d` is literally unchanged); `|α′|=1065761 ≠ |β′|=267707 ≠ \sqrt d=534146`, so the
pair is **NOT** on `Fix(σ_d)`. **The duality EXISTS but does NOT FORCE the pair onto its fixed locus.**
Only "the pair lies on `Fix(σ_d)`" sees the plant; `σ_d` itself is blind to it.

### [4] FF anchor — `q`-reality (Deligne purity) is the THEOREM that puts `F` on `Fix(σ_q)`
Over `𝔽_q` the Frobenius pair `{α, q/α}` lies on `Fix(σ_q)` **unconditionally** — but **NOT because
`σ_q` forces it**: because the Frobenius is a `q`-**WEIL NUMBER** (`|α|=\sqrt q`), which is **Deligne's
purity / RH for the curve**, a theorem **external to `σ_q`** (verified, 5 curves `q=2,5,7,11,13`).
`σ_q`'s existence is free; the `q`-reality (pair on `Fix`) is the theorem.

### [5] DH falsifier — type-level: no Euler product ⟹ no determinant `d` ⟹ no `σ_d` (empty domain)
DH has no Euler product ⟹ no Satake ⟹ no determinant `d = αβ` ⟹ the involution `σ_d = d/\overline{(·)}`
has **empty domain** (it is *built from `d`*). So **even the FREE half — the duality — does not exist
for DH**, a structural failure at the involution's very definition, strictly before the fixed-point
question. Carrier ladder (K2r, refined): **DH < `ζ` < FF** — DH lacks the determinant (no `σ_d`); `ζ`
has `σ_d` (free) and the OPEN "pair on `Fix`"; FF has both (Deligne).

---

## The K2r-split result (the charter's §0 design law showing its TEETH)

| component | datum | status |
|---|---|---|
| the `*`-involution `σ_d(z)=d/\bar z` (the polarization DUALITY) | built from the determinant `d=p^{k−1}` (Euler-borne, K2r-free); `*`-clean, **NOT a metric** | **FREE** |
| `Fix(σ_d)` restricted to a det-`d` pair | `= |α|=|β|=\sqrt d` (the even split) | **free (a tautology of `σ_d`)** |
| **the Frobenius/Satake pair LIES on `Fix(σ_d)`** | `= |α|=\sqrt d =` Ramanujan/Deligne `= RH(f)`; over `𝔽_q` the `q`-Weil-number theorem | **the irreducible residue** |

The charter's §0 said: *the polarization must be a duality pairing, never a metric.* K2r-split
**confirms §0 is exactly right and then shows its teeth**: the `*`-involution `σ_d` is precisely the
non-metric duality §0 demands, it **exists for free** from the Euler-borne determinant edge, it is
`*`-clean (involutive + antilinear), and its fixed locus **is** the even split. **But a duality, by
itself, does not force its own fixed points** — the existence of `σ_d` (the structure) is independent
of whether the Frobenius **is a fixed point of `σ_d`** (the reality/descent condition), and *that
fixedness is the even split = RH*. So the §0 design law **does not dissolve RH; it RELOCATES it** to
the sharpest possible form:

> **RH = "the Frobenius/Satake pair is a FIXED POINT of the polarization duality `σ_d`."**

Over `𝔽_q` this fixedness is the `q`-Weil-number property — a **theorem** (Weil/Deligne purity) that
lives *outside* the involution (it is the statement that Frobenius commutes with the geometric
conjugation, the *reality* of the motive). Over `ℤ` there is no such theorem; the Frobenius's
fixedness under `σ_d` **is** the open RH.

---

## Falsifier verdict (K2r-split — an anchor/coherence check; the residue is the Frobenius's fixedness)

- **EULER-BORNE — YES.** `σ_d` is built from the determinant `d = αβ = p^{k−1}` (Euler-borne). DH has
  no Euler product ⟹ no `d` ⟹ **no `σ_d`** (empty domain) — even the free half fails for DH.
- **SEES-ZEROS — YES**, through the fixed-point property: an off-Ramanujan plant leaves `σ_d`
  unchanged but moves the pair OFF `Fix(σ_d)`. (The involution alone is blind; "pair on `Fix`" sees it.)
- **INDEPENDENT — NO.** "The pair lies on `Fix(σ_d)`" `= |α|=\sqrt d =` Ramanujan/RH; over the FF it is
  Deligne purity = Weil positivity. So K2r-split is **CIRCULAR over the anchor**, sharpened to: *the
  DUALITY is free and `*`-clean; the Frobenius's FIXEDNESS under it is the irreducible RH.*

Tabled **CIRCULAR** (`euler_borne=Y / sees_zeros=Y / independent=N`). **NEW content:** at the level of
the `*`-involution, the K2r edge/split factorization sharpens to a **structure/fixed-point split**: the
polarization duality `σ_d` is the FREE structural half (§0 vindicated — a genuine non-metric
involution from the determinant edge), and the irreducible residue is the **reality condition "the
Frobenius is a fixed point of `σ_d`"** — over `𝔽_q` a theorem (`q`-Weil-number / Deligne purity),
over `ℤ` the open RH.

---

## Verdict

`[coherence-checked · anchored vs 𝔽_q / Δ]` — K2r-split executed the §0 design law on the relocated
residue and found the honest seam: **the `*`-involution `σ_d(z)=d/\bar z` — the polarization/Rosati
duality on the weight-2 determinant line — EXISTS FOR FREE from the Euler-borne determinant edge
`d=p^{k−1}`, is `*`-clean (involutive + antilinear, NOT a metric — charter §0-compliant), and its
fixed locus restricted to a det-`d` pair IS the even split `|α|=|β|=\sqrt d`. BUT its existence does
NOT FORCE the Frobenius/Satake pair onto `Fix(σ_d)`** — an off-Ramanujan plant (same `d`, same `σ_d`)
is not `σ_d`-fixed. "The pair lies on `Fix(σ_d)`" is a **SEPARATE descent/reality condition** =
`|α|=\sqrt d` = Ramanujan/RH; over `𝔽_q` it is the `q`-Weil-number theorem (Deligne purity = RH for
the curve), external to `σ_q`. **Not overclaimed:** this does not build the fixedness (that is RH); it
**proves the charter's §0 duality is the FREE half** and **names the irreducible residue as the
Frobenius's fixedness under the polarization** — the sharpest form of the keystone residue: a duality
is the right structure but cannot force its own fixed points, and *that fixedness is RH*.

**Successors named:**
- **K2r-fix [the reality datum — is "Frobenius ∈ `Fix(σ_d)`" a `Gal`/descent condition supplied by a
  REAL/condensed structure?]** — over `𝔽_q` the fixedness is "Frobenius commutes with geometric
  conjugation" = the **reality of the `ℓ`-adic / Hodge realization**. Attack: is there a condensed/real
  structure on the weight-2 carrier over `ℤ` whose **descent datum** (the real points / the
  `c`-fixed locus, M3b's `κ`) *forces* the Satake pair to be `σ_d`-fixed — or is that real structure
  itself only available *after* purity? (falsify: the reality datum must be Euler-borne + DH-absent +
  see the off-Ramanujan plant the determinant edge is blind to.)
- **K2 re-pointed:** the condensed object must produce not the involution `σ_d` (free) but the
  **fixed-point/reality condition** "Frobenius ∈ `Fix(σ_d)`" — the `q`-Weil-number analogue over `ℤ`.
- **K3 unchanged:** the Hodge–Riemann forcing is free given `C_W`; `C_W`'s radius = the per-prime even
  split = the Frobenius's `σ_d`-fixedness.
