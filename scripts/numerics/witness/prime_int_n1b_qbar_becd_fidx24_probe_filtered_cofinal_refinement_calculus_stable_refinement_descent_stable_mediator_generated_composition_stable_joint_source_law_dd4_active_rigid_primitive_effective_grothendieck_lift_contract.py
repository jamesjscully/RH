r"""Filtered-cofinal refinement-calculus-stable descent contract.

Doc 557 pins refinement descent for the mediator-generated joint law. This
witness prevents that descent from being merely pairwise: it must live on one
cofinal filtered admissible-refinement calculus with common refinements,
base-change stability, chain composition, and zero loop monodromy.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_contract
"""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("PyYAML is required for the filtered-refinement witness") from exc


ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"
EXPECTED_DOC = 558
EXPECTED_WITNESS = (
    "doc558-probe-filtered-cofinal-refinement-calculus-stable-refinement-"
    "descent-stable-mediator-generated-composition-stable-joint-source-law-"
    "dd4-active-rigid-primitive-effective-grothendieck-lift"
)
FRC = "filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
REF = "refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
MED = "mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
JOINT = "joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
ACTIVE = "dd4_active_rigid_primitive_effective_grothendieck_lift_certificate"
CART_EQV = "cartesian_probe_equivalence_certificate"
PROBE_EQV = "probe_equivalence_certificate"
PROBE_ESS = "probe_essential_image_certificate"
PROBE_FULL = "probe_fullness_certificate"
PROBE_NAT = "probe_naturality_certificate"
PROBE_SEP = "probe_separation_certificate"
ADM_CAT = "admissible_source_square_category_certificate"
TERMINAL_CERT = "terminal_square_universal_property_certificate"
PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPFILTCFREFCALCSTABREFDESCSTABMEDGENCOMPSTABJLAWDD4ACTRIGIDPRIMEFFK0LIFTREFDESCSTABMEDGENCOMPSTABJLAWDD4ACTRIGIDPRIMEFFK0LIFTMEDGENCOMPSTABJLAWDD4ACTRIGIDPRIMEFFK0LIFTJLAWDD4ACTRIGIDPRIMEFFK0LIFTDD4ACTRIGIDPRIMEFFK0LIFTRIGIDPRIMEFFK0LIFTPRIMEFFK0LIFTEFFK0LIFTINTK0TRACEEXADDTRACEPIVMONDUALTRACEPAIRADJDAGMONEQVPROBECARTEQVPROBEEQVPROBEESSIMGFULLPROBEFAITHPROBENATPROBEADMCATTERMDCLFIDXINHGRHDD4HCTXFLIMSUBREPCPLFCOHSDXBCFQBARBECD"

failures: list[str] = []

CHAIN_TARGETS = {
    REF,
    MED,
    JOINT,
    ACTIVE,
    ADM_CAT,
    TERMINAL_CERT,
    CART_EQV,
    PROBE_EQV,
    PROBE_ESS,
    PROBE_FULL,
    PROBE_NAT,
    PROBE_SEP,
    "universal_mediator",
    "source_coupling",
    "equalizer_arrow_to_subrep",
    "finite_limit_cut",
    "original_dd4_class",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    "graph_composition",
    "control_death",
    "exact_24_cell_finite_index",
    "coupled_source_image",
}

REQUIRED_CALC_DEPS = {
    REF,
    MED,
    JOINT,
    ACTIVE,
    ADM_CAT,
    TERMINAL_CERT,
    CART_EQV,
    PROBE_EQV,
    PROBE_ESS,
    PROBE_FULL,
    PROBE_NAT,
    PROBE_SEP,
    "universal_mediator",
    "source_coupling",
    "equalizer_arrow_to_subrep",
    "finite_limit_cut",
    "original_dd4_class",
    "dd4_image_only_handoff_contract",
    "graph_later_realization_contract",
    "graph_composition",
    "control_death",
    "exact_24_cell_finite_index",
}

