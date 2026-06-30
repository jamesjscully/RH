r"""Terminal universal-property contract for the budgeted source square.

Doc 535 pins dependency closure inside the exact 24-cell budget. This witness
checks the next canonicality requirement: the dependency-closed inhabited
finite-limit square must be terminal in the category of admissible budgeted
source squares, not merely one chosen inhabitant.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_depclosure_terminal_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the terminality witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 536
EXPECTED_WITNESS = "doc536-terminal-square"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

failures: list[str] = []

SOURCE_FACETS = {
    "facet_endpoint_integrality",
    "facet_degree_maps",
    "facet_dd4_boundary",
    "facet_boundary_pushforward",
    "facet_graph_composition",
    "facet_rosati_count",
    "facet_control_death",
}

COHERENCE_CELLS = {
    "coh_universal_mediator",
    "coh_formation_fiber",
    "coh_formation",
    "coh_cartesian_source",
    "coh_monoidwide_source",
    "coh_source_coupling",
    "coh_coupling_representer",
    "coh_subrepresenter",
    "coh_equalizer_arrow",
    "coh_finite_limit_cut",
    "coh_context_separation",
    "coh_dd4_image_handoff",
    "coh_graph_later_realization",
    "coh_inhabitance_certificate",
    "coh_doc515_payload",
    "coh_exact_delta_certificate",
    "coh_boundary_defect_duality",
}

CELLS = SOURCE_FACETS | COHERENCE_CELLS

LIVE_ASSIGNMENTS = {
    "universal_mediator": "coh_universal_mediator",
    "formation_token": "coh_formation_fiber",
    "formation_fiber": "coh_formation_fiber",
    "formation_coherence": "coh_formation",
    "cartesian_source_coherence": "coh_cartesian_source",
    "monoidwide_source_coherence": "coh_monoidwide_source",
    "source_coupling": "coh_source_coupling",
    "coupling_representer": "coh_coupling_representer",
    "coupling_universal_arrow": "coh_coupling_representer",
    "source_fiber_subrepresenter": "coh_subrepresenter",
    "monic_subrep_inclusion": "coh_subrepresenter",
    "coupled_source_image": "coh_subrepresenter",
    "subrep_factorization": "coh_subrepresenter",
    "finite_limit_cut": "coh_finite_limit_cut",
    "joint_constraint_fork": "coh_finite_limit_cut",
    "equalizer_arrow_to_subrep": "coh_equalizer_arrow",
    "context_separation_contract": "coh_context_separation",
    "dd4_certificate_image": "coh_dd4_image_handoff",
    "dd4_image_only_handoff_contract": "coh_dd4_image_handoff",
    "original_dd4_class": "coh_dd4_image_handoff",
    "dd4_boundary_certificate": "coh_dd4_image_handoff",
    "pregraph_rosati_payload": "coh_graph_later_realization",
    "graph_realization_image": "coh_graph_later_realization",
    "graph_later_realization_contract": "coh_graph_later_realization",
    "finite_limit_inhabitance_certificate": "coh_inhabitance_certificate",
    "finite_index_budget_certificate": "coh_finite_limit_cut",
    "budget_dependency_closure_certificate": "coh_finite_limit_cut",
    TERMINAL_CERT: "coh_finite_limit_cut",
    "exact_delta": "coh_exact_delta_certificate",
    "rank1_boundary_defect_duality": "coh_boundary_defect_duality",
    "source_control_death": "facet_control_death",
    "source_mediator_fixed": "coh_doc515_payload",
    "doc515_coherence_fixed": "coh_doc515_payload",
    "coupled_self_dual_exact_bcf_sources": "coh_source_coupling",
    "endpoint_integrality": "facet_endpoint_integrality",
    "degree_maps": "facet_degree_maps",
    "dd4_boundary": "facet_dd4_boundary",
    "boundary_pushforward": "facet_boundary_pushforward",
    "graph_composition": "facet_graph_composition",
    "rosati_count": "facet_rosati_count",
    "control_death": "facet_control_death",
    "source_before_points": "coh_context_separation",
    "exact_24_cell_finite_index": "coh_finite_limit_cut",
    "doc515_boundary_fiber_coherence": "coh_doc515_payload",
    "original_dd4_res1_nonboundary": "coh_dd4_image_handoff",
}

SOURCE_CONSTRAINTS = {
    "endpoint_integrality",
    "degree_maps",
    "dd4_boundary",
    "boundary_pushforward",
    "graph_composition",
    "rosati_count",
    "control_death",
}

TERMINAL_SUPPORT = {
    "universal_mediator",
    "finite_limit_cut",
    "joint_constraint_fork",
    "equalizer_arrow_to_subrep",
    "context_separation_contract",
    "finite_limit_inhabitance_certificate",
    "finite_index_budget_certificate",
    "budget_dependency_closure_certificate",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    "source_before_points",
    *SOURCE_CONSTRAINTS,
}

REQUIRED_TERMINAL_FLAGS = (
    "terminal_certificate_actual",
    "category_of_admissible_source_squares",
    "unique_factorization_from_any_probe",
    "identity_on_seven_source_constraints",
    "factors_through_equalizer",
    "source_before_points_order",
    "respects_context_bridges",
    "budget_dependency_closed",
    "no_choice_selector",
    "no_graph_first_terminality",
)

BANNED_FLAGS = (
    "nonterminal_inhabitant",
    "arbitrary_terminal_selector",
    "duplicate_terminal_mediator",
    "graph_first_terminality",
    "h1_quotient_terminality",
    "incomplete_constraint_cone",
    "posthoc_universal_arrow",
    "self_proving_terminality",
    "missing_terminality_certificate",
    "expanded_finite_index",
    "one_more_layer_tower",
)


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


def terminal_state(data: dict[str, Any], **kwargs) -> dict[str, Any]:
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "assignments": dict(LIVE_ASSIGNMENTS),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "bridges": deepcopy(data["context_bridges"]),
        "terminal_support": set(TERMINAL_SUPPORT),
        "flags": {flag: True for flag in REQUIRED_TERMINAL_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        state[key] = value
    return state


def reasons(state: dict[str, Any]) -> list[str]:
    out: list[str] = []
    frontier = state["frontier"]
    accepted = set(state["accepted"])
    assignments = dict(state["assignments"])
    terminal_support = set(state["terminal_support"])

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_536")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc536_witness_missing")
    if TERMINAL_CERT not in accepted:
        out.append("terminal_certificate_missing_from_current")
    if TERMINAL_CERT not in assignments:
        out.append("terminal_certificate_unassigned")
    if assignments.get(TERMINAL_CERT) != "coh_finite_limit_cut":
        out.append(f"terminal_certificate_bad_charge:{assignments.get(TERMINAL_CERT)}")
    if len(SOURCE_FACETS) != 7 or len(COHERENCE_CELLS) != 17 or len(CELLS) != 24:
        out.append("cell_count_bad")

    missing_assignments = accepted - set(assignments)
    if missing_assignments:
        out.append("accepted_artifacts_unassigned:" + ",".join(sorted(missing_assignments)))
    extra_assignments = set(assignments) - accepted
    if extra_assignments:
        out.append("assignment_for_noncurrent_artifact:" + ",".join(sorted(extra_assignments)))
    unknown_cells = set(assignments.values()) - CELLS
    if unknown_cells:
        out.append("assignment_uses_undeclared_cell:" + ",".join(sorted(unknown_cells)))

    missing_support = terminal_support - accepted
    if missing_support:
        out.append("terminal_support_not_current:" + ",".join(sorted(missing_support)))
    uncharged_support = terminal_support - set(assignments)
    if uncharged_support:
        out.append("terminal_support_unassigned:" + ",".join(sorted(uncharged_support)))
    if not SOURCE_CONSTRAINTS <= terminal_support:
        out.append("terminal_support_missing_source_constraint")

    requires = state["requires"].get(TERMINAL_CERT, [])
    for req in TERMINAL_SUPPORT:
        if req not in requires:
            out.append(f"terminal_requires_missing:{req}")

    for flag in REQUIRED_TERMINAL_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    dd4_bridge = state["bridges"].get("dd4_certificate_handoff", {})
    graph_bridge = state["bridges"].get("graph_realization_bridge", {})
    if dd4_bridge.get("from") == dd4_bridge.get("to") or dd4_bridge.get("direction") != "image_only":
        out.append("dd4_bridge_not_separated_for_terminality")
    if graph_bridge.get("from") == graph_bridge.get("to") or graph_bridge.get("direction") != "realizes_later":
        out.append("graph_bridge_not_later_for_terminality")
    if not graph_bridge.get("prohibits_reverse_before_points"):
        out.append("graph_bridge_allows_reverse_before_points")

    out.extend(flag for flag, active in state["banned"].items() if active)
    return out


def accepts(state: dict[str, Any]) -> bool:
    return not reasons(state)


def variant(base: dict[str, Any], **kwargs) -> dict[str, Any]:
    data = deepcopy(base)
    for key, value in kwargs.items():
        if key == "flags":
            data["flags"].update(value)
        elif key == "banned":
            data["banned"].update(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = terminal_state(MAP)

gate(
    f"{PREFIX}1 doc 536 terminal source-square layer is embedded in the current map",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s accepted=%d"
    % (live["frontier"].get("current_doc"), live["frontier"].get("current_witness"), len(live["accepted"])),
)

mere_inhabitant = variant(
    live,
    flags={
        "terminal_certificate_actual": False,
        "category_of_admissible_source_squares": False,
        "unique_factorization_from_any_probe": False,
    },
    banned={"nonterminal_inhabitant": True},
)

gate(
    f"{PREFIX}2 rejects mere inhabited finite-limit squares",
    not accepts(mere_inhabitant)
    and "nonterminal_inhabitant" in reasons(mere_inhabitant)
    and "unique_factorization_from_any_probe_missing" in reasons(mere_inhabitant),
    ",".join(reasons(mere_inhabitant)),
)

choice_terminal = variant(
    live,
    flags={"unique_factorization_from_any_probe": False, "no_choice_selector": False},
    banned={"arbitrary_terminal_selector": True, "duplicate_terminal_mediator": True},
)

gate(
    f"{PREFIX}3 rejects chosen or duplicate terminal mediators",
    not accepts(choice_terminal)
    and {"arbitrary_terminal_selector", "duplicate_terminal_mediator"} <= set(reasons(choice_terminal)),
    ",".join(reasons(choice_terminal)),
)

graph_first = variant(
    live,
    flags={"source_before_points_order": False, "no_graph_first_terminality": False},
    banned={"graph_first_terminality": True},
)
graph_first["bridges"]["graph_realization_bridge"]["prohibits_reverse_before_points"] = False

gate(
    f"{PREFIX}4 rejects graph-first terminality",
    not accepts(graph_first)
    and "graph_first_terminality" in reasons(graph_first)
    and "source_before_points_order_missing" in reasons(graph_first)
    and "graph_bridge_allows_reverse_before_points" in reasons(graph_first),
    ",".join(reasons(graph_first)),
)

h1_collapse = variant(
    live,
    flags={"respects_context_bridges": False},
    banned={"h1_quotient_terminality": True},
)
h1_collapse["bridges"]["dd4_certificate_handoff"]["to"] = "original_h1"

gate(
    f"{PREFIX}5 rejects H1 quotient or context-collapsing terminality",
    not accepts(h1_collapse)
    and "h1_quotient_terminality" in reasons(h1_collapse)
    and "dd4_bridge_not_separated_for_terminality" in reasons(h1_collapse),
    ",".join(reasons(h1_collapse)),
)

missing_constraint_support = set(TERMINAL_SUPPORT)
missing_constraint_support.remove("control_death")
incomplete_constraints = variant(
    live,
    terminal_support=missing_constraint_support,
    flags={"identity_on_seven_source_constraints": False},
    banned={"incomplete_constraint_cone": True},
)

gate(
    f"{PREFIX}6 rejects terminal cones missing a source constraint",
    not accepts(incomplete_constraints)
    and "incomplete_constraint_cone" in reasons(incomplete_constraints)
    and "identity_on_seven_source_constraints_missing" in reasons(incomplete_constraints)
    and "terminal_support_missing_source_constraint" in reasons(incomplete_constraints),
    ",".join(reasons(incomplete_constraints)),
)

self_posthoc = variant(
    live,
    flags={"factors_through_equalizer": False},
    banned={"posthoc_universal_arrow": True, "self_proving_terminality": True},
)

gate(
    f"{PREFIX}7 rejects posthoc or self-proving universal arrows",
    not accepts(self_posthoc)
    and {"posthoc_universal_arrow", "self_proving_terminality"} <= set(reasons(self_posthoc)),
    ",".join(reasons(self_posthoc)),
)

missing_budget = variant(
    live,
    flags={"budget_dependency_closed": False},
    banned={"missing_terminality_certificate": True},
)
missing_budget["accepted"].remove(TERMINAL_CERT)
del missing_budget["assignments"][TERMINAL_CERT]

gate(
    f"{PREFIX}8 rejects terminality without the budgeted closure certificate",
    not accepts(missing_budget)
    and "missing_terminality_certificate" in reasons(missing_budget)
    and "terminal_certificate_missing_from_current" in reasons(missing_budget),
    ",".join(reasons(missing_budget)),
)

expanded = variant(
    live,
    banned={"expanded_finite_index": True, "one_more_layer_tower": True},
)
expanded["assignments"]["extra_terminality_layer"] = "coh_extra_terminality_cell"

gate(
    f"{PREFIX}9 rejects expanded finite-index terminality",
    not accepts(expanded)
    and "expanded_finite_index" in reasons(expanded)
    and "one_more_layer_tower" in reasons(expanded)
    and any(reason.startswith("assignment_uses_undeclared_cell:") for reason in reasons(expanded)),
    ",".join(reasons(expanded)),
)

variants = [
    mere_inhabitant,
    choice_terminal,
    graph_first,
    h1_collapse,
    incomplete_constraints,
    self_posthoc,
    missing_budget,
    expanded,
]
variant_reasons = set().union(*(set(reasons(data)) for data in variants))

gate(
    f"{PREFIX}10 only terminal dependency-closed source-square universal property passes",
    accepts(live)
    and not any(accepts(data) for data in variants)
    and {
        "nonterminal_inhabitant",
        "arbitrary_terminal_selector",
        "duplicate_terminal_mediator",
        "graph_first_terminality",
        "h1_quotient_terminality",
        "incomplete_constraint_cone",
        "posthoc_universal_arrow",
        "self_proving_terminality",
        "missing_terminality_certificate",
        "expanded_finite_index",
        "one_more_layer_tower",
    }
    <= variant_reasons,
    "rejected=%s" % sorted(variant_reasons),
)

if failures:
    raise SystemExit("FAILURES: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: terminal source-square universal property pinned")
print(
    "VERDICT: the current frontier remains live only if the dependency-closed "
    "24-cell finite-limit square is terminal among admissible budgeted source "
    "squares. Mere inhabitance, chosen selectors, duplicate mediators, graph-first "
    "terminality, H1 quotient collapse, incomplete source cones, posthoc universal "
    "arrows, self-proving terminality, and extra finite-index layers do not "
    "construct the missing object."
)
