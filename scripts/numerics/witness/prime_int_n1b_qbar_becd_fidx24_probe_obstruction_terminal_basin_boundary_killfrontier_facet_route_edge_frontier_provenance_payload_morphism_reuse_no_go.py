#!/usr/bin/env python3
r"""No-go for using frontier provenance payloads as residual morphism evidence.

Doc 621 kills executable stage-lineage persistence through banned flags,
required dependencies, added atoms, and witness ids. This witness checks the
full frontier-map provenance payload records: deltas and witnesses.

Those records contain no exact doc-614 residual labels and no broad
external/oracle/not/tail tokens. Their generic vocabulary is the already-known
construction provenance for the source-square chain, not a residual-specific
morphism.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_frontier_provenance_payload_morphism_reuse_no_go
"""

from __future__ import annotations

from typing import Any

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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMFRONTPROVENANCEPAYLOADMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

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
BROAD_RESIDUAL_TOKENS = ("external", "oracle", "not", "tail")
GENERIC_TOKENS = ("source", "internal", "boundary", "class", "obstruction")
EXPECTED_SECTION_SIZES = {"deltas": 84, "witnesses": 84}
EXPECTED_GENERIC_COUNTS = {
    "deltas": {
        "source": 42,
        "internal": 27,
        "boundary": 8,
        "class": 4,
        "obstruction": 15,
    },
    "witnesses": {
        "source": 15,
        "internal": 2,
        "boundary": 8,
        "class": 4,
        "obstruction": 15,
    },
}

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def provenance_entries(
    data: dict[str, Any], section: str
) -> list[tuple[str, str, dict[str, Any]]]:
    return [(section, key, value) for key, value in data[section].items()]


def provenance_blob(entry: tuple[str, str, dict[str, Any]]) -> str:
    section, key, value = entry
    return f"{section} {key} {value}"


def section_hits(
    data: dict[str, Any], section: str, label: str
) -> list[tuple[str, str, dict[str, Any]]]:
    return [
        entry
        for entry in provenance_entries(data, section)
        if label in provenance_blob(entry)
    ]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    section_sizes = {section: len(data[section]) for section in EXPECTED_SECTION_SIZES}
    exact_hit_counts = {
        section: {
            label: len(section_hits(data, section, label))
            for label in EXACT_RESIDUAL_LABELS
        }
        for section in EXPECTED_SECTION_SIZES
    }
    broad_hit_counts = {
        section: {
            label: len(section_hits(data, section, label))
            for label in BROAD_RESIDUAL_TOKENS
        }
        for section in EXPECTED_SECTION_SIZES
    }
    generic_counts = {
        section: {
            token: len(section_hits(data, section, token)) for token in GENERIC_TOKENS
        }
        for section in EXPECTED_SECTION_SIZES
    }
    delta_docs = {value["doc"] for value in data["deltas"].values()}
    witness_docs = {value["doc"] for value in data["witnesses"].values()}

    gate(
        f"{PREFIX}1",
        data["frontier"].get("current_doc", 0) >= 610
        and DOC610_WITNESS in data.get("witnesses", {})
        and KILLCOMPEVENTSIGACTION in accepted,
        f"frontier_doc={data['frontier']['current_doc']} doc610_witness={DOC610_WITNESS in data.get('witnesses', {})}",
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
        section_sizes == EXPECTED_SECTION_SIZES,
        f"section_sizes={section_sizes}",
    )
    gate(
        f"{PREFIX}4",
        delta_docs == witness_docs
        and len(delta_docs) == 84
        and min(delta_docs) == 525
        and max(delta_docs) == 610,
        f"delta_docs={len(delta_docs)} witness_docs={len(witness_docs)} min={min(delta_docs)} max={max(delta_docs)}",
    )
    gate(
        f"{PREFIX}5",
        all(
            not section_hits(data, section, label)
            for section in EXPECTED_SECTION_SIZES
            for label in EXACT_RESIDUAL_LABELS
        ),
        f"exact_hit_counts={exact_hit_counts}",
    )
    gate(
        f"{PREFIX}6",
        all(
            not section_hits(data, section, label)
            for section in EXPECTED_SECTION_SIZES
            for label in BROAD_RESIDUAL_TOKENS
        ),
        f"broad_hit_counts={broad_hit_counts}",
    )
    gate(
        f"{PREFIX}7",
        all(
            not section_hits(data, section, surface)
            for section in EXPECTED_SECTION_SIZES
            for surface in IMPOSSIBLE_RESIDUAL_SURFACES
        ),
        "exact residual surface strings do not occur as provenance payload data",
    )
    gate(
        f"{PREFIX}8",
        generic_counts == EXPECTED_GENERIC_COUNTS,
        f"generic_counts={generic_counts}",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: frontier provenance payload morphism reuse fails")
    print(
        "VERDICT: deltas and witnesses provenance payloads contain no residual "
        "labels or broad external/oracle/not/tail tokens. Their generic "
        "vocabulary is source-square provenance, not residual-specific "
        "morphism evidence."
    )


if __name__ == "__main__":
    main()
