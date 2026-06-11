# 108 - Carrier-overreach proof skeleton

Status: theorem-polish skeleton / reusable no-go package,
2026-06-11. This turns doc 107 into a proof object with explicit
dependencies, failure modes, and escape clauses. It is a broad
shadow-functorial carrier-overreach no-go, not a global no-go: it does
not kill strict Euler-carrier-first constructions.

## 1. Purpose

Docs 97, 100, and 105 all prove the same bounded theorem:

```text
If the first load-bearing trace, mixed object, codomain, or traceable
object is constructed in a shadow-stable category before primitive
Euler-carrier fields are consumed, then Epstein/DH controls can enter
the same construction and carrier selectivity fails.
```

Doc 107 records the meta-lemma. This document is the theorem-ready
skeleton for citing it without rerunning examples.

## 2. Program Axiom Used

The proof uses the carrier-selectivity requirement from doc 87:

```text
theta/count shadows may survive;
Epstein/DH controls must fail at the first carrier/effectivity map;
the failure must occur before signs, positivity, zeros, comparison, or
post-selection.
```

Therefore the proof does not need to show that the control produces a
bad zero estimate. It is enough to show that the proposed first
load-bearing construction is still formable for the control.

## 3. Abstract Setup

Let `C` be the intended Euler carrier. Let `P(C)` be the first
load-bearing package used by the proposal. Depending on the branch,
`P(C)` is one of:

```text
S3:
  M_C;
  F_C;
  Tr_L(F_C);
  b1(comb_C) -> M_C <- R_L/T_C.

LT76:
  T_C;
  M_C;
  Tr_L(M_C);
  the trace input coupling b1(comb_C) to R_L/T_C.
```

Let `Prim(C)` denote the primitive Euler-carrier fields:

```text
alpha;
v;
depth;
ell;
mu_C;
Euler-product factorization;
prime-power graph-depth data.
```

Let `Sh` be a shadow category containing at least one of:

```text
represented-norm monoids;
commutative monoids with length/count data;
positive multisets or positive discrete measures;
Dirichlet coefficient or DH-type measure shadows;
theta/count data;
determinant, cokernel, kernel, or trace-class shadows built from
those data.
```

## 4. Hypotheses

The carrier-overreach theorem applies when the following are all true.

```text
H108.1 shadow detection
  The proposal either is defined directly on Sh or admits a
  forgetful/detection functor U to Sh through which the first
  load-bearing construction is formed or certified. The first
  construction factors through this shadow data; no hidden carrier-side
  predicate is checked before the shadow operation.

H108.2 pre-carrier formation
  P(C), or the map that first creates P(C), is formed before any map
  requires Prim(C) as primitive object data.

H108.3 shadow-stable operations
  That formation uses operations available in Sh: tensor, sum,
  completion, pushforward, coend, kernel, correspondence, determinant,
  cokernel, trace-class closure, localizing invariant, or a functorial
  module/sheaf/measure construction.

H108.4 control object closure
  The same input type contains either the Epstein represented-norm
  shadow for Q=x^2+5y^2 or a DH coefficient/measure shadow. One valid
  control substitution is enough for rejection, but the branch must
  state which control is being used.

H108.5 theorem follows the construction
  The traceability, properness, determinant, index, Gram, codomain,
  count, or comparison theorem invoked for P(C) remains applicable to
  the same typed operation P(control) after the shadow substitution.
  The control object is not merely analogous; it enters the same
  construction, coupling, trace, or codomain.

H108.6 no earlier structural exclusion
  Before P(C) is formed, the proposal has not named an object or map
  whose definition fails for the Epstein/DH control because alpha, v,
  depth, ell, mu_C, Euler factorization, or graph-depth data are
  primitive in the source.

H108.7 timed failure test
  The control remains formable through P(control) before signs,
  positivity, zeros, comparison, regularization, or post-selection are
  invoked.
```

Hypothesis H108.6 is the main anti-overclaim clause. If a proposal can
name such an earlier map, it must be routed to doc 103 or the LT76
strict-carrier ledger instead of being killed here.

## 5. Theorem Skeleton

### Theorem 108.1

Under H108.1-H108.7, the proposal fails carrier selectivity.

Branch verdicts:

```text
S3:
  REJECT_CARRIER_OVERREACH;
  REJECT_CARRIER_BLIND.

LT76:
  doc 76 NO76.4 carrier overreach;
  doc 92 LT76.6 reject;
  doc 87 REJECT_CARRIER_BLIND.
```

### Proof

By H108.1-H108.3, the first load-bearing package `P(C)` is constructed
inside, or detected through, a shadow category before primitive
Euler-carrier fields are consumed.

