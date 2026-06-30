# 165 - Evaluation is not the Tate boundary glue

Status: no-go + evaluation/coevaluation boundary-glue repair deletion,
2026-06-20. Twenty-eighth cycle of the doc-137 construction arc. Doc 164
killed Tate/continuous-dual completion of visible support because the
unilateral shift plus its dual adjoint still has one-dimensional kernel and
cokernel, so invertibility needs a boundary glue map. This document tests the
next repair: use the evaluation/coevaluation maps of the Tate dual pair and
claim the boundary glue is automatic.

Witness, lead-reran this cycle:
`prime_int_n1b_eval_boundary_glue_no_go` (EBG1-EBG13 ALL PASS) -- exact
finite-window evaluation, coevaluation, boundary-defect, Laurent-twist,
selector, obstruction, and control-formability checks.

## 1. Purpose

The Tate-dual repair can now say:

```text
the boundary glue is not inserted;
it is the canonical evaluation/coevaluation of the Tate dual pair.
```

Evaluation and coevaluation are real support-linear maps. They are not the
required boundary glue. Evaluation is scalar-valued:

```text
M^vee tensor M -> L.
```

Coevaluation is the diagonal class:

```text
L -> M tensor M^vee.
```

The missing map is different:

```text
dual boundary line -> primal boundary line.
```

Constructing that map requires a self-duality or metric on the boundary line,
plus a Laurent unit twist over `L=F_2[u^{+-1}]`. Choosing degree zero is a
normalization unless the carrier produces it.

This document is local. It does not reject carrier-native evaluation pairings
or carrier-native boundary glue. It rejects only the claim that support-level
evaluation/coevaluation automatically supplies the Tate boundary glue.

## 2. Lemma

```text
Lemma 165.1 (evaluation does not construct boundary glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let M_N^vee be the finite-window dual support module.

For r=3,4,6,10, the Tate windows still have ranks:

  6,8,12,20.

Evaluation and coevaluation see all support summands:

  evaluation diagonal pairs:    3,4,6,10,
  coevaluation diagonal terms:  3,4,6,10.

Without boundary glue, the Tate shift still has:

  dim ker = 1,      dim coker = 1.

Thus a rank-one boundary glue map is still needed in every tested window.

Evaluation is scalar-valued and does not output a map from the dual boundary
line to the primal boundary line. Coevaluation outputs the diagonal class and
does not output that boundary map either.

Supplying the map requires a rank-one boundary self-duality. Over
L=F_2[u^{+-1}], Hom_L(L,L)=L, so the Laurent unit twist is not pinned by
support data. In finite Laurent windows |k|<=1,2,4,8, the unit twist choices
are:

  3,5,9,17,

and the nonzero boundary maps in those windows are:

  7,31,511,131071.

If one imposes degree-zero glue, the count is one in each window, but the
degree-zero choice is a normalization, not carrier output.

Endpoint choices remain:

  3,4,6,10,

and rank-one idempotent counts in the doubled Tate windows remain:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native boundary
self-duality, no pinned Laurent twist, and no torsor splitter. The bottom
obstruction remains y^2=0, there is still no DMP degree -2, the shear
obstruction remains res_1(c)=1, and the same evaluation-glue package is
formable on controls.

Therefore evaluation/coevaluation on visible Tate support is not
construction-grade R1 carrier boundary glue. A surviving route must construct
the boundary self-duality and Laurent twist as carrier-native correspondence
data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_EVALUATION_BOUNDARY_GLUE__SCALAR_PAIRING_NOT_CARRIER_MAP__NO_GO.
```

## 3. Proof

`prime_int_n1b_eval_boundary_glue_no_go` verifies the finite-window models.

EBG1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

EBG2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

EBG3 records that evaluation and coevaluation see every support summand:

```text
evaluation pairs:       3,4,6,10
coevaluation diagonals: 3,4,6,10.
```

EBG4 records that, without the boundary map, the Tate shift still has:

```text
ker 1, coker 1,
```

and a rank-one boundary glue map is still needed.

EBG5 records the type mismatch:

```text
evaluation outputs a scalar, not a dual-boundary-to-primal-boundary map.
```

EBG6 records the matching coevaluation mismatch:

```text
coevaluation outputs the diagonal class, not the boundary glue map.
```

EBG7 records that a rank-one boundary self-duality is an additional
identification.

EBG8 records the Laurent ambiguity. In finite windows |k|<=1,2,4,8:

```text
unit twists:  3,5,9,17
nonzero maps: 7,31,511,131071.
```

EBG9 records that degree-zero glue is a single choice only after imposing
degree-zero normalization.

EBG10 records the surviving selector problem. Endpoint choices remain:

```text
3,4,6,10.
```

Rank-one idempotent counts in Tate windows remain:

```text
2016,32640,8386560,549755289600.
```

EBG11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

EBG12 applies the carrier guard: evaluation/coevaluation of finite-free
support modules are shadow-level data, so controls can form the same package.
EBG13 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-165:

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
      (doc 165).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality and Laurent twist/flag/idempotent/line,
      selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. Evaluation pairings are admissible only if the carrier
constructs the boundary self-duality and Laurent twist. Support
evaluation/coevaluation alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-EBG.1 evaluation as boundary glue
  A proposal uses evaluation M^vee tensor M -> L as the boundary map. This is
  scalar-valued, not a linear map from the dual boundary line to the primal
  boundary line.

KILL-EBG.2 coevaluation as boundary glue
  A proposal uses coevaluation L -> M tensor M^vee as the boundary map. This
  is the diagonal class, not the defect-gluing map.

KILL-EBG.3 degree-zero boundary glue as canonical
  A proposal chooses the degree-zero rank-one glue. Over L the boundary map
  has unpinned Laurent unit twists; degree zero is a normalization unless the
  carrier constructs it.

KILL-EBG.4 evaluation-glue package formable on controls
  Evaluation/coevaluation of finite-free support modules and imposed boundary
  self-duality are shadow-level operations. DH/Epstein have not died at a
  carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 28 = doc 165:
  N1B_EVALUATION_BOUNDARY_GLUE__SCALAR_PAIRING_NOT_CARRIER_MAP__NO_GO.

What got built: no new sub-object. The value is a deletion:
evaluation/coevaluation of visible Tate support does not construct the
boundary glue map; the remaining degree/twist choice is still external.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality and Laurent twist/flag/idempotent/line, shift
  operator, selector/functional, and torsor splitter, with DH/Epstein death at
  that correspondence.
```
