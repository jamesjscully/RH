# 140 - PFV2 structural source axiom audit

Status: candidate-source audit / Q134.1 internal sharpening,
2026-06-11. This follows docs 135 and 139. It is not a construction,
not a PASS for PFV2-STRUCTURAL, and not a witness license.

## 1. Purpose

Doc 135 rejects the coordinate-pair version of PFV2. The live target is
now:

```text
PFV2-STRUCTURAL.
```

This document asks what source axioms would be strong enough to make
the product-formula valuation pair structural rather than decorative.

The point is to prevent the next attempt from merely renaming
coordinate labels as axioms.

## 2. Required Source-Axiom Package

A PFV2-STRUCTURAL proposal must supply a category or subcategory:

```text
ECar_L1^PFV2
```

and an object:

```text
S_C in ECar_L1^PFV2
```

with all of:

```text
SA140.1 rank-one valuation towers
  S_C has two rank-one Euler valuation towers V_p and V_q with
  distinguished atoms alpha_p and alpha_q.

SA140.2 free tower coordinates
  Each tower has a free nonnegative coordinate k before quotienting,
  trace, determinant, or kernel formation.

SA140.3 structural log lengths
  ell_p and ell_q are lengths/norms attached to the towers as object
  data, not later parameters.

SA140.4 product-formula constraint
  PF is a source-category condition relating the two towers, not an
  equation imposed on already formed coordinate labels.

SA140.5 first map
  kappa_PF exists because SA140.1-SA140.4 hold and consumes the PF
  valuation field before M_C, F_C, Tr_L, kernels, determinants, or
  trace-class closure.

SA140.6 control non-formability
  Epstein represented-norm and DH coefficient/measure controls cannot
  form S_C or kappa_PF because at least one of SA140.1-SA140.5 is not
  meaningful for them.

SA140.7 bank embedding
  B0_p and B0_q embed without replacing comb/address/count/guard data.

SA140.8 downstream dependence
  The PF valuation field consumed by kappa_PF remains load-bearing in
  M_C, F_C, or Tr_L.

SA140.9 zero-free freeze
  S_C, kappa_PF, control exclusions, and first zero contact are frozen
  before any zero-side comparison.
```

If any of SA140.1-SA140.6 is missing, the proposal is not
PFV2-STRUCTURAL.

## 3. Axiom Families

### Family A - Marked Product Of One-Place Records

Shape:

```text
S_C = B0_p x B0_q plus marked towers and PF relation.
```

Verdict:

```text
REJECT_COORDINATE_PAIR by doc 135.
```

Reason:

```text
The source is formed before the structural PF condition. The towers and
PF relation are labels/relations on a product of shadows.
```

Escape:

```text
Only if the product itself is not the source; instead, it is the image
of a prior ECar_L1^PFV2 object under a conservative embedding.
```

### Family B - Category Of Marked Commutative Monoids

Shape:

```text
objects are commutative monoids with two distinguished atoms, lengths,
and a relation PF.
```

Verdict:

```text
REJECT_CONTROL_FORMABLE unless the object axioms force free Euler
valuation towers and exclude represented-norm monoids before maps.
```

Reason:

```text
If arbitrary monoids may be marked with atoms/lengths/PF, Epstein or DH
shadows can carry the same decorations. Doc 109 and doc 108 apply.
```

Escape:

```text
State an axiom that represented-norm monoids cannot satisfy before any
trace or sign test. A mere choice of marked irreducibles is not enough.
```

### Family C - UFD/Factorization Domain Objects

Shape:

```text
objects carry unique factorization, rank-one valuations, and lengths.
```

Verdict:

```text
HOLD_SOURCE_AXIOM.
```

Reason:

```text
This can exclude the Epstein represented-norm control by doc 64's
36=4*9=6*6 obstruction if UFD/free tower structure is genuinely
object-defining. It still must prove conservative B0 embedding,
product-formula coupling, and downstream dependence.
```

Risk:

```text
It may be too algebraic or too discrete to carry internal R_L/T_C and
same-form LS4 later.
```

### Family D - Adelic/Product-Formula Carrier Objects

Shape:

```text
objects are adelic or Arakelov-style carriers whose source axiom is a
product formula over valuations with structural length data.
```

Verdict:

```text
HOLD_SOURCE_AXIOM.
```

Reason:

```text
This is the most plausible semantic home for PFV2-STRUCTURAL: PF is
not imposed after coordinates, but is part of the object definition.
```

Risk:

```text
The construction may immediately become broad enough to accept
represented-norm or coefficient shadows unless the Euler-product tower
axiom is primitive. It may also produce only classical adelic
bookkeeping rather than a liquid trace domain.
```

### Family E - Trace-Domain-First Objects

Shape:

```text
objects are chosen because they are traceable, then decorated with
valuation/PF data.
```

Verdict:

```text
REJECT_SHADOW_PACKAGE_FIRST by docs 112 and 136.
```

Reason:

```text
Traceability is obtained before carrier fields are primitive. This is
late carrier reintroduction, not PFV2-STRUCTURAL.
```

## 4. Current Positive Residue

After the audit, only two axiom families remain worth pursuing:

```text
C. UFD/factorization-domain source objects;
D. adelic/product-formula carrier objects.
```

Both remain HOLD, not PASS.

They must next answer:

```text
R140.1
  Can the object axiom make represented-norm controls non-objects
  without relying on selected labels?

R140.2
  Can B0_p and B0_q embed conservatively into the source?

R140.3
  Does kappa_PF consume PF valuation data before every trace,
  determinant, kernel, or mixed-object operation?

R140.4
  Does the consumed PF field remain load-bearing downstream?

R140.5
  Can the source later interact with LCT-STRICT or another legal trace
  route without a carrier-forgetting envelope?
```

## 5. Updated Q134.1 Dispatch

When using doc 139's PFV2 packet, add this sharpened fork:

```text
The coordinate-pair and marked-monoid versions are rejected. The live
question is whether a UFD/factorization-domain source or an
adelic/product-formula carrier source can make the valuation pair
object-defining before trace.
```

Ask the recipient to classify their answer as:

```text
UFD_SOURCE_PASS | UFD_SOURCE_KILL | UFD_SOURCE_SHARPEN |
ADELIC_SOURCE_PASS | ADELIC_SOURCE_KILL | ADELIC_SOURCE_SHARPEN |
OUT_OF_SCOPE
```

## 6. Witness Rule

No PFV2 witness is licensed.

The current state is source-axiom HOLD. A witness would only be
meaningful after a concrete UFD/factorization or adelic/product-formula
source object is named and the question becomes deterministic
formability for Epstein/DH controls.

## 7. Board Update

```text
PFV2-STRUCTURAL:
  marked product and marked monoid versions rejected;
  UFD/factorization source HOLD;
  adelic/product-formula source HOLD;
  no witness licensed.
```

## 8. Relation To Existing Docs

```text
doc 64
  Supplies the Epstein non-UFD/free-tower obstruction used for the UFD
  source test.

doc 135
  Rejects coordinate-pair PFV2.

doc 136
  Rejects trace-domain-first broad packages.

doc 139
  Supplies the current sendable packet; doc 140 adds the source-axiom
  fork to Q134.1.
```
