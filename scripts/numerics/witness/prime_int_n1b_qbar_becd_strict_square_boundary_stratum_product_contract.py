r"""Boundary-stratum product contract for the strict-square branch.

Doc 330 requires a represented boundary-convolution module functor from the
cancellation module to DD.4 boundary localization and Qbar_BECD stratum
product.  This witness sharpens the product side: the module action must land
in a represented stratum product.  Raw character convolution, weighted-mass
collapse, support products, split-pair bookkeeping, absorbing boundary
quotients, local product moduli, finite product tables, endpoint filters, and
declared products do not construct that product.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_boundary_stratum_product_contract
"""

from __future__ import annotations


failures: list[str] = []

REQUIRED_EDGES = {
    ("cancellation_module", "boundary_stratum_product"),
    ("character_convolution_action", "boundary_stratum_product"),
    ("boundary_convolution_module_functor", "boundary_stratum_product"),
    ("boundary_stratum_product", "dd4_boundary_localization"),
    ("boundary_stratum_product", "internal_effectivity_domain"),
    ("dd4_boundary_localization", "internal_effectivity_domain"),
    ("internal_effectivity_domain", "endpoint"),
    ("boundary_stratum_product", "endpoint"),
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


def support(chi: dict[int, int]) -> tuple[int, ...]:
    return tuple(sorted(chi))


def split_pair(chi: dict[int, int]) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    pos = tuple((key, val) for key, val in chi.items() if val > 0)
    neg = tuple((key, -val) for key, val in chi.items() if val < 0)
    return pos, neg


def stratum_record(boundary: dict[int, int], multiplier_name: str, multiplier: dict[int, int]):
    product = convolve_chi(boundary, multiplier)
    return {
        "boundary": tuple(boundary.items()),
        "multiplier_name": multiplier_name,
        "multiplier": tuple(multiplier.items()),
        "product": tuple(product.items()),
        "mass": weighted_mass(product),
        "support": support(product),
    }


def source(**kwargs):
    data = {
        "carrier_native": False,
        "cancellation_module_actual": False,
        "character_convolution_action_actual": False,
        "boundary_convolution_module_functor_actual": False,
        "boundary_stratum_product_actual": False,
        "dd4_boundary_localization_actual": False,
        "internal_effectivity_domain_actual": False,
        "product_preserves_boundary_translate": False,
        "product_preserves_multiplier_data": False,
        "product_preserves_coefficients": False,
        "product_preserves_signed_support": False,
        "product_associative_with_character_convolution": False,
        "product_maps_to_dd4_localization": False,
        "product_maps_to_internal_effectivity_domain": False,
        "product_generates_endpoint_integrality": False,
        "product_generates_pushforward_compatibility": False,
        "product_generates_graph_rosati_count": False,
        "product_generates_control_death": False,
        "controls_undefined_at_product": False,
        "dh_undefined_at_product": False,
        "epstein_undefined_at_product": False,
        "required_edges": set(),
        "raw_character_convolution_product": False,
        "weighted_mass_product": False,
        "support_only_product": False,
        "split_pair_product": False,
        "group_completion_product": False,
        "absorbing_boundary_ideal": False,
        "post_product_quotient": False,
        "local_strata_product_moduli": False,
        "finite_product_table": False,
        "endpoint_degree_product_filter": False,
        "declared_stratum_product": False,
        "control_formable": True,
        "dh_formable": True,
        "epstein_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("cancellation_module_actual", "cancellation_module_missing"),
    ("character_convolution_action_actual", "character_convolution_action_missing"),
    (
        "boundary_convolution_module_functor_actual",
        "boundary_convolution_module_functor_not_actual",
    ),
    ("boundary_stratum_product_actual", "boundary_stratum_product_not_actual"),
    ("dd4_boundary_localization_actual", "dd4_boundary_localization_not_actual"),
    ("internal_effectivity_domain_actual", "internal_effectivity_domain_not_actual"),
    ("product_preserves_boundary_translate", "boundary_translate_not_preserved"),
    ("product_preserves_multiplier_data", "multiplier_data_not_preserved"),
    ("product_preserves_coefficients", "coefficients_not_preserved"),
    ("product_preserves_signed_support", "signed_support_not_preserved"),
    (
        "product_associative_with_character_convolution",
        "product_not_associative_with_character_convolution",
    ),
    ("product_maps_to_dd4_localization", "product_not_mapped_to_dd4_localization"),
    (
        "product_maps_to_internal_effectivity_domain",
        "product_not_mapped_to_internal_effectivity_domain",
    ),
    ("product_generates_endpoint_integrality", "endpoint_integrality_not_generated"),
    (
        "product_generates_pushforward_compatibility",
        "pushforward_compatibility_not_generated",
    ),
    ("product_generates_graph_rosati_count", "graph_rosati_count_not_generated"),
    ("product_generates_control_death", "control_death_not_generated"),
    ("controls_undefined_at_product", "controls_not_undefined_at_product"),
    ("dh_undefined_at_product", "dh_not_undefined_at_product"),
    ("epstein_undefined_at_product", "epstein_not_undefined_at_product"),
)

BANNED = (
    ("raw_character_convolution_product", "raw_character_convolution_product"),
    ("weighted_mass_product", "weighted_mass_product"),
    ("support_only_product", "support_only_product"),
    ("split_pair_product", "split_pair_product"),
    ("group_completion_product", "group_completion_product"),
    ("absorbing_boundary_ideal", "absorbing_boundary_ideal"),
    ("post_product_quotient", "post_product_quotient"),
    ("local_strata_product_moduli", "local_strata_product_moduli"),
    ("finite_product_table", "finite_product_table"),
    ("endpoint_degree_product_filter", "endpoint_degree_product_filter"),
    ("declared_stratum_product", "declared_stratum_product"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_boundary_stratum_product_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_boundary_stratum_product(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        cancellation_module_actual=True,
        character_convolution_action_actual=True,
        boundary_convolution_module_functor_actual=True,
        boundary_stratum_product_actual=True,
        dd4_boundary_localization_actual=True,
        internal_effectivity_domain_actual=True,
        product_preserves_boundary_translate=True,
        product_preserves_multiplier_data=True,
        product_preserves_coefficients=True,
        product_preserves_signed_support=True,
        product_associative_with_character_convolution=True,
        product_maps_to_dd4_localization=True,
        product_maps_to_internal_effectivity_domain=True,
        product_generates_endpoint_integrality=True,
        product_generates_pushforward_compatibility=True,
        product_generates_graph_rosati_count=True,
        product_generates_control_death=True,
        controls_undefined_at_product=True,
        dh_undefined_at_product=True,
        epstein_undefined_at_product=True,
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

z = chi_col(*ZERO_SPLIT)
chi_L = chi_col(*L)
chi_C3 = chi_col(*C3)
chi_F22 = chi_col(*F22)
chi_F41 = chi_col(*F41)
chi_LF22 = convolve_chi(chi_L, chi_F22)

actions = {
    "z": z,
    "zL": convolve_chi(z, chi_L),
    "zC3": convolve_chi(z, chi_C3),
    "zF22": convolve_chi(z, chi_F22),
    "zF41": convolve_chi(z, chi_F41),
}

assoc_left = convolve_chi(actions["zL"], chi_F22)
assoc_right = convolve_chi(z, chi_LF22)
fake_same_support = {2: 1, 4: -1}
fake_balanced = {1: 4, 4: -1}

gate(
    "BSP1 boundary product data keeps associative convolution translates",
    actions["z"] == {1: 2, 2: -1}
    and actions["zL"] == {1: 2, 2: 1, 4: -1}
    and actions["zC3"] == {3: 2, 6: -1}
    and actions["zF22"] == {2: 4, 4: -2}
    and actions["zF41"] == {4: 2, 8: -1}
    and assoc_left == assoc_right == {2: 4, 4: 2, 8: -2}
    and all(weighted_mass(value) == 0 for value in actions.values())
    and stratum_record(actions["zL"], "F22", chi_F22)["product"] == tuple(assoc_left.items()),
    "actions=%s assoc=%s" % (actions, assoc_left),
)


raw_convolution = live_source(
    boundary_stratum_product_actual=False,
    dd4_boundary_localization_actual=False,
    internal_effectivity_domain_actual=False,
    product_maps_to_dd4_localization=False,
    product_maps_to_internal_effectivity_domain=False,
    product_generates_endpoint_integrality=False,
    raw_character_convolution_product=True,
    control_formable=True,
)

gate(
    "BSP2 raw character convolution is not the represented stratum product",
    assoc_left == assoc_right
    and not accepts_boundary_stratum_product(raw_convolution)
    and {
        "boundary_stratum_product_not_actual",
        "dd4_boundary_localization_not_actual",
        "internal_effectivity_domain_not_actual",
        "product_not_mapped_to_dd4_localization",
        "product_not_mapped_to_internal_effectivity_domain",
        "endpoint_integrality_not_generated",
        "raw_character_convolution_product",
        "control_formable",
    }
    <= set(reasons(raw_convolution)),
    ",".join(reasons(raw_convolution)),
)


weighted_product = live_source(
    boundary_stratum_product_actual=False,
    product_preserves_boundary_translate=False,
    product_preserves_multiplier_data=False,
    product_preserves_coefficients=False,
    product_preserves_signed_support=False,
    product_maps_to_dd4_localization=False,
    weighted_mass_product=True,
    endpoint_degree_product_filter=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "BSP3 weighted-mass products collapse all balanced translates",
    weighted_mass(fake_balanced) == 0
    and fake_balanced not in actions.values()
    and len({weighted_mass(value) for value in actions.values()}) == 1
    and not accepts_boundary_stratum_product(weighted_product)
    and {
        "boundary_stratum_product_not_actual",
        "boundary_translate_not_preserved",
        "multiplier_data_not_preserved",
        "coefficients_not_preserved",
        "signed_support_not_preserved",
        "product_not_mapped_to_dd4_localization",
        "weighted_mass_product",
        "endpoint_degree_product_filter",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(weighted_product)),
    "fake=%s reasons=%s" % (fake_balanced, ",".join(reasons(weighted_product))),
)


support_product = live_source(
    boundary_stratum_product_actual=False,
    product_preserves_coefficients=False,
    product_preserves_signed_support=False,
    support_only_product=True,
    control_formable=True,
)

gate(
    "BSP4 support-only products lose coefficient and sign data",
    support(actions["zF22"]) == support(fake_same_support)
    and actions["zF22"] != fake_same_support
    and not accepts_boundary_stratum_product(support_product)
    and {
        "boundary_stratum_product_not_actual",
        "coefficients_not_preserved",
        "signed_support_not_preserved",
        "support_only_product",
        "control_formable",
    }
    <= set(reasons(support_product)),
    ",".join(reasons(support_product)),
)


split_product = live_source(
    boundary_stratum_product_actual=False,
    product_associative_with_character_convolution=False,
    product_maps_to_dd4_localization=False,
    product_maps_to_internal_effectivity_domain=False,
    split_pair_product=True,
    group_completion_product=True,
    control_formable=True,
)

gate(
    "BSP5 split/group products record pairs but not represented product",
    split_pair(actions["zF22"]) == (((2, 4),), ((4, 2),))
    and split_pair(actions["zF41"]) == (((4, 2),), ((8, 1),))
    and not accepts_boundary_stratum_product(split_product)
    and {
        "boundary_stratum_product_not_actual",
        "product_not_associative_with_character_convolution",
        "product_not_mapped_to_dd4_localization",
        "product_not_mapped_to_internal_effectivity_domain",
        "split_pair_product",
        "group_completion_product",
        "control_formable",
    }
    <= set(reasons(split_product)),
    ",".join(reasons(split_product)),
)


absorbing_quotient = live_source(
    boundary_stratum_product_actual=False,
    product_preserves_boundary_translate=False,
    product_preserves_multiplier_data=False,
    product_preserves_coefficients=False,
    product_preserves_signed_support=False,
    product_maps_to_internal_effectivity_domain=False,
    absorbing_boundary_ideal=True,
    post_product_quotient=True,
    control_formable=True,
)

gate(
    "BSP6 absorbing boundary quotients erase the product before strata",
    actions["zF22"] != actions["zF41"]
    and assoc_left != actions["zF22"]
    and not accepts_boundary_stratum_product(absorbing_quotient)
    and {
        "boundary_stratum_product_not_actual",
        "boundary_translate_not_preserved",
        "multiplier_data_not_preserved",
        "coefficients_not_preserved",
        "signed_support_not_preserved",
        "product_not_mapped_to_internal_effectivity_domain",
        "absorbing_boundary_ideal",
        "post_product_quotient",
        "control_formable",
    }
    <= set(reasons(absorbing_quotient)),
    ",".join(reasons(absorbing_quotient)),
)


local_moduli = live_source(
    carrier_native=False,
    boundary_stratum_product_actual=False,
    internal_effectivity_domain_actual=False,
    product_preserves_boundary_translate=False,
    product_maps_to_internal_effectivity_domain=False,
    product_generates_control_death=False,
    local_strata_product_moduli=True,
    control_formable=True,
)

gate(
    "BSP7 products of local stratum moduli are not one carrier product",
    set(stratum_record(actions["zL"], "F22", chi_F22)) == {
        "boundary",
        "multiplier_name",
        "multiplier",
        "product",
        "mass",
        "support",
    }
    and not accepts_boundary_stratum_product(local_moduli)
    and {
        "not_carrier_native",
        "boundary_stratum_product_not_actual",
        "internal_effectivity_domain_not_actual",
        "boundary_translate_not_preserved",
        "product_not_mapped_to_internal_effectivity_domain",
        "control_death_not_generated",
        "local_strata_product_moduli",
        "control_formable",
    }
    <= set(reasons(local_moduli)),
    ",".join(reasons(local_moduli)),
)


finite_table = live_source(
    product_associative_with_character_convolution=False,
    product_generates_pushforward_compatibility=False,
    finite_product_table=True,
)

gate(
    "BSP8 finite product tables do not prove the represented product law",
    {"z", "zF22"} < set(actions)
    and {"zL", "zC3", "zF41"} <= set(actions)
    and not accepts_boundary_stratum_product(finite_table)
    and {
        "product_not_associative_with_character_convolution",
        "pushforward_compatibility_not_generated",
        "finite_product_table",
    }
    <= set(reasons(finite_table)),
    ",".join(reasons(finite_table)),
)


endpoint_filter = live_source(
    cancellation_module_actual=False,
    boundary_stratum_product_actual=False,
    controls_undefined_at_product=False,
    dh_undefined_at_product=False,
    epstein_undefined_at_product=False,
    endpoint_degree_product_filter=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "BSP9 endpoint/control/DH/Epstein product filters remain formable",
    all(weighted_mass(value) == 0 for value in actions.values())
    and not accepts_boundary_stratum_product(endpoint_filter)
    and {
        "cancellation_module_missing",
        "boundary_stratum_product_not_actual",
        "controls_not_undefined_at_product",
        "dh_not_undefined_at_product",
        "epstein_not_undefined_at_product",
        "endpoint_degree_product_filter",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(endpoint_filter)),
    ",".join(reasons(endpoint_filter)),
)


declared = live_source(
    boundary_stratum_product_actual=False,
    dd4_boundary_localization_actual=False,
    required_edges=set(),
    declared_stratum_product=True,
)

missing_downstream = live_source(
    product_generates_endpoint_integrality=False,
    product_generates_pushforward_compatibility=False,
    product_generates_graph_rosati_count=False,
    product_generates_control_death=False,
    required_edges=REQUIRED_EDGES
    - {
        ("internal_effectivity_domain", "endpoint"),
        ("endpoint", "pushforward"),
        ("pushforward", "graph"),
        ("internal_effectivity_domain", "control_death"),
    },
)

live = live_source()
dead_sources = {
    "raw_convolution": raw_convolution,
    "weighted_product": weighted_product,
    "support_product": support_product,
    "split_product": split_product,
    "absorbing_quotient": absorbing_quotient,
    "local_moduli": local_moduli,
    "finite_table": finite_table,
    "endpoint_filter": endpoint_filter,
    "declared": declared,
    "missing_downstream": missing_downstream,
}

gate(
    "BSP10 only represented boundary-stratum product passes",
    not accepts_boundary_stratum_product(declared)
    and {
        "boundary_stratum_product_not_actual",
        "dd4_boundary_localization_not_actual",
        "required_boundary_stratum_product_edges_missing",
        "declared_stratum_product",
    }
    <= set(reasons(declared))
    and not accepts_boundary_stratum_product(missing_downstream)
    and {
        "endpoint_integrality_not_generated",
        "pushforward_compatibility_not_generated",
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_boundary_stratum_product_edges_missing",
    }
    <= set(reasons(missing_downstream))
    and accepts_boundary_stratum_product(live)
    and not any(accepts_boundary_stratum_product(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_boundary_stratum_product(data) for data in dead_sources.values()),
        accepts_boundary_stratum_product(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nBSP1-BSP10 ALL PASS: boundary-stratum product contract pinned")
print(
    "VERDICT: the boundary-convolution module must land in a represented "
    "Qbar_BECD stratum product. Raw convolution, weighted-mass products, "
    "support products, split/group products, absorbing quotients, local "
    "product moduli, finite tables, endpoint filters, and declared products "
    "do not construct the product that feeds DD.4 localization, internal "
    "effectivity, endpoint/pushforward, graph/Rosati/count, and control death."
)
