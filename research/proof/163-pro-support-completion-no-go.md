# 163 - Pro-support completion keeps the boundary defect

Status: no-go + pro-support/infinite-completion repair deletion,
2026-06-20. Twenty-sixth cycle of the doc-137 construction arc. Docs 160-162
killed finite support nilpotents, filtered gluing, and derived support
gluing. This document tests the next repair: pass to an infinite or completed
support chain so that finite nilpotence becomes a topological/pro-nilpotent
operator and `1+N` has unbounded 2-power order on finite quotients.

Witness, lead-reran this cycle:
`prime_int_n1b_pro_support_completion_no_go` (PSC1-PSC12 ALL PASS) -- exact
finite-window shift-defect, one-sided-completion, negative-tail,
pro-unipotent, selector, obstruction, and control-formability checks.

## 1. Purpose

The derived-extension repair can now say:

```text
finite support nilpotents die, but the completed support chain has a
topological nilpotent N;
the pro-unipotent 1+N is the missing completed carrier orbit.
```

The visible DMP support is one-sided:

```text
degree -1 and all nonnegative degrees are present;
degrees <= -2 are absent.
```

Completing that one-sided support does not create a Laurent orbit. Depending
on orientation, the completed unilateral shift is injective but not
surjective, or surjective but not injective. The missing predecessor of the
bottom degree survives every completion of the visible support. The
pro-unipotent `1+N` is congruent to the identity on associated graded; its
finite quotients are 2-power unipotent quotients, not degree translations.

Making the orbit genuinely two-sided requires adding a negative tail. That is
external Laurent support unless a carrier constructs it.

This document is local. It does not reject carrier-native completed orbits.
It rejects only pro/infinite completion of the visible one-sided support
chain.

## 2. Lemma

```text
Lemma 163.1 (visible pro-support completion is one-sided or externally
two-sided).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let S_N be the finite support shift along the visible
support order.

For r=3,4,6,10:

  rank(S_N) = 2,3,5,9,

and each finite window has a rank-one boundary defect:

  dim ker(S_N) = 1,      dim coker(S_N) = 1.

In the one-sided completed limit, the right shift has:

  dim ker = 0,           dim coker = 1,

while the left shift has:

  dim ker = 1,           dim coker = 0.

So neither one-sided completion is an invertible Laurent shift.

The missing negative predecessor tail is absent in the DMP support:

  dim R_DMP[-2] = dim R_DMP[-3] = dim R_DMP[-4] = dim R_DMP[-8] = 0.

Testing negative windows of sizes 1,2,4,8, a two-sided completion would have
to insert:

  1,2,4,8

new negative support classes.

The finite quotient orders of the pro-unipotent `1+N` are 2-power unipotent
orders:

  4,4,8,16.

Moreover `1+N` fixes associated graded:

  displacement 0,

where a Laurent shift has support displacement:

  displacement 1.

The completed strict upper-triangular choices still have finite-window ranks:

  3,6,15,45,

and choice counts:

  8,64,32768,35184372088832.

Endpoint choices remain:

  3,4,6,10,

and rank-one idempotent counts remain:

  28,120,2016,523776.

The package constructs no DMP multiplication, no invertible two-sided carrier
shift, and no torsor splitter. The bottom obstruction remains y^2=0, there
is still no degree -2 predecessor, the shear obstruction remains
res_1(c)=1, and the same pro-support completion is formable on controls.

Therefore pro/infinite completion of the visible support chain is not
construction-grade R1 carrier correspondence. A surviving route must
construct the completed two-sided orbit as carrier-native correspondence data
and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_PRO_SUPPORT_COMPLETION__ONE_SIDED_BOUNDARY_OR_EXTERNAL_NEGATIVE_TAIL__NO_GO.
```

## 3. Proof

`prime_int_n1b_pro_support_completion_no_go` verifies the finite-window
models.

PSC1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

PSC2 records finite support-shift ranks:

```text
rank S_N:  2,3,5,9
ker S_N:   1,1,1,1
coker S_N: 1,1,1,1.
```

The kernel is the finite top cutoff; the cokernel is the bottom boundary.

PSC3 records the one-sided completion alternatives:

```text
right shift: ker 0, coker 1
left shift:  ker 1, coker 0.
```

Neither is invertible.

PSC4 records the absent negative predecessor tail:

```text
dim[-2] = dim[-3] = dim[-4] = dim[-8] = 0.
```

PSC5 records the two-sided-completion cost on negative windows:

```text
1,2,4,8 inserted negative classes.
```

PSC6 records finite quotient order bounds for `1+N`:

```text
4,4,8,16.
```

These are unipotent 2-power finite quotients, not a discrete Laurent orbit.

PSC7 records the associated-graded distinction:

```text
1+N displacement:        0
Laurent shift displacement: 1.
```

PSC8 records the completed upper-triangular overproduction:

```text
strict ranks: 3,6,15,45
choice counts: 8,64,32768,35184372088832.
```

PSC9 records the surviving selector problem. Endpoint choices remain:

```text
3,4,6,10.
```

Rank-one idempotent counts remain:

```text
28,120,2016,523776.
```

PSC10 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

PSC11 applies the carrier guard: one-sided completions and pro-unipotent
support operators are shadow-level data, so controls can form the same
package. PSC12 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-163:

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
      carrier orbit (doc 163).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/flag/idempotent/line,
      selector/functional/shift operator, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 is still open. A completed orbit is admissible only if the carrier
constructs the missing two-sided support. Completing the visible one-sided
support alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-PSC.1 one-sided support completion as carrier orbit
  A proposal completes the visible support chain and calls the unilateral
  shift the carrier shift. The boundary defect remains: one orientation is
  injective not surjective, the other surjective not injective.

KILL-PSC.2 pro-unipotent 1+N as Laurent generator
  A proposal uses the completed pro-unipotent operator as the Laurent
  generator. It fixes associated graded and has 2-power unipotent finite
  quotients; it does not translate support degree.

KILL-PSC.3 two-sided support completion by negative-tail insertion
  A proposal adds the missing negative tail to make the shift invertible.
  DMP support has no degree <= -2 classes; the tail is external unless the
  carrier constructs it.

KILL-PSC.4 pro-support completion formable on controls
  One-sided completions, pro-unipotent support operators, and inserted
  negative tails are shadow-level data. DH/Epstein have not died at a
  carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 26 = doc 163:
  N1B_PRO_SUPPORT_COMPLETION__ONE_SIDED_BOUNDARY_OR_EXTERNAL_NEGATIVE_TAIL__NO_GO.

What got built: no new sub-object. The value is a deletion: pro-completing
the visible one-sided support keeps a boundary defect; forcing a two-sided
orbit inserts an external negative tail.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
