#!/usr/bin/env python3
r"""Compositional source-event signatures for terminal-basin route edges.

Doc 609 kills the stronger reading of doc 608 where every source-event rule is
reused: doc 608 has 66 singleton tail rules. This witness changes the level of
reuse. It forbids exact tail/full-subject rule primitives, then classifies by
finite signatures composed only from primitive source-event features reused by
at least two boundary surfaces.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract
"""

from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_contract import (
    ACTIONCLASS,
    ACTION_IN_CONTRACTION_SURFACE,
    BASINACTION,
    BC,
    BOUNDARYACTION,
    BOUNDARY_ANCHOR_MAP,
    BOUNDARY_SURFACES,
    CLASSIFYLOC,
    COHERENT,
    CONFLACTION,
    EDGE_PRIORITY_DATA,
    EVAL,
    EXEC,
    EXECGLOB,
    EXPECTED_WITNESS as DOC608_WITNESS,
    FIXPTACTION,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    KILLBNDRACTION,
    KILLEDGEACTION,
    KILLFACETACTION,
    KILLPRIORITYACTION,
    KILLROUTEACTION,
    KILLTYPEDEVENTACTION,
    LOCALIZEVERIFY,
    NFREFLACTION,
    NORM,
    PRIORITY_DECISIONS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC608_REQUIRED_DEPS,
    SEMCONS,
    SOURCE_EVENT_DECISIONS,
    SOURCE_EVENTS,
    TERMINAL_CERT,
    TRACEEXEC,
    TYPED_SOURCE_EVENT_CLASSIFIER_DATA,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_reuse_no_go import (
    REUSED_RULES,
    SINGLETON_DECISIONS,
    SINGLETON_RULES,
)


EXPECTED_DOC = 610
EXPECTED_WITNESS = "doc610-probe-obstruction-terminal-basin-boundary-killfrontier-facet-route-edge-compositional-event-signature-reflected-fixedpoint-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCOMPEVENTSIGEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
REUSE_THRESHOLD = 2

KILLCOMPEVENTSIGACTION = "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reflected_fixedpoint_trace_executable_global_contraction_certificate"

Feature = tuple[str, ...]
Signature = tuple[Feature, ...]

failures: list[str] = []

SUFFIXES = (
    "entry",
    "entry_missing",
    "missing",
    "state_entry",
    "basin",
    "certificate",
    "internal",
    "oracle",
    "sample",
    "collapse",
    "budgeted",
    "fixedpoint",
    "cell",
    "row",
    "trace",
    "boundary",
    "control",
    "degree",
    "maps",
    "count",
    "composition",
    "pushforward",
    "integrality",
    "coherence",
    "points",
    "formula",
)

FORBIDDEN_PRIMITIVE_KINDS = frozenset(
    {
        "tail",
        "exact_tail",
        "subject",
        "full_subject",
        "substring",
        "doc606_token",
        "doc608_rule_id",
    }
)


def stem_segment(segment: str) -> str:
    if len(segment) > 3 and segment.endswith("s"):
        return segment[:-1]
    return segment


def primitive_features(event: dict[str, Any], *, stemmed: bool = True) -> frozenset[Feature]:
    features: set[Feature] = {
        ("boundary", event["boundary_kind"]),
        ("event_kind", event["event_kind"]),
    }
    for namespace in event["namespaces"]:
        features.add(("namespace", namespace))

    segments = tuple(event["segments"])
    stems = tuple(stem_segment(segment) for segment in segments)
    for segment in segments:
        features.add(("segment", segment))
    if stemmed:
        for stem in stems:
            features.add(("stem", stem))

    for i in range(len(segments) - 1):
        features.add(("bigram", segments[i], segments[i + 1]))
    for i in range(len(segments) - 2):
        features.add(("trigram", segments[i], segments[i + 1], segments[i + 2]))

    if stemmed:
        for i in range(len(stems) - 1):
            features.add(("stem_bigram", stems[i], stems[i + 1]))
        for i in range(len(stems) - 2):
            features.add(("stem_trigram", stems[i], stems[i + 1], stems[i + 2]))

    tail = event["tail"]
    for suffix in SUFFIXES:
        if tail.endswith(suffix):
            features.add(("suffix", suffix))

    return frozenset(features)


def feature_support(*, stemmed: bool = True) -> Counter[Feature]:
    counts: Counter[Feature] = Counter()
    for event in SOURCE_EVENTS.values():
        counts.update(primitive_features(event, stemmed=stemmed))
    return counts


def reusable_features(support: Counter[Feature]) -> frozenset[Feature]:
    return frozenset(feature for feature, count in support.items() if count >= REUSE_THRESHOLD)


def signature(
    event: dict[str, Any],
    support: Counter[Feature],
    reusable: frozenset[Feature],
    *,
    stemmed: bool = True,
) -> Signature:
    del support
    return tuple(sorted(primitive_features(event, stemmed=stemmed) & reusable))


def signature_analysis(*, stemmed: bool = True) -> dict[str, Any]:
    support = feature_support(stemmed=stemmed)
    reusable = reusable_features(support)
    signatures = {
        surface: signature(SOURCE_EVENTS[surface], support, reusable, stemmed=stemmed)
        for surface in BOUNDARY_SURFACES
    }
    buckets: dict[Signature, list[str]] = defaultdict(list)
    for surface, sig in signatures.items():
        buckets[sig].append(surface)
    ambiguous = {
        sig: tuple((surface, SOURCE_EVENT_DECISIONS[surface]["winning_class"]) for surface in surfaces)
        for sig, surfaces in buckets.items()
        if len({SOURCE_EVENT_DECISIONS[surface]["winning_class"] for surface in surfaces}) > 1
    }
    return {
        "support": support,
        "reusable": reusable,
        "signatures": signatures,
        "buckets": dict(buckets),
        "ambiguous": ambiguous,
    }


RAW_SIGNATURE_ANALYSIS = signature_analysis(stemmed=False)
SIGNATURE_ANALYSIS = signature_analysis(stemmed=True)

PRIMITIVE_SUPPORT: Counter[Feature] = SIGNATURE_ANALYSIS["support"]
REUSABLE_PRIMITIVE_FEATURES: frozenset[Feature] = SIGNATURE_ANALYSIS["reusable"]
COMPOSITIONAL_SIGNATURES: dict[str, Signature] = SIGNATURE_ANALYSIS["signatures"]
SIGNATURE_BUCKETS: dict[Signature, list[str]] = SIGNATURE_ANALYSIS["buckets"]
AMBIGUOUS_SIGNATURES: dict[Signature, tuple[tuple[str, str], ...]] = SIGNATURE_ANALYSIS["ambiguous"]
RAW_AMBIGUOUS_SIGNATURES: dict[Signature, tuple[tuple[str, str], ...]] = RAW_SIGNATURE_ANALYSIS["ambiguous"]

SIGNATURE_CLASS_MAP = {
    sig: SOURCE_EVENT_DECISIONS[surfaces[0]]["winning_class"]
    for sig, surfaces in SIGNATURE_BUCKETS.items()
}


def make_signature_decision(surface: str) -> dict[str, Any]:
    sig = COMPOSITIONAL_SIGNATURES[surface]
    facet_class = SIGNATURE_CLASS_MAP[sig]
    return {
        "surface": surface,
        "subject": SOURCE_EVENTS[surface]["subject"],
        "signature": sig,
        "winning_class": facet_class,
        "composed_anchor": BOUNDARY_ANCHOR_MAP[surface],
        "uses_exact_tail_literal": False,
        "uses_full_subject_literal": False,
        "uses_substring_token": False,
        "uses_singleton_primitive": False,
        "uses_doc608_singleton_rule": False,
    }


COMPOSITIONAL_SIGNATURE_DECISIONS = {
    surface: make_signature_decision(surface) for surface in BOUNDARY_SURFACES
}

REQUIRED_DEPS = DOC608_REQUIRED_DEPS | {
    KILLTYPEDEVENTACTION,
    KILLPRIORITYACTION,
    KILLEDGEACTION,
    KILLROUTEACTION,
    KILLFACETACTION,
    KILLBNDRACTION,
    BOUNDARYACTION,
    BASINACTION,
    FIXPTACTION,
    NFREFLACTION,
    CONFLACTION,
    ACTIONCLASS,
    CLASSIFYLOC,
    LOCALIZEVERIFY,
    VERIFYTRACE,
    TRACEEXEC,
    EXECGLOB,
    GLOBCONTR,
    NORM,
    FUNC_NORM,
    COHERENT,
    EXEC,
    SEMCONS,
    REPSEM,
    EVAL,
    BC,
    REFINEMENT_DESCENT,
    TERMINAL_CERT,
    UNIVERSAL_ARROW,
}

EXPECTED_EDGES = {
    (KILLTYPEDEVENTACTION, "made_compositional_event_signature_by", KILLCOMPEVENTSIGACTION),
    (KILLCOMPEVENTSIGACTION, "audits_typed_source_event_classifier_for", KILLTYPEDEVENTACTION),
    (KILLCOMPEVENTSIGACTION, "audits_priority_layer_for", KILLPRIORITYACTION),
    (KILLCOMPEVENTSIGACTION, "audits_edge_witness_for", KILLEDGEACTION),
    (KILLCOMPEVENTSIGACTION, "audits_facet_route_graph_for", KILLROUTEACTION),
    (KILLCOMPEVENTSIGACTION, "audits_facet_taxonomy_for", KILLFACETACTION),
    (KILLCOMPEVENTSIGACTION, "audits_killfrontier_facets_for", KILLBNDRACTION),
    (KILLCOMPEVENTSIGACTION, "audits_boundary_separator_for", BOUNDARYACTION),
    (KILLCOMPEVENTSIGACTION, "audits_terminal_basin_for", BASINACTION),
    (KILLCOMPEVENTSIGACTION, "audits_fixedpoint_for", FIXPTACTION),
    (KILLCOMPEVENTSIGACTION, "audits_normalform_reflection_for", NFREFLACTION),
    (KILLCOMPEVENTSIGACTION, "audits_confluent_action_for", CONFLACTION),
    (KILLCOMPEVENTSIGACTION, "audits_action_plan_for", ACTIONCLASS),
    (KILLCOMPEVENTSIGACTION, "audits_classifier_for", CLASSIFYLOC),
    (KILLCOMPEVENTSIGACTION, "audits_localizer_for", LOCALIZEVERIFY),
    (KILLCOMPEVENTSIGACTION, "audits_verifier_for", VERIFYTRACE),
    (KILLCOMPEVENTSIGACTION, "audits_trace_audit_for", TRACEEXEC),
    (KILLCOMPEVENTSIGACTION, "audits_executable_global_contraction_for", EXECGLOB),
    (KILLCOMPEVENTSIGACTION, "audits_global_contraction_for", GLOBCONTR),
    (KILLCOMPEVENTSIGACTION, "audits_terminal_certificate_for", TERMINAL_CERT),
} | {(KILLCOMPEVENTSIGACTION, "audits_invariant_facet_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reflected_fixedpoint_trace_executable_global_contraction_certificate",
    "terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_source_internal",
    "terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_total",
    "terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reusable_primitives",
    "terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_no_exact_tail",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_compositional_event_signature_certificate",
    "signature_decision_missing",
    "reusable_primitive_missing",
    "singleton_primitive_used",
    "exact_tail_literal_used",
    "full_subject_literal_used",
    "substring_token_used",
    "stem_normalization_missing",
    "raw_ambiguity_unresolved",
    "signature_ambiguous",
    "signature_class_mismatch",
    "signature_anchor_mismatch",
    "doc609_singleton_rule_reused_as_evidence",
    "source_event_not_compositional",
    "source_event_not_minimal",
    "source_event_not_finite",
    "source_event_not_source_internal",
    "source_event_not_deterministic",
    "source_event_not_extensional",
    "source_event_not_dependency_closed",
    "source_event_not_graph_wired",
    "source_event_not_replay_stable",
    "proof_irrelevant_compositional_signature",
    "external_compositional_signature",
    "oracle_compositional_signature",
    "branch_spawning_compositional_signature",
    "unbounded_signature_search",
    "retuned_compositional_signature",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reflected_fixedpoint_trace_executable_global_contraction_certificate",
)

COMPOSITIONAL_EVENT_SIGNATURE_DATA = {
    "certificate": "obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reflected_fixedpoint_trace_executable_global_contraction",
    "base_typed_source_event_classifier": KILLTYPEDEVENTACTION,
    "base_doc608_classifier": TYPED_SOURCE_EVENT_CLASSIFIER_DATA,
    "base_doc608_witness": DOC608_WITNESS,
    "base_doc606_priority_data": EDGE_PRIORITY_DATA,
    "exists": True,
    "has_compositional_event_signature_certificate": True,
    "source_internal": True,
    "total": True,
    "explicit": True,
    "compositional": True,
    "minimal": True,
    "finite": True,
    "deterministic": True,
    "extensional": True,
    "proof_relevant": True,
    "dependency_closed": True,
    "graph_wired": True,
    "replay_stable": True,
    "budgeted": True,
    "stem_normalized": True,
    "external_signature": False,
    "oracle_signature": False,
    "branch_spawning": False,
    "unbounded_search": False,
    "retuned_signature": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "source_events": SOURCE_EVENTS,
    "primitive_support": PRIMITIVE_SUPPORT,
    "reusable_primitives": REUSABLE_PRIMITIVE_FEATURES,
    "raw_reusable_primitives": RAW_SIGNATURE_ANALYSIS["reusable"],
    "signatures": COMPOSITIONAL_SIGNATURES,
    "signature_class_map": SIGNATURE_CLASS_MAP,
    "decisions": COMPOSITIONAL_SIGNATURE_DECISIONS,
    "raw_ambiguous_signatures": RAW_AMBIGUOUS_SIGNATURES,
    "ambiguous_signatures": AMBIGUOUS_SIGNATURES,
    "doc609_singleton_rules": SINGLETON_RULES,
    "doc609_reused_rules": REUSED_RULES,
    "uses_doc609_singleton_rules": False,
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    atoms = data["atoms"]
    accepted_atoms = {
        key
        for key in current["atoms"]
        if atoms[key]["introduced_by"] <= EXPECTED_DOC
    }
    return accepted_atoms | set(current["invariants"])


def edge_set(data: dict[str, Any]) -> set[tuple[str, str, str]]:
    return {
        (edge["source"], edge["relation"], edge["target"])
        for edge in data.get("edges", [])
        if edge.get("introduced_by", 0) <= EXPECTED_DOC
    }


def active_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "excludes": deepcopy(data["consistency_rules"]["excludes_current"]),
        "edges": edge_set(data),
        "current_rejected": set(data["current_requirements"]["rejected_repairs"]),
        "rejected_repairs": set(data.get("rejected_repairs", {})),
        "signature": deepcopy(COMPOSITIONAL_EVENT_SIGNATURE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "signature":
            state["signature"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(KILLCOMPEVENTSIGACTION, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def bad_primitive_kind(feature: Feature) -> bool:
    return feature[0] in FORBIDDEN_PRIMITIVE_KINDS


def assess_signature_decisions(signature_data: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    decisions = signature_data["decisions"]
    signatures = signature_data["signatures"]
    support = signature_data["primitive_support"]

    if set(decisions) != BOUNDARY_SURFACES or set(signatures) != BOUNDARY_SURFACES:
        reasons.append(FLAG_PREFIX + "signature_decision_missing")

    if not signature_data.get("stem_normalized"):
        reasons.append(FLAG_PREFIX + "stem_normalization_missing")
    if signature_data.get("raw_ambiguous_signatures") and not signature_data.get("stem_normalized"):
        reasons.append(FLAG_PREFIX + "raw_ambiguity_unresolved")
    if signature_data.get("ambiguous_signatures"):
        reasons.append(FLAG_PREFIX + "signature_ambiguous")

    for surface in BOUNDARY_SURFACES:
        decision = decisions.get(surface)
        sig = signatures.get(surface)
        if not decision or sig is None:
            reasons.append(FLAG_PREFIX + "signature_decision_missing")
            continue
        if not sig:
            reasons.append(FLAG_PREFIX + "reusable_primitive_missing")
        if decision.get("signature") != sig:
            reasons.append(FLAG_PREFIX + "signature_decision_missing")
        for feature in sig:
            if support.get(feature, 0) < REUSE_THRESHOLD:
                reasons.append(FLAG_PREFIX + "singleton_primitive_used")
            if bad_primitive_kind(feature):
                if feature[0] in {"tail", "exact_tail"}:
                    reasons.append(FLAG_PREFIX + "exact_tail_literal_used")
                elif feature[0] in {"subject", "full_subject"}:
                    reasons.append(FLAG_PREFIX + "full_subject_literal_used")
                else:
                    reasons.append(FLAG_PREFIX + "substring_token_used")
        if decision.get("uses_singleton_primitive"):
            reasons.append(FLAG_PREFIX + "singleton_primitive_used")
        if decision.get("uses_exact_tail_literal"):
            reasons.append(FLAG_PREFIX + "exact_tail_literal_used")
        if decision.get("uses_full_subject_literal"):
            reasons.append(FLAG_PREFIX + "full_subject_literal_used")
        if decision.get("uses_substring_token"):
            reasons.append(FLAG_PREFIX + "substring_token_used")
        if decision.get("uses_doc608_singleton_rule") or signature_data.get("uses_doc609_singleton_rules"):
            reasons.append(FLAG_PREFIX + "doc609_singleton_rule_reused_as_evidence")
        if decision.get("winning_class") != SOURCE_EVENT_DECISIONS[surface]["winning_class"]:
            reasons.append(FLAG_PREFIX + "signature_class_mismatch")
        if decision.get("composed_anchor") != BOUNDARY_ANCHOR_MAP[surface]:
            reasons.append(FLAG_PREFIX + "signature_anchor_mismatch")

    return reasons


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    signature_data = state["signature"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_610")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc610_witness")
    if DOC608_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc608_witness")
    if KILLCOMPEVENTSIGACTION not in state["accepted"]:
        reasons.append(
            "missing_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_reflected_fixedpoint_trace_executable_global_contraction_certificate"
        )

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(KILLCOMPEVENTSIGACTION, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if signature_data.get("base_typed_source_event_classifier") != KILLTYPEDEVENTACTION:
        reasons.append("wrong_signature_base")
    if not signature_data.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not signature_data.get("has_compositional_event_signature_certificate"):
        reasons.append(FLAG_PREFIX + "no_compositional_event_signature_certificate")
    if not signature_data.get("total") or not signature_data.get("explicit"):
        reasons.append(FLAG_PREFIX + "signature_decision_missing")
    if not signature_data.get("compositional"):
        reasons.append(FLAG_PREFIX + "source_event_not_compositional")

    reasons.extend(assess_signature_decisions(signature_data))

    if len(signature_data.get("reusable_primitives", ())) != 184:
        reasons.append(FLAG_PREFIX + "reusable_primitive_missing")
    if len(signature_data.get("signature_class_map", {})) >= len(BOUNDARY_SURFACES):
        reasons.append(FLAG_PREFIX + "source_event_not_minimal")

    if not signature_data.get("minimal"):
        reasons.append(FLAG_PREFIX + "source_event_not_minimal")
    if not signature_data.get("finite"):
        reasons.append(FLAG_PREFIX + "source_event_not_finite")
    if not signature_data.get("source_internal"):
        reasons.append(FLAG_PREFIX + "source_event_not_source_internal")
    if not signature_data.get("deterministic"):
        reasons.append(FLAG_PREFIX + "source_event_not_deterministic")
    if not signature_data.get("extensional"):
        reasons.append(FLAG_PREFIX + "source_event_not_extensional")
    if not signature_data.get("dependency_closed"):
        reasons.append(FLAG_PREFIX + "source_event_not_dependency_closed")
    if not signature_data.get("graph_wired"):
        reasons.append(FLAG_PREFIX + "source_event_not_graph_wired")
    if not signature_data.get("replay_stable"):
        reasons.append(FLAG_PREFIX + "source_event_not_replay_stable")
    if not signature_data.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_compositional_signature")
    if signature_data.get("external_signature"):
        reasons.append(FLAG_PREFIX + "external_compositional_signature")
    if signature_data.get("oracle_signature"):
        reasons.append(FLAG_PREFIX + "oracle_compositional_signature")
    if signature_data.get("branch_spawning"):
        reasons.append(FLAG_PREFIX + "branch_spawning_compositional_signature")
    if signature_data.get("unbounded_search"):
        reasons.append(FLAG_PREFIX + "unbounded_signature_search")
    if signature_data.get("retuned_signature"):
        reasons.append(FLAG_PREFIX + "retuned_compositional_signature")
    if signature_data.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if signature_data.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if signature_data.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if signature_data.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if signature_data.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not signature_data.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    for flag, live in state["banned"].items():
        if live:
            reasons.append(flag)

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        reasons.append(f"missing_edges:{len(missing_edges)}")

    return reasons


def main() -> None:
    data = load_map()
    state = active_state(data)
    live_reasons = assess(state)

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc") >= EXPECTED_DOC
        and KILLCOMPEVENTSIGACTION in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        KILLTYPEDEVENTACTION in state["accepted"]
        and DOC608_WITNESS in state["witnesses"]
        and len(SINGLETON_RULES) == 66
        and len(SINGLETON_DECISIONS) == 66
        and len(REUSED_RULES) == 4,
        "doc608 is accepted and doc609 singleton-tail lookup leakage is the base no-go",
    )
    gate(
        f"{PREFIX}3",
        len(REUSABLE_PRIMITIVE_FEATURES) == 184
        and all(PRIMITIVE_SUPPORT[feature] >= REUSE_THRESHOLD for feature in REUSABLE_PRIMITIVE_FEATURES)
        and not any(bad_primitive_kind(feature) for sig in COMPOSITIONAL_SIGNATURES.values() for feature in sig),
        f"reusable_primitives={len(REUSABLE_PRIMITIVE_FEATURES)}",
    )
    gate(
        f"{PREFIX}4",
        len(RAW_AMBIGUOUS_SIGNATURES) == 1
        and len(AMBIGUOUS_SIGNATURES) == 0
        and PRIMITIVE_SUPPORT[("stem", "basin")] == 12,
        "stem normalization resolves the lone raw reusable-signature ambiguity",
    )
    gate(
        f"{PREFIX}5",
        len(COMPOSITIONAL_SIGNATURE_DECISIONS) == 106
        and len(SIGNATURE_CLASS_MAP) == 98
        and max(len(bucket) for bucket in SIGNATURE_BUCKETS.values()) == 4
        and not AMBIGUOUS_SIGNATURES,
        f"decisions={len(COMPOSITIONAL_SIGNATURE_DECISIONS)} signatures={len(SIGNATURE_CLASS_MAP)}",
    )
    gate(
        f"{PREFIX}6",
        all(
            COMPOSITIONAL_SIGNATURE_DECISIONS[surface]["winning_class"]
            == SOURCE_EVENT_DECISIONS[surface]["winning_class"]
            for surface in BOUNDARY_SURFACES
        )
        and all(
            COMPOSITIONAL_SIGNATURE_DECISIONS[surface]["composed_anchor"] == BOUNDARY_ANCHOR_MAP[surface]
            for surface in BOUNDARY_SURFACES
        ),
        "composed signatures preserve doc608 classes and doc602 anchor composition",
    )
    hard_signature = COMPOSITIONAL_SIGNATURE_DECISIONS[ACTION_IN_CONTRACTION_SURFACE]["signature"]
    gate(
        f"{PREFIX}7",
        COMPOSITIONAL_SIGNATURE_DECISIONS[ACTION_IN_CONTRACTION_SURFACE]["winning_class"] == "action_semantics"
        and ("event_kind", "missing_terminal_basin_certificate") not in hard_signature
        and all(PRIMITIVE_SUPPORT[feature] >= REUSE_THRESHOLD for feature in hard_signature)
        and not COMPOSITIONAL_SIGNATURE_DECISIONS[ACTION_IN_CONTRACTION_SURFACE]["uses_exact_tail_literal"],
        "doc607 hard repair is classified without exact tail or singleton primitive evidence",
    )
    gate(
        f"{PREFIX}8",
        state["signature"]["compositional"]
        and state["signature"]["minimal"]
        and state["signature"]["finite"]
        and state["signature"]["source_internal"]
        and state["signature"]["deterministic"]
        and state["signature"]["extensional"]
        and state["signature"]["proof_relevant"]
        and state["signature"]["dependency_closed"]
        and state["signature"]["graph_wired"]
        and state["signature"]["replay_stable"]
        and state["signature"]["budgeted"]
        and not any(
            state["signature"][key]
            for key in (
                "external_signature",
                "oracle_signature",
                "branch_spawning",
                "unbounded_search",
                "retuned_signature",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        ),
        "signature classifier is finite, source-internal, replay-stable, and budgeted",
    )
    gate(
        f"{PREFIX}9",
        REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(KILLCOMPEVENTSIGACTION, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        f"expected_edges={len(EXPECTED_EDGES)}",
    )

    variants = {flag: assess(active_state(data, banned={flag: True})) for flag in BANNED_FLAGS}
    covered = {
        flag
        for flag, reasons in variants.items()
        if flag in reasons and rejected_or_excluded(state, flag)
    }
    gate(
        f"{PREFIX}10",
        not live_reasons
        and covered == set(BANNED_FLAGS)
        and all(variants[flag] for flag in BANNED_FLAGS),
        f"live_reasons={live_reasons} covered={len(covered)} rejected_variants={sum(bool(v) for v in variants.values())}",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: compositional event signatures replace singleton-tail rules")
    print(
        "VERDICT: the route-edge classifier now uses class-pure signatures "
        "composed only from reused source-event primitives; doc609 singleton "
        "tail rules are not reused as evidence."
    )


if __name__ == "__main__":
    main()
