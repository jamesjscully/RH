# 165 - PFV2 global PF all-places collapse

Status: bounded no-go from the PFV2-GLOBAL-PF-AXIOM target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only global
product-formula tower axioms whose source is an all-places object first
and whose p,q tower data are selected or projected afterward.

## 1. Purpose

Doc 164 names the missing object-level axiom:

```text
PFV2-GLOBAL-PF-AXIOM.
```

The first false positive is the classical one already isolated by docs
142 and 150: take an all-places adelic/divisor/idele/product-formula
object, then read off p and q. This document rejects that class in the
new global-tower language.

## 2. Covered Class

Call a proposal `PFV2_GPF_allplaces` if it satisfies all of:

```text
D165.1 all-places source
  ECar_L1^{GPF} is an all-places adelic, divisor, idele, Arakelov, or
  product-formula source category.

D165.2 p,q selected after source
  alpha_p, alpha_q, Comb_p, Comb_q, v_p, v_q, ell_p, ell_q, and
  C_{not p,q} are obtained by selecting, projecting, localizing, or
  marking p and q after an all-places object D already exists.

D165.3 global PF before p,q source
  GPF is the classical all-places product-formula structure of D, not
  an axiom whose object definition first forms the p,q+complement
  source.

D165.4 effectivity inherited from D
  Eff_G is all-places effectivity, divisor effectivity, or tower
  admissibility inherited from D and then read at p,q.

D165.5 inherited first map
  Op_G, G_G, tau_G, or kappa_G factors through D, D plus p,q marking,
  or a post-global relative reflector.
```

This class includes:

```text
all-places adelic product-formula objects with p,q coordinates;
global divisor/idele categories localized at p,q after construction;
Arakelov product-formula sources with two selected places;
post-global relative envelopes whose input is already D;
global tower objects whose p,q data are only a readout.
```

## 3. Lemma

### Lemma 165.1

`PFV2_GPF_allplaces` does not satisfy PFV2-GLOBAL-PF-AXIOM.

Verdict:

```text
REJECT_ALLPLACES_GPF
  if S_T is an all-places object first and p,q are selected afterward.

REJECT_POSTGLOBAL_TOWER_READOUT
  if Op_G, G_G, tau_G, or kappa_G factors through D plus p,q marking.

REJECT_INHERITED_EFFECTIVITY
  if Eff_G is only all-places effectivity inherited from D.

HOLD_PQ_COMPLEMENT_GPF
  if a later proposal names a p,q+complement global PF tower source
  formed before any all-places object exists.
```

### Proof

PFV2-GLOBAL-PF-AXIOM requires one source object whose definition
simultaneously contains the p and q effective towers, structural
lengths, complement, product-formula relation, and effectivity before
assembly.

Under D165.1-D165.3, the object is all-places first. The p,q fields
are selected from an already accepted global source. Doc 142 rejects
bare all-places adelic/product-formula bookkeeping as PFV2: the global
product formula may be genuine structure, but the selected p,q map is
only a coordinate projection or readout.

Under D165.4, effectivity is inherited from the global object. It is
not the p,q+complement source-defining effectivity demanded by doc 164.

Under D165.5, the first map factors through D or a post-global
relative construction. Doc 150 rejects that order: the all-places
object is accepted before the relative p,q object exists.

Thus all-places global PF tower readouts do not satisfy
PFV2-GLOBAL-PF-AXIOM. QED.

## 4. What All-Places Global PF Still Supplies

Allowed:

```text
ordinary product-formula notation;
tests for whether a proposed source is only D plus p,q marking;
post-pass comparison data after a stricter source passes;
external examples of what does not count.
```

Not allowed:

```text
claiming PFV2-GLOBAL-PF-AXIOM;
claiming FIRST_MAP_PASS;
claiming p,q source priority;
claiming inherited all-places control exclusion as PFV2 selectivity;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 global-PF route is:

```text
PFV2-GPF-LOCAL.
```

The target:

```text
There is a p,q+complement global product-formula tower source S_{p,q}^G
formed before any all-places object D, such that:

1. S_{p,q}^G simultaneously contains p and q effective towers,
   structural lengths, a structural complement, product-formula
   relation, and effectivity data;
2. D, if it exists, is assembled from S_{p,q}^G rather than selected
   first;
3. Op_G constructs G_G and tau_G before kappa_G and before assembly;
4. Epstein/DH controls cannot instantiate S_{p,q}^G, Op_G, or kappa_G
   while retaining theta/count shadows;
5. B0_p and B0_q embed conservatively into S_{p,q}^G;
6. tau_G or GPF remains load-bearing downstream in M_C/F_C/Tr_L.
```

This is narrower than PFV2-GLOBAL-PF-AXIOM because it forbids
all-places-first formation and requires the global PF axiom to be local
in the p,q+complement source.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `S_{p,q}^G` proposal if
one proves:

```text
KILL-GPF-LOCAL.1 all-places unfolding
  S_{p,q}^G is equivalent to an all-places object D plus p,q marking.

KILL-GPF-LOCAL.2 post-global construction
  Op_G, G_G, tau_G, or kappa_G factors through D or a post-global
  reflector.

KILL-GPF-LOCAL.3 marked tower collapse
  S_{p,q}^G unfolds into marked monoids, independent UFD towers, or a
  later PF relation.

KILL-GPF-LOCAL.4 control formability
  Epstein/DH controls can instantiate S_{p,q}^G, Op_G, and kappa_G
  while retaining theta/count shadows.

KILL-GPF-LOCAL.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_G or sees only D and scalar PF.
```

Do not apply these beyond a named p,q+complement global PF tower
source.

## 7. Board Update

```text
PFV2_GPF_allplaces:
  REJECT_ALLPLACES_GPF;
  REJECT_POSTGLOBAL_TOWER_READOUT.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-LOCAL or another source whose global
  PF axiom is p,q+complement-local before all-places assembly.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 164
  Supplies PFV2-GLOBAL-TOWER(p,q) and the PFV2-GLOBAL-PF-AXIOM target.

doc 142
  Rejects bare all-places adelic/product-formula bookkeeping.

doc 150
  Rejects post-global relative reflection.

doc 151
  Requires p,q+complement descent/gluing source before all-places
  assembly.

doc 103
  Still requires a first carrier-consuming map.
```
