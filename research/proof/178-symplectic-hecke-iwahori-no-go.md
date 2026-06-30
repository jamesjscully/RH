# 178 - Finite Hecke/Iwahori algebras are not the carrier correspondence

Status: no-go + symplectic Hecke/Iwahori/BN-pair repair deletion,
2026-06-20. Forty-first cycle of the doc-137 construction arc. Doc 177
killed using a chosen support-building apartment and Coxeter element as the
missing Laurent shift. This document tests the next repair: package that
apartment descent as the finite type-C Iwahori-Hecke algebra, spherical
Hecke algebra, or BN-pair double-coset algebra of the residual support
symplectic building.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_hecke_iwahori_no_go` (SHI1-SHI13 ALL PASS) --
exact finite-window support rank, residual stabilizer, type-C Weyl/Hecke
basis, Bruhat-length, center-rank, finite/affine distinction,
building/Weyl/Steinberg, choice, obstruction, and control-formability
checks.

## 1. Purpose

After doc 177, the support-symplectic repair can say:

```text
do not choose a single Coxeter element;
use the whole finite Hecke algebra of the support building;
its convolution product is the missing correspondence algebra;
read its generators or center as the carrier shift / Laurent line.
```

This is distinct from docs 176 and 177. The tested object is not a top
building class, a chosen apartment, or one Coxeter rotation. It is the finite
Hecke/Iwahori/BN-pair algebra attached to the residual support building.

The repair is tempting because a Hecke algebra is an actual algebra, and
`End(S^2/Z)` is supposed to be a correspondence algebra. But the finite
support-building Hecke algebra is still finite support data. Its basis is
indexed by the finite Weyl group. Its length filtration has a longest word.
Its center is finite class data. It has no carrier-supplied affine
translation lattice, no bi-infinite Laurent shift, and no boundary glue map.
Choosing the chamber/Borel/Iwahori input is still support data unless the
carrier correspondence constructs it.

This document is local. It does not reject carrier-native Hecke algebras,
affine Hecke algebras, or genuine correspondence algebras. It rejects only
the finite Hecke/Iwahori package read off from the visible support
symplectic building as the R1 correspondence algebra or Laurent carrier.

## 2. Lemma

```text
Lemma 178.1 (finite support Hecke algebras do not supply the carrier).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For N=1,2,4,8, the support ranks are:

  r = 3,4,6,10.

The Tate window ranks are:

  6,8,12,20.

The residual first-pair stabilizer buildings have type C_m with:

  m = 2,3,5,9.

The stabilizer orders are:

  720,
  1451520,
  24815256521932800,
  2060902435720151186326095525680721766346957783040000.

The finite type-C Iwahori-Hecke algebra has basis indexed by W(C_m), so its
ranks are:

  8,48,3840,185794560.

The simple-generator counts are:

  2,3,5,9.

The Coxeter element orders remain finite:

  4,6,10,18.

The longest Bruhat lengths are:

  m^2 = 4,9,25,81.

The center ranks, equivalently the number of conjugacy classes of W(C_m) or
bipartitions of m, are:

  5,10,36,300.

Thus the finite support Hecke algebra is not a rank-one Laurent line, not a
bi-infinite shift algebra, and not the missing boundary map. Its length
filtration terminates at the longest element. Its center is a finite
class-algebra shadow, not a canonical carrier endpoint.

An affine Hecke algebra would require a translation lattice. That lattice is
not supplied by the finite support building; adding it is another external
tail/loop/shift insertion unless a carrier correspondence constructs it.

The building, Weyl, and Steinberg obstructions remain:

  building top degrees: 1,2,4,8;
  chamber counts:       45,2835,739552275,852369269595510700600441875;
  Steinberg dimensions: 16,512,33554432,2417851639229258349412352;
  Weyl group orders:    8,48,3840,185794560.

The graph, endpoint/matching, idempotent, and twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600;
  Laurent twists:         3,5,9,17.

The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same finite Hecke/Iwahori
package is formable on controls.

