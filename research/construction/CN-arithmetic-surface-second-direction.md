# Candidate N — the arithmetic surface's SECOND direction (2026-06-06)

**Verdict: CHAR_DIVIDE_CLOSED.** The second direction of the arithmetic surface does NOT manufacture a
finite ground at infinity. Attacked with the freshest cutting-edge object (the **archimedean
Fargues–Fontaine curve / twistor P¹**, Scholze-school 2024); it degenerates every finite datum to its
archimedean type. Completes the exhaustion: the char-0/char-p divide is irreducible at `∞`.

## The angle (the only road left)

Over `𝔽_q`, the Weil RH proof lives on a **surface** `C ×_{𝔽_q} C` (2-dimensional). The analog for `ℚ` is
`Spec ℤ ×_{𝔽₁} Spec ℤ`. Candidate N's fresh hope: the missing finite ground at `∞` comes from the
**SECOND direction** (the family parameter / second copy), where infinity in one direction meets a finite
structure in the other — and as a **degenerating family** whose special fibre at `∞` lives over a genuine
finite constant field (NOT Deninger's flow, NOT a static smooth surface — those were already closed by
R6/R7 and `square_representability.py`).

## What was tested [BUILT / computed / cited]

### 1. The product / surface structure — does the second copy supply the first's finite ground?
[computed, decisive structural asymmetry]

> **`𝔽_q` case:** `C ×_{𝔽_q} C`. The base `𝔽_q` **exists PRIOR to the product** — the product is taken
> *relative to* `𝔽_q`. The finite ground is a shared **INPUT** to both directions, never an output of the
> product. The surface is proper /`𝔽_q` because `𝔽_q` is already the base.
>
> **`ℚ` case:** `Spec ℤ ×_{𝔽₁} Spec ℤ`. The would-be shared base `𝔽₁` is **exactly what is missing.** The
> product is over `𝔽₁`, which has no finite cardinality at `∞`. The second copy is *also* `Spec ℤ`, whose
> archimedean fibre is the **same** archimedean place — residue field `ℝ` (`ℂ` after base change), **not
> finite**. The product of two archimedean-at-`∞` objects is archimedean-at-`∞` **squared** (a second
> continuum), not a finite cardinality.

The finite ground in the `𝔽_q` surface is **not created by the second direction** — it is the pre-existing
base that both directions share. The second direction cannot supply what neither copy has.

This is the prior closure made structural: `square_representability.py` (21st Euler confirmation) already
found the naive `S × S /ℤ` Künneth cross slot `A⊗P + P⊗A` **factorizes as base⊗base**, the archimedean
factor `A` is **DH-shared** (`max|A_ζ − A_DH| = 0`), and the signature does **not** flip on/off-line. The
second dimension is *necessary* (the square-root `|α|=√q` is genuinely 2-dim) but the product is the *wrong*
second dimension. The Hecke/non-product correspondence (`hecke_correspondence.py`, `theta_twisted_pairing.py`,
22nd–23rd confirmations) supplied genuine non-productness but re-collapsed to a Sylvester congruence of the
DH-shared archimedean `A` — RH-silent.

### 2. The archimedean Fargues–Fontaine curve / twistor P¹ — the freshest realization [cited, primary source]

The cutting-edge object Candidate N must deploy: the **archimedean FF curve `X_ℝ`** (twistor P¹), the
Scholze-school 2024 archimedean analogue (Vizcarra seminar notes, Berkeley 2024, fetched + read in full).
It is built EXACTLY to be the second/twistor direction. Its properties decide the question:

| datum | p-adic FF curve `X_{ℚ_p,C}` | archimedean FF curve `X_ℝ` |
|---|---|---|
| residue field at closed pts | alg-closed nonarch (untilts of `C♭`) | **`ℂ`** (property (i): no real points) |
| local field's residue field | **genuine finite `𝔽_q`** — scale `q` REAL | none — archimedean |
| structure / Aut at `∞` | Frobenius `φ` carrying scale `q` | `ℍˣ/ℝˣ`, stab(∞)=`O(2) → ℤ/2 = Gal(ℂ/ℝ)` |
| slopes (bundle classification) | `λ ∈ ℚ` (discrete arithmetic) | `λ ∈ ½ℤ`, indecomposable `𝒪(1/2)` |
| test category `†`-reduction | perfectoid (char `p`) | nil-perfectoid, `A^{†-red} ≃ ℂ` |
| Banach–Colmez realization | char-`p` perfectoid spaces | `ℝ^la` (the real-analytic **line**, continuum) |

**The decisive fact:** the archimedean FF curve **degenerates every finite datum to its archimedean type:**
- finite residue field `𝔽_q` → **`ℂ`** (continuum — confirms R6/R7: the archimedean fibre is smooth, no
  finite residue);
- Frobenius scale `q` → **`ℤ/2`** (the order-2 COUNT `O(2) → Gal(ℂ/ℝ)` — confirms R8 `F†=F̄` = the free
  involution, the *reality without scale*);
- discrete slopes → **`½`** (the self-dual half `𝒪(1/2)` = the FE axis `Re s=½` — confirms R3's free
  self-dual `½`, NOT an arithmetic `q`).

The p-adic curve geometrizes local Langlands *precisely because* its local field has a finite residue field
carrying `q`. The archimedean curve, the faithful twistor analogue, has **none of it** — residue field `ℂ`,
structure group only `ℤ/2`, slopes only `½`. **No finite cardinality survives the second direction.**

### 3. Connes–Consani `C = Spec ℤ /𝔽₁` counting + the degenerating-family hope [cited, computed]

