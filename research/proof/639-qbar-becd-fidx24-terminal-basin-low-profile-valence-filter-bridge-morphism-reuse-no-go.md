# 639 - Qbar_BECD FIdx24 Terminal-Basin-Low-Profile-Valence-Filter-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by using a
good-vs-bad semantic valence filter inside the low graph-profile
terminal-basin component to select `external_basin` and `oracle_basin`.

The named mechanism is **terminal-basin low-profile valence-filter selector
collapse**.

## Setup

Docs 637 and 638 isolate the surviving low-profile component:

```text
(out,in,total,undirected,eccentricity,distance_sum) = (4,4,8,4,2,14)
```

It contains exactly two desired left endpoints:

```text
external_basin
oracle_basin
```

and four bad-looking labels:

```text
branch_spawning_basin
noncanonical_basin
proof_irrelevant_basin
retuned_basin
```

After suffix, segment, and tail arity fail, the next tempting repair is
semantic valence: keep the apparently non-defect basin labels and exclude
the defect/failure vocabulary.

## Obstruction

The defect-token support is exactly the four bad labels:

```text
branch
spawning
noncanonical
proof
irrelevant
retuned
```

Therefore the defect-token complement does recover:

```text
external_basin
oracle_basin
```

But this is only a lexical complement. It is extensionally identical to the
attachment-token selector:

```text
external / oracle
```

The neutral terminal token still gives the whole component:

```text
basin:
  all six low-profile surfaces
```

and the structural features already checked in doc 638 still do not select
the targets:

```text
boundary=escape
event_kind=plain_tail
segment=basin
suffix=basin
tail_length=2 or 3
```

The exact non-basin token profile inside the six surfaces is one lexical
bucket per surface. The only exact token selector for the two targets is
`external/oracle`; the good-vs-bad filter is just its negative-vocabulary
dual.

## Consequence

Valence filtering does not add terminal-basin structure. It only says that
the two target labels are not the known defect labels, or equivalently that
they carry the `external/oracle` attachment tokens. A surviving route must
construct a positive boundary map, composition law, degree map, Rosati datum,
or control-death mechanism whose action separates the low-profile endpoints
from bad labels without using attachment-token lookup or defect-vocabulary
exclusion.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_low_profile_valence_filter_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILEVALENCEFILTERBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINLOWPROFILEVALENCEFILTERBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the
six-surface low graph profile, defect-token support, equality between
defect-token complement and `external/oracle` attachment-token selection,
failure of neutral terminal/shape features, and the absence of a
non-lexical low-profile selector.
