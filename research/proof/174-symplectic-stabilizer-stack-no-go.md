# 174 - Symplectic stabilizer stacks are residual isotropy, not carrier loops

Status: no-go + symplectic stabilizer-stack repair deletion, 2026-06-20.
Thirty-seventh cycle of the doc-137 construction arc. Doc 173 killed the
set-level Sp quotient/orbit-average of the support Darboux-frame package:
the quotient has one orbit but no representative, and the F_2 transfer is
zero. This document tests the next repair: keep the quotient as a stack or
action groupoid and use the residual stabilizer/parabolic isotropy as the
missing carrier loop data.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_stabilizer_stack_no_go` (SSK1-SSK12 ALL PASS) --
exact finite-window Sp-order, stabilizer, parabolic, graph/type, endpoint,
idempotent, twist, obstruction, and control-formability checks.

## 1. Purpose

After doc 173, the support-symplectic repair can say:

```text
do not take only the set of Sp-orbits;
keep the action groupoid / homotopy quotient / quotient stack;
use the stabilizer of a frame, first pair, or endpoint vector as carrier
isotropy and the source of Laurent loops.
```

This is not doc 157's repair. Doc 157 killed attaching `Z` isotropy to the
support-chain groupoid. Here the isotropy is not arbitrary `Z`; it is the
actual residual stabilizer of the finite symplectic action after docs
172-173. The question is whether that residual stack data constructs the
R1 endpoint, boundary map, Laurent generator, or torsor splitter.

It does not. The full-frame action is simply transitive, so the quotient
stack has trivial stabilizer. The ordered first-pair action has finite
residual stabilizer `Sp(2r-2,F_2)`. The endpoint-vector action has a large
finite parabolic stabilizer. Reading any concrete stabilizer still requires
a support basepoint; finite residual isotropy is not an infinite Laurent
shift; and the graph, endpoint, matching, idempotent, twist, bottom, shear,
and torsor obstructions remain.

This document is local. It does not reject carrier-native quotient stacks,
descent data, or isotropy. It rejects only the quotient stack of the visible
support Darboux-frame action.

## 2. Lemma

```text
Lemma 174.1 (support Sp stabilizers are residual automorphisms).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

The Sp(W_N) group orders are:

  1451520,
  47377612800,
  208114637736580743168000,
  1132992015386677099994486205757869431795095310094129168384000000.

The ordered symplectic-pair counts are:

  2016,32640,8386560,549755289600.

The quotient stack of full symplectic frames has trivial stabilizer:

  1,1,1,1.

Thus the full-frame stack supplies no loop data.

The quotient stack of ordered first symplectic pairs has residual stabilizer
Sp(2r-2,F_2), with orders:

  720,
  1451520,
  24815256521932800,
  2060902435720151186326095525680721766346957783040000.

The quotient stack of nonzero endpoint vectors has finite parabolic
stabilizer. The nonzero endpoint-vector counts are:

  63,255,4095,1048575,

and the corresponding stabilizer orders are:

  23040,
  185794560,
  50821645356918374400,
  1080506416218846625176535970968094253434513802154475520000.

These stabilizers are finite automorphism groups of already chosen support
objects. Identifying a concrete stabilizer requires a support basepoint; the
stack itself does not select the frame, first pair, endpoint vector, graph,
boundary map, Laurent generator, or torsor splitter.

The graph, endpoint/matching, idempotent, and Laurent-twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600;
  Laurent twists:         3,5,9,17.

The package constructs no DMP multiplication, no carrier-native stabilizer
isotropy, no carrier-native endpoint, no carrier-native boundary glue, no
infinite Laurent shift, no pinned Laurent twist, and no torsor splitter. The
bottom obstruction remains y^2=0, there is still no DMP degree -2, the shear
obstruction remains res_1(c)=1, and the same stabilizer-stack package is
formable on controls.

Therefore the support Sp quotient stack is not construction-grade R1
carrier isotropy or boundary glue. A surviving route must construct the
stack/isotropy, endpoint, boundary map, Laurent twist, and torsor splitter
as carrier-native correspondence data and prove DH/Epstein death at that
construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_STABILIZER_STACK__RESIDUAL_ISOTROPY_NOT_CARRIER_LOOP__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_stabilizer_stack_no_go` verifies the finite-window
model.

SSK1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SSK2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SSK3 records the Sp group orders and first-pair counts:

```text
Sp orders =
1451520,
47377612800,
208114637736580743168000,
1132992015386677099994486205757869431795095310094129168384000000;

