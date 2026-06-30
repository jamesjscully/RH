# 623 - Qbar_BECD FIdx24 Typed Rule-Family Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by replacing
singleton typed rule ids with the doc-608 classifier's reusable rule families.

The named mechanism is **mixed rule-family selector collapse**.

## Setup

Doc 609 kills the direct promotion of doc-608 exact rule ids to a fully reused
source-event grammar. The two residual exact rules are singletons:

```text
obstruction_tail:external_or_oracle
tail:not_source_internal
```

A natural repair is to move up one level and treat the typed rule family as the
proof-relevant morphism:

```text
obstruction_tail
tail
```

## Obstruction

The doc-608 classifier has 106 decisions, 70 used exact rule ids, and four
rule families:

```text
event_kind
namespace
obstruction_tail
tail
```

The only reused exact rule ids are the four namespace rules:

```text
namespace:action
namespace:class
namespace:invariant
namespace:payload
```

They do not cover either doc-614 residual.

For `entry_boundary:obstruction:external_or_oracle`, the exact rule
`obstruction_tail:external_or_oracle` is singleton. Its reusable family
`obstruction_tail` has seven surfaces, but the class profile is mixed:

```text
dependency_repair_nogo: 3
boundary_contextual_surrogate: 2
finite_index_budget: 1
boundary_externality: 1
```

For the `not_source_internal` escape boundary, the exact rule
`tail:not_source_internal` is singleton. Its reusable family `tail` has 58
surfaces and spans sixteen classes, with `source_internality` appearing only
once.

There is no reused class-pure rule family in the doc-608 classifier. Thus
passing from singleton exact rules to reusable families only replaces singleton
lookup with a mixed-class selector.

## Consequence

The surviving route cannot use the current typed rule-family dispatcher as the
missing morphism. It must add new proof-relevant morphism evidence outside
doc610 primitive algebra, source-event payload algebra, doc605 route graph,
frontier-map consistency/rejection bookkeeping, executable stage-lineage
diagnostics, doc610 audit dependency wiring, and doc608 typed rule-family
dispatch; or prove that every such addition is synthetic duplication, name
lookup, stem retuning, class collapse, or a doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_rule_family_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTYPEDRULEFAMILYMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTYPEDRULEFAMILYMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-608/doc-610 acceptance, the two doc-614 singleton
residuals, the exact rule and rule-family supports, the mixed class profiles of
`obstruction_tail` and `tail`, and the absence of any reused class-pure rule
family.
