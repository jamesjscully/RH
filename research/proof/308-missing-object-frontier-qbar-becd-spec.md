# 308 - Missing-object frontier: Qbar_BECD

Status: construction-spec frontier anchor, 2026-06-22. One-hundred-seventy-first
cycle of the doc-137 construction arc. This is not a no-go theorem, not an RH
proof, and not added to the no-go bank.

Docs 256, 257, 276, and 287 froze the square-carrier contract, the DD.4/SCC
interface, the carrier-first categorical route, and the represented-carrier
gate. Docs 288-307 then eliminated the current routes and the main
categorical shortcuts. This document records the constructive frontier forced
by that evidence:

```text
first find Qbar_BECD,
then build rep_NS/proper/projection/Rosati/graph data on top of it.
```

Witness, lead-reran this cycle:
`prime_int_n1b_missing_object_frontier` (MOF1-MOF8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_represented_carrier_candidate_matrix_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The phrase "find the missing object" is too broad unless it is split at the
represented-carrier gate. The current bank shows the first missing object is
not a period, trace formula, topos, moduli stack, completion, localization, or
canonical choice. It is the first represented carrier subobject:

```text
Qbar_BECD =
  actual compactified square Qbar with open Q and boundary dQ,
  actual endpoint maps p1,p2 and proper pushforwards,
  actual boundary/localization map killing the DD.4 class,
  self-dual boundary/properness data,
  formation-level death of DH/Epstein/controls.
```

This is Phase A. It is necessary and not sufficient. Phase B must then add:

```text
integral rep_NS, diagonal, Frobenius/Hecke graph, proper pullbacks,
fiber-product composition, projection formula, carrier Rosati duality,
primitive positive sign.
```

## 2. Lemma

```text
Lemma 308.1 (the missing-object frontier).

Under the represented-carrier gate, the current route evidence is:

    PFD/Xbar                         no represented slots,
    Connes-Consani scaling-site/CxC  carrier_object only,
    condensed/liquid metric          no represented slots.

Thus Connes-Consani/CxC is only a starting line, not the object.

The first represented object to construct is:

    Qbar_BECD = Qbar + Q + dQ + p1,p2 + boundary localization
                killing DD.4 + self-dual boundary/properness
                + formation-level control death.

It fills exactly the Phase-A slots:

    carrier_object, endpoint_maps, DD.4_boundary_killing, control_death.

Each Phase-A bundle is necessary:

    without Qbar/Q/dQ, no carrier_object;
    without p1,p2 and pushforward, no endpoint_maps;
    without boundary map, exact localization, DD.4 zero, and self-dual
    boundary, no DD.4_boundary_killing;
    without control-instantiation impossibility and formation death, no
    control_death.

The DD.4 obstruction remains nonzero in the base coefficient system:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1

in truncations L=6,8,10,12. Therefore Phase A requires an actual
boundary/localization map, not a declared zero or formal splitter.

Endpoint maps must be represented pushforwards. In the q=7, Tr(F)=1 finite
anchor, `(10,F,1)` and `(7,F,4)` have the same total degree and the same
diagonal pairing but different endpoints.

Control death must be formation failure. The q=3 positive control still has
negative primitive sign and semantic projection defect 11 unless it fails to
instantiate Qbar_BECD itself.

After Qbar_BECD, the remaining slots are exactly:

    integral_rep_NS, diagonal, Frobenius_graph, proper_composition,
    projection_formula, Rosati_duality, primitive_positive_sign.

Those are Phase B. Phase A plus Phase B is the full represented-carrier
contract. Phase A alone is not End(S^2/Z), not RH, and not sufficient.
```

Verdict label:

```text
N1B_MISSING_OBJECT_FRONTIER__QBAR_BECD_THEN_REPNS_CORR_ROSATI__SPEC.
```

## 3. Proof

`prime_int_n1b_missing_object_frontier` verifies eight gates.

MOF1 reruns the current route matrix: PFD/Xbar has no represented slots,
Connes-Consani/CxC has only `carrier_object`, and condensed metric enrichment
has no represented slots.

MOF2 identifies the Phase-A frontier. The evidence tokens

```text
object_actual, open_actual, boundary_actual,
p1_map_actual, p2_map_actual, proper_pushforward_actual,
boundary_map_actual, localization_exact_actual,
dd4_class_mapped_to_zero, self_dual_boundary_actual,
control_instantiation_impossible, control_death_at_formation_proved
```

fill exactly `carrier_object`, `endpoint_maps`, `DD.4_boundary_killing`, and
`control_death`.

MOF3 deletes each Phase-A bundle in turn and checks that the corresponding
represented slot disappears.

MOF4 recomputes the DD.4 obstruction:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

and verifies that deleting `dd4_class_mapped_to_zero` breaks the DD.4 slot.

MOF5 checks endpoint non-substitutability using the `(10,F,1)` and `(7,F,4)`
finite-field pair.

MOF6 checks control survival: the q=3 control has primitive sign -5.500 and
semantic projection defect 11, so control death must be a formation
obstruction.

MOF7 records that Qbar_BECD is necessary but not sufficient: the Phase-B slots
remain.

MOF8 checks that adding Phase-B evidence fills exactly the full represented
carrier contract.

## 4. Impact on R1

```text
R1 after docs 138-308:
  NEWLY FIXED THIS CYCLE:
    - the missing object is split into a first represented frontier and a
      second square-correspondence phase.

  PHASE A OBJECT TO FIND:
    - Qbar_BECD: actual Qbar/Q/dQ, p1,p2, endpoint pushforwards, carrier
      boundary localization killing DD.4, self-dual boundary/properness, and
      formation-level control death.

  PHASE B AFTER PHASE A:
    - integral rep_NS, diagonal, Frobenius/Hecke graph, proper pullbacks,
      fiber-product composition, projection formula, D^2=id Rosati, primitive
      positive sign.

  ROUTE PRIORITY:
    - Connes-Consani/CxC remains the best current starting line only because
      it has carrier-object evidence. It still must construct the square
      boundary/endpoints/control-death frontier.

  STILL OPEN:
    - construct Qbar_BECD.
```

## 5. Acceptance and Kill Conditions

```text
ACCEPT-MOF.1  Produce actual Qbar, Q, and dQ.
ACCEPT-MOF.2  Produce actual p1,p2 and proper pushforwards.
ACCEPT-MOF.3  Produce the boundary/localization map and prove the DD.4 class
              maps to zero through it.
ACCEPT-MOF.4  Prove the boundary/properness data is self-dual and carrier
              native.
ACCEPT-MOF.5  Prove DH/Epstein/controls cannot instantiate Qbar_BECD at
              formation.
ACCEPT-MOF.6  Only after Phase A, build Phase B: rep_NS, proper pullbacks,
              projection, Rosati, primitive sign, diagonal, and graph.

KILL-MOF.1    Reject any "missing object" proposal that skips Qbar_BECD and
              jumps directly to a period, trace, completion, localization, or
              positivity theorem.
KILL-MOF.2    Reject Phase-A bundles by declaration; every token must be
              represented.
KILL-MOF.3    Reject Phase A as sufficient. It is the frontier object, not
              End(S^2/Z).
KILL-MOF.4    Reject Phase B evidence before Phase A exists as represented
              carrier geometry.
```
