r"""Mixed-support multiplier-orbit closure contract for the strict square.

Doc 333 requires the product image to carry the mixed support 3 and 6 inside
the same internal Qbar_BECD domain.  This witness sharpens that into an
orbit-closure requirement: since z*C3 is a multiplier translate of z, the
mixed-support subtower must be closed under the represented product action.
A finite {3,6} patch, external odd-base label, local product stack, finite
table, or downstream endpoint/count/control filter is not the needed
carrier-native multiplier transport.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_mixed_support_orbit_closure_contract
"""

from __future__ import annotations


failures: list[str] = []

DOMAIN_ID = "D_Qbar_BECD_eff"

REQUIRED_EDGES = {
    ("mixed_support_internalization", "multiplier_transport_C3"),
    ("prime_power_subtower", "multiplier_transport_C3"),
    ("multiplier_transport_C3", "odd_base_subtower"),
    ("multiplier_transport_C3", "product_action"),
    ("product_action", "orbit_closure"),
    ("orbit_closure", "internal_effectivity_domain"),
    ("orbit_closure", "dd4_boundary_localization"),
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


def odd_base_depth(n: int, odd_base: int = 3, p: int = 2) -> int | None:
    if n % odd_base != 0:
        return None
    return valuation_depth(n // odd_base, p)


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


def source(**kwargs):
    data = {
        "carrier_native": False,
        "mixed_support_internalization_actual": False,
        "multiplier_transport_actual": False,
        "product_action_equivariant": False,
        "orbit_closed_under_character_convolution": False,
        "same_domain_types_base_and_c3_orbit": False,
        "odd_base_subtower_native_to_domain": False,
        "base_prime_power_subtower_native_to_domain": False,
        "coefficients_retained": False,
        "signed_support_retained": False,
        "relative_depth_native_to_domain": False,
        "dd4_boundary_localization_equivariant": False,
        "domain_has_no_endpoint_or_count_prerequisite": False,
        "domain_generates_endpoint_integrality": False,
        "domain_generates_boundary_localization": False,
        "domain_generates_pushforward_compatibility": False,
        "domain_generates_graph_rosati_count": False,
        "domain_generates_control_death": False,
        "controls_undefined_at_orbit": False,
        "dh_undefined_at_orbit": False,
        "epstein_undefined_at_orbit": False,
        "required_edges": set(),
        "finite_mixed_patch": False,
        "truncated_orbit": False,
        "external_odd_base_label": False,
        "external_prime_factorization": False,
        "prime_axis_tags": False,
        "local_product_stack": False,
        "finite_orbit_sample": False,
        "finite_product_table": False,
        "declared_transport": False,
        "endpoint_degree_fiber": False,
        "graph_count_fiber": False,
        "boundary_kernel_definition": False,
        "control_death_after_orbit": False,
        "weighted_zero_locus": False,
        "support_key_tower": False,
        "posthoc_gate_intersection": False,
        "control_formable": True,
        "dh_formable": True,
        "epstein_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    (
        "mixed_support_internalization_actual",
        "mixed_support_internalization_not_actual",
    ),
    ("multiplier_transport_actual", "multiplier_transport_not_actual"),
    ("product_action_equivariant", "product_action_not_equivariant"),
    (
        "orbit_closed_under_character_convolution",
        "orbit_not_closed_under_character_convolution",
    ),
    (
        "same_domain_types_base_and_c3_orbit",
        "same_domain_does_not_type_base_and_c3_orbit",
    ),
    (
        "odd_base_subtower_native_to_domain",
        "odd_base_subtower_not_native_to_domain",
    ),
    (
        "base_prime_power_subtower_native_to_domain",
        "base_prime_power_subtower_not_native_to_domain",
    ),
    ("coefficients_retained", "coefficients_not_retained"),
    ("signed_support_retained", "signed_support_not_retained"),
    ("relative_depth_native_to_domain", "relative_depth_not_native_to_domain"),
    (
        "dd4_boundary_localization_equivariant",
        "dd4_boundary_localization_not_equivariant",
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
    ("controls_undefined_at_orbit", "controls_not_undefined_at_orbit"),
    ("dh_undefined_at_orbit", "dh_not_undefined_at_orbit"),
    ("epstein_undefined_at_orbit", "epstein_not_undefined_at_orbit"),
)

BANNED = (
    ("finite_mixed_patch", "finite_mixed_patch"),
    ("truncated_orbit", "truncated_orbit"),
    ("external_odd_base_label", "external_odd_base_label"),
    ("external_prime_factorization", "external_prime_factorization"),
    ("prime_axis_tags", "prime_axis_tags"),
    ("local_product_stack", "local_product_stack"),
    ("finite_orbit_sample", "finite_orbit_sample"),
    ("finite_product_table", "finite_product_table"),
    ("declared_transport", "declared_transport"),
    ("endpoint_degree_fiber", "endpoint_degree_fiber"),
    ("graph_count_fiber", "graph_count_fiber"),
    ("boundary_kernel_definition", "boundary_kernel_definition"),
    ("control_death_after_orbit", "control_death_after_orbit"),
    ("weighted_zero_locus", "weighted_zero_locus"),
    ("support_key_tower", "support_key_tower"),
    ("posthoc_gate_intersection", "posthoc_gate_intersection"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_orbit_closure_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_orbit_closure(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        mixed_support_internalization_actual=True,
        multiplier_transport_actual=True,
        product_action_equivariant=True,
        orbit_closed_under_character_convolution=True,
        same_domain_types_base_and_c3_orbit=True,
        odd_base_subtower_native_to_domain=True,
        base_prime_power_subtower_native_to_domain=True,
        coefficients_retained=True,
        signed_support_retained=True,
        relative_depth_native_to_domain=True,
        dd4_boundary_localization_equivariant=True,
        domain_has_no_endpoint_or_count_prerequisite=True,
        domain_generates_endpoint_integrality=True,
        domain_generates_boundary_localization=True,
        domain_generates_pushforward_compatibility=True,
        domain_generates_graph_rosati_count=True,
        domain_generates_control_death=True,
        controls_undefined_at_orbit=True,
        dh_undefined_at_orbit=True,
        epstein_undefined_at_orbit=True,
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
chi_C3F22 = convolve_chi(chi_C3, chi_F22)

base_products = {
    "z": z,
    "zL": convolve_chi(z, chi_L),
    "zF22": convolve_chi(z, chi_F22),
    "zF41": convolve_chi(z, chi_F41),
    "zLF22": convolve_chi(z, chi_LF22),
}

c3_orbit_products = {
    "zC3": convolve_chi(z, chi_C3),
    "zC3L": convolve_chi(convolve_chi(z, chi_C3), chi_L),
    "zC3F22": convolve_chi(convolve_chi(z, chi_C3), chi_F22),
    "zC3F41": convolve_chi(convolve_chi(z, chi_C3), chi_F41),
    "zC3LF22": convolve_chi(convolve_chi(z, chi_C3), chi_LF22),
}

odd_orbit_support = support_union(c3_orbit_products)
odd_depths = tuple((key, odd_base_depth(key)) for key in odd_orbit_support)
base_support = support_union(base_products)
base_depths = tuple((key, valuation_depth(key)) for key in base_support)


gate(
    "MOC1 C3 transport forces an odd-base subtower, not only 3 and 6",
    c3_orbit_products["zC3"] == {3: 2, 6: -1}
    and c3_orbit_products["zC3L"] == {3: 2, 6: 1, 12: -1}
    and c3_orbit_products["zC3F22"] == {6: 4, 12: -2}
    and c3_orbit_products["zC3F41"] == {12: 2, 24: -1}
    and c3_orbit_products["zC3LF22"] == {6: 4, 12: 2, 24: -2}
    and convolve_chi(convolve_chi(z, chi_C3), chi_F22)
    == convolve_chi(z, chi_C3F22)
    and base_support == (1, 2, 4, 8)
    and base_depths == ((1, 0), (2, 1), (4, 2), (8, 3))
    and odd_orbit_support == (3, 6, 12, 24)
    and odd_depths == ((3, 0), (6, 1), (12, 2), (24, 3)),
    "base=%s odd=%s odd_depths=%s" % (base_support, odd_orbit_support, odd_depths),
)


finite_patch = live_source(
    multiplier_transport_actual=False,
    product_action_equivariant=False,
    orbit_closed_under_character_convolution=False,
    odd_base_subtower_native_to_domain=False,
    relative_depth_native_to_domain=False,
    finite_mixed_patch=True,
    truncated_orbit=True,
    finite_orbit_sample=True,
    control_formable=True,
)

gate(
    "MOC2 finite {3,6} patches fail under F22 and F41 action",
    support(c3_orbit_products["zC3"]) == (3, 6)
    and 12 in support(c3_orbit_products["zC3F22"])
    and 24 in support(c3_orbit_products["zC3F41"])
    and not accepts_orbit_closure(finite_patch)
    and {
        "multiplier_transport_not_actual",
        "product_action_not_equivariant",
        "orbit_not_closed_under_character_convolution",
        "odd_base_subtower_not_native_to_domain",
        "relative_depth_not_native_to_domain",
        "finite_mixed_patch",
        "truncated_orbit",
        "finite_orbit_sample",
        "control_formable",
    }
    <= set(reasons(finite_patch)),
    ",".join(reasons(finite_patch)),
)


external_label = live_source(
    carrier_native=False,
    multiplier_transport_actual=False,
    odd_base_subtower_native_to_domain=False,
    relative_depth_native_to_domain=False,
    dd4_boundary_localization_equivariant=False,
    external_odd_base_label=True,
    external_prime_factorization=True,
    prime_axis_tags=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "MOC3 odd-base labels and prime factorizations are not transport",
    factor_signature(24) == ((2, 3), (3, 1))
    and odd_depths == ((3, 0), (6, 1), (12, 2), (24, 3))
    and not accepts_orbit_closure(external_label)
    and {
        "not_carrier_native",
        "multiplier_transport_not_actual",
        "odd_base_subtower_not_native_to_domain",
        "relative_depth_not_native_to_domain",
        "dd4_boundary_localization_not_equivariant",
        "external_odd_base_label",
        "external_prime_factorization",
        "prime_axis_tags",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(external_label)),
    ",".join(reasons(external_label)),
)


local_stack = live_source(
    carrier_native=False,
    same_domain_types_base_and_c3_orbit=False,
    product_action_equivariant=False,
    dd4_boundary_localization_equivariant=False,
    local_product_stack=True,
    finite_product_table=True,
    control_formable=True,
)

gate(
    "MOC4 local base-by-odd stacks split the domain",
    base_support == (1, 2, 4, 8)
    and odd_orbit_support == (3, 6, 12, 24)
    and not accepts_orbit_closure(local_stack)
    and {
        "not_carrier_native",
        "same_domain_does_not_type_base_and_c3_orbit",
        "product_action_not_equivariant",
        "dd4_boundary_localization_not_equivariant",
        "local_product_stack",
        "finite_product_table",
        "control_formable",
    }
    <= set(reasons(local_stack)),
    ",".join(reasons(local_stack)),
)


declared_transport = live_source(
    mixed_support_internalization_actual=False,
    multiplier_transport_actual=False,
    product_action_equivariant=False,
    required_edges=set(),
    declared_transport=True,
    finite_orbit_sample=True,
)

gate(
    "MOC5 declared transports and finite orbit tables lack edges",
    not accepts_orbit_closure(declared_transport)
    and {
        "mixed_support_internalization_not_actual",
        "multiplier_transport_not_actual",
        "product_action_not_equivariant",
        "required_orbit_closure_edges_missing",
        "declared_transport",
        "finite_orbit_sample",
    }
    <= set(reasons(declared_transport)),
    ",".join(reasons(declared_transport)),
)


downstream_filter = live_source(
    mixed_support_internalization_actual=False,
    domain_has_no_endpoint_or_count_prerequisite=False,
    domain_generates_endpoint_integrality=False,
    domain_generates_boundary_localization=False,
    domain_generates_control_death=False,
    endpoint_degree_fiber=True,
    graph_count_fiber=True,
    boundary_kernel_definition=True,
    control_death_after_orbit=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "MOC6 endpoint, boundary, and control filters are downstream of orbit closure",
    not accepts_orbit_closure(downstream_filter)
    and {
        "mixed_support_internalization_not_actual",
        "domain_has_endpoint_or_count_prerequisite",
        "endpoint_integrality_not_generated",
        "boundary_localization_not_generated",
        "control_death_not_generated",
        "endpoint_degree_fiber",
        "graph_count_fiber",
        "boundary_kernel_definition",
        "control_death_after_orbit",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(downstream_filter)),
    ",".join(reasons(downstream_filter)),
)


weighted_support = live_source(
    mixed_support_internalization_actual=False,
    multiplier_transport_actual=False,
    coefficients_retained=False,
    signed_support_retained=False,
    weighted_zero_locus=True,
    support_key_tower=True,
    control_formable=True,
)

gate(
    "MOC7 weighted-zero and support keys do not encode orbit transport",
    all(weighted_mass(chi) == 0 for chi in c3_orbit_products.values())
    and support_union(c3_orbit_products) == (3, 6, 12, 24)
    and not accepts_orbit_closure(weighted_support)
    and {
        "mixed_support_internalization_not_actual",
        "multiplier_transport_not_actual",
        "coefficients_not_retained",
        "signed_support_not_retained",
        "weighted_zero_locus",
        "support_key_tower",
        "control_formable",
    }
    <= set(reasons(weighted_support)),
    ",".join(reasons(weighted_support)),
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
    "MOC8 orbit closure must still generate downstream square data",
    not accepts_orbit_closure(missing_downstream)
    and {
        "endpoint_integrality_not_generated",
        "pushforward_compatibility_not_generated",
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_orbit_closure_edges_missing",
    }
    <= set(reasons(missing_downstream)),
    ",".join(reasons(missing_downstream)),
)


control_shadow = live_source(
    carrier_native=False,
    multiplier_transport_actual=False,
    controls_undefined_at_orbit=False,
    dh_undefined_at_orbit=False,
    epstein_undefined_at_orbit=False,
    weighted_zero_locus=True,
    endpoint_degree_fiber=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "MOC9 controls/DH/Epstein can mimic orbit shadows but not formation",
    not accepts_orbit_closure(control_shadow)
    and {
        "not_carrier_native",
        "multiplier_transport_not_actual",
        "controls_not_undefined_at_orbit",
        "dh_not_undefined_at_orbit",
        "epstein_not_undefined_at_orbit",
        "weighted_zero_locus",
        "endpoint_degree_fiber",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(control_shadow)),
    ",".join(reasons(control_shadow)),
)


live = live_source()
dead_sources = {
    "finite_patch": finite_patch,
    "external_label": external_label,
    "local_stack": local_stack,
    "declared_transport": declared_transport,
    "downstream_filter": downstream_filter,
    "weighted_support": weighted_support,
    "missing_downstream": missing_downstream,
    "control_shadow": control_shadow,
}

gate(
    "MOC10 only carrier-native multiplier-orbit closure passes",
    accepts_orbit_closure(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_orbit_closure(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_orbit_closure(data) for data in dead_sources.values()),
        accepts_orbit_closure(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nMOC1-MOC10 ALL PASS: mixed-support multiplier-orbit closure contract pinned")
print(
    "VERDICT: the mixed-support subtower must be a carrier-native "
    "C3-multiplier orbit closed under strict-square character convolution. "
    "A finite {3,6} patch, external odd-base label, local product stack, "
    "finite table, downstream endpoint/count/control filter, or "
    "control/DH/Epstein shadow does not construct that orbit closure."
)
