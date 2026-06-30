# 612 - Qbar_BECD FIdx24 Compositional Event Reused Class-State No-Go

## Status

No-go theorem with a named mechanism. Layer I only; this is not an RH result.

## Claim

The doc-610 compositional event-signature classifier cannot be promoted to a
total categorical class-state factorization merely by requiring each decision
to pass through some reused class-pure sub-signature.

The named mechanism is **residual class-state leakage**.

## Setup

Doc 611 kills reuse of whole doc-610 signatures: 93 of the 98 whole signatures
are singleton. The next salvage is weaker and more categorical. Instead of
requiring the whole signature to be reused, require a decision to factor through
a reused intermediate class state: a subset of the doc-610 primitive features
whose containment support has size at least two and lies entirely inside one
doc-610 class.

This is a genuine improvement over whole-signature reuse. It asks whether the
classification can stop at a reused class-pure state before the remaining
signature refinements become singleton.

## Obstruction

The factorization is useful but not total.

```text
85 decisions have a reused class-pure containment state.
21 decisions have no reused class-pure containment state.
```

The size/support profile is:

```text
no reused class state: 21
1 feature, support 2:  19
1 feature, support 6:   6
1 feature, support 8:  16
1 feature, support 11: 11
1 feature, support 13: 13
2 features, support 2: 16
2 features, support 3:  1
2 features, support 11: 3
```

The 21 missing cases span nine classes:

```text
dependency_repair_nogo:        4
terminal_basin_entry:          4
boundary_contextual_surrogate: 4
finite_index_budget:           3
boundary_shape:                2
source_constraint_invariant:   1
source_internality:            1
boundary_externality:          1
action_semantics:              1
```

The doc-607 hard repair remains in the missing set: it has no reused
class-pure containment state, even though doc 610 classifies it without
exact-tail or singleton-primitive evidence.

## Consequence

Doc 612 does not refute doc 610. It sharpens the next target. A categorical
event-composition law cannot be just "find any reused class-pure sub-state";
that works for 85 decisions and fails for the residual 21.

The next constructive frontier should focus on those 21 missing cases. A real
categorical repair must add source-native morphisms or quotient laws that turn
the residual cases into class-pure reused states without exact-tail lookup,
stem retuning, class collapse, or doc-602 anchor changes.

## Witness

Run:

```bash
python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go
```

Expected pass line:

```text
CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPEVENTCLASSSTATENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR1-CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPEVENTCLASSSTATENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR8 ALL PASS
```

The witness verifies doc-610 acceptance, the 106 decisions, 184 reused
primitive features, 98 class-pure signatures, the 85/21 reused-class-state
split, the exact size/support profile, the nine-class residual obstruction,
the doc-607 hard repair in the missing set, and the positive residue of reused
class-pure states.
