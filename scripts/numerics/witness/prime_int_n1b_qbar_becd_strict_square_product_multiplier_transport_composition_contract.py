r"""Multiplier-transport composition contract for the strict-square product.

Doc 334 requires the mixed-support subtower to be a carrier-native C3
multiplier orbit.  This witness sharpens the categorical requirement: a
represented multiplier transport cannot be a lone arrow.  It must compose
with the strict-square character product, so T_C3 o T_C3 agrees with T_C9
and the transports are natural for the product action.  Single-arrow
transports, finite orbit closures, external multiplier monoids, local stacks,
finite tables, and downstream filters do not construct that functorial
transport law.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_multiplier_transport_composition_contract
"""

from __future__ import annotations


failures: list[str] = []

DOMAIN_ID = "D_Qbar_BECD_eff"

REQUIRED_EDGES = {
    ("internal_effectivity_domain", "multiplier_action_functor"),
    ("multiplier_action_functor", "identity_transport"),
    ("multiplier_action_functor", "C3_transport"),
    ("multiplier_action_functor", "C9_transport"),
    ("C3_transport", "transport_composition"),
    ("transport_composition", "C9_transport"),
    ("product_action", "transport_naturality"),
    ("transport_naturality", "internal_effectivity_domain"),
    ("transport_naturality", "dd4_boundary_localization"),
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


def odd_base_depth(n: int, odd_base: int, p: int = 2) -> int | None:
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
        "multiplier_action_functor_actual": False,
        "identity_transport_actual": False,
        "transport_composition_actual": False,
        "product_action_natural": False,
        "orbits_closed_under_composition": False,
        "same_domain_types_transport_orbits": False,
        "coefficients_retained": False,
        "signed_support_retained": False,
        "relative_depth_native_to_domain": False,
        "dd4_boundary_localization_natural": False,
        "domain_has_no_endpoint_or_count_prerequisite": False,
        "domain_generates_endpoint_integrality": False,
        "domain_generates_boundary_localization": False,
        "domain_generates_pushforward_compatibility": False,
        "domain_generates_graph_rosati_count": False,
        "domain_generates_control_death": False,
        "controls_undefined_at_transport": False,
        "dh_undefined_at_transport": False,
        "epstein_undefined_at_transport": False,
        "required_edges": set(),
        "single_transport_arrow": False,
        "finite_orbit_closure": False,
        "external_multiplier_monoid": False,
        "external_odd_base_label": False,
        "external_prime_factorization": False,
        "prime_axis_tags": False,
        "local_product_stack": False,
        "finite_transport_table": False,
        "declared_action_functor": False,
        "endpoint_degree_fiber": False,
        "graph_count_fiber": False,
        "boundary_kernel_definition": False,
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
        "multiplier_action_functor_actual",
        "multiplier_action_functor_not_actual",
    ),
    ("identity_transport_actual", "identity_transport_not_actual"),
    ("transport_composition_actual", "transport_composition_not_actual"),
    ("product_action_natural", "product_action_not_natural"),
    ("orbits_closed_under_composition", "orbits_not_closed_under_composition"),
    (
        "same_domain_types_transport_orbits",
        "same_domain_does_not_type_transport_orbits",
    ),
    ("coefficients_retained", "coefficients_not_retained"),
    ("signed_support_retained", "signed_support_not_retained"),
    ("relative_depth_native_to_domain", "relative_depth_not_native_to_domain"),
    (
        "dd4_boundary_localization_natural",
        "dd4_boundary_localization_not_natural",
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
    ("controls_undefined_at_transport", "controls_not_undefined_at_transport"),
    ("dh_undefined_at_transport", "dh_not_undefined_at_transport"),
    ("epstein_undefined_at_transport", "epstein_not_undefined_at_transport"),
)

