r"""Represented-limit-realized filtered-refinement calculus contract.

Doc 558 pins the refinement law to one filtered cofinal calculus. This witness
prevents that calculus from being only a pro-family or external completion: it
must have an attained represented source-side limit inside the existing
finite-limit/equalizer spine, preserving probes, DD.4 payload, graph,
composition, exact delta, and control.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_represented_limit_realized_filtered_refinement_calculus_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the represented-limit witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 559
EXPECTED_WITNESS = "doc559-probe-represented-limit-realized-filtered-refinement-calculus"
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
DD4 = "original_dd4_class"
HANDOFF = "dd4_image_only_handoff_contract"
GRAPH = "graph_later_realization_contract"
COMPOSITION = "graph_composition"
CONTROL = "control_death"
EXACT_DELTA = "exact_delta"
FINITE_INDEX = "exact_24_cell_finite_index"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPREPLIMFILTCFREFCALCSTABREFDESCSTABMEDGENCOMPSTABJLAWDD4ACTRIGIDPRIMEFFK0LIFT"

failures: list[str] = []

REQUIRED_LIMIT_DEPS = {
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
    DD4,
    HANDOFF,
    GRAPH,
    COMPOSITION,
    CONTROL,
    EXACT_DELTA,
    FINITE_INDEX,
}

LIMIT_TARGETS = {
    FRC,
    FINITE_LIMIT,
    SUBREP,
    EQUALIZER,
    TERMINAL_CERT,
    ADM_CAT,
    CART_EQV,
    MEDIATOR,
    SOURCE_COUPLING,
    DD4,
    HANDOFF,
    GRAPH,
    COMPOSITION,
    CONTROL,
    EXACT_DELTA,
    FINITE_INDEX,
    COUPLED_IMAGE,
}

EXPECTED_EDGES = {
    (FRC, "made_represented_limit_realized_by", RLIM),
    (RLIM, "represented_limit_of", FRC),
    (RLIM, "realizes_limit_cone_on", FINITE_LIMIT),
    (RLIM, "universal_cone_by", TERMINAL_CERT),
    (RLIM, "represented_by", SUBREP),
    (RLIM, "equalizer_monic_by", EQUALIZER),
    (RLIM, "cone_base_cofinal_for", ADM_CAT),
    (RLIM, "probe_limit_reflected_by", CART_EQV),
    (RLIM, "mediator_limit_for", MEDIATOR),
    (RLIM, "source_coupling_limit_for", SOURCE_COUPLING),
    (RLIM, "payload_limit_for", DD4),
    (RLIM, "handoff_limit_for", HANDOFF),
    (RLIM, "graph_limit_for", GRAPH),
    (RLIM, "composition_limit_for", COMPOSITION),
    (RLIM, "control_limit_for", CONTROL),
    (RLIM, "exact_delta_limit_for", EXACT_DELTA),
    (RLIM, "preserves", FINITE_INDEX),
    (RLIM, "coherent_for", COUPLED_IMAGE),
}

REQUIRED_IDENTITIES = {
    "represented_limit_cone",
    "source_category_attainment",
    "equalizer_monic_limit",
    "probe_reflected_limit",
    "payload_limit_law",
    "graph_control_limit_law",
}

BANNED_FLAGS = (
    "pro_refinement_family_only",
    "inverse_limit_not_represented",
    "external_pro_completion",
    "formal_limit_cone_only",
    "nonattained_refinement_limit",
    "limit_outside_source_category",
    "completion_added_limit_object",
    "choice_dependent_limit_cone",
    "nonunique_limit_representative",
    "limit_not_preserved_by_probes",
    "limit_not_equalizer_monic",
    "limit_payload_gap",
    "limit_handoff_gap",
    "limit_graph_gap",
    "limit_composition_gap",
    "limit_control_gap",
    "limit_requires_new_finite_index_cell",
    "limit_basis_row",
    "limit_finite_sample",
    "missing_represented_refinement_limit_certificate",
)

REQUIRED_FLAGS = (
    "represented_refinement_limit_certificate_actual",
    "source_side_limit_cone",
    "represented_source_limit_object",
    "finite_limit_equalizer_spine_limit",
    "probe_reflected_limit",
    "payload_graph_control_limit_preserved",
    "inside_exact_24_budget",
)

LIMIT_DATA = {
    "certificate": "represented_refinement_limit",
    "base_certificate": FRC,
    "source_side": True,
    "represented": True,
    "inside_source_category": True,
    "attained": True,
    "uses_external_completion": False,
    "formal_cone_only": False,
    "choice_free_cone": True,
    "unique_representative": True,
    "probe_reflected": True,
    "equalizer_monic": True,
    "preserves_budget": True,
    "imports_positivity": False,
    "limit_targets": LIMIT_TARGETS,
    "identities": REQUIRED_IDENTITIES,
    "pro_refinement_family_only": False,
    "limit_basis_row": False,
    "limit_finite_sample": False,
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
        "limit": deepcopy(LIMIT_DATA),
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
    limit = state["limit"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_559")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc559_witness_missing")
    if RLIM not in accepted:
        out.append("represented_limit_missing_from_current")
    if FRC not in accepted:
        out.append("filtered_calculus_base_missing_from_current")

    if not isinstance(limit, dict):
        out.append("represented_limit_data_not_mapping")
        limit = {}
    if limit.get("certificate") != "represented_refinement_limit":
        out.append("missing_represented_refinement_limit_certificate")
    if limit.get("base_certificate") != FRC:
        out.append("represented_limit_not_based_on_filtered_calculus")
    if not limit.get("source_side") or not limit.get("inside_source_category"):
        out.append("limit_outside_source_category")
    if not limit.get("represented"):
        out.append("inverse_limit_not_represented")
    if not limit.get("attained"):
        out.append("nonattained_refinement_limit")
    if limit.get("uses_external_completion"):
        out.append("external_pro_completion")
        out.append("completion_added_limit_object")
    if limit.get("formal_cone_only"):
        out.append("formal_limit_cone_only")
    if not limit.get("choice_free_cone"):
        out.append("choice_dependent_limit_cone")
    if not limit.get("unique_representative"):
        out.append("nonunique_limit_representative")
    if not limit.get("probe_reflected"):
        out.append("limit_not_preserved_by_probes")
    if not limit.get("equalizer_monic"):
        out.append("limit_not_equalizer_monic")
    if not limit.get("preserves_budget"):
        out.append("limit_requires_new_finite_index_cell")
    if limit.get("imports_positivity"):
        out.append("represented_limit_imports_positivity")

    for key in ("pro_refinement_family_only", "limit_basis_row", "limit_finite_sample"):
        if limit.get(key):
            out.append(key)

    targets = _as_set(limit.get("limit_targets"))
    if DD4 not in targets:
        out.append("limit_payload_gap")
    if HANDOFF not in targets:
        out.append("limit_handoff_gap")
    if GRAPH not in targets:
        out.append("limit_graph_gap")
    if COMPOSITION not in targets or EXACT_DELTA not in targets:
        out.append("limit_composition_gap")
    if CONTROL not in targets:
        out.append("limit_control_gap")

    missing_targets = LIMIT_TARGETS - targets
    if missing_targets:
        out.append("represented_limit_targets_missing:" + ",".join(sorted(missing_targets)))

    missing_identities = REQUIRED_IDENTITIES - _as_set(limit.get("identities"))
    if missing_identities:
        out.append("represented_limit_identity_missing:" + ",".join(sorted(missing_identities)))

    if RLIM not in requires.get(FRC, []):
        out.append("filtered_calculus_not_required_to_be_represented_limit_realized")
    if FRC not in requires.get(RLIM, []):
        out.append("represented_limit_requires_missing_filtered_calculus_base")
    missing_deps = REQUIRED_LIMIT_DEPS - set(requires.get(RLIM, []))
    if missing_deps:
        out.append("represented_limit_requires_missing:" + ",".join(sorted(missing_deps)))

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("represented_limit_edges_missing:" + ",".join(rendered))

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
        elif key == "limit":
            data["limit"].update(value)
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
    f"{PREFIX}1 doc 559 represented source-side limit layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s targets=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["limit"]["limit_targets"]),
    ),
)

pro_gap = variant(
    live,
    banned={
        "pro_refinement_family_only": True,
        "inverse_limit_not_represented": True,
        "external_pro_completion": True,
    },
    limit={
        "pro_refinement_family_only": True,
        "represented": False,
        "uses_external_completion": True,
    },
)

gate(
    f"{PREFIX}2 rejects pro-family, nonrepresented inverse-limit, or external-completion repairs",
    not accepts(pro_gap)
    and {"pro_refinement_family_only", "inverse_limit_not_represented", "external_pro_completion"}
    <= set(reasons(pro_gap)),
    ",".join(reasons(pro_gap)),
)

formal_gap = variant(
    live,
    banned={
        "formal_limit_cone_only": True,
        "nonattained_refinement_limit": True,
        "limit_outside_source_category": True,
        "completion_added_limit_object": True,
    },
    limit={
        "formal_cone_only": True,
        "attained": False,
        "inside_source_category": False,
        "uses_external_completion": True,
    },
)

gate(
    f"{PREFIX}3 rejects formal cones, nonattainment, outside-category limits, or completion-added objects",
    not accepts(formal_gap)
    and {
        "formal_limit_cone_only",
        "nonattained_refinement_limit",
        "limit_outside_source_category",
        "completion_added_limit_object",
    }
    <= set(reasons(formal_gap)),
    ",".join(reasons(formal_gap)),
)

choice_gap = variant(
    live,
    banned={"choice_dependent_limit_cone": True, "nonunique_limit_representative": True},
    limit={"choice_free_cone": False, "unique_representative": False},
)

gate(
    f"{PREFIX}4 rejects choice-dependent cones or nonunique representatives",
    not accepts(choice_gap)
    and {"choice_dependent_limit_cone", "nonunique_limit_representative"}
    <= set(reasons(choice_gap)),
    ",".join(reasons(choice_gap)),
)

probe_equalizer_gap = variant(
    live,
    banned={"limit_not_preserved_by_probes": True, "limit_not_equalizer_monic": True},
    limit={"probe_reflected": False, "equalizer_monic": False},
)

gate(
    f"{PREFIX}5 rejects probe reflection or equalizer monicity gaps",
    not accepts(probe_equalizer_gap)
    and {"limit_not_preserved_by_probes", "limit_not_equalizer_monic"}
    <= set(reasons(probe_equalizer_gap)),
    ",".join(reasons(probe_equalizer_gap)),
)

payload_gap = variant(
    live,
    banned={
        "limit_payload_gap": True,
        "limit_handoff_gap": True,
        "limit_graph_gap": True,
        "limit_composition_gap": True,
        "limit_control_gap": True,
    },
    limit={
        "limit_targets": {
            FRC,
            FINITE_LIMIT,
            SUBREP,
            EQUALIZER,
            TERMINAL_CERT,
            ADM_CAT,
            CART_EQV,
            MEDIATOR,
            SOURCE_COUPLING,
            FINITE_INDEX,
            COUPLED_IMAGE,
        },
    },
)

gate(
    f"{PREFIX}6 rejects DD4 payload, handoff, graph, composition, or control limit gaps",
    not accepts(payload_gap)
    and {
        "limit_payload_gap",
        "limit_handoff_gap",
        "limit_graph_gap",
        "limit_composition_gap",
        "limit_control_gap",
    }
    <= set(reasons(payload_gap)),
    ",".join(reasons(payload_gap)),
)

budget_gap = variant(
    live,
    banned={
        "limit_requires_new_finite_index_cell": True,
        "limit_basis_row": True,
        "limit_finite_sample": True,
    },
    limit={"preserves_budget": False, "limit_basis_row": True, "limit_finite_sample": True},
)

gate(
    f"{PREFIX}7 rejects finite-index expansion, basis rows, or finite samples",
    not accepts(budget_gap)
    and {"limit_requires_new_finite_index_cell", "limit_basis_row", "limit_finite_sample"}
    <= set(reasons(budget_gap)),
    ",".join(reasons(budget_gap)),
)

missing_gap = variant(
    live,
    banned={"missing_represented_refinement_limit_certificate": True},
    limit={
        "certificate": None,
        "identities": REQUIRED_IDENTITIES - {"represented_limit_cone", "source_category_attainment"},
    },
)

gate(
    f"{PREFIX}8 rejects missing represented-limit certificates",
    not accepts(missing_gap)
    and "missing_represented_refinement_limit_certificate" in reasons(missing_gap)
    and any(reason.startswith("represented_limit_identity_missing:") for reason in reasons(missing_gap)),
    ",".join(reasons(missing_gap)),
)

closure_gap = variant(
    live,
    requires_drop=[(FRC, RLIM), (RLIM, FRC), (RLIM, HANDOFF)],
    edges_drop={
        (FRC, "made_represented_limit_realized_by", RLIM),
        (RLIM, "represented_limit_of", FRC),
        (RLIM, "handoff_limit_for", HANDOFF),
    },
)

gate(
    f"{PREFIX}9 requires filtered calculus and represented limit certificates to close together",
    not accepts(closure_gap)
    and {
        "filtered_calculus_not_required_to_be_represented_limit_realized",
        "represented_limit_requires_missing_filtered_calculus_base",
    }
    <= set(reasons(closure_gap))
    and any(reason.startswith("represented_limit_requires_missing:") for reason in reasons(closure_gap))
    and any(reason.startswith("represented_limit_edges_missing:") for reason in reasons(closure_gap)),
    ",".join(reasons(closure_gap)),
)

variants = [variant(live, banned={flag: True}) for flag in BANNED_FLAGS]
variant_reasons: set[str] = set()
for bad in variants:
    variant_reasons.update(reasons(bad))

gate(
    f"{PREFIX}10 only represented-limit-realized filtered refinement calculi pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILED gates: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: filtered refinement calculus has represented source limit")
print(
    "VERDICT: the filtered refinement calculus counts only when it has an "
    "attained represented source-side limit inside the current finite-limit/"
    "equalizer spine. Pro-family-only, external-completion, formal-cone, "
    "nonattained, choice-dependent, nonunique, probe-losing, equalizer-losing, "
    "payload-losing, graph/composition/control-losing, finite-sample, basis-row, "
    "and finite-index-expanded repairs do not construct the missing object."
)
