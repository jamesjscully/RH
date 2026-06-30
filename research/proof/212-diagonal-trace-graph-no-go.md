# 212 - Diagonal trace shadows do not construct Frobenius graphs

Status: no-go + post-anchor graph boundary, 2026-06-20. Seventy-fifth cycle
of the doc-137 construction arc. Doc 211 fixed the function-field square
anchor. This document tests the immediate shortcut: use only the scalar
diagonal intersections, or explicit-formula traces, as the zeta-side
Frobenius graph.

```text
Delta.Gamma_n scalar traces
  -> formal graph shadows
  -> Frobenius/Hecke graph
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_diagonal_trace_graph_no_go` (DTG1-DTG6 ALL PASS) -- the
genuine finite-field graph has diagonal counts, graph composition, and
`q`-similitude; trace-zero perturbations preserve all sampled
`Delta.Gamma_n` scalars while breaking graph composition and
`q`-similitude/Rosati; arbitrary scalar trace shadows are formable on
controls; and no square package over `Z` is built.

Adjacent witness, lead-reran this cycle:
`prime_int_n1b_ns_square_anchor` (NSA1-NSA6 ALL PASS).

## 1. Purpose

Doc 211 sharpened the target:

```text
Delta.Gamma_{F^n} = q^n + 1 - Tr(F^n)
```

inside a real square correspondence package. The tempting repair is to keep
only the scalar equality and define a zeta-side graph by matching those
diagonal intersections.

The issue is that the scalar equality is only one shadow of the graph. The
finite-field graph also carries:

```text
Gamma_m Gamma_n = Gamma_{m+n},
F^{n,T} E F^n = q^n E,
P_NS(z,w) = Tr(z w^dag),
```

plus off-diagonal pairings and a carrier-native reason DH/Epstein cannot form
the same object.

This document rejects only the shortcut:

```text
explicit-formula traces / diagonal intersections alone construct the
Frobenius graph required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 212.1 (Diagonal trace data is not graph data).

In the function-field square, the diagonal intersection of
Gamma_{F^n}=(q^n,F^n,1) is

    Delta.Gamma_{F^n} = q^n + 1 - Tr(F^n).

This scalar depends on the End slot only through Tr(F^n). Therefore, for any
trace-zero perturbation K_n, the shadow

    S_n = (q^n, F^n + K_n, 1)

has the same diagonal intersection with Delta.

But for generic K_n,

    (F^m+K_m)(F^n+K_n) != F^{m+n}+K_{m+n}

and

    (F^n+K_n)^T E (F^n+K_n) != q^n E.

Thus diagonal traces do not force graph composition or the Rosati
q-similitude relation. They also do not construct the off-diagonal
intersection form `Tr(z w^dag)`.

The trace-only operation is formable on arbitrary scalar control sequences:
choose any numbers t_n and set the End slot to a matrix with trace t_n. This
uses no Euler product, Satake parameter, correspondence algebra, or Rosati
duality. Therefore it is not a carrier guard and cannot be promoted to the
zeta-side square.

Consequently diagonal traces alone construct no `rep_NS`, graph law,
q-similitude, off-diagonal pairing, positive Rosati, DH/Epstein death,
DD.4 weight>=1 datum, or End(S^2/Z).

Therefore explicit-formula diagonal trace shadows cannot themselves be
promoted to Frobenius graphs or to End(S^2/Z).
```

Verdict label:

```text
N1B_DIAGONAL_TRACE_GRAPH__TRACE_SHADOW_NOT_GRAPH__NO_GO.
```

## 3. Proof

`prime_int_n1b_diagonal_trace_graph_no_go` verifies the six gates.

DTG1 records the genuine finite-field graph. For the `q=7, a1=1` model,
`Gamma_{F^n}` reproduces the diagonal counts, satisfies graph composition
for sampled powers, and has zero `q`-similitude defect.

DTG2 records the trace-shadow plant. For `n=1,2,3,4`, the perturbations

```text
S_n = (q^n, F^n + eps_n K, 1),  Tr(K)=0
```

preserve the sampled diagonal intersections:

```text
7, 63, 364, 2331.
```

DTG3 records the graph-law failure. The same shadows have composition
defects

```text
0.957, 5.801, 7.120.
```

DTG4 records the Rosati/q-similitude failure. The same shadows have
similitude defects

```text
0.141, 0.594, 0.859, 4.098.
```

DTG5 records the carrier guard failure. Arbitrary scalar control traces can
be realized by matrices with those traces, without Euler product, Satake
parameters, correspondence algebra, or Rosati duality.

DTG6 records the construction failure: no `rep_NS`, graph composition,
q-similitude, off-diagonal pairing, positive Rosati, control death, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-212:
  NEWLY CLOSED THIS CYCLE:
    - explicit-formula diagonal traces as Frobenius graphs, scalar
      Delta.Gamma_n data as correspondence algebra, trace-only graph shadows
      as End(S^2/Z), and arbitrary trace matching as DH/Epstein carrier guard
      (doc 212).

  STILL ADMISSIBLE:
    - a zeta-native graph whose composition law is constructed, not inferred
      from traces;
    - a square correspondence algebra whose off-diagonal pairings are
      constructed;
    - a carrier-native q-similitude/Rosati duality relation;
    - a construction that kills DH/Epstein before scalar trace matching.

  STILL OPEN:
    - construct `rep_NS` over Z with graph composition, off-diagonal
      intersection form, positive Rosati, DD.4 weight>=1 data, and
      square-side properness.
```

R1 remains open. This cycle prevents a direct promotion error after the
positive anchor: the explicit formula may provide the scalar target for
`Delta.Gamma_n`, but it is not the graph object.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-DTG.1 diagonal trace as graph
  A proposal defines Gamma_n only by matching Delta.Gamma_n. Kill it unless
  it also constructs graph composition and the End-slot action.

KILL-DTG.2 explicit formula as correspondence algebra
  A proposal promotes the explicit-formula trace functional to the full
  square correspondence algebra. Kill it: trace-zero perturbations preserve
  the scalar trace while changing the algebra.

KILL-DTG.3 trace matching as Rosati
  A proposal reads q-similitude or positive Rosati from diagonal traces.
  Kill it unless it constructs the cup/duality pairing and proves the
  q-similitude relation.

KILL-DTG.4 trace-only DH guard
  A proposal says trace matching distinguishes zeta from controls. Kill it:
  arbitrary scalar control traces can be represented by trace shadows.

KILL-DTG.5 graph shadow as End(S^2/Z)
  A proposal promotes formal graph shadows to the square object. Kill it
  unless it constructs rep_NS, graph law, off-diagonal pairings, positive
  Rosati, square-side properness, Laurent boundary data, and DD.4 weight>=1.
```

## 6. Board

```text
doc-137 R1, cycle 75 = doc 212:
  N1B_DIAGONAL_TRACE_GRAPH__TRACE_SHADOW_NOT_GRAPH__NO_GO.

What got built: no End object. The value is a sharper post-anchor boundary:
the scalar explicit-formula trace is only Delta.Gamma_n, not Gamma_n.

What remains: construct the zeta-side rep_NS carrier; construct graph
composition; construct the off-diagonal intersection form; construct the
q-similitude/Rosati duality pairing; construct DH/Epstein death at carrier
formation; solve DD.4 weights>=1 and square-side iota/properness.
```
