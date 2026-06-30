# 345 - Qbar_BECD strict-square product multiplier monoidwide square-layer coherence contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-eighth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 344 left the strict-square branch live only through represented
square-layer coherence on the visible `C3/C9/F22` patch:

```text
    SLC_Qbar_BECD_boundary_pushforward_graph

commuting with DD.4 boundary, endpoint degree, p1/p2 pushforward, graph,
Rosati, count/degree, and coherent control death.
```

This document fixes the next edge. A local `C3`-adic coherence table is still
too small. The same square-layer coherence must be monoidwide for the
carrier-native multiplier-action functor. In particular, it must survive an
independent multiplier direction:

```text
    C3*C5 = C5*C3 = C15,
    C3*C3*C5 = C45,

and product naturality with F22.
```

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_monoidwide_square_layer_coherence_contract`
(MWC1-MWC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_square_layer_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_cartesian_coherence_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_transport_composition_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_represented_source_fiber_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_source_typed_formation_gate_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_control_death_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_graph_rosati_count_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_pushforward_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_endpoint_degree_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_dd4_naturality_contract`,
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 344, the cheap repair is:

```text
build a coherent C3/C9/F22 square-layer patch and call it the multiplier
action.
```

That still does not construct the carrier multiplier action. It can pass the
visible `T_C3(T_C3(z))=T_C9(z)` and `F22` tests while leaving another prime
direction, such as `C5`, supplied by a separate finite table or external
prime-factor label. The square itself must construct the monoid action, so
independent multiplier paths must use the same coherence id and the same
square-layer chain.

The live branch therefore narrows from "square-layer coherent on the visible
patch" to:

```text
construct represented universal-arrow coherence cells that are monoidwide
for the carrier-native multiplier-action functor and commute with every
square layer.
```

## 2. Lemma

```text
Lemma 345.1 (square-layer coherence must be monoidwide).

The represented monoidwide rows carry:

    MWC_Qbar_BECD_multiplier_monoid_square_layers,

over the same square-layer chain:

    B_Qbar_BECD_DD4,
    ED_Qbar_BECD_endpoint_degree,
    PF_Qbar_BECD_p1p2,
    G_Qbar_BECD_prop,
    R_Qbar_BECD_pos,
    CD_Qbar_BECD,
    CTRL_Qbar_BECD_coherent_death.

The new independent multiplier checks are:

    T_C3(T_C5(z))              = T_C5(T_C3(z))
                                = T_C15(z)            = {15:2, 30:-1},
    T_C3(T_C3(T_C5(z)))        = T_C9(T_C5(z))
                                = T_C45(z)            = {45:2, 90:-1},
    T_C15(z*F22)               = T_C3(T_C5(z))*F22
                                = z*(C15*F22)        = {30:4, 60:-2},
    T_C45(z*F22)               = T_C3(T_C3(T_C5(z)))*F22
                                = z*(C45*F22)        = {90:4, 180:-2}.

All endpoint, boundary, and p1/p2 pushforward defects remain zero. The finite
count and Rosati diagnostics remain anchored:

    count defect 0,
    Rosati anti-involution defect 0.

The control warning remains:

    carrier q=7 graph signature = control q=3 graph signature,
    carrier primitive sign -13.5,
    control primitive sign +12,
    control projection defect 24,
    retuned first degree 27.

Thus local `C3` patches, finite generator tables, external prime-axis labels,
declared monoid actions, formal pentagon/hexagon diagrams, late boundary/
pushforward/graph filters, degree/count/support equality, weighted-zero
tests, local layer tables, external 2-cells, retuned multiplier coherences,
and control/DH/Epstein monoid-coherent shadows do not construct this layer.

The accepted datum is exactly:

    carrier-native,
    represented source fiber,
    actual universal arrow,
    actual multiplier-action functor,
    actual identity transport,
    actual composition law,
    actual cartesian coherence,
    actual square-layer coherence,
    actual monoidwide coherence,
    coherence generated by the universal arrow,
    actual C3*C3=C9,
    actual C3*C5=C15,
    actual C5*C3=C15,
    actual C3*C3*C5=C45,
    actual F22 product naturality,
    actual DD.4 boundary,
    actual endpoint degree maps,
    actual p1 and p2 pushforward squares,
    actual graph composition,
    actual Rosati,
    actual count/degree,
    actual control death,
    square layers commute monoidwide,
    the same coherence id is carried by all multiplier paths,
    coefficient and signed-support preservation,
    finite anchors generated,
    controls, DH, and Epstein not point-formable,
    required monoidwide square-layer edges present,
    no local C3 patch,
    no single-prime-axis patch,
    no finite generator table,
    no external prime factorization,
    no prime-axis tags,
    no declared monoid action,
    no formal pentagon or hexagon,
    no degree/count/support/weighted-zero-only argument,
    no late boundary/pushforward/graph filters,
    no local layer table,
    no external choice of 2-cells,
    no retuned multiplier coherence,
    no graph-object coherence.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_MONOIDWIDE_SQUARE_LAYER_COHERENCE__C3_C5_C15_C45__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_monoidwide_square_layer_coherence_contract`
