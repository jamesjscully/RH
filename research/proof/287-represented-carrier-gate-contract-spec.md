# 287 - Represented-carrier gate contract

Status: construction-spec evidence gate, 2026-06-21.
One-hundred-fiftieth cycle of the doc-137 construction arc. This is not a
no-go theorem, not an RH proof, and not added to the no-go bank.

Doc 286 killed the Qbar shell: naming `Qbar`, `p1,p2`, `dQ`,
`Corr^prop`, localization, projection, Rosati, and control death can pass a
name-level checklist while representing zero carrier slots. This document
records the next discipline upgrade:

```text
slot names count only with represented object/map/cycle/pullback/boundary
evidence.
```

Witness, lead-reran this cycle:
`prime_int_n1b_represented_carrier_gate_contract` (RCG1-RCG8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_qbar_shell_positive_envelope_no_go`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

The project now needs a gate, not another vocabulary list. Docs 256 and 276
already say which slots a carrier must provide. Doc 286 shows that a
candidate can satisfy that list by names.

This contract changes the acceptance rule:

```text
declared slot != represented slot.
```

Every future candidate must attach each slot to evidence of an actual object,
map, cycle group, pushforward, proper pullback, boundary map, duality, or
control-formation obstruction. Otherwise it is a shell.

## 2. Represented Evidence Contract

A construction-grade carrier submission must supply represented evidence for
all eleven slots.

```text
RCG.1 carrier object
  actual Qbar, open Q, and boundary dQ.

RCG.2 endpoint maps
  actual maps p1,p2 and proper pushforward. Endpoint integrality and the two
  degree maps must be pushforwards, not labels or decoders.

RCG.3 integral rep_NS
  actual cycle/K-theory lattice, intersection form, and representability
  functor.

RCG.4 diagonal
  an actual diagonal cycle in rep_NS, not a declared identity symbol.

RCG.5 Frobenius/Hecke graph
  an actual graph cycle whose count pairings are carrier consequences.

RCG.6 proper composition
  actual proper pullbacks and a proved fiber-product composition theorem.

RCG.7 projection formula
  a proper push-pull proof against the carrier intersection form.

RCG.8 DD.4 boundary killing
  an actual carrier boundary map, exact localization, the class mapped to
  zero, and self-dual boundary/properness data.

RCG.9 Rosati duality
  an actual duality functor, D^2=id proof, and Rosati evaluation theorem.

RCG.10 primitive positive sign
  a carrier proof of the primitive Hodge/Rosati sign.

RCG.11 control death
  proof that DH/Epstein/controls cannot instantiate the carrier at
  formation, before any positivity, quotient, trace, period, or realization
  filter.
```

## 3. Lemma

```text
Lemma 287.1 (represented evidence is the acceptance gate).

A name-level Qbar shell can declare all eleven carrier slots:

    Qbar, Q, dQ, p1,p2, rep_NS, Delta, Gamma, Corr^prop,
    fiber products, projection formula, localization, DD.4 killing,
    Rosati, primitive sign, and control death.

The represented-carrier gate assigns this shell zero represented slots.

The finite-field q=7, Tr(F)=1 model is accepted only for the visible slots
it actually represents:

    carrier object, endpoint maps, integral rep_NS, diagonal,
    Frobenius graph, proper composition, Rosati duality, and primitive sign.

It verifies:

    Delta.Gamma_n = #C(F_{q^n}) for n=1,2,3,
    Gamma_1 o Gamma_2 = Gamma_3,
    primitive sign negative on-circle and positive off-circle.

It does not fill the zeta-side projection formula, DD.4 boundary killing, or
control death slots.

Projection formula evidence requires represented proper pushforward,
proper pullbacks, a proof of the formula, and the carrier intersection form.
A declared projection formula is rejected; the positive `U+End` semantic
projection defect remains 27.

DD.4 killing requires an actual carrier boundary map, exact localization,
the DD.4 class mapped to zero, and self-dual boundary data. A declared
splitter or chosen coboundary is rejected. In the base coefficient system,
for L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Endpoint maps require represented `p1,p2` pushforwards. Labels or total
degree decoders are rejected: `(10,F,1)` and `(7,F,4)` have the same total
degree and the same diagonal pairing, but different endpoints.

Control death requires formation failure. A named `control_death` guard is
rejected; only proof that controls cannot instantiate the carrier counts.

A complete represented evidence package is slotwise necessary. Removing
essential witnesses such as the actual object, `p1`, proper pullbacks,
boundary map, duality functor, or control-instantiation obstruction breaks
the required slot set.

Therefore future proposals must pass the represented-carrier gate before any
downstream categorical, motivic, trace, period, or positivity language is
allowed to count as evidence.
```

## 4. Proof

`prime_int_n1b_represented_carrier_gate_contract` verifies eight gates.

RCG1 rejects a name-level Qbar shell: it declares all eleven slots but
represents zero.

RCG2 accepts the finite-field model only for represented visible slots. The
q=7 anchor gives the correct counts for n=1,2,3, graph composition, and
primitive sign behavior, but not zeta-side projection, DD.4 killing, or
control death.

RCG3 enforces projection evidence: declaration is rejected, proper push-pull
evidence is accepted, and the semantic defect 27 remains the warning.

RCG4 enforces DD.4 boundary evidence: free splitters are rejected, represented
boundary maps are accepted as the required evidence shape, and the base
class remains non-boundary in the tested truncations.

RCG5 enforces endpoint evidence: `p1,p2` labels and total-degree decoders are
not two carrier-native pushforwards.

RCG6 enforces control death: a named guard is rejected; formation failure is
the evidence.

RCG7 checks slotwise necessity for a complete represented evidence package.
Deleting the actual object, `p1`, proper pullbacks, boundary map, duality
functor, or control-instantiation obstruction breaks the full slot set.

RCG8 records the status: this is an evidence gate only. The zeta-side
represented carrier is still absent.

## 5. Impact on R1

```text
R1 after docs 138-287:
  NEWLY FIXED THIS CYCLE:
    - the represented-carrier acceptance gate. Future proposals must provide
      represented evidence for every SCC/CFC slot. Names, declared formulas,
      shell localizations, and control-death guards do not count.

  STILL ADMISSIBLE:
    - a compactified zeta square with actual Qbar, Q, dQ, p1,p2, integral
      cycles, proper pushforwards, Corr^prop(Qbar), proper pullbacks,
      projection formula, boundary localization killing DD.4, carrier
      Rosati, primitive sign, and formation-level control death.

  STILL OPEN:
    - produce represented evidence for the carrier over Z.
```

## 6. Acceptance and Kill Conditions

```text
ACCEPT-RCG.1 Submit actual object/map evidence for Qbar, Q, dQ, p1,p2.
ACCEPT-RCG.2 Submit cycle/K-theory evidence for integral rep_NS and
             intersection.
ACCEPT-RCG.3 Submit actual proper pullbacks and prove composition.
ACCEPT-RCG.4 Prove projection by carrier push-pull.
ACCEPT-RCG.5 Exhibit the carrier boundary map killing DD.4.
ACCEPT-RCG.6 Exhibit carrier duality/Rosati and primitive positivity.
ACCEPT-RCG.7 Prove controls fail at carrier formation.

KILL-RCG.1 Reject CFC/SCC slot names without represented evidence.
KILL-RCG.2 Reject declared projection formulas without push-pull proof.
KILL-RCG.3 Reject boundary/localization labels without a carrier boundary map.
KILL-RCG.4 Reject p1,p2 labels or endpoint decoders without pushforwards.
KILL-RCG.5 Reject named control-death guards without formation failure.
KILL-RCG.6 Reject any downstream realization before the represented gate
             passes.
```
