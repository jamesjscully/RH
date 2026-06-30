# 171 - Quadratic refinements and Maslov scalars do not supply boundary glue

Status: no-go + quadratic-refinement / Arf-Maslov repair deletion,
2026-06-20. Thirty-fourth cycle of the doc-137 construction arc. Doc 170
killed determinant-one/orientation normalization of the support opposite
graph because `F_2^*` is trivial, determinant-one is tautological after
invertibility, and orientation supplies scalar shadow data rather than an
endpoint, boundary map, or Laurent generator. This document tests the next
repair: add a quadratic refinement, Arf invariant, or Maslov/triple-Lagrangian
index to pin the graph endpoint or Laurent twist.

Witness, lead-reran this cycle:
`prime_int_n1b_quadratic_refinement_no_go` (QRF1-QRF13 ALL PASS) -- exact
finite-window quadratic-refinement count, Arf split, fixed-half
triple-graph/Maslov overproduction, endpoint/matching, twist, idempotent,
obstruction, and control-formability checks.

## 1. Purpose

After doc 170, the graph-boundary repair can try to replace determinant
orientation with characteristic-two symplectic decoration:

```text
choose a quadratic refinement of the hyperbolic support form;
use its Arf invariant, or a Maslov index of a triple of Lagrangians;
let that scalar pin the boundary endpoint or Laurent twist.
```

This is a real mathematical object, but in the visible support model it is
still only support-level scalar data. Quadratic refinements of a fixed
symplectic `F_2` form form a large affine family. The Arf invariant is one
bit splitting that family; it does not choose the graph, endpoint, boundary
map, Laurent generator, or torsor splitter. A Maslov/triple-Lagrangian
variant has the same type problem: it first requires Lagrangian or graph
inputs, then outputs scalar data.

This document is local. It does not reject carrier-native quadratic
refinements, theta characteristics, or Maslov data. It rejects only
quadratic/Arf/Maslov decoration formed inside the visible support Tate
package.

## 2. Lemma

```text
Lemma 171.1 (support Arf/Maslov data is scalar decoration, not carrier glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

Quadratic refinements of the fixed symplectic form form an affine family of
size:

  64,256,4096,1048576.

The Arf-even counts are:

  36,136,2080,524800.

The Arf-odd counts are:

  28,120,2016,523776.

Thus the Arf invariant is a scalar bit separating two large families. It does
not choose the opposite graph. Graph choices remain:

  64,1024,2097152,36028797018963968.

A fixed-half Maslov/triple-Lagrangian variant over graph Lagrangians requires
two graph inputs before producing a scalar. The graph-pair choices are:

  4096,1048576,4398046511104,1298074214633706907132624082305024.

Neither Arf nor Maslov data outputs an endpoint, a boundary map, or a Laurent
generator.

Endpoint-pair choices remain:

  9,16,36,100.

Half-matching choices remain:

  6,24,720,3628800.

Laurent unit twists in windows |k|<=1,2,4,8 remain:

  3,5,9,17.

Rank-one idempotent counts in the doubled Tate windows remain:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native graph, no
carrier-native quadratic refinement, no carrier-native endpoint, no
carrier-native boundary glue, no pinned Laurent twist, and no torsor splitter.
The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same quadratic-refinement /
Arf-Maslov package is formable on controls.

Therefore support quadratic refinements, Arf invariants, and Maslov scalars
are not construction-grade R1 boundary glue. A surviving route must construct
the refinement or Maslov datum, endpoint, boundary map, and Laurent twist as
carrier-native correspondence data and prove DH/Epstein death at that
construction.
```

Verdict label:

```text
N1B_QUADRATIC_REFINEMENT__ARF_MASLOV_SCALAR_NOT_CARRIER_GLUE__NO_GO.
```

## 3. Proof

`prime_int_n1b_quadratic_refinement_no_go` verifies the finite-window models.

QRF1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

QRF2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

QRF3 records quadratic-refinement counts:

```text
64,256,4096,1048576.
```

QRF4 records the Arf split:

```text
Arf even: 36,136,2080,524800.
Arf odd:  28,120,2016,523776.
```

QRF5 records that the Arf bit does not choose the opposite graph:

```text
graph choices = 64,1024,2097152,36028797018963968.
```

It also records that the quadratic refinement has not been supplied by the
carrier.

QRF6 records fixed-half Maslov/triple graph choices:

```text
4096,1048576,4398046511104,1298074214633706907132624082305024.
```

The Maslov index requires Lagrangian inputs first and then outputs a scalar.

QRF7 records the type mismatch: Arf/Maslov scalar data is not an endpoint,
boundary map, or Laurent generator.

QRF8 records endpoint-pair choices:

```text
9,16,36,100.
```

and half-matching choices:

```text
6,24,720,3628800.
```

QRF9 records Laurent unit twist choices:

```text
3,5,9,17.
```

QRF10 records rank-one idempotent choices in Tate windows:

```text
2016,32640,8386560,549755289600.
```

QRF11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

QRF12 applies the carrier guard: quadratic refinements, Arf bits, and Maslov
scalars are finite hyperbolic support operations, so controls can form the
same package. QRF13 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-171:

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
      of the support hyperbolic package as carrier boundary glue (doc 171).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, quadratic refinement
      or Maslov datum, orientation, half-identification, boundary endpoint,
      and Laurent twist/flag/idempotent/line, selector/functional/shift
      operator, torsor splitter, and weight>=1 datum from carrier data, and
      where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Quadratic/Arf/Maslov data is admissible only if the carrier
constructs it together with the graph, endpoint, boundary map, and Laurent
twist. Support scalar decoration alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-QRF.1 quadratic refinement of support form as carrier glue
  A proposal chooses a quadratic refinement of the visible hyperbolic support
  form. Quadratic refinements form a large affine family and do not choose the
  graph, endpoint, boundary map, or Laurent twist.

KILL-QRF.2 Arf invariant as endpoint or boundary map
  A proposal uses the Arf invariant to pin the endpoint or boundary map. Arf
  is a scalar bit splitting two large families, not an endpoint and not a map.

KILL-QRF.3 Maslov/triple-Lagrangian scalar as Laurent twist
  A proposal uses a Maslov or triple-Lagrangian index as the Laurent boundary
  twist. The index requires Lagrangian inputs first and then outputs scalar
  data, not the Laurent generator.

KILL-QRF.4 quadratic-refinement package formable on controls
  Quadratic refinements, Arf bits, and Maslov scalars are finite hyperbolic
  support operations. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 34 = doc 171:
  N1B_QUADRATIC_REFINEMENT__ARF_MASLOV_SCALAR_NOT_CARRIER_GLUE__NO_GO.

What got built: no new sub-object. The value is a deletion: support
quadratic refinements, Arf invariants, and Maslov/triple-Lagrangian scalars
are scalar bookkeeping and do not construct the boundary endpoint, rank-one
boundary map, Laurent twist, or torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, quadratic refinement or
  Maslov datum, orientation, half-identification, boundary endpoint, and
  Laurent twist/flag/idempotent/line, shift operator, selector/functional,
  and torsor splitter, with DH/Epstein death at that correspondence.
```
