# 203 - Named F1 constant towers do not construct End(S^2/Z)

Status: no-go + finite-constant-field boundary, 2026-06-20. Sixty-sixth
cycle of the doc-137 construction arc. Doc 202 killed promoting the
archimedean family / nearby-cycle `N` / `M(N)=W` itself to `End(S^2/Z)`:
the missing datum is a carrier-native finite constant/residue-field marker
at the archimedean special fiber. This document tests the direct repair:

```text
named F1 constant-field object
  = finite base size q at infinity
  = End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_f1_constant_tower_no_go` (CFT1-CFT7 ALL PASS) -- finite
fields have finite constant field `F_q`, finite roots of unity, and marked
radii; the cyclotomic F1 tower has finite levels but infinite colimit
`mu_infinity = Q/Z`; Borger/Witt ghosts form an infinite indexed product
with one Frobenius per prime rather than one finite-field Frobenius; the
Connes-Consani/Arakelov archimedean component has residue field `R` or `C`;
the named F1 tower decision supplies no finite `q`; DH has no
constant-field slot; and no square/Rosati/R1 data is built.

Adjacent witness, lead-reran this cycle:
`constant_field_tower` (exit 0) -- the older R9 type check: every named F1
constant object is infinite, so the doc-202 finite-residue obstruction
recurs at the named candidate level.

## 1. Purpose

Doc 202 left a precise opening: a future family route must construct a
finite constant/residue-field cardinality at the archimedean special
fiber. The obvious next repair is to use one of the named F1 constant
objects that are supposed to play the role of constants for `Spec Z`:

```text
cyclotomic tower mu_infinity / F_{1^n},
Borger Lambda-ring / big-Witt ghosts,
Connes-Consani/Arakelov archimedean component.
```

This is a real test, not a semantic objection. Over `F_q`, the finite
constant field has cardinality `q`, and that finite `q` is the datum that
marks radii `q^{w/2}`. The question is whether any named F1 constant
object supplies an actual finite cardinality at infinity.

The answer tested here is no. The named objects are meaningful, but their
sizes are infinite: a countable colimit, an infinite product, or a
continuum. They do not supply the single finite base size `q` required by
the finite-field analogy, and they do not construct the square
correspondence/Rosati data.

This document is local. It does not prove that no future F1 geometry can
manufacture a finite base size. It rejects only the shortcut:

```text
mu_infinity / Witt ghosts / Arakelov infinity = finite constant field q
at the archimedean special fiber.
```

## 2. Lemma

```text
Lemma 203.1 (Named F1 constant objects are not finite constant fields).

Over a finite field, the constant field F_q is finite, its roots of unity
form the finite group mu_{q-1}, and the base size q marks radii q^{w/2}.

The cyclotomic F1 tower has finite levels mu_n, but the F1 constant object
is the colimit mu_infinity = Q/Z, which is countably infinite. No finite
level is selected as the constant field without reintroducing an external
finite q.

The Borger Lambda-ring / big-Witt ghost structure is an infinite indexed
product with one Frobenius lift per prime. It is not a single finite field
with one Frobenius and one cardinality q.

The Connes-Consani/Arakelov archimedean component has residue field R or C,
a characteristic-zero continuum, and supplies metric archimedean data rather
than a finite field of constants.

Consequently these named F1 constant objects construct no finite base-size
marker, square-side iota/properness theorem, square H2, intersection form,
correspondence algebra, Frobenius graph, Laurent boundary data, torsor
splitter, DD.4 weight>=1 datum, or positive Rosati involution.

Therefore the named F1 constant-field towers cannot themselves be promoted
to End(S^2/Z).
```

Verdict label:

```text
N1B_F1_CONSTANT_TOWER__INFINITE_CONSTANTS_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_f1_constant_tower_no_go` verifies the R1 gate, with
`constant_field_tower` rerun as the adjacent witness.

CFT1 records the finite-field anchor. For `q=4,9,25`, the constant fields
are finite, `|mu_{q-1}|=3,8,24`, and the radii are marked by `q`.

