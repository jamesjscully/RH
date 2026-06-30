# 223 - Numerical/GNS quotients do not construct positive Rosati

Status: no-go + numerical-quotient boundary, 2026-06-20. Eighty-sixth cycle
of the doc-137 construction arc. Doc 222 killed universal/free/presented
correspondence carriers as relation import. This document tests the next
repair: add a numerical pairing to the presented carrier, quotient by the
radical, or take a GNS/positive-part quotient to obtain a positive Rosati
carrier.

```text
presented correspondence carrier
  -> numerical pairing / Gram form
  -> radical quotient or GNS positive quotient
  -> positive Rosati carrier
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_numerical_gns_quotient_no_go` (NGQ1-NGQ6 ALL PASS) -- the
genuine finite-field `Delta/Gamma` intersection Gram is indefinite with no
radical; projecting to the positive part changes non-null finite-field anchor
data; Rosati positivity is a different carrier-native pairing, not a radical
quotient of the presented intersection form; finite numerical windows admit
ghost extensions; the same Gram/radical/GNS operation is formable on controls;
and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_presented_correspondence_carrier_no_go` (PCC1-PCC6 ALL PASS)
and `prime_int_n1b_projection_formula_quotient_no_go` (PFQ1-PFQ6 ALL PASS).

## 1. Purpose

Doc 222 says a presented category only imports desired relations. The natural
repair is to add a numerical pairing and then perform the standard numerical
equivalence/GNS move:

```text
quotient by the radical, or keep only the positive part.
```

This is not construction of positive Rosati. On the finite-field anchor, the
intersection pairing on the visible `Delta/Gamma` plane is already
nondegenerate and indefinite. A radical quotient has no radical to remove.
A positive-part quotient can make a positive semidefinite form only by changing
non-null finite-field pairing data. The actual Rosati-positive pairing is a
different carrier-native structure; it is not recovered by quotienting the
formal/presented NS intersection form.

This document rejects only the shortcut:

```text
numerical radical quotient, GNS quotient, or positive-part completion of a
presented correspondence carrier constructs the positive Rosati square carrier
required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 223.1 (Numerical quotients are not Rosati construction).

For the finite-field q=7, Tr(F)=1 anchor, take the two classes

    Delta=(1,Id,1), Gamma=(q,F,1).

Their NS intersection Gram is

    [[0, 7],
     [7, 27]].

Its eigenvalues are approximately

    -1.707, 28.707.

Thus the form is indefinite and has no radical. Quotienting by the radical
does nothing and leaves the negative direction.

Projecting to the positive part drops one non-null direction and changes the
Gram. This is not numerical equivalence; it modifies finite-field anchor data.

The Rosati-positive pairing is separate. For the same graph,

    Gamma.Gamma = 27,
    Tr(F F^dag) = 14.

The positive Rosati form is not obtained by radical quotient of the displayed
intersection plane; it comes from the carrier-native polarization.

Finite numerical quotients do not determine a carrier: ghost semigroup
summands can preserve a finite trace window while changing the next count.
The same Gram/radical/GNS operations are formable on arbitrary control count
data without Euler product, Satake parameters, rep_NS, square properness, or
positive Rosati.

Consequently numerical radical or GNS quotienting constructs no rep_NS,
actual square, proper correspondence category, fiber-product composition,
carrier-native pairing, numerical equivalence theorem, Frobenius graph,
positive Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).

Therefore numerical/GNS quotienting cannot itself be promoted to the positive
Rosati square carrier.
```

Verdict label:

```text
N1B_NUMERICAL_GNS_QUOTIENT__POSITIVE_PART_NOT_ROSATI_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_numerical_gns_quotient_no_go` verifies the six gates.

NGQ1 records the finite-field Gram. The `Delta/Gamma` plane has

```text
Gram = [[0,7],[7,27]],
eigenvalues = -1.707, 28.707,
inertia = (1,1,0).
```

There is no radical.

NGQ2 records the positive-part modification. Projecting to the positive part
gives a positive semidefinite rank-one form but changes the Gram with norm

```text
1.707.
```

One non-null direction has been dropped.

NGQ3 records the Rosati mismatch. On the same graph,

```text
Gamma.Gamma = 27,
Tr(F F^dag) = 14,
radical dimension = 0.
```

Radical quotienting does not recover the Rosati pairing.

NGQ4 records finite-window non-determination. A ghost summand preserves the
first four traces but changes the fifth count by

```text
15.259.
```

Thus finite numerical quotient data does not determine the graph carrier.

NGQ5 records control formability. The arbitrary control Gram

```text
[[0,10],[10,-39]]
```

has the same indefinite/no-radical shape; positive-part projection changes it
with norm `41.415`. No Euler product, Satake parameters, `rep_NS`, or positive
Rosati is used.

NGQ6 records the construction failure: no `rep_NS`, actual square, proper
correspondences, fiber products, carrier-native pairing, numerical
equivalence theorem, positive Rosati, Frobenius graph, control death, or DD.4
weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-223:
  NEWLY CLOSED THIS CYCLE:
    - numerical radical quotient of a presented carrier as positive Rosati,
      GNS/positive-part quotient as numerical correspondence construction,
      finite Gram positivity as square carrier, and numerical quotient
      repairs as DH/Epstein guard (doc 223).

  STILL ADMISSIBLE:
    - a zeta-native square carrier whose numerical equivalence is induced by
      actual correspondences and a carrier-native intersection theory;
    - a Rosati-positive pairing constructed from the square polarization, not
      from changing an indefinite presented Gram;
    - a carrier theorem excluding ghost extensions and killing controls;
    - a proof that the count/graph/projection/Rosati structures all come from
      one square carrier.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, proper
      correspondence category, fiber-product composition, carrier-native
      degree maps, canonical pairing and numerical equivalence, projection
      formula, off-diagonal intersection form, preserved trace/count anchor,
      positive Rosati, DD.4 weight>=1 data, and square-side properness.
```

R1 remains open. This cycle closes the numerical/GNS quotient repair:
quotienting or completing a presented Gram is not construction of the positive
Rosati carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-NGQ.1 radical quotient as positivity
  A proposal quotients the presented correspondence pairing by its radical and
  calls the result positive Rosati. Kill it unless the finite-field anchor
  radical and signs are preserved by a carrier-native numerical equivalence
  theorem.

KILL-NGQ.2 positive-part projection
  A proposal keeps only the positive eigenspace of a presented Gram. Kill it
  unless no non-null finite-field pairing data is changed.

KILL-NGQ.3 GNS completion as square
  A proposal applies a GNS or Hilbert completion to relation data. Kill it
  unless the pairing is constructed by the square carrier first.

KILL-NGQ.4 finite numerical window
  A proposal verifies finite Gram/count windows. Kill it unless ghost
  extensions are excluded carrier-natively.

KILL-NGQ.5 control survival
  A proposal's numerical quotient can be formed on arbitrary control Grams.
  Kill it unless controls die at carrier formation.
```

