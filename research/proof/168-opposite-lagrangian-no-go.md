# 168 - Opposite Lagrangians are graph choices, not carrier glue

Status: no-go + opposite/transverse Lagrangian graph repair deletion,
2026-06-20. Thirty-first cycle of the doc-137 construction arc. Doc 167
killed support Lagrangian/polarization data as carrier half-identification:
standard Tate halves do not identify each other, Lagrangian/graph choices
overproduce, and a Lagrangian is a submodule rather than a rank-one boundary
map or Laurent generator. This document tests the next repair: fix one
standard half and choose an opposite/transverse Lagrangian, then read the
graph map as the half-identification.

Witness, lead-reran this cycle:
`prime_int_n1b_opposite_lagrangian_no_go` (OPL1-OPL13 ALL PASS) -- exact
finite-window graph/opposite-Lagrangian, half-matching, rank mismatch,
boundary-glue, twist, selector, obstruction, and control-formability checks.

## 1. Purpose

After doc 167, the Lagrangian repair can narrow itself:

```text
do not choose an arbitrary Lagrangian;
fix one standard Tate half;
choose a transverse/opposite Lagrangian;
use the resulting graph map as the half-identification.
```

This is sharper than merely choosing a half, but it still starts from the
visible support Tate module. In that model, an opposite Lagrangian is a graph
choice. The graph may be read as a half-map, but the missing R1 datum is more
specific:

```text
dual boundary line -> primal boundary line,
```

plus the Laurent twist that makes this map the carrier shift. A graph
Lagrangian is a global rank-r half-map. It is not the rank-one boundary glue,
not a Laurent generator, and not a torsor splitter.

This document is local. It does not reject carrier-native opposite
Lagrangians. It rejects only opposite/transverse graph choices formed inside
the visible support Tate package.

## 2. Lemma

```text
Lemma 168.1 (support opposite Lagrangians are graph choices, not carrier glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

Fixing a standard half turns a transverse/opposite Lagrangian into a graph
choice. The number of graph choices in the finite F_2 hyperbolic model is:

  64,1024,2097152,36028797018963968.

These graph choices are not carrier maps. Reading one as a half-map still
requires matching data between the two halves; coordinate matching counts are:

  6,24,720,3628800.

The graph output has rank:

  3,4,6,10.

The missing boundary glue rank is:

  1,1,1,1.

Thus the graph output is a global half-map, not the rank-one boundary glue.
It is also not a Laurent generator.

Laurent unit twists in windows |k|<=1,2,4,8 remain:

  3,5,9,17.

Boundary endpoint-pair choices remain:

  9,16,36,100.

Rank-one idempotent counts in the doubled Tate windows remain:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native graph, no
carrier-native boundary glue, no pinned Laurent twist, and no torsor splitter.
The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same opposite-Lagrangian graph
package is formable on controls.

Therefore support opposite/transverse Lagrangian data is not
construction-grade R1 carrier half-identification. A surviving route must
construct the opposite graph, boundary glue, and Laurent twist as
carrier-native correspondence data and prove DH/Epstein death at that
construction.
```

Verdict label:

```text
N1B_OPPOSITE_LAGRANGIAN__GRAPH_CHOICE_NOT_CARRIER_HALF_IDENTIFICATION__NO_GO.
```

## 3. Proof

`prime_int_n1b_opposite_lagrangian_no_go` verifies the finite-window models.

OPL1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

OPL2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

OPL3 records the type of the proposed repair:

```text
fixed standard half + opposite Lagrangian = graph choice,
not carrier-supplied graph map.
```

OPL4 records graph/opposite Lagrangian counts:

```text
64,1024,2097152,36028797018963968.
```

OPL5 records the matching data still needed for graph half-maps:

```text
6,24,720,3628800.
```

It also records that no carrier-supplied nondegeneracy or transversality
filter has been constructed.

OPL6 records the rank mismatch:

```text
graph half-map rank = 3,4,6,10,
boundary glue rank  = 1,1,1,1.
```

OPL7 records that the opposite graph is not a Laurent generator.

OPL8 records endpoint-pair choices:

```text
9,16,36,100.
```

OPL9 records Laurent unit twist choices:

```text
3,5,9,17.
```

OPL10 records rank-one idempotent choices in Tate windows:

```text
2016,32640,8386560,549755289600.
```

OPL11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

OPL12 applies the carrier guard: opposite graphs in finite hyperbolic support
modules are shadow-level data, so controls can form the same package.
OPL13 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-168:

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
      half-identification or boundary glue (doc 168).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, half-identification,
      and Laurent twist/flag/idempotent/line, selector/functional/shift
      operator, torsor splitter, and weight>=1 datum from carrier data, and
      where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Opposite/transverse Lagrangian data is admissible only if
the carrier constructs the graph, boundary glue, and Laurent twist. Support
opposite graphs alone are bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-OPL.1 standard opposite Lagrangian as half-identification
  A proposal fixes one standard Tate half and chooses an opposite half. This
  only turns the repair into a graph choice; the graph is not carrier-supplied.

KILL-OPL.2 graph Lagrangian as carrier map
  A proposal reads the opposite Lagrangian graph as the carrier map. Graph
  choices overproduce and still require half-matching data.

KILL-OPL.3 graph half-map as boundary glue or Laurent shift
  A proposal uses the graph half-map as the boundary glue or shift. The graph
  has rank r; the missing boundary glue is rank one, and the Laurent twist is
  still unpinned.

KILL-OPL.4 opposite-Lagrangian package formable on controls
  Opposite graph choices and matching normalizations are shadow-level
  operations. DH/Epstein have not died at a carrier-consuming correspondence
  map.
```

## 6. Board

```text
doc-137 R1, cycle 31 = doc 168:
  N1B_OPPOSITE_LAGRANGIAN__GRAPH_CHOICE_NOT_CARRIER_HALF_IDENTIFICATION__NO_GO.

What got built: no new sub-object. The value is a deletion: support
opposite/transverse Lagrangians are graph choices, but do not construct the
rank-one boundary glue, Laurent twist, or torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, half-identification,
  and Laurent twist/flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
