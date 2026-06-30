# 340 - Qbar_BECD strict-square product multiplier control-death naturality contract

Status: construction-spec refinement anchor, 2026-06-23.
Two-hundred-third cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 339 left the strict-square branch live only through:

```text
a carrier-native multiplier-action pushforward square that generates proper
graph composition, positive Rosati, and count/degree data in one layer,
naturally under C3, C9, F22, and C3F22.
```

This document fixes the formation-death edge. Control death cannot be a
late rejection imposed after a graph/count/Rosati shadow has already formed.
It must be generated at the graph-formation gate itself, and that same gate
must make controls, DH, and Epstein undefined before any post-hoc filter
exists.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_control_death_naturality_contract`
(GFD1-GFD10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_graph_rosati_count_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_pushforward_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_endpoint_degree_naturality_contract`,
`prime_int_n1b_qbar_becd_strict_square_product_multiplier_dd4_naturality_contract`,
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`,
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`, and
`prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

After doc 339, the cheap repair is:

```text
allow controls/DH/Epstein to instantiate formal graph, q-similarity,
Rosati, count, or projection data, then reject them by a later sign,
projection, DD.4, finite-sample, or semantic filter.
```

That is still not the square. If a control can instantiate the graph layer,
the construction has already failed the carrier gate. Formation death must be
upstream of graph shadows:

```text
internal effectivity domain
  -> multiplier action
  -> DD.4 boundary
  -> endpoint degree
  -> p1_*,p2_* pushforward square
  -> graph/Rosati/count layer
  -> graph-formation gate
  -> controls, DH, Epstein undefined.
```

The live branch therefore narrows from "generated graph/Rosati/count
naturality" to:

```text
construct a carrier-native graph-formation gate, natural for multiplier
transport, whose own formation rule kills controls, DH, and Epstein before
they can form graph/Rosati/count shadows.
```

## 2. Lemma

```text
Lemma 340.1 (control death must occur at graph formation).

The control matrix still has formal graph/Rosati shadows before any filter:

    graph-law defect              0,
    q-similarity defect           0,
    Rosati anti-involution defect 0,
    primitive Hodge sign          +12,
    projection defect             24,
    retuned first degree          27.

Thus a late Rosati-sign, projection-defect, DD.4, finite-sample, semantic,
or declared-death filter is too late: it lets the control enter the graph
formation layer first.

The strict-square rows share one graph-formation death gate:

    domain       D_Qbar_BECD_eff,
    boundary     B_Qbar_BECD_DD4,
    pushforward  PF_Qbar_BECD_p1p2,
    graph        G_Qbar_BECD_prop,
    Rosati       R_Qbar_BECD_pos,
    count/degree CD_Qbar_BECD,
    death gate   K_Qbar_BECD_graph_formation_death.

The visible transport diagnostics are:

    z                    -> graph 2,  count 4,
    T_C3(z)              -> graph 6,  count 36,
    T_C9(z)              -> graph 18, count 324,
    z*F22                -> graph 8,  count 64,
    T_C3(z*F22)          -> graph 24, count 576,
    T_C3(z)*F22          -> graph 24, count 576,
    z*(C3*F22)           -> graph 24, count 576.

Graph degree scales linearly, count-degree scales quadratically, endpoint
defect remains zero, and the same death gate transports through the rows.

The accepted datum is exactly:

    carrier-native,
    actual internal effectivity domain,
    actual multiplier action,
    actual DD.4 boundary,
    actual endpoint degree maps,
    actual pushforward square,
    generated graph/Rosati/count layer,
    actual graph-formation gate,
    control death generated at graph formation,
    control death natural for multiplier transport,
    controls undefined at graph formation,
    DH undefined at graph formation,
    Epstein undefined at graph formation,
    finite-field anchor generated,
    graph-degree anchor generated,
    count-degree anchor generated,
    coefficients retained,
    signed support retained,
    same gate transports all rows,
    required formation-death edges present,
    no post-hoc control filter,
    no graph/count filter,
    no Rosati-sign filter,
    no projection-defect filter or retuning,
    no DD.4 afterthought filter,
    no finite-sample filter,
    no semantic zeta/Euler/Satake label,
    no declared control death,
    no control/DH/Epstein shadow,
    no local control stack,
    no finite control table,
    no external multiplier degree,
    controls, DH, and Epstein not formable.
```

Verdict label:

```text
N1B_QBAR_BECD_STRICT_SQUARE_PRODUCT_MULTIPLIER_CONTROL_DEATH_NATURALITY__DEATH_AT_GRAPH_FORMATION__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_strict_square_product_multiplier_control_death_naturality_contract`
verifies ten gates.

GFD1 records why late filters are too late: controls can instantiate formal
graph, q-similarity, Rosati anti-involution, and projection-retunable data.

GFD2 records the strict-square graph-formation death rows and their
multiplier naturality.

GFD3 rejects Rosati-sign, projection-defect, and DD.4 after-filters.

GFD4 rejects finite graph/count/control tables and finite samples.

GFD5 rejects semantic zeta/Euler/Satake labels and declared deaths.

GFD6 rejects control, DH, and Epstein graph shadows.

GFD7 rejects local control stacks, finite control tables, and external
multiplier degrees.

GFD8 proves that every upstream layer is part of the same formation
obstruction.

GFD9 rejects static death flags without formation edges.

GFD10 records the live predicate. Only carrier-native graph-formation
control death passes.

## 4. Impact on R1

```text
R1 after docs 138-340:
  NEWLY FIXED THIS CYCLE:
    - control death must be generated at the graph-formation gate produced
      by the carrier-native strict-square multiplier layer. A late filter
      after graph/Rosati/count shadows form does not count.

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
    - construct the graph-formation death gate natural for multiplier
      transport;
    - prove controls, DH, and Epstein are undefined at graph formation.

  DISCIPLINE:
    - control/Rosati/projection/DD.4 after-filters, finite samples, semantic
      labels, declared deaths, local control stacks, finite tables, external
      multiplier degrees, and control/DH/Epstein graph shadows are diagnostics
      only.

  STILL OPEN:
    - construct the carrier-native graph-formation death gate, or kill the
      strict-square branch with a named obstruction at this exact interface.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-GFD.1  Exhibit the graph-formation gate generated by the same
              carrier-native graph/Rosati/count layer.
ACCEPT-GFD.2  Prove the gate is natural for C3, C9, F22, and C3F22.
ACCEPT-GFD.3  Prove controls are undefined before graph/Rosati/count shadows
              form.
ACCEPT-GFD.4  Prove DH is undefined before graph/Rosati/count shadows form.
ACCEPT-GFD.5  Prove Epstein is undefined before graph/Rosati/count shadows
              form.
ACCEPT-GFD.6  Preserve the finite-field count, graph-degree, and count-degree
              anchors as generated consequences.
ACCEPT-GFD.7  Retain coefficients and signed support in one internal domain.
ACCEPT-GFD.8  Keep all formation-death edges in the same strict square.

KILL-GFD.1    Reject post-hoc control filters.
KILL-GFD.2    Reject graph/count filters.
KILL-GFD.3    Reject Rosati-sign filters.
KILL-GFD.4    Reject projection-defect filters and retunings.
KILL-GFD.5    Reject DD.4 afterthought filters.
KILL-GFD.6    Reject finite samples and finite control tables.
KILL-GFD.7    Reject semantic zeta/Euler/Satake labels.
KILL-GFD.8    Reject declared control death.
KILL-GFD.9    Reject local control stacks and external multiplier degrees.
KILL-GFD.10   Reject control/DH/Epstein graph shadows.
```
