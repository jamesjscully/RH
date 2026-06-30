# 635 - Qbar_BECD FIdx24 Terminal-Basin-Kernel-Quotient-Bridge Morphism-Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-614 singleton residual obstruction cannot be repaired by quotienting
all terminal-basin paths with the visible `escape/plain_tail/basin` kernel and
declaring the four target paths to be the same morphism.

The named mechanism is **terminal-basin kernel-quotient collapse**.

## Setup

Doc 634 kills the visible kernel as a selective composition law. The next
escape is quotienting: perhaps all paths with that kernel represent the same
proof-relevant morphism.

The target paths are:

```text
external_basin -> basin_not_absorbing
external_basin -> basin_not_extensional
oracle_basin   -> basin_not_absorbing
oracle_basin   -> basin_not_extensional
```

all with kernel:

```text
boundary=escape, event_kind=plain_tail, segment=basin, stem=basin
```

## Obstruction

The kernel relation has 58 ordered pairs inside `terminal_basin_entry`. The
four target pairs are only a small subfamily; the other 54 pairs are
non-target pairs with the same visible kernel.

As an undirected quotient relation, the kernel gives one connected component
on ten terminal-basin surfaces. That component contains the four target
endpoints:

```text
external_basin
oracle_basin
basin_not_absorbing
basin_not_extensional
```

but it also contains six explicitly non-proof-relevant basin labels:

```text
branch_spawning_basin
no_basin_certificate
noncanonical_basin
proof_irrelevant_basin
retuned_basin
unbounded_basin_search
```

Thus quotienting by the visible kernel identifies the desired mediator paths
with retuned, noncanonical, proof-irrelevant, unbounded, no-certificate, and
branch-spawning basin surfaces.

The quotient component is class-pure only because it erases terminal-basin
distinctions. Its endpoint degree profile is:

```text
total quotient degree 8:  6 surfaces
total quotient degree 16: 2 surfaces
total quotient degree 18: 2 surfaces
```

That degree profile does not single out the target bridge; the highest-degree
members include failure/search labels.

## Consequence

The route cannot escape doc634 by declaring the four target paths equal under
the visible kernel. The quotient is too coarse: it collapses the target
mediators together with labels whose content is precisely noncanonicality,
retuning, proof irrelevance, unbounded search, missing certificate, and branch
spawning. A surviving route must construct a finer composition or boundary
map that separates the proof-relevant path from those terminal-basin failure
labels.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_terminal_basin_kernel_quotient_bridge_morphism_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINKERNELQUOTIENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTERMBASINKERNELQUOTIENTBRIDGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR9 ALL PASS
```

The witness verifies doc-610 acceptance, the doc-614 residual pair, the 58
ordered kernel pairs, the 54 non-target kernel pairs, the single ten-surface
kernel component, containment of the four target endpoints and six
non-proof-relevant basin labels in that component, the quotient degree
profile, and the imported selector/failure vocabulary.
