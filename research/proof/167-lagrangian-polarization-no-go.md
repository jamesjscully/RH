# 167 - Support Lagrangians do not identify the Tate halves

Status: no-go + Lagrangian/polarization half-identification repair deletion,
2026-06-20. Thirtieth cycle of the doc-137 construction arc. Doc 166 killed
the support hyperbolic form/swap as automatic Tate boundary glue because the
form is full duality `W -> W^vee`, turning it into an operator requires
dual-to-primal matching data, and the inserted swap is not a Laurent
generator. This document tests the next repair: use a canonical
polarization/Lagrangian half of the hyperbolic Tate object to supply the
half-identification.

Witness, lead-reran this cycle:
`prime_int_n1b_lagrangian_polarization_no_go` (LPG1-LPG13 ALL PASS) --
exact finite-window Lagrangian-count, graph-Lagrangian, half-matching,
boundary-glue, twist, selector, obstruction, and control-formability checks.

## 1. Purpose

The hyperbolic-swap repair can now say:

```text
do not insert a swap;
choose the canonical Lagrangian/polarization half of the Tate object;
that half identifies the two sides and gives the carrier boundary glue.
```

The standard Tate halves are Lagrangians, but they are two halves:

```text
M,       M^vee.
```

Choosing one half does not identify it with the other. General Lagrangian
choices are worse: they overproduce. Graph Lagrangians also overproduce and
still require matching data between the primal and dual support windows.

Most importantly, a Lagrangian is a submodule. The missing datum is a map:

```text
dual boundary line -> primal boundary line,
```

plus the Laurent twist that makes it the carrier shift. A support-level
polarization half does not construct that map.

This document is local. It does not reject carrier-native polarizations or
carrier-native Lagrangians. It rejects only Lagrangian/polarization choices
formed from the visible support Tate module.

## 2. Lemma

```text
Lemma 167.1 (support Lagrangians are half choices, not half-identifications).
Let M_N = R_DMP[-1..N] tensor L ~= L^r, with r=N+2 and
L=F_2[u^{+-1}]. Let W_N = M_N plus M_N^vee.

For r=3,4,6,10, the Tate windows have ranks:

  6,8,12,20.

The standard hyperbolic halves give two choices:

  2,2,2,2.

They do not identify each other.

The total number of Lagrangian subspaces in the finite F_2 hyperbolic model
is:

  135,2295,4922775,85817142703524375.

Even restricting to graph Lagrangians over a fixed half leaves:

  64,1024,2097152,36028797018963968

choices.

Graph Lagrangians still require dual-to-primal matching data; coordinate
matching counts are:

  6,24,720,3628800.

A Lagrangian outputs a submodule, not the rank-one boundary glue map. The
boundary glue rank still needed is:

  1,1,1,1.

A Lagrangian is also not a Laurent generator.

Laurent unit twists in windows |k|<=1,2,4,8 remain:

  3,5,9,17.

Boundary endpoint-pair choices remain:

  9,16,36,100.

Rank-one idempotent counts in the doubled Tate windows remain:

  2016,32640,8386560,549755289600.

The package constructs no DMP multiplication, no carrier-native Lagrangian,
no carrier-native half-identification, no pinned Laurent twist, and no torsor
splitter. The bottom obstruction remains y^2=0, there is still no DMP degree
-2, the shear obstruction remains res_1(c)=1, and the same
Lagrangian-polarization package is formable on controls.

Therefore support Lagrangian/polarization data is not construction-grade R1
carrier half-identification. A surviving route must construct the
Lagrangian, half-identification, and Laurent twist as carrier-native
correspondence data and prove DH/Epstein death at that construction.
```

Verdict label:

```text
N1B_LAGRANGIAN_POLARIZATION__HALF_CHOICE_NOT_CARRIER_HALF_IDENTIFICATION__NO_GO.
```

## 3. Proof

`prime_int_n1b_lagrangian_polarization_no_go` verifies the finite-window
models.

LPG1 records the support tensor ranks:

