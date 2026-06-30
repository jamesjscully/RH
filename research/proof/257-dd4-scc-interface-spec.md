# 257 - DD.4/SCC interface: the carrier extension problem

Status: construction-spec interface anchor, 2026-06-20. One-hundred-twentieth
cycle of the doc-137 construction arc. This is not a no-go theorem, not an
RH proof, and not added to the no-go bank.

Doc 256 froze the square-carrier contract for `End(S^2/Z)`. This document
pins the interface between that contract and the R1 entry problem DD.4. The
point is not to add another candidate language. The point is to identify the
next carrier-native subobject that must be built before the square contract
can move.

Witness, lead-reran this cycle:
`prime_int_n1b_dd4_scc_interface` (DSI1-DSI6 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_pb_shear_h1_obstruction`, `dd4_weight1_datum`,
`prime_int_torsor_splitter_insertion_no_go`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The SCC contract has an explicit final slot:

```text
SCC.11  DD.4 weight>=1 data, including the Laurent boundary and torsor
        splitter demanded by the R1 entry problem.
```

That slot is not decorative. The square carrier needs a self-dual stage
before the positive Rosati layer can be constructed. Doc 138 computed the
weight>=1 obstruction:

```text
[(1+z)^-1] in H^1(<phi>; 1 + z F_2[[z]]) = Z/2,
```

detected by the torsor-invariant leading coefficient `res_1`.

Therefore the next constructive task is precise:

```text
Build a carrier-native extension in which this DD.4 class dies because of
an actual boundary/properness/self-duality map, while DH/Epstein/controls
die at carrier formation.
```

A free formal splitter is not enough. It makes the cocycle a coboundary by
definition, but supplies no actual square, no `rep_NS`, no degree maps, no
proper correspondence category, no control death, and no square pairing.

## 2. Interface

The DD.4/SCC bridge has three parts.

```text
DSI.A  The obstruction source:

       U_1 = 1 + z F_2[[z]],
       phi(z) = z/(1+z),
       c = (1+z)^-1,
       [c] != 0 in H^1(<phi>; U_1).

DSI.B  The admissible carrier extension:

       a carrier-native boundary/properness/self-duality map must induce an
       extension of the coefficient system in which the image of [c] is zero.
       This extension must be produced by the same object that supplies the
       square carrier, not by adjoining an external generator.

DSI.C  The SCC consequence:

       only after DSI.B is built can SCC.8 (canonical D^2=id Rosati
       duality), SCC.10 (control death), and SCC.11 (DD.4 weight>=1,
       Laurent boundary, torsor splitter) become live construction slots.
```

The interface is deliberately conditional. It does not say the carrier
exists. It says exactly what the carrier must do to pass the next gate.

## 3. Lemma

```text
Lemma 257.1 (DD.4/SCC interface).

In the tested truncations L=6,8,10,12 of U_1/(1+z^{L+1}), the DD.4 defect
c=(1+z)^-1 is a C_2 cocycle for the Artin-Schreier shear phi and represents
the unique nonzero class in

    H^1(<phi>; U_1) = Z/2.

The leading coefficient map

    res_1 : U_1 -> F_2

vanishes on every coboundary and satisfies res_1(c)=1. Hence the obstruction
is carrier-independent at the level of the current coefficient system.

Adjoining a free generator b with phi(b)=b*c^-1 makes b/phi(b)=c, so the
class dies in the formally split extension. But this operation adds an
external splitter and changes no SCC slot: it does not build the actual
square, carrier boundary, integral rep_NS, degree maps, Frobenius graph,
proper correspondence category, projection formula, positive Rosati, or
control death.

Consequently a valid End(S^2/Z) construction must kill [c] only through a
carrier-native extension tied to boundary/properness/self-duality, not by a
free torsor split.
```

## 4. Proof

`prime_int_n1b_dd4_scc_interface` verifies the six gates.

DSI1 checks the Lin boundary. At `z=0`, `c` restricts to `1`, so the
weight-0 Lin singleton remains intact; `res_1(c)=1` shows the weight>=1
obstruction is still present.

DSI2 recomputes the stable cohomology:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and verifies that `c` is nonzero in each quotient.

DSI3 verifies that `res_1` kills all coboundaries and detects `c`.

DSI4 constructs the formal split extension with an adjoined generator `b`
and checks `b/phi(b)=c`. This demonstrates exactly why the formal torsor
splitter is mathematically able to kill the class, and exactly why it is
not sufficient as a carrier construction.

DSI5 evaluates the current SCC dependency state. With only the Lin
boundary, finite-field anchor, and SCC contract in hand, `SCC.11 DD.4`,
`SCC.8 Rosati duality`, `SCC.2 integral rep_NS`, and the other square slots
remain unresolved.

DSI6 compares the free split with the admissible interface. Adding only a
splitter changes no SCC slot. The admissible extension must also supply an
actual square boundary/properness/self-duality map and kill controls at
carrier formation.

## 5. Impact on R1

```text
R1 after docs 138-257:
  NEWLY FIXED THIS CYCLE:
    - the exact DD.4-to-SCC interface. The next construction cannot merely
      name a square carrier or add a torsor splitter. It must provide a
      carrier-native extension killing [c] through boundary/properness/
      self-duality while also supplying control death.

  STILL ADMISSIBLE:
    - a different carrier in which the DD.4 class maps to zero because the
      carrier has an actual boundary/properness/self-duality mechanism;
    - a zeta-native square whose DD.4 extension is part of the same object
      that later supplies integral rep_NS, degree maps, graph, projection
      formula, and Rosati;
    - a proof that such a carrier extension cannot exist, with a named
      mechanism and witness.

  STILL OPEN:
    - construct the carrier-native DD.4 extension;
    - then construct the actual square carrier over Z.
```

## 6. Acceptance and kill conditions

```text
ACCEPT-DSI.1  Exhibit the carrier-native coefficient extension receiving
              U_1 and killing [c].
ACCEPT-DSI.2  Prove the killing map comes from boundary/properness/
              self-duality of the same carrier, not from a free generator.
ACCEPT-DSI.3  Prove DH/Epstein/controls cannot form the same extension.
ACCEPT-DSI.4  Connect the extension to SCC.11 and the later D^2=id Rosati
              pairing, without promoting stage data to RH.

KILL-DSI.1    Reject a bare torsor splitter b with phi(b)=b*c^-1.
KILL-DSI.2    Reject a coefficient extension that is formable on controls.
KILL-DSI.3    Reject a square-carrier claim that does not resolve [c].
KILL-DSI.4    Reject any use of this interface as a completed End(S^2/Z)
              construction. It is the next carrier subproblem, not the
              solution.
```
