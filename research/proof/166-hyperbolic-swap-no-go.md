# 166 - The hyperbolic swap is not carrier boundary glue

Status: no-go + hyperbolic-swap/J boundary-glue repair deletion,
2026-06-20. Twenty-ninth cycle of the doc-137 construction arc. Doc 165
killed support evaluation/coevaluation as automatic Tate boundary glue
because evaluation is scalar-valued, coevaluation is diagonal, and the needed
dual-boundary-to-primal-boundary map still requires boundary self-duality and
a Laurent twist. This document tests the next repair: use the hyperbolic form
itself, or a standard `J`/swap operator, as the canonical boundary glue.

Witness, lead-reran this cycle:
`prime_int_n1b_hyperbolic_swap_no_go` (HSW1-HSW12 ALL PASS) -- exact
finite-window hyperbolic-duality, dual-to-primal matching, involution,
boundary-rank, endpoint, twist, obstruction, and control-formability checks.

## 1. Purpose

The evaluation-glue repair can now say:

```text
do not use evaluation as the boundary map;
use the standard hyperbolic form/swap J on M plus M^vee;
J is the canonical boundary self-duality.
```

The hyperbolic form is a real support-level duality:

```text
W -> W^vee,      W = M plus M^vee.
```

It is not yet an operator:

```text
W -> W.
```

Writing a matrix `J` as an endomorphism of `W` requires an identification of
the primal and dual halves. In finite support windows that is matching data.
If such a matching is inserted, the resulting swap is an involution acting on
all Tate summands, not a Laurent generator and not the rank-one boundary glue
between the two shift defects.

This document is local. It does not reject carrier-native hyperbolic
dualities. It rejects only the claim that the support-level hyperbolic form
or a formal `J` automatically supplies the Tate boundary glue.

## 2. Lemma

```text
Lemma 166.1 (support hyperbolic swap is duality plus matching, not carrier
glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

The hyperbolic form gives full-rank duality:

  W_N -> W_N^vee,

again with ranks:

  6,8,12,20.

The boundary glue still needed by the Tate shift is rank one:

  1,1,1,1.

Turning the hyperbolic form into a swap operator `W_N -> W_N` requires
matching primal support lines with dual support lines. Coordinate matching
counts are:

  6,24,720,3628800.

If a matching is inserted, the swap satisfies:

  J^2 = 1.

A Laurent generator does not satisfy this finite-window involution profile.
The inserted swap acts on all Tate summands:

  6,8,12,20,

whereas the missing boundary glue acts on one boundary summand:

  1,1,1,1.

Boundary endpoint-pair choices remain:

  9,16,36,100.

Laurent unit twists in windows |k|<=1,2,4,8 remain:

  3,5,9,17.

Rank-one idempotent counts in the doubled Tate windows remain:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native
dual-to-primal matching, no pinned Laurent twist, and no torsor splitter. The
bottom obstruction remains y^2=0, there is still no DMP degree -2, the shear
obstruction remains res_1(c)=1, and the same hyperbolic-swap package is
formable on controls.

Therefore support hyperbolic form/swap data is not construction-grade R1
carrier boundary glue. A surviving route must construct the half
identification and Laurent twist as carrier-native correspondence data and
prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_HYPERBOLIC_SWAP__FULL_DUALITY_NOT_RANK_ONE_CARRIER_GLUE__NO_GO.
```

## 3. Proof

`prime_int_n1b_hyperbolic_swap_no_go` verifies the finite-window models.

HSW1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

HSW2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

HSW3 records the mismatch between full hyperbolic duality and boundary glue:

```text
hyperbolic duality ranks: 6,8,12,20
boundary glue rank:       1,1,1,1.
```

HSW4 records the matching data needed to turn the duality into a swap:

```text
6,24,720,3628800.
```

HSW5 records that the inserted swap is involutive:

```text
J^2 = 1.
```

This is not a Laurent-generator profile.

HSW6 records that the full swap acts on all Tate summands:

```text
6,8,12,20,
```

not only on the rank-one boundary defect.

HSW7 records boundary endpoint-pair choices:

```text
9,16,36,100.
```

HSW8 records Laurent unit twist choices in windows |k|<=1,2,4,8:

```text
3,5,9,17.
```

HSW9 records rank-one idempotent overproduction in the Tate windows:

```text
2016,32640,8386560,549755289600.
```

HSW10 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

HSW11 applies the carrier guard: hyperbolic finite-free support duality and
matching choices are shadow-level data, so controls can form the same
package. HSW12 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-166:

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
      correspondence (doc 162);
    - pro/infinite completion of the visible one-sided support chain as
      carrier orbit (doc 163);
    - Tate/continuous-dual completion of the visible support as carrier orbit
      (doc 164);
    - support evaluation/coevaluation as automatic Tate boundary glue
      (doc 165);
    - support hyperbolic form/swap as automatic Tate boundary glue (doc 166).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, half-identification, and Laurent twist/flag/
      idempotent/line, selector/functional/shift operator, torsor splitter,
      and weight>=1 datum from carrier data, and where DH/Epstein controls
      fail before signs, zeros, or comparison.
```

R1 is still open. Hyperbolic duality is admissible only if the carrier
constructs the half-identification and Laurent twist. A support-level `J`
operator alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-HSW.1 hyperbolic form as boundary glue
  A proposal uses the hyperbolic form W -> W^vee as the boundary map. This is
  full duality, not the rank-one boundary glue map.

KILL-HSW.2 standard J as carrier operator
  A proposal writes a swap J: W -> W. That requires a dual-to-primal
  identification/matching of the two halves unless the carrier constructs it.

KILL-HSW.3 hyperbolic swap as Laurent generator
  A proposal uses the inserted swap as the Laurent shift. The swap is an
  involution acting on all Tate summands, not a degree-translation generator
  or rank-one boundary glue.

KILL-HSW.4 hyperbolic-swap package formable on controls
  Hyperbolic finite-free support duality, matching choices, and Laurent twist
  normalization are shadow-level operations. DH/Epstein have not died at a
  carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 29 = doc 166:
  N1B_HYPERBOLIC_SWAP__FULL_DUALITY_NOT_RANK_ONE_CARRIER_GLUE__NO_GO.

What got built: no new sub-object. The value is a deletion: a support-level
hyperbolic form gives full duality, not rank-one boundary glue; turning it
into a swap requires half-identification data.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, half-identification, and Laurent twist/flag/
  idempotent/line, shift operator, selector/functional, and torsor splitter,
  with DH/Epstein death at that correspondence.
```