ordered symplectic pairs =
2016,32640,8386560,549755289600.
```

SSK4 records that the full symplectic-frame stack has trivial stabilizer:

```text
1,1,1,1.
```

Since there is no residual automorphism group, the full-frame stack supplies
no loop data.

SSK5 records that the ordered first-pair stack has finite residual
`Sp(2r-2,F_2)` stabilizer:

```text
720,
1451520,
24815256521932800,
2060902435720151186326095525680721766346957783040000.
```

These are finite groups, not an infinite Laurent shift.

SSK6 records the endpoint-vector stack. The nonzero vector counts are:

```text
63,255,4095,1048575.
```

The finite parabolic stabilizer orders are:

```text
23040,
185794560,
50821645356918374400,
1080506416218846625176535970968094253434513802154475520000.
```

SSK7 records the basepoint defect: identifying a concrete stabilizer as a
group requires choosing a support frame, first pair, or endpoint vector. The
stack does not choose its own representative and does not output an endpoint.

SSK8 records that the stabilizer stack does not construct the boundary map,
Laurent generator, or torsor splitter.

SSK9 records that the graph, endpoint, matching, idempotent, and twist
choices remain:

```text
graph choices = 64,1024,2097152,36028797018963968;
endpoint pairs = 9,16,36,100;
half matchings = 6,24,720,3628800;
rank-one idempotents = 2016,32640,8386560,549755289600;
Laurent twists = 3,5,9,17.
```

SSK10 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SSK11 applies the carrier guard: stabilizers of finite hyperbolic support
actions are support operations, so controls can form the same package. SSK12
records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-174:

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
      carrier endpoint, half-identification, or boundary glue (doc 172);
    - Sp-quotient/orbit averaging of the support Darboux-frame package as
      carrier endpoint, boundary glue, or Laurent twist (doc 173);
    - quotient-stack/stabilizer isotropy of the support Darboux-frame package
      as carrier endpoint, loop, boundary glue, or Laurent twist (doc 174).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy descent data, quadratic refinement
      or Maslov datum, orientation, half-identification, boundary endpoint,
      and Laurent twist/flag/idempotent/line, selector/functional/shift
      operator, torsor splitter, and weight>=1 datum from carrier data, and
      where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Symplectic stack/isotropy data is admissible only if the
carrier constructs it together with the endpoint, boundary map, Laurent
twist, and torsor splitter. Residual support stabilizers alone are
bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SSK.1 full-frame quotient stack as carrier loop data
  A proposal keeps the full symplectic-frame quotient stack. The full-frame
  action is simply transitive, so the residual stabilizer is trivial.

KILL-SSK.2 first-pair stabilizer as carrier isotropy
  A proposal uses the stabilizer of an ordered symplectic pair. The
  stabilizer is finite Sp(2r-2,F_2), requires a support basepoint to
  identify, and is not an infinite Laurent shift.

KILL-SSK.3 endpoint-vector parabolic as boundary glue
  A proposal uses the parabolic stabilizer of an endpoint vector. This
  again requires an endpoint choice and constructs no boundary map,
  Laurent generator, or torsor splitter.

KILL-SSK.4 symplectic stabilizer-stack package formable on controls
  Stabilizers of finite hyperbolic support actions are support operations.
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 37 = doc 174:
  N1B_SYMPLECTIC_STABILIZER_STACK__RESIDUAL_ISOTROPY_NOT_CARRIER_LOOP__NO_GO.

What got built: no new sub-object. The value is a deletion: the support
symplectic quotient stack either has trivial full-frame stabilizer or finite
residual stabilizer/parabolic data attached to already chosen support
objects. It still does not construct the carrier graph, boundary endpoint,
rank-one boundary map, Laurent twist, Laurent loop, or torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
  symplectic quotient/stack/isotropy descent data, quadratic refinement or
  Maslov datum, orientation, half-identification, boundary endpoint, and
  Laurent twist/flag/idempotent/line, shift operator, selector/functional,
  and torsor splitter, with DH/Epstein death at that correspondence.
```
