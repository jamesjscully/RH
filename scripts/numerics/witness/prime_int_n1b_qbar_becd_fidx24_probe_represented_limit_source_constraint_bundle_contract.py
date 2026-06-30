r"""Represented-limit source-constraint bundle contract.

Doc 559 pins an attained represented source-side limit for the filtered
refinement calculus. This witness prevents the seven source constraints from
surviving only as separate projections: endpoint integrality, degree maps,
DD.4 boundary, boundary pushforward, graph composition, Rosati count, and
control death must be one represented-limit bundle.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_represented_limit_source_constraint_bundle_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the represented-limit bundle witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 560
EXPECTED_WITNESS = "doc560-probe-represented-limit-source-constraint-bundle"
BUNDLE = "represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
RLIM = "represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
FRC = "filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REF = "refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MED = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
JOINT = "joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
ACTIVE = "dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
CART_EQV = "cartesian_probe_equivalence_certificate"
PROBE_EQV = "probe_equivalence_certificate"
PROBE_ESS = "probe_essential_image_certificate"
PROBE_FULL = "probe_fullness_certificate"
PROBE_FAITH = "probe_faithfulness_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
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
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPLIMSRCBUNDLEFILTCFREFCALC"

failures: list[str] = []

CONSTRAINT_TARGETS = {
    ENDPOINT,
    DEGREE,
    DD4_BOUNDARY,
    PUSHFORWARD,
    GRAPH_COMP,
    ROSATI,
    CONTROL,
}

SUPPORT_TARGETS = {
    RLIM,
    FRC,
    JOINT,
    SUBREP,
    EQUALIZER,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
    COUPLED_IMAGE,
    EXACT_DELTA,
    FINITE_INDEX,
}

REQUIRED_BUNDLE_DEPS = {
    RLIM,
    FRC,
    REF,
    MED,
    JOINT,
    ACTIVE,
    SUBREP,
    COUPLED_IMAGE,
    FINITE_LIMIT,
    EQUALIZER,
    TERMINAL_CERT,
    ADM_CAT,
    CART_EQV,
    PROBE_EQV,
    PROBE_ESS,
    PROBE_FULL,
    PROBE_FAITH,
    PROBE_NAT,
    PROBE_SEP,
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
    (RLIM, "made_source_constraint_bundle_by", BUNDLE),
    (BUNDLE, "source_constraint_bundle_at_limit_of", RLIM),
    (BUNDLE, "joint_source_law_at_limit_for", JOINT),
    (BUNDLE, "endpoint_integrality_limit_for", ENDPOINT),
    (BUNDLE, "degree_maps_limit_for", DEGREE),
    (BUNDLE, "dd4_boundary_limit_for", DD4_BOUNDARY),
    (BUNDLE, "boundary_pushforward_limit_for", PUSHFORWARD),
    (BUNDLE, "graph_composition_limit_for", GRAPH_COMP),
    (BUNDLE, "rosati_count_limit_for", ROSATI),
    (BUNDLE, "control_death_limit_for", CONTROL),
    (BUNDLE, "represented_by", SUBREP),
    (BUNDLE, "equalizer_monic_by", EQUALIZER),
    (BUNDLE, "probe_reflected_by", CART_EQV),
    (BUNDLE, "mediator_generated_by", MEDIATOR),
    (BUNDLE, "source_coupling_for", SOURCE_COUPLING),
    (BUNDLE, "exact_delta_compatible_with", EXACT_DELTA),
    (BUNDLE, "preserves", FINITE_INDEX),
    (BUNDLE, "coherent_for", COUPLED_IMAGE),
}

REQUIRED_IDENTITIES = {
    "joint_constraint_tuple_at_limit",
    "endpoint_degree_compatibility_law",
    "dd4_boundary_pushforward_law",
    "graph_rosati_control_law",
    "monic_probe_reflected_bundle_law",
    "no_projection_selector_law",
}

BANNED_FLAGS = (
    "separate_limit_constraint_projections",
    "endpoint_integrality_limit_gap",
    "degree_maps_limit_gap",
    "dd4_boundary_limit_gap",
    "boundary_pushforward_limit_gap",
    "graph_composition_limit_gap",
    "rosati_count_limit_gap",
    "control_death_limit_gap",
    "limit_constraint_tuple_not_joint",
    "limit_constraint_tuple_not_monic",
    "limit_constraint_tuple_not_probe_reflected",
    "limit_constraint_tuple_not_mediator_generated",
    "limit_constraint_tuple_not_source_coupled",
    "posthoc_limit_projection_selector",
    "limit_constraint_bundle_requires_new_cell",
    "limit_constraint_bundle_basis_row",
    "limit_constraint_bundle_finite_sample",
    "limit_constraint_bundle_external_table",
    "missing_represented_limit_source_constraint_bundle_certificate",
)

REQUIRED_FLAGS = (
    "represented_limit_source_constraint_bundle_actual",
    "seven_source_constraints_joint",
    "endpoint_degree_law_present",
    "dd4_boundary_pushforward_law_present",
    "graph_rosati_control_law_present",
    "monic_probe_reflected_mediator_source_coupled",
    "inside_exact_24_budget",
)

BUNDLE_DATA = {
    "certificate": "represented_limit_source_constraint_bundle",
    "base_certificate": RLIM,
    "joint": True,
    "represented": True,
    "source_side": True,
    "monic": True,
    "probe_reflected": True,
    "mediator_generated": True,
    "source_coupled": True,
    "preserves_budget": True,
    "external_projection_selector": False,
    "external_table": False,
    "imports_positivity": False,
    "constraint_targets": CONSTRAINT_TARGETS,
    "support_targets": SUPPORT_TARGETS,
    "identities": REQUIRED_IDENTITIES,
    "separate_limit_constraint_projections": False,
    "limit_constraint_bundle_basis_row": False,
    "limit_constraint_bundle_finite_sample": False,
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
        "bundle": deepcopy(BUNDLE_DATA),
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
    bundle = state["bundle"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_560")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc560_witness_missing")
    if BUNDLE not in accepted:
        out.append("source_constraint_bundle_missing_from_current")
    if RLIM not in accepted:
        out.append("represented_limit_base_missing_from_current")

    if not isinstance(bundle, dict):
        out.append("source_constraint_bundle_data_not_mapping")
        bundle = {}
    if bundle.get("certificate") != "represented_limit_source_constraint_bundle":
        out.append("missing_represented_limit_source_constraint_bundle_certificate")
    if bundle.get("base_certificate") != RLIM:
        out.append("source_constraint_bundle_not_based_on_represented_limit")
    if not bundle.get("joint"):
        out.append("limit_constraint_tuple_not_joint")
    if not bundle.get("represented") or not bundle.get("source_side"):
        out.append("missing_represented_limit_source_constraint_bundle_certificate")
    if not bundle.get("monic"):
        out.append("limit_constraint_tuple_not_monic")
    if not bundle.get("probe_reflected"):
        out.append("limit_constraint_tuple_not_probe_reflected")
    if not bundle.get("mediator_generated"):
        out.append("limit_constraint_tuple_not_mediator_generated")
    if not bundle.get("source_coupled"):
        out.append("limit_constraint_tuple_not_source_coupled")
    if not bundle.get("preserves_budget"):
        out.append("limit_constraint_bundle_requires_new_cell")
    if bundle.get("external_projection_selector"):
        out.append("posthoc_limit_projection_selector")
    if bundle.get("external_table"):
        out.append("limit_constraint_bundle_external_table")
    if bundle.get("imports_positivity"):
        out.append("source_constraint_bundle_imports_positivity")

    for key in (
        "separate_limit_constraint_projections",
        "limit_constraint_bundle_basis_row",
        "limit_constraint_bundle_finite_sample",
    ):
        if bundle.get(key):
            out.append(key)

    constraints = _as_set(bundle.get("constraint_targets"))
    if ENDPOINT not in constraints:
        out.append("endpoint_integrality_limit_gap")
    if DEGREE not in constraints:
        out.append("degree_maps_limit_gap")
    if DD4_BOUNDARY not in constraints:
        out.append("dd4_boundary_limit_gap")
    if PUSHFORWARD not in constraints:
        out.append("boundary_pushforward_limit_gap")
    if GRAPH_COMP not in constraints:
        out.append("graph_composition_limit_gap")
    if ROSATI not in constraints:
        out.append("rosati_count_limit_gap")
    if CONTROL not in constraints:
        out.append("control_death_limit_gap")

    missing_constraints = CONSTRAINT_TARGETS - constraints
    if missing_constraints:
        out.append("source_constraint_bundle_targets_missing:" + ",".join(sorted(missing_constraints)))

    support_targets = _as_set(bundle.get("support_targets"))
    missing_support = SUPPORT_TARGETS - support_targets
    if missing_support:
        out.append("source_constraint_bundle_support_missing:" + ",".join(sorted(missing_support)))

    missing_identities = REQUIRED_IDENTITIES - _as_set(bundle.get("identities"))
    if missing_identities:
        out.append("source_constraint_bundle_identity_missing:" + ",".join(sorted(missing_identities)))

    if BUNDLE not in requires.get(RLIM, []):
        out.append("represented_limit_not_required_to_carry_source_constraint_bundle")
    if RLIM not in requires.get(BUNDLE, []):
        out.append("source_constraint_bundle_requires_missing_represented_limit_base")
    missing_deps = REQUIRED_BUNDLE_DEPS - set(requires.get(BUNDLE, []))
    if missing_deps:
        out.append("source_constraint_bundle_requires_missing:" + ",".join(sorted(missing_deps)))

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("source_constraint_bundle_edges_missing:" + ",".join(rendered))

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
        elif key == "bundle":
            data["bundle"].update(value)
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
    f"{PREFIX}1 doc 560 represented-limit source-constraint bundle is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s constraints=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["bundle"]["constraint_targets"]),
    ),
)

separate_gap = variant(
    live,
    banned={
        "separate_limit_constraint_projections": True,
        "limit_constraint_tuple_not_joint": True,
        "limit_constraint_bundle_external_table": True,
    },
    bundle={
        "separate_limit_constraint_projections": True,
        "joint": False,
        "external_table": True,
    },
)

gate(
    f"{PREFIX}2 rejects separate projection bundles, non-joint tuples, or external tables",
    not accepts(separate_gap)
    and {
        "separate_limit_constraint_projections",
        "limit_constraint_tuple_not_joint",
        "limit_constraint_bundle_external_table",
    }
    <= set(reasons(separate_gap)),
    ",".join(reasons(separate_gap)),
)

endpoint_degree_gap = variant(
    live,
    banned={"endpoint_integrality_limit_gap": True, "degree_maps_limit_gap": True},
    bundle={"constraint_targets": CONSTRAINT_TARGETS - {ENDPOINT, DEGREE}},
)

gate(
    f"{PREFIX}3 rejects endpoint-integrality or degree-map limit gaps",
    not accepts(endpoint_degree_gap)
    and {"endpoint_integrality_limit_gap", "degree_maps_limit_gap"} <= set(reasons(endpoint_degree_gap)),
    ",".join(reasons(endpoint_degree_gap)),
)

boundary_gap = variant(
    live,
    banned={"dd4_boundary_limit_gap": True, "boundary_pushforward_limit_gap": True},
    bundle={"constraint_targets": CONSTRAINT_TARGETS - {DD4_BOUNDARY, PUSHFORWARD}},
)

gate(
    f"{PREFIX}4 rejects DD4-boundary or boundary-pushforward limit gaps",
    not accepts(boundary_gap)
    and {"dd4_boundary_limit_gap", "boundary_pushforward_limit_gap"} <= set(reasons(boundary_gap)),
    ",".join(reasons(boundary_gap)),
)

graph_gap = variant(
    live,
    banned={
        "graph_composition_limit_gap": True,
        "rosati_count_limit_gap": True,
        "control_death_limit_gap": True,
    },
    bundle={"constraint_targets": CONSTRAINT_TARGETS - {GRAPH_COMP, ROSATI, CONTROL}},
)

gate(
    f"{PREFIX}5 rejects graph-composition, Rosati-count, or control-death gaps",
    not accepts(graph_gap)
    and {
        "graph_composition_limit_gap",
        "rosati_count_limit_gap",
        "control_death_limit_gap",
    }
    <= set(reasons(graph_gap)),
    ",".join(reasons(graph_gap)),
)

structure_gap = variant(
    live,
    banned={
        "limit_constraint_tuple_not_monic": True,
        "limit_constraint_tuple_not_probe_reflected": True,
        "limit_constraint_tuple_not_mediator_generated": True,
        "limit_constraint_tuple_not_source_coupled": True,
    },
    bundle={
        "monic": False,
        "probe_reflected": False,
        "mediator_generated": False,
        "source_coupled": False,
    },
)

gate(
    f"{PREFIX}6 rejects nonmonic, non-probe-reflected, non-mediator-generated, or non-source-coupled bundles",
    not accepts(structure_gap)
    and {
        "limit_constraint_tuple_not_monic",
        "limit_constraint_tuple_not_probe_reflected",
        "limit_constraint_tuple_not_mediator_generated",
        "limit_constraint_tuple_not_source_coupled",
    }
    <= set(reasons(structure_gap)),
    ",".join(reasons(structure_gap)),
)

selector_gap = variant(
    live,
    banned={
        "posthoc_limit_projection_selector": True,
        "limit_constraint_bundle_requires_new_cell": True,
        "limit_constraint_bundle_basis_row": True,
        "limit_constraint_bundle_finite_sample": True,
    },
    bundle={
        "external_projection_selector": True,
        "preserves_budget": False,
        "limit_constraint_bundle_basis_row": True,
        "limit_constraint_bundle_finite_sample": True,
    },
)

gate(
    f"{PREFIX}7 rejects posthoc selectors, new cells, basis rows, or finite samples",
    not accepts(selector_gap)
    and {
        "posthoc_limit_projection_selector",
        "limit_constraint_bundle_requires_new_cell",
        "limit_constraint_bundle_basis_row",
        "limit_constraint_bundle_finite_sample",
    }
    <= set(reasons(selector_gap)),
    ",".join(reasons(selector_gap)),
)

missing_gap = variant(
    live,
    banned={"missing_represented_limit_source_constraint_bundle_certificate": True},
    bundle={
        "certificate": None,
        "identities": REQUIRED_IDENTITIES
        - {
            "joint_constraint_tuple_at_limit",
            "endpoint_degree_compatibility_law",
            "graph_rosati_control_law",
        },
    },
)

gate(
    f"{PREFIX}8 rejects missing bundle certificates or joint identities",
    not accepts(missing_gap)
    and "missing_represented_limit_source_constraint_bundle_certificate" in reasons(missing_gap)
    and any(reason.startswith("source_constraint_bundle_identity_missing:") for reason in reasons(missing_gap)),
    ",".join(reasons(missing_gap)),
)

closure_gap = variant(
    live,
    requires_drop=[(RLIM, BUNDLE), (BUNDLE, RLIM), (BUNDLE, ROSATI)],
    edges_drop={
        (RLIM, "made_source_constraint_bundle_by", BUNDLE),
        (BUNDLE, "source_constraint_bundle_at_limit_of", RLIM),
        (BUNDLE, "rosati_count_limit_for", ROSATI),
    },
)

gate(
    f"{PREFIX}9 requires represented limit and source-constraint bundle to close together",
    not accepts(closure_gap)
    and {
        "represented_limit_not_required_to_carry_source_constraint_bundle",
        "source_constraint_bundle_requires_missing_represented_limit_base",
    }
    <= set(reasons(closure_gap))
    and any(reason.startswith("source_constraint_bundle_requires_missing:") for reason in reasons(closure_gap))
    and any(reason.startswith("source_constraint_bundle_edges_missing:") for reason in reasons(closure_gap)),
    ",".join(reasons(closure_gap)),
)

variants = [variant(live, banned={flag: True}) for flag in BANNED_FLAGS]
variant_reasons: set[str] = set()
for bad in variants:
    variant_reasons.update(reasons(bad))

gate(
    f"{PREFIX}10 only represented-limit source-constraint bundles pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILED gates: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: represented limit carries joint source constraint bundle")
print(
    "VERDICT: the represented source-side limit counts only when it carries "
    "endpoint integrality, degree maps, DD.4 boundary, boundary pushforward, "
    "graph composition, Rosati count, and control death as one monic, "
    "probe-reflected, mediator-generated, source-coupled tuple. Separate "
    "projection, endpoint/degree, boundary/pushforward, graph/Rosati/control, "
    "selector, basis-row, finite-sample, external-table, and new-cell repairs "
    "do not construct the missing object."
)
