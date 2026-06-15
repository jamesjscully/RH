"""PFV2 gate calibration harness.

This is not a PFV2 construction and not evidence for RH. It is a small
executable calibration object for the current doc-196 target:

    PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-SENSITIVE

The point is to keep the prose gates honest. Each toy candidate below
models a broad class already discussed in the proof docs. The classifier must
reject the known false positives and leave only a deliberately minimal
"survivor" profile as a schema pass.

Run:

    python3 -m scripts.numerics.witness.pfv2_gate_calibration
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LEDGER = ROOT / "research/proof/target-ledger.json"
CALIBRATED_TARGET = "PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-SENSITIVE"


@dataclass(frozen=True)
class SourceRecord:
    """Toy structural record modeled on doc 166's S_{p,q}^G fields."""

    has_source_object: bool
    has_p_tower: bool
    has_q_tower: bool
    has_structural_complement: bool
    has_gpf_axiom: bool
    has_effectivity_data: bool
    has_gamma: bool
    has_residual_monodromy: bool
    has_native_commutator: bool
    has_filtered_action_residue: bool
    has_bank_iota: bool
    has_survival_data: bool


@dataclass(frozen=True)
class Candidate:
    name: str
    source: SourceRecord
    formed_before_assembly: bool
    recovered_from_allplaces_marking: bool
    residual_is_presentation_data: bool
    residual_is_scalar_bookkeeping: bool
    filtration_is_bookkeeping: bool
    filtration_changes_with_complement_structure: bool
    active_layers_created_by_pq_interaction: bool
    residue_varies_with_passive_shadow_fixed: bool
    commutator_extension_operator_named: bool
    extcomm_operator_native_to_gpf_source: bool
    effectivity_boundary_operator_named: bool
    effectivity_boundary_is_descent_coherence: bool
    fixed_readout_residual_fiber_named: bool
    residual_fiber_nontrivial: bool
    residual_pair_named_over_same_readout: bool
    residual_pair_identified_by_readout_data: bool
    internal_pair_separator_named: bool
    separator_is_external_or_rep_dependent: bool
    controls_can_instantiate_separator: bool
    residual_rho_g_named: bool
    kappa_consumes_rho_g: bool
    controls_can_instantiate_rho_g: bool
    banks_embedded_conservatively: bool
    downstream_consumes_rho_g: bool
    first_downstream_load_slot_named: bool
    downstream_load_sensitive_to_separator: bool
    downstream_route_forgets_separator: bool = False
    downstream_separator_consumed_by_trace_interface: bool = True
    downstream_trace_consumer_is_split_bank_operation: bool = False
    downstream_mixed_consumer_control_formable: bool = False
    downstream_selective_consumer_uses_free_trace_codomain: bool = False
    downstream_native_trace_value_sensitive_to_separator: bool = True


def missing_source_fields(source: SourceRecord) -> tuple[str, ...]:
    missing = []
    if not source.has_source_object:
        missing.append("S_{p,q}^G")
    if not source.has_p_tower:
        missing.append("p_tower")
    if not source.has_q_tower:
        missing.append("q_tower")
    if not source.has_structural_complement:
        missing.append("C_not_pq")
    if not source.has_gpf_axiom:
        missing.append("GPF_pq")
    if not source.has_effectivity_data:
        missing.append("Eff_pq")
    if not source.has_gamma:
        missing.append("gamma_G")
    if not source.has_residual_monodromy:
        missing.append("rho_G_mon")
    if not source.has_bank_iota:
        missing.append("bank_iota")
    if not source.has_survival_data:
        missing.append("surv_G")
    return tuple(missing)


