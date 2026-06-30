# 634 - Qbar_BECD FIdx24 Terminal-Basin-Internal-Composition-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by treating the
visible terminal-basin `escape/plain_tail/basin` overlap as the missing
internal composition law.

The named mechanism is **terminal-basin internal-composition overproduction**.

## Setup

Doc 633 leaves the sharpest positive residue so far:

```text
boundary_externality -> terminal_basin_entry -> source_internality
```

with `terminal_basin_entry` the unique common class neighbor. To turn that
adjacency into a bridge, the terminal-basin class would need an internal
composition law selecting the mediator paths

```text
external_basin or oracle_basin
  -> basin_not_absorbing or basin_not_extensional
```

The natural visible kernel for such a law is:

```text
boundary=escape, event_kind=plain_tail, segment=basin, stem=basin
```

## Obstruction

That kernel is real, but it is not a constructed bridge morphism.

On the four target paths, every path has exactly the same pair-kernel:

```text
external_basin -> basin_not_absorbing     escape/plain_tail/basin
external_basin -> basin_not_extensional   escape/plain_tail/basin
oracle_basin   -> basin_not_absorbing     escape/plain_tail/basin
oracle_basin   -> basin_not_extensional   escape/plain_tail/basin
```

The same kernel appears on 58 ordered pairs inside the terminal-basin class.
Thus it is a broad overlap relation, not a bridge selector.

It also cannot distinguish the two right endpoints:

```text
basin_not_absorbing and basin_not_extensional
  have identical doc610 compositional signatures
```

The left endpoints differ only by `external` versus `oracle`, whose global
support is mixed-class. If the third not-attachment is included,
`entry_trace_not_replay_stable` loses the basin/plain-tail composition kernel
and leaves only the shared escape boundary. Thus the alleged composition law
either overproduces the four basin paths or fails to cover the full not-side
attachment.

## Consequence

The current doc610 source-event algebra supplies a terminal-basin overlap
relation, not an internal category law. A surviving route must add a genuine
composition/boundary map that makes one terminal-basin path canonical or
explains why all four paths compose to the same proof-relevant morphism. The
visible `basin` kernel alone is too broad, cannot distinguish the right
endpoint, and imports the already mixed external/oracle and not attachments.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_internal_composition_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASININTCOMPOSITIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASININTCOMPOSITIONBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
unique terminal-basin class hub, the identical pair-kernel on the four target
paths, the 58 ordered terminal-basin pairs with the same kernel, the identical
right-endpoint signatures, the mixed global external/oracle support, and the
split created by including the third not-attachment.
