# 180 - Schubert convolution is not carrier-supplied correspondence

Status: no-go + symplectic affine Grassmannian / Schubert convolution repair
deletion, 2026-06-20. Forty-third cycle of the doc-137 construction arc.
Doc 179 killed appending affine Weyl/Hecke translation lattices to the
support building. This document tests the next repair: use the affine
Grassmannian or geometric-Satake-style Schubert convolution category as the
missing carrier correspondence algebra.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_affine_grassmannian_no_go` (SAG1-SAG13 ALL PASS)
-- exact finite-window support rank, residual stabilizer, finite
Weyl/Hecke/affine data, dominant-coweight monoid, Schubert-label count,
axis-choice, obstruction, and control-formability checks.

## 1. Purpose

After doc 179, the support-symplectic repair can say:

```text
do not merely append the affine translation lattice;
use the affine Grassmannian;
Schubert convolution supplies correspondences;
geometric Satake turns the support-building data into the carrier algebra.
```

This is distinct from doc 179. The tested object is not just the affine
translation lattice, but the Schubert convolution package indexed by
dominant coweights.

The repair is tempting because Schubert convolution is genuinely
correspondence-like. But the finite support building supplies no loop
parameter, no affine valuation, no affine Grassmannian, and no convolution
category. Once inserted, Schubert strata are indexed by the rank-m dominant
coweight monoid:

```text
N^m,  m = 2,3,5,9.
```

That is not a rank-one Laurent line. Choosing one Schubert direction,
fundamental coweight, or primitive coweight axis is another support choice
unless the carrier correspondence constructs it.

This document is local. It does not reject carrier-native affine
Grassmannians, geometric Satake, loop-group correspondences, or Schubert
convolution. It rejects only reading those structures off from the visible
finite support symplectic building as the R1 correspondence algebra.

## 2. Lemma

```text
Lemma 180.1 (support Schubert convolution is external affine data).
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

The finite and affine data before Schubert insertion is unchanged:

  |W(C_m)|:                    8,48,3840,185794560;
  finite longest lengths:      4,9,25,81;
  Coxeter orders:              4,6,10,18;
  affine translation ranks:    2,3,5,9;
  affine simple-generator cts: 3,4,6,10.

Affine-Grassmannian Schubert labels are dominant coweights. For rank m this
is a rank-m monoid, not a rank-one Laurent axis:

  dominant coweight ranks: 2,3,5,9.

In the finite height windows N=1,2,4,8, the number of dominant coweights of
height at most N is:

  3,10,126,24310.

The number of dominant coweights of exact height N is:

  2,6,70,12870.

The fundamental coweight axis choices are:

  2,3,5,9.

The signed simple-axis choices are:

  4,6,10,18.

Thus Schubert convolution, once inserted, overproduces labels and still does
not select one Laurent generator. The finite support building supplies no
loop parameter, no affine valuation, no affine Grassmannian, no Schubert
convolution category, no boundary map, no Laurent generator, and no torsor
splitter.

The building, Weyl, finite Hecke, affine, and Steinberg obstructions remain:

  building top degrees: 1,2,4,8;
  chamber counts:       45,2835,739552275,852369269595510700600441875;
  Steinberg dimensions: 16,512,33554432,2417851639229258349412352;
  finite Hecke ranks:   8,48,3840,185794560;
  affine ranks:         2,3,5,9.

The graph, endpoint/matching, idempotent, and twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600;
  Laurent twists:         3,5,9,17.

The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same affine Grassmannian /
Schubert convolution package is formable on controls.

