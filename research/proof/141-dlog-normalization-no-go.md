# 141 - dlog(1+z) is an obstruction detector, not a pinning

Status: no-go + R1 escape deletion, 2026-06-20. Fourth cycle of the
doc-137 construction arc. It attacks the surviving named external
normalization from docs 138-140: the proposed `dlog(1+z)` pinning of the
weight>=1 torsor. Result: `dlog(1+z)` is indeed `phi`-invariant, but it
does not trivialize the DDG7b cocycle. It carries the same leading
obstruction bit in the differential module.

Witness, lead-reran this cycle:
`prime_int_dlog_normalization_no_go` (DLG1-DLG6 ALL PASS) -- exact
`F_2[[z]]` truncated formal-series computation for the shear action on
1-forms.

## 1. Purpose

Docs 138-140 left two construction-grade R1 exits:

```text
1. an external phi-invariant normalization, with dlog(1+z) named as the
   candidate pinning;
2. a different carrier where the full line and weight>=1 datum survive.
```

This cycle tests the first exit. The test is forced by doc 138. Let

```text
phi(z) = z/(1+z),
c = (1+z)^-1.
```

The DDG7b obstruction vanishes only if `c` is a shear coboundary:

```text
c = b / phi(b)
```

for some `1`-unit `b`. Applying `dlog`, any such solution would imply

```text
dlog(c) = dlog(b) + phi^* dlog(b).
```

So a dlog-normalization can only pin the torsor if `dlog(c)` lies in the
trace image `alpha -> alpha + phi^* alpha` on 1-forms.

It does not.

## 2. Lemma

```text
Lemma 141.1 (the dlog form is invariant but not a coboundary
normalization). In characteristic 2, with `phi(z)=z/(1+z)` and
`c=(1+z)^-1`,

  omega := dlog(c) = dz/(1+z)

is `phi`-invariant. However `omega` is not in the image of

  Tr_phi: Omega^1 -> Omega^1,
  alpha |-> alpha + phi^* alpha.

Indeed, for `alpha=A(z) dz`, the constant coefficient of
`alpha + phi^* alpha` is always `A(0)+A(0)=0`, since `phi(0)=0` and
`phi'(0)=1`. But `omega` has constant coefficient `1`.

Therefore the invariant form `dlog(1+z)` cannot select a
Weyl-shear-fixed torsor representative. It detects the same obstruction
as `res_1(c)=1`; it does not kill it.
```

Verdict label:

```text
DLOG_NORMALIZATION__PHI_INVARIANT_BUT_NOT_TRACE__NO_GO.
```

## 3. Proof

`prime_int_dlog_normalization_no_go` verifies the formal-series identities
at truncations `4,6,8,10,12` over `F_2`.

DLG1 verifies that `phi` is an involution.

DLG2 verifies

```text
phi^*(dz/(1+z)) = dz/(1+z).
```

DLG3 records that `omega=dz/(1+z)` has nonzero constant coefficient.

DLG4 enumerates all truncated 1-forms `alpha=A(z)dz` and checks that every
trace `alpha + phi^*alpha` has zero constant coefficient.

DLG5 enumerates the trace image and checks that `omega` is not in it.

DLG6 records the bridge to doc 138:

```text
res_1((1+z)^-1) = 1,
const(dlog((1+z)^-1)) = 1.
```

The differential calculation preserves the leading obstruction bit.

## 4. Impact on R1

```text
R1 after docs 138-141:

  CLOSED AS DD.4-UNLOCKING ROUTES:
    - Weyl-shear-fixed weight>=1 extension (doc 138);
    - full N1-b' Laurent-line comparison in TCR^{phi} (doc 139);
    - bottom class as multiplicative Lin generator (doc 140);
    - dlog(1+z) as an external phi-invariant torsor pinning (doc 141).

  STILL OPEN:
    - a genuinely different carrier where a full line and weight>=1 datum
      exist, with DH/Epstein death at named points.
```

R1 is not solved, but the named in-house exit is gone. The next valid R1
cycle must present a different carrier, not another normalization of the
same `U_1` torsor. A normalization living in the same unit/differential
disk must first pass the `Tr_phi` test above and the doc-138 `res_1` test.

R2 remains locked.

## 5. Kill Conditions

```text
KILL-DLOG.1 invariant form promoted to pinning
  A proposal says `dlog(1+z)` supplies the missing phi-invariant
  normalization. It does not: it is invariant but not a trace/coboundary
  trivialization.

KILL-DLOG.2 differential shadow mistaken for unit torsor solution
  A proposal moves from the unit torsor to differentials and claims the
  obstruction vanished. The constant term of `dlog(c)` is nonzero, while
  every differential trace has constant term zero.

KILL-DLOG.3 same-carrier normalization without res_1 death
  A proposal stays in the `U_1`/disk carrier and chooses a torsor
  representative. It must exhibit `c` as a coboundary and kill
  `res_1(c)=1`; otherwise it is a choice, not a construction.
```

## 6. Board

```text
doc-137 R1, cycle 4 = doc 141:
  DLOG_NORMALIZATION__PHI_INVARIANT_BUT_NOT_TRACE__NO_GO.

What got built: no new sub-object. The value is a deletion: the named
dlog pinning is an obstruction detector.

Next valid R1 work:
  produce a different carrier where the full line and weight>=1 datum
  exist, with runnable witness and DH/Epstein death at named points.
```
