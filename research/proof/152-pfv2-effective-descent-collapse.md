# 152 - PFV2 effective descent collapse

Status: bounded no-go from the PFV2-DESC shot / Q134.1 internal
result, 2026-06-12. This is not a B1 construction, not an external
answer, and not a witness license. It kills only pre-global descent
packages whose descent theorem is effective in the ordinary sense:
descent data are equivalent to assembled all-places objects with p,q
marking.

## 1. Purpose

Doc 151 gives the first PFV2 candidate with the correct formation
order:

```text
Desc_{p,q} first;
Assemble(Desc_{p,q}) = D second.
```

The first remaining HOLD is:

```text
HOLD_EFFECTIVE_DESCENT.
```

This document asks whether ordinary effective descent is enough.

Answer:

```text
No. If the descent theorem identifies Desc_{p,q} with all-places
objects with p,q marking, then source priority is presentational rather
than load-bearing.
```

## 2. Covered Class

Call a proposal `PFV2_DESC_effective` if it satisfies all of:

```text
E152.1 pre-global notation
  The proposal writes a descent object Desc_{p,q} before the all-places
  object D.

E152.2 assembly functor
  There is an assembly functor

    Assemble : Desc_{p,q} -> G_{p,q-marked}

  into the all-places adelic/divisor/idele category with p,q marking.

E152.3 effective descent equivalence
  Assemble is an equivalence of categories, or fully faithful and
  essentially surjective on the source objects used by kappa_desc.

E152.4 no residual descent datum
  gamma and pf_desc have no invariant, obstruction, or source field
  left after passing across the equivalence. They are exactly the
  gluing presentation of D.

E152.5 inherited first map
  kappa_desc corresponds under Assemble to a map on the assembled
  all-places object or to p,q boundary readout.

E152.6 inherited control exclusion
  Epstein/DH controls fail, if at all, because they cannot form the
  assembled all-places object. They are not excluded by residual
  descent data.

E152.7 downstream assembled
  M_C, F_C, or Tr_L uses only the assembled all-places object, p,q
  marking, or boundary readout.
```

This class includes:

```text
standard sheaf/descent presentations where objects with gluing data are
equivalent to global objects;
adelic local-to-global descent where the only content is reconstruction
of D;
pre-global diagrams whose only theorem is effective assembly into G;
descent certificates that disappear under the equivalence.
```

## 3. Lemma

### Lemma 152.1

`PFV2_DESC_effective` does not satisfy PFV2-DESC-SELECT.

Verdict:

```text
REJECT_EFFECTIVE_DESCENT_COLLAPSE
  if Desc_{p,q} is equivalent to all-places objects with p,q marking.

REJECT_PRESENTATIONAL_PRIORITY
  if source priority is only the choice of presenting D by descent
  data.

REJECT_INHERITED_SELECTIVITY
  if controls fail only at assembled G-object formability.

REJECT_DOWNSTREAM_ASSEMBLED
  if downstream uses only the assembled object.

HOLD_RESIDUAL_DESCENT
  if a later proposal supplies residual descent data not erased by
  effective assembly.
```

### Proof

PFV2-DESC-SELECT requires `Desc_{p,q}` to be source-selective. The
descent data must do work not already done by the all-places source
with p,q marking.

Under E152.1-E152.3, the proposal may write the descent data first, but
the descent theorem identifies those data with assembled all-places
objects. Source priority is then a presentation choice. The category is
not carrying a stricter object than `G_{p,q-marked}`.

Under E152.4, `gamma` and `pf_desc` have no residual content across the
equivalence. They are not load-bearing carrier fields; they are the
ordinary gluing certificate for D.

Under E152.5, kappa_desc is inherited. A map corresponding under an
equivalence to a map on the assembled object is not a new first
carrier-consuming map.

Under E152.6, control exclusion is inherited from the assembled global
source. PFV2-DESC-SELECT needs controls to fail at the descent source
or kappa_desc.

Under E152.7, downstream dependence is assembled-object dependence.
Doc 111 rejects this if `gamma` and `pf_desc` are forgotten before
M_C/F_C/Tr_L.

Thus effective descent presentations do not pass PFV2-DESC-SELECT. QED.

## 4. What Effective Descent Still Supplies

Allowed:

```text
evidence that pre-global notation can be made rigorous;
calibration for descent/gluing external questions;
a clean test for whether a future descent theorem has residual data;
bookkeeping for structural complements.
```

Not allowed:

```text
claiming FIRST_MAP_PASS;
claiming source-selective PFV2;
declaring Epstein/DH dead at the descent source;
running an A2 witness;
promoting presentation order to carrier order.
```

## 5. Surviving Escape

The remaining PFV2 descent route is:

```text
PFV2-DESC-RESIDUAL.
```

The target:

```text
There is a pre-global descent source Desc_{p,q} with residual descent
data rho. The data rho are not erased by effective assembly and are not
equivalent to p,q marking of an all-places object.

kappa_desc consumes rho, Epstein/DH controls cannot form rho or
kappa_desc, B0_p and B0_q embed conservatively, and rho remains
load-bearing downstream in M_C/F_C/Tr_L.
```

This is narrower than PFV2-DESC-SELECT. It asks for residual descent
structure, not ordinary effective reconstruction.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named residual-descent class:

```text
KILL-RESIDUAL.1 residual is marking
  rho is equivalent to p,q marking or complement bookkeeping.

KILL-RESIDUAL.2 control residual
  Epstein/DH shadows can form rho while retaining theta/count shadows.

KILL-RESIDUAL.3 bank replacement
  rho can exist only after replacing B0_p/B0_q by the full global
  source.

KILL-RESIDUAL.4 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho.
```

Do not apply these beyond the named residual-descent class.

## 7. Board Update

```text
PFV2_DESC_effective:
  REJECT_EFFECTIVE_DESCENT_COLLAPSE.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-DESC-RESIDUAL or another pre-global
  descent source with residual, source-selective, downstream
  load-bearing data.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 151
  Supplies PFV2-DESC(p,q) and the HOLD_EFFECTIVE_DESCENT gap.

doc 148
  Rejects all-places assembly plus p,q marking.

doc 149
  Rejects formal relative universal-property packages.

doc 150
  Rejects post-global reflectors.

doc 111
  Still blocks downstream forgetfulness.
```

## 9. Post-doc-153 Update

Doc 153 makes the residual descent shot concrete:

```text
PFV2-RES(p,q):
  LOCAL_SCHEMA_PASS;
  HOLD_RESIDUAL_NONERASURE;
  HOLD_CONTROL_RESIDUAL;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.
```

The surviving target is:

```text
PFV2-RHO-SELECT.
```

Thus PFV2-DESC-RESIDUAL remains the enclosing target, but future work
should decide a named residual datum rho, not merely ask for residual
structure abstractly.
