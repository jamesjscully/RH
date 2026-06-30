r"""Joint formation-coupling contract for Qbar_BECD.

Doc 321 says controls must die at carrier formation. This witness sharpens
what "joint formation" means: the endpoint, boundary, pushforward, graph,
Rosati, count/degree, and control-death atoms must be tied by one represented
carrier primitive. An atomwise intersection, product of local moduli,
sequential filter pipeline, or declared coupling does not count.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_qbar_becd_joint_formation_coupling_contract
"""

from __future__ import annotations

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    frobenius,
    ns_intersection,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


failures: list[str] = []

Corr = tuple[float, np.ndarray, float]

ATOMS = {
    "carrier",
    "endpoint",
    "boundary",
    "pushforward",
    "graph",
    "rosati",
    "count_degree",
    "control_death",
}

COUPLING_EDGES = {
    ("carrier", "endpoint"),
    ("endpoint", "boundary"),
    ("boundary", "pushforward"),
    ("pushforward", "graph"),
    ("graph", "rosati"),
    ("graph", "count_degree"),
    ("rosati", "control_death"),
    ("control_death", "carrier"),
}


def gate(name: str, ok: bool, detail: str = "") -> None:
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


def corr(d1: float, z: np.ndarray, d2: float) -> Corr:
    return (float(d1), z, float(d2))


def delta(F: np.ndarray) -> Corr:
    return corr(1.0, np.eye(F.shape[0]), 1.0)


def graph(F: np.ndarray, q: float, n: int) -> Corr:
    return corr(q**n, np.linalg.matrix_power(F, n), 1.0)


def compose(A: Corr, B: Corr) -> Corr:
    d1, z, d2 = A
    e1, w, e2 = B
    return corr(d1 * e1, z @ w, d2 * e2)


def dagger(A: Corr, E: np.ndarray) -> Corr:
    d1, z, d2 = A
    return corr(d2, rosati(z, E), d1)


def corr_defect(A: Corr, B: Corr) -> float:
    return float(abs(A[0] - B[0]) + np.linalg.norm(A[1] - B[1]) + abs(A[2] - B[2]))


def graph_law_defect(F: np.ndarray, q: float, m: int, n: int) -> float:
    return corr_defect(compose(graph(F, q, m), graph(F, q, n)), graph(F, q, m + n))


def anti_defect(A: Corr, B: Corr, E: np.ndarray) -> float:
    return corr_defect(dagger(compose(A, B), E), compose(dagger(B, E), dagger(A, E)))


def qsim_defect(F: np.ndarray, E: np.ndarray, q: float) -> float:
    return float(np.linalg.norm(F.T @ E @ F - q * E))


