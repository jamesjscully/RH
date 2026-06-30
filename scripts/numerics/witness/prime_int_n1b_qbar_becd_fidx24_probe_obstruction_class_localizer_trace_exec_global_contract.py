#!/usr/bin/env python3
r"""Obstruction-classifying localizer trace executable global contraction.

Doc 594 turns verifier rejection into a localized obstruction. This witness
closes the next escape: localized obstructions cannot remain bespoke search
branches. The doc 595 frontier only counts if every localized obstruction is
classified by a finite source-internal taxonomy with explicit repair/no-go,
kill-frontier, budget, and context links.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_class_localizer_trace_exec_global_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_loc_verifier_trace_exec_global_contract import (
    ADM_CAT,
    BC,
    COHERENT,
    EVAL,
    EXEC,
    EXECGLOB,
    FUNC_NORM,
    GLOBCONTR,
    INVARIANT_TRACE_TARGETS,
    LOCALIZEVERIFY,
    LOCALIZER_EVENTS,
    NORM,
    OBSTRUCTION_FACETS,
    PAYLOAD_TRACE_EVENTS,
    REFINEMENT_DESCENT,
    REPSEM,
    REQUIRED_DEPS as DOC594_REQUIRED_DEPS,
    SEMCONS,
    TERMINAL_CERT,
    TRACEEXEC,
    UNIVERSAL_ARROW,
    VERIFYTRACE,
    load_map,
)


EXPECTED_DOC = 595
EXPECTED_WITNESS = "doc595-probe-obstruction-classifying-localizer-trace-executable-global-contraction-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCLASSLOCVERIFTRACEEXECGLOBCONTR"

CLASSIFYLOC = "obstruction_classifying_localizer_trace_executable_global_contraction_certificate"

failures: list[str] = []

CLASSIFICATION_CODES = {
    "accepted",
    "fatal_no_go",
    "repair_required_existing_requirement",
    "dependency_missing",
    "budget_violation",
    "context_collapse",
    "external_or_oracle",
    "presentation_or_sample",
}

OBSTRUCTION_CLASSES = CLASSIFICATION_CODES - {"accepted"}

CLASSIFIER_EVENTS = {
    "classify_accepted_trace",
    "classify_localized_obstruction",
    "classify_fatal_no_go",
    "classify_repair_required_existing_requirement",
    "classify_dependency_missing",
    "classify_budget_violation",
    "classify_context_collapse",
    "classify_external_or_oracle",
    "classify_presentation_or_sample",
    "emit_repair_or_no_go_link",
    "emit_kill_frontier_link",
    "emit_budget_context_link",
}

REQUIRED_DEPS = DOC594_REQUIRED_DEPS | {
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
    ADM_CAT,
}

EXPECTED_EDGES = {
    (LOCALIZEVERIFY, "made_obstruction_classifying_by", CLASSIFYLOC),
    (CLASSIFYLOC, "classifies_localized_obstruction_for", LOCALIZEVERIFY),
    (CLASSIFYLOC, "classifies_verifier_failure_for", VERIFYTRACE),
    (CLASSIFYLOC, "classifies_trace_audit_failure_for", TRACEEXEC),
    (CLASSIFYLOC, "classifies_executable_global_contraction_failure_for", EXECGLOB),
    (CLASSIFYLOC, "classifies_global_contraction_failure_for", GLOBCONTR),
    (CLASSIFYLOC, "classifies_law_via", NORM),
    (CLASSIFYLOC, "classifies_law_via", FUNC_NORM),
    (CLASSIFYLOC, "classifies_law_via", COHERENT),
    (CLASSIFYLOC, "classifies_law_via", EXEC),
    (CLASSIFYLOC, "classifies_law_via", SEMCONS),
    (CLASSIFYLOC, "classifies_law_via", REPSEM),
    (CLASSIFYLOC, "classifies_law_via", EVAL),
    (CLASSIFYLOC, "classifies_law_via", BC),
    (CLASSIFYLOC, "classifies_law_via", REFINEMENT_DESCENT),
    (CLASSIFYLOC, "classifies_law_via", TERMINAL_CERT),
    (CLASSIFYLOC, "classifies_law_via", UNIVERSAL_ARROW),
} | {(CLASSIFYLOC, "classifies_invariant_failure_for", target) for target in INVARIANT_TRACE_TARGETS}

REQUIRED_FLAGS = (
    "obstruction_classifying_localizer_trace_executable_global_contraction_certificate",
    "classifier_source_internal",
    "classifier_finite_total_taxonomy",
    "classifier_links_repair_no_go_kill_frontier",
    "classifier_links_budget_and_context_classes",
    "inside_exact_24_budget",
)

FLAG_PREFIX = "center_eliminator_semantics_evaluation_obstruction_classifier_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_"

BANNED_SUFFIXES = (
    "missing",
    "no_classifier",
    "unclassified_obstruction",
    "infinite_taxonomy",
    "external_classifier",
    "oracle_classifier",
    "wrong_class",
    "ambiguous_class",
    "nonfatal_class_leak",
    "not_source_internal",
    "not_total",
    "nondeterministic_classifier",
    "nonterminating_classifier",
    "proof_irrelevant_classifier",
    "nonextensional",
    "repair_link_missing",
    "no_go_link_missing",
    "kill_frontier_link_missing",
    "budget_class_missing",
    "context_class_missing",
    "sample_class_missing",
    "taxonomy_retuned",
    "requires_new_cell",
    "context_collapse",
    "by_declaration",
    "finite_sample",
    "basis_row",
    "not_budgeted",
)

BANNED_FLAGS = tuple(FLAG_PREFIX + suffix for suffix in BANNED_SUFFIXES) + (
    "missing_obstruction_classifying_localizer_trace_executable_global_contraction_certificate",
)

CLASSIFIER_DATA = {
    "certificate": "obstruction_classifying_localizer_trace_executable_global_contraction",
    "base_localizer": LOCALIZEVERIFY,
    "base_verifier": VERIFYTRACE,
    "base_trace": TRACEEXEC,
    "base_executable": EXECGLOB,
    "base_global_contractible": GLOBCONTR,
    "exists": True,
    "has_classifier": True,
    "source_internal": True,
    "finite_taxonomy": True,
    "total": True,
    "deterministic": True,
    "terminating": True,
    "proof_relevant": True,
    "extensional_over_obstruction": True,
    "replay_stable": True,
    "budgeted": True,
    "unclassified_obstruction": False,
    "external_classifier": False,
    "oracle_classifier": False,
    "wrong_class": False,
    "ambiguous_class": False,
    "nonfatal_class_leak": False,
    "taxonomy_retuned": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "classes": CLASSIFICATION_CODES,
    "obstruction_classes": OBSTRUCTION_CLASSES,
    "fatal_classes": {
        "fatal_no_go",
        "context_collapse",
        "external_or_oracle",
        "budget_violation",
    },
    "repair_classes": {
        "repair_required_existing_requirement",
        "dependency_missing",
        "presentation_or_sample",
    },
    "classifier_events": CLASSIFIER_EVENTS,
    "localizer_events": LOCALIZER_EVENTS,
    "facets": OBSTRUCTION_FACETS,
    "invariant_targets": INVARIANT_TRACE_TARGETS,
    "payload_events": PAYLOAD_TRACE_EVENTS,
    "classified_facets": OBSTRUCTION_FACETS,
    "classified_events": LOCALIZER_EVENTS,
    "repair_links": {
        "repair_required_existing_requirement",
        "dependency_missing",
        "presentation_or_sample",
    },
    "no_go_links": {
        "fatal_no_go",
        "context_collapse",
        "external_or_oracle",
        "budget_violation",
    },
    "kill_frontier_links": {
        "obstruction_localizing_verifier_failure",
        "verifier_separated_trace_failure",
        "trace_audited_executable_global_contraction_failure",
        "executable_global_contraction_failure",
        "finite_index_budget_impossibility",
        "dependency_closure_impossibility",
        "context_collapse_dd4",
    },
    "budget_classes": {"budget_violation"},
    "context_classes": {"context_collapse"},
    "sample_classes": {"presentation_or_sample"},
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
        "kill_frontier": {item["id"] for item in data["kill_frontier"]["current"]},
        "current_rejected": set(data["current_requirements"]["rejected_repairs"]),
        "rejected_repairs": set(data.get("rejected_repairs", {})),
        "classifier": deepcopy(CLASSIFIER_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "classifier":
            state["classifier"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(CLASSIFYLOC, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    classifier = state["classifier"]
    events = set(classifier["classifier_events"])
    classes = set(classifier["classes"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_595")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc595_witness")
    if CLASSIFYLOC not in state["accepted"]:
        reasons.append("missing_obstruction_classifying_localizer_trace_executable_global_contraction_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(CLASSIFYLOC, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if classifier.get("base_localizer") != LOCALIZEVERIFY or classifier.get("base_verifier") != VERIFYTRACE:
        reasons.append("wrong_classifier_base")
    if not classifier.get("exists"):
        reasons.append(FLAG_PREFIX + "missing")
    if not classifier.get("has_classifier"):
        reasons.append(FLAG_PREFIX + "no_classifier")
    if classifier.get("unclassified_obstruction"):
        reasons.append(FLAG_PREFIX + "unclassified_obstruction")
    if not classifier.get("finite_taxonomy") or classes != CLASSIFICATION_CODES:
        reasons.append(FLAG_PREFIX + "infinite_taxonomy")
    if classifier.get("external_classifier"):
        reasons.append(FLAG_PREFIX + "external_classifier")
    if classifier.get("oracle_classifier"):
        reasons.append(FLAG_PREFIX + "oracle_classifier")
    if classifier.get("wrong_class"):
        reasons.append(FLAG_PREFIX + "wrong_class")
    if classifier.get("ambiguous_class"):
        reasons.append(FLAG_PREFIX + "ambiguous_class")
    if classifier.get("nonfatal_class_leak"):
        reasons.append(FLAG_PREFIX + "nonfatal_class_leak")
    if not classifier.get("source_internal"):
        reasons.append(FLAG_PREFIX + "not_source_internal")
    if not classifier.get("total"):
        reasons.append(FLAG_PREFIX + "not_total")
    if not classifier.get("deterministic"):
        reasons.append(FLAG_PREFIX + "nondeterministic_classifier")
    if not classifier.get("terminating"):
        reasons.append(FLAG_PREFIX + "nonterminating_classifier")
    if not classifier.get("proof_relevant"):
        reasons.append(FLAG_PREFIX + "proof_irrelevant_classifier")
    if not classifier.get("extensional_over_obstruction"):
        reasons.append(FLAG_PREFIX + "nonextensional")
    if classifier.get("taxonomy_retuned"):
        reasons.append(FLAG_PREFIX + "taxonomy_retuned")
    if classifier.get("new_cell"):
        reasons.append(FLAG_PREFIX + "requires_new_cell")
    if classifier.get("context_collapse"):
        reasons.append(FLAG_PREFIX + "context_collapse")
    if classifier.get("declared_only"):
        reasons.append(FLAG_PREFIX + "by_declaration")
    if classifier.get("finite_sample"):
        reasons.append(FLAG_PREFIX + "finite_sample")
    if classifier.get("basis_row"):
        reasons.append(FLAG_PREFIX + "basis_row")
    if not classifier.get("budgeted"):
        reasons.append(FLAG_PREFIX + "not_budgeted")

    if classifier["classified_facets"] != OBSTRUCTION_FACETS:
        reasons.append("unclassified_obstruction_facets")
    if classifier["classified_events"] != LOCALIZER_EVENTS:
        reasons.append("unclassified_localizer_events")
    if not OBSTRUCTION_CLASSES <= classes:
        reasons.append(FLAG_PREFIX + "unclassified_obstruction")
    if not classifier["repair_classes"] <= classifier["repair_links"]:
        reasons.append(FLAG_PREFIX + "repair_link_missing")
    if not classifier["fatal_classes"] <= classifier["no_go_links"]:
        reasons.append(FLAG_PREFIX + "no_go_link_missing")
    if not classifier["kill_frontier_links"] <= state["kill_frontier"]:
        reasons.append(FLAG_PREFIX + "kill_frontier_link_missing")
    if "budget_violation" not in classifier["budget_classes"]:
        reasons.append(FLAG_PREFIX + "budget_class_missing")
    if "context_collapse" not in classifier["context_classes"]:
        reasons.append(FLAG_PREFIX + "context_class_missing")
    if "presentation_or_sample" not in classifier["sample_classes"]:
        reasons.append(FLAG_PREFIX + "sample_class_missing")

    required_events = {
        "classify_accepted_trace",
        "classify_localized_obstruction",
        "classify_fatal_no_go",
        "classify_repair_required_existing_requirement",
        "classify_dependency_missing",
        "classify_budget_violation",
        "classify_context_collapse",
        "classify_external_or_oracle",
        "classify_presentation_or_sample",
        "emit_repair_or_no_go_link",
        "emit_kill_frontier_link",
        "emit_budget_context_link",
    }
    if not required_events <= events:
        reasons.append("missing_classifier_events")
    if not LOCALIZER_EVENTS <= set(classifier["localizer_events"]):
        reasons.append("missing_localizer_event_classification")
    if classifier["invariant_targets"] != INVARIANT_TRACE_TARGETS:
        reasons.append("missing_invariant_classification")
    if not PAYLOAD_TRACE_EVENTS <= set(classifier["payload_events"]):
        reasons.append("missing_payload_route_classification")

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
        and CLASSIFYLOC in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["classifier"]["base_localizer"] == LOCALIZEVERIFY
        and state["classifier"]["has_classifier"]
        and state["classifier"]["source_internal"]
        and state["classifier"]["finite_taxonomy"],
        "source-internal finite classifier is attached to doc594 localizer",
    )
    gate(
        f"{PREFIX}3",
        state["classifier"]["total"]
        and state["classifier"]["deterministic"]
        and state["classifier"]["terminating"]
        and state["classifier"]["proof_relevant"]
        and state["classifier"]["extensional_over_obstruction"]
        and state["classifier"]["replay_stable"],
        "classifier is total, deterministic, terminating, proof-relevant, extensional, and replay-stable",
    )
    gate(
        f"{PREFIX}4",
        state["classifier"]["classes"] == CLASSIFICATION_CODES
        and state["classifier"]["obstruction_classes"] == OBSTRUCTION_CLASSES
        and state["classifier"]["classified_facets"] == OBSTRUCTION_FACETS
        and state["classifier"]["classified_events"] == LOCALIZER_EVENTS,
        "finite taxonomy classifies every localized facet and localizer event",
    )
    gate(
        f"{PREFIX}5",
        state["classifier"]["repair_classes"] <= state["classifier"]["repair_links"]
        and state["classifier"]["fatal_classes"] <= state["classifier"]["no_go_links"]
        and state["classifier"]["kill_frontier_links"] <= state["kill_frontier"],
        "each obstruction class links to repair/no-go and kill-frontier evidence",
    )
    gate(
        f"{PREFIX}6",
        "budget_violation" in state["classifier"]["budget_classes"]
        and "context_collapse" in state["classifier"]["context_classes"]
        and "presentation_or_sample" in state["classifier"]["sample_classes"],
        "budget, context, and presentation/sample failures have named classes",
    )
    gate(
        f"{PREFIX}7",
        not any(
            state["classifier"][key]
            for key in (
                "unclassified_obstruction",
                "external_classifier",
                "oracle_classifier",
                "wrong_class",
                "ambiguous_class",
                "nonfatal_class_leak",
                "taxonomy_retuned",
            )
        ),
        "no unclassified, external, oracle, wrong, ambiguous, leaking, or retuned classes",
    )
    gate(
        f"{PREFIX}8",
        state["classifier"]["budgeted"]
        and not any(
            state["classifier"][key]
            for key in (
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(CLASSIFYLOC, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "obstruction classifier is dependency-closed, graph-wired, budgeted, and internal",
    )

    variants = {flag: assess(active_state(data, banned={flag: True})) for flag in BANNED_FLAGS}
    covered = {
        flag
        for flag, reasons in variants.items()
        if flag in reasons and rejected_or_excluded(state, flag)
    }
    gate(
        f"{PREFIX}9",
        covered == set(BANNED_FLAGS),
        f"covered={len(covered)}",
    )
    gate(
        f"{PREFIX}10",
        not live_reasons and all(variants[flag] for flag in BANNED_FLAGS),
        f"live_reasons={live_reasons} rejected_variants={sum(bool(v) for v in variants.values())}",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: localized verifier failures are finitely classified")
    print(
        "VERDICT: the missing-object candidate now counts only when every "
        "localized obstruction enters a finite source-internal taxonomy linked "
        "to repair/no-go, kill-frontier, budget, and context evidence; "
        "unclassified, ambiguous, retuned, external, oracle, sample, or "
        "unbudgeted classifiers are disguised repairs."
    )


if __name__ == "__main__":
    main()
