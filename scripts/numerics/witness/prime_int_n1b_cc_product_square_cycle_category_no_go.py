r"""CC product square-cycle category closure no-go.

Doc 290 killed grafting finite-field rep_NS data onto CC product
boundary/endpoints.  This witness tests the next categorical repair:

    freely close the product+rep_NS visible data under a square-cycle
    category with pullbacks, projection cells, Rosati cells, DD.4 boundary
    cells, and control-death cells.

The positive fact is that an actual Corr^prop(Qbar) category is the right
target.  The no-go is that free/syntactic categorical closure represents no
new carrier evidence: projection defects, DD.4 cohomology, Rosati sign
semantics, boundary-direction choices, and positive controls all remain.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_product_square_cycle_category_no_go
"""

from math import comb, gcd, log2

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    frobenius,
    frobenius_graph,
    ns_intersection,
    offcircle_plant,
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
    """Only represented object/map/cycle/pullback/boundary evidence counts."""

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


def declared_category_slots(names):
    """Naive square-cycle-category checklist; accepts syntax by design."""

    names = set(names)
    slots = set()

    if {"Qbar", "Q", "dQ"} <= names:
        slots.add("carrier_object")
    if {"p1", "p2", "pushforward"} <= names:
        slots.add("endpoint_maps")
    if {"rep_NS", "intersection"} <= names:
        slots.add("integral_rep_NS")
    if "Delta" in names:
        slots.add("diagonal")
    if "Gamma_F" in names:
        slots.add("frobenius_graph")
    if {"Corr_prop", "pullbacks", "composition"} <= names:
        slots.add("proper_composition")
    if {"projection_cell", "push_pull"} <= names:
        slots.add("projection_formula")
    if {"dQ", "localization_cell", "dd4_zero_cell", "boundary_duality"} <= names:
        slots.add("dd4_boundary_killing")
    if {"Rosati_cell", "duality_cell"} <= names:
        slots.add("rosati_duality")
    if {"primitive_sign_cell", "Gamma_F"} <= names:
        slots.add("primitive_positive_sign")
    if "control_death_cell" in names:
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


def primitive_direction_count(radius):
    count = 0
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1:
                count += 1
    return count


product_repns_evidence = {
    "object_actual",
    "open_actual",
    "boundary_actual",
    "p1_map_actual",
    "p2_map_actual",
    "proper_pushforward_actual",
    "cycle_lattice_actual",
    "intersection_form_actual",
    "rep_functor_actual",
    "diagonal_cycle_actual",
    "frobenius_graph_cycle_actual",
}
product_repns_slots = represented_slots(product_repns_evidence)

gate(
    "PSC1 product+rep_NS visible data still lacks categorical carrier slots",
    product_repns_slots
    == {"carrier_object", "endpoint_maps", "integral_rep_NS", "diagonal", "frobenius_graph"},
    "represented slots=%s" % ",".join(sorted(product_repns_slots)),
)


free_category_names = {
    "Qbar",
    "Q",
    "dQ",
    "p1",
    "p2",
    "pushforward",
    "rep_NS",
    "intersection",
    "Delta",
    "Gamma_F",
    "Corr_prop",
    "pullbacks",
    "composition",
    "projection_cell",
    "push_pull",
    "localization_cell",
    "dd4_zero_cell",
    "boundary_duality",
    "Rosati_cell",
    "duality_cell",
    "primitive_sign_cell",
    "control_death_cell",
}
declared_slots = declared_category_slots(free_category_names)
represented_after_free_closure = represented_slots(
    product_repns_evidence
    | {
        "proper_pullbacks_free",
        "fiber_product_composition_declared",
        "projection_formula_declared",
        "boundary_map_formal",
        "localization_cell_formal",
        "dd4_zero_cell_formal",
        "duality_functor_formal",
        "primitive_sign_cell_formal",
        "control_death_cell_formal",
    }
)

gate(
    "PSC2 free square-cycle category declares all slots but represents no new slots",
    declared_slots == REQUIRED_SLOTS and represented_after_free_closure == product_repns_slots,
    "declared=%d represented=%s"
    % (len(declared_slots), ",".join(sorted(represented_after_free_closure))),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
G1 = frobenius_graph(F_true, q_true, 1)
G2 = frobenius_graph(F_true, q_true, 2)
G3 = frobenius_graph(F_true, q_true, 3)
count_ok = (
    ns_intersection(D_true, G1) == 7
    and ns_intersection(D_true, G2) == 63
    and ns_intersection(D_true, G3) == 364
)
graph_ok = compose(G1, G2)[0] == G3[0] and np.array_equal(compose(G1, G2)[1], G3[1])
semantic_projection = projection_defect(G1, D_true, G1, E_true)
formal_projection = 0.0

gate(
    "PSC3 projection cell does not prove carrier projection formula",
    count_ok
    and graph_ok
    and formal_projection == 0.0
    and semantic_projection == 27.0
    and "projection_formula" not in represented_after_free_closure,
    "formal defect %.0f, semantic defect %.0f"
    % (formal_projection, semantic_projection),
)


on_sign = primitive_hodge_index(F_true, E_true, 1)
F_off, E_off = offcircle_plant(q_true, 1.5)
off_sign = primitive_hodge_index(F_off, E_off, 1)
formal_sign_cell_accepts_offcircle = True

gate(
    "PSC4 Rosati/sign cells do not replace carrier Rosati theorem",
    on_sign < 0
    and off_sign > 0
    and formal_sign_cell_accepts_offcircle
    and "rosati_duality" not in represented_after_free_closure
    and "primitive_positive_sign" not in represented_after_free_closure,
    "on %.3f, off %.3f, formal sign cell unrepresented"
    % (on_sign, off_sign),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
formal_dd4_zero = True

gate(
    "PSC5 DD.4 zero cell does not map the actual class to zero",
    formal_dd4_zero
    and all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles)
    and "dd4_boundary_killing" not in represented_after_free_closure,
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


directions = primitive_direction_count(2)

gate(
    "PSC6 free category does not select the DD.4 boundary direction",
    directions == 16 and "dd4_boundary_killing" not in represented_after_free_closure,
    "primitive directions in [-2,2]^2=%d" % directions,
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)
control_slots = represented_slots(product_repns_evidence | {"control_free_category_closure"})
control_declared_slots = declared_category_slots(free_category_names | {"control"})

gate(
    "PSC7 positive controls admit the same free square-cycle closure",
    control_projection == 11.0
    and control_sign < 0
    and control_declared_slots == REQUIRED_SLOTS
    and control_slots == product_repns_slots
    and "control_death" not in control_slots,
    "control semantic projection_defect=%.0f sign=%.3f represented=%s"
    % (control_projection, control_sign, ",".join(sorted(control_slots))),
)


missing_after_free_closure = REQUIRED_SLOTS - represented_after_free_closure

gate(
    "PSC8 free square-cycle category still fails the represented-carrier gate",
    missing_after_free_closure
    == {
        "proper_composition",
        "projection_formula",
        "dd4_boundary_killing",
        "rosati_duality",
        "primitive_positive_sign",
        "control_death",
    },
    "missing=%s" % ",".join(sorted(missing_after_free_closure)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nPSC1-PSC8 ALL PASS: free square-cycle categorical closure is not the square carrier")
print(
    "VERDICT: the categorical route remains the right shape only when "
    "Corr^prop(Qbar), projection, Rosati, DD.4 boundary, and control death "
    "are represented by the carrier. Freely adjoining the category and its "
    "coherence cells is syntax; projection defects, DD.4, and controls remain."
)
