# 220 - Formal adjoint/projection data does not construct positive Rosati

Status: no-go + formal-adjoint boundary, 2026-06-20. Eighty-third cycle of
the doc-137 construction arc. Doc 219 killed componentwise composition on
formal triples as a square carrier. This document tests the next repair: add
a transpose/Rosati adjoint and read the result as a `*`-correspondence
calculus.

```text
formal NS envelope + componentwise composition
  -> add dagger(d1,z,d2)=(d2,z^dag,d1)
  -> anti-involution and graph transpose
  -> projection formula / positive Rosati correspondence algebra
  -> End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_formal_adjoint_projection_no_go` (FAP1-FAP6 ALL PASS) --
the genuine finite-field graph has the expected formal transpose
`Gamma_F^dag=(1,qF^{-1},q)` and anti-involution; the same formal adjoint
wraps off-circle q-similitudes while positivity fails; the adjoint from a
chosen pairing does not tie an external degree character to graph self-degree;
the pasted intersection form plus componentwise composition lacks the
correspondence projection identity; the same package is formable on controls;
and no square package over `Z` is built.

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_formal_correspondence_composition_no_go` (FCC1-FCC6 ALL PASS)
and `prime_int_n1b_integral_qsim_graph_no_go` (IQG1-IQG6 ALL PASS).

## 1. Purpose

Doc 219 says that the formal law

```text
(d1,z,d2) o (e1,w,e2) = (d1 e1, z w, d2 e2)
```

is symbolic multiplication, not fiber-product composition. The next repair is
to add a transpose/Rosati operation. Given an external pairing `E`, define

```text
z^dag = E^{-1} z^T E,
dagger(d1,z,d2) = (d2,z^dag,d1).
```

For a genuine finite-field Frobenius graph this gives the expected pattern:

```text
Gamma_F=(q,F,1),
Gamma_F^dag=(1,qF^{-1},q).
```

That is a necessary finite-field shadow, not construction of the square over
`Z`. The operation depends on the chosen pairing `E`; it remains available for
off-circle q-similitude data and arbitrary controls; and the formal
composition/intersection package still does not satisfy the projection formula
expected of proper correspondences.

This document rejects only the shortcut:

```text
formal triples + componentwise composition + formal dagger construct the
positive Rosati correspondence algebra required by End(S^2/Z).
```

## 2. Lemma

```text
Lemma 220.1 (Formal adjoints are not positive Rosati carriers).

Given any operator F, scalar q, and chosen alternating form E, define formal
triples, componentwise composition, and dagger by

    (d1,z,d2) o (e1,w,e2) = (d1 e1, z w, d2 e2),
    dagger(d1,z,d2) = (d2, E^{-1} z^T E, d1).

If F^T E F=qE, then dagger(Gamma_F)=(1,qF^{-1},q), dagger^2=id, and dagger
is an anti-automorphism for the symbolic composition law.

These identities do not construct a square carrier. The same identities hold
for off-circle q-similitude data with wrong primitive Hodge sign. If F has
self-degree q0 but the formal graph family is assigned an unrelated external
degree q, then the E-adjoint gives q0 F^{-1}, not q F^{-1}; the formal graph
law still holds because q was inserted as a degree character.

Moreover, the pasted NS pairing together with componentwise composition does
not supply the correspondence projection identity

    <A o B, C> = <B, A^dag o C>.

The defect is nonzero even on the genuine finite-field block when one uses the
formal componentwise law rather than actual proper correspondence composition.
Thus formal dagger supplies an anti-involution on symbols, not the geometric
projection calculus of a square.

The same formal adjoint/projection package is formable on arbitrary control
matrices without Euler product, Satake parameters, rep_NS, square properness,
or carrier-native positivity.

Consequently formal adjoint data constructs no rep_NS, actual square,
fiber-product correspondence composition, carrier-native pairing, projection
formula, degree character, Frobenius graph, off-diagonal intersections,
positive Rosati, DH/Epstein death, DD.4 weight>=1 datum, or End(S^2/Z).

