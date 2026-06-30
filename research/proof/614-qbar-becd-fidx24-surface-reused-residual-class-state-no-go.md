# 614 - Qbar_BECD FIdx24 Surface-Reused Residual Class-State No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-612 residual cases cannot all be repaired by adding a new
class-pure state that is reused by at least two boundary surfaces.

The named mechanism is **surface-reuse singleton-class barrier**.

## Setup

Doc 613 kills quotient closure generated from existing shared doc-610 source
features. The next broader repair is to add new residual morphism or state
names while preserving two requirements:

```text
class purity: the state contains only surfaces from one doc-610 class;
surface reuse: the state has support on at least two boundary surfaces.
```

This test is independent of how the proposed state is named. If a residual
surface lies in a class that occurs only once in the full 106-surface doc-610
boundary set, then every class-pure surface state containing it has support at
most one.

## Obstruction

Exactly two doc-610 classes have global surface support one:

```text
boundary_externality
source_internality
```

Both singleton classes occur inside the doc-612 residual set. Their surfaces
are:

```text
entry_boundary:obstruction:external_or_oracle
escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal
```

For either surface, the maximum support of any class-pure boundary-surface
state is one. Therefore no total repair can make every doc-612 residual factor
through a reused class-pure surface state. This remains true regardless of the
new feature or morphism name added, unless the repair adds synthetic support,
merges classes, changes labels or anchors, or relaxes reuse away from actual
boundary-surface support.

The obstruction appears in both residual forms: one singleton is an
obstruction-namespace event and the other is a plain-tail event.

## Consequence

Surface-reused class-state repair is dead. The surviving categorical route must
move to morphism-level reuse with proof-relevant evidence, or prove that such
morphism-level reuse is only synthetic duplication, name lookup, stem retuning,
class collapse, or a doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSURFREUSEDRESIDCLASSSTATENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSURFREUSEDRESIDCLASSSTATENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the 106 boundary surfaces and
17 classes, the two global singleton classes, the fact that both singleton
classes occur in the doc-612 residual set, and the fact that all other residual
surfaces have class-pure surface support at least two.
