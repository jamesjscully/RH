#!/usr/bin/env python3
r"""No-go for promoting doc610 to a reused signature grammar.

Doc 610 repairs doc 609 at the primitive level: every primitive feature used
in a compositional signature is reused by at least two boundary surfaces. This
witness tests the next stronger reading: every whole signature should also be
reused by at least two boundary surfaces.

That strengthening fails. The doc-610 signature system has 98 signatures for
106 decisions, and 93 of those signatures are singleton signatures.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    ACTION_IN_CONTRACTION_SURFACE,
    AMBIGUOUS_SIGNATURES,
    COMPOSITIONAL_SIGNATURE_DECISIONS,
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    REUSABLE_PRIMITIVE_FEATURES,
    SIGNATURE_BUCKETS,
    load_map,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPEVENTSIGREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
REUSE_THRESHOLD = 2

failures: list[str] = []

SIGNATURE_COUNTS = Counter({signature: len(surfaces) for signature, surfaces in SIGNATURE_BUCKETS.items()})
SINGLETON_SIGNATURES = {
    signature: surfaces[0] for signature, surfaces in SIGNATURE_BUCKETS.items() if len(surfaces) == 1
}
REUSED_SIGNATURES = {
    signature: tuple(surfaces)
    for signature, surfaces in SIGNATURE_BUCKETS.items()
    if len(surfaces) >= REUSE_THRESHOLD
}
SINGLETON_DECISIONS = {
    surface: COMPOSITIONAL_SIGNATURE_DECISIONS[surface] for surface in SINGLETON_SIGNATURES.values()
}
REUSED_DECISIONS = {
    surface: COMPOSITIONAL_SIGNATURE_DECISIONS[surface]
    for surfaces in REUSED_SIGNATURES.values()
    for surface in surfaces
}
SINGLETON_CLASS_COUNTS = Counter(decision["winning_class"] for decision in SINGLETON_DECISIONS.values())
REUSED_CLASS_COUNTS = Counter(decision["winning_class"] for decision in REUSED_DECISIONS.values())
BUCKET_SIZE_COUNTS = Counter(SIGNATURE_COUNTS.values())


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc", 0) >= 610
        and DOC610_WITNESS in data.get("witnesses", {})
        and KILLCOMPEVENTSIGACTION in accepted,
        f"frontier_doc={data['frontier']['current_doc']} doc610_witness={DOC610_WITNESS in data.get('witnesses', {})}",
    )
    gate(
        f"{PREFIX}2",
        len(COMPOSITIONAL_SIGNATURE_DECISIONS) == 106
        and len(REUSABLE_PRIMITIVE_FEATURES) == 184
        and len(SIGNATURE_BUCKETS) == 98
        and not AMBIGUOUS_SIGNATURES,
        f"decisions={len(COMPOSITIONAL_SIGNATURE_DECISIONS)} primitives={len(REUSABLE_PRIMITIVE_FEATURES)} signatures={len(SIGNATURE_BUCKETS)}",
    )
    gate(
        f"{PREFIX}3",
        len(SINGLETON_SIGNATURES) == 93
        and len(REUSED_SIGNATURES) == 5
        and len(SINGLETON_DECISIONS) == 93
        and len(REUSED_DECISIONS) == 13,
        f"singleton_signatures={len(SINGLETON_SIGNATURES)} reused_signatures={len(REUSED_SIGNATURES)}",
    )
    gate(
        f"{PREFIX}4",
        BUCKET_SIZE_COUNTS == Counter({1: 93, 2: 3, 3: 1, 4: 1}),
        f"bucket_sizes={dict(sorted(BUCKET_SIZE_COUNTS.items()))}",
    )
    gate(
        f"{PREFIX}5",
        len(SINGLETON_CLASS_COUNTS) == 17
        and len(REUSED_CLASS_COUNTS) == 3
        and set(SINGLETON_CLASS_COUNTS) >= set(REUSED_CLASS_COUNTS),
        f"singleton_classes={len(SINGLETON_CLASS_COUNTS)} reused_classes={len(REUSED_CLASS_COUNTS)}",
    )
    gate(
        f"{PREFIX}6",
        ACTION_IN_CONTRACTION_SURFACE in SINGLETON_DECISIONS
        and SINGLETON_DECISIONS[ACTION_IN_CONTRACTION_SURFACE]["winning_class"] == "action_semantics",
        "doc607 hard repair is still a singleton whole signature",
    )
    gate(
        f"{PREFIX}7",
        all(
            len({COMPOSITIONAL_SIGNATURE_DECISIONS[surface]["winning_class"] for surface in surfaces}) == 1
            for surfaces in REUSED_SIGNATURES.values()
        )
        and set(REUSED_CLASS_COUNTS) == {
            "boundary_contextual_surrogate",
            "source_constraint_invariant",
            "terminal_basin_entry",
        },
        "the few reused signatures are class-pure but cover only three classes",
    )
    gate(
        f"{PREFIX}8",
        len(SINGLETON_SIGNATURES) > len(REUSED_SIGNATURES) * 10
        and len(SINGLETON_DECISIONS) > len(REUSED_DECISIONS) * 7,
        "singleton-signature lookup leakage dominates whole-signature reuse",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: doc610 fails reused-signature promotion")
    print(
        "VERDICT: doc610 repairs reuse at the primitive-feature level, but "
        "its whole signatures cannot be promoted to a reused signature grammar. "
        "The obstruction is singleton-signature lookup leakage."
    )


if __name__ == "__main__":
    main()
