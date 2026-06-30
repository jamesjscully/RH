# 618 - Qbar_BECD FIdx24 Negation-Normalized Role-Payload Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 `not_source_internal` singleton residual cannot be repaired by
treating `not` as reusable morphism-level evidence.

The named mechanism is **negation-normalized singleton persistence**.

## Setup

Doc 617 kills action-normalized role-payload reuse. The remaining singleton
residual naturally suggests a different normalization: interpret `not` as a
morphism rather than as payload data.

The witness tests two normalizations:

```text
leading-not deletion: delete not only when it is the first segment;
all-not deletion:     delete every not segment.
```

## Obstruction

For both normalizations, `not_source_internal` normalizes to:

```text
source_internal
```

But the normalized group is still a singleton:

```text
escape_boundary:..._not_source_internal
```

Both normalizations leave exactly seven reused normalized payload groups, and
none of those groups is class-pure. The broader segment supports remain mixed:

```text
source segment: source_constraint_invariant, trace_payload_route, source_internality
not segment:    terminal_basin_entry, finite_index_budget, source_internality
```

Thus negation normalization does not produce reusable morphism evidence for the
source-internal singleton. It only renames the singleton payload key.

## Consequence

The surviving route cannot be exact role-payload reuse, action normalization,
or negation normalization. It must add genuinely new proof-relevant morphism
evidence outside the current doc-610 source-event payload algebra, or prove
that every such addition is synthetic duplication, name lookup, stem retuning,
class collapse, or a doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_negation_normalized_role_payload_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNEGATIONNORMROLEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMNEGATIONNORMROLEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the leading-not and all-not normalized payload groupings, the singleton status
of `not_source_internal`, and the mixed-class profile of all reused normalized
groups.
