# 153 - Conjugacy symmetry does not choose the support corner

Status: no-go + conjugacy/symmetrized-idempotent selection deletion,
2026-06-20. Sixteenth cycle of the doc-137 construction arc. Doc 152
killed trace/minimality as a selector for the support End-envelope
idempotent. This document tests the next repair: use symmetry, conjugacy,
or orbit-summing to make the idempotent choice canonical.

Witness, lead-reran this cycle:
`prime_int_n1b_conjugacy_invariant_idempotent_no_go` (CGI1-CGI11 ALL
PASS) -- exact finite-rank rank-one orbit, central-invariant, orbit-sum,
obstruction, and control-formability checks.

## 1. Purpose

After docs 151-152, the support-envelope repair can try:

```text
do not choose an arbitrary minimal idempotent;
choose the conjugacy-invariant one;
or average/sum the rank-one idempotent orbit.
```

This fails for the opposite reason from trace/minimality. The full
`GL_r` symmetry of the support module is too large. It makes all rank-one
idempotents conjugate, so invariant data cannot choose one of them. The
only invariant elements of the full matrix algebra are central scalars,
and scalar idempotents are `0` and `1`, not rank-one corners.

This document is local. It does not reject a genuine smaller symmetry
coming from a carrier correspondence. It rejects only the support-matrix
symmetry of `Mat_r(L)` when no primitive carrier map has already reduced
the symmetry and selected the idempotent.

## 2. Lemma

```text
Lemma 153.1 (support conjugacy cannot select a rank-one corner).
Let M_N = R_DMP[-1..N] tensor L ~= L^r with r=N+2 and
L=F_2[u^{+-1}]. Let A_N = End_L(M_N) ~= Mat_r(L). The group GL_r(F_2)
acts on A_N by conjugation.

The rank-one idempotents in A_N form one GL_r-conjugacy orbit. Therefore
any GL_r-conjugacy invariant predicate can detect rank one, but cannot
distinguish one rank-one idempotent from another.

The GL_r-invariant elements of Mat_r(F_2) are central scalars. The scalar
idempotents are 0 and I. For r=3,4,6,10 their ranks are:

  0 and r = 0,3; 0,4; 0,6; 0,10.

None is rank one.

Moreover, summing the full rank-one idempotent orbit over F_2 gives the
zero matrix in the tested ranks r=3,4,6,10. Symmetrization therefore
collapses to central data and does not produce a corner.

The DMP bottom class remains square-zero, the doc-138 shear obstruction
remains, and the same conjugacy/symmetrization operations are formable on
controls. Therefore support-matrix symmetry is not a construction-grade R1
selector. A surviving route must construct a carrier-native correspondence
symmetry whose invariant data select the idempotent and where DH/Epstein
controls fail at that construction.
```

Verdict label:

```text
N1B_CONJUGACY_INVARIANT_IDEMPOTENT__SYMMETRY_COLLAPSE_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_conjugacy_invariant_idempotent_no_go` verifies the finite
models.

CGI1 records the support ranks inherited from doc 152:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

CGI2 records that the rank-one idempotent family remains large:

```text
28,120,2016,523776.
```

CGI3 records the conjugacy fact: rank-one idempotents form one
`GL_r(F_2)` orbit. Conjugacy sees only rank. It cannot choose a point in
the orbit.

CGI4-CGI5 record the invariant-element obstruction. Conjugacy-invariant
elements in the matrix algebra are central scalars, and the only central
idempotents have ranks:

```text
0 or r.
```

For `r>1`, neither is the required rank-one corner.

CGI6-CGI7 compute the orbit sum of all rank-one idempotents over `F_2`.
It is central and, in the tested support ranks, equals zero:

```text
r = 3,4,6,10  =>  sum_orbit(e) = 0.
```

Thus symmetrization does not rescue the corner.

CGI8-CGI9 record that the base obstructions remain:

```text
y^2 = 0,     res_1(c)=1.
```

CGI10 applies the carrier guard: `GL_r` conjugacy and orbit sums are
finite-free module operations, so controls can perform the same symmetry
test. CGI11 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-153:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141);
    - bottom-class localization / formal inversion repair (doc 142);
    - freely adjoining an independent Laurent generator (doc 143);
    - projecting a free/tensor Laurent repair to one copy (doc 144);
    - formally adjoining a torsor splitter b with phi(b)=b*c^-1 (doc 145);
    - quotienting a free/tensor Laurent repair to one line (doc 146);
    - shift-coinvariant collapse of the tensor copies to one line (doc 147);
    - shift telescope/direct-limit packaging of that collapse (doc 148);
    - formal shift-operator insertion as the missing carrier shift (doc 149);
    - support-module End envelope as the missing correspondence algebra
      (doc 150);
    - Morita/idempotent corner of the support End envelope as the selected
      carrier line (doc 151);
    - trace/minimality selection of that idempotent (doc 152);
    - conjugacy-invariant or symmetrized selection of that idempotent
      (doc 153).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the idempotent or line, selector/functional/shift operator,
      torsor splitter, and weight>=1 datum from carrier data, and where
      DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Symmetry is now allowed only if it is carrier-native and
selective. The full support-module symmetry is not selective; it erases the
choice.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-CGI.1 conjugacy-invariant idempotent as canonical corner
  A proposal uses GL_r-conjugacy invariance in the support End envelope to
  choose e. Rank-one idempotents form one orbit, so invariance cannot pick
  one.

KILL-CGI.2 central scalar as corner
  A proposal replaces the orbit by its invariant central data. The central
  scalar idempotents are 0 and I, not rank-one corners.

KILL-CGI.3 orbit sum / averaging as selected idempotent
  A proposal sums or averages the rank-one orbit. Over F_2 in the tested
  support ranks, the orbit sum is zero; in any case, the result is central,
  not a selected corner.

KILL-CGI.4 symmetry formable on controls
  GL_r-conjugacy and orbit sums are finite-free module operations. DH/Epstein
  have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 16 = doc 153:
  N1B_CONJUGACY_INVARIANT_IDEMPOTENT__SYMMETRY_COLLAPSE_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: support-matrix
symmetry cannot choose the corner.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data choose the idempotent/line, shift operator, selector/functional,
  and torsor splitter, with DH/Epstein death at that correspondence.
```
