r"""Mixed-support subtower contract for the strict-square product image.

Doc 332 pins the product-to-internal-effectivity image edge.  This witness
sharpens the next bottleneck: the same internal image must carry the mixed
support appearing in z*C3 = 2[3]-[6].  Projecting to the visible 2-power
tower, externally factoring 6, declaring 3 and 6 boundary-null, or filtering
by endpoint/count/control data does not construct the internal Qbar_BECD
subtower mechanism.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_mixed_support_subtower_contract
"""

from __future__ import annotations


failures: list[str] = []

DOMAIN_ID = "D_Qbar_BECD_eff"

REQUIRED_EDGES = {
    ("boundary_stratum_product", "internal_effectivity_image"),
    ("internal_effectivity_image", "mixed_support_internalization"),
    ("mixed_support_internalization", "internal_effectivity_domain"),
    ("mixed_support_internalization", "prime_power_subtowers"),
    ("mixed_support_internalization", "mixed_support_subtowers"),
    ("mixed_support_internalization", "valuation_depth"),
    ("mixed_support_internalization", "dd4_boundary_localization"),
    ("dd4_boundary_localization", "internal_effectivity_domain"),
    ("internal_effectivity_domain", "endpoint"),
    ("internal_effectivity_domain", "boundary"),
    ("internal_effectivity_domain", "control_death"),
    ("boundary", "pushforward"),
    ("endpoint", "pushforward"),
    ("pushforward", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
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


def support_union(chars: dict[str, dict[int, int]]) -> tuple[int, ...]:
    keys: set[int] = set()
    for chi in chars.values():
        keys.update(chi)
    return tuple(sorted(keys))


def valuation_depth(n: int, p: int = 2) -> int | None:
    depth = 0
    while n > 1 and n % p == 0:
        n //= p
        depth += 1
    return depth if n == 1 else None


def project_to_prime_power_tower(chi: dict[int, int], p: int = 2) -> dict[int, int]:
    return normalize({key: val for key, val in chi.items() if valuation_depth(key, p) is not None})


def factor_signature(n: int) -> tuple[tuple[int, int], ...]:
    factors: list[tuple[int, int]] = []
    d = 2
    while d * d <= n:
        exponent = 0
        while n % d == 0:
            n //= d
            exponent += 1
        if exponent:
            factors.append((d, exponent))
        d += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def mixed_keys(chars: dict[str, dict[int, int]]) -> tuple[int, ...]:
    return tuple(key for key in support_union(chars) if valuation_depth(key) is None)


def source(**kwargs):
    data = {
        "carrier_native": False,
        "product_internal_image_actual": False,
        "one_internal_effectivity_domain_actual": False,
        "mixed_support_internalization_actual": False,
        "same_domain_types_all_product_images": False,
        "non_2_support_retained": False,
        "mixed_coefficients_retained": False,
        "signed_support_retained": False,
        "valuation_depth_native_to_domain": False,
        "prime_power_subtowers_native_to_domain": False,
        "mixed_support_subtowers_native_to_domain": False,
        "dd4_boundary_localization_feeds_domain": False,
        "domain_has_no_endpoint_or_count_prerequisite": False,
        "domain_generates_endpoint_integrality": False,
        "domain_generates_boundary_localization": False,
        "domain_generates_pushforward_compatibility": False,
        "domain_generates_graph_rosati_count": False,
        "domain_generates_control_death": False,
        "controls_undefined_at_mixed_support": False,
        "dh_undefined_at_mixed_support": False,
        "epstein_undefined_at_mixed_support": False,
        "required_edges": set(),
        "two_power_projection": False,
        "non_two_support_deletion": False,
        "external_prime_factorization": False,
        "prime_axis_tags": False,
        "boundary_null_declaration": False,
        "control_death_after_product": False,
        "weighted_zero_locus": False,
        "support_key_tower": False,
        "endpoint_degree_fiber": False,
        "graph_count_fiber": False,
        "local_product_stack": False,
        "finite_prime_sample": False,
        "finite_product_table": False,
        "declared_mixed_support_domain": False,
        "posthoc_gate_intersection": False,
        "control_formable": True,
        "dh_formable": True,
        "epstein_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("product_internal_image_actual", "product_internal_image_not_actual"),
    (
        "one_internal_effectivity_domain_actual",
        "one_internal_effectivity_domain_not_actual",
    ),
    (
        "mixed_support_internalization_actual",
        "mixed_support_internalization_not_actual",
    ),
    (
        "same_domain_types_all_product_images",
        "same_domain_does_not_type_all_product_images",
    ),
    ("non_2_support_retained", "non_2_support_not_retained"),
    ("mixed_coefficients_retained", "mixed_coefficients_not_retained"),
    ("signed_support_retained", "signed_support_not_retained"),
    ("valuation_depth_native_to_domain", "valuation_depth_not_native_to_domain"),
    (
        "prime_power_subtowers_native_to_domain",
        "prime_power_subtowers_not_native_to_domain",
    ),
    (
        "mixed_support_subtowers_native_to_domain",
        "mixed_support_subtowers_not_native_to_domain",
    ),
    (
        "dd4_boundary_localization_feeds_domain",
        "dd4_boundary_localization_not_feeding_domain",
    ),
    (
        "domain_has_no_endpoint_or_count_prerequisite",
        "domain_has_endpoint_or_count_prerequisite",
    ),
    ("domain_generates_endpoint_integrality", "endpoint_integrality_not_generated"),
    (
        "domain_generates_boundary_localization",
        "boundary_localization_not_generated",
    ),
    (
        "domain_generates_pushforward_compatibility",
        "pushforward_compatibility_not_generated",
    ),
    ("domain_generates_graph_rosati_count", "graph_rosati_count_not_generated"),
    ("domain_generates_control_death", "control_death_not_generated"),
    (
        "controls_undefined_at_mixed_support",
        "controls_not_undefined_at_mixed_support",
    ),
    ("dh_undefined_at_mixed_support", "dh_not_undefined_at_mixed_support"),
    (
        "epstein_undefined_at_mixed_support",
        "epstein_not_undefined_at_mixed_support",
    ),
)

BANNED = (
    ("two_power_projection", "two_power_projection"),
    ("non_two_support_deletion", "non_two_support_deletion"),
    ("external_prime_factorization", "external_prime_factorization"),
    ("prime_axis_tags", "prime_axis_tags"),
    ("boundary_null_declaration", "boundary_null_declaration"),
    ("control_death_after_product", "control_death_after_product"),
    ("weighted_zero_locus", "weighted_zero_locus"),
    ("support_key_tower", "support_key_tower"),
    ("endpoint_degree_fiber", "endpoint_degree_fiber"),
    ("graph_count_fiber", "graph_count_fiber"),
    ("local_product_stack", "local_product_stack"),
    ("finite_prime_sample", "finite_prime_sample"),
    ("finite_product_table", "finite_product_table"),
    ("declared_mixed_support_domain", "declared_mixed_support_domain"),
    ("posthoc_gate_intersection", "posthoc_gate_intersection"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_mixed_support_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_mixed_support_internalization(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        product_internal_image_actual=True,
        one_internal_effectivity_domain_actual=True,
        mixed_support_internalization_actual=True,
        same_domain_types_all_product_images=True,
        non_2_support_retained=True,
        mixed_coefficients_retained=True,
        signed_support_retained=True,
        valuation_depth_native_to_domain=True,
        prime_power_subtowers_native_to_domain=True,
        mixed_support_subtowers_native_to_domain=True,
        dd4_boundary_localization_feeds_domain=True,
        domain_has_no_endpoint_or_count_prerequisite=True,
        domain_generates_endpoint_integrality=True,
        domain_generates_boundary_localization=True,
        domain_generates_pushforward_compatibility=True,
        domain_generates_graph_rosati_count=True,
        domain_generates_control_death=True,
        controls_undefined_at_mixed_support=True,
        dh_undefined_at_mixed_support=True,
        epstein_undefined_at_mixed_support=True,
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

products = {
    "z": z,
    "zL": convolve_chi(z, chi_L),
    "zC3": convolve_chi(z, chi_C3),
    "zF22": convolve_chi(z, chi_F22),
    "zF41": convolve_chi(z, chi_F41),
    "zLF22": convolve_chi(z, chi_LF22),
}

projected_products = {
    name: project_to_prime_power_tower(chi) for name, chi in products.items()
}
all_support = support_union(products)
depths = tuple((key, valuation_depth(key)) for key in all_support)
mixed_support = mixed_keys(products)


gate(
    "PMS1 product image exposes mixed support inside one domain target",
    products["z"] == {1: 2, 2: -1}
    and products["zL"] == {1: 2, 2: 1, 4: -1}
    and products["zC3"] == {3: 2, 6: -1}
    and products["zF22"] == {2: 4, 4: -2}
    and products["zF41"] == {4: 2, 8: -1}
    and products["zLF22"] == {2: 4, 4: 2, 8: -2}
    and all_support == (1, 2, 3, 4, 6, 8)
    and depths == ((1, 0), (2, 1), (3, None), (4, 2), (6, None), (8, 3))
    and mixed_support == (3, 6),
    "domain=%s support=%s depths=%s mixed=%s"
    % (DOMAIN_ID, all_support, depths, mixed_support),
)


two_power_projection = live_source(
    product_internal_image_actual=False,
    mixed_support_internalization_actual=False,
    same_domain_types_all_product_images=False,
    non_2_support_retained=False,
    mixed_coefficients_retained=False,
    signed_support_retained=False,
    mixed_support_subtowers_native_to_domain=False,
    two_power_projection=True,
    non_two_support_deletion=True,
    support_key_tower=True,
    control_formable=True,
)

gate(
    "PMS2 projecting to the 2-power tower deletes the z*C3 image",
    projected_products["zC3"] == {}
    and projected_products["zLF22"] == products["zLF22"]
    and not accepts_mixed_support_internalization(two_power_projection)
    and {
        "product_internal_image_not_actual",
        "mixed_support_internalization_not_actual",
        "same_domain_does_not_type_all_product_images",
        "non_2_support_not_retained",
        "mixed_coefficients_not_retained",
        "signed_support_not_retained",
        "mixed_support_subtowers_not_native_to_domain",
        "two_power_projection",
        "non_two_support_deletion",
        "support_key_tower",
        "control_formable",
    }
    <= set(reasons(two_power_projection)),
    ",".join(reasons(two_power_projection)),
)


external_factorization = live_source(
    carrier_native=False,
    mixed_support_internalization_actual=False,
    valuation_depth_native_to_domain=False,
    mixed_support_subtowers_native_to_domain=False,
    external_prime_factorization=True,
    prime_axis_tags=True,
    local_product_stack=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "PMS3 external prime-axis tags for 6 are labels, not carrier structure",
    factor_signature(6) == ((2, 1), (3, 1))
    and factor_signature(3) == ((3, 1),)
    and not accepts_mixed_support_internalization(external_factorization)
    and {
        "not_carrier_native",
        "mixed_support_internalization_not_actual",
        "valuation_depth_not_native_to_domain",
        "mixed_support_subtowers_not_native_to_domain",
        "external_prime_factorization",
        "prime_axis_tags",
        "local_product_stack",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(external_factorization)),
    ",".join(reasons(external_factorization)),
)


boundary_null = live_source(
    product_internal_image_actual=False,
    non_2_support_retained=False,
    mixed_coefficients_retained=False,
    dd4_boundary_localization_feeds_domain=False,
    domain_generates_boundary_localization=False,
    domain_generates_control_death=False,
    boundary_null_declaration=True,
    control_death_after_product=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "PMS4 declaring 3 and 6 boundary-null or control-dead is too late",
    support(products["zC3"]) == (3, 6)
    and not accepts_mixed_support_internalization(boundary_null)
    and {
        "product_internal_image_not_actual",
        "non_2_support_not_retained",
        "mixed_coefficients_not_retained",
        "dd4_boundary_localization_not_feeding_domain",
        "boundary_localization_not_generated",
        "control_death_not_generated",
        "boundary_null_declaration",
        "control_death_after_product",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(boundary_null)),
    ",".join(reasons(boundary_null)),
)


weighted_zero = live_source(
    mixed_support_internalization_actual=False,
    non_2_support_retained=False,
    mixed_coefficients_retained=False,
    signed_support_retained=False,
    weighted_zero_locus=True,
    support_key_tower=True,
    endpoint_degree_fiber=True,
    control_formable=True,
)

gate(
    "PMS5 weighted-zero and support-key loci collapse the mixed image",
    all(weighted_mass(chi) == 0 for chi in products.values())
    and len({weighted_mass(chi) for chi in products.values()}) == 1
    and not accepts_mixed_support_internalization(weighted_zero)
    and {
        "mixed_support_internalization_not_actual",
        "non_2_support_not_retained",
        "mixed_coefficients_not_retained",
        "signed_support_not_retained",
        "weighted_zero_locus",
        "support_key_tower",
        "endpoint_degree_fiber",
        "control_formable",
    }
    <= set(reasons(weighted_zero)),
    ",".join(reasons(weighted_zero)),
)


endpoint_count = live_source(
    mixed_support_internalization_actual=False,
    domain_has_no_endpoint_or_count_prerequisite=False,
    domain_generates_endpoint_integrality=False,
    domain_generates_graph_rosati_count=False,
    endpoint_degree_fiber=True,
    graph_count_fiber=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "PMS6 endpoint/count filters reverse mixed-support construction",
    support(products["zLF22"]) == (2, 4, 8)
    and support(products["zC3"]) == (3, 6)
    and not accepts_mixed_support_internalization(endpoint_count)
    and {
        "mixed_support_internalization_not_actual",
        "domain_has_endpoint_or_count_prerequisite",
        "endpoint_integrality_not_generated",
        "graph_rosati_count_not_generated",
        "endpoint_degree_fiber",
        "graph_count_fiber",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(endpoint_count)),
    ",".join(reasons(endpoint_count)),
)


local_stack = live_source(
    carrier_native=False,
    one_internal_effectivity_domain_actual=False,
    same_domain_types_all_product_images=False,
    dd4_boundary_localization_feeds_domain=False,
    local_product_stack=True,
    finite_prime_sample=True,
    finite_product_table=True,
    control_formable=True,
)

gate(
    "PMS7 local multi-prime stacks and finite samples split the domain",
    mixed_support == (3, 6)
    and support_union(projected_products) == (1, 2, 4, 8)
    and not accepts_mixed_support_internalization(local_stack)
    and {
        "not_carrier_native",
        "one_internal_effectivity_domain_not_actual",
        "same_domain_does_not_type_all_product_images",
        "dd4_boundary_localization_not_feeding_domain",
        "local_product_stack",
        "finite_prime_sample",
        "finite_product_table",
        "control_formable",
    }
    <= set(reasons(local_stack)),
    ",".join(reasons(local_stack)),
)


declared = live_source(
    product_internal_image_actual=False,
    mixed_support_internalization_actual=False,
    required_edges=set(),
    declared_mixed_support_domain=True,
)

gate(
    "PMS8 declared mixed-support domain IDs without edges are rejected",
    not accepts_mixed_support_internalization(declared)
    and {
        "product_internal_image_not_actual",
        "mixed_support_internalization_not_actual",
        "required_mixed_support_edges_missing",
        "declared_mixed_support_domain",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


missing_downstream = live_source(
    domain_generates_endpoint_integrality=False,
    domain_generates_boundary_localization=False,
    domain_generates_pushforward_compatibility=False,
    domain_generates_graph_rosati_count=False,
    domain_generates_control_death=False,
    required_edges=REQUIRED_EDGES
    - {
        ("internal_effectivity_domain", "endpoint"),
        ("internal_effectivity_domain", "boundary"),
        ("boundary", "pushforward"),
        ("endpoint", "pushforward"),
        ("pushforward", "graph"),
        ("internal_effectivity_domain", "control_death"),
    },
)

gate(
    "PMS9 mixed-support internalization must still generate downstream data",
    not accepts_mixed_support_internalization(missing_downstream)
    and {
        "endpoint_integrality_not_generated",
        "boundary_localization_not_generated",
        "pushforward_compatibility_not_generated",
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_mixed_support_edges_missing",
    }
    <= set(reasons(missing_downstream)),
    ",".join(reasons(missing_downstream)),
)


live = live_source()
dead_sources = {
    "two_power_projection": two_power_projection,
    "external_factorization": external_factorization,
    "boundary_null": boundary_null,
    "weighted_zero": weighted_zero,
    "endpoint_count": endpoint_count,
    "local_stack": local_stack,
    "declared": declared,
    "missing_downstream": missing_downstream,
}

gate(
    "PMS10 only carrier-native mixed-support internalization passes",
    accepts_mixed_support_internalization(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(
        accepts_mixed_support_internalization(data) for data in dead_sources.values()
    ),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_mixed_support_internalization(data) for data in dead_sources.values()),
        accepts_mixed_support_internalization(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPMS1-PMS10 ALL PASS: product mixed-support subtower contract pinned")
print(
    "VERDICT: the strict-square product image must carry 3 and 6 by a "
    "carrier-native mixed-support internalization inside the same internal "
    "Qbar_BECD effectivity domain. Projection to the 2-power tower, external "
    "factorization, boundary-null declarations, endpoint/count filters, "
    "local stacks, finite tables, declared domains, and control/DH/Epstein "
    "shadows do not construct that mixed-support subtower."
)
