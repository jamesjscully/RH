# 107 - Carrier-overreach meta-lemma

Status: theorem statement / proof-polish target, 2026-06-11. This
extracts the common theorem behind docs 97, 100, and 105. It is an
internal program lemma, not a claim about all trace theories.

## 1. Purpose

Several recent gates use the same mechanism:

```text
If the proposed trace/codomain/mixed object is functorial on a shadow
category before primitive Euler-carrier fields are consumed, then
Epstein/DH controls can be substituted and carrier selectivity fails.
```

This document records that mechanism as one reusable lemma, so future
work can cite the lemma rather than re-running Epstein or rewriting the
same argument.

## 2. Setup

Let `C` be a prime-power carrier with intended primitive fields:

```text
alpha;
v;
depth;
ell;
mu_C;
Euler-product factorization or graph-depth object.
```

Let a proposed construction assign one of the following packages:

```text
S3 package:
  b1(comb_C) -> M_C <- R_L/T_C
  M_C -> F_C -> Tr_L(F_C)

LT76 package:
  T_C, b1(comb_C), M_C, Tr_L
```

Let `Sh` be a shadow category containing at least one control input type:

```text
represented-norm monoids;
commutative monoids with length/count data;
positive multisets;
positive discrete measures;
Dirichlet coefficient or DH-type measure shadows;
theta/count data;
determinant/coker shadows built from the above.
```

## 3. Hypotheses

The construction is shadow-functorial if:

```text
H107.1 shadow functor
  There is a forgetful/detection functor U from the proposed carrier or
  trace domain to Sh, or the construction is directly defined on Sh.
  The first load-bearing construction factors through this shadow data;
  no hidden carrier-side predicate is checked before the shadow
  operation.

H107.2 pre-carrier construction
  The first construction of M_C, F_C, Tr_L, or the traceable object uses
  only operations available in Sh: tensor, sum, completion, pushforward,
  coend, kernel, correspondence, determinant, cokernel, trace-class
  closure, localizing invariant, or functorial module/sheaf operation.

H107.3 no earlier primitive carrier map
  Before that construction, no object or map requires alpha, v, depth,
  ell, mu_C, or Euler factorization as primitive object data.

H107.4 control closure
  The same input type admits the Epstein represented-norm shadow for
  Q=x^2+5y^2 or a DH coefficient/measure shadow.

H107.5 theorem follows the shadow
  Any traceability, codomain, determinant, index, Gram, count, or
  properness theorem used by the construction still applies to the same
  typed operation after the control substitution. The control object is
  not merely analogous; it enters the same construction.
```

## 4. Lemma

### Lemma 107.1

Under H107.1-H107.5, the construction fails carrier selectivity. It
routes to:

```text
S3:
  REJECT_CARRIER_OVERREACH / REJECT_CARRIER_BLIND.

LT76:
  NO76.4 carrier overreach / LT76.6 reject.
```

### Proof

By H107.1-H107.3, the load-bearing mixed object, codomain, traceable
object, or trace factors through shadow data before any primitive
Euler-carrier field is required. By H107.4, the same input type admits
an Epstein or DH control shadow. For Epstein, doc 64 supplies the
needed control fact: theta/count data survive while free valuation,
distinguished atom, and tower address fail. DH controls require the
same branch-specific input-type check. By H107.5, substituting the
valid control still leaves the same typed construction and theorem
legal.

Therefore the control also produces the proposed object:

```text
control shadow -> M_control -> F_control -> Tr_L(F_control)
```

or, in the LT76 form:

```text
control shadow -> M_control -> Tr_L(M_control).
```

The first trace/codomain/coupling operation is formable for the control.
Thus the required carrier/effectivity death does not occur before
signs, positivity, zeros, or comparison. This violates the carrier
selectivity required by docs 87, 94, 98, and 76/LT76.6. QED.

## 5. Covered Classes

The lemma covers:

```text
generic theta/count/Poisson kernels;
positive-measure or coefficient trace packages;
represented-norm monoid constructions;
determinant/coker packages built on shadow operators;
trace-class operator packages whose traceability is tested before
primitive carrier checking;
trace-derived codomains that remain functorial after shadow
substitution.
```

## 6. Escape Condition

The only escape from this lemma's rejection is to name an earlier
primitive carrier-consuming object or map:

```text
S_C -> Y_C
```

such that:

```text
1. S_C requires primitive alpha/v/depth/ell/mu_C/Euler-factorization
   data before M_C, F_C, or Tr_L exists;
2. Epstein/DH controls cannot form S_C or the map S_C -> Y_C;
3. the B0 bank embeds conservatively enough to test the map;
4. the later trace and same-form codomain are legal only after this map;
5. zero-free freeze is recorded before first zero contact.
```

For S3, this is exactly the doc-103 first-map record. For LT76, the same
escape must be scored through docs 92, 105, and 106 before any B1
promotion.

## 7. Relation To Existing Docs

```text
doc 64
  Supplies the concrete Epstein represented-norm obstruction.

doc 87
  Supplies the carrier-selectivity ledger.

doc 97
  Proves the monoid-functorial S3 overreach case.

doc 100
  Proves the mixed-object shadow-enlargement S3 case.

doc 101 and doc 102
  Turn doc 100 into an operation audit and apply it to S3 ansatz
  classes.

doc 103 and doc 104
  State and fill the S3 first-map escape record.

doc 105 and doc 106
  State and apply the LT76 trace-operation overreach audit.

doc 108
  Turns this meta-lemma into a theorem-polish proof skeleton with
  explicit dependencies, branch verdicts, and escape clauses.
```

## 8. Use Rule

When a future proposal uses a standard operation before primitive
carrier checking, cite this lemma and then route to the specific local
ledger:

```text
S3 ansatz:
  docs 100-104.

LT76/A6 trace answer:
  docs 92, 105, and 106.
```

Do not rerun Epstein as a new example unless the proposal claims a new
primitive carrier-consuming map outside this lemma's hypotheses.

For theorem-polish citations, use doc 108. This file is the compact
lemma statement; doc 108 is the expanded proof skeleton and
instantiation checklist.