```text
N = 1,2,4,8  =>  r = 3,4,6,10.
```

LPG2 records the doubled Tate/hyperbolic window ranks:

```text
6,8,12,20.
```

LPG3 records the standard-half point:

```text
M and M^vee are two halves, not an identification.
```

LPG4 records total Lagrangian counts:

```text
135,2295,4922775,85817142703524375.
```

LPG5 records graph-Lagrangian counts:

```text
64,1024,2097152,36028797018963968.
```

LPG6 records the matching data still needed for graph Lagrangians:

```text
6,24,720,3628800.
```

LPG7 records the type mismatch:

```text
Lagrangian choice = submodule,
boundary glue = rank-one map.
```

LPG8 records that Lagrangian choice is not a Laurent generator.

LPG9 records Laurent unit twist choices:

```text
3,5,9,17.
```

LPG10 records the surviving selector problem. Endpoint-pair choices remain:

```text
9,16,36,100.
```

Rank-one idempotent counts in Tate windows remain:

```text
2016,32640,8386560,549755289600.
```

LPG11 records the base obstructions:

```text
y^2 = 0,     dim[-2] = 0,     res_1(c)=1,
```

and records that no DMP multiplication and no relation `b/phi(b)=c` has been
constructed.

LPG12 applies the carrier guard: Lagrangian choices in finite hyperbolic
support modules are shadow-level data, so controls can form the same package.
LPG13 records the only escape.

## 4. Impact on R1

```text
R1 after docs 138-167:

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
      (doc 167).

  STILL OPEN:
    - a genuinely different carrier whose first correspondence/multiplication
      produces the arrows/inverse arrows/nontrivial isotropy/holonomy/
      deformation parameter/monodromy operator/non-split gluing/derived
      operation/completed two-sided orbit/Tate duality with carrier-native
      boundary self-duality, Lagrangian, half-identification, and Laurent
      twist/flag/idempotent/line, selector/functional/shift operator, torsor
      splitter, and weight>=1 datum from carrier data, and where DH/Epstein
      controls fail before signs, zeros, or comparison.
```

R1 is still open. Lagrangian/polarization data is admissible only if the
carrier constructs the Lagrangian, half-identification, and Laurent twist.
Support Lagrangians alone are bookkeeping.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-LPG.1 standard Tate half as half-identification
  A proposal uses M or M^vee as the canonical half-identification. The two
  standard halves are Lagrangians, but choosing one does not identify them.

KILL-LPG.2 Lagrangian choice as carrier selection
  A proposal chooses a Lagrangian in the support Tate module. Lagrangian
  choices overproduce; graph Lagrangians also overproduce and require
  half-matching data.

KILL-LPG.3 Lagrangian as boundary glue or Laurent generator
  A proposal uses a Lagrangian as the boundary glue or shift. A Lagrangian is
  a submodule, not the rank-one boundary map or a Laurent generator.

KILL-LPG.4 Lagrangian-polarization package formable on controls
  Lagrangian choices, graph Lagrangians, and half-matching normalizations are
  shadow-level operations. DH/Epstein have not died at a carrier-consuming
  correspondence map.
```

## 6. Board

```text
doc-137 R1, cycle 30 = doc 167:
  N1B_LAGRANGIAN_POLARIZATION__HALF_CHOICE_NOT_CARRIER_HALF_IDENTIFICATION__NO_GO.

What got built: no new sub-object. The value is a deletion: support
Lagrangians choose halves or graphs, but do not construct the
half-identification or rank-one boundary glue.

Next valid R1 work:
  construct the first carrier-native correspondence/multiplication whose
  object data supply the arrows/inverse arrows/nontrivial isotropy/holonomy/
  deformation parameter/monodromy operator/non-split gluing/derived
  operation/completed two-sided orbit/Tate duality with carrier-native
  boundary self-duality, Lagrangian, half-identification, and Laurent twist/
  flag/idempotent/line, shift operator, selector/functional, and torsor
  splitter, with DH/Epstein death at that correspondence.
```
