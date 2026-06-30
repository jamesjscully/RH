# 609 - Qbar_BECD FIdx24 Typed Source Event Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-608 typed source-event classifier cannot be promoted to a reused
source-event grammar by forbidding one-shot exact tail literals.

The named mechanism is **singleton-tail lookup leakage**.

## Setup

Doc 608 is the constructive counter-move to doc 607. It replaces substring
priority by typed source events: namespace, obstruction-tail, exact tail, or
one named event kind. It preserves all 106 doc-606 surface classes and the
doc-602 anchor map with 70 rule literals.

This no-go tests the stricter structural reading that every event rule should
be reused by at least two boundary surfaces. Under that reading, exact
tail-name rules cannot function as a hidden row lookup.

## Obstruction

Of the 70 doc-608 rule ids, only four are reused:

```text
namespace:action
namespace:class
namespace:invariant
namespace:payload
```

The other 66 rules are singleton exact-tail, obstruction-tail, or named-event
rules. Those 66 singleton decisions span every one of the 17 doc-608 classes.
The reused rules cover only 40 of the 106 boundary surfaces.

The doc-607 hard repair is itself singleton:

```text
event_kind:missing_terminal_basin_certificate
```

Coarser repairs do not recover the lost decisions. The `entry_missing_tail`
and `plain_tail` event-kind families each merge 14 classes, the
`obstruction_namespace` family merges four classes, and 37 underscore segments
are class-ambiguous. Suffix-family repairs also merge incompatible classes.

## Consequence

Doc 608 remains a valid exact typed-event classifier. What doc 609 kills is the
stronger claim that doc 608 has already found a reusable categorical event
grammar. The next constructive frontier must add genuine compositional event
structure, or prove that such structure cannot exist, rather than merely
retain exact source-tail names.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTYPEDEVENTREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTYPEDEVENTREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies the 106 doc-608 decisions, 70 rule literals, four reused
namespace rules, 66 singleton decisions, singleton coverage across all 17
classes, the singleton status of the doc-607 hard repair, ambiguity of coarse
event-kind and segment repairs, and the failure of suffix-family repairs.
