# 158 - Support-chain connections have no carrier holonomy

Status: no-go + support-connection/holonomy repair deletion, 2026-06-20.
Twenty-first cycle of the doc-137 construction arc. Doc 157 killed
stabilizer/Laurent-loop decoration because attaching `Z` isotropy to the
support groupoid inserts `Mat_r(L[s^{+-1}])`. This document tests the next
repair: label the support arrows by units, or put a connection on the
support groupoid, and use its holonomy as the missing loop/shift/torsor data.

Witness, lead-reran this cycle:
`prime_int_n1b_connection_holonomy_no_go` (CHN1-CHN11 ALL PASS) -- exact
finite-rank edge-label, gauge, tree-cohomology, artificial-cycle,
obstruction, and control-formability checks.

## 1. Purpose

The stabilizer-loop repair can now say:

```text
do not insert a loop group;
label the support arrows by units;
then the products around paths/loops supply holonomy.
```

The support graph is a line tree. On a tree, edge labels are gauge data. With
one base vertex fixed, vertex gauges have the same count as edge labelings,
and every flat support-chain connection is gauge-equivalent to the trivial
one. Nontrivial holonomy appears only after adding a terminal wrap or an
external loop, which re-enters the cyclic/stabilizer repairs killed in docs
149 and 157.

This document is local. It does not reject carrier-native holonomy. It
rejects only labels/connections placed on the visible support chain when no
primitive carrier correspondence constructs them.

## 2. Lemma

```text
Lemma 158.1 (support-chain connections are tree gauge data).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2, and let C_r be the
ordered support line with r vertices and r-1 edges.

For any finite abelian coefficient group A, an A-valued support connection
is an assignment of a label to each edge of the tree C_r. Hence the number
of edge labelings is:

  |A|^{r-1}.

The based vertex gauge group also has size:

  |A|^{r-1}.

Therefore every support-chain connection is gauge-normalizable, and

  H^1(C_r; A) = 0.

Equivalently, the number of gauge classes is 1.

For A=F_2 and r=3,4,6,10, edge labelings and based gauges both have sizes:

  4,8,32,512,

and the holonomy class counts are:

  1,1,1,1.

For A=F_3, edge labelings and based gauges both have sizes:

  9,27,243,19683,

and the holonomy class counts are again:

  1,1,1,1.

To get nontrivial holonomy from the support chain one must add a terminal
wrap, changing the tree into a cycle. In the mod-2 test this gives

  H^1(cycle; F_2) = F_2,

with two holonomy classes. But the terminal wrap is not supplied by DMP
support; it is the cyclic-shift insertion killed in doc 149.

Labels in external Laurent units are therefore scalar bookkeeping unless
the carrier constructs them. They do not construct DMP multiplication, a
torsor splitter, or a Laurent shift. The doc-138 shear obstruction remains
res_1(c)=1, the bottom obstruction remains y^2=0, and the same
support-chain connection system is formable on controls.

Therefore support-chain connection labels are not construction-grade R1
carrier holonomy. A surviving route must construct nontrivial holonomy as
carrier-native correspondence data and prove DH/Epstein death at that
construction.
```

Verdict label:

```text
N1B_CONNECTION_HOLONOMY__SUPPORT_TREE_LABELS_GAUGE_TRIVIAL__NO_GO.
```

## 3. Proof

`prime_int_n1b_connection_holonomy_no_go` verifies the finite models.

CHN1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

CHN2 records the support-chain edge counts:

```text
r-1 = 2,3,5,9.
```

CHN3 records mod-2 edge labelings and based vertex gauges:

```text
4,8,32,512.
```

They agree exactly.

CHN4 records the mod-2 holonomy class counts:

```text
1,1,1,1.
```

CHN5 repeats the same gauge-triviality test with mod-3 labels:

```text
edge labels = based gauges = 9,27,243,19683,
holonomy classes = 1,1,1,1.
```

This avoids making the no-go depend on the characteristic-2 coefficient.

CHN6 records the only way to get support holonomy: add a terminal wrap. The
cycle edge counts become:

```text
3,4,6,10,
```

and the mod-2 cycle holonomy count is:

```text
2,2,2,2.
```

That is the artificial cyclic wrap already killed as a formal shift repair.

CHN7 records that labeled support paths are determined by endpoint gauges:

```text
6,12,30,90.
```

CHN8 records that support-arrow labels are external scalars unless a carrier
constructs them. They supply no DMP multiplication and no relation
`b/phi(b)=c`.

CHN9 records the base obstructions:

```text
y^2 = 0,     res_1(c)=1.
```

CHN10 applies the carrier guard: finite-tree edge labels and gauges use only
ordered support data, so controls can form the same connection system. CHN11
records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-158:

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
    - unit-labeled support-chain connections as carrier holonomy (doc 158).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/flag/
      idempotent/line, selector/functional/shift operator, torsor splitter,
      and weight>=1 datum from carrier data, and where DH/Epstein controls
      fail before signs, zeros, or comparison.
```

R1 is still open. Holonomy is admissible only if the carrier constructs it.
Connections on the support line alone are gauge bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-CHN.1 support-arrow labels as carrier connection
  A proposal labels the ordered support-chain arrows by units. On the line
  tree, those labels are gauge-normalizable unless a carrier constructs a
  non-tree holonomy source.

KILL-CHN.2 support connection as Laurent shift
  A proposal uses path-label products as the shift. The support tree has no
  nontrivial holonomy; adding a terminal wrap is the cyclic repair killed
  in doc 149.

KILL-CHN.3 support connection as torsor splitter
  A proposal uses labels to trivialize the DDG7b cocycle. Unit labels on the
  support tree do not construct b/phi(b)=c; res_1(c)=1 remains.

KILL-CHN.4 support-chain connection formable on controls
  Edge labels and gauges on a finite tree are shadow-level data. DH/Epstein
  have not died at a carrier-consuming correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 21 = doc 158:
  N1B_CONNECTION_HOLONOMY__SUPPORT_TREE_LABELS_GAUGE_TRIVIAL__NO_GO.

What got built: no new sub-object. The value is a deletion: support-chain
connections have no nontrivial holonomy.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  flag/idempotent/line, shift operator, selector/functional, and torsor
  splitter, with DH/Epstein death at that correspondence.
```
