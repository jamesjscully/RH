# 201 - Static product surface does not construct End(S^2/Z)

Status: no-go + product-surface/Kunneth boundary, 2026-06-20. Sixty-fourth
cycle of the doc-137 construction arc. Doc 200 killed formally adjoining
the lambda^{1/2} cover. This document tests the next carrier-shaped repair:
take the second dimension literally as a static product surface `S x S`,
read the middle Kunneth slot `H^1(S) x H^1(S)`, and promote that product
slot to the missing square correspondence object.

Witness, lead-reran this cycle:
`prime_int_n1b_static_product_surface_no_go` (SPS1-SPS10 ALL PASS) --
the product Kunneth cross slot is exactly `A tensor P + P tensor A`, the
archimedean factor is DH-shared, Euler variation is inherited from the
base prime form, the product slot does not distinguish on-line from
off-line zero input, diagonal self-intersection regularizes only by a
universal corner tail, the smooth product surface has pure weight-2
middle cohomology and `N=0`, rank room for a Jordan block is unused
without a degeneration, nonzero `N` belongs to an external degenerating
family with special fiber, DH dies before any product-surface carrier, and
no indecomposable square correspondence/Rosati/R1 boundary data is built.

Adjacent witnesses, lead-reran this cycle:
`square_representability` (exit 0) -- the older surface representability
probe: `Delta.Delta` has a universal Coulomb corner and the Kunneth cross
slot factorizes through one-place forms;
`surface_archimedean_N` (exit 0) -- the older surface monodromy probe:
smooth `C x C` has rank room but `N=0`; nonzero `N` requires a
degenerating family.

## 1. Purpose

The product surface is the first honest-looking square-shaped object after
the formal repairs are removed. It contains the right formal middle slot:

```text
H^2(S x S) contains H^1(S) x H^1(S).
```

Over finite fields, the product `C x C` is smooth and proper; its middle
cohomology has weight 2, and products of Frobenius eigenvalues have
modulus `q`. This makes the surface look like the right home for the
square-root radius and the Hodge-index/Rosati story.

The issue is that the static product does not create the missing
correspondence. Its Kunneth cross pairing is a tensor expression in the
one-place archimedean form `A` and one-place prime form `P`:

```text
C = A tensor P + P tensor A.
```

Thus the second dimension supplies no new prime-to-archimedean coupling.
The archimedean factor is DH-shared, and the Euler variation is inherited
from the base prime form. Likewise, the smooth surface has `N=0`: it has
rank room for monodromy, but no degeneration. The nonzero nilpotent `N`
that gives a monodromy split lives on a degenerating family with special
fiber, not on the static product surface.

This document is local. It does not reject a future non-product,
indecomposable, compactified square correspondence or family carrier. It
rejects only the shortcut:

```text
static product surface S x S / product Kunneth middle slot = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 201.1 (The static product surface is not the square correspondence).

For the static product surface, the Kunneth cross slot is

  C = A tensor P + P tensor A,

where A is the one-place archimedean form and P is the one-place finite
prime form. The archimedean factor A is DH-shared. Therefore the product
surface's Euler variation is inherited from the base prime form and
modulated by a DH-shared archimedean factor; no new carrier-native
prime-to-archimedean coupling is constructed.

The regularized diagonal self-intersection has the universal corner
divergence already present in the scaling orbit. Its finite remainder does
not construct a new square correspondence algebra.

Moreover, a smooth product surface has pure middle cohomology with
monodromy nilpotent N=0. It may have enough rank to host a Jordan block,
but the block is not present. A nonzero nearby-cycle N, and hence the
monodromy split, belongs to a degenerating family with special fiber, not
to the static smooth product surface.

Consequently the static product surface constructs no indecomposable
square correspondence, square-side iota/properness theorem, square H2,
intersection form, Frobenius graph, positive Rosati involution, Laurent
boundary map, torsor splitter, or DD.4 weight>=1 datum.

Therefore static S x S / product Kunneth data cannot itself be promoted to
End(S^2/Z).
```

Verdict label:

```text
N1B_STATIC_PRODUCT_SURFACE__KUNNETH_FACTORS_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_static_product_surface_no_go` verifies the R1 gate, with
`square_representability` and `surface_archimedean_N` rerun as adjacent
witnesses.