Therefore support affine Grassmannian / Schubert convolution data is not
construction-grade R1 carrier correspondence algebra or Laurent boundary
glue. A surviving route must construct the loop parameter, affine valuation,
affine Grassmannian, Schubert convolution category, selected Laurent axis,
endpoint, boundary map, Laurent twist, and torsor splitter as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_AFFINE_GRASSMANNIAN__SCHUBERT_CONVOLUTION_NOT_CARRIER_CORRESPONDENCE__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_affine_grassmannian_no_go` verifies the
finite-window model.

SAG1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SAG2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SAG3 records the residual first-pair stabilizers. They are finite
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

SAG4 records the finite Weyl/Hecke and affine data inherited from docs
177-179.

SAG5 records that Schubert labels form a rank-m dominant coweight monoid:

```text
2,3,5,9.
```

Group completion gives the same ranks, not one rank-one Laurent axis.

SAG6 records the finite height-window Schubert-label counts:

```text
height <= N: 3,10,126,24310;
height  = N: 2,6,70,12870.
```

SAG7 records that selecting one Schubert/Laurent axis is still a support
choice.

SAG8 records that the loop parameter, affine valuation, affine
Grassmannian, and Schubert convolution category are not supplied by the
finite support building.

SAG9 records that Schubert convolution data does not construct the boundary
map, Laurent generator, or torsor splitter.

SAG10 records that the building/Weyl/Hecke/affine/Steinberg finite-data
obstructions remain.

SAG11 records that graph, endpoint, matching, idempotent, and twist choices
remain.

SAG12 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SAG13 applies the carrier guard: appending affine Grassmannian / Schubert
convolution data to support-building data is formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-180:
  NEWLY CLOSED THIS CYCLE:
    - affine Grassmannian / Schubert convolution data appended to the support
      symplectic building as carrier correspondence algebra, Laurent line,
      boundary glue, or torsor splitter (doc 180).

  PREVIOUSLY CLOSED:
    - docs 138-179 as listed in TODO/HANDOFF, including support-line,
      bottom-class, free-Laurent, selector, path/groupoid, Rees, extension,
      completion, Tate-dual, hyperbolic/Lagrangian, Darboux/symplectic,
      quotient/stack/cohomology/building, Weyl/Coxeter, finite Hecke/Iwahori,
      and affine-translation repairs.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy/cohomology/building/Weyl/Coxeter/
      Hecke/Iwahori/affine-translation/Schubert-convolution descent data,
      quadratic refinement or Maslov datum, orientation, half-identification,
      boundary endpoint, and Laurent twist/flag/idempotent/line,
      selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. Affine Grassmannian / Schubert convolution data is
admissible only if the carrier constructs the loop parameter, affine
valuation, affine Grassmannian, Schubert convolution category, selected
Laurent axis, endpoint, boundary map, Laurent twist, and torsor splitter.
Appending Schubert labels to finite support-building data is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SAG.1 affine Grassmannian as carrier correspondence
  A proposal uses the affine Grassmannian attached to the support building
  as the carrier correspondence space. The finite support building supplies
  no loop parameter, affine valuation, or affine Grassmannian.

KILL-SAG.2 Schubert convolution as carrier multiplication
  A proposal reads Schubert convolution as the missing multiplication. The
  convolution category is not support-supplied; it must be constructed by the
  carrier.

KILL-SAG.3 dominant coweight monoid as Laurent line
  A proposal uses dominant coweights as the Laurent direction. The monoid
  ranks are 2,3,5,9, not one, and finite height windows overproduce labels.

KILL-SAG.4 Schubert/fundamental-coweight selection as carrier endpoint
  A proposal chooses one Schubert class, fundamental coweight, or primitive
  coweight axis to extract a line. This is support choice unless a carrier
  correspondence constructs it.

KILL-SAG.5 geometric-Satake wrapper as proof of carrier nativity
  A proposal invokes geometric Satake or a Satake category after inserting
  the affine Grassmannian. The wrapper does not construct the loop parameter,
  endpoint, boundary map, Laurent twist, or torsor splitter.

KILL-SAG.6 Schubert package formable on controls
  Appending affine Grassmannian / Schubert convolution data to finite
  support-building data is a support operation. DH/Epstein have not died at a
  carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 43 = doc 180:
  N1B_SYMPLECTIC_AFFINE_GRASSMANNIAN__SCHUBERT_CONVOLUTION_NOT_CARRIER_CORRESPONDENCE__NO_GO.

What got built: no new sub-object. The value is a deletion: affine
Grassmannian / Schubert convolution data appended to finite support-building
data does not construct the R1 carrier correspondence algebra or Laurent
boundary glue.

What remains: the route must produce carrier-native loop/affine valuation and
Schubert convolution data together with endpoint, boundary glue, Laurent
twist, and torsor splitting. Appending the Schubert monoid to support data is
not enough.

Next admissible move: either find a carrier-consuming multiplication/
correspondence that constructs affine Grassmannian data internally, or move
to the next deletion test for support-building descent data.
```
