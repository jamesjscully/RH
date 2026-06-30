# 283 - Positive Rosati End envelope is not the square carrier

Status: no-go + positive-Rosati-End-envelope deletion, 2026-06-21.
One-hundred-forty-sixth cycle of the doc-137 construction arc. Doc 282
killed the formal `U+End` envelope because it can wrap off-circle data and
controls. This document tests the stronger repair:

```text
keep U+End, require a chosen polarization, exact q-similitude, formal
dagger, and the primitive Hodge/Rosati sign.
```

Witness, lead-reran this cycle:
`prime_int_n1b_positive_rosati_end_envelope_no_go` (PRE1-PRE7 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_end_augmented_hyperbolic_no_go`,
`prime_int_n1b_formal_adjoint_projection_no_go`,
`prime_int_n1b_integral_qsim_graph_no_go`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 282 leaves one obvious formal strengthening. Add the matrix positivity
that doc 282 did not require:

```text
F^T E F = q E,
F^dag = q F^-1,
primitive Hodge/Rosati sign negative.
```

This blocks the off-circle example used in doc 282. The question is whether
the resulting positive `U+End` package is now the carrier.

It is not. Positivity as a matrix condition is a necessary finite-field
shadow, but it still does not construct the compactified square, proper
correspondence composition, projection formula, carrier boundary, or control
death.

## 2. Lemma

```text
Lemma 283.1 (positive matrix Rosati is not carrier Rosati).

Let U_1=1+z F_2[[z]], phi(z)=z/(1+z), and c=(1+z)^-1. In U_1, for
truncations L=6,8,10,12:

    H^1(<phi>; U_1) = Z/2,
    [c] != 0,
    res_1(c)=1.

For the q=7, Tr(F)=1 finite-field anchor, the formal positive `U+End`
package has:

    Delta.Gamma_1 = 7,
    Gamma_1.Gamma_2 = 76,
    Gamma_1 o Gamma_2 = Gamma_3,
    F^T E F = q E,
    Gamma_F^dag = (1, q F^-1, q),
    primitive Hodge/Rosati sign < 0.

Requiring the primitive sign rejects the standard off-circle q-similitude
used in earlier no-go cycles: it has exact q-similitude but positive
primitive Hodge sign.

However, the formal positive package still does not supply the projection
formula for proper correspondences. With the pasted pairing and componentwise
composition, the sampled defects in

    <A o B, C> = <B, A^dag o C>

are all 27 on the genuine finite-field block. This is the same distinction
as before: symbolic matrix multiplication is not fiber-product
correspondence composition.

The DD.4 split also remains independent of the positive End/Rosati slot: the
same endpoint-difference split works with End labels `positive_F`,
`positive_control`, and `Id`. Thus positivity has not coupled DD.4 boundary
killing to the graph and Rosati data.

Finally, positive `U+End` data is formable on controls. The control matrix

    [[0,-3],[1,0]]

has exact q-similitude for q=3, negative primitive Hodge sign, graph law,
and a formal diagonal pairing, but no Euler product, Satake data, proper
correspondences, carrier boundary, or control death.

Consequently the positive-Rosati End envelope constructs no actual `Qbar`,
no carrier-produced integral `rep_NS`, no proper correspondence category, no
fiber-product composition, no projection formula, no carrier boundary with
control death, and no DD.4 carrier-native weight>=1 datum.
```

Verdict label:

```text
N1B_POSITIVE_ROSATI_END_ENVELOPE__MATRIX_POSITIVITY_NOT_CARRIER__NO_GO.
```

## 3. Proof

`prime_int_n1b_positive_rosati_end_envelope_no_go` verifies seven gates.

PRE1 recomputes the base DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

PRE2 checks the positive finite-field package: diagonal count, off-diagonal
pairing, graph law, q-similitude, dagger relation, and negative primitive
sign all hold.

PRE3 checks that the added primitive sign rejects the off-circle
determinant-q graph. This is the real strengthening over doc 282.

PRE4 checks that the positive formal package still lacks the projection
formula: the sampled defects are `[27, 27, 27]`.

PRE5 checks that DD.4 splitting is independent of the positive End/Rosati
slot. The same split works with positive and nonpositive labels.

PRE6 checks control formability. A positive q-similitude control matrix
forms the same matrix package without Euler product, Satake data, proper
correspondences, carrier boundary, or control death.

PRE7 applies the carrier-first contract: positive `U+End` matrix data is not
`Qbar`, `Corr^prop`, fiber-product composition, projection formula, carrier
boundary, or control death.

## 4. Impact on R1

```text
R1 after docs 138-283:
  NEWLY CLOSED THIS CYCLE:
    - adding q-similitude and primitive Rosati sign to the formal U+End
      envelope as a substitute for the carrier;
    - treating positive matrix data as carrier Rosati;
    - treating DD.4 endpoint splitting plus positive End data as carrier
      boundary.

  POSITIVE INFORMATION RETAINED:
    - the primitive Rosati sign is a necessary filter and really rejects the
      off-circle wrapper;
    - any surviving carrier must include endpoint hyperbolic data, End graph
      data, graph composition, Rosati positivity, and DD.4 boundary together;
    - matrix positivity alone is not enough unless it is produced by the
      compactified square and its proper correspondence calculus.

  STILL ADMISSIBLE:
    - a compactified zeta square whose Rosati pairing and positivity theorem
      are carrier-native;
    - a proof that the projection formula comes from proper correspondence
      composition rather than componentwise matrix multiplication;
    - a carrier-native coupling of DD.4 boundary to the positive graph/Rosati
      package;
    - a proof that no such carrier can exist, with a named mechanism and
      witness.

  STILL OPEN:
    - construct Qbar and prove that positive Rosati, graph composition,
      endpoint integrality, DD.4 boundary killing, and control death are one
      carrier theorem.
```

## 5. Kill conditions

```text
KILL-PRE.1 positive matrix package promoted to carrier
  A proposal adds q-similitude and negative primitive sign to formal U+End.
  Kill it unless Qbar produces the lattice, pairing, and graph.

KILL-PRE.2 projection formula omitted
  Positive Rosati does not replace the projection formula. Kill it unless
  the formula is proved from proper correspondence composition.

KILL-PRE.3 DD.4 split independent of End/Rosati
  If DD.4 splitting works without using graph/Rosati data, it is still an
  attached endpoint split. Kill it unless the carrier couples them.

KILL-PRE.4 positive controls ignored
  Controls can carry positive q-similitude matrix data. Kill any proposal
  where controls survive until a later filter.

KILL-PRE.5 CFC bypassed
  Positive U+End data not embedded in the carrier-first square contract is
  not End(S^2/Z).
```
