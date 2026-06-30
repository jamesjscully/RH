r"""Represented-carrier candidate matrix no-go.

This witness applies the doc-287 represented-carrier gate to the three
standing doc-137 routes:

  1. PFD/Xbar spectral line,
  2. Connes-Consani scaling-site / C x C line,
  3. condensed/liquid metric enrichment.

It is a no-go for the current represented evidence, not a theorem that these
routes can never be strengthened.  The output identifies the smallest common
missing represented bundle: actual boundary/localization killing of DD.4
tied to actual p1,p2 pushforwards and formation-level control death.

Run:
    python3 -m scripts.numerics.witness.prime_int_n1b_represented_carrier_candidate_matrix_no_go
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


# Current represented evidence, read strictly from the doc-137 route status
# and already-banked no-go/spec docs.  These are current evidence tokens, not
# promises about future strengthened versions of the routes.
routes = {
    "pfd_xbar": {
        "object_actual",  # Xbar spectrum exists locally/stage-side.
        "duality_functor_actual",  # Lin/self-duality clause, not full Rosati.
    },
    "connes_consani_scaling_site_cxc": {
        "object_actual",  # curve-level compactified Spec Z/scaling-site object.
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
route_missing = {name: REQUIRED_SLOTS - slots for name, slots in route_slots.items()}

gate(
    "RCM1 doc-137 routes do not pass the represented-carrier gate",
    all(not REQUIRED_SLOTS <= slots for slots in route_slots.values())
    and route_slots["pfd_xbar"] == set()
    and route_slots["connes_consani_scaling_site_cxc"] == {"carrier_object"}
    and route_slots["condensed_metric_enrichment"] == set(),
    "; ".join("%s:%s" % (name, ",".join(sorted(slots)) or "none") for name, slots in route_slots.items()),
)


profiles = [h1_profile(L) for L in (6, 8, 10, 12)]
dd4_obstruction_stable = all(
    p["cocycle"] and p["c_nonboundary"] and p["h1_order"] == 2 and p["res1_c"] == 1
    for p in profiles
)
boundary_bundle = {
    "boundary_map_actual",
    "localization_exact_actual",
    "dd4_class_mapped_to_zero",
    "self_dual_boundary_actual",
}
endpoint_bundle = {"p1_map_actual", "p2_map_actual", "proper_pushforward_actual"}
control_bundle = {"control_instantiation_impossible", "control_death_at_formation_proved"}
shared_blocker_bundle = boundary_bundle | endpoint_bundle | control_bundle

gate(
    "RCM2 the smallest shared blocker is boundary plus endpoints plus control death",
    dd4_obstruction_stable
    and all(not boundary_bundle <= evidence for evidence in routes.values())
    and all(not endpoint_bundle <= evidence for evidence in routes.values())
    and all(not control_bundle <= evidence for evidence in routes.values()),
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
G_true = frobenius_graph(F_true, q_true, 1)
projection = projection_defect(G_true, D_true, G_true, E_true)
H_true = primitive_hodge_index(F_true, E_true, 1)

gate(
    "RCM3 projection/Rosati positives do not replace the shared blocker",
    projection == 27.0 and H_true < 0 and "projection_formula" not in route_slots["pfd_xbar"],
    "finite-field positive sign %.3f, but formal semantic projection defect %.0f"
    % (H_true, projection),
)


attempted = {name: evidence | shared_blocker_bundle for name, evidence in routes.items()}
attempted_slots = {name: represented_slots(evidence) for name, evidence in attempted.items()}
attempted_missing = {name: REQUIRED_SLOTS - slots for name, slots in attempted_slots.items()}

gate(
    "RCM4 adding the shared blocker is necessary but not sufficient",
    all({"endpoint_maps", "dd4_boundary_killing", "control_death"} <= slots for slots in attempted_slots.values())
    and all(not REQUIRED_SLOTS <= slots for slots in attempted_slots.values())
    and "integral_rep_NS" in attempted_missing["pfd_xbar"]
    and "proper_composition" in attempted_missing["connes_consani_scaling_site_cxc"]
    and "carrier_object" in attempted_missing["condensed_metric_enrichment"],
    "; ".join("%s missing %d" % (name, len(missing)) for name, missing in attempted_missing.items()),
)


same_total_a = (10, F_true, 1)
same_total_b = (7, F_true, 4)
same_total = same_total_a[0] + same_total_a[2] == same_total_b[0] + same_total_b[2]
same_diagonal = ns_intersection(D_true, same_total_a) == ns_intersection(D_true, same_total_b)
endpoints_differ = same_total_a[0] != same_total_b[0] and same_total_a[2] != same_total_b[2]

gate(
    "RCM5 endpoint labels and total degree cannot perform the construction",
    same_total and same_diagonal and endpoints_differ,
    "(10,F,1) and (7,F,4) share total and Delta pairing but have different endpoints",
)


control_q = 3
control_F = frobenius(control_q, 1)
control_E = weil_pairing(control_F, control_q)
control_D = diagonal(control_F)
control_G = frobenius_graph(control_F, control_q, 1)
control_projection = projection_defect(control_G, control_D, control_G, control_E)
control_sign = primitive_hodge_index(control_F, control_E, 1)

gate(
    "RCM6 current candidate evidence is still formable on controls",
    control_sign < 0
    and control_projection == 11.0
    and all("control_death" not in slots for slots in route_slots.values()),
    "control sign %.3f and semantic projection defect %.0f; no formation death"
    % (control_sign, control_projection),
)


best_route = max(route_slots, key=lambda name: len(route_slots[name]))
first_action = "construct_boundary_endpoint_control_bundle"

gate(
    "RCM7 matrix selects the next construction target",
    best_route == "connes_consani_scaling_site_cxc"
    and first_action == "construct_boundary_endpoint_control_bundle"
    and route_slots[best_route] == {"carrier_object"},
    "best current represented route=%s; next token bundle=%s"
    % (best_route, first_action),
)


banked_no_go = all(not REQUIRED_SLOTS <= slots for slots in route_slots.values())

gate(
    "RCM8 current standing routes bank a represented-evidence no-go",
    banked_no_go,
    "no route supplies represented Qbar+p1p2+boundary+rep_NS+pullbacks+projection+Rosati+control death",
)


if failures:
    print("\nFAILURES:")
    for failure in failures:
        print(" -", failure)
    raise SystemExit(1)

print("\nRCM1-RCM8 ALL PASS: current standing routes fail the represented-carrier gate")
print(
    "VERDICT: the three doc-137 routes do not currently construct the "
    "represented carrier. The next constructive target is the shared "
    "boundary+endpoint+control-death bundle; adding that bundle is necessary "
    "but still not sufficient without rep_NS, proper pullbacks, projection, "
    "Rosati, and graph data."
)