def failed_gates(candidate: Candidate) -> tuple[str, ...]:
    """Return every PFV2-GPF-RMON-EFFSEP-DLOAD-MIXED-SELECTIVE-TRACE-SENSITIVE gate this toy record fails."""
    failures = []
    if missing_source_fields(candidate.source):
        failures.append("REJECT_INCOMPLETE_GPF_SOURCE")
    if candidate.source.has_residual_monodromy and not candidate.source.has_native_commutator:
        failures.append("REJECT_NO_RMON_COMMUTATOR")
    if candidate.source.has_native_commutator and not candidate.source.has_filtered_action_residue:
        failures.append("REJECT_NO_FILTERED_RESIDUE")
    if not candidate.formed_before_assembly:
        failures.append("REJECT_POSTGLOBAL")
    if candidate.recovered_from_allplaces_marking:
        failures.append("REJECT_GPF_EFFECTIVE_DESCENT")
    if candidate.residual_is_presentation_data:
        failures.append("REJECT_RMON_PRESENTATION")
    if candidate.residual_is_scalar_bookkeeping:
        failures.append("REJECT_COMM_SCALAR")
    if candidate.filtration_is_bookkeeping:
        failures.append("REJECT_FILT_BOOKKEEPING")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.filtration_changes_with_complement_structure
    ):
        failures.append("REJECT_FILT_STRUCT_INERT")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.active_layers_created_by_pq_interaction
    ):
        failures.append("REJECT_EXTDEPTH_NOT_ACTIVE")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.residue_varies_with_passive_shadow_fixed
    ):
        failures.append("REJECT_EXTDEPTH_PASSIVE_SHADOW")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.commutator_extension_operator_named
    ):
        failures.append("REJECT_NO_EXTCOMM_OPERATOR")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.extcomm_operator_native_to_gpf_source
    ):
        failures.append("REJECT_EXTCOMM_FORMAL_AMBIENT")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.effectivity_boundary_operator_named
    ):
        failures.append("REJECT_NO_EFFCOMM_BOUNDARY")
    if (
        candidate.source.has_filtered_action_residue
        and candidate.effectivity_boundary_is_descent_coherence
    ):
        failures.append("REJECT_EFFCOMM_DESCENT_COHERENCE")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.fixed_readout_residual_fiber_named
    ):
        failures.append("REJECT_NO_EFFCOMM_RESIDUAL_FIBER")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.residual_fiber_nontrivial
    ):
        failures.append("REJECT_EFFFIBER_TRIVIAL")
    if (
        candidate.source.has_filtered_action_residue
        and not candidate.residual_pair_named_over_same_readout
    ):
        failures.append("REJECT_NO_EFFPAIR")
    if (
        candidate.source.has_filtered_action_residue
        and candidate.residual_pair_named_over_same_readout
        and candidate.residual_pair_identified_by_readout_data
    ):
        failures.append("REJECT_EFFPAIR_IDENTIFIED")
    if (
        candidate.source.has_filtered_action_residue
        and candidate.residual_pair_named_over_same_readout
        and not candidate.residual_pair_identified_by_readout_data
        and not candidate.internal_pair_separator_named
    ):
        failures.append("REJECT_NO_EFFSEP_SEPARATOR")
    if (
        candidate.source.has_filtered_action_residue
        and candidate.residual_pair_named_over_same_readout
        and not candidate.residual_pair_identified_by_readout_data
        and candidate.internal_pair_separator_named
        and candidate.separator_is_external_or_rep_dependent
    ):
        failures.append("REJECT_EFFSEP_EXTERNAL")
    if (
        candidate.source.has_filtered_action_residue
        and candidate.residual_pair_named_over_same_readout
        and not candidate.residual_pair_identified_by_readout_data
        and candidate.internal_pair_separator_named
        and not candidate.separator_is_external_or_rep_dependent
        and candidate.controls_can_instantiate_separator
    ):
        failures.append("REJECT_EFFSEP_CONTROL_FORMABLE")
    if not candidate.residual_rho_g_named:
        failures.append("REJECT_NO_GPF_RESIDUAL")
    if not candidate.kappa_consumes_rho_g:
        failures.append("REJECT_GPF_INHERITED_MAP")
    if candidate.controls_can_instantiate_rho_g:
        failures.append("REJECT_CONTROL_FORMABLE")
    if not candidate.banks_embedded_conservatively:
        failures.append("REJECT_BANK_REPLACEMENT")
    if not candidate.downstream_consumes_rho_g:
        failures.append("REJECT_DOWNSTREAM_ERASURE")
    if candidate.downstream_consumes_rho_g and not candidate.first_downstream_load_slot_named:
        failures.append("REJECT_NO_EFFSEP_DLOAD_SLOT")
    if (
        candidate.downstream_consumes_rho_g
        and candidate.first_downstream_load_slot_named
        and not candidate.downstream_load_sensitive_to_separator
    ):
        failures.append("REJECT_DLOAD_INSENSITIVE")
    if (
        candidate.downstream_consumes_rho_g
        and candidate.first_downstream_load_slot_named
        and candidate.downstream_load_sensitive_to_separator
        and candidate.downstream_route_forgets_separator
    ):
        failures.append("REJECT_DLOAD_FORGETFUL_ROUTE")
    if (
        candidate.downstream_consumes_rho_g
        and candidate.first_downstream_load_slot_named
        and candidate.downstream_load_sensitive_to_separator
        and not candidate.downstream_route_forgets_separator
        and not candidate.downstream_separator_consumed_by_trace_interface
    ):
        failures.append("REJECT_DLOAD_SIDECAR_ROUTE")
    if (
        candidate.downstream_consumes_rho_g
        and candidate.first_downstream_load_slot_named
        and candidate.downstream_load_sensitive_to_separator
        and not candidate.downstream_route_forgets_separator
        and candidate.downstream_separator_consumed_by_trace_interface
        and candidate.downstream_trace_consumer_is_split_bank_operation
    ):
        failures.append("REJECT_DLOAD_SPLIT_CONSUMPTION")
    if (
        candidate.downstream_consumes_rho_g
        and candidate.first_downstream_load_slot_named
        and candidate.downstream_load_sensitive_to_separator
        and not candidate.downstream_route_forgets_separator
        and candidate.downstream_separator_consumed_by_trace_interface
        and not candidate.downstream_trace_consumer_is_split_bank_operation
        and candidate.downstream_mixed_consumer_control_formable
    ):
        failures.append("REJECT_DLOAD_MIXED_CONTROL_FORMABLE")
    if (
        candidate.downstream_consumes_rho_g
        and candidate.first_downstream_load_slot_named
        and candidate.downstream_load_sensitive_to_separator
        and not candidate.downstream_route_forgets_separator
        and candidate.downstream_separator_consumed_by_trace_interface
        and not candidate.downstream_trace_consumer_is_split_bank_operation
        and not candidate.downstream_mixed_consumer_control_formable
        and candidate.downstream_selective_consumer_uses_free_trace_codomain
    ):
        failures.append("REJECT_DLOAD_FREE_TRACE_CODOMAIN")
    if (
        candidate.downstream_consumes_rho_g
        and candidate.first_downstream_load_slot_named
        and candidate.downstream_load_sensitive_to_separator
        and not candidate.downstream_route_forgets_separator
        and candidate.downstream_separator_consumed_by_trace_interface
        and not candidate.downstream_trace_consumer_is_split_bank_operation
        and not candidate.downstream_mixed_consumer_control_formable
        and not candidate.downstream_selective_consumer_uses_free_trace_codomain
        and not candidate.downstream_native_trace_value_sensitive_to_separator
    ):
        failures.append("REJECT_DLOAD_NATIVE_TRACE_INSENSITIVE")
    return tuple(failures)


