# 280 - Hyperbolic plane Rosati is not the square carrier

Status: no-go + hyperbolic-plane/Rosati deletion, 2026-06-21.
One-hundred-forty-third cycle of the doc-137 construction arc. Doc 279
showed that boundary evenness is exactly the parity theorem needed for
total/difference endpoint decoding, but not a carrier theorem by itself.
This document tests the strongest nearby repair:

```text
make the same-parity endpoint lattice an actual even hyperbolic
intersection plane, with Rosati swapping the two isotropic endpoints.
```

Witness, lead-reran this cycle:
`prime_int_n1b_hyperbolic_plane_rosati_no_go` (HPR1-HPR8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_boundary_even_lattice_no_go`,
`prime_int_n1b_oriented_boundary_complex_no_go`,
`prime_int_n1b_endpoint_parity_saturation_no_go`,
`prime_int_n1b_dd4_scc_interface`,
`prime_int_n1b_square_carrier_contract`, and
`prime_int_n1b_carrier_first_categorical_square_contract`.

## 1. Purpose

Doc 279 left a constructive-looking possibility. Instead of selecting the
same-parity sublattice inside total/difference coordinates, maybe the square
should contain a hyperbolic plane

```text
U = Z e + Z f,        e^2=f^2=0,        e.f=1,
```

with endpoint degrees read from the isotropic basis. Then every vector
`v=x e+y f` has

```text
s = x+y,        a = x-y,
```

so `s` and `a` have the same parity automatically, and the inverse

```text
x=(s+a)/2,      y=(s-a)/2
```

is integral. The endpoint swap `tau(e)=f` is a Rosati-looking isometry, and
the anti-invariant direction `e-f` is exactly the oriented DD.4 direction.

This document rejects only the shortcut:

```text
an abstract hyperbolic endpoint plane with Rosati swap is the square carrier.
```

It does not reject a future `Qbar` whose integral `rep_NS` lattice contains
such a plane as part of the full correspondence geometry.

## 2. Lemma

```text
Lemma 280.1 (hyperbolic endpoint/Rosati data is not the carrier).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Let U be the hyperbolic plane with pairing

    <(x,y),(u,v)> = x v + y u.

Then the basis vectors e=(1,0), f=(0,1) are isotropic and <e,f>=1.
For every v=(x,y), the total/difference coordinates

    s=x+y,        a=x-y

have same parity and decode integrally back to (x,y). The endpoint swap

    tau(x,y)=(y,x)

is an isometry, fixes total degree, and negates the difference direction.
With the valuation twist

    sigma((v,u)) = (v, c^(x-y) phi(u)),

the vector e splits the DD.4 representative c.

However, the plain endpoint swap is only an isometry of U. To commute with
the anti-invariant DD.4 twist it must be lifted to the unit line by

    u |-> u^-1.

That lift is extra data unless it is produced by the actual square carrier.
More importantly, the hyperbolic plane sees only endpoint degrees. In the
finite-field `rep_NS` model, the diagonal/Frobenius graph count is

    Delta . (q,F,1) = q + 1 - Tr(F).

For q=7, endpoint data (7,1) gives the same hyperbolic boundary value 8 for
trace 1 and trace 3, while `rep_NS` counts are 7 and 5. Thus the
hyperbolic boundary plane forgets the End/Frobenius graph component.

The abstract plane supplies no proper correspondence category, no
fiber-product composition, no projection formula, no indecomposable
diagonal, no positive primitive Rosati/Hodge sign, and no control death. The
same hyperbolic/Rosati/DD.4 package is formable on controls. Therefore it
does not construct `End(S^2/Z)`.
```

Verdict label:

```text
N1B_HYPERBOLIC_PLANE_ROSATI__ENDPOINT_LATTICE_NOT_REP_NS_GRAPH__NO_GO.
```

## 3. Proof

`prime_int_n1b_hyperbolic_plane_rosati_no_go` verifies eight gates.

HPR1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

HPR2 checks the positive endpoint-lattice fact: the hyperbolic basis
packages parity, isotropic endpoints, and integral total/difference
decoding.

HPR3 checks the Rosati-looking symmetry: endpoint swap is an isometry, fixes
the total direction, and negates the difference direction.

HPR4 checks the DD.4 lift defect. The plain swap is a lattice isometry but
does not commute with the anti-invariant DD.4 twist; the inverse-unit lift
does commute. That lift is not supplied by the abstract plane.

HPR5 checks graph blindness. Endpoint vector `(7,1)` has the same hyperbolic
boundary value for two traces, while the finite-field `rep_NS` counts
`7+1-1=7` and `7+1-3=5` differ.

HPR6 records that the hyperbolic plane supplies no proper graph composition:
no `Corr^prop`, fiber products, projection formula, indecomposable diagonal,
or End component.

HPR7 attaches the same hyperbolic/Rosati/DD.4 package to controls in
dimensions 2,4,8. No square data is consumed and controls do not die.

HPR8 applies the SCC/CFC contract: endpoint lattice, parity, swap, and DD.4
split do not construct `Qbar`, integral `rep_NS` with End component, graph,
composition, positive Rosati sign, projection, or control death.

## 4. Impact on R1

```text
R1 after docs 138-280:
  NEWLY CLOSED THIS CYCLE:
    - promoting an abstract hyperbolic endpoint plane plus Rosati swap to
      the square carrier;
    - treating endpoint integrality/parity/Rosati-swap data as enough to
      replace full rep_NS graph data.

  POSITIVE INFORMATION RETAINED:
    - a future carrier may well contain a hyperbolic endpoint plane;
    - such a plane is the correct shape for integral total/difference
      decoding and endpoint swap;
    - the missing ingredient is not parity anymore but the carrier-native
      coupling of this plane to the End/Frobenius graph component,
      composition, projection formula, positive Rosati sign, and control
      death.

  STILL ADMISSIBLE:
    - a compactified zeta square whose integral rep_NS lattice contains the
      hyperbolic endpoint plane as a subquotient of actual correspondences;
    - a theorem that the DD.4 boundary, Rosati duality, Frobenius/Hecke
      graph, and endpoint degrees are all produced by one proper
      correspondence category;
    - a proof that no such square can exist, with a named mechanism and
      witness.

  STILL OPEN:
    - construct Qbar and prove that the hyperbolic endpoint plane is only
      one visible face of the full integral rep_NS correspondence lattice.
```

## 5. Kill conditions

```text
KILL-HPR.1 hyperbolic endpoint plane promoted to rep_NS
  A proposal says U=<e,f> gives integral endpoints and Rosati, hence the
  square exists. Kill it unless U is produced by the compactified carrier as
  part of integral rep_NS.

KILL-HPR.2 End/Frobenius trace forgotten
  Endpoint degrees alone see q+1, not q+1-Tr(F). Kill any proposal whose
  lattice cannot distinguish Frobenius graphs with equal endpoint degrees and
  different End traces.

KILL-HPR.3 Rosati lift declared
  The swap of U must lift to the DD.4 unit line and the full correspondence
  duality. Kill it if the lift u |-> u^-1 is inserted rather than derived.

KILL-HPR.4 composition replaced by pairing
  A bilinear form is not fiber-product composition. Kill it unless the
  proposal constructs Corr^prop, graph composition, and projection formula.

KILL-HPR.5 control formability ignored
  Hyperbolic planes with swaps and DD.4 twists can be attached to controls.
  If controls survive until a later filter, carrier formation has failed.

KILL-HPR.6 CFC bypassed
  Hyperbolic/Rosati data not embedded in the carrier-first square contract is
  not End(S^2/Z).
```