By H108.4, the same input type contains an Epstein represented-norm
control or a DH coefficient/measure control. For Epstein, doc 64
supplies the control obstruction: theta/count data survive, but free
valuation, distinguished atom, and tower address fail. For DH, the
candidate must state the analogous coefficient/measure control branch.
By H108.5, the theorem that licenses the proposed package also licenses
the same typed substituted package:

```text
control -> P(control).
```

In S3 notation, this means the control can still form one of:

```text
M_control;
F_control;
Tr_L(F_control);
b1(control) -> M_control <- R_L/T_C.
```

In LT76 notation, this means the control can still form:

```text
T_control;
M_control;
Tr_L(M_control);
```

By H108.6, there is no earlier structural exclusion map that failed for
the control before `P(C)` was formed. Thus the first load-bearing
construction is formable for the control. By H108.7, this happens
before signs, positivity, zeros, comparison, regularization, or
post-selection.

Doc 87 requires the selected Epstein or DH control to fail at the first
carrier/effectivity map before signs, positivity, zeros, comparison, or
post-selection. The control has not failed at that stage. Therefore the
proposal fails carrier selectivity.

The S3 verdict routes through docs 97, 100, 101, 102, 103, and 104
according to the local operation record. The LT76 verdict routes through
docs 92, 105, and 106. QED.

## 6. Dependency Table

```text
doc 64
  Supplies the concrete Epstein represented-norm control and records
  the missing primitive carrier fields.

doc 87
  Supplies the carrier-selectivity criterion used as the program axiom.

doc 97
  Instantiates the skeleton for S3 monoid-functorial codomain/trace
  packages.

doc 100
  Instantiates the skeleton for S3 mixed-object shadow enlargement.

doc 101
  Turns the S3 shadow-enlargement hypothesis into an operation audit.

doc 102
  Applies that audit to the doc-75 S3 ansatz classes.

doc 103
  Records the only current positive-side escape for S3: a strict first
  primitive carrier-consuming map.

doc 109
  Rejects decorated-shadow first maps that only relabel shadow data.

doc 111
  Rejects strict first maps whose consumed primitive field is forgotten
  before the downstream trace package.

doc 112
  Rejects late carrier reintroduction after the shadow trace package is
  already formed.

doc 105
  Instantiates the skeleton for LT76 broad trace operations.

doc 106
  Records the current LT76 no-pass state after doc 105.

doc 107
  Gives the compact reusable lemma statement extracted here.
```

## 7. Instantiation Checklist

Before citing Theorem 108.1, fill the following minimal record:

```text
candidate:
branch: S3 | LT76 | other:

first load-bearing package P(C):
  object/map:
  formed before primitive carrier map? YES/NO:

shadow category Sh:
  input objects:
  operations used:
  represented-norm/Epstein accepted? YES/NO:
  DH coefficient/measure accepted? YES/NO:

theorem-following field:
  trace/properness/determinant/index theorem:
  still applies after control substitution? YES/NO:
  same typed operation after substitution? YES/NO:

earlier exclusion check:
  named earlier S_C or kappa_C:
  primitive field consumed:
  control fails before P(C)? YES/NO:

verdict:
  THEOREM_108_APPLIES | ROUTE_TO_STRICT_FIRST_MAP |
  TRACE_THEOREM_MISSING | OUT_OF_SCOPE:
```

## 8. Escape Clause

The theorem does not apply if the proposal supplies an earlier strict
carrier-consuming map:

```text
S_C -> Y_C
```

with all of:

```text
1. S_C has primitive alpha/v/depth/ell/mu_C/Euler-factorization data
   before M_C, F_C, or Tr_L exists;
2. the map consumes at least one primitive field before shadow-stable
   operations create the traceable package;
3. Epstein/DH controls cannot form S_C or the map for structural
   reasons;
4. the B0 bank embeds conservatively enough to test the map;
5. zero-free freeze is recorded before first zero contact.
```

For S3 this routes to doc 103, then docs 109/111/112, then doc 98. For
LT76 it routes to docs 92, 105, and 106 before any B1 promotion.

## 9. Non-Coverage

The theorem does not prove:

```text
strict ECar_L1 domains are impossible;
all liquid trace theories are carrier-blind;
all trace-derived codomains are fake;
all determinant, coker, or index packages are externally supplied;
B1 admission fails globally.
```

It proves only the broad no-go class in which the first load-bearing
package is shadow-stable before primitive carrier checking.

## 10. Use Rule

Use this file when a future proposal begins with a standard categorical,
measure-theoretic, trace-class, determinant/coker, kernel, or
localizing-invariant operation. Cite Theorem 108.1 after verifying
H108.1-H108.7.

Do not cite it against a proposal whose first nontrivial step is already
a named primitive carrier-consuming map. That proposal gets the stricter
and narrower doc-103/doc-98 or doc-92/doc-105/doc-106 routing instead.
