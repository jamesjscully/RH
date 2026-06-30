# 145 - Formally adjoining a torsor splitter is not the R1 carrier

Status: no-go + torsor-splitting insertion deletion, 2026-06-20. Eighth
cycle of the doc-137 construction arc. Docs 143-144 killed free Laurent
insertion and post-hoc projection. This document tests the next repair:
adjoin a new unit/selector with a twisted shear action chosen to trivialize
the doc-138 cocycle.

Witness, lead-reran this cycle:
`prime_int_torsor_splitter_insertion_no_go` (TSI1-TSI7 ALL PASS) --
exact cocycle/splitter/control-formability check.

## 1. Purpose

Doc 138 proves that the DDG7b defect

```text
c = (1+z)^-1
```

is a nonzero class in `H^1(<phi>;U_1)`. A natural attempted repair is to
extend the carrier by a new unit `b` and define its shear action so that
`c` becomes a coboundary:

```text
phi(b) = b*c^-1,
so b/phi(b) = c.
```

This is algebraically consistent, because `c` is a `C_2` cocycle. But as
stated it is not a construction of the R1 carrier. It is the formal
adjoining of a solution to the equation doc 138 proved has no solution in
the base.

## 2. Lemma

```text
Lemma 145.1 (formal torsor splitting is tautological insertion). Let
U_1 = 1+zF_2[[z]] with the Weyl shear phi(z)=z/(1+z), and let
c=(1+z)^-1. In U_1,

  c*phi(c)=1,
  c notin B^1,
  res_1(c)=1 while res_1(B^1)=0.

Adjoin a formal unit b and prescribe

  phi(b)=b*c^-1.

Then phi^2(b)=b, since c*phi(c)=1, and c=b/phi(b) by definition. Thus the
extended object splits the torsor, but only because the splitting unit and
its transformation law were inserted.

The same construction is formable for any C_2-cocycle d on any control:
adjoin s with phi(s)=s*d^-1. Therefore the formal splitter is not an R1
carrier unless b and the relation phi(b)=b*c^-1 are produced by a
carrier-native first map, and that map is undefined on DH/Epstein controls.
```

Verdict label:

```text
DD4_TORSOR_SPLITTER_INSERTION__TAUTOLOGICAL_COBOUNDARY_EXTENSION__NO_GO.
```

## 3. Proof

`prime_int_torsor_splitter_insertion_no_go` verifies the gates at
truncations `6,8,10,12`.

TSI1 records the base cocycle identity:

```text
c*phi(c)=1.
```

TSI2 records the base nontriviality from doc 138: `res_1(c)=1`, while
generator coboundaries have `res_1=0`; hence `c` is not a base coboundary.

TSI3 checks that the formal action

```text
phi(b)=b*c^-1
```

is involutive. This is exactly the cocycle identity in TSI1.

TSI4 checks the split:

```text
b/phi(b)=b/(b*c^-1)=c.
```

This is the point: the extension trivializes the torsor by definition.

TSI5 applies the control test. For any cocycle `d`, including a trivial
control cocycle or an abstract cocycle control, the same rule

```text
phi(s)=s*d^-1
```

gives a formal splitter. No Euler carrier field is consumed.

TSI6 records that the splitter is a new symbol plus an inserted
transformation law. TSI7 records the only escape: make the splitter
relation carrier-native and show where DH/Epstein cannot form it.

## 4. Impact on R1

```text
R1 after docs 138-145:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141);
    - bottom-class localization / formal inversion repair (doc 142);
    - freely adjoining an independent Laurent generator (doc 143);
    - projecting a free/tensor Laurent repair to one copy (doc 144);
    - formally adjoining a torsor splitter b with phi(b)=b*c^-1 (doc 145).

  STILL OPEN:
    - a genuinely different carrier whose first map produces the full line,
      selector, torsor splitter, and weight>=1 datum from carrier data, and
      where DH/Epstein controls fail before signs, zeros, or comparison.
```

R1 is not solved. What is now excluded is the move "make the obstruction
vanish by adjoining its solution." The next carrier must explain why the
solution exists natively.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-TSI.1 formal splitter promoted to construction
  A proposal adjoins b with phi(b)=b*c^-1 and claims the torsor is pinned.
  That is true in the extended object by definition, but it is not a
  construction of the carrier unless b is produced by a prior carrier map.

KILL-TSI.2 twisted external generator as DD.4
  A proposal twists an external Laurent/unit generator so that it cancels
  c. The twist is exactly the inserted coboundary solution; it must be
  justified as a carrier-native relation.

KILL-TSI.3 splitter formable on controls
  If the construction is "for any cocycle d, adjoin s with phi(s)=s*d^-1",
  then controls can form it too. DH/Epstein have not died.

KILL-TSI.4 base obstruction forgotten after extension
  The base U_1 obstruction remains nonzero. The extension changes the
  coefficient system by adding b; it does not prove c was a coboundary in
  the original R1 carrier.
```

## 6. Board

```text
doc-137 R1, cycle 8 = doc 145:
  DD4_TORSOR_SPLITTER_INSERTION__TAUTOLOGICAL_COBOUNDARY_EXTENSION__NO_GO.

What got built: no new sub-object. The value is a deletion: a formal
torsor-splitting extension is not a carrier unless the splitter relation
is itself constructed.

Next valid R1 work:
  construct the first carrier-native map/relation that produces the line,
  selector, and torsor splitter, with DH/Epstein death at that map; or move
  to a route where the full line and pinning are born without extension.
```
