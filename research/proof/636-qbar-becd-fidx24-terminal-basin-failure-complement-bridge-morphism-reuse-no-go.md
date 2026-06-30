# 636 - Qbar_BECD FIdx24 Terminal-Basin-Failure-Complement-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by taking the
doc-635 kernel quotient component and removing the explicitly bad
terminal-basin labels.

The named mechanism is **terminal-basin failure-complement selector collapse**.

## Setup

Doc 635 shows that the `escape/plain_tail/basin` quotient component is too
coarse. It contains four target endpoints:

```text
external_basin
oracle_basin
basin_not_absorbing
basin_not_extensional
```

and six explicit failure labels:

```text
branch_spawning_basin
no_basin_certificate
noncanonical_basin
proof_irrelevant_basin
retuned_basin
unbounded_basin_search
```

The next escape is to remove the failure labels and keep the four targets.

## Obstruction

The failure-label complement does recover the four target endpoints. But it
does so only as a negative selector:

```text
component minus {branch, no, noncanonical, proof_irrelevant, retuned, unbounded}
  = {external_basin, oracle_basin, basin_not_absorbing, basin_not_extensional}
```

The target endpoints share no positive doc610 compositional feature beyond
the kernel that the bad labels also share:

```text
common target signature:
  boundary=escape, event_kind=plain_tail, segment=basin, stem=basin

common bad-label signature:
  boundary=escape, event_kind=plain_tail, segment=basin, stem=basin

common full component signature:
  boundary=escape, event_kind=plain_tail, segment=basin, stem=basin
```

No conjunction of structural kernel features selects the target endpoints.
The only positive exact selector inside the component is the disjunction of
residual attachment tokens:

```text
external/oracle/not
```

That is not an internal terminal-basin composition law. It is precisely the
external attachment plus the not attachment already isolated in docs 633-635.

## Consequence

The failure-complement route is useful as a diagnostic: it shows exactly which
terminal-basin failure labels must be separated. But it does not construct the
missing morphism. A surviving route must supply positive proof-relevant
structure that distinguishes the target endpoints from the failure labels,
not merely exclude labels whose text already says noncanonical, retuned,
proof-irrelevant, unbounded, no certificate, or branch spawning.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_failure_complement_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFAILCOMPLEMENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFAILCOMPLEMENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
ten-surface kernel component split into four targets and six bad labels, the
failure-complement equality, equality of target/bad/full common signatures,
absence of structural-feature selectors, and the fallback to
`external/oracle/not` attachment tokens.
