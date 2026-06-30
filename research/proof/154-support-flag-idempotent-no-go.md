# 154 - A support flag is not a carrier flag

Status: no-go + support-flag/Borel selector deletion, 2026-06-20.
Seventeenth cycle of the doc-137 construction arc. Doc 153 killed
support-matrix conjugacy because the full `GL_r` symmetry is too large to
choose a rank-one idempotent. This document tests the next repair: reduce
the symmetry by imposing the DMP support-degree flag and then take the
first coordinate corner.

Witness, lead-reran this cycle:
`prime_int_n1b_support_flag_idempotent_no_go` (SFI1-SFI10 ALL PASS) --
exact finite-rank flag-count, Borel-rank, obstruction, and
control-formability checks.

## 1. Purpose

The support-envelope repair can now say:

```text
GL_r was too large;
use the DMP support order -1,0,1,...,N as a flag;
then the first flag line selects the idempotent.
```

This is a real reduction of the matrix symmetry. But it is not a carrier
construction. A flag supplied by the ordered support degrees is the same
bookkeeping that docs 147-149 already rejected when it was used to create a
shift. It orders visible summands; it does not construct multiplication,
adjacent maps, a shift operator, or a torsor splitter.

This document is local. It does not reject a carrier-native flag produced
by a correspondence. It rejects only the support-index flag on
`R_DMP[-1..N] tensor L` when no primitive carrier map constructs the flag.

## 2. Lemma

```text
Lemma 154.1 (support flags are selector data unless carrier-native).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and L=F_2[u^{+-1}].
Let A_N = End_L(M_N) ~= Mat_r(L).

A complete flag in M_N selects a first line and hence a rank-one corner.
But the flag is extra finite-free module data. Over F_2, the number of
complete flags in ranks r=3,4,6,10 is:

  21, 315, 615195, 10414855105976475.

The Borel algebra preserving such a flag has Laurent rank:

  r(r+1)/2 = 6,10,21,55.

So the flag/Borel reduction still overproduces maps, and the selected line
is selected only after the flag has been supplied.

If the flag is the DMP support order, then it consumes no primitive carrier
map. The bottom flag corner recovers the external scalar line L from the
tensor repair; it does not make the DMP bottom class invertible. A flag
does not supply adjacent maps, the shift operator, or a torsor splitter.
The DMP bottom class remains square-zero, the doc-138 shear obstruction
remains, and the same ordered-flag/Borel construction is formable on
controls.

Therefore a support-degree flag is not a construction-grade R1 carrier
selector. A surviving route must construct the flag from carrier
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_SUPPORT_FLAG_IDEMPOTENT__ORDERED_SUPPORT_NOT_CARRIER_FLAG__NO_GO.
```

## 3. Proof

`prime_int_n1b_support_flag_idempotent_no_go` verifies the finite models.

SFI1 records the support ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

SFI2 counts complete flags over `F_2`:

```text
21, 315, 615195, 10414855105976475.
```

This confirms that flags are substantial extra structure in the finite-free
module unless the carrier constructs one.

SFI3 records the Borel algebra ranks:

```text
6,10,21,55.
```

The Borel reduction shrinks `Mat_r(L)` but still contains many maps.

SFI4 records the positive algebraic fact: once a flag is supplied, its
first line selects a coordinate corner. The issue is that the support flag
consumes no carrier map.

SFI5 records that before the flag there are still `r` coordinate choices:

```text
3,4,6,10.
```

SFI6 tests the bottom flag corner. Its scalar is the external `L` from the
tensor repair; the original DMP bottom class still has no degree `-2`
product target and remains square-zero.

SFI7 records that a flag supplies no adjacent maps, no shift operator, and
no torsor splitter.

SFI8 records that the base obstructions remain:

```text
y^2 = 0,     res_1(c)=1.
```

SFI9 applies the carrier guard: ordered finite-free flags and Borel
subalgebras are shadow-level data, so controls can form the same reduction.
SFI10 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-154:

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
      selector (doc 154).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the flag/idempotent/line, selector/functional/shift operator,
      torsor splitter, and weight>=1 datum from carrier data, and where
      DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is still open. A flag is admissible only if the carrier constructs it.
The support degree order alone is bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SFI.1 support-degree flag as carrier flag
  A proposal uses the ordered DMP support degrees to define a flag and then
  picks the first line. The flag is support bookkeeping unless constructed
  by a carrier correspondence.

KILL-SFI.2 Borel reduction as correspondence algebra
  A proposal replaces Mat_r(L) by the Borel algebra preserving the support
  flag. This still overproduces maps and supplies no shift/torsor data.

KILL-SFI.3 bottom flag line as DMP generator
  A proposal chooses the bottom flag line. Its scalar is the external L;
  the DMP bottom class remains square-zero.

KILL-SFI.4 support flag formable on controls
  Ordered finite-free flags and Borel subalgebras are shadow-level data.
  DH/Epstein have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 17 = doc 154:
  N1B_SUPPORT_FLAG_IDEMPOTENT__ORDERED_SUPPORT_NOT_CARRIER_FLAG__NO_GO.

What got built: no new sub-object. The value is a deletion: the DMP support
order is not a carrier flag.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data choose the flag/idempotent/line, shift operator,
  selector/functional, and torsor splitter, with DH/Epstein death at that
  correspondence.
```