verifies ten gates.

MWC1 records one monoidwide square-layer coherence id across `C3`, `C5`,
`C15`, `C45`, and `F22`.

MWC2 records again that graph identities do not supply monoidwide coherence.

MWC3 rejects a local `C3/C9` square-layer patch.

MWC4 rejects prime-axis labels and factorization tables as external data.

MWC5 rejects declared monoid actions and formal coherence diagrams as labels.

MWC6 proves the independent multiplier paths and `F22` naturality are
mandatory.

MWC7 rejects boundary, pushforward, and graph filters after monoid action.

MWC8 rejects numeric equalities and local layer tables as diagnostics.

MWC9 rejects control, DH, and Epstein monoid-coherent shadows.

MWC10 records the live predicate. Only carrier-native monoidwide square-layer
coherence passes.

## 4. Impact on R1

```text
R1 after docs 138-345:
  NEWLY FIXED THIS CYCLE:
    - square-layer coherence must be monoidwide for the multiplier-action
      functor. A coherent C3/C9/F22 patch is not enough; the same represented
      coherence must pass through independent C5 and mixed C15/C45 paths.

  CURRENT LIVE TARGET ON THE STRICT-SQUARE BRANCH:
    - construct the represented strict-square signed-character algebra;
    - construct the cancellation module generated by z=2[1]-[2];
    - construct the represented boundary-convolution module functor;
    - construct the represented boundary-stratum product;
    - construct the product-to-internal-effectivity image map to the single
      internal Qbar_BECD effectivity domain;
    - construct the carrier-native multiplier-action functor on that domain;
    - construct the natural DD.4 boundary localization for that functor;
    - construct generated endpoint degree maps compatible with that boundary;
    - construct generated p1_* and p2_* pushforward squares;
    - construct generated graph composition, Rosati, and count/degree data
      natural for multiplier transport;
    - construct the represented source fiber and universal arrow;
    - construct represented coherence cells for the cartesian multiplier
      lifts;
    - construct square-layer coherence for those cells across DD.4 boundary,
      endpoint degree, p1/p2 pushforward, graph, Rosati, count, and control
      death;
    - prove that square-layer coherence is monoidwide for independent
      multiplier directions, including C3*C5=C5*C3=C15 and C3*C3*C5=C45;
    - prove coherent control death excludes controls, DH, and Epstein.

  DISCIPLINE:
    - local C3 patches, finite generator tables, prime-axis labels, declared
      monoid actions, formal coherence diagrams, late filters, and numeric
      equalities do not count.

  STILL OPEN:
    - construct the carrier-native monoidwide square-layer-coherent
      universal-arrow coherence cells, or kill the strict-square branch with a
      named obstruction at this multiplier-monoid interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-MWC.1  Exhibit monoidwide square-layer coherence generated by
              eta_Qbar_BECD_source.
ACCEPT-MWC.2  Prove the carrier-native multiplier-action functor has identity
              and composition.
ACCEPT-MWC.3  Prove C3*C3=C9, C3*C5=C5*C3=C15, and C3*C3*C5=C45.
ACCEPT-MWC.4  Prove F22 product naturality for the mixed multiplier paths.
ACCEPT-MWC.5  Prove DD.4 boundary, endpoint degree, p1/p2 pushforward, graph,
              Rosati, count/degree, and control death commute monoidwide.
ACCEPT-MWC.6  Prove one coherence id is carried by all multiplier paths.
ACCEPT-MWC.7  Prove controls, DH, and Epstein are not monoid-coherent points.

KILL-MWC.1    Reject local C3 patches.
KILL-MWC.2    Reject single-prime-axis patches.
KILL-MWC.3    Reject finite generator tables.
KILL-MWC.4    Reject external prime factorizations and prime-axis tags.
KILL-MWC.5    Reject declared monoid actions.
KILL-MWC.6    Reject formal pentagon/hexagon diagrams.
KILL-MWC.7    Reject degree/count/support/weighted-zero-only arguments.
KILL-MWC.8    Reject late boundary/pushforward/graph filters.
KILL-MWC.9    Reject external choices or retuned multiplier coherences.
KILL-MWC.10   Reject control/DH/Epstein monoid-shadow point-formability.
```
