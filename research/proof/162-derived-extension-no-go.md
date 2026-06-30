# 162 - Support derived extensions have no hidden higher gluing

Status: no-go + derived-extension/Yoneda-gluing repair deletion,
2026-06-20. Twenty-fifth cycle of the doc-137 construction arc. Doc 161
killed ordinary support filtered extensions because extensions of the free
`L=F_2[u^{+-1}]` support pieces split, and the remaining upper-triangular
gluing is nilpotent support bookkeeping. This document tests the next repair:
replace ordinary filtered extensions by derived/Yoneda Ext classes, Massey
products, or `A_infinity`-style higher gluing on the support filtration.

Witness, lead-reran this cycle:
`prime_int_n1b_derived_extension_no_go` (DEX1-DEX12 ALL PASS) -- exact
finite-rank positive-Ext, Yoneda, Massey-seed, support-interval, nilpotent
radical, selector, obstruction, and control-formability checks.

## 1. Purpose

The filtered-extension repair can now say:

```text
ordinary extensions split, but the derived category remembers higher
extension/Massey/A_infinity gluing;
that hidden higher gluing is the missing carrier correspondence.
```

For the visible support pieces over `L=F_2[u^{+-1}]`, this repair has no
ordinary derived content. Each associated-graded support piece is `L`, hence
projective. Therefore:

```text
Ext^n_L(L,L) = 0 for every n > 0.
```

The ordinary Yoneda algebra has no positive-degree support classes and no
`Ext^1` seeds from which Massey products can be built. Any nonzero "higher
gluing" that remains is not hidden Ext data; it is a chosen cochain on the
finite support chain. Those cochains are the same strict upper-triangular
nilpotent radical already exposed in doc 161.

This document is local. It does not reject carrier-native derived operations.
It rejects only derived/Yoneda/Massey data attached to the visible support
filtration.

## 2. Lemma

```text
Lemma 162.1 (support derived extensions vanish or reduce to nilpotent
support cochains).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let gr M_N be the associated graded of the support flag,
with r rank-one free L-pieces.

For support pieces L and every positive derived degree n:

  Ext^n_L(L,L) = 0.

Thus the positive-degree ordinary Yoneda algebra of the support pieces is
zero. In particular, there are no support Ext^1 seeds for Massey-style
higher products.

The degree-zero derived endomorphism algebra is only the matrix envelope:

  Hom_L(L^r,L^r) ~= Mat_r(L),

with ranks 9,16,36,100 for r=3,4,6,10.

If one inserts higher support cochains anyway, they live in the same strict
upper-triangular radical J of the support chain. Its rank is:

  r(r-1)/2 = 3,6,15,45.

The exact interval slots of length one are:

  2,3,5,9;

of length two:

  1,2,4,8;

and the top interval count is always 1, with no interval of length r:

  0,0,0,0.

The radical is nilpotent, with J^2 ranks:

  1,3,10,36,

and J^r=0.

Endpoint choices remain:

  3,4,6,10,

and rank-one idempotent counts remain:

  28,120,2016,523776.

The package constructs no DMP multiplication, no invertible Laurent shift,
and no torsor splitter. The bottom obstruction remains y^2=0, the shear
obstruction remains res_1(c)=1, and the same derived-extension package is
formable on controls.

Therefore support derived/Yoneda/Massey gluing is not construction-grade R1
carrier correspondence. A surviving route must construct the derived
operations as carrier-native correspondence data and prove DH/Epstein death
at that construction.
```

Verdict label:

```text
N1B_DERIVED_EXTENSION__POSITIVE_EXT_VANISHES_OR_NILPOTENT_SUPPORT_CHAINS__NO_GO.
```

## 3. Proof

`prime_int_n1b_derived_extension_no_go` verifies the finite models.

DEX1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

DEX2 records positive Ext ranks in degrees 1,2,3:

```text
all zero.
```

This is the projectivity/free-module point: the support graded pieces do not
carry positive derived extension classes over `L`.

DEX3 records that the ordinary positive-degree Yoneda algebra contributes no
support classes:

```text
0,0,0,0.
```

DEX4 records that Massey-style products have no `Ext^1` seeds:

```text
0,0,0,0.
```

DEX5 records the degree-zero derived endomorphism ranks:

```text
9,16,36,100.
```

This recovers the support-module matrix envelope of doc 150, not a new
carrier correspondence.

DEX6 records the rank of inserted strict upper-triangular support cochains:

```text
3,6,15,45.
```

DEX7 records exact finite support-interval slots:

```text
length 1:  2,3,5,9
length 2:  1,2,4,8
top:       1,1,1,1
length r:  0,0,0,0
```

DEX8 records nilpotence:

```text
J^2 ranks: 1,3,10,36
J^r ranks: 0,0,0,0.
```

This is not an invertible Laurent orbit.

DEX9 records the surviving selector problem. Endpoint choices remain:

```text
3,4,6,10.
```

Rank-one idempotent counts remain:

```text
28,120,2016,523776.
```

DEX10 records the base obstructions:

```text
y^2 = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

DEX11 applies the carrier guard: projective support pieces and chosen higher
support cochains are shadow-level data, so controls can form the same
package. DEX12 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-162:

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
      (doc 161);
    - support derived/Yoneda/Massey/A_infinity gluing as carrier
      correspondence (doc 162).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/flag/idempotent/line, selector/functional/shift operator,
      torsor splitter, and weight>=1 datum from carrier data, and where
      DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Derived operations are admissible only if the carrier
constructs them. Support-derived gluing alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-DEX.1 support-derived Ext as carrier correspondence
  A proposal promotes derived extension data of the support filtration to
  the carrier. Positive Ext between free L-pieces vanishes.

KILL-DEX.2 Massey/A_infinity support gluing as hidden carrier data
  A proposal uses higher products on the visible support filtration. There
  are no Ext1 seeds; any nonzero higher cochains are inserted support-chain
  data.

KILL-DEX.3 higher support cochains as Laurent shift or selector
  A proposal uses the higher cochain radical as the shift or selector. The
  radical is strict upper-triangular, finite, nilpotent, and leaves endpoint
  and idempotent choices.

KILL-DEX.4 derived-extension package formable on controls
  Projective support pieces, degree-zero matrix envelopes, and chosen higher
  support cochains are shadow-level data. DH/Epstein have not died at a
  carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 25 = doc 162:
  N1B_DERIVED_EXTENSION__POSITIVE_EXT_VANISHES_OR_NILPOTENT_SUPPORT_CHAINS__NO_GO.

What got built: no new sub-object. The value is a deletion: support
derived/Yoneda extension data has no positive Ext content, and inserted
higher cochains reduce to nilpotent support-chain bookkeeping.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/flag/idempotent/line, shift operator, selector/functional, and
  torsor splitter, with DH/Epstein death at that correspondence.
```
