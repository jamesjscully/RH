# Attacking the surface S²/ℤ directly, as a representability question (NEXT #1, load-bearing)

**Date:** 2026-06-06. **Tags:** [THM] (Künneth, Atiyah–Bott trace, the λ=1 divergence), [computed]
(the regularized finite parts + the three falsifier axes, robust across 3 bases), [CONJ] (over-ℤ
representability of H¹(S²)). **Module:** `scripts/numerics/witness/square_representability.py`
(+ 1 `falsify.py` row). **Verdict: RH-SILENT** — the naive product surface S×S factorizes through the
base. **21st Euler-product confirmation.**

## The item

The metric-perturbation route on the 1-dim base `bar(Spec ℤ)` is CLOSED (DONE #0,
`green_current_perturbation.py`): no local-metric move couples the finite Euler piece to the DH-shared
archimedean form. The agenda's reading of that closure: **the missing structure is the SECOND DIMENSION,
not a metric on the 1-dim base** — the surface `S²/ℤ`, where the cross-place coupling could be
INTRINSIC to the geometry. The item asks: frame the `H¹(S²)`-over-ℤ obstruction (the "continuous
Frobenius `Δ·Δ=∞`" wall) as a **representability** question, and check whether the surface pairs the
finite primes against the archimedean place GEOMETRICALLY (intrinsic to S²), not as a perturbation.

## What I built (executable)

1. **The `Δ·Δ=∞` wall as a regularization.** `(Γ_λ·Δ)=Tr(θ_λ)=1/|1−λ|` (lift_obstruction.py); near
   `λ=1` this is `~1/|u|` (the corner Coulomb tail). I regularized by removing the corner `|u|<ε` and
   subtracting the **universal Coulomb tail** `∫_{ε<|u|} (1/|u|) g(u) du = 2log(width/ε)`. The tail
   depends ONLY on the corner geometry, NOT on arithmetic. Computed: the **finite part is
   ε-independent** (`+0.16147` at ε=1e-3, `+0.16157` at ε=1e-4), confirming the divergence IS exactly
   the universal geometric tail. So the surface's only candidate intrinsic self-pairing is this finite
   remainder.

2. **The Künneth split + the FACTORIZATION test.** On a product surface,
   `H¹(S²)=H⁰⊗H¹ ⊕ H¹⊗H⁰`, and the middle `H²` contains the genuinely two-dimensional
   `H¹(S)⊗H¹(S)` ("product of zeros") slot. I built the single-place archimedean Gram `A` (from
   `Re ψ(¼+ir/2)`, the Γ_ℝ density) and finite prime Gram `P` (from the log-derivative coefficients —
   `Λ(n)` for ζ, signed for DH), then the **Künneth cross slot** `C = A⊗P + P⊗A` — the only place a
   geometric prime↔archimedean coupling could live on the product surface.

3. **Two falsifiable hypotheses, decided numerically.**
   - **(H-geom)** the surface couples primes↔archimedean GEOMETRICALLY: `C`'s regularized finite part
     carries the RH sign and is Euler-borne in a way NOT inherited from the base → re-opens construction.
   - **(H-fact)** `C` FACTORS through the single-place base forms: it is the tensor square of the same
     1-dim data, RH-silent, the square buys nothing.

## The decisive computed facts (robust across 3 basis choices)

| fact | value | meaning |
|---|---|---|
| `max\|A_ζ−A_DH\|` | **0.0 exactly** | the archimedean (dominating) factor is **DH-shared** |
| `C = A⊗P + P⊗A` | by construction `f(A,P)` | the product surface's cross slot is the **tensor of the BASE forms** — no new datum enters |
| Kronecker bound `cross_diff ≤ 2‖A‖·‖P_ζ−P_DH‖` | **tight** (all 3 bases) | `C`'s ζ/DH variation is INHERITED from `P`, modulated by the DH-shared `A` |
| sig(C_ζ) vs sig(C_DH) | `(11,14,0)` vs `(12,13,0)` | Euler-borne YES — but inherited from `P` |
| sig(C) on-line vs off-line plant | `(12,13,0) = (12,13,0)` (all 3 bases) | **does NOT distinguish the line** — sees-zeros NO |
| regularized finite part | `+0.161`, ε-independent | the surface's self-pairing = universal Coulomb tail (DH-shared) + finite part inheriting the base's circular positivity |

## Finding [THM + computed]

**The naive product surface S×S over ℤ is the WRONG second dimension — its Künneth factorizes.**
The Künneth cross slot `C = A⊗P + P⊗A` is, *by construction*, a function of the single-place base forms
`(A,P)` alone. The archimedean factor `A` is **exactly** DH-shared (`max|A_ζ−A_DH|=0`, robust), so `C`
is the base prime form `P` (Euler-borne, inherited) merely MODULATED by the DH-shared archimedean form.
Its Euler content is **inherited from the 1-dim base, squared** — NOT intrinsic to the geometry of S².
The `Δ·Δ=∞` divergence regularizes to a UNIVERSAL (DH-shared, geometry-only) Coulomb tail plus a finite
part that inherits the base's circular positivity. Concretely: the cross slot's signature is Euler-borne
(differs ζ/DH) but **does not distinguish on-line from off-line zeros** (identical signature on both
plants, robust across 3 bases) — the hallmark RH-silent failure.

**Verdict: Euler-borne YES (inherited from `P`), sees-zeros NO (on=off signature), independent NO
(inherits the base prime form's circular positivity) → RH-SILENT.** The product surface buys nothing
the 1-dim base lacked; the cross-place coupling is STILL a perturbation of the one (archimedean) place,
now tensored. **21st Euler-product confirmation.**

## What the measurement names (the next missing structure)

The second dimension is genuinely NECESSARY — `Re s=½ ⟺ |α|=q^{1/2}` is the square root of `|α|²=q`, a
2-dim self-intersection number (`F-sym2-os-bridge` pass-two). But the **naive product** `S × S` is the
wrong realization: its `H¹⊗H¹` splits as `base ⊗ base`, so the diagonal `Δ` is a sum of *decomposable*
classes and `Δ·Δ` reduces to base data (the Coulomb tail + a factorized finite part). What is needed is
a **NON-PRODUCT surface** whose `H¹⊗H¹` does NOT split as `base⊗base` — equivalently, a surface whose
**Néron–Severi / Hodge class is NOT of product type**, so the diagonal is an **INDECOMPOSABLE
correspondence**. That indecomposable correspondence-algebra is precisely the **missing `End(S²/ℤ)`**
this program has named from three directions before:
- the missing polarization relation `F^†=(deg)·F^{-1}` (`frobenius_self_norm.py`, DONE);
- the missing Rosati off-diagonal `Tr F` as a *correspondence* (not just a number) (`off_diagonal.py`);
- the BGS §6.3 surface with a Kähler `c₁(H,k)` (`arakelov_signature.py`).

So this pass **unifies the "second dimension" target with the "missing `End(S²/ℤ)`" target**: the
second dimension must come with an indecomposable diagonal (a non-product Hodge class), not a bare
product of two copies of the base. *The square-root structure cannot be a naive self-product.*

## Honest subtleties

- The `5×5`-center Gaussian basis (and the `4`/`5`-center variants) is a coarse finite-rank model; the
  load-bearing facts are the EXACT `max|A_ζ−A_DH|=0`, the BY-CONSTRUCTION factorization of `C` through
  `(A,P)`, the tight Kronecker bound, and the robust on=off-line signature equality — all basis-robust.
- "Factorizes" is established rigorously (the cross slot is literally `A⊗P + P⊗A`, a function of the
  base forms); the numerical Kronecker bound merely confirms the inherited variation magnitude.
- I do not claim the `(11,14,0)`/`(12,13,0)` signatures are the exact arithmetic Hodge index — they are
  the coarse-model cross-slot signatures, whose *invariance* under the on/off-line plant is the point.
- The off-line "plant" enters through `P` (the explicit formula moves weight between primes and zeros);
  the sees-zeros failure is that the product-surface cross slot reacts identically to on- and off-line
  plants — i.e. it is blind to zero LOCATION, only to the prime perturbation magnitude.

## Falsifier row

Added to `falsify.py` REGISTRY: "naive product surface S x S over Z (Künneth cross slot A⊗P+P⊗A)" →
RH-SILENT (Euler-borne Y inherited / sees-zeros N / independent N).
