#!/usr/bin/env python3
r"""No-go for using the consistency/rejection ledger as morphism evidence.

Doc 619 kills the existing route-graph anchor witnesses as a repair for the
doc-614 singleton residual classes. The next existing structure outside the
payload and graph layers is the frontier-map consistency/rejection ledger.

That layer is negative bookkeeping, not hidden positive morphism evidence.
The singleton class labels are not accepted nodes and do not appear as rejected
repair nodes. The visible labels external, oracle, and not_source_internal
appear only as rejected repairs/exclusions, with no accepted counterpart.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_consistency_rejection_morphism_reuse_no_go
"""

from __future__ import annotations

from collections import Counter
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
    SOURCE_EVENTS,
    load_map,
)
from scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_surface_reused_residual_class_state_no_go import (
    IMPOSSIBLE_RESIDUAL_SURFACES,
)


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONSISTREJECTMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"
ROOT = Path(__file__).resolve().parents[3]
MAP_PATH = ROOT / "research/proof/frontier-map.yaml"

EXTERNAL_SURFACE = "entry_boundary:obstruction:external_or_oracle"
SOURCE_INTERNAL_SURFACE = (
    "escape_boundary:center_eliminator_semantics_evaluation_obstruction_terminal_basin_fixedpoint_trace_exec_global_parametric_contractible_loop_complete_path_pres_law_nf_not_source_internal"
)
LABELS = (
    "boundary_externality",
    "source_internality",
    "external_or_oracle",
    "not_source_internal",
    "external",
    "oracle",
)
EXPECTED_NOT_SOURCE_INTERNAL_PROFILE = Counter(
    {
        574: 1,
        576: 1,
        594: 1,
        595: 1,
        596: 1,
        597: 1,
        598: 1,
        599: 1,
        600: 1,
        601: 1,
        602: 1,
        603: 1,
        604: 1,
        605: 1,
        606: 1,
        608: 1,
        610: 1,
    }
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


def current_rejected(data: dict[str, Any]) -> set[str]:
    return set(data["current_requirements"]["rejected_repairs"])


def rejected_by_profile(data: dict[str, Any], hits: set[str]) -> Counter[int]:
    repairs = data["rejected_repairs"]
    return Counter(repairs[hit]["rejected_by"] for hit in hits)


def hits_in(items: set[str], label: str) -> set[str]:
    return {item for item in items if label in item}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    runtime_data = load_map()
    frontier_data = load_frontier()
    accepted = accepted_nodes(frontier_data)
    rejected = current_rejected(frontier_data)
    repairs = frontier_data["rejected_repairs"]
    excludes = frontier_data["consistency_rules"]["excludes_current"]

    doc610_rejected = {key for key in rejected if repairs[key]["rejected_by"] == 610}
    accepted_hits = {label: hits_in(accepted, label) for label in LABELS}
    accepted_hit_counts = {label: len(hits) for label, hits in accepted_hits.items()}
    rejected_hits = {label: hits_in(rejected, label) for label in LABELS}

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
        len(rejected) == 2109
        and len(doc610_rejected) == 36
        and set(excludes[KILLCOMPEVENTSIGACTION]) == doc610_rejected,
        f"current_rejected={len(rejected)} doc610_rejected={len(doc610_rejected)}",
    )
    gate(
        f"{PREFIX}4",
        all(not accepted_hits[label] for label in LABELS),
        f"accepted_hits={accepted_hit_counts}",
    )
    gate(
        f"{PREFIX}5",
        not rejected_hits["boundary_externality"]
        and not rejected_hits["source_internality"]
        and not rejected_hits["external_or_oracle"],
        "singleton class labels and exact external_or_oracle tail are not rejected-repair nodes",
    )
    gate(
        f"{PREFIX}6",
        len(rejected_hits["not_source_internal"]) == 17
        and rejected_by_profile(frontier_data, rejected_hits["not_source_internal"])
        == EXPECTED_NOT_SOURCE_INTERNAL_PROFILE,
        f"not_source_internal_profile={dict(sorted(rejected_by_profile(frontier_data, rejected_hits['not_source_internal']).items()))}",
    )
    gate(
        f"{PREFIX}7",
        len(rejected_hits["external"]) == 64
        and len(rejected_hits["oracle"]) == 21
        and all(hit in rejected for hit in rejected_hits["external"] | rejected_hits["oracle"]),
        f"external_rejected={len(rejected_hits['external'])} oracle_rejected={len(rejected_hits['oracle'])}",
    )
    gate(
        f"{PREFIX}8",
        SOURCE_EVENTS[EXTERNAL_SURFACE]["tail"] == "external_or_oracle"
        and SOURCE_EVENTS[SOURCE_INTERNAL_SURFACE]["tail"] == "not_source_internal"
        and rejected_hits["not_source_internal"].isdisjoint(accepted)
        and rejected_hits["external"].isdisjoint(accepted)
        and rejected_hits["oracle"].isdisjoint(accepted),
        "visible singleton labels occur only on rejected/excluded repairs, not accepted morphism evidence",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: consistency/rejection morphism reuse fails")
    print(
        "VERDICT: the frontier-map consistency layer does not repair the doc614 "
        "singletons. It records rejected external/oracle/not_source_internal "
        "failure modes, but supplies no accepted morphism node for "
        "boundary_externality or source_internality."
    )


if __name__ == "__main__":
    main()
