# 169 - Graph corners and determinants do not supply boundary glue

Status: no-go + graph-boundary extraction repair deletion, 2026-06-20.
Thirty-second cycle of the doc-137 construction arc. Doc 168 killed support
opposite/transverse Lagrangian graphs as carrier half-identification because
fixing a standard half only turns the repair into a graph choice, graph
choices overproduce and still require half-matching data, and the graph is a
rank-r half-map rather than rank-one boundary glue or a Laurent generator.
This document tests the next repair: extract a boundary corner, minor,
cofactor, determinant line, or Schur-style scalar from the graph map.

Witness, lead-reran this cycle:
`prime_int_n1b_graph_boundary_extraction_no_go` (GBE1-GBE13 ALL PASS) --
exact finite-window graph-count, endpoint-pair, fixed-corner scalar,
overproduction, determinant/cofactor/Schur, twist, selector, obstruction, and
control-formability checks.

## 1. Purpose

After doc 168, the graph repair can try to localize the rank-r half-map:

```text
do not use the whole graph map;
extract the boundary corner, a minor, a cofactor, a determinant line,
or a Schur complement scalar;
use that scalar as the rank-one boundary glue.
```

This is the obvious way to answer the rank mismatch in doc 168. It still
does not construct the missing R1 datum. The extraction has two failure
modes:

```text
if the endpoint/corner is not fixed, endpoint choices reappear;
if the endpoint/corner is fixed, the extraction reads one scalar bit of an
already chosen graph.
```

The determinant variant is worse for the boundary problem: it is a scalar
shadow of the whole graph and does not pin a boundary direction. Cofactor and
Schur variants still require a boundary decomposition and do not supply the
Laurent twist.

This document is local. It does not reject carrier-native boundary maps. It
rejects only boundary extraction operations applied to the visible support
opposite graph.

## 2. Lemma

```text
Lemma 169.1 (graph boundary extraction is a scalar readout, not carrier glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let a support opposite Lagrangian graph be represented in
the finite F_2 hyperbolic model by a symmetric map M_N -> M_N^vee.

For r=3,4,6,10, graph choices are:

  64,1024,2097152,36028797018963968.

Choosing a boundary corner requires endpoint-pair choices:

  9,16,36,100.

For a fixed endpoint pair, the corner entry is one free scalar bit. The
number of graphs with that fixed corner nonzero is:

  32,512,1048576,18014398509481984.

Across all endpoint pairs, graph-corner extraction choices are:

  576,16384,75497472,3602879701896396800.

The nonzero graph-corner extraction choices are:

  288,8192,37748736,1801439850948198400.

Thus a corner extraction does not construct boundary glue: it either chooses
an endpoint/corner, or it imposes a scalar predicate on an already chosen
graph.

A determinant extraction is scalar shadow data. It does not output a boundary
map and does not pin an endpoint. Cofactor or Schur extraction still requires
endpoint/decomposition data and does not output a Laurent generator.

Laurent unit twists in windows |k|<=1,2,4,8 remain:

  3,5,9,17.

Rank-one idempotent counts in the doubled Tate windows remain:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native graph, no
carrier-native endpoint, no carrier-native boundary glue, no pinned Laurent
twist, and no torsor splitter. The bottom obstruction remains y^2=0, there
is still no DMP degree -2, the shear obstruction remains res_1(c)=1, and the
same graph-boundary extraction package is formable on controls.

Therefore graph-corner/minor/determinant/cofactor/Schur extraction from the
support opposite graph is not construction-grade R1 boundary glue. A
surviving route must construct the graph, endpoint, boundary map, and Laurent
twist as carrier-native correspondence data and prove DH/Epstein death at
that construction.
```

Verdict label:

```text
N1B_GRAPH_BOUNDARY_EXTRACTION__CORNER_SCALAR_NOT_CARRIER_GLUE__NO_GO.
```

## 3. Proof

`prime_int_n1b_graph_boundary_extraction_no_go` verifies the finite-window
models.

GBE1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

GBE2 records graph/opposite Lagrangian choices:

```text
64,1024,2097152,36028797018963968.
```

GBE3 records endpoint-pair choices:

```text
9,16,36,100.
```

and records that no carrier endpoint has been supplied.

GBE4 records the fixed-corner scalar-bit count:

```text
32,512,1048576,18014398509481984.
```

GBE5 records all graph-corner extraction choices:

```text
576,16384,75497472,3602879701896396800.
```

and nonzero graph-corner extraction choices:

```text
288,8192,37748736,1801439850948198400.
```

GBE6 records that a corner scalar is not carrier boundary glue: no carrier
graph has been supplied, the corner reads one scalar bit, and the scalar is
not a boundary map.

GBE7 records that determinant extraction is scalar shadow data, not a
boundary map, and does not pin an endpoint.

GBE8 records that cofactor or Schur extraction still requires endpoint data
and supplies no Laurent generator.

GBE9 records Laurent unit twist choices:

```text
3,5,9,17.
```

GBE10 records rank-one idempotent choices in Tate windows:

```text
2016,32640,8386560,549755289600.
```

GBE11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

GBE12 applies the carrier guard: corner, minor, determinant, cofactor, and
Schur extraction are finite-free support operations, so controls can form the
same package. GBE13 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-169:

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
      support opposite graph as carrier boundary glue (doc 169).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, half-identification,
      boundary endpoint, and Laurent twist/flag/idempotent/line,
      selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. Graph-boundary extraction is admissible only if the carrier
constructs the graph, endpoint, boundary map, and Laurent twist. Support
corners, minors, determinants, cofactors, and Schur complements alone are
bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-GBE.1 boundary corner of opposite graph as carrier glue
  A proposal extracts a boundary corner from the support opposite graph. The
  corner requires endpoint choices; if endpoints are fixed, it reads only one
  scalar bit of an already chosen graph.

KILL-GBE.2 nonzero corner scalar as construction
  A proposal requires the extracted scalar to be nonzero. This is a predicate
  on the graph choice, not a carrier construction, and it still leaves many
  graph-corner candidates.

KILL-GBE.3 determinant/cofactor/Schur scalar as boundary map
  A proposal uses determinant, cofactor, minor, or Schur data as the boundary
  map. Determinants are scalar shadows; cofactors and Schur complements still
  need endpoint/decomposition data and do not supply the Laurent generator.

KILL-GBE.4 graph-boundary extraction package formable on controls
  Corner, minor, determinant, cofactor, and Schur extraction are finite-free
  support operations. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 32 = doc 169:
  N1B_GRAPH_BOUNDARY_EXTRACTION__CORNER_SCALAR_NOT_CARRIER_GLUE__NO_GO.

What got built: no new sub-object. The value is a deletion: support
graph-boundary extraction reads scalar shadows of graph choices, but does not
construct the boundary endpoint, rank-one boundary map, Laurent twist, or
torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, half-identification,
  boundary endpoint, and Laurent twist/flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
