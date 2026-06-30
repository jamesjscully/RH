# 187 - CC Pic/Jacobian curve data does not construct the square

Status: no-go + CC Pic/Jacobian-to-square repair deletion, 2026-06-20.
Fiftieth cycle of the doc-137 construction arc. Doc 186 killed the
appended-Hitchin Picard/Prym/Jacobian repair, but explicitly left open a
carrier-native Pic/Jacobian route. This document tests the strongest
available such escape in the local record: the Connes-Consani compactified
Spec Z curve-level theory, including integer Riemann-Roch, Pontryagin-Serre
duality, and the 2026 Pic/Jacobian infrastructure.

Witness, lead-reran this cycle:
`prime_int_n1b_cc_pic_jacobian_square_no_go` (CPJ1-CPJ10 ALL PASS) -- exact
curve-level genus/canonical-class transcription, rank-one Pic tensor product,
missing square structures, the strict Gamma-set square noncollapse example,
published-probe diagonal factorization, missing Frobenius graph/Rosati data,
missing Laurent/boundary/torsor data, residual R1 obstruction checks, and
carrier-guard checks.

## 1. Purpose

After doc 186, the surviving Pic/Jacobian claim can say:

```text
Do not append an external Hitchin fiber.
Use the actual compactified Spec Z Pic/Jacobian theory.
That is carrier-native curve-level geometry.
```

The premise is important and true at curve level. The Connes-Consani package
is not being dismissed. It gives a real compactified Spec Z curve-level
Riemann-Roch/Pontryagin-Serre/Pic-Jacobian package in the project record.

The test is whether that package already supplies the self-product
correspondence algebra:

```text
End(S^2/Z) = compactified square + H^2/intersection form +
correspondences/Frobenius graphs + positive Rosati.
```

It does not. The curve-level Pic/Jacobian product is an internal tensor
product of rank-one objects on one curve. The published curve-level machinery
does not define the compactified square, square H^2, an intersection form,
or the correspondence algebra. The strict Gamma-set square contains
object-level extra data, but the published EM/RR/Pic/Hom probes factor
through the diagonal curve shadow. The 2026 idelic translation picture is not
the function-field Frobenius graph package on C x C.

This document is local. It does not reject a future Connes-Consani square, a
tolerant derived square, or an arithmetic correspondence algebra built from
the compactified Spec Z theory. It rejects only the promotion:

```text
curve-level Pic/Jacobian data = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 187.1 (CC curve-level Pic/Jacobian data is not the compactified
square).

In the local CC record:

  - RR over S exists at curve level, with genus 0 and deg_2(K) = -2.
  - Pontryagin-Serre duality exists over S[+-1].
  - arithmetic Pic and Jac infrastructure exists at curve level.

The Pic tensor product is internal to one curve:

  rank-one tensor rank = 1 x 1 = 1.

The demanded square structures are not supplied by this package:

  - external product of two compactified geometries;
  - square cohomology H^0, H^1, H^2;
  - square H^2/intersection form;
  - correspondence algebra;
  - Frobenius graph correspondence;
  - positive Rosati involution.

The strict Gamma-set square is not empty: it has object-level extra data.
For the two square classes

  L  = ((1,1),(1,1), edges (1,1),(1,2),(2,1)),
  C3 = ((3),(1), edge (1,1)),

the diagonal total is the same:

  mu(L) = mu(C3) = 3,

but the divided-power invariant separates them:

  Phi'_2(L) = 1,  Phi'_2(C3) = 0.

However, the published CC RR/Pic/Hom probes are EM/abelian-valued or
short-complex curve-level probes. In the local Q/N analysis they factor
through the diagonal shadow. Their best-effort square output is the curve
shadow:

  pi_1 = 0,  pi_0 = Z.

Thus the current CC curve-level Pic/Jacobian package is not a construction of
End(S^2/Z). A surviving CC route must build an actual compactified square and
then construct its H^2/intersection pairing, correspondence algebra,
Frobenius graph or replacement correspondence, positive Rosati involution,
Laurent/boundary/torsor data, and DH/Epstein death at that square map.
```

Verdict label:

```text
N1B_CC_PIC_JACOBIAN_CURVE_LEVEL__REAL_THEOREM_NOT_COMPACTIFIED_SQUARE_OR_ROSATI__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_pic_jacobian_square_no_go` verifies the local split.

