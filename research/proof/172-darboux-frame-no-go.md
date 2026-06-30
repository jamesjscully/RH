# 172 - Darboux frames are basis choices, not carrier boundary glue

Status: no-go + Darboux/symplectic-frame repair deletion, 2026-06-20.
Thirty-fifth cycle of the doc-137 construction arc. Doc 171 killed support
quadratic refinements, Arf invariants, and Maslov/triple-Lagrangian scalars
because they are scalar data that do not construct the graph, endpoint,
boundary map, Laurent generator, or torsor splitter. This document tests the
next repair: choose a Darboux or symplectic frame of the hyperbolic Tate
window, then use frame coordinates to name the endpoint, half-identification,
and boundary map.

Witness, lead-reran this cycle:
`prime_int_n1b_darboux_frame_no_go` (DFR1-DFR12 ALL PASS) -- exact
finite-window symplectic-frame, adapted-Darboux-frame, first-pair,
graph/type, twist, obstruction, and control-formability checks.

## 1. Purpose

After doc 171, the graph-boundary repair can replace scalar symplectic
decoration with a full coordinate system:

```text
choose a Darboux/symplectic frame of W_N = M_N plus M_N^vee;
use the first symplectic pair as the boundary endpoint;
use frame coordinates to identify the halves and read boundary glue.
```

This certainly names endpoints and coordinates. The issue is that it does so
by choosing a support basis. It does not construct the carrier graph, boundary
map, Laurent generator, or torsor splitter. Full symplectic frames massively
overproduce. Even frames adapted to the two standard halves still overproduce
as ordinary `GL_r(F_2)` basis choices.

This document is local. It does not reject carrier-native frames or bases. It
rejects only Darboux/symplectic frames chosen inside the visible finite
support Tate package.

## 2. Lemma

```text
Lemma 172.1 (support Darboux frames are basis choices).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

The number of full symplectic frames in the finite F_2 hyperbolic model is:

  1451520,
  47377612800,
  208114637736580743168000,
  1132992015386677099994486205757869431795095310094129168384000000.

Even if the two standard halves are fixed and the frame is required to be
adapted to them, Darboux frames still occur with counts:

  168,
  20160,
  20158709760,
  366440137299948128422802227200.

Choosing the first symplectic pair is an endpoint-like basis choice. The
ordered symplectic-pair counts are:

  2016,32640,8386560,549755289600.

A Darboux frame outputs a basis. It does not construct the opposite graph.
Graph choices remain:

  64,1024,2097152,36028797018963968.

The frame also does not output a boundary map, Laurent generator, or torsor
splitter.

Endpoint-pair choices remain as carrier data:

  9,16,36,100.

Half-matching choices remain:

  6,24,720,3628800.

Laurent unit twists in windows |k|<=1,2,4,8 remain:

  3,5,9,17.

The package constructs no DMP multiplication, no carrier-native frame, no
carrier-native graph, no carrier-native endpoint, no carrier-native boundary
glue, no pinned Laurent twist, and no torsor splitter. The bottom obstruction
remains y^2=0, there is still no DMP degree -2, the shear obstruction remains
res_1(c)=1, and the same Darboux-frame package is formable on controls.

Therefore support Darboux/symplectic-frame selection is not construction-grade
R1 boundary glue. A surviving route must construct the frame or coordinate
data, endpoint, boundary map, and Laurent twist as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_DARBOUX_FRAME__BASIS_CHOICE_NOT_CARRIER_GLUE__NO_GO.
```

## 3. Proof

`prime_int_n1b_darboux_frame_no_go` verifies the finite-window models.

DFR1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

DFR2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

DFR3 records full symplectic-frame counts:

```text
1451520,
47377612800,
208114637736580743168000,
1132992015386677099994486205757869431795095310094129168384000000.
```

DFR4 records adapted Darboux-frame counts over the two fixed standard halves:

```text
168,
20160,
20158709760,
366440137299948128422802227200.
```

DFR5 records ordered first symplectic-pair choices:

```text
2016,32640,8386560,549755289600.
```

and records that no frame has been supplied by the carrier.

DFR6 records that frame coordinates do not construct the opposite graph:

```text
graph choices = 64,1024,2097152,36028797018963968.
```

DFR7 records that a frame does not construct a boundary map, Laurent
generator, or torsor splitter.

DFR8 records endpoint-pair choices:

```text
9,16,36,100.
```

and half-matching choices:

```text
6,24,720,3628800.
```

DFR9 records Laurent unit twist choices:

```text
3,5,9,17.
```

DFR10 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

DFR11 applies the carrier guard: symplectic/Darboux frames are finite
hyperbolic support-basis operations, so controls can form the same package.
DFR12 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-172:

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
      as carrier endpoint, boundary glue, or Laurent twist (doc 170);
    - quadratic refinement, Arf invariant, or Maslov/triple-Lagrangian scalar
      of the support hyperbolic package as carrier boundary glue (doc 171);
    - Darboux/symplectic-frame selection of the support hyperbolic package as
      carrier endpoint, half-identification, or boundary glue (doc 172).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      quadratic refinement or Maslov datum, orientation, half-identification,
      boundary endpoint, and Laurent twist/flag/idempotent/line,
      selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. Darboux/frame data is admissible only if the carrier
constructs it together with the graph, endpoint, boundary map, and Laurent
twist. Support frame selection alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-DFR.1 full symplectic frame as carrier endpoint
  A proposal chooses a full symplectic frame of the visible hyperbolic support
  window and uses its first pair as the endpoint. Full frames massively
  overproduce and are support basis choices.

KILL-DFR.2 adapted Darboux frame as half-identification
  A proposal chooses a Darboux frame adapted to the two standard halves. Such
  frames still overproduce as GL_r(F_2) choices and do not construct the
  carrier graph or boundary map.

KILL-DFR.3 frame coordinate as Laurent twist
  A proposal uses a frame coordinate as the Laurent boundary twist. A frame
  names coordinates; it does not supply the Laurent generator or torsor
  splitter.

KILL-DFR.4 Darboux-frame package formable on controls
  Symplectic and Darboux frames are finite hyperbolic support-basis
  operations. DH/Epstein have not died at a carrier-consuming correspondence
  map.
```

## 6. Board

```text
doc-137 R1, cycle 35 = doc 172:
  N1B_DARBOUX_FRAME__BASIS_CHOICE_NOT_CARRIER_GLUE__NO_GO.

What got built: no new sub-object. The value is a deletion: support
Darboux/symplectic frames name coordinates but do not construct the graph,
boundary endpoint, rank-one boundary map, Laurent twist, or torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
  quadratic refinement or Maslov datum, orientation, half-identification,
  boundary endpoint, and Laurent twist/flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
