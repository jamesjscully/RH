r"""Missing-object frontier for the End(S^2/Z) construction arc.

This witness is constructive bookkeeping, not a no-go theorem.  It extracts
the first represented object that the current proof bank forces:

    Qbar_BECD = represented compactified square with boundary, endpoints,
    DD.4 killing, and formation-level control death.

That frontier is necessary and not sufficient.  After Qbar_BECD exists, the
second phase must construct rep_NS, proper correspondences, projection,
Rosati, primitive sign, diagonal, and graph data.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_missing_object_frontier
"""

from math import comb, log2

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    ns_intersection,
    primitive_hodge_index,
    rosati,
    weil_pairing,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


REQUIRED_SLOTS = {
    "carrier_object",
    "endpoint_maps",
    "integral_rep_NS",
    "diagonal",
    "frobenius_graph",
    "proper_composition",
    "projection_formula",
    "dd4_boundary_killing",
    "rosati_duality",
    "primitive_positive_sign",
    "control_death",
}

PHASE_A_SLOTS = {
    "carrier_object",
    "endpoint_maps",
    "dd4_boundary_killing",
    "control_death",
}

PHASE_B_SLOTS = REQUIRED_SLOTS - PHASE_A_SLOTS


def represented_slots(evidence):
    evidence = set(evidence)
    slots = set()

    if {"object_actual", "open_actual", "boundary_actual"} <= evidence:
        slots.add("carrier_object")
    if {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"} <= evidence:
        slots.add("endpoint_maps")
    if {"cycle_lattice_actual", "intersection_form_actual", "rep_functor_actual"} <= evidence:
        slots.add("integral_rep_NS")
    if {"diagonal_cycle_actual", "integral_rep_NS"} <= evidence | slots:
        slots.add("diagonal")
    if {"frobenius_graph_cycle_actual", "endpoint_maps", "integral_rep_NS"} <= evidence | slots:
        slots.add("frobenius_graph")
    if {"proper_pullbacks_actual", "fiber_product_composition_proved"} <= evidence:
        slots.add("proper_composition")
    if {
        "proper_pushforward_actual",
        "proper_pullbacks_actual",
        "projection_formula_proved",
        "intersection_form_actual",
    } <= evidence:
        slots.add("projection_formula")
    if {
        "boundary_map_actual",
        "localization_exact_actual",
        "dd4_class_mapped_to_zero",
        "self_dual_boundary_actual",
    } <= evidence:
        slots.add("dd4_boundary_killing")
    if {"duality_functor_actual", "duality_involutive_proved", "rosati_evaluation_proved"} <= evidence:
        slots.add("rosati_duality")
    if {"rosati_duality", "primitive_sign_proved", "frobenius_graph"} <= evidence | slots:
        slots.add("primitive_positive_sign")
    if {"control_instantiation_impossible", "control_death_at_formation_proved"} <= evidence:
        slots.add("control_death")

    return slots


def make(L):
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

    return mul, inv, phi


def to_vec(f, L):
    return tuple(f.get(k, 0) for k in range(1, L + 1))


def from_vec(v):
    out = {0: 1}
    for i, bit in enumerate(v, start=1):
        if bit:
            out[i] = 1
    return out


def closure(gens, L, mul):
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


def h1_profile(L):
    mul, inv, phi = make(L)
    c = inv({0: 1, 1: 1})
    boundary_gens = [
        mul({0: 1, k: 1}, inv(phi({0: 1, k: 1}))) for k in range(1, L + 1)
    ]
    norm_gens = [
        mul({0: 1, k: 1}, phi({0: 1, k: 1})) for k in range(1, L + 1)
    ]
    coboundaries = closure(boundary_gens, L, mul)
    norm_image = closure(norm_gens, L, mul)
    z1_order = 2**L // len(norm_image)
    return {
        "L": L,
        "cocycle": mul(c, phi(c)) == {0: 1},
        "c_nonboundary": to_vec(c, L) not in coboundaries,
        "res1_c": c.get(1, 0),
        "b_order": len(coboundaries),
        "z1_order": z1_order,
        "h1_order": z1_order // len(coboundaries),
    }


def compose(a, b):
    d1, z, d2 = a
    e1, w, e2 = b
    return d1 * e1, z @ w, d2 * e2


def dagger(a, E):
    d1, z, d2 = a
    return d2, rosati(z, E), d1


def projection_defect(A, B, C, E):
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(abs(lhs - rhs))


object_bundle = {"object_actual", "open_actual", "boundary_actual"}
endpoint_bundle = {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"}
boundary_bundle = {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
}
control_bundle = {"control_instantiation_impossible", "control_death_at_formation_proved"}

phase_a_frontier = object_bundle | endpoint_bundle | boundary_bundle | control_bundle
phase_b_square = {
    "cycle_lattice_actual",
    "intersection_form_actual",
    "rep_functor_actual",
    "diagonal_cycle_actual",
    "frobenius_graph_cycle_actual",
    "proper_pullbacks_actual",
    "fiber_product_composition_proved",
    "projection_formula_proved",
    "duality_functor_actual",
    "duality_involutive_proved",
    "rosati_evaluation_proved",
    "primitive_sign_proved",
}


routes = {
    "pfd_xbar": {
        "object_actual",
        "duality_functor_actual",
    },
    "connes_consani_scaling_site_cxc": {
        "object_actual",
        "open_actual",
        "boundary_actual",
        "duality_functor_actual",
        "duality_involutive_proved",
    },
    "condensed_metric_enrichment": {
        "analytic_site_actual",
        "metric_enrichment_actual",
        "positive_metric_declared",
    },
}

route_slots = {name: represented_slots(evidence) for name, evidence in routes.items()}
best_route = max(route_slots, key=lambda name: len(route_slots[name]))

gate(
    "MOF1 current route evidence selects only a starting line, not the object",
    route_slots["pfd_xbar"] == set()
    and route_slots["connes_consani_scaling_site_cxc"] == {"carrier_object"}
    and route_slots["condensed_metric_enrichment"] == set()
    and best_route == "connes_consani_scaling_site_cxc",
    "; ".join("%s:%s" % (name, ",".join(sorted(slots)) or "none") for name, slots in route_slots.items()),
)


phase_a_slots = represented_slots(phase_a_frontier)

gate(
    "MOF2 the first missing object is the represented boundary-endpoint-control bundle",
    phase_a_slots == PHASE_A_SLOTS,
    "Qbar_BECD slots=%s" % ",".join(sorted(phase_a_slots)),
)


minimality_checks = {
    "no_object": represented_slots(phase_a_frontier - object_bundle),
    "no_endpoint": represented_slots(phase_a_frontier - endpoint_bundle),
    "no_boundary": represented_slots(phase_a_frontier - boundary_bundle),
    "no_control": represented_slots(phase_a_frontier - control_bundle),
}

gate(
    "MOF3 every Phase-A bundle is necessary",
    "carrier_object" not in minimality_checks["no_object"]
    and "endpoint_maps" not in minimality_checks["no_endpoint"]
    and "dd4_boundary_killing" not in minimality_checks["no_boundary"]
    and "control_death" not in minimality_checks["no_control"],
    "; ".join("%s:%s" % (name, ",".join(sorted(slots)) or "none") for name, slots in minimality_checks.items()),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "MOF4 DD.4 forces an actual boundary/localization map in Phase A",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles)
    and "dd4_boundary_killing" not in represented_slots(phase_a_frontier - {"dd4_class_mapped_to_zero"})
    and "dd4_boundary_killing" in phase_a_slots,
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
same_total_a = (10, F_true, 1)
same_total_b = (7, F_true, 4)
same_total = same_total_a[0] + same_total_a[2] == same_total_b[0] + same_total_b[2]
same_diagonal = ns_intersection(D_true, same_total_a) == ns_intersection(D_true, same_total_b)
endpoints_differ = same_total_a[0] != same_total_b[0] and same_total_a[2] != same_total_b[2]

gate(
    "MOF5 endpoints must be represented pushforwards, not total-degree labels",
    same_total and same_diagonal and endpoints_differ and "endpoint_maps" in phase_a_slots,
    "(10,F,1) and (7,F,4) share total and Delta pairing but differ at endpoints",
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)

gate(
    "MOF6 control death must be formation failure in Phase A",
    control_sign < 0
    and control_projection == 11.0
    and "control_death" in phase_a_slots
    and "control_death" not in represented_slots(phase_a_frontier - control_bundle),
    "control sign %.3f and semantic projection defect %.0f; control_death requires formation obstruction"
    % (control_sign, control_projection),
)


remaining_after_phase_a = REQUIRED_SLOTS - phase_a_slots

gate(
    "MOF7 Qbar_BECD is necessary but not sufficient",
    remaining_after_phase_a == PHASE_B_SLOTS
    and not REQUIRED_SLOTS <= phase_a_slots,
    "remaining=%s" % ",".join(sorted(remaining_after_phase_a)),
)


full_slots = represented_slots(phase_a_frontier | phase_b_square)

gate(
    "MOF8 Phase B completion is exactly rep_NS/proper/projection/Rosati/graph",
    full_slots == REQUIRED_SLOTS
    and represented_slots(phase_b_square) == {
        "integral_rep_NS",
        "diagonal",
        "proper_composition",
        "rosati_duality",
    },
    "Phase A=%s; Phase A+B=%s"
    % (",".join(sorted(phase_a_slots)), ",".join(sorted(full_slots))),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nMOF1-MOF8 ALL PASS: missing-object frontier pinned")
print(
    "VERDICT: the first object to find is Qbar_BECD: actual Qbar/Q/dQ plus "
    "p1,p2 pushforwards, boundary localization killing DD.4, self-dual "
    "boundary/properness, and formation-level control death. It is necessary "
    "and not sufficient; Phase B must add rep_NS, proper pullbacks, "
    "projection, Rosati, primitive sign, diagonal, and graph data."
)
