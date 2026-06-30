# 282 - End augmented hyperbolic plane is not the square carrier

Status: no-go + End-augmented-hyperbolic deletion, 2026-06-21.
One-hundred-forty-fifth cycle of the doc-137 construction arc. Doc 281
showed that adding only a scalar trace slot to the hyperbolic endpoint plane
recovers diagonal counts but not off-diagonal graph pairings or graph
composition. This document tests the stronger repair:

```text
keep the hyperbolic endpoint plane, replace scalar trace by a full End
algebra, and add componentwise graph composition.
```

Witness, lead-reran this cycle:
`prime_int_n1b_end_augmented_hyperbolic_no_go` (EAH1-EAH7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_trace_augmented_hyperbolic_no_go`,
`prime_int_n1b_formal_ns_envelope_no_go`,
`prime_int_n1b_formal_correspondence_composition_no_go`,
`prime_int_n1b_hyperbolic_plane_rosati_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The scalar trace shadow in doc 281 fails because

```text
Tr(F^m) Tr(F^n) != Tr(F^(m+n)).
```

The immediate repair is to stop compressing the End component to trace. Use
formal triples

```text
(d1,z,d2),       z in End(V),
```

with the finite-field pairing

```text
(d1,z,d2).(e1,w,e2) = d1 e2 + d2 e1 - Tr(z w)
```

and componentwise graph law

```text
(d1,z,d2) o (e1,w,e2) = (d1 e1, z w, d2 e2).
```

This fixes the exact defect of doc 281: off-diagonal pairings and graph
composition now use the product `z w`, not products of scalar traces.

This document rejects only the shortcut:

```text
hyperbolic endpoint plane plus a formal End algebra is already the square
carrier.
```

It does not reject a future compactified square whose integral `rep_NS`
really produces such triples from proper correspondences.

## 2. Lemma

```text
Lemma 282.1 (formal End augmentation fixes trace shadows but not carrier
construction).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For the q=7, Tr(F)=1 finite-field anchor, the formal End-augmented
hyperbolic package with

    Delta=(1,Id,1),        Gamma_n=(q^n,F^n,1)

reproduces the diagonal counts

    7, 63, 364, ...

and the off-diagonal graph pairings, for example

    Gamma_1.Gamma_1 = 27,
    Gamma_1.Gamma_2 = 76,
    Gamma_2.Gamma_2 = 27.

The componentwise graph law also holds:

    Gamma_m o Gamma_n = Gamma_(m+n).

These are genuine positive checks: replacing scalar trace by the full End
slot fixes doc 281's product-trace defect.

However, the repair is still formal unless the compactified square produces
the End slot and graph classes. The DD.4 split uses only the endpoint
difference direction and the 1-unit line; it is independent of whether the
End label is `Id`, `F`, `F^2`, or an arbitrary control label. The same
formal `U+End(V)` envelope wraps off-circle data where componentwise
composition and the q-similitude identity hold but the primitive Hodge sign
is wrong. The same envelope is also formable on arbitrary control matrices
with no Euler product, Satake data, proper correspondences, carrier boundary,
or control death.

Consequently it constructs no actual `Qbar`, no carrier-produced integral
`rep_NS`, no proper correspondence category, no fiber-product composition,
no projection formula, no carrier Rosati duality, no positive primitive sign
theorem, no carrier boundary with control death, and no DD.4 carrier-native
weight>=1 datum.
```

Verdict label:

```text
N1B_END_AUGMENTED_HYPERBOLIC__FORMAL_END_ENVELOPE_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_end_augmented_hyperbolic_no_go` verifies seven gates.

EAH1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

EAH2 checks the positive repair. Full End augmentation reproduces both
diagonal counts and off-diagonal graph pairings in the finite-field model.

EAH3 checks the formal graph law. Componentwise End multiplication gives
`Gamma_m Gamma_n=Gamma_(m+n)` for the sampled powers.

EAH4 checks the coupling defect. The DD.4 split works with End labels
`Id`, `F`, `F^2`, and `control`, showing that the split is independent of
the formal End slot.

EAH5 checks off-circle formability. The same End envelope wraps an
off-circle q-similitude with exact componentwise composition and q-similitude
but positive primitive Hodge sign.

EAH6 checks control formability. An arbitrary control matrix admits the same
identity, graph law, and diagonal pairing without Euler product, Satake data,
properness, carrier boundary, or control death.

EAH7 applies the carrier-first contract. The package has formal `U+End`,
componentwise graph law, and DD.4 split, but not `Qbar`, carrier-produced
`rep_NS`, `Corr^prop`, fiber products, projection formula, carrier Rosati,
or control death.

## 4. Impact on R1

```text
R1 after docs 138-282:
  NEWLY CLOSED THIS CYCLE:
    - repairing trace-augmented hyperbolic data by adjoining a full formal
      End algebra;
    - treating product-sensitive matrix labels as carrier-produced rep_NS;
    - treating componentwise graph multiplication as proper correspondence
      composition;
    - treating a DD.4 endpoint split independent of End data as carrier
      boundary.

  POSITIVE INFORMATION RETAINED:
    - the full End component is exactly what scalar trace shadows were
      missing;
    - any surviving carrier must include the hyperbolic endpoint plane and a
      product-sensitive End/Frobenius component together;
    - diagonal counts, off-diagonal pairings, graph composition, and DD.4
      boundary must be consequences of one carrier, not separately attached
      formal slots.

  STILL ADMISSIBLE:
    - a compactified zeta square whose integral rep_NS functor produces
      triples `(d1,z,d2)` from actual proper correspondences;
    - a proof that componentwise End multiplication is the image of
      fiber-product composition under that functor;
    - a carrier-native coupling between DD.4 boundary, endpoint plane,
      Frobenius/Hecke graph, projection formula, Rosati, and control death;
    - a proof that no such carrier can exist, with a named mechanism and
      witness.

  STILL OPEN:
    - construct Qbar and show that `U+End` is represented by its proper
      correspondence category rather than assigned as a matrix envelope.
```

## 5. Kill conditions

```text
KILL-EAH.1 formal End slot promoted to rep_NS
  A proposal attaches End(V) to endpoint degrees and calls it rep_NS. Kill it
  unless the compactified square produces the End component.

KILL-EAH.2 componentwise multiplication promoted to composition
  A proposal defines `(d1,z,d2)o(e1,w,e2)=(d1e1,zw,d2e2)`. Kill it unless
  this is induced by actual proper correspondence/fiber-product composition.

KILL-EAH.3 DD.4 split independent of End data
  If the DD.4 split works without using the End/Frobenius graph component,
  it is still an attached boundary split. Kill it unless the carrier couples
  the boundary to graph composition and Rosati.

KILL-EAH.4 off-circle wrapper ignored
  A formal End envelope can wrap off-circle data. Kill it unless positivity
  is a carrier theorem, not a chosen matrix-pairing property.

KILL-EAH.5 control formability ignored
  Arbitrary controls admit the same formal `U+End` envelope. Kill any
  proposal where controls survive until a later filter.

KILL-EAH.6 CFC bypassed
  End-augmented hyperbolic data not embedded in the carrier-first square
  contract is not End(S^2/Z).
```
