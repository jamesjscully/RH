# 155 - PFV2 rho obstruction-defect collapse

Status: bounded no-go from the PFV2-RHO-NONTRIVIAL target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only residual
obstruction/defect data that either vanish on successful assembly or
reduce to a scalar/product-formula failure term.

## 1. Purpose

Doc 154 leaves nontrivial residual classes:

```text
obstruction;
torsor;
extension;
automorphism;
cocycle;
coherence.
```

The cheapest one to test is obstruction/defect data. This document
asks whether an obstruction or defect residual can be the source datum
when the PFV2 route needs successful assembly downstream.

Answer:

```text
Only if the obstruction/defect survives successful assembly as
non-scalar object data. A residual that merely measures failure to
assemble, or becomes zero/scalar after assembly, does not pass
PFV2-RHO-NONTRIVIAL.
```

## 2. Covered Class

Call a proposal `PFV2_RHO_obdef_collapse` if it satisfies all of:

```text
O155.1 obstruction or defect rho
  rho is presented as an obstruction class, defect class, or
  product-formula/gluing error attached to Desc_{p,q}^{rho}.

O155.2 success requires vanishing
  Legal assembly into an all-places object D, or legal downstream
  M_C/F_C/Tr_L, requires rho=0 or requires rho to be killed by a
  quotient/equivalence.

O155.3 scalar defect alternative
  If rho does not vanish, it is only a scalar error term, degree
  mismatch, product-formula defect, or complement-balance value.

O155.4 no residual successful object
  No theorem supplies a successful assembled object that still carries
  rho as non-scalar object data.

O155.5 inherited or failed kappa
  kappa_rho either cannot be formed when rho obstructs assembly, or
  factors through the rho=0 assembled object when assembly succeeds.

O155.6 downstream absent or erased
  M_C/F_C/Tr_L is unavailable for nonzero obstruction rho, or it sees
  only the rho=0 assembled object/scalar defect.
```

This class includes:

```text
rho = obstruction to gluing;
rho = failure of product-formula compatibility;
rho = scalar gluing defect;
rho = class killed by imposing the descent condition;
rho = error term that must vanish before the object exists.
```

## 3. Lemma

### Lemma 155.1

`PFV2_RHO_obdef_collapse` does not satisfy PFV2-RHO-NONTRIVIAL.

Verdict:

```text
REJECT_OBSTRUCTION_VANISHES
  if successful assembly requires rho=0.

REJECT_SCALAR_DEFECT
  if rho is only a scalar/product-formula/gluing error.

REJECT_NO_DOWNSTREAM_OBJECT
  if nonzero rho prevents forming M_C/F_C/Tr_L.

HOLD_SURVIVING_OBSTRUCTION
  if a later proposal supplies obstruction/defect data that survives
  successful assembly as non-scalar object data.
```

### Proof

PFV2-RHO-NONTRIVIAL requires rho to be consumed before assembly and to
remain load-bearing downstream. It cannot be only a failed attempt to
assemble the object.

Under O155.1-O155.2, rho is an obstruction that must vanish, or be
killed, for the source to assemble legally. Then rho cannot be the
load-bearing downstream carrier field in the successful route. The
route either has rho and no object, or has an object after rho is
removed.

Under O155.3, rho is only a scalar defect. Doc 154 already rejects
scalar product-formula defects as residual source data.

Under O155.4, there is no successful object retaining rho. The residual
does not survive the step PFV2 needs to continue.

Under O155.5, kappa_rho is either unavailable or inherited from the
rho=0 assembled object. Neither gives a first carrier-consuming map
using nontrivial rho.

Under O155.6, downstream dependence fails. Doc 111 rejects a strict
prefix whose consumed field is absent from M_C/F_C/Tr_L.

Thus vanishing obstruction/scalar defect residuals do not pass
PFV2-RHO-NONTRIVIAL. QED.

## 4. What Obstruction/Defect Data Can Still Supply

Allowed:

```text
failure diagnostics for candidate descent systems;
boundary data identifying why assembly is impossible;
external questions about whether a non-scalar obstruction can survive;
calibration for the residual-class taxonomy.
```

Not allowed:

```text
claiming FIRST_MAP_PASS;
claiming source selectivity from a failed assembly;
running a witness on nonzero obstruction data;
promoting a scalar defect to rho;
using rho=0 after quotient as a nontrivial residual.
```

## 5. Surviving Escape

The remaining PFV2 residual route is:

```text
PFV2-RHO-SURVIVES.
```

The target:

```text
There is a nontrivial residual datum rho, such as torsor, extension,
automorphism, cocycle, coherence, or a surviving non-scalar obstruction
class, that remains object data after successful assembly.

kappa_rho consumes rho before assembly; Epstein/DH controls cannot form
rho or kappa_rho; B0_p and B0_q embed conservatively; and rho remains
load-bearing in M_C/F_C/Tr_L.
```

This is narrower than PFV2-RHO-NONTRIVIAL. It removes obstruction data
that merely block assembly and asks for residual data that survive
successful assembly.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named surviving-rho class:

```text
KILL-SURVIVE.1 control formability
  Epstein/DH shadows can form the same surviving rho and kappa_rho.

KILL-SURVIVE.2 post-assembly origin
  rho is created only after all-places assembly.

KILL-SURVIVE.3 bank replacement
  rho requires replacing B0_p/B0_q by the full global source.

KILL-SURVIVE.4 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho.
```

Do not apply these beyond the named surviving-rho class.

## 7. Board Update

```text
PFV2_RHO_obdef_collapse:
  REJECT_OBSTRUCTION_VANISHES or REJECT_SCALAR_DEFECT.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-RHO-SURVIVES or another nontrivial
  residual source whose rho remains object data after successful
  assembly.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 154
  Rejects scalar defects and marking/bookkeeping rho.

doc 153
  Supplies the residual source record.

doc 111
  Still blocks downstream forgetfulness.

doc 103
  Still HOLD: no FIRST_MAP_PASS.
```

## 9. Post-doc-156 Update

Doc 156 tests the torsor/extension/cocycle residual shot:

```text
PFV2-RHO-TOR(p,q):
  LOCAL_RHO_CLASS_PASS;
  HOLD_SURVIVAL;
  HOLD_CONTROL_TORSOR;
  HOLD_BANK_PRESERVATION;
  HOLD_DOWNSTREAM.
```

The surviving target is:

```text
PFV2-TOR-SELECT.
```

Thus PFV2-RHO-SURVIVES remains the enclosing target, but future work
should decide the torsor/extension/cocycle survival and selectivity
theorem before moving to a different residual family.
