#!/usr/bin/env python3
r"""No-go for using refinement-stage lineage as morphism evidence.

Doc 620 kills the frontier-map consistency/rejection ledger as positive
morphism evidence. A different possible repair is longitudinal: perhaps the
two doc-614 singleton residuals become reusable because the same labels persist
through the executable refinement stages.

That persistence is negative, not constructive. The labels appear in the
executable modules only as BANNED_FLAGS, rejected by the same documents that
introduce them. They do not appear in required dependencies, accepted added
atoms, witness ids, or current accepted frontier nodes.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_stage_lineage_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
import importlib
from pathlib import Path
from typing import Any

import yaml

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMSTAGELINEAGEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
LABELS = (
    "not_source_internal",
    "external",
    "oracle",
    "boundary_externality",
    "source_internality",
    "external_or_oracle",
)

MODULE_SPECS = (
    (
        574,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_cartesian_compatibility_diagram_contract",
    ),
    (
        576,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_represented_semantic_model_contract",
    ),
    (
        594,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_loc_verifier_trace_exec_global_contract",
    ),
    (
        595,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_class_localizer_trace_exec_global_contract",
    ),
    (
        596,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_action_classifier_trace_exec_global_contract",
    ),
    (
        597,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_confluent_action_classifier_trace_exec_global_contract",
    ),
    (
        598,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_nf_reflect_confluent_action_contract",
    ),
    (
        599,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_reflected_fixedpoint_contract",
    ),
    (
        600,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_fixedpoint_contract",
    ),
    (
        601,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_contract",
    ),
    (
        602,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_contract",
    ),
    (
        603,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_taxonomy_contract",
    ),
    (
        604,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_graph_contract",
    ),
    (
        605,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_witness_contract",
    ),
    (
        606,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_priority_contract",
    ),
    (
        608,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_typed_source_event_classifier_contract",
    ),
    (
        610,
        "scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract",
    ),
)

EXPECTED_NOT_SOURCE_INTERNAL_DOCS = (
    574,
    576,
    594,
    595,
    596,
    597,
    598,
    599,
    600,
    601,
    602,
    603,
    604,
    605,
    606,
    608,
    610,
)
EXPECTED_EXTERNAL_DOCS = (
    576,
    594,
    595,
    596,
    597,
    598,
    599,
    600,
    601,
    602,
    603,
    604,
    605,
    606,
    608,
    610,
)
EXPECTED_ORACLE_DOCS = (
    594,
    595,
    596,
    597,
    598,
    599,
    600,
    601,
    602,
    603,
    604,
    605,
    606,
    608,
    610,
)

failures: list[str] = []


def load_frontier() -> dict[str, Any]:
    data = yaml.safe_load(MAP_PATH.read_text())
    if not isinstance(data, dict):
        raise TypeError("frontier-map.yaml did not load as a mapping")
    return data


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def module_objects() -> dict[int, Any]:
    return {doc: importlib.import_module(name) for doc, name in MODULE_SPECS}


def label_hits(items: set[str] | list[str] | tuple[str, ...], label: str) -> set[str]:
    return {item for item in items if label in str(item)}


def banned_flags_by_label(modules: dict[int, Any]) -> dict[str, dict[int, tuple[str, ...]]]:
    by_label: dict[str, dict[int, tuple[str, ...]]] = {label: {} for label in LABELS}
    for doc, module in modules.items():
        flags = tuple(getattr(module, "BANNED_FLAGS"))
        for label in LABELS:
            hits = tuple(flag for flag in flags if label in flag)
            if hits:
                by_label[label][doc] = hits
    return by_label


def accepted_stage_label_hits(data: dict[str, Any], modules: dict[int, Any]) -> dict[str, set[str]]:
    hits = {label: set() for label in LABELS}
    for doc, module in modules.items():
        delta = data["deltas"].get(f"doc{doc}", {})
        accepted_fragments = set(getattr(module, "REQUIRED_DEPS", set()))
        accepted_fragments.update(delta.get("added_atoms", []))
        accepted_fragments.add(delta.get("witness", ""))
        for label in LABELS:
            hits[label].update(label_hits(accepted_fragments, label))
    return hits


def rejected_by_profile(data: dict[str, Any], flags: tuple[str, ...]) -> Counter[int]:
    repairs = data["rejected_repairs"]
    return Counter(repairs[flag]["rejected_by"] for flag in flags)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    runtime_data = load_map()
    frontier_data = load_frontier()
    modules = module_objects()
    accepted = accepted_nodes(frontier_data)
    rejected = set(frontier_data["current_requirements"]["rejected_repairs"])
    by_label = banned_flags_by_label(modules)
    accepted_stage_hits = accepted_stage_label_hits(frontier_data, modules)

    not_source_flags = tuple(
        flag for hits in by_label["not_source_internal"].values() for flag in hits
    )
    external_flags = tuple(flag for hits in by_label["external"].values() for flag in hits)
    oracle_flags = tuple(flag for hits in by_label["oracle"].values() for flag in hits)
    lineage_flags = not_source_flags + external_flags + oracle_flags
    rejected_profiles = {
        label: dict(sorted(rejected_by_profile(frontier_data, tuple(flag for hits in by_label[label].values() for flag in hits)).items()))
        for label in ("not_source_internal", "external", "oracle")
    }

    gate(
        f"{PREFIX}1",
        runtime_data["frontier"].get("current_doc", 0) >= 610
        and DOC610_WITNESS in runtime_data.get("witnesses", {})
        and KILLCOMPEVENTSIGACTION in accepted_nodes(runtime_data),
        f"frontier_doc={runtime_data['frontier']['current_doc']} doc610_witness={DOC610_WITNESS in runtime_data.get('witnesses', {})}",
    )
    gate(
        f"{PREFIX}2",
        IMPOSSIBLE_RESIDUAL_SURFACES == {EXTERNAL_SURFACE, SOURCE_INTERNAL_SURFACE}
        and IMPOSSIBLE_RESIDUAL_SURFACES <= MISSING_REUSED_CLASS_STATE
        and CLASS_OF[EXTERNAL_SURFACE] == "boundary_externality"
        and CLASS_OF[SOURCE_INTERNAL_SURFACE] == "source_internality",
        f"impossible={sorted(IMPOSSIBLE_RESIDUAL_SURFACES)}",
    )
    gate(
        f"{PREFIX}3",
        tuple(modules) == EXPECTED_NOT_SOURCE_INTERNAL_DOCS
        and all(hasattr(module, "BANNED_FLAGS") for module in modules.values()),
        f"stage_docs={tuple(modules)}",
    )
    gate(
        f"{PREFIX}4",
        tuple(by_label["not_source_internal"]) == EXPECTED_NOT_SOURCE_INTERNAL_DOCS
        and tuple(by_label["external"]) == EXPECTED_EXTERNAL_DOCS
        and tuple(by_label["oracle"]) == EXPECTED_ORACLE_DOCS
        and not by_label["boundary_externality"]
        and not by_label["source_internality"]
        and not by_label["external_or_oracle"],
        f"profiles={{'not_source_internal': {tuple(by_label['not_source_internal'])}, 'external': {tuple(by_label['external'])}, 'oracle': {tuple(by_label['oracle'])}}}",
    )
    gate(
        f"{PREFIX}5",
        all(not hits for hits in accepted_stage_hits.values()),
        f"accepted_stage_hits={{{', '.join(f'{label}: {len(hits)}' for label, hits in accepted_stage_hits.items())}}}",
    )
    gate(
        f"{PREFIX}6",
        all(flag in rejected for flag in lineage_flags)
        and all(flag not in accepted for flag in lineage_flags),
        f"lineage_flags={len(lineage_flags)} rejected={len([flag for flag in lineage_flags if flag in rejected])}",
    )
    gate(
        f"{PREFIX}7",
        rejected_by_profile(frontier_data, not_source_flags)
        == Counter({doc: 1 for doc in EXPECTED_NOT_SOURCE_INTERNAL_DOCS})
        and rejected_by_profile(frontier_data, external_flags)
        == Counter({doc: 1 for doc in EXPECTED_EXTERNAL_DOCS})
        and rejected_by_profile(frontier_data, oracle_flags)
        == Counter({doc: 1 for doc in EXPECTED_ORACLE_DOCS}),
        f"rejected_profiles={rejected_profiles}",
    )
    gate(
        f"{PREFIX}8",
        all(
            not label_hits(accepted, label)
            for label in (
                "not_source_internal",
                "external",
                "oracle",
                "boundary_externality",
                "source_internality",
                "external_or_oracle",
            )
        ),
        "current accepted frontier has no residual label/tail lineage nodes",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: stage-lineage morphism reuse fails")
    print(
        "VERDICT: longitudinal persistence of not_source_internal/external/oracle "
        "is negative diagnostic lineage. It lives in BANNED_FLAGS rejected by "
        "the same stages, not in accepted dependencies, added atoms, witness ids, "
        "or current accepted morphism evidence."
    )


if __name__ == "__main__":
    main()
