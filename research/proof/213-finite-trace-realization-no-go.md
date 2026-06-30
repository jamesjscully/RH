# 213 - Finite trace realizations do not construct the square graph carrier

Status: no-go + finite-realization boundary, 2026-06-20. Seventy-sixth cycle
of the doc-137 construction arc. Doc 212 killed scalar diagonal traces as
Frobenius graphs. This document tests the stronger repair: enforce graph
composition by choosing an operator `A` and using `A^n` as the graph shadow.

```text
finite explicit-formula traces
  -> companion/Newton operator A
  -> semigroup A^n
  -> Frobenius/Hecke graph
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_finite_trace_realization_no_go` (FTR1-FTR6 ALL PASS) -- the
genuine finite-field operator has traces, graph law, `q`-similitude, and the
right Hodge sign; finite trace windows admit ghost semigroup summands;
semigroup trace realizations need not be `q`-similitudes; graph law plus
determinant edge can remain off-circle; Newton/companion finite trace
realization is formable on arbitrary controls; and no square package over `Z`
is built.

Adjacent witness, lead-reran this cycle:
`prime_int_n1b_diagonal_trace_graph_no_go` (DTG1-DTG6 ALL PASS).

## 1. Purpose

Doc 212 says scalar diagonal intersections do not define a graph. The
immediate repair is to add graph composition syntactically:

```text
choose A with Tr(A^n) matching the observed traces,
then declare Gamma_n = A^n.
```

This does produce a semigroup, but it still does not construct the square
carrier. The finite-field anchor supplies a carrier-native operator acting on
`H^1`, a square `rep_NS`, off-diagonal pairings, and a positive Rosati
duality. A finite trace realization supplies only an operator selected to fit
some scalar data.

This document rejects only the shortcut:

```text
finite-window operator realization of explicit-formula traces constructs the
Frobenius/Hecke graph required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 213.1 (Finite trace realization is not a carrier construction).

Let F be the finite-field Frobenius operator. For any finite window N, one
can adjoin a ghost semigroup summand B whose first N power traces vanish.
Then

    Tr((F direct_sum B)^n) = Tr(F^n),  1 <= n <= N,

while the future trace, dimension, determinant data, and polarization
requirements change.

Thus finite trace windows do not determine a canonical graph carrier, even
when graph composition is enforced by using powers of one operator.

Moreover, graph law plus determinant edge is not Rosati positivity. An
off-circle two-eigenvalue operator can have determinant q, a semigroup law,
and the standard two-dimensional q-similitude relation while the primitive
Hodge index has the wrong sign.

Finally, finite Newton/companion realization is formable on arbitrary scalar
control traces: the first d power sums determine a degree-d polynomial by
Newton identities. This uses no Euler product, Satake parameters,
correspondence algebra, or Rosati duality.

Consequently finite trace realization constructs no `rep_NS`, canonical
operator, square H2, off-diagonal pairing, positive Rosati, DH/Epstein death,
DD.4 weight>=1 datum, or End(S^2/Z).

Therefore finite trace realization cannot itself be promoted to the square
Frobenius graph carrier.
```

Verdict label:

```text
N1B_FINITE_TRACE_REALIZATION__OPERATOR_FIT_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_finite_trace_realization_no_go` verifies the six gates.

FTR1 records the genuine finite-field operator for the `q=7, a1=1` model.
It has the trace sequence

```text
1, -13, -20, 71, ...
```

with zero composition defect, zero `q`-similitude defect, and negative
primitive Hodge index.

FTR2 records finite-window underdetermination. A root-of-unity ghost block
has zero power trace for the first five powers, so the direct sum with `F`
matches the first five traces exactly. At the sixth trace it differs by
`28.961`.

FTR3 records that the augmented semigroup trace realization is not a
`q`-similitude carrier; its sampled defect is `17.639`.

FTR4 records that even graph law plus determinant edge and two-dimensional
`q`-similitude do not force Rosati positivity. An off-circle diagonal
operator has determinant `q`, exact graph law, and `q`-similitude defect
`1.3e-15`, but its primitive Hodge index is positive: `2.023`.

FTR5 records control formability. The arbitrary scalar control traces

```text
3, -5, 8, 13
```

are realized by Newton/companion roots without Euler product, Satake
parameters, correspondence algebra, or Rosati duality.

FTR6 records the construction failure: no `rep_NS`, canonical operator,
square H2, off-diagonal pairing, positive Rosati, control death, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-213:
  NEWLY CLOSED THIS CYCLE:
    - finite-window explicit-formula trace realization as Frobenius graph,
      companion/Newton operator fit as carrier, semigroup powers A^n as
      End(S^2/Z), determinant-edge graph law as Rosati positivity, and
      finite trace matching as DH/Epstein carrier guard (doc 213).

  STILL ADMISSIBLE:
    - a zeta-native graph whose operator is constructed by the carrier, not
      fitted to a finite trace window;
    - a square correspondence algebra with off-diagonal pairings;
    - a carrier-native q-similitude/Rosati duality relation;
    - a construction that kills DH/Epstein before trace realization.

  STILL OPEN:
    - construct `rep_NS` over Z with a canonical graph carrier, graph
      composition, off-diagonal intersection form, positive Rosati, DD.4
      weight>=1 data, and square-side properness.
```

R1 remains open. This cycle prevents the natural strengthening of doc 212's
trace-shadow shortcut: adding a fitted semigroup operator still does not
construct the square object.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FTR.1 finite trace window as graph carrier
  A proposal constructs A from finitely many explicit-formula traces and
  declares Gamma_n=A^n. Kill it unless the carrier constructs A
  canonically and proves stability beyond the finite window.

KILL-FTR.2 companion/Newton fit as End(S^2/Z)
  A proposal uses Newton identities or a companion matrix as the graph.
  Kill it: the same finite realization works for arbitrary control traces.

KILL-FTR.3 ghost-free finite realization
  A proposal says the finite trace window determines the carrier. Kill it:
  ghost semigroup summands can preserve the window and change later traces.

KILL-FTR.4 graph law plus determinant as Rosati
  A proposal says A^n and det(A)=q force positivity. Kill it: off-circle
  operators retain graph law and determinant edge while failing Hodge sign.

KILL-FTR.5 finite realization as square package
  A proposal promotes a fitted operator to End(S^2/Z). Kill it unless it
  constructs rep_NS, square H2, off-diagonal pairings, positive Rosati,
  square-side properness, Laurent boundary data, and DD.4 weight>=1.
```

## 6. Board

```text
doc-137 R1, cycle 76 = doc 213:
  N1B_FINITE_TRACE_REALIZATION__OPERATOR_FIT_NOT_CARRIER__NO_GO.

What got built: no End object. The value is a sharper graph boundary:
semigroup composition obtained by fitting an operator to traces is not a
carrier-native Frobenius graph.

What remains: construct the zeta-side rep_NS carrier; construct a canonical
graph operator from the carrier; construct the off-diagonal intersection
form; construct q-similitude/Rosati duality and positivity; construct
DH/Epstein death at carrier formation; solve DD.4 weights>=1 and square-side
iota/properness.
```
