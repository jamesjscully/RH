# 277 - Cartier boundary normal line is not the square carrier

Status: no-go + Cartier-boundary-normal deletion, 2026-06-21.
One-hundred-fortieth cycle of the doc-137 construction arc. Doc 276 fixed
the carrier-first categorical contract. This document attacks the first
actual construction subproblem under that contract:

```text
make the DD.4 Hilbert-90 uniformizer a normal coordinate of an honest
Cartier boundary divisor.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cartier_boundary_normal_no_go` (CBN1-CBN7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_laurent_field_hilbert90_no_go`,
`prime_int_n1b_valuation_degree_character_no_go`,
`prime_int_n1b_endpoint_parity_tag_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 267 showed that the full Laurent field kills the DD.4 class by using an
odd valuation/uniformizer axis. That was too formal: the valuation was
imported, not produced by the square.

Doc 276 now tells us what the first serious construction attempt should be:
make the uniformizer carrier-native by making it the normal coordinate of a
Cartier boundary divisor in the compactified square.

This is genuinely stronger than bare Laurent Hilbert 90. A Cartier boundary
normal line is exactly the kind of geometric object that can turn a
uniformizer into boundary data. The no-go is narrower:

```text
Cartier normal data alone is not the square carrier.
```

It can kill DD.4, but unless the same object also constructs `Qbar`, `p1`,
`p2`, integral `rep_NS`, Frobenius/Hecke graph, proper correspondence
composition, Rosati, and control death, it remains a boundary valuation
package.

## 2. Lemma

```text
Lemma 277.1 (Cartier normal line supplies the valuation, not the square).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

Now model a Cartier boundary normal coordinate t by the normal-line action

    sigma(t) = t * c.

Then sigma^2(t)=t, and the normal-coordinate element sigma(t) has boundary

    sigma(t) / sigma^2(t) = c.

Thus an honest boundary normal line has exactly the right DD.4 splitting
shape. This is positive construction information.

However, one normal valuation is rank one. Any promoted additive degree
character chi(d1,d2)=a d1+b d2 has a nonzero endpoint kernel direction
(b,-a), preserving chi while changing endpoint probes. Therefore a single
Cartier normal line cannot be the two SCC degree maps.

A normal-crossing pair of boundary components gives two integer valuations,
but still does not choose the DD.4 boundary direction. In the tested window,
sixteen primitive linear functionals ell on Z^2 split c once used in

    sigma(v,u) = (v, c^ell(v) phi(u)).

Normal-crossing data by itself does not select ell=d1, ell=d2, ell=d1+d2,
ell=d1-d2, or any other primitive direction.

The finite-field SCC anchor confirms that scalar boundary totals do not
recover endpoints: (10,F,1) and (7,F,4) have the same total degree 11 and
the same diagonal intersection 10, but left and right endpoint probes differ.

The same formal Cartier-boundary-normal package is formable on controls.
Consequently Cartier normal data by itself constructs no actual square,
integral rep_NS, two carrier-native degree maps, indecomposable diagonal,
Frobenius graph, proper correspondence category, fiber-product composition,
projection formula, canonical Rosati, positive primitive sign, or control
death.
```

Verdict label:

```text
N1B_CARTIER_BOUNDARY_NORMAL__NORMAL_VALUATION_NOT_SQUARE_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_cartier_boundary_normal_no_go` verifies seven gates.

CBN1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

CBN2 checks the positive Cartier-normal fact. With a normal coordinate `t`
and `sigma(t)=t*c`, one has `sigma^2(t)=t` and
`sigma(t)/sigma^2(t)=c`.

CBN3 records the rank-one defect. For the tested characters

```text
(1,0), (0,1), (1,1), (1,-1), (2,3), (-2,5),
```

the kernel direction preserves the character while changing the endpoint
pair.

CBN4 tests a normal-crossing pair. Two normal valuations restore rank, but
the DD.4 boundary direction is not forced: sixteen primitive linear
functionals in the small window split c once chosen.

CBN5 anchors the endpoint loss in the finite-field square model. The two
classes `(10,F,1)` and `(7,F,4)` have the same total degree and same
diagonal intersection, but different endpoint probes.

CBN6 repeats the formal Cartier-boundary package on controls in dimensions
2,4,8. No square data is consumed and controls do not die.

CBN7 applies the SCC/CFC contract: DD.4 splitting by normal valuation does
not construct `Qbar`, `p1`, `p2`, `rep_NS`, graph, Rosati, or control death.

## 4. Impact on R1

```text
R1 after docs 138-277:
  NEWLY CLOSED THIS CYCLE:
    - promoting a Cartier boundary normal coordinate, or a bare
      normal-crossing valuation pair, to the full square carrier.

  POSITIVE INFORMATION RETAINED:
    - the boundary normal line is the right local shape for the DD.4
      splitter: sigma(t)=t*c gives boundary c;
    - any surviving carrier should contain this normal-line mechanism, but
      only as part of Qbar with p1,p2, rep_NS, graph, Rosati, and control
      death.

  STILL ADMISSIBLE:
    - a compactified zeta square whose Cartier or normal-crossing boundary
      supplies the normal line and simultaneously ties its components to the
      two endpoint maps p1,p2;
    - a theorem that the carrier boundary selects the DD.4 direction ell and
      excludes the other primitive normal-crossing directions;
    - a construction in which the same boundary localization also yields
      proper correspondence composition, projection formula, Rosati, and
      control death.

  STILL OPEN:
    - construct Qbar and prove the boundary normal line is coupled to the
      endpoint maps and correspondence category.
```

## 5. Kill conditions

```text
KILL-CBN.1 normal coordinate promoted to carrier
  A proposal says a Cartier normal uniformizer kills DD.4, hence the carrier
  is built. Kill it unless Qbar, p1,p2, rep_NS, graph, Rosati, and control
  death are built at the same step.

KILL-CBN.2 one normal valuation as two degree maps
  A single Cartier valuation is rank one. Kill it unless the construction
  supplies two independent endpoint degree maps.

KILL-CBN.3 normal crossings without boundary-direction theorem
  Two boundary components provide two valuations, but not a canonical DD.4
  primitive direction. Kill it unless the carrier selects ell.

KILL-CBN.4 boundary total confused with endpoint data
  Total valuation or diagonal intersection does not recover left/right
  endpoint probes.

KILL-CBN.5 control formability ignored
  Formal boundary divisors and normal lines can be attached to controls. If
  controls survive until a later filter, carrier formation has failed.

KILL-CBN.6 CFC bypassed
  A boundary normal line not embedded in the carrier-first square contract is
  not End(S^2/Z).
```
