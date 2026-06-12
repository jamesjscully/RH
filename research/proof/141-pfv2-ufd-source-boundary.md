# 141 - PFV2 UFD source boundary

Status: bounded source-family audit / Q134.1 internal result,
2026-06-11. This attacks the UFD/factorization-domain subfamily left
open by doc 140. It does not kill PFV2-STRUCTURAL. It demotes bare UFD
pair sources and leaves only product-formula-native global carriers
live.

## 1. Purpose

Doc 140 left two PFV2 source families at HOLD:

```text
C. UFD/factorization-domain source objects;
D. adelic/product-formula carrier objects.
```

This document tests family C. The question is whether unique
factorization and rank-one valuations alone make the two-place
product-formula field structural.

Answer:

```text
UFD/free-tower axioms can supply control exclusion, but not PFV2 by
themselves. A product formula relating two towers is still extra global
structure unless it is part of the source object.
```

## 2. Covered Class

Call a PFV2 proposal `PFV2_UFD_bare` if it satisfies all of:

```text
U141.1 UFD source
  The source objects are UFD/factorization-domain or free
  commutative-monoid-like carriers with distinguished atoms and
  rank-one valuation towers.

U141.2 two independent towers
  The p and q towers are specified independently before any global
  product-formula object is named.

U141.3 external PF relation
  The product-formula relation is imposed after the two towers exist,
  or is read as an equation on their valuation coordinates.

U141.4 no global source object
  There is no object whose existence requires the two towers and their
  product-formula relation simultaneously.

U141.5 downstream unknown
  No theorem shows that the PF field remains load-bearing in M_C,
  F_C, or Tr_L rather than disappearing after the first constraint.
```

This class includes:

```text
pairs of UFDs or free monoids with selected primes;
two rank-one valuation towers plus a later relation;
factorization-domain records used only to make Epstein non-objects;
UFD carrier tests with no same-form downstream trace package.
```

## 3. Lemma

### Lemma 141.1

`PFV2_UFD_bare` does not satisfy PFV2-STRUCTURAL.

Verdict:

```text
SOURCE_CONTROL_PARTIAL
  if UFD/free-tower axioms exclude Epstein/DH controls at the source.

REJECT_COORDINATE_PAIR
  if the PF relation is only an equation on already formed tower
  coordinates.

HOLD_GLOBAL_PF
  if a global product-formula source object is plausible but not
  named.
```

### Proof

UFD/free-tower structure can be real object data. In particular, it can
make the Epstein represented-norm control fail as a source object:
doc 64's obstruction

```text
36 = 4*9 = 6*6
```

shows that the represented-norm monoid lacks the free prime-power
valuation tower required by a UFD-style source. Thus U141.1 can help
with SA140.1, SA140.2, and SA140.6.

But PFV2-STRUCTURAL requires more. By SA140.4 and SA140.5, the product
formula must be a source-category condition and kappa_PF must exist
because that condition is part of the object. Under U141.2-U141.4, the
two towers exist first and the product-formula relation is added or
read afterward. That is not yet a source-defining product-formula
carrier. It is a relation on two independent UFD coordinates.

Therefore the proposal may pass a control-exclusion subtest but still
fails the PFV2 source test. If the relation is merely an equation on
the two towers, doc 135's coordinate-pair obstruction applies. If the
proposal claims a global source object but does not define it, the
honest verdict is HOLD_GLOBAL_PF.

Finally, under U141.5, even a first constraint has not been shown to
remain load-bearing downstream. Doc 111 would reject a strict prefix
that is forgotten before M_C/F_C/Tr_L.

Thus bare UFD source data are not PFV2-STRUCTURAL. QED.

## 4. What UFD Data Can Still Supply

UFD/factorization data remain useful as a subcomponent:

```text
allowed:
  source-level control exclusion against represented-norm shadows;
  verification that prime-power towers are real object data;
  conservative embedding of B0 p^Z combs, if the map is written;
  compatibility check for any future global PF source.
```

Not allowed:

```text
promoting source-level control exclusion to PFV2-FIRST;
calling an external relation on two towers a product-formula source;
running a two-place kernel witness before downstream dependence is
proved.
```

## 5. Surviving Target

PFV2-STRUCTURAL is sharpened again:

```text
PFV2-GLOBAL.
There exists a global product-formula carrier source S_C whose object
definition simultaneously contains:

1. rank-one Euler valuation towers;
2. structural log lengths;
3. a product-formula relation as source data, not later equation;
4. control non-formability for Epstein/DH;
5. conservative B0 bank embedding;
6. downstream dependence through M_C/F_C/Tr_L.
```

The adelic/product-formula family from doc 140 is now the primary live
semantic home for PFV2-GLOBAL.

## 6. Updated Q134.1 Landing

Current Q134.1 status:

```text
PFV2-STRUCTURAL:
  SHARPEN to PFV2-GLOBAL.
```

Answer landing:

```text
PASS:
  Name a global product-formula source object, not just two UFD towers.

KILL:
  Prove every PFV2-GLOBAL attempt either reduces to independent UFD
  towers plus an external relation, accepts controls, forgets PF
  downstream, or cannot embed B0 conservatively.

SHARPEN:
  Name the exact global product-formula source axiom that decides
  whether PF is object data.
```

## 7. Witness Rule

No witness is licensed.

UFD source checks are formal at this stage. A witness could only become
useful after PFV2-GLOBAL names a concrete source and the question is
deterministic formability or downstream dependence.

## 8. Board Update

```text
PFV2:
  marked product rejected;
  marked monoid rejected;
  bare UFD/factorization pair demoted to source-control partial;
  live target sharpened to PFV2-GLOBAL;
  no witness licensed.
```

## 9. Relation To Existing Docs

```text
doc 64
  Supplies the represented-norm non-UFD obstruction.

doc 135
  Rejects coordinate-pair relations.

doc 140
  Left UFD/factorization objects at HOLD. Doc 141 demotes the bare UFD
  version and points to global product-formula carriers.

doc 111
  Will reject any strict UFD/PF prefix whose consumed field is
  forgotten downstream.
```
