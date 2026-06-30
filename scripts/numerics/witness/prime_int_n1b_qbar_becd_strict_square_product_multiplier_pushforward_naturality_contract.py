r"""Pushforward naturality contract for the strict-square multiplier action.

Doc 337 requires endpoint integrality and the two degree maps to be generated
by the DD.4-natural multiplier-action domain.  This witness sharpens the next
edge: the boundary localization and endpoint degree maps must feed the same
p1_* and p2_* pushforward squares.  Detached boundary exactness, endpoint
filters, symbolic composition, formal adjoints, projection retunings, finite
tables, and declared pushforward squares do not construct that compatibility.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_multiplier_pushforward_naturality_contract
"""

from __future__ import annotations


failures: list[str] = []

DOMAIN_ID = "D_Qbar_BECD_eff"
BOUNDARY_ID = "B_Qbar_BECD_DD4"
PUSHFORWARD_ID = "PF_Qbar_BECD_p1p2"

REQUIRED_EDGES = {
    ("dd4_boundary_localization", "boundary_endpoint_pushforward"),
    ("endpoint_degree_maps", "boundary_endpoint_pushforward"),
    ("multiplier_action_functor", "boundary_endpoint_pushforward"),
    ("boundary_endpoint_pushforward", "p1_pushforward"),
    ("boundary_endpoint_pushforward", "p2_pushforward"),
    ("p1_pushforward", "pushforward_naturality"),
    ("p2_pushforward", "pushforward_naturality"),
    ("pushforward_naturality", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
    ("internal_effectivity_domain", "endpoint"),
    ("internal_effectivity_domain", "boundary"),
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


def support(chi: dict[int, int]) -> tuple[int, ...]:
    return tuple(sorted(chi))


def weighted_mass(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items())


def endpoint_degrees(chi: dict[int, int]) -> tuple[int, int]:
    positive = sum(key * val for key, val in chi.items() if val > 0)
    negative = sum(key * (-val) for key, val in chi.items() if val < 0)
    return positive, negative


def multiplier_degree(chi: dict[int, int]) -> int:
    return sum(key * val for key, val in chi.items() if val > 0)


def scale_pair(pair: tuple[int, int], scale: int) -> tuple[int, int]:
    return pair[0] * scale, pair[1] * scale


def pushforward_row(name: str, chi: dict[int, int], transport: str) -> dict[str, object]:
    p1, p2 = endpoint_degrees(chi)
    return {
        "domain": DOMAIN_ID,
        "boundary": BOUNDARY_ID,
        "pushforward": PUSHFORWARD_ID,
        "source": name,
        "transport": transport,
        "support": support(chi),
        "coefficients": tuple(chi.items()),
        "weighted_mass": weighted_mass(chi),
        "p1_degree": p1,
        "p2_degree": p2,
        "endpoint_rank": len(support(chi)),
        "pushforward_defect": p1 - p2,
    }


def source(**kwargs):
    data = {
        "carrier_native": False,
        "multiplier_action_functor_actual": False,
        "dd4_boundary_natural": False,
        "endpoint_degree_maps_actual": False,
        "boundary_endpoint_pushforward_actual": False,
        "p1_pushforward_actual": False,
        "p2_pushforward_actual": False,
        "pushforward_generated_by_domain": False,
        "p1_pushforward_natural": False,
        "p2_pushforward_natural": False,
        "product_pushforward_natural": False,
        "boundary_pushforward_compatible": False,
        "endpoint_pushforward_compatible": False,
        "same_pushforward_types_transport_orbits": False,
        "endpoint_rank_preserved": False,
        "two_degree_maps_retained": False,
        "coefficients_retained": False,
        "signed_support_retained": False,
        "graph_rosati_count_generated": False,
        "control_death_generated": False,
        "controls_undefined_at_pushforward": False,
        "dh_undefined_at_pushforward": False,
        "epstein_undefined_at_pushforward": False,
        "required_edges": set(),
        "detached_boundary_exactness": False,
        "endpoint_degree_filter": False,
        "symbolic_composition_pushforward": False,
        "formal_adjoint_pushforward": False,
        "projection_quotient_or_retuning": False,
        "declared_pushforward_square": False,
        "boundary_after_pushforward_filter": False,
        "graph_count_pushforward_filter": False,
        "support_pushforward": False,
        "weighted_zero_pushforward": False,
        "local_pushforward_stack": False,
        "finite_pushforward_table": False,
        "external_multiplier_degree": False,
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
    ("dd4_boundary_natural", "dd4_boundary_not_natural"),
    ("endpoint_degree_maps_actual", "endpoint_degree_maps_not_actual"),
    (
        "boundary_endpoint_pushforward_actual",
        "boundary_endpoint_pushforward_not_actual",
    ),
    ("p1_pushforward_actual", "p1_pushforward_not_actual"),
    ("p2_pushforward_actual", "p2_pushforward_not_actual"),
    (
        "pushforward_generated_by_domain",
        "pushforward_not_generated_by_domain",
    ),
    ("p1_pushforward_natural", "p1_pushforward_not_natural"),
    ("p2_pushforward_natural", "p2_pushforward_not_natural"),
    ("product_pushforward_natural", "product_pushforward_not_natural"),
    ("boundary_pushforward_compatible", "boundary_pushforward_not_compatible"),
    ("endpoint_pushforward_compatible", "endpoint_pushforward_not_compatible"),
    (
        "same_pushforward_types_transport_orbits",
        "same_pushforward_does_not_type_transport_orbits",
    ),
    ("endpoint_rank_preserved", "endpoint_rank_not_preserved"),
    ("two_degree_maps_retained", "two_degree_maps_not_retained"),
    ("coefficients_retained", "coefficients_not_retained"),
    ("signed_support_retained", "signed_support_not_retained"),
    ("graph_rosati_count_generated", "graph_rosati_count_not_generated"),
    ("control_death_generated", "control_death_not_generated"),
    ("controls_undefined_at_pushforward", "controls_not_undefined_at_pushforward"),
    ("dh_undefined_at_pushforward", "dh_not_undefined_at_pushforward"),
    ("epstein_undefined_at_pushforward", "epstein_not_undefined_at_pushforward"),
)

BANNED = (
    ("detached_boundary_exactness", "detached_boundary_exactness"),
    ("endpoint_degree_filter", "endpoint_degree_filter"),
    ("symbolic_composition_pushforward", "symbolic_composition_pushforward"),
    ("formal_adjoint_pushforward", "formal_adjoint_pushforward"),
    ("projection_quotient_or_retuning", "projection_quotient_or_retuning"),
    ("declared_pushforward_square", "declared_pushforward_square"),
    ("boundary_after_pushforward_filter", "boundary_after_pushforward_filter"),
    ("graph_count_pushforward_filter", "graph_count_pushforward_filter"),
    ("support_pushforward", "support_pushforward"),
    ("weighted_zero_pushforward", "weighted_zero_pushforward"),
    ("local_pushforward_stack", "local_pushforward_stack"),
    ("finite_pushforward_table", "finite_pushforward_table"),
    ("external_multiplier_degree", "external_multiplier_degree"),
    ("posthoc_gate_intersection", "posthoc_gate_intersection"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_pushforward_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_pushforward_naturality(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        multiplier_action_functor_actual=True,
        dd4_boundary_natural=True,
        endpoint_degree_maps_actual=True,
        boundary_endpoint_pushforward_actual=True,
        p1_pushforward_actual=True,
        p2_pushforward_actual=True,
        pushforward_generated_by_domain=True,
        p1_pushforward_natural=True,
        p2_pushforward_natural=True,
        product_pushforward_natural=True,
        boundary_pushforward_compatible=True,
        endpoint_pushforward_compatible=True,
        same_pushforward_types_transport_orbits=True,
        endpoint_rank_preserved=True,
        two_degree_maps_retained=True,
        coefficients_retained=True,
        signed_support_retained=True,
        graph_rosati_count_generated=True,
        control_death_generated=True,
        controls_undefined_at_pushforward=True,
        dh_undefined_at_pushforward=True,
        epstein_undefined_at_pushforward=True,
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
chi_C3F22 = convolve_chi(chi_C3, chi_F22)

T3_z = convolve_chi(z, chi_C3)
T9_z = convolve_chi(z, chi_C9)
T3_T3_z = convolve_chi(T3_z, chi_C3)
zF22 = convolve_chi(z, chi_F22)
T3_zF22 = convolve_chi(zF22, chi_C3)
T3_z_then_F22 = convolve_chi(T3_z, chi_F22)
z_C3F22 = convolve_chi(z, chi_C3F22)

rows = [
    pushforward_row("z", z, "identity"),
    pushforward_row("T3_z", T3_z, "C3"),
    pushforward_row("T3_T3_z", T3_T3_z, "C3_then_C3"),
    pushforward_row("T9_z", T9_z, "C9"),
    pushforward_row("zF22", zF22, "F22"),
    pushforward_row("T3_zF22", T3_zF22, "C3_after_F22"),
    pushforward_row("T3_z_then_F22", T3_z_then_F22, "F22_after_C3"),
    pushforward_row("z_C3F22", z_C3F22, "C3F22"),
]

base_pair = endpoint_degrees(z)
c3_degree = multiplier_degree(chi_C3)
c9_degree = multiplier_degree(chi_C9)
f22_degree = multiplier_degree(chi_F22)
c3f22_degree = multiplier_degree(chi_C3F22)


gate(
    "PFN1 boundary, endpoint, and multiplier data feed one pushforward square",
    {row["domain"] for row in rows} == {DOMAIN_ID}
    and {row["boundary"] for row in rows} == {BOUNDARY_ID}
    and {row["pushforward"] for row in rows} == {PUSHFORWARD_ID}
    and all(row["pushforward_defect"] == 0 for row in rows)
    and endpoint_degrees(T3_z) == scale_pair(base_pair, c3_degree) == (6, 6)
    and endpoint_degrees(T3_T3_z) == endpoint_degrees(T9_z)
    and endpoint_degrees(T9_z) == scale_pair(base_pair, c9_degree) == (18, 18)
    and endpoint_degrees(zF22) == scale_pair(base_pair, f22_degree) == (8, 8)
    and endpoint_degrees(T3_zF22)
    == endpoint_degrees(T3_z_then_F22)
    == endpoint_degrees(z_C3F22)
    == scale_pair(base_pair, c3f22_degree)
    == (24, 24),
    "rows=%s" % rows,
)


detached_boundary = live_source(
    boundary_endpoint_pushforward_actual=False,
    p1_pushforward_natural=False,
    p2_pushforward_natural=False,
    boundary_pushforward_compatible=False,
    endpoint_pushforward_compatible=False,
    detached_boundary_exactness=True,
    boundary_after_pushforward_filter=True,
    control_formable=True,
)

gate(
    "PFN2 detached boundary exactness does not commute with p1_* and p2_*",
    not accepts_pushforward_naturality(detached_boundary)
    and {
        "boundary_endpoint_pushforward_not_actual",
        "p1_pushforward_not_natural",
        "p2_pushforward_not_natural",
        "boundary_pushforward_not_compatible",
        "endpoint_pushforward_not_compatible",
        "detached_boundary_exactness",
        "boundary_after_pushforward_filter",
        "control_formable",
    }
    <= set(reasons(detached_boundary)),
    ",".join(reasons(detached_boundary)),
)


endpoint_filter = live_source(
    pushforward_generated_by_domain=False,
    p1_pushforward_actual=False,
    p2_pushforward_actual=False,
    endpoint_degree_filter=True,
    endpoint_pushforward_compatible=False,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "PFN3 endpoint-degree filters are not pushforward maps",
    all(row["p1_degree"] == row["p2_degree"] for row in rows)
    and not accepts_pushforward_naturality(endpoint_filter)
    and {
        "p1_pushforward_not_actual",
        "p2_pushforward_not_actual",
        "pushforward_not_generated_by_domain",
        "endpoint_pushforward_not_compatible",
        "endpoint_degree_filter",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(endpoint_filter)),
    ",".join(reasons(endpoint_filter)),
)


symbolic_formal = live_source(
    carrier_native=False,
    boundary_endpoint_pushforward_actual=False,
    product_pushforward_natural=False,
    symbolic_composition_pushforward=True,
    formal_adjoint_pushforward=True,
    declared_pushforward_square=True,
    control_formable=True,
    dh_formable=True,
)

gate(
    "PFN4 symbolic composition, adjoints, and declarations are substitutes",
    not accepts_pushforward_naturality(symbolic_formal)
    and {
        "not_carrier_native",
        "boundary_endpoint_pushforward_not_actual",
        "product_pushforward_not_natural",
        "symbolic_composition_pushforward",
        "formal_adjoint_pushforward",
        "declared_pushforward_square",
        "control_formable",
        "dh_formable",
    }
    <= set(reasons(symbolic_formal)),
    ",".join(reasons(symbolic_formal)),
)


retuned = live_source(
    p1_pushforward_natural=False,
    p2_pushforward_natural=False,
    endpoint_rank_preserved=False,
    two_degree_maps_retained=False,
    projection_quotient_or_retuning=True,
    graph_count_pushforward_filter=True,
    control_formable=True,
)

gate(
    "PFN5 projection quotients and local retunings change anchors",
    base_pair == (2, 2)
    and not accepts_pushforward_naturality(retuned)
    and {
        "p1_pushforward_not_natural",
        "p2_pushforward_not_natural",
        "endpoint_rank_not_preserved",
        "two_degree_maps_not_retained",
        "projection_quotient_or_retuning",
        "graph_count_pushforward_filter",
        "control_formable",
    }
    <= set(reasons(retuned)),
    ",".join(reasons(retuned)),
)


support_weighted = live_source(
    p1_pushforward_actual=False,
    p2_pushforward_actual=False,
    coefficients_retained=False,
    signed_support_retained=False,
    support_pushforward=True,
    weighted_zero_pushforward=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "PFN6 support and weighted-zero pushforwards lose signed degree data",
    all(row["weighted_mass"] == 0 for row in rows)
    and not accepts_pushforward_naturality(support_weighted)
    and {
        "p1_pushforward_not_actual",
        "p2_pushforward_not_actual",
        "coefficients_not_retained",
        "signed_support_not_retained",
        "support_pushforward",
        "weighted_zero_pushforward",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(support_weighted)),
    ",".join(reasons(support_weighted)),
)


local_table = live_source(
    carrier_native=False,
    same_pushforward_types_transport_orbits=False,
    product_pushforward_natural=False,
    local_pushforward_stack=True,
    finite_pushforward_table=True,
    external_multiplier_degree=True,
    control_formable=True,
)

gate(
    "PFN7 local pushforward stacks and finite tables split the square",
    len(rows) == 8
    and not accepts_pushforward_naturality(local_table)
    and {
        "not_carrier_native",
        "same_pushforward_does_not_type_transport_orbits",
        "product_pushforward_not_natural",
        "local_pushforward_stack",
        "finite_pushforward_table",
        "external_multiplier_degree",
        "control_formable",
    }
    <= set(reasons(local_table)),
    ",".join(reasons(local_table)),
)


declared = live_source(
    boundary_endpoint_pushforward_actual=False,
    p1_pushforward_actual=False,
    p2_pushforward_actual=False,
    required_edges=set(),
    declared_pushforward_square=True,
)

gate(
    "PFN8 declared pushforward squares without edges are rejected",
    not accepts_pushforward_naturality(declared)
    and {
        "boundary_endpoint_pushforward_not_actual",
        "p1_pushforward_not_actual",
        "p2_pushforward_not_actual",
        "required_pushforward_edges_missing",
        "declared_pushforward_square",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


missing_downstream = live_source(
    graph_rosati_count_generated=False,
    control_death_generated=False,
    required_edges=REQUIRED_EDGES
    - {
        ("pushforward_naturality", "graph"),
        ("graph", "rosati"),
        ("graph", "count_degree"),
        ("internal_effectivity_domain", "control_death"),
    },
)

gate(
    "PFN9 pushforward must still generate graph/Rosati/count and death",
    not accepts_pushforward_naturality(missing_downstream)
    and {
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_pushforward_edges_missing",
    }
    <= set(reasons(missing_downstream)),
    ",".join(reasons(missing_downstream)),
)


control_shadow = live_source(
    carrier_native=False,
    boundary_endpoint_pushforward_actual=False,
    controls_undefined_at_pushforward=False,
    dh_undefined_at_pushforward=False,
    epstein_undefined_at_pushforward=False,
    weighted_zero_pushforward=True,
    endpoint_degree_filter=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

live = live_source()
dead_sources = {
    "detached_boundary": detached_boundary,
    "endpoint_filter": endpoint_filter,
    "symbolic_formal": symbolic_formal,
    "retuned": retuned,
    "support_weighted": support_weighted,
    "local_table": local_table,
    "declared": declared,
    "missing_downstream": missing_downstream,
    "control_shadow": control_shadow,
}

gate(
    "PFN10 only carrier-native endpoint-boundary pushforward naturality passes",
    not accepts_pushforward_naturality(control_shadow)
    and {
        "not_carrier_native",
        "boundary_endpoint_pushforward_not_actual",
        "controls_not_undefined_at_pushforward",
        "dh_not_undefined_at_pushforward",
        "epstein_not_undefined_at_pushforward",
        "weighted_zero_pushforward",
        "endpoint_degree_filter",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(control_shadow))
    and accepts_pushforward_naturality(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_pushforward_naturality(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_pushforward_naturality(data) for data in dead_sources.values()),
        accepts_pushforward_naturality(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPFN1-PFN10 ALL PASS: multiplier pushforward naturality contract pinned")
print(
    "VERDICT: DD.4 boundary localization and endpoint degree maps must feed "
    "the same carrier-native p1_*,p2_* pushforward square, natural for the "
    "multiplier action. Detached boundary exactness, endpoint filters, "
    "symbolic composition, formal adjoints, projection retunings, support or "
    "weighted-zero pushforwards, finite tables, declared squares, and "
    "control/DH/Epstein shadows do not construct pushforward compatibility."
)
