#!/usr/bin/env python3
r"""No-go for using the frontier control plane as residual morphism evidence.

Docs 620-627 kill rejection bookkeeping, metadata, accepted graph/node payloads,
and provenance payloads. The remaining structured frontier-map compartments are
the current frontier descriptor and the positive consistency-rule payloads.

They contain no exact doc-614 residual labels and no broad external/oracle/not/
tail tokens. Their visible vocabulary is generic source-square control-plane
bookkeeping, not residual-specific morphism evidence.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_fidx24_probe_obstruction_terminal_basin_boundary_killfrontier_facet_route_edge_control_plane_morphism_reuse_no_go
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


PREFIX = "CATCOHSRCPRESETACARTCOHGMGBFCARTCOHGMFINEQIDUPCENTERELIMCONTROLPLANEMORPHREUSENOGOEDGEFACETKILLBNDRYBASINFIXPTNFREFLCONFLACTIONCLASSLOCVERIFTRACEEXECGLOBCONTR"

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
EXPECTED_SECTION_SIZES = {
    "frontier": 7,
    "consistency_requires": 86,
    "consistency_context_separation": 4,
}
EXPECTED_GENERIC_COUNTS = {
    "frontier": {
        "source": 1,
        "internal": 1,
        "boundary": 2,
        "class": 1,
        "obstruction": 2,
    },
    "consistency_requires": {
        "source": 75,
        "internal": 39,
        "boundary": 75,
        "class": 36,
        "obstruction": 15,
    },
    "consistency_context_separation": {
        "source": 1,
        "internal": 0,
        "boundary": 0,
        "class": 0,
        "obstruction": 0,
    },
}

failures: list[str] = []


def accepted_nodes(data: dict[str, Any]) -> set[str]:
    current = data["current_requirements"]
    return set(current["atoms"]) | set(current["invariants"])


def section_entries(
    data: dict[str, Any], section: str
) -> list[tuple[str, str, Any]]:
    if section == "frontier":
        return [(section, key, value) for key, value in data["frontier"].items()]
    if section == "consistency_requires":
        return [
            (section, key, value)
            for key, value in data["consistency_rules"]["requires"].items()
        ]
    if section == "consistency_context_separation":
        return [
            (section, str(index), value)
            for index, value in enumerate(data["consistency_rules"]["context_separation"])
        ]
    raise ValueError(section)


def entry_blob(entry: tuple[str, str, Any]) -> str:
    section, key, value = entry
    return f"{section} {key} {value}"


def section_hits(data: dict[str, Any], section: str, label: str) -> list[tuple[str, str, Any]]:
    return [entry for entry in section_entries(data, section) if label in entry_blob(entry)]


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def main() -> None:
    data = load_map()
    accepted = accepted_nodes(data)
    sections = tuple(EXPECTED_SECTION_SIZES)
    section_sizes = {section: len(section_entries(data, section)) for section in sections}
    exact_hit_counts = {
        section: {
            label: len(section_hits(data, section, label))
            for label in EXACT_RESIDUAL_LABELS
        }
        for section in sections
    }
    broad_hit_counts = {
        section: {
            label: len(section_hits(data, section, label))
            for label in BROAD_RESIDUAL_TOKENS
        }
        for section in sections
    }
    generic_counts = {
        section: {
            token: len(section_hits(data, section, token)) for token in GENERIC_TOKENS
        }
        for section in sections
    }

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
        section_sizes == EXPECTED_SECTION_SIZES
        and data["frontier"]["current_doc"] == 610
        and data["frontier"]["current_delta"] == "doc610",
        f"section_sizes={section_sizes}",
    )
    gate(
        f"{PREFIX}4",
        all(
            not section_hits(data, section, label)
            for section in sections
            for label in EXACT_RESIDUAL_LABELS
        ),
        f"exact_hit_counts={exact_hit_counts}",
    )
    gate(
        f"{PREFIX}5",
        all(
            not section_hits(data, section, label)
            for section in sections
            for label in BROAD_RESIDUAL_TOKENS
        ),
        f"broad_hit_counts={broad_hit_counts}",
    )
    gate(
        f"{PREFIX}6",
        all(
            not section_hits(data, section, surface)
            for section in sections
            for surface in IMPOSSIBLE_RESIDUAL_SURFACES
        ),
        "exact residual surface strings do not occur as control-plane payload data",
    )
    gate(
        f"{PREFIX}7",
        generic_counts == EXPECTED_GENERIC_COUNTS,
        f"generic_counts={generic_counts}",
    )
    gate(
        f"{PREFIX}8",
        set(data["consistency_rules"]) == {
            "requires",
            "excludes_current",
            "context_separation",
        }
        and len(data["consistency_rules"]["excludes_current"][KILLCOMPEVENTSIGACTION]) == 36,
        "positive control-plane rules are separated from the already-killed rejected/excluded ledger",
    )

    if failures:
        raise SystemExit(1)

    print(f"\n{PREFIX}1-{PREFIX}8 ALL PASS: frontier control-plane morphism reuse fails")
    print(
        "VERDICT: frontier descriptors and positive consistency-rule payloads "
        "contain no residual labels or broad external/oracle/not/tail tokens. "
        "Their generic vocabulary is source-square control-plane bookkeeping, "
        "not residual-specific morphism evidence."
    )


if __name__ == "__main__":
    main()
