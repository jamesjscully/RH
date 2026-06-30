# 215 - Integral q-similitude graph data does not construct positive Rosati

Status: no-go + integral graph boundary, 2026-06-20. Seventy-eighth cycle
of the doc-137 construction arc. Doc 214 killed full spectrum/conjugacy data
as a square carrier. This document tests the stronger repair: insist that the
graph is integral and satisfies the exact `q`-similitude relation.

```text
integral graph lattice + graph law + F^T E F = q E
  -> positive Rosati / Hodge sign
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_integral_qsim_graph_no_go` (IQG1-IQG6 ALL PASS) -- the
genuine finite-field block has integrality, exact `q`-similitude, graph law,
radius, and Hodge sign; an integral determinant-`q` companion can satisfy the
same Stage-A graph/similitude relations while sitting off circle with the
wrong primitive Hodge sign; this happens in a small family, not by accident;
the Rosati relation `F^dag = q F^{-1}` is only the similitude relation; the
same package is formable on controls; and no square package over `Z` is
built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_isospectral_graph_carrier_no_go` (ISG1-ISG6 ALL PASS) and
`theorem_B_similitude_signature` (exit 0).

## 1. Purpose

Doc 214 says spectrum plus graph law is still only conjugacy data. The next
natural repair is to demand the pieces that conjugacy lost:

```text
an integral graph lattice,
an alternating cup form E,
and the exact relation F^T E F = q E.
```

This is still not the finite-field square package. In dimension two, every
integral matrix of determinant `q` satisfies the standard alternating
`q`-similitude relation. Such matrices can be hyperbolic/off circle, and the
primitive Hodge index has the wrong sign. The relation

```text
F^dag = q F^{-1}
```

is therefore Stage A: duality/similitude. The missing object needs Stage B:
the positive Rosati/Hodge-index sign on the constructed square
correspondence carrier.

This document rejects only the shortcut:

```text
integral q-similitude graph data constructs the positive Rosati square
carrier required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 215.1 (Integral q-similitude is not positive Rosati).

Let E = [[0,1],[-1,0]]. For every 2 x 2 matrix A,

    A^T E A = det(A) E.

Thus an integral matrix with det(A)=q is already an integral q-similitude of
the standard alternating form and its powers obey the graph law
A^m A^n = A^(m+n).

Take

    A = [[0,-2],[1,3]].

Then det(A)=2, A is integral, and A^T E A = 2E. Its eigenvalues are 1 and 2,
so the graph is off the radius sqrt(2). Its primitive Hodge index is
positive rather than negative.

Equivalently, the Rosati relation A^dag = 2 A^(-1) holds, but this relation
alone has not constructed the positive Rosati/Hodge sign. The same
determinant-q integral graph package is formable on arbitrary control
matrices without Euler product, Satake parameters, rep_NS, off-diagonal
intersections, or a carrier-native positivity theorem.

Consequently integral q-similitude graph data constructs no rep_NS,
canonical pairing, off-diagonal intersections, positive Rosati, DH/Epstein
death, DD.4 weight>=1 datum, or End(S^2/Z).

