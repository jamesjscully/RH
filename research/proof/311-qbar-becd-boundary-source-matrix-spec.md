# 311 - Qbar_BECD boundary-source matrix

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-seventy-fourth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 310 reduced the live Connes-Consani/CxC branch to:

```text
O+E is present;
construct actual B next.
```

This document imports the existing DD.4 boundary no-go bank into that target.
It separates the failed boundary sources by which atom of `B` they miss.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_boundary_source_matrix` (BSM1-BSM8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_endpoint_fixed_boundary_sieve`,
`prime_int_n1b_qbar_becd_phase_a_sieve`,
`prime_int_n1b_dd4_scc_interface`,
`prime_int_n1b_coinduced_dd4_extension_no_go`,
`prime_int_n1b_bar_resolution_boundary_no_go`,
`prime_int_n1b_laurent_field_hilbert90_no_go`, and
`prime_int_n1b_cartier_boundary_normal_no_go`.

## 1. Purpose

The word "boundary" is still too broad. The Phase-A boundary bundle is:

```text
B =
  M: actual carrier boundary map,
  L: exact localization,
  Z: DD.4 class mapped to zero,
  S: self-dual boundary/properness.
```

The banked DD.4 attempts do not all fail in the same way. Some make `c` a
formal coboundary, some delete or quotient it, some import a valuation axis,
and some supply plausible geometric direction data without the full carrier
properness package. The useful refinement is to keep only the boundary source
shape that can satisfy all four atoms at once.

## 2. Lemma

```text
Lemma 311.1 (boundary-source matrix).

On the current O+E line, product boundary shape still represents only:

    carrier_object, endpoint_maps.

The existing DD.4 boundary-source attempts divide as follows.

Formal coboundary sources:

    coinduced module,
    bar resolution,
    mapping cone / nullhomotopy.

These can make the class zero in an external resolution, but they lack the
carrier boundary map, self-dual properness, carrier-native source, unique
DD.4 direction, and non-formability on controls.

Deletion and quotient sources:

    jet deletion,
    obstruction quotient.

These do not preserve the original DD.4 class as a class mapped to zero by
the carrier. They delete or quotient the obstruction rather than producing B.

Norm-one / Hilbert-90 language:

    c * phi(c) = 1.

This is only the cocycle condition. In truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

External valuation sources:

    Laurent-field Hilbert 90,
    valuation degree character.

These can zero the named representative, but the valuation axis is not
carrier-native and loses the two independent endpoint degree maps.

Geometric direction sources:

    Cartier boundary normal,
    oriented boundary complex,
    boundary even lattice,
    product normal crossing.

These are shape evidence. They do not by themselves give all of M+L+Z+S.
The tested product normal-crossing window has 16 primitive directions, so
direction exposure is not direction selection.

Therefore none of the banked sources is actual B. The surviving B-shape is:

    a carrier-native boundary source on O+E that supplies
    M + L + Z + S,
    selects a unique DD.4 direction,
    preserves the endpoint rank,
    and is not formable on controls.

If that live B is constructed, the represented Phase-A slots become:

    carrier_object, endpoint_maps, DD.4_boundary_killing.

The only remaining Phase-A slot is then:

    control_death.
```

Verdict label:

```text
N1B_QBAR_BECD_BOUNDARY_SOURCE_MATRIX__CARRIER_NATIVE_SELF_DUAL_B_ON_OE__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_boundary_source_matrix` verifies eight gates.

BSM1 checks the active line: `O+E` gives `carrier_object, endpoint_maps`;
product boundary shape gives no `DD.4_boundary_killing`.

BSM2 classifies coinduction, bar resolution, and mapping cones as formal
coboundary sources. Their shared failure is absence of carrier map,
self-dual properness, carrier-nativity, unique direction, and control death.

BSM3 classifies jet deletion and obstruction quotient as deletion/quotient
sources. They do not preserve `c` as a class mapped to zero by the carrier.

BSM4 recomputes the DD.4 class and checks that norm-one language is only the
cocycle condition, not a boundary.

BSM5 classifies Laurent-field Hilbert 90 and valuation-degree characters:
they can zero the named representative but import an external valuation axis
and lose endpoint rank.

BSM6 classifies Cartier normals, oriented boundary complexes, even boundary
lattices, and product normal crossings as shape evidence rather than actual
B.

BSM7 checks that no banked source satisfies the live boundary-source
predicate, while the live predicate itself is coherent:

```text
carrier map + exact localization + DD.4 zero + self-dual properness
+ carrier-native source + unique direction + endpoint-rank preservation
+ non-formability on controls.
```

BSM8 checks that constructing live B on O+E leaves exactly formation-level
control death.

## 4. Impact on R1

```text
R1 after docs 138-311:
  NEWLY FIXED THIS CYCLE:
    - the active B target is no longer just "some boundary map."

  CURRENT CC/CxC PRODUCT LINE:
    - O+E is live.

  NEXT TARGETED CONSTRUCTION:
    - construct carrier-native self-dual B on O+E:
        actual boundary map,
        exact localization,
        DD.4 class mapped to zero,
        self-dual boundary/properness,
        unique DD.4 direction,
        endpoint-rank preservation,
        non-formability on controls.

  REJECTED AS NEXT MOVES:
    - formal coinduction/bar/cone zeroes;
    - deletion or quotient of the obstruction;
    - external valuation axes;
    - direction-only boundary geometry.

  STILL OPEN:
    - construct live B, then prove formation-level control death.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-BSM.1  A boundary proposal must supply M+L+Z+S together.
ACCEPT-BSM.2  The source must be carrier-native on O+E.
ACCEPT-BSM.3  The boundary must select the DD.4 direction uniquely.
ACCEPT-BSM.4  The construction must preserve two endpoint degree maps.
ACCEPT-BSM.5  The construction must not be formable on DH/Epstein/controls.

KILL-BSM.1    Reject external resolution coboundaries as B.
KILL-BSM.2    Reject deletion, quotient, or filtration loss of c.
KILL-BSM.3    Reject external valuation/uniformizer axes.
KILL-BSM.4    Reject direction-only boundary geometry.
KILL-BSM.5    Reject self-duality language without carrier properness.
```
