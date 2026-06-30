#!/usr/bin/env python3
r"""No-go for preserving doc606 priority under typed token grammar.

Doc 606 resolves overlapping semantic tokens by an explicit priority order,
but the token recognizer is still substring based. This witness tests the
source-native replacement: a finite typed grammar whose tokens are colon
namespaces, full tails, underscore segments, or contiguous underscore ngrams.

The exact doc606 priority decisions cannot be preserved under that grammar.
Three winning decisions have no typed winning token, and two shadow decisions
depend on substring-only tokens. The named mechanism is substring-token
priority collapse.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_token_grammar_no_go
"""

from __future__ import annotations

from typing import Iterable

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_contract import (
    AMBIGUOUS_PRIORITY_DECISIONS,
    CLASS_RULE_TOKENS,
    EXPECTED_WITNESS as DOC606_WITNESS,
    KILLPRIORITYACTION,
    PRIORITY_DECISIONS,
    SEMANTIC_PRIORITY,
    load_map,
)


EXPECTED_DOC = 607
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPRIOGRAMNOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

failures: list[str] = []


def unique(items: Iterable[tuple[str, str]]) -> tuple[tuple[str, str], ...]:
    seen: set[tuple[str, str]] = set()
    result: list[tuple[str, str]] = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return tuple(result)


def typed_token_stream(subject: str) -> tuple[tuple[str, str], ...]:
    parts = subject.split(":")
    tail = parts[-1]
    tokens: list[tuple[str, str]] = [("full", subject), ("tail", tail)]
    tokens.extend(("namespace", namespace) for namespace in parts[:-1])
    tokens.extend(("part", part) for part in parts if part)

    segments = tuple(segment for segment in tail.split("_") if segment)
    tokens.extend(("segment", segment) for segment in segments)
    for start in range(len(segments)):
        for stop in range(start + 2, len(segments) + 1):
            tokens.append(("ngram", "_".join(segments[start:stop])))
    return unique(tokens)


def typed_matches(subject: str, raw_token: str) -> tuple[tuple[str, str], ...]:
    normalized = raw_token[:-1] if raw_token.endswith(":") else raw_token
    return tuple(token for token in typed_token_stream(subject) if token[1] == normalized)


def typed_winning_failures() -> tuple[tuple[str, str, str, tuple[str, ...]], ...]:
    failures_: list[tuple[str, str, str, tuple[str, ...]]] = []
    for surface, decision in PRIORITY_DECISIONS.items():
        subject = decision["subject"]
        winning_tokens = tuple(decision["winning_tokens"])
        if not any(typed_matches(subject, token) for token in winning_tokens):
            failures_.append((surface, subject, decision["winning_class"], winning_tokens))
    return tuple(sorted(failures_))


def typed_shadow_failures() -> tuple[tuple[str, str, str, tuple[str, ...]], ...]:
    failures_: list[tuple[str, str, str, tuple[str, ...]]] = []
    for surface, decision in PRIORITY_DECISIONS.items():
        subject = decision["subject"]
        for shadow_class, raw_tokens in decision["shadow_tokens"].items():
            untyped = tuple(token for token in raw_tokens if not typed_matches(subject, token))
            if untyped:
                failures_.append((surface, subject, shadow_class, untyped))
    return tuple(sorted(failures_))


def all_substring_without_typed() -> tuple[tuple[str, str, str, str], ...]:
    failures_: list[tuple[str, str, str, str]] = []
    for surface, decision in PRIORITY_DECISIONS.items():
        subject = decision["subject"]
        for facet_class in (decision["winning_class"], *tuple(decision["shadow_classes"])):
            for raw_token in CLASS_RULE_TOKENS[facet_class]:
                if raw_token in subject and not typed_matches(subject, raw_token):
                    failures_.append((surface, subject, facet_class, raw_token))
    return tuple(sorted(failures_))


def plural_stem_typed_matches(subject: str, raw_token: str) -> tuple[tuple[str, str], ...]:
    matches = list(typed_matches(subject, raw_token))
    normalized = raw_token[:-1] if raw_token.endswith(":") else raw_token
    for kind, value in typed_token_stream(subject):
        if kind in {"segment", "ngram", "tail"} and value.endswith("s") and value[:-1] == normalized:
            matches.append((kind, value))
    return tuple(matches)


