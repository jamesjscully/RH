# 142 - PFV2 adelic source boundary

Status: bounded source-family audit / Q134.1 internal result,
2026-06-11. This attacks the adelic/product-formula subfamily left
open by docs 140-141. It does not kill global product-formula carriers.
It rejects all-places bookkeeping and post hoc two-place projection as
PFV2 first maps.

## 1. Purpose

Doc 141 sharpened the live A2 target to:

```text
PFV2-GLOBAL.
```

The remaining semantic home is adelic/product-formula structure. This
document asks whether a classical global product formula is already
enough.

Answer:

```text
No. A global product formula can make PF structural, but PFV2 also
needs a two-place carrier source and first map whose two-place field is
object data before trace. Projecting an all-places identity to p and q
afterward is another coordinate/readout operation.
```

## 2. Covered Class

Call a proposal `PFV2_adeles_bare` if it satisfies all of:

```text
A142.1 all-places source
  The source is an adelic, Arakelov, idele, divisor, or product-formula
  object whose product formula is stated over all places.

A142.2 two-place projection
  The PFV2 p,q pair is obtained by selecting two places, quotienting
  out the rest, freezing the rest to constants, or reading a two-place
  relation from the all-places formula after the global object exists.

A142.3 no two-place source object
  No object S_{p,q} exists whose definition requires the p and q
  towers, lengths, and complement/PF field simultaneously before any
  projection, trace, determinant, kernel, or mixed object.

A142.4 control exclusion inherited late
  Epstein/DH controls are excluded because they are not global-field
  adelic objects, but the first p,q map itself is only a projection or
  readout from the already accepted global object.

A142.5 downstream unknown
  No theorem shows that the two-place PF field remains load-bearing in
  M_C, F_C, or Tr_L.
```

This class includes:

```text
using the product formula as a scalar constraint after choosing p,q;
setting all other places to a compensating constant;
idele/divisor bookkeeping with no strict p,q source object;
adelic trace packages where p,q appear only as selected coordinates.
```

## 3. Lemma

### Lemma 142.1

`PFV2_adeles_bare` does not satisfy PFV2-GLOBAL.

Verdict:

```text
HOLD_GLOBAL_PF
  if the all-places product formula is structural but no p,q source
  object is named.

REJECT_COORDINATE_PROJECTION
  if the two-place field is only a projection/readout from an
  all-places object.

REJECT_DOWNSTREAM_FORGETFUL
  if the p,q field is formed but later forgotten before M_C/F_C/Tr_L.
```

### Proof

The all-places product formula can be genuine structure. This improves
on bare UFD pairs from doc 141: PF is not merely an equation imposed on
two independent valuation coordinates.

But PFV2-GLOBAL requires a two-place source and first map:

```text
S_{p,q} --kappa_PF--> Y_PF
```

where the p,q valuation field is object-defining before trace. Under
A142.1-A142.3, the object is global first, and the p,q field is read by
selecting or projecting places after the global product formula already
exists. That is not yet a p,q source object. It is all-places
bookkeeping plus a coordinate projection.

Under A142.4, control exclusion may be true at the level of "is this a
global-field adelic object?" but PFV2 needs the selected first p,q map
to be the carrier-consuming map. If p,q selection is a readout
operation, control exclusion is inherited from the ambient object, not
proved at the PFV2 first map.

Under A142.5, the p,q field has not been shown to remain load-bearing
downstream. Doc 111 would reject a strict prefix whose consumed field
is forgotten before M_C/F_C/Tr_L.

Thus bare adelic bookkeeping does not pass PFV2-GLOBAL. QED.

## 4. What Adelic Structure Can Still Supply

Allowed:

```text
structural product formula over all places;
source-level exclusion of non-adic controls;
conservative home for B0 p^Z combs and log addresses;
candidate source for a future structural complement object.
```

Not allowed:

```text
calling p,q coordinate selection a first carrier-consuming map;
freezing the other places as external constants;
using the global product formula as a post hoc relation on two labels;
running a two-place witness before S_{p,q} is object-defined.
```

## 5. Surviving Target

PFV2-GLOBAL is sharpened to:

```text
PFV2-ADELIC-LOCAL.
There exists an adelic/product-formula carrier source with a structural
two-place localization S_{p,q} such that:

1. p and q valuation towers are object data;
2. the complement of all other places is structural, not a frozen
   external constant;
3. the product-formula relation is part of S_{p,q};
4. kappa_PF consumes the p,q+complement field before trace;
5. Epstein/DH controls cannot form S_{p,q} or kappa_PF;
6. B0_p and B0_q embed conservatively;
7. the consumed field remains load-bearing downstream.
```

This is now the active A2 target.

## 6. Updated Q134.1 Landing

Current Q134.1 status:

```text
PFV2-GLOBAL:
  SHARPEN to PFV2-ADELIC-LOCAL.
```

Answer landing:

```text
PASS:
  Name the structural two-place adelic/local product-formula source
  S_{p,q}, its complement object, and kappa_PF.

KILL:
  Prove every such localization is either coordinate projection,
  external complement freezing, control-formable, bank-replacing, or
  downstream-forgetful.

SHARPEN:
  Name the exact adelic localization, Arakelov divisor, or
  product-formula source theorem that decides whether S_{p,q} exists.
```

## 7. Witness Rule

No witness is licensed.

The current question is categorical/source-theoretic: does S_{p,q}
exist as object data? A witness could only test a named S_{p,q} and
kappa_PF for control formability or downstream dependence.

## 8. Board Update

```text
PFV2:
  bare UFD pair demoted;
  bare all-places adelic bookkeeping demoted;
  active target sharpened to PFV2-ADELIC-LOCAL;
  no witness licensed.
```

## 9. Relation To Existing Docs

```text
doc 135
  Rejects coordinate-pair relations.

doc 140
  Identifies adelic/product-formula carriers as the main semantic home.

doc 141
  Demotes bare UFD pairs.

doc 111
  Governs downstream forgetting after any future p,q first map.
```
