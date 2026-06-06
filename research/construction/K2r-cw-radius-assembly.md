# K2r — assemble `C_W`'s RADIUS over `ℤ` from the per-prime Satake products `αᵢ(p)αⱼ(p)` [coherence-checked · anchored vs 𝔽_q / Δ]

**Charter:** `construction-program.md` §0 (the polarization is a duality pairing, NOT a metric),
§1 (the contract clause C3b — the Euler-borne radius), Pillar B (the object by descent / cross-place
coupling). **Mandate (AGENDA K2r — the named residue, HIGH priority):** K1 factored the keystone
`c=D` (=`P_∞ ⪰ 0`) into (free geometric cup product `E`) + (formal Hodge–Riemann implication) + (the
**Weil operator `C_W`**, whose RADIUS over `𝔽_q` is LITERALLY `|α|=√q` = RH). The one piece the
geometric forcing does NOT supply is `C_W`'s radius. K2r constructs that radius over `ℤ` from the
**Euler assembly** of the prime Satake products `αᵢ(p)αⱼ(p)` — the M4r/C3b descent hinge in its
sharpest Hodge form. **Built on:** M2b (`rad = (·)^{1/2} ∘ (edge-abscissa)`, the purity functor),
M2d (the purity carrier `gr^W_1` is EMPTY per single prime — the radius must be ASSEMBLED across
primes, not read off one). **Module:** `scripts/numerics/witness/cw_radius_assembly.py`
(run: `python3 -m scripts.numerics.witness.cw_radius_assembly`). **Falsifier row added** (`falsify.py`, → 51).

---

## The deliverable — the assembly map, and where it is Euler-borne vs RH

> **[DEF · the radius-assembly map].** For a multi-prime Euler object `f` (a Hecke eigenform), the
> per-prime weight-2 datum is the multiset of **Satake products** `{αᵢ(p)αⱼ(p)}` of the self-tensor
> `H¹⊗H¹`. The assembly map
> `  rad_assembled : {αᵢ(p)αⱼ(p)}_p  ↦  (edge weight)  ↦^{(·)^{1/2}}  (C_W radius)  `
> reads, per prime, the **weight-2 EDGE** `e(p) = max_{ij}|αᵢ(p)αⱼ(p)|` (the abscissa of the
> per-prime Rankin–Selberg factor `L_p(s, f×f̄)`, the Petersson pole), then the **weight-1 centre
> radius** `C_W` needs as its purity square root `e(p)^{1/2}`. **C3b/C6 built in:** for
> Davenport–Heilbronn there are no Satake products (no Euler product), so the domain is empty.

This converts the keystone residue into a typed, computable question: **does the Euler assembly of
the Satake products supply `C_W`'s radius, and at which step (if any) does RH enter?**

---

## The decisive structural finding — the assembly splits into a FREE edge and a HARD even-split

Executing the map on `f = Δ` (Ramanujan τ, weight 12, `H¹` weight `k−1=11`, arithmetic Satake
`α,β` = roots of `X² − τ(p)X + p^{k−1}`, all exact `mpmath` at 40 dps), 16 primes `2..53`:

### [1] the weight-2 EDGE is the DETERMINANT `|α(p)β(p)| = p^{k−1}` — uniform, Euler-borne, RH-FREE
The per-prime weight-2 edge is `e_top(p) = |αβ| = p^{k−1}` **exactly** (the **determinant** of the
Satake matrix), so the **edge exponent `γ = k−1 = 11` is UNIFORM across all primes** and
**read off the Satake matrix unconditionally** — it uses only the determinant, never the eigenvalue
moduli. *The cross-place edge assembles freely.* (Computed: `|αβ| = p^{11}` to `<1e-15` rel, all primes.)

### [2] the weight-1 CENTRE radius is the EVEN SPLIT `|α(p)|=|β(p)|=p^{(k−1)/2}` — = Ramanujan = RH(f)
The radius `C_W` actually needs is the purity square root: `|α(p)| = p^{(k−1)/2}`, which holds **iff
the determinant `p^{k−1}` splits into two EQUAL moduli** — i.e. iff `|τ(p)| ≤ 2p^{(k−1)/2}`, the
**Ramanujan/Deligne bound**, the exact analogue of RH for `f`. (Computed: `|α|=|β|=p^{(k−1)/2}` to
`<1e-20` rel, all primes — a THEOREM here, Deligne.)

### [3] THE PLANT — off-Ramanujan: the edge is PRESERVED, the even split is BROKEN
Plant `{α′,β′}` at `p=11` with `α′β′ = p^{k−1}` (determinant fixed) but `|α′|=p^{(k−1)/2+δ}`,
`|β′|=p^{(k−1)/2−δ}` (`δ=0.3`). Computed: determinant edge `= 285311670611.0 = p^{11}` **PRESERVED**;
`|α′|=1096674`, `|β′|=260161` vs `√` `534146` — even split **BROKEN**. So **the Euler assembly of the
Satake PRODUCTS (the determinant edge) is INSENSITIVE to the off-Ramanujan plant; only the EVEN SPLIT
(the purity square root) sees it.** This is the "off-line zero of `f`" analogue read on the radius.

### [4] FF anchor — a single place: the assembly DEGENERATES, the radius is free (this is WHY)
A curve `C/𝔽_q` is a **single place** (one base size `q`). The weight-2 edge is the determinant
`αβ = q` (free); the even split `|α|=|β|=√q` IS the curve's RH (Deligne). *There is no cross-place
assembly to do* — the single place's determinant **is** the edge, and purity does the square root.
This is precisely why the FF gets `C_W`'s radius "for free": the multi-prime assembly degenerates.
(Computed: 5 Weil curves `q=2,5,7,11,13`, det edge `=q`, even split `|α|=√q` all True.)

