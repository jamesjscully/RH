# 175 - Stabilizer cohomology is not a carrier Laurent line

Status: no-go + symplectic stabilizer-cohomology repair deletion,
2026-06-20. Thirty-eighth cycle of the doc-137 construction arc. Doc 174
killed reading loop data directly from the support Sp quotient-stack
stabilizers. This document tests the next repair: take classifying-space
cohomology, group cohomology, or Tate cohomology of those finite stabilizers
and use a cohomology class as the missing Laurent generator.

Witness, lead-reran this cycle:
`prime_int_n1b_symplectic_stabilizer_cohomology_no_go` (SCH1-SCH13 ALL
PASS) -- exact finite-window stabilizer, elementary-abelian-2-rank,
nonperiodicity, graph/type, endpoint, idempotent, twist, obstruction, and
control-formability checks.

## 1. Purpose

After doc 174, the support-symplectic repair can say:

```text
the residual stabilizer group itself is only finite;
therefore pass to B Stab, H^*(Stab;F_2), or Tate cohomology of Stab;
use a classifying-space/Tate class as the periodic Laurent generator.
```

This is a different repair from doc 174. Doc 174 tested stabilizer isotropy
itself. Here the tested object is cohomological: ordinary group cohomology,
classifying-space cohomology, or finite-group Tate cohomology of the residual
support stabilizer.

The repair fails for two independent reasons. First, ordinary cohomology is
nonnegative and positive-degree classes are not Laurent units. Second, the
tested nontrivial stabilizers are not finite groups with 2-periodic mod-2
cohomology: they contain elementary abelian 2-subgroups of rank at least two.
Thus Tate cohomology of the stabilizer is not a single carrier-supplied
Laurent line. Inverting a chosen cohomology class or imposing periodicity is
another formal localization unless the carrier constructs it.

This document is local. It does not reject carrier-native cohomology,
periodicity, or Tate data. It rejects only cohomology of the visible support
Sp stabilizers as the R1 Laurent carrier.

## 2. Lemma

```text
Lemma 175.1 (support stabilizer cohomology is not the Laurent carrier).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee be the finite hyperbolic support
window.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

The full-frame stabilizer is trivial:

  1,1,1,1.

So full-frame stabilizer cohomology supplies no loop data.

The ordered first-pair stabilizers are Sp(2m,F_2) for:

  m = 2,3,5,9.

Their orders are:

  720,
  1451520,
  24815256521932800,
  2060902435720151186326095525680721766346957783040000.

Their 2-adic orders are:

  2^4, 2^9, 2^25, 2^81.

Each contains an elementary abelian 2-subgroup of rank:

  2,3,5,9.

Hence each contains C_2 x C_2 and does not have 2-periodic mod-2
finite-group cohomology.

The endpoint-vector stabilizers are finite parabolics. The nonzero endpoint
vector counts are:

  63,255,4095,1048575,

and the stabilizer orders are:

  23040,
  185794560,
  50821645356918374400,
  1080506416218846625176535970968094253434513802154475520000.

They contain the same elementary abelian 2-ranks:

  2,3,5,9,

and likewise do not have 2-periodic mod-2 finite-group cohomology.

Ordinary stabilizer cohomology is nonnegative, and positive-degree classes
are not units. Stabilizer Tate cohomology is not a carrier-supplied single
Laurent line in the tested windows. Formal inversion or localization at a
chosen class is inserted periodicity.

The cohomology package constructs no DMP multiplication, no carrier-native
cohomology class, no carrier-native endpoint, no carrier-native boundary
glue, no pinned Laurent twist, and no torsor splitter. The graph,
endpoint/matching, idempotent, and Laurent-twist choices remain:

  graph choices:          64,1024,2097152,36028797018963968;
  endpoint-pair choices:  9,16,36,100;
  half-matching choices:  6,24,720,3628800;
  rank-one idempotents:   2016,32640,8386560,549755289600;
  Laurent twists:         3,5,9,17.

The bottom obstruction remains y^2=0, there is still no DMP degree -2, the
shear obstruction remains res_1(c)=1, and the same stabilizer-cohomology
package is formable on controls.

Therefore support Sp-stabilizer cohomology is not construction-grade R1
carrier periodicity or boundary glue. A surviving route must construct the
cohomology/periodicity, endpoint, boundary map, Laurent twist, and torsor
splitter as carrier-native correspondence data and prove DH/Epstein death at
that construction.
```

Verdict label:

