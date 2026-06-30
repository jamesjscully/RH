# 159 - The support Rees parameter is not a carrier shift

Status: no-go + support-filtration/Rees-parameter repair deletion,
2026-06-20. Twenty-second cycle of the doc-137 construction arc. Doc 158
killed unit-labeled support-chain connections because the support graph is a
tree and the labels are gauge-trivial. This document tests the next repair:
package the support flag as a Rees module and use the Rees parameter as the
missing Laurent/shift/deformation datum.

Witness, lead-reran this cycle:
`prime_int_n1b_rees_filtration_no_go` (RFS1-RFS11 ALL PASS) -- exact
finite-rank support-flag, associated-graded, specialization, localized Rees
window, obstruction, and control-formability checks.

## 1. Purpose

The support-connection repair can now say:

```text
do not label arrows on the tree;
package the support flag by the Rees construction;
then the Rees parameter q supplies the missing shift/deformation variable.
```

The Rees construction is legitimate bookkeeping for a filtration. But in
this support setting it does not construct a carrier correspondence. The
parameter `q` records filtration degree. Specializing `q=1` recovers the
same support module, the associated graded recovers the same visible support
pieces, and inverting `q` gives a rank-`r` Laurent extension rather than a
selected carrier line.

This document is local. It does not reject a carrier-native deformation or
Rees construction. It rejects only the Rees module of the visible support
filtration when no primitive carrier map constructs the parameter.

## 2. Lemma

```text
Lemma 159.1 (support Rees data are external filtration bookkeeping).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2, and let F_*M_N be
the complete support flag.

The Rees module Rees_F(M_N) records the flag by adjoining a parameter q.
Its q=1 specialization recovers M_N. Its associated graded has the same r
one-dimensional support pieces.

For r=3,4,6,10, the support ranks are:

  3,4,6,10,

and the proper support inclusions are:

  2,3,5,9.

The polynomial Rees window 0 <= k <= 2 has rank:

  3r = 9,12,18,30.

After inverting q, the Laurent Rees window |k| <= 1 has rank:

  3r = 9,12,18,30,

and the window |k| <= 2 has rank:

  5r = 15,20,30,50.

Thus localization in q gives a rank-r Laurent extension over L[q^{+-1}],
not one selected Laurent line. The q-shift moves filtration degree; it is
not DMP multiplication. Identifying q with the external tensor variable u or
with the Lin/Weyl-Tate generator t is an imposed relation unless the carrier
constructs it.

Endpoint choices remain:

  3,4,6,10,

and rank-one idempotent counts remain:

  28,120,2016,523776.

The Rees parameter does not invert the DMP bottom class, because there is no
degree -2 target. It constructs no torsor splitter. The doc-138 shear
obstruction remains res_1(c)=1, the bottom obstruction remains y^2=0, and
the same support-filtration Rees package is formable on controls.

Therefore the support Rees parameter is not a construction-grade R1 carrier
shift/deformation. A surviving route must construct the filtration parameter
or deformation as carrier-native correspondence data and prove DH/Epstein
death at that construction.
```

Verdict label:

```text
N1B_REES_FILTRATION__EXTERNAL_PARAMETER_NOT_CARRIER_SHIFT__NO_GO.
```

## 3. Proof

`prime_int_n1b_rees_filtration_no_go` verifies the finite models.

RFS1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

RFS2 records the support flag and proper inclusion counts:

```text
flag steps:        3,4,6,10
proper inclusions: 2,3,5,9.
```

RFS3 records that the associated graded recovers the same support pieces:

```text
3,4,6,10.
```

RFS4 records that the `q=1` specialization recovers the same support module:

```text
3,4,6,10.
```

RFS5 records the polynomial Rees window `0 <= k <= 2`:

```text
9,12,18,30.
```

RFS6 records localized Laurent windows:

```text
|k| <= 1:  9,12,18,30
|k| <= 2:  15,20,30,50.
```

These are rank-`r` Laurent extensions. They do not select one carrier line.

RFS7 records that the Rees parameter consumes no primitive carrier map. It
records filtration degree.

RFS8 records that using `q` as the carrier shift requires an external
identification:

```text
q = u  or  q = t
```

unless a carrier constructs that relation.

RFS9 records the surviving selector problem. Endpoint choices remain:

```text
3,4,6,10.
```

Rank-one idempotent counts remain:

```text
28,120,2016,523776.
```

RFS10 records the base obstructions:

```text
y^2 = 0,     res_1(c)=1,
```

and no relation `b/phi(b)=c` is constructed.

RFS11 applies the carrier guard: Rees construction uses filtered finite-free
support data, so controls can form the same package.

## 4. Impact on R1

```text
R1 after docs 138-159:

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
      (doc 159).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/flag/idempotent/line, selector/functional/shift
      operator, torsor splitter, and weight>=1 datum from carrier data, and
      where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. A Rees/deformation parameter is admissible only if the
carrier constructs it. The support Rees variable alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-RFS.1 support Rees parameter as carrier shift
  A proposal packages the support flag by Rees_F(M) and uses q as the shift.
  The parameter q is external filtration bookkeeping unless a carrier
  constructs it.

KILL-RFS.2 localized Rees module as Laurent line
  A proposal inverts q and takes the localized Rees module as the desired
  Laurent object. It is rank r over L[q^{+-1}], not a selected carrier line.

KILL-RFS.3 Rees specialization/associated graded as new carrier data
  A proposal uses q=1 or gr_F. These recover the original support module or
  visible support pieces; they add no carrier correspondence.

KILL-RFS.4 support Rees package formable on controls
  Rees construction on a finite-free support filtration is shadow-level data.
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 22 = doc 159:
  N1B_REES_FILTRATION__EXTERNAL_PARAMETER_NOT_CARRIER_SHIFT__NO_GO.

What got built: no new sub-object. The value is a deletion: the support
Rees parameter is external filtration bookkeeping.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