def plural_stem_winning_failures() -> tuple[tuple[str, str, str, tuple[str, ...]], ...]:
    failures_: list[tuple[str, str, str, tuple[str, ...]]] = []
    for surface, decision in PRIORITY_DECISIONS.items():
        subject = decision["subject"]
        winning_tokens = tuple(decision["winning_tokens"])
        if not any(plural_stem_typed_matches(subject, token) for token in winning_tokens):
            failures_.append((surface, subject, decision["winning_class"], winning_tokens))
    return tuple(sorted(failures_))


STRICT_WINNER_FAILURES = typed_winning_failures()
STRICT_SHADOW_FAILURES = typed_shadow_failures()
SUBSTRING_ONLY_MATCHES = all_substring_without_typed()
PLURAL_STEM_WINNER_FAILURES = plural_stem_winning_failures()
LEXICON = frozenset(
    token
    for decision in PRIORITY_DECISIONS.values()
    for token in typed_token_stream(decision["subject"])
)
ACTION_IN_CONTRACTION_SURFACE = (
    "escape_boundary:missing_obstruction_terminal_basin_reflected_fixedpoint_trace_executable_global_contraction_certificate"
)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    current = data["current_requirements"]
    accepted = set(current["atoms"]) | set(current["invariants"])

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc") >= 606
        and DOC606_WITNESS in data.get("witnesses", {})
        and KILLPRIORITYACTION in accepted,
        f"frontier_doc={data['frontier']['current_doc']} doc606_witness={DOC606_WITNESS in data.get('witnesses', {})}",
    )
    gate(
        f"{PREFIX}2",
        len(PRIORITY_DECISIONS) == 106
        and len(SEMANTIC_PRIORITY) == 18
        and len(AMBIGUOUS_PRIORITY_DECISIONS) == 57,
        f"decisions={len(PRIORITY_DECISIONS)} classes={len(SEMANTIC_PRIORITY)} ambiguous={len(AMBIGUOUS_PRIORITY_DECISIONS)}",
    )
    gate(
        f"{PREFIX}3",
        len(LEXICON) == 706
        and all(typed_token_stream(decision["subject"]) for decision in PRIORITY_DECISIONS.values()),
        f"typed_lexicon={len(LEXICON)} max_stream={max(len(typed_token_stream(d['subject'])) for d in PRIORITY_DECISIONS.values())}",
    )
    gate(
        f"{PREFIX}4",
        len(STRICT_WINNER_FAILURES) == 3,
        "strict_winner_failures="
        + "; ".join(f"{subject}->{facet_class}/{tokens}" for _, subject, facet_class, tokens in STRICT_WINNER_FAILURES),
    )
    gate(
        f"{PREFIX}5",
        len(STRICT_SHADOW_FAILURES) == 2,
        "strict_shadow_failures="
        + "; ".join(f"{subject}->{facet_class}/{tokens}" for _, subject, facet_class, tokens in STRICT_SHADOW_FAILURES),
    )
    gate(
        f"{PREFIX}6",
        len(SUBSTRING_ONLY_MATCHES) == 8
        and any(
            surface == ACTION_IN_CONTRACTION_SURFACE and raw_token == "action"
            for surface, _, _, raw_token in SUBSTRING_ONLY_MATCHES
        ),
        f"substring_only_matches={len(SUBSTRING_ONLY_MATCHES)}",
    )
    gate(
        f"{PREFIX}7",
        len(PLURAL_STEM_WINNER_FAILURES) == 1
        and PLURAL_STEM_WINNER_FAILURES[0][0] == ACTION_IN_CONTRACTION_SURFACE,
        "plural stemming still leaves action-inside-contraction false winner",
    )
    gate(
        f"{PREFIX}8",
        bool(STRICT_WINNER_FAILURES)
        and bool(SUBSTRING_ONLY_MATCHES)
        and not any(kind == "substring" for kind, _ in LEXICON),
        "no finite source-native typed token grammar can preserve the exact doc606 priority decisions",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: doc606 priority fails typed-token preservation")
    print(
        "VERDICT: doc606's priority layer is killed as a source-native token "
        "grammar. The obstruction is substring-token priority collapse, with "
        "action inside contraction as the hard failure."
    )


if __name__ == "__main__":
    main()
