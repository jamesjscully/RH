# 161 - Support filtered extensions split or overproduce gluing

Status: no-go + filtered-extension/unipotent-gluing repair deletion,
2026-06-20. Twenty-fourth cycle of the doc-137 construction arc. Doc 160
killed Rees-derived monodromy/operators because the nilpotent is finite
support shift and `q d/dq` sees only external Rees degree. This document
tests the next repair: use non-split filtered extension or gluing data
between the support associated-graded pieces as the carrier correspondence.

Witness, lead-reran this cycle:
`prime_int_n1b_filtered_extension_no_go` (FEX1-FEX10 ALL PASS) -- exact
finite-rank ordinary-extension, upper-triangular gluing, nilpotent-radical,
selector, obstruction, and control-formability checks.

## 1. Purpose

The Rees-monodromy repair can now say:

```text
do not use the split Rees package;
the support filtration carries non-split gluing data;
that extension data is the missing carrier correspondence.
```

For the visible support pieces over `L=F_2[u^{+-1}]`, ordinary module
extensions split: the pieces are free/projective rank-one `L`-modules. What
remains after choosing a support flag is filtered presentation data, modeled
by upper-triangular gluing. The strict upper-triangular radical is large and
nilpotent. It overproduces choices and still supplies no invertible Laurent
shift, no canonical idempotent/line, no DMP multiplication, and no torsor
splitter.

This document is local. It does not reject carrier-native non-split gluing.
It rejects only extension/gluing data attached to the visible support
filtration.

## 2. Lemma

```text
Lemma 161.1 (support filtered extensions are split or nilpotent bookkeeping).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let gr M_N be the associated graded of the support flag,
with r rank-one free L-pieces.

Ordinary L-module extensions between the free support pieces vanish:

  Ext^1_L(L,L) = 0.

Thus any support-only extension is split as an L-module. A filtered
presentation may still include upper-triangular gluing data. The strict
upper-triangular radical has rank

  r(r-1)/2.

For r=3,4,6,10 this gives:

  3,6,15,45.

Over the finite F_2 selector model, the unipotent gluing choices are:

  8,64,32768,35184372088832.

The radical is nilpotent. Its square has ranks:

  1,3,10,36,

its top nonzero power has rank:

  1,1,1,1,

and the next power is zero:

  0,0,0,0.

The adjacent extension slots are exactly the support-neighbor slots:

  2,3,5,9.

So the construction supplies support-index gluing, not carrier
multiplication. Endpoint choices remain:

  3,4,6,10,

and rank-one idempotent counts remain:

  28,120,2016,523776.

The gluing data does not invert the DMP bottom class, because there is no
degree -2 target. It constructs no torsor splitter. The doc-138 shear
obstruction remains res_1(c)=1, the bottom obstruction remains y^2=0, and
the same filtered-extension package is formable on controls.

Therefore support filtered extension/gluing data is not construction-grade
R1 carrier correspondence. A surviving route must construct non-split gluing
as carrier-native correspondence data and prove DH/Epstein death at that
construction.
```

Verdict label:

```text
N1B_FILTERED_EXTENSION__SUPPORT_GLUING_SPLIT_OR_NILPOTENT__NO_GO.
```

## 3. Proof

`prime_int_n1b_filtered_extension_no_go` verifies the finite models.

FEX1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

FEX2 records the ordinary extension class ranks:

```text
0,0,0,0.
```

This is the projectivity/free-module point: the support graded pieces do not
carry non-split `L`-module extension classes.

FEX3 records strict upper-triangular gluing ranks and finite unipotent choice
counts:

```text
strict ranks:       3,6,15,45
unipotent choices:  8,64,32768,35184372088832.
```

FEX4 records nilpotence of the unipotent radical:

```text
J^2 ranks:       1,3,10,36
top J^{r-1}:     1,1,1,1
J^r ranks:       0,0,0,0.
```

This is not an invertible Laurent shift.

FEX5 records adjacent extension slots:

```text
2,3,5,9.
```

They are support-neighbor slots.

FEX6 records that filtered gluing supplies no DMP multiplication and no
relation `b/phi(b)=c`.

FEX7 records the surviving selector problem. Endpoint choices remain:

```text
3,4,6,10.
```

Rank-one idempotent counts remain:

```text
28,120,2016,523776.
```

FEX8 records the base obstructions:

```text
y^2 = 0,     res_1(c)=1.
```

FEX9 applies the carrier guard: filtered finite-free modules and
upper-triangular gluing are shadow-level data, so controls can form the same
package. FEX10 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-161:

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
      monodromy (doc 160);
    - support filtered extension/unipotent gluing as carrier correspondence
      (doc 161).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/flag/
      idempotent/line, selector/functional/shift operator, torsor splitter,
      and weight>=1 datum from carrier data, and where DH/Epstein controls
      fail before signs, zeros, or comparison.
```

R1 is still open. Non-split gluing is admissible only if the carrier
constructs it. Support filtered gluing alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FEX.1 support filtered extension as carrier correspondence
  A proposal promotes extension data of the support filtration to the
  carrier. Ordinary extensions of free L-pieces split; remaining gluing is
  filtered presentation data.

KILL-FEX.2 upper-triangular gluing as Laurent shift
  A proposal uses the unipotent radical as the shift. The radical is
  nilpotent and dies at finite support length.

KILL-FEX.3 unipotent gluing as selector or torsor splitter
  A proposal uses gluing choices to select the line or split the torsor.
  The choices overproduce, leave endpoint/idempotent choices, and construct
  no b/phi(b)=c.

KILL-FEX.4 filtered extension package formable on controls
  Filtered finite-free modules and upper-triangular gluing are shadow-level
  data. DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 24 = doc 161:
  N1B_FILTERED_EXTENSION__SUPPORT_GLUING_SPLIT_OR_NILPOTENT__NO_GO.

What got built: no new sub-object. The value is a deletion: support filtered
extensions split as L-modules or become nilpotent upper-triangular gluing
data.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/flag/idempotent/
  line, shift operator, selector/functional, and torsor splitter, with
  DH/Epstein death at that correspondence.
```
