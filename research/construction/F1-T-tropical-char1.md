# F1-T — the TROPICAL / BOOLEAN / max-plus ground (Connes–Consani characteristic 1; arithmetic site / scaling site over B or R_max). Does the characteristic-1 Frobenius `x↦x^λ` (the scaling) supply a DISCRETE ARITHMETIC scale `q` to the archimedean conjugation, or only the CONTINUUM? [DECISION · DEF · coherence-checked vs 𝔽_q · SCALE_FREE]

2026-06-06. Lit (fetched, text-extracted, quoted): Connes–Consani *Characteristic one, entropy and the absolute point* (0911.3537); *The Arithmetic Site* (arithmeticsite.pdf); *The Scaling Site* (1507.05818); *Geometry of the Scaling Site* (1603.03191); Lorscheid *Counting and zeta functions over F1* (1306.3681); Soulé *Schemes over F1 and zeta functions* (0903.2024). Numerics: inline mpmath 40dps (this log). Builds on R3/R3-scaling (the scaling-site continuum), R3b/R3b-BC (discreteness≠base size; `q→1` deletes the ground field), R8 (no constant field at ∞), R10 (compactness gives the count not the radius), QD (the prismatic/Λ-ring canonicality is finite-prime-indexed, archimedean-blind). 49th `falsify.py` consideration, DISPERSING-by-design (terminus-characterizer, Euler-silent).

## The mandate (charter `f1-construction.md`, candidate T)

