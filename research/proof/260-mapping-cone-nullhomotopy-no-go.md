# 260 - Mapping cone nullhomotopy is not the carrier boundary

Status: no-go + mapping-cone/nullhomotopy deletion, 2026-06-20.
One-hundred-twenty-third cycle of the doc-137 construction arc. Docs 257-259
left only the carrier-native DD.4 extension: the nonzero class
`[(1+z)^-1]` must die through a boundary/properness/self-duality map
produced by the actual square carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_mapping_cone_nullhomotopy_no_go` (MCN1-MCN6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_bar_resolution_boundary_no_go`,
`prime_int_n1b_coinduced_dd4_extension_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

After the coinduced and bar-resolution shortcuts fail, the next derived
repair is to replace the missing carrier boundary by a cone/cofiber:

```text
adjoin a formal nullhomotopy h with dh = c.
```

This document rejects only that shortcut. The mapping cone kills the class,
but it kills it by declaration. It is the derived form of formal splitter
insertion, not a construction of the square carrier.

## 2. Lemma

```text
Lemma 260.1 (mapping-cone nullhomotopy is not carrier boundary).

Let

    U_1 = 1 + z F_2[[z]],
    phi(z) = z/(1+z),
    c = (1+z)^-1.

In the base coefficient system, for truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Now form the formal cone repair by adjoining a nullhomotopy symbol h and
declaring

    dh = c.

Equivalently, enlarge the boundary subgroup B^1 by the single generator c.
Then the tested truncated cohomology becomes trivial:

    H^1_cone = 0.

However, if the declared boundary dh=c is removed, c is non-boundary again.
Thus the class dies exactly because the cone inserted c as a boundary. The
operation is formable for arbitrary controls: any chosen control class v can
be killed by adjoining h_v with dh_v=v.

The cone constructs no actual square, integral rep_NS, two degree maps,
indecomposable diagonal, Frobenius graph, proper correspondence category,
fiber-product composition, projection formula, canonical Rosati, positive
primitive sign, carrier boundary, or control death.

Consequently a mapping cone/cofiber/nullhomotopy of the DD.4 obstruction is
not construction-grade End(S^2/Z). A surviving route must produce the
boundary map from the actual square carrier rather than append a formal
nullhomotopy to the obstruction.
```

Verdict label:

```text
N1B_MAPPING_CONE_NULLHOMOTOPY__FORMAL_DH_EQUALS_C_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_mapping_cone_nullhomotopy_no_go` verifies six gates.

MCN1 recomputes the base obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and checks that `c` is non-boundary with `res_1(c)=1`.

MCN2 implements the cone repair exactly: the original boundary generators
are augmented by the extra declared boundary `c`. This makes the quotient
trivial:

```text
L6:  |B_cone|=2^4, |H1_cone|=1
L8:  |B_cone|=2^5, |H1_cone|=1
L10: |B_cone|=2^6, |H1_cone|=1
L12: |B_cone|=2^7, |H1_cone|=1
```

MCN3 removes the declared boundary and checks that `c` is non-boundary again.
That is the decisive failure: the cone supplies no independent carrier map.
It only records the instruction `dh=c`.

MCN4 repeats the same nullhomotopy recipe on exact additive `F_2` controls
in dimensions `1,2,4,8`. The recipe uses no square-carrier data.

MCN5 records the formal support addition:

```text
L=6:  6 -> 7
L=8:  8 -> 9
L=10: 10 -> 11
L=12: 12 -> 13
```

MCN6 applies the SCC contract: the mapping cone satisfies no square-carrier
slot.

## 4. Impact on R1

```text
R1 after docs 138-260:
  NEWLY CLOSED THIS CYCLE:
    - promoting the mapping cone, cofiber, or formal nullhomotopy of the
      DD.4 obstruction to the DD.4/SCC carrier boundary.

  STILL ADMISSIBLE:
    - a carrier-native boundary/properness/self-duality extension in which
      [c] maps to zero because the actual square carrier supplies the map;
    - a construction where that same map kills DH/Epstein/controls at
      carrier formation;
    - a proof that no such carrier-native extension can exist, with a named
      mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only the formal cone/nullhomotopy shortcut. It does not close a
carrier-native cofiber sequence whose maps and properness are constructed by
the square carrier and satisfy the SCC slots.

## 5. Kill conditions

```text
KILL-MCN.1 mapping cone promoted to carrier boundary
  A proposal says the DD.4 class dies because we pass to the cone/cofiber of
  c. Unless the cone map is produced by the actual square carrier, this is
  just the declaration dh=c.

KILL-MCN.2 nullhomotopy promoted to properness
  A formal h with dh=c is a derived splitter. It is not a properness or
  self-duality map.

KILL-MCN.3 control formability ignored
  Any control class can be killed by adjoining its own nullhomotopy. If the
  operation can be run before carrier formation, DH/Epstein have not died.

KILL-MCN.4 SCC slots bypassed
  A cone that kills one cohomology class but lacks the square, integral
  rep_NS, degree maps, diagonal, graph, proper correspondences, projection
  formula, Rosati, positive primitive sign, and control death is not
  End(S^2/Z).
```
