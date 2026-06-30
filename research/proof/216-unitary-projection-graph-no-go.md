# 216 - Unitary projection does not construct the square graph carrier

Status: no-go + unitary-projection boundary, 2026-06-20. Seventy-ninth
cycle of the doc-137 construction arc. Doc 215 killed integral
`q`-similitude graph data as positive Rosati. This document tests the
immediate repair: normalize the graph by `sqrt(q)` and project it to a
unitary/compact graph.

```text
integral q-similitude graph
  -> normalize by sqrt(q)
  -> radial or polar unitary projection
  -> positive Rosati / compact graph carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_unitary_projection_graph_no_go` (UPG1-UPG6 ALL PASS) -- a
spectral radial projection preserves a genuine on-circle finite-field graph,
but on an off-circle integral `q`-similitude it repairs the radius only by
changing graph traces and losing integrality; Euclidean polar projection is
metric-dependent and changes even the genuine finite-field graph; the
original off-circle normalized graph has only an indefinite invariant form;
the same projections are formable on controls; and no square package over
`Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_integral_qsim_graph_no_go` (IQG1-IQG6 ALL PASS) and
`prime_int_n1b_frobenius_tannakian_compactness_no_go` (FTC1-FTC6 ALL PASS).

## 1. Purpose

Doc 215 says exact `q`-similitude is only Stage-A duality/similitude. The
natural repair is to make Stage B by force:

```text
take F / sqrt(q),
project it onto a unitary operator,
and use that compact graph as the positive Rosati carrier.
```

There are two standard versions.

```text
1. Spectral radial projection:
     keep eigenvectors, replace each alpha by sqrt(q) alpha/|alpha|.

2. Polar projection:
     choose a background metric, take the polar unitary of F/sqrt(q),
     and rescale by sqrt(q).
```

Both miss the square carrier. Spectral radial projection preserves a true
finite-field graph only because the graph is already on the correct radius.
Off circle, it changes the power traces and usually loses integrality, so it
is no longer the graph whose diagonal intersections give the counts. Polar
projection is worse as a carrier operation: without the Rosati metric, it
depends on an external background metric and can change even the genuine
finite-field graph.

This document rejects only the shortcut:

```text
post-hoc unitary projection constructs the positive square Frobenius graph
required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 216.1 (Unitary projection is not square-carrier construction).

Let F be an integral determinant-q graph satisfying F^T E F=qE.

If the eigenvalues of F already have modulus sqrt(q), spectral radial
projection is the identity. This is the genuine finite-field case.

If F is off circle, spectral radial projection changes the power traces
Tr(F^n) and can destroy integrality. Therefore it no longer preserves the
diagonal intersections Delta.Gamma_n = q^n + 1 - Tr(F^n), and it is not the
same Frobenius/Hecke graph.

Polar projection requires a background positive metric. With the Euclidean
metric, the polar unitary of F/sqrt(q) can change even a genuine
finite-field graph. Choosing a different metric gives a different projection.
The metric that would make the true graph unitary is precisely the
carrier-native positive Rosati datum, not an output of the projection.

For the off-circle graph [[0,-2],[1,3]] at q=2, the normalized graph has no
positive invariant symmetric form; the invariant form is indefinite. Thus
compactness/positivity is not recovered without either changing the graph or
importing a metric.

The same radial and polar projections are formable on arbitrary controls
without Euler product, Satake parameters, rep_NS, square intersections, or
carrier-native positivity.

Consequently unitary projection constructs no rep_NS, canonical unitary
projection, original graph, canonical pairing, off-diagonal intersections,
positive Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).

Therefore post-hoc unitary projection cannot itself be promoted to the
positive square Frobenius graph carrier.
```

Verdict label:

```text
N1B_UNITARY_PROJECTION_GRAPH__CHANGES_GRAPH_OR_IMPORTS_METRIC__NO_GO.
```

## 3. Proof

`prime_int_n1b_unitary_projection_graph_no_go` verifies the six gates.

UPG1 records the genuine finite-field case. For the genus-1 block at `q=7`,
spectral radial projection changes the graph by only numerical roundoff:

```text
||R(F)-F|| = 1.8e-15,
trace_delta <= 4.3e-14,
integral_defect = 1.8e-15.
```

This is not a construction; it is the already-pure case.

UPG2 records the off-circle integral `q`-similitude graph from doc 215:

