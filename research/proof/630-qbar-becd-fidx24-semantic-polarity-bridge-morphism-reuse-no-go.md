# 630 - Qbar_BECD FIdx24 Semantic-Polarity-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by treating the
visible semantic polarity vocabulary

```text
external / oracle / not / source / internal
```

as the missing reusable bridge morphism.

The named mechanism is **semantic-polarity selector collapse**.

## Setup

Doc 629 kills the direct two-surface bridge between:

```text
entry_boundary:obstruction:external_or_oracle
escape_boundary:..._not_source_internal
```

The next plausible repair is not to pair the residual labels directly, but to
place them inside a broader noninternality or polarity closure. That repair is
proof-relevant only if the closure is reused and class-pure, rather than a
mixed bucket followed by a selector.

## Obstruction

The reusable semantic closures are mixed-class:

```text
external/oracle closure:
  5 surfaces
  terminal_basin_entry=2, action_semantics=1,
  classifier_partition=1, boundary_externality=1

not/source/internal closure:
  7 surfaces
  terminal_basin_entry=3, source_constraint_invariant=1,
  trace_payload_route=1, finite_index_budget=1,
  source_internality=1

combined noninternal closure:
  12 surfaces
  terminal_basin_entry=5, action_semantics=1,
  classifier_partition=1, source_constraint_invariant=1,
  boundary_externality=1, trace_payload_route=1,
  finite_index_budget=1, source_internality=1
```

The exact closures do not solve the problem:

```text
normalized exact external_or_oracle:
  action_semantics=1, classifier_partition=1, boundary_externality=1

exact source/internal, not/source, and not_source_internal:
  singleton source_internality residual lookup
```

Using `or` as an ordinary segment token makes the external closure even less
semantic: it pulls in the unrelated `presentation_or_sample` class and
obstruction surfaces.

Thus there is no semantic-polarity closure in the current doc610 source-event
algebra that is both reused and class-pure. Broad polarity closures are
reusable only because they mix incompatible classes; exact purity is obtained
only by collapsing back to singleton lookup or to the already-killed mixed
action/class/obstruction triple.

## Consequence

The surviving route still needs independent proof-relevant morphism evidence
explaining why `boundary_externality` and `source_internality` should be
coupled. A semantic internal/external polarity slogan is not enough unless it
constructs a new class-pure reused morphism outside the visible doc610
segment algebra; otherwise it is synthetic duplication, name lookup, stem
retuning, class collapse, or a doc-602 anchor change.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_semantic_polarity_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSEMPOLARITYBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSEMPOLARITYBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the mixed profiles of broad external/oracle, not/source/internal, and combined
noninternal closures, the mixed normalized `external_or_oracle` triple, the
singleton status of exact source/internal closures, and the pollution caused
by treating `or` as a semantic segment token.