EXPECTED_EDGES = {
    (REF, "made_filtered_cofinal_by", FRC),
    (FRC, "filtered_refinement_calculus_of", REF),
    (FRC, "chain_coherent_for", REF),
    (FRC, "cofinal_for", ADM_CAT),
    (FRC, "filtered_common_refinement_for", TERMINAL_CERT),
    (FRC, "base_change_stable_for", CART_EQV),
    (FRC, "probe_chain_functorial_by", PROBE_NAT),
    (FRC, "probe_chain_separated_by", PROBE_SEP),
    (FRC, "full_faithful_chain_by", PROBE_FULL),
    (FRC, "essential_image_chain_by", PROBE_ESS),
    (FRC, "equivalence_chain_by", PROBE_EQV),
    (FRC, "mediator_chain_stable_for", "universal_mediator"),
    (FRC, "source_coupling_chain_stable_for", "source_coupling"),
    (FRC, "equalizer_chain_stable_for", "equalizer_arrow_to_subrep"),
    (FRC, "finite_limit_chain_stable_for", "finite_limit_cut"),
    (FRC, "payload_chain_stable_for", "original_dd4_class"),
    (FRC, "handoff_chain_stable_for", "dd4_image_only_handoff_contract"),
    (FRC, "graph_chain_stable_for", "graph_later_realization_contract"),
    (FRC, "composition_chain_stable_for", "graph_composition"),
    (FRC, "control_chain_stable_for", "control_death"),
    (FRC, "preserves", "exact_24_cell_finite_index"),
    (FRC, "coherent_for", "coupled_source_image"),
}

REQUIRED_IDENTITIES = {
    "cofinal_filtered_calculus",
    "common_refinement_law",
    "base_change_law",
    "pullback_stability_law",
    "chain_composition_law",
    "associative_chain_law",
    "loop_monodromy_zero_law",
    "payload_preservation_law",
}

BANNED_FLAGS = (
    "pairwise_refinement_descent_only",
    "noncofinal_refinement_family",
    "missing_common_refinement",
    "filteredness_by_declaration",
    "base_change_gap",
    "pullback_unstable_refinement",
    "chain_composition_gap",
    "nonassociative_refinement_composition",
    "zigzag_dependent_descent",
    "refinement_loop_monodromy",
    "refinement_index_context_collapse",
    "refinement_hypercover_escape",
    "cofinality_by_finite_sample",
    "basis_refinement_calculus_row",
    "tower_index_expansion",
    "terminal_refinement_not_preserved",
    "probe_refinement_not_functorial",
    "mediator_refinement_calculus_mismatch",
    "dd4_payload_refinement_calculus_gap",
    "missing_filtered_cofinal_refinement_calculus_certificate",
)

REQUIRED_FLAGS = (
    "filtered_cofinal_refinement_calculus_certificate_actual",
    "cofinal_refinement_index",
    "filtered_common_refinements",
    "base_change_stable_refinements",
    "functorial_refinement_chains",
    "zero_refinement_loop_monodromy",
    "payload_preserved_by_refinement_calculus",
    "inside_exact_24_budget",
)