```text
N1B_SYMPLECTIC_STABILIZER_COHOMOLOGY__CLASSIFYING_CLASSES_NOT_LAURENT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_symplectic_stabilizer_cohomology_no_go` verifies the
finite-window model.

SCH1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SCH2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

SCH3 records that full-frame stabilizer cohomology is trivial, because the
full-frame stabilizer counts are:

```text
1,1,1,1.
```

SCH4 records the first-pair stabilizers. They are the finite groups
`Sp(2m,F_2)` with:

```text
m = 2,3,5,9.
```

Their orders are:

```text
720,
1451520,
24815256521932800,
2060902435720151186326095525680721766346957783040000.
```

Their 2-adic orders are:

```text
4,9,25,81.
```

SCH5 records the elementary abelian 2-ranks:

```text
2,3,5,9.
```

Since each rank is at least two, each stabilizer contains `C_2 x C_2`. By
the standard finite-group periodic-cohomology criterion, this prevents
2-periodic mod-2 cohomology.

SCH6 records the endpoint-vector parabolic stabilizers. The nonzero endpoint
vector counts are:

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

These stabilizers contain elementary abelian 2-subgroups of the same ranks:

```text
2,3,5,9.
```

SCH7 records the ordinary-cohomology obstruction: ordinary stabilizer
cohomology is nonnegative, positive-degree classes are not units, and the
carrier has supplied no distinguished class.

SCH8 records the Tate-cohomology obstruction: in the tested windows the
finite stabilizer cohomology is not periodic, so the Tate package is not a
carrier-supplied single Laurent line. Imposing periodicity by localizing a
chosen class is formal insertion.

SCH9 records that stabilizer cohomology does not construct the endpoint,
boundary map, Laurent generator, or torsor splitter.

SCH10 records that the graph, endpoint, matching, idempotent, and twist
choices remain:

```text
graph choices = 64,1024,2097152,36028797018963968;
endpoint pairs = 9,16,36,100;
half matchings = 6,24,720,3628800;
rank-one idempotents = 2016,32640,8386560,549755289600;
Laurent twists = 3,5,9,17.
```

SCH11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

SCH12 applies the carrier guard: classifying-space, group-cohomology, and
Tate-cohomology operations on finite support stabilizers are support
operations, so controls can form the same package. SCH13 records the only
escape.

## 4. Impact on R1

```text
R1 after docs 138-175:

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
      torsor splitter (doc 175).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
      symplectic quotient/stack/isotropy/cohomology descent data, quadratic
      refinement or Maslov datum, orientation, half-identification, boundary
      endpoint, and Laurent twist/flag/idempotent/line, selector/functional/
      shift operator, torsor splitter, and weight>=1 datum from carrier data,
      and where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. Stabilizer cohomology is admissible only if the carrier
constructs the cohomology/periodicity data together with the endpoint,
boundary map, Laurent twist, and torsor splitter. Support stabilizer
cohomology alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SCH.1 full-frame stabilizer cohomology as carrier loop
  A proposal takes cohomology of the full-frame stabilizer. The stabilizer is
  trivial, so this supplies no loop or boundary data.

KILL-SCH.2 ordinary stabilizer cohomology class as Laurent generator
  A proposal uses a positive-degree class in H^*(Stab;F_2). Ordinary
  cohomology is nonnegative and positive-degree classes are not Laurent
  units.

KILL-SCH.3 stabilizer Tate cohomology as carrier Laurent line
  A proposal uses Tate cohomology of the finite residual stabilizer as the
  missing Laurent line. The tested stabilizers contain C_2 x C_2, so their
  mod-2 cohomology is not periodic; a single Laurent generator would be
  imposed by localization, not constructed.

KILL-SCH.4 stabilizer-cohomology package formable on controls
  Classifying-space/group/Tate cohomology of finite support stabilizers is a
  support operation. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 38 = doc 175:
  N1B_SYMPLECTIC_STABILIZER_COHOMOLOGY__CLASSIFYING_CLASSES_NOT_LAURENT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion:
classifying-space, group-cohomology, and Tate-cohomology packages of the
support symplectic stabilizers do not construct the carrier endpoint,
rank-one boundary map, Laurent line, Laurent twist, or torsor splitter.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian/opposite graph, Darboux/frame data,
  symplectic quotient/stack/isotropy/cohomology descent data, quadratic
  refinement or Maslov datum, orientation, half-identification, boundary
  endpoint, and Laurent twist/flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
