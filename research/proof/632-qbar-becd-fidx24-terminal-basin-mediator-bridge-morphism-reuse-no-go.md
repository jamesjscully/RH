# 632 - Qbar_BECD FIdx24 Terminal-Basin-Mediator-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by routing the
bridge through the visible `external_basin` and `oracle_basin`
terminal-basin surfaces.

The named mechanism is **terminal-basin mediator selector collapse**.

## Setup

Doc 631 shows that broad boundary transducer axes are mixed-class. The
sharpest remaining boundary-style repair is a two-leg mediator:

```text
entry external_or_oracle obstruction
  -> external_basin / oracle_basin
  -> not_source_internal escape tail
```

The two middle surfaces are real terminal-basin surfaces:

```text
escape_boundary:..._external_basin
escape_boundary:..._oracle_basin
```

They are both `terminal_basin_entry` escape plain tails. The question is
whether they give proof-relevant bridge evidence rather than a pair of
mixed-class selectors.

## Obstruction

The mediator set itself is class-pure:

```text
external_basin/oracle_basin mediators:
  terminal_basin_entry=2
```

but neither attachment leg is class-pure.

The entry-to-mediator leg uses external/oracle vocabulary:

```text
external/oracle closure:
  5 surfaces
  terminal_basin_entry=2, action_semantics=1,
  classifier_partition=1, boundary_externality=1
```

The mediator-to-source-internal leg can use the escape center prefix or the
plain-tail event kind:

```text
escape center/terminal prefix:
  43 surfaces across 16 classes

plain_tail:
  37 surfaces across 14 classes
```

The basin segment support contains the mediators, but it misses both residual
surfaces:

```text
basin segment:
  terminal_basin_entry=10, action_semantics=1
```

The mediators also have no exact segment or namespace overlap with the
`not_source_internal` residual. Therefore the mediator path crosses three
classes:

```text
boundary_externality -> terminal_basin_entry -> source_internality
```

and needs selectors on both legs.

## Consequence

The terminal-basin mediators are not useless; they show where the boundary
story wants to go. But in the current doc610 source-event algebra they do not
construct the missing morphism. A surviving route must add an actual
proof-relevant map from the entry external obstruction through the basin
surfaces to source internality, not merely reuse external/oracle vocabulary,
escape prefix membership, or plain-tail membership.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_mediator_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINMEDIATORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINMEDIATORBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the exact
two-surface terminal-basin mediator set, the mixed external/oracle attachment
leg, the mixed escape-prefix and plain-tail attachment legs, the fact that
basin segment support misses both residuals, and the absence of exact
segment/namespace overlap between the mediators and `not_source_internal`.
