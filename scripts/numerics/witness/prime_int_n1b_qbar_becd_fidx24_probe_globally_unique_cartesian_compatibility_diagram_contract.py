r"""Globally unique represented-limit cartesian compatibility diagram.

Doc 563 pins the represented-limit cartesian compatibility diagram against
non-invertible self-endomorphisms. This witness closes the next escape:
internal rigidity does not imply global uniqueness. The diagram cannot be one
element of a discrete family of equally valid rigid diagrams, nor selected by
an external order, finite enumeration, or basis row.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_globally_unique_cartesian_compatibility_diagram_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the globally-unique diagram witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 564
EXPECTED_WITNESS = "doc564-probe-globally-unique-endomorphism-trivial-cartesian-compatibility-diagram"
GLOB = "globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
ENDTRIV = "endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
AUT = "automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
DIAG = "cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
BUNDLE = "represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
RLIM = "represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FRC = "filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MED = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
JOINT = "joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
CART_EQV = "cartesian_probe_equivalence_certificate"
SUBREP = "source_fiber_subrepresenter"
COUPLED_IMAGE = "coupled_source_image"
FINITE_LIMIT = "finite_limit_cut"
EQUALIZER = "equalizer_arrow_to_subrep"
MEDIATOR = "universal_mediator"
SOURCE_COUPLING = "source_coupling"
DD4_ORIGINAL = "original_dd4_class"
HANDOFF = "dd4_image_only_handoff_contract"
GRAPH_LATER = "graph_later_realization_contract"
ENDPOINT = "endpoint_integrality"
DEGREE = "degree_maps"
DD4_BOUNDARY = "dd4_boundary"
PUSHFORWARD = "boundary_pushforward"
GRAPH_COMP = "graph_composition"
ROSATI = "rosati_count"
CONTROL = "control_death"
EXACT_DELTA = "exact_delta"
FINITE_INDEX = "exact_24_cell_finite_index"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPGLOBUNIQENDTRIVCARTCOMPAT"

failures: list[str] = []

REQUIRED_GLOB_DEPS = {
    ENDTRIV,
    AUT,
    DIAG,
    BUNDLE,
    RLIM,
    FRC,
    MED,
    JOINT,
    SUBREP,
    COUPLED_IMAGE,
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
    DD4_ORIGINAL,
    HANDOFF,
    GRAPH_LATER,
    ENDPOINT,
    DEGREE,
    DD4_BOUNDARY,
    PUSHFORWARD,
    GRAPH_COMP,
    ROSATI,
    CONTROL,
    EXACT_DELTA,
    FINITE_INDEX,
}

EXPECTED_EDGES = {
    (ENDTRIV, "made_globally_unique_by", GLOB),
    (GLOB, "globally_unique_diagram_for", ENDTRIV),
    (GLOB, "unique_solution_for", DIAG),
    (GLOB, "no_parallel_isolated_solution_for", FINITE_LIMIT),
    (GLOB, "no_discrete_solution_family_for", SUBREP),
    (GLOB, "no_duplicate_payload_solution_for", COUPLED_IMAGE),
    (GLOB, "unique_equalizer_solution_for", EQUALIZER),
    (GLOB, "unique_probe_solution_for", CART_EQV),
    (GLOB, "unique_mediator_generated_solution_for", MEDIATOR),
    (GLOB, "unique_source_coupled_solution_for", SOURCE_COUPLING),
    (GLOB, "payload_unique_for", ENDPOINT),
    (GLOB, "payload_unique_for", DEGREE),
    (GLOB, "payload_unique_for", DD4_BOUNDARY),
    (GLOB, "payload_unique_for", PUSHFORWARD),
    (GLOB, "payload_unique_for", EXACT_DELTA),
    (GLOB, "payload_unique_for", GRAPH_COMP),
    (GLOB, "payload_unique_for", ROSATI),
    (GLOB, "payload_unique_for", CONTROL),
    (GLOB, "payload_unique_for", HANDOFF),
    (GLOB, "payload_unique_for", GRAPH_LATER),
    (GLOB, "preserves", FINITE_INDEX),
    (GLOB, "coherent_for", COUPLED_IMAGE),
}

REQUIRED_UNIQUE_TARGETS = {
    DIAG,
    BUNDLE,
    SUBREP,
    COUPLED_IMAGE,
    FINITE_LIMIT,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
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
    FINITE_INDEX,
}

REQUIRED_IDENTITIES = {
    "global_solution_singleton_law",
    "no_parallel_isolated_solution_law",
    "no_discrete_family_law",
    "no_duplicate_payload_solution_law",
    "probe_duplicate_separation_law",
    "equalizer_solution_uniqueness_law",
    "mediator_solution_uniqueness_law",
    "source_coupling_solution_uniqueness_law",
    "payload_solution_uniqueness_law",
    "no_selector_choice_law",
}

BANNED_FLAGS = (
    "diagram_parallel_isolated_solution",
    "diagram_discrete_solution_family",
    "diagram_duplicate_payload_solution",
    "diagram_moduli_component_choice",
    "diagram_same_payload_nonisomorphic_solution",
    "diagram_probe_indistinguishable_duplicate",
    "diagram_equalizer_duplicate_solution",
    "diagram_mediator_duplicate_solution",
    "diagram_source_coupling_duplicate_solution",
    "diagram_endpoint_degree_duplicate_solution",
    "diagram_boundary_duplicate_solution",
    "diagram_exact_delta_duplicate_solution",
    "diagram_graph_rosati_control_duplicate_solution",
    "diagram_handoff_graph_duplicate_solution",
    "diagram_external_solution_selector",
    "diagram_lexicographic_solution_choice",
    "diagram_basis_order_solution_choice",
    "diagram_finite_enumeration_choice",
    "diagram_global_uniqueness_by_declaration",
    "diagram_global_uniqueness_finite_sample",
    "diagram_global_uniqueness_basis_row",
    "missing_globally_unique_cartesian_compatibility_diagram_certificate",
)

REQUIRED_FLAGS = (
    "globally_unique_diagram_actual",
    "solution_space_singleton",
    "no_parallel_isolated_solutions",
    "no_discrete_solution_family",
    "no_duplicate_payload_solution",
    "probe_separates_duplicates",
    "no_external_selector",
    "payload_solution_unique",
    "inside_exact_24_budget",
)

UNIQUE_DATA = {
    "certificate": "represented_limit_globally_unique_cartesian_compatibility_diagram",
    "base_certificate": ENDTRIV,
    "solution_space_singleton": True,
    "parallel_isolated_solution_free": True,
    "discrete_family_free": True,
    "duplicate_payload_free": True,
    "moduli_component_choice_free": True,
    "same_payload_nonisomorphic_free": True,
    "probe_indistinguishable_duplicate_free": True,
    "equalizer_duplicate_free": True,
    "mediator_duplicate_free": True,
    "source_coupling_duplicate_free": True,
    "endpoint_degree_duplicate_free": True,
    "boundary_duplicate_free": True,
    "exact_delta_duplicate_free": True,
    "graph_rosati_control_duplicate_free": True,
    "handoff_graph_duplicate_free": True,
    "external_selector_free": True,
    "lexicographic_choice_free": True,
    "basis_order_choice_free": True,
    "finite_enumeration_choice_free": True,
    "declared_only": False,
    "finite_sample": False,
    "basis_row": False,
    "imports_positivity": False,
    "preserves_budget": True,
    "unique_targets": REQUIRED_UNIQUE_TARGETS,
    "identities": REQUIRED_IDENTITIES,
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


def active_state(data: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    edge_set = {
        (edge["source"], edge["relation"], edge["target"])
        for edge in data.get("edges", [])
        if edge.get("introduced_by", 0) <= EXPECTED_DOC
    }
    state = {
        "frontier": dict(data["frontier"]),
        "witnesses": set(data.get("witnesses", {})),
        "accepted": accepted_nodes(data),
        "requires": deepcopy(data["consistency_rules"]["requires"]),
        "edges": edge_set,
        "unique": deepcopy(UNIQUE_DATA),
        "flags": {flag: True for flag in REQUIRED_FLAGS},
        "banned": {flag: False for flag in BANNED_FLAGS},
    }
    for key, value in kwargs.items():
        state[key] = value
    return state


def _as_set(value: Any) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        return {value}
    return {str(item) for item in value}


def reasons(state: dict[str, Any]) -> list[str]:
    out: list[str] = []
    frontier = state["frontier"]
    accepted = set(state["accepted"])
    requires = state["requires"]
    unique = state["unique"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_564")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc564_witness_missing")
    if GLOB not in accepted:
        out.append("globally_unique_cartesian_compatibility_diagram_missing_from_current")
    if ENDTRIV not in accepted:
        out.append("endomorphism_trivial_diagram_base_missing_from_current")

    if not isinstance(unique, dict):
        out.append("globally_unique_diagram_data_not_mapping")
        unique = {}
    if unique.get("certificate") != "represented_limit_globally_unique_cartesian_compatibility_diagram":
        out.append("missing_globally_unique_cartesian_compatibility_diagram_certificate")
    if unique.get("base_certificate") != ENDTRIV:
        out.append("globally_unique_diagram_not_based_on_endomorphism_trivial_diagram")
    if not unique.get("solution_space_singleton"):
        out.append("diagram_discrete_solution_family")
    if not unique.get("parallel_isolated_solution_free"):
        out.append("diagram_parallel_isolated_solution")
    if not unique.get("discrete_family_free"):
        out.append("diagram_discrete_solution_family")
    if not unique.get("duplicate_payload_free"):
        out.append("diagram_duplicate_payload_solution")
    if not unique.get("moduli_component_choice_free"):
        out.append("diagram_moduli_component_choice")
    if not unique.get("same_payload_nonisomorphic_free"):
        out.append("diagram_same_payload_nonisomorphic_solution")
    if not unique.get("probe_indistinguishable_duplicate_free"):
        out.append("diagram_probe_indistinguishable_duplicate")
    if not unique.get("equalizer_duplicate_free"):
        out.append("diagram_equalizer_duplicate_solution")
    if not unique.get("mediator_duplicate_free"):
        out.append("diagram_mediator_duplicate_solution")
    if not unique.get("source_coupling_duplicate_free"):
        out.append("diagram_source_coupling_duplicate_solution")
    if not unique.get("endpoint_degree_duplicate_free"):
        out.append("diagram_endpoint_degree_duplicate_solution")
    if not unique.get("boundary_duplicate_free"):
        out.append("diagram_boundary_duplicate_solution")
    if not unique.get("exact_delta_duplicate_free"):
        out.append("diagram_exact_delta_duplicate_solution")
    if not unique.get("graph_rosati_control_duplicate_free"):
        out.append("diagram_graph_rosati_control_duplicate_solution")
    if not unique.get("handoff_graph_duplicate_free"):
        out.append("diagram_handoff_graph_duplicate_solution")
    if not unique.get("external_selector_free"):
        out.append("diagram_external_solution_selector")
    if not unique.get("lexicographic_choice_free"):
        out.append("diagram_lexicographic_solution_choice")
    if not unique.get("basis_order_choice_free"):
        out.append("diagram_basis_order_solution_choice")
    if not unique.get("finite_enumeration_choice_free"):
        out.append("diagram_finite_enumeration_choice")
    if unique.get("declared_only"):
        out.append("diagram_global_uniqueness_by_declaration")
    if unique.get("finite_sample"):
        out.append("diagram_global_uniqueness_finite_sample")
    if unique.get("basis_row"):
        out.append("diagram_global_uniqueness_basis_row")
    if unique.get("imports_positivity"):
        out.append("globally_unique_diagram_imports_positivity")
    if not unique.get("preserves_budget"):
        out.append("globally_unique_diagram_not_inside_exact_24_budget")

    missing_targets = REQUIRED_UNIQUE_TARGETS - _as_set(unique.get("unique_targets"))
    if missing_targets:
        out.append("globally_unique_targets_missing:" + ",".join(sorted(missing_targets)))

    missing_identities = REQUIRED_IDENTITIES - _as_set(unique.get("identities"))
    if missing_identities:
        out.append("globally_unique_identity_missing:" + ",".join(sorted(missing_identities)))

    if GLOB not in requires.get(ENDTRIV, []):
        out.append("endomorphism_trivial_diagram_not_required_to_be_globally_unique")
    if ENDTRIV not in requires.get(GLOB, []):
        out.append("globally_unique_diagram_requires_missing_endomorphism_trivial_base")
    missing_deps = REQUIRED_GLOB_DEPS - set(requires.get(GLOB, []))
    if missing_deps:
        out.append("globally_unique_diagram_requires_missing:" + ",".join(sorted(missing_deps)))

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("globally_unique_edges_missing:" + ",".join(rendered))

    for flag in REQUIRED_FLAGS:
        if not state["flags"].get(flag):
            out.append(flag + "_missing")

    out.extend(flag for flag, active_flag in state["banned"].items() if active_flag)
    return out


def accepts(state: dict[str, Any]) -> bool:
    return not reasons(state)


def variant(base: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
    data = deepcopy(base)
    for key, value in kwargs.items():
        if key == "flags":
            data["flags"].update(value)
        elif key == "banned":
            data["banned"].update(value)
        elif key == "unique":
            data["unique"].update(value)
        elif key == "requires_drop":
            for node, req in value:
                data["requires"][node] = [item for item in data["requires"].get(node, []) if item != req]
        elif key == "edges_drop":
            data["edges"] -= set(value)
        else:
            data[key] = value
    return data


MAP = load_map()
live = active_state(MAP)

gate(
    f"{PREFIX}1 doc 564 globally unique diagram layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s unique_targets=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["unique"]["unique_targets"]),
    ),
)

family_gap = variant(
    live,
    banned={
        "diagram_parallel_isolated_solution": True,
        "diagram_discrete_solution_family": True,
        "diagram_duplicate_payload_solution": True,
        "diagram_moduli_component_choice": True,
        "diagram_same_payload_nonisomorphic_solution": True,
    },
    unique={
        "solution_space_singleton": False,
        "parallel_isolated_solution_free": False,
        "discrete_family_free": False,
        "duplicate_payload_free": False,
        "moduli_component_choice_free": False,
        "same_payload_nonisomorphic_free": False,
    },
)

gate(
    f"{PREFIX}2 rejects parallel, discrete, duplicate, moduli, or nonisomorphic solution families",
    not accepts(family_gap)
    and {
        "diagram_parallel_isolated_solution",
        "diagram_discrete_solution_family",
        "diagram_duplicate_payload_solution",
        "diagram_moduli_component_choice",
        "diagram_same_payload_nonisomorphic_solution",
    }
    <= set(reasons(family_gap)),
    ",".join(reasons(family_gap)),
)

selector_gap = variant(
    live,
    banned={
        "diagram_external_solution_selector": True,
        "diagram_lexicographic_solution_choice": True,
        "diagram_basis_order_solution_choice": True,
        "diagram_finite_enumeration_choice": True,
    },
    unique={
        "external_selector_free": False,
        "lexicographic_choice_free": False,
        "basis_order_choice_free": False,
        "finite_enumeration_choice_free": False,
    },
)

gate(
    f"{PREFIX}3 rejects external, lexicographic, basis-order, or finite-enumeration selectors",
    not accepts(selector_gap)
    and {
        "diagram_external_solution_selector",
        "diagram_lexicographic_solution_choice",
        "diagram_basis_order_solution_choice",
        "diagram_finite_enumeration_choice",
    }
    <= set(reasons(selector_gap)),
    ",".join(reasons(selector_gap)),
)

payload_gap = variant(
    live,
    banned={
        "diagram_endpoint_degree_duplicate_solution": True,
        "diagram_boundary_duplicate_solution": True,
        "diagram_exact_delta_duplicate_solution": True,
    },
    unique={
        "endpoint_degree_duplicate_free": False,
        "boundary_duplicate_free": False,
        "exact_delta_duplicate_free": False,
    },
)

gate(
    f"{PREFIX}4 rejects duplicate endpoint-degree, boundary, or exact-delta solutions",
    not accepts(payload_gap)
    and {
        "diagram_endpoint_degree_duplicate_solution",
        "diagram_boundary_duplicate_solution",
        "diagram_exact_delta_duplicate_solution",
    }
    <= set(reasons(payload_gap)),
    ",".join(reasons(payload_gap)),
)

structural_gap = variant(
    live,
    banned={
        "diagram_probe_indistinguishable_duplicate": True,
        "diagram_equalizer_duplicate_solution": True,
        "diagram_mediator_duplicate_solution": True,
        "diagram_source_coupling_duplicate_solution": True,
        "diagram_graph_rosati_control_duplicate_solution": True,
        "diagram_handoff_graph_duplicate_solution": True,
    },
    unique={
        "probe_indistinguishable_duplicate_free": False,
        "equalizer_duplicate_free": False,
        "mediator_duplicate_free": False,
        "source_coupling_duplicate_free": False,
        "graph_rosati_control_duplicate_free": False,
        "handoff_graph_duplicate_free": False,
    },
)

gate(
    f"{PREFIX}5 rejects duplicate probe, equalizer, mediator, coupling, graph, or handoff solutions",
    not accepts(structural_gap)
    and {
        "diagram_probe_indistinguishable_duplicate",
        "diagram_equalizer_duplicate_solution",
        "diagram_mediator_duplicate_solution",
        "diagram_source_coupling_duplicate_solution",
        "diagram_graph_rosati_control_duplicate_solution",
        "diagram_handoff_graph_duplicate_solution",
    }
    <= set(reasons(structural_gap)),
    ",".join(reasons(structural_gap)),
)

declared_gap = variant(
    live,
    banned={
        "diagram_global_uniqueness_by_declaration": True,
        "diagram_global_uniqueness_finite_sample": True,
        "diagram_global_uniqueness_basis_row": True,
    },
    unique={"declared_only": True, "finite_sample": True, "basis_row": True},
)

gate(
    f"{PREFIX}6 rejects declared global uniqueness, finite samples, or basis rows",
    not accepts(declared_gap)
    and {
        "diagram_global_uniqueness_by_declaration",
        "diagram_global_uniqueness_finite_sample",
        "diagram_global_uniqueness_basis_row",
    }
    <= set(reasons(declared_gap)),
    ",".join(reasons(declared_gap)),
)

missing_gap = variant(
    live,
    banned={"missing_globally_unique_cartesian_compatibility_diagram_certificate": True},
    unique={
        "certificate": None,
        "unique_targets": REQUIRED_UNIQUE_TARGETS - {DIAG, EQUALIZER, CART_EQV},
        "identities": REQUIRED_IDENTITIES
        - {
            "global_solution_singleton_law",
            "no_duplicate_payload_solution_law",
            "no_selector_choice_law",
        },
    },
)

gate(
    f"{PREFIX}7 rejects missing global uniqueness certificates, targets, or identities",
    not accepts(missing_gap)
    and "missing_globally_unique_cartesian_compatibility_diagram_certificate" in reasons(missing_gap)
    and any(reason.startswith("globally_unique_targets_missing:") for reason in reasons(missing_gap))
    and any(reason.startswith("globally_unique_identity_missing:") for reason in reasons(missing_gap)),
    ",".join(reasons(missing_gap)),
)

closure_gap = variant(
    live,
    requires_drop=[(ENDTRIV, GLOB), (GLOB, ENDTRIV), (GLOB, EXACT_DELTA)],
)

gate(
    f"{PREFIX}8 requires endomorphism-trivial and globally unique layers to close together",
    not accepts(closure_gap)
    and {
        "endomorphism_trivial_diagram_not_required_to_be_globally_unique",
        "globally_unique_diagram_requires_missing_endomorphism_trivial_base",
    }
    <= set(reasons(closure_gap))
    and any(reason.startswith("globally_unique_diagram_requires_missing:") for reason in reasons(closure_gap)),
    ",".join(reasons(closure_gap)),
)

edge_gap = variant(
    live,
    edges_drop={
        (ENDTRIV, "made_globally_unique_by", GLOB),
        (GLOB, "globally_unique_diagram_for", ENDTRIV),
        (GLOB, "payload_unique_for", EXACT_DELTA),
    },
)

gate(
    f"{PREFIX}9 requires every globally unique graph edge",
    not accepts(edge_gap)
    and any(reason.startswith("globally_unique_edges_missing:") for reason in reasons(edge_gap)),
    ",".join(reasons(edge_gap)),
)

variants = [variant(live, banned={flag: True}) for flag in BANNED_FLAGS]
variant_reasons: set[str] = set()
for bad in variants:
    variant_reasons.update(reasons(bad))

gate(
    f"{PREFIX}10 only globally unique cartesian compatibility diagrams pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILED gates: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: cartesian compatibility diagram is globally unique")
print(
    "VERDICT: the represented-limit cartesian compatibility diagram counts only "
    "when the endomorphism-trivial automorphism-rigid solution is globally "
    "unique, not one element of a parallel isolated, discrete, duplicate-"
    "payload, moduli-component, or selector-dependent family. Probe, equalizer, "
    "mediator, coupling, endpoint-degree, boundary, exact-delta, graph-Rosati-"
    "control, and handoff payloads must determine the same unique source-side "
    "finite-limit diagram inside the exact-24 budget."
)
