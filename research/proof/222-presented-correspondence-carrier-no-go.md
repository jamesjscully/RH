# 222 - Presented correspondence carriers do not construct the square

Status: no-go + presented-carrier boundary, 2026-06-20. Eighty-fifth cycle of
the doc-137 construction arc. Doc 221 killed quotienting or retuning the
formal NS envelope to force the projection formula. This document tests the
next repair: define a universal/presented correspondence category whose
generators and relations include the desired graph, adjoint, projection, and
count identities from the start.

```text
formal quotient fails
  -> free/presented correspondence category with desired relations
  -> projection formula and count identities by presentation
  -> proper correspondence carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_presented_correspondence_carrier_no_go` (PCC1-PCC6 ALL PASS)
-- finite-field data can be encoded as a finite relation table, but that
constructs no square; the same presentation schema fits arbitrary control
count windows; finite presented windows admit ghost carrier extensions;
declared projection remains an axiom while the formal semantics still have
defect; all-count presentations import a trace oracle; and no square package
over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_projection_formula_quotient_no_go` (PFQ1-PFQ6 ALL PASS) and
`prime_int_n1b_finite_trace_realization_no_go` (FTR1-FTR6 ALL PASS).

## 1. Purpose

Doc 221 says projection identities cannot be imposed on the componentwise
formal NS law without damaging the finite-field anchor. The next formal repair
is to change the object of construction:

```text
Do not interpret the formal law.
Instead present a new category by generators and relations.
```

The presentation can include symbols `Delta`, `Gamma_n`, `Gamma_n^dag`, graph
composition relations, count relations

```text
Delta . Gamma_n = c_n,
```

and projection identities as axioms. This is not a construction of
`End(S^2/Z)`. It is a syntactic carrier with relation tables. Unless those
relations are represented by an actual square and proper correspondences, the
presentation imports the target behavior.

This document rejects only the shortcut:

```text
a universal/free/presented correspondence category with the desired relation
list constructs the square correspondence carrier required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 222.1 (Presentations are relation imports, not carriers).

A finite presentation with generators Delta, Gamma_n, formal adjoints, graph
relations, sampled projection identities, and sampled count identities can
encode a finite-field relation table. For the q=7, Tr(F)=1 anchor, a window
through n=4 records the counts

    7, 63, 364, 2331

in a finite list of relations.

This does not construct the square. The same finite presentation schema fits
arbitrary scalar count windows by Newton/companion realization, using no
Euler product, Satake parameters, rep_NS, or positive Rosati.

Finite relation windows also do not determine the carrier. A root-of-unity
ghost summand can have zero traces through the presented window while changing
the next count. Thus the relation table cannot certify the full graph carrier.

Declaring the projection formula inside the presentation does not construct
the projection calculus. Under the formal componentwise semantics the
projection defect remains nonzero; the presentation has merely asserted an
axiom.

If the presentation includes all scalar count identities, it imports the
target trace oracle. Without an independently constructed Euler/Satake square
carrier, those count relations are supplied data, not derived consequences.

Consequently presented correspondence carriers construct no rep_NS, actual
square, proper correspondence category, fiber-product composition,
carrier-native pairing, projection formula, degree character, Frobenius graph,
positive Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).

Therefore a universal or finitely presented correspondence category cannot
itself be promoted to the required square carrier.
```

Verdict label:

```text
N1B_PRESENTED_CORRESPONDENCE_CARRIER__RELATION_IMPORT_NOT_SQUARE__NO_GO.
```

## 3. Proof

`prime_int_n1b_presented_correspondence_carrier_no_go` verifies the six gates.

PCC1 records the finite-field relation table. For the `q=7`, `a=1` anchor,
the first four counts are

```text
7, 63, 364, 2331.
```

A finite presentation window containing graph, count, dagger, and sampled
projection relations has `87` formal relations. It encodes the table but
constructs no square or `rep_NS`.

PCC2 records control count formability. The same schema fits the arbitrary
control count window

```text
10, -3, 25, 6
```

by Newton/companion realization, producing traces

```text
-2, 53, 319, 2396.
```

No Euler product, Satake parameters, `rep_NS`, or positive Rosati is used.

PCC3 records finite-window non-determination. A root-of-unity ghost block
preserves the first four traces of the finite-field graph but changes the
fifth count by

```text
18.565.
```

Thus the finite presented carrier is not the graph carrier.

PCC4 records projection-by-assertion. The presentation may declare projection
as an axiom, but the componentwise formal semantics still has projection
defect

```text
27.
```

That is an assertion, not constructed correspondence calculus.

PCC5 records all-count oracle import. An all-count presentation can be given
the finite-field count sequence as relations, but then the count source is a
supplied oracle. The presentation does not derive those counts from a carrier
and does not kill controls.

PCC6 records the construction failure: no `rep_NS`, actual square, proper
correspondence category, fiber products, carrier-native pairing, projection
formula, degree character, Frobenius graph, positive Rosati, control death, or
DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-222:
  NEWLY CLOSED THIS CYCLE:
    - universal/free/presented correspondence category as square carrier,
      relation tables as proper correspondences, sampled projection/count
      identities as carrier construction, all-count presentations as
      Euler/Satake construction, and presented carriers as DH/Epstein guard
      (doc 222).

  STILL ADMISSIBLE:
    - a zeta-native square carrier that represents correspondences rather than
      presenting them by desired relations;
    - a carrier-native source of graph composition, degree maps, projection
      formula, and count identities;
    - an Euler/Satake construction of the count relations before they are
      used;
    - a positive Rosati theorem on an actual off-diagonal intersection form,
      with controls killed at carrier formation.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category, fiber-product composition, carrier-native
      degree maps, canonical pairing and projection formula, off-diagonal
      intersection form, preserved trace/count anchor, positive Rosati, DD.4
      weight>=1 data, and square-side properness.
```

R1 remains open. This cycle closes the presented-carrier repair: a category
defined by desired relations is not the square correspondence carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-PCC.1 presented category as square
  A proposal presents a correspondence category by generators and relations.
  Kill it unless the category is represented by an actual square carrier.

KILL-PCC.2 relation table as construction
  A proposal lists graph, count, projection, or adjoint relations. Kill it
  unless those relations are derived from carrier-native correspondences.

KILL-PCC.3 finite presentation window
  A proposal verifies finitely many presented relations. Kill it unless ghost
  extensions are excluded by a constructed carrier theorem.

KILL-PCC.4 all-count oracle
  A proposal includes the full trace/count sequence as relations. Kill it
  unless an Euler/Satake square carrier constructs that sequence first.

KILL-PCC.5 control survival
  A proposal's presentation schema can fit arbitrary control count windows.
  Kill it unless controls die at carrier formation.
```

