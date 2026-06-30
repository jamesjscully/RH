# 173 - Symplectic quotients are orbit classes, not carrier endpoints

Status: no-go + symplectic quotient/orbit-averaging repair deletion,
2026-06-20. Thirty-sixth cycle of the doc-137 construction arc. Doc 172
killed support Darboux/symplectic-frame selection because a frame is a basis
choice, not carrier boundary glue. This document tests the next repair:
avoid choosing the frame by quotienting by the symplectic group, or by taking
an invariant/orbit average of the first symplectic pair.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_quotient_no_go` (SPQ1-SPQ11 ALL PASS) -- exact
finite-window Sp-orbit, first-vector transfer, graph/type, endpoint,
idempotent, twist, obstruction, and control-formability checks.

## 1. Purpose

Doc 172 rejects choosing a Darboux frame inside the visible hyperbolic Tate
support package:

```text
choose a symplectic frame of W_N = M_N plus M_N^vee;
use the first symplectic pair as the boundary endpoint.
```

The natural repair is to remove the arbitrary choice:

```text
take the Sp(W_N)-orbit of the frame or first pair;
use the quotient class, invariant predicate, or orbit average as the
canonical endpoint/boundary glue.
```

This is not the doc-153 GL_r idempotent-orbit no-go. Doc 153 killed symmetry
as a selector for rank-one idempotents in the support End envelope. Here the
target is the post-doc-172 hyperbolic support package: Darboux frames and
ordered symplectic pairs under the symplectic group.

The quotient does what it should as a quotient: it collapses the frame or
first-pair family to a single orbit. But a single orbit is not a chosen
representative, endpoint, graph, boundary map, Laurent generator, or torsor
splitter. Over F_2 there is also no normalized averaging by |Sp|, and the
natural additive transfer/orbit sum of endpoint vectors is zero.

This document is local. It does not reject carrier-native symplectic
quotients, orbit objects, or descent data. It rejects only quotienting or
averaging the visible support Darboux-frame package.

## 2. Lemma

```text
Lemma 173.1 (support symplectic quotients do not select boundary glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

The full symplectic-frame counts are:

  1451520,
  47377612800,
  208114637736580743168000,
  1132992015386677099994486205757869431795095310094129168384000000.

The adapted Darboux-frame counts over the fixed standard halves are:

  168,
  20160,
  20158709760,
  366440137299948128422802227200.

The ordered symplectic-pair counts are:

  2016,32640,8386560,549755289600.

Sp(W_N) acts transitively on full symplectic frames and on ordered
symplectic pairs, so the quotient has one orbit in each tested window:

  1,1,1,1.

That orbit class does not choose a representative. It therefore does not
construct a carrier endpoint, opposite graph, boundary map, Laurent
generator, or torsor splitter.

The nonzero endpoint-vector orbit sizes in the finite F_2 model are:

  63,255,4095,1048575.

For each coordinate, the number of nonzero endpoint vectors with that
coordinate equal to 1 is:

  32,128,2048,524288.

Hence the additive F_2 orbit transfer of endpoint vectors is zero in all
tested windows. Weighting by the number of partners b with <a,b>=1 gives
coordinate counts:

  1024,16384,4194304,274877906944,

again zero mod 2. The quotient/transfer therefore supplies no nonzero
rank-one boundary vector.

The graph, endpoint/matching, idempotent, and Laurent-twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600;
  Laurent twists:         3,5,9,17.

The package constructs no DMP multiplication, no carrier-native quotient
descent, no carrier-native endpoint, no carrier-native boundary glue, no
pinned Laurent twist, and no torsor splitter. The bottom obstruction remains
y^2=0, there is still no DMP degree -2, the shear obstruction remains
res_1(c)=1, and the same quotient/averaging package is formable on controls.

Therefore support Sp-quotient/orbit averaging is not construction-grade R1
boundary glue. A surviving route must construct the quotient/orbit object,
endpoint, boundary map, Laurent twist, and torsor splitter as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_QUOTIENT__ORBIT_CLASS_NOT_CARRIER_ENDPOINT__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_quotient_no_go` verifies the finite-window model.

SPQ1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SPQ2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SPQ3 records the doc-172 frame and first-pair counts:

```text
full symplectic frames =
1451520,
47377612800,
208114637736580743168000,
1132992015386677099994486205757869431795095310094129168384000000;

adapted Darboux frames =
168,
20160,
20158709760,
366440137299948128422802227200;

ordered symplectic pairs =
2016,32640,8386560,549755289600.
```

SPQ4 records that the Sp quotient collapses frames and ordered symplectic
pairs to one orbit:

```text
1,1,1,1.
```

It also records that the quotient does not select a representative.

SPQ5 records that invariant predicates see only the orbit class and do not
construct the endpoint, graph, boundary map, Laurent generator, or torsor
splitter.

SPQ6 records the first-vector orbit transfer over F_2. The nonzero vector
counts are:

```text
63,255,4095,1048575.
```

Each coordinate occurs:

```text
32,128,2048,524288
```

times among nonzero endpoint vectors, so the F_2 transfer is zero. Since
|Sp(W_N)| is even, there is no normalized F_2 average by the group order.

SPQ7 records that the ordered-pair first-vector transfer is also zero. Each
first vector has:

```text
32,128,2048,524288
```

possible partners b with <a,b>=1. The weighted coordinate counts are:

```text
1024,16384,4194304,274877906944,
```

again zero mod 2.

SPQ8 records that the graph, endpoint, matching, idempotent, and twist
choices remain:

```text
graph choices = 64,1024,2097152,36028797018963968;
endpoint pairs = 9,16,36,100;
half matchings = 6,24,720,3628800;
rank-one idempotents = 2016,32640,8386560,549755289600;
Laurent twists = 3,5,9,17.
```

SPQ9 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SPQ10 applies the carrier guard: Sp-orbit quotients and F_2 transfers are
finite hyperbolic support operations, so controls can form the same package.
SPQ11 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-173:

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
      carrier endpoint, boundary glue, or Laurent twist (doc 173).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/orbit descent data, quadratic refinement or Maslov
      datum, orientation, half-identification, boundary endpoint, and Laurent
      twist/flag/idempotent/line, selector/functional/shift operator, torsor
      splitter, and weight>=1 datum from carrier data, and where DH/Epstein
      controls fail before signs, zeros, or comparison.
```

R1 is still open. Symplectic quotient/orbit data is admissible only if the
carrier constructs it together with the endpoint, boundary map, Laurent
twist, and torsor splitter. The support orbit class alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SPQ.1 symplectic quotient class as carrier endpoint
  A proposal takes the Sp-orbit of a support Darboux frame or first
  symplectic pair and calls the orbit class the endpoint. The quotient has
  one orbit, but no representative or carrier endpoint.

KILL-SPQ.2 Sp-invariant predicate as boundary map
  A proposal uses an Sp-invariant predicate to define the boundary map.
  The predicate sees only orbit membership and constructs no graph,
  boundary map, Laurent generator, or torsor splitter.

KILL-SPQ.3 orbit average/transfer as Laurent boundary glue
  A proposal averages or sums the endpoint orbit. Over F_2 there is no
  normalized average by |Sp|, and the natural orbit transfer of endpoint
  vectors is zero.

KILL-SPQ.4 symplectic quotient package formable on controls
  Sp-orbit quotients and F_2 transfers are finite hyperbolic support
  operations. DH/Epstein have not died at a carrier-consuming correspondence
  map.
```

## 6. Board

```text
doc-137 R1, cycle 36 = doc 173:
  N1B_SYMPLECTIC_QUOTIENT__ORBIT_CLASS_NOT_CARRIER_ENDPOINT__NO_GO.

What got built: no new sub-object. The value is a deletion: quotienting or
averaging support Darboux/symplectic frames removes the visible choice only
by replacing it with an orbit class or a zero transfer. It still does not
construct the carrier graph, boundary endpoint, rank-one boundary map,
Laurent twist, or torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
  symplectic quotient/orbit descent data, quadratic refinement or Maslov
  datum, orientation, half-identification, boundary endpoint, and Laurent
  twist/flag/idempotent/line, shift operator, selector/functional, and torsor
  splitter, with DH/Epstein death at that correspondence.
```