Therefore support Hecke/Iwahori/BN-pair data is not construction-grade R1
carrier correspondence algebra, monodromy, or Laurent boundary glue. A
surviving route must construct the Hecke/correspondence algebra, endpoint,
boundary map, Laurent twist, affine/translation data if needed, and torsor
splitter as carrier-native correspondence data and prove DH/Epstein death at
that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_HECKE_IWAHORI__FINITE_DOUBLE_COSET_ALGEBRA_NOT_CARRIER_CORRESPONDENCE__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_hecke_iwahori_no_go` verifies the finite-window
model.

SHI1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SHI2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SHI3 records the residual first-pair stabilizers. They are finite
`Sp(2m,F_2)` groups with:

```text
m = 2,3,5,9.
```

and orders:

```text
720,
1451520,
24815256521932800,
2060902435720151186326095525680721766346957783040000.
```

SHI4 records that finite Iwahori-Hecke bases have ranks:

```text
8,48,3840,185794560.
```

These are the type-C Weyl group orders.

SHI5 records the finite generator, Coxeter-order, and length data:

```text
simple generators = 2,3,5,9;
Coxeter orders = 4,6,10,18;
longest Bruhat lengths = 4,9,25,81.
```

The finite Bruhat interval terminates, so it does not construct a
bi-infinite Laurent shift.

SHI6 records the center ranks:

```text
5,10,36,300.
```

These are finite class-data ranks, not canonical Laurent lines.

SHI7 records that affine translations are not supplied by the finite support
building. Passing to an affine Hecke algebra inserts a translation lattice
unless the carrier constructs it.

SHI8 records that the apartment, chamber/Borel, Iwahori subgroup, and Hecke
algebra are not carrier-supplied in this repair.

SHI9 records that Hecke/Iwahori data does not construct the boundary map,
Laurent generator, or torsor splitter.

SHI10 records that the building/Weyl/Steinberg finite-data obstructions
remain.

SHI11 records that the graph, endpoint, matching, idempotent, and twist
choices remain.

SHI12 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SHI13 applies the carrier guard: finite Hecke/Iwahori/BN-pair algebras of
support stabilizer buildings are support operations, so controls can form
the same package.

## 4. Impact on R1

```text
R1 after docs 138-178:

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
      as carrier endpoint, loop, boundary glue, or Laurent twist (doc 174);
    - classifying-space/group/Tate cohomology of the support symplectic
      stabilizers as carrier endpoint, Laurent line, boundary glue, or
      torsor splitter (doc 175);
    - Tits-building/Steinberg dualizing data of the support symplectic
      stabilizers as carrier endpoint, Laurent line, boundary glue, or
      torsor splitter (doc 176);
    - finite Weyl/Coxeter/apartment monodromy of the support symplectic
      building as carrier monodromy, Laurent shift, boundary glue, or torsor
      splitter (doc 177);
    - finite Hecke/Iwahori/BN-pair double-coset algebra of the support
      symplectic building as carrier correspondence algebra, monodromy,
      Laurent line, boundary glue, or torsor splitter (doc 178).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy/cohomology/building/Weyl/Coxeter/
      Hecke/Iwahori descent data, quadratic refinement or Maslov datum,
      orientation, half-identification, boundary endpoint, and Laurent
      twist/flag/idempotent/line, selector/functional/shift operator, torsor
      splitter, and weight>=1 datum from carrier data, and where DH/Epstein
      controls fail before signs, zeros, or comparison.
```

R1 is still open. Hecke/Iwahori/BN-pair data is admissible only if the
carrier constructs the correspondence algebra together with endpoint,
boundary map, Laurent twist, affine/translation data if needed, and torsor
splitter. Finite support-building double-coset algebra alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SHI.1 finite Iwahori-Hecke algebra as carrier correspondence
  A proposal uses the finite Hecke algebra of the residual support building
  as End(Xbar). Its basis is indexed by the finite Weyl group, so it is a
  finite support algebra, not the carrier correspondence algebra.

KILL-SHI.2 Hecke generator as Laurent shift
  A proposal uses a Hecke generator or Coxeter-word action as the missing
  shift. The finite Bruhat interval has a longest element and supplies no
  bi-infinite Laurent generator.

KILL-SHI.3 Hecke center as carrier line
  A proposal reads the center or class algebra as the endpoint line. The
  center ranks are 5,10,36,300, finite class-data ranks rather than a
  canonical Laurent line.

KILL-SHI.4 affine Hecke translation insertion
  A proposal repairs the finite Hecke algebra by passing to an affine Hecke
  algebra. The translation lattice is not supplied by the finite support
  building; it must be constructed by the carrier, not inserted.

KILL-SHI.5 chamber/Borel/Iwahori selection as carrier data
  A proposal chooses a chamber, Borel, Iwahori subgroup, or double-coset
  normalization to extract the line. This is support choice unless a carrier
  correspondence constructs it.

KILL-SHI.6 Hecke/Iwahori package formable on controls
  Finite Hecke/Iwahori/BN-pair algebras of support stabilizer buildings are
  support operations. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 41 = doc 178:
  N1B_SYMPLECTIC_HECKE_IWAHORI__FINITE_DOUBLE_COSET_ALGEBRA_NOT_CARRIER_CORRESPONDENCE__NO_GO.

What got built: no new sub-object. The value is a deletion: finite
Hecke/Iwahori/BN-pair double-coset algebra of the support symplectic
building does not construct the R1 carrier correspondence algebra or Laurent
shift.

What remains: the route must produce carrier-native correspondence data that
constructs Hecke/Iwahori or affine translation data together with endpoint,
boundary glue, Laurent twist, and torsor splitting. Finite support-building
double-coset algebra is not enough.

Next admissible move: either find a carrier-consuming multiplication/
correspondence that constructs Hecke/affine data internally, or move to the
next deletion test for support-building descent data.
```
