# 218 - A formal NS envelope does not construct rep_NS

Status: no-go + formal-envelope boundary, 2026-06-20. Eighty-first cycle
of the doc-137 construction arc. Doc 217 killed the cyclic graph algebra
`Z[F]` as `rep_NS` because it only sees the `z`-component. This document
tests the immediate repair: add the two missing fiber-degree slots by hand.

```text
Z[F] too small
  -> formal Z^2 + Z[F] envelope
  -> intersection d1 e2 + d2 e1 - Tr(zw)
  -> Delta=(1,Id,1), Gamma_F=(q,F,1)
  -> rep_NS over Z
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_formal_ns_envelope_no_go` (FNE1-FNE6 ALL PASS) -- the
genuine finite-field envelope reproduces the doc-211 diagonal intersections;
the same formal recipe wraps an off-circle graph while positivity fails;
diagonal traces do not determine the two fiber degrees; the indecomposable
diagonal can be inserted for controls; arbitrary control count windows can
be calibrated by choosing fiber degrees; and no square package over `Z` is
built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cyclic_graph_algebra_no_go` (CGA1-CGA6 ALL PASS) and
`prime_int_n1b_ns_square_anchor` (NSA1-NSA6 ALL PASS).

## 1. Purpose

Doc 217 says the cyclic algebra `Z[F]` is not the NS square because it only
records the End(H^1) component `z`. The next repair is to add the missing
slots syntactically:

```text
Corr_form(F) = Z . e_1  +  Z[F]  +  Z . e_2,
```

with finite-field intersection formula

```text
(d1,z,d2) . (e1,w,e2) = d1 e2 + d2 e1 - Tr(z w).
```

Then choose

```text
Delta   = (1, Id, 1),
Gamma_n = (q^n, F^n, 1).
```

This reproduces the shape of doc 211. The question is whether it constructs
the over-`Z` square carrier.

It does not. It is a formal envelope around a chosen operator. The fiber
degrees, diagonal, graph, and intersection formula are assigned rather than
represented by a proper square. The same formal wrapper can be put around
off-circle graphs and arbitrary controls, and scalar diagonal intersections
can be calibrated by choosing the degree slots.

This document rejects only the shortcut:

```text
the formal Z^2 + Z[F] envelope with the finite-field formula constructs
rep_NS and therefore End(S^2/Z).
```

## 2. Lemma

```text
Lemma 218.1 (Formal NS envelopes are specification wrappers).

Given any operator F and scalar q, define formal triples (d1,z,d2) and the
bilinear form

    (d1,z,d2).(e1,w,e2) = d1 e2 + d2 e1 - Tr(z w).

Set Delta=(1,Id,1) and Gamma_n=(q^n,F^n,1). Then

    Delta.Gamma_n = q^n + 1 - Tr(F^n)

by definition.

This reproduces the finite-field formula but does not construct the
finite-field object. It does not produce a square, proper correspondences,
fiber-degree maps, an indecomposable diagonal, a Frobenius graph, or a
Rosati/Hodge-index positivity theorem from a carrier.

The diagonal intersection only fixes d1+d2-Tr(z). For fixed z, many pairs
(d1,d2) have the same diagonal intersection. Thus the two fiber degrees are
not constructed by the scalar trace data.

The same formal envelope can wrap off-circle q-similitude graphs, where the
primitive Hodge sign is wrong, and it can wrap arbitrary control operators.
Indeed arbitrary scalar count windows can be matched by solving for d1 after
choosing d2.

Consequently a formal NS envelope constructs no rep_NS, actual square,
fiber-degree maps, carrier-native diagonal, Frobenius graph, off-diagonal
intersections, positive Rosati, DH/Epstein death, DD.4 weight>=1 datum, or
End(S^2/Z).

