# 209 - Global radius descent does not construct End(S^2/Z)

Status: no-go + descent-rigidity boundary, 2026-06-20.
Seventy-second cycle of the doc-137 construction arc. Doc 208 killed the
local shortcut: local Euler factors have edge data but no local weight-1
purity carrier. This document tests the next repair: maybe global descent of
all edge/determinant data forces the center once the local factors are glued.

```text
local edges / determinants
  -> global determinant / FE pairing
  -> forced global even split
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_radius_descent_assembly_no_go` (RDA1-RDA6 ALL PASS) --
the function-field global carrier has determinant, Poincare pairings, and
even split; a balanced modulus redistribution preserves determinant and
pairings while breaking the even split; zeta-style cross-prime determinant
products do not couple the radii; DH fails before the question; and no
square/Rosati/R1 data is built.

Adjacent witness, lead-reran this cycle:
`radius_descent_assembly` (exit 0) -- the older M4r probe: descent assembles
the product edge, but not the split. The FE/determinant sees the product of
moduli, never the individual moduli.

## 1. Purpose

Doc 208 moved purity to the right altitude: it is not per-prime over zeta;
it can act only after a global glued weight-1 carrier exists. The immediate
repair is to hope the global gluing itself supplies the missing center:

```text
The Euler product gives all local edges.
The FE/determinant glues them into a global product.
The global product forces all radii to split evenly.
```

The issue is that product data and radius data have different strength. A
determinant is a product constraint. The center requires uniform modulus
constraints on individual factors. A balanced redistribution can preserve the
product while moving individual radii.

This document rejects only the shortcut:

```text
global determinant/FE descent itself forces purity and therefore constructs
End(S^2/Z).
```

## 2. Lemma

```text
Lemma 209.1 (Radius descent has product but no split).

Let a global weight-1 carrier have Frobenius eigenvalues

    alpha_1, ..., alpha_g, alpha_{g+1}, ..., alpha_{2g}

with Poincare pairings alpha_i alpha_{g+i}=q and determinant
prod_i alpha_i=q^g. These are the FE/product constraints.

For g>=2 and r != 1, replace the moduli in two dual pairs by

    r sqrt(q), sqrt(q)/r
    sqrt(q)/r, r sqrt(q).

Each Poincare pairing still has modulus q, and the determinant modulus is
still q^g. But the even split |alpha_i|=sqrt(q) for every i is false.

Therefore the global even split is not a function of determinant plus
Poincare pairings. It is extra positivity/Rosati information on the global
weight-1 carrier.

The same obstruction appears in zeta-style multi-prime determinant data:
off-even radii can be planted at two primes while preserving each local
determinant, hence also the global determinant product. The global FE couples
no two prime radii into an even split.

DH has no Euler product, no Satake/local determinant data, and no edge to
assemble, so it fails before this descent-rigidity question is typed.

Consequently radius descent constructs no global gr^W_1 carrier over Z, no
carrier-native purity theorem, no global even-split rigidity, no q-power map,
no uniform modulus bound, no DH-killing carrier, no finite constant field, no
square-side iota/properness theorem, no square H2, intersection form,
correspondence algebra, Frobenius graph, Laurent boundary data, torsor
splitter, DD.4 weight>=1 datum, or positive Rosati.

Therefore global radius descent cannot itself be promoted to End(S^2/Z).
```

Verdict label:

```text
N1B_RADIUS_DESCENT_ASSEMBLY__PRODUCT_NOT_SPLIT__NO_GO.
```

## 3. Proof

`prime_int_n1b_radius_descent_assembly_no_go` verifies the R1 gate, with
`radius_descent_assembly` rerun as the adjacent witness.

RDA1 records the function-field global anchor. For the genus-2, `q=9`
model, the on-line carrier has determinant `q^g=81`, pairings `9,9`, and
all moduli equal to `sqrt(q)=3`.

RDA2 records the decisive redistribution. With `r=e^0.4`, the moduli become

```text
4.4754741, 2.0109601, 2.0109601, 4.4754741.
```