Connes–Consani's counting `N(q)` for the would-be curve `C = Spec ℤ` over `𝔽₁` is a **distribution on
`q ∈ (1,∞) CONTINUOUS`**, `N(q) → −∞` at `q=1` (infinite genus). The variable `q` here is the **continuum
scaling parameter `ℝ₊ˣ`** — the same free self-dual `½`/continuum that the `𝔽₁`-survey (R3, T-tropical)
already classified as WRONG_SCALE. The degenerating-family / second-direction picture inherits exactly this
continuum: the "special fibre at `∞`" of any archimedean family is the archimedean FF fibre (residue field
`ℂ`), and the family parameter `q` runs continuously, never landing on a finite cardinality. Deninger's own
direct construction (the foliated dynamical system, the second-direction analogue) is **leafwise cohomology
— infinite-dimensional, a flow** — which is exactly the "Deninger's flow" `f1-construction.md` says
Candidate N must NOT be.

### 4. Anchor — `C × C /𝔽_q`, Hodge index forces the radius [computed, PASS]

`|α| = √q = 2.0` recovered on-circle for `E/𝔽_4`, `θ=0.7`, without assuming the zeros. The surface `E ×_{𝔽_q} E`
is proper over `𝔽_q`; the Hodge-index signature `(1, ρ−1)` on `H¹_prim` of the surface is neg-definite
**iff** `|α|=√q`. Crucially BOTH directions of the surface share the **one finite ground `𝔽_q`** that is the
base — confirming the asymmetry in §1: the finite ground is the input the surface is built over, never the
output of taking the product. The archimedean fibre of the surface stays archimedean (R6/R7: smooth, no
degeneration), now confirmed at the deepest level by the archimedean FF curve.

### 5. DH falsifier [computed, PASS — the structure is right but RH-silent]

`falsify.py`: the prior second-direction modules (`square_representability` RH-SILENT, `hecke_correspondence`
RH-SILENT, `theta_twisted_pairing` RH-SILENT) all carry the Euler product (DH-refusing where the prime form
`P` enters) but their archimedean factor `A` is DH-shared and the signature does not flip on/off-line. The
second direction **fails for DH at the prime form** (no Euler product ⟹ no `P` ⟹ no surface), and is
**RH-silent at the archimedean form** (DH-shared `A`). The decisive object — a finite special fibre at `∞`
carrying `q` — is the one thing DH would also lack, and it is exactly what does not exist.

## Why CHAR_DIVIDE_CLOSED (not VIABLE_LEAD)

A VIABLE_LEAD required a **genuine proper curve / finite special fibre at `∞` supplying the scale `q`**
(anchored, DH-failing). The freshest, most faithful candidate — the archimedean Fargues–Fontaine
curve, purpose-built as the twistor/second direction — supplies instead:
- a residue field `ℂ` (continuum, not finite),
- a structure group `ℤ/2` (the order-2 count `F†=F̄`, the *free* reality),
- slopes `½` (the FE axis, the *free* self-dual half).

These are **Step-A objects** (the complex/twistor/continuum structure that is NOT a finite ground): the
reality (`F†=F̄`, the order-2 datum, the count) is there and free; the scale `q` (a finite cardinality, a
MODULUS) is absent and structurally so. The second direction supplies a **second continuum**, not a finite
ground. The char-0/char-p divide is **irreducible** at the archimedean place: char `p` has a finite residue
field that carries `q` and forces purity; char 0 (the archimedean place) has residue field `ℂ`/`ℝ`, and
**no degeneration manufactures a finite residue** — degeneration of an archimedean family lands on the
archimedean FF fibre, residue field `ℂ`, every time.

This is the same atom as R8/PA/the geometric no-go (`q` is a property a real finite field HAS and `∞`
structurally cannot), now confirmed against the **deepest cutting-edge object the field has produced** for
exactly this purpose. The `𝔽₁`-base path was closed (no base supplies the scale); the new-object /
degenerating-family / second-direction path is now closed too. **The exhaustion is complete: every route to
the finite ground at `∞` lands on the archimedean type (count / continuum / `½` / period), never the
discrete finite `q`.**

## What survives (the honest residual)

The archimedean FF curve **is** the right `Step A` object — it gives the FE (`F·F†=[deg]`), the duality, the
order-2 reality, the `½` axis, archimedean-natively and in families (relative twistor P¹'s over nil-perfectoid
test objects). What it provably does not give is **Step B = `|α|=√q`** (positive-definiteness at the finite
scale `q`). To cross would require the second copy of `Spec ℤ` to *already have* a finite constant field at
`∞` — which it does not — i.e. it requires the `𝔽₁` ground itself, not the product over it. The product
cannot create the base it is taken over. **No degeneration manufactures a finite residue field at `∞`.**

## Sources
- Twistor P¹ as the archimedean Fargues–Fontaine curve (Vizcarra, Berkeley seminar, Oct 2024):
  https://math.berkeley.edu/~avizeff/seminars/archimedean-FF.pdf
- Connes–Consani, Schemes over 𝔽₁ and zeta functions (Compositio): https://math.jhu.edu/~kc/compositiofinal.pdf
- Connes–Consani, On the Jacobian of Spec ℤ (2026); Publications list: https://math.jhu.edu/~kc/Publ2026.pdf
- Deninger foliated dynamical systems / leafwise cohomology: https://arxiv.org/pdf/math/0505354 ,
  https://arxiv.org/pdf/2508.15971
- nLab Fargues–Fontaine curve (p-adic, residue field = untilt): https://ncatlab.org/nlab/show/Fargues-Fontaine+curve