CFT2 records the cyclotomic tower failure. Each finite level `mu_n` is
finite, but the actual F1 constant object is the full colimit
`mu_infinity = Q/Z`, which is countably infinite. Selecting a finite level
would spend the finite `q` that the construction is supposed to produce.

CFT3 records the Witt ghost failure. The ghost structure is an infinite
indexed product with one Frobenius lift per prime, the opposite of a single
finite constant field with one Frobenius and one cardinality.

CFT4 records the Arakelov failure. The archimedean component has residue
field `R` or `C`, hence continuum cardinality, and supplies metric
archimedean structure rather than finite constants.

CFT5 records the combined decision: no named F1 tower furnishes a finite
constant-field `q`, and the earlier finite-`kappa` type check remains
negative.

CFT6 records DH-vacuity: the control has no closed point and no
constant-field slot whose cardinality can be asked.

CFT7 records the carrier failure: no finite constant/residue field,
single Frobenius/base-size marker, finite `q` truncation, family special
fiber, square-side `iota`/properness, square H2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati, Laurent boundary,
torsor splitter, or DD.4 weight>=1 datum is constructed.

## 4. Impact on R1

```text
R1 after docs 138-203:
  NEWLY CLOSED THIS CYCLE:
    - named F1 constant-field towers / mu_infinity / Borger-Witt ghosts /
      Connes-Consani-Arakelov archimedean component as End(S^2/Z), finite
      constant field at infinity, finite residue-field cardinality,
      Frobenius/base size, square-side iota/properness, square
      H2/intersection form, Laurent boundary data, torsor splitter, DD.4
      weight>=1 datum, or positive Rosati (doc 203).

  STILL ADMISSIBLE:
    - a future F1 or family construction that manufactures a finite
      constant/residue-field cardinality at the archimedean place without
      selecting a finite level externally;
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

R1 is still open. The named F1 constant towers are useful as a failure
mode: they show that the "field of constants" exists as an F1 object, but
not as the finite `q` required by the radius marker. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CFT.1 mu_infinity as finite constant field
  A proposal identifies the cyclotomic tower or mu_infinity with the finite
  base size q. Kill it unless it constructs a finite q carrier-natively
  rather than selecting a finite level by hand.

KILL-CFT.2 finite level mu_n as constructed q
  A proposal truncates the cyclotomic tower at a finite n. Kill it unless
  the carrier itself selects n as a constant-field cardinality.

KILL-CFT.3 Witt ghosts as one finite-field Frobenius
  A proposal uses Lambda-ring or big-Witt ghost data as the finite q. Kill
  it unless it collapses the infinite one-Frobenius-per-prime product to a
  carrier-native single finite-field Frobenius and cardinality.

KILL-CFT.4 Arakelov R/C as finite constants
  A proposal uses the archimedean completion or metric component as finite
  constants. Kill it: R/C is a characteristic-zero continuum, not finite q.

KILL-CFT.5 named F1 constants as End(S^2/Z)
  A proposal promotes any named F1 constant object directly to the square
  correspondence algebra. Kill it unless it also constructs square H2,
  intersection form, correspondences, Frobenius graph, and Rosati.

KILL-CFT.6 DH-vacuity as zeta correspondence construction
  A proposal notes DH has no constant-field slot and promotes that to
  End(S^2/Z). Kill it unless the zeta-side finite q and square maps are
  actually constructed.
```

## 6. Board

```text
doc-137 R1, cycle 66 = doc 203:
  N1B_F1_CONSTANT_TOWER__INFINITE_CONSTANTS_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a sharper boundary theorem:
the named F1 constant objects are infinite, so they do not supply the finite
base size q required after doc 202.

What remains: construct a family/F1 carrier with carrier-native finite
constant/residue-field cardinality at the archimedean special fiber;
construct an indecomposable compactified square correspondence; solve
square-side iota/properness; or return to the in-house PFD/Xbar DD.4
weight>=1 obstruction.
```