SPS1 records the product identity: the Kunneth cross slot is exactly
`A tensor P + P tensor A`. No extra square datum enters.

SPS2 records that the archimedean factor is DH-shared:
`max |A_zeta - A_DH| = 0`.

SPS3 records that the zeta/DH variation of the cross slot is bounded by
the base-prime variation tensored with the shared archimedean factor. The
Euler content is inherited from `P`; it is not a new product-surface
coupling.

SPS4 records line-blindness at the product slot: planting an off-line zero
and planting an on-line zero move the product signature to the same
signature. The product slot reacts to the base perturbation, not to an
independent on/off-line distinction.

SPS5 records the diagonal self-intersection wall:
`Gamma_lambda . Delta = 1/|1-lambda|` has the universal corner divergence.
Subtracting the Coulomb tail leaves a stable finite part, but this is a
regularized one-place corner phenomenon, not a square correspondence
construction.

SPS6-SPS8 record the monodromy issue. Smooth `C x C` has pure weight-2
middle cohomology and `N=0`, so `M(N)` is a single weight. The rank room
for a Jordan block is real but unused. A nonzero `N` is supplied only by a
degenerating family with special fiber.

SPS9 records DH-vacuity one level earlier: DH has no `H^1`, no product
surface, and no family to degenerate. That is a good carrier guard, but it
does not construct zeta-side correspondences.

SPS10 records the carrier failure: no indecomposable square
correspondence, square-side `iota`/properness, square H2, intersection
form, correspondence algebra, Frobenius graph, positive Rosati, Laurent
boundary, torsor splitter, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-201:
  NEWLY CLOSED THIS CYCLE:
    - static product surface S x S / product Kunneth middle slot as
      End(S^2/Z), indecomposable square correspondence, new
      prime-to-archimedean coupling, square-side iota/properness,
      square H2/intersection form, Frobenius graph, Laurent boundary
      data, torsor splitter, DD.4 weight>=1 datum, or positive Rosati
      (doc 201).

  STILL ADMISSIBLE:
    - a non-product compactified square whose middle correspondence is
      indecomposable rather than Kunneth-factored;
    - a family-of-surfaces carrier with a carrier-native special fiber and
      nearby-cycle N;
    - a square-side iota/properness theorem that makes the correspondence
      algebra global rather than one-place-tensored;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The static product surface is useful as a failure mode:
the second dimension is necessary, but product Kunneth is the wrong second
dimension. R2 remains locked.

## 5. Kill Conditions

```text
KILL-SPS.1 static S x S as End(S^2/Z)
  A proposal identifies the static product surface with the compactified
  square correspondence algebra. Kill it unless it constructs an
  indecomposable correspondence algebra, not just Kunneth product data.

KILL-SPS.2 Kunneth cross slot as new prime-archimedean coupling
  A proposal uses A tensor P + P tensor A as the missing coupling. Kill it:
  the archimedean factor is DH-shared and the Euler variation is inherited
  from the base prime form.

KILL-SPS.3 regularized Delta.Delta finite part as square properness
  A proposal subtracts the universal corner tail and promotes the finite
  part to properness. Kill it unless the finite part is realized by a
  carrier-native square correspondence theorem.

KILL-SPS.4 rank room as monodromy
  A proposal says the product middle cohomology has enough rank for N and
  treats that as N. Kill it: smooth product cohomology has N=0.

KILL-SPS.5 external degenerating family as static surface data
  A proposal imports a nearby-cycle N from a degeneration and then assigns
  it to the static surface. Kill it unless the family and special fiber are
  part of the constructed carrier.

KILL-SPS.6 DH-vacuity as zeta correspondence construction
  A proposal notes DH has no product-surface carrier and promotes that to
  End(S^2/Z). Kill it unless the zeta-side square maps, correspondences,
  and Rosati are actually constructed.
```

## 6. Board

```text
doc-137 R1, cycle 64 = doc 201:
  N1B_STATIC_PRODUCT_SURFACE__KUNNETH_FACTORS_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
static S x S supplies product Kunneth data only. Its cross slot factors
through one-place forms, smooth middle cohomology has N=0, and nonzero N
requires a degenerating family with special fiber.

What remains: construct an indecomposable compactified square
correspondence; construct a family-of-surfaces carrier with special fiber
and nearby-cycle N; solve square-side iota/properness; or return to the
in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