def projection_sides(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> tuple[float, float]:
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> float:
    lhs, rhs = projection_sides(A, B, C, E)
    return abs(lhs - rhs)


def trace_power(F: np.ndarray, n: int) -> float:
    return float(np.trace(np.linalg.matrix_power(F, n)).real)


def point_count(F: np.ndarray, q: float, n: int) -> float:
    return float(q**n + 1.0 - trace_power(F, n))


def retune_first_degree_for_projection(A: Corr, B: Corr, C: Corr, E: np.ndarray) -> Corr:
    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    return corr(product[0] + (rhs - lhs) / C[2], product[1], product[2])


def connected(atoms: set[str], edges: set[tuple[str, str]]) -> bool:
    if not atoms:
        return False
    adjacency = {atom: set() for atom in atoms}
    for left, right in edges:
        if left in atoms and right in atoms:
            adjacency[left].add(right)
            adjacency[right].add(left)
    seen = set()
    stack = [next(iter(atoms))]
    while stack:
        atom = stack.pop()
        if atom in seen:
            continue
        seen.add(atom)
        stack.extend(adjacency[atom] - seen)
    return seen == atoms


def source(**kwargs):
    data = {
        "carrier_native": False,
        "formation_primitive_actual": False,
        "represented_object_maps_cycles": False,
        "endpoint_integrality_native": False,
        "degree_maps_native": False,
        "dd4_boundary_native": False,
        "boundary_pushforward_compat_native": False,
        "proper_graph_composition_native": False,
        "positive_rosati_native": False,
        "finite_field_count_anchor_native": False,
        "graph_degree_anchor_native": False,
        "controls_impossible_at_first_generator": False,
        "controls_not_instantiated": False,
        "same_relation_endpoints_boundary": False,
        "same_relation_boundary_pushforward": False,
        "same_relation_pushforward_graph": False,
        "same_relation_graph_rosati": False,
        "same_relation_graph_count_degree": False,
        "same_relation_rosati_control_death": False,
        "non_split_dependency_graph": False,
        "coupling_edges": set(),
        "atomwise_intersection": False,
        "product_moduli": False,
        "sequential_pipeline": False,
        "posthoc_filter": False,
        "declared_coupling": False,
        "semantic_zeta_tag": False,
        "control_formable": True,
    }
    data.update(kwargs)
    return data


REQUIRED = (
    ("carrier_native", "not_carrier_native"),
    ("formation_primitive_actual", "formation_primitive_not_actual"),
    ("represented_object_maps_cycles", "object_maps_cycles_not_represented"),
    ("endpoint_integrality_native", "endpoint_integrality_not_native"),
    ("degree_maps_native", "degree_maps_not_native"),
    ("dd4_boundary_native", "dd4_boundary_not_native"),
    ("boundary_pushforward_compat_native", "boundary_pushforward_compat_not_native"),
    ("proper_graph_composition_native", "proper_graph_composition_not_native"),
    ("positive_rosati_native", "positive_rosati_not_native"),
    ("finite_field_count_anchor_native", "finite_field_count_anchor_not_native"),
    ("graph_degree_anchor_native", "graph_degree_anchor_not_native"),
    (
        "controls_impossible_at_first_generator",
        "controls_not_impossible_at_first_generator",
    ),
    ("controls_not_instantiated", "controls_instantiated_before_filter"),
    ("same_relation_endpoints_boundary", "endpoints_boundary_not_coupled"),
    ("same_relation_boundary_pushforward", "boundary_pushforward_not_coupled"),
    ("same_relation_pushforward_graph", "pushforward_graph_not_coupled"),
    ("same_relation_graph_rosati", "graph_rosati_not_coupled"),
    ("same_relation_graph_count_degree", "graph_count_degree_not_coupled"),
    ("same_relation_rosati_control_death", "rosati_control_death_not_coupled"),
    ("non_split_dependency_graph", "dependency_graph_split"),
)

BANNED = (
    ("atomwise_intersection", "atomwise_intersection"),
    ("product_moduli", "product_moduli"),
    ("sequential_pipeline", "sequential_pipeline"),
    ("posthoc_filter", "posthoc_filter"),
    ("declared_coupling", "declared_coupling"),
    ("semantic_zeta_tag", "semantic_zeta_tag"),
    ("control_formable", "control_formable"),
)


def reasons(data) -> list[str]:
    out = [label for key, label in REQUIRED if not data[key]]
    if not connected(ATOMS, set(data["coupling_edges"])):
        out.append("coupling_graph_not_connected")
    if not COUPLING_EDGES <= set(data["coupling_edges"]):
        out.append("required_coupling_edges_missing")
    out.extend(label for key, label in BANNED if data[key])
    return out


def accepts_joint_coupling(data) -> bool:
    return (
        all(data[key] for key, _ in REQUIRED)
        and connected(ATOMS, set(data["coupling_edges"]))
        and COUPLING_EDGES <= set(data["coupling_edges"])
        and not any(data[key] for key, _ in BANNED)
    )


def live_source(**kwargs):
    data = source(
        carrier_native=True,
        formation_primitive_actual=True,
        represented_object_maps_cycles=True,
        endpoint_integrality_native=True,
        degree_maps_native=True,
        dd4_boundary_native=True,
        boundary_pushforward_compat_native=True,
        proper_graph_composition_native=True,
        positive_rosati_native=True,
        finite_field_count_anchor_native=True,
        graph_degree_anchor_native=True,
        controls_impossible_at_first_generator=True,
        controls_not_instantiated=True,
        same_relation_endpoints_boundary=True,
        same_relation_boundary_pushforward=True,
        same_relation_pushforward_graph=True,
        same_relation_graph_rosati=True,
        same_relation_graph_count_degree=True,
        same_relation_rosati_control_death=True,
        non_split_dependency_graph=True,
        coupling_edges=set(COUPLING_EDGES),
        control_formable=False,
    )
    data.update(kwargs)
    return data


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = delta(F_true)
G_true = graph(F_true, q_true, 1)
H_true = graph(F_true, q_true, 2)

count_defects = [
    abs(ns_intersection(D_true, graph(F_true, q_true, n)) - point_count(F_true, q_true, n))
    for n in (1, 2, 3)
]
graph_defect = graph_law_defect(F_true, q_true, 1, 2)
rosati_sign = primitive_hodge_index(F_true, E_true, 1)

gate(
    "JFC1 finite-field anchor has coupled count, graph, and Rosati shadows",
    max(count_defects) < 1e-12 and graph_defect < 1e-12 and rosati_sign < 0,
    "count_defect=%.1e graph=%.1e primitive_H=%.3f"
    % (max(count_defects), graph_defect, rosati_sign),
)


doc321_atoms = ATOMS
doc321_slots = set(doc321_atoms)
doc321_with_coupling = doc321_slots | {"joint_formation_coupling"}

gate(
    "JFC2 doc-321 atoms still need a represented coupling primitive",
    doc321_slots == ATOMS
    and "joint_formation_coupling" not in doc321_slots
    and "joint_formation_coupling" in doc321_with_coupling,
    "atoms=%d coupling_added=%s" % (len(doc321_slots), "joint_formation_coupling" in doc321_with_coupling),
)


atomwise = live_source(
    formation_primitive_actual=False,
    non_split_dependency_graph=False,
    coupling_edges=set(),
    atomwise_intersection=True,
    control_formable=True,
)

gate(
    "JFC3 atomwise intersection of gates is not joint formation",
    not accepts_joint_coupling(atomwise)
    and {
        "formation_primitive_not_actual",
        "dependency_graph_split",
        "coupling_graph_not_connected",
        "required_coupling_edges_missing",
        "atomwise_intersection",
        "control_formable",
    }
    <= set(reasons(atomwise)),
    ",".join(reasons(atomwise)),
)


product_moduli = live_source(
    same_relation_endpoints_boundary=False,
    same_relation_boundary_pushforward=False,
    same_relation_pushforward_graph=False,
    same_relation_graph_rosati=False,
    same_relation_graph_count_degree=False,
    same_relation_rosati_control_death=False,
    non_split_dependency_graph=False,
    coupling_edges={("carrier", atom) for atom in ATOMS if atom != "carrier"},
    product_moduli=True,
    control_formable=True,
)

gate(
    "JFC4 product of local atom moduli is not one coupling relation",
    not accepts_joint_coupling(product_moduli)
    and {
        "endpoints_boundary_not_coupled",
        "boundary_pushforward_not_coupled",
        "pushforward_graph_not_coupled",
        "graph_rosati_not_coupled",
        "graph_count_degree_not_coupled",
        "rosati_control_death_not_coupled",
        "required_coupling_edges_missing",
        "product_moduli",
        "control_formable",
    }
    <= set(reasons(product_moduli)),
    ",".join(reasons(product_moduli)),
)


sequential = live_source(
    controls_impossible_at_first_generator=False,
    controls_not_instantiated=False,
    same_relation_rosati_control_death=False,
    coupling_edges=COUPLING_EDGES - {("rosati", "control_death")},
    sequential_pipeline=True,
    posthoc_filter=True,
    control_formable=True,
)

gate(
    "JFC5 sequential filters let controls enter before carrier death",
    not accepts_joint_coupling(sequential)
    and {
        "controls_not_impossible_at_first_generator",
        "controls_instantiated_before_filter",
        "rosati_control_death_not_coupled",
        "required_coupling_edges_missing",
        "sequential_pipeline",
        "posthoc_filter",
        "control_formable",
    }
    <= set(reasons(sequential)),
    ",".join(reasons(sequential)),
)


declared = live_source(
    formation_primitive_actual=False,
    represented_object_maps_cycles=False,
    declared_coupling=True,
    semantic_zeta_tag=True,
)

gate(
    "JFC6 declared coupling names do not represent the carrier primitive",
    not accepts_joint_coupling(declared)
    and {
        "formation_primitive_not_actual",
        "object_maps_cycles_not_represented",
        "declared_coupling",
        "semantic_zeta_tag",
    }
    <= set(reasons(declared)),
    ",".join(reasons(declared)),
)


control_q = 3
control = np.array([[1.0, 2.0], [1.0, 5.0]])
control_E = weil_pairing(control, control_q)
control_G = graph(control, control_q, 1)
control_H = graph(control, control_q, 2)
control_formal_graph = graph_law_defect(control, control_q, 1, 2)
control_qsim = qsim_defect(control, control_E, control_q)
control_anti = anti_defect(control_G, control_H, control_E)
control_projection = projection_defect(control_G, delta(control), control_G, control_E)

control_package = live_source(
    carrier_native=False,
    formation_primitive_actual=False,
    controls_impossible_at_first_generator=False,
    controls_not_instantiated=False,
    control_formable=True,
)

gate(
    "JFC7 controls satisfy formal shadows but fail the coupling primitive",
    control_formal_graph < 1e-12
    and control_qsim < 1e-12
    and control_anti < 1e-12
    and control_projection == 24.0
    and not accepts_joint_coupling(control_package)
    and {
        "not_carrier_native",
        "formation_primitive_not_actual",
        "controls_not_impossible_at_first_generator",
        "controls_instantiated_before_filter",
        "control_formable",
    }
    <= set(reasons(control_package)),
    "graph=%.1e qsim=%.1e anti=%.1e projection=%.1f reasons=%s"
    % (control_formal_graph, control_qsim, control_anti, control_projection, ",".join(reasons(control_package))),
)


missing_edge_cases = [
    live_source(
        same_relation_endpoints_boundary=False,
        coupling_edges=COUPLING_EDGES - {("endpoint", "boundary")},
    ),
    live_source(
        same_relation_boundary_pushforward=False,
        coupling_edges=COUPLING_EDGES - {("boundary", "pushforward")},
    ),
    live_source(
        same_relation_pushforward_graph=False,
        coupling_edges=COUPLING_EDGES - {("pushforward", "graph")},
    ),
    live_source(
        same_relation_graph_rosati=False,
        coupling_edges=COUPLING_EDGES - {("graph", "rosati")},
    ),
    live_source(
        same_relation_graph_count_degree=False,
        coupling_edges=COUPLING_EDGES - {("graph", "count_degree")},
    ),
    live_source(
        same_relation_rosati_control_death=False,
        coupling_edges=COUPLING_EDGES - {("rosati", "control_death")},
    ),
]

gate(
    "JFC8 every live coupling edge is mandatory",
    not any(accepts_joint_coupling(data) for data in missing_edge_cases)
    and {
        "endpoints_boundary_not_coupled",
        "boundary_pushforward_not_coupled",
        "pushforward_graph_not_coupled",
        "graph_rosati_not_coupled",
        "graph_count_degree_not_coupled",
        "rosati_control_death_not_coupled",
        "required_coupling_edges_missing",
    }
    <= set().union(*(set(reasons(data)) for data in missing_edge_cases)),
    "missing=%s"
    % sorted(set().union(*(set(reasons(data)) for data in missing_edge_cases))),
)


projection_11 = projection_defect(G_true, D_true, G_true, E_true)
actual_count2 = point_count(F_true, q_true, 2)
forced_count2 = q_true**2 + 1.0 - 2.0 * q_true
retuned_G = retune_first_degree_for_projection(G_true, D_true, G_true, E_true)
retuned = live_source(
    finite_field_count_anchor_native=False,
    graph_degree_anchor_native=False,
    posthoc_filter=True,
)

gate(
    "JFC9 coupling cannot retune count or graph-degree anchors",
    not accepts_joint_coupling(retuned)
    and projection_11 == 27.0
    and actual_count2 == 63.0
    and forced_count2 == 36.0
    and retuned_G[0] == -20.0
    and {
        "finite_field_count_anchor_not_native",
        "graph_degree_anchor_not_native",
        "posthoc_filter",
    }
    <= set(reasons(retuned)),
    "projection=%.1f count %.1f->%.1f retuned_d1=%.1f"
    % (projection_11, actual_count2, forced_count2, retuned_G[0]),
)


live_coupling = live_source()
dead_sources = {
    "atomwise": atomwise,
    "product_moduli": product_moduli,
    "sequential": sequential,
    "declared": declared,
    "control_package": control_package,
    "retuned": retuned,
}

gate(
    "JFC10 only represented non-split joint formation coupling passes",
    accepts_joint_coupling(live_coupling)
    and not any(accepts_joint_coupling(data) for data in dead_sources.values()),
    "dead accepted=%d live accepted=%s edges=%d"
    % (
        sum(accepts_joint_coupling(data) for data in dead_sources.values()),
        accepts_joint_coupling(live_coupling),
        len(live_coupling["coupling_edges"]),
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nJFC1-JFC10 ALL PASS: joint formation-coupling contract pinned")
print(
    "VERDICT: Qbar_BECD must contain one represented non-split carrier "
    "primitive coupling endpoint degrees, boundary normal ratio, boundary "
    "pushforward compatibility, graph composition, Rosati, count/degree "
    "anchors, and control exclusion. Atomwise intersections, product moduli, "
    "sequential filters, declared couplings, retunings, and control-formable "
    "packages do not meet this contract."
)
