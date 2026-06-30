# 211 - Weight-2 NS square anchor specifies End(S^2/Z)

Status: construction-spec anchor, 2026-06-20. Seventy-fourth cycle of the
doc-137 construction arc. This is not a no-go theorem and is not added to the
no-go bank. It records the function-field square model that the over-Z
construction must reproduce.

Witnesses, lead-reran this cycle:
`prime_int_n1b_ns_square_anchor` (NSA1-NSA6 ALL PASS),
`ns_diagonal_representability` (exit 0), and `ns_hodge_index_duality`
(exit 0).

## 1. Purpose

Doc 210 sharpened the Rosati wall: abstract positivity is not enough unless
the construction also supplies the square carrier, external base-size datum,
Frobenius graph, and off-diagonal correspondence coupling.

This document fixes the target by anchoring it on the place where the square
object is a theorem. For a smooth curve over `F_q`, the Neron-Severi square
of `C x C` supplies exactly the data the zeta-side construction is missing:

```text
rep_NS : Corr(C) -> (Z-lattice, intersection form)
```

The over-Z problem is now sharper: construct the analogue of this
representability functor for the compactified zeta square, not just another
trace, determinant, or FE-symmetric shadow.

## 2. Anchor

For the function-field curve, a correspondence is represented by

```text
Z |-> (d1, z, d2),
```

where `d1` and `d2` are the two fiber degrees and `z` is the action on
`H^1(C)`. The square intersection form is

```text
(d1,z,d2).(e1,w,e2) = d1 e2 + d2 e1 - Tr(z w).
```

The diagonal and Frobenius graph are

```text
Delta = (1, Id, 1),
Gamma_{F^n} = (q^n, F^n, 1).
```

Then

```text
Delta . Gamma_{F^n}
  = q^n + 1 - Tr(F^n)
  = #C(F_{q^n}).
```

The diagonal is not a product class: its `End(H^1)` component is `Id`, while
the fiber/product classes have zero `End(H^1)` component. This is the
indecomposable square correspondence that the static product-surface route
missed.

On the weight-2 primitive part, duality is the Rosati involution

```text
D(z) = z^dag = E^{-1} z^T E,
D^2 = id,
P_NS(z,w) = Tr(z D(w)) = Tr(z w^dag).
```

The primitive Hodge index is the sign of this canonical pairing. It is
negative on-circle and flips off-circle. Thus the finite-field model says
precisely where RH-strength enters: not in the edge determinant alone, but in
the positive Rosati pairing on the square correspondence carrier.

## 3. Witness Gates

`prime_int_n1b_ns_square_anchor` records six gates:

```text
NSA1 rep_NS diagonal/Frobenius graph reproduces point counts.
NSA2 Delta is indecomposable; product/fiber classes are not.
NSA3 Primitive weight-2 Hodge index flips off circle.
NSA4 Weight-2 duality is involutive and its pairing is canonical.
NSA5 DH has no typed NS square anchor.
NSA6 This is only an anchor/spec; it does not construct End(S^2/Z).
```

The adjacent witnesses supply the two longer anchors:
`ns_diagonal_representability` for the `rep_NS` form and Lefschetz
intersection formula, and `ns_hodge_index_duality` for the weight-2 duality
pairing.

## 4. Impact on R1

```text
R1 after docs 138-211:
  POSITIVE ANCHOR THIS CYCLE:
    - the exact square object to reproduce is rep_NS, not a product surface,
      determinant, local factor, abstract AV, or FE reflection;
    - the required diagonal is indecomposable, with a nonzero End(H^1)
      component;
    - the required graph is a Frobenius/Hecke graph whose intersection with
      the diagonal gives the explicit-formula count/trace;
    - the required positivity is the canonical weight-2 Rosati duality
      pairing, not an inserted metric.

  STILL ADMISSIBLE:
    - a zeta-native construction of rep_NS on a compactified square;
    - a non-product correspondence algebra with an indecomposable diagonal;
    - a Frobenius/Hecke graph whose diagonal intersection gives the
      explicit-formula trace and kills DH at carrier formation;
    - a positive Rosati pairing on that constructed square carrier.

  STILL OPEN:
    - construct this over Z. The function-field anchor specifies the object;
      it does not supply the compactified zeta square.
```

This improves the search discipline. Future proposals must either build the
six displayed pieces or explain which one is impossible. A trace, determinant,
compactness condition, local purity datum, or abstract positivity theorem that
does not construct `rep_NS`, the indecomposable diagonal, the graph, and the
canonical Rosati pairing is not addressing the remaining problem.

R1 is still open. R2 remains locked.

## 5. Board

```text
doc-137 R1, cycle 74 = doc 211:
  construction-spec anchor, not a no-go theorem.

What got built: no End object over Z. The value is a verified finite-field
square specification: rep_NS, diagonal, Frobenius graph, intersection form,
duality, and Rosati/Hodge-index flip.

What remains: construct the global zeta-side square carrier; construct
rep_NS over Z; construct the indecomposable diagonal and Frobenius/Hecke
graph; construct the square intersection form from Euler/Satake products;
construct the canonical positive Rosati pairing; solve DD.4 weights>=1 and
square-side iota/properness; kill DH/Epstein at carrier formation.
```
