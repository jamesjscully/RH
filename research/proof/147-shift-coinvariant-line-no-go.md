# 147 - Shift coinvariants make a line by erasing the carrier

Status: no-go + shift/coinvariant repair deletion, 2026-06-20. Tenth
cycle of the doc-137 construction arc. Docs 143-146 killed free insertion,
projection, formal splitter insertion, and quotient-to-line repairs. This
document tests the next repair: impose shift coinvariants on the tensor
copies so all Laurent copies become one.

Witness, lead-reran this cycle:
`prime_int_n1b_shift_coinvariant_no_go` (SCI1-SCI9 ALL PASS) -- exact
F_2 rank computation for the finite-chain coinvariant quotient.

## 1. Purpose

The tensor repair has

```text
R_DMP[-1..N] tensor F_2[u^{+-1}] ~= L^{N+2}.
```

Docs 144 and 146 say that selecting or quotienting to one copy requires a
noncanonical selector/functional. The next repair is to impose relations
on the DMP-degree copies:

```text
e_i = e_{i+1},  i=0,...,N,
```

so the `N+2` Laurent copies become coinvariantly one copy.

This does produce a visible Laurent line. The problem is that it does so
by quotienting the degree index, not by constructing the R1 carrier.

## 2. Lemma

```text
Lemma 147.1 (shift coinvariants are index collapse unless carrier-native).
Let M_N = R_DMP[-1..N] tensor L, where L=F_2[u^{+-1}]. Then M_N is a free
L-module with basis e_0,...,e_{N+1}. The finite-chain shift relations

  e_i + e_{i+1} = 0,  i=0,...,N,

have rank N+1 over F_2. Therefore the coinvariant quotient has Laurent
rank one.

However, these relations identify the DMP bottom copy with every
nonnegative-degree copy. They erase the DMP degree distinction, leave the
original bottom class square-zero, leave the doc-138 shear obstruction
unchanged, and can be imposed on any same-length control chain.

Thus the shift-coinvariant line is not a construction-grade R1 carrier
unless the shift relation itself is produced by a carrier-native map and
DH/Epstein controls cannot form that map.
```

Verdict label:

```text
N1B_SHIFT_COINVARIANT_LINE__INDEX_COLLAPSE_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_shift_coinvariant_no_go` verifies the finite models.

SCI1 records the tensor ranks:

```text
N = 1,2,4,8  =>  rank = 3,4,6,10.
```

SCI2 computes the rank of the adjacent-relation matrix
`e_i+e_{i+1}` over `F_2` and verifies that the coinvariant rank is `1` at
each truncation.

SCI3 records the relation count:

```text
N = 1,2,4,8  =>  2,3,5,9 relations.
```

The number of inserted index relations grows with the truncation.

SCI4 records the carrier loss: after coinvariants, the bottom coordinate
and all nonnegative coordinates are the same class. The quotient has
forgotten the DMP bottom/nonnegative distinction that docs 139-140 used.

SCI5-SCI6 record that the base obstructions are not repaired. The DMP
bottom class still has no degree `-2` product target, and `res_1(c)=1`
remains outside the base coboundaries.

SCI7 applies the carrier guard: the same finite-chain coinvariant quotient
is formable on controls. SCI8 records the G-INT6 failure for the
index-only collapse: at `N=8`, nine relations are inserted and zero
primitive carrier fields are consumed. SCI9 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-147:

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
    - shift-coinvariant collapse of the tensor copies to one line (doc 147).

  STILL OPEN:
    - a genuinely different carrier whose first map produces the full line,
      selector/functional/shift relation, torsor splitter, and weight>=1
      datum from carrier data, and where DH/Epstein controls fail before
      signs, zeros, or comparison.
```

R1 remains open. The admissible route is now stricter: it must not merely
collapse a visible index family; it must construct the collapse relation in
the carrier.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-SCI.1 degree-shift coinvariants as carrier
  A proposal imposes e_i=e_{i+1} on the tensor copies and points to the
  resulting line. That is an index quotient unless the shift relation is
  carrier-native.

KILL-SCI.2 line by erasing DMP degree data
  A proposal obtains one line only after identifying the bottom copy with
  every nonnegative copy. It has erased the DMP distinction, not produced
  the missing multiplicative line.

KILL-SCI.3 shift quotient hides base obstructions
  The coinvariant quotient does not make the original DMP bottom class
  invertible and does not kill the doc-138 torsor obstruction.

KILL-SCI.4 shift relation formable on controls
  A finite-chain relation e_i=e_{i+1} can be imposed on controls too.
  DH/Epstein have not died at a carrier-consuming map.
```

## 6. Board

```text
doc-137 R1, cycle 10 = doc 147:
  N1B_SHIFT_COINVARIANT_LINE__INDEX_COLLAPSE_NOT_CARRIER__NO_GO.

What got built: no new sub-object. The value is a deletion: shift
coinvariants give one visible line only by imposing index relations.

Next valid R1 work:
  construct the first carrier-native map/relation that produces a rank-one
  line, selector/functional/shift relation, and torsor splitter, with
  DH/Epstein death at that map.
```
