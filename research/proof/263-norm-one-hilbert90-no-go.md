# 263 - Norm-one is not the carrier boundary

Status: no-go + norm-one/Hilbert-90 deletion, 2026-06-20.
One-hundred-twenty-sixth cycle of the doc-137 construction arc. Docs 257-262
left only the carrier-native DD.4 extension: the nonzero class
`[(1+z)^-1]` must die through a boundary/properness/self-duality map
produced by the actual square carrier.

Witness, lead-reran this cycle:
`prime_int_n1b_norm_one_hilbert90_no_go` (NOH1-NOH5 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_obstruction_quotient_no_go`,
`prime_int_n1b_jet_deletion_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The next shortcut is to read the cocycle identity itself as the missing
properness/Rosati boundary:

```text
c * phi(c) = 1, therefore c is self-dual/norm-one, therefore it is harmless.
```

This document rejects only that shortcut. In this coefficient system,
norm-one is the cocycle condition. It is not the coboundary condition.

## 2. Lemma

```text
Lemma 263.1 (norm-one is not carrier boundary).

Let

    U_1 = 1 + z F_2[[z]],
    phi(z) = z/(1+z),
    c = (1+z)^-1.

For truncations L=6,8,10,12:

    c * phi(c) = 1,
    phi(c) = c^-1,
    res_1(c)=1.

Thus c is norm-one/self-dual in the bare C_2 coefficient system. However,
the coboundary subgroup is strictly smaller than the norm-one subgroup:

    |Norm_1(U_1)| / |B^1(U_1)| = 2,
    [c] != 0 in H^1(<phi>; U_1).

Equivalently,

    c * phi(c) = 1

only proves that c is a 1-cocycle. It does not produce b with

    b / phi(b) = c.

The same norm-one-not-boundary pattern is formable on controls: with a
trivial C_2-action in characteristic two, every class is norm-one while the
coboundary subgroup is zero.

Therefore the norm-one/Hilbert-90 slogan is not construction-grade
End(S^2/Z). It constructs no actual square, integral rep_NS, two degree
maps, indecomposable diagonal, Frobenius graph, proper correspondence
category, fiber-product composition, projection formula, canonical Rosati,
positive primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_NORM_ONE_HILBERT90__COCYCLE_NOT_CARRIER_BOUNDARY__NO_GO.
```

## 3. Proof

`prime_int_n1b_norm_one_hilbert90_no_go` verifies five gates.

NOH1 checks the base DD.4 class:

```text
L6,L8,L10,L12: c*phi(c)=1, phi(c)=c^-1, res_1(c)=1, c not in B^1.
```

NOH2 computes the exact index:

```text
L6:  |B|=2^3, |Norm1|=2^4, |Norm1/B|=2
L8:  |B|=2^4, |Norm1|=2^5, |Norm1/B|=2
L10: |B|=2^5, |Norm1|=2^6, |Norm1/B|=2
L12: |B|=2^6, |Norm1|=2^7, |Norm1/B|=2
```

Thus the norm-one identity leaves exactly the nontrivial DD.4 class.

NOH3 records the Hilbert-90 failure in this coefficient system:

```text
c*phi(c)=1 but no b has b/phi(b)=c.
```

NOH4 repeats the norm-one-not-boundary pattern on exact `F_2` controls in
dimensions `1,2,4,8`. No square-carrier data is used.

NOH5 applies the SCC contract: norm-one/self-duality in the coefficient
group satisfies no square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-263:
  NEWLY CLOSED THIS CYCLE:
    - promoting c*phi(c)=1, norm-one, self-dual, or Hilbert-90 language to
      the DD.4/SCC carrier boundary.

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

This closes only the norm-one slogan. It does not close a genuine Hilbert-90
theorem for a carrier-constructed coefficient object where the vanishing of
`H^1` is produced by the square carrier and the SCC slots survive.

## 5. Kill conditions

```text
KILL-NOH.1 norm-one promoted to carrier boundary
  A proposal says c is harmless because c*phi(c)=1. This is just the
  1-cocycle condition; it is not a coboundary.

KILL-NOH.2 Hilbert-90 slogan imported
  In U_1, norm-one classes strictly contain coboundaries. Kill any argument
  that imports Hilbert 90 without constructing a coefficient object where
  H^1 actually vanishes for carrier-native reasons.

KILL-NOH.3 self-duality confused with properness
  phi(c)=c^-1 is a coefficient-level identity. It is not the square
  carrier's properness/Rosati/self-duality map.

KILL-NOH.4 control formability ignored
  Norm-one-not-boundary examples exist in trivial characteristic-two
  controls. If the operation can be run before carrier formation,
  DH/Epstein have not died.

KILL-NOH.5 SCC slots bypassed
  A norm-one identity that lacks the square, integral rep_NS, degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, and control death is not End(S^2/Z).
```
