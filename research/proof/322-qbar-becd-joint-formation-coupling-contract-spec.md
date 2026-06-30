# 322 - Qbar_BECD joint formation coupling contract

Status: construction-spec refinement anchor, 2026-06-22.
One-hundred-eighty-fifth cycle of the doc-137 construction arc. This is not
a no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 321 fixed the timing:

```text
controls must be impossible to instantiate at carrier formation.
```

This document sharpens what "joint formation" means. A conjunction of
already-named atoms does not count. A product of local atom-moduli does not
count. A sequential pipeline in which controls enter and fail later does not
count. The carrier must contain one represented non-split primitive that
couples endpoint degrees, boundary normal ratio, boundary pushforward
compatibility, graph/composition, Rosati, count/degree anchors, and control
exclusion.

Witness, lead-reran this cycle:
`prime_int_n1b_qbar_becd_joint_formation_coupling_contract`
(JFC1-JFC10 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_becd_control_formation_death_contract`,
`prime_int_n1b_qbar_becd_boundary_pushforward_compat_contract`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_fiber_product_saturated_positive_envelope_no_go`,
`prime_int_n1b_cc_product_square_cycle_category_no_go`,
`prime_int_n1b_cc_product_square_cycle_universal_property_recognition_no_go`,
and `prime_int_n1b_dd4_scc_interface`.

## 1. Purpose

The remaining live target can still be weakened in a subtle way:

```text
build or name each required atom separately,
then take their intersection/product/conjunction.
```

That is not Qbar_BECD. The square itself must be the reason the atoms cannot
separate. The endpoint maps, degree maps, boundary normal ratio, restricted
localization, pushforward compatibility, graph/composition, Rosati duality,
count/degree anchors, and control exclusion must all depend on the same
carrier primitive.

This contract is stricter than the represented-carrier gate. Represented
evidence is necessary; non-split coupling is the next requirement.

## 2. Lemma

```text
Lemma 322.1 (joint formation requires non-split carrier coupling).

The finite-field anchor has the desired coupled shadows:

    Delta.Gamma_n = #C(F_{q^n}) for n=1,2,3,
    Gamma_1 o Gamma_2 = Gamma_3,
    primitive Rosati sign < 0.

Doc 321 supplies the list of live atoms:

    carrier,
    endpoint,
    boundary,
    pushforward,
    graph,
    Rosati,
    count_degree,
    control_death.

The accepted Qbar_BECD formation datum must add a represented coupling
primitive whose dependency graph contains the live edges:

    carrier -- endpoint,
    endpoint -- boundary,
    boundary -- pushforward,
    pushforward -- graph,
    graph -- Rosati,
    graph -- count_degree,
    Rosati -- control_death,
    control_death -- carrier.

Equivalently, the carrier primitive must make these atoms one non-split
formation datum. The accepted datum is exactly:

    carrier-native,
    actual formation primitive,
    represented object/map/cycle evidence,
    endpoint integrality native,
    degree maps native,
    DD.4 boundary native,
    boundary pushforward compatibility native,
    proper graph composition native,
    positive Rosati native,
    finite-field count anchor native,
    graph-degree anchor native,
    controls impossible at the first generator,
    controls not instantiated before a filter,
    endpoints and boundary coupled by the same relation,
    boundary and pushforward coupled by the same relation,
    pushforward and graph coupled by the same relation,
    graph and Rosati coupled by the same relation,
    graph and count/degree anchors coupled by the same relation,
    Rosati and control death coupled by the same relation,
    non-split dependency graph,
    no atomwise intersection,
    no product of local moduli,
    no sequential pipeline,
    no post-hoc filter,
    no declared coupling,
    no semantic zeta tag,
    not formable on controls.
```

Verdict label:

```text
N1B_QBAR_BECD_JOINT_FORMATION_COUPLING__NON_SPLIT_CARRIER_PRIMITIVE_OR_NOTHING__SPEC.
```

## 3. Proof

`prime_int_n1b_qbar_becd_joint_formation_coupling_contract` verifies ten
gates.

JFC1 records the finite-field count, graph, and Rosati shadows.

JFC2 records that the doc-321 atom list still needs a represented coupling
primitive.

JFC3 rejects atomwise intersection of gates.

JFC4 rejects product of local atom-moduli.

JFC5 rejects sequential filter pipelines where controls enter before carrier
death.

JFC6 rejects declared coupling names and semantic zeta tags.

JFC7 checks that controls satisfy substantial formal shadows but fail the
carrier primitive.

JFC8 requires every live coupling edge.

JFC9 rejects retuning count or graph-degree anchors to force compatibility.

JFC10 records the live predicate. Only represented non-split joint formation
coupling passes.

## 4. Impact on R1

```text
R1 after docs 138-322:
  NEWLY FIXED THIS CYCLE:
    - "joint formation" means one represented non-split carrier primitive
      coupling endpoint, boundary, pushforward, graph, Rosati, count/degree,
      and control-death atoms.

  CURRENT LIVE TARGET:
    - construct the represented Qbar_BECD carrier primitive;
    - prove it supplies Qbar, Q, dQ, p1, p2, object/map/cycle evidence;
    - prove endpoint integrality and degree maps arise from it;
    - prove the DD.4 boundary normal ratio arises from it;
    - prove restricted localization commutes with p1_* and p2_* through it;
    - prove proper graph/composition, count anchors, graph-degree anchors,
      and positive Rosati through it;
    - prove controls cannot instantiate its first generator.

  DISCIPLINE:
    - atomwise intersections, product moduli, local fiber products,
      universal-property recognition, sequential filters, declared couplings,
      semantic zeta tags, and retunings are diagnostics only.

  STILL OPEN:
    - construct the represented non-split Qbar_BECD carrier primitive.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-JFC.1  Exhibit an actual represented carrier primitive.
ACCEPT-JFC.2  Its dependency graph couples carrier, endpoint, boundary,
              pushforward, graph, Rosati, count/degree, and control death.
ACCEPT-JFC.3  Endpoint integrality and degree maps are native to that
              primitive.
ACCEPT-JFC.4  DD.4 boundary death and boundary pushforward compatibility are
              native to that primitive.
ACCEPT-JFC.5  Graph/composition, positive Rosati, finite-field count anchors,
              and graph-degree anchors are native to that primitive.
ACCEPT-JFC.6  Controls cannot instantiate the first generator.

KILL-JFC.1    Reject atomwise intersections of required gates.
KILL-JFC.2    Reject products of local atom-moduli.
KILL-JFC.3    Reject sequential filter pipelines.
KILL-JFC.4    Reject declared couplings or semantic zeta tags.
KILL-JFC.5    Reject local retunings of count or graph-degree anchors.
KILL-JFC.6    Reject packages formable on controls.
```
