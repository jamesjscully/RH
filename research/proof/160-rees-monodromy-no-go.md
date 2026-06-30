# 160 - Rees monodromy is still support bookkeeping

Status: no-go + Rees-monodromy/filtered-operator repair deletion,
2026-06-20. Twenty-third cycle of the doc-137 construction arc. Doc 159
killed the plain support-filtration Rees parameter because `q` is external
filtration bookkeeping and localized Rees remains rank `r`. This document
tests the next repair: add the standard filtered operators, namely
`q d/dq`, a nilpotent residue `N` along the support flag, or the unipotent
operator `1+N`, and use that package as the missing carrier shift/monodromy.

Witness, lead-reran this cycle:
`prime_int_n1b_rees_monodromy_no_go` (RMN1-RMN11 ALL PASS) -- exact
finite-rank nilpotent-power, unipotent-order, Euler-window, selector,
obstruction, and control-formability checks.

## 1. Purpose

The Rees-parameter repair can now say:

```text
do not use q alone;
use the filtered connection/residue package;
N supplies monodromy and q d/dq supplies the grading operator.
```

There are two different operators here. The Euler operator `q d/dq` acts on
the external Rees degree, so it repeats across every support summand. The
nilpotent `N` along the support flag is the finite support shift. It dies at
the support length. In the `F_2` coefficient model, `1+N` has finite
2-power order on each truncation, not an infinite Laurent orbit.

This document is local. It does not reject carrier-native monodromy. It
rejects only the operator package obtained from the visible support
filtration and its Rees parameter.

## 2. Lemma

```text
Lemma 160.1 (support Rees monodromy is not carrier monodromy).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2, and let F_*M_N be
the complete support flag. Let S be the support nilpotent that shifts one
step along this flag.

For r=3,4,6,10, the ranks of S are:

  2,3,5,9,

and the ranks of S^2 are:

  1,2,4,8.

The top nonzero power S^{r-1} has rank 1, and S^r has rank 0. Hence S is
nilpotent and cannot be inverted to produce a Laurent shift.

Over the F_2 coefficient model, the unipotent T=1+S has finite 2-power
order bounded by:

  4,4,8,16.

So T is not an infinite cyclic/Laurent orbit either.

On the localized Rees window |k| <= 2, the Euler operator q d/dq sees only
q-degree. The window ranks are:

  15,20,30,50,

and each q-degree eigenspace has multiplicity r. This is external Rees
bookkeeping repeated over the support pieces.

The monodromy filtration of the chosen support nilpotent repackages the
same support length:

  3,4,6,10.

The operator package consumes no primitive carrier map. Endpoint choices
remain:

  3,4,6,10,

and rank-one idempotent counts remain:

  28,120,2016,523776.

The operators do not invert the DMP bottom class, because there is no degree
-2 target. They construct no torsor splitter. The doc-138 shear obstruction
remains res_1(c)=1, the bottom obstruction remains y^2=0, and the same
Rees-monodromy package is formable on controls.

Therefore support/Rees-derived monodromy operators are not construction-grade
R1 carrier monodromy. A surviving route must construct N, 1+N, or the
grading operator as carrier-native correspondence data and prove DH/Epstein
death at that construction.
```

Verdict label:

```text
N1B_REES_MONODROMY__SUPPORT_NILPOTENT_AND_EULER_OPERATOR_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_rees_monodromy_no_go` verifies the finite models.

RMN1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

RMN2 records the first two powers of the support nilpotent:

```text
rank S:    2,3,5,9
rank S^2:  1,2,4,8.
```

RMN3 records nilpotence at the support length:

```text
rank S^{r-1}:  1,1,1,1
rank S^r:      0,0,0,0.
```

RMN4 records finite unipotent order bounds for `1+S` over the `F_2`
coefficient model:

```text
4,4,8,16.
```

RMN5 records the Euler window `|k| <= 2`:

```text
15,20,30,50,
```

with each q-degree eigenspace repeated across all `r` support pieces.

RMN6 records that the monodromy filtration of this support nilpotent
repackages the support length:

```text
3,4,6,10.
```

RMN7 records that `S`, `1+S`, and `q d/dq` consume no primitive carrier map.
They come from the support flag and the external Rees parameter.

RMN8 records the surviving selector problem. Endpoint choices remain:

```text
3,4,6,10.
```

Rank-one idempotent counts remain:

```text
28,120,2016,523776.
```

RMN9 records the base obstructions:

```text
y^2 = 0,     res_1(c)=1,
```

and no relation `b/phi(b)=c` is constructed.

RMN10 applies the carrier guard: finite support shifts and Rees-degree
operators use only filtered support data, so controls can form the same
package. RMN11 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-160:

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
      (doc 153);
    - support-degree flag/Borel reduction as the canonical idempotent
      selector (doc 154);
    - support-chain incidence/path algebra as the carrier correspondence
      algebra (doc 155);
    - groupoid completion / formal inversion of support-chain arrows as the
      carrier correspondence algebra (doc 156);
    - stabilizer/Laurent-loop decoration of the support groupoid as carrier
      isotropy (doc 157);
    - unit-labeled support-chain connections as carrier holonomy (doc 158);
    - support-filtration Rees parameter as carrier shift/deformation
      (doc 159);
    - support/Rees-derived nilpotent, unipotent, or Euler operator as carrier
      monodromy (doc 160).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/flag/idempotent/line,
      selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. Monodromy/operator data are admissible only if the carrier
constructs them. Support/Rees operators alone are bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-RMN.1 support nilpotent as carrier monodromy
  A proposal uses the nilpotent shift along the support flag as N. This is
  the finite support shift; it dies at the support length.

KILL-RMN.2 unipotent 1+N as Laurent orbit
  A proposal uses 1+N as the carrier shift. In the F_2 support model it has
  finite 2-power order on each truncation, not an infinite Laurent orbit.

KILL-RMN.3 Euler q d/dq as carrier grading
  A proposal uses q d/dq from the Rees package. It acts on external Rees
  degree and repeats across the support pieces.

KILL-RMN.4 Rees-monodromy package formable on controls
  Finite support shifts and Rees-degree operators are shadow-level data.
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 23 = doc 160:
  N1B_REES_MONODROMY__SUPPORT_NILPOTENT_AND_EULER_OPERATOR_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: Rees-derived
operator packages from the support filtration are not carrier monodromy.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/flag/idempotent/line, shift
  operator, selector/functional, and torsor splitter, with DH/Epstein death
  at that correspondence.
```
