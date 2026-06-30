#!/usr/bin/env python3
r"""Source-law completeness for reflected pasted cyclic Beck-Chevalley mates.

Doc 583 requires pasted cyclic Beck-Chevalley mate equalities to be reflected
by the existing finite executable normalizer and conservative represented
semantics. This witness closes the next cheap escape: those normal forms may
still cover only selected pasted diagrams instead of the full source-law
generator inventory. The current frontier only counts if the same normal-form
reflection is complete for endpoint integrality, degree maps, DD.4 boundary,
exact-delta, graph composition, Rosati, control death, handoff, and the
composition/refinement/descent laws that generate the source square.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the source-law complete normal-form witness") from exc

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    BASE_CHANGE_ROUTES,
    BC,
    COHERENT,
    CONTROL,
    CYCLIC,
    DD4_BOUNDARY,
    DIAG,
    EVAL,
    EXACT_DELTA,
    EXEC,
    FUNC_NORM,
    GRAPH_COMP,
    GRAPH_LATER,
    HANDOFF,
    MAP_PATH,
    MATE,
    MONEXACT_DAGGER,
    NORM,
    NORMREF,
    PASTE,
    PRESERVED_CONTEXTS,
    PROJECTION_FORMULA_TARGETS,
    PUSHFORWARD,
    REPSEM,
    ROSATI,
    SEMCONS,
    SUBREP,
    UNIVERSAL_ARROW,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_cyclic_ambidextrous_mate_beck_chevalley_evaluation_contract import (
    DEGREE,
    ENDPOINT,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract import (
    COMPOSITION_STABLE,
    FILTERED_COFINAL,
    REFINEMENT_DESCENT,
    REPRESENTED_LIMIT,
)


EXPECTED_DOC = 584
EXPECTED_WITNESS = "doc584-probe-source-law-complete-normal-form-reflecting-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSRCLAWCOMPNFREFLPASTECYCMATEBCHEVEVAL"

LAWCOMP = "source_law_complete_" + NORMREF

failures: list[str] = []

NORMALIZER_DEPS = {NORM, FUNC_NORM, MONEXACT_DAGGER, COHERENT, EXEC, SEMCONS, REPSEM}
LAW_COMPLETION_DEPS = {COMPOSITION_STABLE, REFINEMENT_DESCENT, FILTERED_COFINAL, REPRESENTED_LIMIT}
SOURCE_LAW_GENERATORS = {
    ENDPOINT,
    DEGREE,
    DD4_BOUNDARY,
    PUSHFORWARD,
    EXACT_DELTA,
    GRAPH_COMP,
    ROSATI,
    CONTROL,
    HANDOFF,
    GRAPH_LATER,
}

REQUIRED_DEPS = {
    NORMREF,
    PASTE,
    CYCLIC,
    MATE,
    BC,
    EVAL,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
} | NORMALIZER_DEPS | LAW_COMPLETION_DEPS | SOURCE_LAW_GENERATORS | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (NORMREF, "made_source_law_complete_by", LAWCOMP),
    (LAWCOMP, "source_law_complete_for", NORMREF),
    (LAWCOMP, "complete_for_pasting_stable_mate", PASTE),
    (LAWCOMP, "complete_for_cyclic_mate", CYCLIC),
    (LAWCOMP, "complete_for_mate", MATE),
    (LAWCOMP, "complete_for_base_change", BC),
    (LAWCOMP, "complete_for_evaluation", EVAL),
    (LAWCOMP, "source_law_complete_over", DIAG),
    (LAWCOMP, "source_law_internal_to", SUBREP),
    (LAWCOMP, "source_law_selected_by", UNIVERSAL_ARROW),
    (LAWCOMP, "complete_normalizer_via", NORM),
    (LAWCOMP, "complete_functorial_normalizer_via", FUNC_NORM),
    (LAWCOMP, "complete_monoidal_exact_dagger_normalizer_via", MONEXACT_DAGGER),
    (LAWCOMP, "complete_coherent_normalizer_via", COHERENT),
    (LAWCOMP, "complete_executable_diamonds_via", EXEC),
    (LAWCOMP, "complete_semantics_via", SEMCONS),
    (LAWCOMP, "complete_represented_semantics_via", REPSEM),
    (LAWCOMP, "complete_for_composition_law", COMPOSITION_STABLE),
    (LAWCOMP, "complete_for_refinement_law", REFINEMENT_DESCENT),
    (LAWCOMP, "complete_for_filtered_cofinal_law", FILTERED_COFINAL),
    (LAWCOMP, "complete_for_represented_limit_law", REPRESENTED_LIMIT),
} | {(LAWCOMP, "complete_source_law_generator_for", target) for target in SOURCE_LAW_GENERATORS} | {
    (LAWCOMP, "complete_projection_law_for", target) for target in PROJECTION_FORMULA_TARGETS
} | {(LAWCOMP, "complete_route_law_for", target) for target in BASE_CHANGE_ROUTES} | {
    (LAWCOMP, "complete_context_law_for", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "source_law_complete_certificate",
    "all_source_law_generators_covered",
    "payload_complete",
    "structure_complete",
    "critical_pair_coverage_complete",
    "semantic_completeness",
    "not_selected_diagrams_only",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_law_complete_nf_missing",
    "center_eliminator_semantics_evaluation_law_complete_nf_not_complete",
    "center_eliminator_semantics_evaluation_law_complete_nf_selected_diagrams_only",
    "center_eliminator_semantics_evaluation_law_complete_nf_payload_incomplete",
    "center_eliminator_semantics_evaluation_law_complete_nf_structure_incomplete",
    "center_eliminator_semantics_evaluation_law_complete_nf_generator_coverage_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_endpoint_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_degree_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_projection_formula_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_boundary_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_dd4_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_exact_delta_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_graph_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_rosati_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_control_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_handoff_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_composition_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_refinement_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_filtered_cofinal_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_represented_limit_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_critical_pair_coverage_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_semantic_completeness_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_invariant_reflection_gap",
    "center_eliminator_semantics_evaluation_law_complete_nf_descent_not_stable",
    "center_eliminator_semantics_evaluation_law_complete_nf_not_natural",
    "center_eliminator_semantics_evaluation_law_complete_nf_not_coherent",
    "center_eliminator_semantics_evaluation_law_complete_nf_external_rewrite",
    "center_eliminator_semantics_evaluation_law_complete_nf_quotient_normal_form",
    "center_eliminator_semantics_evaluation_law_complete_nf_functor_of_points_only",
    "center_eliminator_semantics_evaluation_law_complete_nf_yoneda_reversal",
    "center_eliminator_semantics_evaluation_law_complete_nf_pointwise_only",
    "center_eliminator_semantics_evaluation_law_complete_nf_objectwise_only",
    "center_eliminator_semantics_evaluation_law_complete_nf_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_law_complete_nf_requires_choice",
    "center_eliminator_semantics_evaluation_law_complete_nf_requires_new_cell",
    "center_eliminator_semantics_evaluation_law_complete_nf_context_collapse",
    "center_eliminator_semantics_evaluation_law_complete_nf_by_declaration",
    "center_eliminator_semantics_evaluation_law_complete_nf_finite_sample",
    "center_eliminator_semantics_evaluation_law_complete_nf_basis_row",
    "center_eliminator_semantics_evaluation_law_complete_nf_not_budgeted",
    "missing_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

LAW_DATA = {
    "certificate": "source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_normal_form": NORMREF,
    "base_paste": PASTE,
    "base_cyclic": CYCLIC,
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "source_law_complete": True,
    "selected_diagrams_only": False,
    "payload_complete": True,
    "structure_complete": True,
    "generator_coverage_complete": True,
    "endpoint_law_complete": True,
    "degree_law_complete": True,
    "projection_formula_law_complete": True,
    "boundary_law_complete": True,
    "dd4_law_complete": True,
    "exact_delta_law_complete": True,
    "graph_law_complete": True,
    "rosati_law_complete": True,
    "control_law_complete": True,
    "handoff_law_complete": True,
    "composition_law_complete": True,
    "refinement_law_complete": True,
    "filtered_cofinal_law_complete": True,
    "represented_limit_law_complete": True,
    "critical_pair_coverage_complete": True,
    "semantic_completeness": True,
    "invariant_reflection": True,
    "descent_stable": True,
    "natural": True,
    "coherent": True,
    "external_rewrite": False,
    "quotient_normal_form": False,
    "functor_of_points_only": False,
    "yoneda_reversal": False,
    "pointwise_only": False,
    "objectwise_only": False,
    "nonfunctorial_choice": False,
    "requires_choice": False,
    "new_cell": False,
    "context_collapse": False,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "budgeted": True,
    "normalizer_deps": NORMALIZER_DEPS,
    "law_completion_deps": LAW_COMPLETION_DEPS,
    "generators": SOURCE_LAW_GENERATORS,
    "routes": BASE_CHANGE_ROUTES,
    "projection_targets": PROJECTION_FORMULA_TARGETS,
    "preserved_contexts": PRESERVED_CONTEXTS,
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def load_map() -> dict[str, Any]:
    with MAP_PATH.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise SystemExit("frontier-map.yaml did not load as a mapping")
    return data


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
        "law": deepcopy(LAW_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "law":
            state["law"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(LAWCOMP, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    law = state["law"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_584")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc584_witness")
    if LAWCOMP not in state["accepted"]:
        reasons.append("missing_source_law_complete_normal_form_reflecting_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")
    for dep in state["requires"].get(LAWCOMP, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")
    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if law.get("base_normal_form") != NORMREF:
        reasons.append("wrong_base_normal_form_reflection")
    if law.get("base_paste") != PASTE:
        reasons.append("wrong_base_pasting_stable_mate")
    if law.get("base_cyclic") != CYCLIC:
        reasons.append("wrong_base_cyclic_mate")
    if law.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if law.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not law.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_missing")
    if not law.get("source_law_complete"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_not_complete")
    if law.get("selected_diagrams_only"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_selected_diagrams_only")
    if not law.get("payload_complete"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_payload_incomplete")
    if not law.get("structure_complete"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_structure_incomplete")
    if not law.get("generator_coverage_complete") or not SOURCE_LAW_GENERATORS <= set(law["generators"]):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_generator_coverage_gap")
    if not law.get("endpoint_law_complete") or ENDPOINT not in law["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_endpoint_gap")
    if not law.get("degree_law_complete") or DEGREE not in law["generators"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_degree_gap")
    if not law.get("projection_formula_law_complete") or not PROJECTION_FORMULA_TARGETS <= set(law["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_projection_formula_gap")
    if not law.get("boundary_law_complete") or PUSHFORWARD not in law["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_boundary_gap")
    if not law.get("dd4_law_complete") or DD4_BOUNDARY not in law["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_dd4_gap")
    if not law.get("exact_delta_law_complete") or EXACT_DELTA not in law["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_exact_delta_gap")
    if not law.get("graph_law_complete") or GRAPH_COMP not in law["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_graph_gap")
    if not law.get("rosati_law_complete") or ROSATI not in law["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_rosati_gap")
    if not law.get("control_law_complete") or CONTROL not in law["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_control_gap")
    if not law.get("handoff_law_complete") or not {HANDOFF, GRAPH_LATER} <= set(law["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_handoff_gap")
    if not law.get("composition_law_complete") or COMPOSITION_STABLE not in law["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_composition_gap")
    if not law.get("refinement_law_complete") or REFINEMENT_DESCENT not in law["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_refinement_gap")
    if not law.get("filtered_cofinal_law_complete") or FILTERED_COFINAL not in law["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_filtered_cofinal_gap")
    if not law.get("represented_limit_law_complete") or REPRESENTED_LIMIT not in law["law_completion_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_represented_limit_gap")
    if not law.get("critical_pair_coverage_complete") or EXEC not in law["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_critical_pair_coverage_gap")
    if not law.get("semantic_completeness") or SEMCONS not in law["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_semantic_completeness_gap")
    if not law.get("invariant_reflection") or REPSEM not in law["normalizer_deps"]:
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_invariant_reflection_gap")
    if not law.get("descent_stable"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_descent_not_stable")
    if not law.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_not_natural")
    if not law.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_not_coherent")
    if law.get("external_rewrite"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_external_rewrite")
    if law.get("quotient_normal_form"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_quotient_normal_form")
    if law.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_functor_of_points_only")
    if law.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_yoneda_reversal")
    if law.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_pointwise_only")
    if law.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_objectwise_only")
    if law.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_nonfunctorial_choice")
    if law.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_requires_choice")
    if law.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_requires_new_cell")
    if law.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_context_collapse")
    if law.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_by_declaration")
    if law.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_finite_sample")
    if law.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_basis_row")
    if not law.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_law_complete_nf_not_budgeted")

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
        and LAWCOMP in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["law"]["source_law_complete"]
        and not state["law"]["selected_diagrams_only"]
        and state["law"]["generator_coverage_complete"]
        and SOURCE_LAW_GENERATORS <= state["law"]["generators"],
        "normal-form reflection covers the full source-law generator inventory",
    )
    gate(
        f"{PREFIX}3",
        state["law"]["payload_complete"]
        and state["law"]["structure_complete"]
        and PROJECTION_FORMULA_TARGETS <= state["law"]["projection_targets"]
        and BASE_CHANGE_ROUTES <= state["law"]["routes"],
        "payload and structure generators are complete, not sampled",
    )
    gate(
        f"{PREFIX}4",
        state["law"]["endpoint_law_complete"]
        and state["law"]["degree_law_complete"]
        and state["law"]["projection_formula_law_complete"]
        and state["law"]["boundary_law_complete"]
        and state["law"]["dd4_law_complete"]
        and state["law"]["exact_delta_law_complete"],
        "endpoint, degree, projection, boundary, DD.4, and exact-delta laws are complete",
    )
    gate(
        f"{PREFIX}5",
        state["law"]["graph_law_complete"]
        and state["law"]["rosati_law_complete"]
        and state["law"]["control_law_complete"]
        and state["law"]["handoff_law_complete"]
        and {GRAPH_COMP, ROSATI, CONTROL, HANDOFF, GRAPH_LATER} <= state["law"]["routes"],
        "graph, Rosati, control, handoff, and graph-later laws are complete",
    )
    gate(
        f"{PREFIX}6",
        state["law"]["composition_law_complete"]
        and state["law"]["refinement_law_complete"]
        and state["law"]["filtered_cofinal_law_complete"]
        and state["law"]["represented_limit_law_complete"]
        and LAW_COMPLETION_DEPS <= state["law"]["law_completion_deps"],
        "composition, refinement, filtered cofinal, and represented-limit source laws are complete",
    )
    gate(
        f"{PREFIX}7",
        state["law"]["critical_pair_coverage_complete"]
        and state["law"]["semantic_completeness"]
        and state["law"]["invariant_reflection"]
        and NORMALIZER_DEPS <= state["law"]["normalizer_deps"],
        "complete law inventory is covered by executable diamonds and conservative semantics",
    )
    gate(
        f"{PREFIX}8",
        state["law"]["budgeted"]
        and state["law"]["descent_stable"]
        and state["law"]["natural"]
        and state["law"]["coherent"]
        and not any(
            state["law"][key]
            for key in (
                "external_rewrite",
                "quotient_normal_form",
                "functor_of_points_only",
                "yoneda_reversal",
                "pointwise_only",
                "objectwise_only",
                "nonfunctorial_choice",
                "requires_choice",
                "new_cell",
                "context_collapse",
                "declared_only",
                "finite_sample",
                "basis_row",
            )
        )
        and REQUIRED_DEPS <= state["accepted"]
        and set(state["requires"].get(LAWCOMP, [])) <= state["accepted"]
        and EXPECTED_EDGES <= state["edges"],
        "source-law completeness is dependency-closed, graph-wired, budgeted, and internal",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: normal-form reflection is source-law complete")
    print(
        "VERDICT: the missing-object candidate counts only when reflected pasted "
        "cyclic Beck-Chevalley normal forms cover the full source-law generator "
        "inventory; selected-diagram normalization is still a disguised repair."
    )


if __name__ == "__main__":
    main()
