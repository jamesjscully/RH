# 164 - PFV2 global tower source shot

Status: concrete PFV2-TOWER-GLOBAL candidate shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, not a witness license, and not a no-go. It writes the smallest
honest global product-formula tower object left by doc 163.

## 1. Purpose

Doc 163 rejects independent tower records with later product-formula
relations or effectivity labels. The remaining target is:

```text
PFV2-TOWER-GLOBAL.
```

The target must supply one source object whose definition
simultaneously contains:

```text
towers;
structural log lengths;
product-formula relation;
effectivity;
control exclusion;
bank embedding;
downstream visibility.
```

This document records the smallest candidate source.

## 2. Candidate Record

Name:

```text
PFV2-GLOBAL-TOWER(p,q).
```

Proposed source object:

```text
S_T in ECar_L1^{GPF}
```

where `ECar_L1^{GPF}` is a still-unnamed global product-formula tower
subcategory.

Fields of `S_T`:

```text
A_p, A_q
  B0_p and B0_q one-place carrier records.

alpha_p, alpha_q
  distinguished prime-power atoms.

Comb_p, Comb_q
  effective prime-power combs.

v_p, v_q
  valuation/tower maps.

ell_p, ell_q
  structural lengths ell_p=log p and ell_q=log q.

C_{not p,q}
  structural complement source.

GPF
  a global product-formula tower axiom: the towers, structural lengths,
  complement, and product-formula relation are part of one object
  definition, not an equation imposed after two towers exist.

Eff_G
  global effectivity data built into GPF, not a predicate on already
  formed coordinates.

bank_iota
  conservative embeddings of B0_p and B0_q into S_T.

surv_T
  survival/visibility data for the future tower torsor in M_C/F_C/Tr_L.
```

The proposed operation is:

```text
Op_G(S_T) = (G_G, tau_G)
```

where `G_G` is the global PF tower groupoid and `tau_G` is its
effective tower torsor.

The intended first map is:

```text
kappa_G : S_T -> Y_G
```

and it must consume:

```text
(GPF, Eff_G, G_G, tau_G)
```

before all-places assembly, kernel, determinant, mixed object, trace,
regularization, positivity, or zero comparison.

## 3. Why This Is Not The Marked Tower Class

This shot requires simultaneous formation:

```text
not independent towers:
  Comb_p and Comb_q are not objects first with PF added later.

not marked monoid:
  GPF is an object axiom of ECar_L1^{GPF}, not a label on arbitrary
  monoids.

not bare UFD pair:
  free/effective tower data are a component of S_T, but do not by
  themselves define the source.

not effectivity label:
  Eff_G is part of the global product-formula tower axiom, not a
  predicate applied afterward.
```

Thus the shot reaches the side of doc 163 that remained open.

## 4. Gate Run

### Gate 164.1 - Simultaneous source shape

Verdict:

```text
LOCAL_SIMULTANEOUS_SCHEMA_PASS
```

Reason: the record defines one object `S_T` with towers, PF, and
effectivity in the same source definition. This is a schema pass only.

### Gate 164.2 - Global PF axiom existence

Verdict:

```text
HOLD_GLOBAL_PF_AXIOM
```

Reason: `ECar_L1^{GPF}` and `GPF` are named as required slots, but no
mathematical axiom or category has been constructed.

### Gate 164.3 - Non-markedness

Verdict:

```text
HOLD_NOT_MARKED_TOWER
```

Reason: no theorem has shown that `S_T` cannot be unfolded into
marked monoids, independent UFD towers, or a later scalar PF relation.
Doc 163 applies if such an unfolding exists.

### Gate 164.4 - Control exclusion

Verdict:

```text
HOLD_CONTROL_GLOBAL_TOWER
```

Reason: no theorem has shown that Epstein/DH controls cannot
instantiate `ECar_L1^{GPF}`, `S_T`, `Op_G`, or `kappa_G` while
retaining theta/count shadows.

### Gate 164.5 - First-map dependence

Verdict:

