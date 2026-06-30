# 197 - ku square / Adams graph shadow does not construct End(S^2/Z)

Status: no-go + chromatic surface-shadow boundary, 2026-06-20. Sixtieth
cycle of the doc-137 construction arc. Doc 196 killed using the ordinary
uncompactified `THH(Z)` diagonal abutment, even with the AA norm-weight
dictionary, as the missing square carrier. This document tests the
stronger height-1 shortcut:

```text
the connective ku square, with its amplitude-2 torsion ladder and Adams
graph HH0 shadow, is already End(S^2/Z).
```

Witness, lead-reran this cycle:
`prime_int_n1b_ku_square_adams_shadow_no_go` (KAS1-KAS10 ALL PASS) --
exact `ku` torsion ladder, positive even-degree surface-like shadow, Adams
HH0 graph counts, p-complete group-like Adams family, missing determinant
scheme/properness/regularized constant, missing full twisted THH, missing
integral structured Adams operations, missing compactified square
cohomology/intersection/correspondence/Frobenius/Rosati data, missing
Laurent boundary/torsor/DD.4 data, and residual R1 carrier-guard checks.

Adjacent witnesses, lead-reran this cycle:
`prime_int_ku_ladder` (ALL PASS) -- the positive first-pass fact that
`THH(ku)` has amplitude 2 and torsion
`|T_{2w}| = lcm(1..w+1)/(w(w+1))`, with Adams graph HH0 shadow
`Z/|k-l|`;
`prime_twisted_adams_ku` (ALL PASS) -- the p-complete Adams-twisted
minimal instance and the group-like/LTE fork that keeps the graph data at
shadow level.

## 1. Purpose

The `ku` square is not another weak analogy. It is the first banked
square-like object with the dimensionality the function-field analogy
demands:

```text
THH(ku) = H0 excess + H1 free odd lattice + H2 even torsion,
|T_{2w}| = lcm(1..w+1)/(w(w+1)).
```

The torsion is in even degree, so the diagonal count pairs with the
positive parity expected of an index surface. The same record also gives a
two-parameter Adams graph shadow:

```text
HH_0(Z[beta]; Z[beta]_(psi^k,psi^l))_w = Z/|k-l|  for w >= 1.
```

This is real surface-shadow evidence. It is also still a shadow. The
determinant scheme for the `ku` torsion ladder is not fixed; the diagonal
constant is not computed; the full Adams-twisted THH correspondence algebra
is not computed; integral structured Adams operations are not constructed;
and the p-complete Adams family is group-like, with bidegree `(1,1)`, not a
function-field Frobenius graph family of bidegrees `(1,q)`.

This document is local. It does not reject a future compactified
chromatic/PFD square or a completed Adams-twisted THH theory with
properness and positive Rosati. It rejects only the shortcut:

```text
connective ku square + Adams HH0 graph shadow = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 197.1 (The ku/Adams surface shadow is not the compactified square).

The connective ku square supplies genuine height-1 square data:

  THH_*(ku) has amplitude 0..2,
  T is even-degree torsion,
  |T_{2w}| = lcm(1..w+1)/(w(w+1)),
  and the pi_*-level Adams graph HH0 shadow gives Z/|k-l| in every
  positive weight.

However, these data do not construct End(S^2/Z). The `ku` diagonal ladder
still has an unfixed determinant/properness scheme, and no regularized
diagonal constant is established. The Adams graph information used here is
HH0/pi_*-level shadow data; the full Adams-twisted THH correspondence
algebra is not computed. The structured Adams family is available
p-completely and group-like; integral structured Adams operations on
connective ku are not constructed, and group-like bidegree `(1,1)` data is
not the function-field Frobenius graph package.

Moreover, no compactified arithmetic square, square H2, intersection form,
correspondence algebra, Frobenius graph, positive Rosati involution,
Laurent boundary map, torsor splitter, or DD.4 weight>=1 datum is
constructed.

Therefore the banked `ku` square / Adams graph shadow cannot itself be
promoted to End(S^2/Z).
```

Verdict label:

```text
N1B_KU_SQUARE_ADAMS_SHADOW__SURFACE_LIKE_SHADOW_NOT_END_S2Z__NO_GO.
```

## 3. Proof

`prime_int_n1b_ku_square_adams_shadow_no_go` verifies the R1 gate, with
`prime_int_ku_ladder` and `prime_twisted_adams_ku` rerun as adjacent
positive witnesses.

KAS1 records the positive `ku` fact: the amplitude-2 `THH(ku)` ladder has
the exact low-degree table

```text
|T_8|=3, |T_10|=2, |T_12|=10, |T_14|=15,
|T_16|=35, |T_18|=28, |T_20|=252,
```

and `w(w+1)` divides `lcm(1..w+1)` in the checked range.

