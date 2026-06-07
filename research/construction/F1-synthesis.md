# 𝔽₁-synthesis — exhausting the candidate finite grounds for the scaled conjugation (2026-06-06)

**Charter:** `research/f1-construction.md`. 𝔽₁ ⟺ a *scaled conjugation*: an archimedean Frobenius carrying
BOTH the reality (`F†=F̄`, which ∞ has) AND an arithmetic scale `q` (which ∞ lacks). If ANY ground supplies
`q` (anchored on `F_q`, failing for DH), 𝔽₁ is constructed and RH follows by Hodge index. This file judges the
six candidate grounds {S, T, M, P, G, Λ}.

---

## 1. Does any ground SUPPLY the scale `q`? — NO.

| ground | reality (Step A) | supplies_scale | anchor `F_q` | DH | verdict |
|---|---|---|---|---|---|
| (S) sphere spectrum 𝕊 | partial (duality skeleton) | **SCALE_FREE** | FAIL (RR blind to radius) | PASS (dies) | SCALE_FREE_CLOSED |
| (T) tropical / char-1 | yes | **SCALE_FREE** | PASS | PASS (dies) | SCALE_FREE_CLOSED |
| (M) monoid / Deitmar–Soulé | partial (μ₂ only) | **SCALE_FREE** | PASS | PASS (dies) | SCALE_FREE_CLOSED |
| (P) Tate-twist period 2π | yes | **WRONG_SCALE** | PASS | PASS (dies) | SCALE_FREE_CLOSED |
| (G) global / product-formula | yes | **WRONG_SCALE** | PASS | PASS (dies) | SCALE_FREE_CLOSED |
| (Λ) Witt / Λ-ring | yes | **SCALE_FREE** | PASS | PASS (dies) | SCALE_FREE_CLOSED |

**No ground returned CONSTRUCTS_F1.** Every one carries the reality / Step-A skeleton (the order-2 conjugation,
the functional-equation / Serre-duality axis, the FE-symmetric center Re s = 1/2) and every one is scale-free
or wrong-scale on the per-eigenvalue radius `|α| = √q` (Step B = purity = RH). The anchor is the tell: where
the ground reaches a genuine `F_q` (T, M, P, G, Λ all PASS) the radius `√q` is recovered ONLY because a finite
constant field already sits under the curve — the ground borrows it, never manufactures it. (S) does not even
pass the anchor: its 𝕊-Riemann–Roch returns χ = deg+1−g, identical for pure and off-circle Frobenius, blind to
the radius which lives in the zeta numerator `P(T)=∏(1−αᵢT)`.

---

## 2. The unifying reason — why every 𝔽₁-ground carries the reality but not the scale.

The six grounds fail for one structural reason, seen six ways:

> **The reality is an order-2 datum (a count of cardinality 2: `Gal(ℂ/ℝ)`, the duality involution, `μ₂={0,±1}`).
> An order-2 involution is INTRINSIC to the archimedean place and to every 𝔽₁-base — it is the abscissa/FE
> axis, a COUNT. The scale `q` is a per-eigenvalue MODULUS, and a modulus `√q` is the eigenvalue of a degree-`q`
> endomorphism of a curve sitting over a FINITE CONSTANT FIELD. No 𝔽₁-ground has a finite constant field at ∞;
> so each ground produces, in place of the discrete arithmetic `q`, the SAME wrong type of object: a count, a
> continuum, a period, or the FE axis.**

The count/radius (location/modulus) decoupling — the central atom of the whole audit (R3, R8, R9, R10, QD) —
recurs at the 𝔽₁-root in exactly six dialects:

- **(S) homotopy cardinality.** 𝕊's finiteness is `π_n(𝕊)` torsion = an Euler-characteristic COUNT / K-theory
  torsion. `π₀=ℤ` (rank 1) builds the curve `𝕊[X]`; the homotopy cardinality fixes only the geometric mean
  `(det F)^{1/2g}`, never the per-eigenvalue `|αᵢ|=√q`. Count, not radius.
- **(T) dequantization q→1.** The char-1 Frobenius `x↦x^λ` has `λ∈ℝ₊ˣ` CONTINUOUS; the only finite 𝔽₁-invariant
  is χ (pole order N(1)), again a count on the FE lattice; the Soulé 𝔽₁-zeta is DEFINED by `q→1`, the limit in
  which `√q→1` — the scale is literally the dequantization parameter sent away. Continuum + count, no radius.
- **(M) valuation continuum.** Every monoid route to ∞ yields the WRONG type: Takagi's ∞-stalk is the valuation
  disk `𝐃ℚ` (a continuum), `Γ={0,±1}=μ₂` (roots of unity), the C–C `N(q)` is a distribution on the real
  continuum `q∈[1,∞)` with `N(1)=−∞`. Continuum/distribution/μ_∞, never a finite cardinality `q`.