def classify(candidate: Candidate) -> str:
    """Collapse the multi-gate audit to a display verdict."""
    failures = failed_gates(candidate)
    if failures:
        return ",".join(failures)
    return "SCHEMA_SURVIVOR"


COMPLETE_SOURCE = SourceRecord(
    has_source_object=True,
    has_p_tower=True,
    has_q_tower=True,
    has_structural_complement=True,
    has_gpf_axiom=True,
    has_effectivity_data=True,
    has_gamma=True,
    has_residual_monodromy=True,
    has_native_commutator=True,
    has_filtered_action_residue=True,
    has_bank_iota=True,
    has_survival_data=True,
)

PRESENTATION_SOURCE = SourceRecord(
    has_source_object=True,
    has_p_tower=True,
    has_q_tower=True,
    has_structural_complement=True,
    has_gpf_axiom=True,
    has_effectivity_data=True,
    has_gamma=True,
    has_residual_monodromy=False,
    has_native_commutator=False,
    has_filtered_action_residue=False,
    has_bank_iota=True,
    has_survival_data=False,
)

GPF_SOURCE_WITHOUT_RMON = SourceRecord(
    has_source_object=True,
    has_p_tower=True,
    has_q_tower=True,
    has_structural_complement=True,
    has_gpf_axiom=True,
    has_effectivity_data=True,
    has_gamma=True,
    has_residual_monodromy=False,
    has_native_commutator=False,
    has_filtered_action_residue=False,
    has_bank_iota=True,
    has_survival_data=True,
)

