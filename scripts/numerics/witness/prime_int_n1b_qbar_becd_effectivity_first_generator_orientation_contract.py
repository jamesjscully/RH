r"""First-generator orientation contract for Qbar_BECD effectivity.

Docs 323-324 say the Euler/effectivity domain must be a represented internal
stratum of Qbar_BECD.  This witness sharpens the causal direction: the domain
has to be the first generator for endpoint integrality, boundary
localization, graph/composition, Rosati, count/degree anchors, and control
death.  A domain recovered later as a fiber of endpoint degrees, graph counts,
boundary kernels, Rosati positivity, or an intersection of already-required
gates is circular and control-formable.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_effectivity_first_generator_orientation_contract
"""

from __future__ import annotations


failures: list[str] = []

ATOMS = {
    "effectivity_domain",
    "endpoint",
    "boundary",
    "pushforward",
    "graph",
    "rosati",
    "count_degree",
    "control_death",
}
DOWNSTREAM = ATOMS - {"effectivity_domain"}
ALLOWED_DOMAIN_PREREQS = {"qbar_object_maps_cycles"}
REQUIRED_GENERATION_EDGES = {
    ("effectivity_domain", "endpoint"),
    ("effectivity_domain", "boundary"),
    ("effectivity_domain", "control_death"),
    ("endpoint", "pushforward"),
    ("boundary", "pushforward"),
    ("pushforward", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def valuation_depth(n: int, p: int) -> int | None:
    depth = 0
    while n > 1 and n % p == 0:
        n //= p
        depth += 1
    if n != 1:
        return None
    return depth


def powers(p: int, length: int) -> list[int]:
    return [p**k for k in range(length)]


def source(**kwargs):
    data = {
        "carrier_native": False,
        "represented_object_maps_cycles": False,
        "internal_effectivity_stratum_actual": False,
        "domain_has_no_downstream_prerequisites": False,
        "domain_generates_endpoint_integrality": False,
        "domain_generates_degree_maps": False,
        "domain_generates_boundary_localization": False,
        "domain_generates_pushforward_compatibility": False,
        "domain_generates_graph_composition": False,
        "domain_generates_rosati": False,
        "domain_generates_count_degree": False,
        "domain_generates_control_death": False,
        "controls_undefined_before_downstream_filters": False,
        "epstein_undefined_before_downstream_filters": False,
        "non_circular_first_generator": False,
        "domain_prerequisites": set(),
        "generation_edges": set(),
        "domain_from_endpoint_degree_fibers": False,
        "domain_from_graph_count_fibers": False,
        "domain_from_boundary_kernel": False,
        "domain_from_rosati_positive_filter": False,
        "domain_from_control_failure_filter": False,
        "posthoc_gate_intersection": False,
        "declared_first_generator": False,
        "retuned_downstream_fiber": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("represented_object_maps_cycles", "object_maps_cycles_not_represented"),
    ("internal_effectivity_stratum_actual", "internal_stratum_not_actual"),
    (
        "domain_has_no_downstream_prerequisites",
        "domain_has_downstream_prerequisites",
    ),
    ("domain_generates_endpoint_integrality", "endpoint_integrality_not_generated"),
    ("domain_generates_degree_maps", "degree_maps_not_generated"),
    (
        "domain_generates_boundary_localization",
        "boundary_localization_not_generated",
    ),
    (
        "domain_generates_pushforward_compatibility",
        "pushforward_compatibility_not_generated",
    ),
    ("domain_generates_graph_composition", "graph_composition_not_generated"),
    ("domain_generates_rosati", "rosati_not_generated"),
    ("domain_generates_count_degree", "count_degree_not_generated"),
    ("domain_generates_control_death", "control_death_not_generated"),
    (
        "controls_undefined_before_downstream_filters",
        "controls_not_undefined_before_downstream_filters",
    ),
    (
        "epstein_undefined_before_downstream_filters",
        "epstein_not_undefined_before_downstream_filters",
    ),
    ("non_circular_first_generator", "first_generator_circular"),
)

BANNED = (
    ("domain_from_endpoint_degree_fibers", "domain_from_endpoint_degree_fibers"),
    ("domain_from_graph_count_fibers", "domain_from_graph_count_fibers"),
    ("domain_from_boundary_kernel", "domain_from_boundary_kernel"),
    ("domain_from_rosati_positive_filter", "domain_from_rosati_positive_filter"),
    ("domain_from_control_failure_filter", "domain_from_control_failure_filter"),
    ("posthoc_gate_intersection", "posthoc_gate_intersection"),
    ("declared_first_generator", "declared_first_generator"),
    ("retuned_downstream_fiber", "retuned_downstream_fiber"),
    ("control_formable", "control_formable"),
)


def domain_prereqs_ok(data) -> bool:
    prereqs = set(data["domain_prerequisites"])
    return bool(prereqs) and prereqs <= ALLOWED_DOMAIN_PREREQS


def generation_edges_ok(data) -> bool:
    return REQUIRED_GENERATION_EDGES <= set(data["generation_edges"])


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    prereqs = set(data["domain_prerequisites"])
    if not domain_prereqs_ok(data):
        out.append("domain_prerequisites_not_qbar_only")
    if prereqs & DOWNSTREAM:
        out.append("domain_depends_on_downstream_atom")
    if not generation_edges_ok(data):
        out.append("required_generation_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_first_generator(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and domain_prereqs_ok(data)
        and generation_edges_ok(data)
        and not (set(data["domain_prerequisites"]) & DOWNSTREAM)
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        represented_object_maps_cycles=True,
        internal_effectivity_stratum_actual=True,
        domain_has_no_downstream_prerequisites=True,
        domain_generates_endpoint_integrality=True,
        domain_generates_degree_maps=True,
        domain_generates_boundary_localization=True,
        domain_generates_pushforward_compatibility=True,
        domain_generates_graph_composition=True,
        domain_generates_rosati=True,
        domain_generates_count_degree=True,
        domain_generates_control_death=True,
        controls_undefined_before_downstream_filters=True,
        epstein_undefined_before_downstream_filters=True,
        non_circular_first_generator=True,
        domain_prerequisites={"qbar_object_maps_cycles"},
        generation_edges=set(REQUIRED_GENERATION_EDGES),
        control_formable=False,
    )
    data.update(kwargs)
    return data


gate(
    "EFO1 accepted domain is first after Qbar object/map/cycle evidence",
    accepts_first_generator(live_source())
    and live_source()["domain_prerequisites"] == {"qbar_object_maps_cycles"}
    and REQUIRED_GENERATION_EDGES <= live_source()["generation_edges"],
    "prereqs=%s edges=%d"
    % (sorted(live_source()["domain_prerequisites"]), len(live_source()["generation_edges"])),
)


endpoint_rows = [
    {"p1_degree": 2**k, "p2_degree": 1, "depth": valuation_depth(2**k, 2)}
    for k in range(6)
]
degree_fiber = live_source(
    domain_has_no_downstream_prerequisites=False,
    domain_generates_endpoint_integrality=False,
    domain_generates_degree_maps=False,
    non_circular_first_generator=False,
    domain_prerequisites={"qbar_object_maps_cycles", "endpoint", "count_degree"},
    domain_from_endpoint_degree_fibers=True,
    control_formable=True,
)

gate(
    "EFO2 endpoint-degree fibers recover towers only circularly",
    [row["p1_degree"] for row in endpoint_rows] == powers(2, 6)
    and [row["depth"] for row in endpoint_rows] == [0, 1, 2, 3, 4, 5]
    and not accepts_first_generator(degree_fiber)
    and {
        "domain_has_downstream_prerequisites",
        "endpoint_integrality_not_generated",
        "degree_maps_not_generated",
        "first_generator_circular",
        "domain_depends_on_downstream_atom",
        "domain_from_endpoint_degree_fibers",
        "control_formable",
    }
    <= set(reasons(degree_fiber)),
    "rows=%s reasons=%s" % (endpoint_rows, ",".join(reasons(degree_fiber))),
)


graph_degree_rows = [
    {"n": k, "graph_degree": 2**k, "depth": valuation_depth(2**k, 2)}
    for k in range(1, 6)
]
count_fiber = live_source(
    domain_has_no_downstream_prerequisites=False,
    domain_generates_graph_composition=False,
    domain_generates_count_degree=False,
    non_circular_first_generator=False,
    domain_prerequisites={"qbar_object_maps_cycles", "graph", "count_degree"},
    domain_from_graph_count_fibers=True,
    retuned_downstream_fiber=True,
    control_formable=True,
)

gate(
    "EFO3 graph/count fibers are downstream, not the first generator",
    [row["graph_degree"] for row in graph_degree_rows] == [2, 4, 8, 16, 32]
    and not accepts_first_generator(count_fiber)
    and {
        "domain_has_downstream_prerequisites",
        "graph_composition_not_generated",
        "count_degree_not_generated",
        "first_generator_circular",
        "domain_depends_on_downstream_atom",
        "domain_from_graph_count_fibers",
        "retuned_downstream_fiber",
        "control_formable",
    }
    <= set(reasons(count_fiber)),
    "rows=%s reasons=%s" % (graph_degree_rows, ",".join(reasons(count_fiber))),
)


boundary_kernel = live_source(
    domain_has_no_downstream_prerequisites=False,
    domain_generates_boundary_localization=False,
    domain_generates_pushforward_compatibility=False,
    non_circular_first_generator=False,
    domain_prerequisites={"qbar_object_maps_cycles", "boundary", "pushforward"},
    domain_from_boundary_kernel=True,
    control_formable=True,
)

gate(
    "EFO4 boundary-kernel domains use the DD.4 map too late",
    not accepts_first_generator(boundary_kernel)
    and {
        "domain_has_downstream_prerequisites",
        "boundary_localization_not_generated",
        "pushforward_compatibility_not_generated",
        "first_generator_circular",
        "domain_depends_on_downstream_atom",
        "domain_from_boundary_kernel",
        "control_formable",
    }
    <= set(reasons(boundary_kernel)),
    ",".join(reasons(boundary_kernel)),
)


rosati_filter = live_source(
    domain_has_no_downstream_prerequisites=False,
    domain_generates_rosati=False,
    domain_generates_control_death=False,
    controls_undefined_before_downstream_filters=False,
    epstein_undefined_before_downstream_filters=False,
    non_circular_first_generator=False,
    domain_prerequisites={"qbar_object_maps_cycles", "rosati", "control_death"},
    domain_from_rosati_positive_filter=True,
    domain_from_control_failure_filter=True,
    control_formable=True,
)

gate(
    "EFO5 Rosati/control filters cannot define the first domain",
    not accepts_first_generator(rosati_filter)
    and {
        "domain_has_downstream_prerequisites",
        "rosati_not_generated",
        "control_death_not_generated",
        "controls_not_undefined_before_downstream_filters",
        "epstein_not_undefined_before_downstream_filters",
        "first_generator_circular",
        "domain_depends_on_downstream_atom",
        "domain_from_rosati_positive_filter",
        "domain_from_control_failure_filter",
        "control_formable",
    }
    <= set(reasons(rosati_filter)),
    ",".join(reasons(rosati_filter)),
)


intersection_domain = live_source(
    domain_has_no_downstream_prerequisites=False,
    non_circular_first_generator=False,
    domain_prerequisites={"qbar_object_maps_cycles"} | DOWNSTREAM,
    posthoc_gate_intersection=True,
    control_formable=True,
)

gate(
    "EFO6 intersection of all gates is post-hoc, not first generation",
    not accepts_first_generator(intersection_domain)
    and {
        "domain_has_downstream_prerequisites",
        "first_generator_circular",
        "domain_depends_on_downstream_atom",
        "posthoc_gate_intersection",
        "control_formable",
    }
    <= set(reasons(intersection_domain)),
    ",".join(reasons(intersection_domain)),
)


control_degree_rows = [
    {"control_dim": dim, "fake_degree": 2**k, "depth": k}
    for k, dim in enumerate((2, 4, 8, 16))
]
control_fiber = live_source(
    carrier_native=False,
    represented_object_maps_cycles=False,
    internal_effectivity_stratum_actual=False,
    domain_has_no_downstream_prerequisites=False,
    controls_undefined_before_downstream_filters=False,
    non_circular_first_generator=False,
    domain_prerequisites={"endpoint", "graph", "count_degree"},
    domain_from_endpoint_degree_fibers=True,
    domain_from_graph_count_fibers=True,
    control_formable=True,
)

gate(
    "EFO7 controls can mimic downstream degree/count fibers",
    [row["fake_degree"] for row in control_degree_rows] == [1, 2, 4, 8]
    and not accepts_first_generator(control_fiber)
    and {
        "not_carrier_native",
        "object_maps_cycles_not_represented",
        "internal_stratum_not_actual",
        "controls_not_undefined_before_downstream_filters",
        "domain_depends_on_downstream_atom",
        "domain_from_endpoint_degree_fibers",
        "domain_from_graph_count_fibers",
        "control_formable",
    }
    <= set(reasons(control_fiber)),
    "rows=%s reasons=%s" % (control_degree_rows, ",".join(reasons(control_fiber))),
)


declared_root = live_source(
    represented_object_maps_cycles=False,
    internal_effectivity_stratum_actual=False,
    domain_prerequisites=set(),
    generation_edges=set(),
    declared_first_generator=True,
)

gate(
    "EFO8 declared root status is not represented first generation",
    not accepts_first_generator(declared_root)
    and {
        "object_maps_cycles_not_represented",
        "internal_stratum_not_actual",
        "domain_prerequisites_not_qbar_only",
        "required_generation_edges_missing",
        "declared_first_generator",
    }
    <= set(reasons(declared_root)),
    ",".join(reasons(declared_root)),
)


missing_endpoint_edge = live_source(
    domain_generates_endpoint_integrality=False,
    generation_edges=REQUIRED_GENERATION_EDGES
    - {("effectivity_domain", "endpoint")},
)

gate(
    "EFO9 first generator must actually generate endpoint integrality",
    not accepts_first_generator(missing_endpoint_edge)
    and {
        "endpoint_integrality_not_generated",
        "required_generation_edges_missing",
    }
    <= set(reasons(missing_endpoint_edge)),
    ",".join(reasons(missing_endpoint_edge)),
)


dead_sources = {
    "degree_fiber": degree_fiber,
    "count_fiber": count_fiber,
    "boundary_kernel": boundary_kernel,
    "rosati_filter": rosati_filter,
    "intersection_domain": intersection_domain,
    "control_fiber": control_fiber,
    "declared_root": declared_root,
    "missing_endpoint_edge": missing_endpoint_edge,
}

gate(
    "EFO10 only non-circular effectivity first generation passes",
    accepts_first_generator(live_source())
    and not any(accepts_first_generator(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s"
    % (
        sum(accepts_first_generator(data) for data in dead_sources.values()),
        accepts_first_generator(live_source()),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nEFO1-EFO10 ALL PASS: effectivity first-generator orientation contract pinned")
print(
    "VERDICT: Qbar_BECD's internal effectivity domain must be the first "
    "generator after represented object/map/cycle evidence. Domains recovered "
    "from endpoint-degree fibers, graph/count fibers, boundary kernels, "
    "Rosati/control filters, or post-hoc gate intersections are circular and "
    "remain formable on controls."
)
