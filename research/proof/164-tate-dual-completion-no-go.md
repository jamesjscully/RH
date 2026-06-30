# 164 - Tate dual completion doubles support before it glues it

Status: no-go + Tate/continuous-dual completion repair deletion,
2026-06-20. Twenty-seventh cycle of the doc-137 construction arc. Doc 163
killed pro/infinite completion of the visible one-sided support chain because
the unilateral boundary defect remains and a two-sided orbit requires a
negative tail. This document tests the next repair: add the continuous dual
tail and call the resulting hyperbolic/Tate object the completed carrier
orbit.

Witness, lead-reran this cycle:
`prime_int_n1b_tate_dual_completion_no_go` (TDC1-TDC12 ALL PASS) -- exact
finite-window dual-rank, Tate-window, unilateral-shift, boundary-glue,
negative-tail, selector, obstruction, and control-formability checks.

## 1. Purpose

The pro-support repair can now say:

```text
do not add an arbitrary negative tail;
take the continuous dual of the one-sided support;
the Tate/hyperbolic object supplies the missing two-sided carrier orbit.
```

This produces a real dual half, but not a carrier-native Laurent orbit. On
finite windows the dual half mirrors the visible support rank, so the
Tate/hyperbolic window doubles the support rank. The dual basis is co-support
data; it is not identified with missing DMP degrees `<= -2` unless one
inserts such an identification.

The direct sum of the unilateral support shift and its dual adjoint still has
a one-dimensional kernel and cokernel. To make it invertible, one must insert
a boundary glue map between the two defects. That is exactly the missing
carrier correspondence unless the carrier constructs it.

This document is local. It does not reject carrier-native Tate dualities. It
rejects only Tate/continuous-dual completion formed from the visible support
module.

## 2. Lemma

```text
Lemma 164.1 (support Tate completion needs non-support boundary glue).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let M_N^vee be the finite-window dual support module.

For r=3,4,6,10, the dual windows have the same ranks:

  3,4,6,10.

Thus the Tate/hyperbolic windows M_N plus M_N^vee have ranks:

  6,8,12,20.

Let S be the one-sided shift on the visible support and S^vee its dual
adjoint. In the completed one-sided model:

  S has        dim ker = 0, dim coker = 1,
  S^vee has   dim ker = 1, dim coker = 0.

Therefore S plus S^vee has:

  dim ker = 1, dim coker = 1.

It is not a Laurent shift. It becomes invertible only after inserting a
rank-one boundary glue map between the cokernel of one half and the kernel of
the other.

The dual tail is not DMP negative support:

  dim R_DMP[-2] = dim R_DMP[-3] = dim R_DMP[-4] = dim R_DMP[-8] = 0.

The pro-unipotent finite quotient orders remain inherited from the one-sided
support:

  4,4,8,16.

The Tate half choice remains:

  2,2,2,2.

Support and dual endpoint choices remain:

  3,4,6,10.

Rank-one idempotent counts in the doubled Tate windows grow to:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native
identification of dual tail with missing negative support, no carrier-native
boundary glue, and no torsor splitter. The bottom obstruction remains y^2=0,
there is still no DMP degree -2, the shear obstruction remains res_1(c)=1,
and the same Tate-dual completion is formable on controls.

Therefore Tate/continuous-dual completion of the visible support is not
construction-grade R1 carrier correspondence. A surviving route must
construct the dual-tail identification and boundary glue as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_TATE_DUAL_COMPLETION__DUAL_TAIL_AND_BOUNDARY_GLUE_INSERTED__NO_GO.
```

## 3. Proof

`prime_int_n1b_tate_dual_completion_no_go` verifies the finite-window models.

TDC1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

TDC2 records that the continuous dual windows mirror the support ranks:

```text
3,4,6,10.
```

TDC3 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

This is not a selected carrier line.

TDC4 records the unilateral plus dual-adjoint shift defects:

```text
visible shift:    ker 0, coker 1
dual adjoint:     ker 1, coker 0
direct sum:       ker 1, coker 1.
```

TDC5 records the missing boundary glue:

```text
rank-one boundary glue needed in every tested window.
```

TDC6 records that the dual tail is not DMP negative support:

```text
dim[-2] = dim[-3] = dim[-4] = dim[-8] = 0.
```

TDC7 records inherited pro-unipotent finite quotient order bounds:

```text
4,4,8,16.
```

TDC8 records that the two halves and endpoints are still choices:

```text
half choices:       2,2,2,2
support endpoints:  3,4,6,10
dual endpoints:     3,4,6,10.
```

TDC9 records rank-one idempotent overproduction in the Tate windows:

```text
2016,32640,8386560,549755289600.
```

TDC10 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

TDC11 applies the carrier guard: dualizing a one-sided finite-free support
module is shadow-level data, so controls can form the same package. TDC12
records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-164:

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
      (doc 164).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with boundary glue/
      flag/idempotent/line, selector/functional/shift operator, torsor
      splitter, and weight>=1 datum from carrier data, and where DH/Epstein
      controls fail before signs, zeros, or comparison.
```

R1 is still open. A Tate duality is admissible only if the carrier constructs
the dual-tail identification and boundary glue. Dualizing visible support
alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-TDC.1 support continuous dual as missing negative tail
  A proposal identifies the continuous dual basis with missing DMP negative
  support. DMP has no degree <= -2 support; the identification is extra data
  unless the carrier constructs it.

KILL-TDC.2 direct-sum unilateral shift plus dual adjoint as Laurent shift
  A proposal uses S plus S^vee as the carrier shift. The direct sum still has
  one-dimensional kernel and cokernel.

KILL-TDC.3 boundary glue as automatic Tate data
  A proposal glues the two shift defects to make the shift invertible. That
  glue is a rank-one correspondence map and must be carrier-native.

KILL-TDC.4 Tate-dual completion formable on controls
  Dualizing one-sided finite-free support, forming the hyperbolic window, and
  inserting boundary glue are shadow-level operations. DH/Epstein have not
  died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 27 = doc 164:
  N1B_TATE_DUAL_COMPLETION__DUAL_TAIL_AND_BOUNDARY_GLUE_INSERTED__NO_GO.

What got built: no new sub-object. The value is a deletion: Tate-dual
completion of visible support doubles the support module, and invertibility
still requires an inserted boundary glue map.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with boundary glue/flag/
  idempotent/line, shift operator, selector/functional, and torsor splitter,
  with DH/Epstein death at that correspondence.
```
