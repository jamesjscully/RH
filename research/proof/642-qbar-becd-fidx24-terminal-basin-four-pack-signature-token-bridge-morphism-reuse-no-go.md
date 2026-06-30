# 642 - Qbar_BECD FIdx24 Terminal-Basin-Four-Pack-Signature-Token-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by promoting
the accepted doc-610 compositional signatures to the missing bridge morphism
inside the four-pack

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

The named mechanism is **terminal-basin four-pack signature-token selector
collapse**.

## Setup

Doc 641 shows that graph profile times structural tail shape leaves the left
target pair in the four-element block:

```text
external_basin
oracle_basin
noncanonical_basin
retuned_basin
```

The next tempting repair is to reuse the accepted doc-610 compositional
signatures. Those signatures do distinguish `external_basin` and
`oracle_basin` from `noncanonical_basin` and `retuned_basin`, because
`external` and `oracle` are globally reused primitive signature features.

## Obstruction

The four surfaces share the same structural signature skeleton:

```text
boundary=escape
event_kind=plain_tail
segment=basin
stem=basin
suffix=basin
```

The target signatures differ only by attachment-token features:

```text
external_basin:
  segment=external
  stem=external

oracle_basin:
  segment=oracle
  stem=oracle
```

The bad two-pack has no matching reusable bad-token features in the doc-610
signature:

```text
noncanonical_basin:
  structural skeleton only

retuned_basin:
  structural skeleton only
```

This asymmetry is a token-support artifact:

```text
segment=external: support 4
segment=oracle:   support 4
segment=noncanonical: support 1
segment=retuned:      support 1
```

After removing the `external/oracle` attachment-token features from the
doc-610 signatures, all four surfaces collapse to the same skeleton. No
conjunction of non-attachment signature features selects
`external_basin/oracle_basin`.

## Consequence

Doc-610 signatures do not provide the missing morphism-level separator. They
can select the target pair only by using the already-isolated residual
attachment tokens. The four-pack still needs a genuinely new operation:
boundary map, composition law, endpoint-degree map, DD.4 boundary operation,
graph/composition datum, Rosati datum, or control-death mechanism.

Equivalently: the surviving object must split

```text
external_basin / oracle_basin
```

from

```text
noncanonical_basin / retuned_basin
```

without relying on global reuse of the words `external` and `oracle`.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_four_pack_signature_token_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKSIGTOKENBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINFOURPACKSIGTOKENBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
doc-641 four-pack, attachment-feature support, normalized signature collapse,
absence of non-attachment signature conjunction selectors, the primitive
support asymmetry between `external/oracle` and `noncanonical/retuned`, and
collapse of all non-basin primitive features to the same structural skeleton.
