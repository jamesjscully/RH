#!/usr/bin/env python3
r"""No-go for promoting doc608 to a reused source-event grammar.

Doc 608 replaces doc606 substring priority with typed source events. This
witness tests the next stronger interpretation: every event rule should be
reused by at least two boundary surfaces, so exact tail literals cannot act as
a disguised row lookup.

That strengthening fails. Of the 70 doc608 rule ids, only four are reused, and
all four are namespace rules. The remaining 66 rules are singleton exact-tail,
obstruction-tail, or named-event rules.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_reuse_no_go
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_contract import (
    ACTION_IN_CONTRACTION_SURFACE,
    EXPECTED_WITNESS as DOC608_WITNESS,
    KILLTYPEDEVENTACTION,
    NAMESPACE_CLASS_RULES,
    RULE_LITERAL_COUNT,
    SOURCE_EVENT_DECISIONS,
    SOURCE_EVENTS,
    load_map,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMTYPEDEVENTREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
REUSE_THRESHOLD = 2

failures: list[str] = []

RuleCounter = Counter[str]
ClassCounter = Counter[str]


def rule_counts() -> RuleCounter:
    return Counter(decision["rule_id"] for decision in SOURCE_EVENT_DECISIONS.values())


RULE_COUNTS = rule_counts()
REUSED_RULES = frozenset(rule for rule, count in RULE_COUNTS.items() if count >= REUSE_THRESHOLD)
SINGLETON_RULES = frozenset(rule for rule, count in RULE_COUNTS.items() if count == 1)
SINGLETON_DECISIONS = {
    surface: decision
    for surface, decision in SOURCE_EVENT_DECISIONS.items()
    if decision["rule_id"] in SINGLETON_RULES
}
REUSED_DECISIONS = {
    surface: decision
    for surface, decision in SOURCE_EVENT_DECISIONS.items()
    if decision["rule_id"] in REUSED_RULES
}

CLASS_COUNTS = Counter(decision["winning_class"] for decision in SOURCE_EVENT_DECISIONS.values())
SINGLETON_CLASS_COUNTS = Counter(decision["winning_class"] for decision in SINGLETON_DECISIONS.values())
REUSED_CLASS_COUNTS = Counter(decision["winning_class"] for decision in REUSED_DECISIONS.values())


def event_kind_class_counts() -> dict[str, ClassCounter]:
    by_kind: dict[str, ClassCounter] = defaultdict(Counter)
    for surface, decision in SOURCE_EVENT_DECISIONS.items():
        event = SOURCE_EVENTS[surface]
        by_kind[event["event_kind"]][decision["winning_class"]] += 1
    return dict(by_kind)


def segment_class_counts() -> dict[str, ClassCounter]:
    by_segment: dict[str, ClassCounter] = defaultdict(Counter)
    for surface, decision in SOURCE_EVENT_DECISIONS.items():
        event = SOURCE_EVENTS[surface]
        for segment in event["segments"]:
            by_segment[segment][decision["winning_class"]] += 1
    return dict(by_segment)


EVENT_KIND_CLASS_COUNTS = event_kind_class_counts()
AMBIGUOUS_EVENT_KINDS = {
    kind: counts for kind, counts in EVENT_KIND_CLASS_COUNTS.items() if len(counts) > 1
}
SEGMENT_CLASS_COUNTS = segment_class_counts()
AMBIGUOUS_SEGMENTS = {
    segment: counts for segment, counts in SEGMENT_CLASS_COUNTS.items() if len(counts) > 1
}


def suffix_class_counts(suffix: str) -> ClassCounter:
    counts: ClassCounter = Counter()
    for surface, decision in SOURCE_EVENT_DECISIONS.items():
        if SOURCE_EVENTS[surface]["tail"].endswith(suffix):
            counts[decision["winning_class"]] += 1
    return counts


ENTRY_MISSING_SUFFIX_COUNTS = suffix_class_counts("entry_missing")
STATE_ENTRY_SUFFIX_COUNTS = suffix_class_counts("state_entry")
MISSING_SUFFIX_COUNTS = suffix_class_counts("missing")


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
        data["frontier"].get("current_doc", 0) >= 608
        and DOC608_WITNESS in data.get("witnesses", {})
        and KILLTYPEDEVENTACTION in accepted,
        f"frontier_doc={data['frontier']['current_doc']} doc608_witness={DOC608_WITNESS in data.get('witnesses', {})}",
    )
    gate(
        f"{PREFIX}2",
        len(SOURCE_EVENT_DECISIONS) == 106
        and RULE_LITERAL_COUNT == 70
        and len(RULE_COUNTS) == 70,
        f"decisions={len(SOURCE_EVENT_DECISIONS)} rule_literals={RULE_LITERAL_COUNT} used_rules={len(RULE_COUNTS)}",
    )
    gate(
        f"{PREFIX}3",
        len(REUSED_RULES) == 4
        and REUSED_RULES == frozenset(f"namespace:{namespace}" for namespace in NAMESPACE_CLASS_RULES),
        f"reused_rules={sorted(REUSED_RULES)}",
    )
    gate(
        f"{PREFIX}4",
        len(SINGLETON_RULES) == 66
        and len(SINGLETON_DECISIONS) == 66,
        f"singleton_rules={len(SINGLETON_RULES)} singleton_decisions={len(SINGLETON_DECISIONS)}",
    )
    gate(
        f"{PREFIX}5",
        set(SINGLETON_CLASS_COUNTS) == set(CLASS_COUNTS)
        and len(REUSED_DECISIONS) == 40
        and len(SOURCE_EVENT_DECISIONS) - len(REUSED_DECISIONS) == 66,
        f"reused_decisions={len(REUSED_DECISIONS)} singleton_classes={len(SINGLETON_CLASS_COUNTS)}",
    )
    gate(
        f"{PREFIX}6",
        ACTION_IN_CONTRACTION_SURFACE in SINGLETON_DECISIONS
        and SINGLETON_DECISIONS[ACTION_IN_CONTRACTION_SURFACE]["rule_id"]
        == "event_kind:missing_terminal_basin_certificate",
        "doc607 hard repair is itself a singleton event-kind rule",
    )
    gate(
        f"{PREFIX}7",
        len(EVENT_KIND_CLASS_COUNTS["entry_missing_tail"]) == 14
        and len(EVENT_KIND_CLASS_COUNTS["plain_tail"]) == 14
        and len(EVENT_KIND_CLASS_COUNTS["obstruction_namespace"]) == 4
        and len(AMBIGUOUS_SEGMENTS) == 37,
        "coarse event-kind/segment repairs are class-ambiguous",
    )
    gate(
        f"{PREFIX}8",
        len(ENTRY_MISSING_SUFFIX_COUNTS) == 14
        and len(STATE_ENTRY_SUFFIX_COUNTS) == 4
        and len(MISSING_SUFFIX_COUNTS) == 14,
        "suffix-family repairs still merge incompatible classes",
    )
    gate(
        f"{PREFIX}9",
        len(SINGLETON_RULES) > len(REUSED_RULES) * 10
        and len(SINGLETON_DECISIONS) > len(REUSED_DECISIONS),
        "singleton-tail lookup leakage dominates the doc608 rule system",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}9 ALL PASS: doc608 fails reused-event promotion")
    print(
        "VERDICT: doc608 is a valid exact typed-event classifier, but its "
        "current rule system cannot be promoted to a reusable source-event "
        "grammar without losing 66 of 106 decisions. The obstruction is "
        "singleton-tail lookup leakage."
    )


if __name__ == "__main__":
    main()
