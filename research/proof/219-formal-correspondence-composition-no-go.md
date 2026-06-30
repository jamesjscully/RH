# 219 - Formal correspondence composition does not construct the square carrier

Status: no-go + formal-composition boundary, 2026-06-20. Eighty-second
cycle of the doc-137 construction arc. Doc 218 killed the formal
`Z^2 + Z[F]` NS envelope as a formula wrapper. This document tests the next
repair: add a composition law so the formal triples behave like
correspondences.

```text
formal NS envelope
  -> componentwise composition
  -> Delta identity and Gamma_m Gamma_n = Gamma_{m+n}
  -> correspondence category / square carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_formal_correspondence_composition_no_go` (FCC1-FCC6 ALL
PASS) -- the genuine finite-field graphs satisfy the formal composition law
and diagonal counts; the same formal law wraps off-circle graphs while
positivity fails; the same `z`-power semigroup can be paired with different
degree characters; formal composition permits an external `q` unrelated to
the graph's self-degree; the same composition envelope is formable on
controls; and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_formal_ns_envelope_no_go` (FNE1-FNE6 ALL PASS) and
`prime_int_n1b_integral_qsim_graph_no_go` (IQG1-IQG6 ALL PASS).

## 1. Purpose

Doc 218 says a formal `Z^2 + Z[F]` envelope only pastes the finite-field
intersection formula around a chosen operator. The immediate repair is to
give the formal triples a correspondence-like multiplication:

```text
(d1,z,d2) o (e1,w,e2) = (d1 e1, z w, d2 e2).
```

Then

```text
Delta = (1,Id,1)
```

is an identity and

```text
Gamma_m o Gamma_n = Gamma_{m+n}
```

for the assigned graphs `Gamma_n=(q^n,F^n,1)`.

This is still a formal wrapper. It is not geometric composition of proper
correspondences by fiber product. The degree character `q^n` is freely
chosen; the same `z`-power semigroup admits different degree characters, and
an unrelated external `q` can be used even when the operator has a different
self-degree. The same law wraps off-circle graphs and controls.

This document rejects only the shortcut:

```text
componentwise composition on formal triples constructs the square
correspondence carrier required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 219.1 (Formal composition is not fiber-product correspondence).

Given any operator F and scalar q, define

    Delta   = (1,Id,1),
    Gamma_n = (q^n,F^n,1),

and define componentwise composition by

    (d1,z,d2) o (e1,w,e2) = (d1 e1, z w, d2 e2).

Then Delta is an identity and Gamma_m o Gamma_n = Gamma_{m+n} by definition.

This does not construct a square or a correspondence category. The same law
works for off-circle q-similitude data where the primitive Hodge sign is
wrong. The same z-power semigroup can be paired with different degree
characters q^n, producing different diagonal intersections. Thus composition
does not construct the external base size or degree maps.

Even an operator with its own determinant/self-degree can be paired with an
unrelated external q; componentwise graph composition still holds. Therefore
the law does not enforce compatibility between graph degree, determinant,
q-similitude, and Rosati positivity.

The same formal composition envelope is formable on arbitrary control
matrices without Euler product, Satake parameters, rep_NS, square properness,
or carrier-native positivity.

Consequently formal correspondence composition constructs no rep_NS, actual
square, fiber-product composition, degree character, diagonal, Frobenius
graph, off-diagonal intersections, positive Rosati, DH/Epstein death, DD.4
weight>=1 datum, or End(S^2/Z).

