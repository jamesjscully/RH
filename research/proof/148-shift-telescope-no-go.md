# 148 - A shift telescope is not a carrier without a carrier shift

Status: no-go + telescope/direct-limit repair deletion, 2026-06-20.
Eleventh cycle of the doc-137 construction arc. Doc 147 killed finite
shift coinvariants when imposed as index relations. This document tests
the next repair: package the same relations as a telescope or direct limit
under a single degree-shift map.

Witness, lead-reran this cycle:
`prime_int_n1b_shift_telescope_no_go` (STL1-STL9 ALL PASS) -- exact
finite-rank telescope/coinvariant check plus support/control tests.

## 1. Purpose

Doc 147 says that imposing

```text
e_i = e_{i+1}
```

on the tensor copies gives one visible Laurent line, but only by erasing
the DMP degree index. A proposal can try to improve this by saying the
relations come from a shift map:

```text
S(e_i)=e_{i+1},
colim(M --S--> M --S--> ...)
```

or from a mapping telescope. This changes the presentation, but not the
carrier issue. DMP support tells us which one-dimensional summands exist;
it does not supply adjacent maps between them.

## 2. Lemma

```text
Lemma 148.1 (support-only shift telescope is index collapse repackaged).
Let M_N = R_DMP[-1..N] tensor L, with L=F_2[u^{+-1}]. Suppose a telescope
is defined using the support-index shift

  S(e_i)=e_{i+1}.

The resulting finite-chain relations again identify adjacent copies and
produce Laurent rank one. But the map S is not supplied by the DMP support
calculation; support gives dimensions, not maps. The telescope uses only
the ordered index chain, so it can be formed on controls as well.

Moreover, the shift is not multiplication by the DMP bottom class: that
class remains square-zero by support. The doc-138 torsor obstruction also
remains unless a torsor splitter is inserted.

Therefore a support-only shift telescope is not a construction-grade R1
carrier. A surviving telescope route must construct S as a carrier-native
multiplication or correspondence and prove that DH/Epstein controls cannot
form it.
```

Verdict label:

```text
N1B_SHIFT_TELESCOPE__SUPPORT_INDEX_MAP_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_shift_telescope_no_go` verifies the finite models.

STL1 records the tensor ranks:

```text
N = 1,2,4,8  =>  rank = 3,4,6,10.
```

STL2 verifies that the support-index telescope relation collapses each
finite chain to rank one.

STL3 records that the telescope encodes the same adjacent identifications
as doc 147:

```text
N = 1,2,4,8  =>  2,3,5,9 shift arrows.
```

STL4 is the carrier point: DMP support supplies one-dimensional groups in
the listed degrees, but it does not supply adjacent maps `e_i -> e_{i+1}`.
Those maps are extra structure.

STL5 rules out the claim that the support-only shift is multiplication by
the DMP bottom class; the bottom class remains square-zero and has no
degree `-2` product target.

STL6 records that the doc-138 shear obstruction remains:

```text
res_1(c)=1
```

is still outside the base coboundaries.

STL7 applies the carrier guard: the same support-only shift telescope is
formable on controls. STL8 records that the shift schema consumes no
primitive carrier field. STL9 records the only escape: construct the shift
map carrier-natively and show where controls fail.

## 4. Impact on R1

```text
R1 after docs 138-148:

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
    - shift telescope/direct-limit packaging of that collapse (doc 148).

  STILL OPEN:
    - a genuinely different carrier whose first map produces the full line,
      selector/functional/shift map, torsor splitter, and weight>=1 datum
      from carrier data, and where DH/Epstein controls fail before signs,
      zeros, or comparison.
```

R1 is still open. The shift map is now explicitly part of the required
carrier data; naming a telescope does not supply it.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-STL.1 support-index telescope as carrier
  A proposal defines S(e_i)=e_{i+1} on tensor copies using only the DMP
  degree index. This is the doc-147 relation repackaged as a map schema.

KILL-STL.2 colimit hides missing maps
  A proposal takes a colimit over adjacent copies but does not construct
  the adjacent maps from carrier data. DMP support gives dimensions, not
  maps.

KILL-STL.3 telescope as bottom multiplication
  The shift cannot be identified with multiplication by the DMP bottom
  class; that class remains square-zero.

KILL-STL.4 telescope formable on controls
  A support-only ordered-chain telescope can be built for controls too.
  DH/Epstein have not died at a carrier-consuming map.
```

## 6. Board

```text
doc-137 R1, cycle 11 = doc 148:
  N1B_SHIFT_TELESCOPE__SUPPORT_INDEX_MAP_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: a shift
telescope does not upgrade index collapse into a carrier.

Next valid R1 work:
  construct the first carrier-native multiplication/correspondence that
  supplies the shift map, rank-one line, selector/functional, and torsor
  splitter, with DH/Epstein death at that map.
```