BANNED = (
    ("single_transport_arrow", "single_transport_arrow"),
    ("finite_orbit_closure", "finite_orbit_closure"),
    ("external_multiplier_monoid", "external_multiplier_monoid"),
    ("external_odd_base_label", "external_odd_base_label"),
    ("external_prime_factorization", "external_prime_factorization"),
    ("prime_axis_tags", "prime_axis_tags"),
    ("local_product_stack", "local_product_stack"),
    ("finite_transport_table", "finite_transport_table"),
    ("declared_action_functor", "declared_action_functor"),
    ("endpoint_degree_fiber", "endpoint_degree_fiber"),
    ("graph_count_fiber", "graph_count_fiber"),
    ("boundary_kernel_definition", "boundary_kernel_definition"),
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
        out.append("required_transport_composition_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_transport_composition(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        multiplier_action_functor_actual=True,
        identity_transport_actual=True,
        transport_composition_actual=True,
        product_action_natural=True,
        orbits_closed_under_composition=True,
        same_domain_types_transport_orbits=True,
        coefficients_retained=True,
        signed_support_retained=True,
        relative_depth_native_to_domain=True,
        dd4_boundary_localization_natural=True,
        domain_has_no_endpoint_or_count_prerequisite=True,
        domain_generates_endpoint_integrality=True,
        domain_generates_boundary_localization=True,
        domain_generates_pushforward_compatibility=True,
        domain_generates_graph_rosati_count=True,
        domain_generates_control_death=True,
        controls_undefined_at_transport=True,
        dh_undefined_at_transport=True,
        epstein_undefined_at_transport=True,
        required_edges=set(REQUIRED_EDGES),
        control_formable=False,
        dh_formable=False,
        epstein_formable=False,
    )
    data.update(kwargs)
    return data


C3 = ((3,), (1,), ((0, 0),))
C9 = ((9,), (1,), ((0, 0),))
F22 = ((2,), (2,), ((0, 0),))
ZERO_SPLIT = ((1, 2), (2, -1), ((0, 0), (1, 1)))

z = chi_col(*ZERO_SPLIT)
chi_C3 = chi_col(*C3)
chi_C9 = chi_col(*C9)
chi_F22 = chi_col(*F22)
chi_C3_squared = convolve_chi(chi_C3, chi_C3)
chi_C3F22 = convolve_chi(chi_C3, chi_F22)
chi_C9F22 = convolve_chi(chi_C9, chi_F22)

T3_z = convolve_chi(z, chi_C3)
T9_z = convolve_chi(z, chi_C9)
T3_T3_z = convolve_chi(T3_z, chi_C3)
T3_zF22 = convolve_chi(convolve_chi(z, chi_F22), chi_C3)
T3_z_then_F22 = convolve_chi(T3_z, chi_F22)
z_C3F22 = convolve_chi(z, chi_C3F22)
T9_zF22 = convolve_chi(T9_z, chi_F22)
z_C9F22 = convolve_chi(z, chi_C9F22)

transport_rows = {
    "z": z,
    "T3_z": T3_z,
    "T3_T3_z": T3_T3_z,
    "T9_z": T9_z,
    "T3_zF22": T3_zF22,
    "T9_zF22": T9_zF22,
}


gate(
    "MTC1 multiplier transports must compose and be product-natural",
    chi_C3_squared == chi_C9
    and T3_z == {3: 2, 6: -1}
    and T3_T3_z == {9: 2, 18: -1}
    and T9_z == {9: 2, 18: -1}
    and T3_T3_z == T9_z
    and T3_zF22 == T3_z_then_F22 == z_C3F22 == {6: 4, 12: -2}
    and T9_zF22 == z_C9F22 == {18: 4, 36: -2}
    and support_union(transport_rows) == (1, 2, 3, 6, 9, 12, 18, 36)
    and tuple((key, odd_base_depth(key, 9)) for key in support(T9_zF22))
    == ((18, 1), (36, 2)),
    "support=%s T9F22=%s" % (support_union(transport_rows), T9_zF22),
)


single_arrow = live_source(
    multiplier_action_functor_actual=False,
    identity_transport_actual=False,
    transport_composition_actual=False,
    orbits_closed_under_composition=False,
    same_domain_types_transport_orbits=False,
    single_transport_arrow=True,
    finite_orbit_closure=True,
    control_formable=True,
)

gate(
    "MTC2 a lone C3 transport does not supply the action functor",
    T3_z == {3: 2, 6: -1}
    and T3_T3_z == T9_z
    and not accepts_transport_composition(single_arrow)
    and {
        "multiplier_action_functor_not_actual",
        "identity_transport_not_actual",
        "transport_composition_not_actual",
        "orbits_not_closed_under_composition",
        "same_domain_does_not_type_transport_orbits",
        "single_transport_arrow",
        "finite_orbit_closure",
        "control_formable",
    }
    <= set(reasons(single_arrow)),
    ",".join(reasons(single_arrow)),
)


finite_orbit = live_source(
    product_action_natural=False,
    orbits_closed_under_composition=False,
    relative_depth_native_to_domain=False,
    finite_orbit_closure=True,
    finite_transport_table=True,
    support_key_tower=True,
    control_formable=True,
)

gate(
    "MTC3 finite C3-orbit closures fail when C9 and C9F22 are forced",
    support(T3_z) == (3, 6)
    and support(T9_z) == (9, 18)
    and support(T9_zF22) == (18, 36)
    and not accepts_transport_composition(finite_orbit)
    and {
        "product_action_not_natural",
        "orbits_not_closed_under_composition",
        "relative_depth_not_native_to_domain",
        "finite_orbit_closure",
        "finite_transport_table",
        "support_key_tower",
        "control_formable",
    }
    <= set(reasons(finite_orbit)),
    ",".join(reasons(finite_orbit)),
)


external_monoid = live_source(
    carrier_native=False,
    multiplier_action_functor_actual=False,
    relative_depth_native_to_domain=False,
    dd4_boundary_localization_natural=False,
    external_multiplier_monoid=True,
    external_odd_base_label=True,
    external_prime_factorization=True,
    prime_axis_tags=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "MTC4 external multiplier monoids and prime-axis labels are not action data",
    factor_signature(36) == ((2, 2), (3, 2))
    and chi_C3_squared == chi_C9
    and not accepts_transport_composition(external_monoid)
    and {
        "not_carrier_native",
        "multiplier_action_functor_not_actual",
        "relative_depth_not_native_to_domain",
        "dd4_boundary_localization_not_natural",
        "external_multiplier_monoid",
        "external_odd_base_label",
        "external_prime_factorization",
        "prime_axis_tags",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(external_monoid)),
    ",".join(reasons(external_monoid)),
)


local_stack = live_source(
    carrier_native=False,
    same_domain_types_transport_orbits=False,
    product_action_natural=False,
    dd4_boundary_localization_natural=False,
    local_product_stack=True,
    finite_transport_table=True,
    control_formable=True,
)

gate(
    "MTC5 local orbit stacks split the transport domain",
    support_union(transport_rows) == (1, 2, 3, 6, 9, 12, 18, 36)
    and not accepts_transport_composition(local_stack)
    and {
        "not_carrier_native",
        "same_domain_does_not_type_transport_orbits",
        "product_action_not_natural",
        "dd4_boundary_localization_not_natural",
        "local_product_stack",
        "finite_transport_table",
        "control_formable",
    }
    <= set(reasons(local_stack)),
    ",".join(reasons(local_stack)),
)


declared_functor = live_source(
    multiplier_action_functor_actual=False,
    transport_composition_actual=False,
    product_action_natural=False,
    required_edges=set(),
    declared_action_functor=True,
    finite_transport_table=True,
)

gate(
    "MTC6 declared action functors and tables lack represented edges",
    not accepts_transport_composition(declared_functor)
    and {
        "multiplier_action_functor_not_actual",
        "transport_composition_not_actual",
        "product_action_not_natural",
        "required_transport_composition_edges_missing",
        "declared_action_functor",
        "finite_transport_table",
    }
    <= set(reasons(declared_functor)),
    ",".join(reasons(declared_functor)),
)


downstream_filter = live_source(
    multiplier_action_functor_actual=False,
    domain_has_no_endpoint_or_count_prerequisite=False,
    domain_generates_endpoint_integrality=False,
    domain_generates_boundary_localization=False,
    endpoint_degree_fiber=True,
    graph_count_fiber=True,
    boundary_kernel_definition=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "MTC7 endpoint, graph, and boundary filters are too late",
    not accepts_transport_composition(downstream_filter)
    and {
        "multiplier_action_functor_not_actual",
        "domain_has_endpoint_or_count_prerequisite",
        "endpoint_integrality_not_generated",
        "boundary_localization_not_generated",
        "endpoint_degree_fiber",
        "graph_count_fiber",
        "boundary_kernel_definition",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(downstream_filter)),
    ",".join(reasons(downstream_filter)),
)


weighted_support = live_source(
    multiplier_action_functor_actual=False,
    coefficients_retained=False,
    signed_support_retained=False,
    weighted_zero_locus=True,
    support_key_tower=True,
    control_formable=True,
)

gate(
    "MTC8 weighted-zero and support keys do not encode composition",
    all(weighted_mass(chi) == 0 for chi in transport_rows.values())
    and not accepts_transport_composition(weighted_support)
    and {
        "multiplier_action_functor_not_actual",
        "coefficients_not_retained",
        "signed_support_not_retained",
        "weighted_zero_locus",
        "support_key_tower",
        "control_formable",
    }
    <= set(reasons(weighted_support)),
    ",".join(reasons(weighted_support)),
)


missing_edges = live_source(
    product_action_natural=False,
    domain_generates_pushforward_compatibility=False,
    domain_generates_graph_rosati_count=False,
    domain_generates_control_death=False,
    required_edges=REQUIRED_EDGES
    - {
        ("product_action", "transport_naturality"),
        ("boundary", "pushforward"),
        ("pushforward", "graph"),
        ("internal_effectivity_domain", "control_death"),
    },
)

gate(
    "MTC9 transport composition must remain tied to downstream square data",
    not accepts_transport_composition(missing_edges)
    and {
        "product_action_not_natural",
        "pushforward_compatibility_not_generated",
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_transport_composition_edges_missing",
    }
    <= set(reasons(missing_edges)),
    ",".join(reasons(missing_edges)),
)


control_shadow = live_source(
    carrier_native=False,
    multiplier_action_functor_actual=False,
    controls_undefined_at_transport=False,
    dh_undefined_at_transport=False,
    epstein_undefined_at_transport=False,
    weighted_zero_locus=True,
    endpoint_degree_fiber=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

live = live_source()
dead_sources = {
    "single_arrow": single_arrow,
    "finite_orbit": finite_orbit,
    "external_monoid": external_monoid,
    "local_stack": local_stack,
    "declared_functor": declared_functor,
    "downstream_filter": downstream_filter,
    "weighted_support": weighted_support,
    "missing_edges": missing_edges,
    "control_shadow": control_shadow,
}

gate(
    "MTC10 only the carrier-native multiplier action functor passes",
    not accepts_transport_composition(control_shadow)
    and {
        "not_carrier_native",
        "multiplier_action_functor_not_actual",
        "controls_not_undefined_at_transport",
        "dh_not_undefined_at_transport",
        "epstein_not_undefined_at_transport",
        "weighted_zero_locus",
        "endpoint_degree_fiber",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(control_shadow))
    and accepts_transport_composition(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_transport_composition(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_transport_composition(data) for data in dead_sources.values()),
        accepts_transport_composition(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nMTC1-MTC10 ALL PASS: multiplier-transport composition contract pinned")
print(
    "VERDICT: the strict-square mixed-support transport must be a "
    "carrier-native multiplier action functor with identity, composition, "
    "and product naturality. Lone transports, finite orbit closures, "
    "external multiplier monoids, local stacks, finite tables, downstream "
    "filters, and control/DH/Epstein shadows do not construct it."
)