Therefore integral q-similitude graph data cannot itself be promoted to the
positive square Frobenius graph carrier.
```

Verdict label:

```text
N1B_INTEGRAL_QSIM_GRAPH__SIMILITUDE_NOT_POSITIVE_ROSATI__NO_GO.
```

## 3. Proof

`prime_int_n1b_integral_qsim_graph_no_go` verifies the six gates.

IQG1 records the genuine finite-field block. For the genus-1 block at
`q=7`, the graph matrix is integral, the `q`-similitude defect and sampled
graph-law defect are zero, the radius defect is zero, and the primitive
Hodge sign is negative:

```text
H = -13.500.
```

IQG2 records the off-circle integral graph. For

```text
F = [[0,-2],[1,3]],
```

the eigenvalue moduli are `1` and `2`, while `sqrt(2)` is the expected
radius. Nevertheless `det(F)=2`, `F` is integral, the `q`-similitude defect
is zero, and the graph law is exact. The primitive Hodge index is

```text
H = +0.500.
```

Thus integrality plus `q`-similitude has not forced the Weil sign.

IQG3 records that this is a family phenomenon. The tested pairs

```text
(q,a) = (2,3), (2,4), (3,4), (5,5), (7,6)
```

all give integral determinant-`q` companion matrices with exact
`q`-similitude, positive radius defect, and positive primitive Hodge index.

IQG4 records the Rosati distinction. For the off-circle integral graph, the
relation

```text
F^dag = q F^{-1}
```

holds with zero residual. The primitive sign still fails. Therefore the
similitude/Rosati relation is not the same thing as positive Rosati.

IQG5 records control formability. The untyped control matrix

```text
[[1,1],[1,3]]
```

is integral, has determinant `2`, satisfies the standard `q`-similitude
relation, and obeys the graph law. It uses no Euler product, Satake
parameters, `rep_NS`, square intersections, or positive Rosati.

IQG6 records the construction failure: no `rep_NS`, canonical graph lattice,
canonical pairing, off-diagonal intersections, positive Rosati, control
death, or DD.4 weight>=1 datum is constructed.

The adjacent witness `theorem_B_similitude_signature` is the same structural
split in eigenbasis form: a similitude form exists at every radius, while
positive-definiteness holds exactly on the normalized circle.

## 4. Impact on R1

```text
R1 after docs 138-215:
  NEWLY CLOSED THIS CYCLE:
    - integral graph lattice plus determinant edge as Frobenius carrier,
      exact q-similitude as positive Rosati, F^dag=qF^{-1} as Hodge sign,
      and determinant-q integral controls as DH/Epstein guard (doc 215).

  STILL ADMISSIBLE:
    - a zeta-native square carrier whose lattice and pairing are constructed
      internally and whose primitive intersection form is positive/negative
      with the Weil sign;
    - a correspondence algebra with off-diagonal intersections, not merely a
      two-dimensional determinant-q graph;
    - a carrier-native theorem that upgrades the similitude relation to the
      positive Rosati/Hodge-index sign;
    - a construction that kills DH/Epstein before determinant-q graph data is
      even available.

  STILL OPEN:
    - construct rep_NS over Z with an integral graph carrier, canonical
      pairing, off-diagonal intersection form, positive Rosati, DD.4
      weight>=1 data, and square-side properness.
```

R1 remains open. This cycle closes the integral-graph version of the graph
shortcut: the relation `F^T E F=qE` is a necessary square-side relation, but
it is not the positive Rosati construction.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-IQG.1 integral graph as square carrier
  A proposal gives an integral graph matrix and declares Gamma constructed.
  Kill it unless the square carrier constructs rep_NS, the pairing, and the
  off-diagonal correspondences.

KILL-IQG.2 q-similitude as positive Rosati
  A proposal says F^T E F=qE forces the Weil sign. Kill it: determinant-q
  integral matrices can satisfy the relation off circle.

KILL-IQG.3 F^dag=qF^{-1} as Hodge positivity
  A proposal identifies the Rosati relation with positivity. Kill it unless
  it also proves the primitive Hodge-index sign from carrier-native square
  data.

KILL-IQG.4 determinant-q controls
  A proposal uses determinant-q integral graphs to distinguish zeta from
  controls. Kill it: arbitrary integral determinant-q controls have the same
  alternating q-similitude package.

KILL-IQG.5 integral q-similitude graph as End(S^2/Z)
  A proposal promotes integral q-similitude graph data to End(S^2/Z). Kill
  it unless it constructs rep_NS, canonical pairing, off-diagonal
  intersections, positive Rosati, square-side properness, Laurent boundary
  data, and DD.4 weight>=1.
```

## 6. Board

```text
doc-137 R1, cycle 78 = doc 215:
  N1B_INTEGRAL_QSIM_GRAPH__SIMILITUDE_NOT_POSITIVE_ROSATI__NO_GO.

What got built: no End object. The value is a sharper graph boundary:
integral graph data and exact q-similitude are still only Stage-A
similitude data; the positive Rosati/Hodge sign is not constructed by them.

What remains: construct the zeta-side rep_NS carrier; construct the integral
graph lattice and canonical pairing from that carrier; construct the
off-diagonal intersection form and positive Rosati theorem; construct
DH/Epstein death at carrier formation; solve DD.4 weights>=1 and square-side
iota/properness.
```