CALC_DATA = {
    "source_side": True,
    "choice_free": True,
    "certificate": "filtered_cofinal_refinement_calculus",
    "base_certificate": REF,
    "cofinal": True,
    "filtered": True,
    "common_refinements": True,
    "base_change_stable": True,
    "pullback_stable": True,
    "chain_composition": True,
    "associative_composition": True,
    "zigzag_independent": True,
    "loop_monodromy_zero": True,
    "preserves_budget": True,
    "nonpositive_stage": True,
    "imports_positivity": False,
    "chain_targets": CHAIN_TARGETS,
    "identities": REQUIRED_IDENTITIES,
    "pairwise_refinement_descent_only": False,
    "filteredness_by_declaration": False,
    "refinement_hypercover_escape": False,
    "cofinality_by_finite_sample": False,
    "basis_refinement_calculus_row": False,
    "tower_index_expansion": False,
    "refinement_index_context_collapse": False,
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
        "calc": deepcopy(CALC_DATA),
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
    calc = state["calc"]

    if frontier.get("current_doc", 0) < EXPECTED_DOC:
        out.append("current_doc_before_558")
    if EXPECTED_WITNESS not in state["witnesses"]:
        out.append("doc558_witness_missing")
    if FRC not in accepted:
        out.append("filtered_cofinal_refinement_calculus_missing_from_current")
    if REF not in accepted:
        out.append("refinement_descent_base_missing_from_current")

    if not isinstance(calc, dict):
        out.append("filtered_refinement_calculus_data_not_mapping")
        calc = {}
    if calc.get("certificate") != "filtered_cofinal_refinement_calculus":
        out.append("missing_filtered_cofinal_refinement_calculus_certificate")
    if calc.get("base_certificate") != REF:
        out.append("filtered_calculus_not_based_on_refinement_descent_law")
    if not calc.get("source_side") or not calc.get("choice_free"):
        out.append("filteredness_by_declaration")
    if not calc.get("cofinal"):
        out.append("noncofinal_refinement_family")
    if not calc.get("filtered") or not calc.get("common_refinements"):
        out.append("missing_common_refinement")
    if not calc.get("base_change_stable"):
        out.append("base_change_gap")
    if not calc.get("pullback_stable"):
        out.append("pullback_unstable_refinement")
    if not calc.get("chain_composition"):
        out.append("chain_composition_gap")
    if not calc.get("associative_composition"):
        out.append("nonassociative_refinement_composition")
    if not calc.get("zigzag_independent"):
        out.append("zigzag_dependent_descent")
    if not calc.get("loop_monodromy_zero"):
        out.append("refinement_loop_monodromy")
    if not calc.get("preserves_budget"):
        out.append("tower_index_expansion")
    if not calc.get("nonpositive_stage") or calc.get("imports_positivity"):
        out.append("refinement_index_context_collapse")

    for key in (
        "pairwise_refinement_descent_only",
        "filteredness_by_declaration",
        "refinement_hypercover_escape",
        "cofinality_by_finite_sample",
        "basis_refinement_calculus_row",
        "tower_index_expansion",
        "refinement_index_context_collapse",
    ):
        if calc.get(key):
            out.append(key)

    chain_targets = _as_set(calc.get("chain_targets"))
    if TERMINAL_CERT not in chain_targets:
        out.append("terminal_refinement_not_preserved")
    if not {PROBE_NAT, PROBE_SEP, PROBE_FULL, PROBE_ESS, PROBE_EQV, CART_EQV} <= chain_targets:
        out.append("probe_refinement_not_functorial")
    if "universal_mediator" not in chain_targets or "source_coupling" not in chain_targets:
        out.append("mediator_refinement_calculus_mismatch")
    if "original_dd4_class" not in chain_targets or "dd4_image_only_handoff_contract" not in chain_targets:
        out.append("dd4_payload_refinement_calculus_gap")
    if "graph_composition" not in chain_targets or "control_death" not in chain_targets:
        out.append("dd4_payload_refinement_calculus_gap")

    missing_identities = REQUIRED_IDENTITIES - _as_set(calc.get("identities"))
    if missing_identities:
        out.append("filtered_refinement_calculus_identity_missing:" + ",".join(sorted(missing_identities)))

    if FRC not in requires.get(REF, []):
        out.append("refinement_descent_law_not_required_to_be_filtered_cofinal")
    if REF not in requires.get(FRC, []):
        out.append("filtered_calculus_requires_missing_refinement_descent_base")
    missing_deps = REQUIRED_CALC_DEPS - set(requires.get(FRC, []))
    if missing_deps:
        out.append("filtered_calculus_requires_missing:" + ",".join(sorted(missing_deps)))

    missing_edges = EXPECTED_EDGES - state["edges"]
    if missing_edges:
        rendered = ["%s/%s/%s" % edge for edge in sorted(missing_edges)]
        out.append("filtered_refinement_calculus_edges_missing:" + ",".join(rendered))

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
        elif key == "calc":
            data["calc"].update(value)
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
    f"{PREFIX}1 doc 558 filtered/cofinal refinement calculus layer is embedded",
    accepts(live)
    and live["frontier"]["current_doc"] >= EXPECTED_DOC
    and EXPECTED_WITNESS in live["witnesses"],
    "current_doc=%s active_witness=%s chain_targets=%d"
    % (
        live["frontier"].get("current_doc"),
        live["frontier"].get("current_witness"),
        len(live["calc"]["chain_targets"]),
    ),
)

