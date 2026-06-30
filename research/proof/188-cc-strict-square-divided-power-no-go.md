# 188 - Strict-square divided-power data does not construct End(S^2/Z)

Status: no-go + CC strict-square divided-power carrier deletion,
2026-06-20. Fifty-first cycle of the doc-137 construction arc. Doc 187
killed promoting the Connes-Consani curve-level Pic/Jacobian theorem itself
to the square. This document tests the sharper repair: use the strict
Gamma-set square HZ ^ HZ directly, especially its divided-power and universal
character invariants, as the missing carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_cc_strict_square_divided_power_no_go` (CSD1-CSD10 ALL PASS)
-- exact diagonal-fiber separation, bilinear factorization memory, zero-fiber
split, universal character overproduction, monoid-ring convolution,
published-probe diagonal factorization, missing grading/Bokstedt dictionary,
missing H^2/intersection/correspondence/Frobenius/Rosati data, missing
Laurent/boundary/torsor data, residual R1 obstruction checks, and
carrier-guard checks.

## 1. Purpose

Doc 187 left one honest positive residue:

```text
The strict Gamma-set square is not empty or collapsed.
It remembers bilinear factorization data.
```

The local Q/V record makes this precise. HZ ^ HZ has object-level
divided-power invariants Phi_p and Phi'_p, and a universal character
invariant chi_col. That is real square-only data.

The repair tested here says:

```text
Use those strict-square invariants themselves as End(S^2/Z).
```

This still fails. The invariants are ungraded diagnostic functions on the
strict object. They do not supply square cohomology H^2, an intersection
form, a correspondence algebra, a Frobenius graph, a positive Rosati
involution, a Laurent axis, a boundary map, or a torsor splitter. Published
CC RR/Pic/Hom probes still factor through the diagonal curve shadow.

This document does not reject a future square functor that extracts the
strict-square data as cohomology or intersection theory. It rejects only the
promotion:

```text
strict-square divided-power noncollapse = End(S^2/Z).
```

## 2. Lemma

```text
Lemma 188.1 (strict-square divided-power data is diagnostic, not the
End(S^2/Z) correspondence algebra).

In the strict Gamma-set square HZ ^ HZ, the diagonal map

  mu : HZ ^ HZ -> HZ

is not injective at 1_+. For the classes

  L  = ((1,1),(1,1), edges (1,1),(1,2),(2,1)),
  C3 = ((3),(1), edge (1,1)),

one has

  mu(L) = mu(C3) = 3,
  Phi'_2(L) = 1,
  Phi'_2(C3) = 0.

The strict square also remembers bilinear factorization. For

  F22 = ((2),(2), edge (1,1)),
  F41 = ((4),(1), edge (1,1)),

one has

  mu(F22) = mu(F41) = 4,
  Phi_3(F22) = 0,
  Phi_3(F41) = 1.

Even the zero fiber can split from the basepoint shadow: a class with
column character

  chi_col = 2[1] - [2]

has diagonal total zero.

The universal character data overproduces invariant axes:

  chi_col(L)   = [1] + [2],
  chi_col(C3)  = [3],
  chi_col(F22) = 2[2],
  chi_col(F41) = [4].

Its product is monoid-ring convolution on nonzero integers:

  chi_col(x*y) = chi_col(x) * chi_col(y).

This is genuine object-level square data. But the package has no grading and
no degree dictionary. The Z/2 invariant Phi'_2 is not a degree-3 Bokstedt
class. The monoid-ring character algebra is not a square H^2, intersection
pairing, correspondence algebra, Frobenius graph, positive Rosati
involution, Laurent boundary map, or torsor splitter.

