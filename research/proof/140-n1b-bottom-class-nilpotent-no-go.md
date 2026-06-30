# 140 - N1-b' bottom class is not the Lin generator

Status: no-go + surviving-scope cut, 2026-06-20. Third cycle of the
doc-137 construction arc. It follows doc 139's support no-go. Doc 139
killed the full Laurent-line reading of N1-b'. This document kills the
next surviving over-promotion: the claim that the remaining degree `-1`
class in `TCR(F_2;2)^{phi Z/2}` can be the Lin/Weyl-Tate generator `t`
in the multiplicative or DD.4-duality sense.

Witness, lead-reran this cycle:
`prime_int_n1b_bottom_class_nilpotent` (N1Q1-N1Q7 ALL PASS) -- exact
support/product obstruction from DMP Theorem C/E plus the Lin Laurent
line model.

## 1. Purpose

After doc 139, N1-b' has only one non-deleted interpretation left:

```text
Maybe the bottom degree -1 geometric class y compares to the Lin class t,
even though the full Laurent line does not survive in TCR^{phi}.
```

This cycle asks what kind of comparison that could be. The answer is
strictly additive/degree-label at best. It cannot be multiplicative, cannot
make `y` invertible, and cannot supply the `t`-periodic DD.4 datum.

## 2. Lemma

```text
Lemma 140.1 (the DMP bottom class is square-zero, hence not the Lin
generator). In the DMP support for `TCR(F_2;2)^{phi Z/2}`,

  pi_-1 = F_2,
  pi_-2 = 0.

Therefore any product of a degree `-1` class with itself is zero by
degree support. In contrast the Lin/Weyl-Tate line

  F_2[t^{+-1}], |t| = -1,

has `t^2 != 0` in degree `-2`, and `t` is a unit.

Consequently no multiplicative comparison, ring comparison, or
DD.4-duality-generator comparison can identify the DMP bottom class with
the Lin generator `t`. A nonzero additive map in degree `-1`, if it exists,
is only a degree label; it does not unlock the weight-complete Lin line and
does not evade doc 138's weight>=1 torsor obstruction.
```

Verdict label:

```text
N1B_PRIME_BOTTOM_CLASS__NILPOTENT_NOT_LIN_GENERATOR__NO_GO.
```

## 3. Proof

`prime_int_n1b_bottom_class_nilpotent` performs the support and product
checks.

N1Q1-N1Q2 record DMP support for `F_2`: a nonzero degree `-1` class and
zero degree `-2` group.

N1Q3 says the square of any degree `-1` class is zero, because the target
degree `-2` group is zero.

N1Q4 records the Lin side: `F_2[t^{+-1}]` has nonzero degree `-1` and
degree `-2` classes, with `t^2` nonzero.

N1Q5 gives the contradiction for a multiplicative comparison:

```text
y^2 = 0, but t^2 != 0.
```

N1Q6-N1Q7 record the DD.4 consequence: the bottom class is not a unit and
multiplication by it cannot be a degree-shift automorphism. The Lin
duality datum is `t`-periodic; the DMP bottom class is not.

## 4. What Survives

An additive comparison of one-dimensional degree `-1` vector spaces is not
ruled out. Such a comparison could still be useful as bookkeeping: it may
identify the geometric bottom label with the Lin bottom label.

But it cannot carry the DD.4 load. DD.4 needs a `t`-periodic duality datum
and a weight-complete self-duality carrier. Docs 138-140 now say:

```text
- the weight>=1 Weyl-shear-fixed extension is obstructed by H^1 = Z/2;
- the full N1-b' Laurent line is absent in TCR^{phi};
- the remaining bottom class is square-zero and noninvertible.
```

So the bottom-class route is demoted from construction clause to
bookkeeping shadow.

## 5. Impact on R1

```text
R1 after docs 138-140:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140).

  STILL OPEN:
    - an additive bottom-class comparison, only as bookkeeping;
    - an external phi-invariant normalization that genuinely bypasses the
      H^1 obstruction, not by choosing a torsor representative;
    - a different carrier where a full line and weight>=1 datum exist, with
      DH/Epstein death at named points.
```

R2 remains locked. Nothing in docs 138-140 supplies the archimedean unit
or the Layer-II positive Rosati involution.

## 6. Kill Conditions

```text
KILL-N1B'.4 bottom class as unit
  A proposal identifies the DMP degree -1 class with the Lin generator `t`
  multiplicatively. It cannot: the DMP class squares to zero by support,
  while `t^2` is nonzero.

KILL-N1B'.5 additive comparison promoted to DD.4
  A proposal constructs only a one-dimensional degree -1 additive
  comparison and promotes it to DD.4. That is bookkeeping, not a
  t-periodic self-duality datum.
```

## 7. Board

```text
doc-137 R1, cycle 3 = doc 140:
  N1B_PRIME_BOTTOM_CLASS__NILPOTENT_NOT_LIN_GENERATOR__NO_GO.

What got built: no new sub-object. The value is a deletion: the last
bottom-class interpretation is demoted to additive bookkeeping.

Next valid R1 work:
  1. external phi-invariant normalization that explicitly evades doc 138;
  2. or a different carrier where the full line and weight>=1 datum exist
     and DH/Epstein die at named points.

Do not spend a cycle merely proving a one-dimensional additive bottom
comparison unless it also supplies one of those two items.
```
