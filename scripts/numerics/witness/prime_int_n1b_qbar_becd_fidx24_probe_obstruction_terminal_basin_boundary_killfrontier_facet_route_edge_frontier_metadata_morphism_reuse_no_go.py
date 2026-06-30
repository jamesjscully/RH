#!/usr/bin/env python3
r"""No-go for using frontier metadata as residual morphism evidence.

Docs 620-623 kill consistency/rejection bookkeeping, stage-lineage diagnostics,
audit-fanout wiring, and typed rule-family dispatch. A nearby remaining source
is the non-current frontier metadata: contexts, claims, context bridges, and
kill-frontier records.

That metadata is orientation and failure bookkeeping. It contains no exact
doc-614 residual class/surface/tail labels as positive evidence. The only broad
external/oracle mentions are generic "without external ..." claim predicates
or negative kill-frontier target conditions.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_frontier_metadata_morphism_reuse_no_go
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_reused_class_state_no_go import (
    CLASS_OF,
    MISSING_REUSED_CLASS_STATE,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_compositional_event_signature_contract import (
    EXPECTED_WITNESS as DOC610_WITNESS,
    KILLCOMPEVENTSIGACTION,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFRONTIERMETADATAMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
EXACT_RESIDUAL_LABELS = (
    "boundary_externality",
    "source_internality",
    "external_or_oracle",
    "not_source_internal",
)
BROAD_LABELS = ("external", "oracle")
EXPECTED_EXTERNAL_CLAIMS = {
    "admissible_probe_adjoint_pairing",
    "admissible_probe_pasting_stable_cyclic_ambidextrous_mate_coherent_descent_effective_beck_chevalley_exact_evaluation_natural_represented_semantic_model_semantic_conservative_invariant_reflecting_executable_critical_pair_diamond_coherent_monoidal_exact_dagger_compatible_functorial_normalizing_confluent_computation_stable_center_eliminator_realized_center_realized_internally_contractible_globally_unique_endomorphism_trivial_automorphism_rigid_cartesian_compatibility_diagram_represented_limit_source_constraint_bundle_represented_limit_realized_filtered_cofinal_refinement_calculus_stable_refinement_descent_stable_mediator_generated_composition_stable_joint_source_law_dd4_active_rigid_primitive_effective_grothendieck_lift",
}
EXPECTED_EXTERNAL_CLAIM_PREDICATES = {
    "nonpositive_source_pairing_makes_dagger_adjoint_without_external_trace",
    "cyclic_ambidextrous_mate_beck_chevalley_evaluation_is_pasting_stable_for_vertical_horizontal_interchange_unit_trace_sliding_boundary_graph_control_and_handoff_routes_without_external_equipment",
}

failures: list[str] = []


def load_frontier() -> dict[str, Any]:
    data = yaml.safe_load(MAP_PATH.read_text())
    if not isinstance(data, dict):
        raise TypeError("frontier-map.yaml did not load as a mapping")
    return data


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def metadata_entries(data: dict[str, Any], section: str) -> list[tuple[str, Any]]:
    if section == "kill_frontier":
        return [(entry["id"], entry) for entry in data["kill_frontier"]["current"]]
    obj = data[section]
    if not isinstance(obj, dict):
        raise TypeError(f"{section} did not load as a mapping")
    return list(obj.items())


def hits(entries: list[tuple[str, Any]], label: str) -> list[tuple[str, Any]]:
    return [(key, value) for key, value in entries if label in f"{key} {value}"]


def section_label_hits(data: dict[str, Any], section: str, label: str) -> list[tuple[str, Any]]:
    return hits(metadata_entries(data, section), label)


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    runtime_data = load_map()
    frontier_data = load_frontier()
    accepted = accepted_nodes(frontier_data)
    sections = ("contexts", "claims", "context_bridges", "kill_frontier")
    section_sizes = {
        section: len(metadata_entries(frontier_data, section)) for section in sections
    }

    claim_entries = metadata_entries(frontier_data, "claims")
    kill_entries = metadata_entries(frontier_data, "kill_frontier")
    external_claim_hits = section_label_hits(frontier_data, "claims", "external")
    external_kill_hits = section_label_hits(frontier_data, "kill_frontier", "external")
    oracle_kill_hits = section_label_hits(frontier_data, "kill_frontier", "oracle")

    exact_hit_counts = {
        section: {
            label: len(section_label_hits(frontier_data, section, label))
            for label in EXACT_RESIDUAL_LABELS
        }
        for section in sections
    }
    broad_hit_counts = {
        section: {
            label: len(section_label_hits(frontier_data, section, label))
            for label in BROAD_LABELS
        }
        for section in sections
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
        section_sizes
        == {"contexts": 9, "claims": 57, "context_bridges": 2, "kill_frontier": 73},
        f"section_sizes={section_sizes}",
    )
    gate(
        f"{PREFIX}4",
        all(
            not section_label_hits(frontier_data, section, label)
            for section in sections
            for label in EXACT_RESIDUAL_LABELS
        ),
        f"exact_hit_counts={exact_hit_counts}",
    )
    gate(
        f"{PREFIX}5",
        not section_label_hits(frontier_data, "contexts", "external")
        and not section_label_hits(frontier_data, "contexts", "oracle")
        and not section_label_hits(frontier_data, "context_bridges", "external")
        and not section_label_hits(frontier_data, "context_bridges", "oracle")
        and not section_label_hits(frontier_data, "claims", "oracle"),
        f"broad_hit_counts={broad_hit_counts}",
    )
    gate(
        f"{PREFIX}6",
        {key for key, _ in external_claim_hits} == EXPECTED_EXTERNAL_CLAIMS
        and {value["predicate"] for _, value in external_claim_hits}
        == EXPECTED_EXTERNAL_CLAIM_PREDICATES
        and all("without_external" in value["predicate"] for _, value in external_claim_hits),
        f"external_claims={[key for key, _ in external_claim_hits]}",
    )
    gate(
        f"{PREFIX}7",
        len(external_kill_hits) == 37
        and len(oracle_kill_hits) == 17
        and all("target" in value and "prove every" in value["target"] for _, value in external_kill_hits)
        and all("target" in value and "prove every" in value["target"] for _, value in oracle_kill_hits)
        and all("external" not in key and "oracle" not in key for key, _ in external_kill_hits + oracle_kill_hits),
        f"external_kill_hits={len(external_kill_hits)} oracle_kill_hits={len(oracle_kill_hits)}",
    )
    gate(
        f"{PREFIX}8",
        all(not any(label in node for node in accepted) for label in EXACT_RESIDUAL_LABELS + BROAD_LABELS),
        "current accepted nodes contain no residual or broad external/oracle metadata node",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: frontier metadata morphism reuse fails")
    print(
        "VERDICT: contexts, claims, context bridges, and kill-frontier records "
        "do not provide residual morphism evidence. Exact residual labels are "
        "absent; broad external/oracle mentions are either without_external "
        "claim predicates or negative kill-target conditions."
    )


if __name__ == "__main__":
    main()
