# 186 - Hitchin Picard/Prym fibers do not construct the Laurent carrier

Status: no-go + symplectic Hitchin Picard/Prym repair deletion, 2026-06-20.
Forty-ninth cycle of the doc-137 construction arc. Doc 185 killed using
Hitchin-system, spectral-curve, or cameral-cover data of the appended dual
type-B group as the carrier. This document tests the next repair: use the
abelianized Hitchin fiber, namely the Picard/Prym/Jacobian torsor of the
spectral or cameral cover, as the missing carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_hitchin_picard_prym_no_go` (HPP1-HPP10 ALL PASS)
-- exact finite-window support ranks, residual stabilizers, Hitchin base
ranks, cameral and spectral cover degrees, generic fiber ranks, Picard/Prym
axis choices, missing origin/norm/polarization data, missing support-supplied
inputs, missing boundary/torsor data, residual choices, and
control-formability checks.

## 1. Purpose

After doc 185, the Hitchin repair can say:

```text
The Hitchin base is only invariant data.
Use the generic Hitchin fiber instead.
Picard/Prym/Jacobian torsors are abelian carrier objects.
```

This is distinct from doc 185. The tested object is not only the Hitchin base
or cameral cover, but the abelianized fiber that would normally carry the
integrable-system geometry.

The repair still fails locally. The fiber rank mirrors the group rank
m=2,3,5,9. The Picard/Prym package depends on a base curve, spectral or
cameral cover, norm condition, degree normalization, origin/basepoint, and
polarization data that the finite support building does not supply. Choosing
one abelian direction or one degree component is still a selector.

This document is local. It does not reject carrier-native Jacobian, Picard,
Prym, or Arakelov-geometric data. It rejects only invoking the Hitchin
Picard/Prym fiber after appending dual-group Hitchin data to the finite
support symplectic building.

## 2. Lemma

```text
Lemma 186.1 (support Hitchin Picard/Prym data is not a Laurent carrier).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For N=1,2,4,8, the support ranks are:

  r = 3,4,6,10.

The Tate window ranks are:

  6,8,12,20.

The residual first-pair stabilizer buildings have type C_m with:

  m = 2,3,5,9.

The appended Hitchin data from doc 185 remains:

  Hitchin base ranks: 2,3,5,9;
  cameral cover degrees: 8,48,3840,185794560;
  vector spectral cover degrees: 5,7,11,19.

The generic Hitchin fiber and regular-centralizer torus ranks are:

  2,3,5,9.

Thus the Picard/Prym/Jacobian fiber is rank-m abelian data in this support
model, not a selected Laurent line.

The Picard/Prym package also requires extra data not supplied by support:

  - a base curve;
  - a canonical bundle or line-bundle twist;
  - a spectral or cameral cover;
  - a norm condition for the Prym;
  - a degree normalization / connected component;
  - an origin/basepoint and polarization.

The degree-normalization choices in finite windows are:

  3,5,9,17.

Selecting one abelian direction gives:

  fundamental choices = 2,3,5,9;
  signed choices      = 4,6,10,18.

The finite support building supplies none of the base curve, canonical
bundle, spectral curve, cameral cover, Picard stack, Prym norm data,
preferred Prym axis, carrier boundary map, Laurent generator, or torsor
splitter. The graph/endpoint/idempotent/twist choices and the
bottom/shear/torsor obstructions remain, and the same Picard/Prym package is
formable on controls.

