# 202 - Archimedean family without finite residue field does not construct End(S^2/Z)

Status: no-go + family/special-fiber residue boundary, 2026-06-20.
Sixty-fifth cycle of the doc-137 construction arc. Doc 201 killed the
static product surface: nonzero monodromy `N` belongs to a degenerating
family with special fiber, not to a smooth static product. This document
tests the next surviving carrier-shaped repair:

```text
archimedean degenerating family + nearby-cycle N + M(N)=W
  = End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_archimedean_family_no_go` (ADF1-ADF7 ALL PASS) -- the
archimedean degeneration has nearby-cycle `N` and `M(N)=W`; over finite
fields a special fiber has finite residue cardinality `|kappa(t=0)|=q`
and hence marks radii `q^{w/2}`; at infinity the special fiber has
residue field `C`, no finite `q`, no Frobenius/base-size marker, and no
radius marking; the scaling-site, length-edge, and Bost-Connes suppliers
fail the finite-`kappa` type check; DH dies before any family/special-fiber
question; and no square/Rosati/R1 data is built.

Adjacent witnesses, lead-reran this cycle:
`archimedean_degenerating_family` (exit 0) -- the family and Schmid
nearby-cycle data are real, but the archimedean special fiber has
continuum residue field and unmarked radius;
`residue_field_cardinality` (exit 0) -- finite closed-point cardinality is
a constant-field datum, while the F1 suppliers provide continuum, length,
or discrete-index data rather than finite `|kappa|`.

## 1. Purpose

Doc 201 left the family carrier as the honest next surface-shaped route.
This is a real improvement over the static product surface. The family is
not missing: at the archimedean place a degeneration over a complex disk
has local monodromy, and Schmid supplies nearby-cycle `N` and the
monodromy filtration `M(N)=W`.

The issue is that `N` and `M(N)=W` are not the radius/base-size datum.
They provide a nilpotent and an integer weight grading. Over a finite
field, weight becomes radius only after the closed point of the base has a
finite residue field:

```text
|kappa(t=0)| = q,
radius on weight w = q^{w/2}.
```

At the archimedean place the base is a complex disk, so the closed point
has residue field `C`. That gives no finite `q`, no Frobenius of a finite
field, and no carrier-native base size. The Schmid grading remains an
integer grading; it is not a marked finite-field radius.

This document is local. It does not reject a future family carrier that
constructs a carrier-native finite constant/residue-field datum at the
archimedean special fiber. It rejects only the shortcut:

```text
archimedean family/N/M(N)=W, with kappa(t=0)=C, already constructs
End(S^2/Z).
```

## 2. Lemma

```text
Lemma 202.1 (The archimedean family lacks the finite residue-field marker).

For a degenerating family over a finite field, the closed point t=0 has
finite residue field F_q. The base size q is the datum that marks radii
q^{w/2} on weight-w graded pieces.

For the archimedean degenerating family, Schmid supplies nearby-cycle N
and M(N)=W over a complex disk. However, the closed point t=0 has residue
field C. Thus the family has no finite residue cardinality |kappa|=q, no
finite-field Frobenius, and no carrier-native base-size marker converting
the integer weight grading into q^{w/2}.

The scaling-site, length-edge, and Bost-Connes suppliers do not repair this
gap: they supply continuum, length, or discrete-index data, not a finite
constant/residue-field cardinality.

Consequently the archimedean family data constructs no square-side
iota/properness theorem, square H2, intersection form, correspondence
algebra, Frobenius graph, Laurent boundary data, torsor splitter, DD.4
weight>=1 datum, or positive Rosati involution.

Therefore archimedean family/N/M(N)=W data with kappa(t=0)=C cannot itself
be promoted to End(S^2/Z).
```

Verdict label:

```text
N1B_ARCHIMEDEAN_FAMILY__NO_FINITE_RESIDUE_FIELD_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_archimedean_family_no_go` verifies the R1 gate, with
`archimedean_degenerating_family` and `residue_field_cardinality` rerun as
adjacent witnesses.

ADF1 records the positive fact: the nearby-cycle `N` exists and `M(N)=W`
is a symmetric split. This is not the failure.