```text
F = [[0,-2],[1,3]], q=2.
```

Spectral radial projection repairs the normalized radius defect

```text
0.414 -> 0,
```

but changes the graph traces and loses integrality:

```text
trace_delta = 9.000,
integral_defect = 0.414.
```

The projected graph still has graph law and the standard `q`-similitude, but
it is no longer the original integral graph whose diagonal intersections
encode the counts.

UPG3 records the polar-projection problem. Using the standard Euclidean
metric, the polar projection is unitary after normalization, but it changes
even the genuine finite-field graph:

```text
orth_defect = 4.5e-16,
trace_delta = 15.124,
integral_defect = 0.375.
```

Thus polar projection is not canonical square data unless the correct metric
has already been constructed.

UPG4 records non-polarizability of the original off-circle graph. Solving
`N^T H N = H` for `N=F/sqrt(2)` gives an invariant symmetric form with
eigenvalues

```text
-1.144306, 0.030134.
```

The residual is `2.8e-16`, so the invariant form is real, but it is
indefinite. This is the same Stage-A/Stage-B split as doc 207.

UPG5 records control formability. Radial and polar projection can be applied
to the untyped control matrix `[[1,1],[1,3]]`; the operation uses no Euler
product, Satake parameters, `rep_NS`, square intersections, or positive
Rosati.

UPG6 records the construction failure: no `rep_NS`, canonical unitary
projection, original graph, canonical pairing, off-diagonal intersections,
positive Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-216:
  NEWLY CLOSED THIS CYCLE:
    - spectral radial projection as Frobenius graph repair, polar projection
      as carrier-native positive Rosati, Euclidean compactification of the
      graph, unitary projection as DH/Epstein guard, and post-hoc
      unitarization as End(S^2/Z) (doc 216).

  STILL ADMISSIBLE:
    - a zeta-native square carrier whose graph is already pure because the
      carrier constructs the correct pairing and Hodge sign;
    - a canonical metric/pairing constructed by rep_NS and off-diagonal
      intersections, not chosen as a background for polar decomposition;
    - a theorem that proves positivity while preserving the original graph
      traces, integrality, and square intersections;
    - a construction that kills DH/Epstein before any spectral or polar
      projection can be formed.

  STILL OPEN:
    - construct rep_NS over Z with an integral graph carrier, canonical
      pairing, off-diagonal intersection form, positive Rosati, DD.4
      weight>=1 data, and square-side properness.
```

R1 remains open. This cycle closes the post-hoc compactification version of
the graph shortcut: unitarization after the fact either changes the graph or
chooses the metric whose construction is the problem.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-UPG.1 radial projection as graph carrier
  A proposal moves eigenvalues to the circle and keeps the same graph name.
  Kill it unless it preserves the original traces, integrality, and diagonal
  intersections.

KILL-UPG.2 polar projection as Rosati construction
  A proposal takes a polar unitary using a background metric. Kill it unless
  the metric is constructed by the square carrier; otherwise Rosati is an
  input.

KILL-UPG.3 unitary projection as positivity proof
  A proposal says the projected graph is positive. Kill it unless the
  original graph is positive without changing its traces or correspondence
  class.

KILL-UPG.4 projection as carrier guard
  A proposal uses unitary projection to distinguish zeta from controls. Kill
  it: arbitrary controls admit the same radial and polar projections.

KILL-UPG.5 projected graph as End(S^2/Z)
  A proposal promotes a projected unitary graph to End(S^2/Z). Kill it
  unless it constructs rep_NS, canonical pairing, off-diagonal
  intersections, positive Rosati, square-side properness, Laurent boundary
  data, and DD.4 weight>=1 while preserving the original graph.
```

## 6. Board

```text
doc-137 R1, cycle 79 = doc 216:
  N1B_UNITARY_PROJECTION_GRAPH__CHANGES_GRAPH_OR_IMPORTS_METRIC__NO_GO.

What got built: no End object. The value is a sharper graph boundary:
post-hoc unitarization is not carrier construction. Radial projection changes
off-circle graph data; polar projection imports a metric.

What remains: construct the zeta-side rep_NS carrier; construct the integral
graph lattice and canonical pairing from that carrier; construct the
off-diagonal intersection form and positive Rosati theorem without changing
the graph; construct DH/Epstein death at carrier formation; solve DD.4
weights>=1 and square-side iota/properness.
```
