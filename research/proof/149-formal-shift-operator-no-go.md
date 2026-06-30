# 149 - A formal shift operator is not a carrier shift

Status: no-go + formal-operator insertion deletion, 2026-06-20. Twelfth
cycle of the doc-137 construction arc. Doc 148 killed the support-index
telescope because DMP support supplies dimensions, not adjacent maps. This
document tests the next repair: adjoin a formal shift operator `S` and
call its orbit the missing Laurent line.

Witness, lead-reran this cycle:
`prime_int_n1b_formal_shift_operator_no_go` (FSO1-FSO10 ALL PASS) --
exact finite-rank shift-operator checks plus support/control tests.

## 1. Purpose

Doc 148 leaves one sharp demand:

```text
construct the shift map carrier-natively.
```

The false repair is to replace construction by formal syntax:

```text
S(e_i)=e_{i+1},      S invertible,
orbit(e_0) = {...,S^-1 e_0,e_0,S e_0,...}.
```

That looks closer to a Laurent line than the doc-147 coinvariants or the
doc-148 telescope. But it still has to answer where `S` comes from. There
are only three support-level possibilities:

```text
finite forward shift        terminal zero, noninvertible;
finite cyclic shift         artificial terminal wrap;
bi-infinite invertible S    external Laurent orbit.
```

None supplies a carrier-native R1 map.

## 2. Lemma

```text
Lemma 149.1 (formal shift operators are insertion unless carrier-native).
Let M_N = R_DMP[-1..N] tensor L, with L=F_2[u^{+-1}]. Let
e_0,...,e_{N+1} be the Laurent copies indexed by the DMP support degrees.

1. The forward support shift S(e_i)=e_{i+1}, S(e_{N+1})=0 is nilpotent
   and noninvertible. Forcing S to be invertible localizes a nilpotent
   operator and kills the truncated carrier.

2. Making S invertible on the finite support by setting
   S(e_{N+1})=e_0 inserts a cyclic wrap not supplied by DMP support. It
   imposes artificial degree periodicity and identifies the terminal
   nonnegative copy with the bottom copy.

3. Making S genuinely invertible by a bi-infinite orbit requires classes
   below the DMP bottom degree. Since DMP support has no degree <= -2,
   this is an externally adjoined Laurent orbit, i.e. doc 143 in operator
   language.

In all three cases the DMP bottom class remains square-zero, the doc-138
shear obstruction remains, and the same formal operator schema is formable
on controls. Therefore a formal shift operator is not a construction-grade
R1 carrier unless S is constructed as carrier-native multiplication or a
carrier-native correspondence and DH/Epstein controls fail at that map.
```

Verdict label:

```text
N1B_FORMAL_SHIFT_OPERATOR__INSERTED_OPERATOR_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_formal_shift_operator_no_go` verifies the finite models.

FSO1 records the tensor ranks:

```text
N = 1,2,4,8  =>  rank = 3,4,6,10.
```

FSO2-FSO3 test the finite forward shift. Its rank is `r-1` on a chain of
rank `r`, and its `r`th power is zero. Thus the support-level forward
shift is not a Laurent generator.

FSO4 records the localization failure: if this nilpotent `S` is forced
invertible, then `S^r=0` implies every class dies. The finite carrier
collapses.

FSO5-FSO6 test the cyclic repair. The cyclic shift is invertible, but
only after adding the terminal arrow

```text
e_{r-1} -> e_0.
```

That arrow is not supplied by DMP support and imposes degree periodicity
modulo the truncation length.

FSO7 tests the infinite repair. A bi-infinite invertible orbit needs
`S^-1 e_0`, hence support below the DMP bottom. Since degree `-2` is zero,
the orbit is new structure: an external Laurent line, already killed by
doc 143 unless produced by a nonfree carrier map.

FSO8 records that the base obstructions remain:

```text
y^2 = 0,     res_1(c)=1.
```

FSO9 applies the carrier guard: the nilpotent, cyclic, and free invertible
`S` schemas use only finite-rank module data and can be formed on controls.
FSO10 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-149:

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
    - formal shift-operator insertion as the missing carrier shift (doc 149).

  STILL OPEN:
    - a genuinely different carrier whose first map produces the full line,
      selector/functional/shift map, torsor splitter, and weight>=1 datum
      from carrier data, and where DH/Epstein controls fail before signs,
      zeros, or comparison.
```

R1 is still open. The word "operator" does not help unless the operator is
constructed by the carrier. A formal `S` is now logged as insertion.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-FSO.1 finite support shift as Laurent generator
  A proposal uses S(e_i)=e_{i+1} on the truncated support with terminal
  zero. This shift is nilpotent and noninvertible; inverting it collapses
  the truncation.

KILL-FSO.2 cyclic shift as carrier map
  A proposal makes the finite support shift invertible by wrapping the
  terminal copy to the bottom copy. The wrap is inserted and imposes
  artificial degree periodicity.

KILL-FSO.3 bi-infinite formal orbit as carrier
  A proposal adjoins S^{+-1} orbit data to get a Laurent line. Since DMP
  support has no degree <= -2, this is external Laurent insertion unless
  the orbit is produced by a carrier-native map.

KILL-FSO.4 formal operator formable on controls
  Nilpotent, cyclic, and free invertible shift-operator schemas can be
  imposed on controls too. DH/Epstein have not died at a carrier-consuming
  map.
```

## 6. Board

```text
doc-137 R1, cycle 12 = doc 149:
  N1B_FORMAL_SHIFT_OPERATOR__INSERTED_OPERATOR_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: a named
operator does not construct the shift map.

Next valid R1 work:
  construct the first carrier-native multiplication/correspondence that
  supplies S, the rank-one line, selector/functional, and torsor splitter,
  with DH/Epstein death at that map.
```
