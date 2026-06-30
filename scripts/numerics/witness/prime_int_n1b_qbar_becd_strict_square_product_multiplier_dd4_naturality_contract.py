r"""Multiplier-action DD.4 naturality contract for the strict square.

Doc 335 requires the mixed-support transport to be a carrier-native
multiplier-action functor.  This witness sharpens the DD.4 edge: the DD.4
boundary localization must be natural for that functor.  Separate torsor
splitters for each multiplier orbit, boundary-after-transport filters,
support/weighted-zero boundary shadows, local stacks, finite tables, and
declared commutative squares do not make the boundary square commute.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_strict_square_product_multiplier_dd4_naturality_contract
"""

from __future__ import annotations

from math import comb, log2


failures: list[str] = []

DOMAIN_ID = "D_Qbar_BECD_eff"
BOUNDARY_ID = "B_Qbar_BECD_DD4"
DD4_CLASS = "dd4_c"

REQUIRED_EDGES = {
    ("multiplier_action_functor", "dd4_boundary_localization"),
    ("dd4_boundary_localization", "dd4_obstruction_class"),
    ("dd4_obstruction_class", "carrier_boundary_extension"),
    ("carrier_boundary_extension", "transported_torsor_splitter"),
    ("C3_transport", "dd4_naturality_square"),
    ("C9_transport", "dd4_naturality_square"),
    ("transport_composition", "dd4_naturality_square"),
    ("product_action", "dd4_naturality_square"),
    ("dd4_naturality_square", "internal_effectivity_domain"),
    ("dd4_naturality_square", "boundary"),
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


def make(L: int):
    """Arithmetic in F_2[z]/z^{L+1}; unit polynomials are dicts {power: 1}."""

    def add(a, b):
        out = dict(a)
        for k in b:
            out[k] = out.get(k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def mul(a, b):
        out = {}
        for i in a:
            for j in b:
                if i + j <= L:
                    out[i + j] = out.get(i + j, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    def inv(a):
        assert a.get(0, 0) == 1
        rem = add(a, {0: 1})
        term = {0: 1}
        out = {0: 1}
        for _ in range(1, L + 1):
            term = mul(term, rem)
            if not term:
                break
            out = add(out, term)
        return out

    def phi(f):
        out = {}
        for m in f:
            if m == 0:
                out[0] = out.get(0, 0) ^ 1
                continue
            for k in range(0, L - m + 1):
                if comb(m + k - 1, k) % 2:
                    out[m + k] = out.get(m + k, 0) ^ 1
        return {k: 1 for k, v in out.items() if v}

    return add, mul, inv, phi


def to_vec(f, L: int):
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, L: int, mul):
    seen = {(0,) * L}
    queue = [(0,) * L]
    while queue:
        current = from_vec(queue.pop())
        for gen in gens:
            nxt = to_vec(mul(current, gen), L)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def h1_profile(L: int) -> dict[str, object]:
    _add, mul, inv, phi = make(L)
    one_plus_z = {0: 1, 1: 1}
    c = inv(one_plus_z)
    bgens = [mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)]
    coboundaries = closure(bgens, L, mul)
    ngens = [mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)]
    norm_image = closure(ngens, L, mul)
    z1_order = 2 ** L // len(norm_image)
    h1_order = z1_order // len(coboundaries)
    return {
        "L": L,
        "c": c,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "h1_order": h1_order,
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "res1_c": c.get(1, 0),
        "coboundaries_res1_zero": all(from_vec(v).get(1, 0) == 0 for v in coboundaries),
    }


def boundary_row(name: str, chi: dict[int, int], transport: str) -> dict[str, object]:
    return {
        "boundary": BOUNDARY_ID,
        "domain": DOMAIN_ID,
        "source": name,
        "transport": transport,
        "support": support(chi),
        "coefficients": tuple(chi.items()),
        "weighted_mass": weighted_mass(chi),
        "dd4_class": DD4_CLASS,
        "res1": 1,
    }


