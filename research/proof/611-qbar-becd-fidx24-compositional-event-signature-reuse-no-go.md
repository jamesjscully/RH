# 611 - Qbar_BECD FIdx24 Compositional Event Signature Reuse No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-610 compositional event-signature classifier cannot be promoted to a
reused whole-signature grammar by requiring every complete signature to occur
on at least two boundary surfaces.

The named mechanism is **singleton-signature lookup leakage**.

## Setup

Doc 610 repairs doc 609 at the primitive level. It forbids exact tail names,
full-subject literals, doc-606 substring tokens, and doc-608 singleton rule ids
as primitive evidence. Every primitive feature used in a signature has support
at least two across the 106 boundary surfaces.

This no-go tests the stricter structural reading that the complete composed
signature should also be reused by at least two surfaces. Under that reading,
the composed signature itself cannot act as a hidden row lookup.

## Obstruction

The doc-610 classifier has 106 decisions and 98 class-pure signatures. Of those
98 signatures, 93 are singleton whole signatures. Only five signatures are
reused, covering 13 of the 106 decisions.

The bucket-size profile is:

```text
size 1: 93 signatures
size 2: 3 signatures
size 3: 1 signature
size 4: 1 signature
```

The singleton signatures span all 17 doc-610 classes. The reused signatures
cover only three classes:

```text
boundary_contextual_surrogate
source_constraint_invariant
terminal_basin_entry
```

The doc-607 hard repair is still a singleton whole signature, even though doc
610 classifies it without exact-tail or singleton-primitive evidence.

## Consequence

Doc 610 remains a valid compositional classifier at the primitive-feature
level. What doc 611 kills is the stronger claim that doc 610 has already found
a reused categorical signature grammar.

The next constructive frontier must either add a genuine categorical
event-composition law behind the signatures, or the negative thread must prove
that every such law collapses classes, reintroduces name lookup, retunes stems,
or changes the doc-602 anchor composition.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reuse_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPEVENTSIGREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPEVENTSIGREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, 106 decisions, 184 reused primitive
features, 98 class-pure signatures, 93 singleton signatures, five reused
signatures, the bucket-size profile, singleton coverage across all 17 classes,
the singleton status of the doc-607 hard repair, and the dominance of
singleton-signature lookup leakage.
