# 631 - Qbar_BECD FIdx24 Boundary-Transducer-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by reusing the
visible boundary axes as an entry-to-escape bridge transducer.

The named mechanism is **boundary-transducer selector collapse**.

## Setup

Docs 629 and 630 kill direct residual-pair selection and semantic-polarity
closure. The next plausible categorical repair is a boundary transducer:

```text
entry obstruction  --->  escape plain-tail / terminal-basin failure
```

This would be proof-relevant only if entry/escape, obstruction/plain-tail, or
terminal-basin structure supplies reusable class-pure support for the two
residuals:

```text
entry_boundary:obstruction:external_or_oracle
escape_boundary:..._not_source_internal
```

## Obstruction

The visible boundary-kind closures are broad mixed-class partitions:

```text
entry boundary:
  62 surfaces across 14 classes

escape boundary:
  44 surfaces across 16 classes
```

The event-kind closures are also mixed:

```text
obstruction_namespace:
  7 surfaces across dependency_repair_nogo, boundary_contextual_surrogate,
  finite_index_budget, and boundary_externality

plain_tail:
  37 surfaces across 14 classes
```

The terminal-basin-looking escape prefix is reused, but it is not class-pure:

```text
escape center/terminal prefix:
  43 surfaces across 16 classes
```

The `basin` segment support is closer to a coherent terminal-basin family:

```text
basin segment:
  terminal_basin_entry=10, action_semantics=1
```

but it does not contain either residual surface as a bridge. The
`terminal`/`obstruction` segment evidence is only the singleton missing
terminal-basin certificate action.

Thus the current doc610 source-event data has no visible boundary transducer
closure that is reused, class-pure, and pair-containing. Entry/escape and
obstruction/plain-tail axes are too broad; terminal-basin segment support is
not the residual bridge.

## Consequence

The surviving route must construct an actual boundary morphism with
proof-relevant endpoint evidence. It cannot be recovered from existing
boundary kind, event kind, escape-prefix, or terminal-basin segment reuse
without adding a selector, changing labels or anchors, merging classes, or
retuning the source-event grammar.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_boundary_transducer_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBNDRYTRANSDUCERBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMBNDRYTRANSDUCERBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the two doc-614 singleton residuals,
the mixed entry/escape boundary-kind profiles, the mixed obstruction/plain-tail
event-kind profiles, the mixed escape terminal-prefix profile, the fact that
`basin` segment support misses the residual pair, and the singleton status of
`terminal`/`obstruction` segment evidence.