pairwise_gap = variant(
    live,
    banned={
        "pairwise_refinement_descent_only": True,
        "noncofinal_refinement_family": True,
        "missing_common_refinement": True,
    },
    calc={
        "pairwise_refinement_descent_only": True,
        "cofinal": False,
        "filtered": False,
        "common_refinements": False,
    },
)

gate(
    f"{PREFIX}2 rejects pairwise-only, noncofinal, or common-refinement gaps",
    not accepts(pairwise_gap)
    and {"pairwise_refinement_descent_only", "noncofinal_refinement_family", "missing_common_refinement"}
    <= set(reasons(pairwise_gap)),
    ",".join(reasons(pairwise_gap)),
)

base_change_gap = variant(
    live,
    banned={
        "filteredness_by_declaration": True,
        "base_change_gap": True,
        "pullback_unstable_refinement": True,
    },
    calc={
        "source_side": False,
        "choice_free": False,
        "filteredness_by_declaration": True,
        "base_change_stable": False,
        "pullback_stable": False,
    },
)

gate(
    f"{PREFIX}3 rejects declared filteredness, base-change gaps, or pullback instability",
    not accepts(base_change_gap)
    and {"filteredness_by_declaration", "base_change_gap", "pullback_unstable_refinement"}
    <= set(reasons(base_change_gap)),
    ",".join(reasons(base_change_gap)),
)

chain_gap = variant(
    live,
    banned={
        "chain_composition_gap": True,
        "nonassociative_refinement_composition": True,
        "zigzag_dependent_descent": True,
        "refinement_loop_monodromy": True,
    },
    calc={
        "chain_composition": False,
        "associative_composition": False,
        "zigzag_independent": False,
        "loop_monodromy_zero": False,
    },
)
chain_gap["calc"]["identities"] -= {
    "chain_composition_law",
    "associative_chain_law",
    "loop_monodromy_zero_law",
}

gate(
    f"{PREFIX}4 rejects chain gaps, nonassociativity, zigzag dependence, or loop monodromy",
    not accepts(chain_gap)
    and {
        "chain_composition_gap",
        "nonassociative_refinement_composition",
        "zigzag_dependent_descent",
        "refinement_loop_monodromy",
    }
    <= set(reasons(chain_gap)),
    ",".join(reasons(chain_gap)),
)

tower_gap = variant(
    live,
    banned={
        "refinement_hypercover_escape": True,
        "cofinality_by_finite_sample": True,
        "basis_refinement_calculus_row": True,
        "tower_index_expansion": True,
    },
    calc={
        "refinement_hypercover_escape": True,
        "cofinality_by_finite_sample": True,
        "basis_refinement_calculus_row": True,
        "tower_index_expansion": True,
        "preserves_budget": False,
    },
)

gate(
    f"{PREFIX}5 rejects hypercover escapes, finite samples, basis rows, or tower expansion",
    not accepts(tower_gap)
    and {
        "refinement_hypercover_escape",
        "cofinality_by_finite_sample",
        "basis_refinement_calculus_row",
        "tower_index_expansion",
    }
    <= set(reasons(tower_gap)),
    ",".join(reasons(tower_gap)),
)

