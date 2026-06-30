# 139 - N1-b' line-comparison no-go: DMP truncates the geometric line

Status: no-go + dependency split, 2026-06-20. Second cycle of the
doc-137 construction arc. It attacks the one R1 clause left open by
doc 138: N1-b', the geometric `y` versus Weyl-Tate `t` comparison
posed after EE.2 killed the old Borel route. Result: the published
Dotto-Moi-Patchkoria computation rules out the strong/full-line reading.
At the `TCR(F_2;2)^{phi Z/2}` fiber level there is a bottom degree `-1`
class, but no classes below degree `-1`, so it cannot supply a Laurent
Lin line `F_2[t^{+-1}]`.

Witness, lead-reran this cycle:
`prime_int_n1b_prime_line_no_go` (N1P1-N1P6 ALL PASS) -- exact support
calculus from DMP Theorem C/E for `F_2`, plus the doc-138 leading
obstruction reminder.

External-source audit, 2026-06-20:

```text
- HNS itself is still not an archived primary paper in the sources found.
  Harpaz's current research page lists the real cyclotomic trace map with
  Shah and Nikolaus as "in preparation"; recent papers still cite
  "Real topological cyclic homology and normal L-theory" as to appear /
  in preparation.
- Dotto-Moi-Patchkoria is published / arXived and is enough for the
  support calculation used here: it gives a formula for geometric
  fixed-points of real TCR and computes perfect characteristic-2 fields.
```

Primary external anchors checked:
`https://www.math.univ-paris13.fr/~harpaz/`;
`https://arxiv.org/abs/2106.04891`;
`https://doi.org/10.1112/jlms.12862`.

## 1. Purpose

Doc 138 closed the Weyl-shear-fixed extension route:

```text
H^1(<phi>; U_1) = Z/2,
c = (1+z)^-1 is the nonzero class.
```

It explicitly did not touch N1-b': the geometric comparison between the
Quigley-Shah/DMP line `y` and the Weyl-Tate Lin line `t`, under the
HNS-style fiber formula.

The question for this cycle is narrower:

```text
Can N1-b' still mean a full Laurent-line comparison

    F_2[y^{+-1}]  ~  F_2[t^{+-1}]

inside the actual TCR geometric fiber?
```

Answer: no. DMP truncates the geometric fiber. The full Laurent line is a
Tate-side input, not a TCR-fiber output.

## 2. Lemma

```text
Lemma 139.1 (DMP support kills the full-line N1-b' reading). For
`k = F_2`, Dotto-Moi-Patchkoria Theorem C/E gives

  TCR(k;2)^{phi Z/2}
    ~=  direct_sum_{n >= 0} (Sigma^{2n-1} H F_2  +  Sigma^{2n} H F_2),

because `id + Frobenius` is zero on `F_2`, so both
`coker(id+F)` and `ker(id+F)` are `F_2`.

Consequently

  pi_d TCR(F_2;2)^{phi Z/2} =
    F_2   for d = -1 and for all d >= 0,
    0     for all d <= -2.

But the Weyl-Tate Lin line `F_2[t^{+-1}]`, with `|t| = -1`, has a
one-dimensional `F_2` class in every integer degree. Therefore no graded
line isomorphism from `TCR(F_2;2)^{phi Z/2}` to the Lin line exists; the
failure is visible already in degree `-2`.

Thus N1-b' cannot supply DD.4's weight-complete Lin/Weyl-Tate line at the
TCR-fiber level. At most it can supply a bottom-class comparison in degree
`-1`, or else the target must move to a different carrier/external
normalization.
```

Verdict label:

```text
N1B_PRIME_FULL_LINE_COMPARISON__NO_GO__DMP_TCR_PHI_SUPPORT_BOTTOMS_AT_MINUS_ONE.
```

## 3. Proof

`prime_int_n1b_prime_line_no_go` verifies the exact support calculation.

N1P1 computes the two coefficient groups for `F_2`: the map
`id + Frobenius` is identically zero, so both the kernel and cokernel are
one-dimensional over `F_2`.

N1P2 records the DMP support:

