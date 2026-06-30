r"""Boundary-convolution module contract for the strict-square branch.

Doc 329 requires the signed zero fiber to map through a represented
boundary-cancellation functor to DD.4 boundary localization.  This witness
sharpens the next split: that boundary map must be a module functor for
strict-square character convolution.  A boundary map only defined on
2[1]-[2], or one recovered as a weighted-zero subspace, support quotient,
post-convolution quotient, external module presentation, finite multiplier
sample, or endpoint/control filter, does not construct the needed interface.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_boundary_convolution_module_contract
"""

from __future__ import annotations


failures: list[str] = []

REQUIRED_EDGES = {
    ("signed_zero_fiber", "cancellation_module_generator"),
    ("signed_character_algebra", "character_convolution_action"),
    ("character_convolution_action", "cancellation_module"),
    ("cancellation_module_generator", "cancellation_module"),
    ("cancellation_module", "boundary_convolution_module_functor"),
    ("boundary_convolution_module_functor", "dd4_boundary_localization"),
    ("boundary_convolution_module_functor", "stratum_product"),
    ("dd4_boundary_localization", "internal_effectivity_domain"),
    ("stratum_product", "internal_effectivity_domain"),
    ("internal_effectivity_domain", "endpoint"),
    ("dd4_boundary_localization", "pushforward"),
    ("endpoint", "pushforward"),
    ("pushforward", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
    ("internal_effectivity_domain", "control_death"),
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def normalize(chi: dict[int, int]) -> dict[int, int]:
    return {key: val for key, val in sorted(chi.items()) if val != 0}


def chi_col(a, b, edges) -> dict[int, int]:
    out: dict[int, int] = {}
    for j, bj in enumerate(b):
        aj = sum(a[i] for i, jj in edges if jj == j)
        if bj != 0 and aj != 0:
            out[aj] = out.get(aj, 0) + bj
    return normalize(out)


def convolve_chi(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for a, ca in left.items():
        for b, cb in right.items():
            out[a * b] = out.get(a * b, 0) + ca * cb
    return normalize(out)


def weighted_mass(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items())


def split_pair(chi: dict[int, int]) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    pos = tuple((key, val) for key, val in chi.items() if val > 0)
    neg = tuple((key, -val) for key, val in chi.items() if val < 0)
    return pos, neg


def support(chi: dict[int, int]) -> tuple[int, ...]:
    return tuple(sorted(chi))


def scaled(chi: dict[int, int], n: int) -> dict[int, int]:
    return normalize({key: n * val for key, val in chi.items()})


def action_family(generator: dict[int, int], multipliers: dict[str, dict[int, int]]):
    return {name: convolve_chi(generator, chi) for name, chi in multipliers.items()}


def source(**kwargs):
    data = {
        "carrier_native": False,
        "signed_character_algebra_actual": False,
        "signed_zero_generator_actual": False,
        "character_convolution_action_actual": False,
        "cancellation_module_actual": False,
        "boundary_convolution_module_functor_actual": False,
        "dd4_boundary_localization_actual": False,
        "preserves_multiplier_data": False,
        "preserves_coefficients": False,
        "preserves_signed_support": False,
        "module_action_total_on_character_subalgebra": False,
        "maps_zero_generator_to_boundary": False,
        "maps_all_convolution_translates_to_boundary": False,
        "maps_module_action_to_stratum_product": False,
        "generates_endpoint_integrality": False,
        "generates_pushforward_compatibility": False,
        "generates_graph_rosati_count": False,
        "generates_control_death": False,
        "controls_undefined_at_module": False,
        "dh_undefined_at_module": False,
        "epstein_undefined_at_module": False,
        "required_edges": set(),
        "zero_fiber_only_boundary": False,
        "weighted_zero_subspace": False,
        "positive_negative_split_only": False,
        "group_completion_only": False,
        "post_convolution_quotient": False,
        "absorbing_boundary_ideal": False,
        "support_only_module": False,
        "finite_multiplier_sample": False,
        "external_module_presentation": False,
        "endpoint_kernel_filter": False,
        "declared_module_functor": False,
        "control_formable": True,
        "dh_formable": True,
        "epstein_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("signed_character_algebra_actual", "signed_character_algebra_missing"),
    ("signed_zero_generator_actual", "signed_zero_generator_missing"),
    ("character_convolution_action_actual", "character_convolution_action_missing"),
    ("cancellation_module_actual", "cancellation_module_missing"),
    (
        "boundary_convolution_module_functor_actual",
        "boundary_convolution_module_functor_not_actual",
    ),
    ("dd4_boundary_localization_actual", "dd4_boundary_localization_not_actual"),
    ("preserves_multiplier_data", "multiplier_data_not_preserved"),
    ("preserves_coefficients", "coefficients_not_preserved"),
    ("preserves_signed_support", "signed_support_not_preserved"),
    (
        "module_action_total_on_character_subalgebra",
        "module_action_not_total_on_character_subalgebra",
    ),
    ("maps_zero_generator_to_boundary", "zero_generator_not_mapped_to_boundary"),
    (
        "maps_all_convolution_translates_to_boundary",
        "convolution_translates_not_mapped_to_boundary",
    ),
    (
        "maps_module_action_to_stratum_product",
        "module_action_not_mapped_to_stratum_product",
    ),
    ("generates_endpoint_integrality", "endpoint_integrality_not_generated"),
    (
        "generates_pushforward_compatibility",
        "pushforward_compatibility_not_generated",
    ),
    ("generates_graph_rosati_count", "graph_rosati_count_not_generated"),
    ("generates_control_death", "control_death_not_generated"),
    ("controls_undefined_at_module", "controls_not_undefined_at_module"),
    ("dh_undefined_at_module", "dh_not_undefined_at_module"),
    ("epstein_undefined_at_module", "epstein_not_undefined_at_module"),
)

BANNED = (
    ("zero_fiber_only_boundary", "zero_fiber_only_boundary"),
    ("weighted_zero_subspace", "weighted_zero_subspace"),
    ("positive_negative_split_only", "positive_negative_split_only"),
    ("group_completion_only", "group_completion_only"),
    ("post_convolution_quotient", "post_convolution_quotient"),
    ("absorbing_boundary_ideal", "absorbing_boundary_ideal"),
    ("support_only_module", "support_only_module"),
    ("finite_multiplier_sample", "finite_multiplier_sample"),
    ("external_module_presentation", "external_module_presentation"),
    ("endpoint_kernel_filter", "endpoint_kernel_filter"),
    ("declared_module_functor", "declared_module_functor"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_boundary_convolution_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_boundary_convolution_module(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        signed_character_algebra_actual=True,
        signed_zero_generator_actual=True,
        character_convolution_action_actual=True,
        cancellation_module_actual=True,
        boundary_convolution_module_functor_actual=True,
        dd4_boundary_localization_actual=True,
        preserves_multiplier_data=True,
        preserves_coefficients=True,
        preserves_signed_support=True,
        module_action_total_on_character_subalgebra=True,
        maps_zero_generator_to_boundary=True,
        maps_all_convolution_translates_to_boundary=True,
        maps_module_action_to_stratum_product=True,
        generates_endpoint_integrality=True,
        generates_pushforward_compatibility=True,
        generates_graph_rosati_count=True,
        generates_control_death=True,
        controls_undefined_at_module=True,
        dh_undefined_at_module=True,
        epstein_undefined_at_module=True,
        required_edges=set(REQUIRED_EDGES),
        control_formable=False,
        dh_formable=False,
        epstein_formable=False,
    )
    data.update(kwargs)
    return data


L = ((1, 1), (1, 1), ((0, 0), (0, 1), (1, 0)))
C3 = ((3,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
F41 = ((4,), (1,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

chi_zero = chi_col(*ZERO_SPLIT)
multipliers = {
    "one": {1: 1},
    "L": chi_col(*L),
    "C3": chi_col(*C3),
    "F22": chi_col(*F22),
    "F41": chi_col(*F41),
}
actions = action_family(chi_zero, multipliers)
fake_balanced = {1: 4, 4: -1}

gate(
    "BCM1 cancellation module has distinct convolution translates",
    chi_zero == {1: 2, 2: -1}
    and actions["one"] == {1: 2, 2: -1}
    and actions["L"] == {1: 2, 2: 1, 4: -1}
    and actions["C3"] == {3: 2, 6: -1}
    and actions["F22"] == {2: 4, 4: -2}
    and actions["F41"] == {4: 2, 8: -1}
    and all(weighted_mass(value) == 0 for value in actions.values())
    and len({tuple(value.items()) for value in actions.values()}) == len(actions),
    "actions=%s" % actions,
)


zero_only = live_source(
    cancellation_module_actual=False,
    boundary_convolution_module_functor_actual=False,
    preserves_multiplier_data=False,
    module_action_total_on_character_subalgebra=False,
    maps_all_convolution_translates_to_boundary=False,
    maps_module_action_to_stratum_product=False,
    zero_fiber_only_boundary=True,
    control_formable=True,
)

gate(
    "BCM2 zero-fiber-only boundary maps do not define the module action",
    actions["one"] != actions["F22"]
    and actions["one"] != actions["L"]
    and not accepts_boundary_convolution_module(zero_only)
    and {
        "cancellation_module_missing",
        "boundary_convolution_module_functor_not_actual",
        "multiplier_data_not_preserved",
        "module_action_not_total_on_character_subalgebra",
        "convolution_translates_not_mapped_to_boundary",
        "module_action_not_mapped_to_stratum_product",
        "zero_fiber_only_boundary",
        "control_formable",
    }
    <= set(reasons(zero_only)),
    ",".join(reasons(zero_only)),
)


weighted_zero = live_source(
    boundary_convolution_module_functor_actual=False,
    preserves_multiplier_data=False,
    preserves_coefficients=False,
    preserves_signed_support=False,
    maps_module_action_to_stratum_product=False,
    weighted_zero_subspace=True,
    endpoint_kernel_filter=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "BCM3 weighted-zero subspaces overaccept balanced non-square profiles",
    weighted_mass(fake_balanced) == 0
    and fake_balanced not in actions.values()
    and all(weighted_mass(value) == 0 for value in actions.values())
    and not accepts_boundary_convolution_module(weighted_zero)
    and {
        "boundary_convolution_module_functor_not_actual",
        "multiplier_data_not_preserved",
        "coefficients_not_preserved",
        "signed_support_not_preserved",
        "module_action_not_mapped_to_stratum_product",
        "weighted_zero_subspace",
        "endpoint_kernel_filter",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(weighted_zero)),
    "fake=%s reasons=%s" % (fake_balanced, ",".join(reasons(weighted_zero))),
)


split_only = live_source(
    boundary_convolution_module_functor_actual=False,
    maps_module_action_to_stratum_product=False,
    positive_negative_split_only=True,
    group_completion_only=True,
    control_formable=True,
)

gate(
    "BCM4 split/group-completion records pairs but not module functoriality",
    split_pair(actions["F22"]) == (((2, 4),), ((4, 2),))
    and split_pair(actions["F41"]) == (((4, 2),), ((8, 1),))
    and not accepts_boundary_convolution_module(split_only)
    and {
        "boundary_convolution_module_functor_not_actual",
        "module_action_not_mapped_to_stratum_product",
        "positive_negative_split_only",
        "group_completion_only",
        "control_formable",
    }
    <= set(reasons(split_only)),
    "F22=%s F41=%s reasons=%s"
    % (split_pair(actions["F22"]), split_pair(actions["F41"]), ",".join(reasons(split_only))),
)


support_only = live_source(
    boundary_convolution_module_functor_actual=False,
    preserves_coefficients=False,
    preserves_signed_support=False,
    support_only_module=True,
    control_formable=True,
)

gate(
    "BCM5 support-only modules lose coefficients and signs",
    support(actions["F22"]) == support(scaled({2: 1, 4: -1}, 1))
    and actions["F22"] != {2: 1, 4: -1}
    and not accepts_boundary_convolution_module(support_only)
    and {
        "boundary_convolution_module_functor_not_actual",
        "coefficients_not_preserved",
        "signed_support_not_preserved",
        "support_only_module",
        "control_formable",
    }
    <= set(reasons(support_only)),
    ",".join(reasons(support_only)),
)


absorbing_quotient = live_source(
    boundary_convolution_module_functor_actual=False,
    preserves_multiplier_data=False,
    preserves_coefficients=False,
    maps_all_convolution_translates_to_boundary=False,
    maps_module_action_to_stratum_product=False,
    post_convolution_quotient=True,
    absorbing_boundary_ideal=True,
    control_formable=True,
)

gate(
    "BCM6 post-convolution quotienting kills the module data too late",
    actions["F22"] != actions["F41"]
    and actions["L"] != actions["C3"]
    and not accepts_boundary_convolution_module(absorbing_quotient)
    and {
        "boundary_convolution_module_functor_not_actual",
        "multiplier_data_not_preserved",
        "coefficients_not_preserved",
        "convolution_translates_not_mapped_to_boundary",
        "module_action_not_mapped_to_stratum_product",
        "post_convolution_quotient",
        "absorbing_boundary_ideal",
        "control_formable",
    }
    <= set(reasons(absorbing_quotient)),
    ",".join(reasons(absorbing_quotient)),
)


finite_sample = live_source(
    module_action_total_on_character_subalgebra=False,
    maps_all_convolution_translates_to_boundary=False,
    finite_multiplier_sample=True,
)

gate(
    "BCM7 finite multiplier samples do not prove total module action",
    {"one", "F22"} < set(actions)
    and len({"L", "C3", "F41"} & set(actions)) == 3
    and not accepts_boundary_convolution_module(finite_sample)
    and {
        "module_action_not_total_on_character_subalgebra",
        "convolution_translates_not_mapped_to_boundary",
        "finite_multiplier_sample",
    }
    <= set(reasons(finite_sample)),
    ",".join(reasons(finite_sample)),
)


external_module = live_source(
    carrier_native=False,
    boundary_convolution_module_functor_actual=False,
    dd4_boundary_localization_actual=False,
    external_module_presentation=True,
    declared_module_functor=True,
    control_formable=True,
)

gate(
    "BCM8 external module presentations and declarations are rejected",
    len(actions) == 5
    and not accepts_boundary_convolution_module(external_module)
    and {
        "not_carrier_native",
        "boundary_convolution_module_functor_not_actual",
        "dd4_boundary_localization_not_actual",
        "external_module_presentation",
        "declared_module_functor",
        "control_formable",
    }
    <= set(reasons(external_module)),
    ",".join(reasons(external_module)),
)


control_filter = live_source(
    signed_character_algebra_actual=False,
    boundary_convolution_module_functor_actual=False,
    controls_undefined_at_module=False,
    dh_undefined_at_module=False,
    epstein_undefined_at_module=False,
    weighted_zero_subspace=True,
    endpoint_kernel_filter=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "BCM9 endpoint/control/DH/Epstein filters mimic balanced translates",
    all(weighted_mass(value) == 0 for value in actions.values())
    and weighted_mass(fake_balanced) == 0
    and not accepts_boundary_convolution_module(control_filter)
    and {
        "signed_character_algebra_missing",
        "boundary_convolution_module_functor_not_actual",
        "controls_not_undefined_at_module",
        "dh_not_undefined_at_module",
        "epstein_not_undefined_at_module",
        "weighted_zero_subspace",
        "endpoint_kernel_filter",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(control_filter)),
    ",".join(reasons(control_filter)),
)


missing_downstream = live_source(
    generates_pushforward_compatibility=False,
    generates_graph_rosati_count=False,
    generates_control_death=False,
    required_edges=REQUIRED_EDGES
    - {
        ("dd4_boundary_localization", "pushforward"),
        ("pushforward", "graph"),
        ("internal_effectivity_domain", "control_death"),
    },
)

live = live_source()
dead_sources = {
    "zero_only": zero_only,
    "weighted_zero": weighted_zero,
    "split_only": split_only,
    "support_only": support_only,
    "absorbing_quotient": absorbing_quotient,
    "finite_sample": finite_sample,
    "external_module": external_module,
    "control_filter": control_filter,
    "missing_downstream": missing_downstream,
}

gate(
    "BCM10 only represented boundary-convolution module functor passes",
    not accepts_boundary_convolution_module(missing_downstream)
    and {
        "pushforward_compatibility_not_generated",
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_boundary_convolution_edges_missing",
    }
    <= set(reasons(missing_downstream))
    and accepts_boundary_convolution_module(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(
        accepts_boundary_convolution_module(data) for data in dead_sources.values()
    ),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_boundary_convolution_module(data) for data in dead_sources.values()),
        accepts_boundary_convolution_module(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBCM1-BCM10 ALL PASS: boundary-convolution module contract pinned")
print(
    "VERDICT: the DD.4 boundary-cancellation interface must be a represented "
    "module functor for strict-square character convolution. Zero-fiber-only "
    "maps, weighted-zero subspaces, split/group-completion bookkeeping, "
    "support modules, post-convolution quotients, finite samples, external "
    "module presentations, declarations, and endpoint/control/DH/Epstein "
    "filters do not construct the needed boundary-convolution module."
)
