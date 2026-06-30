# 288 - Represented carrier candidate matrix no-go

Status: no-go + represented-carrier-candidate-matrix deletion, 2026-06-21.
One-hundred-fifty-first cycle of the doc-137 construction arc. Doc 287
upgraded the acceptance rule: carrier slots count only with represented
object/map/cycle/pullback/boundary evidence. This document applies that gate
to the three standing doc-137 candidate routes:

```text
ROUTE 1: PFD/Xbar spectral line.
ROUTE 2: Connes-Consani scaling-site / C x C.
ROUTE 3: condensed/liquid metric enrichment.
```

Witness, lead-reran this cycle:
`prime_int_n1b_represented_carrier_candidate_matrix_no_go` (RCM1-RCM8 ALL
PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_qbar_shell_positive_envelope_no_go`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The four operations requested after doc 287 are:

```text
1. create a represented carrier candidate matrix;
2. run each standing route against RCG;
3. pick the smallest missing represented token/bundle;
4. attempt construction or bank the no-go.
```

This document does all four for the current evidence. It is not a theorem
that the three routes can never be strengthened. It is a no-go for the
represented evidence currently in the record.

## 2. Candidate Matrix

The represented-carrier gate is intentionally strict. A route gets a slot
only when the current record supplies the corresponding represented evidence.

```text
Route 1: PFD/Xbar spectral line
  Current evidence:
    - Xbar spectrum exists locally/stage-side;
    - Lin/self-duality clause exists.

  RCG result:
    represented slots = none.

  Reason:
    object_actual alone is not Qbar+Q+dQ, and Lin self-duality is not full
    carrier Rosati. The route still lacks actual p1,p2, boundary map,
    rep_NS, proper pullbacks, projection formula, DD.4 boundary killing, and
    control death.

Route 2: Connes-Consani scaling-site / C x C
  Current evidence:
    - curve-level compactified/scaling-site object;
    - open/boundary shape at curve level;
    - curve-level duality evidence.

  RCG result, granting the curve-level carrier-object token:
    represented slots = carrier_object.

  Reason:
    the self-product correspondence carrier is still absent. The route lacks
    actual square p1,p2 pushforwards, integral square rep_NS, diagonal and
    graph cycles in the square carrier, proper pullbacks, projection formula,
    DD.4 boundary killing, carrier Rosati, primitive sign, and formation
    control death.

Route 3: condensed/liquid metric enrichment
  Current evidence:
    - analytic/condensed/liquid site language;
    - metric enrichment and positivity vocabulary.

  RCG result:
    represented slots = none.

  Reason:
    analytic site and metric data are not Qbar, p1,p2, dQ, rep_NS,
    Corr^prop(Qbar), boundary localization, or control death.
```

## 3. Lemma

```text
Lemma 288.1 (current standing routes fail represented carrier evidence).

For the three standing doc-137 routes, the current represented slots are:

    PFD/Xbar                         none
    Connes-Consani scaling-site/CxC  carrier_object
    condensed/liquid metric          none

Thus no route passes the represented-carrier gate.

The shared smallest missing represented bundle is:

    actual boundary map,
    exact localization,
    DD.4 class mapped to zero,
    self-dual boundary/properness data,
    actual p1,p2 maps,
    proper pushforward,
    control-instantiation impossibility,
    control death at formation.

The DD.4 obstruction is still present in the base coefficient system:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1

in truncations L=6,8,10,12.

Positive projection/Rosati shadows do not replace this bundle. In the q=7,
Tr(F)=1 finite-field anchor, the primitive sign is negative, but the formal
semantic projection defect remains 27.

Endpoint labels and total-degree decoders do not construct p1,p2:
`(10,F,1)` and `(7,F,4)` have the same total degree and the same diagonal
pairing, but different endpoint probes.

Current candidate evidence remains formable on positive controls; a q=3
positive control has semantic projection defect 11 and no formation-level
control death.

Attempting to add the shared blocker bundle is necessary but not sufficient.
Even after adjoining that bundle synthetically, PFD/Xbar still lacks
integral rep_NS and square correspondence data, Connes-Consani/CxC still
lacks proper square composition/projection/Rosati/graph data, and condensed
metric enrichment still lacks the carrier object and square data.

Therefore the current standing routes bank a represented-evidence no-go.
The next constructive target is the shared boundary+endpoint+control-death
bundle, but it must be constructed as represented evidence and then extended
to rep_NS, proper pullbacks, projection, Rosati, and graph data.
```

Verdict label:

```text
N1B_REPRESENTED_CARRIER_CANDIDATE_MATRIX__CURRENT_ROUTES_FAIL_RCG__NO_GO.
```

## 4. Proof

`prime_int_n1b_represented_carrier_candidate_matrix_no_go` verifies eight
gates.

RCM1 runs the three standing routes against RCG. PFD/Xbar and condensed
metric enrichment currently represent no RCG slots; Connes-Consani/CxC gets
only the carrier-object slot, granting curve-level object evidence.

RCM2 identifies the shared blocker bundle and recomputes the DD.4 class in
truncations L=6,8,10,12:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

RCM3 checks that finite-field positive sign and projection vocabulary do not
replace the shared blocker: the q=7 sign is negative, but semantic
projection defect is 27.

RCM4 performs the construction attempt. Adding the shared
boundary+endpoint+control-death bundle to each route is necessary but still
does not pass RCG.

RCM5 checks endpoint insufficiency using the `(10,F,1)` and `(7,F,4)`
finite-field anchor pair.

RCM6 checks positive control survival: the q=3 control has negative
primitive sign and projection defect 11, with no formation death.

RCM7 selects the best current route and next token bundle: Connes-Consani/CxC
has the most represented evidence, but the next construction target remains
the boundary+endpoint+control-death bundle.

RCM8 records the banked no-go: no standing route currently supplies the
represented carrier.

## 5. Impact on R1

```text
R1 after docs 138-288:
  NEWLY CLOSED THIS CYCLE:
    - the current represented evidence of the three standing doc-137 routes
      as a completed carrier candidate;
    - route selection by vocabulary or promises rather than represented
      evidence;
    - treating curve-level object evidence, local Xbar evidence, or metric
      enrichment as enough for the square carrier.

  POSITIVE INFORMATION RETAINED:
    - Connes-Consani/CxC is the best current represented route only because
      it has curve-level object evidence;
    - the next target is now concrete: boundary+endpoint+control-death
      represented evidence;
    - that target is necessary but not sufficient, so it must be followed by
      rep_NS, proper pullbacks, projection, Rosati, graph data, and DD.4
      carrier coupling.

  STILL ADMISSIBLE:
    - a strengthened PFD/Xbar route constructing actual Qbar+Q+dQ, p1,p2,
      boundary localization, and control death;
    - a strengthened Connes-Consani route extending curve-level evidence to
      the self-product square with represented correspondences;
    - a strengthened condensed route producing actual carrier geometry rather
      than analytic/metric enrichment alone.

  STILL OPEN:
    - construct the represented boundary+endpoint+control-death bundle.
```

## 6. Kill Conditions

```text
KILL-RCM.1 current-route completion
  Kill claims that any standing doc-137 route currently passes RCG.

KILL-RCM.2 curve-level object promoted to square carrier
  Kill promotion from curve-level object evidence to End(C x C) unless the
  self-product square correspondences are represented.

KILL-RCM.3 local/stage Xbar promoted to Qbar
  Kill promotion from local/stage Xbar evidence to Qbar+Q+dQ unless the
  represented boundary and endpoint maps are supplied.

KILL-RCM.4 metric enrichment promoted to carrier geometry
  Kill condensed/liquid metric positivity unless it constructs Qbar, p1,p2,
  dQ, rep_NS, proper pullbacks, projection, boundary, Rosati, and control
  death.

KILL-RCM.5 blocker bundle by declaration
  Kill declared boundary+endpoint+control-death bundles unless each token is
  represented.

KILL-RCM.6 necessary bundle as sufficient carrier
  Even represented boundary+endpoint+control death is not enough by itself:
  rep_NS, proper pullbacks, projection, Rosati, and graph data must follow.
```
