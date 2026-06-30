r"""CC product boundary-endpoint bundle no-go.

Doc 288 selected the shared boundary+endpoint+control-death bundle as the
next construction target, with Connes-Consani/C x C the best current route
only because it has curve-level object evidence.  This witness tests the
first repair:

    promote the curve-level/product boundary and product projections to the
    represented square bundle.

The positive fact is real: a product-shaped compactification can supply the
right names for boundary and p1,p2.  The no-go is that product boundary and
endpoint data alone do not map the DD.4 class to zero, do not construct
rep_NS/proper square correspondences/projection/Rosati/graph data, and do
not make controls die at carrier formation.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_cc_product_boundary_endpoint_bundle_no_go
"""

from math import comb, gcd, log2

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


cc_curve_evidence = {
    "object_actual",
    "open_actual",
    "boundary_actual",
    "duality_functor_actual",
    "duality_involutive_proved",
}
cc_curve_slots = represented_slots(cc_curve_evidence)

gate(
    "CBE1 CC curve-level evidence is still only a carrier-object token",
    cc_curve_slots == {"carrier_object"},
    "represented slots=%s" % ",".join(sorted(cc_curve_slots)),
)


product_endpoint_evidence = cc_curve_evidence | {
    "p1_map_actual",
    "p2_map_actual",
    "proper_pushforward_actual",
}
product_endpoint_slots = represented_slots(product_endpoint_evidence)

gate(
    "CBE2 product projections add endpoint maps but not the square bundle",
    product_endpoint_slots == {"carrier_object", "endpoint_maps"},
    "represented slots=%s" % ",".join(sorted(product_endpoint_slots)),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
primitive_functionals = [
    (a, b)
    for a in range(-2, 3)
    for b in range(-2, 3)
    if (a, b) != (0, 0) and gcd(abs(a), abs(b)) == 1
]

gate(
    "CBE3 product normal crossings do not select the DD.4 direction",
    all(p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1 for p in profiles)
    and len(primitive_functionals) == 16,
    "primitive directions in [-2,2]^2=%d; "
    % len(primitive_functionals)
    + "  ".join(
        "L%d:|B|=2^%d|Z1|=2^%d|H1|=%d"
        % (p["L"], int(log2(p["b_order"])), int(log2(p["z1_order"])), p["h1_order"])
        for p in profiles
    ),
)


declared_boundary_evidence = product_endpoint_evidence | {
    "boundary_map_declared",
    "localization_exact_declared",
    "dd4_class_mapped_to_zero_declared",
    "self_dual_boundary_declared",
}
declared_boundary_slots = represented_slots(declared_boundary_evidence)

gate(
    "CBE4 declared product boundary localization is not represented DD.4 killing",
    "dd4_boundary_killing" not in declared_boundary_slots
    and declared_boundary_slots == {"carrier_object", "endpoint_maps"},
    "represented slots=%s" % ",".join(sorted(declared_boundary_slots)),
)


q_true = 7
F_true = frobenius(q_true, 1)
E_true = weil_pairing(F_true, q_true)
D_true = diagonal(F_true)
G_true = frobenius_graph(F_true, q_true, 1)
H_true = primitive_hodge_index(F_true, E_true, 1)
projection = projection_defect(G_true, D_true, G_true, E_true)

gate(
    "CBE5 product endpoints do not construct rep_NS, graph, or projection",
    "integral_rep_NS" not in product_endpoint_slots
    and "frobenius_graph" not in product_endpoint_slots
    and "projection_formula" not in product_endpoint_slots
    and ns_intersection(D_true, G_true) == 7
    and projection == 27.0
    and H_true < 0,
    "finite-field count anchor exists separately; semantic projection defect %.0f"
    % projection,
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)

control_product_evidence = declared_boundary_evidence | {"control_death_guard_declared"}
control_product_slots = represented_slots(control_product_evidence)

gate(
    "CBE6 product boundary-endpoint package remains formable on controls",
    control_product_slots == {"carrier_object", "endpoint_maps"}
    and "control_death" not in control_product_slots
    and control_projection == 11.0
    and control_sign < 0,
    "control slots=%s projection_defect=%.0f sign=%.3f"
    % (",".join(sorted(control_product_slots)), control_projection, control_sign),
)


full_blocker_evidence = product_endpoint_evidence | {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
    "control_instantiation_impossible",
    "control_death_at_formation_proved",
}
full_blocker_slots = represented_slots(full_blocker_evidence)
full_blocker_missing = REQUIRED_SLOTS - full_blocker_slots

gate(
    "CBE7 even a represented blocker bundle is necessary but insufficient",
    full_blocker_slots
    == {"carrier_object", "endpoint_maps", "dd4_boundary_killing", "control_death"}
    and full_blocker_missing
    == {
        "integral_rep_NS",
        "diagonal",
        "frobenius_graph",
        "proper_composition",
        "projection_formula",
        "rosati_duality",
        "primitive_positive_sign",
    },
    "slots=%s missing=%s"
    % (",".join(sorted(full_blocker_slots)), ",".join(sorted(full_blocker_missing))),
)


gate(
    "CBE8 CC product boundary-endpoint repair does not pass RCG",
    not REQUIRED_SLOTS <= product_endpoint_slots
    and not REQUIRED_SLOTS <= declared_boundary_slots
    and not REQUIRED_SLOTS <= full_blocker_slots,
    "product endpoints/declarations/full blocker all remain below carrier contract",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nCBE1-CBE8 ALL PASS: CC product boundary-endpoint bundle is not the square carrier")
print(
    "VERDICT: product boundary and p1,p2 data are the right shape, but they "
    "do not by themselves map the DD.4 class to zero, construct rep_NS or "
    "proper square correspondences, prove projection/Rosati/graph data, or "
    "kill controls at formation."
)