The determinant remains `81`, the pairings remain `9,9`, but the even split
is false. Thus determinant plus pairing cannot be the radius theorem.

RDA3 records the zeta-style multi-prime mirror. At `p=5,7`, a cross-prime
off-even plant preserves the determinant product

```text
9.6549157373e16
```

before and after redistribution, while both prime radii move off their
centers. There is no cross-prime modulus link in the determinant data.

RDA4 records the carrier guard. DH has no Euler product, no Satake
parameters, no local determinants, no edge to assemble, and no weight-1
carrier to glue.

RDA5 records the missing discriminator. The on-line and redistributed
configurations have the same determinant/pairing data but different radii.
Only a positivity/Rosati datum on the global weight-1 carrier can distinguish
them, and that datum is not supplied by determinant descent.

RDA6 records the construction failure: no global `gr^W_1` carrier over `Z`,
carrier-native purity theorem, global even-split rigidity, q-power map,
uniform modulus bound, DH-killing carrier, finite constant field, square-side
`iota`/properness, square H2, intersection form, correspondence algebra,
Frobenius graph, positive Rosati, Laurent boundary, torsor splitter, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-209:
  NEWLY CLOSED THIS CYCLE:
    - global radius descent as End(S^2/Z), determinant/product edge as
      center, determinant-plus-pairing as uniform modulus, cross-prime FE
      coupling as radius rigidity, determinant descent as positivity/Rosati,
      finite constant field, Frobenius/base size, square-side
      iota/properness, square H2/intersection form, Laurent boundary data,
      torsor splitter, DD.4 weight>=1 datum, or positive Rosati (doc 209).

  STILL ADMISSIBLE:
    - a global glued carrier that actually constructs `gr^W_1` before
      applying purity;
    - a non-product compactified square whose correspondence algebra
      supplies positive Rosati, not only determinant/pairing data;
    - a zeta-native positivity theorem whose hypotheses are built by the
      carrier and which kills DH/Epstein at carrier formation.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. This cycle sharpens the order of construction again:
global gluing may assemble the edge/product, but the split/center requires
positive Rosati on a carrier already constructed. R2 remains locked.

## 5. Kill Conditions

```text
KILL-RDA.1 determinant edge as center
  A proposal reads Re(s)=1/2 from the global product edge alone. Kill it:
  determinant/product data gives the edge, not the split.

KILL-RDA.2 determinant plus pairing as uniform modulus
  A proposal says FE/pairing forces all individual radii. Kill it: the
  balanced redistribution preserves determinant and pairings while breaking
  the even split.

KILL-RDA.3 cross-prime product as radius coupling
  A proposal uses a global determinant product to couple prime radii. Kill it
  unless it supplies an additional carrier-native positivity/Rosati datum.

KILL-RDA.4 descent before positivity
  A proposal applies the even split before constructing positive Rosati on a
  global `gr^W_1` carrier. Kill it: the split is exactly the missing
  positivity, not a determinant consequence.

KILL-RDA.5 radius descent as DH guard
  A proposal says this descent distinguishes zeta from DH. Kill it unless the
  zeta carrier is constructed; DH already fails at no Euler product/Satake
  data.

KILL-RDA.6 radius descent as End(S^2/Z)
  A proposal promotes the product-edge assembly directly to the square
  correspondence algebra. Kill it unless it constructs square H2,
  intersection form, correspondences, Frobenius graph, Laurent boundary data,
  DD.4 weight>=1 datum, and positive Rosati.
```

## 6. Board

```text
doc-137 R1, cycle 72 = doc 209:
  N1B_RADIUS_DESCENT_ASSEMBLY__PRODUCT_NOT_SPLIT__NO_GO.

What got built: no End object. The value is a sharper descent theorem:
global Euler/FE assembly supplies product-edge data only; it does not force
the individual radius split.

What remains: construct the global `gr^W_1` carrier; construct positive
Rosati on it; construct the q-power/fixed-point/scaling carrier; construct
an indecomposable compactified square correspondence; solve square-side
iota/properness; or return to the in-house PFD/Xbar DD.4 weight>=1
obstruction.
```