```text
degree -1: nonzero,
degree >= 0: nonzero,
degree <= -2: zero.
```

N1P3 records the Lin/Laurent support: `F_2[t^{+-1}]` has a class in
every integer degree.

N1P4-N1P5 compare the two supports. The full-line comparison fails
already at degree `-2`:

```text
pi_-2 TCR(F_2;2)^{phi Z/2} = 0,
pi_-2 F_2[t^{+-1}] = F_2.
```

N1P6 re-records the doc-138 leading obstruction in its minimal form:
`res_1((1+z)^-1) = 1`, while `res_1` kills coboundaries. This cycle does
not undo the Weyl-shear obstruction; it only removes the strongest
remaining interpretation of N1-b'.

## 4. What This Does Not Prove

This is not a proof of DD.4, not a construction of `End(S^2/Z)`, and not
RH progress. It is a Layer-I/STAGE deletion test.

It does not prove that the bottom class in degree `-1` fails to compare
with `t`. DMP leaves that bottom class alive. What is killed is the claim
that the actual TCR geometric fiber contains the whole Laurent `y` line
needed to identify with the Lin line degree-by-degree.

It also does not replace HNS as a theorem about normal L-theory. The
source audit says HNS is still an external dependency for any statement
requiring the unpublished normal-L-theory identification. DMP is used only
for the published support computation.

## 5. Impact on R1

```text
R1 status after docs 138-139:

  - Weyl-shear-fixed weight>=1 extension: NO-GO (doc 138).
  - Full N1-b' Laurent-line comparison in TCR^{phi}: NO-GO (this doc).
  - Bottom-class comparison y -> t: OPEN, but it is not enough by itself
    to unlock the weight-complete DD.4 datum.
  - External phi-invariant normalization: OPEN; still must overcome the
    doc-138 H^1 obstruction with a genuine new carrier or a new map, not
    by choosing a torsor representative.
```

R1 is therefore sharpened again, not finished. The route "use HNS/DMP to
identify the geometric line with the Weyl-Tate line" is closed in its
line-level form. The only surviving R1 work is narrower:

```text
(a) compute the bottom-class comparison explicitly, with a witness, and
    state exactly what it buys;
(b) produce an external phi-invariant normalization that is not a unit
    insertion and not a torsor choice;
(c) move to a different carrier where a full line actually exists in the
    constructed object, and run the DH/Epstein carrier guards.
```

R2 remains locked. The archimedean unit is still gated on a real Layer-I
self-duality carrier; docs 138-139 give two obstructions, not the carrier.

## 6. Kill Conditions

```text
KILL-N1B'.1 full Laurent-line claim
  A proposal says N1-b' supplies `F_2[y^{+-1}] ~= F_2[t^{+-1}]` inside
  `TCR(F_2;2)^{phi Z/2}`. It cannot: DMP support has no class in degree
  -2 or below. Witness: prime_int_n1b_prime_line_no_go.

KILL-N1B'.2 bottom class promoted to full DD.4
  A proposal proves or assumes only a degree -1 comparison `y -> t` and
  promotes it to the weight-complete DD.4 datum. That is too weak: the
  full Lin line and the weight>=1 torsor are exactly where docs 138-139
  find the obstructions.

KILL-N1B'.3 HNS citation without map data
  A proposal cites the unpublished/normal-L-theory HNS identification but
  does not exhibit the induced map on the `y`/`t` classes or its support.
  That is dependency transfer, not construction.
```

## 7. Board

```text
doc-137 R1, cycle 2 = doc 139:
  N1B_PRIME_FULL_LINE_COMPARISON__NO_GO__DMP_TCR_PHI_SUPPORT_BOTTOMS_AT_MINUS_ONE.

What got built: no new sub-object. The value is a deletion: the published
DMP computation removes the full-line version of the last N1-b' escape.

Next valid work:
  1. bottom-class `y -> t` computation only, with a witness and with
     no promotion beyond its degree;
  2. or an external phi-invariant normalization that explicitly evades
     doc 138's `H^1 = Z/2` obstruction;
  3. or a different carrier, admitted only if it has a runnable witness
     and dies on DH/Epstein at a named point.
```
