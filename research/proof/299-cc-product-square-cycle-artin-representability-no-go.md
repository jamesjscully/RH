# 299 - CC product square-cycle Artin representability is not the square carrier

Status: no-go + CC-product-square-cycle-Artin-representability deletion, 2026-06-22.
One-hundred-sixty-second cycle of the doc-137 construction arc. Doc 298
killed the pro-representable/inverse-limit shortcut. This document tests the
next categorical repair:

```text
verify Artin/Schlessinger/Lurie-style deformation, obstruction, effectivity,
and limit-preservation criteria for the square-carrier specification, and
count the representability theorem invocation as the represented carrier.
```

Witness, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_artin_representability_no_go`
(ART1-ART8 ALL PASS).

Adjacent witnesses, lead-reran this cycle:
`prime_int_n1b_cc_product_square_cycle_pro_representable_limit_no_go`,
`prime_int_n1b_cc_product_square_cycle_reflective_completion_no_go`,
`prime_int_n1b_represented_carrier_gate_contract`,
`prime_int_n1b_carrier_first_categorical_square_contract`,
`prime_int_n1b_dd4_scc_interface`, and
`prime_int_n1b_square_carrier_contract`.

## 1. Purpose

Doc 298 rejected treating a pro-object of finite approximations as the
carrier. The next repair is to invoke a representability theorem:

```text
Artin/Schlessinger/Lurie criteria for the square-carrier moduli problem
= represented compactified zeta square.
```

A genuine moduli construction may later be certified by such criteria. The
shortcut is to count the criteria, tangent-obstruction package, and
effectivity predicates as the carrier geometry itself.

## 2. Lemma

```text
Lemma 299.1 (representability criteria are not the representing object).

The product+rep_NS visible data represents only:

    carrier_object, endpoint_maps, integral_rep_NS, diagonal,
    Frobenius_graph.

The Artin/Schlessinger/Lurie criterion package lists all eleven required
predicates:

    carrier object, endpoint maps, rep_NS, diagonal, Frobenius graph,
    proper composition, projection formula, DD.4 boundary killing,
    Rosati duality, primitive positive sign, and control death.

But under the represented-carrier gate it represents no new `Qbar` evidence.
Formal deformation functors, cotangent complexes, obstruction groups,
effectivity predicates, and limit-preservation checks are not actual zeta
square maps, pullbacks, boundary localization, Rosati evaluation, or
control-formation obstruction.

For the q=7, Tr(F)=1 anchor, finite-field counts and graph composition remain
correct, but the formal projection obstruction is zero only at the criterion
level. The semantic projection defect remains 27.

Realizing the projection criterion in NS triples repeats retuning:

    graph degree d1 changes from 7 to -20,

while the genuine second count anchor remains 63.

The obstruction-theory zero does not kill the actual DD.4 class. In
truncations L=6,8,10,12:

    H^1(<phi>; 1+z F_2[[z]]) = Z/2,
    [(1+z)^-1] != 0,
    res_1((1+z)^-1)=1.

Deformation data parameterizes choices rather than selecting carrier data.
The tested boundary window has 16 primitive directions, two Rosati branches,
and four square-zero extension shapes, hence 128 deformation branches. The
q=7 primitive sign is -13.500 on the Weil anchor and +2.431 on the planted
off-circle q-similitude.

Positive controls satisfy the same criteria. The q=3 control has semantic
projection defect 11, negative primitive sign -5.500, the same five
represented slots, and no formation-level control death.

Consequently the Artin-representability wrapper still misses represented:

    proper_composition, projection_formula, DD.4_boundary_killing,
    Rosati_duality, primitive_positive_sign, control_death.

It is not the square carrier and not `End(S^2/Z)`.
```

Verdict label:

```text
N1B_CC_PRODUCT_SQUARE_CYCLE_ARTIN_REPRESENTABILITY__CRITERIA_NOT_QBAR__NO_GO.
```

## 3. Proof

`prime_int_n1b_cc_product_square_cycle_artin_representability_no_go` verifies
eight gates.

ART1 checks that product+`rep_NS` visible data has only the five represented
slots.

ART2 checks that the Artin criterion package lists all eleven slots but
represents no new `Qbar` evidence.

ART3 checks projection: the formal criterion obstruction is zero, while the
semantic defect remains 27.

ART4 checks that realizing the criterion changes graph degree `d1` from 7 to
-20 while the count anchor remains 63.

ART5 recomputes DD.4:

```text
L6:  |B|=2^3, |Z1|=2^4, |H1|=2
L8:  |B|=2^4, |Z1|=2^5, |H1|=2
L10: |B|=2^5, |Z1|=2^6, |H1|=2
L12: |B|=2^6, |Z1|=2^7, |H1|=2
```

ART6 checks parameterization rather than selection: 16 boundary directions,
two Rosati branches, four square-zero extension shapes, 128 deformation
branches, and on/off-circle sign separation remain.

ART7 checks positive control survival: the q=3 control satisfies the same
criteria with projection defect 11 and no represented control death.

ART8 applies the represented-carrier gate and records the six missing slots.

## 4. Impact on R1

```text
R1 after docs 138-299:
  NEWLY CLOSED THIS CYCLE:
    - Artin/Schlessinger/Lurie criteria as the carrier;
    - tangent-obstruction package as representability proof;
    - formal projection obstruction as carrier projection formula;
    - obstruction-theory zero as carrier boundary killing;
    - deformation/effectivity data as boundary/Rosati/control selection.

  POSITIVE INFORMATION RETAINED:
    - a real moduli construction may later be certified by representability
      criteria;
    - those criteria are admissible only downstream of constructed carrier
      geometry or as part of a theorem whose output is proved to be Qbar.

  STILL ADMISSIBLE:
    - an Artin-style representability theorem whose output is explicitly
      identified with the compactified zeta square and whose universal family
      supplies actual maps, pullbacks, projection, Rosati, DD.4 boundary,
      graph composition, and control death.

  STILL OPEN:
    - construct the representing object, not just criteria for a specification
      functor.
```

## 5. Kill Conditions

```text
KILL-ART.1 criteria as carrier
  Kill Artin/Schlessinger/Lurie criterion arguments unless the represented
  output is proved to be actual Qbar geometry with maps, boundary, and cycles.

KILL-ART.2 tangent-obstruction package as construction
  Cotangent and obstruction data do not construct carrier maps, pullbacks,
  Rosati, or boundary localization.

KILL-ART.3 formal projection obstruction
  A vanishing formal obstruction is not the projection formula unless semantic
  carrier push-pull against the intersection form is proved.

KILL-ART.4 obstruction-theory DD.4 zero
  An obstruction-theory zero is not DD.4 boundary killing. The actual class
  [(1+z)^-1] must map to zero in the carrier boundary sequence.

KILL-ART.5 deformation data as selection
  Parameterizing deformation directions, Rosati branches, or square-zero
  extensions is not carrier selection.

KILL-ART.6 controls satisfying criteria
  If positive controls satisfy the same criteria, formation-level control
  death has failed.
```