```text
HOLD_KAPPA_G_DEPENDENCE
```

Reason: no theorem has shown that changing `tau_G` while holding D,
p,q marking, scalar PF, and complement bookkeeping fixed changes
`kappa_G` or its target.

### Gate 164.6 - Bank preservation

Verdict:

```text
HOLD_BANK_PRESERVATION
```

Reason: the global object must embed B0_p and B0_q conservatively. If
`S_T` replaces their comb/address/count/guard data, doc 130's
KILL-A2.5 applies.

### Gate 164.7 - Downstream dependence

Verdict:

```text
HOLD_DOWNSTREAM
```

Reason: no theorem has shown that M_C, F_C, or Tr_L consumes `tau_G`
or `GPF` as load-bearing source data. If downstream only sees scalar
PF or D, doc 111 rejects the route.

## 5. Current Verdict

```text
PFV2-GLOBAL-TOWER(p,q):
  LOCAL_SIMULTANEOUS_SCHEMA_PASS;
  HOLD_GLOBAL_PF_AXIOM;
  HOLD_NOT_MARKED_TOWER;
  HOLD_CONTROL_GLOBAL_TOWER;
  HOLD_KAPPA_G_DEPENDENCE;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.

PFV2-TOWER-GLOBAL:
  SHARPEN to PFV2-GLOBAL-PF-AXIOM.

A2 witness:
  still not licensed.
```

This is construction progress only as a sharper source record. It
identifies the missing object-level axiom.

## 6. Sharpened Theorem Target

The next deciding theorem is:

```text
PFV2-GLOBAL-PF-AXIOM.
```

The theorem:

```text
There is a category or subcategory ECar_L1^{GPF} with objects S_T such
that:

1. S_T simultaneously contains p and q effective valuation towers,
   structural log lengths, a structural complement, product-formula
   relation, and effectivity data;
2. PF and effectivity are object axioms, not later equations or
   predicates on independent towers;
3. Op_G constructs G_G and tau_G before kappa_G;
4. Epstein/DH controls cannot instantiate S_T, Op_G, or kappa_G while
   retaining theta/count shadows;
5. B0_p and B0_q embed conservatively into S_T;
6. tau_G or GPF remains load-bearing downstream in M_C/F_C/Tr_L.
```

This theorem is narrower than PFV2-TOWER-GLOBAL because it asks for the
exact object-level global PF axiom.

## 7. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `ECar_L1^{GPF}` proposal if
one proves:

```text
KILL-GPF-AXIOM.1 marked unfolding
  S_T unfolds into marked monoids, independent UFD towers, or two
  towers plus a later PF relation.

KILL-GPF-AXIOM.2 effectivity predicate
  Eff_G is only a predicate on already formed tower coordinates.

KILL-GPF-AXIOM.3 control formability
  Epstein/DH controls can instantiate S_T, Op_G, and kappa_G while
  retaining theta/count shadows.

KILL-GPF-AXIOM.4 bank replacement
  S_T replaces B0_p/B0_q instead of embedding them conservatively.

KILL-GPF-AXIOM.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_G or sees only D and scalar PF.
```

Do not apply these beyond a named global PF tower source.

## 8. Board Update

```text
PFV2-ADELIC-LOCAL:
  the active construction-facing shot is now a global product-formula
  tower source object;
  simultaneous source shape locally passes;
  global PF axiom existence, non-markedness, control exclusion,
  first-map dependence, bank preservation, and downstream dependence
  remain HOLD.

Immediate theorem target:
  PFV2-GLOBAL-PF-AXIOM.
```

## 9. Relation To Existing Docs

```text
doc 163
  Rejects marked tower/effectivity-label proposals and leaves
  PFV2-TOWER-GLOBAL.

doc 162
  Supplies the effective tower operation shot.

doc 141
  Demotes bare UFD/free-tower data to source-control partial.

doc 140
  Rejects marked product and marked monoid versions.

doc 130
  Names the primitive A2 fields and records FIRST_MAP_HOLD.

doc 103
  Supplies the strict first-map record template.
```
