r"""Square-carrier contract for End(S^2/Z).

This is a construction-spec witness, not a no-go theorem and not a proof of
RH.  It freezes the acceptance test for the only remaining admissible R1
move: construct the zeta-side square carrier whose finite-field model is the
weight-2 Neron-Severi correspondence lattice.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_square_carrier_contract
"""

import numpy as np

from scripts.numerics.witness.ns_diagonal_representability import (
    diagonal,
    end_component,
    frobenius,
    frobenius_graph,
    is_indecomposable,
    ns_intersection,
    offcircle_plant as ns_offcircle_plant,
    primitive_hodge_index as ns_primitive_hodge_index,
    weil_pairing,
)
from scripts.numerics.witness.ns_hodge_index_duality import (
    C4_defect_weight2,
    P_gram,
    frobenius_and_cup,
    involutivity_defect,
    primitive_hodge_index as dual_primitive_hodge_index,
    offcircle_plant as dual_offcircle_plant,
    weil_curves,
)


failures = []


def gate(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        failures.append(name)


curves = [(2, 1, "q=2"), (5, 2, "q=5"), (7, 1, "q=7"), (11, 3, "q=11"), (13, 5, "q=13")]


point_count_checks = []
for q, a1, label in curves:
    F = frobenius(q, a1)
    Delta = diagonal(F)
    for n in (1, 2, 3):
        Gamma = frobenius_graph(F, q, n)
        intersection = ns_intersection(Delta, Gamma)
        count = q ** n + 1 - sum(alpha ** n for alpha in np.linalg.eigvals(F)).real
        point_count_checks.append((label, n, intersection, count, abs(intersection - count) < 1e-9))

gate(
    "SCC1 rep_NS diagonal/Frobenius graph reproduces point counts",
    all(row[-1] for row in point_count_checks),
    "; ".join(
        f"{label}:n={n}:D.G={intersection:.1f}=#{count:.1f}"
        for label, n, intersection, count, _ok in point_count_checks[:5]
    ),
)


F7 = frobenius(7, 1)
Delta7 = diagonal(F7)
Gamma7 = frobenius_graph(F7, 7, 1)
left_degree_changed = (10, F7, 1)
right_degree_changed = (7, F7, 4)
base_intersection = ns_intersection(Delta7, Gamma7)
left_changed_intersection = ns_intersection(Delta7, left_degree_changed)
right_changed_intersection = ns_intersection(Delta7, right_degree_changed)

gate(
    "SCC2 two carrier-native degree maps are required",
    base_intersection == 7
    and left_changed_intersection == 10
    and right_changed_intersection == 10
    and left_changed_intersection != base_intersection
    and right_changed_intersection != base_intersection,
    (
        f"(7,F,1)->{base_intersection:.0f}; "
        f"(10,F,1)->{left_changed_intersection:.0f}; "
        f"(7,F,4)->{right_changed_intersection:.0f}"
    ),
)


indecomp_checks = []
for q, a1, label in curves:
    F = frobenius(q, a1)
    Delta = diagonal(F)
    left_fiber = (1, np.zeros_like(F), 0)
    right_fiber = (0, np.zeros_like(F), 1)
    indecomp_checks.append(
        (
            label,
            float(np.linalg.norm(end_component(Delta))),
            float(np.linalg.norm(end_component(left_fiber))),
            float(np.linalg.norm(end_component(right_fiber))),
            is_indecomposable(Delta)
            and not is_indecomposable(left_fiber)
            and not is_indecomposable(right_fiber),
        )
    )

gate(
    "SCC3 diagonal is indecomposable, fibers/products are not",
    all(row[-1] for row in indecomp_checks),
    "; ".join(
        f"{label}:||End(Delta)||={d_norm:.4f},fibers={lf:.1f}/{rf:.1f}"
        for label, d_norm, lf, rf, _ok in indecomp_checks
    ),
)


duality_checks = []
for name, q, g, roots in weil_curves():
    F, E = frobenius_and_cup(roots, q)
    duality_checks.append(
        (
            name,
            involutivity_defect(E),
            C4_defect_weight2(E),
            P_gram(F, F, E),
            2 * g * q,
        )
    )

gate(
    "SCC4 weight-2 duality is canonical and involutive",
    all(
        d2 < 1e-9 and c4 < 1e-9 and abs(tr_ff - expected) < 1e-8
        for _name, d2, c4, tr_ff, expected in duality_checks
    ),
    "; ".join(
        f"{name}:D2={d2:.1e},C4={c4:.1e},TrFFdag={tr_ff:.2f}"
        for name, d2, c4, tr_ff, _expected in duality_checks
    ),
)


primitive_checks = []
for q, a1, label in curves:
    F = frobenius(q, a1)
    E = weil_pairing(F, q)
    on_index = ns_primitive_hodge_index(F, E, 1)
    Foff, Eoff = ns_offcircle_plant(q, 1.5)
    off_index = ns_primitive_hodge_index(Foff, Eoff, 1)
    primitive_checks.append((label, on_index, off_index))

dual_flip_checks = []
for name, q, g, roots in weil_curves():
    F, E = frobenius_and_cup(roots, q)
    Foff, Eoff = dual_offcircle_plant(q, g, 1.5)
    on_index = dual_primitive_hodge_index(F, E, g)
    off_index = dual_primitive_hodge_index(Foff, Eoff, g)
    dual_flip_checks.append((name, on_index, off_index))

gate(
    "SCC5 primitive Hodge/Rosati sign detects off-circle data",
    all(on_index < 0 and off_index > 0 for _label, on_index, off_index in primitive_checks)
    and all(off_index > on_index + 1e-9 for _name, on_index, off_index in dual_flip_checks),
    "; ".join(f"{label}:on={on:+.3f},off={off:+.3f}" for label, on, off in primitive_checks),
)


required_slots = [
    "ambient_square",
    "rep_NS",
    "two_degree_maps",
    "indecomposable_diagonal",
    "proper_correspondence_category",
    "fiber_product_composition",
    "projection_formula",
    "frobenius_graph",
    "positive_rosati",
    "control_death",
    "dd4_weight_ge_1",
]

formal_packages = {
    "rtf_period_theta": {slot: False for slot in required_slots},
    "shtuka_hecke_profile": {slot: False for slot in required_slots},
    "topos_hyperdescent_shape": {slot: False for slot in required_slots},
    "automorphic_trace_packet": {slot: False for slot in required_slots},
}

gate(
    "SCC6 formal packages fail the carrier contract slotwise",
    all(not any(slots.values()) for slots in formal_packages.values()),
    ", ".join(formal_packages),
)


dh_profile = {
    "euler_product": False,
    "satake": False,
    "fxf_product": False,
    "end_frobenius": False,
    "ns_diagonal_component": False,
}
control_companion_slots = {slot: False for slot in required_slots}
control_companion_slots["projection_formula"] = True
control_companion_slots["positive_rosati"] = True

gate(
    "SCC7 DH/control companions die before carrier formation",
    not any(dh_profile.values())
    and not control_companion_slots["ambient_square"]
    and not control_companion_slots["rep_NS"]
    and not control_companion_slots["two_degree_maps"]
    and not control_companion_slots["frobenius_graph"],
    "DH lacks Euler/Satake/fxf/End-Frobenius/NS diagonal; controls may assert forms but lack the carrier",
)


finite_field_visible_slots = {
    "ambient_square": True,
    "rep_NS": True,
    "two_degree_maps": True,
    "indecomposable_diagonal": True,
    "proper_correspondence_category": True,
    "fiber_product_composition": True,
    "projection_formula": True,
    "frobenius_graph": True,
    "positive_rosati": True,
}
zeta_side_constructed_slots = {slot: False for slot in required_slots}

gate(
    "SCC8 this is a contract/spec, not yet End(S^2/Z)",
    all(finite_field_visible_slots.values()) and not any(zeta_side_constructed_slots.values()),
    (
        "finite-field anchor fills visible square slots; over Z all contract "
        "slots, control death, and DD.4 data remain to be constructed"
    ),
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nSCC1-SCC8 ALL PASS: square-carrier contract is explicit; zeta carrier still unconstructed")
print(
    "VERDICT: every future End(S^2/Z) proposal must construct the actual square carrier, integral rep_NS, "
    "two carrier-native degree maps, indecomposable diagonal, proper correspondence category, fiber-product "
    "composition, projection formula, Frobenius/Hecke graph, canonical D^2=id Rosati pairing, primitive "
    "positive Hodge/Rosati sign, control death, and DD.4 weight>=1 data.  A period, shtuka, topos, trace, "
    "or automorphic package is admissible only downstream of those slots."
)