- **(Λ) dequantization at ∞.** `ψ_p` needs a residue characteristic (`ψ_p(x)≡x^p mod p`); ∞ has none. The one
  construction that DOES build an archimedean Witt-Frobenius (Connes–Consani's universal thickening of ℝ)
  DEQUANTIZES to Viro's tropical real hyperfield — i.e. (Λ) at ∞ literally becomes (T). Continuum again.

Two of the six are not scale-free but **WRONG-SCALE** — they DO put a number in the `q`-slot, but it is the
wrong TYPE of number:

- **(P) period 2π** is a TRANSCENDENTAL (Lindemann; the prototypical motivic period, Grothendieck/Kontsevich–
  Zagier). It occupies the exact slot `q` sits in over `F_q` (Frob on `ℚ_ℓ(1)` = the integer `q`), but it is
  not a finite cardinality and not an eigenvalue of any finite-degree endomorphism of ℂ. **The period is what
  `q` DEGENERATES TO when the finite ground is deleted** — the symptom of the missing ground, not its supplier.
- **(G) global product `∏_v|x|_v=1`** makes the archimedean size global ("minus the sum of the prime sizes"),
  but the archimedean factor is the CONTINUUM `ℝ₊` normalized by the product, and the only thing the global
  relation pins is the FE-symmetric center Re s = 1/2 (which DH shares) and the determinant coupling `α·α'=q`.
  COMPUTED-decisive: two genus-1 configs with the SAME global product (`{2.236,2.236}` pure vs `{4.025,1.242}`
  off-line) are INDISTINGUISHABLE to the product formula — the radius is invisible to every global SUM. Going
  global reproduces the audit's EDGE (`W_∞ ≥ Σ_p W_p`), never the line.

**So the deepest statement is confirmed and sharpened:**

> **The scale is never intrinsic to a ground; it always comes from a real finite field, which ∞ structurally is
> not.** Every 𝔽₁-base supplies the order-2 reality (a count = the FE axis) because an involution is free; none
> supplies `q`, because `q` is the cardinality of a finite constant field and an 𝔽₁-base at ∞ has none. When
> forced to produce a number in the `q`-slot, a ground returns the type it actually carries — a count (S, T-χ,
> M-χ), a continuum (T-λ, M-disk, Λ, G-ℝ₊), a transcendental period (P), or the FE axis (G, all). Never a finite
> arithmetic cardinality.

---

## 3. WRONG-SCALE vs genuine SCALE-FREE.

- **WRONG_SCALE (supplies a number, wrong type): (P), (G).** (P) supplies the transcendental period 2π;
  (G) supplies the continuum `ℝ₊` and the FE axis 1/2. These are the most instructive failures: they show the
  `q`-slot is OCCUPIABLE at ∞, but only by the de-quantized shadow of `q` (a period; a continuum/location),
  proving the obstruction is a TRANSCENDENCE/type gap (period vs cardinality) and a count/radius gap, not a
  mere absence.
- **SCALE_FREE (supplies no `q` at all): (S), (T), (M), (Λ).** These carry only count-typed (χ, homotopy
  cardinality, μ₂) or continuum-typed (λ∈ℝ₊ˣ, valuation disk) invariants; the scale evaporates rather than
  appearing wrong. (Λ) collapses onto (T) at ∞ (Witt perfection of ℝ = the tropical/scaling continuum).
- **The common denominator:** WRONG-SCALE and SCALE-FREE are the same atom — both return a continuum/count/
  period in place of the discrete cardinality `q`. The split is cosmetic: a ground is WRONG-SCALE when it
  numerically fills the slot (period, ℝ₊) and SCALE-FREE when it does not (χ, q→1). In every case the radius
  `√q` is supplied at the anchor ONLY by a pre-existing finite constant field, and deleted at ∞.

---

## 4. Path status — CLOSED, with a strengthened no-go.

**The 𝔽₁-construction path is CLOSED.** All six independent grounds — including the two with the best 𝔽₁
pedigree (S = Connes–Consani's 𝕊-Riemann–Roch; T = the char-1 scaling site) and the two that put an actual
number in the slot (P, G) — are scale-free or wrong-scale, each for the same reason reached from a different
direction. This is the fifth-through-tenth independent confirmation of the R8/R9/R10/QD atom (no finite
constant field at ∞; compactness/duality/homotopy give the count, not the radius). The exhaustion is genuine:
homotopical (S, Λ), order-theoretic/tropical (T, Λ), monoid/blue-scheme (M), motivic/Hodge (P), and adelic/
global (G) routes are ALL covered, and they converge.

**Strengthened no-go (now earned, not assumed):**

> **No 𝔽₁-ground carries an archimedean arithmetic scale.** The arithmetic scale `q` is the cardinality of a
> finite constant field; it is a property a real finite field HAS and the archimedean place structurally CANNOT
> have (char 0, residue field ℝ/ℂ, no finite quotient). Every 𝔽₁-base, by construction, lives in the additively-
> blind / dequantized / count-typed skeleton (Step A) and provably cannot cross the cardinality-vs-continuum
> type gap (Step B). The no-go is therefore not "we failed to find the scale" but "the scale is not the kind of
> thing a ground supplies."

**Surviving lead / not-yet-tried combination — assessed and rejected.** The prompt flags one: marry (S)'s
homotopy-scale to (G)'s global product. It fails by composition of the two verdicts already in hand: (S)'s
homotopy invariant is a COUNT (χ / K-theory torsion, fixing only the geometric mean), and (G)'s global product
is a SUM of locations pinned to the FE axis 1/2. A count summed adelically is still a count/location — neither
factor carries a per-eigenvalue modulus, so their product cannot. Same for any pairing among {S,T,M,Λ}
(all count/continuum) or with {P,G} (period/continuum): you cannot multiply or sum the wrong type into the
right one. No combination survives; there is no surviving 𝔽₁-ground.

---

## 5. The deepest residual / blueprint for the new object (candidate N).

The residual is identical across all six grounds, which is itself the strongest evidence the path is closed:

> **Required:** a single archimedean operator `ψ_∞` that is simultaneously (i) the order-2 reality `F†=F̄`
> (which every ground supplies — the tropical real hyperfield / `μ₂` / complex conjugation), AND (ii) carries a
> DISCRETE finite arithmetic scale `q∈ℤ_{≥2}` with per-`H¹`-eigenvalue modulus forced to `√q` — WITHOUT
> re-importing a finite constant field (because ∞ has none).

Restated as the precise type obstruction each ground hit:
- It is a **quantization of the period** 2π to a finite cardinality (P): forbidden by transcendence.
- It is a **discretization of the char-1 flow** `λ∈ℝ₊ˣ` to a single `q^ℤ` (T, Λ): the char-1 Frobenius IS the
  continuous dequantization (`ħ→0`); discretizing it = re-installing `F_q`, which Spec ℤ lacks.
- It is a **finite residue cardinality** replacing the valuation disk / distribution / `μ_∞` (M): a continuum
  cannot be a finite cardinality.
- It is an **H²/Tate-twist Frobenius eigenvalue `q` over 𝕊** (S): the homotopy structure is a count and cannot
  impose the per-eigenvalue equality.
- It is a **finite-base discrete archimedean factor** in the product formula (G): the product borrows ∞'s size
  from the primes as a continuum real, never as a finite cardinality.

**Candidate N (the minimal new object).** The blueprint that survives all six residuals: not a richer 𝔽₁-base
(provably impossible — every base is count/continuum/period typed), but a **degenerating arithmetic family whose
special fiber at ∞ lives over a genuine finite constant field**, forcing `F†=F̄` AS a purity statement (the
modulus, not the involution). Equivalently: an honest archimedean Frobenius AUTOMORPHISM `F_∞` (not Deninger's
log-Frobenius DERIVATION `Φ`, whose spectrum is the infinite real tower) whose eigenvalue on `ℝ(1)` is a finite
`q` rather than the transcendental `2πi`. This is the same object the geometric no-go (`the-complete-account.md`
§6b) named: a real geometric origin / projective surface over a finite ground at ∞. The 𝔽₁ program has now
proved, six independent ways, that NO existing 𝔽₁-base IS that object — sharpening the open problem to a
single transcendence/cardinality type gap.

---

## 6. Honest status of the 𝔽₁-construction attempt.

The 𝔽₁-construction attempt is **HONESTLY NEGATIVE and CLOSED, not constructive.** It did not find the scaled
conjugation; it proved — by exhausting the six independent candidate grounds and finding each scale-free or
wrong-scale for one converging reason — that **the finite ground at ∞ is not supplied by any 𝔽₁-base**, because
the arithmetic scale `q` is the cardinality of a real finite field and the archimedean place structurally is
not one. The value delivered is a strengthened no-go (`no 𝔽₁-ground carries an archimedean arithmetic scale`)
and a sharp blueprint for candidate N (a degenerating family with a finite special fiber at ∞, or an
archimedean Frobenius automorphism with finite eigenvalue `q`), with the obstruction pinned to a single
transcendence/cardinality type gap. The path that remains is the new-object path (N), not any 𝔽₁ ground.
