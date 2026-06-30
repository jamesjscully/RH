# 170 - Orientation normalization does not pin the graph boundary

Status: no-go + determinant/orientation normalization repair deletion,
2026-06-20. Thirty-third cycle of the doc-137 construction arc. Doc 169
killed graph-boundary extraction from the support opposite graph because
corners reintroduce endpoint choices or read one scalar bit of an already
chosen graph, determinant data is scalar shadow data, and cofactor/Schur
variants still need endpoint data and no Laurent generator is supplied. This
document tests the next repair: add determinant-one or orientation
normalization to the graph/boundary package and claim that the normalization
pins the endpoint or Laurent twist.

Witness, lead-reran this cycle:
`prime_int_n1b_orientation_normalization_no_go` (ONR1-ONR13 ALL PASS) --
exact finite-window determinant-unit, orientation, determinant-one,
endpoint/matching, twist, idempotent, obstruction, and control-formability
checks.

## 1. Purpose

After doc 169, the graph-boundary repair can try to add one more canonical
normalization:

```text
choose an orientation of the graph or determinant line;
impose determinant one;
use that normalized orientation to pin the boundary endpoint or Laurent
twist.
```

In the finite support windows this does not supply new structure. The
determinant unit group is

```text
F_2^* = {1}.
```

Thus determinant-one orientation is tautological once invertibility is
assumed. It cannot distinguish endpoints, cannot construct a boundary map,
and cannot supply the Laurent generator. If one passes to a Laurent
determinant degree, that is still total scalar data for the graph; it is not
the rank-one boundary twist.

This document is local. It does not reject carrier-native orientations or
determinant data. It rejects only orientation/determinant normalization
formed inside the visible support graph package.

## 2. Lemma

```text
Lemma 170.1 (support determinant orientation is tautological over F_2).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let a support opposite Lagrangian graph be represented in
the finite F_2 hyperbolic model by a symmetric map M_N -> M_N^vee.

For r=3,4,6,10, graph choices remain:

  64,1024,2097152,36028797018963968.

The determinant unit group in the finite F_2 model has size:

  1.

Therefore orientation unit choices in every tested window are:

  1,1,1,1.

There are no determinant sign bits:

  0,0,0,0.

Consequently determinant-one normalization is tautological after invertibility:
over F_2 every nonzero determinant equals 1.

Orientation normalization outputs scalar shadow data, not an endpoint and not
a boundary map. It is also not a Laurent generator. Laurent determinant-degree
normalization, if imposed, is only total scalar data; it is not the boundary
twist.

Endpoint-pair choices remain:

  9,16,36,100.

Half-matching choices remain:

  6,24,720,3628800.

Laurent unit twists in windows |k|<=1,2,4,8 remain:

  3,5,9,17.

Rank-one idempotent counts in the doubled Tate windows remain:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native graph, no
carrier-native endpoint, no carrier-native boundary glue, no pinned Laurent
twist, and no torsor splitter. The bottom obstruction remains y^2=0, there
is still no DMP degree -2, the shear obstruction remains res_1(c)=1, and the
same orientation-normalization package is formable on controls.

Therefore determinant-one/orientation normalization of the support opposite
graph is not construction-grade R1 boundary glue. A surviving route must
construct the orientation, endpoint, boundary map, and Laurent twist as
carrier-native correspondence data and prove DH/Epstein death at that
construction.
```

Verdict label:

```text
N1B_ORIENTATION_NORMALIZATION__DETERMINANT_ONE_TAUTOLOGICAL_NOT_CARRIER_GLUE__NO_GO.
```

## 3. Proof

`prime_int_n1b_orientation_normalization_no_go` verifies the finite-window
models.

ONR1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

ONR2 records graph/opposite Lagrangian choices:

```text
64,1024,2097152,36028797018963968.
```

ONR3 records that F_2 determinant orientation has no sign:

```text
|F_2^*| = 1,
orientation choices = 1,1,1,1,
determinant sign bits = 0,0,0,0.
```

ONR4 records that determinant-one normalization is tautological after
invertibility:

```text
over F_2, every nonzero determinant equals 1.
```

ONR5 records that orientation normalization supplies no endpoint or boundary
map.

ONR6 records that orientation normalization supplies no Laurent generator.

ONR7 records that Laurent determinant-degree normalization is only total
scalar data, not a boundary twist.

ONR8 records endpoint-pair choices:

```text
9,16,36,100.
```

and half-matching choices:

```text
6,24,720,3628800.
```

ONR9 records Laurent unit twist choices:

```text
3,5,9,17.
```

ONR10 records rank-one idempotent choices in Tate windows:

```text
2016,32640,8386560,549755289600.
```

ONR11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

ONR12 applies the carrier guard: determinant-one and orientation
normalization are finite-free support operations, so controls can form the
same package. ONR13 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-170:

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
    - support hyperbolic form/swap as automatic Tate boundary glue (doc 166);
    - support Lagrangian/polarization as carrier half-identification
      (doc 167);
    - support opposite/transverse Lagrangian graph as carrier
      half-identification or boundary glue (doc 168);
    - boundary corner/minor/determinant/cofactor/Schur extraction from the
      support opposite graph as carrier boundary glue (doc 169);
    - determinant-one/orientation normalization of the support opposite graph
      as carrier endpoint, boundary glue, or Laurent twist (doc 170).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, orientation,
      half-identification, boundary endpoint, and Laurent
      twist/flag/idempotent/line, selector/functional/shift operator, torsor
      splitter, and weight>=1 datum from carrier data, and where DH/Epstein
      controls fail before signs, zeros, or comparison.
```

R1 is still open. Orientation/determinant data is admissible only if the
carrier constructs it together with the graph, endpoint, boundary map, and
Laurent twist. Support determinant normalization alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-ONR.1 determinant-one normalization of support graph as carrier glue
  A proposal imposes determinant one on the support opposite graph. Over F_2
  this is tautological after invertibility and supplies no boundary data.

KILL-ONR.2 orientation as endpoint or boundary map
  A proposal uses support orientation to choose the endpoint or boundary map.
  The orientation output is scalar shadow data, not an endpoint and not a
  map.

KILL-ONR.3 determinant degree as Laurent twist
  A proposal uses total determinant degree as the Laurent boundary twist. This
  is total scalar data of the graph, not the rank-one boundary generator.

KILL-ONR.4 orientation-normalization package formable on controls
  Determinant-one and orientation normalization are finite-free support
  operations. DH/Epstein have not died at a carrier-consuming correspondence
  map.
```

## 6. Board

```text
doc-137 R1, cycle 33 = doc 170:
  N1B_ORIENTATION_NORMALIZATION__DETERMINANT_ONE_TAUTOLOGICAL_NOT_CARRIER_GLUE__NO_GO.

What got built: no new sub-object. The value is a deletion: support
orientation and determinant-one normalization are scalar bookkeeping and do
not construct the boundary endpoint, rank-one boundary map, Laurent twist, or
torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, orientation,
  half-identification, boundary endpoint, and Laurent twist/flag/idempotent/
  line, shift operator, selector/functional, and torsor splitter, with
  DH/Epstein death at that correspondence.
```