CPJ1 records the real curve-level input:

```text
RR over S;
Serre duality over S[+-1];
Pic/Jac infrastructure;
genus = 0;
deg_2(K) = -2.
```

CPJ2 records that the Pic tensor product is internal curve product:

```text
rank-one tensor rank = 1.
```

That is line-bundle multiplication on one curve, not the external
self-product geometry.

CPJ3 records that the compactified square structures demanded by
End(S^2/Z) are not supplied: no external product geometry, no H^2, no
intersection form, and no correspondence algebra.

CPJ4 records the strict square noncollapse from the Q/N analysis:

```text
mu(L)=mu(C3)=3, but Phi'_2(L)=1 and Phi'_2(C3)=0.
```

So the square has object-level information beyond the diagonal.

CPJ5 records the obstruction at the published-probe level: EM-visible
RR/Pic/Hom probes factor through the diagonal curve shadow. This means the
published curve-level machinery does not extract the square's extra
object-level data as cohomology, dimension, duality, or intersection theory.

CPJ6 records that the idelic translation picture is not the Frobenius graph
correspondence package on a square and does not define the positive Rosati
involution.

CPJ7-CPJ8 record that no Laurent axis, boundary map, torsor splitter, or
weight>=1 DD.4 datum is constructed; the base R1 obstructions are untouched.

CPJ9 records the carrier guard: no carrier-consuming square correspondence
map has been produced at which DH/Epstein die.

CPJ10 is the verdict: CC Pic/Jacobian curve-level data is a real theorem, but
it is not the self-product correspondence algebra.

## 4. Impact on R1

```text
R1 after docs 138-187:
  NEWLY CLOSED THIS CYCLE:
    - promoting the Connes-Consani curve-level Pic/Jacobian package itself
      to End(S^2/Z), the compactified square correspondence algebra, or the
      positive Rosati involution (doc 187).

  STILL ADMISSIBLE:
    - a future CC-derived compactified square theory that actually constructs
      H^2, intersection, correspondences, a Frobenius replacement graph,
      positive Rosati, Laurent boundary data, and DH/Epstein death.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs the square data internally and finishes DD.4 weights>=1.
```

R1 is still open. The CC curve-level theorem is valuable input, not the
target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CPJ.1 curve-level Pic/Jacobian as End(S^2/Z)
  A proposal identifies Connes-Consani curve-level Pic/Jacobian data with the
  self-product correspondence algebra. Kill it unless it constructs the
  compactified square.

KILL-CPJ.2 Pic tensor product as square product
  A proposal uses line-bundle tensor product on one curve as the external
  product/intersection theory of the square. Rank-one tensor remains
  rank-one internal curve product.

KILL-CPJ.3 strict square object data without square cohomology
  A proposal points to the strict Gamma-set square's extra object-level data
  but supplies no H^2, dimension, duality, or intersection theory extracting
  it. Object-level noncollapse is not yet End(S^2/Z).

KILL-CPJ.4 EM-visible diagonal shadow as correspondence algebra
  A proposal uses a published CC RR/Pic/Hom probe that factors through the
  diagonal. The output is curve shadow data, not square correspondences.

KILL-CPJ.5 idelic translations as Frobenius/Rosati
  A proposal reads idele-class translations on Pic/Jacobian as the
  function-field Frobenius graph package. This is not a positive Rosati
  involution on square correspondences.

KILL-CPJ.6 no carrier-consuming square map
  A proposal gives no square correspondence map at which DH/Epstein die and
  no Laurent axis, boundary map, or torsor splitter. This is not construction
  grade.
```

## 6. Board

```text
doc-137 R1, cycle 50 = doc 187:
  N1B_CC_PIC_JACOBIAN_CURVE_LEVEL__REAL_THEOREM_NOT_COMPACTIFIED_SQUARE_OR_ROSATI__NO_GO.

What got built: no new End object. The value is a deletion: curve-level
CC Pic/Jacobian data cannot be promoted to End(S^2/Z).

What remains: build the compactified square itself, or return to the
in-house PFD/Xbar DD.4 weight>=1 obstruction. Curve-level RR/Pic/Jac is
input, not the self-product correspondence algebra.
```
