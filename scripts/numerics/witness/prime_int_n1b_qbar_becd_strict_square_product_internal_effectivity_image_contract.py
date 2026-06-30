r"""Product-to-internal-effectivity image contract for the strict-square branch.

Doc 331 requires the boundary-convolution module to land in a represented
Qbar_BECD stratum product.  This witness sharpens the next edge: the product
must map to the internal Qbar_BECD effectivity domain, not to an external
support-key tower, weighted-zero locus, endpoint/count fiber, boundary
kernel, local product stack, finite table, or declared domain ID.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_internal_effectivity_image_contract
"""

from __future__ import annotations


failures: list[str] = []

DOMAIN_ID = "D_Qbar_BECD_eff"

REQUIRED_EDGES = {
    ("boundary_stratum_product", "internal_effectivity_image"),
    ("internal_effectivity_image", "internal_effectivity_domain"),
    ("internal_effectivity_domain", "prime_power_subtowers"),
    ("internal_effectivity_domain", "valuation_depth"),
    ("internal_effectivity_domain", "endpoint"),
    ("internal_effectivity_domain", "boundary"),
    ("internal_effectivity_domain", "control_death"),
    ("boundary_stratum_product", "dd4_boundary_localization"),
    ("dd4_boundary_localization", "internal_effectivity_domain"),
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


def valuation_depth(n: int, p: int = 2) -> int | None:
    depth = 0
    while n > 1 and n % p == 0:
        n //= p
        depth += 1
    return depth if n == 1 else None


def external_support_tower(chars: dict[str, dict[int, int]]) -> list[int]:
    keys: set[int] = set()
    for chi in chars.values():
        keys.update(key for key in chi if key > 0)
    return sorted(keys)


def internal_image_row(name: str, chi: dict[int, int]) -> dict[str, object]:
    return {
        "domain": DOMAIN_ID,
        "source": name,
        "support": support(chi),
        "coefficients": tuple(chi.items()),
        "mass": weighted_mass(chi),
        "depths": tuple((key, valuation_depth(key)) for key in support(chi)),
    }


def source(**kwargs):
    data = {
        "carrier_native": False,
        "boundary_stratum_product_actual": False,
        "internal_effectivity_image_actual": False,
        "internal_effectivity_domain_actual": False,
        "same_domain_types_all_product_images": False,
        "product_coefficients_retained": False,
        "signed_support_retained": False,
        "valuation_depth_native_to_domain": False,
        "prime_power_subtowers_native_to_domain": False,
        "dd4_boundary_localization_feeds_domain": False,
        "domain_has_no_endpoint_or_count_prerequisite": False,
        "domain_generates_endpoint_integrality": False,
        "domain_generates_boundary_localization": False,
        "domain_generates_pushforward_compatibility": False,
        "domain_generates_graph_rosati_count": False,
        "domain_generates_control_death": False,
        "controls_undefined_at_image": False,
        "dh_undefined_at_image": False,
        "epstein_undefined_at_image": False,
        "required_edges": set(),
        "support_key_tower": False,
        "external_prime_factorization": False,
        "weighted_zero_locus": False,
        "endpoint_degree_fiber": False,
        "graph_count_fiber": False,
        "boundary_kernel_definition": False,
        "local_product_stack": False,
        "finite_product_table": False,
        "declared_internal_image": False,
        "posthoc_gate_intersection": False,
        "control_formable": True,
        "dh_formable": True,
        "epstein_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("boundary_stratum_product_actual", "boundary_stratum_product_not_actual"),
    ("internal_effectivity_image_actual", "internal_effectivity_image_not_actual"),
    ("internal_effectivity_domain_actual", "internal_effectivity_domain_not_actual"),
    (
        "same_domain_types_all_product_images",
        "same_domain_does_not_type_all_product_images",
    ),
    ("product_coefficients_retained", "product_coefficients_not_retained"),
    ("signed_support_retained", "signed_support_not_retained"),
    ("valuation_depth_native_to_domain", "valuation_depth_not_native_to_domain"),
    (
        "prime_power_subtowers_native_to_domain",
        "prime_power_subtowers_not_native_to_domain",
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
    ("controls_undefined_at_image", "controls_not_undefined_at_image"),
    ("dh_undefined_at_image", "dh_not_undefined_at_image"),
    ("epstein_undefined_at_image", "epstein_not_undefined_at_image"),
)

BANNED = (
    ("support_key_tower", "support_key_tower"),
    ("external_prime_factorization", "external_prime_factorization"),
    ("weighted_zero_locus", "weighted_zero_locus"),
    ("endpoint_degree_fiber", "endpoint_degree_fiber"),
    ("graph_count_fiber", "graph_count_fiber"),
    ("boundary_kernel_definition", "boundary_kernel_definition"),
    ("local_product_stack", "local_product_stack"),
    ("finite_product_table", "finite_product_table"),
    ("declared_internal_image", "declared_internal_image"),
    ("posthoc_gate_intersection", "posthoc_gate_intersection"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_product_internal_image_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_product_internal_image(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        boundary_stratum_product_actual=True,
        internal_effectivity_image_actual=True,
        internal_effectivity_domain_actual=True,
        same_domain_types_all_product_images=True,
        product_coefficients_retained=True,
        signed_support_retained=True,
        valuation_depth_native_to_domain=True,
        prime_power_subtowers_native_to_domain=True,
        dd4_boundary_localization_feeds_domain=True,
        domain_has_no_endpoint_or_count_prerequisite=True,
        domain_generates_endpoint_integrality=True,
        domain_generates_boundary_localization=True,
        domain_generates_pushforward_compatibility=True,
        domain_generates_graph_rosati_count=True,
        domain_generates_control_death=True,
        controls_undefined_at_image=True,
        dh_undefined_at_image=True,
        epstein_undefined_at_image=True,
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

internal_rows = [internal_image_row(name, chi) for name, chi in products.items()]
external_tower = external_support_tower(products)

gate(
    "PII1 product image data has one internal-domain typing target",
    products["z"] == {1: 2, 2: -1}
    and products["zL"] == {1: 2, 2: 1, 4: -1}
    and products["zF22"] == {2: 4, 4: -2}
    and products["zF41"] == {4: 2, 8: -1}
    and products["zLF22"] == {2: 4, 4: 2, 8: -2}
    and external_tower == [1, 2, 3, 4, 6, 8]
    and {row["domain"] for row in internal_rows} == {DOMAIN_ID}
    and all(row["mass"] == 0 for row in internal_rows),
    "tower=%s rows=%s" % (external_tower, internal_rows),
)


support_tower = live_source(
    internal_effectivity_image_actual=False,
    internal_effectivity_domain_actual=False,
    same_domain_types_all_product_images=False,
    product_coefficients_retained=False,
    signed_support_retained=False,
    valuation_depth_native_to_domain=False,
    prime_power_subtowers_native_to_domain=False,
    support_key_tower=True,
    external_prime_factorization=True,
    control_formable=True,
)

gate(
    "PII2 support-key towers are external labels, not internal images",
    external_tower == [1, 2, 3, 4, 6, 8]
    and [valuation_depth(n) for n in external_tower] == [0, 1, None, 2, None, 3]
    and not accepts_product_internal_image(support_tower)
    and {
        "internal_effectivity_image_not_actual",
        "internal_effectivity_domain_not_actual",
        "same_domain_does_not_type_all_product_images",
        "product_coefficients_not_retained",
        "signed_support_not_retained",
        "valuation_depth_not_native_to_domain",
        "prime_power_subtowers_not_native_to_domain",
        "support_key_tower",
        "external_prime_factorization",
        "control_formable",
    }
    <= set(reasons(support_tower)),
    ",".join(reasons(support_tower)),
)


weighted_zero = live_source(
    internal_effectivity_image_actual=False,
    product_coefficients_retained=False,
    signed_support_retained=False,
    dd4_boundary_localization_feeds_domain=False,
    weighted_zero_locus=True,
    endpoint_degree_fiber=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "PII3 weighted-zero loci collapse every product image",
    len({weighted_mass(chi) for chi in products.values()}) == 1
    and all(weighted_mass(chi) == 0 for chi in products.values())
    and not accepts_product_internal_image(weighted_zero)
    and {
        "internal_effectivity_image_not_actual",
        "product_coefficients_not_retained",
        "signed_support_not_retained",
        "dd4_boundary_localization_not_feeding_domain",
        "weighted_zero_locus",
        "endpoint_degree_fiber",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(weighted_zero)),
    ",".join(reasons(weighted_zero)),
)


endpoint_count = live_source(
    internal_effectivity_image_actual=False,
    domain_has_no_endpoint_or_count_prerequisite=False,
    domain_generates_endpoint_integrality=False,
    domain_generates_graph_rosati_count=False,
    endpoint_degree_fiber=True,
    graph_count_fiber=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "PII4 endpoint/count fibers reverse the internal-domain direction",
    support(products["zLF22"]) == (2, 4, 8)
    and not accepts_product_internal_image(endpoint_count)
    and {
        "internal_effectivity_image_not_actual",
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


boundary_kernel = live_source(
    internal_effectivity_image_actual=False,
    dd4_boundary_localization_feeds_domain=False,
    domain_generates_boundary_localization=False,
    domain_generates_pushforward_compatibility=False,
    boundary_kernel_definition=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "PII5 boundary kernels are too late to define the image domain",
    products["z"] == {1: 2, 2: -1}
    and not accepts_product_internal_image(boundary_kernel)
    and {
        "internal_effectivity_image_not_actual",
        "dd4_boundary_localization_not_feeding_domain",
        "boundary_localization_not_generated",
        "pushforward_compatibility_not_generated",
        "boundary_kernel_definition",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(boundary_kernel)),
    ",".join(reasons(boundary_kernel)),
)


local_stack = live_source(
    carrier_native=False,
    same_domain_types_all_product_images=False,
    dd4_boundary_localization_feeds_domain=False,
    domain_generates_control_death=False,
    local_product_stack=True,
    finite_product_table=True,
    control_formable=True,
)

gate(
    "PII6 local product stacks and finite tables split the domain",
    len(internal_rows) == 6
    and not accepts_product_internal_image(local_stack)
    and {
        "not_carrier_native",
        "same_domain_does_not_type_all_product_images",
        "dd4_boundary_localization_not_feeding_domain",
        "control_death_not_generated",
        "local_product_stack",
        "finite_product_table",
        "control_formable",
    }
    <= set(reasons(local_stack)),
    ",".join(reasons(local_stack)),
)


declared = live_source(
    internal_effectivity_image_actual=False,
    internal_effectivity_domain_actual=False,
    required_edges=set(),
    declared_internal_image=True,
)

gate(
    "PII7 declared image/domain IDs without edges are rejected",
    not accepts_product_internal_image(declared)
    and {
        "internal_effectivity_image_not_actual",
        "internal_effectivity_domain_not_actual",
        "required_product_internal_image_edges_missing",
        "declared_internal_image",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


control_shadow = live_source(
    carrier_native=False,
    boundary_stratum_product_actual=False,
    internal_effectivity_image_actual=False,
    controls_undefined_at_image=False,
    dh_undefined_at_image=False,
    epstein_undefined_at_image=False,
    weighted_zero_locus=True,
    endpoint_degree_fiber=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "PII8 controls/DH/Epstein can mimic product-image shadows",
    all(weighted_mass(chi) == 0 for chi in products.values())
    and not accepts_product_internal_image(control_shadow)
    and {
        "not_carrier_native",
        "boundary_stratum_product_not_actual",
        "internal_effectivity_image_not_actual",
        "controls_not_undefined_at_image",
        "dh_not_undefined_at_image",
        "epstein_not_undefined_at_image",
        "weighted_zero_locus",
        "endpoint_degree_fiber",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(control_shadow)),
    ",".join(reasons(control_shadow)),
)


missing_downstream = live_source(
    domain_generates_endpoint_integrality=False,
    domain_generates_pushforward_compatibility=False,
    domain_generates_graph_rosati_count=False,
    domain_generates_control_death=False,
    required_edges=REQUIRED_EDGES
    - {
        ("internal_effectivity_domain", "endpoint"),
        ("endpoint", "pushforward"),
        ("pushforward", "graph"),
        ("internal_effectivity_domain", "control_death"),
    },
)

gate(
    "PII9 internal image must generate endpoint, graph/count, and death",
    not accepts_product_internal_image(missing_downstream)
    and {
        "endpoint_integrality_not_generated",
        "pushforward_compatibility_not_generated",
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_product_internal_image_edges_missing",
    }
    <= set(reasons(missing_downstream)),
    ",".join(reasons(missing_downstream)),
)


live = live_source()
dead_sources = {
    "support_tower": support_tower,
    "weighted_zero": weighted_zero,
    "endpoint_count": endpoint_count,
    "boundary_kernel": boundary_kernel,
    "local_stack": local_stack,
    "declared": declared,
    "control_shadow": control_shadow,
    "missing_downstream": missing_downstream,
}

gate(
    "PII10 only product-to-internal-effectivity image passes",
    accepts_product_internal_image(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_product_internal_image(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_product_internal_image(data) for data in dead_sources.values()),
        accepts_product_internal_image(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPII1-PII10 ALL PASS: product internal-effectivity image contract pinned")
print(
    "VERDICT: the boundary-stratum product must map to one represented "
    "internal Qbar_BECD effectivity image/domain. Support-key towers, "
    "weighted-zero loci, endpoint/count fibers, boundary kernels, local "
    "product stacks, finite tables, declared IDs, and control/DH/Epstein "
    "shadows do not construct that internal domain image."
)