Therefore adding a formal adjoint to the formal NS/composition envelope cannot
itself be promoted to the square correspondence carrier.
```

Verdict label:

```text
N1B_FORMAL_ADJOINT_PROJECTION__ANTI_INVOLUTION_NOT_ROSATI_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_formal_adjoint_projection_no_go` verifies the six gates.

FAP1 records the finite-field anchor. For `q=7`, `a=1`, the formal dagger
satisfies

```text
Gamma_F^dag = (1,qF^{-1},q),
dagger^2 = id,
dagger(A o B) = dagger(B) o dagger(A).
```

The measured defects are all zero. This is the necessary finite-field
transpose pattern.

FAP2 records the off-circle failure. For the integral `q=2`, `a=3` graph,
formal dagger, anti-involution, and exact q-similitude all hold, while the
primitive Hodge index is

```text
H = +0.500.
```

Thus the formal adjoint has not constructed positivity.

FAP3 records degree-character incompatibility. A graph with self-degree `5`
can be placed in a formal graph family with external degree character `7^n`.
The graph law still has zero defect, but the adjoint from the actual pairing
gives `5F^{-1}`, not `7F^{-1}`. The measured mismatch between the pairing
adjoint and forced external transpose is

```text
2.191.
```

Thus formal adjoint data does not construct the external base size or degree
maps.

FAP4 records the projection-formula gap. The formal adjoint is an
anti-involution, but the pasted intersection form and componentwise
composition do not satisfy

```text
<A o B, C> = <B, A^dag o C>.
```

On the genuine finite-field block the sampled projection defects are

```text
27, 27, 27.
```

This is the exact distinction between symbolic composition and proper
correspondence calculus.

FAP5 records control formability. The untyped determinant-`3` control matrix

```text
[[1,2],[1,5]]
```

has exact q-similitude and formal anti-involution, while the same
projection-formula defect appears:

```text
144.
```

It has no Euler product, Satake parameters, `rep_NS`, square properness, or
positive Rosati.

FAP6 records the construction failure: no `rep_NS`, actual square,
fiber-product composition, carrier-native pairing, projection formula,
degree character, Frobenius graph, off-diagonal intersections, positive
Rosati, control death, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-220:
  NEWLY CLOSED THIS CYCLE:
    - formal transpose/Rosati adjoint on triples as positive Rosati,
      anti-involution on the componentwise triple monoid as correspondence
      calculus, assigned graph transpose as degree construction, and
      formal adjoint/projection packages as DH/Epstein guard (doc 220).

  STILL ADMISSIBLE:
    - a zeta-native square carrier whose adjoint is induced by constructed
      proper correspondences and a carrier-native pairing;
    - a projection formula proved from actual fiber-product composition;
    - degree maps and graph transpose tied by the same square carrier;
    - a positive Rosati theorem on the constructed off-diagonal intersection
      form, with controls killed before formal adjoints can be assigned.

  STILL OPEN:
    - construct rep_NS over Z with an actual square carrier, genuine
      correspondence composition, carrier-native degree maps, canonical
      pairing and projection formula, off-diagonal intersection form,
      positive Rosati, DD.4 weight>=1 data, and square-side properness.
```

R1 remains open. This cycle closes the formal-adjoint repair of the formal NS
envelope: a `*` operation on symbols is not the positive Rosati correspondence
carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FAP.1 formal dagger as Rosati
  A proposal defines dagger(d1,z,d2)=(d2,z^dag,d1) on a formal envelope. Kill
  it unless the adjoint and pairing are constructed by the square carrier.

KILL-FAP.2 anti-involution as correspondence calculus
  A proposal verifies dagger(A o B)=dagger(B)o dagger(A) for componentwise
  composition. Kill it unless the composition is actual fiber-product
  correspondence composition.

KILL-FAP.3 assigned transpose degree
  A proposal sets Gamma_F^dag=(1,qF^{-1},q). Kill it unless q, the degree maps,
  and the graph transpose are tied by carrier-native self-degree data.

KILL-FAP.4 projection formula by assertion
  A proposal invokes <A o B,C>=<B,A^dag o C>. Kill it unless the identity is
  proved from the constructed pairing and proper correspondence composition.

KILL-FAP.5 off-circle/control survival
  A proposal's adjoint package can be formed on off-circle q-similitudes or
  arbitrary determinant-q controls. Kill it unless it also constructs
  positivity and kills controls at carrier formation.
```

