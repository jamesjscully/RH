r"""CC product rep_NS graft no-go.

Doc 289 killed the product boundary+endpoint bundle as a full carrier.  This
witness tests the next repair:

    graft curve Pic data or the finite-field NS triple model onto the
    CC product boundary/endpoints as the square rep_NS.

The positive fact is that the finite-field NS model is the right visible
target.  The no-go is that grafting it is not represented square cycle
theory; even granting actual rep_NS/diagonal/graph tokens still leaves proper
pullback composition, projection, DD.4 boundary, carrier Rosati, and control
death unconstructed.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_product_repns_graft_no_go
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
    """Arithmetic in F_2[z]/z^(L+1); 1-units are dicts {power: 1}."""

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


product_endpoint_evidence = {
    "object_actual",
    "open_actual",
    "boundary_actual",
    "p1_map_actual",
    "p2_map_actual",
    "proper_pushforward_actual",
}
product_endpoint_slots = represented_slots(product_endpoint_evidence)

gate(
    "CRG1 product boundary endpoints still lack square rep_NS",
    product_endpoint_slots == {"carrier_object", "endpoint_maps"},
    "represented slots=%s" % ",".join(sorted(product_endpoint_slots)),
)


grafted_repns_evidence = product_endpoint_evidence | {
    "cycle_lattice_grafted",
    "intersection_form_grafted",
    "rep_functor_grafted",
    "diagonal_cycle_grafted",
    "frobenius_graph_cycle_grafted",
}
grafted_slots = represented_slots(grafted_repns_evidence)

gate(
    "CRG2 grafted finite-field/curve rep_NS is rejected as unrepresented",
    grafted_slots == {"carrier_object", "endpoint_maps"},
    "represented slots=%s" % ",".join(sorted(grafted_slots)),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
G1 = frobenius_graph(F_true, q_true, 1)
G2 = frobenius_graph(F_true, q_true, 2)
G3 = frobenius_graph(F_true, q_true, 3)
graph_law = compose(G1, G2)
count_ok = (
    ns_intersection(D_true, G1) == 7
    and ns_intersection(D_true, G2) == 63
    and ns_intersection(D_true, G3) == 364
)
graph_ok = graph_law[0] == G3[0] and np.array_equal(graph_law[1], G3[1]) and graph_law[2] == G3[2]

granted_repns_evidence = product_endpoint_evidence | {
    "cycle_lattice_actual",
    "intersection_form_actual",
    "rep_functor_actual",
    "diagonal_cycle_actual",
    "frobenius_graph_cycle_actual",
}
granted_repns_slots = represented_slots(granted_repns_evidence)

gate(
    "CRG3 even granted rep_NS visible anchors do not fill composition/projection",
    granted_repns_slots
    == {"carrier_object", "endpoint_maps", "integral_rep_NS", "diagonal", "frobenius_graph"}
    and count_ok
    and graph_ok,
    "slots=%s counts n=1,2,3 and graph law ok"
    % ",".join(sorted(granted_repns_slots)),
)


projection = projection_defect(G1, D_true, G1, E_true)
positive_sign = primitive_hodge_index(F_true, E_true, 1)

gate(
    "CRG4 componentwise graph law is not proper pullback projection",
    projection == 27.0
    and positive_sign < 0
    and "proper_composition" not in granted_repns_slots
    and "projection_formula" not in granted_repns_slots,
    "positive sign %.3f but semantic projection defect %.0f"
    % (positive_sign, projection),
)


pic_tensor_rank = 1
ns_visible_rank = 2 + F_true.shape[0] ** 2

gate(
    "CRG5 curve Pic tensor rank is not square NS triple rank",
    pic_tensor_rank == 1 and ns_visible_rank == 6,
    "Pic tensor rank=%d vs endpoint+End visible rank=%d"
    % (pic_tensor_rank, ns_visible_rank),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "CRG6 rep_NS graft does not kill DD.4",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles)
    and "dd4_boundary_killing" not in granted_repns_slots,
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)
control_granted_slots = represented_slots(granted_repns_evidence | {"control_repns_grafted"})

gate(
    "CRG7 rep_NS graft remains formable on positive controls",
    control_projection == 11.0
    and control_sign < 0
    and "control_death" not in control_granted_slots,
    "control projection_defect=%.0f sign=%.3f slots=%s"
    % (control_projection, control_sign, ",".join(sorted(control_granted_slots))),
)


full_blocker_plus_repns = granted_repns_evidence | {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
    "control_instantiation_impossible",
    "control_death_at_formation_proved",
}
full_slots = represented_slots(full_blocker_plus_repns)
full_missing = REQUIRED_SLOTS - full_slots

gate(
    "CRG8 product rep_NS graft still does not pass RCG",
    full_missing == {
        "proper_composition",
        "projection_formula",
        "rosati_duality",
        "primitive_positive_sign",
    },
    "slots=%s missing=%s" % (",".join(sorted(full_slots)), ",".join(sorted(full_missing))),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nCRG1-CRG8 ALL PASS: CC product rep_NS graft is not the square carrier")
print(
    "VERDICT: finite-field NS data is the right visible target, but grafting "
    "it onto product boundary/endpoints is not represented square cycle "
    "theory. Even granted rep_NS/diagonal/graph data still lacks proper "
    "pullback projection, carrier Rosati, DD.4 boundary, and control death."
)
