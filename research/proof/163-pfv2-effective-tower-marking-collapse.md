# 163 - PFV2 effective tower marking collapse

Status: bounded no-go from the PFV2-TOWER-EFFECTIVE target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only effective
tower-operation proposals whose effectivity is marked monoid data,
bare UFD/factorization data, or two independent towers plus a later
product-formula relation.

## 1. Purpose

Doc 162 names the tower-operation target:

```text
PFV2-TOWER-EFFECTIVE.
```

The first false positive is inherited from docs 140-141:

```text
marked product;
marked monoid;
bare UFD/factorization pair;
two independent towers plus external PF relation.
```

This document applies that boundary to the new effective-tower
operation language.

## 2. Covered Class

Call a proposal `PFV2_TOWER_marked` if it satisfies all of:

```text
D163.1 tower fields
  The proposal names alpha_p, alpha_q, Comb_p, Comb_q, v_p, v_q,
  ell_p, ell_q, PF, and an effectivity predicate Eff.

D163.2 marked monoid or UFD source
  Comb_p and Comb_q are independent marked commutative monoids,
  UFD/free-tower records, or factorization-domain records.

D163.3 external PF
  PF is imposed after the two towers exist, or is read as an equation
  on their valuation coordinates.

D163.4 effectivity as label
  Eff records positivity, order, atom preservation, or tower
  admissibility as a predicate on the already formed towers, not as a
  source-defining operation.

D163.5 no global product-formula tower object
  No object is named whose existence simultaneously requires the
  towers, structural lengths, product-formula relation, and effectivity
  before the towers are independently available.
```

This class includes:

```text
products B0_p x B0_q with tower labels;
commutative monoids with distinguished atoms, lengths, and PF;
p^Z/q^Z UFD towers plus a later balance relation;
free-factorization domains used only to make controls fail;
effectivity predicates imposed after the tower coordinates exist.
```

## 3. Lemma

### Lemma 163.1

`PFV2_TOWER_marked` does not satisfy PFV2-TOWER-EFFECTIVE.

Verdict:

```text
REJECT_TOWER_MARKED_MONOID
  if the tower operation is marked product/monoid data.

REJECT_TOWER_UFD_PAIR
  if the tower operation is two independent UFD/free towers plus an
  external product-formula relation.

REJECT_EFFECTIVITY_LABEL
  if Eff is only a predicate on already formed tower coordinates.

HOLD_GLOBAL_TOWER_PF
  if a later proposal names a global product-formula tower object whose
  definition simultaneously contains towers, PF, and effectivity.
```

### Proof

PFV2-TOWER-EFFECTIVE requires effectivity as primitive Euler carrier
data and an operation `Op_T` defined before assembly. It is not enough
to label already available towers.

Under D163.1-D163.2, the tower data are marked product, marked monoid,
or bare UFD/factorization data. Doc 140 rejects marked products and
marked monoids unless the product is the image of a prior
`ECar_L1^PFV2` object. Doc 141 demotes bare UFD/free-tower data to
source-control partial: it may exclude Epstein represented-norm
controls, but it does not by itself produce PFV2.

Under D163.3, PF is external to the source. It is a later relation on
two independent towers, not a source-defining product-formula carrier.
This is the doc-141 obstruction.

Under D163.4, effectivity is only a predicate on already formed tower
coordinates. Such a predicate may be useful, but it is not the missing
operation `Op_T`. It does not create `G_T` or `tau_T` as prior object
data.

Under D163.5, no global product-formula tower object has been named.
Thus the proposal cannot establish first-map dependence, bank-safe
source formation, or downstream load-bearing. The route remains
blocked by docs 103, 111, and 162.

Therefore marked effective tower proposals do not satisfy
PFV2-TOWER-EFFECTIVE. QED.

## 4. What Marked Tower Data Still Supplies

Allowed:

```text
source-control subtests against Epstein/DH;
notation for atoms, valuation towers, lengths, and PF;
local calibration of what the global object must contain;
negative examples for external experts.
```

Not allowed:

```text
claiming PFV2-TOWER-EFFECTIVE;
claiming FIRST_MAP_PASS;
claiming the PF relation is object data;
claiming effectivity is a carrier operation;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 tower route is:

```text
PFV2-TOWER-GLOBAL.
```

The target:

```text
There is a global product-formula tower source object S_T whose object
definition simultaneously contains:

1. alpha_p, alpha_q, Comb_p, Comb_q, v_p, v_q;
2. structural lengths ell_p=log p and ell_q=log q;
3. the product-formula relation PF as source data, not a later
   equation;
4. effectivity Eff as a primitive source operation or axiom;
5. a tower operation Op_T producing G_T and tau_T before kappa_T;
6. control non-formability for Epstein/DH before trace, sign,
   regularization, positivity, or zero comparison;
7. conservative B0 bank embedding and downstream load-bearing.
```

This is narrower than PFV2-TOWER-EFFECTIVE because it demands a global
product-formula tower object rather than independent towers plus
labels.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named global tower object if one
proves:

```text
KILL-TOWER-GLOBAL.1 independent towers
  S_T reduces to two independently formed towers plus a later PF
  relation.

KILL-TOWER-GLOBAL.2 marked monoid
  S_T is only a product or category of marked monoids/factorization
  domains.

KILL-TOWER-GLOBAL.3 effectivity predicate
  Eff is only a predicate on already formed coordinates, not a
  primitive source operation or axiom.

KILL-TOWER-GLOBAL.4 control formability
  Epstein/DH controls can instantiate S_T and Op_T while retaining
  theta/count shadows.

KILL-TOWER-GLOBAL.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_T or sees only scalar PF.
```

Do not apply these beyond a named global product-formula tower source.

## 7. Board Update

```text
PFV2_TOWER_marked:
  REJECT_TOWER_MARKED_MONOID;
  REJECT_TOWER_UFD_PAIR;
  REJECT_EFFECTIVITY_LABEL.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-TOWER-GLOBAL or another source whose
  object definition simultaneously contains tower, PF, and effectivity
  data before assembly.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 162
  Supplies PFV2-TOWER-OP(p,q) and the PFV2-TOWER-EFFECTIVE target.

doc 141
  Demotes bare UFD/free-tower data to source-control partial.

doc 140
  Rejects marked product and marked monoid versions.

doc 130
  Names the primitive A2 fields and records FIRST_MAP_HOLD.

doc 103
  Still requires a first carrier-consuming map.

doc 111
  Still blocks downstream forgetfulness.
```
