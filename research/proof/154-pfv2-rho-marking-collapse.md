# 154 - PFV2 rho marking collapse

Status: bounded no-go from the PFV2-RHO-SELECT target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only residual
descent data that reduce to p,q marking, complement bookkeeping, or a
scalar defect.

## 1. Purpose

Doc 153 makes the residual descent datum explicit:

```text
rho
```

The first licensed kill condition is:

```text
KILL-RHO.1 marking collapse.
```

This document applies that kill condition to the weakest residual
classes. It does not kill residual obstruction, torsor, extension,
automorphism, cocycle, or coherence data with additional structure.

## 2. Covered Class

Call a proposal `PFV2_RHO_marking` if it satisfies all of:

```text
M154.1 residual field
  The source includes a residual field rho in Desc_{p,q}^{rho}.

M154.2 marking or bookkeeping content
  rho is equivalent to one of:

    the choice of p and q;
    the list of p,q valuation coordinates;
    the complement object C_{not p,q};
    the degree or scalar value of the complement;
    the product-formula scalar defect;
    a label recording which cover or decomposition was used.

M154.3 no independent residual invariant
  rho has no invariant, obstruction, torsor, extension, automorphism,
  cocycle, or coherence content beyond M154.2.

M154.4 no selective formation theorem
  No theorem says rho is meaningful only for the carrier source and not
  for Epstein/DH theta/count shadows.

M154.5 downstream sees only bookkeeping
  M_C, F_C, or Tr_L sees only p,q labels, complement degree, scalar
  defect, or assembled all-places data.
```

This class includes:

```text
rho = (p,q);
rho = (v_p,v_q);
rho = deg(C_{not p,q});
rho = ell_p v_p + ell_q v_q + c(C_{not p,q});
rho = "the chosen p,q,complement cover";
rho = a scalar product-formula error term.
```

## 3. Lemma

### Lemma 154.1

`PFV2_RHO_marking` does not satisfy PFV2-RHO-SELECT.

Verdict:

```text
REJECT_RHO_MARKING
  if rho is only p,q marking or coordinate labeling.

REJECT_RHO_COMPLEMENT_BOOKKEEPING
  if rho is only C_{not p,q} or its degree/scalar value.

REJECT_RHO_SCALAR_DEFECT
  if rho is only a scalar product-formula defect.

HOLD_NONTRIVIAL_RHO
  if a later proposal supplies nontrivial residual obstruction, torsor,
  extension, automorphism, cocycle, or coherence data not covered by
  M154.1-M154.5.
```

### Proof

PFV2-RHO-SELECT requires rho to do work not already done by the p,q
marking, complement field, or product-formula equation.

Under M154.1-M154.2, rho is only a repackaging of data already present
in PFV2_local_record(p,q) or PFV2-DESC(p,q). Docs 135, 142, 148, and
152 already reject using labels, coordinate readouts, or assembled
bookkeeping as first carrier-consuming structure.

Under M154.3, there is no independent residual invariant. Therefore
kappa_rho cannot consume rho as a new source-selective field; it only
consumes the same marking/complement information under another name.

Under M154.4, control selectivity is unproved. Marking p,q, appending a
scalar defect, or recording a complement degree can be done for
Epstein/DH shadows as bookkeeping while their theta/count data remain
meaningful.

Under M154.5, downstream dependence is not residual dependence. Doc 111
rejects any route where M_C/F_C/Tr_L sees only the marking,
complement degree, scalar defect, or assembled all-places object.

Thus marking/bookkeeping/scalar residuals do not pass
PFV2-RHO-SELECT. QED.

## 4. What Marking Rho Still Supplies

Allowed:

```text
calibration for notation;
external-question examples of what not to count as residual data;
tests for whether a proposed rho has independent invariant content;
bookkeeping for future nontrivial residual classes.
```

Not allowed:

```text
claiming FIRST_MAP_PASS;
claiming control non-formability;
running an A2 witness;
updating doc 103 or doc 113 as passed;
promoting scalar product-formula defect to source-selective structure.
```

## 5. Surviving Escape

The remaining PFV2 residual route is:

```text
PFV2-RHO-NONTRIVIAL.
```

The target:

```text
There is a residual descent datum rho with nontrivial obstruction,
torsor, extension, automorphism, cocycle, or coherence content.

rho is not equivalent to p,q marking, complement bookkeeping, or a
scalar defect; kappa_rho consumes rho before all-places assembly;
Epstein/DH controls cannot form rho or kappa_rho; B0_p and B0_q embed
conservatively; and rho remains load-bearing downstream.
```

This is narrower than PFV2-RHO-SELECT. It removes the bookkeeping
residuals and demands a genuinely nontrivial residual class.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named nontrivial residual class:

```text
KILL-RHO-NONTRIVIAL.1 control formability
  Epstein/DH shadows can form the same nontrivial rho and kappa_rho.

KILL-RHO-NONTRIVIAL.2 post-assembly origin
  rho exists only after all-places assembly or post-global reflection.

KILL-RHO-NONTRIVIAL.3 bank replacement
  rho requires replacing B0_p/B0_q by the full global source.

KILL-RHO-NONTRIVIAL.4 downstream erasure
  every legal M_C/F_C/Tr_L forgets rho.
```

Do not apply these beyond the named nontrivial residual class.

## 7. Board Update

```text
PFV2_RHO_marking:
  REJECT_RHO_MARKING.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-RHO-NONTRIVIAL or another residual
  source whose rho has independent invariant content.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 153
  Supplies PFV2-RES(p,q) and licenses KILL-RHO.1.

doc 152
  Rejects residual data erased by ordinary effective descent.

doc 111
  Still blocks downstream forgetfulness.

doc 103
  Still HOLD: no FIRST_MAP_PASS.
```

## 9. Post-doc-155 Update

Doc 155 rejects vanishing obstruction/scalar defect residuals:

```text
PFV2_RHO_obdef_collapse:
  REJECT_OBSTRUCTION_VANISHES or REJECT_SCALAR_DEFECT.
```

The surviving target is:

```text
PFV2-RHO-SURVIVES.
```

Thus PFV2-RHO-NONTRIVIAL remains the enclosing target, but future work
should ask for nontrivial residual data that survive successful
assembly as object data.
