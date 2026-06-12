# 148 - PFV2 classical relative divisor obstruction

Status: bounded no-go from the doc-147 candidate shot / Q134.1
internal result, 2026-06-11. This is not a B1 construction, not an
external answer, and not a witness license. It kills only the ordinary
relative divisor/idele presentation exposed by PFV2-REL-DIV(p,q).

## 1. Purpose

Doc 147 showed that a relative divisor complement is the first PFV2
candidate with a genuinely structural complement. It still held at:

```text
HOLD_RELATIVE_FIRST_MAP.
```

This document asks whether the classical relative divisor record really
has a first p,q+complement source, or whether it is just an all-places
divisor object with p and q distinguished.

Answer:

```text
The ordinary product/restricted-product relative divisor presentation
collapses to all-places projection. It does not satisfy PFV2-REL-FIRST.
```

## 2. Covered Class

Call a proposal `PFV2_REL_DIV_classical` if it satisfies all of:

```text
C148.1 ordinary divisor/idele source
  The source is built from the classical divisor, idele, Arakelov
  divisor, or all-places product-formula category for a global carrier.

C148.2 relative tuple
  The p,q source is a tuple

    (D_p, D_q, D_{not p,q}, certificate)

  where D_{not p,q} is the complementary divisor/idele component.

C148.3 assembly equivalence
  There is an assembly map

    assemble(D_p, D_q, D_{not p,q}) = D

  into the all-places divisor/idele object, and the certificate is the
  usual all-places principal/product-formula certificate for D.

C148.4 no extra relative universal property
  The relative tuple has no source axiom beyond the all-places object
  plus the marking of p and q.

C148.5 inherited first map
  Any proposed kappa_div factors through the assembled all-places
  object or through ordinary coordinate projections from it.

C148.6 downstream unknown
  No theorem shows that M_C, F_C, or Tr_L needs the relative
  p,q+complement tuple rather than the assembled all-places object.
```

This class includes:

```text
direct sums of place divisors with p and q marked;
idele restricted products with two distinguished factors;
Arakelov divisors split into p, q, and complement components;
principal-divisor certificates attached after assembling the full
divisor.
```

## 3. Lemma

### Lemma 148.1

`PFV2_REL_DIV_classical` does not satisfy PFV2-REL-FIRST.

Verdict:

```text
REJECT_RELATIVE_PROJECTION
  if kappa_div factors through the all-places assembled object.

REJECT_MARKED_GLOBAL_SOURCE
  if the only extra data are the marked places p and q.

HOLD_RELATIVE_UNIVERSAL_PROPERTY
  if a later proposal adds a genuine relative source axiom not covered
  by C148.1-C148.6.
```

### Proof

PFV2-REL-FIRST requires the relative record to be first:

```text
S_{p,q}^{div} --kappa_div--> Y_{p,q}^{div}
```

must exist because the p,q components and complement form a source
object together. It must not exist merely because an all-places divisor
object was formed and then read through p and q coordinates.

Under C148.1-C148.3, the tuple

```text
(D_p, D_q, D_{not p,q}, certificate)
```

is equivalent to the all-places object D together with a marking of two
coordinates. The product-formula certificate is the certificate for D.
Thus the source relation is not relative-first; it is all-places first.

Under C148.4, the relative tuple has no additional source axiom. The
marking of p and q is exactly the kind of coordinate distinction that
doc 142 rejects when it is used as the first carrier-consuming map.

Under C148.5, kappa_div is inherited from the assembled object or from
coordinate projections. Therefore control exclusion, if true, is also
inherited from the ambient global source. PFV2 needs control failure at
the relative source or first map itself.

Under C148.6, even the relative tuple has not been shown to remain
load-bearing downstream. Doc 111 blocks promotion if M_C/F_C/Tr_L only
uses the assembled all-places object or forgets the complement.

Therefore the ordinary classical relative divisor presentation does not
pass PFV2-REL-FIRST. QED.

## 4. What The Classical Record Still Supplies

Allowed:

```text
a real structural complement object;
a useful calibration for product-formula experts;
source-level evidence that formal complements should be replaced by
divisor/idele complements;
a test bed for future relative universal-property claims.
```

Not allowed:

```text
claiming FIRST_MAP_PASS;
claiming Epstein/DH fail at the relative first map;
using marked p,q coordinates as a strict source;
running an A2 witness;
updating docs 103 or 113 as passed.
```

## 5. Surviving Escape

The only surviving relative-divisor route is:

```text
PFV2-REL-UPROP.
```

The target:

```text
There is a relative adelic/divisor source category whose p,q+complement
objects have a universal property, reflection theorem, or descent/gluing
axiom not equivalent to assembling an all-places divisor and marking p
and q.

kappa_div is legal because of that relative structure; controls cannot
form the relative object or map; B0_p and B0_q embed conservatively;
and the relative complement remains load-bearing downstream.
```

This is narrower than PFV2-REL-FIRST and is the remaining exact theorem
after killing the ordinary classical presentation.

## 6. Board Update

```text
PFV2-REL-DIV classical presentation:
  REJECT_RELATIVE_PROJECTION.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-REL-UPROP or another structural
  complement source not equivalent to all-places assembly.

A2 witness:
  still not licensed.
```

## 7. Relation To Existing Docs

```text
doc 142
  Supplies the all-places projection objection. This document applies
  it to the ordinary relative divisor tuple.

doc 143
  Supplies the no-free-complement requirement. Classical relative
  divisors satisfy complement structurality but not relative-first
  priority.

doc 147
  Supplies the PFV2-REL-DIV shot whose classical subfamily is rejected
  here.

doc 103
  Still HOLD: no FIRST_MAP_PASS.

doc 111
  Still blocks downstream forgetfulness.
```

## 8. Post-doc-149 Update

Doc 149 rejects the formal universal-property repair:

```text
PFV2_REL_UPROP_formal:
  REJECT_FORMAL_UPROP.
```

The surviving target is:

```text
PFV2-REL-REFLECT.
```

Thus PFV2-REL-UPROP remains only as an enclosing stage in the proof
history. Future work should ask for a native relative reflector,
localization, descent/gluing theorem, or carrier-reflecting envelope,
not a slice, fiber, pullback, or comma category over the all-places
source.