Therefore support Hitchin Picard/Prym data is not construction-grade R1
carrier correspondence algebra or Laurent boundary glue. A surviving route
must construct the base geometry, spectral/cameral cover, Picard/Prym/Jacobian
data if used, selected Laurent axis, endpoint, boundary map, Laurent twist,
and torsor splitter as carrier-native correspondence data and prove
DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_HITCHIN_PICARD_PRYM__RANK_M_EXTERNAL_ABELIAN_FIBER_NOT_LAURENT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_hitchin_picard_prym_no_go` verifies the
finite-window model.

HPP1-HPP3 record the unchanged support ranks, Tate windows, residual
stabilizers, Hitchin base ranks, and cover degrees:

```text
r = 3,4,6,10;
Hitchin base ranks = 2,3,5,9;
cameral degrees = 8,48,3840,185794560;
spectral degrees = 5,7,11,19.
```

HPP4 records that the generic Hitchin/Prym fibers are rank-m abelian data:

```text
2,3,5,9.
```

HPP5 records that the Picard/Prym origin, norm condition, and polarization
are not support-supplied.

HPP6 records that selecting one Picard/Prym axis or degree component is
another choice:

```text
fundamental choices = 2,3,5,9;
signed choices      = 4,6,10,18;
degree choices      = 3,5,9,17.
```

HPP7 records that the base curve, canonical bundle, spectral curve, cameral
cover, Picard stack, and Prym norm data are not support-supplied.

HPP8 records that Picard/Prym data does not construct the shift, boundary map,
or torsor splitter.

HPP9 records that support choices and base obstructions remain: the DMP bottom
class still has no degree -2 support, the support choices persist, and no
carrier multiplication or torsor splitter is supplied.

HPP10 applies the carrier guard: appending Picard/Prym/Jacobian abelian
geometry to finite support data is formable on controls.

## 4. Impact on R1

```text
R1 after docs 138-186:
  NEWLY CLOSED THIS CYCLE:
    - Hitchin Picard/Prym/Jacobian fiber of the appended dual group as carrier
      correspondence algebra, Laurent axis, boundary glue, or torsor splitter
      (doc 186).

  PREVIOUSLY CLOSED:
    - docs 138-185 as listed in TODO/HANDOFF, including support-line,
      bottom-class, free-Laurent, selector, path/groupoid, Rees, extension,
      completion, Tate-dual, hyperbolic/Lagrangian, Darboux/symplectic,
      quotient/stack/cohomology/building, Weyl/Coxeter, finite Hecke/Iwahori,
      affine-translation, Schubert-convolution, Satake-dual,
      principal-cocharacter, Kostant-section, Springer/Steinberg, and
      Hitchin/cameral repairs.

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      constructs any Jacobian/Picard/Prym data internally if such data is used,
      and whose carrier-native map produces the endpoint, boundary map,
      Laurent twist/axis, torsor splitter, shift operator, and weight>=1
      datum while making DH/Epstein controls fail at named points.
```

R1 is still open. Hitchin Picard/Prym data is admissible only if the carrier
constructs the base geometry, cover, norm/origin/polarization data, selected
Laurent axis, endpoint, boundary map, Laurent twist, and torsor splitter.
Invoking the Picard/Prym fiber of an inserted Hitchin system is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-HPP.1 Hitchin Picard/Prym as carrier construction
  A proposal invokes a Picard, Prym, or Jacobian fiber after appending Hitchin
  data to support-building data. The abelian variety/torsor is inserted
  geometry unless the carrier constructs it.

KILL-HPP.2 generic Hitchin fiber as Laurent line
  A proposal reads the generic Hitchin fiber as the line. The fiber has
  rank m in the support model, not a selected rank-one Laurent axis.

KILL-HPP.3 Prym norm or connected component as selector
  A proposal uses norm-zero, degree-zero, or connected-component data as the
  selector. Those data require a cover, norm map, origin, and degree
  normalization not supplied by support.

KILL-HPP.4 Picard degree as Laurent shift
  A proposal reads degree components as the shift. Degree is a chosen
  line-bundle grading on an external curve, not a carrier-native boundary map.

KILL-HPP.5 Picard/Prym data as boundary map or torsor splitter
  A proposal reads abelian group law, polarization, norm, or degree as the
  endpoint, boundary map, Laurent twist, or b/phi(b)=c splitter. The package
  supplies no such map.

KILL-HPP.6 Picard/Prym package formable on controls
  Appending a curve, cover, Picard/Jacobian, Prym norm condition, origin, and
  polarization to finite support data is a support operation. DH/Epstein have
  not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 49 = doc 186:
  N1B_SYMPLECTIC_HITCHIN_PICARD_PRYM__RANK_M_EXTERNAL_ABELIAN_FIBER_NOT_LAURENT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: the
Picard/Prym/Jacobian fiber of an appended Hitchin system cannot be used as
the missing Laurent carrier.

What remains: the route must produce carrier-native base geometry and
Jacobian/Picard/Prym data or leave the Satake-dual branch. Rank-m external
abelian geometry is not enough.
```