`𝔽₁` ⟺ a *scaled conjugation*: an archimedean Frobenius that is BOTH the reality (`F†=F̄`, order-2 `Gal(ℂ/ℝ)`) AND carries an arithmetic scale `q`. The tropical/characteristic-1 ground (Connes–Consani) is the canonical `𝔽₁`-candidate whose **distinguishing structure is a Frobenius**: the characteristic-1 Frobenius is the scaling `x↦x^λ`. **Decisive test:** does that scaling supply a DISCRETE arithmetic `q`, or only the CONTINUUM (R3's free self-dual ½)? And is there a tropical analogue of `|𝔽_q|=q` (a finite "size" in char 1) that discretizes to a genuine arithmetic `q` at ∞?

---

## What the literature ESTABLISHES (quoted, decisive)

**[lit·1] The characteristic-1 Frobenius is `x↦x^λ` with `λ∈ℝ*₊` — CONTINUOUS.** [0911.3537, §2.1, quoted]
> "On a field of characteristic `p>1`, the arithmetic Frobenius is given by the 'additive' map `x↦x^p`. On `R_max₊`, the Frobenius flow has the analogous description given by the action `x↦x^λ` (`λ∈ℝ*₊`)."

and (eq. 3) `ϑ_λ(u)=u^λ, λ∈R_max₊` "corresponds to the arithmetic Frobenius in characteristic `p>1`." The exponent that over `𝔽_q` is the **integer prime power `q≥2`** is, in characteristic 1, **any positive real `λ`**. The discrete `q^ℤ` becomes the continuous one-parameter group `ℝ*₊` — *exactly the R3 scaling-site generator `θ=t∂_t`*. **The tropical Frobenius is the continuum, by construction.**

**[lit·2] The tropical ground IS the archimedean place — it HAS the reality, by the dequantization table.** [0911.3537, §1, quoted table]
> | Characteristic 0 | `Q_p, p>1` | **Archimedean ℝ** |
> | Characteristic ≠0 | `F_p((T))` | **`p=1, R_max₊`** |

"In characteristic one, the role of the local field `F_p((T))` is played by the local semi-field `R_max₊`." `R_max₊` is obtained from ℝ by **dequantization** (`D_h(u)=u^h`, `h·ln(e^{w₁/h}+e^{w₂/h})→max{w₁,w₂}` as `h→0`). So the tropical ground is *literally the `h→0` semiclassical shadow of the archimedean ℝ* — it sits at ∞ and carries the archimedean reality. **This is the candidate's genuine strength: it is the one `𝔽₁`-object native to `∞`, with a Frobenius.** But that Frobenius's scale is `ℝ*₊` (continuum), not `q`.

**[lit·3] The Boolean semifield `B={0,1}` is the absolute point — but `B↛ℤ`: NO arithmetic scale escapes.** [0911.3537, §2.6, quoted]
> "Spec `B` does not qualify to be the 'absolute point', since **there is no morphism from `B` to `ℤ`**."

`B={0,1}` with `1+1=1`: its **multiplicative group is `B^×={1}`** — `|B^×|=1`. The arithmetic site (Connes–Consani) is the topos `\hat{N^×}` (dual of `(ℕ^×,·)`, finite-prime-indexed) with structure sheaf `B`; the **scaling site is the extension of scalars from `B` to `R_max`** (verified, *Arithmetic Site*/*Scaling Site*), giving the semidirect product `[0,∞)⋊ℕ^×` — *the R3 object*. The size carried is `R*₊` (the scaling) or the index `ℕ^×` (R3b-BC: a base-independent discrete index whose ground field `q→1` deletes). **No finite `|𝔽_q|`-analogue: `|B^×|=1` or `|R*₊|=continuum`.**

**[lit·4] The Soulé/F1-zeta SENDS THE SCALE `q` TO 1 — what survives is the Euler characteristic / pole order, a COUNT located on the FE/abscissa lattice, NOT a radius.** [1306.3681, quoted]
The F1-zeta is the `p→1` limit
> `ζ_{X/F1}(s) = lim_{p→1} Z_X(p,p^{-s})(p−1)^{N(1)}`, and "if `N(x)=a₀+···+a_n x^n`, then **`ζ_{X/F1}(s) = s^{−a₀}(s−1)^{−a₁}···(s−n)^{−a_n}`**."
The pole order at `p=1` is `N(1) = Σ_x Σ_r (−1)^r (...) = χ` (the **Euler characteristic**); the poles sit at the **integer lattice `s∈{0,1,…,n}`** (the dimensions). The functional equation `ζ_{X/F1}(d−s)=(−1)^χ ζ_{X/F1}(s)` is the **FE/abscissa symmetry** (Step A), shared by the torsion-free case. **The whole construction is built by taking `q→1`** — the arithmetic scale is the *parameter that is sent to 1*; what is retained (the `a_i`, the Euler characteristic, the FE lattice) is the **count/location**, never the modulus `√q`. This is the count/radius decoupling (the-complete-account §5) realized exactly in the F1-zeta definition: `𝔽₁`-counting keeps the count, kills the scale.

---

## What got COMPUTED (mpmath 40dps, FF-anchored)

**[1] The char-1 Frobenius `x↦x^λ` ranges over the CONTINUUM — no marked `q`.** [computed]
`ϑ_λ(u)=u^λ` evaluated for `λ=0.5,1,1.7,e,π` on `u=3.3`: every positive real `λ` is on equal footing — `marked_q_exists=False`. Over `𝔽_q` the exponent is the integer `q≥2` (discrete, gapped `q^ℤ`); in char 1 it is `ℝ*₊` (gapless). **The tropical scaling is the R3 continuum, confirmed at the Frobenius level.**

**[2] The scale `q` EVAPORATES in the tropical/`𝔽₁` limit of an `𝔽_q` curve.** [computed, decisive]
The `𝔽_q` local factor `(1−α q^{−s})^{−1}` has radius `√q`. The tropical/dequantization limit is **Tits's `q→1`** (the algebraic structure of `F_q` degenerates as `q→1`). Computed `q=5,3,2,1.5,1.1,1.001` → `√q = 2.236,1.732,1.414,1.225,1.049,1.0005 → 1`: **the radius collapses to 1**. The scale `q` is not transported to ∞ — it is the *thing sent to 1* to reach the tropical/`𝔽₁` point. (Same evaporation R3b-BC computed for the Bost–Connes `q→1`.) The tropical ground does **not** supply `q`; it is *defined by killing `q`*.

**[3] No tropical `|𝔽_q|=q`: the char-1 "size" is `1` (`|B^×|`) or a continuum (`|R*₊|`).** [computed/structural]
`|B^×|=1`; `R_max` multiplicative group `=R*₊` continuum. The F1-zeta pole order is `N(1)=χ` (an integer **dimension/rank** — the Euler characteristic, a *count*), located at the FE lattice `{0,…,n}`, NOT a radius. There is no finite arithmetic "size" between `1` and the continuum.

**[4·ANCHOR] At a FINITE prime `q` SURVIVES — `Frob=x^q`, `|α|=√q` marked.** [computed, anchor]
Genus-1 `(q,a)=(5,1),(7,3),(11,−2),(13,4)` → `|α|=√q={2.236,2.646,3.317,3.606}`, pure `True`. Here `q` is the integer prime power, the residue-field cardinality, and `Frob=x^q` is **ONE ring endomorphism doing `+` and `×` at once** — `q` is simultaneously the size (count) and the scaling exponent (radius). **The discreteness of the integer `q` is exactly what the char-1 continuous `λ∈ℝ*₊` lacks.**

**[5·DH] DH falsified — the tropical apparatus is UNPOSABLE for DH.** [computed/structural]
DH (functional equation, **no Euler product**) has no local Frobenius `P_p(T)`, hence no `#X(F_{p^n})=N(p^n)` polynomial-point-count (Soulé's condition fails — there is no scheme, no `𝔽_q`-points to count), hence **no `q→1` F1-limit and no characteristic-1 Frobenius `x↦x^λ`** (the scaling site/arithmetic site is built on `(ℕ^×,·)` = the multiplicative semigroup of the *primes*, which DH's coefficients do not factor through). The tropical/`𝔽₁` counting machinery is **unposable** for DH (no Euler product ⟹ no point-count ⟹ no Soulé zeta ⟹ no tropical curve). Tropical structure correctly DIES for DH — inherited Euler-product kill.

---

## THE CRUX — discrete arithmetic `q`, or only the continuum?

**The tropical ground is, definitionally, the continuum side.** Three independent confirmations:
1. **The Frobenius exponent is `ℝ*₊`** ([lit·1], [1]): the integer `q^ℤ` of `𝔽_q` is replaced by the continuous flow `ϑ_λ, λ∈ℝ*₊` = the R3 scaling generator. This is the **dequantization** of ℝ — it carries the FE/Haar self-dual axis ½ (R3), free, DH-shared, **not** `q`.
2. **The size is `1` or a continuum** ([lit·3], [3]): `|B^×|=1`, `|R*₊|=∞`; no finite `|𝔽_q|`-analogue. The Connes–Consani "size" of the scaling site at a point is `ℝ` or `ℂ` (R8: continuum residue field), not a finite cardinality.
3. **The F1-zeta is built by `q→1`** ([lit·4], [2]): the arithmetic scale is the *parameter dequantized to 1*; what survives is the Euler characteristic (count) on the FE lattice (location). The tropical limit *removes* the scale by construction.

**Is there a tropical analogue of `|𝔽_q|=q` that discretizes to an arithmetic `q` at ∞?** No. The only finite invariant the F1-counting produces is the **Euler characteristic `χ`** (pole order `N(1)`) — a *dimension*, the COUNT half of the count/radius decoupling — placed on the integer abscissa lattice. The scale `q` is precisely the dequantization parameter `h` (`q=e^{1/h}`-flavored), sent to its degenerate value. **The tropical ground supplies the CONTINUUM (the FE axis ½) and the COUNT (χ), never a discrete arithmetic `q` / a radius.**

**Why this is the genuine `𝔽₁`-frontier object and yet still scale-free.** Among all candidates, the tropical ground is the one that *both* sits at ∞ (the dequantized archimedean ℝ, [lit·2]) *and* has a named Frobenius (`x↦x^λ`). It is the strongest realization of "the archimedean place has the reality." But its Frobenius scale is continuous (`ℝ*₊`), its size is `1`/continuum, and its zeta is defined by `q→1`: it carries the **reality + the FE axis + the count**, and is **scale-free on the arithmetic `q`** — the exact R3/R8/R10 residue, now reached from the characteristic-1 / arithmetic-site root (the most native `𝔽₁`-at-∞ object), confirming the wall a 49th time.

---

## Verdict — SCALE_FREE (the CONTINUUM, by construction); the candidate is CLOSED

> **[DECISION · F1-T verdict].** The tropical / Boolean / max-plus ground (Connes–Consani characteristic 1; arithmetic site over `B`, scaling site over `R_max`) **CARRIES the archimedean reality** — it is the `h→0` dequantization of the archimedean ℝ (the table aligns `p=1, R_max` with Archimedean ℝ), and it has a *named Frobenius* `x↦x^λ`, making it the strongest "scaled-conjugation" candidate. **But it SUPPLIES ONLY THE CONTINUUM, not a discrete arithmetic `q`** — verified three ways: (i) the char-1 Frobenius exponent is `λ∈ℝ*₊` (continuous, = the R3 scaling generator `θ`), vs the integer `q^ℤ` of `𝔽_q`; (ii) the char-1 "size" is `|B^×|=1` or `|R*₊|=continuum`, with no finite `|𝔽_q|`-analogue (the F1 pole order is the Euler characteristic `χ` = a count/dimension on the FE lattice, not a radius); (iii) the Soulé/F1-zeta is *defined by `q→1`* — the arithmetic scale is the dequantization parameter SENT TO 1, computed evaporating `√q→1` for `q=5,…,1.001`. **No tropical `|𝔽_q|=q` discretizes to an arithmetic `q` at ∞; the tropical size is always `1`/a continuum.** The radius `√q` is marked **only at the finite prime** by the integer `q` ([4]·anchor), where `Frob=x^q` is one map doing `+` and `×` at once — the discreteness the continuous `λ` lacks. **DH dies** (no Euler product ⟹ no point-count ⟹ Soulé's condition fails ⟹ no tropical curve / `q→1` limit — unposable). **SCALE_FREE_CLOSED:** the tropical ground is the *cleanest realization of "reality without scale"* — it confirms R3 (the scaling = the continuum/FE axis) at its characteristic-1 root and adds the decisive new fact that **`𝔽₁`-geometry's own counting keeps the count (`χ`) and kills the scale (`q→1`)**, so it can never carry `q`.

## The decision lines (as required)

- **(1) Discrete arithmetic `q`, or continuum?** **CONTINUUM.** The char-1 Frobenius is `x↦x^λ, λ∈ℝ*₊` (= R3's `θ`); the scaling site over `R_max` carries the FE/Haar self-dual axis ½ (free, DH-shared), not the arithmetic `q`. The discrete `q^ℤ` of `𝔽_q` is replaced by the continuous flow `ℝ*₊` — by the dequantization construction.
- **(2) Tropical `|𝔽_q|=q`?** **NONE.** `|B^×|=1`, `|R*₊|=continuum`; the only finite F1-invariant is the Euler characteristic `χ` (pole order `N(1)`) = a count on the integer FE lattice, **not** a finite "size" that discretizes to `q` / a radius. The tropical size is always `1` or a continuum.
- **(3) Anchor / DH.** `𝔽_q`: `q` integer ≥2, `Frob=x^q`, `|α|=√q` marked (computed `2.236,2.646,3.317,3.606`, pure). The `𝔽_q→𝔽₁` (`q→1`) limit **evaporates** `q` (radius `√q→1`, computed). DH: **unposable** (no Euler product ⟹ no point-count ⟹ no Soulé zeta ⟹ no tropical curve).
- **(verdict) SCALE_FREE.** Reality YES (dequantized archimedean ℝ, named Frobenius); discrete arithmetic `q` NO (continuum by construction; F1-counting kills `q` via `q→1`). Candidate **CLOSED**.

## Falsifier verdict (F1-T — terminus characterizer / `𝔽₁`-root, Euler-silent by design)

- **EULER-BORNE — NO, by design.** Type-checks the char-1 Frobenius/size against the anchor; not a standalone ℤ-positivity. DISPERSING-by-design. DH structural verdict SHARP: no Euler product ⟹ no `#X(F_{p^n})` polynomial ⟹ Soulé's condition fails ⟹ no tropical/`𝔽₁` curve (unposable, ground-floor kill).
- **SEES-ZEROS — YES** (only via the Connes–Consani spectral realization: RH = "spectrum on the self-dual axis ½" = N4, which the continuous scaling does not force).
- **INDEPENDENT — NO** (the scaling spectral realization is equivalent to RH; the `½` is the FE-fixed DH-shared locus). → **DISPERSING-by-design.** Ladder `DH < ζ < FF`: DH no point-count (unposable); ζ = the `q→1`/`𝔽₁` place — the scaling-site continuum + the FE axis ½ + the Euler characteristic `χ` all supplied, the arithmetic `q` (radius) **UNMARKED** (it is the dequantized-away parameter); FF a curve over a **finite** `𝔽_q` — integer `q`, `Frob=x^q`, radius `√q` **MARKED**. Registered as the **49th wall confirmation** (the residue as the **continuum/count vs discrete-scale type gap, at the characteristic-1 / arithmetic-site root**).

## Residual / blueprint

The precise residual the tropical ground leaves: **a DISCRETE refinement of the characteristic-1 Frobenius `x↦x^λ` that marks a single arithmetic `λ=q∈ℤ_{≥2}` at ∞** — i.e. a *finite* sub-semifield of `R_max` whose multiplicative group is `q^ℤ` rather than `ℝ*₊`, OR a `q≠1` value of the dequantization parameter at which the Soulé F1-zeta retains a finite radius rather than the `q→1` Euler-characteristic shadow. The literature provides **neither**: the char-1 Frobenius is *defined* as the continuous flow (the dequantization `h→0`), and the F1-zeta is *defined* by `q→1`. Supplying the discrete `q` would be exactly the missing object — re-deriving the finite constant field `𝔽_q` *under* a curve at ∞ (R8), which `Spec ℤ` lacks. The tropical ground is the sharpest statement of *why* it is missing: `𝔽₁` is the `q→1` shadow, and its own zeta keeps the count (`χ`) while sending the scale (`q`) to 1. **Confirms R3/R8/R10/QD; adds the characteristic-1 root and the F1-zeta `q→1`-evaporation as the decisive new evidence. Candidate T CLOSED — SCALE_FREE.**
