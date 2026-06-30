# 607 - Qbar_BECD FIdx24 Priority Token Grammar No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The exact doc-606 terminal-basin boundary kill-frontier facet-route edge
priority decisions cannot be preserved by a finite source-native typed token
grammar.

The named mechanism is **substring-token priority collapse**.

## Setup

Doc 606 makes the priority order explicit: 106 surface witnesses, 57 ambiguous
token-overlap cases, and 18 semantic classes. However, its recognizer is still
based on raw substring membership inside subject strings.

The source-native replacement tested here is the strict finite grammar whose
tokens are colon namespaces, full subject tails, colon parts, underscore
segments, and contiguous underscore ngrams. This grammar preserves token
boundaries and does not admit arbitrary substring hits.

## Obstruction

Under that grammar, three doc-606 winning decisions have no typed winning
token:

```text
multiple_fixedpoints -> fixedpoint_replay / fixedpoint
overlapping_incompatible_basins -> terminal_basin_entry / basin
missing_obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate -> action_semantics / action
```

Two shadow decisions are also substring-only:

```text
invariant:original_dd4_res1_nonboundary -> boundary_shape / boundary
overlapping_incompatible_basins -> boundary_shape / overlap
```

Plural stemming repairs the first two winning failures, but it still leaves the
hard failure: `action` appears only inside `contraction`. Admitting that match
requires returning to substring matching, which is exactly the non-source-native
escape doc 607 rules out.

## Consequence

Doc 606 remains a useful narrowing artifact, but it is killed as a
source-native token grammar. The next constructive frontier must rebuild the
classification from typed source events rather than preserve the exact
substring-priority decisions.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_token_grammar_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPRIOGRAMNOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPRIOGRAMNOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies the 106 doc-606 decisions, 57 ambiguous decisions, the
706-token strict typed lexicon, three untyped winning failures, two untyped
shadow failures, eight substring-only matches, and the failure of plural
stemming to repair the `action`-inside-`contraction` case.
