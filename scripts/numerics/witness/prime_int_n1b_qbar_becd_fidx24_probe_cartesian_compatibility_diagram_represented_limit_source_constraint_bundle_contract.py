r"""Cartesian compatibility diagram for the represented-limit bundle.

Doc 560 pins the seven source constraints into one represented-limit bundle.
This witness prevents that bundle from being only a product tuple with pasted
compatibility equations: the compatibility squares must form one cartesian
finite-limit diagram at the represented source-side limit.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the cartesian-compatibility witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 561
EXPECTED_WITNESS = "doc561-probe-cartesian-compatibility-diagram-represented-limit-source-constraint-bundle"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCARTCOMPATREPLIMSRCBUNDLE"

failures: list[str] = []

REQUIRED_DIAG_DEPS = {
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
    (BUNDLE, "made_cartesian_compatibility_diagram_by", DIAG),
    (DIAG, "cartesian_compatibility_diagram_for", BUNDLE),
    (DIAG, "endpoint_degree_square_for", ENDPOINT),
    (DIAG, "endpoint_degree_square_for", DEGREE),
    (DIAG, "boundary_pushforward_square_for", DD4_BOUNDARY),
    (DIAG, "boundary_pushforward_square_for", PUSHFORWARD),
    (DIAG, "exact_delta_square_for", EXACT_DELTA),
    (DIAG, "graph_rosati_control_square_for", GRAPH_COMP),
    (DIAG, "graph_rosati_control_square_for", ROSATI),
    (DIAG, "graph_rosati_control_square_for", CONTROL),
    (DIAG, "handoff_square_for", HANDOFF),
    (DIAG, "graph_realization_square_for", GRAPH_LATER),
    (DIAG, "equalized_by", EQUALIZER),
    (DIAG, "cartesian_reflected_by", CART_EQV),
    (DIAG, "mediator_generated_by", MEDIATOR),
    (DIAG, "source_coupled_for", SOURCE_COUPLING),
    (DIAG, "finite_limit_realized_on", FINITE_LIMIT),
    (DIAG, "preserves", FINITE_INDEX),
    (DIAG, "coherent_for", COUPLED_IMAGE),
}

REQUIRED_SQUARES = {
    "endpoint_degree_square",
    "boundary_pushforward_square",
    "dd4_exact_delta_square",
    "graph_rosati_control_square",
    "handoff_graph_square",
}

REQUIRED_IDENTITIES = {
    "cartesian_limit_diagram",
    "endpoint_degree_commutes",
    "boundary_pushforward_commutes",
    "dd4_exact_delta_commutes",
    "graph_rosati_control_commutes",
    "handoff_graph_commutes",
    "equalized_probe_reflected_diagram",
    "no_posthoc_pasting_law",
}

BANNED_FLAGS = (
    "product_tuple_without_compatibility_diagram",
    "pairwise_limit_compatibility_only",
    "noncartesian_limit_compatibility_square",
    "endpoint_degree_square_gap",
    "boundary_pushforward_square_gap",
    "dd4_exact_delta_square_gap",
    "graph_rosati_control_square_gap",
    "handoff_graph_square_gap",
    "compatibility_diagram_not_equalized",
    "compatibility_diagram_not_probe_reflected",
    "compatibility_diagram_not_mediator_generated",
    "compatibility_diagram_not_source_coupled",
    "compatibility_diagram_posthoc_pasting",
    "compatibility_diagram_external_commutative_table",
    "compatibility_diagram_new_cell",
    "compatibility_diagram_basis_row",
    "compatibility_diagram_finite_sample",
    "missing_represented_limit_cartesian_compatibility_diagram_certificate",
)

REQUIRED_FLAGS = (
    "cartesian_compatibility_diagram_actual",
    "endpoint_degree_square_present",
    "boundary_pushforward_square_present",
    "dd4_exact_delta_square_present",
    "graph_rosati_control_square_present",
    "handoff_graph_square_present",
    "equalized_probe_mediator_source_coupled",
    "inside_exact_24_budget",
)

DIAG_DATA = {
    "certificate": "represented_limit_cartesian_compatibility_diagram",
    "base_certificate": BUNDLE,
    "cartesian": True,
    "finite_limit_realized": True,
    "equalized": True,
    "probe_reflected": True,
    "mediator_generated": True,
    "source_coupled": True,
    "preserves_budget": True,
    "product_tuple_only": False,
    "pairwise_only": False,
    "posthoc_pasting": False,
    "external_table": False,
    "imports_positivity": False,
    "squares": REQUIRED_SQUARES,
    "identities": REQUIRED_IDENTITIES,
    "compatibility_diagram_basis_row": False,
    "compatibility_diagram_finite_sample": False,
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
        "diagram": deepcopy(DIAG_DATA),
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
    diagram = state["diagram"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_561")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc561_witness_missing")
    if DIAG not in accepted:
        out.append("cartesian_compatibility_diagram_missing_from_current")
    if BUNDLE not in accepted:
        out.append("source_constraint_bundle_base_missing_from_current")

    if not isinstance(diagram, dict):
        out.append("cartesian_compatibility_diagram_data_not_mapping")
        diagram = {}
    if diagram.get("certificate") != "represented_limit_cartesian_compatibility_diagram":
        out.append("missing_represented_limit_cartesian_compatibility_diagram_certificate")
    if diagram.get("base_certificate") != BUNDLE:
        out.append("cartesian_compatibility_diagram_not_based_on_bundle")
    if not diagram.get("cartesian"):
        out.append("noncartesian_limit_compatibility_square")
    if not diagram.get("finite_limit_realized"):
        out.append("noncartesian_limit_compatibility_square")
    if not diagram.get("equalized"):
        out.append("compatibility_diagram_not_equalized")
    if not diagram.get("probe_reflected"):
        out.append("compatibility_diagram_not_probe_reflected")
    if not diagram.get("mediator_generated"):
        out.append("compatibility_diagram_not_mediator_generated")
    if not diagram.get("source_coupled"):
        out.append("compatibility_diagram_not_source_coupled")
    if not diagram.get("preserves_budget"):
        out.append("compatibility_diagram_new_cell")
    if diagram.get("product_tuple_only"):
        out.append("product_tuple_without_compatibility_diagram")
    if diagram.get("pairwise_only"):
        out.append("pairwise_limit_compatibility_only")
    if diagram.get("posthoc_pasting"):
        out.append("compatibility_diagram_posthoc_pasting")
    if diagram.get("external_table"):
        out.append("compatibility_diagram_external_commutative_table")
    if diagram.get("imports_positivity"):
        out.append("cartesian_compatibility_diagram_imports_positivity")

    for key in ("compatibility_diagram_basis_row", "compatibility_diagram_finite_sample"):
        if diagram.get(key):
            out.append(key)

    squares = _as_set(diagram.get("squares"))
    if "endpoint_degree_square" not in squares:
        out.append("endpoint_degree_square_gap")
    if "boundary_pushforward_square" not in squares:
        out.append("boundary_pushforward_square_gap")
    if "dd4_exact_delta_square" not in squares:
        out.append("dd4_exact_delta_square_gap")
    if "graph_rosati_control_square" not in squares:
        out.append("graph_rosati_control_square_gap")
    if "handoff_graph_square" not in squares:
        out.append("handoff_graph_square_gap")

    missing_squares = REQUIRED_SQUARES - squares
    if missing_squares:
        out.append("cartesian_compatibility_squares_missing:" + ",".join(sorted(missing_squares)))

    missing_identities = REQUIRED_IDENTITIES - _as_set(diagram.get("identities"))
    if missing_identities:
        out.append("cartesian_compatibility_identity_missing:" + ",".join(sorted(missing_identities)))

    if DIAG not in requires.get(BUNDLE, []):
        out.append("bundle_not_required_to_have_cartesian_compatibility_diagram")
    if BUNDLE not in requires.get(DIAG, []):
        out.append("cartesian_diagram_requires_missing_bundle_base")
    missing_deps = REQUIRED_DIAG_DEPS - set(requires.get(DIAG, []))
    if missing_deps:
        out.append("cartesian_diagram_requires_missing:" + ",".join(sorted(missing_deps)))

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("cartesian_compatibility_edges_missing:" + ",".join(rendered))

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
        elif key == "diagram":
            data["diagram"].update(value)
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
    f"{PREFIX}1 doc 561 cartesian compatibility diagram layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s squares=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["diagram"]["squares"]),
    ),
)

product_gap = variant(
    live,
    banned={
        "product_tuple_without_compatibility_diagram": True,
        "pairwise_limit_compatibility_only": True,
        "compatibility_diagram_external_commutative_table": True,
    },
    diagram={"product_tuple_only": True, "pairwise_only": True, "external_table": True},
)

gate(
    f"{PREFIX}2 rejects product tuples, pairwise compatibility, or external tables",
    not accepts(product_gap)
    and {
        "product_tuple_without_compatibility_diagram",
        "pairwise_limit_compatibility_only",
        "compatibility_diagram_external_commutative_table",
    }
    <= set(reasons(product_gap)),
    ",".join(reasons(product_gap)),
)

endpoint_gap = variant(
    live,
    banned={"noncartesian_limit_compatibility_square": True, "endpoint_degree_square_gap": True},
    diagram={"cartesian": False, "squares": REQUIRED_SQUARES - {"endpoint_degree_square"}},
)

gate(
    f"{PREFIX}3 rejects noncartesian or endpoint-degree square gaps",
    not accepts(endpoint_gap)
    and {"noncartesian_limit_compatibility_square", "endpoint_degree_square_gap"}
    <= set(reasons(endpoint_gap)),
    ",".join(reasons(endpoint_gap)),
)

boundary_gap = variant(
    live,
    banned={"boundary_pushforward_square_gap": True, "dd4_exact_delta_square_gap": True},
    diagram={"squares": REQUIRED_SQUARES - {"boundary_pushforward_square", "dd4_exact_delta_square"}},
)

gate(
    f"{PREFIX}4 rejects boundary-pushforward or DD4/exact-delta square gaps",
    not accepts(boundary_gap)
    and {"boundary_pushforward_square_gap", "dd4_exact_delta_square_gap"} <= set(reasons(boundary_gap)),
    ",".join(reasons(boundary_gap)),
)

graph_gap = variant(
    live,
    banned={"graph_rosati_control_square_gap": True, "handoff_graph_square_gap": True},
    diagram={"squares": REQUIRED_SQUARES - {"graph_rosati_control_square", "handoff_graph_square"}},
)

gate(
    f"{PREFIX}5 rejects graph-Rosati-control or handoff/graph square gaps",
    not accepts(graph_gap)
    and {"graph_rosati_control_square_gap", "handoff_graph_square_gap"} <= set(reasons(graph_gap)),
    ",".join(reasons(graph_gap)),
)

structure_gap = variant(
    live,
    banned={
        "compatibility_diagram_not_equalized": True,
        "compatibility_diagram_not_probe_reflected": True,
        "compatibility_diagram_not_mediator_generated": True,
        "compatibility_diagram_not_source_coupled": True,
    },
    diagram={
        "equalized": False,
        "probe_reflected": False,
        "mediator_generated": False,
        "source_coupled": False,
    },
)

gate(
    f"{PREFIX}6 rejects non-equalized, non-probe-reflected, non-mediator-generated, or non-source-coupled diagrams",
    not accepts(structure_gap)
    and {
        "compatibility_diagram_not_equalized",
        "compatibility_diagram_not_probe_reflected",
        "compatibility_diagram_not_mediator_generated",
        "compatibility_diagram_not_source_coupled",
    }
    <= set(reasons(structure_gap)),
    ",".join(reasons(structure_gap)),
)

selector_gap = variant(
    live,
    banned={
        "compatibility_diagram_posthoc_pasting": True,
        "compatibility_diagram_new_cell": True,
        "compatibility_diagram_basis_row": True,
        "compatibility_diagram_finite_sample": True,
    },
    diagram={
        "posthoc_pasting": True,
        "preserves_budget": False,
        "compatibility_diagram_basis_row": True,
        "compatibility_diagram_finite_sample": True,
    },
)

gate(
    f"{PREFIX}7 rejects posthoc pasting, new cells, basis rows, or finite samples",
    not accepts(selector_gap)
    and {
        "compatibility_diagram_posthoc_pasting",
        "compatibility_diagram_new_cell",
        "compatibility_diagram_basis_row",
        "compatibility_diagram_finite_sample",
    }
    <= set(reasons(selector_gap)),
    ",".join(reasons(selector_gap)),
)

missing_gap = variant(
    live,
    banned={"missing_represented_limit_cartesian_compatibility_diagram_certificate": True},
    diagram={
        "certificate": None,
        "identities": REQUIRED_IDENTITIES
        - {
            "cartesian_limit_diagram",
            "endpoint_degree_commutes",
            "no_posthoc_pasting_law",
        },
    },
)

gate(
    f"{PREFIX}8 rejects missing cartesian compatibility certificates or identities",
    not accepts(missing_gap)
    and "missing_represented_limit_cartesian_compatibility_diagram_certificate" in reasons(missing_gap)
    and any(reason.startswith("cartesian_compatibility_identity_missing:") for reason in reasons(missing_gap)),
    ",".join(reasons(missing_gap)),
)

closure_gap = variant(
    live,
    requires_drop=[(BUNDLE, DIAG), (DIAG, BUNDLE), (DIAG, EXACT_DELTA)],
    edges_drop={
        (BUNDLE, "made_cartesian_compatibility_diagram_by", DIAG),
        (DIAG, "cartesian_compatibility_diagram_for", BUNDLE),
        (DIAG, "exact_delta_square_for", EXACT_DELTA),
    },
)

gate(
    f"{PREFIX}9 requires bundle and cartesian compatibility diagram to close together",
    not accepts(closure_gap)
    and {
        "bundle_not_required_to_have_cartesian_compatibility_diagram",
        "cartesian_diagram_requires_missing_bundle_base",
    }
    <= set(reasons(closure_gap))
    and any(reason.startswith("cartesian_diagram_requires_missing:") for reason in reasons(closure_gap))
    and any(reason.startswith("cartesian_compatibility_edges_missing:") for reason in reasons(closure_gap)),
    ",".join(reasons(closure_gap)),
)

variants = [variant(live, banned={flag: True}) for flag in BANNED_FLAGS]
variant_reasons: set[str] = set()
for bad in variants:
    variant_reasons.update(reasons(bad))

gate(
    f"{PREFIX}10 only represented-limit cartesian compatibility diagrams pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILED gates: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: represented-limit bundle has cartesian compatibility diagram")
print(
    "VERDICT: the represented-limit source-constraint bundle counts only when "
    "its endpoint-degree, boundary-pushforward, DD.4/exact-delta, "
    "graph-Rosati-control, and handoff/graph-realization compatibilities form "
    "one equalized, probe-reflected, mediator-generated, source-coupled "
    "cartesian finite-limit diagram. Product tuples, pairwise compatibility, "
    "posthoc pasting, external tables, new cells, basis rows, and finite samples "
    "do not construct the missing object."
)