NATIVE_RMON_WITHOUT_COMM = SourceRecord(
    has_source_object=True,
    has_p_tower=True,
    has_q_tower=True,
    has_structural_complement=True,
    has_gpf_axiom=True,
    has_effectivity_data=True,
    has_gamma=True,
    has_residual_monodromy=True,
    has_native_commutator=False,
    has_filtered_action_residue=False,
    has_bank_iota=True,
    has_survival_data=True,
)

NATIVE_COMM_WITHOUT_FILTER = SourceRecord(
    has_source_object=True,
    has_p_tower=True,
    has_q_tower=True,
    has_structural_complement=True,
    has_gpf_axiom=True,
    has_effectivity_data=True,
    has_gamma=True,
    has_residual_monodromy=True,
    has_native_commutator=True,
    has_filtered_action_residue=False,
    has_bank_iota=True,
    has_survival_data=True,
)


CASES = [
    (
        Candidate(
            name="allplaces_readout",
            source=PRESENTATION_SOURCE,
            formed_before_assembly=False,
            recovered_from_allplaces_marking=True,
            residual_is_presentation_data=True,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=False,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=False,
            downstream_consumes_rho_g=False,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_INCOMPLETE_GPF_SOURCE",
            "REJECT_POSTGLOBAL",
            "REJECT_GPF_EFFECTIVE_DESCENT",
            "REJECT_RMON_PRESENTATION",
            "REJECT_NO_GPF_RESIDUAL",
            "REJECT_GPF_INHERITED_MAP",
            "REJECT_BANK_REPLACEMENT",
            "REJECT_DOWNSTREAM_ERASURE",
        ),
    ),
    (
        Candidate(
            name="effective_descent_equiv",
            source=PRESENTATION_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=True,
            residual_is_presentation_data=True,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=False,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=False,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_INCOMPLETE_GPF_SOURCE",
            "REJECT_GPF_EFFECTIVE_DESCENT",
            "REJECT_RMON_PRESENTATION",
            "REJECT_NO_GPF_RESIDUAL",
            "REJECT_GPF_INHERITED_MAP",
            "REJECT_DOWNSTREAM_ERASURE",
        ),
    ),
    (
        Candidate(
            name="presentation_only_local_source",
            source=PRESENTATION_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=True,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=False,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=False,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_INCOMPLETE_GPF_SOURCE",
            "REJECT_RMON_PRESENTATION",
            "REJECT_NO_GPF_RESIDUAL",
            "REJECT_GPF_INHERITED_MAP",
            "REJECT_DOWNSTREAM_ERASURE",
        ),
    ),
    (
        Candidate(
            name="residual_but_control_formable",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=True,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_CONTROL_FORMABLE",),
    ),
    (
        Candidate(
            name="gpf_local_without_rmon",
            source=GPF_SOURCE_WITHOUT_RMON,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=False,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_INCOMPLETE_GPF_SOURCE",
            "REJECT_NO_GPF_RESIDUAL",
            "REJECT_GPF_INHERITED_MAP",
        ),
    ),
    (
        Candidate(
            name="rmon_but_presentation_gauge",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=True,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=False,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_RMON_PRESENTATION",
            "REJECT_GPF_INHERITED_MAP",
            "REJECT_DOWNSTREAM_ERASURE",
        ),
    ),
    (
        Candidate(
            name="native_rmon_without_commutator",
            source=NATIVE_RMON_WITHOUT_COMM,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_NO_RMON_COMMUTATOR",),
    ),
    (
        Candidate(
            name="commutator_but_scalar_bookkeeping",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=True,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=False,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_COMM_SCALAR",
            "REJECT_GPF_INHERITED_MAP",
            "REJECT_DOWNSTREAM_ERASURE",
        ),
    ),
    (
        Candidate(
            name="nonscalar_without_filtered_residue",
            source=NATIVE_COMM_WITHOUT_FILTER,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_NO_FILTERED_RESIDUE",),
    ),
    (
        Candidate(
            name="filtered_but_bookkeeping",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=True,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=False,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_FILT_BOOKKEEPING",
            "REJECT_FILT_STRUCT_INERT",
            "REJECT_EXTDEPTH_NOT_ACTIVE",
            "REJECT_EXTDEPTH_PASSIVE_SHADOW",
            "REJECT_NO_EXTCOMM_OPERATOR",
            "REJECT_EXTCOMM_FORMAL_AMBIENT",
            "REJECT_NO_EFFCOMM_BOUNDARY",
            "REJECT_NO_EFFCOMM_RESIDUAL_FIBER",
            "REJECT_EFFFIBER_TRIVIAL",
            "REJECT_NO_EFFPAIR",
            "REJECT_GPF_INHERITED_MAP",
            "REJECT_DOWNSTREAM_ERASURE",
        ),
    ),
    (
        Candidate(
            name="filtered_but_structurally_inert",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=False,
            active_layers_created_by_pq_interaction=False,
            residue_varies_with_passive_shadow_fixed=False,
            commutator_extension_operator_named=False,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_FILT_STRUCT_INERT",
            "REJECT_EXTDEPTH_NOT_ACTIVE",
            "REJECT_EXTDEPTH_PASSIVE_SHADOW",
            "REJECT_NO_EXTCOMM_OPERATOR",
            "REJECT_EXTCOMM_FORMAL_AMBIENT",
            "REJECT_NO_EFFCOMM_BOUNDARY",
            "REJECT_NO_EFFCOMM_RESIDUAL_FIBER",
            "REJECT_EFFFIBER_TRIVIAL",
            "REJECT_NO_EFFPAIR",
        ),
    ),
    (
        Candidate(
            name="extcomm_but_formal_ambient",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=False,
            effectivity_boundary_operator_named=False,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_EXTCOMM_FORMAL_AMBIENT",
            "REJECT_NO_EFFCOMM_BOUNDARY",
            "REJECT_NO_EFFCOMM_RESIDUAL_FIBER",
            "REJECT_EFFFIBER_TRIVIAL",
            "REJECT_NO_EFFPAIR",
        ),
    ),
    (
        Candidate(
            name="effcomm_but_descent_coherence",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=True,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_EFFCOMM_DESCENT_COHERENCE",
            "REJECT_NO_EFFCOMM_RESIDUAL_FIBER",
            "REJECT_EFFFIBER_TRIVIAL",
            "REJECT_NO_EFFPAIR",
        ),
    ),
    (
        Candidate(
            name="effcomm_without_residual_fiber",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=False,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_NO_EFFCOMM_RESIDUAL_FIBER",
            "REJECT_EFFFIBER_TRIVIAL",
            "REJECT_NO_EFFPAIR",
        ),
    ),
    (
        Candidate(
            name="efffiber_but_trivial",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=False,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (
            "REJECT_EFFFIBER_TRIVIAL",
            "REJECT_NO_EFFPAIR",
        ),
    ),
    (
        Candidate(
            name="efffiber_nontrivial_but_no_pair",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=False,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_NO_EFFPAIR",),
    ),
    (
        Candidate(
            name="effpair_but_identified",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=True,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_EFFPAIR_IDENTIFIED",),
    ),
    (
        Candidate(
            name="effpair_separated_but_no_separator",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=False,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_NO_EFFSEP_SEPARATOR",),
    ),
    (
        Candidate(
            name="effsep_but_external_diagnostic",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=True,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_EFFSEP_EXTERNAL",),
    ),
    (
        Candidate(
            name="effsep_internal_but_control_formable",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=True,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_EFFSEP_CONTROL_FORMABLE",),
    ),
    (
        Candidate(
            name="effsep_control_excluded_but_bank_replacing",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=False,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_BANK_REPLACEMENT",),
    ),
    (
        Candidate(
            name="effsep_banked_but_downstream_erased",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=False,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_DOWNSTREAM_ERASURE",),
    ),
    (
        Candidate(
            name="effsep_loadbearing_but_no_dload_slot",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=False,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_NO_EFFSEP_DLOAD_SLOT",),
    ),
    (
        Candidate(
            name="effsep_dload_but_separator_insensitive",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=False,
        ),
        ("REJECT_DLOAD_INSENSITIVE",),
    ),
    (
        Candidate(
            name="effsep_dload_sensitive_but_forgetful_route",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
            downstream_route_forgets_separator=True,
        ),
        ("REJECT_DLOAD_FORGETFUL_ROUTE",),
    ),
    (
        Candidate(
            name="effsep_dload_nonforgetful_but_sidecar_route",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
            downstream_route_forgets_separator=False,
            downstream_separator_consumed_by_trace_interface=False,
        ),
        ("REJECT_DLOAD_SIDECAR_ROUTE",),
    ),
    (
        Candidate(
            name="effsep_dload_consumed_but_split_bank",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
            downstream_route_forgets_separator=False,
            downstream_separator_consumed_by_trace_interface=True,
            downstream_trace_consumer_is_split_bank_operation=True,
        ),
        ("REJECT_DLOAD_SPLIT_CONSUMPTION",),
    ),
    (
        Candidate(
            name="effsep_dload_mixed_but_control_formable",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
            downstream_route_forgets_separator=False,
            downstream_separator_consumed_by_trace_interface=True,
            downstream_trace_consumer_is_split_bank_operation=False,
            downstream_mixed_consumer_control_formable=True,
        ),
        ("REJECT_DLOAD_MIXED_CONTROL_FORMABLE",),
    ),
    (
        Candidate(
            name="effsep_dload_selective_but_free_trace_codomain",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
            downstream_route_forgets_separator=False,
            downstream_separator_consumed_by_trace_interface=True,
            downstream_trace_consumer_is_split_bank_operation=False,
            downstream_mixed_consumer_control_formable=False,
            downstream_selective_consumer_uses_free_trace_codomain=True,
        ),
        ("REJECT_DLOAD_FREE_TRACE_CODOMAIN",),
    ),
    (
        Candidate(
            name="effsep_dload_trace_native_but_value_insensitive",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
            downstream_route_forgets_separator=False,
            downstream_separator_consumed_by_trace_interface=True,
            downstream_trace_consumer_is_split_bank_operation=False,
            downstream_mixed_consumer_control_formable=False,
            downstream_selective_consumer_uses_free_trace_codomain=False,
            downstream_native_trace_value_sensitive_to_separator=False,
        ),
        ("REJECT_DLOAD_NATIVE_TRACE_INSENSITIVE",),
    ),
    (
        Candidate(
            name="borderline_missing_kappa_use",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=False,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        ("REJECT_GPF_INHERITED_MAP",),
    ),
    (
        Candidate(
            name="borderline_kappa_use_restored",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (),
    ),
    (
        Candidate(
            name="minimal_schema_survivor",
            source=COMPLETE_SOURCE,
            formed_before_assembly=True,
            recovered_from_allplaces_marking=False,
            residual_is_presentation_data=False,
            residual_is_scalar_bookkeeping=False,
            filtration_is_bookkeeping=False,
            filtration_changes_with_complement_structure=True,
            active_layers_created_by_pq_interaction=True,
            residue_varies_with_passive_shadow_fixed=True,
            commutator_extension_operator_named=True,
            extcomm_operator_native_to_gpf_source=True,
            effectivity_boundary_operator_named=True,
            effectivity_boundary_is_descent_coherence=False,
            fixed_readout_residual_fiber_named=True,
            residual_fiber_nontrivial=True,
            residual_pair_named_over_same_readout=True,
            residual_pair_identified_by_readout_data=False,
            internal_pair_separator_named=True,
            separator_is_external_or_rep_dependent=False,
            controls_can_instantiate_separator=False,
            residual_rho_g_named=True,
            kappa_consumes_rho_g=True,
            controls_can_instantiate_rho_g=False,
            banks_embedded_conservatively=True,
            downstream_consumes_rho_g=True,
            first_downstream_load_slot_named=True,
            downstream_load_sensitive_to_separator=True,
        ),
        (),
    ),
]


def ledger_current_target() -> str:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    return ledger["current_target"]


def validate_calibrated_target() -> None:
    current_target = ledger_current_target()
    if current_target != CALIBRATED_TARGET:
        raise AssertionError(
            "PFV2 gate calibration is stale: "
            f"calibrated for {CALIBRATED_TARGET}, ledger current target is "
            f"{current_target}"
        )


def summary() -> list[tuple[str, str]]:
    validate_calibrated_target()
    rows = []
    for candidate, expected in CASES:
        failures = failed_gates(candidate)
        if failures != expected:
            raise AssertionError(
                f"{candidate.name}: expected {expected}, got {failures}"
            )
        verdict = classify(candidate)
        rows.append((candidate.name, verdict))
    return rows


def _report() -> None:
    print(f"PFV2 gate calibration (doc 196 target: {CALIBRATED_TARGET})")
    print("=" * 72)
    for name, verdict in summary():
        print(f"{name:32s} {verdict}")
    print("=" * 72)
    print("pfv2-gate-calibration: OK")


if __name__ == "__main__":
    _report()