### [5] DH falsifier — type-level: no Euler product ⟹ no Satake ⟹ empty domain
DH has no Euler product, hence no Satake products `αᵢ(p)αⱼ(p)`, hence the assembly map has **empty
domain** — the weight-2 edge cannot even be formed (no per-prime determinant). `C_W`'s radius is
undefined for DH at the **first** step, strictly before the even-split/purity question. The
carrier-ladder of M2d refines: **DH < `ζ` < FF** — DH lacks the Satake (no edge); `ζ` has the edge
(determinant, free) and the OPEN even split; the FF has both (single place, Deligne).

---

## The K2r factorization (the result, sharper than the agenda hoped)

| step of the assembly | datum | status |
|---|---|---|
| weight-2 **EDGE** = determinant `\|αβ\|=p^{k−1}`, uniform across primes | Euler-borne, RH-**free** | **the cross-place assembly is FREE** |
| weight-1 **CENTRE** = even split `\|α\|=\|β\|=p^{(k−1)/2}` (purity `(·)^{1/2}`) | = Ramanujan = RH(f) | **the hard residue** |

So the keystone residue (`C_W`'s radius) is **NOT** the cross-place assembly — the agenda's framing
("Euler-assemble the radius from the per-prime Satake products") is **half achievable for free**: the
**determinant edge `p^{k−1}` assembles uniformly across all primes, RH-independently.** The
irreducible residue **relocates one step inward**: it is the **per-prime EVEN SPLIT** of the
assembled weight-2 edge into two equal weight-1 factors — exactly the M2b **purity square root**,
exactly Ramanujan/RH for `f`. The Euler product hands you `p^{k−1}` for free; **RH = that edge splits
evenly at every prime.**

This is the precise Hodge-theoretic shape of K1's "radius-silent `(−1)^w`" and M3b's lesson: the
weight-2 **edge** (the determinant, the Petersson `‖f‖²` pole at `Re s=1` of `f×f̄`) is the
Euler-borne datum the descent assembles; the weight-1 **centre** `Re s=½` is its **even square root**,
and that even-splitting is the whole of RH — not borrowed from the FE, but it is also **not** supplied
by the cross-place assembly (which only gives the determinant).

---

## Falsifier verdict (K2r — an anchor/assembly check; the residue relocates to the even split)

- **EULER-ASSEMBLED — SPLIT.** The weight-2 **edge** (determinant `|αβ|=p^{k−1}`) IS Euler-assembled,
  uniform across primes, and **RH-independent** (free even off-Ramanujan); the **centre** (even split)
  is Euler-borne in the sense of needing the Satake data but is **not** supplied by the assembly — it
  is the purity square root. DH fails at step 0 (no Satake ⟹ empty domain).
- **SEES-ZEROS — YES**, but only through the even split: the off-Ramanujan plant moves `|α|` while the
  determinant edge is blind to it. The assembled edge alone does NOT see the plant.
- **INDEPENDENT — NO.** The even split `|α|=|β|=p^{(k−1)/2}` **IS** Ramanujan/RH for `f`; over the FF
  it is Deligne purity = the Weil positivity. So K2r is **CIRCULAR over the anchor** in the precise
  sense that the even split of the assembled edge = the RH radius.

Tabled CIRCULAR (`euler_borne=Y / sees_zeros=Y / independent=N`) — the FF/Δ archetype verdict; the
NEW content is the **edge/split factorization** of the assembly: the cross-place determinant edge is
free, the residue is the per-prime even split.

---

## Verdict

`[coherence-checked · anchored vs 𝔽_q / Δ]` — K2r executed the radius assembly on the multi-prime
anchor (`f=Δ`, 16 primes, exact) and found the honest seam: **the Euler assembly of the Satake
products `αᵢ(p)αⱼ(p)` supplies `C_W`'s radius-SQUARED EDGE — the determinant `|α(p)β(p)|=p^{k−1}`,
uniform across all primes, Euler-borne, RH-independent (the Satake determinant, free even
off-Ramanujan) — but NOT the SQUARE ROOT / even split `|α|=|β|=p^{(k−1)/2}` the weight-1 `C_W`
needs.** An off-Ramanujan plant PRESERVES the edge (determinant) and BREAKS the even split. So the
cross-place edge assembly is **FREE**; the irreducible residue relocates to the **per-prime even split**
= the M2b purity `(·)^{1/2}` = Ramanujan/RH. **Not overclaimed:** this does not build the even split
(that is RH); it **factors the assembly** and proves the cross-place coupling is the *free* half, the
residue the *per-prime purity split* of the assembled edge — the keystone residue, sharpened from "the
radius" to "the even-splitting of the assembled weight-2 determinant edge."

**Successors named:** K2r-split [the relocated residue — is the per-prime EVEN SPLIT of the assembled
edge `p^{k−1}` itself forced by any geometric/condensed structure on the weight-2 carrier, or is it
the irreducible RH? attack via the `(·)^{1/2}` purity as a structure map on the determinant line];
K2 re-pointed (the condensed object must produce the **even split** of the determinant edge, not the
edge — the edge is free); K3 unchanged (the Hodge–Riemann forcing is free given `C_W`; `C_W`'s radius
= the per-prime even split).