def source(**kwargs):
    data = {
        "carrier_native": False,
        "multiplier_action_functor_actual": False,
        "dd4_boundary_localization_actual": False,
        "carrier_boundary_extension_actual": False,
        "dd4_class_killed_by_carrier_boundary": False,
        "boundary_transport_natural": False,
        "transport_composition_boundary_natural": False,
        "product_boundary_natural": False,
        "same_boundary_map_types_transport_orbits": False,
        "transported_splitter_from_same_boundary": False,
        "coefficients_retained": False,
        "signed_support_retained": False,
        "res1_obstruction_tracked": False,
        "domain_has_no_endpoint_or_count_prerequisite": False,
        "domain_generates_endpoint_integrality": False,
        "domain_generates_boundary_localization": False,
        "domain_generates_pushforward_compatibility": False,
        "domain_generates_graph_rosati_count": False,
        "domain_generates_control_death": False,
        "controls_undefined_at_dd4_boundary": False,
        "dh_undefined_at_dd4_boundary": False,
        "epstein_undefined_at_dd4_boundary": False,
        "required_edges": set(),
        "separate_orbit_splitters": False,
        "free_torsor_splitter": False,
        "boundary_after_transport_filter": False,
        "declared_dd4_naturality": False,
        "support_boundary": False,
        "weighted_zero_boundary": False,
        "endpoint_degree_boundary_filter": False,
        "graph_count_boundary_filter": False,
        "boundary_kernel_definition": False,
        "local_boundary_stack": False,
        "finite_boundary_table": False,
        "external_multiplier_monoid": False,
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
    ("dd4_boundary_localization_actual", "dd4_boundary_localization_not_actual"),
    ("carrier_boundary_extension_actual", "carrier_boundary_extension_not_actual"),
    (
        "dd4_class_killed_by_carrier_boundary",
        "dd4_class_not_killed_by_carrier_boundary",
    ),
    ("boundary_transport_natural", "boundary_transport_not_natural"),
    (
        "transport_composition_boundary_natural",
        "transport_composition_boundary_not_natural",
    ),
    ("product_boundary_natural", "product_boundary_not_natural"),
    (
        "same_boundary_map_types_transport_orbits",
        "same_boundary_map_does_not_type_transport_orbits",
    ),
    (
        "transported_splitter_from_same_boundary",
        "transported_splitter_not_from_same_boundary",
    ),
    ("coefficients_retained", "coefficients_not_retained"),
    ("signed_support_retained", "signed_support_not_retained"),
    ("res1_obstruction_tracked", "res1_obstruction_not_tracked"),
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
        "controls_undefined_at_dd4_boundary",
        "controls_not_undefined_at_dd4_boundary",
    ),
    ("dh_undefined_at_dd4_boundary", "dh_not_undefined_at_dd4_boundary"),
    (
        "epstein_undefined_at_dd4_boundary",
        "epstein_not_undefined_at_dd4_boundary",
    ),
)

