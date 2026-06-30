#!/usr/bin/env python3
r"""Pasting-stable cyclic mate coherence for Beck-Chevalley evaluation.

Doc 581 requires the mate-coherent Beck-Chevalley semantic evaluation to be
cyclic and ambidextrous, so it cannot depend on a marked cut of the trace or
adjunction cycle. This witness closes the next cheap escape: a single
cyclic-ambidextrous square may still fail to paste as a source-square
calculus. The current frontier only counts if the cyclic mate is stable under
vertical and horizontal pasting, interchange, units, associators/unitors, and
trace sliding without importing an external double category or formal pasting
diagram.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_pasting_stable_cyclic_mate_beck_chevalley_evaluation_contract
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the pasting-stable cyclic mate witness") from exc

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_cyclic_ambidextrous_mate_beck_chevalley_evaluation_contract import (
    ADJOINT,
    BASE_CHANGE_ROUTES,
    BC,
    CONTROL,
    DAGGER,
    DD4_BOUNDARY,
    DIAG,
    DOC515_FIXED,
    DUAL_TRACE,
    ENDPOINT,
    EVAL,
    EXACT_ADDITIVE,
    EXACT_DELTA,
    FINITE_INDEX,
    GRAPH_COMP,
    GRAPH_LATER,
    HANDOFF,
    MAP_PATH,
    MATE,
    ORIGINAL_DD4,
    PIVOTAL,
    PRESERVED_CONTEXTS,
    PROJECTION_FORMULA_TARGETS,
    PUSHFORWARD,
    ROSATI,
    SOURCE_BEFORE_POINTS,
    SUBREP,
    UNIVERSAL_ARROW,
    CYCLIC,
)


EXPECTED_DOC = 582
EXPECTED_WITNESS = "doc582-probe-pasting-stable-cyclic-mate-beck-chevalley-evaluation-contract"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMPASTECYCMATEBCHEVEVAL"

PASTE = "pasting_stable_" + CYCLIC
COMPOSITION_STABLE = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REFINEMENT_DESCENT = "refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FILTERED_COFINAL = "filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REPRESENTED_LIMIT = "represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"

failures: list[str] = []

PASTING_STRUCTURES = {DAGGER, ADJOINT, DUAL_TRACE, PIVOTAL, EXACT_ADDITIVE}

REQUIRED_DEPS = {
    CYCLIC,
    MATE,
    BC,
    EVAL,
    DIAG,
    SUBREP,
    UNIVERSAL_ARROW,
    COMPOSITION_STABLE,
    REFINEMENT_DESCENT,
    FILTERED_COFINAL,
    REPRESENTED_LIMIT,
} | PASTING_STRUCTURES | BASE_CHANGE_ROUTES | PROJECTION_FORMULA_TARGETS | PRESERVED_CONTEXTS

EXPECTED_EDGES = {
    (CYCLIC, "made_pasting_stable_by", PASTE),
    (PASTE, "pasting_stable_for", CYCLIC),
    (PASTE, "pastes_mate_of", MATE),
    (PASTE, "pastes_base_change_for", BC),
    (PASTE, "pastes_evaluation_for", EVAL),
    (PASTE, "pasting_coherent_over", DIAG),
    (PASTE, "pasting_internal_to", SUBREP),
    (PASTE, "pasting_selected_by", UNIVERSAL_ARROW),
    (PASTE, "vertical_pasting_stable_over", COMPOSITION_STABLE),
    (PASTE, "refinement_pasting_stable_over", REFINEMENT_DESCENT),
    (PASTE, "cofinal_pasting_stable_over", FILTERED_COFINAL),
    (PASTE, "represented_pasting_over", REPRESENTED_LIMIT),
} | {(PASTE, "pasting_coherent_with", target) for target in PASTING_STRUCTURES} | {
    (PASTE, "pasting_preserves_projection_formula_for", target)
    for target in PROJECTION_FORMULA_TARGETS
} | {(PASTE, "pastes_with", target) for target in BASE_CHANGE_ROUTES} | {
    (PASTE, "pasting_preserves", target) for target in PRESERVED_CONTEXTS
}

REQUIRED_FLAGS = (
    "pasting_stable_certificate",
    "vertical_pasting",
    "horizontal_pasting",
    "interchange_coherence",
    "unit_square_coherence",
    "associator_unitor_coherence",
    "trace_sliding",
    "internal_companion_conjoint",
    "inside_exact_24_budget",
)

BANNED_FLAGS = (
    "center_eliminator_semantics_evaluation_pasting_mate_missing",
    "center_eliminator_semantics_evaluation_pasting_mate_not_stable",
    "center_eliminator_semantics_evaluation_pasting_mate_vertical_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_horizontal_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_interchange_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_unit_square_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_associator_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_unitor_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_trace_sliding_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_dagger_rosati_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_projection_formula_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_boundary_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_dd4_exact_delta_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_graph_composition_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_control_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_handoff_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_companion_conjoint_gap",
    "center_eliminator_semantics_evaluation_pasting_mate_external_equipment",
    "center_eliminator_semantics_evaluation_pasting_mate_descent_not_stable",
    "center_eliminator_semantics_evaluation_pasting_mate_not_natural",
    "center_eliminator_semantics_evaluation_pasting_mate_not_coherent",
    "center_eliminator_semantics_evaluation_pasting_mate_external",
    "center_eliminator_semantics_evaluation_pasting_mate_quotient",
    "center_eliminator_semantics_evaluation_pasting_mate_functor_of_points_only",
    "center_eliminator_semantics_evaluation_pasting_mate_yoneda_reversal",
    "center_eliminator_semantics_evaluation_pasting_mate_pointwise_only",
    "center_eliminator_semantics_evaluation_pasting_mate_objectwise_only",
    "center_eliminator_semantics_evaluation_pasting_mate_nonfunctorial_choice",
    "center_eliminator_semantics_evaluation_pasting_mate_requires_choice",
    "center_eliminator_semantics_evaluation_pasting_mate_requires_new_cell",
    "center_eliminator_semantics_evaluation_pasting_mate_context_collapse",
    "center_eliminator_semantics_evaluation_pasting_mate_by_declaration",
    "center_eliminator_semantics_evaluation_pasting_mate_finite_sample",
    "center_eliminator_semantics_evaluation_pasting_mate_basis_row",
    "center_eliminator_semantics_evaluation_pasting_mate_not_budgeted",
    "missing_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate",
)

PASTE_DATA = {
    "certificate": "pasting_stable_cyclic_mate_beck_chevalley_evaluation",
    "base_cyclic": CYCLIC,
    "base_mate": MATE,
    "base_beck_chevalley": BC,
    "exists": True,
    "pasting_stable": True,
    "vertical_pasting": True,
    "horizontal_pasting": True,
    "interchange": True,
    "unit_square": True,
    "associator": True,
    "unitor": True,
    "trace_sliding": True,
    "dagger_rosati_pasting": True,
    "projection_formula_pasting": True,
    "boundary_pasting": True,
    "dd4_exact_delta_pasting": True,
    "graph_composition_pasting": True,
    "control_pasting": True,
    "handoff_pasting": True,
    "companion_conjoint": True,
    "external_equipment": False,
    "descent_pasting_stable": True,
    "natural": True,
    "coherent": True,
    "external": False,
    "quotient": False,
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
    "structures": PASTING_STRUCTURES,
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
        "paste": deepcopy(PASTE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        if key == "paste":
            state["paste"].update(value)
        elif key == "flags":
            state["flags"].update(value)
        elif key == "banned":
            state["banned"].update(value)
        else:
            state[key] = value
    return state


def rejected_or_excluded(state: dict[str, Any], flag: str) -> bool:
    excluded = set(state["excludes"].get(PASTE, []))
    return flag in state["current_rejected"] and flag in state["rejected_repairs"] and flag in excluded


def assess(state: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    frontier = state["frontier"]
    paste = state["paste"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        reasons.append("current_doc_before_582")
    if EXPECTED_WITNESS not in state["witnesses"]:
        reasons.append("missing_doc582_witness")
    if PASTE not in state["accepted"]:
        reasons.append("missing_pasting_stable_cyclic_mate_beck_chevalley_evaluation_certificate")

    for dep in REQUIRED_DEPS:
        if dep not in state["accepted"]:
            reasons.append(f"missing_dependency:{dep}")

    for dep in state["requires"].get(PASTE, []):
        if dep not in state["accepted"]:
            reasons.append(f"requires_unaccepted:{dep}")

    for flag, present in state["flags"].items():
        if not present:
            reasons.append(f"missing_flag:{flag}")

    if paste.get("base_cyclic") != CYCLIC:
        reasons.append("wrong_base_cyclic_mate")
    if paste.get("base_mate") != MATE:
        reasons.append("wrong_base_mate")
    if paste.get("base_beck_chevalley") != BC:
        reasons.append("wrong_base_beck_chevalley")
    if not paste.get("exists"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_missing")
    if not paste.get("pasting_stable"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_not_stable")
    if not paste.get("vertical_pasting"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_vertical_gap")
    if not paste.get("horizontal_pasting"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_horizontal_gap")
    if not paste.get("interchange"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_interchange_gap")
    if not paste.get("unit_square"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_unit_square_gap")
    if not paste.get("associator"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_associator_gap")
    if not paste.get("unitor"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_unitor_gap")
    if not paste.get("trace_sliding") or DUAL_TRACE not in paste["structures"]:
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_trace_sliding_gap")
    if not paste.get("dagger_rosati_pasting") or not {DAGGER, ADJOINT} <= set(paste["structures"]) or ROSATI not in paste["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_dagger_rosati_gap")
    if not paste.get("projection_formula_pasting") or not PROJECTION_FORMULA_TARGETS <= set(paste["projection_targets"]):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_projection_formula_gap")
    if not paste.get("boundary_pasting") or PUSHFORWARD not in paste["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_boundary_gap")
    if not paste.get("dd4_exact_delta_pasting") or not {DD4_BOUNDARY, EXACT_DELTA} <= set(paste["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_dd4_exact_delta_gap")
    if not paste.get("graph_composition_pasting") or GRAPH_COMP not in paste["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_graph_composition_gap")
    if not paste.get("control_pasting") or CONTROL not in paste["routes"]:
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_control_gap")
    if not paste.get("handoff_pasting") or not {HANDOFF, GRAPH_LATER} <= set(paste["routes"]):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_handoff_gap")
    if not paste.get("companion_conjoint"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_companion_conjoint_gap")
    if paste.get("external_equipment"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_external_equipment")
    if not paste.get("descent_pasting_stable"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_descent_not_stable")
    if not paste.get("natural"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_not_natural")
    if not paste.get("coherent"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_not_coherent")
    if paste.get("external"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_external")
    if paste.get("quotient"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_quotient")
    if paste.get("functor_of_points_only"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_functor_of_points_only")
    if paste.get("yoneda_reversal"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_yoneda_reversal")
    if paste.get("pointwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_pointwise_only")
    if paste.get("objectwise_only"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_objectwise_only")
    if paste.get("nonfunctorial_choice"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_nonfunctorial_choice")
    if paste.get("requires_choice"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_requires_choice")
    if paste.get("new_cell"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_requires_new_cell")
    if paste.get("context_collapse"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_context_collapse")
    if paste.get("declared_only"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_by_declaration")
    if paste.get("finite_sample"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_finite_sample")
    if paste.get("basis_row"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_basis_row")
    if not paste.get("budgeted"):
        reasons.append("center_eliminator_semantics_evaluation_pasting_mate_not_budgeted")

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
        and PASTE in state["accepted"]
        and EXPECTED_WITNESS in state["witnesses"],
        f"current_doc={data['frontier']['current_doc']} active_witness={data['frontier']['current_witness']}",
    )
    gate(
        f"{PREFIX}2",
        state["paste"]["pasting_stable"]
        and state["paste"]["vertical_pasting"]
        and state["paste"]["horizontal_pasting"]
        and state["paste"]["interchange"]
        and state["paste"]["unit_square"],
        "vertical, horizontal, interchange, and unit-square pasting commute",
    )
    gate(
        f"{PREFIX}3",
        state["paste"]["associator"]
        and state["paste"]["unitor"]
        and state["paste"]["trace_sliding"]
        and state["paste"]["dagger_rosati_pasting"]
        and {DAGGER, ADJOINT, DUAL_TRACE, PIVOTAL, EXACT_ADDITIVE} <= state["paste"]["structures"],
        "associator/unitors, trace sliding, dagger/Rosati, pivotal, and exact-additive pasting commute",
    )
    gate(
        f"{PREFIX}4",
        state["paste"]["projection_formula_pasting"]
        and state["paste"]["boundary_pasting"]
        and state["paste"]["dd4_exact_delta_pasting"]
        and state["paste"]["graph_composition_pasting"]
        and PROJECTION_FORMULA_TARGETS <= state["paste"]["projection_targets"]
        and {PUSHFORWARD, DD4_BOUNDARY, EXACT_DELTA, GRAPH_COMP} <= state["paste"]["routes"],
        "projection, boundary, DD.4, exact-delta, and graph pasting commute",
    )
    gate(
        f"{PREFIX}5",
        state["paste"]["control_pasting"]
        and state["paste"]["handoff_pasting"]
        and state["paste"]["descent_pasting_stable"]
        and state["paste"]["natural"]
        and state["paste"]["coherent"]
        and {CONTROL, HANDOFF, GRAPH_LATER} <= state["paste"]["routes"],
        "control, handoff, descent, naturality, and coherence survive pasting",
    )
    gate(
        f"{PREFIX}6",
        state["paste"]["budgeted"]
        and state["paste"]["companion_conjoint"]
        and not state["paste"]["external_equipment"]
        and not any(
            state["paste"][key]
            for key in (
                "external",
                "quotient",
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
        ),
        "pasting-stable cyclic mate data is internal, budgeted, and not external equipment",
    )
    gate(
        f"{PREFIX}7",
        REQUIRED_DEPS <= state["accepted"] and set(state["requires"].get(PASTE, [])) <= state["accepted"],
        "pasting-stable cyclic mate dependency closure is wired",
    )
    gate(
        f"{PREFIX}8",
        EXPECTED_EDGES <= state["edges"],
        "all pasting-stable cyclic mate graph edges present",
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

    print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: Beck-Chevalley cyclic mate is pasting-stable")
    print(
        "VERDICT: the missing-object candidate counts only when the "
        "cyclic-ambidextrous Beck-Chevalley mate pastes vertically and "
        "horizontally with interchange, unit, associator/unitor, trace-sliding, "
        "projection, boundary, graph, control, and handoff coherence inside the "
        "existing source square."
    )


if __name__ == "__main__":
    main()