ADF2 records the finite-field comparison. For `q=4,9,25`, the finite
residue field at the closed point marks radii `2,3,5` on weight 1.

ADF3 records the archimedean special fiber. The closed point has
`kappa(t=0)=C`, the residue field is not finite, there is no Frobenius, and
the radius is unmarked even though `N` and `M(N)=W` are present.

ADF4 records the constant-field reading: finite closed-point cardinality is
inherited from the finite constant field under the family.

ADF5 records the F1 supplier type check. The scaling site supplies a
continuum, the length edge supplies real lengths, and Bost-Connes supplies
a discrete multiplicative index whose q->1 limit deletes the constant-field
cardinality. None is a finite `|kappa|`.

ADF6 records DH-vacuity: the control has no `H1`, no surface, no family,
no special fiber, and no closed point whose cardinality can be asked.

ADF7 records the carrier failure: no carrier-native finite special fiber,
constant field, finite residue cardinality, Frobenius/base-size marker,
square-side `iota`/properness, square H2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent boundary,
torsor splitter, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-202:
  NEWLY CLOSED THIS CYCLE:
    - archimedean degenerating family / nearby-cycle N / M(N)=W /
      continuum special fiber as End(S^2/Z), finite residue-field
      cardinality, Frobenius/base size, square-side iota/properness, square
      H2/intersection form, Laurent boundary data, torsor splitter, DD.4
      weight>=1 datum, or positive Rosati (doc 202).

  STILL ADMISSIBLE:
    - a family carrier whose special fiber constructs a carrier-native
      finite constant/residue-field cardinality at the archimedean place;
    - a non-product compactified square whose middle correspondence is
      indecomposable rather than Kunneth-factored;
    - a square-side iota/properness theorem that makes the correspondence
      algebra global rather than one-place-tensored;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The family/N/M(N)=W half is real and useful, but it is
not enough: the next admissible family route must construct the finite
constant/residue-field marker carrier-natively. R2 remains locked.

## 5. Kill Conditions

```text
KILL-ADF.1 archimedean family/N/M(N)=W as End(S^2/Z)
  A proposal identifies the Schmid nearby-cycle family data with the
  compactified square correspondence algebra. Kill it unless it also
  constructs the finite residue/base-size datum and square correspondences.

KILL-ADF.2 integer weight grading as finite-field radius
  A proposal treats M(N)=W as the radius q^{w/2}. Kill it: M(N)=W gives an
  integer grading; the radius needs finite |kappa|=q and Frobenius.

KILL-ADF.3 continuum residue field C as finite q
  A proposal uses kappa(t=0)=C at infinity as the finite base size. Kill it:
  C is infinite, characteristic 0, and has no finite-field Frobenius.

KILL-ADF.4 scaling/length/Bost-Connes supplier as finite kappa
  A proposal uses the scaling continuum, log p length edge, or N^x
  discreteness as |kappa|. Kill it unless it constructs a finite
  constant/residue-field cardinality rather than continuum/length/index data.

KILL-ADF.5 finite-field analogy without carrier-native constant field
  A proposal copies the finite-field family picture to infinity but does
  not construct the finite constant field under the family. Kill it.

KILL-ADF.6 DH-vacuity as zeta correspondence construction
  A proposal notes DH has no family/special fiber and promotes that to
  End(S^2/Z). Kill it unless the zeta-side square maps, correspondences,
  finite base-size marker, and Rosati are actually constructed.
```

## 6. Board

```text
doc-137 R1, cycle 65 = doc 202:
  N1B_ARCHIMEDEAN_FAMILY__NO_FINITE_RESIDUE_FIELD_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
the archimedean family and nearby-cycle N exist, but the special fiber has
continuum residue field rather than finite |kappa|=q, so the weight
grading is not radius-marked.

What remains: construct a family carrier with carrier-native finite
constant/residue-field cardinality at the archimedean special fiber;
construct an indecomposable compactified square correspondence; solve
square-side iota/properness; or return to the in-house PFD/Xbar DD.4
weight>=1 obstruction.
```
