# 281 - Trace augmented hyperbolic plane is not the square carrier

Status: no-go + trace-augmented-hyperbolic deletion, 2026-06-21.
One-hundred-forty-fourth cycle of the doc-137 construction arc. Doc 280
showed that a hyperbolic endpoint plane gives the right endpoint integrality
and Rosati-swap shape, but forgets the End/Frobenius trace component of
`rep_NS`. This document tests the immediate repair:

```text
keep the hyperbolic endpoint plane and add a scalar trace slot so
Delta.Gamma_n = q^n + 1 - Tr(F^n).
```

Witness, lead-reran this cycle:
`prime_int_n1b_trace_augmented_hyperbolic_no_go` (TAH1-TAH7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_hyperbolic_plane_rosati_no_go`,
`prime_int_n1b_diagonal_trace_graph_no_go`,
`prime_int_n1b_finite_trace_realization_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 280 isolated the missing piece in the bare endpoint plane. The
hyperbolic part supplies

```text
d1 e2 + d2 e1,
```

but the finite-field `rep_NS` form is

```text
(d1,z,d2).(e1,w,e2) = d1 e2 + d2 e1 - Tr(z w).
```

The tempting repair is to attach only the scalar trace

```text
t_n = Tr(F^n)
```

to the hyperbolic graph label. Then the diagonal shadow

```text
Delta_shadow = (1,1,1),        Gamma_n_shadow = (q^n, Tr(F^n), 1)
```

with pairing

```text
(d1,t,d2).(e1,s,e2)=d1 e2+d2 e1-t s
```

does reproduce

```text
Delta_shadow . Gamma_n_shadow = q^n + 1 - Tr(F^n).
```

This document rejects only the shortcut:

```text
hyperbolic endpoint plane plus scalar trace slot constructs the square
carrier.
```

It does not reject a future carrier whose full End component has trace as
one shadow.

## 2. Lemma

```text
Lemma 281.1 (scalar trace augmentation is not the End component).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For the q=7, Tr(F)=1 finite-field anchor, the trace-augmented hyperbolic
shadow reproduces the diagonal point-count intersections:

    n=1: 7
    n=2: 63
    n=3: 364
    n=4: 2331

But this scalar trace slot is not the End component. Off diagonal, the real
`rep_NS` graph pairing uses

    Tr(F^m F^n)=Tr(F^(m+n)),

whereas the scalar shadow pairing uses

    Tr(F^m) Tr(F^n).

For the tested pairs:

    (m,n)=(1,1): real 27, shadow 13
    (m,n)=(1,2): real 76, shadow 69
    (m,n)=(2,2): real 27, shadow -71
    (m,n)=(2,3): real 181, shadow 132

Likewise scalar trace slots do not compose as Frobenius graphs:

    t_1 t_1 = 1       while t_2 = -13
    t_1 t_2 = -13     while t_3 = -20
    t_2 t_2 = 169     while t_4 = 71
    t_2 t_3 = 260     while t_5 = 211.

The defect is structural, not numeric. Matrices A and B can have the same
trace, and C can have a fixed trace, while Tr(A C) != Tr(B C). Therefore
traces alone do not determine End product traces.

The same trace-augmented hyperbolic shadow is formable on arbitrary control
trace sequences. Consequently it constructs no actual square, integral
`rep_NS` with End component, two carrier-native degree maps, indecomposable
diagonal, Frobenius graph, proper correspondence category, fiber-product
composition, projection formula, canonical Rosati, positive primitive sign,
carrier boundary with control death, or DD.4 carrier-native weight>=1 datum.
```

Verdict label:

```text
N1B_TRACE_AUGMENTED_HYPERBOLIC__SCALAR_TRACE_NOT_END_GRAPH__NO_GO.
```

## 3. Proof

`prime_int_n1b_trace_augmented_hyperbolic_no_go` verifies seven gates.

TAH1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

TAH2 checks the positive fact: scalar trace augmentation of the hyperbolic
endpoint plane reproduces diagonal point-count shadows for n=1,2,3,4.

TAH3 checks the off-diagonal failure. The scalar trace pairing disagrees
with the real `rep_NS` graph pairing for `(1,1)`, `(1,2)`, `(2,2)`, and
`(2,3)`.

TAH4 checks the graph-composition failure. Scalar trace multiplication does
not produce the trace of the composed Frobenius graph.

TAH5 checks the structural reason: traces alone do not determine product
traces. There are matrices A,B,C with `Tr(A)=Tr(B)` and fixed `Tr(C)`, but
`Tr(A C) != Tr(B C)`.

TAH6 attaches arbitrary scalar traces to control labels. The same shadow is
available without Euler product, Satake data, End component, proper
correspondences, or control death.

TAH7 applies the SCC contract: diagonal counts are not enough. The package
does not construct `Qbar`, integral `rep_NS` with End component, graph
composition, Rosati, projection, or control death.

## 4. Impact on R1

```text
R1 after docs 138-281:
  NEWLY CLOSED THIS CYCLE:
    - repairing the hyperbolic endpoint plane by adding a scalar trace slot;
    - treating diagonal point-count recovery as the full End/Frobenius graph
      component;
    - replacing Tr(z w) by products of scalar traces.

  POSITIVE INFORMATION RETAINED:
    - scalar trace is the correct diagonal shadow of the End component;
    - a future carrier must include the hyperbolic endpoint plane plus an
      End/Frobenius component whose trace recovers explicit-formula counts;
    - the missing datum is the full product-sensitive End component, not the
      scalar trace functional alone.

  STILL ADMISSIBLE:
    - a compactified zeta square whose `rep_NS` includes a genuine End
      correspondence component with pairing Tr(z w);
    - a carrier-native graph law whose composition gives the trace
      Tr(F^(m+n)) because the graph itself composes, not because scalar trace
      labels are multiplied;
    - a proof that no such carrier can exist, with a named mechanism and
      witness.

  STILL OPEN:
    - construct the full integral `rep_NS` lattice over `Z`, not just its
      hyperbolic endpoint and scalar trace shadows.
```

## 5. Kill conditions

```text
KILL-TAH.1 scalar trace slot promoted to End component
  A proposal adds Tr(F^n) to endpoint labels and calls it rep_NS. Kill it
  unless it constructs product-sensitive End correspondences.

KILL-TAH.2 diagonal counts promoted to graph
  Matching Delta.Gamma_n is not constructing Gamma_n. Kill it unless
  off-diagonal pairings and graph composition are carrier-native.

KILL-TAH.3 trace products replacing End products
  Tr(z)Tr(w) is not Tr(z w). Kill it unless the actual End product is
  constructed.

KILL-TAH.4 control trace shadows ignored
  Arbitrary controls admit scalar trace shadows. Kill any proposal where
  controls survive until a later filter.

KILL-TAH.5 CFC bypassed
  Trace-augmented hyperbolic data not embedded in the carrier-first square
  contract is not End(S^2/Z).
```