KAS2 records the positive parity: the torsion sits in even degree and
therefore has the right sign for a surface-like diagonal shadow. It also
records the limit: a positive count parity is not an intersection form or
Rosati involution.

KAS3 records the Adams HH0 graph shadow exactly:

```text
gcd_{1 <= i <= w}(k^i-l^i) = |k-l|.
```

This gives `Z/|k-l|` in every positive weight, but only at the HH0/pi_*
shadow level.

KAS4 records the p-complete Adams family: the wild line satisfies the LTE
law `v_p((1+p)^w-1)=1+v_p(w)`. This is useful, but it is a group-like
p-complete family, not integral structured Frobenius graphs of bidegree
`(1,q)`.

KAS5 records the properness/determinant failure: the partial log-counts of
the `ku` torsion ladder grow with the cutoff, the determinant scheme is not
fixed, and no regularized `D_ku(0)` constant is constructed.

KAS6 records that the full Adams-twisted THH correspondence algebra is not
computed. The graph counts are not yet a square End algebra.

KAS7-KAS8 record the carrier failure: no compactified square H2,
intersection form, correspondence algebra, Frobenius graph, positive
Rosati, Laurent boundary, torsor splitter, or DD.4 weight>=1 datum is
constructed.

KAS9 records the exact status of the carrier guard. DH/Epstein cannot form
the `ku` THH shadow because they lack the needed ring/complex-orientation
carrier, but that is only a `ku`-specific guard; it does not construct the
`S^2/Z` square map.

KAS10 records that the base R1 obstructions remain.

## 4. Impact on R1

```text
R1 after docs 138-197:
  NEWLY CLOSED THIS CYCLE:
    - connective ku square / Adams graph HH0 shadow, as End(S^2/Z), square
      H2, intersection form, correspondence algebra, Frobenius graph,
      Laurent boundary data, torsor splitter, DD.4 weight>=1 datum, or
      positive Rosati (doc 197).

  STILL ADMISSIBLE:
    - a compactified chromatic/PFD square whose `ku` surface-like data are
      the associated graded of a proper correspondence theory;
    - a full Adams-twisted THH theory with integral structured operations,
      off-diagonal correspondences, properness/duality, and a positive
      Rosati involution;
    - a carrier-native determinant/properness scheme fixing `D_ku` and
      constructing the square intersection form rather than only its
      diagonal count shadow;
    - a genuinely different carrier whose correspondence algebra is built
      internally.

  STILL OPEN:
    - a genuinely different carrier whose first
      correspondence/multiplication constructs the square data internally
      and finishes DD.4 weights>=1.
```

R1 is still open. The `ku` square is a real and valuable surface-like
shadow, but not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-KAS.1 ku square as End(S^2/Z)
  A proposal identifies the known connective ku square with the compactified
  arithmetic square. Kill it unless it constructs properness, square H2,
  and an intersection form.

KILL-KAS.2 ku torsion ladder as regularized square determinant
  A proposal uses the lcm/(w(w+1)) ladder as a finished diagonal constant.
  Kill it unless the determinant scheme is fixed and the regularized
  constant is constructed carrier-natively.

KILL-KAS.3 Adams HH0 graph shadow as correspondence algebra
  A proposal treats Z/|k-l| HH0 graph counts as End(S^2/Z). Kill it unless
  the full Adams-twisted THH correspondence algebra is computed.

KILL-KAS.4 p-complete Adams family as Frobenius graph package
  A proposal uses the p-complete group-like Adams family as function-field
  Frobenius graph data. Kill it unless it constructs integral structured
  operations and the required bidegree/correspondence package.

KILL-KAS.5 positive even torsion as Rosati positivity
  A proposal treats even-degree positive counts as the positive Rosati.
  Kill it: count parity is a diagonal shadow, not a positive involution on
  a correspondence algebra.

KILL-KAS.6 ku carrier guard as S^2/Z construction
  A proposal says DH/Epstein die because they cannot form ku THH, then
  promotes that to End(S^2/Z). Kill it unless the actual S^2/Z square map
  and its carrier-native control death are constructed.
```

## 6. Board

```text
doc-137 R1, cycle 60 = doc 197:
  N1B_KU_SQUARE_ADAMS_SHADOW__SURFACE_LIKE_SHADOW_NOT_END_S2Z__NO_GO.

What got built: no End object. The value is a boundary theorem: the ku
square / Adams graph shadow is real surface-like evidence, but without a
proper compactified square, full twisted correspondences, integral Adams
operations, and positive Rosati, it is not End(S^2/Z).

What remains: construct a compactified chromatic/PFD square using the ku
data as associated graded; compute full Adams-twisted THH with properness
and off-diagonal correspondences; fix the D_ku determinant/properness
scheme; or return to the in-house PFD/Xbar DD.4 weight>=1 obstruction.
```
