# 161 - PFV2 linear product-formula operation collapse

Status: bounded no-go from the PFV2-EULER-OP target / Q134.1
internal result, 2026-06-12. This is not a B1 construction, not an
external answer, and not a witness license. It kills only proposed
Euler operations that use the product-formula valuation vector as a
linear balance, affine constraint, or torsor of scalar normalizations.

## 1. Purpose

Doc 160 tests whether the product-formula valuation vector

```text
V_PF = (v_p, v_q; ell_p, ell_q; PF)
```

can define the Euler band/groupoid required by:

```text
PFV2-EULER-OP.
```

The first false positive is the obvious one: make `Op_E` the kernel,
fiber, affine solution space, or torsor of choices for the scalar
product-formula relation. This document rejects that broad class.

## 2. Covered Class

Call a proposal `PFV2_EULER_OP_linear` if it satisfies all of:

```text
D161.1 scalar product-formula operation
  Op_E is the kernel, cokernel, fiber, affine hyperplane, solution
  torsor, normalization torsor, or compatibility groupoid of a scalar
  product-formula relation.

D161.2 linear data only
  Op_E uses only v_p, v_q, ell_p, ell_q, signs, scalar weights, or the
  equation saying the weighted valuation sum is zero.

D161.3 no tower effectivity
  Op_E does not use the prime-power combs, effective valuation towers,
  alpha_p/alpha_q as atoms, or the source-level operation that makes
  p^Z and q^Z Euler carrier data.

D161.4 broad replacement
  The same operation can be written for arbitrary positive lengths,
  p,q-marked local diagrams, assembled D plus labels, represented-norm
  shadows, or DH coefficient/measure shadows.

D161.5 inherited first map
  kappa_E factors through the scalar relation, its solution torsor, or
  a representative of the normalization torsor.
```

This class includes:

```text
the kernel of a length-weighted valuation sum;
the affine hyperplane of product-formula balances;
torsors of rescaling choices making a scalar product formula hold;
groupoids of compatible scalar normalizations;
fiber products over a one-dimensional length/degree object;
cohomology classes recording the scalar balance relation.
```

## 3. Lemma

### Lemma 161.1

`PFV2_EULER_OP_linear` does not satisfy PFV2-EULER-OP.

Verdict:

```text
REJECT_LINEAR_PF_OP
  if Op_E is only the scalar product-formula balance operation.

REJECT_SCALAR_NORMALIZATION_TORSOR
  if tau_E is only a torsor of choices making the scalar balance hold.

REJECT_CONTROL_LENGTH_OP
  if the same operation can be formed for arbitrary length-marked
  shadows while preserving theta/count shadows.

HOLD_EULER_TOWER_OP
  if a later proposal defines Op_E using the actual Euler valuation
  towers, prime-power combs, and atom/effectivity data.
```

### Proof

PFV2-EULER-OP requires an operation that takes the primitive
product-formula valuation vector as object data and creates an
Euler-specific band/groupoid before assembly.

Under D161.1-D161.2, `Op_E` is only a linear balance operation. Such an
operation can be mathematically precise, but it uses `V_PF` as scalar
degree data rather than as a source-level Euler carrier. It does not
see why `ell_p=log p` and `ell_q=log q` come from prime-power combs
rather than from arbitrary positive lengths.

Under D161.3, no effective tower or atom data is consumed. Therefore
the operation does not distinguish the PFV2 source from a length-marked
shadow carrying the same scalar equation.

Under D161.4, controls can instantiate the same operation. Epstein
represented-norm data and DH coefficient/measure shadows may retain
their theta/count shadows while carrying scalar length labels and a
linear balance relation. That violates the control non-formability
gate.

Under D161.5, `kappa_E` is inherited from the scalar relation or its
normalization torsor. It is not a first carrier-consuming map for the
Euler tower source.

Thus linear product-formula operations do not satisfy PFV2-EULER-OP.
QED.

## 4. What The Linear Class Still Supplies

Allowed:

```text
a notation for the scalar product-formula constraint;
a diagnostic for whether a proposed operation uses more than lengths;
a calibration object for external questions;
a downstream invariant after a stricter Euler tower operation passes.
```

Not allowed:

```text
claiming PFV2-EULER-OP;
claiming FIRST_MAP_PASS;
claiming control exclusion;
using scalar product-formula balance as carrier nativity;
promoting normalization torsors to source evidence.
```

## 5. Surviving Escape

The remaining PFV2 Euler-operation route is:

```text
PFV2-EULER-TOWER-OP.
```

The target:

```text
There is a named operation Op_T on the full Euler valuation-tower
source, not merely on the scalar valuation vector, such that:

1. Op_T consumes alpha_p, alpha_q, v_p, v_q, ell_p, ell_q, PF, and
   the p^Z/q^Z comb or tower effectivity before all-places assembly;
2. Op_T constructs G_T and tau_T before kappa_T;
3. Op_T is not functorial for arbitrary length-marked local diagrams
   or D plus scalar labels;
4. Epstein/DH controls cannot instantiate Op_T while preserving their
   theta/count shadows;
5. kappa_T changes when tau_T changes while D, p,q marking, and scalar
   product-formula balance are held fixed;
6. B0_p and B0_q embed conservatively before tau_T is consumed;
7. tau_T remains load-bearing downstream in M_C/F_C/Tr_L.
```

This is narrower than PFV2-EULER-OP. It demands tower/comb/effectivity
consumption, not only scalar product-formula compatibility.

## 6. Kill Conditions Licensed By This Shot

A future no-go is licensed only for a named `Op_T` proposal if one
proves:

```text
KILL-TOWER-OP.1 scalar collapse
  Op_T factors through the scalar product-formula relation or its
  normalization torsor.

KILL-TOWER-OP.2 no atom consumption
  Op_T does not consume alpha_p/alpha_q or the p^Z/q^Z comb/tower
  effectivity before assembly.

KILL-TOWER-OP.3 broad length transport
  Op_T transports to arbitrary length-marked local-shadow objects.

KILL-TOWER-OP.4 control formability
  Epstein/DH controls can instantiate Op_T while retaining theta/count
  shadows.

KILL-TOWER-OP.5 downstream erasure
  every legal M_C/F_C/Tr_L forgets tau_T or sees only D and scalar PF.
```

Do not apply these to all Euler-operation attempts without a theorem
covering their proposed tower/comb operation.

## 7. Board Update

```text
PFV2_EULER_OP_linear:
  REJECT_LINEAR_PF_OP;
  REJECT_CONTROL_LENGTH_OP.

PFV2-ADELIC-LOCAL:
  still live only through PFV2-EULER-TOWER-OP or another source whose
  operation consumes actual Euler tower/comb/effectivity data before
  assembly.

A2 witness:
  still not licensed.
```

## 8. Relation To Existing Docs

```text
doc 160
  Supplies PFV2-EULER-BAND(p,q) and the PFV2-EULER-OP target.

doc 159
  Rejects broad functorial carrier-torsor packages.

doc 130
  Names V_PF and records FIRST_MAP_HOLD.

doc 103
  Requires primitive fields to be consumed before M_C/F_C/Tr_L.

doc 111
  Still blocks downstream forgetfulness.
```
