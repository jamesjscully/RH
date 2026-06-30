# 266 - Root-shift telescope is not the carrier boundary

Status: no-go + root-shift/telescope deletion, 2026-06-20.
One-hundred-twenty-ninth cycle of the doc-137 construction arc. Doc 265
closed bare perfection-colimit vanishing: every finite-stage DD.4 class dies
one root later, but every finite tower has a new top-stage obstruction. This
document tests the next repair:

```text
promote the Frobenius-root transition itself to a shift/telescope operator.
```

Witness, lead-reran this cycle:
`prime_int_n1b_root_shift_telescope_no_go` (RST1-RST5 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_perfection_colimit_no_go`,
`prime_int_n1b_frobenius_root_extension_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The tempting repair is to say that the root tower supplies a shift:

```text
S: c_n -> c_{n+1},
```

and then to use a telescope, periodic wrap, or formal inverse `S^-1` to turn
the moving-boundary vanishing of doc 265 into a finite carrier boundary.

This document rejects only that shortcut. The Frobenius-root transition is
not an invertible shift on the obstruction line. It sends the old generator
to zero in cohomology.

## 2. Lemma

```text
Lemma 266.1 (root transition is zero, not an invertible carrier shift).

At finite root stage n, let

    U_n = 1 + t_n F_2[[t_n]],
    phi_n(t_n) = t_n/(1+t_n),
    c_n = (1+t_n)^-1.

Then

    H^1(<phi_n>; U_n) = Z/2,
    [c_n] != 0.

Under the root transition `t_n=t_{n+1}^2`,

    c_n |_{t_n=t_{n+1}^2}
      = c_{n+1}^2
      = c_{n+1}/phi(c_{n+1}).

Thus the induced map on the DD.4 obstruction line is

    [c_n] -> 0,

not an isomorphism. It cannot be inverted as a carrier shift without adding
new data.

For a finite tower embedded in the top variable `t_N`, the stage generators
have exponents

    c_j = c_N^(2^(N-j)).

The boundary of an internal candidate has exponent doubled. To kill the top
class `c_N`, one would need an exponent `1/2`, i.e. a new root beyond the
finite tower. The witness checks depths 1,2,3,4:

    depth 1: internal exponents [2,1], need 1/2
    depth 2: internal exponents [4,2,1], need 1/2
    depth 3: internal exponents [8,4,2,1], need 1/2
    depth 4: internal exponents [16,8,4,2,1], need 1/2

A periodic wrap or formal inverse shift supplies exactly that missing
half-root relation by declaration. The same declaration is formable on
controls. Therefore the root-shift telescope constructs no actual square,
integral rep_NS, two degree maps, indecomposable diagonal, Frobenius graph,
proper correspondence category, fiber-product composition, projection
formula, canonical Rosati, positive primitive sign, carrier boundary, or
control death.
```

Verdict label:

```text
N1B_ROOT_SHIFT_TELESCOPE__ZERO_TRANSITION_NOT_CARRIER_SHIFT__NO_GO.
```

## 3. Proof

`prime_int_n1b_root_shift_telescope_no_go` verifies five gates.

RST1 computes the root transition:

```text
L6 -> L12:  H1 generator maps to 0
L8 -> L16:  H1 generator maps to 0
L10 -> L20: H1 generator maps to 0
L12 -> L24: H1 generator maps to 0
```

The source and target each have `H1=Z/2`, but the transition sends the
source generator to a target coboundary.

RST2 checks finite towers:

```text
depth 1: rank 8,  exponents [2,1]
depth 2: rank 16, exponents [4,2,1]
depth 3: rank 32, exponents [8,4,2,1]
depth 4: rank 64, exponents [16,8,4,2,1]
```

At each finite height, the top class is detected by `res_1`, while all
internal-stage boundaries have `res_1=0`.

RST3 records the periodic-wrap obstruction:

```text
needed exponent = 1/2
available finite exponents = powers of 2 down to 1.
```

RST4 repeats the formal inverse-shift/splitter move on exact `F_2` controls
in dimensions `1,2,4,8`. No square-carrier data is used.

RST5 applies the SCC contract: a root-shift telescope supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-266:
  NEWLY CLOSED THIS CYCLE:
    - promoting the root transition, telescope, periodic wrap, or formal
      inverse root-shift to the carrier boundary.

  STILL ADMISSIBLE:
    - a carrier-native boundary/properness/self-duality extension in which
      [c] maps to zero because the actual square carrier supplies the map;
    - a carrier-constructed root/perfection object whose transition is
      accompanied by properness, projection, Rosati, and control death from
      the square carrier itself;
    - a construction where that same map kills DH/Epstein/controls at
      carrier formation;
    - a proof that no such carrier-native extension can exist, with a named
      mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only formal root-shift/telescope promotion. It does not close a
real carrier transition that is produced by the square and preserves all SCC
slots.

## 5. Kill conditions

```text
KILL-RST.1 root transition promoted to invertible shift
  The transition sends the DD.4 H1 generator to zero. Kill any argument that
  treats it as an invertible carrier shift without constructing extra
  carrier data.

KILL-RST.2 finite telescope hides the top obstruction
  Every finite root tower still has a top class. Killing it requires a
  half-root outside the tower.

KILL-RST.3 periodic wrap imported
  A wrap from the missing next root back into a finite stage imposes an
  external half-exponent relation. It is not produced by the coefficient
  arithmetic.

KILL-RST.4 formal inverse shift imported
  A formal inverse shift kills the class exactly as a splitter insertion.
  The same move is formable on controls.

KILL-RST.5 SCC slots bypassed
  A root-shift telescope that lacks the square, integral rep_NS, degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, and control death is not End(S^2/Z).
```