Therefore formal Z^2 + Z[F] envelopes cannot themselves be promoted to the
square correspondence carrier.
```

Verdict label:

```text
N1B_FORMAL_NS_ENVELOPE__FORMULA_WRAPPER_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_formal_ns_envelope_no_go` verifies the six gates.

FNE1 records the finite-field anchor. For `q=7`, `a=1`, the formal envelope
with

```text
Delta=(1,Id,1), Gamma_n=(q^n,F^n,1)
```

reproduces the diagonal intersections:

```text
7, 63, 364.
```

The diagonal is indecomposable because `z=Id`. This is exactly the doc-211
specification, and is the positive anchor.

FNE2 records the off-circle failure. The same formal recipe wraps

```text
F = [[0,-2],[1,3]], q=2.
```

It gives `Delta.Gamma=0` by formula, while the primitive Hodge index is

```text
H = +0.500.
```

Thus the formal envelope has not constructed positivity.

FNE3 records fiber-degree freedom. For the same `z=F`, the degree pairs

```text
(7,1), (6,2), (0,8)
```

all give the same diagonal intersection `7`. Scalar diagonal traces do not
construct the two fiber degrees.

FNE4 records diagonal insertion. The same `Delta=(1,Id,1)` can be assigned
to an untyped control matrix; product/fiber classes are then declared to
have `z=0`. Indecomposability is inserted by choosing `z=Id`, not produced
by a square carrier.

FNE5 records control calibration. For an arbitrary control matrix, the
formal envelope realizes the target scalar window

```text
10, -3, 25
```

by solving for the degree slot `d1` after setting `d2=1`. This uses no Euler
product, Satake parameters, `rep_NS`, square properness, or positive Rosati.

FNE6 records the construction failure: no `rep_NS`, actual square, fiber
degrees, carrier-native diagonal, Frobenius graph, off-diagonal
intersections, positive Rosati, control death, or DD.4 weight>=1 datum is
constructed.

## 4. Impact on R1

```text
R1 after docs 138-218:
  NEWLY CLOSED THIS CYCLE:
    - formal Z^2 + Z[F] envelope as rep_NS, pasted finite-field intersection
      formula as square carrier, assigned Delta=(1,Id,1) as constructed
      diagonal, assigned Gamma_n=(q^n,F^n,1) as Frobenius graph, scalar
      diagonal intersections as fiber-degree construction, and formal
      envelopes as DH/Epstein guard (doc 218).

  STILL ADMISSIBLE:
    - a zeta-native square carrier that represents correspondences and
      produces the degree maps d1,d2, not a formal direct-sum wrapper;
    - a carrier-native diagonal and Frobenius/Hecke graph whose diagonal
      intersections are consequences, not definitions;
    - off-diagonal intersection and Rosati positivity theorems tied to the
      constructed square;
    - a construction that kills DH/Epstein before a formal envelope can be
      assigned.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, integral graph
      lattice, canonical pairing, off-diagonal intersection form, positive
      Rosati, DD.4 weight>=1 data, and square-side properness.
```

R1 remains open. This cycle closes the formal-envelope shortcut: copying the
finite-field formula is not construction of the finite-field object over
`Z`.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FNE.1 formal envelope as rep_NS
  A proposal defines Z^2 + Z[F] and calls it rep_NS. Kill it unless the
  square carrier represents those triples and degree maps.

KILL-FNE.2 pasted intersection formula
  A proposal imports d1 e2 + d2 e1 - Tr(zw) as a definition. Kill it unless
  the formula is induced by a constructed intersection theory.

KILL-FNE.3 assigned diagonal or graph
  A proposal sets Delta=(1,Id,1) or Gamma_n=(q^n,F^n,1). Kill it unless
  these classes are produced by the carrier.

KILL-FNE.4 scalar trace as fiber degrees
  A proposal uses Delta.Gamma_n values to recover d1,d2. Kill it: the scalar
  fixes only d1+d2-Tr(z), and many degree pairs give the same value.

KILL-FNE.5 formal envelope as carrier guard
  A proposal uses the formal envelope to distinguish zeta from controls.
  Kill it: arbitrary controls can be wrapped and calibrated the same way.

KILL-FNE.6 formal NS envelope as End(S^2/Z)
  A proposal promotes formal triples to End(S^2/Z). Kill it unless it
  constructs the actual square, proper correspondences, canonical degree
  maps, diagonal, Frobenius graph, off-diagonal intersections, positive
  Rosati, Laurent boundary data, and DD.4 weight>=1.
```

## 6. Board

```text
doc-137 R1, cycle 81 = doc 218:
  N1B_FORMAL_NS_ENVELOPE__FORMULA_WRAPPER_NOT_CARRIER__NO_GO.

What got built: no End object. The value is a sharper square boundary:
formal triples reproduce the finite-field formula syntactically, but they do
not construct the square correspondence carrier or its positivity.

What remains: construct the zeta-side rep_NS carrier as an actual
representability functor; construct the diagonal, graph, degree maps, and
intersection form from that carrier; construct positive Rosati without
changing q; construct DH/Epstein death at carrier formation; solve DD.4
weights>=1 and square-side iota/properness.
```
