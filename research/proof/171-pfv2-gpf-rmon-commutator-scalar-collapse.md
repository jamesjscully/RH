# 171 - PFV2 GPF residual monodromy commutator scalar collapse

Status: bounded no-go from the PFV2-GPF-RMON-COMM-SELECT target /
Q134.1 internal result, 2026-06-12. This is not a B1 construction, not
an external answer, and not a witness license. It kills only
commutator/holonomy proposals whose content is scalar product-formula
balance, p,q marking, complement bookkeeping, or an abelian
compatibility label.

## 1. Purpose

Doc 170 writes the commutator shot:

```text
PFV2-GPF-RMON-COMM(p,q).
```

The first false positive is a scalar commutator: `rho_G^{comm}` is
named as a p/q action defect, but after inspection it is only the
scalar product-formula balance, the marked p and q valuation lengths,
the complement bookkeeping term, or the assertion that two bookkeeping
operations commute. This document rejects that class.

## 2. Covered Class

Call a proposal `PFV2_GPF_COMM_scalar` if it satisfies all of:

```text
D171.1 commutator syntax
  The proposal names Act_p, Act_q, rho_G^{comm}, and kappa_G^{comm}
  before an assembly functor.

D171.2 scalar source
  rho_G^{comm} is fully determined by one of:
    the scalar product-formula equation;
    the p,q valuation labels or lengths;
    the complement balancing term;
    an abelian compatibility equation saying Act_p Act_q = Act_q Act_p;
    a zero commutator imposed as part of bookkeeping.

D171.3 no object-level action residue
  No theorem shows that changing the action of p or q on the structural
  complement while fixing scalar PF data changes rho_G^{comm}.

D171.4 inherited first map
  kappa_G^{comm} factors through scalar PF, p,q marking, complement
  readout, or the assembled object after forgetting any object-level
  commutator data.

D171.5 downstream scalarity
  M_C/F_C/Tr_L sees only D, scalar PF, p,q marking, or a zero/abelian
  compatibility label.
```

This class includes:

```text
commutators equal to the scalar PF defect;
commutators determined by ell_p, ell_q and complement degree;
zero commutators imposed because the selected operations commute;
abelian action labels with no non-scalar residue;
holonomy names that reduce to product-formula normalization.
```

## 3. Lemma

### Lemma 171.1

`PFV2_GPF_COMM_scalar` does not satisfy PFV2-GPF-RMON-COMM-SELECT.

Verdict:

```text
REJECT_COMM_SCALAR
  if rho_G^{comm} is only scalar PF balance, p,q marking, complement
  bookkeeping, or an imposed zero/abelian compatibility condition.

REJECT_COMM_INHERITED_MAP
  if kappa_G^{comm} factors through scalar PF, marking, complement
  readout, or D after forgetting object-level action residue.

REJECT_COMM_DOWNSTREAM_SCALAR
  if downstream sees only scalar PF, marking, D, or zero/abelian
  compatibility data.

HOLD_COMM_NONSCALAR
  if a later proposal supplies a non-scalar action residue on the
  structural complement that is not determined by scalar PF data.
```

### Proof

PFV2-GPF-RMON-COMM-SELECT requires `rho_G^{comm}` to be an object-level
commutator or holonomy class of p and q tower actions on the structural
complement. It is not enough to rename scalar product-formula balance
as a commutator.

Under D171.1-D171.2, the proposal has commutator syntax but no
non-scalar residue. The data are recovered from scalar PF balance,
p,q labels, complement bookkeeping, or an imposed abelian
compatibility equation. This is the scalar collapse already excluded
by docs 154, 160, and 161 in earlier language.

Under D171.3, there is no theorem that the structural complement
carries action-sensitive object data beyond the scalar relation. Thus
the commutator does not distinguish source objects with the same
scalar PF and marking data.

Under D171.4, the first map is inherited from scalar/readout data.
Forgetting the supposed commutator leaves `kappa_G^{comm}` unchanged
or equivalent, so the first map does not consume a residual primitive.

Under D171.5, downstream dependence fails. If M_C/F_C/Tr_L sees only
scalar PF, p,q marking, D, or an abelian compatibility label, doc 111
rejects the route.

Therefore scalar or abelian bookkeeping commutators do not satisfy
PFV2-GPF-RMON-COMM-SELECT. QED.

## 4. What Scalar Commutators Still Supply

Allowed:

```text
normalization checks for a later non-scalar action class;
diagnostics for whether Act_p and Act_q are actually object actions;
compatibility conditions after a stricter commutator passes;
examples for external questions about what does not count.
```

Not allowed:

```text
claiming PFV2-GPF-RMON-COMM-SELECT;
claiming FIRST_MAP_PASS;
claiming control non-formability;
running an A2 witness;
promoting scalar PF balance to residual monodromy;
updating doc 103 or doc 113 as passed.
```

## 5. Surviving Escape

The remaining PFV2 commutator route is:

```text
PFV2-GPF-RMON-COMM-NONSCALAR.
```

The target:

```text
There is a non-scalar commutator or holonomy class rho_G^{comm}
defined by p and q tower actions on the structural complement such
that rho_G^{comm} is not determined by scalar PF balance, p,q marking,
complement bookkeeping, or an imposed zero/abelian compatibility
condition.

Changing the object-level action residue while holding D, p,q marking,
scalar PF, and presentation data fixed changes kappa_G^{comm} or its
target; Epstein/DH controls cannot form the same action residue; B0_p
and B0_q embed conservatively; and rho_G^{comm} remains load-bearing
in M_C/F_C/Tr_L.
```

This is narrower than PFV2-GPF-RMON-COMM-SELECT because it removes
scalar, marked, and abelian bookkeeping commutators.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named non-scalar commutator
proposal:

```text
KILL-COMM-NONSCALAR.1 no object residue
  The proposed rho_G^{comm} is determined by scalar PF, marking, or
  complement bookkeeping after all.

KILL-COMM-NONSCALAR.2 control formability
  Epstein/DH controls can instantiate the same non-scalar action
  residue and first map while retaining theta/count shadows.

KILL-COMM-NONSCALAR.3 inherited first map
  kappa_G^{comm} is unchanged when the non-scalar action residue is
  changed while D, marking, scalar PF, and presentation data are fixed.

KILL-COMM-NONSCALAR.4 bank replacement
  the non-scalar commutator requires replacing B0_p/B0_q by a full
  global source.

KILL-COMM-NONSCALAR.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets the non-scalar action residue.
```

Do not apply these beyond the named non-scalar commutator proposal.

## 7. Board Update

```text
PFV2_GPF_COMM_scalar:
  REJECT_COMM_SCALAR.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-GPF-RMON-COMM-NONSCALAR or another
  non-scalar native p,q+complement GPF action class.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 170
  Supplies PFV2-GPF-RMON-COMM(p,q) and the
  PFV2-GPF-RMON-COMM-SELECT target.

doc 161
  Rejects scalar product-formula balance and linear normalization
  operations in the Euler-operation language.

doc 160
  Requires product-formula fields to define operations, not only scalar
  balance.

doc 154
  Rejects residual fields that are only marking or bookkeeping.

doc 111
  Still blocks downstream forgetfulness.
```
