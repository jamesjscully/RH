# 150 - The support End envelope is not the correspondence algebra

Status: no-go + endomorphism-envelope deletion, 2026-06-20. Thirteenth
cycle of the doc-137 construction arc. Doc 149 killed formal
shift-operator insertion. This document tests the next tempting repair:
take an endomorphism algebra of the visible support module and claim the
shift has become carrier-native because it lives inside `End`.

Witness, lead-reran this cycle:
`prime_int_n1b_endomorphism_envelope_no_go` (EEV1-EEV10 ALL PASS) --
exact finite-rank matrix-envelope, selector-count, shift, and
control-formability checks.

## 1. Purpose

The final target is an `End` object, so there is an obvious false friend:

```text
M_N = R_DMP[-1..N] tensor L ~= L^(N+2),
take End_L(M_N).
```

The envelope certainly contains shifts and projections. But containment
inside a full matrix algebra is not construction. R1 needs the carrier to
produce the full line, selector/functional, shift operator, torsor splitter,
and weight>=1 datum. The support-module `End` envelope produces all maps at
once, then asks us to choose the right one.

This document is local. It does not reject a genuine correspondence algebra
`End(Xbar)` or `End(S^2/Z)`. It rejects only the support/shadow operation
`M -> End(M)` when no primitive carrier map has been constructed first.

## 2. Lemma

```text
Lemma 150.1 (support End envelope is matrix overproduction).
Let M_N = R_DMP[-1..N] tensor L with L=F_2[u^{+-1}], so
M_N ~= L^r and r=N+2. Then

  End_L(M_N) ~= Mat_r(L).

Consequently:

1. The envelope has Laurent rank r^2, not rank one.
2. It contains r^2 coordinate matrix units and many rank-one maps; choosing
   one is a selector problem, not carrier data.
3. It contains many cyclic shift matrices, but selecting one cyclic order
   and terminal wrap is the doc-149 insertion problem inside Mat_r(L).
4. The support-order forward shift inside Mat_r(L) is still nilpotent and
   noninvertible.
5. The center is the scalar copy L already supplied by the external Laurent
   tensor factor; it is inherited, not produced by DMP support.
6. The DMP bottom class remains square-zero and the doc-138 shear
   obstruction remains.
7. The same End envelope can be formed on controls: `End` of a finite free
   module is a shadow-stable matrix operation before any primitive carrier
   field is consumed.

Therefore the support-module endomorphism envelope is not a
construction-grade R1 carrier. A surviving End route must build a
carrier-native correspondence algebra with composition, the selected shift,
selector/functional, torsor splitter, and DH/Epstein death as object data.
```

Verdict label:

```text
N1B_ENDOMORPHISM_ENVELOPE__MATRIX_OVERPRODUCTION_NOT_CORRESPONDENCE__NO_GO.
```

## 3. Proof

`prime_int_n1b_endomorphism_envelope_no_go` verifies the finite models.

EEV1 records the support-tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

EEV2 computes the Laurent rank of the endomorphism envelope:

```text
rank_L End_L(L^r) = r^2 = 9,16,36,100.
```

This is matrix overproduction, not a singleton Lin line.

EEV3 records the coordinate matrix-unit count, again `r^2`. EEV4 counts
rank-one endomorphism choices over `F_2`:

```text
(2^r - 1)^2 = 49,225,3969,1046529.
```

The envelope supplies many possible selectors. It does not choose one.

EEV5 counts invertible cyclic shift choices:

```text
(r-1)! = 2,6,120,362880.
```

Thus "use a cyclic shift in End" has the same terminal-wrap and selection
defect as doc 149.

EEV6 tests the support-order forward shift inside the matrix algebra. It
has rank `r-1` and is nilpotent, so putting it inside `End` does not make
it a Laurent generator.

EEV7 records that the center is the scalar line `L`. That line is inherited
from the external tensor factor killed by docs 143-144; it is not produced
by DMP support. If one instead takes `End` of the raw DMP support without
the tensor `L`, even this inherited Laurent scalar line is absent.

EEV8 records that the base obstructions remain:

```text
y^2 = 0,     res_1(c)=1.
```

EEV9 applies the carrier-overreach guard: the same `End` of a finite free
module exists for controls. EEV10 records the only escape: construct the
End object as a carrier correspondence before controls can form it.

## 4. Impact on R1

```text
R1 after docs 138-150:

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
      (doc 150).

  STILL OPEN:
    - a genuinely different carrier whose first map produces a
      correspondence algebra with the full line, selector/functional/shift
      operator, torsor splitter, and weight>=1 datum from carrier data, and
      where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. The word `End` now has the same discipline as the word
`operator`: it only counts after the carrier constructs the correspondence
and selects the maps. A matrix envelope of support data is not that object.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-EEV.1 End of support module as carrier
  A proposal forms End_L(R_DMP[-1..N] tensor L) and points to maps inside
  it. This is Mat_r(L), a full matrix envelope, not the correspondence
  algebra.

KILL-EEV.2 shift contained in End
  A proposal says S is now carrier-native because S is an endomorphism.
  The support-order shift remains nilpotent; cyclic/invertible shifts are
  selected from many choices and insert a wrap or external orbit.

KILL-EEV.3 scalar center as produced Laurent line
  A proposal uses the center of Mat_r(L) as the line. That center is the
  already-adjoined external L; it is inherited from the tensor repair, not
  produced by DMP support.

KILL-EEV.4 End envelope formable on controls
  End of a finite free module is a shadow-stable operation. DH/Epstein
  have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 13 = doc 150:
  N1B_ENDOMORPHISM_ENVELOPE__MATRIX_OVERPRODUCTION_NOT_CORRESPONDENCE__NO_GO.

What got built: no new sub-object. The value is a deletion: an End
envelope of support data is not End(S^2/Z).

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  End object supplies S, the rank-one line, selector/functional, and torsor
  splitter, with DH/Epstein death at that correspondence.
```
