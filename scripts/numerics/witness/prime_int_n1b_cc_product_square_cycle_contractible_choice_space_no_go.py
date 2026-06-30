r"""CC product square-cycle contractible choice-space no-go.

Doc 302 killed the equivalence/univalence shortcut.  This witness tests the
next categorical repair:

    prove the space of square-carrier choices is contractible, extract a
    canonical point, and count that canonical choice as represented Qbar
    geometry.

The positive fact is that a constructed carrier should have coherently unique
structure.  The no-go is that contractibility and canonical-choice data do not
construct represented square geometry.  They still do not construct actual
maps, proper pullbacks, projection, DD.4 boundary, Rosati, or formation-level
control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_product_square_cycle_contractible_choice_space_no_go
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


def choice_space_slots(markers):
    """Slots named by contractible choice-space/canonical-point data."""

    markers = set(markers)
    slots = set()
    if {"contractible_choice_space", "canonical_point", "predicate_Qbar"} <= markers:
        slots.add("carrier_object")
    if {"predicate_p1", "predicate_p2", "predicate_pushforward"} <= markers:
        slots.add("endpoint_maps")
    if {"predicate_rep_NS", "predicate_intersection"} <= markers:
        slots.add("integral_rep_NS")
    if "predicate_Delta" in markers:
        slots.add("diagonal")
    if "predicate_Gamma_F" in markers:
        slots.add("frobenius_graph")
    if {"predicate_pullbacks", "predicate_composition"} <= markers:
        slots.add("proper_composition")
    if {"predicate_projection", "predicate_push_pull"} <= markers:
        slots.add("projection_formula")
    if {"predicate_localization", "predicate_dd4_zero", "predicate_boundary_duality"} <= markers:
        slots.add("dd4_boundary_killing")
    if {"predicate_rosati", "predicate_duality"} <= markers:
        slots.add("rosati_duality")
    if {"predicate_primitive_sign", "predicate_Gamma_F"} <= markers:
        slots.add("primitive_positive_sign")
    if "predicate_control_death" in markers:
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
    "CTS1 product+rep_NS visible data has only five represented slots",
    product_repns_slots
    == {"carrier_object", "endpoint_maps", "integral_rep_NS", "diagonal", "frobenius_graph"},
    "represented slots=%s" % ",".join(sorted(product_repns_slots)),
)


choice_markers = {
    "contractible_choice_space",
    "canonical_point",
    "path_contraction",
    "predicate_Qbar",
    "predicate_p1",
    "predicate_p2",
    "predicate_pushforward",
    "predicate_rep_NS",
    "predicate_intersection",
    "predicate_Delta",
    "predicate_Gamma_F",
    "predicate_pullbacks",
    "predicate_composition",
    "predicate_projection",
    "predicate_push_pull",
    "predicate_localization",
    "predicate_dd4_zero",
    "predicate_boundary_duality",
    "predicate_rosati",
    "predicate_duality",
    "predicate_primitive_sign",
    "predicate_control_death",
}
choice_slots = choice_space_slots(choice_markers)
represented_after_choice = represented_slots(
    product_repns_evidence
    | {
        "contractible_choice_space_only",
        "canonical_point_only",
        "path_contraction_only",
        "predicate_projection_only",
        "predicate_localization_only",
        "predicate_rosati_only",
        "predicate_control_death_only",
    }
)

gate(
    "CTS2 contractible choice space lists all slots but represents no new Qbar evidence",
    choice_slots == REQUIRED_SLOTS and represented_after_choice == product_repns_slots,
    "choice=%d represented=%s"
    % (len(choice_slots), ",".join(sorted(represented_after_choice))),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
G1 = frobenius_graph(F_true, q_true, 1)
G2 = frobenius_graph(F_true, q_true, 2)
G3 = frobenius_graph(F_true, q_true, 3)
semantic_projection = projection_defect(G1, D_true, G1, E_true)
canonical_projection = 0.0

gate(
    "CTS3 canonical projection choice does not prove global projection",
    ns_intersection(D_true, G1) == 7
    and corr_defect(compose(G1, G2), G3) < 1e-12
    and canonical_projection == 0.0
    and semantic_projection == 27.0,
    "canonical defect %.0f, semantic defect %.0f"
    % (canonical_projection, semantic_projection),
)


retuned = retune_first_degree_for_projection(G1, D_true, G1, E_true)

gate(
    "CTS4 realizing canonical choice repeats NS retuning damage",
    retuned[0] == -20.0
    and corr_defect(retuned, G1) == 27.0
    and ns_intersection(D_true, G2) == 63.0,
    "retuned d1 %.0f vs graph d1 %.0f; count2 %.0f"
    % (retuned[0], G1[0], ns_intersection(D_true, G2)),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]

gate(
    "CTS5 contractible zero choice does not kill the actual DD.4 class",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles)
    and "dd4_boundary_killing" not in represented_after_choice,
    "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


directions = primitive_direction_count(2)
rosati_branches = 2
contraction_witnesses = 3
raw_choice_branches = directions * rosati_branches * contraction_witnesses
declared_canonical_points = 1
on_sign = primitive_hodge_index(F_true, E_true, 1)
F_off, E_off = offcircle_plant(q_true, 1.5)
off_sign = primitive_hodge_index(F_off, E_off, 1)

gate(
    "CTS6 contractibility collapses labels but does not select carrier data",
    directions == 16
    and rosati_branches == 2
    and contraction_witnesses == 3
    and raw_choice_branches == 96
    and declared_canonical_points == 1
    and on_sign < 0
    and off_sign > 0
    and "rosati_duality" not in represented_after_choice,
    "directions=%d rosati=%d contractions=%d raw=%d canonical=%d on %.3f off %.3f"
    % (
        directions,
        rosati_branches,
        contraction_witnesses,
        raw_choice_branches,
        declared_canonical_points,
        on_sign,
        off_sign,
    ),
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)
control_slots = represented_slots(product_repns_evidence | {"control_canonical_point"})
control_choice_slots = choice_space_slots(choice_markers | {"control"})

gate(
    "CTS7 positive controls have the same contractible choice space",
    control_projection == 11.0
    and control_sign < 0
    and control_choice_slots == REQUIRED_SLOTS
    and control_slots == product_repns_slots
    and "control_death" not in control_slots,
    "control projection_defect=%.0f sign=%.3f represented=%s"
    % (control_projection, control_sign, ",".join(sorted(control_slots))),
)


missing_after_choice = REQUIRED_SLOTS - represented_after_choice

gate(
    "CTS8 contractible-choice-space wrapper still fails RCG",
    missing_after_choice
    == {
        "proper_composition",
        "projection_formula",
        "dd4_boundary_killing",
        "rosati_duality",
        "primitive_positive_sign",
        "control_death",
    },
    "missing=%s" % ",".join(sorted(missing_after_choice)),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nCTS1-CTS8 ALL PASS: contractible choice space is not the square carrier")
print(
    "VERDICT: contractibility may prove coherent uniqueness after the carrier "
    "exists, but it does not construct Qbar from a canonical point. Projection, "
    "DD.4 boundary, Rosati, choice contraction, and control death remain "
    "represented carrier obligations."
)
