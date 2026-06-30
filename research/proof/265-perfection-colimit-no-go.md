# 265 - Perfection colimit is not the carrier boundary

Status: no-go + perfection/direct-colimit deletion, 2026-06-20.
One-hundred-twenty-eighth cycle of the doc-137 construction arc. Doc 264
showed that one Frobenius root kills the old DD.4 class only by introducing
a new lower-root obstruction. This document tests the stronger repair:

```text
pass to the whole Frobenius-root tower / perfect closure / filtered colimit.
```

Witness, lead-reran this cycle:
`prime_int_n1b_perfection_colimit_no_go` (PCL1-PCL6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_frobenius_root_extension_no_go`,
`prime_int_n1b_norm_one_hilbert90_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The direct-limit version is subtler than doc 264. At a finite root stage
there is always a new obstruction, but in the filtered colimit every finite
representative is killed one stage later:

```text
c_n = (1+t_n)^-1,
t_n = t_{n+1}^2,
c_n |_{t_n=t_{n+1}^2} = c_{n+1}^2 = c_{n+1}/phi(c_{n+1}).
```

So the colimit can make the obstruction disappear as a stable finite
representative. This is real algebra. It is still not the square-carrier
boundary. It is moving-boundary vanishing with no terminal carrier object.

## 2. Lemma

```text
Lemma 265.1 (perfection colimit is moving-boundary vanishing).

For every finite stage n, set

    U_n = 1 + t_n F_2[[t_n]],
    phi_n(t_n) = t_n/(1+t_n),
    c_n = (1+t_n)^-1.

Then

    H^1(<phi_n>; U_n) = Z/2,
    [c_n] != 0,
    res_1(c_n)=1.

The root transition

    t_n = t_{n+1}^2

is compatible with the shear, and sends the generator to a coboundary:

    c_n |_{t_n=t_{n+1}^2}
      = (1+t_{n+1})^-2
      = c_{n+1}/phi_{n+1}(c_{n+1}).

Thus the induced map on the detected generator is zero.

For every finite tower

    U_0 -> U_1 -> ... -> U_N

all lower-stage generators have become boundaries in `U_N`, but the top
class `c_N` is still nonzero. The witness checks depths 1,2,3,4 with support
ranks

    6, 12, 24, 48.

Consequently any vanishing in the full perfection colimit uses the absence
of a terminal stage:

    every finite representative dies later,
    no finite top stage contains all the deaths,
    support ranks grow without bound.

This same moving-boundary recipe is formable on controls. Therefore the
perfection colimit constructs no actual square, integral rep_NS, two degree
maps, indecomposable diagonal, Frobenius graph, proper correspondence
category, fiber-product composition, projection formula, canonical Rosati,
positive primitive sign, carrier boundary, or control death.
```

Verdict label:

```text
N1B_PERFECTION_COLIMIT__MOVING_BOUNDARY_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_perfection_colimit_no_go` verifies six gates.

PCL1 recomputes the finite-stage obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, H1=2
L8:  |B|=2^4, |Z1|=2^5, H1=2
L10: |B|=2^5, |Z1|=2^6, H1=2
L12: |B|=2^6, |Z1|=2^7, H1=2
```

PCL2 checks the root transition:

```text
L6 -> L12:  c_n maps to delta(c_{n+1})
L8 -> L16:  c_n maps to delta(c_{n+1})
L10 -> L20: c_n maps to delta(c_{n+1})
L12 -> L24: c_n maps to delta(c_{n+1})
```

PCL3 checks finite towers:

```text
depth 1: rank 6,  survives c_1
depth 2: rank 12, survives c_2
depth 3: rank 24, survives c_3
depth 4: rank 48, survives c_4
```

Every lower class is killed by a displayed boundary at the top stage, but
the top class is detected by `res_1`, which kills generator boundaries.

PCL4 records the direct-limit cost:

```text
ranks = [3, 6, 12, 24, 48, 96, 192]
kill depths = [1, 2, 3, 4, 5, 6]
```

The vanishing depends on unbounded support and no terminal stage.

PCL5 repeats the moving-boundary pattern on exact `F_2` controls in
dimensions `1,2,4,8`. No square-carrier data is used.

PCL6 applies the SCC contract: the perfection colimit supplies no
square-carrier slot.

## 4. Impact on R1

```text
R1 after docs 138-265:
  NEWLY CLOSED THIS CYCLE:
    - passing from one Frobenius root to the full perfect closure or filtered
      colimit and treating colimit vanishing as the DD.4/SCC boundary.

  STILL ADMISSIBLE:
    - a carrier-native boundary/properness/self-duality extension in which
      [c] maps to zero because the actual square carrier supplies the map;
    - a carrier-constructed perfectoid/prismatic/Frobenius-root object whose
      boundary map is produced by the square and preserves SCC slots;
    - a construction where that same map kills DH/Epstein/controls at
      carrier formation;
    - a proof that no such carrier-native extension can exist, with a named
      mechanism and witness.

  STILL OPEN:
    - construct the actual carrier-native DD.4 extension;
    - then construct the zeta-side square carrier over Z.
```

This closes only bare perfection-colimit vanishing. It does not close a
perfected object downstream of a real square carrier.

## 5. Kill conditions

```text
KILL-PCL.1 perfect closure promoted to carrier boundary
  A proposal passes to all 2-power roots and says H^1 vanishes. Kill it
  unless the square carrier constructs the boundary/properness/self-duality
  map and the SCC slots survive.

KILL-PCL.2 moving boundary confused with finite carrier map
  In every finite tower a top-stage obstruction remains. Direct-limit
  vanishing works only because each representative is killed later.

KILL-PCL.3 unbounded support ignored
  The root tower grows support without bound. Projection, compactness,
  properness, or a finite correspondence calculus is extra data unless
  carrier-constructed.

KILL-PCL.4 control formability ignored
  Moving-boundary colimits can be formed on controls before carrier
  formation. If this is the only death mechanism, DH/Epstein have not died.

KILL-PCL.5 SCC slots bypassed
  A perfection colimit that lacks the square, integral rep_NS, degree maps,
  diagonal, graph, proper correspondences, projection formula, Rosati,
  positive primitive sign, and control death is not End(S^2/Z).
```
