r"""CC product square-cycle moduli/classifying stack no-go.

Doc 294 killed hyperdescent/homotopy-coherent descent of local square-cycle
syntax.  This witness tests the next categorical repair:

    form a moduli/classifying stack of square-carrier packages and use its
    tautological universal package as the missing carrier.

The positive fact is that a real carrier may have a moduli interpretation
after it exists.  The no-go is that classifying packages is not constructing
Qbar.  The tautological object carries declared structure by definition, while
the represented-carrier gate still sees no new global Qbar maps, pullbacks,
boundary sequence, Rosati theorem, or control-formation obstruction.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_product_square_cycle_moduli_stack_no_go
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


def moduli_tautological_slots(markers):
    """Slots a naive classifying stack would give the universal object."""

    markers = set(markers)
    slots = set()

    if {"moduli_stack", "universal_Qbar", "universal_Q", "universal_dQ"} <= markers:
        slots.add("carrier_object")
    if {"universal_p1", "universal_p2", "universal_pushforward"} <= markers:
        slots.add("endpoint_maps")
    if {"universal_rep_NS", "universal_intersection"} <= markers:
        slots.add("integral_rep_NS")
    if "universal_Delta" in markers:
        slots.add("diagonal")
    if "universal_Gamma_F" in markers:
        slots.add("frobenius_graph")
    if {"universal_pullbacks", "universal_composition"} <= markers:
        slots.add("proper_composition")
    if {"universal_projection", "universal_push_pull"} <= markers:
        slots.add("projection_formula")
    if {"universal_localization", "universal_dd4_zero", "universal_boundary_duality"} <= markers:
        slots.add("dd4_boundary_killing")
    if {"universal_rosati", "universal_duality"} <= markers:
        slots.add("rosati_duality")
    if {"universal_primitive_sign", "universal_Gamma_F"} <= markers:
        slots.add("primitive_positive_sign")
    if "universal_control_death" in markers:
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


def projection_sides(A, B, C, E):
    lhs = ns_intersection(compose(A, B), C)
    rhs = ns_intersection(B, compose(dagger(A, E), C))
    return float(lhs), float(rhs)


def projection_defect(A, B, C, E):
    lhs, rhs = projection_sides(A, B, C, E)
    return float(abs(lhs - rhs))


def retune_first_degree_for_projection(A, B, C, E):
    product = compose(A, B)
    lhs, rhs = projection_sides(A, B, C, E)
    return product[0] + (rhs - lhs) / C[2], product[1], product[2]


def corr_defect(a, b):
    return abs(a[0] - b[0]) + np.linalg.norm(a[1] - b[1]) + abs(a[2] - b[2])


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
    "MDS1 product+rep_NS visible data has only five represented slots",
    product_repns_slots
    == {"carrier_object", "endpoint_maps", "integral_rep_NS", "diagonal", "frobenius_graph"},
    "represented slots=%s" % ",".join(sorted(product_repns_slots)),
)


moduli_markers = {
    "moduli_stack",
    "universal_Qbar",
    "universal_Q",
    "universal_dQ",
    "universal_p1",
    "universal_p2",
    "universal_pushforward",
    "universal_rep_NS",
    "universal_intersection",
    "universal_Delta",
    "universal_Gamma_F",
    "universal_pullbacks",
    "universal_composition",
    "universal_projection",
    "universal_push_pull",
    "universal_localization",
    "universal_dd4_zero",
    "universal_boundary_duality",
    "universal_rosati",
    "universal_duality",
    "universal_primitive_sign",
    "universal_control_death",
}
tautological_slots = moduli_tautological_slots(moduli_markers)
represented_after_moduli = represented_slots(
    product_repns_evidence
    | {
        "tautological_pullbacks_only",
        "tautological_projection_only",
        "tautological_localization_only",
        "tautological_rosati_only",
        "tautological_control_death_only",
    }
)

gate(
    "MDS2 moduli tautological package declares all slots but represents no new Qbar evidence",
    tautological_slots == REQUIRED_SLOTS and represented_after_moduli == product_repns_slots,
    "tautological=%d represented=%s"
    % (len(tautological_slots), ",".join(sorted(represented_after_moduli))),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
G1 = frobenius_graph(F_true, q_true, 1)
G2 = frobenius_graph(F_true, q_true, 2)
G3 = frobenius_graph(F_true, q_true, 3)
semantic_projection = projection_defect(G1, D_true, G1, E_true)
tautological_projection = 0.0

gate(
    "MDS3 universal projection relation does not prove global projection",
    ns_intersection(D_true, G1) == 7
    and corr_defect(compose(G1, G2), G3) < 1e-12
    and tautological_projection == 0.0
    and semantic_projection == 27.0,
    "tautological defect %.0f, semantic defect %.0f"
    % (tautological_projection, semantic_projection),
)


retuned = retune_first_degree_for_projection(G1, D_true, G1, E_true)

gate(
    "MDS4 realizing universal relation repeats NS retuning damage",
    retuned[0] == -20.0
    and corr_defect(retuned, G1) == 27.0
    and ns_intersection(D_true, G2) == 63.0,
    "retuned d1 %.0f vs graph d1 %.0f; count2 %.0f"
    % (retuned[0], G1[0], ns_intersection(D_true, G2)),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "MDS5 universal DD.4 zero object does not kill the actual class",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles)
    and "dd4_boundary_killing" not in represented_after_moduli,
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


directions = primitive_direction_count(2)
rosati_branches = 2
moduli_branches = directions * rosati_branches
on_sign = primitive_hodge_index(F_true, E_true, 1)
F_off, E_off = offcircle_plant(q_true, 1.5)
off_sign = primitive_hodge_index(F_off, E_off, 1)

gate(
    "MDS6 moduli package parameterizes choices rather than selecting carrier data",
    directions == 16
    and rosati_branches == 2
    and moduli_branches == 32
    and on_sign < 0
    and off_sign > 0
    and "rosati_duality" not in represented_after_moduli,
    "directions=%d rosati branches=%d moduli branches=%d on %.3f off %.3f"
    % (directions, rosati_branches, moduli_branches, on_sign, off_sign),
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)
control_slots = represented_slots(product_repns_evidence | {"control_moduli_point"})
control_tautological_slots = moduli_tautological_slots(moduli_markers | {"control"})

gate(
    "MDS7 positive controls define points of the same moduli stack",
    control_projection == 11.0
    and control_sign < 0
    and control_tautological_slots == REQUIRED_SLOTS
    and control_slots == product_repns_slots
    and "control_death" not in control_slots,
    "control projection_defect=%.0f sign=%.3f represented=%s"
    % (control_projection, control_sign, ",".join(sorted(control_slots))),
)


missing_after_moduli = REQUIRED_SLOTS - represented_after_moduli

gate(
    "MDS8 moduli/classifying stack wrapper still fails RCG",
    missing_after_moduli
    == {
        "proper_composition",
        "projection_formula",
        "dd4_boundary_killing",
        "rosati_duality",
        "primitive_positive_sign",
        "control_death",
    },
    "missing=%s" % ",".join(sorted(missing_after_moduli)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nMDS1-MDS8 ALL PASS: moduli/classifying stack is not the square carrier")
print(
    "VERDICT: classifying square-carrier packages and taking the "
    "tautological package does not construct represented Qbar geometry. "
    "Projection, DD.4 boundary, Rosati, boundary direction, and control "
    "death remain carrier theorems, not moduli labels."
)