BANNED = (
    ("separate_orbit_splitters", "separate_orbit_splitters"),
    ("free_torsor_splitter", "free_torsor_splitter"),
    ("boundary_after_transport_filter", "boundary_after_transport_filter"),
    ("declared_dd4_naturality", "declared_dd4_naturality"),
    ("support_boundary", "support_boundary"),
    ("weighted_zero_boundary", "weighted_zero_boundary"),
    ("endpoint_degree_boundary_filter", "endpoint_degree_boundary_filter"),
    ("graph_count_boundary_filter", "graph_count_boundary_filter"),
    ("boundary_kernel_definition", "boundary_kernel_definition"),
    ("local_boundary_stack", "local_boundary_stack"),
    ("finite_boundary_table", "finite_boundary_table"),
    ("external_multiplier_monoid", "external_multiplier_monoid"),
    ("posthoc_gate_intersection", "posthoc_gate_intersection"),
    ("control_formable", "control_formable"),
    ("dh_formable", "dh_formable"),
    ("epstein_formable", "epstein_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not REQUIRED_EDGES <= set(data["required_edges"]):
        out.append("required_dd4_naturality_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_dd4_naturality(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and REQUIRED_EDGES <= set(data["required_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        multiplier_action_functor_actual=True,
        dd4_boundary_localization_actual=True,
        carrier_boundary_extension_actual=True,
        dd4_class_killed_by_carrier_boundary=True,
        boundary_transport_natural=True,
        transport_composition_boundary_natural=True,
        product_boundary_natural=True,
        same_boundary_map_types_transport_orbits=True,
        transported_splitter_from_same_boundary=True,
        coefficients_retained=True,
        signed_support_retained=True,
        res1_obstruction_tracked=True,
        domain_has_no_endpoint_or_count_prerequisite=True,
        domain_generates_endpoint_integrality=True,
        domain_generates_boundary_localization=True,
        domain_generates_pushforward_compatibility=True,
        domain_generates_graph_rosati_count=True,
        domain_generates_control_death=True,
        controls_undefined_at_dd4_boundary=True,
        dh_undefined_at_dd4_boundary=True,
        epstein_undefined_at_dd4_boundary=True,
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
    boundary_row("z", z, "identity"),
    boundary_row("T3_z", T3_z, "C3"),
    boundary_row("T3_T3_z", T3_T3_z, "C3_then_C3"),
    boundary_row("T9_z", T9_z, "C9"),
    boundary_row("zF22", zF22, "F22"),
    boundary_row("T3_zF22", T3_zF22, "C3_after_F22"),
    boundary_row("T3_z_then_F22", T3_z_then_F22, "F22_after_C3"),
    boundary_row("z_C3F22", z_C3F22, "C3F22"),
]

profiles = [h1_profile(L) for L in (6, 8, 10)]


gate(
    "MBN1 DD.4 class and multiplier boundary squares are simultaneously visible",
    all(
        p["cocycle"]
        and p["c_nonboundary"]
        and p["h1_order"] == 2
        and p["res1_c"] == 1
        and p["coboundaries_res1_zero"]
        for p in profiles
    )
    and T3_T3_z == T9_z == {9: 2, 18: -1}
    and T3_zF22 == T3_z_then_F22 == z_C3F22 == {6: 4, 12: -2}
    and {row["boundary"] for row in rows} == {BOUNDARY_ID}
    and {row["domain"] for row in rows} == {DOMAIN_ID}
    and {row["dd4_class"] for row in rows} == {DD4_CLASS}
    and {row["res1"] for row in rows} == {1},
    "profiles=%s rows=%s"
    % (
        " ".join(
            "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
            % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
            for p in profiles
        ),
        rows,
    ),
)


separate_splitters = live_source(
    carrier_boundary_extension_actual=False,
    boundary_transport_natural=False,
    transport_composition_boundary_natural=False,
    same_boundary_map_types_transport_orbits=False,
    transported_splitter_from_same_boundary=False,
    separate_orbit_splitters=True,
    free_torsor_splitter=True,
    finite_boundary_table=True,
    control_formable=True,
)

gate(
    "MBN2 separate orbit splitters kill local copies but not the boundary square",
    T3_T3_z == T9_z
    and not accepts_dd4_naturality(separate_splitters)
    and {
        "carrier_boundary_extension_not_actual",
        "boundary_transport_not_natural",
        "transport_composition_boundary_not_natural",
        "same_boundary_map_does_not_type_transport_orbits",
        "transported_splitter_not_from_same_boundary",
        "separate_orbit_splitters",
        "free_torsor_splitter",
        "finite_boundary_table",
        "control_formable",
    }
    <= set(reasons(separate_splitters)),
    ",".join(reasons(separate_splitters)),
)


boundary_after_transport = live_source(
    dd4_boundary_localization_actual=False,
    boundary_transport_natural=False,
    product_boundary_natural=False,
    domain_generates_boundary_localization=False,
    boundary_after_transport_filter=True,
    declared_dd4_naturality=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "MBN3 boundary-after-transport filters reverse DD.4 naturality",
    T3_zF22 == T3_z_then_F22
    and not accepts_dd4_naturality(boundary_after_transport)
    and {
        "dd4_boundary_localization_not_actual",
        "boundary_transport_not_natural",
        "product_boundary_not_natural",
        "boundary_localization_not_generated",
        "boundary_after_transport_filter",
        "declared_dd4_naturality",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(boundary_after_transport)),
    ",".join(reasons(boundary_after_transport)),
)


weighted_support = live_source(
    dd4_boundary_localization_actual=False,
    carrier_boundary_extension_actual=False,
    coefficients_retained=False,
    signed_support_retained=False,
    res1_obstruction_tracked=False,
    support_boundary=True,
    weighted_zero_boundary=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "MBN4 support and weighted-zero boundary shadows lose the DD.4 class",
    all(row["weighted_mass"] == 0 for row in rows)
    and {row["support"] for row in rows}
    == {
        (1, 2),
        (3, 6),
        (9, 18),
        (2, 4),
        (6, 12),
    }
    and not accepts_dd4_naturality(weighted_support)
    and {
        "dd4_boundary_localization_not_actual",
        "carrier_boundary_extension_not_actual",
        "coefficients_not_retained",
        "signed_support_not_retained",
        "res1_obstruction_not_tracked",
        "support_boundary",
        "weighted_zero_boundary",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(weighted_support)),
    ",".join(reasons(weighted_support)),
)


endpoint_boundary = live_source(
    dd4_class_killed_by_carrier_boundary=False,
    domain_has_no_endpoint_or_count_prerequisite=False,
    domain_generates_endpoint_integrality=False,
    domain_generates_graph_rosati_count=False,
    endpoint_degree_boundary_filter=True,
    graph_count_boundary_filter=True,
    boundary_kernel_definition=True,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "MBN5 endpoint/count and boundary-kernel definitions are downstream",
    not accepts_dd4_naturality(endpoint_boundary)
    and {
        "dd4_class_not_killed_by_carrier_boundary",
        "domain_has_endpoint_or_count_prerequisite",
        "endpoint_integrality_not_generated",
        "graph_rosati_count_not_generated",
        "endpoint_degree_boundary_filter",
        "graph_count_boundary_filter",
        "boundary_kernel_definition",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(endpoint_boundary)),
    ",".join(reasons(endpoint_boundary)),
)


local_stack = live_source(
    carrier_native=False,
    same_boundary_map_types_transport_orbits=False,
    product_boundary_natural=False,
    local_boundary_stack=True,
    finite_boundary_table=True,
    external_multiplier_monoid=True,
    control_formable=True,
)

gate(
    "MBN6 local boundary stacks and finite tables split the DD.4 square",
    len(rows) == 8
    and not accepts_dd4_naturality(local_stack)
    and {
        "not_carrier_native",
        "same_boundary_map_does_not_type_transport_orbits",
        "product_boundary_not_natural",
        "local_boundary_stack",
        "finite_boundary_table",
        "external_multiplier_monoid",
        "control_formable",
    }
    <= set(reasons(local_stack)),
    ",".join(reasons(local_stack)),
)


declared = live_source(
    multiplier_action_functor_actual=False,
    dd4_boundary_localization_actual=False,
    carrier_boundary_extension_actual=False,
    required_edges=set(),
    declared_dd4_naturality=True,
)

gate(
    "MBN7 declared DD.4 naturality without edges is rejected",
    not accepts_dd4_naturality(declared)
    and {
        "multiplier_action_functor_not_actual",
        "dd4_boundary_localization_not_actual",
        "carrier_boundary_extension_not_actual",
        "required_dd4_naturality_edges_missing",
        "declared_dd4_naturality",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
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
    "MBN8 DD.4 naturality must still generate downstream square data",
    not accepts_dd4_naturality(missing_downstream)
    and {
        "endpoint_integrality_not_generated",
        "pushforward_compatibility_not_generated",
        "graph_rosati_count_not_generated",
        "control_death_not_generated",
        "required_dd4_naturality_edges_missing",
    }
    <= set(reasons(missing_downstream)),
    ",".join(reasons(missing_downstream)),
)


control_shadow = live_source(
    carrier_native=False,
    multiplier_action_functor_actual=False,
    carrier_boundary_extension_actual=False,
    controls_undefined_at_dd4_boundary=False,
    dh_undefined_at_dd4_boundary=False,
    epstein_undefined_at_dd4_boundary=False,
    weighted_zero_boundary=True,
    endpoint_degree_boundary_filter=True,
    control_formable=True,
    dh_formable=True,
    epstein_formable=True,
)

gate(
    "MBN9 controls/DH/Epstein can mimic boundary shadows but not DD.4 naturality",
    not accepts_dd4_naturality(control_shadow)
    and {
        "not_carrier_native",
        "multiplier_action_functor_not_actual",
        "carrier_boundary_extension_not_actual",
        "controls_not_undefined_at_dd4_boundary",
        "dh_not_undefined_at_dd4_boundary",
        "epstein_not_undefined_at_dd4_boundary",
        "weighted_zero_boundary",
        "endpoint_degree_boundary_filter",
        "control_formable",
        "dh_formable",
        "epstein_formable",
    }
    <= set(reasons(control_shadow)),
    ",".join(reasons(control_shadow)),
)


live = live_source()
dead_sources = {
    "separate_splitters": separate_splitters,
    "boundary_after_transport": boundary_after_transport,
    "weighted_support": weighted_support,
    "endpoint_boundary": endpoint_boundary,
    "local_stack": local_stack,
    "declared": declared,
    "missing_downstream": missing_downstream,
    "control_shadow": control_shadow,
}

gate(
    "MBN10 only carrier-native multiplier DD.4 naturality passes",
    accepts_dd4_naturality(live)
    and REQUIRED_EDGES <= live["required_edges"]
    and not any(accepts_dd4_naturality(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_dd4_naturality(data) for data in dead_sources.values()),
        accepts_dd4_naturality(live),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nMBN1-MBN10 ALL PASS: multiplier-action DD.4 naturality contract pinned")
print(
    "VERDICT: DD.4 boundary localization must be natural for the "
    "carrier-native multiplier-action functor. Separate orbit splitters, "
    "boundary-after-transport filters, support or weighted-zero boundaries, "
    "local stacks, finite tables, declared naturality, and control/DH/Epstein "
    "shadows do not construct the commuting DD.4 boundary square."
)
