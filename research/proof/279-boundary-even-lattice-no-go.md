# 279 - Boundary even lattice is not the square carrier

Status: no-go + boundary-even-lattice deletion, 2026-06-21.
One-hundred-forty-second cycle of the doc-137 construction arc. Doc 278
showed that oriented boundary incidence selects the difference direction
`d1-d2`, but total plus difference decodes endpoints integrally only after a
same-parity theorem. This document tests the next repair:

```text
read the same-parity condition from a boundary intersection/even-lattice
condition.
```

Witness, lead-reran this cycle:
`prime_int_n1b_boundary_even_lattice_no_go` (BEL1-BEL8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_oriented_boundary_complex_no_go`,
`prime_int_n1b_endpoint_parity_saturation_no_go`,
`prime_int_n1b_endpoint_parity_tag_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 278 leaves a narrow constructive target. If the oriented boundary complex
gives

```text
a = d1 - d2,
```

then endpoint recovery also needs the total

```text
s = d1 + d2
```

and the parity theorem

```text
s = a mod 2.
```

The natural geometric repair is to say this parity is not a selector but an
evenness property of the boundary lattice. For example, the quadratic parity

```text
q(s,a) = s^2 - a^2
```

is even exactly when `s` and `a` have the same parity.

This document rejects only the shortcut:

```text
bare boundary evenness constructs the integral endpoint lattice.
```

It does not reject a future carrier where the integral cycle lattice of
`Qbar` proves the required parity theorem as part of `rep_NS`.

## 2. Lemma

```text
Lemma 279.1 (boundary evenness packages parity but does not construct it).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

In total/difference coordinates (s,a), the condition

    q(s,a)=s^2-a^2 is even

is equivalent to

    s=a mod 2.

On this same-parity lattice, the half-sum decoder

    (s,a) |-> ((s+a)/2, (s-a)/2)

is integral. The label (1,1) decodes to (1,0), and the oriented-difference
twist

    sigma((s,a),u)=((s,a), c^a phi(u))

splits c.

However, this boundary-even condition is exactly the index-two parity
selector from doc 274 in boundary-lattice language. The full
total/difference register still contains excluded labels such as

    (0,1), (11,8), (10,1),

which can run the same DD.4 split when a=1 but decode only half-integrally.
Saturating the full register sends them to half-integral endpoint degrees.

Modulo 2, the condition s=a is one of several index-two selectors:

    s=a,   s=0,   a=0.

Choosing the boundary quadratic parity without deriving it from the carrier
is still choosing a sublattice. The same boundary-even package is formable on
controls. Therefore it constructs no actual square, integral rep_NS, two
carrier-native degree maps, indecomposable diagonal, Frobenius graph, proper
correspondence category, fiber-product composition, projection formula,
canonical Rosati, positive primitive sign, carrier boundary with control
death, or DD.4 carrier-native weight>=1 datum.
```

Verdict label:

```text
N1B_BOUNDARY_EVEN_LATTICE__PARITY_SELECTOR_NOT_REP_NS__NO_GO.
```

## 3. Proof

`prime_int_n1b_boundary_even_lattice_no_go` verifies eight gates.

BEL1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

BEL2 checks that boundary-quadratic evenness is exactly same-parity
decoding on the tested window.

BEL3 checks the positive fact: the even label `(1,1)` decodes integrally to
`(1,0)` and splits `c`.

BEL4 records the excluded-label defect. Labels `(0,1)`, `(11,8)`, and
`(10,1)` are not boundary-even, but they still exist in the full register and
decode half-integrally.

BEL5 records that mod-2 evenness is a selector among index-two boundary
lattices, not a carrier theorem by itself.

BEL6 records the saturation defect: applying the half-sum decoder on the
full lattice makes excluded labels half-integral endpoints.

BEL7 attaches the same boundary-even package to controls in dimensions
2,4,8. No square data is consumed and controls do not die.

BEL8 applies the SCC/CFC contract: boundary evenness does not construct
`Qbar`, `p1`, `p2`, `rep_NS`, graph, composition, Rosati, projection, or
control death.

## 4. Impact on R1

```text
R1 after docs 138-279:
  NEWLY CLOSED THIS CYCLE:
    - promoting a boundary evenness/intersection-parity condition to the
      integral endpoint lattice or square carrier.

  POSITIVE INFORMATION RETAINED:
    - boundary evenness is exactly the parity condition needed for
      total/difference endpoint decoding;
    - the remaining carrier must prove this parity as a theorem of its
      integral cycle lattice, not declare it as an index-two sublattice.

  STILL ADMISSIBLE:
    - a compactified zeta square whose integral rep_NS lattice has image the
      same-parity total/difference lattice by construction;
    - a parity/2-divisibility theorem derived from proper correspondences,
      projection formula, and Rosati;
    - a proof that no such boundary-even square can exist, with a named
      mechanism and witness.

  STILL OPEN:
    - construct the integral cycle lattice of Qbar and prove the parity
      theorem carrier-natively.
```

## 5. Kill conditions

```text
KILL-BEL.1 boundary evenness promoted to rep_NS
  A proposal says q=s^2-a^2 is even, hence endpoints are integral. Kill it
  unless the even lattice is constructed as the carrier's integral rep_NS
  lattice.

KILL-BEL.2 same-parity selector renamed as geometry
  The condition s=a mod 2 is an index-two sublattice. Kill it unless the
  square carrier forces that sublattice.

KILL-BEL.3 half-sum saturation ignored
  The full total/difference lattice still has half-integral endpoint labels.
  Kill it unless the carrier excludes them.

KILL-BEL.4 mod-2 selector ambiguity ignored
  Boundary parity is one selector among several mod-2 index-two conditions.
  Kill it unless the specific selector is carrier-native.

KILL-BEL.5 control formability ignored
  Boundary-even lattices can be attached to controls. If controls survive
  until a later filter, carrier formation has failed.

KILL-BEL.6 CFC bypassed
  Boundary evenness not embedded in the carrier-first square contract is not
  End(S^2/Z).
```