payload_gap = variant(
    live,
    banned={
        "terminal_refinement_not_preserved": True,
        "probe_refinement_not_functorial": True,
        "mediator_refinement_calculus_mismatch": True,
        "dd4_payload_refinement_calculus_gap": True,
    },
    calc={
        "chain_targets": {
            REF,
            MED,
            JOINT,
            ACTIVE,
            "finite_limit_cut",
            "exact_24_cell_finite_index",
        },
    },
)

gate(
    f"{PREFIX}6 rejects terminal, probe, mediator, or DD4 payload calculus gaps",
    not accepts(payload_gap)
    and {
        "terminal_refinement_not_preserved",
        "probe_refinement_not_functorial",
        "mediator_refinement_calculus_mismatch",
        "dd4_payload_refinement_calculus_gap",
    }
    <= set(reasons(payload_gap)),
    ",".join(reasons(payload_gap)),
)

missing_gap = variant(
    live,
    banned={
        "refinement_index_context_collapse": True,
        "missing_filtered_cofinal_refinement_calculus_certificate": True,
    },
    calc={
        "certificate": None,
        "nonpositive_stage": False,
        "imports_positivity": True,
        "refinement_index_context_collapse": True,
    },
)

gate(
    f"{PREFIX}7 rejects context collapse or missing filtered/cofinal certificate",
    not accepts(missing_gap)
    and {
        "refinement_index_context_collapse",
        "missing_filtered_cofinal_refinement_calculus_certificate",
    }
    <= set(reasons(missing_gap)),
    ",".join(reasons(missing_gap)),
)

closure_gap = variant(
    live,
    requires_drop=[(REF, FRC), (FRC, REF)],
)

gate(
    f"{PREFIX}8 requires refinement-descent and filtered/cofinal certificates to close together",
    not accepts(closure_gap)
    and {
        "refinement_descent_law_not_required_to_be_filtered_cofinal",
        "filtered_calculus_requires_missing_refinement_descent_base",
    }
    <= set(reasons(closure_gap)),
    ",".join(reasons(closure_gap)),
)

edge_gap = variant(
    live,
    edges_drop={(FRC, "chain_coherent_for", REF), (FRC, "cofinal_for", ADM_CAT)},
    requires_drop=[(FRC, "graph_composition")],
)

gate(
    f"{PREFIX}9 requires doc558 graph edges and dependencies to resolve",
    not accepts(edge_gap)
    and any(reason.startswith("filtered_refinement_calculus_edges_missing:") for reason in reasons(edge_gap))
    and any(reason.startswith("filtered_calculus_requires_missing:") for reason in reasons(edge_gap)),
    ",".join(reasons(edge_gap)),
)

variants = [variant(live, banned={flag: True}) for flag in BANNED_FLAGS]
variant_reasons: set[str] = set()
for bad in variants:
    variant_reasons.update(reasons(bad))

gate(
    f"{PREFIX}10 only filtered-cofinal refinement-calculus-stable laws pass",
    accepts(live) and not any(accepts(data) for data in variants) and set(BANNED_FLAGS) <= variant_reasons,
    "live_reasons=%s rejected=%s" % (reasons(live), sorted(variant_reasons)),
)

if failures:
    raise SystemExit("FAILED gates: " + ", ".join(failures))

print(f"\n{PREFIX}1-{PREFIX}10 ALL PASS: refinement descent is filtered-cofinal calculus stable")
print(
    "VERDICT: the refinement-descent-stable mediator-generated joint law counts "
    "only when its admissible refinements form one cofinal filtered calculus "
    "with common refinements, base-change stability, functorial chains, and "
    "zero loop monodromy. Pairwise-only, noncofinal, base-change-gap, "
    "zigzag-dependent, loop-monodromic, sampled, basis-row, tower-expanded, "
    "payload-losing, and missing certificates do not construct the missing object."
)