Therefore componentwise formal composition cannot itself be promoted to the
square correspondence carrier.
```

Verdict label:

```text
N1B_FORMAL_CORRESPONDENCE_COMPOSITION__MONOID_LAW_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_formal_correspondence_composition_no_go` verifies the six
gates.

FCC1 records the finite-field anchor. For `q=7`, `a=1`, the formal graphs
satisfy

```text
Delta o Gamma_n = Gamma_n,
Gamma_m o Gamma_n = Gamma_{m+n},
Delta . Gamma_n = q^n + 1 - Tr(F^n).
```

All sampled defects are zero. This is the positive finite-field pattern.

FCC2 records the off-circle failure. For the integral `q=2`, `a=3` graph,
componentwise composition, identity, and exact `q`-similitude all hold, while
the primitive Hodge index is

```text
H = +0.500.
```

Thus formal composition has not constructed positivity.

FCC3 records degree-character freedom. The same `z=F^2` component can be
paired with degrees

```text
7^2 = 49, 11^2 = 121.
```

Both choices satisfy the formal graph law. Their `Delta.Gamma_1`
intersections differ:

```text
7, 11.
```

The degree character is chosen, not constructed.

FCC4 records self-degree incompatibility. A graph with self-degree `5` can
be placed in a formal graph family with external degree character `7^n`.
The formal composition defect is zero, but the external `q`-similitude defect
is `2.828`.

FCC5 records control formability. The formal composition envelope can be put
around the untyped control matrix `[[1,2],[1,4]]`; it has identity and graph
law, but no Euler product, Satake parameters, `rep_NS`, square properness, or
positive Rosati.

FCC6 records the construction failure: no `rep_NS`, actual square,
fiber-product composition, degree character, carrier-native graph,
off-diagonal intersections, positive Rosati, control death, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-219:
  NEWLY CLOSED THIS CYCLE:
    - componentwise triple multiplication as correspondence composition,
      Delta identity by assignment, Gamma_m Gamma_n=Gamma_{m+n} as square
      graph carrier, formal degree characters as fiber-degree construction,
      and formal composition envelopes as DH/Epstein guard (doc 219).

  STILL ADMISSIBLE:
    - a zeta-native square carrier whose composition is induced by actual
      proper correspondences/fiber products;
    - carrier-native degree maps tied to the graph and base size;
    - a Frobenius/Hecke graph whose composition, diagonal intersections, and
      Rosati positivity are consequences of the same square carrier;
    - a construction that kills DH/Epstein before formal composition can be
      assigned.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, genuine
      correspondence composition, integral graph lattice, canonical pairing,
      off-diagonal intersection form, positive Rosati, DD.4 weight>=1 data,
      and square-side properness.
```

R1 remains open. This cycle closes the composition repair of the formal NS
envelope: a monoid law on symbols is not a square correspondence carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FCC.1 componentwise composition as correspondences
  A proposal defines (d1,z,d2)o(e1,w,e2) componentwise. Kill it unless the
  law is induced by actual proper correspondences/fiber products.

KILL-FCC.2 assigned graph law
  A proposal says Gamma_m Gamma_n=Gamma_{m+n}. Kill it unless the graph
  classes and their composition are carrier-native.

KILL-FCC.3 degree character by choice
  A proposal supplies q^n as the graph degree character. Kill it unless q and
  the degree maps are constructed by the square carrier.

KILL-FCC.4 external q despite self-degree
  A proposal pairs an operator with an unrelated external q inside a formal
  graph monoid. Kill it unless determinant, degree, q-similitude, and Rosati
  are tied by the carrier.

KILL-FCC.5 formal composition as carrier guard
  A proposal uses the formal composition envelope to distinguish zeta from
  controls. Kill it: arbitrary controls can be wrapped the same way.

KILL-FCC.6 formal composition as End(S^2/Z)
  A proposal promotes formal composition triples to End(S^2/Z). Kill it
  unless it constructs the actual square, proper correspondence composition,
  canonical degree maps, diagonal, Frobenius graph, off-diagonal
  intersections, positive Rosati, Laurent boundary data, and DD.4 weight>=1.
```

## 6. Board

```text
doc-137 R1, cycle 82 = doc 219:
  N1B_FORMAL_CORRESPONDENCE_COMPOSITION__MONOID_LAW_NOT_CARRIER__NO_GO.

What got built: no End object. The value is a sharper square boundary:
componentwise multiplication makes a graph monoid on symbols, but it neither
constructs a square nor a fiber-product correspondence category.

What remains: construct the zeta-side rep_NS carrier as an actual
representability functor; construct proper correspondence composition,
degree maps, diagonal, graph, and intersection form from that carrier;
construct positive Rosati without changing q; construct DH/Epstein death at
carrier formation; solve DD.4 weights>=1 and square-side iota/properness.
```