Therefore strict-square divided-power/character data cannot itself be
promoted to End(S^2/Z). A surviving route must build a functor or
construction that extracts this object-level data as square cohomology and
intersection/correspondence data, then constructs the Laurent boundary,
torsor splitter, and positive Rosati.
```

Verdict label:

```text
N1B_CC_STRICT_SQUARE_DIVIDED_POWER__OBJECT_NONCOLLAPSE_NOT_GRADED_H2_OR_ROSATI__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_strict_square_divided_power_no_go` verifies the local
strict-square model.

CSD1 records the diagonal-fiber split:

```text
mu(L)=mu(C3)=3, Phi'_2(L)=1, Phi'_2(C3)=0.
```

CSD2 records bilinear factorization memory:

```text
mu(2x2)=mu(4x1)=4, Phi_3(2x2)=0, Phi_3(4x1)=1.
```

CSD3 records a zero-fiber split:

```text
mu = 0, chi_col = 2[1] - [2].
```

CSD4 records that the universal character algebra overproduces axes:

```text
chi(L)   = [1] + [2],
chi(C3)  = [3],
chi(2x2) = 2[2],
chi(4x1) = [4].
```

CSD5 records that multiplication is monoid-ring convolution on nonzero
integers. This is useful square data, but it is not an H^2/intersection form.

CSD6 records the standing Q/N obstruction: published CC RR/Pic/Hom probes
still factor through the diagonal. So the object-level data is not extracted
by those published functors.

CSD7 records that no grading or Bokstedt-degree dictionary is constructed.
Reading Phi'_2 as a degree-3 THH class spends a degree dictionary with no
independently matched constraints.

CSD8 records that no square H^2, intersection form, correspondence algebra,
Frobenius graph, or positive Rosati is defined.

CSD9-CSD10 record that no Laurent axis, boundary map, torsor splitter, or
DD.4 weight>=1 datum is produced; the DMP bottom support and torsor
obstructions remain.

## 4. Impact on R1

```text
R1 after docs 138-188:
  NEWLY CLOSED THIS CYCLE:
    - promoting strict Gamma-set square divided-power/character invariants
      themselves to End(S^2/Z), square H^2, intersection form,
      correspondence algebra, Frobenius graph, Laurent boundary data, or
      positive Rosati (doc 188).

  STILL ADMISSIBLE:
    - a future non-EM square functor or derived/tolerant construction that
      extracts the strict-square data as actual square cohomology and
      correspondence/intersection theory.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs the square data internally and finishes DD.4 weights>=1.
```

R1 is still open. The strict square's object noncollapse is valuable
evidence, not the target object. R2 remains locked.

## 5. Kill Conditions

```text
KILL-CSD.1 divided-power invariant as End(S^2/Z)
  A proposal identifies Phi_p, Phi'_p, or a strict-square character invariant
  with the correspondence algebra. Kill it unless it constructs square H^2
  and correspondences.

KILL-CSD.2 Z/p shadow as Bokstedt degree
  A proposal reads Phi'_2 as the degree-3 THH class or Phi_p as degree
  2p-1 data. Kill it unless a grading/dictionary is constructed with
  independent constraints.

KILL-CSD.3 monoid-ring character algebra as intersection form
  A proposal reads chi_col or its convolution as the H^2 intersection form.
  The monoid-ring character algebra is diagnostic object data, not an
  intersection pairing.

KILL-CSD.4 diagonal-factorizing published probe
  A proposal uses published CC RR/Pic/Hom machinery to extract the strict
  square data. Those probes factor through the diagonal curve shadow.

KILL-CSD.5 no Rosati/Frobenius/correspondence construction
  A proposal gives divided-power data but no Frobenius graph or replacement
  correspondence and no positive Rosati. This is not End(S^2/Z).

KILL-CSD.6 no Laurent boundary or torsor splitter
  A proposal gives divided-power data but no Laurent axis, boundary map,
  torsor splitter, or DD.4 weight>=1 datum. This does not unblock R2.
```

## 6. Board

```text
doc-137 R1, cycle 51 = doc 188:
  N1B_CC_STRICT_SQUARE_DIVIDED_POWER__OBJECT_NONCOLLAPSE_NOT_GRADED_H2_OR_ROSATI__NO_GO.

What got built: no End object. The value is a deletion: strict-square
divided-power/character data is real, but cannot be promoted to the missing
correspondence algebra.

What remains: construct a non-EM square functor or return to the in-house
PFD/Xbar DD.4 weight>=1 obstruction. Object-level noncollapse alone is not
the compactified square.
```
