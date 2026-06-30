# 617 - Qbar_BECD FIdx24 Action-Normalized Role-Payload Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by
action-normalized role-payload graph reuse.

The named mechanism is **action-normalized selector collapse**.

## Setup

Doc 616 kills exact role-payload graph reuse. The next natural normalization is
minimal: let action-role nodes compose with obstruction/class nodes by stripping
only the action verbs:

```text
reject
emit
```

This tests whether visible action/class/obstruction triples supply the missing
morphism-level evidence without changing the class labels or anchors.

## Obstruction

The normalization gives seven reused payload groups. Their role profiles are:

```text
class + obstruction:          3
action + class + obstruction: 3
class + obstruction + tail:   1
```

Every reused action-normalized role-payload group is mixed-class.

The `external_or_oracle` residual now sits in a real normalized triple:

```text
entry_boundary:action:reject_external_or_oracle
entry_boundary:class:external_or_oracle
entry_boundary:obstruction:external_or_oracle
```

But the triple has class profile:

```text
action_semantics
classifier_partition
boundary_externality
```

Thus the normalization creates a graph, but not a class-pure morphism law.
Selecting the boundary-externality node still requires an extra selector.

The normalized obstruction nodes still span four classes:

```text
dependency_repair_nogo:        3
boundary_contextual_surrogate: 2
boundary_externality:          1
finite_index_budget:           1
```

For the `not_source_internal` residual, action normalization changes nothing:
there is still no reused normalized payload graph. The broader `source` and
`not` segment supports remain mixed-class.

## Consequence

The surviving route cannot be a visible role graph plus action-verb
normalization. It must add genuinely new proof-relevant morphism evidence that
is neither an existing primitive conjunction, nor an exact role-payload graph,
nor an action-normalized role-payload graph; or prove that every such addition
is synthetic duplication, name lookup, stem retuning, class collapse, or a
doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_action_normalized_role_payload_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACTIONNORMROLEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMACTIONNORMROLEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the complete action-normalized payload grouping, the mixed-class profile of all
reused normalized groups, the external_or_oracle action/class/obstruction
triple, and the continued absence of any reused normalized graph for
not_source_internal.
